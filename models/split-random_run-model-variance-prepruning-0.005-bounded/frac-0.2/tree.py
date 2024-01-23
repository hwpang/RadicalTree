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
        Cpdata = ([-0.605798,-1.65644,-2.40614,-2.8275,-3.25989,-3.62766,-4.44092],'cal/mol/K','+|-',[4.12309,4.69607,4.87522,4.69325,4.12476,3.85182,3.96007]),
        H298 = (93.0172,'kcal/mol','+|-',26.8586),
        S298 = (0.379382,'cal/mol/K','+|-',9.89606),
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
        Cpdata = ([-0.605798,-1.65644,-2.40614,-2.8275,-3.25989,-3.62766,-4.44092],'cal/mol/K','+|-',[4.12309,4.69607,4.87522,4.69325,4.12476,3.85182,3.96007]),
        H298 = (93.0172,'kcal/mol','+|-',26.8586),
        S298 = (0.379382,'cal/mol/K','+|-',9.89606),
    ),
    shortDesc = """Radical correction fitted to 506 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 2,
    label = "RJ1_Ext-1R-R_2R!H-inRing",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.218816,-1.37587,-2.25838,-2.76265,-3.32392,-3.79668,-4.89387],'cal/mol/K','+|-',[3.91867,4.46756,4.7827,4.68127,4.07168,3.83147,4.19609]),
        H298 = (91.6397,'kcal/mol','+|-',39.9944),
        S298 = (1.19091,'cal/mol/K','+|-',7.83754),
    ),
    shortDesc = """Radical correction fitted to 155 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.432695,-1.28869,-1.99203,-2.38916,-2.90841,-3.34959,-4.17687],'cal/mol/K','+|-',[3.23896,3.30549,3.40859,3.298,3.24463,3.45636,3.83912]),
        H298 = (80.5735,'kcal/mol','+|-',49.0419),
        S298 = (0.0827347,'cal/mol/K','+|-',9.01698),
    ),
    shortDesc = """Radical correction fitted to 72 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.716405,-1.56666,-2.23939,-2.59398,-3.03452,-3.42973,-4.27583],'cal/mol/K','+|-',[3.30132,3.34331,3.32054,3.0415,2.66068,2.56686,2.45637]),
        H298 = (81.7072,'kcal/mol','+|-',34.6051),
        S298 = (-0.162118,'cal/mol/K','+|-',9.62885),
    ),
    shortDesc = """Radical correction fitted to 59 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C",
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
        Cpdata = ([-0.498218,-1.36696,-2.10177,-2.50161,-2.99662,-3.42362,-4.33464],'cal/mol/K','+|-',[3.20988,3.21453,3.27238,3.05109,2.70952,2.59856,2.46012]),
        H298 = (83.904,'kcal/mol','+|-',32.9058),
        S298 = (0.18085,'cal/mol/K','+|-',9.83591),
    ),
    shortDesc = """Radical correction fitted to 51 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.813348,-1.46847,-2.07098,-2.44883,-2.94626,-3.32183,-4.22604],'cal/mol/K','+|-',[3.45645,4.01173,4.14208,4.11339,3.91178,3.686,3.33376]),
        H298 = (84.8032,'kcal/mol','+|-',48.6441),
        S298 = (1.25014,'cal/mol/K','+|-',12.51),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux r1 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.980783,-1.64213,-2.22583,-2.6193,-3.14017,-3.5037,-4.36456],'cal/mol/K','+|-',[3.63656,4.32569,4.53398,4.52359,4.2408,3.92306,3.42339]),
        H298 = (88.1187,'kcal/mol','+|-',49.3163),
        S298 = (0.070945,'cal/mol/K','+|-',7.93957),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   C   ux r1 {4,D}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15535,-3.44762,-4.33099,-4.71551,-4.8172,-4.786,-5.39466],'cal/mol/K','+|-',[5.573,6.41758,6.43394,6.39254,6.37733,6.03911,5.36714]),
        H298 = (70.2075,'kcal/mol','+|-',21.5533),
        S298 = (1.85496,'cal/mol/K','+|-',13.5512),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 9,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux r1 {4,D}
6   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.68112,-4.19998,-5.13211,-5.47145,-5.50283,-5.4153,-5.92392],'cal/mol/K','+|-',[5.80571,6.28379,6.14382,6.23812,6.43103,6.1428,5.53217]),
        H298 = (74.245,'kcal/mol','+|-',13.5468),
        S298 = (2.72303,'cal/mol/K','+|-',14.9806),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 10,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_1R->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   u0 r1 {3,[S,D,T,B,Q]} {5,D} {7,[S,D,T,B,Q]}
5   C   ux r1 {4,D}
6   C   ux r1 {2,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.3702,-5.56732,-7.22422,-8.33512,-9.32534,-9.371,-9.64316],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (69.6919,'kcal/mol','+|-',4.17612),
        S298 = (13.7291,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CC(C)=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 11,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_1R->C_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C ux r1 {4,D}
6   C ux r1 {2,[S,D,T,B,Q]}
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
    index = 12,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_1R->C_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux r1 {4,D}
6   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63615,-4.51968,-4.85907,-4.67736,-4.21133,-4.06771,-4.55369],'cal/mol/K','+|-',[8.84345,9.43683,8.97632,8.209,6.41396,4.97274,3.55409]),
        H298 = (79.7686,'kcal/mol','+|-',6.11751),
        S298 = (-0.259981,'cal/mol/K','+|-',3.30496),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 13,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_1R->C_N-1C-inRing_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C   ux r1 {4,D}
6   C   ux r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
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
    index = 14,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_N-1R->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   C   u0 r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,D}
5   C   u0 r1 {4,D}
6   R!H u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0522746,-0.438196,-1.12654,-1.69175,-2.07469,-2.26881,-3.27759],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (54.0573,'kcal/mol','+|-',4.17612),
        S298 = (-1.61734,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1=C([O])OC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 15,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_Sp-6R!H-1R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {6,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   C   ux r1 {4,D}
6   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.551068,-0.898226,-1.29143,-1.57532,-2.13434,-2.5724,-3.53444],'cal/mol/K','+|-',[3.14118,2.77892,2.53619,2.53746,2.67896,2.9104,2.60129]),
        H298 = (70.5368,'kcal/mol','+|-',8.382),
        S298 = (-1.08443,'cal/mol/K','+|-',5.11575),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 16,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_Sp-6R!H-1R_6R!H->O",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]} {6,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux r1 {4,D}
6   O ux {1,S}
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
    index = 17,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_Sp-6R!H-1R_6R!H->O_Ext-6O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,D}
5   C   u0 r1 {4,D}
6   O   u0 r0 {1,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
    index = 18,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_Sp-6R!H-1R_6R!H->O_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C   ux r1 {4,D}
6   O   ux {1,S}
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
    index = 19,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_Sp-6R!H-1R_N-6R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {6,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C ux r1 {4,D}
6   C ux {1,S}
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
    index = 20,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_N-Sp-6R!H-1R",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]} {6,[B,D,T,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux r1 {4,D}
6   C ux {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.40782,-0.878094,-1.42883,-1.98467,-2.8713,-3.5252,-4.49662],'cal/mol/K','+|-',[2.00285,2.0004,2.00007,2.00012,2.01025,2.01511,2.00289]),
        H298 = (115.999,'kcal/mol','+|-',2.7252),
        S298 = (-0.0955445,'cal/mol/K','+|-',2.01547),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 21,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_N-Sp-6R!H-1R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,[B,D,T,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,D} {7,[S,D,T,B,Q]}
5   C   ux r1 {4,D}
6   C   ux r1 {1,[B,D,T,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.445597,-0.892311,-1.42277,-1.99247,-2.943,-3.6123,-4.53464],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (116.455,'kcal/mol','+|-',1.69706),
        S298 = (-0.00743587,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CC=[C]C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 22,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.244069,-0.878016,-1.54447,-1.86921,-2.28696,-2.70347,-3.75506],'cal/mol/K','+|-',[3.52646,3.55022,3.38974,3.20358,3.28223,3.49307,3.81498]),
        H298 = (64.0994,'kcal/mol','+|-',19.2865),
        S298 = (5.25939,'cal/mol/K','+|-',21.3666),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 23,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing_Ext-4R!H-R",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D} {6,[S,D,T,B,Q]}
5   C ux r0 {4,D}
6   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13832,-1.85349,-2.46634,-2.74416,-3.2337,-3.72908,-4.80494],'cal/mol/K','+|-',[2.66484,2.7716,2.91502,2.75551,2.60035,2.58465,2.62739]),
        H298 = (65.5442,'kcal/mol','+|-',14.3746),
        S298 = (2.6208,'cal/mol/K','+|-',6.8837),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 24,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing_Ext-4R!H-R_Ext-6R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   u0 r1 {3,[S,D,T,B,Q]} {5,D} {6,[S,D,T,B,Q]}
5   C   ux r0 {4,D}
6   C   ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   u0 r1 {6,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
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
    index = 25,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing_Ext-4R!H-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,D} {6,[S,D,T,B,Q]}
5   C   ux r0 {4,D} {7,[S,D,T,B,Q]}
6   C   ux r1 {4,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 26,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux r0 {4,D}
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
    index = 27,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux r0 {4,D}
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
    index = 28,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,S}
5   C   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.355273,-1.32091,-2.11574,-2.52555,-3.01947,-3.46979,-4.3839],'cal/mol/K','+|-',[3.17482,2.92684,2.94657,2.59287,2.12914,2.0954,2.10489]),
        H298 = (83.4994,'kcal/mol','+|-',24.6314),
        S298 = (-0.304187,'cal/mol/K','+|-',8.45901),
    ),
    shortDesc = """Radical correction fitted to 35 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 29,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,S}
5   C   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.228804,-1.34148,-2.246,-2.67466,-3.16189,-3.59986,-4.44049],'cal/mol/K','+|-',[3.42975,3.14253,3.09732,2.6719,2.18612,2.22941,2.22335]),
        H298 = (79.8785,'kcal/mol','+|-',12.2307),
        S298 = (-0.716506,'cal/mol/K','+|-',8.70472),
    ),
    shortDesc = """Radical correction fitted to 30 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 30,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,S}
5   C   ux {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
6   R!H u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.86317,-2.48632,-2.8968,-3.11866,-3.35342,-3.56768,-3.99557],'cal/mol/K','+|-',[2.57981,3.76657,4.37882,3.8379,3.02468,2.55814,2.79091]),
        H298 = (68.9527,'kcal/mol','+|-',24.0358),
        S298 = (0.633023,'cal/mol/K','+|-',5.91982),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 31,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_1R->C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D} {4,D}
4   C u0 {3,D} {5,S}
5   C ux {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
6   C u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8766,-1.23552,-1.31703,-1.7929,-2.50266,-3.08355,-4.56064],'cal/mol/K','+|-',[3.86798,3.32006,3.21076,3.16751,3.20967,3.23068,3.48332]),
        H298 = (59.3035,'kcal/mol','+|-',9.89052),
        S298 = (-1.06696,'cal/mol/K','+|-',7.06284),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 32,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_1R->C_Sp-6R!H-5C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D} {4,D}
4   C u0 r1 {3,D} {5,S}
5   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,S}
6   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.6641,-1.59308,-1.51357,-1.85724,-2.30837,-2.84975,-4.04422],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (56.4986,'kcal/mol','+|-',4.17612),
        S298 = (-3.29978,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=C=CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 33,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_1R->C_N-Sp-6R!H-5C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D} {4,D}
4   C u0 r1 {3,D} {5,S}
5   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,D}
6   C u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0891,-0.877954,-1.1205,-1.72857,-2.69695,-3.31736,-5.07706],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (62.1085,'kcal/mol','+|-',4.17612),
        S298 = (1.16585,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=C=CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 34,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_N-1R->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,S}
4   C   u0 {3,S} {5,S}
5   C   ux {2,[S,D,T,B,Q]} {4,S} {6,S}
6   R!H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.84974,-3.73711,-4.47656,-4.44441,-4.20418,-4.0518,-3.4305],'cal/mol/K','+|-',[3.16261,3.3921,3.50468,3.32163,3.25015,3.23185,3.33544]),
        H298 = (78.6018,'kcal/mol','+|-',12.7706),
        S298 = (2.33301,'cal/mol/K','+|-',3.74301),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 35,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_N-1R->C_6R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D} {4,S}
4   C u0 r1 {3,S} {5,S}
5   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,S}
6   C u0 r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.86598,-3.30319,-3.94239,-4.08503,-3.93878,-3.81599,-3.80553],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (74.5986,'kcal/mol','+|-',4.17612),
        S298 = (3.04101,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 36,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_N-1R->C_N-6R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D} {4,S}
4   C u0 r1 {3,S} {5,S}
5   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,S}
6   O u0 r1 {5,S}
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
    index = 37,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,S}
5   C   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0382919,-1.12572,-2.09485,-2.56221,-3.10996,-3.61303,-4.46195],'cal/mol/K','+|-',[3.35443,2.99344,2.96362,2.5981,2.23955,2.37026,2.28537]),
        H298 = (80.9358,'kcal/mol','+|-',8.73938),
        S298 = (-1.17952,'cal/mol/K','+|-',8.45002),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 38,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   C   ux {4,S} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.200041,-1.08327,-2.13931,-2.60275,-3.10105,-3.56181,-4.31558],'cal/mol/K','+|-',[3.67969,3.273,3.15043,2.70248,2.32701,2.47676,2.31945]),
        H298 = (82.4714,'kcal/mol','+|-',7.94875),
        S298 = (-1.61281,'cal/mol/K','+|-',9.26392),
    ),
    shortDesc = """Radical correction fitted to 21 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 39,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Int-6R!H-4R!H",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C u0 {3,S} {5,S} {6,S}
5   C u0 {4,S} {6,S}
6   C u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17096,0.318056,-0.710134,-1.36372,-2.41986,-3.17194,-4.48534],'cal/mol/K','+|-',[4.6299,3.84251,3.28704,3.23777,3.18097,3.17619,3.16321]),
        H298 = (79.8107,'kcal/mol','+|-',6.01444),
        S298 = (2.63771,'cal/mol/K','+|-',3.47726),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 40,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Int-6R!H-4R!H_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S} {6,S} {7,[S,D,T,B,Q]}
5   C   u0 r1 {4,S} {6,S}
6   C   u0 r1 {4,S} {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 41,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux {3,S} {5,S}
5   C   ux {4,S} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.11057,-1.2306,-2.29625,-2.69084,-3.05257,-3.44916,-4.15209],'cal/mol/K','+|-',[3.81624,3.33844,3.21762,2.76939,2.20349,2.19304,1.976]),
        H298 = (82.2283,'kcal/mol','+|-',6.59347),
        S298 = (-2.27012,'cal/mol/K','+|-',9.05233),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 42,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux {3,S} {5,S}
5   C   ux {4,S} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.323008,-1.0361,-2.13543,-2.57815,-2.98746,-3.41228,-4.18304],'cal/mol/K','+|-',[3.93102,3.31259,3.15887,2.78829,2.29795,2.31834,2.09736]),
        H298 = (81.8492,'kcal/mol','+|-',6.38861),
        S298 = (-2.0727,'cal/mol/K','+|-',9.35947),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 43,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux {4,S} {6,S}
6   R!H ux {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.754309,-0.632491,-1.97019,-2.09699,-1.9882,-2.25251,-3.14499],'cal/mol/K','+|-',[5.72428,5.38832,4.90063,3.95745,2.75304,2.41878,2.42943]),
        H298 = (80.3747,'kcal/mol','+|-',7.5479),
        S298 = (-6.8391,'cal/mol/K','+|-',8.05493),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 44,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 {4,S} {6,S}
6   R!H u0 {5,S}
7   R!H u0 {4,[S,D,T,B,Q]}
8   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.689342,-2.09682,-3.2369,-2.9033,-2.03771,-2.0518,-2.66865],'cal/mol/K','+|-',[4.8879,3.53686,3.09259,2.97657,2.9382,3.00302,2.59362]),
        H298 = (78.3694,'kcal/mol','+|-',6.86853),
        S298 = (-9.35746,'cal/mol/K','+|-',3.88318),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 45,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R_Ext-1C-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 {4,S} {6,S} {9,S}
6   R!H u0 {5,S}
7   R!H u0 {4,[S,D,T,B,Q]}
8   C   ux {1,[S,D,T,B,Q]}
9   C   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.235448,-1.76027,-3.18214,-3.07512,-2.11383,-1.91273,-2.61831],'cal/mol/K','+|-',[4.89122,4.35511,3.96521,3.69838,3.71397,3.77344,3.17169]),
        H298 = (79.7297,'kcal/mol','+|-',6.19002),
        S298 = (-9.0768,'cal/mol/K','+|-',4.99343),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 46,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R_Ext-1C-R_Ext-5C-R_6R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 r1 {4,S} {6,S} {9,S}
6   O   u0 {5,S}
7   R!H u0 {4,[S,D,T,B,Q]}
8   C   ux r0 {1,[S,D,T,B,Q]}
9   C   u0 r1 {5,S}
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
    index = 47,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R_Ext-1C-R_Ext-5C-R_N-6R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 r1 {4,S} {6,S} {9,S}
6   C   u0 r1 {5,S}
7   R!H u0 {4,[S,D,T,B,Q]}
8   C   ux r0 {1,[S,D,T,B,Q]}
9   C   u0 r1 {5,S}
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
    index = 48,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux r1 {4,S} {6,S} {8,[S,D,T,B,Q]}
6   R!H ux {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
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
    index = 49,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux {3,S} {5,S}
5   C   ux {1,[S,D,T,B,Q]} {4,S} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.103983,-0.819411,-1.65539,-2.18585,-2.80426,-3.32994,-4.29149],'cal/mol/K','+|-',[3.50929,2.79105,2.64705,2.61143,2.31293,2.36117,2.11293]),
        H298 = (83.5597,'kcal/mol','+|-',2.36994),
        S298 = (1.19357,'cal/mol/K','+|-',4.80986),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 50,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux {3,S} {5,S}
5   C   ux {1,[S,D,T,B,Q]} {4,S} {6,S}
6   R!H ux {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,S}
8   C   ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.227359,-1.35288,-2.2616,-2.73804,-3.12184,-3.49511,-4.29427],'cal/mol/K','+|-',[4.45531,2.86054,2.27343,2.45052,2.673,2.99203,2.72305]),
        H298 = (83.7973,'kcal/mol','+|-',3.02843),
        S298 = (0.316424,'cal/mol/K','+|-',5.23262),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 51,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {1,[S,D,T,B,Q]} {4,S} {6,S}
6   R!H ux {5,S} {7,S}
7   R!H u0 {6,S} {8,S} {9,[S,D,T,B,Q]}
8   C   ux {7,S}
9   R!H ux {7,[S,D,T,B,Q]}
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
    index = 52,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {1,[S,D,T,B,Q]} {4,S} {6,S}
6   C   ux {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,S}
8   C   ux {7,S}
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
    index = 53,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {1,[S,D,T,B,Q]} {4,S} {6,S}
6   O   ux {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,S}
8   C   ux {7,S}
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
    index = 54,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H-7R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {5,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 r1 {1,S} {4,S} {6,S}
6   R!H u0 {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,[B,D,T,Q]}
8   C   u0 {7,[B,D,T,Q]}
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
    index = 55,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {7,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S} {6,S}
6   C   ux {5,S}
7   R!H ux {2,[S,D,T,B,Q]}
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
    index = 56,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-3R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S} {7,[S,D,T,B,Q]}
4   C ux {3,S} {5,S}
5   C ux {4,S} {6,S}
6   C ux {5,S}
7   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.23114,-1.60541,-3.36024,-4.03113,-4.23661,-4.40022,-5.00929],'cal/mol/K','+|-',[5.76643,3.96398,3.37341,2.82994,2.61221,2.77709,2.83544]),
        H298 = (78.9822,'kcal/mol','+|-',11.4021),
        S298 = (-5.83442,'cal/mol/K','+|-',7.58321),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 57,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-3R!H-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S} {7,S}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {6,S} {8,[S,D,T,B,Q]}
6   C   u0 {5,S}
7   C   u0 {3,S}
8   R!H ux {5,[S,D,T,B,Q]}
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
    index = 58,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-3R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S} {7,[S,D,T,B,Q]}
4   C   ux {3,S} {5,S}
5   C   ux {4,S} {6,S}
6   C   ux {5,S}
7   C   ux {3,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
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
    index = 59,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S} {6,S}
6   C   ux r1 {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
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
    index = 60,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   C ux {3,S} {5,S}
5   C ux {4,S} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.27027,-2.49489,-3.34157,-3.42334,-3.47577,-3.68885,-3.95096],'cal/mol/K','+|-',[2.78588,3.76114,4.27138,3.69705,2.99064,2.90869,2.79668]),
        H298 = (86.04,'kcal/mol','+|-',5.71242),
        S298 = (-3.5534,'cal/mol/K','+|-',8.39733),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 61,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_N-1C-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {7,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S} {6,S}
6   C   ux r1 {5,S}
7   R!H ux {2,[S,D,T,B,Q]}
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
    index = 62,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_N-1C-inRing_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,S} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S} {6,S}
6   C   ux r1 {5,S}
7   R!H ux {3,[S,D,T,B,Q]}
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
    index = 63,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_N-Sp-4R!H-3R!H",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,D}
4   C   ux r1 {3,D} {5,S}
5   C   ux r1 {4,S} {6,S}
6   R!H ux {5,S}
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
    index = 64,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_N-Sp-6R!H-5C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,S}
5   C   ux {4,S} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.550936,-1.2804,-1.93291,-2.41454,-3.14244,-3.79961,-4.99515],'cal/mol/K','+|-',[2.1941,2.56512,3.04824,3.0606,2.80232,2.80665,2.69709]),
        H298 = (77,'kcal/mol','+|-',5.81236),
        S298 = (0.398877,'cal/mol/K','+|-',3.72195),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 65,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_N-Sp-6R!H-5C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r1 {1,S} {3,D} {7,S}
3   C   u0 r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H u0 {3,[S,D,T,B,Q]} {5,S}
5   C   u0 {4,S} {6,D}
6   R!H u0 {5,D}
7   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.8988,-1.81266,-2.45183,-2.84386,-3.45593,-4.1053,-5.24521],'cal/mol/K','+|-',[2.39298,3.56905,4.71464,4.87214,4.52778,4.57146,4.29353]),
        H298 = (75.4988,'kcal/mol','+|-',4.24785),
        S298 = (1.51392,'cal/mol/K','+|-',4.0218),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 66,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_N-Sp-6R!H-5C_Ext-2R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D} {7,S}
3   C   u0 r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   C   u0 r1 {4,S} {6,D}
6   R!H u0 {5,D}
7   C   u0 r0 {2,S}
8   R!H ux {1,[S,D,T,B,Q]}
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
    index = 67,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_N-Sp-6R!H-5C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C   ux r1 {4,S} {6,D}
6   O   ux r0 {5,D}
7   R!H ux {1,[S,D,T,B,Q]}
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
    index = 68,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_N-1R->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C   ux r1 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 69,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-3R!H-R",
    group = 
"""
1 * R   u1 {2,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,[S,D,T,B,Q]} {6,S}
4   R!H u0 {3,[S,D,T,B,Q]} {5,S}
5   C   u0 {4,S}
6   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.01144,-2.63001,-2.92626,-3.02354,-3.09292,-3.25848,-4.37973],'cal/mol/K','+|-',[2.49902,2.6724,3.24227,3.45289,3.31648,2.85875,4.48894]),
        H298 = (76.1606,'kcal/mol','+|-',14.0935),
        S298 = (2.88125,'cal/mol/K','+|-',16.7305),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 70,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-3R!H-R_1R->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,[S,D,T,B,Q]} {6,S}
4   R!H u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   C   u0 r1 {4,S}
6   R!H u0 {3,S}
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
    index = 71,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-3R!H-R_N-1R->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,[S,D,T,B,Q]} {6,S}
4   R!H u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   C   u0 r1 {4,S}
6   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15863,-2.38863,-2.48372,-2.52016,-2.62848,-2.94173,-3.61211],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (74.7838,'kcal/mol','+|-',1.69706),
        S298 = (-0.46414,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=C([O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 72,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_4R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,[S,D,T,B,Q]}
4   C u0 {3,[S,D,T,B,Q]} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0648806,-0.359649,-0.778873,-1.20598,-1.90116,-2.57278,-3.89021],'cal/mol/K','+|-',[2.42388,2.02676,2.43648,2.54465,2.39537,2.3249,2.29103]),
        H298 = (85.732,'kcal/mol','+|-',3.89581),
        S298 = (-0.178502,'cal/mol/K','+|-',4.46586),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 73,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_4R!H->C_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,[S,D,T,B,Q]}
4   C u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   C u0 r1 {4,S}
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
    index = 74,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_4R!H->C_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,[S,D,T,B,Q]}
4   C u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.549026,-0.243597,-0.286882,-0.64974,-1.43508,-2.15368,-3.49511],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (86.817,'kcal/mol','+|-',1.69706),
        S298 = (-1.59023,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 75,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_N-4R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,S}
4   O ux r1 {3,S} {5,S}
5   C ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.514455,-1.10218,-1.70086,-2.23092,-3.01692,-3.60863,-4.52827],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (120.638,'kcal/mol','+|-',1.69706),
        S298 = (1.16961,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[C]1=COC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 76,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C",
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
        Cpdata = ([-2.33558,-3.04863,-3.26063,-3.27944,-3.31579,-3.47514,-3.83938],'cal/mol/K','+|-',[2.45465,3.27599,3.49512,3.15971,2.78894,2.9064,2.83298]),
        H298 = (62.0667,'kcal/mol','+|-',25.4721),
        S298 = (-2.7073,'cal/mol/K','+|-',6.51855),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 77,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.50531,-3.67997,-3.86962,-3.92153,-4.30105,-4.65541,-4.89892],'cal/mol/K','+|-',[3.56923,4.32095,4.86904,4.78596,4.03415,3.96891,3.4183]),
        H298 = (46.9616,'kcal/mol','+|-',34.6014),
        S298 = (-1.53837,'cal/mol/K','+|-',11.7549),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 78,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_1R->C_Int-5BrClFINOPSSi-2R!H",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C u0 r1 {2,D} {4,D}
4   C ux r1 {3,D} {5,[S,D,T,B,Q]}
5   O u0 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
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
    index = 79,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_1R->C_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
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
    index = 80,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_1R->C_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.67405,-3.32414,-3.50649,-3.47648,-4.18092,-4.68145,-4.49804],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (35.7456,'kcal/mol','+|-',4.17612),
        S298 = (-3.72771,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]C1=C=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 81,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.25724,-2.75724,-2.97956,-2.98309,-2.86105,-2.9304,-3.35036],'cal/mol/K','+|-',[2.6384,3.31412,3.38804,2.82528,2.2484,2.20553,2.60506]),
        H298 = (66.5731,'kcal/mol','+|-',8.02925),
        S298 = (-3.24681,'cal/mol/K','+|-',3.35764),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 82,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_Ext-4R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   R!H ux r1 {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   u0 r1 {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63247,-4.5066,-4.67366,-4.00455,-2.83164,-2.33266,-1.55225],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (72.2984,'kcal/mol','+|-',4.17612),
        S298 = (-4.32244,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=C(O)C(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 83,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_Ext-3R!H-R",
    group = 
"""
1 * O u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S} {6,S}
4   C u0 {3,S} {5,S}
5   O u0 {4,S}
6   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.18191,-3.49476,-3.93997,-3.9147,-3.70024,-3.75699,-4.05035],'cal/mol/K','+|-',[4.34952,3.98794,3.64655,3.33516,3.16293,3.23036,3.31838]),
        H298 = (61.766,'kcal/mol','+|-',6.23272),
        S298 = (-4.0291,'cal/mol/K','+|-',5.33695),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 84,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_Ext-3R!H-R_6R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S} {6,S}
4   C u0 {3,S} {5,S}
5   O u0 {4,S}
6   C u0 r1 {3,S}
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
    index = 85,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_Ext-3R!H-R_N-6R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S} {6,S}
4   C u0 r1 {3,S} {5,S}
5   O u0 r1 {4,S}
6   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.23775,-4.35381,-4.58197,-4.28941,-3.72302,-3.52375,-3.69474],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (61.0618,'kcal/mol','+|-',4.17612),
        S298 = (-2.5091,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=C([O])OOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 86,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_4R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
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
    index = 87,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_N-4R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
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
    index = 88,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.674467,-0.203921,-1.02673,-1.58988,-2.41626,-3.03683,-3.79071],'cal/mol/K','+|-',[2.00006,2.32604,3.32969,4.03134,5.07422,6.01307,7.28392]),
        H298 = (76.7298,'kcal/mol','+|-',84.9814),
        S298 = (1.03826,'cal/mol/K','+|-',6.10496),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 89,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   R!H ux r0 {2,D}
4   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.610007,0.104226,-0.568979,-1.07844,-1.80597,-2.41009,-3.03244],'cal/mol/K','+|-',[1.97173,2.09738,2.94007,3.66697,4.68586,5.723,7.01907]),
        H298 = (72.0769,'kcal/mol','+|-',85.6781),
        S298 = (0.700816,'cal/mol/K','+|-',6.26887),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 90,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.499437,0.173913,-0.351125,-0.828435,-1.51031,-2.03484,-2.52742],'cal/mol/K','+|-',[1.8408,2.29841,3.46677,4.42617,5.75715,7.07574,8.6635]),
        H298 = (67.7357,'kcal/mol','+|-',102.542),
        S298 = (1.30684,'cal/mol/K','+|-',3.15497),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 91,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0391434,0.0528029,-0.240166,-0.566519,-0.923043,-1.19427,-1.01702],'cal/mol/K','+|-',[1.98281,3.32839,5.15518,6.57144,8.39634,10.2202,11.8251]),
        H298 = (39.341,'kcal/mol','+|-',124.609),
        S298 = (0.246191,'cal/mol/K','+|-',2.41189),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 92,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C_Ext-1R-R_Ext-4C-R_Int-6R!H-5R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D} {4,S}
3   C   ux r0 {2,D}
4   C   u0 r1 {2,S} {6,S}
5   R!H ux r1 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H u0 {4,S} {5,[S,D,T,B,Q]}
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
    index = 93,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C_Ext-1R-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux r1 {2,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.63682,-2.2471,-3.87898,-5.09677,-6.11994,-7.20121,-5.96913],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.4835,'kcal/mol','+|-',4.17612),
        S298 = (1.63834,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 94,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C_Ext-1R-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
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
    index = 95,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C_Ext-3C-R",
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
    index = 96,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_N-3R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.831148,-0.0351488,-1.00469,-1.57845,-2.39727,-3.16058,-4.04246],'cal/mol/K','+|-',[3.11882,2.76058,2.62328,2.70192,2.79246,2.87907,3.15292]),
        H298 = (84.1685,'kcal/mol','+|-',12.1742),
        S298 = (-0.511224,'cal/mol/K','+|-',10.7618),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 97,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_N-3R!H->C_Ext-4C-R_Int-5R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H u0 r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
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
    index = 98,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_N-3R!H->C_Ext-4C-R_5R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   C ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.92346,0.752333,-0.543949,-1.06719,-1.60787,-2.38138,-3.47565],'cal/mol/K','+|-',[4.22564,4.08856,4.06534,4.29564,4.10541,4.34565,5.43258]),
        H298 = (78.3427,'kcal/mol','+|-',7.50645),
        S298 = (-5.83748,'cal/mol/K','+|-',8.53073),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 99,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_N-3R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 100,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_N-3R!H->C_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S}
2   C                      u0 r1 {1,S} {3,D} {4,S}
3   O                      u0 r0 {2,D}
4   C                      u0 r1 {2,S} {5,[S,D,T,B,Q]}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {4,[S,D,T,B,Q]}
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
    index = 101,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C",
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
    index = 102,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R",
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
    index = 103,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   R!H u0 r0 {2,D}
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
    index = 104,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_3R!H->C",
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
    index = 105,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_N-3R!H->C",
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
    index = 106,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0381868,-1.44951,-2.48332,-3.07807,-3.67483,-4.17426,-5.4994],'cal/mol/K','+|-',[4.42259,5.28993,5.69332,5.5518,4.58219,4.01282,4.14718]),
        H298 = (100.741,'kcal/mol','+|-',15.0062),
        S298 = (2.12681,'cal/mol/K','+|-',6.16305),
    ),
    shortDesc = """Radical correction fitted to 83 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 107,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   R!H ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.217366,-1.153,-2.17513,-2.8055,-3.48862,-4.04864,-5.49105],'cal/mol/K','+|-',[3.1826,4.2075,4.77681,4.78923,4.01626,3.53748,4.11273]),
        H298 = (101.023,'kcal/mol','+|-',9.65587),
        S298 = (2.18556,'cal/mol/K','+|-',5.75797),
    ),
    shortDesc = """Radical correction fitted to 70 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 108,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   R!H ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00575634,-0.629448,-1.33825,-1.85905,-2.6338,-3.27693,-4.25988],'cal/mol/K','+|-',[2.43372,2.38706,2.16258,1.98281,1.81169,1.82689,1.55066]),
        H298 = (104.337,'kcal/mol','+|-',8.00009),
        S298 = (1.4442,'cal/mol/K','+|-',4.29249),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 109,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.540348,-1.05597,-1.60562,-2.03486,-2.76813,-3.39535,-4.18424],'cal/mol/K','+|-',[1.40501,1.66957,1.94609,2.09324,2.20708,2.2285,1.72261]),
        H298 = (106.096,'kcal/mol','+|-',6.22001),
        S298 = (1.8823,'cal/mol/K','+|-',4.25349),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 110,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.417214,-0.784381,-1.16708,-1.57851,-2.34878,-2.95369,-3.88681],'cal/mol/K','+|-',[1.64977,1.77903,2.00336,2.2235,2.53251,2.56055,1.95999]),
        H298 = (103.88,'kcal/mol','+|-',2.9276),
        S298 = (0.28743,'cal/mol/K','+|-',2.10917),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 111,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_Ext-4R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {1,S} {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]} {5,S}
5   R!H u0 r0 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
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
    index = 112,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_Ext-4R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   O   ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 113,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_3R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.722172,-1.54598,-2.17345,-2.61074,-3.32914,-3.87674,-4.71256],'cal/mol/K','+|-',[2.37326,2.3935,2.5186,2.59051,2.59967,2.49033,2.16558]),
        H298 = (109.043,'kcal/mol','+|-',2.65974),
        S298 = (3.96991,'cal/mol/K','+|-',2.2715),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 114,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_3R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   C   u0 r1 {1,S} {2,S} {5,[S,D,T,B,Q]}
4   O   u0 r0 {2,S}
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
    index = 115,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O ux {2,[S,D,T,B,Q]}
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
    index = 116,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   R!H u0 r1 {1,S} {3,S}
