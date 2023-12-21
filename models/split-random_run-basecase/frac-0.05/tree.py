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
        Cpdata = ([-0.677831,-1.72995,-2.4275,-2.83871,-3.25947,-3.61416,-4.3923],'cal/mol/K','+|-',[3.49316,4.13815,4.52882,4.57161,4.26887,4.02883,4.28284]),
        H298 = (91.8361,'kcal/mol','+|-',36.0453),
        S298 = (0.445098,'cal/mol/K','+|-',9.74929),
    ),
    shortDesc = """Radical correction fitted to 127 radicals""",
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
        Cpdata = ([-0.677831,-1.72995,-2.4275,-2.83871,-3.25947,-3.61416,-4.3923],'cal/mol/K','+|-',[3.49316,4.13815,4.52882,4.57161,4.26887,4.02883,4.28284]),
        H298 = (91.8361,'kcal/mol','+|-',36.0453),
        S298 = (0.445098,'cal/mol/K','+|-',9.74929),
    ),
    shortDesc = """Radical correction fitted to 127 radicals""",
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
        Cpdata = ([-0.520151,-1.41785,-2.07581,-2.39754,-2.68952,-2.89155,-3.50695],'cal/mol/K','+|-',[3.74297,4.79563,5.37057,5.27165,4.47525,3.86391,4.35624]),
        H298 = (79.7931,'kcal/mol','+|-',43.6355),
        S298 = (0.36353,'cal/mol/K','+|-',10.6577),
    ),
    shortDesc = """Radical correction fitted to 49 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0490852,-0.64597,-1.26858,-1.48703,-1.70286,-1.97021,-2.55413],'cal/mol/K','+|-',[2.67987,2.66069,3.34047,3.73597,4.51505,5.32687,6.79605]),
        H298 = (59.0254,'kcal/mol','+|-',83.6989),
        S298 = (-1.10753,'cal/mol/K','+|-',7.72001),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0132801,-1.13627,-2.0507,-2.44386,-2.91172,-3.30364,-4.06465],'cal/mol/K','+|-',[2.76701,2.04383,2.11658,1.78313,1.32375,1.65939,1.8029]),
        H298 = (77.0791,'kcal/mol','+|-',8.57867),
        S298 = (-1.86573,'cal/mol/K','+|-',9.01709),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C u0 {3,S} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.263523,-0.910334,-1.46269,-1.89612,-2.49647,-2.90452,-3.87484],'cal/mol/K','+|-',[1.90734,0.958973,0.520032,0.572004,1.40078,2.2738,2.71456]),
        H298 = (74.5938,'kcal/mol','+|-',0.249444),
        S298 = (0.699715,'cal/mol/K','+|-',3.56407),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S} {6,[S,D,T,B,Q]}
4   C   u0 r1 {3,S} {5,D}
5   C   ux r1 {4,D}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.670186,-0.440882,-1.20812,-1.61611,-1.81074,-1.79142,-2.54597],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.7392,'kcal/mol','+|-',5.2),
        S298 = (-1.04502,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=C[CH]CC=C1)CC from Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 7,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.116846,-1.25376,-2.35646,-2.72869,-3.12765,-3.51118,-4.16336],'cal/mol/K','+|-',[3.36251,2.5311,2.42471,1.97706,1.26927,1.54574,1.75531]),
        H298 = (78.7068,'kcal/mol','+|-',10.044),
        S298 = (-3.19977,'cal/mol/K','+|-',10.1585),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.700631,-1.24056,-2.76462,-3.14635,-3.37998,-3.61981,-3.96012],'cal/mol/K','+|-',[3.61129,3.20121,2.63414,1.91563,1.27843,1.90999,2.07795]),
        H298 = (82.8077,'kcal/mol','+|-',5.05448),
        S298 = (-5.48366,'cal/mol/K','+|-',9.37204),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 9,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   u0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   O   u0 {4,S} {6,S}
6   R!H u0 {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.905903,-1.2019,-2.75761,-2.93419,-3.10314,-3.43854,-3.23458],'cal/mol/K','+|-',[5.62783,4.57381,3.593,2.31643,0.850456,2.2568,1.49891]),
        H298 = (81.7463,'kcal/mol','+|-',7.55759),
        S298 = (-9.461,'cal/mol/K','+|-',2.7778),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 10,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,S}
5   O   u0 {4,S} {6,S}
6   R!H u0 {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
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
C=C(C)COC1C=C[C](C)CC1OO from Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 11,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {7,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux r1 {4,[S,T,Q,B]} {6,S}
6   C   ux r1 {5,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.42508,-2.386,-3.7657,-4.14297,-4.26444,-4.61697,-5.22003],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.4357,'kcal/mol','+|-',5.2),
        S298 = (-2.08528,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]C(C)=CCC1 from Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 12,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,S}
5   R!H u0 {4,S} {6,[B,D,T,Q]}
6   R!H u0 {5,[B,D,T,Q]}
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
CC1=CCC=C[CH]1 from Radical thermo from pang.py and closed shell thermo from Thermo library: ../data/pang.py
""",
)

entry(
    index = 13,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_N-3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   u0 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.18849,0.45,0.479676,0.65178,0.999297,1.0104,0.822319],'cal/mol/K','+|-',[3.17774,3.00225,3.09522,3.49929,4.56309,6.33913,9.91258]),
        H298 = (20.2213,'kcal/mol','+|-',143.055),
        S298 = (0.58729,'cal/mol/K','+|-',1.93184),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 14,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_N-3R!H-inRing_2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.721591,1.09053,1.00824,1.049,1.2922,1.41438,1.76198],'cal/mol/K','+|-',[2.74514,0.691025,2.6001,4.0735,5.95804,8.28276,12.1836]),
        H298 = (5.17691,'kcal/mol','+|-',132.634),
        S298 = (0.221221,'cal/mol/K','+|-',1.27628),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 15,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_N-3R!H-inRing_2R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.124326,0.940182,1.57394,1.93528,2.5885,3.21647,4.4128],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (-11.2929,'kcal/mol','+|-',2.4),
        S298 = (-0.0564621,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]CCC1 from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 16,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_N-3R!H-inRing_2R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C                      u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C                      ux r0 {2,D}
4   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {1,S}
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
C=C1[CH]OC(O)C1=C from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_N-3R!H-inRing_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   u0 r0 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
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
O=C(OO)[C]1CC1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 18,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing",
    group = 
"""
1 * R   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.661816,-1.60995,-2.27671,-2.62414,-2.93507,-3.12084,-3.74408],'cal/mol/K','+|-',[3.94529,5.15133,5.73467,5.54095,4.39382,3.35394,3.49653]),
        H298 = (84.8242,'kcal/mol','+|-',19.1094),
        S298 = (0.72963,'cal/mol/K','+|-',11.2464),
    ),
    shortDesc = """Radical correction fitted to 39 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 19,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.302003,-0.977968,-1.58584,-1.98361,-2.46245,-2.812,-3.51041],'cal/mol/K','+|-',[2.92753,4.22314,5.17308,5.3595,4.54449,3.45812,3.38356]),
        H298 = (85.99,'kcal/mol','+|-',16.3172),
        S298 = (0.305168,'cal/mol/K','+|-',12.3628),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 20,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.121738,-0.215493,-0.376949,-0.610244,-1.18731,-1.87608,-3.11119],'cal/mol/K','+|-',[2.71346,2.89407,3.46421,3.7659,3.62583,2.93041,2.20083]),
        H298 = (90.1484,'kcal/mol','+|-',10.0152),
        S298 = (-0.970841,'cal/mol/K','+|-',13.8908),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 21,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.336352,-0.292104,-0.32372,-0.526681,-1.13552,-1.89707,-3.16138],'cal/mol/K','+|-',[1.99503,3.30906,4.20853,4.6392,4.54197,3.69499,2.59081]),
        H298 = (88.098,'kcal/mol','+|-',3.4063),
        S298 = (-2.51718,'cal/mol/K','+|-',9.71081),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 22,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.203621,0.59478,0.62284,0.297862,-0.697858,-1.82319,-3.45414],'cal/mol/K','+|-',[1.70217,2.95336,4.46336,5.48995,5.79874,4.53491,2.57847]),
        H298 = (88.3862,'kcal/mol','+|-',4.08588),
        S298 = (-3.65685,'cal/mol/K','+|-',11.8612),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 23,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {4,S}
3   C   u0 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   u0 {2,S} {6,[S,D,T,B,Q]}
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
[CH2]C(COO)=C(C)COO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 24,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R_2R!H-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.609961,-0.149017,-0.25084,-0.732145,-1.60128,-2.2944,-3.4619],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (87.0324,'kcal/mol','+|-',2.4),
        S298 = (-1.81321,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CCC=C1 from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 25,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 {2,S} {6,[S,D,T,B,Q]}
5   R!H u0 {3,[S,D,T,B,Q]}
6   O   u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.414108,0.218366,-0.129474,-0.655334,-1.83596,-2.85931,-4.103],'cal/mol/K','+|-',[1.08748,0.160715,0.450178,0.85804,0.429095,0.824841,2.28901]),
        H298 = (89.9833,'kcal/mol','+|-',0.210767),
        S298 = (-1.32776,'cal/mol/K','+|-',1.10658),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 26,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-2R!H-inRing_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   C u0 r0 {2,S} {6,[S,D,T,B,Q]}
