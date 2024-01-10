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
        Cpdata = ([-0.66105,-1.70106,-2.3855,-2.76323,-3.15647,-3.48289,-4.29641],'cal/mol/K','+|-',[3.88382,4.37546,4.57644,4.419,3.89623,3.73071,4.0207]),
        H298 = (92.9694,'kcal/mol','+|-',29.6276),
        S298 = (0.623468,'cal/mol/K','+|-',9.85792),
    ),
    shortDesc = """Radical correction fitted to 253 radicals""",
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
        Cpdata = ([-0.66105,-1.70106,-2.3855,-2.76323,-3.15647,-3.48289,-4.29641],'cal/mol/K','+|-',[3.88382,4.37546,4.57644,4.419,3.89623,3.73071,4.0207]),
        H298 = (92.9694,'kcal/mol','+|-',29.6276),
        S298 = (0.623468,'cal/mol/K','+|-',9.85792),
    ),
    shortDesc = """Radical correction fitted to 253 radicals""",
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
        Cpdata = ([-0.546591,-1.4289,-2.01477,-2.29638,-2.59579,-2.83782,-3.6172],'cal/mol/K','+|-',[3.59444,4.3079,4.54906,4.23825,3.45977,3.26528,3.92194]),
        H298 = (86.325,'kcal/mol','+|-',36.138),
        S298 = (0.194416,'cal/mol/K','+|-',10.8083),
    ),
    shortDesc = """Radical correction fitted to 110 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.319973,-1.08783,-1.71359,-2.15176,-2.77545,-3.22761,-4.10617],'cal/mol/K','+|-',[2.71456,2.83275,3.15435,3.17032,3.4271,3.86901,4.70002]),
        H298 = (81.4816,'kcal/mol','+|-',60.9236),
        S298 = (0.826179,'cal/mol/K','+|-',9.48038),
    ),
    shortDesc = """Radical correction fitted to 34 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.754392,-1.52023,-2.11406,-2.50802,-3.02639,-3.42598,-4.30404],'cal/mol/K','+|-',[2.75571,2.82114,2.91092,2.60518,2.26085,2.23545,2.19342]),
        H298 = (84.6907,'kcal/mol','+|-',39.6702),
        S298 = (0.434762,'cal/mol/K','+|-',11.2355),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.453005,-1.28244,-1.95983,-2.40174,-2.98871,-3.41884,-4.34704],'cal/mol/K','+|-',[2.57308,2.60152,2.77556,2.47492,2.19077,2.17116,2.25099]),
        H298 = (88.8709,'kcal/mol','+|-',37.3736),
        S298 = (1.05497,'cal/mol/K','+|-',11.6725),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.567843,-1.42078,-2.09303,-2.5384,-3.14588,-3.58578,-4.50755],'cal/mol/K','+|-',[2.44713,2.44494,2.68284,2.3355,1.91158,1.82112,1.87975]),
        H298 = (89.9856,'kcal/mol','+|-',36.1094),
        S298 = (0.450356,'cal/mol/K','+|-',8.01555),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.527752,-1.37754,-2.05221,-2.49692,-3.11245,-3.56359,-4.42912],'cal/mol/K','+|-',[2.59286,2.50431,2.75231,2.39039,1.99967,1.95032,1.86529]),
        H298 = (85.6217,'kcal/mol','+|-',28.9924),
        S298 = (-0.0854951,'cal/mol/K','+|-',7.17968),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,S}
5   C ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.538041,-1.44182,-2.13754,-2.58682,-3.19526,-3.62191,-4.44788],'cal/mol/K','+|-',[2.8236,2.70096,2.95999,2.56063,2.12224,2.08335,2.02268]),
        H298 = (80.5148,'kcal/mol','+|-',13.3957),
        S298 = (-0.081482,'cal/mol/K','+|-',7.82861),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 9,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.69739,-3.13973,-3.92423,-3.96155,-3.89198,-3.87997,-4.20124],'cal/mol/K','+|-',[0.946361,2.20479,2.58154,2.04761,0.951532,0.710563,1.83343]),
        H298 = (76.8708,'kcal/mol','+|-',19.7678),
        S298 = (1.08854,'cal/mol/K','+|-',10.8429),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 10,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {4,S}
6   R!H u0 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.80247,-3.89977,-5.09751,-4.79888,-4.09892,-4.19989,-3.48476],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.5741,'kcal/mol','+|-',4.17612),
        S298 = (-7.86091,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CC(OOCC(=C)C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 11,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_1R-inRing",
    group = 
"""
1 * R   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.05888,-1.27346,-1.71326,-2.21736,-3.06961,-3.73986,-4.80033],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (61.5115,'kcal/mol','+|-',4.17612),
        S298 = (0.761903,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 12,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing",
    group = 
"""
1 * R   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83075,-3.41628,-4.18364,-4.18827,-4.04584,-3.83501,-4.23058],'cal/mol/K','+|-',[0.916243,1.5099,1.5476,1.31247,0.651113,0.817361,2.10591]),
        H298 = (78.0348,'kcal/mol','+|-',13.295),
        S298 = (3.40757,'cal/mol/K','+|-',7.76746),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 13,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing_1R->C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S} {6,S}
5   C   u0 r1 {4,S}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.25155,-2.41666,-3.2265,-3.31116,-3.69154,-3.93591,-4.53858],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.5117,'kcal/mol','+|-',4.17612),
        S298 = (0.0307923,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=C(C)C(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 14,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing_N-1R->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.02381,-3.74949,-4.50269,-4.48064,-4.16395,-3.80138,-4.12792],'cal/mol/K','+|-',[0.603872,0.868915,1.07218,0.72963,0.548785,0.987406,2.52969]),
        H298 = (75.8759,'kcal/mol','+|-',12.3802),
        S298 = (4.53316,'cal/mol/K','+|-',7.75198),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 15,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing_N-1R->C_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C u0 {3,S} {5,S} {6,S}
5   C u0 r1 {4,S}
6   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.11897,-3.53872,-4.24867,-4.31906,-4.01113,-3.55826,-4.66414],'cal/mol/K','+|-',[0.715564,0.666178,0.866311,0.661929,0.204633,0.728967,2.42853]),
        H298 = (72.5113,'kcal/mol','+|-',5.90354),
        S298 = (5.98724,'cal/mol/K','+|-',8.33319),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 16,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing_N-1R->C_6R!H->C_Ext-2R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,D} {7,[S,D,T,B,Q]}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S} {6,S}
5   C   u0 r1 {4,S}
6   C   u0 {4,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.37196,-3.77424,-4.55496,-4.55309,-4.08348,-3.30053,-5.52276],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (70.4241,'kcal/mol','+|-',4.17612),
        S298 = (8.93347,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1C=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing_N-1R->C_N-6R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S} {6,[S,D,T,B,Q]}
5   C ux r1 {4,S}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83351,-4.17104,-5.01074,-4.80379,-4.46958,-4.28762,-3.05547],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.605,'kcal/mol','+|-',4.17612),
        S298 = (1.625,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=CC2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 18,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   C ux {3,S} {5,S}
5   C ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0652128,-0.725174,-1.36453,-1.91295,-2.69224,-3.25248,-4.31506],'cal/mol/K','+|-',[2.95206,0.955441,1.25523,1.62611,1.67982,1.53733,1.15035]),
        H298 = (80.7545,'kcal/mol','+|-',9.83028),
        S298 = (-0.987431,'cal/mol/K','+|-',5.79781),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 19,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   C ux {3,S} {5,S}
5   C ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.134906,-0.805265,-1.61273,-2.21937,-3.0289,-3.5755,-4.58194],'cal/mol/K','+|-',[3.4829,0.946425,0.605586,1.10365,1.19698,1.12024,0.737599]),
        H298 = (78.6722,'kcal/mol','+|-',7.15352),
        S298 = (-0.634835,'cal/mol/K','+|-',6.84376),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 20,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_1R-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.920994,-1.27723,-1.63084,-1.98616,-2.67906,-3.31806,-4.52466],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (75.2125,'kcal/mol','+|-',1.69706),
        S298 = (0.860492,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CCC=C[CH]1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 21,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_1R-inRing_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S} {6,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.14583,0.0109467,-2.2244,-3.45616,-4.43431,-4.84338,-5.46625],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (73.02,'kcal/mol','+|-',4.17612),
        S298 = (-9.13086,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=C[CH]C=C(CC=CC)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 22,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_1R-inRing_Ext-5C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   R!H u0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4158,-0.172453,-1.77754,-2.57408,-3.04922,-2.98521,-4.1513],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.3024,'kcal/mol','+|-',4.17612),
        S298 = (-0.927364,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1C1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 23,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_1R-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.16573,-0.86571,-1.61183,-2.2335,-3.15453,-3.75489,-4.52438],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (81.4979,'kcal/mol','+|-',1.69706),
        S298 = (1.11053,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 24,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   C ux {3,S} {5,S}
5   C ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.608391,-0.507786,-0.69083,-1.08124,-1.77845,-2.3757,-3.59066],'cal/mol/K','+|-',[0.293844,1.30767,1.99944,2.13581,1.69958,1.09895,0.472938]),
        H298 = (86.706,'kcal/mol','+|-',1.10706),
        S298 = (-1.94448,'cal/mol/K','+|-',1.75341),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 25,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_N-1R-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.756805,-1.16826,-1.7007,-2.15999,-2.63686,-2.93076,-3.82953],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.0342,'kcal/mol','+|-',4.17612),
        S298 = (-2.83008,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 26,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_N-Sp-4C-3R!H",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,D}
4   C ux r1 {3,D} {5,S}
5   C ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.271289,-0.570791,-1.46665,-3.09871,-5.55409,-6.87607,-7.65443],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.8559,'kcal/mol','+|-',4.17612),
        S298 = (4.67569,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=C=C[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 27,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_N-Sp-5C-4C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   C ux {3,S} {5,D}
5   C u0 r1 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.468957,-1.01024,-1.56461,-1.9832,-2.63927,-3.23033,-4.3219],'cal/mol/K','+|-',[0.489604,0.724481,0.642091,0.0313346,0.79363,1.02846,0.676639]),
        H298 = (110.392,'kcal/mol','+|-',51.3891),
        S298 = (-0.108427,'cal/mol/K','+|-',0.37235),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 28,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_N-Sp-5C-4C_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   C ux r1 {3,S} {5,D}
5   C u0 r1 {4,D}
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
    index = 29,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_N-Sp-5C-4C_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   C ux r1 {3,S} {5,D}
5   C u0 r1 {4,D}
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
    index = 30,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_N-4R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S}
4   O u0 {3,S} {5,S}
5   C ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.837028,-1.71111,-2.36707,-2.81694,-3.37038,-3.73484,-5.03413],'cal/mol/K','+|-',[1.59666,3.01409,3.29759,2.90067,1.74953,0.624714,2.50387]),
        H298 = (115.516,'kcal/mol','+|-',51.1095),
        S298 = (4.04821,'cal/mol/K','+|-',14.2484),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 31,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_N-4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S} {6,[S,D,T,B,Q]}
4   O   u0 r1 {3,S} {5,S}
5   C   ux r1 {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
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
    index = 32,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-5C-inRing",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   C ux {3,S} {5,D}
5   C u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09731,0.5852,-0.161653,-0.556789,-0.866855,-1.16506,-2.18026],'cal/mol/K','+|-',[2.98054,1.95942,0.896858,0.482869,0.110571,1.10559,2.94555]),
        H298 = (61.9321,'kcal/mol','+|-',31.6654),
        S298 = (9.21728,'cal/mol/K','+|-',38.985),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 33,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-5C-inRing_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   C ux {3,S} {5,D}
5   C u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.15109,1.27796,0.155434,-0.386068,-0.905948,-1.55594,-3.22167],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (50.7367,'kcal/mol','+|-',4.17612),
        S298 = (-4.56599,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1=C[CH]OC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 34,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-5C-inRing_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   C ux {3,S} {5,D}
5   C u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0435271,-0.10756,-0.47874,-0.727509,-0.827762,-0.774172,-1.13885],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (73.1275,'kcal/mol','+|-',4.17612),
        S298 = (23.0005,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CC1=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 35,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09904,-2.58114,-2.80214,-2.98219,-3.19452,-3.45785,-4.11216],'cal/mol/K','+|-',[1.94293,3.14261,3.52785,3.34916,2.88598,2.86265,2.17595]),
        H298 = (63.7666,'kcal/mol','+|-',22.1096),
        S298 = (-2.33233,'cal/mol/K','+|-',7.92156),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 36,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_1R-inRing",
    group = 
"""
1 * R   u1 r1 {2,S}
2   C   ux r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   O   ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.92091,-5.56259,-6.09112,-6.12172,-5.90744,-6.14934,-6.16425],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (38.4575,'kcal/mol','+|-',4.17612),
        S298 = (4.96767,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=C[CH]OC=1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 37,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing",
    group = 
"""
1 * R   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.76779,-2.03906,-2.20414,-2.41137,-2.70126,-2.96848,-3.73906],'cal/mol/K','+|-',[0.870557,1.3147,1.6292,1.5031,1.27544,1.26382,0.944039]),
        H298 = (66.5615,'kcal/mol','+|-',4.46631),
        S298 = (-3.6596,'cal/mol/K','+|-',3.86418),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 38,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing_1R->C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   u0 r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.92099,-2.15317,-2.01126,-2.1664,-2.8148,-3.13545,-4.03447],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (66.6817,'kcal/mol','+|-',4.17612),
        S298 = (-5.85508,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 39,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing_N-1R->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.73375,-2.0137,-2.24701,-2.4658,-2.67603,-2.93138,-3.67341],'cal/mol/K','+|-',[1.02084,1.56554,1.93191,1.76775,1.51841,1.49528,1.05644]),
        H298 = (66.5466,'kcal/mol','+|-',5.35049),
        S298 = (-3.17171,'cal/mol/K','+|-',3.54157),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 40,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing_N-1R->C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S} {6,[S,D,T,B,Q]}
4   R!H u0 r1 {3,S} {5,S}
5   O   ux r1 {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12607,-2.63572,-3.29797,-3.53999,-3.67747,-3.99023,-4.40596],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (62.4702,'kcal/mol','+|-',4.17612),
        S298 = (-5.54909,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=C(COO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 41,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing_N-1R->C_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.30375,-2.73698,-2.82018,-2.8134,-2.81049,-2.81608,-3.26755],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (65.1977,'kcal/mol','+|-',4.17612),
        S298 = (-3.37687,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 42,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing_N-1R->C_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   O ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
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
    index = 43,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.614687,-0.157514,-0.851982,-1.38525,-2.23553,-2.80081,-3.68045],'cal/mol/K','+|-',[1.41116,1.86459,3.13311,3.89552,5.19794,6.26713,8.03589]),
        H298 = (75.8279,'kcal/mol','+|-',90.9841),
        S298 = (1.66832,'cal/mol/K','+|-',3.49613),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 44,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux r0 {2,D}
4   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.51047,0.264091,-0.191835,-0.644674,-1.37211,-1.89798,-2.64425],'cal/mol/K','+|-',[0.99933,0.935256,2.0204,2.918,4.44846,5.72791,7.89238]),
        H298 = (70.4411,'kcal/mol','+|-',92.6603),
        S298 = (1.42452,'cal/mol/K','+|-',2.72633),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 45,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux r0 {2,D}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.14959,0.227321,0.00312447,-0.312634,-0.810153,-1.13427,-1.51382],'cal/mol/K','+|-',[0.131728,1.30711,2.74539,3.91017,5.89466,7.53878,10.2652]),
        H298 = (51.752,'kcal/mol','+|-',109.226),
        S298 = (0.654455,'cal/mol/K','+|-',2.37927),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 46,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-1R-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   C   ux r1 {1,S} {3,D} {4,S}
3   R!H u0 r0 {2,D}
4   C   u0 r1 {2,S}
5   C   u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.124326,0.940182,1.57394,1.93528,2.5885,3.21647,4.4128],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (-11.2929,'kcal/mol','+|-',1.69706),
        S298 = (-0.0564621,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 47,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-1R-R_N-5R!H->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux r0 {2,D}
4   C   ux {2,[S,D,T,B,Q]}
5   O   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.162222,-0.12911,-0.782285,-1.43659,-2.50948,-3.30965,-4.47713],'cal/mol/K','+|-',[0.175712,0.606683,0.519121,0.510184,0.434592,0.303836,0.031487]),
        H298 = (83.2745,'kcal/mol','+|-',3.53472),
        S298 = (1.00991,'cal/mol/K','+|-',2.87914),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 48,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-1R-R_N-5R!H->C_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux r1 {2,[S,D,T,B,Q]}
5   O ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.224346,0.0853847,-0.598748,-1.25621,-2.35583,-3.20222,-4.466],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (82.0248,'kcal/mol','+|-',1.69706),
        S298 = (-0.00801698,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]OC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 49,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-1R-R_N-5R!H->C_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   C ux r1 {2,[S,D,T,B,Q]}
5   O ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.100099,-0.343605,-0.965822,-1.61697,-2.66313,-3.41707,-4.48827],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (84.5242,'kcal/mol','+|-',1.69706),
        S298 = (2.02784,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]OOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 50,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r0 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.970463,0.247511,-0.603339,-1.28955,-2.36813,-3.13856,-4.24483],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (99.245,'kcal/mol','+|-',1.69706),
        S298 = (2.85796,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 51,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux r0 {2,D}
4   O   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.940365,-1.47503,-2.91494,-3.69956,-4.93372,-5.62215,-6.91856],'cal/mol/K','+|-',[2.33644,1.22879,1.85264,2.56274,3.48515,4.75935,5.26598]),
        H298 = (116.603,'kcal/mol','+|-',11.8931),
        S298 = (2.4302,'cal/mol/K','+|-',5.446),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 52,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux r0 {2,D}
4   O   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.47282,-1.33565,-3.08417,-4.05762,-5.57969,-6.53739,-7.92459],'cal/mol/K','+|-',[1.17657,1.34113,2.11213,2.6028,2.86437,3.7247,4.15998]),
        H298 = (114.178,'kcal/mol','+|-',8.43353),
        S298 = (1.30187,'cal/mol/K','+|-',3.73268),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 53,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux r0 {2,D}
