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
        Cpdata = ([-0.613263,-1.60848,-2.31944,-2.73523,-3.17391,-3.56223,-4.37159],'cal/mol/K','+|-',[4.00645,4.62392,4.91309,4.86443,4.48433,4.20144,4.1327]),
        H298 = (94.0212,'kcal/mol','+|-',24.7767),
        S298 = (0.410316,'cal/mol/K','+|-',10.0994),
    ),
    shortDesc = """Radical correction fitted to 2257 radicals""",
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
        Cpdata = ([-0.613263,-1.60848,-2.31944,-2.73523,-3.17391,-3.56223,-4.37159],'cal/mol/K','+|-',[4.00645,4.62392,4.91309,4.86443,4.48433,4.20144,4.1327]),
        H298 = (94.0212,'kcal/mol','+|-',24.7767),
        S298 = (0.410316,'cal/mol/K','+|-',10.0994),
    ),
    shortDesc = """Radical correction fitted to 2257 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 2,
    label = "RJ1_1R->C",
    group = 
"""
1 * C u1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0362692,-0.969094,-1.7192,-2.21857,-2.84832,-3.3638,-4.37594],'cal/mol/K','+|-',[3.21093,3.66684,4.01955,4.05622,3.82956,3.63311,3.71559]),
        H298 = (95.0458,'kcal/mol','+|-',23.906),
        S298 = (0.922397,'cal/mol/K','+|-',9.73802),
    ),
    shortDesc = """Radical correction fitted to 1456 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_1R->C_1C-inRing",
    group = 
"""
1 * C u1 r1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.154862,-1.13236,-2.09022,-2.66425,-3.35214,-3.90645,-4.96161],'cal/mol/K','+|-',[3,3.44618,3.77247,3.69903,3.31465,3.18221,3.72848]),
        H298 = (93.8966,'kcal/mol','+|-',31.0047),
        S298 = (1.00559,'cal/mol/K','+|-',7.41401),
    ),
    shortDesc = """Radical correction fitted to 416 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.226257,-1.11666,-2.0661,-2.60013,-3.24675,-3.77034,-4.58108],'cal/mol/K','+|-',[3.02869,3.64462,3.86384,3.72098,3.29368,3.16024,3.0988]),
        H298 = (86.2879,'kcal/mol','+|-',34.6261),
        S298 = (0.380832,'cal/mol/K','+|-',7.85569),
    ),
    shortDesc = """Radical correction fitted to 233 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.268271,-1.12311,-2.0992,-2.63082,-3.25421,-3.77053,-4.56868],'cal/mol/K','+|-',[3.12183,3.7967,4.01261,3.85411,3.37959,3.22519,3.18999]),
        H298 = (83.1251,'kcal/mol','+|-',30.2543),
        S298 = (0.303134,'cal/mol/K','+|-',8.13396),
    ),
    shortDesc = """Radical correction fitted to 219 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   R!H ux {2,D}
4   R!H ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0228544,-1.29619,-2.25518,-2.82008,-3.46948,-4.03398,-4.71761],'cal/mol/K','+|-',[3.36271,4.47429,4.88486,4.88542,4.44017,4.28121,4.54585]),
        H298 = (84.0576,'kcal/mol','+|-',43.0272),
        S298 = (1.18341,'cal/mol/K','+|-',6.64173),
    ),
    shortDesc = """Radical correction fitted to 86 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.257798,-1.76783,-2.61183,-3.04186,-3.50939,-3.91149,-4.36403],'cal/mol/K','+|-',[3.52029,5.44999,5.87288,5.67755,4.93536,4.56937,5.18077]),
        H298 = (76.451,'kcal/mol','+|-',54.8916),
        S298 = (1.38714,'cal/mol/K','+|-',7.59967),
    ),
    shortDesc = """Radical correction fitted to 47 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   O   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0825314,-1.13182,-2.27297,-2.77507,-3.34803,-3.95758,-4.39659],'cal/mol/K','+|-',[3,5.01213,5.9148,5.74322,4.52749,3.25685,6.36955]),
        H298 = (91.5953,'kcal/mol','+|-',52.6104),
        S298 = (1.77794,'cal/mol/K','+|-',8.21711),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 9,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D} {6,[S,D,T,B,Q]}
4   O   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.542329,-0.797365,-1.88109,-2.24882,-2.82668,-3.66969,-2.38478],'cal/mol/K','+|-',[3,3,3.27392,3.30786,3,3,5.8085]),
        H298 = (111.648,'kcal/mol','+|-',83.7196),
        S298 = (1.38983,'cal/mol/K','+|-',9.23321),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 10,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-3C-R_Ext-5R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D} {5,S}
3   C u0 {2,D} {6,[S,D,T,B,Q]}
4   O u0 {1,S}
5   C u0 {2,S} {7,S}
6   O ux {3,[S,D,T,B,Q]}
7   O u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.600653,-1.03172,-2.15084,-2.36973,-2.99362,-4.29058,0.127238],'cal/mol/K','+|-',[3,3,3,3,3,3,7.06874]),
        H298 = (151.534,'kcal/mol','+|-',5.2),
        S298 = (3.14285,'cal/mol/K','+|-',4.15853),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 11,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-3C-R_Ext-5R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D} {5,S}
3   C   u0 r1 {2,D} {6,[S,D,T,B,Q]}
4   O   u0 {1,S}
5   C   u0 r1 {2,S} {7,S}
6   O   ux r1 {3,[S,D,T,B,Q]}
7   O   u0 r1 {5,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.39628,-0.367913,-1.70853,-1.99808,-2.82698,-3.96536,-2.37194],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (151.485,'kcal/mol','+|-',5.2),
        S298 = (4.61311,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1C2=COC1OOC2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 12,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   O   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.79135,1.48394,0.742663,0.208961,-0.754743,-2.13209,-4.00575],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (54.8333,'kcal/mol','+|-',5.2),
        S298 = (-5.65078,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=C(C)C(=O)O[CH]1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 13,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-3C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D} {6,[S,D,T,B,Q]}
4   O   ux r0 {1,S}
5   O   ux {2,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0521994,-1.48046,-2.17299,-2.32226,-2.70082,-2.9039,-3.76351],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.2137,'kcal/mol','+|-',5.2),
        S298 = (0.0776708,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1C=CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 14,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-4O-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {1,S} {6,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
6   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.882349,-3.47523,-5.4425,-5.91974,-5.71155,-5.57735,-7.61213],'cal/mol/K','+|-',[5.57566,8.72275,9.20403,8.81391,7.23139,5.16862,7.35437]),
        H298 = (87.2507,'kcal/mol','+|-',12.0835),
        S298 = (4.99047,'cal/mol/K','+|-',10.6179),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 15,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-4O-R_Ext-6R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {1,S} {6,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
6   C ux {4,[S,D,T,B,Q]} {7,S}
7   O u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.705516,-2.7453,-4.66537,-5.14007,-5.05892,-5.0717,-7.85532],'cal/mol/K','+|-',[7.83744,11.8062,12.4473,11.8651,9.71411,6.87697,10.3322]),
        H298 = (83.8517,'kcal/mol','+|-',5.2),
        S298 = (1.99844,'cal/mol/K','+|-',3.25958),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 16,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {8,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   O   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]}
6   C   ux r1 {4,[S,D,T,B,Q]} {7,S}
7   O   u0 {6,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.47647,-6.9194,-9.06614,-9.33503,-8.49338,-7.50308,-11.5083],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.2099,'kcal/mol','+|-',5.2),
        S298 = (3.15088,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[C]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   O   ux r1 {1,S}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.224346,0.0853847,-0.598748,-1.25621,-2.35583,-3.20222,-4.466],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (82.0248,'kcal/mol','+|-',2.4),
        S298 = (-0.00801698,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]OC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 18,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.353397,-1.94648,-2.70702,-3.1168,-3.55471,-3.89855,-4.35489],'cal/mol/K','+|-',[3.69475,5.59139,5.94482,5.74534,5.11063,4.91964,4.92067]),
        H298 = (72.0001,'kcal/mol','+|-',53.5429),
        S298 = (1.27737,'cal/mol/K','+|-',7.54631),
    ),
    shortDesc = """Radical correction fitted to 37 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 19,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.249355,-1.38178,-2.1556,-2.652,-3.23176,-3.67705,-4.1271],'cal/mol/K','+|-',[4.17561,5.00169,5.51734,5.5913,5.46434,5.64561,5.83596]),
        H298 = (67.7312,'kcal/mol','+|-',62.9358),
        S298 = (0.529406,'cal/mol/K','+|-',6.69313),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 20,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {1,S} {6,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.522871,0.134421,-0.367712,-0.889006,-1.66849,-2.20819,-2.80326],'cal/mol/K','+|-',[3,3,3.42401,4.30181,5.69887,6.68058,8.53781]),
        H298 = (54.9855,'kcal/mol','+|-',89.0532),
        S298 = (-1.00488,'cal/mol/K','+|-',4.45703),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 21,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_Sp-6R!H-4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {1,S} {6,S}
5   C ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {4,S} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.217555,0.163021,-0.0674953,-0.307543,-0.653134,-0.831303,-1.03639],'cal/mol/K','+|-',[3,3,4.0703,5.18018,7.11578,8.67003,11.4841]),
        H298 = (40.5948,'kcal/mol','+|-',123.489),
        S298 = (-0.208069,'cal/mol/K','+|-',4.79732),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 22,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_Sp-6R!H-4C_Sp-6R!H-5R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D} {5,S}
3   C u0 {2,D}
4   C u0 {1,S} {6,S}
5   C u0 {2,S} {6,S}
6   C ux {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.319749,0.232539,0.198116,0.244374,0.388183,0.668354,1.25299],'cal/mol/K','+|-',[3,3.25246,6.32357,7.77172,10.1131,11.7116,14.5231]),
        H298 = (4.92369,'kcal/mol','+|-',130.595),
        S298 = (1.00722,'cal/mol/K','+|-',4.88887),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 23,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_Sp-6R!H-4C_Sp-6R!H-5R!H_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D} {5,S}
3   C   u0 {2,D}
4   C   u0 r1 {1,S} {6,S}
5   C   u0 r1 {2,S} {6,S}
6   C   ux r1 {4,S} {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.759452,-1.35966,-2.8975,-3.56016,-4.56254,-5.06491,-5.85658],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.0517,'kcal/mol','+|-',5.2),
        S298 = (3.40049,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CCC(C)[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 24,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_Sp-6R!H-4C_N-Sp-6R!H-5R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {2,[S,D,T,B,Q]} {6,D}
6   C u0 r1 {4,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0699417,0.062605,-0.451155,-1.10476,-2.15726,-2.99747,-4.34326],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.8645,'kcal/mol','+|-',2.4),
        S298 = (-1.96348,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 25,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {1,S} {6,[B,D,T,Q]}
5   C ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {4,[B,D,T,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.842726,0.10446,-0.682224,-1.49816,-2.73221,-3.65064,-4.65427],'cal/mol/K','+|-',[3.44347,3.23309,3.41971,3.92991,4.29915,3.78911,3.82262]),
        H298 = (74.4154,'kcal/mol','+|-',6.29295),
        S298 = (-1.83964,'cal/mol/K','+|-',4.3246),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 26,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C_3C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D}
4   C ux r1 {1,S} {6,[B,D,T,Q]}
5   C ux r1 {2,[S,D,T,B,Q]} {6,S}
6   C u0 r1 {4,[B,D,T,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.75352,-1.07032,-2.83487,-4.45978,-6.24692,-6.85942,-7.64272],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (69.6111,'kcal/mol','+|-',5.2),
        S298 = (-2.78123,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1=C1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 27,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C_N-3C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux {1,S} {6,[B,D,T,Q]}
5   C ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {4,[B,D,T,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.628422,0.380878,-0.17572,-0.801307,-1.90521,-2.89564,-3.95111],'cal/mol/K','+|-',[3.92844,3.5165,3,3,3,3,3]),
        H298 = (75.1331,'kcal/mol','+|-',5.2),
        S298 = (-1.61809,'cal/mol/K','+|-',5.0146),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 28,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C_N-3C-inRing_Sp-6R!H=4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux {1,S} {6,D}
5   C ux {2,[S,D,T,B,Q]} {6,S}
6   C u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.887125,0.65865,0.0157203,-0.703236,-1.87056,-2.88459,-4.37584],'cal/mol/K','+|-',[5.11638,4.4762,3.65673,3.12166,3,3,3]),
        H298 = (74.4836,'kcal/mol','+|-',5.2),
        S298 = (-2.35407,'cal/mol/K','+|-',5.03898),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 29,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C_N-3C-inRing_Sp-6R!H=4C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {6,D}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,S} {7,[S,D,T,B,Q]}
6   C   u0 r1 {4,D} {5,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.39177,2.84991,1.80582,0.824928,-0.727889,-2.23408,-4.1998],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.5398,'kcal/mol','+|-',5.2),
        S298 = (-4.82083,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 30,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C_N-3C-inRing_N-Sp-6R!H=4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,S}
3   C u0 r0 {2,D}
4   C u0 r1 {1,S} {6,T}
5   C u0 r1 {2,S} {6,[S,D,T,B,Q]}
6   C ux r1 {4,T} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.212362,-0.521882,-0.7979,-1.12004,-2.01784,-2.93152,-2.57073],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.8313,'kcal/mol','+|-',5.2),
        S298 = (0.773844,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C#CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 31,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.746142,-3.12076,-4.3206,-4.84085,-5.16111,-5.4522,-5.4084],'cal/mol/K','+|-',[5.68991,5.57204,5.27736,4.76245,3.67129,3.41858,3]),
        H298 = (80.4006,'kcal/mol','+|-',15.4211),
        S298 = (2.20998,'cal/mol/K','+|-',8.11965),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 32,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   C   u0 {2,D}
4   C   u0 {1,S}
5   R!H u0 r1 {2,S} {6,S} {7,[S,D,T,B,Q]}
6   R!H u0 {5,S}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 33,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_3C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux {1,S}
5   R!H ux r1 {2,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08198,-2.19324,-3.58607,-4.19595,-4.26333,-4.15478,-4.94516],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (67.7511,'kcal/mol','+|-',5.2),
        S298 = (-2.31703,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=CCC([C]2C=CCCC2)=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 34,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.866776,-3.4882,-4.69438,-5.23064,-5.54817,-5.83523,-5.55403],'cal/mol/K','+|-',[6.19658,5.79754,5.40093,4.70719,3.39437,3.16736,3]),
        H298 = (82.7375,'kcal/mol','+|-',12.0081),
        S298 = (2.68628,'cal/mol/K','+|-',8.39274),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 35,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux {1,S}
5   C   ux {2,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.766719,-3.46599,-4.68171,-5.24901,-5.6003,-5.96046,-5.40575],'cal/mol/K','+|-',[6.53811,6.14741,5.72792,4.99121,3.58325,3.25276,3]),
        H298 = (81.5181,'kcal/mol','+|-',9.76213),
        S298 = (1.83006,'cal/mol/K','+|-',6.80094),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 36,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux {1,S} {7,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09346,-4.30218,-5.58637,-6.17946,-6.36381,-6.62039,-5.57322],'cal/mol/K','+|-',[7.3825,5.91946,5.10045,3.83744,3,3,3]),
        H298 = (81.5379,'kcal/mol','+|-',11.1258),
        S298 = (2.10218,'cal/mol/K','+|-',7.74854),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 37,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   C   u0 {1,S} {7,S}
5   C   u0 {2,S} {6,S}
6   R!H u0 {5,S}
7   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.45645,-4.4669,-5.95967,-6.58263,-6.63601,-6.92987,-5.3081],'cal/mol/K','+|-',[6.74039,6.25724,5.34924,4.07188,3,3,3]),
        H298 = (84.5074,'kcal/mol','+|-',5.2),
        S298 = (1.66932,'cal/mol/K','+|-',9.10093),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 38,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C_Int-7R!H-6R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   C   u0 {1,S} {7,S}
5   C   u0 {2,S} {6,S}
6   R!H u0 {5,S} {7,S}
7   R!H u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.988044,-3.14325,-4.85335,-5.74194,-6.18404,-6.76004,-5.02752],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.1755,'kcal/mol','+|-',5.2),
        S298 = (0.0263235,'cal/mol/K','+|-',6.2009),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 39,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C_Int-7R!H-6R!H_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {7,S}
5   C   u0 r1 {2,S} {6,S}
6   R!H u0 r1 {5,S} {7,S}
7   R!H u0 r1 {4,S} {6,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0687,-3.22783,-5.02213,-6.08545,-7.17103,-8.06177,-6.46962],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.1247,'kcal/mol','+|-',5.2),
        S298 = (3.45427,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1COOC[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 40,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C_Int-7R!H-6R!H_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   C   u0 {1,S} {7,S} {8,S}
5   C   u0 {2,S} {6,S}
6   C   u0 {5,S} {7,S}
7   C   u0 {4,S} {6,S}
8   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12333,-3.54904,-5.25614,-5.89278,-5.72259,-5.88859,-3.83567],'cal/mol/K','+|-',[3,3.44805,3.36624,3,3,3,3]),
        H298 = (84.0469,'kcal/mol','+|-',5.2),
        S298 = (-2.49366,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 41,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C_Int-7R!H-6R!H_Ext-4C-R_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {5,S}
3   C u0 r0 {2,D}
4   C u0 r1 {1,S} {7,S} {8,S}
5   C u0 r1 {2,S} {6,S}
6   C u0 r1 {5,S} {7,S}
7   C u0 r1 {4,S} {6,S}
8   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0884508,-2.32997,-4.066,-4.92703,-5.43758,-5.6665,-3.99703],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.7506,'kcal/mol','+|-',5.2),
        S298 = (-1.54806,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]C(=C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 42,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C_Int-7R!H-6R!H_Ext-4C-R_N-8R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,D} {5,S}
3   C                      u0 r0 {2,D}
4   C                      u0 r1 {1,S} {7,S} {8,S}
5   C                      u0 r1 {2,S} {6,S}
6   C                      u0 r1 {5,S} {7,S}
7   C                      u0 r1 {4,S} {6,S}
8   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15821,-4.76811,-6.44629,-6.85852,-6.0076,-6.11068,-3.67432],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.3431,'kcal/mol','+|-',5.2),
        S298 = (-3.43926,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1[CH]C(=C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 43,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_N-Sp-7R!H-4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux {1,S} {7,[B,D,T,Q]}
5   C ux {2,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
7   C ux {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.31403,-3.89035,-4.65312,-5.17153,-5.68332,-5.84668,-6.23603],'cal/mol/K','+|-',[3.90301,7.19226,5.64582,3.26444,3,3,4.06956]),
        H298 = (74.1142,'kcal/mol','+|-',7.58513),
        S298 = (3.18434,'cal/mol/K','+|-',3.97693),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 44,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_N-Sp-7R!H-4C_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {7,[B,D,T,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,S}
6   C   ux r1 {5,S} {8,[S,D,T,B,Q]}
7   C   ux r1 {4,[B,D,T,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.69395,-6.4332,-6.64922,-6.32569,-5.48423,-4.99455,-4.79723],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (71.4325,'kcal/mol','+|-',5.2),
        S298 = (4.5904,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 45,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_4C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux r1 {1,S}
5   C ux r1 {2,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.812109,0.166506,-0.876585,-1.51058,-2.54835,-3.31103,-4.75363],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.0157,'kcal/mol','+|-',5.2),
        S298 = (0.639767,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 46,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_N-4C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux r0 {1,S}
5   C ux r1 {2,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0583814,-1.24522,-2.1542,-2.47424,-3.30765,-3.99042,-4.88553],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.8814,'kcal/mol','+|-',5.2),
        S298 = (1.11552,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CC[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 47,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   C   u0 {1,S}
5   O   u0 r1 {2,S} {6,S}
6   R!H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.76728,-3.68803,-4.8084,-5.06539,-5.079,-4.70816,-6.88854],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.7128,'kcal/mol','+|-',5.2),
        S298 = (10.3923,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1OC[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 48,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {1,S}
5   C   ux {2,[S,D,T,B,Q]} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.57211,-0.751624,-1.22317,-1.64317,-2.3563,-2.91683,-3.96927],'cal/mol/K','+|-',[3.0004,3.34011,3.51097,3.83832,4.31816,4.57887,4.09246]),
        H298 = (75.8237,'kcal/mol','+|-',36.9258),
        S298 = (0.0227544,'cal/mol/K','+|-',4.79534),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 49,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_Sp-7R!H=4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {1,S} {7,D}
5   C ux {2,[S,D,T,B,Q]} {6,D}
6   C ux {5,D}
7   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72293,-1.83394,-2.2827,-2.79604,-3.59901,-4.13141,-4.85269],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (57.6098,'kcal/mol','+|-',5.2),
        S298 = (0.547788,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 50,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_Sp-7R!H=4C_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {7,D}
5   C   u0 r1 {2,S} {6,D}
6   C   u0 r1 {5,D} {8,[S,D,T,B,Q]}
7   C   ux r1 {4,D}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8382,-2.05432,-2.60122,-3.10812,-3.88834,-4.4,-5.07116],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (57.3519,'kcal/mol','+|-',5.2),
        S298 = (1.54882,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC(C)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 51,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_Sp-7R!H=4C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux r1 {1,S} {7,D} {8,[S,D,T,B,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,D}
6   C   ux r1 {5,D}
7   C   ux r1 {4,D}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8382,-2.05432,-2.60122,-3.10812,-3.88834,-4.4,-5.07116],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (57.7019,'kcal/mol','+|-',5.2),
        S298 = (1.23882,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C(C)=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 52,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_Sp-7R!H=4C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D} {8,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {7,D}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,D}
6   C   ux r1 {5,D}
7   C   ux r1 {4,D}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.82845,-2.06764,-2.43909,-2.80256,-3.40275,-3.82578,-4.51612],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (57.8169,'kcal/mol','+|-',5.2),
        S298 = (-0.281388,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C1[CH]C=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 53,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_N-Sp-7R!H=4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D} {5,S}
3   C   u0 {2,D}
4   C   u0 {1,S} {7,[S,T,Q,B]}
5   C   u0 {2,S} {6,D}
6   R!H u0 {5,D}
7   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.844283,0.580454,0.0808657,-0.224241,-0.826816,-1.42196,-2.88198],'cal/mol/K','+|-',[3,3.90947,4.55794,5.13813,6.17392,7.06365,7.08218]),
        H298 = (88.6178,'kcal/mol','+|-',15.1571),
        S298 = (-0.623441,'cal/mol/K','+|-',9.04644),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 54,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_N-Sp-7R!H=4C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {8,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {7,[S,T,Q,B]}
5   C   u0 {2,S} {6,D}
6   R!H u0 {5,D}
7   R!H ux {4,[S,T,Q,B]}
8   R!H ux {1,[S,D,T,B,Q]}
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
    index = 55,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.619133,-3.21399,-3.90708,-4.12395,-4.26211,-4.41116,-4.86407],'cal/mol/K','+|-',[3,6.47669,6.67161,6.0842,4.38103,3.02958,3]),
        H298 = (79.7935,'kcal/mol','+|-',17.6873),
        S298 = (2.65743,'cal/mol/K','+|-',8.84469),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 56,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {1,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.950688,-1.86841,-2.56748,-2.91801,-3.43187,-3.90919,-4.67031],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.4084,'kcal/mol','+|-',14.5421),
        S298 = (0.949622,'cal/mol/K','+|-',5.45388),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 57,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D}
4   C ux {1,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.233,-2.15867,-2.82115,-3.11613,-3.53792,-3.9821,-4.64574],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.8229,'kcal/mol','+|-',11.9296),
        S298 = (0.626901,'cal/mol/K','+|-',4.52827),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 58,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D} {6,S}
4   C ux {1,S}
5   C ux {2,[S,D,T,B,Q]}
6   C u0 {3,S} {7,D}
7   C ux {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09118,-1.57682,-2.05286,-2.41722,-3.07622,-3.64818,-4.68045],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.1038,'kcal/mol','+|-',19.6574),
        S298 = (1.79082,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 59,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {6,S}
4   C   ux r1 {1,S} {8,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]}
6   C   u0 r1 {3,S} {7,D}
7   C   ux {6,D}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5102,-2.16832,-2.82522,-3.16012,-3.74134,-4.24,-5.11916],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (61.6449,'kcal/mol','+|-',5.2),
        S298 = (2.31582,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C(C)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 60,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux {1,S}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]} {7,[S,T,Q,B]}
7   R!H ux {6,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3208,-2.51887,-3.29676,-3.54878,-3.82373,-4.18882,-4.62425],'cal/mol/K','+|-',[3,3,3.43409,3.23567,3,3,3.0018]),
        H298 = (77.8352,'kcal/mol','+|-',10.2253),
        S298 = (-0.0936182,'cal/mol/K','+|-',5.44481),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 61,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   C   u0 r1 {2,D} {6,[S,D,T,B,Q]}
4   C   u0 {1,S} {8,S}
5   C   u0 {2,S}
6   C   ux {3,[S,D,T,B,Q]} {7,S}
7   R!H u0 {6,S}
8   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.00932,-3.59954,-4.56716,-4.58707,-4.3243,-4.22613,-3.52514],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2928,'kcal/mol','+|-',5.2),
        S298 = (-2.78754,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 62,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4C-R_7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   C   u0 r1 {2,D} {6,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {8,S}
5   C   u0 r0 {2,S}
6   C   ux r1 {3,[S,D,T,B,Q]} {7,S}
7   C   u0 {6,S}
8   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21219,-3.6137,-4.46654,-4.58689,-4.29364,-4.18652,-3.69992],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2073,'kcal/mol','+|-',5.2),
        S298 = (-2.30742,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1[CH]C(C)=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 63,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4C-R_N-7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   C   u0 r1 {2,D} {6,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {8,S}
5   C   u0 r0 {2,S}
6   C   ux r1 {3,[S,D,T,B,Q]} {7,S}
7   O   u0 {6,S}
8   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.80645,-3.58537,-4.66777,-4.58725,-4.35496,-4.26574,-3.35036],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.3783,'kcal/mol','+|-',5.2),
        S298 = (-3.26766,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1C=C(C)[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 64,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_4C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H ux r1 {3,[S,D,T,B,Q]} {7,[S,T,Q,B]}
7   C   ux r1 {6,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.920994,-1.27723,-1.63084,-1.98616,-2.67906,-3.31806,-4.52466],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (75.2125,'kcal/mol','+|-',2.4),
        S298 = (0.860492,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CCC=C[CH]1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 65,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-4C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r0 {1,S}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H ux r1 {3,[S,D,T,B,Q]} {7,[S,T,Q,B]}
7   C   ux r1 {6,[S,T,Q,B]}
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
    index = 66,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_N-3C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {5,S}
3   C u0 r0 {2,D}
4   C u0 {1,S}
5   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.249155,-0.634807,-1.48939,-2.07601,-2.98115,-3.59932,-4.77475],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.0223,'kcal/mol','+|-',11.6569),
        S298 = (2.32118,'cal/mol/K','+|-',10.3842),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 67,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_N-3C-inRing_4C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {5,S}
3   C u0 r0 {2,D}
4   C u0 r1 {1,S}
5   C u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0261985,-0.254108,-0.777217,-1.38328,-2.36156,-3.1355,-4.37522],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.901,'kcal/mol','+|-',5.2),
        S298 = (-1.35017,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 68,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_N-3C-inRing_N-4C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {5,S}
3   C u0 r0 {2,D}
4   C u0 r0 {1,S}
5   C u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.524508,-1.01551,-2.20155,-2.76874,-3.60074,-4.06313,-5.17429],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.1437,'kcal/mol','+|-',5.2),
        S298 = (5.99254,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 69,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {1,S}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.54131,-7.92352,-8.59566,-8.34474,-7.16797,-6.16806,-5.54224],'cal/mol/K','+|-',[4.47495,7.56639,7.85664,7.39025,5.73589,4.19446,3]),
        H298 = (92.0286,'kcal/mol','+|-',8.27906),
        S298 = (8.63474,'cal/mol/K','+|-',7.98071),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 70,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_N-5R!H->C_Ext-4C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {1,S} {6,[S,D,T,B,Q]}
5   O   ux {2,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]} {7,S}
7   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.71392,-10.0003,-10.7524,-10.3769,-8.74948,-7.32643,-5.98605],'cal/mol/K','+|-',[3,3.31532,3.43762,3.18136,3,3,3]),
        H298 = (90.2495,'kcal/mol','+|-',7.81763),
        S298 = (10.5603,'cal/mol/K','+|-',6.19628),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 71,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_N-5R!H->C_Ext-4C-R_Ext-6R!H-R_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   O   ux r0 {2,[S,D,T,B,Q]}
6   C   ux r1 {4,[S,D,T,B,Q]} {7,S}
7   R!H u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.65268,-8.82813,-9.53701,-9.2521,-7.90001,-6.71573,-5.61254],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.4855,'kcal/mol','+|-',5.2),
        S298 = (8.36961,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CCOC=C[CH]1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 72,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_N-5R!H->C_Ext-4C-R_Ext-6R!H-R_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   O   ux r0 {2,[S,D,T,B,Q]}
6   O   ux r1 {4,[S,D,T,B,Q]} {7,S}
7   R!H u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.775149,-11.1724,-11.9678,-11.5017,-9.59895,-7.93713,-6.35955],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.0134,'kcal/mol','+|-',5.2),
        S298 = (12.751,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CC=COC[CH]1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 73,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.112779,-1.77609,-3.04887,-3.46431,-3.69343,-3.62325,-4.31451],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.4952,'kcal/mol','+|-',5.2),
        S298 = (5.0855,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[C]1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 74,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.312397,-0.809614,-1.88723,-2.59128,-3.4283,-4.16035,-5.08238],'cal/mol/K','+|-',[3.13439,3,3.52348,3.92958,3.93025,4.0095,3.71028]),
        H298 = (90.7489,'kcal/mol','+|-',22.2685),
        S298 = (0.973213,'cal/mol/K','+|-',5.55496),
    ),
    shortDesc = """Radical correction fitted to 39 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 75,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {1,S}
5   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.18422,-0.850458,-1.85454,-2.49439,-3.22708,-3.88941,-4.64826],'cal/mol/K','+|-',[3.30712,3.36798,3.75874,3.81317,3.31819,3.20103,3.13966]),
        H298 = (86.6304,'kcal/mol','+|-',16.3716),
        S298 = (0.511772,'cal/mol/K','+|-',5.82127),
    ),
    shortDesc = """Radical correction fitted to 24 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 76,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {1,S}
5   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.325348,-0.672278,-1.69075,-2.36319,-3.1904,-3.96694,-4.55447],'cal/mol/K','+|-',[3.49264,3.00919,3.17382,3.41395,3.28673,3.34037,3]),
        H298 = (83.35,'kcal/mol','+|-',11.4847),
        S298 = (-0.0627831,'cal/mol/K','+|-',5.75085),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 77,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux {1,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.415704,-0.50957,-1.46836,-2.11469,-2.97909,-3.73238,-4.61087],'cal/mol/K','+|-',[3.0325,3,3,3,3,3,3]),
        H298 = (82.3306,'kcal/mol','+|-',8.41616),
        S298 = (-0.686582,'cal/mol/K','+|-',6.19017),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 78,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-1C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,D} {5,S}
