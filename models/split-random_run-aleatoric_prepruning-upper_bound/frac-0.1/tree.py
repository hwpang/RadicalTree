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
        Cpdata = ([-0.492584,-1.48297,-2.19316,-2.62104,-3.10299,-3.52634,-4.37677],'cal/mol/K','+|-',[3.83744,4.3795,4.57919,4.42661,3.91911,3.69408,3.98551]),
        H298 = (94.2439,'kcal/mol','+|-',30.435),
        S298 = (0.0464621,'cal/mol/K','+|-',9.02682),
    ),
    shortDesc = """Radical correction fitted to 253 radicals""",
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
        Cpdata = ([-0.492584,-1.48297,-2.19316,-2.62104,-3.10299,-3.52634,-4.37677],'cal/mol/K','+|-',[3.83744,4.3795,4.57919,4.42661,3.91911,3.69408,3.98551]),
        H298 = (94.2439,'kcal/mol','+|-',30.435),
        S298 = (0.0464621,'cal/mol/K','+|-',9.02682),
    ),
    shortDesc = """Radical correction fitted to 253 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 2,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R",
    group = 
"""
1 * C   u1 {2,D}
2   R!H ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0321698,-0.691633,-1.38002,-1.94315,-2.8244,-3.46366,-4.446],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.26,'kcal/mol','+|-',16.7226),
        S298 = (1.71546,'cal/mol/K','+|-',6.69387),
    ),
    shortDesc = """Radical correction fitted to 31 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 3,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C",
    group = 
"""
1 * C u1 {2,D}
2   C ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0705984,-0.77836,-1.4239,-1.95296,-2.80059,-3.41069,-4.39694],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.939,'kcal/mol','+|-',15.8585),
        S298 = (1.93835,'cal/mol/K','+|-',6.84018),
    ),
    shortDesc = """Radical correction fitted to 26 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 4,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,D}
2   C u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.243623,-1.29184,-1.95048,-2.43334,-3.34835,-3.90033,-4.89984],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.373,'kcal/mol','+|-',5.2),
        S298 = (0.584521,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 5,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_1R-inRing_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,D}
2   C   u0 r1 {1,D} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,D,T,B,Q]}
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
CC1=[C]CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 6,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0581712,-0.74148,-1.38607,-1.91845,-2.76125,-3.37553,-4.36082],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.714,'kcal/mol','+|-',16.2926),
        S298 = (2.03558,'cal/mol/K','+|-',7.03524),
    ),
    shortDesc = """Radical correction fitted to 24 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 7,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux {1,D} {3,[S,D,T,B,Q]}
3   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0372948,-0.694172,-1.3365,-1.87098,-2.72319,-3.34475,-4.36466],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.971,'kcal/mol','+|-',17.1665),
        S298 = (1.79824,'cal/mol/K','+|-',7.081),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 8,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux {1,D} {3,S}
3   R!H ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.166173,-0.781783,-1.39273,-1.90553,-2.73961,-3.36935,-4.43671],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.123,'kcal/mol','+|-',5.2),
        S298 = (1.14613,'cal/mol/K','+|-',3.14301),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 9,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_2C-inRing",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   u0 r1 {1,D} {3,S}
3   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.877802,-0.138985,-1.05589,-1.69231,-2.76246,-3.58047,-4.56535],'cal/mol/K','+|-',[4.38594,3,3,3,3,3,3]),
        H298 = (107.117,'kcal/mol','+|-',5.97916),
        S298 = (0.0420148,'cal/mol/K','+|-',4.7705),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 10,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_2C-inRing_Ext-3R!H-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   u0 r1 {1,D} {3,S} {5,S}
3   R!H u0 {2,S} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.14388,0.0750095,-0.929814,-1.59416,-2.76116,-3.64439,-4.53418],'cal/mol/K','+|-',[5.75617,3,3,3,3,3,3]),
        H298 = (107.747,'kcal/mol','+|-',5.53333),
        S298 = (-0.845446,'cal/mol/K','+|-',3.33369),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 11,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_2C-inRing_Ext-3R!H-R_Ext-2C-R_3R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C u0 r1 {1,D} {3,S} {5,S}
3   O u0 r1 {2,S} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.96172,1.42654,-0.612549,-1.49759,-3.16381,-4.40072,-4.75842],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (110.972,'kcal/mol','+|-',5.2),
        S298 = (-2.47741,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C1OOC(C)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 12,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_2C-inRing_Ext-3R!H-R_Ext-2C-R_N-3R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C u0 r1 {1,D} {3,S} {5,S}
3   C u0 r1 {2,S} {4,D}
4   O ux {3,D}
5   C u0 r1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.108501,-0.525669,-1.07082,-1.63708,-2.5822,-3.30825,-4.43451],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (107.06,'kcal/mol','+|-',2.4),
        S298 = (-0.12013,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 13,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux r0 {1,D} {3,S}
3   R!H ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.309299,-0.869909,-1.43891,-1.93477,-2.73647,-3.34041,-4.41908],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.567,'kcal/mol','+|-',5.2),
        S298 = (1.2975,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 14,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R",
    group = 
"""
1 * C   u1 r0 {2,D} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,D} {3,S}
3   R!H u0 {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.542767,-1.44589,-2.15147,-2.62263,-3.28194,-3.7885,-4.73399],'cal/mol/K','+|-',[3.47011,3.24764,3.16536,3,3,3,3]),
        H298 = (110.796,'kcal/mol','+|-',6.39601),
        S298 = (1.80839,'cal/mol/K','+|-',4.96482),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 15,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,D} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,D} {3,S}
3   R!H u0 {2,S} {5,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.923682,-0.82344,-1.92104,-2.46064,-3.03821,-3.46046,-4.27735],'cal/mol/K','+|-',[8.08666,7.80515,7.0318,6.07027,3.99053,3,3]),
        H298 = (117.85,'kcal/mol','+|-',5.2),
        S298 = (0.530741,'cal/mol/K','+|-',12.1975),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 16,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_Ext-3R!H-R_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,D} {4,[S,D,T,B,Q]}
2   C   u0 r0 {1,D} {3,S} {6,[S,D,T,B,Q]}
3   R!H u0 r0 {2,S} {5,S}
4   R!H ux r0 {1,[S,D,T,B,Q]}
5   R!H u0 r0 {3,S}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.78275,1.9361,0.565081,-0.314472,-1.62734,-2.7263,-5.02067],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (116.245,'kcal/mol','+|-',5.2),
        S298 = (-3.78174,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)O[C]=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 17,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,D} {4,S}
2   C u0 r0 {1,D} {3,S}
3   C u0 {2,S}
4   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09234,-1.95389,-2.69139,-3.09875,-3.6367,-4.10165,-5.25635],'cal/mol/K','+|-',[3,3,3.29989,3.38944,3,3,3.38675]),
        H298 = (111.091,'kcal/mol','+|-',5.2),
        S298 = (2.91006,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 18,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,D} {4,S}
2   C   u0 r0 {1,D} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 r0 {2,S}
4   C   u0 {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.25928,-2.88618,-4.30681,-4.758,-5.0253,-5.33937,-6.91428],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (112.242,'kcal/mol','+|-',5.2),
        S298 = (3.93014,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 19,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,D} {4,S}
2   C u0 r0 {1,D} {3,S}
3   C u0 {2,S}
4   O u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.797606,-1.35564,-1.86394,-2.35077,-3.13404,-3.70812,-4.55969],'cal/mol/K','+|-',[2,2.17227,2,2,2,2,2]),
        H298 = (109.114,'kcal/mol','+|-',2.4),
        S298 = (1.58059,'cal/mol/K','+|-',2.0857),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 20,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_N-4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,D} {4,S}
2   C   u0 r0 {1,D} {3,S} {5,[S,D,T,B,Q]}
3   C   u0 r0 {2,S}
4   O   u0 r0 {1,S}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.170019,-0.587629,-1.16579,-1.76222,-2.72597,-3.42935,-4.43543],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (109.12,'kcal/mol','+|-',2.4),
        S298 = (0.843186,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 21,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_3R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux r0 {1,D} {3,S}
3   O ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.649085,-0.764227,-1.01339,-1.3624,-2.0465,-2.66181,-3.91502],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (113.55,'kcal/mol','+|-',2.4),
        S298 = (0.923303,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C(O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 22,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_N-3R!H->O",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux r0 {1,D} {3,S}
3   C ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0821134,-0.563028,-1.13846,-1.68814,-2.60433,-3.26189,-4.37119],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (111.406,'kcal/mol','+|-',5.2),
        S298 = (1.10065,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C(CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CC(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH]=CCC#C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 23,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_N-Sp-3R!H-2C",
    group = 
"""
1 * C u1 r0 {2,D}
2   C ux {1,D} {3,[B,D,T,Q]}
3   C ux {2,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.788698,-0.132665,-0.976094,-1.64953,-2.61795,-3.18711,-3.90288],'cal/mol/K','+|-',[3.13681,3.58992,3.63022,3.22057,3,3,3]),
        H298 = (87.6413,'kcal/mol','+|-',6.87634),
        S298 = (5.97766,'cal/mol/K','+|-',18.334),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 24,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_N-Sp-3R!H-2C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,D}
2   C   ux r0 {1,D} {3,[B,D,T,Q]}
3   C   ux r0 {2,[B,D,T,Q]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.24089,2.36693,1.37583,0.416276,-0.791888,-1.14369,-1.63919],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.0354,'kcal/mol','+|-',5.2),
        S298 = (21.2621,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH]=C=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 25,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_N-Sp-3R!H-2C_Ext-1R-R",
    group = 
"""
1 * C   u1 r0 {2,D} {4,[S,D,T,B,Q]}
2   C   ux {1,D} {3,[B,D,T,Q]}
3   C   ux {2,[B,D,T,Q]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.273541,-1.57844,-2.52024,-3.02762,-3.68553,-4.044,-4.31608],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (84.7515,'kcal/mol','+|-',2.4),
        S298 = (3.79953,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=[C]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 26,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-1R-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,D} {3,S}
2   C   u0 {1,D}
3   C   u0 r0 {1,S} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.33732,-1.4669,-2.16635,-2.70638,-3.46153,-3.89308,-4.24123],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.548,'kcal/mol','+|-',2.4),
        S298 = (6.59239,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=[C]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 27,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C",
    group = 
"""
1 * C u1 {2,D}
2   O ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.02902,0.149612,-0.954423,-1.84802,-3.05535,-3.97742,-4.92195],'cal/mol/K','+|-',[4.19176,3.63117,3,3,3,3,3]),
        H298 = (94.7008,'kcal/mol','+|-',12.2724),
        S298 = (-0.446515,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 28,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 {2,D} {3,[S,D,T,B,Q]}
2   O   ux {1,D}
3   R!H ux {1,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.479087,-0.336876,-1.30896,-2.16654,-3.33434,-4.06091,-4.85669],'cal/mol/K','+|-',[3.91957,3.35698,3,3,3,3,3]),
        H298 = (92.5889,'kcal/mol','+|-',9.04867),
        S298 = (0.0337344,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 29,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_4R!H->C_3R!H->C",
    group = 
"""
1 * C u1 {2,D} {3,[S,D,T,B,Q]}
2   O u0 {1,D}
3   C ux {1,[S,D,T,B,Q]} {4,S}
4   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.05093,0.180564,-0.844778,-1.74951,-2.99445,-3.7392,-4.43638],'cal/mol/K','+|-',[3.89827,3.23698,3,3,3,3,3]),
        H298 = (90.7256,'kcal/mol','+|-',6.28465),
        S298 = (-0.515667,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 30,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_4R!H->C_3R!H->C_3C-inRing",
    group = 
"""
1 * C u1 r0 {2,D} {3,[S,D,T,B,Q]}
2   O u0 r0 {1,D}
3   C ux r1 {1,[S,D,T,B,Q]} {4,S}
4   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.916307,-1.50944,-2.24943,-2.81889,-3.5363,-3.80388,-3.3789],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.2522,'kcal/mol','+|-',5.2),
        S298 = (-0.566728,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 31,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_4R!H->C_3R!H->C_N-3C-inRing",
    group = 
"""
1 * C u1 r0 {2,D} {3,[S,D,T,B,Q]}
2   O u0 r0 {1,D}
3   C ux r0 {1,[S,D,T,B,Q]} {4,S}
4   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.03455,1.02557,-0.142452,-1.21482,-2.72352,-3.70685,-4.96512],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.4623,'kcal/mol','+|-',5.2),
        S298 = (-0.490136,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
C#CCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 32,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_4R!H->C_N-3R!H->C",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   O ux {1,D}
3   O u0 {1,S} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23644,-1.8892,-2.70149,-3.41763,-4.35403,-5.02605,-6.11761],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.1787,'kcal/mol','+|-',5.2),
        S298 = (1.68194,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 33,
    label = "RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,D} {3,[S,D,T,B,Q]}
2   O                      u0 r0 {1,D}
3   R!H                    ux {1,[S,D,T,B,Q]} {4,S}
4   [F,I,Br,Cl,O,Si,P,S,N] u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.22876,2.09556,0.463713,-0.573932,-1.93937,-3.64348,-5.18301],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.148,'kcal/mol','+|-',5.2),
        S298 = (-2.36751,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=[C]C(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 34,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R",
    group = 
"""
1 * R   u1 {2,[S,T,Q,B]}
2   R!H ux {1,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.582207,-1.61812,-2.33204,-2.73682,-3.15057,-3.53704,-4.36495],'cal/mol/K','+|-',[3.97723,4.5864,4.82481,4.68892,4.18984,3.96395,4.27623]),
        H298 = (91.6939,'kcal/mol','+|-',29.9361),
        S298 = (-0.238587,'cal/mol/K','+|-',9.26334),
    ),
    shortDesc = """Radical correction fitted to 222 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 35,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.916978,-1.95309,-2.6319,-3.05582,-3.49258,-3.89506,-4.58133],'cal/mol/K','+|-',[4.17655,4.75979,4.90324,4.87851,4.64449,4.39247,4.41771]),
        H298 = (90.0096,'kcal/mol','+|-',17.3768),
        S298 = (-0.903824,'cal/mol/K','+|-',8.06051),
    ),
    shortDesc = """Radical correction fitted to 86 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 36,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R",
    group = 
"""
1 * R   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0045,-2.15196,-2.86116,-3.31179,-3.78328,-4.24591,-5.04398],'cal/mol/K','+|-',[4.24701,4.68845,4.77571,4.74249,4.50663,4.23538,4.0977]),
        H298 = (92.1702,'kcal/mol','+|-',14.1075),
        S298 = (-0.485465,'cal/mol/K','+|-',7.61234),
    ),
    shortDesc = """Radical correction fitted to 73 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 37,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.910595,0.485067,-0.34146,-0.981656,-1.96505,-2.85305,-4.54447],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.644,'kcal/mol','+|-',5.2),
        S298 = (-0.576733,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 38,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
4   C   ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.34686,0.803195,-0.273732,-1.06666,-2.21386,-3.20872,-4.98731],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.204,'kcal/mol','+|-',5.2),
        S298 = (-0.609715,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 39,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R_Ext-1R-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]} {4,S}
2   O   ux r1 {1,[S,T,Q,B]} {3,S}
3   R!H u0 r1 {1,[S,D,T,B,Q]} {2,S} {5,[S,D,T,B,Q]}
4   C   u0 r0 {1,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0394068,-0.0412143,-0.496081,-0.972669,-1.86745,-2.6634,-4.12517],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (101.287,'kcal/mol','+|-',2.4),
        S298 = (-1.10965,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C]1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 40,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   R!H ux {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
4   C   ux {1,[S,D,T,B,Q]} {5,S}
5   O   ux {4,S} {6,S}
6   O   u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.32098,1.68008,0.278501,-0.812528,-2.34676,-3.60214,-5.48339],'cal/mol/K','+|-',[3,3,3,3,3,3,3.22854]),
        H298 = (102.869,'kcal/mol','+|-',5.2),
        S298 = (-0.625047,'cal/mol/K','+|-',3.40024),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 41,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_Ext-5R!H-R_3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O ux r1 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r1 {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
4   C ux {1,[S,D,T,B,Q]} {5,S}
5   O ux {4,S} {6,S}
6   O u0 r0 {5,S}
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
OOC[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 42,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_Ext-5R!H-R_N-3R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
2   O ux r1 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   O ux r1 {1,[S,D,T,B,Q]} {2,[S,D,T,B,Q]}
4   C ux {1,[S,D,T,B,Q]} {5,S}
5   O ux {4,S} {6,S}
6   O u0 r0 {5,S}
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
    index = 43,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.20705,-2.43052,-3.12735,-3.56478,-3.99244,-4.41091,-5.12499],'cal/mol/K','+|-',[4.22956,4.58877,4.74313,4.74853,4.57691,4.33511,4.21698]),
        H298 = (91.1925,'kcal/mol','+|-',12.6462),
        S298 = (-0.374012,'cal/mol/K','+|-',7.88851),
    ),
    shortDesc = """Radical correction fitted to 66 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 44,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.278197,-0.957579,-1.68627,-2.25438,-3.05521,-3.66729,-4.7843],'cal/mol/K','+|-',[3.54263,4.53181,4.6375,4.4519,3.68517,3.02214,3.50103]),
        H298 = (95.3325,'kcal/mol','+|-',13.2814),
        S298 = (1.6663,'cal/mol/K','+|-',5.56158),
    ),
    shortDesc = """Radical correction fitted to 21 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 45,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.510629,-0.958651,-1.7552,-2.33692,-3.11825,-3.74315,-5.02882],'cal/mol/K','+|-',[3.99901,5.28588,5.40116,5.15442,4.19293,3.35597,3.86975]),
        H298 = (95.5372,'kcal/mol','+|-',14.5902),
        S298 = (1.8546,'cal/mol/K','+|-',5.58252),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 46,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.917897,-0.709305,-1.4978,-2.12576,-3.02018,-3.73688,-4.86759],'cal/mol/K','+|-',[4.07921,5.74363,5.59484,5.23489,4.27248,3.46082,3]),
        H298 = (94.1144,'kcal/mol','+|-',15.7336),
        S298 = (1.90994,'cal/mol/K','+|-',6.145),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 47,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_Sp-4C=3C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,D}
