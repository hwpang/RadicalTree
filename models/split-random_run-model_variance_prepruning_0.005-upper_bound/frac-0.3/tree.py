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
        Cpdata = ([-0.555736,-1.53995,-2.2612,-2.68435,-3.13519,-3.54358,-4.36062],'cal/mol/K','+|-',[3.98434,4.69012,4.97737,4.8765,4.40026,4.11503,4.10198]),
        H298 = (93.6791,'kcal/mol','+|-',26.1568),
        S298 = (0.168372,'cal/mol/K','+|-',9.46693),
    ),
    shortDesc = """Radical correction fitted to 760 radicals""",
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
        Cpdata = ([-0.555736,-1.53995,-2.2612,-2.68435,-3.13519,-3.54358,-4.36062],'cal/mol/K','+|-',[3.98434,4.69012,4.97737,4.8765,4.40026,4.11503,4.10198]),
        H298 = (93.6791,'kcal/mol','+|-',26.1568),
        S298 = (0.168372,'cal/mol/K','+|-',9.46693),
    ),
    shortDesc = """Radical correction fitted to 760 radicals""",
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
        Cpdata = ([0.267931,-1.06733,-2.03357,-2.57838,-3.23824,-3.79379,-4.87181],'cal/mol/K','+|-',[3.1258,3.82761,4.13157,4.0776,3.77757,3.74169,4.29092]),
        H298 = (91.1365,'kcal/mol','+|-',36.3855),
        S298 = (0.798173,'cal/mol/K','+|-',8.21661),
    ),
    shortDesc = """Radical correction fitted to 135 radicals""",
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
        Cpdata = ([0.402698,-0.819915,-1.77671,-2.29945,-2.93514,-3.4736,-4.46805],'cal/mol/K','+|-',[3,3.14133,3.45676,3.49362,3.5145,3.71186,4.22701]),
        H298 = (81.5234,'kcal/mol','+|-',42.2987),
        S298 = (0.211564,'cal/mol/K','+|-',8.90443),
    ),
    shortDesc = """Radical correction fitted to 79 radicals""",
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
        Cpdata = ([0.309653,-0.98442,-1.92963,-2.45924,-3.10667,-3.6626,-4.58053],'cal/mol/K','+|-',[3.10267,3.0642,3.04031,3,3,3,3]),
        H298 = (81.2814,'kcal/mol','+|-',22.5069),
        S298 = (-0.423787,'cal/mol/K','+|-',7.35072),
    ),
    shortDesc = """Radical correction fitted to 50 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.339803,-0.980112,-1.938,-2.46759,-3.10996,-3.66457,-4.58244],'cal/mol/K','+|-',[3.14281,3.12004,3.09474,3,3,3,3]),
        H298 = (79.1317,'kcal/mol','+|-',12.8378),
        S298 = (-0.482082,'cal/mol/K','+|-',7.4591),
    ),
    shortDesc = """Radical correction fitted to 49 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   R!H ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31336,-1.05747,-1.99237,-2.5286,-3.1865,-3.72278,-4.64447],'cal/mol/K','+|-',[3.35259,3.2759,3.23731,3,3,3,3]),
        H298 = (78.3003,'kcal/mol','+|-',13.3252),
        S298 = (-0.356566,'cal/mol/K','+|-',7.34458),
    ),
    shortDesc = """Radical correction fitted to 41 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Int-5R!H-3R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S} {6,S}
4   R!H u0 {1,S} {5,[S,D,T,B,Q]}
5   C   u0 {3,S} {4,[S,D,T,B,Q]}
6   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0814053,-1.27103,-2.03838,-2.31326,-2.43545,-2.70864,-4.03814],'cal/mol/K','+|-',[6.31445,7.20964,6.20503,5.45092,4.32609,3.26033,3]),
        H298 = (73.0218,'kcal/mol','+|-',63.0318),
        S298 = (0.353786,'cal/mol/K','+|-',13.9152),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S} {6,S}
4   C   u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C   u0 r1 {3,S} {4,[S,D,T,B,Q]}
6   R!H ux r0 {3,S}
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
    index = 9,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S} {6,S}
4   O   u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C   u0 r1 {3,S} {4,[S,D,T,B,Q]}
6   R!H ux r0 {3,S}
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
    index = 10,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux {1,S} {5,D}
5   R!H ux {4,D}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16195,-1.25793,-2.40784,-3.12681,-3.9508,-4.52616,-5.40051],'cal/mol/K','+|-',[4.35545,4.30481,3.64105,3.31598,3.04141,3,3]),
        H298 = (73.3557,'kcal/mol','+|-',11.5457),
        S298 = (-0.535656,'cal/mol/K','+|-',8.10024),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 11,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux {1,S} {5,D} {7,[S,D,T,B,Q]}
5   C ux {4,D}
6   C ux {3,[S,D,T,B,Q]}
7   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.415293,-1.26658,-1.95141,-2.51088,-3.42608,-4.09214,-5.20797],'cal/mol/K','+|-',[3,3,3,3,3.11928,3.21756,3]),
        H298 = (72.3782,'kcal/mol','+|-',16.171),
        S298 = (1.37851,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 12,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {6,S}
4   C u0 {1,S} {5,D} {7,[S,D,T,B,Q]}
5   C u0 {4,D}
6   C u0 {3,S} {8,S}
7   C ux {4,[S,D,T,B,Q]}
8   C u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.521078,-1.21414,-1.95925,-2.34795,-3.03832,-3.65965,-4.74325],'cal/mol/K','+|-',[3.72537,3,3,3,3,3,3]),
        H298 = (63.5164,'kcal/mol','+|-',17.4357),
        S298 = (1.76138,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 13,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_8R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {6,S}
4   C u0 r1 {1,S} {5,D} {7,[S,D,T,B,Q]}
5   C u0 r0 {4,D}
6   C u0 r1 {3,S} {8,S}
7   C ux r1 {4,[S,D,T,B,Q]}
8   C u0 r1 {6,S}
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
    index = 14,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_N-8R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {6,S}
4   C u0 r1 {1,S} {5,D} {7,[S,D,T,B,Q]}
5   C u0 r0 {4,D}
6   C u0 r1 {3,S} {8,S}
7   C ux r1 {4,[S,D,T,B,Q]}
8   C u0 r0 {6,S}
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
    index = 15,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_5R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,D} {7,[S,D,T,B,Q]}
5   C ux r1 {4,D}
6   C ux r1 {3,[S,D,T,B,Q]}
7   C ux {4,[S,D,T,B,Q]}
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
    index = 16,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_N-5R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,D} {7,[S,D,T,B,Q]}
5   C ux r0 {4,D}
6   C ux r1 {3,[S,D,T,B,Q]}
7   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.934105,-1.3475,-2.65702,-4.01738,-5.88241,-6.69881,-7.67484],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (76.796,'kcal/mol','+|-',5.2),
        S298 = (1.77829,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Int-6R!H-5R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux {1,S} {5,D}
5   C ux {4,D} {6,[S,D,T,B,Q]}
6   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.11781,-0.198893,-2.20028,-3.31631,-4.12416,-4.55315,-5.39664],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.4608,'kcal/mol','+|-',5.2),
        S298 = (-7.81343,'cal/mol/K','+|-',3.72625),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 18,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Int-6R!H-5R!H_Ext-5R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,D}
5   C   ux r1 {4,D} {6,[S,D,T,B,Q]} {7,S}
6   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
7   C   u0 r0 {5,S}
8   R!H ux {3,[S,D,T,B,Q]}
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
    index = 19,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_5R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux {1,S} {5,D}
5   O   ux {4,D}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.57701,-0.286257,-1.78883,-2.56774,-3.47697,-4.33381,-5.19371],'cal/mol/K','+|-',[5.70493,5.94122,5.37947,4.72155,3.59308,3.07555,3.83775]),
        H298 = (77.7986,'kcal/mol','+|-',9.00875),
        S298 = (-0.0970819,'cal/mol/K','+|-',5.62429),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 20,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_5R!H->O_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux {1,S} {5,D}
5   O ux {4,D}
6   O ux {3,[S,D,T,B,Q]}
7   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00457552,-1.81927,-3.12044,-3.71588,-4.29618,-4.92291,-6.18306],'cal/mol/K','+|-',[3,3.76738,3.91412,3.59843,3.11673,3.25412,3]),
        H298 = (75.4181,'kcal/mol','+|-',5.2),
        S298 = (0.770592,'cal/mol/K','+|-',6.72285),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 21,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_5R!H->O_Ext-1R-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {8,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,D}
5   O   ux {4,D}
6   O   ux r1 {3,[S,D,T,B,Q]}
7   C   u0 r0 {1,S}
8   R!H ux {2,[S,D,T,B,Q]}
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
    index = 22,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_N-5R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {6,S}
4   C u0 {1,S} {5,D}
5   C u0 {4,D}
6   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.72373,-3.75176,-4.74204,-5.39273,-5.86558,-5.92699,-6.21997],'cal/mol/K','+|-',[3,7.58427,5.39431,3,3,3,4.02414]),
        H298 = (70.3468,'kcal/mol','+|-',5.2),
        S298 = (1.05959,'cal/mol/K','+|-',10.8635),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 23,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {7,[S,D,T,B,Q]}
3   C   u0 r1 {2,D} {6,S}
4   C   u0 r1 {1,S} {5,D}
5   C   u0 r1 {4,D}
6   C   u0 r1 {3,S}
7   R!H ux {2,[S,D,T,B,Q]}
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
    index = 24,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   R!H ux {1,S} {5,S}
5   R!H ux {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0519821,-0.979022,-1.85138,-2.34092,-2.97261,-3.51018,-4.42545],'cal/mol/K','+|-',[3,3,3.0304,3,3,3,3]),
        H298 = (79.8453,'kcal/mol','+|-',9.0946),
        S298 = (-0.335528,'cal/mol/K','+|-',7.05142),
    ),
    shortDesc = """Radical correction fitted to 28 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 25,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S} {6,[S,D,T,B,Q]}
5   R!H ux {4,S}
6   C   ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.25128,-0.0854819,-1.23327,-1.86152,-2.67608,-3.37351,-4.26623],'cal/mol/K','+|-',[3.12901,3.80941,3.72905,3.25556,3,3,3]),
        H298 = (83.7222,'kcal/mol','+|-',5.2),
        S298 = (-0.818631,'cal/mol/K','+|-',8.16264),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 26,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C ux {4,S}
6   C ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09558,0.0762402,-0.958163,-1.65569,-2.5483,-3.04631,-4.24061],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.3867,'kcal/mol','+|-',5.2),
        S298 = (0.792868,'cal/mol/K','+|-',5.45434),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 27,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_5R!H->C_Ext-5C-R_Ext-7R!H-R_Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,S}
4   C ux {1,S} {5,S} {6,S}
5   C ux {4,S} {7,S}
6   C ux {3,S} {4,S}
7   C u0 {5,S} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.54016,0.00357549,-1.40136,-2.17743,-2.90346,-3.06168,-4.18898],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.7223,'kcal/mol','+|-',5.2),
        S298 = (-1.43415,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 28,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_5R!H->C_Ext-5C-R_Ext-7R!H-R_Sp-8R!H-7R!H_5C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,S}
4   C ux r1 {1,S} {5,S} {6,S}
5   C ux r1 {4,S} {7,S}
6   C ux r1 {3,S} {4,S}
7   C u0 {5,S} {8,S}
8   C ux {7,S}
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
    index = 29,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_5R!H->C_Ext-5C-R_Ext-7R!H-R_Sp-8R!H-7R!H_N-5C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,S}
4   C ux r1 {1,S} {5,S} {6,S}
5   C ux r0 {4,S} {7,S}
6   C ux r1 {3,S} {4,S}
7   C u0 {5,S} {8,S}
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
    index = 30,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_5R!H->C_Ext-5C-R_Ext-7R!H-R_N-Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {6,[S,D,T,B,Q]}
4   C u0 r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5   C u0 {4,S} {7,[S,D,T,B,Q]}
6   C u0 r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
7   C ux {5,[S,D,T,B,Q]} {8,[B,D,T,Q]}
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
    index = 31,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,S}
4   C ux {1,S} {5,S} {6,S}
5   O ux {4,S}
6   C ux {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.47185,-0.314588,-1.623,-2.15312,-2.8571,-3.83705,-4.30253],'cal/mol/K','+|-',[5.16175,6.46784,6.09538,5.24487,3.62596,3,3]),
        H298 = (84.471,'kcal/mol','+|-',5.2),
        S298 = (-3.10159,'cal/mol/K','+|-',10.1708),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 32,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_N-5R!H->C_Ext-5O-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,S}
4   C ux {1,S} {5,S} {6,S}
5   O ux {4,S} {7,S}
6   C ux {3,S} {4,S}
7   O u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0041168,-2.12212,-3.30313,-3.62918,-3.89631,-4.69462,-4.66995],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.3499,'kcal/mol','+|-',5.2),
        S298 = (-2.05452,'cal/mol/K','+|-',13.438),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 33,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_N-5R!H->C_Ext-5O-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,S}
4   C   ux r1 {1,S} {5,S} {6,S}
5   O   ux {4,S} {7,S}
6   C   ux r1 {3,S} {4,S}
7   O   u0 r0 {5,S} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
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
    index = 34,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   R!H ux {1,S} {5,S}
5   C   ux {4,S} {6,S}
6   R!H ux {3,[S,D,T,B,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.176864,-1.19026,-2.13332,-2.66467,-3.34846,-3.9035,-4.77473],'cal/mol/K','+|-',[3,3,3.38477,3.08251,3,3,3]),
        H298 = (81.6275,'kcal/mol','+|-',7.89974),
        S298 = (-0.515616,'cal/mol/K','+|-',8.40472),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 35,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-2R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D} {7,[S,D,T,B,Q]}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {4,S} {6,S}
6   C ux {3,[S,D,T,B,Q]} {5,S}
7   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31863,-2.99985,-4.11612,-4.36493,-4.27904,-4.40175,-4.45997],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.8215,'kcal/mol','+|-',5.2),
        S298 = (-2.19635,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 36,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-2R!H-R_Ext-4R!H-R_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {7,[S,D,T,B,Q]}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S} {8,S}
5   C ux r1 {4,S} {6,S}
6   C ux r1 {3,[S,D,T,B,Q]} {5,S}
7   C ux {2,[S,D,T,B,Q]}
8   C u0 r0 {4,S}
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
C=C(C)CC1[CH]C(C)=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 37,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-2R!H-R_Ext-4R!H-R_N-8R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C                      ux r1 {1,[S,D,T,B,Q]} {3,D} {7,[S,D,T,B,Q]}
3   C                      ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C                      ux r1 {1,S} {5,S} {8,S}
5   C                      ux r1 {4,S} {6,S}
6   C                      ux r1 {3,[S,D,T,B,Q]} {5,S}
7   C                      ux {2,[S,D,T,B,Q]}
8   [P,F,I,Br,Cl,O,Si,S,N] u0 r0 {4,S}
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
    index = 38,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {4,S} {6,S}
6   C ux {3,[S,D,T,B,Q]} {5,S}
7   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0781109,-1.33604,-2.31184,-2.77054,-3.43633,-3.89803,-4.38638],'cal/mol/K','+|-',[3,3,3.48128,3,3,3,3]),
        H298 = (81.1655,'kcal/mol','+|-',5.2),
        S298 = (-3.06061,'cal/mol/K','+|-',10.5959),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 39,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-1R-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {6,S}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {4,S} {6,S} {8,[S,D,T,B,Q]}
6   C   u0 r1 {3,S} {5,S}
7   C   u0 r0 {1,S}
8   R!H ux {5,[S,D,T,B,Q]}
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
    index = 40,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-1R-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S} {8,[S,D,T,B,Q]}
5   C   ux r1 {4,S} {6,S}
6   C   ux r1 {3,[S,D,T,B,Q]} {5,S}
7   C   ux {1,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
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
    index = 41,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   R!H ux {1,S} {5,S}
5   C   ux {4,S} {6,S}
6   C   ux {3,[S,D,T,B,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0755363,-0.699692,-1.50996,-2.097,-3.01397,-3.73954,-4.80211],'cal/mol/K','+|-',[3,3,3.03285,3,3,3,3]),
        H298 = (81.0628,'kcal/mol','+|-',9.09414),
        S298 = (0.0659322,'cal/mol/K','+|-',7.47066),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 42,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_Ext-6C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,S}
4   C   ux {1,S} {5,S}
5   C   ux {4,S} {6,S}
6   C   ux {3,S} {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17096,0.318056,-0.710134,-1.36372,-2.41986,-3.17194,-4.48534],'cal/mol/K','+|-',[3.38171,3,3,3,3,3,3]),
        H298 = (79.8107,'kcal/mol','+|-',5.2),
        S298 = (2.63771,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 43,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_Ext-6C-R_Ext-6C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,S}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {4,S} {6,S}
6   C   ux r1 {3,S} {5,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
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
    index = 44,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {4,S} {6,S}
6   C ux {3,[S,D,T,B,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.311426,-1.11909,-1.90486,-2.3573,-3.05104,-3.68682,-4.63758],'cal/mol/K','+|-',[3,3,3.16522,3.15719,3,3,3]),
        H298 = (81.642,'kcal/mol','+|-',9.8755),
        S298 = (-0.495169,'cal/mol/K','+|-',8.48609),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 45,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]} {7,S}
4   C ux {1,S} {5,S}
5   C ux {4,S} {6,S}
6   C ux {3,[S,D,T,B,Q]} {5,S}
7   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.22455,-3.08861,-3.98525,-3.95284,-3.46926,-3.53705,-4.19852],'cal/mol/K','+|-',[3,3,3.70755,5.24138,5.97948,4.60391,3.75231]),
        H298 = (74.0755,'kcal/mol','+|-',5.2),
        S298 = (-5.62851,'cal/mol/K','+|-',14.0049),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 46,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-3R!H-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]} {7,S}
4   C   ux r1 {1,S} {5,S} {8,[S,D,T,B,Q]}
5   C   ux r1 {4,S} {6,S}
6   C   ux r1 {3,[S,D,T,B,Q]} {5,S}
7   C   u0 r1 {3,S}
8   R!H ux {4,[S,D,T,B,Q]}
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
    index = 47,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux {4,S} {6,S}
