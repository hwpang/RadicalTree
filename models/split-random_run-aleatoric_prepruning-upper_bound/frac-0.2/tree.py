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
        Cpdata = ([-0.580207,-1.59117,-2.32619,-2.75459,-3.20106,-3.59334,-4.40346],'cal/mol/K','+|-',[3.99439,4.69841,4.92365,4.75455,4.14844,3.78988,3.85407]),
        H298 = (94.0158,'kcal/mol','+|-',26.9104),
        S298 = (0.22968,'cal/mol/K','+|-',9.30978),
    ),
    shortDesc = """Radical correction fitted to 506 radicals""",
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
        Cpdata = ([-0.580207,-1.59117,-2.32619,-2.75459,-3.20106,-3.59334,-4.40346],'cal/mol/K','+|-',[3.99439,4.69841,4.92365,4.75455,4.14844,3.78988,3.85407]),
        H298 = (94.0158,'kcal/mol','+|-',26.9104),
        S298 = (0.22968,'cal/mol/K','+|-',9.30978),
    ),
    shortDesc = """Radical correction fitted to 506 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 2,
    label = "RJ1_1R-inRing",
    group = 
"""
1 * C u1 r1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.327066,-1.02509,-2.004,-2.56755,-3.20253,-3.72787,-4.89275],'cal/mol/K','+|-',[3.11654,4.06807,4.48542,4.48951,4.12641,3.96675,4.7158]),
        H298 = (91.2034,'kcal/mol','+|-',40.8908),
        S298 = (0.577654,'cal/mol/K','+|-',7.24645),
    ),
    shortDesc = """Radical correction fitted to 87 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.429202,-0.732621,-1.73737,-2.26327,-2.80829,-3.28959,-4.33763],'cal/mol/K','+|-',[3,3.13632,3.65474,3.83229,3.95972,4.24351,5.01685]),
        H298 = (78.6341,'kcal/mol','+|-',50.141),
        S298 = (-0.616828,'cal/mol/K','+|-',6.76963),
    ),
    shortDesc = """Radical correction fitted to 47 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.362233,-0.951734,-2.02933,-2.58281,-3.14761,-3.62151,-4.5626],'cal/mol/K','+|-',[3.0819,3,3,3,3,3,3]),
        H298 = (79.608,'kcal/mol','+|-',13.432),
        S298 = (-0.752417,'cal/mol/K','+|-',7.50066),
    ),
    shortDesc = """Radical correction fitted to 30 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0326069,-1.20712,-2.04994,-2.44898,-2.75061,-2.99229,-3.94352],'cal/mol/K','+|-',[3.56593,3.86214,3.97065,3.83036,3.27155,3,3]),
        H298 = (73.7803,'kcal/mol','+|-',24.1075),
        S298 = (-0.101577,'cal/mol/K','+|-',6.62273),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_5R!H->O",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux r1 {2,D} {4,S}
4   C u0 r1 {3,S} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.15109,1.27796,0.155434,-0.386068,-0.905948,-1.55594,-3.22167],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (50.7367,'kcal/mol','+|-',5.2),
        S298 = (-4.56599,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1=C[CH]OC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 7,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.381998,-1.60473,-2.4028,-2.77905,-3.04576,-3.22211,-4.05902],'cal/mol/K','+|-',[3.30452,3.49954,3.81484,3.71541,3.1276,3,3]),
        H298 = (76.4306,'kcal/mol','+|-',16.9882),
        S298 = (0.612728,'cal/mol/K','+|-',5.85652),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux {4,D}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.014017,-1.18277,-2.05434,-2.50069,-2.87067,-3.10035,-3.90747],'cal/mol/K','+|-',[3.05399,3.08786,3.81003,3.88604,3.3997,3,3]),
        H298 = (73.9774,'kcal/mol','+|-',5.2),
        S298 = (-0.275049,'cal/mol/K','+|-',4.05884),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 9,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-1R-R_Ext-5CN-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   C   ux {4,D} {7,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.175006,-1.35734,-2.25345,-2.70882,-3.12007,-3.40833,-4.22783],'cal/mol/K','+|-',[3.53426,3.55421,4.41189,4.49194,3.80021,3.07012,3]),
        H298 = (73.8636,'kcal/mol','+|-',5.2),
        S298 = (-0.0938786,'cal/mol/K','+|-',4.74444),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 10,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-1R-R_Ext-5CN-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 {1,S} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   u0 {3,S} {5,D}
5   C   ux {4,D} {7,[S,D,T,B,Q]}
6   C   u0 {1,S}
7   R!H ux {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H u0 {7,[S,D,T,B,Q]} {9,S}
9   C   ux {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.391431,-1.62549,-3.01577,-3.4831,-3.47874,-3.41856,-3.9605],'cal/mol/K','+|-',[5.24224,5.6222,6.44965,6.57001,5.95267,4.93905,4.42553]),
        H298 = (72.2223,'kcal/mol','+|-',5.2),
        S298 = (-1.85904,'cal/mol/K','+|-',3.34323),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 11,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-1R-R_Ext-5CN-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H_Ext-3R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {6,S}
2    C   u0 r1 {1,S} {3,D}
3    C   ux r1 {2,D} {4,S} {10,[S,D,T,B,Q]}
4    C   u0 r1 {3,S} {5,D}
5    C   ux r1 {4,D} {7,[S,D,T,B,Q]}
6    C   u0 r1 {1,S}
7    R!H ux {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    R!H u0 {7,[S,D,T,B,Q]} {9,S}
9    C   ux {8,S}
10   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46198,-3.61324,-5.29607,-5.80595,-5.58333,-5.16478,-5.52516],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (72.5811,'kcal/mol','+|-',5.2),
        S298 = (-0.67703,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=C(C2=CC=CC2)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 12,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-1R-R_Ext-5CN-R_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   u0 r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C   u0 r1 {4,D} {7,S}
6   C   ux r1 {1,[S,D,T,B,Q]}
7   R!H u0 {5,S} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]} {9,[B,D,T,Q]}
9   C   u0 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.678505,-1.11898,-1.57584,-2.02058,-2.80124,-3.39924,-4.46545],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (74.5628,'kcal/mol','+|-',2.4),
        S298 = (1.47515,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=CC=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 13,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.456864,-0.890526,-2.02439,-2.61489,-3.24276,-3.77231,-4.71097],'cal/mol/K','+|-',[3.01844,3,3,3,3,3,3]),
        H298 = (80.9382,'kcal/mol','+|-',9.06581),
        S298 = (-0.908404,'cal/mol/K','+|-',7.8101),
    ),
    shortDesc = """Radical correction fitted to 24 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 14,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_Ext-3R!H-R",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,D}
3   C ux r1 {2,D} {4,S} {6,[S,D,T,B,Q]}
4   C u0 {3,S} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]}
6   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.11781,-0.198893,-2.20028,-3.31631,-4.12416,-4.55315,-5.39664],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.4608,'kcal/mol','+|-',5.2),
        S298 = (-7.81343,'cal/mol/K','+|-',3.72625),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 15,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,D}
3   C   ux r1 {2,D} {4,S} {6,[S,D,T,B,Q]}
4   C   u0 r1 {3,S} {5,[S,T,Q,B]}
5   C   ux r1 {4,[S,T,Q,B]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.14583,0.0109467,-2.2244,-3.45616,-4.43431,-4.84338,-5.46625],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.02,'kcal/mol','+|-',5.2),
        S298 = (-9.13086,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=C[CH]C=C(CC=CC)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 16,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   O ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.03929,-0.12896,-1.23288,-1.75784,-2.4521,-3.14395,-3.9343],'cal/mol/K','+|-',[4.10259,3.36361,3,3,3,3,3]),
        H298 = (81.8544,'kcal/mol','+|-',6.50285),
        S298 = (-2.46275,'cal/mol/K','+|-',9.95112),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 17,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   O   ux {4,[S,T,Q,B]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4242,-0.132258,-1.42862,-1.92473,-2.54688,-3.19323,-3.68117],'cal/mol/K','+|-',[4.82328,4.18503,3.61277,3,3,3,3]),
        H298 = (83.6217,'kcal/mol','+|-',5.2),
        S298 = (-3.4247,'cal/mol/K','+|-',11.6559),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 18,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O_Ext-1R-R_Ext-5O-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   O   ux {4,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.648271,-0.81744,-1.97051,-2.31374,-2.71354,-3.20207,-3.79085],'cal/mol/K','+|-',[3.55311,3,3,3,3,3,3]),
        H298 = (83.7804,'kcal/mol','+|-',5.79751),
        S298 = (-3.79935,'cal/mol/K','+|-',13.7886),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 19,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O_Ext-1R-R_Ext-5O-R_7R!H->N",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C u0 r1 {3,S} {5,S}
5   O u0 {4,S} {7,S}
6   C ux r1 {1,[S,D,T,B,Q]}
7   N u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.419265,-0.475702,-1.27086,-1.76223,-2.36723,-2.99188,-4.2853],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (84.647,'kcal/mol','+|-',2.4),
        S298 = (1.23323,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1C[CH]C=C1)CC - Radical thermo from pang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 20,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O_Ext-1R-R_Ext-5O-R_N-7R!H->N",
    group = 
"""
1 * C                      u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C                      ux {1,[S,D,T,B,Q]} {3,D}
3   C                      ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C                      ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   O                      ux {4,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   R!H                    ux {1,[S,D,T,B,Q]}
7   [F,I,P,Br,Cl,C,O,Si,S] ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.905903,-1.2019,-2.75761,-2.93419,-3.10314,-3.43854,-3.23458],'cal/mol/K','+|-',[5.62783,4.57381,3.593,3,3,3,3]),
        H298 = (81.7463,'kcal/mol','+|-',7.55759),
        S298 = (-9.461,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 21,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O_Ext-1R-R_Ext-5O-R_N-7R!H->N_Ext-1R-R",
    group = 
"""
1 * C                      u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C                      ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C                      ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C                      ux r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   O                      ux r0 {4,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   R!H                    ux {1,[S,D,T,B,Q]}
7   [F,I,P,Br,Cl,C,O,Si,S] ux {5,[S,D,T,B,Q]}
8   R!H                    ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08383,-2.81898,-4.02793,-3.75317,-2.80245,-2.64064,-2.70464],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.0743,'kcal/mol','+|-',5.2),
        S298 = (-10.4431,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COC1C=C[C](C)CC1OO - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 22,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0101295,-1.23245,-2.29352,-2.85706,-3.44359,-3.92417,-4.9256],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.0665,'kcal/mol','+|-',9.72306),
        S298 = (0.318955,'cal/mol/K','+|-',5.53964),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 23,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux {4,[S,T,Q,B]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.112297,-1.15522,-2.28365,-2.87172,-3.4445,-3.88577,-4.82786],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.8795,'kcal/mol','+|-',7.92605),
        S298 = (0.190365,'cal/mol/K','+|-',5.98522),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 24,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_Int-6R!H-4R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C u0 {3,S} {5,S} {6,[S,D,T,B,Q]}
5   C u0 {4,S} {6,S}
6   C ux {4,[S,D,T,B,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.385693,-0.41383,-1.17228,-1.59862,-2.36496,-3.09812,-4.43674],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.9468,'kcal/mol','+|-',14.8944),
        S298 = (2.56147,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 25,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_Int-6R!H-4R!H_Ext-6R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S} {6,[S,D,T,B,Q]}
5   C   u0 r1 {4,S} {6,S}
6   C   ux r1 {4,[S,D,T,B,Q]} {5,S} {7,S}
7   C   u0 r1 {6,S} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.79604,-0.373959,-1.31728,-1.58777,-2.18831,-2.91931,-4.41535],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (69.6808,'kcal/mol','+|-',5.2),
        S298 = (1.97394,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 26,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux {4,[S,T,Q,B]} {6,S}
6   C   ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.106661,-1.1334,-2.30571,-2.96097,-3.5549,-3.93307,-4.94348],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.556,'kcal/mol','+|-',5.2),
        S298 = (0.357306,'cal/mol/K','+|-',4.96631),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 27,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,D} {7,[S,D,T,B,Q]}
3   C   u0 r1 {2,D} {4,S}
4   R!H u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {6,S}
6   C   u0 {5,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31863,-2.99985,-4.11612,-4.36493,-4.27904,-4.40175,-4.45997],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.8215,'kcal/mol','+|-',5.2),
        S298 = (-2.19635,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]C(C)=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C(C)COOC1[CH]C(C)=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 28,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]} {6,S}
6   C ux {1,[S,D,T,B,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.396284,-0.732331,-1.69314,-2.39795,-3.39867,-4.06291,-5.11863],'cal/mol/K','+|-',[3,3,3,3,3.06503,3,3]),
        H298 = (83.0623,'kcal/mol','+|-',5.2),
        S298 = (0.613847,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 29,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {6,S}
6   C   u0 r1 {1,S} {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.968348,-1.52131,-3.44601,-4.05978,-4.40725,-4.70218,-5.45765],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.7651,'kcal/mol','+|-',5.2),
        S298 = (-1.76525,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1CCC=C[C]1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 30,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R_Ext-6C-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]} {6,S}
6   C ux {1,[S,D,T,B,Q]} {5,S} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.487379,-0.758897,-1.73354,-2.52566,-3.69932,-4.39599,-5.42227],'cal/mol/K','+|-',[3,3,3,3,3.88771,3.83596,3.3614]),
        H298 = (82.9925,'kcal/mol','+|-',7.63573),
        S298 = (0.891582,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 31,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R_Ext-6C-R_Sp-7R!H-6C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]} {6,S}
6   C ux {1,[S,D,T,B,Q]} {5,S} {7,S}
7   C ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.349925,-0.577787,-1.4494,-2.06667,-3.0276,-3.68743,-4.72917],'cal/mol/K','+|-',[3,3,3,3,3.20132,3,3]),
        H298 = (84.0806,'kcal/mol','+|-',5.2),
        S298 = (0.61875,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 32,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R_Ext-6C-R_Sp-7R!H-6C_Ext-6C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux r1 {4,[S,T,Q,B]} {6,S}
6   C   ux r1 {1,[S,D,T,B,Q]} {5,S} {7,S} {8,[S,D,T,B,Q]}
7   C   ux {6,S}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.27252,-0.837608,-2.54074,-3.46,-4.59476,-5.02559,-5.41317],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.3693,'kcal/mol','+|-',5.2),
        S298 = (-0.712704,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1(C)[CH]C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 33,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R_Ext-6C-R_N-Sp-7R!H-6C",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C u0 r1 {3,S} {5,S}
5   C u0 r1 {4,S} {6,S}
6   C u0 r1 {1,S} {5,S} {7,[B,D,T,Q]}
7   C u0 r0 {6,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.934105,-1.3475,-2.65702,-4.01738,-5.88241,-6.69881,-7.67484],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (76.796,'kcal/mol','+|-',5.2),
        S298 = (1.77829,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 34,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C ux r1 {4,[S,T,Q,B]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.773565,-0.40526,-1.87286,-2.63872,-2.99421,-3.00175,-4.22914],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.4071,'kcal/mol','+|-',5.2),
        S298 = (-0.78726,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1C1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]1C=CC(C2=CC=CCC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 35,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   O ux r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C ux r1 {4,[S,T,Q,B]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21563,-2.59299,-4.57772,-5.34252,-4.96046,-4.81587,-6.73983],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.5875,'kcal/mol','+|-',5.2),
        S298 = (6.97426,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1O[CH]C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 36,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux r1 {4,[S,T,Q,B]} {6,S}
6   O   ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.358405,-2.93251,-4.20862,-4.21304,-4.11312,-4.82245,-4.04924],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.3044,'kcal/mol','+|-',5.2),
        S298 = (-6.80556,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 37,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux {4,[S,T,Q,B]} {6,[B,D,T,Q]}
6   R!H u0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.485432,-1.5323,-2.33183,-2.80015,-3.44005,-4.07328,-5.30508],'cal/mol/K','+|-',[3,3,3.09034,3.14623,3,3,3]),
        H298 = (75.274,'kcal/mol','+|-',5.2),
        S298 = (0.818186,'cal/mol/K','+|-',4.18038),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 38,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H-5C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {7,S}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux {4,[S,T,Q,B]} {6,D}
6   R!H u0 {5,D}
7   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.897093,-1.85384,-2.51498,-2.90984,-3.51569,-4.16586,-5.30063],'cal/mol/K','+|-',[3,3,4.06368,4.2454,3.84532,3.89666,3.56653]),
        H298 = (75.5672,'kcal/mol','+|-',5.2),
        S298 = (1.56418,'cal/mol/K','+|-',3.23428),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 39,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H-5C_Ext-2R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {7,S}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux r1 {4,[S,T,Q,B]} {6,D}
6   R!H u0 {5,D}
7   C   u0 r0 {2,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.843316,-3.15124,-4.5043,-4.98811,-5.39811,-6.07341,-7.04657],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.2321,'kcal/mol','+|-',5.2),
        S298 = (3.14748,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1C(=O)OC=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 40,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.550231,-0.336632,-1.20973,-1.68578,-2.19507,-2.68973,-3.93107],'cal/mol/K','+|-',[3,3.6435,4.61087,5.12246,5.73053,6.4172,7.98422]),
        H298 = (76.8251,'kcal/mol','+|-',85.6099),
        S298 = (-0.371788,'cal/mol/K','+|-',5.41802),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 41,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.556674,-0.844157,-1.94305,-2.23882,-2.33861,-2.66446,-4.6724],'cal/mol/K','+|-',[4.20679,5.59632,6.8751,7.35949,7.52855,7.74098,8.71289]),
        H298 = (99.2591,'kcal/mol','+|-',19.1774),
        S298 = (-0.915328,'cal/mol/K','+|-',8.85567),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 42,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   R!H u0 r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.9495,-1.00948,-3.64195,-5.20421,-7.17705,-8.69442,-10.13],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.547,'kcal/mol','+|-',5.2),
        S298 = (0.669818,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1OOC[C]1COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 43,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.157871,-0.816603,-1.6599,-1.74459,-1.5322,-1.65947,-3.7628],'cal/mol/K','+|-',[3.98656,6.12838,7.35028,7.53573,6.79449,6.16206,7.95599]),
        H298 = (96.5444,'kcal/mol','+|-',13.9177),
        S298 = (-1.17952,'cal/mol/K','+|-',9.57927),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 44,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.342149,-0.780286,-1.78826,-1.93107,-1.6698,-1.62429,-3.75759],'cal/mol/K','+|-',[4.60469,7.8169,9.47143,9.62593,8.49129,7.60478,9.95783]),
        H298 = (92.6637,'kcal/mol','+|-',8.67088),
        S298 = (-2.35478,'cal/mol/K','+|-',11.3955),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 45,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R_4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,S}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   R!H u0 r0 {2,D}
4   O   ux r1 {1,S} {6,S}
5   C   u0 r1 {1,S}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8119,-6.42886,-8.61136,-8.75389,-7.30871,-6.39883,-10.5787],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.1324,'kcal/mol','+|-',5.2),
        S298 = (2.02346,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 46,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R_N-4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3935,1.10257,0.486108,0.343204,0.209831,-0.0327818,-1.48388],'cal/mol/K','+|-',[3,3,3.22741,3.85382,4.83326,5.09503,4.96623]),
        H298 = (94.5075,'kcal/mol','+|-',5.5848),
        S298 = (-3.81419,'cal/mol/K','+|-',11.9862),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 47,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R_N-4R!H->O_6R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,S}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   R!H u0 r0 {2,D}
4   C   ux {1,S} {6,S}
5   C   u0 {1,S}
6   O   u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.935148,1.23229,1.10328,1.29583,1.5552,1.38995,-0.107061],'cal/mol/K','+|-',[3,3.56943,3.41916,3,3,3,3]),
        H298 = (94.6763,'kcal/mol','+|-',7.85464),
        S298 = (-7.07188,'cal/mol/K','+|-',5.71309),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 48,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R_N-4R!H->O_6R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,S}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {7,[S,D,T,B,Q]}
3   R!H u0 r0 {2,D}
4   C   ux r1 {1,S} {6,S}
5   C   u0 r1 {1,S}
6   O   u0 r0 {4,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.76517,2.49428,2.31214,2.29106,2.19553,2.03595,0.584999],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.4534,'kcal/mol','+|-',5.2),
        S298 = (-5.052,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C=O)[C]1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 49,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R_N-4R!H->O_N-6R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D}
3   R!H ux r0 {2,D}
4   C   u0 r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux r1 {1,[S,D,T,B,Q]}
6   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.3102,0.843126,-0.748244,-1.56205,-2.48091,-2.87825,-4.23753],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.1697,'kcal/mol','+|-',5.2),
        S298 = (2.70119,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]1CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 50,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54409,-1.63172,-1.23815,-0.639187,0.0473482,-0.302543,-2.23159],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.891,'kcal/mol','+|-',5.2),
        S298 = (1.77702,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C(OO)[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 51,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.603996,-0.521678,-1.34356,-1.95331,-2.94422,-3.58639,-4.67922],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.253,'kcal/mol','+|-',14.7032),
        S298 = (0.212237,'cal/mol/K','+|-',3.05837),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 52,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.21969,-0.76793,-1.84696,-2.47319,-3.46494,-3.97322,-4.98376],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.922,'kcal/mol','+|-',5.2),
        S298 = (0.797239,'cal/mol/K','+|-',4.36326),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 53,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.63366,-0.121351,-1.33911,-2.09918,-2.90572,-3.51521,-4.42947],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.945,'kcal/mol','+|-',5.2),
        S298 = (2.33988,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 54,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r0 {2,D} {4,[S,D,T,B,Q]}
4   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0567129,-0.302788,-0.896099,-1.49118,-2.48136,-3.24254,-4.40852],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.9859,'kcal/mol','+|-',2.4),
        S298 = (-0.307765,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 55,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   R!H u0 r0 {2,D}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.410887,0.261432,-0.165726,-0.586457,-0.842645,-0.991518,-1.1375],'cal/mol/K','+|-',[3,3.57986,5.6476,7.45949,9.65401,11.7292,15.2904]),
        H298 = (19.262,'kcal/mol','+|-',137.615),
        S298 = (0.337126,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 56,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D} {5,S}
3   R!H u0 r0 {2,D}
4   C   u0 {1,S} {7,S}
5   R!H u0 {2,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.733268,-0.502161,-2.12285,-3.42341,-4.70269,-5.72551,-7.38159],'cal/mol/K','+|-',[3.87519,4.93543,4.96709,4.733,4.0086,4.17392,3.99504]),
        H298 = (90.981,'kcal/mol','+|-',9.89261),
        S298 = (0.779912,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 57,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4C-R_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {7,S}
5   R!H u0 r1 {2,S} {6,[S,D,T,B,Q]}
6   R!H ux r1 {5,[S,D,T,B,Q]}
7   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.63682,-2.2471,-3.87898,-5.09677,-6.11994,-7.20121,-5.96913],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.4835,'kcal/mol','+|-',5.2),
        S298 = (1.63834,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 58,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4C-R_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {7,S}
5   R!H u0 r1 {2,S} {6,[S,D,T,B,Q]}
6   R!H ux r1 {5,[S,D,T,B,Q]}
7   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.10336,1.24278,-0.366724,-1.75004,-3.28543,-4.2498,-8.79405],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.4786,'kcal/mol','+|-',5.2),
        S298 = (-0.0785187,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1[CH]C(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 59,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   O   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.610916,0.00572054,-0.968789,-1.62177,-2.49205,-3.37229,-4.59843],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.5045,'kcal/mol','+|-',9.06251),
        S298 = (-0.693733,'cal/mol/K','+|-',3.25811),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 60,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   R!H ux r0 {2,D}
4   O   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.53036,0.603707,-0.769661,-1.51647,-2.38891,-3.40474,-4.68486],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.6528,'kcal/mol','+|-',6.03655),
        S298 = (-1.25114,'cal/mol/K','+|-',3.91973),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 61,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4BrClFINOPSSi-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   R!H u0 r0 {2,D}
4   O   u0 r1 {1,S} {7,S}
5   C   u0 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H u0 r1 {4,S}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.932497,-0.163931,-1.44721,-2.09509,-2.5335,-3.43522,-5.03742],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.9808,'kcal/mol','+|-',5.2),
        S298 = (-3.03629,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(CO)OO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 62,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4BrClFINOPSSi-R_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   O   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,D}
6   C   ux {5,D}
7   R!H ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.06544,1.42881,-0.264604,-0.945121,-1.62447,-2.64032,-4.20234],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.4936,'kcal/mol','+|-',5.2),
        S298 = (0.846007,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]OC(O)C1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 63,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4BrClFINOPSSi-R_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   O   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,D}
6   C   ux {5,D}
7   R!H ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.59314,0.546241,-0.597172,-1.50921,-3.00877,-4.13867,-4.81481],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (76.4839,'kcal/mol','+|-',5.2),
        S298 = (-1.56313,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1OO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 64,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.227909,-1.30903,-2.26285,-2.86295,-3.58526,-4.15337,-5.43168],'cal/mol/K','+|-',[3.28184,4.78266,5.1675,5.03095,4.19303,3.52619,4.1903]),
        H298 = (101.29,'kcal/mol','+|-',10.1267),
        S298 = (1.7373,'cal/mol/K','+|-',7.01533),
    ),
    shortDesc = """Radical correction fitted to 40 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 65,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,S}
3   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.07618,-2.12757,-2.86322,-3.34204,-3.91145,-4.27936,-5.02398],'cal/mol/K','+|-',[3,4.09177,5.02108,5.02199,3.9686,3,3]),
        H298 = (114.247,'kcal/mol','+|-',22.3347),
        S298 = (2.74022,'cal/mol/K','+|-',7.1913),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 66,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux r1 {1,D} {3,S} {4,[S,D,T,B,Q]}
3   R!H u0 r1 {2,S}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.71,-1.23732,-1.77078,-2.2494,-3.048,-3.66438,-4.61619],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (111.474,'kcal/mol','+|-',2.4),
        S298 = (1.1756,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=[C]CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 67,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.302592,-1.26216,-2.22847,-2.83552,-3.56658,-4.14615,-5.45503],'cal/mol/K','+|-',[3.30293,4.86145,5.24908,5.10986,4.26558,3.60029,4.29697]),
        H298 = (100.507,'kcal/mol','+|-',7.42119),
        S298 = (1.67986,'cal/mol/K','+|-',7.11081),
    ),
    shortDesc = """Radical correction fitted to 38 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 68,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   O   ux {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.141025,-0.264866,-0.893041,-1.48067,-2.414,-3.10542,-4.13054],'cal/mol/K','+|-',[2,2,2,2,2.21888,2.30776,2]),
        H298 = (103.973,'kcal/mol','+|-',3.99025),
        S298 = (0.302079,'cal/mol/K','+|-',2.81589),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 69,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,S} {4,S}
3   R!H u0 r0 {2,S}
4   O   ux r1 {1,[S,D,T,B,Q]} {2,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0394068,-0.0412143,-0.496081,-0.972669,-1.86745,-2.6634,-4.12517],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (101.287,'kcal/mol','+|-',2.4),
        S298 = (-1.10965,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 70,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   O   ux r1 {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.349721,-0.433968,-0.537117,-0.7361,-1.24629,-1.82555,-3.26515],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.713,'kcal/mol','+|-',2.4),
        S298 = (-0.481452,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OCC1(O)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 71,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]}
4   O ux r1 {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.22365,0.195092,-1.25453,-2.40676,-3.80074,-4.54877,-4.99643],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (105.849,'kcal/mol','+|-',2.4),
        S298 = (2.08178,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OCC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 72,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   O ux r1 {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.349231,-0.779376,-1.28444,-1.80717,-2.74151,-3.38395,-4.13541],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (105.041,'kcal/mol','+|-',2.4),
        S298 = (0.717637,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 73,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.26103,-1.26118,-2.24728,-2.91246,-3.67465,-4.21421,-5.6042],'cal/mol/K','+|-',[3.15769,4.747,5.2047,5.10786,3.98336,3.03965,4.63079]),
        H298 = (98.4711,'kcal/mol','+|-',6.30333),
        S298 = (1.77031,'cal/mol/K','+|-',4.80245),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 74,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00288291,-1.67466,-2.58732,-3.19628,-3.85581,-4.29621,-5.44036],'cal/mol/K','+|-',[3,4.58189,5.29159,5.3078,4.22243,3.28267,4.66613]),
        H298 = (97.8023,'kcal/mol','+|-',5.68333),
        S298 = (1.987,'cal/mol/K','+|-',4.65706),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 75,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.194009,-0.18743,-0.89884,-1.60502,-2.76319,-3.60109,-4.72059],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.8481,'kcal/mol','+|-',5.2),
        S298 = (0.693907,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 76,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_Sp-4R!H-3R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   R!H ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.240063,-0.210451,-0.984365,-1.70009,-2.89661,-3.7483,-4.82933],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.458,'kcal/mol','+|-',5.2),
        S298 = (0.949847,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 77,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_Sp-4R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   R!H ux r1 {3,S} {5,[S,D,T,B,Q]}
5   R!H u0 r1 {1,S} {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.98591,1.03822,-1.40686,-2.68636,-4.3128,-5.81634,-6.94259],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.6335,'kcal/mol','+|-',5.2),
        S298 = (-0.237344,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)[C]1OCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 78,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_Sp-4R!H-3R!H_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   R!H ux r1 {3,S} {5,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.740247,-0.678845,-1.09769,-1.74572,-3.0165,-3.69503,-4.5715],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.2989,'kcal/mol','+|-',2.4),
        S298 = (1.8144,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 79,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_Sp-4R!H-3R!H_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   ux r1 {3,S} {5,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.311191,-0.625866,-1.06518,-1.58277,-2.55346,-3.31005,-4.49202],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (94.3511,'kcal/mol','+|-',2.4),
        S298 = (-0.325848,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 80,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_Sp-4R!H-3R!H_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   ux r1 {3,S} {5,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.551251,0.118394,-0.602449,-1.33343,-2.49047,-3.32069,-4.48524],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.1125,'kcal/mol','+|-',2.4),
        S298 = (1.88863,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 81,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_N-Sp-4R!H-3R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D}
4   R!H u0 r1 {3,D} {5,S}
5   R!H ux r1 {1,[S,D,T,B,Q]} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0353805,-0.108135,-0.604255,-1.27757,-2.30364,-3.09403,-4.34606],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (93.8886,'kcal/mol','+|-',2.4),
        S298 = (-0.187667,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 82,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.247968,-2.94451,-4.2213,-4.86578,-5.15912,-5.25514,-6.46115],'cal/mol/K','+|-',[3.39798,5.45985,6.29541,6.32736,5.02749,3.75404,6.21281]),
        H298 = (99.2461,'kcal/mol','+|-',5.2),
        S298 = (3.62101,'cal/mol/K','+|-',4.70219),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 83,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.17608,-3.97049,-6.06843,-6.92602,-6.79604,-6.57813,-8.0514],'cal/mol/K','+|-',[3,3,3.27214,3.78426,3.52326,3,7.84399]),
        H298 = (99.3949,'kcal/mol','+|-',7.71474),
        S298 = (5.79087,'cal/mol/K','+|-',3.59077),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 84,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-1R-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   R!H u0 r1 {3,S} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15106,-4.96871,-6.70307,-7.51883,-7.64047,-7.61018,-5.23652],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.402,'kcal/mol','+|-',5.2),
        S298 = (7.61836,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CO[C](C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 85,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-1R-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   R!H ux r1 {3,[S,D,T,B,Q]} {5,S}
5   R!H ux r1 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.55497,-2.42155,-4.21012,-4.80847,-4.77116,-4.91064,-6.38646],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.0767,'kcal/mol','+|-',5.2),
        S298 = (5.72485,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OCC=C(C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 86,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.81391,-5.7997,-7.13881,-7.57388,-7.24904,-6.69354,-7.79307],'cal/mol/K','+|-',[4.6489,3.22198,3,3,3,3,7.17147]),
        H298 = (101.644,'kcal/mol','+|-',5.2),
        S298 = (4.64216,'cal/mol/K','+|-',3.11335),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 87,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-6R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,[S,D]}
5   R!H u0 {4,[S,D]}
6   R!H u0 {1,S} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.15593,-6.62108,-7.24862,-7.44713,-7.11173,-6.57386,-5.72406],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.909,'kcal/mol','+|-',5.2),
        S298 = (4.59503,'cal/mol/K','+|-',4.39688),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 88,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-6R!H-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   u0 r1 {3,[S,D,T,B,Q]} {5,[S,D]}