4   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904944,-1.87324,-2.27408,-2.40607,-2.64255,-2.68012,-2.52329],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (107.122,'kcal/mol','+|-',5.2),
        S298 = (-1.03696,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]OC(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 48,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.02357,-0.64183,-1.4528,-2.10951,-3.04207,-3.79814,-5.00349],'cal/mol/K','+|-',[4.1055,5.90345,5.76677,5.40716,4.41027,3.53295,3]),
        H298 = (93.702,'kcal/mol','+|-',15.2276),
        S298 = (2.08078,'cal/mol/K','+|-',6.1592),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 49,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.18738,-0.826086,-1.73501,-2.45411,-3.45445,-4.19106,-5.22333],'cal/mol/K','+|-',[4.54386,6.57445,6.32437,5.81545,4.41097,3.30178,3]),
        H298 = (92.825,'kcal/mol','+|-',16.4206),
        S298 = (2.49172,'cal/mol/K','+|-',6.0409),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 50,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.32467,-1.18336,-2.07249,-2.82172,-3.88075,-4.57855,-5.46448],'cal/mol/K','+|-',[5.15317,7.44466,7.20972,6.56976,4.75403,3.41794,3]),
        H298 = (96.5686,'kcal/mol','+|-',6.12907),
        S298 = (3.21201,'cal/mol/K','+|-',6.21098),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 51,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.475286,-3.75967,-4.50859,-5.01733,-5.45734,-5.53747,-5.13724],'cal/mol/K','+|-',[5.14642,6.59077,7.19207,6.89855,5.16904,3.94226,3]),
        H298 = (99.6405,'kcal/mol','+|-',5.2),
        S298 = (3.9792,'cal/mol/K','+|-',5.62489),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 52,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-1C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.38693,-6.07029,-7.06677,-7.47103,-7.28797,-6.9193,-5.56155],'cal/mol/K','+|-',[6.12799,3,3,3,3,3,3]),
        H298 = (101.74,'kcal/mol','+|-',5.2),
        S298 = (5.6028,'cal/mol/K','+|-',4.67479),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 53,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-1C-R_Ext-4C-R_5O-inRing",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S} {5,S} {7,D}
5   O   u0 r1 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.501915,-5.41698,-6.47299,-6.97769,-6.99439,-6.88308,-5.54173],'cal/mol/K','+|-',[7.50374,3,3,3,3,3,3]),
        H298 = (101.983,'kcal/mol','+|-',5.2),
        S298 = (5.32943,'cal/mol/K','+|-',6.47408),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 54,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-1C-R_Ext-4C-R_5O-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
2   O   ux r1 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S}
4   C   ux r1 {3,S} {5,S} {7,D}
5   O   u0 r1 {4,S}
6   R!H ux {1,[S,D,T,B,Q]}
7   R!H ux r0 {4,D}
8   R!H ux {1,[S,D,T,B,Q]}
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
    index = 55,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-1C-R_Ext-4C-R_N-5O-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux r0 {4,[S,D,T,B,Q]}
6   R!H ux r1 {1,[S,D,T,B,Q]}
7   R!H u0 {4,[S,D,T,B,Q]}
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
    index = 56,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-5O-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.63333,3.11589,1.52741,0.0644305,-2.42559,-4.40951,-7.68448],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (94.7108,'kcal/mol','+|-',2),
        S298 = (6.11948,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]OCC(C)OO - Radical thermo from johnson_g4.py and closed shell thermo from Thermo library: johnson_g4.py
""",
)

entry(
    index = 57,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
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
[CH]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 58,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.02016,1.41456,0.350859,-0.576242,-1.86421,-2.77865,-4.37554],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.9017,'kcal/mol','+|-',5.2),
        S298 = (0.602666,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 59,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_N-5R!H->O",
    group = 
"""
1 * C u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {3,S} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.733262,0.355681,-0.618751,-1.23817,-2.04435,-2.90938,-4.42569],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.5786,'kcal/mol','+|-',5.2),
        S298 = (0.109235,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 60,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_N-5R!H->O_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,[S,D,T,B,Q]}
2   O   u0 r1 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S}
4   C   u0 r1 {3,S} {5,D}
5   C   ux {4,D}
6   R!H ux {1,[S,D,T,B,Q]}
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
    index = 61,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.569048,0.48731,0.320059,0.153086,0.197359,-0.560039,-3.02186],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.2605,'kcal/mol','+|-',5.2),
        S298 = (-3.64185,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 62,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_N-4R!H->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.84076,-1.78603,-2.60929,-3.03761,-3.44366,-3.76397,-5.56379],'cal/mol/K','+|-',[3,3.76308,5.43627,5.79411,4.84239,3.7728,7.57544]),
        H298 = (99.9933,'kcal/mol','+|-',5.2),
        S298 = (1.67098,'cal/mol/K','+|-',4.15092),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 63,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_N-4R!H->C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]}
2   O   ux r1 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   O   ux r1 {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
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
O[C]1OC(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 64,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4BrClFINOPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]} {5,[S,D,T,B,Q]}
2   O   ux r1 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   O   ux r1 {3,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   C   ux r1 {1,[S,D,T,B,Q]} {6,S}
6   R!H u0 {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
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
    index = 65,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.23297,-0.992018,-1.64466,-2.22092,-3.0623,-3.60746,-4.16312],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.035,'kcal/mol','+|-',13.3175),
        S298 = (0.783327,'cal/mol/K','+|-',6.73936),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 66,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.436282,-2.06156,-2.96946,-3.65708,-4.597,-5.10316,-5.39429],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.391,'kcal/mol','+|-',2.4),
        S298 = (4.22986,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 67,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    group = 
"""
1 * C u1 {2,S} {4,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S}
4   C u0 {1,S} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.471391,-0.848956,-1.34886,-1.86246,-2.63358,-3.23553,-4.11132],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (94.4067,'kcal/mol','+|-',5.2),
        S298 = (0.200987,'cal/mol/K','+|-',3.78008),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 68,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-5R!H-R",
    group = 
"""
1 * C u1 {2,S} {4,S}
2   O u0 {1,S} {3,S}
3   C u0 {2,S}
4   C u0 {1,S} {5,S}
5   C u0 {4,S} {6,S}
6   O u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.168314,-0.483292,-0.951377,-1.39621,-2.12258,-2.79706,-4.29429],'cal/mol/K','+|-',[4.16849,3.4575,3,3,3,3,3]),
        H298 = (94.1619,'kcal/mol','+|-',5.2),
        S298 = (-0.604226,'cal/mol/K','+|-',5.214),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 69,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-5R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S}
4   C   u0 r0 {1,S} {5,S}
5   C   u0 r0 {4,S} {6,S}
6   O   u0 r0 {5,S} {7,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6421,-1.7057,-1.83389,-2.05916,-2.47919,-2.97017,-4.29328],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.1679,'kcal/mol','+|-',5.2),
        S298 = (1.2392,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CO[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 70,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S}
4   C u0 r0 {1,S} {5,[B,D,T,Q]}
5   C u0 r0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.23777,0.806442,0.0789907,-0.51296,-1.43127,-1.82283,-1.61316],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (75.4602,'kcal/mol','+|-',5.2),
        S298 = (-4.49643,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CO[CH]C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 71,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07237,-3.28866,-3.96694,-4.32823,-4.53848,-4.84414,-5.32347],'cal/mol/K','+|-',[3.61954,3.71203,3.98516,4.27532,4.73568,4.768,4.58367]),
        H298 = (88.1941,'kcal/mol','+|-',8.18559),
        S298 = (-1.56272,'cal/mol/K','+|-',8.12763),
    ),
    shortDesc = """Radical correction fitted to 45 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 72,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.62112,-3.77719,-3.68528,-3.40504,-2.95232,-2.92773,-3.0098],'cal/mol/K','+|-',[4.88953,5.3152,4.9845,4.9582,5.51401,5.59921,5.51616]),
        H298 = (88.2053,'kcal/mol','+|-',15.7608),
        S298 = (-2.31489,'cal/mol/K','+|-',9.49599),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 73,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.69987,-4.06663,-4.08455,-3.83563,-3.39215,-3.36732,-3.30953],'cal/mol/K','+|-',[5.30634,5.46652,4.74104,4.58407,5.25162,5.35863,5.67474]),
        H298 = (88.9686,'kcal/mol','+|-',15.4389),
        S298 = (-1.58129,'cal/mol/K','+|-',9.13092),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 74,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   O   ux {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59123,-2.94873,-3.11643,-2.89605,-2.50519,-2.66658,-2.845],'cal/mol/K','+|-',[4.51953,4.76538,4.13921,3.9866,5.2791,5.93285,6.76649]),
        H298 = (88.105,'kcal/mol','+|-',21.1522),
        S298 = (-3.18307,'cal/mol/K','+|-',8.98417),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 75,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,T,Q,B]}
2   O   ux r0 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   O   ux r0 {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.790431,0.704796,0.285743,0.0482161,-0.508576,-1.4306,-3.47376],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.6536,'kcal/mol','+|-',5.2),
        S298 = (-3.40966,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 76,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C_Ext-3C-R_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * O u1 r0 {2,S}
2   O u0 r0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S} {5,S}
4   O u0 r0 {3,S}
5   C u0 r0 {3,S} {6,[S,D,T,B,Q]}
6   O u0 r0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.62154,-5.01509,-4.16219,-2.24521,0.802262,1.82324,2.9607],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (105.664,'kcal/mol','+|-',5.2),
        S298 = (-9.29707,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OC(O)C(=O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 77,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C_Ext-3C-R_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   O ux {3,S}
5   C ux {3,[S,D,T,B,Q]} {6,S}
6   C ux {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.00703,-3.43709,-3.84148,-4.00223,-4.13721,-4.42837,-4.43791],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.3838,'kcal/mol','+|-',5.2),
        S298 = (-1.23213,'cal/mol/K','+|-',8.52342),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 78,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux {2,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   O   ux {3,S}
5   C   ux {3,[S,D,T,B,Q]} {6,S} {7,[S,D,T,B,Q]}
6   C   ux {5,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.60299,-2.07151,-2.8115,-2.92101,-2.87637,-3.63433,-4.0978],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.3051,'kcal/mol','+|-',5.2),
        S298 = (-5.40464,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 79,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_N-Sp-4O-3C",
    group = 
"""
1 * O u1 r0 {2,[S,T,Q,B]}
2   O ux r0 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,D}
4   O ux r0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.03055,-1.60636,-0.690716,-0.175555,0.346398,0.369193,-0.761825],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.7485,'kcal/mol','+|-',5.2),
        S298 = (-7.81684,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 80,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8037,-3.20392,-4.01579,-4.48838,-4.81363,-5.17658,-5.72482],'cal/mol/K','+|-',[3.15964,3.4598,3.8821,4.15734,4.46515,4.38091,3.98548]),
        H298 = (88.192,'kcal/mol','+|-',6.64554),
        S298 = (-1.43224,'cal/mol/K','+|-',8.02385),
    ),
    shortDesc = """Radical correction fitted to 39 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 81,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.52598,-4.36192,-5.36045,-5.73051,-5.5447,-5.65416,-6.95907],'cal/mol/K','+|-',[3,3,3,3,3,3,5.07908]),
        H298 = (88.8132,'kcal/mol','+|-',12.035),
        S298 = (-1.08903,'cal/mol/K','+|-',6.00165),
    ),
    shortDesc = """Radical correction fitted to 10 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 82,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.40471,-4.22926,-5.22436,-5.65197,-5.52961,-5.69544,-7.16244],'cal/mol/K','+|-',[3,3,3,3,3,3,5.15905]),
        H298 = (87.3774,'kcal/mol','+|-',5.2),
        S298 = (-1.29351,'cal/mol/K','+|-',6.16296),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 83,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   R!H ux {4,S}
6   C   ux {3,[S,D,T,B,Q]} {7,S}
7   R!H ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.43361,-4.22827,-5.22927,-5.69257,-5.55519,-5.69959,-7.37117],'cal/mol/K','+|-',[3,3,3,3,3,3,5.29012]),
        H298 = (87.4872,'kcal/mol','+|-',5.2),
        S298 = (-1.44558,'cal/mol/K','+|-',6.4653),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 84,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   O   ux {4,S}
6   C   ux {3,[S,D,T,B,Q]} {7,S}
7   R!H ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.47767,-4.26794,-5.18964,-5.56843,-5.34831,-5.38458,-7.44692],'cal/mol/K','+|-',[3,3,3,3,3,3,5.65081]),
        H298 = (86.938,'kcal/mol','+|-',5.2),
        S298 = (-1.81576,'cal/mol/K','+|-',6.48221),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 85,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O_7R!H->O",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   C u0 {3,S} {5,S}
5   O ux {4,S}
6   C ux {3,[S,D,T,B,Q]} {7,S}
7   O u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.45482,-4.15623,-5.30287,-5.87537,-5.58993,-5.72788,-9.98415],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.6779,'kcal/mol','+|-',5.2),
        S298 = (-4.30905,'cal/mol/K','+|-',4.84906),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 86,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O_7R!H->O_Int-7O-5O_Ext-3C-R_Ext-8R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 r1 {2,S} {4,S} {6,[S,D,T,B,Q]} {8,S}
4   C   u0 r1 {3,S} {5,S}
5   O   ux r1 {4,S}
6   C   ux r1 {3,[S,D,T,B,Q]} {7,S}
7   O   u0 r1 {6,S}
8   C   u0 {3,S} {9,[S,D,T,B,Q]}
9   R!H ux {8,[S,D,T,B,Q]}
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
Derived using the following species:
CC(C)(OO)C1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 87,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O_N-7R!H->O",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,S}
5   O ux {4,S}
6   C ux {3,[S,D,T,B,Q]} {7,S}
7   C ux {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.49916,-4.37308,-5.08308,-5.27955,-5.12091,-5.06146,-5.05894],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.0934,'kcal/mol','+|-',5.2),
        S298 = (0.530876,'cal/mol/K','+|-',3.21153),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 88,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O_N-7R!H->O_Ext-5O-R",
    group = 
"""
1 * O   u1 r0 {2,[S,T,Q,B]}
2   O   ux r0 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,S}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   O   u0 {4,S} {8,[S,D,T,B,Q]}
6   C   u0 r1 {3,S} {7,S}
7   C   ux r1 {6,S}
8   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.12375,-4.814,-5.11752,-5.04335,-4.87749,-4.71725,-4.49081],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (86.264,'kcal/mol','+|-',2.4),
        S298 = (1.26678,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1COOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 89,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O_N-7R!H->O_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,S}
5   O   ux {4,S}
6   C   ux r1 {3,[S,D,T,B,Q]} {7,S}
7   C   ux r1 {6,S}
8   R!H ux {3,[S,D,T,B,Q]}
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
    index = 90,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-5R!H->O",
    group = 
"""
1 * O u1 r0 {2,[S,T,Q,B]}
2   O ux r0 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]} {6,S}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C u0 r1 {4,S}
6   C u0 r1 {3,S} {7,S}
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
    index = 91,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r1 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   C u0 r1 {3,S} {5,S}
5   C ux r1 {4,S}
6   C ux r1 {3,[S,D,T,B,Q]} {7,[B,D,T,Q]}
7   C u0 r1 {6,[B,D,T,Q]}
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
    index = 92,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_N-Sp-5R!H-4BrCClFINPSSi",
    group = 
"""
1 * O u1 r0 {2,[S,T,Q,B]}
2   O ux r0 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r1 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[B,D,T,Q]}
5   C u0 r1 {4,[B,D,T,Q]}
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
    index = 93,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.58846,-2.85882,-3.61507,-4.11821,-4.59577,-5.03425,-5.357],'cal/mol/K','+|-',[3.33373,3.56228,3.99048,4.37344,4.92209,4.817,3.35664]),
        H298 = (88.0428,'kcal/mol','+|-',5.2),
        S298 = (-1.53452,'cal/mol/K','+|-',8.62283),
    ),
    shortDesc = """Radical correction fitted to 29 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 94,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,D}
4   C u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.38351,-1.76623,-1.89923,-2.45666,-2.90642,-3.22766,-4.01309],'cal/mol/K','+|-',[3,3.07379,3,3.56925,3.17092,3,3]),
        H298 = (86.167,'kcal/mol','+|-',5.2),
        S298 = (-4.44001,'cal/mol/K','+|-',3.26987),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 95,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,D} {5,S}
4   C u0 {3,D}
5   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.1967,-1.38106,-1.42857,-2.03067,-2.55334,-2.95049,-3.77795],'cal/mol/K','+|-',[3,3.4266,3,4.07095,3.71761,3,3]),
        H298 = (85.8711,'kcal/mol','+|-',5.2),
        S298 = (-4.54014,'cal/mol/K','+|-',4.42566),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 96,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,D} {5,S}