3   O u0 {2,D}
4   O u0 {1,S}
5   C u0 {2,S}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.1701,1.61734,0.210655,-0.279186,-0.945554,-1.65186,-1.77931],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.3682,'kcal/mol','+|-',9.4368),
        S298 = (-6.93158,'cal/mol/K','+|-',4.82839),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 79,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-1C-R_Ext-6R!H-R_Sp-7R!H-6R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,D} {5,S}
3   O u0 {2,D}
4   O u0 {1,S}
5   C u0 r1 {2,S}
6   C ux r1 {1,[S,D,T,B,Q]} {7,S}
7   C u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.91442,1.6686,0.359309,-0.0393006,-0.682233,-1.32754,-1.91388],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (76.7046,'kcal/mol','+|-',5.2),
        S298 = (-8.63867,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=CC[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 80,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-1C-R_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,D} {5,S}
3   O u0 {2,D}
4   O u0 {1,S}
5   C u0 r1 {2,S}
6   C ux r1 {1,[S,D,T,B,Q]} {7,[B,D,T,Q]}
7   C u0 r1 {6,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.42579,1.56609,0.062002,-0.519071,-1.20887,-1.97619,-1.64473],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (70.0318,'kcal/mol','+|-',5.2),
        S298 = (-5.22448,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CC=C[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 81,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,S} {6,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.148655,-0.80118,-1.77305,-2.46398,-3.35631,-4.12795,-5.09203],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.6071,'kcal/mol','+|-',6.70618),
        S298 = (0.26769,'cal/mol/K','+|-',4.07783),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 82,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,S} {6,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.400722,-0.946162,-2.19077,-2.94464,-3.79698,-4.59651,-5.46835],'cal/mol/K','+|-',[3,3,3,3.14522,3,3,3]),
        H298 = (80.0523,'kcal/mol','+|-',5.2),
        S298 = (-0.210843,'cal/mol/K','+|-',4.74284),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 83,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,S} {6,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {7,S}
6   R!H ux {4,[S,D,T,B,Q]}
7   C   ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.982713,-1.14693,-3.0216,-3.89987,-4.58531,-5.36179,-6.14231],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.5456,'kcal/mol','+|-',5.2),
        S298 = (0.6659,'cal/mol/K','+|-',5.88777),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 84,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C_Ext-5C-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux {1,S} {6,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]} {7,S} {8,S}
6   O ux {4,[S,D,T,B,Q]}
7   C u0 {5,S}
8   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.814889,-0.991186,-2.57952,-3.34845,-3.88654,-4.7643,-5.98366],'cal/mol/K','+|-',[3,3,3.20267,3.54506,3.82699,3.7592,3]),
        H298 = (79.556,'kcal/mol','+|-',5.2),
        S298 = (-0.527747,'cal/mol/K','+|-',7.09524),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 85,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C_Ext-5C-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {7,S} {8,S}
6   O   ux r1 {4,[S,D,T,B,Q]}
7   C   u0 r0 {5,S} {9,[S,D,T,B,Q]}
8   C   u0 r0 {5,S}
9   R!H ux {7,[S,D,T,B,Q]}
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
    index = 86,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C ux r1 {2,[S,D,T,B,Q]} {7,S}
6   C ux r1 {4,[S,D,T,B,Q]}
7   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.26807,-2.54597,-4.50458,-5.42597,-5.77062,-5.95276,-6.14586],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.7382,'kcal/mol','+|-',5.2),
        S298 = (3.82355,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 87,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C ux r1 {2,[S,D,T,B,Q]} {7,S}
6   O ux r1 {4,[S,D,T,B,Q]}
7   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.56914,-0.0593997,-2.42279,-3.4766,-4.79754,-5.96579,-6.45607],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.3324,'kcal/mol','+|-',5.2),
        S298 = (-0.104457,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 88,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   O   u0 {2,D}
4   O   u0 {1,S} {6,S}
5   C   u0 {2,S} {7,[B,D,T,Q]}
6   O   u0 {4,S}
7   R!H ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.315575,-0.699057,-1.16822,-1.76898,-2.82673,-3.65462,-4.63886],'cal/mol/K','+|-',[3.89904,3,3,3,3,3,3]),
        H298 = (79.0033,'kcal/mol','+|-',5.2),
        S298 = (-1.28991,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 89,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {5,S}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S} {6,S}
5   C u0 r1 {2,S} {7,[B,D,T,Q]}
6   O u0 r1 {4,S}
7   C ux {5,[B,D,T,Q]}
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
    index = 90,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C_N-7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {5,S}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S} {6,S}
5   C u0 r1 {2,S} {7,[B,D,T,Q]}
6   O u0 r1 {4,S}
7   O ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.16389,-1.25252,-1.42202,-1.88444,-2.74583,-3.43949,-4.56067],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (79.5399,'kcal/mol','+|-',2.4),
        S298 = (-1.16848,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]OOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 91,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C ux r1 {2,[S,D,T,B,Q]}
6   C ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.615007,-0.791594,-1.23429,-1.76218,-2.62956,-3.32902,-4.48318],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (85.966,'kcal/mol','+|-',2.4),
        S298 = (0.0494729,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]OC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 92,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C ux r1 {2,[S,D,T,B,Q]}
6   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.100099,-0.343605,-0.965822,-1.61697,-2.66313,-3.41707,-4.48827],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (84.5242,'kcal/mol','+|-',2.4),
        S298 = (2.02784,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]OOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 93,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux {1,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.184304,-0.926261,-2.0379,-2.7511,-3.52025,-4.33309,-4.46644],'cal/mol/K','+|-',[4.33491,4.04567,4.10913,4.33747,4.19116,4.28418,3]),
        H298 = (85.4199,'kcal/mol','+|-',16.3355),
        S298 = (0.910952,'cal/mol/K','+|-',4.78781),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 94,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux {1,S}
5   C ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.162879,-1.11854,-2.36918,-3.08968,-3.86409,-4.70072,-4.38232],'cal/mol/K','+|-',[5.42267,5.36434,5.3566,5.61643,5.41753,5.48939,3]),
        H298 = (91.3262,'kcal/mol','+|-',11.7836),
        S298 = (0.964364,'cal/mol/K','+|-',4.83797),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 95,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux {1,S} {7,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.125256,-1.58198,-2.9176,-3.71717,-4.4216,-5.26559,-4.62587],'cal/mol/K','+|-',[6.89154,6.58836,6.4425,6.71394,6.56503,6.66574,3.65407]),
        H298 = (88.6304,'kcal/mol','+|-',9.50289),
        S298 = (0.065108,'cal/mol/K','+|-',4.82059),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 96,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R_Sp-7R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux {1,S} {7,S}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
7   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.74097,-3.03589,-4.1816,-4.86574,-5.28262,-5.96891,-5.09615],'cal/mol/K','+|-',[3,3.7917,4.89018,5.9962,6.84522,7.4011,3.83671]),
        H298 = (90.654,'kcal/mol','+|-',6.09691),
        S298 = (0.69762,'cal/mol/K','+|-',5.02548),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 97,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R_Sp-7R!H-4C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D} {5,S}
3   O   u0 {2,D}
4   C   u0 r1 {1,S} {7,S}
5   C   u0 r1 {2,S} {6,S}
6   O   ux {5,S}
7   R!H ux r1 {4,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8097,-4.72208,-6.24012,-7.14373,-7.72083,-8.56598,-6.39829],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.1743,'kcal/mol','+|-',5.2),
        S298 = (2.7401,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 98,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R_Sp-7R!H-4C_6O-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux r1 {1,S} {7,S}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.34247,-3.40185,-4.82577,-5.98432,-6.75713,-7.609,-5.997],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.0575,'kcal/mol','+|-',5.2),
        S298 = (1.46106,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 99,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R_Sp-7R!H-4C_N-6O-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux r1 {1,S} {7,S}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux r0 {5,[S,D,T,B,Q]}
7   R!H ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0707311,-0.983738,-1.47892,-1.46916,-1.36989,-1.73175,-2.89318],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.7303,'kcal/mol','+|-',5.2),
        S298 = (-2.1083,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 100,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R_N-Sp-7R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S} {7,[B,D,T,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   u0 {5,[S,D,T,B,Q]}
7   R!H u0 r1 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.72188,2.77977,0.874412,-0.271459,-1.83855,-3.15562,-3.21502],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.5594,'kcal/mol','+|-',5.2),
        S298 = (-1.83243,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]C=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 101,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux r1 {1,S}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.474151,-0.838972,-2.02333,-2.50465,-3.31143,-4.07778,-4.06159],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.6659,'kcal/mol','+|-',5.2),
        S298 = (3.79362,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1C(=O)C2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 102,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_N-6R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux {1,S}
5   C ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.21455,-0.654814,-1.57021,-2.27311,-3.03484,-3.81408,-4.5852],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.1263,'kcal/mol','+|-',12.3609),
        S298 = (0.835548,'cal/mol/K','+|-',5.84927),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 103,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_N-6R!H->O_4C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux r1 {1,S}
5   C ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.233865,-0.68256,-1.51733,-2.16541,-3.05494,-3.84306,-4.41236],'cal/mol/K','+|-',[3.94883,3,3,3,3,3,3]),
        H298 = (78.4988,'kcal/mol','+|-',6.53249),
        S298 = (1.27279,'cal/mol/K','+|-',7.50513),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 104,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_N-6R!H->O_4C-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S} {7,[S,D,T,B,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   u0 {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.16696,-0.300265,-2.0402,-2.98343,-3.89219,-4.87926,-4.18068],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.6909,'kcal/mol','+|-',5.2),
        S298 = (4.94682,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 105,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_N-6R!H->O_N-4C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,S}
3   O u0 {2,D}
4   C u0 r0 {1,S}
5   C u0 r1 {2,S} {6,S}
6   C ux r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.151776,-0.564641,-1.74205,-2.62315,-2.96949,-3.71989,-5.14693],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.3937,'kcal/mol','+|-',5.2),
        S298 = (-0.585488,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 106,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {1,S}
5   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.385719,-1.57003,-2.51601,-3.02423,-3.3752,-3.5763,-5.02701],'cal/mol/K','+|-',[3,4.93212,6.1787,5.79723,4.03002,3,5.61915]),
        H298 = (97.7119,'kcal/mol','+|-',8.63957),
        S298 = (2.83209,'cal/mol/K','+|-',3.70281),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 107,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing_Ext-4R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D} {5,S}
3   O   u0 {2,D}
4   R!H u0 r1 {1,S} {6,S}
5   C   u0 {2,S}
6   R!H u0 r1 {4,S}
7   R!H ux {1,[S,D,T,B,Q]}
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
    index = 108,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing_4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux {1,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0175556,-0.680636,-1.38424,-2.00713,-2.78825,-3.17542,-4.05635],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.4045,'kcal/mol','+|-',2.4),
        S298 = (2.62679,'cal/mol/K','+|-',4.62669),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 109,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing_4R!H->O_Ext-4O-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux r1 {1,S} {6,S}
5   C ux {2,[S,D,T,B,Q]}
6   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.148482,-0.931732,-1.64714,-2.17503,-2.62153,-2.90498,-3.8919],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.7538,'kcal/mol','+|-',2.4),
        S298 = (0.99101,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 110,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing_4R!H->O_Ext-4O-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C                      ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O                      ux {2,D}
4   O                      ux r1 {1,S} {6,S}
5   C                      ux {2,[S,D,T,B,Q]}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.113371,-0.42954,-1.12134,-1.83922,-2.95497,-3.44587,-4.22081],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.0552,'kcal/mol','+|-',2.4),
        S298 = (4.26257,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 111,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux r1 {1,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.383725,-0.713504,-1.51362,-1.87153,-2.08295,-2.55768,-3.84323],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.789,'kcal/mol','+|-',5.2),
        S298 = (4.56458,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 112,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {1,S}
5   O   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.498965,-0.750163,-1.93482,-2.73232,-3.7212,-4.55472,-5.71428],'cal/mol/K','+|-',[3,3,3.29199,4.23158,4.76828,4.99979,4.2229]),
        H298 = (96.2741,'kcal/mol','+|-',25.0933),
        S298 = (1.64487,'cal/mol/K','+|-',5.05185),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 113,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux {1,S}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.427363,-0.838069,-1.94937,-2.68175,-3.67524,-4.51521,-5.80187],'cal/mol/K','+|-',[3.26889,3,3,3.72221,4.60757,5.04308,4.64952]),
        H298 = (98.3404,'kcal/mol','+|-',29.0587),
        S298 = (1.40513,'cal/mol/K','+|-',5.4428),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 114,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux {1,S}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.674207,-0.807184,-2.11118,-2.96509,-4.0831,-4.97304,-6.23162],'cal/mol/K','+|-',[3.44583,3,3.2467,3.94898,4.61072,5.0003,4.6735]),
        H298 = (95.4919,'kcal/mol','+|-',30.8231),
        S298 = (0.518107,'cal/mol/K','+|-',3.91757),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 115,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux {1,S} {6,[S,D,T,B,Q]}
5   O   ux {2,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.28974,-0.675459,-2.41282,-3.50171,-4.85606,-5.83719,-7.20254],'cal/mol/K','+|-',[3.59738,3,3.77125,4.51526,5.0846,5.46631,4.71959]),
        H298 = (93.0856,'kcal/mol','+|-',42.957),
        S298 = (0.111278,'cal/mol/K','+|-',4.72762),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 116,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux {1,S} {6,S}
5   O   ux {2,[S,D,T,B,Q]}
6   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.28201,-0.573898,-2.98386,-4.41104,-6.12093,-7.325,-8.7792],'cal/mol/K','+|-',[3,3.72901,4.51309,4.955,4.92265,4.84188,3]),
        H298 = (111.898,'kcal/mol','+|-',19.7568),
        S298 = (0.439788,'cal/mol/K','+|-',5.92563),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 117,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux {1,S} {6,S}
5   O ux {2,[S,D,T,B,Q]}
6   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19182,-1.08866,-3.38963,-4.98706,-6.48305,-7.3844,-9.08806],'cal/mol/K','+|-',[3,6.59431,8.55006,9.15568,9.04423,8.86597,3]),
        H298 = (105.29,'kcal/mol','+|-',30.5791),
        S298 = (1.94502,'cal/mol/K','+|-',5.72343),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 118,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S} {6,S} {7,[S,D,T,B,Q]}
5   O   ux r1 {2,[S,D,T,B,Q]}
6   C   u0 r1 {4,S}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 119,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux {1,S} {6,S}
5   O ux {2,[S,D,T,B,Q]}
6   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.0088,-0.23072,-2.71335,-4.02702,-5.87952,-7.28539,-8.57329],'cal/mol/K','+|-',[3,3,3,3,3,3,3.46607]),
        H298 = (116.303,'kcal/mol','+|-',5.2),
        S298 = (-0.5637,'cal/mol/K','+|-',6.22435),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 120,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux {1,S} {6,S}
5   O   ux r1 {2,[S,D,T,B,Q]}
6   O   u0 {4,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
    index = 121,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux r1 {1,S} {6,S}
5   O   ux r1 {2,[S,D,T,B,Q]}
6   O   ux r1 {4,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.15952,0.946463,-1.8956,-2.98527,-4.59025,-5.94737,-6.70593],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (114.426,'kcal/mol','+|-',5.2),
        S298 = (-4.10355,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1OOC(O)[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 122,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_N-Sp-6R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,S}
3   O u0 {2,D}
4   C u0 {1,S} {6,[B,D,T,Q]}
5   O u0 {2,S}
6   C ux {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.236815,-0.831707,-1.53431,-2.10274,-2.91011,-3.54825,-4.77691],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (76.5676,'kcal/mol','+|-',5.2),
        S298 = (-0.394122,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 123,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_N-Sp-6R!H-4C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D} {5,S}
3   O   u0 {2,D}
4   C   u0 r1 {1,S} {6,[B,D,T,Q]}
5   O   u0 r1 {2,S}
6   C   ux r1 {4,[B,D,T,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.852467,-0.487298,-1.73659,-2.44364,-3.19425,-3.7724,-5.31954],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.6042,'kcal/mol','+|-',5.2),
        S298 = (-1.60629,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]1C=COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 124,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux r1 {1,S}
5   O   ux r1 {2,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06989,-1.90248,-2.30765,-2.51525,-2.92811,-3.62094,-4.54172],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.6911,'kcal/mol','+|-',2.4),
        S298 = (1.38837,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 125,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_N-2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r0 {1,S} {3,D} {5,S}
3   O u0 {2,D}
4   C u0 {1,S}
5   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.541025,-0.959231,-1.31456,-1.57015,-2.07515,-2.71911,-4.11594],'cal/mol/K','+|-',[3,3,3,3,4.33575,4.93644,3.84926]),
        H298 = (108.387,'kcal/mol','+|-',5.2),
        S298 = (4.88496,'cal/mol/K','+|-',6.34877),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 126,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_N-2R!H-inRing_Ext-5O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r0 {1,S} {3,D} {5,S}
3   O   u0 {2,D}
4   C   u0 r1 {1,S}
5   O   u0 r0 {2,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 127,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux {1,S}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.675217,-0.53378,-1.89902,-2.85681,-3.83434,-4.65197,-5.49866],'cal/mol/K','+|-',[3,3,4.676,6.10803,6.01704,5.77847,3.5759]),
        H298 = (91.5972,'kcal/mol','+|-',11.2138),
        S298 = (2.235,'cal/mol/K','+|-',4.48674),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 128,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_N-4R!H->C_4O-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux r1 {1,S}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.289338,-0.869481,-2.02678,-2.87538,-3.79955,-4.50895,-5.22053],'cal/mol/K','+|-',[3,3,5.33582,7.05061,6.94299,6.6078,3.72313]),
        H298 = (90.3626,'kcal/mol','+|-',5.77854),
        S298 = (2.23689,'cal/mol/K','+|-',5.17986),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 129,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux r1 {1,S} {6,S}
5   O ux {2,[S,D,T,B,Q]}
6   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.448216,-1.09491,-2.67165,-3.76566,-4.69548,-5.37181,-5.712],'cal/mol/K','+|-',[3,3.20566,7.87126,10.3272,10.131,9.62116,5.41002]),
        H298 = (88.8539,'kcal/mol','+|-',7.27594),
        S298 = (3.05176,'cal/mol/K','+|-',7.22098),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 130,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R_Ext-5O-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   O   ux r1 {1,S} {6,S}
5   O   ux r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   u0 r1 {4,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3316,-2.6642,-6.52491,-8.82121,-9.65498,-10.0817,-8.36039],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.0953,'kcal/mol','+|-',5.2),
        S298 = (6.58669,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(OO)CO[CH]C(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 131,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_N-4R!H->C_N-4O-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux r0 {1,S}
5   O ux r1 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.79755,1.31258,-1.19632,-2.75465,-4.02573,-5.43856,-7.02839],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (104.423,'kcal/mol','+|-',5.2),
        S298 = (2.22462,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1O[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 132,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.38941,-1.11658,-2.12305,-2.62935,-3.21353,-3.68949,-4.53399],'cal/mol/K','+|-',[3.06889,3.4459,3.48777,3.1372,3,3,3]),
        H298 = (80.0733,'kcal/mol','+|-',14.5741),
        S298 = (-0.736657,'cal/mol/K','+|-',8.12366),
    ),
    shortDesc = """Radical correction fitted to 119 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 133,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
4   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.448155,-0.783953,-1.68143,-2.32703,-3.08965,-3.6578,-4.83033],'cal/mol/K','+|-',[3,4.25705,4.34842,4.13479,3.42651,3,3]),
        H298 = (76.8236,'kcal/mol','+|-',21.4291),
        S298 = (1.09559,'cal/mol/K','+|-',7.57826),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 134,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   O ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.174228,-0.643902,-1.39338,-1.93661,-2.60532,-3.32556,-4.53088],'cal/mol/K','+|-',[3.8032,4.63389,4.29078,3.84505,3.17045,3,3]),
        H298 = (74.1135,'kcal/mol','+|-',31.8488),
        S298 = (-0.0781332,'cal/mol/K','+|-',5.79144),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 135,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O_Sp-5R!H-3R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {3,S} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.402184,0.112819,-0.670653,-1.29275,-2.0973,-2.89114,-4.2796],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.2442,'kcal/mol','+|-',20.8111),
        S298 = (-0.85441,'cal/mol/K','+|-',4.03217),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 136,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O_Sp-5R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C   u0 r1 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   O   u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C   u0 r1 {3,S} {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
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
    index = 137,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O_Sp-5R!H-3R!H_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C   ux r1 {3,S} {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.863408,0.881541,-0.491456,-1.35095,-2.0341,-3.0728,-4.33085],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.4227,'kcal/mol','+|-',5.2),
        S298 = (-1.48193,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1C=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 138,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O_Sp-5R!H-3R!H_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C   ux r1 {3,S} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.319095,-0.512593,-1.01195,-1.59419,-2.52122,-3.26599,-4.48164],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (79.6482,'kcal/mol','+|-',2.4),
        S298 = (0.437887,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 139,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O_N-Sp-5R!H-3R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,D}
4   O ux r1 {1,S} {5,S}
5   C ux r1 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.92091,-5.56259,-6.09112,-6.12172,-5.90744,-6.14934,-6.16425],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (38.4575,'kcal/mol','+|-',5.2),
        S298 = (4.96767,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=C[CH]OC=1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 140,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   O ux {1,S}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.944146,-0.914134,-1.54962,-2.10699,-2.94223,-3.44139,-4.38075],'cal/mol/K','+|-',[3,5.2331,4.79986,4.14917,3.33048,3.17086,3]),
        H298 = (75.0794,'kcal/mol','+|-',12.7593),
        S298 = (0.343659,'cal/mol/K','+|-',7.29732),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 141,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-1C-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux {1,S}
5   C ux {3,S} {6,D}
6   C ux {5,D}
7   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.485345,0.0286783,-0.501807,-0.886567,-1.74091,-2.38066,-3.51263],'cal/mol/K','+|-',[3,3,3,3,3,3.62419,3.21361]),
        H298 = (69.5359,'kcal/mol','+|-',5.2),
        S298 = (-2.33509,'cal/mol/K','+|-',6.58889),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 142,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-1C-R_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r0 {1,S} {8,[S,D,T,B,Q]}
5   C   ux r1 {3,S} {6,D}
6   C   ux r1 {5,D}
7   C   u0 r1 {1,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.378745,-0.0657631,-0.643626,-1.26552,-2.39298,-3.16918,-4.21182],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (69.0231,'kcal/mol','+|-',2.4),
        S298 = (-0.901534,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(O[C]1CC=CC=C1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 143,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   O   ux {1,S}
5   C   ux r1 {3,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.698985,-0.498543,-1.58796,-2.31018,-3.06332,-3.40609,-4.23213],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (80.4529,'kcal/mol','+|-',2.4),
        S298 = (2.00601,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(O[C]1CCC=C1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 144,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r1 {1,S}
5   C ux r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.75714,-6.65719,-6.66543,-6.37222,-5.62915,-5.08672,-5.08307],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.6887,'kcal/mol','+|-',5.2),
        S298 = (5.9612,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CCO[CH]C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 145,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C_N-Sp-5C-3R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,D}
4   O ux r1 {1,S}
5   C ux r1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17387,0.829705,0.247029,-1.35094,-3.88713,-5.32283,-6.83417],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.8117,'kcal/mol','+|-',5.2),
        S298 = (-0.308255,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=C=C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 146,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   O ux {1,S}
5   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.628717,-0.798053,-2.28124,-3.19913,-3.99214,-4.44157,-5.90037],'cal/mol/K','+|-',[3.3091,3.82127,5.23939,5.47254,4.38717,3.38213,3.09502]),
        H298 = (83.9957,'kcal/mol','+|-',15.137),
        S298 = (3.84653,'cal/mol/K','+|-',9.69868),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 147,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   O ux {1,S}
5   O ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.94867,-1.37402,-3.51419,-4.60941,-5.22083,-5.39339,-6.97244],'cal/mol/K','+|-',[4.34773,4.74067,5.44964,5.27017,3.82221,3,3]),
        H298 = (89.0399,'kcal/mol','+|-',16.0777),
        S298 = (6.05608,'cal/mol/K','+|-',10.3122),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 148,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_Sp-7R!H-6R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   O u0 {1,S}
5   O u0 {3,[S,D,T,B,Q]} {6,S}
6   C u0 {5,S} {7,S}
7   C ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.14298,-2.7399,-5.06229,-6.07141,-6.10462,-5.93637,-7.22421],'cal/mol/K','+|-',[3.03393,3,3,3,3.23616,3.16924,3]),
        H298 = (93.1892,'kcal/mol','+|-',10.1873),
        S298 = (8.83283,'cal/mol/K','+|-',5.25684),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 149,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   O   u0 r1 {1,S} {8,[S,D,T,B,Q]}
5   O   u0 r1 {3,[S,D,T,B,Q]} {6,S}
6   C   u0 r1 {5,S} {7,S}
7   C   ux {6,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.929675,-2.88681,-5.54686,-6.80031,-7.24877,-7.05686,-7.70859],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.791,'kcal/mol','+|-',5.2),
        S298 = (10.6914,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=COCC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 150,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r1 {1,S}
5   O ux r1 {3,S} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]} {7,[B,D,T,Q]}
7   C u0 {6,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.13197,1.35774,-0.417992,-1.68539,-3.45327,-4.30743,-6.46891],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.7413,'kcal/mol','+|-',5.2),
        S298 = (0.502589,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=COC=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 151,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.38068,-1.16602,-2.18868,-2.67428,-3.23194,-3.6942,-4.48994],'cal/mol/K','+|-',[3.10457,3.32936,3.3544,3,3,3,3]),
        H298 = (80.608,'kcal/mol','+|-',13.0962),
        S298 = (-1.00897,'cal/mol/K','+|-',8.10393),
    ),
    shortDesc = """Radical correction fitted to 105 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 152,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.387214,-1.1596,-2.18423,-2.67179,-3.23169,-3.69108,-4.48682],'cal/mol/K','+|-',[3.11242,3.33843,3.36534,3,3,3,3]),
        H298 = (80.5636,'kcal/mol','+|-',13.07),
        S298 = (-1.05822,'cal/mol/K','+|-',8.0517),
    ),
    shortDesc = """Radical correction fitted to 104 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 153,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.389584,-1.17173,-2.20324,-2.68926,-3.24454,-3.70003,-4.49063],'cal/mol/K','+|-',[3.12368,3.339,3.34864,3,3,3,3]),
        H298 = (80.5465,'kcal/mol','+|-',13.0955),
        S298 = (-1.04238,'cal/mol/K','+|-',8.0736),
    ),
    shortDesc = """Radical correction fitted to 103 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 154,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.902074,-0.509831,-1.67853,-2.26203,-2.92353,-3.45311,-4.29593],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.1741,'kcal/mol','+|-',5.25891),
        S298 = (-0.766948,'cal/mol/K','+|-',7.57436),
    ),
    shortDesc = """Radical correction fitted to 36 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 155,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.9758,-0.502906,-1.70938,-2.29642,-2.95923,-3.49171,-4.25498],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.2542,'kcal/mol','+|-',5.44522),
        S298 = (-1.00631,'cal/mol/K','+|-',7.28108),
    ),
    shortDesc = """Radical correction fitted to 34 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 156,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3474,-0.213372,-1.50041,-2.14273,-2.85102,-3.45216,-4.23398],'cal/mol/K','+|-',[3,3,3.20432,3,3,3,3]),
        H298 = (83.8249,'kcal/mol','+|-',5.2),
        S298 = (-1.30632,'cal/mol/K','+|-',6.6595),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 157,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.08999,-0.121341,-1.26097,-1.93078,-2.62809,-3.03732,-4.07799],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.2544,'kcal/mol','+|-',5.2),
        S298 = (0.0184807,'cal/mol/K','+|-',4.63374),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 158,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2109,-0.202704,-1.4772,-2.16009,-2.75082,-3.03877,-4.01328],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.2596,'kcal/mol','+|-',5.2),
        S298 = (-0.836196,'cal/mol/K','+|-',3.70233),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 159,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_Int-8R!H-5C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {6,S}
5   C ux r1 {3,S} {4,S} {8,[S,D,T,B,Q]}
6   C u0 {4,S} {7,S}
7   C u0 {6,S} {8,S}
8   C ux {5,[S,D,T,B,Q]} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0242276,-0.216524,-0.737919,-1.36653,-2.35646,-3.14297,-4.41368],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.5628,'kcal/mol','+|-',2.4),
        S298 = (0.990043,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 160,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.765,-0.290507,-2.00605,-2.70129,-2.97094,-2.95531,-3.73471],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.9331,'kcal/mol','+|-',5.2),
        S298 = (-1.58727,'cal/mol/K','+|-',3.48467),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 161,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,S}
8   C ux {7,S} {9,D}
9   C ux {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.77351,-0.388711,-2.13402,-2.8368,-3.04629,-3.03391,-3.70938],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.8723,'kcal/mol','+|-',5.2),
        S298 = (-2.08195,'cal/mol/K','+|-',3.51304),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 162,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]} {8,S}
8   C ux {7,S} {9,D}
9   C u0 {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.24924,-0.351232,-1.95584,-2.70944,-3.13289,-3.06485,-4.12705],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.7561,'kcal/mol','+|-',5.2),
        S298 = (-1.07123,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 163,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing_Sp-7R!H-6C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux r1 {4,[S,D,T,B,Q]} {7,S}
7   C ux r1 {6,S} {8,S}
8   C ux r1 {7,S} {9,D}
9   C u0 r1 {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4158,-0.172453,-1.77754,-2.57408,-3.04922,-2.98521,-4.1513],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.3024,'kcal/mol','+|-',5.2),
        S298 = (-0.927364,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1C1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 164,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing_N-Sp-7R!H-6C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux r1 {4,[S,D,T,B,Q]} {7,D}
7   C ux r1 {6,D} {8,S}
8   C ux r1 {7,S} {9,D}
9   C u0 r1 {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.08268,-0.530012,-2.13414,-2.84481,-3.21657,-3.14449,-4.1028],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.2097,'kcal/mol','+|-',5.2),
        S298 = (-1.2151,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1C1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 165,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_N-7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {6,S}
5   C u0 r1 {3,S} {4,S}
6   C u0 r1 {4,S} {7,[S,D,T,B,Q]}
7   C u0 r0 {6,[S,D,T,B,Q]} {8,S}
8   C u0 {7,S} {9,D}
9   C ux {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.82204,-0.463668,-2.49039,-3.09151,-2.87308,-2.97203,-2.87403],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.1047,'kcal/mol','+|-',5.2),
        S298 = (-4.10339,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1(C2[CH]C=CC2)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 166,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux r1 {4,[S,D,T,B,Q]} {7,S}
7   C ux r1 {6,S} {8,S}
8   C ux r1 {7,S} {9,[S,T,Q,B]}
9   C u0 r1 {8,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.73947,0.00410225,-1.62213,-2.29475,-2.74488,-2.71954,-3.81072],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.1154,'kcal/mol','+|-',5.2),
        S298 = (-0.103238,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 167,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux r0 {4,[S,D,T,B,Q]} {7,S}
7   C ux {6,S} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.66452,0.179604,-1.02518,-1.78079,-2.7577,-3.13816,-4.22667],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.1423,'kcal/mol','+|-',5.2),
        S298 = (-1.94093,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)CC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 168,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_N-Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C u0 r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux {4,[S,D,T,B,Q]} {7,S}
