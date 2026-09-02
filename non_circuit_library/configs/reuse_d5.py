import stim

# 3D color code

stabilizers_k_z = {
# --- Top 24 Specified Stabilizers ---

    "k1_z":  stim.PauliString("Z0*Z13*Z35*Z56"),             # with 67
    "k7_z":  stim.PauliString("Z6*Z13*Z25*Z56"),             # with 65
    "k15_z": stim.PauliString("Z4*Z6*Z21*Z25*Z33*Z55"),      # with 73
    "k34_z": stim.PauliString("Z33*Z41*Z55*Z58"),            # with 71
    "k5_z":  stim.PauliString("Z4*Z13*Z14*Z25*Z31*Z35"),     # with 66
    "k14_z": stim.PauliString("Z7*Z14*Z31*Z54"),             # with 70    
    "k6_z":  stim.PauliString("Z5*Z7*Z40*Z54"),              # with 68
    "k8_z":  stim.PauliString("Z4*Z7*Z19*Z21*Z31*Z40"),      # with 69
    "k20_z": stim.PauliString("Z19*Z21*Z55*Z58"),            # with 72

    
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

    "k1_x": stim.PauliString("X0*X13*X20*X27*X30*X35*X56*X64"),  # with 65
    "k7_x": stim.PauliString("X1*X6*X13*X20*X25*X27*X56*X59"),  # with 66
    "k3_x": stim.PauliString("X1*X4*X6*X18*X21*X22*X24*X25*X32*X33*X38*X44*X47*X52*X55*X57*X59*X60"),  # with 67
    "k9_x": stim.PauliString("X22*X33*X36*X38*X41*X55*X58*X61"), # with 68
    
    "k4_x": stim.PauliString("X1*X2*X4*X12*X13*X14*X17*X24*X25*X26*X27*X31*X34*X35*X44*X60*X63*X64"),
    "k2_x": stim.PauliString("X7*X10*X14*X17*X31*X34*X37*X54"), 
    "k5_x": stim.PauliString("X5*X7*X10*X37*X40*X46*X53*X54"),
    "k8_x": stim.PauliString("X4*X7*X17*X19*X21*X24*X31*X32*X37*X40*X43*X46"),
    "k6_x": stim.PauliString("X3*X18*X19*X21*X32*X38*X39*X43*X47*X55*X58*X61"), 
    
    "k10_x": stim.PauliString("X1*X11*X12*X20*X26*X27*X29*X30*X52*X59*X60*X64"),
    "k11_x": stim.PauliString("X2*X3*X8*X10*X17*X23*X24*X32*X34*X37*X43*X44*X45*X46*X47*X50*X53*X63"),
    "k12_x": stim.PauliString("X16*X18*X22*X36*X38*X39*X57*X61"),
    "k13_x": stim.PauliString("X2*X11*X12*X23*X26*X29*X48*X49*X50*X51*X62*X63"),
    "k14_x": stim.PauliString("X8*X9*X15*X23*X45*X49*X50*X51"),
    "k15_x": stim.PauliString("X3*X9*X11*X12*X16*X18*X23*X39*X42*X44*X45*X47*X48*X49*X52*X57*X60*X63"),
    "k16_x": stim.PauliString("X9*X15*X28*X42*X48*X49*X51*X62")
}

# Operator and Detector of S(T) gate

V_even = [0, 2, 3, 4, 6, 8, 9, 11, 13, 14, 16, 17, 18, 19, 23, 26, 27, 28, 30, 32, 33, 36, 37, 38, 40, 44, 48, 51, 53, 54, 58, 59, 60] # SQRT_Z
V_odd = [1, 5, 7, 10, 12, 15, 20, 21, 22, 24, 25, 29, 31, 34, 35, 39, 41, 42, 43, 45, 46, 47, 49, 50, 52, 55, 56, 57, 61, 62, 63, 64] # SQRT_Z_DAG


