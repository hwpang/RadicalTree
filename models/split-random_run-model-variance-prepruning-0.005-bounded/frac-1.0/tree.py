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
        Cpdata = ([-0.615693,-1.59215,-2.30435,-2.72863,-3.18236,-3.57577,-4.38525],'cal/mol/K','+|-',[3.95404,4.57028,4.86063,4.81533,4.44866,4.17769,4.10484]),
        H298 = (94.3742,'kcal/mol','+|-',25.0186),
        S298 = (0.48471,'cal/mol/K','+|-',10.0141),
    ),
    shortDesc = """Radical correction fitted to 2531 radicals""",
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
        Cpdata = ([-0.615693,-1.59215,-2.30435,-2.72863,-3.18236,-3.57577,-4.38525],'cal/mol/K','+|-',[3.95404,4.57028,4.86063,4.81533,4.44866,4.17769,4.10484]),
        H298 = (94.3742,'kcal/mol','+|-',25.0186),
        S298 = (0.48471,'cal/mol/K','+|-',10.0141),
    ),
    shortDesc = """Radical correction fitted to 2531 radicals""",
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
        Cpdata = ([0.110765,-1.07399,-2.00408,-2.57449,-3.26046,-3.81517,-4.8774],'cal/mol/K','+|-',[2.79391,3.29247,3.67295,3.67884,3.37641,3.29408,3.78653]),
        H298 = (93.4077,'kcal/mol','+|-',32.8218),
        S298 = (0.958734,'cal/mol/K','+|-',7.14887),
    ),
    shortDesc = """Radical correction fitted to 466 radicals""",
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
        Cpdata = ([0.163381,-1.08896,-2.01641,-2.54453,-3.18554,-3.70935,-4.55825],'cal/mol/K','+|-',[2.95685,3.3894,3.61981,3.5163,3.16053,3.07287,3.00066]),
        H298 = (86.1056,'kcal/mol','+|-',33.5843),
        S298 = (0.374881,'cal/mol/K','+|-',7.5711),
    ),
    shortDesc = """Radical correction fitted to 267 radicals""",
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
        Cpdata = ([0.164225,-1.17899,-2.08319,-2.57432,-3.16269,-3.65028,-4.46301],'cal/mol/K','+|-',[3.02541,3.4207,3.4178,3.10733,2.55298,2.31135,2.11849]),
        H298 = (83.463,'kcal/mol','+|-',27.5592),
        S298 = (-0.226622,'cal/mol/K','+|-',7.52573),
    ),
    shortDesc = """Radical correction fitted to 183 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.549687,-2.51576,-3.31601,-3.63384,-3.94468,-4.28522,-4.43188],'cal/mol/K','+|-',[2.86472,5.35547,5.46172,5.05882,3.90112,2.93567,3.9555]),
        H298 = (81.0936,'kcal/mol','+|-',41.0312),
        S298 = (1.16303,'cal/mol/K','+|-',7.97475),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 {1,S} {3,D} {4,S}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 {2,S} {7,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {6,S}
6   R!H u0 {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.984941,-1.04459,-2.37885,-3.06641,-4.07805,-5.14686,-2.46275],'cal/mol/K','+|-',[3.31223,2.90366,2.84131,3.61159,4.57053,3.98602,10.5899]),
        H298 = (124.227,'kcal/mol','+|-',94.7198),
        S298 = (1.16816,'cal/mol/K','+|-',7.88076),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Ext-4R!H-R_Int-6R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 {1,S} {3,D} {4,S}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 {2,S} {7,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {6,S}
6   R!H u0 {1,S} {5,S}
7   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.600653,-1.03172,-2.15084,-2.36973,-2.99362,-4.29058,0.127238],'cal/mol/K','+|-',[3.88125,3.67766,3.40075,3.33241,3.19721,3.29335,7.74384]),
        H298 = (151.534,'kcal/mol','+|-',5.90761),
        S298 = (3.14285,'cal/mol/K','+|-',5.2243),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Ext-4R!H-R_Int-6R!H-1R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D} {4,S}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {2,S} {7,[S,D,T,B,Q]}
5   R!H ux r1 {3,[S,D,T,B,Q]} {6,S}
6   R!H u0 r1 {1,S} {5,S}
7   O   ux r1 {4,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.39628,-0.367913,-1.70853,-1.99808,-2.82698,-3.96536,-2.37194],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (151.485,'kcal/mol','+|-',4.17612),
        S298 = (4.61311,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1C2=COC1OOC2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 9,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.875879,-2.40358,-2.99213,-3.29419,-3.60772,-3.87431,-4.60831],'cal/mol/K','+|-',[2.7252,6.3182,6.46469,5.97077,4.5049,3.19911,1.94656]),
        H298 = (75.4869,'kcal/mol','+|-',22.4254),
        S298 = (1.65867,'cal/mol/K','+|-',9.00248),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 10,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.754063,-1.26412,-1.92982,-2.38044,-3.01527,-3.59842,-4.66998],'cal/mol/K','+|-',[3.14553,3.33029,3.49642,3.50739,3.10707,2.45444,1.96489]),
        H298 = (69.5533,'kcal/mol','+|-',20.8092),
        S298 = (-0.0799181,'cal/mol/K','+|-',6.62428),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 11,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_4R!H->C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 {1,S} {3,D} {4,S}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {2,S}
5   C   u0 {3,S} {6,D} {7,S}
6   R!H ux {5,D}
7   R!H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.140577,-0.342191,-1.04128,-1.47558,-2.24804,-3.18605,-4.56246],'cal/mol/K','+|-',[5.63918,6.05624,5.9548,5.71852,5.27632,4.34587,3.53261]),
        H298 = (58.2391,'kcal/mol','+|-',11.2993),
        S298 = (-1.66748,'cal/mol/K','+|-',11.7019),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 12,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_4R!H->C_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D} {4,S}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r0 {2,S}
5   C   u0 r1 {3,S} {6,D} {7,S}
6   R!H ux r0 {5,D}
7   R!H u0 r1 {5,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5102,-2.16832,-2.82522,-3.16012,-3.74134,-4.24,-5.11916],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (61.6449,'kcal/mol','+|-',4.17612),
        S298 = (2.31582,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C(C)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 13,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_4R!H->C_Ext-1R-R_Ext-7R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux {5,D}
7   C ux {1,[S,D,T,B,Q]} {8,D}
8   C u0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46009,-2.12378,-3.09364,-3.65204,-4.07584,-4.27739,-5.00816],'cal/mol/K','+|-',[3.33822,3.16837,3.45541,3.51663,3.20644,3.18124,3.16729]),
        H298 = (62.7265,'kcal/mol','+|-',15.39),
        S298 = (-0.539106,'cal/mol/K','+|-',5.94038),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 14,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_4R!H->C_Ext-1R-R_Ext-7R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C   ux r1 {5,D}
7   C   ux r1 {1,[S,D,T,B,Q]} {8,D}
8   C   u0 {7,D}
9   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08198,-2.19324,-3.58607,-4.19595,-4.26333,-4.15478,-4.94516],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (67.7511,'kcal/mol','+|-',4.17612),
        S298 = (-2.31703,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=CCC([C]2C=CCCC2)=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 15,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   O ux {2,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01984,-3.75023,-4.24759,-4.37409,-4.30789,-4.20036,-4.53543],'cal/mol/K','+|-',[3.20581,8.82929,9.17094,8.46634,6.36844,4.68891,2.88728]),
        H298 = (82.0758,'kcal/mol','+|-',20.3111),
        S298 = (3.71336,'cal/mol/K','+|-',11.0366),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 16,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_N-4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   O   ux r0 {2,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C   u0 r1 {5,D}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8039,-3.77002,-4.28219,-4.28045,-4.00495,-3.85134,-4.65462],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.587,'kcal/mol','+|-',4.17612),
        S298 = (4.78356,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=C(O)C=C[CH]1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_N-4R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {7,S}
2   C   u0 {1,S} {3,D} {4,S}
3   C   u0 r1 {2,D} {5,S}
4   O   u0 {2,S}
5   C   u0 {3,S} {6,D}
6   C   u0 {5,D}
7   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.361475,-6.32644,-7.07038,-6.91196,-6.14989,-5.42051,-5.06153],'cal/mol/K','+|-',[3.3718,14.0665,14.2083,13.3612,10.2552,7.78888,4.8455]),
        H298 = (90.1136,'kcal/mol','+|-',10.1071),
        S298 = (6.41436,'cal/mol/K','+|-',18.1997),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 18,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_N-4R!H->C_Ext-1R-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {7,S}
2   C   u0 r1 {1,S} {3,D} {4,S}
3   C   u0 r1 {2,D} {5,S}
4   O   u0 r0 {2,S}
5   C   u0 r1 {3,S} {6,D}
6   C   u0 r1 {5,D} {8,[S,D,T,B,Q]}
7   R!H u0 {1,S}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.775149,-11.1724,-11.9678,-11.5017,-9.59895,-7.93713,-6.35955],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.0134,'kcal/mol','+|-',4.17612),
        S298 = (12.751,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CC=COC[CH]1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 19,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.630814,-3.19335,-4.10401,-4.31361,-4.37332,-4.56123,-4.87778],'cal/mol/K','+|-',[3.29477,5.14522,5.30915,4.92167,3.7523,2.93277,2.78243]),
        H298 = (79.248,'kcal/mol','+|-',11.1947),
        S298 = (0.461492,'cal/mol/K','+|-',7.85372),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 20,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H ux {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.443224,-4.15984,-5.26054,-5.34243,-5.0155,-4.88039,-4.62057],'cal/mol/K','+|-',[4.30963,5.71963,5.23929,4.82743,3.79552,2.89249,2.85722]),
        H298 = (84.5385,'kcal/mol','+|-',5.0812),
        S298 = (-0.275205,'cal/mol/K','+|-',9.91818),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 21,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H ux {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,S}
8   R!H ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2172,-2.99277,-4.19143,-4.36502,-4.29437,-4.42155,-4.37258],'cal/mol/K','+|-',[2.90795,2.63895,2.40553,2.29412,2.2377,2.28207,2.98524]),
        H298 = (83.8017,'kcal/mol','+|-',4.33442),
        S298 = (-2.43641,'cal/mol/K','+|-',2.50445),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 22,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]} {8,S}
8   R!H ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.02078,-2.79524,-4.03265,-4.29094,-4.27418,-4.47349,-4.71332],'cal/mol/K','+|-',[3.3053,2.94556,2.691,2.63238,2.58221,2.62939,3.12212]),
        H298 = (83.6095,'kcal/mol','+|-',4.9384),
        S298 = (-2.15932,'cal/mol/K','+|-',2.5947),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 23,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C_6R!H->C_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,S}
6   C u0 {5,S} {7,[S,D,T,B,Q]}
7   C u0 {6,[S,D,T,B,Q]} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.42508,-2.386,-3.8157,-4.14297,-4.26444,-4.61697,-5.22003],'cal/mol/K','+|-',[3.16228,3.16228,3.16544,3.16228,3.16228,3.16228,3.16228]),
        H298 = (83.3107,'kcal/mol','+|-',5.9165),
        S298 = (-2.08528,'cal/mol/K','+|-',3.16228),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 24,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C_6R!H->C_8R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,S}
6   C   u0 {5,S} {7,[S,D,T,B,Q]}
7   C   u0 {6,[S,D,T,B,Q]} {8,S}
8   C   ux r0 {7,S}
9   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.42508,-2.386,-3.8657,-4.14297,-4.26444,-4.61697,-5.22003],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.1857,'kcal/mol','+|-',4.17612),
        S298 = (-2.08528,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1C=C(C)[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 25,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C_6R!H->C_N-8R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,D} {4,S}
3   C u0 r1 {2,D} {5,S}
4   C u0 r0 {2,S}
5   C u0 r1 {3,S} {6,[S,T,Q,B]}
6   C ux {5,[S,T,Q,B]} {7,S}
7   C ux {6,S} {8,S}
8   O u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21219,-3.6137,-4.46654,-4.58689,-4.29364,-4.18652,-3.69992],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.2073,'kcal/mol','+|-',4.17612),
        S298 = (-2.30742,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1[CH]C(C)=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 26,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,S}
6   O   u0 {5,S} {7,[S,D,T,B,Q]}
7   R!H u0 {6,[S,D,T,B,Q]} {8,S}
8   R!H ux r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.80645,-3.58537,-4.66777,-4.58725,-4.35496,-4.26574,-3.35036],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.3783,'kcal/mol','+|-',4.17612),
        S298 = (-3.26766,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1C=C(C)[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 27,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,D} {4,S}
3   C   u0 r1 {2,D} {5,S}
4   O   u0 r0 {2,S}
5   C   u0 r1 {3,S} {6,[S,T,Q,B]}
6   R!H ux {5,[S,T,Q,B]} {7,S}
7   R!H ux {6,S} {8,[S,D,T,B,Q]}
8   R!H u0 {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.65268,-8.82813,-9.53701,-9.2521,-7.90001,-6.71573,-5.61254],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.4855,'kcal/mol','+|-',4.17612),
        S298 = (8.36961,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CCOC=C[CH]1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 28,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
5   C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux r1 {5,[S,T,Q,B]}
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
    index = 29,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
5   O ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux r1 {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.843316,-3.15124,-4.5043,-4.98811,-5.39811,-6.07341,-7.04657],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (77.2321,'kcal/mol','+|-',4.17612),
        S298 = (3.14748,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1C(=O)OC=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 30,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.240727,-1.04896,-1.96748,-2.47532,-3.08877,-3.58917,-4.46661],'cal/mol/K','+|-',[3.04101,3.08802,3.08297,2.80018,2.36432,2.23976,1.8904]),
        H298 = (83.3982,'kcal/mol','+|-',26.1657),
        S298 = (-0.396668,'cal/mol/K','+|-',7.47184),
    ),
    shortDesc = """Radical correction fitted to 163 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 31,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.299253,-1.06221,-2.01395,-2.5178,-3.10835,-3.5962,-4.46469],'cal/mol/K','+|-',[3.14351,3.21755,3.19645,2.90308,2.46109,2.3348,1.9713]),
        H298 = (79.4587,'kcal/mol','+|-',14.0895),
        S298 = (-0.489289,'cal/mol/K','+|-',7.74422),
    ),
    shortDesc = """Radical correction fitted to 155 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 32,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
4   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.291737,-0.72689,-1.60876,-2.21386,-2.92773,-3.50788,-4.53567],'cal/mol/K','+|-',[3.20138,3.72424,3.72788,3.57719,3.03985,2.66093,2.67023]),
        H298 = (75.6955,'kcal/mol','+|-',17.8127),
        S298 = (0.665994,'cal/mol/K','+|-',6.81406),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 33,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux {1,S}
5   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.408597,-0.611834,-1.5166,-2.10702,-2.78952,-3.35152,-4.39787],'cal/mol/K','+|-',[2.86218,3.31659,3.37508,3.36513,2.89751,2.44417,2.53029]),
        H298 = (76.3908,'kcal/mol','+|-',14.6477),
        S298 = (0.549243,'cal/mol/K','+|-',6.85856),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 34,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   O   u0 {1,S}
5   R!H ux r1 {3,S}
6   R!H ux {3,[S,D,T,B,Q]}
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
    index = 35,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r1 {1,S}
5   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.437022,-0.826211,-1.83382,-2.50306,-3.17873,-3.79996,-5.05071],'cal/mol/K','+|-',[2.68138,4.28737,4.45595,4.30436,3.50098,2.70362,2.49955]),
        H298 = (81.3904,'kcal/mol','+|-',8.76821),
        S298 = (1.69893,'cal/mol/K','+|-',7.30757),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 36,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r1 {1,S}
5   C ux {3,S}
6   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.181195,-0.0523805,-1.43856,-2.15931,-2.70373,-3.73788,-4.66184],'cal/mol/K','+|-',[3.7045,4.1204,4.1444,3.90225,3.68608,3.67949,3.29794]),
        H298 = (84.3563,'kcal/mol','+|-',5.90892),
        S298 = (-0.287936,'cal/mol/K','+|-',4.62656),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 37,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_Ext-1R-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r1 {1,S}
5   C   ux r1 {3,S}
6   O   u0 r0 {1,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.501018,-0.986302,-2.38567,-2.96767,-3.37335,-4.40296,-4.99283],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.2898,'kcal/mol','+|-',4.17612),
        S298 = (0.906061,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CO[C]1C=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 38,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   O u0 r1 {1,S}
5   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.374735,-1.09686,-1.65392,-2.12153,-2.73385,-3.35891,-4.54528],'cal/mol/K','+|-',[2.92479,5.72813,5.18,4.48669,3.35544,2.42559,1.78555]),
        H298 = (79.609,'kcal/mol','+|-',3.13005),
        S298 = (0.684426,'cal/mol/K','+|-',5.64992),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 39,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   O   u0 r1 {1,S} {6,[S,D,T,B,Q]}
5   C   u0 r1 {3,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.75714,-6.65719,-6.66543,-6.37222,-5.62915,-5.08672,-5.08307],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.6887,'kcal/mol','+|-',4.17612),
        S298 = (5.9612,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CCO[CH]C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 40,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   O u0 r1 {1,S}
5   C u0 {3,S} {6,[S,D,T,B,Q]}
6   O u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.13913,-0.205041,-0.849046,-1.44499,-2.26584,-3.10092,-4.40614],'cal/mol/K','+|-',[2.55104,2.83402,2.52279,2.50194,2.7041,2.52623,2.4195]),
        H298 = (80.015,'kcal/mol','+|-',4.82475),
        S298 = (-0.178479,'cal/mol/K','+|-',3.87582),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 41,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   O u0 r1 {1,S}
5   C u0 r1 {3,S} {6,S}
6   O u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.310784,0.563839,-0.441786,-1.07198,-1.62739,-2.68825,-4.21737],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.2358,'kcal/mol','+|-',4.17612),
        S298 = (-1.71939,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1C=C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 42,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   O u0 r1 {1,S}
5   C u0 r1 {3,S} {6,[B,D,T,Q]}
6   O u0 r0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.319095,-0.512593,-1.01195,-1.59419,-2.52122,-3.26599,-4.48164],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (79.6482,'kcal/mol','+|-',1.69706),
        S298 = (0.437887,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 43,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r1 {1,S}
5   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.609326,-0.763145,-2.20652,-3.11366,-3.91767,-4.38388,-5.8354],'cal/mol/K','+|-',[3.78603,4.24129,5.56923,5.80121,4.79905,3.89442,3.66956]),
        H298 = (83.5112,'kcal/mol','+|-',15.3502),
        S298 = (3.71262,'cal/mol/K','+|-',9.86463),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 44,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r1 {1,S}
5   O ux {3,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.94867,-1.37402,-3.51419,-4.60941,-5.22083,-5.39339,-6.97244],'cal/mol/K','+|-',[5.05662,5.3982,6.03036,5.86868,4.61258,3.90213,2.89237]),
        H298 = (89.0399,'kcal/mol','+|-',16.7852),
        S298 = (6.05608,'cal/mol/K','+|-',10.6305),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 45,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_Sp-7R!H-6R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r1 {1,S}
5   O ux {3,S} {6,S}
6   C u0 {5,S} {7,S}
7   C ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.14298,-2.7399,-5.06229,-6.07141,-6.10462,-5.93637,-7.22421],'cal/mol/K','+|-',[4.38232,3.18946,3.44652,3.77495,4.52468,4.47706,3.4463]),
        H298 = (93.1892,'kcal/mol','+|-',11.7754),
        S298 = (8.83283,'cal/mol/K','+|-',6.13469),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 46,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r1 {1,S} {8,[S,D,T,B,Q]}
5   O   ux r1 {3,S} {6,S}
6   C   u0 r1 {5,S} {7,S}
7   C   ux {6,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.929675,-2.88681,-5.54686,-6.80031,-7.24877,-7.05686,-7.70859],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.791,'kcal/mol','+|-',4.17612),
        S298 = (10.6914,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=COCC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 47,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   O u0 r1 {1,S}
5   O u0 r1 {3,S} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]} {7,[B,D,T,Q]}
7   C u0 {6,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.13197,1.35774,-0.417992,-1.68539,-3.45327,-4.30743,-6.46891],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.7413,'kcal/mol','+|-',4.17612),
        S298 = (0.502589,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=COC=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 48,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r0 {1,S}
5   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.242854,-0.518091,-1.2914,-1.79765,-2.50028,-2.98945,-3.76019],'cal/mol/K','+|-',[3.43824,2.28541,2.06052,2.24983,2.26095,2.1467,2.24894]),
        H298 = (72.7112,'kcal/mol','+|-',10.1272),
        S298 = (-0.339623,'cal/mol/K','+|-',5.79287),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 49,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r0 {1,S}
5   C ux {3,S} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.905439,-0.32657,-1.40288,-2.02063,-2.7273,-3.19144,-3.8217],'cal/mol/K','+|-',[3.61769,2.54675,2.37984,2.54281,2.47291,2.14924,2.73019]),
        H298 = (75.5252,'kcal/mol','+|-',11.9599),
        S298 = (0.221601,'cal/mol/K','+|-',6.81218),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 50,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r0 {1,S}
5   C   ux {3,S} {6,S}
6   C   ux {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.02014,-0.231029,-1.30005,-1.85976,-2.54063,-3.07218,-3.59369],'cal/mol/K','+|-',[4.80667,3.31342,3.0711,3.25962,3.1317,2.72624,3.45798]),
        H298 = (71.8209,'kcal/mol','+|-',8.01783),
        S298 = (-0.769738,'cal/mol/K','+|-',8.14601),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 51,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Sp-7R!H-6R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r0 {1,S}
5   C   ux r1 {3,S} {6,S}
6   C   u0 r1 {5,S} {7,S}
7   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22246,-0.362924,-2.50842,-3.37968,-3.88293,-3.95073,-3.8516],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (78.0507,'kcal/mol','+|-',4.17612),
        S298 = (-2.8522,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(O[C]1CCCC=C1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 52,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   O   u0 r0 {1,S}
5   C   u0 {3,S} {6,S}
6   C   ux {5,S} {7,[B,D,T,Q]}
7   R!H ux {6,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.676614,-0.193344,-0.954805,-1.4255,-2.15711,-2.82117,-3.52],'cal/mol/K','+|-',[5.94487,4.22481,3.12525,2.98915,3.03957,2.91773,4.41582]),
        H298 = (70.938,'kcal/mol','+|-',3.48089),
        S298 = (-0.17475,'cal/mol/K','+|-',10.2798),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 53,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   O   u0 r0 {1,S} {8,[S,D,T,B,Q]}
5   C   u0 r1 {3,S} {6,S}
6   C   ux r1 {5,S} {7,[B,D,T,Q]}
7   R!H ux {6,[B,D,T,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.423055,-0.897117,-1.36153,-1.78808,-2.53641,-3.15916,-4.2701],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (71.0876,'kcal/mol','+|-',1.69706),
        S298 = (1.84514,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(O[C]1C=CCC=C1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 54,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r0 {1,S}
5   C ux {3,S} {6,[B,D,T,Q]}
6   C ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.530161,-0.741532,-1.16135,-1.53752,-2.23542,-2.75381,-3.68842],'cal/mol/K','+|-',[3.53932,2.93729,2.69703,2.82427,2.92454,3.03915,2.72203]),
        H298 = (69.6826,'kcal/mol','+|-',3.12247),
        S298 = (-0.994384,'cal/mol/K','+|-',5.7975),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 55,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   O   u0 r0 {1,S} {7,[S,D,T,B,Q]}
5   C   u0 r1 {3,S} {6,[B,D,T,Q]}
6   C   ux r1 {5,[B,D,T,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.378745,-0.0657631,-0.643626,-1.26552,-2.39298,-3.16918,-4.21182],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (69.0231,'kcal/mol','+|-',1.69706),
        S298 = (-0.901534,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(O[C]1CC=CC=C1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 56,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r0 {1,S}
5   C   ux r1 {3,S} {6,[B,D,T,Q]}
6   C   ux r1 {5,[B,D,T,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.725194,0.241172,-0.182714,-0.0339279,-0.273752,-0.606491,-1.93946],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (71.9431,'kcal/mol','+|-',4.17612),
        S298 = (-5.56058,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1C=CC=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 57,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_N-Sp-5R!H-3R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,[B,D,T,Q]}
4   O u0 {1,S}
5   C ux {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.37352,-2.36644,-2.92204,-3.73633,-4.89729,-5.73609,-6.49921],'cal/mol/K','+|-',[7.86852,9.5772,9.50496,7.45123,4.26184,3.37138,3.30115]),
        H298 = (57.1346,'kcal/mol','+|-',53.1559),
        S298 = (2.32971,'cal/mol/K','+|-',8.10375),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 58,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[B,D,T,Q]}
4   O   u0 r1 {1,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {3,[B,D,T,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17387,0.829705,0.247029,-1.35094,-3.88713,-5.32283,-6.83417],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (75.8117,'kcal/mol','+|-',4.17612),
        S298 = (-0.308255,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=C=C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 59,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.300516,-1.11856,-2.08203,-2.56888,-3.1387,-3.61104,-4.45277],'cal/mol/K','+|-',[3.16669,3.1485,3.116,2.80163,2.38539,2.31202,1.87331]),
        H298 = (80.1732,'kcal/mol','+|-',12.9679),
        S298 = (-0.683428,'cal/mol/K','+|-',7.8604),
    ),
    shortDesc = """Radical correction fitted to 135 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 60,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.304968,-1.11349,-2.07811,-2.56643,-3.138,-3.60825,-4.45022],'cal/mol/K','+|-',[3.17327,3.15433,3.12293,2.80869,2.39199,2.31726,1.87729]),
        H298 = (80.1418,'kcal/mol','+|-',12.9455),
        S298 = (-0.718524,'cal/mol/K','+|-',7.82496),
    ),
    shortDesc = """Radical correction fitted to 134 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 61,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R",
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
        Cpdata = ([0.306282,-1.1223,-2.09174,-2.57891,-3.14709,-3.61448,-4.45286],'cal/mol/K','+|-',[3.18201,3.15425,3.11004,2.79638,2.38615,2.31769,1.88123]),
        H298 = (80.1288,'kcal/mol','+|-',12.9608),
        S298 = (-0.704786,'cal/mol/K','+|-',7.83824),
    ),
    shortDesc = """Radical correction fitted to 133 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 62,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C",
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
        Cpdata = ([0.503816,-0.685234,-1.69752,-2.24238,-2.84895,-3.36827,-4.27793],'cal/mol/K','+|-',[3.09514,2.57165,2.5902,2.34584,1.98216,1.98135,1.71642]),
        H298 = (81.9498,'kcal/mol','+|-',6.90355),
        S298 = (-0.399124,'cal/mol/K','+|-',7.48327),
    ),
    shortDesc = """Radical correction fitted to 58 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 63,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C",
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
        Cpdata = ([0.601384,-0.648711,-1.69444,-2.2435,-2.85339,-3.38149,-4.18311],'cal/mol/K','+|-',[3.19133,2.64416,2.67062,2.41901,2.05971,2.0772,1.65742]),
        H298 = (82.1305,'kcal/mol','+|-',6.54825),
        S298 = (-0.777729,'cal/mol/K','+|-',6.90968),
    ),
    shortDesc = """Radical correction fitted to 52 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 64,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.713579,-0.598578,-1.68747,-2.24308,-2.85108,-3.38284,-4.16867],'cal/mol/K','+|-',[3.10032,2.58821,2.67926,2.44853,2.12318,2.16431,1.72011]),
        H298 = (82.1742,'kcal/mol','+|-',6.11743),
        S298 = (-1.26297,'cal/mol/K','+|-',6.07745),
    ),
    shortDesc = """Radical correction fitted to 49 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 65,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S}
5   C   ux {3,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.929456,-0.482177,-1.66961,-2.22374,-2.84124,-3.41732,-4.17813],'cal/mol/K','+|-',[3.36545,3.06024,3.17454,2.93214,2.64151,2.60085,2.06104]),
        H298 = (82.28,'kcal/mol','+|-',6.0198),
        S298 = (-1.64165,'cal/mol/K','+|-',6.27061),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 66,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S}
5   C   ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.956768,-0.699341,-2.01634,-2.49261,-2.93254,-3.40025,-4.03455],'cal/mol/K','+|-',[3.34136,2.76133,2.72538,2.27127,1.93719,2.22589,1.56536]),
        H298 = (83.6675,'kcal/mol','+|-',2.80116),
        S298 = (-1.87506,'cal/mol/K','+|-',6.48594),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 67,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.626589,-0.648097,-1.81494,-2.30676,-2.58339,-2.8281,-3.89626],'cal/mol/K','+|-',[3.47581,2.17969,1.88787,1.72122,1.51286,1.64128,1.74781]),
        H298 = (83.1233,'kcal/mol','+|-',2.86501),
        S298 = (-1.32091,'cal/mol/K','+|-',5.53999),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 68,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C   u0 {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.55473,-0.701554,-2.33634,-2.39707,-1.42521,-1.18482,-2.53199],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.3851,'kcal/mol','+|-',4.17612),
        S298 = (-7.71049,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 69,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C   ux {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0242276,-0.216524,-0.737919,-1.36653,-2.35646,-3.14297,-4.41368],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (83.5628,'kcal/mol','+|-',1.69706),
        S298 = (0.990043,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 70,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_Sp-7R!H=6C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {3,S} {4,S} {6,S}
6   C u0 {5,S} {7,D}
7   C u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.417322,-1.25001,-2.39414,-2.99481,-3.05657,-2.99449,-3.9528],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.9997,'kcal/mol','+|-',4.17612),
        S298 = (0.504903,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(C2=CC=CCC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 71,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux {5,S} {7,[S,T,Q,B]}
7   C ux {6,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.817374,-0.697928,-2.00222,-2.49173,-2.73072,-2.90925,-3.89793],'cal/mol/K','+|-',[4.19749,2.65877,1.86399,1.72264,1.58197,1.58257,1.83604]),
        H298 = (83.1399,'kcal/mol','+|-',3.26318),
        S298 = (-1.46369,'cal/mol/K','+|-',4.10393),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 72,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S}
5   C   ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C   ux {5,S} {7,[S,T,Q,B]}
7   C   ux {6,[S,T,Q,B]} {8,S}
8   R!H ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.468553,-0.916075,-2.0492,-2.45383,-2.73514,-2.95137,-3.75999],'cal/mol/K','+|-',[4.64673,2.95104,2.09094,1.95178,1.80257,1.77489,2.00457]),
        H298 = (83.3038,'kcal/mol','+|-',3.50105),
        S298 = (-0.958342,'cal/mol/K','+|-',3.98847),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 73,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux r1 {5,S} {7,[S,T,Q,B]}
7   C ux {6,[S,T,Q,B]} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.99243,-0.210673,-2.06335,-2.65344,-2.88906,-2.89226,-3.61202],'cal/mol/K','+|-',[2.97257,2.62485,2.74301,2.70562,2.60001,2.5993,2.90112]),
        H298 = (82.5908,'kcal/mol','+|-',5.80557),
        S298 = (-1.71133,'cal/mol/K','+|-',4.95092),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 74,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux r1 {5,S} {7,[S,T,Q,B]}
7   C ux {6,[S,T,Q,B]} {8,S}
8   C ux {7,S} {9,S}
9   C u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.28075,-0.229783,-2.15626,-2.69313,-2.80898,-2.84578,-3.34238],'cal/mol/K','+|-',[3.51339,3.23073,3.39231,3.35703,3.16747,3.18237,3.42852]),
        H298 = (81.86,'kcal/mol','+|-',6.55481),
        S298 = (-2.10331,'cal/mol/K','+|-',6.48092),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 75,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_Ext-6C-R",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   ux r1 {1,S} {3,D}
3    C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C   ux r1 {1,S} {5,S}
5    C   ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6    C   ux r1 {5,S} {7,[S,T,Q,B]} {11,[S,D,T,B,Q]}
7    C   ux r1 {6,[S,T,Q,B]} {8,S}
8    C   ux r1 {7,S} {9,S}
9    C   u0 r1 {8,S} {10,D}
10   C   u0 r1 {9,D}
11   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.82204,-0.463668,-2.59039,-3.09151,-2.87308,-2.97203,-2.87403],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.8547,'kcal/mol','+|-',4.17612),
        S298 = (-4.10339,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1(C2C=C[CH]C2)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 76,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux r1 {5,S} {7,[S,T,Q,B]}
7   C ux r1 {6,[S,T,Q,B]} {8,S}
8   C ux r1 {7,S} {9,[B,D,T,Q]}
9   C u0 r1 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4158,-0.172453,-1.87754,-2.57408,-3.04922,-2.98521,-4.1513],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.0524,'kcal/mol','+|-',4.17612),
        S298 = (-0.927364,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(C2C=CC=CC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 77,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S}
5   C   ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C   ux r0 {5,S} {7,[S,T,Q,B]}
7   C   ux {6,[S,T,Q,B]} {8,S}
8   R!H ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.837631,-1.5207,-2.03707,-2.28273,-2.6032,-3.00204,-3.88683],'cal/mol/K','+|-',[5.50059,4.12883,2.99564,2.5888,2.40995,2.4056,2.48335]),
        H298 = (83.607,'kcal/mol','+|-',3.35772),
        S298 = (-0.312925,'cal/mol/K','+|-',4.01296),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 78,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing_Ext-7R!H-R_Sp-9R!H-7R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C   ux r0 {5,S} {7,[S,T,Q,B]}
7   C   ux {6,[S,T,Q,B]} {8,S} {9,S}
8   R!H ux {7,S}
9   R!H ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.66452,0.179604,-1.12518,-1.78079,-2.7577,-3.13816,-4.22667],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.8923,'kcal/mol','+|-',4.17612),
        S298 = (-1.94093,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)CC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 79,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing_Ext-7R!H-R_N-Sp-9R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux r0 {5,S} {7,[S,T,Q,B]}
7   C ux {6,[S,T,Q,B]} {8,S} {9,[B,D,T,Q]}
8   C ux {7,S}
9   C u0 r0 {7,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83849,-2.20083,-2.40182,-2.4835,-2.54141,-2.94759,-3.7509],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (83.725,'kcal/mol','+|-',1.69706),
        S298 = (0.338277,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 80,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_N-Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S}
5   C u0 {3,S} {4,S} {6,S}
6   C u0 {5,S} {7,S}
7   C u0 {6,S} {8,[B,D,T,Q]}
8   C u0 {7,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.95104,0.0110489,-1.84955,-2.61489,-2.71635,-2.77236,-4.34622],'cal/mol/K','+|-',[3.62814,3.21032,3.36109,3.25161,3.19469,3.24236,3.2326]),
        H298 = (82.3159,'kcal/mol','+|-',6.14756),
        S298 = (-3.10606,'cal/mol/K','+|-',4.57059),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 81,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_N-Sp-8R!H-7R!H_Ext-8R!H-R_Ext-8R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   u0 r1 {1,S} {3,D}
3    C   u0 r1 {2,D} {5,S}
4    C   u0 r1 {1,S} {5,S}
5    C   u0 r1 {3,S} {4,S} {6,S}
6    C   u0 r1 {5,S} {7,S}
7    C   u0 r1 {6,S} {8,D}
8    C   u0 r1 {7,D} {9,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
9    R!H ux {8,[S,D,T,B,Q]}
10   R!H ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.57987,-0.184585,-2.25219,-2.88251,-2.55586,-2.51915,-4.10912],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.7125,'kcal/mol','+|-',4.17612),
        S298 = (-4.27281,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=CC(C2C=C[CH]C2)C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 82,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   O ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.40859,-0.769465,-2.29194,-2.74692,-3.41033,-4.18319,-4.2238],'cal/mol/K','+|-',[3.49487,3.87172,3.9466,3.26128,2.57203,2.45699,1.92955]),
        H298 = (84.5058,'kcal/mol','+|-',2.9421),
        S298 = (-2.63338,'cal/mol/K','+|-',7.93992),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 83,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6   O   u0 r0 {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.72188,2.77977,0.874412,-0.271459,-1.83855,-3.15562,-3.21502],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.5594,'kcal/mol','+|-',4.17612),
        S298 = (-1.83243,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]C=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 84,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S}
5   C   ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   O   ux {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C   ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.05384,-1.17417,-2.6732,-3.03715,-3.57583,-4.25849,-4.26266],'cal/mol/K','+|-',[2.84441,3.26797,3.65924,3.10236,2.62726,2.66507,1.95531]),
        H298 = (84.6764,'kcal/mol','+|-',2.90971),
        S298 = (-3.3228,'cal/mol/K','+|-',8.33377),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 85,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux {1,S} {5,S}
5    C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O ux {5,S} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]}
10   C ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.982618,-1.97041,-3.71675,-3.75339,-4.07813,-4.81134,-3.78708],'cal/mol/K','+|-',[4.20088,4.89982,4.72114,3.903,2.87451,2.79529,2.58981]),
        H298 = (85.0347,'kcal/mol','+|-',5.43357),
        S298 = (-6.96885,'cal/mol/K','+|-',4.81062),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 86,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S}
5    C u0 r1 {3,S} {4,S} {6,S}
6    O u0 r0 {5,S} {7,S}
7    O u0 r0 {6,S} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,S} {10,[S,D,T,B,Q]}
9    C u0 {8,S}
10   C ux {8,[S,D,T,B,Q]} {11,S}
11   C u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00488226,-3.42224,-5.2531,-4.93157,-4.65613,-5.29592,-3.89702],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.2103,'kcal/mol','+|-',4.17612),
        S298 = (-4.66184,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(OOC2C=CCCC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 87,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux {1,S} {5,S}
5    C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O ux {5,S} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.47149,-1.24449,-2.94857,-3.16431,-3.78913,-4.56905,-3.7321],'cal/mol/K','+|-',[5.12111,5.66006,5.20409,4.33646,3.34481,3.29925,3.16361]),
        H298 = (85.4469,'kcal/mol','+|-',6.58355),
        S298 = (-8.12235,'cal/mol/K','+|-',3.31919),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 88,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,S}
5    C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O ux {5,S} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,S}
8    C u0 r1 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0473314,-2.90417,-4.40984,-4.21341,-4.17444,-4.90167,-3.69968],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.4754,'kcal/mol','+|-',4.17612),
        S298 = (-7.76581,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(OOC2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 89,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_N-8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,S}
5    C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O ux {5,S} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,S}
8    C u0 r0 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.89564,0.415191,-1.48729,-2.11521,-3.40382,-4.23644,-3.76453],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.4183,'kcal/mol','+|-',4.17612),
        S298 = (-8.4789,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)OOC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 90,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_7R!H->N",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6   O ux {5,S} {7,[S,D,T,B,Q]}
7   N ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux r0 {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.419265,-0.475702,-1.27086,-1.76223,-2.36723,-2.99188,-4.2853],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (84.647,'kcal/mol','+|-',1.69706),
        S298 = (1.23323,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1C[CH]C=C1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 91,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_N-7R!H->N",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S}
5   C u0 {3,S} {4,S} {6,S}
6   O u0 {5,S} {7,S}
7   O u0 {6,S} {8,S}
8   C u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.95391,-0.852909,-2.86081,-3.55643,-4.33313,-5.01247,-4.94774],'cal/mol/K','+|-',[3.16443,3.17528,3.17498,3.16966,3.16229,3.17223,3.22251]),
        H298 = (84.2277,'kcal/mol','+|-',5.90594),
        S298 = (-3.54875,'cal/mol/K','+|-',3.20206),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 92,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_N-7R!H->N_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S}
5    C u0 r1 {3,S} {4,S} {6,S}
6    O u0 r0 {5,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,D}
10   C u0 r0 {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.99521,-0.751437,-2.76052,-3.47999,-4.33049,-4.9237,-4.72848],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.2312,'kcal/mol','+|-',4.17612),
        S298 = (-3.72665,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 93,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_N-7R!H->N_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S}
5    C u0 r1 {3,S} {4,S} {6,S}
6    O u0 r0 {5,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,S}
10   C u0 r0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.91261,-0.95438,-2.96111,-3.63286,-4.33576,-5.10124,-5.167],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.2242,'kcal/mol','+|-',4.17612),
        S298 = (-3.37085,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 94,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S}
5   C   ux {3,[S,D,T,B,Q]} {4,S} {6,[B,D,T,Q]}
6   R!H ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.868005,0.00644266,-0.889476,-1.61878,-2.63581,-3.45574,-4.50116],'cal/mol/K','+|-',[3.99549,3.99719,4.06947,4.29968,4.27339,3.83259,3.30304]),
        H298 = (79.5905,'kcal/mol','+|-',7.69979),
        S298 = (-1.11647,'cal/mol/K','+|-',6.35038),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 95,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,[B,D,T,Q]}
6   C ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.441019,-0.788504,-1.82502,-2.70947,-3.78722,-4.50374,-5.20288],'cal/mol/K','+|-',[3.23575,3.40222,4.5712,5.43726,5.80327,5.2561,4.77286]),
        H298 = (77.1979,'kcal/mol','+|-',6.11722),
        S298 = (0.338953,'cal/mol/K','+|-',7.64034),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 96,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_6R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 r1 {3,[S,D,T,B,Q]} {4,S} {6,D}
6   C   u0 {5,D}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.16696,-0.300265,-2.0402,-2.98343,-3.89219,-4.87926,-4.18068],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (74.6909,'kcal/mol','+|-',4.17612),
        S298 = (4.94682,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 97,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_6R!H->C_6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,[B,D,T,Q]}
6   C ux r1 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.313517,-2.71032,-4.55487,-6.07978,-7.48692,-7.69942,-8.28272],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (73.8211,'kcal/mol','+|-',4.17612),
        S298 = (1.50877,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(=C2C=CCCC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 98,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_6R!H->C_N-6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,[B,D,T,Q]}
6   C ux r0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.198354,-0.215075,-0.64701,-1.25177,-2.26535,-3.07527,-4.37982],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (78.1695,'kcal/mol','+|-',1.69706),
        S298 = (-1.97212,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 99,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C u0 {1,S} {5,S}
5   C u0 {3,[S,D,T,B,Q]} {4,S} {6,D}
6   O u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.21736,0.656854,-0.124029,-0.726398,-1.69375,-2.59828,-3.92703],'cal/mol/K','+|-',[5.29503,4.8416,4.01319,3.39415,2.64445,2.33416,2.42115]),
        H298 = (81.719,'kcal/mol','+|-',7.81855),
        S298 = (-2.30726,'cal/mol/K','+|-',5.53433),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 100,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {3,[S,D,T,B,Q]} {4,S} {6,D}
6   O   u0 r0 {5,D}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.234443,-1.27439,-1.86586,-1.85536,-1.68146,-1.925,-2.78106],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (78.3671,'kcal/mol','+|-',4.17612),
        S298 = (-2.16953,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C[CH]C=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 101,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 {3,S} {4,S} {6,D}
6   O   u0 {5,D}
7   R!H u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.90777,3.07519,1.77154,0.811964,-0.753279,-2.17799,-3.88375],'cal/mol/K','+|-',[3.48282,3.22584,3.16376,3.16249,3.16309,3.16625,3.2862]),
        H298 = (79.1264,'kcal/mol','+|-',11.7384),
        S298 = (-5.00828,'cal/mol/K','+|-',3.20642),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 102,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H->C_Ext-4C-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C u0 r1 {3,S} {4,S} {6,D}
6   O u0 r0 {5,D}
7   C u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.39177,2.84991,1.80582,0.824928,-0.727889,-2.23408,-4.1998],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (75.5398,'kcal/mol','+|-',4.17612),
        S298 = (-4.82083,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 103,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H->C_Ext-4C-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,S}
4   C                      u0 r1 {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C                      u0 r1 {3,S} {4,S} {6,D}
6   O                      u0 r0 {5,D}
7   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.42377,3.30047,1.73726,0.799,-0.778669,-2.12191,-3.56769],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.713,'kcal/mol','+|-',4.17612),
        S298 = (-5.19574,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=C[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 104,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.706777,-0.662069,-1.75438,-2.30828,-2.84648,-3.3708,-4.22319],'cal/mol/K','+|-',[2.7769,2.35275,2.55038,2.28931,1.85893,2.04183,1.55468]),
        H298 = (81.8284,'kcal/mol','+|-',7.57497),
        S298 = (-1.12768,'cal/mol/K','+|-',6.81047),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 105,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {4,S}
6   R!H ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.982983,-0.681145,-1.93047,-2.48296,-2.92352,-3.39341,-4.1594],'cal/mol/K','+|-',[2.81715,2.61711,2.71975,2.41754,2.04206,2.27975,1.71239]),
        H298 = (83.7885,'kcal/mol','+|-',2.7166),
        S298 = (-1.20542,'cal/mol/K','+|-',7.60325),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 106,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C u0 {3,S} {4,S}
6   O u0 {4,[S,D,T,B,Q]} {7,S}
7   O ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.86286,-1.51174,-3.0439,-3.56942,-4.04559,-4.77161,-4.71586],'cal/mol/K','+|-',[2.981,3.39466,3.2715,2.65901,2.04031,1.97075,2.2443]),
        H298 = (84.5167,'kcal/mol','+|-',3.84371),
        S298 = (-3.41771,'cal/mol/K','+|-',7.55592),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 107,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C u0 {3,S} {4,S}
6   O u0 {4,[S,D,T,B,Q]} {7,S}
7   O ux {6,S} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.965398,-1.55174,-3.17315,-3.67424,-4.11881,-4.81258,-4.6009],'cal/mol/K','+|-',[3.25974,3.76695,3.56518,2.88819,2.20819,2.15355,2.39436]),
        H298 = (84.5409,'kcal/mol','+|-',4.22714),
        S298 = (-4.64056,'cal/mol/K','+|-',5.132),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 108,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   u0 {1,S} {3,D}
3    C   u0 r1 {2,D} {5,S}
4    C   u0 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C   u0 {3,S} {4,S}
6    O   u0 {4,[S,D,T,B,Q]} {7,S}
7    O   ux {6,S} {8,[S,D,T,B,Q]}
8    C   ux {7,[S,D,T,B,Q]} {9,S}
9    C   u0 {8,S} {10,S}
10   R!H ux {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.898496,-1.73769,-3.45702,-4.01444,-4.37947,-5.02774,-4.94706],'cal/mol/K','+|-',[3.42614,3.93825,3.78651,3.03503,2.60879,2.6087,2.88634]),
        H298 = (84.0509,'kcal/mol','+|-',4.82222),
        S298 = (-2.95953,'cal/mol/K','+|-',2.90607),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 109,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,[S,D,T,B,Q]} {7,S}
7    O ux r0 {6,S} {8,[S,D,T,B,Q]}
8    C ux r1 {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,S}
10   C ux {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.400854,-3.45057,-5.05188,-4.93121,-4.59481,-5.21671,-4.24658],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.0393,'kcal/mol','+|-',4.17612),
        S298 = (-3.70159,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 110,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   u0 {1,S} {3,D}
3    C   u0 r1 {2,D} {5,S}
4    C   u0 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C   u0 {3,S} {4,S}
6    O   u0 {4,[S,D,T,B,Q]} {7,S}
7    O   ux {6,S} {8,[S,D,T,B,Q]}
8    C   ux r0 {7,[S,D,T,B,Q]} {9,S}
9    C   u0 {8,S} {10,S}
10   R!H ux {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.54817,-0.881245,-2.65959,-3.55606,-4.27181,-4.93326,-5.2973],'cal/mol/K','+|-',[3.16443,3.17528,3.17498,3.16966,3.16229,3.17223,3.22251]),
        H298 = (84.0567,'kcal/mol','+|-',5.90594),
        S298 = (-2.5885,'cal/mol/K','+|-',3.20206),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 111,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing_Ext-9R!H-R_Sp-11R!H-9R!H",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   u0 r1 {1,S} {3,D}
3    C   u0 r1 {2,D} {5,S}
4    C   u0 r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C   u0 r1 {3,S} {4,S}
6    O   u0 r0 {4,[S,D,T,B,Q]} {7,S}
7    O   ux r0 {6,S} {8,[S,D,T,B,Q]}
8    C   ux r0 {7,[S,D,T,B,Q]} {9,S}
9    C   u0 {8,S} {10,S} {11,S}
10   R!H ux {9,S}
11   R!H ux {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.50687,-0.982717,-2.75988,-3.6325,-4.27445,-5.02202,-5.51656],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.0532,'kcal/mol','+|-',4.17612),
        S298 = (-2.4106,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 112,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing_Ext-9R!H-R_N-Sp-11R!H-9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,[S,D,T,B,Q]} {7,S}
7    O ux r0 {6,S} {8,[S,D,T,B,Q]}
8    C ux r0 {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,S} {11,[B,D,T,Q]}
10   C ux {9,S}
11   C u0 r0 {9,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.58947,-0.779774,-2.55929,-3.47963,-4.26917,-4.84449,-5.07804],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.0602,'kcal/mol','+|-',4.17612),
        S298 = (-2.76641,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 113,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C u0 {3,S} {4,S}
6    O u0 {4,[S,D,T,B,Q]} {7,S}
7    O ux {6,S} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,[B,D,T,Q]}
10   C ux {9,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.06575,-1.27283,-2.74734,-3.16394,-3.72781,-4.48984,-4.08167],'cal/mol/K','+|-',[5.12111,5.66006,5.20409,4.33646,3.34481,3.29925,3.16361]),
        H298 = (85.2759,'kcal/mol','+|-',6.58355),
        S298 = (-7.1621,'cal/mol/K','+|-',3.31919),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 114,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H_8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,[S,D,T,B,Q]} {7,S}
7    O ux r0 {6,S} {8,[S,D,T,B,Q]}
8    C ux r1 {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,[B,D,T,Q]}
10   C ux {9,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.358405,-2.93251,-4.20862,-4.21304,-4.11312,-4.82245,-4.04924],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.3044,'kcal/mol','+|-',4.17612),
        S298 = (-6.80556,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 115,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H_N-8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,[S,D,T,B,Q]} {7,S}
7    O ux r0 {6,S} {8,[S,D,T,B,Q]}
8    C ux r0 {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,[B,D,T,Q]}
10   C ux {9,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.4899,0.386854,-1.28607,-2.11484,-3.3425,-4.15722,-4.11409],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.2474,'kcal/mol','+|-',4.17612),
        S298 = (-7.51865,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)OOC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 116,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      ux {1,S} {3,D}
3   C                      ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C                      ux {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C                      ux {3,[S,D,T,B,Q]} {4,S}
6   R!H                    ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   [Cl,C,Si,S,N,P,F,I,Br] ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.03269,-0.33745,-1.46974,-2.03338,-2.45922,-2.82312,-3.92914],'cal/mol/K','+|-',[3.08641,2.25152,2.17751,2.00369,1.5664,1.54451,1.67284]),
        H298 = (83.6149,'kcal/mol','+|-',2.83867),
        S298 = (-0.289995,'cal/mol/K','+|-',7.20078),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 117,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_Ext-3R!H-R",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,S} {8,[S,D,T,B,Q]}
4   C                      u0 r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C                      u0 r1 {3,S} {4,S}
6   R!H                    u0 {4,[S,D,T,B,Q]} {7,S}
7   [Cl,C,Si,S,N,P,F,I,Br] ux {6,S}
8   R!H                    ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.07473,-1.17155,-2.47634,-2.56707,-1.41521,-1.22482,-2.39199],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.6951,'kcal/mol','+|-',4.17612),
        S298 = (-8.93049,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=C[CH]C(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 118,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,S}
6   C ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.828144,-0.52252,-1.65926,-2.23298,-2.68213,-2.98008,-3.96793],'cal/mol/K','+|-',[3.45067,2.23213,2.04057,1.9564,1.49739,1.40585,1.58834]),
        H298 = (83.2418,'kcal/mol','+|-',2.51407),
        S298 = (-0.0790781,'cal/mol/K','+|-',5.62323),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 119,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,S}
6   C ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,D}
8   C ux {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.706931,-0.599701,-1.67695,-2.21525,-2.61435,-2.94425,-3.9242],'cal/mol/K','+|-',[3.85222,2.45587,2.21818,2.1237,1.60868,1.54677,1.75536]),
        H298 = (83.25,'kcal/mol','+|-',2.70603),
        S298 = (0.254019,'cal/mol/K','+|-',6.14487),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 120,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,S}
6   C ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,D}
8   C ux {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.58587,-0.0714655,-1.45427,-2.12656,-2.58532,-2.88885,-3.94791],'cal/mol/K','+|-',[2.59934,1.8212,2.4621,2.50158,1.89556,1.80733,2.07769]),
        H298 = (82.9961,'kcal/mol','+|-',3.37947),
        S298 = (-0.380877,'cal/mol/K','+|-',6.86627),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 121,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing_Ext-8R!H-R_Ext-6C-R_Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C ux {3,[S,D,T,B,Q]} {4,S}
6    C ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C ux {6,[S,D,T,B,Q]} {8,D}
8    C ux {7,D} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,S}
10   C ux {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.61679,-0.0531042,-1.3955,-2.04519,-2.50097,-2.87133,-3.91093],'cal/mol/K','+|-',[2.88877,1.98318,2.71215,2.73677,2.00886,1.96703,2.2768]),
        H298 = (82.8518,'kcal/mol','+|-',3.44194),
        S298 = (-0.281516,'cal/mol/K','+|-',7.75163),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 122,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing_Ext-8R!H-R_Ext-6C-R_Sp-10R!H-9R!H_Ext-8R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   u0 r1 {1,S} {3,D}
3    C   u0 r1 {2,D} {5,S}
4    C   u0 r1 {1,S} {5,S} {6,S}
5    C   u0 r1 {3,S} {4,S}
6    C   u0 r1 {4,S} {7,S}
7    C   u0 r1 {6,S} {8,D}
8    C   ux r1 {7,D} {9,S} {11,[S,D,T,B,Q]}
9    C   u0 r1 {8,S} {10,S}
10   C   ux r1 {9,S}
11   R!H ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.57987,-0.184585,-2.15219,-2.88251,-2.55586,-2.51915,-4.10912],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.9625,'kcal/mol','+|-',4.17612),
        S298 = (-4.27281,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=CC(C2[CH]C=CC2)C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 123,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing_Ext-8R!H-R_Ext-6C-R_Sp-10R!H-9R!H_Ext-10R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   ux r1 {1,S} {3,D}
3    C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C   ux r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C   ux r1 {3,[S,D,T,B,Q]} {4,S}
6    C   ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C   ux r1 {6,[S,D,T,B,Q]} {8,D}
8    C   ux r1 {7,D} {9,[S,D,T,B,Q]}
9    C   ux r1 {8,[S,D,T,B,Q]} {10,S}
10   C   ux r1 {9,S} {11,[S,D,T,B,Q]}
11   R!H ux {10,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.700398,0.140831,-0.564209,-1.19191,-2.23261,-3.03264,-4.2865],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (83.2436,'kcal/mol','+|-',1.69706),
        S298 = (2.77244,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 124,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing_Ext-8R!H-R_Ext-6C-R_Sp-10R!H-9R!H_Ext-6C-R",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   ux r1 {1,S} {3,D}
3    C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C   ux r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C   ux r1 {3,[S,D,T,B,Q]} {4,S}
6    C   ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {11,[S,D,T,B,Q]}
7    C   ux r1 {6,[S,D,T,B,Q]} {8,D}
8    C   ux r1 {7,D} {9,[S,D,T,B,Q]}
9    C   ux r1 {8,[S,D,T,B,Q]} {10,S}
10   C   ux r1 {9,S}
11   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.82204,-0.463668,-2.49039,-3.09151,-2.87308,-2.97203,-2.87403],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.1047,'kcal/mol','+|-',4.17612),
        S298 = (-4.10339,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1(C2[CH]C=CC2)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 125,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing_Ext-8R!H-R_Ext-6C-R_N-Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5    C ux r1 {3,[S,D,T,B,Q]} {4,S}
6    C ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C ux r1 {6,[S,D,T,B,Q]} {8,D}
8    C u0 r1 {7,D} {9,[S,D,T,B,Q]}
9    C ux r1 {8,[S,D,T,B,Q]} {10,[B,D,T,Q]}
10   C u0 r1 {9,[B,D,T,Q]}
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
    index = 126,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_N-6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {6,S}
5   C u0 r1 {3,S} {4,S}
6   C u0 r0 {4,S} {7,S}
7   C u0 {6,S} {8,D}
8   C ux {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57831,-1.97311,-2.2559,-2.44583,-2.68984,-3.0883,-3.86255],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (83.6716,'kcal/mol','+|-',1.69706),
        S298 = (1.90475,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 127,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_N-Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S} {6,S}
5   C u0 {3,S} {4,S}
6   C u0 {4,S} {7,S}
7   C u0 {6,S} {8,[S,T,Q,B]}
8   C ux {7,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3736,-0.175204,-1.57966,-2.3128,-2.98713,-3.14132,-4.16474],'cal/mol/K','+|-',[3.26758,3.3177,3.52981,3.50204,3.22818,3.16229,3.16713]),
        H298 = (83.176,'kcal/mol','+|-',5.9067),
        S298 = (-1.57801,'cal/mol/K','+|-',3.32471),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 128,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_N-Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {6,S}
5   C u0 r1 {3,S} {4,S}
6   C u0 r1 {4,S} {7,S}
7   C u0 {6,S} {8,[S,T,Q,B]}
8   C ux {7,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.08268,-0.530012,-2.13414,-2.84481,-3.21657,-3.14449,-4.1028],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.2097,'kcal/mol','+|-',4.17612),
        S298 = (-1.2151,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1C1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 129,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_N-Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_N-6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {6,S}
5   C u0 r1 {3,S} {4,S}
6   C u0 r0 {4,S} {7,S}
7   C u0 {6,S} {8,[S,T,Q,B]}
8   C ux {7,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.66452,0.179604,-1.02518,-1.78079,-2.7577,-3.13816,-4.22667],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.1423,'kcal/mol','+|-',4.17612),
        S298 = (-1.94093,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)CC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 130,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      ux r1 {1,S} {3,D}
3   C                      ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C                      ux r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C                      ux r1 {3,[S,D,T,B,Q]} {4,S}
6   O                      ux {4,[S,D,T,B,Q]} {7,S}
7   [Cl,C,Si,S,N,P,F,I,Br] ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.91587,0.810499,-0.233194,-0.94166,-1.89599,-2.7718,-4.37334],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (85.0478,'kcal/mol','+|-',1.69706),
        S298 = (2.23817,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1CC=C[CH]1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 131,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S} {6,D}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S}
6   C ux r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.226052,-0.315242,-0.779879,-1.38242,-2.37842,-3.17371,-4.45408],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (74.2586,'kcal/mol','+|-',1.69706),
        S298 = (-1.25774,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 132,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S} {6,D}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S}
6   O ux r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.625286,-0.852469,-1.28494,-1.80185,-2.68283,-3.38253,-4.51533],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (79.31,'kcal/mol','+|-',1.69706),
        S298 = (-0.360111,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 133,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {6,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S}
5   C u0 {3,S} {4,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.19002,-1.52313,-1.94186,-2.41486,-3.29357,-3.6755,-4.09626],'cal/mol/K','+|-',[4.56519,2.82332,2.45754,2.6515,2.57728,2.5181,2.84913]),
        H298 = (81.8877,'kcal/mol','+|-',3.27348),
        S298 = (0.748109,'cal/mol/K','+|-',3.50831),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 134,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-1R-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {3,S} {4,S}
6   C   u0 r0 {1,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97578,-1.82663,-1.82665,-2.18309,-3.09893,-3.51559,-3.78306],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (81.9789,'kcal/mol','+|-',1.69706),
        S298 = (0.22932,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 135,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S}
5   C   ux {3,[S,D,T,B,Q]} {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16208,-0.560157,-1.81513,-2.46033,-2.9248,-3.01157,-3.5304],'cal/mol/K','+|-',[4.54971,3.81676,3.38914,3.24373,3.24928,3.5003,3.66947]),
        H298 = (82.6372,'kcal/mol','+|-',5.00148),
        S298 = (-0.667932,'cal/mol/K','+|-',4.20998),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 136,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S}
5   C   ux {3,[S,D,T,B,Q]} {4,S}
6   R!H ux {3,[S,D,T,B,Q]} {7,S}
7   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.80594,-0.193056,-1.52774,-2.16334,-2.54213,-2.51971,-2.94597],'cal/mol/K','+|-',[5.30257,4.75054,4.20202,3.94884,3.77728,3.91979,3.92419]),
        H298 = (82.5231,'kcal/mol','+|-',6.17177),
        S298 = (-1.61444,'cal/mol/K','+|-',3.25785),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 137,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_Ext-6R!H-R_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {4,S}
6   C   ux {3,[S,D,T,B,Q]} {7,S}
7   R!H u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.301057,-1.44643,-2.50607,-2.99951,-3.27252,-3.33861,-3.76749],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.1567,'kcal/mol','+|-',4.17612),
        S298 = (-1.33749,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 138,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_Ext-6R!H-R_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {4,S}
6   O   ux {3,[S,D,T,B,Q]} {7,S}
7   R!H u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.31082,1.06032,-0.549418,-1.32718,-1.81173,-1.70082,-2.12444],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.8896,'kcal/mol','+|-',4.17612),
        S298 = (-1.89138,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=C[CH]CC1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 139,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C u0 {1,S} {5,D}
5   C u0 {3,[S,D,T,B,Q]} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.651461,-1.20853,-1.7723,-2.2482,-2.87917,-3.36637,-4.34432],'cal/mol/K','+|-',[4.30368,4.1639,3.71471,3.17975,2.3302,1.9331,1.95365]),
        H298 = (81.7658,'kcal/mol','+|-',12.4985),
        S298 = (4.64081,'cal/mol/K','+|-',7.91611),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 140,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C_Ext-3R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,[S,D,T,B,Q]} {6,S}
4   C u0 {1,S} {5,D}
5   C u0 {3,[S,D,T,B,Q]} {4,D}
6   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.94467,-2.29199,-2.63385,-2.93573,-3.27134,-3.52983,-4.2974],'cal/mol/K','+|-',[2.49974,3.85578,3.96593,3.51955,2.75684,2.47893,2.63276]),
        H298 = (80.4894,'kcal/mol','+|-',24.6173),
        S298 = (2.35911,'cal/mol/K','+|-',6.24586),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 141,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C_Ext-3R!H-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]} {6,S}
4   C   u0 r1 {1,S} {5,D}
5   C   u0 r1 {3,[S,D,T,B,Q]} {4,D} {7,[S,D,T,B,Q]}
6   O   u0 r0 {3,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.3139,-3.82002,-4.23219,-4.24045,-3.96495,-3.86134,-4.85462],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.307,'kcal/mol','+|-',4.17612),
        S298 = (5.27356,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=C[CH]C=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 142,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   O ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.287565,-0.981477,-1.72251,-2.23329,-2.81291,-3.26108,-5.04702],'cal/mol/K','+|-',[2.16365,2.50048,2.53327,2.37666,2.00443,1.79009,2.1336]),
        H298 = (80.5727,'kcal/mol','+|-',10.4785),
        S298 = (2.67178,'cal/mol/K','+|-',10.0669),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 143,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,S} {6,S}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   O ux {3,S} {4,[S,D,T,B,Q]}
6   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09987,-2.36885,-3.0843,-3.43779,-3.57603,-3.4295,-6.05861],'cal/mol/K','+|-',[3.51624,3.99755,4.14659,3.96252,3.69829,3.61715,3.23441]),
        H298 = (84.2778,'kcal/mol','+|-',5.93873),
        S298 = (9.96946,'cal/mol/K','+|-',4.7969),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 144,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-3R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,S} {6,S}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   O   ux r1 {3,S} {4,[S,D,T,B,Q]}
6   O   u0 r0 {3,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
    index = 145,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   O   ux r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.852467,-0.487298,-1.73659,-2.44364,-3.19425,-3.7724,-5.31954],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (73.6042,'kcal/mol','+|-',4.17612),
        S298 = (-1.60629,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]1C=COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 146,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S} {6,[S,D,T,B,Q]}
5   O u0 {3,S} {4,S}
6   O u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.432006,-0.885726,-1.54782,-2.04998,-2.67937,-3.21623,-4.83891],'cal/mol/K','+|-',[2.78561,2.44022,2.44465,2.43992,2.44572,2.65281,2.82243]),
        H298 = (79.3689,'kcal/mol','+|-',21.8795),
        S298 = (1.84028,'cal/mol/K','+|-',8.72685),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 147,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R_Sp-6R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {6,S}
5   O u0 r1 {3,S} {4,S}
6   O u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.290329,-0.638098,-1.80637,-2.29687,-2.41825,-2.63526,-5.59684],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (92.5094,'kcal/mol','+|-',4.17612),
        S298 = (6.07942,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 148,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R_N-Sp-6R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {6,[B,D,T,Q]}
5   O u0 r1 {3,S} {4,S}
6   O u0 r0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.72094,-0.984778,-1.4444,-1.95123,-2.78382,-3.44862,-4.53574],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (77.1989,'kcal/mol','+|-',1.69706),
        S298 = (0.14462,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 149,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
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
        Cpdata = ([-0.140286,-1.71076,-2.30376,-2.6628,-3.16556,-3.5722,-4.47849],'cal/mol/K','+|-',[3.31799,3.78944,3.62744,3.25006,2.47541,1.99421,1.59211]),
        H298 = (73.3263,'kcal/mol','+|-',10.0004),
        S298 = (1.36939,'cal/mol/K','+|-',4.86052),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 150,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {7,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   C   ux {5,D}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.170058,-2.40091,-3.06267,-3.37392,-3.7278,-3.9841,-4.72457],'cal/mol/K','+|-',[4.33639,4.94043,4.65974,4.12424,3.00859,2.31406,1.68799]),
        H298 = (72.0195,'kcal/mol','+|-',16.0646),
        S298 = (1.55403,'cal/mol/K','+|-',6.08119),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 151,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {7,S}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   C   ux {5,D}
7   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.61908,-2.33142,-3.13729,-3.44391,-3.7323,-3.92763,-4.71057],'cal/mol/K','+|-',[4.31702,5.68144,5.32818,4.79626,3.6322,2.86085,2.127]),
        H298 = (75.6098,'kcal/mol','+|-',8.5322),
        S298 = (1.72802,'cal/mol/K','+|-',7.29313),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 152,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Int-6R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux {1,S} {6,[S,D,T,B,Q]} {7,S}
5   C   ux r1 {3,S} {6,D}
6   C   ux {4,[S,D,T,B,Q]} {5,D}
7   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.676507,-1.83839,-2.07191,-1.80211,-1.52788,-1.48393,-2.61057],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.7363,'kcal/mol','+|-',4.17612),
        S298 = (-1.62469,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CC=C[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 153,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {7,S} {8,[S,D,T,B,Q]}
5   C u0 {3,S} {6,D}
6   C u0 {5,D}
7   C u0 {4,S}
8   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.41916,-4.26929,-4.83594,-4.74312,-4.42999,-4.38808,-4.92379],'cal/mol/K','+|-',[7.1692,6.88912,6.02526,5.48052,4.34642,3.59756,3.18248]),
        H298 = (72.3968,'kcal/mol','+|-',6.50534),
        S298 = (5.44764,'cal/mol/K','+|-',3.98484),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 154,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R_6R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {7,S} {8,[S,D,T,B,Q]}
5   C u0 r1 {3,S} {6,D}
6   C u0 r1 {5,D}
7   C u0 r1 {4,S}
8   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.69395,-6.4332,-6.64922,-6.32569,-5.48423,-4.99455,-4.79723],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (71.4325,'kcal/mol','+|-',4.17612),
        S298 = (4.5904,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 155,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R_N-6R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {7,S} {8,[S,D,T,B,Q]}
5   C u0 r1 {3,S} {6,D}
6   C u0 r0 {5,D}
7   C u0 r1 {4,S}
8   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.855633,-2.10538,-3.02267,-3.16056,-3.37575,-3.78161,-5.05036],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (73.3611,'kcal/mol','+|-',4.17612),
        S298 = (6.30489,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 156,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {7,S}
5   C u0 {3,S} {6,D}
6   C u0 r1 {5,D}
7   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.819147,-2.49141,-3.59744,-4.12642,-4.53241,-4.61275,-5.13228],'cal/mol/K','+|-',[5.4481,7.23044,6.57496,5.63474,3.72322,2.62393,2.07167]),
        H298 = (72.906,'kcal/mol','+|-',3.92294),
        S298 = (1.35918,'cal/mol/K','+|-',9.17303),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 157,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {7,S}
5   C u0 {3,S} {6,D}
6   C u0 r1 {5,D} {8,[S,D,T,B,Q]}
7   C u0 {4,S}
8   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.500301,-1.25101,-2.53704,-3.27769,-4.04534,-4.34123,-5.06452],'cal/mol/K','+|-',[6.16137,4.11972,4.40349,4.23744,3.20604,2.52172,2.28309]),
        H298 = (72.5663,'kcal/mol','+|-',3.05833),
        S298 = (-0.312201,'cal/mol/K','+|-',4.001),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 158,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Ext-8R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {7,S}
5   C u0 {3,S} {6,D}
6   C u0 r1 {5,D} {8,[S,D,T,B,Q]}
7   C u0 {4,S}
8   C ux {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9   C u0 {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.56192,-1.63614,-3.70023,-4.55605,-4.98382,-4.90408,-5.43571],'cal/mol/K','+|-',[9.11877,6.42426,5.51121,4.74319,3.58822,3.24711,3.17238]),
        H298 = (72.9205,'kcal/mol','+|-',5.98346),
        S298 = (-1.60269,'cal/mol/K','+|-',4.10546),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 159,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Ext-8R!H-R_Ext-1R-R",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S} {10,[S,D,T,B,Q]}
2    C   u0 r1 {1,S} {3,D}
3    C   u0 r1 {2,D} {5,S}
4    C   u0 {1,S} {7,S}
5    C   u0 r1 {3,S} {6,D}
6    C   u0 r1 {5,D} {8,[S,D,T,B,Q]}
7    C   u0 {4,S}
8    C   ux {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9    C   u0 {8,[S,D,T,B,Q]}
10   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.58583,0.340947,-2.1044,-3.30616,-4.38431,-4.64338,-5.34625],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (73.26,'kcal/mol','+|-',4.17612),
        S298 = (-2.52836,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CC=C(CC=CC)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 160,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_N-6R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {7,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C ux r0 {5,D}
7   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0571042,-0.626383,-1.19218,-1.55975,-2.29565,-3.0295,-4.45225],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (79.7027,'kcal/mol','+|-',1.69706),
        S298 = (0.90487,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 161,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {7,[B,D,T,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux {5,D}
7   C ux {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65315,-2.52829,-2.92586,-3.24561,-3.71955,-4.08764,-4.75022],'cal/mol/K','+|-',[4.6708,4.32854,4.19291,3.6051,2.57684,2.09561,1.86844]),
        H298 = (61.1819,'kcal/mol','+|-',11.0289),
        S298 = (1.23504,'cal/mol/K','+|-',4.27265),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 162,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {7,[B,D,T,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux r1 {5,D}
7   C ux {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.68451,-1.76047,-2.17653,-2.69202,-3.50257,-4.04188,-4.77987],'cal/mol/K','+|-',[2.63297,2.78397,2.8478,2.75538,2.67353,2.65648,2.6414]),
        H298 = (57.5791,'kcal/mol','+|-',4.84457),
        S298 = (0.317445,'cal/mol/K','+|-',3.34913),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 163,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {7,D}
5   C   u0 r1 {3,[S,D,T,B,Q]} {6,D} {8,[S,D,T,B,Q]}
6   C   u0 r1 {5,D}
7   C   u0 r0 {4,D}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8382,-2.05432,-2.60122,-3.10812,-3.88834,-4.4,-5.07116],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (57.3519,'kcal/mol','+|-',4.17612),
        S298 = (1.54882,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC(C)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 164,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {7,[B,D,T,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C   ux r1 {5,D}
7   C   ux {4,[B,D,T,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.82845,-2.06764,-2.43909,-2.80256,-3.40275,-3.82578,-4.51612],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (57.8169,'kcal/mol','+|-',4.17612),
        S298 = (-0.281388,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C1[CH]C=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 165,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing",
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
        Cpdata = ([0.378208,-3.2961,-3.67519,-3.7992,-3.93653,-4.1334,-4.72056],'cal/mol/K','+|-',[6.31222,6.08405,5.83981,5.12075,3.72659,2.98277,2.59617]),
        H298 = (64.7846,'kcal/mol','+|-',11.9291),
        S298 = (2.15264,'cal/mol/K','+|-',5.41465),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 166,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {7,D}
5   C   u0 r1 {3,[S,D,T,B,Q]} {6,D} {8,[S,D,T,B,Q]}
6   C   u0 r0 {5,D}
7   C   u0 r1 {4,D}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.69395,-6.4332,-6.64922,-6.32569,-5.48423,-4.99455,-4.79723],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (71.0825,'kcal/mol','+|-',4.17612),
        S298 = (4.9004,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 167,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing_Ext-6R!H-R",
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
        Cpdata = ([-1.50045,-2.18164,-2.66309,-2.85456,-3.25575,-3.66578,-4.56412],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (61.7599,'kcal/mol','+|-',4.17612),
        S298 = (0.795612,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C1C=C[CH]C=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 168,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1R-R",
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
        Cpdata = ([-0.368806,-1.0144,-1.67627,-2.23767,-3.10475,-3.70719,-4.53775],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (71.9674,'kcal/mol','+|-',1.69706),
        S298 = (0.736208,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 169,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S} {7,S}
4   C   u0 {1,S}
5   C   u0 {3,S} {6,D}
6   C   u0 {5,D}
7   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.852336,-1.38944,-1.78131,-2.08321,-2.53055,-2.91464,-3.92688],'cal/mol/K','+|-',[3.84722,3.03996,2.64617,2.56312,2.78304,3.26494,3.63173]),
        H298 = (74.7876,'kcal/mol','+|-',3.14541),
        S298 = (2.59852,'cal/mol/K','+|-',7.5996),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 170,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S} {7,S}
4   C u0 r1 {1,S}
5   C u0 r1 {3,S} {6,D}
6   C u0 r1 {5,D}
7   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46134,-1.76886,-2.01059,-2.27006,-2.81847,-3.36392,-4.47925],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (74.7956,'kcal/mol','+|-',1.69706),
        S298 = (4.05594,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=C[CH]CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 171,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,S} {7,S}
4   C                      u0 r1 {1,S}
5   C                      u0 r1 {3,S} {6,D}
6   C                      u0 r1 {5,D}
7   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.670186,-0.440882,-1.20812,-1.61611,-1.81074,-1.79142,-2.54597],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (74.7392,'kcal/mol','+|-',4.17612),
        S298 = (-1.04502,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=C[CH]CC=C1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 172,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   C   ux {5,D} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.138541,-0.817385,-1.3768,-1.80841,-2.48708,-3.05791,-4.10479],'cal/mol/K','+|-',[3.25972,2.26661,1.97142,1.97672,2.22789,2.41095,2.6596]),
        H298 = (74.286,'kcal/mol','+|-',2.96208),
        S298 = (0.584615,'cal/mol/K','+|-',4.50615),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 173,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux {5,D} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.615218,-1.05331,-1.50506,-1.93805,-2.70967,-3.33502,-4.44658],'cal/mol/K','+|-',[2.00799,2.00861,2.00999,2.01358,2.0167,2.00823,2.00071]),
        H298 = (74.486,'kcal/mol','+|-',2.4098),
        S298 = (1.30975,'cal/mol/K','+|-',2.05399),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 174,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_Ext-7C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C   ux r1 {5,D} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.678505,-1.11898,-1.57584,-2.02058,-2.80124,-3.39924,-4.46545],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (74.5628,'kcal/mol','+|-',1.69706),
        S298 = (1.47515,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=CC=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 175,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C",
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
        Cpdata = ([2.24484,0.362261,-0.735479,-1.16025,-1.37416,-1.67234,-2.39584],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (71.8636,'kcal/mol','+|-',4.17612),
        S298 = (-3.04105,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=CC=C[CH]C1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 176,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-5R!H-R",
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
        Cpdata = ([-0.899076,-1.27203,-1.63832,-1.99818,-2.68342,-3.30234,-4.46074],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (74.8945,'kcal/mol','+|-',1.69706),
        S298 = (1.41328,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC[CH]C=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 177,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
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
        Cpdata = ([0.290305,-1.37162,-2.48728,-2.96856,-3.5222,-3.95505,-4.66504],'cal/mol/K','+|-',[3.30083,3.334,3.35893,3.03349,2.76229,2.84108,2.2991]),
        H298 = (82.0731,'kcal/mol','+|-',15.7911),
        S298 = (-2.21008,'cal/mol/K','+|-',8.53245),
    ),
    shortDesc = """Radical correction fitted to 53 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 178,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O",
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
        Cpdata = ([-0.0856895,-3.12669,-4.08122,-4.01092,-3.9575,-4.21278,-4.21152],'cal/mol/K','+|-',[5.13032,3.67538,3.63306,3.61696,4.01418,4.0928,3.16296]),
        H298 = (80.8019,'kcal/mol','+|-',7.62004),
        S298 = (-6.13166,'cal/mol/K','+|-',9.375),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 179,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing",
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
        Cpdata = ([0.914966,-3.56142,-4.10919,-3.85995,-4.05261,-4.58965,-4.50763],'cal/mol/K','+|-',[7.4409,5.47022,5.24717,5.06498,5.43656,5.2167,3.68941]),
        H298 = (79.343,'kcal/mol','+|-',10.9694),
        S298 = (-3.5929,'cal/mol/K','+|-',12.5526),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 180,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C",
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
        Cpdata = ([0.801801,-4.39314,-4.82015,-4.35941,-4.13146,-4.51569,-4.15702],'cal/mol/K','+|-',[8.55265,4.59537,4.78517,5.21725,6.23771,5.98381,3.81279]),
        H298 = (80.271,'kcal/mol','+|-',11.675),
        S298 = (-4.21729,'cal/mol/K','+|-',14.1195),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 181,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-3R!H-R",
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
        Cpdata = ([-2.98713,-2.56399,-2.67443,-2.09973,-1.3552,-1.90933,-2.87187],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (75.5699,'kcal/mol','+|-',4.17612),
        S298 = (-10.58,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=C2CCC1OOC2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 182,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-1R-R",
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
        Cpdata = ([-2.53892,-2.76994,-3.34642,-2.55965,-1.88547,-2.32994,-2.76933],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (75.6488,'kcal/mol','+|-',4.17612),
        S298 = (-9.9188,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=CC2CC[C]1COO2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 183,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-4C-R",
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
        Cpdata = ([4.66539,-5.84718,-6.4095,-6.18936,-6.45812,-6.75105,-5.44992],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.8788,'kcal/mol','+|-',4.17612),
        S298 = (1.7541,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1[CH]C=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 184,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing",
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
        Cpdata = ([-0.800443,-2.81617,-4.06125,-4.11875,-3.88956,-3.94359,-4.00002],'cal/mol/K','+|-',[2.84408,2.49097,2.88219,3.03639,3.5006,3.7715,3.35171]),
        H298 = (81.8439,'kcal/mol','+|-',4.76255),
        S298 = (-7.94506,'cal/mol/K','+|-',4.66103),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 185,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R",
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
        Cpdata = ([-0.700811,-2.86716,-4.15805,-4.429,-4.79807,-5.06217,-5.05505],'cal/mol/K','+|-',[4.29472,3.89472,3.41294,3.16316,3.66819,3.82894,4.26503]),
        H298 = (84.0165,'kcal/mol','+|-',5.90639),
        S298 = (-8.0914,'cal/mol/K','+|-',3.96016),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 186,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H",
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
        Cpdata = ([-1.72823,-3.67097,-4.61195,-4.45537,-4.14084,-4.29889,-4.04322],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.9904,'kcal/mol','+|-',4.17612),
        S298 = (-8.93423,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1(C)C=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 187,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H",
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
        Cpdata = ([0.326603,-2.06335,-3.70416,-4.40262,-5.4553,-5.82545,-6.06689],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.0425,'kcal/mol','+|-',4.17612),
        S298 = (-7.24857,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1(C)C=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 188,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing",
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
        Cpdata = ([-0.560156,-2.60244,-3.9274,-3.95751,-3.64299,-3.65341,-3.76567],'cal/mol/K','+|-',[3.24325,2.99437,3.88253,4.16258,4.38142,4.56618,3.73211]),
        H298 = (80.987,'kcal/mol','+|-',5.0245),
        S298 = (-7.19419,'cal/mol/K','+|-',5.2896),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 189,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1R-R",
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
        Cpdata = ([0.0313433,-2.49885,-4.35468,-4.54692,-4.30128,-4.39572,-4.31876],'cal/mol/K','+|-',[4.46643,3.28936,3.29456,3.87818,5.28885,5.88579,5.55366]),
        H298 = (80.0127,'kcal/mol','+|-',6.47492),
        S298 = (-7.61462,'cal/mol/K','+|-',8.60247),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 190,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1R-R_Ext-7R!H-R_Ext-8R!H-R",
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
        Cpdata = ([-1.08383,-2.81898,-4.02793,-3.75317,-2.80245,-2.64064,-2.70464],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (79.0743,'kcal/mol','+|-',4.17612),
        S298 = (-10.4431,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COC1C=C[C](C)CC1OO - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 191,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-6O-R",
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
        Cpdata = ([-1.5068,-3.87368,-5.31831,-5.1841,-4.4715,-4.23825,-3.57459],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.3461,'kcal/mol','+|-',4.17612),
        S298 = (-6.26032,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1CC[CH]C=C1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 192,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_N-5R!H-inRing",
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
        Cpdata = ([-1.96086,-3.56909,-4.40303,-4.14323,-3.05883,-2.86717,-2.82734],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.9269,'kcal/mol','+|-',4.17612),
        S298 = (-10.6558,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOCC1=C[CH]CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 193,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O",
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
        Cpdata = ([0.377915,-0.96267,-2.11588,-2.72568,-3.42077,-3.89499,-4.77072],'cal/mol/K','+|-',[2.81725,2.74771,2.90931,2.76181,2.46382,2.57376,2.11753]),
        H298 = (82.2728,'kcal/mol','+|-',16.8144),
        S298 = (-1.29632,'cal/mol/K','+|-',7.2963),
    ),
    shortDesc = """Radical correction fitted to 41 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 194,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R",
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
        Cpdata = ([0.615394,-0.360856,-1.30045,-1.94713,-2.69563,-3.22577,-4.38679],'cal/mol/K','+|-',[3.81369,3.20876,2.65757,2.59764,2.96594,3.66923,3.06686]),
        H298 = (85.6374,'kcal/mol','+|-',31.4178),
        S298 = (-1.68891,'cal/mol/K','+|-',10.7628),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 195,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C",
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
        Cpdata = ([0.178232,-0.326952,-1.15311,-1.77651,-2.56059,-3.08387,-4.32925],'cal/mol/K','+|-',[3.56844,4.12437,3.31789,3.00615,3.45061,4.50702,3.68164]),
        H298 = (94.7147,'kcal/mol','+|-',30.018),
        S298 = (-0.0838457,'cal/mol/K','+|-',10.7387),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 196,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.165019,-0.447596,-1.11574,-1.5965,-2.42966,-3.17183,-4.46554],'cal/mol/K','+|-',[2.81506,2.58587,2.6056,2.58209,2.61567,2.61911,2.58427]),
        H298 = (76.6256,'kcal/mol','+|-',12.9613),
        S298 = (2.77763,'cal/mol/K','+|-',2.93396),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 197,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_7R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r1 {1,S} {6,S} {8,[S,D,T,B,Q]}
5   C   u0 r1 {3,S} {6,S}
6   C   u0 r1 {4,S} {5,S} {7,S}
7   C   u0 r1 {6,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.79604,-0.373959,-1.31728,-1.58777,-2.18831,-2.91931,-4.41535],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (69.6808,'kcal/mol','+|-',4.17612),
        S298 = (1.97394,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 198,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_7R!H-inRing_Int-7R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {6,S} {7,[S,D,T,B,Q]}
5   C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   C ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.276328,-0.515126,-1.00265,-1.59227,-2.55906,-3.31924,-4.52314],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (79.9831,'kcal/mol','+|-',4.17612),
        S298 = (3.20994,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 199,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing",
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
        Cpdata = ([0.185439,-0.261146,-1.17349,-1.8747,-2.632,-3.03589,-4.25492],'cal/mol/K','+|-',[4.70829,5.53653,4.42347,3.9794,4.59607,6.05818,4.9243]),
        H298 = (100.707,'kcal/mol','+|-',21.4129),
        S298 = (-1.64465,'cal/mol/K','+|-',13.1032),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 200,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_7R!H->C",
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
        Cpdata = ([0.896627,0.717659,-0.285961,-0.971231,-1.79165,-2.09711,-3.67812],'cal/mol/K','+|-',[5.63037,6.40904,4.26298,3.95068,4.65015,6.58021,4.45516]),
        H298 = (104.269,'kcal/mol','+|-',4.055),
        S298 = (-0.976689,'cal/mol/K','+|-',11.3473),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 201,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_7R!H->C_Ext-1R-R",
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
        Cpdata = ([-0.133269,-0.483726,-0.999066,-1.6067,-2.59749,-3.33569,-4.43766],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (104.012,'kcal/mol','+|-',1.69706),
        S298 = (1.26436,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1C[C]2C=CC1CC2 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 202,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_N-7R!H->C",
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
        Cpdata = ([-1.05914,-1.97406,-2.72668,-3.45576,-4.10261,-4.67875,-5.26431],'cal/mol/K','+|-',[4.91532,5.07476,4.7646,3.31962,5.18211,6.97322,7.46332]),
        H298 = (88.1446,'kcal/mol','+|-',22.5963),
        S298 = (-2.81358,'cal/mol/K','+|-',21.4176),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 203,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_N-7R!H->C_Ext-3R!H-R",
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
        Cpdata = ([-2.38957,-3.37732,-3.98671,-3.81281,-2.65113,-2.48143,-2.8742],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.4333,'kcal/mol','+|-',4.17612),
        S298 = (-10.3029,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COC1[CH]C=C(C)CC1OO - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 204,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C",
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
        Cpdata = ([1.29101,-0.413253,-1.52816,-2.21081,-2.90433,-3.44508,-4.47571],'cal/mol/K','+|-',[4.78838,2.3367,2.35261,2.82554,3.10061,3.04348,2.98217]),
        H298 = (73.5529,'kcal/mol','+|-',4.13763),
        S298 = (-4.16946,'cal/mol/K','+|-',10.4823),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 205,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R",
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
        Cpdata = ([2.84016,0.0348247,-1.67201,-2.59096,-3.22749,-3.64621,-4.48304],'cal/mol/K','+|-',[3.43788,2.7383,3.16509,3.61366,4.08652,4.1078,4.08681]),
        H298 = (72.4951,'kcal/mol','+|-',5.93483),
        S298 = (-8.0168,'cal/mol/K','+|-',3.75573),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 206,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C",
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
        Cpdata = ([3.11781,-0.198893,-2.20028,-3.31631,-4.12416,-4.55315,-5.39664],'cal/mol/K','+|-',[4.29587,3.21749,3.16301,3.18692,3.2817,3.26709,3.1684]),
        H298 = (73.4608,'kcal/mol','+|-',6.0361),
        S298 = (-7.81343,'cal/mol/K','+|-',4.88722),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 207,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C_Ext-3R!H-R",
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
    index = 208,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_N-7R!H->C",
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
        Cpdata = ([2.28484,0.502261,-0.615479,-1.14025,-1.43416,-1.83234,-2.65584],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (70.5636,'kcal/mol','+|-',4.17612),
        S298 = (-8.42355,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=C[CH]C=CC1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 209,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C",
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
        Cpdata = ([0.404234,-1.18538,-2.47922,-3.08912,-3.77718,-4.21977,-4.92835],'cal/mol/K','+|-',[2.46767,2.64001,2.95045,2.74513,2.1493,2.02132,1.83333]),
        H298 = (81.9737,'kcal/mol','+|-',4.20909),
        S298 = (-1.3259,'cal/mol/K','+|-',5.99906),
    ),
    shortDesc = """Radical correction fitted to 28 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 210,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.428694,-1.73177,-3.35136,-3.98349,-4.29754,-4.51996,-5.06869],'cal/mol/K','+|-',[2.96469,2.72579,2.68414,2.50415,2.30327,2.42617,2.31343]),
        H298 = (81.9907,'kcal/mol','+|-',3.67783),
        S298 = (-3.12249,'cal/mol/K','+|-',4.48833),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 211,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C",
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
        Cpdata = ([0.115944,-2.02577,-3.63138,-4.24058,-4.51619,-4.74361,-5.29525],'cal/mol/K','+|-',[2.67685,2.43239,2.43223,2.2823,2.15974,2.29948,2.14534]),
        H298 = (82.3156,'kcal/mol','+|-',3.51474),
        S298 = (-3.0019,'cal/mol/K','+|-',4.85698),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 212,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-7C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,S} {7,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   C ux {3,S} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   C ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.588561,-1.82626,-3.43155,-4.02652,-4.18343,-4.27049,-4.86138],'cal/mol/K','+|-',[4.93366,4.51027,4.16004,3.57287,3.18889,3.38772,3.47882]),
        H298 = (82.3819,'kcal/mol','+|-',6.13281),
        S298 = (-4.47467,'cal/mol/K','+|-',6.10639),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 213,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,S} {7,[S,D,T,B,Q]}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {3,S} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   C u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.750328,-2.96327,-4.38719,-4.61446,-4.03808,-3.84087,-4.34877],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.7976,'kcal/mol','+|-',4.17612),
        S298 = (-6.32156,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CCC1=C[CH]CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 214,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,S} {7,[S,D,T,B,Q]}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {3,S} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,[B,D,T,Q]}
9   C u0 r0 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.92745,-0.689236,-2.47592,-3.43859,-4.32877,-4.70012,-5.374],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.9662,'kcal/mol','+|-',4.17612),
        S298 = (-2.62778,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=C[CH]CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 215,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S} {7,S}
