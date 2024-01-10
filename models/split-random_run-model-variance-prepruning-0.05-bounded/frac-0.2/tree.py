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
1 * R   u1 r0 {2,[S,D,T,B,Q]}
2   R!H u0 r0 {1,[S,D,T,B,Q]}
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
Derived using the following species:
CC(O[O])C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C(=O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=COC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)[CH]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]COCOO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1=COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC(C=C)CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OC(C=C)[CH2])CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1(CC=CC)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)OC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC([O])C(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[CH]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COOC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)C1C=CC=C(C)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C=C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C=CON(CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC=C[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]OC - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
O=[C]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(CC=CC)CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1COOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[O]C=CCC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OOCC(O[O])C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C[CH]CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC#CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]OC)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)OOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
CC=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=CO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C](C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)OOC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=CC(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O)=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(OC(C)=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CO[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C1(C)OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=CC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COCOO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[CH2]C(=O)OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC(O)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC1OC1(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(C)(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC1C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)OOC(C)(C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OCC(C[CH]C=C)C=C)CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C=CCCC=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
C=CC=C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[C]=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=COC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C - Radical thermo from pang.py and closed shell thermo from pang.py
C=C([O])CCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)CC1=CCCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CCC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC1=CC(O[O])C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C[CH]CC1(CC=CC)C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)CCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)OO - Radical thermo from pang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)OCC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[N]CC - Radical thermo from pang.py and closed shell thermo from GAV
[O]CC1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(CO[O])=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CC(CC=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OOC=C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C([CH]O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C#CC[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(C)([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=COCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CCOC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CCO)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)CC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C]=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C=CC(OO)C(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([CH]O)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC=CCC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CCC(C[O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(COO)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)CC(=C)C - Radical thermo from pang.py and closed shell thermo from GAV
CC([O])=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C=CCC1(CC=CC)C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CCCCO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC#C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=O)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CCCC1C([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CC)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)COC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C=C[C](CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from pang.py
CC(=O)OC(CC(C)O[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C(C=O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC(C)(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C(O)C(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(O[O])C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]OC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(C)=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(C=O)C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CC(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)OC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=C(C)C(O[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCCC1C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]C(O)(O)OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(=O)CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)CCC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1(C(=O)O)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC[CH]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
CC(C)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OC(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN([CH]C)O - Radical thermo from pang.py and closed shell thermo from pang.py
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
"""
)