4   C   u0 {3,D}
5   C   u0 r0 {3,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.1032,-3.0585,-2.72228,-4.02355,-4.37324,-4.36405,-4.55006],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.8706,'kcal/mol','+|-',5.2),
        S298 = (-2.37362,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#CC(=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 97,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.61446,-2.99743,-3.83275,-4.329,-4.81008,-5.26345,-5.52749],'cal/mol/K','+|-',[3.51425,3.59018,3.94751,4.35586,4.99094,4.8811,3.38717]),
        H298 = (88.2924,'kcal/mol','+|-',5.2),
        S298 = (-1.16591,'cal/mol/K','+|-',8.84697),
    ),
    shortDesc = """Radical correction fitted to 26 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 98,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.56337,-3.02355,-3.9035,-4.41535,-4.89475,-5.36258,-5.62009],'cal/mol/K','+|-',[3.619,3.71439,4.052,4.46164,5.12813,4.99673,3.43263]),
        H298 = (88.5761,'kcal/mol','+|-',5.2),
        S298 = (-1.13841,'cal/mol/K','+|-',9.16461),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 99,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S} {5,D}
5   R!H ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54635,-2.68698,-3.33777,-3.62981,-3.89752,-4.32325,-4.77386],'cal/mol/K','+|-',[3.88366,4.12662,4.42264,4.46874,4.42903,3.93655,3]),
        H298 = (89.1584,'kcal/mol','+|-',5.22364),
        S298 = (-2.69587,'cal/mol/K','+|-',9.2977),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 100,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-3C-R",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux {3,S} {5,D}
5   R!H ux {4,D}
6   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.660467,-1.96999,-2.84556,-3.17198,-3.58299,-4.12584,-4.76122],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.3261,'kcal/mol','+|-',5.2),
        S298 = (-4.66803,'cal/mol/K','+|-',6.52442),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 101,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-3C-R_Ext-3C-R",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,S}
4   C ux {3,S} {5,D}
5   C ux {4,D}
6   C ux {3,[S,D,T,B,Q]}
7   C u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.37159,-2.59405,-3.32199,-3.59383,-3.93075,-4.40176,-5.12943],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.9947,'kcal/mol','+|-',5.2),
        S298 = (-3.5197,'cal/mol/K','+|-',9.73959),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 102,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-3C-R_Ext-3C-R_Ext-6R!H-R",
    group = 
"""
1 * O   u1 r0 {2,[S,T,Q,B]}
2   O   ux r0 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]} {7,S}
4   C   ux r0 {3,S} {5,D}
5   C   ux r0 {4,D}
6   C   ux {3,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   C   u0 r0 {3,S}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.630528,-1.972,-2.81149,-3.19531,-3.6052,-3.93815,-5.28011],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.6739,'kcal/mol','+|-',5.2),
        S298 = (-7.49381,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 103,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S} {5,D}
5   C   ux {4,D} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.52372,-2.65887,-2.58609,-2.67145,-2.64644,-3.08804,-4.27318],'cal/mol/K','+|-',[3,4.44158,5.29535,5.47513,5.37565,4.80044,3]),
        H298 = (89.7953,'kcal/mol','+|-',5.94583),
        S298 = (-3.50185,'cal/mol/K','+|-',8.38673),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 104,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,D} {7,[S,D,T,B,Q]}
5   C   u0 r0 {4,D} {6,S}
6   R!H u0 r0 {5,S}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.701454,-0.1889,0.151278,0.0270889,-0.179857,-0.98819,-3.22618],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.4179,'kcal/mol','+|-',5.2),
        S298 = (-7.89731,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 105,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->O",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 {3,S} {5,D}
5   C u0 {4,D} {6,S}
6   O u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59036,-2.45049,-2.16396,-2.0626,-1.77422,-2.14684,-3.65373],'cal/mol/K','+|-',[3,5.48072,6.97281,7.19174,6.75768,5.72483,3]),
        H298 = (91.0421,'kcal/mol','+|-',5.2),
        S298 = (-4.85429,'cal/mol/K','+|-',9.38442),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 106,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->O_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   O   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S}
4   C   u0 r0 {3,S} {5,D}
5   C   u0 r0 {4,D} {6,S} {7,[S,D,T,B,Q]}
6   O   u0 r0 {5,S}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72038,-0.512763,0.301304,0.480068,0.614983,-0.122805,-2.76762],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.4902,'kcal/mol','+|-',5.2),
        S298 = (-8.17218,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(O)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 107,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_N-6R!H->O",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S} {5,D}
5   C ux {4,D} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.36823,-4.10224,-4.3769,-4.62957,-4.75196,-5.07917,-5.41614],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.7371,'kcal/mol','+|-',5.2),
        S298 = (0.0483293,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 108,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S} {5,D}
5   C ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.02085,-0.490655,-2.16813,-3.3445,-4.4717,-5.49815,-4.40975],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.9227,'kcal/mol','+|-',5.2),
        S298 = (-0.318208,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 109,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S} {5,D}
5   O ux {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.20803,-6.35453,-7.3328,-7.565,-7.5758,-7.26981,-6.09463],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (91.2927,'kcal/mol','+|-',2.4),
        S298 = (5.26968,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]OCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 110,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S} {5,[S,T,Q,B]}
5   R!H ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.58241,-3.40005,-4.53635,-5.2941,-6.01029,-6.52522,-6.56672],'cal/mol/K','+|-',[3.50198,3.22616,3.35143,3.93639,5.13331,5.21266,3.75069]),
        H298 = (88.0585,'kcal/mol','+|-',5.2),
        S298 = (0.60384,'cal/mol/K','+|-',8.04665),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 111,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S} {5,[S,T,Q,B]}
5   O ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.03113,-2.97064,-4.29362,-5.19536,-6.13115,-6.82727,-6.79562],'cal/mol/K','+|-',[3.42229,3,3.36185,4.47776,6.21608,6.3896,4.75805]),
        H298 = (88.4308,'kcal/mol','+|-',5.2),
        S298 = (-0.0679625,'cal/mol/K','+|-',9.09348),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 112,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-3C-R",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   C u0 {3,S} {5,S}
5   O u0 {4,S}
6   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0508031,-2.55655,-4.5649,-6.0524,-7.56178,-8.40586,-8.01411],'cal/mol/K','+|-',[3,3.33024,4.74369,5.74935,7.39681,7.20313,4.83026]),
        H298 = (89.3598,'kcal/mol','+|-',6.35913),
        S298 = (0.981929,'cal/mol/K','+|-',11.3401),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 113,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-3C-R_Ext-5O-R",
    group = 
"""
1 * O   u1 {2,S}
2   O   u0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   C   u0 {3,S} {5,S}
5   O   u0 {4,S} {7,S}
6   C   ux {3,[S,D,T,B,Q]}
7   R!H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0387423,-2.99058,-5.18805,-6.78083,-8.41109,-9.26956,-8.62969],'cal/mol/K','+|-',[3,3.06912,4.34769,5.39808,7.32413,6.98106,4.51829]),
        H298 = (89.7195,'kcal/mol','+|-',6.69653),
        S298 = (2.15639,'cal/mol/K','+|-',11.7039),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 114,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-3C-R_Ext-5O-R_7R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   C u0 {3,S} {5,S}
5   O u0 {4,S} {7,S}
6   C ux {3,[S,D,T,B,Q]}
7   C u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.530766,-4.09756,-6.77113,-8.76443,-11.1052,-11.8372,-10.2917],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (90.8338,'kcal/mol','+|-',2),
        S298 = (6.43496,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(COCOO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from Thermo library: johnson_g4.py
""",
)

entry(
    index = 115,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-3C-R_Ext-5O-R_N-7R!H->C",
    group = 
"""
1 * O                      u1 {2,S}
2   O                      u0 {1,S} {3,S}
3   C                      u0 r0 {2,S} {4,S} {6,[S,D,T,B,Q]}
4   C                      u0 {3,S} {5,S}
5   O                      u0 {4,S} {7,S}
6   C                      ux {3,[S,D,T,B,Q]}
7   [F,I,Br,Cl,O,Si,P,S,N] u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.514785,-1.74524,-3.40707,-4.54927,-5.38027,-6.38094,-6.75991],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.9533,'kcal/mol','+|-',5.2),
        S298 = (-2.65699,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 116,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-5O-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C   ux {3,S} {5,[S,T,Q,B]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux {4,[S,T,Q,B]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.974874,-2.70185,-3.66396,-4.10312,-4.58359,-5.35932,-6.30553],'cal/mol/K','+|-',[3,3,3,3,3,3.10687,3]),
        H298 = (87.0027,'kcal/mol','+|-',5.2),
        S298 = (-4.14094,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 117,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-5O-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R_4BrCClFINPSSi-inRing",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C   ux r1 {3,S} {5,[S,T,Q,B]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux {4,[S,T,Q,B]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.375867,-2.7235,-4.02256,-4.5037,-5.41535,-6.45776,-7.24785],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (87.341,'kcal/mol','+|-',5.2),
        S298 = (-5.1452,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C1COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 118,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-5O-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R_N-4BrCClFINPSSi-inRing",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   O   ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C   ux r0 {3,S} {5,[S,T,Q,B]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5   O   ux {4,[S,T,Q,B]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57388,-2.6802,-3.30536,-3.70254,-3.75184,-4.26088,-5.36321],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.6644,'kcal/mol','+|-',5.2),
        S298 = (-3.13668,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 119,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S} {5,[S,T,Q,B]}
5   C ux {4,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.57997,-4.17709,-4.97556,-5.47279,-5.79159,-5.97864,-6.15252],'cal/mol/K','+|-',[3.13691,3.98638,3.75427,3.46514,3.28712,3,3]),
        H298 = (87.2624,'kcal/mol','+|-',5.30494),
        S298 = (1.81948,'cal/mol/K','+|-',6.37936),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 120,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   O ux {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C ux r0 {2,[S,D,T,B,Q]} {4,S}
4   C ux {3,S} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.70005,-4.50563,-5.4048,-5.9411,-6.26782,-6.39941,-6.06136],'cal/mol/K','+|-',[3.69108,4.36841,3.72465,3.10941,3,3,3]),
        H298 = (86.9612,'kcal/mol','+|-',5.8514),
        S298 = (1.78574,'cal/mol/K','+|-',7.63953),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 121,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi_Ext-3C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,T,Q,B]}
2   O   ux r0 {1,[S,T,Q,B]} {3,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   ux {3,S} {5,S}
5   C   ux {4,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21087,-2.73193,-3.88502,-4.66735,-5.12309,-5.59937,-6.05889],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.9091,'kcal/mol','+|-',5.2),
        S298 = (-1.3688,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 122,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_N-Sp-5C-4BrCClFINPSSi",
    group = 
"""
1 * O u1 {2,S}
2   O u0 {1,S} {3,S}
3   C u0 r0 {2,S} {4,S}
4   C u0 r0 {3,S} {5,T}
5   C u0 r0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.0696,-2.78082,-3.15127,-3.48245,-3.76758,-4.19035,-6.53996],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.2789,'kcal/mol','+|-',5.2),
        S298 = (1.96291,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 123,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_N-3R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   O u0 {1,S} {3,S}
3   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.167058,-1.01474,-1.77312,-1.99516,-2.22086,-2.83234,-3.54366],'cal/mol/K','+|-',[3.11001,3,3,3,3,3,4.22499]),
        H298 = (78.8217,'kcal/mol','+|-',5.2),
        S298 = (-5.15725,'cal/mol/K','+|-',5.99898),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 124,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_N-3R!H->C_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   O u0 {1,S} {3,S}
3   O u0 {2,S}
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
    index = 125,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_N-3R!H->C_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   O u0 {1,S} {3,S}
3   O u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26661,-1.86555,-2.09904,-1.89524,-1.90823,-2.22946,-2.0499],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.6627,'kcal/mol','+|-',5.2),
        S298 = (-7.27821,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C](C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 126,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O ux {1,[S,T,Q,B]}
3   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.63999,-1.20511,-1.76627,-2.05259,-2.2605,-2.32164,-2.37564],'cal/mol/K','+|-',[4.08327,5.07938,5.36057,5.24941,4.79379,4.0349,3.47089]),
        H298 = (79.8249,'kcal/mol','+|-',16.8193),
        S298 = (-3.20901,'cal/mol/K','+|-',9.31648),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 127,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O   ux {1,[S,T,Q,B]}
3   C   ux {1,[S,D,T,B,Q]} {4,S}
4   R!H ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.286763,-0.463882,-1.2512,-1.61403,-1.81325,-2.00618,-2.66713],'cal/mol/K','+|-',[4.98359,6.68214,7.13282,7.06348,6.50719,5.26958,3.10492]),
        H298 = (85.5709,'kcal/mol','+|-',19.5498),
        S298 = (-4.45065,'cal/mol/K','+|-',11.8238),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 128,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]} {5,S}
2   O ux {1,[S,T,Q,B]}
3   C ux {1,[S,D,T,B,Q]} {4,S}
4   C u0 {3,S}
5   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.767179,-2.48578,-3.78434,-4.28165,-4.24061,-3.84547,-2.6606],'cal/mol/K','+|-',[6.56913,4.30251,3,3.38317,3.33518,3,3]),
        H298 = (77.1326,'kcal/mol','+|-',6.44373),
        S298 = (-3.24747,'cal/mol/K','+|-',12.2381),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 129,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]} {5,S}
2   O   ux r0 {1,[S,T,Q,B]}
3   C   ux {1,[S,D,T,B,Q]} {4,S} {6,[S,D,T,B,Q]}
4   C   u0 r0 {3,S}
5   C   u0 r0 {1,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.44864,-0.379548,-2.32861,-2.62547,-2.60792,-2.56024,-1.59248],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.8889,'kcal/mol','+|-',5.2),
        S298 = (-9.23843,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 130,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O ux {1,[S,T,Q,B]}
3   C ux {1,[S,D,T,B,Q]} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.31004,1.2708,0.680014,0.23431,-0.376926,-1.1228,-3.05037],'cal/mol/K','+|-',[5.36261,8.17171,8.54176,8.15406,7.60638,6.31834,4.23853]),
        H298 = (92.8235,'kcal/mol','+|-',14.4152),
        S298 = (-5.16685,'cal/mol/K','+|-',16.6565),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 131,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O   ux {1,[S,T,Q,B]}
3   C   ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux {3,S}
5   R!H u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.9383,3.42289,2.9715,2.60935,2.16125,1.34327,-1.3735],'cal/mol/K','+|-',[5.86248,10.1414,10.464,9.31929,7.23853,3.38059,3]),
        H298 = (86.944,'kcal/mol','+|-',15.83),
        S298 = (-12.0431,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 132,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H->C_Ext-3R!H-R_5R!H->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O ux {1,[S,T,Q,B]}
3   C ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C ux {3,S}
5   C u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.865598,-0.16263,-0.728081,-0.685514,-0.397954,0.148046,-0.665762],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (81.3473,'kcal/mol','+|-',5.2),
        S298 = (-11.3748,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C([CH]O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 133,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H->C_Ext-3R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O                      ux {1,[S,T,Q,B]}
3   C                      ux {1,[S,D,T,B,Q]} {4,S} {5,[S,D,T,B,Q]}
4   C                      ux {3,S}
5   [F,I,Br,Cl,O,Si,P,S,N] u0 r0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.01099,7.00841,6.67108,5.90422,4.72046,2.53849,-2.08124],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (92.5408,'kcal/mol','+|-',5.2),
        S298 = (-12.7115,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 134,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O ux {1,[S,T,Q,B]}
3   C ux {1,[S,D,T,B,Q]} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.63685,-1.26511,-1.22613,-0.799707,-0.0287393,0.21713,-1.05955],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.0705,'kcal/mol','+|-',5.2),
        S298 = (-5.31718,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 135,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O   ux {1,[S,T,Q,B]}
3   C   ux {1,[S,D,T,B,Q]} {4,[B,D,T,Q]}
4   R!H ux {3,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.28304,-1.71944,-2.12367,-2.3569,-2.57083,-2.54053,-2.17339],'cal/mol/K','+|-',[3.05325,3.82885,4.18674,4.05169,3.60086,3.30692,3.92568]),
        H298 = (76.6812,'kcal/mol','+|-',12.3508),
        S298 = (-2.34747,'cal/mol/K','+|-',7.62346),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 136,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O   ux {1,[S,T,Q,B]}
3   C   ux {1,[S,D,T,B,Q]} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.75571,-2.28564,-2.6973,-2.85201,-2.87428,-2.6305,-1.81027],'cal/mol/K','+|-',[3,3.15284,3.6587,3.77882,3.75322,3.71543,4.01533]),
        H298 = (75.0328,'kcal/mol','+|-',11.2116),
        S298 = (-2.85028,'cal/mol/K','+|-',8.21955),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 137,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O   ux r0 {1,[S,T,Q,B]}
3   C   ux {1,[S,D,T,B,Q]} {4,D}
4   R!H u0 r0 {3,D} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.23908,-2.95289,-2.66412,-2.35152,-1.61387,-0.74646,0.779456],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (67.8653,'kcal/mol','+|-',2.4),
        S298 = (-6.58566,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=CC(O)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 138,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,S} {3,S} {5,S}
2   O   u0 {1,S}
3   C   u0 {1,S} {4,D}
4   R!H u0 {3,D}
5   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.84814,-3.21653,-3.99737,-4.05612,-3.75927,-3.13079,-1.39255],'cal/mol/K','+|-',[3,4.2519,5.26818,6.07988,6.45132,6.06,3.64828]),
        H298 = (73.3239,'kcal/mol','+|-',7.1396),
        S298 = (-2.82,'cal/mol/K','+|-',15.6567),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 139,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_Ext-1R-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S} {5,S}
2   O u0 r0 {1,S}
3   C u0 r0 {1,S} {4,D}
4   C u0 r0 {3,D}
5   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.638697,-1.13508,-1.41841,-1.0798,-0.601121,-0.164206,0.393419],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (69.162,'kcal/mol','+|-',5.2),
        S298 = (-10.4845,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 140,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_Ext-1R-R_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S} {3,S} {5,S}
