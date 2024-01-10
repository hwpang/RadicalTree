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
        Cpdata = ([-0.66105,-1.70106,-2.3855,-2.76323,-3.15647,-3.48289,-4.29641],'cal/mol/K','+|-',[5.92318,6.25657,6.39873,6.28709,5.93133,5.82393,6.01382]),
        H298 = (92.9694,'kcal/mol','+|-',30.7823),
        S298 = (0.623468,'cal/mol/K','+|-',10.8249),
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
        Cpdata = ([-0.66105,-1.70106,-2.3855,-2.76323,-3.15647,-3.48289,-4.29641],'cal/mol/K','+|-',[5.92318,6.25657,6.39873,6.28709,5.93133,5.82393,6.01382]),
        H298 = (92.9694,'kcal/mol','+|-',30.7823),
        S298 = (0.623468,'cal/mol/K','+|-',10.8249),
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
        Cpdata = ([-0.546591,-1.4289,-2.01477,-2.29638,-2.59579,-2.83782,-3.6172],'cal/mol/K','+|-',[5.73759,6.20951,6.37918,6.1614,5.6542,5.53733,5.94824]),
        H298 = (86.325,'kcal/mol','+|-',37.0906),
        S298 = (0.194416,'cal/mol/K','+|-',11.697),
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
        Cpdata = ([-0.319973,-1.08783,-1.71359,-2.15176,-2.77545,-3.22761,-4.10617],'cal/mol/K','+|-',[5.23152,5.29382,5.47265,5.48187,5.63427,5.91348,6.4877]),
        H298 = (81.4816,'kcal/mol','+|-',61.4935),
        S298 = (0.826179,'cal/mol/K','+|-',10.4823),
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
        Cpdata = ([-0.754392,-1.52023,-2.11406,-2.50802,-3.02639,-3.42598,-4.30404],'cal/mol/K','+|-',[5.25299,5.28761,5.33605,5.17561,5.01113,4.99972,4.98107]),
        H298 = (84.6907,'kcal/mol','+|-',40.5399),
        S298 = (0.434762,'cal/mol/K','+|-',12.0929),
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
        Cpdata = ([-0.453005,-1.28244,-1.95983,-2.40174,-2.98871,-3.41884,-4.34704],'cal/mol/K','+|-',[5.15953,5.17377,5.26344,5.11128,4.97991,4.97131,5.00669]),
        H298 = (88.8709,'kcal/mol','+|-',38.2955),
        S298 = (1.05497,'cal/mol/K','+|-',12.4999),
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
        Cpdata = ([-0.567843,-1.42078,-2.09303,-2.5384,-3.14588,-3.58578,-4.50755],'cal/mol/K','+|-',[5.09789,5.09684,5.21513,5.04525,4.86355,4.82871,4.85113]),
        H298 = (89.9856,'kcal/mol','+|-',37.0628),
        S298 = (0.450356,'cal/mol/K','+|-',9.17873),
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
        Cpdata = ([-0.527752,-1.37754,-2.05221,-2.49692,-3.11245,-3.56359,-4.42912],'cal/mol/K','+|-',[5.16942,5.12558,5.25121,5.07089,4.89884,4.87891,4.84555]),
        H298 = (85.6217,'kcal/mol','+|-',30.1715),
        S298 = (-0.0854951,'cal/mol/K','+|-',8.45859),
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
        Cpdata = ([-0.538041,-1.44182,-2.13754,-2.58682,-3.19526,-3.62191,-4.44788],'cal/mol/K','+|-',[5.28892,5.22448,5.36298,5.15333,4.95014,4.93359,4.90828]),
        H298 = (80.5148,'kcal/mol','+|-',15.7862),
        S298 = (-0.081482,'cal/mol/K','+|-',9.01594),
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
        Cpdata = ([-1.69739,-3.13973,-3.92423,-3.96155,-3.89198,-3.87997,-4.20124],'cal/mol/K','+|-',[4.57117,4.98609,5.16375,4.91861,4.57224,4.52823,4.83337]),
        H298 = (76.8708,'kcal/mol','+|-',21.4598),
        S298 = (1.08854,'cal/mol/K','+|-',11.729),
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
        Cpdata = ([-1.83075,-3.41628,-4.18364,-4.18827,-4.04584,-3.83501,-4.23058],'cal/mol/K','+|-',[4.56503,4.72015,4.73234,4.66075,4.51929,4.54622,4.94316]),
        H298 = (78.0348,'kcal/mol','+|-',15.7008),
        S298 = (3.40757,'cal/mol/K','+|-',8.96289),
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
        Cpdata = ([-2.02381,-3.74949,-4.50269,-4.48064,-4.16395,-3.80138,-4.12792],'cal/mol/K','+|-',[4.51272,4.55577,4.59887,4.53126,4.50568,4.57984,5.13803]),
        H298 = (75.8759,'kcal/mol','+|-',14.9342),
        S298 = (4.53316,'cal/mol/K','+|-',8.94948),
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
        Cpdata = ([-2.11897,-3.53872,-4.24867,-4.31906,-4.01113,-3.55826,-4.66414],'cal/mol/K','+|-',[4.52902,4.52148,4.55527,4.52086,4.47682,4.53116,5.08898]),
        H298 = (72.5113,'kcal/mol','+|-',10.228),
        S298 = (5.98724,'cal/mol/K','+|-',9.45738),
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
        Cpdata = ([-0.0652128,-0.725174,-1.36453,-1.91295,-2.69224,-3.25248,-4.31506],'cal/mol/K','+|-',[5.35861,4.57306,4.64495,4.7586,4.77722,4.72899,4.61772]),
        H298 = (80.7545,'kcal/mol','+|-',12.8994),
        S298 = (-0.987431,'cal/mol/K','+|-',7.3222),
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
        Cpdata = ([0.134906,-0.805265,-1.61273,-2.21937,-3.0289,-3.5755,-4.58194],'cal/mol/K','+|-',[5.66838,4.57118,4.51295,4.6063,4.62955,4.61031,4.53255]),
        H298 = (78.6722,'kcal/mol','+|-',10.9969),
        S298 = (-0.634835,'cal/mol/K','+|-',8.17539),
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
        Cpdata = ([-0.608391,-0.507786,-0.69083,-1.08124,-1.77845,-2.3757,-3.59066],'cal/mol/K','+|-',[4.48178,4.6594,4.89875,4.95597,4.7842,4.60518,4.49707]),
        H298 = (86.706,'kcal/mol','+|-',8.42529),
        S298 = (-1.94448,'cal/mol/K','+|-',4.80359),
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
        Cpdata = ([-0.468957,-1.01024,-1.56461,-1.9832,-2.63927,-3.23033,-4.3219],'cal/mol/K','+|-',[4.49886,4.53044,4.518,4.47225,4.54201,4.58887,4.52303]),
        H298 = (110.392,'kcal/mol','+|-',52.0634),
        S298 = (-0.108427,'cal/mol/K','+|-',4.48761),
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
        Cpdata = ([-0.837028,-1.71111,-2.36707,-2.81694,-3.37038,-3.73484,-5.03413],'cal/mol/K','+|-',[4.74861,5.39303,5.55644,5.33047,4.80217,4.51556,5.12536]),
        H298 = (115.516,'kcal/mol','+|-',51.7874),
        S298 = (4.04821,'cal/mol/K','+|-',14.9337),
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
        Cpdata = ([1.09731,0.5852,-0.161653,-0.556789,-0.866855,-1.16506,-2.18026],'cal/mol/K','+|-',[5.37435,4.88255,4.56118,4.49813,4.4735,4.60677,5.35502]),
        H298 = (61.9321,'kcal/mol','+|-',32.7484),
        S298 = (9.21728,'cal/mol/K','+|-',39.2406),
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
        Cpdata = ([-2.09904,-2.58114,-2.80214,-2.98219,-3.19452,-3.45785,-4.11216],'cal/mol/K','+|-',[4.87596,5.46589,5.69612,5.58721,5.32249,5.30988,4.97341]),
        H298 = (63.7666,'kcal/mol','+|-',23.6346),
        S298 = (-2.33233,'cal/mol/K','+|-',9.09676),
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
        Cpdata = ([-1.76779,-2.03906,-2.20414,-2.41137,-2.70126,-2.96848,-3.73906],'cal/mol/K','+|-',[4.55608,4.66138,4.75965,4.71798,4.65046,4.64728,4.57069]),
        H298 = (66.5615,'kcal/mol','+|-',9.47143),
        S298 = (-3.6596,'cal/mol/K','+|-',5.91032),
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
        Cpdata = ([-1.73375,-2.0137,-2.24701,-2.4658,-2.67603,-2.93138,-3.67341],'cal/mol/K','+|-',[4.58717,4.73824,4.87158,4.80884,4.72288,4.71549,4.59522]),
        H298 = (66.5466,'kcal/mol','+|-',9.91906),
        S298 = (-3.17171,'cal/mol/K','+|-',5.70462),
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
        Cpdata = ([0.614687,-0.157514,-0.851982,-1.38525,-2.23553,-2.80081,-3.68045],'cal/mol/K','+|-',[4.6895,4.84527,5.46044,5.93086,6.85701,7.69915,9.19649]),
        H298 = (75.8279,'kcal/mol','+|-',91.3667),
        S298 = (1.66832,'cal/mol/K','+|-',5.67652),
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
        Cpdata = ([0.51047,0.264091,-0.191835,-0.644674,-1.37211,-1.89798,-2.64425],'cal/mol/K','+|-',[2.99978,2.97904,3.47592,4.06383,5.27151,6.38819,8.38389]),
        H298 = (70.4411,'kcal/mol','+|-',92.7224),
        S298 = (1.42452,'cal/mol/K','+|-',3.92847),
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
        Cpdata = ([0.14959,0.227321,0.00312447,-0.312634,-0.810153,-1.13427,-1.51382],'cal/mol/K','+|-',[2.83149,3.11585,3.94172,4.82591,6.53812,8.0519,10.6478]),
        H298 = (51.752,'kcal/mol','+|-',109.278),
        S298 = (0.654455,'cal/mol/K','+|-',3.69607),
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
        Cpdata = ([0.162222,-0.12911,-0.782285,-1.43659,-2.50948,-3.30965,-4.47713],'cal/mol/K','+|-',[2.83388,2.89276,2.87567,2.87407,2.86162,2.8447,2.8286]),
        H298 = (83.2745,'kcal/mol','+|-',4.90043),
        S298 = (1.00991,'cal/mol/K','+|-',4.03602),
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
        Cpdata = ([0.940365,-1.47503,-2.91494,-3.69956,-4.93372,-5.62215,-6.91856],'cal/mol/K','+|-',[5.04569,4.63788,4.84069,5.15438,5.66977,6.5308,6.90873]),
        H298 = (116.603,'kcal/mol','+|-',14.5329),
        S298 = (2.4302,'cal/mol/K','+|-',7.04691),
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
        Cpdata = ([1.47282,-1.33565,-3.08417,-4.05762,-5.57969,-6.53739,-7.92459],'cal/mol/K','+|-',[4.62432,4.6689,4.94582,5.17442,5.3108,5.82008,6.10782]),
        H298 = (114.178,'kcal/mol','+|-',11.8695),
        S298 = (1.30187,'cal/mol/K','+|-',5.8252),
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
        Cpdata = ([-0.646457,-1.5792,-2.14749,-2.36011,-2.51662,-2.66605,-3.40173],'cal/mol/K','+|-',[5.94918,6.56547,6.74038,6.45095,5.67247,5.34622,5.66709]),
        H298 = (88.4221,'kcal/mol','+|-',18.3092),
        S298 = (-0.0839879,'cal/mol/K','+|-',12.2191),
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
        Cpdata = ([-0.474306,-1.21548,-1.88049,-2.26253,-2.66226,-2.95031,-3.98089],'cal/mol/K','+|-',[5.61842,6.28865,6.83251,6.93342,6.2529,5.58841,5.89807]),
        H298 = (93.6889,'kcal/mol','+|-',18.2139),
        S298 = (-0.358862,'cal/mol/K','+|-',8.1032),
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
        Cpdata = ([-1.19238,-2.12816,-2.77813,-3.00758,-3.12228,-3.19737,-3.89226],'cal/mol/K','+|-',[5.67329,6.5376,7.40638,7.68793,6.93806,6.10415,6.42203]),
        H298 = (89.5118,'kcal/mol','+|-',19.863),
        S298 = (0.0537395,'cal/mol/K','+|-',9.82871),
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
        Cpdata = ([0.214718,-0.707453,-1.62458,-2.15475,-2.60433,-2.97702,-4.29846],'cal/mol/K','+|-',[4.81995,4.60786,4.47353,4.47326,4.47295,4.48633,4.90404]),
        H298 = (98.4578,'kcal/mol','+|-',10.9132),
        S298 = (0.869286,'cal/mol/K','+|-',4.51254),
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
        Cpdata = ([-1.5207,-2.45966,-3.04729,-3.20657,-3.24314,-3.24878,-3.79747],'cal/mol/K','+|-',[5.69821,6.784,7.90148,8.284,7.43812,6.46617,6.8026]),
        H298 = (87.3519,'kcal/mol','+|-',19.2171),
        S298 = (-0.136555,'cal/mol/K','+|-',10.7808),
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
        Cpdata = ([-1.72536,-3.73478,-4.82305,-5.07826,-4.81646,-4.37666,-3.92795],'cal/mol/K','+|-',[6.06326,7.26693,8.93478,9.45404,7.98925,6.60147,8.38475]),
        H298 = (80.6985,'kcal/mol','+|-',17.1059),
        S298 = (0.568486,'cal/mol/K','+|-',12.6956),
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
        Cpdata = ([-1.00444,-3.06674,-4.3393,-4.59222,-4.4329,-3.90955,-2.01664],'cal/mol/K','+|-',[8.16953,6.95028,5.98732,5.92984,5.74942,5.20931,4.5503]),
        H298 = (75.157,'kcal/mol','+|-',12.6081),
        S298 = (-2.22066,'cal/mol/K','+|-',14.5965),
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
        Cpdata = ([-2.44629,-4.40281,-5.30679,-5.5643,-5.20001,-4.84377,-5.83927],'cal/mol/K','+|-',[4.57218,9.80485,14.352,15.4778,12.4607,9.48343,11.011]),
        H298 = (86.24,'kcal/mol','+|-',10.4707),
        S298 = (3.35763,'cal/mol/K','+|-',12.7096),
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
        Cpdata = ([-1.55362,-1.5781,-1.65487,-1.71127,-1.97079,-2.30941,-3.25189],'cal/mol/K','+|-',[5.79989,6.00161,6.10917,6.37482,6.51823,6.34811,5.51015]),
        H298 = (94.0683,'kcal/mol','+|-',9.59372),
        S298 = (-0.730241,'cal/mol/K','+|-',11.2833),
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
        Cpdata = ([-2.31201,-1.8654,-1.80664,-1.85543,-2.08712,-2.45037,-3.54191],'cal/mol/K','+|-',[4.68027,4.4765,4.49992,4.55714,4.69155,4.7646,4.62481]),
        H298 = (92.6324,'kcal/mol','+|-',8.7624),
        S298 = (0.702446,'cal/mol/K','+|-',5.43656),
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
        Cpdata = ([0.659362,0.173862,-0.522761,-1.11215,-1.89228,-2.46372,-3.97444],'cal/mol/K','+|-',[4.78517,4.93611,5.19691,5.35983,5.07279,4.75277,5.33193]),
        H298 = (98.0181,'kcal/mol','+|-',9.50949),
        S298 = (-0.872104,'cal/mol/K','+|-',5.52993),
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
        Cpdata = ([0.686987,-0.0307198,-0.831336,-1.46079,-2.15349,-2.6055,-4.2452],'cal/mol/K','+|-',[4.88427,5.16326,5.55089,5.79678,5.39953,4.93066,5.83507]),
        H298 = (99.595,'kcal/mol','+|-',8.48022),
        S298 = (-0.251079,'cal/mol/K','+|-',5.76872),
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
        Cpdata = ([0.953541,0.319817,-0.390247,-0.980945,-1.80107,-2.32905,-3.66195],'cal/mol/K','+|-',[3.02322,3.15586,3.38142,3.61391,3.60205,3.07054,2.82912]),
        H298 = (99.4594,'kcal/mol','+|-',3.433),
        S298 = (-0.716347,'cal/mol/K','+|-',3.65543),
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
        Cpdata = ([1.22503,0.723878,0.141574,-0.333616,-1.15734,-1.98548,-3.66118],'cal/mol/K','+|-',[2.91731,2.82852,2.84254,2.83969,2.8292,2.83257,2.82981]),
        H298 = (99.3115,'kcal/mol','+|-',3.39497),
        S298 = (-1.38479,'cal/mol/K','+|-',2.82856),
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
        Cpdata = ([-0.713292,-1.72041,-2.25115,-2.39799,-2.46007,-2.55569,-3.17687],'cal/mol/K','+|-',[6.09296,6.68585,6.7406,6.30306,5.46455,5.25665,5.53927]),
        H298 = (86.0164,'kcal/mol','+|-',16.4337),
        S298 = (0.022728,'cal/mol/K','+|-',13.5402),
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
        Cpdata = ([-0.270457,-0.983626,-1.50493,-1.79879,-2.18227,-2.50558,-3.27956],'cal/mol/K','+|-',[5.5862,5.3731,5.26327,5.13844,4.98344,5.01245,5.19655]),
        H298 = (85.8862,'kcal/mol','+|-',14.5942),
        S298 = (-0.75505,'cal/mol/K','+|-',11.8024),
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
        Cpdata = ([-0.622828,-1.42888,-1.93968,-2.17674,-2.41484,-2.58128,-3.12352],'cal/mol/K','+|-',[5.49939,5.28802,5.24512,5.19636,5.1349,5.20375,5.40074]),
        H298 = (84.4033,'kcal/mol','+|-',17.3204),
        S298 = (0.0555571,'cal/mol/K','+|-',13.9011),
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
        Cpdata = ([-0.689159,-1.50077,-2.01274,-2.24575,-2.47812,-2.64329,-3.1834],'cal/mol/K','+|-',[5.45422,5.22252,5.17506,5.13407,5.08321,5.15726,5.36531]),
        H298 = (84.3418,'kcal/mol','+|-',17.3872),
        S298 = (-0.535604,'cal/mol/K','+|-',11.7068),
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
        Cpdata = ([-0.93822,-1.86188,-2.31459,-2.51102,-2.64492,-2.67354,-2.85217],'cal/mol/K','+|-',[5.60222,5.70298,5.73234,5.52465,5.21438,5.27298,5.89402]),
        H298 = (85.2626,'kcal/mol','+|-',24.6485),
        S298 = (0.791641,'cal/mol/K','+|-',14.1373),
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
        Cpdata = ([0.370415,-0.47783,-1.0655,-1.48191,-2.0978,-2.48328,-3.07354],'cal/mol/K','+|-',[5.25374,4.84254,4.68107,4.66108,4.67832,4.7832,5.09938]),
        H298 = (84.7748,'kcal/mol','+|-',10.2281),
        S298 = (2.56966,'cal/mol/K','+|-',19.7046),
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
        Cpdata = ([-0.114559,-0.356075,-0.65986,-1.02792,-1.71068,-2.14357,-2.7072],'cal/mol/K','+|-',[4.5201,4.58164,4.59648,4.57605,4.53649,4.47581,4.98499]),
        H298 = (81.6074,'kcal/mol','+|-',8.79727),
        S298 = (-3.43047,'cal/mol/K','+|-',4.85422),
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
        Cpdata = ([0.0163474,-0.937965,-1.45559,-1.85058,-2.35276,-2.63972,-3.12887],'cal/mol/K','+|-',[5.44828,4.87914,4.74647,4.73215,4.95787,5.38179,5.97492]),
        H298 = (84.9227,'kcal/mol','+|-',8.66072),
        S298 = (8.48855,'cal/mol/K','+|-',22.9997),
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
        Cpdata = ([-0.757146,-1.98301,-2.60612,-2.84859,-2.92875,-2.97612,-3.58133],'cal/mol/K','+|-',[4.90218,5.58435,6.46349,6.58479,6.25294,5.87569,5.50601]),
        H298 = (85.7745,'kcal/mol','+|-',11.4435),
        S298 = (0.235196,'cal/mol/K','+|-',9.01168),
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
        Cpdata = ([-0.711919,-1.08893,-1.46536,-1.65452,-1.92409,-2.22947,-3.16892],'cal/mol/K','+|-',[5.38906,4.81296,4.72362,4.87159,5.07283,5.22858,5.12734]),
        H298 = (82.4189,'kcal/mol','+|-',11.3762),
        S298 = (-1.69096,'cal/mol/K','+|-',8.42167),
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
        Cpdata = ([-0.845926,-1.24079,-1.54949,-1.70502,-1.88782,-2.0927,-3.00559],'cal/mol/K','+|-',[5.52976,4.8833,4.80985,5.01977,5.28786,5.4728,5.3287]),
        H298 = (83.9104,'kcal/mol','+|-',11.3025),
        S298 = (-1.82378,'cal/mol/K','+|-',9.50557),
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
        Cpdata = ([-0.976461,-1.37399,-1.69045,-1.86409,-2.04935,-2.23615,-3.07581],'cal/mol/K','+|-',[5.59655,4.85149,4.75503,4.9712,5.27772,5.51562,5.42369]),
        H298 = (83.6394,'kcal/mol','+|-',11.2629),
        S298 = (-1.71761,'cal/mol/K','+|-',10.0212),
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
        Cpdata = ([-0.971392,-1.18321,-1.36565,-1.49345,-1.76986,-2.0462,-2.87041],'cal/mol/K','+|-',[4.65341,4.86974,4.98697,4.9401,4.77253,4.74616,5.22191]),
        H298 = (81.7687,'kcal/mol','+|-',8.81496),
        S298 = (-2.22945,'cal/mol/K','+|-',5.94077),
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
        Cpdata = ([-0.86246,-1.10804,-1.32184,-1.43408,-1.65954,-1.8779,-2.54219],'cal/mol/K','+|-',[4.7983,5.22428,5.4492,5.35952,5.02613,4.93684,5.65256]),
        H298 = (82.0924,'kcal/mol','+|-',9.1177),
        S298 = (-2.42637,'cal/mol/K','+|-',7.04661),
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
        Cpdata = ([-1.34791,-1.73073,-2.07781,-2.32219,-2.54732,-2.82696,-3.68107],'cal/mol/K','+|-',[5.70947,3.40986,2.89799,3.66411,4.64455,4.87803,4.09298]),
        H298 = (84.2921,'kcal/mol','+|-',10.0858),
        S298 = (0.520922,'cal/mol/K','+|-',5.97941),
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
        Cpdata = ([-0.23503,-1.44287,-2.23856,-2.59296,-2.94249,-3.15051,-3.76602],'cal/mol/K','+|-',[5.5251,4.94668,4.6892,4.66811,4.77492,4.88541,4.7672]),
        H298 = (85.4999,'kcal/mol','+|-',8.61057),
        S298 = (-1.23219,'cal/mol/K','+|-',11.8904),
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
        Cpdata = ([0.441991,-1.07775,-2.05236,-2.45035,-2.77976,-2.9527,-3.56638],'cal/mol/K','+|-',[5.54182,4.9908,4.64718,4.64313,4.85001,5.0399,4.82131]),
        H298 = (84.9427,'kcal/mol','+|-',8.42186),
        S298 = (-2.29999,'cal/mol/K','+|-',14.2924),
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
        Cpdata = ([1.30823,-0.541344,-1.82855,-2.22072,-2.30181,-2.25425,-2.98473],'cal/mol/K','+|-',[6.12998,5.37184,4.83435,4.7611,4.74667,4.76674,4.72664]),
        H298 = (84.9044,'kcal/mol','+|-',8.46529),
        S298 = (-7.53171,'cal/mol/K','+|-',8.67745),
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
        Cpdata = ([2.09855,0.0237156,-1.53957,-1.92049,-1.89473,-1.77866,-2.69588],'cal/mol/K','+|-',[6.3374,5.48181,4.97369,4.81383,4.59179,4.47384,4.76231]),
        H298 = (84.724,'kcal/mol','+|-',8.53118),
        S298 = (-9.43181,'cal/mol/K','+|-',6.62925),
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
        Cpdata = ([0.178439,-0.395929,-0.890875,-1.20023,-1.68411,-2.17869,-3.28857],'cal/mol/K','+|-',[5.83272,5.43372,5.18558,4.95155,4.66933,4.67389,4.87478]),
        H298 = (87.4225,'kcal/mol','+|-',9.73846),
        S298 = (-2.54602,'cal/mol/K','+|-',7.62253),
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
        Cpdata = ([0.380435,-0.0871046,-0.590008,-0.959183,-1.62649,-2.2606,-3.55929],'cal/mol/K','+|-',[5.4729,5.06184,4.76563,4.67727,4.6539,4.67509,4.70356]),
        H298 = (87.8336,'kcal/mol','+|-',9.17015),
        S298 = (-1.70406,'cal/mol/K','+|-',5.86278),
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
        Cpdata = ([0.0649674,-0.224322,-0.582104,-0.884461,-1.48804,-2.08204,-3.35379],'cal/mol/K','+|-',[5.30181,5.09858,4.82063,4.69312,4.60756,4.58434,4.56452]),
        H298 = (87.7889,'kcal/mol','+|-',9.2242),
        S298 = (-1.26238,'cal/mol/K','+|-',5.46197),
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
        Cpdata = ([0.461357,0.0373415,-0.483868,-0.894099,-1.64518,-2.30317,-3.60499],'cal/mol/K','+|-',[4.65131,5.30453,5.43298,5.32585,5.08544,4.87037,4.67344]),
        H298 = (86.494,'kcal/mol','+|-',11.6963),
        S298 = (-2.68545,'cal/mol/K','+|-',4.50914),
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
        Cpdata = ([0.28593,-0.00125416,-0.35337,-0.646501,-1.24062,-1.84621,-3.16205],'cal/mol/K','+|-',[4.67484,4.04517,3.28321,2.96477,2.84178,2.89963,2.97185]),
        H298 = (88.4412,'kcal/mol','+|-',5.22283),
        S298 = (-1.15076,'cal/mol/K','+|-',4.30315),
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
        Cpdata = ([-0.4932,-0.569681,-0.604495,-0.726929,-1.16123,-1.7421,-3.21594],'cal/mol/K','+|-',[4.59774,4.11973,3.47065,3.06993,2.82845,2.92499,3.09744]),
        H298 = (88.7471,'kcal/mol','+|-',6.38666),
        S298 = (-0.710294,'cal/mol/K','+|-',4.93741),
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
        Cpdata = ([-0.424108,-1.36402,-1.88839,-2.02609,-1.95901,-2.02646,-2.57121],'cal/mol/K','+|-',[7.37396,6.42887,6.04974,5.50601,4.79938,4.81272,5.26323]),
        H298 = (87.4117,'kcal/mol','+|-',12.7889),
        S298 = (-4.26564,'cal/mol/K','+|-',11.3625),
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
        Cpdata = ([-0.6541,-1.80433,-2.36295,-2.45219,-2.22377,-2.15575,-2.63851],'cal/mol/K','+|-',[7.89567,6.34365,5.74179,5.14795,4.61376,4.84266,5.45533]),
        H298 = (87.88,'kcal/mol','+|-',13.1634),
        S298 = (-3.98959,'cal/mol/K','+|-',12.5628),
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
        Cpdata = ([2.50098,-0.150599,-1.54519,-2.02932,-1.9611,-1.87527,-1.90019],'cal/mol/K','+|-',[7.31629,6.07383,5.50556,4.80803,4.74115,5.60713,6.97571]),
        H298 = (86.6792,'kcal/mol','+|-',9.95754),
        S298 = (-9.86413,'cal/mol/K','+|-',10.2457),
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
        Cpdata = ([0.454632,-0.167716,-0.905438,-1.59475,-2.69293,-3.47892,-4.53057],'cal/mol/K','+|-',[2.95825,3.01573,3.07681,3.05178,2.97932,2.90908,2.83014]),
        H298 = (88.7547,'kcal/mol','+|-',4.9344),
        S298 = (1.29267,'cal/mol/K','+|-',2.83535),
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
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.9591,-5.45697,-6.03557,-5.43682,-3.86893,-2.80987,-2.65609],'cal/mol/K','+|-',[6.63879,7.67973,8.24815,8.03969,6.87033,6.42632,7.05536]),
        H298 = (87.2822,'kcal/mol','+|-',29.3042),
        S298 = (3.96717,'cal/mol/K','+|-',18.7497),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=COC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])CCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 148,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.752188,-1.91778,-2.68069,-3.13496,-3.60292,-3.99653,-4.83722],'cal/mol/K','+|-',[6.07121,6.27304,6.36655,6.29952,6.00414,5.85024,5.85397]),
        H298 = (98.3634,'kcal/mol','+|-',18.6901),
        S298 = (0.965102,'cal/mol/K','+|-',10.0683),
    ),
    shortDesc = """Radical correction fitted to 143 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 149,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.100342,-1.24122,-2.08752,-2.6189,-3.23541,-3.74336,-4.82457],'cal/mol/K','+|-',[5.64335,5.89722,6.05021,5.97111,5.59731,5.43708,5.42035]),
        H298 = (102.093,'kcal/mol','+|-',16.2077),
        S298 = (1.61666,'cal/mol/K','+|-',8.30791),
    ),
    shortDesc = """Radical correction fitted to 82 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 150,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_Sp-2C=1R",
    group = 