5   C u0 r0 {3,[S,D,T,B,Q]}
6   O u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.177504,0.183399,-0.0315283,-0.468649,-1.7426,-2.67985,-3.60498],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (89.9571,'kcal/mol','+|-',2.4),
        S298 = (-1.56852,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C=O)=CC from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 27,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-2R!H-inRing_N-5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   C u0 r0 {2,S} {6,[S,D,T,B,Q]}
5   O u0 r0 {3,[S,D,T,B,Q]}
6   O u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.946468,0.297041,-0.349852,-1.07537,-2.04602,-3.2631,-5.22356],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.1062,'kcal/mol','+|-',5.2),
        S298 = (-0.786046,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=C=O)COO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 28,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,S}
4   R!H ux r0 {2,[S,D,T,B,Q]}
5   C   ux {3,S}
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
C=CC=C(O)[CH]O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 29,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_3R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D} {5,S}
4   C ux r0 {2,[S,D,T,B,Q]}
5   C ux {3,S}
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
[CH2]C(C)=C1CC1O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 30,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_N-3R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r0 {2,D} {5,S}
4   C ux r0 {2,[S,D,T,B,Q]}
5   C ux {3,S}
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
[CH2]C(C)=CCC(=O)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 31,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_3R!H->C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   R!H ux r0 {2,[S,D,T,B,Q]}
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
C=C=CC[C](C)C(=C)C from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 32,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_N-3R!H->C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0272584,-0.00275128,-0.280216,-0.555643,-1.13557,-1.8517,-3.27342],'cal/mol/K','+|-',[4.65225,2.81643,1.82682,1.29596,0.410502,0.330284,0.977878]),
        H298 = (96.6779,'kcal/mol','+|-',11.754),
        S298 = (-1.99438,'cal/mol/K','+|-',3.57648),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 33,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_N-3R!H->C_Ext-1C-R",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]} {5,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
5   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.60448,-0.811237,-0.642197,-0.704946,-1.13746,-1.76211,-2.87235],'cal/mol/K','+|-',[3.97292,3.26393,2.58024,2.00253,0.660374,0.4013,0.210239]),
        H298 = (90.5594,'kcal/mol','+|-',1.31537),
        S298 = (-2.66936,'cal/mol/K','+|-',5.12075),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 34,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_N-3R!H->C_Ext-1C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {5,S}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux r0 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   u0 r0 {1,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.199835,0.342736,0.270056,0.0030552,-0.903978,-1.90399,-2.79802],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.0944,'kcal/mol','+|-',5.2),
        S298 = (-4.47982,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(=O)[CH]C from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 35,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.572619,-1.63247,-2.52495,-3.00987,-3.39182,-3.51276,-3.85814],'cal/mol/K','+|-',[2.78199,4.54586,5.4848,5.54258,4.37727,3.23676,3.94665]),
        H298 = (83.2676,'kcal/mol','+|-',17.8215),
        S298 = (0.282398,'cal/mol/K','+|-',7.81745),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 36,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.403659,-0.0995924,-0.800819,-1.37739,-2.20379,-2.76717,-3.4384],'cal/mol/K','+|-',[2.26121,2.23347,2.15436,2.20295,2.15802,2.23303,2.22262]),
        H298 = (89.3033,'kcal/mol','+|-',27.4443),
        S298 = (0.274629,'cal/mol/K','+|-',9.93849),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 37,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux {2,D} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.721222,0.486398,-0.215593,-0.807822,-1.66475,-2.28464,-3.09433],'cal/mol/K','+|-',[2.45253,1.11844,0.854633,1.18279,1.31667,1.82519,2.32733]),
        H298 = (80.6128,'kcal/mol','+|-',8.68204),
        S298 = (-2.43298,'cal/mol/K','+|-',3.83988),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 38,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {5,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,D}
3   C   u0 {2,D} {4,S}
4   C   ux {3,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.23777,0.806442,0.0789907,-0.51296,-1.43127,-1.82283,-1.61316],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.4602,'kcal/mol','+|-',5.2),
        S298 = (-4.49643,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CO[CH]C=CC=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 39,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux {2,D} {4,S}
4   C ux {3,S} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00752268,0.2478,-0.213149,-0.645099,-1.38686,-1.96468,-3.03575],'cal/mol/K','+|-',[1.09134,1.38784,1.20174,1.13708,0.188532,0.918978,0.296946]),
        H298 = (80.2029,'kcal/mol','+|-',0.546719),
        S298 = (-2.04823,'cal/mol/K','+|-',4.89424),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 40,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-4R!H-R_5R!H->C_4R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux {2,D} {4,S}
4   C ux r1 {3,S} {5,S}
5   C ux r1 {4,S}
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
[CH2]C=CC1=CC1 from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 41,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-4R!H-R_5R!H->C_N-4R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   C ux {2,D} {4,S}
4   C ux r0 {3,S} {5,S}
5   C ux r1 {4,S}
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
[CH2]C=CCC1C=CC2C3C=CC(C3)C12 from Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 42,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D}
3   C                      u0 r0 {2,D} {4,S}
4   C                      u0 {3,S} {5,S}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 {4,S}
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
[CH2]C=CCOO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 43,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_N-Sp-4R!H-3R!H",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux r0 {2,D} {4,[B,D,T,Q]}
4   C u0 {3,[B,D,T,Q]}
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
C=[C]C=C=CC from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 44,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_4R!H-inRing",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   O   ux {2,D}
4   R!H ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18378,-3.9379,-6.08565,-6.83252,-6.1961,-5.38133,-9.3311],'cal/mol/K','+|-',[4.92982,13.78,17.2791,17.5811,13.7976,10.4263,4.49781]),
        H298 = (90.9302,'kcal/mol','+|-',2.42629),
        S298 = (2.94621,'cal/mol/K','+|-',18.1592),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 45,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_4R!H-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   O   ux {2,D}
4   R!H ux r1 {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
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
C[C](C=O)C1(C)OCOO1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 46,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   R!H ux {2,D}
4   R!H ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00067,-2.11569,-2.93264,-3.33256,-3.62352,-3.64291,-3.31092],'cal/mol/K','+|-',[2.4553,2.96905,3.30701,3.30109,2.77671,1.95153,1.5855]),
        H298 = (79.864,'kcal/mol','+|-',8.85323),
        S298 = (-0.0873815,'cal/mol/K','+|-',5.54741),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 47,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   C   ux {2,D}
4   R!H ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0783191,-1.0525,-1.78175,-2.13527,-2.60672,-3.01036,-3.684],'cal/mol/K','+|-',[1.67227,1.93334,2.28509,2.15798,2.02873,1.90866,1.61312]),
        H298 = (83.3258,'kcal/mol','+|-',6.02168),
        S298 = (-0.0341634,'cal/mol/K','+|-',8.02017),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 48,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   R!H ux r0 {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
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
C=C[C](C=O)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 49,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,D}
3   C ux {2,D}
4   C ux r0 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.230081,-1.11852,-2.08688,-2.50678,-2.98235,-3.36382,-4.13897],'cal/mol/K','+|-',[1.84265,2.53616,3.00727,2.84934,2.62849,2.44394,0.482609]),
        H298 = (83.5451,'kcal/mol','+|-',7.33255),
        S298 = (1.86295,'cal/mol/K','+|-',6.14008),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 50,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-4R!H-R_Sp-5R!H#4R!H",
    group = 
"""
1 * C u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D}
4   C u0 r0 {1,[S,D,T,B,Q]} {5,T}
5   C u0 {4,T}
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
C=C[CH]C#CC from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 51,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-4R!H-R_N-Sp-5R!H#4R!H",
    group = 
"""
1 * C u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,D}
3   C ux {2,D}
4   C ux r0 {1,[S,D,T,B,Q]} {5,[S,D,Q,B]}
5   C ux {4,[S,D,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.160108,-1.66391,-2.72115,-3.11983,-3.54153,-3.87897,-4.20618],'cal/mol/K','+|-',[0.52136,0.392834,0.923412,0.423822,0.661864,0.758512,0.50512]),
        H298 = (84.5815,'kcal/mol','+|-',1.36931),
        S298 = (1.98018,'cal/mol/K','+|-',8.3621),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 52,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-4R!H-R_N-Sp-5R!H#4R!H_Sp-4R!H-1C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux {2,D}
4   C ux r0 {1,S} {5,[S,D,Q,B]}
5   C ux {4,[S,D,Q,B]}
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
C=C[CH]CC1C=CCCC1 from Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 53,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-Sp-4R!H-1C",
    group = 
