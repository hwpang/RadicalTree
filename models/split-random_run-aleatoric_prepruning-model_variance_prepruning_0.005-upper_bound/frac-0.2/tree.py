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
CC=CCC1=CC=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from pang.py
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
CCN(OC1C[CH]C=C1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
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
7   [F,I,Br,Cl,P,C,O,Si,S] ux {5,[S,D,T,B,Q]}
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
7   [F,I,Br,Cl,P,C,O,Si,S] ux {5,[S,D,T,B,Q]}
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
4   [F,I,Br,Cl,P,O,Si,S,N] u0 r0 {3,[S,D,T,B,Q]}
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
O=C=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
CC1=[C]CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
C[C]1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
OCC1(O)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
OCC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
CC(=O)OC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
O[C]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
[CH]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
OC1[CH]OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
[CH]1CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
OOC[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
OOCC1[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
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
C1=CC2[C](C1)C1C=CC2C1 - Radical thermo from pang.py and closed shell thermo from pang.py
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
Derived using the following species:
[CH2]C=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1COOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C(=O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)COC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COCOO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[CH2]C(=C=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C12OC1(O)O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[O]C1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
C=C(C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1C=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)CC(OO)C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C=O)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CC1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC1([CH]C=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=O)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)OOC1C=CCC(C)=C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C([O])C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CCC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COO)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C)OOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C=O)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)[CH]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C1CC(C)(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=C(O)C(O)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC(O)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=CC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](C)C(C)(C)CC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C1CC(C)([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1(O)OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOC(C)(C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC(C)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[CH2]C=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CCC#C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCOC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1(C(=O)O)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[C]#CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from pang.py
CC(=O)OC1OC1(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOC(O)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[C]=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(COC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C1OOC(C)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C[O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(=CO)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=O)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
C=C=C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=C(COO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](O)C=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(N(CC)O)C[CH]C=C - Radical thermo from pang.py and closed shell thermo from pang.py
[O]OCC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]COOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C](O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCCO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC#C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]COC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CC1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C([CH]O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(C)(O[O])C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=O)C[C](C=O)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CC=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=COC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C](C)CCC(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([C]=O)OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
OC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C1(C)OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)CC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1([CH]O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=COC - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC(C)CO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C=C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C[C](C)C(C)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])CCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)C(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C1C=COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC(C)=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCCC=CCC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(O)=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC#CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
CC(C)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[C]=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(OC(C)=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(=O)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCCC1C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1CC(C)=CCC1C - Radical thermo from pang.py and closed shell thermo from GAV
C=C=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1(O)OOC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=CCCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1CC(C)(CO[O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(CC(C)O[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC1C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CC(=O)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[O]OCCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C(=O)OOC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(N(CC)O)C(C=C)[CH2] - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C#CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]OC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C=O)C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(=CO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)OC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C=C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
[O]C(O)(O)OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CCOCO1 - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
[CH2]C=CC#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(=O)CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[H] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[C]#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)OC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OOCC(O[O])C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC(CC(=C)C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1(C(C)C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OC(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(O)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
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
"""
)