6   C   ux {3,[S,D,T,B,Q]} {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.439897,-0.609221,-1.49079,-2.10368,-3.20814,-4.04169,-4.97292],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.4936,'kcal/mol','+|-',11.1298),
        S298 = (1.05134,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 48,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-4C-R_7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {6,S}
4   C u0 r1 {1,S} {5,S} {7,S}
5   C u0 r1 {4,S} {6,S}
6   C u0 r1 {3,S} {5,S}
7   O u0 {4,S}
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
    index = 49,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-4C-R_N-7R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C ux {4,S} {6,S}
6   C ux {3,[S,D,T,B,Q]} {5,S}
7   C ux {4,[S,D,T,B,Q]}
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
    index = 50,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-4C-R_N-7R!H->O_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   ux r1 {4,S} {6,S}
6   C   ux r1 {3,[S,D,T,B,Q]} {5,S}
7   C   ux r0 {4,[S,D,T,B,Q]}
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
    index = 51,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   O ux r1 {1,S} {5,S}
5   C ux r1 {4,S} {6,S}
6   C ux r1 {3,[S,D,T,B,Q]} {5,S}
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
    index = 52,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   R!H ux r1 {1,S} {5,S}
5   C   ux r1 {4,S} {6,S}
6   O   ux r1 {3,[S,D,T,B,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21563,-2.59299,-4.57772,-5.34252,-4.96046,-4.81587,-6.73983],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.5875,'kcal/mol','+|-',5.2),
        S298 = (6.97426,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1O[CH]C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 53,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {4,S} {6,[B,D,T,Q]}
6   C ux {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.357693,-1.21321,-1.77648,-2.09955,-2.51705,-2.91634,-3.92363],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.1964,'kcal/mol','+|-',5.2),
        S298 = (0.304393,'cal/mol/K','+|-',3.52649),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 54,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,S}
4   C   ux r1 {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C   ux r1 {4,S} {6,[B,D,T,Q]}
6   C   ux r1 {3,S} {5,[B,D,T,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 55,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {4,S} {6,[B,D,T,Q]}
6   C   ux r1 {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
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
CCN(OC1=C[CH]CC=C1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 56,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S}
5   C   ux {4,S} {6,[B,D,T,Q]} {7,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0518089,-1.16337,-1.94926,-2.34357,-2.68837,-3.06552,-3.97495],'cal/mol/K','+|-',[3.12323,3,3.04659,3,3,3,3]),
        H298 = (74.2552,'kcal/mol','+|-',5.2),
        S298 = (-0.174653,'cal/mol/K','+|-',4.82366),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 57,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S}
5   C   ux {4,S} {6,[B,D,T,Q]} {7,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
7   R!H ux {5,[S,D,T,B,Q]} {8,S}
8   R!H u0 {7,S} {9,S}
9   C   ux {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.873412,-1.21331,-2.36936,-2.70694,-2.56139,-2.69009,-3.42314],'cal/mol/K','+|-',[3.879,4.45638,4.62131,4.37471,3.35801,3,3]),
        H298 = (73.5332,'kcal/mol','+|-',5.2),
        S298 = (-2.03069,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 58,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H_7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {4,S} {6,[B,D,T,Q]} {7,[S,D,T,B,Q]}
6   C   ux r1 {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
7   C   ux {5,[S,D,T,B,Q]} {8,S}
8   R!H u0 r0 {7,S} {9,S}
9   C   ux {8,S}
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
    index = 59,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H_N-7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {4,S} {6,[B,D,T,Q]} {7,[S,D,T,B,Q]}
6   C   ux r1 {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
7   O   ux {5,[S,D,T,B,Q]} {8,S}
8   R!H u0 r0 {7,S} {9,S}
9   C   ux {8,S}
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
    index = 60,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {6,S}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {4,S} {6,D} {7,S}
6   C   u0 r1 {3,S} {5,D}
7   R!H u0 r0 {5,S} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]} {9,[B,D,T,Q]}
9   C   u0 r0 {8,[B,D,T,Q]}
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
    index = 61,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {7,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {4,S} {6,[B,D,T,Q]}
6   C   ux r1 {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904953,-1.31393,-1.70958,-2.08704,-2.78061,-3.38515,-4.48546],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (75.5448,'kcal/mol','+|-',2.4),
        S298 = (1.55748,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC=CC[CH]1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 62,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 {1,[S,D,T,B,Q]} {3,D}
3   C   u0 r1 {2,D}
4   R!H u0 {1,S} {5,S}
5   C   u0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.557438,-0.736159,-1.91879,-2.39018,-2.87648,-3.47805,-4.21471],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.693,'kcal/mol','+|-',5.2),
        S298 = (-1.32996,'cal/mol/K','+|-',9.62275),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 63,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 {1,[S,D,T,B,Q]} {3,D}
3   C u0 r1 {2,D}
4   C u0 {1,S} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.133921,-1.02595,-2.21054,-2.78447,-3.06634,-3.3786,-4.48261],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.0813,'kcal/mol','+|-',7.35062),
        S298 = (1.40571,'cal/mol/K','+|-',7.74955),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 64,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_6R!H->C_Sp-2R!H-1R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D}
4   C u0 {1,S} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.452447,-0.521664,-1.92053,-2.67104,-2.9667,-3.01003,-4.26806],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.9595,'kcal/mol','+|-',5.2),
        S298 = (-0.717208,'cal/mol/K','+|-',3.45665),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 65,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_6R!H->C_Sp-2R!H-1R_Ext-6C-R_Sp-7R!H=6C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]} {7,D}
7   C u0 r1 {6,D}
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
    index = 66,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_6R!H->C_Sp-2R!H-1R_Ext-6C-R_N-Sp-7R!H=6C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]} {7,S}
7   C u0 r1 {6,S}
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
    index = 67,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_6R!H->C_N-Sp-2R!H-1R",
    group = 
"""
1 * C u1 r1 {2,D} {4,S}
2   C u0 r1 {1,D} {3,D}
3   C u0 r1 {2,D}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
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
    index = 68,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D}
4   R!H u0 {1,S} {5,S}
5   C   u0 {4,S} {6,S}
6   O   ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.799448,-0.570565,-1.75207,-2.16488,-2.76799,-3.53487,-4.06162],'cal/mol/K','+|-',[3,3,3.17689,3,3,3,3]),
        H298 = (84.5416,'kcal/mol','+|-',5.2),
        S298 = (-2.89321,'cal/mol/K','+|-',10.0951),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 69,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D}
4   C u0 {1,S} {5,S}
5   C u0 {4,S} {6,S}
6   O ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.914428,-0.837484,-2.06037,-2.42203,-3.03636,-3.73408,-4.02498],'cal/mol/K','+|-',[3,3.07915,3.34753,3,3,3,3]),
        H298 = (84.886,'kcal/mol','+|-',5.2),
        S298 = (-3.1694,'cal/mol/K','+|-',11.9841),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 70,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_4R!H->C_Ext-6BrClFINOPSSi-R_7R!H->N",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {4,S} {6,S}
6   O ux r0 {5,S} {7,S}
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
    index = 71,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_4R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D}
4   C u0 {1,S} {5,S}
5   C u0 {4,S} {6,S}
6   O ux {5,S} {7,S}
7   O u0 {6,S}
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
    index = 72,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_4R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_8R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {4,S} {6,S}
6   O ux r0 {5,S} {7,S}
7   O u0 r0 {6,S} {8,S}
8   C u0 r1 {7,S}
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
    index = 73,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_4R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_N-8R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {4,S} {6,S}
6   O ux r0 {5,S} {7,S}
7   O u0 r0 {6,S} {8,S}
8   C u0 r0 {7,S}
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
    index = 74,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D}
4   O u0 r1 {1,S} {5,S}
5   C u0 r1 {4,S} {6,S}
6   O ux r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.310784,0.563839,-0.441786,-1.07198,-1.62739,-2.68825,-4.21737],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.2358,'kcal/mol','+|-',5.2),
        S298 = (-1.71939,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1C=C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 75,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D}
4   R!H u0 r1 {1,[B,D,T,Q]}
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
    index = 76,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.570972,-0.522407,-1.50015,-2.01048,-2.62492,-3.13179,-4.26462],'cal/mol/K','+|-',[3,3.25463,4.11534,4.52076,4.96468,5.44317,6.55518]),
        H298 = (81.9855,'kcal/mol','+|-',66.4807),
        S298 = (1.3606,'cal/mol/K','+|-',10.9796),
    ),
    shortDesc = """Radical correction fitted to 29 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 77,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.673584,-1.01026,-2.2393,-2.64093,-3.0481,-3.43667,-4.93091],'cal/mol/K','+|-',[3.45526,4.38804,5.25367,5.66256,5.97478,6.21403,6.83697]),
        H298 = (95.9054,'kcal/mol','+|-',21.6949),
        S298 = (0.934466,'cal/mol/K','+|-',10.6253),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 78,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.754149,-0.627256,-1.7043,-2.09905,-2.6252,-2.82211,-4.10854],'cal/mol/K','+|-',[3,4.20761,4.7652,4.97778,5.22668,5.2195,5.2934]),
        H298 = (92.7356,'kcal/mol','+|-',12.2841),
        S298 = (3.17928,'cal/mol/K','+|-',10.2113),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 79,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C u0 {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.161109,-2.02106,-3.30248,-3.7981,-4.41409,-4.61207,-5.97314],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.9694,'kcal/mol','+|-',13.8033),
        S298 = (6.5951,'cal/mol/K','+|-',7.06923),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 80,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_2R!H-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   C   ux r0 {2,D}
4   C   u0 {1,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
6   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.503917,-2.52384,-3.85295,-4.31278,-4.82077,-4.88654,-6.37256],'cal/mol/K','+|-',[3.57334,3.29281,3,3,3,3,3]),
        H298 = (87.3822,'kcal/mol','+|-',17.9055),
        S298 = (6.89638,'cal/mol/K','+|-',9.88785),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 81,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_2R!H-inRing_Ext-2R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   C   ux r0 {2,D}
4   C   u0 r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
6   R!H u0 r1 {2,S}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 82,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.66941,0.766552,-0.106125,-0.400011,-0.836316,-1.03214,-2.24395],'cal/mol/K','+|-',[3,3.53452,4.33936,4.67549,5.25762,5.35061,5.03491]),
        H298 = (96.5018,'kcal/mol','+|-',5.2),
        S298 = (-0.236533,'cal/mol/K','+|-',8.40771),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 83,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_N-2R!H-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   u0 r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 84,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_N-2R!H-inRing_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {6,[S,D,T,B,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
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
    index = 85,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.613159,-1.29752,-2.64056,-3.04734,-3.36527,-3.8976,-5.54769],'cal/mol/K','+|-',[4.06006,4.71522,5.77255,6.33151,6.76094,7.07011,7.92076]),
        H298 = (98.2828,'kcal/mol','+|-',26.5712),
        S298 = (-0.749146,'cal/mol/K','+|-',10.2446),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 86,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   O   u0 {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.408413,-1.63567,-3.27342,-3.63241,-3.51742,-3.62782,-5.93582],'cal/mol/K','+|-',[5.85845,8.4982,9.44437,9.10779,6.83026,5.13641,8.73133]),
        H298 = (88.8526,'kcal/mol','+|-',26.186),
        S298 = (-2.01675,'cal/mol/K','+|-',11.5619),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 87,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C u0 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   O ux r0 {2,D}
4   O u0 {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
6   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0512609,-2.38013,-4.12603,-4.3966,-3.99547,-3.86318,-6.2463],'cal/mol/K','+|-',[8.09823,11.4515,12.6864,12.3243,9.37125,7.17188,12.2539]),
        H298 = (81.9185,'kcal/mol','+|-',14.7471),
        S298 = (-3.30761,'cal/mol/K','+|-',15.0785),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 88,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_4R!H->O_Ext-2R!H-R_2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   O ux r0 {2,D}
4   O u0 {1,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]}
6   C u0 {2,S}
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
    index = 89,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_4R!H->O_Ext-2R!H-R_N-2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   O ux r0 {2,D}
4   O u0 {1,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]}
6   C u0 {2,S}
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
    index = 90,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   C ux {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.736007,-1.09463,-2.26084,-2.6963,-3.27398,-4.05946,-5.31481],'cal/mol/K','+|-',[3.389,3,3.43417,5.19951,7.52034,8.59858,8.42324]),
        H298 = (103.941,'kcal/mol','+|-',21.5832),
        S298 = (0.0114139,'cal/mol/K','+|-',10.4459),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 91,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux {1,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.893729,-1.36087,-2.79966,-3.44553,-4.32119,-5.26032,-6.44373],'cal/mol/K','+|-',[3.82758,3,3,4.59101,6.79436,7.7541,7.7856]),
        H298 = (106.951,'kcal/mol','+|-',19.4793),
        S298 = (2.28721,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 92,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C u0 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   O ux r0 {2,D}
4   C u0 r1 {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
6   C u0 {2,S}
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
    index = 93,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C ux {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   C ux {1,S}
5   C u0 {1,S}
6   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.03359,-1.53483,-3.05843,-3.75915,-4.65778,-5.6545,-7.23778],'cal/mol/K','+|-',[4.63747,3,3.21979,5.40883,8.15634,9.29839,8.70582]),
        H298 = (111.38,'kcal/mol','+|-',9.92411),
        S298 = (1.78507,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 94,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C_2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C ux r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   C ux {1,S}
5   C u0 {1,S}
6   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.32243,-1.48639,-3.96857,-5.31914,-7.01035,-8.33048,-9.74087],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (114.124,'kcal/mol','+|-',5.2),
        S298 = (1.7891,'cal/mol/K','+|-',3.16579),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 95,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C_2R!H-inRing_Ext-6BrClFINOPSSi-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   ux r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   C   ux {1,S} {8,[S,D,T,B,Q]}
5   C   u0 r1 {1,S}
6   O   ux r1 {2,[S,D,T,B,Q]} {7,S}
7   O   u0 r1 {6,S}
8   R!H ux {4,[S,D,T,B,Q]}
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
    index = 96,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C_N-2R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C ux r0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   C ux r1 {1,S}
5   C u0 r1 {1,S}
6   O ux {2,[S,D,T,B,Q]}
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
    index = 97,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.677896,-0.0689183,-0.774061,-1.2908,-1.9108,-2.29324,-2.93428],'cal/mol/K','+|-',[3,3,3.45231,4.3735,5.72541,6.9134,9.01554]),
        H298 = (65.3227,'kcal/mol','+|-',115.133),
        S298 = (3.07911,'cal/mol/K','+|-',16.0491),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 98,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.71305,-0.28356,-1.07864,-1.67525,-2.56585,-3.11816,-4.12601],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.31,'kcal/mol','+|-',18.0635),
        S298 = (5.01706,'cal/mol/K','+|-',23.6908),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 99,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-3R!H-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   u0 r0 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {1,[S,D,T,B,Q]}
5   R!H u0 r0 {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 100,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-3R!H-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {5,D}
4   C   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   R!H ux {3,D}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 101,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-3R!H-R_5R!H->C",
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
    index = 102,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-3R!H-R_N-5R!H->C",
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
    index = 103,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-4C-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.733258,1.03329,0.976815,0.801333,0.781138,0.919157,0.349151],'cal/mol/K','+|-',[3,3,3,5.21182,8.307,10.5589,18.6773]),
        H298 = (7.28159,'kcal/mol','+|-',149.584),
        S298 = (-0.0632487,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 104,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-4C-R_5R!H->C_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]}
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
C=C1[CH]CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 105,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-4C-R_5R!H->C_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]}
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
    index = 106,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-4C-R_N-5R!H->C",
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
        Cpdata = ([0.495655,-1.29657,-2.81971,-3.68132,-4.56568,-5.34798,-5.14156],'cal/mol/K','+|-',[3.20312,3,3,4.0035,4.39612,5.24173,3]),
        H298 = (92.1274,'kcal/mol','+|-',13.135),
        S298 = (3.09835,'cal/mol/K','+|-',4.12952),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 107,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.63682,-2.2471,-3.87898,-5.09677,-6.11994,-7.20121,-5.96913],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.4835,'kcal/mol','+|-',5.2),
        S298 = (1.63834,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 108,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   O   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.3329,-0.33,-1.24673,-1.89237,-2.77132,-3.55378,-4.69628],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.3888,'kcal/mol','+|-',10.5014),
        S298 = (0.23703,'cal/mol/K','+|-',3.59254),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 109,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   O   ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.405179,-0.27339,-1.28681,-1.97256,-2.8417,-3.63086,-4.74542],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.0032,'kcal/mol','+|-',6.32967),
        S298 = (0.019225,'cal/mol/K','+|-',3.97413),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 110,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   O   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   u0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.08075,-0.183711,-1.70339,-2.49385,-3.23434,-4.04174,-5.05011],'cal/mol/K','+|-',[3,3.40856,3.86543,4.02069,3.57145,3,3]),
        H298 = (80.6741,'kcal/mol','+|-',6.40189),
        S298 = (0.0175341,'cal/mol/K','+|-',5.99961),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 111,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   O   ux {1,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   u0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.898683,-0.558578,-2.38459,-3.18555,-3.69754,-4.29654,-5.1741],'cal/mol/K','+|-',[3.30008,5.62118,5.99624,6.33688,5.86354,4.6845,3]),
        H298 = (83.1159,'kcal/mol','+|-',5.2),
        S298 = (2.33478,'cal/mol/K','+|-',4.21088),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 112,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_5R!H->C_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   O ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C u0 r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
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
C=C1[CH]OC(O)C1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 113,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_5R!H->C_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   O ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C u0 r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
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
    index = 114,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   O   ux {1,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]} {6,S}
6   C   u0 {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.26282,0.191155,-1.02219,-1.80215,-2.77113,-3.78694,-4.92611],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.2323,'kcal/mol','+|-',5.2),
        S298 = (-2.29971,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 115,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_N-5R!H->C_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   O   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]} {6,S}
6   C   u0 r1 {5,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
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
    index = 116,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   O ux r1 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
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
    index = 117,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   O ux r1 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
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
    index = 118,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.105718,-1.36512,-2.34274,-2.91411,-3.60307,-4.17918,-5.35781],'cal/mol/K','+|-',[3.372,4.48009,4.785,4.6335,3.98513,3.66559,4.20361]),
        H298 = (101.009,'kcal/mol','+|-',9.25354),
        S298 = (1.50424,'cal/mol/K','+|-',7.1316),
    ),
    shortDesc = """Radical correction fitted to 56 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 119,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,S}
3   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.07618,-2.12757,-2.86322,-3.34204,-3.91145,-4.27936,-5.02398],'cal/mol/K','+|-',[3,4.09177,5.02108,5.02199,3.9686,3,3]),
        H298 = (114.247,'kcal/mol','+|-',22.3347),
        S298 = (2.74022,'cal/mol/K','+|-',7.1913),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 120,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux r1 {1,D} {3,S} {4,[S,D,T,B,Q]}
3   R!H u0 r1 {2,S}
4   R!H ux {2,[S,D,T,B,Q]}
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
    index = 121,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.154341,-1.33376,-2.32133,-2.89651,-3.59038,-4.17506,-5.37154],'cal/mol/K','+|-',[3.39886,4.529,4.83302,4.67831,4.03101,3.72232,4.2813]),
        H298 = (100.424,'kcal/mol','+|-',7.04292),
        S298 = (1.4534,'cal/mol/K','+|-',7.19725),
    ),
    shortDesc = """Radical correction fitted to 54 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 122,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   O   ux {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.602941,-1.06474,-1.57277,-1.94127,-2.44619,-2.85177,-3.66024],'cal/mol/K','+|-',[3.21868,3.29826,2.83939,2.14567,2,2.4409,2.90313]),
        H298 = (103.771,'kcal/mol','+|-',3.48406),
        S298 = (0.390994,'cal/mol/K','+|-',2.43152),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 123,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   O u0 {1,S} {2,[S,D,T,B,Q]}
