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
        Cpdata = ([-0.446387,-1.3614,-2.09281,-2.34341,-2.36798,-2.66857,-3.46641],'cal/mol/K','+|-',[6.64323,7.67419,7.55422,7.21908,6.78826,6.47996,6.70509]),
        H298 = (40.9028,'kcal/mol','+|-',25.5049),
        S298 = (-3.28008,'cal/mol/K','+|-',13.4786),
    ),
    shortDesc = """Radical correction fitted to 100 radicals""",
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
        Cpdata = ([-0.446387,-1.3614,-2.09281,-2.34341,-2.36798,-2.66857,-3.46641],'cal/mol/K','+|-',[6.64323,7.67419,7.55422,7.21908,6.78826,6.47996,6.70509]),
        H298 = (40.9028,'kcal/mol','+|-',25.5049),
        S298 = (-3.28008,'cal/mol/K','+|-',13.4786),
    ),
    shortDesc = """Radical correction fitted to 100 radicals""",
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
2   R!H ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07127,-3.5818,-4.09772,-3.85083,-2.95985,-2.42062,-2.00024],'cal/mol/K','+|-',[7.22759,8.4794,8.09288,7.51231,7.56967,8.18196,8.75776]),
        H298 = (33.8729,'kcal/mol','+|-',30.4311),
        S298 = (-2.49774,'cal/mol/K','+|-',17.3205),
    ),
    shortDesc = """Radical correction fitted to 34 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0708759,-1.00542,-1.49341,-1.32432,-0.581665,-0.369428,-0.403547],'cal/mol/K','+|-',[6.22651,7.06912,7.1387,7.30313,7.54302,8.06077,7.49687]),
        H298 = (35.2213,'kcal/mol','+|-',15.1833),
        S298 = (-8.40758,'cal/mol/K','+|-',14.0477),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.37913,-1.37888,-1.86106,-1.64096,-0.736388,-0.4018,-0.294642],'cal/mol/K','+|-',[5.91802,6.63162,6.73293,7.09015,7.70193,8.33938,7.70741]),
        H298 = (34.515,'kcal/mol','+|-',14.5874),
        S298 = (-8.21732,'cal/mol/K','+|-',14.4552),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D}
3   O   ux {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.173626,-0.66773,-1.35163,-1.36446,-0.722964,-0.593421,-0.480726],'cal/mol/K','+|-',[6.00731,6.67853,7.20631,7.87141,8.62769,9.2642,8.39784]),
        H298 = (32.8813,'kcal/mol','+|-',12.7694),
        S298 = (-9.13502,'cal/mol/K','+|-',15.4915),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 6,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.420047,-1.28549,-1.86618,-1.69086,-0.739112,-0.453694,-0.17513],'cal/mol/K','+|-',[4.59209,5.37709,6.56848,7.90757,9.04803,9.66318,8.52321]),
        H298 = (32.0429,'kcal/mol','+|-',11.927),
        S298 = (-9.25161,'cal/mol/K','+|-',16.2255),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_1C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.07461,-2.0819,-5.91392,-8.2058,-9.00894,-9.60608,-8.12276],'cal/mol/K','+|-',[2.10156,1.64697,1.72815,1.74064,1.82729,1.34527,0.67213]),
        H298 = (42.7939,'kcal/mol','+|-',5.08726),
        S298 = (4.86206,'cal/mol/K','+|-',4.87798),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_1C-inRing_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_Int-7R!H-6R!H_Int-7R!H-2R!H_Int-7R!H-6R!H_Int-7R!H-5R!H_Int-7R!H-6R!H_Int-7R!H-4O_Int-7R!H-6R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   C   ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.81762,-1.49961,-5.30293,-7.59039,-8.3629,-9.13046,-7.88513],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (44.5925,'kcal/mol','+|-',5.2),
        S298 = (3.13744,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1[CH]OCC(COO)(OO)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 9,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_1C-inRing_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_Int-7R!H-6R!H_Int-7R!H-2R!H_Int-7R!H-6R!H_Int-7R!H-5R!H_Int-7R!H-6R!H_Int-7R!H-4O_Int-7R!H-6R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-7R!H->C",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   O   ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3316,-2.6642,-6.52491,-8.82121,-9.65498,-10.0817,-8.36039],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (40.9953,'kcal/mol','+|-',5.2),
        S298 = (6.58669,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC1(OO)CO[CH]C(=O)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 10,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.974416,-1.10851,-0.966678,-0.243098,1.09863,1.58017,1.59101],'cal/mol/K','+|-',[4.26624,5.91837,5.79074,5.08987,4.28117,3.75688,3.68083]),
        H298 = (29.6538,'kcal/mol','+|-',5.77175),
        S298 = (-12.388,'cal/mol/K','+|-',9.09101),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 11,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.825582,-0.793602,-0.662924,-0.10943,1.03367,1.45552,1.53754],'cal/mol/K','+|-',[4.60491,6.00685,5.8575,5.26382,4.61386,4.25177,4.2414]),
        H298 = (28.8572,'kcal/mol','+|-',5.52804),
        S298 = (-12.205,'cal/mol/K','+|-',9.46771),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 12,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23752,-0.873184,-0.478097,0.416148,2.10811,2.56818,2.54049],'cal/mol/K','+|-',[6.33327,8.3727,8.01692,6.91592,4.84442,3.99066,4.34115]),
        H298 = (30.1647,'kcal/mol','+|-',6.0813),
        S298 = (-13.548,'cal/mol/K','+|-',11.4839),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 13,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Sp-7R!H-6R!H",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,S}
7   R!H ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32294,-1.10442,-0.793051,0.146922,1.94963,2.36363,2.49789],'cal/mol/K','+|-',[7.74534,10.1917,9.6967,8.36691,5.88217,4.78372,5.3127]),
        H298 = (31.4483,'kcal/mol','+|-',3.99086),
        S298 = (-13.3679,'cal/mol/K','+|-',14.0372),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 14,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,S}
7   R!H ux {6,S}
8   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.194039,1.48144,2.16406,3.19175,4.96404,5.04001,4.09006],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (29.2947,'kcal/mol','+|-',5.2),
        S298 = (-20.3848,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[C](O)C(=O)C(O)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 15,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Sp-7R!H-6R!H_6R!H->C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,S}
7   R!H ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.72446,-6.97474,-6.38841,-4.62327,-0.912188,1.61595,3.97225],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (33.2344,'kcal/mol','+|-',5.2),
        S298 = (-6.34758,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C([CH]O)C(O)=CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 16,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-6R!H->C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]} {7,S}
7   R!H ux {6,S}
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
CC(=O)OC(OO)C(=O)[CH]O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[B,D,T,Q]}
7   R!H ux {6,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.981271,-0.179475,0.466766,1.22383,2.58353,3.18182,2.66832],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (26.3137,'kcal/mol','+|-',5.2),
        S298 = (-14.0881,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC(O)C(=O)[CH]O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 18,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   R!H                    ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O                      ux {2,D}
4   O                      ux {1,[S,D,T,B,Q]}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.27633,-0.687492,-0.90936,-0.810199,-0.398915,-0.0280227,0.200264],'cal/mol/K','+|-',[0.531452,1.72496,2.42621,2.49445,2.66673,2.68981,2.63115]),
        H298 = (27.1139,'kcal/mol','+|-',2.07182),
        S298 = (-10.4144,'cal/mol/K','+|-',6.11761),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 19,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_N-5R!H->C_Ext-1C-R_Ext-6R!H-R",
    group = 
"""
1 * C                      u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   R!H                    ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O                      ux {2,D}
4   O                      ux {1,[S,D,T,B,Q]}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {2,[S,D,T,B,Q]}
6   R!H                    ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H                    ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.284943,-0.274377,-0.307875,-0.205752,0.273715,0.701341,0.936189],'cal/mol/K','+|-',[0.750401,1.362,1.75789,1.91731,1.83429,1.30494,0.920756]),
        H298 = (26.5158,'kcal/mol','+|-',0.0335437),
        S298 = (-12.1556,'cal/mol/K','+|-',1.44506),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 20,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_N-5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * C                      u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   R!H                    ux {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   O                      ux {2,D}
4   O                      ux {1,[S,D,T,B,Q]}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   R!H                    ux {1,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H                    ux {6,[S,D,T,B,Q]}
8   R!H                    ux {5,[S,D,T,B,Q]}
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
CC(=O)OC(=O)[C](O)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 21,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-1C-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D}
3   O   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.89106,-4.7412,-4.5491,-2.91196,-0.189317,1.45851,1.88455],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (33.0737,'kcal/mol','+|-',5.2),
        S298 = (-9.16948,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[C](O)C(O)=CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 22,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-1C-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   R!H                    ux {1,[S,D,T,B,Q]} {3,D}
3   O                      ux {2,D}
4   O                      ux {1,[S,D,T,B,Q]}
5   R!H                    ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   [Si,S,N,O,P,F,Br,I,Cl] ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0996016,0.319824,0.489469,1.49008,2.84128,2.57438,1.67177],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (31.8101,'kcal/mol','+|-',5.2),
        S298 = (-16.8873,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)[C](O)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 23,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_N-4R!H->O",
    group = 
