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
        Cpdata = ([-0.66105,-1.70106,-2.3855,-2.76323,-3.15647,-3.48289,-4.29641],'cal/mol/K','+|-',[3.89053,4.38141,4.58213,4.42489,3.90292,3.73769,4.02718]),
        H298 = (92.9694,'kcal/mol','+|-',29.6292),
        S298 = (0.623468,'cal/mol/K','+|-',9.86056),
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
        Cpdata = ([-0.66105,-1.70106,-2.3855,-2.76323,-3.15647,-3.48289,-4.29641],'cal/mol/K','+|-',[3.89053,4.38141,4.58213,4.42489,3.90292,3.73769,4.02718]),
        H298 = (92.9694,'kcal/mol','+|-',29.6292),
        S298 = (0.623468,'cal/mol/K','+|-',9.86056),
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
        Cpdata = ([-0.546591,-1.4289,-2.01477,-2.29638,-2.59579,-2.83782,-3.6172],'cal/mol/K','+|-',[3.61077,4.32154,4.56197,4.25211,3.47673,3.28324,3.93691]),
        H298 = (86.325,'kcal/mol','+|-',36.141),
        S298 = (0.194416,'cal/mol/K','+|-',10.8137),
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
        Cpdata = ([-0.319973,-1.08783,-1.71359,-2.15176,-2.77545,-3.22761,-4.10617],'cal/mol/K','+|-',[2.7845,2.89984,3.21474,3.23041,3.48276,3.9184,4.74076]),
        H298 = (81.4816,'kcal/mol','+|-',60.9297),
        S298 = (0.826179,'cal/mol/K','+|-',9.50064),
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
        Cpdata = ([-0.754392,-1.52023,-2.11406,-2.50802,-3.02639,-3.42598,-4.30404],'cal/mol/K','+|-',[2.8561,2.91928,3.00613,2.71115,2.38218,2.35809,2.31829]),
        H298 = (84.6907,'kcal/mol','+|-',39.6847),
        S298 = (0.434762,'cal/mol/K','+|-',11.2606),
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
        Cpdata = ([-0.453005,-1.28244,-1.95983,-2.40174,-2.98871,-3.41884,-4.34704],'cal/mol/K','+|-',[2.70378,2.73086,2.89714,2.61053,2.34289,2.32456,2.39929]),
        H298 = (88.8709,'kcal/mol','+|-',37.3921),
        S298 = (1.05497,'cal/mol/K','+|-',11.702),
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
        Cpdata = ([-0.567843,-1.42078,-2.09303,-2.5384,-3.14588,-3.58578,-4.50755],'cal/mol/K','+|-',[2.59407,2.59201,2.81751,2.48903,2.0964,2.01425,2.06741]),
        H298 = (89.9856,'kcal/mol','+|-',36.1294),
        S298 = (0.450356,'cal/mol/K','+|-',8.06162),
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
        Cpdata = ([-0.527752,-1.37754,-2.05221,-2.49692,-3.11245,-3.56359,-4.42912],'cal/mol/K','+|-',[2.75209,2.66882,2.9028,2.56223,2.20221,2.1575,2.08096]),
        H298 = (85.6217,'kcal/mol','+|-',29.0216),
        S298 = (-0.0854951,'cal/mol/K','+|-',7.2387),
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
        Cpdata = ([-0.538041,-1.44182,-2.13754,-2.58682,-3.19526,-3.62191,-4.44788],'cal/mol/K','+|-',[2.99545,2.88013,3.12434,2.74897,2.34604,2.31092,2.25638]),
        H298 = (80.5148,'kcal/mol','+|-',13.4715),
        S298 = (-0.081482,'cal/mol/K','+|-',7.89222),
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
        Cpdata = ([-1.69739,-3.13973,-3.92423,-3.96155,-3.89198,-3.87997,-4.20124],'cal/mol/K','+|-',[2.05644,2.86259,3.16191,2.74336,2.05882,1.95914,2.58743]),
        H298 = (76.8708,'kcal/mol','+|-',20.0597),
        S298 = (1.08854,'cal/mol/K','+|-',10.9955),
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
        Cpdata = ([-1.83075,-3.41628,-4.18364,-4.18827,-4.04584,-3.83501,-4.23058],'cal/mol/K','+|-',[2.41651,2.69811,2.71939,2.5928,2.32894,2.38077,3.07162]),
        H298 = (78.0348,'kcal/mol','+|-',13.9354),
        S298 = (3.40757,'cal/mol/K','+|-',8.08291),
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
        Cpdata = ([-2.02381,-3.74949,-4.50269,-4.48064,-4.16395,-3.80138,-4.12792],'cal/mol/K','+|-',[2.65167,2.72428,2.79575,2.6831,2.63967,2.76435,3.61469]),
        H298 = (75.8759,'kcal/mol','+|-',13.2862),
        S298 = (4.53316,'cal/mol/K','+|-',8.17067),
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
        Cpdata = ([-2.11897,-3.53872,-4.24867,-4.31906,-4.01113,-3.55826,-4.66414],'cal/mol/K','+|-',[3.24223,3.23169,3.27879,3.23081,3.16889,3.24521,3.9872]),
        H298 = (72.5113,'kcal/mol','+|-',8.35056),
        S298 = (5.98724,'cal/mol/K','+|-',8.91303),
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
        Cpdata = ([-0.0652128,-0.725174,-1.36453,-1.91295,-2.69224,-3.25248,-4.31506],'cal/mol/K','+|-',[3.20205,1.56567,1.76467,2.04517,2.08812,1.97531,1.69168]),
        H298 = (80.7545,'kcal/mol','+|-',9.95977),
        S298 = (-0.987431,'cal/mol/K','+|-',5.929),
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
        Cpdata = ([0.134906,-0.805265,-1.61273,-2.21937,-3.0289,-3.5755,-4.58194],'cal/mol/K','+|-',[3.77304,1.73233,1.57226,1.82299,1.88096,1.83308,1.62767]),
        H298 = (78.6722,'kcal/mol','+|-',7.39135),
        S298 = (-0.634835,'cal/mol/K','+|-',6.99588),
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
        Cpdata = ([-0.608391,-0.507786,-0.69083,-1.08124,-1.77845,-2.3757,-3.59066],'cal/mol/K','+|-',[2.40845,2.72475,3.11642,3.20562,2.93306,2.63097,2.43679]),
        H298 = (86.706,'kcal/mol','+|-',3.33359),
        S298 = (-1.94448,'cal/mol/K','+|-',2.96458),
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
        Cpdata = ([-0.468957,-1.01024,-1.56461,-1.9832,-2.63927,-3.23033,-4.3219],'cal/mol/K','+|-',[2.44008,2.49783,2.47519,2.39066,2.51876,2.60231,2.48438]),
        H298 = (110.392,'kcal/mol','+|-',51.4852),
        S298 = (-0.108427,'cal/mol/K','+|-',2.41928),
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
        Cpdata = ([-0.837028,-1.71111,-2.36707,-2.81694,-3.37038,-3.73484,-5.03413],'cal/mol/K','+|-',[2.87465,3.84695,4.07288,3.75874,2.96228,2.47074,3.46174]),
        H298 = (115.516,'kcal/mol','+|-',51.2061),
        S298 = (4.04821,'cal/mol/K','+|-',14.4475),
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
        Cpdata = ([1.09731,0.5852,-0.161653,-0.556789,-0.866855,-1.16506,-2.18026],'cal/mol/K','+|-',[4.34553,3.72013,3.287,3.19893,3.16421,3.34997,4.32161]),
        H298 = (61.9321,'kcal/mol','+|-',32.2114),
        S298 = (9.21728,'cal/mol/K','+|-',39.113),
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
        Cpdata = ([-2.09904,-2.58114,-2.80214,-2.98219,-3.19452,-3.45785,-4.11216],'cal/mol/K','+|-',[2.61761,3.59902,3.93988,3.78072,3.37725,3.35733,2.79494]),
        H298 = (63.7666,'kcal/mol','+|-',22.2659),
        S298 = (-2.33233,'cal/mol/K','+|-',8.11345),
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
        Cpdata = ([-1.76779,-2.03906,-2.20414,-2.41137,-2.70126,-2.96848,-3.73906],'cal/mol/K','+|-',[2.09624,2.3162,2.50812,2.4281,2.29415,2.28771,2.12781]),
        H298 = (66.5615,'kcal/mol','+|-',5.25847),
        S298 = (-3.6596,'cal/mol/K','+|-',4.30909),
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
        Cpdata = ([-1.73375,-2.0137,-2.24701,-2.4658,-2.67603,-2.93138,-3.67341],'cal/mol/K','+|-',[2.34234,2.6259,2.8595,2.75125,2.59808,2.58463,2.35807]),
        H298 = (66.5466,'kcal/mol','+|-',6.10636),
        S298 = (-3.17171,'cal/mol/K','+|-',4.12155),
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
        Cpdata = ([0.614687,-0.157514,-0.851982,-1.38525,-2.23553,-2.80081,-3.68045],'cal/mol/K','+|-',[1.78983,2.16536,3.32092,4.04811,5.31326,6.3631,8.11096]),
        H298 = (75.8279,'kcal/mol','+|-',90.9953),
        S298 = (1.66832,'cal/mol/K','+|-',3.66538),
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
        Cpdata = ([0.51047,0.264091,-0.191835,-0.644674,-1.37211,-1.89798,-2.64425],'cal/mol/K','+|-',[1.61204,1.57312,2.3837,3.18036,4.62481,5.86592,7.9931]),
        H298 = (70.4411,'kcal/mol','+|-',92.6727),
        S298 = (1.42452,'cal/mol/K','+|-',3.00548),
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
        Cpdata = ([0.14959,0.227321,0.00312447,-0.312634,-0.810153,-1.13427,-1.51382],'cal/mol/K','+|-',[1.6383,2.0917,3.19434,4.23747,6.11667,7.71361,10.3943]),
        H298 = (51.752,'kcal/mol','+|-',109.243),
        S298 = (0.654455,'cal/mol/K','+|-',2.88576),
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
        Cpdata = ([0.162222,-0.12911,-0.782285,-1.43659,-2.50948,-3.30965,-4.47713],'cal/mol/K','+|-',[2.0077,2.08999,2.06627,2.06405,2.04667,2.02295,2.00025]),
        H298 = (83.2745,'kcal/mol','+|-',4.27249),
        S298 = (1.00991,'cal/mol/K','+|-',3.50563),
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
        Cpdata = ([0.940365,-1.47503,-2.91494,-3.69956,-4.93372,-5.62215,-6.91856],'cal/mol/K','+|-',[3.23403,2.55145,2.90384,3.40112,4.1408,5.25846,5.72106]),
        H298 = (116.603,'kcal/mol','+|-',12.605),
        S298 = (2.4302,'cal/mol/K','+|-',5.88718),
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
        Cpdata = ([1.47282,-1.33565,-3.08417,-4.05762,-5.57969,-6.53739,-7.92459],'cal/mol/K','+|-',[2.83743,2.90952,3.33583,3.66623,3.85633,4.53211,4.89613]),
        H298 = (114.178,'kcal/mol','+|-',9.71483),
        S298 = (1.30187,'cal/mol/K','+|-',4.53868),
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
        Cpdata = ([-0.646457,-1.5792,-2.14749,-2.36011,-2.51662,-2.66605,-3.40173],'cal/mol/K','+|-',[3.9449,4.8244,5.05986,4.66736,3.51374,2.95831,3.50506]),
        H298 = (88.4221,'kcal/mol','+|-',16.3029),
        S298 = (-0.0839879,'cal/mol/K','+|-',11.3787),
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
        Cpdata = ([-0.474306,-1.21548,-1.88049,-2.26253,-2.66226,-2.95031,-3.98089],'cal/mol/K','+|-',[3.48894,4.48923,5.22391,5.35522,4.43901,3.4404,3.92343]),
        H298 = (93.6889,'kcal/mol','+|-',16.2174),
        S298 = (-0.358862,'cal/mol/K','+|-',6.80205),
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
        Cpdata = ([-1.19238,-2.12816,-2.77813,-3.00758,-3.12228,-3.19737,-3.89226],'cal/mol/K','+|-',[3.64244,4.88071,5.99463,6.3392,5.40535,4.28272,4.72478]),
        H298 = (89.5118,'kcal/mol','+|-',18.0748),
        S298 = (0.0537395,'cal/mol/K','+|-',8.81389),
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
        Cpdata = ([0.214718,-0.707453,-1.62458,-2.15475,-2.60433,-2.97702,-4.29846],'cal/mol/K','+|-',[2.99102,2.63565,2.39306,2.39256,2.39197,2.4169,3.12472]),
        H298 = (98.4578,'kcal/mol','+|-',7.6958),
        S298 = (0.869286,'cal/mol/K','+|-',2.46522),
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
        Cpdata = ([-1.5207,-2.45966,-3.04729,-3.20657,-3.24314,-3.24878,-3.79747],'cal/mol/K','+|-',[3.71524,5.2303,6.61564,7.0681,6.05466,4.81089,5.2544]),
        H298 = (87.3519,'kcal/mol','+|-',17.376),
        S298 = (-0.136555,'cal/mol/K','+|-',9.87715),
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
        Cpdata = ([-1.72536,-3.73478,-4.82305,-5.07826,-4.81646,-4.37666,-3.92795],'cal/mol/K','+|-',[4.42948,5.97205,7.91754,8.49918,6.83266,5.14165,7.29118]),
        H298 = (80.6985,'kcal/mol','+|-',15.0929),
        S298 = (0.568486,'cal/mol/K','+|-',12.0015),
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
        Cpdata = ([-1.00444,-3.06674,-4.3393,-4.59222,-4.4329,-3.90955,-2.01664],'cal/mol/K','+|-',[7.24262,5.83273,4.64352,4.56917,4.33245,3.58486,2.53368]),
        H298 = (75.157,'kcal/mol','+|-',9.95444),
        S298 = (-2.22066,'cal/mol/K','+|-',14.0986),
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
        Cpdata = ([-2.44629,-4.40281,-5.30679,-5.5643,-5.20001,-4.84377,-5.83927],'cal/mol/K','+|-',[2.57277,9.04707,13.8454,15.0093,11.8736,8.69769,10.342]),
        H298 = (86.24,'kcal/mol','+|-',7.05429),
        S298 = (3.35763,'cal/mol/K','+|-',12.1346),
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
        Cpdata = ([-1.55362,-1.5781,-1.65487,-1.71127,-1.97079,-2.30941,-3.25189],'cal/mol/K','+|-',[4.06152,4.3447,4.49212,4.84721,5.03433,4.81204,3.63578]),
        H298 = (94.0683,'kcal/mol','+|-',5.21758),
        S298 = (-0.730241,'cal/mol/K','+|-',10.4961),
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
        Cpdata = ([-2.31201,-1.8654,-1.80664,-1.85543,-2.08712,-2.45037,-3.54191],'cal/mol/K','+|-',[2.7603,2.39861,2.44205,2.54593,2.77938,2.90099,2.66517]),
        H298 = (92.6324,'kcal/mol','+|-',4.11181),
        S298 = (0.702446,'cal/mol/K','+|-',3.90774),
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
        Cpdata = ([0.659362,0.173862,-0.522761,-1.11215,-1.89228,-2.46372,-3.97444],'cal/mol/K','+|-',[2.09268,2.41798,2.91365,3.19519,2.68602,2.01751,3.14817]),
        H298 = (98.0181,'kcal/mol','+|-',4.78548),
        S298 = (-0.872104,'cal/mol/K','+|-',3.47299),
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
        Cpdata = ([0.686987,-0.0307198,-0.831336,-1.46079,-2.15349,-2.6055,-4.2452],'cal/mol/K','+|-',[2.4918,3.00203,3.62841,3.99444,3.39232,2.58155,4.04981]),
        H298 = (99.595,'kcal/mol','+|-',2.40704),
        S298 = (-0.251079,'cal/mol/K','+|-',3.95361),
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
        Cpdata = ([0.953541,0.319817,-0.390247,-0.980945,-1.80107,-2.32905,-3.66195],'cal/mol/K','+|-',[1.95103,2.15084,2.46996,2.77975,2.76432,2.02357,1.63419]),
        H298 = (99.4594,'kcal/mol','+|-',2.0262),
        S298 = (-0.716347,'cal/mol/K','+|-',2.83352),
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
        Cpdata = ([1.22503,0.723878,0.141574,-0.333616,-1.15734,-1.98548,-3.66118],'cal/mol/K','+|-',[2.12383,2.00013,2.01991,2.01589,2.0011,2.00585,2.00195]),
        H298 = (99.3115,'kcal/mol','+|-',2.40121),
        S298 = (-1.38479,'cal/mol/K','+|-',2.00018),
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
        Cpdata = ([-0.713292,-1.72041,-2.25115,-2.39799,-2.46007,-2.55569,-3.17687],'cal/mol/K','+|-',[4.16647,4.99358,5.06665,4.4681,3.17752,2.80493,3.30436]),
        H298 = (86.0164,'kcal/mol','+|-',14.1694),
        S298 = (0.022728,'cal/mol/K','+|-',12.7896),
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
        Cpdata = ([-0.270457,-0.983626,-1.50493,-1.79879,-2.18227,-2.50558,-3.27956],'cal/mol/K','+|-',[3.38929,3.02521,2.82554,2.58558,2.26194,2.32517,2.69923]),
        H298 = (85.8862,'kcal/mol','+|-',11.9893),
        S298 = (-0.75505,'cal/mol/K','+|-',10.9352),
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
        Cpdata = ([-0.622828,-1.42888,-1.93968,-2.17674,-2.41484,-2.58128,-3.12352],'cal/mol/K','+|-',[3.27494,2.90605,2.82722,2.7357,2.61709,2.74972,3.10644]),
        H298 = (84.4033,'kcal/mol','+|-',15.2043),
        S298 = (0.0555571,'cal/mol/K','+|-',13.1804),
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
        Cpdata = ([-0.689159,-1.50077,-2.01274,-2.24575,-2.47812,-2.64329,-3.1834],'cal/mol/K','+|-',[3.20037,2.78721,2.69724,2.61773,2.51652,2.66293,3.04637]),
        H298 = (84.3418,'kcal/mol','+|-',15.2808),
        S298 = (-0.535604,'cal/mol/K','+|-',10.8417),
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
        Cpdata = ([-0.93822,-1.86188,-2.31459,-2.51102,-2.64492,-2.67354,-2.85217],'cal/mol/K','+|-',[3.5442,3.70142,3.74649,3.42027,2.89245,2.99679,3.98948]),
        H298 = (85.2626,'kcal/mol','+|-',23.2384),
        S298 = (0.791641,'cal/mol/K','+|-',13.4551),
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
        Cpdata = ([0.370415,-0.47783,-1.0655,-1.48191,-2.0978,-2.48328,-3.07354],'cal/mol/K','+|-',[3.26782,2.55482,2.23369,2.19148,2.22791,2.44048,3.01341]),
        H298 = (84.7748,'kcal/mol','+|-',6.46466),
        S298 = (2.56966,'cal/mol/K','+|-',19.2704),
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
        Cpdata = ([-0.114559,-0.356075,-0.65986,-1.02792,-1.71068,-2.14357,-2.7072],'cal/mol/K','+|-',[3.22975,3.31533,3.33582,3.3076,3.25265,3.16747,3.85358]),
        H298 = (81.6074,'kcal/mol','+|-',6.52012),
        S298 = (-3.43047,'cal/mol/K','+|-',3.68287),
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
        Cpdata = ([0.0163474,-0.937965,-1.45559,-1.85058,-2.35276,-2.63972,-3.12887],'cal/mol/K','+|-',[3.92404,3.08549,2.87111,2.84737,3.20855,3.83119,4.62752]),
        H298 = (84.9227,'kcal/mol','+|-',3.89041),
        S298 = (8.48855,'cal/mol/K','+|-',22.687),
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
        Cpdata = ([-0.757146,-1.98301,-2.60612,-2.84859,-2.92875,-2.97612,-3.58133],'cal/mol/K','+|-',[2.91133,3.95341,5.12065,5.27295,4.85219,4.35524,3.84195]),
        H298 = (85.7745,'kcal/mol','+|-',8.35782),
        S298 = (0.235196,'cal/mol/K','+|-',8.10276),
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
        Cpdata = ([-0.711919,-1.08893,-1.46536,-1.65452,-1.92409,-2.22947,-3.16892],'cal/mol/K','+|-',[3.24398,2.15546,1.94784,2.28338,2.68609,2.96976,2.78766]),
        H298 = (82.4189,'kcal/mol','+|-',7.90057),
        S298 = (-1.69096,'cal/mol/K','+|-',7.2392),
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
        Cpdata = ([-0.845926,-1.24079,-1.54949,-1.70502,-1.88782,-2.0927,-3.00559],'cal/mol/K','+|-',[3.54658,2.41799,2.26598,2.68293,3.15618,3.45709,3.22414]),
        H298 = (83.9104,'kcal/mol','+|-',7.87804),
        S298 = (-1.82378,'cal/mol/K','+|-',8.50622),
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
        Cpdata = ([-0.976461,-1.37399,-1.69045,-1.86409,-2.04935,-2.23615,-3.07581],'cal/mol/K','+|-',[3.68016,2.39983,2.1983,2.63345,3.17435,3.55588,3.41154]),
        H298 = (83.6394,'kcal/mol','+|-',7.83731),
        S298 = (-1.71761,'cal/mol/K','+|-',9.09104),
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
        Cpdata = ([-0.971392,-1.18321,-1.36565,-1.49345,-1.76986,-2.0462,-2.87041],'cal/mol/K','+|-',[2.8846,3.22196,3.39655,3.32734,3.07307,3.03195,3.73297]),
        H298 = (81.7687,'kcal/mol','+|-',5.58541),
        S298 = (-2.22945,'cal/mol/K','+|-',4.68608),
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
        Cpdata = ([-0.86246,-1.10804,-1.32184,-1.43408,-1.65954,-1.8779,-2.54219],'cal/mol/K','+|-',[3.60883,4.1585,4.43776,4.32718,3.90666,3.79109,4.68523]),
        H298 = (82.0924,'kcal/mol','+|-',6.9464),
        S298 = (-2.42637,'cal/mol/K','+|-',6.2972),
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
        Cpdata = ([-1.34791,-1.73073,-2.07781,-2.32219,-2.54732,-2.82696,-3.68107],'cal/mol/K','+|-',[5.34772,2.76172,2.09723,3.07013,4.19187,4.44918,3.57106]),
        H298 = (84.2921,'kcal/mol','+|-',9.79613),
        S298 = (0.520922,'cal/mol/K','+|-',5.63501),
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
        Cpdata = ([-0.23503,-1.44287,-2.23856,-2.59296,-2.94249,-3.15051,-3.76602],'cal/mol/K','+|-',[3.53932,2.54355,1.99714,1.94711,2.19086,2.42224,2.17398]),
        H298 = (85.4999,'kcal/mol','+|-',2.90839),
        S298 = (-1.23219,'cal/mol/K','+|-',11.1077),
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
        Cpdata = ([0.441991,-1.07775,-2.05236,-2.45035,-2.77976,-2.9527,-3.56638],'cal/mol/K','+|-',[3.71331,2.82577,2.16175,2.15305,2.56896,2.91161,2.51434]),
        H298 = (84.9427,'kcal/mol','+|-',2.84696),
        S298 = (-2.29999,'cal/mol/K','+|-',13.6876),
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
        Cpdata = ([1.30823,-0.541344,-1.82855,-2.22072,-2.30181,-2.25425,-2.98473],'cal/mol/K','+|-',[4.92375,3.93996,3.16822,3.05528,3.03274,3.06406,3.00129]),
        H298 = (84.9044,'kcal/mol','+|-',5.01542),
        S298 = (-7.53171,'cal/mol/K','+|-',7.87177),
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
        Cpdata = ([2.09855,0.0237156,-1.53957,-1.92049,-1.89473,-1.77866,-2.69588],'cal/mol/K','+|-',[5.49206,4.47775,3.83896,3.62945,3.32935,3.16469,3.56085]),
        H298 = (84.724,'kcal/mol','+|-',6.15638),
        S298 = (-9.43181,'cal/mol/K','+|-',5.8264),
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
        Cpdata = ([0.178439,-0.395929,-0.890875,-1.20023,-1.68411,-2.17869,-3.28857],'cal/mol/K','+|-',[3.85187,3.21585,2.77607,2.30957,1.61833,1.63142,2.14005]),
        H298 = (87.4225,'kcal/mol','+|-',5.14685),
        S298 = (-2.54602,'cal/mol/K','+|-',6.23854),
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
        Cpdata = ([0.380435,-0.0871046,-0.590008,-0.959183,-1.62649,-2.2606,-3.55929],'cal/mol/K','+|-',[3.35305,2.62916,2.00038,1.77966,1.71729,1.77393,1.84764]),
        H298 = (87.8336,'kcal/mol','+|-',4.05315),
        S298 = (-1.70406,'cal/mol/K','+|-',3.95759),
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
        Cpdata = ([0.0649674,-0.224322,-0.582104,-0.884461,-1.48804,-2.08204,-3.35379],'cal/mol/K','+|-',[3.09687,2.73442,2.17256,1.87266,1.64654,1.58039,1.52194]),
        H298 = (87.7889,'kcal/mol','+|-',4.19001),
        S298 = (-1.26238,'cal/mol/K','+|-',3.36372),
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
        Cpdata = ([0.461357,0.0373415,-0.483868,-0.894099,-1.64518,-2.30317,-3.60499],'cal/mol/K','+|-',[2.7109,3.72186,3.90276,3.75219,3.40235,3.07161,2.7487]),
        H298 = (86.494,'kcal/mol','+|-',8.77099),
        S298 = (-2.68545,'cal/mol/K','+|-',2.45899),
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
        Cpdata = ([0.28593,-0.00125416,-0.35337,-0.646501,-1.24062,-1.84621,-3.16205],'cal/mol/K','+|-',[4.06458,3.32115,2.3337,1.85917,1.65601,1.75343,1.87045]),
        H298 = (88.4412,'kcal/mol','+|-',4.42696),
        S298 = (-1.15076,'cal/mol/K','+|-',3.63095),
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
        Cpdata = ([-0.4932,-0.569681,-0.604495,-0.726929,-1.16123,-1.7421,-3.21594],'cal/mol/K','+|-',[4.13995,3.60169,2.83645,2.32905,2.00003,2.13437,2.36519]),
        H298 = (88.7471,'kcal/mol','+|-',5.91856),
        S298 = (-0.710294,'cal/mol/K','+|-',4.51421),
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
        Cpdata = ([-0.424108,-1.36402,-1.88839,-2.02609,-1.95901,-2.02646,-2.57121],'cal/mol/K','+|-',[6.11982,4.94038,4.43579,3.65966,2.47204,2.49783,3.28307]),
        H298 = (87.4117,'kcal/mol','+|-',10.0367),
        S298 = (-4.26564,'cal/mol/K','+|-',10.5916),
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
        Cpdata = ([-0.6541,-1.80433,-2.36295,-2.45219,-2.22377,-2.15575,-2.63851],'cal/mol/K','+|-',[6.78071,4.88654,4.07487,3.18398,2.21881,2.66227,3.66019]),
        H298 = (87.88,'kcal/mol','+|-',10.546),
        S298 = (-3.98959,'cal/mol/K','+|-',11.8937),
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
        Cpdata = ([2.50098,-0.150599,-1.54519,-2.02932,-1.9611,-1.87527,-1.90019],'cal/mol/K','+|-',[6.59759,5.18569,4.5068,3.62176,3.53249,4.63032,6.21776]),
        H298 = (86.6792,'kcal/mol','+|-',8.01702),
        S298 = (-9.86413,'cal/mol/K','+|-',9.74546),
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
        Cpdata = ([0.454632,-0.167716,-0.905438,-1.59475,-2.69293,-3.47892,-4.53057],'cal/mol/K','+|-',[2.17974,2.25712,2.33811,2.30507,2.20825,2.11252,2.00242]),
        H298 = (88.7547,'kcal/mol','+|-',4.31142),
        S298 = (1.29267,'cal/mol/K','+|-',2.00978),
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
        Cpdata = ([-2.9591,-5.45697,-6.03557,-5.43682,-3.86893,-2.80987,-2.65609],'cal/mol/K','+|-',[5.04997,6.35663,7.03281,6.78713,5.3507,4.76719,5.58629]),
        H298 = (87.2822,'kcal/mol','+|-',28.1773),
        S298 = (3.96717,'cal/mol/K','+|-',18.2477),
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
        Cpdata = ([-3.29741,-5.37064,-5.60343,-4.84183,-3.2194,-2.16852,-2.11368],'cal/mol/K','+|-',[5.86858,7.40366,7.79387,7.28708,5.47119,4.64519,5.13907]),
        H298 = (85.0619,'kcal/mol','+|-',32.5872),
        S298 = (2.44566,'cal/mol/K','+|-',16.1469),
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
        Cpdata = ([-3.4772,-6.09275,-6.63216,-5.89878,-3.96445,-2.70675,-2.37208],'cal/mol/K','+|-',[6.45804,7.49225,7.25849,6.5063,5.2157,4.88406,6.15709]),
        H298 = (94.746,'kcal/mol','+|-',11.146),
        S298 = (4.86027,'cal/mol/K','+|-',16.1055),
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
        Cpdata = ([-3.58478,-6.27765,-6.925,-6.24425,-4.3314,-3.12593,-2.78953],'cal/mol/K','+|-',[7.04014,8.13121,7.76186,6.83322,5.29384,4.75666,6.28816]),
        H298 = (95.604,'kcal/mol','+|-',11.136),
        S298 = (2.45017,'cal/mol/K','+|-',10.7704),
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
        Cpdata = ([-3.8659,-7.17608,-8.00329,-7.20875,-4.87596,-3.35257,-2.52945],'cal/mol/K','+|-',[8.8164,9.62452,8.77645,7.66009,6.19287,5.73163,7.84797]),
        H298 = (98.0908,'kcal/mol','+|-',8.95732),
        S298 = (2.88983,'cal/mol/K','+|-',13.297),
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
        Cpdata = ([-6.05771,-8.88893,-8.89813,-7.16722,-3.54578,-1.5732,0.236515],'cal/mol/K','+|-',[12.1963,14.8577,13.6857,11.2947,5.92129,3.28834,5.76861]),
        H298 = (96.5948,'kcal/mol','+|-',11.863),
        S298 = (-1.43879,'cal/mol/K','+|-',12.7557),
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
        Cpdata = ([-3.02255,-4.48079,-4.7684,-4.31525,-3.24227,-2.67265,-3.30969],'cal/mol/K','+|-',[4.37848,4.71995,4.76202,4.59503,4.3781,4.5213,4.24497]),
        H298 = (90.6306,'kcal/mol','+|-',10.5641),
        S298 = (1.57084,'cal/mol/K','+|-',6.97319),
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
        Cpdata = ([-2.87788,-3.68571,-3.20306,-2.37562,-1.48096,-0.912635,-1.51076],'cal/mol/K','+|-',[5.88147,7.75668,8.49374,8.1281,5.78149,4.27279,2.87025]),
        H298 = (62.4655,'kcal/mol','+|-',7.1546),
        S298 = (-3.18844,'cal/mol/K','+|-',11.3684),
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
        Cpdata = ([-2.37497,-6.15466,-7.82772,-7.68117,-6.19828,-5.17445,-4.77642],'cal/mol/K','+|-',[2.74032,4.03323,5.41221,5.32146,4.03667,3.7817,7.46752]),
        H298 = (93.3758,'kcal/mol','+|-',7.22243),
        S298 = (2.19792,'cal/mol/K','+|-',9.48864),
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
        Cpdata = ([-2.11021,-5.53388,-6.78765,-6.59548,-5.41495,-4.4043,-2.75676],'cal/mol/K','+|-',[3.16274,4.46675,5.41189,5.00133,3.81178,3.32174,3.20902]),
        H298 = (91.8414,'kcal/mol','+|-',6.01631),
        S298 = (-0.41677,'cal/mol/K','+|-',3.55767),
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
        Cpdata = ([-0.752188,-1.91778,-2.68069,-3.13496,-3.60292,-3.99653,-4.83722],'cal/mol/K','+|-',[4.11743,4.40962,4.54165,4.4472,4.01789,3.78404,3.7898]),
        H298 = (98.3634,'kcal/mol','+|-',16.7254),
        S298 = (0.965102,'cal/mol/K','+|-',9.02571),
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
        Cpdata = ([-0.100342,-1.24122,-2.08752,-2.6189,-3.23541,-3.74336,-4.82457],'cal/mol/K','+|-',[3.46427,3.86407,4.09377,3.97593,3.38876,3.117,3.08773]),
        H298 = (102.093,'kcal/mol','+|-',13.9001),
        S298 = (1.61666,'cal/mol/K','+|-',7.01251),
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
        Cpdata = ([-0.731104,-1.46325,-1.95707,-2.33084,-2.95747,-3.52514,-4.75723],'cal/mol/K','+|-',[3.60772,2.90346,2.53819,2.31526,1.96107,1.78859,1.95018]),
        H298 = (110.703,'kcal/mol','+|-',6.21284),
        S298 = (1.93798,'cal/mol/K','+|-',4.61792),
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
        Cpdata = ([1.25626,-0.0904757,-0.874499,-1.33696,-2.07965,-2.78965,-4.53796],'cal/mol/K','+|-',[7.81442,6.54645,5.1555,4.28531,3.41125,3.16735,3.44443]),
        H298 = (117.864,'kcal/mol','+|-',7.47282),
        S298 = (-1.08467,'cal/mol/K','+|-',8.25794),
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
        Cpdata = ([-1.37889,-1.83238,-2.0585,-2.36515,-2.98721,-3.55084,-4.60887],'cal/mol/K','+|-',[2.16969,2.2156,2.15612,2.07039,2.00727,2.00114,2.0148]),
        H298 = (109.281,'kcal/mol','+|-',2.79489),
        S298 = (2.62419,'cal/mol/K','+|-',3.05616),
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
        Cpdata = ([-0.0449195,-1.22171,-2.09898,-2.64421,-3.25984,-3.76253,-4.83049],'cal/mol/K','+|-',[3.48142,3.97185,4.23338,4.11554,3.51262,3.23584,3.20098]),
        H298 = (101.284,'kcal/mol','+|-',13.3433),
        S298 = (1.58842,'cal/mol/K','+|-',7.22001),
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
        Cpdata = ([0.438336,-0.778409,-1.70694,-2.3544,-3.13823,-3.77849,-5.0214],'cal/mol/K','+|-',[2.88105,3.6266,3.99896,3.96269,3.43194,3.19065,3.16352]),
        H298 = (100.292,'kcal/mol','+|-',10.2004),
        S298 = (1.86652,'cal/mol/K','+|-',7.03155),
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
        Cpdata = ([0.514733,-0.883973,-1.9381,-2.56145,-3.25847,-3.87274,-5.14251],'cal/mol/K','+|-',[3.00268,4.03016,4.59883,4.5567,3.90184,3.61988,3.74267]),
        H298 = (102.319,'kcal/mol','+|-',9.38278),
        S298 = (1.84586,'cal/mol/K','+|-',7.80536),
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
        Cpdata = ([0.395763,-0.872689,-1.96369,-2.58783,-3.28743,-3.96547,-5.35782],'cal/mol/K','+|-',[2.95257,4.43345,5.15809,5.16894,4.50179,4.16525,4.20832]),
        H298 = (102.87,'kcal/mol','+|-',10.7113),
        S298 = (1.91504,'cal/mol/K','+|-',9.03038),
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
        Cpdata = ([-0.616096,-1.02392,-1.576,-1.99039,-2.69042,-3.3327,-4.09297],'cal/mol/K','+|-',[1.75764,2.16432,2.54677,2.7421,2.87749,2.9139,2.20946]),
        H298 = (106.05,'kcal/mol','+|-',5.81356),
        S298 = (1.74975,'cal/mol/K','+|-',4.98658),
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
        Cpdata = ([-0.624278,-1.07473,-1.51207,-1.91204,-2.63471,-3.20362,-4.13558],'cal/mol/K','+|-',[1.8902,2.327,2.75024,2.95555,3.13528,3.06578,2.38702]),
        H298 = (105.798,'kcal/mol','+|-',5.45981),
        S298 = (1.52894,'cal/mol/K','+|-',5.2906),
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
        Cpdata = ([-0.349476,-0.606672,-0.910777,-1.27163,-1.9939,-2.60475,-3.70028],'cal/mol/K','+|-',[2,2.05879,2.26207,2.50886,2.91057,2.97612,2.34834]),
        H298 = (104.377,'kcal/mol','+|-',3.04754),
        S298 = (0.118093,'cal/mol/K','+|-',2.62214),
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
        Cpdata = ([-0.931886,-3.04044,-4.50526,-5.25076,-5.8582,-6.41429,-9.30734],'cal/mol/K','+|-',[3.12939,4.0082,4.33345,4.2669,4.45335,5.34633,2.73631]),
        H298 = (98.0185,'kcal/mol','+|-',5.23841),
        S298 = (7.82813,'cal/mol/K','+|-',8.00484),
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
        Cpdata = ([-1.43731,-3.81545,-5.34427,-6.02722,-6.53806,-7.22698,-9.23892],'cal/mol/K','+|-',[3.18149,3.79241,4.16292,4.31393,5.0238,6.16298,3.39546]),
        H298 = (97.7001,'kcal/mol','+|-',6.38927),
        S298 = (9.87094,'cal/mol/K','+|-',4.96672),
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
        Cpdata = ([0.853354,-0.589463,-1.80625,-2.482,-3.19151,-3.89391,-5.31791],'cal/mol/K','+|-',[3.01345,4.94872,5.75513,5.70724,4.81603,4.30158,3.93623]),
        H298 = (101.845,'kcal/mol','+|-',11.6439),
        S298 = (1.32107,'cal/mol/K','+|-',9.48469),
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
        Cpdata = ([1.1293,-0.217897,-1.46057,-2.1991,-3.079,-3.8612,-5.18525],'cal/mol/K','+|-',[2.80604,4.67262,5.48735,5.44176,4.56272,4.1909,3.90978]),
        H298 = (102.342,'kcal/mol','+|-',10.711),
        S298 = (1.35192,'cal/mol/K','+|-',9.24756),
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
        Cpdata = ([0.964845,-0.111929,-1.23473,-1.97605,-2.84848,-3.6433,-5.40601],'cal/mol/K','+|-',[3.07912,5.06632,5.73938,5.57295,4.339,3.74744,4.04009]),
        H298 = (101.297,'kcal/mol','+|-',7.95884),
        S298 = (2.79043,'cal/mol/K','+|-',6.1389),
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
        Cpdata = ([1.15587,0.345598,-0.700806,-1.4776,-2.51808,-3.46621,-5.23531],'cal/mol/K','+|-',[3.04764,4.63488,5.20284,5.13141,4.18262,3.87301,4.21558]),
        H298 = (100.89,'kcal/mol','+|-',5.15459),
        S298 = (2.50196,'cal/mol/K','+|-',6.35754),
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
        Cpdata = ([0.465723,-0.548566,-1.58829,-2.35493,-3.50178,-4.60488,-5.58721],'cal/mol/K','+|-',[3.18138,4.90626,6.2864,6.8201,7.09323,8.31248,6.71819]),
        H298 = (100.186,'kcal/mol','+|-',14.9039),
        S298 = (4.33956,'cal/mol/K','+|-',9.49766),
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
        Cpdata = ([1.36592,0.617735,-0.430702,-1.21058,-2.21869,-3.11966,-5.1282],'cal/mol/K','+|-',[3.32041,4.99607,5.50404,5.31709,3.90596,2.89868,4.24616]),
        H298 = (101.114,'kcal/mol','+|-',3.84719),
        S298 = (1.9427,'cal/mol/K','+|-',5.99577),
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
        Cpdata = ([1.18851,0.47699,-0.515885,-1.27122,-2.24529,-3.06977,-5.12299],'cal/mol/K','+|-',[3.25445,5.19644,5.80929,5.6274,4.13942,3.04788,4.50631]),
        H298 = (101.018,'kcal/mol','+|-',3.83858),
        S298 = (2.35319,'cal/mol/K','+|-',5.55838),
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
        Cpdata = ([1.19057,0.56235,-0.35803,-1.13703,-2.22374,-3.10094,-5.14535],'cal/mol/K','+|-',[2.81264,4.43845,4.99843,4.99007,3.9158,3.34577,6.16749]),
        H298 = (100.686,'kcal/mol','+|-',2.52172),
        S298 = (0.687588,'cal/mol/K','+|-',3.61803),
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
        Cpdata = ([-0.467867,-3.54338,-5.23912,-5.71442,-5.32654,-4.97148,-6.68631],'cal/mol/K','+|-',[3.67712,3.3993,3.20015,3.17001,3.32624,3.29438,3.22748]),
        H298 = (107.25,'kcal/mol','+|-',27.5319),
        S298 = (4.9539,'cal/mol/K','+|-',3.37591),
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
        Cpdata = ([1.5594,-0.495045,-2.05122,-2.78248,-3.68187,-4.43107,-4.60786],'cal/mol/K','+|-',[2.68018,4.45026,5.65461,5.96845,5.85183,5.90491,4.21523]),
        H298 = (105.587,'kcal/mol','+|-',18.2784),
        S298 = (-2.41032,'cal/mol/K','+|-',12.683),
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
        Cpdata = ([1.55496,-0.149385,-1.41007,-1.92585,-2.71648,-3.42086,-3.91573],'cal/mol/K','+|-',[2.98837,4.55303,5.04983,4.25635,2.98619,2.53092,2.15347]),
        H298 = (103.278,'kcal/mol','+|-',3.60433),
        S298 = (-3.35662,'cal/mol/K','+|-',13.1734),
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
        Cpdata = ([1.42609,-0.285354,-1.52814,-2.02744,-2.76916,-3.4636,-3.83138],'cal/mol/K','+|-',[3.37757,5.31349,5.93573,4.97939,3.45003,2.88818,2.36932]),
        H298 = (103.108,'kcal/mol','+|-',3.69442),
        S298 = (-3.89951,'cal/mol/K','+|-',15.3874),
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
        Cpdata = ([0.447799,-2.1696,-3.71972,-3.83985,-3.88981,-4.25963,-3.36664],'cal/mol/K','+|-',[3.84549,4.72344,4.7895,4.11884,3.43578,3.35674,3.1635]),
        H298 = (103.246,'kcal/mol','+|-',7.13563),
        S298 = (-9.40643,'cal/mol/K','+|-',13.8867),
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
        Cpdata = ([-0.511174,-1.93404,-2.62708,-2.78601,-2.54202,-3.12279,-5.4361],'cal/mol/K','+|-',[3.48065,4.92538,5.79561,5.9621,5.89221,5.67257,4.94684]),
        H298 = (92.4453,'kcal/mol','+|-',5.40463),
        S298 = (-1.4297,'cal/mol/K','+|-',9.00498),
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
        Cpdata = ([-1.05129,-3.14471,-4.10065,-4.25555,-3.91171,-4.40416,-6.64322],'cal/mol/K','+|-',[3.72763,3.16352,3.42506,3.99129,4.59107,4.64938,3.26157]),
        H298 = (92.0377,'kcal/mol','+|-',6.54267),
        S298 = (-0.323618,'cal/mol/K','+|-',11.3791),
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
        Cpdata = ([0.795933,-0.910643,-1.87762,-2.49908,-3.19002,-3.65357,-4.63362],'cal/mol/K','+|-',[3.39073,3.27523,3.32371,3.06017,2.33989,2.19888,2.42312]),
        H298 = (100.953,'kcal/mol','+|-',4.65452),
        S298 = (1.68235,'cal/mol/K','+|-',4.14134),
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
        Cpdata = ([0.625305,-0.462439,-1.35449,-2.03677,-2.94935,-3.61067,-4.71134],'cal/mol/K','+|-',[2.58488,4.4872,5.51627,5.87898,5.26577,4.42133,3.2092]),
        H298 = (99.4257,'kcal/mol','+|-',3.16612),
        S298 = (3.07819,'cal/mol/K','+|-',3.6996),
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
        Cpdata = ([1.73484,-2.87603,-3.91083,-4.19666,-3.83996,-3.43472,-3.70337],'cal/mol/K','+|-',[7.78124,5.10624,4.29814,3.43956,3.0316,3.76572,5.01148]),
        H298 = (98.0824,'kcal/mol','+|-',4.91029),
        S298 = (0.268444,'cal/mol/K','+|-',5.68494),
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
        Cpdata = ([1.98321,-4.03774,-4.76692,-4.65665,-3.65708,-2.84934,-2.60257],'cal/mol/K','+|-',[10.7834,4.05273,4.0032,3.90505,3.77427,4.09929,4.22069]),
        H298 = (98.1249,'kcal/mol','+|-',6.04581),
        S298 = (-0.956449,'cal/mol/K','+|-',5.02941),
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
        Cpdata = ([1.5703,0.126999,-1.20718,-1.99646,-2.9502,-3.49991,-4.7552],'cal/mol/K','+|-',[3.01305,3.43801,3.61449,3.35055,3.0351,2.83614,2.61889]),
        H298 = (102.328,'kcal/mol','+|-',10.1636),
        S298 = (2.63954,'cal/mol/K','+|-',4.11675),
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
        Cpdata = ([1.62222,0.614508,-0.539515,-1.41421,-2.53866,-3.23726,-4.65327],'cal/mol/K','+|-',[3.84174,3.82133,3.47808,3.31398,3.32048,3.33143,3.18347]),
        H298 = (99.9693,'kcal/mol','+|-',7.84112),
        S298 = (2.08245,'cal/mol/K','+|-',4.80767),
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
        Cpdata = ([0.146988,-0.737139,-1.55514,-2.2181,-3.13459,-3.83466,-4.94133],'cal/mol/K','+|-',[2.13875,2.13315,2.31246,2.52464,2.42604,2.40135,2.29671]),
        H298 = (102.035,'kcal/mol','+|-',2.67976),
        S298 = (1.18016,'cal/mol/K','+|-',4.45198),
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
        Cpdata = ([0.474214,-0.587365,-1.58449,-2.36168,-3.33992,-4.05753,-5.14003],'cal/mol/K','+|-',[2.36522,2.67391,3.00514,3.24875,3.04056,2.98039,2.85775]),
        H298 = (101.852,'kcal/mol','+|-',3.73097),
        S298 = (0.375314,'cal/mol/K','+|-',4.85311),
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
        Cpdata = ([0.109186,-0.903733,-1.60255,-2.21533,-3.07258,-3.69555,-4.82867],'cal/mol/K','+|-',[3.13689,3.27982,3.10636,3.14602,3.05579,2.92452,2.40003]),
        H298 = (97.3269,'kcal/mol','+|-',8.37605),
        S298 = (2.54347,'cal/mol/K','+|-',5.16216),
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
        Cpdata = ([1.84466,-0.909553,-2.15188,-3.18679,-4.5338,-5.34272,-6.11114],'cal/mol/K','+|-',[3.93947,7.21389,6.68,6.33432,5.52292,4.91571,3.94152]),
        H298 = (101.837,'kcal/mol','+|-',4.36208),
        S298 = (1.03133,'cal/mol/K','+|-',5.79482),
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
        Cpdata = ([2.49304,-0.521321,-1.81368,-2.7889,-4.07918,-4.95132,-5.81438],'cal/mol/K','+|-',[2.41907,8.25556,7.67351,7.12812,5.93624,5.30557,4.26762]),
        H298 = (102.204,'kcal/mol','+|-',3.58719),
        S298 = (0.35241,'cal/mol/K','+|-',5.496),
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
        Cpdata = ([-0.380308,-0.902092,-1.44761,-1.94133,-2.66045,-3.23096,-4.46695],'cal/mol/K','+|-',[2.33323,1.86716,1.78012,1.85588,1.69794,1.51656,1.50515]),
        H298 = (96.4589,'kcal/mol','+|-',7.96119),
        S298 = (2.96997,'cal/mol/K','+|-',4.99567),
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
        Cpdata = ([-0.461806,-0.901198,-1.41209,-1.88419,-2.56023,-3.11024,-4.40019],'cal/mol/K','+|-',[2.57741,2.0801,1.96931,2.03997,1.81194,1.56214,1.63301]),
        H298 = (97.7193,'kcal/mol','+|-',5.10731),
        S298 = (3.41723,'cal/mol/K','+|-',5.11432),
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
        Cpdata = ([-0.825755,-1.02181,-1.42021,-1.84283,-2.56716,-3.22782,-4.51602],'cal/mol/K','+|-',[2.90216,2.58049,2.23858,2.12836,1.91705,1.745,1.54683]),
        H298 = (97.4486,'kcal/mol','+|-',4.97037),
        S298 = (2.2946,'cal/mol/K','+|-',3.54592),
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
        Cpdata = ([-0.24493,-0.550682,-1.073,-1.52976,-2.30861,-3.03973,-4.4894],'cal/mol/K','+|-',[2.44733,2.3655,2.25576,2.18776,2.01404,1.92443,1.83939]),
        H298 = (96.6857,'kcal/mol','+|-',5.49545),
        S298 = (1.46177,'cal/mol/K','+|-',2.25266),
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
        Cpdata = ([-0.321809,-0.485338,-0.870235,-1.28185,-2.07684,-2.84321,-4.45259],'cal/mol/K','+|-',[3.54224,3.39887,3.05851,2.84302,2.5197,2.40364,2.41118]),
        H298 = (97.8507,'kcal/mol','+|-',8.33215),
        S298 = (1.8306,'cal/mol/K','+|-',2.66183),
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
        Cpdata = ([-0.0493313,-0.764499,-1.40289,-1.93106,-2.55237,-2.97699,-4.26891],'cal/mol/K','+|-',[2.81243,2.34552,2.55487,2.80503,2.5613,2.20165,2.50492]),
        H298 = (97.9683,'kcal/mol','+|-',6.45019),
        S298 = (4.68953,'cal/mol/K','+|-',6.28272),
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
        Cpdata = ([-0.70882,-1.21081,-1.77051,-2.22714,-2.64256,-2.92326,-4.38039],'cal/mol/K','+|-',[2.01195,2.21111,2.91168,3.50701,3.4047,2.87956,3.30419]),
        H298 = (96.0546,'kcal/mol','+|-',4.69793),
        S298 = (3.20537,'cal/mol/K','+|-',4.9745),
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
        Cpdata = ([-0.00774594,-0.906178,-1.61001,-2.20258,-3.11859,-3.78281,-4.77213],'cal/mol/K','+|-',[2.40663,2.446,2.47487,2.4974,2.48267,2.46012,2.4512]),
        H298 = (89.3141,'kcal/mol','+|-',3.99936),
        S298 = (0.925367,'cal/mol/K','+|-',2.47843),
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
        Cpdata = ([0.89818,0.0651309,-0.803104,-1.72906,-2.79304,-3.60304,-4.98065],'cal/mol/K','+|-',[2.71307,2.92021,2.80288,2.92559,2.42098,2.3049,2.20526]),
        H298 = (102.344,'kcal/mol','+|-',3.4786),
        S298 = (1.95641,'cal/mol/K','+|-',3.49318),
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
        Cpdata = ([0.706159,-1.05852,-1.96404,-3.29852,-3.9611,-4.50189,-5.92638],'cal/mol/K','+|-',[3.20038,3.18888,3.71778,3.4105,3.6587,4.13734,3.4607]),
        H298 = (101.985,'kcal/mol','+|-',9.99796),
        S298 = (3.92299,'cal/mol/K','+|-',4.64312),
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
        Cpdata = ([0.962187,0.439681,-0.416125,-1.20591,-2.40368,-3.30342,-4.66541],'cal/mol/K','+|-',[3.31994,3.07271,2.67199,2.38482,1.99584,1.91943,2.02055]),
        H298 = (102.399,'kcal/mol','+|-',2.55584),
        S298 = (1.30088,'cal/mol/K','+|-',2.22166),
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
        Cpdata = ([1.3974,0.830197,-0.0963367,-0.94918,-2.26144,-3.23309,-4.62408],'cal/mol/K','+|-',[2.53799,2.41707,2.19103,2.08981,2.00097,2.07095,2.24544]),
        H298 = (102.49,'kcal/mol','+|-',2.52555),
        S298 = (1.09087,'cal/mol/K','+|-',2.07038),
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
        Cpdata = ([-1.58795,-2.63715,-3.35075,-3.56957,-3.64813,-3.71158,-4.22092],'cal/mol/K','+|-',[3.61754,3.88857,4.18993,4.26307,3.86724,3.58929,3.22334]),
        H298 = (104.481,'kcal/mol','+|-',19.8457),
        S298 = (0.700482,'cal/mol/K','+|-',7.81983),
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
        Cpdata = ([-1.11247,-1.257,-1.55572,-1.77118,-2.20343,-2.54968,-4.06704],'cal/mol/K','+|-',[2.14019,2.18135,2.22831,2.25789,2.23313,2.20721,3.78272]),
        H298 = (89.5128,'kcal/mol','+|-',53.9162),
        S298 = (-1.14464,'cal/mol/K','+|-',2.49755),
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
        Cpdata = ([-0.881225,-2.53187,-3.88501,-4.34385,-4.49788,-4.73183,-5.33992],'cal/mol/K','+|-',[2.02259,3.02306,3.40447,3.69426,3.77734,3.54492,3.83912]),
        H298 = (109.401,'kcal/mol','+|-',4.51935),
        S298 = (-0.139881,'cal/mol/K','+|-',5.39909),
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
        Cpdata = ([-0.905893,-2.59719,-4.08041,-4.64904,-4.83216,-5.09573,-5.75429],'cal/mol/K','+|-',[2.18828,3.28572,3.52708,3.57359,3.57637,3.14596,3.31495]),
        H298 = (109.039,'kcal/mol','+|-',3.78328),
        S298 = (0.450611,'cal/mol/K','+|-',4.64141),
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
        Cpdata = ([-1.03919,-2.6065,-4.07011,-4.78292,-5.07875,-5.35299,-5.61357],'cal/mol/K','+|-',[2.36145,2.67358,2.51782,2.84689,3.70454,3.82924,3.46333]),
        H298 = (108.865,'kcal/mol','+|-',3.78889),
        S298 = (1.12357,'cal/mol/K','+|-',2.66914),
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
        Cpdata = ([-2.03886,-3.06142,-3.59747,-3.70809,-3.65589,-3.56471,-3.75425],'cal/mol/K','+|-',[4.60961,4.67919,4.86425,4.84161,4.30312,3.94627,2.93592]),
        H298 = (106.412,'kcal/mol','+|-',4.96294),
        S298 = (1.58568,'cal/mol/K','+|-',9.60882),
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
        Cpdata = ([-0.28201,-2.62119,-4.16866,-4.68699,-4.89689,-4.75067,-4.41874],'cal/mol/K','+|-',[5.59299,6.48633,6.5338,6.36963,5.3851,4.84602,4.21876]),
        H298 = (107.961,'kcal/mol','+|-',9.22753),
        S298 = (5.1118,'cal/mol/K','+|-',12.9658),
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
        Cpdata = ([0.517345,-1.47921,-3.06646,-3.64074,-3.85629,-3.73847,-3.90528],'cal/mol/K','+|-',[7.14209,7.92655,8.07396,7.9203,6.38696,5.57077,5.49748]),
        H298 = (105.653,'kcal/mol','+|-',12.5095),
        S298 = (6.20268,'cal/mol/K','+|-',17.463),
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
        Cpdata = ([-0.602899,-2.42992,-4.13263,-4.88072,-5.11696,-5.00238,-5.30447],'cal/mol/K','+|-',[8.28051,10.0317,9.98815,9.23187,6.3333,4.51601,3.18204]),
        H298 = (102.7,'kcal/mol','+|-',9.59474),
        S298 = (1.53458,'cal/mol/K','+|-',9.14309),
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
        Cpdata = ([-3.37664,-3.58424,-3.42776,-3.21033,-2.77456,-2.58567,-3.24348],'cal/mol/K','+|-',[2.46081,3.8659,4.85951,5.01641,4.59338,4.51704,3.58258]),
        H298 = (106.433,'kcal/mol','+|-',4.74145),
        S298 = (-0.5149,'cal/mol/K','+|-',6.88533),
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
        Cpdata = ([-2.8256,-2.75222,-2.53066,-2.32653,-1.91644,-1.63243,-2.44586],'cal/mol/K','+|-',[2.39133,4.46242,6.32649,6.68201,5.91862,5.39929,3.96134]),
        H298 = (105.171,'kcal/mol','+|-',5.24507),
        S298 = (-2.30443,'cal/mol/K','+|-',6.78889),
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
        Cpdata = ([-1.76704,-2.9711,-3.60419,-3.93842,-4.17509,-4.39069,-4.85692],'cal/mol/K','+|-',[4.29012,4.44196,4.65271,4.72541,4.67224,4.58591,4.7399]),
        H298 = (91.7736,'kcal/mol','+|-',12.7922),
        S298 = (-0.0492958,'cal/mol/K','+|-',11.2741),
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
        Cpdata = ([-0.481461,-1.77876,-2.36796,-2.77031,-3.34135,-3.73218,-4.37842],'cal/mol/K','+|-',[2.89469,3.82679,4.05114,3.9265,3.31765,2.77646,2.32066]),
        H298 = (99.4555,'kcal/mol','+|-',6.41029),
        S298 = (3.77568,'cal/mol/K','+|-',12.411),
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
        Cpdata = ([-0.542523,-2.0716,-2.66803,-3.07355,-3.6379,-4.02203,-4.66522],'cal/mol/K','+|-',[3.15801,3.79138,4.03476,3.96017,3.41504,2.92116,2.33678]),
        H298 = (98.6882,'kcal/mol','+|-',6.03224),
        S298 = (4.51158,'cal/mol/K','+|-',14.2508),
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
        Cpdata = ([-0.357829,-1.6785,-2.46974,-2.92046,-3.49133,-3.95906,-4.63521],'cal/mol/K','+|-',[2.58929,2.0049,2.39666,2.71963,3.00659,3.07858,3.13064]),
        H298 = (97.5037,'kcal/mol','+|-',8.2321),
        S298 = (7.66856,'cal/mol/K','+|-',20.9758),
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
        Cpdata = ([-0.700832,-2.40854,-2.838,-3.20478,-3.76354,-4.076,-4.69094],'cal/mol/K','+|-',[4.30644,5.40236,5.75388,5.53905,4.53881,3.67957,2.5611]),
        H298 = (99.7887,'kcal/mol','+|-',4.42254),
        S298 = (1.80561,'cal/mol/K','+|-',4.90172),
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
        Cpdata = ([-2.10791,-3.28725,-3.93197,-4.24815,-4.39616,-4.5653,-4.9838],'cal/mol/K','+|-',[4.40095,4.45752,4.66197,4.80239,4.9401,4.95365,5.21537]),
        H298 = (89.1734,'kcal/mol','+|-',9.885),
        S298 = (-1.06349,'cal/mol/K','+|-',10.2322),
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
        Cpdata = ([-3.23621,-3.81771,-4.00115,-4.00198,-3.81305,-3.7704,-3.8683],'cal/mol/K','+|-',[4.17477,5.72943,6.52076,6.50388,5.96815,5.69709,5.58108]),
        H298 = (92.1107,'kcal/mol','+|-',13.932),
        S298 = (1.11572,'cal/mol/K','+|-',10.8675),
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
        Cpdata = ([-3.81564,-4.6773,-4.87805,-4.70418,-4.12287,-3.79786,-3.49174],'cal/mol/K','+|-',[4.43582,5.88823,6.84567,7.1315,6.90525,6.71092,6.48693]),
        H298 = (89.1223,'kcal/mol','+|-',13.5728),
        S298 = (1.57991,'cal/mol/K','+|-',12.8909),
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
        Cpdata = ([-5.79514,-7.63866,-8.26603,-8.15818,-7.14834,-6.35674,-5.31743],'cal/mol/K','+|-',[2.58986,3.51,6.02137,6.62431,5.38478,4.55151,4.4356]),
        H298 = (92.4452,'kcal/mol','+|-',12.0213),
        S298 = (4.14017,'cal/mol/K','+|-',8.16864),
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
        Cpdata = ([-5.89257,-7.26105,-7.71,-7.57434,-6.66826,-6.02013,-5.45478],'cal/mol/K','+|-',[3.08543,3.75861,7.1738,8.01859,6.43271,5.57596,5.77164]),
        H298 = (91.2966,'kcal/mol','+|-',9.63303),
        S298 = (4.32101,'cal/mol/K','+|-',10.9787),
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
        Cpdata = ([-2.92265,-3.14641,-2.96948,-2.56171,-1.91213,-1.71412,-1.71548],'cal/mol/K','+|-',[4.74129,5.00144,4.74627,4.92248,6.4979,7.54797,8.39499]),
        H298 = (86.7596,'kcal/mol','+|-',22.254),
        S298 = (0.818792,'cal/mol/K','+|-',18.9801),
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
        Cpdata = ([-2.86861,-3.20452,-3.2499,-2.97865,-2.5445,-2.56901,-2.66349],'cal/mol/K','+|-',[5.5961,5.91004,5.34539,5.24197,6.69681,7.3266,8.17196]),
        H298 = (87.765,'kcal/mol','+|-',24.8639),
        S298 = (-2.47798,'cal/mol/K','+|-',10.5613),
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
        Cpdata = ([-1.78763,-1.66872,-1.80889,-2.24649,-3.03851,-3.70177,-4.80968],'cal/mol/K','+|-',[2.08832,2.75449,3.68983,3.82492,3.82845,3.60959,2.7597]),
        H298 = (97.8271,'kcal/mol','+|-',3.58469),
        S298 = (-0.0447361,'cal/mol/K','+|-',3.59552),
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
        Cpdata = ([-1.70079,-3.09585,-3.90701,-4.33698,-4.60656,-4.85212,-5.3863],'cal/mol/K','+|-',[4.3103,4.02825,4.02011,4.23532,4.62556,4.69304,4.98543]),
        H298 = (87.6703,'kcal/mol','+|-',5.77108),
        S298 = (-1.84981,'cal/mol/K','+|-',9.7611),
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
        Cpdata = ([-1.54499,-3.02247,-3.89619,-4.36364,-4.68542,-4.9936,-5.64302],'cal/mol/K','+|-',[4.17631,4.01052,4.06606,4.31922,4.72326,4.72533,4.79846]),
        H298 = (87.9682,'kcal/mol','+|-',5.76865),
        S298 = (-2.34087,'cal/mol/K','+|-',8.1535),
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
        Cpdata = ([-1.4706,-2.95239,-3.85324,-4.34852,-4.71464,-5.0599,-5.74551],'cal/mol/K','+|-',[4.10194,3.9436,4.07192,4.36503,4.76206,4.69465,4.64959]),
        H298 = (87.9441,'kcal/mol','+|-',5.80759),
        S298 = (-2.27389,'cal/mol/K','+|-',8.19857),
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
        Cpdata = ([-1.31197,-2.96141,-4.00767,-4.60764,-5.00121,-5.39351,-6.21893],'cal/mol/K','+|-',[4.28067,4.03455,4.11654,4.48477,5.12295,5.13088,5.19056]),
        H298 = (87.6138,'kcal/mol','+|-',5.05484),
        S298 = (-2.28842,'cal/mol/K','+|-',8.36557),
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
        Cpdata = ([-1.00842,-2.59146,-3.58224,-4.0989,-4.33624,-4.72423,-5.76669],'cal/mol/K','+|-',[4.54049,4.49274,4.24496,4.15011,3.81257,3.36353,4.82678]),
        H298 = (86.1286,'kcal/mol','+|-',2.97119),
        S298 = (-3.04807,'cal/mol/K','+|-',7.15257),
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
        Cpdata = ([-0.781384,-2.39595,-3.42942,-3.97207,-4.23919,-4.64827,-5.75193],'cal/mol/K','+|-',[4.21811,4.28879,4.15653,4.12416,3.832,3.39881,4.97215]),
        H298 = (86.0045,'kcal/mol','+|-',2.78659),
        S298 = (-3.02745,'cal/mol/K','+|-',7.3687),
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
        Cpdata = ([-0.832176,-2.40101,-3.4045,-3.90748,-4.13918,-4.54915,-5.4534],'cal/mol/K','+|-',[4.41745,4.51073,4.35806,4.33043,4.10235,3.62217,4.74996]),
        H298 = (85.9537,'kcal/mol','+|-',2.98045),
        S298 = (-2.51086,'cal/mol/K','+|-',7.48226),
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
        Cpdata = ([-2.34979,-4.24724,-5.14319,-5.51333,-5.53887,-5.50431,-6.16496],'cal/mol/K','+|-',[3.48685,3.55118,3.73347,4.31524,4.35077,4.03832,6.97983]),
        H298 = (85.9022,'kcal/mol','+|-',3.86342),
        S298 = (0.741346,'cal/mol/K','+|-',2.9382),
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
        Cpdata = ([-0.149248,-1.57021,-2.62208,-3.18484,-3.50931,-4.11933,-5.1332],'cal/mol/K','+|-',[4.44027,4.19541,4.04152,3.98519,3.84157,3.62118,4.31034]),
        H298 = (85.9952,'kcal/mol','+|-',3.64129),
        S298 = (-3.97435,'cal/mol/K','+|-',7.10101),
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
        Cpdata = ([-0.746751,-2.77289,-4.31821,-5.24218,-5.5345,-5.79827,-8.06374],'cal/mol/K','+|-',[4.33973,4.19539,4.03049,3.79594,3.41434,3.24571,7.23735]),
        H298 = (84.9153,'kcal/mol','+|-',6.14361),
        S298 = (-3.55526,'cal/mol/K','+|-',4.4972),
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
        Cpdata = ([1.00092,0.657821,-0.0801114,-0.458058,-0.78172,-1.55942,-3.31876],'cal/mol/K','+|-',[4.35717,5.53712,5.60686,5.133,4.8343,4.60036,3.17223]),
        H298 = (85.2699,'kcal/mol','+|-',6.14975),
        S298 = (-9.26254,'cal/mol/K','+|-',6.4442),
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
        Cpdata = ([1.0846,-0.948214,-2.30775,-3.12043,-3.87954,-4.76109,-5.04948],'cal/mol/K','+|-',[3.76365,3.06422,2.67552,2.59758,2.59427,2.60123,2.48854]),
        H298 = (86.2527,'kcal/mol','+|-',4.71485),
        S298 = (-2.56497,'cal/mol/K','+|-',5.99526),
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
        Cpdata = ([0.672875,-1.03942,-2.19039,-2.79138,-3.32753,-4.22015,-5.13942],'cal/mol/K','+|-',[5.70805,4.6863,3.96568,3.66355,3.20974,3.21085,3.3213]),
        H298 = (86.6271,'kcal/mol','+|-',6.30088),
        S298 = (-3.43764,'cal/mol/K','+|-',8.69134),
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
        Cpdata = ([-3.1696,-3.83953,-4.09661,-3.98311,-3.47127,-3.71677,-4.18453],'cal/mol/K','+|-',[3.65414,3.21106,3.34155,3.22932,3.17273,3.18712,3.29185]),
        H298 = (87.2855,'kcal/mol','+|-',6.58301),
        S298 = (-1.92401,'cal/mol/K','+|-',4.54968),
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
        Cpdata = ([-0.535889,-2.37148,-3.5499,-4.28425,-4.72257,-5.12735,-7.19481],'cal/mol/K','+|-',[4.66285,4.64287,4.61786,4.48675,3.59875,3.46869,6.58405]),
        H298 = (86.3103,'kcal/mol','+|-',5.04543),
        S298 = (-5.52428,'cal/mol/K','+|-',5.73008),
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
        Cpdata = ([-0.0168936,-2.21712,-3.67217,-4.57511,-5.20793,-5.56058,-8.11061],'cal/mol/K','+|-',[5.804,6.26158,6.24157,5.90747,4.11276,4.02811,7.95221]),
        H298 = (86.1333,'kcal/mol','+|-',6.20755),
        S298 = (-6.71809,'cal/mol/K','+|-',5.30381),
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
        Cpdata = ([-1.65931,-3.57505,-4.80859,-5.62521,-6.41611,-6.85856,-6.8678],'cal/mol/K','+|-',[4.08884,3.34148,4.11126,5.18521,6.84061,7.25917,6.18956]),
        H298 = (89.745,'kcal/mol','+|-',5.26867),
        S298 = (-0.51706,'cal/mol/K','+|-',10.4222),
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
        Cpdata = ([-0.946049,-3.44441,-5.13545,-6.26143,-7.43474,-7.998,-7.99563],'cal/mol/K','+|-',[3.96971,3.71919,4.68344,5.81656,7.53896,7.89311,6.16557]),
        H298 = (89.9663,'kcal/mol','+|-',6.07096),
        S298 = (0.284316,'cal/mol/K','+|-',12.5583),
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
        Cpdata = ([-1.13637,-3.94715,-5.92954,-7.30875,-8.77882,-9.42669,-9.40297],'cal/mol/K','+|-',[5.18665,3.60635,3.7644,4.9212,7.14328,7.31498,4.2968]),
        H298 = (89.8149,'kcal/mol','+|-',7.93511),
        S298 = (2.81193,'cal/mol/K','+|-',11.1227),
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
        Cpdata = ([-1.89337,-3.75914,-4.87756,-5.48916,-5.8709,-6.41353,-8.29203],'cal/mol/K','+|-',[7.85068,5.68516,4.4722,3.87979,3.52881,3.17791,5.44142]),
        H298 = (85.3724,'kcal/mol','+|-',5.91776),
        S298 = (-1.71685,'cal/mol/K','+|-',5.71943),
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
        Cpdata = ([-2.03353,-3.11216,-3.60328,-3.77005,-3.99415,-4.17075,-4.34055],'cal/mol/K','+|-',[4.53467,4.79853,5.05322,5.13358,4.95069,4.42782,3.00964]),
        H298 = (89.1216,'kcal/mol','+|-',6.58766),
        S298 = (-2.15384,'cal/mol/K','+|-',10.2708),
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
        Cpdata = ([-1.30869,-2.03137,-2.3601,-2.50507,-2.80027,-3.13773,-3.75586],'cal/mol/K','+|-',[4.20517,2.86619,2.02922,2.03696,2.26048,2.35199,2.35246]),
        H298 = (87.9324,'kcal/mol','+|-',7.04907),
        S298 = (-4.62835,'cal/mol/K','+|-',4.74348),
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
        Cpdata = ([0.205523,-1.12803,-2.10076,-2.46701,-2.91947,-3.4492,-4.29269],'cal/mol/K','+|-',[2.90162,2.60045,2.58381,2.6569,2.91226,3.01097,2.61754]),
        H298 = (91.2441,'kcal/mol','+|-',5.49066),
        S298 = (-6.10865,'cal/mol/K','+|-',4.35832),
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
        Cpdata = ([0.51131,-1.06184,-2.18337,-2.67114,-3.27045,-3.81743,-4.63125],'cal/mol/K','+|-',[3.09057,3.03398,3.00283,2.95893,2.98864,3.08404,2.58709]),
        H298 = (90.7124,'kcal/mol','+|-',5.96075),
        S298 = (-6.04062,'cal/mol/K','+|-',5.24863),
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
        Cpdata = ([-3.03923,-3.06377,-2.6565,-2.54856,-2.66404,-2.78178,-3.14234],'cal/mol/K','+|-',[2.56429,2.39411,2.58355,2.75353,2.8851,2.62324,2.63679]),
        H298 = (86.0549,'kcal/mol','+|-',3.41078),
        S298 = (-2.93657,'cal/mol/K','+|-',2.65263),
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
        Cpdata = ([-1.26484,-2.58053,-3.45746,-4.00251,-4.49351,-4.90323,-5.80958],'cal/mol/K','+|-',[3.72809,3.54799,3.54915,3.39455,3.08612,2.97264,2.61266]),
        H298 = (86.4764,'kcal/mol','+|-',10.4513),
        S298 = (-2.42975,'cal/mol/K','+|-',4.65962),
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
        Cpdata = ([-2.6471,-3.73861,-4.37426,-4.59811,-4.76066,-5.14458,-6.32263],'cal/mol/K','+|-',[3.5465,3.17409,3.22313,3.22958,3.27241,3.26206,3.1631]),
        H298 = (90.6128,'kcal/mol','+|-',5.92778),
        S298 = (-1.03391,'cal/mol/K','+|-',3.20301),
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
        Cpdata = ([-0.343333,-1.80847,-2.84626,-3.60545,-4.31541,-4.74233,-5.46754],'cal/mol/K','+|-',[3.52669,3.85546,4.24992,4.37407,4.10911,3.95361,3.2498]),
        H298 = (83.7188,'kcal/mol','+|-',9.98066),
        S298 = (-3.3603,'cal/mol/K','+|-',5.38258),
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
        Cpdata = ([-3.70401,-4.03932,-4.04618,-3.99414,-3.59261,-3.03301,-2.08553],'cal/mol/K','+|-',[6.54965,6.30906,5.75587,5.0793,4.30636,3.81992,2.55023]),
        H298 = (85.0573,'kcal/mol','+|-',4.36294),
        S298 = (4.46378,'cal/mol/K','+|-',26.3602),
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

