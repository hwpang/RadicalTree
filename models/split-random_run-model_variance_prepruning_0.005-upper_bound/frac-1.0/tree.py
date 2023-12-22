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
        Cpdata = ([-0.613842,-1.60862,-2.32653,-2.74462,-3.18024,-3.56575,-4.37794],'cal/mol/K','+|-',[4.0286,4.66323,4.95301,4.90554,4.53532,4.26771,4.22897]),
        H298 = (94.1973,'kcal/mol','+|-',25.1453),
        S298 = (0.469617,'cal/mol/K','+|-',10.1985),
    ),
    shortDesc = """Radical correction fitted to 2532 radicals""",
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
        Cpdata = ([-0.613842,-1.60862,-2.32653,-2.74462,-3.18024,-3.56575,-4.37794],'cal/mol/K','+|-',[4.0286,4.66323,4.95301,4.90554,4.53532,4.26771,4.22897]),
        H298 = (94.1973,'kcal/mol','+|-',25.1453),
        S298 = (0.469617,'cal/mol/K','+|-',10.1985),
    ),
    shortDesc = """Radical correction fitted to 2532 radicals""",
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
        Cpdata = ([0.145366,-1.12595,-2.09378,-2.67145,-3.35012,-3.9022,-4.96075],'cal/mol/K','+|-',[3,3.4815,3.8703,3.86408,3.52033,3.42139,3.96189]),
        H298 = (93.5403,'kcal/mol','+|-',32.9325),
        S298 = (1.04783,'cal/mol/K','+|-',7.50318),
    ),
    shortDesc = """Radical correction fitted to 458 radicals""",
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
        Cpdata = ([0.211741,-1.11983,-2.07081,-2.60517,-3.24703,-3.77149,-4.58933],'cal/mol/K','+|-',[3.0175,3.5635,3.80085,3.69801,3.31495,3.21065,3.11506]),
        H298 = (86.0237,'kcal/mol','+|-',34.0026),
        S298 = (0.399028,'cal/mol/K','+|-',7.77933),
    ),
    shortDesc = """Radical correction fitted to 250 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.249773,-1.12611,-2.10209,-2.63422,-3.25402,-3.77176,-4.57843],'cal/mol/K','+|-',[3.10477,3.70224,3.93693,3.82116,3.39635,3.27436,3.20121]),
        H298 = (83.0277,'kcal/mol','+|-',29.681),
        S298 = (0.327991,'cal/mol/K','+|-',8.03647),
    ),
    shortDesc = """Radical correction fitted to 236 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.269328,-1.23843,-2.18955,-2.68076,-3.25752,-3.74065,-4.51598],'cal/mol/K','+|-',[3.13871,3.76895,3.75246,3.38739,3,3,3]),
        H298 = (79.6193,'kcal/mol','+|-',19.2511),
        S298 = (-0.34586,'cal/mol/K','+|-',7.87105),
    ),
    shortDesc = """Radical correction fitted to 161 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
4   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.519309,-0.62539,-1.51664,-2.09086,-2.82636,-3.48983,-4.23855],'cal/mol/K','+|-',[3,3.8042,3.8304,3.65626,3.09723,3,3.83281]),
        H298 = (79.3606,'kcal/mol','+|-',38.8659),
        S298 = (0.705474,'cal/mol/K','+|-',7.42098),
    ),
    shortDesc = """Radical correction fitted to 21 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   O   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.735114,-0.514993,-1.433,-1.71319,-2.3607,-3.40429,-1.8787],'cal/mol/K','+|-',[3,3,3,3,3,3,6.17697]),
        H298 = (111.279,'kcal/mol','+|-',96.6523),
        S298 = (0.178147,'cal/mol/K','+|-',8.6324),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-2R!H-R_5R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D}
4   O ux {1,S}
5   C ux r1 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.600653,-1.03172,-2.15084,-2.36973,-2.99362,-4.29058,0.127238],'cal/mol/K','+|-',[3,3,3,3,3,3,7.06874]),
        H298 = (151.534,'kcal/mol','+|-',5.2),
        S298 = (3.14285,'cal/mol/K','+|-',4.15853),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 9,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-2R!H-R_5R!H-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   O   ux {1,S}
5   C   ux r1 {2,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.39628,-0.367913,-1.70853,-1.99808,-2.82698,-3.96536,-2.37194],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (151.485,'kcal/mol','+|-',5.2),
        S298 = (4.61311,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1C2=COC1OOC2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 10,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-2R!H-R_N-5R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   O   ux {1,S}
5   R!H ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.869575,0.00173965,-0.715163,-1.05665,-1.72778,-2.518,-3.88463],'cal/mol/K','+|-',[3,4.1923,4.12335,3.57969,3,3,3]),
        H298 = (71.0235,'kcal/mol','+|-',45.7928),
        S298 = (-2.78656,'cal/mol/K','+|-',8.10126),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 11,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-2R!H-R_N-5R!H-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   O   ux {1,S}
5   R!H ux r0 {2,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0521994,-1.48046,-2.17299,-2.32226,-2.70082,-2.9039,-3.76351],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.2137,'kcal/mol','+|-',5.2),
        S298 = (0.0776708,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1C=CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 12,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H",
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
        Cpdata = ([0.649195,-0.490256,-1.40659,-2.01173,-2.72506,-3.30537,-4.45714],'cal/mol/K','+|-',[3,3.514,3.61144,3.59965,3.08162,3,3]),
        H298 = (77.1215,'kcal/mol','+|-',15.715),
        S298 = (0.654845,'cal/mol/K','+|-',7.53093),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 13,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   O   ux {1,S}
5   R!H ux r1 {3,S}
6   R!H ux {3,[S,D,T,B,Q]}
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
    index = 14,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing",
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
        Cpdata = ([0.535827,-0.849237,-1.85086,-2.52992,-3.21112,-3.79056,-5.08809],'cal/mol/K','+|-',[3,4.40319,4.56069,4.39089,3.50464,3,3]),
        H298 = (81.5708,'kcal/mol','+|-',9.32283),
        S298 = (1.83909,'cal/mol/K','+|-',7.67116),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 15,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r1 {1,S}
5   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.470804,-0.885065,-1.54959,-2.06146,-2.66441,-3.33486,-4.51949],'cal/mol/K','+|-',[3,5.28574,4.60737,3.8798,3,3,3]),
        H298 = (80.0648,'kcal/mol','+|-',5.2),
        S298 = (0.433884,'cal/mol/K','+|-',5.26283),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 16,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r1 {1,S}
5   C   ux r1 {3,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.863408,0.881541,-0.491456,-1.35095,-2.0341,-3.0728,-4.33085],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.4227,'kcal/mol','+|-',5.2),
        S298 = (-1.48193,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1C=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {3,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.75714,-6.65719,-6.66543,-6.37222,-5.62915,-5.08672,-5.08307],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.6887,'kcal/mol','+|-',5.2),
        S298 = (5.9612,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CCO[CH]C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 18,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R",
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
        Cpdata = ([-0.125286,-0.181383,-0.836515,-1.43351,-2.2462,-3.08823,-4.40033],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.1026,'kcal/mol','+|-',5.2),
        S298 = (-0.225892,'cal/mol/K','+|-',3.05086),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 19,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C",
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
    index = 20,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C",
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
        Cpdata = ([-0.319095,-0.512593,-1.01195,-1.59419,-2.52122,-3.26599,-4.48164],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (79.6482,'kcal/mol','+|-',2.4),
        S298 = (0.437887,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 21,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C",
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
        Cpdata = ([0.628717,-0.798053,-2.28124,-3.19913,-3.99214,-4.44157,-5.90037],'cal/mol/K','+|-',[3.3091,3.82127,5.23939,5.47254,4.38717,3.38213,3.09502]),
        H298 = (83.9957,'kcal/mol','+|-',15.137),
        S298 = (3.84653,'cal/mol/K','+|-',9.69868),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 22,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R",
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
        Cpdata = ([0.94867,-1.37402,-3.51419,-4.60941,-5.22083,-5.39339,-6.97244],'cal/mol/K','+|-',[4.34773,4.74067,5.44964,5.27017,3.82221,3,3]),
        H298 = (89.0399,'kcal/mol','+|-',16.0777),
        S298 = (6.05608,'cal/mol/K','+|-',10.3122),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 23,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_Sp-7R!H-6R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   O u0 r1 {1,S}
5   O u0 {3,S} {6,S}
6   C u0 {5,S} {7,S}
7   C ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.14298,-2.7399,-5.06229,-6.07141,-6.10462,-5.93637,-7.22421],'cal/mol/K','+|-',[3.03393,3,3,3,3.23616,3.16924,3]),
        H298 = (93.1892,'kcal/mol','+|-',10.1873),
        S298 = (8.83283,'cal/mol/K','+|-',5.25684),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 24,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   O   u0 r1 {1,S} {8,[S,D,T,B,Q]}
5   O   u0 r1 {3,S} {6,S}
6   C   u0 r1 {5,S} {7,S}
7   C   ux {6,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.929675,-2.88681,-5.54686,-6.80031,-7.24877,-7.05686,-7.70859],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.791,'kcal/mol','+|-',5.2),
        S298 = (10.6914,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=COCC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 25,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r1 {1,S}
5   O ux r1 {3,S} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]} {7,[B,D,T,Q]}
7   C u0 {6,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.13197,1.35774,-0.417992,-1.68539,-3.45327,-4.30743,-6.46891],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.7413,'kcal/mol','+|-',5.2),
        S298 = (0.502589,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=COC=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 26,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing",
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
        Cpdata = ([0.642743,-0.169251,-0.937739,-1.44246,-2.22471,-2.7983,-3.67895],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.2061,'kcal/mol','+|-',11.046),
        S298 = (-0.474105,'cal/mol/K','+|-',6.63986),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 27,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r0 {1,S}
5   C   ux {3,S} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.623274,-0.0552647,-0.712663,-1.14209,-1.93442,-2.58791,-3.48747],'cal/mol/K','+|-',[3.00495,3,3,3,3,3,3]),
        H298 = (70.219,'kcal/mol','+|-',5.2),
        S298 = (-1.33261,'cal/mol/K','+|-',6.96212),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 28,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-4O-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r0 {1,S} {8,S}
5   C ux {3,S} {6,[S,D,T,B,Q]}
6   C u0 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]}
8   N u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0221551,-0.48144,-1.00258,-1.5268,-2.4647,-3.16417,-4.24096],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (70.0553,'kcal/mol','+|-',2.91968),
        S298 = (0.471805,'cal/mol/K','+|-',3.88439),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 29,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-4O-R_Sp-6R!H-5R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r0 {1,S} {8,S}
5   C ux r1 {3,S} {6,S}
6   C u0 r1 {5,S} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]}
8   N u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.423055,-0.897117,-1.36153,-1.78808,-2.53641,-3.15916,-4.2701],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (71.0876,'kcal/mol','+|-',2.4),
        S298 = (1.84514,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(O[C]1C=CCC=C1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 30,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-4O-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,S}
4   O ux r0 {1,S} {8,S}
5   C ux r1 {3,S} {6,D}
6   C u0 r1 {5,D} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]}
8   N u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.378745,-0.0657631,-0.643626,-1.26552,-2.39298,-3.16918,-4.21182],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (69.0231,'kcal/mol','+|-',2.4),
        S298 = (-0.901534,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(O[C]1CC=CC=C1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 31,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,S}
4   O   ux r0 {1,S}
5   C   ux r1 {3,S} {6,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.42579,1.56609,0.062002,-0.519071,-1.20887,-1.97619,-1.64473],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (70.0318,'kcal/mol','+|-',5.2),
        S298 = (-5.22448,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CC=C[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 32,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-Sp-5R!H-3R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D} {5,[B,D,T,Q]}
4   O ux {1,S}
5   C ux {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.37352,-2.36644,-2.92204,-3.73633,-4.89729,-5.73609,-6.49921],'cal/mol/K','+|-',[7.20511,9.04007,8.96349,6.74691,3,3,3]),
        H298 = (57.1346,'kcal/mol','+|-',52.8268),
        S298 = (2.32971,'cal/mol/K','+|-',7.46128),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 33,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r1 {2,D} {5,[B,D,T,Q]}
4   O   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   C   ux r1 {3,[B,D,T,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 34,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.229748,-1.33549,-2.29609,-2.77416,-3.32579,-3.78037,-4.55991],'cal/mol/K','+|-',[3.18885,3.74331,3.71234,3.3216,3,3,3]),
        H298 = (79.6625,'kcal/mol','+|-',14.0633),
        S298 = (-0.512322,'cal/mol/K','+|-',7.91969),
    ),
    shortDesc = """Radical correction fitted to 140 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 35,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.658996,-3.16419,-4.02547,-4.33764,-4.51538,-4.66668,-5.10392],'cal/mol/K','+|-',[3,5.66062,5.73167,5.21007,3.87655,3,3]),
        H298 = (77.281,'kcal/mol','+|-',18.8639),
        S298 = (1.40624,'cal/mol/K','+|-',8.66621),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 36,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux {1,S} {6,D}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.512825,-2.82263,-3.65841,-4.09876,-4.48334,-4.73084,-5.43486],'cal/mol/K','+|-',[3.20325,4.86053,4.88519,4.45495,3.48506,3,3]),
        H298 = (74.4024,'kcal/mol','+|-',22.2485),
        S298 = (1.80466,'cal/mol/K','+|-',6.89288),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 37,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux {1,S} {6,D}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.771367,-1.86361,-2.76153,-3.36289,-4.07806,-4.57838,-5.51797],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (70.8676,'kcal/mol','+|-',15.1992),
        S298 = (0.48827,'cal/mol/K','+|-',4.51279),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 38,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D} {5,S}
3   C u0 r1 {2,D} {7,S}
4   C u0 {1,S} {6,D}
5   C u0 {2,S}
6   C ux {4,D}
7   C u0 {3,S} {8,D}
8   C ux {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.669214,-1.87155,-2.96184,-3.73099,-4.53498,-4.91355,-5.69455],'cal/mol/K','+|-',[3.28913,3,3,3,3,3,3]),
        H298 = (64.1772,'kcal/mol','+|-',10.9934),
        S298 = (-0.385906,'cal/mol/K','+|-',5.0867),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 39,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R_5C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D} {5,S}
3   C u0 r1 {2,D} {7,S}
4   C u0 {1,S} {6,D}
5   C u0 r1 {2,S}
6   C ux {4,D}
7   C u0 {3,S} {8,D}
8   C ux {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.335767,-1.63178,-3.21047,-4.32786,-5.25513,-5.5071,-6.29394],'cal/mol/K','+|-',[4.01,3,3,3,3,3.82494,3.81493]),
        H298 = (68.6811,'kcal/mol','+|-',5.2),
        S298 = (-2.54913,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 40,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R_5C-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {9,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D} {5,S}
3   C   u0 r1 {2,D} {7,S}
4   C   u0 r1 {1,S} {6,D}
5   C   u0 r1 {2,S}
6   C   ux r1 {4,D}
7   C   u0 r1 {3,S} {8,D}
8   C   ux r1 {7,D}
9   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08198,-2.19324,-3.58607,-4.19595,-4.26333,-4.15478,-4.94516],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (67.7511,'kcal/mol','+|-',5.2),
        S298 = (-2.31703,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=CCC([C]2C=CCCC2)=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 41,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R_N-5C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D} {5,S}
3   C u0 r1 {2,D} {7,S}
4   C u0 {1,S} {6,D}
5   C u0 r0 {2,S}
6   C ux {4,D}
7   C u0 {3,S} {8,D}
8   C ux {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6742,-2.11132,-2.71322,-3.13412,-3.81484,-4.32,-5.09516],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (59.6734,'kcal/mol','+|-',5.57624),
        S298 = (1.77732,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 42,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R_N-5C-inRing_6R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,S}
3   C u0 r1 {2,D} {7,S}
4   C u0 r1 {1,S} {6,D}
5   C u0 r0 {2,S}
6   C ux r1 {4,D}
7   C u0 r1 {3,S} {8,D}
8   C ux {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5102,-2.16832,-2.82522,-3.16012,-3.74134,-4.24,-5.11916],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (61.6449,'kcal/mol','+|-',5.2),
        S298 = (2.31582,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C(C)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 43,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R_N-5C-inRing_N-6R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,S}
3   C u0 r1 {2,D} {7,S}
4   C u0 r1 {1,S} {6,D}
5   C u0 r0 {2,S}
6   C ux r0 {4,D}
7   C u0 r1 {3,S} {8,D}
8   C ux {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8382,-2.05432,-2.60122,-3.10812,-3.88834,-4.4,-5.07116],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (57.7019,'kcal/mol','+|-',5.2),
        S298 = (1.23882,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C(C)=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 44,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux r1 {1,S} {6,D}
5   C   ux r0 {2,[S,D,T,B,Q]}
6   R!H ux {4,D}
7   R!H ux {1,[S,D,T,B,Q]}
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
    index = 45,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D}
4   C ux {1,S} {6,D}
5   O ux {2,[S,D,T,B,Q]}
6   C u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.42439,-6.29908,-6.9096,-6.76627,-5.95248,-5.28353,-5.13358],'cal/mol/K','+|-',[6.30256,7.15324,7.43145,7.03098,5.50844,4.05086,3]),
        H298 = (91.5362,'kcal/mol','+|-',11.4572),
        S298 = (6.57659,'cal/mol/K','+|-',5.07145),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 46,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_N-5R!H->C_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux r1 {1,S} {6,D}
5   O   ux r0 {2,[S,D,T,B,Q]}
6   C   u0 r1 {4,D} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.65268,-8.82813,-9.53701,-9.2521,-7.90001,-6.71573,-5.61254],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.4855,'kcal/mol','+|-',5.2),
        S298 = (8.36961,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CCOC=C[CH]1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 47,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux {1,S} {6,[S,T,Q,B]}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.84549,-3.59998,-4.4938,-4.64242,-4.55625,-4.58481,-4.68168],'cal/mol/K','+|-',[3,7.01158,7.11828,6.51722,4.73107,3.17128,3]),
        H298 = (80.7536,'kcal/mol','+|-',13.5261),
        S298 = (0.897896,'cal/mol/K','+|-',11.293),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 48,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux {1,S} {6,[S,T,Q,B]}
5   R!H ux {2,[S,D,T,B,Q]}
6   R!H ux {4,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.818731,-4.6287,-5.7467,-5.79235,-5.35529,-5.12466,-4.76998],'cal/mol/K','+|-',[3,7.41608,6.99766,6.39864,4.74514,3.16912,3]),
        H298 = (85.6441,'kcal/mol','+|-',8.30027),
        S298 = (0.601082,'cal/mol/K','+|-',13.6192),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 49,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux {1,S} {6,[S,T,Q,B]}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H ux {4,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,S}
8   R!H ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2172,-2.99277,-4.19143,-4.36502,-4.29437,-4.42155,-4.37258],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.8017,'kcal/mol','+|-',5.2),
        S298 = (-2.43641,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 50,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C_8R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux {1,S} {6,[S,T,Q,B]}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H ux {4,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,S}
8   C   ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.02078,-2.79524,-4.03265,-4.29094,-4.27418,-4.47349,-4.71332],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.6095,'kcal/mol','+|-',5.2),
        S298 = (-2.15932,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 51,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C_8R!H->C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C ux r1 {2,D}
4   C ux {1,S} {6,S}
5   C ux {2,[S,D,T,B,Q]}
6   C u0 {4,S} {7,[S,D,T,B,Q]}
7   C u0 {6,[S,D,T,B,Q]} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.42508,-2.386,-3.8157,-4.14297,-4.26444,-4.61697,-5.22003],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.3107,'kcal/mol','+|-',5.2),
        S298 = (-2.08528,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 52,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C_8R!H->C_6R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D} {9,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {6,S}
5   C   ux {2,[S,D,T,B,Q]}
6   C   u0 {4,S} {7,[S,D,T,B,Q]}
7   C   u0 {6,[S,D,T,B,Q]} {8,S}
8   C   ux r0 {7,S}
9   R!H ux {3,[S,D,T,B,Q]}
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
    index = 53,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C_8R!H->C_N-6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D} {5,S}
3   C   u0 r1 {2,D}
4   C   u0 r1 {1,S} {6,[S,T,Q,B]}
5   C   u0 r0 {2,S}
6   O   ux {4,[S,T,Q,B]} {7,S}
7   R!H ux {6,S} {8,S}
8   C   u0 {7,S}
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
    index = 54,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C_N-8R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,D}
4   C   ux r1 {1,S} {6,S}
5   C   ux {2,[S,D,T,B,Q]}
6   R!H u0 {4,S} {7,[S,D,T,B,Q]}
7   R!H u0 {6,[S,D,T,B,Q]} {8,S}
8   O   ux r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.80645,-3.58537,-4.66777,-4.58725,-4.35496,-4.26574,-3.35036],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.3783,'kcal/mol','+|-',5.2),
        S298 = (-3.26766,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1C=C(C)[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 55,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D} {5,S}
3   C   u0 r1 {2,D}
4   C   u0 r1 {1,S} {6,[S,T,Q,B]}
5   O   u0 r0 {2,S}
6   R!H ux {4,[S,T,Q,B]} {7,S}
7   R!H ux {6,S} {8,[S,D,T,B,Q]}
8   R!H u0 {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.775149,-11.1724,-11.9678,-11.5017,-9.59895,-7.93713,-6.35955],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.0134,'kcal/mol','+|-',5.2),
        S298 = (12.751,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=CC=COC[CH]1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 56,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.3245,-1.14551,-2.11745,-2.61395,-3.20537,-3.68831,-4.50251],'cal/mol/K','+|-',[3.20011,3.31527,3.29038,3,3,3,3]),
        H298 = (79.8375,'kcal/mol','+|-',13.5771),
        S298 = (-0.745061,'cal/mol/K','+|-',7.73325),
    ),
    shortDesc = """Radical correction fitted to 125 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 57,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R",
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
        Cpdata = ([0.326081,-1.1555,-2.13284,-2.62812,-3.21589,-3.69573,-4.50577],'cal/mol/K','+|-',[3.20988,3.31578,3.27705,3,3,3,3]),
        H298 = (79.8202,'kcal/mol','+|-',13.5961),
        S298 = (-0.729955,'cal/mol/K','+|-',7.74781),
    ),
    shortDesc = """Radical correction fitted to 124 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 58,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C",
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
        Cpdata = ([0.738839,-0.511753,-1.58322,-2.1729,-2.88755,-3.46783,-4.33295],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.0492,'kcal/mol','+|-',7.38929),
        S298 = (-0.516343,'cal/mol/K','+|-',7.02362),
    ),
    shortDesc = """Radical correction fitted to 48 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 59,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C",
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
        Cpdata = ([0.85043,-0.485943,-1.60055,-2.19629,-2.92014,-3.50867,-4.25563],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.2816,'kcal/mol','+|-',6.93178),
        S298 = (-0.810801,'cal/mol/K','+|-',6.79637),
    ),
    shortDesc = """Radical correction fitted to 43 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 60,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C",
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
        Cpdata = ([0.896598,-0.457027,-1.59486,-2.19638,-2.92542,-3.51769,-4.23794],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.056,'kcal/mol','+|-',6.49181),
        S298 = (-1.28814,'cal/mol/K','+|-',5.68595),
    ),
    shortDesc = """Radical correction fitted to 41 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 61,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R",
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
        Cpdata = ([1.12581,-0.553501,-1.64045,-2.06068,-2.25524,-2.32148,-2.891],'cal/mol/K','+|-',[3.82224,3,3,3,3,3,3]),
        H298 = (81.1378,'kcal/mol','+|-',5.2),
        S298 = (-1.79947,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 62,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {6,S}
4   C   ux r1 {1,S} {5,S}
5   C   u0 r1 {3,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
6   R!H u0 r0 {3,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.234443,-1.27439,-1.86586,-1.85536,-1.68146,-1.925,-2.78106],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.3671,'kcal/mol','+|-',5.2),
        S298 = (-2.16953,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C[CH]C=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 63,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S}
6   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.301057,-1.44643,-2.50607,-2.99951,-3.27252,-3.33861,-3.76749],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.1567,'kcal/mol','+|-',5.2),
        S298 = (-1.33749,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 64,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S}
6   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.31082,1.06032,-0.549418,-1.32718,-1.81173,-1.70082,-2.12444],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.8896,'kcal/mol','+|-',5.2),
        S298 = (-1.89138,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=C[CH]CC1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 65,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97578,-1.82663,-1.82665,-2.18309,-3.09893,-3.51559,-3.78306],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (81.9789,'kcal/mol','+|-',2.4),
        S298 = (0.22932,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 66,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R",
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
        Cpdata = ([1.24311,-0.0913154,-1.25851,-1.93041,-2.74787,-3.46145,-4.27506],'cal/mol/K','+|-',[3.01608,3,3.09487,3,3,3,3]),
        H298 = (81.6359,'kcal/mol','+|-',7.68923),
        S298 = (-0.984273,'cal/mol/K','+|-',6.32901),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 67,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {4,S}
6   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.29422,-0.271951,-1.54827,-2.19086,-2.8952,-3.51161,-4.29034],'cal/mol/K','+|-',[3,3,3.13613,3,3,3,3]),
        H298 = (83.8468,'kcal/mol','+|-',5.2),
        S298 = (-1.09283,'cal/mol/K','+|-',6.72514),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 68,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {4,S}
6   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.08999,-0.121341,-1.26097,-1.93078,-2.62809,-3.03732,-4.07799],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.2544,'kcal/mol','+|-',5.2),
        S298 = (0.0184807,'cal/mol/K','+|-',4.63374),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 69,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {4,S}
6   C ux {4,S} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2109,-0.202704,-1.4772,-2.16009,-2.75082,-3.03877,-4.01328],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.2596,'kcal/mol','+|-',5.2),
        S298 = (-0.836196,'cal/mol/K','+|-',3.70233),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 70,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_Int-8R!H-5C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S} {8,[S,D,T,B,Q]}
6   C ux {4,S} {7,S}
7   C u0 {6,S} {8,S}
8   C ux {5,[S,D,T,B,Q]} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0242276,-0.216524,-0.737919,-1.36653,-2.35646,-3.14297,-4.41368],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.5628,'kcal/mol','+|-',2.4),
        S298 = (0.990043,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 71,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {4,S}
6   C ux r1 {4,S} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.765,-0.290507,-2.00605,-2.70129,-2.97094,-2.95531,-3.73471],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.9331,'kcal/mol','+|-',5.2),
        S298 = (-1.58727,'cal/mol/K','+|-',3.48467),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 72,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {4,S}
6   C ux r1 {4,S} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,S}
8   C ux {7,S} {9,D}
9   C ux {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.77351,-0.388711,-2.13402,-2.8368,-3.04629,-3.03391,-3.70938],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.8723,'kcal/mol','+|-',5.2),
        S298 = (-2.08195,'cal/mol/K','+|-',3.51304),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 73,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {4,S}
6   C ux r1 {4,S} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]} {8,S}
8   C ux {7,S} {9,D}
9   C u0 {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.24924,-0.351232,-1.95584,-2.70944,-3.13289,-3.06485,-4.12705],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.7561,'kcal/mol','+|-',5.2),
        S298 = (-1.07123,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 74,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing_Sp-7R!H-6C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S}
6   C ux r1 {4,S} {7,S}
7   C ux r1 {6,S} {8,S}
8   C ux r1 {7,S} {9,D}
9   C u0 r1 {8,D}
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
    index = 75,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing_N-Sp-7R!H-6C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S}
6   C ux r1 {4,S} {7,D}
7   C ux r1 {6,D} {8,S}
8   C ux r1 {7,S} {9,D}
9   C u0 r1 {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.08268,-0.530012,-2.13414,-2.84481,-3.21657,-3.14449,-4.1028],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.2097,'kcal/mol','+|-',5.2),
        S298 = (-1.2151,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1C1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 76,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_N-7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {6,S}
5   C u0 r1 {3,S} {4,S}
6   C u0 r1 {4,S} {7,[S,D,T,B,Q]}
7   C u0 r0 {6,[S,D,T,B,Q]} {8,S}
8   C u0 {7,S} {9,D}
9   C ux {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.82204,-0.463668,-2.49039,-3.09151,-2.87308,-2.97203,-2.87403],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.1047,'kcal/mol','+|-',5.2),
        S298 = (-4.10339,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1(C2[CH]C=CC2)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 77,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S}
6   C ux r1 {4,S} {7,S}
7   C ux r1 {6,S} {8,S}
8   C ux r1 {7,S} {9,[S,T,Q,B]}
9   C u0 r1 {8,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.73947,0.00410225,-1.62213,-2.29475,-2.74488,-2.71954,-3.81072],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.1154,'kcal/mol','+|-',5.2),
        S298 = (-0.103238,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 78,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S}
6   C ux r0 {4,S} {7,S}
7   C ux {6,S} {8,S}
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
    index = 79,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_N-Sp-8R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S} {6,S}
5   C u0 r1 {3,S} {4,S}
6   C u0 {4,S} {7,S}
7   C ux {6,S} {8,[B,D,T,Q]}
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
    index = 80,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {4,S}
6   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.50396,-0.426633,-1.84333,-2.45798,-3.16953,-3.99872,-4.50842],'cal/mol/K','+|-',[3.03636,4.17572,4.28731,3.74525,3,3,3]),
        H298 = (84.5757,'kcal/mol','+|-',5.2),
        S298 = (-2.23418,'cal/mol/K','+|-',8.07025),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 81,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r1 {1,S} {5,S} {6,S}
5   C   u0 r1 {3,S} {4,S} {7,[S,D,T,B,Q]}
6   O   u0 r0 {4,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.42377,3.30047,1.73726,0.799,-0.778669,-2.12191,-3.56769],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.713,'kcal/mol','+|-',5.2),
        S298 = (-5.19574,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=C[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 82,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {4,S}
6   O   ux {4,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C   ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.26037,-0.818633,-2.26075,-2.8262,-3.42897,-4.17923,-4.53028],'cal/mol/K','+|-',[3,3.5863,3.88528,3.29678,3,3,3]),
        H298 = (84.7864,'kcal/mol','+|-',5.2),
        S298 = (-2.50578,'cal/mol/K','+|-',8.08346),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 83,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux {1,S} {5,S} {6,S}
5    C ux {3,[S,D,T,B,Q]} {4,S}
6    O ux {4,S} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]}
10   C ux {8,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.576882,-1.99874,-3.51552,-3.75303,-4.01681,-4.73213,-4.13664],'cal/mol/K','+|-',[3.31372,4.16432,3.95253,3,3,3,3]),
        H298 = (84.8637,'kcal/mol','+|-',5.2),
        S298 = (-6.0086,'cal/mol/K','+|-',4.05898),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 84,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,S}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,S} {7,S}
7    O u0 r0 {6,S} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,S} {10,[S,D,T,B,Q]}
9    C u0 {8,S}
10   C ux {8,[S,D,T,B,Q]} {11,S}
11   C u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.400854,-3.45057,-5.05188,-4.93121,-4.59481,-5.21671,-4.24658],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0393,'kcal/mol','+|-',5.2),
        S298 = (-3.70159,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC1OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 85,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux {1,S} {5,S} {6,S}
5    C ux {3,[S,D,T,B,Q]} {4,S}
6    O ux {4,S} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.06575,-1.27283,-2.74734,-3.16394,-3.72781,-4.48984,-4.08167],'cal/mol/K','+|-',[4.02812,4.69428,4.13311,3,3,3,3]),
        H298 = (85.2759,'kcal/mol','+|-',5.2),
        S298 = (-7.1621,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 86,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,S} {6,S}
5    C ux r1 {3,[S,D,T,B,Q]} {4,S}
6    O ux {4,S} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,S}
8    C u0 r1 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
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
    index = 87,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_N-8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,S} {6,S}
5    C ux r1 {3,[S,D,T,B,Q]} {4,S}
6    O ux {4,S} {7,[S,D,T,B,Q]}
7    O ux {6,[S,D,T,B,Q]} {8,S}
8    C u0 r0 {7,S} {9,[S,D,T,B,Q]} {10,S}
9    C ux {8,[S,D,T,B,Q]}
10   C u0 {8,S} {11,[B,D,T,Q]}
11   C ux {10,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.4899,0.386854,-1.28607,-2.11484,-3.3425,-4.15722,-4.11409],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2474,'kcal/mol','+|-',5.2),
        S298 = (-7.51865,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(C)OOC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 88,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S} {6,S}