"""
1 * C u1 r0 {2,S} {4,D}
2   C ux {1,S} {3,D}
3   C ux {2,D}
4   C ux r0 {1,D} {5,[S,D,Q,B]}
5   C ux {4,[S,D,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.273541,-1.57844,-2.52024,-3.02762,-3.68553,-4.044,-4.31608],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (84.7515,'kcal/mol','+|-',2.4),
        S298 = (3.79953,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=[C]C=C from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 54,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_N-3R!H->C",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   O   u0 {2,D}
4   R!H u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.02551,-3.29701,-4.2114,-4.66288,-4.7533,-4.34575,-2.89639],'cal/mol/K','+|-',[0.939141,1.82696,2.11879,1.88971,1.09604,0.303923,1.25162]),
        H298 = (76.8187,'kcal/mol','+|-',5.76458),
        S298 = (-0.146513,'cal/mol/K','+|-',1.27763),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 55,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_N-3R!H->C_Ext-1C-R",
    group = 
"""
1 * C     u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C     u0 {1,S} {3,D}
3   O     u0 {2,D}
4   [C,O] u0 r0 {1,S}
5   [C,O] ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.29105,-3.78175,-4.78745,-5.19833,-5.06457,-4.43298,-2.66082],'cal/mol/K','+|-',[0.267629,1.01786,1.00727,0.5108,0.278101,0.0460895,1.34212]),
        H298 = (75.2715,'kcal/mol','+|-',3.00104),
        S298 = (0.000814883,'cal/mol/K','+|-',1.65643),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 56,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_N-3R!H->C_Ext-1C-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C u0 r0 {1,S} {3,D}
3   O u0 r0 {2,D}
4   O u0 r0 {1,S}
5   C ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
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
CC[C](O)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 57,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_N-3R!H->C_Ext-1C-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C                      u0 r0 {1,S} {3,D}
3   O                      u0 r0 {2,D}
4   O                      u0 r0 {1,S}
5   C                      ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,[S,D,T,B,Q]}
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
O=C[C](O)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 58,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_N-Sp-2R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux r0 {1,D} {3,D}
3   R!H ux r0 {2,D}
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
[CH]=C=CCO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 59,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.67301,-3.38602,-4.2183,-4.42427,-4.26332,-3.98879,-4.40078],'cal/mol/K','+|-',[5.65653,6.04139,5.67616,4.54175,2.62815,2.42792,3.65179]),
        H298 = (80.7573,'kcal/mol','+|-',26.6914),
        S298 = (1.92252,'cal/mol/K','+|-',7.34117),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 60,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.61216,-3.40817,-4.26384,-4.455,-4.24233,-3.91769,-4.30396],'cal/mol/K','+|-',[5.872,6.29078,5.90148,4.72466,2.73252,2.46355,3.72337]),
        H298 = (79.1771,'kcal/mol','+|-',23.0897),
        S298 = (2.14368,'cal/mol/K','+|-',7.43716),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 61,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_2R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.87603,-2.46289,-2.87295,-3.06455,-3.07767,-3.01395,-4.11265],'cal/mol/K','+|-',[0.710165,2.70688,3.49454,3.18842,2.32807,1.31464,2.05612]),
        H298 = (71.1408,'kcal/mol','+|-',22.4636),
        S298 = (1.46952,'cal/mol/K','+|-',11.4905),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 62,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_2R!H-inRing_Ext-3C-R_Ext-4R!H-R_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C u0 {2,D}
4   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72343,-2.0594,-2.3554,-2.60654,-2.76819,-2.92577,-3.67877],'cal/mol/K','+|-',[0.11668,2.68332,3.48416,3.26076,2.51188,1.70892,0.625253]),
        H298 = (71.2667,'kcal/mol','+|-',30.7968),
        S298 = (-0.827084,'cal/mol/K','+|-',6.02843),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 63,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_2R!H-inRing_Ext-3C-R_Ext-4R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {2,S}
5   C u0 r1 {3,S}
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
[O]C1=CCOOC1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 64,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_2R!H-inRing_Ext-3C-R_Ext-4R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_N-5R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,[S,D,T,B,Q]}
2   C                      ux r1 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C                      u0 r1 {2,D} {5,S}
4   C                      u0 r1 {2,S}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.74882,-1.47559,-1.59735,-1.89709,-2.22168,-2.55396,-3.54274],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (67.4425,'kcal/mol','+|-',2.4),
        S298 = (-2.1387,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=COOC1 from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 65,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_2R!H-inRing_Ext-3C-R_Ext-4R!H-R_N-4R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,[S,D,T,B,Q]}
2   C                      ux r1 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C                      u0 r1 {2,D}
4   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {2,S}
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
CC1C=C([O])OC1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 66,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.49093,-3.84248,-4.90289,-5.09386,-4.77745,-4.33292,-4.39186],'cal/mol/K','+|-',[7.21473,7.4164,6.55312,4.95957,2.3138,2.47306,4.42614]),
        H298 = (83.7775,'kcal/mol','+|-',20.7849),
        S298 = (2.45344,'cal/mol/K','+|-',6.29965),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 67,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.129588,-2.59331,-4.14773,-4.76757,-5.06759,-4.85347,-4.06645],'cal/mol/K','+|-',[9.87419,11.4761,10.4277,7.52587,1.91557,1.87297,4.50569]),
        H298 = (85.1263,'kcal/mol','+|-',10.1261),
        S298 = (2.40195,'cal/mol/K','+|-',5.18589),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 68,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.77007,-7.31784,-8.46242,-7.88163,-5.81866,-4.1971,-2.21871],'cal/mol/K','+|-',[4.74889,1.89115,0.345098,0.236927,0.986446,1.6029,0.976112]),
        H298 = (90.3255,'kcal/mol','+|-',3.1403),
        S298 = (0.591854,'cal/mol/K','+|-',4.48286),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 69,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r0 {2,D} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
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
C=CC([O])=CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 70,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->O",
    group = 