5   R!H u0 r1 {4,[S,D]}
6   R!H u0 r1 {1,S} {7,[S,D,T,B,Q]}
7   C   ux r1 {6,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.15697,-7.37692,-8.25434,-8.45772,-7.87513,-6.99172,-5.60119],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.253,'kcal/mol','+|-',5.2),
        S298 = (6.14956,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CO[CH]OC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 89,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-6R!H-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   ux r1 {3,S} {5,S}
5   O   ux r1 {4,S}
6   R!H ux r1 {1,[S,D,T,B,Q]} {7,S}
7   C   u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.870133,-4.15694,-6.91919,-7.82738,-7.52366,-6.93292,-11.9311],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.113,'kcal/mol','+|-',5.2),
        S298 = (4.73644,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC1[CH]OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 90,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   R!H ux r1 {2,[S,T,Q,B]}
4   C   ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.560987,-1.41358,-2.72027,-3.28042,-3.86883,-4.33789,-9.72422],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.089,'kcal/mol','+|-',5.2),
        S298 = (4.62555,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#C[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 91,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   O   u0 {1,S} {3,S}
3   R!H u0 {2,S}
4   C   u0 {1,S} {5,S}
5   O   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.32098,1.68008,0.278501,-0.812528,-2.34676,-3.60214,-5.48339],'cal/mol/K','+|-',[3,3,3,3,3,3,3.22854]),
        H298 = (102.869,'kcal/mol','+|-',5.2),
        S298 = (-0.625047,'cal/mol/K','+|-',3.40024),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 92,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S}
4   C u0 r0 {1,S} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.51099,1.81661,0.576545,-0.490708,-2.17003,-3.34506,-4.78095],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.528,'kcal/mol','+|-',2.4),
        S298 = (-1.36484,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 93,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O u0 r1 {1,S} {3,S}
3   O u0 r1 {2,S}
4   C u0 r0 {1,S} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.89348,1.37289,-0.392098,-1.53662,-2.74439,-4.18058,-7.06387],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (104.471,'kcal/mol','+|-',5.2),
        S298 = (1.03949,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 94,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.426751,-1.69599,-2.78321,-3.32303,-3.92588,-4.509,-5.83541],'cal/mol/K','+|-',[4.14145,5.91375,6.18078,5.91696,5.12716,4.51376,4.46078]),
        H298 = (101.534,'kcal/mol','+|-',7.00357),
        S298 = (2.15976,'cal/mol/K','+|-',10.3173),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 95,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.242319,-1.71531,-2.9273,-3.47306,-4.13743,-4.87604,-6.74504],'cal/mol/K','+|-',[3.77147,6.09808,6.28142,6.04669,5.5383,4.92759,4.88705]),
        H298 = (101.894,'kcal/mol','+|-',8.98531),
        S298 = (1.39902,'cal/mol/K','+|-',9.8007),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 96,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.292502,-0.88268,-1.87447,-2.5081,-3.3004,-4.08004,-7.28493],'cal/mol/K','+|-',[4.14554,5.10882,5.42036,5.6401,5.4042,4.75865,5.08386]),
        H298 = (100.716,'kcal/mol','+|-',5.2),
        S298 = (2.38479,'cal/mol/K','+|-',8.23838),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 97,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->O_Int-5R!H-4O",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C u0 {1,S} {3,S}
3   O u0 {2,S} {4,S}
4   O ux {3,S} {5,S}
5   C ux {1,[S,D,T,B,Q]} {4,S} {6,S}
6   O u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.26951,1.14761,0.0212111,-0.223028,-0.721489,-1.87578,-6.5427],'cal/mol/K','+|-',[3.02197,4.19865,4.66629,5.47806,5.50699,4.48503,4.60948]),
        H298 = (101.599,'kcal/mol','+|-',5.63139),
        S298 = (-2.69003,'cal/mol/K','+|-',11.5387),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 98,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->O_Int-5R!H-4O_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S} {4,S}
4   O   ux r1 {3,S} {5,S}
5   C   ux r1 {1,[S,D,T,B,Q]} {4,S} {6,S}
6   O   u0 r0 {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.33794,2.63206,1.671,1.71376,1.22553,-0.290088,-4.913],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.6076,'kcal/mol','+|-',5.2),
        S298 = (-6.76959,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1OOC(O)[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 99,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->O_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   C   ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.48134,-3.65978,-4.54212,-5.01037,-5.25943,-5.42128,-9.64173],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.7777,'kcal/mol','+|-',5.2),
        S298 = (5.51997,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
OOC[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 100,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->O_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
5   C   ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.313567,1.07743,0.657584,-0.145745,-1.52184,-2.61449,-4.3221],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (101.33,'kcal/mol','+|-',2.4),
        S298 = (2.90542,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOCC1[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 101,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.34539,-3.43261,-5.09874,-5.4633,-5.86382,-6.51779,-5.63149],'cal/mol/K','+|-',[3,7.2897,6.31958,5.44809,4.67036,3.96224,4.28854]),
        H298 = (105.045,'kcal/mol','+|-',14.8883),
        S298 = (-0.634118,'cal/mol/K','+|-',12.7987),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 102,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->O_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   O   u0 {3,S}
5   C   u0 r1 {1,S} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.53407,-8.65789,-9.49937,-9.45159,-9.32313,-9.38889,-8.58111],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.702,'kcal/mol','+|-',5.2),
        S298 = (5.96901,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCC(=O)OOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 103,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->O_Ext-2C-R",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
7   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.02322,-2.2949,-4.29926,-4.29519,-4.46608,-5.19954,-4.04771],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.9263,'kcal/mol','+|-',5.2),
        S298 = (-5.86437,'cal/mol/K','+|-',6.21702),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 104,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->O_Ext-2C-R_Ext-7R!H-R_Int-8R!H-6BrCClFINPSSi_Int-8R!H-7R!H_8R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {8,S}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]}
7   C ux r1 {2,[S,D,T,B,Q]}
8   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.598487,-3.08892,-5.15354,-4.9647,-4.61499,-5.18134,-3.92696],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.7045,'kcal/mol','+|-',5.2),
        S298 = (-3.66633,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCC=CC1OOC1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 105,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->O_Ext-2C-R_Ext-7R!H-R_Int-8R!H-6BrCClFINPSSi_Int-8R!H-7R!H_N-8R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {8,S}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]}
7   C ux r1 {2,[S,D,T,B,Q]}
8   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.44795,-1.50087,-3.44499,-3.62569,-4.31717,-5.21774,-4.16845],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.148,'kcal/mol','+|-',5.2),
        S298 = (-8.06242,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)OOC1[CH]CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 106,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.692551,-1.66814,-2.57554,-3.10681,-3.621,-3.98004,-4.52448],'cal/mol/K','+|-',[4.99988,6.24428,6.64169,6.30213,4.91384,4.01804,3]),
        H298 = (101.163,'kcal/mol','+|-',5.2),
        S298 = (3.25611,'cal/mol/K','+|-',11.6699),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 107,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S}
5   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.32836,-0.88084,-1.66426,-2.19736,-2.89155,-3.36388,-4.34268],'cal/mol/K','+|-',[3.43541,4.34529,3.95377,3.24858,3,3,3]),
        H298 = (101.267,'kcal/mol','+|-',5.2),
        S298 = (1.45118,'cal/mol/K','+|-',4.18137),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 108,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S}
5   C ux {2,[S,D,T,B,Q]}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3929,-1.5288,-2.35058,-2.83841,-3.36117,-3.66149,-4.45693],'cal/mol/K','+|-',[4.2652,4.61709,3.91442,3,3,3,3]),
        H298 = (99.675,'kcal/mol','+|-',5.2),
        S298 = (1.26202,'cal/mol/K','+|-',5.13732),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 109,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-1R-R_Ext-6R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S}
5   C ux {2,[S,D,T,B,Q]}
6   C ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.55108,-1.75607,-2.52347,-2.92461,-3.41508,-3.73734,-4.42084],'cal/mol/K','+|-',[5.02432,5.36758,4.57803,3.47486,3,3,3]),
        H298 = (99.8555,'kcal/mol','+|-',5.2),
        S298 = (0.279678,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 110,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-1R-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S} {9,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 r1 {2,S} {4,S}
4   C   ux r1 {3,S}
5   C   ux {2,[S,D,T,B,Q]}
6   C   u0 r1 {1,S} {7,[S,D,T,B,Q]}
7   C   ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C   u0 {7,[S,D,T,B,Q]}
9   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.086767,-0.541953,-1.12412,-1.70169,-2.58638,-3.27802,-4.38916],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (100.612,'kcal/mol','+|-',2.4),
        S298 = (0.123374,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=CC2[C](C1)C1C=CC2C1 - Radical thermo from pang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 111,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-1R-R_Ext-6R!H-R_Ext-7R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux r1 {3,S} {9,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux r1 {6,[S,D,T,B,Q]} {8,S}
8   C   ux {7,S}
9   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.71811,-5.52969,-5.54666,-4.87593,-4.07358,-3.65792,-3.16949],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.0873,'kcal/mol','+|-',5.2),
        S298 = (-0.73999,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCC=CCC1CC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 112,
    label = "RJ1_N-1R-inRing",
    group = 
"""
1 * R u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.7582,-1.70222,-2.3894,-2.79129,-3.20077,-3.56695,-4.30747],'cal/mol/K','+|-',[4.05396,4.78591,5.00098,4.80717,4.15825,3.75744,3.63799]),
        H298 = (94.5399,'kcal/mol','+|-',23.3637),
        S298 = (0.161414,'cal/mol/K','+|-',9.66541),
    ),
    shortDesc = """Radical correction fitted to 419 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 113,
    label = "RJ1_N-1R-inRing_1R->O",
    group = 
"""
1 * O u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.98016,-3.31935,-4.07725,-4.34167,-4.35659,-4.45932,-4.82892],'cal/mol/K','+|-',[4.49863,5.26718,5.52568,5.3609,4.77395,4.43378,4.26782]),
        H298 = (91.9914,'kcal/mol','+|-',23.3722),
        S298 = (-0.437629,'cal/mol/K','+|-',9.27242),
    ),
    shortDesc = """Radical correction fitted to 169 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 114,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.90315,-3.2273,-3.9021,-3.98923,-3.80503,-3.73167,-4.00113],'cal/mol/K','+|-',[5.46126,6.14051,6.09909,5.54011,4.32214,3.91756,3.76022]),
        H298 = (96.1222,'kcal/mol','+|-',32.3637),
        S298 = (0.438097,'cal/mol/K','+|-',9.55593),
    ),
    shortDesc = """Radical correction fitted to 70 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 115,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.57308,-4.43767,-5.03517,-4.89415,-4.21779,-3.73923,-3.64733],'cal/mol/K','+|-',[4.90894,6.22321,6.41832,5.66358,3.94933,3.55361,4.00109]),
        H298 = (80.8125,'kcal/mol','+|-',23.7429),
        S298 = (1.97239,'cal/mol/K','+|-',11.0449),
    ),
    shortDesc = """Radical correction fitted to 35 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 116,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.57503,-4.47123,-5.07074,-4.91613,-4.20962,-3.70918,-3.59613],'cal/mol/K','+|-',[4.9721,6.28809,6.48435,5.72933,3.99877,3.5779,3.99704]),
        H298 = (80.2597,'kcal/mol','+|-',22.5069),
        S298 = (2.04781,'cal/mol/K','+|-',11.1436),
    ),
    shortDesc = """Radical correction fitted to 34 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 117,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.16257,-2.62399,-2.89082,-2.97758,-2.95839,-2.99637,-3.69492],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (68.2346,'kcal/mol','+|-',15.1871),
        S298 = (-1.07725,'cal/mol/K','+|-',9.29863),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 118,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_5R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 {2,D} {4,S}
4   R!H u0 {3,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.46835,-2.60571,-2.75239,-2.85958,-2.96632,-2.96539,-4.15158],'cal/mol/K','+|-',[3,3,3.6822,3.45941,3,3,3]),
        H298 = (65.5013,'kcal/mol','+|-',8.44498),
        S298 = (1.04705,'cal/mol/K','+|-',16.11),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 119,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_5R!H->C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   u0 r1 {2,D} {4,S}
4   R!H u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.37196,-3.77424,-4.55496,-4.55309,-4.08348,-3.30053,-5.52276],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (70.4241,'kcal/mol','+|-',5.2),
        S298 = (8.93347,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1C=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 120,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_N-5R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97328,-2.63531,-2.97651,-3.05062,-2.95347,-3.01555,-3.41223],'cal/mol/K','+|-',[3,3,3.01475,3,3,3,3]),
        H298 = (70.2575,'kcal/mol','+|-',20.3905),
        S298 = (-2.3923,'cal/mol/K','+|-',6.07175),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 121,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux r1 {3,[S,D,T,B,Q]} {5,S}
5   O   u0 r1 {4,S} {6,S}
6   R!H u0 r1 {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.66631,-3.37298,-4.06102,-4.20279,-3.99784,-3.76235,-3.98486],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.2191,'kcal/mol','+|-',5.2),
        S298 = (2.12404,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 122,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_N-5R!H->C_Ext-4R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63247,-4.5066,-4.67366,-4.00455,-2.83164,-2.33266,-1.55225],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (72.2984,'kcal/mol','+|-',5.2),
        S298 = (-4.32244,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=C(O)C(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 123,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_N-5R!H->C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   R!H ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12607,-2.63572,-3.29797,-3.53999,-3.67747,-3.99023,-4.40596],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (62.4702,'kcal/mol','+|-',5.2),
        S298 = (-5.54909,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=C(COO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 124,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.68545,-4.96577,-5.65434,-5.43511,-4.5446,-3.90001,-3.56969],'cal/mol/K','+|-',[5.54596,6.66671,6.72309,5.94166,4.19317,3.90812,4.38651]),
        H298 = (84.3792,'kcal/mol','+|-',18.5008),
        S298 = (2.88444,'cal/mol/K','+|-',11.192),
    ),
    shortDesc = """Radical correction fitted to 28 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 125,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.72531,-5.99247,-6.41262,-5.85477,-4.4374,-3.53262,-3.13676],'cal/mol/K','+|-',[5.26678,6.90232,7.30808,6.86679,5.29053,4.78269,4.58427]),
        H298 = (84.0563,'kcal/mol','+|-',26.3067),
        S298 = (1.74116,'cal/mol/K','+|-',9.43079),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 126,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63289,-6.28517,-6.9672,-6.49657,-4.96083,-4.03071,-3.51276],'cal/mol/K','+|-',[5.58151,7.08866,7.19105,6.49984,4.98265,4.7514,5.18917]),
        H298 = (91.8171,'kcal/mol','+|-',9.02109),
        S298 = (2.30386,'cal/mol/K','+|-',8.13175),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 127,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.27753,-5.71043,-6.3015,-5.7919,-4.24634,-3.30943,-3.20794],'cal/mol/K','+|-',[5.89076,6.96593,6.46708,5.26514,3.10848,3,5.49943]),
        H298 = (92.0169,'kcal/mol','+|-',8.9753),
        S298 = (1.32621,'cal/mol/K','+|-',7.08296),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 128,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.15068,-6.87491,-7.46584,-6.70615,-4.52368,-3.26475,-3.32119],'cal/mol/K','+|-',[8.67349,9.96837,8.85905,7.02192,4.18787,4.16594,9.15399]),
        H298 = (95.2463,'kcal/mol','+|-',7.44356),
        S298 = (1.21967,'cal/mol/K','+|-',11.2849),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 129,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D} {7,S}
4   C   u0 {2,S} {5,[S,D,T,B,Q]} {6,S}
5   R!H u0 {4,[S,D,T,B,Q]}
6   O   ux {4,S}
7   O   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.05771,-8.88893,-8.89813,-7.16722,-3.54578,-1.5732,0.236515],'cal/mol/K','+|-',[11.7792,14.5172,13.3153,10.843,5.00616,3,4.82461]),
        H298 = (96.5948,'kcal/mol','+|-',10.2883),
        S298 = (-1.43879,'cal/mol/K','+|-',12.3575),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 130,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-3C-R_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D} {7,S}
4   C u0 r0 {2,S} {5,[S,D,T,B,Q]} {6,S}
5   C u0 r0 {4,[S,D,T,B,Q]}
6   O ux r0 {4,S}
7   O u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.2223,-14.0215,-13.6058,-11.0008,-5.31573,-1.25438,1.94227],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.232,'kcal/mol','+|-',5.2),
        S298 = (2.93024,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=CO)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 131,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-3C-R_N-5R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D} {7,S}
4   C u0 r0 {2,S} {5,S} {6,S}
5   O u0 r0 {4,S}
6   O ux r0 {4,S}
7   O u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.89312,-3.75631,-4.19044,-3.33364,-1.77583,-1.89202,-1.46924],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.9573,'kcal/mol','+|-',5.2),
        S298 = (-5.80781,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 132,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_4C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.13936,-6.53624,-7.81282,-8.08049,-6.73914,-5.78323,-8.66751],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.8748,'kcal/mol','+|-',5.2),
        S298 = (7.6903,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 133,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_N-4C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.347943,-3.18553,-4.25426,-4.40967,-4.26403,-4.12938,-5.0903],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.9206,'kcal/mol','+|-',5.2),
        S298 = (0.0659441,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 134,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.12063,-4.24036,-4.8151,-4.59406,-3.77708,-3.31889,-3.3402],'cal/mol/K','+|-',[3.1543,4.36565,4.439,3.92035,3,3,3]),
        H298 = (88.1997,'kcal/mol','+|-',5.2),
        S298 = (0.448261,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 135,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux r0 {2,[S,D,T,B,Q]} {5,S}
5   R!H ux r0 {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.833731,-3.30234,-4.30371,-4.4312,-4.33685,-4.22872,-4.3026],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.152,'kcal/mol','+|-',5.2),
        S298 = (1.90368,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 136,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D} {6,S}
4   C   u0 {2,S} {5,S}
5   O   u0 {4,S}
6   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.84846,-5.20857,-5.72354,-5.40423,-4.29984,-3.75833,-3.37486],'cal/mol/K','+|-',[4.34426,6.49387,6.68196,5.6792,3.00469,3,3]),
        H298 = (87.5566,'kcal/mol','+|-',5.2),
        S298 = (0.257916,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 137,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D} {6,S}
4   C u0 r0 {2,S} {5,S}
5   O u0 r0 {4,S}
6   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31253,-2.91264,-3.36111,-3.39633,-3.23752,-3.48418,-4.14387],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.2301,'kcal/mol','+|-',5.2),
        S298 = (-0.306429,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 138,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D} {4,S}
3   C                      u0 r0 {2,D} {6,S}
4   C                      u0 r0 {2,S} {5,S}
5   O                      u0 r0 {4,S}
6   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.38439,-7.5045,-8.08597,-7.41213,-5.36216,-4.03249,-2.60585],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.883,'kcal/mol','+|-',5.2),
        S298 = (0.822261,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=CO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 139,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D}
4   C u0 {2,S} {5,D}
5   C u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.84506,-6.32164,-6.94561,-6.35905,-4.63019,-3.37986,-2.71694],'cal/mol/K','+|-',[4.53679,4.70884,4.63527,4.06957,3,3,3]),
        H298 = (93.1926,'kcal/mol','+|-',11.2496),
        S298 = (3.2952,'cal/mol/K','+|-',3.16335),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 140,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D} {6,[S,D,T,B,Q]}
4   C   u0 {2,S} {5,D}
5   C   u0 {4,D}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.44906,-7.98647,-8.58443,-7.79786,-5.4699,-3.63039,-1.8736],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.2153,'kcal/mol','+|-',5.2),
        S298 = (2.17678,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 141,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_3C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D}
4   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.31601,-11.302,-13.5755,-13.4851,-11.3531,-10.2008,-5.49906],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.2985,'kcal/mol','+|-',5.2),
        S298 = (9.60231,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC([O])=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 142,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_N-3C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5033,-7.01573,-7.01592,-6.55477,-5.71338,-5.07342,-4.57467],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.3376,'kcal/mol','+|-',5.2),
        S298 = (4.78195,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 143,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D}
4   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.94712,-5.28997,-5.08163,-4.31445,-3.18118,-2.33721,-2.23436],'cal/mol/K','+|-',[4.99359,6.99195,7.67317,7.45814,5.7015,4.39217,3]),
        H298 = (65.4304,'kcal/mol','+|-',9.32731),
        S298 = (0.390677,'cal/mol/K','+|-',12.6884),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 144,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D}
4   O u0 {2,S} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.75025,-4.95973,-4.70418,-3.98571,-3.06519,-2.3383,-2.35251],'cal/mol/K','+|-',[5.67577,7.89145,8.64316,8.44294,6.55622,5.07164,3]),
        H298 = (66.9234,'kcal/mol','+|-',7.52053),
        S298 = (0.068133,'cal/mol/K','+|-',14.5563),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 145,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   O   u0 {2,S} {5,S}
5   C   u0 {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.99011,-4.17081,-3.7318,-3.0041,-2.47329,-2.02113,-2.06409],'cal/mol/K','+|-',[8.87328,12.9694,14.1657,13.8139,10.9088,8.47214,3.58297]),
        H298 = (67.8918,'kcal/mol','+|-',9.82372),
        S298 = (-1.27677,'cal/mol/K','+|-',22.4366),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 146,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D} {8,[S,D,T,B,Q]}
4   O   u0 {2,S} {5,S}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.12729,-8.75617,-8.74013,-7.88806,-6.33012,-5.01648,-3.33086],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (71.365,'kcal/mol','+|-',5.2),
        S298 = (6.65576,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 147,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D}
4   O u0 r0 {2,S} {5,S}
5   C u0 r0 {4,S} {6,S}
6   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.551,-6.78921,-6.69621,-5.94252,-4.39411,-3.34267,-3.10029],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (68.6514,'kcal/mol','+|-',5.2),
        S298 = (5.00678,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 148,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D}
4   O u0 r0 {2,S} {5,S}
5   C u0 r0 {4,S} {6,[B,D,T,Q]}
6   C u0 r0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.46978,-4.7081,-4.6569,-3.99211,-2.92005,-1.96827,-2.18156],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (63.2586,'kcal/mol','+|-',5.2),
        S298 = (-2.18071,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 149,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.61924,-5.64087,-6.71537,-6.40831,-5.04146,-3.88622,-2.82606],'cal/mol/K','+|-',[3.95117,3.96496,3.66708,3,3,3,4.26838]),
        H298 = (87.5647,'kcal/mol','+|-',7.31087),
        S298 = (-0.493051,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 150,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H u0 {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   R!H u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5424,-7.93374,-8.26219,-7.32036,-4.84811,-2.86917,0.0823629],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.6551,'kcal/mol','+|-',5.2),
        S298 = (-0.611679,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 151,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.64486,-4.87658,-6.19977,-6.10429,-5.10592,-4.22524,-3.79553],'cal/mol/K','+|-',[3,3.09225,3.71361,3.22498,3,3,3]),
        H298 = (89.2012,'kcal/mol','+|-',5.2),
        S298 = (-0.453508,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 152,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,S}
6   R!H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42174,-3.99025,-5.12945,-5.17374,-4.57516,-3.95595,-4.41139],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.084,'kcal/mol','+|-',5.2),
        S298 = (-0.183724,'cal/mol/K','+|-',3.93117),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 153,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_4R!H->C_6R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C u0 {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,S}
6   O u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.51397,-4.17408,-5.23424,-5.12546,-4.32026,-3.43748,-4.17683],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.5624,'kcal/mol','+|-',5.2),
        S298 = (-1.5736,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=C[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 154,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_4R!H->C_N-6R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C u0 {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,S}
6   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32952,-3.80643,-5.02466,-5.22202,-4.83007,-4.47443,-4.64595],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.6055,'kcal/mol','+|-',5.2),
        S298 = (1.20616,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=C[O])C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 155,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {4,S} {5,S}
4   O ux r0 {3,S}
5   C u0 r0 {3,S} {6,[S,T,Q,B]}
6   C ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09109,-6.64922,-8.34041,-7.9654,-6.16742,-4.76381,-2.56382],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.4358,'kcal/mol','+|-',5.2),
        S298 = (-0.993076,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 156,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_4R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {4,[S,D,T,B,Q]}
4   R!H u0 r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.9045,-7.39622,-9.90787,-9.85255,-7.76493,-6.71476,-8.81574],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.4445,'kcal/mol','+|-',5.2),
        S298 = (7.42729,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=CC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 157,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   R!H ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.877066,-2.64939,-3.46066,-3.85106,-4.19738,-4.25755,-4.09154],'cal/mol/K','+|-',[5.58154,5.44285,4.58645,3.44307,3,3,3]),
        H298 = (83.2484,'kcal/mol','+|-',6.23751),
        S298 = (5.79756,'cal/mol/K','+|-',14.6545),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 158,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D} {4,[S,D,T,B,Q]}
4   C u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.825482,-2.46907,-3.28697,-3.75934,-4.29124,-4.50074,-4.36267],'cal/mol/K','+|-',[6.0054,5.72599,4.788,3.65395,3,3,3]),
        H298 = (82.7537,'kcal/mol','+|-',5.2),
        S298 = (3.66127,'cal/mol/K','+|-',4.47492),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 159,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.161819,-1.62326,-2.70143,-3.42935,-4.26,-4.58318,-4.40619],'cal/mol/K','+|-',[7.27863,6.93081,5.73103,4.25226,3,3,3]),
        H298 = (81.9149,'kcal/mol','+|-',5.2),
        S298 = (3.8442,'cal/mol/K','+|-',4.7534),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 160,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 r0 {3,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.0823,-0.441455,-2.22506,-3.46518,-4.87583,-5.4046,-4.93075],'cal/mol/K','+|-',[6.95706,9.41178,8.79074,6.73649,3,3,3.57649]),
        H298 = (83.0414,'kcal/mol','+|-',5.2),
        S298 = (5.05569,'cal/mol/K','+|-',4.80197),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 161,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R_Sp-5R!H-4C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 r0 {3,S} {5,S}
5   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59595,1.60628,-0.312451,-1.99952,-4.39997,-5.43692,-5.70889],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (82.9113,'kcal/mol','+|-',2.4),
        S298 = (4.01092,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 162,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R_N-Sp-5R!H-4C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 r0 {3,S} {5,[B,D,T,Q]}
5   C u0 r0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32343,-5.04885,-6.52844,-6.76293,-5.94651,-5.33188,-3.17993],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.6523,'kcal/mol','+|-',5.2),
        S298 = (7.40642,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=CC=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 163,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D} {4,D}
4   C u0 r0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.4963,-3.90044,-4.2779,-4.31778,-4.3441,-4.36123,-4.28901],'cal/mol/K','+|-',[3,3.07298,3.89854,3.91976,3,3,3]),
        H298 = (84.2842,'kcal/mol','+|-',7.3853),
        S298 = (3.3517,'cal/mol/K','+|-',6.32161),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 164,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C_Ext-4C-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {4,D}
