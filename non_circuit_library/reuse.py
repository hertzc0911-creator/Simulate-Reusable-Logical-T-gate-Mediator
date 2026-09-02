import stim

from .configs import reuse_d3, reuse_d5, reuse_d7


_CONFIGS = {3: reuse_d3, 5: reuse_d5, 7: reuse_d7}


def detector_k_x(circuit, name, tick_num, stabilizers_order, append_dependencies):
    """
    Adds a detector for a k_x stabilizer after SQRT_Z.
    - Target 1: Current-round k_x measurement.
    - Middle Targets: Current-round k_z dependencies.
    - Final Target: Previous-round k_x measurement.
    """
    order_keys = list(stabilizers_order.keys())
    num_measurements_per_round = len(order_keys)

    # The helper is called after the complete stabilizer round.
    physical_index_kx = order_keys.index(name)
    current_kx_record_index = -(num_measurements_per_round - physical_index_kx)

    # Parse the k_z dependencies produced by SQRT_Z.
    deps = [d.strip() for d in append_dependencies[name].split('+')]

    # Start with the current k_x measurement.
    targets = [stim.target_rec(current_kx_record_index)]

    # Add current-round k_z dependency measurements.
    for dep_name in deps:
        physical_index_kz = order_keys.index(dep_name)
        kz_record_index = -(num_measurements_per_round - physical_index_kz)
        targets.append(stim.target_rec(kz_record_index))

    # Add the previous-round k_x measurement.
    targets.append(stim.target_rec(current_kx_record_index - num_measurements_per_round))







    circuit.append("DETECTOR", targets, tag=f"Det_{name}_general_{tick_num}")

