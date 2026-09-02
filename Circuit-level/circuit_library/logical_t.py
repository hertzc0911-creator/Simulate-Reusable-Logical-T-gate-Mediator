import stim

from .configs import logical_t_d3, logical_t_d5, logical_t_d7
from .sequence_specs import LOGICAL_T_SEQUENCE_CONSTANTS, LOGICAL_T_SEQUENCE_SPECS


_CONFIGS = {3: logical_t_d3, 5: logical_t_d5, 7: logical_t_d7}
_ACTIVE_SEQUENCE_SPECS = {}


def pauli_targets(pauli_string, pauli_type):
    text = str(pauli_string).lstrip("+-")
    return [qubit for qubit, pauli in enumerate(text) if pauli == pauli_type]


def pauli_string_type(pauli_string):
    text = str(pauli_string).lstrip("+-")
    non_identity = {pauli for pauli in text if pauli != "_"}
    if non_identity == {"Z"}:
        return "Z"
    if non_identity == {"X"}:
        return "X"
    raise ValueError(f"Expected a Z-only or X-only PauliString, got {pauli_string!r}.")


def pauli_weight(pauli_string):
    pauli_type = pauli_string_type(pauli_string)
    return len(pauli_targets(pauli_string, pauli_type))


def parse_flag_data_sequence(text):
    import re
    return [(kind, int(index) - 1) for kind, index in re.findall(r"([FD])(\d+)", text)]


def run_flag_data_sequence(circuit, pauli_string, expected_type, expected_weight,
                           sequence_text, flag_count, ancilla, flag, error_rate,
                           reset_flag_count=None):
    pauli_type = pauli_string_type(pauli_string)
    targets = pauli_targets(pauli_string, pauli_type)
    if pauli_type != expected_type or len(targets) != expected_weight:
        raise ValueError(
            f"Expected weight-{expected_weight} {expected_type}, "
            f"got weight-{len(targets)} {pauli_type}.")
    if reset_flag_count is None:
        reset_flag_count = flag_count
    required_flags = max(flag_count, reset_flag_count)
    if len(flag) < required_flags:
        raise ValueError(f"This circuit needs {required_flags} flag qubits, got {len(flag)}.")

    used_flags = flag[:flag_count]
    circuit.append("RX", [ancilla])
    circuit.append("R", flag[:reset_flag_count])
    data_gate = "CX" if pauli_type == "X" else "CZ"
    for kind, index in parse_flag_data_sequence(sequence_text):
        if kind == "F":
            pair = [ancilla, used_flags[index]]
            circuit.append("CX", pair)
        else:
            pair = [ancilla, targets[index]]
            circuit.append(data_gate, pair)
        circuit.append("DEPOLARIZE2", pair, error_rate)
    for flag_qubit in used_flags:
        circuit.append("M", [flag_qubit], arg=error_rate)
        circuit.append("DETECTOR", [stim.target_rec(-1)])
    circuit.append("MX", [ancilla], arg=error_rate)
    return circuit


def _weighted_mpp(circuit, pauli_string, pauli_type, weight, ancilla, flag, error_rate):
    try:
        sequence, flag_count, reset_flag_count = _ACTIVE_SEQUENCE_SPECS[(pauli_type, weight)]
    except KeyError as exc:
        raise ValueError(f"No {pauli_type} weight-{weight} flag sequence is configured.") from exc
    return run_flag_data_sequence(
        circuit, pauli_string, pauli_type, weight, sequence, flag_count,
        ancilla, flag, error_rate, reset_flag_count=reset_flag_count)


def _make_weighted_mpp(pauli_type, weight):
    def weighted_mpp(circuit, pauli_string, ancilla, flag, error_rate):
        return _weighted_mpp(
            circuit, pauli_string, pauli_type, weight,
            ancilla, flag, error_rate)
    weighted_mpp.__name__ = f"MPP_circuit_{pauli_type}_weight_{weight}"
    weighted_mpp.__qualname__ = weighted_mpp.__name__
    return weighted_mpp