3   C   u0 {1,S} {2,S}
4   C   u0 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 117,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R_2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {4,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {1,S} {2,S}
4   C   u0 r0 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 118,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R_N-2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {4,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 r1 {1,S} {2,S}
4   C   u0 r0 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 119,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
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
    index = 120,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   O ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12272,-0.146756,-1.5682,-2.10404,-2.56133,-3.1571,-5.31485],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (102.721,'kcal/mol','+|-',4.17612),
        S298 = (0.564975,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 121,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   R!H ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0534371,-1.64688,-2.62526,-3.2237,-3.84118,-4.36468,-5.96361],'cal/mol/K','+|-',[3.61453,4.23212,4.59717,4.64755,4.20343,3.85796,4.83477]),
        H298 = (98.9306,'kcal/mol','+|-',5.67372),
        S298 = (2.07252,'cal/mol/K','+|-',6.68166),
    ),
    shortDesc = """Radical correction fitted to 30 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 122,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   O   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.120899,-2.02243,-2.82131,-3.33072,-3.84218,-4.2106,-5.78593],'cal/mol/K','+|-',[4.04505,5.52735,6.20485,6.09825,4.76383,3.74443,5.75111]),
        H298 = (97.6442,'kcal/mol','+|-',6.78033),
        S298 = (1.68517,'cal/mol/K','+|-',4.98169),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 123,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.173501,-1.73882,-2.79765,-3.42756,-3.94841,-4.38637,-6.58558],'cal/mol/K','+|-',[4.17484,5.9439,6.88669,6.82212,5.29185,4.18306,6.8498]),
        H298 = (95.9069,'kcal/mol','+|-',6.66617),
        S298 = (1.60054,'cal/mol/K','+|-',5.42592),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 124,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   O   u0 r1 {1,S} {3,S}
3   R!H u0 r1 {2,S}
4   C   u0 {1,S} {5,D}
5   R!H u0 {4,D}
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
    index = 125,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   C   ux {1,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.505212,-1.21771,-2.15168,-2.83575,-3.57505,-4.16277,-6.1419],'cal/mol/K','+|-',[3.8022,5.19127,5.79265,5.99189,5.01539,4.18943,6.63655]),
        H298 = (96.4515,'kcal/mol','+|-',4.48711),
        S298 = (1.55355,'cal/mol/K','+|-',5.80516),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 126,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Int-5R!H-3R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 {2,S} {5,S}
4   C   u0 {1,S} {5,S}
5   R!H u0 {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.607026,0.124052,-0.808933,-1.68136,-2.78046,-3.64781,-5.92541],'cal/mol/K','+|-',[2.40635,2.39062,2.59978,2.94618,2.7883,2.8872,7.51861]),
        H298 = (96.3676,'kcal/mol','+|-',8.07029),
        S298 = (3.11178,'cal/mol/K','+|-',6.50909),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 127,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Int-5R!H-3R!H_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {5,S}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.746465,0.138198,-1.32514,-2.55116,-3.50543,-4.46561,-9.52584],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.8569,'kcal/mol','+|-',4.17612),
        S298 = (6.16964,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]OCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 128,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Int-5R!H-3R!H_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {5,S}
4   C u0 r1 {1,S} {5,S}
5   O u0 r1 {3,S} {4,S}
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
    index = 129,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 {2,S}
4   C   u0 {1,S} {5,S}
5   R!H u0 {4,S}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.08184,-1.7415,-4.34948,-5.56856,-6.14465,-6.51496,-9.73689],'cal/mol/K','+|-',[6.2453,8.47436,8.90347,8.74397,6.07004,3.72888,8.51265]),
        H298 = (95.17,'kcal/mol','+|-',6.09777),
        S298 = (1.89603,'cal/mol/K','+|-',6.81252),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 130,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-1C-R_4C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S}
4   C   u0 r1 {1,S} {5,S}
5   R!H u0 {4,S}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.822225,-4.52122,-7.29209,-8.45077,-7.9765,-7.21358,-12.5312],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.7065,'kcal/mol','+|-',4.17612),
        S298 = (4.02941,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC[C]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 131,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-1C-R_N-4C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S}
4   C   u0 r0 {1,S} {5,S}
5   R!H u0 {4,S}
6   R!H u0 r1 {1,S}
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
    index = 132,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]}
4   C   ux r1 {1,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
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
    index = 133,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]}
4   C   ux r1 {1,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.1585,-0.818117,-0.63679,-0.825327,-1.52248,-2.20466,-3.68697],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (96.2932,'kcal/mol','+|-',1.69706),
        S298 = (-1.49672,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 134,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 {2,S}
4   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.611564,-2.4951,-2.86076,-3.1693,-3.66513,-3.91766,-4.45317],'cal/mol/K','+|-',[4.85749,6.13194,6.56256,6.31234,5.12052,4.03106,2.38034]),
        H298 = (99.9115,'kcal/mol','+|-',4.58807),
        S298 = (1.82622,'cal/mol/K','+|-',5.58009),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 135,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 {2,S}
4   O u0 {1,S} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.373245,-2.59258,-3.14245,-3.66343,-4.40468,-4.63694,-4.8657],'cal/mol/K','+|-',[6.00757,9.76948,10.3995,9.78858,7.2751,5.23933,2.79907]),
        H298 = (98.7176,'kcal/mol','+|-',5.22829),
        S298 = (3.05302,'cal/mol/K','+|-',6.58039),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 136,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S}
4   O   u0 r1 {1,S} {5,S}
5   C   u0 r1 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
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
    index = 137,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.160721,-1.41578,-2.50461,-3.15785,-3.84057,-4.4595,-6.07295],'cal/mol/K','+|-',[3.56424,3.47261,3.63775,3.85628,4.09647,4.13289,4.48134]),
        H298 = (99.8971,'kcal/mol','+|-',4.30849),
        S298 = (2.31089,'cal/mol/K','+|-',7.70843),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 138,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Int-5R!H-2C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   R!H ux r1 {2,[S,T,Q,B]} {4,S}
4   R!H ux r1 {3,S} {5,S}
5   C   u0 r1 {2,[S,D,T,B,Q]} {4,S}
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
    index = 139,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_5R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.11805,0.604251,-0.754809,-1.42444,-2.22105,-3.35072,-6.31328],'cal/mol/K','+|-',[3.39236,4.36164,4.97798,6.24436,6.98673,6.54443,4.23343]),
        H298 = (102.933,'kcal/mol','+|-',7.77578),
        S298 = (-0.702701,'cal/mol/K','+|-',10.9832),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 140,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   O   u0 {4,D}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
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
    index = 141,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_5R!H->O_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   O   ux {4,D}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 142,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.108425,-1.54852,-2.57063,-3.21664,-3.87606,-4.39989,-5.91614],'cal/mol/K','+|-',[3.69348,2.97259,3.07293,3.14379,3.34353,3.46131,4.62706]),
        H298 = (99.6826,'kcal/mol','+|-',3.84753),
        S298 = (2.31664,'cal/mol/K','+|-',6.25969),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 143,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.390814,-1.56736,-2.55909,-3.19879,-3.86743,-4.48836,-5.0967],'cal/mol/K','+|-',[3.86945,2.92911,3.10953,3.32866,3.91468,4.20517,3.6532]),
        H298 = (99.6929,'kcal/mol','+|-',4.17922),
        S298 = (1.59256,'cal/mol/K','+|-',6.53336),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 144,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_6R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   R!H u0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.27985,-1.23545,-3.28144,-4.33457,-5.35985,-6.34783,-6.17288],'cal/mol/K','+|-',[2.764,3.12357,3.20279,2.79748,3.45979,3.78426,4.84533]),
        H298 = (102.339,'kcal/mol','+|-',6.38654),
        S298 = (-0.741381,'cal/mol/K','+|-',11.8943),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 145,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_6R!H->O_Ext-1C-R",
    group = 
"""
1 * C u1 r1 {2,S} {7,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   O u0 {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O u0 {5,[S,D,T,B,Q]}
7   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.29368,-0.752489,-2.82855,-4.34899,-5.89145,-7.02274,-7.10743],'cal/mol/K','+|-',[3.45565,3.253,3.50139,3.50906,3.71817,3.79153,4.76027]),
        H298 = (103.252,'kcal/mol','+|-',7.06598),
        S298 = (2.59036,'cal/mol/K','+|-',3.63381),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 146,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_6R!H->O_Ext-1C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {7,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {8,[S,D,T,B,Q]}
4   O   u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   u0 {5,[S,D,T,B,Q]}
7   C   u0 r1 {1,S}
8   R!H ux {3,[S,D,T,B,Q]}
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
    index = 147,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.158891,-1.65394,-2.37065,-2.90251,-3.4781,-4.00329,-4.81596],'cal/mol/K','+|-',[4.29464,3.24609,3.35166,3.52265,3.96503,4.05275,3.51554]),
        H298 = (99.3348,'kcal/mol','+|-',3.63221),
        S298 = (2.20142,'cal/mol/K','+|-',4.4682),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 148,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,D}
5   C ux {4,D} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.06266,-1.20898,-1.95715,-2.39458,-2.83337,-3.35068,-4.32343],'cal/mol/K','+|-',[4.81045,4.00076,3.98081,3.48541,2.34574,1.74028,1.84226]),
        H298 = (100.262,'kcal/mol','+|-',2.8598),
        S298 = (2.21873,'cal/mol/K','+|-',5.24385),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 149,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_Ext-6BrCClFINPSSi-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C   u0 r1 {4,D} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,S}
7   R!H u0 {6,S}
8   R!H ux {3,[S,D,T,B,Q]}
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
    index = 150,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C   ux r1 {4,D} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
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
    index = 151,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C   ux r1 {4,D} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
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
    index = 152,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,S}
5   C ux {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24698,-2.34611,-3.01389,-3.69261,-4.48101,-5.01844,-5.5821],'cal/mol/K','+|-',[2.16472,2.4988,3.12251,4.29518,6.19091,6.71839,5.90449]),
        H298 = (97.7101,'kcal/mol','+|-',3.38132),
        S298 = (2.17448,'cal/mol/K','+|-',4.89618),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 153,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_Sp-4R!H-3C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.03717,-2.89529,-3.97871,-5.28644,-6.96905,-7.72434,-7.9282],'cal/mol/K','+|-',[3.1639,3.23354,3.27778,3.28094,3.34863,3.61638,3.44325]),
        H298 = (98.5972,'kcal/mol','+|-',5.96093),
        S298 = (4.07612,'cal/mol/K','+|-',3.16241),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 154,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_Sp-4R!H-3C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
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
    index = 155,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_N-Sp-4R!H-3C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,D}
4   C u0 r1 {3,D} {5,S}
5   C ux r1 {4,S} {6,S}
6   C u0 {5,S}
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
    index = 156,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,S}
3   O u0 {2,S} {4,[S,D,T,B,Q]}
4   O u0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.437526,-1.51209,-2.59295,-3.25116,-3.89276,-4.22885,-7.50041],'cal/mol/K','+|-',[3.83349,3.77242,3.73915,3.53213,2.80517,2.3154,5.26034]),
        H298 = (99.6592,'kcal/mol','+|-',4.60482),
        S298 = (3.71653,'cal/mol/K','+|-',5.46039),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 157,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 {2,S} {4,[S,D,T,B,Q]}
4   O   u0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36396,-2.59077,-3.72058,-4.26948,-4.57024,-4.6411,-8.95687],'cal/mol/K','+|-',[4.32437,3.47753,2.96093,2.8153,2.56987,2.54196,2.54207]),
        H298 = (97.9124,'kcal/mol','+|-',4.6838),
        S298 = (4.65178,'cal/mol/K','+|-',6.86035),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 158,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Ext-1C-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   C u0 r1 {1,S} {3,S}
3   O u0 {2,S} {4,[S,D,T,B,Q]}
4   O u0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.51724,-2.82142,-3.9293,-4.4138,-4.67158,-4.72442,-8.99073],'cal/mol/K','+|-',[5.16266,4.00372,3.35735,3.24895,2.97095,2.94828,2.97193]),
        H298 = (97.7242,'kcal/mol','+|-',5.39911),
        S298 = (5.48282,'cal/mol/K','+|-',7.29303),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 159,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Ext-1C-R_6R!H->C_Ext-2C-R",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   C u0 r1 {1,S} {3,S} {7,S}
3   O u0 {2,S} {4,[S,D,T,B,Q]}
4   O u0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   C u0 {1,S}
7   C u0 {2,S}
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
    index = 160,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Ext-1C-R_6R!H->C_Ext-2C-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {7,S}
3   O   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   O   u0 r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
6   C   u0 r0 {1,S}
7   C   u0 r0 {2,S} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
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
    index = 161,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Ext-1C-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {6,S}
2   C                      u0 r1 {1,S} {3,S}
3   O                      u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   O                      u0 r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C                      ux r1 {4,[S,D,T,B,Q]}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {1,S}
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
    index = 162,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Int-5BrCClFINPSSi-1C_Ext-5BrCClFINPSSi-R_Ext-5BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S} {4,S}
4   O   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 163,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.48458,-0.914652,-2.13348,-2.84925,-3.55328,-4.10926,-5.61942],'cal/mol/K','+|-',[3.23676,4.87084,5.79087,5.78147,4.56511,3.84212,3.93287]),
        H298 = (100.98,'kcal/mol','+|-',11.7804),
        S298 = (2.66046,'cal/mol/K','+|-',5.50587),
    ),
    shortDesc = """Radical correction fitted to 30 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 164,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.921046,-3.25691,-4.81394,-5.36417,-5.14713,-4.91804,-7.11974],'cal/mol/K','+|-',[3.85868,6.07108,7.25115,7.33928,5.86498,4.47275,4.67194]),
        H298 = (97.7046,'kcal/mol','+|-',22.6908),
        S298 = (4.65794,'cal/mol/K','+|-',7.2248),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 165,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.017,-3.14381,-4.57603,-5.08003,-4.79813,-4.58641,-7.09572],'cal/mol/K','+|-',[4.58736,7.17882,8.52649,8.57969,6.75944,5.14039,5.63211]),
        H298 = (91.1471,'kcal/mol','+|-',9.23784),
        S298 = (4.1577,'cal/mol/K','+|-',7.9768),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 166,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux {1,S}
5   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.35182,-3.5707,-5.09678,-5.54283,-5.13115,-4.77396,-7.4632],'cal/mol/K','+|-',[5.24482,8.15781,9.74031,10.0256,8.02017,6.17881,6.69133]),
        H298 = (89.2926,'kcal/mol','+|-',7.69069),
        S298 = (4.21959,'cal/mol/K','+|-',9.72228),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 167,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C_3R!H-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux r1 {2,[S,T,Q,B]} {5,S}
4   C   ux {1,S}
5   C   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.07325,-3.22131,-4.88764,-5.50082,-5.31957,-5.07994,-8.0767],'cal/mol/K','+|-',[5.85447,9.22738,11.1803,11.5601,9.19153,6.93352,7.02343]),
        H298 = (88.5681,'kcal/mol','+|-',7.98132),
        S298 = (4.47505,'cal/mol/K','+|-',11.1336),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 168,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C_3R!H-inRing_Int-5C-2R!H",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 r1 {1,S} {3,S} {5,S}
3   O u0 r1 {2,S} {5,S}
4   C ux {1,S}
5   C ux {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.75679,-2.28494,-3.16821,-3.59558,-3.8201,-4.17048,-8.68747],'cal/mol/K','+|-',[6.2335,7.95374,8.53906,9.11844,8.22323,7.08411,6.44196]),
        H298 = (89.53,'kcal/mol','+|-',10.4978),
        S298 = (4.02879,'cal/mol/K','+|-',14.3391),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 169,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C_3R!H-inRing_Int-5C-2R!H_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {5,S}
3   O   u0 r1 {2,S} {5,S}
4   C   ux {1,S}
5   C   ux r1 {2,S} {3,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.65601,-4.8652,-5.97257,-6.61936,-6.50388,-6.41171,-10.6717],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (92.5985,'kcal/mol','+|-',4.17612),
        S298 = (8.97362,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 170,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C_3R!H-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux r1 {2,[S,T,Q,B]} {5,S}
4   C   ux {1,S}
5   C   ux r1 {3,S}
6   R!H ux {1,[S,D,T,B,Q]}
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
    index = 171,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C_N-3R!H-inRing",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,S}
3   R!H u0 r0 {2,S} {5,[S,D,T,B,Q]}
4   R!H ux {1,S}
5   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.46613,-4.96824,-5.93333,-5.71085,-4.37747,-3.55004,-5.00923],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (92.1907,'kcal/mol','+|-',4.17612),
        S298 = (3.19774,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1([CH]O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 172,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_N-5R!H->C",
    group = 
"""
1 * C     u1 r0 {2,S} {4,S}
2   C     u0 r1 {1,S} {3,S}
3   [C,O] u0 {2,S} {5,S}
4   C     ux {1,S}
5   O     ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.179957,-2.0766,-3.27415,-3.92303,-3.96557,-4.11753,-6.177],'cal/mol/K','+|-',[4.15218,6.25417,6.82541,5.78613,4.23567,3.49649,3.2607]),
        H298 = (95.7832,'kcal/mol','+|-',8.09945),
        S298 = (4.00298,'cal/mol/K','+|-',3.50334),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 173,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_N-5R!H->C_Ext-1C-R",
    group = 
"""
1 * C     u1 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C     u0 r1 {1,S} {3,S}
3   [C,O] u0 r1 {2,S} {5,S}
4   C     ux {1,S}
5   O     ux r1 {3,S}
6   R!H   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.771396,-0.168892,-1.13563,-2.20987,-2.96927,-3.5901,-5.89589],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.8236,'kcal/mol','+|-',4.17612),
        S298 = (3.4699,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](CO)C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 174,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   C   ux {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.697142,-3.52079,-5.36906,-6.02716,-5.96147,-5.69186,-7.17581],'cal/mol/K','+|-',[3.11113,4.11045,4.70106,4.90204,4.27495,3.44377,3.04482]),
        H298 = (113.006,'kcal/mol','+|-',8.71363),
        S298 = (5.82515,'cal/mol/K','+|-',6.20989),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 175,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3R!H-R_3R!H->C",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]} {4,D}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C u0 r0 {1,D}
5   O u0 {3,[S,D,T,B,Q]}
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
    index = 176,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3R!H-R_N-3R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {4,[B,D,T,Q]}
2   C u0 r1 {1,S} {3,S}
3   O u0 {2,S} {5,S}
4   C ux {1,[B,D,T,Q]}
5   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.1435,-3.72995,-5.5208,-6.14442,-6.09659,-5.88879,-7.30645],'cal/mol/K','+|-',[3.35309,5.42294,6.34933,6.66308,5.72528,4.41079,3.84693]),
        H298 = (111.13,'kcal/mol','+|-',7.46734),
        S298 = (6.05186,'cal/mol/K','+|-',8.51813),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 177,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3R!H-R_N-3R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[B,D,T,Q]}
2   C   u0 r1 {1,S} {3,S} {6,[S,D,T,B,Q]}
3   O   u0 r1 {2,S} {5,S}
4   C   ux {1,[B,D,T,Q]}
5   O   ux r1 {3,S}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 178,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.807404,0.138815,-0.719853,-1.39611,-2.31567,-3.0238,-4.52877],'cal/mol/K','+|-',[2.36032,4.1022,4.76182,4.47906,3.06646,2.0234,2.17067]),
        H298 = (100.535,'kcal/mol','+|-',3.2775),
        S298 = (1.56225,'cal/mol/K','+|-',3.78651),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 179,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.649568,-0.169539,-1.09895,-1.75571,-2.55441,-3.16606,-4.68279],'cal/mol/K','+|-',[2.89365,5.34875,6.23674,5.86121,4.00069,2.62853,2.82145]),
        H298 = (101.275,'kcal/mol','+|-',3.21622),
        S298 = (1.31688,'cal/mol/K','+|-',4.66538),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 180,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,S} {4,[S,D,T,B,Q]}
3   O u0 {2,S} {4,[S,D,T,B,Q]}
4   C u0 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.14564,0.964717,0.259347,-0.478926,-1.71624,-2.67455,-4.143],'cal/mol/K','+|-',[2.19632,2.13656,1.95671,1.84115,1.70683,1.65472,1.6494]),
        H298 = (101.141,'kcal/mol','+|-',2.76801),
        S298 = (0.332578,'cal/mol/K','+|-',1.8198),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 181,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_4R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   u0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.899963,0.582147,-0.0497071,-0.721975,-1.85499,-2.73942,-4.11456],'cal/mol/K','+|-',[2.62025,2.06973,2.00793,2.00713,2.00778,2.01044,2.02196]),
        H298 = (101.494,'kcal/mol','+|-',3.22854),
        S298 = (0.543417,'cal/mol/K','+|-',2.05504),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 182,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_4R!H->C_Ext-2R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C u0 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
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
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_4R!H->C_Ext-2R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      u0 r1 {1,S} {3,S} {4,[S,D,T,B,Q]} {5,S}
3   O                      u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C                      u0 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.301452,0.393801,-0.112732,-0.781755,-1.91743,-2.81177,-4.21963],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.257,'kcal/mol','+|-',1.69706),
        S298 = (0.71044,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 184,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,S}
3   O ux {2,[S,T,Q,B]} {4,S}
4   O ux {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2107,-4.423,-6.19257,-6.54367,-5.69758,-5.00925,-6.70702],'cal/mol/K','+|-',[3.16254,3.3278,3.23117,3.1632,3.21658,3.21882,3.32347]),
        H298 = (102.484,'kcal/mol','+|-',8.72969),
        S298 = (5.008,'cal/mol/K','+|-',3.54207),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 185,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]} {4,S}
4   O ux r1 {2,S} {3,S}
5   C ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.22515,-4.78944,-6.42721,-6.57061,-5.4895,-4.79688,-6.34552],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (104.757,'kcal/mol','+|-',4.17612),
        S298 = (4.44383,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C=COC(C)=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 186,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,[S,D,T,B,Q]}
2   C                      ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
3   O                      ux r1 {2,[S,T,Q,B]} {4,S}
4   O                      ux r1 {2,S} {3,S}
5   C                      ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,[S,D,T,B,Q]}
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
    index = 187,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_N-3R!H->O",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.05731,0.627041,-0.119614,-0.826733,-1.93765,-2.79855,-4.28491],'cal/mol/K','+|-',[2.37166,2.0507,1.89316,1.88776,1.86447,1.83541,1.84811]),
        H298 = (99.3966,'kcal/mol','+|-',2.98274),
        S298 = (1.95076,'cal/mol/K','+|-',3.10531),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 188,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_N-3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,S}
3   C ux r1 {2,[S,T,Q,B]} {4,S}
4   C ux r1 {2,S} {3,S} {5,S}
5   O u0 r0 {4,S}
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
    index = 189,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_N-3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S} {3,S} {4,[S,D,T,B,Q]}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   C u0 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
5   O ux {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.790075,0.477849,-0.13803,-0.779326,-1.88906,-2.78492,-4.23717],'cal/mol/K','+|-',[2.0023,2.05905,2.08802,2.05854,2.0251,2.01101,2.00346]),
        H298 = (99.1987,'kcal/mol','+|-',2.45931),
        S298 = (1.66836,'cal/mol/K','+|-',3.10426),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 190,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_N-3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
5   O   ux {4,[B,D,T,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.824009,0.304763,-0.350109,-0.951655,-2.00144,-2.85924,-4.27876],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (99.3886,'kcal/mol','+|-',1.69706),
        S298 = (2.50774,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 191,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.759072,-0.079449,-0.9418,-1.64994,-2.69967,-3.42097,-4.59632],'cal/mol/K','+|-',[1.97866,1.88858,1.8946,1.89304,1.72683,1.56654,1.55454]),
        H298 = (101.926,'kcal/mol','+|-',4.06434),
        S298 = (2.42574,'cal/mol/K','+|-',2.57741),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 192,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.451054,-0.155809,-0.766705,-1.36935,-2.45983,-3.24828,-4.417],'cal/mol/K','+|-',[1.80361,1.83749,1.77116,1.73319,1.72076,1.70009,1.64225]),
        H298 = (101.818,'kcal/mol','+|-',2.74753),
        S298 = (2.66221,'cal/mol/K','+|-',2.24755),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 193,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-6R!H-3R!H",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   C   u0 {2,S} {5,[S,D,T,B,Q]} {6,S}
4   R!H u0 {2,S} {5,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.584148,0.0117479,-0.600817,-1.23271,-2.40938,-3.231,-4.40164],'cal/mol/K','+|-',[2.17889,2.17844,2.06888,2.05583,2.12783,2.10716,2.01369]),
        H298 = (101.299,'kcal/mol','+|-',2.59255),
        S298 = (2.23914,'cal/mol/K','+|-',2.11515),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 194,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S} {7,[S,D,T,B,Q]}
3   C   u0 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
4   R!H u0 r1 {2,S} {5,[S,D,T,B,Q]}
5   R!H ux r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C   ux {3,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.889838,0.317037,-0.413652,-1.06447,-2.15256,-2.99645,-4.31876],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (101.646,'kcal/mol','+|-',1.69706),
        S298 = (2.48251,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)OOC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 195,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-6R!H-3R!H",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[B,D,T,Q]}
4   R!H ux r1 {2,[S,D,T,B,Q]} {5,S}
5   R!H u0 r1 {3,[S,D,T,B,Q]} {4,S}
6   C   u0 r0 {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.184867,-0.490924,-1.09848,-1.64265,-2.56072,-3.28283,-4.44772],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.855,'kcal/mol','+|-',1.69706),
        S298 = (3.50835,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)OCC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 196,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   C u0 r1 {2,S} {5,S}
4   C u0 r1 {2,S} {5,S}
5   C u0 r1 {3,S} {4,S} {6,[S,D,T,B,Q]}
6   C u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.85094,-0.143989,-1.0515,-1.76464,-2.8967,-3.60781,-4.78291],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.1457,'kcal/mol','+|-',4.17612),
        S298 = (0.802135,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1CC(=C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 197,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {5,S}
4   C ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {3,S} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.86821,0.239172,-1.54356,-2.64478,-3.50056,-3.97517,-5.17551],'cal/mol/K','+|-',[3.36024,4.41088,4.24069,3.48305,3.255,3.16544,3.22099]),
        H298 = (104.798,'kcal/mol','+|-',8.67473),
        S298 = (2.35076,'cal/mol/K','+|-',5.07405),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 198,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-5R!H-R_N-6R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {5,S}
4   C   ux r1 {2,[S,D,T,B,Q]} {5,S}
5   C   ux r1 {3,S} {4,S} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.26995,1.32636,-0.54459,-2.12859,-3.22784,-3.92513,-5.39196],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (102.552,'kcal/mol','+|-',4.17612),
        S298 = (0.947817,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)CC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 199,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.46227,-0.0228981,-3.08964,-4.60546,-6.13241,-7.54823,-7.08454],'cal/mol/K','+|-',[6.18287,7.42021,7.71473,8.76056,8.68315,7.58888,4.9145]),
        H298 = (119.444,'kcal/mol','+|-',20.8019),
        S298 = (0.162322,'cal/mol/K','+|-',8.08821),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 200,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   u0 r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.34069,2.35038,-0.601743,-1.71696,-3.27328,-5.10919,-5.75448],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (112.392,'kcal/mol','+|-',4.17612),
        S298 = (-2.46967,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1OOC(O)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 201,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C     u1 r0 {2,[S,D,T,B,Q]}
2   C     ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   [C,O] ux {2,[S,T,Q,B]}
4   [C,O] ux {2,[S,D,T,B,Q]}
5   [C,O] ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.051398,-2.37829,-4.12289,-5.05095,-5.73872,-6.72573,-8.66385],'cal/mol/K','+|-',[3.30207,2.96212,2.82367,2.85407,3.25175,4.20224,4.32373]),
        H298 = (97.2452,'kcal/mol','+|-',11.8202),
        S298 = (5.11324,'cal/mol/K','+|-',7.19593),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 202,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_4R!H->O",
    group = 
"""
1 * C     u1 r0 {2,[S,D,T,B,Q]}
2   C     ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,S}
3   [C,O] ux r1 {2,[S,T,Q,B]} {6,S}
4   O     ux {2,[S,D,T,B,Q]}
5   [C,O] u0 r1 {2,S} {7,S}
6   [C,O] ux r1 {3,S}
7   [C,O] u0 r1 {5,S}
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
    index = 203,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H->O",
    group = 
"""
1 * C     u1 r0 {2,[S,D,T,B,Q]}
2   C     u0 r1 {1,[S,D,T,B,Q]} {3,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   [C,O] u0 {2,S} {6,[S,D,T,B,Q]}
4   C     ux {2,[S,D,T,B,Q]}
5   [C,O] ux {2,[S,D,T,B,Q]} {7,S}
6   [C,O] u0 {3,[S,D,T,B,Q]}
7   [C,O] ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.220186,-2.21114,-3.9219,-4.78588,-5.17067,-5.77561,-8.6166],'cal/mol/K','+|-',[4.08704,3.68029,3.41222,3.35736,3.17334,3.2123,5.83115]),
        H298 = (100.196,'kcal/mol','+|-',7.67452),
        S298 = (3.17878,'cal/mol/K','+|-',3.22765),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 204,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H->O_Sp-6R!H=3R!H",
    group = 
"""
1 * C     u1 r0 {2,[S,D,T,B,Q]}
2   C     u0 r1 {1,[S,D,T,B,Q]} {3,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   [C,O] u0 r1 {2,S} {6,D}
4   C     ux {2,[S,D,T,B,Q]}
5   [C,O] ux r1 {2,[S,D,T,B,Q]} {7,S}
6   [C,O] u0 {3,D}
7   [C,O] ux r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.1356,-1.54551,-3.46868,-4.38716,-5.07708,-5.97526,-6.88447],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (98.4628,'kcal/mol','+|-',4.17612),
        S298 = (2.95026,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 205,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H->O_N-Sp-6R!H=3R!H",
    group = 
"""
1 * C     u1 r0 {2,[S,D,T,B,Q]}
2   C     u0 r1 {1,[S,D,T,B,Q]} {3,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   [C,O] u0 r1 {2,S} {6,S}
4   C     ux {2,[S,D,T,B,Q]}
5   [C,O] ux r1 {2,[S,D,T,B,Q]} {7,S}
6   [C,O] u0 r1 {3,S}
7   [C,O] ux r1 {5,S}
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
    index = 206,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.87993,-3.58643,-4.70442,-5.04245,-5.01685,-5.07958,-5.55957],'cal/mol/K','+|-',[8.8938,9.43938,9.31877,8.78563,7.29559,6.54473,4.74212]),
        H298 = (97.8357,'kcal/mol','+|-',42.2716),
        S298 = (1.7034,'cal/mol/K','+|-',8.92844),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 207,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_Int-4R!H-2R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31489,-1.34492,-1.67482,-1.87416,-2.26467,-2.65897,-3.90774],'cal/mol/K','+|-',[2.18945,2.01394,2.08997,2.08994,2.02792,2.06021,3.34423]),
        H298 = (85.6225,'kcal/mol','+|-',54.5021),
        S298 = (-1.17085,'cal/mol/K','+|-',2.2151),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 208,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_Int-4R!H-2R!H_Ext-3R!H-R",
    group = 
"""
1 * O u1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,S}
4   O u0 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79998,-1.3025,-1.62796,-1.76416,-2.10899,-2.65152,-3.26679],'cal/mol/K','+|-',[3.38383,3.39632,3.56612,3.55392,3.3894,3.46322,3.16956]),
        H298 = (51.042,'kcal/mol','+|-',10.9072),
        S298 = (-1.69887,'cal/mol/K','+|-',3.36823),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 209,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_Int-4R!H-2R!H_Ext-3R!H-R_Ext-2R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,S}
4   O   u0 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   O   u0 {3,S}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 210,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_Int-4R!H-2R!H_Ext-2R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
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
    index = 211,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.65336,-4.13167,-5.99507,-6.35797,-6.18668,-6.16474,-6.4485],'cal/mol/K','+|-',[5.65533,12.7201,12.122,10.7542,7.51245,5.37101,3.58731]),
        H298 = (117.194,'kcal/mol','+|-',19.8615),
        S298 = (2.28743,'cal/mol/K','+|-',13.1526),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 212,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]} {4,S}
4   O ux {3,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.609732,-5.97289,-7.49748,-7.47675,-6.58075,-6.21224,-6.09698],'cal/mol/K','+|-',[2.97508,12.6691,12.8611,11.9418,8.94958,6.51031,3.93755]),
        H298 = (112.957,'kcal/mol','+|-',12.5699),
        S298 = (3.09628,'cal/mol/K','+|-',15.5869),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 213,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_5R!H->C_Ext-2R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   ux r1 {3,S}
5   C   ux r1 {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 214,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {5,S}
3   O   u0 r1 {2,S} {4,S}
4   O   u0 r1 {3,S}
5   C   u0 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 215,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_N-5R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r1 {1,S} {3,S} {5,S}
3   O                      u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   O                      u0 r1 {3,[S,D,T,B,Q]}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.44264,1.392,-1.48784,-3.00163,-5.00446,-6.02225,-7.50305],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (129.904,'kcal/mol','+|-',4.17612),
        S298 = (-0.139146,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1(O)OOC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 216,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.52811,-5.61589,-7.00445,-7.47515,-7.10839,-6.87412,-6.66544],'cal/mol/K','+|-',[13.321,11.2683,9.80567,8.91857,8.22135,8.35001,6.04051]),
        H298 = (104.469,'kcal/mol','+|-',6.7577),
        S298 = (4.39785,'cal/mol/K','+|-',7.28129),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 217,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2R!H-R_Ext-4BrCClFINPSSi-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
7   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.28608,-8.11942,-9.28225,-9.51217,-8.74527,-8.40202,-6.49686],'cal/mol/K','+|-',[14.6489,11.2835,9.03745,8.26767,9.21633,10.051,7.68891]),
        H298 = (106.257,'kcal/mol','+|-',5.13212),
        S298 = (5.42651,'cal/mol/K','+|-',3.60868),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 218,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2R!H-R_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {5,S}
3   O   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   u0 r1 {2,S} {7,S}
6   R!H ux {4,[S,D,T,B,Q]}
7   C   u0 {5,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.6085,-14.3913,-14.2223,-13.9804,-13.7644,-13.977,-3.52919],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (106.267,'kcal/mol','+|-',4.17612),
        S298 = (6.87366,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1CC(=O)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 219,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2R!H-R_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-2R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {6,S}
5   C   ux r1 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux r1 {4,S}
7   C   ux {5,[S,D,T,B,Q]}
8   R!H ux {2,[S,D,T,B,Q]}
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
    index = 220,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O_3R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,S}
4   C ux r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.88511,-4.65719,-6.39255,-7.02503,-6.12924,-5.30204,-8.65731],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (103.547,'kcal/mol','+|-',4.17612),
        S298 = (7.20819,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1([O])CCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 221,
    label = "RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O_N-3R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {4,S}
4   C ux r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.10281,0.935985,-0.782946,-1.81422,-3.1769,-3.86251,-5.1793],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.027,'kcal/mol','+|-',4.17612),
        S298 = (-1.49849,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1(O)OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 222,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.767594,-1.77374,-2.46792,-2.85461,-3.23313,-3.557,-4.25154],'cal/mol/K','+|-',[4.17408,4.78012,4.91993,4.70907,4.15694,3.86283,3.8057]),
        H298 = (93.5606,'kcal/mol','+|-',19.4112),
        S298 = (0.040085,'cal/mol/K','+|-',10.5796),
    ),
    shortDesc = """Radical correction fitted to 351 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 223,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24428,-2.27575,-2.99744,-3.40512,-3.74835,-4.04749,-4.62711],'cal/mol/K','+|-',[4.25476,4.89106,5.20076,5.19804,4.91246,4.62998,4.62633]),
        H298 = (89.2682,'kcal/mol','+|-',15.4116),
        S298 = (-0.801502,'cal/mol/K','+|-',10.1705),
    ),
    shortDesc = """Radical correction fitted to 169 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 224,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0618921,-0.818804,-1.51444,-1.98525,-2.58641,-3.02148,-3.72371],'cal/mol/K','+|-',[3.64876,3.79041,3.78456,3.7421,3.75651,3.56376,3.76122]),
        H298 = (90.2879,'kcal/mol','+|-',19.7053),
        S298 = (0.0858928,'cal/mol/K','+|-',10.6016),
    ),
    shortDesc = """Radical correction fitted to 57 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 225,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.045697,-0.804835,-1.51479,-1.99408,-2.5957,-3.02975,-3.71972],'cal/mol/K','+|-',[3.76084,3.81302,3.78492,3.769,3.85883,3.7017,3.92]),
        H298 = (89.3869,'kcal/mol','+|-',19.3686),
        S298 = (-0.0902519,'cal/mol/K','+|-',10.9575),
    ),
    shortDesc = """Radical correction fitted to 52 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 226,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,D}
