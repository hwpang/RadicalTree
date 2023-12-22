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
        Cpdata = ([-0.237815,-0.740997,-1.31892,-1.97639,-2.81471,-3.53941,-4.49086],'cal/mol/K','+|-',[4.24221,4.43184,4.56318,4.56589,4.09302,3.94562,3.19856]),
        H298 = (89.1528,'kcal/mol','+|-',13.5939),
        S298 = (0.120879,'cal/mol/K','+|-',8.6636),
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
1 * C u1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.237815,-0.740997,-1.31892,-1.97639,-2.81471,-3.53941,-4.49086],'cal/mol/K','+|-',[4.24221,4.43184,4.56318,4.56589,4.09302,3.94562,3.19856]),
        H298 = (89.1528,'kcal/mol','+|-',13.5939),
        S298 = (0.120879,'cal/mol/K','+|-',8.6636),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 2,
    label = "RJ1_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
2   R!H ux {1,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]}
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
    index = 3,
    label = "RJ1_Ext-1R-R_2R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S}
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
[CH2]C1=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
""",
)

entry(
    index = 4,
    label = "RJ1_Ext-1R-R_N-2R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S}
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

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_Ext-1R-R
        L3: RJ1_Ext-1R-R_2R!H-inRing
        L3: RJ1_Ext-1R-R_N-2R!H-inRing
"""
)