"""
1 * O                      u1 r0 {2,[S,D,T,B,Q]}
2   C                      ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C                      u0 {2,D} {4,S}
4   [Cl,C,Si,S,N,P,F,I,Br] u0 r0 {3,S}
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
[O]C=CCCOO from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 71,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77368,-4.34137,-5.45693,-5.64045,-5.11334,-4.71378,-6.02014],'cal/mol/K','+|-',[4.12618,3.80343,4.08082,4.22632,2.81691,1.85501,4.65255]),
        H298 = (92.6491,'kcal/mol','+|-',5.86028),
        S298 = (3.21998,'cal/mol/K','+|-',7.95794),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 72,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-4C-R",
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
        Cpdata = ([-2.24365,-4.86089,-6.03354,-6.24508,-5.50158,-4.9563,-6.8789],'cal/mol/K','+|-',[5.36187,4.73863,5.03256,5.19133,3.50034,2.3389,5.05894]),
        H298 = (93.8977,'kcal/mol','+|-',5.59216),
        S298 = (3.87812,'cal/mol/K','+|-',10.7825),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 73,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-4C-R_4C-inRing",
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
C=C([O])C1(OO)CO1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 74,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-4C-R_N-4C-inRing",
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
C=C([O])C(C)(C)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 75,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.51039,-5.74865,-5.67656,-4.96732,-3.65708,-2.65547,-2.64093],'cal/mol/K','+|-',[2.94329,2.94314,2.88402,2.75829,2.08463,1.94369,1.29928]),
        H298 = (65.955,'kcal/mol','+|-',7.6266),
        S298 = (1.41303,'cal/mol/K','+|-',10.1646),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 76,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,S}
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
C=C(C)COC(=C)[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 77,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[B,D,T,Q]}
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
C=C([O])OC=C(C)C from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 78,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_N-3R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 {1,S} {3,D}
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
C=CCCC([O])=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 79,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77519,-1.92266,-2.64465,-3.11111,-3.61138,-4.06033,-4.93895],'cal/mol/K','+|-',[3.34359,3.65978,3.90127,4.02614,4.0096,3.89298,3.87979]),
        H298 = (99.0056,'kcal/mol','+|-',20.1897),
        S298 = (0.495462,'cal/mol/K','+|-',9.22575),
    ),
    shortDesc = """Radical correction fitted to 78 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 80,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.22157,-2.64919,-3.3383,-3.75066,-4.09024,-4.47088,-5.18404],'cal/mol/K','+|-',[4.08322,4.25591,4.47441,4.64567,4.8835,4.77466,4.79842]),
        H298 = (92.1026,'kcal/mol','+|-',12.5639),
        S298 = (-0.796597,'cal/mol/K','+|-',7.82033),
    ),
    shortDesc = """Radical correction fitted to 39 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 81,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.113921,-1.65707,-2.40882,-2.90849,-3.4628,-3.89504,-4.9889],'cal/mol/K','+|-',[3.2434,4.78181,5.04012,4.95186,4.29732,3.48754,4.2217]),
        H298 = (98.8898,'kcal/mol','+|-',7.52113),
        S298 = (1.08066,'cal/mol/K','+|-',5.36932),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 82,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.346553,-2.52069,-3.34989,-3.7672,-4.07179,-4.32975,-5.6994],'cal/mol/K','+|-',[4.33711,6.2368,6.57887,6.4852,5.3503,4.04694,5.60914]),
        H298 = (101.61,'kcal/mol','+|-',2.26764),
        S298 = (1.49575,'cal/mol/K','+|-',5.63876),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 83,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Int-3R!H-1C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {3,S}
2   O   u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {1,S} {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.60989,0.393895,-0.464087,-1.14619,-2.13728,-3.13022,-5.02939],'cal/mol/K','+|-',[2.62205,1.99985,0.147054,0.797551,1.24017,2.14563,4.15595]),
        H298 = (101.846,'kcal/mol','+|-',4.50194),
        S298 = (-0.448379,'cal/mol/K','+|-',3.03935),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 84,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Int-3R!H-1C_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {3,S}
2   O u0 r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r1 {1,S} {2,[S,T,Q,B]}
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
C[C]1OC1O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 85,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Int-3R!H-1C_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {3,S}
2   O u0 r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux r1 {1,S} {2,[S,T,Q,B]}
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
OOC[C]1OO1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 86,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.15593,-6.62108,-7.24862,-7.44713,-7.11173,-6.57386,-5.72406],'cal/mol/K','+|-',[0.00295093,2.13782,2.84458,2.85838,2.15924,1.18191,0.347526]),
        H298 = (100.909,'kcal/mol','+|-',0.972259),
        S298 = (4.59503,'cal/mol/K','+|-',4.39688),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 87,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Ext-3R!H-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   O   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r1 {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
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
O=C1CO[CH]OC(=O)C1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 88,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.64563,-2.91196,-3.83648,-4.12363,-4.13557,-4.14828,-6.35422],'cal/mol/K','+|-',[1.58415,2.54319,6.29722,7.56584,6.92104,5.68833,11.3922]),
        H298 = (101.621,'kcal/mol','+|-',2.56106),
        S298 = (1.53262,'cal/mol/K','+|-',6.5446),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 89,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Ext-3R!H-R_N-4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   O   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O   ux r1 {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
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
O[C]1OC(O)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 90,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0942236,-0.884363,-1.56681,-2.14017,-2.91792,-3.50609,-4.35319],'cal/mol/K','+|-',[2.25304,2.76337,2.82139,2.89824,3.23495,3.07964,2.36364]),
        H298 = (96.5063,'kcal/mol','+|-',7.3406),
        S298 = (0.709259,'cal/mol/K','+|-',5.54973),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 91,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.268045,-1.05903,-1.7282,-2.31324,-3.09513,-3.71321,-4.59419],'cal/mol/K','+|-',[1.80453,2.44662,2.81168,3.10568,3.66105,3.46077,2.24736]),
        H298 = (95.7525,'kcal/mol','+|-',3.8717),
        S298 = (0.956301,'cal/mol/K','+|-',6.31748),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 92,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   O ux {1,S} {3,S}
3   C u0 {2,S}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.119062,-0.931317,-1.57846,-2.14333,-2.90145,-3.51123,-4.35982],'cal/mol/K','+|-',[1.76242,2.5962,2.97737,3.279,3.87953,3.62532,1.98871]),
        H298 = (95.555,'kcal/mol','+|-',3.76191),
        S298 = (0.844665,'cal/mol/K','+|-',6.99937),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 93,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   O   ux {1,S} {3,S}
3   C   u0 {2,S}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0488785,-0.332953,-0.84205,-1.34194,-2.00381,-2.66844,-3.81216],'cal/mol/K','+|-',[2.24206,2.29689,2.36296,2.6583,3.41487,3.17124,1.17933]),
        H298 = (94.4189,'kcal/mol','+|-',1.54574),
        S298 = (-0.947496,'cal/mol/K','+|-',5.17514),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 94,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   O   ux {1,S} {3,S}
3   C   u0 {2,S}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,S}
6   O   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.937259,0.613214,0.125597,-0.290091,-0.784304,-1.592,-3.65859],'cal/mol/K','+|-',[1.04146,0.35611,0.550024,1.2535,2.77656,2.91881,1.80093]),
        H298 = (94.2082,'kcal/mol','+|-',2.68052),
        S298 = (-3.04475,'cal/mol/K','+|-',1.68885),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 95,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   O   ux r0 {1,S} {3,S}
3   C   u0 r0 {2,S}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,S}
6   O   u0 r0 {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
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
C[C](OC(C)=O)C(C)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 96,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O                      u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C                      ux {2,[S,T,Q,B]}
4   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23644,-1.8892,-2.70149,-3.41763,-4.35403,-5.02605,-6.11761],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.1787,'kcal/mol','+|-',5.2),
        S298 = (1.68194,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCCO[C]=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 97,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
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
[CH2]OC(C)=C(C)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 98,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.93914,-3.18227,-3.83773,-4.20317,-4.42737,-4.78028,-5.28889],'cal/mol/K','+|-',[3.80479,3.62922,3.90734,4.32346,5.14008,5.31229,5.16665]),
        H298 = (88.2288,'kcal/mol','+|-',6.83027),
        S298 = (-1.80527,'cal/mol/K','+|-',8.27866),
    ),
    shortDesc = """Radical correction fitted to 26 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 99,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.79284,-5.20129,-4.99919,-4.40688,-3.37953,-3.07446,-2.59349],'cal/mol/K','+|-',[4.85081,4.76915,3.8423,4.44659,6.51867,7.10497,7.90183]),
        H298 = (92.5053,'kcal/mol','+|-',16.2345),
        S298 = (-2.31771,'cal/mol/K','+|-',12.6336),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 100,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-3R!H-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O ux {3,S}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.11226,-3.5433,-3.48685,-2.58311,-1.03705,-0.905546,-0.56855],'cal/mol/K','+|-',[4.26888,4.16285,1.91016,0.955725,5.20237,7.71818,9.98224]),
        H298 = (97.4843,'kcal/mol','+|-',23.1343),
        S298 = (-7.35085,'cal/mol/K','+|-',5.50472),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 101,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,D]}
6   O u0 r0 {5,[S,D]}
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
[O]OC(O)C(=O)C(O)=CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 102,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,D]}
6   C u0 r0 {5,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.60299,-2.07151,-2.8115,-2.92101,-2.87637,-3.63433,-4.0978],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.3051,'kcal/mol','+|-',5.2),
        S298 = (-5.40464,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(O)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 103,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5245,-2.88891,-3.66897,-4.17357,-4.57962,-5.02814,-5.68053],'cal/mol/K','+|-',[2.96262,3.19344,3.90761,4.4346,5.07068,5.0765,4.45468]),
        H298 = (87.5712,'kcal/mol','+|-',4.46114),
        S298 = (-1.73081,'cal/mol/K','+|-',7.99427),
    ),
    shortDesc = """Radical correction fitted to 23 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 104,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.59352,-2.47411,-2.89057,-3.1033,-3.35291,-3.78899,-4.365],'cal/mol/K','+|-',[3.13333,3.70382,4.03637,3.9889,3.84831,3.53173,1.72602]),
        H298 = (86.996,'kcal/mol','+|-',4.3258),
        S298 = (-2.98253,'cal/mol/K','+|-',7.5459),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 105,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_3R!H-inRing",
    group = 
"""
1 * O u1 {2,S}
2   O ux {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 {3,S} {5,D}
5   C u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.82026,-4.63691,-5.13642,-5.11504,-5.00533,-5.00641,-4.71878],'cal/mol/K','+|-',[1.39489,0.813941,0.0868603,0.329537,0.587569,1.32905,1.04779]),
        H298 = (86.234,'kcal/mol','+|-',0.241409),
        S298 = (0.91182,'cal/mol/K','+|-',1.63145),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 106,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_3R!H-inRing_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   C   u0 {4,D}
6   R!H ux {4,[S,D,T,B,Q]}
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
C=C1COOCC1(C)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 107,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24683,-1.86289,-2.25588,-2.53477,-2.88592,-3.44493,-4.26502],'cal/mol/K','+|-',[3.18561,3.18992,3.61174,3.76687,3.85993,3.70219,1.88715]),
        H298 = (87.2608,'kcal/mol','+|-',5.0053),
        S298 = (-4.08311,'cal/mol/K','+|-',7.02327),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 108,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-5R!H-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux {4,D} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.1999,-2.19682,-2.06344,-2.19665,-2.27026,-2.73178,-4.14501],'cal/mol/K','+|-',[3.12048,4.58745,5.50048,5.82128,5.89515,5.23257,2.80709]),
        H298 = (89.8951,'kcal/mol','+|-',6.17346),
        S298 = (-5.09881,'cal/mol/K','+|-',7.49533),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 109,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O u1 {2,S}
2   O ux {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 {3,S} {5,D}
5   C u0 {4,D} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,D}
7   C u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21092,-0.350831,0.226291,0.253578,0.217563,-0.555498,-2.9969],'cal/mol/K','+|-',[1.44098,0.458011,0.212169,0.640609,1.12407,1.22384,0.648504]),
        H298 = (92.4541,'kcal/mol','+|-',2.72613),
        S298 = (-8.03475,'cal/mol/K','+|-',0.388719),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 110,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,D} {8,[S,D,T,B,Q]}
