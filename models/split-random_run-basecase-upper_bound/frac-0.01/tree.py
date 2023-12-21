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
        Cpdata = ([-0.646891,-2.07012,-2.84718,-3.31278,-3.80636,-4.12598,-4.71686],'cal/mol/K','+|-',[4.5224,4.83552,4.96185,4.93887,5.14688,5.23928,5.39793]),
        H298 = (95.062,'kcal/mol','+|-',24.7249),
        S298 = (0.998363,'cal/mol/K','+|-',8.73097),
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
        Cpdata = ([-0.646891,-2.07012,-2.84718,-3.31278,-3.80636,-4.12598,-4.71686],'cal/mol/K','+|-',[4.5224,4.83552,4.96185,4.93887,5.14688,5.23928,5.39793]),
        H298 = (95.062,'kcal/mol','+|-',24.7249),
        S298 = (0.998363,'cal/mol/K','+|-',8.73097),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 2,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R",
    group = 
"""
1 * R   u1 {2,S}
2   R!H ux {1,S} {3,[S,D,T,B,Q]}
3   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.556372,-2.19245,-3.0547,-3.53634,-3.99995,-4.3002,-4.82652],'cal/mol/K','+|-',[4.98495,5.30908,5.38515,5.33856,5.59401,5.71802,5.94897]),
        H298 = (90.5506,'kcal/mol','+|-',19.7577),
        S298 = (0.86014,'cal/mol/K','+|-',9.64011),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H",
    group = 
"""
1 * R u1 {2,S}
2   C ux {1,S} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.438066,-1.70087,-2.49052,-2.89548,-3.35902,-3.57169,-3.77437],'cal/mol/K','+|-',[6.26875,6.25946,5.42302,4.13402,3,3,3]),
        H298 = (87.4821,'kcal/mol','+|-',23.1702),
        S298 = (0.692909,'cal/mol/K','+|-',9.96582),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux {1,S} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.396649,-0.93248,-1.93419,-2.60307,-3.43853,-3.86701,-4.14567],'cal/mol/K','+|-',[5.81248,5.88298,5.31728,4.19523,3,3,3]),
        H298 = (90.406,'kcal/mol','+|-',18.1648),
        S298 = (1.30043,'cal/mol/K','+|-',9.60949),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux {1,S} {3,D}
3   C   ux {2,D} {4,S}
4   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.590935,-0.791014,-1.87274,-2.57572,-3.43244,-3.86011,-4.12037],'cal/mol/K','+|-',[6.58759,6.70064,6.08092,4.80169,3,3,3]),
        H298 = (85.7982,'kcal/mol','+|-',5.60133),
        S298 = (-0.100381,'cal/mol/K','+|-',8.62837),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R!H-R",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D} {4,S}
4   R!H ux {3,S}
5   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99713,-2.7517,-3.1082,-3.21129,-3.07544,-2.95415,-3.21123],'cal/mol/K','+|-',[5.02748,8.15483,8.72583,7.44328,4.21098,3,3]),
        H298 = (87.6851,'kcal/mol','+|-',5.2),
        S298 = (0.0520238,'cal/mol/K','+|-',5.0705),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R!H-R_2R!H-inRing",
    group = 
"""
1 * R u1 {2,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C u0 {2,D} {4,S}
4   C ux {3,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.934993,-1.14101,-1.4232,-1.80004,-2.33868,-2.74608,-3.62281],'cal/mol/K','+|-',[3,4.55938,5.38841,4.90824,3.38926,3,3]),
        H298 = (87.4164,'kcal/mol','+|-',5.2),
        S298 = (-0.601749,'cal/mol/K','+|-',5.56812),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R!H-R_2R!H-inRing_1R->C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C u0 r1 {2,D} {4,S}
4   C ux r1 {3,S}
5   C ux r1 {2,[S,D,T,B,Q]}
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
[CH2]C1=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 9,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R!H-R_2R!H-inRing_N-1R->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C u0 r1 {2,D} {4,S}
4   C ux r1 {3,S}
5   C ux r1 {2,[S,D,T,B,Q]}
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
    index = 10,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R!H-R_N-2R!H-inRing",
    group = 
"""
1 * R   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {5,S}
3   C   ux {2,D} {4,S}
4   R!H u0 {3,S}
5   C   u0 {2,S}
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
    index = 11,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_1R->C",
    group = 
