#!/usr/bin/env python
# encoding: utf-8

name = "HBI correction"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "Root",
    group = 
"""
1 * R u[1,2,3,4]
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0552031,-1.03652,-1.71357,-2.11027,-2.5943,-3.06424,-4.18372],'cal/mol/K','+|-',[3.63105,4.31995,4.35512,4.09739,3.72304,3.67772,4.22981]),
        H298 = (94.6851,'kcal/mol','+|-',26.6206),
        S298 = (0.49871,'cal/mol/K','+|-',14.4978),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 1,
    label = "RJ1",
    group = 
"""
1 * R u1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0552031,-1.03652,-1.71357,-2.11027,-2.5943,-3.06424,-4.18372],'cal/mol/K','+|-',[3.63105,4.31995,4.35512,4.09739,3.72304,3.67772,4.22981]),
        H298 = (94.6851,'kcal/mol','+|-',26.6206),
        S298 = (0.49871,'cal/mol/K','+|-',14.4978),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 2,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.332087,-0.72729,-1.13839,-1.42439,-1.85205,-2.25852,-3.42498],'cal/mol/K','+|-',[3.31576,3.62081,3.67455,3.54363,3.15675,2.91277,2.87745]),
        H298 = (89.3485,'kcal/mol','+|-',33.3528),
        S298 = (0.612794,'cal/mol/K','+|-',15.2209),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux {1,S} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.481818,-0.865407,-1.27325,-1.55206,-1.97705,-2.3953,-3.59539],'cal/mol/K','+|-',[3.17563,3.5522,3.62054,3.49833,3.08286,2.7701,2.5796]),
        H298 = (89.3623,'kcal/mol','+|-',34.0927),
        S298 = (-0.848756,'cal/mol/K','+|-',9.15361),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing",
    group = 
"""
1 * R u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.950466,-1.16498,-1.49677,-1.85161,-2.38246,-2.85533,-4.10737],'cal/mol/K','+|-',[1.35815,1.94422,2.37065,2.28916,1.85109,1.43303,1.93684]),
        H298 = (89.1323,'kcal/mol','+|-',44.472),
        S298 = (0.162411,'cal/mol/K','+|-',8.87447),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.502319,-0.690808,-1.03223,-1.42759,-2.13752,-2.78172,-3.97741],'cal/mol/K','+|-',[0.318263,1.05557,1.64215,1.66323,1.57975,1.48529,1.11255]),
        H298 = (99.5036,'kcal/mol','+|-',39.7841),
        S298 = (-0.725846,'cal/mol/K','+|-',1.86237),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_4R!H->C_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.370042,-0.863877,-1.43489,-1.97687,-2.79961,-3.43811,-4.4586],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (115.542,'kcal/mol','+|-',1.69706),
        S298 = (-0.183653,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[C]1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 7,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_4R!H->C_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.596803,-0.567187,-0.744607,-1.03525,-1.66461,-2.31288,-3.63369],'cal/mol/K','+|-',[0.236483,1.60169,2.26562,1.90818,1.1361,0.787991,0.685943]),
        H298 = (85.7381,'kcal/mol','+|-',10.7654),
        S298 = (-1.11313,'cal/mol/K','+|-',2.36156),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_4R!H->C_N-1R-inRing_Ext-4C-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   u0 r1 {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.716244,-1.37616,-1.88892,-1.99903,-2.23842,-2.71087,-3.98015],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (79.2047,'kcal/mol','+|-',4.17612),
        S298 = (0.0796382,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CC=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 9,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * R u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71872,-1.97784,-2.29314,-2.57849,-2.80235,-2.98151,-4.33018],'cal/mol/K','+|-',[0.148997,2.486,3.44397,3.37277,2.87417,2.11623,3.89763]),
        H298 = (69.8598,'kcal/mol','+|-',24.1204),
        S298 = (1.68514,'cal/mol/K','+|-',18.927),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 10,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_N-4R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   O ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.64346,-3.23346,-4.03261,-4.282,-4.25402,-4.05037,-6.29877],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.4982,'kcal/mol','+|-',4.17612),
        S298 = (11.2447,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
COC1=C[CH]CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 11,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_N-4R!H->C_N-1R->C",
    group = 
"""
1 * O u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   O ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.74882,-1.47559,-1.59735,-1.89709,-2.22168,-2.55396,-3.54274],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (67.4425,'kcal/mol','+|-',1.69706),
        S298 = (-2.1387,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 12,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux r0 {1,S} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.203129,-0.427574,-0.946561,-1.11426,-1.38452,-1.72295,-2.8471],'cal/mol/K','+|-',[4.67891,5.35916,5.30494,5.04639,4.3512,3.85308,2.90735]),
        H298 = (89.8235,'kcal/mol','+|-',7.55399),
        S298 = (-2.32661,'cal/mol/K','+|-',10.1429),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 13,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing_Ext-2R!H-R",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux {2,D}