4   C   u0 {1,S} {6,S} {8,S}
5   C   u0 {3,S} {6,S}
6   C   u0 {4,S} {5,S}
7   C   u0 {3,S}
8   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0693579,-2.30048,-4.05468,-4.71154,-4.94312,-5.254,-5.65764],'cal/mol/K','+|-',[3.22769,3.39481,3.56971,3.71418,3.7395,3.78844,3.40335]),
        H298 = (82.2196,'kcal/mol','+|-',5.91147),
        S298 = (-3.34837,'cal/mol/K','+|-',4.84443),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 216,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-4C-R_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S} {7,S}
4   C u0 r1 {1,S} {6,S} {8,S}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,S} {5,S}
7   C u0 r0 {3,S}
8   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.297931,-1.86391,-3.46914,-4.02278,-4.23743,-4.51642,-5.21284],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.1291,'kcal/mol','+|-',4.17612),
        S298 = (-2.05085,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]C=C(C)CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 217,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-4C-R_N-8R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,S} {7,S}
4   C                      u0 r1 {1,S} {6,S} {8,S}
5   C                      u0 r1 {3,S} {6,S}
6   C                      u0 r1 {4,S} {5,S}
7   C                      u0 r0 {3,S}
8   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.159216,-2.73705,-4.64021,-5.4003,-5.6488,-5.99159,-6.10244],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.3101,'kcal/mol','+|-',4.17612),
        S298 = (-4.64589,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=C[CH]C(OOCC(C)C)CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 218,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-5R!H-R",
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
        Cpdata = ([0.068348,-2.05131,-3.70601,-4.11978,-4.31725,-4.62218,-5.27765],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.0451,'kcal/mol','+|-',4.17612),
        S298 = (-2.58525,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1CC[CH]C=C1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 219,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,[S,D,T,B,Q]} {7,S}
4   C                      u0 r1 {1,S} {6,S}
5   C                      u0 r1 {3,[S,D,T,B,Q]} {6,S}
6   C                      u0 r1 {4,S} {5,S}
7   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.30519,0.0322155,-1.67127,-2.44096,-2.98563,-3.17804,-3.70935],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.0415,'kcal/mol','+|-',4.17612),
        S298 = (-3.84605,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=C[CH]CCC1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 220,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R",
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
        Cpdata = ([-0.164984,-1.62047,-2.74854,-3.21493,-3.68434,-4.0163,-4.5403],'cal/mol/K','+|-',[2.31735,2.86421,3.61219,3.12182,1.83368,1.68811,1.97959]),
        H298 = (81.3075,'kcal/mol','+|-',2.29758),
        S298 = (-1.97438,'cal/mol/K','+|-',7.00112),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 221,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R",
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
        Cpdata = ([-0.530946,-1.73626,-2.58747,-2.98207,-3.49382,-3.83069,-4.25275],'cal/mol/K','+|-',[2.85941,4.08296,4.99026,4.12978,2.2269,2.30209,2.68024]),
        H298 = (81.433,'kcal/mol','+|-',3.29133),
        S298 = (-3.34311,'cal/mol/K','+|-',9.55267),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 222,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C",
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
        Cpdata = ([-0.134533,-1.14566,-1.93424,-2.51901,-3.48412,-4.00844,-4.58944],'cal/mol/K','+|-',[2.39797,3.62681,5.00848,4.44948,2.58278,2.43255,2.41422]),
        H298 = (81.5178,'kcal/mol','+|-',3.61327),
        S298 = (-1.71702,'cal/mol/K','+|-',7.15196),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 223,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_Sp-9R!H-8C",
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
        Cpdata = ([-0.230328,-2.52327,-4.15719,-4.41446,-3.97808,-3.78087,-4.41877],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.4376,'kcal/mol','+|-',4.17612),
        S298 = (-5.12156,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC[C]1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 224,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_N-Sp-9R!H-8C",
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
        Cpdata = ([-0.0962158,-0.59461,-1.04506,-1.76083,-3.28653,-4.09947,-4.6577],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (81.6962,'kcal/mol','+|-',1.69706),
        S298 = (-0.355208,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 225,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_N-8R!H->C",
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
        Cpdata = ([-1.91839,-3.80337,-4.87379,-4.60279,-3.52778,-3.20857,-3.07435],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.8348,'kcal/mol','+|-',4.17612),
        S298 = (-9.03442,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC[C]1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 226,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R",
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
        Cpdata = ([-0.0220959,-2.44666,-4.20155,-4.59176,-4.45371,-4.47061,-4.7809],'cal/mol/K','+|-',[4.22467,4.1049,3.81664,3.502,3.16501,3.2294,3.69648]),
        H298 = (80.7051,'kcal/mol','+|-',5.90836),
        S298 = (-3.12266,'cal/mol/K','+|-',4.97398),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 227,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R_8R!H->C",
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
        Cpdata = ([0.968348,-1.52131,-3.44601,-4.05978,-4.40725,-4.70218,-5.45765],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.7651,'kcal/mol','+|-',4.17612),
        S298 = (-1.76525,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1CCC=C[C]1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 228,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R_N-8R!H->C",
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
        Cpdata = ([-1.01254,-3.37202,-4.95709,-5.12373,-4.50018,-4.23904,-4.10415],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.6452,'kcal/mol','+|-',4.17612),
        S298 = (-4.48007,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1CCC=C[C]1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 229,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {6,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]} {8,[S,D,T,B,Q]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]}
7   C   ux {1,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19793,-1.33391,-3.40914,-3.96278,-4.32743,-4.59642,-5.39284],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (80.3491,'kcal/mol','+|-',4.17612),
        S298 = (-1.23085,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1C=C[C](C)CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 230,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R",
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
        Cpdata = ([1.08197,-0.27446,-1.61996,-2.3181,-3.32785,-3.84849,-4.90589],'cal/mol/K','+|-',[2.50981,2.07831,2.4153,2.62253,2.64868,2.3073,1.91276]),
        H298 = (83.0055,'kcal/mol','+|-',3.81557),
        S298 = (0.150419,'cal/mol/K','+|-',3.37806),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 231,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing",
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
        Cpdata = ([2.16907,0.511588,-1.41518,-2.25949,-3.28055,-3.69978,-5.03783],'cal/mol/K','+|-',[3.21124,3.56016,4.28473,4.51936,4.20971,3.63373,3.49391]),
        H298 = (81.1168,'kcal/mol','+|-',7.63038),
        S298 = (0.944066,'cal/mol/K','+|-',4.60256),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 232,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing_Ext-5R!H-R",
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
        Cpdata = ([2.36658,1.08981,-0.392996,-1.11797,-2.2981,-3.06693,-4.51254],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (79.4086,'kcal/mol','+|-',4.17612),
        S298 = (2.12641,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1CC12C=C[CH]CC2 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 233,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing",
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
        Cpdata = ([0.686665,-0.560295,-1.69443,-2.33942,-3.34505,-3.90257,-4.85791],'cal/mol/K','+|-',[2.42617,1.94102,2.51079,2.74109,2.90544,2.62855,2.13714]),
        H298 = (83.4226,'kcal/mol','+|-',2.84854),
        S298 = (-0.13818,'cal/mol/K','+|-',3.55657),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 234,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R",
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
        Cpdata = ([1.24933,-0.591835,-2.18765,-2.86611,-3.92981,-4.2663,-5.11159],'cal/mol/K','+|-',[3.16228,3.16228,3.16228,3.16228,3.16228,3.16228,3.16228]),
        H298 = (83.0078,'kcal/mol','+|-',5.90593),
        S298 = (-1.51972,'cal/mol/K','+|-',3.16228),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 235,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R_Ext-7R!H-R",
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
        Cpdata = ([1.24933,-0.591835,-2.18765,-2.86611,-3.92981,-4.2663,-5.11159],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.0078,'kcal/mol','+|-',4.17612),
        S298 = (-1.51972,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1C=C[CH]C(C)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 236,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-5R!H-R",
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
        Cpdata = ([1.27252,-0.837608,-2.54074,-3.46,-4.59476,-5.08559,-5.41317],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.3593,'kcal/mol','+|-',4.17612),
        S298 = (-0.712704,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1(C)C=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 237,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,S} {6,S} {7,[S,D,T,B,Q]}
5   C   u0 {3,S} {6,S}
6   C   u0 {4,S} {5,S}
7   R!H u0 r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.69031,0.103933,-1.45205,-2.24782,-3.45224,-4.19769,-5.28041],'cal/mol/K','+|-',[3.09457,3.162,3.24584,3.44652,3.29802,3.35255,2.91103]),
        H298 = (78.6471,'kcal/mol','+|-',10.8406),
        S298 = (1.44942,'cal/mol/K','+|-',3.91398),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 238,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,S} {6,S} {7,[S,D,T,B,Q]} {8,S}
5   C   u0 {3,S} {6,S}
6   C   u0 {4,S} {5,S}
7   R!H u0 r1 {4,[S,D,T,B,Q]}
8   C   u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.54968,0.189218,-1.00939,-1.67122,-3.04687,-4.13022,-5.13906],'cal/mol/K','+|-',[3.91724,4.06061,3.61037,3.52767,3.80481,4.36309,3.62428]),
        H298 = (76.4331,'kcal/mol','+|-',10.2846),
        S298 = (2.29327,'cal/mol/K','+|-',3.19611),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 239,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {6,S} {7,[S,D,T,B,Q]} {8,S}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,S} {5,S}
7   O u0 r1 {4,[S,D,T,B,Q]}
8   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.732308,-0.711378,-1.6253,-2.22399,-3.79491,-5.19303,-5.7651],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (73.4563,'kcal/mol','+|-',4.17612),
        S298 = (2.45726,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1CC2([CH]C=CCC2)OO1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 240,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_N-7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {6,S} {7,[S,D,T,B,Q]} {8,S}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,S} {5,S}
7   C u0 r1 {4,[S,D,T,B,Q]}
8   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.36705,1.08981,-0.393474,-1.11845,-2.29882,-3.0674,-4.51302],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (79.41,'kcal/mol','+|-',4.17612),
        S298 = (2.12928,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1CC12[CH]C=CCC2 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 241,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S} {7,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   R!H ux r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.121967,-1.57372,-2.59117,-3.2103,-4.02804,-4.64812,-5.23764],'cal/mol/K','+|-',[3.16913,3.57809,3.93215,3.81196,3.74575,3.65199,3.32718]),
        H298 = (82.9536,'kcal/mol','+|-',6.24914),
        S298 = (-1.37779,'cal/mol/K','+|-',8.32606),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 242,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S} {7,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   R!H ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31398,-1.61485,-2.57919,-3.06356,-3.69089,-4.27527,-4.79451],'cal/mol/K','+|-',[3.3523,4.01414,4.42716,4.19507,3.67457,3.41451,2.56678]),
        H298 = (83.6336,'kcal/mol','+|-',3.60164),
        S298 = (-1.95163,'cal/mol/K','+|-',8.75902),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 243,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {6,S} {7,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   O ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42456,-3.44414,-4.61696,-4.88554,-4.9387,-5.37833,-4.94685],'cal/mol/K','+|-',[4.29472,3.89472,3.41294,3.16316,3.66819,3.82894,4.26503]),
        H298 = (82.0983,'kcal/mol','+|-',5.90639),
        S298 = (-6.52375,'cal/mol/K','+|-',3.96016),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 244,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Sp-11R!H=10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {6,S} {7,S}