"""
1 * C u1 {2,S} {4,[S,D,T,B,Q]}
2   C ux {1,S} {3,D}
3   O u0 {2,D}
4   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.70403,6.12763,4.30835,2.22599,-0.545336,-2.13042,-3.84229],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (42.1032,'kcal/mol','+|-',5.2),
        S298 = (-7.85248,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(=O)[CH]COO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 24,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_N-3R!H->O",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,D}
3   C ux {2,D}
4   O ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59016,-4.22346,-3.89877,-2.74697,-0.790084,0.364687,0.449694],'cal/mol/K','+|-',[3.16431,1.3586,0.751364,1.39379,2.41095,3.2205,4.8779]),
        H298 = (41.05,'kcal/mol','+|-',16.5055),
        S298 = (-4.54653,'cal/mol/K','+|-',6.4564),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 25,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_N-3R!H->O_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {4,S}
2   C   u0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   O   u0 {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.36955,-4.99944,-3.93924,-2.17066,0.461811,2.10102,3.14235],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (32.1404,'kcal/mol','+|-',5.2),
        S298 = (-7.9037,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC(O)=C(O)[CH]O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 26,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_N-3R!H->O_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D}
4   O   ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34195,-3.93465,-4.25258,-3.5215,-1.94304,-1.07948,-1.61126],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (48.4326,'kcal/mol','+|-',5.2),
        S298 = (-1.46498,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)O[CH]C(O)=CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 27,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.33192,-5.20543,-5.73896,-5.44302,-4.45857,-3.71328,-3.00647],'cal/mol/K','+|-',[6.80782,7.80248,6.96955,5.76826,5.9779,7.32145,9.14273]),
        H298 = (33.0232,'kcal/mol','+|-',37.8475),
        S298 = (1.22662,'cal/mol/K','+|-',15.117),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 28,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.91208,-5.97155,-6.43522,-5.89762,-4.42099,-3.35214,-2.33694],'cal/mol/K','+|-',[7.0394,7.90531,7.02865,5.93305,6.53683,7.98607,9.92376]),
        H298 = (25.3288,'kcal/mol','+|-',25.5688),
        S298 = (1.26678,'cal/mol/K','+|-',16.9273),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 29,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_2R!H-inRing",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux r1 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.2774,-7.36261,-9.5509,-9.91676,-8.13686,-6.19082,-8.61838],'cal/mol/K','+|-',[2.10156,1.64697,1.72815,1.74064,1.82729,1.34527,0.67213]),
        H298 = (22.2126,'kcal/mol','+|-',5.08726),
        S298 = (14.8093,'cal/mol/K','+|-',4.87798),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 30,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_2R!H-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_Int-7R!H-6R!H_Ext-7R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux r1 {1,[S,D,T,B,Q]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.53439,-6.78032,-8.9399,-9.30135,-7.49081,-5.7152,-8.38075],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (24.0112,'kcal/mol','+|-',5.2),
        S298 = (13.0847,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=COCC(COO)(OO)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 31,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.98382,-5.81432,-6.08306,-5.44334,-4.00099,-3.03129,-1.62695],'cal/mol/K','+|-',[7.46087,8.34113,7.09308,5.52795,6.35632,8.22297,9.44736]),
        H298 = (25.681,'kcal/mol','+|-',27.0918),
        S298 = (-0.263926,'cal/mol/K','+|-',14.8115),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 32,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.22698,-6.09721,-6.3546,-5.67146,-4.09214,-3.01248,-1.48273],'cal/mol/K','+|-',[7.4107,8.2552,6.9283,5.34508,6.53082,8.51313,9.69656]),
        H298 = (25.7929,'kcal/mol','+|-',28.0353),
        S298 = (-0.239773,'cal/mol/K','+|-',15.3357),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 33,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.00173,-5.69678,-6.0207,-5.56613,-4.38308,-3.48908,-1.98867],'cal/mol/K','+|-',[7.45533,7.91996,6.39437,4.88791,6.9974,9.256,10.5348]),
        H298 = (22.3632,'kcal/mol','+|-',25.7965),
        S298 = (0.49213,'cal/mol/K','+|-',16.2579),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 34,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.75085,-4.46876,-5.2559,-5.58819,-5.85832,-5.67581,-4.24932],'cal/mol/K','+|-',[8.65629,8.72759,6.80692,5.10706,6.96044,9.2824,11.4016]),
        H298 = (17.8861,'kcal/mol','+|-',17.4709),
        S298 = (3.96545,'cal/mol/K','+|-',15.5906),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 35,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R_5R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
5   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.22684,-5.94943,-4.9572,-2.76693,0.813868,2.48061,4.55767],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (35.376,'kcal/mol','+|-',5.2),
        S298 = (-10.6339,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=C(O)C=O)C(O)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 36,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R_N-5R!H->C",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C                      ux {2,D} {4,[S,D,T,B,Q]}
4   C                      ux {3,[S,D,T,B,Q]}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.42906,-4.27633,-5.29472,-5.95485,-6.72547,-6.73585,-5.39391],'cal/mol/K','+|-',[9.4837,9.77446,7.70604,5.03753,4.10761,6.54833,9.37606]),
        H298 = (15.613,'kcal/mol','+|-',8.96812),
        S298 = (5.86284,'cal/mol/K','+|-',9.74909),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 37,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-3C-R",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C                      ux {2,D} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C                      ux {3,[S,D,T,B,Q]}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {2,[S,D,T,B,Q]}
6   R!H                    ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.45017,-5.24829,-6.12163,-6.6135,-7.15812,-7.01358,-5.3872],'cal/mol/K','+|-',[7.71093,8.60075,6.29016,2.7398,3.42237,7.4985,11.2146]),
        H298 = (14.7414,'kcal/mol','+|-',8.03893),
        S298 = (6.61393,'cal/mol/K','+|-',9.92612),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 38,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-3C-R_Ext-4C-R",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C                      ux {2,D} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C                      ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {2,[S,D,T,B,Q]}
6   R!H                    ux {3,[S,D,T,B,Q]}
7   R!H                    ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.98004,-4.63227,-5.66179,-6.38968,-7.30353,-7.3643,-5.74832],'cal/mol/K','+|-',[9.56485,10.2056,7.41117,3.08178,4.48252,9.71955,14.9897]),
        H298 = (13.947,'kcal/mol','+|-',7.95545),
        S298 = (6.60658,'cal/mol/K','+|-',13.6187),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 39,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-3C-R_Ext-4C-R_Ext-5BrClFINOPSSi-R",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C                      ux {2,D} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C                      ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {2,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
6   R!H                    ux {3,[S,D,T,B,Q]}
7   R!H                    ux {4,[S,D,T,B,Q]}
8   R!H                    ux {5,[S,D,T,B,Q]}
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
CC(=O)OC([O])=C(O)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 40,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.85382,-9.12515,-8.71905,-6.56441,-2.19248,0.167772,1.60044],'cal/mol/K','+|-',[6.94938,10.5379,10.7815,10.0904,8.16381,5.52345,5.05504]),
        H298 = (41.1933,'kcal/mol','+|-',13.6254),
        S298 = (-3.21902,'cal/mol/K','+|-',20.1805),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 41,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   C   ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.39684,-5.39943,-4.9072,-2.99693,0.693868,2.12061,3.38767],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (36.376,'kcal/mol','+|-',5.2),
        S298 = (-10.3539,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=C(O)C(=O)C(O)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 42,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   R!H ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,D}
5   C   ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.31079,-12.8509,-12.5309,-10.1319,-5.07882,-1.78506,-0.18679],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (46.0106,'kcal/mol','+|-',5.2),
        S298 = (3.91588,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C=C(O)C(O)=CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 43,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C                      ux {2,D} {4,[S,D,T,B,Q]}
4   C                      ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.72557,-6.97018,-6.43831,-4.83668,-1.56799,0.4105,2.1703],'cal/mol/K','+|-',[1.52629,1.68793,1.76811,2.02293,1.94882,0.923405,2.59427]),
        H298 = (22.7853,'kcal/mol','+|-',32.7387),
        S298 = (-7.09995,'cal/mol/K','+|-',1.80916),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 44,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=4C",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C                      ux {2,D} {4,[S,D,T,B,Q]}
4   C                      ux {3,[S,D,T,B,Q]} {5,D}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.13869,-7.37034,-6.8013,-5.27009,-1.98787,0.400347,2.89523],'cal/mol/K','+|-',[0.750401,1.362,1.75789,1.91731,1.83429,1.30494,0.920756]),
        H298 = (13.3344,'kcal/mol','+|-',0.0335437),
        S298 = (-6.66896,'cal/mol/K','+|-',1.44506),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 45,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=4C_Ext-4C-R_Ext-6R!H-R",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C                      ux {2,D} {4,[S,D,T,B,Q]}
4   C                      ux {3,[S,D,T,B,Q]} {5,D} {6,[S,D,T,B,Q]}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {4,D}
6   R!H                    ux {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
7   R!H                    ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.87338,-6.8888,-6.17979,-4.59222,-1.33935,0.861715,2.5697],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (13.3225,'kcal/mol','+|-',5.2),
        S298 = (-7.17987,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(=O)C(O)=C[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 46,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=4C",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C                      ux {2,D} {4,[S,D,T,B,Q]}
4   C                      ux {3,[S,D,T,B,Q]} {5,S}
5   [Si,S,N,O,P,F,Br,I,Cl] ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.89933,-6.16985,-5.71233,-3.96984,-0.728227,0.430804,0.720431],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (41.687,'kcal/mol','+|-',5.2),
        S298 = (-7.96192,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C(O)=C[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 47,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->C",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D}
3   C                      ux {2,D} {4,[S,D,T,B,Q]}
4   [Si,S,N,O,P,F,Br,I,Cl] ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.25522,-7.92512,-7.87878,-6.1523,-2.76408,-0.836912,0.826772],'cal/mol/K','+|-',[8.78083,10.7945,10.0557,8.43482,4.45685,2.62907,3.97735]),
        H298 = (41.4486,'kcal/mol','+|-',12.8172),
        S298 = (-3.58078,'cal/mol/K','+|-',11.4635),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 48,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C                      ux {2,D} {4,[S,D,T,B,Q]}
4   [Si,S,N,O,P,F,Br,I,Cl] ux {3,[S,D,T,B,Q]}
5   R!H                    ux {2,[S,D,T,B,Q]} {6,D}
6   R!H                    ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.2223,-14.0215,-13.6058,-11.0008,-5.31573,-1.25438,1.94227],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (48.1323,'kcal/mol','+|-',5.2),
        S298 = (2.93024,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=CO)C(O)=CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 49,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C                      ux {2,D} {4,[S,D,T,B,Q]}
4   [Si,S,N,O,P,F,Br,I,Cl] ux {3,[S,D,T,B,Q]}
5   R!H                    ux {2,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H                    ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.77169,-4.8769,-5.01527,-3.72805,-1.48826,-0.628178,0.269022],'cal/mol/K','+|-',[2.48497,3.1695,2.33297,1.11556,0.813392,3.57467,4.91656]),
        H298 = (38.1067,'kcal/mol','+|-',7.78001),
        S298 = (-6.83628,'cal/mol/K','+|-',2.90895),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 50,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C                      ux {2,D} {4,[S,D,T,B,Q]}
4   [Si,S,N,O,P,F,Br,I,Cl] ux {3,[S,D,T,B,Q]}
5   R!H                    ux {2,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.65026,-5.99749,-5.8401,-4.12246,-1.20068,0.63566,2.00729],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (35.356,'kcal/mol','+|-',5.2),
        S298 = (-7.86475,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=CO)C(O)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 51,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   R!H                    ux r0 {1,[S,D,T,B,Q]} {3,D} {5,[S,D,T,B,Q]}
3   C                      ux {2,D} {4,[S,D,T,B,Q]}
4   [Si,S,N,O,P,F,Br,I,Cl] ux {3,[S,D,T,B,Q]}
5   R!H                    ux {2,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O                      ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.89312,-3.75631,-4.19044,-3.33364,-1.77583,-1.89202,-1.46924],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (40.8573,'kcal/mol','+|-',5.2),
        S298 = (-5.80781,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C([O])=CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 52,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_N-3R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S} {3,D}
3   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3254,-2.55578,-3.33089,-3.87078,-4.58852,-4.96227,-5.32208],'cal/mol/K','+|-',[6.33002,7.0601,6.42234,6.34509,6.08447,5.62518,2.77326]),
        H298 = (59.6345,'kcal/mol','+|-',18.0657),
        S298 = (1.0877,'cal/mol/K','+|-',9.73929),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 53,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_N-3R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,D} {4,S}
3   O   u0 {2,D}
4   O   u0 {2,S} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
[O]C(=O)OC(O)(O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 54,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.285721,-0.360977,-1.18947,-1.66423,-2.10131,-2.78029,-4.12701],'cal/mol/K','+|-',[5.8695,6.42126,6.62039,6.72829,6.41937,5.63336,5.11577]),
        H298 = (44.0702,'kcal/mol','+|-',20.2653),
        S298 = (-3.63256,'cal/mol/K','+|-',11.4803),
    ),
    shortDesc = """Radical correction fitted to 66 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 55,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.576252,-1.2891,-1.96243,-2.36891,-2.65615,-3.15536,-4.11681],'cal/mol/K','+|-',[5.65452,6.24755,6.62828,6.7373,6.18686,5.34359,5.13699]),
        H298 = (39.7285,'kcal/mol','+|-',15.9745),
        S298 = (-2.96929,'cal/mol/K','+|-',11.239),
    ),
    shortDesc = """Radical correction fitted to 40 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 56,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.148541,-0.492324,-0.9077,-1.12419,-1.47946,-2.19149,-3.7605],'cal/mol/K','+|-',[5.70512,6.91362,7.0705,6.55125,5.28371,4.26301,6.28798]),
        H298 = (44.4938,'kcal/mol','+|-',15.7724),
        S298 = (-2.78632,'cal/mol/K','+|-',10.3179),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 57,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.325435,-0.0688259,-0.658611,-1.16272,-1.89193,-2.66188,-4.8536],'cal/mol/K','+|-',[5.19259,7.03897,7.98878,7.87471,6.27732,4.72074,6.20763]),
        H298 = (46.6418,'kcal/mol','+|-',10.7343),
        S298 = (-0.405074,'cal/mol/K','+|-',8.57864),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 58,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0830864,-0.225192,-0.864446,-1.46032,-2.29604,-3.01956,-5.2642],'cal/mol/K','+|-',[5.2888,6.36774,6.93258,6.76809,5.21759,4.17306,6.47062]),
        H298 = (46.0537,'kcal/mol','+|-',6.52839),
        S298 = (0.131563,'cal/mol/K','+|-',6.19436),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 59,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {5,S}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
5   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0983,-1.31179,-1.69723,-2.10732,-2.52349,-3.02223,-5.91082],'cal/mol/K','+|-',[2.96274,5.16951,7.3838,7.66794,5.92357,4.79308,8.92801]),
        H298 = (46.6047,'kcal/mol','+|-',3.46351),
        S298 = (0.786948,'cal/mol/K','+|-',6.64526),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 60,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C_1C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {5,S}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
5   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.86205,-3.49121,-5.18174,-5.80402,-5.36388,-5.27818,-10.7018],'cal/mol/K','+|-',[2.24801,3.77934,5.29593,5.2094,3.77978,2.82606,1.74299]),
        H298 = (46.4605,'kcal/mol','+|-',4.13432),
        S298 = (3.61819,'cal/mol/K','+|-',3.92498),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 61,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C_1C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {5,S} {6,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
5   R!H ux {1,S}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.45398,-3.8566,-5.53372,-6.13772,-5.5895,-5.35997,-10.8464],'cal/mol/K','+|-',[1.30301,5.03614,7.28837,7.18354,5.22989,3.97652,2.36093]),
        H298 = (45.5053,'kcal/mol','+|-',3.50515),
        S298 = (3.53994,'cal/mol/K','+|-',5.53751),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 62,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C_1C-inRing_Ext-1C-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]} {5,S} {6,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S} {7,[S,D,T,B,Q]}
4   O   ux {3,S}
5   R!H ux {1,S}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9933,-2.07605,-2.9569,-3.59796,-3.74045,-3.95406,-10.0117],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (44.266,'kcal/mol','+|-',5.2),
        S298 = (1.58213,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1COOC(OC(C)=O)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 63,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C_N-1C-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {5,S}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
5   R!H ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.695939,-0.163605,0.138516,-0.159784,-1.02709,-1.83374,-3.38681],'cal/mol/K','+|-',[4.21097,4.71941,4.41882,4.29878,3.78357,3.62983,4.09856]),
        H298 = (46.6806,'kcal/mol','+|-',4.52817),
        S298 = (-0.704633,'cal/mol/K','+|-',6.70013),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 64,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C_N-1C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {5,S} {6,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,S}
4   O   ux {3,S}
5   R!H ux {1,S}
6   R!H ux {1,[S,D,T,B,Q]}
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
O=C(O)O[C](O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 65,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_N-Sp-5R!H-1C",
    group = 
"""
1 * C u1 {2,[S,D,T,B,Q]} {5,[B,D,T,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   O u0 {3,S}
5   O u0 {1,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.61742,1.18603,0.217134,-0.620035,-2.00065,-3.01609,-4.42439],'cal/mol/K','+|-',[7.56918,8.89078,8.36187,7.76775,6.37711,5.08895,2.55926]),
        H298 = (45.3381,'kcal/mol','+|-',11.6955),
        S298 = (-0.719621,'cal/mol/K','+|-',7.60657),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 66,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_N-Sp-5R!H-1C_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {5,D}
2   O   u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   O   u0 {3,S}
5   O   u0 {1,D}
6   R!H ux {3,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
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
O=[C]OC(O)(O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 67,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_N-Sp-5R!H-1C_Ext-3R!H-R_Sp-6R!H-3R!H",
    group = 
"""
1 * C u1 {2,S} {5,D}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {6,S}
4   O u0 {3,S}
5   O u0 {1,D}
6   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.68528,5.76464,4.45847,3.14048,0.837071,-0.946603,-2.95487],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (45.2419,'kcal/mol','+|-',5.2),
        S298 = (-4.53445,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]OC(O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 68,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_N-Sp-5R!H-1C_Ext-3R!H-R_N-Sp-6R!H-3R!H",
    group = 
"""
1 * C u1 {2,S} {5,D}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S} {6,[B,D,T,Q]}
4   O u0 {3,S}
5   O u0 {1,D}
6   O u0 {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0640284,-0.789543,-1.64053,-2.34318,-3.40798,-4.13009,-4.99092],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (47.3475,'kcal/mol','+|-',2.4),
        S298 = (0.969835,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]OC(=O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 69,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_N-Sp-4O-3R!H",
    group = 
"""
1 * C u1 {2,S}
2   O ux {1,S} {3,S}
3   C u0 {2,S} {4,D}
4   O ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.56859,0.733274,0.397241,0.363886,0.181037,-0.827122,-2.74742],'cal/mol/K','+|-',[5.31066,11.5507,13.9676,13.6391,10.462,6.55321,3.58492]),
        H298 = (49.6585,'kcal/mol','+|-',23.8602),
        S298 = (-3.15782,'cal/mol/K','+|-',16.8317),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 70,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_N-Sp-4O-3R!H_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   O   ux {1,S} {3,S}
3   C   u0 {2,S} {4,D}
4   O   ux {3,D}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.00538,4.01874,4.38101,4.25533,3.15569,1.05557,-1.76406],'cal/mol/K','+|-',[2.61957,2.78809,3.04949,2.93459,2.55727,0.905843,1.57967]),
        H298 = (42.7836,'kcal/mol','+|-',2.06515),
        S298 = (-7.62479,'cal/mol/K','+|-',9.36587),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 71,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_N-Sp-4O-3R!H_Ext-1C-R_Ext-1C-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   O   ux {1,S} {3,S}
3   C   u0 {2,S} {4,D} {7,[S,D,T,B,Q]}
4   O   ux {3,D}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.93153,5.00448,5.45917,5.29287,4.05982,1.37583,-2.32255],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (42.0535,'kcal/mol','+|-',5.2),
        S298 = (-10.9361,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)O[C](COO)C(C)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 72,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.893844,-1.15825,-1.29938,-1.06361,-0.830889,-1.45183,-2.04166],'cal/mol/K','+|-',[6.83092,7.40733,6.30643,4.80169,3.61815,3.45189,5.29291]),
        H298 = (41.1162,'kcal/mol','+|-',21.2139),
        S298 = (-6.53069,'cal/mol/K','+|-',8.70636),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 73,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.44507,-1.71518,-1.73915,-1.3245,-0.839601,-1.35148,-1.72479],'cal/mol/K','+|-',[7.15094,7.88644,6.80848,5.33794,4.16763,3.90708,5.83614]),
        H298 = (43.4975,'kcal/mol','+|-',18.8953),
        S298 = (-7.17533,'cal/mol/K','+|-',9.35245),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 74,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R",
    group = 
"""
1 * O     u1 {2,[S,D,T,B,Q]}
2   O     u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C     ux {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O     u0 {3,S}
5   C     ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   [C,O] ux {5,[S,D,T,B,Q]}
7   [C,O] u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09511,-3.00703,-3.10701,-2.05265,-0.173804,-0.0622657,0.216349],'cal/mol/K','+|-',[9.11885,9.4476,7.43236,5.33552,2.87178,3.24404,6.59638]),
        H298 = (52.655,'kcal/mol','+|-',7.69675),
        S298 = (-9.13647,'cal/mol/K','+|-',7.38927),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 75,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_8R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O u0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
7   C u0 {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5669,-6.21115,-5.36676,-3.36873,-0.107879,1.24487,3.04398],'cal/mol/K','+|-',[2.67388,3.38297,3.40703,3.17781,2.57427,1.63587,0.235552]),
        H298 = (52.2575,'kcal/mol','+|-',3.69389),
        S298 = (-10.1116,'cal/mol/K','+|-',2.30372),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 76,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_8R!H->C_Sp-6R!H-5C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O u0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,S} {7,[S,D,T,B,Q]}