for _pauli_type in ("X", "Z"):
    for _weight in (3, 4, 5, 6, 7, 8, 9, 12, 13, 18, 19, 24, 25):
        _name = f"MPP_circuit_{_pauli_type}_weight_{_weight}"
        globals()[_name] = _make_weighted_mpp(_pauli_type, _weight)


def MPP_circuit(circuit, pauli_string, ancilla, flag, error):
    pauli_type = pauli_string_type(pauli_string)
    weight = pauli_weight(pauli_string)
    try:
        mpp_circuit = MPP_CIRCUITS_BY_TYPE_AND_WEIGHT[pauli_type][weight]
    except KeyError as exc:
        supported = sorted(MPP_CIRCUITS_BY_TYPE_AND_WEIGHT.get(pauli_type, {}))
        raise ValueError(
            f"No MPP_circuit_{pauli_type}_weight_{weight} is configured. "
            f"Supported {pauli_type} weights are {supported}.") from exc
    return mpp_circuit(circuit, pauli_string, ancilla, flag, error)


def count_added_flag_measurements(stabilizers):
    """Count flag outcomes added before the syndrome outcomes."""
    if isinstance(stabilizers, dict):
        stabilizers = stabilizers.values()

    total = 0
    for stabilizer in stabilizers:
        temp = stim.Circuit()
        MPP_circuit(
            temp, stabilizer,
            ancilla=DEFAULT_SYNDROME_ANCILLA,
            flag=DEFAULT_FLAG_QUBITS,
            error=0,
        )
        # Every MPP_circuit has one syndrome-ancilla measurement; all other measurement results in it belong to flags.
        
        total += temp.num_measurements - 1
    return total


def flag_adjusted_target_rec(original_distance, stabilizers_measured_so_far):
    """Return the old rec target shifted past intervening flag outcomes.

    original_distance is the positive distance used before flags, e.g.
    num_ancilla + 1.  Pass the stabilizers already measured in the current
    loop, including the current stabilizer.
    """
    added_flags = count_added_flag_measurements(stabilizers_measured_so_far)
    return stim.target_rec(-(original_distance + added_flags))


def count_measurements_for_stabilizers(stabilizers, error_rate):
    total = 0
    for stabilizer in stabilizers.values():
        temp = stim.Circuit()
        MPP_circuit(
            temp, stabilizer,
            ancilla=DEFAULT_SYNDROME_ANCILLA,
            flag=DEFAULT_FLAG_QUBITS,
            error=error_rate,
        )
        total += temp.num_measurements
    return total


def target_rec_from_previous_stabilizer_round(
        previous_stabilizers, stabilizer_name, current_measurements_so_far):
    """Locate a named syndrome in the immediately preceding flagged round."""
    previous_round_measurements = 0
    previous_syndrome_position = None

    for name, stabilizer in previous_stabilizers.items():
        temp = stim.Circuit()
        MPP_circuit(
            temp, stabilizer,
            ancilla=DEFAULT_SYNDROME_ANCILLA,
            flag=DEFAULT_FLAG_QUBITS,
            error=0,
        )
        previous_round_measurements += temp.num_measurements
        if name == stabilizer_name:
            # The syndrome ancilla is the final measurement of MPP_circuit.
            previous_syndrome_position = previous_round_measurements

    if previous_syndrome_position is None:
        raise KeyError(
            f"{stabilizer_name!r} is not in the previous stabilizer round.")

    distance = (
        previous_round_measurements
        - previous_syndrome_position
        + current_measurements_so_far
        + 1
    )
    return stim.target_rec(-distance)