5    C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6    C ux r1 {4,S} {5,[S,T,Q,B]}
7    O ux r0 {4,S} {8,[S,D,T,B,Q]}
8    O ux {7,[S,D,T,B,Q]} {9,S}
9    C u0 r0 {8,S} {10,[S,D,T,B,Q]}
10   C ux {9,[S,D,T,B,Q]} {11,D}
11   C u0 r0 {10,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.45197,-4.24795,-5.07086,-4.91191,-4.28147,-4.61504,-3.93502],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.0722,'kcal/mol','+|-',4.17612),
        S298 = (-7.36658,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1(C)[CH]C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 245,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_N-Sp-11R!H=10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {6,S} {7,S}
5    C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6    C ux r1 {4,S} {5,[S,T,Q,B]}
7    O ux r0 {4,S} {8,[S,D,T,B,Q]}
8    O ux {7,[S,D,T,B,Q]} {9,S}
9    C u0 r0 {8,S} {10,[S,D,T,B,Q]}
10   C ux {9,[S,D,T,B,Q]} {11,S}
11   C u0 r0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.397145,-2.64033,-4.16307,-4.85916,-5.59593,-6.14161,-5.95869],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.1244,'kcal/mol','+|-',4.17612),
        S298 = (-5.68093,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1(C)[CH]C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 246,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_N-7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {6,S} {7,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   C ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.320636,-0.569539,-1.41475,-2.02244,-2.97785,-3.64495,-4.70746],'cal/mol/K','+|-',[3.04403,2.44867,3.26868,3.71689,3.99534,3.63132,2.76886]),
        H298 = (84.0688,'kcal/mol','+|-',3.18316),
        S298 = (0.661018,'cal/mol/K','+|-',3.62102),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 247,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_N-7R!H->O_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {6,S} {7,S} {8,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]}
7   C   ux r0 {4,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.27252,-0.837608,-2.54074,-3.46,-4.59476,-5.02559,-5.41317],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.3693,'kcal/mol','+|-',4.17612),
        S298 = (-0.712704,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1(C)[CH]C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 248,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_N-Sp-7R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {6,S} {7,D}
5   C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.934105,-1.3475,-2.65702,-4.01738,-5.88241,-6.69881,-7.67484],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (76.796,'kcal/mol','+|-',4.17612),
        S298 = (1.77829,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 249,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux {1,S} {6,[B,D,T,Q]}
5   C ux {3,S} {6,[S,T,Q,B]}
6   C ux {4,[B,D,T,Q]} {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.827664,-1.20647,-1.84802,-2.30942,-2.8591,-3.4169,-4.77515],'cal/mol/K','+|-',[3.67826,3.74287,3.85003,4.03152,3.54763,3.06188,2.84444]),
        H298 = (74.2494,'kcal/mol','+|-',3.68535),
        S298 = (0.561369,'cal/mol/K','+|-',3.16969),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 250,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux r1 {1,S} {6,[B,D,T,Q]}
5   C   ux r1 {3,S} {6,[S,T,Q,B]}
6   C   ux r1 {4,[B,D,T,Q]} {5,[S,T,Q,B]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.23965,-2.66112,-3.37235,-3.94908,-4.18307,-4.38328,-5.55377],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (73.0829,'kcal/mol','+|-',4.17612),
        S298 = (1.61268,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 251,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_N-Sp-2R!H-1R",
    group = 
"""
1 * C u1 r1 {2,D} {4,S}
2   C u0 r1 {1,D} {3,D}
3   C u0 r1 {2,D}
4   C u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.503132,-2.03451,-2.79058,-3.01131,-3.26561,-4.11574,-4.91171],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (89.3249,'kcal/mol','+|-',4.17612),
        S298 = (5.65154,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C=[C]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 252,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C u0 {1,[S,D,T,B,Q]} {3,D}
3   C u0 r1 {2,D}
4   C u0 {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.429944,-0.89717,-1.43494,-1.98847,-2.86434,-3.50861,-4.48855],'cal/mol/K','+|-',[1.06918,1.10344,1.11395,1.09977,1.06353,1.05551,1.04405]),
        H298 = (114.914,'kcal/mol','+|-',7.90133),
        S298 = (0.664719,'cal/mol/K','+|-',2.29238),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 253,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C   u0 {1,[S,D,T,B,Q]} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,D}
5   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.40589,-0.866651,-1.40769,-1.96462,-2.85618,-3.51197,-4.48467],'cal/mol/K','+|-',[1.07677,1.09945,1.11806,1.10969,1.09121,1.08503,1.07292]),
        H298 = (115.175,'kcal/mol','+|-',7.11341),
        S298 = (0.50639,'cal/mol/K','+|-',1.85833),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 254,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C   u0 {1,[S,D,T,B,Q]} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,D} {6,[S,D,T,B,Q]}
5   R!H u0 {3,S}
6   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.387795,-0.827397,-1.35883,-1.92023,-2.8294,-3.49586,-4.4774],'cal/mol/K','+|-',[1.15855,1.16648,1.17548,1.17193,1.16905,1.16873,1.15824]),
        H298 = (114.264,'kcal/mol','+|-',5.72776),
        S298 = (0.395853,'cal/mol/K','+|-',1.92235),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 255,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R_Ext-4R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C   u0 {1,[S,D,T,B,Q]} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,D} {6,[S,D,T,B,Q]}
5   R!H u0 {3,S}
6   C   ux {4,[S,D,T,B,Q]} {7,D}
7   O   u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.347747,-0.726002,-1.21883,-1.79136,-2.74558,-3.43716,-4.43897],'cal/mol/K','+|-',[2.00061,2.00254,2.00158,2.00003,2.00004,2.00006,2.00002]),
        H298 = (110.795,'kcal/mol','+|-',3.52642),
        S298 = (1.37865,'cal/mol/K','+|-',2.02379),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 256,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R_Ext-4R!H-R_Ext-6R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,D} {6,[S,D,T,B,Q]}
5   C u0 r1 {3,S}
6   C ux r1 {4,[S,D,T,B,Q]} {7,D}
7   O u0 r0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.330326,-0.690371,-1.19076,-1.7876,-2.7503,-3.44249,-4.43616],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (109.881,'kcal/mol','+|-',1.69706),
        S298 = (1.48803,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=[C]C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 257,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,D} {6,[S,D,T,B,Q]}
5   O u0 r1 {3,S}
6   C ux r1 {4,[S,D,T,B,Q]} {7,D}
7   O u0 r0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.365167,-0.761633,-1.2469,-1.79512,-2.74086,-3.43183,-4.44177],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (111.708,'kcal/mol','+|-',1.69706),
        S298 = (1.26927,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=[C]C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 258,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,D}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,D} {6,S}
5   C u0 r1 {3,S} {7,S}
6   C u0 r1 {4,S}
7   O u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.445597,-0.892311,-1.42277,-1.99247,-2.943,-3.6123,-4.53464],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (116.455,'kcal/mol','+|-',2.4),
        S298 = (-0.00743587,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CC=[C]C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
OC1=CC=[C]C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 259,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.161599,-0.898907,-1.87544,-2.48163,-3.23378,-3.83404,-4.75932],'cal/mol/K','+|-',[2.85701,3.3393,4.04545,4.2954,4.20386,4.28689,4.32067]),
        H298 = (91.5158,'kcal/mol','+|-',41.6937),
        S298 = (1.64472,'cal/mol/K','+|-',7.08074),
    ),
    shortDesc = """Radical correction fitted to 84 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 260,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.184205,-0.875022,-1.87392,-2.4791,-3.20268,-3.80449,-4.73289],'cal/mol/K','+|-',[2.94519,3.50397,4.23861,4.48023,4.31595,4.3778,4.47181]),
        H298 = (88.9041,'kcal/mol','+|-',40.9796),
        S298 = (1.65099,'cal/mol/K','+|-',7.3706),
    ),
    shortDesc = """Radical correction fitted to 77 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 261,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0454939,-0.964689,-1.87697,-2.38005,-2.99347,-3.45338,-4.29804],'cal/mol/K','+|-',[3.2133,4.25034,4.90466,4.85307,4.35226,4.25208,4.93455]),
        H298 = (83.3622,'kcal/mol','+|-',53.7902),
        S298 = (2.30781,'cal/mol/K','+|-',8.65745),
    ),
    shortDesc = """Radical correction fitted to 36 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 262,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.828307,-2.6666,-3.93752,-4.31444,-4.59198,-4.65233,-5.65778],'cal/mol/K','+|-',[5.43674,5.78806,5.77857,5.42952,4.40073,3.95211,4.6122]),
        H298 = (91.8703,'kcal/mol','+|-',18.0554),
        S298 = (4.11531,'cal/mol/K','+|-',5.87394),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 263,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   C   ux {1,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.874423,-2.7235,-3.95784,-4.30853,-4.5844,-4.64625,-5.75384],'cal/mol/K','+|-',[5.64651,6.00731,6.01169,5.65023,4.57905,4.1121,4.74091]),
        H298 = (90.2355,'kcal/mol','+|-',13.82),
        S298 = (3.95214,'cal/mol/K','+|-',5.97947),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 264,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.936698,-0.693913,-1.8689,-2.26978,-2.74509,-2.89007,-3.84016],'cal/mol/K','+|-',[2.65556,2.79001,2.58058,2.46159,2.29509,2.24587,2.25901]),
        H298 = (96.7273,'kcal/mol','+|-',5.55353),
        S298 = (3.22556,'cal/mol/K','+|-',3.30676),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 265,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   ux r0 {1,S} {3,D}