2   O   u0 r0 {1,[S,D,T,B,Q]}
3   R!H u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19137,0.254889,-0.69253,-1.42061,-2.51399,-3.30214,-4.39864],'cal/mol/K','+|-',[5.25514,5.55703,5.17808,4.68511,3.69548,2.92848,2.51808]),
        H298 = (102.329,'kcal/mol','+|-',18.6501),
        S298 = (0.769386,'cal/mol/K','+|-',7.4517),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 227,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C_3R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]} {3,D}
2   O u0 r0 {1,[S,D,T,B,Q]}
3   C u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.847016,-0.306056,-1.2162,-1.84796,-2.76583,-3.40742,-4.35277],'cal/mol/K','+|-',[3.91799,3.14908,2.87694,2.6767,2.31823,1.9992,2.03807]),
        H298 = (103.026,'kcal/mol','+|-',21.0531),
        S298 = (1.50127,'cal/mol/K','+|-',7.39859),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 228,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C_3R!H->C_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,D}
2   O   u0 r0 {1,[S,D,T,B,Q]}
3   C   u0 {1,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.959343,0.133435,-0.671253,-1.34858,-2.41208,-3.22848,-4.60264],'cal/mol/K','+|-',[6.07972,4.29566,3.42142,3.14742,2.85101,2.58898,2.52968]),
        H298 = (110.13,'kcal/mol','+|-',10.5556),
        S298 = (-0.478222,'cal/mol/K','+|-',6.96378),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 229,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-2O-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,D}
2   O   u0 r0 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   u0 r0 {1,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 230,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C_N-3R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]} {3,D}
2   O u0 r0 {1,[S,D,T,B,Q]}
3   O u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22442,1.93772,0.87849,-0.138578,-1.75848,-2.98632,-4.53624],'cal/mol/K','+|-',[10.2869,11.2766,10.608,9.79885,7.99344,6.57904,5.47776]),
        H298 = (97.7603,'kcal/mol','+|-',6.02331),
        S298 = (-1.42626,'cal/mol/K','+|-',9.34275),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 231,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C_N-3R!H->C_Ext-2O-R_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,D}
2   O   u0 r0 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
3   O   u0 r0 {1,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.68528,5.76464,4.45847,3.14048,0.837071,-0.946603,-2.95487],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.3419,'kcal/mol','+|-',4.17612),
        S298 = (-4.53445,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]OC(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 232,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,T,Q,B]}
2   O   ux r0 {1,[S,D,T,B,Q]}
3   R!H ux {1,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.169403,-0.910807,-1.59702,-2.05142,-2.60388,-3.00251,-3.65183],'cal/mol/K','+|-',[3.59893,3.6494,3.68792,3.74206,3.94322,3.82145,4.05431]),
        H298 = (88.1593,'kcal/mol','+|-',17.8217),
        S298 = (-0.176216,'cal/mol/K','+|-',11.3112),
    ),
    shortDesc = """Radical correction fitted to 47 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 233,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,T,Q,B]}
2   O   ux r0 {1,[S,D,T,B,Q]}
3   R!H ux {1,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.202012,-0.981293,-1.68465,-2.1279,-2.62851,-2.9744,-3.52845],'cal/mol/K','+|-',[3.76188,3.79425,3.83831,3.91725,4.16479,4.03815,4.22352]),
        H298 = (86.9414,'kcal/mol','+|-',17.6232),
        S298 = (-0.551942,'cal/mol/K','+|-',11.737),
    ),
    shortDesc = """Radical correction fitted to 43 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 234,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,T,Q,B]}
2   O   ux r0 {1,[S,D,T,B,Q]}
3   C   ux {1,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.728399,-1.48636,-2.13524,-2.4934,-2.81187,-2.92463,-3.10108],'cal/mol/K','+|-',[3.49486,3.29399,3.47859,3.82599,4.43915,4.52878,4.91175]),
        H298 = (82.943,'kcal/mol','+|-',15.4899),
        S298 = (-1.57016,'cal/mol/K','+|-',10.895),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 235,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S}
3   C   ux {1,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.1542,-1.85562,-2.38783,-2.55599,-2.55997,-2.44319,-2.29978],'cal/mol/K','+|-',[3.51707,3.27907,3.72158,4.34649,5.09201,4.95487,4.65854]),
        H298 = (78.8726,'kcal/mol','+|-',11.2109),
        S298 = (-3.0992,'cal/mol/K','+|-',11.2212),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 236,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S}
3   C   ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08727,-1.74712,-2.21828,-2.38271,-2.37723,-2.20399,-2.45821],'cal/mol/K','+|-',[4.32824,4.00941,4.54835,5.43033,6.75801,6.75287,6.25302]),
        H298 = (83.7408,'kcal/mol','+|-',8.82052),
        S298 = (-2.14956,'cal/mol/K','+|-',14.0612),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 237,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S}
3   C   ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.20528,-1.88922,-2.37973,-2.55849,-2.53916,-2.32085,-2.46526],'cal/mol/K','+|-',[4.44536,4.05681,4.60241,5.53008,6.97711,7.02562,6.55896]),
        H298 = (83.5035,'kcal/mol','+|-',8.82927),
        S298 = (-2.09709,'cal/mol/K','+|-',14.7478),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 238,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-2O-R",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S} {6,S}
3   C ux {1,[S,T,Q,B]} {4,D} {5,S}
4   C ux {3,D}
5   C u0 {3,S}
6   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0995426,-1.63586,-2.97903,-3.91987,-4.84812,-4.8216,-4.67938],'cal/mol/K','+|-',[3.12387,2.6455,4.91785,6.83019,8.40288,7.63015,5.48359]),
        H298 = (86.3179,'kcal/mol','+|-',9.51537),
        S298 = (2.93453,'cal/mol/K','+|-',14.001),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 239,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-2O-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S} {6,S}
3   C   ux {1,[S,T,Q,B]} {4,D} {5,S}
4   C   ux {3,D}
5   C   u0 r0 {3,S}
6   C   u0 r0 {2,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.946677,-2.17905,-4.9151,-6.83158,-8.54202,-8.15208,-6.85014],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (88.5716,'kcal/mol','+|-',1.69706),
        S298 = (9.13129,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([CH]OC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 240,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-2O-R_Ext-5C-R",
    group = 
"""
1 * C   u1 {2,S} {3,S}
2   O   u0 r0 {1,S} {6,S}
3   C   u0 {1,S} {4,D} {5,S}
4   C   u0 {3,D}
5   C   u0 {3,S} {7,D}
6   C   u0 {2,S}
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
    index = 241,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-2O-R_Ext-5C-R_7R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   O u0 r0 {1,S} {6,S}
3   C u0 r0 {1,S} {4,D} {5,S}
4   C u0 r0 {3,D}
5   C u0 r0 {3,S} {7,D}
6   C u0 r0 {2,S}
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
    index = 242,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-2O-R_Ext-5C-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {3,S}
2   O                      u0 r0 {1,S} {6,S}
3   C                      u0 r0 {1,S} {4,D} {5,S}
4   C                      u0 r0 {3,D}
5   C                      u0 r0 {3,S} {7,D}
6   C                      u0 r0 {2,S}
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
    index = 243,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S}
3   C   ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D} {6,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.491012,-0.316397,0.0369631,0.464372,1.0341,0.768872,-0.909654],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (81.3781,'kcal/mol','+|-',4.17612),
        S298 = (-11.2983,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC([CH]O)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 244,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_6R!H->O",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S}
3   C   ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,S}
6   O   ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.42943,-3.56868,-3.55825,-2.65439,-0.655071,0.881996,1.65325],'cal/mol/K','+|-',[9.84163,10.1395,8.6069,6.40405,3.24482,3.78278,7.28165]),
        H298 = (83.3408,'kcal/mol','+|-',8.16543),
        S298 = (-8.86119,'cal/mol/K','+|-',7.78111),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 245,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_6R!H->O_4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S}
3   C ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   C ux {3,D}
5   C ux {3,[S,D,T,B,Q]} {6,S}
6   O ux {5,S}
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
    index = 246,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_6R!H->O_N-4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S}
3   C ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O ux {3,D}
5   C ux {3,[S,D,T,B,Q]} {6,S}
6   O ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.72446,-6.97474,-6.38841,-4.62327,-0.912188,1.61595,3.97225],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.3344,'kcal/mol','+|-',4.17612),
        S298 = (-6.34758,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C([CH]O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 247,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-6R!H->O",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S}
3   C   ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   C   ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.44742,-1.77702,-1.45503,-1.22803,-1.00835,-1.10409,-1.78383],'cal/mol/K','+|-',[4.02406,3.91757,3.10276,2.74018,2.66167,2.86142,4.84437]),
        H298 = (80.2387,'kcal/mol','+|-',7.61817),
        S298 = (-3.50978,'cal/mol/K','+|-',10.9947),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 248,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-6R!H->O_4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S}
3   C ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   C ux {3,D}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux {5,D}
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
    index = 249,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S}
3   C ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   O ux {3,D}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.812444,-0.209411,-0.45594,-0.551477,-0.417125,-0.309742,0.344312],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (76.0276,'kcal/mol','+|-',4.17612),
        S298 = (-8.93012,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 250,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {3,[S,T,Q,B]}
2   O                      ux r0 {1,S}
3   C                      ux {1,[S,T,Q,B]} {4,D} {5,S}
4   R!H                    ux {3,D}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {3,S}
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
    index = 251,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S}
3   C ux {1,[S,T,Q,B]} {4,D}
4   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.27792,-1.36807,-1.54883,-1.59392,-1.6834,-1.78535,-2.1],'cal/mol/K','+|-',[3.30961,2.61422,2.08268,1.77549,1.68131,2.42818,4.59917]),
        H298 = (75.9036,'kcal/mol','+|-',12.575),
        S298 = (-3.9067,'cal/mol/K','+|-',6.86336),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 252,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-2O-R",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S} {5,S}
3   C ux {1,[S,T,Q,B]} {4,D}
4   C ux {3,D}
5   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.675963,-0.623025,-0.936406,-1.21219,-1.73906,-2.37035,-3.59999],'cal/mol/K','+|-',[2.86061,2.6863,2.71673,2.60833,2.462,2.45886,2.40112]),
        H298 = (79.4344,'kcal/mol','+|-',3.50447),
        S298 = (-1.70784,'cal/mol/K','+|-',5.30156),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 253,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-2O-R_Ext-4C-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S} {5,S}
3   C   ux {1,[S,T,Q,B]} {4,D}
4   C   ux {3,D} {6,[S,D,T,B,Q]}
5   C   u0 r0 {2,S}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 254,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-1C-R",
    group = 
"""
1 * C u1 {2,S} {3,S} {5,S}
2   O u0 r0 {1,S}
3   C u0 {1,S} {4,D}
4   C u0 {3,D}
5   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.346581,-0.625581,-1.35644,-1.40402,-1.52642,-1.55914,-1.60845],'cal/mol/K','+|-',[4.215,3.47515,3.16713,3.29256,4.10481,5.05636,6.48535]),
        H298 = (74.2948,'kcal/mol','+|-',15.6731),
        S298 = (-6.59756,'cal/mol/K','+|-',11.4397),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 255,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-1C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S} {5,S}
2   O   u0 r0 {1,S}
3   C   u0 r0 {1,S} {4,D}
4   C   u0 r0 {3,D}
5   C   u0 r0 {1,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.638697,-1.13508,-1.41841,-1.0798,-0.601121,-0.164206,0.393419],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (69.162,'kcal/mol','+|-',4.17612),
        S298 = (-10.4845,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 256,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-4C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S}
2   O   u0 r0 {1,S}
3   C   u0 r0 {1,S} {4,D}
4   C   u0 r0 {3,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 257,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S}
3   C ux {1,[S,T,Q,B]} {4,D}
4   O ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11335,-2.4775,-3.43675,-3.7326,-3.66281,-3.39718,-2.30342],'cal/mol/K','+|-',[3.78604,3.58055,3.85845,4.56385,5.25704,4.73942,3.44265]),
        H298 = (77.3694,'kcal/mol','+|-',6.63765),
        S298 = (-3.46742,'cal/mol/K','+|-',12.6058),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 258,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
2   O ux r0 {1,S}
3   C ux {1,[S,T,Q,B]} {4,D}
4   O ux {3,D}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.994271,-2.52437,-3.5547,-3.77654,-3.51657,-3.15527,-1.97088],'cal/mol/K','+|-',[4.41201,4.19845,4.49905,5.36347,6.14819,5.45739,3.72529]),
        H298 = (76.35,'kcal/mol','+|-',6.85045),
        S298 = (-4.41313,'cal/mol/K','+|-',14.1756),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 259,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
2   O   ux r0 {1,S}
3   C   ux {1,[S,T,Q,B]} {4,D}
4   O   ux {3,D}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16704,-0.428734,-1.50012,-1.4069,-0.936562,-1.02576,-0.820991],'cal/mol/K','+|-',[3.62779,3.01081,4.31888,5.66177,7.04785,6.76992,5.1196]),
        H298 = (80.7041,'kcal/mol','+|-',8.17747),
        S298 = (-11.7697,'cal/mol/K','+|-',9.23246),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 260,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C   u1 {2,S} {3,S} {5,[S,D,T,B,Q]}
2   O   u0 r0 {1,S}
3   C   u0 {1,S} {4,D}
4   O   u0 {3,D}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   u0 {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.80035,-0.803013,-2.49492,-2.85539,-2.82548,-2.82583,-2.06737],'cal/mol/K','+|-',[3.65544,3.38151,3.19707,3.22845,3.22159,3.25028,3.43572]),
        H298 = (79.1012,'kcal/mol','+|-',7.77479),
        S298 = (-9.21091,'cal/mol/K','+|-',3.16324),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 261,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S} {5,[S,D,T,B,Q]}
2   O   u0 r0 {1,S}
3   C   u0 r0 {1,S} {4,D}
4   O   u0 r0 {3,D}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   u0 r0 {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.15206,-1.22648,-2.66122,-3.08531,-3.04304,-3.09141,-2.54226],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (77.3135,'kcal/mol','+|-',4.17612),
        S298 = (-9.1834,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 262,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]} {5,S}
2   O ux r0 {1,S}
3   C ux {1,[S,T,Q,B]} {4,D}
4   O ux {3,D}
5   C u0 r0 {1,S} {6,S} {7,S}
6   O ux {5,S}
7   O u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0996016,0.319824,0.489469,1.49008,2.84128,2.57438,1.67177],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.9101,'kcal/mol','+|-',4.17612),
        S298 = (-16.8873,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 263,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S} {5,S}
2   O u0 r0 {1,S}
3   C u0 r0 {1,S} {4,D}
4   O u0 r0 {3,D}
5   C u0 r0 {1,S} {6,[S,D,T,B,Q]}
6   C u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.19643,-3.42188,-4.43133,-5.01774,-4.96625,-4.41668,-3.13533],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (76.3325,'kcal/mol','+|-',1.69706),
        S298 = (-0.58482,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 264,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {3,S} {5,S}
2   O                      u0 r0 {1,S}
3   C                      u0 r0 {1,S} {4,D}
4   O                      u0 r0 {3,D}
5   C                      u0 r0 {1,S} {6,[S,D,T,B,Q]}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.38568,-4.14162,-5.14357,-5.37893,-5.16289,-4.44927,-2.18631],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (74.2104,'kcal/mol','+|-',1.69706),
        S298 = (0.58645,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 265,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C",
    group = 
"""
1 * C u1 {2,D} {3,[S,T,Q,B]}
2   O ux r0 {1,D}
3   C ux {1,[S,T,Q,B]} {4,D}
4   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.42978,-0.481977,-1.44821,-2.32314,-3.49702,-4.23416,-5.28063],'cal/mol/K','+|-',[2.63993,2.89428,2.76682,2.40244,1.63932,1.47276,2.57529]),
        H298 = (91.4845,'kcal/mol','+|-',6.01416),
        S298 = (2.58881,'cal/mol/K','+|-',2.55507),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 266,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,D} {3,[S,T,Q,B]}
2   O   ux r0 {1,D}
3   C   ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   C   ux {3,D}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.909108,-0.0555224,-1.18086,-2.19687,-3.54552,-4.3907,-5.59307],'cal/mol/K','+|-',[1.7413,2.48719,2.85791,2.67153,1.84041,1.45097,2.4711]),
        H298 = (91.8337,'kcal/mol','+|-',6.69205),
        S298 = (2.76837,'cal/mol/K','+|-',2.77696),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 267,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,D} {3,S}
2   O   u0 r0 {1,D}
3   C   u0 {1,S} {4,D} {5,[S,D,T,B,Q]}
4   C   u0 {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,D}
6   R!H u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.816929,-0.540824,-1.87686,-2.858,-3.85118,-4.42292,-5.16486],'cal/mol/K','+|-',[2.31379,2.47682,2.33215,2.15924,2,2.07155,2.35234]),
        H298 = (89.2849,'kcal/mol','+|-',5.20995),
        S298 = (2.18613,'cal/mol/K','+|-',2.07645),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 268,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   O u0 r0 {1,D}
3   C u0 r0 {1,S} {4,D} {5,[S,D,T,B,Q]}
4   C u0 r0 {3,D}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.22827,-0.0242663,-1.45275,-2.57027,-3.85254,-4.61376,-5.60268],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (90.9198,'kcal/mol','+|-',1.69706),
        S298 = (1.98876,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(=C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 269,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 {2,D} {3,S}
2   O                      u0 r0 {1,D}
3   C                      u0 r0 {1,S} {4,D} {5,[S,D,T,B,Q]}
4   C                      u0 r0 {3,D}
5   C                      ux {3,[S,D,T,B,Q]} {6,D}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,D}
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
    index = 270,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R_5R!H->C",
    group = 
"""
1 * C u1 {2,D} {3,[S,T,Q,B]}
2   O ux r0 {1,D}
3   C ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   C ux {3,D}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.553123,-0.482315,-1.56382,-2.52035,-3.81719,-4.32696,-5.03059],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (94.1641,'kcal/mol','+|-',1.69706),
        S298 = (4.54428,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 271,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 {2,D} {3,[S,T,Q,B]}
2   O ux r0 {1,D}
3   C ux {1,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   C ux {3,D}
5   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.44945,1.34187,0.594114,-0.551143,-2.66254,-4.38997,-7.01196],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (94.601,'kcal/mol','+|-',1.69706),
        S298 = (2.15694,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 272,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,T,Q,B]}
2   O   ux r0 {1,[S,D,T,B,Q]}
3   R!H ux {1,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.777069,-0.0418674,-0.846551,-1.44807,-2.28746,-3.06696,-4.32336],'cal/mol/K','+|-',[3.6717,4.1651,4.14158,3.9637,3.77895,3.21333,1.95629]),
        H298 = (95.0372,'kcal/mol','+|-',7.91937),
        S298 = (1.34194,'cal/mol/K','+|-',12.7664),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 273,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,T,Q,B]}
2   O   ux r0 {1,[S,D,T,B,Q]}
3   C   ux {1,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.93627,3.19709,2.48495,1.82779,0.992816,-0.555012,-3.4287],'cal/mol/K','+|-',[5.16277,7.26853,7.69794,7.55295,7.27449,6.69951,4.09685]),
        H298 = (96.3165,'kcal/mol','+|-',12.7982),
        S298 = (-6.24029,'cal/mol/K','+|-',11.5724),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 274,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Sp-2O-1C",
    group = 
"""
1 * C     u1 {2,S} {3,[S,T,Q,B]}
2   O     ux r0 {1,S}
3   C     ux {1,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   [C,O] ux {3,[S,T,Q,B]}
5   [C,O] ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.79002,3.74786,3.49557,3.02865,2.45891,0.989223,-2.55155],'cal/mol/K','+|-',[7.03291,9.74933,9.52213,8.72646,7.13561,5.40386,3.43068]),
        H298 = (92.9006,'kcal/mol','+|-',5.99299),
        S298 = (-8.17667,'cal/mol/K','+|-',13.2105),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 275,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Sp-2O-1C_Ext-1C-R",
    group = 
"""
1 * C     u1 r0 {2,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
2   O     ux r0 {1,S}
3   C     ux {1,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   [C,O] ux {3,[S,T,Q,B]}
5   [C,O] ux {3,[S,D,T,B,Q]}
6   R!H   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.569048,0.48731,0.320059,0.153086,0.197359,-0.560039,-3.02186],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.2605,'kcal/mol','+|-',4.17612),
        S298 = (-3.64185,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 276,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_N-Sp-2O-1C",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   O u0 r0 {1,D}
3   C u0 r0 {1,S} {4,S} {5,S}
4   O u0 r0 {3,S}
5   O u0 r0 {3,S}
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
    index = 277,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S}
3   R!H ux {1,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.140113,-0.782345,-1.53157,-2.03309,-2.74486,-3.34891,-4.32544],'cal/mol/K','+|-',[2.20252,1.97446,2.20891,2.32436,2.32064,2.23187,1.88791]),
        H298 = (96.3913,'kcal/mol','+|-',5.60102),
        S298 = (3.23971,'cal/mol/K','+|-',13.0599),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 278,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_Ext-1C-R",
    group = 
"""
1 * C u1 {2,S} {3,S} {5,[S,D,T,B,Q]}
2   O u0 r0 {1,S}
3   O u0 {1,S} {4,S}
4   C u0 {3,S}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.277433,-1.46011,-2.68043,-3.29472,-3.85663,-4.29931,-4.58128],'cal/mol/K','+|-',[2.95707,2.9254,2.58557,2.5629,3.01286,3.25406,3.67197]),
        H298 = (98.4371,'kcal/mol','+|-',11.3667),
        S298 = (7.83617,'cal/mol/K','+|-',26.1615),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 279,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_Ext-1C-R_Ext-4R!H-R",
    group = 
"""
1 * C u1 {2,S} {3,S} {5,[S,D,T,B,Q]}
2   O u0 r0 {1,S}
3   O u0 {1,S} {4,S}
4   C u0 {3,S} {6,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
6   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16958,-0.708306,-2.31914,-2.84176,-2.93116,-3.29449,-3.56501],'cal/mol/K','+|-',[3.16306,3.58195,3.75441,3.56505,3.16558,3.44181,4.38538]),
        H298 = (101.604,'kcal/mol','+|-',17.9029),
        S298 = (12.3441,'cal/mol/K','+|-',39.1236),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 280,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H",
    group = 
"""
1 * C u1 r0 {2,S} {3,S} {5,[S,D,T,B,Q]}
2   O u0 r0 {1,S}
3   O u0 r0 {1,S} {4,S}
4   C u0 r0 {3,S} {6,S}
5   C ux {1,[S,D,T,B,Q]}
6   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.14476,-0.1135,-1.60363,-2.25978,-2.88003,-3.77486,-4.63923],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.6289,'kcal/mol','+|-',4.17612),
        S298 = (-1.44294,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCCCO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 281,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_Ext-1C-R_Ext-4R!H-R_N-Sp-6R!H-4R!H",
    group = 
"""
1 * C u1 r0 {2,S} {3,S} {5,[S,D,T,B,Q]}
2   O u0 r0 {1,S}
3   O u0 r0 {1,S} {4,S}
4   C u0 r0 {3,S} {6,[B,D,T,Q]}
5   C ux {1,[S,D,T,B,Q]}
6   C u0 r0 {4,[B,D,T,Q]}
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
    index = 282,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S}
3   C ux {1,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0234442,-0.366425,-0.929549,-1.41598,-2.23109,-2.98033,-4.46167],'cal/mol/K','+|-',[2.55934,2.39493,2.21223,2.09857,1.90056,1.80527,1.70922]),
        H298 = (96.5773,'kcal/mol','+|-',5.19997),
        S298 = (0.903284,'cal/mol/K','+|-',3.8489),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 283,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-2O-R",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S} {5,[S,D,T,B,Q]}
3   C ux {1,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0398085,-0.213236,-0.692153,-1.15994,-2.00776,-2.79449,-4.41764],'cal/mol/K','+|-',[3.34581,3.05305,2.67279,2.46259,2.21295,2.12941,2.12758]),
        H298 = (97.5162,'kcal/mol','+|-',6.91893),
        S298 = (0.879876,'cal/mol/K','+|-',5.15101),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 284,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-2O-R_Ext-4C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S}
2   O   u0 r0 {1,S} {5,[S,D,T,B,Q]}
3   C   u0 r0 {1,S} {4,S}
4   C   u0 r0 {3,S} {6,S}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H u0 r0 {4,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
    index = 285,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-2O-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   C   ux {1,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 286,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S}
3   C ux {1,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.245506,-0.75464,-1.34042,-1.76159,-2.46355,-3.00955,-3.90446],'cal/mol/K','+|-',[3.53781,2.02994,2.19303,2.53894,3.00968,3.05986,2.37669]),
        H298 = (94.814,'kcal/mol','+|-',2.45776),
        S298 = (2.37387,'cal/mol/K','+|-',2.97538),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 287,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-4O-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,T,Q,B]}
2   O   ux r0 {1,S}
3   C   ux {1,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]} {5,S}
5   O   u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.786245,-0.877453,-1.02235,-1.20862,-1.66839,-2.19081,-3.45049],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (94.6267,'kcal/mol','+|-',1.69706),
        S298 = (1.59502,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
COOC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 288,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   O u0 r0 {1,D}
3   C u0 {1,S} {4,S}
4   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.51019,0.412858,-0.608683,-1.47985,-2.70451,-3.59126,-4.80511],'cal/mol/K','+|-',[5.60689,5.08174,4.23167,3.47057,2.61351,2.06856,1.98725]),
        H298 = (89.4876,'kcal/mol','+|-',3.43892),
        S298 = (-0.215579,'cal/mol/K','+|-',4.91787),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 289,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-4R!H-R_Sp-5R!H=4R!H",
    group = 
"""
1 * C   u1 {2,D} {3,S}
2   O   u0 r0 {1,D}
3   C   u0 {1,S} {4,S}
4   C   u0 {3,S} {5,D}
5   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.72422,-0.215739,-1.12588,-1.86918,-2.9213,-3.62389,-4.63335],'cal/mol/K','+|-',[4.57568,3.75759,2.96581,2.56401,2.40999,2.39926,2.39483]),
        H298 = (89.1015,'kcal/mol','+|-',3.16375),
        S298 = (0.655298,'cal/mol/K','+|-',3.11115),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 290,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,D} {3,S}
2   O u0 r0 {1,D}
3   C u0 r0 {1,S} {4,S}
4   C u0 r0 {3,S} {5,D}
5   C ux {4,D}
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
    index = 291,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C",
    group = 
"""
1 * C u1 r0 {2,D} {3,S}
2   O u0 r0 {1,D}
3   C u0 r0 {1,S} {4,S}
4   C u0 r0 {3,S} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.69483,1.24857,-0.239227,-1.40083,-2.76663,-3.52017,-4.56029],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (89.3135,'kcal/mol','+|-',4.17612),
        S298 = (-0.350421,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]CC(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 292,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   O u0 r0 {1,D}
3   C u0 {1,S} {4,S}
4   C u0 {3,S} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.88565,1.5129,0.296419,-0.798528,-2.32512,-3.53417,-5.1057],'cal/mol/K','+|-',[8.40349,8.21563,7.05599,5.91955,4.50023,3.51457,3.16678]),
        H298 = (90.8498,'kcal/mol','+|-',5.9068),
        S298 = (-1.73961,'cal/mol/K','+|-',7.32097),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 293,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,D} {3,S}
2   O   u0 r0 {1,D}
3   C   u0 r0 {1,S} {4,S}
4   C   u0 r0 {3,S} {5,[S,T,Q,B]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,T,Q,B]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.63834,4.19378,2.52652,0.970689,-1.19308,-2.99193,-5.16537],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.8856,'kcal/mol','+|-',4.17612),
        S298 = (-4.07405,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]CC(CC=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 294,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-2O-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,T,Q,B]}
2   O   ux r0 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
3   C   ux {1,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.523703,0.151968,-0.491426,-1.16881,-2.31641,-3.2248,-4.67126],'cal/mol/K','+|-',[2.39746,2.2426,2.13973,2.14853,2.13245,2.0362,1.87865]),
        H298 = (97.5787,'kcal/mol','+|-',3.65429),
        S298 = (2.67683,'cal/mol/K','+|-',2.61081),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 295,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-2O-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,S}
2   O   u0 r0 {1,[S,D,T,B,Q]} {4,S}
3   C   u0 {1,S}
4   C   u0 {2,S} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00464884,-0.283026,-0.864004,-1.54084,-2.65126,-3.49737,-4.78336],'cal/mol/K','+|-',[2.39073,2.39074,2.39119,2.41381,2.50278,2.46989,2.43582]),
        H298 = (96.6058,'kcal/mol','+|-',3.31853),
        S298 = (2.15688,'cal/mol/K','+|-',2.91522),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 296,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-2O-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {3,S}
2   O   u0 r0 {1,[S,D,T,B,Q]} {4,S}
3   C   u0 r0 {1,S}
4   C   u0 r0 {2,S} {5,S} {6,[S,D,T,B,Q]}
5   R!H ux {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0229239,-0.301742,-0.834063,-1.37165,-2.27682,-3.18355,-5.01967],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.2496,'kcal/mol','+|-',4.17612),
        S298 = (2.99965,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 297,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-2O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    group = 
"""
1 * C u1 {2,S} {3,[S,T,Q,B]}
2   O ux r0 {1,S} {4,[S,D,T,B,Q]}
3   C ux {1,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]} {5,[B,D,T,Q]}
5   O u0 r0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.25038,0.76096,0.0301822,-0.647975,-1.84762,-2.84319,-4.51432],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (98.7123,'kcal/mol','+|-',1.69706),
        S298 = (3.40476,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 298,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-2O-R",
    group = 
"""
1 * C u1 {2,S}
2   O ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.570278,-1.47929,-2.08468,-2.41372,-2.83653,-3.10854,-3.66169],'cal/mol/K','+|-',[3.24709,4.99327,5.2463,4.82322,3.64534,2.65196,2.36778]),
        H298 = (103.092,'kcal/mol','+|-',10.4355),
        S298 = (2.29052,'cal/mol/K','+|-',5.55722),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 299,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C u1 {2,S}
2   O ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C u0 {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.33435,-2.90591,-3.49251,-3.57869,-3.53128,-3.37511,-3.34408],'cal/mol/K','+|-',[3.38749,4.30478,4.67723,4.5826,4.03964,3.72346,3.92295]),
        H298 = (109.309,'kcal/mol','+|-',8.55306),
        S298 = (2.06855,'cal/mol/K','+|-',9.33563),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 300,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   O   ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C   u0 r0 {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 301,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-2O-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,[S,D,T,B,Q]}
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
    index = 302,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.06089,-3.28198,-4.02167,-4.38575,-4.55083,-4.7561,-5.25104],'cal/mol/K','+|-',[3.89292,4.5702,5.08504,5.18588,5.00647,4.78123,4.78863]),
        H298 = (88.3285,'kcal/mol','+|-',9.90326),
        S298 = (-1.41438,'cal/mol/K','+|-',9.75172),
    ),
    shortDesc = """Radical correction fitted to 112 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 303,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.04555,-3.88877,-4.21367,-4.22978,-3.92261,-3.82266,-3.9075],'cal/mol/K','+|-',[4.12274,5.58572,6.48948,6.52699,5.86923,5.50513,5.26393]),
        H298 = (92.555,'kcal/mol','+|-',13.7951),
        S298 = (0.552706,'cal/mol/K','+|-',10.8249),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 304,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.14094,-7.27987,-8.0228,-7.9587,-6.9845,-6.25812,-5.2254],'cal/mol/K','+|-',[4.17715,5.56686,6.92717,6.95231,5.33388,4.11058,3.62406]),
        H298 = (94.174,'kcal/mol','+|-',13.5091),
        S298 = (4.16758,'cal/mol/K','+|-',8.3917),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 305,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.90352,-6.266,-6.75251,-6.71633,-6.05892,-5.63819,-5.13005],'cal/mol/K','+|-',[5.43999,5.68709,7.1142,7.29528,5.68533,4.63525,4.66047]),
        H298 = (92.02,'kcal/mol','+|-',9.43),
        S298 = (3.29016,'cal/mol/K','+|-',9.5425),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 306,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_6R!H->O_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]} {7,S}
4   O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   u0 {5,[S,D,T,B,Q]}
7   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.17456,-5.75467,-7.26377,-7.57673,-6.80541,-6.43295,-6.05082],'cal/mol/K','+|-',[5.83252,8.97949,11.3732,11.3759,8.73604,6.80789,6.62267]),
        H298 = (96.9731,'kcal/mol','+|-',5.92127),
        S298 = (4.70761,'cal/mol/K','+|-',14.5616),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 307,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_6R!H->O_Ext-3R!H-R_3R!H-inRing",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]} {7,S}
4   O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   u0 {5,[S,D,T,B,Q]}
7   R!H u0 {3,S}
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
    index = 308,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_6R!H->O_Ext-3R!H-R_N-3R!H-inRing",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C   u0 r0 {2,S} {4,[S,D,T,B,Q]} {7,S}
4   O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   u0 {5,[S,D,T,B,Q]}
7   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.44185,-2.78333,-3.40131,-3.71327,-3.92621,-4.30142,-3.99352],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.1237,'kcal/mol','+|-',4.17612),
        S298 = (-0.317835,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)OC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 309,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C u0 {2,S} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.67514,-9.56109,-10.881,-10.7541,-9.06706,-7.65296,-5.43993],'cal/mol/K','+|-',[3.22346,3.58989,3.68493,3.52725,3.2334,3.17986,3.59317]),
        H298 = (102.85,'kcal/mol','+|-',8.78845),
        S298 = (6.14178,'cal/mol/K','+|-',8.09493),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 310,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_N-6R!H->O_Ext-6BrCClFINPSSi-R_Ext-6BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   u0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
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
    index = 311,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21863,-3.05058,-3.40222,-3.36652,-3.02067,-2.98148,-3.16157],'cal/mol/K','+|-',[3.70036,3.30274,3.52549,4.00299,4.95292,5.63169,6.30154]),
        H298 = (88.3893,'kcal/mol','+|-',14.4177),
        S298 = (-0.330593,'cal/mol/K','+|-',12.4277),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 312,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   O   ux {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21908,-3.14934,-3.52682,-3.41537,-2.86774,-2.74777,-2.88166],'cal/mol/K','+|-',[4.24596,3.76106,4.00388,4.58858,5.64273,6.37673,7.12122]),
        H298 = (88.4666,'kcal/mol','+|-',18.2926),
        S298 = (-0.0295593,'cal/mol/K','+|-',14.2097),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 313,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   O   ux {3,S}
5   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09284,-3.18459,-3.76938,-3.77936,-3.37457,-3.39852,-3.60595],'cal/mol/K','+|-',[4.52005,4.06048,4.03212,4.36332,5.14202,5.45336,6.10438]),
        H298 = (89.3536,'kcal/mol','+|-',18.2503),
        S298 = (-2.12074,'cal/mol/K','+|-',7.18286),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 314,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   O ux {3,S}
5   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.53642,-3.78296,-4.39325,-4.36821,-3.8155,-3.70128,-3.62629],'cal/mol/K','+|-',[4.11501,2.39567,2.0555,3.04885,4.93462,5.69569,6.72499]),
        H298 = (90.8155,'kcal/mol','+|-',15.6505),
        S298 = (-1.92244,'cal/mol/K','+|-',7.81978),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 315,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C_Ext-5C-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {5,S}
4   O   u0 {3,S}
5   C   ux {3,S} {6,[S,D,T,B,Q]}
6   C   u0 r0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
    index = 316,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C_Ext-5C-R_Sp-6R!H-5C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   O ux {3,S}
5   C ux {3,S} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.86713,-3.93289,-4.55932,-4.83319,-4.80008,-4.77028,-4.66281],'cal/mol/K','+|-',[4.47345,2.45293,2.71504,2.9534,2.4437,2.39108,2.41817]),
        H298 = (87.4045,'kcal/mol','+|-',5.31958),
        S298 = (0.162368,'cal/mol/K','+|-',3.30114),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 317,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S} {7,[S,D,T,B,Q]}
4   O   ux {3,S}
5   C   ux {3,S} {6,S}
6   C   ux {5,S}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.957342,-3.65507,-5.20951,-5.70921,-5.05632,-4.74282,-4.84717],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.0085,'kcal/mol','+|-',4.17612),
        S298 = (-0.987524,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 318,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   O ux {3,S}
5   C ux {3,S} {6,[B,D,T,Q]}
6   C ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.915125,-2.90452,-4.21816,-4.61601,-4.40136,-4.59278,-5.10588],'cal/mol/K','+|-',[4.22379,3.18025,3.52707,3.84321,3.57092,3.18095,3.34684]),
        H298 = (95.4246,'kcal/mol','+|-',7.33138),
        S298 = (-1.88354,'cal/mol/K','+|-',3.17584),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 319,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S} {7,[S,D,T,B,Q]}
4   O   ux {3,S}
5   C   ux {3,S} {6,[B,D,T,Q]}
6   C   ux {5,[B,D,T,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0748503,-3.02389,-4.77045,-5.38821,-4.98782,-4.71446,-4.71836],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.8888,'kcal/mol','+|-',4.17612),
        S298 = (-1.98718,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(O)(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 320,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_N-5R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {5,S}
4   O ux {3,S}
5   O ux {3,S}
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
    index = 321,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S} {5,[B,D,T,Q]}
4   O   ux r0 {3,S}
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
    index = 322,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H",
    group = 
"""
1 * O u1 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,D}
4   O u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.39926,-2.05703,-1.95175,-2.12378,-2.49677,-2.88302,-3.8559],'cal/mol/K','+|-',[3.0083,3.4565,4.11654,4.28215,4.62995,5.09272,5.57485]),
        H298 = (96.7478,'kcal/mol','+|-',10.331),
        S298 = (-1.41592,'cal/mol/K','+|-',9.26593),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 323,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,D} {5,[S,D,T,B,Q]}