5   C u0 {3,S} {4,S}
6   O u0 {4,S} {7,S}
7   O u0 {6,S} {8,S}
8   C u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.54817,-0.881245,-2.65959,-3.55606,-4.27181,-4.93326,-5.2973],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0567,'kcal/mol','+|-',5.2),
        S298 = (-2.5885,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 89,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_7R!H->O_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,S}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,D}
10   C u0 r0 {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.58947,-0.779774,-2.55929,-3.47963,-4.26917,-4.84449,-5.07804],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0602,'kcal/mol','+|-',5.2),
        S298 = (-2.76641,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 90,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_7R!H->O_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C u0 r1 {1,S} {3,D}
3    C u0 r1 {2,D} {5,S}
4    C u0 r1 {1,S} {5,S} {6,S}
5    C u0 r1 {3,S} {4,S}
6    O u0 r0 {4,S} {7,S}
7    O u0 r0 {6,S} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,S}
10   C u0 r0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.50687,-0.982717,-2.75988,-3.6325,-4.27445,-5.02202,-5.51656],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0532,'kcal/mol','+|-',5.2),
        S298 = (-2.4106,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 91,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_N-7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S}
6   O ux {4,S} {7,[S,D,T,B,Q]}
7   N ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux r0 {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.91587,0.810499,-0.233194,-0.94166,-1.89599,-2.7718,-4.37334],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (85.0478,'kcal/mol','+|-',2.4),
        S298 = (2.23817,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1CC=C[CH]1)CC - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 92,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S} {6,[B,D,T,Q]}
5   C   ux {3,[S,D,T,B,Q]} {4,S}
6   R!H ux {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.11535,0.360274,-0.53411,-1.27927,-2.37953,-3.33607,-4.23689],'cal/mol/K','+|-',[4.58054,3.4211,3,3,3,3,3]),
        H298 = (76.981,'kcal/mol','+|-',6.77964),
        S298 = (-0.71288,'cal/mol/K','+|-',5.96271),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 93,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,S} {6,D}
5   C u0 {3,S} {4,S}
6   C u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.887125,0.65865,0.0157203,-0.703236,-1.87056,-2.88459,-4.37584],'cal/mol/K','+|-',[5.11638,4.4762,3.65673,3.12166,3,3,3]),
        H298 = (74.4836,'kcal/mol','+|-',5.2),
        S298 = (-2.35407,'cal/mol/K','+|-',5.03898),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 94,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_6R!H->C_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r1 {1,S} {5,S} {6,D}
5   C   u0 r1 {3,S} {4,S} {7,[S,D,T,B,Q]}
6   C   u0 {4,D}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.39177,2.84991,1.80582,0.824928,-0.727889,-2.23408,-4.1998],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.5398,'kcal/mol','+|-',5.2),
        S298 = (-4.82083,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 95,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S} {6,[B,D,T,Q]}
5   C ux {3,[S,D,T,B,Q]} {4,S}
6   O ux {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.28987,0.132105,-0.954568,-1.71977,-2.76873,-3.68131,-4.13063],'cal/mol/K','+|-',[5.66977,3.80704,3,3,3,3,3]),
        H298 = (79.1054,'kcal/mol','+|-',6.38312),
        S298 = (0.54215,'cal/mol/K','+|-',6.44426),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 96,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_N-6R!H->C_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {5,S} {6,[B,D,T,Q]}
5   C   ux {3,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
6   O   ux {4,[B,D,T,Q]}
7   R!H u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.44442,1.23975,-0.582896,-1.62744,-2.86537,-4.01744,-3.69785],'cal/mol/K','+|-',[3.61321,4.35582,4.12189,3.8353,3,3,3]),
        H298 = (78.6251,'kcal/mol','+|-',11.1278),
        S298 = (1.55719,'cal/mol/K','+|-',9.5873),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 97,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_N-6R!H->C_Ext-5C-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S} {6,[B,D,T,Q]}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
6   O ux r0 {4,[B,D,T,Q]}
7   C u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.16696,-0.300265,-2.0402,-2.98343,-3.89219,-4.87926,-4.18068],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.6909,'kcal/mol','+|-',5.2),
        S298 = (4.94682,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 98,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_N-6R!H->C_Ext-5C-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      ux r1 {1,S} {3,D}
3   C                      ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C                      ux r1 {1,S} {5,S} {6,[B,D,T,Q]}
5   C                      ux r1 {3,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
6   O                      ux r0 {4,[B,D,T,Q]}
7   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.72188,2.77977,0.874412,-0.271459,-1.83855,-3.15562,-3.21502],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.5594,'kcal/mol','+|-',5.2),
        S298 = (-1.83243,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]C=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 99,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R",
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
        Cpdata = ([0.818825,-0.799883,-2.10737,-2.67092,-3.31265,-3.82274,-4.43144],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.4532,'kcal/mol','+|-',6.10683),
        S298 = (-1.79161,'cal/mol/K','+|-',5.88853),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 100,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C",
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
        Cpdata = ([1.20012,-0.804667,-2.34993,-2.83979,-3.32112,-3.76643,-4.17113],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.9848,'kcal/mol','+|-',5.2),
        S298 = (-2.24578,'cal/mol/K','+|-',6.53227),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 101,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   O ux {5,S} {7,S}
7   O ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2686,-1.4834,-3.24512,-3.56979,-4.10691,-4.85083,-4.3663],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.6876,'kcal/mol','+|-',5.2),
        S298 = (-4.37796,'cal/mol/K','+|-',7.33202),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 102,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   O ux {5,S} {7,S}
7   O ux {6,S} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.37113,-1.52341,-3.37437,-3.67461,-4.18013,-4.89179,-4.25134],'cal/mol/K','+|-',[3,3.19217,3,3,3,3,3]),
        H298 = (84.7119,'kcal/mol','+|-',5.2),
        S298 = (-5.60081,'cal/mol/K','+|-',4.72625),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 103,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   ux {1,S} {3,D}
3    C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C   ux {1,S} {5,S}
5    C   ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O   ux {5,S} {7,S}
7    O   ux {6,S} {8,[S,D,T,B,Q]}
8    C   ux {7,[S,D,T,B,Q]} {9,S}
9    C   u0 {8,S} {10,S}
10   R!H ux {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.30423,-1.70935,-3.65824,-4.01481,-4.44079,-5.10696,-4.5975],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2219,'kcal/mol','+|-',5.2),
        S298 = (-3.91978,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 104,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,S}
5    C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O ux r0 {5,S} {7,S}
7    O ux r0 {6,S} {8,[S,D,T,B,Q]}
8    C ux r1 {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,S}
10   C ux {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00488226,-3.42224,-5.2531,-4.93157,-4.65613,-5.29592,-3.89702],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2103,'kcal/mol','+|-',5.2),
        S298 = (-4.66184,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(OOC2C=CCCC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 105,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   ux {1,S} {3,D}
3    C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C   ux {1,S} {5,S}
5    C   ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O   ux {5,S} {7,S}
7    O   ux {6,S} {8,[S,D,T,B,Q]}
8    C   ux r0 {7,[S,D,T,B,Q]} {9,S}
9    C   u0 {8,S} {10,S}
10   R!H ux {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.95391,-0.852909,-2.86081,-3.55643,-4.33313,-5.01247,-4.94774],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2277,'kcal/mol','+|-',5.2),
        S298 = (-3.54875,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 106,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing_Ext-9R!H-R_Sp-11R!H-9R!H",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   ux r1 {1,S} {3,D}
3    C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C   ux r1 {1,S} {5,S}
5    C   ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O   ux r0 {5,S} {7,S}
7    O   ux r0 {6,S} {8,[S,D,T,B,Q]}
8    C   ux r0 {7,[S,D,T,B,Q]} {9,S}
9    C   u0 {8,S} {10,S} {11,S}
10   R!H ux {9,S}
11   R!H ux {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.91261,-0.95438,-2.96111,-3.63286,-4.33576,-5.10124,-5.167],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2242,'kcal/mol','+|-',5.2),
        S298 = (-3.37085,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 107,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing_Ext-9R!H-R_N-Sp-11R!H-9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,S}
5    C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O ux r0 {5,S} {7,S}
7    O ux r0 {6,S} {8,[S,D,T,B,Q]}
8    C ux r0 {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,S} {11,[B,D,T,Q]}
10   C ux {9,S}
11   C u0 r0 {9,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.99521,-0.751437,-2.76052,-3.47999,-4.33049,-4.9237,-4.72848],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.2312,'kcal/mol','+|-',5.2),
        S298 = (-3.72665,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 108,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux {1,S} {5,S}
5    C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O ux {5,S} {7,S}
7    O ux {6,S} {8,[S,D,T,B,Q]}
8    C ux {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,[B,D,T,Q]}
10   C ux {9,[B,D,T,Q]}
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
    index = 109,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H_8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,S}
5    C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O ux r0 {5,S} {7,S}
7    O ux r0 {6,S} {8,[S,D,T,B,Q]}
8    C ux r1 {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,[B,D,T,Q]}
10   C ux {9,[B,D,T,Q]}
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
    index = 110,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H_N-8R!H-inRing",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C ux r1 {1,S} {5,S}
5    C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6    O ux r0 {5,S} {7,S}
7    O ux r0 {6,S} {8,[S,D,T,B,Q]}
8    C ux r0 {7,[S,D,T,B,Q]} {9,S}
9    C u0 {8,S} {10,[B,D,T,Q]}
10   C ux {9,[B,D,T,Q]}
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
    index = 111,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      ux {1,S} {3,D}
3   C                      ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C                      ux {1,S} {5,S}
5   C                      ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   R!H                    ux {5,S} {7,[S,D,T,B,Q]}
7   [F,I,P,Br,Cl,C,Si,S,N] ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.15031,-0.311039,-1.69888,-2.30888,-2.74964,-2.97778,-4.02918],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.5905,'kcal/mol','+|-',5.2),
        S298 = (-0.695099,'cal/mol/K','+|-',3.7989),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 112,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      ux r1 {1,S} {3,D}
3   C                      ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C                      ux r1 {1,S} {5,S}
5   C                      ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6   R!H                    ux {5,S} {7,D}
7   [F,I,P,Br,Cl,C,Si,S,N] ux {6,D}
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
    index = 113,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      ux {1,S} {3,D}
3   C                      ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C                      ux {1,S} {5,S}
5   C                      ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   R!H                    ux {5,S} {7,S}
7   [F,I,P,Br,Cl,C,Si,S,N] ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.36654,-0.181526,-1.60298,-2.21426,-2.70731,-2.97548,-4.03972],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.6515,'kcal/mol','+|-',5.2),
        S298 = (-0.860617,'cal/mol/K','+|-',3.98637),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 114,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux {5,S} {7,S}
7   C ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.79281,-0.0491463,-1.75243,-2.41768,-2.86034,-2.9681,-3.92921],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.7168,'kcal/mol','+|-',5.2),
        S298 = (-1.80285,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 115,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux {5,S} {7,S}
7   C ux {6,S} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.91046,-0.113104,-1.82881,-2.43528,-2.85622,-2.95373,-3.76568],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.6662,'kcal/mol','+|-',5.2),
        S298 = (-1.76873,'cal/mol/K','+|-',3.45679),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 116,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi_6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux r1 {5,S} {7,S}
7   C ux {6,S} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.99243,-0.210673,-2.06335,-2.65344,-2.88906,-2.89226,-3.61202],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.5908,'kcal/mol','+|-',5.2),
        S298 = (-1.71133,'cal/mol/K','+|-',4.22433),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 117,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {5,S}
5   C ux {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux r1 {5,S} {7,S}
7   C ux {6,S} {8,S}
8   C ux {7,S} {9,S}
9   C u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.28075,-0.229783,-2.15626,-2.69313,-2.80898,-2.84578,-3.34238],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.86,'kcal/mol','+|-',5.2),
        S298 = (-2.10331,'cal/mol/K','+|-',5.65706),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 118,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_Ext-6C-R",
    group = 