7   C ux {6,S} {8,[B,D,T,Q]}
8   C u0 {7,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.700398,0.140831,-0.564209,-1.19191,-2.23261,-3.03264,-4.2865],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.2436,'kcal/mol','+|-',2.4),
        S298 = (2.77244,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 169,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.64381,-0.319348,-1.77614,-2.38678,-3.10772,-3.92986,-4.4136],'cal/mol/K','+|-',[3.12073,4.42096,4.57603,3.98848,3,3,3]),
        H298 = (84.5925,'kcal/mol','+|-',5.2),
        S298 = (-2.83184,'cal/mol/K','+|-',7.68905),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 170,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   u0 r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O   ux r0 {4,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.42377,3.30047,1.73726,0.799,-0.778669,-2.12191,-3.56769],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.713,'kcal/mol','+|-',5.2),
        S298 = (-5.19574,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=C[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 171,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->N",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {6,S}
5   C u0 r1 {3,S} {4,S}
6   O u0 r0 {4,S} {7,S}
7   N u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.91587,0.810499,-0.233194,-0.94166,-1.89599,-2.7718,-4.37334],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (85.0478,'kcal/mol','+|-',2.4),
        S298 = (2.23817,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1CC=C[CH]1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 172,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.965398,-1.55174,-3.17315,-3.67424,-4.11881,-4.81258,-4.6009],'cal/mol/K','+|-',[3,3.19217,3,3,3,3,3]),
        H298 = (84.5409,'kcal/mol','+|-',5.2),
        S298 = (-4.64056,'cal/mol/K','+|-',4.72625),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 173,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5    C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6    O ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]}
10   C ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.576882,-1.99874,-3.51552,-3.75303,-4.01681,-4.73213,-4.13664],'cal/mol/K','+|-',[3.31372,4.16432,3.95253,3,3,3,3]),
        H298 = (84.8637,'kcal/mol','+|-',5.2),
        S298 = (-6.0086,'cal/mol/K','+|-',4.05898),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 174,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5    C ux r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6    O ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,S} {10,[S,D,T,B,Q]}
9    C u0 {8,S}
10   C ux {8,[S,D,T,B,Q]} {11,S}
11   C u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.400854,-3.45057,-5.05188,-4.93121,-4.59481,-5.21671,-4.24658],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0393,'kcal/mol','+|-',5.2),
        S298 = (-3.70159,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 175,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 {1,S} {5,S} {6,S}
5    C u0 {3,S} {4,S}
6    O u0 {4,S} {7,S}
7    O u0 {6,S} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.06575,-1.27283,-2.74734,-3.16394,-3.72781,-4.48984,-4.08167],'cal/mol/K','+|-',[4.02812,4.69428,4.13311,3,3,3,3]),
        H298 = (85.2759,'kcal/mol','+|-',5.2),
        S298 = (-7.1621,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 176,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,S}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 r1 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
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
    index = 177,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_N-8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,S}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 r0 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.4899,0.386854,-1.28607,-2.11484,-3.3425,-4.15722,-4.11409],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2474,'kcal/mol','+|-',5.2),
        S298 = (-7.51865,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)OOC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 178,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,S}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 r0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,D}
10   C u0 r0 {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.58947,-0.779774,-2.55929,-3.47963,-4.26917,-4.84449,-5.07804],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0602,'kcal/mol','+|-',5.2),
        S298 = (-2.76641,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 179,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,S}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 r0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,S}
10   C u0 r0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.50687,-0.982717,-2.75988,-3.6325,-4.27445,-5.02202,-5.51656],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0532,'kcal/mol','+|-',5.2),
        S298 = (-2.4106,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 180,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.620122,-0.944998,-2.17444,-2.68919,-3.24484,-3.69347,-4.34774],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.6901,'kcal/mol','+|-',7.97475),
        S298 = (-1.63935,'cal/mol/K','+|-',6.36584),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 181,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.98469,-0.982676,-2.46455,-2.92363,-3.33685,-3.71137,-4.16506],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.6282,'kcal/mol','+|-',6.27468),
        S298 = (-1.99755,'cal/mol/K','+|-',7.40736),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 182,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.42445,-0.249291,-1.85938,-2.51387,-2.89305,-2.9725,-3.93314],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.764,'kcal/mol','+|-',5.2),
        S298 = (-1.41822,'cal/mol/K','+|-',3.277),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 183,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_Sp-7R!H=6C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C ux r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,S}
6   C ux {5,S} {7,D}
7   C u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.417322,-1.25001,-2.39414,-2.99481,-3.05657,-2.99449,-3.9528],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.9997,'kcal/mol','+|-',5.2),
        S298 = (0.504903,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(C2=CC=CCC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 184,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,S}
6   C ux {5,S} {7,[S,T,Q,B]}
7   C ux {6,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.79281,-0.0491463,-1.75243,-2.41768,-2.86034,-2.9681,-3.92921],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.7168,'kcal/mol','+|-',5.2),
        S298 = (-1.80285,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 185,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S}
5   C u0 {3,S} {4,S} {6,S}
6   C u0 {5,S} {7,[S,T,Q,B]}
7   C ux {6,[S,T,Q,B]} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.91046,-0.113104,-1.82881,-2.43528,-2.85622,-2.95373,-3.76568],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.6662,'kcal/mol','+|-',5.2),
        S298 = (-1.76873,'cal/mol/K','+|-',3.45679),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 186,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S}
5   C u0 {3,S} {4,S} {6,S}
6   C u0 r1 {5,S} {7,[S,T,Q,B]}
7   C ux {6,[S,T,Q,B]} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.99243,-0.210673,-2.06335,-2.65344,-2.88906,-2.89226,-3.61202],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.5908,'kcal/mol','+|-',5.2),
        S298 = (-1.71133,'cal/mol/K','+|-',4.22433),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 187,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S}
5   C u0 {3,S} {4,S} {6,S}
6   C u0 r1 {5,S} {7,[S,T,Q,B]}
7   C ux {6,[S,T,Q,B]} {8,S}
8   C ux {7,S} {9,S}
9   C u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.28075,-0.229783,-2.15626,-2.69313,-2.80898,-2.84578,-3.34238],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.86,'kcal/mol','+|-',5.2),
        S298 = (-2.10331,'cal/mol/K','+|-',5.65706),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 188,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_Ext-6C-R",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   u0 r1 {1,S} {3,D}
3    C   u0 r1 {2,D} {5,S}
4    C   u0 r1 {1,S} {5,S}
5    C   u0 r1 {3,S} {4,S} {6,S}
6    C   u0 r1 {5,S} {7,[S,T,Q,B]} {11,[S,D,T,B,Q]}
7    C   ux r1 {6,[S,T,Q,B]} {8,S}
8    C   ux r1 {7,S} {9,S}
9    C   u0 r1 {8,S} {10,D}
10   C   u0 r1 {9,D}
11   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.82204,-0.463668,-2.59039,-3.09151,-2.87308,-2.97203,-2.87403],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.8547,'kcal/mol','+|-',5.2),
        S298 = (-4.10339,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1(C2C=C[CH]C2)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 189,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {3,S} {4,S} {6,S}
6   C u0 r1 {5,S} {7,[S,T,Q,B]}
7   C ux r1 {6,[S,T,Q,B]} {8,S}
8   C ux r1 {7,S} {9,[B,D,T,Q]}
9   C u0 r1 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4158,-0.172453,-1.87754,-2.57408,-3.04922,-2.98521,-4.1513],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0524,'kcal/mol','+|-',5.2),
        S298 = (-0.927364,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(C2C=CC=CC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 190,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {3,S} {4,S} {6,S}
6   C u0 r0 {5,S} {7,[S,T,Q,B]}
7   C ux {6,[S,T,Q,B]} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.66452,0.179604,-1.12518,-1.78079,-2.7577,-3.13816,-4.22667],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.8923,'kcal/mol','+|-',5.2),
        S298 = (-1.94093,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)CC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 191,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_N-Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C ux r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,S}
6   C ux {5,S} {7,S}
7   C u0 {6,S} {8,[B,D,T,Q]}
8   C u0 {7,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.32222,0.206683,-1.44691,-2.34728,-2.87683,-3.02556,-4.58331],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.9193,'kcal/mol','+|-',5.2),
        S298 = (-1.93932,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 192,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,S}
6   O ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.664862,-1.51605,-2.90467,-3.22164,-3.65962,-4.24873,-4.33373],'cal/mol/K','+|-',[3.23969,3.22222,3.19045,3,3,3,3]),
        H298 = (85.6741,'kcal/mol','+|-',7.25715),
        S298 = (-2.41887,'cal/mol/K','+|-',9.68882),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 193,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S} {7,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C   u0 r1 {3,S} {4,[S,D,T,B,Q]} {6,S}
6   O   u0 r0 {5,S}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.3139,-3.82002,-4.23219,-4.24045,-3.96495,-3.86134,-4.85462],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.307,'kcal/mol','+|-',5.2),
        S298 = (5.27356,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=C[CH]C=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 194,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_7R!H->N",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C u0 r1 {3,S} {4,[S,D,T,B,Q]} {6,S}
6   O u0 r0 {5,S} {7,S}
7   N u0 r0 {6,S}
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
    index = 195,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,S}
6   O ux {5,S} {7,[S,D,T,B,Q]}
7   O ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.37113,-1.52341,-3.37437,-3.67461,-4.18013,-4.89179,-4.25134],'cal/mol/K','+|-',[3,3.19217,3,3,3,3,3]),
        H298 = (84.7119,'kcal/mol','+|-',5.2),
        S298 = (-5.60081,'cal/mol/K','+|-',4.72625),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 196,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux {1,S} {5,[S,D,T,B,Q]}
5    C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,S}
6    O ux {5,S} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]}
10   C ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.982618,-1.97041,-3.71675,-3.75339,-4.07813,-4.81134,-3.78708],'cal/mol/K','+|-',[3.31372,4.16432,3.95253,3,3,3,3]),
        H298 = (85.0347,'kcal/mol','+|-',5.2),
        S298 = (-6.96885,'cal/mol/K','+|-',4.05898),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 197,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,S}
5    C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O ux {5,S} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,S} {10,[S,D,T,B,Q]}
9    C u0 {8,S}
10   C ux {8,[S,D,T,B,Q]} {11,S}
11   C u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00488226,-3.42224,-5.2531,-4.93157,-4.65613,-5.29592,-3.89702],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2103,'kcal/mol','+|-',5.2),
        S298 = (-4.66184,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(OOC2C=CCCC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 198,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 {1,S} {5,[S,D,T,B,Q]}
5    C u0 {3,S} {4,[S,D,T,B,Q]} {6,S}
6    O u0 {5,S} {7,S}
7    O u0 {6,S} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.47149,-1.24449,-2.94857,-3.16431,-3.78913,-4.56905,-3.7321],'cal/mol/K','+|-',[4.02812,4.69428,4.13311,3,3,3,3]),
        H298 = (85.4469,'kcal/mol','+|-',5.2),
        S298 = (-8.12235,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 199,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,[S,D,T,B,Q]}
5    C u0 r1 {3,S} {4,[S,D,T,B,Q]} {6,S}
6    O u0 r0 {5,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 r1 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0473314,-2.90417,-4.40984,-4.21341,-4.17444,-4.90167,-3.69968],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.4754,'kcal/mol','+|-',5.2),
        S298 = (-7.76581,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(OOC2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 200,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_N-8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,[S,D,T,B,Q]}
5    C u0 r1 {3,S} {4,[S,D,T,B,Q]} {6,S}
6    O u0 r0 {5,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 r0 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.89564,0.415191,-1.48729,-2.11521,-3.40382,-4.23644,-3.76453],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.4183,'kcal/mol','+|-',5.2),
        S298 = (-8.4789,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)OOC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 201,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S}
5    C u0 r1 {3,S} {4,S} {6,S}
6    O u0 r0 {5,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 r0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,D}
10   C u0 r0 {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.99521,-0.751437,-2.76052,-3.47999,-4.33049,-4.9237,-4.72848],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2312,'kcal/mol','+|-',5.2),
        S298 = (-3.72665,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 202,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S}
5    C u0 r1 {3,S} {4,S} {6,S}
6    O u0 r0 {5,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 r0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,S}
10   C u0 r0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.91261,-0.95438,-2.96111,-3.63286,-4.33576,-5.10124,-5.167],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2242,'kcal/mol','+|-',5.2),
        S298 = (-3.37085,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 203,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   R!H ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.179123,-0.862398,-1.53845,-2.17523,-3.04312,-3.65421,-4.74823],'cal/mol/K','+|-',[3,3,3.18988,3.97156,4.52759,4.2129,3.82029]),
        H298 = (79.8492,'kcal/mol','+|-',7.46377),
        S298 = (-0.854075,'cal/mol/K','+|-',3.09295),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 204,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_6R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {4,S} {6,[B,D,T,Q]}
6   R!H ux r1 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.313517,-2.71032,-4.55487,-6.07978,-7.48692,-7.69942,-8.28272],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.8211,'kcal/mol','+|-',5.2),
        S298 = (1.50877,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(=C2C=CCCC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 205,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   R!H ux r0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.268694,-0.526413,-0.990014,-1.46531,-2.23516,-2.91872,-4.1056],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.4295,'kcal/mol','+|-',6.42475),
        S298 = (-1.28368,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 206,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C u0 r1 {3,S} {4,[S,D,T,B,Q]} {6,D}
6   C u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.198354,-0.215075,-0.64701,-1.25177,-2.26535,-3.07527,-4.37982],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (78.1695,'kcal/mol','+|-',2.4),
        S298 = (-1.97212,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 207,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,[B,D,T,Q]}
6   O ux r0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31739,-0.741955,-1.22748,-1.61315,-2.21425,-2.81034,-3.91575],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.2925,'kcal/mol','+|-',6.73393),
        S298 = (-0.807073,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 208,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing_N-6R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {4,S} {6,[B,D,T,Q]}
6   O   ux r0 {5,[B,D,T,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.234443,-1.27439,-1.86586,-1.85536,-1.68146,-1.925,-2.78106],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.3671,'kcal/mol','+|-',5.2),
        S298 = (-2.16953,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C[CH]C=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 209,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S}
5   C u0 {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09029,0.176776,-0.67286,-1.32785,-2.16221,-2.66479,-3.67007],'cal/mol/K','+|-',[4.53599,3,3,3,3,3,3.15735]),
        H298 = (83.5229,'kcal/mol','+|-',5.2),
        S298 = (-1.44713,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 210,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {3,S} {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.31082,1.06032,-0.549418,-1.32718,-1.81173,-1.70082,-2.12444],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.8896,'kcal/mol','+|-',5.2),
        S298 = (-1.89138,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=C[CH]CC1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 211,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,D}
5   C ux r1 {3,[S,D,T,B,Q]} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.15904,0.30831,-0.56612,-1.28566,-2.33012,-3.13752,-4.41001],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.2529,'kcal/mol','+|-',2.4),
        S298 = (7.83519,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC=C1 - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 212,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   O u0 {3,[S,D,T,B,Q]} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0960587,-0.603592,-1.26093,-1.79647,-2.44029,-2.93047,-4.85036],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.2808,'kcal/mol','+|-',5.2),
        S298 = (2.47365,'cal/mol/K','+|-',12.7071),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 213,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   O   u0 r1 {3,[S,D,T,B,Q]} {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.556283,-1.50424,-2.136,-2.59357,-2.89804,-2.80863,-5.81844],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0574,'kcal/mol','+|-',5.2),
        S298 = (8.6942,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=C[CH]CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 214,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.212843,-1.82759,-2.51087,-2.85667,-3.23523,-3.60057,-4.50953],'cal/mol/K','+|-',[3.2627,3.81517,3.72265,3.35144,3,3,3]),
        H298 = (73.8052,'kcal/mol','+|-',7.35525),
        S298 = (1.31676,'cal/mol/K','+|-',4.94654),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 215,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux r1 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.29274,-1.73652,-2.46316,-2.84686,-3.22924,-3.57783,-4.46148],'cal/mol/K','+|-',[3.21762,3.76102,3.72254,3.39666,3,3,3]),
        H298 = (73.8005,'kcal/mol','+|-',5.2),
        S298 = (1.01474,'cal/mol/K','+|-',4.9094),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 216,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {7,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   C   ux r1 {5,D}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.221621,-2.79741,-3.70257,-4.02952,-4.05767,-4.09074,-4.70129],'cal/mol/K','+|-',[5.04501,5.36005,4.87791,4.31001,3.18001,3,3]),
        H298 = (73.3597,'kcal/mol','+|-',5.93713),
        S298 = (1.58277,'cal/mol/K','+|-',7.46025),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 217,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Int-6R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux {1,S} {6,[S,D,T,B,Q]} {7,S}
5   C   ux r1 {3,S} {6,D}
6   C   ux r1 {4,[S,D,T,B,Q]} {5,D}
7   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.676507,-1.83839,-2.07191,-1.80211,-1.52788,-1.48393,-2.61057],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.7363,'kcal/mol','+|-',5.2),
        S298 = (-1.62469,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CC=C[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 218,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Ext-6R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {7,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux r1 {5,D} {8,[S,D,T,B,Q]}
7   C ux {4,[S,D,T,B,Q]}
8   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.532496,-2.1333,-3.2355,-3.76971,-4.03663,-4.22351,-4.90972],'cal/mol/K','+|-',[5.61639,3.88584,3.57671,3.08409,3,3,3]),
        H298 = (72.4238,'kcal/mol','+|-',5.2),
        S298 = (0.953515,'cal/mol/K','+|-',5.00542),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 219,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Ext-6R!H-R_Ext-8R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {7,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux r1 {5,D} {8,[S,D,T,B,Q]}
7   C ux {4,[S,D,T,B,Q]}
8   C ux {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9   C u0 {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.56192,-1.63614,-3.70023,-4.55605,-4.98382,-4.90408,-5.43571],'cal/mol/K','+|-',[8.5529,5.59206,4.5137,3.53524,3,3,3]),
        H298 = (72.9205,'kcal/mol','+|-',5.2),
        S298 = (-1.60269,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 220,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Ext-6R!H-R_Ext-8R!H-R_Ext-1C-R",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S} {10,[S,D,T,B,Q]}
2    C   ux r1 {1,S} {3,D}
3    C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C   ux {1,S} {7,[S,D,T,B,Q]}
5    C   ux r1 {3,[S,D,T,B,Q]} {6,D}
6    C   ux r1 {5,D} {8,[S,D,T,B,Q]}
7    C   ux {4,[S,D,T,B,Q]}
8    C   ux {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9    C   u0 {8,[S,D,T,B,Q]}
10   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.58583,0.340947,-2.1044,-3.30616,-4.38431,-4.64338,-5.34625],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.26,'kcal/mol','+|-',5.2),
        S298 = (-2.52836,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CC=C(CC=CC)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 221,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Ext-6R!H-R_Int-8R!H-1C_Ext-7R!H-R_Sp-9R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {7,S}
5   C u0 r1 {3,S} {6,D}
6   C u0 r1 {5,D} {8,S}
7   C u0 {4,S} {9,S}
8   C u0 r1 {6,S}
9   C u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.5777,-3.7656,-4.4514,-4.58546,-3.93676,-3.9511,-4.58432],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (72.1867,'kcal/mol','+|-',2.4),
        S298 = (3.45902,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CCC[C]1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 222,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Ext-6R!H-R_Int-8R!H-1C_Ext-7R!H-R_N-Sp-9R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {7,S}
5   C u0 r1 {3,S} {6,D}
6   C u0 r1 {5,D} {8,S}
7   C u0 {4,S} {9,[B,D,T,Q]}
8   C u0 r1 {6,S}
9   C u0 r0 {7,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.348996,-0.942898,-1.60649,-2.255,-3.29456,-3.89095,-4.76756],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (72.4492,'kcal/mol','+|-',2.4),
        S298 = (0.720194,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 223,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C   ux r1 {5,D}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.368806,-1.0144,-1.67627,-2.23767,-3.10475,-3.70719,-4.53775],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (71.9674,'kcal/mol','+|-',2.4),
        S298 = (0.736208,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 224,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   C   ux r1 {5,D} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.157178,-1.10254,-1.771,-2.17463,-2.66405,-3.13658,-4.13168],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.3187,'kcal/mol','+|-',5.2),
        S298 = (0.281922,'cal/mol/K','+|-',3.8991),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 225,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux r1 {5,D} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.593909,-1.36887,-1.95928,-2.35906,-2.89857,-3.4028,-4.44728],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.555,'kcal/mol','+|-',5.2),
        S298 = (0.886099,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 226,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R_7R!H->C_Ext-7C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux r1 {5,D} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.622971,-1.63279,-2.32273,-2.70767,-3.09275,-3.49419,-4.46083],'cal/mol/K','+|-',[3,3,3.43286,3.15803,3,3,3]),
        H298 = (74.6752,'kcal/mol','+|-',5.2),
        S298 = (0.707315,'cal/mol/K','+|-',3.52914),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 227,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C ux r1 {5,D} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   C u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.49802,-2.78887,-4.00323,-4.25364,-3.74863,-3.70784,-4.45043],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.2028,'kcal/mol','+|-',5.2),
        S298 = (-1.02032,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CCCC1=CC=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 228,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C ux r1 {5,D} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,[B,D,T,Q]}
9   C u0 r0 {8,[B,D,T,Q]}
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
    index = 229,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,S}
4   C                      u0 r1 {1,S}
5   C                      u0 r1 {3,S} {6,D}
6   C                      u0 r1 {5,D} {7,S}
7   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.24484,0.362261,-0.735479,-1.16025,-1.37416,-1.67234,-2.39584],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (71.8636,'kcal/mol','+|-',5.2),
        S298 = (-3.04105,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=CC=C[CH]C1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 230,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,D} {7,[S,D,T,B,Q]}
6   C   ux r1 {5,D}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.899076,-1.27203,-1.63832,-1.99818,-2.68342,-3.30234,-4.46074],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (74.8945,'kcal/mol','+|-',2.4),
        S298 = (1.41328,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC[CH]C=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 231,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0651961,-2.14449,-2.6769,-2.89082,-3.25609,-3.67971,-4.67674],'cal/mol/K','+|-',[3.84391,4.50371,4.26102,3.68695,3,3,3]),
        H298 = (73.8259,'kcal/mol','+|-',18.1056),
        S298 = (2.3678,'cal/mol/K','+|-',5.14626),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 232,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing_Ext-4C-R_Sp-7R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C u0 {1,S} {7,S}
5   C u0 {3,[S,D,T,B,Q]} {6,D}
6   C u0 r0 {5,D}
7   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.223738,-1.08146,-1.7554,-2.05231,-2.62799,-3.26092,-4.63628],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.589,'kcal/mol','+|-',8.96828),
        S298 = (2.56641,'cal/mol/K','+|-',7.63678),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 233,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {7,S} {8,[S,D,T,B,Q]}
5   C   u0 r1 {3,[S,D,T,B,Q]} {6,D}
6   C   u0 r0 {5,D}
7   C   ux r1 {4,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.855633,-2.10538,-3.02267,-3.16056,-3.37575,-3.78161,-5.05036],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.3611,'kcal/mol','+|-',5.2),
        S298 = (6.30489,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 234,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing_Ext-4C-R_N-Sp-7R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {7,[B,D,T,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux r0 {5,D}
7   C ux {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.378208,-3.2961,-3.67519,-3.7992,-3.93653,-4.1334,-4.72056],'cal/mol/K','+|-',[5.75999,5.50899,5.23801,4.42215,3,3,3]),
        H298 = (64.7846,'kcal/mol','+|-',10.911),
        S298 = (2.15264,'cal/mol/K','+|-',4.75938),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 235,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing_Ext-4C-R_N-Sp-7R!H-4C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {7,[B,D,T,Q]}
5   C   u0 r1 {3,[S,D,T,B,Q]} {6,D} {8,[S,D,T,B,Q]}
6   C   u0 r0 {5,D}
7   C   ux r1 {4,[B,D,T,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.69395,-6.4332,-6.64922,-6.32569,-5.48423,-4.99455,-4.79723],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (71.0825,'kcal/mol','+|-',5.2),
        S298 = (4.9004,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 236,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing_Ext-4C-R_N-Sp-7R!H-4C_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {7,[B,D,T,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C   ux r0 {5,D} {8,[S,D,T,B,Q]}
7   C   ux r1 {4,[B,D,T,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.50045,-2.18164,-2.66309,-2.85456,-3.25575,-3.66578,-4.56412],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (61.7599,'kcal/mol','+|-',5.2),
        S298 = (0.795612,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C1C=C[CH]C=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 237,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.265055,-1.39056,-2.47747,-2.95196,-3.50604,-3.94498,-4.63758],'cal/mol/K','+|-',[3.3069,3.37204,3.40973,3,3,3,3]),
        H298 = (82.3112,'kcal/mol','+|-',15.0773),
        S298 = (-2.38255,'cal/mol/K','+|-',8.66515),
    ),
    shortDesc = """Radical correction fitted to 49 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 238,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0856895,-3.12669,-4.08122,-4.01092,-3.9575,-4.21278,-4.21152],'cal/mol/K','+|-',[4.96523,3.44119,3.39595,3.37871,3.80092,3.88386,3]),
        H298 = (80.8019,'kcal/mol','+|-',7.22853),
        S298 = (-6.13166,'cal/mol/K','+|-',9.28569),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 239,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O ux r1 {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.914966,-3.56142,-4.10919,-3.85995,-4.05261,-4.58965,-4.50763],'cal/mol/K','+|-',[7.16708,5.09149,4.85106,4.65339,5.05531,4.81808,3.10028]),
        H298 = (79.343,'kcal/mol','+|-',10.3138),
        S298 = (-3.5929,'cal/mol/K','+|-',12.3923),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 240,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {7,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O ux r1 {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   O ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.801801,-4.39314,-4.82015,-4.35941,-4.13146,-4.51569,-4.15702],'cal/mol/K','+|-',[8.25517,4.01466,4.23059,4.71377,5.82315,5.55032,3.08827]),
        H298 = (80.271,'kcal/mol','+|-',10.9026),
        S298 = (-4.21729,'cal/mol/K','+|-',13.9414),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 241,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {7,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O   ux r1 {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   O   ux r1 {4,S} {6,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.98713,-2.56399,-2.67443,-2.09973,-1.3552,-1.90933,-2.87187],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.5699,'kcal/mol','+|-',5.2),
        S298 = (-10.58,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=C2CCC1OOC2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 242,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {7,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O   ux r1 {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   O   ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.53892,-2.76994,-3.34642,-2.55965,-1.88547,-2.32994,-2.76933],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.6488,'kcal/mol','+|-',5.2),
        S298 = (-9.9188,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=CC2CC[C]1COO2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 243,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O   ux r1 {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   O   ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.66539,-5.84718,-6.4095,-6.18936,-6.45812,-6.75105,-5.44992],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.8788,'kcal/mol','+|-',5.2),
        S298 = (1.7541,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1[CH]C=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 244,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O ux r0 {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.800443,-2.81617,-4.06125,-4.11875,-3.88956,-3.94359,-4.00002],'cal/mol/K','+|-',[3,3,3,3,3.06546,3.37151,3]),
        H298 = (81.8439,'kcal/mol','+|-',5.2),
        S298 = (-7.94506,'cal/mol/K','+|-',4.34374),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 245,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {7,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {8,S}
6   O ux r0 {5,[S,T,Q,B]}
7   C ux {4,S}
8   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.700811,-2.86716,-4.15805,-4.429,-4.79807,-5.06217,-5.05505],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0165,'kcal/mol','+|-',5.2),
        S298 = (-8.0914,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 246,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {7,S}
5    C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {8,S}
6    O ux r0 {5,[S,T,Q,B]} {9,[S,D,T,B,Q]}
7    C ux r1 {4,S}
8    C u0 r0 {5,S}
9    O ux {6,[S,D,T,B,Q]} {10,S}
10   C u0 r0 {9,S} {11,[S,D,T,B,Q]}
11   C ux {10,[S,D,T,B,Q]} {12,D}
12   C u0 r0 {11,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72823,-3.67097,-4.61195,-4.45537,-4.14084,-4.29889,-4.04322],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.9904,'kcal/mol','+|-',5.2),
        S298 = (-8.93423,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1(C)C=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 247,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {7,S}
5    C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {8,S}
6    O ux r0 {5,[S,T,Q,B]} {9,[S,D,T,B,Q]}
7    C ux r1 {4,S}
8    C u0 r0 {5,S}
9    O ux {6,[S,D,T,B,Q]} {10,S}
10   C u0 r0 {9,S} {11,[S,D,T,B,Q]}
11   C ux {10,[S,D,T,B,Q]} {12,S}
12   C u0 r0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.326603,-2.06335,-3.70416,-4.40262,-5.4553,-5.82545,-6.06689],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0425,'kcal/mol','+|-',5.2),
        S298 = (-7.24857,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1(C)C=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 248,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O ux r0 {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.560156,-2.60244,-3.9274,-3.95751,-3.64299,-3.65341,-3.76567],'cal/mol/K','+|-',[3,3,3.17396,3.511,3.76787,3.9812,3]),
        H298 = (80.987,'kcal/mol','+|-',5.2),
        S298 = (-7.19419,'cal/mol/K','+|-',4.79373),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 249,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S}
5   C u0 r1 {3,S} {6,S}
6   O u0 r0 {5,S}
7   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0313433,-2.49885,-4.35468,-4.54692,-4.30128,-4.39572,-4.31876],'cal/mol/K','+|-',[3.1542,3,3,3,4.23934,4.96412,4.56542]),
        H298 = (80.0127,'kcal/mol','+|-',5.2),
        S298 = (-7.61462,'cal/mol/K','+|-',8.00016),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 250,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1C-R_Ext-7R!H-R_Ext-8R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r0 {1,S}
5   C   u0 r1 {3,S} {6,S}
6   O   u0 r0 {5,S}
7   C   ux r1 {1,[S,D,T,B,Q]} {8,S}
8   C   u0 r1 {7,S} {9,[S,D,T,B,Q]}
9   R!H ux {8,[S,D,T,B,Q]}
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
    index = 251,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-6O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O   ux r0 {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5068,-3.87368,-5.31831,-5.1841,-4.4715,-4.23825,-3.57459],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.3461,'kcal/mol','+|-',5.2),
        S298 = (-6.26032,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1CC[CH]C=C1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 252,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_N-5R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S}
5   C ux r0 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O ux r0 {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.96086,-3.56909,-4.40303,-4.14323,-3.05883,-2.86717,-2.82734],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.9269,'kcal/mol','+|-',5.2),
        S298 = (-10.6558,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOCC1=C[CH]CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 253,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.354606,-0.947288,-2.068,-2.68159,-3.39078,-3.87661,-4.74636],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.5833,'kcal/mol','+|-',16.1355),
        S298 = (-1.42533,'cal/mol/K','+|-',7.4564),
    ),
    shortDesc = """Radical correction fitted to 37 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 254,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,[S,D,T,B,Q]} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.610131,-0.53098,-1.52471,-2.24188,-3.00449,-3.50626,-4.59881],'cal/mol/K','+|-',[3.90169,3.19271,3,3,3,3,3]),
        H298 = (85.4219,'kcal/mol','+|-',30.1321),
        S298 = (-2.17524,'cal/mol/K','+|-',10.58),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 255,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20031,-0.342648,-1.19095,-1.97392,-2.95273,-3.49236,-4.67226],'cal/mol/K','+|-',[3.96244,4.07006,3.00925,3,3,3.22746,3]),
        H298 = (96.1041,'kcal/mol','+|-',26.0158),
        S298 = (0.01117,'cal/mol/K','+|-',10.58),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 256,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {6,S}
