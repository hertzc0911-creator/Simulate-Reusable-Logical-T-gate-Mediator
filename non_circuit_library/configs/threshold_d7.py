import stim

stabilizers_k_z = {
    "k1_z": stim.PauliString("Z43*Z68*Z100*Z157"),
    "k2_z": stim.PauliString("Z59*Z77*Z138*Z167"),
    "k3_z": stim.PauliString("Z54*Z57*Z62*Z168"),
    "k4_z": stim.PauliString("Z59*Z68*Z71*Z133*Z138*Z157"),
    "k5_z": stim.PauliString("Z5*Z54*Z77*Z167*Z168*Z171"),
    "k6_z": stim.PauliString("Z57*Z62*Z64*Z173"),
    "k7_z": stim.PauliString("Z98*Z100*Z133*Z157"),
    "k8_z": stim.PauliString("Z59*Z71*Z102*Z126*Z167*Z171"),
    "k9_z": stim.PauliString("Z5*Z54*Z62*Z88*Z132*Z173"),
    "k46_z": stim.PauliString("Z69*Z71*Z98*Z102*Z118*Z133"),
    "k47_z": stim.PauliString("Z5*Z81*Z95*Z126*Z132*Z171"),
    "k48_z": stim.PauliString("Z13*Z69*Z81*Z102*Z112*Z126"),
    "k49_z": stim.PauliString("Z88*Z95*Z132*Z174"),
    "k50_z": stim.PauliString("Z26*Z69*Z112*Z118"),
    "k51_z": stim.PauliString("Z12*Z13*Z81*Z95*Z96*Z174"),
    "k64_z": stim.PauliString("Z8*Z12*Z13*Z26*Z92*Z112"),
    "k65_z": stim.PauliString("Z8*Z12*Z14*Z96"),
    "k66_z": stim.PauliString("Z8*Z14*Z92*Z109"),
    "k87_z": stim.PauliString("Z22*Z57*Z62*Z87"),
    "k134_z": stim.PauliString("Z26*Z27*Z60*Z112"),
    "k111_z": stim.PauliString("Z39*Z81*Z95*Z124"),
    "k100_z": stim.PauliString("Z13*Z42*Z78*Z81*Z116*Z124"),
    "k121_z": stim.PauliString("Z41*Z45*Z55*Z125*Z167*Z171"),
    "k142_z": stim.PauliString("Z8*Z14*Z29*Z105"),
    "k81_z": stim.PauliString("Z54*Z131*Z134*Z168"),
    "k73_z": stim.PauliString("Z56*Z69*Z102*Z147"),
    "k83_z": stim.PauliString("Z56*Z60*Z69*Z93*Z112*Z144"),
    "k96_z": stim.PauliString("Z71*Z133*Z146*Z152"),
    "k201_z": stim.PauliString("Z1*Z8*Z29*Z92"),
    "k129_z": stim.PauliString("Z13*Z60*Z78*Z112"),
    "k116_z": stim.PauliString("Z81*Z124*Z126*Z140"),
    "k200_z": stim.PauliString("Z12*Z13*Z48*Z78"),
    "k194_z": stim.PauliString("Z8*Z12*Z29*Z48"),
    "k151_z": stim.PauliString("Z28*Z35*Z68*Z157"),
    "k153_z": stim.PauliString("Z5*Z15*Z19*Z54*Z101*Z131"),
    "k155_z": stim.PauliString("Z22*Z62*Z172*Z173"),
    "k118_z": stim.PauliString("Z5*Z19*Z125*Z171"),
    "k163_z": stim.PauliString("Z58*Z98*Z133*Z146"),
    "k176_z": stim.PauliString("Z28*Z61*Z133*Z136*Z146*Z157"),
    "k195_z": stim.PauliString("Z22*Z54*Z62*Z131"),
    "k174_z": stim.PauliString("Z32*Z59*Z137*Z138"),
    "k197_z": stim.PauliString("Z20*Z32*Z59*Z71*Z129*Z152"),
    "k203_z": stim.PauliString("Z32*Z45*Z59*Z167"),
    "k177_z": stim.PauliString("Z45*Z72*Z77*Z167"),
    "k179_z": stim.PauliString("Z28*Z100*Z154*Z157"),
    "k206_z": stim.PauliString("Z56*Z69*Z114*Z118"),
    "k105_z": stim.PauliString("Z71*Z102*Z147*Z152"),
    "k188_z": stim.PauliString("Z12*Z21*Z48*Z96"),
    "k162_z": stim.PauliString("Z7*Z39*Z95*Z174"),
    "k193_z": stim.PauliString("Z39*Z95*Z132*Z162"),
    "k213_z": stim.PauliString("Z88*Z122*Z132*Z162"),
    "k154_z": stim.PauliString("Z5*Z19*Z132*Z162"),
    "k140_z": stim.PauliString("Z30*Z91*Z102*Z126*Z140*Z147"),
    "k101_z": stim.PauliString("Z0*Z38*Z46*Z85*Z111*Z113"),
    "k102_z": stim.PauliString("Z41*Z49*Z84*Z151"),
    "k103_z": stim.PauliString("Z91*Z116*Z124*Z140"),
    "k104_z": stim.PauliString("Z2*Z6*Z65*Z117"),
    "k106_z": stim.PauliString("Z58*Z61*Z110*Z146"),
    "k107_z": stim.PauliString("Z31*Z42*Z89*Z116"),
    "k108_z": stim.PauliString("Z15*Z41*Z55*Z101*Z151*Z163"),
    "k110_z": stim.PauliString("Z18*Z33*Z53*Z106*Z160*Z164"),
    "k112_z": stim.PauliString("Z73*Z79*Z86*Z89"),
    "k113_z": stim.PauliString("Z25*Z86*Z89*Z91*Z116*Z120"),
    "k114_z": stim.PauliString("Z36*Z51*Z63*Z74"),
    "k117_z": stim.PauliString("Z3*Z33*Z106*Z161"),
    "k119_z": stim.PauliString("Z10*Z19*Z101*Z103*Z122*Z162"),
    "k11_z": stim.PauliString("Z37*Z50*Z66*Z70*Z110*Z139"),
    "k120_z": stim.PauliString("Z4*Z16*Z18*Z53*Z84*Z120"),
    "k122_z": stim.PauliString("Z18*Z20*Z164*Z169"),
    "k124_z": stim.PauliString("Z121*Z135*Z148*Z153"),
    "k125_z": stim.PauliString("Z11*Z75*Z143*Z170"),
    "k126_z": stim.PauliString("Z10*Z17*Z83*Z103"),
    "k128_z": stim.PauliString("Z11*Z47*Z67*Z75"),
    "k12_z": stim.PauliString("Z76*Z80*Z82*Z108*Z127*Z150"),
    "k130_z": stim.PauliString("Z53*Z61*Z70*Z110*Z129*Z160"),
    "k131_z": stim.PauliString("Z15*Z131*Z134*Z163"),
    "k132_z": stim.PauliString("Z28*Z136*Z139*Z154"),
    "k133_z": stim.PauliString("Z6*Z16*Z49*Z84*Z117*Z130"),
    "k135_z": stim.PauliString("Z111*Z121*Z135*Z142"),
    "k136_z": stim.PauliString("Z111*Z113*Z135*Z153"),
    "k137_z": stim.PauliString("Z3*Z33*Z34*Z46*Z149*Z160"),
    "k138_z": stim.PauliString("Z16*Z41*Z55*Z84"),
    "k139_z": stim.PauliString("Z18*Z49*Z84*Z164"),
    "k13_z": stim.PauliString("Z40*Z50*Z139*Z154"),
    "k141_z": stim.PauliString("Z22*Z87*Z158*Z172"),
    "k143_z": stim.PauliString("Z41*Z45*Z72*Z151"),
    "k144_z": stim.PauliString("Z3*Z108*Z127*Z161"),
    "k145_z": stim.PauliString("Z10*Z52*Z83*Z97*Z107*Z115"),
    "k146_z": stim.PauliString("Z7*Z39*Z79*Z89*Z116*Z124"),
    "k148_z": stim.PauliString("Z47*Z80*Z82*Z94"),
    "k149_z": stim.PauliString("Z9*Z17*Z83*Z107"),
    "k14_z": stim.PauliString("Z37*Z66*Z108*Z127"),
    "k150_z": stim.PauliString("Z47*Z67*Z82*Z155"),
    "k152_z": stim.PauliString("Z15*Z83*Z107*Z163"),
    "k156_z": stim.PauliString("Z11*Z47*Z82*Z150"),
    "k157_z": stim.PauliString("Z1*Z29*Z105*Z119"),
    "k158_z": stim.PauliString("Z25*Z65*Z85*Z99*Z117*Z130"),
    "k159_z": stim.PauliString("Z11*Z75*Z150*Z166"),
    "k15_z": stim.PauliString("Z80*Z82*Z155*Z156"),
    "k160_z": stim.PauliString("Z3*Z76*Z108*Z149"),
    "k161_z": stim.PauliString("Z21*Z31*Z42*Z48*Z78*Z104"),
    "k164_z": stim.PauliString("Z10*Z15*Z83*Z101"),
    "k165_z": stim.PauliString("Z25*Z38*Z85*Z86"),
    "k166_z": stim.PauliString("Z111*Z113*Z142*Z165"),
    "k167_z": stim.PauliString("Z24*Z44*Z97*Z115"),
    "k168_z": stim.PauliString("Z61*Z129*Z146*Z152"),
    "k169_z": stim.PauliString("Z6*Z52*Z97*Z117"),
    "k170_z": stim.PauliString("Z42*Z60*Z78*Z144"),
    "k171_z": stim.PauliString("Z23*Z38*Z73*Z86"),
    "k172_z": stim.PauliString("Z31*Z104*Z121*Z135"),
    "k173_z": stim.PauliString("Z24*Z52*Z97*Z123"),
    "k17_z": stim.PauliString("Z0*Z37*Z70*Z76*Z108*Z159"),
    "k180_z": stim.PauliString("Z34*Z70*Z159*Z160"),
    "k181_z": stim.PauliString("Z25*Z44*Z73*Z86*Z115*Z130"),
    "k183_z": stim.PauliString("Z27*Z60*Z144*Z145"),
    "k184_z": stim.PauliString("Z4*Z34*Z53*Z160"),
    "k185_z": stim.PauliString("Z4*Z30*Z53*Z129*Z147*Z152"),
    "k186_z": stim.PauliString("Z2*Z36*Z65*Z74"),
    "k189_z": stim.PauliString("Z51*Z74*Z143*Z170"),
    "k190_z": stim.PauliString("Z4*Z30*Z34*Z93*Z141*Z159"),
    "k191_z": stim.PauliString("Z31*Z42*Z135*Z144*Z145*Z153"),
    "k196_z": stim.PauliString("Z18*Z20*Z53*Z129"),
    "k202_z": stim.PauliString("Z97*Z115*Z117*Z130"),
    "k207_z": stim.PauliString("Z23*Z38*Z85*Z99*Z143*Z170"),
    "k20_z": stim.PauliString("Z9*Z17*Z24*Z44*Z103*Z123"),
    "k210_z": stim.PauliString("Z0*Z46*Z76*Z149"),
    "k212_z": stim.PauliString("Z65*Z74*Z99*Z170"),
    "k214_z": stim.PauliString("Z46*Z85*Z99*Z149"),
    "k21_z": stim.PauliString("Z51*Z63*Z67*Z75*Z128*Z143"),
    "k24_z": stim.PauliString("Z67*Z128*Z155*Z156"),
    "k30_z": stim.PauliString("Z50*Z66*Z90*Z106*Z164*Z169"),
    "k33_z": stim.PauliString("Z2*Z36*Z80*Z94*Z127*Z161"),
    "k36_z": stim.PauliString("Z2*Z6*Z49*Z106*Z161*Z164"),
    "k53_z": stim.PauliString("Z0*Z113*Z141*Z145*Z153*Z159"),
}

