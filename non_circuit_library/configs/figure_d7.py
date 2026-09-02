import stim

# 3D color code

stabilizers_k_z = {
    "k1_z": stim.PauliString("Z43*Z68*Z100*Z157"),  # with 175
    "k7_z": stim.PauliString("Z98*Z100*Z133*Z157"),  # with 181
    "k46_z": stim.PauliString("Z69*Z71*Z98*Z102*Z118*Z133"),  # with 184
    "k50_z": stim.PauliString("Z26*Z69*Z112*Z118"),  # with 188
    "k64_z": stim.PauliString("Z8*Z12*Z13*Z26*Z92*Z112"),  # with 190
    "k66_z": stim.PauliString("Z8*Z14*Z92*Z109"),  # with 192
    "k51_z": stim.PauliString("Z12*Z13*Z81*Z95*Z96*Z174"),  # with 189
    "k48_z": stim.PauliString("Z13*Z69*Z81*Z102*Z112*Z126"),  # with 186
    "k47_z": stim.PauliString("Z5*Z81*Z95*Z126*Z132*Z171"),  # with 185
    "k8_z": stim.PauliString("Z59*Z71*Z102*Z126*Z167*Z171"),  # with 182
    "k9_z": stim.PauliString("Z5*Z54*Z62*Z88*Z132*Z173"),  # with 183
    "k4_z": stim.PauliString("Z59*Z68*Z71*Z133*Z138*Z157"),  # with 178
    "k5_z": stim.PauliString("Z5*Z54*Z77*Z167*Z168*Z171"),  # with 179
    "k65_z": stim.PauliString("Z8*Z12*Z14*Z96"),  # with 191
    "k49_z": stim.PauliString("Z88*Z95*Z132*Z174"),  # with 187
    "k6_z": stim.PauliString("Z57*Z62*Z64*Z173"),  # with 180
    "k2_z": stim.PauliString("Z59*Z77*Z138*Z167"),  # with 176
    "k3_z": stim.PauliString("Z54*Z57*Z62*Z168"),  # with 177

    "k87_z": stim.PauliString("Z22*Z57*Z62*Z87"),  # with 193
    "k134_z": stim.PauliString("Z26*Z27*Z60*Z112"),  # with 194
    "k111_z": stim.PauliString("Z39*Z81*Z95*Z124"),  # with 195
    "k100_z": stim.PauliString("Z13*Z42*Z78*Z81*Z116*Z124"),  # with 196
    "k121_z": stim.PauliString("Z41*Z45*Z55*Z125*Z167*Z171"),  # with 197
    "k142_z": stim.PauliString("Z8*Z14*Z29*Z105"),  # with 198
    "k81_z": stim.PauliString("Z54*Z131*Z134*Z168"),  # with 199
    "k73_z": stim.PauliString("Z56*Z69*Z102*Z147"),  # with 200
    "k83_z": stim.PauliString("Z56*Z60*Z69*Z93*Z112*Z144"),  # with 201
    "k96_z": stim.PauliString("Z71*Z133*Z146*Z152"),  # with 202
    "k201_z": stim.PauliString("Z1*Z8*Z29*Z92"),  # with 203
    "k129_z": stim.PauliString("Z13*Z60*Z78*Z112"),  # with 204
    "k116_z": stim.PauliString("Z81*Z124*Z126*Z140"),  # with 205
    "k200_z": stim.PauliString("Z12*Z13*Z48*Z78"),  # with 206
    "k194_z": stim.PauliString("Z8*Z12*Z29*Z48"),  # with 207
    "k151_z": stim.PauliString("Z28*Z35*Z68*Z157"),  # with 208
    "k153_z": stim.PauliString("Z5*Z15*Z19*Z54*Z101*Z131"),  # with 209
    "k155_z": stim.PauliString("Z22*Z62*Z172*Z173"),  # with 210
    "k118_z": stim.PauliString("Z5*Z19*Z125*Z171"),  # with 211
    "k163_z": stim.PauliString("Z58*Z98*Z133*Z146"),  # with 212
    "k176_z": stim.PauliString("Z28*Z61*Z133*Z136*Z146*Z157"),  # with 213
    "k195_z": stim.PauliString("Z22*Z54*Z62*Z131"),  # with 214
    "k174_z": stim.PauliString("Z32*Z59*Z137*Z138"),  # with 215
    "k197_z": stim.PauliString("Z20*Z32*Z59*Z71*Z129*Z152"),  # with 216
    "k203_z": stim.PauliString("Z32*Z45*Z59*Z167"),  # with 217
    "k177_z": stim.PauliString("Z45*Z72*Z77*Z167"),  # with 218
    "k179_z": stim.PauliString("Z28*Z100*Z154*Z157"),  # with 219
    "k206_z": stim.PauliString("Z56*Z69*Z114*Z118"),  # with 220
    "k105_z": stim.PauliString("Z71*Z102*Z147*Z152"),  # with 221
    "k188_z": stim.PauliString("Z12*Z21*Z48*Z96"),  # with 222
    "k162_z": stim.PauliString("Z7*Z39*Z95*Z174"),  # with 223
    "k193_z": stim.PauliString("Z39*Z95*Z132*Z162"),  # with 224
    "k213_z": stim.PauliString("Z88*Z122*Z132*Z162"),  # with 225
    "k154_z": stim.PauliString("Z5*Z19*Z132*Z162"),  # with 226
    "k140_z": stim.PauliString("Z30*Z91*Z102*Z126*Z140*Z147"),  # with 227

    
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
    "k1_x": stim.PauliString("X28*X35*X40*X43*X68*X100*X154*X157"),  # with 175
    "k19_x": stim.PauliString("X28*X58*X61*X98*X100*X110*X133*X136*X139*X146*X154*X157"),  # with 176
    "k25_x": stim.PauliString("X56*X58*X69*X71*X98*X102*X114*X118*X133*X146*X147*X152"),  # with 177
    "k34_x": stim.PauliString("X26*X27*X56*X60*X69*X93*X112*X114*X118*X141*X144*X145"),  # with 178
    "k37_x": stim.PauliString("X1*X8*X12*X13*X26*X27*X29*X48*X60*X78*X92*X112"),  # with 179
    "k40_x": stim.PauliString("X1*X8*X14*X29*X92*X105*X109*X119"),  # with 180

    "k35_x": stim.PauliString("X7*X12*X13*X21*X31*X39*X42*X48*X78*X79*X81*X89*X95*X96*X104*X116*X124*X174"),
    "k28_x": stim.PauliString("X13*X30*X42*X56*X60*X69*X78*X81*X91*X93*X102*X112*X116*X124*X126*X140*X144*X147"),
    "k26_x": stim.PauliString("X5*X19*X39*X81*X95*X124*X125*X126*X132*X140*X162*X171"),
    "k20_x": stim.PauliString("X4*X16*X18*X20*X30*X32*X41*X45*X53*X55*X59*X71*X84*X91*X102*X120*X125*X126*X129*X140*X147*X152*X167*X171"),
    "k22_x": stim.PauliString("X5*X10*X15*X17*X19*X22*X54*X62*X83*X88*X101*X103*X122*X131*X132*X162*X172*X173"),    
    "k7_x": stim.PauliString("X20*X28*X32*X35*X59*X61*X68*X71*X90*X129*X133*X136*X137*X138*X146*X152*X157*X169"),
    "k8_x": stim.PauliString("X5*X15*X19*X41*X45*X54*X55*X72*X77*X101*X125*X131*X134*X151*X163*X167*X168*X171"), 
    "k38_x": stim.PauliString("X8*X12*X14*X21*X29*X48*X96*X105"),
    "k29_x": stim.PauliString("X7*X39*X88*X95*X122*X132*X162*X174"),
    "k10_x": stim.PauliString("X22*X57*X62*X64*X87*X158*X172*X173"),
    "k2_x": stim.PauliString("X32*X45*X59*X72*X77*X137*X138*X167"),
    "k4_x": stim.PauliString("X22*X54*X57*X62*X87*X131*X134*X168"),
    
    "k3_x": stim.PauliString("X18*X20*X33*X37*X50*X53*X61*X66*X70*X90*X106*X110*X129*X136*X139*X160*X164*X169"),
    "k5_x": stim.PauliString("X6*X10*X15*X16*X41*X49*X52*X55*X83*X84*X97*X101*X107*X115*X117*X130*X151*X163"),
    "k6_x": stim.PauliString("X2*X3*X11*X36*X47*X65*X74*X76*X80*X82*X94*X99*X108*X127*X149*X150*X161*X170"),
    "k9_x": stim.PauliString("X2*X3*X4*X6*X16*X18*X25*X33*X34*X46*X49*X53*X65*X84*X85*X99*X106*X117*X120*X130*X149*X160*X161*X164"),
    "k11_x": stim.PauliString("X9*X10*X17*X24*X44*X52*X83*X97*X103*X107*X115*X123"),
    "k12_x": stim.PauliString("X11*X36*X47*X51*X63*X67*X74*X75*X94*X128*X143*X170"),
    "k13_x": stim.PauliString("X28*X35*X40*X50*X90*X136*X139*X154"),
    "k14_x": stim.PauliString("X18*X20*X32*X41*X45*X49*X72*X84*X137*X151*X164*X169"),
    "k15_x": stim.PauliString("X3*X33*X37*X66*X106*X108*X127*X161"),
    "k16_x": stim.PauliString("X9*X15*X17*X22*X83*X87*X107*X131*X134*X158*X163*X172"),
    "k17_x": stim.PauliString("X2*X6*X24*X36*X51*X52*X63*X65*X74*X97*X117*X123"),
    "k18_x": stim.PauliString("X47*X67*X80*X82*X94*X128*X155*X156"),
    "k21_x": stim.PauliString("X0*X3*X33*X34*X37*X46*X70*X76*X108*X149*X159*X160"),
    "k23_x": stim.PauliString("X23*X24*X25*X38*X44*X51*X65*X73*X74*X85*X86*X97*X99*X115*X117*X130*X143*X170"),
    "k24_x": stim.PauliString("X11*X47*X67*X75*X82*X150*X155*X166"),
    "k27_x": stim.PauliString("X0*X4*X25*X30*X31*X34*X38*X42*X46*X85*X86*X89*X91*X93*X111*X113*X116*X120*X135*X141*X144*X145*X153*X159"),
    "k30_x": stim.PauliString("X23*X31*X38*X73*X79*X86*X89*X104*X111*X121*X135*X142"),
    "k31_x": stim.PauliString("X4*X30*X34*X53*X56*X58*X61*X70*X93*X110*X114*X129*X141*X146*X147*X152*X159*X160"),
    "k32_x": stim.PauliString("X7*X10*X16*X19*X25*X39*X44*X55*X73*X79*X86*X89*X91*X101*X103*X115*X116*X120*X122*X124*X125*X130*X140*X162"),
    "k33_x": stim.PauliString("X0*X11*X23*X38*X46*X75*X76*X85*X99*X111*X113*X142*X143*X149*X150*X165*X166*X170"),
    "k36_x": stim.PauliString("X111*X113*X121*X135*X142*X148*X153*X165"),
    "k39_x": stim.PauliString("X1*X21*X27*X29*X31*X42*X48*X60*X78*X104*X105*X119*X121*X135*X144*X145*X148*X153"),

}