5   C u0 {3,S} {6,S}
6   C u0 {4,S} {5,S} {7,S}
7   C u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.150492,-0.484414,-1.01496,-1.60087,-2.55034,-3.29809,-4.49063],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.0979,'kcal/mol','+|-',5.2),
        S298 = (3.17947,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 257,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_7R!H-inRing_Int-7R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {6,S} {7,[S,D,T,B,Q]}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,S} {5,S} {7,S}
7   C u0 r1 {4,[S,D,T,B,Q]} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.276328,-0.515126,-1.00265,-1.59227,-2.55906,-3.31924,-4.52314],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.9831,'kcal/mol','+|-',5.2),
        S298 = (3.20994,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 258,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux r0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.333949,-0.288642,-1.25799,-2.11603,-3.10602,-3.56637,-4.74145],'cal/mol/K','+|-',[4.93759,5.1071,3.76823,3,3,4.04062,3.64114]),
        H298 = (100.265,'kcal/mol','+|-',21.702),
        S298 = (-1.1958,'cal/mol/K','+|-',12.1163),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 259,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux {1,S} {6,S}
5   C ux {3,S} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]} {7,S}
7   C ux r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19123,0.748535,-0.354183,-1.29158,-2.49274,-2.88183,-4.41969],'cal/mol/K','+|-',[6.08767,5.66371,3,3,3,3,3]),
        H298 = (104.521,'kcal/mol','+|-',5.2),
        S298 = (-0.200247,'cal/mol/K','+|-',6.7316),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 260,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_7R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux r1 {1,S} {6,S}
5   C   ux r1 {3,S} {6,[S,T,Q,B]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]} {7,S}
7   C   ux r0 {6,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.133269,-0.483726,-0.999066,-1.6067,-2.59749,-3.33569,-4.43766],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.012,'kcal/mol','+|-',2.4),
        S298 = (1.26436,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1C[C]2C=CC1CC2 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 261,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_N-7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   O ux r0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.05914,-1.97406,-2.72668,-3.45576,-4.10261,-4.67875,-5.26431],'cal/mol/K','+|-',[3.76302,3.96903,3.5639,3,4.1054,6.21497,6.76027]),
        H298 = (88.1446,'kcal/mol','+|-',21.8108),
        S298 = (-2.81358,'cal/mol/K','+|-',21.1829),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 262,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_N-7R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {6,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   O   ux r0 {6,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.38957,-3.37732,-3.98671,-3.81281,-2.65113,-2.48143,-2.8742],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.4333,'kcal/mol','+|-',5.2),
        S298 = (-10.3029,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COC1[CH]C=C(C)CC1OO - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 263,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,D} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.08552,-0.749444,-1.91188,-2.55271,-3.06453,-3.52237,-4.51362],'cal/mol/K','+|-',[4.1177,3,3,3,3,3,3]),
        H298 = (73.5111,'kcal/mol','+|-',5.2),
        S298 = (-4.71147,'cal/mol/K','+|-',9.09377),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 264,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,D} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.01561,-0.6361,-2.22482,-3.00163,-3.37278,-3.70162,-4.53989],'cal/mol/K','+|-',[3.78324,3,3,3,3,3,3]),
        H298 = (72.847,'kcal/mol','+|-',5.2),
        S298 = (-7.61331,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 265,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux {1,S} {6,D}
5   C ux {3,S} {6,[S,T,Q,B]}
6   C ux {4,D} {5,[S,T,Q,B]} {7,S}
7   C ux {6,S} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.92587,-1.01555,-2.76127,-3.62209,-4.01898,-4.32471,-5.16791],'cal/mol/K','+|-',[4.6126,3,3,3,3,3,3]),
        H298 = (73.6081,'kcal/mol','+|-',5.2),
        S298 = (-7.34323,'cal/mol/K','+|-',3.09767),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 266,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,S} {9,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {6,D}
5   C   ux r1 {3,S} {6,[S,T,Q,B]}
6   C   ux r1 {4,D} {5,[S,T,Q,B]} {7,S}
7   C   ux r0 {6,S} {8,[S,D,T,B,Q]}
8   C   ux {7,[S,D,T,B,Q]}
9   R!H ux {3,[S,D,T,B,Q]}
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
    index = 267,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {6,D}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,D} {5,S} {7,S}
7   C u0 r0 {6,S} {8,S}
8   C u0 r0 {7,S} {9,S}
9   C u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.45802,-2.64887,-3.88323,-4.23364,-3.80863,-3.86784,-4.71043],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.9028,'kcal/mol','+|-',5.2),
        S298 = (-6.40282,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CCCC1=C[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 268,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {6,D}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,D} {5,S} {7,S}
7   C u0 r0 {6,S} {8,S}
8   C u0 r0 {7,S} {9,[B,D,T,Q]}
9   C u0 r0 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.0898,-0.408733,-2.17616,-3.17647,-3.81401,-4.26291,-5.32703],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.9016,'kcal/mol','+|-',5.2),
        S298 = (-6.496,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=C[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 269,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_N-7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {6,D}
5   C   u0 r1 {3,[S,D,T,B,Q]} {6,S}
6   C   u0 r1 {4,D} {5,S} {7,[S,D,T,B,Q]}
7   O   u0 {6,[S,D,T,B,Q]} {8,S}
8   R!H u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.28484,0.502261,-0.615479,-1.14025,-1.43416,-1.83234,-2.65584],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (70.5636,'kcal/mol','+|-',5.2),
        S298 = (-8.42355,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=C[CH]C=CC1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 270,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.288678,-1.15037,-2.36244,-2.94557,-3.63406,-4.09753,-4.83045],'cal/mol/K','+|-',[3,3,3.00613,3,3,3,3]),
        H298 = (82.2618,'kcal/mol','+|-',5.2),
        S298 = (-1.21414,'cal/mol/K','+|-',6.13138),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 271,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0795465,-2.05814,-3.66382,-4.28413,-4.57194,-4.78905,-5.31173],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.3529,'kcal/mol','+|-',5.2),
        S298 = (-3.19211,'cal/mol/K','+|-',4.92299),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 272,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]} {7,S}
4   C   u0 r1 {1,S} {6,S} {8,[S,D,T,B,Q]}
5   C   u0 r1 {3,[S,D,T,B,Q]} {6,S}
6   C   u0 r1 {4,S} {5,S}
7   C   u0 r0 {3,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.159216,-2.73705,-4.64021,-5.4003,-5.6488,-5.99159,-6.10244],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.3101,'kcal/mol','+|-',5.2),
        S298 = (-4.64589,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=C[CH]C(OOCC(C)C)CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 273,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   C ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.588561,-1.82626,-3.43155,-4.02652,-4.18343,-4.27049,-4.86138],'cal/mol/K','+|-',[3.78695,3.21598,3,3,3,3,3]),
        H298 = (82.3819,'kcal/mol','+|-',5.2),
        S298 = (-4.47467,'cal/mol/K','+|-',5.22379),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 274,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   C u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.750328,-2.96327,-4.38719,-4.61446,-4.03808,-3.84087,-4.34877],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.7976,'kcal/mol','+|-',5.2),
        S298 = (-6.32156,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CCC1=C[CH]CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 275,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,[B,D,T,Q]}
9   C u0 r0 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.92745,-0.689236,-2.47592,-3.43859,-4.32877,-4.70012,-5.374],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.9662,'kcal/mol','+|-',5.2),
        S298 = (-2.62778,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=C[CH]CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 276,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {6,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {8,[S,D,T,B,Q]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]}
7   C   ux {3,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.068348,-2.05131,-3.70601,-4.11978,-4.31725,-4.62218,-5.27765],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.0451,'kcal/mol','+|-',5.2),
        S298 = (-2.58525,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1CC[CH]C=C1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 277,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.327328,-1.70655,-2.75436,-3.19859,-3.63596,-3.95329,-4.43701],'cal/mol/K','+|-',[3,3,3.52988,3,3,3,3]),
        H298 = (81.3203,'kcal/mol','+|-',5.2),
        S298 = (-2.20021,'cal/mol/K','+|-',7.37361),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 278,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   C   ux {1,[S,D,T,B,Q]} {8,S}
8   R!H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.556518,-1.80342,-2.6782,-3.05391,-3.50601,-3.81488,-4.22893],'cal/mol/K','+|-',[3,3.47324,4.48385,3.51889,3,3,3]),
        H298 = (81.3795,'kcal/mol','+|-',5.2),
        S298 = (-3.51887,'cal/mol/K','+|-',9.26215),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 279,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-7R!H-R_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   C ux {1,[S,D,T,B,Q]} {8,S}
8   C u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.137481,-1.18804,-2.00264,-2.57733,-3.49932,-4.00144,-4.58419],'cal/mol/K','+|-',[3,3,4.40121,3.75281,3,3,3]),
        H298 = (81.4752,'kcal/mol','+|-',5.2),
        S298 = (-1.82178,'cal/mol/K','+|-',6.74064),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 280,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_Sp-9R!H-8C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux {1,[S,D,T,B,Q]} {8,S}
8   C u0 r0 {7,S} {9,S}
9   C u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.230328,-2.52327,-4.15719,-4.41446,-3.97808,-3.78087,-4.41877],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.4376,'kcal/mol','+|-',5.2),
        S298 = (-5.12156,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC[C]1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 281,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_N-Sp-9R!H-8C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux {1,[S,D,T,B,Q]} {8,S}
8   C u0 r0 {7,S} {9,[B,D,T,Q]}
9   C u0 r0 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0962158,-0.59461,-1.04506,-1.76083,-3.28653,-4.09947,-4.6577],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (81.6962,'kcal/mol','+|-',2.4),
        S298 = (-0.355208,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 282,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-7R!H-R_N-8R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C                      ux r1 {1,S} {3,D}
3   C                      ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C                      ux r1 {1,S} {6,S}
5   C                      ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux r1 {4,S} {5,[S,T,Q,B]}
7   C                      ux {1,[S,D,T,B,Q]} {8,S}
8   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.91839,-3.80337,-4.87379,-4.60279,-3.52778,-3.20857,-3.07435],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.8348,'kcal/mol','+|-',5.2),
        S298 = (-9.03442,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC[C]1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 283,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,S} {6,S} {8,S}
5   C   u0 {3,S} {6,S}
6   C   u0 {4,S} {5,S}
7   C   u0 {1,S}
8   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0220959,-2.44666,-4.20155,-4.59176,-4.45371,-4.47061,-4.7809],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.7051,'kcal/mol','+|-',5.2),
        S298 = (-3.12266,'cal/mol/K','+|-',3.83934),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 284,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-4C-R_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {6,S} {8,S}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,S} {5,S}
7   C u0 r0 {1,S}
8   C u0 r0 {4,S}
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
    index = 285,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-4C-R_N-8R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S} {7,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,S}
4   C                      u0 r1 {1,S} {6,S} {8,S}
5   C                      u0 r1 {3,S} {6,S}
6   C                      u0 r1 {4,S} {5,S}
7   C                      u0 r0 {1,S}
8   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01254,-3.37202,-4.95709,-5.12373,-4.50018,-4.23904,-4.10415],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.6452,'kcal/mol','+|-',5.2),
        S298 = (-4.48007,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1CCC=C[C]1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 286,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.11921,-0.269298,-1.64267,-2.34735,-3.36062,-3.87298,-4.9222],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.9262,'kcal/mol','+|-',5.2),
        S298 = (0.114335,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 287,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   R!H ux r1 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.16907,0.511588,-1.41518,-2.25949,-3.28055,-3.69978,-5.03783],'cal/mol/K','+|-',[3,3,3,3.22872,3,3,3]),
        H298 = (81.1168,'kcal/mol','+|-',5.2),
        S298 = (0.944066,'cal/mol/K','+|-',3.34418),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 288,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {6,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]}
7   R!H ux r1 {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.36658,1.08981,-0.392996,-1.11797,-2.2981,-3.06693,-4.51254],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.4086,'kcal/mol','+|-',5.2),
        S298 = (2.12641,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1CC12C=C[CH]CC2 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 289,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   R!H ux r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.719259,-0.566779,-1.72934,-2.38082,-3.39113,-3.93896,-4.87815],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.3965,'kcal/mol','+|-',5.2),
        S298 = (-0.201754,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 290,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {6,S} {8,S}
5   C u0 {3,S} {6,S} {7,S}
6   C u0 {4,S} {5,S}
7   C u0 r0 {5,S}
8   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.24933,-0.591835,-2.18765,-2.86611,-3.92981,-4.2663,-5.11159],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.0078,'kcal/mol','+|-',5.2),
        S298 = (-1.51972,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 291,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r1 {1,S} {6,S} {8,S}
5   C   u0 r1 {3,S} {6,S} {7,S}
6   C   u0 r1 {4,S} {5,S}
7   C   u0 r0 {5,S} {9,[S,D,T,B,Q]}
8   C   u0 r0 {4,S}
9   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.24933,-0.591835,-2.18765,-2.86611,-3.92981,-4.2663,-5.11159],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.0078,'kcal/mol','+|-',5.2),
        S298 = (-1.51972,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1C=C[CH]C(C)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 292,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {6,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]}
7   R!H ux r0 {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.27252,-0.837608,-2.54074,-3.46,-4.59476,-5.08559,-5.41317],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.3593,'kcal/mol','+|-',5.2),
        S298 = (-0.712704,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1(C)C=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 293,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,S} {6,S} {7,S}
5   C   u0 {3,S} {6,S}
6   C   u0 {4,S} {5,S}
7   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.40716,-1.02476,-2.21826,-2.8159,-3.64531,-4.28289,-4.98239],'cal/mol/K','+|-',[3.0866,3.33694,3.33897,3.11599,3,3,3]),
        H298 = (82.1857,'kcal/mol','+|-',7.22203),
        S298 = (-0.810704,'cal/mol/K','+|-',7.43767),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 294,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,S} {6,S} {7,S}
5   C   u0 {3,S} {6,S}
6   C   u0 {4,S} {5,S}
7   R!H u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.69031,0.103933,-1.45205,-2.24782,-3.45224,-4.19769,-5.28041],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.6471,'kcal/mol','+|-',9.70901),
        S298 = (1.44942,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 295,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,S} {6,S} {7,S} {8,S}
5   C   u0 {3,S} {6,S}
6   C   u0 {4,S} {5,S}
7   R!H u0 r1 {4,S}
8   C   u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.54968,0.189218,-1.00939,-1.67122,-3.04687,-4.13022,-5.13906],'cal/mol/K','+|-',[3,3,3,3,3,3.00609,3]),
        H298 = (76.4331,'kcal/mol','+|-',8.41984),
        S298 = (2.29327,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 296,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {6,S} {7,S} {8,S}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,S} {5,S}
7   O u0 r1 {4,S}
8   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.732308,-0.711378,-1.6253,-2.22399,-3.79491,-5.19303,-5.7651],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.4563,'kcal/mol','+|-',5.2),
        S298 = (2.45726,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1CC2([CH]C=CCC2)OO1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 297,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_N-7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {6,S} {7,S} {8,S}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,S} {5,S}
7   C u0 r1 {4,S}
8   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.36705,1.08981,-0.393474,-1.11845,-2.29882,-3.0674,-4.51302],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.41,'kcal/mol','+|-',5.2),
        S298 = (2.12928,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1CC12[CH]C=CCC2 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 298,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,S} {6,S} {7,S}
5   C   u0 {3,S} {6,S}
6   C   u0 {4,S} {5,S}
7   R!H u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.326069,-1.66973,-2.65609,-3.14052,-3.75564,-4.33158,-4.8121],'cal/mol/K','+|-',[3,3.52863,3.95909,3.69,3.1017,3,3]),
        H298 = (83.5654,'kcal/mol','+|-',5.2),
        S298 = (-2.1022,'cal/mol/K','+|-',8.50342),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 299,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {6,S} {7,S}
5   C u0 {3,S} {6,S}
6   C u0 {4,S} {5,S}
7   O u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42456,-3.44414,-4.61696,-4.88554,-4.9387,-5.37833,-4.94685],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.0983,'kcal/mol','+|-',5.2),
        S298 = (-6.52375,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 300,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Sp-11R!H=10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {6,S} {7,S}
5    C u0 r1 {3,S} {6,S}
6    C u0 r1 {4,S} {5,S}
7    O u0 r0 {4,S} {8,[S,D,T,B,Q]}
8    O ux {7,[S,D,T,B,Q]} {9,S}
9    C u0 r0 {8,S} {10,[S,D,T,B,Q]}
10   C ux {9,[S,D,T,B,Q]} {11,D}
11   C u0 r0 {10,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.45197,-4.24795,-5.07086,-4.91191,-4.28147,-4.61504,-3.93502],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.0722,'kcal/mol','+|-',5.2),
        S298 = (-7.36658,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1(C)[CH]C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 301,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_N-Sp-11R!H=10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {6,S} {7,S}
5    C u0 r1 {3,S} {6,S}
6    C u0 r1 {4,S} {5,S}
7    O u0 r0 {4,S} {8,[S,D,T,B,Q]}
8    O ux {7,[S,D,T,B,Q]} {9,S}
9    C u0 r0 {8,S} {10,[S,D,T,B,Q]}
10   C ux {9,[S,D,T,B,Q]} {11,S}
11   C u0 r0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.397145,-2.64033,-4.16307,-4.85916,-5.59593,-6.14161,-5.95869],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.1244,'kcal/mol','+|-',5.2),
        S298 = (-5.68093,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1(C)[CH]C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 302,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_N-7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {6,S} {7,S}
5   C u0 {3,S} {6,S}
6   C u0 {4,S} {5,S}
7   C u0 r0 {4,S}
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
    index = 303,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_N-7R!H->O_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r1 {1,S} {6,S} {7,S} {8,[S,D,T,B,Q]}
5   C   u0 r1 {3,S} {6,S}
6   C   u0 r1 {4,S} {5,S}
7   C   u0 r0 {4,S}
8   R!H ux {4,[S,D,T,B,Q]}
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
    index = 304,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C u0 r1 {1,S} {6,[B,D,T,Q]}
5   C u0 r1 {3,[S,D,T,B,Q]} {6,S}
6   C u0 r1 {4,[B,D,T,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.262869,-0.624605,-1.23829,-1.65356,-2.32951,-3.03035,-4.4637],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (74.442,'kcal/mol','+|-',2.4),
        S298 = (0.140843,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 305,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_N-Sp-2R!H-1C",
    group = 
"""
1 * C u1 r1 {2,D} {4,S}
2   C ux r1 {1,D} {3,D}
3   C ux r1 {2,D}
4   C ux r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.503132,-2.03451,-2.79058,-3.01131,-3.26561,-4.11574,-4.91171],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.3249,'kcal/mol','+|-',5.2),
        S298 = (5.65154,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C=[C]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 306,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.667794,-0.26698,-1.11124,-1.65339,-2.42645,-2.98496,-4.04366],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.3011,'kcal/mol','+|-',9.20757),
        S298 = (3.276,'cal/mol/K','+|-',10.5758),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 307,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.80437,-0.0849911,-0.932002,-1.51833,-2.37086,-2.94249,-3.8808],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.4083,'kcal/mol','+|-',11.7932),
        S298 = (4.03383,'cal/mol/K','+|-',16.2876),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 308,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   C u0 {1,S} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
6   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.05469,-0.154654,-0.917505,-1.21127,-1.59067,-1.69115,-2.42708],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.0924,'kcal/mol','+|-',13.5481),
        S298 = (13.5394,'cal/mol/K','+|-',33.6531),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 309,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   C u0 r1 {1,S} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
6   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17653,0.72844,0.0472595,-0.493509,-0.957762,-1.12817,-1.77485],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.3024,'kcal/mol','+|-',5.2),
        S298 = (25.4375,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C1[CH]C1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 310,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   C u0 r1 {1,S} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
6   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.932851,-1.03775,-1.88227,-1.92903,-2.22357,-2.25412,-3.07931],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.8824,'kcal/mol','+|-',5.2),
        S298 = (1.64121,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O)=C[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 311,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_Sp-5R!H-3R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {5,S}
4   C   ux r1 {1,S}
5   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.794855,-0.121614,-1.12852,-1.78904,-2.7189,-3.30413,-4.03738],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (91.9493,'kcal/mol','+|-',2.4),
        S298 = (1.85481,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 312,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_N-Sp-5R!H-3R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {5,D}
4   C   ux {1,S}
5   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.717237,-0.0446769,-0.856881,-1.51924,-2.5122,-3.24958,-4.34537],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.706,'kcal/mol','+|-',8.80644),
        S298 = (1.46869,'cal/mol/K','+|-',3.74653),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 313,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r0 {2,D} {5,D}
4   C   u0 r1 {1,S}
5   R!H u0 r0 {3,D} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 314,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_N-Sp-5R!H-3R!H_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {5,D}
4   C ux r1 {1,S}
5   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.970463,0.247511,-0.603339,-1.28955,-2.36813,-3.13856,-4.24483],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.245,'kcal/mol','+|-',2.4),
        S298 = (2.85796,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 315,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_N-Sp-5R!H-3R!H_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {5,D}
4   C ux r1 {1,S}
5   O ux {3,D}
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
    index = 316,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.599351,-0.395491,-1.23941,-1.75883,-2.46769,-2.96646,-3.98208],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.2152,'kcal/mol','+|-',5.2),
        S298 = (3.26064,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 317,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.407614,-0.50611,-1.25951,-1.70004,-2.37133,-2.88551,-3.9317],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.6306,'kcal/mol','+|-',5.2),
        S298 = (3.43418,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 318,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_3R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0235257,-0.98104,-1.73296,-2.07282,-2.53512,-2.85215,-3.66526],'cal/mol/K','+|-',[3.24531,3,3,3,3,3,3]),
        H298 = (95.8775,'kcal/mol','+|-',5.2),
        S298 = (4.03396,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 319,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_3R!H->C_Ext-4C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S}
5   R!H u0 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.07478,-0.498275,-1.76779,-2.24604,-2.58293,-2.6258,-3.52472],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.2506,'kcal/mol','+|-',5.2),
        S298 = (3.92405,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 320,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_3R!H->C_Ext-4C-R_2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.62813,-0.346037,-1.76043,-2.26587,-3.01141,-3.49475,-4.314],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.7713,'kcal/mol','+|-',5.2),
        S298 = (4.55835,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 321,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_3R!H->C_Ext-4C-R_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.15686,-1.47783,-1.70527,-1.91003,-2.30219,-2.66716,-3.43939],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.1815,'kcal/mol','+|-',2.4),
        S298 = (3.84975,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 322,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   O u0 r0 {2,D}
4   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2225,-0.0359786,-1.17408,-1.94986,-2.78085,-3.22953,-4.14583],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.544,'kcal/mol','+|-',5.2),
        S298 = (2.69664,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 323,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_N-3R!H->C_Ext-4C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,D}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.50929,-0.265378,-1.76262,-2.76498,-3.77665,-4.15595,-4.62027],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.8284,'kcal/mol','+|-',5.2),
        S298 = (3.24228,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)C[C]1C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 324,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   R!H u0 r0 {2,D}
4   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.437073,-0.476842,-1.31374,-1.78283,-2.48534,-3.16074,-4.69329],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.533,'kcal/mol','+|-',5.2),
        S298 = (1.0427,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 325,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_N-4R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,D}
3   R!H u0 r0 {2,D}
4   O   u0 r1 {1,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12272,-0.146756,-1.5682,-2.10404,-2.56133,-3.1571,-5.31485],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.721,'kcal/mol','+|-',5.2),
        S298 = (0.564975,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 326,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
4   C   ux {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.256698,-1.04256,-1.68557,-2.24737,-3.16095,-3.76815,-4.72359],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.043,'kcal/mol','+|-',9.62802),
        S298 = (1.27398,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 327,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
4   C   ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.232195,-1.02653,-1.67624,-2.24083,-3.1673,-3.78128,-4.73048],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.285,'kcal/mol','+|-',9.10466),
        S298 = (1.18484,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 328,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
4   C ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.436691,-0.89208,-1.42885,-1.9727,-2.84346,-3.49494,-4.4843],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.194,'kcal/mol','+|-',4.22765),
        S298 = (0.796905,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 329,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C u0 r1 {2,D}
4   C u0 {1,D} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.358894,-0.794939,-1.32686,-1.88412,-2.77259,-3.43763,-4.44879],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.169,'kcal/mol','+|-',5.68118),
        S298 = (0.597498,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 330,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   u0 r1 {2,D} {7,S}
4   C   u0 {1,D} {5,S}
5   C   u0 {4,S} {6,D}
6   O   ux {5,D}
7   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.347747,-0.726002,-1.21883,-1.79136,-2.74558,-3.43716,-4.43897],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (110.795,'kcal/mol','+|-',2.58372),
        S298 = (1.37865,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 331,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C u0 r1 {2,D} {7,S}
4   C u0 r1 {1,D} {5,S}
5   C u0 r1 {4,S} {6,D}
6   O ux r0 {5,D}
7   C u0 r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.330326,-0.690371,-1.19076,-1.7876,-2.7503,-3.44249,-4.43616],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.881,'kcal/mol','+|-',2.4),
        S298 = (1.48803,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=[C]C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 332,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C                      ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C                      u0 r1 {2,D} {7,S}
4   C                      u0 r1 {1,D} {5,S}
5   C                      u0 r1 {4,S} {6,D}
6   O                      ux r0 {5,D}
7   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.365167,-0.761633,-1.2469,-1.79512,-2.74086,-3.43183,-4.44177],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (111.708,'kcal/mol','+|-',2.4),
        S298 = (1.26927,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=[C]C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 333,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_N-3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,[B,D,T,Q]}
2   C u0 {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.540419,-1.0216,-1.56483,-2.0908,-2.93794,-3.57136,-4.53165],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.227,'kcal/mol','+|-',2.4),
        S298 = (1.06278,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 334,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,[B,D,T,Q]}
2   C u0 {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.539656,-1.00455,-1.53667,-2.07018,-2.93787,-3.57703,-4.52737],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.425,'kcal/mol','+|-',3.07394),
        S298 = (1.09456,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 335,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R_Sp-6R!H-5C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[B,D,T,Q]}
2   C u0 r1 {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]} {6,S}
6   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.550222,-1.01015,-1.53813,-2.06521,-2.92134,-3.56029,-4.52754],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (112.338,'kcal/mol','+|-',2.4),
        S298 = (0.952538,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[C]=CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 336,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R_N-Sp-6R!H-5C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[B,D,T,Q]}
2   C u0 r1 {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   C u0 r0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.52909,-0.998943,-1.53521,-2.07515,-2.95441,-3.59377,-4.5272],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (114.512,'kcal/mol','+|-',2.4),
        S298 = (1.23659,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[C]=CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 337,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
4   C   ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.146723,-1.27566,-2.13464,-2.73768,-3.76737,-4.31184,-5.18665],'cal/mol/K','+|-',[3,3,3,3,3.5836,4.13,3.04001]),
        H298 = (120.416,'kcal/mol','+|-',10.0162),
        S298 = (1.90367,'cal/mol/K','+|-',4.0365),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 338,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[B,D,T,Q]}
2   C   u0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   R!H ux {2,D}
4   C   ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.583173,-1.23239,-2.26862,-2.97625,-4.23596,-4.88663,-5.7138],'cal/mol/K','+|-',[3,3,3,3,4.51621,5.11056,3.55128]),
        H298 = (119.831,'kcal/mol','+|-',14.4227),
        S298 = (1.47321,'cal/mol/K','+|-',3.34165),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 339,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[B,D,T,Q]}
2   C u0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
6   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.00625,-1.13365,-2.0836,-2.62404,-3.75649,-4.20759,-5.5508],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (112.122,'kcal/mol','+|-',5.2),
        S298 = (0.317014,'cal/mol/K','+|-',3.00498),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 340,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_3R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[B,D,T,Q]}
2   C   u0 r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   ux {2,D} {7,[S,D,T,B,Q]}
4   C   ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]}
6   O   ux r1 {2,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.805725,-1.41451,-2.35481,-2.84721,-4.02415,-4.43123,-5.53806],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.899,'kcal/mol','+|-',5.2),
        S298 = (-0.745405,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C1[C]=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 341,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[B,D,T,Q]}
2   C   u0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.322818,-1.29315,-2.38248,-3.19299,-4.53102,-5.3045,-5.81411],'cal/mol/K','+|-',[3.56781,3,3,4.22658,7.22176,8.09133,5.79501]),
        H298 = (122.538,'kcal/mol','+|-',12.7805),
        S298 = (2.18471,'cal/mol/K','+|-',3.31009),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 342,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_N-3R!H->C_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[B,D,T,Q]}
2   C   u0 r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux r1 {2,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.06939,-1.14229,-3.42435,-5.26206,-8.06632,-9.26549,-8.65097],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.088,'kcal/mol','+|-',5.2),
        S298 = (3.80512,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OOC=[C]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 343,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
4   C ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.514455,-1.10218,-1.70086,-2.23092,-3.01692,-3.60863,-4.52827],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (120.638,'kcal/mol','+|-',2.4),
        S298 = (1.16961,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[C]1=COC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 344,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_N-3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.656988,-1.89317,-2.40726,-2.6254,-2.9958,-2.87645,-3.90047],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (123.875,'kcal/mol','+|-',5.2),
        S298 = (5.81522,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[C]=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 345,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0738359,-1.15016,-2.11759,-2.73703,-3.47174,-4.06093,-5.39348],'cal/mol/K','+|-',[3,3.2167,3.67691,3.67981,3.33212,3.1884,4.17844]),
        H298 = (101.705,'kcal/mol','+|-',15.4651),
        S298 = (1.71462,'cal/mol/K','+|-',6.62053),
    ),
    shortDesc = """Radical correction fitted to 183 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 346,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.347226,-1.20696,-1.94234,-2.45376,-3.1511,-3.66319,-4.58031],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.009,'kcal/mol','+|-',10.9169),
        S298 = (1.84907,'cal/mol/K','+|-',9.94675),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 347,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O",
    group = 
"""
1 * C u1 r1 {2,D}
2   C ux {1,D} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0170001,-1.30226,-2.31468,-2.89055,-3.53874,-3.9349,-4.82725],'cal/mol/K','+|-',[3,3.33764,3.63349,3.46124,3,3,3]),
        H298 = (120.325,'kcal/mol','+|-',8.18714),
        S298 = (0.327947,'cal/mol/K','+|-',6.7143),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 348,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.147151,-1.04657,-2.04932,-2.64008,-3.32477,-3.77835,-4.70209],'cal/mol/K','+|-',[3,3.05439,3.37832,3.22727,3,3,3]),
        H298 = (121.143,'kcal/mol','+|-',5.2),
        S298 = (-0.149548,'cal/mol/K','+|-',6.29287),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 349,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.388004,-0.683737,-1.66439,-2.26826,-3.02718,-3.55661,-4.55627],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (120.685,'kcal/mol','+|-',5.2),
        S298 = (-0.903685,'cal/mol/K','+|-',4.35102),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 350,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   ux {1,D} {3,S} {6,S}
3   O   u0 {2,S}
4   R!H u0 {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12137,0.25228,-0.629401,-1.32583,-2.25778,-2.95325,-4.2798],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (120.954,'kcal/mol','+|-',5.52243),
        S298 = (0.41905,'cal/mol/K','+|-',6.20259),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 351,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_Ext-2R!H-R_3O-inRing",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   ux r1 {1,D} {3,S} {6,S}
3   O   u0 r1 {2,S}
4   R!H u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   R!H ux r1 {4,[S,D,T,B,Q]}
6   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.439881,-0.828181,-1.60876,-2.04834,-2.70008,-3.23573,-4.12026],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (117.735,'kcal/mol','+|-',5.2),
        S298 = (-2.61734,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=[C]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 352,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_Ext-2R!H-R_N-3O-inRing",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   ux r1 {1,D} {3,S} {6,S}
3   O   u0 r0 {2,S}
4   R!H u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   R!H ux r1 {4,[S,D,T,B,Q]}
6   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.42425,0.732485,-0.19413,-1.00471,-2.06121,-2.82771,-4.35071],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (121.64,'kcal/mol','+|-',2.4),
        S298 = (1.76856,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CO[C]=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 353,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C ux {1,D} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.190447,-1.92941,-3.35227,-3.94933,-4.58493,-4.6601,-5.25404],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (119.785,'kcal/mol','+|-',5.2),
        S298 = (-1.1548,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 354,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,D} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   C   ux r1 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,S}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H u0 {4,S}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.367395,-1.93127,-3.45988,-4.15807,-4.72555,-4.63719,-5.74934],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (120.021,'kcal/mol','+|-',5.2),
        S298 = (-2.05108,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)[C]=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 355,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,D} {4,S}
2   C u0 {1,D} {3,S}
3   O u0 {2,S}
4   C u0 {1,S} {5,S}
5   O u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.223788,-0.853184,-1.66068,-2.1762,-2.83797,-3.48091,-4.40335],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (120.733,'kcal/mol','+|-',5.2),
        S298 = (-2.07189,'cal/mol/K','+|-',4.55838),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 356,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_N-5R!H->C_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   u0 r1 {1,D} {3,S}
3   O   u0 r1 {2,S} {6,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {5,S}
5   O   u0 {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.243073,-0.613677,-1.57505,-2.05821,-2.54345,-3.25626,-3.9821],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (121.195,'kcal/mol','+|-',5.2),
        S298 = (-4.30338,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[C]=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 357,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O",
    group = 
"""
1 * C u1 r1 {2,D}
2   C ux {1,D} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.520594,-1.15693,-1.74687,-2.22445,-2.94759,-3.52054,-4.45066],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (112.94,'kcal/mol','+|-',8.97458),
        S298 = (2.64766,'cal/mol/K','+|-',11.2818),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 358,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.527416,-1.14001,-1.70504,-2.16602,-2.88246,-3.45603,-4.39477],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (113.648,'kcal/mol','+|-',8.90731),
        S298 = (2.83387,'cal/mol/K','+|-',12.4316),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 359,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_4R!H->O",
    group = 