stabilizers_k_x = {
    "k1_x": stim.PauliString("X28*X35*X40*X43*X68*X100*X154*X157"),
    "k2_x": stim.PauliString("X32*X45*X59*X72*X77*X137*X138*X167"),
    "k3_x": stim.PauliString("X18*X20*X33*X37*X50*X53*X61*X66*X70*X90*X106*X110*X129*X136*X139*X160*X164*X169"),
    "k4_x": stim.PauliString("X22*X54*X57*X62*X87*X131*X134*X168"),
    "k5_x": stim.PauliString("X6*X10*X15*X16*X41*X49*X52*X55*X83*X84*X97*X101*X107*X115*X117*X130*X151*X163"),
    "k6_x": stim.PauliString("X2*X3*X11*X36*X47*X65*X74*X76*X80*X82*X94*X99*X108*X127*X149*X150*X161*X170"),
    "k7_x": stim.PauliString("X20*X28*X32*X35*X59*X61*X68*X71*X90*X129*X133*X136*X137*X138*X146*X152*X157*X169"),
    "k8_x": stim.PauliString("X5*X15*X19*X41*X45*X54*X55*X72*X77*X101*X125*X131*X134*X151*X163*X167*X168*X171"),
    "k9_x": stim.PauliString("X2*X3*X4*X6*X16*X18*X25*X33*X34*X46*X49*X53*X65*X84*X85*X99*X106*X117*X120*X130*X149*X160*X161*X164"),
    "k10_x": stim.PauliString("X22*X57*X62*X64*X87*X158*X172*X173"),
    "k11_x": stim.PauliString("X9*X10*X17*X24*X44*X52*X83*X97*X103*X107*X115*X123"),
    "k12_x": stim.PauliString("X11*X36*X47*X51*X63*X67*X74*X75*X94*X128*X143*X170"),
    "k13_x": stim.PauliString("X28*X35*X40*X50*X90*X136*X139*X154"),
    "k14_x": stim.PauliString("X18*X20*X32*X41*X45*X49*X72*X84*X137*X151*X164*X169"),
    "k15_x": stim.PauliString("X3*X33*X37*X66*X106*X108*X127*X161"),
    "k16_x": stim.PauliString("X9*X15*X17*X22*X83*X87*X107*X131*X134*X158*X163*X172"),
    "k17_x": stim.PauliString("X2*X6*X24*X36*X51*X52*X63*X65*X74*X97*X117*X123"),
    "k18_x": stim.PauliString("X47*X67*X80*X82*X94*X128*X155*X156"),
    "k19_x": stim.PauliString("X28*X58*X61*X98*X100*X110*X133*X136*X139*X146*X154*X157"),
    "k20_x": stim.PauliString("X4*X16*X18*X20*X30*X32*X41*X45*X53*X55*X59*X71*X84*X91*X102*X120*X125*X126*X129*X140*X147*X152*X167*X171"),
    "k21_x": stim.PauliString("X0*X3*X33*X34*X37*X46*X70*X76*X108*X149*X159*X160"),
    "k22_x": stim.PauliString("X5*X10*X15*X17*X19*X22*X54*X62*X83*X88*X101*X103*X122*X131*X132*X162*X172*X173"),
    "k23_x": stim.PauliString("X23*X24*X25*X38*X44*X51*X65*X73*X74*X85*X86*X97*X99*X115*X117*X130*X143*X170"),
    "k24_x": stim.PauliString("X11*X47*X67*X75*X82*X150*X155*X166"),
    "k25_x": stim.PauliString("X56*X58*X69*X71*X98*X102*X114*X118*X133*X146*X147*X152"),
    "k26_x": stim.PauliString("X5*X19*X39*X81*X95*X124*X125*X126*X132*X140*X162*X171"),
    "k27_x": stim.PauliString("X0*X4*X25*X30*X31*X34*X38*X42*X46*X85*X86*X89*X91*X93*X111*X113*X116*X120*X135*X141*X144*X145*X153*X159"),
    "k28_x": stim.PauliString("X13*X30*X42*X56*X60*X69*X78*X81*X91*X93*X102*X112*X116*X124*X126*X140*X144*X147"),
    "k29_x": stim.PauliString("X7*X39*X88*X95*X122*X132*X162*X174"),
    "k30_x": stim.PauliString("X23*X31*X38*X73*X79*X86*X89*X104*X111*X121*X135*X142"),
    "k31_x": stim.PauliString("X4*X30*X34*X53*X56*X58*X61*X70*X93*X110*X114*X129*X141*X146*X147*X152*X159*X160"),
    "k32_x": stim.PauliString("X7*X10*X16*X19*X25*X39*X44*X55*X73*X79*X86*X89*X91*X101*X103*X115*X116*X120*X122*X124*X125*X130*X140*X162"),
    "k33_x": stim.PauliString("X0*X11*X23*X38*X46*X75*X76*X85*X99*X111*X113*X142*X143*X149*X150*X165*X166*X170"),
    "k34_x": stim.PauliString("X26*X27*X56*X60*X69*X93*X112*X114*X118*X141*X144*X145"),
    "k35_x": stim.PauliString("X7*X12*X13*X21*X31*X39*X42*X48*X78*X79*X81*X89*X95*X96*X104*X116*X124*X174"),
    "k36_x": stim.PauliString("X111*X113*X121*X135*X142*X148*X153*X165"),
    "k37_x": stim.PauliString("X1*X8*X12*X13*X26*X27*X29*X48*X60*X78*X92*X112"),
    "k38_x": stim.PauliString("X8*X12*X14*X21*X29*X48*X96*X105"),
    "k39_x": stim.PauliString("X1*X21*X27*X29*X31*X42*X48*X60*X78*X104*X105*X119*X121*X135*X144*X145*X148*X153"),
    "k40_x": stim.PauliString("X1*X8*X14*X29*X92*X105*X109*X119")
}