# Operator and Detector of S(T) gate

V_even = [0, 2, 3, 5, 8, 10, 11, 12, 17, 20, 21, 22, 25, 27, 30, 31, 35, 36, 38, 39, 40, 44, 45, 46, 49, 51, 53, 55, 57, 58, 59, 60, 66, 67, 69, 70, 72, 73, 78, 79, 80, 81, 82, 84, 88, 92, 93, 97, 99, 100, 101, 102, 105, 106, 107, 108, 116, 117, 118, 119, 120, 123, 128, 131, 135, 136, 138, 139, 140, 141, 142, 146, 152, 153, 157, 158, 160, 162, 163, 165, 166, 168, 169, 170, 171, 173, 174]
V_odd = [1, 4, 6, 7, 9, 13, 14, 15, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 37, 41, 42, 43, 47, 48, 50, 52, 54, 56, 61, 62, 63, 64, 65, 68, 71, 74, 75, 76, 77, 83, 85, 86, 87, 89, 90, 91, 94, 95, 96, 98, 103, 104, 109, 110, 111, 112, 113, 114, 115, 121, 122, 124, 125, 126, 127, 129, 130, 132, 133, 134, 137, 143, 144, 145, 147, 148, 149, 150, 151, 154, 155, 156, 159, 161, 164, 167, 172]



