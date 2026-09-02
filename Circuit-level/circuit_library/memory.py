import stim

from .configs import memory_d3, memory_d5, memory_d7
from .sequence_specs import MEMORY_SEQUENCE_CONSTANTS, MEMORY_SEQUENCE_SPECS


_CONFIGS = {3: memory_d3, 5: memory_d5, 7: memory_d7}
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


def x_pauli_targets(pauli_string):
    return pauli_targets(pauli_string, "Z")


def z_pauli_targets(pauli_string):
    return pauli_targets(pauli_string, "X")


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
    sequence, flag_count, reset_flag_count = _ACTIVE_SEQUENCE_SPECS[(pauli_type, weight)]
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
    for _weight in (4, 6, 8, 12, 18, 24):
        _name = f"MPP_circuit_{_pauli_type}_weight_{_weight}"
        globals()[_name] = _make_weighted_mpp(_pauli_type, _weight)


def MPP_circuit(circuit, pauli_string, ancilla, flag, error):
    pauli_type = pauli_string_type(pauli_string)
    weight = pauli_weight(pauli_string)
    try:
        function = MPP_CIRCUITS_BY_TYPE_AND_WEIGHT[pauli_type][weight]
    except KeyError as exc:
        supported = sorted(MPP_CIRCUITS_BY_TYPE_AND_WEIGHT.get(pauli_type, {}))
        raise ValueError(
            f"No MPP_circuit_{pauli_type}_weight_{weight} is configured. "
            f"Supported {pauli_type} weights are {supported}.") from exc
    return function(circuit, pauli_string, ancilla, flag, error)


def count_measurements_for_stabilizers(stabilizers, ancilla=None, flag=None, error=0):
    ancilla = DEFAULT_SYNDROME_ANCILLA if ancilla is None else ancilla
    flag = DEFAULT_FLAG_QUBITS if flag is None else flag
    total = 0
    for stabilizer in stabilizers.values():
        circuit = stim.Circuit()
        MPP_circuit(circuit, stabilizer, ancilla, flag, error)
        total += circuit.num_measurements
    return total


def Stabilizers_measurement_general(error_rate, tick_num, After_merging=False,
                                    After_merging_string=False, ancilla=None, flag=None):
    circuit = stim.Circuit()
    ancilla = DEFAULT_SYNDROME_ANCILLA if ancilla is None else ancilla
    flag = DEFAULT_FLAG_QUBITS if flag is None else flag
    measurements_per_round = count_measurements_for_stabilizers(
        stabilizers_general, ancilla, flag, error_rate)
    for name, stabilizer in stabilizers_general.items():
        MPP_circuit(circuit, stabilizer, ancilla, flag, error_rate)
        if tick_num != 1:
            circuit.append(
                "DETECTOR",
                [stim.target_rec(-1), stim.target_rec(-(measurements_per_round + 1))],
                tag=f"Det_{name}_general_{tick_num}",
            )
    return circuit


def measure_logical_qubits_3D():
    circuit = stim.Circuit()
    circuit.append("MPP", stim.PauliString(LOGICAL_3D_PAULI), tag="logical_qubits_3D")
    circuit.append("OBSERVABLE_INCLUDE", [stim.target_rec(-1)], 0)
    return circuit


def configure(distance):
    global _ACTIVE_SEQUENCE_SPECS, MPP_CIRCUITS_BY_TYPE_AND_WEIGHT
    if distance not in _CONFIGS:
        raise ValueError(f"Unsupported distance {distance}; choose 3, 5, or 7.")
    config = _CONFIGS[distance]
    for name in config.__all__:
        globals()[name] = getattr(config, name)
    _ACTIVE_SEQUENCE_SPECS = MEMORY_SEQUENCE_SPECS[distance]
    for name, value in MEMORY_SEQUENCE_CONSTANTS[distance].items():
        globals()[name] = value
    MPP_CIRCUITS_BY_TYPE_AND_WEIGHT = {"X": {}, "Z": {}}
    for pauli_type, weight in _ACTIVE_SEQUENCE_SPECS:
        name = f"MPP_circuit_{pauli_type}_weight_{weight}"
        MPP_CIRCUITS_BY_TYPE_AND_WEIGHT[pauli_type][weight] = globals()[name]
    globals()["MPP_circuit_X"] = MPP_CIRCUITS_BY_TYPE_AND_WEIGHT["X"].get(8)
    globals()["MPP_circuit_Z"] = MPP_CIRCUITS_BY_TYPE_AND_WEIGHT["Z"].get(4)

    exports = {name: getattr(config, name) for name in config.__all__}
    exports.update(MEMORY_SEQUENCE_CONSTANTS[distance])
    exports["MPP_CIRCUITS_BY_TYPE_AND_WEIGHT"] = MPP_CIRCUITS_BY_TYPE_AND_WEIGHT
    exports["MPP_circuit_X"] = globals()["MPP_circuit_X"]
    exports["MPP_circuit_Z"] = globals()["MPP_circuit_Z"]
    for name, value in globals().items():
        if callable(value) and getattr(value, "__module__", None) == __name__ and not name.startswith("_"):
            exports[name] = value
    return exports
