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

V_even = [0, 2, 4, 6, 9, 12, 13] # SQRT_Z
V_odd = [1, 3, 5, 7, 8, 10, 11, 14] # SQRT_Z_DAG

# Stabilizer set:
stabilizers_general = {**stabilizers_k_z, **stabilizers_k_x}

def measure_logical_qubits_3D_Z() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("Z10*Z13*Z14"), tag="logical_qubits_3D_Z")
    c.append("OBSERVABLE_INCLUDE", [
        stim.target_rec(-1), ], 0)
    
    return c

def measure_logical_qubits_3D_X() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("X0*X3*X6*X7*X10*X13*X14"), tag="logical_qubits_3D_X")
    c.append("OBSERVABLE_INCLUDE", [
        stim.target_rec(-1), ], 0)
    
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

DISTANCE = 3

__all__ = ['stabilizers_k_z', 'stabilizers_k_x', 'V_even', 'V_odd', 'stabilizers_general', 'measure_logical_qubits_3D_Z', 'measure_logical_qubits_3D_X', 'S_Z_Gate', 'S_Z_DAG_Gate', 'DISTANCE']
