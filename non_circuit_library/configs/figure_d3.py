import stim

# 3D color code

stabilizers_k_z = {
    "k1_z" : stim.PauliString("Z0*Z3*Z6*Z7"),
    "k2_z" : stim.PauliString("Z3*Z6*Z10*Z13"),
    "k3_z" : stim.PauliString("Z6*Z7*Z13*Z14"),
    "k7_z" : stim.PauliString("Z2*Z3*Z5*Z6"),
    "k6_z" : stim.PauliString("Z4*Z5*Z6*Z7"),
    "k10_z": stim.PauliString("Z5*Z6*Z11*Z13"),
    "k5_z" : stim.PauliString("Z1*Z2*Z4*Z5"),
    "k8_z" : stim.PauliString("Z4*Z5*Z11*Z12"),
    "k9_z" : stim.PauliString("Z2*Z5*Z9*Z11"),
    "k4_z" : stim.PauliString("Z8*Z9*Z11*Z12")
}

stabilizers_k_x = {
    "k1_x" : stim.PauliString("X0*X1*X2*X3*X4*X5*X6*X7"),
    "k2_x" : stim.PauliString("X2*X3*X5*X6*X9*X10*X11*X13"),
    "k3_x" : stim.PauliString("X4*X5*X6*X7*X11*X12*X13*X14"),
    "k4_x" : stim.PauliString("X1*X2*X4*X5*X8*X9*X11*X12")
}

# Operator and Detector of S(T) gate

V_even = [0, 2, 4, 6, 9, 12, 13] # SQRT_Z
V_odd = [1, 3, 5, 7, 8, 10, 11, 14] # SQRT_Z_DAG


S_gate_track = {
    "k1_x": "k1_z + k5_z",
    "k2_x": "k2_z + k9_z",
    "k3_x": "k3_z + k8_z",
    "k4_x": "k5_z + k4_z"
}

# Aniclla: 15, 16, 17, 18, 19, 20

# 2D color code

stabilizers_s_x = {
    "s1_x" : stim.PauliString("X24*X25*X26*X27"),
    "s2_x" : stim.PauliString("X21*X23*X25*X27"),
    "s3_x" : stim.PauliString("X22*X23*X26*X27")
}

stabilizers_s_z = {
    "s1_z" : stim.PauliString("Z24*Z25*Z26*Z27"),
    "s2_z" : stim.PauliString("Z21*Z23*Z25*Z27"),
    "s3_z" : stim.PauliString("Z22*Z23*Z26*Z27"),

}

# Enlargable stabilizers Face to Face

stabilizers_added_X = {
    # --- Added M-series X Stabilizers ---
    "m1_x": stim.PauliString("X0*X24*X15"),  # 0(3D) 3(2D) 15
    "m2_x": stim.PauliString("X10*X21*X16"),  # 10(3D) 0(2D) 16
    "m3_x": stim.PauliString("X14*X22*X17"),  # 14(3D) 1(2D) 17
    "m4_x": stim.PauliString("X3*X25*X15*X16*X18"),  # 3(3D) 4(2D) 15 16 18
    "m5_x": stim.PauliString("X7*X26*X15*X17*X19"),  # 7(3D) 5(2D) 15 17 19
    "m6_x": stim.PauliString("X13*X23*X16*X17*X20"),  # 13(3D) 2(2D) 16 17 20
    "m7_x": stim.PauliString("X6*X27*X15*X16*X17*X18*X19*X20"),  # 6(3D) 6(2D) 15 16 17 18 19 20
}

# --- matching logical operators --- 
    # 3D (X):    0,  3,  6,  7, 10, 13, 14
    
    # 2D (Z/X): 21, 22, 23, 24, 25, 26, 27
    # 2D (Z/X):  0,  1,  2,  3,  4,  5,  6


stabilizers_k_z_enlargable = {
    "k1_z" : stim.PauliString("Z0*Z3*Z6*Z7"), # with 15
    "k2_z" : stim.PauliString("Z3*Z6*Z10*Z13"), # with 16
    "k3_z" : stim.PauliString("Z6*Z7*Z13*Z14"), # with 17
    "k7_z" : stim.PauliString("Z2*Z3*Z5*Z6"),  # with 18
    "k6_z" : stim.PauliString("Z4*Z5*Z6*Z7"), # with 19
    "k10_z": stim.PauliString("Z5*Z6*Z11*Z13"), # with 20
}

stabilizers_k_z_enlargable_horizontal = {
    "k1_z" : stim.PauliString("Z0*Z3*Z6*Z7"), # with 15
    "k2_z" : stim.PauliString("Z3*Z6*Z10*Z13"), # with 16
    "k3_z" : stim.PauliString("Z6*Z7*Z13*Z14"), # with 17
}