logical_operators = {
    "logical_X": stim.PauliString("X5*X8*X12*X13*X14*X26*X43*X54*X57*X59*X62*X64*X68*X69*X71*X77*X81*X88*X92*X95*X96*X98*X100*X102*X109*X112*X118*X126*X132*X133*X138*X157*X167*X168*X171*X173*X174"),
    "logical_Z": stim.PauliString("Z109*Z119*Z148*Z155*Z156*Z165*Z166")
}

V_even = [0, 2, 3, 5, 8, 10, 11, 12, 17, 20, 21, 22, 25, 27, 30, 31, 35, 36, 38, 39, 40, 44, 45, 46, 49, 51, 53, 55, 57, 58, 59, 60, 66, 67, 69, 70, 72, 73, 78, 79, 80, 81, 82, 84, 88, 92, 93, 97, 99, 100, 101, 102, 105, 106, 107, 108, 116, 117, 118, 119, 120, 123, 128, 131, 135, 136, 138, 139, 140, 141, 142, 146, 152, 153, 157, 158, 160, 162, 163, 165, 166, 168, 169, 170, 171, 173, 174]
V_odd = [1, 4, 6, 7, 9, 13, 14, 15, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 37, 41, 42, 43, 47, 48, 50, 52, 54, 56, 61, 62, 63, 64, 65, 68, 71, 74, 75, 76, 77, 83, 85, 86, 87, 89, 90, 91, 94, 95, 96, 98, 103, 104, 109, 110, 111, 112, 113, 114, 115, 121, 122, 124, 125, 126, 127, 129, 130, 132, 133, 134, 137, 143, 144, 145, 147, 148, 149, 150, 151, 154, 155, 156, 159, 161, 164, 167, 172]

# Stabilizer set:
stabilizers_general = {**stabilizers_k_z, **stabilizers_k_x}

def measure_logical_qubits_3D_Z() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("Z109*Z119*Z148*Z155*Z156*Z165*Z166"), tag="logical_qubits_3D_Z")
    c.append("OBSERVABLE_INCLUDE", [
        stim.target_rec(-1), ], 0)
    return c

def measure_logical_qubits_3D_X() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("X5*X8*X12*X13*X14*X26*X43*X54*X57*X59*X62*X64*X68*X69*X71*X77*X81*X88*X92*X95*X96*X98*X100*X102*X109*X112*X118*X126*X132*X133*X138*X157*X167*X168*X171*X173*X174"), tag="logical_qubits_3D_X")
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

DISTANCE = 7

__all__ = ['stabilizers_k_z', 'stabilizers_k_x', 'logical_operators', 'V_even', 'V_odd', 'stabilizers_general', 'measure_logical_qubits_3D_Z', 'measure_logical_qubits_3D_X', 'S_Z_Gate', 'S_Z_DAG_Gate', 'DISTANCE']