6   O ux {5,S}
7   C u0 {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.51225,-7.4072,-6.57132,-4.49226,-1.01802,0.666506,3.12726],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (50.9515,'kcal/mol','+|-',5.2),
        S298 = (-10.926,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(O)C(O)=C(O)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 77,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_8R!H->C_N-Sp-6R!H-5C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O u0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,[B,D,T,Q]} {7,[S,D,T,B,Q]}
6   O ux {5,[B,D,T,Q]}
7   C u0 {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.62154,-5.01509,-4.16219,-2.24521,0.802262,1.82324,2.9607],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (53.5635,'kcal/mol','+|-',5.2),
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
    index = 78,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_N-8R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O u0 {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
7   C u0 {5,[S,D,T,B,Q]} {8,S}
8   O ux {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.37668,0.197082,-0.847268,-0.736572,-0.23973,-1.36941,-2.61129],'cal/mol/K','+|-',[7.03261,9.59507,8.50934,6.89868,4.24795,1.248,1.59783]),
        H298 = (53.0524,'kcal/mol','+|-',12.7101),
        S298 = (-8.1614,'cal/mol/K','+|-',11.9702),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 79,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_N-8R!H->C_Ext-4O-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O   u0 {3,S} {9,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   O   ux {5,[S,D,T,B,Q]}
7   C   u0 {5,[S,D,T,B,Q]} {8,S}
8   O   ux {7,S}
9   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.10972,-3.19529,-3.85577,-3.17562,-1.74161,-1.81064,-2.04637],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (57.5462,'kcal/mol','+|-',5.2),
        S298 = (-3.92931,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(O[O])C(O)=CO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 80,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   C   ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C   ux {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.91677,-1.85045,-1.76177,-1.76504,-2.18898,-2.77396,-3.22609],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (37.245,'kcal/mol','+|-',2.4),
        S298 = (-4.02657,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(CC(C)OO)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 81,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_N-5R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   O u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   O u0 {3,S}
5   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.77809,1.54128,0.83231,0.200954,-0.78866,-1.93828,-3.57762],'cal/mol/K','+|-',[2.79352,2.36595,1.54592,0.432008,0.792198,1.43591,0.293756]),
        H298 = (29.5739,'kcal/mol','+|-',19.8565),
        S298 = (-3.40601,'cal/mol/K','+|-',0.0103228),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 82,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_N-5R!H->C_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   O   u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   O   u0 {3,S}