5   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.78768,-2.17182,-2.41818,-2.34071,-2.00817,-1.92502,-2.52922],'cal/mol/K','+|-',[5.16778,6.02625,5.43651,3.8694,2,2.08845,4.51404]),
        H298 = (101.742,'kcal/mol','+|-',2.4),
        S298 = (-0.680983,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 124,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_Ext-1R-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   u0 r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   O   u0 r1 {1,S} {2,[S,D,T,B,Q]}
5   C   u0 r0 {1,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 125,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {2,S}
4   O u0 {1,S} {2,S}
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
    index = 126,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_3R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,S} {4,S} {5,[S,D,T,B,Q]}
3   C   u0 r0 {2,S}
4   O   u0 r1 {1,S} {2,S}
5   R!H ux {2,[S,D,T,B,Q]}
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
    index = 127,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_3R!H->C_Ext-3C-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   C u0 r0 {2,S} {5,S}
4   O u0 r1 {1,S} {2,S}
5   C u0 r0 {3,S}
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
    index = 128,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_3R!H->C_Ext-3C-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,S} {4,S}
3   C                      u0 r0 {2,S} {5,S}
4   O                      u0 r1 {1,S} {2,S}
5   [P,F,I,Br,Cl,O,Si,S,N] u0 r0 {3,S}
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
    index = 129,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   O ux r1 {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
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
    index = 130,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.27857,-1.28395,-2.53628,-3.16359,-3.89613,-4.60474,-6.13265],'cal/mol/K','+|-',[3.43389,5.1574,5.72749,5.61235,4.76824,4.20739,4.84043]),
        H298 = (100.213,'kcal/mol','+|-',6.77019),
        S298 = (1.65266,'cal/mol/K','+|-',9.16621),
    ),
    shortDesc = """Radical correction fitted to 32 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 131,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0560091,-1.25358,-2.36408,-3.05715,-3.86417,-4.55887,-6.41855],'cal/mol/K','+|-',[3.22555,5.23371,5.85118,5.84976,5.03752,4.45788,4.99675]),
        H298 = (100.162,'kcal/mol','+|-',6.97131),
        S298 = (2.62597,'cal/mol/K','+|-',8.01941),
    ),
    shortDesc = """Radical correction fitted to 26 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 132,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.812077,-2.64662,-3.63402,-4.15076,-4.62429,-5.09436,-6.66475],'cal/mol/K','+|-',[3.65166,5.97743,6.73801,6.87801,6.01302,5.21387,5.46897]),
        H298 = (98.9289,'kcal/mol','+|-',8.55945),
        S298 = (3.09461,'cal/mol/K','+|-',10.7774),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 133,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.270877,-1.2069,-2.13474,-2.69008,-3.31387,-3.87445,-5.44165],'cal/mol/K','+|-',[3,4.6511,5.91559,6.4997,5.76143,4.54771,5.36568]),
        H298 = (98.227,'kcal/mol','+|-',5.2),
        S298 = (0.395216,'cal/mol/K','+|-',7.79901),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 134,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {6,[S,D,T,B,Q]}
3   O   u0 r1 {2,S}
4   O   u0 {1,S}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 135,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_5R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.297142,-0.727325,-1.25771,-1.77369,-2.65464,-3.35734,-4.50005],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.9405,'kcal/mol','+|-',2.4),
        S298 = (-0.151826,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 136,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_5R!H-inRing_2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   O   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S}
4   O   u0 r0 {1,S}
5   R!H u0 r1 {1,S}
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
    index = 137,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_5R!H-inRing_N-2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.199423,-0.458743,-0.89314,-1.41874,-2.34797,-3.11394,-4.39452],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.1296,'kcal/mol','+|-',2.4),
        S298 = (0.0656898,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 138,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_5R!H-inRing_N-2R!H->O_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux r1 {1,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
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
    index = 139,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_N-5R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   O u0 r1 {2,S}
4   O u0 {1,S}
5   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.48664,-4.74497,-6.99758,-7.9848,-7.80848,-7.41188,-8.88386],'cal/mol/K','+|-',[3,3,3,3,3,3,10.3162]),
        H298 = (99.5541,'kcal/mol','+|-',10.8824),
        S298 = (5.82388,'cal/mol/K','+|-',5.07554),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 140,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_N-5R!H-inRing_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S}
4   O   u0 r1 {1,S}
5   C   u0 r0 {1,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 141,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.69153,-4.98616,-6.07034,-6.52436,-6.75371,-7.07672,-8.65229],'cal/mol/K','+|-',[4.79102,5.00207,5.2783,4.91763,3.90944,3.76793,3]),
        H298 = (100.928,'kcal/mol','+|-',15.3063),
        S298 = (7.48112,'cal/mol/K','+|-',9.22472),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 142,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Int-7R!H-6R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C   ux {1,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.45166,-4.65451,-5.99457,-6.56517,-6.86564,-7.42424,-8.01005],'cal/mol/K','+|-',[3,5.14839,5.97005,5.83161,4.02457,3.4162,3.83754]),
        H298 = (96.7253,'kcal/mol','+|-',6.0271),
        S298 = (8.89284,'cal/mol/K','+|-',13.7401),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 143,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Int-7R!H-6R!H_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {6,S}
4   C   ux {1,[S,D,T,B,Q]}
5   C   u0 r1 {1,S} {7,[S,D,T,B,Q]}
6   C   u0 r1 {3,S} {7,S}
7   R!H ux r1 {5,[S,D,T,B,Q]} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.07604,-7.57293,-9.41019,-9.92771,-9.09185,-8.60119,-5.88796],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.7779,'kcal/mol','+|-',5.2),
        S298 = (16.7931,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1OC[C](C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 144,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Int-7R!H-6R!H_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C u0 {1,S} {3,S}
3   O u0 r1 {2,S} {6,[S,D,T,B,Q]}
4   C u0 {1,S}
5   C ux {1,[S,D,T,B,Q]} {7,S}
6   O ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C u0 {5,S} {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.63947,-3.1953,-4.28676,-4.88391,-5.75254,-6.83576,-9.07109],'cal/mol/K','+|-',[3,3,3,3,3,3.8768,3]),
        H298 = (95.199,'kcal/mol','+|-',5.2),
        S298 = (4.9427,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 145,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Int-7R!H-6R!H_N-6R!H->C_4C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C u0 r1 {1,S} {3,S}
3   O u0 r1 {2,S} {6,[S,D,T,B,Q]}
4   C u0 r1 {1,S}
5   C ux r1 {1,[S,D,T,B,Q]} {7,S}
6   O ux r1 {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C u0 r1 {5,S} {6,[S,D,T,B,Q]}
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
    index = 146,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Int-7R!H-6R!H_N-6R!H->C_N-4C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C u0 r1 {1,S} {3,S}
3   O u0 r1 {2,S} {6,[S,D,T,B,Q]}
4   C u0 r0 {1,S}
5   C ux r1 {1,[S,D,T,B,Q]} {7,S}
6   O ux r1 {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C u0 r1 {5,S} {6,[S,D,T,B,Q]}
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
C[C]1CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 147,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_4C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]}
4   C   ux r1 {1,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.66413,-3.64778,-4.46949,-4.99953,-5.30109,-5.39937,-9.65126],'cal/mol/K','+|-',[3.34647,3,3,3,3,3,3]),
        H298 = (99.8437,'kcal/mol','+|-',5.2),
        S298 = (6.11958,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 148,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_4C-inRing_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux r1 {1,[S,D,T,B,Q]}
5   C ux r0 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r0 {5,[S,D,T,B,Q]}
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
    index = 149,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_4C-inRing_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux r1 {1,[S,D,T,B,Q]}
5   C ux r0 {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.48097,-3.08702,-4.2415,-5.02272,-5.57162,-5.93599,-10.2196],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.579,'kcal/mol','+|-',5.2),
        S298 = (6.09934,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 150,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_N-4C-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S}
4   C   u0 r0 {1,S}
5   C   u0 r1 {1,S} {6,S}
6   R!H u0 r1 {5,S}
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
    index = 151,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.441391,-0.535495,-1.69673,-2.49266,-3.49889,-4.29466,-6.25653],'cal/mol/K','+|-',[3,3.37316,4.62547,4.85057,4.40073,4.22769,5.2196]),
        H298 = (100.522,'kcal/mol','+|-',5.6821),
        S298 = (2.9023,'cal/mol/K','+|-',5.16506),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 152,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Int-5C-3O",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S} {5,[S,D,T,B,Q]}
4   R!H u0 {1,S} {5,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
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
    index = 153,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.243335,-0.537091,-1.6118,-2.31941,-3.36058,-4.3206,-6.66983],'cal/mol/K','+|-',[3,4.88965,6.10483,6.11696,5.58776,5.69716,4.90246]),
        H298 = (100.88,'kcal/mol','+|-',5.2),
        S298 = (3.64352,'cal/mol/K','+|-',9.17133),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 154,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_5C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,S}
3   O u0 r1 {2,S}
4   C u0 r1 {1,S} {5,S} {6,S}
5   C u0 r1 {4,S}
6   O u0 r1 {4,S}
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
    index = 155,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_N-5C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux r0 {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.667826,0.408438,-0.508343,-1.20289,-2.2882,-3.19668,-6.16821],'cal/mol/K','+|-',[3,3,3.39065,3.27239,3,3,5.08073]),
        H298 = (101.226,'kcal/mol','+|-',5.2),
        S298 = (1.85964,'cal/mol/K','+|-',3.31289),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 156,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_N-5C-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]}
4   C   ux r1 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C   ux r0 {4,[S,D,T,B,Q]}
6   O   ux r1 {4,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
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
    index = 157,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_N-5C-inRing_Int-6R!H-3O_Ext-5C-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S}
4   C   u0 r1 {1,S} {5,S} {6,S}
5   C   u0 r0 {4,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   O   u0 r1 {4,S}
7   R!H ux {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
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
    index = 158,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Int-3O-1R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
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
    index = 159,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.23563,-0.0199498,-1.36665,-2.42178,-3.7279,-4.72216,-5.50379],'cal/mol/K','+|-',[3,3,3.66308,4.7679,5.38699,5.72591,4.46466]),
        H298 = (103.534,'kcal/mol','+|-',5.2),
        S298 = (2.23238,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 160,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_4R!H->C_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {6,S}
4   C   ux {1,[S,D,T,B,Q]} {5,S}
5   C   ux {4,S}
6   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.30071,-0.752339,-2.83343,-4.35701,-5.90154,-7.03145,-7.10993],'cal/mol/K','+|-',[3,3,3,3,3,3,3.55104]),
        H298 = (103.741,'kcal/mol','+|-',5.26033),
        S298 = (2.61471,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 161,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_4R!H->C_Ext-3O-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {6,S}
4   C   ux r1 {1,[S,D,T,B,Q]} {5,S}
5   C   ux r1 {4,S} {7,[S,D,T,B,Q]}
6   R!H u0 r1 {3,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.78631,-1.02221,-3.36002,-4.88675,-6.58289,-7.76231,-8.36541],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.881,'kcal/mol','+|-',5.2),
        S298 = (1.95745,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C[CH]COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 162,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,S}
3   O u0 r1 {2,S}
4   O u0 {1,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0449272,-1.38961,-2.70822,-3.42537,-4.00713,-4.35472,-6.73253],'cal/mol/K','+|-',[3,5.65298,8.60196,8.99223,7.18341,5.26661,10.6194]),
        H298 = (98.9139,'kcal/mol','+|-',7.20415),
        S298 = (2.75255,'cal/mol/K','+|-',4.05258),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 163,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_N-4R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,S} {6,[S,D,T,B,Q]}
3   O   u0 r1 {2,S}
4   O   u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C   u0 r1 {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
    index = 164,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]}
4   C   ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.82218,1.20551,-0.170222,-1.12954,-2.42246,-3.56904,-6.11609],'cal/mol/K','+|-',[3,3,3,3,3,3,3.75788]),
        H298 = (102.976,'kcal/mol','+|-',5.2),
        S298 = (-0.151031,'cal/mol/K','+|-',3.31383),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 165,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.80025,1.15401,-0.101953,-1.00428,-2.32341,-3.38088,-5.82447],'cal/mol/K','+|-',[3.26669,3.04543,3.11851,3,3,3,4.79623]),
        H298 = (102.714,'kcal/mol','+|-',5.2),
        S298 = (-0.517345,'cal/mol/K','+|-',3.89526),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 166,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_2R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]}
4   C   ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   u0 {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.201088,-0.336838,-1.62857,-2.15982,-2.6685,-3.46148,-8.17239],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.59,'kcal/mol','+|-',5.2),
        S298 = (1.38952,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 167,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O u0 r1 {1,S} {3,S}
3   O u0 r1 {2,S}
4   C u0 {1,S} {5,S}
5   O ux {4,S}
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
    index = 168,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.61394,-1.46617,-3.56949,-3.80219,-4.08789,-4.87996,-4.41724],'cal/mol/K','+|-',[3.73,5.17261,4.91192,4.16754,3.05452,3,3]),
        H298 = (100.692,'kcal/mol','+|-',5.2),
        S298 = (-4.18724,'cal/mol/K','+|-',6.8436),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 169,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.877465,-2.4633,-4.48557,-4.58441,-4.6867,-5.37403,-4.56503],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.8058,'kcal/mol','+|-',5.2),
        S298 = (-4.04873,'cal/mol/K','+|-',7.61367),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 170,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
7   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.756882,-2.74024,-4.8139,-4.8126,-4.80768,-5.46278,-4.44857],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.185,'kcal/mol','+|-',5.2),
        S298 = (-4.38822,'cal/mol/K','+|-',8.61493),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 171,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S}
3   O u0 r0 {2,S} {4,S}
4   O u0 {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,S} {7,[S,D,T,B,Q]}
6   C u0 {5,S}
7   C ux {5,[S,D,T,B,Q]} {8,S}
8   C u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.696177,-3.19718,-5.43713,-5.35521,-4.99475,-5.48245,-4.56725],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.1533,'kcal/mol','+|-',5.2),
        S298 = (-1.13038,'cal/mol/K','+|-',7.17273),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 172,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H_Ext-8R!H-R_Ext-6R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S}
2    C   u0 r1 {1,S} {3,S}
3    O   u0 r0 {2,S} {4,S}
4    O   u0 r0 {3,S} {5,[S,D,T,B,Q]}
5    C   ux r1 {4,[S,D,T,B,Q]} {6,S} {7,[S,D,T,B,Q]}
6    C   u0 r1 {5,S} {10,[S,D,T,B,Q]}
7    C   ux r1 {5,[S,D,T,B,Q]} {8,S}
8    C   u0 r1 {7,S} {9,S}
9    C   u0 r1 {8,S}
10   R!H ux {6,[S,D,T,B,Q]}
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
    index = 173,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]} {7,S}
6   C ux {5,[S,D,T,B,Q]}
7   C u0 {5,S} {8,[B,D,T,Q]}
8   C ux {7,[B,D,T,Q]}
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
    index = 174,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H-7R!H_5R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,S}
5   C u0 r1 {4,S} {6,[S,D,T,B,Q]} {7,S}
6   C ux {5,[S,D,T,B,Q]}
7   C u0 {5,S} {8,[B,D,T,Q]}
8   C ux {7,[B,D,T,Q]}
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
    index = 175,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H-7R!H_N-5R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,S}
5   C u0 r0 {4,S} {6,[S,D,T,B,Q]} {7,S}
6   C ux {5,[S,D,T,B,Q]}
7   C u0 {5,S} {8,[B,D,T,Q]}
8   C ux {7,[B,D,T,Q]}
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
    index = 176,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.367347,-1.57732,-2.36718,-2.96793,-3.70124,-4.16732,-4.99435],'cal/mol/K','+|-',[3.46382,4.15883,4.00273,3.7326,3.12414,3,3]),
        H298 = (98.2994,'kcal/mol','+|-',6.01298),
        S298 = (1.70758,'cal/mol/K','+|-',4.61324),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 177,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.685762,-1.66833,-2.49793,-3.11527,-3.85145,-4.27532,-5.13548],'cal/mol/K','+|-',[3.51177,4.66553,4.533,4.18452,3.3698,3,3]),
        H298 = (97.4719,'kcal/mol','+|-',5.86143),
        S298 = (1.89712,'cal/mol/K','+|-',5.09833),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 178,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.13599,-2.7209,-3.64194,-4.19755,-4.61441,-4.72356,-5.39751],'cal/mol/K','+|-',[3.96936,5.18403,4.83309,4.34637,3.62939,3.0699,3]),
        H298 = (99.8688,'kcal/mol','+|-',5.2),
        S298 = (3.06913,'cal/mol/K','+|-',5.4586),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 179,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.60872,-2.76498,-3.56921,-4.02898,-4.35721,-4.41234,-5.02927],'cal/mol/K','+|-',[3.8627,5.90328,5.48932,4.88236,3.81396,3,3]),
        H298 = (100.035,'kcal/mol','+|-',5.2),
        S298 = (2.6239,'cal/mol/K','+|-',5.75145),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 180,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2R!H",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   R!H u0 r1 {4,S} {6,S}
6   C   ux r1 {2,[S,D,T,B,Q]} {5,S} {7,S}
7   R!H u0 {6,S}
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
    index = 181,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Int-5R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,S}
5   R!H ux r1 {1,[S,D,T,B,Q]} {4,S} {6,S}
6   C   ux r1 {5,S} {7,S}
7   R!H ux {6,S}
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
    index = 182,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Sp-4C-3C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,S}
5   R!H ux {4,S} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.27479,-4.87152,-5.67318,-5.87376,-5.72955,-5.41397,-5.09027],'cal/mol/K','+|-',[3,5.77129,4.64036,4.09993,3.45585,3,3]),
        H298 = (99.4941,'kcal/mol','+|-',5.2),
        S298 = (2.52527,'cal/mol/K','+|-',5.75351),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 183,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Sp-4C-3C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {8,D}
4   C   ux {3,S} {5,S}
5   C   ux {4,S} {6,S}
6   C   ux {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H u0 {3,D}
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
    index = 184,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Sp-4C-3C_Ext-3C-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {9,[S,D,T,B,Q]}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S} {8,D}