3   C   u0 r0 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   u0 r1 {1,S} {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.932851,-1.03775,-1.88227,-1.92903,-2.22357,-2.25412,-3.07931],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.8824,'kcal/mol','+|-',4.17612),
        S298 = (1.64121,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O)=C[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 266,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16592,-0.47708,-1.85497,-2.42414,-2.91909,-3.04243,-4.02559],'cal/mol/K','+|-',[3.39415,3.67809,3.46155,3.22186,2.91134,2.78252,2.72492]),
        H298 = (96.9718,'kcal/mol','+|-',6.84611),
        S298 = (3.90358,'cal/mol/K','+|-',3.51466),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 267,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C_Ext-4C-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D}
4   C u0 r1 {1,S} {5,S} {6,S}
5   C u0 r1 {1,S} {4,S}
6   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.3102,0.843126,-0.748244,-1.56205,-2.48091,-2.87825,-4.23753],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (94.1697,'kcal/mol','+|-',4.17612),
        S298 = (2.70119,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]1CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 268,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C_Ext-4C-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.593781,-1.13718,-2.40833,-2.85518,-3.13818,-3.12453,-3.91962],'cal/mol/K','+|-',[3.44251,3.6422,3.64449,3.60116,3.53078,3.46263,3.35374]),
        H298 = (98.3729,'kcal/mol','+|-',5.91604),
        S298 = (4.50477,'cal/mol/K','+|-',3.56342),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 269,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C_Ext-4C-R_N-6R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {7,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.112779,-1.77609,-3.04887,-3.46431,-3.69343,-3.62325,-4.31451],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.4952,'kcal/mol','+|-',4.17612),
        S298 = (5.0855,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[C]1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 270,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux {1,S}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.32358,-4.36694,-5.72222,-6.07761,-6.17625,-6.15625,-7.0065],'cal/mol/K','+|-',[6.81729,6.94726,6.87749,6.32984,4.70782,3.97003,4.97093]),
        H298 = (84.4693,'kcal/mol','+|-',10.6065),
        S298 = (4.95912,'cal/mol/K','+|-',7.33186),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 271,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux {1,S}
5   R!H ux {1,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.43484,-4.50272,-5.90499,-6.28005,-6.39569,-6.44587,-7.03009],'cal/mol/K','+|-',[7.58659,7.72081,7.61289,6.97764,5.10813,4.12534,5.54115]),
        H298 = (82.6206,'kcal/mol','+|-',6.12442),
        S298 = (3.87249,'cal/mol/K','+|-',5.6219),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 272,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C_2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux {1,S}
5   C ux {1,[S,D,T,B,Q]}
6   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.17443,-3.89856,-5.1147,-5.51631,-5.87127,-6.18157,-5.91054],'cal/mol/K','+|-',[8.63713,8.3315,7.76444,7.00203,5.20803,4.52715,2.6799]),
        H298 = (81.9732,'kcal/mol','+|-',6.13797),
        S298 = (4.05289,'cal/mol/K','+|-',6.39842),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 273,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C_2R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux {1,S} {7,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.87978,-4.783,-6.10153,-6.53033,-6.72582,-6.91196,-6.2522],'cal/mol/K','+|-',[9.95622,9.19313,8.13783,6.93048,4.72505,4.13597,2.67166]),
        H298 = (82.6705,'kcal/mol','+|-',6.47581),
        S298 = (5.03202,'cal/mol/K','+|-',6.12926),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 274,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C_2R!H-inRing_Ext-4C-R_Ext-6C-R_Int-8R!H-7R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   u0 r1 {1,S} {3,D} {6,S}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {7,[S,D,T,B,Q]}
5   C   u0 {1,S}
6   C   u0 r1 {2,S} {8,S}
7   R!H ux {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H u0 r1 {6,S} {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0687,-3.22783,-5.02213,-6.08545,-7.17103,-8.06177,-6.46962],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.1247,'kcal/mol','+|-',4.17612),
        S298 = (3.45427,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1COOC[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 275,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C_2R!H-inRing_Ext-4C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
6   C   ux r1 {2,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.759452,-1.35966,-2.8975,-3.56016,-4.56254,-5.06491,-5.85658],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.0517,'kcal/mol','+|-',4.17612),
        S298 = (3.40049,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CCC(C)[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 276,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S}
5   R!H ux r1 {1,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.47647,-6.9194,-9.06614,-9.33503,-8.49338,-7.50308,-11.5083],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.2099,'kcal/mol','+|-',4.17612),
        S298 = (3.15088,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[C]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 277,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S} {5,S}
2   C                      u0 {1,S} {3,D} {6,S}
3   C                      u0 r0 {2,D}
4   C                      u0 r1 {1,S}
5   R!H                    u0 {1,S}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.76728,-3.68803,-4.8084,-5.06539,-5.079,-4.70816,-6.88854],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.7128,'kcal/mol','+|-',4.17612),
        S298 = (10.3923,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1OC[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 278,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux r1 {1,S}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.524508,-1.01551,-2.20155,-2.76874,-3.60074,-4.06313,-5.17429],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (92.1437,'kcal/mol','+|-',4.17612),
        S298 = (5.99254,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 279,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_N-2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux r1 {1,S}
5   C ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.63403,-4.7188,-5.57251,-5.42759,-5.21352,-4.9503,-8.38582],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.4653,'kcal/mol','+|-',4.17612),
        S298 = (-0.497217,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O)=C[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 280,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   ux {1,S} {3,D}
3   C   u0 r0 {2,D}
4   O   ux r1 {1,S}
5   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.228808,-1.92686,-3.67343,-4.39133,-4.69059,-4.73131,-4.40912],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (113.123,'kcal/mol','+|-',4.17612),
        S298 = (6.23655,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C1O[C]1OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 281,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.224835,-0.457794,-1.23408,-1.76365,-2.41643,-2.97495,-3.63518],'cal/mol/K','+|-',[1.78608,3.16186,4.20351,4.49164,4.46315,4.83202,5.55975]),
        H298 = (74.4215,'kcal/mol','+|-',64.8325),
        S298 = (1.50431,'cal/mol/K','+|-',10.7958),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 282,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C",
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
        Cpdata = ([0.165844,-0.375104,-1.01692,-1.50962,-2.14475,-2.6847,-3.11999],'cal/mol/K','+|-',[1.77871,2.8736,3.9362,4.40376,4.74379,5.4388,6.20106]),
        H298 = (70.8418,'kcal/mol','+|-',76.7018),
        S298 = (1.34438,'cal/mol/K','+|-',12.0136),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 283,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_5R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0500516,-1.27335,-2.41111,-3.10011,-3.73495,-4.41183,-4.49728],'cal/mol/K','+|-',[3.46938,4.85596,5.76731,5.78683,4.69471,4.58652,2.59642]),
        H298 = (90.5582,'kcal/mol','+|-',9.122),
        S298 = (0.784046,'cal/mol/K','+|-',6.17083),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 284,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_5R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {6,S}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
6   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39751,-3.5076,-5.16264,-5.97765,-6.06377,-6.65594,-4.82172],'cal/mol/K','+|-',[3.82482,4.7656,4.81478,4.02586,3.16627,3.51832,4.53126]),
        H298 = (85.9133,'kcal/mol','+|-',7.38941),
        S298 = (-0.900458,'cal/mol/K','+|-',7.84628),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 285,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_5R!H->O_Ext-2R!H-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   C   u0 r1 {2,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15821,-4.76811,-6.44629,-6.85852,-6.0076,-6.11068,-3.67432],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.3431,'kcal/mol','+|-',4.17612),
        S298 = (-3.43926,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1[CH]C(=C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 286,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_5R!H->O_Int-4C-2R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux r1 {1,S} {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.62813,-0.346037,-1.76043,-2.26587,-3.01141,-3.49475,-4.314],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.7713,'kcal/mol','+|-',4.17612),
        S298 = (4.55835,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 287,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.245006,-0.0457457,-0.505715,-0.926446,-1.56168,-2.05142,-2.61498],'cal/mol/K','+|-',[1.37357,2.00505,2.98197,3.61189,4.56692,5.49714,7.04369]),
        H298 = (64.732,'kcal/mol','+|-',85.8174),
        S298 = (1.54984,'cal/mol/K','+|-',13.9797),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 288,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.142721,-0.110585,-0.498265,-0.875777,-1.46312,-1.93305,-2.36008],'cal/mol/K','+|-',[1.35457,2.22403,3.39599,4.11923,5.18059,6.21519,7.89198]),
        H298 = (62.4049,'kcal/mol','+|-',91.3179),
        S298 = (-0.123298,'cal/mol/K','+|-',2.96502),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 289,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.239892,-0.552018,-1.33137,-1.91093,-2.76963,-3.46875,-4.32068],'cal/mol/K','+|-',[1.88698,2.72186,3.60424,3.87087,3.53094,3.08906,1.86411]),
        H298 = (85.279,'kcal/mol','+|-',4.26666),
        S298 = (0.466073,'cal/mol/K','+|-',3.11991),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 290,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Ext-5C-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {4,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux r1 {2,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.176122,-0.122722,-0.658088,-1.27327,-2.30199,-3.0996,-4.34797],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (84.0747,'kcal/mol','+|-',1.69706),
        S298 = (0.392991,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]CC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 291,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Ext-5C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]} {7,S}
6   C   ux r1 {2,[S,D,T,B,Q]}
7   C   ux r1 {5,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0884508,-2.32997,-4.066,-4.92703,-5.43758,-5.6665,-3.99703],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.7506,'kcal/mol','+|-',4.17612),
        S298 = (-1.54806,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]C(=C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 292,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Int-6R!H-5C_Sp-6R!H-5C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,S}
6   C ux {2,[S,D,T,B,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0281294,0.522449,0.896274,1.06233,1.27241,1.4599,2.4175],'cal/mol/K','+|-',[2.43742,3.16062,4.11893,4.93804,6.93909,9.0172,10.1614]),
        H298 = (1.4806,'kcal/mol','+|-',127.494),
        S298 = (0.180768,'cal/mol/K','+|-',2.66329),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 293,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Int-6R!H-5C_Sp-6R!H-5C_Sp-5C-4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux r1 {1,S} {5,S}
5   C ux r1 {4,S} {6,S}
6   C ux r1 {2,[S,D,T,B,Q]} {5,S}
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
    index = 294,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Int-6R!H-5C_Sp-6R!H-5C_N-Sp-5C-4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux r1 {1,S} {5,T}
5   C ux r1 {4,T} {6,S}
6   C ux r1 {2,[S,D,T,B,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.212362,-0.521882,-0.7979,-1.12004,-2.01784,-2.93152,-2.57073],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (78.8313,'kcal/mol','+|-',4.17612),
        S298 = (0.773844,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C#CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 295,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Int-6R!H-5C_N-Sp-6R!H-5C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {6,S}
3   C u0 r0 {2,D}
4   C u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C u0 r1 {4,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   C u0 r1 {2,S} {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0699417,0.062605,-0.451155,-1.10476,-2.15726,-2.99747,-4.34326],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (83.8645,'kcal/mol','+|-',1.69706),
        S298 = (-1.96348,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 296,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17653,0.72844,0.0472595,-0.493509,-0.957762,-1.12817,-1.77485],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.3024,'kcal/mol','+|-',4.17612),
        S298 = (25.4375,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C1[CH]C1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 297,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.812109,0.166506,-0.876585,-1.51058,-2.54835,-3.31103,-4.75363],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.0157,'kcal/mol','+|-',4.17612),
        S298 = (0.639767,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 298,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   O ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.375998,-0.669687,-1.79057,-2.4146,-3.11261,-3.71873,-4.95535],'cal/mol/K','+|-',[2.55605,4.53872,5.48724,5.31999,4.14745,3.16779,2.69442]),
        H298 = (83.489,'kcal/mol','+|-',8.09689),
        S298 = (1.91414,'cal/mol/K','+|-',8.34866),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 299,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D} {6,S}
3   C u0 r0 {2,D}
4   O u0 {1,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]}
6   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.644497,-1.88391,-3.78257,-4.33336,-4.38091,-4.58726,-5.73388],'cal/mol/K','+|-',[4.26613,6.88268,7.22947,7.03815,5.98227,4.71857,3.90788]),
        H298 = (88.2698,'kcal/mol','+|-',12.5208),
        S298 = (4.99188,'cal/mol/K','+|-',10.9259),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 300,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {6,S}
3   C   u0 r0 {2,D}
4   O   u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C   u0 r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   u0 r1 {2,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.06544,1.42881,-0.264604,-0.945121,-1.62447,-2.64032,-4.20234],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.4936,'kcal/mol','+|-',4.17612),
        S298 = (0.846007,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]OC(O)C1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 301,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C_Ext-2R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {6,S}
3   C u0 r0 {2,D}
4   O u0 r1 {1,S} {5,S}
5   C u0 r1 {4,S} {6,S}
6   C u0 r1 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.10407,-2.14544,-4.08637,-4.57591,-4.50146,-4.53279,-5.87355],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.2673,'kcal/mol','+|-',4.17612),
        S298 = (3.15513,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]OCC1=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 302,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C_Ext-2R!H-R_Int-6R!H-5R!H_N-Sp-6R!H-5R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {6,S}
3   C u0 r0 {2,D}
4   O u0 r1 {1,S} {5,S}
5   C u0 r1 {4,S} {6,[B,D,T,Q]}
6   C u0 r1 {2,S} {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23601,-4.93511,-6.99674,-7.47906,-7.01681,-6.58866,-7.12575],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (94.0485,'kcal/mol','+|-',4.17612),
        S298 = (10.9745,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]OC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 303,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   O   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 304,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.966144,0.172292,-0.699022,-1.35817,-2.38299,-3.1304,-4.23906],'cal/mol/K','+|-',[1.66768,1.71651,1.81018,1.8193,1.76037,1.67132,1.68073]),
        H298 = (96.2997,'kcal/mol','+|-',7.93658),
        S298 = (2.33801,'cal/mol/K','+|-',1.91756),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 305,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_4R!H->C_Ext-3C-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.882659,0.0629487,-0.865928,-1.53929,-2.54351,-3.22134,-4.14111],'cal/mol/K','+|-',[2.01536,2.067,2.13345,2.12108,2.0606,2.01366,2.0214]),
        H298 = (95.5971,'kcal/mol','+|-',10.5931),
        S298 = (2.35639,'cal/mol/K','+|-',2.45206),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 306,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_4R!H->C_Ext-3C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S}
5   C   u0 r0 {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.794855,-0.121614,-1.12852,-1.78904,-2.7189,-3.30413,-4.03738],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (91.9493,'kcal/mol','+|-',1.69706),
        S298 = (1.85481,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 307,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   O ux r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.132343,-0.623548,-1.20065,-1.64007,-2.45156,-3.16236,-4.41704],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.706,'kcal/mol','+|-',1.69706),
        S298 = (1.25502,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 308,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.310854,-0.793153,-1.87114,-2.56954,-3.39369,-4.12506,-5.12992],'cal/mol/K','+|-',[2.76557,2.77225,3.65173,4.22023,4.35348,4.49526,3.95573]),
        H298 = (94.1592,'kcal/mol','+|-',19.4913),
        S298 = (1.05128,'cal/mol/K','+|-',5.87502),
    ),
    shortDesc = """Radical correction fitted to 41 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 309,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.293221,-0.906813,-1.97815,-2.61693,-3.36219,-4.06989,-5.13143],'cal/mol/K','+|-',[3.17565,3.35907,4.0665,4.47391,4.73739,4.97829,4.77809]),
        H298 = (99.0299,'kcal/mol','+|-',17.2105),
        S298 = (1.03198,'cal/mol/K','+|-',6.69222),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 310,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   ux {1,S} {3,D}
3   O   u0 r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {1,S} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.196186,-0.640764,-1.3589,-1.83658,-2.38999,-2.89337,-4.06764],'cal/mol/K','+|-',[2.32591,1.78332,1.59719,1.88554,2.56837,2.68937,2.20899]),
        H298 = (102.924,'kcal/mol','+|-',11.5634),
        S298 = (3.30457,'cal/mol/K','+|-',4.65592),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 311,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   ux {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {1,S} {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.252802,-0.903632,-1.46299,-1.84401,-2.30509,-2.80079,-4.02688],'cal/mol/K','+|-',[2.14749,1.85429,1.73079,2.07314,2.93672,3.16078,2.69799]),
        H298 = (103.408,'kcal/mol','+|-',13.4564),
        S298 = (3.49783,'cal/mol/K','+|-',5.87241),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 312,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   ux {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {1,S} {4,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00357719,-0.869382,-1.60899,-2.08832,-2.46765,-2.80576,-3.87799],'cal/mol/K','+|-',[2.50615,2.4103,2.3979,2.42869,2.50887,2.44039,2.39145]),
        H298 = (98.3258,'kcal/mol','+|-',6.51592),
        S298 = (2.01203,'cal/mol/K','+|-',5.59062),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 313,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R_6R!H->C_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C ux r0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C ux r1 {1,S} {4,[S,D,T,B,Q]}
6   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.383725,-0.713504,-1.51362,-1.87153,-2.08295,-2.55768,-3.84323],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.789,'kcal/mol','+|-',4.17612),
        S298 = (4.56458,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 314,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R_6R!H->C_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C ux r0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]}
5   O ux r1 {1,S} {4,[S,D,T,B,Q]}
6   C ux {2,[S,D,T,B,Q]}
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
    index = 315,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C ux {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {1,S} {4,[S,D,T,B,Q]}
6   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.509182,-0.937882,-1.31699,-1.59971,-2.14254,-2.79582,-4.17576],'cal/mol/K','+|-',[3.14845,2.75707,2.39555,3.05465,4.95106,5.48478,4.53112]),
        H298 = (108.489,'kcal/mol','+|-',5.31226),
        S298 = (4.98363,'cal/mol/K','+|-',6.78389),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 316,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   ux r0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C   ux r1 {1,S} {4,[S,D,T,B,Q]}
6   O   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54409,-1.63172,-1.23815,-0.639187,0.0473482,-0.302543,-2.23159],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (105.891,'kcal/mol','+|-',4.17612),
        S298 = (1.77702,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C(OO)[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 317,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,D}
3   O   u0 r0 {2,D}
4   C   u0 {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C   u0 {1,S} {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.39789,-0.137819,-1.38127,-2.1615,-2.9896,-3.51254,-4.4084],'cal/mol/K','+|-',[3.17794,3.18279,3.34117,3.59354,3.86725,3.64854,3.21856]),
        H298 = (100.343,'kcal/mol','+|-',6.08296),
        S298 = (3.20496,'cal/mol/K','+|-',3.16404),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 318,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-4C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   u0 r0 {1,S} {3,D}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   u0 r1 {1,S} {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.50929,-0.265378,-1.76262,-2.76498,-3.77665,-4.15595,-4.62027],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.8284,'kcal/mol','+|-',4.17612),
        S298 = (3.24228,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)C[C]1C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 319,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.613438,-0.194063,-1.18031,-1.80917,-2.59974,-3.37097,-4.48435],'cal/mol/K','+|-',[2.45469,2.89816,3.80434,4.54479,5.17798,5.42549,5.05605]),
        H298 = (93.1291,'kcal/mol','+|-',16.4612),
        S298 = (-0.896337,'cal/mol/K','+|-',8.34579),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 320,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.861325,0.340624,-0.524035,-1.08118,-1.94509,-2.80782,-4.28628],'cal/mol/K','+|-',[2.525,2.30899,2.42063,2.6913,3.65133,4.2,5.47329]),
        H298 = (93.9895,'kcal/mol','+|-',6.93396),
        S298 = (-0.528839,'cal/mol/K','+|-',9.28378),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 321,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.01257,0.414687,-0.607727,-1.35754,-2.51708,-3.51818,-4.98371],'cal/mol/K','+|-',[2.6677,2.51656,2.63581,2.56826,2.58522,2.59714,4.7631]),
        H298 = (94.4075,'kcal/mol','+|-',7.36722),
        S298 = (1.18375,'cal/mol/K','+|-',4.42501),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 322,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing_Int-6R!H-2R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.122232,0.603157,0.31446,-0.382543,-1.35616,-2.281,-3.71454],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.9948,'kcal/mol','+|-',4.17612),
        S298 = (1.82914,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]C2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 323,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.474151,-0.838972,-2.02333,-2.50465,-3.31143,-4.07778,-4.06159],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.6659,'kcal/mol','+|-',4.17612),
        S298 = (3.79362,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1C(=O)C2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 324,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {7,S}
3   O   u0 r0 {2,D}
4   C   u0 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.85338,0.926792,-0.404207,-1.36789,-2.86556,-4.08397,-6.70679],'cal/mol/K','+|-',[3.24036,3.28615,3.16405,3.3419,3.37792,3.19687,6.69726]),
        H298 = (93.3035,'kcal/mol','+|-',6.77696),
        S298 = (-0.718085,'cal/mol/K','+|-',3.64312),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 325,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing_Ext-2R!H-R_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {7,S}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   C   ux {4,[S,D,T,B,Q]}
7   R!H u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.10336,1.24278,-0.366724,-1.75004,-3.28543,-4.2498,-8.79405],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (94.4786,'kcal/mol','+|-',4.17612),
        S298 = (-0.0785187,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1[CH]C(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 326,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing_Ext-2R!H-R_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {7,S}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S} {6,S}
5   C   u0 r1 {4,S}
6   O   u0 {4,S}
7   R!H u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.6034,0.610808,-0.44169,-0.985738,-2.44569,-3.91814,-4.61953],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (92.1284,'kcal/mol','+|-',4.17612),
        S298 = (-1.35765,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]C(OO)C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 327,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S} {6,S}
5   C   u0 r1 {4,S}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.105122,-0.02969,-0.105572,0.300612,0.914871,0.743958,-0.799121],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.8993,'kcal/mol','+|-',4.17612),
        S298 = (-9.09176,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[C]1CC(O)=CC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 328,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,S}
2   C   u0 {1,S} {3,D}
3   O   u0 r0 {2,D}
4   C   u0 {1,S} {5,S}
5   C   u0 {4,S}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5331,0.551978,-0.691372,-1.33123,-1.82586,-2.52371,-3.53041],'cal/mol/K','+|-',[5.02637,4.46931,4.33952,4.83245,4.52362,4.63105,5.55924]),
        H298 = (83.0492,'kcal/mol','+|-',18.8919),
        S298 = (-4.61208,'cal/mol/K','+|-',11.8198),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 329,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-1R-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,S}
2   C   u0 r1 {1,S} {3,D} {7,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {4,S}
6   R!H u0 r0 {1,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.91442,1.6686,0.359309,-0.0393006,-0.682233,-1.32754,-1.91388],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (76.7046,'kcal/mol','+|-',4.17612),
        S298 = (-8.63867,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=CC[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 330,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {7,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   C   u0 {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.280287,-3.42011,-6.41253,-8.22409,-9.68067,-10.519,-9.38207],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (116.101,'kcal/mol','+|-',4.17612),
        S298 = (3.96856,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)C[CH]C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 331,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {4,S} {6,D}
6   C   u0 r1 {5,D} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0707311,-0.983738,-1.47892,-1.46916,-1.36989,-1.73175,-2.89318],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (89.7303,'kcal/mol','+|-',4.17612),
        S298 = (-2.1083,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 332,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0405245,-1.87097,-3.32528,-4.10863,-4.96657,-5.77836,-6.69197],'cal/mol/K','+|-',[4.85232,4.51295,5.00766,5.08059,4.67866,4.81094,5.1516]),
        H298 = (100.501,'kcal/mol','+|-',19.6246),
        S298 = (1.14681,'cal/mol/K','+|-',3.88394),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 333,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.299836,-1.45662,-2.84472,-3.68633,-4.75365,-5.72196,-6.33862],'cal/mol/K','+|-',[4.72945,3.59313,3.84681,4.31246,4.66542,5.05493,4.73677]),
        H298 = (101.239,'kcal/mol','+|-',19.0548),
        S298 = (1.06711,'cal/mol/K','+|-',4.0495),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 334,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5   O   u0 r1 {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.15952,0.946463,-1.8956,-2.98527,-4.59025,-5.94737,-6.70593],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (114.426,'kcal/mol','+|-',4.17612),
        S298 = (-4.10355,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1OOC(O)[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 335,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.282009,-2.34517,-4.3211,-5.53158,-6.87399,-8.01006,-8.1522],'cal/mol/K','+|-',[5.6775,3.95486,3.3694,3.10005,2.41433,2.36077,4.19609]),
        H298 = (105.883,'kcal/mol','+|-',27.8861),
        S298 = (1.9044,'cal/mol/K','+|-',2.73007),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 336,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
6   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.57609,-4.06197,-5.53294,-6.56403,-7.23898,-8.08749,-6.19764],'cal/mol/K','+|-',[3.23057,3.67232,3.74176,3.56209,3.44346,3.43971,3.2128]),
        H298 = (91.1159,'kcal/mol','+|-',10.2032),
        S298 = (2.10058,'cal/mol/K','+|-',3.64306),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 337,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R_6R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]}
6   C   ux r1 {2,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8097,-4.72208,-6.24012,-7.14373,-7.72083,-8.56598,-6.39829],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.1743,'kcal/mol','+|-',4.17612),
        S298 = (2.7401,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 338,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {6,S}
3   O u0 r0 {2,D}
4   C u0 {1,S} {5,S}
5   O u0 {4,S}
6   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.18741,-1.20064,-3.51321,-4.84329,-6.63066,-7.95845,-9.45523],'cal/mol/K','+|-',[2.90832,2.92511,3.09542,3.07193,2.91682,2.97613,2.87252]),
        H298 = (115.728,'kcal/mol','+|-',7.88744),
        S298 = (1.77361,'cal/mol/K','+|-',3.4177),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 339,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R_N-6R!H->C_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,S}
2   C u0 r1 {1,S} {3,D} {6,S}
3   O u0 r0 {2,D}
4   C u0 {1,S} {5,S}
5   O u0 {4,S}
6   O u0 {2,S}
7   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.32243,-1.48639,-3.96857,-5.31914,-7.01035,-8.33048,-9.74087],'cal/mol/K','+|-',[3.62571,3.43795,3.29446,3.17894,3.19723,3.3256,3.34833]),
        H298 = (114.124,'kcal/mol','+|-',7.14717),
        S298 = (1.7891,'cal/mol/K','+|-',4.47462),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 340,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R_N-6R!H->C_Ext-1R-R_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,S}
2   C   u0 r1 {1,S} {3,D} {6,S}
3   O   u0 r0 {2,D}
4   C   u0 {1,S} {5,S}
5   O   u0 {4,S} {8,[S,D,T,B,Q]}
6   O   u0 r1 {2,S}
7   C   u0 {1,S}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.9495,-1.00948,-3.64195,-5.20421,-7.17705,-8.69442,-10.13],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (115.547,'kcal/mol','+|-',4.17612),
        S298 = (0.669818,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1OOC[C]1COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 341,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06989,-1.90248,-2.30765,-2.51525,-2.92811,-3.62094,-4.54172],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (95.6911,'kcal/mol','+|-',1.69706),
        S298 = (1.38837,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 342,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_N-2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8119,-6.42886,-8.61136,-8.75389,-7.30871,-6.39883,-10.5787],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.1324,'kcal/mol','+|-',4.17612),
        S298 = (2.02346,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 343,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.337303,-0.622662,-1.71062,-2.49845,-3.44094,-4.20782,-5.12765],'cal/mol/K','+|-',[2.30986,1.82968,3.18253,4.08655,3.99339,3.9463,2.56638]),
        H298 = (88.4157,'kcal/mol','+|-',15.9156),
        S298 = (1.08023,'cal/mol/K','+|-',4.71456),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 344,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   O ux {1,S}
5   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.396154,-0.0277842,-1.06841,-1.78683,-2.77522,-3.47785,-4.81739],'cal/mol/K','+|-',[2.35303,2.63891,2.33001,2.21517,2.17196,2.20078,2.76267]),
        H298 = (100.776,'kcal/mol','+|-',11.12),
        S298 = (2.14261,'cal/mol/K','+|-',6.76863),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 345,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-1R-R_2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   O u0 r1 {1,S}
5   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.37655,1.09558,-0.436315,-1.33865,-2.53973,-3.87856,-5.81139],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (109.253,'kcal/mol','+|-',4.17612),
        S298 = (-1.57968,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1O[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 346,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-1R-R_N-2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C ux r0 {1,S} {3,D}
3   O u0 r0 {2,D}
4   O ux {1,S}
5   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.401755,-0.348744,-1.24901,-1.91489,-2.8425,-3.36336,-4.53339],'cal/mol/K','+|-',[2.78421,2.42368,2.47258,2.41962,2.45442,2.42509,2.84748]),
        H298 = (99.5747,'kcal/mol','+|-',6.06283),
        S298 = (3.20612,'cal/mol/K','+|-',5.74967),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 347,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-1R-R_N-2R!H-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   O   ux r1 {1,S}
5   O   ux r1 {1,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.113371,-0.42954,-1.12134,-1.83922,-2.95497,-3.44587,-4.22081],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (99.0552,'kcal/mol','+|-',1.69706),
        S298 = (4.26257,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 348,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux {1,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.133689,-0.667748,-1.52805,-2.19493,-3.14292,-3.96213,-4.99116],'cal/mol/K','+|-',[2.81463,1.92151,2.19448,2.36532,2.32781,2.50428,2.20053]),
        H298 = (82.4346,'kcal/mol','+|-',6.58163),
        S298 = (-0.0758181,'cal/mol/K','+|-',3.74579),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 349,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux {1,S} {6,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.348064,-0.609539,-1.57207,-2.27069,-3.23353,-4.08605,-5.09561],'cal/mol/K','+|-',[3.06189,2.17688,2.50302,2.68556,2.63082,2.80875,2.46842]),
        H298 = (81.461,'kcal/mol','+|-',6.70978),
        S298 = (-0.0638519,'cal/mol/K','+|-',4.30697),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 350,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   O   ux {1,S} {6,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.443436,-0.711821,-1.80524,-2.52212,-3.45292,-4.34335,-5.32921],'cal/mol/K','+|-',[3.64921,2.55763,2.81577,3.02309,3.00038,3.17295,2.77027]),
        H298 = (79.6164,'kcal/mol','+|-',4.78798),
        S298 = (-0.868351,'cal/mol/K','+|-',3.81321),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 351,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   O   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O   ux r1 {4,[S,D,T,B,Q]}
7   R!H u0 r0 {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.932497,-0.163931,-1.44721,-2.09509,-2.5335,-3.43522,-5.03742],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (79.9808,'kcal/mol','+|-',4.17612),
        S298 = (-3.03629,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(CO)OO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 352,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   O   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   O   ux r1 {4,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.697281,-1.81844,-3.71184,-4.60182,-5.23959,-6.09338,-6.9299],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (79.1311,'kcal/mol','+|-',4.17612),
        S298 = (1.9808,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)OO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 353,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   O   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {2,[S,D,T,B,Q]} {7,S}
6   O   ux r1 {4,[S,D,T,B,Q]}
7   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.56914,-0.0593997,-2.42279,-3.4766,-4.79754,-5.96579,-6.45607],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.3324,'kcal/mol','+|-',4.17612),
        S298 = (-0.104457,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 354,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D} {5,S}
3   O   u0 r0 {2,D}
4   O   u0 {1,S} {6,S}
5   C   u0 {2,S} {7,D}
6   O   u0 {4,S}
7   R!H u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.376169,-0.73859,-1.18635,-1.77723,-2.82095,-3.63925,-4.63328],'cal/mol/K','+|-',[4.57349,3.49076,2.65989,2.44865,2.41921,2.58689,2.41733]),
        H298 = (79.1068,'kcal/mol','+|-',5.34477),
        S298 = (-1.28124,'cal/mol/K','+|-',2.45475),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 355,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {5,S}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S} {6,S}
5   C u0 r1 {2,S} {7,D}
6   O u0 r1 {4,S}
7   C u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.59314,0.546241,-0.597172,-1.50921,-3.00877,-4.13867,-4.81481],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (76.4839,'kcal/mol','+|-',4.17612),
        S298 = (-1.56313,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1OO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 356,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C_N-7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {5,S}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S} {6,S}
5   C u0 r1 {2,S} {7,D}
6   O u0 r1 {4,S}
7   O u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.16389,-1.25252,-1.42202,-1.88444,-2.74583,-3.43949,-4.56067],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (79.5399,'kcal/mol','+|-',1.69706),
        S298 = (-1.16848,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]OOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 357,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux {1,S}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.633978,-0.931012,-2.4234,-3.45457,-4.35851,-5.08071,-5.55135],'cal/mol/K','+|-',[2.91026,2.53757,5.58291,7.40108,7.25812,7.05424,4.23973]),
        H298 = (90.755,'kcal/mol','+|-',7.13746),
        S298 = (2.29649,'cal/mol/K','+|-',4.77728),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 358,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-4O-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux {1,S} {6,[S,D,T,B,Q]}
5   O ux {2,[S,D,T,B,Q]}
6   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.952939,-1.1461,-3.16124,-4.49077,-5.388,-6.09077,-6.12952],'cal/mol/K','+|-',[3.59091,3.19227,6.81774,8.95033,8.74626,8.47662,5.10569]),
        H298 = (89.6743,'kcal/mol','+|-',10.2801),
        S298 = (2.98352,'cal/mol/K','+|-',5.69417),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 359,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-4O-R_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux {1,S} {6,[S,D,T,B,Q]}
5   O ux {2,[S,D,T,B,Q]} {7,S}
6   C ux {4,[S,D,T,B,Q]}
7   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.07461,-2.0819,-5.91392,-8.2058,-9.00894,-9.60608,-8.12276],'cal/mol/K','+|-',[3.79691,3.56546,3.60368,3.60969,3.65226,3.43653,3.23292]),
        H298 = (94.8939,'kcal/mol','+|-',7.79488),
        S298 = (4.86206,'cal/mol/K','+|-',5.81332),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 360,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-4O-R_Ext-5BrClFINOPSSi-R_Int-7R!H-6R!H_Ext-7R!H-R_Ext-8R!H-R_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux r1 {1,S} {6,[S,D,T,B,Q]}
5   O ux r1 {2,[S,D,T,B,Q]} {7,S}
6   C ux r1 {4,[S,D,T,B,Q]}
7   C u0 r1 {5,S} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   O u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.81762,-1.49961,-5.30293,-7.59039,-8.3629,-9.13046,-7.88513],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.6925,'kcal/mol','+|-',4.17612),
        S298 = (3.13744,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]OCC(COO)(OO)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 361,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-4O-R_Ext-5BrClFINOPSSi-R_Int-7R!H-6R!H_Ext-7R!H-R_Ext-8R!H-R_N-8R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux r1 {1,S} {6,[S,D,T,B,Q]}
5   O ux r1 {2,[S,D,T,B,Q]} {7,S}
6   C ux r1 {4,[S,D,T,B,Q]}
7   C u0 r1 {5,S} {8,[S,D,T,B,Q]}
8   O ux {7,[S,D,T,B,Q]} {9,S}
9   O u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3316,-2.6642,-6.52491,-8.82121,-9.65498,-10.0817,-8.36039],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.0953,'kcal/mol','+|-',4.17612),
        S298 = (6.58669,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(OO)CO[CH]C(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 362,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   C   ux {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0546302,-1.12737,-1.89,-2.50579,-3.53128,-4.11672,-5.01221],'cal/mol/K','+|-',[2.34732,1.44535,1.80886,2.35276,3.42228,3.80903,2.96516]),
        H298 = (113.692,'kcal/mol','+|-',5.86934),
        S298 = (1.5848,'cal/mol/K','+|-',3.81239),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 363,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   C   ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.172951,-1.05404,-1.90936,-2.60763,-3.78358,-4.44573,-5.29868],'cal/mol/K','+|-',[2.74188,1.62043,2.14702,2.85797,4.13011,4.5231,3.45852]),
        H298 = (113.363,'kcal/mol','+|-',3.73112),
        S298 = (1.23899,'cal/mol/K','+|-',3.09698),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 364,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   C   ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.492061,-1.07909,-2.07943,-2.84967,-4.16048,-4.83298,-5.64935],'cal/mol/K','+|-',[3.11869,1.95564,2.54024,3.39938,4.91243,5.42085,4.04868]),
        H298 = (112.594,'kcal/mol','+|-',4.03818),
        S298 = (1.24009,'cal/mol/K','+|-',3.85951),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 365,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D} {7,[S,D,T,B,Q]}
4   C   u0 r1 {1,D} {5,S}
5   R!H u0 r1 {4,S} {6,S}
6   R!H ux {5,S}
7   R!H ux {3,[S,D,T,B,Q]}
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
    index = 366,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   C   ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.550222,-1.01015,-1.53813,-2.06521,-2.92134,-3.56029,-4.52754],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (112.338,'kcal/mol','+|-',1.69706),
        S298 = (0.952538,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[C]=CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 367,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,D}
2   C   u0 {1,S} {3,D}
3   R!H u0 r0 {2,D}
4   C   u0 {1,D} {5,S}
5   O   u0 {4,S} {6,S}
6   O   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.63808,-0.997538,-2.61837,-3.83147,-5.77757,-6.62472,-7.10725],'cal/mol/K','+|-',[3.38943,3.18867,3.89831,5.13543,7.20465,8.11107,5.39116]),
        H298 = (114.217,'kcal/mol','+|-',6.39979),
        S298 = (2.59228,'cal/mol/K','+|-',4.66561),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 368,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_N-5R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,D}
2   C   u0 r1 {1,S} {3,D} {7,[S,D,T,B,Q]}
3   R!H u0 r0 {2,D}
4   C   u0 r1 {1,D} {5,S}
5   O   u0 r1 {4,S} {6,S}
6   O   u0 r1 {5,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.06939,-1.14229,-3.42435,-5.26206,-8.06632,-9.26549,-8.65097],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (115.088,'kcal/mol','+|-',4.17612),
        S298 = (3.80512,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OOC=[C]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 369,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[B,D,T,Q]}
2   C   ux r1 {1,S} {3,D}
3   R!H u0 r0 {2,D}
4   C   ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   R!H ux r1 {4,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   R!H u0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.52909,-0.998943,-1.53521,-2.07515,-2.95441,-3.59377,-4.5272],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (114.512,'kcal/mol','+|-',1.69706),
        S298 = (1.23659,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[C]=CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 370,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,D}
2   C u0 r1 {1,S} {3,D}
3   C u0 r0 {2,D}
4   C u0 r1 {1,D} {5,S}
5   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.541947,-1.05571,-1.62114,-2.13205,-2.93809,-3.56003,-4.54021],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (112.832,'kcal/mol','+|-',1.69706),
        S298 = (0.999217,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[C]=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 371,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,D}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r0 {2,D}
4   C                      u0 r1 {1,D} {5,S}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.656988,-1.89317,-2.40726,-2.6254,-2.9958,-2.87645,-3.90047],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (123.875,'kcal/mol','+|-',4.17612),
        S298 = (5.81522,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[C]=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 372,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0501271,-1.05673,-1.98986,-2.60903,-3.34681,-3.93713,-5.24519],'cal/mol/K','+|-',[2.60815,3.19586,3.75159,3.87468,3.61925,3.5338,4.42945]),
        H298 = (100.794,'kcal/mol','+|-',24.4306),
        S298 = (1.63159,'cal/mol/K','+|-',6.39405),
    ),
    shortDesc = """Radical correction fitted to 199 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 373,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.433581,-1.19197,-1.88161,-2.34231,-2.99813,-3.52406,-4.43164],'cal/mol/K','+|-',[1.23433,1.21165,1.32678,1.31742,1.28138,1.2341,1.41167]),
        H298 = (114.515,'kcal/mol','+|-',12.2379),
        S298 = (1.26437,'cal/mol/K','+|-',9.10702),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 374,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.371115,-1.13517,-1.8321,-2.28865,-2.94495,-3.47444,-4.39139],'cal/mol/K','+|-',[1.07399,0.982025,1.17731,1.22742,1.26254,1.24908,1.4823]),
        H298 = (115.569,'kcal/mol','+|-',9.32237),
        S298 = (1.2583,'cal/mol/K','+|-',9.74792),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 375,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.472758,-1.11527,-1.73972,-2.18448,-2.84478,-3.40151,-4.3963],'cal/mol/K','+|-',[1.10662,0.979225,0.967239,0.958209,1.02375,1.22196,1.42005]),
        H298 = (114.613,'kcal/mol','+|-',8.96929),
        S298 = (2.26193,'cal/mol/K','+|-',10.3357),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 376,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Int-4C-1R",
    group = 