S_gate_track = {
    "k1_x": "k1_z + k2_z + k4_z + k96_z + k151_z + k177_z + k102_z + k110_z + k117_z + k11_z + k130_z + k139_z + k13_z + k143_z + k144_z + k14_z + k168_z",
    "k2_x": "k174_z + k177_z",
    "k3_x": "k7_z + k46_z + k50_z + k134_z + k111_z + k121_z + k116_z + k118_z + k197_z + k203_z + k179_z + k193_z + k154_z + k140_z + k101_z + k107_z + k113_z + k120_z + k130_z + k132_z + k136_z + k137_z + k138_z + k160_z + k165_z + k17_z + k180_z + k183_z + k185_z + k191_z + k30_z",
    "k4_x": "k87_z + k81_z",
    "k5_x": "k108_z + k133_z + k145_z",
    "k6_x": "k156_z + k160_z + k212_z + k33_z",
    "k7_x": "k7_z + k46_z + k50_z + k134_z + k111_z + k121_z + k96_z + k116_z + k151_z + k118_z + k174_z + k197_z + k203_z + k179_z + k193_z + k154_z + k140_z + k101_z + k107_z + k110_z + k113_z + k11_z + k120_z + k130_z + k132_z + k136_z + k137_z + k138_z + k160_z + k165_z + k17_z + k180_z + k183_z + k185_z + k191_z + k30_z",
    "k8_x": "k81_z + k118_z + k177_z + k108_z",
    "k9_x": "k120_z + k137_z + k158_z + k36_z",
    "k10_x": "k6_z + k141_z",
    "k11_x": "k145_z + k20_z",
    "k12_x": "k114_z + k125_z + k148_z + k15_z + k24_z",
    "k13_x": "k2_z + k4_z + k7_z + k46_z + k50_z + k134_z + k111_z + k121_z + k96_z + k116_z + k151_z + k118_z + k197_z + k203_z + k177_z + k179_z + k193_z + k154_z + k140_z + k101_z + k102_z + k107_z + k110_z + k113_z + k11_z + k120_z + k122_z + k130_z + k132_z + k136_z + k137_z + k138_z + k139_z + k13_z + k143_z + k160_z + k165_z + k168_z + k17_z + k180_z + k183_z + k185_z + k191_z + k30_z",
    "k14_x": "k2_z + k174_z + k177_z + k102_z + k122_z",
    "k15_x": "k117_z + k14_z",
    "k16_x": "k131_z + k141_z + k149_z",
    "k17_x": "k104_z + k114_z + k173_z",
    "k18_x": "k148_z + k24_z",
    "k19_x": "k7_z + k106_z + k132_z",
    "k20_x": "k121_z + k197_z + k140_z + k120_z",
    "k21_x": "k137_z + k17_z",
    "k22_x": "k153_z + k155_z + k213_z + k126_z",
    "k23_x": "k158_z + k167_z + k171_z + k189_z",
    "k24_x": "k150_z + k159_z",
    "k25_x": "k163_z + k206_z + k105_z",
    "k26_x": "k116_z + k118_z + k193_z",
    "k27_x": "k101_z + k113_z + k190_z + k191_z",
    "k28_x": "k100_z + k83_z + k140_z",
    "k29_x": "k162_z + k213_z",
    "k30_x": "k51_z + k100_z + k188_z + k162_z + k135_z + k146_z + k161_z + k171_z",
    "k31_x": "k46_z + k163_z + k206_z + k105_z + k130_z + k190_z",
    "k32_x": "k5_z + k49_z + k81_z + k118_z + k177_z + k162_z + k213_z + k103_z + k104_z + k108_z + k112_z + k117_z + k120_z + k131_z + k137_z + k139_z + k143_z + k145_z + k149_z + k158_z + k173_z + k184_z + k20_z + k214_z + k36_z",
    "k33_x": "k159_z + k166_z + k207_z + k210_z",
    "k34_x": "k46_z + k50_z + k163_z + k206_z + k105_z + k106_z + k130_z + k180_z + k183_z + k185_z + k190_z",
    "k35_x": "k51_z + k146_z + k161_z",
    "k36_x": "k124_z + k166_z",
    "k37_x": "k134_z + k201_z + k200_z",
    "k38_x": "k142_z + k188_z",
    "k39_x": "k124_z + k157_z + k161_z + k183_z",
    "k40_x": "k66_z + k157_z"
}


# 2D color code

stabilizers_s_x = { 
    "s15_x": stim.PauliString("X252*X253*X258*X259"), # with 175
    "s14_x": stim.PauliString("X242*X247*X252*X253"), # with 181
    "s4_x": stim.PauliString("X238*X239*X242*X243*X247*X248"), # with 184   
    "s12_x": stim.PauliString("X232*X235*X238*X239"), # with 188
    "s1_x": stim.PauliString("X230*X231*X232*X233*X235*X236"), # with 190
    "s10_x": stim.PauliString("X228*X229*X230*X231"), # with 192
    "s2_x": stim.PauliString("X233*X234*X236*X237*X240*X241"), # with 189
    "s3_x": stim.PauliString("X235*X236*X239*X240*X243*X244"), # with 186
    "s5_x": stim.PauliString("X240*X241*X244*X245*X249*X250"), # with 185
    "s6_x": stim.PauliString("X243*X244*X248*X249*X254*X255"), # with 182
    "s7_x": stim.PauliString("X245*X246*X250*X251*X256*X257"), # with 183
    "s8_x": stim.PauliString("X247*X248*X253*X254*X259*X260"), # with 178
    "s9_x": stim.PauliString("X249*X250*X255*X256*X261*X262"), # with 179    
    "s11_x": stim.PauliString("X229*X231*X233*X234"), # with 191
    "s13_x": stim.PauliString("X237*X241*X245*X246"), # with 187
    "s16_x": stim.PauliString("X251*X257*X263*X264"), # with 180 
    "s17_x": stim.PauliString("X254*X255*X260*X261"), # with 176
    "s18_x": stim.PauliString("X256*X257*X262*X263"), # with 177
}

stabilizers_s_z = {
    "s15_z": stim.PauliString("Z252*Z253*Z258*Z259"),  # with 175
    "s14_z": stim.PauliString("Z242*Z247*Z252*Z253"),  # with 176
    "s4_z": stim.PauliString("Z238*Z239*Z242*Z243*Z247*Z248"),  # with 177
    "s12_z": stim.PauliString("Z232*Z235*Z238*Z239"),  # with 178
    "s1_z": stim.PauliString("Z230*Z231*Z232*Z233*Z235*Z236"),  # with 179
    "s10_z": stim.PauliString("Z228*Z229*Z230*Z231"),  # with 180
    
    "s2_z": stim.PauliString("Z233*Z234*Z236*Z237*Z240*Z241"),
    "s3_z": stim.PauliString("Z235*Z236*Z239*Z240*Z243*Z244"),
    "s5_z": stim.PauliString("Z240*Z241*Z244*Z245*Z249*Z250"),
    "s6_z": stim.PauliString("Z243*Z244*Z248*Z249*Z254*Z255"),
    "s7_z": stim.PauliString("Z245*Z246*Z250*Z251*Z256*Z257"),
    "s8_z": stim.PauliString("Z247*Z248*Z253*Z254*Z259*Z260"),
    "s9_z": stim.PauliString("Z249*Z250*Z255*Z256*Z261*Z262"),
    "s11_z": stim.PauliString("Z229*Z231*Z233*Z234"),
    "s13_z": stim.PauliString("Z237*Z241*Z245*Z246"),
    "s16_z": stim.PauliString("Z251*Z257*Z263*Z264"),
    "s17_z": stim.PauliString("Z254*Z255*Z260*Z261"),
    "s18_z": stim.PauliString("Z256*Z257*Z262*Z263"),
}

# --- matching logical operators --- 
    # 3D (X):     5,   8,  12,  13,  14,  26,  43,  54,  57,  59,  62,  64,  68,  69,  71,  77,  81,  88,  92,  95,  96,  98, 100, 102, 109, 112, 118, 126, 132, 133, 138, 157, 167, 168, 171, 173, 174
    
    # 2D (Z/X): 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264
    # 2D (Z/X):   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36