"""
1 * C u1 {2,S}
2   C u0 {1,S} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.70992,0.678494,-1.00271,-1.87337,-3.10261,-4.01138,-4.2652],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.2588,'kcal/mol','+|-',5.20572),
        S298 = (-5.04945,'cal/mol/K','+|-',9.69993),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 12,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_1R->C_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 {3,S}
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
    index = 13,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_1R->C_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,D}
3   C u0 {2,D} {4,S}
4   C u0 {3,S}
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
    index = 14,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_N-1R->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S} {3,D}
3   C ux {2,D} {4,S}
4   C ux {3,S}
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
    index = 15,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_N-Sp-4R!H-3R!H",
    group = 
"""
1 * R   u1 {2,S}
2   C   u0 {1,S} {3,D}
3   C   ux {2,D} {4,[B,D,T,Q]}
4   R!H u0 {3,[B,D,T,Q]}
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
    index = 16,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_1R->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux r0 {2,D}
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
    index = 17,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_N-1R->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.51039,-5.74865,-5.67656,-4.96732,-3.65708,-2.65547,-2.64093],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
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
    index = 18,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_N-1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * O u1 r0 {2,S}
2   C ux r0 {1,S} {3,D} {4,S}
3   C ux r0 {2,D}
4   O u0 r0 {2,S} {5,[S,D,T,B,Q]}
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
C=C(C)COC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 19,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_N-1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * O u1 r0 {2,S}
2   C ux r0 {1,S} {3,D} {4,S}
3   C ux r0 {2,D}
4   O u0 r0 {2,S} {5,[S,D,T,B,Q]}
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
C=C([O])OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 20,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,S}
2   R!H ux {1,S} {3,[S,T]}
3   R!H ux {2,[S,T]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65206,-2.59004,-3.51102,-4.05468,-4.51835,-4.88942,-5.67752],'cal/mol/K','+|-',[3.99707,4.57432,5.45005,6.15654,7.21398,7.36604,7.4053]),
        H298 = (92.7936,'kcal/mol','+|-',17.0173),
        S298 = (0.9954,'cal/mol/K','+|-',9.87951),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 21,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-2R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux {1,S} {3,[S,T]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,T]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.150524,-1.69501,-2.92981,-3.57987,-4.09974,-4.43189,-6.50084],'cal/mol/K','+|-',[3,3.51012,5.74085,6.14731,4.96178,3.65327,7.80907]),
        H298 = (103.684,'kcal/mol','+|-',5.2),
        S298 = (3.43242,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 22,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-2R!H-R_3R!H->O",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux {1,S} {3,[S,T]} {4,[S,D,T,B,Q]}
3   O   u0 {2,[S,T]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.278056,-1.87301,-3.1241,-3.74466,-4.22564,-4.49578,-6.77235],'cal/mol/K','+|-',[3,4.66551,7.75244,8.33998,6.73704,4.97847,10.538]),
        H298 = (104.036,'kcal/mol','+|-',5.2),
        S298 = (3.16741,'cal/mol/K','+|-',3.20514),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 23,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-2R!H-R_3R!H->O_1R-inRing",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T]} {4,[S,D,T,B,Q]}