4   C   ux {3,S} {5,S}
5   C   ux {4,S} {6,S}
6   C   ux {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H u0 {3,D}
9   R!H ux {1,[S,D,T,B,Q]}
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
    index = 185,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Sp-4C-3C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {8,[S,D,T,B,Q]}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux r1 {3,S} {5,S}
5   R!H ux r1 {4,S} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,S}
7   C   ux r1 {6,S}
8   R!H ux {1,[S,D,T,B,Q]}
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
    index = 186,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_N-Sp-4C-3C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,D}
4   C   ux r1 {3,D} {5,S}
5   R!H ux r1 {4,S} {6,S}
6   C   ux r1 {5,S} {7,S}
7   R!H ux {6,S}
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
    index = 187,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {7,[S,D,T,B,Q]}
2   R!H ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   ux r1 {3,S} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]} {6,S}
6   C   ux {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
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
    index = 188,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.406262,-0.150517,-1.19282,-2.03515,-3.41536,-4.34774,-5.30107],'cal/mol/K','+|-',[5.26958,3,3,3,3,3,3.35322]),
        H298 = (97.6553,'kcal/mol','+|-',5.2),
        S298 = (1.18309,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 189,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   ux r1 {3,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
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
    index = 190,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]}
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
    index = 191,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_N-2R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]}
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
    index = 192,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   O   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.674738,-1.27949,-1.93924,-2.48574,-3.20963,-3.81385,-4.53248],'cal/mol/K','+|-',[3,3,3,3,3,3.03698,3]),
        H298 = (100.512,'kcal/mol','+|-',5.2),
        S298 = (1.08728,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 193,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_N-4R!H->C_Ext-3C-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   R!H u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {5,[S,D,T,B,Q]}
4   O   ux {3,S}
5   O   ux {3,[S,D,T,B,Q]}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13142,-1.78144,-2.41429,-2.88789,-3.4206,-3.94836,-4.48295],'cal/mol/K','+|-',[3.94755,3,3,3,3.63488,4.76945,3]),
        H298 = (101.886,'kcal/mol','+|-',5.2),
        S298 = (1.06703,'cal/mol/K','+|-',4.40466),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 194,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_N-4R!H->C_Ext-3C-R_Ext-1R-R_2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
4   O   ux r1 {3,S}
5   O   ux {3,[S,D,T,B,Q]}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.801046,-0.482768,-2.29708,-3.81123,-5.2,-6.28317,-5.84944],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (104.624,'kcal/mol','+|-',5.2),
        S298 = (3.22327,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C[CH]CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 195,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_N-4R!H->C_Ext-3C-R_Ext-1R-R_N-2R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {5,S}
4   O   ux r1 {3,S}
5   O   ux {3,S}
6   R!H u0 {1,S}
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
    index = 196,
    label = "RJ1_N-1R-inRing",
    group = 
"""
1 * R u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.721844,-1.63527,-2.3071,-2.70572,-3.11441,-3.49312,-4.25752],'cal/mol/K','+|-',[4.05795,4.82606,5.12943,5.02438,4.51734,4.18214,4.03543]),
        H298 = (94.1594,'kcal/mol','+|-',23.6717),
        S298 = (0.0413612,'cal/mol/K','+|-',9.68634),
    ),
    shortDesc = """Radical correction fitted to 625 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 197,
    label = "RJ1_N-1R-inRing_1R->O",
    group = 
"""
1 * O u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8593,-3.05963,-3.77159,-4.04607,-4.1038,-4.24895,-4.62136],'cal/mol/K','+|-',[4.43045,5.37769,5.74348,5.63907,5.088,4.7379,4.53096]),
        H298 = (91.8002,'kcal/mol','+|-',25.5301),
        S298 = (-0.634655,'cal/mol/K','+|-',9.66108),
    ),
    shortDesc = """Radical correction fitted to 262 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 198,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.86463,-3.07209,-3.78758,-4.06246,-4.11749,-4.26092,-4.63048],'cal/mol/K','+|-',[4.44342,5.38712,5.74942,5.64374,5.09404,4.74475,4.54068]),
        H298 = (91.5351,'kcal/mol','+|-',25.0746),
        S298 = (-0.612767,'cal/mol/K','+|-',9.67869),
    ),
    shortDesc = """Radical correction fitted to 261 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 199,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.90189,-3.01794,-3.60415,-3.70123,-3.58402,-3.57204,-3.91348],'cal/mol/K','+|-',[4.96398,6.03058,6.15836,5.68307,4.54839,3.979,3.67894]),
        H298 = (94.8192,'kcal/mol','+|-',34.8639),
        S298 = (0.202235,'cal/mol/K','+|-',9.80571),
    ),
    shortDesc = """Radical correction fitted to 110 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 200,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.85157,-4.44412,-4.90659,-4.77095,-4.20817,-3.81098,-3.6716],'cal/mol/K','+|-',[4.11018,5.47357,5.69463,5.01756,3.72578,3.54007,3.69608]),
        H298 = (81.0763,'kcal/mol','+|-',29.7062),
        S298 = (1.69555,'cal/mol/K','+|-',9.63922),
    ),
    shortDesc = """Radical correction fitted to 53 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 201,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.87856,-4.56076,-5.04088,-4.87416,-4.22235,-3.76103,-3.5696],'cal/mol/K','+|-',[4.2685,5.62357,5.83915,5.15805,3.85509,3.64925,3.77084]),
        H298 = (77.5982,'kcal/mol','+|-',22.3144),
        S298 = (1.74925,'cal/mol/K','+|-',10.0236),
    ),
    shortDesc = """Radical correction fitted to 50 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 202,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.4795,-2.9661,-3.15872,-3.18473,-3.10791,-3.09407,-3.59867],'cal/mol/K','+|-',[3,3.12369,3.4741,3,3,3,3]),
        H298 = (66.803,'kcal/mol','+|-',16.4121),
        S298 = (-0.910946,'cal/mol/K','+|-',7.13899),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 203,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.30245,-2.63149,-2.80364,-2.88544,-2.9394,-3.0329,-3.66292],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (65.8986,'kcal/mol','+|-',13.8191),
        S298 = (-1.07855,'cal/mol/K','+|-',7.3477),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 204,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {2,[S,D,T,B,Q]} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.53127,-2.85085,-2.98734,-3.04625,-3.11808,-3.138,-3.95162],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (63.3235,'kcal/mol','+|-',11.7227),
        S298 = (0.739813,'cal/mol/K','+|-',9.86059),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 205,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C_Ext-5C-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {2,[S,D,T,B,Q]} {5,S}
5   C u0 {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.51027,-2.80635,-3.01335,-3.10135,-3.14911,-3.07272,-4.12113],'cal/mol/K','+|-',[3,3,3.14912,3,3,3,3]),
        H298 = (67.2647,'kcal/mol','+|-',5.41989),
        S298 = (1.48749,'cal/mol/K','+|-',15.2103),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 206,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   O   ux r1 {2,[S,D,T,B,Q]} {5,S}
5   C   u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
CC1C=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 207,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C_Ext-5C-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r1 {1,S} {3,D} {4,S}
3   C                      u0 r1 {2,D}
4   O                      u0 r1 {2,S} {5,S}
5   C                      ux r1 {4,S} {6,[S,D,T,B,Q]}
6   [P,F,I,Br,Cl,O,Si,S,N] u0 r1 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.5616,-2.91511,-2.94976,-2.96665,-3.07325,-3.2323,-3.70676],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (58.5428,'kcal/mol','+|-',2.4),
        S298 = (-0.34016,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 208,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,S}
5   O   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13465,-2.47062,-2.66893,-2.76751,-2.80837,-2.95582,-3.45121],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (68.0579,'kcal/mol','+|-',16.1463),
        S298 = (-2.41201,'cal/mol/K','+|-',4.88046),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 209,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {6,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]} {5,S}
5   O   ux {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97328,-2.63531,-2.97651,-3.05062,-2.95347,-3.01555,-3.41223],'cal/mol/K','+|-',[3,3,3.01475,3,3,3,3]),
        H298 = (70.2575,'kcal/mol','+|-',20.3905),
        S298 = (-2.3923,'cal/mol/K','+|-',6.07175),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 210,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C_Ext-3C-R_Int-6R!H-5O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {6,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]} {5,S}
5   O   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.0455,-2.46174,-2.72133,-2.77952,-2.70774,-2.83984,-3.2775],'cal/mol/K','+|-',[3,3.14494,3.28595,3,3,3,3]),
        H298 = (67.4251,'kcal/mol','+|-',7.88988),
        S298 = (-3.45496,'cal/mol/K','+|-',3.73697),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 211,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C_Ext-3C-R_Int-6R!H-5O_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]}
