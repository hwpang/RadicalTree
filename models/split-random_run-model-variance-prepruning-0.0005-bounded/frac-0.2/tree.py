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
        Cpdata = ([-0.605798,-1.65644,-2.40614,-2.8275,-3.25989,-3.62766,-4.44092],'cal/mol/K','+|-',[6.08055,6.48277,6.61369,6.48072,6.08167,5.89997,5.97121]),
        H298 = (93.0172,'kcal/mol','+|-',28.1263),
        S298 = (0.379382,'cal/mol/K','+|-',10.8584),
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
        Cpdata = ([-0.605798,-1.65644,-2.40614,-2.8275,-3.25989,-3.62766,-4.44092],'cal/mol/K','+|-',[6.08055,6.48277,6.61369,6.48072,6.08167,5.89997,5.97121]),
        H298 = (93.0172,'kcal/mol','+|-',28.1263),
        S298 = (0.379382,'cal/mol/K','+|-',10.8584),
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
        Cpdata = ([-0.218816,-1.37587,-2.25838,-2.76265,-3.32392,-3.79668,-4.89387],'cal/mol/K','+|-',[5.93842,6.31411,6.54088,6.46709,6.04048,5.88125,6.12503]),
        H298 = (91.6397,'kcal/mol','+|-',40.8549),
        S298 = (1.19091,'cal/mol/K','+|-',9.01864),
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
        Cpdata = ([-0.432695,-1.28869,-1.99203,-2.38916,-2.90841,-3.34959,-4.17687],'cal/mol/K','+|-',[5.50381,5.54322,5.60531,5.53875,5.50714,5.63448,5.87706]),
        H298 = (80.5735,'kcal/mol','+|-',49.7439),
        S298 = (0.0827347,'cal/mol/K','+|-',10.0552),
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
        Cpdata = ([-0.716405,-1.56666,-2.23939,-2.59398,-3.03452,-3.42973,-4.27583],'cal/mol/K','+|-',[5.53613,5.56127,5.54761,5.38523,5.1797,5.13213,5.07777]),
        H298 = (81.7072,'kcal/mol','+|-',35.5912),
        S298 = (-0.162118,'cal/mol/K','+|-',10.6049),
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
        Cpdata = ([-0.498218,-1.36696,-2.10177,-2.50161,-2.99662,-3.42362,-4.33464],'cal/mol/K','+|-',[5.47902,5.48174,5.51586,5.38753,5.20171,5.14479,5.07627]),
        H298 = (83.904,'kcal/mol','+|-',33.9405),
        S298 = (0.18085,'cal/mol/K','+|-',10.7917),
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
        Cpdata = ([-0.813348,-1.46847,-2.07098,-2.44883,-2.94626,-3.32183,-4.22604],'cal/mol/K','+|-',[5.57117,5.93169,6.02061,6.00091,5.86455,5.71642,5.4959]),
        H298 = (84.8032,'kcal/mol','+|-',49.3364),
        S298 = (1.25014,'cal/mol/K','+|-',13.2511),
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
        Cpdata = ([-0.980783,-1.64213,-2.22583,-2.6193,-3.14017,-3.5037,-4.36456],'cal/mol/K','+|-',[5.6611,6.12659,6.27539,6.26789,6.06695,5.84927,5.52659]),
        H298 = (88.1187,'kcal/mol','+|-',49.9962),
        S298 = (0.070945,'cal/mol/K','+|-',9.04767),
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
        Cpdata = ([-2.15535,-3.44762,-4.33099,-4.71551,-4.8172,-4.786,-5.39466],'cal/mol/K','+|-',[6.85991,7.5621,7.57599,7.54086,7.52797,7.24367,6.69374]),
        H298 = (70.2075,'kcal/mol','+|-',22.8112),
        S298 = (1.85496,'cal/mol/K','+|-',14.1292),
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
        Cpdata = ([-2.68112,-4.19998,-5.13211,-5.47145,-5.50283,-5.4153,-5.92392],'cal/mol/K','+|-',[6.97899,7.38146,7.26268,7.34263,7.50721,7.26181,6.75314]),
        H298 = (74.245,'kcal/mol','+|-',15.357),
        S298 = (2.72303,'cal/mol/K','+|-',15.4731),
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
        Cpdata = ([-3.63615,-4.51968,-4.85907,-4.67736,-4.21133,-4.06771,-4.55369],'cal/mol/K','+|-',[9.39184,9.95257,9.51706,8.79702,7.15114,5.89306,4.75727]),
        H298 = (79.7686,'kcal/mol','+|-',8.50317),
        S298 = (-0.259981,'cal/mol/K','+|-',4.57414),
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
        Cpdata = ([-0.551068,-0.898226,-1.29143,-1.57532,-2.13434,-2.5724,-3.53444],'cal/mol/K','+|-',[5.1971,4.98651,4.85542,4.85608,4.9315,5.06096,4.88974]),
        H298 = (70.5368,'kcal/mol','+|-',11.6221),
        S298 = (-1.08443,'cal/mol/K','+|-',6.58132),
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
        Cpdata = ([-0.530161,-0.741532,-1.16135,-1.53752,-2.23542,-2.75381,-3.68842],'cal/mol/K','+|-',[5.40309,5.02935,4.89292,4.96419,5.02191,5.08951,4.90674]),
        H298 = (69.6826,'kcal/mol','+|-',8.61331),
        S298 = (-0.994384,'cal/mol/K','+|-',7.09068),
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
        Cpdata = ([-0.40782,-0.878094,-1.42883,-1.98467,-2.8713,-3.5252,-4.49662],'cal/mol/K','+|-',[2.83044,2.82871,2.82848,2.82851,2.83569,2.83913,2.83047]),
        H298 = (115.999,'kcal/mol','+|-',3.63135),
        S298 = (-0.0955445,'cal/mol/K','+|-',2.83938),
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
        Cpdata = ([-0.244069,-0.878016,-1.54447,-1.86921,-2.28696,-2.70347,-3.75506],'cal/mol/K','+|-',[5.33253,5.34828,5.24312,5.12473,5.17426,5.31051,5.52757]),
        H298 = (64.0994,'kcal/mol','+|-',20.6828),
        S298 = (5.25939,'cal/mol/K','+|-',21.7378),
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
        Cpdata = ([-1.13832,-1.85349,-2.46634,-2.74416,-3.2337,-3.72908,-4.80494],'cal/mol/K','+|-',[4.52048,4.58423,4.67233,4.57451,4.48276,4.47367,4.4985]),
        H298 = (65.5442,'kcal/mol','+|-',15.9103),
        S298 = (2.6208,'cal/mol/K','+|-',7.79221),
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
        Cpdata = ([-0.355273,-1.32091,-2.11574,-2.52555,-3.01947,-3.46979,-4.3839],'cal/mol/K','+|-',[5.44675,5.30604,5.31695,5.12939,4.9113,4.89677,4.90084]),
        H298 = (83.4994,'kcal/mol','+|-',25.9923),
        S298 = (-0.304187,'cal/mol/K','+|-',9.54685),
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
        Cpdata = ([-0.228804,-1.34148,-2.246,-2.67466,-3.16189,-3.59986,-4.44049],'cal/mol/K','+|-',[5.58837,5.41684,5.39074,5.15807,4.924,4.94337,4.94064]),
        H298 = (79.8785,'kcal/mol','+|-',14.7678),
        S298 = (-0.716506,'cal/mol/K','+|-',9.75904),
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
        Cpdata = ([-1.86317,-2.48632,-2.8968,-3.11866,-3.35342,-3.56768,-3.99557],'cal/mol/K','+|-',[4.65354,5.4025,5.84586,5.45247,4.91413,4.64156,4.7738]),
        H298 = (68.9527,'kcal/mol','+|-',25.1006),
        S298 = (0.633023,'cal/mol/K','+|-',7.0742),
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
        Cpdata = ([-1.8766,-1.23552,-1.31703,-1.7929,-2.50266,-3.08355,-4.56064],'cal/mol/K','+|-',[4.99613,4.58506,4.50655,4.47584,4.50577,4.52076,4.70463]),
        H298 = (59.3035,'kcal/mol','+|-',11.5196),
        S298 = (-1.06696,'cal/mol/K','+|-',7.73846),
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
        Cpdata = ([-1.84974,-3.73711,-4.47656,-4.44441,-4.20418,-4.0518,-3.4305],'cal/mol/K','+|-',[4.47237,4.63749,4.72046,4.5862,4.5347,4.5216,4.59621]),
        H298 = (78.6018,'kcal/mol','+|-',14.0701),
        S298 = (2.33301,'cal/mol/K','+|-',4.90001),
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
        Cpdata = ([0.0382919,-1.12572,-2.09485,-2.56221,-3.10996,-3.61303,-4.46195],'cal/mol/K','+|-',[5.53506,5.32403,5.30732,5.11221,4.93966,5.00027,4.9606]),
        H298 = (80.9358,'kcal/mol','+|-',12.0312),
        S298 = (-1.17952,'cal/mol/K','+|-',9.52824),
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
        Cpdata = ([0.200041,-1.08327,-2.13931,-2.60275,-3.10105,-3.56181,-4.31558],'cal/mol/K','+|-',[5.72327,5.47067,5.39823,5.14967,4.96293,5.03488,4.95939]),
        H298 = (82.4714,'kcal/mol','+|-',11.4461),
        S298 = (-1.61281,'cal/mol/K','+|-',10.2487),
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
        Cpdata = ([1.17096,0.318056,-0.710134,-1.36372,-2.41986,-3.17194,-4.48534],'cal/mol/K','+|-',[5.60678,4.97643,4.56121,4.52583,4.48538,4.48199,4.4728]),
        H298 = (79.8107,'kcal/mol','+|-',8.42932),
        S298 = (2.63771,'cal/mol/K','+|-',4.70015),
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
        Cpdata = ([0.11057,-1.2306,-2.29625,-2.69084,-3.05257,-3.44916,-4.15209],'cal/mol/K','+|-',[5.803,5.50057,5.42809,5.175,4.89556,4.89086,4.79747]),
        H298 = (82.2283,'kcal/mol','+|-',10.5418),
        S298 = (-2.27012,'cal/mol/K','+|-',10.0527),
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
        Cpdata = ([0.323008,-1.0361,-2.13543,-2.57815,-2.98746,-3.41228,-4.18304],'cal/mol/K','+|-',[5.86748,5.47244,5.38078,5.17194,4.92493,4.93448,4.83459]),
        H298 = (81.8492,'kcal/mol','+|-',10.4049),
        S298 = (-2.0727,'cal/mol/K','+|-',10.3235),
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
        Cpdata = ([0.754309,-0.632491,-1.97019,-2.09699,-1.9882,-2.25251,-3.14499],'cal/mol/K','+|-',[6.98336,6.71074,6.32583,5.62685,4.85585,4.67445,4.67997]),
        H298 = (80.3747,'kcal/mol','+|-',10.6197),
        S298 = (-6.8391,'cal/mol/K','+|-',8.99344),
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
        Cpdata = ([-0.689342,-2.09682,-3.2369,-2.9033,-2.03771,-2.0518,-2.66865],'cal/mol/K','+|-',[6.10122,5.08358,4.78513,4.71097,4.68682,4.72774,4.47886]),
        H298 = (78.3694,'kcal/mol','+|-',9.67902),
        S298 = (-9.35746,'cal/mol/K','+|-',5.33033),
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
        Cpdata = ([0.235448,-1.76027,-3.18214,-3.07512,-2.11383,-1.91273,-2.61831],'cal/mol/K','+|-',[5.82443,5.3821,5.07178,4.866,4.87787,4.92329,4.4788]),
        H298 = (79.7297,'kcal/mol','+|-',8.55549),
        S298 = (-9.0768,'cal/mol/K','+|-',5.91053),
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
        Cpdata = ([0.103983,-0.819411,-1.65539,-2.18585,-2.80426,-3.32994,-4.29149],'cal/mol/K','+|-',[5.42752,4.99328,4.91424,4.89514,4.74263,4.76634,4.64837]),
        H298 = (83.5597,'kcal/mol','+|-',8.39244),
        S298 = (1.19357,'cal/mol/K','+|-',6.34646),
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
        Cpdata = ([-0.227359,-1.35288,-2.2616,-2.73804,-3.12184,-3.49511,-4.29427],'cal/mol/K','+|-',[5.95024,4.87219,4.55236,4.64334,4.7645,4.95054,4.79276]),
        H298 = (83.7973,'kcal/mol','+|-',8.38281),
        S298 = (0.316424,'cal/mol/K','+|-',6.55255),
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
        Cpdata = ([1.23114,-1.60541,-3.36024,-4.03113,-4.23661,-4.40022,-5.00929],'cal/mol/K','+|-',[6.82532,5.38948,4.97124,4.61973,4.48965,4.58754,4.6231]),
        H298 = (78.9822,'kcal/mol','+|-',13.2859),
        S298 = (-5.83442,'cal/mol/K','+|-',8.41656),
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
        Cpdata = ([-1.27027,-2.49489,-3.34157,-3.42334,-3.47577,-3.68885,-3.95096],'cal/mol/K','+|-',[4.59287,5.24209,5.61944,5.1963,4.71988,4.66838,4.59943]),
        H298 = (86.04,'kcal/mol','+|-',8.89598),
        S298 = (-3.5534,'cal/mol/K','+|-',9.15688),
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
        Cpdata = ([-0.550936,-1.2804,-1.93291,-2.41454,-3.14244,-3.79961,-4.99515],'cal/mol/K','+|-',[4.68582,4.87059,5.14146,5.1488,4.99959,5.00201,4.94137]),
        H298 = (77,'kcal/mol','+|-',9.92975),
        S298 = (0.398877,'cal/mol/K','+|-',5.56739),
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
        Cpdata = ([-0.8988,-1.81266,-2.45183,-2.84386,-3.45593,-4.1053,-5.24521],'cal/mol/K','+|-',[4.47348,5.19845,6.04264,6.16631,5.89801,5.9316,5.72015]),
        H298 = (75.4988,'kcal/mol','+|-',8.82706),
        S298 = (1.51392,'cal/mol/K','+|-',5.51911),
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
        Cpdata = ([-2.01144,-2.63001,-2.92626,-3.02354,-3.09292,-3.25848,-4.37973],'cal/mol/K','+|-',[4.53109,4.62898,4.97976,5.11939,5.0284,4.739,5.86824]),
        H298 = (76.1606,'kcal/mol','+|-',16.0779),
        S298 = (2.88125,'cal/mol/K','+|-',17.1521),
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
        Cpdata = ([-0.0648806,-0.359649,-0.778873,-1.20598,-1.90116,-2.57278,-3.89021],'cal/mol/K','+|-',[3.14248,2.84741,3.15221,3.23655,3.12055,3.06678,3.04119]),
        H298 = (85.732,'kcal/mol','+|-',4.57574),
        S298 = (-0.178502,'cal/mol/K','+|-',4.89325),
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
        Cpdata = ([-2.33558,-3.04863,-3.26063,-3.27944,-3.31579,-3.47514,-3.83938],'cal/mol/K','+|-',[4.89081,5.3504,5.48731,5.28001,5.06685,5.13243,5.09122]),
        H298 = (62.0667,'kcal/mol','+|-',26.7066),
        S298 = (-2.7073,'cal/mol/K','+|-',7.77086),
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
        Cpdata = ([-2.50531,-3.67997,-3.86962,-3.92153,-4.30105,-4.65541,-4.89892],'cal/mol/K','+|-',[5.10614,5.6572,6.08612,6.01987,5.4413,5.3931,5.00181]),
        H298 = (46.9616,'kcal/mol','+|-',35.2671),
        S298 = (-1.53837,'cal/mol/K','+|-',12.309),
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
        Cpdata = ([-2.25724,-2.75724,-2.97956,-2.98309,-2.86105,-2.9304,-3.35036],'cal/mol/K','+|-',[4.88715,5.28266,5.32934,4.99052,4.68811,4.6677,4.86923]),
        H298 = (66.5731,'kcal/mol','+|-',11.2823),
        S298 = (-3.24681,'cal/mol/K','+|-',5.31007),
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
        Cpdata = ([-2.18191,-3.49476,-3.93997,-3.9147,-3.70024,-3.75699,-4.05035],'cal/mol/K','+|-',[5.37758,5.08956,4.82673,4.59601,4.4726,4.52053,4.58385]),
        H298 = (61.766,'kcal/mol','+|-',8.58643),
        S298 = (-4.0291,'cal/mol/K','+|-',6.20347),
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
        Cpdata = ([0.674467,-0.203921,-1.02673,-1.58988,-2.41626,-3.03683,-3.79071],'cal/mol/K','+|-',[4.7984,4.94316,5.48737,5.93937,6.69119,7.42842,8.48999]),
        H298 = (76.7298,'kcal/mol','+|-',85.3802),
        S298 = (1.03826,'cal/mol/K','+|-',7.50299),
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
        Cpdata = ([0.610007,0.104226,-0.568979,-1.07844,-1.80597,-2.41009,-3.03244],'cal/mol/K','+|-',[4.76189,4.81527,5.23755,5.67755,6.38319,7.17918,8.24956]),
        H298 = (72.0769,'kcal/mol','+|-',86.0724),
        S298 = (0.700816,'cal/mol/K','+|-',7.62146),
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
        Cpdata = ([0.499437,0.173913,-0.351125,-0.828435,-1.51031,-2.03484,-2.52742],'cal/mol/K','+|-',[4.64439,4.84402,5.49548,6.14596,7.16426,8.26123,9.65599]),
        H298 = (67.7357,'kcal/mol','+|-',102.868),
        S298 = (1.30684,'cal/mol/K','+|-',5.3043),
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
        Cpdata = ([0.0391434,0.0528029,-0.240166,-0.566519,-0.923043,-1.19427,-1.01702],'cal/mol/K','+|-',[4.53852,5.26734,6.57591,7.73631,9.33623,11.0054,12.51]),
        H298 = (39.341,'kcal/mol','+|-',124.867),
        S298 = (0.246191,'cal/mol/K','+|-',4.74172),
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
        Cpdata = ([0.831148,-0.0351488,-1.00469,-1.57845,-2.39727,-3.16058,-4.04246],'cal/mol/K','+|-',[5.1079,4.89739,4.82133,4.86456,4.91543,4.96515,5.1288]),
        H298 = (84.1685,'kcal/mol','+|-',14.5006),
        S298 = (-0.511224,'cal/mol/K','+|-',11.4969),
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
        Cpdata = ([1.92346,0.752333,-0.543949,-1.06719,-1.60787,-2.38138,-3.47565],'cal/mol/K','+|-',[5.27788,5.16878,5.15044,5.33409,5.18212,5.37444,6.28593]),
        H298 = (78.3427,'kcal/mol','+|-',9.55127),
        S298 = (-5.83748,'cal/mol/K','+|-',9.09798),
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
        Cpdata = ([-0.0381868,-1.44951,-2.48332,-3.07807,-3.67483,-4.17426,-5.4994],'cal/mol/K','+|-',[6.27624,6.91486,7.22812,7.11719,6.38971,5.99455,6.08532]),
        H298 = (100.741,'kcal/mol','+|-',17.1641),
        S298 = (2.12681,'cal/mol/K','+|-',7.60363),
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
        Cpdata = ([0.217366,-1.153,-2.17513,-2.8055,-3.48862,-4.04864,-5.49105],'cal/mol/K','+|-',[5.47152,6.12468,6.5289,6.53799,5.99491,5.68528,6.05996]),
        H298 = (101.023,'kcal/mol','+|-',12.7523),
        S298 = (2.18556,'cal/mol/K','+|-',7.27756),
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
        Cpdata = ([0.00575634,-0.629448,-1.33825,-1.85905,-2.6338,-3.27693,-4.25988],'cal/mol/K','+|-',[4.99474,4.97217,4.86838,4.79124,4.72299,4.72884,4.62914]),
        H298 = (104.337,'kcal/mol','+|-',11.4989),
        S298 = (1.4442,'cal/mol/K','+|-',6.11963),
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
        Cpdata = ([-0.540348,-1.05597,-1.60562,-2.03486,-2.76813,-3.39535,-4.18424],'cal/mol/K','+|-',[4.52687,4.61584,4.7229,4.78541,4.83629,4.8461,4.63529]),
        H298 = (106.096,'kcal/mol','+|-',10.3062),
        S298 = (1.8823,'cal/mol/K','+|-',6.05068),
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
        Cpdata = ([-0.417214,-0.784381,-1.16708,-1.57851,-2.34878,-2.95369,-3.88681],'cal/mol/K','+|-',[2.83814,2.91518,3.05725,3.20582,3.42738,3.44815,3.02901]),
        H298 = (103.88,'kcal/mol','+|-',4.03123),
        S298 = (0.28743,'cal/mol/K','+|-',3.12761),
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
        Cpdata = ([-0.722172,-1.54598,-2.17345,-2.61074,-3.32914,-3.87674,-4.71256],'cal/mol/K','+|-',[3.1036,3.11911,3.21611,3.27273,3.27998,3.19401,2.94783]),
        H298 = (109.043,'kcal/mol','+|-',3.58249),
        S298 = (3.96991,'cal/mol/K','+|-',3.0265),
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
        Cpdata = ([0.00357719,-0.869382,-1.60899,-2.08832,-2.46765,-2.80576,-3.87799],'cal/mol/K','+|-',[4.53503,4.48277,4.47612,4.49269,4.53653,4.49903,4.47267]),
        H298 = (98.3258,'kcal/mol','+|-',10.1158),
        S298 = (2.01203,'cal/mol/K','+|-',6.74839),
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
        Cpdata = ([0.0534371,-1.64688,-2.62526,-3.2237,-3.84118,-4.36468,-5.96361],'cal/mol/K','+|-',[5.70864,6.11838,6.37635,6.41276,6.09858,5.8658,6.54972]),
        H298 = (98.9306,'kcal/mol','+|-',10.0479),
        S298 = (2.07252,'cal/mol/K','+|-',8.01052),
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
        Cpdata = ([-0.120899,-2.02243,-2.82131,-3.33072,-3.84218,-4.2106,-5.78593],'cal/mol/K','+|-',[5.92558,7.02151,7.56638,7.47921,6.43771,5.72458,7.19898]),
        H298 = (97.6442,'kcal/mol','+|-',10.6501),
        S298 = (1.68517,'cal/mol/K','+|-',6.60055),
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
        Cpdata = ([0.173501,-1.73882,-2.79765,-3.42756,-3.94841,-4.38637,-6.58558],'cal/mol/K','+|-',[5.95225,7.30274,8.08867,8.03376,6.7826,5.95802,8.05728]),
        H298 = (95.9069,'kcal/mol','+|-',10.4938),
        S298 = (1.60054,'cal/mol/K','+|-',6.88772),
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
        Cpdata = ([0.505212,-1.21771,-2.15168,-2.83575,-3.57505,-4.16277,-6.1419],'cal/mol/K','+|-',[5.67754,6.68783,7.16467,7.3267,6.55225,5.94383,7.86267]),
        H298 = (96.4515,'kcal/mol','+|-',9.25009),
        S298 = (1.55355,'cal/mol/K','+|-',7.1748),
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
        Cpdata = ([0.607026,0.124052,-0.808933,-1.68136,-2.78046,-3.64781,-5.92541],'cal/mol/K','+|-',[4.48065,4.47222,4.58744,4.79225,4.69684,4.75622,8.41518]),
        H298 = (96.3676,'kcal/mol','+|-',11.1804),
        S298 = (3.11178,'cal/mol/K','+|-',7.52688),
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
        Cpdata = ([1.08184,-1.7415,-4.34948,-5.56856,-6.14465,-6.51496,-9.73689],'cal/mol/K','+|-',[7.00027,9.04515,9.44838,9.29822,6.84437,4.88923,9.08103]),
        H298 = (95.17,'kcal/mol','+|-',8.48898),
        S298 = (1.89603,'cal/mol/K','+|-',7.51068),
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
        Cpdata = ([-0.611564,-2.4951,-2.86076,-3.1693,-3.66513,-3.91766,-4.45317],'cal/mol/K','+|-',[6.34523,7.36664,7.72877,7.51746,6.54877,5.73726,4.72574]),
        H298 = (99.9115,'kcal/mol','+|-',9.24606),
        S298 = (1.82622,'cal/mol/K','+|-',6.91405),
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
        Cpdata = ([0.373245,-2.59258,-3.14245,-3.66343,-4.40468,-4.63694,-4.8657],'cal/mol/K','+|-',[7.09765,10.4751,11.065,10.4929,8.19834,6.46037,4.70324]),
        H298 = (98.7176,'kcal/mol','+|-',9.33851),
        S298 = (3.05302,'cal/mol/K','+|-',7.58863),
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
        Cpdata = ([0.160721,-1.41578,-2.50461,-3.15785,-3.84057,-4.4595,-6.07295],'cal/mol/K','+|-',[5.65107,5.59372,5.69772,5.83966,6.00099,6.02591,6.27002]),
        H298 = (99.8971,'kcal/mol','+|-',9.30531),
        S298 = (2.31089,'cal/mol/K','+|-',8.86852),
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
        Cpdata = ([1.11805,0.604251,-0.754809,-1.42444,-2.22105,-3.35072,-6.31328],'cal/mol/K','+|-',[4.98412,5.68834,6.17362,7.23363,7.88338,7.49419,5.59064]),
        H298 = (102.933,'kcal/mol','+|-',10.3426),
        S298 = (-0.702701,'cal/mol/K','+|-',11.5743),
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
        Cpdata = ([0.108425,-1.54852,-2.57063,-3.21664,-3.87606,-4.39989,-5.91614],'cal/mol/K','+|-',[5.72125,5.28462,5.34171,5.38278,5.50183,5.57419,6.36401]),
        H298 = (99.6826,'kcal/mol','+|-',9.09052),
        S298 = (2.31664,'cal/mol/K','+|-',7.63378),
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
        Cpdata = ([0.390814,-1.56736,-2.55909,-3.19879,-3.86743,-4.48836,-5.0967],'cal/mol/K','+|-',[5.79598,5.2154,5.31882,5.44983,5.82627,6.02529,5.6539]),
        H298 = (99.6929,'kcal/mol','+|-',9.18988),
        S298 = (1.59256,'cal/mol/K','+|-',7.82978),
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
        Cpdata = ([1.27985,-1.23545,-3.28144,-4.33457,-5.35985,-6.34783,-6.17288],'cal/mol/K','+|-',[4.57963,4.80521,4.85708,4.59992,5.03026,5.2587,6.06717]),
        H298 = (102.339,'kcal/mol','+|-',9.34316),
        S298 = (-0.741381,'cal/mol/K','+|-',12.4422),
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
        Cpdata = ([1.29368,-0.752489,-2.82855,-4.34899,-5.89145,-7.02274,-7.10743],'cal/mol/K','+|-',[4.68418,4.53674,4.71802,4.72372,4.88106,4.93718,5.71491]),
        H298 = (103.252,'kcal/mol','+|-',9.20913),
        S298 = (2.59036,'cal/mol/K','+|-',4.81711),
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
        Cpdata = ([0.158891,-1.65394,-2.37065,-2.90251,-3.4781,-4.00329,-4.81596],'cal/mol/K','+|-',[6.05845,5.36637,5.43088,5.53804,5.82944,5.88945,5.53352]),
        H298 = (99.3348,'kcal/mol','+|-',8.93342),
        S298 = (2.20142,'cal/mol/K','+|-',6.18269),
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
        Cpdata = ([1.06266,-1.20898,-1.95715,-2.39458,-2.83337,-3.35068,-4.32343],'cal/mol/K','+|-',[6.34691,5.75751,5.74366,5.41211,4.75871,4.49126,4.53175]),
        H298 = (100.262,'kcal/mol','+|-',8.5437),
        S298 = (2.21873,'cal/mol/K','+|-',6.68138),
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
        Cpdata = ([-1.24698,-2.34611,-3.01389,-3.69261,-4.48101,-5.01844,-5.5821],'cal/mol/K','+|-',[4.49906,4.669,5.03047,5.83131,7.3405,7.79053,7.10061]),
        H298 = (97.7101,'kcal/mol','+|-',8.51666),
        S298 = (2.17448,'cal/mol/K','+|-',6.28714),
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
        Cpdata = ([-1.03717,-2.89529,-3.97871,-5.28644,-6.96905,-7.72434,-7.9282],'cal/mol/K','+|-',[4.47329,4.52281,4.55454,4.55682,4.6058,4.80398,4.67504]),
        H298 = (98.5972,'kcal/mol','+|-',8.39123),
        S298 = (4.07612,'cal/mol/K','+|-',4.47223),
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
        Cpdata = ([-0.437526,-1.51209,-2.59295,-3.25116,-3.89276,-4.22885,-7.50041],'cal/mol/K','+|-',[5.65942,5.61823,5.59595,5.45979,5.02019,4.76387,6.70854]),
        H298 = (99.6592,'kcal/mol','+|-',9.20078),
        S298 = (3.71653,'cal/mol/K','+|-',6.86653),
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
        Cpdata = ([-1.36396,-2.59077,-3.72058,-4.26948,-4.57024,-4.6411,-8.95687],'cal/mol/K','+|-',[5.80519,5.20512,4.87515,4.7881,4.64803,4.63266,4.63272]),
        H298 = (97.9124,'kcal/mol','+|-',8.61731),
        S298 = (4.65178,'cal/mol/K','+|-',7.8781),
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
        Cpdata = ([-1.51724,-2.82142,-3.9293,-4.4138,-4.67158,-4.72442,-8.99073],'cal/mol/K','+|-',[6.32348,5.41877,4.96036,4.88764,4.70743,4.69315,4.70804]),
        H298 = (97.7242,'kcal/mol','+|-',8.69811),
        S298 = (5.48282,'cal/mol/K','+|-',8.15608),
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
        Cpdata = ([-0.352222,-2.12785,-3.54521,-4.13253,-4.49209,-4.65526,-8.94465],'cal/mol/K','+|-',[5.23432,5.21359,5.06653,5.08718,4.85247,4.8925,4.92751]),
        H298 = (97.0322,'kcal/mol','+|-',8.37025),
        S298 = (5.15432,'cal/mol/K','+|-',10.5097),
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
        Cpdata = ([0.48458,-0.914652,-2.13348,-2.84925,-3.55328,-4.10926,-5.61942],'cal/mol/K','+|-',[5.47726,6.57639,7.28409,7.27662,6.35327,5.8554,5.91534]),
        H298 = (100.98,'kcal/mol','+|-',14.4065),
        S298 = (2.66046,'cal/mol/K','+|-',7.05963),
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
        Cpdata = ([-0.921046,-3.25691,-4.81394,-5.36417,-5.14713,-4.91804,-7.11974],'cal/mol/K','+|-',[5.73493,7.40662,8.40114,8.47733,7.23865,6.16486,6.31087]),
        H298 = (97.7046,'kcal/mol','+|-',24.0345),
        S298 = (4.65794,'cal/mol/K','+|-',8.37841),
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
        Cpdata = ([-1.017,-3.14381,-4.57603,-5.08003,-4.79813,-4.58641,-7.09572],'cal/mol/K','+|-',[6.17954,8.28724,9.4786,9.52648,7.92672,6.60049,6.99025]),
        H298 = (91.1471,'kcal/mol','+|-',12.0471),
        S298 = (4.1577,'cal/mol/K','+|-',8.98733),
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
        Cpdata = ([-1.35182,-3.5707,-5.09678,-5.54283,-5.13115,-4.77396,-7.4632],'cal/mol/K','+|-',[6.59607,9.08569,10.5297,10.7941,8.96232,7.36055,7.79576]),
        H298 = (89.2926,'kcal/mol','+|-',10.7217),
        S298 = (4.21959,'cal/mol/K','+|-',10.513),
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
        Cpdata = ([-1.07325,-3.22131,-4.88764,-5.50082,-5.31957,-5.07994,-8.0767],'cal/mol/K','+|-',[7.0196,10.0072,11.8321,12.1917,9.97418,7.94189,8.02051]),
        H298 = (88.5681,'kcal/mol','+|-',10.7713),
        S298 = (4.47505,'cal/mol/K','+|-',11.788),
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
        Cpdata = ([-1.75679,-2.28494,-3.16821,-3.59558,-3.8201,-4.17048,-8.68747],'cal/mol/K','+|-',[6.98975,8.55932,9.1058,9.65122,8.8103,7.75788,7.17627]),
        H298 = (89.53,'kcal/mol','+|-',12.0451),
        S298 = (4.02879,'cal/mol/K','+|-',14.6837),
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
        Cpdata = ([-0.179957,-2.0766,-3.27415,-3.92303,-3.96557,-4.11753,-6.177],'cal/mol/K','+|-',[5.21925,7.00819,7.52238,6.59389,5.28591,4.71439,4.54226]),
        H298 = (95.7832,'kcal/mol','+|-',10.024),
        S298 = (4.00298,'cal/mol/K','+|-',4.71947),
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
        Cpdata = ([-0.697142,-3.52079,-5.36906,-6.02716,-5.96147,-5.69186,-7.17581],'cal/mol/K','+|-',[4.79713,5.4981,5.95259,6.11255,5.62215,5.01925,4.75439]),
        H298 = (113.006,'kcal/mol','+|-',11.065),
        S298 = (5.82515,'cal/mol/K','+|-',7.20389),
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
        Cpdata = ([-1.1435,-3.72995,-5.5208,-6.14442,-6.09659,-5.88879,-7.30645],'cal/mol/K','+|-',[4.60904,6.2776,7.09324,7.37541,6.54056,5.42725,4.97985]),
        H298 = (111.13,'kcal/mol','+|-',9.52057),
        S298 = (6.05186,'cal/mol/K','+|-',9.08617),
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
        Cpdata = ([0.807404,0.138815,-0.719853,-1.39611,-2.31567,-3.0238,-4.52877],'cal/mol/K','+|-',[4.92756,5.96135,6.43308,6.22669,5.30216,4.77534,4.83958]),
        H298 = (100.535,'kcal/mol','+|-',8.8547),
        S298 = (1.56225,'cal/mol/K','+|-',5.74868),
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
        Cpdata = ([0.649568,-0.169539,-1.09895,-1.75571,-2.55441,-3.16606,-4.68279],'cal/mol/K','+|-',[5.12522,6.81938,7.53602,7.22831,5.82239,4.98035,5.08481]),
        H298 = (101.275,'kcal/mol','+|-',8.75471),
        S298 = (1.31688,'cal/mol/K','+|-',6.29766),
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
        Cpdata = ([1.14564,0.964717,0.259347,-0.478926,-1.71624,-2.67455,-4.143],'cal/mol/K','+|-',[3.18703,3.14614,3.02689,2.9535,2.87169,2.84103,2.83793]),
        H298 = (101.141,'kcal/mol','+|-',3.91687),
        S298 = (0.332578,'cal/mol/K','+|-',2.94024),
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
        Cpdata = ([0.899963,0.582147,-0.0497071,-0.721975,-1.85499,-2.73942,-4.11456],'cal/mol/K','+|-',[3.29632,2.87816,2.83404,2.83348,2.83394,2.83582,2.844]),
        H298 = (101.494,'kcal/mol','+|-',4.02287),
        S298 = (0.543417,'cal/mol/K','+|-',2.86761),
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
        Cpdata = ([-1.2107,-4.423,-6.19257,-6.54367,-5.69758,-5.00925,-6.70702],'cal/mol/K','+|-',[4.47232,4.59067,4.52111,4.47279,4.51069,4.5123,4.58753]),
        H298 = (102.484,'kcal/mol','+|-',10.5398),
        S298 = (5.008,'cal/mol/K','+|-',4.74829),
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
        Cpdata = ([1.05731,0.627041,-0.119614,-0.826733,-1.93765,-2.79855,-4.28491],'cal/mol/K','+|-',[4.72138,4.56859,4.50008,4.49781,4.48809,4.47609,4.48131]),
        H298 = (99.3966,'kcal/mol','+|-',8.56365),
        S298 = (1.95076,'cal/mol/K','+|-',5.12929),
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
        Cpdata = ([0.790075,0.477849,-0.13803,-0.779326,-1.88906,-2.78492,-4.23717],'cal/mol/K','+|-',[2.83006,2.87048,2.89134,2.87012,2.84623,2.83623,2.83087]),
        H298 = (99.1987,'kcal/mol','+|-',3.43631),
        S298 = (1.66836,'cal/mol/K','+|-',3.69275),
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
        Cpdata = ([0.759072,-0.079449,-0.9418,-1.64994,-2.69967,-3.42097,-4.59632],'cal/mol/K','+|-',[4.69152,4.65424,4.65669,4.65605,4.59099,4.53313,4.529]),
        H298 = (101.926,'kcal/mol','+|-',9.10951),
        S298 = (2.42574,'cal/mol/K','+|-',4.97376),
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
        Cpdata = ([0.451054,-0.155809,-0.766705,-1.36935,-2.45983,-3.24828,-4.417],'cal/mol/K','+|-',[2.93025,2.95122,2.91039,2.88744,2.87999,2.86769,2.83378]),
        H298 = (101.818,'kcal/mol','+|-',3.90243),
        S298 = (2.66221,'cal/mol/K','+|-',3.22255),
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
        Cpdata = ([0.584148,0.0117479,-0.600817,-1.23271,-2.40938,-3.231,-4.40164],'cal/mol/K','+|-',[2.95763,2.9573,2.87754,2.86817,2.92021,2.90519,2.83812]),
        H298 = (101.299,'kcal/mol','+|-',3.53289),
        S298 = (2.23914,'cal/mol/K','+|-',2.91099),
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
        Cpdata = ([1.86821,0.239172,-1.54356,-2.64478,-3.50056,-3.97517,-5.17551],'cal/mol/K','+|-',[4.61424,5.42733,5.28994,4.70443,4.53817,4.47437,4.51385]),
        H298 = (104.798,'kcal/mol','+|-',10.4943),
        S298 = (2.35076,'cal/mol/K','+|-',5.97879),
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
        Cpdata = ([3.46227,-0.0228981,-3.08964,-4.60546,-6.13241,-7.54823,-7.08454],'cal/mol/K','+|-',[6.94463,8.06595,8.33769,9.31383,9.24106,8.22138,5.844]),
        H298 = (119.444,'kcal/mol','+|-',21.624),
        S298 = (0.162322,'cal/mol/K','+|-',8.68442),
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
        Cpdata = ([-0.051398,-2.37829,-4.12289,-5.05095,-5.73872,-6.72573,-8.66385],'cal/mol/K','+|-',[4.92311,4.70186,4.61589,4.63455,4.8895,5.56706,5.65932]),
        H298 = (97.2452,'kcal/mol','+|-',13.6464),
        S298 = (5.11324,'cal/mol/K','+|-',8.06937),
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
        Cpdata = ([0.220186,-2.21114,-3.9219,-4.78588,-5.17067,-5.77561,-8.6166],'cal/mol/K','+|-',[5.16758,4.85227,4.65223,4.61214,4.47996,4.50765,6.63342]),
        H298 = (100.196,'kcal/mol','+|-',9.68392),
        S298 = (3.17878,'cal/mol/K','+|-',4.5186),
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
        Cpdata = ([-1.87993,-3.58643,-4.70442,-5.04245,-5.01685,-5.07958,-5.55957],'cal/mol/K','+|-',[9.88536,10.379,10.2694,9.78815,8.47622,7.83928,6.41159]),
        H298 = (97.8357,'kcal/mol','+|-',43.0439),
        S298 = (1.7034,'cal/mol/K','+|-',9.91653),
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
        Cpdata = ([-1.31489,-1.34492,-1.67482,-1.87416,-2.26467,-2.65897,-3.90774],'cal/mol/K','+|-',[4.59971,4.51881,4.5532,4.55318,4.52505,4.53962,5.24857]),
        H298 = (85.6225,'kcal/mol','+|-',55.0685),
        S298 = (-1.17085,'cal/mol/K','+|-',4.61197),
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
        Cpdata = ([-1.79998,-1.3025,-1.62796,-1.76416,-2.10899,-2.65152,-3.26679],'cal/mol/K','+|-',[4.63144,4.64058,4.76626,4.75714,4.63552,4.68976,4.47729]),
        H298 = (51.042,'kcal/mol','+|-',12.4035),
        S298 = (-1.69887,'cal/mol/K','+|-',4.62006),
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
        Cpdata = ([0.65336,-4.13167,-5.99507,-6.35797,-6.18668,-6.16474,-6.4485],'cal/mol/K','+|-',[6.85439,13.2967,12.7257,11.4303,8.45204,6.62176,5.27909]),
        H298 = (117.194,'kcal/mol','+|-',21.1377),
        S298 = (2.28743,'cal/mol/K','+|-',13.711),
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
        Cpdata = ([-0.609732,-5.97289,-7.49748,-7.47675,-6.58075,-6.21224,-6.09698],'cal/mol/K','+|-',[4.71003,13.1848,13.3694,12.4875,9.66583,7.46441,5.37007]),
        H298 = (112.957,'kcal/mol','+|-',14.3007),
        S298 = (3.09628,'cal/mol/K','+|-',16.0089),
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
        Cpdata = ([-4.52811,-5.61589,-7.00445,-7.47515,-7.10839,-6.87412,-6.66544],'cal/mol/K','+|-',[13.9086,11.9572,10.5901,9.7745,9.14279,9.25866,7.24484]),
        H298 = (104.469,'kcal/mol','+|-',10.0735),
        S298 = (4.39785,'cal/mol/K','+|-',8.30766),
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
        Cpdata = ([-7.28608,-8.11942,-9.28225,-9.51217,-8.74527,-8.40202,-6.49686],'cal/mol/K','+|-',[15.0971,11.8596,9.74725,9.03812,9.91332,10.6937,8.51191]),
        H298 = (106.257,'kcal/mol','+|-',8.53495),
        S298 = (5.42651,'cal/mol/K','+|-',5.1338),
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
        Cpdata = ([-0.767594,-1.77374,-2.46792,-2.85461,-3.23313,-3.557,-4.25154],'cal/mol/K','+|-',[6.11431,6.54305,6.64587,6.49132,6.10263,5.90621,5.86901]),
        H298 = (93.5606,'kcal/mol','+|-',21.1301),
        S298 = (0.040085,'cal/mol/K','+|-',11.4843),
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
        Cpdata = ([-1.24428,-2.27575,-2.99744,-3.40512,-3.74835,-4.04749,-4.62711],'cal/mol/K','+|-',[6.16586,6.62098,6.85294,6.85088,6.6368,6.43052,6.42789]),
        H298 = (89.2682,'kcal/mol','+|-',17.5243),
        S298 = (-0.801502,'cal/mol/K','+|-',11.1065),
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
        Cpdata = ([-0.0618921,-0.818804,-1.51444,-1.98525,-2.58641,-3.02148,-3.72371],'cal/mol/K','+|-',[5.75371,5.84456,5.84077,5.81335,5.82263,5.70018,5.82567]),
        H298 = (90.2879,'kcal/mol','+|-',21.3937),
        S298 = (0.0858928,'cal/mol/K','+|-',11.4972),
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
        Cpdata = ([-0.045697,-0.804835,-1.51479,-1.99408,-2.5957,-3.02975,-3.71972],'cal/mol/K','+|-',[5.8238,5.85763,5.83938,5.82907,5.88756,5.78578,5.92783]),
        H298 = (89.3869,'kcal/mol','+|-',21.0832),
        S298 = (-0.0902519,'cal/mol/K','+|-',11.8254),
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
        Cpdata = ([1.19137,0.254889,-0.69253,-1.42061,-2.51399,-3.30214,-4.39864],'cal/mol/K','+|-',[6.71688,6.95562,6.65676,6.28094,5.58181,5.10647,4.88269]),
        H298 = (102.329,'kcal/mol','+|-',20.3216),
        S298 = (0.769386,'cal/mol/K','+|-',8.54563),
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
        Cpdata = ([0.847016,-0.306056,-1.2162,-1.84796,-2.76583,-3.40742,-4.35277],'cal/mol/K','+|-',[5.65839,5.15591,4.99434,4.88174,4.69477,4.54571,4.56294]),
        H298 = (103.026,'kcal/mol','+|-',22.5316),
        S298 = (1.50127,'cal/mol/K','+|-',8.45019),
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
        Cpdata = ([0.959343,0.133435,-0.671253,-1.34858,-2.41208,-3.22848,-4.60264],'cal/mol/K','+|-',[7.15882,5.72175,5.09822,4.91853,4.73434,4.58133,4.54808]),
        H298 = (110.13,'kcal/mol','+|-',13.0879),
        S298 = (-0.478222,'cal/mol/K','+|-',7.92338),
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
        Cpdata = ([2.22442,1.93772,0.87849,-0.138578,-1.75848,-2.98632,-4.53624],'cal/mol/K','+|-',[10.762,11.7116,11.0693,10.2965,8.59623,7.29957,6.32502]),
        H298 = (97.7603,'kcal/mol','+|-',8.43565),
        S298 = (-1.42626,'cal/mol/K','+|-',9.86342),
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
        Cpdata = ([-0.169403,-0.910807,-1.59702,-2.05142,-2.60388,-3.00251,-3.65183],'cal/mol/K','+|-',[5.71859,5.75049,5.77501,5.80973,5.94129,5.86118,6.0156]),
        H298 = (88.1593,'kcal/mol','+|-',19.6707),
        S298 = (-0.176216,'cal/mol/K','+|-',12.1529),
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
        Cpdata = ([-0.202012,-0.981293,-1.68465,-2.1279,-2.62851,-2.9744,-3.52845],'cal/mol/K','+|-',[5.81997,5.84095,5.86966,5.92158,6.08816,6.00225,6.12849]),
        H298 = (86.9414,'kcal/mol','+|-',19.4895),
        S298 = (-0.551942,'cal/mol/K','+|-',12.549),
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
        Cpdata = ([-0.728399,-1.48636,-2.13524,-2.4934,-2.81187,-2.92463,-3.10108],'cal/mol/K','+|-',[5.63773,5.51545,5.62766,5.84877,6.26705,6.33085,6.61023]),
        H298 = (82.943,'kcal/mol','+|-',17.577),
        S298 = (-1.57016,'cal/mol/K','+|-',11.7588),
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
        Cpdata = ([-1.1542,-1.85562,-2.38783,-2.55599,-2.55997,-2.44319,-2.29978],'cal/mol/K','+|-',[5.63752,5.49218,5.76732,6.189,6.73352,6.63042,6.412]),
        H298 = (78.8726,'kcal/mol','+|-',13.9408),
        S298 = (-3.0992,'cal/mol/K','+|-',12.0552),
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
        Cpdata = ([-1.08727,-1.74712,-2.21828,-2.38271,-2.37723,-2.20399,-2.45821],'cal/mol/K','+|-',[6.09878,5.87681,6.25692,6.92459,8.00826,8.00392,7.58695]),
        H298 = (83.7408,'kcal/mol','+|-',12.0039),
        S298 = (-2.14956,'cal/mol/K','+|-',14.703),
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
        Cpdata = ([-1.20528,-1.88922,-2.37973,-2.55849,-2.53916,-2.32085,-2.46526],'cal/mol/K','+|-',[6.17208,5.8984,6.28614,6.99394,8.18617,8.22755,7.83283]),
        H298 = (83.5035,'kcal/mol','+|-',12.0027),
        S298 = (-2.09709,'cal/mol/K','+|-',15.3568),
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
        Cpdata = ([-0.0995426,-1.63586,-2.97903,-3.91987,-4.84812,-4.8216,-4.67938],'cal/mol/K','+|-',[5.11099,4.83346,6.3678,7.93821,9.32588,8.63614,6.8142]),
        H298 = (86.3179,'kcal/mol','+|-',12.3531),
        S298 = (2.93453,'cal/mol/K','+|-',14.5736),
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
        Cpdata = ([-2.42943,-3.56868,-3.55825,-2.65439,-0.655071,0.881996,1.65325],'cal/mol/K','+|-',[10.3372,10.6212,9.16945,7.14226,4.53088,4.93046,7.93866]),
        H298 = (83.3408,'kcal/mol','+|-',10.0774),
        S298 = (-8.86119,'cal/mol/K','+|-',8.39915),
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
        Cpdata = ([-2.44742,-1.77702,-1.45503,-1.22803,-1.00835,-1.10409,-1.78383],'cal/mol/K','+|-',[5.52076,5.44362,4.89008,4.66844,4.62279,4.74062,6.1444]),
        H298 = (80.2387,'kcal/mol','+|-',10.8586),
        S298 = (-3.50978,'cal/mol/K','+|-',11.6263),
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
        Cpdata = ([-1.27792,-1.36807,-1.54883,-1.59392,-1.6834,-1.78535,-2.1],'cal/mol/K','+|-',[5.38969,4.99293,4.73633,4.60951,4.57406,4.89809,6.26479]),
        H298 = (75.9036,'kcal/mol','+|-',14.9919),
        S298 = (-3.9067,'cal/mol/K','+|-',8.07471),
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
        Cpdata = ([-0.675963,-0.623025,-0.936406,-1.21219,-1.73906,-2.37035,-3.59999],'cal/mol/K','+|-',[4.74013,4.63702,4.65471,4.59229,4.51078,4.50907,4.47784]),
        H298 = (79.4344,'kcal/mol','+|-',8.572),
        S298 = (-1.70784,'cal/mol/K','+|-',6.51093),
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
        Cpdata = ([0.346581,-0.625581,-1.35644,-1.40402,-1.52642,-1.55914,-1.60845],'cal/mol/K','+|-',[5.26936,4.69858,4.47557,4.56519,5.18165,5.96379,7.21524]),
        H298 = (74.2948,'kcal/mol','+|-',16.7489),
        S298 = (-6.59756,'cal/mol/K','+|-',11.8688),
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
        Cpdata = ([-1.11335,-2.4775,-3.43675,-3.7326,-3.66281,-3.39718,-2.30342],'cal/mol/K','+|-',[5.69467,5.56018,5.74307,6.23891,6.76253,6.36847,5.47239]),
        H298 = (77.3694,'kcal/mol','+|-',10.513),
        S298 = (-3.46742,'cal/mol/K','+|-',13.3042),
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
        Cpdata = ([-0.994271,-2.52437,-3.5547,-3.77654,-3.51657,-3.15527,-1.97088],'cal/mol/K','+|-',[6.07995,5.9268,6.14341,6.80197,7.43641,6.87627,5.60159]),
        H298 = (76.35,'kcal/mol','+|-',10.5864),
        S298 = (-4.41313,'cal/mol/K','+|-',14.78),
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
        Cpdata = ([1.16704,-0.428734,-1.50012,-1.4069,-0.936562,-1.02576,-0.820991],'cal/mol/K','+|-',[5.14725,4.73269,5.65562,6.73713,7.9376,7.69189,6.28837]),
        H298 = (80.7041,'kcal/mol','+|-',10.6479),
        S298 = (-11.7697,'cal/mol/K','+|-',9.92833),
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
        Cpdata = ([1.80035,-0.803013,-2.49492,-2.85539,-2.82548,-2.82583,-2.06737],'cal/mol/K','+|-',[4.83345,4.62975,4.49681,4.51917,4.51427,4.53479,4.66949]),
        H298 = (79.1012,'kcal/mol','+|-',9.76358),
        S298 = (-9.21091,'cal/mol/K','+|-',4.47281),
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
        Cpdata = ([0.42978,-0.481977,-1.44821,-2.32314,-3.49702,-4.23416,-5.28063],'cal/mol/K','+|-',[3.65639,3.84407,3.74904,3.4888,3.01453,2.92729,3.61001]),
        H298 = (91.4845,'kcal/mol','+|-',6.73692),
        S298 = (2.58881,'cal/mol/K','+|-',3.59561),
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
        Cpdata = ([0.909108,-0.0555224,-1.18086,-2.19687,-3.54552,-4.3907,-5.59307],'cal/mol/K','+|-',[3.00535,3.49086,3.764,3.62451,3.06384,2.84698,3.47941]),
        H298 = (91.8337,'kcal/mol','+|-',7.30914),
        S298 = (2.76837,'cal/mol/K','+|-',3.7029),
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
        Cpdata = ([0.816929,-0.540824,-1.87686,-2.858,-3.85118,-4.42292,-5.16486],'cal/mol/K','+|-',[3.05837,3.1835,3.07228,2.94318,2.82843,2.87947,3.08763]),
        H298 = (89.2849,'kcal/mol','+|-',5.73616),
        S298 = (2.18613,'cal/mol/K','+|-',2.88299),
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
        Cpdata = ([0.777069,-0.0418674,-0.846551,-1.44807,-2.28746,-3.06696,-4.32336],'cal/mol/K','+|-',[5.71676,6.0455,6.02932,5.90855,5.78623,5.43373,4.79865]),
        H298 = (95.0372,'kcal/mol','+|-',11.4443),
        S298 = (1.34194,'cal/mol/K','+|-',13.4975),
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
        Cpdata = ([2.93627,3.19709,2.48495,1.82779,0.992816,-0.555012,-3.4287],'cal/mol/K','+|-',[6.32357,8.13418,8.52007,8.3893,8.13951,7.62999,5.48794]),
        H298 = (96.3165,'kcal/mol','+|-',14.5017),
        S298 = (-6.24029,'cal/mol/K','+|-',12.1348),
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
        Cpdata = ([2.79002,3.74786,3.49557,3.02865,2.45891,0.989223,-2.55155],'cal/mol/K','+|-',[7.71115,10.2494,10.0335,9.28176,7.80493,6.26113,4.66578]),
        H298 = (92.9006,'kcal/mol','+|-',8.41403),
        S298 = (-8.17667,'cal/mol/K','+|-',13.5837),
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
        Cpdata = ([0.140113,-0.782345,-1.53157,-2.03309,-2.74486,-3.34891,-4.32544],'cal/mol/K','+|-',[4.86199,4.76302,4.86489,4.91839,4.91663,4.87536,4.7278]),
        H298 = (96.3913,'kcal/mol','+|-',9.95471),
        S298 = (3.23971,'cal/mol/K','+|-',13.7604),
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
        Cpdata = ([0.277433,-1.46011,-2.68043,-3.29472,-3.85663,-4.29931,-4.58128],'cal/mol/K','+|-',[4.92949,4.91055,4.71601,4.70362,4.96315,5.11316,5.38878]),
        H298 = (98.4371,'kcal/mol','+|-',13.795),
        S298 = (7.83617,'cal/mol/K','+|-',26.4571),
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
        Cpdata = ([1.16958,-0.708306,-2.31914,-2.84176,-2.93116,-3.29449,-3.56501],'cal/mol/K','+|-',[4.47269,4.77811,4.90873,4.76546,4.47447,4.67397,5.40662]),
        H298 = (101.604,'kcal/mol','+|-',18.8519),
        S298 = (12.3441,'cal/mol/K','+|-',39.2512),
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
        Cpdata = ([-0.0234442,-0.366425,-0.929549,-1.41598,-2.23109,-2.98033,-4.46167],'cal/mol/K','+|-',[4.86756,4.78315,4.69434,4.64186,4.55576,4.51684,4.47932]),
        H298 = (96.5773,'kcal/mol','+|-',9.58416),
        S298 = (0.903284,'cal/mol/K','+|-',5.65304),
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
        Cpdata = ([0.0398085,-0.213236,-0.692153,-1.15994,-2.00776,-2.79449,-4.41764],'cal/mol/K','+|-',[5.17204,4.98765,4.76438,4.64972,4.52247,4.48218,4.48131]),
        H298 = (97.5162,'kcal/mol','+|-',10.4389),
        S298 = (0.879876,'cal/mol/K','+|-',6.48757),
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
        Cpdata = ([0.245506,-0.75464,-1.34042,-1.76159,-2.46355,-3.00955,-3.90446],'cal/mol/K','+|-',[4.064,2.84968,2.96806,3.23206,3.61361,3.65551,3.10623]),
        H298 = (94.814,'kcal/mol','+|-',3.4352),
        S298 = (2.37387,'cal/mol/K','+|-',3.58509),
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
        Cpdata = ([1.51019,0.412858,-0.608683,-1.47985,-2.70451,-3.59126,-4.80511],'cal/mol/K','+|-',[6.91382,6.49521,5.85412,5.32996,4.81602,4.54341,4.50697]),
        H298 = (89.4876,'kcal/mol','+|-',8.5955),
        S298 = (-0.215579,'cal/mol/K','+|-',6.36782),
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
        Cpdata = ([0.72422,-0.215739,-1.12588,-1.86918,-2.9213,-3.62389,-4.63335],'cal/mol/K','+|-',[5.93486,5.32966,4.80435,4.56726,4.48261,4.47685,4.47447]),
        H298 = (89.1015,'kcal/mol','+|-',8.35955),
        S298 = (0.655298,'cal/mol/K','+|-',4.8954),
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
        Cpdata = ([2.88565,1.5129,0.296419,-0.798528,-2.32512,-3.53417,-5.1057],'cal/mol/K','+|-',[8.97879,8.80321,7.7322,6.71126,5.50019,4.72781,4.47532]),
        H298 = (90.8498,'kcal/mol','+|-',8.35286),
        S298 = (-1.73961,'cal/mol/K','+|-',7.97475),
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
        Cpdata = ([0.523703,0.151968,-0.491426,-1.16881,-2.31641,-3.2248,-4.67126],'cal/mol/K','+|-',[4.73439,4.65789,4.60924,4.61333,4.60587,4.5621,4.494]),
        H298 = (97.5787,'kcal/mol','+|-',8.82004),
        S298 = (2.67683,'cal/mol/K','+|-',4.84592),
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
        Cpdata = ([0.00464884,-0.283026,-0.864004,-1.54084,-2.65126,-3.49737,-4.78336],'cal/mol/K','+|-',[4.47228,4.47229,4.47253,4.48466,4.53317,4.51509,4.49654]),
        H298 = (96.6058,'kcal/mol','+|-',8.41934),
        S298 = (2.15688,'cal/mol/K','+|-',4.77328),
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
        Cpdata = ([-0.570278,-1.47929,-2.08468,-2.41372,-2.83653,-3.10854,-3.66169],'cal/mol/K','+|-',[5.18722,6.42622,6.62475,6.29501,5.44538,4.837,4.68722]),
        H298 = (103.092,'kcal/mol','+|-',13.075),
        S298 = (2.29052,'cal/mol/K','+|-',6.8736),
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
        Cpdata = ([-1.33435,-2.90591,-3.49251,-3.57869,-3.53128,-3.37511,-3.34408],'cal/mol/K','+|-',[4.63412,5.34146,5.64593,5.56779,5.13017,4.88509,5.0388]),
        H298 = (109.309,'kcal/mol','+|-',10.394),
        S298 = (2.06855,'cal/mol/K','+|-',9.85667),
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
        Cpdata = ([-2.06089,-3.28198,-4.02167,-4.38575,-4.55083,-4.7561,-5.25104],'cal/mol/K','+|-',[5.91701,6.38301,6.7612,6.83736,6.7023,6.53577,6.54119]),
        H298 = (88.3285,'kcal/mol','+|-',12.942),
        S298 = (-1.41438,'cal/mol/K','+|-',10.7216),
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
        Cpdata = ([-3.04555,-3.88877,-4.21367,-4.22978,-3.92261,-3.82266,-3.9075],'cal/mol/K','+|-',[6.01504,7.09817,7.82924,7.86036,7.32336,7.03492,6.84782]),
        H298 = (92.555,'kcal/mol','+|-',16.0753),
        S298 = (0.552706,'cal/mol/K','+|-',11.6774),
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
        Cpdata = ([-5.14094,-7.27987,-8.0228,-7.9587,-6.9845,-6.25812,-5.2254],'cal/mol/K','+|-',[5.86273,6.92192,8.0566,8.07823,6.73597,5.81549,5.48242]),
        H298 = (94.174,'kcal/mol','+|-',15.6627),
        S298 = (4.16758,'cal/mol/K','+|-',9.34579),
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
        Cpdata = ([-4.90352,-6.266,-6.75251,-6.71633,-6.05892,-5.63819,-5.13005],'cal/mol/K','+|-',[6.71931,6.92088,8.13433,8.29317,6.91943,6.08614,6.10537]),
        H298 = (92.02,'kcal/mol','+|-',12.2485),
        S298 = (3.29016,'cal/mol/K','+|-',10.3254),
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
        Cpdata = ([-3.17456,-5.75467,-7.26377,-7.57673,-6.80541,-6.43295,-6.05082],'cal/mol/K','+|-',[6.63463,9.52004,11.8046,11.8072,9.29077,7.50649,7.33892]),
        H298 = (96.9731,'kcal/mol','+|-',8.3631),
        S298 = (4.70761,'cal/mol/K','+|-',14.901),
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
        Cpdata = ([-5.67514,-9.56109,-10.881,-10.7541,-9.06706,-7.65296,-5.43993],'cal/mol/K','+|-',[4.51561,4.78407,4.85579,4.73724,4.52271,4.48458,4.78653]),
        H298 = (102.85,'kcal/mol','+|-',10.5885),
        S298 = (6.14178,'cal/mol/K','+|-',8.69068),
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
        Cpdata = ([-2.21863,-3.05058,-3.40222,-3.36652,-3.02067,-2.98148,-3.16157],'cal/mol/K','+|-',[5.64575,5.3935,5.53271,5.84857,6.53553,7.06384,7.60863]),
        H298 = (88.3893,'kcal/mol','+|-',16.5462),
        S298 = (-0.330593,'cal/mol/K','+|-',13.1389),
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
        Cpdata = ([-2.21908,-3.14934,-3.52682,-3.41537,-2.86774,-2.74777,-2.88166],'cal/mol/K','+|-',[5.97288,5.6385,5.80329,6.2211,7.03473,7.63608,8.26794]),
        H298 = (88.4666,'kcal/mol','+|-',19.9648),
        S298 = (-0.0295593,'cal/mol/K','+|-',14.8177),
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
        Cpdata = ([-2.09284,-3.18459,-3.76938,-3.77936,-3.37457,-3.39852,-3.60595],'cal/mol/K','+|-',[6.14526,5.81557,5.7958,6.03091,6.61617,6.86094,7.38897]),
        H298 = (89.3536,'kcal/mol','+|-',19.9129),
        S298 = (-2.12074,'cal/mol/K','+|-',8.30222),
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
        Cpdata = ([-2.53642,-3.78296,-4.39325,-4.36821,-3.8155,-3.70128,-3.62629],'cal/mol/K','+|-',[5.81863,4.76049,4.59871,5.12041,6.42445,7.02595,7.88343]),
        H298 = (90.8155,'kcal/mol','+|-',17.5431),
        S298 = (-1.92244,'cal/mol/K','+|-',8.83584),
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
        Cpdata = ([-2.86713,-3.93289,-4.55932,-4.83319,-4.80008,-4.77028,-4.66281],'cal/mol/K','+|-',[5.8564,4.50584,4.65373,4.7967,4.50082,4.47247,4.48701]),
        H298 = (87.4045,'kcal/mol','+|-',9.38992),
        S298 = (0.162368,'cal/mol/K','+|-',5.01829),
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
        Cpdata = ([-0.915125,-2.90452,-4.21816,-4.61601,-4.40136,-4.59278,-5.10588],'cal/mol/K','+|-',[5.2764,4.48486,4.73711,4.97698,4.76985,4.48536,4.60449]),
        H298 = (95.4246,'kcal/mol','+|-',9.4143),
        S298 = (-1.88354,'cal/mol/K','+|-',4.48173),
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
        Cpdata = ([-2.39926,-2.05703,-1.95175,-2.12378,-2.49677,-2.88302,-3.8559],'cal/mol/K','+|-',[5.11788,5.39354,5.83856,5.95648,6.21122,6.56344,6.94419]),
        H298 = (96.7478,'kcal/mol','+|-',13.0975),
        S298 = (-1.41592,'cal/mol/K','+|-',10.1489),
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
        Cpdata = ([-2.73814,-2.08661,-1.83852,-2.00508,-2.34533,-2.79612,-4.19865],'cal/mol/K','+|-',[5.77463,6.9983,7.14554,6.35194,5.02063,4.53892,4.48241]),
        H298 = (97.0049,'kcal/mol','+|-',8.4366),
        S298 = (-0.556954,'cal/mol/K','+|-',5.22064),
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
        Cpdata = ([-1.8502,-3.15214,-3.98059,-4.41912,-4.68526,-4.95583,-5.53852],'cal/mol/K','+|-',[5.82942,6.22333,6.55207,6.6411,6.56736,6.38593,6.35658]),
        H298 = (87.2348,'kcal/mol','+|-',11.1785),
        S298 = (-1.83528,'cal/mol/K','+|-',10.3927),
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
        Cpdata = ([-2.21668,-3.8892,-4.9312,-5.41478,-5.5456,-5.68943,-6.88567],'cal/mol/K','+|-',[5.2865,5.70339,6.1819,6.3737,6.2063,6.09375,7.02117]),
        H298 = (85.9521,'kcal/mol','+|-',13.3998),
        S298 = (-0.90054,'cal/mol/K','+|-',9.87287),
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
        Cpdata = ([-2.16442,-3.57388,-4.47583,-4.91329,-5.07285,-5.24348,-6.55252],'cal/mol/K','+|-',[5.33366,5.26487,5.42617,5.4945,5.29951,5.28309,6.9358]),
        H298 = (86.5376,'kcal/mol','+|-',9.21749),
        S298 = (-1.95691,'cal/mol/K','+|-',7.62658),
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
        Cpdata = ([0.420485,-1.05945,-2.02591,-2.65448,-3.50857,-3.69887,-4.14578],'cal/mol/K','+|-',[4.99577,4.76764,4.7329,4.72373,4.9317,4.98288,5.08451]),
        H298 = (88.9749,'kcal/mol','+|-',10.3731),
        S298 = (-7.92977,'cal/mol/K','+|-',4.64158),
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
        Cpdata = ([-0.221175,-1.43598,-2.15404,-2.57625,-3.12374,-3.20909,-3.45319],'cal/mol/K','+|-',[4.47593,4.6966,4.94031,4.94776,5.0089,4.88886,4.4936]),
        H298 = (90.7335,'kcal/mol','+|-',8.43865),
        S298 = (-7.7829,'cal/mol/K','+|-',4.75087),
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
        Cpdata = ([-2.48094,-3.88176,-4.77582,-5.18988,-5.26439,-5.43262,-6.84722],'cal/mol/K','+|-',[5.02293,4.98073,5.19387,5.32493,5.22967,5.21003,6.92327]),
        H298 = (86.3297,'kcal/mol','+|-',9.03638),
        S298 = (-1.22554,'cal/mol/K','+|-',6.49828),
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
        Cpdata = ([-2.53503,-4.6302,-5.79748,-6.20181,-6.03647,-5.99759,-7.83074],'cal/mol/K','+|-',[5.23015,4.72787,4.69998,4.91884,4.97891,4.96176,7.4771]),
        H298 = (85.5843,'kcal/mol','+|-',8.82798),
        S298 = (-0.312998,'cal/mol/K','+|-',6.42489),
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
        Cpdata = ([-2.81238,-4.65478,-5.85038,-6.4489,-6.27804,-6.36579,-10.3091],'cal/mol/K','+|-',[5.08672,4.7924,4.65507,4.58815,4.50788,4.49179,4.52297]),
        H298 = (85.9716,'kcal/mol','+|-',8.51611),
        S298 = (-1.57779,'cal/mol/K','+|-',7.57046),
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
        Cpdata = ([-2.33332,-4.61232,-5.75901,-6.02212,-5.86079,-5.7298,-6.02831],'cal/mol/K','+|-',[5.51721,4.76013,4.80667,5.25714,5.43072,5.35589,7.16985]),
        H298 = (85.4133,'kcal/mol','+|-',9.17735),
        S298 = (0.606848,'cal/mol/K','+|-',4.92713),
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
        Cpdata = ([-2.15217,-4.47354,-5.61133,-5.8838,-5.70755,-5.57199,-6.11494],'cal/mol/K','+|-',[5.80769,4.80541,4.86158,5.49775,5.72015,5.61352,8.04302]),
        H298 = (85.8025,'kcal/mol','+|-',8.77242),
        S298 = (0.655537,'cal/mol/K','+|-',5.10248),
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
        Cpdata = ([-1.39373,-3.05349,-4.28152,-5.04961,-5.1641,-5.52529,-7.91278],'cal/mol/K','+|-',[4.84602,4.48582,4.59162,4.76276,4.73699,4.833,8.60669]),
        H298 = (88.6719,'kcal/mol','+|-',8.57057),
        S298 = (-3.9669,'cal/mol/K','+|-',7.75697),
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
        Cpdata = ([-1.81269,-3.30216,-4.42632,-5.10073,-5.51581,-6.13912,-5.75275],'cal/mol/K','+|-',[4.69369,4.82384,5.15284,5.54135,5.84562,6.18723,4.88526]),
        H298 = (89.0312,'kcal/mol','+|-',11.2755),
        S298 = (-1.34893,'cal/mol/K','+|-',8.15634),
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
        Cpdata = ([-2.59557,-3.26369,-3.74939,-4.01401,-4.32787,-4.56897,-5.2427],'cal/mol/K','+|-',[4.86904,5.10616,5.27417,5.19921,5.09711,5.0381,6.0478]),
        H298 = (86.0563,'kcal/mol','+|-',8.41318),
        S298 = (-1.14205,'cal/mol/K','+|-',5.39002),
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
        Cpdata = ([-2.76123,-3.85244,-4.42735,-4.54191,-4.68758,-4.97157,-5.59302],'cal/mol/K','+|-',[5.03794,4.82196,4.89255,5.10165,5.20674,5.05545,6.6375]),
        H298 = (85.9277,'kcal/mol','+|-',8.46393),
        S298 = (-0.263894,'cal/mol/K','+|-',4.48938),
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
        Cpdata = ([-3.03594,-3.97919,-4.45405,-4.49906,-4.56154,-4.85025,-5.68499],'cal/mol/K','+|-',[4.99025,4.90497,5.06069,5.34427,5.43973,5.23556,7.35734]),
        H298 = (85.7972,'kcal/mol','+|-',8.422),
        S298 = (-0.221331,'cal/mol/K','+|-',4.48933),
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
        Cpdata = ([-3.35999,-4.10668,-4.38004,-4.33821,-4.37806,-4.70793,-5.87913],'cal/mol/K','+|-',[4.95183,5.18262,5.49833,5.90253,6.03473,5.7394,9.05803]),
        H298 = (85.8875,'kcal/mol','+|-',8.42008),
        S298 = (-0.26331,'cal/mol/K','+|-',4.49554),
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
        Cpdata = ([-3.85511,-4.49669,-5.04716,-5.3607,-5.06625,-5.05116,-9.16973],'cal/mol/K','+|-',[4.51807,4.7085,4.98366,5.30385,5.62193,5.60367,4.94813]),
        H298 = (86.8657,'kcal/mol','+|-',8.35225),
        S298 = (-2.96761,'cal/mol/K','+|-',7.42419),
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
        Cpdata = ([-2.42196,-5.12797,-6.72019,-7.38492,-7.40287,-7.44136,-8.1945],'cal/mol/K','+|-',[5.19204,6.83528,7.80474,8.18518,8.18752,7.89697,7.05243]),
        H298 = (82.76,'kcal/mol','+|-',26.3896),
        S298 = (3.24948,'cal/mol/K','+|-',13.4744),
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
        Cpdata = ([-1.89762,-3.9501,-5.37428,-5.90694,-5.70241,-5.7315,-7.10786],'cal/mol/K','+|-',[4.96592,5.98185,7.02656,7.2193,6.31422,5.67273,6.62833]),
        H298 = (89.9078,'kcal/mol','+|-',10.7541),
        S298 = (0.0546784,'cal/mol/K','+|-',9.14137),
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
        Cpdata = ([-1.6074,-3.46037,-4.8543,-5.39443,-5.28592,-5.45818,-7.25208],'cal/mol/K','+|-',[4.8957,5.88623,7.20788,7.47128,6.47045,5.85215,7.16648]),
        H298 = (88.7732,'kcal/mol','+|-',9.82941),
        S298 = (-1.05738,'cal/mol/K','+|-',8.47201),
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
        Cpdata = ([-2.42582,-4.73269,-6.26891,-6.72181,-6.21839,-6.08635,-7.30841],'cal/mol/K','+|-',[4.49631,6.16783,9.15577,9.96338,8.46062,7.4964,9.72382]),
        H298 = (89.4812,'kcal/mol','+|-',10.0329),
        S298 = (-0.837014,'cal/mol/K','+|-',13.1111),
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
        Cpdata = ([-3.73281,-8.07266,-10.085,-11.0799,-11.654,-11.716,-10.9111],'cal/mol/K','+|-',[4.88434,4.48101,4.60326,4.53864,4.5086,4.56079,4.47502]),
        H298 = (64.8907,'kcal/mol','+|-',8.35286),
        S298 = (11.2365,'cal/mol/K','+|-',4.54144),
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
        Cpdata = ([-1.69216,-2.83429,-3.57064,-3.98974,-4.31423,-4.63947,-4.95756],'cal/mol/K','+|-',[6.03634,6.34899,6.56109,6.59555,6.60454,6.42878,5.69577]),
        H298 = (87.7249,'kcal/mol','+|-',10.1403),
        S298 = (-2.23839,'cal/mol/K','+|-',10.5733),
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
        Cpdata = ([-1.57445,-2.80193,-3.60069,-4.05078,-4.41104,-4.7824,-5.14468],'cal/mol/K','+|-',[6.03335,6.41995,6.6617,6.70413,6.71572,6.4965,5.62248]),
        H298 = (87.9329,'kcal/mol','+|-',10.2476),
        S298 = (-2.47498,'cal/mol/K','+|-',9.86512),
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
        Cpdata = ([-1.20865,-2.56038,-3.43766,-3.93283,-4.3885,-4.74992,-5.16761],'cal/mol/K','+|-',[5.76638,5.69478,5.77713,6.06543,6.63801,6.75952,6.00142]),
        H298 = (88.1314,'kcal/mol','+|-',10.7969),
        S298 = (-3.10361,'cal/mol/K','+|-',9.68404),
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
        Cpdata = ([-0.74704,-2.43651,-3.54244,-4.10542,-4.46777,-4.96116,-5.99547],'cal/mol/K','+|-',[6.15951,5.93472,5.73731,5.72577,5.65626,5.5882,5.23227]),
        H298 = (87.2823,'kcal/mol','+|-',9.33031),
        S298 = (-5.1529,'cal/mol/K','+|-',8.34057),
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
        Cpdata = ([-0.839555,-2.92362,-4.17929,-4.91203,-5.34235,-6.11835,-6.89989],'cal/mol/K','+|-',[7.84526,6.90108,6.23149,5.83521,5.17495,4.98011,4.53061]),
        H298 = (85.9948,'kcal/mol','+|-',8.86929),
        S298 = (-3.95169,'cal/mol/K','+|-',9.32789),
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
        Cpdata = ([-1.0495,-2.59799,-3.5836,-4.23958,-4.72262,-5.41968,-6.71703],'cal/mol/K','+|-',[11.4411,9.50815,7.90993,6.96966,5.55593,4.94716,4.47533]),
        H298 = (87.1023,'kcal/mol','+|-',8.59045),
        S298 = (-3.77629,'cal/mol/K','+|-',14.7081),
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
        Cpdata = ([-0.62961,-3.24924,-4.77498,-5.58449,-5.96208,-6.81701,-7.08275],'cal/mol/K','+|-',[5.74809,5.54738,5.31505,5.13202,4.82978,4.7032,4.5843]),
        H298 = (84.8872,'kcal/mol','+|-',8.53289),
        S298 = (-4.12708,'cal/mol/K','+|-',4.92022),
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
        Cpdata = ([-0.069422,-1.06774,-1.88194,-2.14642,-2.28161,-2.7697,-4.1733],'cal/mol/K','+|-',[5.02143,4.86404,4.63585,4.56478,4.64433,4.53506,4.7054]),
        H298 = (87.647,'kcal/mol','+|-',9.54354),
        S298 = (-8.68267,'cal/mol/K','+|-',4.54397),
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
        Cpdata = ([-0.250049,-1.3633,-2.02738,-2.29873,-2.62385,-2.97436,-4.58846],'cal/mol/K','+|-',[5.44486,5.02208,4.74074,4.59539,4.5087,4.48646,4.4883]),
        H298 = (88.9544,'kcal/mol','+|-',8.4487),
        S298 = (-8.45105,'cal/mol/K','+|-',4.47301),
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
        Cpdata = ([-1.3013,-3.15579,-4.35382,-4.98894,-5.48781,-5.6097,-6.61177],'cal/mol/K','+|-',[5.34083,5.21098,4.96474,4.76483,4.60346,4.55035,4.63896]),
        H298 = (88.6344,'kcal/mol','+|-',9.37447),
        S298 = (-3.22474,'cal/mol/K','+|-',5.76844),
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
        Cpdata = ([-0.997151,-2.89454,-4.21372,-4.95929,-5.56874,-5.709,-6.30183],'cal/mol/K','+|-',[5.90158,5.71581,5.36901,5.03847,4.7145,4.60161,4.55351]),
        H298 = (87.4388,'kcal/mol','+|-',8.46735),
        S298 = (-4.26409,'cal/mol/K','+|-',4.54131),
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
        Cpdata = ([-0.952853,-2.47806,-3.6041,-4.26067,-4.93284,-5.37863,-5.48436],'cal/mol/K','+|-',[5.52427,5.70549,6.02012,6.52198,7.46063,7.52441,6.22165]),
        H298 = (89.0225,'kcal/mol','+|-',10.6474),
        S298 = (-1.94562,'cal/mol/K','+|-',11.0634),
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
        Cpdata = ([-1.32098,-2.69221,-3.53032,-3.76816,-3.93005,-4.23419,-4.3688],'cal/mol/K','+|-',[6.00587,5.6546,5.40694,5.38749,5.47048,5.45066,4.94914]),
        H298 = (90.1538,'kcal/mol','+|-',11.4312),
        S298 = (-3.05909,'cal/mol/K','+|-',8.35059),
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
        Cpdata = ([0.0315041,-1.67673,-2.83323,-3.28038,-3.78178,-4.36553,-4.61935],'cal/mol/K','+|-',[4.84158,5.12355,5.32396,5.50436,5.61122,5.62482,4.99444]),
        H298 = (91.4381,'kcal/mol','+|-',8.74285),
        S298 = (-4.79047,'cal/mol/K','+|-',5.46222),
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
        Cpdata = ([0.21734,-1.76427,-3.07831,-3.63683,-4.2606,-4.87079,-4.95493],'cal/mol/K','+|-',[4.86487,5.30377,5.43363,5.5084,5.40376,5.35821,4.85689]),
        H298 = (91.0879,'kcal/mol','+|-',8.68285),
        S298 = (-4.40991,'cal/mol/K','+|-',5.40855),
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
        Cpdata = ([-2.57587,-3.52199,-4.07912,-4.28979,-4.43617,-4.59853,-4.49378],'cal/mol/K','+|-',[6.61229,6.04901,5.64983,5.64467,5.60088,5.18634,4.74053]),
        H298 = (88.0613,'kcal/mol','+|-',8.8224),
        S298 = (-1.0825,'cal/mol/K','+|-',11.2613),
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
        Cpdata = ([-0.601454,-2.27364,-3.67452,-4.73079,-5.89005,-6.47105,-6.54922],'cal/mol/K','+|-',[5.05827,5.89557,6.76098,7.57114,8.82344,8.79972,6.68849]),
        H298 = (88.2571,'kcal/mol','+|-',10.2481),
        S298 = (-0.882772,'cal/mol/K','+|-',13.4093),
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
        Cpdata = ([0.316345,-0.26261,-1.00211,-1.5363,-1.91361,-2.61716,-4.13153],'cal/mol/K','+|-',[5.66442,6.28166,6.70547,7.11038,7.27319,6.93138,5.2921]),
        H298 = (85.0612,'kcal/mol','+|-',8.5901),
        S298 = (-8.90372,'cal/mol/K','+|-',8.57867),
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
        Cpdata = ([-0.783653,-2.94005,-4.68839,-6.08568,-7.71306,-8.27177,-7.6141],'cal/mol/K','+|-',[4.65236,5.11037,5.87916,6.54823,7.62156,7.85758,6.54301]),
        H298 = (88.699,'kcal/mol','+|-',10.3363),
        S298 = (2.60209,'cal/mol/K','+|-',8.64122),
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
        Cpdata = ([-0.625897,-2.87698,-4.74428,-6.25952,-8.0949,-8.67377,-7.87065],'cal/mol/K','+|-',[4.58764,5.27824,6.24516,6.9797,7.97038,8.22316,6.85795]),
        H298 = (88.9957,'kcal/mol','+|-',10.094),
        S298 = (3.14263,'cal/mol/K','+|-',8.87484),
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
        Cpdata = ([-0.693848,-2.00513,-3.29653,-4.4703,-5.94472,-6.41417,-6.14132],'cal/mol/K','+|-',[4.75796,4.77014,4.53683,4.48164,5.05163,4.99152,4.54079]),
        H298 = (86.724,'kcal/mol','+|-',8.75345),
        S298 = (0.790969,'cal/mol/K','+|-',6.64675),
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
        Cpdata = ([-2.39873,-2.91431,-2.8934,-2.90053,-2.91836,-2.91114,-3.39245],'cal/mol/K','+|-',[5.57169,5.68456,5.37842,5.01799,4.62617,4.61322,5.00066]),
        H298 = (86.2612,'kcal/mol','+|-',12.3609),
        S298 = (-3.6217,'cal/mol/K','+|-',5.41298),
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
        Cpdata = ([-2.34387,-3.23273,-3.32769,-3.36745,-3.29147,-3.09213,-3.16038],'cal/mol/K','+|-',[6.14857,6.41806,5.93165,5.26863,4.61343,4.73002,5.52304]),
        H298 = (84.3324,'kcal/mol','+|-',12.5036),
        S298 = (-4.31078,'cal/mol/K','+|-',4.833),
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
        Cpdata = ([-3.69419,-4.61826,-4.46863,-4.13392,-3.4398,-2.702,-1.85699],'cal/mol/K','+|-',[5.48651,6.14049,5.82058,5.13904,4.47358,4.80929,4.91784]),
        H298 = (88.146,'kcal/mol','+|-',9.11346),
        S298 = (-4.4025,'cal/mol/K','+|-',5.12525),
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
        Cpdata = ([-0.993548,-1.84721,-2.18674,-2.60098,-3.14314,-3.48227,-4.46377],'cal/mol/K','+|-',[5.84285,5.92907,5.55394,5.24081,4.84626,4.64271,4.48835]),
        H298 = (80.5189,'kcal/mol','+|-',9.13855),
        S298 = (-4.21905,'cal/mol/K','+|-',4.86528),
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
        Cpdata = ([-1.75028,-2.72606,-3.38861,-3.79821,-4.10323,-4.57149,-4.9639],'cal/mol/K','+|-',[6.50664,7.15501,7.31378,7.05952,6.50122,6.00928,5.17516]),
        H298 = (87.9417,'kcal/mol','+|-',9.94493),
        S298 = (-2.5577,'cal/mol/K','+|-',9.59203),
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
        Cpdata = ([-2.05648,-2.28097,-2.59827,-2.96542,-3.34023,-3.91448,-4.7271],'cal/mol/K','+|-',[6.34304,7.98614,8.33617,7.98908,7.00762,6.33478,5.32497]),
        H298 = (87.2737,'kcal/mol','+|-',9.84208),
        S298 = (-4.16128,'cal/mol/K','+|-',8.13142),
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
        Cpdata = ([-2.26195,-2.20687,-2.45709,-2.84744,-3.32608,-3.93967,-4.76709],'cal/mol/K','+|-',[6.2661,8.53954,9.01549,8.65699,7.55216,6.77545,5.54809]),
        H298 = (86.6905,'kcal/mol','+|-',9.52956),
        S298 = (-4.07969,'cal/mol/K','+|-',8.34026),
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
        Cpdata = ([-1.94972,-1.53371,-1.77036,-2.22941,-2.86659,-3.63966,-4.86622],'cal/mol/K','+|-',[7.07502,10.2832,11.0066,10.5486,9.04569,7.96652,5.92535]),
        H298 = (86.4246,'kcal/mol','+|-',10.147),
        S298 = (-5.41117,'cal/mol/K','+|-',8.04063),
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
        Cpdata = ([-4.96771,-6.18719,-6.55567,-6.59934,-6.2301,-6.18401,-6.13207],'cal/mol/K','+|-',[4.47231,4.49924,4.55151,4.54216,4.50618,4.48734,4.48237]),
        H298 = (89.7026,'kcal/mol','+|-',8.78354),
        S298 = (-2.5111,'cal/mol/K','+|-',5.14299),
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
        Cpdata = ([-0.225152,1.12542,0.964111,0.267687,-0.944584,-2.18574,-4.14288],'cal/mol/K','+|-',[4.49192,7.64431,9.39789,9.77033,9.24498,8.89422,6.79847]),
        H298 = (85.4954,'kcal/mol','+|-',9.57071),
        S298 = (-7.06836,'cal/mol/K','+|-',7.7984),
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
        Cpdata = ([-1.18324,-2.59586,-3.19829,-3.46684,-3.40036,-3.80742,-4.55714],'cal/mol/K','+|-',[7.84099,6.7602,6.03162,5.51071,4.9657,4.58877,4.4724]),
        H298 = (90.7891,'kcal/mol','+|-',8.37045),
        S298 = (-4.50802,'cal/mol/K','+|-',9.52075),
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
        Cpdata = ([-0.238655,-2.17353,-3.31364,-3.89613,-4.34361,-4.9965,-5.33345],'cal/mol/K','+|-',[6.36485,5.84129,5.313,5.0071,4.85041,4.78198,4.69923]),
        H298 = (86.4376,'kcal/mol','+|-',8.65838),
        S298 = (-2.00366,'cal/mol/K','+|-',6.44589),
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
        Cpdata = ([-0.75698,-2.64491,-3.7075,-4.24788,-4.58571,-5.11243,-5.30046],'cal/mol/K','+|-',[6.1302,5.56641,5.06272,4.75678,4.75917,4.81466,4.75088]),
        H298 = (86.555,'kcal/mol','+|-',8.70955),
        S298 = (-1.14442,'cal/mol/K','+|-',4.97874),
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
        Cpdata = ([-0.315668,-2.29696,-3.51478,-4.25622,-4.88706,-5.49645,-5.49861],'cal/mol/K','+|-',[6.1843,5.60519,5.14954,4.84776,4.5947,4.50652,4.73083]),
        H298 = (86.1153,'kcal/mol','+|-',8.5284),
        S298 = (-1.23864,'cal/mol/K','+|-',5.11341),
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
        Cpdata = ([1.49633,-0.857007,-2.42511,-3.44949,-4.43155,-5.30203,-4.95953],'cal/mol/K','+|-',[4.71179,4.59061,4.53081,4.48198,4.47358,4.50641,4.73477]),
        H298 = (85.8783,'kcal/mol','+|-',8.77869),
        S298 = (-1.69231,'cal/mol/K','+|-',5.92496),
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
        Cpdata = ([-2.65098,-3.95507,-4.73452,-5.05309,-5.11389,-5.24049,-5.0053],'cal/mol/K','+|-',[6.61081,7.10867,7.22861,7.10893,7.05311,6.61123,5.57435]),
        H298 = (89.773,'kcal/mol','+|-',10.5832),
        S298 = (-0.478744,'cal/mol/K','+|-',13.5357),
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
        Cpdata = ([-0.930749,-1.66099,-2.34309,-2.70927,-2.83823,-3.3076,-3.79038],'cal/mol/K','+|-',[6.72696,5.76485,5.51378,5.43401,5.56251,5.85659,5.54709]),
        H298 = (87.2724,'kcal/mol','+|-',11.2005),
        S298 = (-6.01841,'cal/mol/K','+|-',7.89325),
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
        Cpdata = ([-4.12547,-5.92142,-6.78432,-7.06207,-7.06445,-6.89726,-6.04666],'cal/mol/K','+|-',[4.49077,4.95942,5.23166,5.1183,5.13871,4.83739,4.47843]),
        H298 = (90.8362,'kcal/mol','+|-',9.51359),
        S298 = (4.26954,'cal/mol/K','+|-',6.67135),
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
        Cpdata = ([-2.6333,-3.94266,-4.74055,-5.1035,-5.20921,-5.39742,-5.46872],'cal/mol/K','+|-',[5.76421,7.51299,8.58006,8.55087,7.90579,6.908,5.20337]),
        H298 = (87.2575,'kcal/mol','+|-',9.36598),
        S298 = (0.229779,'cal/mol/K','+|-',10.6365),
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
        Cpdata = ([-2.56869,-3.95459,-4.80574,-5.18542,-5.29212,-5.45696,-5.37668],'cal/mol/K','+|-',[5.91741,7.87064,9.02823,8.98942,8.28136,7.19254,5.26489]),
        H298 = (87.0381,'kcal/mol','+|-',9.21784),
        S298 = (0.350187,'cal/mol/K','+|-',11.2466),
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
        Cpdata = ([-3.2571,-4.92448,-5.7754,-6.0132,-5.90233,-5.78967,-5.29922],'cal/mol/K','+|-',[5.14499,7.04627,8.92098,9.36265,8.97479,7.95682,5.56232]),
        H298 = (87.0234,'kcal/mol','+|-',9.44195),
        S298 = (1.65092,'cal/mol/K','+|-',11.3905),
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
        Cpdata = ([-3.19204,-4.93341,-5.85021,-6.08684,-5.96308,-5.80354,-5.22449],'cal/mol/K','+|-',[5.32119,7.67886,9.90251,10.425,9.97048,8.77009,5.84186]),
        H298 = (87.0294,'kcal/mol','+|-',9.62367),
        S298 = (2.00802,'cal/mol/K','+|-',12.5906),
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
        Cpdata = ([-2.82325,-2.86552,-2.90357,-2.98101,-3.08304,-3.48412,-4.32457],'cal/mol/K','+|-',[6.21516,4.65908,4.54857,5.09005,5.77606,6.54746,6.16738]),
        H298 = (85.3692,'kcal/mol','+|-',8.40956),
        S298 = (-1.88815,'cal/mol/K','+|-',5.15588),
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
        Cpdata = ([-0.159277,-0.559984,-1.41193,-2.28821,-3.15638,-4.29249,-5.64781],'cal/mol/K','+|-',[6.00074,7.48082,6.97714,6.00022,4.77877,4.47303,4.544]),
        H298 = (87.1422,'kcal/mol','+|-',8.46084),
        S298 = (-4.20239,'cal/mol/K','+|-',5.39313),
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
        Cpdata = ([-2.91968,-3.17173,-3.25735,-3.35321,-3.30459,-3.1489,-3.00618],'cal/mol/K','+|-',[5.85632,5.89377,5.70348,5.44091,5.04113,4.84738,5.08586]),
        H298 = (86.1897,'kcal/mol','+|-',8.9415),
        S298 = (0.228914,'cal/mol/K','+|-',17.9347),
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
        Cpdata = ([-3.32326,-3.81236,-3.909,-3.96014,-3.69512,-3.27645,-2.68371],'cal/mol/K','+|-',[6.58366,6.28326,5.92719,5.54862,5.20786,5.11428,5.37366]),
        H298 = (85.4042,'kcal/mol','+|-',9.10971),
        S298 = (2.55748,'cal/mol/K','+|-',21.7954),
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
        Cpdata = ([-0.381313,-1.36694,-2.03883,-2.40851,-2.81562,-3.15953,-3.9472],'cal/mol/K','+|-',[5.96982,6.37454,6.35601,6.04983,5.50189,5.32136,5.3044]),
        H298 = (96.6525,'kcal/mol','+|-',21.3957),
        S298 = (0.722061,'cal/mol/K','+|-',11.6327),
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
        Cpdata = ([-0.644548,-1.68321,-2.31589,-2.67223,-3.02605,-3.3047,-3.98379],'cal/mol/K','+|-',[5.4535,5.33631,5.33235,5.29597,5.18273,5.19421,5.32242]),
        H298 = (95.3559,'kcal/mol','+|-',19.2312),
        S298 = (2.16293,'cal/mol/K','+|-',13.5395),
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
        Cpdata = ([-0.676944,-1.43817,-1.95264,-2.35979,-2.99653,-3.46772,-4.17975],'cal/mol/K','+|-',[5.35879,5.09101,4.88996,4.79237,4.70937,4.69536,4.71086]),
        H298 = (103.117,'kcal/mol','+|-',17.4612),
        S298 = (3.82917,'cal/mol/K','+|-',9.66872),
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
        Cpdata = ([-0.527593,-1.3543,-1.93012,-2.35865,-2.99852,-3.45003,-4.08845],'cal/mol/K','+|-',[5.48906,5.19936,4.97476,4.86163,4.76345,4.7458,4.7426]),
        H298 = (101.772,'kcal/mol','+|-',17.7987),
        S298 = (4.08554,'cal/mol/K','+|-',10.4203),
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
        Cpdata = ([-0.595834,-1.47299,-2.07218,-2.50718,-3.15321,-3.60633,-4.20407],'cal/mol/K','+|-',[4.30107,3.81342,3.41078,3.20143,2.97758,2.88229,2.86459]),
        H298 = (100.903,'kcal/mol','+|-',15.3016),
        S298 = (3.29355,'cal/mol/K','+|-',4.42859),
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
        Cpdata = ([-0.627585,-1.53997,-2.13856,-2.56417,-3.19911,-3.62186,-4.16478],'cal/mol/K','+|-',[4.49571,3.93256,3.47483,3.2408,2.98859,2.88962,2.86051]),
        H298 = (99.9261,'kcal/mol','+|-',15.3493),
        S298 = (3.49183,'cal/mol/K','+|-',4.48107),
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
        Cpdata = ([-1.27667,-2.03072,-2.46006,-2.78296,-3.26766,-3.59859,-4.05993],'cal/mol/K','+|-',[3.06873,3.00085,2.99175,2.9813,2.95295,2.91525,2.84625]),
        H298 = (98.9488,'kcal/mol','+|-',19.8918),
        S298 = (3.12916,'cal/mol/K','+|-',3.43453),
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
        Cpdata = ([-1.3214,-1.86692,-2.2362,-2.54695,-3.03541,-3.40001,-3.96433],'cal/mol/K','+|-',[3.46728,3.20753,3.11252,3.02962,2.91565,2.86238,2.83015]),
        H298 = (95.059,'kcal/mol','+|-',29.515),
        S298 = (3.07395,'cal/mol/K','+|-',3.72436),
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
        Cpdata = ([1.34236,0.0565619,-1.03697,-1.77979,-2.85772,-3.56864,-4.39818],'cal/mol/K','+|-',[5.65778,4.41336,3.85598,3.56931,3.1233,2.90046,2.85852]),
        H298 = (103.778,'kcal/mol','+|-',3.44627),
        S298 = (5.2363,'cal/mol/K','+|-',5.10141),
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
        Cpdata = ([-0.137645,-0.676078,-1.11835,-1.50996,-2.11457,-2.55687,-3.42778],'cal/mol/K','+|-',[6.24455,6.18599,6.1574,6.1447,6.32967,6.65135,7.01425]),
        H298 = (107.74,'kcal/mol','+|-',32.0983),
        S298 = (8.61123,'cal/mol/K','+|-',30.79),
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
        Cpdata = ([-0.632934,-1.77105,-2.44611,-2.78424,-3.03663,-3.24627,-3.91353],'cal/mol/K','+|-',[5.51031,5.42758,5.47083,5.45779,5.3503,5.3648,5.527]),
        H298 = (91.483,'kcal/mol','+|-',15.0495),
        S298 = (1.56561,'cal/mol/K','+|-',14.5809),
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
        Cpdata = ([-1.29212,-2.58477,-3.24079,-3.54848,-3.7439,-3.88822,-4.66719],'cal/mol/K','+|-',[5.0897,5.11535,5.19837,5.24053,5.3768,5.6157,6.1399]),
        H298 = (91.1493,'kcal/mol','+|-',14.8169),
        S298 = (4.36093,'cal/mol/K','+|-',17.4039),
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
        Cpdata = ([-1.16481,-2.45853,-3.16244,-3.48279,-3.66262,-3.7963,-4.62574],'cal/mol/K','+|-',[5.10369,5.13369,5.26411,5.31801,5.46161,5.72105,6.32252]),
        H298 = (90.0858,'kcal/mol','+|-',14.6383),
        S298 = (4.02982,'cal/mol/K','+|-',18.3312),
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
        Cpdata = ([-0.923944,-2.22957,-2.99123,-3.3616,-3.50485,-3.63403,-4.57589],'cal/mol/K','+|-',[5.22908,5.31616,5.43387,5.47789,5.69953,6.12906,7.02631]),
        H298 = (91.2263,'kcal/mol','+|-',15.5354),
        S298 = (4.43986,'cal/mol/K','+|-',21.7554),
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
        Cpdata = ([-0.881158,-1.97946,-2.62417,-3.10635,-3.70426,-4.06354,-4.66916],'cal/mol/K','+|-',[6.33795,6.04562,5.82335,5.69795,5.42127,5.19765,4.98698]),
        H298 = (88.4447,'kcal/mol','+|-',16.8458),
        S298 = (10.5649,'cal/mol/K','+|-',21.0953),
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
        Cpdata = ([-0.842325,-2.43884,-3.46636,-3.92656,-3.96595,-4.16029,-5.77115],'cal/mol/K','+|-',[4.6358,5.14003,5.43078,5.33784,5.17959,4.96908,4.68396]),
        H298 = (95.6685,'kcal/mol','+|-',10.6471),
        S298 = (2.59667,'cal/mol/K','+|-',8.43631),
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
        Cpdata = ([-0.728223,-2.08926,-3.01197,-3.49029,-3.59382,-3.91672,-5.82237],'cal/mol/K','+|-',[4.62974,4.86834,4.95053,4.88074,4.8598,4.88135,4.73313]),
        H298 = (96.1249,'kcal/mol','+|-',10.4687),
        S298 = (2.32275,'cal/mol/K','+|-',9.1197),
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
        Cpdata = ([-1.59632,-2.77572,-3.29527,-3.44531,-3.67707,-3.82519,-4.40689],'cal/mol/K','+|-',[4.87513,4.68079,4.96101,5.02332,4.9067,4.74071,4.66179]),
        H298 = (86.3066,'kcal/mol','+|-',9.99127),
        S298 = (1.86589,'cal/mol/K','+|-',8.58329),
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
        Cpdata = ([-0.804637,-2.40846,-3.3749,-3.68582,-4.01214,-4.16137,-4.91043],'cal/mol/K','+|-',[5.00269,4.62772,4.52426,4.49834,4.47486,4.47228,4.47261]),
        H298 = (85.8053,'kcal/mol','+|-',9.31199),
        S298 = (-0.177331,'cal/mol/K','+|-',4.59586),
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
        Cpdata = ([-0.293527,-1.21918,-1.79249,-2.02607,-2.24729,-2.48544,-3.12706],'cal/mol/K','+|-',[5.7205,5.4495,5.40234,5.35109,5.17356,5.11154,4.92747]),
        H298 = (87.3148,'kcal/mol','+|-',11.4042),
        S298 = (-0.509068,'cal/mol/K','+|-',13.5786),
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
        Cpdata = ([-0.011228,-1.29267,-2.04427,-2.34382,-2.53827,-2.69206,-3.15279],'cal/mol/K','+|-',[5.68729,5.47244,5.32272,5.16124,4.94543,4.95631,4.8863]),
        H298 = (85.8245,'kcal/mol','+|-',10.6713),
        S298 = (-0.0736636,'cal/mol/K','+|-',14.5451),
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
        Cpdata = ([-1.30389,-2.44329,-2.82317,-2.77056,-2.53612,-2.58893,-3.16947],'cal/mol/K','+|-',[5.09022,5.83111,5.91,5.4839,4.87107,4.74675,4.68673]),
        H298 = (87.4342,'kcal/mol','+|-',13.7596),
        S298 = (-2.09271,'cal/mol/K','+|-',6.48589),
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
        Cpdata = ([-2.45431,-4.9482,-5.41906,-4.84815,-3.40929,-2.67155,-2.79206],'cal/mol/K','+|-',[5.1823,5.83213,5.92428,5.75435,5.55736,5.54869,5.03959]),
        H298 = (95.6168,'kcal/mol','+|-',15.4681),
        S298 = (-0.22413,'cal/mol/K','+|-',8.02806),
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
        Cpdata = ([-1.13542,-1.65519,-1.94772,-1.99574,-2.06761,-2.38643,-3.11095],'cal/mol/K','+|-',[4.79534,4.47446,4.49281,4.4806,4.50992,4.52974,4.51583]),
        H298 = (86.0253,'kcal/mol','+|-',8.37898),
        S298 = (-2.25848,'cal/mol/K','+|-',5.37588),
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
        Cpdata = ([-1.09574,-1.67887,-1.98951,-2.00352,-1.95187,-2.23879,-3.23986],'cal/mol/K','+|-',[5.05191,4.47371,4.50211,4.48762,4.47692,4.4729,4.47215]),
        H298 = (85.9488,'kcal/mol','+|-',8.35652),
        S298 = (-1.9051,'cal/mol/K','+|-',5.57733),
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
        Cpdata = ([0.807431,-0.593944,-1.58737,-2.06876,-2.49322,-2.71186,-3.06158],'cal/mol/K','+|-',[5.67221,5.06594,4.94248,4.96503,4.95388,5.05605,4.9756]),
        H298 = (85.0849,'kcal/mol','+|-',9.68607),
        S298 = (0.893567,'cal/mol/K','+|-',18.4123),
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
        Cpdata = ([0.851452,-0.855741,-1.85708,-2.39766,-2.71805,-2.72663,-2.01819],'cal/mol/K','+|-',[4.93789,4.88703,5.69793,6.06084,5.90057,5.88429,4.85013]),
        H298 = (84.2357,'kcal/mol','+|-',9.17647),
        S298 = (7.08855,'cal/mol/K','+|-',23.64),
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
        Cpdata = ([0.483137,-1.3073,-2.45943,-3.06187,-3.44118,-3.52617,-2.46347],'cal/mol/K','+|-',[5.05072,4.7825,6.01872,6.54822,6.08961,5.82301,4.72111]),
        H298 = (83.1971,'kcal/mol','+|-',8.5303),
        S298 = (0.691117,'cal/mol/K','+|-',10.7448),
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
        Cpdata = ([1.86903,0.730741,-0.447496,-1.08479,-1.94097,-2.65093,-3.34714],'cal/mol/K','+|-',[6.31679,4.52488,4.53813,4.6393,4.4722,4.4932,4.47703]),
        H298 = (80.5721,'kcal/mol','+|-',13.2307),
        S298 = (-0.718341,'cal/mol/K','+|-',8.16683),
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
        Cpdata = ([0.404688,-0.928649,-1.84202,-2.2638,-2.58758,-2.72928,-3.26238],'cal/mol/K','+|-',[5.87905,5.0563,4.73961,4.71334,4.88528,5.12067,5.05107]),
        H298 = (85.4701,'kcal/mol','+|-',8.60206),
        S298 = (0.0614275,'cal/mol/K','+|-',18.9705),
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
        Cpdata = ([1.02304,-0.62564,-1.73226,-2.19906,-2.47822,-2.55389,-3.07715],'cal/mol/K','+|-',[5.69011,5.08106,4.81112,4.79192,5.00765,5.28574,5.186]),
        H298 = (84.8429,'kcal/mol','+|-',8.38454),
        S298 = (-0.342081,'cal/mol/K','+|-',22.0018),
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
        Cpdata = ([0.793562,-0.848356,-1.96853,-2.42066,-2.68019,-2.77189,-3.36713],'cal/mol/K','+|-',[5.74448,5.01249,4.65017,4.65462,4.95695,5.27194,5.0072]),
        H298 = (84.8554,'kcal/mol','+|-',8.39069),
        S298 = (-3.27408,'cal/mol/K','+|-',15.6553),
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
        Cpdata = ([1.57526,-0.438003,-1.79806,-2.16519,-2.07865,-1.94613,-2.72632],'cal/mol/K','+|-',[5.73224,5.1064,4.71828,4.67205,4.74173,4.83048,4.75701]),
        H298 = (84.9055,'kcal/mol','+|-',8.42778),
        S298 = (-8.12876,'cal/mol/K','+|-',7.91005),
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
        Cpdata = ([2.19114,-0.0268501,-1.59524,-1.94653,-1.73288,-1.52637,-2.44761],'cal/mol/K','+|-',[5.49402,5.00558,4.7335,4.647,4.5669,4.55757,4.69888]),
        H298 = (84.7856,'kcal/mol','+|-',8.44488),
        S298 = (-9.59451,'cal/mol/K','+|-',5.68253),
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
        Cpdata = ([-0.432422,-2.37352,-3.23841,-3.48797,-3.21967,-2.95042,-3.33947],'cal/mol/K','+|-',[5.42285,6.03263,6.49977,6.70662,6.71853,6.62491,6.27413]),
        H298 = (86.4996,'kcal/mol','+|-',15.7905),
        S298 = (-1.20734,'cal/mol/K','+|-',11.0897),
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
        Cpdata = ([-1.28158,-0.961961,-0.911235,-0.91395,-1.22887,-1.76225,-3.03701],'cal/mol/K','+|-',[5.62421,5.57767,5.51751,5.62004,5.64503,5.59186,5.22431]),
        H298 = (91.4787,'kcal/mol','+|-',8.87043),
        S298 = (-2.03298,'cal/mol/K','+|-',10.004),
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
        Cpdata = ([-1.62536,-1.23095,-1.08879,-1.08667,-1.42789,-2.02351,-3.28286],'cal/mol/K','+|-',[5.09131,4.99462,4.85527,4.7213,4.54082,4.51989,4.57456]),
        H298 = (90.3827,'kcal/mol','+|-',8.39009),
        S298 = (-1.86158,'cal/mol/K','+|-',5.77554),
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
        Cpdata = ([-0.508507,-1.84526,-2.71516,-3.26513,-3.63198,-3.86274,-4.45429],'cal/mol/K','+|-',[5.46264,5.37334,5.45014,5.29786,4.96546,4.92293,5.23537]),
        H298 = (98.1456,'kcal/mol','+|-',10.4056),
        S298 = (2.1272,'cal/mol/K','+|-',11.436),
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
        Cpdata = ([-0.541311,-1.86189,-2.76103,-3.26335,-3.6312,-3.86557,-4.40054],'cal/mol/K','+|-',[5.50453,5.41764,5.48279,5.34086,4.99199,4.9472,5.2501]),
        H298 = (98.4991,'kcal/mol','+|-',9.35448),
        S298 = (2.27383,'cal/mol/K','+|-',11.6228),
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
        Cpdata = ([-0.559892,-1.87391,-2.79661,-3.28333,-3.57264,-3.75469,-4.2677],'cal/mol/K','+|-',[5.64286,5.54588,5.61556,5.45867,5.05384,4.9715,5.29922]),
        H298 = (99.0767,'kcal/mol','+|-',9.04586),
        S298 = (1.55233,'cal/mol/K','+|-',11.579),
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
        Cpdata = ([-0.235207,-2.22604,-3.56979,-4.07466,-3.99328,-3.87554,-4.14106],'cal/mol/K','+|-',[5.62787,5.89684,5.83178,5.58931,5.30742,5.34648,5.97028]),
        H298 = (97.8249,'kcal/mol','+|-',8.94521),
        S298 = (-1.50568,'cal/mol/K','+|-',11.8106),
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
        Cpdata = ([-0.34389,-2.38084,-3.73155,-4.05722,-3.62826,-3.27602,-3.32686],'cal/mol/K','+|-',[5.97112,6.40181,6.38021,6.08833,5.53607,5.31453,5.95392]),
        H298 = (97.4214,'kcal/mol','+|-',9.08606),
        S298 = (-3.88645,'cal/mol/K','+|-',11.2997),
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
        Cpdata = ([0.22172,-1.88501,-3.28601,-3.76052,-3.60352,-3.45342,-3.8779],'cal/mol/K','+|-',[5.47452,6.23328,6.31891,6.22045,5.7699,5.4186,5.49562]),
        H298 = (97.7652,'kcal/mol','+|-',9.06689),
        S298 = (-2.23717,'cal/mol/K','+|-',8.54398),
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
        Cpdata = ([-0.368529,-2.74518,-4.12838,-4.51298,-4.06698,-3.4754,-3.58808],'cal/mol/K','+|-',[4.89932,5.04064,5.25824,5.46141,5.65636,5.69814,5.60023]),
        H298 = (97.0311,'kcal/mol','+|-',8.48442),
        S298 = (-3.07478,'cal/mol/K','+|-',8.48274),
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
        Cpdata = ([-0.359238,-2.25974,-3.45501,-3.73064,-3.20942,-2.62988,-2.8749],'cal/mol/K','+|-',[5.09931,4.73883,4.53778,4.47784,4.51017,4.64171,4.98365]),
        H298 = (96.817,'kcal/mol','+|-',8.48517),
        S298 = (-4.59824,'cal/mol/K','+|-',6.49869),
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
        Cpdata = ([-0.92384,-2.56805,-3.56595,-3.73373,-3.22027,-2.51734,-2.49407],'cal/mol/K','+|-',[4.9351,4.75728,4.5703,4.48352,4.54757,4.77357,5.11788]),
        H298 = (96.9652,'kcal/mol','+|-',8.58541),
        S298 = (-3.3757,'cal/mol/K','+|-',5.34748),
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
        Cpdata = ([-1.05283,-1.54111,-1.93414,-2.35431,-3.03487,-3.54737,-4.38221],'cal/mol/K','+|-',[4.9175,4.06918,3.63401,3.37343,3.07341,2.94662,2.88837]),
        H298 = (99.8378,'kcal/mol','+|-',3.78835),
        S298 = (5.34937,'cal/mol/K','+|-',4.90166),
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
        Cpdata = ([-2.21406,-2.37572,-2.56738,-2.86201,-3.3663,-3.77883,-4.55034],'cal/mol/K','+|-',[2.82847,2.89802,2.96448,2.92812,2.87319,2.84242,2.82966]),
        H298 = (99.2703,'kcal/mol','+|-',3.42795),
        S298 = (4.19511,'cal/mol/K','+|-',2.84205),
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
        Cpdata = ([-0.275566,-1.33202,-1.98141,-2.25956,-2.51809,-2.78137,-3.60977],'cal/mol/K','+|-',[6.64785,7.62754,7.66011,7.08006,5.97694,5.5468,5.519]),
        H298 = (89.6366,'kcal/mol','+|-',16.9637),
        S298 = (-0.473151,'cal/mol/K','+|-',10.9832),
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
        Cpdata = ([-0.566065,-1.80964,-2.47055,-2.68502,-2.81384,-2.96095,-3.59522],'cal/mol/K','+|-',[6.82707,7.79329,7.80121,7.12869,5.89865,5.55707,5.55394]),
        H298 = (86.9109,'kcal/mol','+|-',14.5422),
        S298 = (-0.0108804,'cal/mol/K','+|-',11.5063),
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
        Cpdata = ([0.295677,-0.290188,-0.862226,-1.26257,-1.83664,-2.37676,-3.5244],'cal/mol/K','+|-',[5.61738,5.17323,4.99697,4.86178,4.69734,4.71812,4.79416]),
        H298 = (87.5719,'kcal/mol','+|-',9.68858),
        S298 = (-2.16417,'cal/mol/K','+|-',7.4068),
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
        Cpdata = ([0.0680192,-0.229603,-0.671663,-1.04501,-1.68657,-2.2988,-3.56057],'cal/mol/K','+|-',[5.25406,4.99138,4.80582,4.74153,4.678,4.69128,4.70514]),
        H298 = (87.7979,'kcal/mol','+|-',9.10388),
        S298 = (-1.55501,'cal/mol/K','+|-',5.54015),
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
        Cpdata = ([-0.136036,-0.386095,-0.736534,-1.03977,-1.59299,-2.19257,-3.46085],'cal/mol/K','+|-',[5.15422,5.0493,4.87528,4.79676,4.68726,4.6745,4.65106]),
        H298 = (87.576,'kcal/mol','+|-',9.1675),
        S298 = (-1.26977,'cal/mol/K','+|-',5.34474),
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
        Cpdata = ([-0.019996,-0.254656,-0.603735,-0.901924,-1.47495,-2.07408,-3.34835],'cal/mol/K','+|-',[5.07895,4.9307,4.7368,4.6373,4.56637,4.55132,4.53935]),
        H298 = (87.4708,'kcal/mol','+|-',9.06592),
        S298 = (-1.40496,'cal/mol/K','+|-',5.24382),
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
        Cpdata = ([0.653431,0.221444,-0.453994,-0.860097,-1.41969,-2.00523,-3.11831],'cal/mol/K','+|-',[4.3981,3.83216,3.30268,3.02022,2.82901,2.83185,2.83422]),
        H298 = (87.6402,'kcal/mol','+|-',3.43598),
        S298 = (-2.21189,'cal/mol/K','+|-',2.87399),
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
        Cpdata = ([-0.713089,-0.799738,-0.871609,-1.0129,-1.44426,-1.98804,-3.3364],'cal/mol/K','+|-',[3.89228,3.62232,3.29832,3.11345,2.99355,3.0006,2.9952]),
        H298 = (88.2784,'kcal/mol','+|-',5.36571),
        S298 = (-0.341842,'cal/mol/K','+|-',4.22115),
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
        Cpdata = ([-1.46381,-1.44428,-1.36072,-1.36687,-1.58386,-1.97925,-3.17343],'cal/mol/K','+|-',[2.96201,2.87613,2.8313,2.89484,3.07489,3.16313,3.05041]),
        H298 = (87.0877,'kcal/mol','+|-',3.46892),
        S298 = (-0.873027,'cal/mol/K','+|-',4.56776),
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
        Cpdata = ([2.50984,0.839112,-0.643363,-1.46356,-2.56102,-3.46591,-4.94643],'cal/mol/K','+|-',[4.53018,4.49706,4.47469,4.48367,4.51235,4.4765,4.61217]),
        H298 = (88.5323,'kcal/mol','+|-',8.55855),
        S298 = (-4.6854,'cal/mol/K','+|-',4.48465),
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
        Cpdata = ([0.562477,-0.408267,-1.11122,-1.46604,-1.7978,-2.16876,-3.18731],'cal/mol/K','+|-',[6.4173,5.65165,5.38125,5.09657,4.69032,4.66369,4.86251]),
        H298 = (86.6426,'kcal/mol','+|-',11.0298),
        S298 = (-3.98726,'cal/mol/K','+|-',8.4297),
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
        Cpdata = ([0.671798,-0.467069,-1.23044,-1.57782,-1.83992,-2.16174,-3.14443],'cal/mol/K','+|-',[6.67145,5.82396,5.4845,5.16039,4.72154,4.69617,4.92169]),
        H298 = (86.4483,'kcal/mol','+|-',11.6856),
        S298 = (-4.25549,'cal/mol/K','+|-',8.81684),
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
        Cpdata = ([0.832091,-0.383015,-1.18677,-1.52884,-1.77293,-2.08374,-3.04723],'cal/mol/K','+|-',[6.92906,6.01658,5.6431,5.26726,4.74481,4.7062,4.96438]),
        H298 = (86.7572,'kcal/mol','+|-',10.5753),
        S298 = (-4.70346,'cal/mol/K','+|-',8.98754),
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
        Cpdata = ([0.912901,-0.52335,-1.4306,-1.7625,-1.8792,-2.08781,-2.94532],'cal/mol/K','+|-',[7.40554,6.30626,5.77741,5.32647,4.78228,4.76274,5.05525]),
        H298 = (87.4361,'kcal/mol','+|-',11.1354),
        S298 = (-5.03877,'cal/mol/K','+|-',9.65648),
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
        Cpdata = ([0.920486,-0.689776,-1.65716,-1.98144,-2.02408,-2.16912,-3.02367],'cal/mol/K','+|-',[7.70061,6.39813,5.70651,5.20414,4.71215,4.76464,5.09554]),
        H298 = (87.7628,'kcal/mol','+|-',11.0655),
        S298 = (-4.96033,'cal/mol/K','+|-',10.1154),
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
        Cpdata = ([3.65309,1.17336,-0.266785,-1.08491,-2.03442,-2.59868,-3.64324],'cal/mol/K','+|-',[5.81484,5.51605,5.21649,5.19833,5.0876,4.97439,4.55062]),
        H298 = (88.5193,'kcal/mol','+|-',8.57342),
        S298 = (-6.94289,'cal/mol/K','+|-',7.54548),
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
        Cpdata = ([4.72129,2.01097,0.365941,-0.517122,-1.58609,-2.21211,-3.48053],'cal/mol/K','+|-',[4.49886,4.90058,4.9815,5.12914,5.19069,5.08947,4.55861]),
        H298 = (88.0559,'kcal/mol','+|-',8.49078),
        S298 = (-8.3707,'cal/mol/K','+|-',6.70381),
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
        Cpdata = ([0.177071,-0.939687,-1.77587,-2.00201,-1.85866,-1.9746,-2.78081],'cal/mol/K','+|-',[7.20065,5.39451,4.87547,4.67705,4.54207,4.73308,5.51886]),
        H298 = (86.3891,'kcal/mol','+|-',8.54336),
        S298 = (-4.87512,'cal/mol/K','+|-',11.47),
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
        Cpdata = ([2.12828,-0.150117,-1.67892,-2.04684,-1.60565,-1.56817,-2.36123],'cal/mol/K','+|-',[5.52701,5.39861,5.20324,4.8531,4.51204,4.73343,6.13524]),
        H298 = (85.9302,'kcal/mol','+|-',8.68437),
        S298 = (-8.02666,'cal/mol/K','+|-',10.0934),
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
        Cpdata = ([2.07504,-0.0946947,-1.42531,-1.80733,-1.43364,-1.39337,-1.52029],'cal/mol/K','+|-',[6.40528,6.18192,5.70997,5.07232,4.4729,4.90688,6.18952]),
        H298 = (85.9512,'kcal/mol','+|-',9.00366),
        S298 = (-8.80379,'cal/mol/K','+|-',13.01),
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
        Cpdata = ([-0.370103,-1.01342,-1.51425,-1.89621,-2.27538,-2.66877,-3.77624],'cal/mol/K','+|-',[4.56727,4.4833,4.47577,4.48359,4.52727,4.56245,4.5016]),
        H298 = (83.3423,'kcal/mol','+|-',23.1079),
        S298 = (-1.34372,'cal/mol/K','+|-',5.18997),
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
        Cpdata = ([-1.78034,-3.95067,-4.73683,-4.68938,-4.1908,-3.78414,-3.69502],'cal/mol/K','+|-',[7.66213,8.83233,8.76876,7.87662,6.32174,6.22631,6.51451]),
        H298 = (85.6128,'kcal/mol','+|-',21.2057),
        S298 = (3.0233,'cal/mol/K','+|-',13.4852),
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
        Cpdata = ([-2.52845,-4.54248,-5.04117,-4.73196,-3.87611,-3.32363,-3.26395],'cal/mol/K','+|-',[7.40832,8.78632,8.95977,8.30766,6.82207,6.48921,6.26613]),
        H298 = (85.2845,'kcal/mol','+|-',25.7306),
        S298 = (2.41288,'cal/mol/K','+|-',12.6782),
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
        Cpdata = ([-1.99026,-4.289,-5.07521,-4.94709,-4.19921,-3.7534,-3.66637],'cal/mol/K','+|-',[7.61903,9.31576,9.45137,8.56898,6.84614,6.5521,6.60222]),
        H298 = (90.5216,'kcal/mol','+|-',14.5147),
        S298 = (3.32293,'cal/mol/K','+|-',12.6902),
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
        Cpdata = ([-1.6926,-3.73847,-4.48234,-4.41732,-3.86224,-3.54728,-3.80682],'cal/mol/K','+|-',[7.75787,8.97543,8.72039,7.565,5.69966,5.39727,6.45778]),
        H298 = (90.3391,'kcal/mol','+|-',14.948),
        S298 = (1.73169,'cal/mol/K','+|-',8.84677),
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
        Cpdata = ([-2.05305,-5.48743,-6.59946,-6.19454,-4.67157,-3.67355,-3.14058],'cal/mol/K','+|-',[10.9213,11.3865,10.3223,8.8606,6.79982,6.42596,8.27033]),
        H298 = (96.3502,'kcal/mol','+|-',12.2824),
        S298 = (0.915958,'cal/mol/K','+|-',12.8654),
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
        Cpdata = ([-2.47932,-6.06291,-7.18575,-6.64076,-4.77345,-3.55959,-2.65316],'cal/mol/K','+|-',[12.1459,12.5448,11.2354,9.62829,7.39639,6.9314,8.84283]),
        H298 = (97.4576,'kcal/mol','+|-',12.0493),
        S298 = (1.12846,'cal/mol/K','+|-',14.5884),
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
        Cpdata = ([0.10167,-3.41003,-5.04573,-5.18741,-4.5927,-4.328,-4.18496],'cal/mol/K','+|-',[7.16982,7.5598,8.33303,8.85227,8.4425,6.92068,7.13995]),
        H298 = (96.5328,'kcal/mol','+|-',12.7424),
        S298 = (0.527869,'cal/mol/K','+|-',17.3371),
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
        Cpdata = ([0.706059,-1.98022,-3.11354,-2.99096,-2.57815,-2.92473,-2.76217],'cal/mol/K','+|-',[8.60499,6.72579,5.41089,4.57596,5.01494,5.34154,5.77696]),
        H298 = (93.7974,'kcal/mol','+|-',8.68366),
        S298 = (-4.21983,'cal/mol/K','+|-',6.33826),
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
        Cpdata = ([-1.54829,-2.87611,-3.41258,-3.476,-3.17493,-2.94622,-3.22269],'cal/mol/K','+|-',[6.21343,8.2036,8.1504,7.15363,5.43384,4.98428,4.81985]),
        H298 = (84.2638,'kcal/mol','+|-',10.4223),
        S298 = (0.381181,'cal/mol/K','+|-',4.69121),
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
        Cpdata = ([-1.43641,-2.65754,-3.19974,-3.38395,-3.65031,-4.00806,-5.13121],'cal/mol/K','+|-',[6.22482,7.44519,7.29803,6.18026,4.59068,4.68007,5.30488]),
        H298 = (92.6833,'kcal/mol','+|-',10.1016),
        S298 = (3.98858,'cal/mol/K','+|-',4.5132),
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
        Cpdata = ([-3.16715,-5.18822,-5.66701,-5.20709,-4.05163,-3.47224,-3.9356],'cal/mol/K','+|-',[5.18277,4.71796,4.58672,4.54513,4.53272,4.57609,4.59641]),
        H298 = (95.4487,'kcal/mol','+|-',9.66759),
        S298 = (4.09088,'cal/mol/K','+|-',4.56434),
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
        Cpdata = ([-3.96362,-5.21844,-4.9504,-4.15826,-3.01453,-2.17756,-2.19083],'cal/mol/K','+|-',[6.32102,7.69628,8.21677,8.0675,6.83171,6.00373,4.8415]),
        H298 = (65.1119,'kcal/mol','+|-',11.9077),
        S298 = (-0.0139146,'cal/mol/K','+|-',12.3582),
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
        Cpdata = ([-3.80942,-4.93994,-4.6222,-3.86403,-2.8884,-2.14649,-2.27664],'cal/mol/K','+|-',[6.65062,8.16787,8.72712,8.58828,7.2707,6.32669,4.90707]),
        H298 = (66.2426,'kcal/mol','+|-',11.0204),
        S298 = (-0.352868,'cal/mol/K','+|-',13.5078),
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
        Cpdata = ([-2.99011,-4.17081,-3.7318,-3.0041,-2.47329,-2.02113,-2.06409],'cal/mol/K','+|-',[9.93655,13.7188,14.8549,14.5198,11.7899,9.58004,5.73042]),
        H298 = (67.8918,'kcal/mol','+|-',12.8944),
        S298 = (-1.27677,'cal/mol/K','+|-',22.8779),
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
        Cpdata = ([-3.75793,-4.78444,-4.47559,-3.68472,-2.55066,-1.67377,-2.07737],'cal/mol/K','+|-',[4.5458,4.47735,4.50144,4.55587,4.59256,4.54905,4.48184]),
        H298 = (63.389,'kcal/mol','+|-',8.36039),
        S298 = (-2.10879,'cal/mol/K','+|-',4.47676),
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
        Cpdata = ([-0.17969,-2.62106,-4.04293,-4.59928,-4.96457,-4.96274,-4.84096],'cal/mol/K','+|-',[7.88452,9.28618,9.12361,7.61232,5.0592,5.10575,6.87872]),
        H298 = (85.8445,'kcal/mol','+|-',12.3254),
        S298 = (2.21953,'cal/mol/K','+|-',7.47736),
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
        Cpdata = ([0.123067,-2.09048,-3.39127,-4.01559,-4.65342,-4.76807,-4.39932],'cal/mol/K','+|-',[7.99594,9.06113,8.45387,6.82418,4.64522,5.00824,6.45355]),
        H298 = (85.1866,'kcal/mol','+|-',10.89),
        S298 = (1.64089,'cal/mol/K','+|-',6.67236),
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
        Cpdata = ([-0.351831,-2.94768,-4.28505,-4.71317,-4.76896,-4.41655,-3.67388],'cal/mol/K','+|-',[8.92579,9.82022,8.92947,7.03037,4.69504,5.00494,6.44272]),
        H298 = (85.2239,'kcal/mol','+|-',12.713),
        S298 = (1.07823,'cal/mol/K','+|-',7.0481),
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
        Cpdata = ([-3.04915,-6.25235,-7.27894,-6.80374,-5.11193,-3.69015,-2.21943],'cal/mol/K','+|-',[6.24355,5.88282,5.70514,5.3727,4.86012,4.8766,6.20456]),
        H298 = (87.5511,'kcal/mol','+|-',12.2445),
        S298 = (-1.05945,'cal/mol/K','+|-',4.57586),
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
        Cpdata = ([-1.80253,-5.41165,-6.78732,-6.54543,-5.24384,-4.10065,-3.37032],'cal/mol/K','+|-',[4.546,5.67914,6.2687,6.01087,5.17919,4.84957,5.02032]),
        H298 = (89.9991,'kcal/mol','+|-',9.28829),
        S298 = (-1.28334,'cal/mol/K','+|-',4.54687),
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
        Cpdata = ([0.824179,0.476104,-0.129663,-0.648863,-1.39846,-2.1015,-3.66482],'cal/mol/K','+|-',[5.48378,5.78021,5.88245,5.99532,5.84652,5.37142,5.47426]),
        H298 = (98.6471,'kcal/mol','+|-',10.6394),
        S298 = (-2.22318,'cal/mol/K','+|-',8.11575),
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
        Cpdata = ([0.990115,0.65426,0.0440304,-0.480836,-1.24105,-1.95915,-3.56267],'cal/mol/K','+|-',[5.29883,5.58733,5.71213,5.85065,5.71743,5.24111,5.43822]),
        H298 = (98.3769,'kcal/mol','+|-',10.0147),
        S298 = (-2.28117,'cal/mol/K','+|-',8.26152),
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
        Cpdata = ([1.11602,0.698463,0.0581016,-0.467966,-1.17198,-1.8713,-3.57885],'cal/mol/K','+|-',[5.49316,5.92601,6.09757,6.27892,6.10659,5.48684,5.75736]),
        H298 = (99.5598,'kcal/mol','+|-',9.59074),
        S298 = (-2.39895,'cal/mol/K','+|-',9.27796),
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
        Cpdata = ([1.91956,1.68036,0.850499,0.23772,-0.395165,-1.53119,-4.01682],'cal/mol/K','+|-',[7.42736,8.66581,9.1297,9.48349,8.78833,7.3712,8.49474]),
        H298 = (102.369,'kcal/mol','+|-',12.6929),
        S298 = (-5.26494,'cal/mol/K','+|-',14.6923),
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
        Cpdata = ([-0.372526,-1.3295,-2.3547,-3.06366,-3.21363,-3.43042,-6.12335],'cal/mol/K','+|-',[5.20225,5.84435,6.74418,7.2022,6.32829,5.6982,8.35767]),
        H298 = (99.4664,'kcal/mol','+|-',11.1123),
        S298 = (-0.368454,'cal/mol/K','+|-',11.139),
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
        Cpdata = ([0.823823,0.341411,-0.230043,-0.724578,-1.45446,-1.99497,-3.41959],'cal/mol/K','+|-',[4.63348,4.60234,4.71894,4.867,4.96192,4.79503,4.60288]),
        H298 = (99.1143,'kcal/mol','+|-',8.69648),
        S298 = (-1.35677,'cal/mol/K','+|-',5.53899),
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
        Cpdata = ([0.949836,0.362234,-0.265379,-0.804492,-1.61007,-2.18741,-3.56303],'cal/mol/K','+|-',[2.95975,3.05534,3.24636,3.44554,3.44966,3.04517,2.85642]),
        H298 = (99.3215,'kcal/mol','+|-',3.46431),
        S298 = (-1.00094,'cal/mol/K','+|-',3.58757),
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
        Cpdata = ([1.1296,0.645748,0.130792,-0.314121,-1.11726,-1.91116,-3.52955],'cal/mol/K','+|-',[2.89217,2.84139,2.83574,2.83487,2.83222,2.84218,2.86563]),
        H298 = (99.1769,'kcal/mol','+|-',3.42642),
        S298 = (-1.54144,'cal/mol/K','+|-',2.88007),
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
        Cpdata = ([-0.162886,-0.9909,-1.7425,-2.2427,-2.90367,-3.43347,-4.31481],'cal/mol/K','+|-',[5.74711,5.91335,5.8212,5.60684,5.276,5.13043,4.92516]),
        H298 = (106.098,'kcal/mol','+|-',13.3896),
        S298 = (0.286532,'cal/mol/K','+|-',8.70643),
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
        Cpdata = ([-0.20016,-1.08466,-1.85861,-2.34196,-2.94832,-3.44193,-4.27623],'cal/mol/K','+|-',[5.92307,6.11271,6.00659,5.76915,5.39666,5.22535,4.99103]),
        H298 = (104.357,'kcal/mol','+|-',11.6297),
        S298 = (0.0307864,'cal/mol/K','+|-',9.2253),
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
        Cpdata = ([0.961244,0.113399,-0.792467,-1.51992,-2.53981,-3.35941,-4.62837],'cal/mol/K','+|-',[5.24542,5.73179,5.70423,5.46471,5.02736,4.79046,4.68673]),
        H298 = (101.292,'kcal/mol','+|-',11.1639),
        S298 = (0.301891,'cal/mol/K','+|-',9.41507),
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
        Cpdata = ([1.21508,0.282181,-0.710139,-1.39416,-2.42062,-3.25955,-4.43059],'cal/mol/K','+|-',[5.41089,6.22681,6.24255,5.85081,5.24448,4.88063,4.66404]),
        H298 = (102.463,'kcal/mol','+|-',8.50862),
        S298 = (-0.0520655,'cal/mol/K','+|-',10.4809),
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
        Cpdata = ([1.92607,0.77629,-0.374775,-1.00372,-2.04591,-2.95321,-3.99079],'cal/mol/K','+|-',[4.99334,6.38091,6.7983,6.24452,5.34299,4.92784,4.54928]),
        H298 = (103.041,'kcal/mol','+|-',8.52784),
        S298 = (-0.60421,'cal/mol/K','+|-',14.6621),
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
        Cpdata = ([0.720478,-0.0615467,-0.943435,-1.66577,-2.68128,-3.47266,-4.73653],'cal/mol/K','+|-',[5.57379,6.32439,6.13247,5.76648,5.25173,4.87596,4.65661]),
        H298 = (102.069,'kcal/mol','+|-',8.42607),
        S298 = (0.332035,'cal/mol/K','+|-',7.7213),
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
        Cpdata = ([1.04339,0.201005,-0.788193,-1.58413,-2.65803,-3.48354,-4.77899],'cal/mol/K','+|-',[5.68283,6.70647,6.54495,6.1199,5.48264,5.00128,4.71124]),
        H298 = (101.991,'kcal/mol','+|-',8.45553),
        S298 = (-0.305976,'cal/mol/K','+|-',7.95184),
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
        Cpdata = ([2.82255,2.3918,1.12052,0.0786665,-1.26868,-2.41198,-4.38082],'cal/mol/K','+|-',[8.50292,11.8781,11.4361,9.78459,7.43936,5.35385,4.59326]),
        H298 = (102.328,'kcal/mol','+|-',8.4034),
        S298 = (-4.85869,'cal/mol/K','+|-',6.80707),
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
        Cpdata = ([0.510482,-0.893113,-2.20709,-3.15016,-4.06619,-4.74813,-5.85335],'cal/mol/K','+|-',[4.80076,5.08608,5.16221,5.22883,5.02056,4.99677,4.75384]),
        H298 = (100.797,'kcal/mol','+|-',8.66177),
        S298 = (-0.890019,'cal/mol/K','+|-',6.92098),
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
        Cpdata = ([0.544896,-0.237667,-0.984121,-1.62283,-2.6505,-3.40632,-4.50852],'cal/mol/K','+|-',[2.84245,2.84401,2.84318,2.84489,2.845,2.84218,2.83366]),
        H298 = (102.132,'kcal/mol','+|-',3.39966),
        S298 = (1.74873,'cal/mol/K','+|-',3.00723),
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
        Cpdata = ([0.565991,-0.217135,-1.0233,-1.85777,-2.84971,-3.62476,-5.07357],'cal/mol/K','+|-',[5.10877,5.1116,4.99435,4.98152,4.7486,4.69997,4.69416]),
        H298 = (102.398,'kcal/mol','+|-',8.72285),
        S298 = (2.25061,'cal/mol/K','+|-',5.36754),
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
        Cpdata = ([0.565865,-0.322979,-1.16318,-2.07756,-3.06992,-3.85341,-5.2715],'cal/mol/K','+|-',[5.44692,5.39657,5.20712,5.1729,4.82201,4.74738,4.62875]),
        H298 = (102.079,'kcal/mol','+|-',9.0053),
        S298 = (2.43559,'cal/mol/K','+|-',5.60834),
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
        Cpdata = ([0.508707,-0.21567,-1.14324,-1.93767,-3.02618,-3.90701,-5.24281],'cal/mol/K','+|-',[5.68723,5.59747,5.3998,5.28979,4.91133,4.81294,4.6698]),
        H298 = (101.774,'kcal/mol','+|-',8.78096),
        S298 = (1.94661,'cal/mol/K','+|-',5.08063),
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
        Cpdata = ([1.54475,0.591804,-0.601484,-1.5964,-2.94871,-4.00082,-5.39597],'cal/mol/K','+|-',[4.90102,5.71311,6.04433,6.17925,5.55344,5.30822,4.91307]),
        H298 = (101.776,'kcal/mol','+|-',9.41937),
        S298 = (1.42144,'cal/mol/K','+|-',5.15947),
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
        Cpdata = ([-1.23252,-2.1496,-2.80629,-3.07265,-3.31144,-3.51529,-3.96321],'cal/mol/K','+|-',[5.7499,5.67061,5.6623,5.68125,5.64601,5.61598,5.18862]),
        H298 = (106.946,'kcal/mol','+|-',9.27386),
        S298 = (-0.210196,'cal/mol/K','+|-',9.23363),
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
        Cpdata = ([-0.836244,-1.2789,-1.61918,-1.74357,-1.96817,-2.10798,-2.79602],'cal/mol/K','+|-',[6.20038,5.16185,4.82719,4.86483,5.11092,5.23891,5.11959]),
        H298 = (106.88,'kcal/mol','+|-',10.2986),
        S298 = (-0.811835,'cal/mol/K','+|-',14.3086),
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
        Cpdata = ([-1.23964,-1.30147,-1.22923,-1.093,-0.968966,-0.813291,-1.60746],'cal/mol/K','+|-',[9.0907,5.62553,4.51014,4.47415,4.53047,4.54081,4.58064]),
        H298 = (105.715,'kcal/mol','+|-',12.7472),
        S298 = (1.87671,'cal/mol/K','+|-',27.4169),
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
        Cpdata = ([0.437439,-0.504991,-1.28775,-1.48477,-1.7784,-2.21257,-3.0148],'cal/mol/K','+|-',[5.08272,5.27921,5.041,4.72257,4.59627,4.49558,4.64276]),
        H298 = (110.639,'kcal/mol','+|-',9.40334),
        S298 = (-4.55887,'cal/mol/K','+|-',4.67111),
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
        Cpdata = ([-1.36461,-2.43983,-3.202,-3.51568,-3.75919,-3.98439,-4.35228],'cal/mol/K','+|-',[5.67512,5.7628,5.72611,5.68222,5.56445,5.45714,5.00285]),
        H298 = (106.965,'kcal/mol','+|-',9.11407),
        S298 = (-0.0096494,'cal/mol/K','+|-',7.42618),
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
        Cpdata = ([-0.705254,-2.36212,-3.81336,-4.45594,-4.84888,-5.2367,-5.45579],'cal/mol/K','+|-',[4.86642,4.84114,4.79924,5.03275,5.27738,5.24285,5.09103]),
        H298 = (108.82,'kcal/mol','+|-',8.59364),
        S298 = (0.118708,'cal/mol/K','+|-',6.93201),
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
        Cpdata = ([0.262176,-1.6672,-3.40724,-4.26019,-4.94591,-5.56832,-5.04344],'cal/mol/K','+|-',[4.72148,4.61634,4.94885,5.74618,5.49923,5.08403,4.55069]),
        H298 = (109.663,'kcal/mol','+|-',9.01824),
        S298 = (-1.94388,'cal/mol/K','+|-',8.26948),
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
        Cpdata = ([-1.53328,-2.45971,-3.0456,-3.27515,-3.48043,-3.66404,-4.06998],'cal/mol/K','+|-',[5.86572,6.0303,5.94753,5.79144,5.55847,5.37549,4.85536]),
        H298 = (106.603,'kcal/mol','+|-',9.0534),
        S298 = (-0.042485,'cal/mol/K','+|-',7.7328),
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
        Cpdata = ([-1.28093,-2.32075,-3.00706,-3.28924,-3.52045,-3.73345,-4.20143],'cal/mol/K','+|-',[5.82825,5.91027,5.88484,5.80184,5.69719,5.5674,4.94222]),
        H298 = (107.088,'kcal/mol','+|-',9.08347),
        S298 = (-0.12434,'cal/mol/K','+|-',8.14726),
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
        Cpdata = ([-1.5379,-2.02349,-2.46776,-2.42754,-2.0767,-2.06245,-2.92394],'cal/mol/K','+|-',[6.19447,6.64638,6.74427,6.74974,6.26459,5.83626,4.99265]),
        H298 = (105.29,'kcal/mol','+|-',10.0711),
        S298 = (-3.96328,'cal/mol/K','+|-',8.48574),
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
        Cpdata = ([-2.37349,-2.94525,-3.42462,-3.3954,-2.94712,-2.88735,-3.43383],'cal/mol/K','+|-',[5.54979,5.9892,6.02109,5.98803,5.53934,4.97612,4.59891]),
        H298 = (106.622,'kcal/mol','+|-',8.64209),
        S298 = (-2.68165,'cal/mol/K','+|-',7.65439),
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
        Cpdata = ([-2.69467,-4.37033,-5.0875,-5.19507,-5.06077,-4.94275,-4.69753],'cal/mol/K','+|-',[4.98996,3.02451,3.05032,3.53116,4.17313,4.04536,2.98505]),
        H298 = (108.504,'kcal/mol','+|-',3.79429),
        S298 = (2.8966,'cal/mol/K','+|-',3.81694),
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
        Cpdata = ([-0.137715,-1.16936,-2.0801,-2.73961,-3.69926,-4.28429,-4.78183],'cal/mol/K','+|-',[4.33768,3.446,2.91111,2.83015,3.06574,3.32761,3.38356]),
        H298 = (107.123,'kcal/mol','+|-',4.14777),
        S298 = (0.696776,'cal/mol/K','+|-',4.82214),
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
        Cpdata = ([0.0248651,-0.518638,-1.15762,-1.74274,-2.67878,-3.39084,-4.50916],'cal/mol/K','+|-',[4.83209,4.7493,4.66591,4.62637,4.64007,4.66829,4.5877]),
        H298 = (113.445,'kcal/mol','+|-',9.74595),
        S298 = (1.57473,'cal/mol/K','+|-',4.74662),
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
        Cpdata = ([0.269782,-0.29026,-0.986482,-1.63421,-2.67892,-3.43794,-4.539],'cal/mol/K','+|-',[5.01281,4.87822,4.76648,4.72408,4.76863,4.81392,4.665]),
        H298 = (114.97,'kcal/mol','+|-',9.12058),
        S298 = (1.35548,'cal/mol/K','+|-',4.83879),
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
        Cpdata = ([0.00639429,-0.907736,-1.7603,-2.40829,-3.39662,-4.08074,-4.98774],'cal/mol/K','+|-',[5.13699,5.07275,4.60458,4.47318,4.78861,5.09007,4.83824]),
        H298 = (116.686,'kcal/mol','+|-',9.53918),
        S298 = (2.24526,'cal/mol/K','+|-',4.64435),
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
        Cpdata = ([-0.391494,-0.906882,-1.44855,-1.92724,-2.67855,-3.31078,-4.45842],'cal/mol/K','+|-',[2.83064,2.83954,2.84181,2.84258,2.83407,2.83655,2.87521]),
        H298 = (111.031,'kcal/mol','+|-',3.39472),
        S298 = (1.94746,'cal/mol/K','+|-',3.00778),
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