3   O   u0 {2,[S,T]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
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
    index = 24,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-2R!H-R_3R!H->O_N-1R-inRing",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux {1,S} {3,[S,T]} {4,[S,D,T,B,Q]}
3   O   u0 {2,[S,T]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
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
[CH2]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 25,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-2R!H-R_N-3R!H->O",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 {1,S} {3,S} {4,S}
3   C   ux {2,S}
4   R!H u0 {2,S}
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
[CH2]C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 26,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R",
    group = 
"""
1 * R   u1 {2,S}
2   R!H ux {1,S} {3,[S,T]}
3   R!H ux {2,[S,T]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.17002,-3.67812,-4.58988,-5.08222,-5.39412,-5.66364,-5.74933],'cal/mol/K','+|-',[4.80702,3.69609,4.43316,5.77156,8.19165,8.84273,8.44551]),
        H298 = (91.0824,'kcal/mol','+|-',12.8013),
        S298 = (0.246446,'cal/mol/K','+|-',12.2418),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 27,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * R   u1 {2,S}
2   R!H ux {1,S} {3,[S,T]}
3   R!H ux {2,[S,T]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.20972,-4.87869,-4.976,-4.60084,-3.70143,-3.47551,-3.13907],'cal/mol/K','+|-',[7.9496,3,3,4.28699,7.84053,9.17791,10.5872]),
        H298 = (102.13,'kcal/mol','+|-',6.13407),
        S298 = (-0.0143668,'cal/mol/K','+|-',16.3882),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 28,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 {1,S} {3,S}
3   R!H u0 {2,S} {4,S}
4   O   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.496197,-4.8105,-5.3829,-5.77866,-5.95328,-6.12488,-6.18896],'cal/mol/K','+|-',[7.51992,3,3,3,3,3,3]),
        H298 = (100.363,'kcal/mol','+|-',5.2),
        S298 = (4.62698,'cal/mol/K','+|-',4.48727),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 29,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_1C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 {1,S} {3,S}
3   R!H u0 {2,S} {4,S}
4   O   u0 {3,S}
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
    index = 30,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_N-1C-inRing",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 {1,S} {3,S}
3   R!H u0 {2,S} {4,S}
4   O   u0 {3,S}
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
    index = 31,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_N-1R->C",
    group = 
"""
1 * O   u1 {2,S}
2   R!H ux {1,S} {3,[S,T]}
3   R!H ux {2,[S,T]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
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
    index = 32,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * O u1 {2,S}
2   O ux {1,S} {3,[S,T]}
3   C ux {2,[S,T]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.15414,-3.19789,-4.43543,-5.27477,-6.07119,-6.53889,-6.79343],'cal/mol/K','+|-',[3.74684,3.93943,5.33698,6.69795,8.6522,8.86662,7.23215]),
        H298 = (88.7895,'kcal/mol','+|-',5.82409),
        S298 = (0.350771,'cal/mol/K','+|-',11.833),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 33,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,[S,T]}
3   C   ux {2,[S,T]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06702,-3.61098,-5.16416,-6.16012,-7.09983,-7.52598,-7.41279],'cal/mol/K','+|-',[4.13499,3.47477,3.60481,4.7622,6.95395,7.51944,6.98225]),
        H298 = (88.5888,'kcal/mol','+|-',5.95132),
        S298 = (1.66199,'cal/mol/K','+|-',10.0687),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 34,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-5R!H-R_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,[S,T]}
3   C   ux {2,[S,T]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   u0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.1276,-3.73485,-5.25775,-6.25673,-7.35139,-7.77194,-6.84917],'cal/mol/K','+|-',[4.75794,3.93213,4.11819,5.46287,7.86447,8.53656,7.20516]),
        H298 = (88.6367,'kcal/mol','+|-',6.48217),
        S298 = (3.09285,'cal/mol/K','+|-',7.13616),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 35,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-5R!H-R_Ext-6R!H-R_7R!H->O_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,[S,T]}