S_gate_track = {
    "k1_x": "k1_z + k26_z",
    "k7_x": "k2_z + k21_z",
    "k3_x": "k23_z + k2_z + k25_z + k22_z",
    "k9_x": "k34_z + k37_z",
    "k2_x": "k32_z + k11_z",
    "k4_x": "k35_z + k28_z + k32_z + k3_z",
    "k5_x": "k6_z + k38_z",
    "k6_x": "k44_z + k41_z + k4_z",
    "k8_x": "k41_z + k33_z + k39_z",
    "k10_x": "k15_z + k23_z + k2_z + k25_z + k22_z + k26_z + k30_z + k31_z + k42_z",
    "k11_x": "k9_z + k13_z + k38_z + k40_z",
    "k12_x": "k17_z + k37_z",
    "k13_x": "k24_z + k30_z + k46_z",
    "k14_x": "k9_z + k10_z",
    "k15_x": "k12_z + k17_z + k43_z + k45_z",
    "k16_x": "k29_z + k46_z"
}

# Aniclla: 15, 16, 17, 18, 19, 20

# 2D color code

stabilizers_s_x = {
    # --- 2D S-series X Stabilizers ---
    "s1_x": stim.PauliString("X89*X90*X91*X92"),           # with 67  
    "s2_x": stim.PauliString("X90*X92*X94*X95"),           # with 65
    "s6_x": stim.PauliString("X94*X95*X97*X98*X101*X102"),  # with 73
    "s4_x": stim.PauliString("X98*X102*X106*X107"),        # with 71    
    "s3_x": stim.PauliString("X91*X92*X93*X94*X96*X97"),   # with 66
    "s5_x": stim.PauliString("X93*X96*X99*X100"),          # with 70    
    "s7_x": stim.PauliString("X99*X100*X103*X104"),        # with 68
    "s8_x": stim.PauliString("X96*X97*X100*X101*X104*X105"),# with 69
    "s9_x": stim.PauliString("X101*X102*X105*X106"),       # with 72
}

stabilizers_s_z = {
    # Specified Stabilizers

    "s1_z": stim.PauliString("Z89*Z90*Z91*Z92"),  # with 65
    "s2_z": stim.PauliString("Z90*Z92*Z94*Z95"),  # with 66
    "s6_z": stim.PauliString("Z94*Z95*Z97*Z98*Z101*Z102"),  # with 67
    "s4_z": stim.PauliString("Z98*Z102*Z106*Z107"),  # with 68
    
    # Remaining Stabilizers 

    "s3_z": stim.PauliString("Z91*Z92*Z93*Z94*Z96*Z97"),
    "s5_z": stim.PauliString("Z93*Z96*Z99*Z100"),
    "s7_z": stim.PauliString("Z99*Z100*Z103*Z104"),
    "s8_z": stim.PauliString("Z96*Z97*Z100*Z101*Z104*Z105"),
    "s9_z": stim.PauliString("Z101*Z102*Z105*Z106")
}

# --- matching logical operators --- 
    # 3D (X):    0,  4,  5,  6,  7, 13, 14, 19, 21, 25, 31, 33, 35, 40, 41, 54, 55, 56, 58
    
    # 2D (Z/X): 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107
    # 2D (Z/X):  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10,  11,  12,  13,  14,  15,  16,  17,  18

# Enlargable stabilizers Face to Face