def Stabilizers_measurement_general(error_rate, tick_num, After_merging=False, After_merging_string=False):
    c = stim.Circuit()
    
    
    num_measurements_per_round = len(stabilizers_general)

    if tick_num == 1:
        for name, stabilizer in stabilizers_general.items():  
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)


    
    elif After_merging:
        
        num_ancilla = len(stabilizers_k_z_enlargable)

        
        # k_x: stay the same
        for name, stabilizer in stabilizers_k_x.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement
                    # k_x is unchanged by the face split.
                ], tag=f"Det_{name}_general_{tick_num}")

        # k_z_enlargable + ancilla = k_z_enlarged
        len_k_z = len(stabilizers_k_x)
        for name, stabilizer in stabilizers_k_z_enlargable.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_ancilla + len_k_z + 1) ),  # Ancilla measurement
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")

        # k_z_unchange: stay the same
        for name, stabilizer in stabilizers_k_z_unchange.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")


        # s_x: stay the same
        for name, stabilizer in stabilizers_s_x.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")

            
        # s_z + ancilla = s_z_enlarged
        len_s_z = len(stabilizers_k_x) + len(stabilizers_k_z_enlargable) + len(stabilizers_k_z_unchange) + len(stabilizers_s_x)
        for name, stabilizer in stabilizers_s_z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_ancilla + len_s_z + 1) ),  # Ancilla measurement
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")

            
    
    elif After_merging_string:
        
        num_ancilla = len(stabilizers_k_x_enlargable)
        
        # k_x_enlargable + ancilla = k_x_enlarged
        for name, stabilizer in stabilizers_k_x_enlargable.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_ancilla + 1) ),  # Ancilla measurement
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")

        # k_x_unchange: stay the same
        for name, stabilizer in stabilizers_k_x_unchange.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")

        # k_z: stay the same
        for name, stabilizer in stabilizers_k_z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")

        # s_x_enlargable + ancilla = s_x_enlarged
        len_s_x = len(stabilizers_k_x_enlargable) + len(stabilizers_k_x_unchange) + len(stabilizers_k_z)
        for name, stabilizer in stabilizers_s_x_enlargable.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_ancilla + len_s_x + 1) ),  # Ancilla measurement
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
        
        # s_x_unchange: stay the same
        for name, stabilizer in stabilizers_s_x_unchange.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")

        # s_z: stay the same        
        for name, stabilizer in stabilizers_s_z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + num_ancilla + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")    


            
    else:
        for name, stabilizer in stabilizers_general.items():  
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [   
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")

    return c

def Stabilizers_measurement_general_after_gate(error_rate, tick_num, After_CZ=False, After_S_3D=False, After_H_2D=False):
    c = stim.Circuit()
    num_measurements_per_round = len(stabilizers_general)
    if After_CZ:
        # k_x: measurement first
        for name, stabilizer in stabilizers_k_x.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            
            
        # k_z: stay the same
        for name, stabilizer in stabilizers_k_z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement   
                ], tag=f"Det_{name}_general_{tick_num}")
            

        # s_x: goes to s_x + k_z
        address_s_x = len(stabilizers_k_z)
        for name, stabilizer in stabilizers_s_x.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (address_s_x + 1) ), # Current k_z measurement
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
            
        # s_z: stay the same
        for name, stabilizer in stabilizers_s_z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
            
        # detector of k_x:
        address_k_x = len(stabilizers_s_x) + len(stabilizers_s_z) + len(stabilizers_k_z) + (len(stabilizers_k_x)-len(stabilizers_s_z))
        for i, (name, stabilizer) in enumerate(list(stabilizers_k_x.items())[:len(stabilizers_s_z)]):
            c.append("DETECTOR", [  
                    stim.target_rec( - (address_k_x + i + 1)),                    # Current measurement  
                    stim.target_rec( - (i + 1)),                                  # Current s_z measurement
                    stim.target_rec( - (address_k_x + num_measurements_per_round + i + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
        address_k_x = len(stabilizers_s_x) + len(stabilizers_s_z) + len(stabilizers_k_z)
        for i, (name, stabilizer) in enumerate(list(stabilizers_k_x.items())[len(stabilizers_s_z):]):
            c.append("DETECTOR", [  
                    stim.target_rec( - (address_k_x + i + 1)),                    # Current measurement  
                    stim.target_rec( - (address_k_x + num_measurements_per_round + i + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")

            
    if After_S_3D:  
        # k_x: goes to k_x + k_z + k_z
        for name, stabilizer in stabilizers_k_x.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)

        # k_z: stay the same
        for name, stabilizer in stabilizers_k_z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
            
        # s_x: stay the same
        for name, stabilizer in stabilizers_s_x.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
            
        # s_z: stay the same
        for name, stabilizer in stabilizers_s_z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")   
        
        for kx_name in S_gate_track.keys():
            detector_k_x(c, kx_name, tick_num, stabilizers_general, S_gate_track)



        
    if After_H_2D:
        # k_x: stay the same
        for name, stabilizer in stabilizers_k_x.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement
                ], tag=f"Det_{name}_general_{tick_num}")
            
        # k_z: stay the same
        for name, stabilizer in stabilizers_k_z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")


        # s_x: goes to s_z
        len_s_x = len(stabilizers_s_z)
        for name, stabilizer in stabilizers_s_x.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round - len_s_x + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")

            
        # s_z: goes to s_x
        len_s_z = len(stabilizers_s_x)
        for name, stabilizer in stabilizers_s_z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + len_s_z + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")

    
    return c

def Stabilizers_measurement_merged(error_rate, tick_num, First_merging_round=False, offset=0, Observable_list_ZZ=None):
    c = stim.Circuit()
    num_measurements_per_round = len(stabilizers_merged)

    if First_merging_round:
        for name, stabilizer in stabilizers_added_X.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_merged_{tick_num}", arg=error_rate)
        
        for name, stabilizer in stabilizers_merged_without_add_X.items():  
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_merged_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1))  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")
  
    

    if Observable_list_ZZ is not None:
        for name, stabilizer in stabilizers_added_X.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_merged_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")
            Observable_list_ZZ.append(c.num_measurements - 1 + offset)
        for name, stabilizer in stabilizers_merged_without_add_X.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_merged_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")

            
    else:
        for name, stabilizer in stabilizers_merged.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_merged_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")

    return c

def Stabilizers_measurement_merged_string(error_rate, tick_num, First_merging_round=False, offset=0, Observable_list_XX=None):
    c = stim.Circuit()
    num_measurements_per_round = len(stabilizers_merged_string)

    if First_merging_round:
        for name, stabilizer in stabilizers_added_Z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_merged_{tick_num}", arg=error_rate)
        
        for name, stabilizer in stabilizers_merged_string_without_add_Z.items():  
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_merged_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1))  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")

    

    if Observable_list_XX is not None:
        for name, stabilizer in stabilizers_added_Z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_merged_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")
            Observable_list_XX.append(c.num_measurements - 1 + offset)
        for name, stabilizer in stabilizers_merged_string_without_add_Z.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_merged_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")
            if name in stabilizer_global:
                Observable_list_XX.append(c.num_measurements - 1 + offset)

            

    else:
        for name, stabilizer in stabilizers_merged_string.items():
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_merged_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [  
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_merged_{tick_num}")

    return c


def configure(distance):
    if distance not in _CONFIGS:
        raise ValueError(f"Unsupported distance {distance}; choose 3, 5, or 7.")
    config = _CONFIGS[distance]
    for name in config.__all__:
        globals()[name] = getattr(config, name)
    exports = {name: getattr(config, name) for name in config.__all__}
    exports['detector_k_x'] = detector_k_x
    exports['Stabilizers_measurement_general'] = Stabilizers_measurement_general
    exports['Stabilizers_measurement_general_after_gate'] = Stabilizers_measurement_general_after_gate
    exports['Stabilizers_measurement_merged'] = Stabilizers_measurement_merged
    exports['Stabilizers_measurement_merged_string'] = Stabilizers_measurement_merged_string
    return exports