"""
1  * C   u1 r1 {2,S} {4,S}
2    C   ux r1 {1,S} {3,D}
3    C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4    C   ux r1 {1,S} {5,S}
5    C   ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6    C   ux r1 {5,S} {7,S} {11,[S,D,T,B,Q]}
7    C   ux r1 {6,S} {8,S}
8    C   ux r1 {7,S} {9,S}
9    C   u0 r1 {8,S} {10,D}
10   C   u0 r1 {9,D}
11   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.82204,-0.463668,-2.59039,-3.09151,-2.87308,-2.97203,-2.87403],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.8547,'kcal/mol','+|-',5.2),
        S298 = (-4.10339,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1(C2C=C[CH]C2)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 119,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi_6C-inRing_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux r1 {5,S} {7,S}
7   C ux r1 {6,S} {8,S}
8   C ux r1 {7,S} {9,[B,D,T,Q]}
9   C u0 r1 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4158,-0.172453,-1.87754,-2.57408,-3.04922,-2.98521,-4.1513],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0524,'kcal/mol','+|-',5.2),
        S298 = (-0.927364,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(C2C=CC=CC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 120,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi_N-6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S} {5,S}
5   C ux r1 {3,[S,D,T,B,Q]} {4,S} {6,S}
6   C ux r0 {5,S} {7,S}
7   C ux {6,S} {8,S}
8   C ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.66452,0.179604,-1.12518,-1.78079,-2.7577,-3.13816,-4.22667],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.8923,'kcal/mol','+|-',5.2),
        S298 = (-1.94093,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)CC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 121,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_N-Sp-8R!H-7BrCClFINPSSi",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {3,S} {4,S} {6,S}
6   C u0 {5,S} {7,S}
7   C u0 {6,S} {8,[B,D,T,Q]}
8   C u0 {7,[B,D,T,Q]}
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
    index = 122,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,S}
4   C                      u0 r1 {1,S} {5,S}
5   C                      u0 r1 {3,S} {4,S} {6,S}
6   O                      u0 {5,S} {7,S}
7   [F,I,P,Br,Cl,C,Si,S,N] u0 {6,S}
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
    index = 123,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C",
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
        Cpdata = ([-0.169064,-0.787491,-1.47892,-2.23339,-3.2907,-3.96861,-5.1059],'cal/mol/K','+|-',[3,3,3.66283,4.5699,4.98007,4.42615,3.76713]),
        H298 = (79.9919,'kcal/mol','+|-',8.12545),
        S298 = (-0.614901,'cal/mol/K','+|-',3.22457),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 124,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_6R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {4,S} {6,[B,D,T,Q]}
6   R!H ux r1 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.313517,-2.71032,-4.55487,-6.07978,-7.48692,-7.69942,-8.28272],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.8211,'kcal/mol','+|-',5.2),
        S298 = (1.50877,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CC(=C2C=CCCC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 125,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 {1,S} {5,S}
5   C   u0 {3,S} {4,S} {6,D}
6   R!H u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.276305,-0.360196,-0.795382,-1.37864,-2.3582,-3.13955,-4.39994],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (80.6491,'kcal/mol','+|-',7.01334),
        S298 = (-1.08683,'cal/mol/K','+|-',2.50398),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 126,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {3,S} {4,S} {6,D}
6   C u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.198354,-0.215075,-0.64701,-1.25177,-2.26535,-3.07527,-4.37982],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (78.1695,'kcal/mol','+|-',2.4),
        S298 = (-1.97212,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 127,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 r1 {1,S} {5,S}
5   C u0 r1 {3,S} {4,S} {6,D}
6   O u0 r0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.354256,-0.505317,-0.943754,-1.5055,-2.45105,-3.20383,-4.42005],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.1287,'kcal/mol','+|-',2.4),
        S298 = (-0.201537,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=C[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 128,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {5,D}
5   C ux {3,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0904424,-0.961947,-1.69414,-2.19482,-2.83315,-3.36023,-4.54681],'cal/mol/K','+|-',[4.91148,5.83834,5.1846,4.17871,3,3,3]),
        H298 = (85.3697,'kcal/mol','+|-',17.047),
        S298 = (7.04699,'cal/mol/K','+|-',3.62269),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 129,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S} {6,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {5,D}
5   C   ux r1 {3,S} {4,D}
6   R!H ux {3,[S,D,T,B,Q]}
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
    index = 130,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C",
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
        Cpdata = ([-0.105535,-0.707042,-1.45212,-1.9959,-2.64094,-3.15881,-4.91806],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.4804,'kcal/mol','+|-',11.1053),
        S298 = (1.71172,'cal/mol/K','+|-',8.06027),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 131,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,S}
5   O   u0 r1 {3,[S,D,T,B,Q]} {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.852467,-0.487298,-1.73659,-2.44364,-3.19425,-3.7724,-5.31954],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.6042,'kcal/mol','+|-',5.2),
        S298 = (-1.60629,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]1C=COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 132,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   O   ux r1 {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.556283,-1.50424,-2.136,-2.59357,-2.89804,-2.80863,-5.81844],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0574,'kcal/mol','+|-',5.2),
        S298 = (8.6942,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1=C[CH]CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 133,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R",
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
        Cpdata = ([-0.40978,-0.878107,-1.55578,-2.05758,-2.67134,-3.19835,-4.86223],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.8875,'kcal/mol','+|-',21.6524),
        S298 = (1.97071,'cal/mol/K','+|-',8.39307),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 134,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R_Sp-6R!H-4C",
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
        Cpdata = ([0.290329,-0.638098,-1.80637,-2.29687,-2.41825,-2.63526,-5.59684],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.5094,'kcal/mol','+|-',5.2),
        S298 = (6.07942,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 135,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R_N-Sp-6R!H-4C",
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
        Cpdata = ([-0.72094,-0.984778,-1.4444,-1.95123,-2.78382,-3.44862,-4.53574],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (77.1989,'kcal/mol','+|-',2.4),
        S298 = (0.14462,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 136,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
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
        Cpdata = ([-0.281901,-1.90944,-2.53092,-2.86843,-3.25477,-3.61125,-4.48306],'cal/mol/K','+|-',[3.37926,3.76431,3.6419,3.2482,3,3,3]),
        H298 = (73.011,'kcal/mol','+|-',10.0636),
        S298 = (1.43242,'cal/mol/K','+|-',4.86268),
    ),
    shortDesc = """Radical correction fitted to 24 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 137,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R",
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
        Cpdata = ([-0.151247,-2.60777,-3.27367,-3.55842,-3.77774,-3.99411,-4.71079],'cal/mol/K','+|-',[4.39518,4.62296,4.35376,3.82006,3,3,3]),
        H298 = (71.6262,'kcal/mol','+|-',14.585),
        S298 = (1.8024,'cal/mol/K','+|-',5.81006),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 138,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C",
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
        Cpdata = ([0.0849428,-2.64517,-3.43734,-3.70562,-3.80513,-3.9501,-4.69224],'cal/mol/K','+|-',[4.58293,5.13602,4.77123,4.25429,3.06024,3,3]),
        H298 = (74.7465,'kcal/mol','+|-',7.63431),
        S298 = (2.0694,'cal/mol/K','+|-',6.70181),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 139,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Int-6R!H-4C",
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
    index = 140,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R",
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
        Cpdata = ([1.41916,-4.26929,-4.83594,-4.74312,-4.42999,-4.38808,-4.92379],'cal/mol/K','+|-',[6.43408,6.12046,5.12872,4.47617,3,3,3]),
        H298 = (72.3968,'kcal/mol','+|-',5.2),
        S298 = (5.44764,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 141,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R_6R!H-inRing",
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
        Cpdata = ([3.69395,-6.4332,-6.64922,-6.32569,-5.48423,-4.99455,-4.79723],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (71.4325,'kcal/mol','+|-',5.2),
        S298 = (4.5904,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 142,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R_N-6R!H-inRing",
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
        Cpdata = ([-0.855633,-2.10538,-3.02267,-3.16056,-3.37575,-3.78161,-5.05036],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.3611,'kcal/mol','+|-',5.2),
        S298 = (6.30489,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 143,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing",
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
        Cpdata = ([-0.16097,-2.92528,-3.91999,-4.32651,-4.39498,-4.43831,-4.98005],'cal/mol/K','+|-',[5.4869,5.78295,5.11867,4.26384,3,3,3]),
        H298 = (72.6836,'kcal/mol','+|-',5.2),
        S298 = (2.01043,'cal/mol/K','+|-',7.62087),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 144,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R",
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
        Cpdata = ([-0.532496,-2.1333,-3.2355,-3.76971,-4.03663,-4.22351,-4.90972],'cal/mol/K','+|-',[5.61639,3.88584,3.57671,3.08409,3,3,3]),
        H298 = (72.4238,'kcal/mol','+|-',5.2),
        S298 = (0.953515,'cal/mol/K','+|-',5.00542),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 145,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Ext-8R!H-R",
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
        Cpdata = ([1.56192,-1.63614,-3.70023,-4.55605,-4.98382,-4.90408,-5.43571],'cal/mol/K','+|-',[8.5529,5.59206,4.5137,3.53524,3,3,3]),
        H298 = (72.9205,'kcal/mol','+|-',5.2),
        S298 = (-1.60269,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 146,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Ext-8R!H-R_Ext-1R-R",
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
        Cpdata = ([4.58583,0.340947,-2.1044,-3.30616,-4.38431,-4.64338,-5.34625],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.26,'kcal/mol','+|-',5.2),
        S298 = (-2.52836,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CC=C(CC=CC)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 147,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Int-8R!H-1R_Ext-7R!H-R_Sp-9R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {7,S}
5   C u0 r1 {3,S} {6,D}
6   C u0 r1 {5,D} {8,S}
7   C u0 {4,S} {9,S}
8   C u0 r1 {6,S}
9   C u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.5777,-3.7656,-4.4514,-4.58546,-3.93676,-3.9511,-4.58432],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (72.1867,'kcal/mol','+|-',2.4),
        S298 = (3.45902,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CCC[C]1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 148,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Int-8R!H-1R_Ext-7R!H-R_N-Sp-9R!H-7R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S}
4   C u0 {1,S} {7,S}
5   C u0 r1 {3,S} {6,D}
6   C u0 r1 {5,D} {8,S}
7   C u0 {4,S} {9,[B,D,T,Q]}
8   C u0 r1 {6,S}
9   C u0 r0 {7,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.348996,-0.942898,-1.60649,-2.255,-3.29456,-3.89095,-4.76756],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (72.4492,'kcal/mol','+|-',2.4),
        S298 = (0.720194,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 149,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_N-6R!H-inRing",
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
        Cpdata = ([0.0571042,-0.626383,-1.19218,-1.55975,-2.29565,-3.0295,-4.45225],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (79.7027,'kcal/mol','+|-',2.4),
        S298 = (0.90487,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 150,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C",
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
        Cpdata = ([-0.65315,-2.52829,-2.92586,-3.24561,-3.71955,-4.08764,-4.75022],'cal/mol/K','+|-',[4.29919,3.92465,3.77455,3.1086,3,3,3]),
        H298 = (61.1819,'kcal/mol','+|-',10.4886),
        S298 = (1.23504,'cal/mol/K','+|-',3.86293),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 151,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing",
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
        Cpdata = ([-1.68451,-1.76047,-2.17653,-2.69202,-3.50257,-4.04188,-4.77987],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (57.5791,'kcal/mol','+|-',5.2),
        S298 = (0.317445,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 152,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing_Ext-5R!H-R",
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
    index = 153,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing_Ext-7R!H-R",
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
        Cpdata = ([-1.82845,-2.06764,-2.43909,-2.80256,-3.40275,-3.82578,-4.51612],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (57.8169,'kcal/mol','+|-',5.2),
        S298 = (-0.281388,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C1[CH]C=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 154,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing",
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
        Cpdata = ([0.378208,-3.2961,-3.67519,-3.7992,-3.93653,-4.1334,-4.72056],'cal/mol/K','+|-',[5.75999,5.50899,5.23801,4.42215,3,3,3]),
        H298 = (64.7846,'kcal/mol','+|-',10.911),
        S298 = (2.15264,'cal/mol/K','+|-',4.75938),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 155,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing_Ext-5R!H-R",
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
        Cpdata = ([3.69395,-6.4332,-6.64922,-6.32569,-5.48423,-4.99455,-4.79723],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (71.0825,'kcal/mol','+|-',5.2),
        S298 = (4.9004,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=C[CH]C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 156,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing_Ext-6R!H-R",
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
        Cpdata = ([-1.50045,-2.18164,-2.66309,-2.85456,-3.25575,-3.66578,-4.56412],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (61.7599,'kcal/mol','+|-',5.2),
        S298 = (0.795612,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C1C=C[CH]C=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 157,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1R-R",
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
        Cpdata = ([-0.368806,-1.0144,-1.67627,-2.23767,-3.10475,-3.70719,-4.53775],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (71.9674,'kcal/mol','+|-',2.4),
        S298 = (0.736208,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 158,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-5R!H-R",
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
        Cpdata = ([-0.899076,-1.27203,-1.63832,-1.99818,-2.68342,-3.30234,-4.46074],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (74.8945,'kcal/mol','+|-',2.4),
        S298 = (1.41328,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC[CH]C=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 159,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R",
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
        Cpdata = ([-0.805489,-1.36025,-1.76368,-2.06884,-2.5084,-2.88008,-3.88439],'cal/mol/K','+|-',[3.01444,3,3,3,3,3,3]),
        H298 = (74.7857,'kcal/mol','+|-',5.2),
        S298 = (2.48641,'cal/mol/K','+|-',7.21385),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 160,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_7R!H->C",
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
        Cpdata = ([-1.46134,-1.76886,-2.01059,-2.27006,-2.81847,-3.36392,-4.47925],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (74.7956,'kcal/mol','+|-',2.4),
        S298 = (4.05594,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=C[CH]CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 161,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,S} {7,S}
4   C                      u0 r1 {1,S}
5   C                      u0 r1 {3,S} {6,D}
6   C                      u0 r1 {5,D}
7   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {3,S}
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
    index = 162,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R",
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
        Cpdata = ([-0.157178,-1.10254,-1.771,-2.17463,-2.66405,-3.13658,-4.13168],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.3187,'kcal/mol','+|-',5.2),
        S298 = (0.281922,'cal/mol/K','+|-',3.8991),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 163,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C",
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
        Cpdata = ([-0.593909,-1.36887,-1.95928,-2.35906,-2.89857,-3.4028,-4.44728],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.555,'kcal/mol','+|-',5.2),
        S298 = (0.886099,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 164,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_Ext-7C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S}
5   C ux {3,[S,D,T,B,Q]} {6,D}
6   C ux {5,D} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.622971,-1.63279,-2.32273,-2.70767,-3.09275,-3.49419,-4.46083],'cal/mol/K','+|-',[3,3,3.43286,3.15803,3,3,3]),
        H298 = (74.6752,'kcal/mol','+|-',5.2),
        S298 = (0.707315,'cal/mol/K','+|-',3.52914),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 165,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C ux r1 {5,D} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   C u0 r0 {8,S}
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
    index = 166,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux r1 {1,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,D}
6   C ux r1 {5,D} {7,[S,D,T,B,Q]}
7   C ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,[B,D,T,Q]}
9   C u0 r0 {8,[B,D,T,Q]}
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
    index = 167,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,S}
4   C                      u0 r1 {1,S}
5   C                      u0 r1 {3,S} {6,D}
6   C                      u0 r1 {5,D} {7,S}
7   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {6,S}
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
    index = 168,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
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
        Cpdata = ([0.244011,-1.39396,-2.47608,-2.96323,-3.53404,-3.97993,-4.69776],'cal/mol/K','+|-',[3.29414,3.31351,3.34534,3,3,3,3]),
        H298 = (81.9756,'kcal/mol','+|-',15.2308),
        S298 = (-2.18074,'cal/mol/K','+|-',8.63872),
    ),
    shortDesc = """Radical correction fitted to 52 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 169,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O",
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
        Cpdata = ([-0.0856895,-3.12669,-4.08122,-4.01092,-3.9575,-4.21278,-4.21152],'cal/mol/K','+|-',[4.96523,3.44119,3.39595,3.37871,3.80092,3.88386,3]),
        H298 = (80.8019,'kcal/mol','+|-',7.22853),
        S298 = (-6.13166,'cal/mol/K','+|-',9.28569),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 170,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing",
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
        Cpdata = ([0.914966,-3.56142,-4.10919,-3.85995,-4.05261,-4.58965,-4.50763],'cal/mol/K','+|-',[7.16708,5.09149,4.85106,4.65339,5.05531,4.81808,3.10028]),
        H298 = (79.343,'kcal/mol','+|-',10.3138),
        S298 = (-3.5929,'cal/mol/K','+|-',12.3923),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 171,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C",
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
        Cpdata = ([0.801801,-4.39314,-4.82015,-4.35941,-4.13146,-4.51569,-4.15702],'cal/mol/K','+|-',[8.25517,4.01466,4.23059,4.71377,5.82315,5.55032,3.08827]),
        H298 = (80.271,'kcal/mol','+|-',10.9026),
        S298 = (-4.21729,'cal/mol/K','+|-',13.9414),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 172,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-3R!H-R",
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
    index = 173,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-1R-R",
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
        Cpdata = ([-2.53892,-2.76994,-3.34642,-2.55965,-1.88547,-2.32994,-2.76933],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.6488,'kcal/mol','+|-',5.2),
        S298 = (-9.9188,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C1=CC2CC[C]1COO2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 174,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-4C-R",
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
        Cpdata = ([4.66539,-5.84718,-6.4095,-6.18936,-6.45812,-6.75105,-5.44992],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.8788,'kcal/mol','+|-',5.2),
        S298 = (1.7541,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1[CH]C=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 175,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing",
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
        Cpdata = ([-0.800443,-2.81617,-4.06125,-4.11875,-3.88956,-3.94359,-4.00002],'cal/mol/K','+|-',[3,3,3,3,3.06546,3.37151,3]),
        H298 = (81.8439,'kcal/mol','+|-',5.2),
        S298 = (-7.94506,'cal/mol/K','+|-',4.34374),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 176,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R",
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
        Cpdata = ([-0.700811,-2.86716,-4.15805,-4.429,-4.79807,-5.06217,-5.05505],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0165,'kcal/mol','+|-',5.2),
        S298 = (-8.0914,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 177,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H",
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
        Cpdata = ([-1.72823,-3.67097,-4.61195,-4.45537,-4.14084,-4.29889,-4.04322],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.9904,'kcal/mol','+|-',5.2),
        S298 = (-8.93423,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1(C)C=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 178,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H",
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
        Cpdata = ([0.326603,-2.06335,-3.70416,-4.40262,-5.4553,-5.82545,-6.06689],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.0425,'kcal/mol','+|-',5.2),
        S298 = (-7.24857,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1(C)C=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 179,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing",
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
        Cpdata = ([-0.560156,-2.60244,-3.9274,-3.95751,-3.64299,-3.65341,-3.76567],'cal/mol/K','+|-',[3,3,3.17396,3.511,3.76787,3.9812,3]),
        H298 = (80.987,'kcal/mol','+|-',5.2),
        S298 = (-7.19419,'cal/mol/K','+|-',4.79373),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 180,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1R-R",
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
        Cpdata = ([0.0313433,-2.49885,-4.35468,-4.54692,-4.30128,-4.39572,-4.31876],'cal/mol/K','+|-',[3.1542,3,3,3,4.23934,4.96412,4.56542]),
        H298 = (80.0127,'kcal/mol','+|-',5.2),
        S298 = (-7.61462,'cal/mol/K','+|-',8.00016),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 181,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1R-R_Ext-7R!H-R_Ext-8R!H-R",
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
    index = 182,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-6O-R",
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
        Cpdata = ([-1.5068,-3.87368,-5.31831,-5.1841,-4.4715,-4.23825,-3.57459],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.3461,'kcal/mol','+|-',5.2),
        S298 = (-6.26032,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1CC[CH]C=C1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 183,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_N-5R!H-inRing",
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
        Cpdata = ([-1.96086,-3.56909,-4.40303,-4.14323,-3.05883,-2.86717,-2.82734],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.9269,'kcal/mol','+|-',5.2),
        S298 = (-10.6558,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOCC1=C[CH]CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 184,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O",
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
        Cpdata = ([0.32314,-0.978103,-2.09085,-2.71178,-3.4324,-3.92404,-4.81445],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.1781,'kcal/mol','+|-',16.2796),
        S298 = (-1.23252,'cal/mol/K','+|-',7.38473),
    ),
    shortDesc = """Radical correction fitted to 40 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 185,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C",
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
        Cpdata = ([0.301323,-0.991472,-2.13419,-2.76457,-3.53191,-4.02434,-4.86211],'cal/mol/K','+|-',[3,3,3.02847,3,3,3,3]),
        H298 = (84.3672,'kcal/mol','+|-',15.4459),
        S298 = (-0.842189,'cal/mol/K','+|-',6.92466),
    ),
    shortDesc = """Radical correction fitted to 33 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 186,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R",
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
        Cpdata = ([0.27252,-0.346444,-1.20626,-1.92711,-2.86007,-3.4229,-4.64112],'cal/mol/K','+|-',[3.67452,3.74907,3,3,3,3.00084,3]),
        H298 = (93.6334,'kcal/mol','+|-',29.8757),
        S298 = (0.249082,'cal/mol/K','+|-',9.84551),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 187,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_7R!H-inRing",
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
        Cpdata = ([0.165019,-0.447596,-1.11574,-1.5965,-2.42966,-3.17183,-4.46554],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (76.6256,'kcal/mol','+|-',12.0308),
        S298 = (2.77763,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 188,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_7R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S}
4   C   u0 r1 {1,S} {6,S} {8,[S,D,T,B,Q]}
5   C   u0 r1 {3,S} {6,S}
6   C   u0 r1 {4,S} {5,S} {7,S}
7   C   ux r1 {6,S}
8   R!H ux {4,[S,D,T,B,Q]}
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
    index = 189,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_7R!H-inRing_Int-7R!H-4C",
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
        Cpdata = ([-0.276328,-0.515126,-1.00265,-1.59227,-2.55906,-3.31924,-4.52314],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.9831,'kcal/mol','+|-',5.2),
        S298 = (3.20994,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C=CCC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 190,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_N-7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   R!H u0 r0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.333949,-0.288642,-1.25799,-2.11603,-3.10602,-3.56637,-4.74145],'cal/mol/K','+|-',[4.93759,5.1071,3.76823,3,3,4.04062,3.64114]),
        H298 = (100.265,'kcal/mol','+|-',21.702),
        S298 = (-1.1958,'cal/mol/K','+|-',12.1163),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 191,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_N-7R!H-inRing_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux {1,S} {6,S}
5   C ux {3,S} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]} {7,S}
7   C u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19123,0.748535,-0.354183,-1.29158,-2.49274,-2.88183,-4.41969],'cal/mol/K','+|-',[6.08767,5.66371,3,3,3,3,3]),
        H298 = (104.521,'kcal/mol','+|-',5.2),
        S298 = (-0.200247,'cal/mol/K','+|-',6.7316),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 192,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_N-7R!H-inRing_7R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux r1 {1,S} {6,S}
5   C   ux r1 {3,S} {6,[S,T,Q,B]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]} {7,S}
7   C   u0 r0 {6,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.133269,-0.483726,-0.999066,-1.6067,-2.59749,-3.33569,-4.43766],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.012,'kcal/mol','+|-',2.4),
        S298 = (1.26436,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1C[C]2C=CC1CC2 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 193,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_N-7R!H-inRing_N-7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   O u0 r0 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.05914,-1.97406,-2.72668,-3.45576,-4.10261,-4.67875,-5.26431],'cal/mol/K','+|-',[3.76302,3.96903,3.5639,3,4.1054,6.21497,6.76027]),
        H298 = (88.1446,'kcal/mol','+|-',21.8108),
        S298 = (-2.81358,'cal/mol/K','+|-',21.1829),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 194,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_N-7R!H-inRing_N-7R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {6,S}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]} {7,[S,D,T,B,Q]}
7   O   u0 r0 {6,[S,D,T,B,Q]}
8   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.38957,-3.37732,-3.98671,-3.81281,-2.65113,-2.48143,-2.8742],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.4333,'kcal/mol','+|-',5.2),
        S298 = (-10.3029,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COC1[CH]C=C(C)CC1OO - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 195,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R",
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
        Cpdata = ([0.0795465,-2.05814,-3.66382,-4.28413,-4.57194,-4.78905,-5.31173],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.3529,'kcal/mol','+|-',5.2),
        S298 = (-3.19211,'cal/mol/K','+|-',4.92299),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 196,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]} {7,S}
4   C   u0 r1 {1,S} {6,S} {8,[S,D,T,B,Q]}
5   C   u0 r1 {3,[S,D,T,B,Q]} {6,S}
6   C   u0 r1 {4,S} {5,S}
7   C   u0 r0 {3,S}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.159216,-2.73705,-4.64021,-5.4003,-5.6488,-5.99159,-6.10244],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.3101,'kcal/mol','+|-',5.2),
        S298 = (-4.64589,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=C[CH]C(OOCC(C)C)CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 197,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux {1,S} {6,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   C ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.588561,-1.82626,-3.43155,-4.02652,-4.18343,-4.27049,-4.86138],'cal/mol/K','+|-',[3.78695,3.21598,3,3,3,3,3]),
        H298 = (82.3819,'kcal/mol','+|-',5.2),
        S298 = (-4.47467,'cal/mol/K','+|-',5.22379),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 198,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   C u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.750328,-2.96327,-4.38719,-4.61446,-4.03808,-3.84087,-4.34877],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.7976,'kcal/mol','+|-',5.2),
        S298 = (-6.32156,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CCC1=C[CH]CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 199,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,[B,D,T,Q]}
9   C u0 r0 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.92745,-0.689236,-2.47592,-3.43859,-4.32877,-4.70012,-5.374],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.9662,'kcal/mol','+|-',5.2),
        S298 = (-2.62778,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=C[CH]CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 200,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-5R!H-R",
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
        Cpdata = ([0.068348,-2.05131,-3.70601,-4.11978,-4.31725,-4.62218,-5.27765],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.0451,'kcal/mol','+|-',5.2),
        S298 = (-2.58525,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1CC[CH]C=C1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 201,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux {1,S} {6,S}
5   C ux {3,S} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.327328,-1.70655,-2.75436,-3.19859,-3.63596,-3.95329,-4.43701],'cal/mol/K','+|-',[3,3,3.52988,3,3,3,3]),
        H298 = (81.3203,'kcal/mol','+|-',5.2),
        S298 = (-2.20021,'cal/mol/K','+|-',7.37361),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 202,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux {1,S} {6,S}
5   C   ux {3,S} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   C   ux {1,[S,D,T,B,Q]} {8,S}
8   R!H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.556518,-1.80342,-2.6782,-3.05391,-3.50601,-3.81488,-4.22893],'cal/mol/K','+|-',[3,3.47324,4.48385,3.51889,3,3,3]),
        H298 = (81.3795,'kcal/mol','+|-',5.2),
        S298 = (-3.51887,'cal/mol/K','+|-',9.26215),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 203,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux {1,S} {6,S}
5   C ux {3,S} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   C ux {1,[S,D,T,B,Q]} {8,S}
8   C u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.137481,-1.18804,-2.00264,-2.57733,-3.49932,-4.00144,-4.58419],'cal/mol/K','+|-',[3,3,4.40121,3.75281,3,3,3]),
        H298 = (81.4752,'kcal/mol','+|-',5.2),
        S298 = (-1.82178,'cal/mol/K','+|-',6.74064),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 204,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_Sp-9R!H-8C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {3,S} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux {1,[S,D,T,B,Q]} {8,S}
8   C u0 r0 {7,S} {9,S}
9   C u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.230328,-2.52327,-4.15719,-4.41446,-3.97808,-3.78087,-4.41877],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.4376,'kcal/mol','+|-',5.2),
        S298 = (-5.12156,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC[C]1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 205,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_N-Sp-9R!H-8C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux r1 {1,S} {6,S}
5   C ux r1 {3,S} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux {1,[S,D,T,B,Q]} {8,S}
8   C u0 r0 {7,S} {9,[B,D,T,Q]}
9   C u0 r0 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0962158,-0.59461,-1.04506,-1.76083,-3.28653,-4.09947,-4.6577],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (81.6962,'kcal/mol','+|-',2.4),
        S298 = (-0.355208,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CC[C]1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 206,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_N-8R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C                      ux r1 {1,S} {3,D}
3   C                      ux r1 {2,D} {5,S}
4   C                      ux r1 {1,S} {6,S}
5   C                      ux r1 {3,S} {6,[S,T,Q,B]}
6   C                      ux r1 {4,S} {5,[S,T,Q,B]}
7   C                      ux {1,[S,D,T,B,Q]} {8,S}
8   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.91839,-3.80337,-4.87379,-4.60279,-3.52778,-3.20857,-3.07435],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.8348,'kcal/mol','+|-',5.2),
        S298 = (-9.03442,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC[C]1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 207,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R",
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
        Cpdata = ([-0.0220959,-2.44666,-4.20155,-4.59176,-4.45371,-4.47061,-4.7809],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.7051,'kcal/mol','+|-',5.2),
        S298 = (-3.12266,'cal/mol/K','+|-',3.83934),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 208,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R_8R!H->C",
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
    index = 209,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R_N-8R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S} {7,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {5,S}
4   C                      u0 r1 {1,S} {6,S} {8,S}
5   C                      u0 r1 {3,S} {6,S}
6   C                      u0 r1 {4,S} {5,S}
7   C                      u0 r0 {1,S}
8   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01254,-3.37202,-4.95709,-5.12373,-4.50018,-4.23904,-4.10415],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.6452,'kcal/mol','+|-',5.2),
        S298 = (-4.48007,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1CCC=C[C]1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 210,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R",
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
        Cpdata = ([1.11921,-0.269298,-1.64267,-2.34735,-3.36062,-3.87298,-4.9222],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.9262,'kcal/mol','+|-',5.2),
        S298 = (0.114335,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 211,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux {1,S} {6,S}
5   C   ux {3,S} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   R!H ux r1 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.16907,0.511588,-1.41518,-2.25949,-3.28055,-3.69978,-5.03783],'cal/mol/K','+|-',[3,3,3,3.22872,3,3,3]),
        H298 = (81.1168,'kcal/mol','+|-',5.2),
        S298 = (0.944066,'cal/mol/K','+|-',3.34418),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 212,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux r1 {1,S} {6,S}
5   C   ux r1 {3,S} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]}
7   R!H ux r1 {5,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
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
    index = 213,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing",
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
        Cpdata = ([0.719259,-0.566779,-1.72934,-2.38082,-3.39113,-3.93896,-4.87815],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.3965,'kcal/mol','+|-',5.2),
        S298 = (-0.201754,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 214,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C u0 {1,S} {6,S} {8,S}
5   C u0 {3,[S,D,T,B,Q]} {6,S} {7,S}
6   C u0 {4,S} {5,S}
7   C u0 r0 {5,S}
8   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.24933,-0.591835,-2.18765,-2.86611,-3.92981,-4.2663,-5.11159],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.0078,'kcal/mol','+|-',5.2),
        S298 = (-1.51972,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 215,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {6,S} {8,S}
5   C   u0 r1 {3,[S,D,T,B,Q]} {6,S} {7,S}
6   C   u0 r1 {4,S} {5,S}
7   C   u0 r0 {5,S} {9,[S,D,T,B,Q]}
8   C   u0 r0 {4,S}
9   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.24933,-0.591835,-2.18765,-2.86611,-3.92981,-4.2663,-5.11159],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.0078,'kcal/mol','+|-',5.2),
        S298 = (-1.51972,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1C=C[CH]C(C)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 216,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-5R!H-R",
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
        Cpdata = ([1.27252,-0.837608,-2.54074,-3.46,-4.59476,-5.08559,-5.41317],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.3593,'kcal/mol','+|-',5.2),
        S298 = (-0.712704,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1(C)C=C[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 217,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S} {6,S} {7,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.464127,-1.05965,-2.26569,-2.94579,-3.88716,-4.54407,-5.27347],'cal/mol/K','+|-',[3,3.11912,3.12736,3.01506,3,3,3]),
        H298 = (81.7248,'kcal/mol','+|-',7.56609),
        S298 = (-0.530813,'cal/mol/K','+|-',7.14912),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 218,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 {1,S} {6,S} {7,[S,D,T,B,Q]}
5   C   u0 {3,[S,D,T,B,Q]} {6,S}
6   C   u0 {4,S} {5,S}
7   R!H u0 r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.69031,0.103933,-1.45205,-2.24782,-3.45224,-4.19769,-5.28041],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.6471,'kcal/mol','+|-',9.70901),
        S298 = (1.44942,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 219,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C   u0 {1,S} {6,S} {7,[S,D,T,B,Q]} {8,S}
5   C   u0 {3,[S,D,T,B,Q]} {6,S}
6   C   u0 {4,S} {5,S}
7   R!H u0 r1 {4,[S,D,T,B,Q]}
8   C   u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.54968,0.189218,-1.00939,-1.67122,-3.04687,-4.13022,-5.13906],'cal/mol/K','+|-',[3,3,3,3,3,3.00609,3]),
        H298 = (76.4331,'kcal/mol','+|-',8.41984),
        S298 = (2.29327,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 220,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C u0 r1 {1,S} {6,S} {7,[S,D,T,B,Q]} {8,S}
5   C u0 r1 {3,[S,D,T,B,Q]} {6,S}
6   C u0 r1 {4,S} {5,S}
7   O u0 r1 {4,[S,D,T,B,Q]}
8   C u0 r1 {4,S}
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
    index = 221,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_N-7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,[S,D,T,B,Q]}
4   C u0 r1 {1,S} {6,S} {7,[S,D,T,B,Q]} {8,S}
5   C u0 r1 {3,[S,D,T,B,Q]} {6,S}
6   C u0 r1 {4,S} {5,S}
7   C u0 r1 {4,[S,D,T,B,Q]}
8   C u0 r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.36705,1.08981,-0.393474,-1.11845,-2.29882,-3.0674,-4.51302],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.41,'kcal/mol','+|-',5.2),
        S298 = (2.12928,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1CC12[CH]C=CCC2 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 222,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux {1,S} {6,S} {7,[S,D,T,B,Q]}
5   C   ux {3,S} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   R!H ux r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.124441,-1.61817,-2.65624,-3.28082,-4.09592,-4.71034,-5.27014],'cal/mol/K','+|-',[3,3.1157,3.48268,3.32783,3.2574,3.16212,3]),
        H298 = (82.7868,'kcal/mol','+|-',5.7109),
        S298 = (-1.48133,'cal/mol/K','+|-',8.15435),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 223,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux {1,S} {6,S} {7,S}
5   C   ux {3,S} {6,[S,T,Q,B]}
6   C   ux {4,S} {5,[S,T,Q,B]}
7   R!H ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.326069,-1.66973,-2.65609,-3.14052,-3.75564,-4.33158,-4.8121],'cal/mol/K','+|-',[3,3.52863,3.95909,3.69,3.1017,3,3]),
        H298 = (83.5654,'kcal/mol','+|-',5.2),
        S298 = (-2.1022,'cal/mol/K','+|-',8.50342),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 224,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux {1,S} {6,S} {7,S}
5   C ux {3,S} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   O ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42456,-3.44414,-4.61696,-4.88554,-4.9387,-5.37833,-4.94685],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.0983,'kcal/mol','+|-',5.2),
        S298 = (-6.52375,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 225,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Sp-11R!H=10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,S}
4    C ux r1 {1,S} {6,S} {7,S}
5    C ux r1 {3,S} {6,[S,T,Q,B]}
6    C ux r1 {4,S} {5,[S,T,Q,B]}
7    O ux r0 {4,S} {8,[S,D,T,B,Q]}
8    O ux {7,[S,D,T,B,Q]} {9,S}
9    C u0 r0 {8,S} {10,[S,D,T,B,Q]}
10   C ux {9,[S,D,T,B,Q]} {11,D}
11   C u0 r0 {10,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.45197,-4.24795,-5.07086,-4.91191,-4.28147,-4.61504,-3.93502],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.0722,'kcal/mol','+|-',5.2),
        S298 = (-7.36658,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1(C)[CH]C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 226,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_N-Sp-11R!H=10R!H",
    group = 
"""
1  * C u1 r1 {2,S} {4,S}
2    C ux r1 {1,S} {3,D}
3    C ux r1 {2,D} {5,S}
4    C ux r1 {1,S} {6,S} {7,S}
5    C ux r1 {3,S} {6,[S,T,Q,B]}
6    C ux r1 {4,S} {5,[S,T,Q,B]}
7    O ux r0 {4,S} {8,[S,D,T,B,Q]}
8    O ux {7,[S,D,T,B,Q]} {9,S}
9    C u0 r0 {8,S} {10,[S,D,T,B,Q]}
10   C ux {9,[S,D,T,B,Q]} {11,S}
11   C u0 r0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.397145,-2.64033,-4.16307,-4.85916,-5.59593,-6.14161,-5.95869],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.1244,'kcal/mol','+|-',5.2),
        S298 = (-5.68093,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)COOC1(C)[CH]C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 227,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_N-7R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux {1,S} {6,S} {7,S}
5   C ux {3,S} {6,[S,T,Q,B]}
6   C ux {4,S} {5,[S,T,Q,B]}
7   C ux r0 {4,S}
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
    index = 228,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_N-7R!H->O_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,S}
4   C   ux r1 {1,S} {6,S} {7,S} {8,[S,D,T,B,Q]}
5   C   ux r1 {3,S} {6,[S,T,Q,B]}
6   C   ux r1 {4,S} {5,[S,T,Q,B]}
7   C   ux r0 {4,S}
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
    index = 229,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_N-Sp-7R!H-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D}
3   C ux r1 {2,D} {5,S}
4   C ux r1 {1,S} {6,S} {7,D}
5   C ux r1 {3,S} {6,[S,T,Q,B]}
6   C ux r1 {4,S} {5,[S,T,Q,B]}
7   C ux r0 {4,D}
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
    index = 230,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C ux {1,S} {6,[B,D,T,Q]}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,[B,D,T,Q]} {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.416149,-0.921106,-1.90608,-2.48674,-3.00819,-3.49646,-4.61129],'cal/mol/K','+|-',[3.97501,3,3,3,3,3,3]),
        H298 = (73.7851,'kcal/mol','+|-',5.2),
        S298 = (-2.89654,'cal/mol/K','+|-',9.02187),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 231,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux {1,S} {6,[B,D,T,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,[B,D,T,Q]} {5,[S,T,Q,B]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.08552,-0.749444,-1.91188,-2.55271,-3.06453,-3.52237,-4.51362],'cal/mol/K','+|-',[4.1177,3,3,3,3,3,3]),
        H298 = (73.5111,'kcal/mol','+|-',5.2),
        S298 = (-4.71147,'cal/mol/K','+|-',9.09377),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 232,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux {1,S} {6,[B,D,T,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux {4,[B,D,T,Q]} {5,[S,T,Q,B]}
7   R!H ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.01561,-0.6361,-2.22482,-3.00163,-3.37278,-3.70162,-4.53989],'cal/mol/K','+|-',[3.78324,3,3,3,3,3,3]),
        H298 = (72.847,'kcal/mol','+|-',5.2),
        S298 = (-7.61331,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 233,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux {1,S} {3,D}
3   C ux r1 {2,D} {5,[S,D,T,B,Q]} {7,S}
4   C ux {1,S} {6,D}
5   C ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C ux {4,D} {5,[S,T,Q,B]}
7   C u0 {3,S} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.92587,-1.01555,-2.76127,-3.62209,-4.01898,-4.32471,-5.16791],'cal/mol/K','+|-',[4.6126,3,3,3,3,3,3]),
        H298 = (73.6081,'kcal/mol','+|-',5.2),
        S298 = (-7.34323,'cal/mol/K','+|-',3.09767),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 234,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_7R!H->C_Ext-6CN-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]} {7,S}
4   C   ux r1 {1,S} {6,D}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux r1 {4,D} {5,[S,T,Q,B]} {9,[S,D,T,B,Q]}
7   C   u0 r0 {3,S} {8,[S,D,T,B,Q]}
8   C   ux {7,[S,D,T,B,Q]}
9   R!H ux {6,[S,D,T,B,Q]}
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
    index = 235,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_7R!H->C_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S} {7,S}
4   C u0 r1 {1,S} {6,D}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,D} {5,S}
7   C u0 r0 {3,S} {8,S}
8   C u0 r0 {7,S} {9,S}
9   C u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.45802,-2.64887,-3.88323,-4.23364,-3.80863,-3.86784,-4.71043],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.9028,'kcal/mol','+|-',5.2),
        S298 = (-6.40282,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CCCC1=C[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 236,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_7R!H->C_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {5,S} {7,S}
4   C u0 r1 {1,S} {6,D}
5   C u0 r1 {3,S} {6,S}
6   C u0 r1 {4,D} {5,S}
7   C u0 r0 {3,S} {8,S}
8   C u0 r0 {7,S} {9,[B,D,T,Q]}
9   C u0 r0 {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.0898,-0.408733,-2.17616,-3.17647,-3.81401,-4.26291,-5.32703],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.9016,'kcal/mol','+|-',5.2),
        S298 = (-6.496,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCC1=C[CH]C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 237,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_N-7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {5,S} {7,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {6,[B,D,T,Q]}
5   C   u0 r1 {3,S} {6,S}
6   C   u0 r1 {4,[B,D,T,Q]} {5,S}
7   O   ux {3,[S,D,T,B,Q]} {8,S}
8   R!H u0 r0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.28484,0.502261,-0.615479,-1.14025,-1.43416,-1.83234,-2.65584],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (70.5636,'kcal/mol','+|-',5.2),
        S298 = (-8.42355,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCN(OC1=C[CH]C=CC1)CC - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 238,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,D}
3   C   ux r1 {2,D} {5,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {6,[B,D,T,Q]}
5   C   ux r1 {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C   ux r1 {4,[B,D,T,Q]} {5,[S,T,Q,B]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.23965,-2.66112,-3.37235,-3.94908,-4.18307,-4.38328,-5.55377],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (73.0829,'kcal/mol','+|-',5.2),
        S298 = (1.61268,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 239,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_N-Sp-2R!H-1R",
    group = 
"""
1 * C u1 r1 {2,D} {4,S}
2   C ux r1 {1,D} {3,D}
3   C ux r1 {2,D}
4   C ux r1 {1,S}
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
    index = 240,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.209995,-0.897633,-1.92419,-2.53955,-3.24691,-3.83503,-4.70546],'cal/mol/K','+|-',[3.05706,3.54706,4.29642,4.60319,4.50376,4.60968,4.6086]),
        H298 = (89.601,'kcal/mol','+|-',40.3449),
        S298 = (1.6987,'cal/mol/K','+|-',7.72025),
    ),
    shortDesc = """Radical correction fitted to 75 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 241,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.273301,-0.847417,-1.91978,-2.59996,-3.40942,-4.09051,-4.82029],'cal/mol/K','+|-',[3.1342,3.41501,4.15801,4.54025,4.49267,4.65885,4.45974]),
        H298 = (87.2178,'kcal/mol','+|-',43.6734),
        S298 = (1.52613,'cal/mol/K','+|-',7.91096),
    ),
    shortDesc = """Radical correction fitted to 58 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 242,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0988049,-0.817379,-1.69356,-2.22955,-2.91457,-3.45942,-4.11499],'cal/mol/K','+|-',[3.22458,4.06369,4.66062,4.68015,4.31432,4.36658,4.60036]),
        H298 = (83.6642,'kcal/mol','+|-',56.6913),
        S298 = (2.24387,'cal/mol/K','+|-',9.74834),
    ),
    shortDesc = """Radical correction fitted to 29 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 243,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.177154,-1.1279,-2.02853,-2.52904,-3.08899,-3.55563,-3.98929],'cal/mol/K','+|-',[3.74132,4.79151,5.51414,5.56825,5.1976,5.3021,5.58137]),
        H298 = (74.166,'kcal/mol','+|-',65.5319),
        S298 = (2.36727,'cal/mol/K','+|-',11.6873),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 244,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.47869,-3.36105,-4.66382,-5.18927,-5.46344,-5.81491,-5.53636],'cal/mol/K','+|-',[6.83097,6.75262,6.51926,5.90297,4.32068,3.84346,3]),
        H298 = (87.522,'kcal/mol','+|-',11.2308),
        S298 = (3.08068,'cal/mol/K','+|-',10.5663),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 245,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Int-4R!H-2R!H",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C u0 r0 {2,D}
4   C u0 r1 {1,S} {2,[S,D,T,B,Q]} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.62813,-0.346037,-1.76043,-2.26587,-3.01141,-3.49475,-4.314],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.7713,'kcal/mol','+|-',5.2),
        S298 = (4.55835,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 246,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {6,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r0 {2,D}
4   C u0 {1,S} {5,S}
5   O u0 {4,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.72202,-5.55912,-6.7385,-7.03208,-6.89797,-6.79304,-6.59619],'cal/mol/K','+|-',[8.01191,7.29329,6.3195,5.14807,3.39796,3.63937,3]),
        H298 = (86.8909,'kcal/mol','+|-',12.2652),
        S298 = (7.3626,'cal/mol/K','+|-',7.10296),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 247,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Ext-1R-R_Ext-2R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {6,S}
2   C u0 r1 {1,S} {3,D} {7,[S,D,T,B,Q]}
3   C u0 r0 {2,D}
4   C u0 {1,S} {5,S}
5   O u0 {4,S}
6   C u0 {1,S}
7   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.69939,-6.49467,-7.70355,-8.01542,-7.80746,-7.83548,-6.45002],'cal/mol/K','+|-',[10.2692,9.24003,7.58421,5.45877,3,3,3]),
        H298 = (83.48,'kcal/mol','+|-',5.2),
        S298 = (5.84778,'cal/mol/K','+|-',6.76987),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 248,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Ext-1R-R_Ext-2R!H-R_Ext-7R!H-R_Ext-5O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,S}
2   C   u0 r1 {1,S} {3,D} {7,[S,D,T,B,Q]}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S}
5   O   u0 r1 {4,S} {9,[S,D,T,B,Q]}
6   C   u0 r0 {1,S}
7   C   ux r1 {2,[S,D,T,B,Q]} {8,S}
8   O   u0 r1 {7,S}
9   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.33008,-9.76152,-10.385,-9.94539,-8.44388,-7.60919,-6.43041],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.8352,'kcal/mol','+|-',5.2),
        S298 = (8.24129,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1COC(C)(C)C(C)(C)OOC[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 249,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15821,-4.76811,-6.44629,-6.85852,-6.0076,-6.11068,-3.67432],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.3431,'kcal/mol','+|-',5.2),
        S298 = (-3.43926,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)COOC1[CH]C(=C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 250,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Ext-5O-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {7,[S,D,T,B,Q]}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S}
5   O   u0 r1 {4,S} {6,S}
6   O   u0 r1 {5,S}
7   R!H ux {2,[S,D,T,B,Q]}
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
    index = 251,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   R!H ux {1,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.251586,-0.392271,-1.16043,-1.65273,-2.30682,-2.8114,-3.47966],'cal/mol/K','+|-',[3,3,3.91287,4.26892,4.52362,4.91621,6.01447]),
        H298 = (71.3729,'kcal/mol','+|-',71.6756),
        S298 = (2.13227,'cal/mol/K','+|-',12.3038),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 252,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   C   ux r0 {2,D}
4   R!H ux {1,S} {5,S}
5   C   u0 {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.225943,-0.1424,-0.864955,-1.47375,-2.50666,-3.31016,-4.56153],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.2954,'kcal/mol','+|-',5.2),
        S298 = (0.0945129,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 253,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   C   ux r0 {2,D}
4   R!H ux r1 {1,S} {5,S}
5   C   u0 r1 {2,S} {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0583814,-1.24522,-2.1542,-2.47424,-3.30765,-3.99042,-4.88553],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.8814,'kcal/mol','+|-',5.2),
        S298 = (1.11552,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CC[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 254,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {5,S}
3   C u0 r0 {2,D}
4   C u0 {1,S} {5,S}
5   C u0 {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.392955,-0.0438015,-0.826901,-1.44693,-2.45495,-3.22327,-4.56442],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.4583,'kcal/mol','+|-',5.2),
        S298 = (-0.355203,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 255,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H_4R!H->C_Ext-5BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.812109,0.166506,-0.876585,-1.51058,-2.54835,-3.31103,-4.75363],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.0157,'kcal/mol','+|-',5.2),
        S298 = (0.639767,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 256,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {5,S}
3   C u0 r0 {2,D}
4   O u0 {1,S} {5,S}
5   C u0 {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.214898,0.0588486,-0.595368,-1.26334,-2.35164,-3.19761,-4.48824],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (82.3048,'kcal/mol','+|-',2.4),
        S298 = (0.0674961,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 257,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H_N-4R!H->C_Ext-5BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D}
4   O   u0 r1 {1,S} {5,S}
5   C   u0 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 258,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.283815,-0.17066,-0.673227,-1.04669,-1.57099,-1.94937,-2.23202],'cal/mol/K','+|-',[3,3,3.57175,4.32359,5.38465,6.3358,7.81118]),
        H298 = (59.7122,'kcal/mol','+|-',94.9976),
        S298 = (2.46928,'cal/mol/K','+|-',16.4816),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 259,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.151414,0.057651,-0.179865,-0.432543,-0.863088,-1.15441,-1.27244],'cal/mol/K','+|-',[3,3,3.58048,4.54042,6.27297,7.72138,10.0334]),
        H298 = (43.9522,'kcal/mol','+|-',115.284),
        S298 = (-0.0570052,'cal/mol/K','+|-',4.23926),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 260,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H_Sp-6R!H-5BrCClFINPSSi",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,S}
6   C ux {2,[S,D,T,B,Q]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.194547,0.0550283,-0.036241,-0.0766648,-0.177939,-0.178675,0.35329],'cal/mol/K','+|-',[3,3,4.7502,5.87467,7.84569,9.41767,11.4068]),
        H298 = (15.9638,'kcal/mol','+|-',122.671),
        S298 = (0.952305,'cal/mol/K','+|-',3.58477),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 261,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H_Sp-6R!H-5BrCClFINPSSi_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]} {6,S}
6   C   u0 r1 {2,[S,D,T,B,Q]} {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
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
    index = 262,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H_Sp-6R!H-5BrCClFINPSSi_Sp-5BrCClFINPSSi-4C",
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
    index = 263,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H_Sp-6R!H-5BrCClFINPSSi_N-Sp-5BrCClFINPSSi-4C",
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
        Cpdata = ([-0.212362,-0.521882,-0.7979,-1.12004,-2.01784,-2.93152,-2.57073],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.8313,'kcal/mol','+|-',5.2),
        S298 = (0.773844,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]C#CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 264,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H_N-Sp-6R!H-5BrCClFINPSSi",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {6,S}
3   C u0 r0 {2,D}
4   C u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C u0 r1 {4,[S,D,T,B,Q]} {6,D}
6   C ux r1 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0699417,0.062605,-0.451155,-1.10476,-2.15726,-2.99747,-4.34326],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.8645,'kcal/mol','+|-',2.4),
        S298 = (-1.96348,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 265,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D} {6,S}
3   C u0 r0 {2,D}
4   C u0 {1,S} {5,S}
5   C u0 {4,S}
6   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.273937,-0.903929,-1.88164,-2.44519,-3.17547,-3.79195,-4.29183],'cal/mol/K','+|-',[3,3,4.46211,5.06978,4.62093,3.82925,3]),
        H298 = (86.2115,'kcal/mol','+|-',5.2),
        S298 = (0.454695,'cal/mol/K','+|-',4.09112),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 266,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-2R!H-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {6,S}
