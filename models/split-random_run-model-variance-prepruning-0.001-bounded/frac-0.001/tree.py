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
        Cpdata = ([0.59333,-0.100907,-0.940716,-1.55783,-2.47535,-3.13628,-4.7078],'cal/mol/K','+|-',[4.54169,5.84744,6.48356,5.88039,4.30563,3.16485,3.99076]),
        H298 = (95.6981,'kcal/mol','+|-',22.2906),
        S298 = (-0.96261,'cal/mol/K','+|-',3.44759),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
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
        Cpdata = ([0.59333,-0.100907,-0.940716,-1.55783,-2.47535,-3.13628,-4.7078],'cal/mol/K','+|-',[4.54169,5.84744,6.48356,5.88039,4.30563,3.16485,3.99076]),
        H298 = (95.6981,'kcal/mol','+|-',22.2906),
        S298 = (-0.96261,'cal/mol/K','+|-',3.44759),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 2,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_3R!H->O",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C u0 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4093,0.0010141,-1.40774,-2.20647,-3.2184,-3.83814,-5.574],'cal/mol/K','+|-',[5.95403,9.29922,10.1084,8.82261,5.71329,3.41629,4.59599]),
        H298 = (103.321,'kcal/mol','+|-',8.51395),
        S298 = (-0.514308,'cal/mol/K','+|-',4.84126),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_3R!H->O_1R->C",
    group = 
"""
1 * C u1 {2,S}
2   C u0 r1 {1,S} {3,S}
3   O ux r1 {2,S}
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
    index = 4,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_3R!H->O_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,D,T,B,Q]}
2   C u0 r1 {1,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
3   O ux {2,[S,D,T,B,Q]}
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
    index = 5,
    label = "RJ1_Ext-1R-R_Ext-2R!H-R_N-3R!H->O",
    group = 
"""
1 * R u1 {2,[S,D,T,B,Q]}
2   C ux r1 {1,[S,D,T,B,Q]} {3,S}
3   C u0 r1 {2,S}
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

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_3R!H->O
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_3R!H->O_1R->C
            L4: RJ1_Ext-1R-R_Ext-2R!H-R_3R!H->O_N-1R->C
        L3: RJ1_Ext-1R-R_Ext-2R!H-R_N-3R!H->O
"""
)