2   O u0 r0 {1,S}
3   C u0 r0 {1,S} {4,D}
4   O u0 r0 {3,D}
5   C u0 r0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.38568,-4.14162,-5.14357,-5.37893,-5.16289,-4.44927,-2.18631],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (74.2104,'kcal/mol','+|-',2.4),
        S298 = (0.58645,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 141,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_4R!H->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O ux {1,[S,T,Q,B]}
3   C ux {1,[S,D,T,B,Q]} {4,D}
4   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.400133,-0.231895,-0.490607,-0.873295,-1.59987,-2.25111,-3.44613],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (79.393,'kcal/mol','+|-',2.4),
        S298 = (-1.56774,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 142,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_N-4R!H->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {3,[S,D,T,B,Q]}
2   O ux {1,[S,T,Q,B]}
3   C ux {1,[S,D,T,B,Q]} {4,D}
4   O ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.49442,-2.32751,-3.05931,-3.59197,-4.13077,-4.17129,-3.36752],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (79.9132,'kcal/mol','+|-',2.4),
        S298 = (-0.441168,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 143,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_N-Sp-4R!H=3R!H",
    group = 
"""
1 * C   u1 {2,S} {3,S}
2   O   u0 {1,S}
3   C   u0 r0 {1,S} {4,T}
4   R!H ux {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.81772,0.797011,0.425813,-0.15638,-1.22218,-2.14066,-3.78725],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (83.6256,'kcal/mol','+|-',2.4),
        S298 = (-0.112743,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C#C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 144,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.360655,-1.39644,-2.13359,-2.5257,-2.92422,-3.30011,-4.22175],'cal/mol/K','+|-',[3.7937,4.43375,4.75242,4.53172,3.81416,3.59536,4.17515]),
        H298 = (92.8798,'kcal/mol','+|-',36.1868),
        S298 = (0.20167,'cal/mol/K','+|-',9.91634),
    ),
    shortDesc = """Radical correction fitted to 136 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 145,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C",
    group = 
"""
1 * R   u1 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D}
3   R!H ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.403955,-1.26509,-1.87255,-2.16967,-2.49087,-2.82835,-3.70553],'cal/mol/K','+|-',[4.12066,5.07164,5.4295,5.09383,4.13829,3.83216,4.55089]),
        H298 = (84.5632,'kcal/mol','+|-',37.6859),
        S298 = (-0.577098,'cal/mol/K','+|-',9.5185),
    ),
    shortDesc = """Radical correction fitted to 77 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 146,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.498904,-1.45416,-2.05382,-2.30824,-2.55964,-2.853,-3.51646],'cal/mol/K','+|-',[4.40951,5.344,5.55422,5.04529,3.95665,3.73508,4.41805]),
        H298 = (80.2609,'kcal/mol','+|-',40.0115),
        S298 = (-0.448956,'cal/mol/K','+|-',10.3779),
    ),
    shortDesc = """Radical correction fitted to 60 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 147,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R",
    group = 
"""
1 * R   u1 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D}
3   C   ux {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.435539,-1.40894,-2.06431,-2.3664,-2.68726,-3.05029,-3.72644],'cal/mol/K','+|-',[4.68636,5.61399,5.70688,4.98977,3.5633,3.06983,3.61287]),
        H298 = (84.2568,'kcal/mol','+|-',15.6882),
        S298 = (-1.05243,'cal/mol/K','+|-',9.82419),
    ),
    shortDesc = """Radical correction fitted to 45 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 148,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing",
    group = 
"""
1 * R   u1 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.149885,-1.07998,-1.8344,-2.25668,-2.78623,-3.23735,-4.12809],'cal/mol/K','+|-',[3.2798,3,3,3,3,3,3]),
        H298 = (79.832,'kcal/mol','+|-',14.4963),
        S298 = (-1.05046,'cal/mol/K','+|-',8.39518),
    ),
    shortDesc = """Radical correction fitted to 22 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 149,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_4R!H->O",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.966582,-1.6264,-2.18975,-2.55828,-2.87238,-3.20265,-4.13264],'cal/mol/K','+|-',[3,3,3.31492,3.46649,3.61567,4.15663,4.26887]),
        H298 = (69.9948,'kcal/mol','+|-',11.6587),
        S298 = (-0.637556,'cal/mol/K','+|-',5.49848),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 150,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_4R!H->O_1R->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C u0 r1 {2,D} {4,S}
4   O ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0865654,-1.79606,-2.85621,-3.30211,-3.60443,-3.93242,-4.79627],'cal/mol/K','+|-',[3,3.83302,4.6615,4.76874,5.0733,6.05565,6.36482]),
        H298 = (75.9856,'kcal/mol','+|-',5.2),
        S298 = (1.05123,'cal/mol/K','+|-',5.92909),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 151,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_4R!H->O_1R->C_Ext-2C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]}
2   C   ux r1 {1,[S,T,Q,B]} {3,D} {5,[S,D,T,B,Q]}
3   C   u0 r1 {2,D} {4,S}
4   O   ux {3,S}
5   R!H ux {2,[S,D,T,B,Q]}
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
    index = 152,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_4R!H->O_N-1R->C",
    group = 
"""
1 * O u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   O u0 {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.74882,-1.47559,-1.59735,-1.89709,-2.22168,-2.55396,-3.54274],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (67.4425,'kcal/mol','+|-',2.4),
        S298 = (-2.1387,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 153,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0124211,-0.988013,-1.77458,-2.20591,-2.77173,-3.24319,-4.12732],'cal/mol/K','+|-',[3.38133,3,3,3,3,3,3]),
        H298 = (81.5894,'kcal/mol','+|-',12.219),
        S298 = (-1.11995,'cal/mol/K','+|-',8.92361),
    ),
    shortDesc = """Radical correction fitted to 19 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 154,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.384754,-0.783476,-1.63978,-1.99845,-2.5434,-3.02975,-3.47253],'cal/mol/K','+|-',[4.98067,4.28795,3.80331,3.12006,3,3,3]),
        H298 = (86.1131,'kcal/mol','+|-',7.24299),
        S298 = (-3.44277,'cal/mol/K','+|-',10.5584),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 155,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R",
    group = 
"""
1 * R   u1 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.128545,-1.35955,-2.35426,-2.57078,-2.81909,-3.09441,-3.35837],'cal/mol/K','+|-',[4.06708,4.03604,4.1285,3.6209,3,3,3]),
        H298 = (84.8746,'kcal/mol','+|-',8.67049),
        S298 = (-6.12997,'cal/mol/K','+|-',11.2418),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 156,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_6R!H->C",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux r1 {1,[S,T,Q,B]} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C ux r1 {3,S} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]} {6,S}
6   C u0 {5,S}
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
    index = 157,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_N-6R!H->C",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.532671,-0.87307,-1.79637,-2.17665,-2.82463,-3.24566,-3.57628],'cal/mol/K','+|-',[4.57079,4.33065,4.25405,3.99227,3.09281,3,3]),
        H298 = (86.8081,'kcal/mol','+|-',5.2),
        S298 = (-4.69226,'cal/mol/K','+|-',11.8304),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 158,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_N-6R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]} {6,S}
6   O u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.63216,0.376887,-0.66404,-1.16357,-2.23803,-2.98732,-3.37199],'cal/mol/K','+|-',[3.57365,3,3,3,3.29734,3.53304,3]),
        H298 = (85.6026,'kcal/mol','+|-',5.2),
        S298 = (-8.10042,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 159,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_N-6R!H->C_1R->C_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]}
2   C ux r1 {1,[S,T,Q,B]} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C ux r1 {3,S} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]} {6,S}
6   O u0 {5,S}
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
    index = 160,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_N-6R!H->C_1R->C_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]}
2   C ux r1 {1,[S,T,Q,B]} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C ux r1 {3,S} {5,[S,D,T,B,Q]}
5   O u0 {4,[S,D,T,B,Q]} {6,S}
6   O u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.368686,0.338583,0.159212,-0.211944,-1.07224,-1.7382,-2.97946],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.7868,'kcal/mol','+|-',5.2),
        S298 = (-7.72193,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 161,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_N-6R!H->C_N-1R->C",
    group = 
"""
1 * O u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C u0 r1 {3,[S,D,T,B,Q]} {5,S}
5   O ux {4,S} {6,[S,D,T,B,Q]}
6   O ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.66631,-3.37298,-4.06102,-4.20279,-3.99784,-3.76235,-3.98486],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.2191,'kcal/mol','+|-',5.2),
        S298 = (2.12404,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 162,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r0 {4,[S,D,T,B,Q]}
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
    index = 163,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux r0 {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08737,-1.34301,-1.48703,-1.74853,-2.36656,-2.85887,-3.78993],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (87.9254,'kcal/mol','+|-',2.4),
        S298 = (0.618758,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 164,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.172394,-1.0704,-1.82888,-2.28947,-2.86369,-3.32916,-4.39106],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.0106,'kcal/mol','+|-',12.2896),
        S298 = (-0.184373,'cal/mol/K','+|-',7.868),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 165,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0430085,-0.911347,-1.66852,-2.15632,-2.79194,-3.33085,-4.32449],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (80.3686,'kcal/mol','+|-',11.9041),
        S298 = (-0.720716,'cal/mol/K','+|-',6.56765),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 166,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0289939,-0.926331,-1.7118,-2.21813,-2.8988,-3.46583,-4.56995],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.9153,'kcal/mol','+|-',10.401),
        S298 = (0.203451,'cal/mol/K','+|-',6.65756),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 167,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Ext-4C-R",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C ux {3,S} {5,S} {7,S}
5   C u0 {4,S}
6   C ux {1,[S,D,T,B,Q]}
7   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.385693,-0.41383,-1.17228,-1.59862,-2.36496,-3.09812,-4.43674],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (74.9468,'kcal/mol','+|-',14.8944),
        S298 = (2.56147,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 168,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Ext-4C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,T,Q,B]} {3,D}
3   C   u0 r1 {2,D} {4,S}
4   C   ux r1 {3,S} {5,S} {7,S}
5   C   u0 r1 {4,S}
6   C   ux r1 {1,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   C   u0 r1 {4,S}
8   R!H ux {6,[S,D,T,B,Q]}
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
    index = 169,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Sp-5BrCClFINPSSi-4C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,S}
5   C ux {4,S}
6   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.146124,-1.0052,-1.89646,-2.4426,-3.07042,-3.58387,-4.63683],'cal/mol/K','+|-',[3.66409,3,3,3,3,3,3]),
        H298 = (79.6649,'kcal/mol','+|-',10.8237),
        S298 = (-0.806865,'cal/mol/K','+|-',7.82665),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 170,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Sp-5BrCClFINPSSi-4C_Ext-3C-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,D}
3   C   u0 r1 {2,D} {4,S} {7,[S,D,T,B,Q]}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S}
6   C   u0 r1 {1,S}
7   R!H ux {3,[S,D,T,B,Q]}
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
    index = 171,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Sp-5BrCClFINPSSi-4C_Ext-2C-R",
    group = 
"""
1 * C u1 {2,S} {6,S}
2   C u0 {1,S} {3,D} {7,S}
3   C u0 r1 {2,D} {4,S}
4   C u0 {3,S} {5,S}
5   C u0 {4,S}
6   C u0 {1,S}
7   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.768405,-1.61839,-2.28772,-2.64979,-3.16687,-3.71772,-4.73862],'cal/mol/K','+|-',[3,3,3.01915,3.05018,3,3,3]),
        H298 = (76.6566,'kcal/mol','+|-',11.6293),
        S298 = (-0.0458988,'cal/mol/K','+|-',4.16595),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 172,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Sp-5BrCClFINPSSi-4C_Ext-2C-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r1 {2,S} {6,S}
2   C   u0 r1 {1,S} {3,D} {7,S}
3   C   u0 r1 {2,D} {4,S}
4   C   u0 r1 {3,S} {5,S}
5   C   u0 r1 {4,S}
6   C   u0 r1 {1,S} {8,[S,D,T,B,Q]}
7   C   u0 r0 {2,S}
8   R!H ux {6,[S,D,T,B,Q]}
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
    index = 173,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Sp-5BrCClFINPSSi-4C_Ext-5BrCClFINPSSi-R",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,T,Q,B]} {3,D}
3   C   ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C   ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C   ux r1 {4,S} {7,[S,D,T,B,Q]}
6   C   ux r1 {1,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 174,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_N-Sp-5BrCClFINPSSi-4C",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]} {6,[S,D,T,B,Q]}
2   C ux r1 {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,D}
5   C ux r1 {4,D}
6   C ux r1 {1,[S,D,T,B,Q]}
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
CC=CCC1=CC=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 175,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_6R!H->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.167863,-0.394352,-0.951207,-1.5015,-2.18563,-2.60667,-3.71061],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.4755,'kcal/mol','+|-',5.2),
        S298 = (-1.84404,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 176,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_6R!H->C_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]}
2   C ux r1 {1,[S,T,Q,B]} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C ux r1 {3,[S,D,T,B,Q]} {5,S}
5   C ux r1 {4,S} {6,[S,D,T,B,Q]}
6   C ux r1 {5,[S,D,T,B,Q]}
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
    index = 177,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_6R!H->C_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C u0 {3,S} {5,[S,D,T,B,Q]}
5   C u0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   C u0 {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.655144,-0.462629,-0.696951,-1.17148,-1.91992,-2.4902,-3.57502],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.8571,'kcal/mol','+|-',5.2),
        S298 = (-2.12609,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 178,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_6R!H->C_N-1C-inRing_Sp-6C-5BrCClFINPSSi",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   C u0 r1 {4,[S,D,T,B,Q]} {6,S}
6   C u0 r1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.756805,-1.16826,-1.7007,-2.15999,-2.63686,-2.93076,-3.82953],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.0342,'kcal/mol','+|-',5.2),
        S298 = (-2.83008,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 179,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_6R!H->C_N-1C-inRing_N-Sp-6C-5BrCClFINPSSi",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C u0 r1 {2,D} {4,S}
4   C u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   C u0 r1 {4,[S,D,T,B,Q]} {6,D}
6   C u0 r1 {5,D}
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
[CH2]C1=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 180,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_N-6R!H->C",
    group = 
"""
1 * C                      u1 {2,S}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 r1 {2,D} {4,S}
4   C                      u0 r1 {3,S} {5,[S,D,T,B,Q]}
5   C                      u0 r1 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   [F,I,Br,Cl,O,Si,P,S,N] u0 {5,[S,D,T,B,Q]}
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
    index = 181,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_N-1R->C",
    group = 
"""
1 * O u1 {2,S}
2   C u0 r1 {1,S} {3,D}
3   C ux r1 {2,D} {4,[S,D,T,B,Q]}
4   C u0 r1 {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux r1 {4,[S,D,T,B,Q]}
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
    index = 182,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing",
    group = 
"""
1 * R   u1 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D}
3   C   ux r0 {2,D} {4,[S,D,T,B,Q]}
4   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.700949,-1.71459,-2.27792,-2.46835,-2.59531,-2.87648,-3.35325],'cal/mol/K','+|-',[5.73534,7.40459,7.53628,6.56959,4.6325,3.8855,4.6382]),
        H298 = (88.2565,'kcal/mol','+|-',12.3239),
        S298 = (-1.05427,'cal/mol/K','+|-',11.2142),
    ),
    shortDesc = """Radical correction fitted to 23 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 183,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.20547,-4.18039,-4.83754,-4.60236,-3.66239,-3.248,-3.07521],'cal/mol/K','+|-',[7.5059,9.95461,9.47372,7.36793,3.39801,3,4.77992]),
        H298 = (96.2849,'kcal/mol','+|-',10.0541),
        S298 = (-0.23397,'cal/mol/K','+|-',5.22255),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 184,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_Ext-1R-R",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {5,S}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C u0 r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00076,-2.13939,-2.71046,-2.91802,-3.12578,-3.42416,-4.16388],'cal/mol/K','+|-',[4.86034,8.44136,8.33918,6.55803,3,3,3]),
        H298 = (100.027,'kcal/mol','+|-',5.2),
        S298 = (0.44325,'cal/mol/K','+|-',3.45181),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 185,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_Ext-1R-R_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]} {5,S}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C u0 r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C u0 {1,S}
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
O=C=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 186,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_Ext-1R-R_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]} {5,S}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C u0 r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.38006,-6.27173,-6.79279,-6.12841,-4.57571,-3.8328,-3.61345],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.22,'kcal/mol','+|-',5.2),
        S298 = (2.13303,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 187,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_1R->C",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]}
2   C ux r0 {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.25372,0.34898,-0.608554,-1.49527,-2.49473,-3.68746,-5.47434],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.2801,'kcal/mol','+|-',5.2),
        S298 = (-0.955458,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=C=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 188,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.91389,-8.10339,-8.68027,-7.52443,-4.68222,-2.88515,-0.991098],'cal/mol/K','+|-',[7.79391,8.64484,7.70664,6.31581,3.9454,3.2105,4.01423]),
        H298 = (93.4602,'kcal/mol','+|-',9.53812),
        S298 = (-0.423467,'cal/mol/K','+|-',7.94349),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 189,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_N-1R->C_Ext-2C-R",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D} {5,S}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.85483,-8.58811,-8.79356,-7.37744,-4.18715,-2.25893,-0.466858],'cal/mol/K','+|-',[8.35877,10.318,9.42234,7.70167,4.17937,3,4.19228]),
        H298 = (94.135,'kcal/mol','+|-',11.2043),
        S298 = (-0.233597,'cal/mol/K','+|-',9.68418),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 190,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_N-1R->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D} {5,S}