4   O   u0 {3,D}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.27335,-1.25023,0.0355851,0.649344,1.21297,1.51565,1.40897],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.6972,'kcal/mol','+|-',4.17612),
        S298 = (-10.4913,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C=O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 324,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,D} {5,S}
4   O   u0 {3,D}
5   C   u0 {3,S} {6,S}
6   R!H ux {5,S} {7,S}
7   R!H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.73814,-2.08661,-1.83852,-2.00508,-2.34533,-2.79612,-4.19865],'cal/mol/K','+|-',[4.36585,5.88986,6.06408,5.10504,3.30469,2.51319,2.40962]),
        H298 = (97.0049,'kcal/mol','+|-',3.36206),
        S298 = (-0.556954,'cal/mol/K','+|-',3.6013),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 325,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,D} {5,S}
4   O   u0 r0 {3,D}
5   C   u0 r0 {3,S} {6,S}
6   C   ux {5,S} {7,S}
7   R!H u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.58332,-4.80541,-4.65333,-4.28337,-3.49782,-3.18794,-4.35185],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.7271,'kcal/mol','+|-',4.17612),
        S298 = (0.803483,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CCC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 326,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,D} {5,S}
4   O   u0 r0 {3,D}
5   C   u0 r0 {3,S} {6,S}
6   O   ux {5,S} {7,S}
7   R!H u0 r0 {6,S}
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
    index = 327,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8502,-3.15214,-3.98059,-4.41912,-4.68526,-4.95583,-5.53852],'cal/mol/K','+|-',[3.76255,4.34793,4.8067,4.92736,4.82751,4.57765,4.53661]),
        H298 = (87.2348,'kcal/mol','+|-',7.45832),
        S298 = (-1.83528,'cal/mol/K','+|-',9.39059),
    ),
    shortDesc = """Radical correction fitted to 95 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 328,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21668,-3.8892,-4.9312,-5.41478,-5.5456,-5.68943,-6.88567],'cal/mol/K','+|-',[2.92007,3.62054,4.33538,4.60476,4.37011,4.20874,5.46594]),
        H298 = (85.9521,'kcal/mol','+|-',10.5517),
        S298 = (-0.90054,'cal/mol/K','+|-',8.83477),
    ),
    shortDesc = """Radical correction fitted to 30 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 329,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.16442,-3.57388,-4.47583,-4.91329,-5.07285,-5.24348,-6.55252],'cal/mol/K','+|-',[3.02905,2.90622,3.18913,3.30406,2.96851,2.9391,5.3696]),
        H298 = (86.5376,'kcal/mol','+|-',4.12674),
        S298 = (-1.95691,'cal/mol/K','+|-',6.23635),
    ),
    shortDesc = """Radical correction fitted to 23 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 330,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,D}
4   C ux r1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.420485,-1.05945,-2.02591,-2.65448,-3.50857,-3.69887,-4.14578],'cal/mol/K','+|-',[3.40945,3.06546,3.01115,2.99671,3.31487,3.39054,3.53821]),
        H298 = (88.9749,'kcal/mol','+|-',7.81631),
        S298 = (-7.92977,'cal/mol/K','+|-',2.86547),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 331,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * O u1 r0 {2,S}
2   O ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   C u0 r1 {3,D}
5   C ux r1 {3,[S,D,T,B,Q]} {6,D}
6   O u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.7038,-0.306379,-1.76963,-2.81094,-4.27823,-4.67842,-5.53094],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.4575,'kcal/mol','+|-',4.17612),
        S298 = (-8.22351,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1=COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 332,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C u0 r1 {2,S} {4,D} {5,S}
4   C ux r1 {3,D}
5   C u0 {3,S} {6,[S,T,Q,B]}
6   O ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.221175,-1.43598,-2.15404,-2.57625,-3.12374,-3.20909,-3.45319],'cal/mol/K','+|-',[3.16765,3.47248,3.79561,3.80531,3.88447,3.7284,3.19256]),
        H298 = (90.7335,'kcal/mol','+|-',6.02751),
        S298 = (-7.7829,'cal/mol/K','+|-',3.54553),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 333,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C   u0 r1 {2,S} {4,D} {5,S}
4   C   ux r1 {3,D}
5   C   u0 r1 {3,S} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   O   ux r1 {5,[S,T,Q,B]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.156001,-1.94319,-2.89623,-3.32462,-3.92132,-3.90739,-3.6083],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.3077,'kcal/mol','+|-',4.17612),
        S298 = (-7.21603,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OOC=C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 334,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S}
4   C ux r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.48094,-3.88176,-4.77582,-5.18988,-5.26439,-5.43262,-6.84722],'cal/mol/K','+|-',[2.45889,2.3715,2.79152,3.0284,2.85758,2.82147,5.36172]),
        H298 = (86.3297,'kcal/mol','+|-',3.72557),
        S298 = (-1.22554,'cal/mol/K','+|-',4.80041),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 335,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
7   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.53503,-4.6302,-5.79748,-6.20181,-6.03647,-5.99759,-7.83074],'cal/mol/K','+|-',[3.07567,2.11141,2.04819,2.51004,2.6258,2.59312,6.16542]),
        H298 = (85.5843,'kcal/mol','+|-',3.67649),
        S298 = (-0.312998,'cal/mol/K','+|-',4.83575),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 336,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_6R!H->O",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]}
7   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.81238,-4.65478,-5.85038,-6.4489,-6.27804,-6.36579,-10.3091],'cal/mol/K','+|-',[3.29768,2.8226,2.58257,2.45989,2.30673,2.27512,2.33608]),
        H298 = (85.9716,'kcal/mol','+|-',4.49491),
        S298 = (-1.57779,'cal/mol/K','+|-',6.50476),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 337,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_6R!H->O_Ext-6O-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C   u0 r1 {2,S} {4,S} {5,S}
4   C   ux r1 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   u0 {3,S} {9,[S,D,T,B,Q]}
6   O   ux r1 {4,[S,D,T,B,Q]} {8,S}
7   C   u0 {4,[S,D,T,B,Q]}
8   O   u0 r1 {6,S}
9   R!H ux {5,[S,D,T,B,Q]}
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
    index = 338,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_6R!H->O_Ext-7R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]}
6   O   ux r1 {4,[S,D,T,B,Q]}
7   C   ux {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
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
    index = 339,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_6R!H->O_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   O   ux r1 {4,[S,D,T,B,Q]}
7   C   ux {4,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.71997,-5.59149,-6.71771,-7.18084,-6.64406,-6.43827,-10.3126],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.0436,'kcal/mol','+|-',4.17612),
        S298 = (-0.753015,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)OOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 340,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_N-6R!H->O",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   C   ux {4,[S,D,T,B,Q]}
7   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.33332,-4.61232,-5.75901,-6.02212,-5.86079,-5.7298,-6.02831],'cal/mol/K','+|-',[3.75179,2.50903,2.59624,3.35765,3.62341,3.51026,5.91972]),
        H298 = (85.4133,'kcal/mol','+|-',4.70822),
        S298 = (0.606848,'cal/mol/K','+|-',2.81299),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 341,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_N-6R!H->O_Ext-7R!H-R_Sp-7R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {6,[S,D,T,B,Q]} {7,S}
5   R!H ux {3,[S,D,T,B,Q]}
6   C   ux {4,[S,D,T,B,Q]}
7   C   ux {4,S} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15217,-4.47354,-5.61133,-5.8838,-5.70755,-5.57199,-6.11494],'cal/mol/K','+|-',[4.26307,2.74525,2.84242,3.8301,4.14301,3.99451,7.00961]),
        H298 = (85.8025,'kcal/mol','+|-',3.98186),
        S298 = (0.655537,'cal/mol/K','+|-',3.23724),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 342,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_N-6R!H->O_Ext-7R!H-R_Sp-7R!H-4BrCClFINPSSi_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   u0 r1 {3,S} {6,[S,D,T,B,Q]} {7,S} {9,[S,D,T,B,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]}
6   C   u0 {4,[S,D,T,B,Q]}
7   C   ux r1 {4,S} {8,[S,D,T,B,Q]}
8   R!H ux r1 {7,[S,D,T,B,Q]}
9   R!H ux {4,[S,D,T,B,Q]}
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
    index = 343,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_N-6R!H->O_Ext-7R!H-R_Sp-7R!H-4BrCClFINPSSi_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {6,[S,D,T,B,Q]} {7,S}
5   R!H ux {3,[S,D,T,B,Q]}
6   C   ux {4,[S,D,T,B,Q]}
7   C   ux r1 {4,S} {8,[S,D,T,B,Q]}
8   R!H ux r1 {7,[S,D,T,B,Q]}
9   R!H ux {3,[S,D,T,B,Q]}
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
    index = 344,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_N-6R!H->O_Ext-7R!H-R_N-Sp-7R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C   u0 r1 {2,S} {4,S} {5,S}
4   C   ux r1 {3,S} {6,[S,D,T,B,Q]} {7,D}
5   C   u0 r1 {3,S}
6   C   ux {4,[S,D,T,B,Q]}
7   C   u0 r1 {4,D} {8,S}
8   R!H u0 r1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.14849,-5.23683,-6.42353,-6.64454,-6.55037,-6.43994,-5.63849],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.2783,'kcal/mol','+|-',4.17612),
        S298 = (0.38775,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=C(C)C(O[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 345,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {5,S}
4   C   u0 r1 {3,S}
5   C   u0 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39373,-3.05349,-4.28152,-5.04961,-5.1641,-5.52529,-7.91278],'cal/mol/K','+|-',[3.67205,3.1816,3.32911,3.56144,3.52691,3.65484,8.00469]),
        H298 = (88.6719,'kcal/mol','+|-',6.21085),
        S298 = (-3.9669,'cal/mol/K','+|-',7.08312),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 346,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {5,S}
4   C   u0 r1 {3,S}
5   C   u0 r0 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.733818,-2.92971,-4.64945,-5.62882,-5.71626,-6.17316,-10.5127],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.9923,'kcal/mol','+|-',4.17612),
        S298 = (-6.20774,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(OO)C1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 347,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S}
4   C   ux r1 {3,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.81269,-3.30216,-4.42632,-5.10073,-5.51581,-6.13912,-5.75275],'cal/mol/K','+|-',[2.94914,3.15216,3.63571,4.16813,4.56486,4.99485,3.24538]),
        H298 = (89.0312,'kcal/mol','+|-',8.97944),
        S298 = (-1.34893,'cal/mol/K','+|-',7.29332),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 348,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   u0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
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
    index = 349,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Sp-5R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07013,-3.90098,-5.55615,-6.71675,-7.26191,-8.29849,-6.74624],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (93.3604,'kcal/mol','+|-',4.17612),
        S298 = (1.60836,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1CCOC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 350,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-Sp-5R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S}
4   C   ux r1 {3,S} {5,D}
5   C   ux r1 {4,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.36071,-3.7433,-4.68635,-5.14006,-5.76354,-6.09543,-5.73157],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.3299,'kcal/mol','+|-',4.17612),
        S298 = (-5.07975,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC(O[O])C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 351,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S}
4   C ux r1 {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59557,-3.26369,-3.74939,-4.01401,-4.32787,-4.56897,-5.2427],'cal/mol/K','+|-',[2.49149,2.92794,3.21199,3.08736,2.91213,2.80757,4.36759]),
        H298 = (86.0563,'kcal/mol','+|-',2.37445),
        S298 = (-1.14205,'cal/mol/K','+|-',3.39887),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 352,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S}
4   C ux r1 {3,S} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.76123,-3.85244,-4.42735,-4.54191,-4.68758,-4.97157,-5.59302],'cal/mol/K','+|-',[3.00286,2.62443,2.75198,3.10858,3.27818,3.03216,5.26239]),
        H298 = (85.9277,'kcal/mol','+|-',3.09542),
        S298 = (-0.263894,'cal/mol/K','+|-',1.94703),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 353,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi_Ext-5C-R_Sp-6R!H-5C",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.03594,-3.97919,-4.45405,-4.49906,-4.56154,-4.85025,-5.68499],'cal/mol/K','+|-',[3.05729,2.91602,3.17097,3.60634,3.74635,3.44318,6.21087]),
        H298 = (85.7972,'kcal/mol','+|-',3.13529),
        S298 = (-0.221331,'cal/mol/K','+|-',2.14441),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 354,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {8,S}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   R!H ux {5,S} {7,S}
7   R!H ux {6,S}
8   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.35999,-4.10668,-4.38004,-4.33821,-4.37806,-4.70793,-5.87913],'cal/mol/K','+|-',[3.1992,3.54597,3.99323,4.53367,4.70449,4.31914,8.23178]),
        H298 = (85.8875,'kcal/mol','+|-',3.32039),
        S298 = (-0.26331,'cal/mol/K','+|-',2.43396),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 355,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Ext-3R!H-R_6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {8,S}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {6,S}
6   C   ux r1 {5,S} {7,S}
7   R!H ux r1 {6,S}
8   C   u0 r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.93044,-3.57754,-3.73381,-3.55993,-3.55945,-3.98116,-4.28772],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (85.9944,'kcal/mol','+|-',1.69706),
        S298 = (-0.355863,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 356,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Ext-3R!H-R_N-6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {8,S}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {6,S}
6   O   ux r1 {5,S} {7,S}
7   R!H ux r1 {6,S}
8   C   u0 r1 {3,S}
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
    index = 357,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi_Ext-5C-R_N-Sp-6R!H-5C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S} {6,[B,D,T,Q]}
6   R!H u0 r1 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.52502,-3.28205,-4.30718,-4.73472,-5.25473,-5.51751,-5.17916],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.9791,'kcal/mol','+|-',4.17612),
        S298 = (-0.455423,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 358,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_N-Sp-5C-4BrCClFINPSSi",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S}
4   C ux r1 {3,S} {5,D}
5   C ux r1 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.23111,-1.96843,-2.25789,-2.85264,-3.53651,-3.68324,-4.47202],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (86.2487,'kcal/mol','+|-',1.69706),
        S298 = (-3.07399,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1C=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 359,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S}
4   C ux r1 {3,S} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.85511,-4.49669,-5.04716,-5.3607,-5.06625,-5.05116,-9.16973],'cal/mol/K','+|-',[3.22691,3.48855,3.85186,4.25803,4.64823,4.62614,3.80578]),
        H298 = (86.8657,'kcal/mol','+|-',5.90593),
        S298 = (-2.96761,'cal/mol/K','+|-',6.71703),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 360,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S}
5   O   ux r1 {4,S} {8,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]} {7,S}
7   R!H u0 {6,S}
8   R!H ux {5,[S,D,T,B,Q]}
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
    index = 361,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.42196,-5.12797,-6.72019,-7.38492,-7.40287,-7.44136,-8.1945],'cal/mol/K','+|-',[3.1328,5.43859,6.61597,7.06075,7.06347,6.72452,5.70911]),
        H298 = (82.76,'kcal/mol','+|-',25.2312),
        S298 = (3.24948,'cal/mol/K','+|-',12.8225),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 362,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.89762,-3.9501,-5.37428,-5.90694,-5.70241,-5.7315,-7.10786],'cal/mol/K','+|-',[2.94286,4.44775,5.7769,6.00985,4.88563,4.02242,5.28534]),
        H298 = (89.9078,'kcal/mol','+|-',7.73575),
        S298 = (0.0546784,'cal/mol/K','+|-',8.21977),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 363,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C   u0 r1 {3,[S,D,T,B,Q]} {5,D}
5   R!H u0 r1 {4,D} {6,S}
6   O   ux r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.05849,-5.90901,-7.45418,-7.95697,-7.36838,-6.82481,-6.53097],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (94.4462,'kcal/mol','+|-',4.17612),
        S298 = (4.50291,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 364,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6074,-3.46037,-4.8543,-5.39443,-5.28592,-5.45818,-7.25208],'cal/mol/K','+|-',[2.99464,4.43258,6.07894,6.38906,5.18331,4.38721,6.02979]),
        H298 = (88.7732,'kcal/mol','+|-',6.65562),
        S298 = (-1.05738,'cal/mol/K','+|-',7.53492),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 365,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 r0 {1,[S,D,T,B,Q]} {3,S}
3   C   u0 r0 {2,S} {4,S} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S}
5   R!H ux r1 {4,S} {6,[S,D,T,B,Q]}
6   O   u0 r1 {5,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13718,-2.18589,-3.4826,-4.05922,-4.23817,-4.65926,-8.75586],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.3469,'kcal/mol','+|-',4.17612),
        S298 = (-1.85283,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(C=O)C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 366,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C ux r1 {4,S} {6,[S,D,T,B,Q]}
6   O ux r1 {5,[S,D,T,B,Q]}
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
    index = 367,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S}
5   O ux {4,S} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.42582,-4.73269,-6.26891,-6.72181,-6.21839,-6.08635,-7.30841],'cal/mol/K','+|-',[3.19637,5.29549,8.59233,9.44823,7.84742,6.79676,9.19526]),
        H298 = (89.4812,'kcal/mol','+|-',8.11038),
        S298 = (-0.837014,'cal/mol/K','+|-',12.7241),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 368,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-6O-R_Ext-7R!H-R_7R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S} {7,[S,D,T,B,Q]}
5   O ux r1 {4,S} {6,[S,D,T,B,Q]}
6   O ux r1 {5,[S,D,T,B,Q]}
7   C u0 r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59043,-3.23094,-3.44428,-3.57401,-3.67914,-3.95927,-4.25569],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.516,'kcal/mol','+|-',4.17612),
        S298 = (-5.19451,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 369,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-6O-R_Ext-7R!H-R_N-7R!H->C",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   O                      ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C                      ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C                      ux r1 {3,[S,D,T,B,Q]} {5,S} {7,[S,D,T,B,Q]}
5   O                      ux r1 {4,S} {6,[S,D,T,B,Q]}
6   O                      ux r1 {5,[S,D,T,B,Q]}
7   [Cl,O,Si,S,N,P,F,I,Br] u0 r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26121,-6.23445,-9.09354,-9.8696,-8.75763,-8.21344,-10.3611],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.4465,'kcal/mol','+|-',4.17612),
        S298 = (3.52048,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 370,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * O u1 {2,S}
2   O ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C u0 r1 {3,[S,D,T,B,Q]} {5,[S,D]}
5   C u0 {4,[S,D]} {6,[S,D]}
6   C ux {5,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.73281,-8.07266,-10.085,-11.0799,-11.654,-11.716,-10.9111],'cal/mol/K','+|-',[3.72247,3.17481,3.34514,3.25566,3.21363,3.28645,3.16636]),
        H298 = (64.8907,'kcal/mol','+|-',5.9068),
        S298 = (11.2365,'cal/mol/K','+|-',3.25955),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 371,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-6R!H->O_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   u0 r1 {3,[S,D,T,B,Q]} {5,[S,D]}
5   C   u0 r1 {4,[S,D]} {6,[S,D]}
6   C   ux r1 {5,[S,D]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.03847,-8.17229,-10.4706,-11.3536,-11.8563,-12.0324,-10.8543],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (64.8547,'kcal/mol','+|-',4.17612),
        S298 = (10.9571,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O[O])C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 372,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.69216,-2.83429,-3.57064,-3.98974,-4.31423,-4.63947,-4.95756],'cal/mol/K','+|-',[4.08503,4.53427,4.82679,4.87352,4.88569,4.64535,3.56255]),
        H298 = (87.7249,'kcal/mol','+|-',5.80135),
        S298 = (-2.23839,'cal/mol/K','+|-',9.59404),
    ),
    shortDesc = """Radical correction fitted to 65 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 373,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57445,-2.80193,-3.60069,-4.05078,-4.41104,-4.7824,-5.14468],'cal/mol/K','+|-',[4.08354,4.6357,4.9651,5.02189,5.03734,4.74115,3.44765]),
        H298 = (87.9329,'kcal/mol','+|-',5.99365),
        S298 = (-2.47498,'cal/mol/K','+|-',8.80878),
    ),
    shortDesc = """Radical correction fitted to 61 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 374,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.20865,-2.56038,-3.43766,-3.93283,-4.3885,-4.74992,-5.16761],'cal/mol/K','+|-',[3.70825,3.5959,3.72495,4.15806,4.95612,5.11773,4.06411]),
        H298 = (88.1314,'kcal/mol','+|-',6.931),
        S298 = (-3.10361,'cal/mol/K','+|-',8.61862),
    ),
    shortDesc = """Radical correction fitted to 34 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 375,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]}
6   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.74704,-2.43651,-3.54244,-4.10542,-4.46777,-4.96116,-5.99547],'cal/mol/K','+|-',[4.46538,4.14981,3.86221,3.84505,3.74075,3.63703,3.06213]),
        H298 = (87.2823,'kcal/mol','+|-',4.92652),
        S298 = (-5.1529,'cal/mol/K','+|-',7.18088),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 376,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   u0 r0 {3,S}
5   C   u0 {3,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H u0 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   O   ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.839555,-2.92362,-4.17929,-4.91203,-5.34235,-6.11835,-6.89989],'cal/mol/K','+|-',[6.82262,5.71183,4.88175,4.36459,3.43221,3.13074,2.35084]),
        H298 = (85.9948,'kcal/mol','+|-',5.13267),
        S298 = (-3.95169,'cal/mol/K','+|-',8.48584),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 377,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_7R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   O ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C u0 r0 {3,S}
5   C u0 {3,[S,D,T,B,Q]}
6   C ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C u0 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   O ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0495,-2.59799,-3.5836,-4.23958,-4.72262,-5.41968,-6.71703],'cal/mol/K','+|-',[10.9954,8.96688,7.25031,6.21097,4.56819,3.80452,3.16679]),
        H298 = (87.1023,'kcal/mol','+|-',6.23826),
        S298 = (-3.77629,'cal/mol/K','+|-',14.3641),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 378,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_7R!H->C_Sp-7C-6R!H",
    group = 
"""
1 * O u1 r0 {2,S}
2   O ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C u0 r0 {3,S}
5   C u0 r0 {3,[S,D,T,B,Q]}
6   C ux {3,[S,D,T,B,Q]} {7,S}
7   C u0 r0 {6,S} {8,[S,D,T,B,Q]}
8   O ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.67372,0.368593,-1.2769,-2.3496,-3.55705,-4.67182,-6.77675],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.3921,'kcal/mol','+|-',4.17612),
        S298 = (-8.73017,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(COO)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 379,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_7R!H->C_N-Sp-7C-6R!H",
    group = 
"""
1 * O u1 r0 {2,S}
2   O ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C u0 r0 {3,S}
5   C u0 r0 {3,[S,D,T,B,Q]}
6   C ux {3,[S,D,T,B,Q]} {7,D}
7   C u0 r0 {6,D} {8,[S,D,T,B,Q]}
8   O ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.77272,-5.56457,-5.8903,-6.12956,-5.88818,-6.16754,-6.6573],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.8126,'kcal/mol','+|-',4.17612),
        S298 = (1.1776,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 380,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_N-7R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   O ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C u0 r0 {3,S}
5   C u0 {3,[S,D,T,B,Q]}
6   C ux {3,[S,D,T,B,Q]} {7,S}
7   O u0 {6,S} {8,S}
8   O ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62961,-3.24924,-4.77498,-5.58449,-5.96208,-6.81701,-7.08275],'cal/mol/K','+|-',[4.80006,4.55779,4.27198,4.04198,3.65059,3.4814,3.319]),
        H298 = (84.8872,'kcal/mol','+|-',6.15875),
        S298 = (-4.12708,'cal/mol/K','+|-',3.76942),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 381,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_N-7R!H->C_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   u0 r0 {3,S}
5   C   u0 r0 {3,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]} {7,S} {9,[S,D,T,B,Q]}
7   O   u0 r0 {6,S} {8,S}
8   O   ux {7,S}
9   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.90635,-4.40971,-5.79047,-6.47455,-6.60694,-7.33181,-7.43908],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.2697,'kcal/mol','+|-',4.17612),
        S298 = (-4.85239,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
COOC(C)(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 382,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * O u1 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {5,S} {6,S}
4   C u0 r0 {3,S}
5   C u0 {3,S}
6   C u0 {3,S} {7,[S,D,T,B,Q]}
7   O u0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.069422,-1.06774,-1.88194,-2.14642,-2.28161,-2.7697,-4.1733],'cal/mol/K','+|-',[3.44695,3.21334,2.85619,2.73931,2.86992,2.68951,2.96773]),
        H298 = (87.647,'kcal/mol','+|-',6.67627),
        S298 = (-8.68267,'cal/mol/K','+|-',2.70451),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 383,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_7R!H->O_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {5,S} {6,S}
4   C   u0 r0 {3,S} {8,[S,D,T,B,Q]}
5   C   u0 {3,S}
6   C   u0 {3,S} {7,[S,D,T,B,Q]}
7   O   u0 {6,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.250049,-1.3633,-2.02738,-2.29873,-2.62385,-2.97436,-4.58846],'cal/mol/K','+|-',[4.43244,3.90145,3.53195,3.33431,3.21378,3.18251,3.18509]),
        H298 = (88.9544,'kcal/mol','+|-',6.04156),
        S298 = (-8.45105,'cal/mol/K','+|-',3.16351),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 384,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_7R!H->O_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,S} {6,S}
4   C   u0 r0 {3,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
5   C   u0 r0 {3,S}
6   C   u0 r0 {3,S} {7,[S,D,T,B,Q]}
7   O   u0 r0 {6,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
9   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34815,-2.17117,-2.58355,-2.6725,-2.82646,-3.10102,-4.45391],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.5043,'kcal/mol','+|-',4.17612),
        S298 = (-8.41985,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 385,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]}
6   C ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3013,-3.15579,-4.35382,-4.98894,-5.48781,-5.6097,-6.61177],'cal/mol/K','+|-',[3.89758,3.71765,3.36382,3.06109,2.80331,2.71522,2.86123]),
        H298 = (88.6344,'kcal/mol','+|-',6.43226),
        S298 = (-3.22474,'cal/mol/K','+|-',4.46559),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 386,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H",
    group = 
"""
1 * O u1 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {5,S} {6,S}
4   C u0 r0 {3,S}
5   C u0 {3,S}
6   C u0 {3,S} {7,S}
7   C u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.997151,-2.89454,-4.21372,-4.95929,-5.56874,-5.709,-6.30183],'cal/mol/K','+|-',[4.98284,4.76136,4.33892,3.92252,3.49665,3.34287,3.27634]),
        H298 = (87.4388,'kcal/mol','+|-',6.06761),
        S298 = (-4.26409,'cal/mol/K','+|-',3.25937),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 387,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,S} {6,S}
4   C   u0 r0 {3,S} {8,[S,D,T,B,Q]}
5   C   u0 r0 {3,S}
6   C   u0 r0 {3,S} {7,S}
7   C   u0 r0 {6,S}
8   R!H ux {4,[S,D,T,B,Q]}
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
    index = 388,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-6R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C ux r0 {3,S}
5   C ux {3,[S,D,T,B,Q]}
6   C ux {3,[S,D,T,B,Q]} {7,[D,T]}
7   C ux {6,[D,T]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.90961,-3.67829,-4.634,-5.04824,-5.32596,-5.41109,-7.23165],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.0256,'kcal/mol','+|-',4.17612),
        S298 = (-1.14603,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#CC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 389,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C ux r0 {3,S}
5   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.952853,-2.47806,-3.6041,-4.26067,-4.93284,-5.37863,-5.48436],'cal/mol/K','+|-',[3.38346,3.67191,4.14392,4.84422,6.04906,6.12756,4.4316]),
        H298 = (89.0225,'kcal/mol','+|-',6.75351),
        S298 = (-1.94562,'cal/mol/K','+|-',10.1651),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 390,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S}
5   C   ux {3,S} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32098,-2.69221,-3.53032,-3.76816,-3.93005,-4.23419,-4.3688],'cal/mol/K','+|-',[4.23972,3.72548,3.33762,3.30602,3.43961,3.408,2.52957]),
        H298 = (90.1538,'kcal/mol','+|-',8.11633),
        S298 = (-3.05909,'cal/mol/K','+|-',7.18589),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 391,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,S}
4   C   u0 r0 {3,S}
5   C   u0 r0 {3,S} {6,D}
6   R!H ux {5,D} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.43644,-4.03565,-4.54616,-3.85967,-2.39381,-1.93795,-2.5536],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (100.588,'kcal/mol','+|-',4.17612),
        S298 = (-3.29675,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 392,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C ux r0 {3,S}
5   C ux {3,S} {6,D}
6   C ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0315041,-1.67673,-2.83323,-3.28038,-3.78178,-4.36553,-4.61935],'cal/mol/K','+|-',[2.7278,3.20168,3.51348,3.78126,3.9352,3.95456,2.99072]),
        H298 = (91.4381,'kcal/mol','+|-',4.54195),
        S298 = (-4.79047,'cal/mol/K','+|-',3.71966),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 393,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S} {7,[S,D,T,B,Q]}
5   C   ux {3,S} {6,D}
6   C   ux {5,D}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.21734,-1.76427,-3.07831,-3.63683,-4.2606,-4.87079,-4.95493],'cal/mol/K','+|-',[2.94397,3.62353,3.81108,3.91695,3.76837,3.70276,2.93077]),
        H298 = (91.0879,'kcal/mol','+|-',4.80332),
        S298 = (-4.40991,'cal/mol/K','+|-',3.77524),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 394,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S} {7,[S,D,T,B,Q]}
5   C   ux {3,S} {6,D}
6   C   ux {5,D}
7   O   u0 r0 {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
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
    index = 395,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S} {7,D}
5   C   ux {3,S} {6,D} {8,[S,D,T,B,Q]}
6   C   ux {5,D}
7   O   ux {4,D}
8   R!H ux {5,[S,D,T,B,Q]}
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
    index = 396,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   ux {3,S} {6,D}
6   C   ux {5,D}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.93279,-0.729276,-1.9487,-2.47686,-3.15728,-3.82244,-4.28883],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.2223,'kcal/mol','+|-',4.17612),
        S298 = (-5.54418,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 397,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {5,S}
4   C u0 r0 {3,S}
5   C u0 {3,S} {6,D}
6   O u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.57587,-3.52199,-4.07912,-4.28979,-4.43617,-4.59853,-4.49378],'cal/mol/K','+|-',[5.30725,4.58638,4.04536,4.03816,3.97672,3.36788,2.63003]),
        H298 = (88.0613,'kcal/mol','+|-',4.09079),
        S298 = (-1.0825,'cal/mol/K','+|-',10.5481),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 398,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,S}
4   C   u0 r0 {3,S} {7,[S,D,T,B,Q]}
5   C   u0 r0 {3,S} {6,D}
6   O   u0 r0 {5,D}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.23124,-4.79689,-5.05134,-5.21246,-5.3271,-5.26502,-4.92667],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (88.2092,'kcal/mol','+|-',1.69706),
        S298 = (2.26846,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 399,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-5R!H-R_7R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S} {5,S}
4   C u0 r0 {3,S}
5   C u0 r0 {3,S} {6,D} {7,S}
6   O u0 r0 {5,D}
7   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0588543,-0.949183,-1.71706,-1.88755,-2.07451,-2.7407,-3.40755],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.8761,'kcal/mol','+|-',4.17612),
        S298 = (-7.27735,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(O[O])C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 400,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-5R!H-R_N-7R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   O                      u0 r0 {1,S} {3,S}
3   C                      u0 r0 {2,S} {4,S} {5,S}
4   C                      u0 r0 {3,S}
5   C                      u0 r0 {3,S} {6,D} {7,S}
6   O                      u0 r0 {5,D}
7   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.954462,-2.90754,-4.01064,-4.38535,-4.57051,-4.79012,-4.49779],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (89.3511,'kcal/mol','+|-',4.17612),
        S298 = (-3.26506,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 401,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S}
5   C   ux {3,S} {6,[S,T,Q,B]}
6   R!H ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.601454,-2.27364,-3.67452,-4.73079,-5.89005,-6.47105,-6.54922],'cal/mol/K','+|-',[2.72108,4.07136,5.24682,6.25622,7.72472,7.69762,5.15306]),
        H298 = (88.2571,'kcal/mol','+|-',6.21468),
        S298 = (-0.882772,'cal/mol/K','+|-',12.7133),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 402,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S}
5   C   ux {3,S} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C   ux {5,[S,T,Q,B]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.316345,-0.26261,-1.00211,-1.5363,-1.91361,-2.61716,-4.13153],'cal/mol/K','+|-',[4.3304,5.11136,5.62405,6.10116,6.29015,5.89158,3.83053]),
        H298 = (85.0612,'kcal/mol','+|-',5.22332),
        S298 = (-8.90372,'cal/mol/K','+|-',7.76275),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 403,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S}
5   C   ux {3,S} {6,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   u0 r0 {5,S}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
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
    index = 404,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S} {8,[S,D,T,B,Q]}
5   C   ux {3,S} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C   ux {5,[S,T,Q,B]}
7   C   ux {5,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
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
    index = 405,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S}
5   C   ux {3,S} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.783653,-2.94005,-4.68839,-6.08568,-7.71306,-8.27177,-7.6141],'cal/mol/K','+|-',[2.12171,2.99551,4.17393,5.07312,6.39886,6.67822,5.06637]),
        H298 = (88.699,'kcal/mol','+|-',6.42159),
        S298 = (2.60209,'cal/mol/K','+|-',7.58471),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 406,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H_Ext-6R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S}
5   C   ux {3,S} {6,S}
6   R!H ux {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.625897,-2.87698,-4.74428,-6.25952,-8.0949,-8.67377,-7.87065],'cal/mol/K','+|-',[2.09278,3.34562,4.72603,5.66123,6.84546,7.13819,5.51042]),
        H298 = (88.9957,'kcal/mol','+|-',6.04575),
        S298 = (3.14263,'cal/mol/K','+|-',7.88011),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 407,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H_Ext-6R!H-R_Ext-7R!H-R_8R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S}
5   C   ux {3,S} {6,S}
6   R!H ux {5,S} {7,S}
7   R!H u0 {6,S} {8,S}
8   C   ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.693848,-2.00513,-3.29653,-4.4703,-5.94472,-6.41417,-6.14132],'cal/mol/K','+|-',[2.89007,2.91008,2.5094,2.40819,3.3516,3.26031,2.51656]),
        H298 = (86.724,'kcal/mol','+|-',4.09269),
        S298 = (0.790969,'cal/mol/K','+|-',5.46751),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 408,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_6R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S}
5   C   ux {3,S} {6,S}
6   C   ux {5,S} {7,S}
7   R!H u0 r0 {6,S} {8,S}
8   C   ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.365698,-1.66984,-3.1423,-4.52923,-6.41934,-6.86208,-6.30024],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (86.9865,'kcal/mol','+|-',1.69706),
        S298 = (1.7844,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(CC(C)O[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 409,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_N-6R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S}
5   C   ux {3,S} {6,S}
6   O   ux {5,S} {7,S}
7   R!H u0 r0 {6,S} {8,S}
8   C   ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.51422,-2.84335,-3.68212,-4.32297,-4.75817,-5.29439,-5.74402],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.1341,'kcal/mol','+|-',4.17612),
        S298 = (-1.69262,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 410,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H_Ext-6R!H-R_Ext-7R!H-R_N-8R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,S}
4   C   u0 r0 {3,S}
5   C   u0 r0 {3,S} {6,S}
6   R!H u0 r0 {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,S}
8   O   u0 r0 {7,S}
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
    index = 411,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-Sp-6R!H-5R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,S}
4   C   ux r0 {3,S}
5   C   ux {3,S} {6,T}
6   R!H ux {5,T}
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
    index = 412,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H",
    group = 
"""
1 * O u1 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {5,D}
4   C u0 r0 {3,S}
5   C u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.39873,-2.91431,-2.8934,-2.90053,-2.91836,-2.91114,-3.39245],'cal/mol/K','+|-',[3.66015,3.82977,3.35863,2.74467,1.93763,1.9065,2.71285]),
        H298 = (86.2612,'kcal/mol','+|-',9.42433),
        S298 = (-3.6217,'cal/mol/K','+|-',3.41369),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 413,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {5,D}