4   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.149839,-0.943005,-1.55111,-1.80039,-2.09599,-2.39328,-3.35144],'cal/mol/K','+|-',[4.85399,5.20402,4.75377,3.89917,2.33539,1.52093,1.17134]),
        H298 = (89.6149,'kcal/mol','+|-',8.36557),
        S298 = (-0.712506,'cal/mol/K','+|-',5.92213),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 14,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing_Ext-2R!H-R_1R->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux {2,D}
4   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.314877,-0.117714,-0.716507,-1.10709,-1.71943,-2.22971,-3.30504],'cal/mol/K','+|-',[5.07127,3.6729,2.54894,1.9809,1.59535,1.52279,1.3728]),
        H298 = (88.677,'kcal/mol','+|-',4.6538),
        S298 = (-1.85164,'cal/mol/K','+|-',1.42883),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 15,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing_Ext-2R!H-R_1R->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux r0 {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.84419,1.1356,0.14888,-0.485643,-1.3994,-2.05443,-3.05427],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (87.8293,'kcal/mol','+|-',1.69706),
        S298 = (-2.03169,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=COC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 16,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing_Ext-2R!H-R_1R->C_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux {2,D}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.00912,-1.96521,-1.55445,-1.41295,-1.37093,-1.62023,-2.94668],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.0245,'kcal/mol','+|-',4.17612),
        S298 = (-0.858899,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[CH]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing_Ext-2R!H-R_N-1R->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,D} {4,S}
3   R!H u0 {2,D}
4   C   u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.24106,-4.65681,-5.3068,-4.92025,-3.79049,-3.12934,-3.56028],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.17,'kcal/mol','+|-',4.17612),
        S298 = (4.41361,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 18,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-Sp-2R!H-1R",
    group = 
"""
1 * R   u1 {2,D}
2   C   u0 {1,D} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.06361,1.48258,1.01935,0.618409,0.147845,-0.0701442,-0.698511],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.931,'kcal/mol','+|-',4.17612),
        S298 = (23.9976,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 19,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.180148,-1.29936,-2.20246,-2.69327,-3.22522,-3.74909,-4.82866],'cal/mol/K','+|-',[3.97321,4.94614,4.80693,4.32741,3.83068,3.81796,4.86525]),
        H298 = (99.5538,'kcal/mol','+|-',15.3214),
        S298 = (0.401738,'cal/mol/K','+|-',14.604),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 20,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.385622,-0.940879,-1.73991,-2.2341,-2.87815,-3.41381,-4.75274],'cal/mol/K','+|-',[4.2135,5.45645,5.13055,4.41937,3.80931,3.68937,5.32981]),
        H298 = (100.841,'kcal/mol','+|-',13.4186),
        S298 = (-0.273829,'cal/mol/K','+|-',8.24719),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 21,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.903907,-0.350779,-1.19754,-1.90542,-2.93348,-3.6892,-5.1304],'cal/mol/K','+|-',[3.10492,4.80855,4.48047,4.02405,3.02465,2.19623,2.91935]),
        H298 = (100.397,'kcal/mol','+|-',13.5703),
        S298 = (0.2752,'cal/mol/K','+|-',6.98135),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 22,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Int-3R!H-1C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H u0 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.17388,-2.01085,-2.71466,-3.19285,-3.91632,-4.40135,-5.00618],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (108.638,'kcal/mol','+|-',1.69706),
        S298 = (4.35064,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 23,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,S}
3   R!H ux {2,S} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.65996,0.0211763,-0.93788,-1.73932,-2.84619,-3.65799,-5.4005],'cal/mol/K','+|-',[2.62995,5.9772,5.56646,5.01479,3.73058,2.67754,3.73274]),
        H298 = (100.877,'kcal/mol','+|-',4.26431),
        S298 = (0.566404,'cal/mol/K','+|-',4.2421),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 24,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_Ext-2R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   R!H u0 {2,S} {4,S}
4   O   u0 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.854952,0.33181,-0.600332,-1.38916,-2.44358,-3.27674,-5.64549],'cal/mol/K','+|-',[2.2983,4.06302,4.34267,4.17166,3.23017,2.36441,5.43443]),
        H298 = (99.6745,'kcal/mol','+|-',4.63539),
        S298 = (1.08952,'cal/mol/K','+|-',3.987),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 25,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_Ext-2R!H-R_Ext-1C-R",
    group = 
"""
1 * C u1 {2,S} {6,S}
2   C u0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   O u0 {2,S} {4,S}
4   O u0 {3,S}
5   C ux {2,[S,D,T,B,Q]}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.1226,-1.41575,-2.44757,-3.13458,-3.69964,-4.19166,-7.45252],'cal/mol/K','+|-',[0.570117,0.211167,1.07391,1.5931,2.25951,1.68934,5.63327]),
        H298 = (97.3669,'kcal/mol','+|-',3.64379),
        S298 = (2.5628,'cal/mol/K','+|-',3.33675),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 26,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_Ext-2R!H-R_Ext-1C-R_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   C u0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   O u0 {2,S} {4,S}