"""
1 * C u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C ux {1,D} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.534087,-1.1515,-1.72496,-2.19969,-2.90062,-3.41687,-4.27971],'cal/mol/K','+|-',[1.68657,1.54581,1.56488,1.54644,1.61765,1.91208,2.37348]),
        H298 = (111.871,'kcal/mol','+|-',4.16789),
        S298 = (4.04609,'cal/mol/K','+|-',18.7145),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 377,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Int-4C-1R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C   ux {1,D} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   R!H u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.412329,-1.17535,-1.79544,-2.23027,-2.76824,-3.1319,-3.84121],'cal/mol/K','+|-',[2.7345,2.39078,2.43299,2.40719,2.55366,3.15644,4.08435]),
        H298 = (112.476,'kcal/mol','+|-',10.3598),
        S298 = (8.27284,'cal/mol/K','+|-',34.8144),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 378,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Int-4C-1R_Ext-3R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C ux r1 {1,D} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C ux r1 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   C u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.258337,-1.15538,-2.02421,-2.37336,-2.31455,-2.09081,-2.16853],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (118.466,'kcal/mol','+|-',4.17612),
        S298 = (25.8152,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C1C=[C]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 379,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Int-4C-1R_Ext-3R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C                      ux r1 {1,D} {3,S}
3   C                      u0 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C                      ux r1 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.680595,-1.18333,-1.70393,-2.17303,-2.94972,-3.54834,-4.51028],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (111.486,'kcal/mol','+|-',1.69706),
        S298 = (1.25588,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1C=[C]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 380,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Int-4C-1R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,D} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.71,-1.23732,-1.77078,-2.2494,-3.048,-3.66438,-4.61619],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (111.474,'kcal/mol','+|-',1.69706),
        S298 = (1.1756,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=[C]CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 381,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.326215,-1.01726,-1.68587,-2.07952,-2.71643,-3.28082,-4.39294],'cal/mol/K','+|-',[1.60511,1.57128,1.59581,1.58959,1.65769,1.8075,1.79027]),
        H298 = (112.159,'kcal/mol','+|-',6.95984),
        S298 = (1.01696,'cal/mol/K','+|-',2.44723),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 382,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux r1 {1,D} {3,[S,T,Q,B]}
3   R!H ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.231261,-1.01079,-1.63325,-2.02327,-2.72966,-3.37378,-4.53761],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (109.466,'kcal/mol','+|-',1.69706),
        S298 = (1.23246,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=[C]CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 383,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux r1 {1,D} {3,[S,T,Q,B]}
3   R!H ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.303809,-0.880208,-1.45009,-1.95597,-2.79826,-3.44997,-4.48411],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (110.676,'kcal/mol','+|-',1.69706),
        S298 = (1.32678,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC=[C]CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 384,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,D} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,D} {3,[S,T,Q,B]}
3   R!H ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.870355,-1.38058,-1.94923,-1.86503,-2.00675,-2.16945,-3.32079],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (114.433,'kcal/mol','+|-',4.17612),
        S298 = (-1.20326,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[C]1=COC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 385,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,D}
2   C u0 {1,D} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   C u0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.569334,-1.18528,-1.81747,-2.28618,-2.92697,-3.52088,-4.53224],'cal/mol/K','+|-',[1.83364,1.73358,1.66703,1.64813,1.64449,1.65419,1.63359]),
        H298 = (120.096,'kcal/mol','+|-',2.05194),
        S298 = (1.65085,'cal/mol/K','+|-',1.74794),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 386,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C u1 r1 {2,D}
2   C u0 {1,D} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]} {6,S}
4   C u0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]}
6   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.793418,-1.31464,-1.82745,-2.28057,-2.98269,-3.59708,-4.52375],'cal/mol/K','+|-',[2.04597,2.06777,2.05481,2.0245,2.00021,2.00001,2.00054]),
        H298 = (119.921,'kcal/mol','+|-',2.4005),
        S298 = (1.81666,'cal/mol/K','+|-',2.02915),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 387,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-3R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   u0 r1 {1,D} {3,S} {7,[S,D,T,B,Q]}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]} {6,S}
4   C   u0 r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   u0 r1 {4,[S,D,T,B,Q]}
6   O   u0 r0 {3,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.945903,-1.50027,-1.99414,-2.39158,-2.97246,-3.59507,-4.54017],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (119.938,'kcal/mol','+|-',1.69706),
        S298 = (1.93783,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=[C]OC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 388,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0390805,-1.20019,-2.13389,-2.62897,-3.27218,-3.71269,-4.37533],'cal/mol/K','+|-',[1.75173,1.94951,2.32719,2.43255,2.4352,2.10942,2.46085]),
        H298 = (120.451,'kcal/mol','+|-',3.73714),
        S298 = (-2.02023,'cal/mol/K','+|-',3.29904),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 389,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,D}
2   C ux r1 {1,D} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.332765,-1.30164,-1.86896,-2.14051,-2.70578,-3.08111,-2.72812],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (122.646,'kcal/mol','+|-',4.17612),
        S298 = (-3.22109,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC1=[C]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 390,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,D}
2   C ux {1,D} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00610171,-1.18458,-2.17465,-2.70412,-3.35932,-3.80985,-4.62875],'cal/mol/K','+|-',[1.86704,2.10932,2.52223,2.61055,2.59877,2.20816,2.15957]),
        H298 = (120.233,'kcal/mol','+|-',3.56292),
        S298 = (-1.83548,'cal/mol/K','+|-',3.42629),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 391,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   u0 r1 {1,D} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   u0 r1 {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.439881,-0.828181,-1.60876,-2.04834,-2.70008,-3.23573,-4.12026],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (117.735,'kcal/mol','+|-',4.17612),
        S298 = (-2.61734,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=[C]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 392,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0459403,-1.49083,-2.75986,-3.31895,-3.90444,-4.19215,-4.83006],'cal/mol/K','+|-',[2.65377,2.99581,3.3052,3.40726,3.50751,3.04901,3.1313]),
        H298 = (120.255,'kcal/mol','+|-',5.11146),
        S298 = (-2.20432,'cal/mol/K','+|-',4.80604),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 393,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,D}
2   C u0 {1,D} {3,S}
3   O u0 {2,S} {4,S}
4   O u0 {3,S} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.190447,-1.92941,-3.35227,-3.94933,-4.58493,-4.6601,-5.25404],'cal/mol/K','+|-',[3.20164,3.16228,3.17689,3.21692,3.18719,3.16294,3.4587]),
        H298 = (119.785,'kcal/mol','+|-',5.9435),
        S298 = (-1.1548,'cal/mol/K','+|-',4.05297),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 394,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   u0 r1 {1,D} {3,S}
3   O   u0 r1 {2,S} {4,S}
4   O   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.367395,-1.93127,-3.45988,-4.15807,-4.72555,-4.63719,-5.74934],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (120.021,'kcal/mol','+|-',4.17612),
        S298 = (-2.05108,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)[C]=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 395,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,D}
2   C                      ux r1 {1,D} {3,[S,T,Q,B]}
3   O                      ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O                      ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C                      ux r1 {4,[S,D,T,B,Q]} {6,S}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.243073,-0.613677,-1.57505,-2.05821,-2.54345,-3.25626,-3.9821],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (121.195,'kcal/mol','+|-',4.17612),
        S298 = (-4.30338,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[C]=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 396,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,D}
2   C u0 {1,D} {3,S}
3   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.463312,-1.20607,-1.92079,-2.4887,-3.25472,-3.83079,-4.72524],'cal/mol/K','+|-',[2.78221,3.42328,3.59102,3.36891,3.01604,2.78626,2.54334]),
        H298 = (108.835,'kcal/mol','+|-',5.25951),
        S298 = (1.64972,'cal/mol/K','+|-',3.42891),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 397,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C   u0 r1 {1,D} {3,S}
3   C   u0 {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18229,-2.44372,-3.27427,-3.68768,-4.1836,-4.55376,-5.1639],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (106.276,'kcal/mol','+|-',4.17612),
        S298 = (2.89133,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=[C]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 398,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,D}
2   C ux r1 {1,D} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.32844,-2.96034,-3.32858,-3.547,-3.80151,-4.03819,-4.69236],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.3895,'kcal/mol','+|-',4.17612),
        S298 = (0.109847,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[C]1=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 399,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.110694,-1.03979,-2.00341,-2.64242,-3.39046,-3.98885,-5.34706],'cal/mol/K','+|-',[2.7223,3.37355,3.96196,4.08943,3.81451,3.72137,4.64167]),
        H298 = (98.9357,'kcal/mol','+|-',23.2945),
        S298 = (1.67757,'cal/mol/K','+|-',6.01485),
    ),
    shortDesc = """Radical correction fitted to 179 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 400,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.281993,-0.968994,-2.01131,-2.63498,-3.35644,-3.95393,-5.46423],'cal/mol/K','+|-',[3.03033,3.50881,4.06229,4.06824,3.58832,3.34484,4.69698]),
        H298 = (101.582,'kcal/mol','+|-',8.48257),
        S298 = (1.36821,'cal/mol/K','+|-',6.76011),
    ),
    shortDesc = """Radical correction fitted to 100 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 401,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.340051,-0.971999,-1.63264,-2.13973,-2.88382,-3.47227,-4.39749],'cal/mol/K','+|-',[2.07814,2.13141,2.29104,2.28793,2.23502,2.28118,2.34444]),
        H298 = (104.805,'kcal/mol','+|-',4.88585),
        S298 = (1.27007,'cal/mol/K','+|-',3.53784),
    ),
    shortDesc = """Radical correction fitted to 23 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 402,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_4R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H u0 r1 {1,S} {2,[S,T,Q,B]}
4   R!H ux r1 {2,[S,D,T,B,Q]}
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
    index = 403,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.336038,-0.978151,-1.62473,-2.13154,-2.87962,-3.45679,-4.40916],'cal/mol/K','+|-',[2.09795,2.15062,2.31078,2.3074,2.25639,2.29198,2.36123]),
        H298 = (104.759,'kcal/mol','+|-',4.79072),
        S298 = (1.23015,'cal/mol/K','+|-',3.52185),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 404,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.558872,-1.21517,-1.77954,-2.24174,-3.01332,-3.61243,-4.55853],'cal/mol/K','+|-',[1.59883,1.69155,1.74084,1.72748,1.67048,1.57708,1.36535]),
        H298 = (107.468,'kcal/mol','+|-',6.01714),
        S298 = (2.48134,'cal/mol/K','+|-',3.96501),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 405,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,S}
2   C   u0 {1,S} {3,S} {4,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {2,S}
4   R!H ux r0 {2,[S,D,T,B,Q]}
5   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.706614,-1.26332,-1.73123,-2.16469,-2.91069,-3.51046,-4.49618],'cal/mol/K','+|-',[2.0632,2.03095,2.05131,2.07979,2.09627,2.0696,2.0029]),
        H298 = (104.456,'kcal/mol','+|-',3.82338),
        S298 = (0.610928,'cal/mol/K','+|-',3.35834),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 406,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C_Ext-1R-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,S}
2   C   u0 r1 {1,S} {3,S} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   ux r1 {1,[S,D,T,B,Q]} {2,S}
4   R!H ux r0 {2,[S,D,T,B,Q]}
5   R!H u0 r0 {1,S}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.527452,-1.13845,-1.57003,-1.96297,-2.68866,-3.3223,-4.45812],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (105.508,'kcal/mol','+|-',1.69706),
        S298 = (1.56477,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 407,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
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
    index = 408,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0632128,-0.457259,-1.08836,-1.65785,-2.58697,-3.28774,-4.37517],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (110.34,'kcal/mol','+|-',1.69706),
        S298 = (3.24501,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C(O)C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 409,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.270461,-1.08111,-1.63223,-2.02864,-2.74196,-3.35213,-4.41893],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (109.449,'kcal/mol','+|-',1.69706),
        S298 = (3.58917,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 410,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.268101,-0.905889,-1.57754,-2.09794,-2.83886,-3.40933,-4.36362],'cal/mol/K','+|-',[2.34279,2.38637,2.57906,2.58127,2.52887,2.58409,2.69613]),
        H298 = (103.921,'kcal/mol','+|-',2.98335),
        S298 = (0.848689,'cal/mol/K','+|-',3.17836),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 411,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.381559,-1.28137,-2.1149,-2.64189,-3.24248,-3.6486,-4.23371],'cal/mol/K','+|-',[3.4329,3.36416,3.44697,3.3405,3.31926,3.56911,3.39779]),
        H298 = (103.307,'kcal/mol','+|-',3.68522),
        S298 = (0.67591,'cal/mol/K','+|-',4.31474),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 412,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O u0 {1,S} {2,[S,T,Q,B]}
4   O ux r0 {2,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.15613,-1.61836,-1.99802,-2.1979,-2.43888,-2.7005,-3.41873],'cal/mol/K','+|-',[3.60989,3.96911,3.58065,2.6739,1.77127,2.59681,3.60809]),
        H298 = (102.364,'kcal/mol','+|-',2.34975),
        S298 = (-0.081956,'cal/mol/K','+|-',2.10606),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 413,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_5R!H->C_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   u0 r1 {1,S} {2,[S,T,Q,B]}
4   O   ux r0 {2,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.61477,-4.30242,-4.34027,-3.70875,-2.1489,-1.18664,-0.933265],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.197,'kcal/mol','+|-',1.69706),
        S298 = (-0.252313,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC[C]1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 414,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_5R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {5,S}
2   C   u0 {1,S} {3,S} {4,S}
3   O   u0 {1,S} {2,S}
4   O   u0 r0 {2,S} {6,S}
5   C   u0 {1,S}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.524585,-1.06491,-1.57786,-2.05509,-2.86959,-3.47598,-4.30824],'cal/mol/K','+|-',[2.00158,2.01119,2.02063,2.0373,2.07017,2.06074,2.00467]),
        H298 = (102.986,'kcal/mol','+|-',2.41673),
        S298 = (0.517071,'cal/mol/K','+|-',2.02364),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 415,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_5R!H->C_Ext-4R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S} {5,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r1 {1,S} {2,S}
4   O u0 r0 {2,S} {6,S}
5   C u0 r0 {1,S}
6   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.496479,-0.990016,-1.47603,-1.9179,-2.68065,-3.30039,-4.35659],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.086,'kcal/mol','+|-',1.69706),
        S298 = (0.408039,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 416,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_5R!H->C_Ext-4R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {3,S} {5,S}
2   C                      u0 r1 {1,S} {3,S} {4,S}
3   O                      u0 r1 {1,S} {2,S}
4   O                      u0 r0 {2,S} {6,S}
5   C                      u0 r0 {1,S}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.552691,-1.1398,-1.67969,-2.19228,-3.05853,-3.65157,-4.25988],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.886,'kcal/mol','+|-',1.69706),
        S298 = (0.626104,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 417,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
5   O   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.651207,-0.832039,-2.27075,-3.23387,-4.31395,-4.91275,-5.32036],'cal/mol/K','+|-',[2.61651,3.23113,4.2891,4.61634,4.30467,3.68227,2.22422]),
        H298 = (104.564,'kcal/mol','+|-',4.37003),
        S298 = (1.6864,'cal/mol/K','+|-',6.38078),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 418,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_N-5R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   u0 r1 {1,S} {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   ux {1,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.685186,-2.14048,-4.51629,-5.72647,-6.57826,-6.70981,-5.89496],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (106.799,'kcal/mol','+|-',1.69706),
        S298 = (5.19163,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OCC1O[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 419,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_N-5R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]}
5   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.387543,-0.989828,-1.53601,-2.02215,-2.83462,-3.46555,-4.46517],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.189,'kcal/mol','+|-',1.69706),
        S298 = (-0.611126,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1O[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 420,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_N-5R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O ux r0 {2,[S,D,T,B,Q]}
5   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.65598,0.634195,-0.759943,-1.95299,-3.52895,-4.56288,-5.60095],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.703,'kcal/mol','+|-',1.69706),
        S298 = (0.478685,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 421,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.183089,-0.743991,-1.40861,-1.95717,-2.77123,-3.42188,-4.6021],'cal/mol/K','+|-',[1.98743,1.78282,1.71108,1.87298,2.15759,2.26995,3.21144]),
        H298 = (104.866,'kcal/mol','+|-',2.29647),
        S298 = (1.27838,'cal/mol/K','+|-',2.53272),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 422,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,S}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.387248,-1.04317,-1.3893,-1.64528,-2.1703,-2.68253,-3.81528],'cal/mol/K','+|-',[2.00281,2.63989,3.13206,3.25773,3.29095,3.1425,2.53399]),
        H298 = (104.273,'kcal/mol','+|-',2.87525),
        S298 = (0.892728,'cal/mol/K','+|-',4.37115),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 423,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_Ext-2R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,S}
3   O   ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H u0 r0 {2,S}
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
    index = 424,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_Ext-2R!H-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,S}
3   O   ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.424774,-1.65237,-2.24149,-2.55445,-3.09431,-3.5395,-4.3654],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (104.833,'kcal/mol','+|-',1.69706),
        S298 = (2.26691,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(OO)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 425,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S}
2   C   u0 {1,S} {3,S} {4,S}
3   O   u0 {1,S} {2,S}
4   C   u0 r0 {2,S} {5,S}
5   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.328333,-0.415724,-1.38936,-2.21146,-3.33648,-4.02553,-4.75123],'cal/mol/K','+|-',[3.22687,2.64287,2.03604,2.07488,2.39254,2.48802,2.11683]),
        H298 = (105.195,'kcal/mol','+|-',3.03057),
        S298 = (1.73587,'cal/mol/K','+|-',2.22648),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 426,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_4R!H->C_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r1 {1,S} {2,S}
4   C u0 r0 {2,S} {5,S}
5   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.56698,-1.02654,-1.5242,-2.01617,-2.87223,-3.50229,-4.50603],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (104.541,'kcal/mol','+|-',1.69706),
        S298 = (1.38996,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 427,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r1 {1,S} {2,S}
4   C u0 r0 {2,S} {5,S}
5   O u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.22365,0.195092,-1.25453,-2.40676,-3.80074,-4.54877,-4.99643],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (105.849,'kcal/mol','+|-',1.69706),
        S298 = (2.08178,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OCC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 428,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S}
2   C   u0 {1,S} {3,S} {4,S}
3   O   u0 {1,S} {2,S}
4   O   u0 r0 {2,S} {5,S}
5   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.622037,-0.785547,-1.4637,-2.03947,-2.82221,-3.61574,-5.5131],'cal/mol/K','+|-',[2.74548,2.39065,2.54981,2.65264,2.4236,2.65151,7.22606]),
        H298 = (105.32,'kcal/mol','+|-',4.19646),
        S298 = (1.17574,'cal/mol/K','+|-',3.29481),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 429,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_N-4R!H->C_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r1 {1,S} {2,S}
4   O u0 r0 {2,S} {5,S}
5   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.349231,-0.779376,-1.28444,-1.80717,-2.74151,-3.38395,-4.13541],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (105.041,'kcal/mol','+|-',1.69706),
        S298 = (0.717637,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 430,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_N-4R!H->C_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r1 {1,S} {2,S}
4   O u0 r0 {2,S} {5,S}
5   O u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.30405,-0.800975,-1.91184,-2.62024,-3.02395,-4.19519,-8.95732],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (107.006,'kcal/mol','+|-',4.17612),
        S298 = (2.32099,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 431,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_4R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {3,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 {1,S} {2,S}
4   O u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00829234,0.0338857,-0.191619,-0.627553,-1.56591,-2.42418,-4.01643],'cal/mol/K','+|-',[2.26491,2.00335,2.00472,2.00097,2.00945,2.00829,2.00023]),
        H298 = (102.974,'kcal/mol','+|-',2.40825),
        S298 = (-0.392674,'cal/mol/K','+|-',2.07786),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 432,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S}
2   C   u0 r1 {1,S} {3,S} {4,S} {5,[S,D,T,B,Q]}
3   O   u0 r1 {1,S} {2,S}
4   O   u0 r0 {2,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.384097,-0.00705781,-0.143013,-0.649531,-1.63472,-2.48862,-4.00564],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.903,'kcal/mol','+|-',1.69706),
        S298 = (-0.193462,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(O)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 433,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {3,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 {1,S} {2,S}
4   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.360341,-0.968619,-1.53877,-2.0446,-2.88173,-3.52317,-4.52156],'cal/mol/K','+|-',[2.00246,2.0122,2.01315,2.01206,2.00772,2.00351,2.00011]),
        H298 = (104.578,'kcal/mol','+|-',2.43571),
        S298 = (1.53462,'cal/mol/K','+|-',2.04837),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 434,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_N-4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S}
2   C   u0 r1 {1,S} {3,S} {4,S} {5,[S,D,T,B,Q]}
3   O   u0 r1 {1,S} {2,S}
4   C   u0 r0 {2,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.395434,-1.04683,-1.61998,-2.12238,-2.94391,-3.56506,-4.52883],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (104.432,'kcal/mol','+|-',1.69706),
        S298 = (1.69108,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 435,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.176601,-2.12269,-3.87458,-4.81931,-5.20915,-5.5948,-9.12222],'cal/mol/K','+|-',[3.82601,5.22483,6.07742,6.37037,6.12526,5.88115,5.11442]),
        H298 = (97.4564,'kcal/mol','+|-',6.69729),
        S298 = (3.21192,'cal/mol/K','+|-',11.6835),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 436,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.316274,-2.06306,-3.68158,-4.55428,-4.94948,-5.32581,-9.05315],'cal/mol/K','+|-',[3.77449,5.52733,6.28508,6.39826,6.02862,5.67054,5.38324]),
        H298 = (96.7355,'kcal/mol','+|-',4.96017),
        S298 = (2.8223,'cal/mol/K','+|-',11.9855),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 437,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0416698,-1.49074,-2.96853,-3.82527,-4.39068,-4.95235,-8.78556],'cal/mol/K','+|-',[3.34572,4.45039,4.87154,5.07223,5.55192,5.74102,4.49518]),
        H298 = (97.0177,'kcal/mol','+|-',5.00449),
        S298 = (1.62661,'cal/mol/K','+|-',11.8908),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 438,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Int-8R!H-3R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S} {8,[S,D,T,B,Q]}
4   R!H u0 {2,S}
5   R!H u0 {2,S} {8,S}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H u0 {3,[S,D,T,B,Q]} {5,S}
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
    index = 439,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
8   O   ux {5,[S,D,T,B,Q]}
9   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.158247,-1.05267,-2.20204,-2.96287,-3.36654,-3.89686,-9.13112],'cal/mol/K','+|-',[4.30015,5.81331,6.25235,6.48879,7.02736,7.11329,5.60942]),
        H298 = (95.4548,'kcal/mol','+|-',5.41075),
        S298 = (-1.72848,'cal/mol/K','+|-',12.7137),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 440,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {9,S}
2    C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3    R!H ux {2,[S,T,Q,B]}
4    R!H ux {2,[S,D,T,B,Q]}
5    R!H ux {2,[S,D,T,B,Q]} {8,S}
6    C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    O   ux {6,[S,D,T,B,Q]}
8    O   ux {5,S}
9    C   u0 {1,S} {10,[S,D,T,B,Q]}
10   O   ux {9,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.775223,0.556046,-0.56675,-1.45027,-2.01331,-2.7058,-8.51075],'cal/mol/K','+|-',[5.01381,5.65624,6.17419,6.74569,8.06336,8.5592,7.16172]),
        H298 = (94.977,'kcal/mol','+|-',7.0736),
        S298 = (-5.91167,'cal/mol/K','+|-',9.20306),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 441,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R_5R!H-inRing",
    group = 
"""
1  * C     u1 r1 {2,S} {6,[S,D,T,B,Q]} {9,S}
2    C     ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3    [C,O] ux {2,[S,T,Q,B]}
4    [C,O] ux {2,[S,D,T,B,Q]}
5    C     ux r1 {2,[S,D,T,B,Q]} {8,S}
6    C     ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    O     ux {6,[S,D,T,B,Q]}
8    O     ux {5,S}
9    C     u0 {1,S} {10,[S,D,T,B,Q]}
10   O     ux {9,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.63056,2.10893,0.166519,-1.41563,-2.92456,-4.10942,-10.0135],'cal/mol/K','+|-',[3.54941,5.52444,5.65565,4.71352,3.71071,3.16349,3.70176]),
        H298 = (96.8872,'kcal/mol','+|-',6.22205),
        S298 = (-3.46151,'cal/mol/K','+|-',6.98593),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 442,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R_5R!H-inRing_Ext-3R!H-R",
    group = 
"""
1  * C     u1 r1 {2,S} {6,[S,D,T,B,Q]} {9,S}
2    C     ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3    [C,O] ux r0 {2,[S,T,Q,B]} {11,[S,D,T,B,Q]}
4    [C,O] ux r0 {2,[S,D,T,B,Q]}
5    C     ux r1 {2,[S,D,T,B,Q]} {8,S}
6    C     ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    O     ux r1 {6,[S,D,T,B,Q]}
8    O     ux r1 {5,S}
9    C     u0 {1,S} {10,[S,D,T,B,Q]}
10   O     ux {9,[S,D,T,B,Q]}
11   R!H   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.20046,3.71047,1.82432,-0.179845,-2.23814,-4.14033,-10.6938],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.1949,'kcal/mol','+|-',4.17612),
        S298 = (-5.66387,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(OO)COOC[C]1COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 443,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R_N-5R!H-inRing",
    group = 
"""
1  * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {9,S}
2    C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3    C   ux {2,[S,T,Q,B]}
4    R!H ux {2,[S,D,T,B,Q]}
5    R!H ux r0 {2,[S,D,T,B,Q]} {8,S}
6    C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    O   ux {6,[S,D,T,B,Q]}
8    O   ux {5,S}
9    C   u0 {1,S} {10,[S,D,T,B,Q]}
10   O   ux {9,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08011,-0.99684,-1.30002,-1.48492,-1.10207,-1.30218,-7.00803],'cal/mol/K','+|-',[3.56935,5.64592,8.87539,10.9214,13.1529,13.537,10.4421]),
        H298 = (93.0669,'kcal/mol','+|-',8.39367),
        S298 = (-8.36184,'cal/mol/K','+|-',10.688),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 444,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R_N-5R!H-inRing_2R!H-inRing",
    group = 
"""
1  * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {9,S}
2    C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3    C   ux {2,[S,T,Q,B]}
4    R!H ux {2,[S,D,T,B,Q]}
5    R!H ux r0 {2,[S,D,T,B,Q]} {8,S}
6    C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    O   ux r1 {6,[S,D,T,B,Q]}
8    O   ux r0 {5,S}
9    C   u0 {1,S} {10,[S,D,T,B,Q]}
10   O   ux {9,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.66537,0.656808,1.63197,2.21096,3.41177,3.35144,-3.48956],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.9581,'kcal/mol','+|-',4.17612),
        S298 = (-11.9714,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(CO)OOC[C]1COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 445,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R_N-5R!H-inRing_N-2R!H-inRing",
    group = 
"""
1  * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {9,S}
2    C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3    C   ux {2,[S,T,Q,B]}
4    C   ux {2,[S,D,T,B,Q]}
5    R!H ux r0 {2,[S,D,T,B,Q]} {8,S}
6    C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    O   ux r1 {6,[S,D,T,B,Q]}
8    O   ux r0 {5,S}
9    C   u0 r1 {1,S} {10,[S,D,T,B,Q]}
10   O   ux r1 {9,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.494847,-2.65049,-4.23201,-5.1808,-5.61591,-5.9558,-10.5265],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.1756,'kcal/mol','+|-',4.17612),
        S298 = (-4.75226,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(OO)[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 446,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-3R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
2    C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3    C   ux {2,[S,T,Q,B]} {10,[S,D,T,B,Q]}
4    C   ux {2,[S,D,T,B,Q]}
5    R!H ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6    C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    O   ux {6,[S,D,T,B,Q]}
8    O   ux {5,[S,D,T,B,Q]}
9    C   ux {1,[S,D,T,B,Q]}
10   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.48615,-3.68141,-5.18241,-5.984,-6.22278,-6.61093,-10.8357],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.4927,'kcal/mol','+|-',4.17612),
        S298 = (5.89114,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 447,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
8   O   ux {5,[S,D,T,B,Q]}
9   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04161,-2.04575,-2.64212,-2.80041,-2.90919,-3.29787,-8.20651],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (94.8551,'kcal/mol','+|-',4.17612),
        S298 = (0.728069,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 448,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_N-3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
8   O   ux {5,[S,D,T,B,Q]}
9   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.68086,-3.86569,-5.32273,-6.15461,-6.38059,-6.54604,-10.8326],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.9275,'kcal/mol','+|-',4.17612),
        S298 = (4.92814,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)OOC[C]1COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 449,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux r1 {6,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.567201,-1.85471,-3.60277,-4.53185,-5.44636,-6.80837,-6.62705],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.9092,'kcal/mol','+|-',4.17612),
        S298 = (5.99535,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)OC2OOC[C]21 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 450,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
9   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.181102,-1.684,-3.36937,-4.42862,-5.20796,-5.40224,-9.75801],'cal/mol/K','+|-',[3.17545,3.20934,3.51442,3.7779,3.74523,3.60683,3.28449]),
        H298 = (98.1938,'kcal/mol','+|-',6.04838),
        S298 = (4.31364,'cal/mol/K','+|-',3.55098),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 451,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-5R!H-R_3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux r1 {6,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
9   R!H ux {5,[S,D,T,B,Q]}
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
    index = 452,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-5R!H-R_N-3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux r1 {6,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
9   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.283238,-1.8776,-3.91148,-5.15942,-5.91743,-6.01555,-10.0718],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.7325,'kcal/mol','+|-',4.17612),
        S298 = (4.88476,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OOC[CH]C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 453,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux r1 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.919586,-0.58207,-2.50535,-3.28262,-3.66283,-4.26031,-8.69672],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.7892,'kcal/mol','+|-',4.17612),
        S298 = (1.65079,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)[CH]C(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 454,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_N-3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 {1,S} {3,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C   u0 {2,S}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   u0 {1,S} {7,S}
7   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.685257,-1.57068,-3.4984,-4.53863,-5.23023,-5.54224,-7.71923],'cal/mol/K','+|-',[4.90149,3.98147,3.6469,3.6295,3.5002,3.2295,6.55761]),
        H298 = (99.2083,'kcal/mol','+|-',5.91584),
        S298 = (3.68675,'cal/mol/K','+|-',4.73839),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 455,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_N-3R!H->O_7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C   u0 r1 {2,S}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   u0 r1 {1,S} {7,S}
7   C   u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.0093,-0.71539,-2.85615,-3.90882,-4.69973,-5.31048,-5.68815],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.0873,'kcal/mol','+|-',4.17612),
        S298 = (2.43914,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1(C)[CH]CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 456,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_N-3R!H->O_N-7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C   u0 r1 {2,S}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   u0 r1 {1,S} {7,S}
7   O   u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.638783,-2.42596,-4.14065,-5.16845,-5.76073,-5.77399,-9.75031],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.3293,'kcal/mol','+|-',4.17612),
        S298 = (4.93437,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC1(C)[CH]COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 457,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-1R-R",
    group = 
"""
1 * C     u1 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C     ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   [C,O] ux {2,[S,T,Q,B]}
4   [C,O] ux {2,[S,D,T,B,Q]}
5   R!H   ux {2,[S,D,T,B,Q]}
6   C     ux {1,[S,D,T,B,Q]}
7   O     ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.14492,-7.02145,-9.58141,-10.43,-9.34422,-8.34134,-13.0109],'cal/mol/K','+|-',[3.28596,3.39984,3.62312,3.84567,3.84892,3.55286,3.44722]),
        H298 = (94.2472,'kcal/mol','+|-',6.62352),
        S298 = (8.2862,'cal/mol/K','+|-',4.01267),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 458,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-1R-R_Ext-7R!H-R_Ext-8R!H-R_3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