stabilizers_k_z_enlargable_vertical = {
    "k7_z" : stim.PauliString("Z2*Z3*Z5*Z6"),  # with 18
    "k6_z" : stim.PauliString("Z4*Z5*Z6*Z7"), # with 19
    "k10_z": stim.PauliString("Z5*Z6*Z11*Z13"), # with 20
}
    
stabilizers_k_z_enlarged = {
    "k1_z" : stim.PauliString("Z0*Z3*Z6*Z7*Z15"), # with 15
    "k2_z" : stim.PauliString("Z3*Z6*Z10*Z13*Z16"), # with 16
    "k3_z" : stim.PauliString("Z6*Z7*Z13*Z14*Z17"), # with 17
    "k7_z" : stim.PauliString("Z2*Z3*Z5*Z6*Z18"),  # with 18
    "k6_z" : stim.PauliString("Z4*Z5*Z6*Z7*Z19"), # with 19
    "k10_z": stim.PauliString("Z5*Z6*Z11*Z13*Z20"), # with 20
}

stabilizers_s_z_enlarged = {
    "s1_z" : stim.PauliString("Z24*Z25*Z26*Z27*Z15"),
    "s2_z" : stim.PauliString("Z21*Z23*Z25*Z27*Z16"),
    "s3_z" : stim.PauliString("Z22*Z23*Z26*Z27*Z17"),
}

# Enlargable stabilizers String to String

stabilizers_added_Z = {
    "m1_z": stim.PauliString("Z0*Z24*Z15"),  # 0(3D) 3(2D) 15
    "m2_z": stim.PauliString("Z3*Z25*Z15*Z16"),  # 3(3D) 4(2D) 15 16
    "m3_z": stim.PauliString("Z10*Z21*Z16"),  # 10(3D) 0(2D) 16
}


# Ensure the logical ZZ are supported by all the physical qubits in a face
stabilizer_global = {
    "k3_z" : stim.PauliString("Z6*Z7*Z13*Z14"),
    "s3_z" : stim.PauliString("Z22*Z23*Z26*Z27"),
}

# --- matching logical operators --- 
    # 3D (Z):    0,  3,  6,  7, 10, 13, 14
    
    # 2D (Z/X): 21, 22, 23, 24, 25, 26, 27
    # 2D (Z/X):  0,  1,  2,  3,  4,  5,  6


stabilizers_k_x_enlargable = {
    "k1_x" : stim.PauliString("X0*X1*X2*X3*X4*X5*X6*X7"),  # with 15
    "k2_x" : stim.PauliString("X2*X3*X5*X6*X9*X10*X11*X13"),  # with 16

}

stabilizers_k_x_enlarged = {
    "k1_x" : stim.PauliString("X0*X1*X2*X3*X4*X5*X6*X7*X15"),  # with 15
    "k2_x" : stim.PauliString("X2*X3*X5*X6*X9*X10*X11*X13*X16"),  # with 16

}

stabilizers_s_x_enlargable = {
    "s1_x" : stim.PauliString("X24*X25*X26*X27"),  # with 15
    "s2_x" : stim.PauliString("X21*X23*X25*X27"),  # with 16
}

stabilizers_s_x_enlarged = {
    "s1_x" : stim.PauliString("X24*X25*X26*X27*X15"),  # with 15
    "s2_x" : stim.PauliString("X21*X23*X25*X27*X16"),  # with 16
}

# Stabilizer set Face to Face:
stabilizers_general = {**stabilizers_k_x, **stabilizers_k_z, **stabilizers_s_x, **stabilizers_s_z}

stabilizers_k_z_unchange = {k: v for k, v in stabilizers_k_z.items() if k not in stabilizers_k_z_enlargable}

stabilizers_merged = {**stabilizers_added_X, **stabilizers_k_x, **stabilizers_k_z_enlarged, **stabilizers_k_z_unchange, **stabilizers_s_x, **stabilizers_s_z_enlarged}

stabilizers_merged_without_add_X = {**stabilizers_k_x, **stabilizers_k_z_enlarged, **stabilizers_k_z_unchange, **stabilizers_s_x, **stabilizers_s_z_enlarged}

# Stabilizer set String to String:
stabilizers_k_x_unchange = {k: v for k, v in stabilizers_k_x.items() if k not in stabilizers_k_x_enlargable}

stabilizers_s_x_unchange = {k: v for k, v in stabilizers_s_x.items() if k not in stabilizers_s_x_enlargable}

stabilizers_merged_string = {**stabilizers_added_Z, **stabilizers_k_x_enlarged, **stabilizers_k_x_unchange, **stabilizers_k_z, **stabilizers_s_x_enlarged, **stabilizers_s_x_unchange, **stabilizers_s_z,}