4   O u0 {3,S}
5   C ux r0 {2,[S,D,T,B,Q]}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0789673,-1.49041,-2.82725,-3.69782,-4.49849,-4.78893,-9.44418],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.6552,'kcal/mol','+|-',4.17612),
        S298 = (3.74252,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)C1(C)[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 27,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_Ext-2R!H-R_Ext-1C-R_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,S} {6,S}
2   C u0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   O u0 {2,S} {4,S}
4   O u0 {3,S}
5   C ux r0 {2,[S,D,T,B,Q]}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.324166,-1.34109,-2.06788,-2.57133,-2.90078,-3.59439,-5.46086],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.0787,'kcal/mol','+|-',4.17612),
        S298 = (1.38308,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 28,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,S}
3   R!H ux {2,S} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.15489,-5.86525,-6.24291,-6.43654,-6.34832,-6.15599,-5.84693],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.565,'kcal/mol','+|-',4.17612),
        S298 = (3.04049,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CO[CH]CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 29,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,S}
3   R!H ux {2,S} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.51099,1.81661,0.576545,-0.490708,-2.17003,-3.34506,-4.78095],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.528,'kcal/mol','+|-',1.69706),
        S298 = (-1.36484,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 30,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_N-Sp-3R!H-2R!H",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,T}
3   R!H ux {2,T} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.562345,0.119029,-0.511306,-1.14951,-2.22996,-3.07689,-4.39029],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (90.9569,'kcal/mol','+|-',1.69706),
        S298 = (-4.7321,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C#CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 31,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_N-1R->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,S}
3   R!H u0 {2,S} {4,[S,D,T,B,Q]}
4   O   u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.98323,-4.77653,-5.26532,-4.37054,-2.51853,-1.6238,-2.29797],'cal/mol/K','+|-',[4.63383,0.674751,3.12013,6.01136,9.39262,9.74972,14.8738]),
        H298 = (106.893,'kcal/mol','+|-',3.47714),
        S298 = (-3.84252,'cal/mol/K','+|-',15.4278),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 32,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_N-1R->C_2R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,S}