5   C   u0 r0 {4,D} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,D}
7   C   u0 r0 {6,D}
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
C=CC=C(O)CO[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 111,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-5R!H-R_Sp-4BrCClFINPSSi-3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,D}
5   C ux {4,D} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.38713,-5.0676,-5.27749,-5.45262,-5.46224,-5.68766,-5.80891],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.8206,'kcal/mol','+|-',5.2),
        S298 = (-0.211166,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=CCO[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 112,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-5R!H-R_N-Sp-4BrCClFINPSSi-3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,D}
4   C ux {3,D} {5,D}
5   C ux {4,D} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99065,-3.01802,-3.42886,-3.84114,-4.05393,-4.12847,-4.77732],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.8515,'kcal/mol','+|-',5.2),
        S298 = (-4.1146,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C=CO[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 113,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   C   ux {4,D}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.16305,-1.8685,-2.3878,-2.61827,-3.02082,-3.56791,-4.31661],'cal/mol/K','+|-',[1.79615,2.5193,2.89141,2.77743,2.47099,2.53055,1.58407]),
        H298 = (86.5409,'kcal/mol','+|-',2.89809),
        S298 = (-4.03728,'cal/mol/K','+|-',7.37385),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 114,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-3R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]}
4   C ux {3,S} {5,D}
5   C ux {4,D}
6   C ux {3,[S,D,T,B,Q]} {7,S}
7   O u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.602783,-1.8173,-2.5523,-2.77972,-3.10746,-3.56761,-4.54492],'cal/mol/K','+|-',[2.10821,1.00091,0.0883921,0.303288,0.794769,1.31973,0.257401]),
        H298 = (88.7269,'kcal/mol','+|-',0.629581),
        S298 = (-6.94469,'cal/mol/K','+|-',4.17239),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 115,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   ux {3,S} {5,D}
5   C   ux {4,D}
6   C   ux {3,[S,D,T,B,Q]} {7,S}
7   O   u0 r0 {6,S}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34815,-2.17117,-2.58355,-2.6725,-2.82646,-3.10102,-4.45391],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.5043,'kcal/mol','+|-',5.2),
        S298 = (-8.41985,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(C)(CO)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 116,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   C   ux {4,D}
6   R!H ux {3,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
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
C=C(C=O)C(C)(C)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 117,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.45429,-3.31086,-4.46078,-5.26228,-5.82749,-6.28866,-7.01874],'cal/mol/K','+|-',[2.94587,2.49977,3.23487,3.90644,5.09021,5.30143,4.82948]),
        H298 = (88.1632,'kcal/mol','+|-',4.66072),
        S298 = (-0.457513,'cal/mol/K','+|-',7.99368),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 118,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O     u1 {2,[S,D,T,B,Q]}
2   O     ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C     ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C     ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   [C,O] ux {4,[S,T,Q,B]}
6   [C,O] ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.3226,-3.73126,-4.51054,-4.86247,-4.9451,-5.33436,-6.92954],'cal/mol/K','+|-',[3.23152,2.35722,2.37539,2.66555,2.32429,2.25487,5.87159]),
        H298 = (86.9479,'kcal/mol','+|-',1.88664),
        S298 = (-2.04184,'cal/mol/K','+|-',6.58874),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 119,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,T,Q,B]}
6   O   ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,S}
8   C   ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.62523,-3.88393,-4.48408,-4.7165,-4.79821,-5.17459,-6.24704],'cal/mol/K','+|-',[3.20297,2.52131,2.69575,2.9033,2.4938,2.38089,5.30029]),
        H298 = (86.8121,'kcal/mol','+|-',1.85971),
        S298 = (-1.24834,'cal/mol/K','+|-',5.8182),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 120,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S} {6,S}
5   C   u0 {4,S} {9,[S,D,T,B,Q]}
6   O   u0 {4,S} {7,S}
7   R!H ux {6,S} {8,S}
8   C   u0 {7,S}
9   R!H ux {5,[S,D,T,B,Q]}
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
C=C1COOC1(C)CO[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 121,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_4BrCClFINPSSi-inRing",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 r1 {3,S} {5,S} {6,S}
5   C u0 {4,S}
6   O u0 {4,S} {7,S}
7   O u0 {6,S} {8,S}
8   C u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.64083,-4.61137,-4.98877,-5.09397,-4.93028,-5.0609,-6.21105],'cal/mol/K','+|-',[0.161663,2.00215,3.5318,4.26296,3.50082,2.81362,8.37845]),
        H298 = (86.7452,'kcal/mol','+|-',2.91908),
        S298 = (0.531721,'cal/mol/K','+|-',2.6244),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 122,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_4BrCClFINPSSi-inRing_3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 r1 {3,S} {5,S} {6,S}
5   C u0 {4,S}
6   O u0 r1 {4,S} {7,S}
7   O u0 r1 {6,S} {8,S}
8   C u0 r1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.71997,-5.59149,-6.71771,-7.18084,-6.64406,-6.43827,-10.3126],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.0436,'kcal/mol','+|-',5.2),
        S298 = (-0.753015,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)OOCC1(C)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 123,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_4BrCClFINPSSi-inRing_N-3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r1 {3,S} {5,S} {6,S}
5   C u0 {4,S}
6   O u0 r1 {4,S} {7,S}
7   O u0 r1 {6,S} {8,S}
8   C u0 r1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.60566,-4.17576,-4.22035,-4.16647,-4.16861,-4.44874,-4.38814],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (87.1077,'kcal/mol','+|-',2.4),
        S298 = (1.10272,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC1CCOO1 from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 124,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_N-4BrCClFINPSSi-inRing",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r0 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,T,Q,B]}
6   O   ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,S}
8   C   ux {7,S}
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
CC(=O)OC(C)(C)CO[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 125,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   C   ux {3,D} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
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
C#CC(=CC)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 126,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.616236,-2.98327,-4.65767,-5.77781,-6.78876,-7.37679,-7.43614],'cal/mol/K','+|-',[1.97051,2.84593,4.06466,5.02714,6.64805,6.81415,4.34583]),
        H298 = (89.0866,'kcal/mol','+|-',6.07847),
        S298 = (1.17258,'cal/mol/K','+|-',9.00139),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 127,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.315252,-3.16133,-5.15926,-6.4745,-7.70163,-8.32211,-7.87884],'cal/mol/K','+|-',[1.82318,3.46145,4.56521,5.42854,7.19949,7.34143,5.06341]),
        H298 = (89.5983,'kcal/mol','+|-',5.74197),
        S298 = (1.56179,'cal/mol/K','+|-',10.849),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 128,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O_Ext-3R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]}
4   C ux {3,S} {5,S}
5   O ux {4,S}
6   C ux {3,[S,D,T,B,Q]} {7,S}
7   C u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.553989,-2.64436,-4.04579,-4.78837,-5.06489,-5.37757,-5.74057],'cal/mol/K','+|-',[2.78702,5.46581,6.02251,5.18106,3.14715,1.81701,0.96929]),
        H298 = (87.469,'kcal/mol','+|-',3.56473),
        S298 = (-1.43875,'cal/mol/K','+|-',7.27131),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 129,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O_Ext-3R!H-R_Ext-6R!H-R_3R!H-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]}