def Stabilizers_measurement_general(error_rate, tick_num, After_merging=False,After_merging_string=False):


    c = stim.Circuit()
    num_measurements_per_round = count_measurements_for_stabilizers(
        stabilizers_general, error_rate)

    if After_merging:
        
        num_ancilla = len(stabilizers_k_z_enlargable)

        # Keep the prefix so rec offsets include all flag measurements
        # inserted before each current syndrome measurement.
        stabilizers_measured_so_far = []

        # k_x: stay the same
        for name, stabilizer in stabilizers_k_x.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged, name,
                        num_ancilla + c.num_measurements)  # Previous merged-round measurement
                ], tag=f"Det_{name}_general_{tick_num}")


        # k_z_enlargable + ancilla = k_z_enlargabled
        for name, stabilizer in stabilizers_k_z_enlargable.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    flag_adjusted_target_rec(
                        num_ancilla + len(stabilizers_k_x) + 1, stabilizers_measured_so_far),  # Ancilla measurement
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged, name,
                        num_ancilla + c.num_measurements)  # Previous merged-round measurement
                ], tag=f"Det_{name}_general_{tick_num}")

        # k_z_unchange: stay the same
        for name, stabilizer in stabilizers_k_z_unchange.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged, name,
                        num_ancilla + c.num_measurements)  # Previous merged-round measurement
                ], tag=f"Det_{name}_general_{tick_num}")

        # s_x: stay the same
        for name, stabilizer in stabilizers_s_x.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate); stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged, name,
                        num_ancilla + c.num_measurements)  # Previous merged-round measurement
                ], tag=f"Det_{name}_general_{tick_num}")

            
    
        # s_z + ancilla = k_z_enlargabled
        len_s_z = len(stabilizers_k_z_enlargable) + len(stabilizers_k_z_unchange) + len(stabilizers_k_x) + len(stabilizers_s_x)
        for name, stabilizer in stabilizers_s_z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    flag_adjusted_target_rec(
                        num_ancilla + len_s_z + 1,
                        stabilizers_measured_so_far),  # Ancilla measurement
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged, name,
                        num_ancilla + c.num_measurements)  # Previous merged-round measurement
                ], tag=f"Det_{name}_general_{tick_num}")

            
    elif After_merging_string:


        num_ancilla = len(stabilizers_k_x_enlargable)
        stabilizers_measured_so_far = []
        
        # k_x_enlargable + ancilla = k_x_enlargabled
        # The enlargable k_x block is measured first.
        for name, stabilizer in stabilizers_k_x_enlargable.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    flag_adjusted_target_rec(
                        num_ancilla + 1,
                        stabilizers_measured_so_far),  # Ancilla measurement
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged_string, name,
                        num_ancilla + c.num_measurements)  # Previous string-merged measurement
                ], tag=f"Det_{name}_general_{tick_num}")

        # k_x_unchange: stay the same
        for name, stabilizer in stabilizers_k_x_unchange.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged_string, name,
                        num_ancilla + c.num_measurements)  # Previous string-merged measurement
                ], tag=f"Det_{name}_general_{tick_num}")     

        # k_z: stay the same
        for name, stabilizer in stabilizers_k_z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged_string, name,
                        num_ancilla + c.num_measurements)  # Previous string-merged measurement
                ], tag=f"Det_{name}_general_{tick_num}")
            
        # s_x_enlargable + ancilla = s_x_enlargabled
        len_s_x = len(stabilizers_k_z) + len(stabilizers_k_x_enlargable) + len(stabilizers_k_x_unchange)
        for name, stabilizer in stabilizers_s_x_enlargable.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [
                    stim.target_rec(-1),                    # Current measurement  
                    flag_adjusted_target_rec(
                        num_ancilla + len_s_x + 1,
                        stabilizers_measured_so_far),  # Ancilla measurement
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged_string, name,
                        num_ancilla + c.num_measurements)  # Previous string-merged measurement
                ], tag=f"Det_{name}_general_{tick_num}")

        # s_x_unchange: stay the same        
        for name, stabilizer in stabilizers_s_x_unchange.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged_string, name,
                        num_ancilla + c.num_measurements)  # Previous string-merged measurement
                ], tag=f"Det_{name}_general_{tick_num}")    
 
        

        # s_z: stay the same
        for name, stabilizer in stabilizers_s_z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            stabilizers_measured_so_far.append(stabilizer)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_merged_string, name,
                        num_ancilla + c.num_measurements)  # Previous string-merged measurement
                ], tag=f"Det_{name}_general_{tick_num}")
        
    else:
        for name, stabilizer in stabilizers_general.items():
            MPP_circuit(
                c, stabilizer,
                ancilla=DEFAULT_SYNDROME_ANCILLA,
                flag=DEFAULT_FLAG_QUBITS,
                error=error_rate,
            )
            if tick_num != 1:
                c.append("DETECTOR", [
                    stim.target_rec(-1),
                    stim.target_rec(-(num_measurements_per_round + 1)),
                ], tag=f"Det_{name}_general_{tick_num}")
    return c