7   O   ux r1 {1,[S,D,T,B,Q]}
8   O   u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.82918,-6.58001,-8.95621,-9.65627,-8.56848,-7.76876,-12.5257],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.3073,'kcal/mol','+|-',4.17612),
        S298 = (9.15952,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OCOOC1(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 459,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-1R-R_Ext-7R!H-R_Ext-8R!H-R_N-3R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
5   O ux r1 {2,[S,D,T,B,Q]} {8,S}
6   C ux {1,[S,D,T,B,Q]}
7   O ux r1 {1,[S,D,T,B,Q]}
8   O u0 r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.46066,-7.46288,-10.2066,-11.2037,-10.12,-8.91393,-13.4961],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.1871,'kcal/mol','+|-',4.17612),
        S298 = (7.41289,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OCOOC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 460,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_N-6R!H->C",
    group = 
"""
1 * C     u1 r1 {2,S} {6,S}
2   C     ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   [C,O] ux {2,[S,T,Q,B]}
4   [C,O] ux {2,[S,D,T,B,Q]}
5   [C,O] ux {2,[S,D,T,B,Q]}
6   O     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.01063,-2.62953,-5.51509,-7.07203,-7.41633,-7.88125,-9.70939],'cal/mol/K','+|-',[5.72856,3.18388,4.31372,6.3219,7.75551,8.4401,3.73562]),
        H298 = (103.584,'kcal/mol','+|-',10.6028),
        S298 = (6.52372,'cal/mol/K','+|-',8.39386),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 461,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_3R!H-inRing",
    group = 
"""
1 * C     u1 r1 {2,S} {6,S}
2   C     ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   [C,O] ux r1 {2,[S,T,Q,B]}
4   [C,O] ux {2,[S,D,T,B,Q]}
5   O     ux {2,[S,D,T,B,Q]} {7,S}
6   O     u0 r1 {1,S}
7   O     u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.69943,-2.49861,-6.5524,-9.00744,-9.92003,-10.6479,-9.00628],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (106.697,'kcal/mol','+|-',4.17612),
        S298 = (9.27274,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CO[CH]C(COO)(OO)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 462,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_N-3R!H-inRing",
    group = 
"""
1 * C     u1 r1 {2,S} {6,S}
2   C     ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   [C,O] ux r0 {2,[S,T,Q,B]}
4   [C,O] ux {2,[S,D,T,B,Q]}
5   O     ux r1 {2,[S,D,T,B,Q]} {7,S}
6   O     u0 r1 {1,S}
7   O     u0 r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.678177,-2.76044,-4.47778,-5.13662,-4.91263,-5.11459,-10.4125],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.471,'kcal/mol','+|-',4.17612),
        S298 = (3.7747,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1O[CH]C(C)(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 463,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.612407,-0.540073,-1.69749,-2.33418,-3.20151,-3.95361,-5.5747],'cal/mol/K','+|-',[2.63884,3.56538,4.41173,4.22674,3.48343,3.00548,4.54599]),
        H298 = (99.2362,'kcal/mol','+|-',7.68451),
        S298 = (0.72207,'cal/mol/K','+|-',7.15949),
    ),
    shortDesc = """Radical correction fitted to 38 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 464,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.734164,-0.777262,-2.10583,-2.74588,-3.59291,-4.32404,-5.70723],'cal/mol/K','+|-',[2.75475,3.68824,4.44371,4.10993,3.38546,2.99276,4.55041]),
        H298 = (98.5461,'kcal/mol','+|-',8.57411),
        S298 = (0.544996,'cal/mol/K','+|-',8.06807),
    ),
    shortDesc = """Radical correction fitted to 28 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 465,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.167562,-0.915698,-1.91296,-2.50985,-3.23132,-3.76569,-6.65311],'cal/mol/K','+|-',[2.30517,3.68189,4.82595,4.8551,3.9812,3.09531,6.14789]),
        H298 = (98.8563,'kcal/mol','+|-',14.5632),
        S298 = (1.96528,'cal/mol/K','+|-',8.73444),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 466,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_4C-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 r1 {2,S}
4   C u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.319201,-0.533412,-1.11874,-1.44075,-2.12054,-2.87385,-3.87847],'cal/mol/K','+|-',[4.07189,3.86801,3.85431,2.64694,2.63001,2.80755,3.4256]),
        H298 = (96.0258,'kcal/mol','+|-',38.7269),
        S298 = (-1.48061,'cal/mol/K','+|-',15.8077),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 467,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_4C-inRing_Ext-4C-R_Sp-5R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r1 {2,S}
4   C u0 r1 {2,S} {5,S}
5   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.346765,0.0809461,-0.507909,-1.21111,-2.3421,-3.17132,-4.37419],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (99.8942,'kcal/mol','+|-',1.69706),
        S298 = (1.67631,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C2CCC1C1CCC=CC1OO2 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 468,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_4C-inRing_Ext-4C-R_N-Sp-5R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r1 {2,S}
4   C u0 r1 {2,S} {5,[B,D,T,Q]}
5   C u0 r1 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.98412,-2.06931,-2.64583,-2.01486,-1.56665,-2.13016,-2.63919],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (72.6006,'kcal/mol','+|-',4.17612),
        S298 = (-9.37291,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC2C=CC1OOC2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 469,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.105123,-1.07311,-2.23999,-2.95007,-3.6887,-4.13292,-7.79561],'cal/mol/K','+|-',[2.33453,4.18898,5.52432,5.5756,4.41603,3.36445,5.7168]),
        H298 = (100.513,'kcal/mol','+|-',5.31568),
        S298 = (3.38418,'cal/mol/K','+|-',5.41953),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 470,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]}
4   C   ux r0 {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.536181,-2.05151,-3.39495,-4.03386,-4.4168,-4.56722,-8.91486],'cal/mol/K','+|-',[3.28205,3.21362,3.1261,3.1182,2.91684,2.95431,2.96943]),
        H298 = (97.5138,'kcal/mol','+|-',5.11732),
        S298 = (4.15577,'cal/mol/K','+|-',7.99116),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 471,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-1R-R_5R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]}
5   O ux {1,[S,D,T,B,Q]}
6   C u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.9041,-1.89883,-3.09443,-3.83653,-4.26622,-4.39114,-8.85528],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.477,'kcal/mol','+|-',4.17612),
        S298 = (2.15867,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OOC[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 472,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-1R-R_N-5R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,[S,D,T,B,Q]}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 r1 {2,S}
4   C u0 r0 {2,S}
5   C u0 {1,S}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.352222,-2.12785,-3.54521,-4.13253,-4.49209,-4.65526,-8.94465],'cal/mol/K','+|-',[4.17111,4.14506,3.9585,3.98489,3.68056,3.73317,3.77894]),
        H298 = (97.0322,'kcal/mol','+|-',5.93136),
        S298 = (5.15432,'cal/mol/K','+|-',10.0226),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 473,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-1R-R_N-5R!H->O_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S}
4   C   u0 r0 {2,S} {7,[S,D,T,B,Q]}
5   C   u0 r1 {1,S}
6   C   ux {1,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.609427,-1.18039,-2.70336,-3.27525,-3.82628,-3.95378,-8.21318],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.2262,'kcal/mol','+|-',4.17612),
        S298 = (1.79178,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 474,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]}
4   C   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.25043,-0.348812,-1.42442,-2.1541,-3.10359,-3.75825,-6.7844],'cal/mol/K','+|-',[2.78085,5.82353,8.13108,8.27572,6.59224,4.96155,8.27287]),
        H298 = (101.781,'kcal/mol','+|-',3.84191),
        S298 = (2.60344,'cal/mol/K','+|-',4.91133),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 475,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-4C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S}
4   C   u0 r0 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.21315,-0.106284,-1.13467,-1.50173,-2.63789,-3.443,-7.79347],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (103.179,'kcal/mol','+|-',4.17612),
        S298 = (-0.284497,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C(O)C1[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 476,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-4C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]}
4   C   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.313567,1.07743,0.657584,-0.145745,-1.52184,-2.61449,-4.3221],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (101.33,'kcal/mol','+|-',1.69706),
        S298 = (2.90542,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOCC1[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 477,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r0 {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16699,-0.710813,-2.1984,-2.85917,-3.76647,-4.59204,-5.2532],'cal/mol/K','+|-',[2.7156,3.90219,4.48871,3.95588,3.26067,3.01224,3.54468]),
        H298 = (98.3949,'kcal/mol','+|-',4.95809),
        S298 = (-0.136743,'cal/mol/K','+|-',7.69575),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 478,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]} {5,D}
5   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.41119,-1.23829,-3.07204,-3.50047,-4.04017,-4.82523,-4.72775],'cal/mol/K','+|-',[2.89685,4.05007,4.35551,3.78033,3.13007,2.72959,2.15862]),
        H298 = (99.7885,'kcal/mol','+|-',4.30753),
        S298 = (-1.67079,'cal/mol/K','+|-',8.09751),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 479,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r0 {2,S}
4   C   u0 r1 {2,S} {5,D} {6,[S,D,T,B,Q]}
5   R!H ux {4,D}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2963,3.51947,1.0109,0.108907,-1.09382,-2.4096,-3.67827],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (105.123,'kcal/mol','+|-',4.17612),
        S298 = (-4.87982,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C(O)[CH]OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 480,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r0 {2,S}
4   C   u0 r1 {2,S} {5,D}
5   C   u0 r1 {4,D}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.10426,-1.63689,-4.49328,-5.65322,-6.53932,-6.75123,-6.37473],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.2509,'kcal/mol','+|-',4.17612),
        S298 = (-2.06586,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCC=CC1OOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 481,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r0 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]} {5,D}
5   C ux {4,D}
6   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.872899,-1.90665,-3.61438,-3.82446,-4.07324,-4.79951,-4.54712],'cal/mol/K','+|-',[1.55259,2.4411,3.30615,3.01669,2.61149,2.37547,1.87095]),
        H298 = (99.6354,'kcal/mol','+|-',3.09317),
        S298 = (-1.65989,'cal/mol/K','+|-',8.74155),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 482,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r0 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]} {5,D}
5   C ux {4,D}
6   O ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.956096,-2.3824,-4.39024,-4.50786,-4.64246,-5.30457,-4.52067],'cal/mol/K','+|-',[1.80107,2.25405,2.46472,2.28883,2.02086,1.89717,2.21409]),
        H298 = (99.1697,'kcal/mol','+|-',3.54012),
        S298 = (-3.85957,'cal/mol/K','+|-',6.13598),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 483,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r0 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]} {5,D}
5   C ux {4,D}
6   O ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   C ux {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.82477,-2.5595,-4.58162,-4.68858,-4.75431,-5.37013,-4.61552],'cal/mol/K','+|-',[2.00706,2.47951,2.72297,2.52102,2.30443,2.18414,2.55272]),
        H298 = (98.7829,'kcal/mol','+|-',3.74674),
        S298 = (-2.56822,'cal/mol/K','+|-',4.51141),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 484,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1  * C   u1 r1 {2,S} {11,S}
2    C   u0 {1,S} {3,S} {4,S}
3    O   u0 r0 {2,S} {6,S}
4    C   u0 {2,S} {5,D}
5    C   u0 {4,D} {10,[S,D,T,B,Q]}
6    O   u0 {3,S} {7,[S,D,T,B,Q]}
7    C   ux {6,[S,D,T,B,Q]} {8,S}
8    C   u0 {7,S} {9,S}
9    C   ux {8,S}
10   R!H ux {5,[S,D,T,B,Q]}
11   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.637581,-2.72927,-4.95691,-5.2387,-5.40237,-5.96427,-5.18406],'cal/mol/K','+|-',[3.41579,3.96838,3.95573,3.38169,3.1626,3.17059,3.44873]),
        H298 = (99.4155,'kcal/mol','+|-',6.39416),
        S298 = (-3.98729,'cal/mol/K','+|-',3.52648),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 485,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-5R!H-R_Ext-1R-R_Ext-5R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {11,S}
2    C   u0 r1 {1,S} {3,S} {4,S}
3    O   u0 r0 {2,S} {6,S}
4    C   u0 r1 {2,S} {5,D}
5    C   u0 r1 {4,D} {10,[S,D,T,B,Q]} {12,[S,D,T,B,Q]}
6    O   u0 r0 {3,S} {7,[S,D,T,B,Q]}
7    C   ux {6,[S,D,T,B,Q]} {8,S}
8    C   u0 {7,S} {9,S}
9    C   ux {8,S}
10   R!H ux {5,[S,D,T,B,Q]}
11   C   u0 r1 {1,S}
12   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09414,-1.88163,-4.11669,-4.81505,-5.38645,-5.88313,-5.67059],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.5491,'kcal/mol','+|-',4.17612),
        S298 = (-4.53912,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC(OOCC(C)C)[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 486,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r0 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]} {5,D}
5   C ux {4,D}
6   O ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   C ux {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.771222,-2.84765,-4.80123,-4.6608,-4.50612,-5.09108,-4.09804],'cal/mol/K','+|-',[2.61541,2.70491,3.0365,3.19701,2.99171,2.84735,3.22997]),
        H298 = (98.5257,'kcal/mol','+|-',4.87789),
        S298 = (-1.58133,'cal/mol/K','+|-',5.83683),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 487,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r1 {2,S}
2    C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3    O ux r0 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4    C ux {2,[S,D,T,B,Q]} {5,D}
5    C ux {4,D}
6    O ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,S}
9    C ux {8,S} {10,S}
10   C u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.880622,-2.92576,-5.06387,-4.96997,-4.68671,-5.2526,-4.44306],'cal/mol/K','+|-',[3.17178,3.33965,3.66766,3.84894,3.71277,3.50077,3.83083]),
        H298 = (98.364,'kcal/mol','+|-',5.9442),
        S298 = (-0.635021,'cal/mol/K','+|-',6.58117),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 488,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_Sp-10R!H-9R!H_Ext-10R!H-R_Ext-7R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S}
2    C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3    O   ux r0 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4    C   ux r1 {2,[S,D,T,B,Q]} {5,D}
5    C   ux r1 {4,D}
6    O   ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C   ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]} {12,[S,D,T,B,Q]}
8    C   ux r1 {7,[S,D,T,B,Q]} {9,S}
9    C   ux r1 {8,S} {10,S}
10   C   u0 r1 {9,S} {11,[S,D,T,B,Q]}
11   C   u0 r1 {10,[S,D,T,B,Q]}
12   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.793867,-3.30545,-5.72073,-5.74573,-5.37452,-5.78356,-5.20753],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.6021,'kcal/mol','+|-',4.17612),
        S298 = (1.40556,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC1OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 489,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_N-Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r1 {2,S}
2    C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3    O ux r0 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4    C ux r1 {2,[S,D,T,B,Q]} {5,D}
5    C ux r1 {4,D}
6    O ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C ux r1 {7,[S,D,T,B,Q]} {9,S}
9    C ux r1 {8,S} {10,[B,D,T,Q]}
10   C u0 r1 {9,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.55242,-2.69142,-4.27593,-4.04246,-4.14495,-4.76804,-3.40801],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.8491,'kcal/mol','+|-',4.17612),
        S298 = (-3.47395,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC1OOC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 490,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_N-7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r0 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux r1 {2,[S,D,T,B,Q]} {5,D}
5   C ux r1 {4,D}
6   O ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux r0 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   C ux {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3598,-1.3555,-3.17224,-3.67165,-4.20275,-5.01903,-5.03087],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.2891,'kcal/mol','+|-',4.17612),
        S298 = (-2.69074,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1[CH]CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 491,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 r0 {2,S} {6,S}
4   C u0 {2,S} {5,D}
5   C u0 {4,D}
6   O u0 {3,S} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,S}
8   C u0 {7,S} {9,[B,D,T,Q]}
9   C ux {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.35007,-1.85113,-3.81611,-3.96571,-4.30692,-5.10787,-4.23613],'cal/mol/K','+|-',[3.17437,3.31382,3.33194,3.30528,3.16241,3.17751,3.16807]),
        H298 = (100.33,'kcal/mol','+|-',5.92835),
        S298 = (-7.73364,'cal/mol/K','+|-',3.29617),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 492,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r0 {2,S} {6,S}
4   C u0 r1 {2,S} {5,D}
5   C u0 r1 {4,D}
6   O u0 r0 {3,S} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]} {8,S}
8   C u0 {7,S} {9,[B,D,T,Q]}
9   C ux {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2522,-2.20138,-4.18722,-4.30572,-4.29667,-4.99801,-4.3038],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.512,'kcal/mol','+|-',4.17612),
        S298 = (-7.40486,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC1OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 493,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_N-7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r0 {2,S} {6,S}
4   C u0 r1 {2,S} {5,D}
5   C u0 r1 {4,D}
6   O u0 r0 {3,S} {7,[S,D,T,B,Q]}
7   C ux r0 {6,[S,D,T,B,Q]} {8,S}
8   C u0 {7,S} {9,[B,D,T,Q]}
9   C ux {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.44795,-1.50087,-3.44499,-3.62569,-4.31717,-5.21774,-4.16845],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.148,'kcal/mol','+|-',4.17612),
        S298 = (-8.06242,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)OOC1[CH]CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 494,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r0 {2,S} {6,S}
4   C   u0 r1 {2,S} {5,D}
5   C   u0 r1 {4,D} {7,S}
6   O   u0 r0 {3,S}
7   C   u0 r1 {5,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.522738,-0.64448,-1.45565,-1.82762,-2.34001,-3.25961,-4.43598],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (100.486,'kcal/mol','+|-',1.69706),
        S298 = (3.74378,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 495,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.829762,0.0176131,-0.99195,-1.97356,-3.38852,-4.27002,-5.97882],'cal/mol/K','+|-',[2.8572,3.71445,3.93451,4.01337,3.84043,3.80071,4.98897]),
        H298 = (97.2061,'kcal/mol','+|-',4.81538),
        S298 = (1.98171,'cal/mol/K','+|-',4.97055),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 496,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 r0 {2,S}
4   C u0 {2,S} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.127429,-1.4979,-2.80439,-4.07337,-5.43197,-6.40512,-8.96785],'cal/mol/K','+|-',[4.01367,5.60486,5.24455,5.34201,6.30018,6.33197,3.53423]),
        H298 = (95.0842,'kcal/mol','+|-',10.8722),
        S298 = (5.1177,'cal/mol/K','+|-',4.34195),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 497,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_5R!H->C_Ext-5C-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r0 {2,S}
4   C   u0 r1 {2,S} {5,[S,T,Q,B]}
5   C   ux r1 {4,[S,T,Q,B]} {6,S}
6   R!H u0 r1 {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00132,-3.13399,-4.28363,-5.59559,-7.3585,-8.34464,-8.40987],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.3115,'kcal/mol','+|-',4.17612),
        S298 = (4.06577,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 498,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r0 {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   O ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.05498,0.374203,-0.565494,-1.47949,-2.90771,-3.76764,-5.27552],'cal/mol/K','+|-',[2.90496,3.38225,3.5761,3.41728,2.89689,2.70186,4.36128]),
        H298 = (97.4275,'kcal/mol','+|-',4.23979),
        S298 = (1.24383,'cal/mol/K','+|-',4.03736),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 499,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_N-5R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   O   ux {4,[S,T,Q,B]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.800084,-0.0125418,-1.01,-1.86998,-3.14933,-4.02931,-5.66339],'cal/mol/K','+|-',[3.4559,3.87878,4.02764,3.92094,3.46548,3.16094,5.24525]),
        H298 = (98.2483,'kcal/mol','+|-',4.00757),
        S298 = (1.76187,'cal/mol/K','+|-',4.52391),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 500,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_N-5R!H->C_Ext-1R-R_5O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]} {5,S}
5   O   u0 r1 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.56481,-0.613001,-1.84938,-2.7381,-3.95385,-4.75635,-6.5965],'cal/mol/K','+|-',[5.19744,5.28934,4.79328,4.42664,3.64228,3.28019,6.97897]),
        H298 = (99.2598,'kcal/mol','+|-',4.47491),
        S298 = (2.61597,'cal/mol/K','+|-',5.79046),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 501,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_N-5R!H->C_Ext-1R-R_5O-inRing_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   C   ux r1 {2,[S,D,T,B,Q]} {5,S}
5   O   u0 r1 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.76617,-2.99613,-3.9478,-4.61986,-5.34183,-5.89085,-9.90819],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.192,'kcal/mol','+|-',4.17612),
        S298 = (5.27974,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 502,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_N-5R!H->C_Ext-1R-R_N-5O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r0 {2,S}
4   C   u0 r1 {2,S} {5,[S,T,Q,B]}
5   O   ux r0 {4,[S,T,Q,B]}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12947,0.828101,0.165127,-0.654617,-2.02301,-3.01145,-4.35702],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (97.0698,'kcal/mol','+|-',1.69706),
        S298 = (0.566126,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 503,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.375299,-0.0781787,-0.902297,-1.53246,-2.4393,-3.23226,-5.31661],'cal/mol/K','+|-',[2.66946,3.45248,4.22883,4.32093,3.47143,2.78237,4.85891]),
        H298 = (100.234,'kcal/mol','+|-',6.23205),
        S298 = (1.0669,'cal/mol/K','+|-',5.33169),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 504,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   O ux {2,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.617773,0.0188509,-1.00325,-1.69427,-2.59388,-3.39997,-5.75607],'cal/mol/K','+|-',[2.77779,4.02645,4.99722,5.06845,4.0142,3.13595,5.43268]),
        H298 = (101.75,'kcal/mol','+|-',4.55881),
        S298 = (1.37795,'cal/mol/K','+|-',5.78692),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 505,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   O ux {2,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.889498,0.453928,-0.456538,-1.1571,-2.22121,-3.14106,-5.3003],'cal/mol/K','+|-',[1.8702,2.25659,2.71469,2.97531,2.89266,2.50666,4.29929]),
        H298 = (101.857,'kcal/mol','+|-',4.49882),
        S298 = (1.06104,'cal/mol/K','+|-',5.48242),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 506,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Int-4O-3O",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   O u0 r1 {2,S} {3,[S,D,T,B,Q]}
5   C u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.680747,-1.29592,-3.17885,-4.06438,-4.37701,-4.89546,-10.8017],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (104.112,'kcal/mol','+|-',4.17612),
        S298 = (3.74096,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1O[C]1C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 507,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {6,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 {2,S}
4   O u0 {2,S}
5   C u0 r1 {1,S}
6   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.37617,1.15097,0.304476,-0.343987,-1.54973,-2.72548,-4.97112],'cal/mol/K','+|-',[3.05619,3.78328,3.61032,4.72365,5.99218,5.38185,2.39323]),
        H298 = (99.2353,'kcal/mol','+|-',3.20369),
        S298 = (-1.55409,'cal/mol/K','+|-',10.5992),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 508,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Ext-1R-R_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S} {7,[S,D,T,B,Q]}
4   O   u0 {2,S}
5   C   u0 r1 {1,S}
6   O   u0 r0 {1,S}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.33794,2.63206,1.671,1.71376,1.22553,-0.290088,-4.913],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.6076,'kcal/mol','+|-',4.17612),
        S298 = (-6.76959,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1OOC(O)[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 509,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Ext-5C-R",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 {2,S}
4   O u0 {2,S}
5   C u0 r1 {1,S} {6,S}
6   O u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.656144,0.05028,-0.961743,-1.64793,-2.59564,-3.37844,-5.47251],'cal/mol/K','+|-',[2.55461,2.51033,2.73082,2.59643,2.39481,2.3961,5.85565]),
        H298 = (101.349,'kcal/mol','+|-',4.84971),
        S298 = (1.97539,'cal/mol/K','+|-',2.65703),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 510,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Ext-5C-R_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 {2,S} {7,[S,D,T,B,Q]}
4   O   u0 r1 {2,S}
5   C   u0 r1 {1,S} {6,S}
6   O   u0 r1 {5,S}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.201088,-0.336838,-1.62857,-2.15982,-2.6685,-3.46148,-8.17239],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (103.59,'kcal/mol','+|-',4.17612),
        S298 = (1.38952,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 511,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   O   ux r1 {2,[S,D,T,B,Q]}
5   C   ux r1 {1,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.853737,0.170066,-0.652463,-1.31011,-2.38828,-3.20383,-4.44062],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.915,'kcal/mol','+|-',1.69706),
        S298 = (2.43392,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 512,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_N-5C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]}
4   O ux {2,[S,D,T,B,Q]}
5   C ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.91466,-5.63715,-8.11055,-8.67749,-7.43854,-6.76588,-11.6811],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.8445,'kcal/mol','+|-',4.17612),
        S298 = (5.49774,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OCOOC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 513,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   O ux {2,[S,D,T,B,Q]}
5   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.303626,-0.349862,-0.61962,-1.07938,-2.00647,-2.76268,-4.08611],'cal/mol/K','+|-',[3.13792,2.39877,2.00059,2.12517,2.42363,2.54776,2.29662]),
        H298 = (96.7028,'kcal/mol','+|-',2.66509),
        S298 = (0.195957,'cal/mol/K','+|-',5.18857),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 514,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_N-5R!H->C_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   O   ux {2,[S,D,T,B,Q]}
5   O   ux r1 {1,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.551251,0.118394,-0.602449,-1.33343,-2.49047,-3.32069,-4.48524],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (97.1125,'kcal/mol','+|-',1.69706),
        S298 = (1.88863,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 515,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.26614,-1.048,-2.126,-2.73022,-3.32513,-3.7536,-4.74787],'cal/mol/K','+|-',[3.99637,4.00502,3.32976,2.68212,2.15661,2.24629,3.07264]),
        H298 = (98.5536,'kcal/mol','+|-',4.75904),
        S298 = (1.63363,'cal/mol/K','+|-',5.74644),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 516,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Int-4R!H-3C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   C u0 {2,S} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.594834,-0.281535,-1.25899,-2.00703,-2.87527,-3.50278,-4.62831],'cal/mol/K','+|-',[3.26514,3.4861,3.71424,3.77197,3.54193,3.34845,3.24358]),
        H298 = (95.0838,'kcal/mol','+|-',6.89339),
        S298 = (6.14989,'cal/mol/K','+|-',5.15372),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 517,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Int-4R!H-3C_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 r1 {2,S} {3,[S,D,T,B,Q]} {5,S}
5   C   u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.882311,0.237223,-0.570194,-1.28007,-2.31122,-3.11353,-4.37315],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.8269,'kcal/mol','+|-',4.17612),
        S298 = (4.71111,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 518,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3343,-1.15616,-2.20989,-2.75293,-3.26978,-3.64718,-4.69423],'cal/mol/K','+|-',[4.26295,4.2391,3.50062,2.77105,2.06327,2.02872,3.23195]),
        H298 = (98.5539,'kcal/mol','+|-',3.81672),
        S298 = (1.06882,'cal/mol/K','+|-',5.0761),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 519,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   C   u0 {1,S} {3,S} {4,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   R!H u0 r1 {1,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.086767,-0.541953,-1.12412,-1.70169,-2.58638,-3.27802,-4.38916],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (100.612,'kcal/mol','+|-',1.69706),
        S298 = (0.123374,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=CC2[C](C1)C1C=CC2C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 520,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.985081,-0.23738,-1.45138,-2.22758,-2.98849,-3.47638,-5.02752],'cal/mol/K','+|-',[5.20387,4.01438,2.66854,1.95691,2.14479,2.70608,5.09699]),
        H298 = (97.1088,'kcal/mol','+|-',3.37475),
        S298 = (0.918228,'cal/mol/K','+|-',5.23414),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 521,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.52228,0.818719,-1.02848,-2.27859,-3.51143,-4.13497,-6.40894],'cal/mol/K','+|-',[4.34996,4.01421,3.37943,2.74489,2.70659,3.49655,6.43764]),
        H298 = (96.6927,'kcal/mol','+|-',5.80335),
        S298 = (1.96891,'cal/mol/K','+|-',6.86735),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 522,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-4R!H-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   C   u0 r1 {2,S} {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
4   C   u0 {2,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   R!H u0 r1 {1,S} {6,S}
6   C   u0 r1 {3,[S,D,T,B,Q]} {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
9   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.720635,-0.562883,-1.6158,-2.47208,-3.13205,-3.33914,-4.6103],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.4663,'kcal/mol','+|-',4.17612),
        S298 = (5.43699,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 523,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-4R!H-R_4R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C   ux r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.62974,0.545058,-1.69907,-2.61643,-3.4628,-3.57644,-4.8047],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.303,'kcal/mol','+|-',4.17612),
        S298 = (1.285,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC1C1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 524,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-4R!H-R_N-4R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C   ux r0 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.21646,2.47398,0.229417,-1.74727,-3.93945,-5.48934,-9.81182],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.3088,'kcal/mol','+|-',4.17612),
        S298 = (-0.815252,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(OO)C1[CH]OC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 525,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {2,[S,T,Q,B]} {6,D}
4   C ux r0 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r1 {3,D} {5,[S,D,T,B,Q]}
7   C ux {4,[S,D,T,B,Q]} {8,D}
8   C u0 r0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.41483,-1.90677,-2.24204,-2.41756,-2.49058,-2.85373,-3.70522],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (97.4171,'kcal/mol','+|-',1.69706),
        S298 = (0.653162,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]CC=C1 - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 526,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {2,[S,T,Q,B]} {6,D}
4   C ux r0 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r1 {3,D} {5,[S,D,T,B,Q]}
7   C ux {4,[S,D,T,B,Q]} {8,S}
8   C u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.37326,0.767799,-0.743445,-1.59962,-2.66445,-3.05724,-4.18902],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.4908,'kcal/mol','+|-',4.17612),
        S298 = (-1.57116,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)CC1[CH]CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 527,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.83179,-2.17447,-3.14536,-3.45259,-3.58106,-3.67142,-4.36921],'cal/mol/K','+|-',[4.6134,4.69072,4.05156,3.36616,2.53658,2.05392,2.68766]),
        H298 = (99.0402,'kcal/mol','+|-',3.23737),
        S298 = (1.31538,'cal/mol/K','+|-',6.25721),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 528,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
8   C ux {3,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9   C ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.30487,-3.07372,-4.11367,-4.08594,-3.62505,-3.47407,-3.65379],'cal/mol/K','+|-',[5.81831,4.51254,3.38544,2.91082,2.52466,2.35362,2.55518]),
        H298 = (98.1593,'kcal/mol','+|-',4.36902),
        S298 = (-1.31285,'cal/mol/K','+|-',3.30155),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 529,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R_Int-7R!H-4R!H",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
8   C ux {3,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9   C ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.392715,-1.635,-3.12897,-3.36236,-3.22204,-3.31362,-3.83619],'cal/mol/K','+|-',[3.27093,2.82655,2.65269,2.7221,2.9801,3.05722,3.32385]),
        H298 = (98.3757,'kcal/mol','+|-',5.53074),
        S298 = (-2.0835,'cal/mol/K','+|-',3.1935),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 530,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R_Int-7R!H-4R!H_Ext-1R-R",
    group = 
"""
1  * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
2    C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3    C   ux {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4    C   ux r1 {2,[S,D,T,B,Q]} {7,D}
5    C   ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6    C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C   ux r1 {4,D} {6,[S,D,T,B,Q]}
8    C   u0 r0 {3,[S,D,T,B,Q]} {9,[S,D]}
9    C   ux r0 {8,[S,D]}
10   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.54784,-0.975523,-2.91934,-3.50512,-3.63396,-3.67547,-4.50178],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.3697,'kcal/mol','+|-',4.17612),
        S298 = (-1.01465,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1C=CCC[C]1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 531,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R_Int-7R!H-4R!H_Ext-4R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2    C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3    C   ux {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4    C   ux r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
5    C   ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6    C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C   ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
8    C   ux {3,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9    C   ux {8,[S,D,T,B,Q]}
10   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.270507,-1.89777,-2.98972,-2.87805,-2.36315,-2.37653,-2.62986],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.9155,'kcal/mol','+|-',4.17612),
        S298 = (-2.45635,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]CCC=C1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 532,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R_8R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4   C ux r1 {2,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]}
8   C ux r1 {3,[S,D,T,B,Q]} {9,S}
9   C ux {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.71811,-5.52969,-5.54666,-4.87593,-4.07358,-3.65792,-3.16949],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.0873,'kcal/mol','+|-',4.17612),
        S298 = (-0.73999,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCC=CCC1CC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 533,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R_N-8R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4   C ux r1 {2,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]}
8   C ux r0 {3,[S,D,T,B,Q]} {9,S}
9   C ux {8,S}
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
    index = 534,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Int-8R!H-7R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16819,-5.39258,-5.47371,-5.35521,-5.10764,-4.69345,-4.3864],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.3897,'kcal/mol','+|-',4.17612),
        S298 = (5.27827,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1[CH]CCC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 535,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
9   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.06919,-0.714224,-2.64882,-3.72485,-4.62114,-4.85024,-5.74347],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.0716,'kcal/mol','+|-',4.17612),
        S298 = (1.65103,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCCC1=CCC(C)[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 536,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_3C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.729875,0.0744822,-0.690897,-1.31971,-2.2679,-3.04186,-4.33334],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (99.5365,'kcal/mol','+|-',1.69706),
        S298 = (3.04595,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CCC(C)[CH]C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 537,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_N-3C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,T,Q,B]} {8,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.352648,-1.5427,-2.6082,-3.44316,-4.07736,-4.03123,-6.64449],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.058,'kcal/mol','+|-',4.17612),
        S298 = (5.83152,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC1[CH]OC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 538,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.98591,1.03822,-1.40686,-2.68636,-4.3128,-5.81634,-6.94259],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (94.6335,'kcal/mol','+|-',4.17612),
        S298 = (-0.237344,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)[C]1OCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 539,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C                      ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C                      ux {2,[S,T,Q,B]}
