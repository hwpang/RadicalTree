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
        Cpdata = ([0.638145,0.273722,-0.256503,-0.352717,-0.455424,-0.977677,-1.89752],'cal/mol/K','+|-',[6.45782,7.71985,7.1649,6.43543,5.82007,5.72463,5.52082]),
        H298 = (35.4333,'kcal/mol','+|-',27.1149),
        S298 = (-6.49654,'cal/mol/K','+|-',12.5005),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
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
        Cpdata = ([0.638145,0.273722,-0.256503,-0.352717,-0.455424,-0.977677,-1.89752],'cal/mol/K','+|-',[6.45782,7.71985,7.1649,6.43543,5.82007,5.72463,5.52082]),
        H298 = (35.4333,'kcal/mol','+|-',27.1149),
        S298 = (-6.49654,'cal/mol/K','+|-',12.5005),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
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
3   R!H u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.94205,-1.67719,-2.09,-1.96008,-1.54962,-1.61451,-1.69544],'cal/mol/K','+|-',[5.93285,7.11276,6.67512,6.26049,6.78152,7.29506,7.14694]),
        H298 = (29.423,'kcal/mol','+|-',28.3047),
        S298 = (-5.88626,'cal/mol/K','+|-',15.66),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S} {3,D}
3   C u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.18628,-4.67004,-5.03725,-4.64429,-3.65844,-3.20051,-2.16974],'cal/mol/K','+|-',[4.65529,3.86289,2.05424,2.67488,7.29063,9.70138,10.2514]),
        H298 = (23.0382,'kcal/mol','+|-',30.9057),
        S298 = (-1.56333,'cal/mol/K','+|-',17.1348),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,D}
3   C   u0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.83286,-5.1269,-5.46065,-5.29961,-4.59975,-3.85475,-2.51998],'cal/mol/K','+|-',[5.77148,4.98342,2.03403,2.00079,9.22179,13.3402,14.3958]),
        H298 = (14.1287,'kcal/mol','+|-',2.28014),
        S298 = (0.558905,'cal/mol/K','+|-',21.8886),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-2R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   u0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79233,-3.36499,-4.74151,-6.007,-7.86014,-8.57122,-7.60966],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (14.9348,'kcal/mol','+|-',2.4),
        S298 = (8.29768,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
smiles: CC(=O)OC([O])=C(O)C=O, Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 6,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.30218,1.31566,0.857243,0.724126,0.559201,-0.0285145,-1.22115],'cal/mol/K','+|-',[2.42617,2.01767,1.71407,2.09039,2.90754,2.95692,4.46162]),
        H298 = (35.8078,'kcal/mol','+|-',23.6335),
        S298 = (-10.2092,'cal/mol/K','+|-',9.75882),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.770983,1.1936,1.07942,1.1722,1.35964,0.798816,0.0210011],'cal/mol/K','+|-',[2.23621,2.79006,2.16597,1.98014,1.23718,1.02924,1.66779]),
        H298 = (29.16,'kcal/mol','+|-',7.51236),
        S298 = (-13.019,'cal/mol/K','+|-',0.996885),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_4R!H->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   O u0 {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5616,2.18003,1.8452,1.87229,1.79705,0.434924,-0.568651],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (31.816,'kcal/mol','+|-',5.2),
        S298 = (-13.3714,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
smiles: CC(=O)OC(OO)C(=O)[CH]O, Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 9,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 {2,S}
2   C                      ux {1,S} {3,D} {4,S}
3   O                      u0 {2,D}
4   [Si,S,N,P,F,Br,I,Cl,O] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0196358,0.207164,0.313633,0.472118,0.922234,1.16271,0.610653],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (26.5039,'kcal/mol','+|-',5.2),
        S298 = (-12.6665,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
smiles: CC(=O)OC(=O)[C](O)C=O, Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 10,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_N-1R->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S} {3,D}
3   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.36456,1.55978,0.412894,-0.172027,-1.04168,-1.68318,-3.70545],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (49.1035,'kcal/mol','+|-',5.2),
        S298 = (-4.58964,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
smiles: [O]C(=O)OC(O)(O)O, Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 11,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.00844,3.20009,2.49375,2.05833,1.18587,-0.0224275,-2.20063],'cal/mol/K','+|-',[4.06271,4.28346,3.5371,2.6924,1.01277,1.22736,2.34319]),
        H298 = (44.4488,'kcal/mol','+|-',12.1619),
        S298 = (-7.41197,'cal/mol/K','+|-',7.25332),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 12,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.6009,4.23457,3.70545,3.0274,1.47338,0.213103,-2.11602],'cal/mol/K','+|-',[5.21033,4.65864,2.80315,1.92697,0.834138,0.195453,3.16329]),
        H298 = (40.0212,'kcal/mol','+|-',11.3696),
        S298 = (-4.7231,'cal/mol/K','+|-',0.318898),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 13,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   O u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.75877,2.58749,2.71439,2.34611,1.17847,0.282207,-0.997631],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (44.041,'kcal/mol','+|-',5.2),
        S298 = (-4.61035,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
smiles: O=C(O)O[C](O)O, Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 14,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.44303,5.88165,4.69651,3.70868,1.7683,0.144,-3.23442],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (36.0015,'kcal/mol','+|-',5.2),
        S298 = (-4.83585,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
smiles: O=[C]OC(O)(O)O, Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 15,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C",
    group = 
"""
1 * O   u1 {2,S}
2   R!H ux {1,S} {3,S}
3   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.41598,2.16561,1.28204,1.08926,0.89836,-0.257958,-2.28523],'cal/mol/K','+|-',[4.09305,4.02724,2.48675,1.73445,1.02894,1.89564,2.52006]),
        H298 = (48.8765,'kcal/mol','+|-',0.898684),
        S298 = (-10.1008,'cal/mol/K','+|-',6.4846),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 16,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_2R!H->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,S}
3   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.968866,0.741762,0.402841,0.476043,0.534574,0.412253,-1.39425],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (49.1942,'kcal/mol','+|-',5.2),
        S298 = (-7.80818,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
smiles: [O]C(O)(O)OC(=O)O, Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_N-2R!H->C",
    group = 
"""
1 * O   u1 {2,S}
2   O   ux {1,S} {3,S}
3   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.86309,3.58945,2.16124,1.70248,1.26215,-0.92817,-3.1762],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (48.5587,'kcal/mol','+|-',5.2),
        S298 = (-12.3935,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
smiles: CC(=O)OC(OO)C(=O)C(O)O[O], Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_3R!H->C_Ext-3C-R_Ext-3C-R_Ext-2R!H-R
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_4R!H->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_N-4R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_N-1R->C
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_Sp-4R!H=3R!H
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_2R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_N-2R!H->C
"""
)

