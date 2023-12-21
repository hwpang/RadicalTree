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
        Cpdata = ([-1.08398,-1.6912,-1.9904,-1.70479,-1.06588,-1.03732,-1.56281],'cal/mol/K','+|-',[6.66654,7.98784,7.33869,6.44755,5.89928,5.91585,7.46114]),
        H298 = (86.3564,'kcal/mol','+|-',27.7859),
        S298 = (-6.03209,'cal/mol/K','+|-',14.2955),
    ),
    shortDesc = """Radical correction fitted to 30 radicals""",
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
        Cpdata = ([-1.08398,-1.6912,-1.9904,-1.70479,-1.06588,-1.03732,-1.56281],'cal/mol/K','+|-',[6.66654,7.98784,7.33869,6.44755,5.89928,5.91585,7.46114]),
        H298 = (86.3564,'kcal/mol','+|-',27.7859),
        S298 = (-6.03209,'cal/mol/K','+|-',14.2955),
    ),
    shortDesc = """Radical correction fitted to 30 radicals""",
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
        Cpdata = ([-2.56334,-3.44614,-3.5117,-2.85484,-1.52545,-0.914633,-0.138402],'cal/mol/K','+|-',[6.36281,7.84442,7.39516,6.88845,7.32135,7.60744,7.70978]),
        H298 = (77.641,'kcal/mol','+|-',23.6735),
        S298 = (-6.41035,'cal/mol/K','+|-',16.8635),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.62529,-6.13898,-6.12296,-5.19,-3.28566,-2.15215,-0.436678],'cal/mol/K','+|-',[4.64609,4.88999,3.91932,3.91005,6.80786,8.47145,9.4473]),
        H298 = (74.1293,'kcal/mol','+|-',25.5213),
        S298 = (-2.35143,'cal/mol/K','+|-',15.6729),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * O     u1 {2,[S,D,T,B,Q]}
2   C     ux {1,[S,D,T,B,Q]} {3,D}
3   C     ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   [C,O] ux {3,[S,D,T,B,Q]}
5   [C,O] ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.92066,-6.39657,-6.33188,-5.39068,-3.44889,-2.18027,-0.32505],'cal/mol/K','+|-',[4.4966,4.88301,3.90748,3.91756,7.14711,9.00152,10.0111]),
        H298 = (72.5193,'kcal/mol','+|-',23.732),
        S298 = (-1.97777,'cal/mol/K','+|-',16.4562),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O ux {3,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.7744,-6.11055,-6.03997,-5.08797,-3.09965,-1.83648,0.039291],'cal/mol/K','+|-',[4.7232,4.87933,3.71417,3.68809,7.30468,9.379,10.4594]),
        H298 = (72.6273,'kcal/mol','+|-',25.3363),
        S298 = (-3.02425,'cal/mol/K','+|-',16.2193),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {6,D}
5   O ux {3,[S,D,T,B,Q]}
6   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.75717,-6.10238,-6.08516,-5.2422,-3.42674,-2.14921,-0.0546594],'cal/mol/K','+|-',[5.12651,5.29693,4.02189,3.88081,7.64997,9.98426,11.3392]),
        H298 = (70.4446,'kcal/mol','+|-',21.5485),
        S298 = (-2.3432,'cal/mol/K','+|-',17.0622),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-2R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {7,[S,D,T,B,Q]}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {6,D}
5   O   ux {3,[S,D,T,B,Q]}
6   O   ux {4,D}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.19183,-5.67108,-6.02532,-5.75737,-5.07341,-4.35367,-2.2528],'cal/mol/K','+|-',[7.14891,7.47499,5.62929,4.81184,8.98867,12.0388,14.6267]),
        H298 = (69.248,'kcal/mol','+|-',23.1738),
        S298 = (1.57734,'cal/mol/K','+|-',20.0144),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-2R!H-R_7R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D} {7,S}
3   C ux r0 {2,D} {4,S} {5,[S,D,T,B,Q]}
4   C u0 r0 {3,S} {6,D}
5   O ux {3,[S,D,T,B,Q]}
6   O u0 r0 {4,D}
7   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.22684,-5.94943,-4.9572,-2.76693,0.813868,2.48061,4.55767],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.476,'kcal/mol','+|-',5.2),
        S298 = (-10.6339,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=C(O)C=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 9,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-2R!H-R_N-7R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S} {3,D} {7,[S,D,T,B,Q]}