4   O   ux r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.69536,-1.96329,-4.29519,-5.43407,-6.84365,-7.96653,-9.35175],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (112.701,'kcal/mol','+|-',4.17612),
        S298 = (2.90837,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 54,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   O ux r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
6   C ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.805725,-1.41451,-2.35481,-2.84721,-4.02415,-4.43123,-5.53806],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (110.899,'kcal/mol','+|-',4.17612),
        S298 = (-0.745405,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C1[C]=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 55,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
6   C ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.91737,-0.629138,-2.6025,-3.89158,-5.87127,-7.21439,-8.88397],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (118.935,'kcal/mol','+|-',4.17612),
        S298 = (1.74263,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 56,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.646457,-1.5792,-2.14749,-2.36011,-2.51662,-2.66605,-3.40173],'cal/mol/K','+|-',[3.92336,4.8068,5.04309,4.64917,3.48954,2.92952,3.4808]),
        H298 = (88.4221,'kcal/mol','+|-',16.2931),
        S298 = (-0.0839879,'cal/mol/K','+|-',11.3713),
    ),
    shortDesc = """Radical correction fitted to 76 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 57,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.474306,-1.21548,-1.88049,-2.26253,-2.66226,-2.95031,-3.98089],'cal/mol/K','+|-',[3.40098,4.42121,5.16557,5.29833,4.37021,3.35116,3.84542]),
        H298 = (93.6889,'kcal/mol','+|-',16.186),
        S298 = (-0.358862,'cal/mol/K','+|-',6.75735),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 58,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O   ux {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.19238,-2.12816,-2.77813,-3.00758,-3.12228,-3.19737,-3.89226],'cal/mol/K','+|-',[3.49088,4.76867,5.90377,6.25335,5.30441,4.15459,4.60896]),
        H298 = (89.5118,'kcal/mol','+|-',18.0216),
        S298 = (0.0537395,'cal/mol/K','+|-',8.75235),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 59,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C u0 r0 {1,S} {3,D}
3   O ux {2,D}
4   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.214718,-0.707453,-1.62458,-2.15475,-2.60433,-2.97702,-4.29846],'cal/mol/K','+|-',[1.79775,1.11012,0.111629,0.100395,0.0851367,0.35655,2.01235]),
        H298 = (98.4578,'kcal/mol','+|-',7.0241),
        S298 = (0.869286,'cal/mol/K','+|-',0.602504),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 60,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_1R-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux r1 {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.148482,-0.931732,-1.64714,-2.17503,-2.62153,-2.90498,-3.8919],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (97.7538,'kcal/mol','+|-',1.69706),
        S298 = (0.99101,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 61,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O   ux {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5207,-2.45966,-3.04729,-3.20657,-3.24314,-3.24878,-3.79747],'cal/mol/K','+|-',[3.53124,5.10125,6.51409,6.97314,5.94354,4.67026,5.12595]),
        H298 = (87.3519,'kcal/mol','+|-',17.3071),
        S298 = (-0.136555,'cal/mol/K','+|-',9.80942),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 62,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O   ux {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72536,-3.73478,-4.82305,-5.07826,-4.81646,-4.37666,-3.92795],'cal/mol/K','+|-',[4.09428,5.72785,7.73501,8.3294,6.62028,4.85586,7.09254]),
        H298 = (80.6985,'kcal/mol','+|-',14.9282),
        S298 = (0.568486,'cal/mol/K','+|-',11.8819),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 63,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R_4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S} {4,S} {5,S}
2   C ux r0 {1,S} {3,D}
3   O u0 {2,D}
4   O u0 {1,S}
5   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00444,-3.06674,-4.3393,-4.59222,-4.4329,-3.90955,-2.01664],'cal/mol/K','+|-',[6.83676,5.32038,3.98096,3.89397,3.61328,2.6715,0.839797]),
        H298 = (75.157,'kcal/mol','+|-',9.44476),
        S298 = (-2.22066,'cal/mol/K','+|-',13.8945),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 64,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,S}
2   C   ux r0 {1,S} {3,D}
3   O   u0 r0 {2,D}
4   O   u0 {1,S}
5   C   u0 {1,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.44864,-0.379548,-2.32861,-2.62547,-2.60792,-2.56024,-1.59248],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.8889,'kcal/mol','+|-',4.17612),
        S298 = (-9.23843,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 65,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R_N-4R!H->O",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
4   C ux {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.44629,-4.40281,-5.30679,-5.5643,-5.20001,-4.84377,-5.83927],'cal/mol/K','+|-',[0.951248,8.72554,13.6374,14.8177,11.6305,8.36274,10.0619]),
        H298 = (86.24,'kcal/mol','+|-',6.31473),
        S298 = (3.35763,'cal/mol/K','+|-',11.8968),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 66,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R_N-4R!H->O_4C-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
4   C ux r1 {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.92674,-8.80987,-12.1947,-13.0484,-11.0743,-9.06759,-10.9213],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.0723,'kcal/mol','+|-',4.17612),
        S298 = (9.36644,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C=O)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 67,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R_N-4R!H->O_N-4C-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
4   C ux r0 {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.25411,-2.63998,-2.55161,-2.57068,-2.8503,-3.15424,-3.80645],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (85.6071,'kcal/mol','+|-',1.69706),
        S298 = (0.954106,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 68,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_4R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
4   C ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.142443,0.295317,-0.363851,-0.571802,-1.13631,-1.92926,-6.7032],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.4615,'kcal/mol','+|-',4.17612),
        S298 = (-0.916036,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1OC1[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 69,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_N-4R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
4   C ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.55362,-1.5781,-1.65487,-1.71127,-1.97079,-2.30941,-3.25189],'cal/mol/K','+|-',[3.69307,4.00241,4.16197,4.54294,4.74208,4.50539,3.21897]),
        H298 = (94.0683,'kcal/mol','+|-',4.72012),
        S298 = (-0.730241,'cal/mol/K','+|-',10.3592),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 70,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_N-4R!H-inRing_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O   ux {2,D}
4   C   ux r0 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.14446,2.40729,2.37843,2.65948,2.52853,1.9639,-0.0731802],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.7124,'kcal/mol','+|-',4.17612),
        S298 = (-11.2042,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[CH]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 71,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_N-4R!H-inRing_Sp-2R!H-1R",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 r0 {1,S} {3,D}
3   O u0 {2,D}
4   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.31201,-1.8654,-1.80664,-1.85543,-2.08712,-2.45037,-3.54191],'cal/mol/K','+|-',[1.3802,0.197605,0.4993,0.876069,1.41798,1.64361,1.1785]),
        H298 = (92.6324,'kcal/mol','+|-',2.64947),
        S298 = (0.702446,'cal/mol/K','+|-',3.09131),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 72,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_N-4R!H-inRing_Sp-2R!H-1R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   C   u0 r0 {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
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
    index = 73,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_N-4R!H-inRing_N-Sp-2R!H-1R",
    group = 
"""
1 * C u1 r0 {2,D} {4,[S,D,T,B,Q]}
2   C ux r0 {1,D} {3,D}
3   O ux {2,D}
4   C ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97112,-2.77004,-3.05573,-3.25775,-3.60766,-3.82139,-4.11735],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (96.1304,'kcal/mol','+|-',1.69706),
        S298 = (1.45358,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 74,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.659362,0.173862,-0.522761,-1.11215,-1.89228,-2.46372,-3.97444],'cal/mol/K','+|-',[1.7023,2.0893,2.64723,2.95428,2.39441,1.60899,2.90335]),
        H298 = (98.0181,'kcal/mol','+|-',4.54647),
        S298 = (-0.872104,'cal/mol/K','+|-',3.25272),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 75,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.686987,-0.0307198,-0.831336,-1.46079,-2.15349,-2.6055,-4.2452],'cal/mol/K','+|-',[1.9637,2.58055,3.28823,3.68818,3.02571,2.0764,3.74807]),
        H298 = (99.595,'kcal/mol','+|-',1.46771),
        S298 = (-0.251079,'cal/mol/K','+|-',3.64391),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 76,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,D} {4,S}
3   O   ux {2,D}
4   C   u0 {2,S} {5,S}
5   C   ux {4,S} {6,S}
6   R!H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31217,-2.65974,-4.1395,-5.05965,-4.79663,-4.67889,-8.61961],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (102.058,'kcal/mol','+|-',4.17612),
        S298 = (3.23843,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 77,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.953541,0.319817,-0.390247,-0.980945,-1.80107,-2.32905,-3.66195],'cal/mol/K','+|-',[1.06763,1.3998,1.85311,2.24952,2.23042,1.19507,0.0625414]),
        H298 = (99.4594,'kcal/mol','+|-',0.515247),
        S298 = (-0.716347,'cal/mol/K','+|-',2.31563),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 78,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,D} {4,S}
3   O ux {2,D}
4   O u0 {2,S} {5,S}
5   C ux {4,S} {6,S}
6   C u0 {5,S} {7,[S,D,T,B,Q]}
7   O u0 r0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.410555,-0.488306,-1.45389,-2.2756,-3.08852,-3.01618,-3.66348],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (99.7552,'kcal/mol','+|-',1.69706),
        S298 = (0.620539,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 79,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O u0 {2,D}
4   O ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,D}
7   C ux {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.22503,0.723878,0.141574,-0.333616,-1.15734,-1.98548,-3.66118],'cal/mol/K','+|-',[0.714614,0.0225588,0.282924,0.252615,0.0663359,0.153124,0.0883669]),
        H298 = (99.3115,'kcal/mol','+|-',0.0762315),
        S298 = (-1.38479,'cal/mol/K','+|-',0.0271821),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 80,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_N-7R!H->O_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   u0 r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   O   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux r0 {5,[S,D,T,B,Q]} {7,D}
7   C   ux {6,D}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.47769,0.715902,0.0415453,-0.422929,-1.13389,-1.93134,-3.62994],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (99.2845,'kcal/mol','+|-',1.69706),
        S298 = (-1.3944,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OC(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 81,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0322275,0.101593,-0.34033,-0.819458,-1.65969,-2.34317,-3.42372],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (95.2521,'kcal/mol','+|-',1.69706),
        S298 = (-1.84388,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 82,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_N-1R->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C ux r0 {1,S} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.49453,-3.08702,-3.60354,-4.00941,-4.54664,-4.94863,-5.70787],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (109.816,'kcal/mol','+|-',4.17612),
        S298 = (-1.06324,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CCCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 83,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.713292,-1.72041,-2.25115,-2.39799,-2.46007,-2.55569,-3.17687],'cal/mol/K','+|-',[4.13814,4.96997,5.04338,4.44169,3.14027,2.76267,3.26856]),
        H298 = (86.0164,'kcal/mol','+|-',14.153),
        S298 = (0.022728,'cal/mol/K','+|-',12.7804),
    ),
    shortDesc = """Radical correction fitted to 58 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 84,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.270457,-0.983626,-1.50493,-1.79879,-2.18227,-2.50558,-3.27956],'cal/mol/K','+|-',[3.34747,2.97829,2.77525,2.53052,2.19879,2.26378,2.64654]),
        H298 = (85.8862,'kcal/mol','+|-',11.9679),
        S298 = (-0.75505,'cal/mol/K','+|-',10.9223),
    ),
    shortDesc = """Radical correction fitted to 44 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 85,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.622828,-1.42888,-1.93968,-2.17674,-2.41484,-2.58128,-3.12352],'cal/mol/K','+|-',[3.20052,2.82191,2.74067,2.64616,2.52334,2.66064,3.02787]),
        H298 = (84.4033,'kcal/mol','+|-',15.1736),
        S298 = (0.0555571,'cal/mol/K','+|-',13.1621),
    ),
    shortDesc = """Radical correction fitted to 28 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 86,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.689159,-1.50077,-2.01274,-2.24575,-2.47812,-2.64329,-3.1834],'cal/mol/K','+|-',[3.12226,2.69717,2.60409,2.52164,2.41641,2.56853,2.96421]),
        H298 = (84.3418,'kcal/mol','+|-',15.2498),
        S298 = (-0.535604,'cal/mol/K','+|-',10.8189),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 87,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.93822,-1.86188,-2.31459,-2.51102,-2.64492,-2.67354,-2.85217],'cal/mol/K','+|-',[3.37415,3.53893,3.58604,3.24373,2.68138,2.79361,3.8392]),
        H298 = (85.2626,'kcal/mol','+|-',23.1903),
        S298 = (0.791641,'cal/mol/K','+|-',13.4113),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 88,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   R!H u0 r0 {1,[S,D,T,B,Q]}
5   R!H u0 r0 {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.38006,-6.27173,-6.79279,-6.12841,-4.57571,-3.8328,-3.61345],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.22,'kcal/mol','+|-',4.17612),
        S298 = (2.13303,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 89,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.23908,-2.95289,-2.66412,-2.35152,-1.61387,-0.74646,0.779456],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (67.8653,'kcal/mol','+|-',1.69706),
        S298 = (-6.58566,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC(O)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 90,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {5,[S,D,T,B,Q]}
4   R!H u0 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H u0 {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.370415,-0.47783,-1.0655,-1.48191,-2.0978,-2.48328,-3.07354],'cal/mol/K','+|-',[2.75713,1.85747,1.38291,1.31364,1.37355,1.69677,2.45025]),
        H298 = (84.7748,'kcal/mol','+|-',5.90376),
        S298 = (2.56966,'cal/mol/K','+|-',19.1904),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 91,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   R!H u0 r0 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H u0 r0 {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.5796,0.889129,-0.511459,-1.09954,-1.97967,-2.61519,-3.61255],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.0662,'kcal/mol','+|-',4.17612),
        S298 = (-6.14618,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(O)[CH]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 92,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-3C",
    group = 
"""
1 * C   u1 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {5,S}
4   R!H u0 {1,S} {6,S}
5   C   u0 {3,S}
6   C   u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.114559,-0.356075,-0.65986,-1.02792,-1.71068,-2.14357,-2.7072],'cal/mol/K','+|-',[0.656746,0.995697,1.06192,0.969663,0.761418,0.181306,2.20229]),
        H298 = (81.6074,'kcal/mol','+|-',2.7626),
        S298 = (-3.43047,'cal/mol/K','+|-',1.88772),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 93,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-3C_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {5,S}
4   C u0 r0 {1,S} {6,S}
5   C u0 r0 {3,S}
6   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.346754,-0.708107,-1.0353,-1.37075,-1.97988,-2.20767,-1.92857],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.5841,'kcal/mol','+|-',4.17612),
        S298 = (-2.76306,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC=C[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 94,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-3C_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {5,S}
4   O u0 r0 {1,S} {6,S}
5   C u0 r0 {3,S}
6   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.117635,-0.00404238,-0.284416,-0.685096,-1.44147,-2.07947,-3.48583],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.6307,'kcal/mol','+|-',4.17612),
        S298 = (-4.09788,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 95,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H-3C",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {5,D}
4   C   u0 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H u0 {3,D}
6   C   u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0163474,-0.937965,-1.45559,-1.85058,-2.35276,-2.63972,-3.12887],'cal/mol/K','+|-',[3.11188,1.95089,1.59027,1.547,2.14021,2.99395,3.96228]),
        H298 = (84.9227,'kcal/mol','+|-',2.29086),
        S298 = (8.48855,'cal/mol/K','+|-',22.5607),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 96,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H-3C_Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D} {5,D}
4   C   u0 r0 {1,S} {6,[S,D,T,B,Q]}
5   R!H u0 r0 {3,D}
6   C   u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.58808,0.0473857,-0.652384,-1.06922,-1.27179,-1.12755,-1.12762],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.313,'kcal/mol','+|-',4.17612),
        S298 = (19.8834,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C[CH]CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 97,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H-3C_N-Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D} {5,D}