"""
1 * C u1 r1 {2,D}
2   C u0 {1,D} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.755811,-1.27087,-1.78628,-2.24472,-2.9717,-3.58084,-4.51926],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (117.109,'kcal/mol','+|-',9.73915),
        S298 = (1.62973,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 360,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_4R!H->O_Ext-3C-R_Ext-1C-R",
    group = 
"""
1 * C u1 r1 {2,D} {6,S}
2   C u0 {1,D} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {5,D}
4   O ux {3,S}
5   C ux {3,D}
6   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.793418,-1.31464,-1.82745,-2.28057,-2.98269,-3.59708,-4.52375],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (119.921,'kcal/mol','+|-',2.4),
        S298 = (1.81666,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 361,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_4R!H->O_Ext-3C-R_Ext-1C-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D} {6,S}
2   C   u0 r1 {1,D} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S} {5,D}
4   O   ux r0 {3,S}
5   C   ux r1 {3,D}
6   O   u0 r1 {1,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.945903,-1.50027,-1.99414,-2.39158,-2.97246,-3.59507,-4.54017],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (119.938,'kcal/mol','+|-',2.4),
        S298 = (1.93783,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=[C]OC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 362,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,D}
2   C ux {1,D} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.37325,-1.05168,-1.65021,-2.11289,-2.82221,-3.37178,-4.31073],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.183,'kcal/mol','+|-',5.2),
        S298 = (3.64667,'cal/mol/K','+|-',16.6561),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 363,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_N-4R!H->O_Ext-3C-R",
    group = 
"""
1 * C u1 r1 {2,D}
2   C ux {1,D} {3,S}
3   C u0 {2,S} {4,[S,D]} {5,[S,D]}
4   C u0 {3,[S,D]}
5   C u0 {3,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0806156,-1.05528,-1.75355,-2.13099,-2.60193,-2.97902,-3.80866],'cal/mol/K','+|-',[3,3,3,3,3,3,3.35039]),
        H298 = (111.047,'kcal/mol','+|-',12.7279),
        S298 = (8.79639,'cal/mol/K','+|-',34.7653),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 364,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_N-4R!H->O_Ext-3C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,D} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,D} {3,S}
3   C   u0 r1 {2,S} {4,[S,D]} {5,[S,D]}
4   C   u0 r1 {3,[S,D]}
5   C   u0 {3,[S,D]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.231261,-1.01079,-1.63325,-2.02327,-2.72966,-3.37378,-4.53761],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.466,'kcal/mol','+|-',2.4),
        S298 = (1.23246,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=[C]CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 365,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_N-4R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,D} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,D} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.303809,-0.880208,-1.45009,-1.95597,-2.79826,-3.44997,-4.48411],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (110.676,'kcal/mol','+|-',2.4),
        S298 = (1.32678,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC=[C]CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 366,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_N-4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux r1 {1,D} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   ux r1 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
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
    index = 367,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,D} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18229,-2.44372,-3.27427,-3.68768,-4.1836,-4.55376,-5.1639],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (106.276,'kcal/mol','+|-',5.2),
        S298 = (2.89133,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=[C]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 368,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.125724,-1.14316,-2.13918,-2.77193,-3.51125,-4.10994,-5.49369],'cal/mol/K','+|-',[3,3.34321,3.82234,3.82704,3.46971,3.33162,4.36547]),
        H298 = (99.9204,'kcal/mol','+|-',12.1622),
        S298 = (1.69806,'cal/mol/K','+|-',6.14431),
    ),
    shortDesc = """Radical correction fitted to 165 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 369,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.314338,-1.07763,-1.83784,-2.40163,-3.19114,-3.77661,-4.8173],'cal/mol/K','+|-',[3,3,3,3,3.05964,3.14016,3.55075]),
        H298 = (103.386,'kcal/mol','+|-',16.255),
        S298 = (1.40383,'cal/mol/K','+|-',3.75476),
    ),
    shortDesc = """Radical correction fitted to 30 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 370,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.257344,-0.989548,-1.70538,-2.23548,-2.99216,-3.55207,-4.57284],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (104.921,'kcal/mol','+|-',5.2),
        S298 = (1.51363,'cal/mol/K','+|-',3.6185),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 371,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.333597,-1.17372,-1.99985,-2.54579,-3.2267,-3.71523,-4.74933],'cal/mol/K','+|-',[3,3,3,3,3,3,3.76892]),
        H298 = (103.81,'kcal/mol','+|-',5.2),
        S298 = (1.21124,'cal/mol/K','+|-',4.0667),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 372,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C   ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.906493,-2.05505,-3.17819,-3.57174,-3.60851,-3.62546,-5.29459],'cal/mol/K','+|-',[5.10769,3.97335,3,3,3,4.25352,8.94726]),
        H298 = (103.269,'kcal/mol','+|-',5.2),
        S298 = (2.00116,'cal/mol/K','+|-',4.31385),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 373,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O u0 r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]}
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
    index = 374,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.969312,-2.17169,-3.26145,-3.6247,-3.56118,-3.49593,-4.4892],'cal/mol/K','+|-',[5.88296,4.52577,3,3,3,4.83985,8.94553]),
        H298 = (103.575,'kcal/mol','+|-',5.2),
        S298 = (1.524,'cal/mol/K','+|-',3.92935),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 375,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R_N-5R!H->C_4R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {3,S} {4,S}
2   C u0 r1 {1,S} {3,S}
3   O ux r1 {1,S} {2,S}
4   C u0 r1 {1,S} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.680747,-1.29592,-3.17885,-4.06438,-4.37701,-4.89546,-10.8017],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (104.112,'kcal/mol','+|-',5.2),
        S298 = (3.74096,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1O[C]1C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 376,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R_N-5R!H->C_N-4R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O u0 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux r0 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.03344,-2.3663,-3.2798,-3.527,-3.37988,-3.18492,-3.08642],'cal/mol/K','+|-',[7.3011,5.47617,2.99947,2,3.48175,5.65199,6.09005]),
        H298 = (103.518,'kcal/mol','+|-',3.73645),
        S298 = (1.03134,'cal/mol/K','+|-',3.63072),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 377,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R_N-5R!H->C_N-4R!H-inRing_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   O   u0 r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C   ux r0 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   u0 r0 {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.61477,-4.30242,-4.34027,-3.70875,-2.1489,-1.18664,-0.933265],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.197,'kcal/mol','+|-',2.4),
        S298 = (-0.252313,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC[C]1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 378,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {1,S} {2,S} {5,[S,D,T,B,Q]}
4   R!H u0 {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.706614,-1.26332,-1.73123,-2.16469,-2.91069,-3.51046,-4.49618],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.456,'kcal/mol','+|-',2.97628),
        S298 = (0.610928,'cal/mol/K','+|-',2.69786),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 379,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {4,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 r1 {1,S} {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   R!H u0 {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.527452,-1.13845,-1.57003,-1.96297,-2.68866,-3.3223,-4.45812],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (105.508,'kcal/mol','+|-',2.4),
        S298 = (1.56477,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 380,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {1,S} {2,S}
4   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.533149,-1.04462,-1.49564,-1.91001,-2.63198,-3.20228,-4.16267],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.878,'kcal/mol','+|-',4.41453),
        S298 = (3.04495,'cal/mol/K','+|-',2.99549),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 381,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_3R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S} {4,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {1,S} {2,S}
4   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.178754,-0.955987,-1.6608,-2.19054,-3.00486,-3.59333,-4.44289],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (106.438,'kcal/mol','+|-',2.4),
        S298 = (4.10402,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 382,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_3R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S} {4,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {1,S} {2,S}
4   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.887544,-1.13325,-1.33048,-1.62948,-2.25911,-2.81124,-3.88245],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.317,'kcal/mol','+|-',2.4),
        S298 = (1.98589,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 383,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0664269,-0.821278,-1.73437,-2.41292,-3.32933,-3.95734,-4.76425],'cal/mol/K','+|-',[2,2,2.65279,3.04762,3.03341,2.67381,2]),
        H298 = (103.507,'kcal/mol','+|-',3.29816),
        S298 = (0.532848,'cal/mol/K','+|-',4.26774),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 384,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S} {4,S}
2   C u0 {1,S} {3,S}
3   O u0 {1,S} {2,S}
4   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.499037,-0.865139,-1.32768,-1.76476,-2.5373,-3.18285,-4.31522],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.466,'kcal/mol','+|-',2.4),
        S298 = (-0.244953,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 385,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_4R!H->C_Ext-2C-R",
    group = 
"""
1 * C u1 r1 {2,S} {3,S} {4,S}
2   C u0 {1,S} {3,S} {5,S}
3   O u0 {1,S} {2,S}
4   C u0 {1,S}
5   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.228536,-0.515615,-0.986057,-1.44528,-2.27405,-2.98189,-4.24088],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.187,'kcal/mol','+|-',2.54426),
        S298 = (-0.350807,'cal/mol/K','+|-',2.14634),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 386,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {4,S}
2   C   u0 r1 {1,S} {3,S} {5,S}
3   O   u0 r1 {1,S} {2,S}
4   C   u0 {1,S}
5   O   u0 r0 {2,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.496479,-0.990016,-1.47603,-1.9179,-2.68065,-3.30039,-4.35659],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.086,'kcal/mol','+|-',2.4),
        S298 = (0.408039,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 387,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.490525,-0.788383,-2.03939,-2.89904,-3.92335,-4.5382,-5.10103],'cal/mol/K','+|-',[2,2.28317,3.36792,3.77135,3.60786,3.08321,2]),
        H298 = (104.289,'kcal/mol','+|-',3.37374),
        S298 = (1.1162,'cal/mol/K','+|-',5.52876),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 388,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_N-4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.651207,-0.832039,-2.27075,-3.23387,-4.31395,-4.91275,-5.32036],'cal/mol/K','+|-',[2.04437,2.78811,3.96607,4.31786,3.9829,3.30037,2]),
        H298 = (104.564,'kcal/mol','+|-',3.90604),
        S298 = (1.6864,'cal/mol/K','+|-',6.16829),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 389,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_N-4R!H->C_Ext-2C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {4,S}
2   C   u0 r1 {1,S} {3,S} {5,S}
3   O   u0 r1 {1,S} {2,S}
4   O   u0 {1,S}
5   R!H u0 r0 {2,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.685186,-2.14048,-4.51629,-5.72647,-6.57826,-6.70981,-5.89496],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (106.799,'kcal/mol','+|-',2.4),
        S298 = (5.19163,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OCC1O[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 390,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_N-4R!H->C_Ext-2C-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O ux {1,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.387543,-0.989828,-1.53601,-2.02215,-2.83462,-3.46555,-4.46517],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.189,'kcal/mol','+|-',2.4),
        S298 = (-0.611126,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1O[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 391,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O ux {1,[S,D,T,B,Q]}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.65598,0.634195,-0.759943,-1.95299,-3.52895,-4.56288,-5.60095],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.703,'kcal/mol','+|-',2.4),
        S298 = (0.478685,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 392,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.30221,-0.939266,-1.5538,-2.07515,-2.90819,-3.53815,-4.52103],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.446,'kcal/mol','+|-',2.4),
        S298 = (3.47778,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 393,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_3R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.460377,-1.18307,-1.81175,-2.29311,-3.08175,-3.68041,-4.6001],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.476,'kcal/mol','+|-',2.4),
        S298 = (3.72827,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 394,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_3R!H->C_Ext-2C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,S}
3   C   ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H u0 r0 {2,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.17388,-2.01085,-2.71466,-3.19285,-3.91632,-4.40135,-5.00618],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (108.638,'kcal/mol','+|-',2.4),
        S298 = (4.35064,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 395,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_3R!H->C_Ext-2C-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0632128,-0.457259,-1.08836,-1.65785,-2.58697,-3.28774,-4.37517],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (110.34,'kcal/mol','+|-',2.4),
        S298 = (3.24501,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C(O)C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 396,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_3R!H->C_Ext-2C-R_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.270461,-1.08111,-1.63223,-2.02864,-2.74196,-3.35213,-4.41893],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.449,'kcal/mol','+|-',2.4),
        S298 = (3.58917,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 397,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.102529,-0.694946,-1.26994,-1.77693,-2.62695,-3.27577,-4.29234],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.522,'kcal/mol','+|-',2.4),
        S298 = (1.05652,'cal/mol/K','+|-',2.18187),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 398,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0934122,-0.739432,-1.36835,-1.90413,-2.75101,-3.36001,-4.25368],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.795,'kcal/mol','+|-',2.4),
        S298 = (1.19497,'cal/mol/K','+|-',2.23869),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 399,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S}
2   C   u0 r1 {1,S} {3,S} {4,[S,D,T,B,Q]}
3   O   u0 r1 {1,S} {2,S}
4   R!H ux {2,[S,D,T,B,Q]} {5,S}
5   R!H u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 400,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.102315,-0.421805,-1.10528,-1.71968,-2.63975,-3.2922,-4.25587],'cal/mol/K','+|-',[2,2,2,2,2.58599,2.74743,2]),
        H298 = (104.701,'kcal/mol','+|-',2.4),
        S298 = (0.996765,'cal/mol/K','+|-',2.65217),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 401,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S}
2   C   u0 r1 {1,S} {3,S} {4,S} {6,[S,D,T,B,Q]}
3   O   u0 r1 {1,S} {2,S}
4   C   u0 r0 {2,S} {5,S}
5   R!H u0 r0 {4,S}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 402,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_4R!H->C_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.56698,-1.02654,-1.5242,-2.01617,-2.87223,-3.50229,-4.50603],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.541,'kcal/mol','+|-',2.4),
        S298 = (1.38996,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 403,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_4R!H->C_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
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
    index = 404,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.424774,-1.65237,-2.24149,-2.55445,-3.09431,-3.5395,-4.3654],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.833,'kcal/mol','+|-',2.4),
        S298 = (2.26691,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(OO)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 405,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.360341,-0.968619,-1.53877,-2.0446,-2.88173,-3.52317,-4.52156],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.578,'kcal/mol','+|-',2.4),
        S298 = (1.53462,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 406,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.395434,-1.04683,-1.61998,-2.12238,-2.94391,-3.56506,-4.52883],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.432,'kcal/mol','+|-',2.4),
        S298 = (1.69108,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 407,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {3,S}
2   C                      u0 r1 {1,S} {3,S} {4,S}
3   O                      u0 r1 {1,S} {2,S}
4   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.367513,0.0748293,-0.240226,-0.605576,-1.4971,-2.35973,-4.02722],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.044,'kcal/mol','+|-',2.4),
        S298 = (-0.591887,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 408,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S}
2   O u0 {1,S} {3,S}
3   O ux {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.917956,-2.0105,-3.24062,-4.16122,-5.29854,-6.15469,-7.40633],'cal/mol/K','+|-',[4.5,6.32878,7.12131,7.65456,8.02362,7.88604,7.05095]),
        H298 = (85.7544,'kcal/mol','+|-',52.0541),
        S298 = (0.240958,'cal/mol/K','+|-',5.40303),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 409,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_N-2R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {4,S}
2   O   u0 {1,S} {3,S}
3   O   ux {1,S} {2,S}
4   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.40522,-2.9794,-4.71007,-5.88543,-7.16647,-8.14245,-9.49559],'cal/mol/K','+|-',[6.73841,8.89065,8.82055,8.88354,9.03323,8.09311,4.96739]),
        H298 = (71.0086,'kcal/mol','+|-',57.4029),
        S298 = (-1.25482,'cal/mol/K','+|-',4.6867),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 410,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_N-2R!H->C_Ext-1C-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S} {4,S}
2   O u0 r1 {1,S} {3,S}
3   O ux r1 {1,S} {2,S}
4   C u0 r0 {1,S}
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
    index = 411,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_N-2R!H->C_Ext-1C-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {3,S} {4,S}