stabilizers_added_X = {
    # --- Added M-series X Stabilizers ---
    "m1_x": stim.PauliString("X0*X89*X67"),  # 1(3D) 0(2D) 67
    "m2_x": stim.PauliString("X56*X90*X65*X67*X84"),  # 57(3D) 1(2D) 65 67 84
    "m3_x": stim.PauliString("X35*X91*X66*X67*X86"),  # 36(3D) 2(2D) 66 67 86
    "m4_x": stim.PauliString("X13*X92*X65*X66*X67*X81*X84*X86"),  # 14(3D) 3(2D) 65 66 67 81 84 86
    "m5_x": stim.PauliString("X14*X93*X66*X70*X87"),  # 15(3D) 4(2D) 66 70 87
    "m6_x": stim.PauliString("X25*X94*X65*X66*X73*X78*X80*X81"),  # 26(3D) 5(2D) 65 66 73 78 80 81
    "m7_x": stim.PauliString("X6*X95*X65*X73*X78"),  # 7(3D) 6(2D) 65 73 78 
    "m8_x": stim.PauliString("X31*X96*X66*X69*X70*X82*X85*X87"),   # 32(3D) 7(2D) 66 69 70 82 85 87
    "m9_x": stim.PauliString("X4*X97*X66*X69*X73*X79*X80*X82"),    # 5(3D) 8(2D) 66 69 73 79 80 82
    "m10_x": stim.PauliString("X33*X98*X71*X73*X75"),   # 34(3D) 9(2D) 71 73 75
    "m11_x": stim.PauliString("X54*X99*X68*X70*X88"),   # 55(3D) 10(2D) 68 70 88
    "m12_x": stim.PauliString("X7*X100*X68*X69*X70*X83*X85*X88"),   # 8(3D) 11(2D) 68 69 70 83 85 88
    "m13_x": stim.PauliString("X21*X101*X69*X72*X73*X76*X77*X79"),   # 22(3D) 12(2D) 69 72 73 76 77 79
    "m14_x": stim.PauliString("X55*X102*X71*X72*X73*X74*X75*X76"),   # 56(3D) 13(2D) 71 72 73 74 75 76
    "m15_x": stim.PauliString("X5*X103*X68"),   # 6(3D) 14(2D) 68
    "m16_x": stim.PauliString("X40*X104*X68*X69*X83"),   # 41(3D) 15(2D) 68 69 83
    "m17_x": stim.PauliString("X19*X105*X69*X72*X77"),   # 20(3D) 16(2D) 69 72 77
    "m18_x": stim.PauliString("X58*X106*X71*X72*X74"),   # 59(3D) 17(2D) 71 72 74
    "m19_x": stim.PauliString("X41*X107*X71"),   # 42(3D) 18(2D) 71
}

# --- matching logical operators --- 
    # 3D (X):    0,  4,  5,  6,  7, 13, 14, 19, 21, 25, 31, 33, 35, 40, 41, 54, 55, 56, 58
    
    # 2D (Z/X): 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107
    # 2D (Z/X):  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10,  11,  12,  13,  14,  15,  16,  17,  18


stabilizers_k_z_enlargable = {
    "k1_z":  stim.PauliString("Z0*Z13*Z35*Z56"),             # with 67
    "k7_z":  stim.PauliString("Z6*Z13*Z25*Z56"),             # with 65
    "k15_z": stim.PauliString("Z4*Z6*Z21*Z25*Z33*Z55"),      # with 73
    "k34_z": stim.PauliString("Z33*Z41*Z55*Z58"),            # with 71
    "k5_z":  stim.PauliString("Z4*Z13*Z14*Z25*Z31*Z35"),     # with 66
    "k14_z": stim.PauliString("Z7*Z14*Z31*Z54"),             # with 70    
    "k6_z":  stim.PauliString("Z5*Z7*Z40*Z54"),              # with 68
    "k8_z":  stim.PauliString("Z4*Z7*Z19*Z21*Z31*Z40"),      # with 69
    "k20_z": stim.PauliString("Z19*Z21*Z55*Z58"),            # with 72

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

}

stabilizers_k_z_enlargable_horizontal = {
    "k1_z":  stim.PauliString("Z0*Z13*Z35*Z56"),             # with 67
    "k7_z":  stim.PauliString("Z6*Z13*Z25*Z56"),             # with 65
    "k15_z": stim.PauliString("Z4*Z6*Z21*Z25*Z33*Z55"),      # with 73
    "k34_z": stim.PauliString("Z33*Z41*Z55*Z58"),            # with 71
    "k5_z":  stim.PauliString("Z4*Z13*Z14*Z25*Z31*Z35"),     # with 66
    "k14_z": stim.PauliString("Z7*Z14*Z31*Z54"),             # with 70    
    "k6_z":  stim.PauliString("Z5*Z7*Z40*Z54"),              # with 68
    "k8_z":  stim.PauliString("Z4*Z7*Z19*Z21*Z31*Z40"),      # with 69
    "k20_z": stim.PauliString("Z19*Z21*Z55*Z58"),            # with 72
}