3   C u0 {2,D} {4,[S,D,T,B,Q]} {5,S}
4   C ux {3,[S,D,T,B,Q]} {6,D}
5   O u0 {3,S}
6   O ux {4,D}
7   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.87337,-5.58544,-6.35397,-6.6775,-6.88487,-6.45652,-4.34833],'cal/mol/K','+|-',[9.56485,10.2056,7.41117,3.08178,4.48252,9.71955,14.9897]),
        H298 = (66.047,'kcal/mol','+|-',7.95545),
        S298 = (5.33465,'cal/mol/K','+|-',13.6187),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 10,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,D} {7,[S,D,T,B,Q]}
3   C   u0 {2,D} {4,[S,D,T,B,Q]} {5,S}
4   C   ux {3,[S,D,T,B,Q]} {6,D}
5   O   u0 r0 {3,S}
6   O   ux {4,D}
7   O   ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79233,-3.36499,-4.74151,-6.007,-7.86014,-8.57122,-7.60966],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (67.0348,'kcal/mol','+|-',2.4),
        S298 = (8.29768,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 11,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-4R!H-R_7R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {4,S} {5,S}
4   C u0 r0 {3,S} {6,D} {7,S}
5   O u0 r0 {3,S}
6   O u0 r0 {4,D}
7   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.39684,-5.39943,-4.9072,-2.99693,0.693868,2.12061,3.38767],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.476,'kcal/mol','+|-',5.2),
        S298 = (-10.3539,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=C(O)C(=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 12,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-4R!H-R_N-7R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D}
3   C                      u0 r0 {2,D} {4,S} {5,S}
4   C                      u0 r0 {3,S} {6,D} {7,S}
5   O                      u0 r0 {3,S}
6   O                      u0 r0 {4,D}
7   [Si,S,N,O,P,F,Br,I,Cl] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.13869,-7.37034,-6.8013,-5.27009,-1.98787,0.400347,2.89523],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (65.4344,'kcal/mol','+|-',5.2),
        S298 = (-6.66896,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 13,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-Sp-6R!H=4R!H",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {4,S} {5,[S,D,T,B,Q]}
4   C u0 r0 {3,S} {6,[S,T,Q,B]}
5   O ux {3,[S,D,T,B,Q]}
6   O u0 r0 {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.89933,-6.16985,-5.71233,-3.96984,-0.728227,0.430804,0.720431],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.787,'kcal/mol','+|-',5.2),
        S298 = (-7.96192,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 14,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C",
    group = 
"""
1 * R u1 {2,S}
2   C ux {1,S} {3,D}
3   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.455945,0.496943,0.311935,0.564499,1.05199,0.897439,0.298359],'cal/mol/K','+|-',[3,3,3,3.53954,4.71278,4.6928,4.9353]),
        H298 = (84.0094,'kcal/mol','+|-',15.7825),
        S298 = (-12.3538,'cal/mol/K','+|-',10.8432),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 15,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,S}
2   C ux {1,S} {3,D}
3   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.137842,0.319804,0.295109,0.687254,1.40094,1.32754,0.965661],'cal/mol/K','+|-',[3,3,3.25319,3.81152,4.74985,4.49569,3.77714]),
        H298 = (81.1437,'kcal/mol','+|-',5.2),
        S298 = (-13.6478,'cal/mol/K','+|-',9.21021),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 16,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux {1,S} {3,D} {4,S}
3   O   u0 {2,D}
4   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.18533,0.3198,0.256236,0.526688,1.11287,1.07817,0.824439],'cal/mol/K','+|-',[3,3.05639,3.63093,4.16967,5.07068,4.8372,4.15153]),
        H298 = (80.5904,'kcal/mol','+|-',5.2),
        S298 = (-12.9999,'cal/mol/K','+|-',9.66653),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 17,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_4R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C ux {1,S} {3,D} {4,S}
3   O u0 {2,D}
4   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.877821,1.83074,2.00463,2.53202,3.38055,2.73747,1.7607],'cal/mol/K','+|-',[3,3,3,3,4.4788,6.51258,6.58841]),
        H298 = (82.6553,'kcal/mol','+|-',5.2),
        S298 = (-16.8781,'cal/mol/K','+|-',9.91844),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 18,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D} {4,S}
3   O   u0 {2,D}
4   C   u0 r0 {2,S}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.194039,1.48144,2.16406,3.19175,4.96404,5.04001,4.09006],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.3947,'kcal/mol','+|-',5.2),
        S298 = (-20.3848,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[C](O)C(=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 19,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_N-4R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C ux {1,S} {3,D} {4,S}
3   O u0 {2,D}
4   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.27633,-0.687492,-0.90936,-0.810199,-0.398915,-0.0280227,0.200264],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.2139,'kcal/mol','+|-',5.2),
        S298 = (-10.4144,'cal/mol/K','+|-',6.11761),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 20,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R",
    group = 
"""
1 * C     u1 {2,S} {5,S}
2   C     ux {1,S} {3,D} {4,S}
3   O     u0 {2,D}
4   O     u0 r0 {2,S}
5   [C,O] u0 r0 {1,S} {6,[S,D,T,B,Q]}
6   R!H   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.284943,-0.274377,-0.307875,-0.205752,0.273715,0.701341,0.936189],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.6158,'kcal/mol','+|-',5.2),
        S298 = (-12.1556,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(=O)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C](O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 21,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_N-1R->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S} {3,D}