3   C   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 r1 {4,S}
6   C   u0 r1 {2,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0884508,-2.32997,-4.066,-4.92703,-5.43758,-5.6665,-3.99703],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.7506,'kcal/mol','+|-',5.2),
        S298 = (-1.54806,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]C(=C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 267,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r0 {2,D}
4   O u0 {1,S} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.200205,-1.81105,-3.64492,-4.27184,-4.44396,-4.65343,-5.24574],'cal/mol/K','+|-',[3.38404,6.36708,6.73232,6.53722,5.40924,3.95064,3.26283]),
        H298 = (96.555,'kcal/mol','+|-',30.9353),
        S298 = (6.01902,'cal/mol/K','+|-',10.1355),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 268,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_N-4R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   O   u0 {1,S} {5,S}
5   C   u0 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.228808,-1.92686,-3.67343,-4.39133,-4.69059,-4.73131,-4.40912],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (113.123,'kcal/mol','+|-',5.2),
        S298 = (6.23655,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=C1O[C]1OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 269,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_N-4R!H->C_Ext-5BrCClFINPSSi-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {7,[S,D,T,B,Q]}
3   C   u0 r0 {2,D}
4   O   u0 r1 {1,S} {5,S}
5   C   u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   R!H u0 {5,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
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
    index = 270,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D}
4   R!H ux r1 {1,S}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.524508,-1.01551,-2.20155,-2.76874,-3.60074,-4.06313,-5.17429],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.1437,'kcal/mol','+|-',5.2),
        S298 = (5.99254,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 271,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.828274,0.036035,-0.807373,-1.4622,-2.4574,-3.19411,-4.29623],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.9151,'kcal/mol','+|-',9.78492),
        S298 = (1.7429,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 272,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {5,[S,D,T,B,Q]}
4   C   ux {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.739771,-0.0670134,-0.935743,-1.59757,-2.57221,-3.26542,-4.25595],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.9806,'kcal/mol','+|-',11.7212),
        S298 = (1.58079,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 273,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R_Sp-5R!H-3C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {5,S}
4   C   ux r1 {1,S}
5   R!H u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.794855,-0.121614,-1.12852,-1.78904,-2.7189,-3.30413,-4.03738],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (91.9493,'kcal/mol','+|-',2.4),
        S298 = (1.85481,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 274,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R_N-Sp-5R!H-3C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {5,[B,D,T,Q]}
4   C   ux {1,S}
5   R!H ux {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.717237,-0.0446769,-0.856881,-1.51924,-2.5122,-3.24958,-4.34537],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.706,'kcal/mol','+|-',8.80644),
        S298 = (1.46869,'cal/mol/K','+|-',3.74653),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 275,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r0 {2,D} {5,[B,D,T,Q]}
4   C   u0 r1 {1,S}
5   R!H ux {3,[B,D,T,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 276,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R_N-Sp-5R!H-3C_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {5,[B,D,T,Q]}
4   C ux r1 {1,S}
5   C ux {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.970463,0.247511,-0.603339,-1.28955,-2.36813,-3.13856,-4.24483],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.245,'kcal/mol','+|-',2.4),
        S298 = (2.85796,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 277,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R_N-Sp-5R!H-3C_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D} {5,[B,D,T,Q]}
4   C ux r1 {1,S}
5   O ux {3,[B,D,T,Q]}
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
    index = 278,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   O ux r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.132343,-0.623548,-1.20065,-1.64007,-2.45156,-3.16236,-4.41704],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.706,'kcal/mol','+|-',2.4),
        S298 = (1.25502,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 279,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.458983,-0.879381,-2.16051,-2.99411,-3.93598,-4.76204,-5.5708],'cal/mol/K','+|-',[3.05935,3,3.58539,4.34517,4.52663,4.66994,3.85266]),
        H298 = (91.2199,'kcal/mol','+|-',20.6015),
        S298 = (0.762368,'cal/mol/K','+|-',5.10473),
    ),
    shortDesc = """Radical correction fitted to 29 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 280,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   R!H ux {1,S}
5   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0174928,-0.941658,-1.9232,-2.58122,-3.37009,-4.11955,-4.77881],'cal/mol/K','+|-',[3,3,3.23606,3.57362,3.48916,3.5761,3]),
        H298 = (84.7059,'kcal/mol','+|-',10.6135),
        S298 = (0.0605852,'cal/mol/K','+|-',5.53262),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 281,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux {1,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.215032,-0.647947,-1.57038,-2.22106,-3.0971,-3.84946,-4.80861],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.827,'kcal/mol','+|-',6.67602),
        S298 = (-0.384056,'cal/mol/K','+|-',5.89191),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 282,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   O   ux {1,S}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.365577,-0.607472,-1.60581,-2.27381,-3.14658,-3.90831,-4.84276],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (82.3132,'kcal/mol','+|-',7.06433),
        S298 = (-0.430848,'cal/mol/K','+|-',6.43549),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 283,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   O   ux {1,S} {7,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.400722,-0.946162,-2.19077,-2.94464,-3.79698,-4.59651,-5.46835],'cal/mol/K','+|-',[3,3,3,3.14522,3,3,3]),
        H298 = (80.0523,'kcal/mol','+|-',5.2),
        S298 = (-0.210843,'cal/mol/K','+|-',4.74284),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 284,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_Sp-6R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   O   ux {1,S} {7,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,S}
6   C   ux {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.982713,-1.14693,-3.0216,-3.89987,-4.58531,-5.36179,-6.14231],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.5456,'kcal/mol','+|-',5.2),
        S298 = (0.6659,'cal/mol/K','+|-',5.88777),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 285,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_Sp-6R!H-5C_Ext-5C-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O ux r0 {2,D}
4   O ux {1,S} {7,S}
5   C u0 {2,S} {6,S} {8,S}
6   C ux {5,S}
7   O u0 {4,S}
8   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.814889,-0.991186,-2.57952,-3.34845,-3.88654,-4.7643,-5.98366],'cal/mol/K','+|-',[3,3,3.20267,3.54506,3.82699,3.7592,3]),
        H298 = (79.556,'kcal/mol','+|-',5.2),
        S298 = (-0.527747,'cal/mol/K','+|-',7.09524),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 286,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_Sp-6R!H-5C_Ext-5C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O   ux r0 {2,D}
4   O   ux r1 {1,S} {7,S}
5   C   u0 r1 {2,S} {6,S} {8,S}
6   C   ux r0 {5,S} {9,[S,D,T,B,Q]}
7   O   u0 r1 {4,S}
8   C   u0 r0 {5,S}
9   R!H ux {6,[S,D,T,B,Q]}
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
    index = 287,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_Sp-6R!H-5C_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux r1 {1,S} {7,[S,D,T,B,Q]}
5   C ux r1 {2,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
7   C ux r1 {4,[S,D,T,B,Q]}
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
    index = 288,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_Sp-6R!H-5C_N-7R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux r1 {1,S} {7,[S,D,T,B,Q]}
5   C ux r1 {2,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
7   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.56914,-0.0593997,-2.42279,-3.4766,-4.79754,-5.96579,-6.45607],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.3324,'kcal/mol','+|-',5.2),
        S298 = (-0.104457,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 289,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_N-Sp-6R!H-5C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   O   u0 {1,S} {7,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,D}
6   R!H u0 {5,D}
7   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.315575,-0.699057,-1.16822,-1.76898,-2.82673,-3.65462,-4.63886],'cal/mol/K','+|-',[3.89904,3,3,3,3,3,3]),
        H298 = (79.0033,'kcal/mol','+|-',5.2),
        S298 = (-1.28991,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 290,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_N-Sp-6R!H-5C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S} {7,[S,D,T,B,Q]}
5   C ux r1 {2,[S,D,T,B,Q]} {6,D}
6   C u0 {5,D}
7   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.59314,0.546241,-0.597172,-1.50921,-3.00877,-4.13867,-4.81481],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (76.4839,'kcal/mol','+|-',5.2),
        S298 = (-1.56313,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1OO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 291,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_N-Sp-6R!H-5C_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S} {7,[S,D,T,B,Q]}
5   C ux r1 {2,[S,D,T,B,Q]} {6,D}
6   O u0 {5,D}
7   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.16389,-1.25252,-1.42202,-1.88444,-2.74583,-3.43949,-4.56067],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (79.5399,'kcal/mol','+|-',2.4),
        S298 = (-1.16848,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]OOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 292,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   O   ux {1,S}
5   C   ux r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
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
    index = 293,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux r1 {1,S}
5   C ux r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]}
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
    index = 294,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux r1 {1,S}
5   C ux r1 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux r1 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.100099,-0.343605,-0.965822,-1.61697,-2.66313,-3.41707,-4.48827],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (84.5242,'kcal/mol','+|-',2.4),
        S298 = (2.02784,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]OOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 295,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   C ux {1,S}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.598804,-1.67594,-2.80526,-3.48163,-4.05258,-4.79476,-4.70431],'cal/mol/K','+|-',[3.16119,3.92083,4.43603,4.96258,5.15142,5.38059,3]),
        H298 = (92.4652,'kcal/mol','+|-',8.60972),
        S298 = (1.17219,'cal/mol/K','+|-',4.34311),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 296,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O ux r0 {2,D}
4   C ux {1,S}
5   C u0 {2,S}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.727925,-2.0419,-3.33517,-4.09051,-4.66725,-5.45455,-5.20227],'cal/mol/K','+|-',[3.62013,4.65031,5.03938,5.28966,5.3,5.40102,3]),
        H298 = (90.4113,'kcal/mol','+|-',5.76746),
        S298 = (1.98274,'cal/mol/K','+|-',4.57136),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 297,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O_Ext-1R-R_Int-5C-4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O ux r0 {2,D}
4   C ux {1,S} {5,S}
5   C u0 {2,S} {4,S}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.312963,-0.701806,-1.88269,-2.5639,-3.14046,-3.89884,-4.60426],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.5298,'kcal/mol','+|-',6.04177),
        S298 = (1.60407,'cal/mol/K','+|-',6.193),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 298,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O_Ext-1R-R_Int-5C-4C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S} {5,S} {7,[S,D,T,B,Q]}
5   C   u0 r1 {2,S} {4,S}
6   C   ux r0 {1,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 299,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O_Int-5C-4C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.00415,0.455664,-0.521349,-1.16474,-2.18668,-3.06417,-3.72884],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.7697,'kcal/mol','+|-',5.2),
        S298 = (1.73213,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]C2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 300,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O_Ext-5C-R_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   C   u0 r1 {1,S} {3,D} {5,S}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S}
5   C   u0 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0707311,-0.983738,-1.47892,-1.46916,-1.36989,-1.73175,-2.89318],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.7303,'kcal/mol','+|-',5.2),
        S298 = (-2.1083,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 301,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   R!H ux {1,S}
5   O   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.01487,-0.806723,-2.43738,-3.47582,-4.59619,-5.51162,-6.4948],'cal/mol/K','+|-',[3.07474,3,4.03793,5.1063,5.36638,5.48189,4.49661]),
        H298 = (98.4373,'kcal/mol','+|-',19.5815),
        S298 = (1.58112,'cal/mol/K','+|-',4.20646),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 302,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   C ux {1,S}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.05344,-0.9097,-2.49774,-3.46715,-4.70908,-5.69914,-6.97904],'cal/mol/K','+|-',[3.53697,3,3.73603,4.43566,5.08063,5.42947,5.04823]),
        H298 = (103.613,'kcal/mol','+|-',19.4574),
        S298 = (1.02811,'cal/mol/K','+|-',4.26152),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 303,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O   ux r0 {2,D}
4   C   ux {1,S} {6,[S,D,T,B,Q]}
5   O   u0 {2,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.18423,-0.805463,-3.20241,-4.58154,-6.24139,-7.43192,-8.87463],'cal/mol/K','+|-',[3,3.52297,4.17622,4.50992,4.44232,4.36227,3]),
        H298 = (112.032,'kcal/mol','+|-',17.6832),
        S298 = (0.851219,'cal/mol/K','+|-',5.67037),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 304,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O ux r0 {2,D}
4   C ux {1,S} {6,[S,D,T,B,Q]}
5   O u0 {2,S}
6   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19182,-1.08866,-3.38963,-4.98706,-6.48305,-7.3844,-9.08806],'cal/mol/K','+|-',[3,6.59431,8.55006,9.15568,9.04423,8.86597,3]),
        H298 = (105.29,'kcal/mol','+|-',30.5791),
        S298 = (1.94502,'cal/mol/K','+|-',5.72343),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 305,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_6R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   u0 r1 {2,S}
6   C   ux r1 {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 306,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O ux r0 {2,D}
4   C ux {1,S} {6,[S,D,T,B,Q]}
5   O u0 {2,S}
6   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.68044,-0.663863,-3.10881,-4.37878,-6.12055,-7.45568,-8.76791],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.402,'kcal/mol','+|-',5.25995),
        S298 = (0.304318,'cal/mol/K','+|-',6.15497),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 307,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_N-6R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O   ux r0 {2,D}
4   C   ux {1,S} {6,[S,D,T,B,Q]}
5   O   u0 {2,S}
6   O   ux {4,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.93479,-0.675438,-3.27758,-4.54118,-6.20365,-7.53611,-8.72922],'cal/mol/K','+|-',[3,3,3,3,3,3,3.58981]),
        H298 = (114.225,'kcal/mol','+|-',5.2),
        S298 = (-0.175119,'cal/mol/K','+|-',7.16301),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 308,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_N-6R!H->C_Ext-1R-R_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O   ux r0 {2,D}
4   C   ux {1,S} {6,[S,D,T,B,Q]}
5   O   u0 {2,S} {8,S}
6   O   ux {4,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
8   O   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.55451,-0.0315107,-2.76877,-4.09474,-5.88365,-7.32089,-8.41796],'cal/mol/K','+|-',[3,3,3,3.13805,3.65828,3.88491,4.84234]),
        H298 = (114.987,'kcal/mol','+|-',5.2),
        S298 = (-1.71686,'cal/mol/K','+|-',6.75056),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 309,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_N-6R!H->C_Ext-1R-R_Ext-5BrClFINOPSSi-R_4C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S} {6,[S,D,T,B,Q]}
5   O   u0 r1 {2,S} {8,S}
6   O   ux r0 {4,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
8   O   u0 r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.15952,0.946463,-1.8956,-2.98527,-4.59025,-5.94737,-6.70593],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (114.426,'kcal/mol','+|-',5.2),
        S298 = (-4.10355,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1OOC(O)[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 310,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_N-6R!H->C_Ext-1R-R_Ext-5BrClFINOPSSi-R_N-4C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O   ux r0 {2,D}
4   C   ux r0 {1,S} {6,[S,D,T,B,Q]}
5   O   u0 r1 {2,S} {8,S}
6   O   ux r0 {4,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
8   O   u0 r1 {5,S}
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
    index = 311,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux r1 {1,S}
5   O   ux r1 {2,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06989,-1.90248,-2.30765,-2.51525,-2.92811,-3.62094,-4.54172],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.6911,'kcal/mol','+|-',2.4),
        S298 = (1.38837,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 312,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O ux r0 {2,D}
4   O ux {1,S}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.960871,-0.662557,-2.35287,-3.48795,-4.43815,-5.2491,-5.81686],'cal/mol/K','+|-',[3,3,4.96076,6.60152,6.44561,6.24546,3.70678]),
        H298 = (92.0085,'kcal/mol','+|-',10.8915),
        S298 = (2.35533,'cal/mol/K','+|-',4.08863),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 313,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_4O-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.678305,-0.966424,-2.5308,-3.60077,-4.5016,-5.21995,-5.63047],'cal/mol/K','+|-',[3,3,5.40366,7.31661,7.16765,6.95395,3.94783]),
        H298 = (90.9184,'kcal/mol','+|-',6.88626),
        S298 = (2.37543,'cal/mol/K','+|-',4.55226),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 314,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S} {6,[S,D,T,B,Q]}
5   O ux {2,[S,D,T,B,Q]}
6   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.00572,-1.19014,-3.29078,-4.6656,-5.5584,-6.2562,-6.22332],'cal/mol/K','+|-',[3,3,6.42861,8.62226,8.41447,8.13732,4.60854]),
        H298 = (90.0248,'kcal/mol','+|-',9.77143),
        S298 = (3.07192,'cal/mol/K','+|-',5.28234),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 315,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S} {6,[S,D,T,B,Q]}
5   O ux {2,[S,D,T,B,Q]} {7,S}
6   C ux {4,[S,D,T,B,Q]}
7   C u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.07461,-2.0819,-5.91392,-8.2058,-9.00894,-9.60608,-8.12276],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.8939,'kcal/mol','+|-',5.2),
        S298 = (4.86206,'cal/mol/K','+|-',4.87798),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 316,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R_Ext-5BrClFINOPSSi-R_Int-7R!H-6R!H_Ext-7R!H-R_Ext-8R!H-R_8R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S} {6,[S,D,T,B,Q]}
5   O ux r1 {2,[S,D,T,B,Q]} {7,S}
6   C ux r1 {4,[S,D,T,B,Q]}
7   C u0 r1 {5,S} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]} {9,S}
9   O u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.81762,-1.49961,-5.30293,-7.59039,-8.3629,-9.13046,-7.88513],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.6925,'kcal/mol','+|-',5.2),
        S298 = (3.13744,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]OCC(COO)(OO)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 317,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R_Ext-5BrClFINOPSSi-R_Int-7R!H-6R!H_Ext-7R!H-R_Ext-8R!H-R_N-8R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C ux r1 {1,S} {3,D} {5,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   O u0 r1 {1,S} {6,[S,D,T,B,Q]}
5   O ux r1 {2,[S,D,T,B,Q]} {7,S}
6   C ux r1 {4,[S,D,T,B,Q]}
7   C u0 r1 {5,S} {8,[S,D,T,B,Q]}
8   O ux {7,[S,D,T,B,Q]} {9,S}
9   O u0 r0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3316,-2.6642,-6.52491,-8.82121,-9.65498,-10.0817,-8.36039],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.0953,'kcal/mol','+|-',5.2),
        S298 = (6.58669,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(OO)CO[CH]C(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 318,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_N-4O-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,D} {5,S}
3   O ux r0 {2,D}
4   O ux r0 {1,S}
5   O u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.79755,1.31258,-1.19632,-2.75465,-4.02573,-5.43856,-7.02839],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (104.423,'kcal/mol','+|-',5.2),
        S298 = (2.22462,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1O[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 319,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0216495,-1.08138,-1.94029,-2.31848,-2.65226,-2.90022,-4.28527],'cal/mol/K','+|-',[3,4.10846,4.93425,4.97257,4.50059,4.03848,5.20224]),
        H298 = (98.9379,'kcal/mol','+|-',11.9542),
        S298 = (2.33018,'cal/mol/K','+|-',7.10043),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 320,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   R!H ux r0 {2,D}
4   R!H ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.300366,-0.548021,-1.3107,-1.74833,-2.2875,-2.66563,-3.75736],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.07,'kcal/mol','+|-',9.78601),
        S298 = (2.90428,'cal/mol/K','+|-',5.26742),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 321,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.495566,-0.455148,-1.2375,-1.54592,-1.92624,-2.11677,-3.0772],'cal/mol/K','+|-',[3,3.18044,3.43675,3.63255,3.80854,3.79028,3.38422]),
        H298 = (96.2485,'kcal/mol','+|-',5.2),
        S298 = (2.33957,'cal/mol/K','+|-',6.93269),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 322,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,S}
2   C u0 r0 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   C ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {1,S} {4,[S,D,T,B,Q]}
6   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.938977,0.359093,-0.368366,-0.586627,-0.748947,-0.793653,-1.86476],'cal/mol/K','+|-',[3,6.03921,7.58161,8.13932,8.32825,8.00331,6.92896]),
        H298 = (97.9743,'kcal/mol','+|-',5.2),
        S298 = (0.0167532,'cal/mol/K','+|-',14.3366),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 323,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-2R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,S}
2   C   u0 r0 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   C   ux r0 {2,D}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C   ux r1 {1,S} {4,[S,D,T,B,Q]}
6   C   u0 r0 {2,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
    index = 324,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux r0 {2,D} {6,[S,D,T,B,Q]}
4   C   ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C   ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
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
    index = 325,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   C   u0 {1,S} {5,S} {6,S}
5   C   u0 {1,S} {4,S}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.69249,0.172426,-1.25802,-1.90405,-2.53192,-2.75203,-3.88112],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.2102,'kcal/mol','+|-',5.77137),
        S298 = (3.31262,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 326,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-4R!H-R_6R!H->C",
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
        Cpdata = ([2.3102,0.843126,-0.748244,-1.56205,-2.48091,-2.87825,-4.23753],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.1697,'kcal/mol','+|-',5.2),
        S298 = (2.70119,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]1CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 327,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-4R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S} {5,S}
2   C                      u0 r0 {1,S} {3,D}
3   C                      u0 r0 {2,D}
4   C                      u0 r1 {1,S} {5,S} {6,S}
5   C                      u0 r1 {1,S} {4,S}
6   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.07478,-0.498275,-1.76779,-2.24604,-2.58293,-2.6258,-3.52472],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.2506,'kcal/mol','+|-',5.2),
        S298 = (3.92405,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C]1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 328,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   R!H ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.179923,-0.605326,-1.35586,-1.87322,-2.51041,-3.00429,-4.17703],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.011,'kcal/mol','+|-',9.83047),
        S298 = (3.25273,'cal/mol/K','+|-',4.30933),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 329,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,D}
3   O   u0 r0 {2,D}
4   R!H u0 r1 {1,S} {5,S} {6,[S,D,T,B,Q]}
5   R!H u0 r1 {1,[S,D,T,B,Q]} {4,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.50929,-0.265378,-1.76262,-2.76498,-3.77665,-4.15595,-4.62027],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.8284,'kcal/mol','+|-',5.2),
        S298 = (3.24228,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)C[C]1C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 330,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_4R!H->O",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O   ux r0 {2,D}
4   O   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.189767,-0.583567,-1.41769,-2.02475,-2.74699,-3.17209,-4.28517],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.8199,'kcal/mol','+|-',5.2),
        S298 = (2.25192,'cal/mol/K','+|-',4.22518),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 331,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   O   ux r0 {2,D}
4   O   ux {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0175556,-0.680636,-1.38424,-2.00713,-2.78825,-3.17542,-4.05635],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.4045,'kcal/mol','+|-',2.4),
        S298 = (2.62679,'cal/mol/K','+|-',4.62669),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 332,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_4R!H->O_Ext-2R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   O ux r0 {2,D}
4   O ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.148482,-0.931732,-1.64714,-2.17503,-2.62153,-2.90498,-3.8919],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.7538,'kcal/mol','+|-',2.4),
        S298 = (0.99101,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 333,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_4R!H->O_Ext-2R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   O ux r0 {2,D}
4   O ux r1 {1,S} {5,[S,D,T,B,Q]}
5   O ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.113371,-0.42954,-1.12134,-1.83922,-2.95497,-3.44587,-4.22081],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.0552,'kcal/mol','+|-',2.4),
        S298 = (4.26257,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 334,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_N-4R!H->O",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D}
3   O ux r0 {2,D}
4   C ux {1,S} {5,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0836007,-0.692873,-1.21361,-1.54462,-2.02138,-2.60912,-3.97932],'cal/mol/K','+|-',[3,3,3,3,3,3.03811,3]),
        H298 = (106.603,'kcal/mol','+|-',8.35007),
        S298 = (4.30319,'cal/mol/K','+|-',4.61216),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 335,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,D} {6,[S,D,T,B,Q]}
3   O   ux r0 {2,D}
4   C   ux {1,S} {5,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.323437,-0.901413,-1.3614,-1.64107,-2.07699,-2.68113,-4.05178],'cal/mol/K','+|-',[3,3,3,3,3.17123,3.61484,3]),
        H298 = (107.401,'kcal/mol','+|-',7.57994),
        S298 = (4.80958,'cal/mol/K','+|-',4.65662),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 336,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,D} {6,S}
3   O ux r0 {2,D}
4   C ux r1 {1,S} {5,[S,D,T,B,Q]}
5   C ux r1 {1,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
6   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.383725,-0.713504,-1.51362,-1.87153,-2.08295,-2.55768,-3.84323],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.789,'kcal/mol','+|-',5.2),
        S298 = (4.56458,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 337,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C u0 r0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O u0 r0 {2,D}
4   C u0 {1,S} {5,S}
5   C u0 {1,S} {4,S}
6   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.541025,-0.959231,-1.31456,-1.57015,-2.07515,-2.71911,-4.11594],'cal/mol/K','+|-',[3,3,3,3,4.33575,4.93644,3.84926]),
        H298 = (108.387,'kcal/mol','+|-',5.2),
        S298 = (4.88496,'cal/mol/K','+|-',6.34877),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 338,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   u0 r0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O   u0 r0 {2,D}
4   C   u0 r1 {1,S} {5,S}
5   C   u0 r1 {1,S} {4,S}
6   O   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
    index = 339,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-2R!H-R",
    group = 
"""
1 * C     u1 r1 {2,S} {4,S}
2   C     u0 r0 {1,S} {3,D} {5,S}
3   R!H   u0 r0 {2,D}
4   [C,O] u0 {1,S}
5   C     u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.14418,-6.67413,-8.83875,-9.04446,-7.90104,-6.95095,-11.0435],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.1711,'kcal/mol','+|-',5.2),
        S298 = (2.58717,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 340,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-2R!H-R_3R!H->C",
    group = 
"""
1 * C     u1 r1 {2,S} {4,S}
2   C     u0 r0 {1,S} {3,D} {5,S}
3   C     u0 r0 {2,D}
4   [C,O] u0 r1 {1,S}
5   C     u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.47647,-6.9194,-9.06614,-9.33503,-8.49338,-7.50308,-11.5083],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.2099,'kcal/mol','+|-',5.2),
        S298 = (3.15088,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)[C]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 341,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-2R!H-R_N-3R!H->C",
    group = 
"""
1 * C     u1 r1 {2,S} {4,S}
2   C     u0 r0 {1,S} {3,D} {5,S}
3   O     u0 r0 {2,D}
4   [C,O] u0 r1 {1,S}
5   C     u0 r0 {2,S}
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
    index = 342,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
4   C   ux {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.256698,-1.04256,-1.68557,-2.24737,-3.16095,-3.76815,-4.72359],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.043,'kcal/mol','+|-',9.62802),
        S298 = (1.27398,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 343,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
4   C   ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.232195,-1.02653,-1.67624,-2.24083,-3.1673,-3.78128,-4.73048],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.285,'kcal/mol','+|-',9.10466),
        S298 = (1.18484,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 344,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
4   C ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.436691,-0.89208,-1.42885,-1.9727,-2.84346,-3.49494,-4.4843],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.194,'kcal/mol','+|-',4.22765),
        S298 = (0.796905,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 345,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C u0 r1 {2,D}
4   C u0 {1,D} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.358894,-0.794939,-1.32686,-1.88412,-2.77259,-3.43763,-4.44879],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.169,'kcal/mol','+|-',5.68118),
        S298 = (0.597498,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 346,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   u0 r1 {2,D} {7,S}
4   C   u0 {1,D} {5,S}
5   C   u0 {4,S} {6,D}
6   O   ux {5,D}
7   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.347747,-0.726002,-1.21883,-1.79136,-2.74558,-3.43716,-4.43897],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (110.795,'kcal/mol','+|-',2.58372),
        S298 = (1.37865,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 347,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C u0 r1 {2,D} {7,S}
4   C u0 r1 {1,D} {5,S}
5   C u0 r1 {4,S} {6,D}
6   O ux r0 {5,D}
7   C u0 r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.330326,-0.690371,-1.19076,-1.7876,-2.7503,-3.44249,-4.43616],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.881,'kcal/mol','+|-',2.4),
        S298 = (1.48803,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=[C]C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 348,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,[S,D,T,B,Q]} {4,D}
2   C                      ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C                      u0 r1 {2,D} {7,S}
4   C                      u0 r1 {1,D} {5,S}
5   C                      u0 r1 {4,S} {6,D}
6   O                      ux r0 {5,D}
7   [F,I,P,Br,Cl,O,Si,S,N] u0 r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.365167,-0.761633,-1.2469,-1.79512,-2.74086,-3.43183,-4.44177],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (111.708,'kcal/mol','+|-',2.4),
        S298 = (1.26927,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=[C]C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 349,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_N-3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,[B,D,T,Q]}
2   C u0 {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.540419,-1.0216,-1.56483,-2.0908,-2.93794,-3.57136,-4.53165],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.227,'kcal/mol','+|-',2.4),
        S298 = (1.06278,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 350,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R",
    group = 
"""
1 * C u1 r1 {2,S} {4,[B,D,T,Q]}
2   C u0 {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.539656,-1.00455,-1.53667,-2.07018,-2.93787,-3.57703,-4.52737],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.425,'kcal/mol','+|-',3.07394),
        S298 = (1.09456,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 351,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R_Sp-6R!H-5C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[B,D,T,Q]}
2   C u0 r1 {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]} {6,S}
6   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.550222,-1.01015,-1.53813,-2.06521,-2.92134,-3.56029,-4.52754],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (112.338,'kcal/mol','+|-',2.4),
        S298 = (0.952538,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[C]=CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 352,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R_N-Sp-6R!H-5C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[B,D,T,Q]}
2   C u0 r1 {1,S} {3,D}
3   C ux r0 {2,D}
4   C ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   C u0 r0 {5,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.52909,-0.998943,-1.53521,-2.07515,-2.95441,-3.59377,-4.5272],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (114.512,'kcal/mol','+|-',2.4),
        S298 = (1.23659,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[C]=CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 353,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
4   C   ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.146723,-1.27566,-2.13464,-2.73768,-3.76737,-4.31184,-5.18665],'cal/mol/K','+|-',[3,3,3,3,3.5836,4.13,3.04001]),
        H298 = (120.416,'kcal/mol','+|-',10.0162),
        S298 = (1.90367,'cal/mol/K','+|-',4.0365),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 354,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[B,D,T,Q]}
2   C   u0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   R!H ux {2,D}
4   C   ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.583173,-1.23239,-2.26862,-2.97625,-4.23596,-4.88663,-5.7138],'cal/mol/K','+|-',[3,3,3,3,4.51621,5.11056,3.55128]),
        H298 = (119.831,'kcal/mol','+|-',14.4227),
        S298 = (1.47321,'cal/mol/K','+|-',3.34165),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 355,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[B,D,T,Q]}
2   C u0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
6   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.00625,-1.13365,-2.0836,-2.62404,-3.75649,-4.20759,-5.5508],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (112.122,'kcal/mol','+|-',5.2),
        S298 = (0.317014,'cal/mol/K','+|-',3.00498),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 356,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_3R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[B,D,T,Q]}
2   C   u0 r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   ux {2,D} {7,[S,D,T,B,Q]}
4   C   ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]}
6   O   ux r1 {2,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
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
    index = 357,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[B,D,T,Q]}
2   C   u0 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.322818,-1.29315,-2.38248,-3.19299,-4.53102,-5.3045,-5.81411],'cal/mol/K','+|-',[3.56781,3,3,4.22658,7.22176,8.09133,5.79501]),
        H298 = (122.538,'kcal/mol','+|-',12.7805),
        S298 = (2.18471,'cal/mol/K','+|-',3.31009),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 358,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_N-3R!H->C_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[B,D,T,Q]}
2   C   u0 r1 {1,S} {3,D} {6,[S,D,T,B,Q]}
3   O   ux {2,D}
4   C   ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O   ux r1 {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux r1 {2,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.06939,-1.14229,-3.42435,-5.26206,-8.06632,-9.26549,-8.65097],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.088,'kcal/mol','+|-',5.2),
        S298 = (3.80512,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OOC=[C]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 359,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r1 {2,D}
4   C ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
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
    index = 360,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_N-3R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,D,T,B,Q]} {4,[B,D,T,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C ux r0 {2,D}
4   C ux r1 {1,[B,D,T,Q]} {5,[S,D,T,B,Q]}
5   O ux r1 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.656988,-1.89317,-2.40726,-2.6254,-2.9958,-2.87645,-3.90047],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (123.875,'kcal/mol','+|-',5.2),
        S298 = (5.81522,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1[C]=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 361,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0740612,-1.13252,-2.11845,-2.74265,-3.46086,-4.04262,-5.35976],'cal/mol/K','+|-',[3,3.40063,3.95319,4.04007,3.72471,3.62193,4.58129]),
        H298 = (100.85,'kcal/mol','+|-',24.2014),
        S298 = (1.74483,'cal/mol/K','+|-',6.949),
    ),
    shortDesc = """Radical correction fitted to 208 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 362,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.331727,-1.19107,-1.93051,-2.43405,-3.11554,-3.6263,-4.52336],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (115.556,'kcal/mol','+|-',10.9462),
        S298 = (1.66352,'cal/mol/K','+|-',9.59079),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 363,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O",
    group = 