3   C   ux r0 {2,D} {4,[S,D,T,B,Q]}
4   O   ux {3,[S,D,T,B,Q]}
5   C   u0 {2,S} {6,[S,D,T,B,Q]} {7,S}
6   R!H ux {5,[S,D,T,B,Q]}
7   O   u0 {5,S}
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
    index = 191,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_N-1R->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,T,Q,B]}
2   C ux r0 {1,[S,T,Q,B]} {3,D} {5,S}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C u0 r0 {2,S} {6,[S,D,T,B,Q]} {7,S}
6   C ux {5,[S,D,T,B,Q]}
7   O u0 r0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.2223,-14.0215,-13.6058,-11.0008,-5.31573,-1.25438,1.94227],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.232,'kcal/mol','+|-',5.2),
        S298 = (2.93024,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[O]C(=CO)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 192,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_N-1R->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,T,Q,B]}
2   C ux r0 {1,[S,T,Q,B]} {3,D} {5,S}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   O ux {3,[S,D,T,B,Q]}
5   C u0 r0 {2,S} {6,S} {7,S}
6   O ux {5,S}
7   O u0 r0 {5,S}
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
    index = 193,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0824242,-0.700876,-1.22564,-1.59104,-2.15662,-2.72375,-3.46755],'cal/mol/K','+|-',[4.52703,5.13486,5.62275,5.51566,4.88613,4.44666,4.72164]),
        H298 = (85.7304,'kcal/mol','+|-',7.73596),
        S298 = (-1.3915,'cal/mol/K','+|-',13.0563),
    ),
    shortDesc = """Radical correction fitted to 15 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 194,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-1R-R",
    group = 
"""
1 * R   u1 r0 {2,S} {5,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D}
3   C   ux r0 {2,D} {4,[S,D,T,B,Q]}
4   C   u0 {3,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.0446,0.631262,-0.93584,-2.06119,-3.17114,-4.11574,-1.4297],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (78.9886,'kcal/mol','+|-',5.2),
        S298 = (2.72696,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[CH]C=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 195,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.45589,-1.43166,-1.18048,-0.908178,-0.660067,-0.942152,-1.84426],'cal/mol/K','+|-',[5.27272,7.87172,8.8708,9.06029,8.30255,7.12987,7.31906]),
        H298 = (85.8826,'kcal/mol','+|-',5.2),
        S298 = (-6.49454,'cal/mol/K','+|-',24.609),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 196,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D}
3   C   ux r0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {6,S}
5   C   ux {3,[S,D,T,B,Q]}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.295539,0.545865,1.61922,2.44118,3.10118,2.65912,1.40253],'cal/mol/K','+|-',[4.65456,8.33199,9.65745,9.25483,5.46591,3,7.72265]),
        H298 = (86.3377,'kcal/mol','+|-',5.2),
        S298 = (-19.137,'cal/mol/K','+|-',10.6415),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 197,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-4C-R_Ext-2C-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D} {7,[S,D,T,B,Q]}
3   C   ux r0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {6,S}
5   C   ux {3,[S,D,T,B,Q]}
6   R!H u0 r0 {4,S}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3501,3.49167,5.03364,5.71326,5.03367,2.60445,-1.32783],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.6475,'kcal/mol','+|-',5.2),
        S298 = (-15.3746,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(COO)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 198,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_1R->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.688455,-0.707659,-1.07558,-1.37579,-1.75748,-2.30716,-3.51678],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (85.5917,'kcal/mol','+|-',2.4),
        S298 = (-0.268609,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 199,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]}
5   C ux {3,[S,D,T,B,Q]}
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
    index = 200,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-2C-R",
    group = 
"""
1 * C u1 {2,S}
2   C u0 {1,S} {3,D} {5,S}
3   C u0 r0 {2,D} {4,S}
4   C u0 {3,S}
5   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.448153,-0.709739,-0.931522,-1.20569,-1.91941,-2.57141,-3.09453],'cal/mol/K','+|-',[3,4.10503,4.13654,3.38758,3,3,3]),
        H298 = (89.7282,'kcal/mol','+|-',5.2),
        S298 = (-0.890569,'cal/mol/K','+|-',3.11598),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 201,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-2C-R_Ext-4C-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {5,S}
3   C   u0 r0 {2,D} {4,S}
4   C   u0 r0 {3,S} {6,[S,D,T,B,Q]}
5   C   u0 r0 {2,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.85588,-2.7193,-2.95651,-2.86403,-2.31723,-2.32741,-1.94603],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (88.6536,'kcal/mol','+|-',5.2),
        S298 = (0.634814,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)=CCC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 202,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,[S,D,T,B,Q]}
4   C ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.41646,-0.0112426,-0.635452,-1.23333,-2.28027,-3.0331,-3.93354],'cal/mol/K','+|-',[4.22284,3,3,3,3,3,3]),
        H298 = (84.2732,'kcal/mol','+|-',6.88247),
        S298 = (-0.259296,'cal/mol/K','+|-',5.67094),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 203,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.515893,0.123899,-0.504027,-1.11449,-2.21297,-2.98763,-3.90318],'cal/mol/K','+|-',[4.44702,3,3,3,3,3.04606,3]),
        H298 = (84.0101,'kcal/mol','+|-',6.59881),
        S298 = (-0.182914,'cal/mol/K','+|-',6.02786),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 204,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_1R->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.378318,-0.306469,-0.559646,-0.857546,-1.57804,-2.27654,-3.37894],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.3521,'kcal/mol','+|-',7.72875),
        S298 = (-1.40048,'cal/mol/K','+|-',3.80323),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 205,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_1R->C_4C-inRing",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux r1 {3,S} {5,S}
5   C ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.229923,-0.0541546,-0.474612,-0.892495,-1.34584,-1.76474,-2.97114],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (80.2708,'kcal/mol','+|-',2.4),
        S298 = (-3.11307,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CC1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 206,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_1R->C_N-4C-inRing",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux r0 {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.439025,-0.409689,-0.594433,-0.843249,-1.67303,-2.48592,-3.54576],'cal/mol/K','+|-',[3.60887,3,3,3,3,3,3]),
        H298 = (86.1963,'kcal/mol','+|-',5.47091),
        S298 = (-0.699873,'cal/mol/K','+|-',3.58508),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 207,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_1R->C_N-4C-inRing_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux r0 {3,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,S}
6   C u0 {5,S} {7,[S,D,T,B,Q]} {8,S}
7   C ux {6,[S,D,T,B,Q]}
8   C u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.751414,0.547015,-0.0143481,-0.555041,-1.65762,-2.4367,-4.01872],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (85.935,'kcal/mol','+|-',10.3798),
        S298 = (0.48461,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 208,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_1R->C_N-4C-inRing_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Int-10R!H-8R!H_Int-10R!H-9R!H_Int-10R!H-9R!H_Ext-9R!H-R",
    group = 
"""
1  * C   u1 {2,[S,T,Q,B]}
2    C   ux {1,[S,T,Q,B]} {3,D}
3    C   ux r0 {2,D} {4,S}
4    C   ux r0 {3,S} {5,[S,D,T,B,Q]}
5    C   ux r1 {4,[S,D,T,B,Q]} {6,S}
6    C   u0 r1 {5,S} {7,[S,D,T,B,Q]} {8,S}
7    C   ux r1 {6,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8    C   u0 r1 {6,S}
9    C   ux r1 {7,[S,D,T,B,Q]} {10,[S,D,T,B,Q]} {11,[S,D,T,B,Q]}
10   R!H ux {9,[S,D,T,B,Q]}
11   R!H ux {9,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.541775,0.927198,0.375144,-0.0884557,-1.47915,-2.41455,-3.18111],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (79.8842,'kcal/mol','+|-',5.2),
        S298 = (0.347677,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=CCC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 209,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_N-1R->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D} {4,S}
4   C u0 {3,S} {5,S}
5   C u0 {4,S}
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
[O]C=CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 210,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_N-Sp-4C-3C",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,D}
4   C ux {3,D} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.577874,-1.36266,-1.9497,-2.42175,-2.95328,-3.48787,-4.23722],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (89.4762,'kcal/mol','+|-',5.2),
        S298 = (-1.02311,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C=C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 211,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->C",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux {3,S} {5,S}
5   O ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.190154,-3.22721,-5.213,-5.74204,-5.28317,-5.25054,-6.7908],'cal/mol/K','+|-',[7.67734,11.7917,13.2791,11.6263,7.01948,4.14143,5.72739]),
        H298 = (92.2719,'kcal/mol','+|-',11.8019),
        S298 = (2.90364,'cal/mol/K','+|-',12.7948),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 212,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux {3,S} {5,S}
5   O ux {4,S}
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

entry(
    index = 213,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->C_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux r0 {2,D} {4,S}
4   C ux {3,S} {5,S}
5   O ux {4,S}
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
    index = 214,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,S}
2   C u0 {1,S} {3,D}
3   C u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.109873,-0.0405199,-0.103881,-0.228431,-0.0910179,0.0110311,1.21836],'cal/mol/K','+|-',[3,4.50749,7.7116,9.94482,12.3156,14.7328,14.6823]),
        H298 = (6.05318,'kcal/mol','+|-',139.691),
        S298 = (0.465016,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 215,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_1R-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C u0 r1 {1,S} {3,D}
3   C u0 {2,D}
4   C ux r1 {1,[S,D,T,B,Q]} {5,S}
5   C u0 r1 {4,S}
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
C=C1[CH]CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 216,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_1R-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,S} {4,[S,D,T,B,Q]}
2   C                      u0 r1 {1,S} {3,D}
3   C                      u0 {2,D}
4   C                      ux r1 {1,[S,D,T,B,Q]} {5,S}
5   [F,I,Br,Cl,O,Si,P,S,N] u0 r1 {4,S}
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
    index = 217,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing",
    group = 
"""
1 * R u1 r0 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.806096,-1.89378,-2.39384,-2.49911,-2.57194,-2.68727,-3.66734],'cal/mol/K','+|-',[3.86664,4.63375,4.96048,4.76461,3.58959,3,3.37865]),
        H298 = (82.372,'kcal/mol','+|-',15.6543),
        S298 = (1.58044,'cal/mol/K','+|-',12.6461),
    ),
    shortDesc = """Radical correction fitted to 13 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 218,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R",
    group = 
"""
1 * R   u1 r0 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D} {4,[S,D,T,B,Q]}
3   C   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.56894,-3.25275,-3.75739,-3.61354,-3.16138,-2.80364,-3.65849],'cal/mol/K','+|-',[4.98855,5.3598,5.84524,5.97761,4.79802,4.09854,4.87324]),
        H298 = (80.4472,'kcal/mol','+|-',26.1125),
        S298 = (2.46134,'cal/mol/K','+|-',17.5972),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 219,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C",
    group = 
"""
1 * R u1 r0 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.735559,-2.98784,-3.99651,-4.17072,-3.87208,-3.61848,-4.63776],'cal/mol/K','+|-',[4.20269,4.67423,4.97191,5.0233,3.94046,3.28878,5.10742]),
        H298 = (89.4498,'kcal/mol','+|-',9.8244),
        S298 = (5.21479,'cal/mol/K','+|-',18.4328),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 220,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_1R->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C u0 {2,D}
4   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.821618,-0.957556,-1.80588,-1.96611,-2.01019,-1.97554,-2.56419],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (84.6508,'kcal/mol','+|-',5.2),
        S298 = (8.20701,'cal/mol/K','+|-',33.3623),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 221,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_1R->C_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   u0 {2,D}
4   C   ux {2,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.55212,-0.296077,-1.36029,-1.74059,-1.96402,-1.75409,-1.88216],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.5151,'kcal/mol','+|-',5.2),
        S298 = (20.0024,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=CC[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 222,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_N-1R->C",
    group = 
"""
1 * O u1 r0 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D} {4,S}
3   C ux {2,D}
4   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77368,-4.34137,-5.45693,-5.64045,-5.11334,-4.71378,-6.02014],'cal/mol/K','+|-',[4.12618,3.80343,4.08082,4.22632,3,3,4.65255]),
        H298 = (92.6491,'kcal/mol','+|-',5.86028),
        S298 = (3.21998,'cal/mol/K','+|-',7.95794),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 223,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_N-1R->C_Ext-4C-R_Ext-4C-R",
    group = 
"""
1 * O   u1 r0 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D} {4,S}
3   C   ux {2,D}
4   C   u0 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.24365,-4.86089,-6.03354,-6.24508,-5.50158,-4.9563,-6.8789],'cal/mol/K','+|-',[5.36187,4.73863,5.03256,5.19133,3.50034,3,5.05894]),
        H298 = (93.8977,'kcal/mol','+|-',5.59216),
        S298 = (3.87812,'cal/mol/K','+|-',10.7825),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 224,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_N-1R->C_Ext-4C-R_Ext-4C-R_4C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D} {4,S}
3   C   ux r0 {2,D}
4   C   u0 r1 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 225,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_N-1R->C_Ext-4C-R_Ext-4C-R_N-4C-inRing",
    group = 
"""
1 * O   u1 r0 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D} {4,S}
3   C   ux r0 {2,D}
4   C   u0 r0 {2,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
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
    index = 226,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.9579,-3.69425,-3.35886,-2.68492,-1.97687,-1.44557,-2.02639],'cal/mol/K','+|-',[5.76663,7.41471,8.28368,8.14345,6.00415,4.41081,3]),
        H298 = (65.4428,'kcal/mol','+|-',5.67714),
        S298 = (-2.12774,'cal/mol/K','+|-',14.2164),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 227,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,D} {4,[S,D,T,B,Q]}
3   C   u0 {2,D}
4   O   ux r0 {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 228,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 * O u1 r0 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,S}
6   C u0 r0 {5,S}
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
    index = 229,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 * O u1 r0 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D} {4,[S,D,T,B,Q]}
3   C ux {2,D}
4   O ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]} {6,[B,D,T,Q]}
6   C u0 r0 {5,[B,D,T,Q]}
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
    index = 230,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 r0 {1,S} {3,D}
3   C   u0 r0 {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0205149,-0.571163,-1.06998,-1.55077,-2.38493,-3.06757,-4.24563],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (82.5298,'kcal/mol','+|-',2.4),
        S298 = (4.7775,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[C](CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 231,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-4R!H-R",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux {2,D}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.164268,-0.738648,-1.23186,-1.41105,-1.75429,-2.26554,-3.4395],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.2659,'kcal/mol','+|-',6.94554),
        S298 = (-0.722853,'cal/mol/K','+|-',3.31006),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 232,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 {1,S} {3,D}
3   C u0 {2,D}
4   C u0 {1,S} {5,S}
5   C ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.675795,-1.16715,-1.60304,-1.68695,-1.9356,-2.44276,-3.29148],'cal/mol/K','+|-',[3,3,3.20743,3.35084,3,3,3]),
        H298 = (84.2533,'kcal/mol','+|-',5.2),
        S298 = (-1.40126,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 233,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D}
4   C u0 r0 {1,S} {5,S}
5   C ux r1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0951163,-1.85622,-3.17319,-3.32731,-3.21752,-3.50765,-3.9589],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (83.7833,'kcal/mol','+|-',5.2),
        S298 = (-2.11337,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]CC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 234,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 r0 {1,S} {3,D}
3   C u0 r0 {2,D}
4   C u0 r0 {1,S} {5,S}
5   C ux r0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01842,-0.8609,-0.905191,-0.957907,-1.36585,-1.96948,-2.99485],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (84.3534,'kcal/mol','+|-',2.4),
        S298 = (-1.08477,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 235,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   C ux {2,D}
4   C ux {1,[S,D,T,B,Q]} {5,[B,D,T,Q]}
5   C u0 {4,[B,D,T,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4982,0.65399,-0.0255236,-0.514376,-1.16503,-1.68956,-3.92055],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (77.6434,'kcal/mol','+|-',5.2),
        S298 = (1.48197,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C[CH]C#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 236,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C",
    group = 
"""
1 * R u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.104357,-0.668517,-1.30058,-1.73243,-2.27388,-2.75058,-4.30212],'cal/mol/K','+|-',[3.08354,4.01673,5.01958,5.32572,4.79294,4.25976,4.91344]),
        H298 = (96.8903,'kcal/mol','+|-',10.1159),
        S298 = (-0.98143,'cal/mol/K','+|-',6.27639),
    ),
    shortDesc = """Radical correction fitted to 17 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 237,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00778488,-0.5708,-1.20753,-1.64043,-2.18205,-2.66177,-4.24532],'cal/mol/K','+|-',[3,3.9747,5.03649,5.35697,4.80286,4.25259,4.98676]),
        H298 = (96.5815,'kcal/mol','+|-',9.33721),
        S298 = (-0.978125,'cal/mol/K','+|-',6.41569),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 238,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_1C-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.903472,-0.357029,-1.3381,-1.82321,-2.37507,-3.1257,-5.48869],'cal/mol/K','+|-',[4.04209,3,3.22085,4.80958,7.35568,8.5805,9.31434]),
        H298 = (101.954,'kcal/mol','+|-',21.8253),
        S298 = (-1.68086,'cal/mol/K','+|-',9.9981),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 239,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->C",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   O u0 {2,D}
4   C ux {1,[S,D,T,B,Q]} {5,S}
5   C u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.221464,-0.139545,-0.570147,-0.696205,-0.774405,-1.26946,-3.94159],'cal/mol/K','+|-',[3.65301,3,3,3,4.43491,5.26711,8.52591]),
        H298 = (97.4229,'kcal/mol','+|-',14.8919),
        S298 = (-2.46442,'cal/mol/K','+|-',11.6279),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 240,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,T,Q,B]} {3,D}
3   O   u0 {2,D}
4   C   ux {1,[S,D,T,B,Q]} {5,S} {6,S}
5   C   u0 {4,S}
6   R!H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.10424,0.606543,-0.236148,-0.724714,-1.18528,-1.75292,-4.79659],'cal/mol/K','+|-',[3,3,3,3,5.94013,7.06225,11.3065]),
        H298 = (93.189,'kcal/mol','+|-',5.2),
        S298 = (-4.58514,'cal/mol/K','+|-',12.7466),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 241,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
2   C   ux {1,[S,T,Q,B]} {3,D}
3   O   u0 r0 {2,D}
4   C   ux r1 {1,[S,D,T,B,Q]} {5,S} {6,S}
5   C   u0 r1 {4,S}
6   R!H u0 {4,S}
7   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.105122,-0.02969,-0.105572,0.300612,0.914871,0.743958,-0.799121],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.8993,'kcal/mol','+|-',5.2),
        S298 = (-9.09176,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[C]1CC(O)=CC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 242,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_N-5R!H->C",
    group = 
"""
1 * C                      u1 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C                      ux {1,[S,T,Q,B]} {3,D}
3   O                      u0 r0 {2,D}
4   C                      ux r1 {1,[S,D,T,B,Q]} {5,S}
5   [F,I,Br,Cl,O,Si,P,S,N] u0 r1 {4,S}
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
    index = 243,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   O ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.183449,-0.612009,-1.18236,-1.6052,-2.14484,-2.57234,-4.00564],'cal/mol/K','+|-',[3,4.27063,5.41269,5.59567,4.41499,3.18013,3.86636]),
        H298 = (96.0139,'kcal/mol','+|-',6.38007),
        S298 = (-0.842658,'cal/mol/K','+|-',5.81397),
    ),
    shortDesc = """Radical correction fitted to 12 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 244,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,T,Q,B]} {3,D}
3   O   ux {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46401,-1.95523,-2.5697,-2.8802,-3.02675,-3.15183,-4.86428],'cal/mol/K','+|-',[3,6.53424,8.7535,9.17283,7.2523,5.35646,6.49671]),
        H298 = (92.0213,'kcal/mol','+|-',5.2),
        S298 = (-0.100308,'cal/mol/K','+|-',9.86768),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 245,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-1C-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 {1,S} {3,D}
3   O   ux {2,D}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.92674,-8.80987,-12.1947,-13.0484,-11.0743,-9.06759,-10.9213],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (90.0723,'kcal/mol','+|-',5.2),
        S298 = (9.36644,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C=O)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 246,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-2C-R",
    group = 
"""
1 * C u1 r0 {2,S} {4,S}
2   C u0 {1,S} {3,D} {5,S}
3   O u0 {2,D}
4   C u0 {1,S}
5   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.60448,-0.811237,-0.642197,-0.704946,-1.13746,-1.76211,-2.87235],'cal/mol/K','+|-',[3.97292,3.26393,3,3,3,3,3]),
        H298 = (90.5594,'kcal/mol','+|-',5.2),
        S298 = (-2.66936,'cal/mol/K','+|-',5.12075),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 247,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-2C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S} {4,S}