stabilizers_k_z_enlargable_vertical = {
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
}
    
stabilizers_k_z_enlarged = {
    "k1_z":  stim.PauliString("Z0*Z13*Z35*Z56*Z67"),             # with 67
    "k7_z":  stim.PauliString("Z6*Z13*Z25*Z56*Z65"),             # with 65
    "k15_z": stim.PauliString("Z4*Z6*Z21*Z25*Z33*Z55*Z73"),      # with 73
    "k34_z": stim.PauliString("Z33*Z41*Z55*Z58*Z71"),            # with 71
    "k5_z":  stim.PauliString("Z4*Z13*Z14*Z25*Z31*Z35*Z66"),     # with 66
    "k14_z": stim.PauliString("Z7*Z14*Z31*Z54*Z70"),             # with 70    
    "k6_z":  stim.PauliString("Z5*Z7*Z40*Z54*Z68"),              # with 68
    "k8_z":  stim.PauliString("Z4*Z7*Z19*Z21*Z31*Z40*Z69"),      # with 69
    "k20_z": stim.PauliString("Z19*Z21*Z55*Z58*Z72"),            # with 72

    "k44_z": stim.PauliString("Z38*Z55*Z58*Z61*Z74"),            # with 74
    "k23_z": stim.PauliString("Z22*Z33*Z38*Z55*Z75"),            # with 75
    "k19_z": stim.PauliString("Z18*Z21*Z32*Z38*Z47*Z55*Z76"),    # with 76
    "k41_z": stim.PauliString("Z19*Z21*Z32*Z43*Z77"),            # with 77
    "k2_z":  stim.PauliString("Z1*Z6*Z25*Z59*Z78"),              # with 78  
    "k25_z": stim.PauliString("Z4*Z21*Z24*Z32*Z79"),             # with 79  
    "k35_z": stim.PauliString("Z1*Z4*Z24*Z25*Z44*Z60*Z80"),      # with 80 
    "k36_z": stim.PauliString("Z1*Z13*Z25*Z27*Z81"),             # with 81
    "k33_z": stim.PauliString("Z4*Z17*Z24*Z31*Z82"),             # with 82      
    "k39_z": stim.PauliString("Z7*Z37*Z40*Z46*Z83"),             # with 83
    "k21_z": stim.PauliString("Z13*Z20*Z27*Z56*Z84"),            # with 84
    "k18_z": stim.PauliString("Z7*Z17*Z31*Z37*Z85"),             # with 85
    "k28_z": stim.PauliString("Z13*Z27*Z35*Z64*Z86"),            # with 86
    "k32_z": stim.PauliString("Z14*Z17*Z31*Z34*Z87"),            # with 87        
    "k11_z": stim.PauliString("Z7*Z10*Z37*Z54*Z88"),             # with 88
}

stabilizers_s_z_enlarged = {
    "s1_z": stim.PauliString("Z89*Z90*Z91*Z92*Z67"),           # with 67  
    "s2_z": stim.PauliString("Z90*Z92*Z94*Z95*Z65"),           # with 65
    "s6_z": stim.PauliString("Z94*Z95*Z97*Z98*Z101*Z102*Z73"),  # with 73
    "s4_z": stim.PauliString("Z98*Z102*Z106*Z107*Z71"),        # with 71    
    "s3_z": stim.PauliString("Z91*Z92*Z93*Z94*Z96*Z97*Z66"),   # with 66
    "s5_z": stim.PauliString("Z93*Z96*Z99*Z100*Z70"),          # with 70    
    "s7_z": stim.PauliString("Z99*Z100*Z103*Z104*Z68"),        # with 68
    "s8_z": stim.PauliString("Z96*Z97*Z100*Z101*Z104*Z105*Z69"),# with 69
    "s9_z": stim.PauliString("Z101*Z102*Z105*Z106*Z72"),       # with 72
}