# Enlargable stabilizers Face to Face

stabilizers_added_X = {
    # --- Added M-series X Stabilizers ---
    "m1_x": stim.PauliString("X109*X228*X192"),  # 110(3D) 0(2D) 192
    "m2_x": stim.PauliString("X14*X229*X192*X198*X191"),  # 15(3D) 1(2D) 192 198 191
    "m3_x": stim.PauliString("X92*X230*X192*X203*X190"),  # 93(3D) 2(2D) 192 203 190
    "m4_x": stim.PauliString("X8*X231*X192*X198*X203*X191*X190*X207"),  # 9(3D) 3(2D) 192 198 203 191 190 207
    "m5_x": stim.PauliString("X26*X232*X190*X194*X188"),  # 27(3D) 4(2D) 190 194 188
    "m6_x": stim.PauliString("X12*X233*X191*X207*X190*X222*X206*X189"),  # 13(3D) 5(2D) 191 207 190 222 206 189
    "m7_x": stim.PauliString("X96*X234*X191*X222*X189"),  # 97(3D) 6(2D) 191 222 189
    "m8_x": stim.PauliString("X112*X235*X190*X194*X188*X204*X201*X186"),  # 113(3D) 7(2D) 190 194 188 204 201 186
    "m9_x": stim.PauliString("X13*X236*X190*X206*X189*X204*X196*X186"),  # 14(3D) 8(2D) 190 206 189 204 196 186
    "m10_x": stim.PauliString("X174*X237*X189*X187*X223"), # 175(3D) 9(2D) 189 187 223
    "m11_x": stim.PauliString("X118*X238*X188*X184*X220"), # 119(3D) 10(2D) 188 184 220
    "m12_x": stim.PauliString("X69*X239*X188*X186*X184*X201*X220*X200"), # 70(3D) 11(2D) 188 186 184 201 220 200
    "m13_x": stim.PauliString("X81*X240*X186*X189*X185*X196*X195*X205"), # 82(3D) 12(2D) 186 189 185 196 195 205
    "m14_x": stim.PauliString("X95*X241*X189*X187*X185*X195*X223*X224"), # 96(3D) 13(2D) 189 187 185 195 223 224  
    "m15_x": stim.PauliString("X98*X242*X184*X181*X212"), # 99(3D) 14(2D) 184 181 212
    "m16_x": stim.PauliString("X102*X243*X186*X184*X182*X200*X221*X227"), # 103(3D) 15(2D) 186 184 182 200 221 227
    "m17_x": stim.PauliString("X126*X244*X186*X185*X182*X205*X227"), # 127(3D) 16(2D) 186 185 182 205 227
    "m18_x": stim.PauliString("X132*X245*X187*X185*X183*X224*X225*X226"), # 133(3D) 17(2D) 187 185 183 224 225 226
    "m19_x": stim.PauliString("X88*X246*X187*X183*X225"), # 89(3D) 18(2D) 187 183 225
    "m20_x": stim.PauliString("X133*X247*X184*X181*X178*X202*X212*X213"), # 134(3D) 19(2D) 184 181 178 202 212 213
    "m21_x": stim.PauliString("X71*X248*X184*X182*X178*X202*X216*X221"), # 72(3D) 20(2D) 184 182 178 202 216 221
    "m22_x": stim.PauliString("X171*X249*X185*X182*X179*X197*X211"), # 172(3D) 21(2D) 185 182 179 197 211
    "m23_x": stim.PauliString("X5*X250*X185*X183*X179*X209*X211*X226"), # 6(3D) 22(2D) 185 183 179 209 211 226
    "m24_x": stim.PauliString("X173*X251*X183*X180*X210"), # 174(3D) 23(2D) 183 180 210
    "m25_x": stim.PauliString("X100*X252*X181*X175*X219"), # 101(3D) 24(2D) 181 175 219
    "m26_x": stim.PauliString("X157*X253*X181*X178*X175*X208*X213*X219"), # 158(3D) 25(2D) 181 178 175 208 213 219
    "m27_x": stim.PauliString("X59*X254*X182*X178*X176*X215*X216*X217"), # 60(3D) 26(2D) 182 178 176 215 216 217
    "m28_x": stim.PauliString("X167*X255*X182*X179*X176*X197*X217*X218"), # 168(3D) 27(2D) 182 179 176 197 217 218
    "m29_x": stim.PauliString("X54*X256*X183*X179*X177*X199*X209*X214"), # 55(3D) 28(2D) 183 179 177 199 209 214
    "m30_x": stim.PauliString("X62*X257*X183*X180*X177*X193*X210*X214"), # 63(3D) 29(2D) 183 180 177 193 210 214
    "m31_x": stim.PauliString("X43*X258*X175"), # 44(3D) 30(2D) 175
    "m32_x": stim.PauliString("X68*X259*X178*X175*X208"), # 69(3D) 31(2D) 178 175 208
    "m33_x": stim.PauliString("X138*X260*X178*X176*X215"), # 139(3D) 32(2D) 178 176 215
    "m34_x": stim.PauliString("X77*X261*X176*X179*X218"), # 78(3D) 33(2D) 176 179 218
    "m35_x": stim.PauliString("X168*X262*X179*X177*X199"), # 169(3D) 34(2D) 179 177 199
    "m36_x": stim.PauliString("X57*X263*X180*X177*X193"), # 58(3D) 35(2D) 180 177 193
    "m37_x": stim.PauliString("X64*X264*X180"), # 65(3D) 36(2D) 180
}

# --- matching logical operators --- 
    # 3D (X):     5,   8,  12,  13,  14,  26,  43,  54,  57,  59,  62,  64,  68,  69,  71,  77,  81,  88,  92,  95,  96,  98, 100, 102, 109, 112, 118, 126, 132, 133, 138, 157, 167, 168, 171, 173, 174
    
    # 2D (Z/X): 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264
    # 2D (Z/X):   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36