4   R!H ux r1 {2,[S,D,T,B,Q]} {5,S}
5   O   u0 r1 {4,S} {6,S}
6   R!H ux r1 {3,[S,D,T,B,Q]} {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63247,-4.5066,-4.67366,-4.00455,-2.83164,-2.33266,-1.55225],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (72.2984,'kcal/mol','+|-',5.2),
        S298 = (-4.32244,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=C(O)C(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 212,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C_Ext-3C-R_Int-6R!H-5O_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   R!H ux r1 {2,[S,D,T,B,Q]} {5,S}
5   O   ux r1 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12607,-2.63572,-3.29797,-3.53999,-3.67747,-3.99023,-4.40596],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (62.4702,'kcal/mol','+|-',5.2),
        S298 = (-5.54909,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=C(COO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 213,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   R!H ux r1 {2,[S,D,T,B,Q]} {5,[B,D,T,Q]}
5   R!H u0 r1 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.7811,-7.31601,-7.77464,-7.07555,-5.29851,-3.88931,-2.7634],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.4047,'kcal/mol','+|-',5.2),
        S298 = (1.26789,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=C(O)CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 214,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.99087,-5.00951,-5.57054,-5.34957,-4.53596,-3.94872,-3.56142],'cal/mol/K','+|-',[4.72943,5.87259,5.96681,5.27562,4.05849,4.02564,4.18648]),
        H298 = (81.4373,'kcal/mol','+|-',19.0371),
        S298 = (2.49785,'cal/mol/K','+|-',10.2965),
    ),
    shortDesc = """Radical correction fitted to 41 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 215,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.58184,-5.58998,-6.01654,-5.63788,-4.60219,-3.90388,-3.46801],'cal/mol/K','+|-',[4.38163,5.8635,6.14879,5.7067,4.78837,4.82749,4.47357]),
        H298 = (78.2885,'kcal/mol','+|-',24.7065),
        S298 = (1.99372,'cal/mol/K','+|-',9.19123),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 216,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.66613,-6.32691,-6.95836,-6.44761,-4.91079,-3.97699,-3.3887],'cal/mol/K','+|-',[5.09867,6.43072,6.48818,5.8455,4.44923,4.22464,4.63872]),
        H298 = (90.3853,'kcal/mol','+|-',10.183),
        S298 = (2.01991,'cal/mol/K','+|-',7.50956),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 217,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.26008,-5.79917,-6.41963,-5.88814,-4.31181,-3.35852,-3.15539],'cal/mol/K','+|-',[5.58966,6.63462,6.18506,5.03558,3,3,5.22885]),
        H298 = (91.5333,'kcal/mol','+|-',9.09906),
        S298 = (1.04834,'cal/mol/K','+|-',6.96769),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 218,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R",
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
        Cpdata = ([-3.93764,-6.83722,-7.49287,-6.73503,-4.61224,-3.38169,-3.18292],'cal/mol/K','+|-',[7.57164,8.6345,7.67312,6.08253,3.64836,3.64552,7.95167]),
        H298 = (93.5364,'kcal/mol','+|-',10.0015),
        S298 = (0.629669,'cal/mol/K','+|-',10.1229),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 219,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.52427,-5.46942,-6.55603,-6.44691,-5.32321,-4.58735,-5.46254],'cal/mol/K','+|-',[3.91405,3.95867,3.99239,3.73681,3,3,6.07203]),
        H298 = (91.4974,'kcal/mol','+|-',9.2073),
        S298 = (2.00864,'cal/mol/K','+|-',10.0035),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 220,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {8,[S,D,T,B,Q]}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,S}
5   C   ux {4,[S,D,T,B,Q]}
6   O   u0 r0 {4,S} {7,[S,D,T,B,Q]}
7   O   ux r0 {6,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.0855,-6.68648,-7.60099,-6.85056,-4.96647,-3.84944,-2.62981],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.6968,'kcal/mol','+|-',5.2),
        S298 = (-1.73033,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 221,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->C_4C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux r1 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux {6,[S,D,T,B,Q]}
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
C=C([O])C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 222,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->C_N-4C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   O ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux {6,[S,D,T,B,Q]}
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
C=C([O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 223,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_N-5R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H u0 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.05771,-8.88893,-8.89813,-7.16722,-3.54578,-1.5732,0.236515],'cal/mol/K','+|-',[11.7792,14.5172,13.3153,10.843,5.00616,3,4.82461]),
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
    index = 224,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_N-5R!H->C_Ext-5O-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   ux r0 {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   R!H u0 r0 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux r0 {6,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.89312,-3.75631,-4.19044,-3.33364,-1.77583,-1.89202,-1.46924],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.9573,'kcal/mol','+|-',5.2),
        S298 = (-5.80781,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 225,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux {2,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.12063,-4.24036,-4.8151,-4.59406,-3.77708,-3.31889,-3.3402],'cal/mol/K','+|-',[3.1543,4.36565,4.439,3.92035,3,3,3]),
        H298 = (88.1997,'kcal/mol','+|-',5.2),
        S298 = (0.448261,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 226,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   C   ux r0 {2,[S,D,T,B,Q]} {5,S}
5   R!H ux r0 {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.833731,-3.30234,-4.30371,-4.4312,-4.33685,-4.22872,-4.3026],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.152,'kcal/mol','+|-',5.2),
        S298 = (1.90368,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 227,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D} {6,S}
4   C   u0 {2,S} {5,S}
5   O   u0 {4,S}
6   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.84846,-5.20857,-5.72354,-5.40423,-4.29984,-3.75833,-3.37486],'cal/mol/K','+|-',[4.34426,6.49387,6.68196,5.6792,3.00469,3,3]),
        H298 = (87.5566,'kcal/mol','+|-',5.2),
        S298 = (0.257916,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 228,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D} {6,S}
4   C u0 r0 {2,S} {5,S}
5   O u0 r0 {4,S}
6   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31253,-2.91264,-3.36111,-3.39633,-3.23752,-3.48418,-4.14387],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.2301,'kcal/mol','+|-',5.2),
        S298 = (-0.306429,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 229,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D} {4,S}
3   C                      u0 r0 {2,D} {6,S}
4   C                      u0 r0 {2,S} {5,S}
5   O                      u0 r0 {4,S}
6   [P,F,I,Br,Cl,O,Si,S,N] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.38439,-7.5045,-8.08597,-7.41213,-5.36216,-4.03249,-2.60585],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.883,'kcal/mol','+|-',5.2),
        S298 = (0.822261,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=CO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 230,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 {2,D}
4   C u0 {2,S} {5,D}
5   C u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.84506,-6.32164,-6.94561,-6.35905,-4.63019,-3.37986,-2.71694],'cal/mol/K','+|-',[4.53679,4.70884,4.63527,4.06957,3,3,3]),
        H298 = (93.1926,'kcal/mol','+|-',11.2496),
        S298 = (3.2952,'cal/mol/K','+|-',3.16335),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 231,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D} {6,[S,D,T,B,Q]}
4   C   u0 {2,S} {5,D}
5   C   u0 {4,D}
6   R!H ux {3,[S,D,T,B,Q]}
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
    index = 232,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_3C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux r1 {2,D}
4   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.31601,-11.302,-13.5755,-13.4851,-11.3531,-10.2008,-5.49906],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.2985,'kcal/mol','+|-',5.2),
        S298 = (9.60231,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC([O])=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 233,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_N-3C-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D}
4   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.60503,-6.60362,-6.72798,-6.1532,-4.95964,-4.17013,-3.54072],'cal/mol/K','+|-',[3.37528,3.64665,3.02054,3,3,3,3]),
        H298 = (84.5386,'kcal/mol','+|-',5.43301),
        S298 = (3.05485,'cal/mol/K','+|-',3.13565),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 234,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_N-3C-inRing_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D} {5,[S,D,T,B,Q]} {6,S}
4   C   u0 {2,S}
5   R!H ux {3,[S,D,T,B,Q]}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.57842,-7.60068,-7.54473,-6.83789,-5.45685,-4.55347,-3.62796],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.101,'kcal/mol','+|-',5.2),
        S298 = (3.72162,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 235,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_N-3C-inRing_Ext-3C-R_Ext-3C-R_5R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D} {5,[S,D,T,B,Q]} {6,S}
4   C u0 {2,S}
5   O ux {3,[S,D,T,B,Q]}
6   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.65354,-8.18562,-8.07355,-7.121,-5.20031,-4.03353,-2.68124],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.8644,'kcal/mol','+|-',5.2),
        S298 = (2.66129,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC([O])=C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 236,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_N-3C-inRing_Ext-3C-R_Ext-3C-R_N-5R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   C u0 r0 {2,D} {5,[S,D,T,B,Q]} {6,S}
4   C u0 {2,S}
5   C ux {3,[S,D,T,B,Q]}
6   C u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5033,-7.01573,-7.01592,-6.55477,-5.71338,-5.07342,-4.57467],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.3376,'kcal/mol','+|-',5.2),
        S298 = (4.78195,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 237,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.4807,-4.70566,-4.88635,-4.6662,-4.23187,-3.81614,-3.56319],'cal/mol/K','+|-',[3.55882,4.78886,5.10285,5.13547,5.32394,5.7255,4.50407]),
        H298 = (67.8534,'kcal/mol','+|-',6.97743),
        S298 = (1.96229,'cal/mol/K','+|-',11.3831),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 238,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   O   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.37166,-4.53999,-4.73809,-4.58244,-4.28288,-3.94512,-3.71983],'cal/mol/K','+|-',[3.64651,4.87208,5.24207,5.35795,5.58006,5.93536,4.58072]),
        H298 = (68.3657,'kcal/mol','+|-',5.50121),
        S298 = (1.98676,'cal/mol/K','+|-',11.9579),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 239,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.41844,-4.83462,-5.15406,-5.03754,-4.76549,-4.38758,-4.0368],'cal/mol/K','+|-',[4.08662,5.27634,5.52288,5.58916,5.80392,6.30271,4.90355]),
        H298 = (67.4347,'kcal/mol','+|-',5.31399),
        S298 = (2.6788,'cal/mol/K','+|-',12.9904),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 240,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-5C-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   O   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.08353,-4.00785,-3.85038,-3.27303,-2.50062,-1.89478,-2.22567],'cal/mol/K','+|-',[4.73517,6.18267,7.04355,7.05297,5.33125,4.02477,3]),
        H298 = (65.8906,'kcal/mol','+|-',5.2),
        S298 = (-2.86975,'cal/mol/K','+|-',11.9811),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 241,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   O   u0 {2,S} {5,S}
5   C   u0 {4,S} {6,[S,D,T,B,Q]}
6   C   u0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
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
    index = 242,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-5C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   O   u0 {2,S} {5,S}
5   C   u0 r0 {4,S} {6,S}
6   C   u0 r0 {5,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
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
    index = 243,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H-5C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   O   u0 {2,S} {5,S}
5   C   u0 r0 {4,S} {6,D}
6   C   u0 r0 {5,D} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
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
    index = 244,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   O   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,S} {8,[S,D,T,B,Q]}
6   C   ux {5,S} {7,S}
7   R!H ux {6,S}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.147065,0.414555,1.27653,1.87986,1.38353,0.974224,-0.797316],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (64.4186,'kcal/mol','+|-',5.2),
        S298 = (-9.2093,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 245,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {6,[S,D,T,B,Q]}
4   O   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.47126,-5.26362,-6.03521,-6.46212,-6.99613,-6.98472,-6.00166],'cal/mol/K','+|-',[4.75902,5.68549,4.14641,3,3,4.32463,4.6262]),
        H298 = (68.4194,'kcal/mol','+|-',6.24973),
        S298 = (7.48191,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 246,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-3C-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,S}
3   C   u0 r0 {2,D} {6,S}
4   O   u0 r0 {2,S} {5,S}
5   C   u0 r0 {4,S}
6   C   u0 r0 {3,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79233,-3.36499,-4.74151,-6.007,-7.86014,-8.57122,-7.60966],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (67.0348,'kcal/mol','+|-',2.4),
        S298 = (8.29768,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 247,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   O   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.12729,-8.75617,-8.74013,-7.88806,-6.33012,-5.01648,-3.33086],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (71.365,'kcal/mol','+|-',5.2),
        S298 = (6.65576,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 248,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_N-5R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D} {4,S}
3   C                      u0 {2,D}
4   O                      u0 {2,S} {5,S}
5   [P,F,I,Br,Cl,O,Si,S,N] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.17933,-3.32874,-3.02796,-2.71151,-2.29883,-2.12612,-2.41676],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (70.6849,'kcal/mol','+|-',2.4),
        S298 = (-0.858295,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 249,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.76648,-6.71689,-7.45812,-6.79427,-4.84684,-3.46223,-2.28578],'cal/mol/K','+|-',[4.08806,4.54646,4.37421,4.14526,4.07184,3.71862,4.05752]),
        H298 = (88.4686,'kcal/mol','+|-',7.46475),
        S298 = (-0.52762,'cal/mol/K','+|-',8.16368),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 250,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.57767,-6.80806,-7.74909,-7.26501,-5.53327,-4.11107,-2.78681],'cal/mol/K','+|-',[4.34245,4.95228,4.48507,3.62963,3,3,3.36472]),
        H298 = (87.5822,'kcal/mol','+|-',6.36142),
        S298 = (0.711431,'cal/mol/K','+|-',5.32829),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 251,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.32386,-6.56557,-7.54709,-7.08672,-5.41493,-4.06627,-2.89935],'cal/mol/K','+|-',[4.65172,5.37515,4.89088,3.9388,3,3,3.71103]),
        H298 = (88.0333,'kcal/mol','+|-',6.66925),
        S298 = (0.754234,'cal/mol/K','+|-',5.95259),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 252,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,S}
6   C   ux {5,[S,D,T,B,Q]}
7   R!H ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.76923,-6.22353,-7.36832,-7.02831,-5.55663,-4.36555,-3.64478],'cal/mol/K','+|-',[4.54403,5.95006,5.57154,4.53812,3,3,3]),
        H298 = (89.3779,'kcal/mol','+|-',5.2),
        S298 = (1.09571,'cal/mol/K','+|-',6.64341),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 253,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H_7R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,S}
6   C   ux {5,[S,D,T,B,Q]}
7   O   ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.24913,-7.02923,-8.14954,-7.6304,-5.79882,-4.32926,-3.31106],'cal/mol/K','+|-',[5.0443,6.12578,5.64941,4.71076,3,3,3]),
        H298 = (89.9687,'kcal/mol','+|-',5.2),
        S298 = (1.0589,'cal/mol/K','+|-',8.13449),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 254,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H_7R!H->O_Ext-7O-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H u0 {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,S}
6   C   u0 r0 {5,[S,D,T,B,Q]}
7   O   u0 r0 {5,S} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09109,-6.64922,-8.34041,-7.9654,-6.16742,-4.76381,-2.56382],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.4358,'kcal/mol','+|-',5.2),
        S298 = (-0.993076,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 255,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H_7R!H->O_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,S}
6   C ux {5,[S,D,T,B,Q]}
7   O ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.51397,-4.17408,-5.23424,-5.12546,-4.32026,-3.43748,-4.17683],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.5624,'kcal/mol','+|-',5.2),
        S298 = (-1.5736,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=C[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 256,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H_7R!H->O_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,S}
6   C ux {5,[S,D,T,B,Q]}
7   O ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.14234,-10.2644,-10.874,-9.80035,-6.90878,-4.78648,-3.19253],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.9079,'kcal/mol','+|-',5.2),
        S298 = (5.74337,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=C(O)C(O)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 257,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H_N-7R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {4,S} {5,S}
4   R!H ux r0 {3,S}
5   C   u0 r0 {3,S} {6,[S,D,T,B,Q]} {7,S}
6   C   ux {5,[S,D,T,B,Q]}
7   C   ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32952,-3.80643,-5.02466,-5.22202,-4.83007,-4.47443,-4.64595],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.6055,'kcal/mol','+|-',5.2),
        S298 = (1.20616,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=C[O])C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 258,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_N-Sp-7R!H-5R!H",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H u0 {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[B,D,T,Q]}
6   C   u0 r0 {5,[S,D,T,B,Q]}
7   R!H u0 r0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5424,-7.93374,-8.26219,-7.32036,-4.84811,-2.86917,0.0823629],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.6551,'kcal/mol','+|-',5.2),
        S298 = (-0.611679,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 259,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,S}
2   C                      u0 r0 {1,S} {3,D}
3   C                      u0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H                    u0 {3,[S,D,T,B,Q]}
5   C                      ux {3,[S,D,T,B,Q]} {6,S}
6   [P,F,I,Br,Cl,O,Si,S,N] u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.89933,-6.16985,-5.71233,-3.96984,-0.728227,0.430804,0.720431],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.787,'kcal/mol','+|-',5.2),
        S298 = (-7.96192,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 260,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_4R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 {2,D} {4,[S,D,T,B,Q]}
4   R!H u0 r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.9045,-7.39622,-9.90787,-9.85255,-7.76493,-6.71476,-8.81574],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.4445,'kcal/mol','+|-',5.2),
        S298 = (7.42729,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=CC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 261,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   R!H ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.47544,-2.88311,-3.47822,-3.76752,-4.02883,-4.08014,-3.99957],'cal/mol/K','+|-',[4.86511,4.4269,3.68081,3,3,3,3]),
        H298 = (82.8637,'kcal/mol','+|-',5.2),
        S298 = (4.61102,'cal/mol/K','+|-',12.346),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 262,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,[S,D,T,B,Q]}
4   C ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.48654,-2.78167,-3.36484,-3.70065,-4.07809,-4.22735,-4.17167],'cal/mol/K','+|-',[5.09254,4.55904,3.73923,3,3,3,3]),
        H298 = (82.5363,'kcal/mol','+|-',5.2),
        S298 = (3.11071,'cal/mol/K','+|-',3.88865),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 263,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,S}
4   C ux r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.733555,-2.13286,-2.90372,-3.41894,-4.01065,-4.25141,-4.20293],'cal/mol/K','+|-',[6.57809,5.74288,4.5521,3.3328,3,3,3]),
        H298 = (81.6364,'kcal/mol','+|-',5.2),
        S298 = (3.41892,'cal/mol/K','+|-',4.03721),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 264,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,S}
4   C ux r0 {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0349842,-1.64299,-2.70499,-3.43586,-4.27255,-4.60107,-4.42975],'cal/mol/K','+|-',[7.58798,6.96173,5.73375,4.2518,3,3,3]),
        H298 = (82.1281,'kcal/mol','+|-',5.2),
        S298 = (3.96082,'cal/mol/K','+|-',4.48739),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 265,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,S}
4   C   ux r0 {3,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,S}
6   R!H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.0823,-0.441455,-2.22506,-3.46518,-4.87583,-5.4046,-4.93075],'cal/mol/K','+|-',[6.95706,9.41178,8.79074,6.73649,3,3,3.57649]),
        H298 = (83.0414,'kcal/mol','+|-',5.2),
        S298 = (5.05569,'cal/mol/K','+|-',4.80197),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 266,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Sp-5R!H-4C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {4,S}
4   C   ux r0 {3,S} {5,S}
5   C   ux {4,S} {6,S}
6   R!H u0 r0 {5,S}
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
[O]C=CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 267,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_N-Sp-5R!H-4C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {4,S}
4   C   ux r0 {3,S} {5,D}
5   C   ux {4,D} {6,S}
6   R!H u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32343,-5.04885,-6.52844,-6.76293,-5.94651,-5.33188,-3.17993],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.6523,'kcal/mol','+|-',5.2),
        S298 = (7.40642,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=CC=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 268,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,D}
4   C ux r0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.54756,-3.6959,-4.0146,-4.09759,-4.1731,-4.19344,-4.12763],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.8427,'kcal/mol','+|-',5.2),
        S298 = (2.67643,'cal/mol/K','+|-',4.48107),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 269,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C_Ext-4C-R_Sp-5R!H-4C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D} {4,D}
4   C ux r0 {3,D} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.40511,-3.31615,-3.53199,-3.62224,-3.87322,-4.01629,-3.97098],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (84.2542,'kcal/mol','+|-',2.67862),
        S298 = (1.83867,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 270,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C_Ext-4C-R_Sp-5R!H-4C_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {4,D}
4   C   ux r0 {3,D} {5,S}
5   C   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.18861,-3.23185,-3.42968,-3.46495,-3.82033,-4.08149,-4.04745],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (85.2012,'kcal/mol','+|-',2.4),
        S298 = (1.9763,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 271,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C_Ext-4C-R_N-Sp-5R!H-4C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 {2,D} {4,D}
4   C u0 r0 {3,D} {5,[B,D,T,Q]}
5   C u0 r0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.18861,-5.40477,-6.18637,-6.23664,-5.52259,-4.99065,-4.83253],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.979,'kcal/mol','+|-',5.2),
        S298 = (6.44635,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 272,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32842,-4.22716,-4.98042,-4.65365,-3.37613,-2.12961,-1.71919],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.2046,'kcal/mol','+|-',5.2),
        S298 = (24.4901,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 273,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.53871,-3.0922,-3.35001,-3.57473,-4.04384,-4.38986,-4.85386],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.421,'kcal/mol','+|-',5.2),
        S298 = (1.07311,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 274,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,S}
3   O   ux {2,D}
4   R!H u0 {2,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,S}
6   C   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09253,-2.43509,-2.75768,-3.04738,-3.53647,-3.96034,-4.711],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.306,'kcal/mol','+|-',5.2),
        S298 = (0.382487,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 275,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,S}
3   O   ux {2,D}
4   C   u0 r0 {2,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,S}
6   C   u0 r0 {5,S}
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
C=CCCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 276,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {4,S}
3   O   ux {2,D}
4   O   u0 r0 {2,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,S}
6   C   u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.91386,-2.14535,-2.38175,-2.61981,-3.0875,-3.5211,-4.26794],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (110.41,'kcal/mol','+|-',2.4),
        S298 = (1.02503,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
COOC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 277,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0478,-1.7353,-2.4328,-2.73917,-3.02269,-3.35715,-4.13102],'cal/mol/K','+|-',[5.08078,5.35557,5.63994,5.60134,4.95063,4.32715,3.64582]),
        H298 = (106.768,'kcal/mol','+|-',16.5811),
        S298 = (-1.14078,'cal/mol/K','+|-',9.24576),
    ),
    shortDesc = """Radical correction fitted to 57 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 278,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 {1,S} {3,S} {4,[S,D,T,B,Q]}
3   [C,O] u0 {2,S} {4,[S,D,T,B,Q]}
4   [C,O] u0 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79998,-1.3025,-1.62796,-1.76416,-2.10899,-2.65152,-3.26679],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (51.042,'kcal/mol','+|-',9.16988),
        S298 = (-1.69887,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 279,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C_Ext-4R!H-R_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   O   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]} {5,S}
5   O   u0 {4,S}
6   R!H ux {2,[S,D,T,B,Q]}
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
[O]C12OC1(O)O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 280,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72193,-3.00544,-4.65499,-5.31951,-5.45476,-5.62078,-7.02479],'cal/mol/K','+|-',[10.6741,9.83981,8.95059,8.17214,6.79028,6.03557,4.5648]),
        H298 = (109.495,'kcal/mol','+|-',16.5303),
        S298 = (0.765167,'cal/mol/K','+|-',10.5473),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 281,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   O   ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.813451,-1.39948,-2.90348,-3.71877,-4.71421,-5.62674,-5.88439],'cal/mol/K','+|-',[14.7223,12.8415,11.2495,10.2315,9.18638,8.45667,3.88305]),
        H298 = (112.499,'kcal/mol','+|-',21.0018),
        S298 = (-2.20177,'cal/mol/K','+|-',10.7729),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 282,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D} {6,[S,D,T,B,Q]}
5   O   ux {4,D}
6   R!H ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8635,-2.44179,-3.9717,-4.74355,-5.71686,-6.68171,-5.83143],'cal/mol/K','+|-',[18.4886,16.0403,13.8802,12.5545,11.1347,10.0532,4.83024]),
        H298 = (116.992,'kcal/mol','+|-',19.4866),
        S298 = (-1.97296,'cal/mol/K','+|-',13.7476),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 283,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D} {6,[S,D,T,B,Q]}
5   O   ux {4,D}
6   R!H ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.71817,1.54139,-0.554823,-1.66459,-3.03434,-4.24994,-6.59884],'cal/mol/K','+|-',[3,3,3,3,3.6426,3.1104,4.56757]),
        H298 = (120.567,'kcal/mol','+|-',16.2118),
        S298 = (-4.92183,'cal/mol/K','+|-',8.6483),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 284,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_7R!H->O_3R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   u0 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   O   ux {4,D}
6   R!H ux {4,[S,D,T,B,Q]} {7,S}
7   O   u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.85593,1.61609,-0.0883148,-0.996066,-2.04927,-3.36378,-6.14673],'cal/mol/K','+|-',[3,3.1916,3.51486,3,3,3,6.06793]),
        H298 = (115.899,'kcal/mol','+|-',5.2),
        S298 = (-7.31317,'cal/mol/K','+|-',3.51309),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 285,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_7R!H->O_3R!H->C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {8,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   u0 r1 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   O   ux r0 {4,D}
6   R!H ux r1 {4,[S,D,T,B,Q]} {7,S}
7   O   u0 {6,S}
8   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.92424,2.74449,1.15438,-0.0555673,-1.41202,-3.11312,-8.29207],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (116.467,'kcal/mol','+|-',5.2),
        S298 = (-8.55524,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1CC(=O)C(OO)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 286,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_7R!H->O_N-3R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,D} {6,S}