4   C   u0 r0 {3,D} {5,[S,D,T,B,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.18861,-3.23185,-3.42968,-3.46495,-3.82033,-4.08149,-4.04745],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (85.2012,'kcal/mol','+|-',2.4),
        S298 = (1.9763,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 165,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32842,-4.22716,-4.98042,-4.65365,-3.37613,-2.12961,-1.71919],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.2046,'kcal/mol','+|-',5.2),
        S298 = (24.4901,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 166,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.49453,-3.08702,-3.60354,-4.00941,-4.54664,-4.94863,-5.70787],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (109.816,'kcal/mol','+|-',5.2),
        S298 = (-1.06324,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CCCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 167,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.33628,-2.20314,-2.94335,-3.22353,-3.45578,-3.72528,-4.3005],'cal/mol/K','+|-',[5.7192,5.34311,5.16514,5.01877,4.55813,4.25803,3.49131]),
        H298 = (106.945,'kcal/mol','+|-',15.664),
        S298 = (-0.860152,'cal/mol/K','+|-',7.27835),
    ),
    shortDesc = """Radical correction fitted to 35 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 168,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 {1,S} {3,S} {4,[S,D,T,B,Q]}
3   R!H u0 {2,S} {4,[S,D,T,B,Q]}
4   R!H u0 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3742,-0.864459,-1.04516,-1.19075,-1.67771,-2.15229,-3.34269],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (47.7999,'kcal/mol','+|-',5.2),
        S298 = (-2.10889,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C12OC1(O)O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 169,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.0638,-3.56313,-5.24675,-5.83751,-6.00218,-6.1337,-6.70837],'cal/mol/K','+|-',[13.1643,10.984,9.42768,8.49284,7.33084,7.11583,5.13424]),
        H298 = (110.047,'kcal/mol','+|-',19.8561),
        S298 = (1.83191,'cal/mol/K','+|-',9.69),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 170,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.62845,-0.886092,-3.06243,-3.81136,-4.51011,-4.90252,-6.35369],'cal/mol/K','+|-',[5.79413,6.38955,5.72834,4.77015,3.267,3,4.07465]),
        H298 = (117.786,'kcal/mol','+|-',22.1931),
        S298 = (-1.53274,'cal/mol/K','+|-',8.05338),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 171,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-4O_Int-6R!H-5R!H_6R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O u0 {3,[S,D,T,B,Q]} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.11513,0.939844,-1.40942,-2.4691,-3.8455,-4.81835,-5.75222],'cal/mol/K','+|-',[3.75475,3,3,3,3.27805,3.40515,4.95209]),
        H298 = (122.618,'kcal/mol','+|-',20.6094),
        S298 = (-3.10513,'cal/mol/K','+|-',8.38906),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 172,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-4O_Int-6R!H-5R!H_6R!H->O_6O-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   C u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   O ux r1 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.44264,1.392,-1.48784,-3.00163,-5.00446,-6.02225,-7.50305],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (129.904,'kcal/mol','+|-',5.2),
        S298 = (-0.139146,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1(O)OOC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 173,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-4O_Int-6R!H-5R!H_6R!H->O_N-6O-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   C u0 r1 {4,S} {6,D}
6   O ux r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.78763,0.487687,-1.33101,-1.93656,-2.68653,-3.61444,-4.00139],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.331,'kcal/mol','+|-',5.2),
        S298 = (-6.07111,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C(=O)OOC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 174,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-4O_Int-6R!H-5R!H_N-6R!H->O",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r1 {1,S} {3,S}
3   O                      u0 r1 {2,S} {4,S}
4   O                      ux r1 {3,S} {5,[S,D,T,B,Q]}
5   C                      ux r1 {4,[S,D,T,B,Q]} {6,S}
6   [F,I,P,Br,Cl,C,Si,S,N] u0 r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34493,-4.53796,-6.36845,-6.49588,-5.83932,-5.07085,-7.55663],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.122,'kcal/mol','+|-',5.2),
        S298 = (1.61203,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C1CC(C)([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 175,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S}
3   R!H u0 {2,S} {4,S}
4   C   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.83298,-5.5709,-6.88499,-7.35713,-7.12123,-7.05709,-6.97439],'cal/mol/K','+|-',[15.1257,12.8028,11.0674,10.0175,9.20777,9.3133,6.38527]),
        H298 = (104.243,'kcal/mol','+|-',6.39701),
        S298 = (4.3554,'cal/mol/K','+|-',8.08135),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 176,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   R!H u0 {2,S} {4,S}
4   C   ux {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.391151,-1.8606,-3.58775,-4.41962,-4.65307,-4.58228,-6.9183],'cal/mol/K','+|-',[7.05399,7.90994,7.93318,7.36919,4.17524,3,4.91865]),
        H298 = (101.787,'kcal/mol','+|-',5.2),
        S298 = (2.85485,'cal/mol/K','+|-',12.3131),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 177,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2C-R_Ext-2C-R_3R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   u0 r1 {2,S} {4,S}
4   C   ux r1 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.88511,-4.65719,-6.39255,-7.02503,-6.12924,-5.30204,-8.65731],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.547,'kcal/mol','+|-',5.2),
        S298 = (7.20819,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1([O])CCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 178,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2C-R_Ext-2C-R_N-3R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   O   u0 r1 {2,S} {4,S}
4   C   ux r1 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.10281,0.935985,-0.782946,-1.81422,-3.1769,-3.86251,-5.1793],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.027,'kcal/mol','+|-',5.2),
        S298 = (-1.49849,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1(O)OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 179,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 r1 {1,S} {3,S}
3   [C,O] u0 r1 {2,S} {4,S}
4   C     u0 r1 {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H   ux {4,[S,D,T,B,Q]}
6   R!H   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.6085,-14.3913,-14.2223,-13.9804,-13.7644,-13.977,-3.52919],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (106.267,'kcal/mol','+|-',5.2),
        S298 = (6.87366,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1CC(=O)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 180,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21038,-2.00237,-2.59425,-2.82439,-3.06199,-3.35016,-3.91038],'cal/mol/K','+|-',[3.52291,3.77513,3.72442,3.65246,3.34768,3.01817,3]),
        H298 = (107.499,'kcal/mol','+|-',5.2),
        S298 = (-1.29195,'cal/mol/K','+|-',6.58938),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 181,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09994,-1.74257,-2.09805,-2.18331,-2.47504,-2.87264,-3.34886],'cal/mol/K','+|-',[4.40509,3.9754,3.2922,3.04632,3,3,3]),
        H298 = (108.001,'kcal/mol','+|-',5.2),
        S298 = (-2.2541,'cal/mol/K','+|-',7.32204),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 182,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-4R!H-R",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   C u0 {3,D} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.50658,-3.63571,-3.48397,-3.31781,-3.14871,-3.03994,-3.06009],'cal/mol/K','+|-',[3,3,3.20052,3.39683,3.39554,3.37854,3.96276]),
        H298 = (109.954,'kcal/mol','+|-',5.2),
        S298 = (-4.23984,'cal/mol/K','+|-',6.22733),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 183,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   C   u0 {3,D} {5,S}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.11437,-2.68512,-2.35242,-2.11685,-1.94821,-1.84544,-1.65904],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.374,'kcal/mol','+|-',5.2),
        S298 = (-6.44153,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C=O)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 184,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.320407,-1.22758,-1.80879,-1.99785,-2.46939,-2.97212,-3.56929],'cal/mol/K','+|-',[3,3.18702,3,3,3.20719,3,3]),
        H298 = (108.84,'kcal/mol','+|-',5.2),
        S298 = (-1.95992,'cal/mol/K','+|-',8.45288),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 185,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.835258,-1.54113,-1.74245,-1.91546,-2.62799,-3.29192,-3.98937],'cal/mol/K','+|-',[5.15659,4.17176,3,3,3,3,3]),
        H298 = (107.598,'kcal/mol','+|-',5.2),
        S298 = (-0.0559569,'cal/mol/K','+|-',8.87382),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 186,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_Ext-2C-R_4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   C   ux {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.95718,-2.44878,-2.31894,-2.28706,-3.0207,-3.72295,-4.10253],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (107.326,'kcal/mol','+|-',2.4),
        S298 = (1.87473,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C=O)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 187,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_Ext-2C-R_N-4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   O   ux {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.68908,0.501097,-0.445348,-1.07936,-1.7444,-2.32211,-3.73475],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.876,'kcal/mol','+|-',5.2),
        S298 = (-4.4,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C(C)([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 188,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   C   ux {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.155014,-0.606942,-1.25419,-1.20246,-1.33577,-1.71807,-2.5257],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.456,'kcal/mol','+|-',5.2),
        S298 = (-5.80325,'cal/mol/K','+|-',4.24605),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 189,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,D} {6,S}
4   C   ux {3,D}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0604589,-0.956021,-1.47977,-1.29624,-1.3708,-1.60256,-2.45698],'cal/mol/K','+|-',[3,3.25626,3.21054,3.009,3,3,3]),
        H298 = (110.688,'kcal/mol','+|-',6.6776),
        S298 = (-6.05562,'cal/mol/K','+|-',5.87617),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 190,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_4R!H->C_Ext-3R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,D} {6,S}
4   C   ux {3,D}
5   C   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H u0 r0 {3,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8418,0.195242,-0.344673,-0.232399,-0.416515,-0.838626,-2.26743],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.327,'kcal/mol','+|-',5.2),
        S298 = (-8.13316,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 191,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_N-4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {5,S}
3   C   u0 {2,S} {4,D}
4   O   u0 {3,D}
5   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.244407,-1.48692,-2.38706,-2.81444,-3.35722,-3.80991,-4.11254],'cal/mol/K','+|-',[3.33716,5.09345,5.07113,5.32111,5.60635,4.73774,3.12812]),
        H298 = (109.232,'kcal/mol','+|-',5.2),
        S298 = (-0.3162,'cal/mol/K','+|-',10.7643),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 192,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_N-4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {5,S}
3   C   u0 r0 {2,S} {4,D} {6,[S,D,T,B,Q]}
4   O   u0 r0 {3,D}
5   R!H u0 r0 {2,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.38925,1.0065,0.0954418,-0.209571,-0.612713,-1.49061,-2.58121],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (109.482,'kcal/mol','+|-',5.2),
        S298 = (-5.5857,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 193,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,D} {5,S}
4   C   u0 r0 {3,D}
5   C   u0 r0 {3,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.5291,1.6487,0.824065,0.25046,-0.541917,-1.54407,-1.91976],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (104.496,'kcal/mol','+|-',5.2),
        S298 = (-5.27581,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 194,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.27304,-2.14976,-2.87575,-3.18807,-3.39497,-3.62106,-4.22893],'cal/mol/K','+|-',[3.06731,3.75985,3.94316,3.86141,3.48389,3.18084,3]),
        H298 = (107.255,'kcal/mol','+|-',5.2),
        S298 = (-0.746109,'cal/mol/K','+|-',6.10959),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 195,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing",
    group = 
"""
1 * O     u1 r0 {2,[S,D,T,B,Q]}
2   C     ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C     ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   [C,O] ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.20117,-2.64943,-3.79703,-4.2634,-4.38757,-4.48425,-4.96237],'cal/mol/K','+|-',[3,3,3,3,3.18921,3.28001,3.13807]),
        H298 = (108.768,'kcal/mol','+|-',5.2),
        S298 = (0.530478,'cal/mol/K','+|-',3.13078),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 196,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-4R!H-R",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 r0 {1,S} {3,S}
3   C     u0 r1 {2,S} {4,[S,T,Q,B]} {5,S}
4   [C,O] ux {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
5   [C,O] u0 {3,S} {6,S}
6   O     ux {5,S}
7   R!H   u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.990165,-3.17976,-4.85861,-5.66281,-5.64775,-5.45899,-5.58861],'cal/mol/K','+|-',[3,3.13332,3,3,3,3,3]),
        H298 = (112.168,'kcal/mol','+|-',5.2),
        S298 = (1.4261,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 197,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 r0 {1,S} {3,S}
3   C     u0 r1 {2,S} {4,[S,T,Q,B]} {5,S} {8,[S,D,T,B,Q]}
4   [C,O] ux r1 {3,[S,T,Q,B]} {7,S}
5   [C,O] u0 r1 {3,S} {6,S}
6   O     ux r1 {5,S}
7   R!H   u0 r1 {4,S}
8   R!H   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.273125,-2.07196,-4.1565,-5.53586,-6.07736,-6.42326,-5.3411],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.865,'kcal/mol','+|-',5.2),
        S298 = (0.515398,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 198,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.28896,-1.9667,-2.70971,-2.88532,-2.81281,-2.95385,-4.59234],'cal/mol/K','+|-',[3,3,3,3,3,3,6.08159]),
        H298 = (107.761,'kcal/mol','+|-',5.2),
        S298 = (-0.819552,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 199,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_5R!H->C_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux r1 {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24842,-1.74679,-3.09912,-3.46218,-2.92185,-3.09424,-7.56949],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.82,'kcal/mol','+|-',5.2),
        S298 = (0.329631,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1OC1(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 200,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 r0 {1,S} {3,S}
3   C     u0 r1 {2,S} {4,S}
4   [C,O] u0 r1 {3,S} {5,S}
5   O     u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26193,-3.16419,-4.42396,-5.01004,-5.54206,-5.82839,-4.94019],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (108.542,'kcal/mol','+|-',2.4),
        S298 = (1.68441,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CC1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 201,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.30217,-1.94719,-2.50226,-2.75213,-2.99256,-3.27112,-3.93159],'cal/mol/K','+|-',[3.66027,4.32203,4.30014,3.98699,3.41022,3.01625,3]),
        H298 = (106.69,'kcal/mol','+|-',5.2),
        S298 = (-1.26364,'cal/mol/K','+|-',6.83882),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 202,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34424,-2.06284,-2.64095,-2.8874,-3.1189,-3.38051,-3.97842],'cal/mol/K','+|-',[3.76263,4.33938,4.25913,3.93028,3.32968,3,3]),
        H298 = (106.695,'kcal/mol','+|-',5.2),
        S298 = (-1.00192,'cal/mol/K','+|-',6.65032),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 203,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5379,-2.02349,-2.46776,-2.42754,-2.0767,-2.06245,-2.92394],'cal/mol/K','+|-',[4.2862,4.91675,5.04828,5.05559,4.38692,3.74992,3]),
        H298 = (105.29,'kcal/mol','+|-',5.6274),
        S298 = (-3.96328,'cal/mol/K','+|-',7.21164),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 204,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.37349,-2.94525,-3.42462,-3.3954,-2.94712,-2.88735,-3.43383],'cal/mol/K','+|-',[3.28637,3.98379,4.03156,3.98202,3.26868,3,3]),
        H298 = (106.622,'kcal/mol','+|-',5.2),
        S298 = (-2.68165,'cal/mol/K','+|-',6.21206),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 205,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {7,[S,D,T,B,Q]}
3   R!H u0 r0 {2,S} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.561205,-0.758197,-1.46141,-1.51091,-1.39274,-1.93466,-3.02646],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (106.648,'kcal/mol','+|-',5.2),
        S298 = (-4.47588,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 206,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.76623,-3.42212,-3.32332,-3.19719,-2.7975,-2.64975,-3.23374],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.499,'kcal/mol','+|-',5.2),
        S298 = (-4.47396,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC(=O)CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 207,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_N-3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.79303,-4.65542,-5.48914,-5.4781,-4.65113,-4.07765,-4.04129],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.718,'kcal/mol','+|-',5.2),
        S298 = (0.904887,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 208,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,S}
4   C   u0 r0 {3,S} {5,[S,D]} {6,[S,D]}
5   O   ux {4,[S,D]}
6   O   u0 r0 {4,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.968866,0.741762,0.402841,0.476043,0.534574,0.412253,-1.39425],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.294,'kcal/mol','+|-',5.2),
        S298 = (-7.80818,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(O)(O)OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 209,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.02501,-0.473403,-1.83654,-2.77456,-4.1174,-4.90407,-5.43838],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (107.966,'kcal/mol','+|-',2.4),
        S298 = (2.07758,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]COOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 210,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.43909,-3.5454,-4.03926,-4.11299,-3.98553,-4.00715,-4.20538],'cal/mol/K','+|-',[3.88212,4.41098,4.45038,4.02211,3.1963,2.33267,2]),
        H298 = (107.15,'kcal/mol','+|-',3.09597),
        S298 = (1.10325,'cal/mol/K','+|-',4.89885),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 211,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   R!H u0 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   C   u0 r0 {3,S} {5,[S,D,T,B,Q]}
5   O   u0 r0 {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.328727,-0.999969,-1.56298,-1.95559,-2.3922,-2.88674,-4.0924],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (105.37,'kcal/mol','+|-',2.4),
        S298 = (-1.66614,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(C[O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 212,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C_3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.84046,-4.88716,-5.87111,-5.93572,-5.58846,-5.21453,-4.16357],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (108.176,'kcal/mol','+|-',2.4),
        S298 = (2.98547,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 213,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C_N-3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.1481,-4.74908,-4.6837,-4.44765,-3.97593,-3.9202,-4.36016],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (107.905,'kcal/mol','+|-',2.4),
        S298 = (1.99044,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 214,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   R!H u0 r0 {2,S} {4,S}
4   O   u0 {3,S} {5,S}
5   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.714449,-0.668689,-1.09962,-1.51422,-2.2461,-2.85037,-3.84534],'cal/mol/K','+|-',[2,2.61349,2.52805,2.35814,2,2,2]),
        H298 = (105.975,'kcal/mol','+|-',2.4),
        S298 = (-3.0671,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 215,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-4R!H->C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {6,[S,D,T,B,Q]}
3   R!H u0 r0 {2,S} {4,S}
4   O   u0 r0 {3,S} {5,S}
5   R!H u0 r0 {4,S}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.118777,0.255321,-0.205822,-0.680493,-1.57159,-2.35621,-3.71914],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (106.255,'kcal/mol','+|-',2.4),
        S298 = (-3.30106,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 216,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.03605,-3.38616,-4.20437,-4.59747,-4.75692,-4.98746,-5.42973],'cal/mol/K','+|-',[3.67807,4.56515,5.0924,5.20056,4.9489,4.50832,4.23121]),
        H298 = (88.9444,'kcal/mol','+|-',9.99927),
        S298 = (-1.07324,'cal/mol/K','+|-',8.90355),
    ),
    shortDesc = """Radical correction fitted to 99 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 217,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.03159,-3.40098,-4.22882,-4.62369,-4.77788,-5.00886,-5.45322],'cal/mol/K','+|-',[3.71149,4.60204,5.1265,5.23403,4.98484,4.53877,4.2559]),
        H298 = (89.02,'kcal/mol','+|-',10.0945),
        S298 = (-1.06595,'cal/mol/K','+|-',8.98522),
    ),
    shortDesc = """Radical correction fitted to 98 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 218,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.18435,-4.28566,-4.77994,-4.84961,-4.53259,-4.45301,-4.47002],'cal/mol/K','+|-',[3.84147,5.86931,6.87644,6.88718,5.93462,5.07907,4.30278]),
        H298 = (92.9417,'kcal/mol','+|-',13.9144),
        S298 = (0.347799,'cal/mol/K','+|-',8.97924),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 219,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.68833,-6.74069,-7.43565,-7.43588,-6.67807,-6.08542,-5.20914],'cal/mol/K','+|-',[3.21545,5.3194,6.83814,6.87104,5.25179,3.94494,3]),
        H298 = (93.1334,'kcal/mol','+|-',12.2454),
        S298 = (3.53501,'cal/mol/K','+|-',7.72478),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 220,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H u0 {5,[S,D,T,B,Q]}
7   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.97019,-7.34362,-8.02833,-7.96399,-7.06771,-6.32787,-5.0336],'cal/mol/K','+|-',[3.88933,5.40168,6.60329,6.57273,5.11353,3.78179,3]),
        H298 = (95.1596,'kcal/mol','+|-',13.651),
        S298 = (3.72678,'cal/mol/K','+|-',6.7706),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 221,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O u0 {5,[S,D,T,B,Q]}
7   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.79597,-5.4776,-5.43821,-5.31578,-4.98926,-4.7867,-4.27039],'cal/mol/K','+|-',[6.85164,5.50374,4.16089,3.27353,3,3,3]),
        H298 = (91.5676,'kcal/mol','+|-',9.53135),
        S298 = (1.39496,'cal/mol/K','+|-',3.49881),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 222,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->O_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O   u0 {5,[S,D,T,B,Q]}
7   C   ux {5,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.44185,-2.78333,-3.40131,-3.71327,-3.92621,-4.30142,-3.99352],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.1237,'kcal/mol','+|-',5.2),
        S298 = (-0.317835,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)OC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 223,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C u0 {5,[S,D,T,B,Q]}
7   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.15893,-9.36514,-10.8343,-10.8329,-9.31937,-7.99748,-5.86042],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.978,'kcal/mol','+|-',5.50478),
        S298 = (6.25292,'cal/mol/K','+|-',5.28319),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 224,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-7R!H-R_Ext-8R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   u0 {5,[S,D,T,B,Q]}
7   C   ux {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9   R!H u0 {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.67514,-9.56109,-10.881,-10.7541,-9.06706,-7.65296,-5.43993],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.85,'kcal/mol','+|-',6.50822),
        S298 = (6.14178,'cal/mol/K','+|-',7.4517),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 225,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R",
    group = 
"""
1  * O   u1 r0 {2,S}
2    O   u0 {1,S} {3,S}
3    C   u0 {2,S} {4,[S,D,T,B,Q]}
4    O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5    C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6    C   u0 {5,[S,D,T,B,Q]}
7    C   ux {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
8    R!H ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9    R!H u0 r0 {8,[S,D,T,B,Q]}
10   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.45415,-8.96032,-10.2121,-10.2016,-8.8286,-7.5349,-4.83672],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.549,'kcal/mol','+|-',5.2),
        S298 = (3.50721,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C=O)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 226,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.90727,-8.72602,-11.1262,-11.4402,-9.68461,-8.56448,-8.10811],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.8225,'kcal/mol','+|-',5.2),
        S298 = (9.73306,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1C=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 227,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_N-3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.80808,-4.18351,-4.14907,-4.18923,-4.2595,-4.31013,-4.40829],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (88.5947,'kcal/mol','+|-',2.4),
        S298 = (0.247632,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCOCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 228,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.37549,-2.84783,-3.19848,-3.30672,-3.2496,-3.47375,-3.99744],'cal/mol/K','+|-',[3,3,3.74512,4.04943,4.46026,4.73505,5.21091]),
        H298 = (93.7149,'kcal/mol','+|-',13.8569),
        S298 = (-1.73228,'cal/mol/K','+|-',7.41796),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 229,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S} {7,S}
7   O   u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.80668,-2.23478,-1.77401,-1.44806,-1.05768,-1.26627,-1.95335],'cal/mol/K','+|-',[3.70732,5.67948,4.87846,3,3.79941,6.31111,10.0382]),
        H298 = (98.4271,'kcal/mol','+|-',12.4138),
        S298 = (-3.62296,'cal/mol/K','+|-',11.5908),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 230,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Sp-4O-3R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   O   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S} {7,S}
7   O   u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.62154,-5.01509,-4.16219,-2.24521,0.802262,1.82324,2.9607],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.664,'kcal/mol','+|-',5.2),
        S298 = (-9.29707,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(O)C(=O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 231,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-Sp-4O-3R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   O   ux r0 {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S} {7,S}
7   O   u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.00007,-0.999087,-0.712601,-1.09377,-1.88433,-2.63939,-4.13738],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (96.8857,'kcal/mol','+|-',2.4),
        S298 = (-1.10113,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 232,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H-5C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.62109,-3.1299,-3.50191,-3.59848,-3.45826,-3.57444,-3.81566],'cal/mol/K','+|-',[3,3,3.70198,4.45024,4.73555,4.66386,3.56711]),
        H298 = (86.6026,'kcal/mol','+|-',8.55464),
        S298 = (-2.43977,'cal/mol/K','+|-',8.09905),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 233,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Sp-4O-3R!H",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   O ux {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.52475,-3.48838,-4.16337,-4.40387,-4.35347,-4.50236,-4.53421],'cal/mol/K','+|-',[3.06035,3,3,3,3,3,3]),
        H298 = (87.7759,'kcal/mol','+|-',5.2),
        S298 = (-1.17457,'cal/mol/K','+|-',6.23981),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 234,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Sp-4O-3R!H_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   O   ux {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,S} {7,D}
6   C   ux {5,S}
7   R!H u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.28016,-2.86329,-4.01051,-4.31511,-3.96635,-4.18858,-4.47249],'cal/mol/K','+|-',[3,3,3.39129,3.94312,3.08292,3,3]),
        H298 = (89.6568,'kcal/mol','+|-',5.2),
        S298 = (-3.19608,'cal/mol/K','+|-',6.24675),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 235,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Sp-4O-3R!H_Ext-5C-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   O   ux {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,S} {7,D}
6   C   ux {5,S}
7   R!H u0 r0 {5,D}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.957342,-3.65507,-5.20951,-5.70921,-5.05632,-4.74282,-4.84717],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.0085,'kcal/mol','+|-',5.2),
        S298 = (-0.987524,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 236,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-Sp-4O-3R!H",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   O ux {3,D}
5   C ux {3,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.03055,-1.60636,-0.690716,-0.175555,0.346398,0.369193,-0.761825],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.7485,'kcal/mol','+|-',5.2),
        S298 = (-7.81684,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 237,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   R!H ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.74236,-2.9682,-3.91296,-4.36765,-4.66803,-5.03743,-5.78513],'cal/mol/K','+|-',[3,3,3.6603,3.86981,3,3,3]),
        H298 = (97.8813,'kcal/mol','+|-',5.2),
        S298 = (0.587477,'cal/mol/K','+|-',3.51748),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 238,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   R!H ux {5,[B,D,T,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.95575,-4.56842,-6.42752,-7.07049,-6.59066,-6.21866,-6.75895],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.6373,'kcal/mol','+|-',5.2),
        S298 = (2.00045,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#CC(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 239,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_Sp-4O-3R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   O   ux {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   R!H ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9051,-2.78516,-3.66586,-3.84381,-3.8149,-4.47109,-5.49339],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.9603,'kcal/mol','+|-',5.2),
        S298 = (-1.7799,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 240,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-4O-3R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   O   ux {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   R!H ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57518,-2.33834,-2.90519,-3.3992,-4.19269,-4.76414,-5.48199],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.7685,'kcal/mol','+|-',2.4),
        S298 = (1.01166,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 241,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_N-5R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   O                      u0 r0 {1,S} {3,S}
3   C                      u0 {2,S} {4,[S,D,T,B,Q]} {5,S}
4   O                      u0 {3,[S,D,T,B,Q]}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.790431,0.704796,0.285743,0.0482161,-0.508576,-1.4306,-3.47376],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.6536,'kcal/mol','+|-',5.2),
        S298 = (-3.40966,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 242,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.75949,-3.19216,-4.09874,-4.57037,-4.83578,-5.14006,-5.68529],'cal/mol/K','+|-',[3.4936,4.19948,4.65435,4.82799,4.78186,4.4055,4.14378]),
        H298 = (87.9886,'kcal/mol','+|-',7.83064),
        S298 = (-1.39965,'cal/mol/K','+|-',8.92714),
    ),
    shortDesc = """Radical correction fitted to 81 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 243,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.29452,-4.16334,-5.29105,-5.71972,-5.67819,-5.86077,-7.0732],'cal/mol/K','+|-',[3,3,3.23311,3.62102,3.4873,3.27584,5.20406]),
        H298 = (87.3906,'kcal/mol','+|-',12.5863),
        S298 = (-0.406162,'cal/mol/K','+|-',7.03803),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 244,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.35912,-4.13852,-5.20157,-5.62051,-5.54218,-5.70807,-7.61461],'cal/mol/K','+|-',[3,3,3.02777,3.4411,3,3,5.51211]),
        H298 = (86.8548,'kcal/mol','+|-',5.2),
        S298 = (-1.21907,'cal/mol/K','+|-',6.13063),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 245,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.57485,-4.33395,-5.37172,-5.78836,-5.66556,-5.76958,-7.78217],'cal/mol/K','+|-',[3,3,3,3.21415,3,3,5.48146]),
        H298 = (86.8243,'kcal/mol','+|-',5.2),
        S298 = (-1.07013,'cal/mol/K','+|-',6.17839),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 246,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S}
5   O u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.90028,-5.40563,-7.6343,-8.24488,-7.4676,-7.11671,-8.2222],'cal/mol/K','+|-',[3,3,4.12734,4.59542,3.64875,3.10202,6.04982]),
        H298 = (90.0879,'kcal/mol','+|-',5.2),
        S298 = (2.32627,'cal/mol/K','+|-',3.37776),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 247,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_6R!H->C_3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S}
5   O u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53935,-4.57681,-6.17507,-6.62015,-6.17757,-6.01998,-6.08326],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.7293,'kcal/mol','+|-',5.2),
        S298 = (1.13205,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CC(C)(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 248,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_6R!H->C_N-3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S}
5   O u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26121,-6.23445,-9.09354,-9.8696,-8.75763,-8.21344,-10.3611],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.4465,'kcal/mol','+|-',5.2),
        S298 = (3.52048,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 249,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.66189,-4.19567,-5.07978,-5.47139,-5.43304,-5.59575,-7.7254],'cal/mol/K','+|-',[3,3,3,3,3,3,5.62784]),
        H298 = (86.5042,'kcal/mol','+|-',5.2),
        S298 = (-1.50837,'cal/mol/K','+|-',5.95883),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 250,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.72976,-4.24083,-5.08286,-5.46645,-5.42424,-5.57043,-7.76563],'cal/mol/K','+|-',[3,3,3,3,3,3,5.83417]),
        H298 = (86.3331,'kcal/mol','+|-',5.2),
        S298 = (-1.61281,'cal/mol/K','+|-',6.12663),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 251,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.70761,-4.31034,-5.12676,-5.47072,-5.4611,-5.60833,-7.28257],'cal/mol/K','+|-',[3,3,3,3,3,3,6.2025]),
        H298 = (86.1669,'kcal/mol','+|-',5.2),
        S298 = (-0.977631,'cal/mol/K','+|-',5.82226),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 252,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Int-8R!H-3R!H",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {8,S}
4   C u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]} {6,S}
6   O u0 {5,S} {7,S}
7   C u0 {6,S} {8,[S,D,T,B,Q]}
8   C ux {3,S} {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.87764,-4.83659,-5.68251,-5.99208,-5.91901,-5.71979,-6.45661],'cal/mol/K','+|-',[3,3,3,4.36058,4.78703,4.60787,9.03522]),
        H298 = (85.8366,'kcal/mol','+|-',5.2),
        S298 = (1.14524,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 253,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Int-8R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {8,S} {9,[S,D,T,B,Q]}
4   C   u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]} {6,S}
6   O   u0 r1 {5,S} {7,S}
7   C   u0 r1 {6,S} {8,[S,D,T,B,Q]}
8   C   ux r1 {3,S} {7,[S,D,T,B,Q]}
9   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.12375,-4.814,-5.11752,-5.04335,-4.87749,-4.71725,-4.49081],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (86.264,'kcal/mol','+|-',2.4),
        S298 = (1.26678,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1COOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 254,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Ext-7R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,S}
5   O   u0 r1 {4,S} {6,S}
6   O   u0 {5,S} {7,S}
7   C   u0 {6,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
9   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.67654,-4.62503,-5.88173,-6.4967,-6.273,-6.36995,-10.3472],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.9021,'kcal/mol','+|-',5.2),
        S298 = (-1.77654,'cal/mol/K','+|-',5.49461),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 255,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Ext-7R!H-R_3R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,S}
5   O   u0 r1 {4,S} {6,S}
6   O   u0 {5,S} {7,S}
7   C   u0 {6,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
9   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.41837,-4.489,-5.83138,-6.50156,-6.25713,-6.3126,-10.4561],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.7888,'kcal/mol','+|-',5.2),
        S298 = (-2.7968,'cal/mol/K','+|-',4.50597),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 256,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Ext-7R!H-R_3R!H-inRing_Ext-3R!H-R",
    group = 
"""
1  * O   u1 r0 {2,S}
2    O   u0 {1,S} {3,S}
3    C   u0 r1 {2,S} {4,S} {10,S}
4    C   u0 r1 {3,S} {5,S}
5    O   u0 r1 {4,S} {6,S}
6    O   u0 {5,S} {7,S}
7    C   u0 {6,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8    R!H ux {7,[S,D,T,B,Q]}
9    R!H ux {7,[S,D,T,B,Q]}
10   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.72878,-4.85967,-6.14621,-6.76005,-6.39085,-6.44051,-10.5014],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.9263,'kcal/mol','+|-',5.2),
        S298 = (-2.98284,'cal/mol/K','+|-',6.3069),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 257,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Ext-7R!H-R_3R!H-inRing_Ext-3R!H-R_Ext-10R!H-R",
    group = 
"""
1  * O   u1 r0 {2,S}
2    O   u0 r0 {1,S} {3,S}
3    C   u0 r1 {2,S} {4,S} {10,S}
4    C   u0 r1 {3,S} {5,S}
5    O   u0 r1 {4,S} {6,S}
6    O   u0 r1 {5,S} {7,S}
7    C   u0 r1 {6,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8    R!H ux {7,[S,D,T,B,Q]}
9    R!H ux {7,[S,D,T,B,Q]}
10   C   u0 r0 {3,S} {11,[S,D,T,B,Q]}
11   R!H ux {10,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.73759,-4.12785,-5.57471,-6.33927,-6.13763,-6.44275,-10.6903],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.8091,'kcal/mol','+|-',5.2),
        S298 = (-5.21267,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 258,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Ext-7R!H-R_N-3R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,S}
5   O   u0 r1 {4,S} {6,S}
6   O   u0 r1 {5,S} {7,S}
7   C   u0 r1 {6,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
9   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.45105,-5.03312,-6.03277,-6.48211,-6.32062,-6.54202,-10.0205],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.2421,'kcal/mol','+|-',5.2),
        S298 = (1.28423,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1CC(C)(CO[O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 259,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Int-8R!H-4BrCClFINPSSi_Sp-8R!H-4BrCClFINPSSi",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {8,S}
5   O ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {4,S} {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.61188,-3.72891,-4.15949,-4.27023,-4.55222,-5.0669,-5.26805],'cal/mol/K','+|-',[4.56762,3,3,3,3,3,4.04424]),
        H298 = (87.1486,'kcal/mol','+|-',5.2),
        S298 = (-0.819722,'cal/mol/K','+|-',8.83589),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 260,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Int-8R!H-4BrCClFINPSSi_Sp-8R!H-4BrCClFINPSSi_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {8,S} {9,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C   ux r1 {4,S} {7,[S,D,T,B,Q]}
9   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.375867,-2.7235,-4.02256,-4.5037,-5.41535,-6.45776,-7.24785],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.341,'kcal/mol','+|-',5.2),
        S298 = (-5.1452,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 261,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Int-8R!H-4BrCClFINPSSi_N-Sp-8R!H-4BrCClFINPSSi",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 r1 {3,S} {5,S} {8,[B,D,T,Q]}
5   O u0 r1 {4,S} {6,S}
6   O u0 r1 {5,S} {7,S}
7   C u0 r1 {6,S} {8,S}
8   C u0 r1 {4,[B,D,T,Q]} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59043,-3.23094,-3.44428,-3.57401,-3.67914,-3.95927,-4.25569],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.516,'kcal/mol','+|-',5.2),
        S298 = (-5.19451,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 262,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-8R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
8   C   ux {3,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9   R!H ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.18087,-3.45279,-4.45952,-4.99069,-4.78902,-5.01526,-9.46686],'cal/mol/K','+|-',[4.09287,3,3,3,3,3.27503,3]),
        H298 = (87.4294,'kcal/mol','+|-',5.2),
        S298 = (-5.63527,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 263,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-8R!H-R",
    group = 
"""
1  * O   u1 r0 {2,[S,D,T,B,Q]}
2    O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3    C   ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4    C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5    O   ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6    O   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C   ux r1 {6,[S,D,T,B,Q]}
8    C   ux {3,[S,D,T,B,Q]} {9,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
9    R!H ux {8,[S,D,T,B,Q]}
10   R!H ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.733818,-2.92971,-4.64945,-5.62882,-5.71626,-6.17316,-10.5127],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.9923,'kcal/mol','+|-',5.2),
        S298 = (-6.20774,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(OO)C1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 264,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_N-5O-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   O ux r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.41616,-0.718612,-2.22385,-2.68317,-3.38292,-4.63175,-4.68217],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.5371,'kcal/mol','+|-',5.2),
        S298 = (-3.82554,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 265,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.16173,-4.21436,-5.47499,-5.92364,-5.95778,-6.17466,-5.96031],'cal/mol/K','+|-',[3,3.38755,3.79826,4.16736,4.56122,4.54263,3.92733]),
        H298 = (88.7831,'kcal/mol','+|-',23.4869),
        S298 = (1.26481,'cal/mol/K','+|-',7.95922),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 266,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.87855,-3.74452,-4.94695,-5.31332,-5.27104,-5.52154,-5.33436],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.7652,'kcal/mol','+|-',16.2655),
        S298 = (-0.0165797,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 267,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.45361,-3.38674,-4.65028,-5.11882,-5.18672,-5.58502,-5.41455],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.7247,'kcal/mol','+|-',6.40531),
        S298 = (-0.290527,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 268,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi_Ext-5BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C   u0 {4,S} {6,S}
6   R!H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.33361,-3.42863,-4.79762,-5.24851,-5.30168,-5.72654,-5.43488],'cal/mol/K','+|-',[3,3,3,3,3,3.137,3]),
        H298 = (87.3993,'kcal/mol','+|-',6.93609),
        S298 = (-0.00341809,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 269,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi_Ext-5BrCClFINPSSi-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C u0 r1 {4,S} {6,S}
6   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.14948,-3.31054,-4.60799,-4.88145,-4.81162,-5.08355,-5.10704],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.9091,'kcal/mol','+|-',5.2),
        S298 = (-0.406361,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=CC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]OC1C=CCCC1C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]OC1CC1C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 270,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi_Ext-5BrCClFINPSSi-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   O                      u0 {1,S} {3,S}
3   C                      u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C                      ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C                      u0 r1 {4,S} {6,S}
6   [F,I,P,Br,Cl,O,Si,S,N] u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07013,-3.90098,-5.55615,-6.71675,-7.26191,-8.29849,-6.74624],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.3604,'kcal/mol','+|-',5.2),
        S298 = (1.60836,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1CCOC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 271,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_N-Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.15337,-4.81788,-5.83695,-5.89681,-5.52402,-5.33109,-5.09378],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.887,'kcal/mol','+|-',8.92094),
        S298 = (0.805264,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 272,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_N-Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi_Ext-5BrCClFINPSSi-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5BrCClFINPSSi_Int-7R!H-6R!H_Int-7R!H-3R!H_Ext-7R!H-R_Int-7R!H-6R!H_Ext-6R!H-R_Ext-8R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C   u0 r1 {4,D} {6,S}
6   O   u0 r0 {5,S}
7   C   ux r1 {3,[S,D,T,B,Q]} {8,D}
8   C   u0 r1 {7,D} {9,[S,D,T,B,Q]}
9   R!H ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.769,-5.72167,-6.75537,-6.53559,-5.69945,-5.23101,-4.87452],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.041,'kcal/mol','+|-',5.2),
        S298 = (1.00689,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1C=C(O)C(O)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 273,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_N-3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.42714,-7.97303,-9.69928,-10.8062,-11.4517,-11.3996,-10.9679],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (64.9266,'kcal/mol','+|-',5.2),
        S298 = (11.5159,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 274,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.55227,-2.816,-3.63693,-4.12519,-4.50949,-4.86091,-5.14772],'cal/mol/K','+|-',[3.66815,4.44072,4.81469,4.96951,5.07723,4.68055,3.08388]),
        H298 = (88.1776,'kcal/mol','+|-',5.70038),
        S298 = (-1.78445,'cal/mol/K','+|-',9.50799),
    ),
    shortDesc = """Radical correction fitted to 56 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 275,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,D}
