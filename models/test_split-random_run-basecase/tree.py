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
        Cpdata = ([0.368092,-0.13058,-0.754837,-0.98097,-1.27817,-1.8214,-2.5322],'cal/mol/K','+|-',[6.33708,7.71498,7.42579,7.17513,7.40639,7.4244,6.47558]),
        H298 = (82.0033,'kcal/mol','+|-',31.2375),
        S298 = (-4.85274,'cal/mol/K','+|-',15.4244),
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
        Cpdata = ([0.368092,-0.13058,-0.754837,-0.98097,-1.27817,-1.8214,-2.5322],'cal/mol/K','+|-',[6.33708,7.71498,7.42579,7.17513,7.40639,7.4244,6.47558]),
        H298 = (82.0033,'kcal/mol','+|-',31.2375),
        S298 = (-4.85274,'cal/mol/K','+|-',15.4244),
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
        Cpdata = ([-1.08865,-1.96819,-2.54716,-2.65782,-2.63764,-2.81394,-2.71514],'cal/mol/K','+|-',[5.52565,6.72029,6.55495,6.7075,8.20586,8.91927,8.26181]),
        H298 = (76.0017,'kcal/mol','+|-',29.2935),
        S298 = (-3.44075,'cal/mol/K','+|-',18.7399),
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
        Cpdata = ([-2.77629,-4.2862,-4.95027,-5.04508,-4.89424,-4.78013,-3.76971],'cal/mol/K','+|-',[4.40409,3.72197,1.8385,2.8392,8.07137,10.5858,11.0255]),
        H298 = (70.6662,'kcal/mol','+|-',27.4882),
        S298 = (1.33696,'cal/mol/K','+|-',18.9598),
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
        Cpdata = ([-3.04804,-4.44924,-5.18406,-5.57168,-5.85375,-5.66878,-4.47755],'cal/mol/K','+|-',[5.77148,4.98342,2.03403,2.00079,9.22179,13.3402,14.3958]),
        H298 = (66.7517,'kcal/mol','+|-',2.28014),
        S298 = (3.53536,'cal/mol/K','+|-',21.8886),
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
1 * O   u1 r0 {2,S}
2   C   ux {1,S} {3,D} {6,[S,D,T,B,Q]}
3   C   u0 r0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
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
CC(=O)OC([O])=C(O)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
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
        H298 = (87.9078,'kcal/mol','+|-',23.6335),
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
        H298 = (81.26,'kcal/mol','+|-',7.51236),
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
3   O u0 r0 {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5616,2.18003,1.8452,1.87229,1.79705,0.434924,-0.568651],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.916,'kcal/mol','+|-',5.2),
        S298 = (-13.3714,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C(=O)[CH]O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 9,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_1R->C_Ext-2R!H-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      ux {1,S} {3,D} {4,S}
3   O                      u0 r0 {2,D}
4   [Si,S,N,P,F,Br,I,Cl,O] u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0196358,0.207164,0.313633,0.472118,0.922234,1.16271,0.610653],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.6039,'kcal/mol','+|-',5.2),
        S298 = (-12.6665,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(=O)[C](O)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 10,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-3R!H->C_N-1R->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C ux {1,S} {3,D}
3   O u0 r0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.36456,1.55978,0.412894,-0.172027,-1.04168,-1.68318,-3.70545],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.203,'kcal/mol','+|-',5.2),
        S298 = (-4.58964,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=O)OC(O)(O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
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
        H298 = (96.5488,'kcal/mol','+|-',12.1619),
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
        H298 = (92.1212,'kcal/mol','+|-',11.3696),
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
2   O u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,D}
4   O u0 r0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.75877,2.58749,2.71439,2.34611,1.17847,0.282207,-0.997631],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (96.141,'kcal/mol','+|-',5.2),
        S298 = (-4.61035,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C(O)O[C](O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 14,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]}
2   O u0 r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   O u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.44303,5.88165,4.69651,3.70868,1.7683,0.144,-3.23442],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.1015,'kcal/mol','+|-',5.2),
        S298 = (-4.83585,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]OC(O)(O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
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
        H298 = (100.976,'kcal/mol','+|-',0.898684),
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
1 * O   u1 r0 {2,S}
2   C   ux {1,S} {3,S}
3   R!H u0 r0 {2,S}
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
[O]C(O)(O)OC(=O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-1R->C_N-2R!H->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   ux {1,S} {3,S}
3   R!H u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.86309,3.58945,2.16124,1.70248,1.26215,-0.92817,-3.1762],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.659,'kcal/mol','+|-',5.2),
        S298 = (-12.3935,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C(=O)C(O)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
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

