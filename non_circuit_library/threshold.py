import stim

from .configs import threshold_d3, threshold_d5, threshold_d7


_CONFIGS = {3: threshold_d3, 5: threshold_d5, 7: threshold_d7}


def Stabilizers_measurement_general(error_rate, tick_num, After_merging=False):
    c = stim.Circuit()
    
    
    num_measurements_per_round = len(stabilizers_k_z) + len(stabilizers_k_x) 
    if tick_num == 1:
        for name, stabilizer in stabilizers_general.items():  
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)

    

            
    else:
        for name, stabilizer in stabilizers_general.items():  
            c.append("MPP", [stabilizer], tag=f"Stabilizers_{name}_general_{tick_num}", arg=error_rate)
            c.append("DETECTOR", [   
                    stim.target_rec(-1),                    # Current measurement  
                    stim.target_rec( - (num_measurements_per_round + 1) )  # Previous round measurement  
                ], tag=f"Det_{name}_general_{tick_num}")

    return c


def configure(distance):
    if distance not in _CONFIGS:
        raise ValueError(f"Unsupported distance {distance}; choose 3, 5, or 7.")
    config = _CONFIGS[distance]
    for name in config.__all__:
        globals()[name] = getattr(config, name)
    exports = {name: getattr(config, name) for name in config.__all__}
    exports['Stabilizers_measurement_general'] = Stabilizers_measurement_general
    return exports