5   O   ux {3,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.790431,0.704796,0.285743,0.0482161,-0.508576,-1.4306,-3.47376],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (22.5536,'kcal/mol','+|-',5.2),
        S298 = (-3.40966,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(O)(O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 83,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.977301,-2.0362,-2.95141,-3.53603,-3.75948,-4.05915,-4.45091],'cal/mol/K','+|-',[5.73565,5.42361,5.78774,6.28887,6.35738,5.78223,3.94624]),
        H298 = (35.2602,'kcal/mol','+|-',10.2281),
        S298 = (-3.14085,'cal/mol/K','+|-',12.4886),
    ),
    shortDesc = """Radical correction fitted to 21 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 84,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.588129,-4.0076,-7.53274,-9.63508,-10.1701,-10.7069,-8.51414],'cal/mol/K','+|-',[5.97165,4.26806,2.7728,1.77523,0.707306,0.166737,1.39199]),
        H298 = (50.6164,'kcal/mol','+|-',11.2601),
        S298 = (7.07674,'cal/mol/K','+|-',6.21122),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 85,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_1R->C",
    group = 
"""
1 * C                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.69943,-2.49861,-6.5524,-9.00744,-9.92003,-10.6479,-9.00628],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (54.5975,'kcal/mol','+|-',5.2),
        S298 = (9.27274,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1CO[CH]C(COO)(OO)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 86,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-1R->C",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r1 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.52317,-5.51659,-8.51307,-10.2627,-10.4202,-10.7658,-8.02199],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (46.6354,'kcal/mol','+|-',5.2),
        S298 = (4.88074,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC1(OO)COCC(=O)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 87,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08137,-1.90514,-2.64684,-3.13056,-3.33329,-3.61719,-4.18078],'cal/mol/K','+|-',[5.77621,5.45931,5.40848,5.55696,5.54024,4.71441,3.3989]),
        H298 = (34.2393,'kcal/mol','+|-',5.87259),
        S298 = (-3.82014,'cal/mol/K','+|-',11.5762),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 88,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,D}
