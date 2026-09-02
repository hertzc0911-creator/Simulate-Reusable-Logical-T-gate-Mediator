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
stabilizers_general = {**stabilizers_k_z, **stabilizers_k_x}

DISTANCE = 3
QUBIT_RANGE_3D = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
DEFAULT_SYNDROME_ANCILLA = 15
DEFAULT_FLAG_QUBITS = [16, 17, 18]
LOGICAL_3D_PAULI = 'X0*X3*X6*X7*X10*X13*X14'

__all__ = ['stabilizers_k_z', 'stabilizers_k_x', 'V_even', 'V_odd', 'S_gate_track', 'stabilizers_general', 'DISTANCE', 'QUBIT_RANGE_3D', 'DEFAULT_SYNDROME_ANCILLA', 'DEFAULT_FLAG_QUBITS', 'LOGICAL_3D_PAULI']