2   C   u0 r0 {1,S} {3,D} {5,S}
3   O   u0 r0 {2,D}
4   C   u0 r0 {1,S} {6,[S,D,T,B,Q]}
5   C   u0 r0 {2,S}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.00912,-1.96521,-1.55445,-1.41295,-1.37093,-1.62023,-2.94668],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.0245,'kcal/mol','+|-',5.2),
        S298 = (-0.858899,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)[CH]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 248,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->O",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   O ux {2,D}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23553,-0.976388,-1.31337,-1.59681,-2.04877,-2.44786,-4.99874],'cal/mol/K','+|-',[3.66612,3.9026,3,3,3,3,5.60153]),
        H298 = (92.703,'kcal/mol','+|-',5.2),
        S298 = (-0.150252,'cal/mol/K','+|-',6.78966),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 249,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->O_4R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   O ux {2,D}
4   C ux r1 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.55917,0.934073,0.0234411,-0.616678,-1.31791,-1.69507,-7.74088],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.788,'kcal/mol','+|-',5.2),
        S298 = (-3.47403,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=CC1([CH]C=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 250,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->O_N-4R!H-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   O ux {2,D}
4   C ux r0 {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   O ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.03317,-1.82548,-1.90751,-2.03242,-2.37359,-2.78243,-3.78],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (92.8979,'kcal/mol','+|-',2.4),
        S298 = (1.32698,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC(=O)OC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 251,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-5R!H->O",
    group = 
"""
1 * C                      u1 r0 {2,S} {4,S}
2   C                      u0 r0 {1,S} {3,D}
3   O                      u0 r0 {2,D}
4   C                      u0 {1,S} {5,S}
5   [F,I,Br,Cl,C,Si,P,S,N] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.462944,-0.569809,-0.882705,-1.23354,-1.93622,-2.30342,-2.35408],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.0119,'kcal/mol','+|-',5.2),
        S298 = (-4.26664,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
O=C[CH]CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 252,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.658393,0.202497,-0.410466,-0.931777,-1.70739,-2.28957,-3.56344],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.7747,'kcal/mol','+|-',4.62823),
        S298 = (-1.19284,'cal/mol/K','+|-',2.09571),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 253,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R_4R!H->C",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   O u0 r0 {2,D}
4   C u0 r0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.215672,0.0265177,-0.440793,-0.858025,-1.56689,-2.23035,-3.41567],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (95.2475,'kcal/mol','+|-',2.4),
        S298 = (-1.90757,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH2]C(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 254,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R_N-4R!H->C",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D} {4,[S,D,T,B,Q]}
3   O ux {2,D}
4   O ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.953541,0.319817,-0.390247,-0.980945,-1.80107,-2.32905,-3.66195],'cal/mol/K','+|-',[2,2,2,2.24952,2.23042,2,2]),
        H298 = (99.4594,'kcal/mol','+|-',2.4),
        S298 = (-0.716347,'cal/mol/K','+|-',2.31563),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 255,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,D} {4,[S,D,T,B,Q]}
3   O   ux {2,D}
4   O   ux {2,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C   ux {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.47769,0.715902,0.0415453,-0.422929,-1.13389,-1.93134,-3.62994],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.2845,'kcal/mol','+|-',2.4),
        S298 = (-1.3944,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OC(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 256,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   O u0 r0 {2,D}
4   O u0 r0 {2,S} {5,S}
5   C u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,S}
7   O u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.410555,-0.488306,-1.45389,-2.2756,-3.08852,-3.01618,-3.66348],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.7552,'kcal/mol','+|-',2.4),
        S298 = (0.620539,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 257,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->O",
    group = 
"""
1 * C u1 r0 {2,S}
2   C u0 r0 {1,S} {3,D} {4,S}
3   O u0 r0 {2,D}
4   O u0 r0 {2,S} {5,S}
5   C u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   C ux {5,[S,D,T,B,Q]} {7,S}
7   C u0 r0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.97238,0.731854,0.241603,-0.244303,-1.18079,-2.03962,-3.69242],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.3384,'kcal/mol','+|-',2.4),
        S298 = (-1.37518,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(=O)OCC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 258,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_N-1R->C",
    group = 
"""
1 * O u1 {2,[S,T,Q,B]}
2   C ux {1,[S,T,Q,B]} {3,D}
3   O u0 r0 {2,D}
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
    index = 259,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C",
    group = 
"""
1 * R   u1 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.303806,-1.56888,-2.4763,-2.99313,-3.49317,-3.91947,-4.89948],'cal/mol/K','+|-',[3.35386,3.44179,3.62031,3.49949,3.01932,3,3.18735]),
        H298 = (103.781,'kcal/mol','+|-',18.4074),
        S298 = (1.2241,'cal/mol/K','+|-',10.1498),
    ),
    shortDesc = """Radical correction fitted to 59 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 260,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C   ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.47928,-2.23046,-3.22927,-3.72285,-4.06003,-4.35266,-5.26291],'cal/mol/K','+|-',[3.62814,3.27689,3.23717,3,3,3,3.50657]),
        H298 = (99.2478,'kcal/mol','+|-',6.30956),
        S298 = (2.62595,'cal/mol/K','+|-',14.4287),
    ),
    shortDesc = """Radical correction fitted to 25 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 261,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01036,-2.36595,-3.31909,-3.82756,-4.09011,-4.37749,-6.1133],'cal/mol/K','+|-',[3,3,3.07232,3,3,3,3.63357]),
        H298 = (97.4686,'kcal/mol','+|-',5.75476),
        S298 = (5.48083,'cal/mol/K','+|-',15.7848),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 262,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.40854,-2.81667,-3.73358,-4.17883,-4.30984,-4.60736,-6.88268],'cal/mol/K','+|-',[3,3,3,3,3,3,3.44132]),
        H298 = (96.1727,'kcal/mol','+|-',5.2),
        S298 = (3.52314,'cal/mol/K','+|-',7.12212),
    ),
    shortDesc = """Radical correction fitted to 7 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 263,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-2C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,S} {6,[S,D,T,B,Q]}
3   O   u0 {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0592,-2.96771,-3.93755,-4.29105,-4.30297,-4.86438,-6.5321],'cal/mol/K','+|-',[3,3,3,3.19357,3.61749,3.60344,3]),
        H298 = (93.7836,'kcal/mol','+|-',5.2),
        S298 = (1.94249,'cal/mol/K','+|-',9.40773),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 264,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 * C   u1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
3   O   u0 {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   R!H ux {2,[S,D,T,B,Q]}
7   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.30421,-3.50992,-4.56077,-4.86429,-4.77036,-5.28771,-6.88918],'cal/mol/K','+|-',[3,3,3,3,3.79294,3.89566,3]),
        H298 = (93.0185,'kcal/mol','+|-',5.2),
        S298 = (2.12896,'cal/mol/K','+|-',11.4858),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 265,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-2C-R_Ext-2C-R_Ext-3O-R_Ext-8R!H-R_Ext-9R!H-R",
    group = 
"""
1  * C   u1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2    C   ux {1,S} {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
3    O   u0 {2,S} {8,[S,D,T,B,Q]}
4    R!H ux {1,[S,D,T,B,Q]}
5    R!H ux {1,[S,D,T,B,Q]}
6    R!H ux {2,[S,D,T,B,Q]}
7    R!H ux {2,[S,D,T,B,Q]}
8    O   ux {3,[S,D,T,B,Q]} {9,S}
9    C   u0 {8,S} {10,[S,D,T,B,Q]}
10   C   ux {9,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.05129,-3.14471,-4.10065,-4.25555,-3.91171,-4.40416,-6.64322],'cal/mol/K','+|-',[3,3,3,3,3.32835,3.40833,3]),
        H298 = (92.0377,'kcal/mol','+|-',5.2),
        S298 = (-0.323618,'cal/mol/K','+|-',10.9309),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 266,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-2C-R_Ext-2C-R_Ext-3O-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_11R!H->O",
    group = 
"""
1  * C   u1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2    C   ux {1,S} {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
3    O   u0 {2,S} {8,[S,D,T,B,Q]}
4    R!H ux {1,[S,D,T,B,Q]}
5    R!H ux {1,[S,D,T,B,Q]}
6    R!H ux {2,[S,D,T,B,Q]}
7    R!H ux {2,[S,D,T,B,Q]}
8    O   ux {3,[S,D,T,B,Q]} {9,S}
9    C   u0 r0 {8,S} {10,[S,D,T,B,Q]}
10   C   ux {9,[S,D,T,B,Q]} {11,[S,D]}
11   O   u0 r0 {10,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3535,-3.11341,-4.56582,-5.11654,-5.08845,-5.60919,-6.92558],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (91.0423,'kcal/mol','+|-',5.2),
        S298 = (3.54103,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](C)C(C)(C)OOC(C)(C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 267,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-2C-R_Ext-2C-R_Ext-3O-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_N-11R!H->O",
    group = 
"""
1  * C   u1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2    C   ux {1,S} {3,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
3    O   u0 {2,S} {8,[S,D,T,B,Q]}
4    R!H ux {1,[S,D,T,B,Q]}
5    R!H ux {1,[S,D,T,B,Q]}
6    R!H ux {2,[S,D,T,B,Q]}
7    R!H ux {2,[S,D,T,B,Q]}
8    O   ux {3,[S,D,T,B,Q]} {9,S}
9    C   u0 r0 {8,S} {10,[S,D,T,B,Q]}
10   C   ux {9,[S,D,T,B,Q]} {11,[S,D]}
11   C   u0 r0 {10,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.74907,-3.17601,-3.63548,-3.39456,-2.73496,-3.19913,-6.36086],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (93.0331,'kcal/mol','+|-',5.2),
        S298 = (-4.18827,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(COO)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 268,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-5R!H-R_4R!H-inRing",
    group = 
"""
1 * C   u1 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,S}
3   O   u0 {2,S}
4   C   u0 r1 {1,S}
5   C   u0 {1,S} {6,S}
6   R!H u0 {5,S}
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
    index = 269,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-5R!H-R_N-4R!H-inRing",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   C   ux r0 {1,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08812,-2.2025,-3.18596,-3.79532,-4.09653,-4.21244,-6.63717],'cal/mol/K','+|-',[3,3.02587,3.06704,3,3,3,6.09862]),
        H298 = (97.3355,'kcal/mol','+|-',5.2),
        S298 = (4.66342,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 270,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-5R!H-R_N-4R!H-inRing_1R-inRing",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   C   ux r0 {1,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 271,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-5R!H-R_N-4R!H-inRing_N-1R-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   O   ux {2,[S,T,Q,B]}
4   C   ux r0 {1,[S,D,T,B,Q]}
5   C   ux {1,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.631395,-1.54416,-2.51866,-3.24566,-3.61672,-3.6557,-5.31029],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (97.4825,'kcal/mol','+|-',2.4),
        S298 = (4.81571,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[C](COO)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 272,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_N-3R!H->O",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.38464,-1.65769,-2.66774,-3.27557,-3.74482,-4.01626,-4.90429],'cal/mol/K','+|-',[3.68996,3.57527,3.76736,3.63577,3,3,3]),
        H298 = (99.2697,'kcal/mol','+|-',5.27828),
        S298 = (8.55721,'cal/mol/K','+|-',25.073),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 273,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_N-3R!H->O_1R-inRing",
    group = 
"""
1 * C   u1 r1 {2,S} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   ux {1,S} {3,S}
3   C   u0 {2,S}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
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
C1=CC2[C](C1)C1C=CC2C1 - Radical thermo from pang.py and closed shell thermo from Thermo library: pang.py
""",
)

entry(
    index = 274,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_N-3R!H->O_N-1R-inRing",
    group = 
"""
1 * C   u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.608045,-2.49449,-3.82546,-4.45599,-4.61365,-4.56994,-5.29063],'cal/mol/K','+|-',[4.9586,3.73306,3,3,3,3,3.4134]),
        H298 = (97.169,'kcal/mol','+|-',5.2),
        S298 = (14.8826,'cal/mol/K','+|-',24.6446),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 275,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_N-3R!H->O_N-1R-inRing_Ext-2C-R",
    group = 
"""
1 * C   u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 {1,[S,T,Q,B]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.666893,-1.51139,-3.20027,-3.95052,-4.08836,-3.99025,-4.85969],'cal/mol/K','+|-',[3.18815,3,3,3,3,3,4.34113]),
        H298 = (97.5315,'kcal/mol','+|-',5.81022),
        S298 = (16.0317,'cal/mol/K','+|-',34.3951),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 276,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_N-3R!H->O_N-1R-inRing_Ext-2C-R_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 * C   u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
2   C   u0 r0 {1,[S,T,Q,B]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   C   ux r0 {2,[S,T,Q,B]}
4   R!H ux {1,[S,D,T,B,Q]}
5   R!H ux {1,[S,D,T,B,Q]}
6   C   ux {2,[S,D,T,B,Q]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
7   R!H ux {6,[S,D,T,B,Q]}
8   R!H ux {6,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.79407,-0.746857,-2.34822,-3.24767,-3.66704,-3.48603,-3.32486],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.4773,'kcal/mol','+|-',5.2),
        S298 = (28.1922,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 277,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.371984,-2.13524,-3.28151,-3.70638,-4.00944,-4.28955,-4.31283],'cal/mol/K','+|-',[3.21775,3.90122,4.30883,3.94672,3,3,3.39852]),
        H298 = (101.654,'kcal/mol','+|-',5.8413),
        S298 = (-2.00751,'cal/mol/K','+|-',14.1791),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 278,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.819104,-3.21365,-4.72901,-4.85737,-4.55546,-4.42728,-3.28798],'cal/mol/K','+|-',[3.78434,3,3,3,3,3,3.76543]),
        H298 = (100.091,'kcal/mol','+|-',7.92639),
        S298 = (-9.27866,'cal/mol/K','+|-',4.09703),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 279,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 {1,S} {3,S} {6,S}
3   O u0 r0 {2,S}
4   C u0 {1,S} {5,[S,D,T,B,Q]}
5   C ux {4,[S,D,T,B,Q]}
6   C u0 {2,S}
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
    index = 280,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]} {5,S}
5   C u0 {4,S}
6   C ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57479,-3.78457,-5.15701,-5.26793,-4.6349,-4.16379,-2.99449],'cal/mol/K','+|-',[3,3,3,3,3,3.16919,4.38182]),
        H298 = (100.072,'kcal/mol','+|-',9.70735),
        S298 = (-9.68408,'cal/mol/K','+|-',4.60802),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 281,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R_N-1R-inRing_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2    C ux r0 {1,[S,T,Q,B]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3    O ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4    C ux r0 {1,[S,D,T,B,Q]} {5,S}
5    C u0 r0 {4,S}
6    C ux r0 {2,[S,D,T,B,Q]}
7    O ux {3,[S,D,T,B,Q]} {8,S}
8    C u0 r1 {7,S} {9,[S,D,T,B,Q]}
9    C ux r1 {8,[S,D,T,B,Q]} {10,S}
10   C u0 r1 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.17194,-4.85996,-5.95926,-5.54068,-3.75194,-2.38905,-0.571621],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (95.7021,'kcal/mol','+|-',5.2),
        S298 = (-12.1329,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]C(CC)OOC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 282,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R_N-1R-inRing_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-10R!H-9R!H",
    group = 
"""
1  * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2    C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3    O ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4    C ux {1,[S,D,T,B,Q]} {5,S}
5    C u0 {4,S}
6    C ux {2,[S,D,T,B,Q]}
7    O ux {3,[S,D,T,B,Q]} {8,S}
8    C u0 {7,S} {9,[S,D,T,B,Q]}
9    C ux {8,[S,D,T,B,Q]} {10,D}
10   C u0 {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.776213,-3.24688,-4.75589,-5.13155,-5.07637,-5.05116,-4.20593],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.257,'kcal/mol','+|-',8.59646),
        S298 = (-8.45968,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 283,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R_N-1R-inRing_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-10R!H-9R!H_Ext-10R!H-R_Ext-10R!H-R",
    group = 
"""
1  * C   u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2    C   ux r0 {1,[S,T,Q,B]} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3    O   ux {2,[S,T,Q,B]} {7,[S,D,T,B,Q]}
4    C   ux r0 {1,[S,D,T,B,Q]} {5,S}
5    C   u0 r0 {4,S}
6    C   ux r0 {2,[S,D,T,B,Q]}
7    O   ux {3,[S,D,T,B,Q]} {8,S}
8    C   u0 r1 {7,S} {9,[S,D,T,B,Q]}
9    C   ux r1 {8,[S,D,T,B,Q]} {10,D}
10   C   u0 r1 {9,D} {11,[S,D,T,B,Q]} {12,[S,D,T,B,Q]}
11   R!H ux {10,[S,D,T,B,Q]}
12   R!H ux {10,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.600264,-3.12594,-4.70395,-5.21884,-5.3292,-5.43674,-4.8363],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (99.2173,'kcal/mol','+|-',5.2),
        S298 = (-9.36023,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]C(CC)OOC1C=CCC(C)=C1 - Radical thermo from pang.py and closed shell thermo from GAV
""",
)