3   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.36456,1.55978,0.412894,-0.172027,-1.04168,-1.68318,-3.70545],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.203,'kcal/mol','+|-',5.2),
        S298 = (-4.58964,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=O)OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 22,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.5894,0.293893,-0.269588,-0.403904,-0.546044,-1.1761,-3.17402],'cal/mol/K','+|-',[5.45891,6.28743,5.76248,4.9487,3.74121,3.40566,5.89839]),
        H298 = (96.057,'kcal/mol','+|-',17.3869),
        S298 = (-5.60422,'cal/mol/K','+|-',11.3319),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 23,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.37385,-0.300539,-1.08849,-1.0702,-0.73973,-1.17911,-3.19325],'cal/mol/K','+|-',[5.65687,6.54465,5.81724,5.02468,4.1353,3.89225,7.19052]),
        H298 = (97.4419,'kcal/mol','+|-',16.2803),
        S298 = (-7.28951,'cal/mol/K','+|-',12.3439),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 24,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.446332,-0.154394,-0.798604,-0.670994,-0.338494,-0.789093,-2.02644],'cal/mol/K','+|-',[6.3529,7.11076,5.99218,4.67419,3.28183,3.09072,5.28337]),
        H298 = (98.0585,'kcal/mol','+|-',17.2501),
        S298 = (-8.92352,'cal/mol/K','+|-',10.5568),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 25,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   O ux {1,S} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   C u0 {3,[S,D,T,B,Q]} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.81099,-5.30125,-5.21355,-3.83394,-1.37981,-0.572067,0.540449],'cal/mol/K','+|-',[7.64034,5.95655,3.84037,3,3,3.50321,7.31662]),
        H298 = (106.349,'kcal/mol','+|-',9.3262),
        S298 = (-7.42767,'cal/mol/K','+|-',9.89487),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 26,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-5C-R_Ext-5C-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,D}
5   C   ux r0 {4,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.51225,-7.4072,-6.57132,-4.49226,-1.01802,0.666506,3.12726],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.052,'kcal/mol','+|-',5.2),
        S298 = (-10.926,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(O)C(O)=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 27,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   O   ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.86544,1.56122,0.673044,0.383321,0.00861255,-0.861435,-2.88206],'cal/mol/K','+|-',[3,3,3,3,3.54342,3.28917,3.78374]),
        H298 = (95.2951,'kcal/mol','+|-',15.8926),
        S298 = (-9.42213,'cal/mol/K','+|-',11.4747),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 28,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_2R!H->C",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.80321,1.4366,0.430297,0.125195,-0.472265,-1.24678,-3.82885],'cal/mol/K','+|-',[3,3,3,3.57993,4.73524,4.58469,4.22525]),
        H298 = (100.309,'kcal/mol','+|-',5.2),
        S298 = (-5.35875,'cal/mol/K','+|-',6.76636),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 29,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_2R!H->C_2C-inRing",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,D}
5   O u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22038,1.78402,0.444024,-0.0502294,-0.975685,-2.0763,-5.04615],'cal/mol/K','+|-',[3,3,3.4704,4.98932,6.22597,5.05217,3]),
        H298 = (99.8171,'kcal/mol','+|-',5.2),
        S298 = (-4.13404,'cal/mol/K','+|-',7.45446),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 30,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_2R!H->C_2C-inRing_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,D}
5   O u0 {4,D}
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
    index = 31,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_2R!H->C_2C-inRing_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,D}
5   O u0 {4,D}
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
    index = 32,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_2R!H->C_N-2C-inRing",
    group = 