4   C ux r0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.40201,-1.81143,-2.01309,-2.49419,-2.95935,-3.22679,-3.82027],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.252,'kcal/mol','+|-',5.2),
        S298 = (-4.4783,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 276,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   C ux r0 {3,D}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.28989,-1.58161,-1.74342,-2.23763,-2.75086,-3.05504,-3.63798],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.0441,'kcal/mol','+|-',5.2),
        S298 = (-4.54758,'cal/mol/K','+|-',3.10517),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 277,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.66195,-2.29116,-2.41078,-3.05715,-3.50564,-3.60464,-3.79038],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.9813,'kcal/mol','+|-',5.2),
        S298 = (-3.83099,'cal/mol/K','+|-',3.2738),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 278,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,D} {5,S}
4   C   u0 r0 {3,D}
5   C   u0 {3,S} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.44133,-1.90749,-2.25504,-2.57395,-3.07183,-3.22494,-3.41054],'cal/mol/K','+|-',[3.19372,3.4594,3,3,3,3,3]),
        H298 = (86.5367,'kcal/mol','+|-',5.2),
        S298 = (-4.55968,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 279,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,D} {5,S}
4   C   u0 r0 {3,D} {7,[S,D,T,B,Q]}
5   C   u0 r0 {3,S} {6,D}
6   R!H ux {5,D}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.57048,-3.13057,-3.15148,-3.23881,-3.47994,-3.32743,-2.58027],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.8569,'kcal/mol','+|-',5.2),
        S298 = (-3.51733,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 280,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,D} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H u0 r0 {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.1032,-3.0585,-2.72228,-4.02355,-4.37324,-4.36405,-4.55006],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.8706,'kcal/mol','+|-',5.2),
        S298 = (-2.37362,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#CC(=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 281,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.56677,-2.91297,-3.79367,-4.28263,-4.65912,-5.01864,-5.27586],'cal/mol/K','+|-',[3.80896,4.54468,4.88578,5.04041,5.18168,4.76074,3.07662]),
        H298 = (88.3561,'kcal/mol','+|-',5.80405),
        S298 = (-1.52442,'cal/mol/K','+|-',9.7783),
    ),
    shortDesc = """Radical correction fitted to 51 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 282,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.741545,-2.14288,-3.21708,-3.83111,-4.4232,-4.94596,-5.35121],'cal/mol/K','+|-',[3,3,3.37102,4.053,5.13449,5.19992,3.80296]),
        H298 = (88.1228,'kcal/mol','+|-',6.79613),
        S298 = (-3.08415,'cal/mol/K','+|-',9.03285),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 283,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.1809,-2.37706,-3.15303,-3.38018,-3.59769,-3.97305,-4.49866],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.0193,'kcal/mol','+|-',7.72387),
        S298 = (-4.17858,'cal/mol/K','+|-',6.11417),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 284,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   u0 r0 {3,S}
5   C   u0 r0 {3,S} {6,D}
6   R!H ux {5,D} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.43644,-4.03565,-4.54616,-3.85967,-2.39381,-1.93795,-2.5536],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.588,'kcal/mol','+|-',5.2),
        S298 = (-3.29675,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 285,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux {5,D}
7   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.55959,-2.891,-3.69192,-4.01021,-4.34324,-4.72375,-5.41046],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.9885,'kcal/mol','+|-',5.2),
        S298 = (-3.60831,'cal/mol/K','+|-',8.14187),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 286,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-8R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,D} {8,S}
6   C   ux {5,D}
7   C   ux {3,[S,D,T,B,Q]}
8   C   u0 r0 {5,S} {9,[S,D,T,B,Q]}
9   R!H ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.03031,-3.14698,-3.77577,-3.94807,-4.22013,-4.81386,-4.99549],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (86.7053,'kcal/mol','+|-',2.4),
        S298 = (0.0128487,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 287,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r0 {3,S} {8,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   C   ux {5,D}
7   C   ux {3,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.630528,-1.972,-2.81149,-3.19531,-3.6052,-3.93815,-5.28011],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.6739,'kcal/mol','+|-',5.2),
        S298 = (-7.49381,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 288,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06932,-1.93055,-2.58893,-2.80481,-3.11706,-3.54949,-4.09396],'cal/mol/K','+|-',[4.28509,3.18086,3,3,3,3,3]),
        H298 = (89.7942,'kcal/mol','+|-',7.56574),
        S298 = (-4.12145,'cal/mol/K','+|-',6.67287),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 289,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,D} {7,[S,D,T,B,Q]}
6   C   ux {5,D}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.82556,-2.32312,-2.75554,-2.86265,-3.04374,-3.37122,-3.92058],'cal/mol/K','+|-',[4.67249,3.89672,3.07553,3.09864,3.06615,3,3]),
        H298 = (89.7071,'kcal/mol','+|-',10.0748),
        S298 = (-3.4695,'cal/mol/K','+|-',8.59355),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 290,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_7R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,D} {7,S}
6   C ux {5,D}
7   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.47593,-3.70958,-3.86471,-3.99007,-4.1702,-4.28366,-4.44155],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (87.5713,'kcal/mol','+|-',2.4),
        S298 = (-0.338776,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 291,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_N-7R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {5,S}
4   C u0 r0 {3,S}
5   C u0 {3,S} {6,D} {7,[S,D,T,B,Q]}
6   C u0 {5,D}
7   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0311077,-0.763358,-1.50773,-1.59431,-1.77648,-2.34471,-3.33449],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.7204,'kcal/mol','+|-',5.32112),
        S298 = (-6.99156,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 292,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_N-7R!H->C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,S}
4   C   u0 r0 {3,S} {8,[S,D,T,B,Q]}
5   C   u0 r0 {3,S} {6,D} {7,[S,D,T,B,Q]}
6   C   u0 r0 {5,D}
7   O   ux {5,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.774054,-0.200137,-1.16254,-1.33401,-1.68644,-2.34493,-3.39197],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.6017,'kcal/mol','+|-',5.2),
        S298 = (-7.6704,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(O[O])C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 293,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   O ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.332149,-1.85504,-2.92082,-3.3165,-3.69558,-4.22013,-4.39451],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.1495,'kcal/mol','+|-',5.2),
        S298 = (-5.5895,'cal/mol/K','+|-',4.16103),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 294,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,D} {7,S}
6   O   ux {5,D}
7   R!H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.506658,-1.92836,-2.86385,-3.13645,-3.32251,-3.76541,-3.95267],'cal/mol/K','+|-',[3,3,3.24361,3.53241,3.52987,3,3]),
        H298 = (87.6136,'kcal/mol','+|-',5.2),
        S298 = (-5.27121,'cal/mol/K','+|-',5.67424),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 295,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-5R!H-R_7R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,D} {7,S}
6   O ux {5,D}
7   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0588543,-0.949183,-1.71706,-1.88755,-2.07451,-2.7407,-3.40755],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.8761,'kcal/mol','+|-',5.2),
        S298 = (-7.27735,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O[O])C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 296,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-5R!H-R_N-7R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C                      ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C                      ux r0 {3,S}
5   C                      ux {3,[S,D,T,B,Q]} {6,D} {7,S}
6   O                      ux {5,D}
7   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.954462,-2.90754,-4.01064,-4.38535,-4.57051,-4.79012,-4.49779],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.3511,'kcal/mol','+|-',5.2),
        S298 = (-3.26506,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 297,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.271886,-1.89255,-3.28554,-4.31314,-5.30563,-5.98597,-6.26255],'cal/mol/K','+|-',[3,3.29329,4.35356,5.2968,6.66062,6.59205,4.42693]),
        H298 = (87.2674,'kcal/mol','+|-',5.80594),
        S298 = (-1.91424,'cal/mol/K','+|-',11.2295),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 298,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,T,Q,B]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.225794,-1.03374,-1.87831,-2.36722,-2.60267,-3.26629,-4.56105],'cal/mol/K','+|-',[3.00811,4.25532,4.74095,5.13268,5.30974,4.91803,3.41434]),
        H298 = (84.5467,'kcal/mol','+|-',5.2),
        S298 = (-6.71457,'cal/mol/K','+|-',10.1884),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 299,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   u0 r0 {3,S}
5   C   u0 {3,S} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C   ux {5,[S,T,Q,B]} {8,S}
7   C   ux {5,[S,D,T,B,Q]}
8   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.322499,0.505152,0.214173,-0.0545604,-0.33077,-1.15586,-3.31624],'cal/mol/K','+|-',[4.91634,4.97711,3.79763,3,3,3,3]),
        H298 = (85.4332,'kcal/mol','+|-',5.2),
        S298 = (-11.0127,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 300,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   u0 r0 {3,S} {9,[S,D,T,B,Q]}
5   C   u0 r0 {3,S} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C   ux {5,[S,T,Q,B]} {8,S}
7   C   ux {5,[S,D,T,B,Q]}
8   R!H u0 r0 {6,S}
9   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.06069,2.26483,1.55684,0.971437,0.51107,-0.378144,-3.22998],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.6638,'kcal/mol','+|-',5.2),
        S298 = (-11.2477,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 301,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C   ux {5,[S,T,Q,B]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0329,-2.85119,-4.11442,-4.94259,-5.37734,-5.82968,-6.41491],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.4173,'kcal/mol','+|-',5.2),
        S298 = (-1.20078,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 302,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   O   ux {5,[S,T,Q,B]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.291832,-0.476633,-1.59107,-1.84181,-1.59712,-2.36038,-3.34297],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.0324,'kcal/mol','+|-',5.2),
        S298 = (-9.14592,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(O[O])C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 303,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.199601,-2.60244,-4.42365,-5.77569,-7.1132,-7.90803,-7.65089],'cal/mol/K','+|-',[3,3,4.23772,5.26041,6.91661,6.85025,4.65418]),
        H298 = (88.9671,'kcal/mol','+|-',6.4778),
        S298 = (0.554002,'cal/mol/K','+|-',10.2234),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 304,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_Ext-6O-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O   ux {5,[S,T,Q,B]} {7,S}
7   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.319786,-2.96254,-4.9012,-6.31266,-7.7153,-8.51238,-8.08004],'cal/mol/K','+|-',[3,3,3.89216,5.05685,7.00094,6.90915,4.63523]),
        H298 = (89.2497,'kcal/mol','+|-',6.85463),
        S298 = (1.42325,'cal/mol/K','+|-',10.4101),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 305,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_Ext-6O-R_7R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O ux {5,[S,T,Q,B]} {7,S}
7   C u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.833368,-3.71165,-5.82067,-7.39783,-9.15223,-9.82404,-8.89243],'cal/mol/K','+|-',[3,3,4.36852,6.28117,8.97599,9.25295,6.43142]),
        H298 = (90.0993,'kcal/mol','+|-',8.06056),
        S298 = (3.93417,'cal/mol/K','+|-',11.4941),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 306,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_Ext-6O-R_7R!H->C_Ext-7C-R_Ext-7C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O   ux {5,[S,T,Q,B]} {7,S}
7   C   u0 r0 {6,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
9   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.51422,-2.84335,-3.68212,-4.32297,-4.75817,-5.29439,-5.74402],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.1341,'kcal/mol','+|-',5.2),
        S298 = (-1.69262,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 307,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_Ext-6O-R_N-7R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C                      ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C                      ux r0 {3,S}
5   C                      ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O                      ux {5,[S,T,Q,B]} {7,S}
7   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.514785,-1.74524,-3.40707,-4.54927,-5.38027,-6.38094,-6.75991],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.9533,'kcal/mol','+|-',5.2),
        S298 = (-2.65699,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 308,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {5,S}
4   C u0 r0 {3,S}
5   C u0 {3,S} {6,S}
6   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.481804,-1.84861,-3.26182,-4.49424,-5.98795,-6.47384,-6.21036],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.4446,'kcal/mol','+|-',5.2),
        S298 = (0.724253,'cal/mol/K','+|-',4.87266),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 309,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,S}
4   C   u0 r0 {3,S} {7,[S,D,T,B,Q]}
5   C   u0 r0 {3,S} {6,S}
6   C   u0 r0 {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.743043,-2.25085,-3.53076,-4.41553,-5.01732,-5.60029,-6.00814],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.9008,'kcal/mol','+|-',5.2),
        S298 = (-1.66109,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 310,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.27609,-3.64308,-4.39123,-4.77923,-4.94785,-5.1641,-5.27791],'cal/mol/K','+|-',[4.27256,5.45301,5.93356,5.87349,5.44121,4.56327,3]),
        H298 = (88.8442,'kcal/mol','+|-',5.2),
        S298 = (-0.0830454,'cal/mol/K','+|-',10.0869),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 311,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D}
5   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.87643,-3.09081,-3.80215,-4.23369,-4.47598,-4.81284,-5.11282],'cal/mol/K','+|-',[4.81496,5.74056,5.82473,5.62132,5.14913,4.33763,3]),
        H298 = (89.6456,'kcal/mol','+|-',5.2),
        S298 = (-1.16115,'cal/mol/K','+|-',10.5517),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 312,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.37838,-2.11697,-2.6101,-3.01696,-3.34144,-3.9419,-4.78707],'cal/mol/K','+|-',[5.57468,6.11764,5.78289,5.42601,4.76665,4.09046,3]),
        H298 = (89.2056,'kcal/mol','+|-',5.98109),
        S298 = (-3.8866,'cal/mol/K','+|-',7.85171),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 313,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D}
5   C   ux {4,D} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.3096,-3.00838,-3.27848,-3.52177,-3.60454,-4.04136,-4.85955],'cal/mol/K','+|-',[3.66804,4.17494,4.63523,4.68618,4.53948,4.05435,3]),
        H298 = (89.881,'kcal/mol','+|-',5.55236),
        S298 = (-3.45907,'cal/mol/K','+|-',6.44469),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 314,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D}
5   C   ux {4,D} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.88523,-2.5684,-2.83397,-3.07959,-3.15903,-3.63556,-4.61918],'cal/mol/K','+|-',[3.60793,4.22885,4.80124,4.87192,4.68523,4.1677,3]),
        H298 = (90.5534,'kcal/mol','+|-',5.39873),
        S298 = (-4.00455,'cal/mol/K','+|-',6.73062),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 315,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {8,[S,D,T,B,Q]}
5   C   ux {4,D} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.52049,-2.45131,-2.82365,-3.06053,-3.08091,-3.58223,-4.67991],'cal/mol/K','+|-',[6.21187,6.80053,7.24111,7.02276,6.2928,5.33171,3.01846]),
        H298 = (91.6886,'kcal/mol','+|-',5.2),
        S298 = (-5.66338,'cal/mol/K','+|-',7.0276),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 316,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {8,S}
5   C   ux {4,D} {6,S} {9,[S,D,T,B,Q]}
6   R!H u0 r0 {5,S} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
8   R!H u0 r0 {4,S}
9   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.95386,-6.36153,-6.85489,-6.88024,-6.42557,-6.31452,-6.23911],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.6638,'kcal/mol','+|-',5.2),
        S298 = (-1.61316,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 317,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R_6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {8,[S,D,T,B,Q]}
5   C   ux {4,D} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.701454,-0.1889,0.151278,0.0270889,-0.179857,-0.98819,-3.22618],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.4179,'kcal/mol','+|-',5.2),
        S298 = (-7.89731,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 318,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R_N-6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {8,[S,D,T,B,Q]}
5   C   ux {4,D} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09385,-0.803503,-1.76735,-2.32843,-2.63729,-3.44397,-4.57444],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.9841,'kcal/mol','+|-',5.2),
        S298 = (-7.47965,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 319,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D}
5   C   ux {4,D} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72038,-0.512763,0.301304,0.480068,0.614983,-0.122805,-2.76762],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.4902,'kcal/mol','+|-',5.2),
        S298 = (-8.17218,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(O)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 320,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D}
5   C   ux {4,D} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77988,-2.76409,-3.29097,-3.77666,-4.16037,-4.68137,-5.20208],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.0924,'kcal/mol','+|-',8.40473),
        S298 = (-1.77923,'cal/mol/K','+|-',4.00285),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 321,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_6R!H->C_Sp-6C-5C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,D}
5   C   u0 r0 {4,D} {6,S}
6   C   u0 r0 {5,S} {7,[S,D,T,B,Q]}
7   R!H u0 r0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.34933,-3.13688,-3.47632,-3.80652,-4.04169,-4.47067,-5.02338],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.6536,'kcal/mol','+|-',5.2),
        S298 = (0.307825,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 322,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_6R!H->C_N-Sp-6C-5C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D}
5   C   ux {4,D} {6,D}
6   C   ux {5,D} {7,D}
7   R!H ux {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.49516,-2.5777,-3.19829,-3.76173,-4.2197,-4.78672,-5.29143],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.3118,'kcal/mol','+|-',10.2759),
        S298 = (-2.82275,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 323,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_6R!H->C_N-Sp-6C-5C_7R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D}
5   C ux {4,D} {6,D}
6   C ux {5,D} {7,D}
7   C ux {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6676,-2.94515,-3.64141,-4.2193,-4.61709,-5.10384,-5.44783],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.6787,'kcal/mol','+|-',5.2),
        S298 = (-1.96318,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 324,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_6R!H->C_N-Sp-6C-5C_N-7R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D}
5   C ux {4,D} {6,D}
6   C ux {5,D} {7,D}
7   O ux {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32272,-2.21025,-2.75517,-3.30417,-3.82232,-4.4696,-5.13502],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.9448,'kcal/mol','+|-',5.2),
        S298 = (-3.68232,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 325,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D}
5   C   ux {4,D} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.46033,-4.38822,-4.62922,-4.60526,-4.16342,-4.17087,-4.53984],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.594,'kcal/mol','+|-',5.2),
        S298 = (-1.53639,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 326,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {7,[S,D,T,B,Q]}
5   C   ux {4,D} {6,S}
6   C   ux {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.62705,-4.46897,-4.83557,-5.12836,-5.3109,-5.64145,-5.83321],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.5625,'kcal/mol','+|-',5.2),
        S298 = (-2.34319,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 327,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   C   ux {4,D}
6   C   ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.53455,5.17079,3.63173,2.35873,0.419856,-1.39107,-4.43959],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.7344,'kcal/mol','+|-',5.2),
        S298 = (-11.7302,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(CO[O])C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 328,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.48942,-4.28939,-5.26929,-5.7312,-5.87234,-5.88478,-5.51373],'cal/mol/K','+|-',[3.62596,4.4734,4.65455,4.51948,4.39231,3.86595,3]),
        H298 = (89.9547,'kcal/mol','+|-',5.2),
        S298 = (2.19324,'cal/mol/K','+|-',10.0323),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 329,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   O   ux {4,D}
6   R!H ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97384,-3.66985,-4.65024,-5.18105,-5.3613,-5.46927,-5.33946],'cal/mol/K','+|-',[3.46677,4.33155,4.58731,4.60064,4.5332,4.07315,3]),
        H298 = (89.4477,'kcal/mol','+|-',5.2),
        S298 = (1.2703,'cal/mol/K','+|-',10.8974),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 330,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   O u0 {4,D}
6   C ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O u0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.02576,-4.1124,-5.25399,-5.83945,-6.08689,-6.15466,-5.81891],'cal/mol/K','+|-',[3.12722,3.6446,3.55525,3.32901,3,3,3]),
        H298 = (90.0898,'kcal/mol','+|-',5.2),
        S298 = (3.14016,'cal/mol/K','+|-',6.34112),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 331,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_7R!H->O_Ext-7O-R",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   O u0 {4,D}
6   C ux {4,[S,D,T,B,Q]} {7,S}
7   O u0 {6,S} {8,S}
8   O u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.14795,-3.78724,-4.5225,-5.00625,-5.41496,-5.75345,-5.80658],'cal/mol/K','+|-',[4.92111,5.56167,4.41165,3.44952,3.12525,3,3]),
        H298 = (89.5051,'kcal/mol','+|-',5.44337),
        S298 = (2.77461,'cal/mol/K','+|-',9.89519),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 332,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   O   u0 r0 {4,D}
6   C   ux {4,[S,D,T,B,Q]} {7,S} {9,[S,D,T,B,Q]}
7   O   u0 r0 {6,S} {8,S}
8   O   u0 r0 {7,S}
9   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.21864,-4.9973,-5.48235,-5.75677,-6.09493,-6.21209,-5.9405],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (90.1811,'kcal/mol','+|-',2.4),
        S298 = (4.92752,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 333,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {6,S}
5   O   ux {4,D}
6   R!H u0 {4,S} {7,S}
7   C   ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83106,-2.45284,-2.98993,-3.37047,-3.36593,-3.58442,-4.02098],'cal/mol/K','+|-',[5.90574,6.74808,6.85385,6.88515,6.84518,6.73583,5.39032]),
        H298 = (86.1127,'kcal/mol','+|-',5.54111),
        S298 = (-3.8718,'cal/mol/K','+|-',15.9551),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 334,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D} {6,S}
5   O ux {4,D}
6   C u0 r0 {4,S} {7,S}
7   C ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.256932,-0.0670303,-0.566724,-0.936203,-0.945791,-1.20294,-2.11522],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.1536,'kcal/mol','+|-',5.2),
        S298 = (-9.51278,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC(=O)CC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 335,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_N-6R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D} {6,S}
5   O ux {4,D}
6   O u0 r0 {4,S} {7,S}
7   C ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.91906,-4.83864,-5.41313,-5.80474,-5.78607,-5.9659,-5.92675],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.0718,'kcal/mol','+|-',5.2),
        S298 = (1.76919,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 336,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.08469,-4.76047,-5.58307,-5.88302,-5.90255,-5.87477,-5.61195],'cal/mol/K','+|-',[3,4.35443,5.86743,6.22196,5.96326,5.06026,3]),
        H298 = (87.5552,'kcal/mol','+|-',5.2),
        S298 = (2.09825,'cal/mol/K','+|-',8.03904),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 337,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,[S,T,Q,B]}
5   O ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11974,-2.85748,-3.89106,-4.42717,-4.74559,-5.36685,-5.82479],'cal/mol/K','+|-',[3,3,3,3,3,3.12816,3]),
        H298 = (88.2571,'kcal/mol','+|-',5.2),
        S298 = (-2.07917,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 338,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-5O-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,[S,T,Q,B]}
5   O ux {4,[S,T,Q,B]} {6,S}
6   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57388,-2.6802,-3.30536,-3.70254,-3.75184,-4.26088,-5.36321],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.6644,'kcal/mol','+|-',5.2),
        S298 = (-3.13668,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 339,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-5O-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C                      ux {2,[S,D,T,B,Q]} {4,S}
4   C                      ux r0 {3,S} {5,[S,T,Q,B]}
5   O                      ux {4,[S,T,Q,B]} {6,S}
6   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.665604,-3.03475,-4.47677,-5.1518,-5.73934,-6.47282,-6.28638],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.8497,'kcal/mol','+|-',5.2),
        S298 = (-1.02166,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 340,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,[S,T,Q,B]}
5   C u0 {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.53383,-5.19544,-5.96982,-6.21578,-6.167,-5.99086,-5.5633],'cal/mol/K','+|-',[3,4.44618,6.39786,6.88893,6.62408,5.65815,3]),
        H298 = (87.4679,'kcal/mol','+|-',5.2),
        S298 = (3.05308,'cal/mol/K','+|-',7.66733),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 341,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.72276,-5.507,-6.3335,-6.56847,-6.4766,-6.22319,-5.43728],'cal/mol/K','+|-',[3,4.36393,6.53645,7.13606,6.92826,5.98224,3]),
        H298 = (87.3478,'kcal/mol','+|-',5.2),
        S298 = (3.19375,'cal/mol/K','+|-',8.33763),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 342,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,S} {6,[S,D,T,B,Q]}
5   C   u0 {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.52434,-3.50158,-3.51981,-3.54212,-3.48078,-3.65132,-4.27878],'cal/mol/K','+|-',[3,3,3.60343,4.83609,5.22251,5.20912,3.73316]),
        H298 = (85.2625,'kcal/mol','+|-',5.2),
        S298 = (-0.728131,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 343,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   u0 r0 {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.13985,-4.33882,-5.28382,-5.90956,-6.03738,-6.20137,-6.1063],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.2229,'kcal/mol','+|-',5.2),
        S298 = (0.715605,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 344,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi_Ext-5C-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,S}
5   C u0 r0 {4,S} {6,S}
6   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.70835,-7.82846,-9.9755,-10.435,-9.99513,-9.05073,-6.48438],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (88.9637,'kcal/mol','+|-',2.4),
        S298 = (7.46267,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 345,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi_Ext-5C-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   O                      u0 r0 {1,S} {3,S}
3   C                      u0 r0 {2,S} {4,S}
4   C                      u0 r0 {3,S} {5,S}
5   C                      u0 r0 {4,S} {6,S}
6   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.02377,-6.08225,-6.75572,-7.07332,-7.28537,-7.11055,-6.06356],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (88.2614,'kcal/mol','+|-',2.4),
        S298 = (4.58977,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 346,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_N-Sp-5C-4BrCClFINPSSi",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,T}
5   C u0 r0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.0696,-2.78082,-3.15127,-3.48245,-3.76758,-4.19035,-6.53996],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.2789,'kcal/mol','+|-',5.2),
        S298 = (1.96291,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 347,
    label = "RJ1_N-1R-inRing_N-1R->O",
    group = 
"""
1 * [H,C] u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0855334,-0.812022,-1.46027,-1.93783,-2.56452,-3.07572,-4.02042],'cal/mol/K','+|-',[3.04823,3.37225,3.50822,3.44484,3.12399,3,3.10192]),
        H298 = (95.7086,'kcal/mol','+|-',23.0435),
        S298 = (0.491176,'cal/mol/K','+|-',9.83163),
    ),
    shortDesc = """Radical correction fitted to 250 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 348,
    label = "RJ1_N-1R-inRing_N-1R->O_1CH->H",
    group = 
"""
1 * H u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99274,-1.98515,-1.97951,-1.98202,-2.03209,-2.13435,-2.50693],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.234,'kcal/mol','+|-',2.4),
        S298 = (-5.12703,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[H] - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 349,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H",
    group = 
"""
1 * C u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0744307,-0.805193,-1.45724,-1.93757,-2.56762,-3.0812,-4.02924],'cal/mol/K','+|-',[3.04309,3.37729,3.51755,3.45488,3.13204,3,3.10229]),
        H298 = (95.6478,'kcal/mol','+|-',23.0804),
        S298 = (0.523882,'cal/mol/K','+|-',9.82257),
    ),
    shortDesc = """Radical correction fitted to 249 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 350,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.100506,-0.844836,-1.50213,-1.97624,-2.57617,-3.07432,-4.01574],'cal/mol/K','+|-',[3.11269,3.50919,3.67812,3.62264,3.29081,3.04065,3.24307]),
        H298 = (93.5134,'kcal/mol','+|-',19.5024),
        S298 = (0.292037,'cal/mol/K','+|-',9.54543),
    ),
    shortDesc = """Radical correction fitted to 227 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 351,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.154787,-0.886491,-1.52804,-1.98421,-2.54501,-3.02042,-3.94189],'cal/mol/K','+|-',[3.01029,3.46309,3.69269,3.67343,3.36342,3.10124,3.26843]),
        H298 = (92.7266,'kcal/mol','+|-',19.2859),
        S298 = (0.0950181,'cal/mol/K','+|-',9.75213),
    ),
    shortDesc = """Radical correction fitted to 210 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 352,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,[S,D,T,B,Q]}