4   C   u0 r0 {1,D} {6,[S,D,T,B,Q]}
5   R!H u0 r0 {3,D}
6   C   u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.612347,-1.3321,-1.77688,-2.16312,-2.78515,-3.24459,-3.92938],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (84.6931,'kcal/mol','+|-',1.69706),
        S298 = (3.9306,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 98,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Sp-4R!H-1C",
    group = 
"""
1 * C   u1 {2,S} {4,S}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.757146,-1.98301,-2.60612,-2.84859,-2.92875,-2.97612,-3.58133],'cal/mol/K','+|-',[2.00783,3.3444,4.66655,4.83317,4.37028,3.811,3.21188]),
        H298 = (85.7745,'kcal/mol','+|-',7.82262),
        S298 = (0.235196,'cal/mol/K','+|-',7.8237),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 99,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Sp-4R!H-1C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r0 {1,S}
5   R!H u0 r0 {3,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46989,-4.36154,-5.96549,-6.32605,-6.01267,-5.49993,-5.48944],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.5357,'kcal/mol','+|-',4.17612),
        S298 = (4.10321,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 100,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Sp-4R!H-1C_5R!H->C",
    group = 
"""
1 * C u1 {2,S} {4,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0357,-1.44797,-1.67649,-1.90865,-2.28788,-2.66809,-3.53716],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (85.4857,'kcal/mol','+|-',1.69706),
        S298 = (0.700151,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 101,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Sp-4R!H-1C_N-5R!H->C",
    group = 
"""
1 * C u1 {2,S} {4,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.651975,-0.942054,-1.57081,-1.72095,-1.44701,-1.22237,-1.78364],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.7617,'kcal/mol','+|-',4.17612),
        S298 = (-4.7952,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]C=CON(CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 102,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_N-Sp-4R!H-1C",
    group = 
"""
1 * C   u1 {2,S} {4,D}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,D}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.38901,-2.38743,-2.89665,-3.29162,-3.81529,-4.08697,-4.29126],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (100.319,'kcal/mol','+|-',1.69706),
        S298 = (4.01114,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=[C]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 103,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O",
    group = 
"""
1 * C u1 {2,S} {4,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D}
4   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.711919,-1.08893,-1.46536,-1.65452,-1.92409,-2.22947,-3.16892],'cal/mol/K','+|-',[3.00698,1.77892,1.52072,1.93193,2.39449,2.70888,2.50791]),
        H298 = (82.4189,'kcal/mol','+|-',7.7238),
        S298 = (-1.69096,'cal/mol/K','+|-',7.13614),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 104,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.845926,-1.24079,-1.54949,-1.70502,-1.88782,-2.0927,-3.00559],'cal/mol/K','+|-',[3.25242,1.96129,1.7705,2.27994,2.82161,3.1546,2.89743]),
        H298 = (83.9104,'kcal/mol','+|-',7.6149),
        S298 = (-1.82378,'cal/mol/K','+|-',8.38784),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 105,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C",
    group = 
"""
1 * C u1 {2,S} {4,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {1,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.976461,-1.37399,-1.69045,-1.86409,-2.04935,-2.23615,-3.07581],'cal/mol/K','+|-',[3.36472,1.88068,1.61565,2.1709,2.80255,3.22833,3.06862]),
        H298 = (83.6394,'kcal/mol','+|-',7.55602),
        S298 = (-1.71761,'cal/mol/K','+|-',8.96799),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 106,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-4O-R",
    group = 
"""
1 * C u1 {2,S} {4,[S,D,T,B,Q]}
2   C u0 r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C u0 {2,D}
4   O u0 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
6   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.971392,-1.18321,-1.36565,-1.49345,-1.76986,-2.0462,-2.87041],'cal/mol/K','+|-',[1.28617,1.92727,2.20678,2.0987,1.66645,1.58935,2.69599]),
        H298 = (81.7687,'kcal/mol','+|-',2.81843),
        S298 = (-2.22945,'cal/mol/K','+|-',3.91059),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 107,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   u0 {2,D}
4   O   u0 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {7,D}
6   C   ux {4,[S,D,T,B,Q]}
7   R!H u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.86246,-1.10804,-1.32184,-1.43408,-1.65954,-1.8779,-2.54219],'cal/mol/K','+|-',[1.73887,2.70058,3.11348,2.95373,2.29391,2.09102,3.45708]),
        H298 = (82.0924,'kcal/mol','+|-',3.65684),
        S298 = (-2.42637,'cal/mol/K','+|-',5.44562),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 108,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_7R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C u0 r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C u0 r0 {2,D}
4   O u0 r0 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]} {7,D}
6   C ux {4,[S,D,T,B,Q]}
7   C u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.47724,-2.06284,-2.42262,-2.47838,-2.47056,-2.61719,-3.76446],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.3853,'kcal/mol','+|-',4.17612),
        S298 = (-0.501049,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(=C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 109,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C                      u0 r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C                      u0 r0 {2,D}
4   O                      u0 r0 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C                      ux {2,[S,D,T,B,Q]} {7,D}
6   C                      ux {4,[S,D,T,B,Q]}
7   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.247678,-0.153241,-0.221061,-0.389778,-0.848517,-1.13862,-1.31993],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.7995,'kcal/mol','+|-',4.17612),
        S298 = (-4.35168,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([CH]OC)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 110,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34791,-1.73073,-2.07781,-2.32219,-2.54732,-2.82696,-3.68107],'cal/mol/K','+|-',[4.95965,1.9045,0.631159,2.32931,3.68399,3.97431,2.95846]),
        H298 = (84.2921,'kcal/mol','+|-',9.49759),
        S298 = (0.520922,'cal/mol/K','+|-',5.26815),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 111,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Sp-4O-1C",
    group = 
"""
1 * C   u1 {2,S} {4,S}
2   C   ux r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   O   ux {1,S}
5   C   ux {2,[S,D,T,B,Q]} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.10141,-2.40407,-1.85466,-1.49866,-1.24484,-1.42183,-2.63509],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (80.9341,'kcal/mol','+|-',1.69706),
        S298 = (-1.34165,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(=C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 112,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-Sp-4O-1C",
    group = 
"""
1 * C   u1 {2,S} {4,D}
2   C   ux r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D}
4   O   ux {1,D}
5   C   ux {2,[S,D,T,B,Q]} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.405586,-1.05738,-2.30096,-3.14573,-3.84981,-4.23209,-4.72704],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (87.65,'kcal/mol','+|-',1.69706),
        S298 = (2.38349,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([C]=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 113,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   O   u0 r0 {1,[S,D,T,B,Q]}
5   C   u0 r0 {2,S} {6,[S,T,Q,B]}
6   R!H u0 r0 {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.865598,-0.16263,-0.728081,-0.685514,-0.397954,0.148046,-0.665762],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.3473,'kcal/mol','+|-',4.17612),
        S298 = (-11.3748,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([CH]O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 114,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 {2,S} {4,[S,D,T,B,Q]}
2   C                      ux r0 {1,S} {3,D} {5,S}
3   C                      ux {2,D}
4   O                      ux {1,[S,D,T,B,Q]}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.328881,-0.0420224,-0.280776,-0.273391,-0.434048,-0.801631,-2.37361],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.276,'kcal/mol','+|-',4.17612),
        S298 = (-2.7793,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(O)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 115,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D}
4   O   ux {1,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.33186,-0.116086,-1.29447,-1.72823,-2.45173,-2.95408,-3.61031],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (79.4276,'kcal/mol','+|-',4.17612),
        S298 = (-2.71059,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 116,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O",
    group = 
"""
1 * C u1 {2,S} {4,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D}
4   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.23503,-1.44287,-2.23856,-2.59296,-2.94249,-3.15051,-3.76602],'cal/mol/K','+|-',[3.2445,2.11415,1.41016,1.33838,1.67328,1.96653,1.65112]),
        H298 = (85.4999,'kcal/mol','+|-',2.09329),
        S298 = (-1.23219,'cal/mol/K','+|-',11.0173),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 117,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   C   u0 r0 {1,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.59733,-2.82914,-3.617,-3.85722,-4.06732,-4.17394,-4.93354],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.3496,'kcal/mol','+|-',4.17612),
        S298 = (-0.551823,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[C](C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 118,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C",
    group = 
"""
1 * C u1 {2,S} {4,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.441991,-1.07775,-2.05236,-2.45035,-2.77976,-2.9527,-3.56638],'cal/mol/K','+|-',[3.27288,2.21541,1.26343,1.24848,1.87687,2.32391,1.80139]),
        H298 = (84.9427,'kcal/mol','+|-',1.08061),
        S298 = (-2.29999,'cal/mol/K','+|-',13.5747),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 119,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {1,[S,D,T,B,Q]} {5,S}
5   C   ux {4,S}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0911134,-1.61903,-2.25148,-2.19162,-2.05635,-2.197,-3.24622],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.7866,'kcal/mol','+|-',4.17612),
        S298 = (-3.58835,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[CH]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 120,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * C u1 {2,S} {4,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D}
4   C ux {1,[S,D,T,B,Q]} {5,S}
5   C ux {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O u0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.457149,-1.50492,-2.24127,-2.82941,-3.64266,-4.09312,-4.39242],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (84.8224,'kcal/mol','+|-',1.69706),
        S298 = (4.49341,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OCC(C[CH]C=C)C=C)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 121,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * C u1 {2,S} {4,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D}
4   C u0 {1,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]} {6,S}
6   C u0 {5,S} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.30823,-0.541344,-1.82855,-2.22072,-2.30181,-2.25425,-2.98473],'cal/mol/K','+|-',[4.19245,2.97601,1.83602,1.63343,1.59086,1.64978,1.53006]),
        H298 = (84.9044,'kcal/mol','+|-',1.3788),
        S298 = (-7.53171,'cal/mol/K','+|-',7.43627),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 122,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R",
    group = 
"""
1 * C u1 {2,S} {4,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D}
4   C u0 {1,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]} {6,S}
6   C u0 {5,S} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   C u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.09855,0.0237156,-1.53957,-1.92049,-1.89473,-1.77866,-2.69588],'cal/mol/K','+|-',[4.49029,3.17021,2.17661,1.78127,1.04142,0.123619,1.63696]),
        H298 = (84.724,'kcal/mol','+|-',1.73812),
        S298 = (-9.43181,'cal/mol/K','+|-',4.89357),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 123,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R_Ext-5C-R",
    group = 
"""
1  * C   u1 r0 {2,S} {4,S}
2    C   u0 r0 {1,S} {3,D}
3    C   u0 r0 {2,D}
4    C   u0 r0 {1,S} {5,[S,D,T,B,Q]}
5    C   u0 r0 {4,[S,D,T,B,Q]} {6,S} {10,[S,D,T,B,Q]}
6    C   u0 r0 {5,S} {7,[S,D,T,B,Q]}
7    C   ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C   ux {7,[S,D,T,B,Q]} {9,S}
9    C   u0 r1 {8,S}
10   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.68611,1.14456,-0.77002,-1.29072,-1.52653,-1.82237,-3.27463],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.3385,'kcal/mol','+|-',4.17612),
        S298 = (-7.70168,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]CC(C=C)CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 124,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,S}
2   C                      u0 r0 {1,S} {3,D}
3   C                      u0 r0 {2,D}
4   C                      u0 r0 {1,S} {5,S}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.45036,-1.83767,-2.17131,-2.45805,-2.91564,-3.25545,-3.81809],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (86.615,'kcal/mol','+|-',1.69706),
        S298 = (1.27195,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 125,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_N-Sp-2R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,D} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,D} {3,D}
3   C   ux {2,D}
4   R!H u0 r0 {1,[S,D,T,B,Q]}
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
    index = 126,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.178439,-0.395929,-0.890875,-1.20023,-1.68411,-2.17869,-3.28857],'cal/mol/K','+|-',[3.74441,3.08631,2.62492,2.12551,1.34264,1.35839,1.93997]),
        H298 = (87.4225,'kcal/mol','+|-',5.00776),
        S298 = (-2.54602,'cal/mol/K','+|-',6.17276),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 127,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.380435,-0.0871046,-0.590008,-0.959183,-1.62649,-2.2606,-3.55929],'cal/mol/K','+|-',[3.15477,2.37111,1.64657,1.36999,1.28793,1.36253,1.45721]),
        H298 = (87.8336,'kcal/mol','+|-',3.78573),
        S298 = (-1.70406,'cal/mol/K','+|-',3.79107),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 128,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   u0 {2,D} {5,S}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0649674,-0.224322,-0.582104,-0.884461,-1.48804,-2.08204,-3.35379],'cal/mol/K','+|-',[2.84766,2.44858,1.79959,1.42316,1.10888,1.00804,0.913678]),
        H298 = (87.7889,'kcal/mol','+|-',3.91482),
        S298 = (-1.26238,'cal/mol/K','+|-',3.13579),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 129,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C u0 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
5   C u0 {3,S}
6   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.461357,0.0373415,-0.483868,-0.894099,-1.64518,-2.30317,-3.60499],'cal/mol/K','+|-',[1.27856,2.85272,3.08501,2.89217,2.4211,1.92886,1.35686]),
        H298 = (86.494,'kcal/mol','+|-',8.18798),
        S298 = (-2.68545,'cal/mol/K','+|-',0.576505),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 130,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C u0 r0 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
5   C u0 r0 {3,S}
6   C ux {3,[S,D,T,B,Q]} {7,S}
7   C u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.719665,0.613677,0.139399,-0.309793,-1.15604,-1.91349,-3.33086],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (85.6734,'kcal/mol','+|-',1.69706),
        S298 = (-2.80192,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 131,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C                      u0 r0 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   C                      ux {2,[S,D,T,B,Q]}
5   C                      u0 r0 {3,S}
6   C                      ux {3,[S,D,T,B,Q]} {7,S}
7   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.184412,-1.4035,-2.04203,-2.35486,-2.86802,-3.2774,-4.2903],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.4631,'kcal/mol','+|-',4.17612),
        S298 = (-2.39427,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 132,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H-4R!H",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D} {5,S}
4   C   u0 {2,S} {6,S}
5   O   u0 {3,S}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.28593,-0.00125416,-0.35337,-0.646501,-1.24062,-1.84621,-3.16205],'cal/mol/K','+|-',[3.72211,2.89195,1.66718,0.888738,0.275122,0.638625,0.912093]),
        H298 = (88.4412,'kcal/mol','+|-',3.96963),
        S298 = (-1.15076,'cal/mol/K','+|-',3.24301),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 133,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D} {5,S}
4   C   u0 {2,S} {6,S} {7,D}
5   O   u0 {3,S}
6   C   u0 {4,S}
7   R!H u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.4932,-0.569681,-0.604495,-0.726929,-1.16123,-1.7421,-3.21594],'cal/mol/K','+|-',[3.6248,2.99536,2.01132,1.19351,0.0108285,0.745351,1.26259]),
        H298 = (88.7471,'kcal/mol','+|-',5.41012),
        S298 = (-0.710294,'cal/mol/K','+|-',4.04698),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 134,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-4R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D} {5,S}
4   C u0 r0 {2,S} {6,S} {7,D}
5   O u0 r0 {3,S}
6   C u0 r0 {4,S}
7   C u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77476,-1.6287,-1.31561,-1.1489,-1.1574,-1.47858,-2.76954],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (86.8344,'kcal/mol','+|-',1.69706),
        S298 = (-2.14112,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=CO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 135,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-4R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D} {4,S}
3   C                      u0 r0 {2,D} {5,S}
4   C                      u0 r0 {2,S} {6,S} {7,D}
5   O                      u0 r0 {3,S}
6   C                      u0 r0 {4,S}
7   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.788362,0.489339,0.106615,-0.30496,-1.16506,-2.00562,-3.66233],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (90.6599,'kcal/mol','+|-',1.69706),
        S298 = (0.720529,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 136,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-4R!H-R_N-Sp-6R!H-4R!H",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D} {5,S}
4   C   u0 r0 {2,S} {6,[B,D,T,Q]}
5   O   u0 r0 {3,S}
6   R!H u0 r0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.15287,-1.25985,-1.40584,-1.58485,-2.01031,-2.47993,-3.57732],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (87.341,'kcal/mol','+|-',1.69706),
        S298 = (0.395063,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C=C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 137,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.76541,1.00628,-0.589909,-1.57719,-2.77355,-3.53581,-5.3452],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (89.1927,'kcal/mol','+|-',4.17612),
        S298 = (-4.56703,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 138,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {4,S}
4   O u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.492687,0.20639,-0.162708,-0.547473,-1.32659,-2.06663,-3.47524],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (85.1813,'kcal/mol','+|-',1.69706),
        S298 = (-3.29518,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 139,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.424108,-1.36402,-1.88839,-2.02609,-1.95901,-2.02646,-2.57121],'cal/mol/K','+|-',[5.86304,4.61848,4.07423,3.21188,1.74186,1.77827,2.77518]),
        H298 = (87.4117,'kcal/mol','+|-',9.68489),
        S298 = (-4.26564,'cal/mol/K','+|-',10.4454),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 140,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.6541,-1.80433,-2.36295,-2.45219,-2.22377,-2.15575,-2.63851],'cal/mol/K','+|-',[6.50704,4.4991,3.60113,2.54978,1.13434,1.85778,3.1242]),
        H298 = (87.88,'kcal/mol','+|-',10.1742),
        S298 = (-3.98959,'cal/mol/K','+|-',11.7399),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 141,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,S}
6   R!H u0 {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.18855,-4.90468,-5.17533,-4.55789,-2.90287,-1.95031,-2.50066],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.9338,'kcal/mol','+|-',4.17612),
        S298 = (0.518706,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CC(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 142,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H-6R!H",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,S}
5   C ux {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,S}
7   C ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.50098,-0.150599,-1.54519,-2.02932,-1.9611,-1.87527,-1.90019],'cal/mol/K','+|-',[5.79035,4.10992,3.21111,1.76554,1.57433,3.38229,5.35355]),
        H298 = (86.6792,'kcal/mol','+|-',5.4215),
        S298 = (-9.86413,'cal/mol/K','+|-',9.21814),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 143,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   C   ux {4,S} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,S}
7   C   ux {6,S}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.54818,1.30248,-0.409891,-1.4051,-2.51771,-3.07109,-3.79296],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.596,'kcal/mol','+|-',4.17612),
        S298 = (-6.60502,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=C(CC=CC)CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 144,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {4,S}
4   C u0 r0 {3,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]} {6,S}
6   C u0 {5,S} {7,D}
7   C u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.16439,-1.88717,-1.89222,-1.94822,-2.16228,-2.46231,-3.2843],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (86.6164,'kcal/mol','+|-',1.69706),
        S298 = (-1.09329,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CCCC=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 145,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_N-Sp-2R!H-1C",
    group = 
"""
1 * C u1 {2,D}
2   C u0 r0 {1,D} {3,D}
3   C u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.454632,-0.167716,-0.905438,-1.59475,-2.69293,-3.47892,-4.53057],'cal/mol/K','+|-',[0.866746,1.04623,1.21111,1.14602,0.936146,0.680261,0.0984156]),
        H298 = (88.7547,'kcal/mol','+|-',3.58167),
        S298 = (1.29267,'cal/mol/K','+|-',0.198045),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 146,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_N-Sp-2R!H-1C_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   u0 r0 {1,D} {3,D}
3   C   u0 r0 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.148191,-0.537616,-1.33363,-1.99993,-3.02391,-3.71943,-4.56537],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (87.4884,'kcal/mol','+|-',1.69706),
        S298 = (1.22265,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 147,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.9591,-5.45697,-6.03557,-5.43682,-3.86893,-2.80987,-2.65609],'cal/mol/K','+|-',[4.90648,6.24325,6.9305,6.68106,5.2155,4.61493,5.45693]),
        H298 = (87.2822,'kcal/mol','+|-',28.0887),
        S298 = (3.96717,'cal/mol/K','+|-',18.2085),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 148,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.29741,-5.37064,-5.60343,-4.84183,-3.2194,-2.16852,-2.11368],'cal/mol/K','+|-',[5.69563,7.26733,7.66449,7.14853,5.28525,4.42467,4.94066]),
        H298 = (85.0619,'kcal/mol','+|-',32.48),
        S298 = (2.44566,'cal/mol/K','+|-',16.0848),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 149,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.4772,-6.09275,-6.63216,-5.89878,-3.96445,-2.70675,-2.37208],'cal/mol/K','+|-',[6.23291,7.29909,7.05894,6.2829,4.93421,4.58223,5.92053]),
        H298 = (94.746,'kcal/mol','+|-',10.6896),
        S298 = (4.86027,'cal/mol/K','+|-',16.0166),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 150,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.58478,-6.27765,-6.925,-6.24425,-4.3314,-3.12593,-2.78953],'cal/mol/K','+|-',[6.79928,7.92359,7.54408,6.5848,4.96904,4.39232,6.01728]),
        H298 = (95.604,'kcal/mol','+|-',10.6011),
        S298 = (2.45017,'cal/mol/K','+|-',10.6145),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 151,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.8659,-7.17608,-8.00329,-7.20875,-4.87596,-3.35257,-2.52945],'cal/mol/K','+|-',[8.52812,9.36116,8.48681,7.32646,5.77509,5.27746,7.52267]),
        H298 = (98.0908,'kcal/mol','+|-',7.92424),
        S298 = (2.88983,'cal/mol/K','+|-',13.1077),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 152,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   u0 {2,D} {7,S}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,S}
6   O   u0 {5,S}
7   O   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.05771,-8.88893,-8.89813,-7.16722,-3.54578,-1.5732,0.236515],'cal/mol/K','+|-',[11.7792,14.5172,13.3153,10.843,5.00616,0.901755,4.82461]),
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
    index = 153,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_5R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C u0 r0 {2,D} {7,S}
4   C ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux r0 {4,[S,D,T,B,Q]} {6,S}
6   O u0 r0 {5,S}
7   O u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.2223,-14.0215,-13.6058,-11.0008,-5.31573,-1.25438,1.94227],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.232,'kcal/mol','+|-',4.17612),
        S298 = (2.93024,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=CO)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 154,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_N-5R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C u0 r0 {2,D} {7,S}
4   C ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r0 {4,[S,D,T,B,Q]} {6,S}
6   O u0 r0 {5,S}
7   O u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.89312,-3.75631,-4.19044,-3.33364,-1.77583,-1.89202,-1.46924],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (92.9573,'kcal/mol','+|-',4.17612),
        S298 = (-5.80781,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 155,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O_4C-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.10711,-6.26966,-8.91012,-9.58032,-8.6218,-7.13453,-7.03056],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (102.003,'kcal/mol','+|-',4.17612),
        S298 = (10.0233,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 156,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O_N-4C-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,S}