def Stabilizers_measurement_merged(error_rate, tick_num, First_merging_round=False, offset=0, Observable_list_XX=None):
    
    c = stim.Circuit()
    num_measurements_per_round = count_measurements_for_stabilizers(stabilizers_merged, error_rate)

    if First_merging_round:
        for name, stabilizer in stabilizers_added_X.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
        
        for name, stabilizer in stabilizers_merged_without_add_X.items():  
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_general, name, c.num_measurements)  # Previous general-round measurement
                ], tag=f"Det_{name}_merged_{tick_num}")
  

    elif Observable_list_XX is not None:
        for name, stabilizer in stabilizers_added_X.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")
            Observable_list_XX.append(c.num_measurements - 1 + offset)
        for name, stabilizer in stabilizers_merged_without_add_X.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")

            
    else:
        for name, stabilizer in stabilizers_merged.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")

    return c


def Stabilizers_measurement_merged_string(error_rate, tick_num, First_merging_round=False, offset=0, Observable_list_ZZ=None):
    c = stim.Circuit()
    num_measurements_per_round = count_measurements_for_stabilizers(
        stabilizers_merged_string, error_rate)

    if First_merging_round:
        for name, stabilizer in stabilizers_added_Z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
        
        for name, stabilizer in stabilizers_merged_string_without_add_Z.items():  
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_general, name, c.num_measurements)  # Previous general-round measurement
                ], tag=f"Det_{name}_merged_{tick_num}")

    

    elif Observable_list_ZZ is not None:
        for name, stabilizer in stabilizers_added_Z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")
            Observable_list_ZZ.append(c.num_measurements - 1 + offset)
        for name, stabilizer in stabilizers_merged_string_without_add_Z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")
            if name in stabilizer_global:
                Observable_list_ZZ.append(c.num_measurements - 1 + offset)

            

    else:
        for name, stabilizer in stabilizers_merged_string.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")

    return c

def detector_k_x(circuit, name, tick_num, previous_stabilizers,
                 current_syndrome_positions, append_dependencies):
    """Add current k_x, its current k_z factors, and previous k_x."""
    def current_target(stabilizer_name):
        try:
            position = current_syndrome_positions[stabilizer_name]
        except KeyError as exc:
            raise KeyError(
                f"Current syndrome {stabilizer_name!r} has not been measured.") from exc
        return stim.target_rec(-(circuit.num_measurements - position + 1))

    targets = [current_target(name)]
    for dependency_name in append_dependencies[name].split('+'):
        targets.append(current_target(dependency_name.strip()))

    targets.append(target_rec_from_previous_stabilizer_round(
        previous_stabilizers, name, circuit.num_measurements))
    circuit.append("DETECTOR", targets, tag=f"Det_{name}_general_{tick_num}")