# Enlargable stabilizers String to String

stabilizers_added_Z = {
    "m1_z": stim.PauliString("Z0*Z89*Z65"),  # 1(3D) 0(2D) 65
    "m2_z": stim.PauliString("Z56*Z90*Z65*Z66"),  # 57(3D) 1(2D) 65 66
    "m3_z": stim.PauliString("Z6*Z95*Z66*Z67"),  # 7(3D) 6(2D) 66 67
    "m4_z": stim.PauliString("Z33*Z98*Z67*Z68"),  # 34(3D) 9(2D) 67 68
    "m5_z": stim.PauliString("Z41*Z107*Z68"),  # 42(3D) 18(2D) 68
}


# Ensure the logical ZZ are supported by all the physical qubits in a face
stabilizer_global = {
    "k6_z":  stim.PauliString("Z5*Z7*Z40*Z54"),
    "k5_z":  stim.PauliString("Z4*Z13*Z14*Z25*Z31*Z35"),
    "k20_z": stim.PauliString("Z19*Z21*Z55*Z58"),
    "s7_z": stim.PauliString("Z99*Z100*Z103*Z104"),
    "s3_z": stim.PauliString("Z91*Z92*Z93*Z94*Z96*Z97"),
    "s9_z": stim.PauliString("Z101*Z102*Z105*Z106"),
}

# --- matching logical operators --- 
    # 3D (X):    0,  4,  5,  6,  7, 13, 14, 19, 21, 25, 31, 33, 35, 40, 41, 54, 55, 56, 58
    
    # 2D (Z/X): 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107
    # 2D (Z/X):  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10,  11,  12,  13,  14,  15,  16,  17,  18


stabilizers_k_x_enlargable = {
    "k1_x": stim.PauliString("X0*X13*X20*X27*X30*X35*X56*X64"),  # with 65
    "k7_x": stim.PauliString("X1*X6*X13*X20*X25*X27*X56*X59"),  # with 66
    "k3_x": stim.PauliString("X1*X4*X6*X18*X21*X22*X24*X25*X32*X33*X38*X44*X47*X52*X55*X57*X59*X60"),  # with 67
    "k9_x": stim.PauliString("X22*X33*X36*X38*X41*X55*X58*X61"), # with 68

}

stabilizers_k_x_enlarged = {
    "k1_x": stim.PauliString("X0*X13*X20*X27*X30*X35*X56*X64*X65"),  # with 65
    "k7_x": stim.PauliString("X1*X6*X13*X20*X25*X27*X56*X59*X66"),  # with 66
    "k3_x": stim.PauliString("X1*X4*X6*X18*X21*X22*X24*X25*X32*X33*X38*X44*X47*X52*X55*X57*X59*X60*X67"),  # with 67
    "k9_x": stim.PauliString("X22*X33*X36*X38*X41*X55*X58*X61*X68"), # with 68

}

stabilizers_s_x_enlargable = {
    "s1_x": stim.PauliString("X89*X90*X91*X92"),  # with 65
    "s2_x": stim.PauliString("X90*X92*X94*X95"),  # with 66
    "s6_x": stim.PauliString("X94*X95*X97*X98*X101*X102"),  # with 67
    "s4_x": stim.PauliString("X98*X102*X106*X107"),  # with 68
}