"""
1 * C u1 {2,D}
2   C ux {1,D} {3,[S,T,Q,B]}
3   C u0 {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.731104,-1.46325,-1.95707,-2.33084,-2.95747,-3.52514,-4.75723],'cal/mol/K','+|-',[5.57771,5.15027,4.95355,4.8431,4.68413,4.61457,4.67958]),
        H298 = (110.703,'kcal/mol','+|-',10.2501),
        S298 = (1.93798,'cal/mol/K','+|-',6.27857),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 151,
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
        Cpdata = ([1.25626,-0.0904757,-0.874499,-1.33696,-2.07965,-2.78965,-4.53796],'cal/mol/K','+|-',[8.43001,7.27021,6.04807,5.32578,4.65152,4.47572,4.6759]),
        H298 = (117.864,'kcal/mol','+|-',9.52487),
        S298 = (-1.08467,'cal/mol/K','+|-',8.84272),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 152,
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
    index = 153,
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
        Cpdata = ([-1.37889,-1.83238,-2.0585,-2.36515,-2.98721,-3.55084,-4.60887],'cal/mol/K','+|-',[2.95085,2.98478,2.94089,2.87863,2.83358,2.82923,2.83891]),
        H298 = (109.281,'kcal/mol','+|-',3.68394),
        S298 = (2.62419,'cal/mol/K','+|-',3.65241),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 154,
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
    index = 155,
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
    index = 156,
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
    index = 157,
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
    index = 158,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0449195,-1.22171,-2.09898,-2.64421,-3.25984,-3.76253,-4.83049],'cal/mol/K','+|-',[5.65269,5.96726,6.14444,6.06385,5.67196,5.50485,5.48443]),
        H298 = (101.284,'kcal/mol','+|-',15.732),
        S298 = (1.58842,'cal/mol/K','+|-',8.48299),
    ),
    shortDesc = """Radical correction fitted to 76 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 159,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.438336,-0.778409,-1.70694,-2.3544,-3.13823,-3.77849,-5.0214],'cal/mol/K','+|-',[5.29912,5.73868,5.98096,5.95677,5.61769,5.47362,5.45785]),
        H298 = (100.292,'kcal/mol','+|-',13.1682),
        S298 = (1.86652,'cal/mol/K','+|-',8.32003),
    ),
    shortDesc = """Radical correction fitted to 58 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 160,
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
        Cpdata = ([0.514733,-0.883973,-1.9381,-2.56145,-3.25847,-3.87274,-5.14251],'cal/mol/K','+|-',[5.3531,5.99015,6.38662,6.35635,5.90457,5.72217,5.80062]),
        H298 = (102.319,'kcal/mol','+|-',12.5323),
        S298 = (1.84586,'cal/mol/K','+|-',8.97571),
    ),
    shortDesc = """Radical correction fitted to 39 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 161,
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
        Cpdata = ([0.395763,-0.872689,-1.96369,-2.58783,-3.28743,-3.96547,-5.35782],'cal/mol/K','+|-',[5.31082,6.25641,6.78919,6.79744,6.30502,6.0693,6.09894]),
        H298 = (102.87,'kcal/mol','+|-',13.5447),
        S298 = (1.91504,'cal/mol/K','+|-',10.0516),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 162,
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
        Cpdata = ([-0.616096,-1.02392,-1.576,-1.99039,-2.69042,-3.3327,-4.09297],'cal/mol/K','+|-',[4.55372,4.72561,4.91255,5.01659,5.09186,5.11252,4.74645]),
        H298 = (106.05,'kcal/mol','+|-',9.99589),
        S298 = (1.74975,'cal/mol/K','+|-',6.52021),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 163,
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
    index = 164,
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
        Cpdata = ([-0.624278,-1.07473,-1.51207,-1.91204,-2.63471,-3.20362,-4.13558],'cal/mol/K','+|-',[2.98432,3.27845,3.59126,3.75081,3.89401,3.83827,3.32132]),
        H298 = (105.798,'kcal/mol','+|-',6.12287),
        S298 = (1.52894,'cal/mol/K','+|-',5.77268),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 165,
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
    index = 166,
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
        Cpdata = ([-0.349476,-0.606672,-0.910777,-1.27163,-1.9939,-2.60475,-3.70028],'cal/mol/K','+|-',[2.82843,2.8703,3.01943,3.20848,3.53149,3.5857,3.08459]),
        H298 = (104.377,'kcal/mol','+|-',3.87911),
        S298 = (0.118093,'cal/mol/K','+|-',3.29782),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 167,
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
    index = 168,
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
        Cpdata = ([-0.931886,-3.04044,-4.50526,-5.25076,-5.8582,-6.41429,-9.30734],'cal/mol/K','+|-',[4.80899,5.42208,5.66676,5.61603,5.75897,6.4743,4.56298]),
        H298 = (98.0185,'kcal/mol','+|-',8.59928),
        S298 = (7.82813,'cal/mol/K','+|-',8.79834),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 169,
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
        Cpdata = ([-1.43731,-3.81545,-5.34427,-6.02722,-6.53806,-7.22698,-9.23892],'cal/mol/K','+|-',[4.48574,4.93785,5.2278,5.34883,5.9362,6.92693,4.63995]),
        H298 = (97.7001,'kcal/mol','+|-',8.70073),
        S298 = (9.87094,'cal/mol/K','+|-',5.88798),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 170,
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
    index = 171,
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
    index = 172,
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
        Cpdata = ([0.853354,-0.589463,-1.80625,-2.482,-3.19151,-3.89391,-5.31791],'cal/mol/K','+|-',[5.32481,6.61533,7.23838,7.20037,6.51666,6.14625,5.89632]),
        H298 = (101.845,'kcal/mol','+|-',14.2759),
        S298 = (1.32107,'cal/mol/K','+|-',10.4514),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 173,
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
        Cpdata = ([1.1293,-0.217897,-1.46057,-2.1991,-3.079,-3.8612,-5.18525],'cal/mol/K','+|-',[5.19834,6.40175,7.01854,6.98296,6.32197,6.05909,5.86816]),
        H298 = (102.342,'kcal/mol','+|-',13.5202),
        S298 = (1.35192,'cal/mol/K','+|-',10.2307),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 174,
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
        Cpdata = ([0.964845,-0.111929,-1.23473,-1.97605,-2.84848,-3.6433,-5.40601],'cal/mol/K','+|-',[5.3202,6.67017,7.19472,7.06267,6.136,5.73296,5.9284]),
        H298 = (101.297,'kcal/mol','+|-',11.4398),
        S298 = (2.79043,'cal/mol/K','+|-',7.51728),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 175,
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
        Cpdata = ([1.15587,0.345598,-0.700806,-1.4776,-2.51808,-3.46621,-5.23531],'cal/mol/K','+|-',[5.28723,6.33631,6.76286,6.70806,6.0134,5.80231,6.03637]),
        H298 = (100.89,'kcal/mol','+|-',9.6924),
        S298 = (2.50196,'cal/mol/K','+|-',7.68667),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 176,
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
        Cpdata = ([0.465723,-0.548566,-1.58829,-2.35493,-3.50178,-4.60488,-5.58721],'cal/mol/K','+|-',[4.94033,6.19331,7.33515,7.79741,8.03739,9.13143,7.70842]),
        H298 = (100.186,'kcal/mol','+|-',16.7929),
        S298 = (4.33956,'cal/mol/K','+|-',10.2221),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 177,
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
    index = 178,
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
        Cpdata = ([1.36592,0.617735,-0.430702,-1.21058,-2.21869,-3.11966,-5.1282],'cal/mol/K','+|-',[5.41166,6.57431,6.96816,6.82146,5.78942,5.16364,6.02418]),
        H298 = (101.114,'kcal/mol','+|-',9.02296),
        S298 = (1.9427,'cal/mol/K','+|-',7.36276),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 179,
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
        Cpdata = ([1.18851,0.47699,-0.515885,-1.27122,-2.24529,-3.06977,-5.12299],'cal/mol/K','+|-',[5.356,6.71552,7.20021,7.05428,5.93549,5.23305,6.19694]),
        H298 = (101.018,'kcal/mol','+|-',9.01105),
        S298 = (2.35319,'cal/mol/K','+|-',6.99935),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 180,
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
        Cpdata = ([1.19057,0.56235,-0.35803,-1.13703,-2.22374,-3.10094,-5.14535],'cal/mol/K','+|-',[4.95758,6.03046,6.45376,6.44729,5.65687,5.27834,7.39626]),
        H298 = (100.686,'kcal/mol','+|-',8.41418),
        S298 = (0.687588,'cal/mol/K','+|-',5.45498),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 181,
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
    index = 182,
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
    index = 183,
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
    index = 184,
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
    index = 185,
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
    index = 186,
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
    index = 187,
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
        Cpdata = ([-0.467867,-3.54338,-5.23912,-5.71442,-5.32654,-4.97148,-6.68631],'cal/mol/K','+|-',[4.84987,4.64276,4.49899,4.47761,4.58954,4.5665,4.51848]),
        H298 = (107.25,'kcal/mol','+|-',28.1582),
        S298 = (4.9539,'cal/mol/K','+|-',4.62566),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 188,
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
    index = 189,
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
    index = 190,
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
        Cpdata = ([1.5594,-0.495045,-2.05122,-2.78248,-3.68187,-4.43107,-4.60786],'cal/mol/K','+|-',[4.90983,6.06035,6.99269,7.24883,7.15311,7.1966,5.88992]),
        H298 = (105.587,'kcal/mol','+|-',19.9229),
        S298 = (-2.41032,'cal/mol/K','+|-',13.3335),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 191,
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
    index = 192,
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
        Cpdata = ([1.55496,-0.149385,-1.41007,-1.92585,-2.71648,-3.42086,-3.91573],'cal/mol/K','+|-',[5.02931,6.09046,6.47028,5.87198,5.02802,4.77171,4.58269]),
        H298 = (103.278,'kcal/mol','+|-',8.663),
        S298 = (-3.35662,'cal/mol/K','+|-',13.7805),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 193,
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
        Cpdata = ([1.42609,-0.285354,-1.52814,-2.02744,-2.76916,-3.4636,-3.83138],'cal/mol/K','+|-',[5.19264,6.61731,7.1266,6.35215,5.24007,4.88847,4.601]),
        H298 = (103.108,'kcal/mol','+|-',8.64574),
        S298 = (-3.89951,'cal/mol/K','+|-',15.8848),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 194,
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
    index = 195,
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
        Cpdata = ([0.447799,-2.1696,-3.71972,-3.83985,-3.88981,-4.25963,-3.36664],'cal/mol/K','+|-',[4.97873,5.68426,5.73928,5.19277,4.66954,4.61169,4.473]),
        H298 = (103.246,'kcal/mol','+|-',9.26268),
        S298 = (-9.40643,'cal/mol/K','+|-',14.2423),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 196,
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
    index = 197,
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
    index = 198,
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
    index = 199,
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
        Cpdata = ([-0.511174,-1.93404,-2.62708,-2.78601,-2.54202,-3.12279,-5.4361],'cal/mol/K','+|-',[5.04463,6.13129,6.84999,6.99142,6.93192,6.74621,6.14854]),
        H298 = (92.4453,'kcal/mol','+|-',8.70153),
        S298 = (-1.4297,'cal/mol/K','+|-',9.71715),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 200,
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
        Cpdata = ([-1.05129,-3.14471,-4.10065,-4.25555,-3.91171,-4.40416,-6.64322],'cal/mol/K','+|-',[4.88828,4.47301,4.66166,5.09219,5.57476,5.62288,4.54289]),
        H298 = (92.0377,'kcal/mol','+|-',8.814),
        S298 = (-0.323618,'cal/mol/K','+|-',11.8103),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 201,
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
    index = 202,
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
    index = 203,
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
        Cpdata = ([0.795933,-0.910643,-1.87762,-2.49908,-3.19002,-3.65357,-4.63362],'cal/mol/K','+|-',[5.50317,5.43277,5.46214,5.3059,4.92575,4.86035,4.96582]),
        H298 = (100.953,'kcal/mol','+|-',9.42639),
        S298 = (1.68235,'cal/mol/K','+|-',5.99488),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 204,
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
        Cpdata = ([0.625305,-0.462439,-1.35449,-2.03677,-2.94935,-3.61067,-4.71134],'cal/mol/K','+|-',[4.57901,5.86691,6.68692,6.98914,6.48183,5.81669,4.9583]),
        H298 = (99.4257,'kcal/mol','+|-',8.36045),
        S298 = (3.07819,'cal/mol/K','+|-',5.28893),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 205,
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
    index = 206,
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
        Cpdata = ([1.73484,-2.87603,-3.91083,-4.19666,-3.83996,-3.43472,-3.70337],'cal/mol/K','+|-',[8.5954,6.27751,5.6398,5.01636,4.74594,5.24538,6.20067]),
        H298 = (98.0824,'kcal/mol','+|-',8.40343),
        S298 = (0.268444,'cal/mol/K','+|-',6.75661),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 207,
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
        Cpdata = ([1.98321,-4.03774,-4.76692,-4.65665,-3.65708,-2.84934,-2.60257],'cal/mol/K','+|-',[11.2375,5.14049,5.10153,5.02488,4.92394,5.17727,5.27392]),
        H298 = (98.1249,'kcal/mol','+|-',8.45173),
        S298 = (-0.956449,'cal/mol/K','+|-',5.94095),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 208,
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
    index = 209,
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
    index = 210,
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
    index = 211,
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
        Cpdata = ([1.5703,0.126999,-1.20718,-1.99646,-2.9502,-3.49991,-4.7552],'cal/mol/K','+|-',[4.73411,5.0153,5.13789,4.95575,4.74817,4.62353,4.49354]),
        H298 = (102.328,'kcal/mol','+|-',12.2395),
        S298 = (2.63954,'cal/mol/K','+|-',5.50281),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 212,
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
    index = 213,
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
        Cpdata = ([1.62222,0.614508,-0.539515,-1.41421,-2.53866,-3.23726,-4.65327],'cal/mol/K','+|-',[4.97584,4.96009,4.70075,4.58066,4.58536,4.5933,4.48714]),
        H298 = (99.9693,'kcal/mol','+|-',9.81647),
        S298 = (2.08245,'cal/mol/K','+|-',5.75445),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 214,
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
    index = 215,
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
        Cpdata = ([0.146988,-0.737139,-1.55514,-2.2181,-3.13459,-3.83466,-4.94133],'cal/mol/K','+|-',[4.66016,4.65759,4.7424,4.8494,4.79881,4.78637,4.73474]),
        H298 = (102.035,'kcal/mol','+|-',8.48513),
        S298 = (1.18016,'cal/mol/K','+|-',6.07972),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 216,
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
        Cpdata = ([0.474214,-0.587365,-1.58449,-2.36168,-3.33992,-4.05753,-5.14003],'cal/mol/K','+|-',[4.5989,4.76502,4.95847,5.10979,4.98002,4.94351,4.87055]),
        H298 = (101.852,'kcal/mol','+|-',8.66143),
        S298 = (0.375314,'cal/mol/K','+|-',6.25366),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 217,
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
    index = 218,
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
    index = 219,
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
    index = 220,
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
        Cpdata = ([0.109186,-0.903733,-1.60255,-2.21533,-3.07258,-3.69555,-4.82867],'cal/mol/K','+|-',[5.38888,5.47332,5.37117,5.39421,5.34209,5.26809,4.99601]),
        H298 = (97.3269,'kcal/mol','+|-',11.776),
        S298 = (2.54347,'cal/mol/K','+|-',6.77111),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 221,
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
        Cpdata = ([1.84466,-0.909553,-2.15188,-3.18679,-4.5338,-5.34272,-6.11114],'cal/mol/K','+|-',[5.64651,8.27066,7.80936,7.5158,6.84589,6.36614,5.64794]),
        H298 = (101.837,'kcal/mol','+|-',9.00468),
        S298 = (1.03133,'cal/mol/K','+|-',7.06708),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 222,
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
    index = 223,
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
        Cpdata = ([2.49304,-0.521321,-1.81368,-2.7889,-4.07918,-4.95132,-5.81438],'cal/mol/K','+|-',[4.62682,9.14931,8.62776,8.14652,7.12703,6.61095,5.81104]),
        H298 = (102.204,'kcal/mol','+|-',8.60047),
        S298 = (0.35241,'cal/mol/K','+|-',6.76473),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 224,
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
    index = 225,
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
    index = 226,
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
    index = 227,
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
        Cpdata = ([-0.380308,-0.902092,-1.44761,-1.94133,-2.66045,-3.23096,-4.46695],'cal/mol/K','+|-',[4.94149,4.73926,4.70565,4.73483,4.67519,4.61241,4.60867]),
        H298 = (96.4589,'kcal/mol','+|-',11.4742),
        S298 = (2.96997,'cal/mol/K','+|-',6.62805),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 228,
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
        Cpdata = ([-0.461806,-0.901198,-1.41209,-1.88419,-2.56023,-3.11024,-4.40019],'cal/mol/K','+|-',[5.03915,4.80383,4.75691,4.78659,4.69394,4.60329,4.62782]),
        H298 = (97.7193,'kcal/mol','+|-',9.70054),
        S298 = (3.41723,'cal/mol/K','+|-',6.70121),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 229,
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
        Cpdata = ([-0.825755,-1.02181,-1.42021,-1.84283,-2.56716,-3.22782,-4.51602],'cal/mol/K','+|-',[5.10584,4.93011,4.76007,4.70924,4.61759,4.54886,4.47658]),
        H298 = (97.4486,'kcal/mol','+|-',9.53021),
        S298 = (2.2946,'cal/mol/K','+|-',5.49732),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 230,
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
    index = 231,
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
        Cpdata = ([-0.24493,-0.550682,-1.073,-1.52976,-2.30861,-3.03973,-4.4894],'cal/mol/K','+|-',[4.75984,4.71829,4.66424,4.63173,4.55226,4.51332,4.47773]),
        H298 = (96.6857,'kcal/mol','+|-',9.72827),
        S298 = (1.46177,'cal/mol/K','+|-',4.66274),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 232,
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
        Cpdata = ([-0.321809,-0.485338,-0.870235,-1.28185,-2.07684,-2.84321,-4.45259],'cal/mol/K','+|-',[5.18008,5.08311,4.86212,4.72953,4.54253,4.4792,4.48325]),
        H298 = (97.8507,'kcal/mol','+|-',11.3709),
        S298 = (1.8306,'cal/mol/K','+|-',4.62288),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 233,
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
    index = 234,
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
    index = 235,
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
        Cpdata = ([-0.0493313,-0.764499,-1.40289,-1.93106,-2.55237,-2.97699,-4.26891],'cal/mol/K','+|-',[3.6391,3.29163,3.44393,3.63339,3.44871,3.1907,3.40705]),
        H298 = (97.9683,'kcal/mol','+|-',7.05522),
        S298 = (4.68953,'cal/mol/K','+|-',6.69372),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 236,
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
        Cpdata = ([-0.70882,-1.21081,-1.77051,-2.22714,-2.64256,-2.92326,-4.38039],'cal/mol/K','+|-',[2.83689,2.98144,3.53241,4.03722,3.94867,3.50597,3.86234]),
        H298 = (96.0546,'kcal/mol','+|-',5.27547),
        S298 = (3.20537,'cal/mol/K','+|-',5.3615),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 237,
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
    index = 238,
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
    index = 239,
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
        Cpdata = ([-0.00774594,-0.906178,-1.61001,-2.20258,-3.11859,-3.78281,-4.77213],'cal/mol/K','+|-',[4.4808,4.50207,4.51782,4.5302,4.5221,4.50976,4.5049]),
        H298 = (89.3141,'kcal/mol','+|-',8.7102),
        S298 = (0.925367,'cal/mol/K','+|-',4.51977),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 240,
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
    index = 241,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_1R->C_Sp-3R!H-2C",
    group = 