5   O   u0 {4,D}
6   R!H u0 r1 {4,S} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.44264,1.392,-1.48784,-3.00163,-5.00446,-6.02225,-7.50305],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (129.904,'kcal/mol','+|-',5.2),
        S298 = (-0.139146,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1(O)OOC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 287,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * O                      u1 r0 {2,[S,D,T,B,Q]}
2   C                      ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux r1 {2,[S,T,Q,B]} {4,S}
4   C                      u0 r1 {3,S} {5,D} {6,[S,D,T,B,Q]}
5   O                      ux r0 {4,D}
6   R!H                    ux r1 {4,[S,D,T,B,Q]} {7,S}
7   [P,F,I,Br,Cl,C,Si,S,N] u0 r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.6085,-14.3913,-14.2223,-13.9804,-13.7644,-13.977,-3.52919],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (106.267,'kcal/mol','+|-',5.2),
        S298 = (6.87366,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1CC(=O)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 288,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.470473,0.434255,-0.751139,-1.52422,-2.24095,-3.17108,-6.80137],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107,'kcal/mol','+|-',5.2),
        S298 = (-3.82029,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 289,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_N-3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.10281,0.935985,-0.782946,-1.81422,-3.1769,-3.86251,-5.1793],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.027,'kcal/mol','+|-',5.2),
        S298 = (-1.49849,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1(O)OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 290,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   R!H u0 {3,S} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.81211,-4.93259,-6.7568,-7.2404,-6.34341,-5.61363,-8.39326],'cal/mol/K','+|-',[3,3,3,3,3,3,4.00991]),
        H298 = (105.89,'kcal/mol','+|-',5.2),
        S298 = (4.32549,'cal/mol/K','+|-',4.10468),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 291,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   R!H u0 {3,S} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H u0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.79386,-5.00144,-6.84787,-7.29424,-6.39695,-5.69153,-8.32725],'cal/mol/K','+|-',[3,3,3,3,3,3,4.61768]),
        H298 = (106.476,'kcal/mol','+|-',5.2),
        S298 = (3.60481,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 292,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   C   u0 {3,S} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H u0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.27684,-5.15593,-7.00767,-7.56036,-6.58283,-5.89842,-8.58412],'cal/mol/K','+|-',[3,3,3,3,3,3,5.5137]),
        H298 = (105.927,'kcal/mol','+|-',5.2),
        S298 = (4.26908,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 293,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_4R!H->C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {8,S}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   C   u0 {3,S} {5,[S,T,Q,B]}
5   C   ux {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H u0 {6,[S,D,T,B,Q]}
8   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.44468,-5.64835,-7.44044,-8.03611,-7.16705,-6.30423,-7.6103],'cal/mol/K','+|-',[3,3,3,3,3,3,6.16783]),
        H298 = (105.326,'kcal/mol','+|-',5.2),
        S298 = (3.9845,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 294,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_4R!H->C_Ext-2C-R_3R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {8,S}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   u0 r1 {3,S} {5,[S,T,Q,B]}
5   C   ux r1 {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H u0 {6,[S,D,T,B,Q]}
8   C   u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.58076,-5.50087,-7.39857,-8.12501,-7.27709,-6.46622,-9.79096],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.278,'kcal/mol','+|-',5.2),
        S298 = (3.40135,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1([O])CCCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 295,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_4R!H->C_Ext-2C-R_N-3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {8,S}
3   O ux r1 {2,[S,T,Q,B]} {4,S}
4   C u0 r1 {3,S} {5,[S,T,Q,B]}
5   C ux r1 {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C u0 {6,[S,D,T,B,Q]}
8   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.30861,-5.79583,-7.48231,-7.94722,-7.05701,-6.14225,-5.42964],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.373,'kcal/mol','+|-',5.2),
        S298 = (4.56765,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CCOC1(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 296,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O   ux r1 {2,[S,T,Q,B]} {4,S}
4   O   u0 r1 {3,S} {5,[S,T,Q,B]}
5   R!H ux r1 {4,[S,T,Q,B]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,S}
7   C   u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34493,-4.53796,-6.36845,-6.49588,-5.83932,-5.07085,-7.55663],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.122,'kcal/mol','+|-',5.2),
        S298 = (1.61203,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C1CC(C)([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 297,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.908425,-1.53052,-2.07601,-2.32615,-2.63323,-2.99014,-3.66066],'cal/mol/K','+|-',[3.5305,4.22134,4.63786,4.65766,4.1637,3.54276,3]),
        H298 = (107.558,'kcal/mol','+|-',5.27534),
        S298 = (-1.45093,'cal/mol/K','+|-',9.08876),
    ),
    shortDesc = """Radical correction fitted to 44 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 298,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.803521,-1.28388,-1.7504,-1.97576,-2.31902,-2.74661,-3.54704],'cal/mol/K','+|-',[3.44931,4.0479,4.32849,4.27591,3.84324,3.3075,3]),
        H298 = (107.734,'kcal/mol','+|-',5.65436),
        S298 = (-1.87966,'cal/mol/K','+|-',9.18304),
    ),
    shortDesc = """Radical correction fitted to 38 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 299,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.868501,-1.40542,-1.90723,-2.16179,-2.5172,-2.91873,-3.62211],'cal/mol/K','+|-',[3.53144,4.19383,4.4415,4.31322,3.80316,3.29,3]),
        H298 = (108.091,'kcal/mol','+|-',5.87296),
        S298 = (-1.3488,'cal/mol/K','+|-',9.94551),
    ),
    shortDesc = """Radical correction fitted to 27 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 300,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.564923,-1.11781,-1.70329,-1.97979,-2.25029,-2.68488,-3.45631],'cal/mol/K','+|-',[3.78999,4.30844,4.92576,5.06405,4.85088,4.45331,3.56352]),
        H298 = (109.379,'kcal/mol','+|-',8.84703),
        S298 = (-4.3727,'cal/mol/K','+|-',8.15183),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 301,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   R!H u0 {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S} {6,[S,D,T,B,Q]}
6   R!H u0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.225109,-0.989541,-1.92537,-2.40594,-2.76013,-3.31487,-4.6903],'cal/mol/K','+|-',[4.50678,4.39256,4.89925,5.057,4.4641,3.92331,3.24159]),
        H298 = (107.476,'kcal/mol','+|-',5.2),
        S298 = (-3.72352,'cal/mol/K','+|-',7.71475),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 302,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_6R!H-inRing",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 r0 {1,S} {3,S}
3   C     u0 {2,S} {4,[S,D,T,B,Q]}
4   [C,O] u0 {3,[S,D,T,B,Q]} {5,S}
5   [C,O] ux {4,S} {6,[S,D,T,B,Q]}
6   C     u0 r1 {5,[S,D,T,B,Q]} {7,S}
7   [C,O] ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.262176,-1.6672,-3.40724,-4.26019,-4.94591,-5.56832,-5.04344],'cal/mol/K','+|-',[3,3,3,3.60813,3.20024,3,3]),
        H298 = (109.663,'kcal/mol','+|-',5.2),
        S298 = (-1.94388,'cal/mol/K','+|-',6.95589),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 303,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_6R!H-inRing_Ext-3C-R",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 r0 {1,S} {3,S}
3   C     u0 r1 {2,S} {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   [C,O] u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   [C,O] ux r1 {4,S} {6,[S,D,T,B,Q]}
6   C     u0 r1 {5,[S,D,T,B,Q]} {7,S}
7   [C,O] ux r1 {6,S}
8   R!H   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.273125,-2.07196,-4.1565,-5.53586,-6.07736,-6.42326,-5.3411],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.865,'kcal/mol','+|-',5.2),
        S298 = (0.515398,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 304,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S} {6,[S,D,T,B,Q]}
6   R!H u0 r0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.468752,-0.650709,-1.18443,-1.47882,-1.66725,-2.18815,-4.51372],'cal/mol/K','+|-',[5.66902,5.46661,5.45193,4.95274,3.26947,3,4.0961]),
        H298 = (106.382,'kcal/mol','+|-',5.2),
        S298 = (-4.61334,'cal/mol/K','+|-',8.3904),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 305,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H-inRing_3C-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S} {6,[S,D,T,B,Q]}
6   R!H u0 r0 {5,[S,D,T,B,Q]} {7,S}
7   C   ux r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24842,-1.74679,-3.09912,-3.46218,-2.92185,-3.09424,-7.56949],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.82,'kcal/mol','+|-',5.2),
        S298 = (0.329631,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1OC1(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 306,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H-inRing_N-3C-inRing",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S} {6,[S,D,T,B,Q]}
6   R!H u0 r0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.208863,-0.285348,-0.5462,-0.817704,-1.24905,-1.88612,-3.49513],'cal/mol/K','+|-',[6.82537,6.45151,5.89994,5.1288,3.44046,3,3]),
        H298 = (105.57,'kcal/mol','+|-',5.2),
        S298 = (-6.261,'cal/mol/K','+|-',6.35954),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 307,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H-inRing_N-3C-inRing_Ext-3C-R",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 r0 {1,S} {3,S}
3   C     u0 r0 {2,S} {4,[S,D,T,B,Q]} {8,S}
4   C     u0 {3,[S,D,T,B,Q]} {5,S}
5   O     ux {4,S} {6,[S,D,T,B,Q]}
6   C     u0 r0 {5,[S,D,T,B,Q]} {7,[S,D]}
7   [C,O] ux {6,[S,D]}
8   C     u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.56982,1.28304,0.842361,0.372037,-0.474819,-1.50431,-3.62583],'cal/mol/K','+|-',[4.15239,4.92014,4.83156,4.31712,3.0475,3,3]),
        H298 = (105.605,'kcal/mol','+|-',5.2),
        S298 = (-7.15452,'cal/mol/K','+|-',7.85661),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 308,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-8R!H-R",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 r0 {1,S} {3,S}
3   C     u0 r0 {2,S} {4,[S,D,T,B,Q]} {8,S}
4   C     u0 {3,[S,D,T,B,Q]} {5,S}
5   O     ux {4,S} {6,[S,D,T,B,Q]}
6   C     u0 r0 {5,[S,D,T,B,Q]} {7,[S,D]}
7   [C,O] ux r0 {6,[S,D]}
8   C     u0 r0 {3,S} {9,[S,D,T,B,Q]}
9   R!H   ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.03791,3.02257,2.55058,1.89837,0.602634,-0.968015,-3.50179],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.822,'kcal/mol','+|-',5.2),
        S298 = (-9.93225,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC(C[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 309,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.647678,-1.106,-1.54609,-1.72163,-1.95361,-2.32345,-2.67874],'cal/mol/K','+|-',[3.64378,4.75827,5.53738,5.62972,5.55553,5.10305,3.1695]),
        H298 = (109.082,'kcal/mol','+|-',5.76176),
        S298 = (-4.44437,'cal/mol/K','+|-',9.05991),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 310,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0979816,-0.698436,-1.14719,-1.18876,-1.26125,-1.56928,-1.79241],'cal/mol/K','+|-',[4.11269,3.47774,3,3,3,3,3]),
        H298 = (110.541,'kcal/mol','+|-',7.23536),
        S298 = (-6.24453,'cal/mol/K','+|-',3.57129),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 311,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {7,D}
4   R!H u0 {3,S} {5,S}
5   C   u0 {4,S} {6,[S,D,T,B,Q]} {8,S}
6   O   u0 {5,[S,D,T,B,Q]}
7   C   ux {3,D}
8   C   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.904111,-0.229292,-0.895403,-1.05481,-1.4335,-1.95528,-2.28315],'cal/mol/K','+|-',[4.59618,5.31177,4.86339,3.69187,3,3,3]),
        H298 = (108.772,'kcal/mol','+|-',12.0955),
        S298 = (-4.62695,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 312,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_Ext-5R!H-R_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {9,[S,D,T,B,Q]}
3   C   u0 {2,S} {4,S} {7,D}
4   R!H u0 {3,S} {5,S}
5   C   u0 {4,S} {6,[S,D,T,B,Q]} {8,S}
6   O   u0 {5,[S,D,T,B,Q]}
7   C   ux {3,D}
8   C   u0 r0 {5,S}
9   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.720883,-2.10728,-2.61487,-2.36009,-2.32508,-2.36649,-2.64653],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (113.049,'kcal/mol','+|-',5.2),
        S298 = (-3.97808,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(OC(C)=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 313,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,D} {7,[S,D,T,B,Q]}
4   C u0 {3,D} {5,S}
5   C u0 {4,S} {6,D}
6   O u0 {5,D}
7   C u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39455,-1.54385,-1.6155,-1.54783,-1.56701,-1.5984,-1.68933],'cal/mol/K','+|-',[4.86439,3.228,3,3,3,3,3]),
        H298 = (110.809,'kcal/mol','+|-',5.2),
        S298 = (-6.59948,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 314,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,D} {7,[S,D,T,B,Q]}
4   C   u0 r0 {3,D} {5,S} {8,[S,D,T,B,Q]}
5   C   u0 r0 {4,S} {6,D}
6   O   u0 r0 {5,D}
7   C   u0 r0 {3,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.11437,-2.68512,-2.35242,-2.11685,-1.94821,-1.84544,-1.65904],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.374,'kcal/mol','+|-',5.2),
        S298 = (-6.44153,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C=O)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 315,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_N-4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,S}
4   O   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
7   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.490967,0.054105,-0.714148,-0.738521,-0.305225,-0.739077,-1.01707],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (113.541,'kcal/mol','+|-',5.2),
        S298 = (-8.76981,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CC(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 316,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-4R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   R!H ux {3,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.425143,3.28553,4.13591,3.92051,3.20413,2.11424,-1.13897],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (106.079,'kcal/mol','+|-',5.2),
        S298 = (-11.2044,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CCC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 317,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_3C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   R!H ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26193,-3.16419,-4.42396,-5.01004,-5.54206,-5.82839,-4.94019],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (108.542,'kcal/mol','+|-',2.4),
        S298 = (1.68441,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CC1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 318,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_N-3C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S}
4   R!H ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.08691,-2.9044,-2.74735,-2.62919,-2.49917,-2.64584,-3.56192],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.329,'kcal/mol','+|-',5.2),
        S298 = (-2.47324,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 319,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83833,-1.99672,-1.825,-1.8108,-1.93544,-2.24821,-3.24488],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (123.152,'kcal/mol','+|-',5),
        S298 = (-7.60486,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
COC(=O)CC[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
""",
)

entry(
    index = 320,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01996,-1.5867,-1.96799,-2.16884,-2.60691,-2.98637,-3.71555],'cal/mol/K','+|-',[3.62682,4.07498,3.77564,3.3271,3,3,3]),
        H298 = (107.605,'kcal/mol','+|-',5.2),
        S298 = (1.86264,'cal/mol/K','+|-',9.80801),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 321,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_6R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.89003,-2.67095,-2.95281,-2.97142,-3.06275,-3.15969,-3.75297],'cal/mol/K','+|-',[3,3,3.11455,3.40361,3,3,3]),
        H298 = (108.906,'kcal/mol','+|-',5.2),
        S298 = (-0.078011,'cal/mol/K','+|-',3.29392),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 322,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_6R!H->O_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   R!H ux {3,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   O   ux {3,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7072,-4.28755,-5.56073,-5.78976,-5.21814,-4.49473,-5.83613],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (113.471,'kcal/mol','+|-',5.2),
        S298 = (2.33681,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CC1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 323,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_6R!H->O_3C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
6   O   ux r0 {3,[S,D,T,B,Q]}
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
[O]CC1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 324,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_6R!H->O_N-3C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]} {5,S}
5   O ux {4,S}
6   O ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.55434,-2.55899,-2.2099,-2.06131,-2.40319,-2.83459,-3.31093],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.304,'kcal/mol','+|-',2.4),
        S298 = (0.101024,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 325,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.473062,-0.905164,-1.34896,-1.66436,-2.32038,-2.87743,-3.69204],'cal/mol/K','+|-',[4.3265,4.66445,3.95861,3.26613,3,3,3]),
        H298 = (106.765,'kcal/mol','+|-',5.2),
        S298 = (3.08247,'cal/mol/K','+|-',12.1821),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 326,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_Sp-4R!H-3C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]}
4   R!H ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0310328,-0.430178,-0.927464,-1.29605,-2.05859,-2.70233,-3.5928],'cal/mol/K','+|-',[3.6159,3.90751,3.20484,3,3,3,3]),
        H298 = (106.581,'kcal/mol','+|-',5.2),
        S298 = (3.7432,'cal/mol/K','+|-',12.5284),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 327,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_Sp-4R!H-3C_Ext-4R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   R!H u0 {3,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   C   u0 {3,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.75783,0.422212,-0.934123,-1.16077,-1.33497,-1.21065,-1.10689],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.559,'kcal/mol','+|-',5.2),
        S298 = (15.5389,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=CC([O])C(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 328,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_Sp-4R!H-3C_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   C u0 {3,S} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]}
6   C u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.14296,-1.72438,-1.94096,-2.12132,-2.70645,-3.30484,-4.09747],'cal/mol/K','+|-',[2.30299,2.04893,2,2,2,2,2]),
        H298 = (106.348,'kcal/mol','+|-',2.76587),
        S298 = (0.104295,'cal/mol/K','+|-',5.00755),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 329,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_Sp-4R!H-3C_4R!H->C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {7,[S,D,T,B,Q]}
3   C   u0 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   C   u0 r0 {3,S} {5,[S,D,T,B,Q]}
5   O   u0 r0 {4,[S,D,T,B,Q]}
6   C   u0 r0 {3,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.95718,-2.44878,-2.31894,-2.28706,-3.0207,-3.72295,-4.10253],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (107.326,'kcal/mol','+|-',2.4),
        S298 = (1.87473,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C=O)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 330,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_Sp-4R!H-3C_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]}
4   O ux {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
6   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.953317,1.77938,1.10248,0.294361,-1.08447,-2.16026,-3.68831],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (105.987,'kcal/mol','+|-',2.4),
        S298 = (5.77849,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 331,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_N-Sp-4R!H-3C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,D} {6,[S,D,T,B,Q]}
4   R!H ux r0 {3,D} {5,[S,D,T,B,Q]}
5   R!H ux r0 {4,[S,D,T,B,Q]}
6   C   ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.89879,-4.5863,-4.61552,-4.51877,-4.34921,-4.23443,-4.46113],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (109.534,'kcal/mol','+|-',5.2),
        S298 = (-2.03814,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 332,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.566305,-0.361176,-0.730773,-1.13737,-1.81695,-2.49521,-3.64833],'cal/mol/K','+|-',[3.13234,3,3,3,3,3,3]),
        H298 = (106.961,'kcal/mol','+|-',5.2),
        S298 = (-2.50823,'cal/mol/K','+|-',4.03496),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 333,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,S}
5   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4427,0.762408,-0.481296,-0.91336,-1.21419,-1.97555,-3.22889],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (106.554,'kcal/mol','+|-',5.2),
        S298 = (-4.81266,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCCC([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 334,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01275,-0.610861,-0.786212,-1.18716,-1.9509,-2.61069,-3.74154],'cal/mol/K','+|-',[2.52854,2.44993,2,2,2,2,2]),
        H298 = (107.004,'kcal/mol','+|-',2.4),
        S298 = (-1.99613,'cal/mol/K','+|-',3.69091),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 335,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-4R!H->C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S}
4   O   ux r0 {3,S} {5,S}
5   R!H ux r0 {4,S}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.118777,0.255321,-0.205822,-0.680493,-1.57159,-2.35621,-3.71914],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (106.255,'kcal/mol','+|-',2.4),
        S298 = (-3.30106,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 336,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,S}
4   R!H ux r0 {3,S} {5,D}
5   R!H ux r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.84046,-4.88716,-5.87111,-5.93572,-5.58846,-5.21453,-4.16357],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (108.176,'kcal/mol','+|-',2.4),
        S298 = (2.98547,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 337,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0699372,-0.859082,-1.63522,-1.93879,-2.28166,-2.72709,-3.56729],'cal/mol/K','+|-',[3,3,3.05484,3.24779,3.37867,3.00257,3]),
        H298 = (108.44,'kcal/mol','+|-',5.2),
        S298 = (-3.35967,'cal/mol/K','+|-',6.93115),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 338,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {5,D}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.253356,-0.760961,-1.62084,-1.94241,-2.38532,-2.85046,-3.51568],'cal/mol/K','+|-',[3,3.13812,3.20951,3.43044,3.67716,3.30473,3]),
        H298 = (109.122,'kcal/mol','+|-',5.2),
        S298 = (-3.08226,'cal/mol/K','+|-',8.14812),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 339,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {5,D}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0197067,-1.25994,-2.10352,-2.44915,-2.93621,-3.28117,-3.85606],'cal/mol/K','+|-',[3,3.16042,3.32382,3.60009,3.85885,3.64982,3]),
        H298 = (108.962,'kcal/mol','+|-',5.2),
        S298 = (-2.18327,'cal/mol/K','+|-',9.39014),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 340,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_4R!H->C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {4,S}
3   C   u0 {2,S} {5,D} {6,S}
4   C   u0 {2,S}
5   R!H ux {3,D}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.26544,0.34817,-0.395011,-0.655877,-1.08046,-1.58037,-3.00109],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.602,'kcal/mol','+|-',5.2),
        S298 = (-6.26658,'cal/mol/K','+|-',5.27948),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 341,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_4R!H->C_Ext-3C-R_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {4,S} {7,[S,D,T,B,Q]}
3   C   u0 {2,S} {5,D} {6,S}
4   C   u0 r0 {2,S}
5   R!H ux {3,D}
6   C   u0 r0 {3,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.68908,0.501097,-0.445348,-1.07936,-1.7444,-2.32211,-3.73475],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.876,'kcal/mol','+|-',5.2),
        S298 = (-4.4,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C(C)([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 342,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_4R!H->C_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {5,D}
4   C ux {2,[S,D,T,B,Q]}
5   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.243844,-1.47202,-2.40008,-2.60892,-2.95595,-3.17383,-3.4576],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.669,'kcal/mol','+|-',5.2),
        S298 = (-3.48705,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 343,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_4R!H->C_N-5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux {2,[S,T,Q,B]} {5,D}
4   C ux {2,[S,D,T,B,Q]}
5   O ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.970476,-2.59511,-3.49039,-3.97216,-4.577,-4.8407,-4.79313],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.179,'kcal/mol','+|-',2.4),
        S298 = (2.0258,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 344,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_N-4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {5,D}
4   O   ux {2,[S,D,T,B,Q]}
5   R!H u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.866687,0.54886,-0.353792,-0.612226,-0.93921,-1.71986,-2.62217],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (109.737,'kcal/mol','+|-',5.2),
        S298 = (-5.44211,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 345,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_N-4R!H->C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,T,Q,B]} {5,D} {6,[S,D,T,B,Q]}