6   R!H                    ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.66299,1.53511,1.15286,1.15807,1.15212,0.702854,-0.514416],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (33.9298,'kcal/mol','+|-',5.2),
        S298 = (-18.5503,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C(CC(=O)OC=O)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 89,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H                    ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.17574,-2.02343,-2.77749,-3.27802,-3.48752,-3.76573,-4.30685],'cal/mol/K','+|-',[5.78998,5.39839,5.30645,5.40647,5.36332,4.49272,3.14687]),
        H298 = (34.2499,'kcal/mol','+|-',5.98848),
        S298 = (-3.31366,'cal/mol/K','+|-',10.2599),
    ),
    shortDesc = """Radical correction fitted to 18 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 90,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06525,-2.017,-2.7597,-3.15718,-2.94004,-3.08158,-3.7835],'cal/mol/K','+|-',[6.49869,6.63788,6.74495,6.72187,5.83295,4.06317,2.78127]),
        H298 = (33.8124,'kcal/mol','+|-',5.3049),
        S298 = (-5.06066,'cal/mol/K','+|-',11.2134),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 91,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C                      ux {5,[S,T,Q,B]}
7   R!H                    ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.10967,-4.71454,-5.07916,-5.17918,-4.11097,-2.94245,-3.09102],'cal/mol/K','+|-',[6.19535,7.7449,8.91466,9.56151,9.23493,6.27751,2.72251]),
        H298 = (32.8369,'kcal/mol','+|-',6.47294),
        S298 = (-2.13001,'cal/mol/K','+|-',19.6584),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 92,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_Ext-7R!H-R_8R!H->C",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C                      ux {5,[S,T,Q,B]}
7   R!H                    ux {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   C                      ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.82804,-0.547515,-0.148543,0.266682,1.44059,1.17964,-1.14031],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (29.0955,'kcal/mol','+|-',5.2),
        S298 = (-13.1338,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(CCO[O])COO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 93,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_Ext-7R!H-R_N-8R!H->C",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C                      ux {5,[S,T,Q,B]}
7   R!H                    ux {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   [Si,S,N,O,P,F,Br,I,Cl] ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.68596,-5.44631,-5.94502,-6.13553,-5.08588,-3.66632,-3.43359],'cal/mol/K','+|-',[6.44501,7.9619,8.95898,9.35481,8.52301,5.07154,1.76063]),
        H298 = (33.4939,'kcal/mol','+|-',6.24105),
        S298 = (-0.197624,'cal/mol/K','+|-',19.5482),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 94,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_Ext-7R!H-R_N-8R!H->C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]} {7,[S,D,T,B,Q]}
6   C                      ux {5,[S,T,Q,B]}
7   R!H                    ux {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   [Si,S,N,O,P,F,Br,I,Cl] ux {7,[S,D,T,B,Q]}
9   R!H                    ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.928957,-0.805061,-0.722543,-0.682314,-0.117547,-0.70996,-2.40726],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (29.8558,'kcal/mol','+|-',5.2),
        S298 = (-11.5929,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(CO[O])C(C)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 95,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]}
7   R!H                    ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8719,-0.697819,-1.93777,-2.67095,-2.98593,-3.73654,-4.50331],'cal/mol/K','+|-',[4.19788,4.42738,4.02392,3.43191,2.88173,2.67302,2.71449]),
        H298 = (34.6906,'kcal/mol','+|-',5.617),
        S298 = (-5.89267,'cal/mol/K','+|-',4.56317),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 96,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]}
7   R!H                    ux {4,[S,D,T,B,Q]}
8   R!H                    ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4807,-0.757092,-2.32925,-3.46135,-4.28919,-5.3518,-6.19077],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (38.9049,'kcal/mol','+|-',5.2),
        S298 = (-6.07874,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(C)(CO[O])COO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 97,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_7R!H->C",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]}
7   C                      ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.52131,-0.492035,-1.79985,-2.5936,-2.89943,-3.74877,-5.00798],'cal/mol/K','+|-',[2.02115,1.09498,2.26855,2.60996,2.86979,2.40214,0.17009]),
        H298 = (32.361,'kcal/mol','+|-',5.06531),
        S298 = (-5.29132,'cal/mol/K','+|-',1.96595),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 98,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_7R!H->C_Ext-7C-R",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]}
7   C                      ux {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H                    ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.2359,-0.879168,-2.6019,-3.51636,-3.91406,-4.59805,-5.06812],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (34.1519,'kcal/mol','+|-',5.2),
        S298 = (-4.59625,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(COO)C(C)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 99,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]}
7   O                      ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.553963,-0.756535,-1.9185,-2.565,-2.79756,-3.46325,-4.05385],'cal/mol/K','+|-',[5.09137,5.57098,4.97222,4.11329,3.17785,2.79857,2.85106]),
        H298 = (34.7648,'kcal/mol','+|-',4.7362),
        S298 = (-6.0621,'cal/mol/K','+|-',5.63906),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 100,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-7O-R",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]}
7   O                      ux {4,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H                    ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.65072,3.14614,1.43818,0.0447602,-1.40527,-3.40608,-4.97103],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (35.8764,'kcal/mol','+|-',5.2),
        S298 = (-8.27805,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C(C)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 101,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-6C-R_Ext-6C-R",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]} {8,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
7   O                      ux {4,[S,D,T,B,Q]}
8   R!H                    ux {6,[S,D,T,B,Q]}
9   R!H                    ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.627718,-2.15504,-3.15393,-3.52671,-3.32594,-3.51425,-3.55518],'cal/mol/K','+|-',[4.40763,4.14409,3.833,3.48487,3.47332,3.60644,3.09058]),
        H298 = (35.0597,'kcal/mol','+|-',5.31744),
        S298 = (-5.08977,'cal/mol/K','+|-',6.13801),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 102,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-6C-R_Ext-6C-R_Sp-8R!H=6C",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]} {8,D} {9,[S,D,T,B,Q]}
7   O                      ux {4,[S,D,T,B,Q]}
8   R!H                    ux {6,D}
9   R!H                    ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.332106,-1.30608,-2.52443,-3.1436,-3.3937,-3.69513,-3.94827],'cal/mol/K','+|-',[2.65151,2.90904,3.53942,3.83328,4.24096,4.32716,3.25868]),
        H298 = (34.2987,'kcal/mol','+|-',5.33992),
        S298 = (-5.19047,'cal/mol/K','+|-',7.5013),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 103,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-6C-R_Ext-6C-R_Sp-8R!H=6C_Ext-3R!H-R",
    group = 
"""
1  * R                      u1 {2,[S,D,T,B,Q]}
2    O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3    R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
4    [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5    R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6    C                      ux {5,[S,T,Q,B]} {8,D} {9,[S,D,T,B,Q]}
7    O                      ux {4,[S,D,T,B,Q]}
8    R!H                    ux {6,D}
9    R!H                    ux {6,[S,D,T,B,Q]}
10   R!H                    ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.369694,-1.9256,-3.50329,-4.2473,-4.61766,-4.94123,-4.8648],'cal/mol/K','+|-',[3.74528,2.77733,1.43501,0.390464,0.133376,0.427386,1.03805]),
        H298 = (35.4213,'kcal/mol','+|-',5.17557),
        S298 = (-3.02931,'cal/mol/K','+|-',0.666789),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 104,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-6C-R_Ext-6C-R_Sp-8R!H=6C_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  * R                      u1 {2,[S,D,T,B,Q]}
