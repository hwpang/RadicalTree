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
Derived using the following species:
[CH2]C=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCC=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C1COOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)C(=O)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=CC1[CH]OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C=CCCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(O)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=[C]C=C=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C(O)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)COC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(CO)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(CO[O])CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(C)OOC1C=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
O=C1CO[CH]CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](C=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1=CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])OC=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)(OO)C1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(COCOO)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[CH2]C(=C=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]C12OC1(O)O2 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1C=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCCO[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1[CH]CCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C(C)CC(=C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C(C)CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]CC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=C1CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CCOO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]1OC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]C - Radical thermo from pang.py and closed shell thermo from dong_pio_liang.py
[O]C1=COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]1CCC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
C=C=[C]C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=CC1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C)(COOCC(=O)O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(O)[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=CC[C](C)C(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from johnson_g4.py
C=C(C=O)C(C)(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1C=C([O])OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C)(C)[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC=C(O)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCC1=CC=C[CH]C1 - Radical thermo from pang.py and closed shell thermo from pang.py
O=C(OO)[C]1CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CC2C3C=CC(C3)C12 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C(=O)OC(C)C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1COOC1(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)CC1[CH]C(C)=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
COOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]C#CC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OCC1CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1(C)CC(OO)C(=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](OC(C)=O)C(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]1C=CCC1C1C=CC=CC1 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](C=O)C1(C)OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]COOCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=C=CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1C=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C1CO[CH]OC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C#CC(=CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1[CH]OC(O)C1=C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C([O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(C=O)OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCN(OC1=C[CH]CC=C1)CC - Radical thermo from pang.py and closed shell thermo from GAV
CC[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC(C)(C)CO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1C=CC(O[O])C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1[CH]CO1 - Radical thermo from johnson_g4.py and closed shell thermo from dong_pio_liang.py
C=C(C)COC1C=C[C](C)CC1OO - Radical thermo from pang.py and closed shell thermo from GAV
C=C(COO)C(C)(C)OOC(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]1CCOOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1=CCC=C[CH]1 - Radical thermo from pang.py and closed shell thermo from pang.py
[O]CC1(O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC1([CH]C=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C=O)=CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]C(CC)OOC1C=CCC(C)=C1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C([O])C1(OO)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]COC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(C)=CCC(=O)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(OO)C(O)=C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH]=C=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(COO)=C(C)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC(=O)[CH]C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([O])C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)C(C)(C)[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COOC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C)OOCC1(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=[C]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC#CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[C](C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C[C]1COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C=O)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(C)(C)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[C]1OC(O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
OOC[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CCCC([O])=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)[CH]CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OC(C)=C(C)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[CH]CC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=C1CC(C)(O[O])CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=CC([O])O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C=C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1C=C(O)C(O)=C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C1[CH]C=CC1O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC=CCCC1=CCC(C)[CH]C1 - Radical thermo from pang.py and closed shell thermo from GAV
[O]OCC(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]1C=CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1(C[O])COCC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C#CCC[C]=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC[CH]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C([O])OC(=CC)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)[CH]C(=C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C(OO)OC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
OCC1(O)[CH]O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]1COOCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=[C]COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=CC(O)=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C=C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C=CC1OCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=C1CC1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]OC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC=CCC1=C[CH]C=C(CC=CC)C1 - Radical thermo from pang.py and closed shell thermo from GAV
O=C[CH]CC=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC[CH]C(CC)OOC1C=CC(C2C=CCC=C2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C[C](C)C(C)(C)CC(=O)C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](COO)COC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)C1CC(C)([O])OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C]1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]OCCCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=C[CH]CC - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C1(O)OC(=O)O1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C(C)C(C)(CC)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CO[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([C]=O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(O)COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1=[C]CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C1OOC[C]1COO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC(O)(O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
OOC[C]1CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1=CCOO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C1=CC2[C](C1)C1C=CC2C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C[C](C)C(C)(C)OOC(C)(C)C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[C]1OCCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(C=O)O[O] - Radical thermo from johnson_g4.py and closed shell thermo from GAV
C=C[CH]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC[C](C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1[CH]COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1[CH]C=CCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
O=C=C1[CH]C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(CC=CC)CCC=CCCC=CC - Radical thermo from pang.py and closed shell thermo from GAV
C=C(O)C(C)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=[C]C1OO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C([CH]O)C(C)(C)O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)CC1(O[O])COOC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=CC(O)C=CC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C=C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C1C[CH]CCO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]1C=CC2CC2C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(CC)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[C]1C(=O)OC=C1C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=[C]C1=CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OC(OO)C([O])=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]OCC(C)OO - Radical thermo from johnson_g4.py and closed shell thermo from johnson_g4.py
[CH2]C=CCC1C=CCCC1 - Radical thermo from pang.py and closed shell thermo from pang.py
C=C(C)C(=O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(C)=C(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]=CCC#C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1CCOC(=O)C1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1OOCC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1[CH]C=CC2CC12 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C[C](C)C(CO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
COC=[C]C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC([O])COO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C(=O)C(=O)O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=[C]C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(OO)[C](O)C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]OC1(C(=O)O)CC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[C]#CCO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC1[CH]C(=O)OC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C[C](CC=CC)CC(C)C=C - Radical thermo from pang.py and closed shell thermo from pang.py
CC(=O)OC1OC1(C)C[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=CCC1C=CCC1C1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from pang.py
C[CH]CCOC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
O=C[CH]C=CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]1C=CCC1OOC1C=CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
[CH2]C1(C)COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH2]C1OOC(O)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)OCC=CCO[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1=CCCC1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O[CH]C(CCOO)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(CO)OO[CH]C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]1C=CC(C2=CC=CCC2)C1 - Radical thermo from pang.py and closed shell thermo from GAV
C[CH]C(C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[O]CCC=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CCC[CH]OC(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)O[C]=C(C)CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C=C=CCC - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
C=C1CO[C](C)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]O - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
CC(=O)OC[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C1(COC(C)=O)CO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C=CC(C)OOC1[CH]CCC=C1 - Radical thermo from pang.py and closed shell thermo from GAV
CC=C1[C]=COO1 - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=O)OCC(=C)C - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[CH]=C1OOC(C)C1=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C(=C=O)C(C)(C)OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(C[O])CO - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
[O]C(=CO)C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC1(C)OOCC1(COO)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CCC(O)O[O] - Radical thermo from dong_pio_liang.py and closed shell thermo from dong_pio_liang.py
C[CH]C(O)=CO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH2]C#CC=C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
[CH]1CCC=CCC1CC1=CC=CCC1 - Radical thermo from pang.py and closed shell thermo from GAV
C=CC(O[O])C(C)=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
O=C[C]1CC(O)=CC1OO - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
CC(=O)C(C)([O])C=O - Radical thermo from dong_pio_liang.py and closed shell thermo from GAV
""",
)

tree(
"""
L1: Root
    L2: RJ1
"""
)