"""
1 * R u1 {2,S}
2   C ux r0 {1,S} {3,S}
3   O u0 {2,S} {4,[S,D,T,B,Q]}
4   C u0 {3,[S,D,T,B,Q]} {5,D}
5   O ux r0 {4,D}
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
    index = 33,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_N-2R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,D}
5   O u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.92767,1.68584,0.915792,0.641448,0.48949,-0.476087,-1.93528],'cal/mol/K','+|-',[3.63518,3.66579,3,3,3,3,3]),
        H298 = (90.2807,'kcal/mol','+|-',18.0729),
        S298 = (-13.4855,'cal/mol/K','+|-',9.23329),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 34,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_N-2R!H->C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {6,S}
4   C   ux {3,S} {5,D}
5   O   u0 {4,D}
6   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.76304,2.56228,1.65705,1.43027,1.20713,-0.112658,-1.84531],'cal/mol/K','+|-',[3.1114,3,3,3,3,3,3.76434]),
        H298 = (93.3443,'kcal/mol','+|-',20.6884),
        S298 = (-15.4719,'cal/mol/K','+|-',8.70701),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 35,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_N-2R!H->C_Ext-3R!H-R_6R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {6,S}
4   C ux {3,S} {5,D}
5   O u0 {4,D}
6   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.66299,1.53511,1.15286,1.15807,1.15212,0.702854,-0.514416],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.0298,'kcal/mol','+|-',5.2),
        S298 = (-18.5503,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C(CC(=O)OC=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 36,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_N-2R!H->C_Ext-3R!H-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   O                      u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C                      ux {2,[S,T,Q,B]} {4,S} {6,S}
4   C                      ux {3,S} {5,D}
5   O                      u0 {4,D}
6   [Si,S,N,O,P,F,Br,I,Cl] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.86309,3.58945,2.16124,1.70248,1.26215,-0.92817,-3.1762],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.659,'kcal/mol','+|-',5.2),
        S298 = (-12.3935,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C(=O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 37,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 * C     u1 {2,S}
2   C     ux {1,S} {3,S}
3   O     u0 {2,S} {4,[S,D,T,B,Q]}
4   O     u0 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   [C,O] ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0839235,-0.885118,-2.24805,-2.66701,-2.34467,-2.73919,-7.86052],'cal/mol/K','+|-',[3,5.30423,6.30661,6.9851,7.26329,6.71865,7.21809]),
        H298 = (94.9754,'kcal/mol','+|-',15.5439),
        S298 = (-0.753459,'cal/mol/K','+|-',12.8076),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 38,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_1R-inRing",
    group = 
"""
1 * C     u1 r1 {2,S}
2   C     ux r1 {1,S} {3,S}
3   O     u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   O     u0 r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   [C,O] ux r1 {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.678177,-2.76044,-4.47778,-5.13662,-4.91263,-5.11459,-10.4125],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.471,'kcal/mol','+|-',5.2),
        S298 = (3.7747,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1O[CH]C(C)(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 39,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-1R-inRing",
    group = 
"""
1 * C     u1 r0 {2,S}
2   C     ux r1 {1,S} {3,S}
3   O     u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   O     u0 r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   [C,O] ux r1 {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.846024,0.99021,-0.0183271,-0.19741,0.223288,-0.363784,-5.30854],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.4797,'kcal/mol','+|-',5.2),
        S298 = (-5.28162,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](O)C1OOC(OC(C)=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 40,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.04927,1.59587,1.52658,1.05747,-0.0991278,-1.10914,-3.05823],'cal/mol/K','+|-',[6.96429,7.00259,5.54558,4.90828,3.83483,3.19722,3.00818]),
        H298 = (97.1854,'kcal/mol','+|-',11.6582),
        S298 = (-2.15521,'cal/mol/K','+|-',6.20788),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 41,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   O u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.30265,0.277171,0.551218,0.241707,-0.67372,-1.49473,-3.00402],'cal/mol/K','+|-',[4.21097,4.71941,4.41882,4.29878,3.78357,3.62983,4.09856]),
        H298 = (98.7806,'kcal/mol','+|-',5.2),
        S298 = (-1.3304,'cal/mol/K','+|-',6.70013),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 42,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,D}
4   O   u0 r0 {3,D}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.75877,2.58749,2.71439,2.34611,1.17847,0.282207,-0.997631],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.141,'kcal/mol','+|-',5.2),
        S298 = (-4.61035,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C(O)O[C](O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 43,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S}
4   O u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.44303,5.88165,4.69651,3.70868,1.7683,0.144,-3.23442],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.1015,'kcal/mol','+|-',5.2),
        S298 = (-4.83585,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 44,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]}
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

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-2R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-2R!H-R_7R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-2R!H-R_N-7R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-4R!H-R_7R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H=4R!H_Ext-4R!H-R_N-7R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-Sp-6R!H=4R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_4R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-1C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_N-4R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_N-1R->C
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-5C-R_Ext-5C-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_2R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_2R!H->C_2C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_2R!H->C_2C-inRing_1R->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_2R!H->C_2C-inRing_N-1R->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_2R!H->C_N-2C-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_N-2R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_N-2R!H->C_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_N-2R!H->C_Ext-3R!H-R_6R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_N-2R!H->C_Ext-3R!H-R_N-6R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_1R-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-1R-inRing
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_Sp-4R!H=3R!H
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_Ext-1C-R_Ext-1C-R
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C
"""
)