2   O                      u0 r1 {1,S} {3,S}
3   O                      ux r1 {1,S} {2,S}
4   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8713,-4.91375,-6.62917,-7.81823,-9.13184,-9.90327,-10.5763],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (63.8806,'kcal/mol','+|-',2.4),
        S298 = (-2.27451,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 412,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.499416,-1.31896,-2.70184,-3.31366,-3.91092,-4.50386,-5.34351],'cal/mol/K','+|-',[3,3.50707,4.09033,3.98887,3.43557,3.24884,3.90066]),
        H298 = (98.5158,'kcal/mol','+|-',11.1056),
        S298 = (0.96928,'cal/mol/K','+|-',8.03857),
    ),
    shortDesc = """Radical correction fitted to 56 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 413,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
5   R!H ux {1,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.107737,-1.90051,-3.43067,-4.20269,-4.7055,-5.1933,-6.59924],'cal/mol/K','+|-',[3.17139,3.58433,4.00415,4.18422,3.68422,3.56415,4.36802]),
        H298 = (98.1297,'kcal/mol','+|-',7.18128),
        S298 = (3.51463,'cal/mol/K','+|-',7.40826),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 414,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
5   O   ux {1,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.58834,-1.6922,-3.67422,-4.44437,-4.82643,-5.36411,-6.99178],'cal/mol/K','+|-',[4.2065,5.40493,5.64844,5.52887,4.13251,3.16464,5.88873]),
        H298 = (94.8263,'kcal/mol','+|-',6.896),
        S298 = (2.67114,'cal/mol/K','+|-',7.96006),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 415,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   C   ux {1,S} {3,S}
3   C   ux {2,S} {4,D}
4   R!H ux {3,D}
5   O   ux {1,[S,D,T,B,Q]}
6   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.825235,-3.45946,-5.18623,-5.72452,-5.38145,-5.34142,-8.31316],'cal/mol/K','+|-',[5.66802,8.82624,10.6631,11.1207,9.01427,6.86557,11.9148]),
        H298 = (92.9593,'kcal/mol','+|-',6.64122),
        S298 = (4.79031,'cal/mol/K','+|-',12.358),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 416,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_2R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   C   ux r1 {1,S} {3,S} {7,[S,D,T,B,Q]}
3   C   ux {2,S} {4,D}
4   R!H ux r0 {3,D}
5   O   ux r1 {1,[S,D,T,B,Q]}
6   C   u0 {1,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.82918,-6.58001,-8.95621,-9.65627,-8.56848,-7.76876,-12.5257],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.3073,'kcal/mol','+|-',5.2),
        S298 = (9.15952,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OCOOC1(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 417,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
5   O   ux {1,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.29513,-0.808563,-2.91821,-3.80429,-4.54892,-5.37545,-6.33109],'cal/mol/K','+|-',[3.28472,3.19817,3,3,3,3,3]),
        H298 = (95.7599,'kcal/mol','+|-',7.11427),
        S298 = (1.61155,'cal/mol/K','+|-',6.06087),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 418,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C_Ext-5O-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,[S,T,Q,B]}
3   C   u0 r1 {2,[S,T,Q,B]} {4,D}
4   R!H u0 {3,D}
5   O   u0 r1 {1,S} {7,S}
6   C   ux r0 {1,[S,D,T,B,Q]}
7   C   u0 r1 {5,S} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.32288,-0.02226,-2.47122,-3.62434,-4.59701,-5.7889,-7.00222],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.2521,'kcal/mol','+|-',5.2),
        S298 = (-1.04531,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC(=O)C(C)(C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 419,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,D}
4   C u0 {3,D}
5   O u0 {1,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0641377,-2.12511,-3.89738,-4.45323,-4.64294,-4.94828,-5.68977],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.5769,'kcal/mol','+|-',5.2),
        S298 = (3.86444,'cal/mol/K','+|-',5.26204),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 420,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C_4R!H->C_4C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 r1 {3,D}
5   O u0 r1 {1,S}
6   C u0 r0 {1,S}
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
    index = 421,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C_4R!H->C_N-4C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 r0 {3,D}
5   O u0 r1 {1,S}
6   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.426695,-1.82866,-3.58465,-4.09798,-4.51471,-4.98592,-4.99307],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.0771,'kcal/mol','+|-',5.2),
        S298 = (2.00402,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CO[C](C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 422,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,D}
4   O ux {3,D}
5   O ux r1 {1,[S,D,T,B,Q]}
6   C ux {1,[S,D,T,B,Q]}
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
    index = 423,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   R!H ux {1,S} {3,S}
3   C   ux {2,S} {4,D}
4   R!H ux {3,D}
5   C   ux {1,[S,D,T,B,Q]}
6   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.478978,-2.01161,-3.30078,-4.0738,-4.64101,-5.1022,-6.38989],'cal/mol/K','+|-',[3,3,3.10192,3.55884,3.63908,3.91417,3.57598]),
        H298 = (99.577,'kcal/mol','+|-',5.2),
        S298 = (3.96449,'cal/mol/K','+|-',7.34776),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 424,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   C   ux {1,S} {3,S}
3   C   ux {2,S} {4,D}
4   R!H ux {3,D}
5   C   ux {1,[S,D,T,B,Q]}
6   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.504308,-1.91135,-2.98926,-3.56594,-4.02133,-4.39947,-5.91055],'cal/mol/K','+|-',[3,3,3.12981,3.00064,3,3,3.62058]),
        H298 = (98.8654,'kcal/mol','+|-',5.2),
        S298 = (3.56014,'cal/mol/K','+|-',6.61345),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 425,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   C   ux {1,S} {3,S}
3   C   ux {2,S} {4,D}
4   R!H ux {3,D} {7,[S,D,T,B,Q]}
5   C   ux r1 {1,[S,D,T,B,Q]}
6   C   u0 r1 {1,S}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 426,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,S}
2   C   u0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D}
4   R!H u0 {3,D}
5   C   u0 {1,S}
6   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.181864,-2.29008,-3.68283,-4.33466,-4.62495,-5.02589,-5.39759],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.1643,'kcal/mol','+|-',5.33188),
        S298 = (5.29049,'cal/mol/K','+|-',6.02363),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 427,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_3R!H-inRing_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   C u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 {3,D}
5   C u0 {1,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.102965,-2.57145,-3.98127,-4.56635,-4.90638,-5.22321,-5.12802],'cal/mol/K','+|-',[3,3,3,3,3,3.07686,3]),
        H298 = (97.4115,'kcal/mol','+|-',6.41689),
        S298 = (6.02827,'cal/mol/K','+|-',6.43137),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 428,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_3R!H-inRing_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   C u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D} {7,S}
4   C u0 {3,D}
5   C u0 {1,S}
6   C u0 {1,S}
7   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.149866,-3.14962,-4.69483,-5.22847,-5.45261,-5.82276,-5.26993],'cal/mol/K','+|-',[3,3,3,3,3,3.21048,3]),
        H298 = (98.5858,'kcal/mol','+|-',7.01851),
        S298 = (7.71073,'cal/mol/K','+|-',3.84562),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 429,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_3R!H-inRing_4R!H->C_Ext-3R!H-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D} {7,S}
4   C   u0 r0 {3,D}
5   C   u0 r1 {1,S} {8,[S,D,T,B,Q]}
6   C   u0 {1,S}
7   O   u0 r1 {3,S}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.494843,-3.1075,-4.54482,-5.32932,-6.18865,-6.95783,-5.16268],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.1044,'kcal/mol','+|-',5.2),
        S298 = (6.3511,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C[C](C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 430,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_3R!H-inRing_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D}
4   O u0 {3,D}
5   C u0 r1 {1,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.418563,-1.44595,-2.78752,-3.63959,-3.78066,-4.43393,-6.20629],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.4226,'kcal/mol','+|-',5.2),
        S298 = (3.07716,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 431,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_N-3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   C u0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,D}
4   O u0 {3,D}
5   C u0 {1,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.61893,-2.69447,-3.70042,-4.12579,-4.42842,-4.40827,-8.64803],'cal/mol/K','+|-',[6.30274,4.28246,3,3,3,3,3]),
        H298 = (98.1672,'kcal/mol','+|-',5.2),
        S298 = (3.9658,'cal/mol/K','+|-',6.14906),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 432,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_N-3R!H-inRing_2C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r0 {2,S} {4,D}
4   O u0 r0 {3,D}
5   C u0 r1 {1,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.609427,-1.18039,-2.70336,-3.27525,-3.82628,-3.95378,-8.21318],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.2262,'kcal/mol','+|-',5.2),
        S298 = (1.79178,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 433,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_N-3R!H-inRing_N-2C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   C u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,D}
4   O u0 r0 {3,D}
5   C u0 r1 {1,S}
6   C u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.84728,-4.20854,-4.69748,-4.97634,-5.03057,-4.86275,-9.08289],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.1082,'kcal/mol','+|-',5.2),
        S298 = (6.13982,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 434,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   O ux {1,S} {3,S}
3   C ux {2,S} {4,D}
4   O ux {3,D}
5   C ux {1,[S,D,T,B,Q]}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.409322,-2.28734,-4.15744,-5.4704,-6.3451,-7.03472,-7.70808],'cal/mol/K','+|-',[3,3,3,4.03286,4.52911,5.10105,3]),
        H298 = (102.114,'kcal/mol','+|-',5.2),
        S298 = (5.07646,'cal/mol/K','+|-',10.4277),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 435,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_N-2R!H->C_2O-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   O ux r1 {1,S} {3,S}
3   C ux {2,S} {4,D}
4   O ux {3,D}
5   C ux {1,[S,D,T,B,Q]}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.24473,-2.66323,-4.98725,-6.62701,-7.63577,-8.49374,-7.13634],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.131,'kcal/mol','+|-',5.2),
        S298 = (8.0277,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 436,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_N-2R!H->C_2O-inRing_Ext-6R!H-R_5C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   O ux r1 {1,S} {3,S}
3   C ux r1 {2,S} {4,D}
4   O ux r0 {3,D}
5   C ux r1 {1,[S,D,T,B,Q]}
6   C u0 {1,S} {7,S}
7   O u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0209725,-2.5392,-5.01153,-6.85664,-7.99733,-8.83875,-7.49498],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.959,'kcal/mol','+|-',5.2),
        S298 = (7.00071,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1COC[C](COO)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 437,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_N-2R!H->C_2O-inRing_Ext-6R!H-R_N-5C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   O ux r1 {1,S} {3,S}
3   C ux r1 {2,S} {4,D}
4   O ux r0 {3,D}
5   C ux r0 {1,[S,D,T,B,Q]}
6   C u0 r1 {1,S} {7,S}
7   O u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.510433,-2.78726,-4.96297,-6.39739,-7.27421,-8.14872,-6.77771],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.303,'kcal/mol','+|-',5.2),
        S298 = (9.0547,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 438,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_N-2R!H->C_N-2O-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   O ux r0 {1,S} {3,S}
3   C ux {2,S} {4,D}
4   O ux r0 {3,D}
5   C ux r1 {1,[S,D,T,B,Q]}
6   C u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.738506,-1.53556,-2.49783,-3.15718,-3.76377,-4.1167,-8.85156],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.079,'kcal/mol','+|-',5.2),
        S298 = (-0.82603,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)O[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 439,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.28961,-0.507767,-1.83117,-2.71026,-3.72191,-4.4475,-5.29348],'cal/mol/K','+|-',[3,4.23696,4.39445,4.33913,3.87037,3.81093,3.61058]),
        H298 = (100.279,'kcal/mol','+|-',6.92837),
        S298 = (1.48131,'cal/mol/K','+|-',5.15537),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 440,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_5R!H->O",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S} {4,D} {5,S}
4   O u0 {3,D}
5   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.550757,-0.230549,-1.21627,-1.99856,-3.10486,-3.9534,-5.52303],'cal/mol/K','+|-',[3,3,3,3,3,3.32637,3.57257]),
        H298 = (102.661,'kcal/mol','+|-',5.2),
        S298 = (1.27306,'cal/mol/K','+|-',3.11977),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 441,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_5R!H->O_Ext-1C-R",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S} {4,D} {5,S}
4   O u0 {3,D}
5   O u0 {3,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.0071,-0.294526,-1.71587,-2.65648,-3.91895,-4.86309,-6.82145],'cal/mol/K','+|-',[3,3,3,3.26612,3.62337,4.01661,3]),
        H298 = (103.902,'kcal/mol','+|-',5.2),
        S298 = (1.46938,'cal/mol/K','+|-',4.96072),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 442,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_5R!H->O_Ext-1C-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {7,[S,D,T,B,Q]}
3   C   u0 {2,S} {4,D} {5,S}
4   O   u0 {3,D}
5   O   u0 {3,S}
6   C   u0 r1 {1,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.21315,-0.106284,-1.13467,-1.50173,-2.63789,-3.443,-7.79347],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.179,'kcal/mol','+|-',5.2),
        S298 = (-0.284497,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C(O)C1[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 443,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.50618,-0.58902,-2.0114,-2.91886,-3.90277,-4.59233,-5.2262],'cal/mol/K','+|-',[3,4.85081,4.93472,4.76236,4.16663,4.07043,3.81998]),
        H298 = (99.456,'kcal/mol','+|-',7.28977),
        S298 = (1.54235,'cal/mol/K','+|-',5.7509),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 444,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   C   ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.29412,-1.04151,-2.94107,-4.09533,-5.20174,-5.85863,-5.56487],'cal/mol/K','+|-',[3,6.51129,6.43277,5.96839,4.5888,4.22264,3.24174]),
        H298 = (102.518,'kcal/mol','+|-',7.28983),
        S298 = (2.31381,'cal/mol/K','+|-',7.10697),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 445,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   R!H u0 {1,S} {3,S}
3   C   u0 {2,S} {4,D} {5,S}
4   R!H u0 {3,D}
5   C   u0 {3,S} {7,[S,D,T,B,Q]}
6   R!H u0 {1,S} {8,S}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.75679,-0.934341,-2.36201,-3.31022,-4.41949,-4.79938,-4.89218],'cal/mol/K','+|-',[3,9.01335,8.48476,7.58271,5.56989,4.44178,3.86909]),
        H298 = (99.9617,'kcal/mol','+|-',5.2),
        S298 = (1.26572,'cal/mol/K','+|-',8.7989),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 446,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_Ext-6R!H-R_Int-6R!H-4R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   R!H u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D} {5,S}
4   R!H u0 {3,D} {6,[S,D,T,B,Q]}
5   C   u0 {3,S} {7,[S,D,T,B,Q]}
6   R!H u0 r1 {1,S} {4,[S,D,T,B,Q]} {8,S}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.77757,2.26515,0.952011,0.172897,-1.07465,-1.7449,-2.01647],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.2251,'kcal/mol','+|-',5.2),
        S298 = (-4.54558,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC1=CC(O)[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 447,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   R!H u0 {1,S} {3,S}
3   C   u0 {2,S} {4,D} {5,S}
4   R!H u0 {3,D}
5   C   u0 {3,S} {7,S}
6   R!H u0 {1,S} {8,S}
7   C   u0 {5,S} {9,[S,D,T,B,Q]}
8   C   u0 {6,S}
9   R!H u0 {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.61308,-4.04557,-5.45158,-6.09129,-6.24814,-5.92098,-5.67233],'cal/mol/K','+|-',[3,9.42247,7.92739,6.69329,4.60184,3.02852,3]),
        H298 = (100.162,'kcal/mol','+|-',5.2),
        S298 = (3.9003,'cal/mol/K','+|-',6.36188),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 448,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D} {5,S}
4   R!H u0 {3,D}
5   C   u0 {3,S} {7,S}
6   R!H u0 r1 {1,S} {8,S}
7   C   u0 {5,S} {9,[S,D,T,B,Q]}
8   C   u0 r1 {6,S}
9   R!H u0 r0 {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.06919,-0.714224,-2.64882,-3.72485,-4.62114,-4.85024,-5.74347],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.0716,'kcal/mol','+|-',5.2),
        S298 = (1.65103,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCCC1=CCC(C)[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 449,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_N-2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D} {5,S}
4   R!H u0 {3,D}
5   C   u0 {3,S} {7,S}
6   R!H u0 r1 {1,S} {8,S}
7   C   u0 {5,S} {9,[S,D,T,B,Q]}
8   C   u0 r1 {6,S}
9   R!H u0 r0 {7,[S,D,T,B,Q]}
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
    index = 450,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   ux r0 {3,D}
5   C   ux r1 {3,[S,D,T,B,Q]} {7,S}
6   C   ux r1 {1,[S,D,T,B,Q]}
7   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.475571,-0.988731,-2.73786,-4.36605,-6.06207,-7.45311,-6.64156],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.722,'kcal/mol','+|-',5.2),
        S298 = (4.01967,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CC(OO)C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 451,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,D} {5,S}
4   O   u0 {3,D}
5   C   u0 {3,S} {7,[S,D,T,B,Q]}
6   O   u0 {1,S}
7   R!H u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.27806,-1.28222,-4.2008,-5.53019,-6.33608,-7.17988,-6.37189],'cal/mol/K','+|-',[3,3.1625,3.7529,3.8225,3.19782,3,3]),
        H298 = (107.53,'kcal/mol','+|-',5.2),
        S298 = (3.55708,'cal/mol/K','+|-',5.4047),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 452,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_N-6R!H->C_Int-6O-5BrCClFINPSSi",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D} {5,S}
4   O   u0 {3,D}
5   C   u0 r1 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O   u0 r1 {1,S} {5,[S,D,T,B,Q]}
7   R!H u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.89713,-0.164108,-2.87395,-4.17873,-5.20548,-6.33511,-6.73525],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.236,'kcal/mol','+|-',5.2),
        S298 = (1.64623,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1O[CH]OC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 453,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   C   ux {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.270507,-1.89777,-2.98972,-2.87805,-2.36315,-2.37653,-2.62986],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.9155,'kcal/mol','+|-',5.2),
        S298 = (-2.45635,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]CCC=C1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 454,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   R!H u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D} {5,S}
4   R!H u0 {3,D} {7,[S,D,T,B,Q]}
5   C   u0 {3,S}
6   R!H u0 r1 {1,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.729875,0.0744822,-0.690897,-1.31971,-2.2679,-3.04186,-4.33334],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.5365,'kcal/mol','+|-',2.4),
        S298 = (3.04595,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CCC(C)[CH]C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 455,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   R!H u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D} {5,S}
4   R!H u0 {3,D}
5   C   u0 {3,S}
6   R!H u0 r1 {1,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.21646,2.47398,0.229417,-1.74727,-3.93945,-5.48934,-9.81182],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.3088,'kcal/mol','+|-',5.2),
        S298 = (-0.815252,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(OO)C1[CH]OC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 456,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.706674,-0.504853,-1.6937,-2.44599,-3.23808,-3.67018,-4.55635],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.1401,'kcal/mol','+|-',5.2),
        S298 = (0.637112,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 457,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_N-2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.228512,-0.661869,-1.14192,-1.60692,-2.45981,-3.19915,-4.47901],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (96.3009,'kcal/mol','+|-',2.4),
        S298 = (0.865981,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CO[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 458,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   C   ux {3,D} {6,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
6   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.45558,-1.42928,-2.80706,-3.14897,-3.55078,-4.21358,-4.59734],'cal/mol/K','+|-',[3,3,3.54426,3.18412,3,3,3]),
        H298 = (99.5659,'kcal/mol','+|-',20.6063),
        S298 = (-0.74012,'cal/mol/K','+|-',10.6541),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 459,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   C   ux {3,D} {6,S}
5   C   ux {1,[S,D,T,B,Q]}
6   C   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.409235,-1.57374,-2.99753,-3.31781,-3.67889,-4.3065,-4.61227],'cal/mol/K','+|-',[3,3,3.3682,3.03397,3,3,3]),
        H298 = (97.7937,'kcal/mol','+|-',14.688),
        S298 = (-1.09824,'cal/mol/K','+|-',10.7254),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 460,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-6R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   C ux {3,D} {6,S}
5   C ux {1,[S,D,T,B,Q]}
6   C u0 {4,S} {7,S}
7   C u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.550903,-0.916043,-1.60801,-1.64746,-1.93893,-2.62185,-3.50617],'cal/mol/K','+|-',[4.05374,3.26193,3,3,3,3,3]),
        H298 = (83.2137,'kcal/mol','+|-',30.0184),
        S298 = (-2.3309,'cal/mol/K','+|-',19.9178),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 461,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-6R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {8,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D}
4   C   ux r1 {3,D} {6,S}
5   C   ux r1 {1,[S,D,T,B,Q]}
6   C   u0 r1 {4,S} {7,S}
7   C   u0 r1 {6,S}
8   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.98412,-2.06931,-2.64583,-2.01486,-1.56665,-2.13016,-2.63919],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (72.6006,'kcal/mol','+|-',5.2),
        S298 = (-9.37291,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC2C=CC1OOC2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 462,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   C   ux {3,D} {6,S}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,S}
6   C   ux {4,S} {5,[S,D,T,B,Q]}
7   C   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0354598,-0.854343,-1.72164,-2.47955,-3.28631,-3.64394,-5.54968],'cal/mol/K','+|-',[3,3,3,3,3,3,3.0966]),
        H298 = (99.3827,'kcal/mol','+|-',5.2),
        S298 = (4.48001,'cal/mol/K','+|-',3.82264),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 463,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-5R!H-R_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,D}
4   C ux r1 {3,D} {6,S}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,S}
6   C ux r1 {4,S} {5,[S,D,T,B,Q]}
7   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.281728,-0.165988,-0.835078,-1.51595,-2.49527,-3.25666,-4.45486],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.7074,'kcal/mol','+|-',5.2),
        S298 = (3.1285,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C2C=CCC1C2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 464,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-5R!H-R_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,D}
4   C ux r1 {3,D} {6,S}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,S}
6   C ux r1 {4,S} {5,[S,D,T,B,Q]}
7   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.352648,-1.5427,-2.6082,-3.44316,-4.07736,-4.03123,-6.64449],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.058,'kcal/mol','+|-',5.2),
        S298 = (5.83152,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC1[CH]OC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 465,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   C ux {3,D} {6,S}
5   C ux {1,[S,D,T,B,Q]}
6   C ux {4,S}
7   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.955052,-1.37356,-3.167,-3.80637,-4.18437,-4.59967,-5.03254],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.4646,'kcal/mol','+|-',5.2),
        S298 = (-0.170185,'cal/mol/K','+|-',7.38028),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 466,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_7R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D}
4   C   ux r1 {3,D} {6,S}
5   C   ux r1 {1,[S,D,T,B,Q]}
6   C   ux r1 {4,S}
7   C   ux {2,[S,D,T,B,Q]}
8   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.0093,-0.71539,-2.85615,-3.90882,-4.69973,-5.31048,-5.68815],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.0873,'kcal/mol','+|-',5.2),
        S298 = (2.43914,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1(C)[CH]CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 467,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   C ux {3,D} {6,S}
5   C ux {1,[S,D,T,B,Q]}
6   C ux {4,S}
7   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.646204,-2.00885,-3.68606,-3.87506,-4.12772,-4.87313,-4.54287],'cal/mol/K','+|-',[3,3,3.65801,3.28757,3,3,3]),
        H298 = (100.335,'kcal/mol','+|-',5.2),
        S298 = (-2.55304,'cal/mol/K','+|-',10.0289),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 468,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   C ux {3,D} {6,S}
5   C ux {1,[S,D,T,B,Q]}
6   C ux {4,S}
7   O ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   O ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9   C ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.701764,-2.62281,-4.68974,-4.79642,-4.93219,-5.59922,-4.59097],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.194,'kcal/mol','+|-',5.2),
        S298 = (-5.38661,'cal/mol/K','+|-',4.24753),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 469,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2    C ux {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3    C ux {2,[S,T,Q,B]} {4,D}
4    C ux {3,D} {6,S}
5    C ux {1,[S,D,T,B,Q]}
6    C ux {4,S}
7    O ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    O ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
10   C ux {9,[S,D,T,B,Q]} {11,S}
11   C ux {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.624549,-2.84916,-5.02245,-5.14736,-5.13991,-5.70329,-4.76502],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.5118,'kcal/mol','+|-',5.2),
        S298 = (-3.8803,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 470,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H_Ext-4R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {5,S}
2    C   u0 r1 {1,S} {3,S} {7,S}
3    C   u0 r1 {2,S} {4,D}
4    C   u0 r1 {3,D} {6,S} {12,[S,D,T,B,Q]}
5    C   u0 r1 {1,S}
6    C   u0 r1 {4,S}
7    O   u0 r0 {2,S} {8,S}
8    O   u0 r0 {7,S} {9,[S,D,T,B,Q]}
9    C   ux {8,[S,D,T,B,Q]} {10,S}
10   C   u0 {9,S} {11,S}
11   C   ux {10,S}
12   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09414,-1.88163,-4.11669,-4.81505,-5.38645,-5.88313,-5.67059],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.5491,'kcal/mol','+|-',5.2),
        S298 = (-4.53912,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC(OOCC(C)C)[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 471,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H_Ext-11R!H-R_Ext-12R!H-R_Ext-12R!H-R_Ext-11R!H-R_Ext-12R!H-R_Ext-12R!H-R_Ext-11R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2    C   ux r1 {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3    C   ux r1 {2,[S,T,Q,B]} {4,D}
4    C   ux r1 {3,D} {6,S}
5    C   ux r1 {1,[S,D,T,B,Q]}
6    C   ux r1 {4,S}
7    O   ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    O   ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9    C   ux r1 {8,[S,D,T,B,Q]} {10,[S,D,T,B,Q]} {12,[S,D,T,B,Q]}
10   C   ux r1 {9,[S,D,T,B,Q]} {11,S}
11   C   ux r1 {10,S} {14,[S,D,T,B,Q]}
12   C   ux r1 {9,[S,D,T,B,Q]} {13,D}
13   C   u0 r1 {12,D}
14   R!H ux {11,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.181017,-3.57692,-5.79714,-5.66234,-5.4183,-6.0454,-4.69752],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.282,'kcal/mol','+|-',5.2),
        S298 = (-3.43547,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCC=CC1OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 472,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {5,S}
2    C u0 {1,S} {3,S} {7,S}
3    C u0 {2,S} {4,D}
4    C u0 {3,D} {6,S}
5    C u0 {1,S}
6    C u0 {4,S}
7    O u0 {2,S} {8,S}
8    O u0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,S}
10   C u0 {9,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.817587,-2.2833,-4.19067,-4.26999,-4.62062,-5.44312,-4.3299],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.217,'kcal/mol','+|-',5.2),
        S298 = (-7.64606,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 473,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_9R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {5,S}
2    C u0 r1 {1,S} {3,S} {7,S}
3    C u0 r1 {2,S} {4,D}
4    C u0 r1 {3,D} {6,S}
5    C u0 r1 {1,S}
6    C u0 r1 {4,S}
7    O u0 r0 {2,S} {8,S}
8    O u0 r0 {7,S} {9,[S,D,T,B,Q]}
9    C ux r1 {8,[S,D,T,B,Q]} {10,S}
10   C u0 {9,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.187226,-3.06573,-4.93636,-4.9143,-4.92406,-5.66849,-4.49134],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.285,'kcal/mol','+|-',5.2),
        S298 = (-7.2297,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCC=CC1OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 474,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_N-9R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {5,S}
2    C u0 r1 {1,S} {3,S} {7,S}
3    C u0 r1 {2,S} {4,D}
4    C u0 r1 {3,D} {6,S}
5    C u0 r1 {1,S}
6    C u0 r1 {4,S}
7    O u0 r0 {2,S} {8,S}
8    O u0 r0 {7,S} {9,[S,D,T,B,Q]}
9    C ux r0 {8,[S,D,T,B,Q]} {10,S}
10   C u0 {9,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
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
    index = 475,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_N-Sp-6R!H-4R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D}
4   C   ux r1 {3,D} {6,[B,D,T,Q]}
5   C   ux r1 {1,[S,D,T,B,Q]}
6   C   u0 r1 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.06966,0.484729,-0.283344,-0.911906,-1.85334,-2.98236,-4.39956],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (127.379,'kcal/mol','+|-',5.2),
        S298 = (4.00495,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=CC[CH]CCC=1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 476,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_2R!H->O",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.362168,-0.512784,-0.940595,-1.52611,-2.47396,-3.21527,-4.41088],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (92.5227,'kcal/mol','+|-',3.8633),
        S298 = (-0.143991,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 477,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_2R!H->O_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,D}
4   C ux r1 {3,D} {5,S}
5   C u0 r1 {4,S}
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
    index = 478,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_2R!H->O_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S}
2   O                      ux r1 {1,S} {3,[S,T,Q,B]}
3   C                      ux r1 {2,[S,T,Q,B]} {4,D}
4   C                      ux r1 {3,D} {5,S}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.759716,-0.917434,-1.27693,-1.77465,-2.64427,-3.33651,-4.4757],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (91.1568,'kcal/mol','+|-',2.4),
        S298 = (-0.100316,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1OC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 479,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.513547,-1.96198,-3.60664,-3.87975,-4.03852,-4.42376,-4.81962],'cal/mol/K','+|-',[3,3,3.70098,3.64213,3.07002,3,4.87419]),
        H298 = (98.5426,'kcal/mol','+|-',5.2),
        S298 = (-1.17642,'cal/mol/K','+|-',7.00778),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 480,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
5   O   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.791379,-2.29089,-4.22888,-4.44891,-4.54584,-4.97124,-5.13491],'cal/mol/K','+|-',[3,3,3.65021,3.71597,3.00293,3,5.64697]),
        H298 = (99.483,'kcal/mol','+|-',5.2),
        S298 = (-1.99867,'cal/mol/K','+|-',7.7006),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 481,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 {2,S} {4,D}
4   R!H u0 {3,D}
5   O   ux {2,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]} {7,S}
7   C   u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.664817,-1.73391,-3.79634,-4.54095,-4.85387,-4.8627,-7.90026],'cal/mol/K','+|-',[4.34149,6.85335,8.83277,9.29542,7.55132,5.85545,11.4009]),
        H298 = (101.422,'kcal/mol','+|-',5.2),
        S298 = (2.15655,'cal/mol/K','+|-',7.29702),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 482,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 r1 {2,S} {4,D}
4   R!H u0 {3,D}
5   O   ux {2,[S,D,T,B,Q]}
6   R!H ux r1 {1,[S,D,T,B,Q]} {7,S}
7   C   u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.19977,0.689111,-0.673481,-1.25452,-2.18408,-2.79249,-3.86942],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.7303,'kcal/mol','+|-',5.2),
        S298 = (-0.423337,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC1[CH]C(O)C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 483,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_N-3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 r0 {2,S} {4,D}
4   R!H u0 {3,D}
5   O   ux {2,[S,D,T,B,Q]}
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
    index = 484,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {2,S} {4,D}
4   C u0 {3,D}
5   O u0 {2,S} {6,S}
6   O u0 {5,S} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.891466,-2.68608,-4.64773,-4.57203,-4.45376,-5.06781,-4.14948],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.0224,'kcal/mol','+|-',5.2),
        S298 = (-3.03721,'cal/mol/K','+|-',7.22367),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 485,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Int-8R!H-1C_Int-8R!H-4R!H_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {2,S} {4,D}
4   C u0 {3,D}
5   O u0 {2,S} {6,S}
6   O u0 {5,S} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   C u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.771222,-2.84765,-4.80123,-4.6608,-4.50612,-5.09108,-4.09804],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.5257,'kcal/mol','+|-',5.2),
        S298 = (-1.58133,'cal/mol/K','+|-',5.23468),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 486,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Int-8R!H-1C_Int-8R!H-4R!H_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r1 {2,S}
2    C u0 {1,S} {3,S} {5,S}
3    C u0 {2,S} {4,D}
4    C u0 {3,D}
5    O u0 {2,S} {6,S}
6    O u0 {5,S} {7,[S,D,T,B,Q]}
7    C ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,S}
10   C u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.880622,-2.92576,-5.06387,-4.96997,-4.68671,-5.2526,-4.44306],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.364,'kcal/mol','+|-',5.2),
        S298 = (-0.635021,'cal/mol/K','+|-',5.77163),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 487,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Int-8R!H-1C_Int-8R!H-4R!H_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_Sp-10R!H-9R!H_Ext-10R!H-R_Ext-7R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S}
2    C   u0 r1 {1,S} {3,S} {5,S}
3    C   u0 r1 {2,S} {4,D}
4    C   u0 r1 {3,D}
5    O   u0 {2,S} {6,S}
6    O   u0 r0 {5,S} {7,[S,D,T,B,Q]}
7    C   ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]} {12,[S,D,T,B,Q]}
8    C   ux r1 {7,[S,D,T,B,Q]} {9,S}
9    C   u0 r1 {8,S} {10,S}
10   C   u0 r1 {9,S} {11,[S,D,T,B,Q]}
11   C   u0 r1 {10,[S,D,T,B,Q]}
12   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.793867,-3.30545,-5.72073,-5.74573,-5.37452,-5.78356,-5.20753],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.6021,'kcal/mol','+|-',5.2),
        S298 = (1.40556,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC1OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 488,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Int-8R!H-1C_Int-8R!H-4R!H_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_N-Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r1 {2,S}
2    C u0 r1 {1,S} {3,S} {5,S}
3    C u0 r1 {2,S} {4,D}
4    C u0 r1 {3,D}
5    O u0 {2,S} {6,S}
6    O u0 r0 {5,S} {7,[S,D,T,B,Q]}
7    C ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C ux r1 {7,[S,D,T,B,Q]} {9,S}
9    C u0 r1 {8,S} {10,[B,D,T,Q]}
10   C u0 r1 {9,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.55242,-2.69142,-4.27593,-4.04246,-4.14495,-4.76804,-3.40801],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.8491,'kcal/mol','+|-',5.2),
        S298 = (-3.47395,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC1OOC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 489,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Int-8R!H-1C_Int-8R!H-4R!H_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,S} {5,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 r1 {3,D}
5   O u0 {2,S} {6,S}
6   O u0 r0 {5,S} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux r1 {7,[S,D,T,B,Q]} {9,D}
9   C u0 r1 {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2522,-2.20138,-4.18722,-4.30572,-4.29667,-4.99801,-4.3038],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.512,'kcal/mol','+|-',5.2),
        S298 = (-7.40486,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC1OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 490,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_N-7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   C ux {3,D}
5   O ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]} {7,S}
7   C u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.717766,-2.0575,-3.82372,-4.1106,-4.42199,-4.88665,-4.34041],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.4656,'kcal/mol','+|-',5.2),
        S298 = (-4.07682,'cal/mol/K','+|-',3.92042),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 491,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_N-7R!H-inRing_Ext-7R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D}
4   C   ux r1 {3,D}
5   O   ux r0 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]} {7,S}
7   C   u0 r0 {6,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
9   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0757365,-2.7595,-4.47521,-4.54955,-4.64124,-4.75427,-3.64995],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.6421,'kcal/mol','+|-',5.2),
        S298 = (-5.4629,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)OOC1[CH]CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 492,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_N-5R!H->O",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C u0 {2,S} {4,D}
4   C u0 {3,D}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.170346,-1.15236,-2.07497,-2.47875,-2.78973,-3.0761,-4.04352],'cal/mol/K','+|-',[5.71988,3.46741,3,3,3,3,3]),
        H298 = (97.2214,'kcal/mol','+|-',5.2),
        S298 = (0.847573,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 493,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_N-5R!H->O_5BrCClFINPSSi-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C u0 r1 {2,S} {4,D}
4   C u0 r1 {3,D}
5   C ux r1 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.62974,0.545058,-1.69907,-2.61643,-3.4628,-3.57644,-4.8047],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.303,'kcal/mol','+|-',5.2),
        S298 = (1.285,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC1C1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 494,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_N-5R!H->O_N-5BrCClFINPSSi-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C u0 r1 {2,S} {4,D}
4   C u0 r1 {3,D}
5   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.41483,-1.90677,-2.24204,-2.41756,-2.49058,-2.85373,-3.70522],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.4171,'kcal/mol','+|-',2.4),
        S298 = (0.653162,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]CC=C1 - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 495,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.154517,-1.0801,-1.98696,-2.66877,-3.46054,-4.06961,-5.94406],'cal/mol/K','+|-',[3,3.69082,4.08295,4.07786,3.65477,3.43423,4.829]),
        H298 = (98.2257,'kcal/mol','+|-',6.3169),
        S298 = (2.26584,'cal/mol/K','+|-',5.81109),
    ),
    shortDesc = """Radical correction fitted to 79 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 496,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.14385,-1.26895,-2.19133,-2.88498,-3.65365,-4.23027,-5.9109],'cal/mol/K','+|-',[3,3.83557,4.2272,4.18106,3.77733,3.66642,4.82325]),
        H298 = (97.4798,'kcal/mol','+|-',6.02319),
        S298 = (2.51146,'cal/mol/K','+|-',5.8046),
    ),
    shortDesc = """Radical correction fitted to 59 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 497,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0596724,-1.00803,-1.88639,-2.58319,-3.44724,-4.08355,-6.08745],'cal/mol/K','+|-',[3,3.33548,3.88701,3.86521,3.16846,3,5.09847]),
        H298 = (97.3616,'kcal/mol','+|-',5.2),
        S298 = (1.88347,'cal/mol/K','+|-',4.86171),
    ),
    shortDesc = """Radical correction fitted to 38 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 498,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0832446,-1.15258,-2.10051,-2.80467,-3.61428,-4.22826,-6.37055],'cal/mol/K','+|-',[3,3.45591,4.01635,4.00268,3.31627,3,5.31727]),
        H298 = (97.7395,'kcal/mol','+|-',5.2),
        S298 = (2.11825,'cal/mol/K','+|-',5.08996),
    ),
    shortDesc = """Radical correction fitted to 34 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 499,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
5   O   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.050663,-0.794362,-1.39527,-1.97445,-2.86857,-3.53408,-4.54073],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.2024,'kcal/mol','+|-',5.2),
        S298 = (1.02698,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 500,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,S}
2   O   u0 {1,S} {3,[S,T,Q,B]}
3   C   u0 {2,[S,T,Q,B]} {4,S}
4   O   u0 {3,S}
5   O   u0 {1,S}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.942431,-1.29281,-1.63196,-1.96939,-2.58369,-3.12003,-4.17749],'cal/mol/K','+|-',[2.96381,3.0146,2.3601,2,2,2,2]),
        H298 = (99.8584,'kcal/mol','+|-',4.0846),
        S298 = (0.257209,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 501,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-1C-R_4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,S}
2   O   u0 r1 {1,S} {3,[S,T,Q,B]}
3   C   u0 r1 {2,[S,T,Q,B]} {4,S}
4   O   u0 r1 {3,S}
5   O   u0 {1,S}
6   R!H u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.105435,-0.226991,-0.797543,-1.46125,-2.53764,-3.3294,-4.47936],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.4143,'kcal/mol','+|-',2.4),
        S298 = (0.405716,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 502,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-1C-R_N-4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,S}
2   O   u0 r1 {1,S} {3,[S,T,Q,B]}
3   C   u0 r1 {2,[S,T,Q,B]} {4,S}
4   O   u0 r0 {3,S}
5   O   u0 {1,S}
6   R!H u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9903,-2.35863,-2.46639,-2.47752,-2.62975,-2.91066,-3.87562],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (101.303,'kcal/mol','+|-',2.4),
        S298 = (0.108702,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OC(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 503,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   O   ux {1,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.837601,-1.15564,-1.75124,-2.33474,-3.20308,-3.82728,-4.73473],'cal/mol/K','+|-',[3,5.67552,5.44604,4.98554,3.83926,3,3]),
        H298 = (98.8637,'kcal/mol','+|-',5.2),
        S298 = (1.0502,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 504,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-4O-R_4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   R!H u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   O   u0 r1 {3,S} {6,S}
5   O   u0 r1 {1,S}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.15489,-5.86525,-6.24291,-6.43654,-6.34832,-6.15599,-5.84693],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.565,'kcal/mol','+|-',5.2),
        S298 = (3.04049,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CO[CH]CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 505,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-4O-R_N-4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux r0 {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   O   ux {1,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.322648,-0.109056,-0.753089,-1.42323,-2.50414,-3.30979,-4.48758],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.6825,'kcal/mol','+|-',2.4),
        S298 = (0.607913,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 506,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-4O-R_N-4O-inRing_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux r0 {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   O ux r1 {1,[S,D,T,B,Q]}
6   O ux r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.660377,0.336324,-0.253115,-0.941602,-2.10336,-3.00002,-4.37114],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.5195,'kcal/mol','+|-',2.4),
        S298 = (0.0992994,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 507,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-4O-R_N-4O-inRing_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux r0 {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   O ux r1 {1,[S,D,T,B,Q]}
6   O ux r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0150817,-0.554435,-1.25306,-1.90486,-2.90491,-3.61956,-4.60401],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.8455,'kcal/mol','+|-',2.4),
        S298 = (1.11653,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 508,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   O   ux {3,[S,T,Q,B]}
5   O   ux {1,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.472755,-0.808818,-1.27349,-1.80388,-2.68441,-3.35885,-4.42326],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.9577,'kcal/mol','+|-',2.4),
        S298 = (1.42322,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1CO[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 509,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]}
5   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.47672,0.08005,-0.555963,-1.25388,-2.40419,-3.24989,-4.45875],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (96.7967,'kcal/mol','+|-',2.4),
        S298 = (0.300861,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 510,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_2R!H->C_4O-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   O u0 r1 {3,S}
5   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.078573,-0.67325,-1.37936,-2.00171,-2.98178,-3.68042,-4.65576],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (96.335,'kcal/mol','+|-',2.4),
        S298 = (-0.272386,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 511,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_2R!H->C_N-4O-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux r0 {3,[S,T,Q,B]}
5   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.754366,0.4567,-0.144263,-0.879959,-2.11539,-3.03462,-4.36024],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.0275,'kcal/mol','+|-',2.4),
        S298 = (0.587484,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 512,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_2R!H->C_N-4O-inRing_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux r0 {3,[S,T,Q,B]}
5   O   ux r1 {1,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12947,0.828101,0.165127,-0.654617,-2.02301,-3.01145,-4.35702],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.0698,'kcal/mol','+|-',2.4),
        S298 = (0.566126,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 513,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   O u0 {3,S}
5   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.295432,-1.15874,-2.04335,-2.70529,-3.53325,-4.10367,-4.84854],'cal/mol/K','+|-',[2,2,2.57307,2.9235,2.7125,2.32268,2]),
        H298 = (99.0455,'kcal/mol','+|-',4.38983),
        S298 = (2.65941,'cal/mol/K','+|-',5.39896),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 514,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_N-2R!H->C_4O-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   O u0 r1 {3,S}
5   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.233198,-1.64869,-2.95307,-3.7389,-4.49227,-4.92486,-5.26854],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (100.598,'kcal/mol','+|-',2.4),
        S298 = (4.56823,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 515,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_N-2R!H->C_N-4O-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   O u0 r0 {3,S}
5   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.357666,-0.6688,-1.13364,-1.67168,-2.57424,-3.28248,-4.42855],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.4934,'kcal/mol','+|-',2.4),
        S298 = (0.750591,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 516,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
5   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.190828,-1.44038,-2.66711,-3.47168,-4.2134,-4.78598,-7.84066],'cal/mol/K','+|-',[3,3.83995,4.51316,4.46627,3.67752,3.29681,5.55235]),
        H298 = (97.2043,'kcal/mol','+|-',5.2),
        S298 = (2.995,'cal/mol/K','+|-',5.84707),
    ),
    shortDesc = """Radical correction fitted to 23 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 517,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