6   O ux {5,S}
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
    index = 157,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C ux {2,D}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.02255,-4.48079,-4.7684,-4.31525,-3.24227,-2.67265,-3.30969],'cal/mol/K','+|-',[3.02837,3.50398,3.56045,3.33381,3.02782,3.23144,2.83193]),
        H298 = (90.6306,'kcal/mol','+|-',8.75903),
        S298 = (1.57084,'cal/mol/K','+|-',6.21493),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 158,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   u0 r0 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C   ux {2,D}
4   C   u0 r0 {2,S} {5,[S,D,T,B,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]} {6,S} {7,[S,D,T,B,Q]}
6   C   ux r0 {5,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.09324,-5.71963,-6.02721,-5.49393,-4.31277,-3.81514,-4.31093],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.7274,'kcal/mol','+|-',4.17612),
        S298 = (3.76815,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 159,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_N-4R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.87788,-3.68571,-3.20306,-2.37562,-1.48096,-0.912635,-1.51076],'cal/mol/K','+|-',[5.28441,7.31433,8.09178,7.7071,5.17291,3.40442,1.25367]),
        H298 = (62.4655,'kcal/mol','+|-',5.28536),
        S298 = (-3.18844,'cal/mol/K','+|-',11.0713),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 160,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_N-4R!H->C_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   O   ux r0 {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.73462,-6.6109,-6.59142,-5.62941,-3.64516,-2.33287,-1.76178],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (59.4585,'kcal/mol','+|-',4.17612),
        S298 = (1.68085,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC=C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 161,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   O   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.147065,0.414555,1.27653,1.87986,1.38353,0.974224,-0.797316],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (64.4186,'kcal/mol','+|-',4.17612),
        S298 = (-9.2093,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 162,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-3C-R_4R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.37497,-6.15466,-7.82772,-7.68117,-6.19828,-5.17445,-4.77642],'cal/mol/K','+|-',[0.917966,3.09844,4.75661,4.65309,3.1029,2.76308,7.00694]),
        H298 = (93.3758,'kcal/mol','+|-',5.37682),
        S298 = (2.19792,'cal/mol/K','+|-',9.13058),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 163,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-3C-R_4R!H->C_4C-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.9045,-7.39622,-9.90787,-9.85255,-7.76493,-6.71476,-8.81574],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.4445,'kcal/mol','+|-',4.17612),
        S298 = (7.42729,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=CC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 164,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-3C-R_4R!H->C_N-4C-inRing",
    group = 
"""
1 * O u1 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.11021,-5.53388,-6.78765,-6.59548,-5.41495,-4.4043,-2.75676],'cal/mol/K','+|-',[0.0540798,3.15465,4.39187,3.8747,2.12829,1.01685,0.545724]),
        H298 = (91.8414,'kcal/mol','+|-',1.14717),
        S298 = (-0.41677,'cal/mol/K','+|-',1.63004),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 165,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-3C-R_4R!H->C_N-4C-inRing_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D} {4,S} {5,[S,D,T,B,Q]}
4   C   u0 r0 {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09109,-6.64922,-8.34041,-7.9654,-6.16742,-4.76381,-2.56382],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.4358,'kcal/mol','+|-',4.17612),
        S298 = (-0.993076,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 166,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-3C-R_N-4R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D}
3   C                      u0 r0 {2,D} {4,S}
4   [Cl,O,Si,S,N,P,F,I,Br] u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32842,-4.22716,-4.98042,-4.65365,-3.37613,-2.12961,-1.71919],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.2046,'kcal/mol','+|-',4.17612),
        S298 = (24.4901,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 167,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.752188,-1.91778,-2.68069,-3.13496,-3.60292,-3.99653,-4.83722],'cal/mol/K','+|-',[4.10604,4.39899,4.53133,4.43666,4.00621,3.77164,3.77742]),
        H298 = (98.3634,'kcal/mol','+|-',16.72),
        S298 = (0.965102,'cal/mol/K','+|-',9.02052),
    ),
    shortDesc = """Radical correction fitted to 143 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 168,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.100342,-1.24122,-2.08752,-2.6189,-3.23541,-3.74336,-4.82457],'cal/mol/K','+|-',[3.442,3.84412,4.07493,3.95654,3.36599,3.09222,3.06271]),
        H298 = (102.093,'kcal/mol','+|-',13.8899),
        S298 = (1.61666,'cal/mol/K','+|-',7.00153),
    ),
    shortDesc = """Radical correction fitted to 82 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 169,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R",
    group = 
"""
1 * C u1 {2,D}
2   C ux {1,D} {3,[S,T,Q,B]}
3   C u0 {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.731104,-1.46325,-1.95707,-2.33084,-2.95747,-3.52514,-4.75723],'cal/mol/K','+|-',[3.3333,2.55447,2.13017,1.85894,1.39321,1.13767,1.37783]),
        H298 = (110.703,'kcal/mol','+|-',5.94169),
        S298 = (1.93798,'cal/mol/K','+|-',4.40686),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 170,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-2C-R",
    group = 
"""
1 * C   u1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]} {4,S}
3   C   u0 {2,[S,T,Q,B]}
4   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.25626,-0.0904757,-0.874499,-1.33696,-2.07965,-2.78965,-4.53796],'cal/mol/K','+|-',[7.14599,5.73201,4.07175,2.89204,1.27931,0.179173,1.36531]),
        H298 = (117.864,'kcal/mol','+|-',4.57855),
        S298 = (-1.08467,'cal/mol/K','+|-',7.62847),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 171,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-2C-R_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,D} {5,[S,D,T,B,Q]}
2   C   ux {1,D} {3,[S,T,Q,B]} {4,S}
3   C   u0 {2,[S,T,Q,B]}
4   C   u0 r0 {2,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.78275,1.9361,0.565081,-0.314472,-1.62734,-2.7263,-5.02067],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (116.245,'kcal/mol','+|-',4.17612),
        S298 = (-3.78174,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)O[C]=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 172,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,D}
2   C   u0 {1,D} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   R!H u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.37889,-1.83238,-2.0585,-2.36515,-2.98721,-3.55084,-4.60887],'cal/mol/K','+|-',[0.841152,0.95336,0.80551,0.535277,0.170736,0.0674739,0.243732]),
        H298 = (109.281,'kcal/mol','+|-',1.43228),
        S298 = (2.62419,'cal/mol/K','+|-',2.31087),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 173,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,D}
2   C u0 r0 {1,D} {3,S}
3   C u0 r0 {2,S} {4,[S,D,T,B,Q]}
4   C u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0815,-1.49532,-1.77371,-2.1759,-2.92685,-3.52698,-4.5227],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (108.775,'kcal/mol','+|-',1.69706),
        S298 = (1.80717,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 174,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,D}
2   C                      u0 r0 {1,D} {3,S}
3   C                      u0 r0 {2,S} {4,[S,D,T,B,Q]}
4   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.67628,-2.16945,-2.34329,-2.5544,-3.04758,-3.57469,-4.69504],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (109.787,'kcal/mol','+|-',1.69706),
        S298 = (3.4412,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 175,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-1R-R_4R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,D} {4,S}
2   C u0 r0 {1,D} {3,S}
3   C u0 r0 {2,S}
4   C u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.749289,-2.17238,-3.5742,-4.07087,-4.40918,-4.80164,-6.53194],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (112.745,'kcal/mol','+|-',4.17612),
        S298 = (3.25547,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 176,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-1R-R_N-4R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,D} {4,S}
2   C u0 r0 {1,D} {3,S}
3   C u0 r0 {2,S}
4   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01815,-1.53954,-1.97343,-2.3613,-3.01954,-3.55156,-4.51949],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (110.846,'kcal/mol','+|-',1.69706),
        S298 = (2.45669,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=[C]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 177,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0449195,-1.22171,-2.09898,-2.64421,-3.25984,-3.76253,-4.83049],'cal/mol/K','+|-',[3.4573,3.95072,4.21356,4.09516,3.48872,3.20988,3.17473]),
        H298 = (101.284,'kcal/mol','+|-',13.3317),
        S298 = (1.58842,'cal/mol/K','+|-',7.20841),
    ),
    shortDesc = """Radical correction fitted to 76 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 178,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.438336,-0.778409,-1.70694,-2.3544,-3.13823,-3.77849,-5.0214],'cal/mol/K','+|-',[2.84265,3.59617,3.97138,3.93486,3.39977,3.15602,3.12859]),
        H298 = (100.292,'kcal/mol','+|-',10.1805),
        S298 = (1.86652,'cal/mol/K','+|-',7.0159),
    ),
    shortDesc = """Radical correction fitted to 58 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 179,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.514733,-0.883973,-1.9381,-2.56145,-3.25847,-3.87274,-5.14251],'cal/mol/K','+|-',[2.94206,3.98521,4.55948,4.51699,3.85538,3.56976,3.69421]),
        H298 = (102.319,'kcal/mol','+|-',9.34341),
        S298 = (1.84586,'cal/mol/K','+|-',7.78224),
    ),
    shortDesc = """Radical correction fitted to 39 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 180,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.395763,-0.872689,-1.96369,-2.58783,-3.28743,-3.96547,-5.35782],'cal/mol/K','+|-',[2.86441,4.37523,5.10814,5.11909,4.44447,4.10322,4.14694]),
        H298 = (102.87,'kcal/mol','+|-',10.6629),
        S298 = (1.91504,'cal/mol/K','+|-',9.00194),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 181,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.616096,-1.02392,-1.576,-1.99039,-2.69042,-3.3327,-4.09297],'cal/mol/K','+|-',[0.858109,1.52688,2.03301,2.27292,2.43455,2.47747,1.59021]),
        H298 = (106.05,'kcal/mol','+|-',5.49161),
        S298 = (1.74975,'cal/mol/K','+|-',4.74479),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 182,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C_3O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   ux r1 {2,S}
4   R!H u0 r1 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.554731,-0.642861,-2.05548,-2.57805,-3.10826,-4.30081,-3.77339],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (110.638,'kcal/mol','+|-',4.17612),
        S298 = (3.40577,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O1[C]2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 183,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C_N-3O-inRing",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.624278,-1.07473,-1.51207,-1.91204,-2.63471,-3.20362,-4.13558],'cal/mol/K','+|-',[0.951943,1.65778,2.21295,2.46345,2.67644,2.59467,1.74103]),
        H298 = (105.798,'kcal/mol','+|-',5.09603),
        S298 = (1.52894,'cal/mol/K','+|-',5.03228),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 184,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C_N-3O-inRing_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O u0 r0 {2,[S,T,Q,B]}
4   C ux r1 {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
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
    index = 185,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C_N-3O-inRing_N-4R!H->C",
    group = 
"""
1 * C u1 {2,S} {4,S}
2   C u0 {1,S} {3,S} {4,S}
3   O ux r0 {2,S}
4   O u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.349476,-0.606672,-0.910777,-1.27163,-1.9939,-2.60475,-3.70028],'cal/mol/K','+|-',[0.000693138,0.488481,1.05687,1.51472,2.11457,2.20392,1.23073]),
        H298 = (104.377,'kcal/mol','+|-',1.87816),
        S298 = (0.118093,'cal/mol/K','+|-',1.69577),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 186,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C_N-3O-inRing_N-4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,S} {4,S} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,S}
4   O   u0 r1 {1,S} {2,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.349721,-0.433968,-0.537117,-0.7361,-1.24629,-1.82555,-3.26515],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.713,'kcal/mol','+|-',1.69706),
        S298 = (-0.481452,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OCC1(O)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 187,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_1C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.931886,-3.04044,-4.50526,-5.25076,-5.8582,-6.41429,-9.30734],'cal/mol/K','+|-',[1.76817,3.06577,3.48025,3.39703,3.62845,4.68152,0.905954]),
        H298 = (98.0185,'kcal/mol','+|-',2.04637),
        S298 = (7.82813,'cal/mol/K','+|-',7.57699),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 188,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_1C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-3O_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]}
5   C   u0 {1,S}
6   O   ux {3,[S,D,T,B,Q]} {7,S}
7   C   u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.43731,-3.81545,-5.34427,-6.02722,-6.53806,-7.22698,-9.23892],'cal/mol/K','+|-',[0.349147,2.09341,2.70738,2.93427,3.90365,5.28983,1.23659]),
        H298 = (97.7001,'kcal/mol','+|-',2.43778),
        S298 = (9.87094,'cal/mol/K','+|-',3.82992),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 189,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_1C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-3O_Ext-6R!H-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
5   C u0 {1,S}
6   O ux r1 {3,[S,D,T,B,Q]} {7,S}
7   C u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31387,-3.07532,-4.38707,-4.9898,-5.15791,-5.35674,-9.67612],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.8382,'kcal/mol','+|-',4.17612),
        S298 = (8.51686,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 190,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_1C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-3O_Ext-6R!H-R_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   O ux {2,[S,D,T,B,Q]}
5   C u0 {1,S}
6   O ux r1 {3,[S,D,T,B,Q]} {7,S}
7   C u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.56076,-4.55559,-6.30147,-7.06465,-7.91821,-9.09721,-8.80172],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.562,'kcal/mol','+|-',4.17612),
        S298 = (11.225,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1COOC12COO2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 191,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.853354,-0.589463,-1.80625,-2.482,-3.19151,-3.89391,-5.31791],'cal/mol/K','+|-',[2.89027,4.87469,5.69159,5.64316,4.73992,4.2162,3.84273]),
        H298 = (101.845,'kcal/mol','+|-',11.5776),
        S298 = (1.32107,'cal/mol/K','+|-',9.44627),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 192,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.1293,-0.217897,-1.46057,-2.1991,-3.079,-3.8612,-5.18525],'cal/mol/K','+|-',[2.65005,4.58065,5.40924,5.36299,4.46848,4.0881,3.79939]),
        H298 = (102.342,'kcal/mol','+|-',10.6318),
        S298 = (1.35192,'cal/mol/K','+|-',9.20143),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 193,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.964845,-0.111929,-1.23473,-1.97605,-2.84848,-3.6433,-5.40601],'cal/mol/K','+|-',[2.88175,4.94885,5.63596,5.46637,4.20124,3.58704,3.89177]),
        H298 = (101.297,'kcal/mol','+|-',7.81722),
        S298 = (2.79043,'cal/mol/K','+|-',6.04232),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 194,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]} {5,S}
5   O   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.15587,0.345598,-0.700806,-1.4776,-2.51808,-3.46621,-5.23531],'cal/mol/K','+|-',[2.82042,4.48874,5.07309,4.9998,4.02008,3.69687,4.05436]),
        H298 = (100.89,'kcal/mol','+|-',4.91758),
        S298 = (2.50196,'cal/mol/K','+|-',6.2518),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 195,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_5O-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 {2,S}
4   C u0 {2,S} {5,S}
5   O ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.465723,-0.548566,-1.58829,-2.35493,-3.50178,-4.60488,-5.58721],'cal/mol/K','+|-',[2.09926,4.28452,5.81416,6.38745,6.67829,7.96134,6.27852]),
        H298 = (100.186,'kcal/mol','+|-',14.5685),
        S298 = (4.33956,'cal/mol/K','+|-',9.19191),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 196,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_5O-inRing_Ext-3O-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S} {6,[S,D,T,B,Q]}
4   C   u0 r1 {2,S} {5,S}
5   O   ux r1 {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.594565,-2.71257,-4.52489,-5.58108,-6.87482,-8.62597,-8.75834],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.3445,'kcal/mol','+|-',4.17612),
        S298 = (8.98217,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C12COOC1(C)COO2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 197,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]} {5,S}
5   O   ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.36592,0.617735,-0.430702,-1.21058,-2.21869,-3.11966,-5.1282],'cal/mol/K','+|-',[3.0473,4.81888,5.34372,5.15095,3.6766,2.58132,4.03618]),
        H298 = (101.114,'kcal/mol','+|-',3.41377),
        S298 = (1.9427,'cal/mol/K','+|-',5.84895),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 198,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]} {5,S}
5   O ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.18851,0.47699,-0.515885,-1.27122,-2.24529,-3.06977,-5.12299],'cal/mol/K','+|-',[2.94732,5.00981,5.64297,5.45553,3.90256,2.7175,4.28976]),
        H298 = (101.018,'kcal/mol','+|-',3.38215),
        S298 = (2.35319,'cal/mol/K','+|-',5.38432),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 199,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_Ext-5O-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]} {5,S}
5   O   ux r0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19057,0.56235,-0.35803,-1.13703,-2.22374,-3.10094,-5.14535],'cal/mol/K','+|-',[2.13953,4.04555,4.65306,4.64408,3.46413,2.80372,5.89106]),
        H298 = (100.686,'kcal/mol','+|-',1.01902),
        S298 = (0.687588,'cal/mol/K','+|-',3.12359),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 200,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_Ext-5O-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S}
4   C   u0 {2,S} {5,S} {7,[S,D,T,B,Q]}
5   O   ux r0 {4,S} {6,S}
6   R!H u0 r0 {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.695229,-2.87677,-4.37511,-5.18461,-5.26426,-5.57596,-10.3487],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.928,'kcal/mol','+|-',4.17612),
        S298 = (3.40729,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)OOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 201,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_Ext-5O-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]} {5,S}
5   O   ux r0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.49847,0.770492,0.0133183,-0.662195,-1.79254,-2.66708,-4.00948],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (100.73,'kcal/mol','+|-',1.69706),
        S298 = (0.376393,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(COC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 202,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   C   ux r0 {2,[S,D,T,B,Q]} {5,S}
5   O   ux r0 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
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
    index = 203,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]} {5,S}
5   O ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.19625,-4.05656,-5.95793,-6.51672,-5.90565,-5.22162,-7.06852],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.211,'kcal/mol','+|-',4.17612),
        S298 = (5.57217,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(CO)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 204,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_N-2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]} {5,S}
5   O ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.74251,2.81278,1.90288,1.02498,-0.570666,-1.92438,-4.15594],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.685,'kcal/mol','+|-',1.69706),
        S298 = (5.4511,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 205,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 {2,S}
4   O u0 {2,S} {5,S}
5   O ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.22876,2.09556,0.463713,-0.573932,-1.93937,-3.64348,-5.18301],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (103.148,'kcal/mol','+|-',4.17612),
        S298 = (-2.36751,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]C(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 206,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_N-Sp-5O-4R!H",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 {2,S}
4   C u0 {2,S} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.467867,-3.54338,-5.23912,-5.71442,-5.32654,-4.97148,-6.68631],'cal/mol/K','+|-',[1.8765,1.2471,0.490865,0.221286,1.03145,0.923532,0.645474]),
        H298 = (107.25,'kcal/mol','+|-',26.891),
        S298 = (4.9539,'cal/mol/K','+|-',1.18184),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 207,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_N-Sp-5O-4R!H_Ext-3O-R_Int-6R!H-2C_Int-6R!H-3O_Sp-6R!H-1C",
    group = 
"""
1 * C u1 r0 {2,S} {6,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r1 {2,S}
4   C u0 {2,S} {5,D}
5   O ux {4,D}
6   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13131,-3.9843,-5.41267,-5.63619,-4.96187,-4.64496,-6.45811],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.7428,'kcal/mol','+|-',4.17612),
        S298 = (4.53605,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 208,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_N-Sp-5O-4R!H_Ext-3O-R_Int-6R!H-2C_Int-6R!H-3O_N-Sp-6R!H-1C",
    group = 
"""
1 * C u1 r0 {2,S} {6,[B,D,T,Q]}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r1 {2,S}
4   C u0 {2,S} {5,D}
5   O ux {4,D}
6   C u0 r0 {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.195576,-3.10247,-5.06558,-5.79266,-5.69121,-5.298,-6.91452],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (116.758,'kcal/mol','+|-',4.17612),
        S298 = (5.37174,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=[C]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 209,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 {2,S}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5594,-0.495045,-2.05122,-2.78248,-3.68187,-4.43107,-4.60786],'cal/mol/K','+|-',[2.02643,4.08997,5.37566,5.70487,5.58275,5.63836,3.83291]),
        H298 = (105.587,'kcal/mol','+|-',18.0876),
        S298 = (-2.41032,'cal/mol/K','+|-',12.5611),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 210,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 {2,S}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.58384,-2.39617,-5.57754,-7.49396,-8.99154,-9.98726,-8.41459],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (126.496,'kcal/mol','+|-',4.17612),
        S298 = (2.79432,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)CC(OO)C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 211,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.55496,-0.149385,-1.41007,-1.92585,-2.71648,-3.42086,-3.91573],'cal/mol/K','+|-',[2.30087,4.13445,4.67595,3.80528,2.29803,1.66409,1.00053]),
        H298 = (103.278,'kcal/mol','+|-',2.29948),
        S298 = (-3.35662,'cal/mol/K','+|-',13.0346),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 212,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing_Ext-3O-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {4,S}
3   O   u0 {2,S} {6,S}
4   C   u0 {2,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.42609,-0.285354,-1.52814,-2.02744,-2.76916,-3.4636,-3.83138],'cal/mol/K','+|-',[2.63885,4.87737,5.54873,4.51108,2.73099,1.97412,1.0813]),
        H298 = (103.108,'kcal/mol','+|-',2.23357),
        S298 = (-3.89951,'cal/mol/K','+|-',15.2423),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 213,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing_Ext-3O-R_6R!H->N",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S} {6,S}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   N u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.20872,1.22205,0.225114,-0.577511,-1.87265,-2.82678,-4.20318],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.062,'kcal/mol','+|-',1.69706),
        S298 = (0.506017,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC(C=C)[CH2])CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 214,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing_Ext-3O-R_N-6R!H->N",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S} {6,S}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.447799,-2.1696,-3.71972,-3.83985,-3.88981,-4.25963,-3.36664],'cal/mol/K','+|-',[2.1881,3.50868,3.59713,2.6391,1.34336,1.12593,0.0878782]),
        H298 = (103.246,'kcal/mol','+|-',4.00465),
        S298 = (-9.40643,'cal/mol/K','+|-',13.5219),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 215,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing_Ext-3O-R_N-6R!H->N_Ext-6BrCClFIOPSSi-R_7R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S} {6,S}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O u0 r0 {3,S} {7,S}
7   C u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.325811,-3.41011,-4.99149,-4.77291,-4.36476,-4.65771,-3.39771],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (104.661,'kcal/mol','+|-',4.17612),
        S298 = (-4.62571,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C=C)OOC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 216,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing_Ext-3O-R_N-6R!H->N_Ext-6BrCClFIOPSSi-R_N-7R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S} {6,S}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O u0 r0 {3,S} {7,S}
7   C u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.22141,-0.929098,-2.44794,-2.90678,-3.41486,-3.86156,-3.33557],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.83,'kcal/mol','+|-',4.17612),
        S298 = (-14.1871,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C=C)OOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 217,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_2C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53771,-5.28753,-7.46739,-8.21796,-7.78401,-6.97593,-8.08096],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (109.514,'kcal/mol','+|-',4.17612),
        S298 = (8.84825,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=[C]C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 218,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_N-2C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.511174,-1.93404,-2.62708,-2.78601,-2.54202,-3.12279,-5.4361],'cal/mol/K','+|-',[2.33415,4.19436,5.18868,5.37401,5.29637,5.05088,4.21955]),
        H298 = (92.4453,'kcal/mol','+|-',2.44063),
        S298 = (-1.4297,'cal/mol/K','+|-',8.62688),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 219,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_N-2C-inRing_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.05129,-3.14471,-4.10065,-4.25555,-3.91171,-4.40416,-6.64322],'cal/mol/K','+|-',[1.97364,0.0885303,1.31569,2.43525,3.32835,3.40833,0.798641]),
        H298 = (92.0377,'kcal/mol','+|-',2.81541),
        S298 = (-0.323618,'cal/mol/K','+|-',10.9309),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 220,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_N-2C-inRing_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-7R!H-R_9R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   O   ux {3,[S,D,T,B,Q]} {7,S}
7   C   u0 r0 {6,S} {8,[S,D,T,B,Q]}
8   C   ux {7,[S,D,T,B,Q]} {9,[S,D]}
9   O   u0 r0 {8,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3535,-3.11341,-4.56582,-5.11654,-5.08845,-5.60919,-6.92558],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.0423,'kcal/mol','+|-',4.17612),
        S298 = (3.54103,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C(C)(C)OOC(C)(C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 221,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_N-2C-inRing_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-7R!H-R_N-9R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   O   ux {3,[S,D,T,B,Q]} {7,S}
7   C   u0 r0 {6,S} {8,[S,D,T,B,Q]}
8   C   ux {7,[S,D,T,B,Q]} {9,[S,D]}
9   C   u0 r0 {8,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.74907,-3.17601,-3.63548,-3.39456,-2.73496,-3.19913,-6.36086],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.0331,'kcal/mol','+|-',4.17612),
        S298 = (-4.18827,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(COO)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 222,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.795933,-0.910643,-1.87762,-2.49908,-3.19002,-3.65357,-4.63362],'cal/mol/K','+|-',[3.20701,3.08464,3.13607,2.85527,2.0647,1.90341,2.15856]),
        H298 = (100.953,'kcal/mol','+|-',4.36998),
        S298 = (1.68235,'cal/mol/K','+|-',3.99232),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 223,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-2C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 {1,S} {3,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C   ux {2,S}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.625305,-0.462439,-1.35449,-2.03677,-2.94935,-3.61067,-4.71134],'cal/mol/K','+|-',[0.983537,3.79746,4.97141,5.37104,4.69192,3.7194,2.14119]),
        H298 = (99.4257,'kcal/mol','+|-',0.37027),
        S298 = (3.07819,'cal/mol/K','+|-',2.8236),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 224,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-2C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {6,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C   ux {2,S}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.128544,-2.38044,-3.86543,-4.74956,-5.31913,-5.48925,-5.79281],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.6504,'kcal/mol','+|-',4.17612),
        S298 = (4.50432,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(C)(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 225,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-1C-R",
    group = 
"""
1 * C u1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.73484,-2.87603,-3.91083,-4.19666,-3.83996,-3.43472,-3.70337],'cal/mol/K','+|-',[7.34036,4.40535,3.43619,2.27242,1.58868,2.74117,4.29515]),
        H298 = (98.0824,'kcal/mol','+|-',0.926088),
        S298 = (0.268444,'cal/mol/K','+|-',5.06477),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 226,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-1C-R_3C-inRing",
    group = 