4   C                      ux {2,[S,D,T,B,Q]}
5   R!H                    ux r1 {1,[S,D,T,B,Q]} {6,S}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.14318,-0.255309,-2.05637,-3.68833,-5.41475,-6.54316,-6.14038],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (105.484,'kcal/mol','+|-',4.17612),
        S298 = (4.74467,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1[CH]COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 540,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0630036,-1.03606,-1.9184,-2.59676,-3.43747,-4.07877,-5.14681],'cal/mol/K','+|-',[2.31366,3.02615,3.66492,3.94577,3.79738,3.73698,3.3621]),
        H298 = (97.1616,'kcal/mol','+|-',13.9917),
        S298 = (1.52492,'cal/mol/K','+|-',5.10599),
    ),
    shortDesc = """Radical correction fitted to 50 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 541,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.116757,-1.08559,-1.91383,-2.55672,-3.33421,-3.94522,-4.96746],'cal/mol/K','+|-',[2.01445,2.77833,3.51082,3.79965,3.55934,3.47814,2.87919]),
        H298 = (97.0884,'kcal/mol','+|-',6.03875),
        S298 = (1.73627,'cal/mol/K','+|-',5.23326),
    ),
    shortDesc = """Radical correction fitted to 42 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 542,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0196288,-1.04055,-1.93507,-2.6306,-3.47554,-4.13188,-5.22375],'cal/mol/K','+|-',[2.22757,2.87375,3.65344,3.98976,3.59528,3.37084,3.50588]),
        H298 = (98.2571,'kcal/mol','+|-',5.62624),
        S298 = (1.91305,'cal/mol/K','+|-',4.45991),
    ),
    shortDesc = """Radical correction fitted to 24 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 543,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   O ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.698085,-1.53102,-3.00943,-3.95933,-4.79571,-5.50442,-5.94098],'cal/mol/K','+|-',[3.00467,4.30197,4.87771,5.2433,4.89743,4.76227,3.23412]),
        H298 = (100.355,'kcal/mol','+|-',9.14143),
        S298 = (2.79837,'cal/mol/K','+|-',6.66448),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 544,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   ux {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.994822,-1.88774,-3.65203,-4.71367,-5.53973,-6.27146,-6.04831],'cal/mol/K','+|-',[3.29424,4.81145,5.0227,5.26334,4.84009,4.61753,2.71922]),
        H298 = (99.3987,'kcal/mol','+|-',11.1286),
        S298 = (3.62721,'cal/mol/K','+|-',7.0189),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 545,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   ux {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2832,-2.70943,-4.89472,-6.1897,-6.98015,-7.63201,-6.5432],'cal/mol/K','+|-',[3.56497,5.33083,4.43695,3.75734,2.87302,2.55624,2.25341]),
        H298 = (103.883,'kcal/mol','+|-',6.75792),
        S298 = (5.55647,'cal/mol/K','+|-',5.40381),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 546,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   ux {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux r1 {6,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.889172,-4.23446,-6.07628,-7.23725,-7.71556,-7.99306,-6.62463],'cal/mol/K','+|-',[4.73052,6.02937,4.57174,3.36841,2.69554,3.18604,3.21301]),
        H298 = (101.838,'kcal/mol','+|-',5.19845),
        S298 = (7.40166,'cal/mol/K','+|-',3.94826),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 547,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_7R!H-inRing_Ext-8R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D} {5,S}
4   O   ux {3,D}
5   C   u0 r1 {3,S} {6,[S,D,T,B,Q]}
6   R!H ux r1 {5,[S,D,T,B,Q]} {7,S}
7   C   u0 r1 {6,S}
8   R!H ux {1,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9   R!H ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0209725,-2.5392,-5.01153,-6.85664,-7.99733,-8.83875,-7.49498],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (102.959,'kcal/mol','+|-',4.17612),
        S298 = (7.00071,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1COC[C](COO)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 548,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_7R!H-inRing_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   ux {3,D}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux r1 {6,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
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
    index = 549,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_7R!H-inRing_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   ux {3,D}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux r1 {6,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.510433,-2.78726,-4.96297,-6.39739,-7.27421,-8.14872,-6.77771],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.303,'kcal/mol','+|-',4.17612),
        S298 = (9.0547,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 550,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_N-7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   ux {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux r0 {6,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.67723,-1.18439,-3.71315,-5.14214,-6.24475,-7.27095,-6.46178],'cal/mol/K','+|-',[3.54,3.43253,4.06969,3.97233,3.44671,3.10173,2.70032]),
        H298 = (105.927,'kcal/mol','+|-',7.37753),
        S298 = (3.71128,'cal/mol/K','+|-',4.64299),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 551,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_N-7R!H-inRing_8R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D} {5,S}
4   O   ux {3,D}
5   C   u0 r1 {3,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,S}
7   R!H u0 r0 {6,S}
8   C   ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.475571,-0.988731,-2.73786,-4.36605,-6.06207,-7.45311,-6.64156],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (102.722,'kcal/mol','+|-',4.17612),
        S298 = (4.01967,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CC(OO)C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 552,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_N-7R!H-inRing_N-8R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {8,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   u0 {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,S}
6   R!H u0 {5,S} {7,[S,D,T,B,Q]}
7   R!H ux r0 {6,[S,D,T,B,Q]}
8   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.27806,-1.28222,-4.2008,-5.53019,-6.33608,-7.17988,-6.37189],'cal/mol/K','+|-',[3.61469,4.4723,4.90757,4.961,4.49734,3.96346,3.32509]),
        H298 = (107.53,'kcal/mol','+|-',5.96419),
        S298 = (3.55708,'cal/mol/K','+|-',6.26185),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 553,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_N-7R!H-inRing_N-8R!H->C_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {8,S}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   u0 r0 {3,D}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,S}
6   C   u0 {5,S} {7,[S,D,T,B,Q]}
7   R!H ux r0 {6,[S,D,T,B,Q]}
8   O   u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.65899,-2.40034,-5.52765,-6.88165,-7.46668,-8.02464,-6.00854],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (107.824,'kcal/mol','+|-',4.17612),
        S298 = (5.46794,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C1CC(=O)O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 554,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_N-7R!H-inRing_N-8R!H->C_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {8,S}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   u0 r0 {3,D}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,S}
6   O   u0 {5,S} {7,[S,D,T,B,Q]}
7   R!H ux r0 {6,[S,D,T,B,Q]}
8   O   u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.89713,-0.164108,-2.87395,-4.17873,-5.20548,-6.33511,-6.73525],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (107.236,'kcal/mol','+|-',4.17612),
        S298 = (1.64623,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1O[CH]OC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 555,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {7,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O   ux {3,D}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.32288,-0.02226,-2.47122,-3.62434,-4.59701,-5.7889,-7.00222],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.2521,'kcal/mol','+|-',4.17612),
        S298 = (-1.04531,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC(=O)C(C)(C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 556,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_2O-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   O ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.14512,-0.173681,-0.772171,-1.41374,-2.38123,-3.14479,-4.36888],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.132,'kcal/mol','+|-',1.69706),
        S298 = (1.09855,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 557,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_N-2O-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux r0 {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   O ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.738506,-1.53556,-2.49783,-3.15718,-3.76377,-4.1167,-8.85156],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (102.079,'kcal/mol','+|-',4.17612),
        S298 = (-0.82603,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)O[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 558,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.255994,-0.841295,-1.49861,-2.0908,-2.93922,-3.57429,-4.93237],'cal/mol/K','+|-',[1.77071,2.18873,2.80337,2.93951,2.39161,1.90062,3.61346]),
        H298 = (97.692,'kcal/mol','+|-',3.97745),
        S298 = (1.55339,'cal/mol/K','+|-',3.20691),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 559,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.186165,-0.844363,-1.56269,-2.17313,-3.00571,-3.6232,-5.01716],'cal/mol/K','+|-',[1.9001,2.39676,3.05332,3.19173,2.5967,2.06534,3.93544]),
        H298 = (98.115,'kcal/mol','+|-',3.77492),
        S298 = (1.64078,'cal/mol/K','+|-',3.4604),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 560,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
5   R!H ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.147214,-1.07453,-1.9912,-2.67598,-3.42415,-3.94889,-5.99859],'cal/mol/K','+|-',[2.38452,3.29843,4.58858,4.93215,3.95253,3.0262,6.52594]),
        H298 = (96.5075,'kcal/mol','+|-',3.00134),
        S298 = (2.64804,'cal/mol/K','+|-',3.38467),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 561,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R_Int-4O-1R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   u0 {1,[S,D,T,B,Q]} {3,S}
5   R!H ux {1,[S,D,T,B,Q]} {6,S}
6   R!H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.717718,-0.475791,-1.35679,-2.07642,-3.19634,-3.97104,-4.93218],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (95.7011,'kcal/mol','+|-',1.69706),
        S298 = (4.52389,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC[C]1OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 562,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {5,S} {7,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   O u0 {3,S}
5   C u0 {1,S} {6,S}
6   O u0 {5,S}
7   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.40776,-3.29864,-5.12449,-6.02437,-5.85848,-5.58382,-11.2714],'cal/mol/K','+|-',[3.56971,4.6859,6.8984,7.55642,6.77408,5.59007,4.76404]),
        H298 = (96.0363,'kcal/mol','+|-',5.97912),
        S298 = (2.80577,'cal/mol/K','+|-',4.68811),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 563,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R_Ext-1R-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S} {7,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {8,[S,D,T,B,Q]}
4   O   u0 r1 {3,S}
5   C   u0 r1 {1,S} {6,S}
6   O   u0 r1 {5,S}
7   C   u0 {1,S}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9933,-2.07605,-2.9569,-3.59796,-3.74045,-3.95406,-10.0117],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.366,'kcal/mol','+|-',4.17612),
        S298 = (1.58213,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC(OC(C)=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 564,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R_4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   ux r1 {3,S}
5   R!H ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux r1 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.321831,-0.159679,-0.836683,-1.46892,-2.44423,-3.20886,-4.42206],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (98.0193,'kcal/mol','+|-',1.69706),
        S298 = (1.87083,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 565,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R_N-4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   ux r0 {3,S}
5   R!H ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux r1 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.472755,-0.808818,-1.27349,-1.80388,-2.68441,-3.35885,-4.42326],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (95.9577,'kcal/mol','+|-',1.69706),
        S298 = (1.42322,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1CO[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 566,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]}
4   O   ux {3,S}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
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
    index = 567,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S} {6,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.250244,-0.148367,-0.767907,-1.4359,-2.5153,-3.31632,-4.48484],'cal/mol/K','+|-',[1.78489,1.86512,1.91551,1.89643,1.81951,1.74671,1.64954]),
        H298 = (98.5931,'kcal/mol','+|-',2.01053),
        S298 = (0.540514,'cal/mol/K','+|-',1.93802),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 568,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-4O-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   O   u0 {3,S} {6,S}
5   C   u0 {1,S}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.660377,0.336324,-0.253115,-0.941602,-2.10336,-3.00002,-4.37114],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (98.5195,'kcal/mol','+|-',1.69706),
        S298 = (0.0992994,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 569,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-4O-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S} {6,[S,D,T,B,Q]}
5   O   ux {1,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0451768,-0.390713,-1.0253,-1.68306,-2.72127,-3.47448,-4.54169],'cal/mol/K','+|-',[2.00725,2.05291,2.10119,2.09609,2.06634,2.04166,2.00775]),
        H298 = (98.6299,'kcal/mol','+|-',2.47628),
        S298 = (0.761121,'cal/mol/K','+|-',2.23841),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 570,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-4O-R_N-5R!H->C_4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   ux r1 {3,S} {6,[S,D,T,B,Q]}
5   O   ux {1,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.105435,-0.226991,-0.797543,-1.46125,-2.53764,-3.3294,-4.47936],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (98.4143,'kcal/mol','+|-',1.69706),
        S298 = (0.405716,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 571,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-4O-R_N-5R!H->C_N-4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   ux r0 {3,S} {6,[S,D,T,B,Q]}
5   O   ux {1,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0150817,-0.554435,-1.25306,-1.90486,-2.90491,-3.61956,-4.60401],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (98.8455,'kcal/mol','+|-',1.69706),
        S298 = (1.11653,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 572,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   ux r1 {3,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.233198,-1.64869,-2.95307,-3.7389,-4.49227,-4.92486,-5.26854],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (100.598,'kcal/mol','+|-',1.69706),
        S298 = (4.56823,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 573,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_N-4O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   O   u0 r0 {3,S}
5   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0108001,-0.29175,-0.793644,-1.38849,-2.39101,-3.17013,-4.396],'cal/mol/K','+|-',[2.25525,2.26657,2.21918,2.15443,2.06606,2.02509,2.00212]),
        H298 = (97.2394,'kcal/mol','+|-',2.50529),
        S298 = (0.679717,'cal/mol/K','+|-',2.01002),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 574,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_N-4O-inRing_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   O u0 r0 {3,S}
5   C u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.379266,0.0852996,-0.453652,-1.1053,-2.20778,-3.05779,-4.36345],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (96.9853,'kcal/mol','+|-',1.69706),
        S298 = (0.608843,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 575,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_N-4O-inRing_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   O u0 r0 {3,S}
5   O u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.357666,-0.6688,-1.13364,-1.67168,-2.57424,-3.28248,-4.42855],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (97.4934,'kcal/mol','+|-',1.69706),
        S298 = (0.750591,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 576,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O   ux r1 {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.754919,-0.902436,-1.18868,-1.69222,-2.58318,-3.29972,-4.45844],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (95.7638,'kcal/mol','+|-',1.69706),
        S298 = (0.628512,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OCC1O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 577,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.302737,-1.147,-1.88488,-2.45599,-3.14149,-3.69069,-4.61798],'cal/mol/K','+|-',[1.84994,2.8413,3.51465,3.72894,3.67582,3.75131,1.73234]),
        H298 = (95.4726,'kcal/mol','+|-',5.28034),
        S298 = (1.49519,'cal/mol/K','+|-',6.31343),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 578,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,S}
4   C ux {3,[S,D,T,B,Q]}
5   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0717785,-1.46283,-3.03713,-3.43373,-3.02927,-3.01747,-4.7685],'cal/mol/K','+|-',[2.76243,3.50449,3.99229,4.43214,6.16275,7.16999,4.33508]),
        H298 = (95.3804,'kcal/mol','+|-',12.1188),
        S298 = (5.87381,'cal/mol/K','+|-',8.30436),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 579,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,D} {5,S}
4   C ux {3,D}
5   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0641377,-2.12511,-3.89738,-4.45323,-4.64294,-4.94828,-5.68977],'cal/mol/K','+|-',[3.4536,3.27155,3.28366,3.31807,3.18301,3.16407,3.726]),
        H298 = (98.5769,'kcal/mol','+|-',6.07277),
        S298 = (3.86444,'cal/mol/K','+|-',6.13914),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 580,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_4BrCClFINPSSi-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D} {5,S}
4   C ux r1 {3,D}
5   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.55497,-2.42155,-4.21012,-4.80847,-4.77116,-4.91064,-6.38646],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.0767,'kcal/mol','+|-',4.17612),
        S298 = (5.72485,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OCC=C(C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 581,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_N-4BrCClFINPSSi-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D} {5,S}
4   C ux r0 {3,D}
5   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.426695,-1.82866,-3.58465,-4.09798,-4.51471,-4.98592,-4.99307],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.0771,'kcal/mol','+|-',4.17612),
        S298 = (2.00402,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CO[C](C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 582,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,S} {5,S}
4   C u0 r1 {3,S}
5   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0870601,-0.138283,-1.31661,-1.39474,0.198061,0.844151,-2.92597],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.9873,'kcal/mol','+|-',4.17612),
        S298 = (9.89257,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC(C)C(C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 583,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.377356,-1.3829,-2.08213,-2.68326,-3.36491,-3.90848,-4.63231],'cal/mol/K','+|-',[2.54818,3.75013,4.52385,4.83385,4.68203,4.62088,2.06894]),
        H298 = (94.914,'kcal/mol','+|-',6.56616),
        S298 = (1.91621,'cal/mol/K','+|-',6.84505),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 584,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.539528,-2.59033,-3.62924,-4.26774,-4.55097,-4.80398,-4.89079],'cal/mol/K','+|-',[3.93762,4.74002,5.56256,6.13066,6.60848,6.89613,3.18261]),
        H298 = (98.3774,'kcal/mol','+|-',6.91958),
        S298 = (4.9075,'cal/mol/K','+|-',6.44783),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 585,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.439169,-3.54607,-4.89501,-5.52875,-5.31821,-5.35846,-5.05043],'cal/mol/K','+|-',[4.8069,4.47214,4.7308,5.70309,7.52849,8.16843,3.84854]),
        H298 = (98.4725,'kcal/mol','+|-',9.46546),
        S298 = (6.45405,'cal/mol/K','+|-',5.14632),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 586,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.213572,-4.2338,-5.80148,-6.70302,-6.91783,-7.09592,-5.69815],'cal/mol/K','+|-',[5.39609,3.70417,2.75602,2.50257,2.64628,2.85135,2.86834]),
        H298 = (99.6546,'kcal/mol','+|-',9.00187),
        S298 = (6.32281,'cal/mol/K','+|-',5.87539),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 587,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H u0 r0 {4,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
7   C   ux r1 {4,[S,D,T,B,Q]} {8,S}
8   C   u0 r1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.92005,-3.56978,-5.26622,-6.25557,-6.2739,-6.56407,-4.82104],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (94.0107,'kcal/mol','+|-',4.17612),
        S298 = (5.3522,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCC(=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 588,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_N-7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]}
7   O   ux {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C   ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.355255,-4.45514,-5.9799,-6.85217,-7.13248,-7.2732,-5.99052],'cal/mol/K','+|-',[5.92266,4.30954,3.12987,2.83321,2.92662,3.25694,3.0751]),
        H298 = (101.536,'kcal/mol','+|-',5.80528),
        S298 = (6.64634,'cal/mol/K','+|-',6.95951),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 589,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_N-7R!H->C_6C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   ux r1 {3,S} {5,D} {7,S}
5   R!H ux {4,D}
6   C   u0 r1 {1,S}
7   O   u0 r1 {4,S} {8,[S,D,T,B,Q]}
8   C   ux r1 {7,[S,D,T,B,Q]}
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
    index = 590,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_N-7R!H->C_N-6C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H u0 {4,[S,D,T,B,Q]}
6   C   ux r0 {1,[S,D,T,B,Q]}
7   O   ux {4,[S,D,T,B,Q]} {8,S}
8   C   u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04456,-3.75008,-5.84839,-7.05999,-7.52456,-7.83181,-6.06231],'cal/mol/K','+|-',[4.44912,4.67766,3.98043,3.41823,3.17923,3.22381,3.93134]),
        H298 = (102.021,'kcal/mol','+|-',7.07961),
        S298 = (8.44927,'cal/mol/K','+|-',3.93996),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 591,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_N-7R!H->C_N-6C-inRing_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C u0 r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]}
6   C ux r0 {1,[S,D,T,B,Q]}
7   O ux r1 {4,[S,D,T,B,Q]} {8,S}
8   C u0 r1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15106,-4.96871,-6.70307,-7.51883,-7.64047,-7.61018,-5.23652],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (103.402,'kcal/mol','+|-',4.17612),
        S298 = (7.61836,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CO[C](C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 592,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_N-7R!H->C_N-6C-inRing_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C u0 r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O u0 r0 {4,[S,D,T,B,Q]}
6   C ux r0 {1,[S,D,T,B,Q]}
7   O ux r1 {4,[S,D,T,B,Q]} {8,S}
8   C u0 r1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0619349,-2.53145,-4.99371,-6.60115,-7.40865,-8.05344,-6.8881],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.641,'kcal/mol','+|-',4.17612),
        S298 = (9.28017,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COC(=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 593,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {6,S}
2   O                      ux r1 {1,S} {3,[S,T,Q,B]}
3   C                      ux r1 {2,[S,T,Q,B]} {4,S}
4   C                      ux r1 {3,S} {5,S}
5   O                      ux r1 {4,S}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 {1,S}
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
    index = 594,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-4BrCClFINPSSi-3R!H",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,[S,D,T,B,Q]}
5   R!H u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.149284,-0.441884,-0.903003,-1.4637,-2.47678,-3.25845,-4.46602],'cal/mol/K','+|-',[2.05176,2.06659,2.05193,2.02815,2.01173,2.00532,2.00135]),
        H298 = (94.1437,'kcal/mol','+|-',2.47063),
        S298 = (-0.510511,'cal/mol/K','+|-',2.06708),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 595,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-4BrCClFINPSSi-3R!H_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   C u0 r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0126232,-0.257902,-0.740828,-1.34464,-2.4001,-3.20684,-4.44002],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (93.9363,'kcal/mol','+|-',1.69706),
        S298 = (-0.695173,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 596,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-4BrCClFINPSSi-3R!H_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   O u0 r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.311191,-0.625866,-1.06518,-1.58277,-2.55346,-3.31005,-4.49202],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (94.3511,'kcal/mol','+|-',1.69706),
        S298 = (-0.325848,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 597,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-4BrCClFINPSSi-3R!H",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,D}
4   C   u0 {3,D} {5,[S,D,T,B,Q]}
5   R!H u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.362168,-0.512784,-0.940595,-1.52611,-2.47396,-3.21527,-4.41088],'cal/mol/K','+|-',[2.29442,2.30433,2.21472,2.11995,2.0572,2.02918,2.00839]),
        H298 = (92.5227,'kcal/mol','+|-',4.54809),
        S298 = (-0.143991,'cal/mol/K','+|-',2.00381),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 598,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-4BrCClFINPSSi-3R!H_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 r1 {3,D} {5,[S,D,T,B,Q]}
5   C u0 r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0353805,-0.108135,-0.604255,-1.27757,-2.30364,-3.09403,-4.34606],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (93.8886,'kcal/mol','+|-',1.69706),
        S298 = (-0.187667,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 599,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-4BrCClFINPSSi-3R!H_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 r1 {3,D} {5,[S,D,T,B,Q]}
5   O u0 r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.759716,-0.917434,-1.27693,-1.77465,-2.64427,-3.33651,-4.4757],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (91.1568,'kcal/mol','+|-',1.69706),
        S298 = (-0.100316,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1OC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 600,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.178144,-0.667693,-1.27609,-1.87573,-2.86431,-3.56776,-4.5656],'cal/mol/K','+|-',[1.66621,1.79177,1.92583,1.93472,1.8484,1.77198,1.65296]),
        H298 = (95.5076,'kcal/mol','+|-',2.61729),
        S298 = (-0.0177099,'cal/mol/K','+|-',1.7603),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 601,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_3R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S}
5   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.223889,-0.853419,-1.55318,-2.16081,-3.10411,-3.76085,-4.63889],'cal/mol/K','+|-',[2.0418,2.0639,2.05954,2.05,2.02971,2.0129,2.00057]),
        H298 = (95.4699,'kcal/mol','+|-',3.4273),
        S298 = (0.0404305,'cal/mol/K','+|-',2.18697),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 602,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_3R!H->C_Ext-1R-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {5,S}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,S}
4   C ux r1 {3,S}
5   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.369206,-1.03359,-1.72699,-2.31991,-3.22644,-3.84127,-4.62203],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (94.6049,'kcal/mol','+|-',1.69706),
        S298 = (0.353247,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 603,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_3R!H->C_Ext-1R-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {5,S}
2   O                      ux r1 {1,S} {3,[S,T,Q,B]}
3   C                      ux r1 {2,[S,T,Q,B]} {4,S}
4   C                      ux r1 {3,S}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.078573,-0.67325,-1.37936,-2.00171,-2.98178,-3.68042,-4.65576],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (96.335,'kcal/mol','+|-',1.69706),
        S298 = (-0.272386,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 604,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 {1,S} {3,S}
3   O u0 {2,S} {4,[S,D,T,B,Q]}
4   C u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.367034,-0.850833,-1.41631,-1.94425,-2.84259,-3.51673,-4.55607],'cal/mol/K','+|-',[2.03128,2.31709,2.56983,2.51535,2.33401,2.20399,2.04751]),
        H298 = (97.0703,'kcal/mol','+|-',2.77422),
        S298 = (-0.336204,'cal/mol/K','+|-',2.12194),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 605,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-3R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 r1 {3,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.492581,-1.26449,-1.98684,-2.48358,-3.26798,-3.84414,-4.71111],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (97.5622,'kcal/mol','+|-',1.69706),
        S298 = (-0.586859,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 606,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.81289,-0.119215,-1.20085,-2.00079,-3.12879,-3.87347,-5.18265],'cal/mol/K','+|-',[2.95879,2.78485,2.7876,2.7184,2.46387,2.18415,3.57995]),
        H298 = (103.781,'kcal/mol','+|-',3.26295),
        S298 = (0.734689,'cal/mol/K','+|-',4.35542),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 607,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.13028,0.0481116,-1.19888,-2.07138,-3.25883,-4.02293,-5.39801],'cal/mol/K','+|-',[3.10027,3.15857,3.26742,3.16587,2.80882,2.43721,4.07523]),
        H298 = (103.426,'kcal/mol','+|-',3.47154),
        S298 = (0.648815,'cal/mol/K','+|-',5.11436),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 608,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5977,0.342081,-1.13787,-2.14505,-3.47018,-4.27642,-5.79592],'cal/mol/K','+|-',[3.24573,3.74292,4.11837,3.98094,3.38826,2.80057,4.83385]),
        H298 = (103.409,'kcal/mol','+|-',4.5204),
        S298 = (1.16682,'cal/mol/K','+|-',6.0581),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 609,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R_4R!H->C_Ext-4C-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]}
4   C u0 r0 {1,S} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.560987,-1.41358,-2.72027,-3.28042,-3.86883,-4.33789,-9.72422],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.089,'kcal/mol','+|-',4.17612),
        S298 = (4.62555,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#C[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 610,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R_4R!H->C_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   O u0 {1,S} {3,S}
3   C u0 {2,S}
4   C ux {1,[S,D,T,B,Q]} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.02944,0.693212,-0.821392,-1.91798,-3.39045,-4.26413,-5.01026],'cal/mol/K','+|-',[2.41973,3.75448,4.43101,4.50519,3.9894,3.27987,2.10254]),
        H298 = (103.683,'kcal/mol','+|-',4.05565),
        S298 = (0.475076,'cal/mol/K','+|-',5.57516),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 611,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S}
4   C   ux {1,[S,D,T,B,Q]} {5,S}
5   O   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 612,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   O                      ux r1 {1,S} {3,[S,T,Q,B]}
3   C                      ux r1 {2,[S,T,Q,B]}
4   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00847871,-0.657415,-1.34531,-1.89455,-2.75157,-3.41457,-4.44303],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.463,'kcal/mol','+|-',1.69706),
        S298 = (-0.594401,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 613,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.970019,-2.07316,-3.29337,-4.20983,-5.34584,-6.19124,-7.41267],'cal/mol/K','+|-',[4.82108,6.5741,7.38943,7.92904,8.29911,8.1815,7.38523]),
        H298 = (85.3405,'kcal/mol','+|-',52.8332),
        S298 = (0.226171,'cal/mol/K','+|-',5.77354),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 614,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_N-3R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.50994,-3.11757,-4.84715,-6.02349,-7.30686,-8.26822,-9.57278],'cal/mol/K','+|-',[7.14986,9.20641,9.13873,9.19954,9.34417,8.43876,5.51265]),
        H298 = (69.6336,'kcal/mol','+|-',57.489),
        S298 = (-1.32765,'cal/mol/K','+|-',5.26113),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 615,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_N-3R!H->C_Ext-1R-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]}
4   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.89348,1.37289,-0.392098,-1.53662,-2.74439,-4.18058,-7.06387],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (104.471,'kcal/mol','+|-',4.17612),
        S298 = (1.03949,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 616,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_N-3R!H->C_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   O                      ux r1 {1,S} {3,[S,T,Q,B]}
3   O                      ux r1 {2,[S,T,Q,B]}
4   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8713,-4.91375,-6.62917,-7.81823,-9.13184,-9.90327,-10.5763],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (63.8806,'kcal/mol','+|-',1.69706),
        S298 = (-2.27451,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 617,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.121746,-1.30465,-2.16481,-2.77148,-3.40867,-3.9144,-5.37012],'cal/mol/K','+|-',[2.48716,3.82592,4.4861,4.73893,4.83783,5.06761,6.73716]),
        H298 = (93.722,'kcal/mol','+|-',56.5693),
        S298 = (3.13975,'cal/mol/K','+|-',4.17797),
    ),
    shortDesc = """Radical correction fitted to 29 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 618,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.277733,-1.91867,-2.96788,-3.61996,-4.24284,-4.7534,-6.74418],'cal/mol/K','+|-',[3.02642,4.29183,4.7189,4.64129,4.11206,3.83916,5.08416]),
        H298 = (99.9214,'kcal/mol','+|-',7.2746),
        S298 = (3.58764,'cal/mol/K','+|-',4.83236),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 619,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.847789,-2.80579,-3.78261,-4.28956,-4.68112,-5.05384,-7.16026],'cal/mol/K','+|-',[2.95046,4.12293,4.73602,4.73614,4.20892,3.8893,5.20376]),
        H298 = (99.0401,'kcal/mol','+|-',8.71139),
        S298 = (3.98518,'cal/mol/K','+|-',5.92185),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 620,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_4R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C u0 {1,S} {3,S}
3   O u0 {2,S}
4   O u0 {1,S}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.832098,-0.943168,-1.19561,-1.57449,-2.325,-3.01855,-4.32092],'cal/mol/K','+|-',[2.20447,2.12385,2.08383,2.07713,2.05482,2.02862,2.00025]),
        H298 = (98.0566,'kcal/mol','+|-',2.4735),
        S298 = (0.715387,'cal/mol/K','+|-',3.44041),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 621,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_4R!H->O_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S} {6,[S,D,T,B,Q]}
4   O   u0 r0 {1,S}
5   C   ux r1 {1,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.15991,-1.19584,-1.40248,-1.77276,-2.49168,-3.13861,-4.33216],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (98.2682,'kcal/mol','+|-',1.69706),
        S298 = (1.70511,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 622,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.854921,-3.65244,-4.95852,-5.52369,-5.75208,-5.97897,-8.45087],'cal/mol/K','+|-',[3.52645,3.80557,3.61113,3.3277,3.08855,3.14695,3.98726]),
        H298 = (100.123,'kcal/mol','+|-',11.7515),
        S298 = (5.47145,'cal/mol/K','+|-',4.23068),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 623,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C   ux {1,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.58549,-3.14027,-4.18365,-4.65372,-4.84168,-4.99153,-8.64249],'cal/mol/K','+|-',[3.60656,2.59868,2.51305,2.36474,2.22844,2.28232,4.25862]),
        H298 = (99.6941,'kcal/mol','+|-',4.28524),
        S298 = (5.88293,'cal/mol/K','+|-',5.45662),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 624,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C   ux {1,[S,D,T,B,Q]} {7,S}
5   C   u0 {1,S} {6,S}
6   O   u0 {3,[S,D,T,B,Q]} {5,S}
7   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05337,-3.06075,-3.95131,-4.53225,-4.95476,-5.11268,-9.49541],'cal/mol/K','+|-',[4.09176,3.47271,3.17753,3.04779,2.89807,2.96729,2.87233]),
        H298 = (99.5078,'kcal/mol','+|-',5.17408),
        S298 = (4.7313,'cal/mol/K','+|-',5.45857),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 625,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_Ext-4C-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {1,[S,D,T,B,Q]} {7,S}
5   C u0 r1 {1,S} {6,S}
6   O u0 r1 {3,[S,D,T,B,Q]} {5,S}
7   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.84728,-4.20854,-4.69748,-4.97634,-5.03057,-4.86275,-9.08289],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (99.1082,'kcal/mol','+|-',4.17612),
        S298 = (6.13982,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 626,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_Ext-4C-R_N-7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {1,[S,D,T,B,Q]} {7,S}
5   C u0 {1,S} {6,S}
6   O u0 {3,[S,D,T,B,Q]} {5,S}
7   O u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.15641,-2.48685,-3.57823,-4.3102,-4.91685,-5.23765,-9.70168],'cal/mol/K','+|-',[3.29283,3.58909,3.67688,3.74985,3.66467,3.72847,3.48513]),
        H298 = (99.7075,'kcal/mol','+|-',6.39983),
        S298 = (4.02704,'cal/mol/K','+|-',6.65997),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 627,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_Ext-4C-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {1,[S,D,T,B,Q]} {7,S}
5   C u0 r1 {1,S} {6,S}
6   O u0 r1 {3,[S,D,T,B,Q]} {5,S}
7   O u0 r0 {4,S} {8,S}
8   C u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.831839,-1.88669,-2.91495,-3.59769,-4.26208,-4.53931,-9.18373],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.8359,'kcal/mol','+|-',4.17612),
        S298 = (1.95475,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 628,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_Ext-4C-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_N-8R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,S}
2   C                      ux r1 {1,S} {3,[S,T,Q,B]}
3   O                      ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C                      ux {1,[S,D,T,B,Q]} {7,S}
5   C                      u0 r1 {1,S} {6,S}
6   O                      u0 r1 {3,[S,D,T,B,Q]} {5,S}
7   O                      u0 r0 {4,S} {8,S}
8   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.48097,-3.08702,-4.2415,-5.02272,-5.57162,-5.93599,-10.2196],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.579,'kcal/mol','+|-',4.17612),
        S298 = (6.09934,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 629,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {1,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.195112,-3.19175,-4.84483,-5.12762,-4.71658,-4.68768,-5.37717],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.067,'kcal/mol','+|-',4.17612),
        S298 = (9.07037,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C[C](C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 630,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {1,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.96245,-3.32733,-4.21949,-4.54422,-4.62756,-4.93195,-9.34906],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.8799,'kcal/mol','+|-',4.17612),
        S298 = (6.15038,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 631,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.802153,-3.16352,-4.82523,-5.60807,-5.94827,-6.28442,-8.2332],'cal/mol/K','+|-',[2.71461,2.31214,2.45551,2.50963,2.29076,2.45654,4.96254]),
        H298 = (97.4362,'kcal/mol','+|-',7.69493),
        S298 = (4.96045,'cal/mol/K','+|-',4.00333),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 632,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C u0 r1 {1,S} {3,S}
3   O u0 r1 {2,S} {6,S}
4   C u0 r1 {1,S} {7,S}
5   C u0 r0 {1,S}
6   C u0 r1 {3,S} {7,S}
7   C ux r1 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.138314,-2.19521,-4.08577,-5.30074,-6.0708,-7.10535,-6.43817],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (103.216,'kcal/mol','+|-',4.17612),
        S298 = (5.64968,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 633,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
6   O ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C u0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.968113,-3.4056,-5.01009,-5.68491,-5.91763,-6.07918,-8.68196],'cal/mol/K','+|-',[2.95933,2.28735,2.60667,2.81192,2.57651,2.56702,5.20885]),
        H298 = (95.9913,'kcal/mol','+|-',4.70268),
        S298 = (4.78814,'cal/mol/K','+|-',4.49932),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 634,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   O   ux r1 {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   u0 r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0935624,-3.4769,-6.00199,-6.93714,-6.65028,-6.01041,-10.0178],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.7847,'kcal/mol','+|-',4.17612),
        S298 = (2.21904,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(O)C[C](CO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 635,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-6R!H->C_Ext-7R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   O u0 {2,S} {6,S}
4   C u0 {1,S} {7,S}
5   C u0 {1,S}
6   O u0 {3,S} {7,S}
7   C u0 {4,S} {6,S} {8,[S,D,T,B,Q]}
8   C u0 {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.925129,-3.23086,-4.67549,-5.38522,-5.92208,-6.42061,-7.5437],'cal/mol/K','+|-',[3.38839,3.18147,3.1838,3.16623,3.25092,3.5084,7.44003]),
        H298 = (95.2674,'kcal/mol','+|-',6.36267),
        S298 = (6.30639,'cal/mol/K','+|-',3.16481),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 636,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-6R!H->C_Ext-7R!H-R_Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C u0 r1 {1,S} {3,S}
3   O u0 r1 {2,S} {6,S}
4   C u0 r1 {1,S} {7,S}
5   C u0 r0 {1,S}
6   O u0 r1 {3,S} {7,S}
7   C u0 r1 {4,S} {6,S} {8,S}
8   C u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.35541,-3.35421,-4.80617,-5.44112,-5.65551,-5.88339,-9.92472],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (94.4305,'kcal/mol','+|-',4.17612),
        S298 = (6.26167,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC(C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 637,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-6R!H->C_Ext-7R!H-R_N-Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C u0 r1 {1,S} {3,S}
3   O u0 r1 {2,S} {6,S}
4   C u0 r1 {1,S} {7,S}
5   C u0 r0 {1,S}
6   O u0 r1 {3,S} {7,S}
7   C u0 r1 {4,S} {6,S} {8,[B,D,T,Q]}
8   C u0 r0 {7,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.494843,-3.1075,-4.54482,-5.32932,-6.18865,-6.95783,-5.16268],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.1044,'kcal/mol','+|-',4.17612),
        S298 = (6.3511,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C[C](C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 638,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.968237,0.259806,-0.781368,-1.7613,-2.95147,-3.84291,-4.65518],'cal/mol/K','+|-',[2.40961,2.80608,3.85182,4.73769,5.08829,5.42141,3.36931]),
        H298 = (102.359,'kcal/mol','+|-',6.19824),
        S298 = (3.38997,'cal/mol/K','+|-',2.40185),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 639,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_4R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.815107,-0.482467,-2.30685,-3.82727,-5.22018,-6.30059,-5.85445],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (105.6,'kcal/mol','+|-',4.17612),
        S298 = (3.27196,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CC[CH]CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 640,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.58772,-0.724269,-1.98916,-2.85481,-3.78965,-4.4588,-6.86311],'cal/mol/K','+|-',[3.31721,3.47342,4.12423,4.50841,4.65103,4.72653,6.14445]),
        H298 = (100.271,'kcal/mol','+|-',5.06693),
        S298 = (2.55698,'cal/mol/K','+|-',2.05112),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 641,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0811167,-1.76431,-3.37706,-4.37851,-5.26434,-5.80284,-9.05408],'cal/mol/K','+|-',[4.16463,2.91181,2.60191,2.80753,3.50937,4.30449,2.90457]),
        H298 = (99.1646,'kcal/mol','+|-',7.36663),
        S298 = (2.46026,'cal/mol/K','+|-',2.76274),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 642,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