stabilizers_k_z_enlargable = {

    # Horizontal
    "k1_z": stim.PauliString("Z43*Z68*Z100*Z157"),  # with 175
    "k7_z": stim.PauliString("Z98*Z100*Z133*Z157"),  # with 181
    "k46_z": stim.PauliString("Z69*Z71*Z98*Z102*Z118*Z133"),  # with 184
    "k50_z": stim.PauliString("Z26*Z69*Z112*Z118"),  # with 188
    "k64_z": stim.PauliString("Z8*Z12*Z13*Z26*Z92*Z112"),  # with 190
    "k66_z": stim.PauliString("Z8*Z14*Z92*Z109"),  # with 192
    "k51_z": stim.PauliString("Z12*Z13*Z81*Z95*Z96*Z174"),  # with 189
    "k48_z": stim.PauliString("Z13*Z69*Z81*Z102*Z112*Z126"),  # with 186
    "k47_z": stim.PauliString("Z5*Z81*Z95*Z126*Z132*Z171"),  # with 185
    "k8_z": stim.PauliString("Z59*Z71*Z102*Z126*Z167*Z171"),  # with 182
    "k9_z": stim.PauliString("Z5*Z54*Z62*Z88*Z132*Z173"),  # with 183
    "k4_z": stim.PauliString("Z59*Z68*Z71*Z133*Z138*Z157"),  # with 178
    "k5_z": stim.PauliString("Z5*Z54*Z77*Z167*Z168*Z171"),  # with 179
    "k65_z": stim.PauliString("Z8*Z12*Z14*Z96"),  # with 191
    "k49_z": stim.PauliString("Z88*Z95*Z132*Z174"),  # with 187
    "k6_z": stim.PauliString("Z57*Z62*Z64*Z173"),  # with 180
    "k2_z": stim.PauliString("Z59*Z77*Z138*Z167"),  # with 176
    "k3_z": stim.PauliString("Z54*Z57*Z62*Z168"),  # with 177

    # Vertical
    "k87_z": stim.PauliString("Z22*Z57*Z62*Z87"),  # with 193
    "k134_z": stim.PauliString("Z26*Z27*Z60*Z112"),  # with 194
    "k111_z": stim.PauliString("Z39*Z81*Z95*Z124"),  # with 195
    "k100_z": stim.PauliString("Z13*Z42*Z78*Z81*Z116*Z124"),  # with 196
    "k121_z": stim.PauliString("Z41*Z45*Z55*Z125*Z167*Z171"),  # with 197
    "k142_z": stim.PauliString("Z8*Z14*Z29*Z105"),  # with 198
    "k81_z": stim.PauliString("Z54*Z131*Z134*Z168"),  # with 199
    "k73_z": stim.PauliString("Z56*Z69*Z102*Z147"),  # with 200
    "k83_z": stim.PauliString("Z56*Z60*Z69*Z93*Z112*Z144"),  # with 201
    "k96_z": stim.PauliString("Z71*Z133*Z146*Z152"),  # with 202
    "k201_z": stim.PauliString("Z1*Z8*Z29*Z92"),  # with 203
    "k129_z": stim.PauliString("Z13*Z60*Z78*Z112"),  # with 204
    "k116_z": stim.PauliString("Z81*Z124*Z126*Z140"),  # with 205
    "k200_z": stim.PauliString("Z12*Z13*Z48*Z78"),  # with 206
    "k194_z": stim.PauliString("Z8*Z12*Z29*Z48"),  # with 207
    "k151_z": stim.PauliString("Z28*Z35*Z68*Z157"),  # with 208
    "k153_z": stim.PauliString("Z5*Z15*Z19*Z54*Z101*Z131"),  # with 209
    "k155_z": stim.PauliString("Z22*Z62*Z172*Z173"),  # with 210
    "k118_z": stim.PauliString("Z5*Z19*Z125*Z171"),  # with 211
    "k163_z": stim.PauliString("Z58*Z98*Z133*Z146"),  # with 212
    "k176_z": stim.PauliString("Z28*Z61*Z133*Z136*Z146*Z157"),  # with 213
    "k195_z": stim.PauliString("Z22*Z54*Z62*Z131"),  # with 214
    "k174_z": stim.PauliString("Z32*Z59*Z137*Z138"),  # with 215
    "k197_z": stim.PauliString("Z20*Z32*Z59*Z71*Z129*Z152"),  # with 216
    "k203_z": stim.PauliString("Z32*Z45*Z59*Z167"),  # with 217
    "k177_z": stim.PauliString("Z45*Z72*Z77*Z167"),  # with 218
    "k179_z": stim.PauliString("Z28*Z100*Z154*Z157"),  # with 219
    "k206_z": stim.PauliString("Z56*Z69*Z114*Z118"),  # with 220
    "k105_z": stim.PauliString("Z71*Z102*Z147*Z152"),  # with 221
    "k188_z": stim.PauliString("Z12*Z21*Z48*Z96"),  # with 222
    "k162_z": stim.PauliString("Z7*Z39*Z95*Z174"),  # with 223
    "k193_z": stim.PauliString("Z39*Z95*Z132*Z162"),  # with 224
    "k213_z": stim.PauliString("Z88*Z122*Z132*Z162"),  # with 225
    "k154_z": stim.PauliString("Z5*Z19*Z132*Z162"),  # with 226
    "k140_z": stim.PauliString("Z30*Z91*Z102*Z126*Z140*Z147"),  # with 227
}

stabilizers_k_z_enlargable_horizontal = {
    "k1_z": stim.PauliString("Z43*Z68*Z100*Z157"),  # with 175
    "k7_z": stim.PauliString("Z98*Z100*Z133*Z157"),  # with 181
    "k46_z": stim.PauliString("Z69*Z71*Z98*Z102*Z118*Z133"),  # with 184
    "k50_z": stim.PauliString("Z26*Z69*Z112*Z118"),  # with 188
    "k64_z": stim.PauliString("Z8*Z12*Z13*Z26*Z92*Z112"),  # with 190
    "k66_z": stim.PauliString("Z8*Z14*Z92*Z109"),  # with 192
    "k51_z": stim.PauliString("Z12*Z13*Z81*Z95*Z96*Z174"),  # with 189
    "k48_z": stim.PauliString("Z13*Z69*Z81*Z102*Z112*Z126"),  # with 186
    "k47_z": stim.PauliString("Z5*Z81*Z95*Z126*Z132*Z171"),  # with 185
    "k8_z": stim.PauliString("Z59*Z71*Z102*Z126*Z167*Z171"),  # with 182
    "k9_z": stim.PauliString("Z5*Z54*Z62*Z88*Z132*Z173"),  # with 183
    "k4_z": stim.PauliString("Z59*Z68*Z71*Z133*Z138*Z157"),  # with 178
    "k5_z": stim.PauliString("Z5*Z54*Z77*Z167*Z168*Z171"),  # with 179
    "k65_z": stim.PauliString("Z8*Z12*Z14*Z96"),  # with 191
    "k49_z": stim.PauliString("Z88*Z95*Z132*Z174"),  # with 187
    "k6_z": stim.PauliString("Z57*Z62*Z64*Z173"),  # with 180
    "k2_z": stim.PauliString("Z59*Z77*Z138*Z167"),  # with 176
    "k3_z": stim.PauliString("Z54*Z57*Z62*Z168"),  # with 177
}