"""
1 * C u1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.98321,-4.03774,-4.76692,-4.65665,-3.65708,-2.84934,-2.60257],'cal/mol/K','+|-',[10.3093,2.53468,2.45471,2.29116,2.06037,2.60848,2.79539]),
        H298 = (98.1249,'kcal/mol','+|-',1.29298),
        S298 = (-0.956449,'cal/mol/K','+|-',3.91087),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 227,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-1C-R_3C-inRing_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.62809,-4.93389,-5.63479,-5.4667,-4.38553,-3.77158,-3.59088],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.5821,'kcal/mol','+|-',4.17612),
        S298 = (0.426254,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCCC1[CH]CCC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 228,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-1C-R_3C-inRing_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.66168,-3.1416,-3.89905,-3.8466,-2.92863,-1.92711,-1.61425],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.6678,'kcal/mol','+|-',4.17612),
        S298 = (-2.33915,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]C(CC)C1C=CC=C(C)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 229,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-1C-R_N-3C-inRing",
    group = 
"""
1 * C u1 {2,S} {5,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 r0 {2,S}
4   C u0 {2,S}
5   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2381,-0.552619,-2.19866,-3.27666,-4.20573,-4.60546,-5.90498],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.9972,'kcal/mol','+|-',4.17612),
        S298 = (2.71823,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]C(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 230,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_2C-inRing",
    group = 
"""
1 * C u1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5703,0.126999,-1.20718,-1.99646,-2.9502,-3.49991,-4.7552],'cal/mol/K','+|-',[1.553,2.27008,2.5294,2.1353,1.59535,1.17347,0.438071]),
        H298 = (102.328,'kcal/mol','+|-',8.94685),
        S298 = (2.63954,'cal/mol/K','+|-',3.20639),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 231,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_2C-inRing_Ext-4R!H-R_Sp-5R!H=4R!H",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]}
4   C   ux r1 {2,[S,D,T,B,Q]} {5,D}
5   R!H u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.46646,-0.848019,-2.54252,-3.16098,-3.77327,-4.0252,-4.95906],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (107.044,'kcal/mol','+|-',4.17612),
        S298 = (3.7537,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1C=C(O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 232,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_2C-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   C   u0 {2,S}
4   C   u0 {2,S} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.62222,0.614508,-0.539515,-1.41421,-2.53866,-3.23726,-4.65327],'cal/mol/K','+|-',[2.1815,2.14535,1.4481,0.991183,1.0127,1.04807,0.366687]),
        H298 = (99.9693,'kcal/mol','+|-',5.15782),
        S298 = (2.08245,'cal/mol/K','+|-',3.62129),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 233,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_2C-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-4R!H-3C",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 r1 {2,S} {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.39349,1.373,-0.0275328,-1.06377,-2.18062,-2.86671,-4.52362],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.793,'kcal/mol','+|-',4.17612),
        S298 = (3.36277,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 234,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_N-2C-inRing",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.146988,-0.737139,-1.55514,-2.2181,-3.13459,-3.83466,-4.94133],'cal/mol/K','+|-',[1.31039,1.30122,1.57808,1.87527,1.74027,1.70567,1.55491]),
        H298 = (102.035,'kcal/mol','+|-',1.49583),
        S298 = (1.18016,'cal/mol/K','+|-',4.11861),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 235,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_N-2C-inRing_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.474214,-0.587365,-1.58449,-2.36168,-3.33992,-4.05753,-5.14003],'cal/mol/K','+|-',[1.07231,1.6448,2.14159,2.47183,2.19102,2.10673,1.92932]),
        H298 = (101.852,'kcal/mol','+|-',2.29353),
        S298 = (0.375314,'cal/mol/K','+|-',4.3713),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 236,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_N-2C-inRing_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.1067,-1.74957,-3.11871,-4.10806,-4.87288,-5.53614,-6.42332],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.9854,'kcal/mol','+|-',4.17612),
        S298 = (-2.7575,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 237,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_N-2C-inRing_Ext-3C-R_5R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.445199,-0.342768,-1.0864,-1.73089,-2.7589,-3.50505,-4.56937],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.201,'kcal/mol','+|-',1.69706),
        S298 = (1.38758,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 238,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_N-2C-inRing_Ext-3C-R_N-5R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
5   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12766,-0.0366518,-1.29547,-2.19225,-3.2595,-3.96012,-5.28338],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.608,'kcal/mol','+|-',4.17612),
        S298 = (0.977465,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 239,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.109186,-0.903733,-1.60255,-2.21533,-3.07258,-3.69555,-4.82867],'cal/mol/K','+|-',[3.00667,3.15551,2.9748,3.0162,2.92196,2.78439,2.22713]),
        H298 = (97.3269,'kcal/mol','+|-',8.3015),
        S298 = (2.54347,'cal/mol/K','+|-',5.08408),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 240,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.84466,-0.909553,-2.15188,-3.18679,-4.5338,-5.34272,-6.11114],'cal/mol/K','+|-',[3.44718,6.95728,6.40204,6.04047,5.18327,4.53076,3.44953]),
        H298 = (101.837,'kcal/mol','+|-',3.36514),
        S298 = (1.03133,'cal/mol/K','+|-',5.47207),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 241,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing_Ext-4R!H-R_Ext-5R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,S}
3   R!H u0 {2,S} {5,S}
4   R!H u0 r1 {1,[S,D,T,B,Q]}
5   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.07302,-2.6566,-3.67378,-4.97729,-6.57961,-7.10404,-7.44654],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.8828,'kcal/mol','+|-',4.17612),
        S298 = (4.08648,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 242,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {5,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   O   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.49304,-0.521321,-1.81368,-2.7889,-4.07918,-4.95132,-5.81438],'cal/mol/K','+|-',[1.18637,7.98184,7.37823,6.80924,5.54928,4.86874,3.71055]),
        H298 = (102.204,'kcal/mol','+|-',2.05136),
        S298 = (0.35241,'cal/mol/K','+|-',5.07558),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 243,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {5,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   O   ux {3,S}
6   R!H ux {1,[S,D,T,B,Q]}
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
    index = 244,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-5R!H->C_3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {5,S}
4   R!H ux r1 {1,[S,D,T,B,Q]}
5   O   ux r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.78631,-1.02221,-3.36002,-4.88675,-6.58289,-7.76231,-8.36541],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.881,'kcal/mol','+|-',4.17612),
        S298 = (1.95745,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C[CH]COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 245,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-5R!H->C_N-3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {5,S}
4   R!H ux r1 {1,[S,D,T,B,Q]}
5   O   ux r1 {3,S}
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
    index = 246,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.380308,-0.902092,-1.44761,-1.94133,-2.66045,-3.23096,-4.46695],'cal/mol/K','+|-',[2.10198,1.56864,1.46396,1.5552,1.36285,1.12885,1.11348]),
        H298 = (96.4589,'kcal/mol','+|-',7.86752),
        S298 = (2.96997,'cal/mol/K','+|-',4.89194),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 247,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.461806,-0.901198,-1.41209,-1.88419,-2.56023,-3.11024,-4.40019],'cal/mol/K','+|-',[2.32229,1.75408,1.62117,1.7063,1.42587,1.09099,1.19026]),
        H298 = (97.7193,'kcal/mol','+|-',4.93361),
        S298 = (3.41723,'cal/mol/K','+|-',4.99062),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 248,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.825755,-1.02181,-1.42021,-1.84283,-2.56716,-3.22782,-4.51602],'cal/mol/K','+|-',[2.46365,2.07509,1.63043,1.47546,1.14984,0.831918,0.199367]),
        H298 = (97.4486,'kcal/mol','+|-',4.58966),
        S298 = (2.2946,'cal/mol/K','+|-',3.19696),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 249,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]}
4   C ux r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21973,-2.15253,-2.25351,-2.59418,-3.18768,-3.67923,-4.57992],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (99.1004,'kcal/mol','+|-',1.69706),
        S298 = (4.29339,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 250,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.24493,-0.550682,-1.073,-1.52976,-2.30861,-3.03973,-4.4894],'cal/mol/K','+|-',[1.62975,1.50408,1.32481,1.20539,0.850317,0.608358,0.223696]),
        H298 = (96.6857,'kcal/mol','+|-',4.98791),
        S298 = (1.46177,'cal/mol/K','+|-',1.31952),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 251,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C_N-4R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {5,S}
4   O   ux {1,S}
5   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.321809,-0.485338,-0.870235,-1.28185,-2.07684,-2.84321,-4.45259],'cal/mol/K','+|-',[2.61404,2.4162,1.90793,1.53898,0.796604,0.251377,0.315432]),
        H298 = (97.8507,'kcal/mol','+|-',7.71606),
        S298 = (1.8306,'cal/mol/K','+|-',1.17091),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 252,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C_N-4R!H->C_Ext-3C-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {5,S}
4   O ux r0 {1,S}
5   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.206306,0.00280813,-0.484774,-0.97093,-1.91591,-2.79242,-4.51632],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (98.624,'kcal/mol','+|-',1.69706),
        S298 = (2.06716,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 253,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C_N-4R!H->C_Ext-3C-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,S}
2   C                      ux r0 {1,S} {3,[S,T,Q,B]}
3   C                      ux r0 {2,[S,T,Q,B]} {5,S}
4   O                      ux r0 {1,S}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6421,-1.7057,-1.83389,-2.05916,-2.47919,-2.97017,-4.29328],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.1679,'kcal/mol','+|-',4.17612),
        S298 = (1.2392,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CO[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 254,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_N-3R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0493313,-0.764499,-1.40289,-1.93106,-2.55237,-2.97699,-4.26891],'cal/mol/K','+|-',[2.28978,1.68369,1.96486,2.28068,1.97322,1.47668,1.89947]),
        H298 = (97.9683,'kcal/mol','+|-',6.18515),
        S298 = (4.68953,'cal/mol/K','+|-',6.06679),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 255,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_N-3R!H->C_Ext-3O-R_5R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux {1,S}
5   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.70882,-1.21081,-1.77051,-2.22714,-2.64256,-2.92326,-4.38039],'cal/mol/K','+|-',[0.21899,0.942871,2.11611,2.88082,2.75536,2.07168,2.63015]),
        H298 = (96.0546,'kcal/mol','+|-',4.03864),
        S298 = (3.20537,'cal/mol/K','+|-',4.55474),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 256,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_N-3R!H->C_Ext-3O-R_5R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   O   ux r0 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux r0 {1,S}
5   O   ux {3,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.631395,-1.54416,-2.51866,-3.24566,-3.61672,-3.6557,-5.31029],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (97.4825,'kcal/mol','+|-',1.69706),
        S298 = (4.81571,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](COO)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 257,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_N-3R!H->C_Ext-3O-R_N-5R!H->O",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,S}
2   C                      u0 {1,S} {3,S}
3   O                      u0 {2,S} {5,S}
4   R!H                    u0 {1,S}
5   [Cl,C,Si,S,N,P,F,I,Br] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.26965,0.128119,-0.66765,-1.3389,-2.37199,-3.08445,-4.04596],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (100.626,'kcal/mol','+|-',1.41421),
        S298 = (7.65787,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]COCOO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
""",
)