4   C   u0 r0 {3,S}
5   C   u0 {3,D} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.34387,-3.23273,-3.32769,-3.36745,-3.29147,-3.09213,-3.16038],'cal/mol/K','+|-',[4.77545,5.11776,4.49272,3.5719,2.50673,2.71535,3.9375]),
        H298 = (84.3324,'kcal/mol','+|-',10.199),
        S298 = (-4.31078,'cal/mol/K','+|-',2.891),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 414,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {5,D}
4   C   u0 r0 {3,S}
5   C   u0 {3,D} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.69419,-4.61826,-4.46863,-4.13392,-3.4398,-2.702,-1.85699],'cal/mol/K','+|-',[4.48351,5.26361,4.88663,4.0509,3.16432,3.62344,3.76632]),
        H298 = (88.146,'kcal/mol','+|-',6.94084),
        S298 = (-4.4025,'cal/mol/K','+|-',4.03338),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 415,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,D}
4   C   u0 r0 {3,S} {7,[S,D,T,B,Q]}
5   C   u0 r0 {3,D} {6,S}
6   R!H ux {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 416,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * O u1 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {5,D}
4   C u0 r0 {3,S}
5   C u0 {3,D} {6,[B,D,T,Q]}
6   O ux {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.993548,-1.84721,-2.18674,-2.60098,-3.14314,-3.48227,-4.46377],'cal/mol/K','+|-',[4.91314,5.01537,4.56577,4.17924,3.67236,3.39922,3.18517]),
        H298 = (80.5189,'kcal/mol','+|-',6.97374),
        S298 = (-4.21905,'cal/mol/K','+|-',3.69742),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 417,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,D}
4   C   u0 r0 {3,S} {7,[S,D,T,B,Q]}
5   C   u0 r0 {3,D} {6,[B,D,T,Q]}
6   O   ux {5,[B,D,T,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 418,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {5,D}
4   C   u0 r0 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   u0 r0 {3,D}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.6347,-3.56367,-3.77831,-3.59448,-3.13229,-2.84489,-3.53562],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.0726,'kcal/mol','+|-',4.17612),
        S298 = (-1.17861,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(O)C(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 419,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-4BrCClFINPSSi-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S} {5,D}
4   C u0 r0 {3,S} {6,[S,D,T,B,Q]}
5   C u0 r0 {3,D}
6   C u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.312182,-0.684407,-1.35859,-1.90908,-2.66373,-3.12245,-4.2408],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.2165,'kcal/mol','+|-',4.17612),
        S298 = (-5.60203,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 420,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-4BrCClFINPSSi-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   O                      u0 r0 {1,S} {3,S}
3   C                      u0 r0 {2,S} {4,S} {5,D}
4   C                      u0 r0 {3,S} {6,[S,D,T,B,Q]}
5   C                      u0 r0 {3,D}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,[S,D,T,B,Q]}
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
    index = 421,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D}
5   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.75028,-2.72606,-3.38861,-3.79821,-4.10323,-4.57149,-4.9639],'cal/mol/K','+|-',[4.81725,5.66248,5.86181,5.54134,4.80994,4.1208,2.76619]),
        H298 = (87.9417,'kcal/mol','+|-',5.60879),
        S298 = (-2.5577,'cal/mol/K','+|-',8.53678),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 422,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D}
5   C   ux {4,D} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05648,-2.28097,-2.59827,-2.96542,-3.34023,-3.91448,-4.7271],'cal/mol/K','+|-',[4.7052,6.75893,7.16914,6.76241,5.56879,4.69406,3.20313]),
        H298 = (87.2737,'kcal/mol','+|-',5.66302),
        S298 = (-4.16128,'cal/mol/K','+|-',6.92999),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 423,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D}
5   C ux {4,D} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26195,-2.20687,-2.45709,-2.84744,-3.32608,-3.93967,-4.76709],'cal/mol/K','+|-',[4.6494,7.43483,7.97697,7.56944,6.27599,5.31598,3.62412]),
        H298 = (86.6905,'kcal/mol','+|-',5.18065),
        S298 = (-4.07969,'cal/mol/K','+|-',7.20506),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 424,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O u1 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {7,S}
5   C u0 {4,D} {6,S}
6   C u0 {5,S}
7   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.94972,-1.53371,-1.77036,-2.22941,-2.86659,-3.63966,-4.86622],'cal/mol/K','+|-',[5.8045,9.45409,10.2363,9.74215,8.09079,6.86308,4.32968]),
        H298 = (86.4246,'kcal/mol','+|-',6.39565),
        S298 = (-5.41117,'cal/mol/K','+|-',6.94897),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 425,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-6C-R_8R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {7,S}
5   C u0 {4,D} {6,S}
6   C u0 {5,S} {8,[S,D,T,B,Q]}
7   C u0 {4,S}
8   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.96771,-6.18719,-6.55567,-6.59934,-6.2301,-6.18401,-6.13207],'cal/mol/K','+|-',[3.16252,3.20049,3.27356,3.26056,3.21024,3.18375,3.17674]),
        H298 = (89.7026,'kcal/mol','+|-',6.50158),
        S298 = (-2.5111,'cal/mol/K','+|-',4.05591),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 426,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-6C-R_8R!H->C_Sp-8C-6C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {7,S}
5   C u0 r0 {4,D} {6,S}
6   C u0 r0 {5,S} {8,S}
7   C u0 r0 {4,S}
8   C ux {6,S}
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
    index = 427,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-6C-R_8R!H->C_N-Sp-8C-6C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {7,S}
5   C u0 r0 {4,D} {6,S}
6   C u0 r0 {5,S} {8,D}
7   C u0 r0 {4,S}
8   C ux {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.95386,-6.36153,-6.85489,-6.88024,-6.42557,-6.31452,-6.23911],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.6638,'kcal/mol','+|-',4.17612),
        S298 = (-1.61316,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 428,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-6C-R_N-8R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {7,S}
5   C u0 {4,D} {6,S}
6   C u0 {5,S} {8,S}
7   C u0 {4,S}
8   O ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.225152,1.12542,0.964111,0.267687,-0.944584,-2.18574,-4.14288],'cal/mol/K','+|-',[2.42727,6.64452,8.60434,9.00964,8.43706,8.05117,5.65097]),
        H298 = (85.4954,'kcal/mol','+|-',5.63256),
        S298 = (-7.06836,'cal/mol/K','+|-',6.82124),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 429,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-6C-R_N-8R!H->C_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,D} {7,S}
5   C   u0 r0 {4,D} {6,S} {9,[S,D,T,B,Q]}
6   C   u0 r0 {5,S} {8,S}
7   C   u0 r0 {4,S}
8   O   ux {6,S}
9   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0124585,-2.00586,-3.21066,-4.11977,-5.03133,-6.06883,-6.72911],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.3315,'kcal/mol','+|-',4.17612),
        S298 = (-3.84159,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(CO[O])=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 430,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D}
5   C   ux {4,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
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
    index = 431,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-7R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,D}
5   C   u0 r0 {4,D} {6,S}
6   C   u0 r0 {5,S} {7,[S,D,T,B,Q]}
7   O   u0 r0 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.34933,-3.13688,-3.47632,-3.80652,-4.04169,-4.47067,-5.02338],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.6536,'kcal/mol','+|-',4.17612),
        S298 = (0.307825,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 432,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D}
5   C ux {4,D} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18324,-2.59586,-3.19829,-3.46684,-3.40036,-3.80742,-4.55714],'cal/mol/K','+|-',[7.17504,5.97498,5.13619,4.51309,3.82859,3.32517,3.16266]),
        H298 = (90.7891,'kcal/mol','+|-',5.93165),
        S298 = (-4.50802,'cal/mol/K','+|-',8.98024),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 433,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_N-6R!H->C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {7,[S,D,T,B,Q]}
5   C   ux {4,D} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09385,-0.803503,-1.76735,-2.32843,-2.63729,-3.44397,-4.57444],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.9841,'kcal/mol','+|-',4.17612),
        S298 = (-7.47965,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 434,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.238655,-2.17353,-3.31364,-3.89613,-4.34361,-4.9965,-5.33345],'cal/mol/K','+|-',[4.8831,4.17779,3.4002,2.89903,2.61913,2.49011,2.32726]),
        H298 = (86.4376,'kcal/mol','+|-',4.10296),
        S298 = (-2.00366,'cal/mol/K','+|-',4.98827),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 435,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   C u0 r0 {4,D}
6   C ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O u0 r0 {6,[S,D,T,B,Q]}
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
    index = 436,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   C ux {4,D}
6   C ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.75698,-2.64491,-3.7075,-4.24788,-4.58571,-5.11243,-5.30046],'cal/mol/K','+|-',[4.64535,3.87103,3.10341,2.57429,2.5787,2.67973,2.56336]),
        H298 = (86.555,'kcal/mol','+|-',4.47753),
        S298 = (-1.14442,'cal/mol/K','+|-',2.96442),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 437,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   C ux {4,D}
6   C ux {4,[S,D,T,B,Q]} {7,S}
7   C ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.315668,-2.29696,-3.51478,-4.25622,-4.88706,-5.49645,-5.49861],'cal/mol/K','+|-',[4.82137,4.05193,3.39379,2.91561,2.4721,2.30408,2.71675]),
        H298 = (86.1153,'kcal/mol','+|-',4.51814),
        S298 = (-1.23864,'cal/mol/K','+|-',3.33871),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 438,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H_Ext-7BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {6,S}
5   C   ux {4,D}
6   C   u0 {4,S} {7,S}
7   C   ux {6,S} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.49633,-0.857007,-2.42511,-3.44949,-4.43155,-5.30203,-4.95953],'cal/mol/K','+|-',[3.49299,3.32772,3.24473,3.17619,3.16432,3.21056,3.52392]),
        H298 = (85.8783,'kcal/mol','+|-',6.49503),
        S298 = (-1.69231,'cal/mol/K','+|-',5.01051),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 439,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H_Ext-7BrCClFINPSSi-R_Ext-7BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {6,S}
5   C   ux {4,D}
6   C   u0 r0 {4,S} {7,S}
7   C   ux {6,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
9   R!H ux {7,[S,D,T,B,Q]}
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
    index = 440,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H_Ext-6R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   C   ux {4,D}
6   C   ux {4,[S,D,T,B,Q]} {7,S} {8,[S,D,T,B,Q]}
7   C   ux {6,S}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.1097,-3.71174,-4.66229,-5.07454,-5.33065,-5.64931,-6.13411],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (86.0531,'kcal/mol','+|-',4.17612),
        S298 = (-0.711795,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(CO[O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 441,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-6R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D} {6,S}
5   C ux {4,D}
6   C u0 r0 {4,S} {7,D}
7   C ux {6,D}
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
    index = 442,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.65098,-3.95507,-4.73452,-5.05309,-5.11389,-5.24049,-5.0053],'cal/mol/K','+|-',[5.17491,5.79743,5.94388,5.79775,5.72917,5.17546,3.76169]),
        H298 = (89.773,'kcal/mol','+|-',7.01297),
        S298 = (-0.478744,'cal/mol/K','+|-',12.8954),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 443,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_6R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux r0 {3,S} {5,D} {6,S}
5   O ux {4,D}
6   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.930749,-1.66099,-2.34309,-2.70927,-2.83823,-3.3076,-3.79038],'cal/mol/K','+|-',[5.64966,4.46096,4.1314,4.02432,4.19621,4.57889,4.17575]),
        H298 = (87.2724,'kcal/mol','+|-',8.88506),
        S298 = (-6.01841,'cal/mol/K','+|-',6.99786),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 444,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_6R!H->C_Ext-6C-R_Ext-6C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,D} {6,S}
5   O   ux {4,D}
6   C   u0 r0 {4,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.767801,-1.27356,-2.74772,-3.43995,-4.00668,-4.86265,-5.39473],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.4062,'kcal/mol','+|-',4.17612),
        S298 = (-5.46197,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 445,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {6,S}
5   O u0 r0 {4,D}
6   C u0 r0 {4,S} {7,S}
7   C u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.256932,-0.0670303,-0.566724,-0.936203,-0.945791,-1.20294,-2.11522],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.1536,'kcal/mol','+|-',4.17612),
        S298 = (-9.51278,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC(=O)CC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 446,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {6,S}
5   O u0 r0 {4,D}
6   C u0 r0 {4,S} {7,[B,D,T,Q]}
7   C u0 r0 {6,[B,D,T,Q]}
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
    index = 447,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_N-6R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   O u0 {4,D}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.12547,-5.92142,-6.78432,-7.06207,-7.06445,-6.89726,-6.04666],'cal/mol/K','+|-',[2.42514,3.21094,3.61725,3.45128,3.48147,3.01905,2.40222]),
        H298 = (90.8362,'kcal/mol','+|-',5.53495),
        S298 = (4.26954,'cal/mol/K','+|-',5.49738),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 448,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_N-6R!H->C_Ext-6BrClFINOPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   O   u0 r0 {4,D}
6   O   ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.91906,-4.83864,-5.41313,-5.80474,-5.78607,-5.9659,-5.92675],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.0718,'kcal/mol','+|-',4.17612),
        S298 = (1.76919,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 449,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.6333,-3.94266,-4.74055,-5.1035,-5.20921,-5.39742,-5.46872],'cal/mol/K','+|-',[3.90206,6.2004,7.45771,7.42411,6.67094,5.45164,3.01249]),
        H298 = (87.2575,'kcal/mol','+|-',4.69451),
        S298 = (0.229779,'cal/mol/K','+|-',9.75375),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 450,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.56869,-3.95459,-4.80574,-5.18542,-5.29212,-5.45696,-5.37668],'cal/mol/K','+|-',[4.15186,6.64599,7.98318,7.93926,7.12763,5.82708,3.15298]),
        H298 = (87.0381,'kcal/mol','+|-',4.42023),
        S298 = (0.350187,'cal/mol/K','+|-',10.4263),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 451,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_5R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,T,Q,B]}
5   C   ux {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.2571,-4.92448,-5.7754,-6.0132,-5.90233,-5.78967,-5.29922],'cal/mol/K','+|-',[3.05419,5.7015,7.90197,8.3974,7.96266,6.79472,3.71438]),
        H298 = (87.0234,'kcal/mol','+|-',4.93296),
        S298 = (1.65092,'cal/mol/K','+|-',10.6114),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 452,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_5R!H->C_Ext-6R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,T,Q,B]}
5   C   ux {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.19204,-4.93341,-5.85021,-6.08684,-5.96308,-5.80354,-5.22449],'cal/mol/K','+|-',[3.41298,6.50371,9.0218,9.59239,9.09636,7.76194,4.1786]),
        H298 = (87.0294,'kcal/mol','+|-',5.30808),
        S298 = (2.00802,'cal/mol/K','+|-',11.9103),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 453,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_5R!H->C_Ext-6R!H-R_Ext-7R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,T,Q,B]}
5   C   ux {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,S}
7   R!H ux {6,S} {8,[S,D,T,B,Q]}
8   O   u0 {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.82325,-2.86552,-2.90357,-2.98101,-3.08304,-3.48412,-4.32457],'cal/mol/K','+|-',[4.93381,2.72421,2.53056,3.40923,4.36774,5.34636,4.87349]),
        H298 = (85.3692,'kcal/mol','+|-',3.29362),
        S298 = (-1.88815,'cal/mol/K','+|-',3.50677),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 454,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_5R!H->C_Ext-6R!H-R_Ext-7R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,T,Q,B]} {9,[S,D,T,B,Q]}
5   C   ux {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,S}
7   R!H ux {6,S} {8,[S,D,T,B,Q]}
8   O   u0 r0 {7,[S,D,T,B,Q]}
9   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.69522,-3.12948,-2.73581,-2.48993,-2.34451,-2.51797,-3.46656],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (85.271,'kcal/mol','+|-',1.69706),
        S298 = (-1.36979,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 455,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_N-5R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,T,Q,B]}
5   O   ux {4,[S,T,Q,B]} {6,S}
6   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.159277,-0.559984,-1.41193,-2.28821,-3.15638,-4.29249,-5.64781],'cal/mol/K','+|-',[5.09988,6.77957,6.21937,5.09927,3.58282,3.16354,3.26312]),
        H298 = (87.1422,'kcal/mol','+|-',6.05853),
        S298 = (-4.20239,'cal/mol/K','+|-',4.36874),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 456,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_N-5R!H->C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
5   O   ux {4,[S,T,Q,B]} {6,S}
6   R!H ux {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 457,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrCClFINPSSi-3R!H",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,D}
4   C ux r0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.91968,-3.17173,-3.25735,-3.35321,-3.30459,-3.1489,-3.00618],'cal/mol/K','+|-',[4.14169,4.19447,3.92261,3.52996,2.87578,2.52075,2.9535]),
        H298 = (86.1897,'kcal/mol','+|-',3.89026),
        S298 = (0.228914,'cal/mol/K','+|-',17.4502),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 458,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,D}
4   C   ux r0 {3,D} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.32326,-3.81236,-3.909,-3.96014,-3.69512,-3.27645,-2.68371],'cal/mol/K','+|-',[5.27154,4.8912,4.42449,3.90277,3.40091,3.2558,3.64974]),
        H298 = (85.4042,'kcal/mol','+|-',4.67832),
        S298 = (2.55748,'cal/mol/K','+|-',21.4356),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 459,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   ux r0 {1,S} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,D}
4   C   u0 r0 {3,D} {5,[S,D,T,B,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99065,-3.01802,-3.42886,-3.84114,-4.05393,-4.12847,-4.77732],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.8515,'kcal/mol','+|-',4.17612),
        S298 = (-4.1146,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 460,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,D}
4   C   ux r0 {3,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
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

entry(
    index = 461,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.381313,-1.36694,-2.03883,-2.40851,-2.81562,-3.15953,-3.9472],'cal/mol/K','+|-',[3.9633,4.55014,4.52414,4.08282,3.21555,2.89584,2.86455]),
        H298 = (96.6525,'kcal/mol','+|-',19.7013),
        S298 = (0.722061,'cal/mol/K','+|-',10.7419),
    ),
    shortDesc = """Radical correction fitted to 182 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 462,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.644548,-1.68321,-2.31589,-2.67223,-3.02605,-3.3047,-3.98379],'cal/mol/K','+|-',[3.15054,2.94302,2.93583,2.86924,2.6544,2.67674,2.91776]),
        H298 = (95.3559,'kcal/mol','+|-',17.3327),
        S298 = (2.16293,'cal/mol/K','+|-',12.7868),
    ),
    shortDesc = """Radical correction fitted to 69 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 463,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R",
    group = 
"""
1 * C u1 {2,D} {3,[S,D,T,B,Q]}
2   C ux r0 {1,D}
3   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.676944,-1.43817,-1.95264,-2.35979,-2.99653,-3.46772,-4.17975],'cal/mol/K','+|-',[3.06895,2.57297,2.14789,1.91535,1.69703,1.65776,1.70115]),
        H298 = (103.117,'kcal/mol','+|-',15.3677),
        S298 = (3.82917,'cal/mol/K','+|-',8.61313),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 464,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,D} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,D}
3   C   ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.527593,-1.3543,-1.93012,-2.35865,-2.99852,-3.45003,-4.08845],'cal/mol/K','+|-',[3.31374,2.80792,2.36628,2.11814,1.8819,1.83675,1.82848]),
        H298 = (101.772,'kcal/mol','+|-',15.7572),
        S298 = (4.08554,'cal/mol/K','+|-',9.45694),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 465,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C u1 {2,D} {3,[S,D,T,B,Q]}
2   C ux r0 {1,D}
3   C ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.595834,-1.47299,-2.07218,-2.50718,-3.15321,-3.60633,-4.20407],'cal/mol/K','+|-',[3.39105,2.7463,2.15253,1.80254,1.36601,1.14351,1.09812]),
        H298 = (100.903,'kcal/mol','+|-',14.9686),
        S298 = (3.29355,'cal/mol/K','+|-',3.5514),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 466,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_Sp-4C-3R!H",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   C u0 r0 {1,D}
3   C ux {1,S} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.373579,-1.0041,-1.60754,-2.10825,-2.83191,-3.49765,-4.47913],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (107.743,'kcal/mol','+|-',1.69706),
        S298 = (1.90556,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=[C]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 467,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H",
    group = 
"""
1 * C u1 {2,D} {3,[S,D,T,B,Q]}
2   C ux r0 {1,D}
3   C ux {1,[S,D,T,B,Q]} {4,[D,T]}
4   C ux {3,[D,T]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.627585,-1.53997,-2.13856,-2.56417,-3.19911,-3.62186,-4.16478],'cal/mol/K','+|-',[3.65435,2.93391,2.28415,1.90935,1.44032,1.22178,1.15126]),
        H298 = (99.9261,'kcal/mol','+|-',15.0242),
        S298 = (3.49183,'cal/mol/K','+|-',3.63632),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 468,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R",
    group = 
"""
1 * C   u1 {2,D} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,D}
3   C   ux {1,[S,D,T,B,Q]} {4,[D,T]}
4   C   ux {3,[D,T]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.27667,-2.03072,-2.46006,-2.78296,-3.26766,-3.59859,-4.05993],'cal/mol/K','+|-',[1.84854,1.73352,1.71772,1.69946,1.64922,1.58072,1.44953]),
        H298 = (98.9488,'kcal/mol','+|-',19.6734),
        S298 = (3.12916,'cal/mol/K','+|-',2.40748),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 469,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R_Ext-2CN-R",
    group = 
"""
1 * C u1 {2,D} {3,[S,D,T,B,Q]}
2   C ux r0 {1,D} {6,[S,D,T,B,Q]}
3   C u0 {1,[S,D,T,B,Q]} {4,[D,T]}
4   C u0 {3,[D,T]} {5,D}
5   O ux {4,D}
6   C u0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3214,-1.86692,-2.2362,-2.54695,-3.03541,-3.40001,-3.96433],'cal/mol/K','+|-',[2.83231,2.50764,2.38491,2.27565,2.12156,2.04774,2.00244]),
        H298 = (95.059,'kcal/mol','+|-',29.4173),
        S298 = (3.07395,'cal/mol/K','+|-',3.1418),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 470,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R_Ext-2CN-R_Sp-6R!H-2CN",
    group = 
"""
1 * C u1 r0 {2,D} {3,[S,D,T,B,Q]}
2   C ux r0 {1,D} {6,S}
3   C u0 r0 {1,[S,D,T,B,Q]} {4,[D,T]}
4   C u0 r0 {3,[D,T]} {5,D}
5   O ux {4,D}
6   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.03045,-2.40174,-2.69552,-2.93077,-3.28567,-3.55542,-3.99929],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (105.425,'kcal/mol','+|-',1.69706),
        S298 = (2.21729,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 471,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R_Ext-2CN-R_N-Sp-6R!H-2CN",
    group = 
"""
1 * C u1 r0 {2,D} {3,[S,D,T,B,Q]}
2   C ux r0 {1,D} {6,[B,D,T,Q]}
3   C u0 r0 {1,[S,D,T,B,Q]} {4,[D,T]}
4   C u0 r0 {3,[D,T]} {5,D}
5   O ux {4,D}
6   C u0 r0 {2,[B,D,T,Q]}
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
    index = 472,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R_5R!H->C",
    group = 
"""
1 * C u1 {2,D} {3,[S,D,T,B,Q]}
2   C ux r0 {1,D}
3   C ux {1,[S,D,T,B,Q]} {4,[D,T]}
4   C ux {3,[D,T]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
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
    index = 473,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * C u1 {2,D} {3,[S,D,T,B,Q]}
2   C ux r0 {1,D}
3   C ux {1,[S,D,T,B,Q]} {4,[D,T]}
4   C ux {3,[D,T]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.07489,-2.00159,-2.47119,-2.74632,-3.18455,-3.50738,-4.0198],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (105.358,'kcal/mol','+|-',1.69706),
        S298 = (2.35762,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 474,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-2CN-R_Sp-5R!H-2CN",
    group = 
"""
1 * C   u1 {2,D} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,D} {5,S}
3   C   ux {1,[S,D,T,B,Q]} {4,[D,T]}
4   C   ux {3,[D,T]}
5   R!H ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.34236,0.0565619,-1.03697,-1.77979,-2.85772,-3.56864,-4.39818],'cal/mol/K','+|-',[5.29249,3.93418,3.29676,2.95634,2.39896,2.10064,2.04234]),
        H298 = (103.778,'kcal/mol','+|-',2.47322),
        S298 = (5.2363,'cal/mol/K','+|-',4.69301),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 475,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-2CN-R_Sp-5R!H-2CN_Sp-4C=3R!H",
    group = 
"""
1 * C   u1 {2,D} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,D} {5,S}
3   C   ux {1,[S,D,T,B,Q]} {4,D}
4   C   ux {3,D}
5   R!H ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.390073,-1.14124,-1.96356,-2.54953,-3.3261,-3.79576,-4.25191],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.99,'kcal/mol','+|-',1.69706),
        S298 = (3.73529,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 476,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-2CN-R_Sp-5R!H-2CN_N-Sp-4C=3R!H",
    group = 
"""
1 * C   u1 {2,D} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,D} {5,S}
3   C   ux {1,[S,D,T,B,Q]} {4,T}
4   C   ux {3,T}
5   R!H ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.07478,1.25436,-0.110376,-1.01005,-2.38934,-3.34152,-4.54445],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (103.567,'kcal/mol','+|-',1.69706),
        S298 = (6.73731,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#C[C]=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 477,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-2CN-R_N-Sp-5R!H-2CN",
    group = 
"""
1 * C   u1 r0 {2,D} {3,S}
2   C   u0 r0 {1,D} {5,[B,D,T,Q]}
3   C   u0 r0 {1,S} {4,[D,T]}
4   C   u0 r0 {3,[D,T]}
5   R!H u0 r0 {2,[B,D,T,Q]}
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
    index = 478,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   C u0 r0 {1,D}
3   C ux {1,S} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.137645,-0.676078,-1.11835,-1.50996,-2.11457,-2.55687,-3.42778],'cal/mol/K','+|-',[4.97079,4.89701,4.86084,4.84475,5.0773,5.47309,5.90881]),
        H298 = (107.74,'kcal/mol','+|-',31.1517),
        S298 = (8.61123,'cal/mol/K','+|-',30.5571),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 479,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 {2,D} {3,S}
2   C   u0 r0 {1,D}
3   C   ux {1,S} {4,S}
4   O   ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
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
    index = 480,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-2CN-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 {2,D} {3,[S,D,T,B,Q]}
2   C ux r0 {1,D} {4,[S,D,T,B,Q]}
3   C ux {1,[S,D,T,B,Q]}
4   C ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]}
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
    index = 481,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-2CN-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 {2,D} {3,[S,D,T,B,Q]}
2   C                      ux r0 {1,D} {4,[S,D,T,B,Q]}
3   C                      ux {1,[S,D,T,B,Q]}
4   C                      ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,[S,D,T,B,Q]}
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
    index = 482,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R",
    group = 
"""
1 * R   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.632934,-1.77105,-2.44611,-2.78424,-3.03663,-3.24627,-3.91353],'cal/mol/K','+|-',[3.25809,3.11613,3.19085,3.16844,2.97948,3.00544,3.28623]),
        H298 = (91.483,'kcal/mol','+|-',12.5396),
        S298 = (1.56561,'cal/mol/K','+|-',13.8872),
    ),
    shortDesc = """Radical correction fitted to 57 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 483,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.29212,-2.58477,-3.24079,-3.54848,-3.7439,-3.88822,-4.66719],'cal/mol/K','+|-',[2.60653,2.65626,2.81281,2.89,3.13031,3.52491,4.31129]),
        H298 = (91.1493,'kcal/mol','+|-',12.3091),
        S298 = (4.36093,'cal/mol/K','+|-',16.8459),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 484,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.16481,-2.45853,-3.16244,-3.48279,-3.66262,-3.7963,-4.62574],'cal/mol/K','+|-',[2.65474,2.71196,2.95142,3.04651,3.29077,3.70546,4.57976]),
        H298 = (90.0858,'kcal/mol','+|-',12.1062),
        S298 = (4.02982,'cal/mol/K','+|-',17.8054),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 485,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.923944,-2.22957,-2.99123,-3.3616,-3.50485,-3.63403,-4.57589],'cal/mol/K','+|-',[2.97064,3.12139,3.31789,3.38951,3.73713,4.36427,5.55433]),
        H298 = (91.2263,'kcal/mol','+|-',13.2089),
        S298 = (4.43986,'cal/mol/K','+|-',21.3255),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 486,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.881158,-1.97946,-2.62417,-3.10635,-3.70426,-4.06354,-4.66916],'cal/mol/K','+|-',[4.84799,4.45902,4.15268,3.97492,3.567,3.21696,2.86413]),
        H298 = (88.4447,'kcal/mol','+|-',14.8102),
        S298 = (10.5649,'cal/mol/K','+|-',20.6965),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 487,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {5,S}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   C   u0 r0 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.85292,-3.88079,-4.28874,-4.6054,-5.03847,-5.29051,-5.63041],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (93.1981,'kcal/mol','+|-',1.69706),
        S298 = (9.30128,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(C)(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 488,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_Ext-5R!H-R_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.79407,-0.746857,-2.34822,-3.24767,-3.66704,-3.48603,-3.32486],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.4773,'kcal/mol','+|-',4.17612),
        S298 = (28.1922,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 489,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.842325,-2.43884,-3.46636,-3.92656,-3.96595,-4.16029,-5.77115],'cal/mol/K','+|-',[2.1372,3.08169,3.54546,3.40139,3.14724,2.78724,2.23974]),
        H298 = (95.6685,'kcal/mol','+|-',7.10897),
        S298 = (2.59667,'cal/mol/K','+|-',7.36534),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 490,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_5R!H->O",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   O   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.728223,-2.08926,-3.01197,-3.49029,-3.59382,-3.91672,-5.82237],'cal/mol/K','+|-',[2.25185,2.7087,2.8538,2.73094,2.69332,2.73202,2.45741]),
        H298 = (96.1249,'kcal/mol','+|-',6.89472),
        S298 = (2.32275,'cal/mol/K','+|-',8.17346),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 491,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_5R!H->O_Ext-6O-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {5,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   O   u0 {2,[S,D,T,B,Q]} {6,S}
6   O   u0 {5,S} {7,S}
7   C   u0 {6,S}
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
    index = 492,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_5R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_9R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {5,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   O   u0 r0 {2,[S,D,T,B,Q]} {6,S}
6   O   u0 r0 {5,S} {7,S}
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
    index = 493,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_5R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_N-9R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {5,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   O   u0 r0 {2,[S,D,T,B,Q]} {6,S}
6   O   u0 r0 {5,S} {7,S}
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
    index = 494,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_5R!H->O_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   O   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
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
    index = 495,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_N-5R!H->O",
    group = 
"""
1 * C   u1 r0 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {5,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   C   u0 r0 {2,[S,D,T,B,Q]} {6,S}
6   O   u0 r0 {5,S}
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
    index = 496,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]} {6,S}
6   C   ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71118,-2.36994,-2.10521,-1.22089,0.688686,2.36378,3.7529],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.0278,'kcal/mol','+|-',4.17612),
        S298 = (-20.3293,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C](CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 497,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Sp-5R!H=2CCNN",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,D}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.59632,-2.77572,-3.29527,-3.44531,-3.67707,-3.82519,-4.40689],'cal/mol/K','+|-',[2.72089,2.35503,2.87193,2.97827,2.77706,2.47198,2.31703]),
        H298 = (86.3066,'kcal/mol','+|-',6.14565),
        S298 = (1.86589,'cal/mol/K','+|-',7.57029),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 498,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Sp-5R!H=2CCNN_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,D}
3   C   ux {1,[S,D,T,B,Q]} {6,S}
4   C   ux {1,[S,D,T,B,Q]}
5   C   ux {2,D}
6   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.804637,-2.40846,-3.3749,-3.68582,-4.01214,-4.16137,-4.91043],'cal/mol/K','+|-',[3.87645,3.37872,3.23557,3.19922,3.16613,3.16248,3.16295]),
        H298 = (85.8053,'kcal/mol','+|-',7.19952),
        S298 = (-0.177331,'cal/mol/K','+|-',3.33496),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 499,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Sp-5R!H=2CCNN_Ext-3R!H-R_6R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux r0 {1,S} {5,D}