4   C ux {3,S} {5,S}
5   O ux {4,S}
6   C ux {3,[S,D,T,B,Q]} {7,S}
7   C u0 {6,S}
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
C=C1CC(C)(O[O])CO1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 130,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O_Ext-3R!H-R_Ext-6R!H-R_N-3R!H-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]}
4   C ux {3,S} {5,S}
5   O ux {4,S}
6   C ux {3,[S,D,T,B,Q]} {7,S}
7   C u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.431371,-0.711905,-1.91651,-2.95658,-3.9522,-4.73516,-5.39787],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.2087,'kcal/mol','+|-',5.2),
        S298 = (-4.00954,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(CO)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 131,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O_Ext-5O-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {3,S} {5,S}
5   O u0 {4,S} {6,S}
6   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.530766,-4.09756,-6.77113,-8.76443,-11.1052,-11.8372,-10.2917],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (90.8338,'kcal/mol','+|-',2),
        S298 = (6.43496,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(COCOO)O[O] from Radical thermo from johnson_g4.py and closed shell thermo from Thermo library: ../data/johnson_g4.py
""",
)

entry(
    index = 132,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O_Ext-5O-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   O                      u0 r0 {1,S} {3,S}
3   C                      u0 {2,S} {4,S}
4   C                      u0 {3,S} {5,S}
5   O                      u0 {4,S} {6,S}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.647131,-2.08877,-3.75949,-4.69443,-5.31722,-6.30221,-6.72642],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.5047,'kcal/mol','+|-',5.2),
        S298 = (-3.40178,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(COOCC(=O)O)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 133,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_N-5R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.40632,-2.51583,-3.34101,-3.94899,-4.39245,-4.89532,-6.27405],'cal/mol/K','+|-',[1.87603,0.749482,0.536679,1.31957,1.7674,1.99394,0.752108]),
        H298 = (86.5899,'kcal/mol','+|-',7.60587),
        S298 = (0.150912,'cal/mol/K','+|-',5.12511),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 134,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_N-5R!H->O_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux r0 {3,S} {5,[S,T,Q,B]}
5   C   ux r0 {4,[S,T,Q,B]}
6   R!H ux {3,[S,D,T,B,Q]}
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
CCC(CC)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 135,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.393641,-1.30164,-2.05174,-2.56445,-3.20206,-3.70941,-4.72946],'cal/mol/K','+|-',[2.34534,2.50833,2.89916,3.06687,2.89714,2.82019,2.87667]),
        H298 = (104.309,'kcal/mol','+|-',18.5546),
        S298 = (1.59988,'cal/mol/K','+|-',9.85355),
    ),
    shortDesc = """Radical correction fitted to 39 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 136,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.288037,-1.36418,-2.21823,-2.74739,-3.34444,-3.84394,-4.86979],'cal/mol/K','+|-',[2.6211,2.875,3.3187,3.51695,3.34046,3.25946,3.34022]),
        H298 = (101.034,'kcal/mol','+|-',19.378),
        S298 = (1.58597,'cal/mol/K','+|-',11.6227),
    ),
    shortDesc = """Radical correction fitted to 31 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 137,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.172359,-1.42854,-2.37016,-2.97758,-3.6067,-4.13315,-5.29391],'cal/mol/K','+|-',[2.58503,3.14043,3.70523,3.84532,3.48132,3.28072,3.17014]),
        H298 = (99.9049,'kcal/mol','+|-',14.4835),
        S298 = (2.92107,'cal/mol/K','+|-',11.7303),
    ),
    shortDesc = """Radical correction fitted to 24 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 138,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.405261,-1.67099,-2.56394,-3.09278,-3.60118,-4.04244,-5.31125],'cal/mol/K','+|-',[3.04293,3.82586,4.21818,4.07671,3.4128,2.95819,3.76232]),
        H298 = (96.2996,'kcal/mol','+|-',14.6255),
        S298 = (2.8414,'cal/mol/K','+|-',15.918),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 139,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   C   ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.678953,-2.13125,-3.11711,-3.66811,-4.13238,-4.4623,-5.70434],'cal/mol/K','+|-',[3.32197,3.75123,4.01449,3.80283,3.02748,2.53093,4.22819]),
        H298 = (101.412,'kcal/mol','+|-',5.62719),
        S298 = (1.7096,'cal/mol/K','+|-',11.1789),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 140,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   C   ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.175812,-2.35927,-3.74826,-4.37119,-4.65098,-4.73268,-4.70374],'cal/mol/K','+|-',[1.49628,2.53835,2.96584,2.56159,2.07953,2.00484,1.82031]),
        H298 = (100.657,'kcal/mol','+|-',6.26151),
        S298 = (-1.74451,'cal/mol/K','+|-',15.5962),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 141,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R_3R!H->O",
    group = 
"""
1 * C u1 {2,S} {4,S}
2   C u0 {1,S} {3,[S,T,Q,B]} {6,S}
3   O ux {2,[S,T,Q,B]}
4   C u0 {1,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.776213,-3.24688,-4.75589,-5.13155,-5.07637,-5.05116,-4.20593],'cal/mol/K','+|-',[0.49766,0.342063,0.146906,0.246874,0.715111,1.09057,1.78295]),
        H298 = (102.257,'kcal/mol','+|-',8.59646),
        S298 = (-8.45968,'cal/mol/K','+|-',2.54715),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 142,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R_3R!H->O_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-10R!H-R",
    group = 
"""
1  * C   u1 {2,S} {4,S}
2    C   u0 {1,S} {3,[S,T,Q,B]} {6,S}
3    O   ux {2,[S,T,Q,B]} {7,S}
4    C   u0 {1,S} {5,[S,D,T,B,Q]}
5    C   ux {4,[S,D,T,B,Q]}
6    C   u0 {2,S}
7    O   u0 r0 {3,S} {8,[S,D,T,B,Q]}
8    C   ux r1 {7,[S,D,T,B,Q]} {9,S}
9    C   u0 r1 {8,S} {10,[S,D,T,B,Q]}
10   C   ux r1 {9,[S,D,T,B,Q]} {11,[S,D,T,B,Q]} {12,[S,D,T,B,Q]}
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
CC[CH]C(CC)OOC1C=CCC(C)=C1 from Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 143,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R_N-3R!H->O",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,S} {6,[S,D,T,B,Q]}
3   C   u0 {2,S}
4   C   ux {1,[S,D,T,B,Q]} {5,S}
5   R!H u0 {4,S}
6   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.42459,-1.47166,-2.74062,-3.61082,-4.22559,-4.41419,-5.20155],'cal/mol/K','+|-',[0.837344,2.57042,3.18145,3.22083,3.09299,3.04071,1.67232]),
        H298 = (99.0583,'kcal/mol','+|-',1.6745),
        S298 = (4.97066,'cal/mol/K','+|-',1.31899),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 144,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R_N-3R!H->O_1C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,S} {6,[S,D,T,B,Q]}
3   C   u0 {2,S}
4   C   ux {1,[S,D,T,B,Q]} {5,S}
5   R!H u0 {4,S}
6   C   ux {2,[S,D,T,B,Q]}
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
[CH]1CCC2C3C=CC(C3)C12 from Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 145,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R_N-3R!H->O_N-1C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,S} {6,[S,D,T,B,Q]}
3   C   u0 {2,S}
4   C   ux {1,[S,D,T,B,Q]} {5,S}
5   R!H u0 {4,S}
6   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.128544,-2.38044,-3.86543,-4.74956,-5.31913,-5.48925,-5.79281],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.6504,'kcal/mol','+|-',5.2),
        S298 = (4.50432,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(C)(C)[CH]CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 146,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C u1 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {6,S}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.70851,-3.88269,-4.63592,-5.04305,-5.25497,-5.47388,-8.41218],'cal/mol/K','+|-',[1.97296,0.568967,0.19604,0.145697,0.545062,1.23112,3.30273]),
        H298 = (98.6381,'kcal/mol','+|-',3.60808),
        S298 = (5.55801,'cal/mol/K','+|-',2.14426),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 147,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-3R!H-R_Int-6R!H-5R!H",
    group = 
"""
1 * C u1 {2,S} {4,S}
2   C u0 {1,S} {3,S}
3   O u0 {2,S} {6,S}
4   C u0 {1,S} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   O u0 {3,S} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.11576,-3.68377,-4.68739,-5.03205,-5.1761,-5.4651,-9.62266],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.6456,'kcal/mol','+|-',5.2),
        S298 = (4.32075,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCOOC1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 148,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-3R!H-R_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {6,S}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {3,S}
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
CC(=O)C[C]1COOC1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 149,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-3R!H-R_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {6,S}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {3,S}
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
CC[CH]COO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 150,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_1C-inRing",
    group = 
"""
1 * C     u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C     ux {1,S} {3,[S,T,Q,B]}
3   [C,O] ux {2,[S,T,Q,B]}
4   C     ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   [C,O] ux {4,[S,D,T,B,Q]}
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
CC1[CH]CO1 from Radical thermo from johnson_g4.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 151,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_N-1C-inRing",
    group = 
"""
1 * C     u1 r0 {2,S} {4,[S,D,T,B,Q]}
2   C     ux {1,S} {3,[S,T,Q,B]}
3   [C,O] ux {2,[S,T,Q,B]}
4   C     ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   [C,O] ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.780507,-2.18006,-2.90824,-3.4057,-3.9476,-4.37991,-5.2467],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.315,'kcal/mol','+|-',5.2),
        S298 = (3.56917,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 152,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_3R!H->O",
    group = 
"""
1 * C u1 {2,S} {4,S}
2   C u0 {1,S} {3,S}
3   O u0 {2,S}
4   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77957,-3.70817,-4.55825,-4.73816,-4.61131,-5.12696,-6.87098],'cal/mol/K','+|-',[0.0862615,1.50519,2.60998,3.80025,5.30714,5.45272,1.44284]),
        H298 = (94.0066,'kcal/mol','+|-',2.75348),
        S298 = (1.42292,'cal/mol/K','+|-',15.8708),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 153,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_3R!H->O_Ext-3O-R_Ext-5R!H-R_Ext-3O-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-3O-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 {2,S} {4,S}
2   C   u0 {1,S} {3,S}
3   O   u0 {2,S} {5,[S,D,T,B,Q]}
4   C   u0 {1,S}
5   O   ux {3,[S,D,T,B,Q]} {6,S}
6   C   u0 r0 {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
C=C(COO)C(C)(C)OOC(C)(C)[C](C)C from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 154,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_N-3R!H->O",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.604549,-0.0724453,-0.807833,-1.42226,-2.24389,-2.86562,-4.0115],'cal/mol/K','+|-',[1.78036,1.82205,2.72923,2.91812,2.32888,1.52493,1.18235]),
        H298 = (90.0546,'kcal/mol','+|-',15.2986),
        S298 = (5.46649,'cal/mol/K','+|-',26.9734),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 155,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_N-3R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,[S,T,Q,B]}