entry(
    index = 258,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_N-Sp-4R!H-1C",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   O ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00774594,-0.906178,-1.61001,-2.20258,-3.11859,-3.78281,-4.77213],'cal/mol/K','+|-',[0.278562,0.518317,0.640837,0.722982,0.670337,0.581302,0.542299]),
        H298 = (89.3141,'kcal/mol','+|-',2.47136),
        S298 = (0.925367,'cal/mol/K','+|-',0.654451),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 259,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_N-Sp-4R!H-1C_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,D}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   O   ux r0 {1,D}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.064024,-0.801462,-1.48055,-2.05652,-2.98316,-3.66537,-4.66257],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (89.0665,'kcal/mol','+|-',1.69706),
        S298 = (1.05759,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 260,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C",
    group = 
"""
1 * C u1 {2,S}
2   C ux {1,S} {3,S}
3   C ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.89818,0.0651309,-0.803104,-1.72906,-2.79304,-3.60304,-4.98065],'cal/mol/K','+|-',[2.20471,2.45512,2.31433,2.46152,1.83335,1.67707,1.53726]),
        H298 = (102.344,'kcal/mol','+|-',2.73573),
        S298 = (1.95641,'cal/mol/K','+|-',3.11485),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 261,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.706159,-1.05852,-1.96404,-3.29852,-3.9611,-4.50189,-5.92638],'cal/mol/K','+|-',[0.492361,0.41108,1.95497,1.27732,1.84012,2.66788,1.40587]),
        H298 = (101.985,'kcal/mol','+|-',8.06717),
        S298 = (3.92299,'cal/mol/K','+|-',3.39978),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 262,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.532083,-1.20386,-2.65523,-3.75012,-4.61168,-5.44513,-6.42343],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.1328,'kcal/mol','+|-',4.17612),
        S298 = (2.72098,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]CC(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 263,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C ux {1,S} {3,S}
3   C ux {2,S} {4,S}
4   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.962187,0.439681,-0.416125,-1.20591,-2.40368,-3.30342,-4.66541],'cal/mol/K','+|-',[2.77285,2.47148,1.95095,1.53428,0.806255,0.592345,0.865626]),
        H298 = (102.399,'kcal/mol','+|-',1.10075),
        S298 = (1.30088,'cal/mol/K','+|-',1.26588),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 264,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C_Ext-3R!H-R_N-4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C u1 {2,S}
2   C ux {1,S} {3,S}
3   C ux {2,S} {4,S} {5,[S,D,T,B,Q]}
4   O u0 {3,S}
5   O u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3974,0.830197,-0.0963367,-0.94918,-2.26144,-3.23309,-4.62408],'cal/mol/K','+|-',[1.56249,1.35728,0.89477,0.606061,0.0624498,0.537443,1.02077]),
        H298 = (102.49,'kcal/mol','+|-',0.786393),
        S298 = (1.09087,'cal/mol/K','+|-',0.53524),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 265,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C_Ext-3R!H-R_N-4R!H->C_Ext-3R!H-R_Ext-4BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,S}
3   C   ux r0 {2,S} {4,S} {5,S}
4   O   u0 r0 {3,S} {6,[S,D,T,B,Q]}
5   O   u0 r0 {3,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.94982,1.31007,0.220012,-0.734905,-2.28352,-3.4231,-4.98498],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.212,'kcal/mol','+|-',1.69706),
        S298 = (0.901629,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]CC(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 266,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_N-Sp-3R!H-2C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,T}
3   C ux r0 {2,T}
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
    index = 267,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.58795,-2.63715,-3.35075,-3.56957,-3.64813,-3.71158,-4.22092],'cal/mol/K','+|-',[3.51921,3.79727,4.10534,4.17995,3.77541,3.49016,3.11258]),
        H298 = (104.481,'kcal/mol','+|-',19.8128),
        S298 = (0.700482,'cal/mol/K','+|-',7.77483),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 268,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_Int-4R!H-2C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11247,-1.257,-1.55572,-1.77118,-2.20343,-2.54968,-4.06704],'cal/mol/K','+|-',[0.368765,0.560232,0.721763,0.808472,0.736509,0.653689,3.14078]),
        H298 = (89.5128,'kcal/mol','+|-',53.8359),
        S298 = (-1.14464,'cal/mol/K','+|-',1.33914),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 269,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_Int-4R!H-2C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,S} {4,S}
3   R!H u0 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
4   R!H ux r1 {2,S} {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3742,-0.864459,-1.04516,-1.19075,-1.67771,-2.15229,-3.34269],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (47.7999,'kcal/mol','+|-',4.17612),
        S298 = (-2.10889,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C12OC1(O)O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 270,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_Int-4R!H-2C_Ext-2C-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   R!H ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.994736,-1.28002,-1.79475,-1.98015,-2.28664,-2.42145,-6.32718],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (113.294,'kcal/mol','+|-',4.17612),
        S298 = (-0.877071,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#CC1([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 271,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.881225,-2.53187,-3.88501,-4.34385,-4.49788,-4.73183,-5.33992],'cal/mol/K','+|-',[1.19341,2.54405,2.98726,3.31375,3.40611,3.14639,3.4745]),
        H298 = (109.401,'kcal/mol','+|-',3.75694),
        S298 = (-0.139881,'cal/mol/K','+|-',5.14621),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 272,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.905893,-2.59719,-4.08041,-4.64904,-4.83216,-5.09573,-5.75429],'cal/mol/K','+|-',[1.30831,2.77831,3.05997,3.11346,3.11665,2.61154,2.81282]),
        H298 = (109.039,'kcal/mol','+|-',2.71583),
        S298 = (0.450611,'cal/mol/K','+|-',4.29718),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 273,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_Ext-4O-R_Ext-5R!H-R_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 {1,S} {3,S} {7,[S,D,T,B,Q]}
3   R!H u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   O   u0 r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux r1 {4,[S,D,T,B,Q]} {6,S}
6   R!H u0 {5,S}
7   R!H ux {2,[S,D,T,B,Q]}
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
    index = 274,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_2C-inRing",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   R!H ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.132994,-0.614532,-1.8387,-2.19977,-2.71534,-3.96296,-4.5852],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (111.355,'kcal/mol','+|-',4.17612),
        S298 = (-3.7391,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1COOC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 275,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_N-2C-inRing",
    group = 
"""
1 * O u1 {2,S}
2   C u0 r0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.03919,-2.6065,-4.07011,-4.78292,-5.07875,-5.35299,-5.61357],'cal/mol/K','+|-',[1.06395,1.64426,1.37657,1.9132,3.04617,3.19666,2.74776]),
        H298 = (108.865,'kcal/mol','+|-',2.38659),
        S298 = (1.12357,'cal/mol/K','+|-',1.63702),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 276,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_N-2C-inRing_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4O-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
4   O   u0 r1 {3,S} {7,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,S}
6   O   u0 {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.273125,-2.07196,-4.1565,-5.53586,-6.07736,-6.42326,-5.3411],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (110.865,'kcal/mol','+|-',4.17612),
        S298 = (0.515398,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 277,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_N-2C-inRing_Ext-4O-R_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   O u0 r1 {3,S} {5,S}
5   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24842,-1.74679,-3.09912,-3.46218,-2.92185,-3.09424,-7.56949],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (108.82,'kcal/mol','+|-',4.17612),
        S298 = (0.329631,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1OC1(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 278,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_N-2C-inRing_Ext-4O-R_N-5R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,S}
3   C                      u0 r1 {2,S} {4,S}
4   O                      u0 r1 {3,S} {5,S}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26193,-3.16419,-4.42396,-5.01004,-5.54206,-5.82839,-4.94019],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (108.542,'kcal/mol','+|-',1.69706),
        S298 = (1.68441,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CC1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 279,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_N-3R!H-inRing",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.720883,-2.10728,-2.61487,-2.36009,-2.32508,-2.36649,-2.64653],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (113.049,'kcal/mol','+|-',4.17612),
        S298 = (-3.97808,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(OC(C)=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 280,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.03886,-3.06142,-3.59747,-3.70809,-3.65589,-3.56471,-3.75425],'cal/mol/K','+|-',[4.47621,4.54782,4.73801,4.71478,4.15989,3.78958,2.72167]),
        H298 = (106.412,'kcal/mol','+|-',4.75349),
        S298 = (1.58568,'cal/mol/K','+|-',9.54554),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 281,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.28201,-2.62119,-4.16866,-4.68699,-4.89689,-4.75067,-4.41874],'cal/mol/K','+|-',[5.25787,6.19968,6.24934,6.07748,5.03616,4.45506,3.76319]),
        H298 = (107.961,'kcal/mol','+|-',8.80021),
        S298 = (5.1118,'cal/mol/K','+|-',12.8248),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 282,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-4BrCClFINPSSi-R_Sp-6R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {6,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.517345,-1.47921,-3.06646,-3.64074,-3.85629,-3.73847,-3.90528],'cal/mol/K','+|-',[6.65904,7.49424,7.64998,7.48762,5.84179,4.93627,4.85341]),
        H298 = (105.653,'kcal/mol','+|-',11.5427),
        S298 = (6.20268,'cal/mol/K','+|-',17.2711),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 283,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-4BrCClFINPSSi-R_Sp-6R!H-4BrCClFINPSSi_2C-inRing",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {6,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.602899,-2.42992,-4.13263,-4.88072,-5.11696,-5.00238,-5.30447],'cal/mol/K','+|-',[7.6529,9.52022,9.47434,8.67337,5.48732,3.22403,0.354045]),
        H298 = (102.7,'kcal/mol','+|-',7.56168),
        S298 = (1.53458,'cal/mol/K','+|-',8.57882),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 284,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-4BrCClFINPSSi-R_Sp-6R!H-4BrCClFINPSSi_2C-inRing_Ext-2C-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   ux r1 {3,S} {6,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H u0 r1 {4,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.30861,-5.79583,-7.48231,-7.94722,-7.05701,-6.14225,-5.42964],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (105.373,'kcal/mol','+|-',4.17612),
        S298 = (4.56765,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CCOC1(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 285,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-4BrCClFINPSSi-R_Sp-6R!H-4BrCClFINPSSi_N-2C-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {4,S}
4   C   u0 {3,S} {6,S}
5   R!H u0 {2,S}
6   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.75783,0.422212,-0.934123,-1.16077,-1.33497,-1.21065,-1.10689],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (111.559,'kcal/mol','+|-',4.17612),
        S298 = (15.5389,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=CC([O])C(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 286,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-4BrCClFINPSSi-R_N-Sp-6R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {6,[B,D,T,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H u0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24124,-3.99157,-5.4913,-5.94249,-6.14562,-5.96531,-5.03489],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (109.104,'kcal/mol','+|-',1.69706),
        S298 = (3.80276,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 287,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.37664,-3.58424,-3.42776,-3.21033,-2.77456,-2.58567,-3.24348],'cal/mol/K','+|-',[1.64992,3.40761,4.50349,4.67237,4.21495,4.13163,3.08246]),
        H298 = (106.433,'kcal/mol','+|-',4.14254),
        S298 = (-0.5149,'cal/mol/K','+|-',6.63886),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 288,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8256,-2.75222,-2.53066,-2.32653,-1.91644,-1.63243,-2.44586],'cal/mol/K','+|-',[0.0644842,3.76814,5.85749,6.23979,5.41441,4.84129,3.15879]),
        H298 = (105.171,'kcal/mol','+|-',4.19804),
        S298 = (-2.30443,'cal/mol/K','+|-',6.35412),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 289,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_3R!H->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r0 {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.83863,-1.99094,-1.34727,-1.0659,-0.822565,-0.654347,-1.80769],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (104.75,'kcal/mol','+|-',1.69706),
        S298 = (-3.58815,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 290,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_N-3R!H->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   O   ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r0 {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.79303,-4.65542,-5.48914,-5.4781,-4.65113,-4.07765,-4.04129],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (107.718,'kcal/mol','+|-',4.17612),
        S298 = (0.904887,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 291,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 {1,S} {3,S}
3   R!H u0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
5   O   u0 r0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.1481,-4.74908,-4.6837,-4.44765,-3.97593,-3.9202,-4.36016],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (107.905,'kcal/mol','+|-',1.69706),
        S298 = (1.99044,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 292,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_3R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S}
4   C ux r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.647964,-0.732587,-1.10158,-1.42902,-2.1098,-2.65411,-3.48749],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (104.857,'kcal/mol','+|-',1.69706),
        S298 = (-1.99921,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 293,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_N-3R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,S}
4   C ux r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.08414,-5.10396,-5.24401,-5.02823,-4.58693,-4.21588,-3.78496],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (105.603,'kcal/mol','+|-',1.69706),
        S298 = (2.45448,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
COC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 294,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.76704,-2.9711,-3.60419,-3.93842,-4.17509,-4.39069,-4.85692],'cal/mol/K','+|-',[4.26211,4.41492,4.6269,4.7,4.64653,4.55972,4.71456]),
        H298 = (91.7736,'kcal/mol','+|-',12.7726),
        S298 = (-0.0492958,'cal/mol/K','+|-',11.2635),
    ),
    shortDesc = """Radical correction fitted to 61 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 295,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.481461,-1.77876,-2.36796,-2.77031,-3.34135,-3.73218,-4.37842],'cal/mol/K','+|-',[2.69005,3.67444,3.90754,3.77816,3.14069,2.5624,2.05976]),
        H298 = (99.4555,'kcal/mol','+|-',6.25414),
        S298 = (3.77568,'cal/mol/K','+|-',12.3649),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 296,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.542523,-2.0716,-2.66803,-3.07355,-3.6379,-4.02203,-4.66522],'cal/mol/K','+|-',[2.90424,3.58275,3.83938,3.76092,3.18183,2.64475,1.98043]),
        H298 = (98.6882,'kcal/mol','+|-',5.81595),
        S298 = (4.51158,'cal/mol/K','+|-',14.1967),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 297,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_4R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.357829,-1.6785,-2.46974,-2.92046,-3.49133,-3.95906,-4.63521],'cal/mol/K','+|-',[1.83605,0.828418,1.55262,2.0157,2.38878,2.47877,2.54314]),
        H298 = (97.5037,'kcal/mol','+|-',7.90233),
        S298 = (7.66856,'cal/mol/K','+|-',20.8962),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 298,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,S}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C   ux r0 {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
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
    index = 299,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_4R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   C   ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.436282,-2.06156,-2.96946,-3.65708,-4.597,-5.10316,-5.39429],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (97.391,'kcal/mol','+|-',1.69706),
        S298 = (4.22986,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 300,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_N-4R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.700832,-2.40854,-2.838,-3.20478,-3.76354,-4.076,-4.69094],'cal/mol/K','+|-',[3.96085,5.13112,5.49999,5.27484,4.21233,3.26835,1.92408]),
        H298 = (99.7887,'kcal/mol','+|-',3.82299),
        S298 = (1.80561,'cal/mol/K','+|-',4.60106),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 301,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_N-4R!H->C_Int-4BrClFINOPSSi-3R!H",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9903,-2.35863,-2.46639,-2.47752,-2.62975,-2.91066,-3.87562],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (101.303,'kcal/mol','+|-',1.69706),
        S298 = (0.108702,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OC(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 302,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_N-4R!H->C_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   O   u0 {1,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.15697,-7.37692,-8.25434,-8.45772,-7.87513,-6.99172,-5.60119],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.253,'kcal/mol','+|-',4.17612),
        S298 = (6.14956,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CO[CH]OC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 303,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_N-4R!H->C_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.740247,-0.678845,-1.09769,-1.74572,-3.0165,-3.69503,-4.5715],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (98.2989,'kcal/mol','+|-',1.69706),
        S298 = (1.8144,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 304,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_N-4R!H->C_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23644,-1.8892,-2.70149,-3.41763,-4.35403,-5.02605,-6.11761],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.1787,'kcal/mol','+|-',4.17612),
        S298 = (1.68194,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 305,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904944,-1.87324,-2.27408,-2.40607,-2.64255,-2.68012,-2.52329],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (107.122,'kcal/mol','+|-',4.17612),
        S298 = (-1.03696,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]OC(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 306,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.90441,-3.56718,-4.39736,-4.64132,-4.52976,-4.16712,-3.45035],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (104.181,'kcal/mol','+|-',4.17612),
        S298 = (4.58276,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]OC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 307,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.10791,-3.28725,-3.93197,-4.24815,-4.39616,-4.5653,-4.9838],'cal/mol/K','+|-',[4.36639,4.4234,4.62936,4.77074,4.90933,4.92297,5.18624]),
        H298 = (89.1734,'kcal/mol','+|-',9.85108),
        S298 = (-1.06349,'cal/mol/K','+|-',10.2174),
    ),
    shortDesc = """Radical correction fitted to 51 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 308,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.23621,-3.81771,-4.00115,-4.00198,-3.81305,-3.7704,-3.8683],'cal/mol/K','+|-',[4.03558,5.62881,6.43253,6.41542,5.87162,5.59589,5.47774]),
        H298 = (92.1107,'kcal/mol','+|-',13.8608),
        S298 = (1.11572,'cal/mol/K','+|-',10.8148),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 309,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.81564,-4.6773,-4.87805,-4.70418,-4.12287,-3.79786,-3.49174],'cal/mol/K','+|-',[4.25164,5.75076,6.7278,7.01843,6.78841,6.59063,6.36241]),
        H298 = (89.1223,'kcal/mol','+|-',13.4614),
        S298 = (1.57991,'cal/mol/K','+|-',12.8287),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 310,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-4O-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   O ux {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.79514,-7.63866,-8.26603,-8.15818,-7.14834,-6.35674,-5.31743],'cal/mol/K','+|-',[1.50431,2.80637,5.64026,6.27989,4.95494,4.03383,3.90257]),
        H298 = (92.4452,'kcal/mol','+|-',11.6555),
        S298 = (4.14017,'cal/mol/K','+|-',7.8919),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 311,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-4O-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   O ux {3,S} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.89257,-7.26105,-7.71,-7.57434,-6.66826,-6.02013,-5.45478],'cal/mol/K','+|-',[1.95079,2.90049,6.76381,7.65399,5.97206,5.03757,5.25334]),
        H298 = (91.2966,'kcal/mol','+|-',9.10539),
        S298 = (4.32101,'cal/mol/K','+|-',10.7153),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 312,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-4O-R_Ext-5R!H-R_6R!H->O_3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,S}
4   O ux {3,S} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.90727,-8.72602,-11.1262,-11.4402,-9.68461,-8.56448,-8.10811],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.8225,'kcal/mol','+|-',4.17612),
        S298 = (9.73306,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1C=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 313,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-4O-R_Ext-5R!H-R_6R!H->O_N-3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S}
