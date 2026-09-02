import stim

stabilizers_k_z = {
# --- Top 24 Specified Stabilizers ---
    "k7_z":  stim.PauliString("Z6*Z13*Z25*Z56"),             # with 65
    "k5_z":  stim.PauliString("Z4*Z13*Z14*Z25*Z31*Z35"),     # with 66
    "k1_z":  stim.PauliString("Z0*Z13*Z35*Z56"),             # with 67
    "k6_z":  stim.PauliString("Z5*Z7*Z40*Z54"),              # with 68
    "k8_z":  stim.PauliString("Z4*Z7*Z19*Z21*Z31*Z40"),      # with 69
    "k14_z": stim.PauliString("Z7*Z14*Z31*Z54"),             # with 70
    "k34_z": stim.PauliString("Z33*Z41*Z55*Z58"),            # with 71
    "k20_z": stim.PauliString("Z19*Z21*Z55*Z58"),            # with 72
    "k15_z": stim.PauliString("Z4*Z6*Z21*Z25*Z33*Z55"),      # with 73



    
    "k44_z": stim.PauliString("Z38*Z55*Z58*Z61"),            # with 74
    "k23_z": stim.PauliString("Z22*Z33*Z38*Z55"),            # with 75
    "k19_z": stim.PauliString("Z18*Z21*Z32*Z38*Z47*Z55"),    # with 76
    "k41_z": stim.PauliString("Z19*Z21*Z32*Z43"),            # with 77
    "k2_z":  stim.PauliString("Z1*Z6*Z25*Z59"),              # with 78    
    "k25_z": stim.PauliString("Z4*Z21*Z24*Z32"),             # with 79  
    "k35_z": stim.PauliString("Z1*Z4*Z24*Z25*Z44*Z60"),      # with 80 
    "k36_z": stim.PauliString("Z1*Z13*Z25*Z27"),             # with 81
    "k33_z": stim.PauliString("Z4*Z17*Z24*Z31"),             # with 82      
    "k39_z": stim.PauliString("Z7*Z37*Z40*Z46"),             # with 83
    "k21_z": stim.PauliString("Z13*Z20*Z27*Z56"),            # with 84
    "k18_z": stim.PauliString("Z7*Z17*Z31*Z37"),             # with 85
    "k28_z": stim.PauliString("Z13*Z27*Z35*Z64"),            # with 86
    "k32_z": stim.PauliString("Z14*Z17*Z31*Z34"),            # with 87       
    "k11_z": stim.PauliString("Z7*Z10*Z37*Z54"),             # with 88


    
    # --- Remaining Stabilizers ---
    "k3_z":  stim.PauliString("Z2*Z12*Z26*Z63"),
    "k4_z":  stim.PauliString("Z3*Z18*Z39*Z47"),
    "k9_z":  stim.PauliString("Z8*Z23*Z45*Z50"),
    "k10_z": stim.PauliString("Z9*Z15*Z49*Z51"),
    "k12_z": stim.PauliString("Z11*Z12*Z52*Z60"),
    "k13_z": stim.PauliString("Z2*Z17*Z24*Z34*Z44*Z63"),
    "k16_z": stim.PauliString("Z9*Z23*Z45*Z49"),
    "k17_z": stim.PauliString("Z16*Z18*Z39*Z57"),
    "k22_z": stim.PauliString("Z18*Z44*Z47*Z52*Z57*Z60"),
    "k24_z": stim.PauliString("Z2*Z23*Z50*Z63"),
    "k26_z": stim.PauliString("Z20*Z27*Z30*Z64"),
    "k27_z": stim.PauliString("Z12*Z44*Z60*Z63"),
    "k29_z": stim.PauliString("Z9*Z15*Z28*Z42"),
    "k30_z": stim.PauliString("Z11*Z12*Z26*Z29"),
    "k31_z": stim.PauliString("Z24*Z32*Z44*Z47"),
    "k37_z": stim.PauliString("Z22*Z36*Z38*Z61"),
    "k38_z": stim.PauliString("Z10*Z37*Z46*Z53"),
    "k40_z": stim.PauliString("Z3*Z32*Z43*Z47"),
    "k42_z": stim.PauliString("Z18*Z22*Z38*Z57"),
    "k43_z": stim.PauliString("Z9*Z42*Z48*Z49"),
    "k45_z": stim.PauliString("Z3*Z23*Z44*Z45*Z47*Z63"),
    "k46_z": stim.PauliString("Z48*Z49*Z51*Z62"),
    "k47_z": stim.PauliString("Z23*Z49*Z50*Z51"),
    "k48_z": stim.PauliString("Z11*Z12*Z23*Z48*Z49*Z63")
}