stabilizers_s_x_enlarged = {
    "s1_x": stim.PauliString("X89*X90*X91*X92*X65"),  # with 65
    "s2_x": stim.PauliString("X90*X92*X94*X95*X66"),  # with 66
    "s6_x": stim.PauliString("X94*X95*X97*X98*X101*X102*X67"),  # with 67
    "s4_x": stim.PauliString("X98*X102*X106*X107*X68"),  # with 68
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
    
    c.append("R", [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88])
    # Ancillas stay in the Z basis after reset.
   
    return c

def lattice_surgery_Split(error_rate):
    
    c = stim.Circuit()

    c.append("M", [67, 65, 73, 71, 66, 70, 68, 69, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], tag="Measurement_ancilla", arg=error_rate)
    
    return c

def lattice_surgery_Merge_string():
    
    c = stim.Circuit()  
    
    c.append("R", [65, 66, 67, 68]); c.append("H", [65, 66, 67, 68])
   
    return c

def lattice_surgery_Split_string(error_rate):
    
    c = stim.Circuit()

    c.append("MX", [65, 66, 67, 68], tag="Measurement_ancilla_string", arg=error_rate)
    
    return c

def lattice_surgery_Reset_string():
    
    c = stim.Circuit()

    c.append("R", [65, 66, 67, 68])
    
    return c    

def measure_logical_qubits_3D() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("X0*X4*X5*X6*X7*X13*X14*X19*X21*X25*X31*X33*X35*X40*X41*X54*X55*X56*X58"), tag="logical_qubits_3D")
    c.append("OBSERVABLE_INCLUDE", [
        stim.target_rec(-1), ], 0)
    
    return c

def measure_logical_qubits_2D() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("Z89*Z90*Z91*Z92*Z93*Z94*Z95*Z96*Z97*Z98*Z99*Z100*Z101*Z102*Z103*Z104*Z105*Z106*Z107"), tag="logical_qubits_2D")
    c.append("OBSERVABLE_INCLUDE", [
        stim.target_rec(-1), ], 1)

    return c


def measurement_XX() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("Z0*Z4*Z5*Z6*Z7*Z13*Z14*Z19*Z21*Z25*Z31*Z33*Z35*Z40*Z41*Z54*Z55*Z56*Z58"), tag="logical_qubits_3D")
    c.append("MPP", stim.PauliString("X89*X90*X91*X92*X93*X94*X95*X96*X97*X98*X99*X100*X101*X102*X103*X104*X105*X106*X107"), tag="logical_qubits_2D") 
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

    control_qubits = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]  

    target_qubits = [0,  56,  35,  13,  14, 25, 6, 31, 4, 33, 54, 7, 21, 55, 5, 40, 19, 58, 41]

    c.append("CZ", [q for pair in zip(control_qubits, target_qubits) for q in pair])

    return c

DISTANCE = 5

__all__ = ['stabilizers_k_z', 'stabilizers_k_x', 'V_even', 'V_odd', 'S_gate_track', 'stabilizers_s_x', 'stabilizers_s_z', 'stabilizers_added_X', 'stabilizers_k_z_enlargable', 'stabilizers_k_z_enlargable_horizontal', 'stabilizers_k_z_enlargable_vertical', 'stabilizers_k_z_enlarged', 'stabilizers_s_z_enlarged', 'stabilizers_added_Z', 'stabilizer_global', 'stabilizers_k_x_enlargable', 'stabilizers_k_x_enlarged', 'stabilizers_s_x_enlargable', 'stabilizers_s_x_enlarged', 'stabilizers_general', 'stabilizers_k_z_unchange', 'stabilizers_merged', 'stabilizers_merged_without_add_X', 'stabilizers_k_x_unchange', 'stabilizers_s_x_unchange', 'stabilizers_merged_string', 'stabilizers_merged_string_without_add_Z', 'lattice_surgery_Merge', 'lattice_surgery_Split', 'lattice_surgery_Merge_string', 'lattice_surgery_Split_string', 'lattice_surgery_Reset_string', 'measure_logical_qubits_3D', 'measure_logical_qubits_2D', 'measurement_XX', 'S_Z_Gate', 'S_Z_DAG_Gate', 'logical_CZ', 'DISTANCE']