stabilizers_k_z_enlargable_vertical = {
    "k87_z": stim.PauliString("Z22*Z57*Z62*Z87"),  # with 193
    "k134_z": stim.PauliString("Z26*Z27*Z60*Z112"),  # with 194
    "k111_z": stim.PauliString("Z39*Z81*Z95*Z124"),  # with 195
    "k100_z": stim.PauliString("Z13*Z42*Z78*Z81*Z116*Z124"),  # with 196
    "k121_z": stim.PauliString("Z41*Z45*Z55*Z125*Z167*Z171"),  # with 197
    "k142_z": stim.PauliString("Z8*Z14*Z29*Z105"),  # with 198
    "k81_z": stim.PauliString("Z54*Z131*Z134*Z168"),  # with 199
    "k73_z": stim.PauliString("Z56*Z69*Z102*Z147"),  # with 200
    "k83_z": stim.PauliString("Z56*Z60*Z69*Z93*Z112*Z144"),  # with 201
    "k96_z": stim.PauliString("Z71*Z133*Z146*Z152"),  # with 202
    "k201_z": stim.PauliString("Z1*Z8*Z29*Z92"),  # with 203
    "k129_z": stim.PauliString("Z13*Z60*Z78*Z112"),  # with 204
    "k116_z": stim.PauliString("Z81*Z124*Z126*Z140"),  # with 205
    "k200_z": stim.PauliString("Z12*Z13*Z48*Z78"),  # with 206
    "k194_z": stim.PauliString("Z8*Z12*Z29*Z48"),  # with 207
    "k151_z": stim.PauliString("Z28*Z35*Z68*Z157"),  # with 208
    "k153_z": stim.PauliString("Z5*Z15*Z19*Z54*Z101*Z131"),  # with 209
    "k155_z": stim.PauliString("Z22*Z62*Z172*Z173"),  # with 210
    "k118_z": stim.PauliString("Z5*Z19*Z125*Z171"),  # with 211
    "k163_z": stim.PauliString("Z58*Z98*Z133*Z146"),  # with 212
    "k176_z": stim.PauliString("Z28*Z61*Z133*Z136*Z146*Z157"),  # with 213
    "k195_z": stim.PauliString("Z22*Z54*Z62*Z131"),  # with 214
    "k174_z": stim.PauliString("Z32*Z59*Z137*Z138"),  # with 215
    "k197_z": stim.PauliString("Z20*Z32*Z59*Z71*Z129*Z152"),  # with 216
    "k203_z": stim.PauliString("Z32*Z45*Z59*Z167"),  # with 217
    "k177_z": stim.PauliString("Z45*Z72*Z77*Z167"),  # with 218
    "k179_z": stim.PauliString("Z28*Z100*Z154*Z157"),  # with 219
    "k206_z": stim.PauliString("Z56*Z69*Z114*Z118"),  # with 220
    "k105_z": stim.PauliString("Z71*Z102*Z147*Z152"),  # with 221
    "k188_z": stim.PauliString("Z12*Z21*Z48*Z96"),  # with 222
    "k162_z": stim.PauliString("Z7*Z39*Z95*Z174"),  # with 223
    "k193_z": stim.PauliString("Z39*Z95*Z132*Z162"),  # with 224
    "k213_z": stim.PauliString("Z88*Z122*Z132*Z162"),  # with 225
    "k154_z": stim.PauliString("Z5*Z19*Z132*Z162"),  # with 226
    "k140_z": stim.PauliString("Z30*Z91*Z102*Z126*Z140*Z147"),  # with 227
}
    
stabilizers_k_z_enlarged = {
    # Horizontal
    "k1_z": stim.PauliString("Z43*Z68*Z100*Z157*Z175"),  # with 175
    "k7_z": stim.PauliString("Z98*Z100*Z133*Z157*Z181"),  # with 181
    "k46_z": stim.PauliString("Z69*Z71*Z98*Z102*Z118*Z133*Z184"),  # with 184
    "k50_z": stim.PauliString("Z26*Z69*Z112*Z118*Z188"),  # with 188
    "k64_z": stim.PauliString("Z8*Z12*Z13*Z26*Z92*Z112*Z190"),  # with 190
    "k66_z": stim.PauliString("Z8*Z14*Z92*Z109*Z192"),  # with 192
    "k51_z": stim.PauliString("Z12*Z13*Z81*Z95*Z96*Z174*Z189"),  # with 189
    "k48_z": stim.PauliString("Z13*Z69*Z81*Z102*Z112*Z126*Z186"),  # with 186
    "k47_z": stim.PauliString("Z5*Z81*Z95*Z126*Z132*Z171*Z185"),  # with 185
    "k8_z": stim.PauliString("Z59*Z71*Z102*Z126*Z167*Z171*Z182"),  # with 182
    "k9_z": stim.PauliString("Z5*Z54*Z62*Z88*Z132*Z173*Z183"),  # with 183
    "k4_z": stim.PauliString("Z59*Z68*Z71*Z133*Z138*Z157*Z178"),  # with 178
    "k5_z": stim.PauliString("Z5*Z54*Z77*Z167*Z168*Z171*Z179"),  # with 179
    "k65_z": stim.PauliString("Z8*Z12*Z14*Z96*Z191"),  # with 191
    "k49_z": stim.PauliString("Z88*Z95*Z132*Z174*Z187"),  # with 187
    "k6_z": stim.PauliString("Z57*Z62*Z64*Z173*Z180"),  # with 180
    "k2_z": stim.PauliString("Z59*Z77*Z138*Z167*Z176"),  # with 176
    "k3_z": stim.PauliString("Z54*Z57*Z62*Z168*Z177"),  # with 177

    # Vertical
    "k87_z": stim.PauliString("Z22*Z57*Z62*Z87*Z193"),  # with 193
    "k134_z": stim.PauliString("Z26*Z27*Z60*Z112*Z194"),  # with 194
    "k111_z": stim.PauliString("Z39*Z81*Z95*Z124*Z195"),  # with 195
    "k100_z": stim.PauliString("Z13*Z42*Z78*Z81*Z116*Z124*Z196"),  # with 196
    "k121_z": stim.PauliString("Z41*Z45*Z55*Z125*Z167*Z171*Z197"),  # with 197
    "k142_z": stim.PauliString("Z8*Z14*Z29*Z105*Z198"),  # with 198
    "k81_z": stim.PauliString("Z54*Z131*Z134*Z168*Z199"),  # with 199
    "k73_z": stim.PauliString("Z56*Z69*Z102*Z147*Z200"),  # with 200
    "k83_z": stim.PauliString("Z56*Z60*Z69*Z93*Z112*Z144*Z201"),  # with 201
    "k96_z": stim.PauliString("Z71*Z133*Z146*Z152*Z202"),  # with 202
    "k201_z": stim.PauliString("Z1*Z8*Z29*Z92*Z203"),  # with 203
    "k129_z": stim.PauliString("Z13*Z60*Z78*Z112*Z204"),  # with 204
    "k116_z": stim.PauliString("Z81*Z124*Z126*Z140*Z205"),  # with 205
    "k200_z": stim.PauliString("Z12*Z13*Z48*Z78*Z206"),  # with 206
    "k194_z": stim.PauliString("Z8*Z12*Z29*Z48*Z207"),  # with 207
    "k151_z": stim.PauliString("Z28*Z35*Z68*Z157*Z208"),  # with 208
    "k153_z": stim.PauliString("Z5*Z15*Z19*Z54*Z101*Z131*Z209"),  # with 209
    "k155_z": stim.PauliString("Z22*Z62*Z172*Z173*Z210"),  # with 210
    "k118_z": stim.PauliString("Z5*Z19*Z125*Z171*Z211"),  # with 211
    "k163_z": stim.PauliString("Z58*Z98*Z133*Z146*Z212"),  # with 212
    "k176_z": stim.PauliString("Z28*Z61*Z133*Z136*Z146*Z157*Z213"),  # with 213
    "k195_z": stim.PauliString("Z22*Z54*Z62*Z131*Z214"),  # with 214
    "k174_z": stim.PauliString("Z32*Z59*Z137*Z138*Z215"),  # with 215
    "k197_z": stim.PauliString("Z20*Z32*Z59*Z71*Z129*Z152*Z216"),  # with 216
    "k203_z": stim.PauliString("Z32*Z45*Z59*Z167*Z217"),  # with 217
    "k177_z": stim.PauliString("Z45*Z72*Z77*Z167*Z218"),  # with 218
    "k179_z": stim.PauliString("Z28*Z100*Z154*Z157*Z219"),  # with 219
    "k206_z": stim.PauliString("Z56*Z69*Z114*Z118*Z220"),  # with 220
    "k105_z": stim.PauliString("Z71*Z102*Z147*Z152*Z221"),  # with 221
    "k188_z": stim.PauliString("Z12*Z21*Z48*Z96*Z222"),  # with 222
    "k162_z": stim.PauliString("Z7*Z39*Z95*Z174*Z223"),  # with 223
    "k193_z": stim.PauliString("Z39*Z95*Z132*Z162*Z224"),  # with 224
    "k213_z": stim.PauliString("Z88*Z122*Z132*Z162*Z225"),  # with 225
    "k154_z": stim.PauliString("Z5*Z19*Z132*Z162*Z226"),  # with 226
    "k140_z": stim.PauliString("Z30*Z91*Z102*Z126*Z140*Z147*Z227"),  # with 227

}