"""
1 * C u1 r1 {2,D}
2   C ux {1,D} {3,S}
3   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0444579,-1.30221,-2.27592,-2.82533,-3.46631,-3.86066,-4.64472],'cal/mol/K','+|-',[3,3.15836,3.44884,3.3065,3,3,3]),
        H298 = (120.467,'kcal/mol','+|-',7.92516),
        S298 = (0.019335,'cal/mol/K','+|-',6.70552),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 364,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   ux {1,D} {3,S}
3   O   u0 {2,S}
4   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.101445,-1.07086,-2.03214,-2.5925,-3.26582,-3.71194,-4.51409],'cal/mol/K','+|-',[3,3,3.17509,3.04772,3,3,3]),
        H298 = (121.24,'kcal/mol','+|-',5.2),
        S298 = (-0.442076,'cal/mol/K','+|-',6.22434),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 365,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   ux {1,D} {3,S}
3   O   u0 {2,S}
4   R!H u0 {1,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.312134,-0.748779,-1.68592,-2.25482,-2.99335,-3.50656,-4.36384],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (120.822,'kcal/mol','+|-',5.2),
        S298 = (-1.14762,'cal/mol/K','+|-',4.33603),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 366,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   ux {1,D} {3,S}
3   O   u0 {2,S}
4   R!H u0 {1,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.843639,-0.520172,-1.68031,-2.39041,-3.24884,-3.69001,-4.77581],'cal/mol/K','+|-',[3,3.40511,4.04434,3.7846,3.23781,3,3]),
        H298 = (121.086,'kcal/mol','+|-',5.2),
        S298 = (0.392861,'cal/mol/K','+|-',4.058),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 367,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   ux r1 {1,D} {3,S} {6,[S,D,T,B,Q]}
3   O   u0 {2,S}
4   R!H u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.42425,0.732485,-0.19413,-1.00471,-2.06121,-2.82771,-4.35071],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (121.64,'kcal/mol','+|-',2.4),
        S298 = (1.76856,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CO[C]=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 368,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   u0 r1 {1,D} {3,S}
3   O   u0 r1 {2,S} {7,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {5,S} {6,S}
5   C   u0 {4,S}
6   R!H u0 {4,S}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.367395,-1.93127,-3.45988,-4.15807,-4.72555,-4.63719,-5.74934],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (120.021,'kcal/mol','+|-',5.2),
        S298 = (-2.05108,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)[C]=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 369,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,D} {4,S}
2   C ux {1,D} {3,S}
3   O u0 {2,S}
4   C u0 {1,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.118132,-0.933841,-1.69047,-2.14505,-2.78653,-3.35805,-4.03034],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (120.592,'kcal/mol','+|-',5.2),
        S298 = (-2.39468,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 370,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   ux r1 {1,D} {3,S}
3   O   u0 r1 {2,S} {6,[S,D,T,B,Q]}
4   C   u0 r1 {1,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.243073,-0.613677,-1.57505,-2.05821,-2.54345,-3.25626,-3.9821],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (121.195,'kcal/mol','+|-',5.2),
        S298 = (-4.30338,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[C]=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 371,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C u1 r1 {2,D} {4,S}
2   C u0 {1,D} {3,S} {6,S}
3   O u0 {2,S}
4   C u0 {1,S} {5,S}
5   O u0 {4,S}
6   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0535583,-1.06491,-1.73886,-2.09443,-2.70293,-3.15842,-3.42419],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (120.19,'kcal/mol','+|-',6.94446),
        S298 = (-2.91921,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 372,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,S}
2   C   u0 r1 {1,D} {3,S} {6,S}
3   O   u0 r1 {2,S}
4   C   u0 r1 {1,S} {5,S}
5   O   u0 r1 {4,S}
6   C   u0 r0 {2,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.332765,-1.30164,-1.86896,-2.14051,-2.70578,-3.08111,-2.72812],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (122.646,'kcal/mol','+|-',5.2),
        S298 = (-3.22109,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC1=[C]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 373,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O",
    group = 
"""
1 * C u1 r1 {2,D}
2   C ux {1,D} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.480203,-1.13364,-1.75199,-2.23183,-2.93424,-3.50516,-4.46063],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (113.737,'kcal/mol','+|-',9.74038),
        S298 = (2.51332,'cal/mol/K','+|-',10.6691),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 374,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   ux {1,D} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.479308,-1.11473,-1.71599,-2.18158,-2.87453,-3.44566,-4.41306],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (114.476,'kcal/mol','+|-',9.53168),
        S298 = (2.65451,'cal/mol/K','+|-',11.6203),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 375,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Int-4R!H-1R",
    group = 
"""
1 * C u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C ux {1,D} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.523862,-1.15155,-1.72882,-2.20193,-2.89306,-3.39976,-4.25247],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.97,'kcal/mol','+|-',5.2),
        S298 = (4.32698,'cal/mol/K','+|-',19.3555),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 376,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Int-4R!H-1R_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C   ux {1,D} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C   u0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   R!H u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.391693,-1.17473,-1.80248,-2.23467,-2.75428,-3.09987,-3.78974],'cal/mol/K','+|-',[3,3,3,3,3,3,3.31174]),
        H298 = (112.712,'kcal/mol','+|-',9.87109),
        S298 = (8.8126,'cal/mol/K','+|-',34.7322),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 377,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Int-4R!H-1R_Ext-3C-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C ux r1 {1,D} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C u0 r1 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   C u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.258337,-1.15538,-2.02421,-2.37336,-2.31455,-2.09081,-2.16853],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (118.466,'kcal/mol','+|-',5.2),
        S298 = (25.8152,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C1C=[C]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 378,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Int-4R!H-1R_Ext-3C-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C                      ux r1 {1,D} {3,S}
3   C                      u0 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C                      u0 r1 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.680595,-1.18333,-1.70393,-2.17303,-2.94972,-3.54834,-4.51028],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (111.486,'kcal/mol','+|-',2.4),
        S298 = (1.25588,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1C=[C]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 379,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Int-4R!H-1R_Ext-2R!H-R",
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
    index = 380,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,D} {6,S}
2   C ux {1,D} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.267535,-0.945497,-1.54167,-1.98962,-2.76396,-3.41187,-4.51086],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (110.071,'kcal/mol','+|-',2.4),
        S298 = (1.27962,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 381,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Ext-1R-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,D} {6,S}
2   C   ux r1 {1,D} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux r1 {4,[S,D,T,B,Q]}
6   C   u0 r1 {1,S}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.231261,-1.01079,-1.63325,-2.02327,-2.72966,-3.37378,-4.53761],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.466,'kcal/mol','+|-',2.4),
        S298 = (1.23246,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C=[C]CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 382,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   u0 {1,D} {3,S}
3   C   u0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.793418,-1.31464,-1.82745,-2.28057,-2.98269,-3.59708,-4.52375],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (119.921,'kcal/mol','+|-',2.4),
        S298 = (1.81666,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 383,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Ext-3C-R_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   u0 r1 {1,D} {3,S} {6,[S,D,T,B,Q]}
3   C   u0 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.945903,-1.50027,-1.99414,-2.39158,-2.97246,-3.59507,-4.54017],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (119.938,'kcal/mol','+|-',2.4),
        S298 = (1.93783,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=[C]OC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 384,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,D} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,D} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18229,-2.44372,-3.27427,-3.68768,-4.1836,-4.55376,-5.1639],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (106.276,'kcal/mol','+|-',5.2),
        S298 = (2.89133,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=[C]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 385,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   R!H ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.123104,-1.12544,-2.14117,-2.77995,-3.50259,-4.09293,-5.46085],'cal/mol/K','+|-',[3,3.54478,4.12349,4.21701,3.89215,3.79471,4.78892]),
        H298 = (98.9052,'kcal/mol','+|-',22.7656),
        S298 = (1.75465,'cal/mol/K','+|-',6.60325),
    ),
    shortDesc = """Radical correction fitted to 188 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 386,
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
        Cpdata = ([0.327346,-1.04782,-2.16013,-2.78351,-3.48461,-4.08255,-5.62987],'cal/mol/K','+|-',[3.05981,3.64317,4.17166,4.13182,3.62465,3.42274,4.95376]),
        H298 = (101.387,'kcal/mol','+|-',8.75011),
        S298 = (1.38715,'cal/mol/K','+|-',7.26719),
    ),
    shortDesc = """Radical correction fitted to 106 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 387,
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
        Cpdata = ([-0.34045,-1.01713,-1.70544,-2.21303,-2.94439,-3.52266,-4.42462],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (104.916,'kcal/mol','+|-',5.2),
        S298 = (1.34691,'cal/mol/K','+|-',3.50711),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 388,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.453793,-1.27736,-2.02964,-2.53584,-3.16875,-3.61791,-4.29204],'cal/mol/K','+|-',[2.8453,2.7653,2.86261,2.78026,2.74607,2.95754,2.80297]),
        H298 = (103.562,'kcal/mol','+|-',3.32951),
        S298 = (0.66147,'cal/mol/K','+|-',3.74415),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 389,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.076603,-1.42292,-2.54078,-3.2372,-4.03385,-4.49922,-4.93942],'cal/mol/K','+|-',[2,2,3.42186,4.31196,4.40947,3.83154,2]),
        H298 = (105.165,'kcal/mol','+|-',3.65896),
        S298 = (2.04843,'cal/mol/K','+|-',5.86292),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 390,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H u0 r1 {1,S} {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.685186,-2.14048,-4.51629,-5.72647,-6.57826,-6.70981,-5.89496],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (106.799,'kcal/mol','+|-',2.4),
        S298 = (5.19163,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OCC1O[C]1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 391,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_4R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
3   R!H ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.527452,-1.13845,-1.57003,-1.96297,-2.68866,-3.3223,-4.45812],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (105.508,'kcal/mol','+|-',2.4),
        S298 = (1.56477,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 392,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,S}
2   C   u0 {1,S} {3,S} {4,S}
3   R!H ux {1,[S,D,T,B,Q]} {2,S}
4   O   u0 {2,S}
5   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.642388,-1.20458,-1.77407,-2.18517,-2.7362,-3.17725,-3.96835],'cal/mol/K','+|-',[3.42589,3.39589,2.73625,2,2,2.30799,3.15692]),
        H298 = (102.761,'kcal/mol','+|-',2.4),
        S298 = (-0.0320084,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 393,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,S}
2   C u0 {1,S} {3,S} {4,S}
3   O ux {1,[S,D,T,B,Q]} {2,S}
4   O u0 {2,S}
5   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.15613,-1.61836,-1.99802,-2.1979,-2.43888,-2.7005,-3.41873],'cal/mol/K','+|-',[3.32134,3.70862,3.28953,2.2693,2,2.17793,3.31938]),
        H298 = (102.364,'kcal/mol','+|-',2.4),
        S298 = (-0.081956,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 394,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_5R!H->C_Ext-5C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   ux r1 {1,[S,D,T,B,Q]} {2,S}
4   O   u0 r0 {2,S}
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
    index = 395,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_5R!H->C_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S} {5,S}
2   C   u0 {1,S} {3,S} {4,S}
3   O   u0 {1,S} {2,S}
4   O   u0 {2,S} {6,S}
5   C   u0 {1,S}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.524585,-1.06491,-1.57786,-2.05509,-2.86959,-3.47598,-4.30824],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.986,'kcal/mol','+|-',2.4),
        S298 = (0.517071,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 396,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_5R!H->C_Ext-4O-R_6R!H->C",
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
        Cpdata = ([-0.496479,-0.990016,-1.47603,-1.9179,-2.68065,-3.30039,-4.35659],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.086,'kcal/mol','+|-',2.4),
        S298 = (0.408039,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 397,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_5R!H->C_Ext-4O-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {3,S} {5,S}
2   C                      u0 r1 {1,S} {3,S} {4,S}
3   O                      u0 r1 {1,S} {2,S}
4   O                      u0 r0 {2,S} {6,S}
5   C                      u0 r0 {1,S}
6   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.552691,-1.1398,-1.67969,-2.19228,-3.05853,-3.65157,-4.25988],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.886,'kcal/mol','+|-',2.4),
        S298 = (0.626104,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 398,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,S}
2   C   u0 {1,S} {3,S} {4,S}
3   R!H ux {1,[S,D,T,B,Q]} {2,S}
4   O   u0 {2,S}
5   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.385101,-0.377002,-1.32618,-2.1597,-3.33083,-4.13076,-5.0676],'cal/mol/K','+|-',[3.59458,2.8601,2,2,2,2,2]),
        H298 = (103.553,'kcal/mol','+|-',2.4),
        S298 = (0.0678869,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 399,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_N-5R!H->C_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   C ux r1 {1,[S,D,T,B,Q]} {2,S}
4   O u0 r0 {2,S}
5   O u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.885775,-1.3882,-1.89242,-2.36641,-3.13271,-3.69863,-4.53425],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.404,'kcal/mol','+|-',2.4),
        S298 = (-0.342911,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 400,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_N-5R!H->C_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]} {5,S}
2   C u0 r1 {1,S} {3,S} {4,S}
3   O ux r1 {1,[S,D,T,B,Q]} {2,S}
4   O u0 r0 {2,S}
5   O u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.65598,0.634195,-0.759943,-1.95299,-3.52895,-4.56288,-5.60095],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.703,'kcal/mol','+|-',2.4),
        S298 = (0.478685,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 401,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.460377,-1.18307,-1.81175,-2.29311,-3.08175,-3.68041,-4.6001],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.476,'kcal/mol','+|-',2.4),
        S298 = (3.72827,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 402,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_3R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   C   u0 r1 {1,S} {2,S} {5,[S,D,T,B,Q]}
4   R!H u0 r0 {2,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.17388,-2.01085,-2.71466,-3.19285,-3.91632,-4.40135,-5.00618],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (108.638,'kcal/mol','+|-',2.4),
        S298 = (4.35064,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 403,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_3R!H->C_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0632128,-0.457259,-1.08836,-1.65785,-2.58697,-3.28774,-4.37517],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (110.34,'kcal/mol','+|-',2.4),
        S298 = (3.24501,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C(O)C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 404,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_3R!H->C_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.270461,-1.08111,-1.63223,-2.02864,-2.74196,-3.35213,-4.41893],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.449,'kcal/mol','+|-',2.4),
        S298 = (3.58917,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 405,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.185215,-0.697643,-1.34131,-1.85915,-2.67087,-3.37299,-4.49965],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (104.74,'kcal/mol','+|-',5.2),
        S298 = (1.23721,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 406,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_4R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {3,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {1,S} {2,S}
4   R!H u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.554731,-0.642861,-2.05548,-2.57805,-3.10826,-4.30081,-3.77339],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.638,'kcal/mol','+|-',5.2),
        S298 = (3.40577,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O1[C]2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 407,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.165767,-0.700526,-1.30373,-1.82131,-2.64785,-3.32416,-4.53787],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (104.587,'kcal/mol','+|-',5.2),
        S298 = (1.12307,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 408,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.139752,-0.80917,-1.43915,-1.96711,-2.79617,-3.41041,-4.36269],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.682,'kcal/mol','+|-',2.4),
        S298 = (1.38774,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 409,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C   ux r0 {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.389976,-1.04439,-1.4662,-1.80431,-2.42817,-2.9767,-4.05313],'cal/mol/K','+|-',[2,2,2,2,2.05259,2,2]),
        H298 = (104.326,'kcal/mol','+|-',2.4),
        S298 = (1.15884,'cal/mol/K','+|-',2.89884),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 410,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-2R!H-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,S}
3   O   ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C   ux r0 {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H u0 r0 {2,S}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 411,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-2R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.395434,-1.04683,-1.61998,-2.12238,-2.94391,-3.56506,-4.52883],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.432,'kcal/mol','+|-',2.4),
        S298 = (1.69108,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 412,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-2R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]}
5   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.424774,-1.65237,-2.24149,-2.55445,-3.09431,-3.5395,-4.3654],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.833,'kcal/mol','+|-',2.4),
        S298 = (2.26691,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(OO)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 413,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-4C-R",
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
        Cpdata = ([0.328333,-0.415724,-1.38936,-2.21146,-3.33648,-4.02553,-4.75123],'cal/mol/K','+|-',[2.53233,2,2,2,2,2,2]),
        H298 = (105.195,'kcal/mol','+|-',2.4),
        S298 = (1.73587,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 414,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-4C-R_5R!H->C",
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
    index = 415,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {3,S}
2   C                      u0 r1 {1,S} {3,S} {4,S}
3   O                      u0 r1 {1,S} {2,S}
4   C                      u0 r0 {2,S} {5,S}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,S}
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
    index = 416,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.229621,-0.433855,-0.971333,-1.46344,-2.28379,-3.11245,-4.96786],'cal/mol/K','+|-',[3,3,3,3,3,3,4.73202]),
        H298 = (104.328,'kcal/mol','+|-',5.2),
        S298 = (0.473441,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 417,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_N-4R!H->C_Ext-4O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O   ux r0 {2,[S,D,T,B,Q]} {5,S}
5   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.643022,-0.786022,-1.47748,-2.05734,-2.82842,-3.63356,-5.61907],'cal/mol/K','+|-',[3,3,3,3,3,3,6.81921]),
        H298 = (105.386,'kcal/mol','+|-',5.2),
        S298 = (1.21098,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 418,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_N-4R!H->C_Ext-4O-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O ux r0 {2,[S,D,T,B,Q]} {5,S}
5   C u0 r0 {4,S}
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
    index = 419,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_N-4R!H->C_Ext-4O-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {3,[S,D,T,B,Q]}
2   C                      ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O                      ux r1 {1,[S,D,T,B,Q]} {2,[S,T,Q,B]}
4   O                      ux r0 {2,[S,D,T,B,Q]} {5,S}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.30405,-0.800975,-1.91184,-2.62024,-3.02395,-4.19519,-8.95732],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.006,'kcal/mol','+|-',5.2),
        S298 = (2.32099,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 420,
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
        Cpdata = ([-0.22675,-2.17317,-3.87315,-4.80326,-5.26318,-5.71164,-9.23749],'cal/mol/K','+|-',[3.49424,4.71013,5.45686,5.70763,5.49032,5.35112,4.60906]),
        H298 = (96.9666,'kcal/mol','+|-',6.22304),
        S298 = (3.54417,'cal/mol/K','+|-',10.7371),
    ),
    shortDesc = """Radical correction fitted to 23 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 421,
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
        Cpdata = ([-0.344595,-2.12971,-3.71678,-4.58719,-5.05812,-5.50501,-9.19255],'cal/mol/K','+|-',[3.40868,4.93009,5.58064,5.66404,5.34972,5.13555,4.80338]),
        H298 = (96.3364,'kcal/mol','+|-',5.2),
        S298 = (3.26041,'cal/mol/K','+|-',10.95),
    ),
    shortDesc = """Radical correction fitted to 21 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 422,
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
        Cpdata = ([-0.135734,-1.69569,-3.16805,-4.02567,-4.6416,-5.2444,-9.00766],'cal/mol/K','+|-',[3,3.94089,4.26471,4.413,4.87188,5.15496,3.95721]),
        H298 = (96.4894,'kcal/mol','+|-',5.2),
        S298 = (2.40345,'cal/mol/K','+|-',10.9046),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 423,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.680988,-2.15346,-3.34324,-3.96974,-4.40368,-4.97053,-8.86114],'cal/mol/K','+|-',[3,3.22643,4.33493,5.07832,6.19997,6.79577,4.18305]),
        H298 = (95.7308,'kcal/mol','+|-',5.2),
        S298 = (3.07926,'cal/mol/K','+|-',12.1742),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 424,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_4R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   R!H ux r1 {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   u0 {1,S} {7,S}
7   O   u0 {3,[S,D,T,B,Q]} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36196,-3.63121,-5.0938,-5.90021,-7.12359,-8.65182,-8.66062],'cal/mol/K','+|-',[3,3,3.41582,3.29354,3,3,3]),
        H298 = (96.1572,'kcal/mol','+|-',6.80177),
        S298 = (8.39483,'cal/mol/K','+|-',8.00498),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 425,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_4R!H-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   R!H ux r1 {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   u0 r1 {1,S} {7,S}
7   O   u0 r1 {3,[S,D,T,B,Q]} {6,S}
8   R!H ux {1,[S,D,T,B,Q]}
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
    index = 426,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   C ux r0 {2,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
6   C ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.510744,-1.78403,-2.9056,-3.48712,-3.7237,-4.05021,-8.91127],'cal/mol/K','+|-',[3,3.04761,4.25629,5.12682,6.17514,6.30801,4.73467]),
        H298 = (95.6242,'kcal/mol','+|-',5.2),
        S298 = (1.75037,'cal/mol/K','+|-',11.876),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 427,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   C ux r0 {2,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
6   C ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
8   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.847417,-2.03329,-2.98537,-3.48609,-3.60472,-3.89207,-8.85821],'cal/mol/K','+|-',[3,3.38824,5.01984,6.06045,7.26871,7.42397,5.57731]),
        H298 = (94.5916,'kcal/mol','+|-',5.2),
        S298 = (1.43494,'cal/mol/K','+|-',13.921),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 428,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-8R!H-R",
    group = 
"""
1 * C u1 r1 {2,S} {6,S} {8,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   C ux r0 {2,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
6   C u0 {1,S} {7,S}
7   O u0 {3,[S,D,T,B,Q]} {6,S}
8   C ux {1,[S,D,T,B,Q]} {9,S}
9   O u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.67312,-1.60444,-1.84538,-1.97182,-1.48441,-1.5973,-7.16109],'cal/mol/K','+|-',[3,6.39578,9.83544,11.8307,13.8485,13.9972,10.3846]),
        H298 = (93.9428,'kcal/mol','+|-',8.442),
        S298 = (-3.52164,'cal/mol/K','+|-',23.8996),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 429,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-8R!H-R_Ext-4R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {6,S} {8,[S,D,T,B,Q]}
2    C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3    O   ux r1 {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4    C   ux r0 {2,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
5    C   ux r0 {2,[S,D,T,B,Q]}
6    C   u0 r1 {1,S} {7,S}
7    O   u0 r1 {3,[S,D,T,B,Q]} {6,S}
8    C   ux {1,[S,D,T,B,Q]} {9,S}
9    O   u0 r0 {8,S}
10   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.66537,0.656808,1.63197,2.21096,3.41177,3.35144,-3.48956],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.9581,'kcal/mol','+|-',5.2),
        S298 = (-11.9714,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(CO)OOC[C]1COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 430,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   C   ux r0 {2,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
8   C   ux {1,[S,D,T,B,Q]}
9   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0263077,-1.85129,-3.18274,-3.89674,-4.33233,-4.78013,-9.62257],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.7601,'kcal/mol','+|-',5.2),
        S298 = (2.75914,'cal/mol/K','+|-',4.41785),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 431,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-4R!H-R_9R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {6,S} {8,S}
2   C u0 r1 {1,S} {3,S} {4,S} {5,S}
3   O u0 r1 {2,S} {7,S}
4   C u0 r0 {2,S} {9,S}
5   C u0 r0 {2,S}
6   C u0 r1 {1,S} {7,S}
7   O u0 r1 {3,S} {6,S}
8   C u0 r0 {1,S}
9   C u0 r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.528026,-2.65665,-4.26276,-5.07629,-5.39422,-5.60349,-10.0231],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.9558,'kcal/mol','+|-',5.2),
        S298 = (5.11087,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC1(C)OOC[C]1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 432,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-4R!H-R_N-9R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   C ux r0 {2,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
5   C ux {2,[S,D,T,B,Q]}
6   C ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
8   C ux {1,[S,D,T,B,Q]}
9   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.224551,-1.44861,-2.64273,-3.30696,-3.80139,-4.36845,-9.42231],'cal/mol/K','+|-',[3.58125,3,3,3,3,3.02805,3.43881]),
        H298 = (94.6622,'kcal/mol','+|-',5.2),
        S298 = (1.58328,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 433,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-4R!H-R_N-9R!H->C_Ext-9BrClFINOPSSi-R",
    group = 
"""
1  * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2    C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3    O   ux r1 {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4    C   ux r0 {2,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
5    C   ux {2,[S,D,T,B,Q]}
6    C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    O   ux r1 {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
8    C   ux {1,[S,D,T,B,Q]}
9    O   ux {4,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
10   R!H ux {9,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.49072,-0.851456,-2.64333,-3.81351,-4.69358,-5.43903,-10.6381],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.4693,'kcal/mol','+|-',5.2),
        S298 = (2.43849,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 434,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4   C   ux r0 {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux r1 {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0789673,-1.49041,-2.82725,-3.69782,-4.49849,-4.78893,-9.44418],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.6552,'kcal/mol','+|-',5.2),
        S298 = (3.74252,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)C1(C)[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 435,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.694502,-0.905315,-2.76578,-3.94054,-4.8423,-5.53402,-9],'cal/mol/K','+|-',[3.48031,4.84445,4.65081,3.9433,3,3,4.0547]),
        H298 = (97.7608,'kcal/mol','+|-',5.2),
        S298 = (2.46025,'cal/mol/K','+|-',8.79784),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 436,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-5R!H-R_Ext-8R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {4,S} {5,S}
3   R!H u0 {2,S}
4   R!H u0 {2,S}
5   R!H u0 {2,S} {8,S}
6   C   u0 {1,S} {7,S}
7   R!H u0 {6,S}
8   R!H ux {5,S} {9,S}
9   R!H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.6758,0.411941,-1.53147,-2.81798,-3.9988,-5.08442,-8.08554],'cal/mol/K','+|-',[3.18642,4.8025,4.80389,3.84964,3,3,4.65251]),
        H298 = (97.6927,'kcal/mol','+|-',5.2),
        S298 = (0.377869,'cal/mol/K','+|-',9.99915),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 437,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {4,S} {5,S}
3   R!H u0 {2,S}
4   R!H u0 {2,S}
5   C   u0 {2,S} {8,S}
6   C   u0 {1,S} {7,S}
7   R!H u0 {6,S}
8   R!H ux {5,S} {9,S}
9   R!H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.42347,1.16749,-0.841036,-2.24669,-3.51628,-4.50977,-8.5717],'cal/mol/K','+|-',[3,4.57115,4.81407,3.7943,3,3,5.1765]),
        H298 = (97.6206,'kcal/mol','+|-',5.2),
        S298 = (-1.49462,'cal/mol/K','+|-',8.11326),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 438,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_5R!H->C_Ext-1R-R",
    group = 
"""
1  * C     u1 r1 {2,S} {6,S} {10,S}
2    C     u0 r1 {1,S} {3,S} {4,S} {5,S}
3    [C,O] u0 {2,S}
4    [C,O] u0 {2,S}
5    C     u0 {2,S} {8,S}
6    C     u0 {1,S} {7,S}
7    O     u0 {6,S}
8    O     ux {5,S} {9,S}
9    O     u0 {8,S}
10   C     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.63056,2.10893,0.166519,-1.41563,-2.92456,-4.10942,-10.0135],'cal/mol/K','+|-',[3,4.52984,4.68897,3.49532,3,3,3]),
        H298 = (96.8872,'kcal/mol','+|-',5.2),
        S298 = (-3.46151,'cal/mol/K','+|-',6.22922),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 439,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_5R!H->C_Ext-1R-R_Ext-3R!H-R",
    group = 
"""
1  * C     u1 r1 {2,S} {6,S} {10,S}
2    C     u0 r1 {1,S} {3,S} {4,S} {5,S}
3    [C,O] u0 r0 {2,S} {11,[S,D,T,B,Q]}
4    [C,O] u0 r0 {2,S}
5    C     u0 r1 {2,S} {8,S}
6    C     u0 r0 {1,S} {7,S}
7    O     u0 r0 {6,S}
8    O     ux r1 {5,S} {9,S}
9    O     u0 r1 {8,S}
10   C     u0 r1 {1,S}
11   R!H   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.20046,3.71047,1.82432,-0.179845,-2.23814,-4.14033,-10.6938],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.1949,'kcal/mol','+|-',5.2),
        S298 = (-5.66387,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(OO)COOC[C]1COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 440,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_N-5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   O   u0 {2,S} {8,S}
6   C   u0 {1,S} {7,S}
7   R!H u0 {6,S}
8   R!H ux {5,S} {9,S}
9   R!H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.567201,-1.85471,-3.60277,-4.53185,-5.44636,-6.80837,-6.62705],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.9092,'kcal/mol','+|-',5.2),
        S298 = (5.99535,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(C)OC2OOC[C]21 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 441,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux r1 {6,[S,D,T,B,Q]}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.48615,-3.68141,-5.18241,-5.984,-6.22278,-6.61093,-10.8357],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.4927,'kcal/mol','+|-',5.2),
        S298 = (5.89114,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 442,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-7R!H-R_Int-8R!H-5R!H_3R!H-inRing",
    group = 
"""
1 * C     u1 r1 {2,S} {6,S}
2   C     u0 r1 {1,S} {3,S} {4,S} {5,S}
3   C     u0 r1 {2,S}
4   C     u0 {2,S}
5   C     u0 {2,S} {8,S}
6   C     u0 r1 {1,S} {7,S}
7   O     u0 r1 {6,S}
8   [C,O] u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.638783,-2.42596,-4.14065,-5.16845,-5.76073,-5.77399,-9.75031],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.3293,'kcal/mol','+|-',5.2),
        S298 = (4.93437,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC1(C)[CH]COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 443,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-7R!H-R_Int-8R!H-5R!H_N-3R!H-inRing",
    group = 
"""
1 * C     u1 r1 {2,S} {6,S}
2   C     u0 r1 {1,S} {3,S} {4,S} {5,S}
3   C     u0 r0 {2,S}
4   C     u0 {2,S}
5   C     u0 r1 {2,S} {8,S}
6   C     u0 r1 {1,S} {7,S}
7   O     u0 r1 {6,S}
8   [C,O] u0 r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.283238,-1.8776,-3.91148,-5.15942,-5.91743,-6.01555,-10.0718],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.7325,'kcal/mol','+|-',5.2),
        S298 = (4.88476,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1OOC[CH]C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 444,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_N-2R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r0 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux r1 {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.494847,-2.65049,-4.23201,-5.1808,-5.61591,-5.9558,-10.5265],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.1756,'kcal/mol','+|-',5.2),
        S298 = (-4.75226,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(OO)[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 445,
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
        Cpdata = ([-3.14492,-7.02145,-9.58141,-10.43,-9.34422,-8.34134,-13.0109],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.2472,'kcal/mol','+|-',5.2),
        S298 = (8.2862,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 446,
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
        Cpdata = ([-2.82918,-6.58001,-8.95621,-9.65627,-8.56848,-7.76876,-12.5257],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.3073,'kcal/mol','+|-',5.2),
        S298 = (9.15952,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OCOOC1(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 447,
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
        Cpdata = ([-3.46066,-7.46288,-10.2066,-11.2037,-10.12,-8.91393,-13.4961],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.1871,'kcal/mol','+|-',5.2),
        S298 = (7.41289,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OCOOC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 448,
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
        Cpdata = ([1.01063,-2.62953,-5.51509,-7.07203,-7.41633,-7.88125,-9.70939],'cal/mol/K','+|-',[4.77665,3,3,5.47416,7.08153,7.8253,3]),
        H298 = (103.584,'kcal/mol','+|-',8.80562),
        S298 = (6.52372,'cal/mol/K','+|-',7.7754),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 449,
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
        Cpdata = ([2.69943,-2.49861,-6.5524,-9.00744,-9.92003,-10.6479,-9.00628],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (106.697,'kcal/mol','+|-',5.2),
        S298 = (9.27274,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CO[CH]C(COO)(OO)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 450,
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
        Cpdata = ([-0.678177,-2.76044,-4.47778,-5.13662,-4.91263,-5.11459,-10.4125],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.471,'kcal/mol','+|-',5.2),
        S298 = (3.7747,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1O[CH]C(C)(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 451,
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
        Cpdata = ([0.705277,-0.59783,-1.83504,-2.43532,-3.25836,-4.01199,-5.52328],'cal/mol/K','+|-',[3,3.79163,4.60378,4.28468,3.41278,3,4.64638]),
        H298 = (99.6154,'kcal/mol','+|-',8.10725),
        S298 = (0.403703,'cal/mol/K','+|-',7.85927),
    ),
    shortDesc = """Radical correction fitted to 41 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 452,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.287976,-0.412157,-1.4043,-2.03963,-2.87239,-3.58566,-6.09474],'cal/mol/K','+|-',[3,3.54474,4.53741,4.5741,3.6396,3,5.36161]),
        H298 = (100.336,'kcal/mol','+|-',10.0319),
        S298 = (1.75412,'cal/mol/K','+|-',6.79432),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 453,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_4R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S}