entry(
    index = 284,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
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
CC1[CH]CO1 - Radical thermo from johnson_g4.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 285,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   O ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.938153,-2.77209,-3.76552,-4.42535,-4.94165,-5.32098,-5.85683],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (100.375,'kcal/mol','+|-',5.2),
        S298 = (4.76232,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Derived using the following species:
CC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 286,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.372731,-2.09964,-2.99538,-3.54888,-4.06858,-4.38694,-4.89157],'cal/mol/K','+|-',[5.09718,3.62159,3,3,3,3,3]),
        H298 = (99.4988,'kcal/mol','+|-',5.2),
        S298 = (3.22161,'cal/mol/K','+|-',4.26066),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 287,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]} {5,S}
3   C ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
5   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.71754,-2.22301,-3.23415,-3.719,-4.08029,-4.19891,-4.86069],'cal/mol/K','+|-',[4.5707,4.61672,3.3309,3,3,3,3]),
        H298 = (98.2863,'kcal/mol','+|-',5.2),
        S298 = (2.72888,'cal/mol/K','+|-',5.64615),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 288,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]} {5,S}
3   C ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
5   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.50265,-2.26893,-3.27043,-3.69096,-3.94226,-3.9491,-4.50775],'cal/mol/K','+|-',[4.06737,5.64983,4.07563,3,3,3,3]),
        H298 = (98.2084,'kcal/mol','+|-',5.2),
        S298 = (2.11601,'cal/mol/K','+|-',6.22927),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 289,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R_1R-inRing_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 * C   u1 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C   ux r1 {1,[S,T,Q,B]} {3,[S,T,Q,B]} {5,S}
3   C   ux {2,[S,T,Q,B]}
4   C   ux r1 {1,[S,D,T,B,Q]}
5   C   u0 r1 {2,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
7   R!H ux {5,[S,D,T,B,Q]}
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
    index = 290,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R_1R-inRing_Ext-5R!H-R_3C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,S} {5,S}
3   C u0 r1 {2,S}
4   C u0 r1 {1,S}
5   C u0 {2,S} {6,S}
6   C u0 r1 {5,S}
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
    index = 291,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R_1R-inRing_Ext-5R!H-R_N-3C-inRing",
    group = 
"""
1 * C u1 r1 {2,S} {4,S}
2   C u0 r1 {1,S} {3,S} {5,S}
3   C u0 r0 {2,S}
4   C u0 r1 {1,S}
5   C u0 r1 {2,S} {6,S}
6   C u0 r1 {5,S}
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
    index = 292,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]} {5,S}
3   C ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
5   C u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.637796,-2.08524,-3.12532,-3.80312,-4.49437,-4.94833,-5.9195],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (98.5201,'kcal/mol','+|-',5.2),
        S298 = (4.5675,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 293,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_1R-inRing",
    group = 
"""
1 * C u1 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
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
    index = 294,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_N-1R-inRing",
    group = 
"""
1 * C u1 r0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
2   C ux {1,[S,T,Q,B]} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
4   C ux {1,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.20839,-2.59891,-2.88125,-3.12984,-3.54492,-3.87844,-4.52075],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (99.4401,'kcal/mol','+|-',2.4),
        S298 = (4.09684,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 295,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C",
    group = 
"""
1 * R   u1 {2,[S,T,Q,B]}
2   C   ux {1,[S,T,Q,B]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   R!H ux {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.363518,-0.5087,-1.35599,-1.8961,-2.50238,-2.93452,-4.38062],'cal/mol/K','+|-',[3.18979,3.96468,4.94451,4.97963,3.44489,3,3]),
        H298 = (93.1766,'kcal/mol','+|-',55.9067),
        S298 = (0.639084,'cal/mol/K','+|-',5.39821),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 296,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C_1R->C",
    group = 
"""
1 * C   u1 {2,[S,T,Q,B]}
2   C   u0 {1,[S,T,Q,B]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   R!H u0 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O   u0 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.898201,-0.399236,-1.45162,-2.11313,-2.75612,-3.1752,-4.69998],'cal/mol/K','+|-',[3,5.37629,6.73316,6.66877,4.42878,3,3.17368]),
        H298 = (101.145,'kcal/mol','+|-',5.2),
        S298 = (1.48461,'cal/mol/K','+|-',5.0936),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 297,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C_1R->C_3R!H->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C u0 r1 {1,[S,T,Q,B]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   C u0 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O u0 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.49847,0.770492,0.0133183,-0.662195,-1.79254,-2.66708,-4.00948],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (100.73,'kcal/mol','+|-',2.4),
        S298 = (0.376393,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(COC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 298,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C_1R->C_N-3R!H->C",
    group = 
"""
1 * C u1 {2,[S,T,Q,B]}
2   C u0 r1 {1,[S,T,Q,B]} {3,[S,T,Q,B]} {4,[S,D,T,B,Q]}
3   O u0 r1 {2,[S,T,Q,B]} {4,[S,D,T,B,Q]}
4   O u0 r1 {2,[S,D,T,B,Q]} {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.452413,-3.03112,-4.74775,-5.37773,-4.92417,-4.31848,-6.25361],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.093,'kcal/mol','+|-',5.2),
        S298 = (3.97811,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 299,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C_N-1R->C",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,S} {4,S}
3   O   ux r1 {2,S} {4,S}
4   R!H ux r1 {2,S} {3,S}
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
    index = 300,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R",
    group = 
"""
1 * R   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.195822,-1.20497,-2.08829,-2.63262,-3.23468,-3.75139,-4.74144],'cal/mol/K','+|-',[3.30176,3.40284,3.6207,3.60367,3.26778,3.13134,3.08101]),
        H298 = (105.266,'kcal/mol','+|-',8.83734),
        S298 = (0.360441,'cal/mol/K','+|-',6.48229),
    ),
    shortDesc = """Radical correction fitted to 30 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 301,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.458743,-0.637137,-1.58145,-2.3252,-3.23824,-4.02326,-5.27533],'cal/mol/K','+|-',[3,3,3,3.38813,3.45372,3.53107,3.09322]),
        H298 = (103.215,'kcal/mol','+|-',10.8296),
        S298 = (2.3172,'cal/mol/K','+|-',4.43409),
    ),
    shortDesc = """Radical correction fitted to 14 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 302,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing",
    group = 
"""
1 * C u1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.09372,-0.369139,-1.7663,-2.62928,-3.72324,-4.67899,-5.89921],'cal/mol/K','+|-',[4.1981,3.55948,4.30852,5.17047,5.36815,5.43803,4.86641]),
        H298 = (104.58,'kcal/mol','+|-',17.1254),
        S298 = (1.84859,'cal/mol/K','+|-',4.83002),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 303,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_Ext-2C-R_Ext-4R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux {2,[S,T,Q,B]} {4,S}
4   C   u0 {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.46227,-0.0228981,-3.08964,-4.60546,-6.13241,-7.54823,-7.08454],'cal/mol/K','+|-',[5.31299,6.71264,7.03684,8.16991,8.08685,6.89863,3.76195]),
        H298 = (119.444,'kcal/mol','+|-',19.9459),
        S298 = (0.162322,'cal/mol/K','+|-',7.44441),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 304,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_Ext-2C-R_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S} {7,[S,D,T,B,Q]}
4   C   u0 r1 {3,S} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
6   R!H ux {4,[S,D,T,B,Q]}
7   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.34069,2.35038,-0.601743,-1.71696,-3.27328,-5.10919,-5.75448],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (112.392,'kcal/mol','+|-',5.2),
        S298 = (-2.46967,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1OOC(O)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 305,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C u1 {2,S}
2   C ux r1 {1,S} {3,[S,T,Q,B]}
3   C ux {2,[S,T,Q,B]} {4,S}
4   C ux {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0239315,-0.99695,-1.93133,-2.60829,-3.49936,-4.23964,-6.30706],'cal/mol/K','+|-',[3,3.65325,4.23612,4.5688,4.11684,3.89872,7.80416]),
        H298 = (101.403,'kcal/mol','+|-',5.2),
        S298 = (3.12671,'cal/mol/K','+|-',4.93),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 306,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r1 {1,S} {3,[S,T,Q,B]}
3   C   ux r1 {2,[S,T,Q,B]} {4,S} {5,[S,D,T,B,Q]}
4   C   ux r1 {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.32774,-2.78535,-4.00506,-4.84489,-5.51469,-6.14821,-10.1275],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.71,'kcal/mol','+|-',5.2),
        S298 = (5.54011,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1OOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 307,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 r0 {2,S}
2   C                      u0 r1 {1,S} {3,S}
3   C                      u0 r1 {2,S} {4,S}
4   [F,I,Br,Cl,O,Si,P,S,N] u0 r1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.602746,0.229929,-0.351621,-0.902974,-1.90514,-2.76317,-4.25649],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (102.101,'kcal/mol','+|-',2.4),
        S298 = (1.50132,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 308,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.118574,-0.780708,-1.48242,-2.16231,-2.97843,-3.67197,-4.9411],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.504,'kcal/mol','+|-',7.53497),
        S298 = (2.56825,'cal/mol/K','+|-',4.46695),
    ),
    shortDesc = """Radical correction fitted to 9 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 309,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,S}
3   R!H ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0129039,-0.905866,-1.64375,-2.24651,-3.05583,-3.75561,-4.94527],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (103.206,'kcal/mol','+|-',5.2),
        S298 = (2.89897,'cal/mol/K','+|-',3.83469),
    ),
    shortDesc = """Radical correction fitted to 8 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 310,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,S}
3   R!H ux {2,S} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.432067,-1.61609,-2.45648,-3.06473,-3.70823,-4.34329,-5.50257],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.711,'kcal/mol','+|-',5.2),
        S298 = (4.06369,'cal/mol/K','+|-',4.37521),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 311,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C_Ext-3R!H-R",
    group = 
"""
1 * C   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,S}
3   R!H ux {2,S} {4,S} {5,[S,D,T,B,Q]}
4   C   ux {3,S}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.329258,-2.19057,-4.03189,-5.22154,-5.83838,-6.37249,-6.95002],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.037,'kcal/mol','+|-',5.2),
        S298 = (0.735312,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)(C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 312,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C_Ext-4C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,S}
3   R!H ux {2,S} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]} {5,[S,D,T,B,Q]}
5   R!H ux {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39488,-1.7446,-2.16755,-2.58023,-3.20861,-3.83056,-5.07751],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (102.24,'kcal/mol','+|-',5.2),
        S298 = (3.38031,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 313,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C_Ext-2C-R",
    group = 
"""
1 * C   u1 {2,S}
2   C   ux r0 {1,S} {3,S} {5,[S,D,T,B,Q]}
3   R!H ux {2,S} {4,[S,D,T,B,Q]}
4   C   ux {3,[S,D,T,B,Q]}
5   R!H ux {2,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.689779,-1.0042,-2.35691,-3.27525,-4.11171,-4.83684,-5.989],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (101.974,'kcal/mol','+|-',5.2),
        S298 = (3.66199,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 314,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C_Ext-3R!H-R_N-4R!H->C",
    group = 
"""
1 * C                      u1 {2,S}
2   C                      u0 r0 {1,S} {3,S}
3   R!H                    u0 r0 {2,S} {4,S}
4   [F,I,Br,Cl,O,Si,P,S,N] u0 r0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.37521,-0.248253,-0.891218,-1.4889,-2.45177,-3.21145,-4.42926],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (103.511,'kcal/mol','+|-',2.4),
        S298 = (1.82053,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH2]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
[CH2]C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 315,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_N-Sp-3R!H-2C",
    group = 
"""
1 * C   u1 {2,S}
2   C   u0 r0 {1,S} {3,T}
3   R!H u0 r0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.82779,0.846349,0.614802,-1.06771,-1.97213,-2.58468,-4.88683],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (86.531,'kcal/mol','+|-',5.2),
        S298 = (-1.73124,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[CH2]C#CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 316,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.794679,-1.72448,-2.55199,-2.91387,-3.23142,-3.50267,-4.25299],'cal/mol/K','+|-',[3.26083,3.85869,3.99914,3.83159,3.2259,3,3]),
        H298 = (107.208,'kcal/mol','+|-',5.2),
        S298 = (-1.42979,'cal/mol/K','+|-',6.05729),
    ),
    shortDesc = """Radical correction fitted to 16 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 317,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,S}
3   C   ux {2,S} {4,D}
4   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.827632,-1.29677,-1.7122,-1.79245,-1.94481,-2.23794,-2.95709],'cal/mol/K','+|-',[5.01548,4.48704,3.62503,3.3294,3,3,3]),
        H298 = (109.421,'kcal/mol','+|-',5.2),
        S298 = (-5.26227,'cal/mol/K','+|-',4.55768),
    ),
    shortDesc = """Radical correction fitted to 5 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 318,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S} {3,S}
3   C ux {2,S} {4,D}
4   C ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.45681,-1.74624,-2.02891,-1.97072,-1.99491,-2.2169,-2.76268],'cal/mol/K','+|-',[4.79413,4.63221,3.85308,3.73261,3.37994,3,3]),
        H298 = (109.557,'kcal/mol','+|-',5.2),
        S298 = (-5.47784,'cal/mol/K','+|-',5.14368),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 319,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2C-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,S} {5,S}
3   C   ux {2,S} {4,D}
4   C   ux {3,D}
5   R!H u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.592962,0.143229,-0.57385,-0.62364,-0.84111,-1.39387,-2.46528],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (109.16,'kcal/mol','+|-',5.2),
        S298 = (-6.71584,'cal/mol/K','+|-',4.00878),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 320,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2C-R_Ext-3R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   ux r0 {1,S} {3,S} {5,S}