3   R!H u0 {2,S} {4,[S,D,T,B,Q]}
4   O   u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34493,-4.53796,-6.36845,-6.49588,-5.83932,-5.07085,-7.55663],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (108.122,'kcal/mol','+|-',4.17612),
        S298 = (1.61203,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C1CC(C)([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 33,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_N-1R->C_N-2R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,S}
3   R!H u0 {2,S} {4,[S,D,T,B,Q]}
4   O   u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.62154,-5.01509,-4.16219,-2.24521,0.802262,1.82324,2.9607],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (105.664,'kcal/mol','+|-',4.17612),
        S298 = (-9.29707,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(O)C(=O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 34,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.436275,-2.37482,-3.59013,-4.07079,-4.26641,-4.75493,-5.0564],'cal/mol/K','+|-',[3.43411,2.67319,2.65293,3.05191,3.54441,3.94016,3.91524]),
        H298 = (92.0298,'kcal/mol','+|-',18.0676),
        S298 = (2.42844,'cal/mol/K','+|-',26.9191),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 35,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_1R->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C ux r0 {2,S} {4,[S,D,T,B,Q]}
4   C ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.1944,-1.30311,-3.03464,-3.42374,-2.98229,-2.81412,-2.4908],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (107.58,'kcal/mol','+|-',4.17612),
        S298 = (26.1311,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 36,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.843943,-2.64275,-3.729,-4.23255,-4.58744,-5.24014,-5.6978],'cal/mol/K','+|-',[3.36041,2.75929,2.97822,3.4236,3.74195,3.79761,3.07705]),
        H298 = (88.1424,'kcal/mol','+|-',5.68003),
        S298 = (-3.49722,'cal/mol/K','+|-',5.46139),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 37,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_N-1R->C_Ext-4BrCClFINPSSi-R_5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34097,-2.82741,-3.71884,-4.07859,-4.34418,-4.88611,-5.35493],'cal/mol/K','+|-',[3.31809,3.25609,3.64722,4.12465,4.42528,4.31564,3.37356]),
        H298 = (89.0217,'kcal/mol','+|-',5.46264),
        S298 = (-3.52903,'cal/mol/K','+|-',6.687),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 38,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_N-1R->C_Ext-4BrCClFINPSSi-R_5R!H->C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   u0 {2,[S,T,Q,B]} {4,S}
4   C   u0 {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0588543,-0.949183,-1.71706,-1.88755,-2.07451,-2.7407,-3.40755],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.8761,'kcal/mol','+|-',4.17612),
        S298 = (-7.27735,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O[O])C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 39,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_N-1R->C_Ext-4BrCClFINPSSi-R_5R!H->C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.749311,-3.69771,-5.2856,-5.98201,-6.495,-7.05613,-6.36016],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.3962,'kcal/mol','+|-',4.17612),
        S298 = (-2.45586,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 40,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_N-1R->C_Ext-4BrCClFINPSSi-R_N-5R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   O                      u0 r0 {1,S} {3,S}
3   C                      ux r0 {2,S} {4,[S,D,T,B,Q]}
4   C                      ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.647131,-2.08877,-3.75949,-4.69443,-5.31722,-6.30221,-6.72642],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.5047,'kcal/mol','+|-',4.17612),
        S298 = (-3.40178,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_4R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_4R!H->C_1R-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_4R!H->C_N-1R-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_4R!H->C_N-1R-inRing_Ext-4C-R_Ext-2R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_N-4R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_N-4R!H->C_1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_2R!H-inRing_Ext-3R!H-R_N-4R!H->C_N-1R->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing_Ext-2R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing_Ext-2R!H-R_1R->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing_Ext-2R!H-R_1R->C_Ext-4R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing_Ext-2R!H-R_1R->C_Ext-1C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Sp-2R!H-1R_N-2R!H-inRing_Ext-2R!H-R_N-1R->C
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-Sp-2R!H-1R
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Int-3R!H-1C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_Ext-2R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_Ext-2R!H-R_Ext-1C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_Ext-2R!H-R_Ext-1C-R_1C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_Ext-2R!H-R_Ext-1C-R_N-1C-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_2R!H-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_Sp-3R!H-2R!H_N-2R!H-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_N-Sp-3R!H-2R!H
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_N-1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_N-1R->C_2R!H->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_N-1R->C_N-2R!H->C
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_1R->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_N-1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_N-1R->C_Ext-4BrCClFINPSSi-R_5R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_N-1R->C_Ext-4BrCClFINPSSi-R_5R!H->C_Ext-4BrCClFINPSSi-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_N-1R->C_Ext-4BrCClFINPSSi-R_5R!H->C_Ext-3R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_N-1R->C_Ext-4BrCClFINPSSi-R_N-5R!H->C
"""
)