4   R!H u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.266711,-0.82685,-1.76096,-2.21457,-2.90172,-3.73128,-5.57817],'cal/mol/K','+|-',[3,3,3,3,3,3,6.51096]),
        H298 = (96.658,'kcal/mol','+|-',24.8493),
        S298 = (0.589522,'cal/mol/K','+|-',11.873),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 454,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_4R!H-inRing_Ext-3O-R",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 r1 {2,S} {5,[S,D,T,B,Q]}
4   C u0 r1 {2,S}
5   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.16929,-0.716481,-1.42734,-1.77932,-2.55459,-3.45736,-4.3491],'cal/mol/K','+|-',[3,3,3,3,3,3.00154,3]),
        H298 = (95.5446,'kcal/mol','+|-',28.3041),
        S298 = (-0.151994,'cal/mol/K','+|-',13.5402),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 455,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_4R!H-inRing_Ext-3O-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S} {5,[S,D,T,B,Q]}
4   C   u0 r1 {2,S}
5   O   ux {3,[S,D,T,B,Q]}
6   C   u0 {1,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.389118,-0.300226,-1.05242,-1.70685,-2.85858,-3.86573,-4.87523],'cal/mol/K','+|-',[3,3,3,3,3,3.19162,3]),
        H298 = (99.5737,'kcal/mol','+|-',5.2),
        S298 = (2.68521,'cal/mol/K','+|-',4.63709),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 456,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_4R!H-inRing_Ext-3O-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S} {5,[S,D,T,B,Q]}
4   C   u0 r1 {2,S} {9,[S,D,T,B,Q]}
5   O   ux r1 {3,[S,D,T,B,Q]}
6   C   u0 r1 {1,S} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
9   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.484412,-1.15786,-2.27756,-2.82227,-4.02064,-5.42814,-6.00257],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.0692,'kcal/mol','+|-',5.2),
        S298 = (4.95523,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1C2CC=CC1OOC2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 457,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.417403,-0.315395,-1.32108,-1.9988,-2.86554,-3.55168,-6.21527],'cal/mol/K','+|-',[3,3.85171,4.94041,5.00434,3.93481,3,5.30612]),
        H298 = (101.08,'kcal/mol','+|-',5.34982),
        S298 = (2.02587,'cal/mol/K','+|-',5.56833),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 458,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.134827,-0.711721,-1.85224,-2.52628,-3.26623,-3.85964,-7.06526],'cal/mol/K','+|-',[3,4.37077,5.57339,5.66707,4.47432,3.27559,5.51199]),
        H298 = (99.5227,'kcal/mol','+|-',5.2),
        S298 = (2.13356,'cal/mol/K','+|-',6.66521),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 459,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux r0 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux {3,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.155435,-0.77107,-2.10252,-2.67343,-3.18709,-3.72482,-7.56715],'cal/mol/K','+|-',[3.10231,5.65366,7.30607,7.54137,6.06662,4.45703,6.25323]),
        H298 = (101.104,'kcal/mol','+|-',5.2),
        S298 = (1.56346,'cal/mol/K','+|-',7.70471),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 460,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux r0 {2,[S,D,T,B,Q]} {7,S}
5   O   ux {3,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   C   ux {4,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0109018,-1.39516,-3.04764,-3.41299,-3.34643,-3.66992,-8.2691],'cal/mol/K','+|-',[5.35393,8.27757,9.7997,10.394,8.70384,6.49443,6.76879]),
        H298 = (98.5595,'kcal/mol','+|-',5.2),
        S298 = (0.17331,'cal/mol/K','+|-',12.5835),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 461,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_Ext-1R-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S} {5,[S,D,T,B,Q]}
4   C   u0 r0 {2,S} {7,S}
5   O   ux r1 {3,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   C   ux {4,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.609427,-1.18039,-2.70336,-3.27525,-3.82628,-3.95378,-8.21318],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.2262,'kcal/mol','+|-',5.2),
        S298 = (1.79178,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 462,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {5,S}
4   O   ux r0 {2,[S,D,T,B,Q]} {7,S}
5   O   u0 {3,S}
6   R!H ux {1,[S,D,T,B,Q]}
7   C   u0 {4,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.288361,-1.50254,-3.21978,-3.48186,-3.10651,-3.52798,-8.29705],'cal/mol/K','+|-',[7.4283,11.6944,13.8332,14.6954,12.2528,9.15815,9.57154]),
        H298 = (99.2261,'kcal/mol','+|-',5.2),
        S298 = (-0.635923,'cal/mol/K','+|-',17.3486),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 463,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_Ext-1R-R_N-4R!H->C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {5,S}
4   O   ux r0 {2,[S,D,T,B,Q]} {7,S}
5   O   u0 r1 {3,S} {9,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   C   u0 r0 {4,S}
8   R!H ux {1,[S,D,T,B,Q]}
9   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.91466,-5.63715,-8.11055,-8.67749,-7.43854,-6.76588,-11.6811],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.8445,'kcal/mol','+|-',5.2),
        S298 = (5.49774,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OCOOC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 464,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux r0 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   O   ux r1 {3,[S,D,T,B,Q]}
6   R!H ux r1 {1,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
8   R!H ux {4,[S,D,T,B,Q]}
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
    index = 465,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S} {5,S}
4   C   u0 r0 {2,S} {7,[S,D,T,B,Q]}
5   O   u0 {3,S}
6   R!H u0 {1,S}
7   O   u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0506481,-0.533146,-1.67373,-2.50933,-3.36855,-3.94324,-6.66333],'cal/mol/K','+|-',[3,7.40252,10.7152,10.8635,8.48787,6.10718,10.7607]),
        H298 = (101.643,'kcal/mol','+|-',5.2),
        S298 = (3.46881,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 466,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S} {5,S}
4   C   u0 r0 {2,S} {7,[S,D,T,B,Q]}
5   O   u0 r1 {3,S} {8,[S,D,T,B,Q]}
6   R!H u0 r1 {1,S}
7   O   u0 r0 {4,[S,D,T,B,Q]}
8   R!H ux {5,[S,D,T,B,Q]}
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
    index = 467,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_N-4R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   O   ux r0 {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux r1 {3,[S,D,T,B,Q]}
6   R!H ux r1 {1,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 468,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_6R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   O   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.466726,-0.068315,-0.908134,-1.72049,-2.88261,-3.67034,-5.48808],'cal/mol/K','+|-',[3,3,3,3,3,3,4.03439]),
        H298 = (98.1753,'kcal/mol','+|-',5.2),
        S298 = (1.38279,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 469,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_6R!H->O_6O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S} {5,S}
4   R!H u0 r0 {2,S}
5   R!H u0 r1 {3,S}
6   O   u0 r1 {1,S}
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
    index = 470,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_6R!H->O_N-6O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   O   ux r0 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.408209,-0.197575,-1.11976,-1.98845,-3.1541,-3.91241,-6.18234],'cal/mol/K','+|-',[3,3.47525,4.03376,3.77516,3,3,5.46015]),
        H298 = (99.0514,'kcal/mol','+|-',5.2),
        S298 = (1.03259,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 471,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_6R!H->O_N-6O-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux r0 {2,[S,D,T,B,Q]}
5   R!H ux r1 {3,[S,D,T,B,Q]}
6   O   ux r0 {1,[S,D,T,B,Q]}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.9041,-1.89883,-3.09443,-3.83653,-4.26622,-4.39114,-8.85528],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.477,'kcal/mol','+|-',5.2),
        S298 = (2.15867,'cal/mol/K','+|-',3),
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
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_N-6R!H->O",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 r1 {2,S} {5,S}
4   C u0 r0 {2,S}
5   O u0 {3,S}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.862902,-2.23628,-3.41612,-4.13519,-4.64767,-4.93637,-9.33222],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.0678,'kcal/mol','+|-',5.2),
        S298 = (6.54981,'cal/mol/K','+|-',5.56365),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 473,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_N-6R!H->O_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r1 {2,S} {5,S}
4   C   u0 r0 {2,S}
5   O   u0 r1 {3,S}
6   C   u0 r1 {1,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31387,-3.07532,-4.38707,-4.9898,-5.15791,-5.35674,-9.67612],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.8382,'kcal/mol','+|-',5.2),
        S298 = (8.51686,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 474,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r1 {2,[S,T,Q,B]}
4   R!H ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.853737,0.170066,-0.652463,-1.31011,-2.38828,-3.20383,-4.44062],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.915,'kcal/mol','+|-',2.4),
        S298 = (2.43392,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 475,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]}
4   C ux r0 {2,[S,D,T,B,Q]}
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
CC1[CH]CO1 - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 476,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r1 {2,[S,T,Q,B]}
4   O ux r0 {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19872,1.02697,0.47018,-0.2924,-1.60773,-2.62599,-4.17917],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.071,'kcal/mol','+|-',2.4),
        S298 = (0.997299,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 477,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r0 {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.13417,-0.788662,-2.27775,-2.84201,-3.65506,-4.45016,-4.93595],'cal/mol/K','+|-',[3,4.09805,4.63392,3.93591,3.06901,3,3.5703]),
        H298 = (98.7183,'kcal/mol','+|-',5.2),
        S298 = (-0.984231,'cal/mol/K','+|-',8.08561),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 478,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H",
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
        Cpdata = ([1.33237,-1.20934,-2.96636,-3.29319,-3.7707,-4.51782,-4.28906],'cal/mol/K','+|-',[3,4.30512,4.65157,3.87617,3,3,3]),
        H298 = (100.033,'kcal/mol','+|-',5.2),
        S298 = (-2.71611,'cal/mol/K','+|-',7.53663),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 479,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,[S,T,Q,B]}
4   C   ux r1 {2,[S,D,T,B,Q]} {5,D} {6,[S,D,T,B,Q]}
5   R!H ux {4,D}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2963,3.51947,1.0109,0.108907,-1.09382,-2.4096,-3.67827],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.123,'kcal/mol','+|-',5.2),
        S298 = (-4.87982,'cal/mol/K','+|-',3),
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
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R",
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
        Cpdata = ([0.731047,-2.22064,-3.99715,-4.12102,-4.27057,-4.93394,-4.39355],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.7625,'kcal/mol','+|-',5.2),
        S298 = (-2.92921,'cal/mol/K','+|-',8.03069),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 481,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R",
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
        Cpdata = ([0.773656,-2.54304,-4.51701,-4.59013,-4.66545,-5.27642,-4.38487],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.4536,'kcal/mol','+|-',5.2),
        S298 = (-4.29414,'cal/mol/K','+|-',5.41854),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 482,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H",
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
        Cpdata = ([0.792444,-2.63513,-4.66333,-4.72802,-4.73441,-5.34316,-4.51715],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.9145,'kcal/mol','+|-',5.2),
        S298 = (-2.72509,'cal/mol/K','+|-',3.85642),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 483,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1  * C   u1 r1 {2,S} {11,[S,D,T,B,Q]}
2    C   ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3    O   ux r0 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4    C   ux {2,[S,D,T,B,Q]} {5,D}
5    C   ux {4,D} {10,[S,D,T,B,Q]}
6    O   ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C   ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8    C   ux {7,[S,D,T,B,Q]} {9,S}
9    C   ux {8,S}
10   R!H ux {5,[S,D,T,B,Q]}
11   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.624549,-2.84916,-5.02245,-5.14736,-5.13991,-5.70329,-4.76502],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.5118,'kcal/mol','+|-',5.2),
        S298 = (-3.8803,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 484,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-5R!H-R_Ext-1R-R_Ext-5R!H-R",
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
        Cpdata = ([1.09414,-1.88163,-4.11669,-4.81505,-5.38645,-5.88313,-5.67059],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.5491,'kcal/mol','+|-',5.2),
        S298 = (-4.53912,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC(OOCC(C)C)[CH]CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 485,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-5R!H-R_Ext-1R-R_Int-11R!H-10R!H_Ext-9R!H-R_Ext-12R!H-R_Ext-12R!H-R_Ext-9R!H-R",
    group = 
"""
1  * C   u1 r1 {2,S} {11,[S,D,T,B,Q]}
2    C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3    O   ux r0 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4    C   ux r1 {2,[S,D,T,B,Q]} {5,D}
5    C   ux r1 {4,D} {10,[S,D,T,B,Q]}
6    O   ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7    C   ux r1 {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]} {12,[S,D,T,B,Q]}
8    C   ux r1 {7,[S,D,T,B,Q]} {9,S}
9    C   ux r1 {8,S} {14,[S,D,T,B,Q]}
10   C   ux r1 {5,[S,D,T,B,Q]}
11   C   ux r1 {1,[S,D,T,B,Q]}
12   C   ux r1 {7,[S,D,T,B,Q]} {13,D}
13   C   u0 r1 {12,D}
14   R!H ux {9,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.181017,-3.57692,-5.79714,-5.66234,-5.4183,-6.0454,-4.69752],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.282,'kcal/mol','+|-',5.2),
        S298 = (-3.43547,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCC=CC1OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 486,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing",
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
        Cpdata = ([0.771222,-2.84765,-4.80123,-4.6608,-4.50612,-5.09108,-4.09804],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.5257,'kcal/mol','+|-',5.2),
        S298 = (-1.58133,'cal/mol/K','+|-',5.23468),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 487,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_Sp-10R!H-9R!H",
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
        Cpdata = ([0.880622,-2.92576,-5.06387,-4.96997,-4.68671,-5.2526,-4.44306],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.364,'kcal/mol','+|-',5.2),
        S298 = (-0.635021,'cal/mol/K','+|-',5.77163),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 488,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_Sp-10R!H-9R!H_Ext-10R!H-R_Ext-7R!H-R",
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
    index = 489,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_N-Sp-10R!H-9R!H",
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
        Cpdata = ([0.55242,-2.69142,-4.27593,-4.04246,-4.14495,-4.76804,-3.40801],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.8491,'kcal/mol','+|-',5.2),
        S298 = (-3.47395,'cal/mol/K','+|-',3),
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
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_N-7R!H-inRing",
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
        Cpdata = ([1.3598,-1.3555,-3.17224,-3.67165,-4.20275,-5.01903,-5.03087],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.2891,'kcal/mol','+|-',5.2),
        S298 = (-2.69074,'cal/mol/K','+|-',3),
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
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H",
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
        Cpdata = ([0.740778,-2.38187,-4.26095,-4.34882,-4.54478,-5.15963,-4.15338],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.397,'kcal/mol','+|-',5.2),
        S298 = (-7.03997,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 492,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 r0 {2,S} {6,S}
4   C u0 {2,S} {5,D}
5   C u0 {4,D}
6   O u0 {3,S} {7,[S,D,T,B,Q]}
7   C ux r1 {6,[S,D,T,B,Q]} {8,S}
8   C u0 {7,S} {9,[B,D,T,Q]}
9   C ux {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.719713,-2.63356,-4.56179,-4.61001,-4.61037,-5.33325,-4.39757],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.399,'kcal/mol','+|-',5.2),
        S298 = (-7.31728,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 493,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-1R-R",
    group = 
"""
1  * C   u1 r1 {2,S} {11,[S,D,T,B,Q]}
2    C   u0 r1 {1,S} {3,S} {4,S}
3    O   u0 r0 {2,S} {6,S}
4    C   u0 r1 {2,S} {5,D}
5    C   u0 r1 {4,D} {10,S}
6    O   u0 r0 {3,S} {7,[S,D,T,B,Q]}
7    C   ux r1 {6,[S,D,T,B,Q]} {8,S}
8    C   u0 r1 {7,S} {9,[B,D,T,Q]}
9    C   ux r1 {8,[B,D,T,Q]}
10   C   u0 r1 {5,S}
11   R!H ux {1,[S,D,T,B,Q]}
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
    index = 494,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_N-7R!H-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,S} {4,S}
3   O u0 r0 {2,S} {6,S}
4   C u0 {2,S} {5,D}
5   C u0 {4,D}
6   O u0 {3,S} {7,[S,D,T,B,Q]}
7   C ux r0 {6,[S,D,T,B,Q]} {8,S}
8   C u0 {7,S} {9,[B,D,T,Q]}
9   C ux {8,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.761842,-2.13019,-3.9601,-4.08762,-4.4792,-4.986,-3.9092],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.3951,'kcal/mol','+|-',5.2),
        S298 = (-6.76266,'cal/mol/K','+|-',3.67628),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 495,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_N-7R!H-inRing_Ext-7R!H-R_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1  * C   u1 r1 {2,S} {11,[S,D,T,B,Q]}
2    C   u0 r1 {1,S} {3,S} {4,S}
3    O   u0 r0 {2,S} {6,S}
4    C   u0 r1 {2,S} {5,D}
5    C   u0 r1 {4,D} {10,S}
6    O   u0 r0 {3,S} {7,[S,D,T,B,Q]}
7    C   ux r0 {6,[S,D,T,B,Q]} {8,S}
8    C   u0 {7,S} {9,[B,D,T,Q]}
9    C   ux {8,[B,D,T,Q]}
10   C   u0 r1 {5,S}
11   R!H ux {1,[S,D,T,B,Q]}
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
    index = 496,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r0 {2,S}