4   O   ux {2,[S,D,T,B,Q]}
5   R!H u0 r0 {3,D}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.38925,1.0065,0.0954418,-0.209571,-0.612713,-1.49061,-2.58121],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (109.482,'kcal/mol','+|-',5.2),
        S298 = (-5.5857,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 346,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_N-Sp-5R!H=3C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {5,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.85123,-1.09621,-1.66998,-1.93003,-2.03116,-2.42895,-3.69203],'cal/mol/K','+|-',[3,3,3.41727,3.58402,3.32652,3,3]),
        H298 = (106.237,'kcal/mol','+|-',5.2),
        S298 = (-4.03008,'cal/mol/K','+|-',4.14589),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 347,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_N-Sp-5R!H=3C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   C   u0 {2,S} {5,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,T,Q,B]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42657,-2.60704,-3.47333,-3.89446,-3.91905,-3.99539,-4.93772],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.53,'kcal/mol','+|-',5.2),
        S298 = (-1.7705,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 348,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {5,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,T,Q,B]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.561205,-0.758197,-1.46141,-1.51091,-1.39274,-1.93466,-3.02646],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (106.648,'kcal/mol','+|-',5.2),
        S298 = (-4.47588,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 349,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.86499,-3.74142,-3.38619,-3.03964,-2.75925,-2.89437,-3.31001],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (105.342,'kcal/mol','+|-',2.4),
        S298 = (-0.38812,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 350,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.41387,-2.71885,-3.64487,-4.01434,-4.14712,-4.16353,-4.2081],'cal/mol/K','+|-',[4.1123,4.64232,5.24413,5.39132,4.71495,4.04454,3]),
        H298 = (106.857,'kcal/mol','+|-',5.2),
        S298 = (0.614766,'cal/mol/K','+|-',8.09302),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 351,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   O   u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H ux {4,S} {6,S}
6   O   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.321648,-2.60549,-4.44082,-5.30347,-5.77434,-5.73064,-4.91272],'cal/mol/K','+|-',[3.80893,6.03046,7.36601,7.15284,4.68653,2.33789,2]),
        H298 = (107.416,'kcal/mol','+|-',2.4),
        S298 = (3.45818,'cal/mol/K','+|-',3.90492),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 352,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   O   u0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,S}
5   R!H ux {4,S} {6,S}
6   O   u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.66831,-4.73758,-7.0451,-7.83239,-7.43128,-6.55721,-4.38706],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (106.865,'kcal/mol','+|-',2.4),
        S298 = (4.83878,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]COCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 353,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   O   u0 {2,S} {4,S}
4   O   u0 r0 {3,S} {5,S}
5   R!H ux {4,S} {6,S}
6   O   u0 r0 {5,S}
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
[O]COOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 354,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-2C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.968866,0.741762,0.402841,0.476043,0.534574,0.412253,-1.39425],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.294,'kcal/mol','+|-',5.2),
        S298 = (-7.80818,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(O)(O)OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 355,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   O   u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   C   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7664,-2.53507,-3.06903,-3.31107,-3.45307,-3.5701,-3.993],'cal/mol/K','+|-',[3,4.33134,4.94369,4.4267,3,3,3]),
        H298 = (106.05,'kcal/mol','+|-',5.2),
        S298 = (-1.68298,'cal/mol/K','+|-',5.28637),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 356,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_5R!H->C_4R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S}
3   O u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.79303,-4.65542,-5.48914,-5.4781,-4.65113,-4.07765,-4.04129],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.718,'kcal/mol','+|-',5.2),
        S298 = (0.904887,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 357,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_5R!H->C_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,S}
3   O u0 r0 {2,S} {4,S}
4   O u0 r0 {3,S} {5,S}
5   C ux {4,S}
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
COOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 358,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * O                      u1 r0 {2,[S,D,T,B,Q]}
2   C                      ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O                      ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H                    ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   [P,F,I,Br,Cl,O,Si,S,N] u0 r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.1481,-4.74908,-4.6837,-4.44765,-3.97593,-3.9202,-4.36016],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (107.905,'kcal/mol','+|-',2.4),
        S298 = (1.99044,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 359,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83573,-3.11409,-3.9299,-4.34272,-4.5314,-4.7954,-5.18678],'cal/mol/K','+|-',[4.01342,4.85343,5.4193,5.57131,5.35238,5.02255,4.83818]),
        H298 = (88.8517,'kcal/mol','+|-',9.69269),
        S298 = (-1.2451,'cal/mol/K','+|-',9.42494),
    ),
    shortDesc = """Radical correction fitted to 151 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 360,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.92389,-3.72442,-4.96712,-5.49523,-5.54136,-5.77199,-6.62418],'cal/mol/K','+|-',[3.18953,3.29909,3.72551,3.79398,3.15698,3,4.87822]),
        H298 = (89.2856,'kcal/mol','+|-',10.5495),
        S298 = (-0.63611,'cal/mol/K','+|-',6.47492),
    ),
    shortDesc = """Radical correction fitted to 29 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 361,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.82229,-3.64702,-4.91593,-5.47951,-5.53478,-5.79158,-6.76289],'cal/mol/K','+|-',[3.26694,3.38713,3.863,3.97485,3.32445,3.14775,5.0528]),
        H298 = (88.4996,'kcal/mol','+|-',7.84584),
        S298 = (-0.581342,'cal/mol/K','+|-',6.56004),
    ),
    shortDesc = """Radical correction fitted to 26 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 362,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_6R!H->O",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {6,S}
4   C   u0 {3,S} {5,S}
5   R!H ux {4,S}
6   O   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.114185,-3.08195,-5.36691,-6.09775,-6.36174,-7.1725,-6.51417],'cal/mol/K','+|-',[3.4168,3,3,3,3,3,3]),
        H298 = (99.6082,'kcal/mol','+|-',5.2),
        S298 = (1.22115,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 363,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_6R!H->O_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S} {6,S}
4   C u0 r1 {3,S} {5,S}
5   C ux r1 {4,S}
6   O ux r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32221,-3.71406,-5.46206,-5.81932,-5.77794,-6.53819,-5.67142],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.4968,'kcal/mol','+|-',5.2),
        S298 = (1.8442,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1OC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 364,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_6R!H->O_N-5R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S} {6,S}
4   C u0 r1 {3,S} {5,S}
5   O ux r1 {4,S}
6   O ux r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09384,-2.44984,-5.27175,-6.37618,-6.94553,-7.8068,-7.35692],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.7197,'kcal/mol','+|-',5.2),
        S298 = (0.598104,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1OCOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 365,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
6   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9512,-3.68967,-4.8819,-5.43285,-5.47237,-5.68736,-6.78166],'cal/mol/K','+|-',[3.17316,3.48593,4.00496,4.11142,3.40471,3.14988,5.22679]),
        H298 = (87.7918,'kcal/mol','+|-',5.48062),
        S298 = (-0.717379,'cal/mol/K','+|-',6.72568),
    ),
    shortDesc = """Radical correction fitted to 24 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 366,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_Sp-4R!H=3R!H",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,D} {6,S}
4   R!H u0 r1 {3,D} {5,S}
5   R!H ux {4,S}
6   C   ux r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.286349,-0.928771,-1.41186,-1.82789,-2.32615,-2.51079,-3.29808],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.1594,'kcal/mol','+|-',5.2),
        S298 = (-8.34978,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 367,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   R!H ux {3,S} {5,S}
5   R!H ux {4,S}
6   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.01649,-3.79794,-5.01798,-5.57422,-5.59575,-5.81193,-6.91827],'cal/mol/K','+|-',[3.16427,3.36918,3.82678,3.92184,3.22161,3,5.13578]),
        H298 = (87.6809,'kcal/mol','+|-',5.42958),
        S298 = (-0.418069,'cal/mol/K','+|-',6.09424),
    ),
    shortDesc = """Radical correction fitted to 23 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 368,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux {3,S} {5,S}
5   R!H ux {4,S}
6   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.84952,-3.61568,-4.78904,-5.35574,-5.45874,-5.71467,-6.93232],'cal/mol/K','+|-',[3.0182,3,3,3.20856,3,3,5.30075]),
        H298 = (87.3158,'kcal/mol','+|-',5.2),
        S298 = (-0.845291,'cal/mol/K','+|-',4.60639),
    ),
    shortDesc = """Radical correction fitted to 21 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 369,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux {3,S} {5,S}
5   R!H ux {4,S}
6   C   ux {3,[S,D,T,B,Q]}
7   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59467,-4.34412,-5.40048,-5.94503,-5.81734,-5.92221,-7.82054],'cal/mol/K','+|-',[3,3,3,3,3,3,5.33205]),
        H298 = (87.3676,'kcal/mol','+|-',5.2),
        S298 = (-1.03608,'cal/mol/K','+|-',5.84853),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 370,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux {3,S} {5,S}
5   O ux {4,S}
6   C ux {3,[S,D,T,B,Q]}
7   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.69822,-4.46926,-5.48931,-5.99186,-5.86291,-5.96182,-7.9868],'cal/mol/K','+|-',[3,3,3,3,3,3,5.45967]),
        H298 = (87.319,'kcal/mol','+|-',5.2),
        S298 = (-1.28378,'cal/mol/K','+|-',5.85776),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 371,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux r1 {3,S} {5,S}
5   O ux {4,S}
6   C ux {3,[S,D,T,B,Q]}
7   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.76111,-4.59531,-5.64303,-6.1403,-5.98495,-6.06762,-8.24767],'cal/mol/K','+|-',[3,3,3,3,3,3,5.45095]),
        H298 = (87.1589,'kcal/mol','+|-',5.2),
        S298 = (-1.24063,'cal/mol/K','+|-',6.17526),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 372,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_6BrCClFINPSSi-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S}
5   O   ux {4,S}
6   C   ux r1 {3,[S,D,T,B,Q]}
7   C   ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.03311,-3.67781,-4.83125,-5.44021,-5.23856,-5.49109,-9.87467],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.2226,'kcal/mol','+|-',5.2),
        S298 = (-5.4944,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 373,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_6BrCClFINPSSi-inRing_Ext-7R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,S} {7,S}
4   C   ux r1 {3,S} {5,S}
5   O   u0 r1 {4,S}
6   C   u0 r1 {3,S}
7   C   u0 r0 {3,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
9   R!H ux {7,[S,D,T,B,Q]}
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
    index = 374,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_6BrCClFINPSSi-inRing_Ext-4C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S} {9,[S,D,T,B,Q]}
5   O   ux r1 {4,S}
6   C   ux r1 {3,[S,D,T,B,Q]}
7   C   ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
9   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.73759,-4.12785,-5.57471,-6.33927,-6.13763,-6.44275,-10.6903],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.8091,'kcal/mol','+|-',5.2),
        S298 = (-5.21267,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 375,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S}
5   O   ux {4,S}
6   C   ux r0 {3,[S,D,T,B,Q]}
7   C   ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.06235,-4.97496,-5.97894,-6.42999,-6.29381,-6.30618,-7.57443],'cal/mol/K','+|-',[3,3,3,3,3,3.0173,5.97158]),
        H298 = (87.1392,'kcal/mol','+|-',5.2),
        S298 = (0.519553,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 376,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_Ext-7R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S}
5   O   ux {4,S}
6   C   ux r0 {3,[S,D,T,B,Q]}
7   C   ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
9   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.32395,-5.25266,-6.03502,-6.27643,-5.96478,-5.84012,-7.50739],'cal/mol/K','+|-',[3,3,3,3.45771,3.10644,3.26862,8.265]),
        H298 = (86.1777,'kcal/mol','+|-',5.2),
        S298 = (0.381384,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 377,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R",
    group = 
"""
1  * O   u1 r0 {2,[S,D,T,B,Q]}
2    O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3    C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,S} {7,S}
4    C   ux r1 {3,S} {5,S}
5    O   u0 r1 {4,S} {10,S}
6    C   u0 r0 {3,S}
7    C   u0 r1 {3,S} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]} {11,[S,D,T,B,Q]}
8    R!H ux {7,[S,D,T,B,Q]}
9    R!H ux {7,[S,D,T,B,Q]}
10   O   u0 r1 {5,S}
11   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.37838,-5.9008,-7.41672,-8.14646,-7.7319,-7.76844,-11.4895],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.9072,'kcal/mol','+|-',5.2),
        S298 = (-0.476351,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(O[O])COOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 378,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_Ext-7R!H-R_Ext-7R!H-R",
    group = 
"""
1  * O   u1 r0 {2,[S,D,T,B,Q]}
2    O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3    C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4    C   ux r1 {3,S} {5,S}
5    O   ux r1 {4,S}
6    C   ux r0 {3,[S,D,T,B,Q]}
7    C   ux r1 {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
8    R!H ux {7,[S,D,T,B,Q]}
9    R!H ux {7,[S,D,T,B,Q]}
10   R!H ux {7,[S,D,T,B,Q]}
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
CC1(C)OOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 379,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_Ext-5O-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S}
5   O   ux r1 {4,S} {9,[S,D,T,B,Q]}
6   C   ux r0 {3,[S,D,T,B,Q]}
7   C   ux r1 {3,[S,D,T,B,Q]} {8,S}
8   R!H ux r1 {7,S}
9   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.45358,-4.15032,-5.69871,-6.95359,-7.83149,-8.63434,-7.00658],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.2602,'kcal/mol','+|-',5.2),
        S298 = (1.88625,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(O[O])CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 380,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_8R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux r1 {3,S} {5,S}
5   O ux r1 {4,S}
6   C ux r0 {3,[S,D,T,B,Q]}
7   C ux r1 {3,[S,D,T,B,Q]} {8,S}
8   C ux r1 {7,S}
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
C=C1CC(C)(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 381,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_N-8R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux r1 {3,S} {5,S}
5   O ux r1 {4,S}
6   C ux r0 {3,[S,D,T,B,Q]}
7   C ux r1 {3,[S,D,T,B,Q]} {8,S}
8   O ux r1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.08231,-5.01751,-5.82472,-6.36884,-6.27073,-6.24495,-9.91839],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.8648,'kcal/mol','+|-',5.2),
        S298 = (-0.872423,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 382,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_N-4C-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C u0 r0 {3,S} {5,S}
5   O ux {4,S}
6   C ux r1 {3,[S,D,T,B,Q]}
7   C ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05365,-3.17728,-3.91359,-4.4704,-4.61193,-4.87743,-5.3129],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.3514,'kcal/mol','+|-',5.2),
        S298 = (-1.72607,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1(C(=O)O)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 383,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_N-5R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,S} {7,S}
4   C ux {3,S} {5,S}
5   C u0 {4,S}
6   C u0 r1 {3,S}
7   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42971,-2.93628,-4.40123,-5.41811,-5.30468,-5.47653,-5.95011],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.0322,'kcal/mol','+|-',5.2),
        S298 = (1.75057,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(O[O])CCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 384,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux {3,S} {5,S}
5   R!H ux {4,S}
6   C   ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.807506,-3.13335,-4.74029,-5.36374,-5.62369,-6.10929,-6.57245],'cal/mol/K','+|-',[3.52342,3.07584,3.16263,3.50195,3.10031,3,5.20984]),
        H298 = (87.1742,'kcal/mol','+|-',6.60754),
        S298 = (-0.560736,'cal/mol/K','+|-',3.5985),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 385,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_5R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux {3,S} {5,S}
5   O   ux {4,S}
6   C   ux {3,[S,D,T,B,Q]} {7,S}
7   R!H ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.06071,-4.31753,-6.07773,-7.05566,-7.12607,-7.01614,-10.6225],'cal/mol/K','+|-',[3,3,3,3.02949,3.21412,3,3]),
        H298 = (84.672,'kcal/mol','+|-',5.2),
        S298 = (-0.776477,'cal/mol/K','+|-',4.66196),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 386,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_5R!H->O_Ext-4C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S} {8,[S,D,T,B,Q]}
5   O   ux r1 {4,S}
6   C   ux r1 {3,[S,D,T,B,Q]} {7,S}
7   R!H ux r1 {6,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79754,-3.74765,-5.20173,-5.98457,-5.9897,-6.05678,-10.3654],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.5136,'kcal/mol','+|-',5.2),
        S298 = (-2.42473,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)C1(C)OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 387,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux {3,S} {5,S}
5   C   ux {4,S}
6   C   ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.389769,-2.73862,-4.29447,-4.79977,-5.12289,-5.80701,-5.22243],'cal/mol/K','+|-',[3.73082,3.11993,3,3.03755,3,3,3]),
        H298 = (88.0082,'kcal/mol','+|-',6.82885),
        S298 = (-0.488822,'cal/mol/K','+|-',3.69902),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 388,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux {3,S} {5,S}
5   C   ux {4,S}
6   C   ux {3,[S,D,T,B,Q]} {7,D}
7   R!H ux {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.053698,-2.50615,-4.04214,-4.41637,-4.69509,-5.30871,-4.91767],'cal/mol/K','+|-',[3.74305,3.24749,3.04778,3,3,3,3]),
        H298 = (86.9378,'kcal/mol','+|-',5.2),
        S298 = (-0.908258,'cal/mol/K','+|-',3.43885),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 389,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi_Ext-6BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {6,S}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S}