"""
1 * C u1 {2,S}
2   C ux {1,S} {3,S}
3   C ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.89818,0.0651309,-0.803104,-1.72906,-2.79304,-3.60304,-4.98065],'cal/mol/K','+|-',[4.98606,5.10173,5.03549,5.10481,4.83334,4.77625,4.72897]),
        H298 = (102.344,'kcal/mol','+|-',8.78887),
        S298 = (1.95641,'cal/mol/K','+|-',5.44998),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 242,
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
        Cpdata = ([0.706159,-1.05852,-1.96404,-3.29852,-3.9611,-4.50189,-5.92638],'cal/mol/K','+|-',[4.49916,4.49099,4.88077,4.65097,4.83591,5.20745,4.68791]),
        H298 = (101.985,'kcal/mol','+|-',11.612),
        S298 = (3.92299,'cal/mol/K','+|-',5.6177),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 243,
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
    index = 244,
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
        Cpdata = ([0.962187,0.439681,-0.416125,-1.20591,-2.40368,-3.30342,-4.66541],'cal/mol/K','+|-',[5.262,5.10962,4.87916,4.728,4.54423,4.51119,4.55514]),
        H298 = (102.399,'kcal/mol','+|-',8.42447),
        S298 = (1.30088,'cal/mol/K','+|-',4.64784),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 245,
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
        Cpdata = ([1.3974,0.830197,-0.0963367,-0.94918,-2.26144,-3.23309,-4.62408],'cal/mol/K','+|-',[3.23131,3.13723,2.96658,2.89263,2.82912,2.87904,3.00699]),
        H298 = (102.49,'kcal/mol','+|-',3.48402),
        S298 = (1.09087,'cal/mol/K','+|-',2.87863),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 246,
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
    index = 247,
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
    index = 248,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->C_N-Sp-2C=1R_N-1R->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.58795,-2.63715,-3.35075,-3.56957,-3.64813,-3.71158,-4.22092],'cal/mol/K','+|-',[5.69077,5.86679,6.07073,6.12144,5.85267,5.67285,5.44869]),
        H298 = (104.481,'kcal/mol','+|-',21.5013),
        S298 = (0.700482,'cal/mol/K','+|-',8.96928),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 249,
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
        Cpdata = ([-1.11247,-1.257,-1.55572,-1.77118,-2.20343,-2.54968,-4.06704],'cal/mol/K','+|-',[4.48731,4.50709,4.53,4.54463,4.53238,4.51966,5.46484]),
        H298 = (89.5128,'kcal/mol','+|-',54.4799),
        S298 = (-1.14464,'cal/mol/K','+|-',4.66833),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 250,
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
    index = 251,
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
    index = 252,
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
        Cpdata = ([-0.881225,-2.53187,-3.88501,-4.34385,-4.49788,-4.73183,-5.33992],'cal/mol/K','+|-',[4.62863,5.14512,5.37808,5.56605,5.62153,5.46807,5.66323]),
        H298 = (109.401,'kcal/mol','+|-',9.15831),
        S298 = (-0.139881,'cal/mol/K','+|-',6.81788),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 253,
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
        Cpdata = ([-0.905893,-2.59719,-4.08041,-4.64904,-4.83216,-5.09573,-5.75429],'cal/mol/K','+|-',[4.65958,5.26488,5.4188,5.44919,5.45101,5.17882,5.28318]),
        H298 = (109.039,'kcal/mol','+|-',8.78269),
        S298 = (0.450611,'cal/mol/K','+|-',6.20208),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 254,
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
    index = 255,
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
    index = 256,
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
        Cpdata = ([-1.03919,-2.6065,-4.07011,-4.78292,-5.07875,-5.35299,-5.61357],'cal/mol/K','+|-',[4.59696,4.76483,4.6792,4.86419,5.41102,5.49715,5.24883]),
        H298 = (108.865,'kcal/mol','+|-',8.68653),
        S298 = (1.12357,'cal/mol/K','+|-',4.76234),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 257,
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
    index = 258,
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
    index = 259,
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
    index = 260,
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
    index = 261,
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
        Cpdata = ([-2.03886,-3.06142,-3.59747,-3.70809,-3.65589,-3.56471,-3.75425],'cal/mol/K','+|-',[6.32743,6.3783,6.51527,6.49839,6.10776,5.86182,5.23522]),
        H298 = (106.412,'kcal/mol','+|-',9.61018),
        S298 = (1.58568,'cal/mol/K','+|-',10.5412),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 262,
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
        Cpdata = ([-0.28201,-2.62119,-4.16866,-4.68699,-4.89689,-4.75067,-4.41874],'cal/mol/K','+|-',[6.90255,7.64435,7.68468,7.54558,6.7352,6.31249,5.84479]),
        H298 = (107.961,'kcal/mol','+|-',12.1328),
        S298 = (5.1118,'cal/mol/K','+|-',13.5822),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 263,
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
        Cpdata = ([0.517345,-1.47921,-3.06646,-3.64074,-3.85629,-3.73847,-3.90528],'cal/mol/K','+|-',[8.0214,8.72717,8.86127,8.72149,7.35708,6.66084,6.59967]),
        H298 = (105.653,'kcal/mol','+|-',14.2476),
        S298 = (6.20268,'cal/mol/K','+|-',17.8407),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 264,
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
        Cpdata = ([-0.602899,-2.42992,-4.13263,-4.88072,-5.11696,-5.00238,-5.30447],'cal/mol/K','+|-',[8.86379,10.5183,10.4768,9.75845,7.07889,5.51311,4.48613]),
        H298 = (102.7,'kcal/mol','+|-',11.2667),
        S298 = (1.53458,'cal/mol/K','+|-',9.67451),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 265,
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
    index = 266,
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
    index = 267,
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
    index = 268,
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
        Cpdata = ([-3.37664,-3.58424,-3.42776,-3.21033,-2.77456,-2.58567,-3.24348],'cal/mol/K','+|-',[4.76679,5.62244,6.34677,6.46769,6.14539,6.08854,5.43153]),
        H298 = (106.433,'kcal/mol','+|-',9.32312),
        S298 = (-0.5149,'cal/mol/K','+|-',8.00465),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 269,
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
        Cpdata = ([-2.8256,-2.75222,-2.53066,-2.32653,-1.91644,-1.63243,-2.44586],'cal/mol/K','+|-',[4.4726,5.84798,7.36955,7.67691,7.02252,6.59076,5.47521]),
        H298 = (105.171,'kcal/mol','+|-',9.34792),
        S298 = (-2.30443,'cal/mol/K','+|-',7.77012),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 270,
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
    index = 271,
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
    index = 272,
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
    index = 273,
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
    index = 274,
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
    index = 275,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.76704,-2.9711,-3.60419,-3.93842,-4.17509,-4.39069,-4.85692],'cal/mol/K','+|-',[6.17783,6.28423,6.43492,6.48768,6.44905,6.38678,6.49824]),
        H298 = (91.7736,'kcal/mol','+|-',15.261),
        S298 = (-0.0492958,'cal/mol/K','+|-',12.1188),
    ),
    shortDesc = """Radical correction fitted to 61 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 276,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.481461,-1.77876,-2.36796,-2.77031,-3.34135,-3.73218,-4.37842],'cal/mol/K','+|-',[5.21885,5.78805,5.93876,5.85444,5.46479,5.15421,4.92368]),
        H298 = (99.4555,'kcal/mol','+|-',10.4343),
        S298 = (3.77568,'cal/mol/K','+|-',13.1488),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 277,
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
        Cpdata = ([-0.542523,-2.0716,-2.66803,-3.07355,-3.6379,-4.02203,-4.66522],'cal/mol/K','+|-',[5.33241,5.73028,5.89414,5.84333,5.48854,5.19564,4.89102]),
        H298 = (98.6882,'kcal/mol','+|-',10.1777),
        S298 = (4.51158,'cal/mol/K','+|-',14.8844),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 278,
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
        Cpdata = ([-0.357829,-1.6785,-2.46974,-2.92046,-3.49133,-3.95906,-4.63521],'cal/mol/K','+|-',[4.83436,4.54822,4.73399,4.90541,5.07014,5.11315,5.14467]),
        H298 = (97.5037,'kcal/mol','+|-',11.4981),
        S298 = (7.66856,'cal/mol/K','+|-',21.3694),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 279,
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
    index = 280,
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
    index = 281,
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
        Cpdata = ([-0.700832,-2.40854,-2.838,-3.20478,-3.76354,-4.076,-4.69094],'cal/mol/K','+|-',[5.97397,6.8065,7.08872,6.91549,6.14359,5.53914,4.86848]),
        H298 = (99.7887,'kcal/mol','+|-',9.1856),
        S298 = (1.80561,'cal/mol/K','+|-',6.41636),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 282,
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
    index = 283,
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
    index = 284,
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
    index = 285,
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
    index = 286,
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
    index = 287,
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
    index = 288,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.10791,-3.28725,-3.93197,-4.24815,-4.39616,-4.5653,-4.9838],'cal/mol/K','+|-',[6.25023,6.29019,6.43669,6.53911,6.6409,6.65099,6.84814]),
        H298 = (89.1734,'kcal/mol','+|-',12.9153),
        S298 = (-1.06349,'cal/mol/K','+|-',11.1533),
    ),
    shortDesc = """Radical correction fitted to 51 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 289,
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
        Cpdata = ([-3.23621,-3.81771,-4.00115,-4.00198,-3.81305,-3.7704,-3.8683],'cal/mol/K','+|-',[6.02378,7.18912,7.83438,7.82033,7.38078,7.16338,7.07147]),
        H298 = (92.1107,'kcal/mol','+|-',16.1828),
        S298 = (1.11572,'cal/mol/K','+|-',11.703),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 290,
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
        Cpdata = ([-3.81564,-4.6773,-4.87805,-4.70418,-4.12287,-3.79786,-3.49174],'cal/mol/K','+|-',[6.17061,7.285,8.07857,8.32216,8.12911,7.9647,7.7769]),
        H298 = (89.1223,'kcal/mol','+|-',15.842),
        S298 = (1.57991,'cal/mol/K','+|-',13.5858),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 291,
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
        Cpdata = ([-5.79514,-7.63866,-8.26603,-8.15818,-7.14834,-6.35674,-5.31743],'cal/mol/K','+|-',[4.71836,5.27974,7.19809,7.70954,6.67469,6.02261,5.93549]),
        H298 = (92.4452,'kcal/mol','+|-',14.3391),
        S298 = (4.14017,'cal/mol/K','+|-',9.07095),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 292,
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
        Cpdata = ([-5.89257,-7.26105,-7.71,-7.57434,-6.66826,-6.02013,-5.45478],'cal/mol/K','+|-',[4.8791,5.33037,8.10858,8.86474,7.46093,6.73625,6.8991]),
        H298 = (91.2966,'kcal/mol','+|-',12.3559),
        S298 = (4.32101,'cal/mol/K','+|-',11.6111),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 293,
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
    index = 294,
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
    index = 295,
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
    index = 296,
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
        Cpdata = ([-2.92265,-3.14641,-2.96948,-2.56171,-1.91213,-1.71412,-1.71548],'cal/mol/K','+|-',[6.23245,6.43258,6.23624,6.37138,7.65417,8.56361,9.31877]),
        H298 = (86.7596,'kcal/mol','+|-',23.6071),
        S298 = (0.818792,'cal/mol/K','+|-',19.4064),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 297,
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
        Cpdata = ([-2.86861,-3.20452,-3.2499,-2.97865,-2.5445,-2.56901,-2.66349],'cal/mol/K','+|-',[6.84631,7.10522,6.64295,6.56001,7.77192,8.32073,9.07395]),
        H298 = (87.765,'kcal/mol','+|-',26.0636),
        S298 = (-2.47798,'cal/mol/K','+|-',11.2737),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 298,
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
    index = 299,
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
    index = 300,
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
    index = 301,
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
        Cpdata = ([-1.78763,-1.66872,-1.80889,-2.24649,-3.03851,-3.70177,-4.80968],'cal/mol/K','+|-',[2.89155,3.404,4.19701,4.31625,4.31938,4.12664,3.40822]),
        H298 = (97.8271,'kcal/mol','+|-',4.31393),
        S298 = (-0.0447361,'cal/mol/K','+|-',4.11433),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 302,
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
    index = 303,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.70079,-3.09585,-3.90701,-4.33698,-4.60656,-4.85212,-5.3863],'cal/mol/K','+|-',[6.17789,5.98451,5.97904,6.12581,6.40183,6.45076,6.66649]),
        H298 = (87.6703,'kcal/mol','+|-',10.1022),
        S298 = (-1.84981,'cal/mol/K','+|-',10.7176),
    ),
    shortDesc = """Radical correction fitted to 41 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 304,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_Sp-4BrCClFINPSSi-3R!H",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54499,-3.02247,-3.89619,-4.36364,-4.68542,-4.9936,-5.64302],'cal/mol/K','+|-',[6.08253,5.96991,6.00736,6.18152,6.4703,6.47181,6.5254]),
        H298 = (87.9682,'kcal/mol','+|-',10.0951),
        S298 = (-2.34087,'cal/mol/K','+|-',9.27551),
    ),
    shortDesc = """Radical correction fitted to 39 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O[O])C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1=COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OOCC(O[O])C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C1(C)OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(COCOO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[O]OCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CC1C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 305,
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
        Cpdata = ([-3.70401,-4.03932,-4.04618,-3.99414,-3.59261,-3.03301,-2.08553],'cal/mol/K','+|-',[7.56198,7.35459,6.88591,6.33127,5.72979,5.37378,4.55954]),
        H298 = (85.0573,'kcal/mol','+|-',8.88302),
        S298 = (4.46378,'cal/mol/K','+|-',26.6298),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 306,
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
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_N-Sp-4BrCClFINPSSi-3R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->C_N-1R->C_Ext-3R!H-R_N-4R!H->O_N-Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R
"""
)