3   C ux {1,[S,D,T,B,Q]} {6,S}
4   C ux {1,[S,D,T,B,Q]}
5   C ux {2,D}
6   C u0 r0 {3,S}
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
    index = 500,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Sp-5R!H=2CCNN_Ext-3R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C                      ux r0 {1,S} {5,D}
3   C                      ux {1,[S,D,T,B,Q]} {6,S}
4   C                      ux {1,[S,D,T,B,Q]}
5   C                      ux {2,D}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0119455,-1.98778,-3.1328,-3.51443,-3.95697,-4.14879,-4.88732],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.261,'kcal/mol','+|-',4.17612),
        S298 = (0.197161,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 501,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Sp-5R!H=2CCNN_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,D} {6,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {2,D}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53525,-3.8496,-4.99513,-5.15087,-5.07383,-4.83022,-4.90089],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.5444,'kcal/mol','+|-',4.17612),
        S298 = (8.2318,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(O)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 502,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_N-Sp-5R!H=2CCNN",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,S}
3   R!H ux {1,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.04319,-3.80503,-4.74333,-5.32488,-5.71309,-5.82809,-6.50246],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.7474,'kcal/mol','+|-',4.17612),
        S298 = (10.3959,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 503,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   C   ux {1,[S,D,T,B,Q]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.293527,-1.21918,-1.79249,-2.02607,-2.24729,-2.48544,-3.12706],'cal/mol/K','+|-',[3.64413,3.20196,3.12104,3.03146,2.70579,2.58523,2.19898]),
        H298 = (87.3148,'kcal/mol','+|-',7.84295),
        S298 = (-0.509068,'cal/mol/K','+|-',12.8427),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 504,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r0 {1,S}
3   C ux {1,[S,D,T,B,Q]} {4,D}
4   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.011228,-1.29267,-2.04427,-2.34382,-2.53827,-2.69206,-3.15279],'cal/mol/K','+|-',[3.61381,3.26526,3.00759,2.71159,2.27412,2.29767,2.14248]),
        H298 = (85.8245,'kcal/mol','+|-',6.76524),
        S298 = (-0.0736636,'cal/mol/K','+|-',13.8663),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 505,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   C   ux {1,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   C   ux {3,D}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.30389,-2.44329,-2.82317,-2.77056,-2.53612,-2.58893,-3.16947],'cal/mol/K','+|-',[2.92865,4.08271,4.19461,3.56929,2.52863,2.27997,2.15224]),
        H298 = (87.4342,'kcal/mol','+|-',11.2194),
        S298 = (-2.09271,'cal/mol/K','+|-',4.97327),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 506,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_Ext-4C-R",
    group = 
"""
1 * C u1 {2,S} {3,S}
2   C u0 r0 {1,S}
3   C u0 {1,S} {4,D} {5,[S,D,T,B,Q]}
4   C u0 {3,D} {6,S}
5   O ux {3,[S,D,T,B,Q]}
6   O u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.45431,-4.9482,-5.41906,-4.84815,-3.40929,-2.67155,-2.79206],'cal/mol/K','+|-',[4.10563,4.90039,5.0097,4.80755,4.56993,4.55938,3.92396]),
        H298 = (95.6168,'kcal/mol','+|-',14.2962),
        S298 = (-0.22413,'cal/mol/K','+|-',7.37901),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 507,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-2CN-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S}
2   C   u0 r0 {1,S} {7,[S,D,T,B,Q]}
3   C   u0 r0 {1,S} {4,D} {5,[S,D,T,B,Q]}
4   C   u0 {3,D} {6,S}
5   O   ux {3,[S,D,T,B,Q]}
6   O   u0 r0 {4,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.52855,-3.62468,-4.04533,-3.56789,-2.24287,-1.51031,-1.97066],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.0138,'kcal/mol','+|-',4.17612),
        S298 = (-2.58129,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 508,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r0 {1,S}
3   C ux {1,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   C ux {3,D}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13542,-1.65519,-1.94772,-1.99574,-2.06761,-2.38643,-3.11095],'cal/mol/K','+|-',[2.72759,2.11311,2.1517,2.12607,2.1872,2.22779,2.19935]),
        H298 = (86.0253,'kcal/mol','+|-',3.01779),
        S298 = (-2.25848,'cal/mol/K','+|-',3.65302),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 509,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->C_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {6,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   C   ux {3,D}
5   C   ux {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09574,-1.67887,-1.98951,-2.00352,-1.95187,-2.23879,-3.23986],'cal/mol/K','+|-',[3.35203,2.39339,2.44608,2.41929,2.39939,2.39189,2.39049]),
        H298 = (85.9488,'kcal/mol','+|-',3.15573),
        S298 = (-1.9051,'cal/mol/K','+|-',4.10133),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 510,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->C_Ext-2CN-R_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   C   ux {3,D}
5   C   ux {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
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
    index = 511,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r0 {1,S}
3   C ux {1,[S,D,T,B,Q]} {4,D} {5,[S,D,T,B,Q]}
4   C ux {3,D}
5   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.238798,-0.979956,-1.5709,-2.10208,-2.89805,-3.33492,-4.18766],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.4179,'kcal/mol','+|-',4.17612),
        S298 = (-5.08394,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([CH]C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 512,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,D}
4   C   ux {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.807431,-0.593944,-1.58737,-2.06876,-2.49322,-2.71186,-3.06158],'cal/mol/K','+|-',[3.66388,2.6294,2.38288,2.4293,2.40644,2.61029,2.45084]),
        H298 = (85.0849,'kcal/mol','+|-',5.2037),
        S298 = (0.893567,'cal/mol/K','+|-',17.8959),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 513,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_Ext-2CN-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S}
2   C   u0 r0 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   u0 r0 {1,S} {4,D}
4   C   u0 r0 {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 514,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_Ext-4C-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,D}
4   C   ux {3,D} {6,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.851452,-0.855741,-1.85708,-2.39766,-2.71805,-2.72663,-2.01819],'cal/mol/K','+|-',[3.32407,3.24804,4.37414,4.8374,4.63501,4.61428,3.19224]),
        H298 = (84.2357,'kcal/mol','+|-',6.14011),
        S298 = (7.08855,'cal/mol/K','+|-',23.3563),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 515,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_Ext-4C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,D}
4   C   ux {3,D} {6,S}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {4,S} {7,[S,D,T,B,Q]}
7   R!H u0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.483137,-1.3073,-2.45943,-3.06187,-3.44118,-3.52617,-2.46347],'cal/mol/K','+|-',[3.93824,3.5878,5.12104,5.73404,5.20417,4.88952,3.50555]),
        H298 = (83.1971,'kcal/mol','+|-',6.15516),
        S298 = (0.691117,'cal/mol/K','+|-',10.2689),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 516,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_Ext-4C-R_Ext-6R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,D}
4   C   ux {3,D} {6,S}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H ux {4,S} {7,[S,D,T,B,Q]}
7   R!H u0 r0 {6,[S,D,T,B,Q]}
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
    index = 517,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_Ext-4C-R_Ext-6R!H-R_N-5R!H->C",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,D}
4   C   ux {3,D} {6,S}
5   O   ux {2,[S,D,T,B,Q]}
6   R!H ux {4,S} {7,[S,D,T,B,Q]}
7   R!H u0 r0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.31303,-1.9065,-3.88355,-4.753,-4.90249,-4.84466,-2.99836],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (83.8101,'kcal/mol','+|-',4.17612),
        S298 = (4.14529,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
COC=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 518,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_5R!H-inRing",
    group = 
"""
1 * C u1 {2,S} {3,S}
2   C u0 r0 {1,S} {5,[S,D,T,B,Q]}
3   C u0 {1,S} {4,D}
4   C u0 {3,D}
5   C u0 r1 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.86903,0.730741,-0.447496,-1.08479,-1.94097,-2.65093,-3.34714],'cal/mol/K','+|-',[5.46826,3.23643,3.25494,3.39457,3.16236,3.19199,3.16919]),
        H298 = (80.5721,'kcal/mol','+|-',11.8394),
        S298 = (-0.718341,'cal/mol/K','+|-',7.52975),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 519,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_5R!H-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S}
2   C   u0 r0 {1,S} {5,[S,D,T,B,Q]}
3   C   u0 r0 {1,S} {4,D}
4   C   u0 r0 {3,D}
5   C   u0 r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.291775,0.487198,-0.174856,-0.648456,-1.94915,-2.80455,-3.42111],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (76.9442,'kcal/mol','+|-',4.17612),
        S298 = (1.69768,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]CC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 520,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {5,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,D}
4   C   ux {3,D}
5   R!H ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.404688,-0.928649,-1.84202,-2.2638,-2.58758,-2.72928,-3.26238],'cal/mol/K','+|-',[4.0698,2.75067,2.11279,2.05318,2.42198,2.86728,2.74104]),
        H298 = (85.4701,'kcal/mol','+|-',2.88312),
        S298 = (0.0614275,'cal/mol/K','+|-',18.49),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 521,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r0 {1,S} {5,[S,D,T,B,Q]}
3   C ux {1,[S,D,T,B,Q]} {4,D}
4   C ux {3,D}
5   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.02304,-0.62564,-1.73226,-2.19906,-2.47822,-2.55389,-3.07715],'cal/mol/K','+|-',[3.87866,2.91271,2.41112,2.37259,2.78267,3.25664,3.09212]),
        H298 = (84.8429,'kcal/mol','+|-',2.61734),
        S298 = (-0.342081,'cal/mol/K','+|-',21.6043),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 522,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r0 {1,S} {5,[S,D,T,B,Q]}
3   C ux {1,[S,D,T,B,Q]} {4,D}
4   C ux {3,D}
5   C ux r0 {2,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.793562,-0.848356,-1.96853,-2.42066,-2.68019,-2.77189,-3.36713],'cal/mol/K','+|-',[4.00948,2.8639,2.16818,2.1777,2.76555,3.297,2.85464]),
        H298 = (84.8554,'kcal/mol','+|-',2.75337),
        S298 = (-3.27408,'cal/mol/K','+|-',15.1052),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 523,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   C u0 r0 {1,S} {5,[S,D,T,B,Q]}
3   C u0 r0 {1,S} {4,D}
4   C u0 r0 {3,D}
5   C u0 r0 {2,[S,D,T,B,Q]} {6,S}
6   C u0 r0 {5,S} {7,[S,D,T,B,Q]}
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
    index = 524,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r0 {1,S} {5,S}
3   C ux {1,[S,D,T,B,Q]} {4,D}
4   C ux {3,D}
5   C ux r0 {2,S} {6,S}
6   C ux {5,S} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.57526,-0.438003,-1.79806,-2.16519,-2.07865,-1.94613,-2.72632],'cal/mol/K','+|-',[4.22594,3.32796,2.69485,2.61306,2.73569,2.88678,2.7621]),
        H298 = (84.9055,'kcal/mol','+|-',4.32521),
        S298 = (-8.12876,'cal/mol/K','+|-',6.89702),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 525,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r0 {1,S} {5,S}
3   C ux {1,[S,D,T,B,Q]} {4,D}
4   C ux {3,D}
5   C ux r0 {2,S} {6,S}
6   C ux {5,S} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9   C u0 {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.19114,-0.0268501,-1.59524,-1.94653,-1.73288,-1.52637,-2.44761],'cal/mol/K','+|-',[4.10498,3.42381,3.01209,2.87424,2.74286,2.7273,2.95739]),
        H298 = (84.7856,'kcal/mol','+|-',4.9809),
        S298 = (-9.59451,'cal/mol/K','+|-',4.35405),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 526,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R_Ext-5C-R",
    group = 
"""
1  * C   u1 {2,S} {3,[S,D,T,B,Q]}
2    C   ux r0 {1,S} {5,S}
3    C   ux {1,[S,D,T,B,Q]} {4,D}
4    C   ux {3,D}
5    C   ux r0 {2,S} {6,S} {10,[S,D,T,B,Q]}
6    C   ux {5,S} {7,[S,D,T,B,Q]}
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
    index = 527,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-12R!H-R_Ext-12R!H-R_Sp-12R!H=11R!H",
    group = 
"""
1  * C u1 r0 {2,S} {3,S}
2    C u0 r0 {1,S} {5,S}
3    C u0 r0 {1,S} {4,D}
4    C u0 r0 {3,D}
5    C u0 r0 {2,S} {6,S}
6    C u0 r0 {5,S} {7,[S,D,T,B,Q]}
7    C u0 {6,[S,D,T,B,Q]} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]}
9    C u0 r1 {8,[S,D,T,B,Q]} {10,S}
10   C u0 r1 {9,S} {11,[S,D,T,B,Q]}
11   C ux r1 {10,[S,D,T,B,Q]} {12,D}
12   C u0 r1 {11,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.37633,-0.127981,-1.70659,-1.99862,-1.40919,-1.02177,-1.95107],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.9087,'kcal/mol','+|-',4.17612),
        S298 = (-9.91989,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]CCC=CCC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 528,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-12R!H-R_Ext-12R!H-R_N-Sp-12R!H=11R!H",
    group = 
"""
1  * C u1 r0 {2,S} {3,S}
2    C u0 r0 {1,S} {5,S}
3    C u0 r0 {1,S} {4,D}
4    C u0 r0 {3,D}
5    C u0 r0 {2,S} {6,S}
6    C u0 r0 {5,S} {7,[S,D,T,B,Q]}
7    C u0 {6,[S,D,T,B,Q]} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]}
9    C u0 r1 {8,[S,D,T,B,Q]} {10,S}
10   C u0 r1 {9,S} {11,[S,D,T,B,Q]}
11   C ux r1 {10,[S,D,T,B,Q]} {12,S}
12   C u0 r1 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.510997,-1.09712,-2.30912,-2.55027,-2.26292,-1.73496,-2.11712],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.1095,'kcal/mol','+|-',4.17612),
        S298 = (-11.162,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]CCC=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 529,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   C u0 r0 {1,S} {5,[S,D,T,B,Q]}
3   C u0 r0 {1,S} {4,D}
4   C u0 r0 {3,D}
5   C u0 r0 {2,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   C u0 r0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.51464,0.822012,-0.196489,-0.758637,-1.16542,-1.13689,-1.19227],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.7172,'kcal/mol','+|-',4.17612),
        S298 = (18.7159,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=CC[CH]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 530,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_N-5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   C u0 r0 {1,S} {5,[S,D,T,B,Q]}
3   C u0 r0 {1,S} {4,D}
4   C u0 r0 {3,D}
5   O u0 r0 {2,[S,D,T,B,Q]}
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
    index = 531,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-4C-R_5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   C u0 r0 {1,S}
3   C u0 r0 {1,S} {4,D}
4   C u0 r0 {3,D} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]}
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
    index = 532,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,S}
2   C u0 r0 {1,S}
3   C u0 {1,S} {4,D}
4   C u0 {3,D} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.432422,-2.37352,-3.23841,-3.48797,-3.21967,-2.95042,-3.33947],'cal/mol/K','+|-',[4.40538,5.13738,5.67865,5.91428,5.92778,5.82146,5.41892]),
        H298 = (86.4996,'kcal/mol','+|-',14.6445),
        S298 = (-1.20734,'cal/mol/K','+|-',10.6293),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 533,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_6R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   C u0 r0 {1,S}
3   C u0 r0 {1,S} {4,D}
4   C u0 r0 {3,D} {5,[S,D,T,B,Q]}
5   O u0 r0 {4,[S,D,T,B,Q]} {6,S}
6   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.51682,-3.80498,-4.906,-5.25498,-4.99233,-4.67848,-4.89529],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.2375,'kcal/mol','+|-',4.17612),
        S298 = (2.38053,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]C=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 534,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S} {3,S}
2   C                      u0 r0 {1,S}
3   C                      u0 r0 {1,S} {4,D}
4   C                      u0 r0 {3,D} {5,[S,D,T,B,Q]}
5   O                      u0 r0 {4,[S,D,T,B,Q]} {6,S}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,S}
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
    index = 535,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r0 {1,S}
3   C ux {1,[S,D,T,B,Q]} {4,D}
4   O ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.28158,-0.961961,-0.911235,-0.91395,-1.22887,-1.76225,-3.03701],'cal/mol/K','+|-',[3.75922,3.68922,3.59763,3.75297,3.7903,3.71065,3.12944]),
        H298 = (91.4787,'kcal/mol','+|-',3.67981),
        S298 = (-2.03298,'cal/mol/K','+|-',9.08736),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 536,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r0 {1,S}
3   C ux {1,[S,D,T,B,Q]} {4,D} {5,S}
4   O ux {3,D}
5   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.62536,-1.23095,-1.08879,-1.08667,-1.42789,-2.02351,-3.28286],'cal/mol/K','+|-',[3.2196,3.06442,2.83162,2.59521,2.25022,2.20767,2.31754]),
        H298 = (90.3827,'kcal/mol','+|-',3.04852),
        S298 = (-1.86158,'cal/mol/K','+|-',4.21915),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 537,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C_Ext-3R!H-R_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {6,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,D} {5,S}
4   O   ux r0 {3,D}
5   C   u0 r0 {3,S}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 538,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   C u0 r0 {1,S}
3   C u0 r0 {1,S} {4,D} {5,S}
4   O u0 r0 {3,D}
5   C u0 r0 {3,S} {6,D}
6   C u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.199835,0.342736,0.270056,0.0030552,-0.903978,-1.90399,-2.79802],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.0944,'kcal/mol','+|-',4.17612),
        S298 = (-4.47982,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 539,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   C u0 r0 {1,S}
3   C u0 r0 {1,S} {4,D} {5,S}
4   O u0 r0 {3,D}
5   C u0 r0 {3,S} {6,[S,T,Q,B]}
6   C u0 r0 {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.64208,-1.56672,-1.44606,-1.39205,-1.66024,-2.23263,-3.61126],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (90.3244,'kcal/mol','+|-',1.69706),
        S298 = (-1.21536,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 540,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C_Ext-2CN-R_Ext-2CN-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S}
2   C   u0 r0 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   u0 r0 {1,S} {4,D}
4   O   u0 r0 {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 541,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * R   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   R!H ux {1,[S,D,T,B,Q]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.508507,-1.84526,-2.71516,-3.26513,-3.63198,-3.86274,-4.45429],'cal/mol/K','+|-',[3.28524,3.13451,3.26442,3.00327,2.36817,2.27763,2.89162]),
        H298 = (98.1456,'kcal/mol','+|-',6.35278),
        S298 = (2.1272,'cal/mol/K','+|-',10.5705),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 542,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H",
    group = 
"""
1 * R   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   R!H ux {1,[S,D,T,B,Q]} {4,S}
4   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.541311,-1.86189,-2.76103,-3.26335,-3.6312,-3.86557,-4.40054],'cal/mol/K','+|-',[3.36152,3.21727,3.32581,3.08623,2.4331,2.33983,2.92636]),
        H298 = (98.4991,'kcal/mol','+|-',4.43142),
        S298 = (2.27383,'cal/mol/K','+|-',10.7745),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 543,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_3R!H->N",
    group = 
"""
1 * R   u1 r0 {2,S} {3,S}
2   C   u0 r0 {1,S}
3   N   u0 r0 {1,S} {4,S}
4   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.411242,-1.77775,-2.51199,-3.12353,-4.04114,-4.64176,-5.33041],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (95.5584,'kcal/mol','+|-',1.69706),
        S298 = (7.3243,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN([CH]C)O - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 544,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N",
    group = 
"""
1 * R   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   C   ux {1,[S,D,T,B,Q]} {4,S}
4   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.559892,-1.87391,-2.79661,-3.28333,-3.57264,-3.75469,-4.2677],'cal/mol/K','+|-',[3.60343,3.44959,3.56053,3.30756,2.58538,2.42048,3.0372]),
        H298 = (99.0767,'kcal/mol','+|-',3.78554),
        S298 = (1.55233,'cal/mol/K','+|-',10.7339),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 545,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   C   ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   R!H ux {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.235207,-2.22604,-3.56979,-4.07466,-3.99328,-3.87554,-4.14106],'cal/mol/K','+|-',[3.72761,4.12249,4.02887,3.66914,3.22349,3.28742,4.22687]),
        H298 = (97.8249,'kcal/mol','+|-',4.24357),
        S298 = (-1.50568,'cal/mol/K','+|-',11.0324),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 546,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   C   ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   R!H ux {3,S} {7,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34389,-2.38084,-3.73155,-4.05722,-3.62826,-3.27602,-3.32686],'cal/mol/K','+|-',[4.35747,4.93118,4.9031,4.51676,3.73917,3.40258,4.33388]),
        H298 = (97.4214,'kcal/mol','+|-',4.94198),
        S298 = (-3.88645,'cal/mol/K','+|-',10.5364),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 547,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   C   ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   R!H ux {3,S} {7,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   C   ux {4,[S,D,T,B,Q]} {8,[S,D]}
8   C   ux {7,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.22172,-1.88501,-3.28601,-3.76052,-3.60352,-3.45342,-3.8779],'cal/mol/K','+|-',[3.7377,4.78056,4.89169,4.76382,4.15833,3.6553,3.76853]),
        H298 = (97.7652,'kcal/mol','+|-',5.13814),
        S298 = (-2.23717,'cal/mol/K','+|-',7.5498),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 548,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R",
    group = 
"""
1 * C u1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r0 {1,S} {9,[S,D,T,B,Q]}
3   C ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C ux {3,S} {7,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
7   C ux {4,[S,D,T,B,Q]} {8,[S,D]}
8   C ux {7,[S,D]}
9   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.368529,-2.74518,-4.12838,-4.51298,-4.06698,-3.4754,-3.58808],'cal/mol/K','+|-',[3.00056,3.22615,3.55656,3.85058,4.12243,4.17956,4.04506]),
        H298 = (97.0311,'kcal/mol','+|-',4.43457),
        S298 = (-3.07478,'cal/mol/K','+|-',7.54698),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 549,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R_Ext-8R!H-R_Sp-8R!H=7C",
    group = 
"""
1  * C u1 {2,S} {3,[S,D,T,B,Q]}
2    C ux r0 {1,S} {9,S}
3    C ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4    C ux {3,S} {7,[S,D,T,B,Q]}
5    C ux {3,[S,D,T,B,Q]} {6,S}
6    C u0 {5,S}
7    C ux {4,[S,D,T,B,Q]} {8,D}
8    C u0 {7,D} {10,S}
9    C u0 {2,S}
10   C ux {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.359238,-2.25974,-3.45501,-3.73064,-3.20942,-2.62988,-2.8749],'cal/mol/K','+|-',[3.55944,3.02045,2.6941,2.59186,2.64732,2.86568,3.39166]),
        H298 = (96.817,'kcal/mol','+|-',5.0489),
        S298 = (-4.59824,'cal/mol/K','+|-',5.37583),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 550,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R_Ext-8R!H-R_Sp-8R!H=7C_4R!H-inRing",
    group = 
"""
1  * C u1 {2,S} {3,[S,D,T,B,Q]}
2    C ux r0 {1,S} {9,S}
3    C ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4    C ux r1 {3,S} {7,[S,D,T,B,Q]}
5    C ux {3,[S,D,T,B,Q]} {6,S}
6    C u0 {5,S}
7    C ux {4,[S,D,T,B,Q]} {8,D}
8    C u0 {7,D} {10,S}
9    C u0 {2,S}
10   C ux {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.92384,-2.56805,-3.56595,-3.73373,-3.22027,-2.51734,-2.49407],'cal/mol/K','+|-',[3.78883,3.55411,3.29964,3.17835,3.26809,3.57589,4.02402]),
        H298 = (96.9652,'kcal/mol','+|-',6.23132),
        S298 = (-3.3757,'cal/mol/K','+|-',4.31225),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 551,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R_Ext-8R!H-R_Sp-8R!H=7C_4R!H-inRing_Ext-10R!H-R_Ext-4R!H-R",
    group = 
"""
1  * C   u1 {2,S} {3,[S,D,T,B,Q]}
2    C   ux r0 {1,S} {9,S}
3    C   ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4    C   ux r1 {3,S} {7,[S,D,T,B,Q]} {12,[S,D,T,B,Q]}
5    C   ux r0 {3,[S,D,T,B,Q]} {6,S}
6    C   u0 r0 {5,S}
7    C   ux r1 {4,[S,D,T,B,Q]} {8,D}
8    C   u0 r1 {7,D} {10,S}
9    C   u0 r0 {2,S}
10   C   ux r1 {8,S} {11,[S,D,T,B,Q]}
11   C   u0 r1 {10,[S,D,T,B,Q]}
12   R!H ux {4,[S,D,T,B,Q]}
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
    index = 552,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R_Ext-8R!H-R_Sp-8R!H=7C_N-4R!H-inRing",
    group = 
"""
1  * C u1 {2,S} {3,[S,D,T,B,Q]}
2    C ux r0 {1,S} {9,S}
3    C ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4    C ux r0 {3,S} {7,[S,D,T,B,Q]}
5    C ux r0 {3,[S,D,T,B,Q]} {6,S}
6    C u0 r0 {5,S}
7    C ux r1 {4,[S,D,T,B,Q]} {8,D}
8    C u0 r1 {7,D} {10,S}
9    C u0 r0 {2,S}
10   C ux r1 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.769968,-1.64313,-3.23314,-3.72444,-3.18772,-2.85495,-3.63655],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.5207,'kcal/mol','+|-',4.17612),
        S298 = (-7.04331,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]C(CC)CC1=CCCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 553,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R_Ext-8R!H-R_N-Sp-8R!H=7C",
    group = 
"""
1  * C u1 r0 {2,S} {3,S}
2    C u0 r0 {1,S} {9,[S,D,T,B,Q]}
3    C u0 r0 {1,S} {4,S} {5,S}
4    C u0 {3,S} {7,S}
5    C u0 {3,S} {6,[S,D,T,B,Q]}
6    C ux {5,[S,D,T,B,Q]}
7    C u0 r1 {4,S} {8,S}
8    C ux r1 {7,S} {10,S}
9    C ux {2,[S,D,T,B,Q]}
10   C u0 r1 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.396402,-4.20148,-6.14848,-6.86,-6.63967,-6.01196,-5.72763],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (97.6733,'kcal/mol','+|-',4.17612),
        S298 = (1.49561,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=CCCC1C([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 554,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_N-7R!H->C",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   C   ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   R!H ux {3,S} {7,[S,D,T,B,Q]}
5   R!H ux r0 {3,[S,D,T,B,Q]} {6,S}
6   R!H u0 r0 {5,S}
7   O   ux {4,[S,D,T,B,Q]} {8,S}
8   C   u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.17194,-4.85996,-5.95926,-5.54068,-3.75194,-2.38905,-0.571621],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.7021,'kcal/mol','+|-',4.17612),
        S298 = (-12.1329,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]C(CC)OOC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 555,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S}
2   C   u0 r0 {1,S}
3   C   u0 r0 {1,S} {4,S} {5,S}
4   C   u0 {3,S}
5   R!H u0 {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 556,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {6,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r0 {3,S}
5   C   ux r0 {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 557,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_1R->C",
    group = 
"""
1 * C   u1 {2,S} {3,S}
2   C   u0 r0 {1,S}
3   C   u0 {1,S} {4,S}
4   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.05283,-1.54111,-1.93414,-2.35431,-3.03487,-3.54737,-4.38221],'cal/mol/K','+|-',[4.34148,3.35035,2.80583,2.45901,2.02793,1.83009,1.73475]),
        H298 = (99.8378,'kcal/mol','+|-',2.48604),
        S298 = (5.34937,'cal/mol/K','+|-',4.32353),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 558,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_1R->C_4R!H->C",
    group = 
"""
1 * C u1 {2,S} {3,S}
2   C u0 r0 {1,S}
3   C u0 {1,S} {4,S}
4   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21406,-2.37572,-2.56738,-2.86201,-3.3663,-3.77883,-4.55034],'cal/mol/K','+|-',[2.00006,2.09726,2.18818,2.13866,2.06282,2.01975,2.00175]),
        H298 = (99.2703,'kcal/mol','+|-',2.44762),
        S298 = (4.19511,'cal/mol/K','+|-',2.01922),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 559,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_1R->C_4R!H->C_Ext-4C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {3,S}
2   C   u0 r0 {1,S}
3   C   u0 r0 {1,S} {4,S}
4   C   u0 {3,S} {5,[S,D,T,B,Q]}
5   O   u0 r0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.20839,-2.59891,-2.88125,-3.12984,-3.54492,-3.87844,-4.52075],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (99.4401,'kcal/mol','+|-',1.69706),
        S298 = (4.09684,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 560,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_1R->C_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S}
2   C u0 r0 {1,S}
3   C u0 r0 {1,S} {4,S}
4   O u0 {3,S}
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
    index = 561,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_N-1R->C",
    group = 
"""
1 * N   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   C   ux {1,[S,D,T,B,Q]} {4,S}
4   R!H ux r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.21496,-1.20068,-2.30653,-3.12899,-3.82014,-4.22186,-4.54865],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (94.4872,'kcal/mol','+|-',4.17612),
        S298 = (0.596722,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[N]CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 562,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H",
    group = 
"""
1 * R   u1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r0 {1,S}
3   R!H ux {1,[S,D,T,B,Q]} {4,T}
4   R!H ux {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.147574,-1.5128,-1.79761,-3.30076,-3.64767,-3.80616,-5.52932],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (85.1051,'kcal/mol','+|-',4.17612),
        S298 = (-0.805385,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC#C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 563,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.275566,-1.33202,-1.98141,-2.25956,-2.51809,-2.78137,-3.60977],'cal/mol/K','+|-',[4.93892,6.19502,6.23508,5.50693,3.99034,3.31149,3.26471]),
        H298 = (89.6366,'kcal/mol','+|-',14.778),
        S298 = (-0.473151,'cal/mol/K','+|-',10.0413),
    ),
    shortDesc = """Radical correction fitted to 66 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 564,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.566065,-1.80964,-2.47055,-2.68502,-2.81384,-2.96095,-3.59522],'cal/mol/K','+|-',[5.18271,6.40211,6.41174,5.57403,3.87887,3.33655,3.33134]),
        H298 = (86.9109,'kcal/mol','+|-',11.9254),
        S298 = (-0.0108804,'cal/mol/K','+|-',10.6135),
    ),
    shortDesc = """Radical correction fitted to 54 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 565,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.295677,-0.290188,-0.862226,-1.26257,-1.83664,-2.37676,-3.5244],'cal/mol/K','+|-',[3.46194,2.68186,2.32375,2.01668,1.5796,1.64036,1.84773]),
        H298 = (87.5719,'kcal/mol','+|-',4.98608),
        S298 = (-2.16417,'cal/mol/K','+|-',5.94061),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 566,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0680192,-0.229603,-0.671663,-1.04501,-1.68657,-2.2988,-3.56057],'cal/mol/K','+|-',[2.90491,2.39732,1.98223,1.82083,1.64835,1.68567,1.72385]),
        H298 = (87.7979,'kcal/mol','+|-',3.80143),
        S298 = (-1.55501,'cal/mol/K','+|-',3.39508),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 567,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.136036,-0.386095,-0.736534,-1.03977,-1.59299,-2.19257,-3.46085],'cal/mol/K','+|-',[2.7553,2.55364,2.18952,2.00862,1.73091,1.69604,1.63033]),
        H298 = (87.576,'kcal/mol','+|-',3.98178),
        S298 = (-1.26977,'cal/mol/K','+|-',3.09708),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 568,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,S}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.019996,-0.254656,-0.603735,-0.901924,-1.47495,-2.07408,-3.34835],'cal/mol/K','+|-',[2.62237,2.32225,1.87572,1.60799,1.39025,1.33999,1.29874]),
        H298 = (87.4708,'kcal/mol','+|-',3.74682),
        S298 = (-1.40496,'cal/mol/K','+|-',2.92896),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 569,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   C u0 {2,S}
5   C ux {3,S}
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
    index = 570,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R_Ext-6R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   C u0 r0 {2,S}
5   C ux {3,S}
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
    index = 571,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R_Ext-6R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D} {4,S}
3   C                      u0 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   C                      u0 r0 {2,S}
5   C                      ux {3,S}
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
    index = 572,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D} {5,S}
4   C   u0 {2,S}
5   R!H u0 {3,S} {6,S}
6   C   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.653431,0.221444,-0.453994,-0.860097,-1.41969,-2.00523,-3.11831],'cal/mol/K','+|-',[3.91705,3.26886,2.62824,2.26312,2.00082,2.00484,2.00818]),
        H298 = (87.6402,'kcal/mol','+|-',2.45885),
        S298 = (-2.21189,'cal/mol/K','+|-',2.06393),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 573,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D} {5,S}
4   C   u0 r0 {2,S} {7,[S,D,T,B,Q]}
5   R!H u0 r0 {3,S} {6,S}
6   C   u0 r0 {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.84419,1.1356,0.14888,-0.485643,-1.3994,-2.05443,-3.05427],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (87.8293,'kcal/mol','+|-',1.69706),
        S298 = (-2.03169,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=COC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 574,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,S}
4   C   ux {2,[S,D,T,B,Q]} {6,D}
5   O   ux {3,S}
6   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.713089,-0.799738,-0.871609,-1.0129,-1.44426,-1.98804,-3.3364],'cal/mol/K','+|-',[3.13313,2.79068,2.3549,2.08812,1.90473,1.9158,1.90732]),
        H298 = (88.2784,'kcal/mol','+|-',4.59465),
        S298 = (-0.341842,'cal/mol/K','+|-',3.53338),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 575,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-4R!H-R_6R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D} {5,S}
4   C u0 r0 {2,S} {6,D}
5   O u0 r0 {3,S}
6   O u0 r0 {4,D}
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
    index = 576,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-4R!H-R_N-6R!H->O",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D} {5,S}
4   C ux {2,[S,D,T,B,Q]} {6,D}
5   O ux {3,S}
6   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46381,-1.44428,-1.36072,-1.36687,-1.58386,-1.97925,-3.17343],'cal/mol/K','+|-',[2.18484,2.0669,2.00407,2.09287,2.33558,2.45059,2.30326]),
        H298 = (87.0877,'kcal/mol','+|-',2.50468),
        S298 = (-0.873027,'cal/mol/K','+|-',4.10663),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 577,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-4R!H-R_N-6R!H->O_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {5,S}
4   C   ux {2,[S,D,T,B,Q]} {6,D} {7,[S,D,T,B,Q]}
5   O   ux {3,S}
6   C   ux {4,D}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 578,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_N-Sp-5R!H-3C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r0 {2,D} {5,[B,D,T,Q]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H u0 r0 {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.28277,-2.81772,-3.19333,-3.58994,-3.77659,-4.3847,-5.54201],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (92.1399,'kcal/mol','+|-',4.17612),
        S298 = (1.23125,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=C=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 579,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.50984,0.839112,-0.643363,-1.46356,-2.56102,-3.46591,-4.94643],'cal/mol/K','+|-',[3.24384,3.19743,3.16589,3.17857,3.2189,3.16845,3.3574]),
        H298 = (88.5323,'kcal/mol','+|-',6.19425),
        S298 = (-4.6854,'cal/mol/K','+|-',3.17995),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 580,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D}
4   C   u0 r0 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]}
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
    index = 581,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D}
4   C u0 r0 {2,S} {5,S}
5   O u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.29381,0.136062,-0.18831,-0.751023,-1.71692,-2.19366,-3.22971],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (89.1819,'kcal/mol','+|-',1.69706),
        S298 = (-1.27551,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=C)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 582,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.562477,-0.408267,-1.11122,-1.46604,-1.7978,-2.16876,-3.18731],'cal/mol/K','+|-',[4.72489,3.61718,3.17816,2.66794,1.77256,1.70084,2.18788]),
        H298 = (86.6426,'kcal/mol','+|-',7.37383),
        S298 = (-3.98726,'cal/mol/K','+|-',7.22515),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 583,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.671798,-0.467069,-1.23044,-1.57782,-1.83992,-2.16174,-3.14443],'cal/mol/K','+|-',[5.08347,3.90537,3.37833,2.82186,1.90428,1.84048,2.35719]),
        H298 = (86.4483,'kcal/mol','+|-',8.36344),
        S298 = (-4.25549,'cal/mol/K','+|-',7.6857),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 584,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {4,S}