def Stabilizers_measurement_general_after_gate(error_rate, tick_num, After_CZ=False, After_S_3D=False, After_H_2D=False):
    c = stim.Circuit()
    num_measurements_per_round = count_measurements_for_stabilizers(
        stabilizers_general, error_rate)

    if After_CZ:
        # Save the one-based position of every syndrome outcome in this
        # local circuit.  c.num_measurements includes all flag outcomes.
        current_syndrome_positions = {}

        # k_x: k_x goes to k_x + s_z
        for name, stabilizer in stabilizers_k_x.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            current_syndrome_positions[name] = c.num_measurements

    
        # k_z: stay the same
        for name, stabilizer in stabilizers_k_z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            current_syndrome_positions[name] = c.num_measurements
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
            

        # s_x:  goes to s_x + k_z
        k_z_names = list(stabilizers_k_z)
        for i, (name, stabilizer) in enumerate(stabilizers_s_x.items()):
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            current_syndrome_positions[name] = c.num_measurements
            paired_k_z_position = current_syndrome_positions[k_z_names[i]]
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec(-(
                        c.num_measurements - paired_k_z_position + 1)),  # Current k_z measurement
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
            
        # s_z: stay the same
        for name, stabilizer in stabilizers_s_z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            current_syndrome_positions[name] = c.num_measurements
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")   
            
        # detector of k_x: 
        s_z_names = list(stabilizers_s_z)
        for i, (name, stabilizer) in enumerate(list(stabilizers_k_x.items())[:len(stabilizers_s_z)]):
            current_k_x_position = current_syndrome_positions[name]
            current_s_z_position = current_syndrome_positions[s_z_names[i]]
            c.append("DETECTOR", [  
                    stim.target_rec(-(
                        c.num_measurements - current_k_x_position + 1)),  # Current k_x measurement
                    stim.target_rec(-(
                        c.num_measurements - current_s_z_position + 1)),  # Current s_z measurement
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_general, name, c.num_measurements)  # Previous k_x measurement
                ], tag=f"Det_{name}_general_{tick_num}")
        for i, (name, stabilizer) in enumerate(list(stabilizers_k_x.items())[len(stabilizers_s_z):]):
            current_k_x_position = current_syndrome_positions[name]
            c.append("DETECTOR", [  
                    stim.target_rec(-(
                        c.num_measurements - current_k_x_position + 1)),  # Current k_x measurement
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_general, name, c.num_measurements)  # Previous k_x measurement
                ], tag=f"Det_{name}_general_{tick_num}")   

            
    if After_S_3D:  
        current_syndrome_positions = {}

        # k_x: goes to k_x + k_z + k_z
        for name, stabilizer in stabilizers_k_x.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            current_syndrome_positions[name] = c.num_measurements
        # k_z: stay the same
        for name, stabilizer in stabilizers_k_z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            current_syndrome_positions[name] = c.num_measurements
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")


        for kx_name in S_gate_track.keys():
            detector_k_x(
                c, kx_name, tick_num,
                stabilizers_general, current_syndrome_positions, S_gate_track)
            
        
        # s_x:  stay the same
        for name, stabilizer in stabilizers_s_x.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
            
        # s_z: stay the same
        for name, stabilizer in stabilizers_s_z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")   
        


        
    if After_H_2D:
        # k_x: stay the same
        for name, stabilizer in stabilizers_k_x.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")


        # k_z: stay the same
        for name, stabilizer in stabilizers_k_z.items():
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
            
        # s_x: goes to s_z
        s_z_names = list(stabilizers_s_z)
        if len(stabilizers_s_x) != len(s_z_names):
            raise ValueError("After_H_2D requires one s_z partner for each s_x.")
        for i, (name, stabilizer) in enumerate(stabilizers_s_x.items()):
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_general, s_z_names[i],
                        c.num_measurements)  # Previous s_z measurement
                ], tag=f"Det_{name}_general_{tick_num}")

            
        # s_z: goes to s_x
        s_x_names = list(stabilizers_s_x)
        for i, (name, stabilizer) in enumerate(stabilizers_s_z.items()):
            MPP_circuit(c, stabilizer, ancilla=DEFAULT_SYNDROME_ANCILLA, flag=DEFAULT_FLAG_QUBITS, error=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    target_rec_from_previous_stabilizer_round(
                        stabilizers_general, s_x_names[i],
                        c.num_measurements)  # Previous s_x measurement
                ], tag=f"Det_{name}_general_{tick_num}")

    return c


def lattice_surgery_Merge():
    return stim.Circuit()


def lattice_surgery_Split(error_rate):
    circuit = stim.Circuit()
    circuit.append("M", FACE_ANCILLAS, tag="Measurement_ancilla", arg=error_rate)
    return circuit


