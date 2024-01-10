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
        Cpdata = ([-0.0552031,-1.03652,-1.71357,-2.11027,-2.5943,-3.06424,-4.18372],'cal/mol/K','+|-',[5.7606,6.21788,6.24236,6.06536,5.81902,5.79013,6.15559]),
        H298 = (94.6851,'kcal/mol','+|-',27.9001),
        S298 = (0.49871,'cal/mol/K','+|-',15.1719),
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
        Cpdata = ([-0.0552031,-1.03652,-1.71357,-2.11027,-2.5943,-3.06424,-4.18372],'cal/mol/K','+|-',[5.7606,6.21788,6.24236,6.06536,5.81902,5.79013,6.15559]),
        H298 = (94.6851,'kcal/mol','+|-',27.9001),
        S298 = (0.49871,'cal/mol/K','+|-',15.1719),
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
        Cpdata = ([-0.332087,-0.72729,-1.13839,-1.42439,-1.85205,-2.25852,-3.42498],'cal/mol/K','+|-',[5.56725,5.75416,5.78812,5.7059,5.47404,5.33706,5.31787]),
        H298 = (89.3485,'kcal/mol','+|-',34.3827),
        S298 = (0.612794,'cal/mol/K','+|-',15.8643),
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
        Cpdata = ([-0.481818,-0.865407,-1.27325,-1.55206,-1.97705,-2.3953,-3.59539],'cal/mol/K','+|-',[5.48495,5.71122,5.75398,5.67788,5.43176,5.26056,5.16278]),
        H298 = (89.3623,'kcal/mol','+|-',35.1009),
        S298 = (-0.848756,'cal/mol/K','+|-',10.1877),
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
        Cpdata = ([-0.950466,-1.16498,-1.49677,-1.85161,-2.38246,-2.85533,-4.10737],'cal/mol/K','+|-',[4.67382,4.87647,5.06162,5.02397,4.8401,4.69612,4.87354]),
        H298 = (89.1323,'kcal/mol','+|-',45.2495),
        S298 = (0.162411,'cal/mol/K','+|-',9.93762),
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
        Cpdata = ([-0.502319,-0.690808,-1.03223,-1.42759,-2.13752,-2.78172,-3.97741],'cal/mol/K','+|-',[4.48345,4.59502,4.7641,4.77141,4.74295,4.71233,4.60844]),
        H298 = (99.5036,'kcal/mol','+|-',40.6514),
        S298 = (-0.725846,'cal/mol/K','+|-',4.84442),
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
        Cpdata = ([-0.596803,-0.567187,-0.744607,-1.03525,-1.66461,-2.31288,-3.63369],'cal/mol/K','+|-',[4.47838,4.75031,5.01329,4.86222,4.61419,4.54103,4.52444]),
        H298 = (85.7381,'kcal/mol','+|-',13.6255),
        S298 = (-1.11313,'cal/mol/K','+|-',5.05737),
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
        Cpdata = ([-1.71872,-1.97784,-2.29314,-2.57849,-2.80235,-2.98151,-4.33018],'cal/mol/K','+|-',[4.47462,5.11666,5.64455,5.60139,5.31609,4.94757,5.93224]),
        H298 = (69.8598,'kcal/mol','+|-',25.5255),
        S298 = (1.68514,'cal/mol/K','+|-',19.4482),
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
        Cpdata = ([0.203129,-0.427574,-0.946561,-1.11426,-1.38452,-1.72295,-2.8471],'cal/mol/K','+|-',[6.47242,6.98002,6.93847,6.74286,6.23963,5.90307,5.33411]),
        H298 = (89.8235,'kcal/mol','+|-',11.2616),
        S298 = (-2.32661,'cal/mol/K','+|-',11.085),
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
        Cpdata = ([-0.149839,-0.943005,-1.55111,-1.80039,-2.09599,-2.39328,-3.35144],'cal/mol/K','+|-',[6.60009,6.86162,6.52674,5.93326,5.0452,4.72369,4.62299]),
        H298 = (89.6149,'kcal/mol','+|-',11.8213),
        S298 = (-0.712506,'cal/mol/K','+|-',7.42102),
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
        Cpdata = ([0.314877,-0.117714,-0.716507,-1.10709,-1.71943,-2.22971,-3.30504],'cal/mol/K','+|-',[6.7615,5.78707,5.14753,4.89121,4.74817,4.72429,4.67809]),
        H298 = (88.677,'kcal/mol','+|-',9.56127),
        S298 = (-1.85164,'cal/mol/K','+|-',4.69484),
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
        Cpdata = ([0.180148,-1.29936,-2.20246,-2.69327,-3.22522,-3.74909,-4.82866],'cal/mol/K','+|-',[5.98217,6.66816,6.56556,6.22306,5.88847,5.88021,6.60838]),
        H298 = (99.5538,'kcal/mol','+|-',17.4501),
        S298 = (0.401738,'cal/mol/K','+|-',15.2734),
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
        Cpdata = ([0.385622,-0.940879,-1.73991,-2.2341,-2.87815,-3.41381,-4.75274],'cal/mol/K','+|-',[6.14439,7.05499,6.80607,6.28736,5.8746,5.79754,6.95751]),
        H298 = (100.841,'kcal/mol','+|-',15.8056),
        S298 = (-0.273829,'cal/mol/K','+|-',9.38169),
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
        Cpdata = ([0.903907,-0.350779,-1.19754,-1.90542,-2.93348,-3.6892,-5.1304],'cal/mol/K','+|-',[5.44431,6.56675,6.33045,6.01606,5.39894,4.98231,5.34065]),
        H298 = (100.397,'kcal/mol','+|-',15.9346),
        S298 = (0.2752,'cal/mol/K','+|-',8.29091),
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
        Cpdata = ([1.65996,0.0211763,-0.93788,-1.73932,-2.84619,-3.65799,-5.4005],'cal/mol/K','+|-',[5.18813,7.46504,7.14041,6.71923,5.82385,5.21241,5.82523]),
        H298 = (100.877,'kcal/mol','+|-',9.37786),
        S298 = (0.566404,'cal/mol/K','+|-',6.16404),
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
        Cpdata = ([0.854952,0.33181,-0.600332,-1.38916,-2.44358,-3.27674,-5.64549],'cal/mol/K','+|-',[5.02814,6.0422,6.23368,6.11578,5.5167,5.0587,7.03797]),
        H298 = (99.6745,'kcal/mol','+|-',9.55232),
        S298 = (1.08952,'cal/mol/K','+|-',5.99134),
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
        Cpdata = ([-0.1226,-1.41575,-2.44757,-3.13458,-3.69964,-4.19166,-7.45252],'cal/mol/K','+|-',[4.50833,4.47712,4.59927,4.74742,5.01053,4.78057,7.19261]),
        H298 = (97.3669,'kcal/mol','+|-',9.11248),
        S298 = (2.5628,'cal/mol/K','+|-',5.57978),
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
        Cpdata = ([-2.98323,-4.77653,-5.26532,-4.37054,-2.51853,-1.6238,-2.29797],'cal/mol/K','+|-',[6.43991,4.52275,5.453,7.49243,10.4029,10.7265,15.5315]),
        H298 = (106.893,'kcal/mol','+|-',9.04713),
        S298 = (-3.84252,'cal/mol/K','+|-',16.0629),
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
        Cpdata = ([-0.436275,-2.37482,-3.59013,-4.07079,-4.26641,-4.75493,-5.0564],'cal/mol/K','+|-',[5.63854,5.21018,5.19981,5.41425,5.70639,5.96027,5.94383]),
        H298 = (92.0298,'kcal/mol','+|-',19.9047),
        S298 = (2.42844,'cal/mol/K','+|-',27.2881),
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
        Cpdata = ([-0.843943,-2.64275,-3.729,-4.23255,-4.58744,-5.24014,-5.6978],'cal/mol/K','+|-',[5.59396,5.25487,5.37306,5.63215,5.83114,5.86701,5.42847]),
        H298 = (88.1424,'kcal/mol','+|-',10.1006),
        S298 = (-3.49722,'cal/mol/K','+|-',7.05881),
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
        Cpdata = ([-1.34097,-2.82741,-3.71884,-4.07859,-4.34418,-4.88611,-5.35493],'cal/mol/K','+|-',[5.56864,5.53192,5.77081,6.08381,6.29151,6.21488,5.60187]),
        H298 = (89.0217,'kcal/mol','+|-',9.98),
        S298 = (-3.52903,'cal/mol/K','+|-',8.04462),
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