5   C   ux {1,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.284749,-2.01634,-3.61504,-4.51127,-5.01841,-5.48178,-10.0304],'cal/mol/K','+|-',[3.54614,4.76462,4.92902,4.52672,3.51627,3.03398,3]),
        H298 = (95.7525,'kcal/mol','+|-',5.2),
        S298 = (2.37385,'cal/mol/K','+|-',7.08141),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 518,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
5   C   ux r1 {1,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.673855,-1.29742,-3.36943,-4.59099,-5.36097,-5.92985,-10.2191],'cal/mol/K','+|-',[3.77579,6.74283,7.28609,6.60632,4.71751,3.66975,3.04717]),
        H298 = (96.0036,'kcal/mol','+|-',5.2),
        S298 = (0.978015,'cal/mol/K','+|-',9.00043),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 519,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_6R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,S}
2   R!H u0 r1 {1,S} {3,[S,T,Q,B]}
3   C   u0 r1 {2,[S,T,Q,B]} {4,S}
4   O   u0 r1 {3,S}
5   C   u0 r1 {1,S}
6   C   u0 r1 {1,S} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.16317,-2.70683,-3.88613,-4.73577,-6.32898,-8.20642,-8.51952],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.7524,'kcal/mol','+|-',5.2),
        S298 = (5.56464,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC12COOC[C]1COO2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 520,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_N-6R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
5   C   ux r1 {1,[S,D,T,B,Q]}
6   C   ux r0 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.13311,-0.945065,-3.24026,-4.55479,-5.11897,-5.36071,-10.644],'cal/mol/K','+|-',[3.65846,7.57036,8.38677,7.62603,5.30203,3.05256,3]),
        H298 = (96.5664,'kcal/mol','+|-',5.2),
        S298 = (-0.168641,'cal/mol/K','+|-',8.54099),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 521,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_N-6R!H-inRing_Ext-2R!H-R",
    group = 
"""
1 * C     u1 r1 {2,S} {5,S} {6,S}
2   C     u0 {1,S} {3,[S,T,Q,B]} {8,S}
3   C     u0 {2,[S,T,Q,B]} {4,S}
4   O     u0 {3,S}
5   C     u0 r1 {1,S}
6   C     u0 r0 {1,S} {7,[S,D,T,B,Q]}
7   O     ux {6,[S,D,T,B,Q]}
8   [C,O] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.63056,2.10893,0.166519,-1.41563,-2.92456,-4.10942,-10.0135],'cal/mol/K','+|-',[3,4.52984,4.68897,3.49532,3,3,3]),
        H298 = (96.8872,'kcal/mol','+|-',5.2),
        S298 = (-3.46151,'cal/mol/K','+|-',6.22922),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 522,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_N-6R!H-inRing_Ext-2R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C     u1 r1 {2,S} {5,S} {6,S}
2   C     u0 r1 {1,S} {3,[S,T,Q,B]} {8,S}
3   C     u0 r1 {2,[S,T,Q,B]} {4,S}
4   O     u0 r1 {3,S}
5   C     u0 r1 {1,S}
6   C     u0 r0 {1,S} {7,[S,D,T,B,Q]}
7   O     ux {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8   [C,O] u0 r0 {2,S}
9   R!H   ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.20046,3.71047,1.82432,-0.179845,-2.23814,-4.14033,-10.6938],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.1949,'kcal/mol','+|-',5.2),
        S298 = (-5.66387,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(OO)COOC[C]1COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 523,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_N-6R!H-inRing_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux r1 {3,[S,T,Q,B]}
5   C ux r1 {1,[S,D,T,B,Q]}
6   C ux r0 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0935624,-3.4769,-6.00199,-6.93714,-6.65028,-6.01041,-10.0178],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.7847,'kcal/mol','+|-',5.2),
        S298 = (2.21904,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(O)C[C](CO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 524,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_N-6R!H-inRing_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux r1 {3,[S,T,Q,B]}
5   C ux r1 {1,[S,D,T,B,Q]}
6   C ux r0 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.822225,-4.52122,-7.29209,-8.45077,-7.9765,-7.21358,-12.5312],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.7065,'kcal/mol','+|-',5.2),
        S298 = (4.02941,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC[C]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 525,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
5   C   ux r0 {1,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08359,-2.61544,-3.81972,-4.44484,-4.73294,-5.1084,-9.87323],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.5432,'kcal/mol','+|-',5.2),
        S298 = (3.53704,'cal/mol/K','+|-',4.60421),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 526,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]}
5   C ux r0 {1,[S,D,T,B,Q]}
6   C ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.901643,-2.72332,-3.99228,-4.61422,-4.93143,-5.33927,-9.84554],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.3786,'kcal/mol','+|-',5.2),
        S298 = (3.92802,'cal/mol/K','+|-',4.68107),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 527,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,S}
3   C   ux {2,S} {4,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4   O   ux {3,[S,T,Q,B]}
5   C   ux r0 {1,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {7,S}
7   O   u0 r1 {6,S}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.35541,-3.35421,-4.80617,-5.44112,-5.65551,-5.88339,-9.92472],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.4305,'kcal/mol','+|-',5.2),
        S298 = (6.26167,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC(C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 528,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]} {8,[S,D,T,B,Q]}
5   C   ux r0 {1,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux r1 {6,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.49072,-0.851456,-2.64333,-3.81351,-4.69358,-5.43903,-10.6381],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.4693,'kcal/mol','+|-',5.2),
        S298 = (2.43849,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 529,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C_3C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   C u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   O u0 {3,S}
5   C u0 r0 {1,S}
6   C u0 {1,S} {7,S}
7   O u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.80095,-3.68259,-4.9349,-5.50802,-5.69944,-6.03802,-10.2292],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.5691,'kcal/mol','+|-',5.2),
        S298 = (5.10595,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 530,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C_3C-inRing_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {8,[S,D,T,B,Q]}
3   C   u0 r1 {2,S} {4,S}
4   O   u0 r1 {3,S}
5   C   u0 r0 {1,S}
6   C   u0 r1 {1,S} {7,S}
7   O   u0 r1 {6,S}
8   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.48615,-3.68141,-5.18241,-5.984,-6.22278,-6.61093,-10.8357],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.4927,'kcal/mol','+|-',5.2),
        S298 = (5.89114,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 531,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C_N-3C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]}
5   C ux r0 {1,[S,D,T,B,Q]}
6   C ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux r1 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04161,-2.04575,-2.64212,-2.80041,-2.90919,-3.29787,-8.20651],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.8551,'kcal/mol','+|-',5.2),
        S298 = (0.728069,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 532,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   O u0 r1 {1,S} {3,[S,T,Q,B]}
3   C u0 {2,[S,T,Q,B]} {4,S}
4   O u0 {3,S}
5   C u0 r0 {1,S}
6   C u0 r1 {1,S} {7,[S,D,T,B,Q]}
7   O ux r1 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9933,-2.07605,-2.9569,-3.59796,-3.74045,-3.95406,-10.0117],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.366,'kcal/mol','+|-',5.2),
        S298 = (1.58213,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC(OC(C)=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 533,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Int-4O-1C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   O   u0 {1,S} {3,S}
5   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.174256,-0.754689,-1.54189,-2.19816,-3.21139,-3.90615,-4.7771],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.153,'kcal/mol','+|-',2.4),
        S298 = (2.43857,'cal/mol/K','+|-',5.89818),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 534,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Int-4O-1C_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   O u0 r1 {1,S} {3,S}
5   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.369206,-1.03359,-1.72699,-2.31991,-3.22644,-3.84127,-4.62203],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (94.6049,'kcal/mol','+|-',2.4),
        S298 = (0.353247,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 535,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Int-4O-1C_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   O u0 r1 {1,S} {3,S}
5   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.717718,-0.475791,-1.35679,-2.07642,-3.19634,-3.97104,-4.93218],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.7011,'kcal/mol','+|-',2.4),
        S298 = (4.52389,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC[C]1OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 536,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
5   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.342537,-1.65038,-2.85117,-3.62636,-4.36209,-4.88956,-7.63329],'cal/mol/K','+|-',[3,3.1432,3.98135,4.13715,3.72767,3.6247,5.53224]),
        H298 = (98.1723,'kcal/mol','+|-',5.2),
        S298 = (3.82441,'cal/mol/K','+|-',5.6128),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 537,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.438634,-1.78062,-3.04623,-3.83493,-4.44149,-4.80741,-8.35022],'cal/mol/K','+|-',[3,3,3.05065,3.30145,3,3,5.30954]),
        H298 = (98.6011,'kcal/mol','+|-',5.2),
        S298 = (3.4553,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 538,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_Ext-5BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   R!H u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   O   u0 r1 {3,S} {6,S}
5   C   u0 r1 {1,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O   ux r1 {4,S} {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 539,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_Ext-3C-R",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S} {7,S}
4   O u0 {3,S} {6,S}
5   C u0 {1,S} {6,S}
6   O u0 {4,S} {5,S}
7   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.10538,-1.90653,-3.72854,-4.80786,-5.42582,-5.56584,-9.88241],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.0245,'kcal/mol','+|-',5.2),
        S298 = (3.91213,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 540,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_Ext-3C-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   C   u0 r1 {1,S} {3,S} {8,[S,D,T,B,Q]}
3   C   u0 r1 {2,S} {4,S} {7,S}
4   O   u0 r1 {3,S} {6,S}
5   C   u0 r1 {1,S} {6,S}
6   O   u0 r1 {4,S} {5,S}
7   C   u0 r0 {3,S}
8   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.283238,-1.8776,-3.91148,-5.15942,-5.91743,-6.01555,-10.0718],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.7325,'kcal/mol','+|-',5.2),
        S298 = (4.88476,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OOC[CH]C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 541,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.29181,-2.58578,-3.77134,-4.52693,-5.12616,-5.39831,-9.58744],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.9393,'kcal/mol','+|-',5.2),
        S298 = (4.23264,'cal/mol/K','+|-',3.04868),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 542,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_2R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.20247,-2.71105,-4.04423,-4.89415,-5.55128,-5.83242,-9.82925],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.261,'kcal/mol','+|-',5.2),
        S298 = (5.10705,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 543,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_2R!H->C_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux r1 {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   C   ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux r1 {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
8   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.638783,-2.42596,-4.14065,-5.16845,-5.76073,-5.77399,-9.75031],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.3293,'kcal/mol','+|-',5.2),
        S298 = (4.93437,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC1(C)[CH]COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 544,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux r1 {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux r1 {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.321831,-0.159679,-0.836683,-1.46892,-2.44423,-3.20886,-4.42206],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.0193,'kcal/mol','+|-',2.4),
        S298 = (1.87083,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 545,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux r1 {3,[S,T,Q,B]}
5   C ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.56076,-4.55559,-6.30147,-7.06465,-7.91821,-9.09721,-8.80172],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.562,'kcal/mol','+|-',5.2),
        S298 = (11.225,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1COOC12COO2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 546,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux r1 {3,[S,T,Q,B]}
5   C ux r1 {1,[S,D,T,B,Q]}
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
    index = 547,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_N-3C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
5   C   ux r1 {1,[S,D,T,B,Q]}
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
    index = 548,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.790046,0.503076,-0.1103,-0.923933,-2.35625,-3.16061,-4.38182],'cal/mol/K','+|-',[2.47967,2.26081,2,2,2,2,2]),
        H298 = (95.6167,'kcal/mol','+|-',2.4),
        S298 = (-0.0667292,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 549,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_2R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 r1 {2,S} {4,S}
4   O   u0 r1 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.66674,1.30239,0.501323,-0.542287,-2.3278,-3.13963,-4.34463],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.6504,'kcal/mol','+|-',2.4),
        S298 = (0.000532222,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 550,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.633073,-0.824728,-1.15256,-1.64618,-2.58015,-3.31015,-4.4745],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.5076,'kcal/mol','+|-',2.4),
        S298 = (1.08149,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 551,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_N-2R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
4   O   u0 r1 {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.754919,-0.902436,-1.18868,-1.69222,-2.58318,-3.29972,-4.45844],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.7638,'kcal/mol','+|-',2.4),
        S298 = (0.628512,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OCC1O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 552,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.651628,-1.91992,-2.95216,-3.63795,-4.16864,-4.59635,-5.47043],'cal/mol/K','+|-',[3.74282,4.7236,4.75811,4.66233,4.94211,5.27005,4.07559]),
        H298 = (97.8783,'kcal/mol','+|-',10.4118),
        S298 = (4.07826,'cal/mol/K','+|-',6.85742),
    ),
    shortDesc = """Radical correction fitted to 21 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 553,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.153007,-0.323412,-1.14082,-1.74936,-2.28995,-2.79081,-4.64534],'cal/mol/K','+|-',[3,3,3,3,3,3.84855,3.39661]),
        H298 = (95.6021,'kcal/mol','+|-',6.63472),
        S298 = (3.62159,'cal/mol/K','+|-',8.20784),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 554,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.373754,-0.577912,-1.51118,-1.65347,-0.720322,-0.485494,-3.423],'cal/mol/K','+|-',[3,3,3,3,4.79137,5.94743,3]),
        H298 = (93.024,'kcal/mol','+|-',7.45836),
        S298 = (8.15342,'cal/mol/K','+|-',3.07338),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 555,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-1C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,S}
2   R!H u0 r1 {1,S} {3,[S,T,Q,B]}
3   C   u0 r1 {2,[S,T,Q,B]} {4,S} {7,[S,D,T,B,Q]}
4   C   u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   R!H u0 r1 {1,S} {4,[S,D,T,B,Q]}
6   C   u0 r0 {1,S}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0870601,-0.138283,-1.31661,-1.39474,0.198061,0.844151,-2.92597],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.9873,'kcal/mol','+|-',5.2),
        S298 = (9.89257,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC(C)C(C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 556,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-1C-R_2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux r1 {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.307358,-0.800293,-1.94779,-2.73399,-3.43932,-3.89204,-4.88346],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.3407,'kcal/mol','+|-',5.2),
        S298 = (7.58868,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 557,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-1C-R_N-2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux r1 {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34156,-0.79516,-1.26913,-0.831679,1.08029,1.5914,-2.45957],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.744,'kcal/mol','+|-',5.2),
        S298 = (6.97901,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 558,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.713119,-0.0764358,-1.13302,-2.04901,-3.02674,-3.70731,-5.49753],'cal/mol/K','+|-',[3,3,3,3,3,3,4.66759]),
        H298 = (98.3868,'kcal/mol','+|-',6.95543),
        S298 = (4.57378,'cal/mol/K','+|-',6.45302),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 559,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-2R!H-R_6R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C ux r1 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.461802,-0.117155,-0.8488,-1.5991,-2.58516,-3.22296,-4.44684],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.6435,'kcal/mol','+|-',5.2),
        S298 = (2.83345,'cal/mol/K','+|-',5.31841),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 560,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-2R!H-R_6R!H-inRing_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C   ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C   ux r1 {2,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.720635,-0.562883,-1.6158,-2.47208,-3.13205,-3.33914,-4.6103],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.4663,'kcal/mol','+|-',5.2),
        S298 = (5.43699,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 561,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-2R!H-R_N-6R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   R!H ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12151,-0.0102668,-1.59488,-2.7801,-3.7443,-4.49439,-7.2049],'cal/mol/K','+|-',[3,3,3,3,3,3,6.56461]),
        H298 = (94.8089,'kcal/mol','+|-',8.34935),
        S298 = (7.40184,'cal/mol/K','+|-',3.48518),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 562,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-2R!H-R_N-6R!H-inRing_Int-4C-2R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux r1 {2,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   R!H ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.49655,-0.158732,-1.86462,-3.00905,-3.98318,-4.52317,-4.88396],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.7608,'kcal/mol','+|-',5.2),
        S298 = (8.63403,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC12[CH]CC1C2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 563,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux r1 {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   O ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0126232,-0.257902,-0.740828,-1.34464,-2.4001,-3.20684,-4.44002],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (93.9363,'kcal/mol','+|-',2.4),
        S298 = (-0.695173,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 564,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux r1 {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   O ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
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
    index = 565,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]}
5   C ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.48801,-4.32935,-4.92251,-5.25414,-5.50097,-5.51432,-5.40064],'cal/mol/K','+|-',[6.52019,3,3,3,3,4.20655,4.74585]),
        H298 = (98.2507,'kcal/mol','+|-',5.2),
        S298 = (2.62336,'cal/mol/K','+|-',5.23538),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 566,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_6R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {7,[S,D,T,B,Q]}
5   C   u0 {1,S} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.83813,-5.28538,-5.55172,-5.23262,-4.52225,-4.04098,-3.71559],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.0197,'kcal/mol','+|-',5.2),
        S298 = (1.65484,'cal/mol/K','+|-',6.3834),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 567,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_6R!H->C_Ext-4C-R_Ext-6C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {7,[S,D,T,B,Q]}
5   C   u0 {1,S} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {8,S}
7   R!H ux {4,[S,D,T,B,Q]}
8   C   u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.1731,-5.23179,-5.59072,-5.17132,-4.22956,-3.71475,-3.38019],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.8347,'kcal/mol','+|-',5.2),
        S298 = (-0.156868,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 568,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_6R!H->C_Ext-4C-R_Ext-6C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 r1 {3,S} {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
5   C   u0 r1 {1,S} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {8,S}
7   R!H ux {4,[S,D,T,B,Q]}
8   C   u0 r1 {6,S}
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
    index = 569,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_6R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux r1 {3,[S,T,Q,B]}
5   C   ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00132,-3.13399,-4.28363,-5.59559,-7.3585,-8.34464,-8.40987],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.3115,'kcal/mol','+|-',5.2),
        S298 = (4.06577,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 570,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.248128,-3.10681,-4.84399,-5.92346,-6.63889,-7.2293,-7.02312],'cal/mol/K','+|-',[3,5.81172,5.18149,4.15912,3.07506,3,3.37881]),
        H298 = (104.143,'kcal/mol','+|-',12.5328),
        S298 = (5.94924,'cal/mol/K','+|-',3.94064),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 571,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.377487,-3.18184,-4.94086,-6.06465,-6.84633,-7.50027,-6.52312],'cal/mol/K','+|-',[3.12254,6.35154,5.6482,4.48198,3.14663,3,3]),
        H298 = (105.674,'kcal/mol','+|-',10.4743),
        S298 = (6.08897,'cal/mol/K','+|-',4.24008),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 572,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-6BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux r1 {3,[S,T,Q,B]}
5   C   ux r1 {1,[S,D,T,B,Q]} {6,S}
6   O   u0 r1 {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
    index = 573,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {7,S}
2   R!H u0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 {3,S}
5   C   u0 {1,S} {6,S}
6   O   u0 {5,S}
7   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.742479,-3.23179,-5.26085,-6.47357,-7.03997,-7.58966,-6.1876],'cal/mol/K','+|-',[3,3.02717,3,3,3,3,3]),
        H298 = (102.419,'kcal/mol','+|-',5.2),
        S298 = (7.51607,'cal/mol/K','+|-',3.63482),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 574,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-1C-R_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {7,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 r1 {3,S}
5   C u0 r1 {1,S} {6,S}
6   O u0 r1 {5,S}
7   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.138314,-2.19521,-4.08577,-5.30074,-6.0708,-7.10535,-6.43817],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.216,'kcal/mol','+|-',5.2),
        S298 = (5.64968,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 575,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-1C-R_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {7,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 {3,S}
5   C u0 {1,S} {6,S}
6   O u0 {5,S}
7   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04456,-3.75008,-5.84839,-7.05999,-7.52456,-7.83181,-6.06231],'cal/mol/K','+|-',[3.12965,3.44681,3,3,3,3,3]),
        H298 = (102.021,'kcal/mol','+|-',5.2),
        S298 = (8.44927,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 576,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-1C-R_N-2R!H->C_Int-6BrClFINOPSSi-4C_Ext-4C-R_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {7,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 r1 {3,S} {8,D}
5   C u0 r1 {1,S} {6,S}
6   O u0 r1 {5,S}
7   C u0 r0 {1,S}
8   C u0 r0 {4,D}
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
    index = 577,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-1C-R_N-2R!H->C_Int-6BrClFINOPSSi-4C_Ext-4C-R_N-8R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {5,S} {7,S}
2   O                      u0 r1 {1,S} {3,S}
3   C                      u0 r1 {2,S} {4,S}
4   C                      u0 r1 {3,S} {8,D}
5   C                      u0 r1 {1,S} {6,S}
6   O                      u0 r1 {5,S}
7   C                      u0 r0 {1,S}
8   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0619349,-2.53145,-4.99371,-6.60115,-7.40865,-8.05344,-6.8881],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.641,'kcal/mol','+|-',5.2),
        S298 = (9.28017,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COC(=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 578,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux r1 {3,[S,T,Q,B]}
5   C   ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.14318,-0.255309,-2.05637,-3.68833,-5.41475,-6.54316,-6.14038],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.484,'kcal/mol','+|-',5.2),
        S298 = (4.74467,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1[CH]COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 579,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_N-3C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   R!H u0 r1 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 {3,S}
5   C   u0 r1 {1,S} {6,[S,D,T,B,Q]}
6   O   ux r1 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.528026,-2.65665,-4.26276,-5.07629,-5.39422,-5.60349,-10.0231],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.9558,'kcal/mol','+|-',5.2),
        S298 = (5.11087,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC1(C)OOC[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 580,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.184043,-0.55739,-1.42126,-2.07031,-2.926,-3.6249,-6.03584],'cal/mol/K','+|-',[3,3.1195,3.51843,3.6211,3.14524,3,4.98441]),
        H298 = (100.158,'kcal/mol','+|-',5.52716),
        S298 = (1.58597,'cal/mol/K','+|-',5.77596),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 581,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.511241,0.0785103,-0.616764,-1.22872,-2.23657,-3.07238,-4.84124],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.512,'kcal/mol','+|-',5.79809),
        S298 = (0.731135,'cal/mol/K','+|-',4.41305),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 582,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09435,0.696833,-0.095808,-0.750563,-1.85992,-2.83628,-4.80805],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.374,'kcal/mol','+|-',5.2),
        S298 = (0.708692,'cal/mol/K','+|-',5.44321),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 583,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
5   O   ux {2,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12231,0.835749,-0.118205,-0.722823,-1.74767,-2.84135,-5.723],'cal/mol/K','+|-',[3,3,3,3.61287,4.22674,3.63527,3.48311]),
        H298 = (99.8982,'kcal/mol','+|-',5.2),
        S298 = (-0.984194,'cal/mol/K','+|-',8.27226),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 584,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_Ext-1C-R_3O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   ux r1 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   O   ux r1 {2,S} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
5   O   ux {2,[S,D,T,B,Q]}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.991458,0.558539,-0.242131,-1.16709,-2.65983,-3.69964,-4.99437],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.1738,'kcal/mol','+|-',2.4),
        S298 = (0.532105,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1COC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 585,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_Ext-1C-R_N-3O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,[S,T,Q,B]} {5,S}
3   O   u0 r0 {2,[S,T,Q,B]} {4,S}
4   C   u0 {3,S}
5   O   u0 {2,S}
6   R!H ux {1,[S,D,T,B,Q]}
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
    index = 586,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_Ext-1C-R_N-3O-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,[S,T,Q,B]} {5,S}
3   O   u0 r0 {2,[S,T,Q,B]} {4,S}
4   C   u0 r0 {3,S}
5   O   u0 r1 {2,S}
6   R!H ux {1,[S,D,T,B,Q]}
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
    index = 587,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux r1 {3,[S,T,Q,B]}
5   R!H ux r0 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.853737,0.170066,-0.652463,-1.31011,-2.38828,-3.20383,-4.44062],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.915,'kcal/mol','+|-',2.4),
        S298 = (2.43392,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 588,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux r1 {3,[S,T,Q,B]}
5   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17779,0.631063,-0.0628351,-0.701572,-1.79577,-2.66946,-4.07611],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.46,'kcal/mol','+|-',2.2),
        S298 = (1.89253,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1[CH]CO1 - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 589,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux r1 {3,[S,T,Q,B]}
5   O ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19872,1.02697,0.47018,-0.2924,-1.60773,-2.62599,-4.17917],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.071,'kcal/mol','+|-',2.4),
        S298 = (0.997299,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 590,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.559051,-1.1428,-1.74727,-2.23314,-2.99477,-3.58368,-5.36009],'cal/mol/K','+|-',[3,3,3,3,3,3,4.55674]),
        H298 = (97.8126,'kcal/mol','+|-',5.2),
        S298 = (0.00310169,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 591,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-1C-R_2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.605068,-1.05855,-1.58142,-2.05976,-2.80562,-3.40336,-5.80939],'cal/mol/K','+|-',[3,3,3,3.14161,3,3,6.89294]),
        H298 = (98.019,'kcal/mol','+|-',5.2),
        S298 = (0.411536,'cal/mol/K','+|-',3.1524),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 592,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-1C-R_2R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.831839,-1.88669,-2.91495,-3.59769,-4.26208,-4.53931,-9.18373],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.8359,'kcal/mol','+|-',5.2),
        S298 = (1.95475,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 593,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-1C-R_N-2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   O   u0 {1,S} {3,S}
3   O   u0 {2,S} {4,S}
4   C   u0 {3,S}
5   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.492581,-1.26449,-1.98684,-2.48358,-3.26798,-3.84414,-4.71111],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.5622,'kcal/mol','+|-',2.4),
        S298 = (-0.586859,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 594,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux r1 {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.02949,0.556716,-0.171175,-0.934915,-2.04398,-2.85984,-4.17547],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (101.824,'kcal/mol','+|-',2.4),
        S298 = (3.43717,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 595,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux r1 {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.241488,-0.437176,-0.845782,-1.40492,-2.41721,-3.18933,-4.40103],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (96.5783,'kcal/mol','+|-',2.4),
        S298 = (-0.0855491,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 596,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,S}
3   O ux {2,S} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.486315,-1.86021,-3.06948,-3.79455,-4.3385,-4.75688,-8.48331],'cal/mol/K','+|-',[3,3.36627,3.61779,3.62866,3.11376,3,5.02696]),
        H298 = (99.0041,'kcal/mol','+|-',5.2),
        S298 = (3.33733,'cal/mol/K','+|-',6.89245),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 597,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   ux {1,S} {3,S}
3   O   ux {2,S} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36376,-3.04439,-4.29723,-5.00359,-5.35406,-5.59639,-9.95708],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.5705,'kcal/mol','+|-',5.2),
        S298 = (3.65996,'cal/mol/K','+|-',8.97043),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 598,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   ux {1,S} {3,S} {7,[S,D,T,B,Q]}
3   O   ux {2,S} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H u0 {1,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.41477,-3.06717,-4.36346,-5.09127,-5.43643,-5.58488,-9.88243],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.9294,'kcal/mol','+|-',5.2),
        S298 = (4.82077,'cal/mol/K','+|-',5.22016),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 599,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R_Ext-2R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   ux {1,S} {3,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
3   O   ux {2,S} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   C   u0 {1,S}
7   R!H ux {2,[S,D,T,B,Q]}
8   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6701,-3.65134,-4.99798,-5.71865,-6.02153,-6.18174,-10.396],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.1556,'kcal/mol','+|-',5.2),
        S298 = (6.15183,'cal/mol/K','+|-',3.46112),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 600,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R_Ext-2R!H-R_Ext-2R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   ux r1 {1,S} {3,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
3   O   ux r1 {2,S} {4,[S,T,Q,B]}
4   O   ux r1 {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
6   C   u0 r0 {1,S} {9,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
8   R!H ux {2,[S,D,T,B,Q]}
9   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.68086,-3.86569,-5.32273,-6.15461,-6.38059,-6.54604,-10.8326],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.9275,'kcal/mol','+|-',5.2),
        S298 = (4.92814,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)OOC[C]1COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 601,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 {1,S} {3,S}
3   O   u0 {2,S} {4,S}
4   O   u0 {3,S} {5,S}
5   C   u0 {4,S}
6   C   u0 {1,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.98791,-2.86875,-4.23675,-5.10176,-5.59376,-5.9459,-10.3731],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.8774,'kcal/mol','+|-',7.6418),
        S298 = (0.673539,'cal/mol/K','+|-',15.3465),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 602,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S} {4,S}
4   O   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S}
6   C   u0 r0 {1,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.494847,-2.65049,-4.23201,-5.1808,-5.61591,-5.9558,-10.5265],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.1756,'kcal/mol','+|-',5.2),
        S298 = (-4.75226,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(OO)[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 603,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   O   u0 {2,S} {4,S}
4   O   u0 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.253827,-0.989652,-2.47526,-3.2816,-3.90013,-4.38816,-8.84252],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.0433,'kcal/mol','+|-',5.2),
        S298 = (3.11677,'cal/mol/K','+|-',4.14644),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 604,
    label = "RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   O   u0 r1 {2,S} {4,S}