3   C   u0 {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
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
C=C=C(C)C(C)(C)[C](C)C from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 156,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_N-3R!H->O_Sp-3C-2C",
    group = 
"""
1 * C u1 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,S}
3   C ux {2,S}
4   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.137299,-0.642163,-1.35686,-1.87684,-2.63309,-3.31485,-4.54092],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.3283,'kcal/mol','+|-',2.4),
        S298 = (0.945418,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 157,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_N-3R!H->O_N-Sp-3C-2C",
    group = 
"""
1 * C u1 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,T}
3   C ux {2,T}
4   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.81772,0.797011,0.425813,-0.15638,-1.22218,-2.14066,-3.78725],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.6256,'kcal/mol','+|-',2.4),
        S298 = (-0.112743,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#C[CH]O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 158,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_2C-inRing",
    group = 
"""
1 * C u1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.560328,-1.38401,-2.96401,-3.88324,-4.65269,-5.1615,-5.89145],'cal/mol/K','+|-',[1.79001,3.2609,5.36235,6.44223,6.61873,6.92705,3.96983]),
        H298 = (105.208,'kcal/mol','+|-',26.2814),
        S298 = (2.68097,'cal/mol/K','+|-',1.99668),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 159,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r1 {1,S} {3,[S,T,Q,B]}
3   C   u0 {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.245401,-1.07257,-2.15985,-2.77225,-3.31766,-3.67665,-5.1151],'cal/mol/K','+|-',[1.42546,4.00083,5.28644,5.32236,3.28171,1.3111,2.32569]),
        H298 = (101.47,'kcal/mol','+|-',2.78384),
        S298 = (2.64609,'cal/mol/K','+|-',2.72099),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 160,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_3R!H-inRing",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r1 {1,S} {3,[S,T,Q,B]}
3   C   u0 r1 {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.555541,-0.202108,-1.00967,-1.61425,-2.60365,-3.39139,-4.6091],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (101.124,'kcal/mol','+|-',2.4),
        S298 = (2.05408,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1C=CC1 from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 161,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-3R!H-inRing",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r1 {1,S} {3,[S,T,Q,B]}
3   C   u0 r0 {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.452413,-3.03112,-4.74775,-5.37773,-4.92417,-4.31848,-6.25361],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.093,'kcal/mol','+|-',5.2),
        S298 = (3.97811,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C=O)OO1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 162,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,S}
3   C   ux r1 {2,S} {4,S}
4   R!H u0 r1 {3,S}
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
[CH2]C1(C)CC(OO)C(=O)OO1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 163,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0774672,-1.04583,-1.81541,-2.42931,-3.20229,-3.87636,-5.02905],'cal/mol/K','+|-',[1.99822,1.85819,2.15772,2.47409,2.33641,2.29577,1.91198]),
        H298 = (103.121,'kcal/mol','+|-',2.04885),
        S298 = (3.14753,'cal/mol/K','+|-',4.06833),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 164,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.432067,-1.61609,-2.45648,-3.06473,-3.70823,-4.34329,-5.50257],'cal/mol/K','+|-',[2.28034,1.017,1.61182,2.42033,2.59938,2.64637,1.99853]),
        H298 = (102.711,'kcal/mol','+|-',2.22648),
        S298 = (4.06369,'cal/mol/K','+|-',4.37521),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 165,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,[S,T,Q,B]}
3   R!H u0 r0 {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
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
[CH2]C(C)(C)C(C)(C)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 166,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
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
[CH2]COC(C)=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 167,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,S} {5,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S}
5   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.689779,-1.0042,-2.35691,-3.27525,-4.11171,-4.83684,-5.989],'cal/mol/K','+|-',[1.20441,0.317691,0.165538,0.653324,1.19124,1.73265,1.04806]),
        H298 = (101.974,'kcal/mol','+|-',0.819694),
        S298 = (3.66199,'cal/mol/K','+|-',1.7868),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 168,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C_Ext-2C-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S} {5,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S}
5   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.263956,-1.11652,-2.29838,-3.04427,-3.69054,-4.22425,-5.61845],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.684,'kcal/mol','+|-',5.2),
        S298 = (4.29372,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)CC from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 169,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C_Ext-2C-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,S} {5,S}
3   C                      u0 r0 {2,S} {4,S}
4   C                      u0 r0 {3,S}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.1156,-0.891876,-2.41544,-3.50624,-4.53287,-5.44943,-6.35954],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.263,'kcal/mol','+|-',5.2),
        S298 = (3.03026,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(CC)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 170,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,[S,T,Q,B]}
3   R!H u0 {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.415032,-0.253799,-0.925038,-1.54679,-2.49961,-3.22784,-4.37138],'cal/mol/K','+|-',[1.21606,1.70872,1.44915,1.08423,0.736095,0.522599,0.306025]),
        H298 = (103.5,'kcal/mol','+|-',2.07036),
        S298 = (1.87508,'cal/mol/K','+|-',1.68285),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 171,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_N-4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   R!H u0 r0 {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0149104,-0.857923,-1.43739,-1.93012,-2.75986,-3.41261,-4.47957],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.232,'kcal/mol','+|-',2.4),
        S298 = (2.47006,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(O)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 172,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.64045,-1.16808,-1.75536,-2.04611,-2.54544,-2.96284,-3.57769],'cal/mol/K','+|-',[2.8398,2.01911,1.53393,1.7989,2.43271,2.69377,2.55601]),
        H298 = (104.203,'kcal/mol','+|-',30.9362),
        S298 = (-2.48142,'cal/mol/K','+|-',6.86815),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 173,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_2C-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,S}
3   R!H u0 {2,S}
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
[O]C12OC1(O)O2 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 174,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.565193,-1.19922,-1.8282,-2.13384,-2.63443,-3.04598,-3.6018],'cal/mol/K','+|-',[2.97799,2.14101,1.54702,1.80839,2.51156,2.80772,2.71985]),
        H298 = (107.504,'kcal/mol','+|-',3.10785),
        S298 = (-2.51963,'cal/mol/K','+|-',7.31835),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 175,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,S}
3   C u0 {2,S} {4,D}
4   C u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.642815,-0.799555,-1.16671,-1.12138,-1.21014,-1.54439,-2.19653],'cal/mol/K','+|-',[4.30969,3.26755,2.10424,1.89346,1.53471,1.22681,1.01157]),
        H298 = (109.565,'kcal/mol','+|-',2.17762),
        S298 = (-6.62441,'cal/mol/K','+|-',2.85228),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 176,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,S} {5,S}
3   C   u0 {2,S} {4,D}
4   C   u0 {3,D}
5   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.592962,0.143229,-0.57385,-0.62364,-0.84111,-1.39387,-2.46528],'cal/mol/K','+|-',[0.703822,0.147115,0.64821,1.1066,1.20094,1.57045,0.559608]),
        H298 = (109.16,'kcal/mol','+|-',2.35618),
        S298 = (-6.71584,'cal/mol/K','+|-',4.00878),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 177,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,S} {5,S}
3   C   u0 {2,S} {4,D} {6,[S,D,T,B,Q]}
4   C   u0 {3,D}
5   R!H u0 r0 {2,S}
6   R!H ux {3,[S,D,T,B,Q]}
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
C=C(C)C([O])CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 178,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.530695,-1.37684,-2.1222,-2.58382,-3.26745,-3.71335,-4.22636],'cal/mol/K','+|-',[2.69456,1.63436,0.734775,0.433714,1.48043,2.11157,2.21366]),
        H298 = (107.065,'kcal/mol','+|-',2.41255),
        S298 = (-0.695287,'cal/mol/K','+|-',5.03239),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 179,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,S}
3   R!H u0 {2,S} {4,S}
4   O   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,[S,D,T,B,Q]}
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
[O]COOCO from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 180,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.30697,-2.06443,-2.53664,-2.62894,-2.76435,-2.89145,-3.26916],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (107.535,'kcal/mol','+|-',2.4),
        S298 = (-1.3303,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CC1(O)CO1 from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 181,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31012,-1.5927,-1.99342,-2.34795,-2.9206,-3.34452,-3.97154],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (105.695,'kcal/mol','+|-',2.4),
        S298 = (-2.83314,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
COOC[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 182,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R",
    group = 
"""
1 * C   u1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.667897,-1.13924,-1.61937,-2.08935,-2.83232,-3.36003,-4.36504],'cal/mol/K','+|-',[1.36177,1.15374,0.945185,0.876429,0.866082,0.783714,0.552694]),
        H298 = (110.967,'kcal/mol','+|-',4.35652),
        S298 = (1.636,'cal/mol/K','+|-',1.22097),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 183,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_2C-inRing",
    group = 
"""
1 * C u1 r0 {2,D}
2   C u0 r1 {1,D} {3,S}
3   C ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.013064,-0.834465,-1.46565,-2.01132,-2.76669,-3.3727,-4.66668],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.531,'kcal/mol','+|-',5.2),
        S298 = (2.92626,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C1C=C1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 184,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing",
    group = 
"""
1 * C   u1 {2,D}
2   C   ux r0 {1,D} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.711133,-1.15859,-1.62913,-2.09431,-2.83648,-3.35923,-4.34589],'cal/mol/K','+|-',[1.36232,1.18651,0.978286,0.90959,0.899138,0.814278,0.54874]),
        H298 = (111.194,'kcal/mol','+|-',3.41082),
        S298 = (1.55408,'cal/mol/K','+|-',1.04156),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 185,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_Ext-1R-R",
    group = 