2    O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3    R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {10,[S,D,T,B,Q]} {11,[S,D,T,B,Q]}
4    [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5    R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6    C                      ux {5,[S,T,Q,B]} {8,D} {9,[S,D,T,B,Q]}
7    O                      ux {4,[S,D,T,B,Q]}
8    R!H                    ux {6,D}
9    R!H                    ux {6,[S,D,T,B,Q]}
10   R!H                    ux {3,[S,D,T,B,Q]}
11   R!H                    ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.69385,-0.943665,-2.99593,-4.10925,-4.66482,-5.09233,-5.2318],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (33.5915,'kcal/mol','+|-',5.2),
        S298 = (-2.79357,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(=O)C(C)(C)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 105,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-6C-R_Ext-6C-R_N-Sp-8R!H=6C",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]} {8,S} {9,[S,D,T,B,Q]}
7   O                      ux {4,[S,D,T,B,Q]}
8   R!H                    ux {6,S}
9   R!H                    ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.50719,-4.70192,-5.04241,-4.67603,-3.12265,-2.97161,-2.3759],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (37.3426,'kcal/mol','+|-',5.2),
        S298 = (-4.78767,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)C(OO)OC(=O)CO[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 106,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-3R!H-R",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   C                      ux {5,[S,T,Q,B]}
7   R!H                    ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.01117,2.46218,3.48883,3.82715,3.13985,0.757141,-2.45585],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (32.5385,'kcal/mol','+|-',5.2),
        S298 = (-13.8803,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC(COO)O[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 107,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O                      ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34739,-2.03342,-2.80512,-3.46576,-4.33812,-4.82868,-5.11995],'cal/mol/K','+|-',[5.41877,3.17201,1.86123,2.75945,4.77649,5.04238,3.48774]),
        H298 = (34.9297,'kcal/mol','+|-',7.96733),
        S298 = (-0.599422,'cal/mol/K','+|-',5.72107),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 108,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C_Ext-3R!H-R",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O                      ux {5,[S,T,Q,B]}
7   R!H                    ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.187836,-1.74341,-3.25068,-4.55824,-6.22579,-6.76376,-6.37508],'cal/mol/K','+|-',[1.43236,0.59246,0.872845,0.23363,1.55863,0.791775,0.602702]),
        H298 = (34.6263,'kcal/mol','+|-',2.09563),
        S298 = (0.873659,'cal/mol/K','+|-',7.33437),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 109,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O                      ux {5,[S,T,Q,B]}
7   R!H                    ux {3,[S,D,T,B,Q]}
8   R!H                    ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.647131,-2.08877,-3.75949,-4.69443,-5.31722,-6.30221,-6.72642],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (33.4047,'kcal/mol','+|-',5.2),
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
    index = 110,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O                      ux {5,[S,T,Q,B]}
7   C                      ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.69522,-3.12948,-2.73581,-2.48993,-2.34451,-2.51797,-3.46656],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (33.171,'kcal/mol','+|-',2.4),
        S298 = (-1.36979,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C(C)CO[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 111,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_N-7R!H->C",
    group = 
"""
1 * R                      u1 {2,[S,D,T,B,Q]}
2   O                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H                    ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux r0 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   R!H                    ux {4,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   O                      ux {5,[S,T,Q,B]}
7   [Si,S,N,O,P,F,Br,I,Cl] ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.07138,1.46056,-0.593221,-1.82573,-2.94772,-4.65694,-5.73445],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (44.9136,'kcal/mol','+|-',5.2),
        S298 = (-5.37134,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(OO)C(=O)CO[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 112,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O",
    group = 
"""
1 * R   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.0903,1.58208,0.428758,-0.188954,-0.939731,-1.99506,-4.14835],'cal/mol/K','+|-',[4.66205,5.01572,5.50249,5.87731,6.46729,6.06652,5.24504]),
        H298 = (53.1597,'kcal/mol','+|-',15.8814),
        S298 = (-5.02116,'cal/mol/K','+|-',11.8508),
    ),
    shortDesc = """Radical correction fitted to 26 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 113,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61367,2.97774,1.33209,0.285022,-1.02236,-2.48906,-5.39343],'cal/mol/K','+|-',[4.01775,6.18601,8.26476,9.22894,10.4014,9.76761,6.80935]),
        H298 = (46.1419,'kcal/mol','+|-',10.8874),
        S298 = (-1.73402,'cal/mol/K','+|-',17.1993),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 114,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_3R!H->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.7503,4.30722,3.70639,3.52639,3.46602,1.76583,-1.57872],'cal/mol/K','+|-',[1.53817,8.44687,12.9876,14.182,14.1319,12.3717,6.79771]),
        H298 = (48.7898,'kcal/mol','+|-',16.5147),
        S298 = (-10.2278,'cal/mol/K','+|-',16.4264),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 115,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_3R!H->C_2C-inRing",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.41407,0.517131,-2.62943,-3.5513,-3.66919,-4.4677,-5.06159],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (58.2785,'kcal/mol','+|-',5.2),
        S298 = (-2.03933,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C1C(O)OOC1(O)[CH]O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 116,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_3R!H->C_N-2C-inRing",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.41841,6.20227,6.8743,7.06524,7.03362,4.88259,0.162716],'cal/mol/K','+|-',[1.44512,7.51735,9.82341,10.0843,9.69315,8.54255,4.4312]),
        H298 = (44.0455,'kcal/mol','+|-',2.29313),
        S298 = (-14.322,'cal/mol/K','+|-',11.7196),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 117,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_3R!H->C_N-2C-inRing_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.90748,3.54448,3.4012,3.4999,3.60657,1.86234,-1.40395],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (44.8562,'kcal/mol','+|-',5.2),
        S298 = (-10.1785,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(C[CH]COO)OO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 118,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5604,2.45939,0.406375,-0.978761,-2.77234,-4.14801,-6.88075],'cal/mol/K','+|-',[5.31141,5.54921,5.19935,4.97926,5.57376,6.04232,2.9706]),
        H298 = (45.1095,'kcal/mol','+|-',8.14368),
        S298 = (1.57763,'cal/mol/K','+|-',12.0532),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 119,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C_1C-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.33794,2.63206,1.671,1.71376,1.22553,-0.290088,-4.913],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (47.5076,'kcal/mol','+|-',5.2),
        S298 = (-6.76959,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC1OOC(O)[C]1O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 120,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C_N-1C-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.74301,2.43359,0.217469,-1.38096,-3.36954,-4.7243,-7.17469],'cal/mol/K','+|-',[6.17635,6.63413,6.02552,4.97312,4.55754,5.49424,2.62475]),
        H298 = (44.7512,'kcal/mol','+|-',9.29314),
        S298 = (2.82452,'cal/mol/K','+|-',10.2293),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 121,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C_N-1C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.36197,3.28682,1.05551,-0.676623,-3.104,-4.75474,-6.93875],'cal/mol/K','+|-',[6.03148,3.93976,1.84213,0.822074,5.70785,7.53253,2.79658]),
        H298 = (44.2418,'kcal/mol','+|-',11.7717),
        S298 = (2.25789,'cal/mol/K','+|-',12.9338),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 122,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_2C-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.846024,0.99021,-0.0183271,-0.19741,0.223288,-0.363784,-5.30854],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (37.3797,'kcal/mol','+|-',5.2),
        S298 = (-5.28162,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](O)C1OOC(OC(C)=O)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 123,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-2C-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.11093,3.77604,1.28426,-0.778703,-3.81277,-5.69009,-7.28602],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (45.7036,'kcal/mol','+|-',2.4),
        S298 = (3.86394,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](COO)C(OO)OC(C)=O from Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: ../data/dong_pio_liang.py
""",
)