6   C   u0 r1 {3,S} {7,D} {8,[S,D,T,B,Q]}
7   R!H u0 {6,D}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.41616,-0.718612,-2.22385,-2.68317,-3.38292,-4.63175,-4.68217],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.5371,'kcal/mol','+|-',5.2),
        S298 = (-3.82554,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 390,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi_Ext-4C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {6,S}
4   C   u0 {3,S} {5,S} {8,[S,D,T,B,Q]}
5   C   u0 {4,S}
6   C   u0 {3,S} {7,D}
7   C   u0 {6,D}
8   R!H u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17726,-2.02034,-4.0474,-4.53012,-4.79792,-5.45318,-4.83449],'cal/mol/K','+|-',[3,3.3607,4.11837,3.42768,3,3,3]),
        H298 = (87.9495,'kcal/mol','+|-',8.39893),
        S298 = (-0.377254,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 391,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi_Ext-4C-R_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {6,S}
4   C   u0 r1 {3,S} {5,S} {8,[S,D,T,B,Q]}
5   C   u0 r1 {4,S} {9,[S,D,T,B,Q]}
6   C   u0 r1 {3,S} {7,D}
7   C   u0 r1 {6,D}
8   R!H u0 {4,[S,D,T,B,Q]}
9   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.448491,-3.20853,-5.50346,-5.74199,-5.22782,-5.30534,-5.41051],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.98,'kcal/mol','+|-',5.2),
        S298 = (-1.0888,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1C=CCCC1C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 392,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi_Ext-5C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux r1 {3,S} {5,S}
5   C   ux r1 {4,S} {8,[S,D,T,B,Q]}
6   C   ux r1 {3,[S,D,T,B,Q]} {7,D}
7   C   ux r1 {6,D}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13741,-4.23846,-5.17894,-5.27636,-5.29296,-5.65703,-5.23171],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.0933,'kcal/mol','+|-',5.2),
        S298 = (0.113167,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=CC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 393,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_N-Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C ux r1 {3,S} {5,S}
5   C ux r1 {4,S}
6   C ux r1 {3,[S,D,T,B,Q]} {7,S}
7   C ux r1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07013,-3.90098,-5.55615,-6.71675,-7.26191,-8.29849,-6.74624],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.3604,'kcal/mol','+|-',5.2),
        S298 = (1.60836,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1CCOC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 394,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C ux r1 {3,S} {5,S}
5   C ux {4,S}
6   C ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00722,-2.2622,-3.03645,-3.44537,-3.52197,-4.02343,-4.78042],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.4034,'kcal/mol','+|-',5.2),
        S298 = (-0.575404,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1CC1C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 395,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_N-5R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C ux r1 {3,S} {5,S}
5   O ux {4,S}
6   C ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.87185,-1.96628,-2.41237,-2.96798,-3.78063,-3.93335,-4.33236],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (87.3766,'kcal/mol','+|-',2.4),
        S298 = (-0.938269,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 396,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,S} {6,S}
4   O ux {3,S} {5,S}
5   C u0 {4,S}
6   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.97842,-5.93944,-7.70795,-8.14138,-7.20573,-6.9547,-6.75322],'cal/mol/K','+|-',[3,7.88164,9.66836,9.33045,7.01134,4.55316,3.83221]),
        H298 = (92.8636,'kcal/mol','+|-',11.1975),
        S298 = (4.60179,'cal/mol/K','+|-',14.5134),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 397,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_N-4R!H->C_Ext-6BrCClFINPSSi-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {6,S}
4   O   ux r1 {3,S} {5,S}
5   C   u0 r1 {4,S} {8,[S,D,T,B,Q]}
6   C   u0 r1 {3,S} {7,D}
7   C   u0 r1 {6,D}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.90727,-8.72602,-11.1262,-11.4402,-9.68461,-8.56448,-8.10811],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.8225,'kcal/mol','+|-',5.2),
        S298 = (9.73306,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1C=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 398,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
5   C ux {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.88915,-4.45968,-5.45342,-5.64456,-5.60386,-5.58587,-5.30638],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.0344,'kcal/mol','+|-',21.2315),
        S298 = (-1.15641,'cal/mol/K','+|-',6.80739),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 399,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 {3,S} {5,[B,D,T,Q]}
5   C ux {4,[B,D,T,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.15337,-4.81788,-5.83695,-5.89681,-5.52402,-5.33109,-5.09378],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.887,'kcal/mol','+|-',8.92094),
        S298 = (0.805264,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 400,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R_6R!H->O_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
4   C   u0 r1 {3,S} {5,[B,D,T,Q]}
5   C   ux r1 {4,[B,D,T,Q]} {6,[S,D,T,B,Q]}
6   O   ux r0 {5,[S,D,T,B,Q]}
7   C   ux r1 {3,[S,D,T,B,Q]} {8,D}
8   C   u0 r1 {7,D} {9,[S,D,T,B,Q]}
9   R!H ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.769,-5.72167,-6.75537,-6.53559,-5.69945,-5.23101,-4.87452],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.041,'kcal/mol','+|-',5.2),
        S298 = (1.00689,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC1C=C(O)C(O)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 401,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,D,T,B,Q]}
2   O ux r0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C u0 r1 {4,D} {6,S}
6   C u0 r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.36071,-3.7433,-4.68635,-5.14006,-5.76354,-6.09543,-5.73157],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.3299,'kcal/mol','+|-',5.2),
        S298 = (-5.07975,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC(O[O])C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 402,
    label = "RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_N-3R!H-inRing",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.81804,-2.99164,-3.7218,-4.11149,-4.32876,-4.59946,-4.89838],'cal/mol/K','+|-',[4.16951,5.0844,5.61919,5.76533,5.61476,5.25964,4.63763]),
        H298 = (88.7829,'kcal/mol','+|-',9.5945),
        S298 = (-1.36728,'cal/mol/K','+|-',9.91559),
    ),
    shortDesc = """Radical correction fitted to 122 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(O)C(=O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COCOO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]OCC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)CC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1CC(C)(CO[O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CC(C)O[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCOCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)OC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC(C)(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CCCO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1(OO)COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CCO)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CCC(C)(O[O])C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CC(=O)OC(=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(CO)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(CCO[O])OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=CC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)(O[O])C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(=O)C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CCC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 403,
    label = "RJ1_N-1R-inRing_N-1R->O",
    group = 
"""
1 * [H,C] u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0394709,-0.780778,-1.42854,-1.90163,-2.52086,-3.03969,-4.03926],'cal/mol/K','+|-',[3.1043,3.48875,3.75847,3.80398,3.66204,3.51711,3.64396]),
        H298 = (95.3638,'kcal/mol','+|-',22.3289),
        S298 = (0.446911,'cal/mol/K','+|-',9.62434),
    ),
    shortDesc = """Radical correction fitted to 363 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CCC(C)(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC(OO)C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C=O)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(COO)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC1([CH]C=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=O)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)OOC1C=CCC(C)=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]COC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CCC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COO)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)[CH]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC(O)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](C)C(C)(C)CC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOC(C)(C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
CC(C)=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC(C)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[CH2]C=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH]=CCC#C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[C]#CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C=CCC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOC(O)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[C]=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(COC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C1OOC(C)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
C=CC(=C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](O)C=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(N(CC)O)C[CH]C=C - Radical thermo from pang.py and closed shell thermo from pang.py
C=C[CH]COOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C](O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCCO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC#C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]COC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C([CH]O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=O)C[C](C=O)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CC=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=COC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C](C)CCC(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([C]=O)OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
OC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1([CH]O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=COC - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC(C)CO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C=C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C[C](C)C(C)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C1C=COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC(C)=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCCC=CCC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(O)=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC#CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
CC(=O)O[C]=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(=O)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1CC(C)=CCC1C - Radical thermo from pang.py and closed shell thermo from GAV
C=C=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=CCCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[CH]=C=C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(N(CC)O)C(C=C)[CH2] - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C#CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=C(C)[CH]CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]OC(C)=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C=O)C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C=C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C=CC#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[H] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[C]#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)OC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CC1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC(CC(=C)C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C[C]=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1(C(C)C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]OC(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(C)(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(CO)OOCC1(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)CC(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(OC(=C)C(=C)C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=O)=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1(CC=CC)C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COC=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C=C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC(CC=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)CCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[C]=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[C](O)C(=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CN(CC)O - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C(=O)OCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]C(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]CCOO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
[CH2]C1=CC(C)=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC=C[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C(=C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=COC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[C]=CC=CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)C1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOCC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]CC#CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]C1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC1(CC=CC)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)OOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=COC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([CH]O)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(CC=CC)CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCC(CON(CC)CC)C=C - Radical thermo from pang.py and closed shell thermo from pang.py
CC(=O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C(C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(=C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(=O)C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]OC - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
[CH2]C(C)=C(COO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C1=CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(OC)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
C=C[CH]C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC12COOC2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)COC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC1OC1[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C=C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(C)(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_1R-inRing
            L4: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_8R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_N-8R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_5R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_N-5R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Int-6R!H-5R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_Int-6R!H-5R!H_Ext-5R!H-R_Ext-3R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_5R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_5R!H->O_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_5R!H->O_Ext-1R-R_Ext-2R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_N-5R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_Sp-5R!H=4R!H_N-5R!H->O_Ext-2R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_5R!H->C_Ext-5C-R_Ext-7R!H-R_Sp-8R!H-7R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_5R!H->C_Ext-5C-R_Ext-7R!H-R_Sp-8R!H-7R!H_5C-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_5R!H->C_Ext-5C-R_Ext-7R!H-R_Sp-8R!H-7R!H_N-5C-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_5R!H->C_Ext-5C-R_Ext-7R!H-R_N-Sp-8R!H-7R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_N-5R!H->C_Ext-5O-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-4R!H_N-5R!H->C_Ext-5O-R_Ext-7R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-2R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-2R!H-R_Ext-4R!H-R_8R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-2R!H-R_Ext-4R!H-R_N-8R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-1R-R_Ext-5R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_Ext-1R-R_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_Ext-6C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_Ext-6C-R_Ext-6C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-3R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-3R!H-R_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-4C-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-4C-R_7R!H->O
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-4C-R_N-7R!H->O
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_4R!H->C_Ext-4C-R_N-7R!H->O_Ext-4C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_6R!H->C_N-4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-6R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-3R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-5R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H_7R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H_N-7R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-5R!H=4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-2R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_6R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_6R!H->C_Sp-2R!H-1R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_6R!H->C_Sp-2R!H-1R_Ext-6C-R_Sp-7R!H=6C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_6R!H->C_Sp-2R!H-1R_Ext-6C-R_N-Sp-7R!H=6C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_6R!H->C_N-Sp-2R!H-1R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_4R!H->C_Ext-6BrClFINOPSSi-R_7R!H->N
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_4R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_4R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_8R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_4R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->N_Ext-7BrCClFIOPSSi-R_N-8R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-1R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->C_N-4R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-1R
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_2R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_2R!H-inRing_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_2R!H-inRing_Ext-2R!H-R_Ext-4R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_N-2R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_N-2R!H-inRing_Ext-2R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_3R!H->C_N-2R!H-inRing_Ext-3C-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_4R!H->O
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_4R!H->O_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_4R!H->O_Ext-2R!H-R_2R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_4R!H->O_Ext-2R!H-R_N-2R!H-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_6R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C_2R!H-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C_2R!H-inRing_Ext-6BrClFINOPSSi-R_Ext-4C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_Ext-1R-R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C_N-2R!H-inRing
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-3R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-3R!H-R_Ext-2R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-3R!H-R_Ext-4C-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-3R!H-R_5R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-3R!H-R_N-5R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-4C-R_5R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-4C-R_5R!H->C_3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-4C-R_5R!H->C_N-3R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-4C-R_N-5R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-2R!H-R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_5R!H->C_3R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_5R!H->C_N-3R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_N-5R!H->C_Ext-6R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H-inRing_Ext-1R-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-3R!H->C
            L4: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_Ext-2R!H-R
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_Ext-1R-R_Ext-5R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_3R!H->C_Ext-2R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_3R!H->C_Ext-3C-R_5R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_3R!H->C_Ext-3C-R_N-5R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-1R-R_Int-4R!H-2R!H_N-3R!H->C
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_5R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_5R!H-inRing_2R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_5R!H-inRing_N-2R!H->O
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_5R!H-inRing_N-2R!H->O_Ext-3O-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_N-5R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_4R!H->O_N-5R!H-inRing_Ext-5R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Int-7R!H-6R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Int-7R!H-6R!H_6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Int-7R!H-6R!H_N-6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Int-7R!H-6R!H_N-6R!H->C_4C-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Int-7R!H-6R!H_N-6R!H->C_N-4C-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_4C-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_4C-inRing_6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_4C-inRing_N-6R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_N-4C-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Int-5C-3O
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_5C-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_N-5C-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_N-5C-inRing_Ext-2R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_N-5C-inRing_Int-6R!H-3O_Ext-5C-R_Ext-5C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_Int-3O-1R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_4R!H->C_Ext-3O-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_4R!H->C_Ext-3O-R_Ext-5C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_N-4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_5R!H->C_N-4R!H->C_Ext-2R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_N-5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_2R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_2R!H->C_Ext-2C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_3O-inRing_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_N-2R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H-7R!H_Ext-8R!H-R_Ext-6R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H-7R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H-7R!H_5R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_3R!H->O_N-3O-inRing_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H-7R!H_N-5R!H-inRing
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Int-5R!H-1R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Sp-4C-3C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Sp-4C-3C_Ext-3C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Sp-4C-3C_Ext-3C-R_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Sp-4C-3C_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_N-Sp-4C-3C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-5R!H-R_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-1R-R_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_2R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_4R!H->C_N-2R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_N-4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_N-4R!H->C_Ext-3C-R_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_N-4R!H->C_Ext-3C-R_Ext-1R-R_2R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_N-4R!H->C_Ext-3C-R_Ext-1R-R_N-2R!H->C
        L3: RJ1_N-1R-inRing
            L4: RJ1_N-1R-inRing_1R->O
                L5: RJ1_N-1R-inRing_1R->O_Ext-1O-R
                    L6: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C_Ext-5C-R_6R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C_Ext-5C-R_N-6R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C_Ext-3C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C_Ext-3C-R_Int-6R!H-5O
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C_Ext-3C-R_Int-6R!H-5O_Ext-6R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C_Ext-3C-R_Int-6R!H-5O_Ext-3C-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->C_Ext-3C-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->C_4C-inRing
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_5R!H->C_N-4C-inRing
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_N-5R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-4C-R_Ext-6R!H-R_N-5R!H->C_Ext-5O-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-5R!H-R_Ext-5R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R_6R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H-4C_Ext-3C-R_N-6R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H-4C_Ext-3C-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_3C-inRing
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_N-3C-inRing
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_N-3C-inRing_Ext-3C-R_Ext-3C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_N-3C-inRing_Ext-3C-R_Ext-3C-R_5R!H->O
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_4R!H->C_N-3C-inRing_Ext-3C-R_Ext-3C-R_N-5R!H->O
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-5C-R_Ext-6R!H-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-5C
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H-5C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-5C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-3C-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-3C-R_Ext-6R!H-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_5R!H->C_Ext-3C-R_Ext-3C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_N-5R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H_7R!H->O
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H_7R!H->O_Ext-7O-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H_7R!H->O_4R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H_7R!H->O_N-4R!H->C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_Sp-7R!H-5R!H_N-7R!H->O
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->C_Ext-5R!H-R_N-Sp-7R!H-5R!H
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_4R!H-inRing
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Sp-5R!H-4C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_N-Sp-5R!H-4C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C_Ext-4C-R_Sp-5R!H-4C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C_Ext-4C-R_Sp-5R!H-4C_Ext-5R!H-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_4R!H->C_N-Sp-4C-3C_Ext-4C-R_N-Sp-5R!H-4C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-2C-inRing_Ext-3C-R_N-4R!H-inRing_N-4R!H->C
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_4R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C_Ext-4R!H-R_Ext-2C-R
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_7R!H->O
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_7R!H->O_3R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_7R!H->O_3R!H->C_Ext-2C-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_7R!H->O_N-3R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_3R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H=4R!H_N-3R!H->C
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_4R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_4R!H->C_Ext-2C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_4R!H->C_Ext-2C-R_3R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_4R!H->C_Ext-2C-R_N-3R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_2C-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-4R!H->C
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_6R!H-inRing
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_6R!H-inRing_Ext-3C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H-inRing
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H-inRing_3C-inRing
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H-inRing_N-3C-inRing
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H-inRing_N-3C-inRing_Ext-3C-R
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_N-6R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-8R!H-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_Ext-5R!H-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_Ext-5R!H-R_Ext-2C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_4R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_4R!H->C_Ext-4C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-3C-R_N-4R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_Ext-4R!H-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_3C-inRing
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_6R!H->O_N-3C-inRing
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-5R!H-R_N-6R!H->O
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_6R!H->O
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_6R!H->O_Ext-3C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_6R!H->O_3C-inRing
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_6R!H->O_N-3C-inRing
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_Sp-4R!H-3C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_Sp-4R!H-3C_Ext-4R!H-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_Sp-4R!H-3C_4R!H->C
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_Sp-4R!H-3C_4R!H->C_Ext-2C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_Sp-4R!H-3C_N-4R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_N-6R!H->O_N-Sp-4R!H-3C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_4R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-4R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-4R!H->C_Ext-2C-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_4R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_4R!H->C_Ext-3C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_4R!H->C_Ext-3C-R_Ext-2C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_4R!H->C_5R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_4R!H->C_N-5R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_N-4R!H->C
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_Sp-5R!H=3C_N-4R!H->C_Ext-3C-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_N-Sp-5R!H=3C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_N-Sp-5R!H=3C_Ext-2C-R
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-2C-R_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_3R!H->C_Ext-3C-R_Ext-3C-R
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_4R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_Ext-5R!H-R_N-4R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-2C-R
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_5R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_5R!H->C_4R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_5R!H->C_N-4R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_2R!H->C_Ext-2C-R_N-Sp-3R!H=2C_N-2C-inRing_N-3R!H->C_Ext-3O-R_Ext-4R!H-R_N-5R!H->C
                    L6: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_6R!H->O
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_6R!H->O_5R!H->C
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_6R!H->O_N-5R!H->C
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_Sp-4R!H=3R!H
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_6BrCClFINPSSi-inRing
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_6BrCClFINPSSi-inRing_Ext-7R!H-R
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_6BrCClFINPSSi-inRing_Ext-4C-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_Ext-7R!H-R
                                                                L17: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_Ext-7R!H-R_Ext-5O-R_Ext-7R!H-R
                                                                L17: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_Ext-7R!H-R_Ext-7R!H-R
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_Ext-5O-R
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_8R!H->C
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_4C-inRing_Ext-7R!H-R_N-6BrCClFINPSSi-inRing_N-8R!H->C
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_5R!H->O_N-4C-inRing
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-3R!H-R_N-5R!H->O
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_5R!H->O
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_5R!H->O_Ext-4C-R
                                                L13: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi_Ext-6BrCClFINPSSi-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi_Ext-4C-R
                                                            L16: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi_Ext-4C-R_Ext-5C-R
                                                        L15: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi_Ext-5C-R
                                                    L14: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_Ext-6BrCClFINPSSi-R_N-5R!H->O_N-Sp-7R!H=6BrBrCCClClFFIINNPPSSSiSi
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_5R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_4R!H->C_N-5R!H->C
                                        L11: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_N-4R!H->C
                                            L12: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-3R!H-R_N-6R!H->O_N-Sp-4R!H=3R!H_N-4R!H->C_Ext-6BrCClFINPSSi-R_Ext-5R!H-R
                            L8: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R_6R!H->O
                                    L10: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R_6R!H->O_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R
                                L9: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R_N-6R!H->O
                        L7: RJ1_N-1R-inRing_1R->O_Ext-1O-R_N-2R!H->C_Ext-2BrClFINOPSSi-R_N-3R!H-inRing
            L4: RJ1_N-1R-inRing_N-1R->O
"""
)