4   O ux {3,S} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.28669,-6.67506,-6.3435,-6.028,-5.46173,-5.00238,-4.39344],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (90.3841,'kcal/mol','+|-',1.69706),
        S298 = (2.1562,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 314,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-4O-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * O                      u1 {2,S}
2   O                      ux {1,S} {3,S}
3   C                      u0 {2,S} {4,S}
4   O                      u0 {3,S} {5,[S,D,T,B,Q]}
5   C                      ux {4,[S,D,T,B,Q]} {6,S}
6   [Cl,C,Si,S,N,P,F,I,Br] u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.45415,-8.96032,-10.2121,-10.2016,-8.8286,-7.5349,-4.83672],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.549,'kcal/mol','+|-',4.17612),
        S298 = (3.50721,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C=O)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 315,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O   ux {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.92265,-3.14641,-2.96948,-2.56171,-1.91213,-1.71412,-1.71548],'cal/mol/K','+|-',[4.3409,4.62364,4.34634,4.53811,6.21179,7.30311,8.17554]),
        H298 = (86.7596,'kcal/mol','+|-',22.0802),
        S298 = (0.818792,'cal/mol/K','+|-',18.8841),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 316,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {5,S}
4   O   ux {3,S}
5   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.86861,-3.20452,-3.2499,-2.97865,-2.5445,-2.56901,-2.66349],'cal/mol/K','+|-',[5.18382,5.52125,4.9121,4.79935,6.35632,7.01674,7.89535]),
        H298 = (87.765,'kcal/mol','+|-',24.6891),
        S298 = (-2.47798,'cal/mol/K','+|-',10.3487),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 317,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S} {5,S} {6,[S,D,T,B,Q]}
4   O   ux r0 {3,S}
5   R!H ux {3,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.790431,0.704796,0.285743,0.0482161,-0.508576,-1.4306,-3.47376],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (74.6536,'kcal/mol','+|-',4.17612),
        S298 = (-3.40966,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 318,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,S}
4   O   u0 r0 {3,S}
5   C   u0 r0 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 319,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {5,[B,D,T,Q]}
4   O   u0 {3,S}
5   R!H u0 r0 {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.16587,-2.88494,-1.7076,-0.685491,0.933524,2.13287,2.55058],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (78.6605,'kcal/mol','+|-',4.17612),
        S298 = (15.6543,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 320,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H",
    group = 
"""
1 * O u1 {2,S}
2   O ux {1,S} {3,S}
3   C u0 {2,S} {4,D}
4   O u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.78763,-1.66872,-1.80889,-2.24649,-3.03851,-3.70177,-4.80968],'cal/mol/K','+|-',[0.600886,1.89399,3.10079,3.26037,3.26451,3.00486,1.90157]),
        H298 = (97.8271,'kcal/mol','+|-',2.6627),
        S298 = (-0.0447361,'cal/mol/K','+|-',2.98793),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 321,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,S}
3   C   u0 r0 {2,S} {4,D} {5,[S,D,T,B,Q]}
4   O   u0 r0 {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   u0 r0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.00007,-0.999087,-0.712601,-1.09377,-1.88433,-2.63939,-4.13738],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (96.8857,'kcal/mol','+|-',1.69706),
        S298 = (-1.10113,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 322,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.70079,-3.09585,-3.90701,-4.33698,-4.60656,-4.85212,-5.3863],'cal/mol/K','+|-',[4.2622,3.97673,3.96849,4.18636,4.58077,4.6489,4.9439]),
        H298 = (87.6703,'kcal/mol','+|-',5.68273),
        S298 = (-1.84981,'cal/mol/K','+|-',9.73995),
    ),
    shortDesc = """Radical correction fitted to 41 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 323,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54499,-3.02247,-3.89619,-4.36364,-4.68542,-4.9936,-5.64302],'cal/mol/K','+|-',[4.12276,3.95472,4.01103,4.26746,4.67597,4.67807,4.75193]),
        H298 = (87.9682,'kcal/mol','+|-',5.67011),
        S298 = (-2.34087,'cal/mol/K','+|-',8.1262),
    ),
    shortDesc = """Radical correction fitted to 39 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 324,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.4706,-2.95239,-3.85324,-4.34852,-4.71464,-5.0599,-5.74551],'cal/mol/K','+|-',[4.04615,3.88554,4.01572,4.31265,4.71409,4.64599,4.60045]),
        H298 = (87.9441,'kcal/mol','+|-',5.7081),
        S298 = (-2.27389,'cal/mol/K','+|-',8.1708),
    ),
    shortDesc = """Radical correction fitted to 38 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 325,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31197,-2.96141,-4.00767,-4.60764,-5.00121,-5.39351,-6.21893],'cal/mol/K','+|-',[4.19934,3.94816,4.03191,4.40721,5.05519,5.06323,5.1237]),
        H298 = (87.6138,'kcal/mol','+|-',4.87364),
        S298 = (-2.28842,'cal/mol/K','+|-',8.32425),
    ),
    shortDesc = """Radical correction fitted to 26 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 326,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00842,-2.59146,-3.58224,-4.0989,-4.33624,-4.72423,-5.76669],'cal/mol/K','+|-',[4.41983,4.37077,4.11565,4.01775,3.66805,3.19879,4.71346]),
        H298 = (86.1286,'kcal/mol','+|-',2.38014),
        S298 = (-3.04807,'cal/mol/K','+|-',7.07659),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 327,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   R!H ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.781384,-2.39595,-3.42942,-3.97207,-4.23919,-4.64827,-5.75193],'cal/mol/K','+|-',[4.08039,4.15341,4.0167,3.9832,3.67986,3.22631,4.85586]),
        H298 = (86.0045,'kcal/mol','+|-',2.10997),
        S298 = (-3.02745,'cal/mol/K','+|-',7.29074),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 328,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.832176,-2.40101,-3.4045,-3.90748,-4.13918,-4.54915,-5.4534],'cal/mol/K','+|-',[4.25847,4.35516,4.19683,4.16813,3.93064,3.42649,4.60247]),
        H298 = (85.9537,'kcal/mol','+|-',2.24041),
        S298 = (-2.51086,'cal/mol/K','+|-',7.38951),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 329,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_5C-inRing",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux r1 {4,S} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.34979,-4.24724,-5.14319,-5.51333,-5.53887,-5.50431,-6.16496],'cal/mol/K','+|-',[2.77736,2.8577,3.08129,3.76522,3.80588,3.44435,6.65384]),
        H298 = (85.9022,'kcal/mol','+|-',2.50323),
        S298 = (0.741346,'cal/mol/K','+|-',2.04659),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 330,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_5C-inRing_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   ux r1 {4,S} {6,S}
6   O   u0 r1 {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.32389,-4.8874,-6.95373,-8.12674,-8.26243,-7.97551,-10.8797],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.8303,'kcal/mol','+|-',4.17612),
        S298 = (0.871776,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OOCC(O[O])C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 331,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_5C-inRing_3R!H-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,S}
4   C ux r1 {3,S} {5,S} {7,D}
5   C ux r1 {4,S} {6,[S,D,T,B,Q]}
6   O ux r1 {5,[S,D,T,B,Q]}
7   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.12375,-4.814,-5.11752,-5.04335,-4.87749,-4.71725,-4.49081],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (86.264,'kcal/mol','+|-',1.69706),
        S298 = (1.26678,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1COOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 332,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_5C-inRing_N-3R!H-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S}
4   C ux r1 {3,S} {5,S} {7,D}
5   C ux r1 {4,S} {6,[S,D,T,B,Q]}
6   O ux r1 {5,[S,D,T,B,Q]}
7   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.440798,-2.19019,-3.39681,-4.0749,-4.46875,-5.00074,-5.63563],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.7833,'kcal/mol','+|-',4.17612),
        S298 = (-0.702662,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 333,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux r0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.149248,-1.57021,-2.62208,-3.18484,-3.50931,-4.11933,-5.1332],'cal/mol/K','+|-',[4.20903,3.94987,3.78602,3.72582,3.57179,3.33361,4.07174]),
        H298 = (85.9952,'kcal/mol','+|-',2.50659),
        S298 = (-3.97435,'cal/mol/K','+|-',6.95876),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 334,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.746751,-2.77289,-4.31821,-5.24218,-5.5345,-5.79827,-8.06374],'cal/mol/K','+|-',[2.97208,2.75704,2.49897,2.0998,1.28752,0.731183,6.50994]),
        H298 = (84.9153,'kcal/mol','+|-',1.69232),
        S298 = (-3.55526,'cal/mol/K','+|-',3.19763),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 335,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Ext-4BrCClFINPSSi-R_3R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79754,-3.74765,-5.20173,-5.98457,-5.9897,-6.05678,-10.3654],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.5136,'kcal/mol','+|-',4.17612),
        S298 = (-2.42473,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)C1(C)OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 336,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Ext-4BrCClFINPSSi-R_N-3R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.304037,-1.79813,-3.43469,-4.49979,-5.07929,-5.53976,-5.76213],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.317,'kcal/mol','+|-',4.17612),
        S298 = (-4.6858,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 337,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {8,S}
4   C   u0 {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H u0 {4,[S,D,T,B,Q]}
8   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.00092,0.657821,-0.0801114,-0.458058,-0.78172,-1.55942,-3.31876],'cal/mol/K','+|-',[2.99749,4.54529,4.62999,4.04322,3.65656,3.34116,0.251117]),
        H298 = (85.2699,'kcal/mol','+|-',1.71447),
        S298 = (-9.26254,'cal/mol/K','+|-',5.61495),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 338,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Ext-3R!H-R_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {8,S}
4   C   u0 r0 {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H u0 r0 {4,[S,D,T,B,Q]}
8   C   u0 r0 {3,S}
9   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.06069,2.26483,1.55684,0.971437,0.51107,-0.378144,-3.22998],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.6638,'kcal/mol','+|-',4.17612),
        S298 = (-11.2477,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 339,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Sp-6R!H-5C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux r0 {4,S} {6,S}
6   R!H ux {5,S}
7   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.0846,-0.948214,-2.30775,-3.12043,-3.87954,-4.76109,-5.04948],'cal/mol/K','+|-',[3.02738,2.09509,1.46916,1.3219,1.31539,1.32905,1.09217]),
        H298 = (86.2527,'kcal/mol','+|-',2.18857),
        S298 = (-2.56497,'cal/mol/K','+|-',5.56265),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 340,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Sp-6R!H-5C_Ext-5C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux r0 {4,S} {6,S} {8,[S,D,T,B,Q]}
6   O   ux {5,S}
7   C   ux {4,[S,D,T,B,Q]}
8   R!H u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.672875,-1.03942,-2.19039,-2.79138,-3.32753,-4.22015,-5.13942],'cal/mol/K','+|-',[4.75204,3.45853,2.39304,1.84976,0.549951,0.556408,1.0154]),
        H298 = (86.6271,'kcal/mol','+|-',2.1957),
        S298 = (-3.43764,'cal/mol/K','+|-',8.09564),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 341,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Sp-6R!H-5C_Ext-5C-R_3R!H-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C ux r0 {4,S} {6,S} {8,[S,D,T,B,Q]}
6   O ux {5,S}
7   C ux {4,[S,D,T,B,Q]}
8   O u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00722,-2.2622,-3.03645,-3.44537,-3.52197,-4.02343,-4.78042],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.4034,'kcal/mol','+|-',4.17612),
        S298 = (-0.575404,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1CC1C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 342,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Sp-6R!H-5C_Ext-5C-R_N-3R!H-inRing",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux r0 {4,S} {6,S} {8,[S,D,T,B,Q]}
6   O   ux {5,S}
7   C   ux {4,[S,D,T,B,Q]}
8   R!H u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.35297,0.183354,-1.34432,-2.13739,-3.1331,-4.41687,-5.49842],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.8508,'kcal/mol','+|-',4.17612),
        S298 = (-6.29988,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(CO[O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 343,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Sp-6R!H-5C_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 r0 {4,S} {6,S}
6   C   u0 r0 {5,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
7   C   u0 {4,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
9   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.02085,-0.490655,-2.16813,-3.3445,-4.4717,-5.49815,-4.40975],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.9227,'kcal/mol','+|-',4.17612),
        S298 = (-0.318208,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 344,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_N-Sp-6R!H-5C",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S} {7,D}
5   C   u0 r0 {4,S} {6,D}
6   C   u0 {5,D}
7   R!H u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.1696,-3.83953,-4.09661,-3.98311,-3.47127,-3.71677,-4.18453],'cal/mol/K','+|-',[1.83106,0.55761,1.07981,0.654606,0.257276,0.397165,0.914485]),
        H298 = (87.2855,'kcal/mol','+|-',2.90792),
        S298 = (-1.92401,'cal/mol/K','+|-',3.27102),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 345,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_N-Sp-6R!H-5C_7R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,S} {7,D}
5   C u0 r0 {4,S} {6,D}
6   C u0 r0 {5,D}
7   C u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.52223,-4.03668,-4.47838,-4.21454,-3.38031,-3.57635,-4.50785],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.3136,'kcal/mol','+|-',4.17612),
        S298 = (-0.767527,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC=CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 346,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_N-Sp-6R!H-5C_N-7R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,S} {7,D}
5   C u0 r0 {4,S} {6,D}
6   C u0 r0 {5,D}
7   O u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.81698,-3.64239,-3.71484,-3.75167,-3.56223,-3.85719,-3.86121],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.2574,'kcal/mol','+|-',4.17612),
        S298 = (-3.08048,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 347,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_N-5R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   O   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.535889,-2.37148,-3.5499,-4.28425,-4.72257,-5.12735,-7.19481],'cal/mol/K','+|-',[3.88272,3.85871,3.82858,3.66937,2.50686,2.31628,6.05666]),
        H298 = (86.3103,'kcal/mol','+|-',1.48427),
        S298 = (-5.52428,'cal/mol/K','+|-',5.11539),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 348,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_N-5R!H->C_3R!H-inRing",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 {3,S} {5,S} {7,[S,D,T,B,Q]}
5   O   ux {4,S} {6,[S,D,T,B,Q]}
6   O   u0 {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0168936,-2.21712,-3.67217,-4.57511,-5.20793,-5.56058,-8.11061],'cal/mol/K','+|-',[4.86687,5.40438,5.38119,4.98981,2.6296,2.49514,7.29641]),
        H298 = (86.1333,'kcal/mol','+|-',1.91147),
        S298 = (-6.71809,'cal/mol/K','+|-',4.25798),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 349,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_N-5R!H->C_3R!H-inRing_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   O   ux r1 {4,S} {6,[S,D,T,B,Q]}
6   O   u0 r1 {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.73759,-4.12785,-5.57471,-6.33927,-6.13763,-6.44275,-10.6903],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.8091,'kcal/mol','+|-',4.17612),
        S298 = (-5.21267,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 350,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_N-5R!H->C_N-3R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   O   u0 {4,S} {6,S}
6   R!H ux {5,S}
7   R!H u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57388,-2.6802,-3.30536,-3.70254,-3.75184,-4.26088,-5.36321],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.6644,'kcal/mol','+|-',4.17612),
        S298 = (-3.13668,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 351,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_N-Sp-5R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,D} {7,[S,D,T,B,Q]}
5   R!H u0 {4,D} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.98156,-6.01285,-6.25646,-6.31844,-6.03463,-6.0535,-6.02503],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.7414,'kcal/mol','+|-',4.17612),
        S298 = (-3.40904,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 352,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.62791,-3.97588,-4.26959,-4.35256,-3.86178,-3.85736,-8.42106],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.8666,'kcal/mol','+|-',4.17612),
        S298 = (-5.0628,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 353,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.65931,-3.57505,-4.80859,-5.62521,-6.41611,-6.85856,-6.8678],'cal/mol/K','+|-',[3.82274,3.01002,3.84671,4.97806,6.68496,7.11269,6.01709]),
        H298 = (89.745,'kcal/mol','+|-',4.8292),
        S298 = (-0.51706,'cal/mol/K','+|-',10.3207),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 354,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,[S,D,T,B,Q]}
5   R!H u0 {4,[S,D,T,B,Q]} {6,S} {7,[S,D,T,B,Q]}
6   R!H u0 {5,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.38713,-5.0676,-5.27749,-5.45262,-5.46224,-5.68766,-5.80891],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.8206,'kcal/mol','+|-',4.17612),
        S298 = (-0.211166,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 355,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {7,[S,D,T,B,Q]}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S}
7   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.946049,-3.44441,-5.13545,-6.26143,-7.43474,-7.998,-7.99563],'cal/mol/K','+|-',[3.56113,3.27955,4.34254,5.54576,7.33205,7.69573,5.91078]),
        H298 = (89.9663,'kcal/mol','+|-',5.60109),
        S298 = (0.284316,'cal/mol/K','+|-',12.4352),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 356,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {7,[S,D,T,B,Q]}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S} {8,[S,D,T,B,Q]}
7   C   ux {3,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13637,-3.94715,-5.92954,-7.30875,-8.77882,-9.42669,-9.40297],'cal/mol/K','+|-',[4.73887,2.92597,3.1187,4.44677,6.8251,7.0046,3.74406]),
        H298 = (89.8149,'kcal/mol','+|-',7.51388),
        S298 = (2.81193,'cal/mol/K','+|-',10.9211),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 357,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_Ext-6R!H-R_6R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {7,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]} {6,S}
6   C   ux {5,S} {8,S}
7   C   ux {3,S}
8   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.530766,-4.09756,-6.77113,-8.76443,-11.1052,-11.8372,-10.2917],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (90.8338,'kcal/mol','+|-',1.41421),
        S298 = (6.43496,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(COCOO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
""",
)

entry(
    index = 358,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_Ext-6R!H-R_N-6R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {7,[S,D,T,B,Q]}
4   C u0 {3,S} {5,S}
5   O u0 {4,S} {6,S}
6   O u0 {5,S} {8,[S,D,T,B,Q]}
7   C u0 {3,[S,D,T,B,Q]}
8   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.89337,-3.75914,-4.87756,-5.48916,-5.8709,-6.41353,-8.29203],'cal/mol/K','+|-',[7.18562,4.72452,3.16237,2.24784,1.56605,0.314847,4.42822]),
        H298 = (85.3724,'kcal/mol','+|-',0.374069),
        S298 = (-1.71685,'cal/mol/K','+|-',4.76569),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 359,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_Ext-6R!H-R_N-6R!H->C_3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
4   C u0 {3,S} {5,S}
5   O u0 {4,S} {6,S}
6   O u0 {5,S} {8,[S,D,T,B,Q]}
7   C u0 {3,[S,D,T,B,Q]}
8   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.43387,-5.42951,-5.99562,-6.28389,-6.42458,-6.52484,-9.85764],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.2402,'kcal/mol','+|-',4.17612),
        S298 = (-0.0319264,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 360,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_Ext-6R!H-R_N-6R!H->C_N-3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S} {7,[S,D,T,B,Q]}
4   C u0 {3,S} {5,S}
5   O u0 {4,S} {6,S}
6   O u0 {5,S} {8,[S,D,T,B,Q]}
7   C u0 {3,[S,D,T,B,Q]}
8   C ux {6,[S,D,T,B,Q]}
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

entry(
    index = 361,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_3R!H-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,S} {7,[S,D,T,B,Q]}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]} {6,S}