stabilizers_merged_string_without_add_Z = {**stabilizers_k_x_enlarged, **stabilizers_k_x_unchange, **stabilizers_k_z, **stabilizers_s_x_enlarged, **stabilizers_s_x_unchange, **stabilizers_s_z,}

def lattice_surgery_Merge():
    
    c = stim.Circuit()  
    
    c.append("R", [15, 16, 17, 18, 19, 20])
   
    return c

def lattice_surgery_Split(error_rate):
    
    c = stim.Circuit()

    c.append("M", [15, 16, 17, 18, 19, 20], tag="Measurement_ancilla", arg=error_rate)
    
    return c

def lattice_surgery_Merge_string():
    
    c = stim.Circuit()  
    
    c.append("H", [15, 16])
   
    return c

def lattice_surgery_Split_string(error_rate):
    
    c = stim.Circuit()

    c.append("MX", [15, 16], tag="Measurement_ancilla_string", arg=error_rate)
    
    return c

def measure_logical_qubits_3D() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("X0*X3*X6*X7*X10*X13*X14"), tag="logical_qubits_3D")
    c.append("OBSERVABLE_INCLUDE", [
        stim.target_rec(-1), ], 0)
    
    return c

def measure_logical_qubits_2D() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("Z21*Z22*Z23*Z24*Z25*Z26*Z27"), tag="logical_qubits_2D")
    c.append("OBSERVABLE_INCLUDE", [
        stim.target_rec(-1), ], 1)

    return c


def measurement_XX() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("Z0*Z3*Z6*Z7*Z10*Z13*Z14"), tag="logical_qubits_3D")
    c.append("MPP", stim.PauliString("X21*X22*X23*X24*X25*X26*X27"), tag="logical_qubits_2D") 
    c.append("OBSERVABLE_INCLUDE", [stim.target_rec(-1), stim.target_rec(-2), ], 0)
    
    return c


def measurement_ZZ() -> stim.Circuit:

    c = stim.Circuit()
    c.append("MPP", stim.PauliString("X0*X3*X6*X7*X10*X13*X14"), tag="logical_qubits_3D")
    c.append("MPP", stim.PauliString("Z21*Z22*Z23*Z24*Z25*Z26*Z27"), tag="logical_qubits_2D") 
    c.append("OBSERVABLE_INCLUDE", [stim.target_rec(-1), stim.target_rec(-2), ], 0)

    return c   

def S_Z_Gate() -> stim.Circuit:
    c = stim.Circuit()
    c.append("SQRT_Z", V_even)
    c.append("SQRT_Z_DAG", V_odd)
    
    return c

def S_Z_DAG_Gate() -> stim.Circuit:
    c = stim.Circuit()
    c.append("SQRT_Z_DAG", V_odd)
    c.append("SQRT_Z", V_even)
    
    return c

def logical_CZ() -> stim.Circuit:

    c = stim.Circuit()

    control_qubits = [24, 21, 22, 25, 26, 23, 27]  

    target_qubits = [0, 10, 14, 3, 7, 13, 6]  

    c.append("CZ", [q for pair in zip(control_qubits, target_qubits) for q in pair])

    return c

DISTANCE = 3

__all__ = ['stabilizers_k_z', 'stabilizers_k_x', 'V_even', 'V_odd', 'S_gate_track', 'stabilizers_s_x', 'stabilizers_s_z', 'stabilizers_added_X', 'stabilizers_k_z_enlargable', 'stabilizers_k_z_enlargable_horizontal', 'stabilizers_k_z_enlargable_vertical', 'stabilizers_k_z_enlarged', 'stabilizers_s_z_enlarged', 'stabilizers_added_Z', 'stabilizer_global', 'stabilizers_k_x_enlargable', 'stabilizers_k_x_enlarged', 'stabilizers_s_x_enlargable', 'stabilizers_s_x_enlarged', 'stabilizers_general', 'stabilizers_k_z_unchange', 'stabilizers_merged', 'stabilizers_merged_without_add_X', 'stabilizers_k_x_unchange', 'stabilizers_s_x_unchange', 'stabilizers_merged_string', 'stabilizers_merged_string_without_add_Z', 'lattice_surgery_Merge', 'lattice_surgery_Split', 'lattice_surgery_Merge_string', 'lattice_surgery_Split_string', 'measure_logical_qubits_3D', 'measure_logical_qubits_2D', 'measurement_XX', 'measurement_ZZ', 'S_Z_Gate', 'S_Z_DAG_Gate', 'logical_CZ', 'DISTANCE']