6   C   u0 r1 {1,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
    index = 643,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0724775,-1.93547,-3.54559,-4.45631,-4.9342,-5.11612,-9.69298],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.3165,'kcal/mol','+|-',4.17612),
        S298 = (2.9395,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC1(C)C[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 644,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.101094,-0.427477,-1.01756,-1.55936,-2.217,-2.71583,-3.40717],'cal/mol/K','+|-',[1.7779,2.42124,3.20734,4.04496,5.125,5.95268,7.20724]),
        H298 = (86.8295,'kcal/mol','+|-',83.5192),
        S298 = (2.4999,'cal/mol/K','+|-',2.93148),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 645,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.400415,-0.173813,-0.837925,-1.41856,-1.96688,-2.37372,-2.81026],'cal/mol/K','+|-',[2.01342,3.08437,4.27266,5.4638,6.92023,8.02671,9.63183]),
        H298 = (66.0832,'kcal/mol','+|-',109.83),
        S298 = (2.17078,'cal/mol/K','+|-',3.45068),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 646,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.492949,0.494302,0.400685,0.433362,0.899171,1.15159,1.43388],'cal/mol/K','+|-',[2.9952,4.52454,6.74979,8.41088,9.56899,11.3142,15.3145]),
        H298 = (16.5112,'kcal/mol','+|-',131.712),
        S298 = (2.14455,'cal/mol/K','+|-',3.02055),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 647,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.418563,-1.44595,-2.78752,-3.63959,-3.78066,-4.43393,-6.20629],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.4226,'kcal/mol','+|-',4.17612),
        S298 = (3.07716,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 648,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,S}
5   C   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.21985,-0.718711,-1.72696,-2.68918,-3.81137,-4.50643,-5.22211],'cal/mol/K','+|-',[2.48336,3.24766,3.65383,4.16436,4.57541,4.53913,3.45637]),
        H298 = (97.938,'kcal/mol','+|-',7.5487),
        S298 = (1.85398,'cal/mol/K','+|-',4.43421),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 649,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   R!H ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C   ux r1 {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.801046,-0.482768,-2.29708,-3.81123,-5.2,-6.28317,-5.84944],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (104.624,'kcal/mol','+|-',4.17612),
        S298 = (3.22327,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C[CH]CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 650,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   C u0 {3,[S,D,T,B,Q]} {5,S}
5   C u0 {4,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.541091,-2.03585,-3.11396,-4.1097,-5.19676,-5.56407,-6.14537],'cal/mol/K','+|-',[3.50194,3.61699,3.53654,4.0027,5.02973,5.38255,4.85225]),
        H298 = (96.9729,'kcal/mol','+|-',8.00389),
        S298 = (3.37492,'cal/mol/K','+|-',3.74841),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 651,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R-R_Sp-4R!H-3C",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 r1 {3,S} {5,S}
5   C u0 r1 {4,S}
6   C u0 {1,S}
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
    index = 652,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R-R_N-Sp-4R!H-3C",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 r1 {3,D} {5,S}
5   C u0 r1 {4,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00916313,-1.4151,-2.55415,-3.24212,-3.81391,-4.02411,-4.8442],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.063,'kcal/mol','+|-',4.17612),
        S298 = (2.66335,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 653,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   R!H u0 r1 {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
5   C   u0 r1 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.06966,0.484729,-0.283344,-0.911906,-1.85334,-2.98236,-4.39956],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (127.379,'kcal/mol','+|-',4.17612),
        S298 = (4.00495,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=CC[CH]CCC=1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 654,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S}
4   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.533149,-1.04462,-1.49564,-1.91001,-2.63198,-3.20228,-4.16267],'cal/mol/K','+|-',[2.23713,2.01565,2.05383,2.15165,2.26103,2.28546,2.15133]),
        H298 = (104.878,'kcal/mol','+|-',5.02474),
        S298 = (3.04495,'cal/mol/K','+|-',3.6018),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 655,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-1R-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S}
4   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.178754,-0.955987,-1.6608,-2.19054,-3.00486,-3.59333,-4.44289],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (106.438,'kcal/mol','+|-',1.69706),
        S298 = (4.10402,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 656,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,S}
3   C                      u0 r1 {2,S}
4   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.887544,-1.13325,-1.33048,-1.62948,-2.25911,-2.81124,-3.88245],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.317,'kcal/mol','+|-',1.69706),
        S298 = (1.98589,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 657,
    label = "RJ1_N-1R-inRing",
    group = 
"""
1 * R u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.779083,-1.7087,-2.37189,-2.7633,-3.16479,-3.52193,-4.27455],'cal/mol/K','+|-',[4.10185,4.78176,5.08148,5.03469,4.65673,4.34608,4.1428]),
        H298 = (94.5893,'kcal/mol','+|-',22.919),
        S298 = (0.378096,'cal/mol/K','+|-',10.5421),
    ),
    shortDesc = """Radical correction fitted to 2065 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 658,
    label = "RJ1_N-1R-inRing_1R->C",
    group = 
"""
1 * C u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0926535,-0.885033,-1.55945,-2.0404,-2.67107,-3.18171,-4.18443],'cal/mol/K','+|-',[3.31353,3.70072,4.01536,4.06275,3.87625,3.65116,3.55707]),
        H298 = (95.9801,'kcal/mol','+|-',20.9172),
        S298 = (0.968373,'cal/mol/K','+|-',10.3343),
    ),
    shortDesc = """Radical correction fitted to 1164 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=COC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)[CH]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]COCOO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC(C=C)CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN(OC(C=C)[CH2])CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C(C)C(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC1(CC=CC)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](C=O)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[CH]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COOC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)C1C=CC=C(C)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C=C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C=CON(CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC1=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC=C[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]OC - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
O=[C]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(CC=CC)CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=CC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C[CH]CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1OC1[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC#CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]OC)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)OOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1(C)OOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(CO)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=CO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C](C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1C=C(O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)OOC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C12COOC1(C)COO2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CO[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC(=C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC(OOCC(=C)C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(COO)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC(OO)C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC(O)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(COC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(C)(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)OOC(C)(C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN(OCC(C[CH]C=C)C=C)CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C=CCCC=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
C[CH]C(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[C]=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C - Radical thermo from pang.py and closed shell thermo from pang.py
CC[CH]C(CC)CC1=CCCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CCC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1(CC=CC)C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)CCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)OO - Radical thermo from pang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCC=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C=CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CC(CC=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C([CH]O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=COCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](CO)C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C]=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C=CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC(C)=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([CH]O)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC=CCC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OOC(O)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC(C)=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)CC(=C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCC1(CC=CC)C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CCCCO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC#C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=O)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CCCC1C([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOCC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)OCC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C=C[CH]C1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from pang.py
C[CH]C1=C=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=CC1([CH]O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]OC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
CC=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(C)=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CC(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C=COC(C)=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC[CH]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
CC(C)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]OC(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN([CH]C)O - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]OCC(C)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[CH2]CC(C)(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(CO)OOCC1(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1OOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(OO)C(=C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(C=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C=CCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=CC(=C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(O)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)CO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
O[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C](O)C(=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C[C](COO)C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)CC(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1CC=CC=C1C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCCC=CCC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH]=C1OOC(C)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COO)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C#CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]CCOO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
O[CH]C1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=COC - Radical thermo from johnson_g4.py and closed shell thermo from GAV
[CH2]C1=COC(O)C1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C(C)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(OO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CCC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C1C=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C#CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[C]#CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC=CCC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)OOC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C[CH]C(C)OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)COC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([C]=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(C)(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C1=CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(OC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(CC(=C)C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)CCC(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOC(OC(C)=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[C]=CC=CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)COOCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC1=C(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[C]#CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOCC(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)CC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C)=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C1CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)OOC1C=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C(C)C#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
CC=[C]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCOOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C12COOC1(C)C2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]C1CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[C](C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)OCC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=COC)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=[C]C(=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C([CH]O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C1C(O)OOC1(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCOOC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
O=C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(C)=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
O=[C]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC=CC#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OOC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC(O)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCOC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
O[CH]C(O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC=CC(C)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)CC(C)=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CO[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=COC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(COOC(C)(C)[C](C)C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=[C]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CO)C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)O[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]C1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC([CH]O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)CC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=CC(O)=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](CCOO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C1CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(COO)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)OO - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
O=[C]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)COC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C2OO2)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC[CH]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(=O)OCO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
C#C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(=O)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(COO)CCC(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(N(CC)O)C[CH]C=C - Radical thermo from pang.py and closed shell thermo from pang.py
CC(=O)O[CH]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)[C](O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC=CCC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C[C]=C(CO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]OC)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC1(C)CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](COO)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(=C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C(C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)OC(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CO[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC#CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]CC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCCCOO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=C([CH]O)C(=C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=O)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[C](C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C#CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
OC[C](O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(OOC(C)=O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([CH]CO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC([CH]COO)OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
O=C=C(O)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CO[CH]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC(CON(CC)CC)C=C - Radical thermo from pang.py and closed shell thermo from pang.py
C=C(C)[C](COO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C(O)O[C](O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(=C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([CH]C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(CC=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)C(C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C(C[CH]CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C(C)=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C1(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[C]=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(OC(=C)C1OO1)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C1C=COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]COOC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1=COCC1=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(COO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([C]=O)C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CO[C](O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C=C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(=C)COC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C1([C]=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC(O)=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
C=C[CH]OC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C](O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]CC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)CC=CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
C[C](O)OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC(=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(ON(CC)CC)C - Radical thermo from pang.py and closed shell thermo from pang.py
CC([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC(C=C)OO - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C(COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)C(=O)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]COC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
C[C]=CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)(C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
OC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=COC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)C1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C=CO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[C]=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC1CC(C)=CCC1C - Radical thermo from pang.py and closed shell thermo from GAV
C=C[CH]CC(C=C)CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCCC=C(C)CC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)C1C=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C=CC1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CO)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C(=O)C=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCOOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOC(C)(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C(C)=O)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)OOCC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)O[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([CH]OCOO)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[CH2]C(=C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OC[CH]C=C)CC - Radical thermo from pang.py and closed shell thermo from pang.py
O=[C]OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)C=C1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([CH]OC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(C)=O - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(COO)COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C=[C]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(OO)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC([CH2])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(CC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[C]#COC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)OOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
C=C(COO)[C](C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(OC(C)(C)[C](C)C)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(O)=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(=C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C1OOCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]COOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC(O)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]COOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C=CCCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCOOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C[CH]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)COC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)CCC(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(O)C#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)OOC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C=CCC(C=C)CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C[C]=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1COOC1[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO)C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)O[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC(C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C(C)[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[CH]CCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(N(CC)O)C(C=C)[CH2] - Radical thermo from pang.py and closed shell thermo from GAV
C=C[C]=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(COC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[C](CCOO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CO[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC=C(C)CC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[CH]OC=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=COC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C(O)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(COC(C)=O)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C(C)C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=CCC([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C)=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[CH2]OCCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=O)C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(OO)OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C=C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[CH]C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(OC(C)=O)OC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)OC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=O)C[C](C=O)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([CH]CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC=CC=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC(CC(=C)C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=CC(=O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(=C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC(=O)OC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CC)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C=C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[C](COO)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(OC)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
[CH2]C1(C)CC(=C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(=C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([CH]COO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([CH]O)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1CC(C)=CCC1C - Radical thermo from pang.py and closed shell thermo from GAV
CC([C]=O)C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]OCOO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
CC=C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1=C(OC)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC(C=C)OO - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C)(OO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COO)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(CO)OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]CC(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCCC(=C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CC=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C[CH]ON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
CC[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CCC([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CN(CC)O - Radical thermo from pang.py and closed shell thermo from pang.py
CO[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C(OO)C(O)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC#CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CCC#C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C]=O - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
[CH2]CCC(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C1OOC(OC(C)=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)OOC([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=CO)C(=C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CCC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C(O)O[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[CH2]C(C)=C(C=O)CC(=C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=CC)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCOOC([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COOCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=CC(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[CH]C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([CH]CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)(COO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(CC)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
[CH2]C1CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(=C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C(CCO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1(OC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C(=C)O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[C]#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]C(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(OC)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
[CH]=C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C(=C)C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=COC)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC(=C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[CH2]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=O)=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(OC1=COC=C1C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(=C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C=C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[C](COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CCC(C)=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1(C)CC(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(OC(=C)C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=COCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[C](O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC(=C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(O)C(CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]OCOOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC(C=C)CCC=CC - Radical thermo from pang.py and closed shell thermo from pang.py
C=CCC(=O)O[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](C)C(C)(C)CC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(C=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C)CC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCC(N(CC)O)C - Radical thermo from pang.py and closed shell thermo from pang.py
C[CH]C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
OC=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(O)C(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C(C)C[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC=CC(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C([CH]O)CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](CC=CC)CCC=CC - Radical thermo from pang.py and closed shell thermo from pang.py
CCC[CH]OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)O[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C=C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([C]=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([CH]O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[C](O)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(=C)OC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[C](C)CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(=O)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCCC(C=C)CC=C[CH]C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)C1C=C(C)C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(C)(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)OC1=COC=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C#C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)OOC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)C([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1(CC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CCC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)C=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH3] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[C](O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C)(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]C1OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C(C)COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(CCOO)OO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
[CH]=CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=CC=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([C]=O)OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
[CH2]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]CCOC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCCOC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C[CH]COO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(O)(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C(C)C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)CCC(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC=CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC(=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1(CC=CC)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOC1CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC1([CH]C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)=CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(CO)CC(C)(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](COO)C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCCC(C=C)C[CH]C=CC - Radical thermo from pang.py and closed shell thermo from GAV
O[CH]C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C(C)COOC(C)(C)C(C)(C)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[C]#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
O=[C]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 659,
    label = "RJ1_N-1R-inRing_N-1R->C",
    group = 
"""
1 * [N,O] u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.86461,-3.01125,-3.65668,-3.9065,-3.94558,-4.05996,-4.41708],'cal/mol/K','+|-',[4.2906,5.13109,5.5159,5.55376,5.31817,5.08246,4.91996]),
        H298 = (91.9618,'kcal/mol','+|-',25.4979),
        S298 = (-0.555375,'cal/mol/K','+|-',10.6057),
    ),
    shortDesc = """Radical correction fitted to 901 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C1CC(C)([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C(=O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC1([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1=COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CC2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C12OC1(O)O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC([O])C(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OOCC(O[O])C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1C=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1(O)OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(OC(C)=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=CCOC1(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C1(C)OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(COO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(COCOO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
CC(=O)OC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC1OC1(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CC1C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=COC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])CCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC1=CC(O[O])C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)OCC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[N]CC - Radical thermo from pang.py and closed shell thermo from GAV
[O]CC1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CO[O])=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OOC=C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)C(C)([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CCOC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CCO)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)CC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C=CC(OO)C(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C[O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=C([O])OOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=C(O)C(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(COO)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
[O]C1C=COCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C12OC1O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CC)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1(O)OOC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)COC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)OC(CC(C)O[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CC(=O)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC(C)(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1=C([O])OC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(O[O])C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(C=O)C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)OC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=C(C)C(O[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCCC1C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]C(O)(O)OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CCOCO1 - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
CC(=O)OCC(=O)CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CCC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1(C(=O)O)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1OCOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC1(O[O])CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(CCCO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1CCCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1(OO)COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCC([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)COOC(C)(C)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C(O)=COC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CC(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CC(=O)C(OO)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
C=CC(C)C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=C(O)C(O)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CCC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(=O)CC[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC(=O)OCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(CO)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCCCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COCC(C)[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
[O]OC1=COC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(CCO[O])OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
[O]CC1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1([O])CCCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN(O[O])CC - Radical thermo from pang.py and closed shell thermo from GAV
CC1(O[O])COOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CCC(C)(O[O])C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)CC(=C[O])C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C(O)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)(O[O])C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(=O)C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=C(C)O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C)CC1=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1CC(C)(CO[O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(O[O])C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C)OC=C1CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[N+](CC)[O-] - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)OCC([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C([O])OCO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
[O]C=C(O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(OC)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
[O]OC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=CCC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC=CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CCC(=O)OOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(CC(=O)OC=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C1OOCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCC1=CC(O[O])C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC1=CC=CCC1O[O] - Radical thermo from pang.py and closed shell thermo from GAV
CC1OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1OC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CCOO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(O)C(=CO)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COCCCO[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)([O])C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)CC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(=O)OC[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
[O]C1=CC=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CCC(=O)OC([O])O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C(O[O])OC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CCC(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OC1OC[O] - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
CC(=O)OC(COO)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC=CC(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CC=CC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C=CC(C)(O[O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COCC(COO)(OO)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC1C=CC(O[O])COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(COC(C)=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C(CC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(CC(C)OO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(CCCOO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)C=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O[O])C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C(OO)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CO[O] - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(OO)C(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C(=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CCO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=CC(OO)C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=COC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)C(O)COO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C=C(C(=O)O[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(OO)OCO[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C=C(C[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(OCO[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(=CO)C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCC(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(CO[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)(O[O])C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COOCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)(C=CC=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1COC(=O)C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CC=CC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1OOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(OO)COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(O)(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])(CO)C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1C(=O)OOC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=C(C)C([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)C=CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(C=O)CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCC(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(O)CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C1CC(=O)OC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C([O])C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(O)(C=O)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COCO[O])OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
CC=CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CC1=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCC(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)C=CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(=O)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC1(CO)OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1OCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)O[O] - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])C(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC(OO)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1CC(C)(O[O])COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CC[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(C)OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C(O)=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=COCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=CC)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(OO)=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1(COO)COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)CC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=C(C[O])CC(C)(C)C(C)(C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCC=O - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC(C)CO[O] - Radical thermo from pang.py and closed shell thermo from pang.py
CC(=O)OCC(CCO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OOC=C=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(COC(=O)CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])COOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)=CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])OC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C(CO[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN(OC1C=CC(C1)[O])CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C1OOC=C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CCO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(C=O)CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([O])C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(CCOO)O[O] - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
CC(=O)OC([O])C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=C(O)C(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CCC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(C=O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([O])C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(CC)[O] - Radical thermo from pang.py and closed shell thermo from pang.py
C=C(C[O])C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CC1(COO)COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CCC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC1CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)CC(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CO)=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=CC(OOC2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]C(=C=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC([O])C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(COO)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])CCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(OO)C(=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1(CO)COOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C(CO[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC1(C)COOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(C)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CCCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C=C([O])OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C1(O[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(O[O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)C(CCO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC([O])=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(O[O])=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[OH] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN(OC1CC=CC1[O])CC - Radical thermo from pang.py and closed shell thermo from GAV
CC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COC(C)=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC#CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC1OC1C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1OC(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OC(C)(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CCCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1([O])CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(OO)C(O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C1CC(O)=CC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=C(O)C=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(O)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CO)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)CC=C([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C1([O])CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC1OC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)OC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(=O)C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(C)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(OO)COC=C([O])O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C1(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CCC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)CCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(CCO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C)(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C=C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)(COO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=COC([O])=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C)CC(O[O])C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(CO[O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC#C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CCC(C=C)OO)O[O] - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)OCC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OCC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C(=O)O[O])C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=COC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(OO)C1CC(=O)OC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=CC=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CC(C)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])COC=O - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=C1C=CC(O[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(O)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=CC(=O)C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(O)CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(O[O])OCOO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from johnson_g4.py
C=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1(C=O)OC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(O)=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(=O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=C(CO[O])OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CC(C)(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1COC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(O)C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CO)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(CO[O])CCC(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1CCC(C)([O])O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(O)=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=O)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
CC(C)=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])COC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OC1O[O] - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
CC(C)(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC1(C)CC(O[O])COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1COC(C)([O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1([O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)C(C)(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(C=O)C1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)=CC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CC(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC1OC1CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1CC(C)([O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])C(C)(C)C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])C2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1ON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
CC1([O])CC=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1OOC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=COC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(CC)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OC1C=CC(C1)O[O])CC - Radical thermo from pang.py and closed shell thermo from pang.py
C#CC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])C=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
C=CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(C)(C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)OC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1OC1C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC([O])C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=COC(O[O])C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC#C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(CO[O])COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1CC1=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCOCO[O] - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from johnson_g4.py
C=C(C(O)O[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_1R-inRing
            L4: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Ext-4R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Ext-4R!H-R_Int-6R!H-1R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Ext-4R!H-R_Int-6R!H-1R_Ext-1R-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_4R!H->C_Ext-5R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_4R!H->C_Ext-5R!H-R_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_4R!H->C_Ext-1R-R_Ext-7R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_4R!H->C_Ext-1R-R_Ext-7R!H-R_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_N-4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_N-4R!H->C_Ext-3R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_N-4R!H->C_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_Sp-6R!H=5R!H_N-4R!H->C_Ext-1R-R_Ext-6R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C_6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C_6R!H->C_8R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C_6R!H->C_8R!H->C_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C_6R!H->C_N-8R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_4R!H->C_N-6R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R_N-4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_5R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-2R!H-R_Ext-3R!H-R_Ext-1R-R_N-Sp-6R!H=5R!H_N-5R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-3R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_Ext-1R-R_Ext-6R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-4O-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_Sp-7R!H-6R!H
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4O-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Sp-6R!H-5R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Sp-7R!H-6R!H
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_Ext-4O-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_N-Sp-6R!H-5R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4O-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_N-Sp-5R!H-3R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_4R!H->O_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-4O-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-1R-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-4C-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_Sp-7R!H=6C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H
                                                                                L21: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_Ext-6C-R
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing_Ext-7R!H-R_Sp-9R!H-7R!H
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing_Ext-7R!H-R_N-Sp-9R!H-7R!H
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_N-Sp-8R!H-7R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_Ext-7R!H-R_N-Sp-8R!H-7R!H_Ext-8R!H-R_Ext-8R!H-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-4C-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_8R!H-inRing
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_N-8R!H-inRing
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_7R!H->N
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_N-7R!H->N
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_N-7R!H->N_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_N-7R!H->N_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_6R!H->C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_6R!H->C_Ext-4C-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_6R!H->C_6C-inRing
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_6R!H->C_N-6C-inRing
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H->C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H->C_Ext-3R!H-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H->C_Ext-4C-R
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H->C_Ext-4C-R_7R!H->C
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H->C_Ext-4C-R_N-7R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_8R!H-inRing
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing_Ext-9R!H-R_Sp-11R!H-9R!H
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing_Ext-9R!H-R_N-Sp-11R!H-9R!H
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H_8R!H-inRing
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H_N-8R!H-inRing
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_Ext-3R!H-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing_Ext-8R!H-R_Ext-6C-R_Sp-10R!H-9R!H
                                                                                L21: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing_Ext-8R!H-R_Ext-6C-R_Sp-10R!H-9R!H_Ext-8R!H-R
                                                                                L21: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing_Ext-8R!H-R_Ext-6C-R_Sp-10R!H-9R!H_Ext-10R!H-R
                                                                                L21: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing_Ext-8R!H-R_Ext-6C-R_Sp-10R!H-9R!H_Ext-6C-R
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing_Ext-8R!H-R_Ext-6C-R_N-Sp-10R!H-9R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_N-6C-inRing
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_N-Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_N-Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_6C-inRing
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_6R!H->C_Ext-7BrCClFINPSSi-R_N-Sp-8R!H=7BrBrCCClClFFIINNPPSSSiSi_N-6C-inRing
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-6R!H-R_N-7R!H->O_N-6R!H->C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_6R!H->C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-6R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-1R-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-1R-R_Ext-6R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_Ext-6R!H-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_Ext-6R!H-R_6R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_Ext-6R!H-R_N-6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C_Ext-3R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C_Ext-3R!H-R_Ext-5C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-3R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-3R!H-R_Ext-6R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-1R-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R_Sp-6R!H-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R_N-Sp-6R!H-4C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Int-6R!H-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R_6R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R_N-6R!H-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Ext-8R!H-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Ext-8R!H-R_Ext-1R-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_N-6R!H-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing_Ext-5R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing_Ext-7R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing_Ext-5R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing_Ext-6R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_7R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_N-7R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_Ext-7C-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-5R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-3R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-1R-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-4C-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1R-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1R-R_Ext-7R!H-R_Ext-8R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-6O-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_N-5R!H-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_7R!H-inRing
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_7R!H-inRing_Ext-4C-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_7R!H-inRing_Int-7R!H-4C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_7R!H->C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_7R!H->C_Ext-1R-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_N-7R!H->C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_Sp-6CN-4C_N-7R!H-inRing_N-7R!H->C_Ext-3R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_7R!H->C_Ext-3R!H-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Ext-6CN-R_N-Sp-6CN-4C_Ext-7R!H-R_N-7R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-7C-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H-8R!H
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-4C-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-4C-R_8R!H->C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-4C-R_N-8R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_7R!H->C_Ext-5R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_N-7R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_Sp-9R!H-8C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_N-Sp-9R!H-8C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_N-8R!H->C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R_8R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R_N-8R!H->C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-5R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing_Ext-5R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R_Ext-7R!H-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-5R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_7R!H->O
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_N-7R!H->O
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Sp-11R!H=10R!H
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_N-Sp-11R!H=10R!H
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_N-7R!H->O
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_N-7R!H->O_Ext-4C-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_N-Sp-7R!H-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-4R!H->O_N-Sp-2R!H-1R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R_Ext-4R!H-R_Ext-6R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R_Ext-4R!H-R_Ext-6R!H-R_5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C_Ext-3C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C_Ext-4C-R_6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C_Ext-4C-R_N-6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Int-5R!H-4C_Ext-4C-R_N-6R!H->C_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C_2R!H-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C_2R!H-inRing_Ext-4C-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C_2R!H-inRing_Ext-4C-R_Ext-6C-R_Int-8R!H-7R!H
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C_2R!H-inRing_Ext-4C-R_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_6R!H->C_N-2R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_Ext-2R!H-R_N-6R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_2R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_4R!H->C_N-2R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-1R-R_N-4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_5R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_5R!H->O_Ext-2R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_5R!H->O_Ext-2R!H-R_Ext-4C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_5R!H->O_Int-4C-2R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Ext-5C-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Ext-5C-R_Ext-5C-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Ext-5C-R_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Int-6R!H-5C_Sp-6R!H-5C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Int-6R!H-5C_Sp-6R!H-5C_Sp-5C-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Int-6R!H-5C_Sp-6R!H-5C_N-Sp-5C-4C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-2R!H-R_Int-6R!H-5C_N-Sp-6R!H-5C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-3C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->O_Ext-5C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C_Ext-2R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C_Ext-2R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C_Ext-2R!H-R_Int-6R!H-5R!H_N-Sp-6R!H-5R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_4R!H->C_Ext-3C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_4R!H->C_Ext-3C-R_Ext-5R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_3R!H->C_N-4R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R_6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R_6R!H->C_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R_6R!H->C_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R_N-6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-2R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-4C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_Int-5R!H-1R_Ext-4C-R_Ext-4C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing_Int-6R!H-2R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing_Ext-2R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing_Ext-2R!H-R_6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_2R!H-inRing_Ext-2R!H-R_N-6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R_N-2R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-1R-R_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-4C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R_6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R_6R!H->C_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R_N-6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R_N-6R!H->C_Ext-1R-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-2R!H-R_N-6R!H->C_Ext-1R-R_Ext-5BrClFINOPSSi-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_2R!H-inRing_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_4R!H->C_Ext-4C-R_N-5R!H->C_N-2R!H-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-1R-R_2R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-1R-R_N-2R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-1R-R_N-2R!H-inRing_Ext-2R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_Ext-7R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_Ext-5C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_Sp-7R!H-5C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C_7R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_5R!H->C_Ext-4O-R_Ext-5C-R_N-Sp-7R!H-5C_N-7R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-4O-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-4O-R_Ext-5BrClFINOPSSi-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-4O-R_Ext-5BrClFINOPSSi-R_Int-7R!H-6R!H_Ext-7R!H-R_Ext-8R!H-R_8R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Sp-4R!H-1R_N-3R!H->C_N-4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-4O-R_Ext-5BrClFINOPSSi-R_Int-7R!H-6R!H_Ext-7R!H-R_Ext-8R!H-R_N-8R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_N-5R!H->C_Ext-2R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C
            L4: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Int-4C-1R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Int-4C-1R_Ext-3R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Int-4C-1R_Ext-3R!H-R_5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Int-4C-1R_Ext-3R!H-R_N-5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Int-4C-1R_Ext-2R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-3R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_N-5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-3R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-3R!H-R_Ext-2R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C_Ext-2R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-3R!H-R_N-4R!H->C_N-3R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-6R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->C_Ext-1R-R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->C
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_4R!H-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C_Ext-1R-R_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C_Ext-3C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_3R!H->C_N-4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_5R!H->C_Ext-5C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_5R!H->C_Ext-4R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_5R!H->C_Ext-4R!H-R_6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_5R!H->C_Ext-4R!H-R_N-6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_N-5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_N-5R!H->C_Ext-4R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_N-5R!H->C_4R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-1R-R_N-5R!H->C_N-4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_Ext-2R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_Ext-2R!H-R_4R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_Ext-2R!H-R_N-4R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_4R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_4R!H->C_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_4R!H->C_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_N-4R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_N-4R!H->C_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_Ext-4R!H-R_N-4R!H->C_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_4R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_4R!H->O_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_N-4R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-4R!H-inRing_N-3R!H->C_N-4R!H->O_Ext-2R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Int-8R!H-3R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R_5R!H-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R_5R!H-inRing_Ext-3R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R_N-5R!H-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R_N-5R!H-inRing_2R!H-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-9R!H-R_N-5R!H-inRing_N-2R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_Ext-3R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_3R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-1R-R_N-3R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-5R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-5R!H-R_3R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Ext-5R!H-R_Ext-5R!H-R_N-3R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_3R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_N-3R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_N-3R!H->O_7R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_N-3R!H->O_N-7R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-1R-R_Ext-7R!H-R_Ext-8R!H-R_3R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-1R-R_Ext-7R!H-R_Ext-8R!H-R_N-3R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_N-6R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_3R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_N-3R!H-inRing
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_4C-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_4C-inRing_Ext-4C-R_Sp-5R!H-4C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_4C-inRing_Ext-4C-R_N-Sp-5R!H-4C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-1R-R_5R!H->O
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-1R-R_N-5R!H->O
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-3O-R_Ext-5R!H-R_Ext-1R-R_N-5R!H->O_Ext-4C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-4C-R_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_3O-inRing_N-4C-inRing_Ext-4C-R_Ext-5R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-4C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-1R-R_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-5R!H-R_Ext-1R-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-5R!H-R_Ext-1R-R_Ext-5R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_Sp-10R!H-9R!H
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_Sp-10R!H-9R!H_Ext-10R!H-R_Ext-7R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_N-Sp-10R!H-9R!H
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_N-7R!H-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_7R!H-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_N-7R!H-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_Sp-5R!H=4C_Ext-3O-R_Ext-5R!H-R_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_5R!H->C_Ext-5C-R_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_N-5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_N-5R!H->C_Ext-1R-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_N-5R!H->C_Ext-1R-R_5O-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_N-5R!H->C_Ext-1R-R_5O-inRing_Ext-3O-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_4R!H->C_N-3O-inRing_Ext-4C-R_N-Sp-5R!H=4C_N-5R!H->C_Ext-1R-R_N-5O-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Int-4O-3O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Ext-1R-R_Ext-3O-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Ext-5C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Ext-5C-R_Ext-3O-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_5C-inRing_Ext-3O-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_5R!H->C_N-5C-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-4R!H->C_Ext-1R-R_N-5R!H->C_Ext-3O-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Int-4R!H-3C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Int-4R!H-3C_Ext-4R!H-R_Ext-5R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-4R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-4R!H-R_Ext-3C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-4R!H-R_4R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-4R!H-R_N-4R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Int-6C-3C_Ext-4R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R_Int-7R!H-4R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R_Int-7R!H-4R!H_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R_Int-7R!H-4R!H_Ext-4R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R_8R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-8R!H-R_N-8R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Int-8R!H-7R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_Ext-7R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_3C-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-3C-R_N-3C-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_6R!H->C_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_7R!H-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_7R!H-inRing_Ext-8R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_7R!H-inRing_6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_7R!H-inRing_N-6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_N-7R!H-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_N-7R!H-inRing_8R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_N-7R!H-inRing_N-8R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_N-7R!H-inRing_N-8R!H->C_6R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-1R-R_N-7R!H-inRing_N-8R!H->C_N-6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_2O-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_Sp-4O=3R!H_N-2O-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R_Int-4O-1R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R_Ext-1R-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R_Ext-1R-R_Ext-3R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R_4O-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-5R!H-R_N-4O-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-3R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-4O-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-4O-R_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-4O-R_N-5R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-4O-R_N-5R!H->C_4O-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_Ext-4O-R_N-5R!H->C_N-4O-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_4O-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_N-4O-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_N-4O-inRing_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-1R-R_N-4O-inRing_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_4R!H->O_N-Sp-4O=3R!H_Ext-3R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_4BrCClFINPSSi-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_N-4BrCClFINPSSi-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_7R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_N-7R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_N-7R!H->C_6C-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_N-7R!H->C_N-6C-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_N-7R!H->C_N-6C-inRing_5R!H->C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R_N-7R!H->C_N-6C-inRing_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_N-6R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-4BrCClFINPSSi-3R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-4BrCClFINPSSi-3R!H_5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-4BrCClFINPSSi-3R!H_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-4BrCClFINPSSi-3R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-4BrCClFINPSSi-3R!H_5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-4BrCClFINPSSi-3R!H_N-5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_3R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_3R!H->C_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_3R!H->C_Ext-1R-R_5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_3R!H->C_Ext-1R-R_N-5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-3R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-3R!H->C_Ext-1R-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R_4R!H->C_Ext-4C-R_5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R_4R!H->C_Ext-4C-R_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-5BrClFINOPSSi-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Ext-1R-R_N-4R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_N-3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_N-3R!H->C_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_N-3R!H->C_Ext-1R-R_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_N-3R!H->C_Ext-1R-R_N-4R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_4R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_4R!H->O_Ext-3O-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_Ext-4C-R_7R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_Ext-4C-R_N-7R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_Ext-4C-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_8R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_Ext-4C-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_N-8R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Int-6R!H-3O_N-6R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-6R!H->C_Ext-5R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-6R!H->C_Ext-7R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-6R!H->C_Ext-7R!H-R_Sp-8R!H-7R!H
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-6R!H->C_Ext-7R!H-R_N-Sp-8R!H-7R!H
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_4R!H->C_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_Ext-6R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_Ext-5R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R-R_Sp-4R!H-3C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R-R_N-Sp-4R!H-3C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-1R-R_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-1R-R_N-4R!H->C
        L3: RJ1_N-1R-inRing
            L4: RJ1_N-1R-inRing_1R->C
            L4: RJ1_N-1R-inRing_N-1R->C
"""
)