stabilizers_s_z_enlarged = {
    "s15_z": stim.PauliString("Z252*Z253*Z258*Z259*Z175"), # with 175
    "s14_z": stim.PauliString("Z242*Z247*Z252*Z253*Z181"), # with 181
    "s4_z": stim.PauliString("Z238*Z239*Z242*Z243*Z247*Z248*Z184"), # with 184
    "s12_z": stim.PauliString("Z232*Z235*Z238*Z239*Z188"), # with 188
    "s1_z": stim.PauliString("Z230*Z231*Z232*Z233*Z235*Z236*Z190"), # with 190
    "s10_z": stim.PauliString("Z228*Z229*Z230*Z231*Z192"), # with 192
    "s2_z": stim.PauliString("Z233*Z234*Z236*Z237*Z240*Z241*Z189"), # with 189
    "s3_z": stim.PauliString("Z235*Z236*Z239*Z240*Z243*Z244*Z186"), # with 186
    "s5_z": stim.PauliString("Z240*Z241*Z244*Z245*Z249*Z250*Z185"), # with 185
    "s6_z": stim.PauliString("Z243*Z244*Z248*Z249*Z254*Z255*Z182"), # with 182
    "s7_z": stim.PauliString("Z245*Z246*Z250*Z251*Z256*Z257*Z183"), # with 183
    "s8_z": stim.PauliString("Z247*Z248*Z253*Z254*Z259*Z260*Z178"), # with 178
    "s9_z": stim.PauliString("Z249*Z250*Z255*Z256*Z261*Z262*Z179"), # with 179
    "s11_z": stim.PauliString("Z229*Z231*Z233*Z234*Z191"), # with 191
    "s13_z": stim.PauliString("Z237*Z241*Z245*Z246*Z187"), # with 187
    "s16_z": stim.PauliString("Z251*Z257*Z263*Z264*Z180"), # with 180
    "s17_z": stim.PauliString("Z254*Z255*Z260*Z261*Z176"), # with 176
    "s18_z": stim.PauliString("Z256*Z257*Z262*Z263*Z177"), # with 177
}

# Enlargable stabilizers String to String

stabilizers_added_Z = {
    "m1_z": stim.PauliString("Z43*Z258*Z175"),  # 44(3D) 30(2D) 175
    "m2_z": stim.PauliString("Z100*Z252*Z175*Z176"),  # 101(3D) 24(2D) 175 176
    "m3_z": stim.PauliString("Z98*Z242*Z176*Z177"),  # 99(3D) 14(2D) 176 177
    "m4_z": stim.PauliString("Z118*Z238*Z177*Z178"),  # 119(3D) 10(2D) 177 178
    "m5_z": stim.PauliString("Z26*Z232*Z178*Z179"),  # 27(3D) 4(2D) 178 179
    "m6_z": stim.PauliString("Z92*Z230*Z179*Z180"),  # 93(3D) 2(2D) 179 180
    "m7_z": stim.PauliString("Z109*Z228*Z180"),  # 110(3D) 0(2D) 180
}


# Ensure the logical ZZ are supported by all the physical qubits in a face
stabilizer_global = {
    "k6_z": stim.PauliString("Z57*Z62*Z64*Z173"),  # with 180
    "k5_z": stim.PauliString("Z5*Z54*Z77*Z167*Z168*Z171"),  # with 179
    "k4_z": stim.PauliString("Z59*Z68*Z71*Z133*Z138*Z157"),  # with 178
    "k49_z": stim.PauliString("Z88*Z95*Z132*Z174"),  # with 187
    "k48_z": stim.PauliString("Z13*Z69*Z81*Z102*Z112*Z126"),  # with 186
    "k65_z": stim.PauliString("Z8*Z12*Z14*Z96"),  # with 191
    
    "s8_z": stim.PauliString("Z247*Z248*Z253*Z254*Z259*Z260"), # with 178
    "s9_z": stim.PauliString("Z249*Z250*Z255*Z256*Z261*Z262"), # with 179
    "s16_z": stim.PauliString("Z251*Z257*Z263*Z264"), # with 180
    "s3_z": stim.PauliString("Z235*Z236*Z239*Z240*Z243*Z244"), # with 186
    "s13_z": stim.PauliString("Z237*Z241*Z245*Z246"), # with 187
    "s11_z": stim.PauliString("Z229*Z231*Z233*Z234"), # with 191
}

# --- matching logical operators --- 
    # 3D (X):     5,   8,  12,  13,  14,  26,  43,  54,  57,  59,  62,  64,  68,  69,  71,  77,  81,  88,  92,  95,  96,  98, 100, 102, 109, 112, 118, 126, 132, 133, 138, 157, 167, 168, 171, 173, 174
    
    # 2D (Z/X): 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264
    # 2D (Z/X):   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36