4   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.832091,-0.383015,-1.18677,-1.52884,-1.77293,-2.08374,-3.04723],'cal/mol/K','+|-',[5.43602,4.21162,3.65828,3.04672,2.01287,1.9201,2.48668]),
        H298 = (86.7572,'kcal/mol','+|-',6.74875),
        S298 = (-4.70346,'cal/mol/K','+|-',7.89394),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 585,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_4R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {4,S}
4   O ux {3,S}
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
    index = 586,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.912901,-0.52335,-1.4306,-1.7625,-1.8792,-2.08781,-2.94532],'cal/mol/K','+|-',[6.06191,4.6555,3.90937,3.20562,2.18517,2.14207,2.73135]),
        H298 = (87.4361,'kcal/mol','+|-',7.69418),
        S298 = (-5.03877,'cal/mol/K','+|-',8.66905),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 587,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.920486,-0.689776,-1.65716,-1.98144,-2.02408,-2.16912,-3.02367],'cal/mol/K','+|-',[6.43465,4.80014,3.83008,3.03123,2.07595,2.19251,2.84074]),
        H298 = (87.7628,'kcal/mol','+|-',7.61761),
        S298 = (-4.96033,'cal/mol/K','+|-',9.18841),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 588,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_Ext-4C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {4,S}
4   C   u0 r0 {3,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H u0 {5,[S,D,T,B,Q]}
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
    index = 589,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {4,S}
4   C ux {3,S} {5,S}
5   C ux {4,S} {6,D}
6   C ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.65309,1.17336,-0.266785,-1.08491,-2.03442,-2.59868,-3.64324],'cal/mol/K','+|-',[4.52537,4.13443,3.72538,3.69991,3.54264,3.37805,2.71566]),
        H298 = (88.5193,'kcal/mol','+|-',5.19585),
        S298 = (-6.94289,'cal/mol/K','+|-',6.60311),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 590,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3C-R",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {4,S} {7,S}
4   C ux {3,S} {5,S}
5   C ux {4,S} {6,D}
6   C ux {5,D}
7   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.72129,2.01097,0.365941,-0.517122,-1.58609,-2.21211,-3.48053],'cal/mol/K','+|-',[3.19996,3.74375,3.84907,4.03833,4.11622,3.98782,3.28343]),
        H298 = (88.0559,'kcal/mol','+|-',6.10028),
        S298 = (-8.3707,'cal/mol/K','+|-',5.91109),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 591,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-8R!H-R",
    group = 
"""
1  * C   u1 {2,S}
2    C   ux r0 {1,S} {3,D}
3    C   ux {2,D} {4,S} {7,S}
4    C   ux {3,S} {5,S}
5    C   ux {4,S} {6,D}
6    C   ux {5,D}
7    C   u0 r0 {3,S} {8,[S,D,T,B,Q]}
8    C   ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
9    R!H ux {8,[S,D,T,B,Q]}
10   R!H ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.89439,2.71946,1.14177,0.370859,-0.654475,-1.35314,-3.1681],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.5158,'kcal/mol','+|-',4.17612),
        S298 = (-10.1364,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=C(CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 592,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {4,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.177071,-0.939687,-1.77587,-2.00201,-1.85866,-1.9746,-2.78081],'cal/mol/K','+|-',[5.95699,3.5689,2.72151,2.34758,2.06561,2.45733,3.75423]),
        H298 = (86.3891,'kcal/mol','+|-',3.30645),
        S298 = (-4.87512,'cal/mol/K','+|-',10.733),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 593,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_5R!H-inRing",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {4,S}
4   C ux {3,S} {5,S}
5   C ux r1 {4,S} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.12828,-0.150117,-1.67892,-2.04684,-1.60565,-1.56817,-2.36123],'cal/mol/K','+|-',[4.14903,3.97638,3.7068,3.19676,2.6505,3.01199,4.9303]),
        H298 = (85.9302,'kcal/mol','+|-',5.37695),
        S298 = (-8.02666,'cal/mol/K','+|-',9.40979),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 594,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_5R!H-inRing_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {4,S}
4   C ux {3,S} {5,S}
5   C ux r1 {4,S} {6,S} {7,[S,D,T,B,Q]} {8,S}
6   C ux {5,S}
7   C ux {5,[S,D,T,B,Q]}
8   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.07504,-0.0946947,-1.42531,-1.80733,-1.43364,-1.39337,-1.52029],'cal/mol/K','+|-',[5.57024,5.31189,4.75434,3.96591,3.16335,3.752,5.32073]),
        H298 = (85.9512,'kcal/mol','+|-',6.79603),
        S298 = (-8.80379,'cal/mol/K','+|-',12.6198),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 595,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_5R!H-inRing_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Int-10R!H-7R!H",
    group = 
"""
1  * C u1 {2,S}
2    C ux r0 {1,S} {3,D}
3    C ux {2,D} {4,S}
4    C ux {3,S} {5,S}
5    C ux r1 {4,S} {6,S} {7,[S,D,T,B,Q]} {8,S}
6    C ux r1 {5,S} {9,[S,D,T,B,Q]}
7    C ux r1 {5,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
8    C u0 {5,S}
9    C ux r1 {6,[S,D,T,B,Q]} {10,[S,D]}
10   C u0 r1 {7,[S,D,T,B,Q]} {9,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.453786,-1.60367,-2.68049,-2.65353,-1.40449,-0.679449,-0.00742515],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (84.7624,'kcal/mol','+|-',4.17612),
        S298 = (-13.1232,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CCC1(CC=CC)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 596,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-5R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {4,S}
4   C u0 r0 {3,S} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]} {6,S}
6   C u0 {5,S}
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
    index = 597,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_N-Sp-4R!H-3C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,D}
3   C ux {2,D} {4,[B,D,T,Q]}
4   C u0 {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.370103,-1.01342,-1.51425,-1.89621,-2.27538,-2.66877,-3.77624],'cal/mol/K','+|-',[3.29544,3.17804,3.16741,3.17845,3.23978,3.28875,3.2038]),
        H298 = (83.3423,'kcal/mol','+|-',22.3404),
        S298 = (-1.34372,'cal/mol/K','+|-',4.11531),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 598,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_N-Sp-4R!H-3C_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,D}
3   C   ux {2,D} {4,D}
4   C   u0 r0 {3,D} {5,[S,D,T,B,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0422465,-0.901633,-1.45051,-1.78297,-2.02633,-2.34941,-3.59446],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (90.9598,'kcal/mol','+|-',4.17612),
        S298 = (-2.27483,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=C=CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 599,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_N-Sp-2CN-1C",
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
    index = 600,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_N-Sp-2CN-1C_Ext-3C-R",
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
    index = 601,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.78034,-3.95067,-4.73683,-4.68938,-4.1908,-3.78414,-3.69502],'cal/mol/K','+|-',[6.27012,7.65611,7.58269,6.53048,4.53547,4.40148,4.80051]),
        H298 = (85.6128,'kcal/mol','+|-',19.5294),
        S298 = (3.0233,'cal/mol/K','+|-',12.7459),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 602,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.52845,-4.54248,-5.04117,-4.73196,-3.87611,-3.32363,-3.26395],'cal/mol/K','+|-',[5.98266,7.62289,7.82218,7.06586,5.23926,4.79781,4.49149]),
        H298 = (85.2845,'kcal/mol','+|-',24.3865),
        S298 = (2.41288,'cal/mol/K','+|-',11.9015),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 603,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99026,-4.289,-5.07521,-4.94709,-4.19921,-3.7534,-3.66637],'cal/mol/K','+|-',[6.26894,8.24823,8.4011,7.39442,5.30279,4.91732,4.98391]),
        H298 = (90.5216,'kcal/mol','+|-',11.9973),
        S298 = (3.32293,'cal/mol/K','+|-',11.9286),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 604,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R",
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
        Cpdata = ([-1.6926,-3.73847,-4.48234,-4.41732,-3.86224,-3.54728,-3.80682],'cal/mol/K','+|-',[6.45082,7.87317,7.58115,6.21754,3.73025,3.24947,4.80953]),
        H298 = (90.3391,'kcal/mol','+|-',12.5295),
        S298 = (1.73169,'cal/mol/K','+|-',7.72618),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 605,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05305,-5.48743,-6.59946,-6.19454,-4.67157,-3.67355,-3.14058],'cal/mol/K','+|-',[10.1625,10.6608,9.51582,7.90634,5.49887,5.02921,7.23868]),
        H298 = (96.3502,'kcal/mol','+|-',9.74927),
        S298 = (0.915958,'cal/mol/K','+|-',12.2278),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 606,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->O",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.47932,-6.06291,-7.18575,-6.64076,-4.77345,-3.55959,-2.65316],'cal/mol/K','+|-',[11.5118,11.9319,10.5468,8.81498,6.30132,5.74842,7.94957]),
        H298 = (97.4576,'kcal/mol','+|-',9.63667),
        S298 = (1.12846,'cal/mol/K','+|-',14.0649),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 607,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->O_Ext-5O-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.10167,-3.41003,-5.04573,-5.18741,-4.5927,-4.328,-4.18496],'cal/mol/K','+|-',[6.17033,6.61946,7.49039,8.06408,7.61199,5.87899,6.13559]),
        H298 = (96.5328,'kcal/mol','+|-',10.7639),
        S298 = (0.527869,'cal/mol/K','+|-',16.9482),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 608,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->O_Ext-5O-R_4C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   u0 r0 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C   u0 r0 {2,D}
4   C   u0 r1 {2,S} {5,S} {6,S}
5   O   u0 {4,S} {8,S}
6   R!H ux {4,S} {7,[S,D,T,B,Q]}
7   R!H u0 {6,[S,D,T,B,Q]}
8   O   u0 {5,S}
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
    index = 609,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->O_Ext-5O-R_N-4C-inRing",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   R!H u0 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
8   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.706059,-1.98022,-3.11354,-2.99096,-2.57815,-2.92473,-2.76217],'cal/mol/K','+|-',[8.00287,5.93601,4.39064,3.30748,3.89226,4.30488,4.83459]),
        H298 = (93.7974,'kcal/mol','+|-',6.366),
        S298 = (-4.21983,'cal/mol/K','+|-',5.49304),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 610,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->O_Ext-5O-R_N-4C-inRing_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {9,[S,D,T,B,Q]}
4   C   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   ux r0 {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   R!H u0 r0 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux r0 {6,[S,D,T,B,Q]}
8   O   ux r0 {5,[S,D,T,B,Q]}
9   R!H ux {3,[S,D,T,B,Q]}
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
    index = 611,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_N-5R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   u0 r0 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C   u0 r0 {2,D}
4   C   u0 {2,S} {5,S} {6,[S,D,T,B,Q]}
5   C   u0 {4,S}
6   R!H ux {4,[S,D,T,B,Q]} {7,S}
7   O   u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.347943,-3.18553,-4.25426,-4.40967,-4.26403,-4.12938,-5.0903],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (91.9206,'kcal/mol','+|-',4.17612),
        S298 = (0.0659441,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 612,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54829,-2.87611,-3.41258,-3.476,-3.17493,-2.94622,-3.22269],'cal/mol/K','+|-',[4.80117,7.1933,7.13257,5.96815,3.73779,3.04754,2.77046]),
        H298 = (84.2638,'kcal/mol','+|-',6.89386),
        S298 = (0.381181,'cal/mol/K','+|-',2.54006),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 613,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D} {6,[S,D,T,B,Q]}
4   C   u0 {2,S} {5,S}
5   R!H u0 {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.38439,-7.5045,-8.08597,-7.41213,-5.36216,-4.03249,-2.60585],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.883,'kcal/mol','+|-',4.17612),
        S298 = (0.822261,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=CO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 614,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.95185,-3.24194,-3.50959,-3.13657,-2.17178,-1.53016,-2.30846],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (87.5338,'kcal/mol','+|-',4.17612),
        S298 = (-0.626466,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])CCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 615,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.252423,-0.878422,-1.50441,-2.03731,-2.7013,-3.07814,-3.83512],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (83.1262,'kcal/mol','+|-',1.69706),
        S298 = (0.607808,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 616,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C",
    group = 
"""
1 * O   u1 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   C   u0 {2,S} {5,D}
5   R!H u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.43641,-2.65754,-3.19974,-3.38395,-3.65031,-4.00806,-5.13121],'cal/mol/K','+|-',[4.8159,6.31469,6.14049,4.75816,2.3492,2.51943,3.5477]),
        H298 = (92.6833,'kcal/mol','+|-',6.39863),
        S298 = (3.98858,'cal/mol/K','+|-',2.19395),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 617,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C_5R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D}
4   C u0 {2,S} {5,D}
5   C u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.16715,-5.18822,-5.66701,-5.20709,-4.05163,-3.47224,-3.9356],'cal/mol/K','+|-',[4.10623,3.50131,3.32235,3.26469,3.24739,3.30766,3.33571]),
        H298 = (95.4487,'kcal/mol','+|-',7.65391),
        S298 = (4.09088,'cal/mol/K','+|-',3.29139),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 618,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D}
4   C   u0 {2,S} {5,D}
5   C   u0 {4,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 619,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C_N-5R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D}
4   C u0 {2,S} {5,D}
5   O u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0518143,-0.632988,-1.22593,-1.92543,-3.32925,-4.43671,-6.08769],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (91.77,'kcal/mol','+|-',1.69706),
        S298 = (3.90674,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 620,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_3C-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D}
4   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.31601,-11.302,-13.5755,-13.4851,-11.3531,-10.2008,-5.49906],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (95.2985,'kcal/mol','+|-',4.17612),
        S298 = (9.60231,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC([O])=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 621,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_N-3C-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.83176,-4.98336,-4.87518,-3.82595,-1.76276,-0.191705,0.132665],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (89.5979,'kcal/mol','+|-',4.17612),
        S298 = (19.3209,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=COC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 622,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C u0 {2,D}
4   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.96362,-5.21844,-4.9504,-4.15826,-3.01453,-2.17756,-2.19083],'cal/mol/K','+|-',[4.82583,6.52426,7.13082,6.95829,5.47773,4.40205,2.6026]),
        H298 = (65.1119,'kcal/mol','+|-',9.14659),
        S298 = (-0.0139146,'cal/mol/K','+|-',11.6644),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 623,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C u0 {2,D}
4   O u0 {2,S} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.80942,-4.93994,-4.6222,-3.86403,-2.8884,-2.14649,-2.27664],'cal/mol/K','+|-',[5.31326,7.12138,7.75646,7.5999,6.07149,4.90173,2.84241]),
        H298 = (66.2426,'kcal/mol','+|-',8.10187),
        S298 = (-0.352868,'cal/mol/K','+|-',12.9019),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 624,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   u0 r0 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C   u0 {2,D}
4   O   u0 {2,S} {5,S}
5   C   u0 {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.99011,-4.17081,-3.7318,-3.0041,-2.47329,-2.02113,-2.06409],'cal/mol/K','+|-',[9.41993,13.3493,14.5144,14.1713,11.3579,9.04307,4.77888]),
        H298 = (67.8918,'kcal/mol','+|-',11.4623),
        S298 = (-1.27677,'cal/mol/K','+|-',22.6583),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 625,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   u0 r0 {1,[S,D,T,B,Q]} {3,D} {4,S}
3   C   u0 {2,D} {8,[S,D,T,B,Q]}
4   O   u0 {2,S} {5,S}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.12729,-8.75617,-8.74013,-7.88806,-6.33012,-5.01648,-3.33086],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (71.365,'kcal/mol','+|-',4.17612),
        S298 = (6.65576,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 626,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H",
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
        Cpdata = ([-5.551,-6.78921,-6.69621,-5.94252,-4.39411,-3.34267,-3.10029],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (68.6514,'kcal/mol','+|-',4.17612),
        S298 = (5.00678,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 627,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * O u1 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D}
4   O u0 {2,S} {5,S}
5   C u0 {4,S} {6,[B,D,T,Q]}
6   C u0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.75793,-4.78444,-4.47559,-3.68472,-2.55066,-1.67377,-2.07737],'cal/mol/K','+|-',[3.26562,3.16964,3.20359,3.27963,3.33041,3.27015,3.17598]),
        H298 = (63.389,'kcal/mol','+|-',5.91744),
        S298 = (-2.10879,'cal/mol/K','+|-',3.16881),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 628,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D}
4   O   u0 r0 {2,S} {5,S}
5   C   u0 r0 {4,S} {6,D}
6   C   u0 r0 {5,D} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.46978,-4.7081,-4.6569,-3.99211,-2.92005,-1.96827,-2.18156],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (63.2586,'kcal/mol','+|-',4.17612),
        S298 = (-2.18071,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 629,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.17969,-2.62106,-4.04293,-4.59928,-4.96457,-4.96274,-4.84096],'cal/mol/K','+|-',[6.64572,8.26033,8.07714,6.3204,2.75599,2.84055,5.4145]),
        H298 = (85.8445,'kcal/mol','+|-',9.2862),
        S298 = (2.21953,'cal/mol/K','+|-',6.15719),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 630,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.123067,-2.09048,-3.39127,-4.01559,-4.65342,-4.76807,-4.39932],'cal/mol/K','+|-',[6.79391,8.02037,7.32736,5.36578,1.94943,2.70272,4.88575]),
        H298 = (85.1866,'kcal/mol','+|-',7.29118),
        S298 = (1.64089,'cal/mol/K','+|-',5.17132),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 631,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_4C-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3578,0.138224,-1.06744,-2.20189,-4.35302,-5.68202,-6.28545],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (85.1246,'kcal/mol','+|-',1.69706),
        S298 = (3.10382,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 632,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.351831,-2.94768,-4.28505,-4.71317,-4.76896,-4.41655,-3.67388],'cal/mol/K','+|-',[7.92127,8.91705,7.92542,5.70114,2.26282,2.85067,4.95838]),
        H298 = (85.2239,'kcal/mol','+|-',9.93965),
        S298 = (1.07823,'cal/mol/K','+|-',5.72299),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 633,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.04915,-6.25235,-7.27894,-6.80374,-5.11193,-3.69015,-2.21943],'cal/mol/K','+|-',[5.06444,4.6124,4.38352,3.94114,3.20741,3.23232,5.01629]),
        H298 = (87.5511,'kcal/mol','+|-',10.1697),
        S298 = (-1.05945,'cal/mol/K','+|-',2.75775),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 634,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-3C-R_Ext-4C-R_Sp-7R!H-4C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {6,S}
4   C   ux r0 {3,[S,D,T,B,Q]} {5,S} {7,S}
5   C   ux {4,S}
6   R!H u0 {3,S}
7   O   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.80253,-5.41165,-6.78732,-6.54543,-5.24384,-4.10065,-3.37032],'cal/mol/K','+|-',[3.2659,4.71727,5.41263,5.1118,4.10171,3.67673,3.89918]),
        H298 = (89.9991,'kcal/mol','+|-',7.16884),
        S298 = (-1.28334,'cal/mol/K','+|-',3.26711),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 635,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-3C-R_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {4,[S,D,T,B,Q]} {6,S}
4   C   ux r0 {3,[S,D,T,B,Q]} {5,S} {7,S} {8,[S,D,T,B,Q]}
5   C   ux {4,S}
6   R!H u0 r0 {3,S}
7   O   ux {4,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.51397,-4.17408,-5.23424,-5.12546,-4.32026,-3.43748,-4.17683],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (88.5624,'kcal/mol','+|-',4.17612),
        S298 = (-1.5736,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=C[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 636,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-3C-R_Ext-4C-R_N-Sp-7R!H-4C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {4,S} {6,[S,D,T,B,Q]}
4   C   u0 r0 {3,S} {5,[S,D,T,B,Q]} {7,[B,D,T,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
7   O   u0 r0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5424,-7.93374,-8.26219,-7.32036,-4.84811,-2.86917,0.0823629],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (82.6551,'kcal/mol','+|-',4.17612),
        S298 = (-0.611679,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 637,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-5C-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {4,S}
4   C u0 r0 {3,S} {5,S}
5   C u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   C u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.12933,-4.41855,-5.23489,-5.22557,-4.66249,-4.04479,-2.9497],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (92.247,'kcal/mol','+|-',4.17612),
        S298 = (0.159536,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=CCC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 638,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-5C-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D}
3   C                      u0 r0 {2,D} {4,S}
4   C                      u0 r0 {3,S} {5,S}
5   C                      u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59595,1.60628,-0.312451,-1.99952,-4.39997,-5.43692,-5.70889],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (82.9113,'kcal/mol','+|-',1.69706),
        S298 = (4.01092,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 639,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D}
3   C                      u0 {2,D} {4,S}
4   C                      u0 {3,S} {5,S}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 {4,S}
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
    index = 640,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D}
3   C                      u0 {2,D} {4,S}
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
    index = 641,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.824179,0.476104,-0.129663,-0.648863,-1.39846,-2.1015,-3.66482],'cal/mol/K','+|-',[3.32028,3.78989,3.94406,4.11051,3.89027,3.13122,3.30453]),
        H298 = (98.6471,'kcal/mol','+|-',6.71453),
        S298 = (-2.22318,'cal/mol/K','+|-',6.84235),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 642,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.990115,0.65426,0.0440304,-0.480836,-1.24105,-1.95915,-3.56267],'cal/mol/K','+|-',[3.01291,3.49546,3.69167,3.90257,3.69986,2.9102,3.25181]),
        H298 = (98.3769,'kcal/mol','+|-',5.67642),
        S298 = (-2.28117,'cal/mol/K','+|-',7.01802),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 643,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.11602,0.698463,0.0581016,-0.467966,-1.17198,-1.8713,-3.57885],'cal/mol/K','+|-',[3.39236,4.05597,4.30275,4.55611,4.31553,3.38212,3.80533]),
        H298 = (99.5598,'kcal/mol','+|-',4.9608),
        S298 = (-2.39895,'cal/mol/K','+|-',8.21059),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 644,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.91956,1.68036,0.850499,0.23772,-0.395165,-1.53119,-4.01682],'cal/mol/K','+|-',[6.33764,7.75218,8.26749,8.65659,7.8889,6.27173,7.56046]),
        H298 = (102.369,'kcal/mol','+|-',10.4302),
        S298 = (-5.26494,'cal/mol/K','+|-',14.1727),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 645,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-6O-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H u0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.55212,5.56948,4.21265,2.87275,0.671258,-1.65745,-4.02074],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (108.541,'kcal/mol','+|-',4.17612),
        S298 = (-6.62751,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 646,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_5R!H->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   O   u0 {2,D}
4   R!H u0 {2,S} {5,S}
5   C   u0 {4,S} {6,[S,D,T,B,Q]}
6   O   u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.372526,-1.3295,-2.3547,-3.06366,-3.21363,-3.43042,-6.12335],'cal/mol/K','+|-',[4.13079,4.91492,5.95684,6.47084,5.48154,4.7402,7.73632]),
        H298 = (99.4664,'kcal/mol','+|-',9.41291),
        S298 = (-0.368454,'cal/mol/K','+|-',10.6807),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 647,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_5R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   O u0 r0 {2,D}
4   C u0 {2,S} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   O u0 {5,[S,D,T,B,Q]}
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
    index = 648,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_5R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   O u0 r0 {2,D}
4   O u0 {2,S} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   O u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.567117,0.000744342,-0.569909,-1.06767,-1.63062,-2.18194,-3.62708],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (96.8749,'kcal/mol','+|-',4.17612),
        S298 = (-3.97534,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OC(=O)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 649,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_N-5R!H->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.87119,3.81095,3.89875,4.20545,4.17534,2.39354,0.200152],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (102.004,'kcal/mol','+|-',4.17612),
        S298 = (-13.6953,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 650,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.823823,0.341411,-0.230043,-0.724578,-1.45446,-1.99497,-3.41959],'cal/mol/K','+|-',[1.81309,1.73196,2.02153,2.34645,2.53749,2.19328,1.7334]),
        H298 = (99.1143,'kcal/mol','+|-',2.93847),
        S298 = (-1.35677,'cal/mol/K','+|-',3.53534),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 651,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_4R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O ux {2,D}
4   C ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.436308,0.133181,0.123315,0.0745543,0.101627,-0.0705836,-1.98517],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (94.0954,'kcal/mol','+|-',4.17612),
        S298 = (-4.91505,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)CCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 652,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C",
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
        Cpdata = ([0.949836,0.362234,-0.265379,-0.804492,-1.61007,-2.18741,-3.56303],'cal/mol/K','+|-',[1.66136,1.82622,2.13045,2.42316,2.42903,1.80917,1.4694]),
        H298 = (99.3215,'kcal/mol','+|-',1.83342),
        S298 = (-1.00094,'cal/mol/K','+|-',2.6212),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 653,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C_Ext-6BrCClFINPSSi-R_7R!H->O",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
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
    index = 654,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C_Ext-6BrCClFINPSSi-R_N-7R!H->O",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.1296,0.645748,0.130792,-0.314121,-1.11726,-1.91116,-3.52955],'cal/mol/K','+|-',[1.74106,1.65535,1.64563,1.64412,1.63956,1.65671,1.69661]),
        H298 = (99.1769,'kcal/mol','+|-',2.01503),
        S298 = (-1.54144,'cal/mol/K','+|-',1.7209),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 655,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C_Ext-6BrCClFINPSSi-R_N-7R!H->O_Sp-6BrCClFINPSSi-5R!H",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]} {6,S}
6   C ux {5,S} {7,D}
7   C u0 {6,D}
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
    index = 656,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C_Ext-6BrCClFINPSSi-R_N-7R!H->O_Sp-6BrCClFINPSSi-5R!H_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]} {6,S} {8,[S,D,T,B,Q]}
6   C   ux r0 {5,S} {7,D}
7   C   u0 r0 {6,D}
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
    index = 657,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C_Ext-6BrCClFINPSSi-R_N-7R!H->O_N-Sp-6BrCClFINPSSi-5R!H",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   O u0 r0 {2,D}
4   O u0 {2,S} {5,S}
5   C ux {4,S} {6,D}
6   C u0 {5,D} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.938719,0.489487,0.109227,-0.275131,-1.03709,-1.76251,-3.26629],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (98.9076,'kcal/mol','+|-',1.69706),
        S298 = (-1.85473,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 658,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-4R!H-R",
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
    index = 659,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_N-1R->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   O u0 r0 {2,D}
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
    index = 660,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.162886,-0.9909,-1.7425,-2.2427,-2.90367,-3.43347,-4.31481],'cal/mol/K','+|-',[3.64344,3.9004,3.75922,3.4179,2.84281,2.56256,2.12193]),
        H298 = (106.098,'kcal/mol','+|-',10.4856),
        S298 = (0.286532,'cal/mol/K','+|-',7.48648),
    ),
    shortDesc = """Radical correction fitted to 47 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 661,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.20016,-1.08466,-1.85861,-2.34196,-2.94832,-3.44193,-4.27623],'cal/mol/K','+|-',[3.92133,4.20229,4.04639,3.68472,3.06888,2.75652,2.28133]),
        H298 = (104.357,'kcal/mol','+|-',8.12518),
        S298 = (0.0307864,'cal/mol/K','+|-',8.08705),
    ),
    shortDesc = """Radical correction fitted to 41 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 662,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.961244,0.113399,-0.792467,-1.51992,-2.53981,-3.35941,-4.62837],'cal/mol/K','+|-',[2.85298,3.6713,3.62811,3.23853,2.42886,1.89036,1.60948]),
        H298 = (101.292,'kcal/mol','+|-',7.48514),
        S298 = (0.301891,'cal/mol/K','+|-',8.32277),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 663,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.21508,0.282181,-0.710139,-1.39416,-2.42062,-3.25955,-4.43059],'cal/mol/K','+|-',[3.20989,4.44959,4.47158,3.90611,2.92066,2.2014,1.667]),
        H298 = (102.463,'kcal/mol','+|-',2.12319),
        S298 = (-0.0520655,'cal/mol/K','+|-',9.53287),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 664,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S}
4   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.92607,0.77629,-0.374775,-1.00372,-2.04591,-2.95321,-3.99079],'cal/mol/K','+|-',[2.72644,4.8183,5.35882,4.63617,3.32379,2.60454,1.78771]),
        H298 = (103.041,'kcal/mol','+|-',2.75328),
        S298 = (-0.60421,'cal/mol/K','+|-',14.0527),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 665,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]}
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
    index = 666,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C_Ext-3O-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,S} {4,S}
3   O   u0 {2,S} {6,S}
4   C   u0 {2,S} {5,[S,D,T,B,Q]}
5   C   u0 {4,[S,D,T,B,Q]}
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
    index = 667,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C_Ext-3O-R_6R!H->N",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S} {6,S}
4   C u0 r0 {2,S} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]}
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
    index = 668,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C_Ext-3O-R_N-6R!H->N",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S} {6,S}
4   C u0 {2,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]}
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
    index = 669,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C_Ext-3O-R_N-6R!H->N_Ext-6BrCClFIOPSSi-R_7R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S} {6,S}
4   C u0 r0 {2,S} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]}
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
    index = 670,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C_Ext-3O-R_N-6R!H->N_Ext-6BrCClFIOPSSi-R_N-7R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   O u0 {2,S} {6,S}
4   C u0 r0 {2,S} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]}
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
    index = 671,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,S} {4,S}
3   O                      u0 {2,S}
4   C                      u0 r0 {2,S} {5,[S,D,T,B,Q]}
5   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {4,[S,D,T,B,Q]}
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
    index = 672,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O",
    group = 
"""
1 * C u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.720478,-0.0615467,-0.943435,-1.66577,-2.68128,-3.47266,-4.73653],'cal/mol/K','+|-',[3.57859,4.6623,4.39845,3.87188,3.05284,2.34822,1.85018]),
        H298 = (102.069,'kcal/mol','+|-',2.09421),
        S298 = (0.332035,'cal/mol/K','+|-',6.43098),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 673,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R",
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
        Cpdata = ([1.04339,0.201005,-0.788193,-1.58413,-2.65803,-3.48354,-4.77899],'cal/mol/K','+|-',[3.81009,5.21526,5.00585,4.4357,3.5045,2.6898,2.10191]),
        H298 = (101.991,'kcal/mol','+|-',2.4629),
        S298 = (-0.305976,'cal/mol/K','+|-',6.74196),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 674,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H u0 {4,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.82255,2.3918,1.12052,0.0786665,-1.26868,-2.41198,-4.38082],'cal/mol/K','+|-',[7.89301,11.4494,10.9901,9.2595,6.7338,4.32015,3.33137]),
        H298 = (102.328,'kcal/mol','+|-',5.97806),
        S298 = (-4.85869,'cal/mol/K','+|-',6.02795),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 675,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H u0 r0 {4,[S,D]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.37939,6.28231,4.8418,3.15556,0.833226,-1.37132,-4.7513],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (102,'kcal/mol','+|-',4.17612),
        S298 = (-6.67309,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 676,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_5R!H->O",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   C u0 {2,S} {5,S}
4   C u0 {2,S}
5   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.510482,-0.893113,-2.20709,-3.15016,-4.06619,-4.74813,-5.85335],'cal/mol/K','+|-',[3.61211,3.98349,4.08025,4.16421,3.89949,3.86881,3.5495]),
        H298 = (100.797,'kcal/mol','+|-',6.33611),
        S298 = (-0.890019,'cal/mol/K','+|-',6.15629),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 677,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_5R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {4,S}
3   C   u0 r0 {2,S} {5,S} {6,[S,D,T,B,Q]}
4   C   u0 r0 {2,S}
5   O   u0 r0 {3,S}
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
    index = 678,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_N-5R!H->O",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r0 {1,S} {3,S} {4,S}
3   C u0 {2,S} {5,D}
4   C u0 {2,S}
5   C u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.544896,-0.237667,-0.984121,-1.62283,-2.6505,-3.40632,-4.50852],'cal/mol/K','+|-',[2.01978,2.02197,2.02081,2.02322,2.02336,2.0194,2.00739]),
        H298 = (102.132,'kcal/mol','+|-',2.40783),
        S298 = (1.74873,'cal/mol/K','+|-',2.24576),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 679,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_N-5R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {4,S}
3   C   u0 r0 {2,S} {5,D} {6,[S,D,T,B,Q]}
4   C   u0 r0 {2,S}
5   C   u0 r0 {3,D}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.644593,-0.132567,-0.881839,-1.51477,-2.5421,-3.3076,-4.44767],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.064,'kcal/mol','+|-',1.69706),
        S298 = (2.10988,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 680,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,S}
3   R!H ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.565991,-0.217135,-1.0233,-1.85777,-2.84971,-3.62476,-5.07357],'cal/mol/K','+|-',[2.84596,2.85105,2.63507,2.61067,2.13288,2.0223,2.00878]),
        H298 = (102.398,'kcal/mol','+|-',3.22569),
        S298 = (2.25061,'cal/mol/K','+|-',3.28792),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 681,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,S}
3   R!H ux {2,S} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.565865,-0.322979,-1.16318,-2.07756,-3.06992,-3.85341,-5.2715],'cal/mol/K','+|-',[3.57014,3.49284,3.19233,3.13621,2.5157,2.3695,2.12186]),
        H298 = (102.079,'kcal/mol','+|-',4.27467),
        S298 = (2.43559,'cal/mol/K','+|-',3.81188),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 682,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,S}
3   R!H ux {2,S} {4,S}
4   R!H ux {3,S} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.508707,-0.21567,-1.14324,-1.93767,-3.02618,-3.90701,-5.24281],'cal/mol/K','+|-',[3.99762,3.86886,3.57689,3.40856,2.78523,2.60782,2.3331]),
        H298 = (101.774,'kcal/mol','+|-',3.87928),
        S298 = (1.94661,'cal/mol/K','+|-',3.07396),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 683,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   O   ux {3,S} {5,S}
5   O   u0 {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.54475,0.591804,-0.601484,-1.5964,-2.94871,-4.00082,-5.39597],'cal/mol/K','+|-',[3.11998,4.28415,4.71681,4.88849,4.06878,3.72712,3.13888]),
        H298 = (101.776,'kcal/mol','+|-',5.37138),
        S298 = (1.42144,'cal/mol/K','+|-',3.51203),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 684,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   O   ux {3,S} {5,S}
5   O   u0 r0 {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
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
    index = 685,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_3R!H->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,S}
3   C   ux {2,S} {4,S}
4   R!H ux {3,S} {5,S}
5   C   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21387,-1.5129,-2.01507,-2.48956,-3.11489,-3.6551,-4.87205],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.296,'kcal/mol','+|-',4.17612),
        S298 = (2.35098,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]CCOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 686,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_N-3R!H->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,S}