3   C   ux r0 {2,S} {4,D} {6,[S,D,T,B,Q]}
4   C   ux r0 {3,D}
5   R!H u0 r0 {2,S}
6   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8418,0.195242,-0.344673,-0.232399,-0.416515,-0.838626,-2.26743],'cal/mol/K','+|-',[3,3,3,3,3,3,3]),
        H298 = (108.327,'kcal/mol','+|-',5.2),
        S298 = (-8.13316,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
C=C(C)C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

entry(
    index = 321,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-4C-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   C   u0 r0 {2,S} {4,D}
4   C   u0 r0 {3,D} {5,S}
5   C   u0 r0 {4,S} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
    index = 322,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C",
    group = 
"""
1 * O u1 r0 {2,S}
2   C ux r0 {1,S} {3,S}
3   C ux r0 {2,S} {4,D}
4   O ux r0 {3,D}
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
    index = 323,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.785773,-1.84008,-2.77896,-3.21695,-3.57916,-3.84448,-4.60323],'cal/mol/K','+|-',[3,3.79691,4.09292,3.83133,3.00856,3,3]),
        H298 = (106.875,'kcal/mol','+|-',5.2),
        S298 = (-0.39398,'cal/mol/K','+|-',4.54697),
    ),
    shortDesc = """Radical correction fitted to 11 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 324,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-4R!H-R_Int-5R!H-2C",
    group = 
"""
1 * O   u1 {2,S}
2   C   u0 {1,S} {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
3   R!H u0 {2,[S,T,Q,B]} {4,S}
4   R!H u0 {3,S} {5,[S,D,T,B,Q]}
5   R!H u0 {2,[S,D,T,B,Q]} {4,[S,D,T,B,Q]}
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
    index = 325,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing",
    group = 
"""
1 * O     u1 {2,S}
2   C     ux {1,S} {3,[S,T,Q,B]}
3   C     ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   [C,O] ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.10613,-2.47651,-3.68219,-4.07791,-4.01111,-4.01793,-5.29959],'cal/mol/K','+|-',[3,3,3.39989,3.75246,3.63889,3.37908,4.58544]),
        H298 = (108.211,'kcal/mol','+|-',5.2),
        S298 = (-0.102118,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 4 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 326,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_2C-inRing",
    group = 
"""
1 * O     u1 r0 {2,S}
2   C     u0 r1 {1,S} {3,S}
3   C     u0 r1 {2,S} {4,S}
4   [C,O] u0 r1 {3,S}
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
    index = 327,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_N-2C-inRing",
    group = 
"""
1 * O     u1 {2,S}
2   C     ux r0 {1,S} {3,[S,T,Q,B]}
3   C     ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   [C,O] ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04994,-1.99146,-3.05013,-3.50898,-3.58094,-3.77018,-4.76852],'cal/mol/K','+|-',[3,3,3,3.00757,3.55268,3.77747,4.52202]),
        H298 = (108.225,'kcal/mol','+|-',5.2),
        S298 = (-0.505446,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 328,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_N-2C-inRing_Ext-4R!H-R_Int-5R!H-3R!H",
    group = 
"""
1 * O     u1 {2,S}
2   C     ux r0 {1,S} {3,[S,T,Q,B]}
3   C     ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,S}
4   [C,O] ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   [C,O] ux {3,S} {4,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.28896,-1.9667,-2.70971,-2.88532,-2.81281,-2.95385,-4.59234],'cal/mol/K','+|-',[3,3,3,3,3,3,6.08159]),
        H298 = (107.761,'kcal/mol','+|-',5.2),
        S298 = (-0.819552,'cal/mol/K','+|-',3),
    ),
    shortDesc = """Radical correction fitted to 2 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 329,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_N-2C-inRing_Ext-4R!H-R_Int-5R!H-3R!H_Ext-4R!H-R",
    group = 
"""
1 * O     u1 {2,S}
2   C     ux r0 {1,S} {3,[S,T,Q,B]}
3   C     ux r1 {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,S}
4   [C,O] ux r1 {3,[S,T,Q,B]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5   [C,O] ux r1 {3,S} {4,[S,D,T,B,Q]}
6   R!H   ux {4,[S,D,T,B,Q]}
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
    index = 330,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.884281,-1.79394,-2.55481,-2.96248,-3.42687,-3.76868,-4.25776],'cal/mol/K','+|-',[3.00967,4.20226,4.44298,4.03634,3.07078,3,3]),
        H298 = (106.734,'kcal/mol','+|-',5.2),
        S298 = (-0.4289,'cal/mol/K','+|-',5.52726),
    ),
    shortDesc = """Radical correction fitted to 6 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 331,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]} {5,[S,D,T,B,Q]}
5   R!H u0 r0 {4,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
6   R!H ux {5,[S,D,T,B,Q]}
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
[O]COOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 332,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-3R!H-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]} {5,[S,D,T,B,Q]}
4   R!H ux {3,[S,T,Q,B]}
5   R!H ux {3,[S,D,T,B,Q]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.328727,-0.999969,-1.56298,-1.95559,-2.3922,-2.88674,-4.0924],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (105.37,'kcal/mol','+|-',2.4),
        S298 = (-1.66614,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
CCC(C[O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 333,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Sp-5R!H-4R!H",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]} {5,S}
5   R!H ux {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09237,-1.39355,-1.89772,-2.23493,-2.68338,-3.07351,-3.88097],'cal/mol/K','+|-',[3,4.40212,4.7191,4.28792,3,3,3]),
        H298 = (106.143,'kcal/mol','+|-',5.2),
        S298 = (-2.34492,'cal/mol/K','+|-',3.88999),
    ),
    shortDesc = """Radical correction fitted to 3 radicals""",
    longDesc = 
"""
Averaged from children nodes
""",
)

entry(
    index = 334,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2C-R",
    group = 
"""
1 * O   u1 {2,S}
2   C   ux {1,S} {3,[S,T,Q,B]} {6,[S,D,T,B,Q]}
3   R!H ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   R!H ux {3,[S,T,Q,B]} {5,S}
5   R!H ux {4,S}
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
CC([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 335,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Sp-5R!H-4R!H_4R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   C ux {3,[S,T,Q,B]} {5,S}
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
    index = 336,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Sp-5R!H-4R!H_N-4R!H->C",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S} {3,[S,T,Q,B]}
3   O ux r0 {2,[S,T,Q,B]} {4,[S,T,Q,B]}
4   O ux {3,[S,T,Q,B]} {5,S}
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
COOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 337,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    group = 
"""
1 * O   u1 r0 {2,S}
2   C   u0 r0 {1,S} {3,S}
3   R!H u0 r0 {2,S} {4,S}
4   R!H u0 r0 {3,S} {5,[B,D,T,Q]}
5   R!H u0 r0 {4,[B,D,T,Q]}
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
[O]CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

entry(
    index = 338,
    label = "RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_N-Sp-2C-1R",
    group = 
"""
1 * R   u1 r0 {2,T}
2   C   ux {1,T} {3,[S,T,Q,B]}
3   R!H ux {2,[S,T,Q,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.38436,-2.02874,-2.31305,-2.54584,-2.9761,-3.36561,-4.19473],'cal/mol/K','+|-',[2,2,2,2,2,2,2]),
        H298 = (134.66,'kcal/mol','+|-',2.4),
        S298 = (0.911082,'cal/mol/K','+|-',2),
    ),
    shortDesc = """Radical correction fitted to 1 radicals""",
    longDesc = 
"""
Derived using the following species:
[C]#CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from Thermo library: dong_pio_liang.py
""",
)

tree(
"""
L1: Root
    L2: RJ1
        L3: RJ1_Ext-1R-R_Sp-2R!H=1R
            L4: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C
                L5: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_1R-inRing
                    L6: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_1R-inRing_Ext-2C-R_Ext-2C-R
                L5: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing
                    L6: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R
                        L7: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C
                            L8: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_2C-inRing
                                L9: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_2C-inRing_Ext-3R!H-R_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_2C-inRing_Ext-3R!H-R_Ext-2C-R_3R!H->O
                                    L10: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_2C-inRing_Ext-3R!H-R_Ext-2C-R_N-3R!H->O
                            L8: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing
                                L9: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R
                                    L10: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_Ext-3R!H-R_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_4R!H->C
                                        L11: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_4R!H->C_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_N-4R!H->C
                                        L11: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_Ext-1R-R_N-4R!H->C_Ext-2C-R
                                L9: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_3R!H->O
                                L9: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_Sp-3R!H-2C_N-2C-inRing_N-3R!H->O
                        L7: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_N-Sp-3R!H-2C
                            L8: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_N-Sp-3R!H-2C_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-2C-R_N-Sp-3R!H-2C_Ext-1R-R
                    L6: RJ1_Ext-1R-R_Sp-2R!H=1R_2R!H->C_N-1R-inRing_Ext-1R-R_Ext-3R!H-R
            L4: RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C
                L5: RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_4R!H->C
                    L6: RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_4R!H->C_3R!H->C
                        L7: RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_4R!H->C_3R!H->C_3C-inRing
                        L7: RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_4R!H->C_3R!H->C_N-3C-inRing
                    L6: RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_4R!H->C_N-3R!H->C
                L5: RJ1_Ext-1R-R_Sp-2R!H=1R_N-2R!H->C_Ext-1R-R_Ext-3R!H-R_N-4R!H->C
        L3: RJ1_Ext-1R-R_N-Sp-2R!H=1R
            L4: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O
                L5: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R_Ext-1R-R
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R_Ext-1R-R_Ext-3R!H-R
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_Ext-5R!H-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_Ext-5R!H-R_3R!H->C
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_Int-3R!H-1R_Ext-1R-R_Ext-4R!H-R_Ext-5R!H-R_N-3R!H->C
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_Sp-4C=3C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-1C-R
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-1C-R_Ext-4C-R
                                                        L15: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-1C-R_Ext-4C-R_5O-inRing
                                                            L16: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-1C-R_Ext-4C-R_5O-inRing_Ext-1C-R
                                                        L15: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-1C-R_Ext-4C-R_N-5O-inRing
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_Ext-5O-R
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_1C-inRing
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_5R!H->O_N-1C-inRing
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_N-5R!H->O
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-4C-R_N-5R!H->O_Ext-1C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_4R!H->C_N-Sp-4C=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_N-4R!H->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_N-4R!H->C_Ext-3C-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-3C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4BrClFINOPSSi-R
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R_Ext-1C-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-5R!H-R_Ext-6R!H-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_1R->C_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C_Ext-3C-R_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C_Ext-3C-R_Ext-5R!H-R_6R!H->O
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C_Ext-3C-R_Ext-5R!H-R_N-6R!H->O
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_Sp-4O-3C_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_4R!H->O_N-Sp-4O-3C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O_7R!H->O
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O_7R!H->O_Int-7O-5O_Ext-3C-R_Ext-8R!H-R
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O_N-7R!H->O
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O_N-7R!H->O_Ext-5O-R
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_5R!H->O_N-7R!H->O_Ext-3C-R
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-5R!H->O
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_Sp-5R!H-4BrCClFINPSSi_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_3C-inRing_Ext-4BrCClFINPSSi-R_N-Sp-5R!H-4BrCClFINPSSi
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-3C-R
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-3C-R_Ext-3C-R
                                                        L15: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-3C-R_Ext-3C-R_Ext-6R!H-R
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_Ext-4BrCClFINPSSi-R
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->O
                                                        L15: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_6R!H->O_Ext-5R!H-R
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_Ext-5R!H-R_N-6R!H->O
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->C
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->C
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-3C-R
                                                        L15: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-3C-R_Ext-5O-R
                                                            L16: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-3C-R_Ext-5O-R_7R!H->C
                                                            L16: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-3C-R_Ext-5O-R_N-7R!H->C
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-5O-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R
                                                        L15: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-5O-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R_4BrCClFINPSSi-inRing
                                                        L15: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_5R!H->O_Ext-5O-R_Ext-6R!H-R_Ext-4BrCClFINPSSi-R_N-4BrCClFINPSSi-inRing
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi
                                                        L15: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_Sp-5C-4BrCClFINPSSi_Ext-3C-R
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_3R!H->C_N-1R->C_Ext-3C-R_N-4R!H->O_N-3C-inRing_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-5R!H->O_N-Sp-5C-4BrCClFINPSSi
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_N-3R!H->C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_N-3R!H->C_1R-inRing
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-2O-R_N-3R!H->C_N-1R-inRing
                L5: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-3R!H-R
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H->C_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H->C_Ext-3R!H-R_5R!H->C
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H->C_Ext-3R!H-R_N-5R!H->C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H->C
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_Ext-4R!H-R
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_Ext-1R-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_Ext-1R-R_4R!H->C
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_Ext-1R-R_N-4R!H->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_4R!H->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Sp-4R!H=3R!H_N-4R!H->C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_2R!H->O_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_N-Sp-4R!H=3R!H
            L4: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O
                L5: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_4R!H->O
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_4R!H->O_1R->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_4R!H->O_1R->C_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_4R!H->O_N-1R->C
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_6R!H->C
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_N-6R!H->C
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_N-6R!H->C_1R->C
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_N-6R!H->C_1R->C_1C-inRing
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_N-6R!H->C_1R->C_N-1C-inRing
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_Ext-5O-R_N-6R!H->C_N-1R->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_1R-inRing
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->O_N-1R-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Ext-4C-R
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Ext-4C-R_Ext-6R!H-R
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Sp-5BrCClFINPSSi-4C
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Sp-5BrCClFINPSSi-4C_Ext-3C-R
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Sp-5BrCClFINPSSi-4C_Ext-2C-R
                                                        L15: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Sp-5BrCClFINPSSi-4C_Ext-2C-R_Ext-6R!H-R
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_Sp-5BrCClFINPSSi-4C_Ext-5BrCClFINPSSi-R
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-1C-R_N-Sp-5BrCClFINPSSi-4C
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_6R!H->C
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_6R!H->C_1C-inRing
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_6R!H->C_N-1C-inRing
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_6R!H->C_N-1C-inRing_Sp-6C-5BrCClFINPSSi
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_6R!H->C_N-1C-inRing_N-Sp-6C-5BrCClFINPSSi
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_1R->C_Ext-5BrCClFINPSSi-R_N-6R!H->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->O_N-1R->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_Ext-1R-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_Ext-1R-R_1R-inRing
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_Ext-1R-R_N-1R-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_1R->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_N-1R->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_N-1R->C_Ext-2C-R
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_N-1R->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_N-1R->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_4R!H->O_N-1R->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-1R-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-4C-R
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-4C-R_Ext-2C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_1R->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-1R->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-2C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-2C-R_Ext-4C-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_1R->C
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_1R->C_4C-inRing
                                                L13: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_1R->C_N-4C-inRing
                                                    L14: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_1R->C_N-4C-inRing_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R
                                                        L15: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_1R->C_N-4C-inRing_Ext-5C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Int-10R!H-8R!H_Int-10R!H-9R!H_Int-10R!H-9R!H_Ext-9R!H-R
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_Sp-4C-3C_N-1R->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_5R!H->C_N-Sp-4C-3C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->C_1R->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R_N-3C-inRing_N-4R!H->O_Ext-4C-R_N-5R!H->C_N-1R->C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_1R-inRing
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_1R-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_1R-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_1R->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_1R->C_Ext-1C-R_Ext-1C-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_N-1R->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_N-1R->C_Ext-4C-R_Ext-4C-R
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_N-1R->C_Ext-4C-R_Ext-4C-R_4C-inRing
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_4R!H->C_N-1R->C_Ext-4C-R_Ext-4C-R_N-4C-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_N-4R!H->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-1R-R
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-4R!H-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-4R!H-R_Sp-5R!H-4R!H
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_3R!H->C_N-1R-inRing_Ext-1R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_1C-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->C_Ext-4R!H-R_Ext-1C-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_N-5R!H->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-1C-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-2C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-2C-R_Ext-4R!H-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->O
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->O_4R!H-inRing
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_5R!H->O_N-4R!H-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-5R!H->O
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R_4R!H->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R_N-4R!H->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->O
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_1R->C_N-1C-inRing_Ext-2C-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->O
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C_N-1R->C
                L5: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-2C-R_Ext-2C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-2C-R_Ext-2C-R_Ext-3O-R_Ext-8R!H-R_Ext-9R!H-R
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-2C-R_Ext-2C-R_Ext-3O-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_11R!H->O
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-2C-R_Ext-2C-R_Ext-3O-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_N-11R!H->O
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-5R!H-R_4R!H-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-5R!H-R_N-4R!H-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-5R!H-R_N-4R!H-inRing_1R-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_3R!H->O_Ext-5R!H-R_N-4R!H-inRing_N-1R-inRing
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_N-3R!H->O
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_N-3R!H->O_1R-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_N-3R!H->O_N-1R-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_N-3R!H->O_N-1R-inRing_Ext-2C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_Ext-1R-R_N-3R!H->O_N-1R-inRing_Ext-2C-R_Ext-6R!H-R_Ext-6R!H-R
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R_1R-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R_N-1R-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R_N-1R-inRing_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-10R!H-9R!H
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R_N-1R-inRing_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-10R!H-9R!H
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_Ext-4R!H-R_Ext-2C-R_N-1R-inRing_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-10R!H-9R!H_Ext-10R!H-R_Ext-10R!H-R
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_1R-inRing
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_3R!H->O_N-1R-inRing
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R_1R-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R_1R-inRing_Ext-5R!H-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R_1R-inRing_Ext-5R!H-R_3C-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R_1R-inRing_Ext-5R!H-R_N-3C-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_Ext-2C-R_N-1R-inRing
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_1R-inRing
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-1R-R_N-3R!H->O_N-1R-inRing
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C_1R->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C_1R->C_3R!H->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C_1R->C_N-3R!H->C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Ext-3R!H-R_Int-4R!H-2C_N-1R->C
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_Ext-2C-R_Ext-4R!H-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_Ext-2C-R_Ext-4R!H-R_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_4R!H->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_4R!H->C_Ext-3R!H-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_2C-inRing_Ext-3R!H-R_N-4R!H->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C_Ext-3R!H-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C_Ext-4C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C_Ext-3R!H-R_4R!H->C_Ext-2C-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_Sp-3R!H-2C_Ext-3R!H-R_N-4R!H->C
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_1R->C_N-2C-inRing_N-Sp-3R!H-2C
                        L7: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-2C-R_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_4R!H->C_Ext-4C-R_Ext-5R!H-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_Sp-4R!H=3R!H_N-4R!H->C
                            L8: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-4R!H-R_Int-5R!H-2C
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_2C-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_N-2C-inRing
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_N-2C-inRing_Ext-4R!H-R_Int-5R!H-3R!H
                                            L12: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_3R!H-inRing_N-2C-inRing_Ext-4R!H-R_Int-5R!H-3R!H_Ext-4R!H-R
                                L9: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-5R!H-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-3R!H-R
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Sp-5R!H-4R!H
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2C-R
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Sp-5R!H-4R!H_4R!H->C
                                        L11: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_Sp-5R!H-4R!H_N-4R!H->C
                                    L10: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_Sp-2C-1R_N-1R->C_Ext-3R!H-R_N-Sp-4R!H=3R!H_N-3R!H-inRing_Ext-4R!H-R_N-Sp-5R!H-4R!H
                    L6: RJ1_Ext-1R-R_N-Sp-2R!H=1R_N-2R!H->O_Ext-2C-R_N-Sp-3R!H=2C_N-Sp-2C-1R
"""
)