6   O ux {5,S}
7   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.286349,-0.928771,-1.41186,-1.82789,-2.32615,-2.51079,-3.29808],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.1594,'kcal/mol','+|-',4.17612),
        S298 = (-8.34978,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 362,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_N-3R!H-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S} {7,[S,D,T,B,Q]}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]} {6,S}
6   O ux {5,S}
7   C ux {3,[S,D,T,B,Q]}
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
    index = 363,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S}
4   C ux r0 {3,S} {5,D}
5   C ux r0 {4,D} {6,S}
6   C ux r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.76663,-2.11854,-2.39449,-2.68236,-3.00152,-3.31078,-2.9238],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (89.0058,'kcal/mol','+|-',4.17612),
        S298 = (-5.01256,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 364,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S}
4   C ux r0 {3,S} {5,D}
5   C ux r0 {4,D} {6,S}
6   O ux r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.46033,-4.38822,-4.62922,-4.60526,-4.16342,-4.17087,-4.53984],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.594,'kcal/mol','+|-',4.17612),
        S298 = (-1.53639,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 365,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.03353,-3.11216,-3.60328,-3.77005,-3.99415,-4.17075,-4.34055],'cal/mol/K','+|-',[4.30851,4.5854,4.85129,4.93494,4.7444,4.19591,2.65668]),
        H298 = (89.1216,'kcal/mol','+|-',6.27059),
        S298 = (-2.15384,'cal/mol/K','+|-',10.173),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 366,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
6   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.30869,-2.03137,-2.3601,-2.50507,-2.80027,-3.13773,-3.75586],'cal/mol/K','+|-',[3.87515,2.3555,1.2046,1.21759,1.56305,1.69269,1.69334]),
        H298 = (87.9324,'kcal/mol','+|-',6.58631),
        S298 = (-4.62835,'cal/mol/K','+|-',4.45353),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 367,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_Sp-6R!H-3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {6,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
6   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.205523,-1.12803,-2.10076,-2.46701,-2.91947,-3.4492,-4.29269],'cal/mol/K','+|-',[1.84916,1.32753,1.29463,1.43497,1.86581,2.01642,1.3607]),
        H298 = (91.2441,'kcal/mol','+|-',3.56474),
        S298 = (-6.10865,'cal/mol/K','+|-',3.74099),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 368,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {6,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
6   C ux {3,S} {7,D}
7   C ux {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.51131,-1.06184,-2.18337,-2.67114,-3.27045,-3.81743,-4.63125],'cal/mol/K','+|-',[1.69851,1.59323,1.53307,1.44521,1.50509,1.6866,0.162308]),
        H298 = (90.7124,'kcal/mol','+|-',3.50388),
        S298 = (-6.04062,'cal/mol/K','+|-',4.56962),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 369,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S} {6,S}
4   C   ux r0 {3,S} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   O   ux r0 {4,[S,D,T,B,Q]}
6   C   u0 r0 {3,S} {7,D}
7   C   u0 r0 {6,D}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.14056,-0.650037,-2.08429,-2.72084,-3.53548,-4.22573,-4.56889],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.03,'kcal/mol','+|-',4.17612),
        S298 = (-5.68538,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 370,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {6,S} {8,[S,D,T,B,Q]}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   C   ux {3,S} {7,D}
7   C   ux {6,D}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.848049,-0.555419,-1.4712,-1.92497,-2.42125,-2.8477,-4.72301],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (89.4044,'kcal/mol','+|-',4.17612),
        S298 = (-8.48225,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 371,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_N-Sp-6R!H-3R!H",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {6,[B,D,T,Q]}
4   C u0 {3,S} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]}
6   C ux {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.03923,-3.06377,-2.6565,-2.54856,-2.66404,-2.78178,-3.14234],'cal/mol/K','+|-',[0.928066,0.132268,0.980011,1.36663,1.6154,1.08033,1.11283]),
        H298 = (86.0549,'kcal/mol','+|-',1.32143),
        S298 = (-2.93657,'cal/mol/K','+|-',1.14984),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 372,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_N-Sp-6R!H-3R!H_Sp-5O-4BrCClFINPSSi",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {6,[B,D,T,Q]}
4   C u0 {3,S} {5,S}
5   O u0 {4,S}
6   C ux {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.22672,-3.03705,-2.45851,-2.27246,-2.33768,-2.56352,-3.36716],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (85.9225,'kcal/mol','+|-',1.69706),
        S298 = (-2.70427,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 373,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_N-Sp-6R!H-3R!H_N-Sp-5O-4BrCClFINPSSi",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {6,[B,D,T,Q]}
4   C u0 {3,S} {5,D}
5   O u0 {4,D}
6   C ux {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.57048,-3.13057,-3.15148,-3.23881,-3.47994,-3.32743,-2.58027],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.8569,'kcal/mol','+|-',4.17612),
        S298 = (-3.51733,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 374,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26484,-2.58053,-3.45746,-4.00251,-4.49351,-4.90323,-5.80958],'cal/mol/K','+|-',[3.14622,2.93056,2.93198,2.7428,2.35035,2.19923,1.68107]),
        H298 = (86.4764,'kcal/mol','+|-',9.76103),
        S298 = (-2.42975,'cal/mol/K','+|-',4.20857),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 375,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,T}
5   C ux {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.6471,-3.73861,-4.37426,-4.59811,-4.76066,-5.14458,-6.32263],'cal/mol/K','+|-',[1.60552,0.273559,0.623371,0.655906,0.841806,0.800662,0.0722593]),
        H298 = (90.6128,'kcal/mol','+|-',0.508524),
        S298 = (-1.03391,'cal/mol/K','+|-',0.50917),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 376,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux r0 {3,S} {5,T}
5   C   ux r0 {4,T}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07946,-3.6419,-4.59465,-4.83001,-5.05829,-5.42766,-6.34818],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.433,'kcal/mol','+|-',4.17612),
        S298 = (-1.21393,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 377,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_N-Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,[S,D]}
5   C ux {4,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.343333,-1.80847,-2.84626,-3.60545,-4.31541,-4.74233,-5.46754],'cal/mol/K','+|-',[2.40227,2.8632,3.37567,3.5307,3.19658,2.99405,1.97345]),
        H298 = (83.7188,'kcal/mol','+|-',8.73843),
        S298 = (-3.3603,'cal/mol/K','+|-',4.72288),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 378,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_N-Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   u0 {3,S} {5,[S,D]}
5   C   u0 {4,[S,D]}
6   R!H ux {3,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.364314,-1.63605,-3.16335,-4.13876,-5.04118,-5.32579,-5.99883],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.9308,'kcal/mol','+|-',4.17612),
        S298 = (-4.54327,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 379,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_N-Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi_Sp-5C-4BrCClFINPSSi",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.73019,-3.31848,-4.35306,-5.04266,-5.42205,-5.85977,-6.07477],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.0179,'kcal/mol','+|-',4.17612),
        S298 = (-0.641183,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 380,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_N-Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi_N-Sp-5C-4BrCClFINPSSi",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.335874,-0.470894,-1.02236,-1.63493,-2.48301,-3.04143,-4.32901],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (79.2077,'kcal/mol','+|-',4.17612),
        S298 = (-4.89645,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(=C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 381,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_N-Sp-4BrCClFINPSSi-3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.70401,-4.03932,-4.04618,-3.99414,-3.59261,-3.03301,-2.08553],'cal/mol/K','+|-',[6.09784,5.83866,5.23601,4.48163,3.58197,2.97951,0.888462]),
        H298 = (85.0573,'kcal/mol','+|-',3.02457),
        S298 = (4.46378,'cal/mol/K','+|-',26.2516),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 382,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_N-Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   C   ux {3,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.93595,-5.21891,-5.10402,-4.89957,-4.31627,-3.63496,-2.26503],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (84.7542,'kcal/mol','+|-',1.69706),
        S298 = (-0.839846,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O)=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_1R-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing_1R->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing_N-1R->C
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing_N-1R->C_6R!H->C
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing_N-1R->C_6R!H->C_Ext-2R!H-R
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Ext-4C-R_N-1R-inRing_N-1R->C_N-6R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_1R-inRing
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_1R-inRing_Ext-2R!H-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_1R-inRing_Ext-3R!H-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_1R-inRing_Ext-5C-R_Ext-6R!H-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_1R-inRing_Ext-1R-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_N-1R-inRing
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_Sp-4C-3R!H_N-1R-inRing_Ext-2R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_Sp-5C-4C_N-Sp-4C-3R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_N-Sp-5C-4C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_N-Sp-5C-4C_1R-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_4R!H->C_N-Sp-5C-4C_N-1R-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_N-4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_5C-inRing_N-4R!H->C_Ext-3R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-5C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-5C-inRing_1R-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-5C-inRing_N-1R-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_1R-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing_1R->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing_N-1R->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing_N-1R->C_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing_N-1R->C_4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R-inRing_N-1R->C_N-4R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-1R-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-1R-R_5R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-1R-R_N-5R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-1R-R_N-5R!H->C_3R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-1R-R_N-5R!H->C_N-3R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-3R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_Ext-1R-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_3R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_2R!H-inRing_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_N-3R!H->C
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_1R-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_1R-inRing_Ext-2R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R_4R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R_N-4R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R_N-4R!H->O_4C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_Ext-1R-R_N-4R!H->O_N-4C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_4R!H-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_N-4R!H-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_N-4R!H-inRing_Ext-4R!H-R_Ext-4R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_N-4R!H-inRing_Sp-2R!H-1R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_N-4R!H-inRing_Sp-2R!H-1R_Ext-2R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_Ext-1R-R_N-1R-inRing_N-4R!H-inRing_N-Sp-2R!H-1R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_4R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_7R!H->O
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_N-7R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_N-7R!H->O_Ext-5R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_3R!H->O_N-1R->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-2R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-3C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-3C_4R!H->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-3C_N-4R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H-3C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H-3C_Sp-4R!H-1C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H-3C_N-Sp-4R!H-1C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Sp-4R!H-1C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Sp-4R!H-1C_Ext-1C-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Sp-4R!H-1C_5R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_Sp-4R!H-1C_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_Ext-3C-R_N-Sp-4R!H-1C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-4O-R
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_7R!H->C
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_N-7R!H->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Sp-4O-1C
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-Sp-4O-1C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-2R!H-R_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_4R!H->O_Ext-1C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-1C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C_Ext-2R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_7R!H->O
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-7R!H->O
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R_Ext-5C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_Sp-2R!H-1C_N-4R!H->O_Ext-4C-R_N-5R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Ext-1C-R_N-Sp-2R!H-1C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_7R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_N-7R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H-4R!H
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-4R!H-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-4R!H-R_7R!H->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-4R!H-R_N-7R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-3C-R_Ext-4R!H-R_N-Sp-6R!H-4R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_4R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H-6R!H
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_Sp-2R!H-1C_Ext-3C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_N-Sp-2R!H-1C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_1R->C_N-Sp-2R!H-1C_Ext-3C-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_5R!H->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_N-5R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O_4C-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_6R!H->O_N-4C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_N-6R!H->O
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_N-4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_N-4R!H->C_Ext-3C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-3C-R_4R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-3C-R_4R!H->C_4C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-3C-R_4R!H->C_N-4C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-3C-R_4R!H->C_N-4C-inRing_Ext-3C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-2R!H-inRing_N-3R!H->O_N-1R->C_Ext-3C-R_N-4R!H->C
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-2C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-2C-R_Ext-1R-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-3R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-3R!H-R_4R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-3R!H-R_N-4R!H->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-1R-R_4R!H-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R_Ext-1R-R_N-4R!H-inRing
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C_3O-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C_N-3O-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C_N-3O-inRing_4R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C_N-3O-inRing_N-4R!H->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_Int-4R!H-1C_N-3O-inRing_N-4R!H->C_Ext-2C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_1C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_1C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-3O_Ext-6R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_1C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-3O_Ext-6R!H-R_4R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_1C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-3O_Ext-6R!H-R_N-4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_5O-inRing
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_5O-inRing_Ext-3O-R
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_Ext-5O-R
                                                            L16: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_Ext-5O-R_Ext-4C-R
                                                            L16: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_Ext-5O-R_Ext-2C-R
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_Ext-1C-R
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_2C-inRing
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_4R!H->C_N-2C-inRing
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_Sp-5O-4R!H_N-5O-inRing_N-4R!H->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_N-Sp-5O-4R!H
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_N-Sp-5O-4R!H_Ext-3O-R_Int-6R!H-2C_Int-6R!H-3O_Sp-6R!H-1C
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_5R!H->O_N-Sp-5O-4R!H_Ext-3O-R_Int-6R!H-2C_Int-6R!H-3O_N-Sp-6R!H-1C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_2C-inRing
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing_Ext-3O-R
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing_Ext-3O-R_6R!H->N
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing_Ext-3O-R_N-6R!H->N
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing_Ext-3O-R_N-6R!H->N_Ext-6BrCClFIOPSSi-R_7R!H-inRing
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_Ext-4R!H-R_N-5R!H->O_N-2C-inRing_Ext-3O-R_N-6R!H->N_Ext-6BrCClFIOPSSi-R_N-7R!H-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_2C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_N-2C-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_N-2C-inRing_Ext-2C-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_N-2C-inRing_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-7R!H-R_9R!H->O
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_3R!H->O_N-1C-inRing_N-2C-inRing_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-7R!H-R_N-9R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-2C-R_Ext-1C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-1C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-1C-R_3C-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-1C-R_3C-inRing_1C-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-1C-R_3C-inRing_N-1C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_Ext-1C-R_N-3C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_2C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_2C-inRing_Ext-4R!H-R_Sp-5R!H=4R!H
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_2C-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_2C-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-4R!H-3C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_N-2C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_N-2C-inRing_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_N-2C-inRing_Ext-3C-R_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_N-2C-inRing_Ext-3C-R_5R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-2C-R_N-3R!H->O_N-2C-inRing_Ext-3C-R_N-5R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing_Ext-4R!H-R_Ext-5R!H-R_5R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-1C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-5R!H->C_3R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_1C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-5R!H->C_N-3R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C_4R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C_N-4R!H->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C_N-4R!H->C_Ext-3C-R
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C_N-4R!H->C_Ext-3C-R_5R!H->C
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_3R!H->C_N-4R!H->C_Ext-3C-R_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_N-3R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_N-3R!H->C_Ext-3O-R_5R!H->O
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_N-3R!H->C_Ext-3O-R_5R!H->O_Ext-1C-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C_N-3R!H->C_Ext-3O-R_N-5R!H->O
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_N-Sp-4R!H-1C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Ext-1C-R_N-1C-inRing_N-Sp-4R!H-1C_Ext-3R!H-R_Ext-3R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C_Ext-3R!H-R_N-4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C_Ext-3R!H-R_N-4R!H->C_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C_Ext-3R!H-R_N-4R!H->C_Ext-3R!H-R_Ext-4BrClFINOPSSi-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_N-Sp-3R!H-2C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_Int-4R!H-2C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_Int-4R!H-2C_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_Int-4R!H-2C_Ext-2C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_Ext-4O-R_Ext-5R!H-R_Ext-2C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_2C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_N-2C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_N-2C-inRing_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4O-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_N-2C-inRing_Ext-4O-R_5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_3R!H-inRing_N-2C-inRing_Ext-4O-R_N-5R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_4R!H->O_N-3R!H-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-4BrCClFINPSSi-R_Sp-6R!H-4BrCClFINPSSi
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-4BrCClFINPSSi-R_Sp-6R!H-4BrCClFINPSSi_2C-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-4BrCClFINPSSi-R_Sp-6R!H-4BrCClFINPSSi_2C-inRing_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-4BrCClFINPSSi-R_Sp-6R!H-4BrCClFINPSSi_N-2C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-2C-R_Ext-4BrCClFINPSSi-R_N-Sp-6R!H-4BrCClFINPSSi
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_3R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_N-3R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H-4BrCClFINPSSi
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_3R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C_Ext-3R!H-R_N-4R!H->O_N-3R!H->C
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_4R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_4R!H->C_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_4R!H->C_Ext-1C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_N-4R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_N-4R!H->C_Int-4BrClFINOPSSi-3R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_N-4R!H->C_Ext-3R!H-R_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_N-4R!H->C_1C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-1C-R_N-4R!H->C_N-1C-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-3R!H-R_Ext-3R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C_Ext-3R!H-R_Ext-4R!H-R
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-4O-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-4O-R_Ext-5R!H-R_6R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-4O-R_Ext-5R!H-R_6R!H->O_3R!H-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-4O-R_Ext-5R!H-R_6R!H->O_N-3R!H-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-4O-R_Ext-5R!H-R_N-6R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_5C-inRing
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_5C-inRing_Ext-4BrCClFINPSSi-R
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_5C-inRing_3R!H-inRing
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_5C-inRing_N-3R!H-inRing
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Ext-4BrCClFINPSSi-R
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Ext-4BrCClFINPSSi-R_3R!H-inRing
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Ext-4BrCClFINPSSi-R_N-3R!H-inRing
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Ext-3R!H-R
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Ext-3R!H-R_Ext-5C-R
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Sp-6R!H-5C
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Sp-6R!H-5C_Ext-5C-R
                                                            L16: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Sp-6R!H-5C_Ext-5C-R_3R!H-inRing
                                                            L16: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Sp-6R!H-5C_Ext-5C-R_N-3R!H-inRing
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_Sp-6R!H-5C_Ext-6R!H-R_Ext-6R!H-R
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_N-Sp-6R!H-5C
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_N-Sp-6R!H-5C_7R!H->C
                                                        L15: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_5R!H->C_N-5C-inRing_N-Sp-6R!H-5C_N-7R!H->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_N-5R!H->C
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_N-5R!H->C_3R!H-inRing
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_N-5R!H->C_3R!H-inRing_Ext-4BrCClFINPSSi-R
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_N-5R!H->C_N-3R!H-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R_N-Sp-5R!H-4BrCClFINPSSi
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_Ext-6R!H-R
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_Ext-6R!H-R_6R!H->C
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_Ext-6R!H-R_N-6R!H->C
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_Ext-6R!H-R_N-6R!H->C_3R!H-inRing
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_Ext-6R!H-R_N-6R!H->C_N-3R!H-inRing
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_3R!H-inRing
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R_N-3R!H-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_Sp-6R!H-3R!H
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-4BrCClFINPSSi-R
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_N-Sp-6R!H-3R!H
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_N-Sp-6R!H-3R!H_Sp-5O-4BrCClFINPSSi
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_5R!H->O_Ext-3R!H-R_N-Sp-6R!H-3R!H_N-Sp-5O-4BrCClFINPSSi
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_N-Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_N-Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi_Ext-3R!H-R_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_N-Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi_Sp-5C-4BrCClFINPSSi
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->O_N-Sp-5C#4BrBrBrCCCClClClFFFIIINNNPPPSSSSiSiSi_N-Sp-5C-4BrCClFINPSSi
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_N-Sp-4BrCClFINPSSi-3R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_N-Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R
"""
)