"""
1 * C u1 {2,D} {4,S}
2   C u0 r0 {1,D} {3,S}
3   C ux {2,S}
4   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.797606,-1.35564,-1.86394,-2.35077,-3.13404,-3.70812,-4.55969],'cal/mol/K','+|-',[1.77508,2.17227,1.97469,1.66467,1.15421,0.78849,0.351435]),
        H298 = (109.114,'kcal/mol','+|-',0.0189081),
        S298 = (1.58059,'cal/mol/K','+|-',2.0857),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 186,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_Ext-1R-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,D} {4,S}
2   C   u0 r0 {1,D} {3,S} {5,[S,D,T,B,Q]}
3   C   ux {2,S}
4   O   u0 r0 {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
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
CC(C)=[C]O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 187,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_3R!H->O",
    group = 
"""
1 * C u1 {2,D}
2   C ux r0 {1,D} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.730155,-1.11417,-1.37855,-1.5899,-2.07085,-2.59329,-3.8524],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.62,'kcal/mol','+|-',2.4),
        S298 = (1.1138,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C(O)CC from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 188,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_N-3R!H->O",
    group = 
"""
1 * C u1 {2,D}
2   C u0 r0 {1,D} {3,S}
3   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.663141,-1.07117,-1.57436,-2.09218,-2.87911,-3.37626,-4.36236],'cal/mol/K','+|-',[1.62136,1.04678,0.606248,0.465126,0.381355,0.102434,0.336169]),
        H298 = (111.627,'kcal/mol','+|-',1.69706),
        S298 = (1.65089,'cal/mol/K','+|-',0.639794),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 189,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_N-3R!H->O_Ext-3C-R_4R!H->O",
    group = 
"""
1 * C u1 {2,D}
2   C u0 r0 {1,D} {3,S}
3   C u0 {2,S} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32719,-1.49739,-1.82842,-2.288,-2.99722,-3.39694,-4.26599],'cal/mol/K','+|-',[0.862011,0.556425,0.18025,0.186334,0.461556,0.0561449,0.425367]),
        H298 = (111.025,'kcal/mol','+|-',1.65802),
        S298 = (1.77257,'cal/mol/K','+|-',0.905777),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 190,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_N-3R!H->O_Ext-3C-R_4R!H->O_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   u0 r0 {1,D} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 r0 {2,S} {4,S}
4   O   ux {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.02243,-1.30067,-1.76469,-2.35388,-3.1604,-3.41679,-4.1156],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (110.439,'kcal/mol','+|-',2.4),
        S298 = (1.45233,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C(CO)C(C)=O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 191,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_N-3R!H->O_Ext-3C-R_N-4R!H->O",
    group = 
"""
1 * C u1 {2,D}
2   C u0 r0 {1,D} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.000912146,-0.644954,-1.32031,-1.89636,-2.761,-3.35559,-4.45873],'cal/mol/K','+|-',[0.296412,0.266537,0.193474,0.0281491,0.00824188,0.146581,0.097389]),
        H298 = (112.23,'kcal/mol','+|-',0.291129),
        S298 = (1.5292,'cal/mol/K','+|-',0.413116),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 192,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_N-3R!H->O_Ext-3C-R_N-4R!H->O_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   u0 r0 {1,D} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 r0 {2,S} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.105709,-0.550719,-1.25191,-1.88641,-2.76392,-3.30376,-4.49317],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (112.127,'kcal/mol','+|-',2.4),
        S298 = (1.67526,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C(C)CC from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-3R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-1R-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-1R-R_Ext-1R-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-2R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_N-3R!H-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_N-3R!H-inRing_2R!H-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_N-3R!H-inRing_2R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_4R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_N-3R!H-inRing_2R!H-inRing_Ext-2R!H-R_Ext-4R!H-R_N-4R!H->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R-inRing_N-3R!H-inRing_N-2R!H-inRing
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R_2R!H-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-2R!H-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-2R!H-inRing_5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-2R!H-inRing_N-5R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_Ext-1C-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_3R!H-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_Ext-3R!H-R_N-3R!H-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_3R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_N-3R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_N-3R!H->C_Ext-1C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Ext-2R!H-R_N-3R!H->C_Ext-1C-R_Ext-4R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-4R!H-R_5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-4R!H-R_5R!H->C_4R!H-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-4R!H-R_5R!H->C_N-4R!H-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-4R!H-R_N-5R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-3R!H-R_N-Sp-4R!H-3R!H
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_4R!H-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_4R!H-inRing_Ext-1C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-1C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-4R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-4R!H-R_Sp-5R!H#4R!H
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-4R!H-R_N-Sp-5R!H#4R!H
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-4R!H-R_N-Sp-5R!H#4R!H_Sp-4R!H-1C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_3R!H->C_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-Sp-4R!H-1C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_N-3R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_N-3R!H->C_Ext-1C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_N-3R!H->C_Ext-1C-R_Ext-5R!H-R_6R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_Sp-2R!H-1C_Ext-1C-R_N-4R!H-inRing_N-3R!H->C_Ext-1C-R_Ext-5R!H-R_N-6R!H->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_1R->C_N-Sp-2R!H-1C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_2R!H-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_2R!H-inRing_Ext-3C-R_Ext-4R!H-R_4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_2R!H-inRing_Ext-3C-R_Ext-4R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_5R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_2R!H-inRing_Ext-3C-R_Ext-4R!H-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_N-5R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_2R!H-inRing_Ext-3C-R_Ext-4R!H-R_N-4R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->O_Ext-2R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-4C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-4C-R_4C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_4R!H->C_Ext-4C-R_Ext-4C-R_N-4C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_N-4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R-inRing_N-1R->C_N-3R!H->C
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Int-3R!H-1C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Int-3R!H-1C_3R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Int-3R!H-1C_N-3R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Ext-3R!H-R_4R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Ext-3R!H-R_4R!H->C_Ext-3R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Ext-3R!H-R_N-4R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_1C-inRing_Ext-3R!H-R_N-4R!H->C_Ext-3R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R_4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R_4R!H->C_Ext-4C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-1C-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-1C-R_N-4R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-3R!H-R
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_4R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_Ext-5R!H-R_6R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-3R!H-R_Ext-5R!H-R_N-6R!H->O
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_3R!H-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_3R!H-inRing_Ext-4BrCClFINPSSi-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-5R!H-R_Ext-6R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-5R!H-R_Sp-4BrCClFINPSSi-3R!H
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-5R!H-R_N-Sp-4BrCClFINPSSi-3R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-3R!H-R_Ext-6R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_4BrCClFINPSSi-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_4BrCClFINPSSi-inRing_3R!H-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_4BrCClFINPSSi-inRing_N-3R!H-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_Ext-7R!H-R_N-4BrCClFINPSSi-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O_Ext-3R!H-R_Ext-6R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O_Ext-3R!H-R_Ext-6R!H-R_3R!H-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O_Ext-3R!H-R_Ext-6R!H-R_N-3R!H-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O_Ext-5O-R_6R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_5R!H->O_Ext-5O-R_N-6R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_N-5R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_N-5R!H->O_Ext-3R!H-R
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R_3R!H->O
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R_3R!H->O_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-10R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R_N-3R!H->O
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R_N-3R!H->O_1C-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-2C-R_N-3R!H->O_N-1C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-3R!H-R_Int-6R!H-5R!H
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-3R!H-R_1C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_Ext-3R!H-R_N-1C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_1C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_Ext-4R!H-R_N-1C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_3R!H->O
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_3R!H->O_Ext-3O-R_Ext-5R!H-R_Ext-3O-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-3O-R_Ext-6R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_N-3R!H->O
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_N-3R!H->O_Ext-1C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_N-3R!H->O_Sp-3C-2C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_Ext-1C-R_N-3R!H->O_N-Sp-3C-2C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_2C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_3R!H-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-3R!H-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C_Ext-4C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C_Ext-2C-R_5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_4R!H->C_Ext-2C-R_N-5R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_N-4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_1R->C_N-2C-inRing_Ext-3R!H-R_N-4R!H->C_Ext-2C-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_2C-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2C-R_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-4R!H-R_Ext-5R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_Sp-2C-1R_N-1R->C_N-2C-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_2C-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_Ext-1R-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_Ext-1R-R_Ext-2C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_3R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_N-3R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_N-3R!H->O_Ext-3C-R_4R!H->O
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_N-3R!H->O_Ext-3C-R_4R!H->O_Ext-2C-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_N-3R!H->O_Ext-3C-R_N-4R!H->O
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-Sp-2C-1R_N-2C-inRing_N-3R!H->O_Ext-3C-R_N-4R!H->O_Ext-2C-R
"""
)