entry(
    index = 124,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.23285,0.796516,-0.0796981,-0.455739,-0.893221,-1.717,-3.44755],'cal/mol/K','+|-',[4.2525,3.85892,3.69034,3.86155,4.09546,3.71209,4.05091]),
        H298 = (57.1097,'kcal/mol','+|-',12.5619),
        S298 = (-6.87137,'cal/mol/K','+|-',6.8208),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 125,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.994365,0.754003,0.0221049,-0.269953,-0.582776,-1.44691,-3.21418],'cal/mol/K','+|-',[4.3,4.21441,3.94657,3.91082,3.64342,2.97406,3.62624]),
        H298 = (56.885,'kcal/mol','+|-',5.97896),
        S298 = (-7.56939,'cal/mol/K','+|-',5.80783),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 126,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_2C-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.46452,1.60199,0.107411,-0.787036,-1.53856,-2.77113,-7.30975],'cal/mol/K','+|-',[1.3003,3.23148,2.96127,2.06891,0.3579,0.967309,2.77843]),
        H298 = (59.7793,'kcal/mol','+|-',12.9747),
        S298 = (-6.61378,'cal/mol/K','+|-',5.49127),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 127,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_2C-inRing_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.00479,0.459485,-0.939555,-1.51851,-1.66509,-2.42913,-6.32742],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (55.192,'kcal/mol','+|-',5.2),
        S298 = (-4.67232,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)C1CC(=O)OC1[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 128,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.9272,0.632863,0.00991839,-0.196083,-0.446236,-1.25773,-2.62909],'cal/mol/K','+|-',[4.58793,4.38004,4.15836,4.13887,3.82941,2.98338,1.66791]),
        H298 = (56.4715,'kcal/mol','+|-',4.73355),
        S298 = (-7.70591,'cal/mol/K','+|-',5.99654),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 129,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_Sp-4R!H=3C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.457656,0.304554,-0.192209,-0.0704965,-0.00810159,-0.770478,-1.89374],'cal/mol/K','+|-',[5.01957,6.25997,6.13162,5.51519,4.22923,2.80141,1.3156]),
        H298 = (59.4165,'kcal/mol','+|-',3.58511),
        S298 = (-7.21151,'cal/mol/K','+|-',7.67669),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 130,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.87884,2.01523,1.40754,1.27222,0.865126,-0.323409,-1.92576],'cal/mol/K','+|-',[1.38478,2.85312,3.71118,4.19113,4.17996,3.30136,1.85391]),
        H298 = (58.7433,'kcal/mol','+|-',3.85104),
        S298 = (-8.59044,'cal/mol/K','+|-',8.49871),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 131,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,D} {5,[S,D,T,B,Q]}
4   R!H ux {3,D}
5   R!H ux {3,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.36844,3.02396,2.71964,2.75401,2.34297,0.843797,-1.2703],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (60.1049,'kcal/mol','+|-',5.2),
        S298 = (-11.5952,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])C(=O)C=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 132,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.05526,0.722402,0.065044,-0.230334,-0.565728,-1.39062,-2.82965],'cal/mol/K','+|-',[4.68913,4.11559,3.85976,4.02017,3.89786,3.1046,1.56347]),
        H298 = (55.6683,'kcal/mol','+|-',3.64857),
        S298 = (-7.84075,'cal/mol/K','+|-',5.88102),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 133,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.14519,1.5738,0.719069,0.30363,-0.197244,-1.22691,-2.8345],'cal/mol/K','+|-',[2.79607,2.95496,3.37486,4.00561,4.2479,3.56058,1.82288]),
        H298 = (55.7968,'kcal/mol','+|-',3.90453),
        S298 = (-8.91127,'cal/mol/K','+|-',5.37309),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 134,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->O",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   O   ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.94832,1.49051,-0.0475653,-0.886714,-1.70641,-2.51781,-3.39011],'cal/mol/K','+|-',[2.66746,2.53669,3.21274,4.12714,3.74423,3.71808,1.50879]),
        H298 = (57.6938,'kcal/mol','+|-',3.65668),
        S298 = (-7.8293,'cal/mol/K','+|-',5.49003),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 135,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->O_3C-inRing",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   O   ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.58911,0.0515813,-1.89976,-3.23821,-3.73353,-4.50555,-4.20582],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (59.6635,'kcal/mol','+|-',5.2),
        S298 = (-4.96617,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]CC1(COO)COCC(=O)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 136,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->O_N-3C-inRing",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   O   ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.62792,2.20998,0.878531,0.289034,-0.692853,-1.52393,-2.98226],'cal/mol/K','+|-',[1.77371,0.668179,0.244372,0.943071,1.83936,1.98528,0.748763]),
        H298 = (56.7089,'kcal/mol','+|-',1.86099),
        S298 = (-9.26087,'cal/mol/K','+|-',3.331),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 137,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->O_N-3C-inRing_Ext-2C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   O   ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.00082,1.97374,0.964929,0.62246,-0.0425412,-0.822028,-2.71754],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (57.3669,'kcal/mol','+|-',5.2),
        S298 = (-8.08319,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(C=O)C(C)[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 138,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C   ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.66332,1.62378,1.17905,1.01784,0.708257,-0.452378,-2.50114],'cal/mol/K','+|-',[2.651,3.46841,3.45688,3.57221,3.69271,2.69727,1.78748]),
        H298 = (54.6586,'kcal/mol','+|-',1.64946),
        S298 = (-9.56045,'cal/mol/K','+|-',5.46199),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 139,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O_Ext-2C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C   ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.67957,1.87782,1.39333,1.41815,1.37652,0.079798,-2.29296],'cal/mol/K','+|-',[1.12273,0.554728,0.378474,1.23902,2.40536,1.93492,0.530901]),
        H298 = (55.491,'kcal/mol','+|-',0.877615),
        S298 = (-9.77127,'cal/mol/K','+|-',2.5869),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 140,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O_Ext-2C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C   ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
8   R!H ux {7,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.28262,1.6817,1.52714,1.85621,2.22695,0.763895,-2.10526],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (55.1807,'kcal/mol','+|-',5.2),
        S298 = (-10.6859,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC([O])C(C)COO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 141,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C   ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]} {6,D}
6   R!H ux {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.424547,-1.33579,-1.76074,-2.044,-2.20152,-2.36326,-3.17488],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (54.2958,'kcal/mol','+|-',5.2),
        S298 = (-5.44765,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(=O)C(C)C[O] from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 142,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C   ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H ux {5,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.691,2.84953,2.43467,2.14844,1.49488,-0.0291098,-2.37244],'cal/mol/K','+|-',[0.9812,0.489452,0.327845,0.707299,2.52364,2.65563,3.1943]),
        H298 = (54.0076,'kcal/mol','+|-',0.808),
        S298 = (-11.406,'cal/mol/K','+|-',4.16845),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 143,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   C   ux {3,[S,T,Q,B]} {7,[S,D,T,B,Q]}