3   O   ux {2,S} {4,S}
4   R!H ux {3,S} {5,S}
5   C   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39488,-1.7446,-2.16755,-2.58023,-3.20861,-3.83056,-5.07751],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (102.24,'kcal/mol','+|-',4.17612),
        S298 = (3.38031,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 687,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   R!H u0 r0 {2,S} {4,[D,T]}
4   R!H ux {3,[D,T]} {5,S}
5   R!H u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.880235,-0.913179,-1.27286,-2.84693,-3.31052,-3.55865,-5.42933],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (104.837,'kcal/mol','+|-',4.17612),
        S298 = (5.12499,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]CC#CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 688,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.844975,0.350325,-0.412686,-1.16346,-2.23936,-3.04307,-4.26318],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (102.768,'kcal/mol','+|-',1.69706),
        S298 = (1.2801,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 689,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_N-Sp-3R!H-2CN",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,T}
3   R!H ux {2,T}
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
    index = 690,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23252,-2.1496,-2.80629,-3.07265,-3.31144,-3.51529,-3.96321],'cal/mol/K','+|-',[3.69011,3.56529,3.55207,3.5822,3.52604,3.47775,2.73448]),
        H298 = (106.946,'kcal/mol','+|-',4.14963),
        S298 = (-0.210196,'cal/mol/K','+|-',8.11268),
    ),
    shortDesc = """Radical correction fitted to 21 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 691,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.836244,-1.2789,-1.61918,-1.74357,-1.96817,-2.10798,-2.79602],'cal/mol/K','+|-',[4.54609,2.97774,2.35032,2.42669,2.88855,3.1094,2.90386]),
        H298 = (106.88,'kcal/mol','+|-',6.37432),
        S298 = (-0.811835,'cal/mol/K','+|-',13.6733),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 692,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-4R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   u0 r0 {1,S} {3,[S,T,Q,B]}
3   C   u0 {2,[S,T,Q,B]} {4,D}
4   C   u0 {3,D} {5,[S,D,T,B,Q]}
5   R!H u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23964,-1.30147,-1.22923,-1.093,-0.968966,-0.813291,-1.60746],'cal/mol/K','+|-',[8.26771,4.16664,2.46083,2.39422,2.49788,2.51659,2.58777]),
        H298 = (105.715,'kcal/mol','+|-',10.13),
        S298 = (1.87671,'cal/mol/K','+|-',27.1551),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 693,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-4R!H-R_Ext-2CN-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   u0 {2,[S,T,Q,B]} {4,D}
4   C   u0 {3,D} {5,[S,D,T,B,Q]}
5   R!H u0 r0 {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 694,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2CN-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.437439,-0.504991,-1.28775,-1.48477,-1.7784,-2.21257,-3.0148],'cal/mol/K','+|-',[3.53563,3.8127,3.47539,2.99488,2.79149,2.62238,2.86739]),
        H298 = (110.639,'kcal/mol','+|-',6.47426),
        S298 = (-4.55887,'cal/mol/K','+|-',2.91307),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 695,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2CN-R_Ext-2CN-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   u0 r0 {2,S} {4,D}
4   R!H u0 r0 {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.68908,0.501097,-0.445348,-1.07936,-1.7444,-2.32211,-3.73475],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (108.876,'kcal/mol','+|-',4.17612),
        S298 = (-4.4,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C(C)([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 696,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2CN-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,D} {6,[S,D,T,B,Q]}
4   C   ux {3,D}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
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
    index = 697,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36461,-2.43983,-3.202,-3.51568,-3.75919,-3.98439,-4.35228],'cal/mol/K','+|-',[3.59829,3.73506,3.67818,3.60948,3.42108,3.24362,2.40193]),
        H298 = (106.965,'kcal/mol','+|-',3.81635),
        S298 = (-0.0096494,'cal/mol/K','+|-',5.99074),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 698,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing",
    group = 
"""
1 * O     u1 {2,S}
2   C     ux r0 {1,S} {3,S}
3   C     ux r1 {2,S} {4,[S,T,Q,B]}
4   [C,O] ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.705254,-2.36212,-3.81336,-4.45594,-4.84888,-5.2367,-5.45579],'cal/mol/K','+|-',[2.70526,2.65951,2.58246,2.99416,3.38927,3.33524,3.09112]),
        H298 = (108.82,'kcal/mol','+|-',3.43428),
        S298 = (0.118708,'cal/mol/K','+|-',5.62931),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 699,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R",
    group = 
"""
1 * O     u1 {2,S}
2   C     ux r0 {1,S} {3,S}
3   C     ux r1 {2,S} {4,[S,T,Q,B]} {5,S}
4   [C,O] ux {3,[S,T,Q,B]} {7,S}
5   [C,O] u0 {3,S} {6,S}
6   [C,O] ux {5,S}
7   [C,O] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.262176,-1.6672,-3.40724,-4.26019,-4.94591,-5.56832,-5.04344],'cal/mol/K','+|-',[3.50605,3.36313,3.80672,4.79777,4.49906,3.98087,3.27243]),
        H298 = (109.663,'kcal/mol','+|-',6.81533),
        S298 = (-1.94388,'cal/mol/K','+|-',7.64097),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 700,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1 * O     u1 {2,S}
2   C     ux r0 {1,S} {3,S}
3   C     ux r1 {2,S} {4,[S,T,Q,B]} {5,S} {8,[S,D,T,B,Q]}
4   [C,O] ux r1 {3,[S,T,Q,B]} {7,S}
5   [C,O] u0 r1 {3,S} {6,S}
6   [C,O] ux r1 {5,S}
7   [C,O] u0 r1 {4,S}
8   R!H   ux {3,[S,D,T,B,Q]}
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
    index = 701,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 r0 {1,S} {3,S}
3   C     u0 r1 {2,S} {4,S}
4   [C,O] u0 r1 {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H   ux {4,[S,D,T,B,Q]}
6   R!H   ux {4,[S,D,T,B,Q]}
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
    index = 702,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53328,-2.45971,-3.0456,-3.27515,-3.48043,-3.66404,-4.06998],'cal/mol/K','+|-',[3.91624,4.15869,4.03775,3.80408,3.43902,3.13467,2.12243]),
        H298 = (106.603,'kcal/mol','+|-',3.70241),
        S298 = (-0.042485,'cal/mol/K','+|-',6.38173),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 703,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.28093,-2.32075,-3.00706,-3.28924,-3.52045,-3.73345,-4.20143],'cal/mol/K','+|-',[3.89622,4.01788,3.98039,3.85661,3.6973,3.49401,2.37438]),
        H298 = (107.088,'kcal/mol','+|-',3.84507),
        S298 = (-0.12434,'cal/mol/K','+|-',6.89855),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 704,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5379,-2.02349,-2.46776,-2.42754,-2.0767,-2.06245,-2.92394],'cal/mol/K','+|-',[4.8344,5.40133,5.52133,5.52802,4.92393,4.366,3.15064]),
        H298 = (105.29,'kcal/mol','+|-',7.00768),
        S298 = (-3.96328,'cal/mol/K','+|-',7.55035),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 705,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.37349,-2.94525,-3.42462,-3.3954,-2.94712,-2.88735,-3.43383],'cal/mol/K','+|-',[4.17934,4.74734,4.7875,4.74585,4.16544,3.3806,2.79583]),
        H298 = (106.622,'kcal/mol','+|-',5.3084),
        S298 = (-2.68165,'cal/mol/K','+|-',6.72729),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 706,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_Ext-2CN-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,S} {7,[S,D,T,B,Q]}
3   R!H ux r0 {2,S} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   u0 r0 {4,[S,D,T,B,Q]}
6   O   ux {4,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.561205,-0.758197,-1.46141,-1.51091,-1.39274,-1.93466,-3.02646],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (106.648,'kcal/mol','+|-',4.17612),
        S298 = (-4.47588,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 707,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_3R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.76623,-3.42212,-3.32332,-3.19719,-2.7975,-2.64975,-3.23374],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (105.499,'kcal/mol','+|-',4.17612),
        S298 = (-4.47396,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC(=O)CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 708,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_N-3R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]}
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
    index = 709,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,[S,T,Q,B]}
3   R!H u0 r0 {2,[S,T,Q,B]} {4,S}
4   C   u0 r0 {3,S} {5,[S,D]} {6,[S,D]}
5   O   ux {4,[S,D]}
6   O   u0 r0 {4,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.968866,0.741762,0.402841,0.476043,0.534574,0.412253,-1.39425],'cal/mol/K','+|-',[2.23607,2.23607,2.23607,2.23607,2.23607,2.23607,2.23607]),
        H298 = (101.294,'kcal/mol','+|-',4.17612),
        S298 = (-7.80818,'cal/mol/K','+|-',2.23607),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(O)(O)OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 710,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   R!H ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.328727,-0.999969,-1.56298,-1.95559,-2.3922,-2.88674,-4.0924],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (105.37,'kcal/mol','+|-',1.69706),
        S298 = (-1.66614,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(C[O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 711,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   R!H u0 r0 {2,S} {4,S}
4   C   u0 {3,S} {5,D}
5   O   u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.69467,-4.37033,-5.0875,-5.19507,-5.06077,-4.94275,-4.69753],'cal/mol/K','+|-',[4.57162,2.26884,2.30314,2.91017,3.66266,3.51639,2.21597]),
        H298 = (108.504,'kcal/mol','+|-',2.93881),
        S298 = (2.8966,'cal/mol/K','+|-',3.251),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 712,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C_Ext-2CN-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {6,[S,D,T,B,Q]}
3   R!H u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,D}
5   O   u0 r0 {4,D}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 713,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-4R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.137715,-1.16936,-2.0801,-2.73961,-3.69926,-4.28429,-4.78183],'cal/mol/K','+|-',[3.84909,2.80622,2.11532,2.00244,2.32352,2.65951,2.72918]),
        H298 = (107.123,'kcal/mol','+|-',3.3829),
        S298 = (0.696776,'cal/mol/K','+|-',4.38783),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 714,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,S}
6   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.30044,-1.86532,-2.32366,-2.70465,-3.28112,-3.66451,-4.12528],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (106.28,'kcal/mol','+|-',1.69706),
        S298 = (-0.684031,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCOOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 715,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 {2,S}
2   C                      ux r0 {1,S} {3,[S,T,Q,B]}
3   O                      ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O                      ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   C                      ux {4,[S,D,T,B,Q]} {6,S}
6   [Cl,O,Si,S,N,P,F,I,Br] u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.02501,-0.473403,-1.83654,-2.77456,-4.1174,-4.90407,-5.43838],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (107.966,'kcal/mol','+|-',1.69706),
        S298 = (2.07758,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]COOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 716,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_3R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]}
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
    index = 717,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_N-3R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux r0 {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]}
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
    index = 718,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R",
    group = 
"""
1 * C   u1 {2,D}
2   C   ux r0 {1,D} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0248651,-0.518638,-1.15762,-1.74274,-2.67878,-3.39084,-4.50916],'cal/mol/K','+|-',[2.19786,2.0093,1.80338,1.69848,1.73543,1.80954,1.59012]),
        H298 = (113.445,'kcal/mol','+|-',5.23964),
        S298 = (1.57473,'cal/mol/K','+|-',2.00297),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 719,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_3R!H->O",
    group = 
"""
1 * C u1 {2,D}
2   C ux r0 {1,D} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.269782,-0.29026,-0.986482,-1.63421,-2.67892,-3.43794,-4.539],'cal/mol/K','+|-',[2.73517,2.47992,2.25218,2.161,2.25673,2.3509,2.0286]),
        H298 = (114.97,'kcal/mol','+|-',4.13094),
        S298 = (1.35548,'cal/mol/K','+|-',2.40142),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 720,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_3R!H->O_Ext-2CN-R",
    group = 
"""
1 * C   u1 {2,D}
2   C   u0 r0 {1,D} {3,S} {4,S}
3   O   u0 {2,S}
4   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00639429,-0.907736,-1.7603,-2.40829,-3.39662,-4.08074,-4.98774],'cal/mol/K','+|-',[3.47893,3.38335,2.62992,2.39241,2.94025,3.40927,3.02041]),
        H298 = (116.686,'kcal/mol','+|-',5.57882),
        S298 = (2.24526,'cal/mol/K','+|-',2.69894),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 721,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_3R!H->O_Ext-2CN-R_Ext-3O-R",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   u0 r0 {1,D} {3,S} {4,S}
3   O   u0 r0 {2,S} {5,[S,D,T,B,Q]}
4   R!H u0 r0 {2,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.517044,-0.424011,-1.53878,-2.42783,-3.74249,-4.57184,-5.36074],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (116.224,'kcal/mol','+|-',1.69706),
        S298 = (2.4984,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 722,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_3R!H->O_Ext-3O-R",
    group = 
"""
1 * C   u1 {2,D}
2   C   ux r0 {1,D} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.47632,0.698226,-0.241394,-1.04979,-2.33091,-3.24564,-4.47212],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (114.461,'kcal/mol','+|-',1.69706),
        S298 = (0.73245,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=COCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 723,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_N-3R!H->O",
    group = 
"""
1 * C u1 {2,D}
2   C u0 r0 {1,D} {3,S}
3   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.391494,-0.906882,-1.44855,-1.92724,-2.67855,-3.31078,-4.45842],'cal/mol/K','+|-',[2.00312,2.01569,2.01888,2.01996,2.00798,2.01147,2.06563]),
        H298 = (111.031,'kcal/mol','+|-',2.40087),
        S298 = (1.94746,'cal/mol/K','+|-',2.24649),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 724,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_N-3R!H->O_Ext-3C-R_4R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C u0 r0 {1,D} {3,S}
3   C u0 r0 {2,S} {4,[S,D]}
4   O u0 r0 {3,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.431025,-0.995626,-1.54594,-2.02739,-2.74178,-3.38663,-4.64106],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (111.054,'kcal/mol','+|-',1.69706),
        S298 = (2.30918,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=CC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 725,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_N-3R!H->O_Ext-3C-R_N-4R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C u0 r0 {1,D} {3,S}
3   C u0 r0 {2,S} {4,[S,D]}
4   C u0 r0 {3,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.351963,-0.818138,-1.35116,-1.82709,-2.61533,-3.23493,-4.27579],'cal/mol/K','+|-',[1.41421,1.41421,1.41421,1.41421,1.41421,1.41421,1.41421]),
        H298 = (111.008,'kcal/mol','+|-',1.69706),
        S298 = (1.58574,'cal/mol/K','+|-',1.41421),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_2R!H-inRing
            L4: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H
                L5: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing
                    L6: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_1R->C
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_1R->C_Ext-4R!H-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_1R->C_1C-inRing
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_1R->C_N-1C-inRing
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_1R->C_N-1C-inRing_Ext-6R!H-R_Ext-6R!H-R
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-2R!H-R_N-1R->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_Sp-6R!H-1R
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_Sp-6R!H-1R_6R!H->O
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_Sp-6R!H-1R_6R!H->O_Ext-6O-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_Sp-6R!H-1R_6R!H->O_Ext-1R-R
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_Sp-6R!H-1R_N-6R!H->O
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_N-Sp-6R!H-1R
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_5C-inRing_Ext-1R-R_N-Sp-6R!H-1R_Ext-4R!H-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing_Ext-4R!H-R
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing_Ext-4R!H-R_Ext-6R!H-R_Ext-1R-R
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing_Ext-4R!H-R_Ext-5C-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing_1R-inRing
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_Sp-5C=4R!H_N-5C-inRing_N-1R-inRing
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_1R->C
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_1R->C_Sp-6R!H-5C
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_1R->C_N-Sp-6R!H-5C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_N-1R->C
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_N-1R->C_6R!H->C
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_Int-5C-2R!H_N-1R->C_N-6R!H->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Int-6R!H-4R!H
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Int-6R!H-4R!H_Ext-4R!H-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing
                                                L13: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R
                                                    L14: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R_Ext-1C-R
                                                        L15: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R_Ext-1C-R_Ext-5C-R
                                                            L16: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R_Ext-1C-R_Ext-5C-R_6R!H->O
                                                            L16: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R_Ext-1C-R_Ext-5C-R_N-6R!H->O
                                                    L14: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-4R!H-R_Ext-5C-R
                                                L13: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C
                                                    L14: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H
                                                        L15: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H_Ext-7R!H-R
                                                        L15: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H_6R!H->C
                                                        L15: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H_N-6R!H->C
                                                    L14: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Int-5C-1C_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H-7R!H
                                                L13: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-2R!H-R
                                                L13: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-3R!H-R
                                                    L14: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-3R!H-R_Ext-5C-R
                                                    L14: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-3R!H-R_Ext-1C-R
                                                L13: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_1C-inRing_Ext-1C-R
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_N-1C-inRing
                                                L13: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_N-1C-inRing_Ext-2R!H-R
                                                L13: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_Sp-4R!H-3R!H_N-1C-inRing_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_Sp-6R!H-5C_N-Sp-4R!H-3R!H
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_N-Sp-6R!H-5C
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_N-Sp-6R!H-5C_Ext-2R!H-R
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_N-Sp-6R!H-5C_Ext-2R!H-R_Ext-1C-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_1R->C_N-Sp-6R!H-5C_Ext-1C-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-5C-R_N-1R->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-3R!H-R_1R->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_Ext-3R!H-R_N-1R->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_4R!H->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_4R!H->C_1R-inRing
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_4R!H->C_N-1R-inRing
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_5R!H->C_N-Sp-5C=4R!H_N-4R!H->C
                    L6: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_1R->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_1R->C_Int-5BrClFINOPSSi-2R!H
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_1R->C_1C-inRing
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_1R->C_N-1C-inRing
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_Ext-4R!H-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_Ext-3R!H-R_6R!H-inRing
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_Ext-3R!H-R_N-6R!H-inRing
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_4R!H->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-5R!H->C_N-1R->C_N-4R!H->C
                L5: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing
                    L6: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C_Ext-1R-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C_Ext-1R-R_Ext-4C-R_Int-6R!H-5R!H
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C_Ext-1R-R_5R!H->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C_Ext-1R-R_N-5R!H->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_3R!H->C_Ext-3C-R
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_N-3R!H->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_N-3R!H->C_Ext-4C-R_Int-5R!H-1R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_N-3R!H->C_Ext-4C-R_5R!H->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_N-3R!H->C_Ext-4C-R_5R!H->C_Ext-4C-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_4R!H->C_N-3R!H->C_Ext-4C-R_N-5R!H->C
                    L6: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_Ext-1R-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_3R!H->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-2R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_N-3R!H->C
            L4: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H
                L5: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C
                    L6: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_Ext-4R!H-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_Ext-4R!H-R_Ext-1C-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_Ext-4R!H-R_Ext-2R!H-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_3R!H->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_3R!H->C_Ext-3C-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-2R!H-R_N-3R!H->C
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R_2R!H->O
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R_N-2R!H->O
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_2R!H->C
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Int-3R!H-1C_N-2R!H->C
                    L6: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Int-5R!H-3R!H
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Int-5R!H-3R!H_5R!H->C
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Int-5R!H-3R!H_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-1C-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-1C-R_4C-inRing
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-1C-R_N-4C-inRing
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_3R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R!H->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_N-4R!H->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_2R!H->O_Ext-1C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1C-R
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Int-5R!H-2C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_5R!H->O
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-1C-R_Ext-1C-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_5R!H->O_Ext-2C-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_6R!H->O
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_6R!H->O_Ext-1C-R
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_6R!H->O_Ext-1C-R_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_Ext-6BrCClFINPSSi-R_Ext-3C-R
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_Ext-3C-R
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_Ext-1C-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_Sp-4R!H-3C
                                                L13: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_Sp-4R!H-3C_Ext-2C-R
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_3R!H->C_Ext-5BrCClFINPSSi-R_N-6R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=4R!H_N-Sp-4R!H-3C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Ext-1C-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Ext-1C-R_6R!H->C
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Ext-1C-R_6R!H->C_Ext-2C-R
                                                L13: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Ext-1C-R_6R!H->C_Ext-2C-R_Ext-7R!H-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Ext-1C-R_N-6R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_1C-inRing_N-2R!H->O_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_N-5R!H->O_N-3R!H->C_Int-5BrCClFINPSSi-1C_Ext-5BrCClFINPSSi-R_Ext-5BrCClFINPSSi-R
                    L6: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C_3R!H-inRing
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C_3R!H-inRing_Int-5C-2R!H
                                            L12: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C_3R!H-inRing_Int-5C-2R!H_Ext-1C-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C_3R!H-inRing_Ext-1C-R
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_5R!H->C_N-3R!H-inRing
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-3R!H-R_N-5R!H->C_Ext-1C-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3R!H-R_3R!H->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3R!H-R_N-3R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_Ext-3R!H-R_N-3R!H->C_Ext-2R!H-R
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_4R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_4R!H->C_Ext-2R!H-R
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_4R!H->C_Ext-2R!H-R_5R!H->C
                                        L11: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_4R!H->C_Ext-2R!H-R_N-5R!H->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_N-4R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_6R!H->C
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_3R!H->O_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-6R!H->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_N-3R!H->O
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_N-3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_N-3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Int-4R!H-2R!H_N-3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-2R!H-R
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-6R!H-3R!H
                                    L10: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-2R!H-R
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-6R!H-3R!H
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-5R!H-R_N-6R!H->C
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-3R!H_Ext-5R!H-R_N-6R!H->C_Ext-2R!H-R
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-3R!H-R
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2R!H-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_4R!H->O
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H->O
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H->O_Sp-6R!H=3R!H
                                L9: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_N-1C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H->O_N-Sp-6R!H=3R!H
                L5: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C
                    L6: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_Int-4R!H-2R!H
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_Int-4R!H-2R!H_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_Int-4R!H-2R!H_Ext-3R!H-R_Ext-2R!H-R
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_Int-4R!H-2R!H_Ext-2R!H-R
                    L6: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_4R!H->O
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_5R!H->C
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_5R!H->C_Ext-2R!H-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_N-5R!H->C
                    L6: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2R!H-R_Ext-4BrCClFINPSSi-R_Ext-5R!H-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2R!H-R_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R
                            L8: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-2R!H-R_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-2R!H-R
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O_3R!H->C
                        L7: RJ1_Ext-1R-R_2R!H-inRing_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_Ext-3R!H-R_N-4R!H->O_N-3R!H->C
        L3: RJ1_Ext-1R-R_N-2R!H-inRing
            L4: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O
                L5: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C
                    L6: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C_3R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C_3R!H->C_Ext-3C-R_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-2O-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C_N-3R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_Sp-3R!H=1C_N-3R!H->C_Ext-2O-R_Ext-4R!H-R_Ext-4R!H-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-2O-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-2O-R_Ext-6R!H-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-2O-R_Ext-5C-R
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-2O-R_Ext-5C-R_7R!H->C
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-2O-R_Ext-5C-R_N-7R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-4R!H-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_6R!H->O
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_6R!H->O_4R!H->C
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_6R!H->O_N-4R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-6R!H->O
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-6R!H->O_4R!H->C
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-4R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_Ext-3R!H-R_N-5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-2O-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-2O-R_Ext-4C-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-1C-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-1C-R_Ext-5R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-4C-R_Ext-4C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_6R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-6R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R_Ext-5R!H-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R_Ext-5R!H-R_6R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R_Ext-5R!H-R_N-6R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R_5R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-3R!H-R_N-5R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Sp-2O-1C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Sp-2O-1C_Ext-1C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_N-Sp-2O-1C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_Ext-1C-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_Ext-1C-R_Ext-4R!H-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_Ext-1C-R_Ext-4R!H-R_Sp-6R!H-4R!H
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_Ext-1C-R_Ext-4R!H-R_N-Sp-6R!H-4R!H
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-2O-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-2O-R_Ext-4C-R_Ext-6R!H-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_4R!H->C_Ext-2O-R_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-2O-1C_N-4R!H->C_Ext-4O-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-4R!H-R_Sp-5R!H=4R!H
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-4R!H-R_N-Sp-5R!H=4R!H
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-2O-1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-4R!H-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-2O-R_Ext-4R!H-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-2O-R_Ext-4R!H-R_Sp-5R!H-4R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-2O-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-1C-R_N-Sp-3R!H=1C_Ext-2O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
                    L6: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-2O-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-2O-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-5R!H-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_1R->C_Ext-2O-R_Ext-3R!H-R_Ext-4R!H-R
                L5: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C
                    L6: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_6R!H->O
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_6R!H->O_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_6R!H->O_Ext-3R!H-R_3R!H-inRing
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_6R!H->O_Ext-3R!H-R_N-3R!H-inRing
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_N-6R!H->O
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Ext-4O-R_Ext-5R!H-R_N-6R!H->O_Ext-6BrCClFINPSSi-R_Ext-6BrCClFINPSSi-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C_Ext-5C-R_Ext-6R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C_Ext-5C-R_Sp-6R!H-5C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_N-5R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_Sp-4O-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-5R!H-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_6R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_4R!H->O_N-Sp-4O-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H->C
                    L6: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_6R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_6R!H->O_Ext-6O-R_Ext-5R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_6R!H->O_Ext-7R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_6R!H->O_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_N-6R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_N-6R!H->O_Ext-7R!H-R_Sp-7R!H-4BrCClFINPSSi
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_N-6R!H->O_Ext-7R!H-R_Sp-7R!H-4BrCClFINPSSi_Ext-4BrCClFINPSSi-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_N-6R!H->O_Ext-7R!H-R_Sp-7R!H-4BrCClFINPSSi_Ext-3R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R_N-6R!H->O_Ext-7R!H-R_N-Sp-7R!H-4BrCClFINPSSi
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-5R!H-R_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-3R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-4BrCClFINPSSi-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Sp-5R!H-4BrCClFINPSSi
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-Sp-5R!H-4BrCClFINPSSi
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi_Ext-5C-R_Sp-6R!H-5C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Ext-3R!H-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Ext-3R!H-R_6R!H->C
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Ext-3R!H-R_N-6R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_Sp-5C-4BrCClFINPSSi_Ext-5C-R_N-Sp-6R!H-5C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_5R!H->C_N-Sp-5C-4BrCClFINPSSi
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_3R!H-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3R!H_Ext-4BrCClFINPSSi-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5BrClFINOPSSi-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-6O-R_Ext-7R!H-R_7R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_6R!H->O_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-6O-R_Ext-7R!H-R_N-7R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-6R!H->O
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-3R!H-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-6R!H->O_Ext-3R!H-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_7R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_7R!H->C_Sp-7C-6R!H
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_7R!H->C_N-Sp-7C-6R!H
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_N-7R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-7R!H-R_N-7R!H->C_Ext-6R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_7R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_7R!H->O_Ext-4BrCClFINPSSi-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_7R!H->O_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-7R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H_Ext-4BrCClFINPSSi-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-6R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-7R!H-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-5R!H-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-4BrCClFINPSSi-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-5R!H-R_7R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H=5R!H_N-6R!H->C_Ext-5R!H-R_N-7R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_Ext-5R!H-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-5R!H-R_Ext-4BrCClFINPSSi-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H_Ext-6R!H-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H_Ext-6R!H-R_Ext-7R!H-R_8R!H->C
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_6R!H->C
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_N-6R!H->C
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Sp-6R!H-5R!H_Ext-6R!H-R_Ext-7R!H-R_N-8R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-Sp-6R!H-5R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H-5R!H
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-4BrCClFINPSSi-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-4BrCClFINPSSi-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-4BrCClFINPSSi-R_6R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-4BrCClFINPSSi-R_N-6R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-6C-R_8R!H->C
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-6C-R_8R!H->C_Sp-8C-6C
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-6C-R_8R!H->C_N-Sp-8C-6C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-6C-R_N-8R!H->C
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-6C-R_N-8R!H->C_Ext-5R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->C_Ext-6C-R_Ext-7R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_N-6R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_N-6R!H->C_Ext-4BrCClFINPSSi-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_7R!H->O
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H_Ext-7BrCClFINPSSi-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H_Ext-7BrCClFINPSSi-R_Ext-7BrCClFINPSSi-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_Sp-7BrCClFINPSSi-6R!H_Ext-6R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C_Ext-4BrCClFINPSSi-R_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-6R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_6R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_6R!H->C_Ext-6C-R_Ext-6C-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_N-6R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C_Ext-4BrCClFINPSSi-R_N-6R!H->C_Ext-6BrClFINOPSSi-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_5R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_5R!H->C_Ext-6R!H-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_5R!H->C_Ext-6R!H-R_Ext-7R!H-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_5R!H->C_Ext-6R!H-R_Ext-7R!H-R_Ext-4BrCClFINPSSi-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_N-5R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_N-5R!H->C_Ext-4BrCClFINPSSi-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrCClFINPSSi-3R!H
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_2R!H->O_N-1R->C_Ext-2O-R_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_N-Sp-4BrCClFINPSSi-3R!H_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R
            L4: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O
                L5: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R
                    L6: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_Sp-4C-3R!H
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R_Ext-2CN-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R_Ext-2CN-R_Sp-6R!H-2CN
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R_Ext-2CN-R_N-Sp-6R!H-2CN
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R_5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-4C-R_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-2CN-R_Sp-5R!H-2CN
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-2CN-R_Sp-5R!H-2CN_Sp-4C=3R!H
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-2CN-R_Sp-5R!H-2CN_N-Sp-4C=3R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_4R!H->C_N-Sp-4C-3R!H_Ext-2CN-R_N-Sp-5R!H-2CN
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_N-4R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-3R!H-R_N-4R!H->C_Ext-4BrClFINOPSSi-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-2CN-R_Ext-4R!H-R_5R!H->C
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_Sp-2CCNN=1R_Ext-2CN-R_Ext-4R!H-R_N-5R!H->C
                    L6: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_Ext-5R!H-R_Ext-2CN-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_5R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_5R!H->O_Ext-6O-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_5R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_9R!H->O
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_5R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_N-9R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_5R!H->O_Ext-2CN-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_6R!H->O_N-5R!H->O
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Ext-5R!H-R_N-6R!H->O
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Sp-5R!H=2CCNN
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Sp-5R!H=2CCNN_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Sp-5R!H=2CCNN_Ext-3R!H-R_6R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Sp-5R!H=2CCNN_Ext-3R!H-R_N-6R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_Sp-5R!H=2CCNN_Ext-2CN-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-1R-R_Ext-2CN-R_N-Sp-5R!H=2CCNN
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_Ext-4C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-2CN-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->C_Ext-2CN-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->C_Ext-2CN-R_Ext-2CN-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_N-5R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_Ext-2CN-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_Ext-4C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_Ext-4C-R_Ext-6R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_Ext-4C-R_Ext-6R!H-R_5R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_Ext-4C-R_Ext-6R!H-R_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_5R!H-inRing
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_5R!H-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R_Ext-5C-R
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-12R!H-R_Ext-12R!H-R_Sp-12R!H=11R!H
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_Ext-7BrCClFINPSSi-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Ext-12R!H-R_Ext-12R!H-R_N-Sp-12R!H=11R!H
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2CN-R_N-5R!H-inRing_N-5R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-4C-R_5R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-4C-R_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_6R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_N-6R!H->C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C_Ext-3R!H-R_Ext-2CN-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C_Ext-2CN-R_Ext-2CN-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_3R!H->N
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R_Ext-8R!H-R_Sp-8R!H=7C
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R_Ext-8R!H-R_Sp-8R!H=7C_4R!H-inRing
                                                            L16: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R_Ext-8R!H-R_Sp-8R!H=7C_4R!H-inRing_Ext-10R!H-R_Ext-4R!H-R
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R_Ext-8R!H-R_Sp-8R!H=7C_N-4R!H-inRing
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_7R!H->C_Ext-2CN-R_Ext-8R!H-R_N-Sp-8R!H=7C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_N-7R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_Ext-3C-R_Ext-2CN-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_1R->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_1R->C_4R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_1R->C_4R!H->C_Ext-4C-R_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_1R->C_N-4R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_N-3R!H->N_N-1R->C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-1R-R_N-Sp-2CCNN=1R_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H
                L5: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN
                    L6: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R_Ext-6R!H-R_7R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R_Ext-6R!H-R_N-7R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Ext-4R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-4R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-4R!H-R_6R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-4R!H-R_N-6R!H->O
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_Sp-5R!H-3C_Ext-4R!H-R_N-6R!H->O_Ext-4R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-3C-R_N-Sp-5R!H-3C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_5R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_Ext-4R!H-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_N-5R!H->C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_4R!H->O
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_Ext-4C-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3C-R
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-8R!H-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_5R!H-inRing
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_5R!H-inRing_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R
                                                            L16: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_5R!H-inRing_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Int-10R!H-7R!H
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->O_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-5R!H-inRing
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_N-Sp-4R!H-3C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_Sp-2CN-1C_Ext-3C-R_N-Sp-4R!H-3C_Ext-4R!H-R_Ext-5R!H-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_N-Sp-2CN-1C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_1R->C_N-Sp-2CN-1C_Ext-3C-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->O
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->O_Ext-5O-R
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->O_Ext-5O-R_4C-inRing
                                                    L14: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->O_Ext-5O-R_N-4C-inRing
                                                        L15: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->O_Ext-5O-R_N-4C-inRing_Ext-3C-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_N-5R!H->O
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_5R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C_5R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C_5R!H->C_Ext-5C-R_Ext-5C-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_3C-inRing
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_4R!H->C_N-3C-inRing
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-2CN-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-6R!H-R_Ext-6R!H-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_4C-inRing
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-3C-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-3C-R_Ext-4C-R_Sp-7R!H-4C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-3C-R_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-3C-R_Ext-4C-R_N-Sp-7R!H-4C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-5C-R_6R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-4C-inRing_Ext-5C-R_N-6R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->C
                    L6: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-6O-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_5R!H->C_4R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_5R!H->C_N-4R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_N-5R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_4R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C_Ext-6BrCClFINPSSi-R_7R!H->O
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C_Ext-6BrCClFINPSSi-R_N-7R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C_Ext-6BrCClFINPSSi-R_N-7R!H->O_Sp-6BrCClFINPSSi-5R!H
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C_Ext-6BrCClFINPSSi-R_N-7R!H->O_Sp-6BrCClFINPSSi-5R!H_Ext-5R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O_N-4R!H->C_Ext-6BrCClFINPSSi-R_N-7R!H->O_N-Sp-6BrCClFINPSSi-5R!H
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_1R->C_Ext-2CN-R_Ext-4R!H-R_Ext-4R!H-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_Sp-3R!H=2CCNN_N-3R!H->C_N-1R->C
                L5: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN
                    L6: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C_Ext-3O-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C_Ext-3O-R_6R!H->N
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C_Ext-3O-R_N-6R!H->N
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C_Ext-3O-R_N-6R!H->N_Ext-6BrCClFIOPSSi-R_7R!H-inRing
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_5R!H->C_Ext-3O-R_N-6R!H->N_Ext-6BrCClFIOPSSi-R_N-7R!H-inRing
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_3R!H->O_Ext-4R!H-R_N-5R!H->C
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_Ext-4R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_5R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_5R!H->O_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_N-5R!H->O
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Ext-2CN-R_N-3R!H->O_Ext-3C-R_N-5R!H->O_Ext-3C-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_3R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_N-3R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_Sp-3R!H-2CN_Ext-3R!H-R_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_1R->C_N-Sp-3R!H-2CN
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-4R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-4R!H-R_Ext-2CN-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2CN-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2CN-R_Ext-2CN-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_Ext-2CN-R_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_Ext-2CN-R
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_3R!H->C
                                                L13: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_5R!H->C_N-3R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->C
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_4R!H->C_Ext-2CN-R
                                        L11: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-4R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R_6R!H->C
                                            L12: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R_N-6R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_3R!H->C
                                    L10: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_Sp-2CN-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_N-3R!H->C
                    L6: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_3R!H->O
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_3R!H->O_Ext-2CN-R
                                L9: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_3R!H->O_Ext-2CN-R_Ext-3O-R
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_3R!H->O_Ext-3O-R
                        L7: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_N-3R!H->O
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_N-3R!H->O_Ext-3C-R_4R!H->O
                            L8: RJ1_Ext-1R-R_N-2R!H-inRing_N-2R!H->O_Ext-2CN-R_N-Sp-3R!H=2CCNN_N-Sp-2CN-1R_N-3R!H->O_Ext-3C-R_N-4R!H->O
"""
)