def lattice_surgery_Merge_string():
    circuit = stim.Circuit()
    circuit.append("R", STRING_ANCILLAS)
    circuit.append("H", STRING_ANCILLAS)
    return circuit


def lattice_surgery_Split_string(error_rate):
    circuit = stim.Circuit()
    circuit.append("MX", STRING_ANCILLAS, tag="Measurement_ancilla_string", arg=error_rate)
    return circuit


def lattice_surgery_Reset_string():
    circuit = stim.Circuit()
    circuit.append("R", STRING_ANCILLAS)
    return circuit


def measure_logical_qubits_3D():
    circuit = stim.Circuit()
    circuit.append("MPP", stim.PauliString(LOGICAL_3D_PAULI), tag="logical_qubits_3D")
    circuit.append("OBSERVABLE_INCLUDE", [stim.target_rec(-1)], 0)
    return circuit


def measure_logical_qubits_2D():
    circuit = stim.Circuit()
    circuit.append("MPP", stim.PauliString(LOGICAL_2D_PAULI), tag="logical_qubits_2D")
    circuit.append("OBSERVABLE_INCLUDE", [stim.target_rec(-1)], 1)
    return circuit


def measurement_XX():
    circuit = stim.Circuit()
    for pauli, tag in MEASUREMENT_XX_PRODUCTS:
        circuit.append("MPP", stim.PauliString(pauli), tag=tag)
    circuit.append("OBSERVABLE_INCLUDE", [stim.target_rec(-1), stim.target_rec(-2)], 0)
    return circuit


def measurement_ZZ():
    circuit = stim.Circuit()
    circuit.append("MPP", stim.PauliString(LOGICAL_3D_PAULI), tag="logical_qubits_3D")
    circuit.append("MPP", stim.PauliString(LOGICAL_2D_PAULI), tag="logical_qubits_2D")
    circuit.append("OBSERVABLE_INCLUDE", [stim.target_rec(-1), stim.target_rec(-2)], 0)
    return circuit


def S_Z_Gate():
    circuit = stim.Circuit()
    circuit.append("SQRT_Z", V_even)
    circuit.append("SQRT_Z_DAG", V_odd)
    return circuit


def S_Z_DAG_Gate():
    circuit = stim.Circuit()
    circuit.append("SQRT_Z_DAG", V_odd)
    circuit.append("SQRT_Z", V_even)
    return circuit


def logical_CZ():
    circuit = stim.Circuit()
    circuit.append("CZ", [qubit for pair in LOGICAL_CZ_PAIRS for qubit in pair])
    return circuit


def configure(distance):
    global _ACTIVE_SEQUENCE_SPECS, MPP_CIRCUITS_BY_TYPE_AND_WEIGHT
    if distance not in _CONFIGS:
        raise ValueError(f"Unsupported distance {distance}; choose 3, 5, or 7.")
    config = _CONFIGS[distance]
    for name in config.__all__:
        globals()[name] = getattr(config, name)
    _ACTIVE_SEQUENCE_SPECS = LOGICAL_T_SEQUENCE_SPECS[distance]
    for name, value in LOGICAL_T_SEQUENCE_CONSTANTS[distance].items():
        globals()[name] = value
    MPP_CIRCUITS_BY_TYPE_AND_WEIGHT = {"X": {}, "Z": {}}
    for pauli_type, weight in _ACTIVE_SEQUENCE_SPECS:
        name = f"MPP_circuit_{pauli_type}_weight_{weight}"
        MPP_CIRCUITS_BY_TYPE_AND_WEIGHT[pauli_type][weight] = globals()[name]

    exports = {name: getattr(config, name) for name in config.__all__}
    exports.update(LOGICAL_T_SEQUENCE_CONSTANTS[distance])
    exports["MPP_CIRCUITS_BY_TYPE_AND_WEIGHT"] = MPP_CIRCUITS_BY_TYPE_AND_WEIGHT
    for name, value in globals().items():
        if callable(value) and getattr(value, "__module__", None) == __name__ and not name.startswith("_"):
            exports[name] = value
    return exports