4   O   u0 r1 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.919586,-0.58207,-2.50535,-3.28262,-3.66283,-4.26031,-8.69672],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.7892,'kcal/mol','+|-',5.2),
        S298 = (1.65079,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)[CH]C(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 605,
    label = "RJ1_1R->C_N-1C-inRing",
    group = 
"""
1 * C u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.106946,-0.908723,-1.58201,-2.05376,-2.66202,-3.16314,-4.15937],'cal/mol/K','+|-',[3.3365,3.7397,4.07498,4.13402,3.94008,3.70819,3.61789]),
        H298 = (95.4424,'kcal/mol','+|-',20.8707),
        S298 = (0.891633,'cal/mol/K','+|-',10.4705),
    ),
    shortDesc = """Radical correction fitted to 1040 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]C(CC)C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C)(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]CC(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C1OOC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCCC(C=C)CC=C[CH]C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=COC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC=CC#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C(C)O[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C1C=COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C#CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
[CH2]C(O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COO)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC#C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CCC(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C#C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=O)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC=CC(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C[C]=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)COC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)CCC(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCOOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C)C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(C)O[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(O)C(CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(N(CC)O)C[CH]C=C - Radical thermo from pang.py and closed shell thermo from pang.py
[CH]=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN(OCC(C[CH]C=C)C=C)CC - Radical thermo from pang.py and closed shell thermo from pang.py
O=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1OOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C=COC(C)=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](CCOO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)CO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)OCC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
O=[C]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CO)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(CC=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)OC(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=O)C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)C1C=CC=C(C)C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=CO)C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C1C(O)OOC1(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC=CCC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=CC(=O)[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)OOC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C[C]=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)C1C=C(C)C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C[C](C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC#CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=O - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(CC)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C=O)CC(=C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([CH]CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(O)(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(CC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[C]#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(C)(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=COC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1COOC1[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OOC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C#CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C(C)C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[C]=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[C](COO)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC=CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C=O)C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC(O)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)OOC1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC[C](CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COC=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COO)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C([CH]O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC(=C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC(C)=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1([CH]C=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC12COOC2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC(=C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1=CCC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[C]#COC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[C](C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(=O)C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C1OOC(OC(C)=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C(C)C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)CC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([CH]O)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)C#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](CO)C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C(C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)COOCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[C](O)C(=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(=O)OCO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
C[C](O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC(C)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]CCOO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=C([CH]C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[C]=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)CC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC[CH]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)OOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC1([CH]C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)OO - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
O=[C]OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CCC=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C(=C)O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC(=C)C - Radical thermo from pang.py and closed shell thermo from GAV
C=CC#CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C1=CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]C1CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CO[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC(C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](C)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]OCOO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C#C[CH]CCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OC(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)OOC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
O=C([CH]O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CCC#C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COOCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C=C(COOC(C)(C)[C](C)C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(=O)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC(O)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=O)C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C=CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC(C=C)CCC=CC - Radical thermo from pang.py and closed shell thermo from pang.py
CC(C)(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCC(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(OC(C)(C)[C](C)C)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[C](CCOO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CCC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1=CCCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=C(C)C(=C)COC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=O)=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=COC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=COCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(=C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C=O)C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)CC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C[C](C)C(C)(C)CC(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C12COOC1(C)COO2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC#CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C[CH]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=C[C]=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC(N(CC)O)C - Radical thermo from pang.py and closed shell thermo from pang.py
O=[C]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]CCOC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([CH]O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC(C=C)CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]OC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C=C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(CC(=C)C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C=C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[C]#CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)CCC(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C1C=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1=C=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=[C]COC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(CCO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OC(C=C)[CH2])CC - Radical thermo from pang.py and closed shell thermo from pang.py
C#C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COO)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC=CC=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)OCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(OC1=COC=C1C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C(O)O[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CO[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CO)C(=C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
OC[C](O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(OC)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
C=C(C)C(=C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C(=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1(CC=CC)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C(CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCOOC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
C=C[CH]COOC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
O=C(O)O[C](O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC(=C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C1([C]=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](COO)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([CH]CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCC(C)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
O=C[C](O)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)COC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CO[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(ON(CC)CC)C - Radical thermo from pang.py and closed shell thermo from pang.py
C=C(C)[C](C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)C([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC=CCC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C(C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(CO)OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(COO)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)[C](C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC1=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(O)=C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([CH]OCOO)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[CH2]C=C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]COCOO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C[C](O)C(=O)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH3] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(OO)OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C](C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC(OOCC(=C)C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]OC(C)=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(=C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CC(CC=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)COC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=CC)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CCC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOCC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH]=CC(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCC([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)OOCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]COOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
O[C]=CC=CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)C(C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)=CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCOC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
C=[C]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)OOC1CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[C](O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCCO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC([CH2])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1(C)CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C(=O)C=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CCCC1C([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
C#CC1([CH2])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1CC(C)=CCC1C - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1(OC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
OC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)CC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)O[C]=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH]=C(C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(COO)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(O)C(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CCC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C=COC - Radical thermo from johnson_g4.py and closed shell thermo from GAV
[CH2]C=CCC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
O=C[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([CH]O)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
[CH2]C(O)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(C)(COO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)OOC([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C(COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=CCOOC([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
CCN([CH]C)O - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1OOC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)O[CH]C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]OC - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
[CH2]C1=CC=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CN(CC)O - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)OC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[C]#CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(O)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=O)C[C](C=O)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC1(CC=CC)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C(C)O[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]COC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CC=[C]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC=CCC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C[CH]CC(C=C)CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from pang.py
C[C](COO)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([C]=O)OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC(=O)[CH]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]OC)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)CC(=C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(COC(C)=O)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C(C)COOC(C)(C)C(C)(C)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1=C(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO)C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC(C=C)OO - Radical thermo from pang.py and closed shell thermo from GAV
C=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC1=C(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1=C(OC)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]OC)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(C=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[CH]C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC(C=C)CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)[C](O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)C=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(COC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)O[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1OOCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C=C(O)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([CH]C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=CCCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C](O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]OC=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[CH]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([CH]CO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(=C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC(C)=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[C]=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=COC)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C(C)COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=CCCC(C=C)C[CH]C=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)OOC(C)(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C(C)=O)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1C=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[CH2]C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C)(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(C)(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCOOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=C(CO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=O)=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC#CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[CH2]C(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C(C)=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1([CH]O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[C]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)OOC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(CCOO)OO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
[CH2]C1(OC(C)=O)OC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC(=C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(CC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CCC(C)=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C=C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COC([CH]COO)OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC1OC1[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C[CH]C(C)OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)CC=CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C([C]=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(OO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)C - Radical thermo from pang.py and closed shell thermo from pang.py
CCC([CH]O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(COO)CCC(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC(O)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC(CC(=C)C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1C=C(O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]C1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)CC(=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C=O)C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OC[CH]C=C)CC - Radical thermo from pang.py and closed shell thermo from pang.py
C[C](C)C(C)(C)OC1=COC=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1OOC(C)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C=C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([CH]COO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(OC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C[CH]COO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
CC(N(CC)O)C(C=C)[CH2] - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
CC[C]=O - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC1(CC=CC)C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=CC=C=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC(CON(CC)CC)C=C - Radical thermo from pang.py and closed shell thermo from pang.py
C=C[CH]OC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(O)=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=O)[CH]C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOC(OC(C)=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC=C[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)OOC1C=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]CC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C#C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC(C=C)OO - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1(C)CC(OO)C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=C)C - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C1OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)CC1=CCCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C)(OC(=C)C(=C)C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=CC)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=COCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C[CH]CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(=O)CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C(=C)C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(=C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)(C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[CH]=C(O)C#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([C]=O)C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1CC=CC=C1C - Radical thermo from pang.py and closed shell thermo from GAV
O=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCC(=O)O[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
OC=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([C]=O)C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]O)C(=C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C(C)C(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OOC(O)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC=CCC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
CC(=O)O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1=C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOCC(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=COC(O)C1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)C1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=O)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(OO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=CCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(C=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]C1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]C(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC1(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC1(CC=CC)C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(C)(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1CC(C)=CCC1C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCCC=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=[C]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(OC)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
C[C]=CC(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)CC(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](CC=CC)CCC=CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(CO)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[C](C)CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC([CH]OC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC[CH]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOCC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(CC=CC)CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(OC(=C)C1OO1)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(OOC(C)=O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C#CC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(C)(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1=C=CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 606,
    label = "RJ1_N-1R->C",
    group = 
"""
1 * [Cl,O,Si,H,S,N,P,F,I,Br] u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83476,-2.96204,-3.59014,-3.82901,-3.86318,-3.9823,-4.3624],'cal/mol/K','+|-',[4.40897,5.2361,5.61786,5.64941,5.37307,5.10596,4.90302]),
        H298 = (91.5418,'kcal/mol','+|-',26.137),
        S298 = (-0.673757,'cal/mol/K','+|-',10.5077),
    ),
    shortDesc = """Radical correction fitted to 801 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CC(OO)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)CC(=C[O])C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(OO)C(=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCC(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1(C(=O)O)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OC1C=CC(C1)O[O])CC - Radical thermo from pang.py and closed shell thermo from pang.py
[O]C12OC1(O)O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC([O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(CCO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=COC(O[O])C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)(COO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1OCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[H] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1OC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(OO)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CC2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=C(C)O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CCCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COCOO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
CC[N]CC - Radical thermo from pang.py and closed shell thermo from GAV
[O]OC(O)(C=O)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(OO)C(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(OO)COC=C([O])O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1OCOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])C2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C[O])C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=COCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=CC=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CCCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)C(O)COO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1COOC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=C(O)C=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCCCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1C=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[OH] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1CC(C)(O[O])COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(OO)OCO[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[O]C(=CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1(O)OOC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(CC)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[N+](CC)[O-] - Radical thermo from pang.py and closed shell thermo from GAV
C=C(CO[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1OC(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=C[O])C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(OC)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
CC(=O)OC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(CC(C)OO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C=O)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C1(C)OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1OOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CC(=O)C(OO)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC=COC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCO[O] - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([O])C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(=O)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=C(O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C1([O])CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=CC=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(=O)OC[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=C1C=CC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1=COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1(OO)COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=CC)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CCC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCC1=CC(O[O])C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C([O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OC(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C12OC1O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CCC(=O)OOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O)C(=CO)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C1CC(=O)OC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(O)(O)OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OCC=CCO[O])CC - Radical thermo from pang.py and closed shell thermo from pang.py
COOCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C1(O[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OC1O[O] - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
CCCCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC1OC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=C(O)C(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(C)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([O])C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=CC=CC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C=C(C=O)C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C(O)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CO[O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CCC(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(CO)=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1OOC=C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C(=O)O[O])C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]CC1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC1CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1(O)OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])C(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(COC(=O)CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1(COO)COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)COC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC([O])C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(O)=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C=C([O])OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(O)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(=C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CC(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])C(C)(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C)CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)OC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]OCCC(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C(O[O])OC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1=C([O])OC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1C=COCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C=O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CC(C)([O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C(=O)OOC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CCC(=O)OC([O])O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CCCOO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC([O])C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCC(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COCC(C)[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC(=O)OC=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])COC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=CCC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(O[O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(CO)OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=COC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C(O)O[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OOCC(O[O])C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OOC=C=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([O])=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC(C)(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])COOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=COC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C[O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)OC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=C(O)C(=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(C=O)C1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC1(C)COOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(CC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)C=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC1(C)OOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])COOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CCOO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1(C=C[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C(CO[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C)(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1(COO)COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)CO[O] - Radical thermo from pang.py and closed shell thermo from pang.py
CC=C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C=O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(O)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(C=O)CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]C1OOC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CC(O[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1CCC(C)([O])O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C(=O)O[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CCO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCOC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CCO)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC#C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CC)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CCC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CCC(CO)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])C(C)(C)C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]OC1C=CC(=O)C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(OC(C)=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC1([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(COO)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCOCO[O] - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from johnson_g4.py
C=C([O])OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C1CC(=O)OC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([O])C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC([O])=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CCC(C)(O[O])C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(OOC2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=CC(C)O[O] - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(CCCO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(CCO[O])OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=CC=CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(COO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C([O])OCO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
C=C(COO)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C)CC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC([O])C(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C(CO[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OC1OC[O] - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
[O]OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COCCCO[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC1(CO[O])COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])C=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(C=O)CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(=O)CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])=C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CCC(COC(C)=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=CC(=O)C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)CC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C(C[O])CC(C)(C)C(C)(C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(C)OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC1C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C1(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)CC(O[O])C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(C)(C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(CC(=O)OC=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1([O])CC=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CC(C)O[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC#CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1COC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC([O])=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(OO)C(O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OOC=C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CC(=O)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1COC(=O)C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC([O])C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([O])C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=C(O)C(O)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CCOCO1 - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
CC1([O])CCC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(=O)CC[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COOC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)OC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCOC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C([O])C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1CC(C)(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(O[O])C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1CC(C)(CO[O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CC(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=CC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN(CC)[O] - Radical thermo from pang.py and closed shell thermo from pang.py
CCC(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C1OOCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(C=O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=C(CO[O])OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])(CO)C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=C=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(O)=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(OO)COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CCN(OC1C=CC(C1)[O])CC - Radical thermo from pang.py and closed shell thermo from GAV
CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC(=O)C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(O[O])C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1OC1C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1ON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
[O]CCC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CO[O] - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[O]CC1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(O)C(=O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(=O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=COC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CC[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)CC=C([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCC([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)C(CCO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=O)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CCOC1(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C1CC(C)([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC=CC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCOCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=COC([O])=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C(O)=COC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC=C(O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)CC1=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CCCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CCO)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C=C=C(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(=O)C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(CO[O])=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(OO)=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CCC(C=C)OO)O[O] - Radical thermo from pang.py and closed shell thermo from GAV
[O]C1=C(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=COC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C=O)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)C=CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(C=O)C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1(C=O)OC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)C(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
[O]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=CC=CCC1O[O] - Radical thermo from pang.py and closed shell thermo from GAV
[O]OC1C=CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1C=CC(O[O])COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C[O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OC=C1CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C(O)(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OCC(C=C)O[O])CC - Radical thermo from pang.py and closed shell thermo from pang.py
CC(C=O)(O[O])C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC1OC1C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(O[O])=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
[O]OC1C=CCCC1C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CCC(O[O])OCOO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from johnson_g4.py
CC(=O)OC(C=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=O)C=CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)COOC(C)(C)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])COC=O - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC=C(C=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CO[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(OCO[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CCC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C=C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)=CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=C=C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CCO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC#C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)C(C)(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_1R->C
            L4: RJ1_1R->C_1C-inRing
                L5: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H
                    L6: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C
                        L7: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-3C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-3C-R_Ext-5R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-3C-R_Ext-5R!H-R_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-3C-R_Ext-3C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-3C-R_Ext-1C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-4O-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-4O-R_Ext-6R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Ext-1C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_4R!H->O_Ext-5R!H-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_Sp-6R!H-4C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_Sp-6R!H-4C_Sp-6R!H-5R!H
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_Sp-6R!H-4C_Sp-6R!H-5R!H_Ext-1C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_Sp-6R!H-4C_N-Sp-6R!H-5R!H
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C_3C-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C_N-3C-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C_N-3C-inRing_Sp-6R!H=4C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C_N-3C-inRing_Sp-6R!H=4C_Ext-5R!H-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Int-6R!H-4C_N-Sp-6R!H-4C_N-3C-inRing_N-Sp-6R!H=4C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_3C-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C_Int-7R!H-6R!H
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C_Int-7R!H-6R!H_Ext-1C-R
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C_Int-7R!H-6R!H_Ext-4C-R
                                                                    L18: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C_Int-7R!H-6R!H_Ext-4C-R_8R!H->C
                                                                    L18: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_Sp-7R!H-4C_Int-7R!H-6R!H_Ext-4C-R_N-8R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_N-Sp-7R!H-4C
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_Ext-4C-R_N-Sp-7R!H-4C_Ext-6R!H-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_4C-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_5R!H->C_N-4C-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_Sp-6R!H-5R!H_N-3C-inRing_N-5R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_Sp-7R!H=4C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_Sp-7R!H=4C_Ext-6R!H-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_Sp-7R!H=4C_Ext-4C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_Sp-7R!H=4C_Ext-3C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_N-Sp-7R!H=4C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4C-R_N-Sp-7R!H=4C_Ext-1C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4C-R_7R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4C-R_N-7R!H->C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_4C-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_3C-inRing_Ext-4C-R_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-4C-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_N-3C-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_N-3C-inRing_4C-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_5R!H->C_N-3C-inRing_N-4C-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_N-5R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_N-5R!H->C_Ext-4C-R_Ext-6R!H-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_N-5R!H->C_Ext-4C-R_Ext-6R!H-R_6R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_2R!H-inRing_N-5R!H->C_Ext-4C-R_Ext-6R!H-R_N-6R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_3R!H->C_N-4R!H->O_N-2R!H-inRing
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-1C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-1C-R_Ext-6R!H-R_Sp-7R!H-6R!H
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-1C-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C_Ext-5C-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C_Ext-5C-R_Ext-7R!H-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C_6R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C_N-6R!H->C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C_7R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C_N-7R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_6R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_4R!H->O_Ext-4O-R_N-6R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R_Sp-7R!H-4C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R_Sp-7R!H-4C_Ext-1C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R_Sp-7R!H-4C_6O-inRing
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R_Sp-7R!H-4C_N-6O-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-4C-R_N-Sp-7R!H-4C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_6R!H->O_Ext-1C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_N-6R!H->O
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_N-6R!H->O_4C-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_N-6R!H->O_4C-inRing_Ext-4C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_2R!H-inRing_N-4R!H->O_Ext-5C-R_N-6R!H->O_N-4C-inRing
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing_Ext-4R!H-R_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing_4R!H->O
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing_4R!H->O_Ext-4O-R_6R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing_4R!H->O_Ext-4O-R_N-6R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_5R!H->C_N-2R!H-inRing_N-4R!H->O
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C_6R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-4C-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-1C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_N-Sp-6R!H-4C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-4C-R_N-Sp-6R!H-4C_Ext-1C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_2R!H-inRing_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_N-2R!H-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_4R!H->C_N-2R!H-inRing_Ext-5O-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_N-4R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_N-4R!H->C_4O-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R_Ext-5O-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_Ext-2R!H-R_N-3R!H->C_N-5R!H->C_N-4R!H->C_N-4O-inRing
                        L7: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O_Sp-5R!H-3R!H
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O_Sp-5R!H-3R!H_Ext-3R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O_Sp-5R!H-3R!H_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O_Sp-5R!H-3R!H_Ext-5R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_Int-5R!H-4O_N-Sp-5R!H-3R!H
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-1C-R_Ext-4O-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C_Ext-1C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_5R!H->C_N-Sp-5C-3R!H
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-5R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_Sp-7R!H-6R!H
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4O-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_Int-8R!H-5C
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H
                                                                    L18: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing
                                                                        L19: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing_Sp-7R!H-6C
                                                                        L19: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing_N-Sp-7R!H-6C
                                                                    L18: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_N-7R!H-inRing
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_N-Sp-9R!H=8R!H
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R_N-Sp-8R!H-7R!H
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-5C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->N
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H
                                                                    L18: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_8R!H-inRing
                                                                    L18: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_N-8R!H-inRing
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-4C-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_Sp-7R!H=6C
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H
                                                                    L18: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing
                                                                        L19: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H
                                                                            L20: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_Ext-6C-R
                                                                        L19: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                                                    L18: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_N-Sp-8R!H-7R!H
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-3R!H-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_7R!H->N
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R
                                                                    L18: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H
                                                                    L18: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H
                                                                        L19: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_8R!H-inRing
                                                                        L19: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_N-8R!H-inRing
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_6R!H-inRing
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing_6R!H->C
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing_N-6R!H->C
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing_N-6R!H->C_Ext-3R!H-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-3R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Int-6R!H-4C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Ext-6R!H-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Ext-6R!H-R_Ext-8R!H-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Ext-6R!H-R_Ext-8R!H-R_Ext-1C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Ext-6R!H-R_Int-8R!H-1C_Ext-7R!H-R_Sp-9R!H-7R!H
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-4C-R_Ext-6R!H-R_Int-8R!H-1C_Ext-7R!H-R_N-Sp-9R!H-7R!H
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-1C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R_7R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R_7R!H->C_Ext-7C-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H-8R!H
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-6R!H-R_N-7R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H-inRing_Ext-5R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing_Ext-4C-R_Sp-7R!H-4C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing_Ext-4C-R_N-Sp-7R!H-4C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing_Ext-4C-R_N-Sp-7R!H-4C_Ext-5R!H-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H-inRing_Ext-4C-R_N-Sp-7R!H-4C_Ext-6R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-3R!H-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-1C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-4C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1C-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1C-R_Ext-7R!H-R_Ext-8R!H-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-6O-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_N-5R!H-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_7R!H-inRing
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_7R!H-inRing_Int-7R!H-4C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_7R!H->C
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_7R!H->C_Ext-1C-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_N-7R!H->C
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_N-7R!H->C_Ext-3R!H-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C_Ext-3R!H-R
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C_Ext-8R!H-R_Sp-9R!H-8R!H
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_N-7R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-4C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-5R!H-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-7R!H-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-7R!H-R_8R!H->C
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_Sp-9R!H-8C
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_N-Sp-9R!H-8C
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-7R!H-R_N-8R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-4C-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-4C-R_8R!H->C
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1C-R_Ext-4C-R_N-8R!H->C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing_Ext-5R!H-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R_Ext-7R!H-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-5R!H-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_7R!H->O
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_N-7R!H->O
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_7R!H->O
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Sp-11R!H=10R!H
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_N-Sp-11R!H=10R!H
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_N-7R!H->O
                                                                L17: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_N-7R!H->O_Ext-4C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_Sp-2R!H-1C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_3R!H-inRing_N-4R!H->O_N-Sp-2R!H-1C
                        L7: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_2R!H-inRing
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-2R!H-inRing
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_Sp-5R!H-3R!H
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_N-Sp-5R!H-3R!H
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_N-Sp-5R!H-3R!H_5R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_Ext-3R!H-R_N-Sp-5R!H-3R!H_N-5R!H->C
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_3R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_3R!H->C_Ext-4C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_3R!H->C_Ext-4C-R_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_3R!H->C_Ext-4C-R_2R!H-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_3R!H->C_Ext-4C-R_N-2R!H-inRing
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_N-3R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_4R!H->C_N-3R!H->C_Ext-4C-R_Ext-1C-R
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_N-4R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_Sp-4R!H-1C_N-3R!H-inRing_N-4R!H->C_Ext-1C-R
                    L6: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C
                        L7: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_3R!H-inRing
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R_7R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R_N-7R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_N-3R!H-inRing
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R_Sp-6R!H-5C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R_N-Sp-6R!H-5C
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_3R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_3R!H->C_Ext-3C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_N-3R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_N-3R!H->C_Ext-5BrClFINOPSSi-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_3R!H-inRing
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_N-5R!H->C_N-3R!H-inRing
                L5: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
                    L6: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C
                        L7: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_Ext-2R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_Ext-2R!H-R_3O-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_Ext-2R!H-R_N-3O-inRing
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_Ext-3O-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_N-5R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_3R!H->O_Ext-1C-R_Ext-4R!H-R_N-5R!H->C_Ext-3O-R
                        L7: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_4R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_4R!H->O_Ext-3C-R_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_4R!H->O_Ext-3C-R_Ext-1C-R_Ext-2R!H-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_N-4R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_N-4R!H->O_Ext-3C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_N-4R!H->O_Ext-3C-R_Ext-1C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_N-4R!H->O_Ext-1C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-3C-R_N-4R!H->O_Ext-2R!H-R
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1C_N-3R!H->O_Ext-1C-R
                    L6: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C
                        L7: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R_5R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R_N-5R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R_N-5R!H->C_4R!H-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R_N-5R!H->C_N-4R!H-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-4R!H-R_N-5R!H->C_N-4R!H-inRing_Ext-2C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-3R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_Ext-3R!H-R_Ext-3R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_3R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_3R!H->C_4R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_3R!H->C_N-4R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_4R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_4R!H->C_Ext-2C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_N-4R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_N-4R!H->C_Ext-2C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_N-4R!H->C_Ext-2C-R_Ext-5R!H-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_N-4R!H->C_Ext-2C-R_5R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_Ext-1C-R_N-3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_3R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_3R!H->C_Ext-2C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_3R!H->C_Ext-2C-R_Ext-3C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_3R!H->C_Ext-2C-R_4R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_3R!H->C_Ext-2C-R_N-4R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_4R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_4R!H->C_Ext-2C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_4R!H->C_5R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_4R!H->C_N-5R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_N-4R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_4R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_4R!H->C_Ext-2C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_2R!H->C_N-3R!H->C_Ext-2C-R_N-4R!H->C
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_N-2R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_N-2R!H->C_Ext-1C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_N-2R!H->C_Ext-1C-R_4R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Int-3R!H-1C_N-2R!H->C_Ext-1C-R_N-4R!H->C
                        L7: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_2R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_2R!H->C_Ext-2C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C_Ext-5O-R_Ext-7R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C_4R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C_4R!H->C_4C-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C_4R!H->C_N-4C-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_5R!H->O_N-2R!H->C_N-4R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_Ext-4R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_3R!H-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_3R!H-inRing_4R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_3R!H-inRing_4R!H->C_Ext-3R!H-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_3R!H-inRing_4R!H->C_Ext-3R!H-R_Ext-5C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_3R!H-inRing_N-4R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_N-3R!H-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_N-3R!H-inRing_2C-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_2R!H->C_N-3R!H-inRing_N-2C-inRing
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_N-2R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_N-2R!H->C_2O-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_N-2R!H->C_2O-inRing_Ext-6R!H-R_5C-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_N-2R!H->C_2O-inRing_Ext-6R!H-R_N-5C-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-1C-R_N-5R!H->O_N-2R!H->C_N-2O-inRing
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_5R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_5R!H->O_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_5R!H->O_Ext-1C-R_Ext-2R!H-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_Ext-6R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_Ext-6R!H-R_Int-6R!H-4R!H
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_2R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_N-2R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_6R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_N-6R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-5BrCClFINPSSi-R_N-6R!H->C_Int-6O-5BrCClFINPSSi
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-2R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-4R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_2R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-3R!H-R_N-5R!H->O_N-2R!H->C
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-6R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-6R!H-R_Ext-2R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-5R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-5R!H-R_2R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-5R!H-R_N-2R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_7R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_7R!H->C_Ext-2R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H_Ext-4R!H-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H_Ext-11R!H-R_Ext-12R!H-R_Ext-12R!H-R_Ext-11R!H-R_Ext-12R!H-R_Ext-12R!H-R_Ext-11R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_9R!H-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-2R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_N-9R!H-inRing
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-1C-R_Ext-4R!H-R_N-Sp-6R!H-4R!H
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_2R!H->O
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_2R!H->O_Ext-4R!H-R_5R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_2R!H->O_Ext-4R!H-R_N-5R!H->C
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_3R!H-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_N-3R!H-inRing
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Int-8R!H-1C_Int-8R!H-4R!H_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Int-8R!H-1C_Int-8R!H-4R!H_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_Sp-10R!H-9R!H
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Int-8R!H-1C_Int-8R!H-4R!H_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_Sp-10R!H-9R!H_Ext-10R!H-R_Ext-7R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Int-8R!H-1C_Int-8R!H-4R!H_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_N-Sp-10R!H-9R!H
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_7R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Int-8R!H-1C_Int-8R!H-4R!H_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_N-7R!H-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R_Int-6R!H-1C_Int-6R!H-4R!H_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R_N-7R!H-inRing_Ext-7R!H-R_Ext-7R!H-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_N-5R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_N-5R!H->O_5BrCClFINPSSi-inRing
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-2R!H->O_Ext-2C-R_N-5R!H->O_N-5BrCClFINPSSi-inRing
                        L7: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-1C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-1C-R_4O-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-1C-R_N-4O-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-4O-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-4O-R_4O-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-4O-R_N-4O-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-4O-R_N-4O-inRing_2R!H->C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-4O-R_N-4O-inRing_N-2R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_Ext-3C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_2R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_2R!H->C_4O-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_2R!H->C_N-4O-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_2R!H->C_N-4O-inRing_Ext-2C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_N-2R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_N-2R!H->C_4O-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_5R!H->O_N-2R!H->C_N-4O-inRing
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_6R!H-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_N-6R!H-inRing
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_N-6R!H-inRing_Ext-2R!H-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_N-6R!H-inRing_Ext-2R!H-R_Ext-7R!H-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_N-6R!H-inRing_2R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_5BrCClFINPSSi-inRing_N-6R!H-inRing_N-2R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C_Ext-3C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C_Ext-4O-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C_3C-inRing
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C_3C-inRing_Ext-2C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_2R!H->C_N-3C-inRing
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Ext-1C-R_Ext-6R!H-R_N-5BrCClFINPSSi-inRing_N-2R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Int-4O-1C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Int-4O-1C_2R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_Int-4O-1C_N-2R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_Ext-5BrCClFINPSSi-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_Ext-3C-R
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_Ext-3C-R_Ext-2R!H-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_2R!H->C
                                                        L15: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_2R!H->C_Ext-2C-R
                                                            L16: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_2R!H->C_Ext-2C-R_Ext-2C-R
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_Ext-5BrCClFINPSSi-R_Int-6R!H-4O_N-2R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_2R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_3C-inRing_N-2R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_Ext-1C-R_N-5R!H->O_N-3C-inRing
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_2R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_2R!H->C_Ext-2C-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_N-2R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_4R!H->O_N-2R!H->C_Ext-3C-R
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-1C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-1C-R_Ext-3C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-1C-R_2R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-1C-R_N-2R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-2R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-2R!H-R_6R!H-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-2R!H-R_6R!H-inRing_Ext-3C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-2R!H-R_N-6R!H-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_Ext-2R!H-R_N-6R!H-inRing_Int-4C-2R!H
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_2R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Int-5R!H-4C_N-2R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_6R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_6R!H->C_Ext-4C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_6R!H->C_Ext-4C-R_Ext-6C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_6R!H->C_Ext-4C-R_Ext-6C-R_Ext-4C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_6R!H->C_Ext-2R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-6BrClFINOPSSi-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-1C-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-1C-R_2R!H->C
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-1C-R_N-2R!H->C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-1C-R_N-2R!H->C_Int-6BrClFINOPSSi-4C_Ext-4C-R_8R!H->C
                                                    L14: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-1C-R_N-2R!H->C_Int-6BrClFINOPSSi-4C_Ext-4C-R_N-8R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_3C-inRing_Ext-2R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C_N-4R!H->O_Ext-1C-R_Ext-5R!H-R_N-6R!H->C_N-3C-inRing
                            L8: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_Ext-1C-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_Ext-1C-R_3O-inRing
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_Ext-1C-R_N-3O-inRing
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_Ext-1C-R_N-3O-inRing_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_Ext-5R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_5R!H->C
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-2R!H-R_N-5R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-1C-R_2R!H->C
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-1C-R_2R!H->C_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_Ext-1C-R_N-2R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_2R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_4R!H->C_N-2R!H->C
                                L9: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R_Ext-2R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R_Ext-2R!H-R_Ext-2R!H-R
                                                L13: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R_Ext-2R!H-R_Ext-2R!H-R_Ext-6R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R_Ext-6R!H-R
                                            L12: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-4O-R_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R
                                    L10: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-2R!H-R
                                        L11: RJ1_1R->C_1C-inRing_Ext-1C-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_Ext-2R!H-R
            L4: RJ1_1R->C_N-1C-inRing
        L3: RJ1_N-1R->C
"""
)