5   R!H ux {3,[S,D,T,B,Q]} {6,[S,T,Q,B]}
6   R!H ux {5,[S,T,Q,B]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.03791,3.02257,2.55058,1.89837,0.602634,-0.968015,-3.50179],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (53.7219,'kcal/mol','+|-',5.2),
        S298 = (-9.93225,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC(C[O])COO from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 144,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-2C-R",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.893741,-0.610945,-0.856873,-0.882768,-0.923776,-1.41589,-2.60817],'cal/mol/K','+|-',[1.93986,1.45999,1.68467,1.25108,0.571305,0.661052,0.371221]),
        H298 = (56.289,'kcal/mol','+|-',1.48402),
        S298 = (-5.24205,'cal/mol/K','+|-',2.78093),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 145,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-2C-R_4R!H->O",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O   ux {3,[S,T,Q,B]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.207896,-0.0947591,-0.261252,-0.440445,-0.721789,-1.18218,-2.73942],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (55.7643,'kcal/mol','+|-',5.2),
        S298 = (-6.22526,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OCC([O])CC=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 146,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-2C-R_N-4R!H->O",
    group = 
"""
1 * O   u1 {2,[S,D,T,B,Q]}
2   C   ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C   ux {3,[S,T,Q,B]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57959,-1.12713,-1.45249,-1.32509,-1.12576,-1.64961,-2.47692],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (56.8137,'kcal/mol','+|-',5.2),
        S298 = (-4.25885,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)CC([O])OC(C)=O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 147,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_N-3R!H->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.50477,1.02325,-0.622648,-1.4466,-2.54893,-3.1575,-4.6922],'cal/mol/K','+|-',[3.54285,0.667575,1.91096,3.53548,5.64482,6.54935,6.16678]),
        H298 = (58.3083,'kcal/mol','+|-',33.7916),
        S298 = (-3.1486,'cal/mol/K','+|-',8.1843),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 148,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_N-3R!H->C_Ext-3O-R_4R!H->O",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C u0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]} {4,S}
4   O u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.44264,1.392,-1.48784,-3.00163,-5.00446,-6.02225,-7.50305],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.8042,'kcal/mol','+|-',5.2),
        S298 = (-0.139146,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1(O)OOC(=O)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 149,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_N-3R!H->C_Ext-3O-R_N-4R!H->O",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   C                      ux {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O                      ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.53584,0.838874,-0.190052,-0.669088,-1.32116,-1.72513,-3.28677],'cal/mol/K','+|-',[1.60364,0.274672,1.67696,3.23892,5.24881,6.04543,5.35286]),
        H298 = (48.5604,'kcal/mol','+|-',1.7927),
        S298 = (-4.65333,'cal/mol/K','+|-',8.92326),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 150,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_N-3R!H->C_Ext-3O-R_N-4R!H->O_2C-inRing",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   C                      ux r1 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O                      ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.10281,0.935985,-0.782946,-1.81422,-3.1769,-3.86251,-5.1793],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (47.9266,'kcal/mol','+|-',5.2),
        S298 = (-1.49849,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1(O)OC(=O)O1 from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 151,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_N-3R!H->C_Ext-3O-R_N-4R!H->O_N-2C-inRing",
    group = 
"""
1 * O                      u1 {2,[S,D,T,B,Q]}
2   C                      ux r0 {1,[S,D,T,B,Q]} {3,[S,T,Q,B]}
3   O                      ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   [Si,S,N,P,F,Br,I,Cl,C] ux {3,[S,D,T,B,Q]}
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
[O]C(O)(O)OC(=O)O from Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_1C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_1C-inRing_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_Int-7R!H-6R!H_Int-7R!H-2R!H_Int-7R!H-6R!H_Int-7R!H-5R!H_Int-7R!H-6R!H_Int-7R!H-4O_Int-7R!H-6R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_7R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_1C-inRing_Ext-4O-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_Int-7R!H-6R!H_Int-7R!H-2R!H_Int-7R!H-6R!H_Int-7R!H-5R!H_Int-7R!H-6R!H_Int-7R!H-4O_Int-7R!H-6R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-7R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Sp-7R!H-6R!H
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-1C-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Sp-7R!H-6R!H_6R!H->C
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-6R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_N-5R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_N-5R!H->C_Ext-1C-R_Ext-6R!H-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-2R!H-R_N-5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-5BrClFINOPSSi-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-1C-R_Ext-5R!H-R_6R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_4R!H->O_N-1C-inRing_Ext-1C-R_Ext-5R!H-R_N-6R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_3R!H->O_N-4R!H->O
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_N-3R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_N-3R!H->O_Ext-3C-R_Ext-3C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_1R->C_Ext-1C-R_N-3R!H->O_Ext-4R!H-R
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_2R!H-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_2R!H-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Int-7R!H-5R!H_Int-7R!H-6R!H_Ext-7R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R_5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R_N-5R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-3C-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-3C-R_Ext-4C-R
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-2R!H-R_N-5R!H->C_Ext-3C-R_Ext-4C-R_Ext-5BrClFINOPSSi-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=4C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=4C_Ext-4C-R_Ext-6R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=4C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_3R!H->C_N-2R!H-inRing_Ext-3C-R_N-4R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_N-3R!H->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_Sp-3R!H=2R!H_N-1R->C_N-3R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C_1C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C_1C-inRing_Ext-1C-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C_1C-inRing_Ext-1C-R_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C_N-1C-inRing
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_Sp-5R!H-1C_N-1C-inRing_Ext-1C-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_N-Sp-5R!H-1C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_N-Sp-5R!H-1C_Ext-3R!H-R_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_N-Sp-5R!H-1C_Ext-3R!H-R_Sp-6R!H-3R!H
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_Sp-4O-3R!H_Ext-1C-R_N-Sp-5R!H-1C_Ext-3R!H-R_N-Sp-6R!H-3R!H
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_N-Sp-4O-3R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_N-Sp-4O-3R!H_Ext-1C-R_Ext-1C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_1R->C_N-Sp-4O-3R!H_Ext-1C-R_Ext-1C-R_Ext-3R!H-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_8R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_8R!H->C_Sp-6R!H-5C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_8R!H->C_N-Sp-6R!H-5C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_N-8R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-7R!H-R_N-8R!H->C_Ext-4O-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_5R!H->C_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_N-5R!H->C
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_4R!H->O_N-1R->C_Ext-3R!H-R_N-5R!H->C_Ext-3R!H-R
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_1R->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_4BrCClFINPSSi-inRing_N-1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_Ext-7R!H-R_8R!H->C
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_Ext-7R!H-R_N-8R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-5R!H-R_Ext-7R!H-R_N-8R!H->C_Ext-4BrCClFINPSSi-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_Ext-4BrCClFINPSSi-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_7R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_7R!H->C_Ext-7C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-7O-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-6C-R_Ext-6C-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-6C-R_Ext-6C-R_Sp-8R!H=6C
                                                L13: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-6C-R_Ext-6C-R_Sp-8R!H=6C_Ext-3R!H-R
                                                    L14: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-6C-R_Ext-6C-R_Sp-8R!H=6C_Ext-3R!H-R_Ext-3R!H-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-4BrCClFINPSSi-R_N-7R!H->C_Ext-6C-R_Ext-6C-R_N-Sp-8R!H=6C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_6R!H->C_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C_Ext-3R!H-R_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_2R!H->O_Ext-3R!H-R_N-4R!H->O_N-4BrCClFINPSSi-inRing_Ext-4BrCClFINPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-6R!H->C_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_N-7R!H->C
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_3R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_3R!H->C_2C-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_3R!H->C_N-2C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_3R!H->C_N-2C-inRing_Ext-3C-R
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C_1C-inRing
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C_N-1C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C_N-1C-inRing_Ext-1C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_2C-inRing
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_1R->C_Ext-3R!H-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-2C-inRing
                L5: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_2C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_2C-inRing_Ext-3C-R_Ext-3C-R
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_Sp-4R!H=3C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->O
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->O_3C-inRing
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->O_N-3C-inRing
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->O_N-3C-inRing_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O_Ext-2C-R
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O_Ext-2C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O_Ext-5R!H-R_Sp-6R!H=5R!H
                                        L11: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                            L12: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->O_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R
                                L9: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-2C-R_4R!H->O
                                    L10: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_3R!H->C_N-2C-inRing_Ext-3C-R_N-Sp-4R!H=3C_Ext-2C-R_N-4R!H->O
                    L6: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_N-3R!H->C
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_N-3R!H->C_Ext-3O-R_4R!H->O
                        L7: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_N-3R!H->C_Ext-3O-R_N-4R!H->O
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_N-3R!H->C_Ext-3O-R_N-4R!H->O_2C-inRing
                            L8: RJ1_Ext-1R-R_Ext-2R!H-R_N-Sp-3R!H=2R!H_N-2R!H->O_N-1R->C_N-3R!H->C_Ext-3O-R_N-4R!H->O_N-2C-inRing
"""
)