3   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.141626,-0.857372,-1.49744,-1.95089,-2.50056,-2.96939,-3.89575],'cal/mol/K','+|-',[3.06058,3.51341,3.75924,3.74147,3.41107,3.13497,3.32625]),
        H298 = (92.2037,'kcal/mol','+|-',19.1602),
        S298 = (-0.0513951,'cal/mol/K','+|-',9.88222),
    ),
    shortDesc = """Radical correction fitted to 201 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 353,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.309131,-0.904343,-1.45113,-1.80185,-2.2419,-2.6091,-3.34776],'cal/mol/K','+|-',[3,3.48281,3.82243,3.85698,3.5716,3.20183,3.39167]),
        H298 = (87.7191,'kcal/mol','+|-',17.3914),
        S298 = (-1.36171,'cal/mol/K','+|-',9.82147),
    ),
    shortDesc = """Radical correction fitted to 118 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 354,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.268811,-0.861282,-1.40074,-1.77227,-2.26915,-2.66661,-3.38489],'cal/mol/K','+|-',[3,3,3.10305,3.1725,3.11379,3,3]),
        H298 = (85.894,'kcal/mol','+|-',14.6602),
        S298 = (-1.13179,'cal/mol/K','+|-',10.0728),
    ),
    shortDesc = """Radical correction fitted to 89 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 355,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.177056,-0.70733,-1.21242,-1.5955,-2.15993,-2.60904,-3.53793],'cal/mol/K','+|-',[3,3.16791,3.72938,3.96397,3.92991,3.4291,3]),
        H298 = (87.9611,'kcal/mol','+|-',9.79666),
        S298 = (-1.11829,'cal/mol/K','+|-',10.7449),
    ),
    shortDesc = """Radical correction fitted to 39 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 356,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.255309,-0.575983,-0.913444,-1.2168,-1.73259,-2.29225,-3.45301],'cal/mol/K','+|-',[3,3.46022,3.73061,3.58594,3.02354,3,3]),
        H298 = (87.8867,'kcal/mol','+|-',7.89713),
        S298 = (-2.18707,'cal/mol/K','+|-',7.51926),
    ),
    shortDesc = """Radical correction fitted to 24 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 357,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.1105,-0.27967,-0.627504,-1.0157,-1.70481,-2.38403,-3.6082],'cal/mol/K','+|-',[3,3,3.12031,3.27302,3.02323,3,3]),
        H298 = (87.6421,'kcal/mol','+|-',7.40796),
        S298 = (-2.00776,'cal/mol/K','+|-',7.62021),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 358,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.13751,-0.00284996,-0.373962,-0.795681,-1.58123,-2.35246,-3.67923],'cal/mol/K','+|-',[3,3,3,3.27882,3.14315,3,3]),
        H298 = (88.2762,'kcal/mol','+|-',7.00984),
        S298 = (-2.7175,'cal/mol/K','+|-',6.87193),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 359,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   u0 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H u0 {4,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3501,3.49167,5.03364,5.71326,5.03367,2.60445,-1.32783],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.6475,'kcal/mol','+|-',5.2),
        S298 = (-15.3746,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(COO)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 360,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.312957,-0.386801,-0.73517,-1.13625,-1.8321,-2.42047,-3.57465],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.361,'kcal/mol','+|-',8.39536),
        S298 = (-3.18625,'cal/mol/K','+|-',4.30802),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 361,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_Sp-6R!H-4C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,S}
5   C   ux {3,[S,D,T,B,Q]}
6   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.590922,-1.06898,-1.55659,-1.86628,-2.38365,-2.80136,-3.83667],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.5135,'kcal/mol','+|-',8.57608),
        S298 = (-2.17541,'cal/mol/K','+|-',3.99681),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 362,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_Sp-6R!H-4C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {4,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.55189,-1.04562,-1.52268,-1.79718,-2.32407,-2.77092,-3.83834],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.9876,'kcal/mol','+|-',9.32009),
        S298 = (-2.02137,'cal/mol/K','+|-',4.70172),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 363,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_Sp-6R!H-4C_Ext-5R!H-R_Sp-7R!H-5R!H",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {7,S}
6   R!H ux {4,S}
7   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00113151,-0.931391,-1.86711,-2.29212,-2.91928,-3.25316,-4.08957],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.8431,'kcal/mol','+|-',5.2),
        S298 = (-2.38127,'cal/mol/K','+|-',7.43362),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 364,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_Sp-6R!H-4C_Ext-5R!H-R_Sp-7R!H-5R!H_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {2,[S,D,T,B,Q]} {6,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {7,S} {8,[S,D,T,B,Q]}
6   R!H ux r1 {4,S}
7   R!H ux r1 {5,S}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.138451,-1.48997,-2.616,-2.86703,-3.46758,-3.6765,-4.15703],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.5606,'kcal/mol','+|-',5.2),
        S298 = (-5.00946,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CC(CC(=C)C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 365,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_Sp-6R!H-4C_Ext-5R!H-R_N-Sp-7R!H-5R!H",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,D} {4,S}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r1 {2,S} {6,S}
5   C   u0 r1 {3,S} {7,[B,D,T,Q]}
6   R!H u0 r1 {4,S}
7   R!H u0 r1 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04347,-1.14715,-1.21653,-1.35722,-1.79499,-2.34226,-3.61504],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (79.9189,'kcal/mol','+|-',2.4),
        S298 = (-1.70146,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CC=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 366,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_N-Sp-6R!H-4C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S} {3,D} {4,S}
3   C u0 {2,D} {5,S}
4   C u0 {2,S} {6,D}
5   C u0 {3,S}
6   C u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.150811,0.011134,-0.256008,-0.71039,-1.51037,-2.19827,-3.42181],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (89.3474,'kcal/mol','+|-',3.93672),
        S298 = (-3.77591,'cal/mol/K','+|-',4.46026),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 367,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_N-Sp-6R!H-4C_Ext-5R!H-R",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S} {3,D} {4,S}
3   C u0 {2,D} {5,S}
4   C u0 {2,S} {6,D}
5   C u0 {3,S} {7,D}
6   C u0 {4,D}
7   C u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00223952,0.0645175,-0.25773,-0.703139,-1.48007,-2.16623,-3.40845],'cal/mol/K','+|-',[2,2.16431,2,2,2,2,2]),
        H298 = (90.1191,'kcal/mol','+|-',2.99249),
        S298 = (-4.43014,'cal/mol/K','+|-',4.42362),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 368,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_N-Sp-6R!H-4C_Ext-5R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D} {4,S}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r1 {2,S} {6,D}
5   C   u0 r1 {3,S} {7,D}
6   C   u0 r1 {4,D}
7   C   u0 r1 {5,D}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0983,-1.18505,-1.28542,-1.43413,-1.83002,-2.29093,-3.35078],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (88.3914,'kcal/mol','+|-',2.4),
        S298 = (-1.87616,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 369,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.671517,0.199897,-0.400668,-0.965518,-1.89302,-2.76148,-4.07326],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.8482,'kcal/mol','+|-',5.2),
        S298 = (-0.734249,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 370,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r0 {2,S} {6,[S,D,T,B,Q]}
5   R!H u0 r0 {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O   u0 r0 {4,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.84419,1.1356,0.14888,-0.485643,-1.3994,-2.05443,-3.05427],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (87.8293,'kcal/mol','+|-',2.4),
        S298 = (-2.03169,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=COC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 371,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_Sp-5R!H-3C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D} {5,S}
4   C   u0 {2,S} {6,[S,D,T,B,Q]}
5   R!H u0 {3,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.482933,0.336369,0.0375434,-0.386805,-1.45383,-2.34274,-3.63366],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (90.3085,'kcal/mol','+|-',2.4),
        S298 = (-0.423994,'cal/mol/K','+|-',3.2372),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 372,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_Sp-5R!H-3C_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D} {5,S}
4   C   u0 r0 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H u0 r0 {3,S}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.788362,0.489339,0.106615,-0.30496,-1.16506,-2.00562,-3.66233],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (90.6599,'kcal/mol','+|-',2.4),
        S298 = (0.720529,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 373,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_N-Sp-5R!H-3C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,D}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   ux {3,D}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0748868,-0.706587,-1.47015,-2.19349,-2.92202,-3.91987,-5.4969],'cal/mol/K','+|-',[4.12956,3.65807,3.02916,3,3,3,3]),
        H298 = (91.5667,'kcal/mol','+|-',5.2),
        S298 = (-0.226555,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 374,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_N-Sp-5R!H-3C_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,D}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux {3,D}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.360904,-1.2084,-2.03029,-2.75255,-3.36002,-4.24826,-5.63357],'cal/mol/K','+|-',[5.43587,4.55184,3.28956,3,3,3,3]),
        H298 = (92.297,'kcal/mol','+|-',5.2),
        S298 = (0.0531904,'cal/mol/K','+|-',3.33206),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 375,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_N-Sp-5R!H-3C_Ext-4C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,D}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   O   ux {3,D}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.56097,0.400918,-0.867256,-1.91517,-2.94345,-4.11182,-5.72512],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.4541,'kcal/mol','+|-',5.2),
        S298 = (-1.12487,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=C=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 376,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux r0 {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.61678,-3.52639,-3.97326,-4.2814,-4.44267,-4.58826,-5.15875],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.3089,'kcal/mol','+|-',5.2),
        S298 = (8.97256,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C(C)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 377,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D} {5,S}
4   C ux {2,[S,D,T,B,Q]}
5   C ux {3,S} {6,S}
6   C ux {5,S} {7,S}
7   O u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32384,-1.76648,-1.93917,-2.09176,-2.35138,-2.69535,-3.22258],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.0533,'kcal/mol','+|-',5.2),
        S298 = (0.623699,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 378,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_3C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D} {5,S}
4   C ux r0 {2,[S,D,T,B,Q]}
5   C ux {3,S} {6,S}
6   C ux {5,S} {7,S}
7   O u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08737,-1.34301,-1.48703,-1.74853,-2.36656,-2.85887,-3.78993],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (87.9254,'kcal/mol','+|-',2.4),
        S298 = (0.618758,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 379,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_N-3C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux r0 {2,D} {5,S}
4   C ux r0 {2,[S,D,T,B,Q]}
5   C ux {3,S} {6,S}
6   C ux {5,S} {7,S}
7   O u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.85588,-2.7193,-2.95651,-2.86403,-2.31723,-2.32741,-1.94603],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.6536,'kcal/mol','+|-',5.2),
        S298 = (0.634814,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)=CCC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 380,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   O   ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.16761,-2.44275,-2.71487,-2.48371,-1.90758,-1.71405,-2.47536],'cal/mol/K','+|-',[3,5.12711,5.47443,4.80144,3.39747,3,3]),
        H298 = (90.6239,'kcal/mol','+|-',11.7538),
        S298 = (-3.31674,'cal/mol/K','+|-',7.32782),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 381,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D} {5,[S,D,T,B,Q]}
4   O ux {2,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.309804,-0.772451,-0.912072,-0.907413,-0.906435,-1.07571,-2.26423],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.2953,'kcal/mol','+|-',5.2),
        S298 = (-5.37848,'cal/mol/K','+|-',4.62684),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 382,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_5R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   u0 {2,D} {5,[S,D,T,B,Q]}
4   O   ux {2,[S,D,T,B,Q]}
5   C   u0 {3,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.63685,-1.26511,-1.22613,-0.799707,-0.0287393,0.21713,-1.05955],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.0705,'kcal/mol','+|-',5.2),
        S298 = (-5.31718,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 383,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_5R!H->C_2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r1 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D} {5,[S,D,T,B,Q]}
4   O ux {2,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.368686,0.338583,0.159212,-0.211944,-1.07224,-1.7382,-2.97946],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.7868,'kcal/mol','+|-',5.2),
        S298 = (-7.72193,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 384,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_5R!H->C_N-2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D} {5,[S,D,T,B,Q]}
4   O ux {2,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.661248,-1.39082,-1.6693,-1.71059,-1.61832,-1.70606,-2.75368],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.0286,'kcal/mol','+|-',5.2),
        S298 = (-3.09631,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(O)=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 385,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_N-5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,D} {4,S}
3   C ux {2,D} {5,S}
4   O u0 {2,S}
5   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.45431,-4.9482,-5.41906,-4.84815,-3.40929,-2.67155,-2.79206],'cal/mol/K','+|-',[3,3.7435,3.8855,3.62112,3.29913,3.2845,3]),
        H298 = (95.6168,'kcal/mol','+|-',13.0193),
        S298 = (-0.22413,'cal/mol/K','+|-',6.66706),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 386,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_N-5R!H->C_Ext-1C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {6,S}
2   C   u0 {1,S} {3,D} {4,S}
3   C   ux {2,D} {5,S}
4   O   u0 {2,S}
5   O   ux {3,S}
6   C   u0 r0 {1,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.52855,-3.62468,-4.04533,-3.56789,-2.24287,-1.51031,-1.97066],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.0138,'kcal/mol','+|-',5.2),
        S298 = (-2.58129,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 387,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r1 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.199026,-0.990439,-1.80063,-2.33584,-3.06524,-3.46872,-3.7156],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.4567,'kcal/mol','+|-',15.7899),
        S298 = (1.83142,'cal/mol/K','+|-',4.89883),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 388,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_2C-inRing_Int-4R!H-3C_Ext-1C-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {5,D}
2   C ux r1 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D}
4   C ux r1 {2,[S,D,T,B,Q]}
5   C u0 r0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.119766,-0.75977,-1.60117,-2.12116,-2.85588,-3.31976,-3.86525],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.4174,'kcal/mol','+|-',2.4),
        S298 = (2.89727,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 389,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_2C-inRing_Int-4R!H-3C_Ext-1C-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {5,D}
2   C                      ux r1 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C                      ux r1 {2,D}
4   C                      ux r1 {2,[S,D,T,B,Q]}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.916307,-1.50944,-2.24943,-2.81889,-3.5363,-3.80388,-3.3789],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.2522,'kcal/mol','+|-',5.2),
        S298 = (-0.566728,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 390,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0249699,-0.908582,-1.68001,-2.18857,-2.81736,-3.06457,-3.66893],'cal/mol/K','+|-',[3,3,3.97758,4.75607,5.31342,4.87011,3.72542]),
        H298 = (86.5679,'kcal/mol','+|-',10.7232),
        S298 = (0.410225,'cal/mol/K','+|-',15.3939),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 391,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0106119,-1.04684,-1.87744,-2.37883,-2.96301,-3.17984,-3.72707],'cal/mol/K','+|-',[3,3.01292,4.0734,4.9461,5.60738,5.15625,3.96538]),
        H298 = (86.1096,'kcal/mol','+|-',11.4432),
        S298 = (0.633337,'cal/mol/K','+|-',16.3946),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 392,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S} {5,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.294223,-1.34019,-2.09677,-2.47482,-2.86392,-2.95588,-3.47696],'cal/mol/K','+|-',[3,3,4.34973,5.47513,6.24895,5.68473,4.27139]),
        H298 = (83.9718,'kcal/mol','+|-',8.32786),
        S298 = (0.0600541,'cal/mol/K','+|-',18.0717),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 393,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R",
    group = 
"""
1 * C u1 r0 {2,S} {5,S} {6,[S,D,T,B,Q]}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D}
4   C u0 {2,S}
5   C ux {1,S}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0887002,-0.595192,-0.928389,-1.06774,-1.44115,-1.73695,-2.50812],'cal/mol/K','+|-',[3.11145,4.22521,5.58085,5.97195,5.30349,4.38252,4.15545]),
        H298 = (80.139,'kcal/mol','+|-',7.57365),
        S298 = (-0.508503,'cal/mol/K','+|-',26.5519),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 394,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_Ext-6R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {5,S} {6,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D}
4   C   u0 r0 {2,S}
5   C   ux {1,S} {8,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H u0 r0 {6,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.43654,2.72626,3.38143,3.61825,2.76431,1.68111,0.420688],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.605,'kcal/mol','+|-',5.2),
        S298 = (-15.4627,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C=O)C[C](C=O)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 395,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_Ext-6R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {5,S} {6,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D}
4   C u0 {2,S}
5   C u0 {1,S}
6   C u0 {1,S} {7,[S,D,T,B,Q]}
7   C u0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.636368,-1.49881,-2.71952,-3.01917,-3.09972,-2.93856,-3.4835],'cal/mol/K','+|-',[3,3.40184,3.8445,3.61637,3.21224,3.3502,4.52927]),
        H298 = (84.8538,'kcal/mol','+|-',5.2),
        S298 = (9.26919,'cal/mol/K','+|-',30.358),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 396,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_Sp-8R!H-7C",
    group = 
"""
1 * C u1 r0 {2,S} {5,S} {6,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D}
4   C u0 r0 {2,S}
5   C u0 r0 {1,S}
6   C u0 r0 {1,S} {7,[S,D,T,B,Q]}
7   C u0 r0 {6,[S,D,T,B,Q]} {8,S}
8   C u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.279385,-2.70154,-4.07876,-4.29775,-4.23542,-4.12304,-5.08484],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.1925,'kcal/mol','+|-',5.2),
        S298 = (-1.46399,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[C](C)CCC(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 397,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-Sp-8R!H-7C",
    group = 
"""
1 * C u1 r0 {2,S} {5,S} {6,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D}
4   C u0 r0 {2,S}
5   C u0 r0 {1,S}
6   C u0 r0 {1,S} {7,[S,D,T,B,Q]}
7   C u0 r0 {6,[S,D,T,B,Q]} {8,[B,D,T,Q]}
8   C u0 r0 {7,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.55212,-0.296077,-1.36029,-1.74059,-1.96402,-1.75409,-1.88216],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.5151,'kcal/mol','+|-',5.2),
        S298 = (20.0024,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=CC[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 398,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_Ext-6R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {5,S} {6,S}
2   C                      u0 r0 {1,S} {3,D} {4,S}
3   C                      u0 r0 {2,D}
4   C                      u0 r0 {2,S}
5   C                      u0 r0 {1,S}
6   C                      u0 r0 {1,S} {7,[S,D,T,B,Q]}
7   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.41109,-1.26818,-1.25175,-1.41579,-1.83596,-2.18798,-2.9428],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (78.4571,'kcal/mol','+|-',2.4),
        S298 = (-2.55346,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[C](C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 399,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {5,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {1,S} {6,S}
6   C   ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.592731,-2.0187,-3.09714,-3.69835,-4.18866,-4.22299,-4.52998],'cal/mol/K','+|-',[3,3,3,4.79221,6.59332,5.94111,3.55574]),
        H298 = (86.5641,'kcal/mol','+|-',5.2),
        S298 = (1.98269,'cal/mol/K','+|-',11.0672),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 400,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {5,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux {1,S} {6,S}
6   C   ux {5,S}
7   R!H u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.236004,-2.27998,-3.93798,-4.98997,-5.89669,-5.74129,-5.51639],'cal/mol/K','+|-',[3.21872,3,3,5.06541,7.23424,6.59316,3.6524]),
        H298 = (87.093,'kcal/mol','+|-',6.66466),
        S298 = (4.99532,'cal/mol/K','+|-',11.3402),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 401,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {5,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux {1,S} {6,S}
6   C   ux {5,S} {8,[S,D,T,B,Q]}
7   R!H u0 r0 {4,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.946677,-2.17905,-4.9151,-6.83158,-8.54202,-8.15208,-6.85014],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (88.5716,'kcal/mol','+|-',2.4),
        S298 = (9.13129,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([CH]OC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 402,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-5R!H-R_4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S} {5,S}
2   C ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {2,[S,D,T,B,Q]}
5   C ux {1,S} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0911134,-1.61903,-2.25148,-2.19162,-2.05635,-2.197,-3.24622],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.7866,'kcal/mol','+|-',5.2),
        S298 = (-3.58835,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[CH]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 403,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-5R!H-R_N-4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S} {5,S}
2   C ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
5   C ux {1,S} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57048,-1.70281,-1.88472,-1.92828,-1.91008,-2.25551,-3.23732],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (85.9755,'kcal/mol','+|-',2.4),
        S298 = (-1.2318,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[CH]CC - Radical thermo from pang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 404,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_N-Sp-5R!H-1C",
    group = 
"""
1 * C u1 r0 {2,S} {5,[B,D,T,Q]}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D}
4   C u0 {2,S}
5   O ux {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3003,0.194251,-0.949495,-1.97274,-3.38223,-4.12737,-4.78521],'cal/mol/K','+|-',[3.43416,3.10963,3,3,3,3,3]),
        H298 = (94.0249,'kcal/mol','+|-',5.2),
        S298 = (3.05877,'cal/mol/K','+|-',6.8277),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 405,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_N-Sp-5R!H-1C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {5,[B,D,T,Q]}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D}
4   C   u0 r0 {2,S} {6,[S,D,T,B,Q]}
5   O   ux {1,[B,D,T,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.98144,1.71653,0.432748,-0.740614,-2.40357,-3.67828,-4.2331],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.3711,'kcal/mol','+|-',5.2),
        S298 = (-0.283637,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([C]=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 406,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_3C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.229962,-1.07471,-1.92187,-2.02867,-2.07825,-2.17303,-2.85036],'cal/mol/K','+|-',[3,3,3.32001,3.34553,3,3,3]),
        H298 = (66.9568,'kcal/mol','+|-',25.2647),
        S298 = (-2.6713,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 407,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_3C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.06755,-0.0361888,-0.748072,-0.845851,-1.39044,-1.78468,-2.6672],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.8892,'kcal/mol','+|-',5.2),
        S298 = (-3.31658,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](O)C=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 408,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.358164,-0.981926,-1.54107,-1.91048,-2.36429,-2.72771,-3.27396],'cal/mol/K','+|-',[3,3,3,3,3,3,3.23643]),
        H298 = (84.4996,'kcal/mol','+|-',16.4472),
        S298 = (-1.09998,'cal/mol/K','+|-',9.75482),
    ),
    shortDesc = """Radical correction fitted to 48 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 409,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31653,-1.11021,-1.78846,-2.18871,-2.67901,-3.04167,-3.45815],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2233,'kcal/mol','+|-',19.6928),
        S298 = (-0.232918,'cal/mol/K','+|-',8.82141),
    ),
    shortDesc = """Radical correction fitted to 30 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 410,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.329051,-1.03458,-1.65788,-1.96975,-2.30144,-2.62605,-3.07746],'cal/mol/K','+|-',[3,3,3,3,3,3,3.06487]),
        H298 = (79.664,'kcal/mol','+|-',12.5551),
        S298 = (-1.76418,'cal/mol/K','+|-',8.37901),
    ),
    shortDesc = """Radical correction fitted to 23 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 411,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D}
4   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.566262,-0.653051,-1.00089,-1.1777,-1.49613,-1.69245,-1.8857],'cal/mol/K','+|-',[3.25126,3,3,3,3,3,3.64935]),
        H298 = (73.2886,'kcal/mol','+|-',10.4319),
        S298 = (-4.78489,'cal/mol/K','+|-',6.60478),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 412,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-4O-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   O   ux {1,S} {5,S}
5   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0144219,-0.529552,-1.01002,-1.2041,-1.66975,-2.02614,-1.83153],'cal/mol/K','+|-',[3.54173,3.77876,3.0802,3,3,3,3]),
        H298 = (76.5614,'kcal/mol','+|-',5.2),
        S298 = (-5.88732,'cal/mol/K','+|-',3.93404),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 413,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-4O-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   O   ux {1,S} {5,S}
5   R!H u0 r0 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26661,-1.86555,-2.09904,-1.89524,-1.90823,-2.22946,-2.0499],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.6627,'kcal/mol','+|-',5.2),
        S298 = (-7.27821,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C](C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 414,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {5,[S,D,T,B,Q]}
4   O   ux {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.23908,-2.95289,-2.66412,-2.35152,-1.61387,-0.74646,0.779456],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (67.8653,'kcal/mol','+|-',2.4),
        S298 = (-6.58566,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC(O)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 415,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R",
    group = 
"""
1 * C u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D}
4   O ux {1,S}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.297809,0.105051,-0.503293,-0.795027,-1.33507,-1.73132,-2.3798],'cal/mol/K','+|-',[3,3,3,3,3,3,3.37184]),
        H298 = (72.0222,'kcal/mol','+|-',7.86153),
        S298 = (-4.97194,'cal/mol/K','+|-',8.82627),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 416,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   O   ux {1,S}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0545033,0.157083,-0.317135,-0.575449,-1.07232,-1.44362,-2.09027],'cal/mol/K','+|-',[3,3,3,3,3,3,3.66402]),
        H298 = (70.916,'kcal/mol','+|-',5.2),
        S298 = (-5.50402,'cal/mol/K','+|-',10.1012),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 417,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   O   u0 {1,S}
5   C   u0 {1,S} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.177496,-0.192065,-0.715957,-0.690441,-0.775813,-0.798004,-0.90294],'cal/mol/K','+|-',[3,3,3,3,3,3,3.66666]),
        H298 = (70.8286,'kcal/mol','+|-',5.2),
        S298 = (-9.63897,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 418,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S} {5,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D}
4   O u0 r0 {1,S}
5   C u0 r0 {1,S} {6,D}
6   C ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.993688,0.750946,-0.0135071,-0.301077,-0.950504,-1.4318,-2.1993],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (72.4953,'kcal/mol','+|-',5.2),
        S298 = (-8.79342,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C](O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 419,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S} {5,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D}
4   O u0 r0 {1,S}
5   C u0 r0 {1,S} {6,D}
6   O ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.638697,-1.13508,-1.41841,-1.0798,-0.601121,-0.164206,0.393419],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (69.162,'kcal/mol','+|-',5.2),
        S298 = (-10.4845,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 420,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   O   ux {1,S}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H u0 r0 {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0548235,0.467437,0.0373728,-0.473234,-1.33589,-2.0175,-3.14567],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (70.9532,'kcal/mol','+|-',2.4),
        S298 = (-1.82851,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#C[C](O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 421,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.197888,-1.24555,-2.02115,-2.40772,-2.74674,-3.14227,-3.73643],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.2987,'kcal/mol','+|-',6.25169),
        S298 = (-0.0939077,'cal/mol/K','+|-',7.47725),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 422,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.124679,-1.93656,-3.18323,-3.8195,-4.22928,-4.48707,-3.75987],'cal/mol/K','+|-',[5.06462,4.99893,5.11425,4.45743,3.1068,3,4.1909]),
        H298 = (80.7112,'kcal/mol','+|-',20.1485),
        S298 = (2.42163,'cal/mol/K','+|-',3.70641),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 423,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-3C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,D}
3   C   u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S}
5   R!H u0 r0 {3,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46989,-4.36154,-5.96549,-6.32605,-6.01267,-5.49993,-5.48944],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.5357,'kcal/mol','+|-',5.2),
        S298 = (4.10321,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 424,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-3C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.0446,0.631262,-0.93584,-2.06119,-3.17114,-4.11574,-1.4297],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.9886,'kcal/mol','+|-',5.2),
        S298 = (2.72696,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[CH]C=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 425,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   C   ux {1,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0205149,-0.571163,-1.06998,-1.55077,-2.38493,-3.06757,-4.24563],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (82.5298,'kcal/mol','+|-',2.4),
        S298 = (4.7775,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C](CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 426,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.314668,-1.31626,-2.07982,-2.38187,-2.57069,-2.93513,-3.67836],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.6331,'kcal/mol','+|-',5.2),
        S298 = (-1.39013,'cal/mol/K','+|-',7.51243),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 427,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   C   ux {1,S} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.456853,-1.47079,-2.24094,-2.52834,-2.68094,-3.03282,-3.65937],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.9314,'kcal/mol','+|-',5.2),
        S298 = (-1.61539,'cal/mol/K','+|-',7.6526),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 428,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.283054,-1.25588,-2.02034,-2.31943,-2.52662,-2.9381,-3.675],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.8452,'kcal/mol','+|-',5.2),
        S298 = (-0.954043,'cal/mol/K','+|-',6.21306),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 429,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   C   u0 r0 {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C   u0 {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.26895,0.186989,-0.761144,-1.45298,-2.18272,-2.87911,-2.19836],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.9067,'kcal/mol','+|-',5.2),
        S298 = (-1.45058,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 430,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   C   ux {1,S} {5,S}
5   C   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.270986,-1.53018,-2.46367,-2.78177,-2.87434,-3.20144,-4.02877],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.9612,'kcal/mol','+|-',5.2),
        S298 = (-0.861022,'cal/mol/K','+|-',7.51138),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 431,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   C   ux {1,S} {5,S}
5   C   ux {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.300225,-1.53869,-2.44781,-2.73925,-2.83044,-3.1926,-4.01747],'cal/mol/K','+|-',[3.04189,3,3,3,3,3,3]),
        H298 = (83.966,'kcal/mol','+|-',5.2),
        S298 = (-0.406837,'cal/mol/K','+|-',7.61253),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 432,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R",
    group = 
"""
1  * C   u1 r0 {2,S} {4,S}
2    C   ux {1,S} {3,D}
3    C   ux r0 {2,D}
4    C   ux {1,S} {5,S}
5    C   ux {4,S} {6,[S,D,T,B,Q]} {7,S}
6    R!H ux {5,[S,D,T,B,Q]} {8,S}
7    C   u0 {5,S}
8    C   ux {6,S} {9,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
9    R!H ux {8,[S,D,T,B,Q]}
10   R!H ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.75938,-0.612828,-2.40063,-2.85369,-2.73139,-2.89236,-4.23081],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.1203,'kcal/mol','+|-',5.2),
        S298 = (-5.22367,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]CC1CC(C)=CCC1C - Radical thermo from pang.py and closed shell thermo from GAV
C=C[CH]CC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 433,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   C   ux {1,S} {5,S}
5   C   ux {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {8,S}
7   C   ux {5,[S,D,T,B,Q]}
8   C   ux {6,S} {9,D}
9   C   u0 {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.22125,-2.09163,-2.68283,-2.93536,-2.95091,-3.50339,-4.15464],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.9403,'kcal/mol','+|-',2.4),
        S298 = (3.20762,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 434,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   C   u0 {1,S} {5,S}
5   C   u0 {4,S} {6,S} {7,S}
6   R!H u0 {5,S} {8,S}
7   C   u0 {5,S}
8   C   u0 {6,S} {9,[S,T,Q,B]}
9   C   ux {8,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.93004,-1.72566,-2.31413,-2.53306,-2.808,-3.1622,-3.79122],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2842,'kcal/mol','+|-',5.2),
        S298 = (0.0550519,'cal/mol/K','+|-',4.42955),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 435,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_5C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   C   u0 r0 {1,S} {5,S}
5   C   u0 r1 {4,S} {6,S} {7,S}
6   R!H u0 {5,S} {8,S}
7   C   u0 {5,S}
8   C   u0 {6,S} {9,[S,T,Q,B]}
9   C   ux {8,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0951163,-1.85622,-3.17319,-3.32731,-3.21752,-3.50765,-3.9589],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.7833,'kcal/mol','+|-',5.2),
        S298 = (-2.11337,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]CC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 436,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-5C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   C   u0 r0 {1,S} {5,S}
5   C   u0 r0 {4,S} {6,S} {7,S}
6   R!H u0 {5,S} {8,S}
7   C   u0 {5,S}
8   C   u0 {6,S} {9,[S,T,Q,B]}
9   C   ux {8,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.38566,-1.66763,-1.93233,-2.18006,-2.62599,-3.00867,-3.71669],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (84.391,'kcal/mol','+|-',2.4),
        S298 = (1.01879,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(N(CC)O)C[CH]C=C - Radical thermo from pang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 437,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_N-5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.499,-3.996,-4.83306,-4.98307,-4.49418,-4.14576,-3.47562],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.5761,'kcal/mol','+|-',5.2),
        S298 = (-9.38621,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]COOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 438,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_N-Sp-5R!H-4C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   C   u0 r0 {1,S} {5,[B,D,T,Q]}
5   R!H u0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4982,0.65399,-0.0255236,-0.514376,-1.16503,-1.68956,-3.92055],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.6434,'kcal/mol','+|-',5.2),
        S298 = (1.48197,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]C#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 439,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[B,D,T,Q]}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.285345,-1.29857,-2.11367,-2.73405,-3.61937,-4.0768,-4.40629],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.6303,'kcal/mol','+|-',19.061),
        S298 = (3.5808,'cal/mol/K','+|-',4.01726),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 440,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D}
4   C   u0 {1,D} {5,[S,D,T,B,Q]}
5   R!H u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.344323,-1.347,-2.23981,-2.95463,-4.0158,-4.49282,-4.65899],'cal/mol/K','+|-',[2.3134,2.08703,2,2,2,2,2]),
        H298 = (90.9963,'kcal/mol','+|-',23.5731),
        S298 = (3.73402,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 441,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C ux r0 {1,S} {3,D}
3   C ux r0 {2,D}
4   C u0 r0 {1,D} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904165,-1.91691,-2.64495,-3.10637,-3.78563,-4.16857,-4.36875],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (84.1989,'kcal/mol','+|-',2.4),
        S298 = (3.6583,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=[C]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
C=C=[C]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 442,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,D}
2   C                      ux r0 {1,S} {3,D}
3   C                      ux r0 {2,D}
4   C                      u0 r0 {1,D} {5,[S,D,T,B,Q]}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.775363,-0.207194,-1.42953,-2.65117,-4.47613,-5.14134,-5.23949],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.591,'kcal/mol','+|-',2.4),
        S298 = (3.88548,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 443,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[B,D,T,Q]}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {5,[S,D,T,B,Q]}
4   R!H ux {1,[B,D,T,Q]}
5   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.584897,-1.69784,-2.38371,-2.81212,-3.31662,-3.59679,-3.88622],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.212,'kcal/mol','+|-',10.5922),
        S298 = (3.58811,'cal/mol/K','+|-',8.27534),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 444,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3C-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,[B,D,T,Q]}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,[B,D,T,Q]}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3413,-1.62542,-2.36683,-2.76747,-3.21023,-3.49341,-4.04052],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.317,'kcal/mol','+|-',9.90866),
        S298 = (4.86209,'cal/mol/K','+|-',7.9528),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 445,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3C-R_4R!H->C_Sp-5R!H-3C",
    group = 