stabilizers_k_x = {
    # --- 3D K-series X Stabilizers ---
    "k1_x": stim.PauliString("X0*X13*X20*X27*X30*X35*X56*X64"),
    "k2_x": stim.PauliString("X7*X10*X14*X17*X31*X34*X37*X54"),
    "k3_x": stim.PauliString("X1*X4*X6*X18*X21*X22*X24*X25*X32*X33*X38*X44*X47*X52*X55*X57*X59*X60"),
    "k4_x": stim.PauliString("X1*X2*X4*X12*X13*X14*X17*X24*X25*X26*X27*X31*X34*X35*X44*X60*X63*X64"),
    "k5_x": stim.PauliString("X5*X7*X10*X37*X40*X46*X53*X54"),
    "k6_x": stim.PauliString("X3*X18*X19*X21*X32*X38*X39*X43*X47*X55*X58*X61"),
    "k7_x": stim.PauliString("X1*X6*X13*X20*X25*X27*X56*X59"),
    "k8_x": stim.PauliString("X4*X7*X17*X19*X21*X24*X31*X32*X37*X40*X43*X46"),
    "k9_x": stim.PauliString("X22*X33*X36*X38*X41*X55*X58*X61"),
    "k10_x": stim.PauliString("X1*X11*X12*X20*X26*X27*X29*X30*X52*X59*X60*X64"),
    "k11_x": stim.PauliString("X2*X3*X8*X10*X17*X23*X24*X32*X34*X37*X43*X44*X45*X46*X47*X50*X53*X63"),
    "k12_x": stim.PauliString("X16*X18*X22*X36*X38*X39*X57*X61"),
    "k13_x": stim.PauliString("X2*X11*X12*X23*X26*X29*X48*X49*X50*X51*X62*X63"),
    "k14_x": stim.PauliString("X8*X9*X15*X23*X45*X49*X50*X51"),
    "k15_x": stim.PauliString("X3*X9*X11*X12*X16*X18*X23*X39*X42*X44*X45*X47*X48*X49*X52*X57*X60*X63"),
    "k16_x": stim.PauliString("X9*X15*X28*X42*X48*X49*X51*X62")
}

V_even = [0, 2, 3, 4, 6, 8, 9, 11, 13, 14, 16, 17, 18, 19, 23, 26, 27, 28, 30, 32, 33, 36, 37, 38, 40, 44, 48, 51, 53, 54, 58, 59, 60] # SQRT_Z
V_odd = [1, 5, 7, 10, 12, 15, 20, 21, 22, 24, 25, 29, 31, 34, 35, 39, 41, 42, 43, 45, 46, 47, 49, 50, 52, 55, 56, 57, 61, 62, 63, 64] # SQRT_Z_DAG

# Stabilizer set:
stabilizers_general = {**stabilizers_k_z, **stabilizers_k_x}

def measure_logical_qubits_3D_Z() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("Z0*Z5*Z14*Z35*Z54"), tag="logical_qubits_3D_Z")
    c.append("OBSERVABLE_INCLUDE", [
        stim.target_rec(-1), ], 0)
    return c

def measure_logical_qubits_3D_X() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("X0*X4*X5*X6*X7*X13*X14*X19*X21*X25*X31*X33*X35*X40*X41*X54*X55*X56*X58"), tag="logical_qubits_3D_X")
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

DISTANCE = 5

__all__ = ['stabilizers_k_z', 'stabilizers_k_x', 'V_even', 'V_odd', 'stabilizers_general', 'measure_logical_qubits_3D_Z', 'measure_logical_qubits_3D_X', 'S_Z_Gate', 'S_Z_DAG_Gate', 'DISTANCE']