3   C   ux {2,[S,T]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S} {8,D}
5   C   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   u0 {6,[S,D,T,B,Q]}
8   C   u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5408,-3.48374,-4.21002,-4.52063,-4.75263,-4.95753,-4.46587],'cal/mol/K','+|-',[7.27557,6.11413,4.17107,3,3,3,3]),
        H298 = (86.0284,'kcal/mol','+|-',5.2),
        S298 = (0.779089,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 36,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-5R!H-R_Ext-6R!H-R_7R!H->O_Ext-4BrCClFINPSSi-R_3R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   ux r0 {1,S} {3,[S,T]}
3   C   ux r1 {2,[S,T]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S} {8,D}
5   C   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   u0 {6,[S,D,T,B,Q]}
8   C   u0 r0 {4,D}
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
    index = 37,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-5R!H-R_Ext-6R!H-R_7R!H->O_Ext-4BrCClFINPSSi-R_N-3R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   ux r0 {1,S} {3,[S,T]}
3   C   ux r0 {2,[S,T]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S} {8,D}
5   C   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   u0 {6,[S,D,T,B,Q]}
8   C   u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.02085,-0.490655,-2.16813,-3.3445,-4.4717,-5.49815,-4.40975],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.9227,'kcal/mol','+|-',5.2),
        S298 = (-0.318208,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 38,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   O                      ux r0 {1,S} {3,[S,T]}
3   C                      ux {2,[S,T]} {4,[S,D,T,B,Q]}
4   C                      ux {3,[S,D,T,B,Q]} {5,S}
5   R!H                    ux {4,S} {6,[S,D,T,B,Q]}
6   R!H                    ux {5,[S,D,T,B,Q]} {7,S}
7   [F,I,Br,Cl,C,Si,P,S,N] u0 {6,S}
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
    index = 39,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,[B,D,T,Q]}
5   R!H u0 {4,[B,D,T,Q]}
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
    index = 40,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-2R!H-1R",
    group = 
"""
1 * C   u1 {2,D}
2   C   ux {1,D} {3,[S,D,T,B,Q]}
3   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.05926,-1.51283,-1.90178,-2.29436,-2.92446,-3.33233,-4.21731],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (111.055,'kcal/mol','+|-',4.63721),
        S298 = (1.62804,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 41,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-2R!H-1R_3R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C u0 r0 {1,D} {3,S}
3   O ux r0 {2,S}
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
[CH]=C(O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 42,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-2R!H-1R_N-3R!H->O",
    group = 
"""
1 * C u1 {2,D}
2   C ux {1,D} {3,[S,D,T,B,Q]}
3   C u0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.22381,-1.71216,-2.1634,-2.6466,-3.35126,-3.70184,-4.39977],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.773,'kcal/mol','+|-',2.4),
        S298 = (1.88517,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 43,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-2R!H-1R_N-3R!H->O_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,D} {4,[S,D,T,B,Q]}
2   C   ux {1,D} {3,[S,D,T,B,Q]}
3   C   u0 {2,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42519,-2.12366,-2.5621,-2.93932,-3.54212,-3.98689,-4.68394],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.107,'kcal/mol','+|-',2.4),
        S298 = (2.318,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R!H-R_2R!H-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R!H-R_2R!H-inRing_1R->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R!H-R_2R!H-inRing_N-1R->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R!H-R_N-2R!H-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_1R->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_1R->C_1C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_1R->C_N-1C-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_Sp-4R!H-3R!H_N-1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_Ext-3R!H-R_N-Sp-4R!H-3R!H
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_1R->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_N-1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_N-1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_Sp-3R!H=2R!H_N-1R->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-2R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-2R!H-R_3R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-2R!H-R_3R!H->O_1R-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-2R!H-R_3R!H->O_N-1R-inRing
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-2R!H-R_N-3R!H->O
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_1C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_1R->C_N-1C-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_4R!H->O_N-1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-5R!H-R_Ext-6R!H-R_7R!H->O
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-5R!H-R_Ext-6R!H-R_7R!H->O_Ext-4BrCClFINPSSi-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-5R!H-R_Ext-6R!H-R_7R!H->O_Ext-4BrCClFINPSSi-R_3R!H-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-5R!H-R_Ext-6R!H-R_7R!H->O_Ext-4BrCClFINPSSi-R_N-3R!H-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-2R!H-1R_N-Sp-3R!H=2R!H_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H-4BrCClFINPSSi
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-2R!H-1R
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-2R!H-1R_3R!H->O
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-2R!H-1R_N-3R!H->O
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-2R!H-1R_N-3R!H->O_Ext-1R-R
"""
)