"""
1 * C u1 r0 {2,S} {4,[B,D,T,Q]}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D} {5,S}
4   C ux {1,[B,D,T,Q]}
5   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.350254,-1.98208,-2.81793,-2.90494,-2.6448,-2.59417,-3.58893],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.5411,'kcal/mol','+|-',5.2),
        S298 = (0.968912,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=[C]C=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 446,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3C-R_4R!H->C_N-Sp-5R!H-3C",
    group = 
"""
1 * C u1 r0 {2,S} {4,[B,D,T,Q]}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D} {5,D}
4   C ux {1,[B,D,T,Q]}
5   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.33732,-1.4669,-2.16635,-2.70638,-3.46153,-3.89308,-4.24123],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.548,'kcal/mol','+|-',2.4),
        S298 = (6.59239,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=[C]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 447,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3C-R_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   O u0 r0 {1,D}
5   C u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.37659,-1.93319,-2.43858,-2.95721,-3.66241,-3.93275,-3.38475],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.9167,'kcal/mol','+|-',5.2),
        S298 = (-0.552341,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 448,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {4,S}
4   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.458088,-0.804635,-1.12119,-1.39283,-1.70591,-2.02053,-2.76486],'cal/mol/K','+|-',[3,3,3,3,3,3,4.06597]),
        H298 = (84.2702,'kcal/mol','+|-',7.45535),
        S298 = (-3.02135,'cal/mol/K','+|-',11.845),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 449,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.38534,-0.655725,-0.94121,-1.216,-1.56304,-1.90282,-2.6686],'cal/mol/K','+|-',[3,3,3,3,3,3,4.0734]),
        H298 = (83.9774,'kcal/mol','+|-',6.7703),
        S298 = (-3.28771,'cal/mol/K','+|-',11.8967),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 450,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_4C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {4,S}
4   C u0 r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.229923,-0.0541546,-0.474612,-0.892495,-1.34584,-1.76474,-2.97114],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (80.2708,'kcal/mol','+|-',2.4),
        S298 = (-3.11307,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CC1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 451,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.404768,-0.730922,-0.999535,-1.25644,-1.59019,-1.92008,-2.63078],'cal/mol/K','+|-',[3.09838,3,3,3,3,3,4.32961]),
        H298 = (84.6038,'kcal/mol','+|-',6.47705),
        S298 = (-3.30954,'cal/mol/K','+|-',12.6633),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 452,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18322,-1.31439,-1.37132,-1.35504,-1.31768,-1.31943,-1.60246],'cal/mol/K','+|-',[3,3,3,3,3,3.70002,5.80915]),
        H298 = (82.8944,'kcal/mol','+|-',7.55188),
        S298 = (-4.24402,'cal/mol/K','+|-',18.2897),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 453,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-3C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   R!H ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08334,-1.15649,-1.13278,-1.09558,-0.948021,-0.732579,-0.760731],'cal/mol/K','+|-',[3.57006,3.4589,3,3,3.01301,4.96441,7.5333]),
        H298 = (80.7178,'kcal/mol','+|-',8.26082),
        S298 = (-5.9295,'cal/mol/K','+|-',25.7804),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 454,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   R!H ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H u0 r0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.94118,-2.39994,-1.79521,-0.830894,1.16869,2.71378,4.1329],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.0278,'kcal/mol','+|-',5.2),
        S298 = (-22.8993,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=C(CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 455,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S} {7,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.0651,-2.76379,-2.04917,-1.61394,-1.4971,-1.25696,-0.332094],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.3593,'kcal/mol','+|-',5.2),
        S298 = (-6.79244,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=C(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 456,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-3C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S} {6,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.72091,-3.3506,-3.05055,-2.41105,-1.89922,-1.59113,-0.872617],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.8024,'kcal/mol','+|-',5.2),
        S298 = (-6.02541,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=C(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 457,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {4,S}
4   C   ux r0 {3,S} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0715904,-0.310804,-0.763282,-1.11144,-1.73323,-2.33645,-3.26579],'cal/mol/K','+|-',[3.15436,3,3,3,3,3,3]),
        H298 = (86.1743,'kcal/mol','+|-',5.2),
        S298 = (-3.08142,'cal/mol/K','+|-',8.56789),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 458,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_5R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux r0 {3,S} {5,S}
5   C ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.439025,-0.409689,-0.594433,-0.843249,-1.67303,-2.48592,-3.54576],'cal/mol/K','+|-',[3.60887,3,3,3,3,3,3]),
        H298 = (86.1963,'kcal/mol','+|-',5.47091),
        S298 = (-0.699873,'cal/mol/K','+|-',3.58508),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 459,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_5R!H-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux r0 {3,S} {5,S}
5   C ux r1 {4,S} {6,S}
6   C u0 {5,S} {7,[S,D,T,B,Q]} {8,S}
7   C ux {6,[S,D,T,B,Q]}
8   C u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.751414,0.547015,-0.0143481,-0.555041,-1.65762,-2.4367,-4.01872],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.935,'kcal/mol','+|-',10.3798),
        S298 = (0.48461,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 460,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_5R!H-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Int-10R!H-8R!H_Int-10R!H-9R!H_Int-10R!H-9R!H_Ext-9R!H-R",
    group = 
"""
1  * C   u1 r0 {2,S}
2    C   ux {1,S} {3,D}
3    C   ux r0 {2,D} {4,S}
4    C   ux r0 {3,S} {5,S}
5    C   ux r1 {4,S} {6,S}
6    C   u0 r1 {5,S} {7,[S,D,T,B,Q]} {8,S}
7    C   ux r1 {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8    C   u0 r1 {6,S}
9    C   ux r1 {7,[S,D,T,B,Q]} {10,[S,D,T,B,Q]} {11,[S,D,T,B,Q]}
10   R!H ux {9,[S,D,T,B,Q]}
11   R!H ux {9,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.541775,0.927198,0.375144,-0.0884557,-1.47915,-2.41455,-3.18111],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.8842,'kcal/mol','+|-',5.2),
        S298 = (0.347677,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CCC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 461,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_N-5R!H-inRing",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D}
3   C   ux r0 {2,D} {4,S}
4   C   ux r0 {3,S} {5,S}
5   R!H ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.773687,-0.174838,-0.99545,-1.4802,-1.81602,-2.13093,-2.88083],'cal/mol/K','+|-',[3,3,3,3,3,3,3.62062]),
        H298 = (86.117,'kcal/mol','+|-',5.2),
        S298 = (-6.35604,'cal/mol/K','+|-',8.93434),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 462,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_N-5R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D} {4,S}
4   C   u0 r0 {3,S} {5,S} {6,[S,D,T,B,Q]}
5   R!H u0 r0 {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.840844,1.0577,0.721705,0.317484,-0.502833,-1.3154,-2.20104],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.1703,'kcal/mol','+|-',5.2),
        S298 = (-5.78389,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 463,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_N-5R!H-inRing_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,D}
3   C u0 r0 {2,D} {4,S}
4   C u0 r0 {3,S} {5,S}
5   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.135145,-1.34942,-2.09269,-2.30338,-1.97991,-1.71099,-2.2782],'cal/mol/K','+|-',[3,3,3,3,3,3.30003,4.51214]),
        H298 = (86.5992,'kcal/mol','+|-',5.2),
        S298 = (-9.01013,'cal/mol/K','+|-',9.59605),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 464,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_N-5R!H-inRing_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D} {4,S}
4   C   u0 r0 {3,S} {5,S}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.198307,-1.02636,-2.0326,-2.54068,-2.73358,-2.87773,-3.87348],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.8411,'kcal/mol','+|-',5.2),
        S298 = (-5.61741,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CCCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 465,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_N-5R!H-inRing_N-5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux r0 {3,S} {5,S}
5   O ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.52419,0.941798,-0.51812,-1.63154,-2.80141,-3.78633,-4.76587],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.0993,'kcal/mol','+|-',5.2),
        S298 = (-1.62001,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 466,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_N-Sp-5R!H-4C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D} {4,S}
4   C   u0 r0 {3,S} {5,[B,D,T,Q]}
5   R!H u0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.908195,-0.34601,-0.455524,-1.89438,-2.27503,-2.46956,-4.31055],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.1834,'kcal/mol','+|-',5.2),
        S298 = (1.53197,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CC#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 467,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux r0 {2,D} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.93124,-3.82007,-4.76569,-4.97367,-4.59908,-4.40406,-4.7142],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.0605,'kcal/mol','+|-',5),
        S298 = (2.37232,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=COC - Radical thermo from johnson_g4.py and closed shell thermo from GAV
""",
)

entry(
    index = 468,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_N-Sp-4R!H-3C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D} {4,[B,D,T,Q]}
4   R!H u0 {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.311614,-0.472342,-0.948331,-1.47093,-2.2312,-2.84711,-3.81492],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.8694,'kcal/mol','+|-',5.2),
        S298 = (-0.928838,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH2]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 469,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.424238,-1.02728,-1.595,-1.88628,-2.16409,-2.4449,-3.24175],'cal/mol/K','+|-',[4.01802,4.99435,5.4504,5.43683,4.71398,3.86792,4.51616]),
        H298 = (92.6568,'kcal/mol','+|-',20.5517),
        S298 = (-2.01809,'cal/mol/K','+|-',9.12683),
    ),
    shortDesc = """Radical correction fitted to 29 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 470,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   O   ux {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.50476,-2.36038,-2.95887,-3.0947,-2.93585,-2.80505,-3.10773],'cal/mol/K','+|-',[3.64609,4.77024,5.59725,5.87382,5.38317,4.79908,5.96853]),
        H298 = (87.275,'kcal/mol','+|-',24.4942),
        S298 = (-1.82928,'cal/mol/K','+|-',11.1972),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 471,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   O   ux {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53914,-2.38098,-2.99502,-3.10886,-2.86951,-2.67216,-2.94488],'cal/mol/K','+|-',[3.89949,5.07679,5.94747,6.25765,5.74815,5.09565,6.33689]),
        H298 = (83.2863,'kcal/mol','+|-',14.1032),
        S298 = (-2.61217,'cal/mol/K','+|-',11.1229),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 472,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   O   ux {2,D}
4   R!H ux {1,S}
5   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.30824,-3.16167,-4.40278,-4.70265,-4.26099,-3.78822,-3.58225],'cal/mol/K','+|-',[3.93113,5.41077,6.89124,7.68171,7.26122,6.04452,7.70152]),
        H298 = (78.0276,'kcal/mol','+|-',10.5235),
        S298 = (-2.45138,'cal/mol/K','+|-',15.8087),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 473,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   O   ux {2,D}
4   R!H ux {1,S}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.423703,-2.60359,-4.05659,-4.25653,-3.53776,-3.20793,-4.41154],'cal/mol/K','+|-',[4.71729,7.34904,9.59421,10.6963,9.93338,8.28708,10.4398]),
        H298 = (83.2031,'kcal/mol','+|-',9.38742),
        S298 = (-4.65836,'cal/mol/K','+|-',21.0028),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 474,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   O   ux {2,D}
4   R!H ux {1,S}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.504729,-3.33445,-5.1931,-5.69319,-5.13252,-4.65351,-5.93236],'cal/mol/K','+|-',[5.43096,7.60048,9.39615,9.87465,7.98389,5.98684,9.14551]),
        H298 = (83.0264,'kcal/mol','+|-',10.8012),
        S298 = (-1.60113,'cal/mol/K','+|-',18.4096),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 475,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   O   ux {2,D}
4   R!H ux {1,S}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.48919,-4.31942,-6.14793,-6.71576,-5.97406,-5.35127,-7.37899],'cal/mol/K','+|-',[4.58075,7.96034,10.5143,11.0076,8.86664,6.48681,8.67381]),
        H298 = (83.7389,'kcal/mol','+|-',12.7599),
        S298 = (0.944632,'cal/mol/K','+|-',18.7838),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 476,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_7R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   O   u0 {2,D}
4   R!H ux {1,S}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
7   C   ux {5,[S,D,T,B,Q]}
8   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.770409,-2.07419,-3.12452,-3.54945,-3.42394,-3.4931,-5.60783],'cal/mol/K','+|-',[5.43758,3,3,3,3,3,8.67072]),
        H298 = (80.5722,'kcal/mol','+|-',9.21704),
        S298 = (-3.26627,'cal/mol/K','+|-',16.7362),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 477,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_7R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,D}
3   O u0 r0 {2,D}
4   C ux r0 {1,S}
5   C ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
7   C ux {5,[S,D,T,B,Q]}
8   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.69288,-2.92189,-3.58782,-4.0136,-3.80484,-3.89479,-8.67339],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.8309,'kcal/mol','+|-',5.2),
        S298 = (2.65085,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C=O)C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 478,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_7R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,D}
3   O u0 r0 {2,D}
4   O ux r0 {1,S}
5   C ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
7   C ux {5,[S,D,T,B,Q]}
8   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.15206,-1.22648,-2.66122,-3.08531,-3.04304,-3.09141,-2.54226],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.3135,'kcal/mol','+|-',5.2),
        S298 = (-9.1834,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 479,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_N-7R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,D}
3   O   ux {2,D}
4   R!H u0 {1,S}
5   C   u0 {1,S} {6,S} {7,S} {8,S}
6   C   ux {5,S}
7   O   u0 {5,S}
8   O   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.92674,-8.80987,-12.1947,-13.0484,-11.0743,-9.06759,-10.9213],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.0723,'kcal/mol','+|-',5.2),
        S298 = (9.36644,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C=O)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 480,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,D}
3   O   ux {2,D}
4   R!H u0 {1,S}
5   C   u0 {1,S} {6,S} {7,S}
6   O   ux {5,S}
7   O   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0996016,0.319824,0.489469,1.49008,2.84128,2.57438,1.67177],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.9101,'kcal/mol','+|-',5.2),
        S298 = (-16.8873,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 481,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S} {5,S}
2   C u0 r0 {1,S} {3,D}
3   O u0 r0 {2,D}
4   O u0 {1,S}
5   C u0 {1,S} {6,[S,D,T,B,Q]}
6   C u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.19643,-3.42188,-4.43133,-5.01774,-4.96625,-4.41668,-3.13533],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (76.3325,'kcal/mol','+|-',2.4),
        S298 = (-0.58482,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 482,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,S} {5,S}
2   C                      u0 r0 {1,S} {3,D}
3   O                      u0 r0 {2,D}
4   O                      u0 {1,S}
5   C                      u0 {1,S} {6,[S,D,T,B,Q]}
6   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.38568,-4.14162,-5.14357,-5.37893,-5.16289,-4.44927,-2.18631],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (74.2104,'kcal/mol','+|-',2.4),
        S298 = (0.58645,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 483,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   O ux {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.764537,-0.408034,-0.559603,-0.713597,-1.1505,-1.63025,-3.36798],'cal/mol/K','+|-',[3.62743,3.43208,3.18241,3.36288,3.47096,3.34903,4.66481]),
        H298 = (92.1905,'kcal/mol','+|-',5.2),
        S298 = (-2.93764,'cal/mol/K','+|-',8.97356),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 484,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-2C-R",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,D} {5,S}
3   O ux {2,D}
4   C ux {1,S}
5   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.60448,-0.811237,-0.642197,-0.704946,-1.13746,-1.76211,-2.87235],'cal/mol/K','+|-',[3.97292,3.26393,3,3,3,3,3]),
        H298 = (90.5594,'kcal/mol','+|-',5.2),
        S298 = (-2.66936,'cal/mol/K','+|-',5.12075),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 485,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-2C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D} {5,S}
3   O   ux {2,D}
4   C   ux r0 {1,S} {6,[S,D,T,B,Q]}
5   C   u0 r0 {2,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.00912,-1.96521,-1.55445,-1.41295,-1.37093,-1.62023,-2.94668],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.0245,'kcal/mol','+|-',5.2),
        S298 = (-0.858899,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[CH]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 486,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_Ext-5R!H-R_5R!H->O",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   O u0 {2,D}
4   C u0 {1,S} {5,S}
5   O u0 {4,S} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23553,-0.976388,-1.31337,-1.59681,-2.04877,-2.44786,-4.99874],'cal/mol/K','+|-',[3.66612,3.9026,3,3,3,3,5.60153]),
        H298 = (92.703,'kcal/mol','+|-',5.2),
        S298 = (-0.150252,'cal/mol/K','+|-',6.78966),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 487,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_Ext-5R!H-R_5R!H->O_4C-inRing",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 r0 {1,S} {3,D}
3   O u0 r0 {2,D}
4   C u0 r1 {1,S} {5,S}
5   O u0 {4,S} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.55917,0.934073,0.0234411,-0.616678,-1.31791,-1.69507,-7.74088],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.788,'kcal/mol','+|-',5.2),
        S298 = (-3.47403,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1([CH]C=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 488,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_Ext-5R!H-R_5R!H->O_N-4C-inRing",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 r0 {1,S} {3,D}
3   O u0 r0 {2,D}
4   C u0 r0 {1,S} {5,S}
5   O u0 {4,S} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.03317,-1.82548,-1.90751,-2.03242,-2.37359,-2.78243,-3.78],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (92.8979,'kcal/mol','+|-',2.4),
        S298 = (1.32698,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 489,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_Ext-5R!H-R_N-5R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   O   u0 {2,D}
4   C   u0 {1,S} {5,S}
5   C   u0 {4,S} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.840756,0.918743,0.747864,0.712971,0.296154,-0.16976,-1.21363],'cal/mol/K','+|-',[3.68742,4.21026,4.61195,5.50557,6.3141,6.03489,3.22568]),
        H298 = (92.3622,'kcal/mol','+|-',5.2),
        S298 = (-7.73542,'cal/mol/K','+|-',9.8112),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 490,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_Ext-5R!H-R_N-5R!H->O_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D}
3   O   u0 r0 {2,D}
4   C   u0 r0 {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 r0 {4,S} {6,D}
6   R!H ux r0 {5,D}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.14446,2.40729,2.37843,2.65948,2.52853,1.9639,-0.0731802],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.7124,'kcal/mol','+|-',5.2),
        S298 = (-11.2042,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[CH]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 491,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   O ux {2,D}
4   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.95903,-3.63322,-3.77374,-3.51336,-2.73204,-2.11784,-1.28625],'cal/mol/K','+|-',[3.80694,4.16416,3.11512,3,3.12636,5.22995,6.57188]),
        H298 = (82.2607,'kcal/mol','+|-',5.67844),
        S298 = (-2.46085,'cal/mol/K','+|-',5.30626),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 492,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   O   u0 r0 {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.72446,-6.97474,-6.38841,-4.62327,-0.912188,1.61595,3.97225],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.3344,'kcal/mol','+|-',5.2),
        S298 = (-6.34758,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C([CH]O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 493,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_Ext-4O-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   O   ux {2,D}
4   O   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.19457,-3.45381,-3.32608,-2.94147,-2.14213,-1.72386,-1.54209],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.9535,'kcal/mol','+|-',2.4),
        S298 = (-2.75309,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[CH]OO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 494,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_N-Sp-4R!H-1C",
    group = 
"""
1 * C u1 r0 {2,S} {4,[B,D,T,Q]}
2   C u0 {1,S} {3,D}
3   O ux {2,D}
4   C u0 {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26941,-2.21938,-2.71144,-2.9977,-3.38998,-3.71484,-4.22264],'cal/mol/K','+|-',[3,3,3.46392,3.287,3,3,3]),
        H298 = (111.421,'kcal/mol','+|-',13.7808),
        S298 = (3.53045,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 495,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C u0 {1,S} {3,D}
3   O ux {2,D}
4   C u0 {1,D} {5,S}
5   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.973422,-1.61333,-1.95779,-2.28255,-2.91926,-3.50161,-4.52869],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.71,'kcal/mol','+|-',2.4),
        S298 = (2.947,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 496,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,D}
2   C                      u0 {1,S} {3,D}
3   O                      ux {2,D}
4   C                      u0 {1,D} {5,S}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.93538,-3.58298,-4.40715,-4.6068,-4.44908,-4.19462,-3.53403],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (119.454,'kcal/mol','+|-',5.2),
        S298 = (4.84323,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
COC=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 497,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.02633,0.705244,0.137062,-0.365516,-1.19534,-1.99421,-3.39903],'cal/mol/K','+|-',[3,3.10421,3.05155,3.14936,3.15514,3,3]),
        H298 = (98.3184,'kcal/mol','+|-',5.80071),
        S298 = (-2.33899,'cal/mol/K','+|-',6.55185),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 498,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.28233,0.919579,0.319543,-0.209988,-1.078,-1.91964,-3.39377],'cal/mol/K','+|-',[3,3.49636,3.46718,3.61059,3.64381,3,3]),
        H298 = (99.4075,'kcal/mol','+|-',5.2),
        S298 = (-2.47523,'cal/mol/K','+|-',7.62184),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 499,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.67246,1.78641,1.33299,0.865256,-0.0521935,-1.23781,-2.84681],'cal/mol/K','+|-',[5.16025,5.56801,5.09175,5.09509,5.2856,4.22039,3.56503]),
        H298 = (98.7449,'kcal/mol','+|-',11.0983),
        S298 = (-5.11258,'cal/mol/K','+|-',11.0283),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 500,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-6O-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H u0 r0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.55212,5.56948,4.21265,2.87275,0.671258,-1.65745,-4.02074],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.541,'kcal/mol','+|-',5.2),
        S298 = (-6.62751,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 501,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.818817,1.17182,1.03245,0.842314,0.210877,-0.818185,-2.24551],'cal/mol/K','+|-',[4.19248,5.39108,5.85514,6.87006,8.09842,6.56076,4.99588]),
        H298 = (97.353,'kcal/mol','+|-',7.97795),
        S298 = (-4.99637,'cal/mol/K','+|-',17.7698),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 502,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_4R!H->C_Ext-4C-R_7R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,S}
5   O ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
7   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0933478,-0.00111986,-0.241457,-0.652415,-1.55111,-2.24562,-3.33247],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (96.3623,'kcal/mol','+|-',2.4),
        S298 = (-1.13016,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 503,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_4R!H->C_Ext-4C-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   O                      ux {2,D}
4   C                      ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,S}
5   O                      ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O                      ux {5,[S,D,T,B,Q]}
7   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.87119,3.81095,3.89875,4.20545,4.17534,2.39354,0.200152],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.004,'kcal/mol','+|-',5.2),
        S298 = (-13.6953,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 504,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_N-4R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.567117,0.000744342,-0.569909,-1.06767,-1.63062,-2.18194,-3.62708],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.8749,'kcal/mol','+|-',5.2),
        S298 = (-3.97534,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OC(=O)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 505,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,D} {4,S}
3   O u0 {2,D}
4   O u0 {2,S} {5,S}
5   C ux {4,S} {6,S}
6   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.05476,0.413927,-0.271636,-0.837213,-1.67639,-2.31738,-3.71283],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.679,'kcal/mol','+|-',2.4),
        S298 = (-0.93677,'cal/mol/K','+|-',2.08618),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 506,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-6BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 {1,S} {3,D} {4,S}
3   O   u0 {2,D}
4   O   u0 {2,S} {5,S}
5   C   ux {4,S} {6,S}
6   C   u0 {5,S} {7,[S,D,T,B,Q]}
7   R!H u0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.953541,0.319817,-0.390247,-0.980945,-1.80107,-2.32905,-3.66195],'cal/mol/K','+|-',[2,2,2,2.24952,2.23042,2,2]),
        H298 = (99.4594,'kcal/mol','+|-',2.4),
        S298 = (-0.716347,'cal/mol/K','+|-',2.31563),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 507,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-6BrCClFINPSSi-R_7R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   O u0 r0 {2,D}
4   O u0 r0 {2,S} {5,S}
5   C ux {4,S} {6,S}
6   C u0 r0 {5,S} {7,[S,D,T,B,Q]}
7   O u0 r0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.410555,-0.488306,-1.45389,-2.2756,-3.08852,-3.01618,-3.66348],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.7552,'kcal/mol','+|-',2.4),
        S298 = (0.620539,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 508,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-6BrCClFINPSSi-R_N-7R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   O u0 r0 {2,D}
4   O u0 r0 {2,S} {5,S}
5   C ux {4,S} {6,S}
6   C u0 r0 {5,S} {7,[S,D,T,B,Q]}
7   C u0 r0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.22503,0.723878,0.141574,-0.333616,-1.15734,-1.98548,-3.66118],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.3115,'kcal/mol','+|-',2.4),
        S298 = (-1.38479,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OC(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH2]C(=O)OCC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 509,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.107545,-0.787501,-1.56631,-2.1726,-2.88534,-3.50534,-4.71091],'cal/mol/K','+|-',[3.16985,3.57916,3.68639,3.54363,3.02085,3,3]),
        H298 = (99.0893,'kcal/mol','+|-',12.4495),
        S298 = (1.89777,'cal/mol/K','+|-',8.66545),
    ),
    shortDesc = """Radical correction fitted to 83 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 510,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0608567,-0.97045,-1.83803,-2.38582,-3.003,-3.61099,-4.8016],'cal/mol/K','+|-',[3.57144,4.24706,4.39779,4.18591,3.62817,3.33618,3.10814]),
        H298 = (101.437,'kcal/mol','+|-',11.8757),
        S298 = (1.10057,'cal/mol/K','+|-',8.64042),
    ),
    shortDesc = """Radical correction fitted to 43 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 511,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.508917,-0.724093,-1.85004,-2.53235,-3.25198,-3.89419,-5.34423],'cal/mol/K','+|-',[3.40902,3.89638,4.47968,4.55785,4.03923,3.9562,3.56243]),
        H298 = (102.222,'kcal/mol','+|-',14.1396),
        S298 = (1.82584,'cal/mol/K','+|-',3.84019),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 512,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.937706,0.474089,-0.189277,-0.874807,-2.02994,-2.92108,-4.26563],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (101.075,'kcal/mol','+|-',2.65792),
        S298 = (1.39372,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 513,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_4R!H->C_Ext-2C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,S} {5,S}
3   O   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {6,[S,D,T,B,Q]}
5   C   u0 {2,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.798196,0.760269,0.258407,-0.47115,-1.74155,-2.74358,-4.26957],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.9529,'kcal/mol','+|-',2.4),
        S298 = (2.09275,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)OC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 514,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.51645,-0.108495,-0.839556,-1.49108,-2.55571,-3.35258,-4.51783],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.543,'kcal/mol','+|-',2.4),
        S298 = (1.71202,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 515,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.226544,-1.51314,-2.94371,-3.6239,-4.05674,-4.53502,-6.05454],'cal/mol/K','+|-',[4.29296,4.27443,4.45716,4.6047,4.47361,4.66252,3.96904]),
        H298 = (103.494,'kcal/mol','+|-',20.6711),
        S298 = (2.11041,'cal/mol/K','+|-',4.75815),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 516,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.13749,-0.478887,-2.01661,-3.00836,-4.07607,-5.02273,-6.37001],'cal/mol/K','+|-',[4.61425,3.89134,4.56656,5.41763,5.62173,5.6717,4.90868]),
        H298 = (105.636,'kcal/mol','+|-',20.7518),
        S298 = (1.82046,'cal/mol/K','+|-',5.28502),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 517,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-2C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,S} {6,[S,D,T,B,Q]}
3   O   u0 {2,S} {4,S}
4   O   u0 {3,S} {5,S}
5   C   u0 {4,S} {7,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
7   O   u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.46227,-0.0228981,-3.08964,-4.60546,-6.13241,-7.54823,-7.08454],'cal/mol/K','+|-',[5.31299,6.71264,7.03684,8.16991,8.08685,6.89863,3.76195]),
        H298 = (119.444,'kcal/mol','+|-',19.9459),
        S298 = (0.162322,'cal/mol/K','+|-',7.44441),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 518,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-2C-R_Ext-5R!H-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
3   O   u0 r1 {2,S} {4,S}
4   O   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {7,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
7   O   u0 {5,[S,D,T,B,Q]}
8   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.58384,-2.39617,-5.57754,-7.49396,-8.99154,-9.98726,-8.41459],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (126.496,'kcal/mol','+|-',5.2),
        S298 = (2.79432,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)CC(OO)C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 519,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-2C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]} {7,S}
7   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.585702,-1.73229,-2.81668,-3.77983,-4.46202,-5.03924,-8.0332],'cal/mol/K','+|-',[3,3,3.36123,3.01244,3,3.13665,5.9235]),
        H298 = (100.123,'kcal/mol','+|-',7.31853),
        S298 = (3.83764,'cal/mol/K','+|-',4.81533),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 520,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-2C-R_Ext-6R!H-R_Int-5R!H-2C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]} {7,S}
7   R!H u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.15634,-0.679242,-1.6283,-2.71477,-3.40934,-3.93026,-5.93893],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.5353,'kcal/mol','+|-',5.2),
        S298 = (2.13516,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C(C)C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 521,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.44494,-3.16184,-4.27383,-4.32166,-3.72732,-3.59113,-5.33094],'cal/mol/K','+|-',[3,3.37112,3.35247,3.30235,3.4359,3.45611,3]),
        H298 = (97.4213,'kcal/mol','+|-',26.0383),
        S298 = (2.09191,'cal/mol/K','+|-',5.15158),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 522,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-1C-R_5R!H->O",
    group = 
"""
1 * C u1 r0 {2,S} {5,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53777,-3.29967,-4.25734,-4.1035,-3.07833,-2.71702,-4.53927],'cal/mol/K','+|-',[3,4.71943,4.74042,4.54628,3.67453,3,3]),
        H298 = (90.0108,'kcal/mol','+|-',6.1656),
        S298 = (1.1728,'cal/mol/K','+|-',5.7274),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 523,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-1C-R_5R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {5,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux r1 {3,[S,D,T,B,Q]}
5   O   ux {1,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.60941,-1.6311,-2.58135,-2.49614,-1.77918,-1.88399,-4.06932],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.8309,'kcal/mol','+|-',5.2),
        S298 = (-0.852143,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 524,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-1C-R_N-5R!H->O",
    group = 
"""
1 * C                      u1 r0 {2,S} {5,[S,D,T,B,Q]}
2   C                      u0 r1 {1,S} {3,S}
3   O                      u0 r1 {2,S} {4,S}
4   O                      u0 r1 {3,S}
5   [F,I,P,Br,Cl,C,Si,S,N] u0 r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.25928,-2.88618,-4.30681,-4.758,-5.0253,-5.33937,-6.91428],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (112.242,'kcal/mol','+|-',5.2),
        S298 = (3.93014,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 525,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.114247,-1.06673,-1.83333,-2.32855,-2.9057,-3.50032,-4.58954],'cal/mol/K','+|-',[3.63623,4.4341,4.45418,4.12012,3.51992,3.11972,3]),
        H298 = (101.129,'kcal/mol','+|-',11.2364),
        S298 = (0.817135,'cal/mol/K','+|-',9.91869),
    ),
    shortDesc = """Radical correction fitted to 31 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 526,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0765159,-1.11758,-1.94752,-2.43006,-2.91117,-3.46538,-4.51877],'cal/mol/K','+|-',[4.14657,5.16556,5.20342,4.80485,4.09761,3.59938,3.31829]),
        H298 = (100.048,'kcal/mol','+|-',13.1403),
        S298 = (-0.220954,'cal/mol/K','+|-',10.7824),
    ),
    shortDesc = """Radical correction fitted to 24 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 527,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.701848,-2.04937,-2.90995,-3.35363,-3.46926,-3.89557,-5.66875],'cal/mol/K','+|-',[3,3.16846,3.8182,4.00334,4.21915,4.10937,3]),
        H298 = (95.5208,'kcal/mol','+|-',5.38292),
        S298 = (2.06392,'cal/mol/K','+|-',8.89801),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 528,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_Ext-3O-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,S}
3   O   u0 {2,S} {6,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H u0 {3,S} {7,S}
7   C   ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01586,-2.66745,-3.68558,-4.17059,-4.27594,-4.58828,-6.21251],'cal/mol/K','+|-',[3,3,3,3,3.09666,3.44378,3]),
        H298 = (95.742,'kcal/mol','+|-',6.31183),
        S298 = (3.28042,'cal/mol/K','+|-',9.00171),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 529,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_Ext-3O-R_Ext-6R!H-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,S} {8,S}
3   O   u0 {2,S} {6,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   O   u0 {3,S} {7,S}
7   C   ux {6,S}
8   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.30421,-3.50992,-4.56077,-4.86429,-4.77036,-5.28771,-6.88918],'cal/mol/K','+|-',[3,3,3,3,3.79294,3.89566,3]),
        H298 = (93.0185,'kcal/mol','+|-',5.2),
        S298 = (2.12896,'cal/mol/K','+|-',11.4858),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 530,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_Ext-3O-R_Ext-6R!H-R_Ext-2C-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,S} {8,S}
3   O   u0 {2,S} {6,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   O   u0 {3,S} {7,S}
7   C   ux {6,S} {9,[S,D,T,B,Q]}
8   C   u0 {2,S}
9   C   ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.05129,-3.14471,-4.10065,-4.25555,-3.91171,-4.40416,-6.64322],'cal/mol/K','+|-',[3,3,3,3,3.32835,3.40833,3]),
        H298 = (92.0377,'kcal/mol','+|-',5.2),
        S298 = (-0.323618,'cal/mol/K','+|-',10.9309),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 531,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_Ext-3O-R_Ext-6R!H-R_Ext-2C-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->O",
    group = 