4   C   u0 r1 {2,S} {5,D}
5   C   u0 r1 {4,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.77757,2.26515,0.952011,0.172897,-1.07465,-1.7449,-2.01647],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.2251,'kcal/mol','+|-',5.2),
        S298 = (-4.54558,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC1=CC(O)[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 497,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {7,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r0 {2,S}
4   C   u0 r1 {2,S} {5,D}
5   C   u0 r1 {4,D} {6,S}
6   C   u0 r1 {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.02343,2.08863,0.503102,-1.2312,-4.10703,-5.61068,-6.20759],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.298,'kcal/mol','+|-',5.2),
        S298 = (1.80785,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C=CC(O)[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 498,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H",
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
        Cpdata = ([0.783503,-0.0443844,-1.05945,-2.04377,-3.45047,-4.33044,-6.08043],'cal/mol/K','+|-',[3,3.51965,3.7466,3.8311,3.65131,3.60897,4.87689]),
        H298 = (97.2027,'kcal/mol','+|-',5.2),
        S298 = (2.07986,'cal/mol/K','+|-',4.85299),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 499,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O ux r0 {2,[S,T,Q,B]}
4   C ux {2,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.127429,-1.4979,-2.80439,-4.07337,-5.43197,-6.40512,-8.96785],'cal/mol/K','+|-',[3,4.62757,4.18394,4.30547,5.44906,5.48578,3]),
        H298 = (95.0842,'kcal/mol','+|-',9.12819),
        S298 = (5.1177,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 500,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H->C_Ext-5C-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,[S,T,Q,B]}
4   C   ux r1 {2,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux r1 {4,[S,T,Q,B]} {6,S}
6   R!H u0 r1 {5,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00132,-3.13399,-4.28363,-5.59559,-7.3585,-8.34464,-8.40987],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.3115,'kcal/mol','+|-',5.2),
        S298 = (4.06577,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 501,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H->C",
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
        Cpdata = ([1.01858,0.330715,-0.609137,-1.52001,-2.93911,-3.79503,-5.33529],'cal/mol/K','+|-',[3,3.1168,3.32334,3.1375,3,3,4.22646]),
        H298 = (97.4836,'kcal/mol','+|-',5.2),
        S298 = (1.2959,'cal/mol/K','+|-',3.85109),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 502,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H->C_Ext-1R-R",
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
        Cpdata = ([0.753425,-0.0667889,-1.06342,-1.91998,-3.1892,-4.06316,-5.74056],'cal/mol/K','+|-',[3.0167,3.51746,3.67209,3.54124,3,3,5.05006]),
        H298 = (98.312,'kcal/mol','+|-',5.2),
        S298 = (1.82583,'cal/mol/K','+|-',4.24573),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 503,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H->C_Ext-1R-R_5O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,S} {4,S}
3   O   u0 r0 {2,S}
4   C   u0 {2,S} {5,S}
5   O   u0 r1 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.493088,-0.686328,-1.91395,-2.796,-3.99655,-4.79126,-6.6984],'cal/mol/K','+|-',[4.6151,4.71835,4.15467,3.7257,3,3,6.5568]),
        H298 = (99.3361,'kcal/mol','+|-',5.2),
        S298 = (2.69793,'cal/mol/K','+|-',5.274),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 504,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H->C_Ext-1R-R_5O-inRing_Ext-3O-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C   u0 r1 {1,S} {3,S} {4,S}
3   O   u0 r0 {2,S} {7,[S,D,T,B,Q]}
4   C   u0 r1 {2,S} {5,S}
5   O   u0 r1 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.76617,-2.99613,-3.9478,-4.61986,-5.34183,-5.89085,-9.90819],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.192,'kcal/mol','+|-',5.2),
        S298 = (5.27974,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1[CH]COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 505,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H->C_Ext-1R-R_N-5O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O   ux r0 {2,[S,T,Q,B]}
4   C   ux r1 {2,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   O   ux r0 {4,[S,T,Q,B]}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12947,0.828101,0.165127,-0.654617,-2.02301,-3.01145,-4.35702],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.0698,'kcal/mol','+|-',2.4),
        S298 = (0.566126,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1[CH]OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 506,
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
        Cpdata = ([1.31424,-1.0561,-2.15043,-2.75919,-3.35282,-3.77557,-4.76699],'cal/mol/K','+|-',[3.89442,3.94489,3.22915,3,3,3,3]),
        H298 = (98.4702,'kcal/mol','+|-',5.2),
        S298 = (1.64498,'cal/mol/K','+|-',5.73585),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 507,
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
        Cpdata = ([0.594834,-0.281535,-1.25899,-2.00703,-2.87527,-3.50278,-4.62831],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.0838,'kcal/mol','+|-',5.2),
        S298 = (6.14989,'cal/mol/K','+|-',4.06949),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 508,
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
        Cpdata = ([0.882311,0.237223,-0.570194,-1.28007,-2.31122,-3.11353,-4.37315],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.8269,'kcal/mol','+|-',5.2),
        S298 = (4.71111,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 509,
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
        Cpdata = ([1.39183,-1.16935,-2.24088,-2.78691,-3.29948,-3.66848,-4.71417],'cal/mol/K','+|-',[4.15679,4.17971,3.39271,3,3,3,3.12458]),
        H298 = (98.4617,'kcal/mol','+|-',5.2),
        S298 = (1.06139,'cal/mol/K','+|-',5.03908),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 510,
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
    index = 511,
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
        Cpdata = ([1.08108,-0.170605,-1.41976,-2.21999,-3.00841,-3.50129,-5.08041],'cal/mol/K','+|-',[4.83435,3.57335,3,3,3,3,4.80736]),
        H298 = (97.0606,'kcal/mol','+|-',5.2),
        S298 = (0.928831,'cal/mol/K','+|-',4.99276),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 512,
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
        Cpdata = ([2.52228,0.818719,-1.02848,-2.27859,-3.51143,-4.13497,-6.40894],'cal/mol/K','+|-',[3.50078,3.07363,3,3,3,3,5.89717]),
        H298 = (96.6927,'kcal/mol','+|-',5.2),
        S298 = (1.96891,'cal/mol/K','+|-',6.36347),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 513,
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
    index = 514,
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
        Cpdata = ([2.62974,0.545058,-1.69907,-2.61643,-3.4628,-3.57644,-4.8047],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.303,'kcal/mol','+|-',5.2),
        S298 = (1.285,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CC=CC1C1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 515,
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
        Cpdata = ([4.21646,2.47398,0.229417,-1.74727,-3.93945,-5.48934,-9.81182],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.3088,'kcal/mol','+|-',5.2),
        S298 = (-0.815252,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(OO)C1[CH]OC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 516,
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
        Cpdata = ([-1.41483,-1.90677,-2.24204,-2.41756,-2.49058,-2.85373,-3.70522],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.4171,'kcal/mol','+|-',2.4),
        S298 = (0.653162,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]CC=C1 - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 517,
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
        Cpdata = ([2.37326,0.767799,-0.743445,-1.59962,-2.66445,-3.05724,-4.18902],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.4908,'kcal/mol','+|-',5.2),
        S298 = (-1.57116,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)CC1[CH]CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 518,
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
        Cpdata = ([1.85866,-2.22932,-3.20523,-3.50461,-3.61309,-3.68678,-4.37008],'cal/mol/K','+|-',[4.42733,4.46042,3.75409,3.01375,3,3,3]),
        H298 = (98.987,'kcal/mol','+|-',5.2),
        S298 = (1.27317,'cal/mol/K','+|-',6.1319),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 519,
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
        Cpdata = ([2.30487,-3.07372,-4.11367,-4.08594,-3.62505,-3.47407,-3.65379],'cal/mol/K','+|-',[5.46376,4.04513,3,3,3,3,3]),
        H298 = (98.1593,'kcal/mol','+|-',5.2),
        S298 = (-1.31285,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 520,
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
        Cpdata = ([0.392715,-1.635,-3.12897,-3.36236,-3.22204,-3.31362,-3.83619],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.3757,'kcal/mol','+|-',5.2),
        S298 = (-2.0835,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 521,
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
        Cpdata = ([1.54784,-0.975523,-2.91934,-3.50512,-3.63396,-3.67547,-4.50178],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (97.3697,'kcal/mol','+|-',5.2),
        S298 = (-1.01465,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1C=CCC[C]1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 522,
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
        Cpdata = ([-0.270507,-1.89777,-2.98972,-2.87805,-2.36315,-2.37653,-2.62986],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.9155,'kcal/mol','+|-',5.2),
        S298 = (-2.45635,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)CC1[CH]CCC=C1C - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 523,
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
    index = 524,
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
        Cpdata = ([5.62809,-4.93389,-5.63479,-5.4667,-4.38553,-3.77158,-3.59088],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.5821,'kcal/mol','+|-',5.2),
        S298 = (0.426254,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC=CCCC1[CH]CCC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 525,
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
        Cpdata = ([4.16819,-5.39258,-5.47371,-5.35521,-5.10764,-4.69345,-4.3864],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.3897,'kcal/mol','+|-',5.2),
        S298 = (5.27827,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1[CH]CCC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 526,
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
    index = 527,
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
        Cpdata = ([0.729875,0.0744822,-0.690897,-1.31971,-2.2679,-3.04186,-4.33334],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.5365,'kcal/mol','+|-',2.4),
        S298 = (3.04595,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CCC(C)[CH]C1 - Radical thermo from pang.py and closed shell thermo from pang.py
""",
)

entry(
    index = 528,
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
    index = 529,
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
    index = 530,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_N-3R!H->O_Ext-1R-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {5,[S,D,T,B,Q]}
2   C                      ux {1,S} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C                      ux {2,[S,T,Q,B]}
4   C                      ux {2,[S,D,T,B,Q]}
5   R!H                    ux r1 {1,[S,D,T,B,Q]} {6,S}
6   [F,I,P,Br,Cl,O,Si,S,N] u0 r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.14318,-0.255309,-2.05637,-3.68833,-5.41475,-6.54316,-6.14038],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.484,'kcal/mol','+|-',5.2),
        S298 = (4.74467,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1[CH]COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 531,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.061132,-1.07967,-1.98165,-2.6569,-3.47313,-4.10469,-5.17043],'cal/mol/K','+|-',[3,3.03626,3.67809,3.96705,3.82346,3.76601,3.38413]),
        H298 = (97.1341,'kcal/mol','+|-',13.7811),
        S298 = (1.55571,'cal/mol/K','+|-',5.20018),
    ),
    shortDesc = """Radical correction fitted to 51 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 532,
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
        Cpdata = ([-0.0905741,-1.11233,-1.96691,-2.61186,-3.37013,-3.97452,-4.99367],'cal/mol/K','+|-',[3,3,3.5472,3.85098,3.6196,3.54107,3]),
        H298 = (97.1068,'kcal/mol','+|-',6.29952),
        S298 = (1.79458,'cal/mol/K','+|-',5.30491),
    ),
    shortDesc = """Radical correction fitted to 43 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 533,
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
        Cpdata = ([0.0347415,-1.0743,-1.99587,-2.70207,-3.54109,-4.19344,-5.28499],'cal/mol/K','+|-',[3,3,3.68866,4.04109,3.62964,3.39614,3.54906]),
        H298 = (98.3347,'kcal/mol','+|-',5.80852),
        S298 = (1.9563,'cal/mol/K','+|-',4.5044),
    ),
    shortDesc = """Radical correction fitted to 24 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 534,
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
        Cpdata = ([0.727676,-1.57555,-3.09152,-4.05729,-4.89072,-5.59772,-6.00166],'cal/mol/K','+|-',[3,4.15901,4.7123,5.06945,4.70553,4.56402,3]),
        H298 = (100.533,'kcal/mol','+|-',9.04648),
        S298 = (2.87101,'cal/mol/K','+|-',6.61069),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 535,
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
        Cpdata = ([1.02789,-1.92087,-3.71987,-4.79763,-5.62297,-6.35449,-6.09073],'cal/mol/K','+|-',[3,4.61221,4.77195,4.9863,4.5302,4.28738,3]),
        H298 = (99.7592,'kcal/mol','+|-',10.89),
        S298 = (3.70183,'cal/mol/K','+|-',6.86438),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 536,
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
        Cpdata = ([1.2832,-2.70943,-4.89472,-6.1897,-6.98015,-7.63201,-6.5432],'cal/mol/K','+|-',[3.06198,5.00843,4.04391,3.28394,3,3,3]),
        H298 = (103.883,'kcal/mol','+|-',5.83462),
        S298 = (5.55647,'cal/mol/K','+|-',5.08604),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 537,
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
        Cpdata = ([0.889172,-4.23446,-6.07628,-7.23725,-7.71556,-7.99306,-6.62463],'cal/mol/K','+|-',[3.96373,5.44855,3.77282,3,3,3,3]),
        H298 = (101.838,'kcal/mol','+|-',5.2),
        S298 = (7.40166,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 538,
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
        Cpdata = ([0.0209725,-2.5392,-5.01153,-6.85664,-7.99733,-8.83875,-7.49498],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.959,'kcal/mol','+|-',5.2),
        S298 = (7.00071,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1COC[C](COO)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 539,
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
        Cpdata = ([3.15697,-7.37692,-8.25434,-8.45772,-7.87513,-6.99172,-5.60119],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.253,'kcal/mol','+|-',5.2),
        S298 = (6.14956,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CO[CH]OC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 540,
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
        Cpdata = ([-0.510433,-2.78726,-4.96297,-6.39739,-7.27421,-8.14872,-6.77771],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.303,'kcal/mol','+|-',5.2),
        S298 = (9.0547,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 541,
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
        Cpdata = ([1.67723,-1.18439,-3.71315,-5.14214,-6.24475,-7.27095,-6.46178],'cal/mol/K','+|-',[3,3,3.14574,3.01873,3,3,3]),
        H298 = (105.927,'kcal/mol','+|-',5.58343),
        S298 = (3.71128,'cal/mol/K','+|-',3.85885),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 542,
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
        Cpdata = ([0.475571,-0.988731,-2.73786,-4.36605,-6.06207,-7.45311,-6.64156],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.722,'kcal/mol','+|-',5.2),
        S298 = (4.01967,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CC(OO)C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 543,
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
        Cpdata = ([2.27806,-1.28222,-4.2008,-5.53019,-6.33608,-7.17988,-6.37189],'cal/mol/K','+|-',[3,3.1625,3.7529,3.8225,3.19782,3,3]),
        H298 = (107.53,'kcal/mol','+|-',5.2),
        S298 = (3.55708,'cal/mol/K','+|-',5.4047),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 544,
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
        Cpdata = ([1.65899,-2.40034,-5.52765,-6.88165,-7.46668,-8.02464,-6.00854],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.824,'kcal/mol','+|-',5.2),
        S298 = (5.46794,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C1CC(=O)O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 545,
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
        Cpdata = ([2.89713,-0.164108,-2.87395,-4.17873,-5.20548,-6.33511,-6.73525],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.236,'kcal/mol','+|-',5.2),
        S298 = (1.64623,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1O[CH]OC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 546,
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
        Cpdata = ([2.32288,-0.02226,-2.47122,-3.62434,-4.59701,-5.7889,-7.00222],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.2521,'kcal/mol','+|-',5.2),
        S298 = (-1.04531,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC(=O)C(C)(C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 547,
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
        Cpdata = ([0.14512,-0.173681,-0.772171,-1.41374,-2.38123,-3.14479,-4.36888],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.132,'kcal/mol','+|-',2.4),
        S298 = (1.09855,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 548,
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
        Cpdata = ([-0.738506,-1.53556,-2.49783,-3.15718,-3.76377,-4.1167,-8.85156],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.079,'kcal/mol','+|-',5.2),
        S298 = (-0.82603,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)O[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 549,
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
        Cpdata = ([-0.263937,-0.858242,-1.52361,-2.11792,-2.95935,-3.58815,-4.97609],'cal/mol/K','+|-',[3,3,3,3,3,3,3.6845]),
        H298 = (97.6793,'kcal/mol','+|-',5.2),
        S298 = (1.56203,'cal/mol/K','+|-',3.1109),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 550,
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
        Cpdata = ([-0.196137,-0.864398,-1.59176,-2.20457,-3.029,-3.63921,-5.06821],'cal/mol/K','+|-',[3,3,3.02042,3.17777,3,3,4.00737]),
        H298 = (98.0959,'kcal/mol','+|-',5.2),
        S298 = (1.65029,'cal/mol/K','+|-',3.35169),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 551,
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
        Cpdata = ([-0.176027,-1.12536,-2.06282,-2.75251,-3.47979,-3.98626,-6.11912],'cal/mol/K','+|-',[3,3.043,4.48018,4.8525,3.78516,3,6.53226]),
        H298 = (96.4943,'kcal/mol','+|-',5.2),
        S298 = (2.65165,'cal/mol/K','+|-',3.04178),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 552,
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
        Cpdata = ([0.717718,-0.475791,-1.35679,-2.07642,-3.19634,-3.97104,-4.93218],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.7011,'kcal/mol','+|-',2.4),
        S298 = (4.52389,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC[C]1OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 553,
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
        Cpdata = ([-1.40776,-3.29864,-5.12449,-6.02437,-5.85848,-5.58382,-11.2714],'cal/mol/K','+|-',[3,3.45799,6.1309,6.86291,5.99068,4.60965,3.56315]),
        H298 = (96.0363,'kcal/mol','+|-',5.2),
        S298 = (2.80577,'cal/mol/K','+|-',3.46098),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 554,
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
        Cpdata = ([-1.9933,-2.07605,-2.9569,-3.59796,-3.74045,-3.95406,-10.0117],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.366,'kcal/mol','+|-',5.2),
        S298 = (1.58213,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC(OC(C)=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 555,
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
        Cpdata = ([0.321831,-0.159679,-0.836683,-1.46892,-2.44423,-3.20886,-4.42206],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.0193,'kcal/mol','+|-',2.4),
        S298 = (1.87083,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 556,
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
        Cpdata = ([-0.472755,-0.808818,-1.27349,-1.80388,-2.68441,-3.35885,-4.42326],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.9577,'kcal/mol','+|-',2.4),
        S298 = (1.42322,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1CO[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 557,
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
    index = 558,
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
        Cpdata = ([0.250244,-0.148367,-0.767907,-1.4359,-2.5153,-3.31632,-4.48484],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.5931,'kcal/mol','+|-',2.4),
        S298 = (0.540514,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 559,
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
        Cpdata = ([0.660377,0.336324,-0.253115,-0.941602,-2.10336,-3.00002,-4.37114],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.5195,'kcal/mol','+|-',2.4),
        S298 = (0.0992994,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 560,
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
        Cpdata = ([0.0451768,-0.390713,-1.0253,-1.68306,-2.72127,-3.47448,-4.54169],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.6299,'kcal/mol','+|-',2.4),
        S298 = (0.761121,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 561,
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
    index = 562,
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
        Cpdata = ([-0.0150817,-0.554435,-1.25306,-1.90486,-2.90491,-3.61956,-4.60401],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.8455,'kcal/mol','+|-',2.4),
        S298 = (1.11653,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC1O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 563,
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
        Cpdata = ([-0.233198,-1.64869,-2.95307,-3.7389,-4.49227,-4.92486,-5.26854],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (100.598,'kcal/mol','+|-',2.4),
        S298 = (4.56823,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 564,
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
        Cpdata = ([0.0108001,-0.29175,-0.793644,-1.38849,-2.39101,-3.17013,-4.396],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.2394,'kcal/mol','+|-',2.4),
        S298 = (0.679717,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 565,
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
        Cpdata = ([0.379266,0.0852996,-0.453652,-1.1053,-2.20778,-3.05779,-4.36345],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (96.9853,'kcal/mol','+|-',2.4),
        S298 = (0.608843,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1C[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 566,
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
        Cpdata = ([-0.357666,-0.6688,-1.13364,-1.67168,-2.57424,-3.28248,-4.42855],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.4934,'kcal/mol','+|-',2.4),
        S298 = (0.750591,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OC1O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 567,
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
        Cpdata = ([-0.754919,-0.902436,-1.18868,-1.69222,-2.58318,-3.29972,-4.45844],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.7638,'kcal/mol','+|-',2.4),
        S298 = (0.628512,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OCC1O[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 568,
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
        Cpdata = ([-0.255672,-1.16244,-1.92875,-2.49302,-3.1449,-3.68609,-4.60985],'cal/mol/K','+|-',[3,3,3.46684,3.69867,3.67055,3.75117,3]),
        H298 = (95.4449,'kcal/mol','+|-',5.50708),
        S298 = (1.58151,'cal/mol/K','+|-',6.33357),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 569,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H u0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.256768,-1.3966,-2.26018,-2.82073,-3.30561,-3.76318,-4.63655],'cal/mol/K','+|-',[3,3.3707,4.1539,4.46872,4.56333,4.70735,3]),
        H298 = (94.9477,'kcal/mol','+|-',6.98052),
        S298 = (2.54074,'cal/mol/K','+|-',7.24809),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 570,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,S}
5   R!H u0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.281852,-3.87135,-5.48321,-6.32411,-6.4885,-6.65886,-5.83581],'cal/mol/K','+|-',[4.26399,3.02788,3,3,3,3,3]),
        H298 = (99.539,'kcal/mol','+|-',6.92549),
        S298 = (6.20321,'cal/mol/K','+|-',4.73563),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 571,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]} {5,S}
5   C   u0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23751,-2.99566,-4.73817,-5.53202,-5.52253,-5.73736,-5.60375],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.5437,'kcal/mol','+|-',7.1644),
        S298 = (5.53852,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 572,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_5R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   C   u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   C   u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux r1 {5,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
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
    index = 573,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C u0 {3,S} {5,S}
5   O u0 {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.355255,-4.45514,-5.9799,-6.85217,-7.13248,-7.2732,-5.99052],'cal/mol/K','+|-',[5.33021,3.45043,3,3,3,3,3]),
        H298 = (101.536,'kcal/mol','+|-',5.2),
        S298 = (6.64634,'cal/mol/K','+|-',6.46282),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 574,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   u0 r1 {3,S} {5,S}
5   O   u0 r1 {4,S} {6,[S,D,T,B,Q]}
6   C   ux r1 {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
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
    index = 575,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-5R!H->C_Int-6R!H-1R_Ext-4BrCClFINPSSi-R_7R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 r1 {3,S} {5,S} {7,D}
5   O u0 r1 {4,S} {6,S}
6   C u0 r1 {5,S}
7   C u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15106,-4.96871,-6.70307,-7.51883,-7.64047,-7.61018,-5.23652],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.402,'kcal/mol','+|-',5.2),
        S298 = (7.61836,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CO[C](C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 576,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-5R!H->C_Int-6R!H-1R_Ext-4BrCClFINPSSi-R_N-7R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S}
2   O                      u0 r1 {1,S} {3,S}
3   C                      u0 r1 {2,S} {4,S}
4   C                      u0 r1 {3,S} {5,S} {7,D}
5   O                      u0 r1 {4,S} {6,S}
6   C                      u0 r1 {5,S}
7   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0619349,-2.53145,-4.99371,-6.60115,-7.40865,-8.05344,-6.8881],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.641,'kcal/mol','+|-',5.2),
        S298 = (9.28017,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COC(=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 577,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,[S,D,T,B,Q]}
5   R!H u0 {4,[S,D,T,B,Q]}
6   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.238202,-0.740548,-1.60903,-1.92721,-1.95486,-2.20452,-3.96242],'cal/mol/K','+|-',[3,3,3,3,4.37734,5.54841,3]),
        H298 = (95.7944,'kcal/mol','+|-',8.86819),
        S298 = (3.74066,'cal/mol/K','+|-',7.67663),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 578,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,[S,D,T,B,Q]}
5   R!H u0 {4,[S,D,T,B,Q]}
6   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0441976,-0.775256,-1.89666,-2.02929,-1.3577,-1.36611,-3.61982],'cal/mol/K','+|-',[3,3,3,3,5.03733,6.23232,3]),
        H298 = (92.8549,'kcal/mol','+|-',8.00447),
        S298 = (4.82418,'cal/mol/K','+|-',8.76905),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 579,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {3,S} {5,D}
5   C u0 {4,D}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.802704,-1.08379,-2.50045,-2.94537,-3.35457,-3.95,-4.54686],'cal/mol/K','+|-',[3,3,3.06658,3.26008,3.28138,3,3]),
        H298 = (94.3442,'kcal/mol','+|-',10.5583),
        S298 = (1.21257,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 580,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 r1 {3,S} {5,D}
5   C u0 r0 {4,D}
6   C u0 r1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17871,-0.338917,-1.41625,-1.79276,-2.19443,-2.91407,-4.10064],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.6113,'kcal/mol','+|-',5.2),
        S298 = (0.421107,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1CO[C](C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 581,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-6C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {6,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S}
4   C u0 r1 {3,S} {5,D}
5   C u0 r0 {4,D}
6   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.426695,-1.82866,-3.58465,-4.09798,-4.51471,-4.98592,-4.99307],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.0771,'kcal/mol','+|-',5.2),
        S298 = (2.00402,'cal/mol/K','+|-',3),
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
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   R!H u0 {4,S}
6   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.714309,-0.466721,-1.29287,-1.11321,0.639177,1.21778,-2.69277],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.3657,'kcal/mol','+|-',6.727),
        S298 = (8.43579,'cal/mol/K','+|-',4.1204),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 583,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S} {7,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,S}
5   R!H u0 {4,S}
6   C   u0 r0 {1,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0870601,-0.138283,-1.31661,-1.39474,0.198061,0.844151,-2.92597],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.9873,'kcal/mol','+|-',5.2),
        S298 = (9.89257,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC(C)C(C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 584,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {6,S}
2   O                      u0 r1 {1,S} {3,S}
3   C                      u0 r1 {2,S} {4,S}
4   C                      u0 r1 {3,S} {5,S}
5   R!H                    u0 r1 {4,S}
6   [F,I,P,Br,Cl,O,Si,S,N] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.740247,-0.678845,-1.09769,-1.74572,-3.0165,-3.69503,-4.5715],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.2989,'kcal/mol','+|-',2.4),
        S298 = (1.8144,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 585,
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
        Cpdata = ([-0.149284,-0.441884,-0.903003,-1.4637,-2.47678,-3.25845,-4.46602],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (94.1437,'kcal/mol','+|-',2.4),
        S298 = (-0.510511,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 586,
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
        Cpdata = ([0.0126232,-0.257902,-0.740828,-1.34464,-2.4001,-3.20684,-4.44002],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (93.9363,'kcal/mol','+|-',2.4),
        S298 = (-0.695173,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 587,
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
    index = 588,
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
        Cpdata = ([-0.362168,-0.512784,-0.940595,-1.52611,-2.47396,-3.21527,-4.41088],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (92.5227,'kcal/mol','+|-',3.8633),
        S298 = (-0.143991,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 589,
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
    index = 590,
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
        Cpdata = ([-0.759716,-0.917434,-1.27693,-1.77465,-2.64427,-3.33651,-4.4757],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (91.1568,'kcal/mol','+|-',2.4),
        S298 = (-0.100316,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1OC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 591,
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
        Cpdata = ([-0.178144,-0.667693,-1.27609,-1.87573,-2.86431,-3.56776,-4.5656],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.5076,'kcal/mol','+|-',2.4),
        S298 = (-0.0177099,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 592,
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
        Cpdata = ([-0.223889,-0.853419,-1.55318,-2.16081,-3.10411,-3.76085,-4.63889],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.4699,'kcal/mol','+|-',2.44671),
        S298 = (0.0404305,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 593,
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
        Cpdata = ([-0.369206,-1.03359,-1.72699,-2.31991,-3.22644,-3.84127,-4.62203],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (94.6049,'kcal/mol','+|-',2.4),
        S298 = (0.353247,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 594,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_3R!H->C_Ext-1R-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {5,S}
2   O                      ux r1 {1,S} {3,[S,T,Q,B]}
3   C                      ux r1 {2,[S,T,Q,B]} {4,S}
4   C                      ux r1 {3,S}
5   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.078573,-0.67325,-1.37936,-2.00171,-2.98178,-3.68042,-4.65576],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (96.335,'kcal/mol','+|-',2.4),
        S298 = (-0.272386,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 595,
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
        Cpdata = ([-0.367034,-0.850833,-1.41631,-1.94425,-2.84259,-3.51673,-4.55607],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.0703,'kcal/mol','+|-',2.4),
        S298 = (-0.336204,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 596,
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
    index = 597,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.625048,-0.329272,-1.3968,-2.15825,-3.22104,-3.9275,-5.2311],'cal/mol/K','+|-',[3.05871,3,3,3,3,3,3.44505]),
        H298 = (103.293,'kcal/mol','+|-',5.2),
        S298 = (0.535119,'cal/mol/K','+|-',4.25111),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 598,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   O   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   C   ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.55845,0.31016,-1.16664,-2.16569,-3.47743,-4.27754,-5.86735],'cal/mol/K','+|-',[3,3.27265,3.67555,3.506,3,3,4.60288]),
        H298 = (103.337,'kcal/mol','+|-',5.2),
        S298 = (1.22971,'cal/mol/K','+|-',5.80835),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 599,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C u0 r0 {4,[S,D,T,B,Q]}
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
    index = 600,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   C u0 {1,S} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.02944,0.693212,-0.821392,-1.91798,-3.39045,-4.26413,-5.01026],'cal/mol/K','+|-',[2,3.17744,3.95396,4.03693,3.45186,2.59953,2]),
        H298 = (103.683,'kcal/mol','+|-',3.2693),
        S298 = (0.475076,'cal/mol/K','+|-',5.20407),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 601,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S}
2   O   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]}
4   C   u0 r0 {1,S} {5,S}
5   O   ux {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.51099,1.81661,0.576545,-0.490708,-2.17003,-3.34506,-4.78095],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.528,'kcal/mol','+|-',2.4),
        S298 = (-1.36484,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
OOC[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 602,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   O u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S}
4   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04004,-1.56419,-2.01092,-2.40373,-3.06379,-3.58478,-4.46391],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.024,'kcal/mol','+|-',2.4),
        S298 = (-0.0332429,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CO1 - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 603,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   O                      u0 r1 {1,S} {3,S}
3   C                      u0 r1 {2,S}
4   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00847871,-0.657415,-1.34531,-1.89455,-2.75157,-3.41457,-4.44303],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.463,'kcal/mol','+|-',2.4),
        S298 = (-0.594401,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 604,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   O ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.917956,-2.0105,-3.24062,-4.16122,-5.29854,-6.15469,-7.40633],'cal/mol/K','+|-',[4.5,6.32878,7.12131,7.65456,8.02362,7.88604,7.05095]),
        H298 = (85.7544,'kcal/mol','+|-',52.0541),
        S298 = (0.240958,'cal/mol/K','+|-',5.40303),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 605,
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
        Cpdata = ([-1.40522,-2.9794,-4.71007,-5.88543,-7.16647,-8.14245,-9.49559],'cal/mol/K','+|-',[6.73841,8.89065,8.82055,8.88354,9.03323,8.09311,4.96739]),
        H298 = (71.0086,'kcal/mol','+|-',57.4029),
        S298 = (-1.25482,'cal/mol/K','+|-',4.6867),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 606,
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
    index = 607,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_N-3R!H->C_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   O                      ux r1 {1,S} {3,[S,T,Q,B]}
3   O                      ux r1 {2,[S,T,Q,B]}
4   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8713,-4.91375,-6.62917,-7.81823,-9.13184,-9.90327,-10.5763],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (63.8806,'kcal/mol','+|-',2.4),
        S298 = (-2.27451,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 608,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.208845,-1.49414,-2.40865,-3.02517,-3.62752,-4.1048,-5.47511],'cal/mol/K','+|-',[3,4.18735,4.8868,5.08329,4.97532,5.07768,6.5097]),
        H298 = (94.387,'kcal/mol','+|-',53.6788),
        S298 = (3.46308,'cal/mol/K','+|-',5.90363),
    ),
    shortDesc = """Radical correction fitted to 31 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 609,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.446384,-2.21353,-3.31543,-3.96597,-4.51938,-4.98002,-6.80918],'cal/mol/K','+|-',[3.23043,4.6871,5.19311,5.09005,4.35265,3.94759,4.89379]),
        H298 = (99.9536,'kcal/mol','+|-',7.38323),
        S298 = (4.18396,'cal/mol/K','+|-',7.04964),
    ),
    shortDesc = """Radical correction fitted to 20 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 610,
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
        Cpdata = ([-1.04392,-3.15115,-4.20207,-4.71354,-5.01983,-5.3305,-7.16919],'cal/mol/K','+|-',[3.11684,4.48412,5.1966,5.18955,4.43633,3.96746,4.91147]),
        H298 = (99.1998,'kcal/mol','+|-',8.65908),
        S298 = (4.8605,'cal/mol/K','+|-',8.41593),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 611,
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
        Cpdata = ([-0.832098,-0.943168,-1.19561,-1.57449,-2.325,-3.01855,-4.32092],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.0566,'kcal/mol','+|-',2.4),
        S298 = (0.715387,'cal/mol/K','+|-',2.79936),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 612,
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
        Cpdata = ([-1.15991,-1.19584,-1.40248,-1.77276,-2.49168,-3.13861,-4.33216],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (98.2682,'kcal/mol','+|-',2.4),
        S298 = (1.70511,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 613,
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
        Cpdata = ([-1.12335,-3.97915,-5.3295,-5.89069,-6.03039,-6.19749,-8.2373],'cal/mol/K','+|-',[3.62091,4.07876,4.09972,3.85735,3.27675,3.10517,3.87163]),
        H298 = (100.094,'kcal/mol','+|-',10.9461),
        S298 = (6.41492,'cal/mol/K','+|-',7.57268),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 614,
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
        Cpdata = ([-1.58549,-3.14027,-4.18365,-4.65372,-4.84168,-4.99153,-8.64249],'cal/mol/K','+|-',[3.00121,3,3,3,3,3,3.75976]),
        H298 = (99.6941,'kcal/mol','+|-',5.2),
        S298 = (5.88293,'cal/mol/K','+|-',5.07688),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 615,
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
        Cpdata = ([-2.05337,-3.06075,-3.95131,-4.53225,-4.95476,-5.11268,-9.49541],'cal/mol/K','+|-',[3.17424,3,3,3,3,3,3]),
        H298 = (99.5078,'kcal/mol','+|-',5.2),
        S298 = (4.7313,'cal/mol/K','+|-',4.8093),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 616,
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
    index = 617,
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
        Cpdata = ([-1.15641,-2.48685,-3.57823,-4.3102,-4.91685,-5.23765,-9.70168],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.7075,'kcal/mol','+|-',5.2),
        S298 = (4.02704,'cal/mol/K','+|-',5.86133),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 618,
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
        Cpdata = ([-0.831839,-1.88669,-2.91495,-3.59769,-4.26208,-4.53931,-9.18373],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.8359,'kcal/mol','+|-',5.2),
        S298 = (1.95475,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 619,
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
8   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {7,S}
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
    index = 620,
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
        Cpdata = ([0.195112,-3.19175,-4.84483,-5.12762,-4.71658,-4.68768,-5.37717],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.067,'kcal/mol','+|-',5.2),
        S298 = (9.07037,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C[C](C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 621,
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
        Cpdata = ([-1.96245,-3.32733,-4.21949,-4.54422,-4.62756,-4.93195,-9.34906],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.8799,'kcal/mol','+|-',5.2),
        S298 = (6.15038,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 622,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C   ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3478,-3.89842,-5.58939,-6.32801,-6.4722,-6.67054,-7.84233],'cal/mol/K','+|-',[3.13701,3.74682,3.95452,3.77864,3,3,4.4909]),
        H298 = (97.8265,'kcal/mol','+|-',6.31379),
        S298 = (6.93256,'cal/mol/K','+|-',10.1471),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 623,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C",
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
        Cpdata = ([-0.802153,-3.16352,-4.82523,-5.60807,-5.94827,-6.28442,-8.2332],'cal/mol/K','+|-',[3,3,3,3,3,3,4.54167]),
        H298 = (97.4362,'kcal/mol','+|-',6.72755),
        S298 = (4.96045,'cal/mol/K','+|-',3.46795),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 624,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   O ux r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
4   C ux r1 {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C ux {1,[S,D,T,B,Q]}
6   C ux r1 {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C u0 r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.138314,-2.19521,-4.08577,-5.30074,-6.0708,-7.10535,-6.43817],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.216,'kcal/mol','+|-',5.2),
        S298 = (5.64968,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 625,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_N-6R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   O u0 {2,S} {6,S}
4   C u0 {1,S} {7,S}
5   C u0 {1,S}
6   O u0 {3,S} {7,S}
7   C ux {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.968113,-3.4056,-5.01009,-5.68491,-5.91763,-6.07918,-8.68196],'cal/mol/K','+|-',[3,3,3,3,3,3,4.70448]),
        H298 = (95.9913,'kcal/mol','+|-',5.2),
        S298 = (4.78814,'cal/mol/K','+|-',3.90434),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 626,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_N-6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S} {6,S}
4   C   u0 r1 {1,S} {7,S}
5   C   u0 r0 {1,S} {8,[S,D,T,B,Q]}
6   O   u0 r1 {3,S} {7,S}
7   C   ux r1 {4,S} {6,S}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0935624,-3.4769,-6.00199,-6.93714,-6.65028,-6.01041,-10.0178],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.7847,'kcal/mol','+|-',5.2),
        S298 = (2.21904,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(O)C[C](CO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 627,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_N-6R!H->C_Ext-7C-R",
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
        Cpdata = ([-0.925129,-3.23086,-4.67549,-5.38522,-5.92208,-6.42061,-7.5437],'cal/mol/K','+|-',[3,3,3,3,3,3,6.73454]),
        H298 = (95.2674,'kcal/mol','+|-',5.2),
        S298 = (6.30639,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 628,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_N-6R!H->C_Ext-7C-R_Sp-8R!H-7C",
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
        Cpdata = ([-1.35541,-3.35421,-4.80617,-5.44112,-5.65551,-5.88339,-9.92472],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.4305,'kcal/mol','+|-',5.2),
        S298 = (6.26167,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC(C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 629,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_N-6R!H->C_Ext-7C-R_N-Sp-8R!H-7C",
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
        Cpdata = ([-0.494843,-3.1075,-4.54482,-5.32932,-6.18865,-6.95783,-5.16268],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.1044,'kcal/mol','+|-',5.2),
        S298 = (6.3511,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1C[C](C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 630,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,S} {4,S} {5,S}
2   C   u0 r1 {1,S} {3,S}
3   O   u0 r1 {2,S} {6,S}
4   C   u0 r1 {1,S} {7,S}
5   C   u0 r0 {1,S}
6   R!H u0 r1 {3,S} {7,S}
7   O   ux r1 {4,S} {6,S}
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
    index = 631,
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
        Cpdata = ([0.963525,0.236967,-0.828306,-1.82487,-3.02128,-3.91853,-4.69208],'cal/mol/K','+|-',[3,3,3.0203,4.09041,4.49182,4.86595,3]),
        H298 = (102.487,'kcal/mol','+|-',5.34144),
        S298 = (3.38634,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 632,
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
        Cpdata = ([0.815107,-0.482467,-2.30685,-3.82727,-5.22018,-6.30059,-5.85445],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.6,'kcal/mol','+|-',5.2),
        S298 = (3.27196,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CC[CH]CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 633,
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
        Cpdata = ([0.558771,-0.7837,-2.06847,-2.94188,-3.87392,-4.5356,-6.98831],'cal/mol/K','+|-',[3,3,3.60064,4.02657,4.19712,4.30038,5.75522]),
        H298 = (100.174,'kcal/mol','+|-',5.2),
        S298 = (2.55145,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 634,
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
        Cpdata = ([0.0811167,-1.76431,-3.37706,-4.37851,-5.26434,-5.80284,-9.05408],'cal/mol/K','+|-',[3.26765,3,3,3,3,3.44412,3]),
        H298 = (99.1646,'kcal/mol','+|-',5.56901),
        S298 = (2.46026,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 635,
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
    index = 636,
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
        Cpdata = ([-0.0724775,-1.93547,-3.54559,-4.45631,-4.9342,-5.11612,-9.69298],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.3165,'kcal/mol','+|-',5.2),
        S298 = (2.9395,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC1(C)C[CH]COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 637,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.135414,-0.451547,-1.09449,-1.66169,-2.33499,-2.83636,-3.54168],'cal/mol/K','+|-',[3,3,3,3.80512,4.86477,5.65443,6.84279]),
        H298 = (87.8182,'kcal/mol','+|-',80.178),
        S298 = (2.41832,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 638,
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
        Cpdata = ([0.414039,-0.249594,-0.989963,-1.60679,-2.19645,-2.62061,-3.1165],'cal/mol/K','+|-',[3,3,3.80151,4.95741,6.3403,7.36075,8.84815]),
        H298 = (70.8401,'kcal/mol','+|-',102.158),
        S298 = (2.08377,'cal/mol/K','+|-',3.10337),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 639,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,D}
5   R!H u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.607198,0.446397,0.16472,0.0209946,0.141406,0.0474734,-0.118461],'cal/mol/K','+|-',[3,3,4.66065,6.0454,7.34636,9.16388,12.6274]),
        H298 = (35.7554,'kcal/mol','+|-',148.086),
        S298 = (2.60423,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 640,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   ux {3,S} {5,D} {6,S}
5   R!H u0 {4,D}
6   C   u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.464902,0.434602,0.302586,0.308041,0.755176,0.97973,1.1988],'cal/mol/K','+|-',[3,3.84151,6.31232,8.06403,9.2656,11.0588,15.1268]),
        H298 = (19.6654,'kcal/mol','+|-',131.674),
        S298 = (2.17325,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 641,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r1 {2,S} {7,[S,D,T,B,Q]}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S}
4   C   ux r1 {3,S} {5,D} {6,S}
5   R!H u0 r0 {4,D}
6   C   u0 r1 {4,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.418563,-1.44595,-2.78752,-3.63959,-3.78066,-4.43393,-6.20629],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.4226,'kcal/mol','+|-',5.2),
        S298 = (3.07716,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CCC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 642,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 * C   u1 r1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C   ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.282691,-0.722867,-1.77515,-2.71368,-3.78619,-4.4349,-5.15517],'cal/mol/K','+|-',[3,3,3,3.22873,3.66793,3.68075,3]),
        H298 = (97.8542,'kcal/mol','+|-',6.48501),
        S298 = (1.72986,'cal/mol/K','+|-',3.64046),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 643,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.183957,-0.768601,-1.67573,-2.50463,-3.51689,-4.08285,-5.02293],'cal/mol/K','+|-',[3,3,3.02331,3.45363,3.85015,3.62333,3]),
        H298 = (96.9744,'kcal/mol','+|-',5.2),
        S298 = (1.4454,'cal/mol/K','+|-',3.77725),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 644,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_4R!H->C_Ext-1R-R",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C ux {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.125169,-1.52552,-2.64054,-3.55513,-4.54387,-4.93278,-5.6157],'cal/mol/K','+|-',[3,3,3,3,3.57271,3.77735,3.18415]),
        H298 = (96.6953,'kcal/mol','+|-',5.2),
        S298 = (2.46231,'cal/mol/K','+|-',3.4669),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 645,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_4R!H->C_Ext-1R-R_Int-5R!H-1R",
    group = 
"""
1 * C u1 r1 {2,S} {5,[S,D,T,B,Q]} {6,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   C u0 r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C ux {1,[S,D,T,B,Q]} {4,[S,T,Q,B]}
6   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00916313,-1.4151,-2.55415,-3.24212,-3.81391,-4.02411,-4.8442],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.063,'kcal/mol','+|-',5.2),
        S298 = (2.66335,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 646,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_4R!H->C_Ext-1R-R_Sp-4C-3C",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,S}
4   C ux r1 {3,S} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]}
6   C ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.07302,-2.6566,-3.67378,-4.97729,-6.57961,-7.10404,-7.44654],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.8828,'kcal/mol','+|-',5.2),
        S298 = (4.08648,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]1CCCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 647,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_4R!H->C_Ext-1R-R_N-Sp-4C-3C",
    group = 
"""
1 * C u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux r1 {2,[S,T,Q,B]} {4,D}
4   C ux r1 {3,D} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]}
6   C ux r1 {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.706674,-0.504853,-1.6937,-2.44599,-3.23808,-3.67018,-4.55635],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.1401,'kcal/mol','+|-',5.2),
        S298 = (0.637112,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1=CC[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 648,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-4R!H->C",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 r1 {1,S} {3,S}
3   C u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   O u0 r1 {3,[S,D,T,B,Q]} {5,[S,T,Q,B]}
5   C ux r1 {4,[S,T,Q,B]}
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
    index = 649,
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
        Cpdata = ([-0.533149,-1.04462,-1.49564,-1.91001,-2.63198,-3.20228,-4.16267],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (104.878,'kcal/mol','+|-',4.41453),
        S298 = (3.04495,'cal/mol/K','+|-',2.99549),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 650,
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
        Cpdata = ([-0.178754,-0.955987,-1.6608,-2.19054,-3.00486,-3.59333,-4.44289],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (106.438,'kcal/mol','+|-',2.4),
        S298 = (4.10402,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 651,
    label = "RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,S}
2   C                      u0 r1 {1,S} {3,S}
3   C                      u0 r1 {2,S}
4   [F,I,P,Br,Cl,O,Si,S,N] u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.887544,-1.13325,-1.33048,-1.62948,-2.25911,-2.81124,-3.88245],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.317,'kcal/mol','+|-',2.4),
        S298 = (1.98589,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 652,
    label = "RJ1_N-1R-inRing",
    group = 
"""
1 * R u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.779029,-1.71364,-2.37717,-2.76054,-3.14328,-3.49255,-4.25114],'cal/mol/K','+|-',[4.16696,4.85806,5.15392,5.10443,4.72498,4.41775,4.24371]),
        H298 = (94.3375,'kcal/mol','+|-',23.153),
        S298 = (0.343811,'cal/mol/K','+|-',10.6805),
    ),
    shortDesc = """Radical correction fitted to 2074 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 653,
    label = "RJ1_N-1R-inRing_1R->C",
    group = 
"""
1 * C u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0757957,-0.876185,-1.55572,-2.03359,-2.65192,-3.15629,-4.15907],'cal/mol/K','+|-',[3.35798,3.75647,4.07618,4.1321,3.95723,3.73796,3.68158]),
        H298 = (95.7438,'kcal/mol','+|-',21.001),
        S298 = (0.95182,'cal/mol/K','+|-',10.4659),
    ),
    shortDesc = """Radical correction fitted to 1176 radicals""",
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
C=C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(OC(=C)C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)CCC(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOC(OC(C)=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CO[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)COOCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)C=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C(C)=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC=CC(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)[CH]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
CC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C(=C)O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(ON(CC)CC)C - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C(C)=CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=CC(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C(=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC1([CH2])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(OO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)OCC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C(C)=O)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
C[C]=CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C(C)C(C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(O)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C([CH]O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C1C(O)OOC1(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]COOC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
C=CCCC(C=C)CC=C[CH]C - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([CH]CO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)CC(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC=CCON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
O=CC(O)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC=CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCOC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
O[CH]C(O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1OOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC=CC(C)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)=CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CO[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(C)=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C2OO2)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C](C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COOC(C)(C)[C](C)C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C(=CO)C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)O[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]C1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC([CH]O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC1(CC=CC)C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC[CH]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C=COC(C)=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)(C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](CCOO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C](C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C[CH]CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CCC=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(=O)OCO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
[CH2]OCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(COO)CCC(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[CH]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)[C](O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
C[C]=C(CO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OOC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]OC)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](COO)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OCC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)OC(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1C=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CO[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC#CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)CC1=CCCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
C#CC(O)=C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]CC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)OOC([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
C=CC(=O)[CH]C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C#CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
OC[C](O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(OOC(C)=O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC([CH]COO)OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
[CH]=CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C=C(O)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1C=CCCC1C([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C=C)=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(COO)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OCC(C[CH]C=C)C=C)CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]OC(=C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C(O)O[C](O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC=CCC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
CC(=O)OC([CH]C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C(C[CH]CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CO[CH]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1(C)OOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OOC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(OC)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
C=C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([C]=O)C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=CC)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CO[C](O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1CC=CC=C1C - Radical thermo from pang.py and closed shell thermo from GAV
O=[C]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCOOC([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C)(OC(=C)C1OO1)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(=C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C1([C]=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC(O)=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C=CC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C1(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C](O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC(C=C)CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]CC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CCC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(C)(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC(=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(OC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CCC(C=C)OO - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C(COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)C(=O)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[CH]=C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)(C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=COC)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC(C=C)CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
O=[C]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)CC(C)=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C=CCCC(C=C)OO - Radical thermo from pang.py and closed shell thermo from GAV
[C]#COC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C](COO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CO)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=CCC([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C(C)[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(=O)CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(CC=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[C](C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)(C)OOC(C)(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)OOC1CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]C1CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)O[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([CH]OCOO)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[CH2]C(=CO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OC[CH]C=C)CC - Radical thermo from pang.py and closed shell thermo from pang.py
O=[C]OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC([CH]OC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(=O)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=O - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
C=[C]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)C1C=CC=C(C)C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1=CCCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]COOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(C)C#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(COO)COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(OO)C(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC(C=C)CCC=CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1CC1(C)CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(CC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]CC(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCCC(C=C)C[CH]C=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=CC[C](C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC1=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[C]#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]OC)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
C=C(COO)[C](C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(OC(C)(C)[C](C)C)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]C(O)=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCC(N(CC)O)C - Radical thermo from pang.py and closed shell thermo from pang.py
C=C(O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1OOCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCOOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]COOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC(O)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(CC)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
OC=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=O)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC(=C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)OOC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)OOC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)COC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1(CC=CC)C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1(C)CCC(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C]=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=CC(O)C=C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)C([CH]CC)CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C1COOC1[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)C[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[C](C)CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)O[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[C]#CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)CC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
C#CC(=O)C[CH2] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(COC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[C](CCOO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(=C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=CO[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(=C)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCCC=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=[C]C=CCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCOOC(C)C=C - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]COC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CC(=O)O[CH]OC=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C(C)COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)C - Radical thermo from pang.py and closed shell thermo from pang.py
C=CC=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(COC(C)=O)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(CO)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[CH2]C(O)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(OO)OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C=C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C)CC=CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[CH]C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C=C)OOC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1(OC(C)=O)OC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)OC1OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C=O)CC(=C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([CH]CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(O)C#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(C)[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC#CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(=C)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC(=O)OC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC([CH2])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(=C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)OO - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C1CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCOOCC(C)C - Radical thermo from pang.py and closed shell thermo from GAV
O=CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[C](COO)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=O)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC(C=C)CC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]CC1=C(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(OO)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=CC)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([CH]COO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=COC)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([CH]O)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([C]=O)C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)OOC1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=[C]CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]OCOO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC(OOCC(=C)C)CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(COO)C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](CC=CC)CCC=CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1(CO)OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCCC(=C)C - Radical thermo from pang.py and closed shell thermo from GAV
C[C](C)C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C(OO)C(O)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C([CH]O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC(C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[C]=O - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CCCC=CCC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]CCC(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C=C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)C1OOC(OC(C)=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=CO)C(=C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1=C=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C(O)O[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(COO)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([CH]C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C12COOC1(C)COO2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([CH]CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)(COO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[CH]CCC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
O[CH]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(CCO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C1OOC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC(=C)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1(OC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COOCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1CC(C)=CCC1C - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(C=O)=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC=CC#C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(CC(=C)C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C=C)OOC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC=CCC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1(C(=C)C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](C)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CCC(=C)C - Radical thermo from pang.py and closed shell thermo from GAV
C=CCO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(CC)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
C=CC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=CC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)C1C=C(C)C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=COC(O)C1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C(C)C(C)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC(=C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(C=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C=C(O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
C[C](C)C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[C](COO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[C]=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C#CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(=C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=COCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1C(=O)C=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=COC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[C](O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC(=C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(O)C(CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)C[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]OCOOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=C)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCC(=O)O[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
[CH2]C(=O)COC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=C)C(=C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(C=O)C[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)CC=CC - Radical thermo from pang.py and closed shell thermo from GAV
O=[C]C=C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)OOC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C[CH]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)(C)OOCC(C)=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(O)C(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CCC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](O)C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)COC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C([CH]O)CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C(C)O[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC1([CH]C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]OC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([C]=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([CH]O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[C](O)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=COCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(=O)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]COCOO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C=C[CH]CCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CC=CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]CC(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1=C(OC)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C(C)OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
O=C[CH]C1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[CH]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C[C](C)C(C)(C)OC1=COC=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC[CH]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN([CH]C)O - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1(CC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C[C](C)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[C](O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C)(C)[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C1OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC(CCOO)OO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
[CH]=C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[C]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C]=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C(C)CC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[CH]CCOC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C]=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
C#C[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C[CH]COO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(OC1=COC=C1C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(O)(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C(C)C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)C(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOCC1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)=CCC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)(C)OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=C(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH3] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](CO)C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C]=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(C)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(CO)CC(C)(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]CC(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)OC(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](COO)C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C](C=O)C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=C(C)COOC(C)(C)C(C)(C)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OC(C=C)[CH2])CC - Radical thermo from pang.py and closed shell thermo from pang.py
[CH2]C1=C=CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C)CC1C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CO[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)C1C=CC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
O=[C]C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)=COC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 654,
    label = "RJ1_N-1R-inRing_N-1R->C",
    group = 
"""
1 * [H,O,N] u1 r0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8782,-3.02261,-3.6611,-3.89679,-3.91129,-4.01813,-4.39504],'cal/mol/K','+|-',[4.35555,5.2171,5.59702,5.62622,5.37632,5.1379,4.98635]),
        H298 = (91.7763,'kcal/mol','+|-',25.8768),
        S298 = (-0.606521,'cal/mol/K','+|-',10.7423),
    ),
    shortDesc = """Radical correction fitted to 898 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1COOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(O)C(=O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)COC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COCOO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[O]C12OC1(O)O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1C=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]COOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C)OOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CC(C)(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=C(O)C(O)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C1CC(C)([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1(O)OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCOC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1(C(=O)O)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC1OC1(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C[O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(=CO)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(COO)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(C)(O[O])C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]OCC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C1(C)OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)CC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])CCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)C(O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCC=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(OC(C)=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCCC1C1C=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1(O)OOC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1CC(C)(CO[O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CC(C)O[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC1C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CC(=O)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCOCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C(=O)OOC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)OC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(O)(O)OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CCOCO1 - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
CC(=O)OCC(=O)CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[H] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OOCC(O[O])C1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)=C(C)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(O)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1OCOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C12OC1O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC(C)(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CCCO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CCOC1(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1(OO)COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CC(O[O])C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=CC=CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCC([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC([O])C(=C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C(C=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CCO)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1OC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CC(=O)C(OO)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CCC(C)(O[O])C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CC(=O)OC(=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CCC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(=O)CC[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC(C)=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=CCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(CO)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(CCO[O])OO - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=CC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CCCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[OH] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])COOCC1(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C(O)=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)(O[O])C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=CC=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(=O)C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CCC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[N+](CC)[O-] - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)OCC([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C([O])OCO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
[O]C=C(O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(=O)C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])CCC(=O)OOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(CC(=O)OC=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C1OOCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CO)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCC1=CC(O[O])C=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CCOO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O)C(=CO)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COCCCO[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=C([O])C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([O])C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CCC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])=C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)COOC(C)(C)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)CC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1=C([O])OC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(=O)OC[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(CO[O])=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CCC(=O)OC([O])O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CCC(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OC1OC[O] - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
CC(=O)OC(COO)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(CCC(C=C)OO)O[O] - Radical thermo from pang.py and closed shell thermo from GAV
[O]C(O)=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CC=CC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
[O]C1=COCC(COO)(OO)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(CC)[O] - Radical thermo from pang.py and closed shell thermo from pang.py
CC(=O)OCC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCCC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(COC(C)=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C(CC(C)=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C(C)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CC(C)OO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CCCOO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=CCO[O] - Radical thermo from pang.py and closed shell thermo from GAV
CC(C)(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=COC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C1(O[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(OO)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)OC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])COC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)C(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C(=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CCO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CC2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1C=CC(O[O])COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CO[O] - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
C=COC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)C(O)COO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C=C(C(=O)O[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])OOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]OCOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)CO[O] - Radical thermo from pang.py and closed shell thermo from pang.py
[O]C(C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(OO)OCO[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
C=C(OCO[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(O[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C(C=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=COC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1OC1C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(OOC2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCC(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CO[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(C=O)C1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCOC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC1(C=C[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC([O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1COC(=O)C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CC=CCC1O[O] - Radical thermo from pang.py and closed shell thermo from GAV
[O]OCC(=O)COC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CC=CC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1OOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(OO)COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C(O)(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])(CO)C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from pang.py
C=C(C)C([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)C=CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(C=O)CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCC(CO)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
[O]OC(O)CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C1CC(=O)OC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=CCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C=C(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(C=O)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COCO[O])OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[O]OC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]OCC#CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(O)=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(C)([O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCC(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CCC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(=O)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC1(CO)OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=C([O])OCC(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])C(=O)OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(OC)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_cbs-qb3.py
CC(C)(O[O])C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CC(OO)CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1CC(C)(O[O])COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CC[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(C)OC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C(O)=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=COC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])C=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC=CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC#C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC#C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=O)CC(=C[O])C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)=CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OC(C)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC([O])C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1(COO)COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=CC(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C1(C)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(O[O])C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CC(O[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(C)CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(CCO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(COC(=O)CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=COCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])COOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1OOC=C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C(CO[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=C([O])C2OC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1CCCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN(OC1C=CC(C1)[O])CC - Radical thermo from pang.py and closed shell thermo from GAV
COC=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CCO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([O])C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC(CCOO)O[O] - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from GAV
CC(=O)OC([O])C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=C(O)C(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CCC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(C=O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(O[O])CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=C=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC([O])C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1OOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC([O])C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])C(=O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1C=COCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC([O])=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC(=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1(COO)COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)CC(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CO)=C(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(O[O])COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OOC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(=C=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC1([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C=C(C)O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])=C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O[O])C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C1=CC=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C(C)C(OO)C(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CCO)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C(CO[O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(C=O)CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(OO)C(=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1(CO)COOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC1(C)COOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCCCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1=COOC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C=O)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN(O[O])CC - Radical thermo from pang.py and closed shell thermo from GAV
CC([O])=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=CC)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(O[O])C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)C(CCO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
CC(=O)OC(C[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(O[O])=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CO[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COC(C)=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCCOC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=COC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC1OC1C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1OC(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC=C=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)C(C)(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(O[O])C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C)CC1=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(OO)C(O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C1CC(O)=CC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=C(O)C=O)C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC(O)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=C[O])C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)C=C=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)CC=C([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)C1([O])CC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC1OC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=COC=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOC1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)O[O] - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
C=C(C[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(C)OC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C(C[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)CC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(OO)COC=C([O])O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C1(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(COO)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CCC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CC)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)CCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(CCO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C)(CO[O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C=C[O])OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(C)(COO)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=COC([O])=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1COCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C)CC(O[O])C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C(C[O])CC(C)(C)C(C)(C)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(CO[O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)(CC)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCC(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCCCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OCC=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]CCCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CC=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C(=O)O[O])C(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(O[O])C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=C(O)C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1=COC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCC(C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CCCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C[O])C1(C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C)OC=C1CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
CC(OO)C1CC(=O)OC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCN(OC1C=CC(C1)O[O])CC - Radical thermo from pang.py and closed shell thermo from pang.py
CC([O])COC=O - Radical thermo from johnson_g4.py and closed shell thermo from GAV
[O]CC1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1C(O)=COC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CCC1ON(CC)CC - Radical thermo from pang.py and closed shell thermo from pang.py
[O]OC1C=CC(=O)C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(O)CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(O[O])OCOO - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from johnson_g4.py
C=C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])C(=O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C([O])C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OCC(C=C)O[O])CC - Radical thermo from pang.py and closed shell thermo from pang.py
C=C(C)C(=C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1(C=O)OC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(O)=C(O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C(=O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=C(CO[O])OCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CC=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)C=CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OC1O[O] - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
[O]C1COC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COC=CC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C(O[O])OC1(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCC(=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(=O)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CO)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(CO[O])CCC(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1CCC(C)([O])O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[N]CC - Radical thermo from pang.py and closed shell thermo from GAV
[O]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=O)C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=COC(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COC(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1OOC=C=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(C)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC1(C)CC(O[O])COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OOCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1COC(C)([O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1CC(C)([O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO[O])OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(CO)C(C)(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(C=O)C1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OC1OCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1CC(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC(C)(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC1OC1CC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=O)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(OO)=C1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C=O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC([O])C(C)(C)C(=O)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1OOC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=C(C=C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1OOC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=C=C([O])OC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CCCC1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O[O])OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C=CC([O])C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OCC=CCO[O])CC - Radical thermo from pang.py and closed shell thermo from pang.py
C=C([O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1([O])CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CC=C1[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(=O)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC(=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)([O])CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)(C=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=C(O)C=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C(=CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1OOCC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
COCC(C)[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
CC(=O)OC(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1OOC=C1O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(O[O])C(C)(C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=CC=C1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)OC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CC1CC=CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C1=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(O[O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CC([O])C=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=COC(O[O])C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(CO[O])COC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(=C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(O[O])C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(O)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(OO)OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(=O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1=CC=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCCOCO[O] - Radical thermo from johnson_cbs-qb3.py and closed shell thermo from johnson_g4.py
C=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C(O)O[O])C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CCC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_1R-inRing
            L4: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-2R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-2R!H-R_5R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-2R!H-R_5R!H-inRing_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-2R!H-R_N-5R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-2R!H-R_N-5R!H-inRing_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_Ext-3R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-4O-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R_Sp-6R!H-5C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_Sp-7R!H-6R!H
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4O-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_4O-inRing_N-5R!H->C_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Ext-6R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-4O-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-4O-R_Sp-6R!H-5R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-4O-R_N-Sp-6R!H-5R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_Sp-5R!H-3R!H_N-4O-inRing_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-1R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-Sp-5R!H-3R!H
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_4R!H->O_Ext-3R!H-R_N-Sp-5R!H-3R!H_Ext-4O-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R_5C-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R_5C-inRing_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R_N-5C-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R_N-5C-inRing_6R!H-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-3R!H-R_Ext-7R!H-R_N-5C-inRing_N-6R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_5R!H->C_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_Sp-6R!H=4C_N-5R!H->C_Ext-6R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C_8R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C_8R!H->C_6R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C_8R!H->C_6R!H->C_Ext-3R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C_8R!H->C_N-6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_5R!H->C_N-8R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Ext-2R!H-R_Ext-4C-R_N-Sp-6R!H=4C_Ext-6R!H-R_Ext-7R!H-R_N-5R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_Ext-5C-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_6R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-3R!H-R_N-6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-1R-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_Int-8R!H-5C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing_Sp-7R!H-6C
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_7R!H-inRing_N-Sp-7R!H-6C
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_Sp-9R!H=8R!H_N-7R!H-inRing
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_6C-inRing_Ext-8R!H-R_N-Sp-9R!H=8R!H
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_Sp-8R!H-7R!H_N-6C-inRing
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_6R!H->C_Ext-6C-R_Ext-7R!H-R_N-Sp-8R!H-7R!H
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-5C-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H-10R!H
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_8R!H-inRing
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H-10R!H_N-8R!H-inRing
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_7R!H->O
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_7R!H->O_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_7R!H->O_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_Sp-6R!H-4C_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_N-7R!H->O
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_6R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_6R!H->C_Ext-5C-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_N-6R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_N-6R!H->C_Ext-5C-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_N-6R!H->C_Ext-5C-R_7R!H->C
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-4C-R_N-Sp-6R!H-4C_N-6R!H->C_Ext-5C-R_N-7R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_8R!H-inRing
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing_Ext-9R!H-R_Sp-11R!H-9R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_Sp-10R!H-9R!H_N-8R!H-inRing_Ext-9R!H-R_N-Sp-11R!H-9R!H
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H_8R!H-inRing
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-9R!H-R_N-Sp-10R!H-9R!H_N-8R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi_6C-inRing
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H
                                                                                L21: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi_6C-inRing_Ext-8R!H-R_Sp-9R!H-8R!H_Ext-9R!H-R_Ext-6C-R
                                                                            L20: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi_6C-inRing_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                                                        L19: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_Sp-8R!H-7BrCClFINPSSi_N-6C-inRing
                                                                    L18: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_6R!H->C_Ext-7BrCClFINPSSi-R_N-Sp-8R!H-7BrCClFINPSSi
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-7R!H->O_N-Sp-7BrBrCCClClFFIINNPPSSSiSi=6R!H_N-6R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_6R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing_6R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_Sp-5C-4C_Ext-5C-R_N-Sp-6R!H-5C_N-6R!H-inRing_N-6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_5R!H->C_N-Sp-5C-4C_Ext-3R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-3R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R_Sp-6R!H-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Int-5R!H-4C_N-5R!H->C_Ext-4C-R_N-Sp-6R!H-4C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Int-6R!H-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R_6R!H-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_Ext-4C-R_N-6R!H-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Ext-8R!H-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Ext-8R!H-R_Ext-1R-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Int-8R!H-1R_Ext-7R!H-R_Sp-9R!H-7R!H
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_6R!H-inRing_Ext-6R!H-R_Int-8R!H-1R_Ext-7R!H-R_N-Sp-9R!H-7R!H
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Sp-7R!H-4C_N-6R!H-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing_Ext-5R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_6R!H-inRing_Ext-7R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing_Ext-5R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_N-Sp-7R!H-4C_N-6R!H-inRing_Ext-6R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-5R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_7R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_N-7R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_Ext-7C-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H-8R!H
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-3R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-1R-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_6O-inRing_Ext-6O-R_Int-7R!H-4C_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_Ext-4C-R_Ext-5R!H-R_Int-7R!H-5R!H_Ext-6O-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-10R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1R-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-1R-R_Ext-7R!H-R_Ext-8R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_5R!H-inRing_Ext-6O-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->O_N-6O-inRing_N-5R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_7R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_7R!H-inRing_Ext-4C-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_7R!H-inRing_Int-7R!H-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_N-7R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_N-7R!H-inRing_7R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_N-7R!H-inRing_7R!H->C_Ext-1R-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_N-7R!H-inRing_N-7R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-6CN-R_N-7R!H-inRing_N-7R!H->C_Ext-3R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-4C-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-3R!H-R_Ext-5R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_Sp-9R!H-8C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_8R!H->C_Ext-8C-R_N-Sp-9R!H-8C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-7R!H-R_N-8R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R_8R!H->C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-1R-R_Ext-4C-R_N-8R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_7R!H-inRing_Ext-5R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-4C-R_Ext-7R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-5R!H-R_N-7R!H-inRing_Ext-5R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_7R!H->O
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_7R!H-inRing_Ext-4C-R_N-7R!H->O
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_Sp-11R!H=10R!H
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-7O-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R_Ext-11R!H-R_N-Sp-11R!H=10R!H
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_N-7R!H->O
                                                                L17: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_Sp-7R!H-4C_N-7R!H->O_Ext-4C-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_Sp-6CN-4C_Ext-4C-R_N-7R!H-inRing_N-Sp-7R!H-4C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_7R!H->C
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_7R!H->C_Ext-6CN-R
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_7R!H->C_Ext-8R!H-R_Sp-9R!H-8R!H
                                                            L16: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_7R!H->C_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-3R!H-R_Ext-7R!H-R_N-7R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_Sp-2R!H-1R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->O_Int-6CN-4C_N-Sp-6CN-4C_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_3R!H-inRing_N-4R!H->O_N-Sp-2R!H-1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Int-4R!H-2R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Ext-1R-R_Ext-2R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Ext-1R-R_Ext-2R!H-R_Ext-7R!H-R_Ext-5O-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Ext-4R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_5R!H->O_Ext-5O-R_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H_4R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H_4R!H->C_Ext-5BrCClFINPSSi-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H_N-4R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-2R!H_N-4R!H->C_Ext-5BrCClFINPSSi-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H_Sp-6R!H-5BrCClFINPSSi
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H_Sp-6R!H-5BrCClFINPSSi_Ext-1R-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H_Sp-6R!H-5BrCClFINPSSi_Sp-5BrCClFINPSSi-4C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H_Sp-6R!H-5BrCClFINPSSi_N-Sp-5BrCClFINPSSi-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-5BrCClFINPSSi-R_Int-6R!H-2R!H_N-Sp-6R!H-5BrCClFINPSSi
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-2R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_4R!H->C_Ext-2R!H-R_Ext-4C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_N-4R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_N-4R!H->C_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-4R!H-R_N-5R!H->O_N-4R!H->C_Ext-5BrCClFINPSSi-R_Ext-2R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R_Sp-5R!H-3C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R_N-Sp-5R!H-3C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R_N-Sp-5R!H-3C_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_4R!H->C_Ext-3C-R_N-Sp-5R!H-3C_N-5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_3R!H->C_N-4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_Sp-6R!H-5C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_Sp-6R!H-5C_Ext-5C-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_Sp-6R!H-5C_Ext-5C-R_Ext-6R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_Sp-6R!H-5C_7R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_Sp-6R!H-5C_N-7R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_N-Sp-6R!H-5C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_N-Sp-6R!H-5C_6R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-4O-R_N-Sp-6R!H-5C_N-6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_4R!H->O_Ext-5C-R_N-6R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O_Ext-1R-R_Int-5C-4C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O_Ext-1R-R_Int-5C-4C_Ext-4C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O_Int-5C-4C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_5R!H->C_N-4R!H->O_Ext-5C-R_Ext-5C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_6R!H->C_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_N-6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_N-6R!H->C_Ext-1R-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_N-6R!H->C_Ext-1R-R_Ext-5BrClFINOPSSi-R
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_N-6R!H->C_Ext-1R-R_Ext-5BrClFINOPSSi-R_4C-inRing
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-4C-R_N-6R!H->C_Ext-1R-R_Ext-5BrClFINOPSSi-R_N-4C-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_4R!H->C_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_4O-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R_Ext-5BrClFINOPSSi-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R_Ext-5BrClFINOPSSi-R_Int-7R!H-6R!H_Ext-7R!H-R_Ext-8R!H-R_8R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_4O-inRing_Ext-4O-R_Ext-5BrClFINOPSSi-R_Int-7R!H-6R!H_Ext-7R!H-R_Ext-8R!H-R_N-8R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_2R!H-inRing_N-3R!H->C_Ext-2R!H-R_N-5R!H->C_N-4R!H->C_N-4O-inRing
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-2R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-2R!H-R_Ext-6R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-3C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-4R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-4R!H-R_6R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_3R!H->C_Ext-4R!H-R_N-6R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_4R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_4R!H->O_Ext-2R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_4R!H->O_Ext-2R!H-R_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_4R!H->O_Ext-2R!H-R_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_N-4R!H->O
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-4R!H-R_Int-5R!H-1R_N-3R!H->C_N-4R!H->O_Ext-2R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-2R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-2R!H-R_3R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_Sp-4R!H-1R_N-3R!H-inRing_N-2R!H-inRing_Ext-2R!H-R_N-3R!H->C
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_3R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R_7R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_3R!H-inRing_Ext-5C-R_Ext-3R!H-R_N-7R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_N-3R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R_Sp-6R!H-5C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_5R!H->C_N-3R!H-inRing_Ext-5C-R_N-Sp-6R!H-5C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_3R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_3R!H->C_Ext-3C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_N-3R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_N-3R!H->C_Ext-5BrClFINOPSSi-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_3R!H-inRing
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_Ext-1R-R_N-Sp-4R!H-1R_Ext-4R!H-R_N-5R!H->C_N-3R!H-inRing
            L4: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-2R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_Ext-3O-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_Ext-3O-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_3R!H->O_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_Ext-2R!H-R_Ext-6R!H-R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Int-4R!H-1R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Int-4R!H-1R_Ext-3C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Int-4R!H-1R_Ext-3C-R_5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Int-4R!H-1R_Ext-3C-R_N-5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Int-4R!H-1R_Ext-2R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Ext-1R-R_Ext-3C-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Ext-3C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-3C-R_Ext-3C-R_Ext-2R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_Sp-2R!H=1R_N-3R!H->O_Ext-1R-R
                L5: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R
                    L6: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_4R!H->C_Ext-4C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_4R!H->C_Ext-2R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_5R!H->C_Ext-5C-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_5R!H->C_Ext-4O-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_5R!H->C_Ext-4O-R_6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_5R!H->C_Ext-4O-R_N-6R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_N-5R!H->C_3R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_Ext-1R-R_N-4R!H->C_N-5R!H->C_N-3R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_3R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_3R!H->C_Ext-3C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_3R!H->C_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_3R!H->C_N-4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_4R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-2R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-2R!H-R_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-2R!H-R_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-2R!H-R_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-4C-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-4C-R_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_4R!H->C_Ext-4C-R_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_N-4R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_N-4R!H->C_Ext-4O-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_N-4R!H->C_Ext-4O-R_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Int-3R!H-1R_N-3R!H->C_N-4R!H-inRing_N-4R!H->C_Ext-4O-R_N-5R!H->C
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_4R!H-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_4R!H-inRing_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-8R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-8R!H-R_Ext-4R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-4R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-4R!H-R_9R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-4R!H-R_N-9R!H->C
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-1R-R_Ext-4R!H-R_N-9R!H->C_Ext-9BrClFINOPSSi-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_Int-7R!H-3R!H_N-4R!H-inRing_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-5R!H-R_Ext-8R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_5R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_5R!H->C_Ext-1R-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_5R!H->C_Ext-1R-R_Ext-3R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-7R!H-R_Int-8R!H-5R!H_3R!H-inRing
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_2R!H-inRing_Ext-7R!H-R_Int-8R!H-5R!H_N-3R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-6C-R_N-2R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-1R-R_Ext-7R!H-R_Ext-8R!H-R_3R!H->O
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_6R!H->C_Ext-1R-R_Ext-7R!H-R_Ext-8R!H-R_N-3R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_N-6R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_3R!H-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_Ext-2R!H-R_Ext-1R-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Ext-7R!H-R_N-3R!H-inRing
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_4R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_4R!H-inRing_Ext-3O-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_4R!H-inRing_Ext-3O-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_4R!H-inRing_Ext-3O-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-4R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_Ext-1R-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_Ext-1R-R_4R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_Ext-1R-R_N-4R!H->C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_Ext-1R-R_N-4R!H->C_Ext-5R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_Ext-4R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_4R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_Ext-4R!H-R_N-4R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_6R!H->O
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_6R!H->O_6O-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_6R!H->O_N-6O-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_6R!H->O_N-6O-inRing_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_N-6R!H->O
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-3O-R_Ext-1R-R_N-6R!H->O_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_4R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_3O-inRing_N-4R!H-inRing_N-4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-5R!H-R_Ext-1R-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-5R!H-R_Ext-1R-R_Ext-5R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_Ext-5R!H-R_Ext-1R-R_Int-11R!H-10R!H_Ext-9R!H-R_Ext-12R!H-R_Ext-12R!H-R_Ext-9R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_Sp-10R!H-9R!H
                                                        L15: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_Sp-10R!H-9R!H_Ext-10R!H-R_Ext-7R!H-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_N-Sp-10R!H-9R!H
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_Sp-9R!H-8R!H_N-7R!H-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_7R!H-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_7R!H-inRing_Ext-9R!H-R_Ext-10R!H-R_Ext-10R!H-R_Ext-1R-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_N-7R!H-inRing
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-Sp-9R!H-8R!H_N-7R!H-inRing_Ext-7R!H-R_Ext-5R!H-R_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-5R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H->C_Ext-5C-R_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H->C_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H->C_Ext-1R-R_5O-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H->C_Ext-1R-R_5O-inRing_Ext-3O-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_Ext-2R!H-R_3R!H->O_N-3O-inRing_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H->C_Ext-1R-R_N-5O-inRing
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
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_5R!H->C_Ext-3R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-5R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-5R!H->C_Int-6R!H-1R_Ext-4BrCClFINPSSi-R_7R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-5R!H->C_Int-6R!H-1R_Ext-4BrCClFINPSSi-R_N-7R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_6C-inRing
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-6C-inRing
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_Ext-3R!H-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Ext-1R-R_6R!H->C_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-1R-R
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
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_Ext-4R!H-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_Ext-4R!H-R_5R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_Ext-4R!H-R_N-5R!H->C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_Ext-4R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_2R!H->O_3R!H->C_Int-3C-1R_Ext-1R-R_N-4R!H->C
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
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_6R!H->C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_N-6R!H->C
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_N-6R!H->C_Ext-5R!H-R
                                                L13: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_N-6R!H->C_Ext-7C-R
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_N-6R!H->C_Ext-7C-R_Sp-8R!H-7C
                                                    L14: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_7R!H->C_N-6R!H->C_Ext-7C-R_N-Sp-8R!H-7C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-1R-R_Ext-1R-R_N-4R!H->O_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-4C_N-7R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_4R!H->C_Ext-1R-R
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_Ext-6R!H-R
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_3R!H->O_Ext-3O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-1R-R_Ext-5R!H-R
                        L7: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-4R!H-R_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_4R!H->C
                                        L11: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_4R!H->C_Ext-1R-R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_4R!H->C_Ext-1R-R_Int-5R!H-1R
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_4R!H->C_Ext-1R-R_Sp-4C-3C
                                            L12: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_4R!H->C_Ext-1R-R_N-Sp-4C-3C
                                    L10: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-4R!H->C
                            L8: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-1R-R
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-1R-R_4R!H->C
                                L9: RJ1_1R-inRing_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-Sp-2R!H=1R_N-2R!H->O_N-3R!H->O_Ext-1R-R_N-4R!H->C
        L3: RJ1_N-1R-inRing
            L4: RJ1_N-1R-inRing_1R->C
            L4: RJ1_N-1R-inRing_N-1R->C
"""
)