stabilizers_k_x_enlargable = {
    "k1_x": stim.PauliString("X28*X35*X40*X43*X68*X100*X154*X157"),  # with 175
    "k19_x": stim.PauliString("X28*X58*X61*X98*X100*X110*X133*X136*X139*X146*X154*X157"),  # with 176
    "k25_x": stim.PauliString("X56*X58*X69*X71*X98*X102*X114*X118*X133*X146*X147*X152"),  # with 177
    "k34_x": stim.PauliString("X26*X27*X56*X60*X69*X93*X112*X114*X118*X141*X144*X145"),  # with 178
    "k37_x": stim.PauliString("X1*X8*X12*X13*X26*X27*X29*X48*X60*X78*X92*X112"),  # with 179
    "k40_x": stim.PauliString("X1*X8*X14*X29*X92*X105*X109*X119"),  # with 180
}

stabilizers_k_x_enlarged = {
    "k1_x": stim.PauliString("X28*X35*X40*X43*X68*X100*X154*X157*X175"),  # with 175
    "k19_x": stim.PauliString("X28*X58*X61*X98*X100*X110*X133*X136*X139*X146*X154*X157*X176"),  # with 176
    "k25_x": stim.PauliString("X56*X58*X69*X71*X98*X102*X114*X118*X133*X146*X147*X152*X177"),  # with 177
    "k34_x": stim.PauliString("X26*X27*X56*X60*X69*X93*X112*X114*X118*X141*X144*X145*X178"),  # with 178
    "k37_x": stim.PauliString("X1*X8*X12*X13*X26*X27*X29*X48*X60*X78*X92*X112*X179"),  # with 179
    "k40_x": stim.PauliString("X1*X8*X14*X29*X92*X105*X109*X119*X180"),  # with 180
}

stabilizers_s_x_enlargable = {
    "s15_x": stim.PauliString("X252*X253*X258*X259"),  # with 175
    "s14_x": stim.PauliString("X242*X247*X252*X253"),  # with 176
    "s4_x": stim.PauliString("X238*X239*X242*X243*X247*X248"),  # with 177
    "s12_x": stim.PauliString("X232*X235*X238*X239"),  # with 178
    "s1_x": stim.PauliString("X230*X231*X232*X233*X235*X236"),  # with 179
    "s10_x": stim.PauliString("X228*X229*X230*X231"),  # with 180
}

stabilizers_s_x_enlarged = {
    "s15_x": stim.PauliString("X252*X253*X258*X259*X175"),  # with 175
    "s14_x": stim.PauliString("X242*X247*X252*X253*X176"),  # with 176
    "s4_x": stim.PauliString("X238*X239*X242*X243*X247*X248*X177"),  # with 177
    "s12_x": stim.PauliString("X232*X235*X238*X239*X178"),  # with 178
    "s1_x": stim.PauliString("X230*X231*X232*X233*X235*X236*X179"),  # with 179
    "s10_x": stim.PauliString("X228*X229*X230*X231*X180"),  # with 180
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
    
    c.append("R", list(range(175, 228)))
   
    return c

def lattice_surgery_Split(error_rate):
    
    c = stim.Circuit()

    c.append("M", [175, 181, 184, 188, 190, 192, 189, 186, 185, 182, 183, 178, 179, 191, 187, 180, 176, 177, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227], tag="Measurement_ancilla", arg=error_rate)
    
    return c

def lattice_surgery_Merge_string():
    
    c = stim.Circuit()  
    
    c.append("H", [175, 176, 177, 178, 179, 180])
   
    return c

def lattice_surgery_Split_string(error_rate):
    
    c = stim.Circuit()

    c.append("MX", [175, 176, 177, 178, 179, 180], tag="Measurement_ancilla_string", arg=error_rate)
    
    return c

def lattice_surgery_Reset_string():
    
    c = stim.Circuit()

    c.append("R", [175, 176, 177, 178, 179, 180])
    
    return c    

def measure_logical_qubits_3D() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("X5*X8*X12*X13*X14*X26*X43*X54*X57*X59*X62*X64*X68*X69*X71*X77*X81*X88*X92*X95*X96*X98*X100*X102*X109*X112*X118*X126*X132*X133*X138*X157*X167*X168*X171*X173*X174"), tag="logical_qubits_3D")
    c.append("OBSERVABLE_INCLUDE", [
        stim.target_rec(-1), ], 0)
    
    return c

def measure_logical_qubits_2D() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("Z228*Z230*Z232*Z238*Z242*Z252*Z258"), tag="logical_qubits_2D")
    c.append("OBSERVABLE_INCLUDE", [
        stim.target_rec(-1), ], 1)

    return c


def measurement_XX() -> stim.Circuit:
    c = stim.Circuit()
    c.append("MPP", stim.PauliString("X5*X8*X12*X13*X14*X26*X43*X54*X57*X59*X62*X64*X68*X69*X71*X77*X81*X88*X92*X95*X96*X98*X100*X102*X109*X112*X118*X126*X132*X133*X138*X157*X167*X168*X171*X173*X174"), tag="logical_qubits_3D_X")
    c.append("MPP", stim.PauliString("X228*X229*X230*X231*X232*X233*X234*X235*X236*X237*X238*X239*X240*X241*X242*X243*X244*X245*X246*X247*X248*X249*X250*X251*X252*X253*X254*X255*X256*X257*X258*X259*X260*X261*X262*X263*X264"), tag="logical_qubits_2D_X") 
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

    control_qubits = [228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264]  

    target_qubits = [ 109,  14,  92,   8,  26,  12,  96, 112,  13, 174, 118,  69,  81,  95,  98, 102, 126, 132,  88, 133,  71, 171,   5, 173, 100, 157,  59, 167,  54,  62,  43,  68, 138,  77, 168,  57, 64]

    c.append("CZ", [q for pair in zip(control_qubits, target_qubits) for q in pair])

    return c

DISTANCE = 7

__all__ = ['stabilizers_k_z', 'stabilizers_k_x', 'V_even', 'V_odd', 'S_gate_track', 'stabilizers_s_x', 'stabilizers_s_z', 'stabilizers_added_X', 'stabilizers_k_z_enlargable', 'stabilizers_k_z_enlargable_horizontal', 'stabilizers_k_z_enlargable_vertical', 'stabilizers_k_z_enlarged', 'stabilizers_s_z_enlarged', 'stabilizers_added_Z', 'stabilizer_global', 'stabilizers_k_x_enlargable', 'stabilizers_k_x_enlarged', 'stabilizers_s_x_enlargable', 'stabilizers_s_x_enlarged', 'stabilizers_general', 'stabilizers_k_z_unchange', 'stabilizers_merged', 'stabilizers_merged_without_add_X', 'stabilizers_k_x_unchange', 'stabilizers_s_x_unchange', 'stabilizers_merged_string', 'stabilizers_merged_string_without_add_Z', 'lattice_surgery_Merge', 'lattice_surgery_Split', 'lattice_surgery_Merge_string', 'lattice_surgery_Split_string', 'lattice_surgery_Reset_string', 'measure_logical_qubits_3D', 'measure_logical_qubits_2D', 'measurement_XX', 'S_Z_Gate', 'S_Z_DAG_Gate', 'logical_CZ', 'DISTANCE']