"""
1  * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2    C   ux r0 {1,S} {3,S} {8,S}
3    O   u0 {2,S} {6,S}
4    R!H ux {1,[S,D,T,B,Q]}
5    R!H ux {1,[S,D,T,B,Q]}
6    O   u0 r0 {3,S} {7,S}
7    C   ux {6,S} {9,[S,D,T,B,Q]}
8    C   u0 r0 {2,S}
9    C   ux {7,[S,D,T,B,Q]} {10,[S,D]}
10   O   u0 r0 {9,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3535,-3.11341,-4.56582,-5.11654,-5.08845,-5.60919,-6.92558],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.0423,'kcal/mol','+|-',5.2),
        S298 = (3.54103,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C(C)(C)OOC(C)(C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 532,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_Ext-3O-R_Ext-6R!H-R_Ext-2C-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->O",
    group = 
"""
1  * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2    C   ux r0 {1,S} {3,S} {8,S}
3    O   u0 {2,S} {6,S}
4    R!H ux {1,[S,D,T,B,Q]}
5    R!H ux {1,[S,D,T,B,Q]}
6    O   u0 r0 {3,S} {7,S}
7    C   ux {6,S} {9,[S,D,T,B,Q]}
8    C   u0 r0 {2,S}
9    C   ux {7,[S,D,T,B,Q]} {10,[S,D]}
10   C   u0 r0 {9,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.74907,-3.17601,-3.63548,-3.39456,-2.73496,-3.19913,-6.36086],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.0331,'kcal/mol','+|-',5.2),
        S298 = (-4.18827,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(COO)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 533,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
4   O ux {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.569048,0.48731,0.320059,0.153086,0.197359,-0.560039,-3.02186],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.2605,'kcal/mol','+|-',5.2),
        S298 = (-3.64185,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 534,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_N-4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.324166,-1.34109,-2.06788,-2.57133,-2.90078,-3.59439,-5.46086],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.0787,'kcal/mol','+|-',5.2),
        S298 = (1.38308,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 535,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.715968,-1.81128,-2.60122,-2.98451,-3.29909,-3.62505,-4.05641],'cal/mol/K','+|-',[3.74545,4.55262,4.61205,4.02321,3.10471,3.1025,3.76084]),
        H298 = (104.644,'kcal/mol','+|-',12.1919),
        S298 = (-0.544715,'cal/mol/K','+|-',11.1174),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 536,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.324277,-1.76728,-2.92596,-3.50486,-3.9375,-4.32761,-4.49597],'cal/mol/K','+|-',[4.23363,5.69093,5.67929,4.64068,3,3,3.9553]),
        H298 = (99.8542,'kcal/mol','+|-',5.2),
        S298 = (-1.54892,'cal/mol/K','+|-',13.3272),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 537,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   C   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01756,-2.91571,-4.22451,-4.40139,-3.99847,-3.88022,-3.11815],'cal/mol/K','+|-',[4.63693,5.24396,4.94163,4.10021,3,3,3.96551]),
        H298 = (99.6987,'kcal/mol','+|-',7.28325),
        S298 = (-6.97866,'cal/mol/K','+|-',9.90226),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 538,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R_Ext-4C-R",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,S} {6,S}
5   C ux {2,[S,D,T,B,Q]}
6   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.91763,-4.03355,-5.30151,-5.31407,-4.56066,-4.0089,-2.63839],'cal/mol/K','+|-',[3,3,3,3,3,3,3.85087]),
        H298 = (99.4479,'kcal/mol','+|-',8.30965),
        S298 = (-9.00165,'cal/mol/K','+|-',4.64837),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 539,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R_Ext-4C-R_Ext-5R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r0 {2,S} {4,S}
2    C ux r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3    O ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4    C ux {1,S} {6,S}
5    C ux {2,[S,D,T,B,Q]}
6    C u0 {4,S}
7    O ux {3,[S,D,T,B,Q]} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,S}
10   C u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.05904,-4.82022,-5.84712,-5.49658,-4.04495,-2.96663,-1.07086],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.6391,'kcal/mol','+|-',5.2),
        S298 = (-9.54362,'cal/mol/K','+|-',7.32354),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 540,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R_Ext-4C-R_Ext-5R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-10R!H-9R!H_Ext-10R!H-R_Ext-10R!H-R",
    group = 
"""
1  * C   u1 r0 {2,S} {4,S}
2    C   ux r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3    O   ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4    C   ux {1,S} {6,S}
5    C   ux {2,[S,D,T,B,Q]}
6    C   u0 r0 {4,S}
7    O   ux {3,[S,D,T,B,Q]} {8,S}
8    C   u0 r1 {7,S} {9,[S,D,T,B,Q]}
9    C   ux r1 {8,[S,D,T,B,Q]} {10,S}
10   C   u0 r1 {9,S} {11,[S,D,T,B,Q]} {12,[S,D,T,B,Q]}
11   R!H ux {10,[S,D,T,B,Q]}
12   R!H ux {10,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.17194,-4.85996,-5.95926,-5.54068,-3.75194,-2.38905,-0.571621],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.7021,'kcal/mol','+|-',5.2),
        S298 = (-12.1329,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]C(CC)OOC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 541,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R_Ext-4C-R_Ext-5R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r0 {2,S} {4,S}
2    C ux r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3    O ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4    C ux {1,S} {6,S}
5    C ux {2,[S,D,T,B,Q]}
6    C u0 {4,S}
7    O ux {3,[S,D,T,B,Q]} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,D}
10   C u0 {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.776213,-3.24688,-4.75589,-5.13155,-5.07637,-5.05116,-4.20593],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.257,'kcal/mol','+|-',8.59646),
        S298 = (-8.45968,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 542,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R_Ext-4C-R_Ext-5R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-10R!H-9R!H_Ext-10R!H-R_Ext-10R!H-R",
    group = 
"""
1  * C   u1 r0 {2,S} {4,S}
2    C   ux r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3    O   ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4    C   ux {1,S} {6,S}
5    C   ux {2,[S,D,T,B,Q]}
6    C   u0 r0 {4,S}
7    O   ux {3,[S,D,T,B,Q]} {8,S}
8    C   u0 r1 {7,S} {9,[S,D,T,B,Q]}
9    C   ux r1 {8,[S,D,T,B,Q]} {10,D}
10   C   u0 r1 {9,D} {11,[S,D,T,B,Q]} {12,[S,D,T,B,Q]}
11   R!H ux {10,[S,D,T,B,Q]}
12   R!H ux {10,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.600264,-3.12594,-4.70395,-5.21884,-5.3292,-5.43674,-4.8363],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.2173,'kcal/mol','+|-',5.2),
        S298 = (-9.36023,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]C(CC)OOC1C=CCC(C)=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 543,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-3O-R",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.743358,0.315204,-0.644571,-1.77309,-3.41549,-4.64237,-5.98567],'cal/mol/K','+|-',[5.93594,8.31595,7.92243,6.8385,4.37711,3,3]),
        H298 = (99.7702,'kcal/mol','+|-',5.2),
        S298 = (3.36718,'cal/mol/K','+|-',5.81426),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 544,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-3O-R_Ext-4C-R_6R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   O ux {3,[S,D,T,B,Q]}
6   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.1625,-3.75575,-4.52288,-5.12078,-5.55823,-6.09378,-6.53099],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.161,'kcal/mol','+|-',5.2),
        S298 = (6.21347,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 545,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-3O-R_Ext-4C-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,S}
2   C                      ux r0 {1,S} {3,[S,T,Q,B]}
3   O                      ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C                      ux {1,S} {6,S}
5   O                      ux {3,[S,D,T,B,Q]}
6   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.03485,2.12452,1.07912,-0.285231,-2.46315,-3.99731,-5.7433],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.687,'kcal/mol','+|-',2.4),
        S298 = (2.10217,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 546,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_N-Sp-4C-1C",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C u0 r0 {1,S} {3,S}
3   O u0 {2,S}
4   C u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.44594,-1.89329,-1.99602,-2.01477,-2.10933,-2.31574,-3.23723],'cal/mol/K','+|-',[3,3,3,3,3,3.10077,3.30328]),
        H298 = (110.497,'kcal/mol','+|-',5.2),
        S298 = (1.32676,'cal/mol/K','+|-',3.56723),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 547,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C u0 r0 {1,S} {3,S}
3   O u0 {2,S}
4   C u0 {1,D} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.76938,-1.96243,-1.92978,-1.90376,-1.98746,-2.21101,-3.10245],'cal/mol/K','+|-',[2.12482,2,2,2,2.91916,3.79165,4.008]),
        H298 = (109.972,'kcal/mol','+|-',2.47321),
        S298 = (1.04017,'cal/mol/K','+|-',4.00652),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 548,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   u0 r0 {1,S} {3,S} {6,[S,D,T,B,Q]}
3   O   u0 r0 {2,S}
4   C   u0 r0 {1,D} {5,S}
5   C   u0 r0 {4,S}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.52062,-2.38532,-1.88614,-1.44621,-0.955382,-0.870456,-1.6854],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.097,'kcal/mol','+|-',2.4),
        S298 = (-0.376347,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(O)[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 549,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
4   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.64172,0.962568,0.0846463,-0.614936,-1.71637,-2.8026,-4.39464],'cal/mol/K','+|-',[4.85919,5.96682,5.79062,5.56303,5.3359,4.36823,3]),
        H298 = (95.429,'kcal/mol','+|-',6.21135),
        S298 = (-1.56991,'cal/mol/K','+|-',12.349),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 550,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.87321,3.30166,1.97976,1.0644,-0.317672,-1.88843,-4.10932],'cal/mol/K','+|-',[3,4.95005,6.25588,6.45319,6.72136,5.91578,3]),
        H298 = (95.0963,'kcal/mol','+|-',10.8706),
        S298 = (-6.68352,'cal/mol/K','+|-',9.16532),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 551,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   O ux {1,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.08802,3.70369,2.48511,1.61051,0.222894,-1.30341,-3.75142],'cal/mol/K','+|-',[3,5.73371,7.25085,7.43692,7.79435,6.65438,3]),
        H298 = (92.4833,'kcal/mol','+|-',5.2),
        S298 = (-8.12219,'cal/mol/K','+|-',8.73671),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 552,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R_5R!H->C_Sp-4O-1C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 r0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   O u0 r0 {2,S}
4   O u0 r0 {1,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.01099,7.00841,6.67108,5.90422,4.72046,2.53849,-2.08124],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.5408,'kcal/mol','+|-',5.2),
        S298 = (-12.7115,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 553,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R_5R!H->C_N-Sp-4O-1C",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C ux r0 {1,S} {3,[S,T,Q,B]} {5,S}
3   O ux {2,[S,T,Q,B]}
4   O ux {1,D}
5   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.62654,2.05134,0.392126,-0.536339,-2.02589,-3.22436,-4.58651],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.4557,'kcal/mol','+|-',5.2),
        S298 = (-5.82754,'cal/mol/K','+|-',5.12736),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 554,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R_5R!H->C_N-Sp-4O-1C_Ext-3O-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {5,S}
3   O   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   O   ux {1,D}
5   C   u0 r0 {2,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.41064,1.884,0.347667,-0.538745,-1.89587,-3.232,-4.77175],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.0391,'kcal/mol','+|-',5),
        S298 = (-7.64034,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC([C]=O)OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
""",
)

entry(
    index = 555,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C                      ux r0 {1,S} {3,[S,T,Q,B]} {5,S}
3   O                      ux {2,[S,T,Q,B]}
4   O                      ux {1,[S,D,T,B,Q]}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.22876,2.09556,0.463713,-0.573932,-1.93937,-3.64348,-5.18301],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.148,'kcal/mol','+|-',5.2),
        S298 = (-2.36751,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]C(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 556,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.476085,-0.449712,-1.28076,-1.98037,-2.97886,-3.7547,-4.90514],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.515,'kcal/mol','+|-',5.2),
        S298 = (2.14052,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH2]C(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH2]C(C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 557,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-3O-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,S}
5   C   u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.812216,-1.26731,-1.73493,-2.17551,-2.90075,-3.51687,-4.6261],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.194,'kcal/mol','+|-',5.2),
        S298 = (4.50263,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 558,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-3O-R_Ext-4R!H-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,S}
5   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39488,-1.7446,-2.16755,-2.58023,-3.20861,-3.83056,-5.07751],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.24,'kcal/mol','+|-',5.2),
        S298 = (3.38031,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 559,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-3O-R_Ext-4R!H-R_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,S}
5   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.553256,-1.05518,-1.54265,-1.99563,-2.76392,-3.37745,-4.42547],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.397,'kcal/mol','+|-',2.4),
        S298 = (5.00144,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]COOC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 560,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.154623,-0.603027,-1.29233,-1.9576,-2.76669,-3.3988,-4.61947],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.8634,'kcal/mol','+|-',11.4826),
        S298 = (2.70161,'cal/mol/K','+|-',8.50983),
    ),
    shortDesc = """Radical correction fitted to 40 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 561,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.170665,-1.00203,-1.67398,-2.30711,-3.00837,-3.5531,-4.62347],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.642,'kcal/mol','+|-',11.7673),
        S298 = (2.96302,'cal/mol/K','+|-',10.7728),
    ),
    shortDesc = """Radical correction fitted to 23 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 562,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0168981,-0.586988,-1.11468,-1.70639,-2.43346,-3.03694,-4.15946],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.6754,'kcal/mol','+|-',10.7482),
        S298 = (2.25823,'cal/mol/K','+|-',5.2895),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 563,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.128201,-0.278433,-0.801636,-1.3161,-2.17199,-2.87835,-4.04501],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.9033,'kcal/mol','+|-',8.25101),
        S298 = (1.80306,'cal/mol/K','+|-',4.70013),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 564,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_Sp-3C-2C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,S}
3   C u0 {2,S}
4   O ux {1,S} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.236804,-0.554114,-1.04975,-1.55386,-2.38516,-3.08215,-4.25151],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.0188,'kcal/mol','+|-',5.25445),
        S298 = (0.84697,'cal/mol/K','+|-',3.5216),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 565,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_Sp-3C-2C_Ext-5C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,S}
3   C   u0 r0 {2,S}
4   O   ux {1,S} {5,S}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.206306,0.00280813,-0.484774,-0.97093,-1.91591,-2.79242,-4.51632],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.624,'kcal/mol','+|-',2.4),
        S298 = (2.06716,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 566,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_Sp-3C-2C_Ext-3C-R",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S} {6,S}
4   O u0 {1,S} {5,S}
5   C u0 {4,S}
6   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.168314,-0.483292,-0.951377,-1.39621,-2.12258,-2.79706,-4.29429],'cal/mol/K','+|-',[4.16849,3.4575,3,3,3,3,3]),
        H298 = (94.1619,'kcal/mol','+|-',5.2),
        S298 = (-0.604226,'cal/mol/K','+|-',5.214),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 567,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_Sp-3C-2C_Ext-3C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {6,S}
4   O   u0 r0 {1,S} {5,S}
5   C   u0 r0 {4,S}
6   O   u0 r0 {3,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6421,-1.7057,-1.83389,-2.05916,-2.47919,-2.97017,-4.29328],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.1679,'kcal/mol','+|-',5.2),
        S298 = (1.2392,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CO[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 568,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_N-Sp-3C-2C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,T}
3   C   ux {2,T}
4   R!H u0 r0 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.18266,0.517981,-0.0848501,-0.629239,-1.55618,-2.2896,-3.44846],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.833,'kcal/mol','+|-',2.4),
        S298 = (4.56512,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 569,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C                      ux {1,S} {3,[S,T,Q,B]}
3   C                      u0 r0 {2,[S,T,Q,B]}
4   R!H                    ux {1,[S,D,T,B,Q]} {5,S}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.957004,-3.28685,-3.85383,-5.12143,-4.72135,-4.42461,-5.16088],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.783,'kcal/mol','+|-',5.2),
        S298 = (6.2409,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 570,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.608045,-2.49449,-3.82546,-4.45599,-4.61365,-4.56994,-5.29063],'cal/mol/K','+|-',[4.9586,3.73306,3,3,3,3,3.4134]),
        H298 = (97.169,'kcal/mol','+|-',5.2),
        S298 = (14.8826,'cal/mol/K','+|-',24.6446),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 571,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-1C-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,S} {6,[S,D,T,B,Q]}
3   C   u0 {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.666893,-1.51139,-3.20027,-3.95052,-4.08836,-3.99025,-4.85969],'cal/mol/K','+|-',[3.18815,3,3,3,3,3,4.34113]),
        H298 = (97.5315,'kcal/mol','+|-',5.81022),
        S298 = (16.0317,'cal/mol/K','+|-',34.3951),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 572,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-1C-R_Ext-2C-R_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,S} {6,[S,D,T,B,Q]}
3   C   u0 r0 {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.79407,-0.746857,-2.34822,-3.24767,-3.66704,-3.48603,-3.32486],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.4773,'kcal/mol','+|-',5.2),
        S298 = (28.1922,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 573,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,S}
3   C   ux {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.350588,-1.18475,-1.88573,-2.49863,-3.25361,-3.84174,-4.82926],'cal/mol/K','+|-',[3.12407,3,3,3,3,3,3]),
        H298 = (93.9387,'kcal/mol','+|-',7.57093),
        S298 = (1.89254,'cal/mol/K','+|-',4.07847),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 574,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,S}
3   C   ux {2,S}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21188,-1.57637,-2.03378,-2.43251,-3.05472,-3.6053,-4.6827],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.5006,'kcal/mol','+|-',5.26743),
        S298 = (2.22346,'cal/mol/K','+|-',4.03967),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 575,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_Sp-4R!H-1C_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S}
4   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72513,-2.44086,-2.95635,-3.337,-3.83706,-4.20764,-4.95114],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.2786,'kcal/mol','+|-',5.2),
        S298 = (4.24166,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 576,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_Sp-4R!H-1C_4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 {2,S}
4   C   u0 r0 {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.637796,-2.08524,-3.12532,-3.80312,-4.49437,-4.94833,-5.9195],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.5201,'kcal/mol','+|-',5.2),
        S298 = (4.5675,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 577,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_Sp-4R!H-1C_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,S}
3   C ux r0 {2,S}
4   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.841195,-0.952015,-1.36748,-1.77927,-2.48969,-3.17029,-4.48884],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (94.8158,'kcal/mol','+|-',2.4),
        S298 = (0.765879,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
O[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 578,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C ux {1,S} {3,S}
3   C ux {2,S}
4   O ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.371033,-0.856638,-1.76169,-2.55402,-3.42026,-4.03984,-4.95205],'cal/mol/K','+|-',[3.28578,3,3,3,3,3,3]),
        H298 = (90.6343,'kcal/mol','+|-',5.2),
        S298 = (1.61527,'cal/mol/K','+|-',4.4381),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 579,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   ux {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C   ux {2,S}
4   O   ux {1,D}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.50215,-1.8298,-2.0198,-2.28816,-2.98613,-3.60936,-4.69598],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (89.6988,'kcal/mol','+|-',2.4),
        S298 = (1.34764,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 580,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   ux {1,S} {3,S}
3   C   ux {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   O   ux {1,D}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.724308,-0.705894,-1.99156,-2.76678,-3.61048,-4.24905,-5.08756],'cal/mol/K','+|-',[3.07379,3.26426,3.25432,3,3,3,3]),
        H298 = (90.2455,'kcal/mol','+|-',5.2),
        S298 = (2.23866,'cal/mol/K','+|-',6.21278),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 581,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Ext-3C-R_5R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {5,[S,D,T,B,Q]} {6,S}
4   O   u0 {1,D}
5   O   u0 {3,[S,D,T,B,Q]}
6   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.9902,-0.175021,-1.42998,-2.23637,-3.19048,-3.87477,-5.27304],'cal/mol/K','+|-',[3.53206,3.03632,3,3,3,3,3]),
        H298 = (90.0155,'kcal/mol','+|-',5.2),
        S298 = (0.772553,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 582,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Ext-3C-R_5R!H->O_3C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
4   O   u0 r0 {1,D}
5   O   u0 {3,[S,D,T,B,Q]}
6   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.831417,-1.77274,-3.03323,-3.48605,-3.84759,-4.3915,-6.48467],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.1868,'kcal/mol','+|-',5.2),
        S298 = (2.12889,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]CC1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 583,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Ext-3C-R_5R!H->O_N-3C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {5,[S,D,T,B,Q]} {6,S}
4   O   u0 r0 {1,D}
5   O   u0 {3,[S,D,T,B,Q]}
6   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.90101,0.623839,-0.628347,-1.61153,-2.86193,-3.61641,-4.66722],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.4298,'kcal/mol','+|-',5.2),
        S298 = (0.0943839,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 584,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Ext-3C-R_N-5R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   ux {1,S} {3,S}
3   C   ux {2,S} {5,S} {6,[S,D,T,B,Q]}
4   O   ux {1,D}
5   C   ux {3,S}
6   R!H u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0733667,-2.29852,-3.67629,-4.358,-4.8705,-5.37188,-4.53112],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.9357,'kcal/mol','+|-',5.2),
        S298 = (6.637,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(=C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 585,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Sp-5R!H-3C",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C u0 r0 {1,S} {3,S}
3   C u0 {2,S} {5,S}
4   O u0 r0 {1,D}
5   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.610302,-0.416678,-1.32567,-2.12838,-3.25032,-3.90592,-5.37158],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.1838,'kcal/mol','+|-',5.2),
        S298 = (-0.0509083,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
C#CCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 586,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_N-Sp-5R!H-3C",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C u0 r0 {1,S} {3,S}
3   C u0 {2,S} {5,[B,D,T,Q]}
4   O u0 r0 {1,D}
5   C u0 r0 {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.69406,-0.149915,-1.13349,-3.15244,-3.97601,-4.43942,-4.14707],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.4825,'kcal/mol','+|-',5.2),
        S298 = (3.05623,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC#CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 587,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_N-Sp-3C-2C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 {1,S} {3,T}
3   C   u0 {2,T}
4   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.611521,0.0862996,-0.258317,-1.12388,-1.96849,-2.65312,-4.32327],'cal/mol/K','+|-',[3,3.26657,3.1444,4.44682,3.43015,3,3]),
        H298 = (83.8854,'kcal/mol','+|-',5.2),
        S298 = (-0.325863,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 588,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_N-Sp-3C-2C_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,T}
3   C   u0 r0 {2,T} {5,[S,D,T,B,Q]}
4   R!H u0 r0 {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.147574,-1.5128,-1.79761,-3.30076,-3.64767,-3.80616,-5.52932],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.1051,'kcal/mol','+|-',5.2),
        S298 = (-0.805385,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC#C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 589,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,S}
3   C ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.534341,-0.119461,-0.884336,-1.52564,-2.48186,-3.24118,-4.60399],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.054,'kcal/mol','+|-',5.2),
        S298 = (2.50245,'cal/mol/K','+|-',4.47889),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 590,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r1 {1,S} {3,S}
3   C ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.586767,0.107832,-0.57919,-1.21995,-2.30076,-3.11446,-4.45416],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.8556,'kcal/mol','+|-',5.2),
        S298 = (2.34872,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 591,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing_Ext-3C-R_Int-4R!H-2C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r1 {1,S} {3,S} {4,S}
3   C ux {2,S} {4,[S,D,T,B,Q]}
4   C ux {2,S} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.704299,0.354055,-0.357904,-1.0208,-2.06941,-2.89707,-4.39002],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.8804,'kcal/mol','+|-',5.2),
        S298 = (2.57288,'cal/mol/K','+|-',3.33261),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 592,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing_Ext-3C-R_Int-4R!H-2C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,S} {4,S} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,S} {4,[S,D,T,B,Q]}
4   C   ux r1 {2,S} {3,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.862383,0.358923,-0.372729,-1.02741,-2.12738,-2.98511,-4.33145],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.5806,'kcal/mol','+|-',2.4),
        S298 = (2.99827,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 593,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing_Ext-3C-R_Int-4R!H-2C_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   C   u0 {2,S} {4,S} {5,D}
4   C   u0 {2,S} {3,S}
5   R!H u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.949378,0.585372,-0.189007,-0.897682,-2.02439,-2.88166,-4.39898],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.6513,'kcal/mol','+|-',5.2),
        S298 = (2.0621,'cal/mol/K','+|-',5.66764),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 594,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing_Ext-3C-R_Int-4R!H-2C_Ext-3C-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   C u0 r1 {2,S} {4,S} {5,D}
4   C u0 r1 {2,S} {3,S}
5   C u0 r0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.38416,0.437858,-0.780884,-1.55172,-2.58175,-3.26654,-4.85665],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.9721,'kcal/mol','+|-',5.2),
        S298 = (4.83661,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 595,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing_Ext-3C-R_Int-4R!H-2C_Ext-3C-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      u0 r1 {1,S} {3,S} {4,S}
3   C                      u0 r1 {2,S} {4,S} {5,D}
4   C                      u0 r1 {2,S} {3,S}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.756141,0.650934,0.0740492,-0.606996,-1.77668,-2.71061,-4.19558],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.0089,'kcal/mol','+|-',2.4),
        S298 = (0.828984,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 596,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,S}
3   C ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.485262,-0.332246,-1.17001,-1.81182,-2.6514,-3.35981,-4.74426],'cal/mol/K','+|-',[3.75573,3.87137,3.67823,3.69175,3.42116,3.18785,3]),
        H298 = (102.36,'kcal/mol','+|-',5.2),
        S298 = (2.64638,'cal/mol/K','+|-',6.00922),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 597,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,S}
3   C   ux {2,S} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.683015,-0.180005,-1.09575,-1.79693,-2.65779,-3.36466,-4.80026],'cal/mol/K','+|-',[4.11252,4.29319,4.12613,4.15742,3.85318,3.59045,3]),
        H298 = (102.508,'kcal/mol','+|-',5.2),
        S298 = (2.37049,'cal/mol/K','+|-',6.6257),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 598,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,S}
3   C   ux {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.90619,0.864823,-0.339912,-1.23194,-2.20111,-2.98168,-4.40317],'cal/mol/K','+|-',[5.66142,6.54057,6.63775,6.88119,6.47116,6.08509,4.21792]),
        H298 = (102.091,'kcal/mol','+|-',5.2),
        S298 = (-0.221831,'cal/mol/K','+|-',6.19051),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 599,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,S}
3   C   ux r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.329258,-2.19057,-4.03189,-5.22154,-5.83838,-6.37249,-6.95002],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.037,'kcal/mol','+|-',5.2),
        S298 = (0.735312,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)(C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 600,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,S} {6,[S,D,T,B,Q]}
3   C   ux {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.87087,5.07784,3.51581,2.60359,1.52221,0.547265,-2.17132],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.9688,'kcal/mol','+|-',5.2),
        S298 = (-4.55832,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(N(CC)O)C(C=C)[CH2] - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 601,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0825081,-0.899952,-1.63365,-2.20942,-3.02619,-3.70592,-4.98581],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.061,'kcal/mol','+|-',5.2),
        S298 = (5.42678,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 602,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.236492,-0.803701,-1.33821,-1.83838,-2.73093,-3.47554,-4.70464],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.355,'kcal/mol','+|-',2.4),
        S298 = (5.93036,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)(C=C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 603,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_N-Sp-3C-2C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,T}
3   C ux {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.647777,-0.0934156,-0.51293,-1.55605,-2.41483,-3.0445,-4.6712],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.6445,'kcal/mol','+|-',5.47105),
        S298 = (1.73792,'cal/mol/K','+|-',7.25754),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 604,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_N-Sp-3C-2C_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,T}
3   C   ux {2,T} {4,S}
4   C   u0 r0 {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.02705,-0.0597769,-0.256026,-1.85098,-2.60708,-3.08361,-5.1059],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.7997,'kcal/mol','+|-',5.2),
        S298 = (-1.24475,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C#CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 605,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S}
2   C   ux {1,S}
3   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.612006,-1.651,-2.29909,-2.81527,-3.57731,-4.13418,-4.88715],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.696,'kcal/mol','+|-',5.2),
        S298 = (3.13473,'cal/mol/K','+|-',5.54722),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 606,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C_3R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   C ux {1,S}
3   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.31057,-3.5947,-3.86755,-4.074,-4.39412,-4.62355,-4.99874],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.1592,'kcal/mol','+|-',2.4),
        S298 = (7.00981,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 607,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C_N-3R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   C u0 {1,S}
3   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.175232,-1.15119,-1.89577,-2.49159,-3.36728,-4.00835,-4.85846],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.5608,'kcal/mol','+|-',5.2),
        S298 = (2.13828,'cal/mol/K','+|-',3.95882),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 608,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C_N-3R!H->C_Ext-3O-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S}
2   C   u0 {1,S}
3   O   u0 {1,S} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.131636,-1.25633,-2.09275,-2.72374,-3.62703,-4.27708,-5.0454],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.1069,'kcal/mol','+|-',5.2),
        S298 = (2.53853,'cal/mol/K','+|-',4.41035),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 609,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C_N-3R!H->C_Ext-3O-R_Ext-1C-R",
    group = 
"""
1 * C u1 r0 {2,S} {3,S} {5,S}
2   C u0 {1,S}
3   O u0 {1,S} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
5   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0501921,-1.46216,-2.5492,-3.22714,-4.0687,-4.69445,-5.16196],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.0816,'kcal/mol','+|-',5.2),
        S298 = (2.48438,'cal/mol/K','+|-',8.02255),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 610,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C_N-3R!H->C_Ext-3O-R_Ext-1C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S} {5,S}
2   C   u0 {1,S}
3   O   u0 r0 {1,S} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   u0 r0 {1,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.14476,-0.1135,-1.60363,-2.25978,-2.88003,-3.77486,-4.63923],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.6289,'kcal/mol','+|-',5.2),
        S298 = (-1.44294,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCCCO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 611,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-3R!H-1C",
    group = 
"""
1 * C u1 r0 {2,S} {3,[B,D,T,Q]}
2   C u0 {1,S}
3   C u0 {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0424032,-0.944458,-1.65386,-2.13791,-2.90302,-3.57386,-4.56582],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (109.647,'kcal/mol','+|-',5.2),
        S298 = (1.99512,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 612,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-3R!H-1C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,D}
2   C   u0 {1,S}
3   C   u0 {1,D} {4,S}
4   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.180531,-0.994029,-1.75785,-2.24012,-3.00873,-3.68365,-4.67319],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.309,'kcal/mol','+|-',5.2),
        S298 = (2.14593,'cal/mol/K','+|-',3.60349),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 613,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-3R!H-1C_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,D}
2   C u0 {1,S}
3   C u0 r0 {1,D} {4,S}
4   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.861627,-2.13209,-2.47702,-2.25093,-2.03486,-2.43756,-3.65317],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.881,'kcal/mol','+|-',5.2),
        S298 = (0.38189,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC=CC=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 614,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-3R!H-1C_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {3,D}
2   C                      u0 {1,S}
3   C                      u0 r0 {1,D} {4,S}
4   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.643713,-0.488226,-1.43823,-2.23531,-3.44156,-4.23747,-5.12654],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (111.4,'kcal/mol','+|-',2.4),
        S298 = (2.92994,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 615,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.507144,-0.378524,-1.21212,-1.88701,-2.925,-3.67771,-4.84253],'cal/mol/K','+|-',[4.01734,4.00188,3.58066,3.09893,3,3,3]),
        H298 = (101.411,'kcal/mol','+|-',14.3755),
        S298 = (2.4976,'cal/mol/K','+|-',5.22592),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 616,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,[S,D,T,B,Q]}
2   O   ux {1,S}
3   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.282074,-0.593019,-1.47463,-2.18772,-3.21681,-3.92624,-4.88669],'cal/mol/K','+|-',[4.06375,4.15184,3.78388,3.43228,3,3,3]),
        H298 = (104.521,'kcal/mol','+|-',16.2289),
        S298 = (2.14996,'cal/mol/K','+|-',5.92679),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 617,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,[S,D,T,B,Q]}
2   O ux {1,S}
3   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.231013,-0.772799,-1.62456,-2.27286,-3.24669,-3.92788,-4.87592],'cal/mol/K','+|-',[3.15708,3,3,3,3,3,3]),
        H298 = (107.157,'kcal/mol','+|-',16.5321),
        S298 = (2.34578,'cal/mol/K','+|-',5.66422),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 618,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C_Ext-3C-R_Sp-4R!H-3C",
    group = 
"""
1 * C u1 r0 {2,S} {3,[S,D,T,B,Q]}
2   O ux {1,S}
3   C ux {1,[S,D,T,B,Q]} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0978293,-0.729673,-1.52162,-2.19325,-3.24251,-4.00625,-5.12936],'cal/mol/K','+|-',[3.66509,3,3,3,3,3,3]),
        H298 = (111.019,'kcal/mol','+|-',5.99469),
        S298 = (1.78639,'cal/mol/K','+|-',6.08388),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 619,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,D}
2   O   u0 r0 {1,S}
3   C   ux {1,D} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.78275,1.9361,0.565081,-0.314472,-1.62734,-2.7263,-5.02067],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (116.245,'kcal/mol','+|-',5.2),
        S298 = (-3.78174,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)O[C]=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 620,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C_Ext-3C-R_Sp-4R!H-3C_Ext-2O-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,[S,D,T,B,Q]}
2   O   ux {1,S} {5,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.250959,-0.662519,-1.76439,-2.71321,-4.17728,-5.17136,-6.31703],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.716,'kcal/mol','+|-',2.4),
        S298 = (4.67272,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)O[C]=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 621,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,[S,D,T,B,Q]}
2   O   ux {1,S}
3   C   ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.170019,-0.587629,-1.16579,-1.76222,-2.72597,-3.42935,-4.43543],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.12,'kcal/mol','+|-',2.4),
        S298 = (0.843186,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 622,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C_Ext-3C-R_N-Sp-4R!H-3C",
    group = 
"""
1 * C u1 r0 {2,S} {3,[S,D,T,B,Q]}
2   O ux {1,S}
3   C u0 r0 {1,[S,D,T,B,Q]} {4,[B,D,T,Q]}
4   C u0 r0 {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.689759,-0.921343,-1.97913,-2.5471,-3.26109,-3.65793,-4.00295],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (94.7478,'kcal/mol','+|-',2.4),
        S298 = (4.27255,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 623,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_N-3R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,[S,D,T,B,Q]}
2   O u0 {1,S}
3   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.379333,-0.250581,-1.18905,-2.02553,-3.1599,-3.92311,-4.90721],'cal/mol/K','+|-',[6.16792,6.9536,6.52055,5.96275,4.62097,3.47813,3]),
        H298 = (97.7477,'kcal/mol','+|-',5.2),
        S298 = (1.77696,'cal/mol/K','+|-',7.53806),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 624,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_N-3R!H->C_Ext-2O-R",
    group = 
"""
1 * C u1 r0 {2,S} {3,[S,D,T,B,Q]}
2   O u0 {1,S} {4,[S,D,T,B,Q]}
3   O ux {1,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.40009,0.862057,-0.181192,-1.13138,-2.53972,-3.56775,-5.03183],'cal/mol/K','+|-',[7.48761,8.5127,8.04613,7.40518,5.85419,4.54957,3.59864]),
        H298 = (98.0714,'kcal/mol','+|-',5.2),
        S298 = (0.148655,'cal/mol/K','+|-',8.2709),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 625,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_N-3R!H->C_Ext-2O-R_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,[S,D,T,B,Q]}
2   O   u0 r0 {1,S} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.68528,5.76464,4.45847,3.14048,0.837071,-0.946603,-2.95487],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.3419,'kcal/mol','+|-',5.2),
        S298 = (-4.53445,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]OC(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 626,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R",
    group = 
"""
1 * C u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.830752,-0.183305,-1.04164,-1.70218,-2.76554,-3.56348,-4.95613],'cal/mol/K','+|-',[4.69518,4.54789,3.85504,3,3,3,3.33671]),
        H298 = (98.1757,'kcal/mol','+|-',9.85608),
        S298 = (3.21295,'cal/mol/K','+|-',4.86337),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 627,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17543,-0.0117321,-1.02689,-1.75711,-2.87123,-3.69516,-5.1367],'cal/mol/K','+|-',[5.10676,5.13976,4.41345,3.34681,3,3,3.71778]),
        H298 = (98.493,'kcal/mol','+|-',11.6935),
        S298 = (3.36939,'cal/mol/K','+|-',5.51612),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 628,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D]} {5,[S,D]}
4   R!H ux {3,[S,D]}
5   C   u0 {3,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.590881,-1.84371,-2.61034,-2.93583,-3.34815,-3.58323,-4.01218],'cal/mol/K','+|-',[3,3.14379,3.02196,3,3,3,3]),
        H298 = (103.056,'kcal/mol','+|-',12.492),
        S298 = (3.03755,'cal/mol/K','+|-',5.94066),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 629,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,[S,D]} {5,[S,D]}
4   O ux {3,[S,D]}
5   C u0 r0 {3,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0699759,-0.89953,-1.82619,-2.36441,-3.18538,-3.76822,-4.60605],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (100.392,'kcal/mol','+|-',2.4),
        S298 = (3.89889,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]OC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 630,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,[S,D]} {5,[S,D]}
4   C ux {3,[S,D]}
5   C u0 {3,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.33435,-2.90591,-3.49251,-3.57869,-3.53128,-3.37511,-3.34408],'cal/mol/K','+|-',[3,3,3.44623,3.31666,3,3,3]),
        H298 = (109.309,'kcal/mol','+|-',6.18667),
        S298 = (2.06855,'cal/mol/K','+|-',8.78373),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 631,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R_N-4R!H->O_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,D}
4   C   ux {3,S}
5   C   u0 r0 {3,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904944,-1.87324,-2.27408,-2.40607,-2.64255,-2.68012,-2.52329],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.122,'kcal/mol','+|-',5.2),
        S298 = (-1.03696,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]OC(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 632,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 r0 {3,[S,D,T,B,Q]} {5,S}
5   R!H u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.63333,3.11589,1.52741,0.0644305,-2.42559,-4.40951,-7.68448],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (94.7108,'kcal/mol','+|-',2),
        S298 = (6.11948,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]OCC(C)OO - Radical thermo from johnson_g4.py and closed shell thermo from Thermo library: johnson_g4.py
""",
)

entry(
    index = 633,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C",
    group = 
"""
1 * C u1 r0 {2,[B,D,T,Q]}
2   C ux {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.139453,-0.480019,-1.08903,-1.62043,-2.49744,-3.13764,-4.13991],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.842,'kcal/mol','+|-',24.2591),
        S298 = (2.42557,'cal/mol/K','+|-',11.4198),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 634,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.236335,-0.36027,-0.975057,-1.51869,-2.42189,-3.08137,-4.11303],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.819,'kcal/mol','+|-',18.2657),
        S298 = (2.52775,'cal/mol/K','+|-',12.0934),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 635,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux {1,D} {3,S}
3   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0354956,-0.502574,-1.07157,-1.59098,-2.50657,-3.20799,-4.30414],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.745,'kcal/mol','+|-',5.2),
        S298 = (0.752023,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 636,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_2R!H-inRing",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux r1 {1,D} {3,S}
3   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.877802,-0.138985,-1.05589,-1.69231,-2.76246,-3.58047,-4.56535],'cal/mol/K','+|-',[4.38594,3,3,3,3,3,3]),
        H298 = (107.117,'kcal/mol','+|-',5.97916),
        S298 = (0.0420148,'cal/mol/K','+|-',4.7705),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 637,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_2R!H-inRing_Ext-3R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux r1 {1,D} {3,S} {5,S}
3   R!H u0 {2,S} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.14388,0.0750095,-0.929814,-1.59416,-2.76116,-3.64439,-4.53418],'cal/mol/K','+|-',[5.75617,3,3,3,3,3,3]),
        H298 = (107.747,'kcal/mol','+|-',5.53333),
        S298 = (-0.845446,'cal/mol/K','+|-',3.33369),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 638,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_2R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_3R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux r1 {1,D} {3,S} {5,S}
3   O u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.96172,1.42654,-0.612549,-1.49759,-3.16381,-4.40072,-4.75842],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.972,'kcal/mol','+|-',5.2),
        S298 = (-2.47741,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C1OOC(C)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 639,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_2R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_N-3R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux r1 {1,D} {3,S} {5,S}
3   C u0 r1 {2,S} {4,D}
4   O ux {3,D}
5   C u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.108501,-0.525669,-1.07082,-1.63708,-2.5822,-3.30825,-4.43451],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (107.06,'kcal/mol','+|-',2.4),
        S298 = (-0.12013,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 640,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux r0 {1,D} {3,S}
3   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.103526,-0.562584,-1.07416,-1.57426,-2.46434,-3.14651,-4.26103],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (112.334,'kcal/mol','+|-',5.2),
        S298 = (0.869208,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 641,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_N-2R!H-inRing_3R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux r0 {1,D} {3,S}
3   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.143377,-0.561758,-0.954487,-1.36232,-2.20379,-2.93179,-4.056],'cal/mol/K','+|-',[2.35008,2.17709,2,2,2,2,2]),
        H298 = (114.007,'kcal/mol','+|-',2.4),
        S298 = (0.438465,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 642,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_N-2R!H-inRing_3R!H->O_Ext-3O-R",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux r0 {1,D} {3,S}
3   O u0 {2,S} {4,S}
4   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.362331,-0.359289,-0.895586,-1.36224,-2.36109,-3.20177,-4.19699],'cal/mol/K','+|-',[3.52479,3.54733,3.02411,2.57715,2.18476,2,2]),
        H298 = (114.464,'kcal/mol','+|-',2.4),
        S298 = (-0.0463727,'cal/mol/K','+|-',2.60944),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 643,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_N-2R!H-inRing_3R!H->O_Ext-3O-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux r0 {1,D} {3,S} {5,[S,D,T,B,Q]}
3   O   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.60853,0.894882,0.173598,-0.451082,-1.58866,-2.65347,-3.93077],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.793,'kcal/mol','+|-',2.4),
        S298 = (-0.968951,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 644,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_N-2R!H-inRing_N-3R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux r0 {1,D} {3,S}
3   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0821134,-0.563028,-1.13846,-1.68814,-2.60433,-3.26189,-4.37119],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.406,'kcal/mol','+|-',5.2),
        S298 = (1.10065,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C(CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CC(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CCC#C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 645,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux {1,D} {3,[B,D,T,Q]}
3   C u0 {2,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.03969,0.208949,-0.589003,-1.22949,-2.08315,-2.57487,-3.3486],'cal/mol/K','+|-',[3,3,3,3,3,3,3.32374]),
        H298 = (89.0151,'kcal/mol','+|-',5.2),
        S298 = (9.63067,'cal/mol/K','+|-',23.4197),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 646,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux {1,D} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.1591,0.211849,-0.636898,-1.2466,-1.96367,-2.2905,-2.85696],'cal/mol/K','+|-',[3,3,3,3,3,3,3.54212]),
        H298 = (88.4014,'kcal/mol','+|-',5.2),
        S298 = (13.1741,'cal/mol/K','+|-',24.748),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 647,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux {1,D} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.25549,-0.022545,-0.859437,-1.23055,-1.35678,-1.25636,-1.54388],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.7274,'kcal/mol','+|-',5.2),
        S298 = (22.5754,'cal/mol/K','+|-',4.53669),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 648,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux {1,D} {3,D}
3   C   u0 {2,D} {4,S} {6,[S,D,T,B,Q]}
4   C   u0 r0 {3,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.472227,-0.699621,-1.52225,-1.70103,-1.4645,-1.14718,-1.2681],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.5785,'kcal/mol','+|-',5.2),
        S298 = (24.1794,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C=C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 649,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux {1,D} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09979,0.356091,-0.499951,-1.25648,-2.33713,-2.92689,-3.66501],'cal/mol/K','+|-',[4.37373,4.10765,3.83175,3.41704,3.15656,3.64265,4.13824]),
        H298 = (87.9356,'kcal/mol','+|-',5.2),
        S298 = (7.38864,'cal/mol/K','+|-',28.3401),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 650,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_Sp-5BrClFINOPSSi-4R!H",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux {1,D} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 r0 {3,S} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.24089,2.36693,1.37583,0.416276,-0.791888,-1.14369,-1.63919],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.0354,'kcal/mol','+|-',5.2),
        S298 = (21.2621,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 651,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-4R!H",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux {1,D} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 r0 {3,S} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.148191,-0.537616,-1.33363,-1.99993,-3.02391,-3.71943,-4.56537],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (87.4884,'kcal/mol','+|-',2.4),
        S298 = (1.22265,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 652,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_N-Sp-2R!H=1C",
    group = 
"""
1 * C u1 r0 {2,T}
2   C u0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.667902,-1.47793,-2.03883,-2.46826,-3.12707,-3.60662,-4.36391],'cal/mol/K','+|-',[2.02644,2,2,2,2,2,2]),
        H298 = (133.933,'kcal/mol','+|-',2.4),
        S298 = (1.57405,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 653,
    label = "RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_N-Sp-2R!H=1C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,T}
2   C   u0 r0 {1,T} {3,[S,D,T,B,Q]}
3   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.38436,-2.02874,-2.31305,-2.54584,-2.9761,-3.36561,-4.19473],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (134.66,'kcal/mol','+|-',2.4),
        S298 = (0.911082,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[C]#CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_1R-inRing
            L4: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_5R!H->O
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-1R-R_Ext-5CN-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-1R-R_Ext-5CN-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-1R-R_Ext-5CN-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H_Ext-3R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-1R-R_Ext-5CN-R_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_Ext-3R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O_Ext-1R-R_Ext-5O-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O_Ext-1R-R_Ext-5O-R_7R!H->N
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O_Ext-1R-R_Ext-5O-R_N-7R!H->N
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_5R!H->O_Ext-1R-R_Ext-5O-R_N-7R!H->N_Ext-1R-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_Int-6R!H-4R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_Int-6R!H-4R!H_Ext-6R!H-R_Ext-7R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R_Ext-6C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R_Ext-6C-R_Sp-7R!H-6C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R_Ext-6C-R_Sp-7R!H-6C_Ext-6C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Int-6C-1R_Ext-6C-R_N-Sp-7R!H-6C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_6R!H->C_N-4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H-5C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H-5C_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-1R-R_N-Sp-5R!H=4R!H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H-5C_Ext-2R!H-R_Ext-1R-R
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_2R!H-inRing
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R_4R!H->O
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R_N-4R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R_N-4R!H->O_6R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R_N-4R!H->O_6R!H->O_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-4R!H-R_N-4R!H->O_N-6R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-2R!H-inRing_Ext-2R!H-R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-3R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-3R!H-R_4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Ext-4C-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_4R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4C-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4C-R_3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4C-R_N-3R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4BrClFINOPSSi-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4BrClFINOPSSi-R_Ext-5R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4BrClFINOPSSi-R_3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4BrClFINOPSSi-R_N-3R!H->C
            L4: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-2R!H-R
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_Ext-1R-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_Ext-2R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_3R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_N-3R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_Sp-4R!H-3R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_Sp-4R!H-3R!H_Ext-3R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_Sp-4R!H-3R!H_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_Sp-4R!H-3R!H_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_Sp-4R!H-3R!H_N-4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-1R-R_Int-5R!H-4R!H_N-Sp-4R!H-3R!H
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-1R-R_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-1R-R_Ext-3R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-6R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-6R!H-R_4R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-6R!H-R_4R!H->C_Ext-3R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-1R-R_Ext-6R!H-R_N-4R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_5R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_N-5R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_N-3R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->O
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->O_Int-5R!H-4O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->O_Int-5R!H-4O_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->O_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->O_Ext-2C-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->O
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->O_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->O_Ext-2C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->O_Ext-2C-R_Ext-7R!H-R_Int-8R!H-6BrCClFINPSSi_Int-8R!H-7R!H_8R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_4R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->O_Ext-2C-R_Ext-7R!H-R_Int-8R!H-6BrCClFINPSSi_Int-8R!H-7R!H_N-8R!H-inRing
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-2C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-1R-R_Ext-6R!H-R_Ext-7R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-1R-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-1R-R_Ext-6R!H-R_Ext-7R!H-R_Ext-4BrCClFINPSSi-R
        L3: RJ1_N-1R-inRing
            L4: RJ1_N-1R-inRing_1R->O
                L5: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C
                    L6: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_5R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_5R!H->C_Ext-2C-R
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_N-5R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_N-5R!H->C_Ext-4R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-2C-R_N-5R!H->C_Ext-3C-R
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-3C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-3C-R_5R!H->C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-3C-R_N-5R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_4C-inRing
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_N-4C-inRing
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-5R!H-R_Ext-5R!H-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R_6R!H->C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R_N-6R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C_Ext-3C-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_3C-inRing
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_N-3C-inRing
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_4R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_4R!H->C_6R!H->O
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_4R!H->C_N-6R!H->O
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-4R!H->C
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_4R!H-inRing
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R_Sp-5R!H-4C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R_N-Sp-5R!H-4C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C_Ext-4C-R_Ext-5R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_N-4R!H->C
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C
                    L6: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_4R!H->O
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-4O_Int-6R!H-5R!H_6R!H->O
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-4O_Int-6R!H-5R!H_6R!H->O_6O-inRing
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-4O_Int-6R!H-5R!H_6R!H->O_N-6O-inRing
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-4O_Int-6R!H-5R!H_N-6R!H->O
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_N-4R!H->O
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2C-R_Ext-2C-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2C-R_Ext-2C-R_3R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2C-R_Ext-2C-R_N-3R!H->C
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-4R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-4R!H-R_Ext-5R!H-R
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_Ext-2C-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_Ext-2C-R_4R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_Ext-2C-R_N-4R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_4R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_4R!H->C_Ext-3R!H-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_4R!H->C_Ext-3R!H-R_Ext-5R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_N-4R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_N-4R!H->C_Ext-3R!H-R
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-4R!H-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-3R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_5R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_5R!H->C_Ext-5C-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_N-5R!H->C
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_Ext-2C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_3R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_N-3R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-5R!H-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C_Ext-3R!H-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C_3R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C_N-3R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-4R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-4R!H->C_Ext-2C-R
                L5: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C
                    L6: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->O
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->O_Ext-3R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->O
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-7R!H-R_Ext-8R!H-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_3R!H-inRing
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_N-3R!H-inRing
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Sp-4O-3R!H
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-Sp-4O-3R!H
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H-5C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Sp-4O-3R!H
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Sp-4O-3R!H_Ext-5C-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Sp-4O-3R!H_Ext-5C-R_Ext-3R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-Sp-4O-3R!H
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_Ext-3R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_Sp-4O-3R!H
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-4O-3R!H
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_N-5R!H->C
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_6R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_6R!H->C_3R!H-inRing
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_6R!H->C_N-3R!H-inRing
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Int-8R!H-3R!H
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Int-8R!H-3R!H_Ext-3R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Ext-7R!H-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Ext-7R!H-R_3R!H-inRing
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Ext-7R!H-R_3R!H-inRing_Ext-3R!H-R
                                                                L17: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Ext-7R!H-R_3R!H-inRing_Ext-3R!H-R_Ext-10R!H-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Ext-7R!H-R_N-3R!H-inRing
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Int-8R!H-4BrCClFINPSSi_Sp-8R!H-4BrCClFINPSSi
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Int-8R!H-4BrCClFINPSSi_Sp-8R!H-4BrCClFINPSSi_Ext-4BrCClFINPSSi-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_Int-8R!H-4BrCClFINPSSi_N-Sp-8R!H-4BrCClFINPSSi
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-8R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_5O-inRing_Ext-5O-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-8R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_5R!H->O_N-5O-inRing
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi_Ext-5BrCClFINPSSi-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi_Ext-5BrCClFINPSSi-R_6R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi_Ext-5BrCClFINPSSi-R_N-6R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_N-Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_3R!H-inRing_N-Sp-5BrCClFINPSSi-4BrBrCCClClFFIINNPPSSSiSi_Ext-5BrCClFINPSSi-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5BrCClFINPSSi_Int-7R!H-6R!H_Int-7R!H-3R!H_Ext-7R!H-R_Int-7R!H-6R!H_Ext-6R!H-R_Ext-8R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_N-5R!H->O_N-3R!H-inRing
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4BrCClFINPSSi-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-8R!H-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-4BrCClFINPSSi-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_7R!H->C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_N-7R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_N-7R!H->C_Ext-4BrCClFINPSSi-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-5R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-5R!H-R_7R!H->C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-5R!H-R_N-7R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_Ext-6R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_6R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_N-6R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_Ext-6O-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_Ext-6O-R_7R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_Ext-6O-R_7R!H->C_Ext-7C-R_Ext-7C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_Ext-6O-R_N-7R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Ext-4BrCClFINPSSi-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R_Ext-5C-R
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R_6R!H->C
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R_N-6R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-5C-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_6R!H->C
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_6R!H->C_Sp-6C-5C
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_6R!H->C_N-Sp-6C-5C
                                                                L17: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_6R!H->C_N-Sp-6C-5C_7R!H->C
                                                                L17: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_6R!H->C_N-Sp-6C-5C_N-7R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-6R!H->C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-5C-R_Ext-4BrCClFINPSSi-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-6R!H-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_7R!H->O
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_7R!H->O_Ext-7O-R
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-6R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_6R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_N-6R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-5O-R_6R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-5O-R_N-6R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi_Ext-4BrCClFINPSSi-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi_Ext-5C-R_6R!H->C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi_Ext-5C-R_N-6R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_N-Sp-5C-4BrCClFINPSSi
            L4: RJ1_N-1R-inRing_N-1R->O
                L5: RJ1_N-1R-inRing_N-1R->O_1CH->H
                L5: RJ1_N-1R-inRing_N-1R->O_N-1CH->H
                    L6: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C
                        L7: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C
                            L8: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-3C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_Sp-6R!H-4C
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_Sp-6R!H-4C_Ext-5R!H-R
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_Sp-6R!H-4C_Ext-5R!H-R_Sp-7R!H-5R!H
                                                                        L19: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_Sp-6R!H-4C_Ext-5R!H-R_Sp-7R!H-5R!H_Ext-5R!H-R
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_Sp-6R!H-4C_Ext-5R!H-R_N-Sp-7R!H-5R!H
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_N-Sp-6R!H-4C
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_N-Sp-6R!H-4C_Ext-5R!H-R
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_2C-inRing_N-Sp-6R!H-4C_Ext-5R!H-R_Ext-1C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_Ext-5R!H-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_Sp-5R!H-3C
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_Sp-5R!H-3C_Ext-4C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_N-Sp-5R!H-3C
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_N-Sp-5R!H-3C_Ext-4C-R
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-4C-R_N-2C-inRing_N-Sp-5R!H-3C_Ext-4C-R_Ext-4C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-1C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-5R!H-R_Ext-6R!H-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_3C-inRing
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_N-3C-inRing
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_5R!H->C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_5R!H->C_Ext-1C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_5R!H->C_2C-inRing
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_5R!H->C_N-2C-inRing
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_N-5R!H->C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_Ext-3C-R_N-4R!H->C_N-5R!H->C_Ext-1C-R_Ext-6R!H-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_2C-inRing
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_2C-inRing_Int-4R!H-3C_Ext-1C-R_5R!H->C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_2C-inRing_Int-4R!H-3C_Ext-1C-R_N-5R!H->C
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_Ext-6R!H-R_Ext-5R!H-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_Ext-6R!H-R_7R!H->C
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_Sp-8R!H-7C
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-Sp-8R!H-7C
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_Ext-6R!H-R_N-7R!H->C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-5R!H-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-4R!H-R
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-5R!H-R_4R!H->O
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_Sp-5R!H-1C_Ext-5R!H-R_N-4R!H->O
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_N-Sp-5R!H-1C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-2C-R_N-2C-inRing_Ext-1C-R_N-Sp-5R!H-1C_Ext-4R!H-R
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_3C-inRing
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_3C-inRing_Ext-1C-R
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-4O-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-4O-R_Ext-1C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-3C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_Ext-5R!H-R
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-3C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-3C-R_Ext-1C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-3C-R_Ext-4C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-4C-R
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R
                                                                        L19: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R
                                                                            L20: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R
                                                                            L20: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
                                                                            L20: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
                                                                                L21: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_5C-inRing
                                                                                L21: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-5C-inRing
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_Sp-5R!H-4C_N-5R!H->C
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-4C-R_N-Sp-5R!H-4C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3C-R_4R!H->C
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3C-R_4R!H->C_Sp-5R!H-3C
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3C-R_4R!H->C_N-Sp-5R!H-3C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3C-R_N-4R!H->C
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_4C-inRing
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-3C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-3C-R_Ext-5R!H-R
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-4C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-3C-R_Ext-4C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_5R!H-inRing
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_5R!H-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_5R!H-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Int-10R!H-8R!H_Int-10R!H-9R!H_Int-10R!H-9R!H_Ext-9R!H-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_N-5R!H-inRing
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_N-5R!H-inRing_Ext-4C-R
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_N-5R!H-inRing_5R!H->C
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_N-5R!H-inRing_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_Sp-5R!H-4C_N-5R!H-inRing_N-5R!H->C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_4R!H->C_N-4C-inRing_Ext-4C-R_N-Sp-5R!H-4C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-3C-inRing_Ext-3C-R_N-Sp-4R!H-3C
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_7R!H->C
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_7R!H->C_4R!H->C
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_7R!H->C_N-4R!H->C
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_N-7R!H->C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_6R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_Ext-5R!H-R_N-6R!H->C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-2C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-2C-R_Ext-4C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_Ext-5R!H-R_5R!H->O
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_Ext-5R!H-R_5R!H->O_4C-inRing
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_Ext-5R!H-R_5R!H->O_N-4C-inRing
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_Ext-5R!H-R_N-5R!H->O
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_Ext-5R!H-R_N-5R!H->O_Ext-4C-R
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_Ext-2C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_Ext-4O-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_N-Sp-4R!H-1C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-6O-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_4R!H->C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_4R!H->C_Ext-4C-R_7R!H->C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_4R!H->C_Ext-4C-R_N-7R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_N-4R!H->C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-6BrCClFINPSSi-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-6BrCClFINPSSi-R_7R!H->O
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-6BrCClFINPSSi-R_N-7R!H->O
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_4R!H->C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_4R!H->C_Ext-2C-R_Ext-4C-R
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_4R!H->C_Ext-4C-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-2C-R_Ext-5R!H-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-2C-R_Ext-5R!H-R_Ext-2C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-2C-R_Ext-6R!H-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-2C-R_Ext-6R!H-R_Int-5R!H-2C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-1C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-1C-R_5R!H->O
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-1C-R_5R!H->O_Ext-1C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_2C-inRing_Ext-3O-R_N-4R!H->C_Ext-1C-R_N-5R!H->O
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_Ext-3O-R_Ext-6R!H-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_Ext-3O-R_Ext-6R!H-R_Ext-2C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_Ext-3O-R_Ext-6R!H-R_Ext-2C-R_Ext-7R!H-R
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_Ext-3O-R_Ext-6R!H-R_Ext-2C-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->O
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_Ext-3O-R_Ext-6R!H-R_Ext-2C-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->O
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_4R!H->O
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_Ext-1C-R_N-4R!H->O
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R_Ext-4C-R
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R_Ext-4C-R_Ext-5R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-10R!H-9R!H
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R_Ext-4C-R_Ext-5R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-10R!H-9R!H_Ext-10R!H-R_Ext-10R!H-R
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R_Ext-4C-R_Ext-5R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-10R!H-9R!H
                                                                    L18: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-2C-R_Ext-4C-R_Ext-5R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-10R!H-9R!H_Ext-10R!H-R_Ext-10R!H-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-3O-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-3O-R_Ext-4C-R_6R!H->C
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-3O-R_Ext-4C-R_N-6R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_N-Sp-4C-1C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R_Ext-2C-R
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R_5R!H->C
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R_5R!H->C_Sp-4O-1C
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R_5R!H->C_N-Sp-4O-1C
                                                                L17: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R_5R!H->C_N-Sp-4O-1C_Ext-3O-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-1C-R_N-4R!H->C_Ext-2C-R_N-5R!H->C
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-2C-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-3O-R_Ext-4R!H-R
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-3O-R_Ext-4R!H-R_4R!H->C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->O_N-2C-inRing_Ext-3O-R_Ext-4R!H-R_N-4R!H->C
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_Sp-3C-2C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_Sp-3C-2C_Ext-5C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_Sp-3C-2C_Ext-3C-R
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_Sp-3C-2C_Ext-3C-R_Ext-6R!H-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_N-Sp-3C-2C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-4R!H-R_N-5R!H->C
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-1C-R
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-1C-R_Ext-2C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Ext-1C-R_Ext-2C-R_Ext-6R!H-R_Ext-6R!H-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_Sp-4R!H-1C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_Sp-4R!H-1C_4R!H->C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_Sp-4R!H-1C_4R!H->C_Ext-2C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_Sp-4R!H-1C_N-4R!H->C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-2C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Ext-3C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Ext-3C-R_5R!H->O
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Ext-3C-R_5R!H->O_3C-inRing
                                                            L16: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Ext-3C-R_5R!H->O_N-3C-inRing
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Ext-3C-R_N-5R!H->O
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_Sp-5R!H-3C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_Sp-3C-2C_N-Sp-4R!H-1C_Ext-3C-R_N-Sp-5R!H-3C
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_N-Sp-3C-2C
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Ext-1C-R_N-Sp-3C-2C_Ext-3C-R
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing_Ext-3C-R_Int-4R!H-2C
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing_Ext-3C-R_Int-4R!H-2C_Ext-2C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing_Ext-3C-R_Int-4R!H-2C_Ext-3C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing_Ext-3C-R_Int-4R!H-2C_Ext-3C-R_5R!H->C
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_2C-inRing_Ext-3C-R_Int-4R!H-2C_Ext-3C-R_N-5R!H->C
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing
                                                L13: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R_Ext-3C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-3C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-2C-R
                                                    L14: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R_Ext-2C-R
                                                        L15: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_Sp-3C-2C_N-2C-inRing_Ext-3C-R_Ext-2C-R_Ext-2C-R
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_N-Sp-3C-2C
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->O_N-Sp-3C-2C_Ext-3C-R_Ext-4R!H-R
                            L8: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C_3R!H->C
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C_N-3R!H->C
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C_N-3R!H->C_Ext-3O-R
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C_N-3R!H->C_Ext-3O-R_Ext-1C-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-3R!H-1C_N-3R!H->C_Ext-3O-R_Ext-1C-R_Ext-4R!H-R
                            L8: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-3R!H-1C
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-3R!H-1C_Ext-3R!H-R
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-3R!H-1C_Ext-3R!H-R_4R!H->C
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-3R!H-1C_Ext-3R!H-R_N-4R!H->C
                        L7: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C
                            L8: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C_Ext-3C-R_Sp-4R!H-3C
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C_Ext-3C-R_Sp-4R!H-3C_Ext-2O-R
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_3R!H->C_Ext-3C-R_N-Sp-4R!H-3C
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_N-3R!H->C
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_N-3R!H->C_Ext-2O-R
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-1C-R_N-3R!H->C_Ext-2O-R_Ext-4R!H-R_Ext-4R!H-R
                            L8: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R_4R!H->O
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R_N-4R!H->O
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R_N-4R!H->O_Ext-5R!H-R_Ext-5R!H-R
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_Sp-2R!H-1C_N-2R!H->C_Ext-2O-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R
                    L6: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C
                        L7: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C
                            L8: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_2R!H-inRing
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_2R!H-inRing_Ext-3R!H-R_Ext-2R!H-R
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_2R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_3R!H->O
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_2R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_N-3R!H->O
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_N-2R!H-inRing
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_N-2R!H-inRing_3R!H->O
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_N-2R!H-inRing_3R!H->O_Ext-3O-R
                                            L12: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_N-2R!H-inRing_3R!H->O_Ext-3O-R_Ext-2R!H-R
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_Sp-3R!H-2R!H_N-2R!H-inRing_N-3R!H->O
                            L8: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H
                                L9: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-4R!H-R_5R!H->C
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Ext-3R!H-R
                                    L10: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_Sp-5BrClFINOPSSi-4R!H
                                        L11: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_Sp-2R!H=1C_Ext-2R!H-R_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-4R!H
                        L7: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_N-Sp-2R!H=1C
                            L8: RJ1_N-1R-inRing_N-1R->O_N-1CH->H_Ext-1C-R_N-Sp-2R!H-1C_N-Sp-2R!H=1C_Ext-2R!H-R
"""
)

