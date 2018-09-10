# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Coal_Foreign_Imports = Worksheet('Coal_Foreign_Imports', 10, 10)



@register(Coal_Foreign_Imports)
class A1():
    # 'Coal_Foreign_Imports'!A1
    value = "Year"

@register(Coal_Foreign_Imports)
class B1():
    # 'Coal_Foreign_Imports'!B1
    value = "Total Coal Imports (tons)"

@register(Coal_Foreign_Imports)
class C1():
    # 'Coal_Foreign_Imports'!C1
    value = "Total Revenue"

@register(Coal_Foreign_Imports)
class D1():
    # 'Coal_Foreign_Imports'!D1
    value = "price per ton"

@register(Coal_Foreign_Imports)
class A2():
    # 'Coal_Foreign_Imports'!A2
    value = 2002
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A2,"")'''
    @eval_fn
    def A2():
        a2_1 = Input_EIA_Imports_Coal_Foreign.A2()
        var_1 = IFERROR(a2_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B2():
    # 'Coal_Foreign_Imports'!B2
    value = 119940
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K2,"")'''
    @eval_fn
    def B2():
        k2_1 = Input_EIA_Imports_Coal_Foreign.K2()
        var_1 = IFERROR(k2_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C2():
    # 'Coal_Foreign_Imports'!C2
    value = 5833497
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L2,"")'''
    @eval_fn
    def C2():
        l2_1 = Input_EIA_Imports_Coal_Foreign.L2()
        var_1 = IFERROR(l2_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D2():
    # 'Coal_Foreign_Imports'!D2
    value = 48.6367933967
    formula = '''=IFERROR(C2/B2,"")'''
    @eval_fn
    def D2():
        c2_1 = Coal_Foreign_Imports.C2()
        b2_1 = Coal_Foreign_Imports.B2()
        var_1 = divide(c2_1, b2_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A3():
    # 'Coal_Foreign_Imports'!A3
    value = 2002
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A3,"")'''
    @eval_fn
    def A3():
        a3_1 = Input_EIA_Imports_Coal_Foreign.A3()
        var_1 = IFERROR(a3_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B3():
    # 'Coal_Foreign_Imports'!B3
    value = 51305
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K3,"")'''
    @eval_fn
    def B3():
        k3_1 = Input_EIA_Imports_Coal_Foreign.K3()
        var_1 = IFERROR(k3_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C3():
    # 'Coal_Foreign_Imports'!C3
    value = 1603689
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L3,"")'''
    @eval_fn
    def C3():
        l3_1 = Input_EIA_Imports_Coal_Foreign.L3()
        var_1 = IFERROR(l3_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D3():
    # 'Coal_Foreign_Imports'!D3
    value = 31.2579475685
    formula = '''=IFERROR(C3/B3,"")'''
    @eval_fn
    def D3():
        c3_1 = Coal_Foreign_Imports.C3()
        b3_1 = Coal_Foreign_Imports.B3()
        var_1 = divide(c3_1, b3_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A4():
    # 'Coal_Foreign_Imports'!A4
    value = 2002
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A4,"")'''
    @eval_fn
    def A4():
        a4_1 = Input_EIA_Imports_Coal_Foreign.A4()
        var_1 = IFERROR(a4_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B4():
    # 'Coal_Foreign_Imports'!B4
    value = 115358
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K4,"")'''
    @eval_fn
    def B4():
        k4_1 = Input_EIA_Imports_Coal_Foreign.K4()
        var_1 = IFERROR(k4_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C4():
    # 'Coal_Foreign_Imports'!C4
    value = 5631204
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L4,"")'''
    @eval_fn
    def C4():
        l4_1 = Input_EIA_Imports_Coal_Foreign.L4()
        var_1 = IFERROR(l4_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D4():
    # 'Coal_Foreign_Imports'!D4
    value = 48.8150279998
    formula = '''=IFERROR(C4/B4,"")'''
    @eval_fn
    def D4():
        c4_1 = Coal_Foreign_Imports.C4()
        b4_1 = Coal_Foreign_Imports.B4()
        var_1 = divide(c4_1, b4_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A5():
    # 'Coal_Foreign_Imports'!A5
    value = 2002
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A5,"")'''
    @eval_fn
    def A5():
        a5_1 = Input_EIA_Imports_Coal_Foreign.A5()
        var_1 = IFERROR(a5_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B5():
    # 'Coal_Foreign_Imports'!B5
    value = 27822
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K5,"")'''
    @eval_fn
    def B5():
        k5_1 = Input_EIA_Imports_Coal_Foreign.K5()
        var_1 = IFERROR(k5_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C5():
    # 'Coal_Foreign_Imports'!C5
    value = 858487
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L5,"")'''
    @eval_fn
    def C5():
        l5_1 = Input_EIA_Imports_Coal_Foreign.L5()
        var_1 = IFERROR(l5_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D5():
    # 'Coal_Foreign_Imports'!D5
    value = 30.8564085975
    formula = '''=IFERROR(C5/B5,"")'''
    @eval_fn
    def D5():
        c5_1 = Coal_Foreign_Imports.C5()
        b5_1 = Coal_Foreign_Imports.B5()
        var_1 = divide(c5_1, b5_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A6():
    # 'Coal_Foreign_Imports'!A6
    value = 2002
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A6,"")'''
    @eval_fn
    def A6():
        a6_1 = Input_EIA_Imports_Coal_Foreign.A6()
        var_1 = IFERROR(a6_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B6():
    # 'Coal_Foreign_Imports'!B6
    value = 180609
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K6,"")'''
    @eval_fn
    def B6():
        k6_1 = Input_EIA_Imports_Coal_Foreign.K6()
        var_1 = IFERROR(k6_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C6():
    # 'Coal_Foreign_Imports'!C6
    value = 9031872
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L6,"")'''
    @eval_fn
    def C6():
        l6_1 = Input_EIA_Imports_Coal_Foreign.L6()
        var_1 = IFERROR(l6_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D6():
    # 'Coal_Foreign_Imports'!D6
    value = 50.0078733618
    formula = '''=IFERROR(C6/B6,"")'''
    @eval_fn
    def D6():
        c6_1 = Coal_Foreign_Imports.C6()
        b6_1 = Coal_Foreign_Imports.B6()
        var_1 = divide(c6_1, b6_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A7():
    # 'Coal_Foreign_Imports'!A7
    value = 2002
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A7,"")'''
    @eval_fn
    def A7():
        a7_1 = Input_EIA_Imports_Coal_Foreign.A7()
        var_1 = IFERROR(a7_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B7():
    # 'Coal_Foreign_Imports'!B7
    value = 32995
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K7,"")'''
    @eval_fn
    def B7():
        k7_1 = Input_EIA_Imports_Coal_Foreign.K7()
        var_1 = IFERROR(k7_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C7():
    # 'Coal_Foreign_Imports'!C7
    value = 1053396
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L7,"")'''
    @eval_fn
    def C7():
        l7_1 = Input_EIA_Imports_Coal_Foreign.L7()
        var_1 = IFERROR(l7_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D7():
    # 'Coal_Foreign_Imports'!D7
    value = 31.9259281709
    formula = '''=IFERROR(C7/B7,"")'''
    @eval_fn
    def D7():
        c7_1 = Coal_Foreign_Imports.C7()
        b7_1 = Coal_Foreign_Imports.B7()
        var_1 = divide(c7_1, b7_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A8():
    # 'Coal_Foreign_Imports'!A8
    value = 2002
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A8,"")'''
    @eval_fn
    def A8():
        a8_1 = Input_EIA_Imports_Coal_Foreign.A8()
        var_1 = IFERROR(a8_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B8():
    # 'Coal_Foreign_Imports'!B8
    value = 58473
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K8,"")'''
    @eval_fn
    def B8():
        k8_1 = Input_EIA_Imports_Coal_Foreign.K8()
        var_1 = IFERROR(k8_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C8():
    # 'Coal_Foreign_Imports'!C8
    value = 2977213
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L8,"")'''
    @eval_fn
    def C8():
        l8_1 = Input_EIA_Imports_Coal_Foreign.L8()
        var_1 = IFERROR(l8_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D8():
    # 'Coal_Foreign_Imports'!D8
    value = 50.9160296205
    formula = '''=IFERROR(C8/B8,"")'''
    @eval_fn
    def D8():
        c8_1 = Coal_Foreign_Imports.C8()
        b8_1 = Coal_Foreign_Imports.B8()
        var_1 = divide(c8_1, b8_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A9():
    # 'Coal_Foreign_Imports'!A9
    value = 2003
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A9,"")'''
    @eval_fn
    def A9():
        a9_1 = Input_EIA_Imports_Coal_Foreign.A9()
        var_1 = IFERROR(a9_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B9():
    # 'Coal_Foreign_Imports'!B9
    value = 39683
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K9,"")'''
    @eval_fn
    def B9():
        k9_1 = Input_EIA_Imports_Coal_Foreign.K9()
        var_1 = IFERROR(k9_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C9():
    # 'Coal_Foreign_Imports'!C9
    value = 1184335
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L9,"")'''
    @eval_fn
    def C9():
        l9_1 = Input_EIA_Imports_Coal_Foreign.L9()
        var_1 = IFERROR(l9_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D9():
    # 'Coal_Foreign_Imports'!D9
    value = 29.8448957992
    formula = '''=IFERROR(C9/B9,"")'''
    @eval_fn
    def D9():
        c9_1 = Coal_Foreign_Imports.C9()
        b9_1 = Coal_Foreign_Imports.B9()
        var_1 = divide(c9_1, b9_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A10():
    # 'Coal_Foreign_Imports'!A10
    value = 2003
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A10,"")'''
    @eval_fn
    def A10():
        a10_1 = Input_EIA_Imports_Coal_Foreign.A10()
        var_1 = IFERROR(a10_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B10():
    # 'Coal_Foreign_Imports'!B10
    value = 178834
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K10,"")'''
    @eval_fn
    def B10():
        k10_1 = Input_EIA_Imports_Coal_Foreign.K10()
        var_1 = IFERROR(k10_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C10():
    # 'Coal_Foreign_Imports'!C10
    value = 8990546
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L10,"")'''
    @eval_fn
    def C10():
        l10_1 = Input_EIA_Imports_Coal_Foreign.L10()
        var_1 = IFERROR(l10_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D10():
    # 'Coal_Foreign_Imports'!D10
    value = 50.2731359809
    formula = '''=IFERROR(C10/B10,"")'''
    @eval_fn
    def D10():
        c10_1 = Coal_Foreign_Imports.C10()
        b10_1 = Coal_Foreign_Imports.B10()
        var_1 = divide(c10_1, b10_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A11():
    # 'Coal_Foreign_Imports'!A11
    value = 2003
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A11,"")'''
    @eval_fn
    def A11():
        a11_1 = Input_EIA_Imports_Coal_Foreign.A11()
        var_1 = IFERROR(a11_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B11():
    # 'Coal_Foreign_Imports'!B11
    value = 20170
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K11,"")'''
    @eval_fn
    def B11():
        k11_1 = Input_EIA_Imports_Coal_Foreign.K11()
        var_1 = IFERROR(k11_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C11():
    # 'Coal_Foreign_Imports'!C11
    value = 606912
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L11,"")'''
    @eval_fn
    def C11():
        l11_1 = Input_EIA_Imports_Coal_Foreign.L11()
        var_1 = IFERROR(l11_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D11():
    # 'Coal_Foreign_Imports'!D11
    value = 30.0898363907
    formula = '''=IFERROR(C11/B11,"")'''
    @eval_fn
    def D11():
        c11_1 = Coal_Foreign_Imports.C11()
        b11_1 = Coal_Foreign_Imports.B11()
        var_1 = divide(c11_1, b11_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A12():
    # 'Coal_Foreign_Imports'!A12
    value = 2003
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A12,"")'''
    @eval_fn
    def A12():
        a12_1 = Input_EIA_Imports_Coal_Foreign.A12()
        var_1 = IFERROR(a12_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B12():
    # 'Coal_Foreign_Imports'!B12
    value = 179549
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K12,"")'''
    @eval_fn
    def B12():
        k12_1 = Input_EIA_Imports_Coal_Foreign.K12()
        var_1 = IFERROR(k12_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C12():
    # 'Coal_Foreign_Imports'!C12
    value = 8951277
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L12,"")'''
    @eval_fn
    def C12():
        l12_1 = Input_EIA_Imports_Coal_Foreign.L12()
        var_1 = IFERROR(l12_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D12():
    # 'Coal_Foreign_Imports'!D12
    value = 49.8542292076
    formula = '''=IFERROR(C12/B12,"")'''
    @eval_fn
    def D12():
        c12_1 = Coal_Foreign_Imports.C12()
        b12_1 = Coal_Foreign_Imports.B12()
        var_1 = divide(c12_1, b12_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A13():
    # 'Coal_Foreign_Imports'!A13
    value = 2003
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A13,"")'''
    @eval_fn
    def A13():
        a13_1 = Input_EIA_Imports_Coal_Foreign.A13()
        var_1 = IFERROR(a13_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B13():
    # 'Coal_Foreign_Imports'!B13
    value = 27448
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K13,"")'''
    @eval_fn
    def B13():
        k13_1 = Input_EIA_Imports_Coal_Foreign.K13()
        var_1 = IFERROR(k13_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C13():
    # 'Coal_Foreign_Imports'!C13
    value = 853764
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L13,"")'''
    @eval_fn
    def C13():
        l13_1 = Input_EIA_Imports_Coal_Foreign.L13()
        var_1 = IFERROR(l13_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D13():
    # 'Coal_Foreign_Imports'!D13
    value = 31.1047799475
    formula = '''=IFERROR(C13/B13,"")'''
    @eval_fn
    def D13():
        c13_1 = Coal_Foreign_Imports.C13()
        b13_1 = Coal_Foreign_Imports.B13()
        var_1 = divide(c13_1, b13_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A14():
    # 'Coal_Foreign_Imports'!A14
    value = 2003
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A14,"")'''
    @eval_fn
    def A14():
        a14_1 = Input_EIA_Imports_Coal_Foreign.A14()
        var_1 = IFERROR(a14_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B14():
    # 'Coal_Foreign_Imports'!B14
    value = 177342
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K14,"")'''
    @eval_fn
    def B14():
        k14_1 = Input_EIA_Imports_Coal_Foreign.K14()
        var_1 = IFERROR(k14_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C14():
    # 'Coal_Foreign_Imports'!C14
    value = 7292900
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L14,"")'''
    @eval_fn
    def C14():
        l14_1 = Input_EIA_Imports_Coal_Foreign.L14()
        var_1 = IFERROR(l14_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D14():
    # 'Coal_Foreign_Imports'!D14
    value = 41.1233661513
    formula = '''=IFERROR(C14/B14,"")'''
    @eval_fn
    def D14():
        c14_1 = Coal_Foreign_Imports.C14()
        b14_1 = Coal_Foreign_Imports.B14()
        var_1 = divide(c14_1, b14_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A15():
    # 'Coal_Foreign_Imports'!A15
    value = 2003
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A15,"")'''
    @eval_fn
    def A15():
        a15_1 = Input_EIA_Imports_Coal_Foreign.A15()
        var_1 = IFERROR(a15_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B15():
    # 'Coal_Foreign_Imports'!B15
    value = 23082
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K15,"")'''
    @eval_fn
    def B15():
        k15_1 = Input_EIA_Imports_Coal_Foreign.K15()
        var_1 = IFERROR(k15_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C15():
    # 'Coal_Foreign_Imports'!C15
    value = 701131
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L15,"")'''
    @eval_fn
    def C15():
        l15_1 = Input_EIA_Imports_Coal_Foreign.L15()
        var_1 = IFERROR(l15_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D15():
    # 'Coal_Foreign_Imports'!D15
    value = 30.375660688
    formula = '''=IFERROR(C15/B15,"")'''
    @eval_fn
    def D15():
        c15_1 = Coal_Foreign_Imports.C15()
        b15_1 = Coal_Foreign_Imports.B15()
        var_1 = divide(c15_1, b15_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A16():
    # 'Coal_Foreign_Imports'!A16
    value = 2003
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A16,"")'''
    @eval_fn
    def A16():
        a16_1 = Input_EIA_Imports_Coal_Foreign.A16()
        var_1 = IFERROR(a16_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B16():
    # 'Coal_Foreign_Imports'!B16
    value = 179209
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K16,"")'''
    @eval_fn
    def B16():
        k16_1 = Input_EIA_Imports_Coal_Foreign.K16()
        var_1 = IFERROR(k16_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C16():
    # 'Coal_Foreign_Imports'!C16
    value = 3699339
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L16,"")'''
    @eval_fn
    def C16():
        l16_1 = Input_EIA_Imports_Coal_Foreign.L16()
        var_1 = IFERROR(l16_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D16():
    # 'Coal_Foreign_Imports'!D16
    value = 20.642596075
    formula = '''=IFERROR(C16/B16,"")'''
    @eval_fn
    def D16():
        c16_1 = Coal_Foreign_Imports.C16()
        b16_1 = Coal_Foreign_Imports.B16()
        var_1 = divide(c16_1, b16_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A17():
    # 'Coal_Foreign_Imports'!A17
    value = 2004
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A17,"")'''
    @eval_fn
    def A17():
        a17_1 = Input_EIA_Imports_Coal_Foreign.A17()
        var_1 = IFERROR(a17_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B17():
    # 'Coal_Foreign_Imports'!B17
    value = 32990
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K17,"")'''
    @eval_fn
    def B17():
        k17_1 = Input_EIA_Imports_Coal_Foreign.K17()
        var_1 = IFERROR(k17_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C17():
    # 'Coal_Foreign_Imports'!C17
    value = 1029793
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L17,"")'''
    @eval_fn
    def C17():
        l17_1 = Input_EIA_Imports_Coal_Foreign.L17()
        var_1 = IFERROR(l17_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D17():
    # 'Coal_Foreign_Imports'!D17
    value = 31.215307669
    formula = '''=IFERROR(C17/B17,"")'''
    @eval_fn
    def D17():
        c17_1 = Coal_Foreign_Imports.C17()
        b17_1 = Coal_Foreign_Imports.B17()
        var_1 = divide(c17_1, b17_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A18():
    # 'Coal_Foreign_Imports'!A18
    value = 2004
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A18,"")'''
    @eval_fn
    def A18():
        a18_1 = Input_EIA_Imports_Coal_Foreign.A18()
        var_1 = IFERROR(a18_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B18():
    # 'Coal_Foreign_Imports'!B18
    value = 176064
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K18,"")'''
    @eval_fn
    def B18():
        k18_1 = Input_EIA_Imports_Coal_Foreign.K18()
        var_1 = IFERROR(k18_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C18():
    # 'Coal_Foreign_Imports'!C18
    value = 3588792
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L18,"")'''
    @eval_fn
    def C18():
        l18_1 = Input_EIA_Imports_Coal_Foreign.L18()
        var_1 = IFERROR(l18_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D18():
    # 'Coal_Foreign_Imports'!D18
    value = 20.3834514722
    formula = '''=IFERROR(C18/B18,"")'''
    @eval_fn
    def D18():
        c18_1 = Coal_Foreign_Imports.C18()
        b18_1 = Coal_Foreign_Imports.B18()
        var_1 = divide(c18_1, b18_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A19():
    # 'Coal_Foreign_Imports'!A19
    value = 2004
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A19,"")'''
    @eval_fn
    def A19():
        a19_1 = Input_EIA_Imports_Coal_Foreign.A19()
        var_1 = IFERROR(a19_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B19():
    # 'Coal_Foreign_Imports'!B19
    value = 33841
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K19,"")'''
    @eval_fn
    def B19():
        k19_1 = Input_EIA_Imports_Coal_Foreign.K19()
        var_1 = IFERROR(k19_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C19():
    # 'Coal_Foreign_Imports'!C19
    value = 1074295
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L19,"")'''
    @eval_fn
    def C19():
        l19_1 = Input_EIA_Imports_Coal_Foreign.L19()
        var_1 = IFERROR(l19_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D19():
    # 'Coal_Foreign_Imports'!D19
    value = 31.7453680447
    formula = '''=IFERROR(C19/B19,"")'''
    @eval_fn
    def D19():
        c19_1 = Coal_Foreign_Imports.C19()
        b19_1 = Coal_Foreign_Imports.B19()
        var_1 = divide(c19_1, b19_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A20():
    # 'Coal_Foreign_Imports'!A20
    value = 2004
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A20,"")'''
    @eval_fn
    def A20():
        a20_1 = Input_EIA_Imports_Coal_Foreign.A20()
        var_1 = IFERROR(a20_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B20():
    # 'Coal_Foreign_Imports'!B20
    value = 122116
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K20,"")'''
    @eval_fn
    def B20():
        k20_1 = Input_EIA_Imports_Coal_Foreign.K20()
        var_1 = IFERROR(k20_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C20():
    # 'Coal_Foreign_Imports'!C20
    value = 2318274
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L20,"")'''
    @eval_fn
    def C20():
        l20_1 = Input_EIA_Imports_Coal_Foreign.L20()
        var_1 = IFERROR(l20_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D20():
    # 'Coal_Foreign_Imports'!D20
    value = 18.9841953552
    formula = '''=IFERROR(C20/B20,"")'''
    @eval_fn
    def D20():
        c20_1 = Coal_Foreign_Imports.C20()
        b20_1 = Coal_Foreign_Imports.B20()
        var_1 = divide(c20_1, b20_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A21():
    # 'Coal_Foreign_Imports'!A21
    value = 2004
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A21,"")'''
    @eval_fn
    def A21():
        a21_1 = Input_EIA_Imports_Coal_Foreign.A21()
        var_1 = IFERROR(a21_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B21():
    # 'Coal_Foreign_Imports'!B21
    value = 27784
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K21,"")'''
    @eval_fn
    def B21():
        k21_1 = Input_EIA_Imports_Coal_Foreign.K21()
        var_1 = IFERROR(k21_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C21():
    # 'Coal_Foreign_Imports'!C21
    value = 864222
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L21,"")'''
    @eval_fn
    def C21():
        l21_1 = Input_EIA_Imports_Coal_Foreign.L21()
        var_1 = IFERROR(l21_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D21():
    # 'Coal_Foreign_Imports'!D21
    value = 31.1050244745
    formula = '''=IFERROR(C21/B21,"")'''
    @eval_fn
    def D21():
        c21_1 = Coal_Foreign_Imports.C21()
        b21_1 = Coal_Foreign_Imports.B21()
        var_1 = divide(c21_1, b21_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A22():
    # 'Coal_Foreign_Imports'!A22
    value = 2004
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A22,"")'''
    @eval_fn
    def A22():
        a22_1 = Input_EIA_Imports_Coal_Foreign.A22()
        var_1 = IFERROR(a22_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B22():
    # 'Coal_Foreign_Imports'!B22
    value = 237538
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K22,"")'''
    @eval_fn
    def B22():
        k22_1 = Input_EIA_Imports_Coal_Foreign.K22()
        var_1 = IFERROR(k22_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C22():
    # 'Coal_Foreign_Imports'!C22
    value = 4575647
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L22,"")'''
    @eval_fn
    def C22():
        l22_1 = Input_EIA_Imports_Coal_Foreign.L22()
        var_1 = IFERROR(l22_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D22():
    # 'Coal_Foreign_Imports'!D22
    value = 19.2628000573
    formula = '''=IFERROR(C22/B22,"")'''
    @eval_fn
    def D22():
        c22_1 = Coal_Foreign_Imports.C22()
        b22_1 = Coal_Foreign_Imports.B22()
        var_1 = divide(c22_1, b22_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A23():
    # 'Coal_Foreign_Imports'!A23
    value = 2004
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A23,"")'''
    @eval_fn
    def A23():
        a23_1 = Input_EIA_Imports_Coal_Foreign.A23()
        var_1 = IFERROR(a23_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B23():
    # 'Coal_Foreign_Imports'!B23
    value = 117349
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K23,"")'''
    @eval_fn
    def B23():
        k23_1 = Input_EIA_Imports_Coal_Foreign.K23()
        var_1 = IFERROR(k23_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C23():
    # 'Coal_Foreign_Imports'!C23
    value = 2186283
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L23,"")'''
    @eval_fn
    def C23():
        l23_1 = Input_EIA_Imports_Coal_Foreign.L23()
        var_1 = IFERROR(l23_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D23():
    # 'Coal_Foreign_Imports'!D23
    value = 18.6306061407
    formula = '''=IFERROR(C23/B23,"")'''
    @eval_fn
    def D23():
        c23_1 = Coal_Foreign_Imports.C23()
        b23_1 = Coal_Foreign_Imports.B23()
        var_1 = divide(c23_1, b23_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A24():
    # 'Coal_Foreign_Imports'!A24
    value = 2005
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A24,"")'''
    @eval_fn
    def A24():
        a24_1 = Input_EIA_Imports_Coal_Foreign.A24()
        var_1 = IFERROR(a24_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B24():
    # 'Coal_Foreign_Imports'!B24
    value = 19846
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K24,"")'''
    @eval_fn
    def B24():
        k24_1 = Input_EIA_Imports_Coal_Foreign.K24()
        var_1 = IFERROR(k24_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C24():
    # 'Coal_Foreign_Imports'!C24
    value = 612354
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L24,"")'''
    @eval_fn
    def C24():
        l24_1 = Input_EIA_Imports_Coal_Foreign.L24()
        var_1 = IFERROR(l24_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D24():
    # 'Coal_Foreign_Imports'!D24
    value = 30.8552856999
    formula = '''=IFERROR(C24/B24,"")'''
    @eval_fn
    def D24():
        c24_1 = Coal_Foreign_Imports.C24()
        b24_1 = Coal_Foreign_Imports.B24()
        var_1 = divide(c24_1, b24_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A25():
    # 'Coal_Foreign_Imports'!A25
    value = 2005
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A25,"")'''
    @eval_fn
    def A25():
        a25_1 = Input_EIA_Imports_Coal_Foreign.A25()
        var_1 = IFERROR(a25_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B25():
    # 'Coal_Foreign_Imports'!B25
    value = 176780
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K25,"")'''
    @eval_fn
    def B25():
        k25_1 = Input_EIA_Imports_Coal_Foreign.K25()
        var_1 = IFERROR(k25_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C25():
    # 'Coal_Foreign_Imports'!C25
    value = 3283050
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L25,"")'''
    @eval_fn
    def C25():
        l25_1 = Input_EIA_Imports_Coal_Foreign.L25()
        var_1 = IFERROR(l25_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D25():
    # 'Coal_Foreign_Imports'!D25
    value = 18.5713881661
    formula = '''=IFERROR(C25/B25,"")'''
    @eval_fn
    def D25():
        c25_1 = Coal_Foreign_Imports.C25()
        b25_1 = Coal_Foreign_Imports.B25()
        var_1 = divide(c25_1, b25_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A26():
    # 'Coal_Foreign_Imports'!A26
    value = 2005
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A26,"")'''
    @eval_fn
    def A26():
        a26_1 = Input_EIA_Imports_Coal_Foreign.A26()
        var_1 = IFERROR(a26_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B26():
    # 'Coal_Foreign_Imports'!B26
    value = 28087
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K26,"")'''
    @eval_fn
    def B26():
        k26_1 = Input_EIA_Imports_Coal_Foreign.K26()
        var_1 = IFERROR(k26_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C26():
    # 'Coal_Foreign_Imports'!C26
    value = 911013
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L26,"")'''
    @eval_fn
    def C26():
        l26_1 = Input_EIA_Imports_Coal_Foreign.L26()
        var_1 = IFERROR(l26_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D26():
    # 'Coal_Foreign_Imports'!D26
    value = 32.4353971588
    formula = '''=IFERROR(C26/B26,"")'''
    @eval_fn
    def D26():
        c26_1 = Coal_Foreign_Imports.C26()
        b26_1 = Coal_Foreign_Imports.B26()
        var_1 = divide(c26_1, b26_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A27():
    # 'Coal_Foreign_Imports'!A27
    value = 2005
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A27,"")'''
    @eval_fn
    def A27():
        a27_1 = Input_EIA_Imports_Coal_Foreign.A27()
        var_1 = IFERROR(a27_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B27():
    # 'Coal_Foreign_Imports'!B27
    value = 178000
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K27,"")'''
    @eval_fn
    def B27():
        k27_1 = Input_EIA_Imports_Coal_Foreign.K27()
        var_1 = IFERROR(k27_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C27():
    # 'Coal_Foreign_Imports'!C27
    value = 3388451
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L27,"")'''
    @eval_fn
    def C27():
        l27_1 = Input_EIA_Imports_Coal_Foreign.L27()
        var_1 = IFERROR(l27_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D27():
    # 'Coal_Foreign_Imports'!D27
    value = 19.036241573
    formula = '''=IFERROR(C27/B27,"")'''
    @eval_fn
    def D27():
        c27_1 = Coal_Foreign_Imports.C27()
        b27_1 = Coal_Foreign_Imports.B27()
        var_1 = divide(c27_1, b27_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A28():
    # 'Coal_Foreign_Imports'!A28
    value = 2005
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A28,"")'''
    @eval_fn
    def A28():
        a28_1 = Input_EIA_Imports_Coal_Foreign.A28()
        var_1 = IFERROR(a28_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B28():
    # 'Coal_Foreign_Imports'!B28
    value = 179978
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K28,"")'''
    @eval_fn
    def B28():
        k28_1 = Input_EIA_Imports_Coal_Foreign.K28()
        var_1 = IFERROR(k28_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C28():
    # 'Coal_Foreign_Imports'!C28
    value = 3481699
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L28,"")'''
    @eval_fn
    def C28():
        l28_1 = Input_EIA_Imports_Coal_Foreign.L28()
        var_1 = IFERROR(l28_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D28():
    # 'Coal_Foreign_Imports'!D28
    value = 19.3451366278
    formula = '''=IFERROR(C28/B28,"")'''
    @eval_fn
    def D28():
        c28_1 = Coal_Foreign_Imports.C28()
        b28_1 = Coal_Foreign_Imports.B28()
        var_1 = divide(c28_1, b28_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A29():
    # 'Coal_Foreign_Imports'!A29
    value = 2005
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A29,"")'''
    @eval_fn
    def A29():
        a29_1 = Input_EIA_Imports_Coal_Foreign.A29()
        var_1 = IFERROR(a29_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B29():
    # 'Coal_Foreign_Imports'!B29
    value = 24744
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K29,"")'''
    @eval_fn
    def B29():
        k29_1 = Input_EIA_Imports_Coal_Foreign.K29()
        var_1 = IFERROR(k29_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C29():
    # 'Coal_Foreign_Imports'!C29
    value = 790445
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L29,"")'''
    @eval_fn
    def C29():
        l29_1 = Input_EIA_Imports_Coal_Foreign.L29()
        var_1 = IFERROR(l29_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D29():
    # 'Coal_Foreign_Imports'!D29
    value = 31.9449159392
    formula = '''=IFERROR(C29/B29,"")'''
    @eval_fn
    def D29():
        c29_1 = Coal_Foreign_Imports.C29()
        b29_1 = Coal_Foreign_Imports.B29()
        var_1 = divide(c29_1, b29_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A30():
    # 'Coal_Foreign_Imports'!A30
    value = 2005
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A30,"")'''
    @eval_fn
    def A30():
        a30_1 = Input_EIA_Imports_Coal_Foreign.A30()
        var_1 = IFERROR(a30_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B30():
    # 'Coal_Foreign_Imports'!B30
    value = 241479
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K30,"")'''
    @eval_fn
    def B30():
        k30_1 = Input_EIA_Imports_Coal_Foreign.K30()
        var_1 = IFERROR(k30_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C30():
    # 'Coal_Foreign_Imports'!C30
    value = 4670947
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L30,"")'''
    @eval_fn
    def C30():
        l30_1 = Input_EIA_Imports_Coal_Foreign.L30()
        var_1 = IFERROR(l30_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D30():
    # 'Coal_Foreign_Imports'!D30
    value = 19.3430774519
    formula = '''=IFERROR(C30/B30,"")'''
    @eval_fn
    def D30():
        c30_1 = Coal_Foreign_Imports.C30()
        b30_1 = Coal_Foreign_Imports.B30()
        var_1 = divide(c30_1, b30_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A31():
    # 'Coal_Foreign_Imports'!A31
    value = 2006
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A31,"")'''
    @eval_fn
    def A31():
        a31_1 = Input_EIA_Imports_Coal_Foreign.A31()
        var_1 = IFERROR(a31_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B31():
    # 'Coal_Foreign_Imports'!B31
    value = 19127
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K31,"")'''
    @eval_fn
    def B31():
        k31_1 = Input_EIA_Imports_Coal_Foreign.K31()
        var_1 = IFERROR(k31_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C31():
    # 'Coal_Foreign_Imports'!C31
    value = 583186
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L31,"")'''
    @eval_fn
    def C31():
        l31_1 = Input_EIA_Imports_Coal_Foreign.L31()
        var_1 = IFERROR(l31_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D31():
    # 'Coal_Foreign_Imports'!D31
    value = 30.4901971036
    formula = '''=IFERROR(C31/B31,"")'''
    @eval_fn
    def D31():
        c31_1 = Coal_Foreign_Imports.C31()
        b31_1 = Coal_Foreign_Imports.B31()
        var_1 = divide(c31_1, b31_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A32():
    # 'Coal_Foreign_Imports'!A32
    value = 2006
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A32,"")'''
    @eval_fn
    def A32():
        a32_1 = Input_EIA_Imports_Coal_Foreign.A32()
        var_1 = IFERROR(a32_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B32():
    # 'Coal_Foreign_Imports'!B32
    value = 179045
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K32,"")'''
    @eval_fn
    def B32():
        k32_1 = Input_EIA_Imports_Coal_Foreign.K32()
        var_1 = IFERROR(k32_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C32():
    # 'Coal_Foreign_Imports'!C32
    value = 3505051
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L32,"")'''
    @eval_fn
    def C32():
        l32_1 = Input_EIA_Imports_Coal_Foreign.L32()
        var_1 = IFERROR(l32_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D32():
    # 'Coal_Foreign_Imports'!D32
    value = 19.5763690692
    formula = '''=IFERROR(C32/B32,"")'''
    @eval_fn
    def D32():
        c32_1 = Coal_Foreign_Imports.C32()
        b32_1 = Coal_Foreign_Imports.B32()
        var_1 = divide(c32_1, b32_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A33():
    # 'Coal_Foreign_Imports'!A33
    value = 2006
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A33,"")'''
    @eval_fn
    def A33():
        a33_1 = Input_EIA_Imports_Coal_Foreign.A33()
        var_1 = IFERROR(a33_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B33():
    # 'Coal_Foreign_Imports'!B33
    value = 120696
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K33,"")'''
    @eval_fn
    def B33():
        k33_1 = Input_EIA_Imports_Coal_Foreign.K33()
        var_1 = IFERROR(k33_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C33():
    # 'Coal_Foreign_Imports'!C33
    value = 2377551
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L33,"")'''
    @eval_fn
    def C33():
        l33_1 = Input_EIA_Imports_Coal_Foreign.L33()
        var_1 = IFERROR(l33_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D33():
    # 'Coal_Foreign_Imports'!D33
    value = 19.6986726983
    formula = '''=IFERROR(C33/B33,"")'''
    @eval_fn
    def D33():
        c33_1 = Coal_Foreign_Imports.C33()
        b33_1 = Coal_Foreign_Imports.B33()
        var_1 = divide(c33_1, b33_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A34():
    # 'Coal_Foreign_Imports'!A34
    value = 2006
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A34,"")'''
    @eval_fn
    def A34():
        a34_1 = Input_EIA_Imports_Coal_Foreign.A34()
        var_1 = IFERROR(a34_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B34():
    # 'Coal_Foreign_Imports'!B34
    value = 26375
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K34,"")'''
    @eval_fn
    def B34():
        k34_1 = Input_EIA_Imports_Coal_Foreign.K34()
        var_1 = IFERROR(k34_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C34():
    # 'Coal_Foreign_Imports'!C34
    value = 803902
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L34,"")'''
    @eval_fn
    def C34():
        l34_1 = Input_EIA_Imports_Coal_Foreign.L34()
        var_1 = IFERROR(l34_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D34():
    # 'Coal_Foreign_Imports'!D34
    value = 30.4796966825
    formula = '''=IFERROR(C34/B34,"")'''
    @eval_fn
    def D34():
        c34_1 = Coal_Foreign_Imports.C34()
        b34_1 = Coal_Foreign_Imports.B34()
        var_1 = divide(c34_1, b34_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A35():
    # 'Coal_Foreign_Imports'!A35
    value = 2006
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A35,"")'''
    @eval_fn
    def A35():
        a35_1 = Input_EIA_Imports_Coal_Foreign.A35()
        var_1 = IFERROR(a35_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B35():
    # 'Coal_Foreign_Imports'!B35
    value = 242203
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K35,"")'''
    @eval_fn
    def B35():
        k35_1 = Input_EIA_Imports_Coal_Foreign.K35()
        var_1 = IFERROR(k35_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C35():
    # 'Coal_Foreign_Imports'!C35
    value = 4623461
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L35,"")'''
    @eval_fn
    def C35():
        l35_1 = Input_EIA_Imports_Coal_Foreign.L35()
        var_1 = IFERROR(l35_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D35():
    # 'Coal_Foreign_Imports'!D35
    value = 19.0891979042
    formula = '''=IFERROR(C35/B35,"")'''
    @eval_fn
    def D35():
        c35_1 = Coal_Foreign_Imports.C35()
        b35_1 = Coal_Foreign_Imports.B35()
        var_1 = divide(c35_1, b35_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A36():
    # 'Coal_Foreign_Imports'!A36
    value = 2006
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A36,"")'''
    @eval_fn
    def A36():
        a36_1 = Input_EIA_Imports_Coal_Foreign.A36()
        var_1 = IFERROR(a36_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B36():
    # 'Coal_Foreign_Imports'!B36
    value = 118549
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K36,"")'''
    @eval_fn
    def B36():
        k36_1 = Input_EIA_Imports_Coal_Foreign.K36()
        var_1 = IFERROR(k36_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C36():
    # 'Coal_Foreign_Imports'!C36
    value = 2252284
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L36,"")'''
    @eval_fn
    def C36():
        l36_1 = Input_EIA_Imports_Coal_Foreign.L36()
        var_1 = IFERROR(l36_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D36():
    # 'Coal_Foreign_Imports'!D36
    value = 18.9987600064
    formula = '''=IFERROR(C36/B36,"")'''
    @eval_fn
    def D36():
        c36_1 = Coal_Foreign_Imports.C36()
        b36_1 = Coal_Foreign_Imports.B36()
        var_1 = divide(c36_1, b36_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A37():
    # 'Coal_Foreign_Imports'!A37
    value = 2007
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A37,"")'''
    @eval_fn
    def A37():
        a37_1 = Input_EIA_Imports_Coal_Foreign.A37()
        var_1 = IFERROR(a37_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B37():
    # 'Coal_Foreign_Imports'!B37
    value = 27580
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K37,"")'''
    @eval_fn
    def B37():
        k37_1 = Input_EIA_Imports_Coal_Foreign.K37()
        var_1 = IFERROR(k37_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C37():
    # 'Coal_Foreign_Imports'!C37
    value = 864895
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L37,"")'''
    @eval_fn
    def C37():
        l37_1 = Input_EIA_Imports_Coal_Foreign.L37()
        var_1 = IFERROR(l37_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D37():
    # 'Coal_Foreign_Imports'!D37
    value = 31.3594996374
    formula = '''=IFERROR(C37/B37,"")'''
    @eval_fn
    def D37():
        c37_1 = Coal_Foreign_Imports.C37()
        b37_1 = Coal_Foreign_Imports.B37()
        var_1 = divide(c37_1, b37_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A38():
    # 'Coal_Foreign_Imports'!A38
    value = 2007
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A38,"")'''
    @eval_fn
    def A38():
        a38_1 = Input_EIA_Imports_Coal_Foreign.A38()
        var_1 = IFERROR(a38_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B38():
    # 'Coal_Foreign_Imports'!B38
    value = 176243
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K38,"")'''
    @eval_fn
    def B38():
        k38_1 = Input_EIA_Imports_Coal_Foreign.K38()
        var_1 = IFERROR(k38_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C38():
    # 'Coal_Foreign_Imports'!C38
    value = 3435907
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L38,"")'''
    @eval_fn
    def C38():
        l38_1 = Input_EIA_Imports_Coal_Foreign.L38()
        var_1 = IFERROR(l38_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D38():
    # 'Coal_Foreign_Imports'!D38
    value = 19.4952820821
    formula = '''=IFERROR(C38/B38,"")'''
    @eval_fn
    def D38():
        c38_1 = Coal_Foreign_Imports.C38()
        b38_1 = Coal_Foreign_Imports.B38()
        var_1 = divide(c38_1, b38_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A39():
    # 'Coal_Foreign_Imports'!A39
    value = 2007
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A39,"")'''
    @eval_fn
    def A39():
        a39_1 = Input_EIA_Imports_Coal_Foreign.A39()
        var_1 = IFERROR(a39_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B39():
    # 'Coal_Foreign_Imports'!B39
    value = 19748
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K39,"")'''
    @eval_fn
    def B39():
        k39_1 = Input_EIA_Imports_Coal_Foreign.K39()
        var_1 = IFERROR(k39_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C39():
    # 'Coal_Foreign_Imports'!C39
    value = 621263
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L39,"")'''
    @eval_fn
    def C39():
        l39_1 = Input_EIA_Imports_Coal_Foreign.L39()
        var_1 = IFERROR(l39_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D39():
    # 'Coal_Foreign_Imports'!D39
    value = 31.4595402066
    formula = '''=IFERROR(C39/B39,"")'''
    @eval_fn
    def D39():
        c39_1 = Coal_Foreign_Imports.C39()
        b39_1 = Coal_Foreign_Imports.B39()
        var_1 = divide(c39_1, b39_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A40():
    # 'Coal_Foreign_Imports'!A40
    value = 2007
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A40,"")'''
    @eval_fn
    def A40():
        a40_1 = Input_EIA_Imports_Coal_Foreign.A40()
        var_1 = IFERROR(a40_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B40():
    # 'Coal_Foreign_Imports'!B40
    value = 178075
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K40,"")'''
    @eval_fn
    def B40():
        k40_1 = Input_EIA_Imports_Coal_Foreign.K40()
        var_1 = IFERROR(k40_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C40():
    # 'Coal_Foreign_Imports'!C40
    value = 3482341
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L40,"")'''
    @eval_fn
    def C40():
        l40_1 = Input_EIA_Imports_Coal_Foreign.L40()
        var_1 = IFERROR(l40_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D40():
    # 'Coal_Foreign_Imports'!D40
    value = 19.5554738172
    formula = '''=IFERROR(C40/B40,"")'''
    @eval_fn
    def D40():
        c40_1 = Coal_Foreign_Imports.C40()
        b40_1 = Coal_Foreign_Imports.B40()
        var_1 = divide(c40_1, b40_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A41():
    # 'Coal_Foreign_Imports'!A41
    value = 2007
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A41,"")'''
    @eval_fn
    def A41():
        a41_1 = Input_EIA_Imports_Coal_Foreign.A41()
        var_1 = IFERROR(a41_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B41():
    # 'Coal_Foreign_Imports'!B41
    value = 168080
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K41,"")'''
    @eval_fn
    def B41():
        k41_1 = Input_EIA_Imports_Coal_Foreign.K41()
        var_1 = IFERROR(k41_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C41():
    # 'Coal_Foreign_Imports'!C41
    value = 3311551
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L41,"")'''
    @eval_fn
    def C41():
        l41_1 = Input_EIA_Imports_Coal_Foreign.L41()
        var_1 = IFERROR(l41_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D41():
    # 'Coal_Foreign_Imports'!D41
    value = 19.7022310804
    formula = '''=IFERROR(C41/B41,"")'''
    @eval_fn
    def D41():
        c41_1 = Coal_Foreign_Imports.C41()
        b41_1 = Coal_Foreign_Imports.B41()
        var_1 = divide(c41_1, b41_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A42():
    # 'Coal_Foreign_Imports'!A42
    value = 2007
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A42,"")'''
    @eval_fn
    def A42():
        a42_1 = Input_EIA_Imports_Coal_Foreign.A42()
        var_1 = IFERROR(a42_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B42():
    # 'Coal_Foreign_Imports'!B42
    value = 18310
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K42,"")'''
    @eval_fn
    def B42():
        k42_1 = Input_EIA_Imports_Coal_Foreign.K42()
        var_1 = IFERROR(k42_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C42():
    # 'Coal_Foreign_Imports'!C42
    value = 593986
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L42,"")'''
    @eval_fn
    def C42():
        l42_1 = Input_EIA_Imports_Coal_Foreign.L42()
        var_1 = IFERROR(l42_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D42():
    # 'Coal_Foreign_Imports'!D42
    value = 32.4405243037
    formula = '''=IFERROR(C42/B42,"")'''
    @eval_fn
    def D42():
        c42_1 = Coal_Foreign_Imports.C42()
        b42_1 = Coal_Foreign_Imports.B42()
        var_1 = divide(c42_1, b42_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A43():
    # 'Coal_Foreign_Imports'!A43
    value = 2007
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A43,"")'''
    @eval_fn
    def A43():
        a43_1 = Input_EIA_Imports_Coal_Foreign.A43()
        var_1 = IFERROR(a43_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B43():
    # 'Coal_Foreign_Imports'!B43
    value = 60572
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K43,"")'''
    @eval_fn
    def B43():
        k43_1 = Input_EIA_Imports_Coal_Foreign.K43()
        var_1 = IFERROR(k43_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C43():
    # 'Coal_Foreign_Imports'!C43
    value = 3468444
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L43,"")'''
    @eval_fn
    def C43():
        l43_1 = Input_EIA_Imports_Coal_Foreign.L43()
        var_1 = IFERROR(l43_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D43():
    # 'Coal_Foreign_Imports'!D43
    value = 57.2615069669
    formula = '''=IFERROR(C43/B43,"")'''
    @eval_fn
    def D43():
        c43_1 = Coal_Foreign_Imports.C43()
        b43_1 = Coal_Foreign_Imports.B43()
        var_1 = divide(c43_1, b43_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A44():
    # 'Coal_Foreign_Imports'!A44
    value = 2007
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A44,"")'''
    @eval_fn
    def A44():
        a44_1 = Input_EIA_Imports_Coal_Foreign.A44()
        var_1 = IFERROR(a44_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B44():
    # 'Coal_Foreign_Imports'!B44
    value = 120241
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K44,"")'''
    @eval_fn
    def B44():
        k44_1 = Input_EIA_Imports_Coal_Foreign.K44()
        var_1 = IFERROR(k44_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C44():
    # 'Coal_Foreign_Imports'!C44
    value = 4849555
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L44,"")'''
    @eval_fn
    def C44():
        l44_1 = Input_EIA_Imports_Coal_Foreign.L44()
        var_1 = IFERROR(l44_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D44():
    # 'Coal_Foreign_Imports'!D44
    value = 40.331958317
    formula = '''=IFERROR(C44/B44,"")'''
    @eval_fn
    def D44():
        c44_1 = Coal_Foreign_Imports.C44()
        b44_1 = Coal_Foreign_Imports.B44()
        var_1 = divide(c44_1, b44_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A45():
    # 'Coal_Foreign_Imports'!A45
    value = 2008
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A45,"")'''
    @eval_fn
    def A45():
        a45_1 = Input_EIA_Imports_Coal_Foreign.A45()
        var_1 = IFERROR(a45_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B45():
    # 'Coal_Foreign_Imports'!B45
    value = 39004
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K45,"")'''
    @eval_fn
    def B45():
        k45_1 = Input_EIA_Imports_Coal_Foreign.K45()
        var_1 = IFERROR(k45_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C45():
    # 'Coal_Foreign_Imports'!C45
    value = 2208384
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L45,"")'''
    @eval_fn
    def C45():
        l45_1 = Input_EIA_Imports_Coal_Foreign.L45()
        var_1 = IFERROR(l45_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D45():
    # 'Coal_Foreign_Imports'!D45
    value = 56.6194236489
    formula = '''=IFERROR(C45/B45,"")'''
    @eval_fn
    def D45():
        c45_1 = Coal_Foreign_Imports.C45()
        b45_1 = Coal_Foreign_Imports.B45()
        var_1 = divide(c45_1, b45_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A46():
    # 'Coal_Foreign_Imports'!A46
    value = 2008
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A46,"")'''
    @eval_fn
    def A46():
        a46_1 = Input_EIA_Imports_Coal_Foreign.A46()
        var_1 = IFERROR(a46_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B46():
    # 'Coal_Foreign_Imports'!B46
    value = 59172
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K46,"")'''
    @eval_fn
    def B46():
        k46_1 = Input_EIA_Imports_Coal_Foreign.K46()
        var_1 = IFERROR(k46_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C46():
    # 'Coal_Foreign_Imports'!C46
    value = 2305556
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L46,"")'''
    @eval_fn
    def C46():
        l46_1 = Input_EIA_Imports_Coal_Foreign.L46()
        var_1 = IFERROR(l46_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D46():
    # 'Coal_Foreign_Imports'!D46
    value = 38.9636314473
    formula = '''=IFERROR(C46/B46,"")'''
    @eval_fn
    def D46():
        c46_1 = Coal_Foreign_Imports.C46()
        b46_1 = Coal_Foreign_Imports.B46()
        var_1 = divide(c46_1, b46_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A47():
    # 'Coal_Foreign_Imports'!A47
    value = 2008
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A47,"")'''
    @eval_fn
    def A47():
        a47_1 = Input_EIA_Imports_Coal_Foreign.A47()
        var_1 = IFERROR(a47_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B47():
    # 'Coal_Foreign_Imports'!B47
    value = 117887
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K47,"")'''
    @eval_fn
    def B47():
        k47_1 = Input_EIA_Imports_Coal_Foreign.K47()
        var_1 = IFERROR(k47_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C47():
    # 'Coal_Foreign_Imports'!C47
    value = 4755424
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L47,"")'''
    @eval_fn
    def C47():
        l47_1 = Input_EIA_Imports_Coal_Foreign.L47()
        var_1 = IFERROR(l47_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D47():
    # 'Coal_Foreign_Imports'!D47
    value = 40.3388329502
    formula = '''=IFERROR(C47/B47,"")'''
    @eval_fn
    def D47():
        c47_1 = Coal_Foreign_Imports.C47()
        b47_1 = Coal_Foreign_Imports.B47()
        var_1 = divide(c47_1, b47_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A48():
    # 'Coal_Foreign_Imports'!A48
    value = 2008
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A48,"")'''
    @eval_fn
    def A48():
        a48_1 = Input_EIA_Imports_Coal_Foreign.A48()
        var_1 = IFERROR(a48_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B48():
    # 'Coal_Foreign_Imports'!B48
    value = 17234
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K48,"")'''
    @eval_fn
    def B48():
        k48_1 = Input_EIA_Imports_Coal_Foreign.K48()
        var_1 = IFERROR(k48_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C48():
    # 'Coal_Foreign_Imports'!C48
    value = 963367
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L48,"")'''
    @eval_fn
    def C48():
        l48_1 = Input_EIA_Imports_Coal_Foreign.L48()
        var_1 = IFERROR(l48_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D48():
    # 'Coal_Foreign_Imports'!D48
    value = 55.8992108622
    formula = '''=IFERROR(C48/B48,"")'''
    @eval_fn
    def D48():
        c48_1 = Coal_Foreign_Imports.C48()
        b48_1 = Coal_Foreign_Imports.B48()
        var_1 = divide(c48_1, b48_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A49():
    # 'Coal_Foreign_Imports'!A49
    value = 2008
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A49,"")'''
    @eval_fn
    def A49():
        a49_1 = Input_EIA_Imports_Coal_Foreign.A49()
        var_1 = IFERROR(a49_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B49():
    # 'Coal_Foreign_Imports'!B49
    value = 176159
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K49,"")'''
    @eval_fn
    def B49():
        k49_1 = Input_EIA_Imports_Coal_Foreign.K49()
        var_1 = IFERROR(k49_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C49():
    # 'Coal_Foreign_Imports'!C49
    value = 16145260
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L49,"")'''
    @eval_fn
    def C49():
        l49_1 = Input_EIA_Imports_Coal_Foreign.L49()
        var_1 = IFERROR(l49_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D49():
    # 'Coal_Foreign_Imports'!D49
    value = 91.6516328998
    formula = '''=IFERROR(C49/B49,"")'''
    @eval_fn
    def D49():
        c49_1 = Coal_Foreign_Imports.C49()
        b49_1 = Coal_Foreign_Imports.B49()
        var_1 = divide(c49_1, b49_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A50():
    # 'Coal_Foreign_Imports'!A50
    value = 2008
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A50,"")'''
    @eval_fn
    def A50():
        a50_1 = Input_EIA_Imports_Coal_Foreign.A50()
        var_1 = IFERROR(a50_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B50():
    # 'Coal_Foreign_Imports'!B50
    value = 24692
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K50,"")'''
    @eval_fn
    def B50():
        k50_1 = Input_EIA_Imports_Coal_Foreign.K50()
        var_1 = IFERROR(k50_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C50():
    # 'Coal_Foreign_Imports'!C50
    value = 1406720
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L50,"")'''
    @eval_fn
    def C50():
        l50_1 = Input_EIA_Imports_Coal_Foreign.L50()
        var_1 = IFERROR(l50_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D50():
    # 'Coal_Foreign_Imports'!D50
    value = 56.9706787624
    formula = '''=IFERROR(C50/B50,"")'''
    @eval_fn
    def D50():
        c50_1 = Coal_Foreign_Imports.C50()
        b50_1 = Coal_Foreign_Imports.B50()
        var_1 = divide(c50_1, b50_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A51():
    # 'Coal_Foreign_Imports'!A51
    value = 2008
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A51,"")'''
    @eval_fn
    def A51():
        a51_1 = Input_EIA_Imports_Coal_Foreign.A51()
        var_1 = IFERROR(a51_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B51():
    # 'Coal_Foreign_Imports'!B51
    value = 184843
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K51,"")'''
    @eval_fn
    def B51():
        k51_1 = Input_EIA_Imports_Coal_Foreign.K51()
        var_1 = IFERROR(k51_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C51():
    # 'Coal_Foreign_Imports'!C51
    value = 8706644
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L51,"")'''
    @eval_fn
    def C51():
        l51_1 = Input_EIA_Imports_Coal_Foreign.L51()
        var_1 = IFERROR(l51_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D51():
    # 'Coal_Foreign_Imports'!D51
    value = 47.1029143652
    formula = '''=IFERROR(C51/B51,"")'''
    @eval_fn
    def D51():
        c51_1 = Coal_Foreign_Imports.C51()
        b51_1 = Coal_Foreign_Imports.B51()
        var_1 = divide(c51_1, b51_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A52():
    # 'Coal_Foreign_Imports'!A52
    value = 2008
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A52,"")'''
    @eval_fn
    def A52():
        a52_1 = Input_EIA_Imports_Coal_Foreign.A52()
        var_1 = IFERROR(a52_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B52():
    # 'Coal_Foreign_Imports'!B52
    value = 68414
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K52,"")'''
    @eval_fn
    def B52():
        k52_1 = Input_EIA_Imports_Coal_Foreign.K52()
        var_1 = IFERROR(k52_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C52():
    # 'Coal_Foreign_Imports'!C52
    value = 3364517
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L52,"")'''
    @eval_fn
    def C52():
        l52_1 = Input_EIA_Imports_Coal_Foreign.L52()
        var_1 = IFERROR(l52_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D52():
    # 'Coal_Foreign_Imports'!D52
    value = 49.1787791972
    formula = '''=IFERROR(C52/B52,"")'''
    @eval_fn
    def D52():
        c52_1 = Coal_Foreign_Imports.C52()
        b52_1 = Coal_Foreign_Imports.B52()
        var_1 = divide(c52_1, b52_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A53():
    # 'Coal_Foreign_Imports'!A53
    value = 2008
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A53,"")'''
    @eval_fn
    def A53():
        a53_1 = Input_EIA_Imports_Coal_Foreign.A53()
        var_1 = IFERROR(a53_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B53():
    # 'Coal_Foreign_Imports'!B53
    value = 59293
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K53,"")'''
    @eval_fn
    def B53():
        k53_1 = Input_EIA_Imports_Coal_Foreign.K53()
        var_1 = IFERROR(k53_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C53():
    # 'Coal_Foreign_Imports'!C53
    value = 2409254
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L53,"")'''
    @eval_fn
    def C53():
        l53_1 = Input_EIA_Imports_Coal_Foreign.L53()
        var_1 = IFERROR(l53_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D53():
    # 'Coal_Foreign_Imports'!D53
    value = 40.6330258209
    formula = '''=IFERROR(C53/B53,"")'''
    @eval_fn
    def D53():
        c53_1 = Coal_Foreign_Imports.C53()
        b53_1 = Coal_Foreign_Imports.B53()
        var_1 = divide(c53_1, b53_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A54():
    # 'Coal_Foreign_Imports'!A54
    value = 2009
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A54,"")'''
    @eval_fn
    def A54():
        a54_1 = Input_EIA_Imports_Coal_Foreign.A54()
        var_1 = IFERROR(a54_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B54():
    # 'Coal_Foreign_Imports'!B54
    value = 59563
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K54,"")'''
    @eval_fn
    def B54():
        k54_1 = Input_EIA_Imports_Coal_Foreign.K54()
        var_1 = IFERROR(k54_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C54():
    # 'Coal_Foreign_Imports'!C54
    value = 3461216
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L54,"")'''
    @eval_fn
    def C54():
        l54_1 = Input_EIA_Imports_Coal_Foreign.L54()
        var_1 = IFERROR(l54_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D54():
    # 'Coal_Foreign_Imports'!D54
    value = 58.1101690647
    formula = '''=IFERROR(C54/B54,"")'''
    @eval_fn
    def D54():
        c54_1 = Coal_Foreign_Imports.C54()
        b54_1 = Coal_Foreign_Imports.B54()
        var_1 = divide(c54_1, b54_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A55():
    # 'Coal_Foreign_Imports'!A55
    value = 2009
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A55,"")'''
    @eval_fn
    def A55():
        a55_1 = Input_EIA_Imports_Coal_Foreign.A55()
        var_1 = IFERROR(a55_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B55():
    # 'Coal_Foreign_Imports'!B55
    value = 172130
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K55,"")'''
    @eval_fn
    def B55():
        k55_1 = Input_EIA_Imports_Coal_Foreign.K55()
        var_1 = IFERROR(k55_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C55():
    # 'Coal_Foreign_Imports'!C55
    value = 7123314
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L55,"")'''
    @eval_fn
    def C55():
        l55_1 = Input_EIA_Imports_Coal_Foreign.L55()
        var_1 = IFERROR(l55_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D55():
    # 'Coal_Foreign_Imports'!D55
    value = 41.3833381746
    formula = '''=IFERROR(C55/B55,"")'''
    @eval_fn
    def D55():
        c55_1 = Coal_Foreign_Imports.C55()
        b55_1 = Coal_Foreign_Imports.B55()
        var_1 = divide(c55_1, b55_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A56():
    # 'Coal_Foreign_Imports'!A56
    value = 2009
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A56,"")'''
    @eval_fn
    def A56():
        a56_1 = Input_EIA_Imports_Coal_Foreign.A56()
        var_1 = IFERROR(a56_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B56():
    # 'Coal_Foreign_Imports'!B56
    value = 170607
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K56,"")'''
    @eval_fn
    def B56():
        k56_1 = Input_EIA_Imports_Coal_Foreign.K56()
        var_1 = IFERROR(k56_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C56():
    # 'Coal_Foreign_Imports'!C56
    value = 10616975
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L56,"")'''
    @eval_fn
    def C56():
        l56_1 = Input_EIA_Imports_Coal_Foreign.L56()
        var_1 = IFERROR(l56_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D56():
    # 'Coal_Foreign_Imports'!D56
    value = 62.2305942898
    formula = '''=IFERROR(C56/B56,"")'''
    @eval_fn
    def D56():
        c56_1 = Coal_Foreign_Imports.C56()
        b56_1 = Coal_Foreign_Imports.B56()
        var_1 = divide(c56_1, b56_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A57():
    # 'Coal_Foreign_Imports'!A57
    value = 2009
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A57,"")'''
    @eval_fn
    def A57():
        a57_1 = Input_EIA_Imports_Coal_Foreign.A57()
        var_1 = IFERROR(a57_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B57():
    # 'Coal_Foreign_Imports'!B57
    value = 33951
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K57,"")'''
    @eval_fn
    def B57():
        k57_1 = Input_EIA_Imports_Coal_Foreign.K57()
        var_1 = IFERROR(k57_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C57():
    # 'Coal_Foreign_Imports'!C57
    value = 2007939
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L57,"")'''
    @eval_fn
    def C57():
        l57_1 = Input_EIA_Imports_Coal_Foreign.L57()
        var_1 = IFERROR(l57_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D57():
    # 'Coal_Foreign_Imports'!D57
    value = 59.1422638508
    formula = '''=IFERROR(C57/B57,"")'''
    @eval_fn
    def D57():
        c57_1 = Coal_Foreign_Imports.C57()
        b57_1 = Coal_Foreign_Imports.B57()
        var_1 = divide(c57_1, b57_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A58():
    # 'Coal_Foreign_Imports'!A58
    value = 2009
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A58,"")'''
    @eval_fn
    def A58():
        a58_1 = Input_EIA_Imports_Coal_Foreign.A58()
        var_1 = IFERROR(a58_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B58():
    # 'Coal_Foreign_Imports'!B58
    value = 177870
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K58,"")'''
    @eval_fn
    def B58():
        k58_1 = Input_EIA_Imports_Coal_Foreign.K58()
        var_1 = IFERROR(k58_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C58():
    # 'Coal_Foreign_Imports'!C58
    value = 10229824
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L58,"")'''
    @eval_fn
    def C58():
        l58_1 = Input_EIA_Imports_Coal_Foreign.L58()
        var_1 = IFERROR(l58_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D58():
    # 'Coal_Foreign_Imports'!D58
    value = 57.5129251701
    formula = '''=IFERROR(C58/B58,"")'''
    @eval_fn
    def D58():
        c58_1 = Coal_Foreign_Imports.C58()
        b58_1 = Coal_Foreign_Imports.B58()
        var_1 = divide(c58_1, b58_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A59():
    # 'Coal_Foreign_Imports'!A59
    value = 2009
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A59,"")'''
    @eval_fn
    def A59():
        a59_1 = Input_EIA_Imports_Coal_Foreign.A59()
        var_1 = IFERROR(a59_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B59():
    # 'Coal_Foreign_Imports'!B59
    value = 58224
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K59,"")'''
    @eval_fn
    def B59():
        k59_1 = Input_EIA_Imports_Coal_Foreign.K59()
        var_1 = IFERROR(k59_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C59():
    # 'Coal_Foreign_Imports'!C59
    value = 3261836
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L59,"")'''
    @eval_fn
    def C59():
        l59_1 = Input_EIA_Imports_Coal_Foreign.L59()
        var_1 = IFERROR(l59_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D59():
    # 'Coal_Foreign_Imports'!D59
    value = 56.0221901621
    formula = '''=IFERROR(C59/B59,"")'''
    @eval_fn
    def D59():
        c59_1 = Coal_Foreign_Imports.C59()
        b59_1 = Coal_Foreign_Imports.B59()
        var_1 = divide(c59_1, b59_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A60():
    # 'Coal_Foreign_Imports'!A60
    value = 2009
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A60,"")'''
    @eval_fn
    def A60():
        a60_1 = Input_EIA_Imports_Coal_Foreign.A60()
        var_1 = IFERROR(a60_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B60():
    # 'Coal_Foreign_Imports'!B60
    value = 121200
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K60,"")'''
    @eval_fn
    def B60():
        k60_1 = Input_EIA_Imports_Coal_Foreign.K60()
        var_1 = IFERROR(k60_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C60():
    # 'Coal_Foreign_Imports'!C60
    value = 6494746
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L60,"")'''
    @eval_fn
    def C60():
        l60_1 = Input_EIA_Imports_Coal_Foreign.L60()
        var_1 = IFERROR(l60_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D60():
    # 'Coal_Foreign_Imports'!D60
    value = 53.5870132013
    formula = '''=IFERROR(C60/B60,"")'''
    @eval_fn
    def D60():
        c60_1 = Coal_Foreign_Imports.C60()
        b60_1 = Coal_Foreign_Imports.B60()
        var_1 = divide(c60_1, b60_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A61():
    # 'Coal_Foreign_Imports'!A61
    value = 2010
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A61,"")'''
    @eval_fn
    def A61():
        a61_1 = Input_EIA_Imports_Coal_Foreign.A61()
        var_1 = IFERROR(a61_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B61():
    # 'Coal_Foreign_Imports'!B61
    value = 91604
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K61,"")'''
    @eval_fn
    def B61():
        k61_1 = Input_EIA_Imports_Coal_Foreign.K61()
        var_1 = IFERROR(k61_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C61():
    # 'Coal_Foreign_Imports'!C61
    value = 4977310
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L61,"")'''
    @eval_fn
    def C61():
        l61_1 = Input_EIA_Imports_Coal_Foreign.L61()
        var_1 = IFERROR(l61_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D61():
    # 'Coal_Foreign_Imports'!D61
    value = 54.3350727042
    formula = '''=IFERROR(C61/B61,"")'''
    @eval_fn
    def D61():
        c61_1 = Coal_Foreign_Imports.C61()
        b61_1 = Coal_Foreign_Imports.B61()
        var_1 = divide(c61_1, b61_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A62():
    # 'Coal_Foreign_Imports'!A62
    value = 2010
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A62,"")'''
    @eval_fn
    def A62():
        a62_1 = Input_EIA_Imports_Coal_Foreign.A62()
        var_1 = IFERROR(a62_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B62():
    # 'Coal_Foreign_Imports'!B62
    value = 110523
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K62,"")'''
    @eval_fn
    def B62():
        k62_1 = Input_EIA_Imports_Coal_Foreign.K62()
        var_1 = IFERROR(k62_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C62():
    # 'Coal_Foreign_Imports'!C62
    value = 5922653
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L62,"")'''
    @eval_fn
    def C62():
        l62_1 = Input_EIA_Imports_Coal_Foreign.L62()
        var_1 = IFERROR(l62_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D62():
    # 'Coal_Foreign_Imports'!D62
    value = 53.5875157207
    formula = '''=IFERROR(C62/B62,"")'''
    @eval_fn
    def D62():
        c62_1 = Coal_Foreign_Imports.C62()
        b62_1 = Coal_Foreign_Imports.B62()
        var_1 = divide(c62_1, b62_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A63():
    # 'Coal_Foreign_Imports'!A63
    value = 2010
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A63,"")'''
    @eval_fn
    def A63():
        a63_1 = Input_EIA_Imports_Coal_Foreign.A63()
        var_1 = IFERROR(a63_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B63():
    # 'Coal_Foreign_Imports'!B63
    value = 169012
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K63,"")'''
    @eval_fn
    def B63():
        k63_1 = Input_EIA_Imports_Coal_Foreign.K63()
        var_1 = IFERROR(k63_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C63():
    # 'Coal_Foreign_Imports'!C63
    value = 11161217
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L63,"")'''
    @eval_fn
    def C63():
        l63_1 = Input_EIA_Imports_Coal_Foreign.L63()
        var_1 = IFERROR(l63_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D63():
    # 'Coal_Foreign_Imports'!D63
    value = 66.0380150522
    formula = '''=IFERROR(C63/B63,"")'''
    @eval_fn
    def D63():
        c63_1 = Coal_Foreign_Imports.C63()
        b63_1 = Coal_Foreign_Imports.B63()
        var_1 = divide(c63_1, b63_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A64():
    # 'Coal_Foreign_Imports'!A64
    value = 2010
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A64,"")'''
    @eval_fn
    def A64():
        a64_1 = Input_EIA_Imports_Coal_Foreign.A64()
        var_1 = IFERROR(a64_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B64():
    # 'Coal_Foreign_Imports'!B64
    value = 81103
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K64,"")'''
    @eval_fn
    def B64():
        k64_1 = Input_EIA_Imports_Coal_Foreign.K64()
        var_1 = IFERROR(k64_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C64():
    # 'Coal_Foreign_Imports'!C64
    value = 4258140
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L64,"")'''
    @eval_fn
    def C64():
        l64_1 = Input_EIA_Imports_Coal_Foreign.L64()
        var_1 = IFERROR(l64_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D64():
    # 'Coal_Foreign_Imports'!D64
    value = 52.502866725
    formula = '''=IFERROR(C64/B64,"")'''
    @eval_fn
    def D64():
        c64_1 = Coal_Foreign_Imports.C64()
        b64_1 = Coal_Foreign_Imports.B64()
        var_1 = divide(c64_1, b64_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A65():
    # 'Coal_Foreign_Imports'!A65
    value = 2010
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A65,"")'''
    @eval_fn
    def A65():
        a65_1 = Input_EIA_Imports_Coal_Foreign.A65()
        var_1 = IFERROR(a65_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B65():
    # 'Coal_Foreign_Imports'!B65
    value = 58492
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K65,"")'''
    @eval_fn
    def B65():
        k65_1 = Input_EIA_Imports_Coal_Foreign.K65()
        var_1 = IFERROR(k65_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C65():
    # 'Coal_Foreign_Imports'!C65
    value = 3555208
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L65,"")'''
    @eval_fn
    def C65():
        l65_1 = Input_EIA_Imports_Coal_Foreign.L65()
        var_1 = IFERROR(l65_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D65():
    # 'Coal_Foreign_Imports'!D65
    value = 60.7810982698
    formula = '''=IFERROR(C65/B65,"")'''
    @eval_fn
    def D65():
        c65_1 = Coal_Foreign_Imports.C65()
        b65_1 = Coal_Foreign_Imports.B65()
        var_1 = divide(c65_1, b65_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A66():
    # 'Coal_Foreign_Imports'!A66
    value = 2010
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A66,"")'''
    @eval_fn
    def A66():
        a66_1 = Input_EIA_Imports_Coal_Foreign.A66()
        var_1 = IFERROR(a66_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B66():
    # 'Coal_Foreign_Imports'!B66
    value = 116748
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K66,"")'''
    @eval_fn
    def B66():
        k66_1 = Input_EIA_Imports_Coal_Foreign.K66()
        var_1 = IFERROR(k66_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C66():
    # 'Coal_Foreign_Imports'!C66
    value = 6256221
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L66,"")'''
    @eval_fn
    def C66():
        l66_1 = Input_EIA_Imports_Coal_Foreign.L66()
        var_1 = IFERROR(l66_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D66():
    # 'Coal_Foreign_Imports'!D66
    value = 53.5873933601
    formula = '''=IFERROR(C66/B66,"")'''
    @eval_fn
    def D66():
        c66_1 = Coal_Foreign_Imports.C66()
        b66_1 = Coal_Foreign_Imports.B66()
        var_1 = divide(c66_1, b66_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A67():
    # 'Coal_Foreign_Imports'!A67
    value = 2010
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A67,"")'''
    @eval_fn
    def A67():
        a67_1 = Input_EIA_Imports_Coal_Foreign.A67()
        var_1 = IFERROR(a67_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B67():
    # 'Coal_Foreign_Imports'!B67
    value = 207697
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K67,"")'''
    @eval_fn
    def B67():
        k67_1 = Input_EIA_Imports_Coal_Foreign.K67()
        var_1 = IFERROR(k67_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C67():
    # 'Coal_Foreign_Imports'!C67
    value = 12350831
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L67,"")'''
    @eval_fn
    def C67():
        l67_1 = Input_EIA_Imports_Coal_Foreign.L67()
        var_1 = IFERROR(l67_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D67():
    # 'Coal_Foreign_Imports'!D67
    value = 59.4656205915
    formula = '''=IFERROR(C67/B67,"")'''
    @eval_fn
    def D67():
        c67_1 = Coal_Foreign_Imports.C67()
        b67_1 = Coal_Foreign_Imports.B67()
        var_1 = divide(c67_1, b67_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A68():
    # 'Coal_Foreign_Imports'!A68
    value = 2011
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A68,"")'''
    @eval_fn
    def A68():
        a68_1 = Input_EIA_Imports_Coal_Foreign.A68()
        var_1 = IFERROR(a68_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B68():
    # 'Coal_Foreign_Imports'!B68
    value = 61745
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K68,"")'''
    @eval_fn
    def B68():
        k68_1 = Input_EIA_Imports_Coal_Foreign.K68()
        var_1 = IFERROR(k68_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C68():
    # 'Coal_Foreign_Imports'!C68
    value = 3254974
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L68,"")'''
    @eval_fn
    def C68():
        l68_1 = Input_EIA_Imports_Coal_Foreign.L68()
        var_1 = IFERROR(l68_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D68():
    # 'Coal_Foreign_Imports'!D68
    value = 52.7163980889
    formula = '''=IFERROR(C68/B68,"")'''
    @eval_fn
    def D68():
        c68_1 = Coal_Foreign_Imports.C68()
        b68_1 = Coal_Foreign_Imports.B68()
        var_1 = divide(c68_1, b68_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A69():
    # 'Coal_Foreign_Imports'!A69
    value = 2011
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A69,"")'''
    @eval_fn
    def A69():
        a69_1 = Input_EIA_Imports_Coal_Foreign.A69()
        var_1 = IFERROR(a69_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B69():
    # 'Coal_Foreign_Imports'!B69
    value = 56942
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K69,"")'''
    @eval_fn
    def B69():
        k69_1 = Input_EIA_Imports_Coal_Foreign.K69()
        var_1 = IFERROR(k69_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C69():
    # 'Coal_Foreign_Imports'!C69
    value = 2686164
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L69,"")'''
    @eval_fn
    def C69():
        l69_1 = Input_EIA_Imports_Coal_Foreign.L69()
        var_1 = IFERROR(l69_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D69():
    # 'Coal_Foreign_Imports'!D69
    value = 47.1736855045
    formula = '''=IFERROR(C69/B69,"")'''
    @eval_fn
    def D69():
        c69_1 = Coal_Foreign_Imports.C69()
        b69_1 = Coal_Foreign_Imports.B69()
        var_1 = divide(c69_1, b69_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A70():
    # 'Coal_Foreign_Imports'!A70
    value = 2011
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A70,"")'''
    @eval_fn
    def A70():
        a70_1 = Input_EIA_Imports_Coal_Foreign.A70()
        var_1 = IFERROR(a70_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B70():
    # 'Coal_Foreign_Imports'!B70
    value = 60189
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K70,"")'''
    @eval_fn
    def B70():
        k70_1 = Input_EIA_Imports_Coal_Foreign.K70()
        var_1 = IFERROR(k70_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C70():
    # 'Coal_Foreign_Imports'!C70
    value = 3112371
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L70,"")'''
    @eval_fn
    def C70():
        l70_1 = Input_EIA_Imports_Coal_Foreign.L70()
        var_1 = IFERROR(l70_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D70():
    # 'Coal_Foreign_Imports'!D70
    value = 51.7099636146
    formula = '''=IFERROR(C70/B70,"")'''
    @eval_fn
    def D70():
        c70_1 = Coal_Foreign_Imports.C70()
        b70_1 = Coal_Foreign_Imports.B70()
        var_1 = divide(c70_1, b70_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A71():
    # 'Coal_Foreign_Imports'!A71
    value = 2011
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A71,"")'''
    @eval_fn
    def A71():
        a71_1 = Input_EIA_Imports_Coal_Foreign.A71()
        var_1 = IFERROR(a71_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B71():
    # 'Coal_Foreign_Imports'!B71
    value = 63202
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K71,"")'''
    @eval_fn
    def B71():
        k71_1 = Input_EIA_Imports_Coal_Foreign.K71()
        var_1 = IFERROR(k71_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C71():
    # 'Coal_Foreign_Imports'!C71
    value = 2981457
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L71,"")'''
    @eval_fn
    def C71():
        l71_1 = Input_EIA_Imports_Coal_Foreign.L71()
        var_1 = IFERROR(l71_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D71():
    # 'Coal_Foreign_Imports'!D71
    value = 47.1734597006
    formula = '''=IFERROR(C71/B71,"")'''
    @eval_fn
    def D71():
        c71_1 = Coal_Foreign_Imports.C71()
        b71_1 = Coal_Foreign_Imports.B71()
        var_1 = divide(c71_1, b71_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A72():
    # 'Coal_Foreign_Imports'!A72
    value = 2011
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A72,"")'''
    @eval_fn
    def A72():
        a72_1 = Input_EIA_Imports_Coal_Foreign.A72()
        var_1 = IFERROR(a72_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B72():
    # 'Coal_Foreign_Imports'!B72
    value = 237787
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K72,"")'''
    @eval_fn
    def B72():
        k72_1 = Input_EIA_Imports_Coal_Foreign.K72()
        var_1 = IFERROR(k72_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C72():
    # 'Coal_Foreign_Imports'!C72
    value = 12560141
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L72,"")'''
    @eval_fn
    def C72():
        l72_1 = Input_EIA_Imports_Coal_Foreign.L72()
        var_1 = IFERROR(l72_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D72():
    # 'Coal_Foreign_Imports'!D72
    value = 52.8209742332
    formula = '''=IFERROR(C72/B72,"")'''
    @eval_fn
    def D72():
        c72_1 = Coal_Foreign_Imports.C72()
        b72_1 = Coal_Foreign_Imports.B72()
        var_1 = divide(c72_1, b72_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A73():
    # 'Coal_Foreign_Imports'!A73
    value = 2011
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A73,"")'''
    @eval_fn
    def A73():
        a73_1 = Input_EIA_Imports_Coal_Foreign.A73()
        var_1 = IFERROR(a73_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B73():
    # 'Coal_Foreign_Imports'!B73
    value = 121866
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K73,"")'''
    @eval_fn
    def B73():
        k73_1 = Input_EIA_Imports_Coal_Foreign.K73()
        var_1 = IFERROR(k73_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C73():
    # 'Coal_Foreign_Imports'!C73
    value = 5634013
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L73,"")'''
    @eval_fn
    def C73():
        l73_1 = Input_EIA_Imports_Coal_Foreign.L73()
        var_1 = IFERROR(l73_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D73():
    # 'Coal_Foreign_Imports'!D73
    value = 46.2312129716
    formula = '''=IFERROR(C73/B73,"")'''
    @eval_fn
    def D73():
        c73_1 = Coal_Foreign_Imports.C73()
        b73_1 = Coal_Foreign_Imports.B73()
        var_1 = divide(c73_1, b73_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class P73():
    # 'Coal_Foreign_Imports'!P73
    value = "a"

@register(Coal_Foreign_Imports)
class A74():
    # 'Coal_Foreign_Imports'!A74
    value = 2011
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A74,"")'''
    @eval_fn
    def A74():
        a74_1 = Input_EIA_Imports_Coal_Foreign.A74()
        var_1 = IFERROR(a74_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B74():
    # 'Coal_Foreign_Imports'!B74
    value = 120995
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K74,"")'''
    @eval_fn
    def B74():
        k74_1 = Input_EIA_Imports_Coal_Foreign.K74()
        var_1 = IFERROR(k74_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C74():
    # 'Coal_Foreign_Imports'!C74
    value = 5382691
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L74,"")'''
    @eval_fn
    def C74():
        l74_1 = Input_EIA_Imports_Coal_Foreign.L74()
        var_1 = IFERROR(l74_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D74():
    # 'Coal_Foreign_Imports'!D74
    value = 44.4868878879
    formula = '''=IFERROR(C74/B74,"")'''
    @eval_fn
    def D74():
        c74_1 = Coal_Foreign_Imports.C74()
        b74_1 = Coal_Foreign_Imports.B74()
        var_1 = divide(c74_1, b74_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A75():
    # 'Coal_Foreign_Imports'!A75
    value = 2011
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A75,"")'''
    @eval_fn
    def A75():
        a75_1 = Input_EIA_Imports_Coal_Foreign.A75()
        var_1 = IFERROR(a75_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B75():
    # 'Coal_Foreign_Imports'!B75
    value = 122613
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K75,"")'''
    @eval_fn
    def B75():
        k75_1 = Input_EIA_Imports_Coal_Foreign.K75()
        var_1 = IFERROR(k75_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C75():
    # 'Coal_Foreign_Imports'!C75
    value = 5894780
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L75,"")'''
    @eval_fn
    def C75():
        l75_1 = Input_EIA_Imports_Coal_Foreign.L75()
        var_1 = IFERROR(l75_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D75():
    # 'Coal_Foreign_Imports'!D75
    value = 48.0763051226
    formula = '''=IFERROR(C75/B75,"")'''
    @eval_fn
    def D75():
        c75_1 = Coal_Foreign_Imports.C75()
        b75_1 = Coal_Foreign_Imports.B75()
        var_1 = divide(c75_1, b75_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A76():
    # 'Coal_Foreign_Imports'!A76
    value = 2012
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A76,"")'''
    @eval_fn
    def A76():
        a76_1 = Input_EIA_Imports_Coal_Foreign.A76()
        var_1 = IFERROR(a76_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B76():
    # 'Coal_Foreign_Imports'!B76
    value = 118081
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K76,"")'''
    @eval_fn
    def B76():
        k76_1 = Input_EIA_Imports_Coal_Foreign.K76()
        var_1 = IFERROR(k76_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C76():
    # 'Coal_Foreign_Imports'!C76
    value = 6158969
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L76,"")'''
    @eval_fn
    def C76():
        l76_1 = Input_EIA_Imports_Coal_Foreign.L76()
        var_1 = IFERROR(l76_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D76():
    # 'Coal_Foreign_Imports'!D76
    value = 52.158848587
    formula = '''=IFERROR(C76/B76,"")'''
    @eval_fn
    def D76():
        c76_1 = Coal_Foreign_Imports.C76()
        b76_1 = Coal_Foreign_Imports.B76()
        var_1 = divide(c76_1, b76_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A77():
    # 'Coal_Foreign_Imports'!A77
    value = 2012
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A77,"")'''
    @eval_fn
    def A77():
        a77_1 = Input_EIA_Imports_Coal_Foreign.A77()
        var_1 = IFERROR(a77_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B77():
    # 'Coal_Foreign_Imports'!B77
    value = 181879
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K77,"")'''
    @eval_fn
    def B77():
        k77_1 = Input_EIA_Imports_Coal_Foreign.K77()
        var_1 = IFERROR(k77_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C77():
    # 'Coal_Foreign_Imports'!C77
    value = 9031732
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L77,"")'''
    @eval_fn
    def C77():
        l77_1 = Input_EIA_Imports_Coal_Foreign.L77()
        var_1 = IFERROR(l77_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D77():
    # 'Coal_Foreign_Imports'!D77
    value = 49.6579154273
    formula = '''=IFERROR(C77/B77,"")'''
    @eval_fn
    def D77():
        c77_1 = Coal_Foreign_Imports.C77()
        b77_1 = Coal_Foreign_Imports.B77()
        var_1 = divide(c77_1, b77_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A78():
    # 'Coal_Foreign_Imports'!A78
    value = 2012
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A78,"")'''
    @eval_fn
    def A78():
        a78_1 = Input_EIA_Imports_Coal_Foreign.A78()
        var_1 = IFERROR(a78_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B78():
    # 'Coal_Foreign_Imports'!B78
    value = 120912
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K78,"")'''
    @eval_fn
    def B78():
        k78_1 = Input_EIA_Imports_Coal_Foreign.K78()
        var_1 = IFERROR(k78_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C78():
    # 'Coal_Foreign_Imports'!C78
    value = 6066056
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L78,"")'''
    @eval_fn
    def C78():
        l78_1 = Input_EIA_Imports_Coal_Foreign.L78()
        var_1 = IFERROR(l78_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D78():
    # 'Coal_Foreign_Imports'!D78
    value = 50.1691808919
    formula = '''=IFERROR(C78/B78,"")'''
    @eval_fn
    def D78():
        c78_1 = Coal_Foreign_Imports.C78()
        b78_1 = Coal_Foreign_Imports.B78()
        var_1 = divide(c78_1, b78_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A79():
    # 'Coal_Foreign_Imports'!A79
    value = 2012
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A79,"")'''
    @eval_fn
    def A79():
        a79_1 = Input_EIA_Imports_Coal_Foreign.A79()
        var_1 = IFERROR(a79_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B79():
    # 'Coal_Foreign_Imports'!B79
    value = 117500
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K79,"")'''
    @eval_fn
    def B79():
        k79_1 = Input_EIA_Imports_Coal_Foreign.K79()
        var_1 = IFERROR(k79_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C79():
    # 'Coal_Foreign_Imports'!C79
    value = 6624014
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L79,"")'''
    @eval_fn
    def C79():
        l79_1 = Input_EIA_Imports_Coal_Foreign.L79()
        var_1 = IFERROR(l79_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D79():
    # 'Coal_Foreign_Imports'!D79
    value = 56.374587234
    formula = '''=IFERROR(C79/B79,"")'''
    @eval_fn
    def D79():
        c79_1 = Coal_Foreign_Imports.C79()
        b79_1 = Coal_Foreign_Imports.B79()
        var_1 = divide(c79_1, b79_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A80():
    # 'Coal_Foreign_Imports'!A80
    value = 2012
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A80,"")'''
    @eval_fn
    def A80():
        a80_1 = Input_EIA_Imports_Coal_Foreign.A80()
        var_1 = IFERROR(a80_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B80():
    # 'Coal_Foreign_Imports'!B80
    value = 59280
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K80,"")'''
    @eval_fn
    def B80():
        k80_1 = Input_EIA_Imports_Coal_Foreign.K80()
        var_1 = IFERROR(k80_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C80():
    # 'Coal_Foreign_Imports'!C80
    value = 2821733
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L80,"")'''
    @eval_fn
    def C80():
        l80_1 = Input_EIA_Imports_Coal_Foreign.L80()
        var_1 = IFERROR(l80_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D80():
    # 'Coal_Foreign_Imports'!D80
    value = 47.6000843455
    formula = '''=IFERROR(C80/B80,"")'''
    @eval_fn
    def D80():
        c80_1 = Coal_Foreign_Imports.C80()
        b80_1 = Coal_Foreign_Imports.B80()
        var_1 = divide(c80_1, b80_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A81():
    # 'Coal_Foreign_Imports'!A81
    value = 2012
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A81,"")'''
    @eval_fn
    def A81():
        a81_1 = Input_EIA_Imports_Coal_Foreign.A81()
        var_1 = IFERROR(a81_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B81():
    # 'Coal_Foreign_Imports'!B81
    value = 120129
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K81,"")'''
    @eval_fn
    def B81():
        k81_1 = Input_EIA_Imports_Coal_Foreign.K81()
        var_1 = IFERROR(k81_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C81():
    # 'Coal_Foreign_Imports'!C81
    value = 6911620
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L81,"")'''
    @eval_fn
    def C81():
        l81_1 = Input_EIA_Imports_Coal_Foreign.L81()
        var_1 = IFERROR(l81_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D81():
    # 'Coal_Foreign_Imports'!D81
    value = 57.5349832264
    formula = '''=IFERROR(C81/B81,"")'''
    @eval_fn
    def D81():
        c81_1 = Coal_Foreign_Imports.C81()
        b81_1 = Coal_Foreign_Imports.B81()
        var_1 = divide(c81_1, b81_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A82():
    # 'Coal_Foreign_Imports'!A82
    value = 2013
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A82,"")'''
    @eval_fn
    def A82():
        a82_1 = Input_EIA_Imports_Coal_Foreign.A82()
        var_1 = IFERROR(a82_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B82():
    # 'Coal_Foreign_Imports'!B82
    value = 117481
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K82,"")'''
    @eval_fn
    def B82():
        k82_1 = Input_EIA_Imports_Coal_Foreign.K82()
        var_1 = IFERROR(k82_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C82():
    # 'Coal_Foreign_Imports'!C82
    value = 7107782
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L82,"")'''
    @eval_fn
    def C82():
        l82_1 = Input_EIA_Imports_Coal_Foreign.L82()
        var_1 = IFERROR(l82_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D82():
    # 'Coal_Foreign_Imports'!D82
    value = 60.5015449307
    formula = '''=IFERROR(C82/B82,"")'''
    @eval_fn
    def D82():
        c82_1 = Coal_Foreign_Imports.C82()
        b82_1 = Coal_Foreign_Imports.B82()
        var_1 = divide(c82_1, b82_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A83():
    # 'Coal_Foreign_Imports'!A83
    value = 2013
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A83,"")'''
    @eval_fn
    def A83():
        a83_1 = Input_EIA_Imports_Coal_Foreign.A83()
        var_1 = IFERROR(a83_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B83():
    # 'Coal_Foreign_Imports'!B83
    value = 180355
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K83,"")'''
    @eval_fn
    def B83():
        k83_1 = Input_EIA_Imports_Coal_Foreign.K83()
        var_1 = IFERROR(k83_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C83():
    # 'Coal_Foreign_Imports'!C83
    value = 11208629
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L83,"")'''
    @eval_fn
    def C83():
        l83_1 = Input_EIA_Imports_Coal_Foreign.L83()
        var_1 = IFERROR(l83_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D83():
    # 'Coal_Foreign_Imports'!D83
    value = 62.1475922486
    formula = '''=IFERROR(C83/B83,"")'''
    @eval_fn
    def D83():
        c83_1 = Coal_Foreign_Imports.C83()
        b83_1 = Coal_Foreign_Imports.B83()
        var_1 = divide(c83_1, b83_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A84():
    # 'Coal_Foreign_Imports'!A84
    value = 2013
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A84,"")'''
    @eval_fn
    def A84():
        a84_1 = Input_EIA_Imports_Coal_Foreign.A84()
        var_1 = IFERROR(a84_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B84():
    # 'Coal_Foreign_Imports'!B84
    value = 187311
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K84,"")'''
    @eval_fn
    def B84():
        k84_1 = Input_EIA_Imports_Coal_Foreign.K84()
        var_1 = IFERROR(k84_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C84():
    # 'Coal_Foreign_Imports'!C84
    value = 11958306
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L84,"")'''
    @eval_fn
    def C84():
        l84_1 = Input_EIA_Imports_Coal_Foreign.L84()
        var_1 = IFERROR(l84_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D84():
    # 'Coal_Foreign_Imports'!D84
    value = 63.8419847206
    formula = '''=IFERROR(C84/B84,"")'''
    @eval_fn
    def D84():
        c84_1 = Coal_Foreign_Imports.C84()
        b84_1 = Coal_Foreign_Imports.B84()
        var_1 = divide(c84_1, b84_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A85():
    # 'Coal_Foreign_Imports'!A85
    value = 2013
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A85,"")'''
    @eval_fn
    def A85():
        a85_1 = Input_EIA_Imports_Coal_Foreign.A85()
        var_1 = IFERROR(a85_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B85():
    # 'Coal_Foreign_Imports'!B85
    value = 181496
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K85,"")'''
    @eval_fn
    def B85():
        k85_1 = Input_EIA_Imports_Coal_Foreign.K85()
        var_1 = IFERROR(k85_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C85():
    # 'Coal_Foreign_Imports'!C85
    value = 10426789
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L85,"")'''
    @eval_fn
    def C85():
        l85_1 = Input_EIA_Imports_Coal_Foreign.L85()
        var_1 = IFERROR(l85_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D85():
    # 'Coal_Foreign_Imports'!D85
    value = 57.449139375
    formula = '''=IFERROR(C85/B85,"")'''
    @eval_fn
    def D85():
        c85_1 = Coal_Foreign_Imports.C85()
        b85_1 = Coal_Foreign_Imports.B85()
        var_1 = divide(c85_1, b85_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A86():
    # 'Coal_Foreign_Imports'!A86
    value = 2014
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A86,"")'''
    @eval_fn
    def A86():
        a86_1 = Input_EIA_Imports_Coal_Foreign.A86()
        var_1 = IFERROR(a86_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B86():
    # 'Coal_Foreign_Imports'!B86
    value = 183238
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K86,"")'''
    @eval_fn
    def B86():
        k86_1 = Input_EIA_Imports_Coal_Foreign.K86()
        var_1 = IFERROR(k86_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C86():
    # 'Coal_Foreign_Imports'!C86
    value = 11722287
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L86,"")'''
    @eval_fn
    def C86():
        l86_1 = Input_EIA_Imports_Coal_Foreign.L86()
        var_1 = IFERROR(l86_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D86():
    # 'Coal_Foreign_Imports'!D86
    value = 63.9730132396
    formula = '''=IFERROR(C86/B86,"")'''
    @eval_fn
    def D86():
        c86_1 = Coal_Foreign_Imports.C86()
        b86_1 = Coal_Foreign_Imports.B86()
        var_1 = divide(c86_1, b86_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A87():
    # 'Coal_Foreign_Imports'!A87
    value = 2014
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A87,"")'''
    @eval_fn
    def A87():
        a87_1 = Input_EIA_Imports_Coal_Foreign.A87()
        var_1 = IFERROR(a87_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B87():
    # 'Coal_Foreign_Imports'!B87
    value = 178525
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K87,"")'''
    @eval_fn
    def B87():
        k87_1 = Input_EIA_Imports_Coal_Foreign.K87()
        var_1 = IFERROR(k87_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C87():
    # 'Coal_Foreign_Imports'!C87
    value = 11482729
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L87,"")'''
    @eval_fn
    def C87():
        l87_1 = Input_EIA_Imports_Coal_Foreign.L87()
        var_1 = IFERROR(l87_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D87():
    # 'Coal_Foreign_Imports'!D87
    value = 64.3200056015
    formula = '''=IFERROR(C87/B87,"")'''
    @eval_fn
    def D87():
        c87_1 = Coal_Foreign_Imports.C87()
        b87_1 = Coal_Foreign_Imports.B87()
        var_1 = divide(c87_1, b87_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A88():
    # 'Coal_Foreign_Imports'!A88
    value = 2014
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A88,"")'''
    @eval_fn
    def A88():
        a88_1 = Input_EIA_Imports_Coal_Foreign.A88()
        var_1 = IFERROR(a88_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B88():
    # 'Coal_Foreign_Imports'!B88
    value = 184083
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K88,"")'''
    @eval_fn
    def B88():
        k88_1 = Input_EIA_Imports_Coal_Foreign.K88()
        var_1 = IFERROR(k88_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C88():
    # 'Coal_Foreign_Imports'!C88
    value = 11673484
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L88,"")'''
    @eval_fn
    def C88():
        l88_1 = Input_EIA_Imports_Coal_Foreign.L88()
        var_1 = IFERROR(l88_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D88():
    # 'Coal_Foreign_Imports'!D88
    value = 63.4142424884
    formula = '''=IFERROR(C88/B88,"")'''
    @eval_fn
    def D88():
        c88_1 = Coal_Foreign_Imports.C88()
        b88_1 = Coal_Foreign_Imports.B88()
        var_1 = divide(c88_1, b88_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A89():
    # 'Coal_Foreign_Imports'!A89
    value = 2014
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A89,"")'''
    @eval_fn
    def A89():
        a89_1 = Input_EIA_Imports_Coal_Foreign.A89()
        var_1 = IFERROR(a89_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B89():
    # 'Coal_Foreign_Imports'!B89
    value = 179281
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K89,"")'''
    @eval_fn
    def B89():
        k89_1 = Input_EIA_Imports_Coal_Foreign.K89()
        var_1 = IFERROR(k89_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C89():
    # 'Coal_Foreign_Imports'!C89
    value = 11465355
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L89,"")'''
    @eval_fn
    def C89():
        l89_1 = Input_EIA_Imports_Coal_Foreign.L89()
        var_1 = IFERROR(l89_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D89():
    # 'Coal_Foreign_Imports'!D89
    value = 63.9518688539
    formula = '''=IFERROR(C89/B89,"")'''
    @eval_fn
    def D89():
        c89_1 = Coal_Foreign_Imports.C89()
        b89_1 = Coal_Foreign_Imports.B89()
        var_1 = divide(c89_1, b89_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A90():
    # 'Coal_Foreign_Imports'!A90
    value = 2015
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A90,"")'''
    @eval_fn
    def A90():
        a90_1 = Input_EIA_Imports_Coal_Foreign.A90()
        var_1 = IFERROR(a90_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B90():
    # 'Coal_Foreign_Imports'!B90
    value = 238083
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K90,"")'''
    @eval_fn
    def B90():
        k90_1 = Input_EIA_Imports_Coal_Foreign.K90()
        var_1 = IFERROR(k90_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C90():
    # 'Coal_Foreign_Imports'!C90
    value = 14722877
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L90,"")'''
    @eval_fn
    def C90():
        l90_1 = Input_EIA_Imports_Coal_Foreign.L90()
        var_1 = IFERROR(l90_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D90():
    # 'Coal_Foreign_Imports'!D90
    value = 61.8392619381
    formula = '''=IFERROR(C90/B90,"")'''
    @eval_fn
    def D90():
        c90_1 = Coal_Foreign_Imports.C90()
        b90_1 = Coal_Foreign_Imports.B90()
        var_1 = divide(c90_1, b90_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A91():
    # 'Coal_Foreign_Imports'!A91
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A91,"")'''
    @eval_fn
    def A91():
        a91_1 = Input_EIA_Imports_Coal_Foreign.A91()
        var_1 = IFERROR(a91_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B91():
    # 'Coal_Foreign_Imports'!B91
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K91,"")'''
    @eval_fn
    def B91():
        k91_1 = Input_EIA_Imports_Coal_Foreign.K91()
        var_1 = IFERROR(k91_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C91():
    # 'Coal_Foreign_Imports'!C91
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L91,"")'''
    @eval_fn
    def C91():
        l91_1 = Input_EIA_Imports_Coal_Foreign.L91()
        var_1 = IFERROR(l91_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D91():
    # 'Coal_Foreign_Imports'!D91
    value = None
    formula = '''=IFERROR(C91/B91,"")'''
    @eval_fn
    def D91():
        c91_1 = Coal_Foreign_Imports.C91()
        b91_1 = Coal_Foreign_Imports.B91()
        var_1 = divide(c91_1, b91_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A92():
    # 'Coal_Foreign_Imports'!A92
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A92,"")'''
    @eval_fn
    def A92():
        a92_1 = Input_EIA_Imports_Coal_Foreign.A92()
        var_1 = IFERROR(a92_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B92():
    # 'Coal_Foreign_Imports'!B92
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K92,"")'''
    @eval_fn
    def B92():
        k92_1 = Input_EIA_Imports_Coal_Foreign.K92()
        var_1 = IFERROR(k92_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C92():
    # 'Coal_Foreign_Imports'!C92
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L92,"")'''
    @eval_fn
    def C92():
        l92_1 = Input_EIA_Imports_Coal_Foreign.L92()
        var_1 = IFERROR(l92_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D92():
    # 'Coal_Foreign_Imports'!D92
    value = None
    formula = '''=IFERROR(C92/B92,"")'''
    @eval_fn
    def D92():
        c92_1 = Coal_Foreign_Imports.C92()
        b92_1 = Coal_Foreign_Imports.B92()
        var_1 = divide(c92_1, b92_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A93():
    # 'Coal_Foreign_Imports'!A93
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A93,"")'''
    @eval_fn
    def A93():
        a93_1 = Input_EIA_Imports_Coal_Foreign.A93()
        var_1 = IFERROR(a93_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B93():
    # 'Coal_Foreign_Imports'!B93
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K93,"")'''
    @eval_fn
    def B93():
        k93_1 = Input_EIA_Imports_Coal_Foreign.K93()
        var_1 = IFERROR(k93_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C93():
    # 'Coal_Foreign_Imports'!C93
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L93,"")'''
    @eval_fn
    def C93():
        l93_1 = Input_EIA_Imports_Coal_Foreign.L93()
        var_1 = IFERROR(l93_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D93():
    # 'Coal_Foreign_Imports'!D93
    value = None
    formula = '''=IFERROR(C93/B93,"")'''
    @eval_fn
    def D93():
        c93_1 = Coal_Foreign_Imports.C93()
        b93_1 = Coal_Foreign_Imports.B93()
        var_1 = divide(c93_1, b93_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A94():
    # 'Coal_Foreign_Imports'!A94
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A94,"")'''
    @eval_fn
    def A94():
        a94_1 = Input_EIA_Imports_Coal_Foreign.A94()
        var_1 = IFERROR(a94_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B94():
    # 'Coal_Foreign_Imports'!B94
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K94,"")'''
    @eval_fn
    def B94():
        k94_1 = Input_EIA_Imports_Coal_Foreign.K94()
        var_1 = IFERROR(k94_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C94():
    # 'Coal_Foreign_Imports'!C94
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L94,"")'''
    @eval_fn
    def C94():
        l94_1 = Input_EIA_Imports_Coal_Foreign.L94()
        var_1 = IFERROR(l94_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D94():
    # 'Coal_Foreign_Imports'!D94
    value = None
    formula = '''=IFERROR(C94/B94,"")'''
    @eval_fn
    def D94():
        c94_1 = Coal_Foreign_Imports.C94()
        b94_1 = Coal_Foreign_Imports.B94()
        var_1 = divide(c94_1, b94_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A95():
    # 'Coal_Foreign_Imports'!A95
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A95,"")'''
    @eval_fn
    def A95():
        a95_1 = Input_EIA_Imports_Coal_Foreign.A95()
        var_1 = IFERROR(a95_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B95():
    # 'Coal_Foreign_Imports'!B95
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K95,"")'''
    @eval_fn
    def B95():
        k95_1 = Input_EIA_Imports_Coal_Foreign.K95()
        var_1 = IFERROR(k95_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C95():
    # 'Coal_Foreign_Imports'!C95
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L95,"")'''
    @eval_fn
    def C95():
        l95_1 = Input_EIA_Imports_Coal_Foreign.L95()
        var_1 = IFERROR(l95_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D95():
    # 'Coal_Foreign_Imports'!D95
    value = None
    formula = '''=IFERROR(C95/B95,"")'''
    @eval_fn
    def D95():
        c95_1 = Coal_Foreign_Imports.C95()
        b95_1 = Coal_Foreign_Imports.B95()
        var_1 = divide(c95_1, b95_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A96():
    # 'Coal_Foreign_Imports'!A96
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A96,"")'''
    @eval_fn
    def A96():
        a96_1 = Input_EIA_Imports_Coal_Foreign.A96()
        var_1 = IFERROR(a96_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B96():
    # 'Coal_Foreign_Imports'!B96
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K96,"")'''
    @eval_fn
    def B96():
        k96_1 = Input_EIA_Imports_Coal_Foreign.K96()
        var_1 = IFERROR(k96_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C96():
    # 'Coal_Foreign_Imports'!C96
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L96,"")'''
    @eval_fn
    def C96():
        l96_1 = Input_EIA_Imports_Coal_Foreign.L96()
        var_1 = IFERROR(l96_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D96():
    # 'Coal_Foreign_Imports'!D96
    value = None
    formula = '''=IFERROR(C96/B96,"")'''
    @eval_fn
    def D96():
        c96_1 = Coal_Foreign_Imports.C96()
        b96_1 = Coal_Foreign_Imports.B96()
        var_1 = divide(c96_1, b96_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A97():
    # 'Coal_Foreign_Imports'!A97
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A97,"")'''
    @eval_fn
    def A97():
        a97_1 = Input_EIA_Imports_Coal_Foreign.A97()
        var_1 = IFERROR(a97_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B97():
    # 'Coal_Foreign_Imports'!B97
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K97,"")'''
    @eval_fn
    def B97():
        k97_1 = Input_EIA_Imports_Coal_Foreign.K97()
        var_1 = IFERROR(k97_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C97():
    # 'Coal_Foreign_Imports'!C97
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L97,"")'''
    @eval_fn
    def C97():
        l97_1 = Input_EIA_Imports_Coal_Foreign.L97()
        var_1 = IFERROR(l97_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D97():
    # 'Coal_Foreign_Imports'!D97
    value = None
    formula = '''=IFERROR(C97/B97,"")'''
    @eval_fn
    def D97():
        c97_1 = Coal_Foreign_Imports.C97()
        b97_1 = Coal_Foreign_Imports.B97()
        var_1 = divide(c97_1, b97_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A98():
    # 'Coal_Foreign_Imports'!A98
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A98,"")'''
    @eval_fn
    def A98():
        a98_1 = Input_EIA_Imports_Coal_Foreign.A98()
        var_1 = IFERROR(a98_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B98():
    # 'Coal_Foreign_Imports'!B98
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K98,"")'''
    @eval_fn
    def B98():
        k98_1 = Input_EIA_Imports_Coal_Foreign.K98()
        var_1 = IFERROR(k98_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C98():
    # 'Coal_Foreign_Imports'!C98
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L98,"")'''
    @eval_fn
    def C98():
        l98_1 = Input_EIA_Imports_Coal_Foreign.L98()
        var_1 = IFERROR(l98_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D98():
    # 'Coal_Foreign_Imports'!D98
    value = None
    formula = '''=IFERROR(C98/B98,"")'''
    @eval_fn
    def D98():
        c98_1 = Coal_Foreign_Imports.C98()
        b98_1 = Coal_Foreign_Imports.B98()
        var_1 = divide(c98_1, b98_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A99():
    # 'Coal_Foreign_Imports'!A99
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A99,"")'''
    @eval_fn
    def A99():
        a99_1 = Input_EIA_Imports_Coal_Foreign.A99()
        var_1 = IFERROR(a99_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B99():
    # 'Coal_Foreign_Imports'!B99
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K99,"")'''
    @eval_fn
    def B99():
        k99_1 = Input_EIA_Imports_Coal_Foreign.K99()
        var_1 = IFERROR(k99_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C99():
    # 'Coal_Foreign_Imports'!C99
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L99,"")'''
    @eval_fn
    def C99():
        l99_1 = Input_EIA_Imports_Coal_Foreign.L99()
        var_1 = IFERROR(l99_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D99():
    # 'Coal_Foreign_Imports'!D99
    value = None
    formula = '''=IFERROR(C99/B99,"")'''
    @eval_fn
    def D99():
        c99_1 = Coal_Foreign_Imports.C99()
        b99_1 = Coal_Foreign_Imports.B99()
        var_1 = divide(c99_1, b99_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A100():
    # 'Coal_Foreign_Imports'!A100
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A100,"")'''
    @eval_fn
    def A100():
        a100_1 = Input_EIA_Imports_Coal_Foreign.A100()
        var_1 = IFERROR(a100_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B100():
    # 'Coal_Foreign_Imports'!B100
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K100,"")'''
    @eval_fn
    def B100():
        k100_1 = Input_EIA_Imports_Coal_Foreign.K100()
        var_1 = IFERROR(k100_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C100():
    # 'Coal_Foreign_Imports'!C100
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L100,"")'''
    @eval_fn
    def C100():
        l100_1 = Input_EIA_Imports_Coal_Foreign.L100()
        var_1 = IFERROR(l100_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D100():
    # 'Coal_Foreign_Imports'!D100
    value = None
    formula = '''=IFERROR(C100/B100,"")'''
    @eval_fn
    def D100():
        c100_1 = Coal_Foreign_Imports.C100()
        b100_1 = Coal_Foreign_Imports.B100()
        var_1 = divide(c100_1, b100_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A101():
    # 'Coal_Foreign_Imports'!A101
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A101,"")'''
    @eval_fn
    def A101():
        a101_1 = Input_EIA_Imports_Coal_Foreign.A101()
        var_1 = IFERROR(a101_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B101():
    # 'Coal_Foreign_Imports'!B101
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K101,"")'''
    @eval_fn
    def B101():
        k101_1 = Input_EIA_Imports_Coal_Foreign.K101()
        var_1 = IFERROR(k101_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C101():
    # 'Coal_Foreign_Imports'!C101
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L101,"")'''
    @eval_fn
    def C101():
        l101_1 = Input_EIA_Imports_Coal_Foreign.L101()
        var_1 = IFERROR(l101_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D101():
    # 'Coal_Foreign_Imports'!D101
    value = None
    formula = '''=IFERROR(C101/B101,"")'''
    @eval_fn
    def D101():
        c101_1 = Coal_Foreign_Imports.C101()
        b101_1 = Coal_Foreign_Imports.B101()
        var_1 = divide(c101_1, b101_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A102():
    # 'Coal_Foreign_Imports'!A102
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A102,"")'''
    @eval_fn
    def A102():
        a102_1 = Input_EIA_Imports_Coal_Foreign.A102()
        var_1 = IFERROR(a102_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B102():
    # 'Coal_Foreign_Imports'!B102
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K102,"")'''
    @eval_fn
    def B102():
        k102_1 = Input_EIA_Imports_Coal_Foreign.K102()
        var_1 = IFERROR(k102_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C102():
    # 'Coal_Foreign_Imports'!C102
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L102,"")'''
    @eval_fn
    def C102():
        l102_1 = Input_EIA_Imports_Coal_Foreign.L102()
        var_1 = IFERROR(l102_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D102():
    # 'Coal_Foreign_Imports'!D102
    value = None
    formula = '''=IFERROR(C102/B102,"")'''
    @eval_fn
    def D102():
        c102_1 = Coal_Foreign_Imports.C102()
        b102_1 = Coal_Foreign_Imports.B102()
        var_1 = divide(c102_1, b102_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A103():
    # 'Coal_Foreign_Imports'!A103
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A103,"")'''
    @eval_fn
    def A103():
        a103_1 = Input_EIA_Imports_Coal_Foreign.A103()
        var_1 = IFERROR(a103_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B103():
    # 'Coal_Foreign_Imports'!B103
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K103,"")'''
    @eval_fn
    def B103():
        k103_1 = Input_EIA_Imports_Coal_Foreign.K103()
        var_1 = IFERROR(k103_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C103():
    # 'Coal_Foreign_Imports'!C103
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L103,"")'''
    @eval_fn
    def C103():
        l103_1 = Input_EIA_Imports_Coal_Foreign.L103()
        var_1 = IFERROR(l103_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D103():
    # 'Coal_Foreign_Imports'!D103
    value = None
    formula = '''=IFERROR(C103/B103,"")'''
    @eval_fn
    def D103():
        c103_1 = Coal_Foreign_Imports.C103()
        b103_1 = Coal_Foreign_Imports.B103()
        var_1 = divide(c103_1, b103_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A104():
    # 'Coal_Foreign_Imports'!A104
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A104,"")'''
    @eval_fn
    def A104():
        a104_1 = Input_EIA_Imports_Coal_Foreign.A104()
        var_1 = IFERROR(a104_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B104():
    # 'Coal_Foreign_Imports'!B104
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K104,"")'''
    @eval_fn
    def B104():
        k104_1 = Input_EIA_Imports_Coal_Foreign.K104()
        var_1 = IFERROR(k104_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C104():
    # 'Coal_Foreign_Imports'!C104
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L104,"")'''
    @eval_fn
    def C104():
        l104_1 = Input_EIA_Imports_Coal_Foreign.L104()
        var_1 = IFERROR(l104_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D104():
    # 'Coal_Foreign_Imports'!D104
    value = None
    formula = '''=IFERROR(C104/B104,"")'''
    @eval_fn
    def D104():
        c104_1 = Coal_Foreign_Imports.C104()
        b104_1 = Coal_Foreign_Imports.B104()
        var_1 = divide(c104_1, b104_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A105():
    # 'Coal_Foreign_Imports'!A105
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A105,"")'''
    @eval_fn
    def A105():
        a105_1 = Input_EIA_Imports_Coal_Foreign.A105()
        var_1 = IFERROR(a105_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B105():
    # 'Coal_Foreign_Imports'!B105
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K105,"")'''
    @eval_fn
    def B105():
        k105_1 = Input_EIA_Imports_Coal_Foreign.K105()
        var_1 = IFERROR(k105_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C105():
    # 'Coal_Foreign_Imports'!C105
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L105,"")'''
    @eval_fn
    def C105():
        l105_1 = Input_EIA_Imports_Coal_Foreign.L105()
        var_1 = IFERROR(l105_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D105():
    # 'Coal_Foreign_Imports'!D105
    value = None
    formula = '''=IFERROR(C105/B105,"")'''
    @eval_fn
    def D105():
        c105_1 = Coal_Foreign_Imports.C105()
        b105_1 = Coal_Foreign_Imports.B105()
        var_1 = divide(c105_1, b105_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A106():
    # 'Coal_Foreign_Imports'!A106
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A106,"")'''
    @eval_fn
    def A106():
        a106_1 = Input_EIA_Imports_Coal_Foreign.A106()
        var_1 = IFERROR(a106_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B106():
    # 'Coal_Foreign_Imports'!B106
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K106,"")'''
    @eval_fn
    def B106():
        k106_1 = Input_EIA_Imports_Coal_Foreign.K106()
        var_1 = IFERROR(k106_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C106():
    # 'Coal_Foreign_Imports'!C106
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L106,"")'''
    @eval_fn
    def C106():
        l106_1 = Input_EIA_Imports_Coal_Foreign.L106()
        var_1 = IFERROR(l106_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D106():
    # 'Coal_Foreign_Imports'!D106
    value = None
    formula = '''=IFERROR(C106/B106,"")'''
    @eval_fn
    def D106():
        c106_1 = Coal_Foreign_Imports.C106()
        b106_1 = Coal_Foreign_Imports.B106()
        var_1 = divide(c106_1, b106_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A107():
    # 'Coal_Foreign_Imports'!A107
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A107,"")'''
    @eval_fn
    def A107():
        a107_1 = Input_EIA_Imports_Coal_Foreign.A107()
        var_1 = IFERROR(a107_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B107():
    # 'Coal_Foreign_Imports'!B107
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K107,"")'''
    @eval_fn
    def B107():
        k107_1 = Input_EIA_Imports_Coal_Foreign.K107()
        var_1 = IFERROR(k107_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C107():
    # 'Coal_Foreign_Imports'!C107
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L107,"")'''
    @eval_fn
    def C107():
        l107_1 = Input_EIA_Imports_Coal_Foreign.L107()
        var_1 = IFERROR(l107_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D107():
    # 'Coal_Foreign_Imports'!D107
    value = None
    formula = '''=IFERROR(C107/B107,"")'''
    @eval_fn
    def D107():
        c107_1 = Coal_Foreign_Imports.C107()
        b107_1 = Coal_Foreign_Imports.B107()
        var_1 = divide(c107_1, b107_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A108():
    # 'Coal_Foreign_Imports'!A108
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A108,"")'''
    @eval_fn
    def A108():
        a108_1 = Input_EIA_Imports_Coal_Foreign.A108()
        var_1 = IFERROR(a108_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B108():
    # 'Coal_Foreign_Imports'!B108
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K108,"")'''
    @eval_fn
    def B108():
        k108_1 = Input_EIA_Imports_Coal_Foreign.K108()
        var_1 = IFERROR(k108_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C108():
    # 'Coal_Foreign_Imports'!C108
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L108,"")'''
    @eval_fn
    def C108():
        l108_1 = Input_EIA_Imports_Coal_Foreign.L108()
        var_1 = IFERROR(l108_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D108():
    # 'Coal_Foreign_Imports'!D108
    value = None
    formula = '''=IFERROR(C108/B108,"")'''
    @eval_fn
    def D108():
        c108_1 = Coal_Foreign_Imports.C108()
        b108_1 = Coal_Foreign_Imports.B108()
        var_1 = divide(c108_1, b108_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A109():
    # 'Coal_Foreign_Imports'!A109
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A109,"")'''
    @eval_fn
    def A109():
        a109_1 = Input_EIA_Imports_Coal_Foreign.A109()
        var_1 = IFERROR(a109_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B109():
    # 'Coal_Foreign_Imports'!B109
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K109,"")'''
    @eval_fn
    def B109():
        k109_1 = Input_EIA_Imports_Coal_Foreign.K109()
        var_1 = IFERROR(k109_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C109():
    # 'Coal_Foreign_Imports'!C109
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L109,"")'''
    @eval_fn
    def C109():
        l109_1 = Input_EIA_Imports_Coal_Foreign.L109()
        var_1 = IFERROR(l109_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D109():
    # 'Coal_Foreign_Imports'!D109
    value = None
    formula = '''=IFERROR(C109/B109,"")'''
    @eval_fn
    def D109():
        c109_1 = Coal_Foreign_Imports.C109()
        b109_1 = Coal_Foreign_Imports.B109()
        var_1 = divide(c109_1, b109_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A110():
    # 'Coal_Foreign_Imports'!A110
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A110,"")'''
    @eval_fn
    def A110():
        a110_1 = Input_EIA_Imports_Coal_Foreign.A110()
        var_1 = IFERROR(a110_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B110():
    # 'Coal_Foreign_Imports'!B110
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K110,"")'''
    @eval_fn
    def B110():
        k110_1 = Input_EIA_Imports_Coal_Foreign.K110()
        var_1 = IFERROR(k110_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C110():
    # 'Coal_Foreign_Imports'!C110
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L110,"")'''
    @eval_fn
    def C110():
        l110_1 = Input_EIA_Imports_Coal_Foreign.L110()
        var_1 = IFERROR(l110_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D110():
    # 'Coal_Foreign_Imports'!D110
    value = None
    formula = '''=IFERROR(C110/B110,"")'''
    @eval_fn
    def D110():
        c110_1 = Coal_Foreign_Imports.C110()
        b110_1 = Coal_Foreign_Imports.B110()
        var_1 = divide(c110_1, b110_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A111():
    # 'Coal_Foreign_Imports'!A111
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A111,"")'''
    @eval_fn
    def A111():
        a111_1 = Input_EIA_Imports_Coal_Foreign.A111()
        var_1 = IFERROR(a111_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B111():
    # 'Coal_Foreign_Imports'!B111
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K111,"")'''
    @eval_fn
    def B111():
        k111_1 = Input_EIA_Imports_Coal_Foreign.K111()
        var_1 = IFERROR(k111_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C111():
    # 'Coal_Foreign_Imports'!C111
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L111,"")'''
    @eval_fn
    def C111():
        l111_1 = Input_EIA_Imports_Coal_Foreign.L111()
        var_1 = IFERROR(l111_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D111():
    # 'Coal_Foreign_Imports'!D111
    value = None
    formula = '''=IFERROR(C111/B111,"")'''
    @eval_fn
    def D111():
        c111_1 = Coal_Foreign_Imports.C111()
        b111_1 = Coal_Foreign_Imports.B111()
        var_1 = divide(c111_1, b111_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A112():
    # 'Coal_Foreign_Imports'!A112
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A112,"")'''
    @eval_fn
    def A112():
        a112_1 = Input_EIA_Imports_Coal_Foreign.A112()
        var_1 = IFERROR(a112_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B112():
    # 'Coal_Foreign_Imports'!B112
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K112,"")'''
    @eval_fn
    def B112():
        k112_1 = Input_EIA_Imports_Coal_Foreign.K112()
        var_1 = IFERROR(k112_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C112():
    # 'Coal_Foreign_Imports'!C112
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L112,"")'''
    @eval_fn
    def C112():
        l112_1 = Input_EIA_Imports_Coal_Foreign.L112()
        var_1 = IFERROR(l112_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D112():
    # 'Coal_Foreign_Imports'!D112
    value = None
    formula = '''=IFERROR(C112/B112,"")'''
    @eval_fn
    def D112():
        c112_1 = Coal_Foreign_Imports.C112()
        b112_1 = Coal_Foreign_Imports.B112()
        var_1 = divide(c112_1, b112_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A113():
    # 'Coal_Foreign_Imports'!A113
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A113,"")'''
    @eval_fn
    def A113():
        a113_1 = Input_EIA_Imports_Coal_Foreign.A113()
        var_1 = IFERROR(a113_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B113():
    # 'Coal_Foreign_Imports'!B113
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K113,"")'''
    @eval_fn
    def B113():
        k113_1 = Input_EIA_Imports_Coal_Foreign.K113()
        var_1 = IFERROR(k113_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C113():
    # 'Coal_Foreign_Imports'!C113
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L113,"")'''
    @eval_fn
    def C113():
        l113_1 = Input_EIA_Imports_Coal_Foreign.L113()
        var_1 = IFERROR(l113_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D113():
    # 'Coal_Foreign_Imports'!D113
    value = None
    formula = '''=IFERROR(C113/B113,"")'''
    @eval_fn
    def D113():
        c113_1 = Coal_Foreign_Imports.C113()
        b113_1 = Coal_Foreign_Imports.B113()
        var_1 = divide(c113_1, b113_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A114():
    # 'Coal_Foreign_Imports'!A114
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A114,"")'''
    @eval_fn
    def A114():
        a114_1 = Input_EIA_Imports_Coal_Foreign.A114()
        var_1 = IFERROR(a114_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B114():
    # 'Coal_Foreign_Imports'!B114
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K114,"")'''
    @eval_fn
    def B114():
        k114_1 = Input_EIA_Imports_Coal_Foreign.K114()
        var_1 = IFERROR(k114_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C114():
    # 'Coal_Foreign_Imports'!C114
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L114,"")'''
    @eval_fn
    def C114():
        l114_1 = Input_EIA_Imports_Coal_Foreign.L114()
        var_1 = IFERROR(l114_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D114():
    # 'Coal_Foreign_Imports'!D114
    value = None
    formula = '''=IFERROR(C114/B114,"")'''
    @eval_fn
    def D114():
        c114_1 = Coal_Foreign_Imports.C114()
        b114_1 = Coal_Foreign_Imports.B114()
        var_1 = divide(c114_1, b114_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A115():
    # 'Coal_Foreign_Imports'!A115
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A115,"")'''
    @eval_fn
    def A115():
        a115_1 = Input_EIA_Imports_Coal_Foreign.A115()
        var_1 = IFERROR(a115_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B115():
    # 'Coal_Foreign_Imports'!B115
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K115,"")'''
    @eval_fn
    def B115():
        k115_1 = Input_EIA_Imports_Coal_Foreign.K115()
        var_1 = IFERROR(k115_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C115():
    # 'Coal_Foreign_Imports'!C115
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L115,"")'''
    @eval_fn
    def C115():
        l115_1 = Input_EIA_Imports_Coal_Foreign.L115()
        var_1 = IFERROR(l115_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D115():
    # 'Coal_Foreign_Imports'!D115
    value = None
    formula = '''=IFERROR(C115/B115,"")'''
    @eval_fn
    def D115():
        c115_1 = Coal_Foreign_Imports.C115()
        b115_1 = Coal_Foreign_Imports.B115()
        var_1 = divide(c115_1, b115_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A116():
    # 'Coal_Foreign_Imports'!A116
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A116,"")'''
    @eval_fn
    def A116():
        a116_1 = Input_EIA_Imports_Coal_Foreign.A116()
        var_1 = IFERROR(a116_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B116():
    # 'Coal_Foreign_Imports'!B116
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K116,"")'''
    @eval_fn
    def B116():
        k116_1 = Input_EIA_Imports_Coal_Foreign.K116()
        var_1 = IFERROR(k116_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C116():
    # 'Coal_Foreign_Imports'!C116
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L116,"")'''
    @eval_fn
    def C116():
        l116_1 = Input_EIA_Imports_Coal_Foreign.L116()
        var_1 = IFERROR(l116_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D116():
    # 'Coal_Foreign_Imports'!D116
    value = None
    formula = '''=IFERROR(C116/B116,"")'''
    @eval_fn
    def D116():
        c116_1 = Coal_Foreign_Imports.C116()
        b116_1 = Coal_Foreign_Imports.B116()
        var_1 = divide(c116_1, b116_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A117():
    # 'Coal_Foreign_Imports'!A117
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A117,"")'''
    @eval_fn
    def A117():
        a117_1 = Input_EIA_Imports_Coal_Foreign.A117()
        var_1 = IFERROR(a117_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B117():
    # 'Coal_Foreign_Imports'!B117
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K117,"")'''
    @eval_fn
    def B117():
        k117_1 = Input_EIA_Imports_Coal_Foreign.K117()
        var_1 = IFERROR(k117_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C117():
    # 'Coal_Foreign_Imports'!C117
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L117,"")'''
    @eval_fn
    def C117():
        l117_1 = Input_EIA_Imports_Coal_Foreign.L117()
        var_1 = IFERROR(l117_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D117():
    # 'Coal_Foreign_Imports'!D117
    value = None
    formula = '''=IFERROR(C117/B117,"")'''
    @eval_fn
    def D117():
        c117_1 = Coal_Foreign_Imports.C117()
        b117_1 = Coal_Foreign_Imports.B117()
        var_1 = divide(c117_1, b117_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A118():
    # 'Coal_Foreign_Imports'!A118
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A118,"")'''
    @eval_fn
    def A118():
        a118_1 = Input_EIA_Imports_Coal_Foreign.A118()
        var_1 = IFERROR(a118_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B118():
    # 'Coal_Foreign_Imports'!B118
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K118,"")'''
    @eval_fn
    def B118():
        k118_1 = Input_EIA_Imports_Coal_Foreign.K118()
        var_1 = IFERROR(k118_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C118():
    # 'Coal_Foreign_Imports'!C118
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L118,"")'''
    @eval_fn
    def C118():
        l118_1 = Input_EIA_Imports_Coal_Foreign.L118()
        var_1 = IFERROR(l118_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D118():
    # 'Coal_Foreign_Imports'!D118
    value = None
    formula = '''=IFERROR(C118/B118,"")'''
    @eval_fn
    def D118():
        c118_1 = Coal_Foreign_Imports.C118()
        b118_1 = Coal_Foreign_Imports.B118()
        var_1 = divide(c118_1, b118_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A119():
    # 'Coal_Foreign_Imports'!A119
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A119,"")'''
    @eval_fn
    def A119():
        a119_1 = Input_EIA_Imports_Coal_Foreign.A119()
        var_1 = IFERROR(a119_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B119():
    # 'Coal_Foreign_Imports'!B119
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K119,"")'''
    @eval_fn
    def B119():
        k119_1 = Input_EIA_Imports_Coal_Foreign.K119()
        var_1 = IFERROR(k119_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C119():
    # 'Coal_Foreign_Imports'!C119
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L119,"")'''
    @eval_fn
    def C119():
        l119_1 = Input_EIA_Imports_Coal_Foreign.L119()
        var_1 = IFERROR(l119_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D119():
    # 'Coal_Foreign_Imports'!D119
    value = None
    formula = '''=IFERROR(C119/B119,"")'''
    @eval_fn
    def D119():
        c119_1 = Coal_Foreign_Imports.C119()
        b119_1 = Coal_Foreign_Imports.B119()
        var_1 = divide(c119_1, b119_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A120():
    # 'Coal_Foreign_Imports'!A120
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A120,"")'''
    @eval_fn
    def A120():
        a120_1 = Input_EIA_Imports_Coal_Foreign.A120()
        var_1 = IFERROR(a120_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B120():
    # 'Coal_Foreign_Imports'!B120
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K120,"")'''
    @eval_fn
    def B120():
        k120_1 = Input_EIA_Imports_Coal_Foreign.K120()
        var_1 = IFERROR(k120_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C120():
    # 'Coal_Foreign_Imports'!C120
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L120,"")'''
    @eval_fn
    def C120():
        l120_1 = Input_EIA_Imports_Coal_Foreign.L120()
        var_1 = IFERROR(l120_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D120():
    # 'Coal_Foreign_Imports'!D120
    value = None
    formula = '''=IFERROR(C120/B120,"")'''
    @eval_fn
    def D120():
        c120_1 = Coal_Foreign_Imports.C120()
        b120_1 = Coal_Foreign_Imports.B120()
        var_1 = divide(c120_1, b120_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A121():
    # 'Coal_Foreign_Imports'!A121
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A121,"")'''
    @eval_fn
    def A121():
        a121_1 = Input_EIA_Imports_Coal_Foreign.A121()
        var_1 = IFERROR(a121_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B121():
    # 'Coal_Foreign_Imports'!B121
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K121,"")'''
    @eval_fn
    def B121():
        k121_1 = Input_EIA_Imports_Coal_Foreign.K121()
        var_1 = IFERROR(k121_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C121():
    # 'Coal_Foreign_Imports'!C121
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L121,"")'''
    @eval_fn
    def C121():
        l121_1 = Input_EIA_Imports_Coal_Foreign.L121()
        var_1 = IFERROR(l121_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D121():
    # 'Coal_Foreign_Imports'!D121
    value = None
    formula = '''=IFERROR(C121/B121,"")'''
    @eval_fn
    def D121():
        c121_1 = Coal_Foreign_Imports.C121()
        b121_1 = Coal_Foreign_Imports.B121()
        var_1 = divide(c121_1, b121_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A122():
    # 'Coal_Foreign_Imports'!A122
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A122,"")'''
    @eval_fn
    def A122():
        a122_1 = Input_EIA_Imports_Coal_Foreign.A122()
        var_1 = IFERROR(a122_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B122():
    # 'Coal_Foreign_Imports'!B122
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K122,"")'''
    @eval_fn
    def B122():
        k122_1 = Input_EIA_Imports_Coal_Foreign.K122()
        var_1 = IFERROR(k122_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C122():
    # 'Coal_Foreign_Imports'!C122
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L122,"")'''
    @eval_fn
    def C122():
        l122_1 = Input_EIA_Imports_Coal_Foreign.L122()
        var_1 = IFERROR(l122_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D122():
    # 'Coal_Foreign_Imports'!D122
    value = None
    formula = '''=IFERROR(C122/B122,"")'''
    @eval_fn
    def D122():
        c122_1 = Coal_Foreign_Imports.C122()
        b122_1 = Coal_Foreign_Imports.B122()
        var_1 = divide(c122_1, b122_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A123():
    # 'Coal_Foreign_Imports'!A123
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A123,"")'''
    @eval_fn
    def A123():
        a123_1 = Input_EIA_Imports_Coal_Foreign.A123()
        var_1 = IFERROR(a123_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B123():
    # 'Coal_Foreign_Imports'!B123
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K123,"")'''
    @eval_fn
    def B123():
        k123_1 = Input_EIA_Imports_Coal_Foreign.K123()
        var_1 = IFERROR(k123_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C123():
    # 'Coal_Foreign_Imports'!C123
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L123,"")'''
    @eval_fn
    def C123():
        l123_1 = Input_EIA_Imports_Coal_Foreign.L123()
        var_1 = IFERROR(l123_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D123():
    # 'Coal_Foreign_Imports'!D123
    value = None
    formula = '''=IFERROR(C123/B123,"")'''
    @eval_fn
    def D123():
        c123_1 = Coal_Foreign_Imports.C123()
        b123_1 = Coal_Foreign_Imports.B123()
        var_1 = divide(c123_1, b123_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A124():
    # 'Coal_Foreign_Imports'!A124
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A124,"")'''
    @eval_fn
    def A124():
        a124_1 = Input_EIA_Imports_Coal_Foreign.A124()
        var_1 = IFERROR(a124_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B124():
    # 'Coal_Foreign_Imports'!B124
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K124,"")'''
    @eval_fn
    def B124():
        k124_1 = Input_EIA_Imports_Coal_Foreign.K124()
        var_1 = IFERROR(k124_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C124():
    # 'Coal_Foreign_Imports'!C124
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L124,"")'''
    @eval_fn
    def C124():
        l124_1 = Input_EIA_Imports_Coal_Foreign.L124()
        var_1 = IFERROR(l124_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D124():
    # 'Coal_Foreign_Imports'!D124
    value = None
    formula = '''=IFERROR(C124/B124,"")'''
    @eval_fn
    def D124():
        c124_1 = Coal_Foreign_Imports.C124()
        b124_1 = Coal_Foreign_Imports.B124()
        var_1 = divide(c124_1, b124_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A125():
    # 'Coal_Foreign_Imports'!A125
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A125,"")'''
    @eval_fn
    def A125():
        a125_1 = Input_EIA_Imports_Coal_Foreign.A125()
        var_1 = IFERROR(a125_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B125():
    # 'Coal_Foreign_Imports'!B125
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K125,"")'''
    @eval_fn
    def B125():
        k125_1 = Input_EIA_Imports_Coal_Foreign.K125()
        var_1 = IFERROR(k125_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C125():
    # 'Coal_Foreign_Imports'!C125
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L125,"")'''
    @eval_fn
    def C125():
        l125_1 = Input_EIA_Imports_Coal_Foreign.L125()
        var_1 = IFERROR(l125_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D125():
    # 'Coal_Foreign_Imports'!D125
    value = None
    formula = '''=IFERROR(C125/B125,"")'''
    @eval_fn
    def D125():
        c125_1 = Coal_Foreign_Imports.C125()
        b125_1 = Coal_Foreign_Imports.B125()
        var_1 = divide(c125_1, b125_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A126():
    # 'Coal_Foreign_Imports'!A126
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A126,"")'''
    @eval_fn
    def A126():
        a126_1 = Input_EIA_Imports_Coal_Foreign.A126()
        var_1 = IFERROR(a126_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B126():
    # 'Coal_Foreign_Imports'!B126
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K126,"")'''
    @eval_fn
    def B126():
        k126_1 = Input_EIA_Imports_Coal_Foreign.K126()
        var_1 = IFERROR(k126_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C126():
    # 'Coal_Foreign_Imports'!C126
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L126,"")'''
    @eval_fn
    def C126():
        l126_1 = Input_EIA_Imports_Coal_Foreign.L126()
        var_1 = IFERROR(l126_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D126():
    # 'Coal_Foreign_Imports'!D126
    value = None
    formula = '''=IFERROR(C126/B126,"")'''
    @eval_fn
    def D126():
        c126_1 = Coal_Foreign_Imports.C126()
        b126_1 = Coal_Foreign_Imports.B126()
        var_1 = divide(c126_1, b126_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A127():
    # 'Coal_Foreign_Imports'!A127
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A127,"")'''
    @eval_fn
    def A127():
        a127_1 = Input_EIA_Imports_Coal_Foreign.A127()
        var_1 = IFERROR(a127_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B127():
    # 'Coal_Foreign_Imports'!B127
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K127,"")'''
    @eval_fn
    def B127():
        k127_1 = Input_EIA_Imports_Coal_Foreign.K127()
        var_1 = IFERROR(k127_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C127():
    # 'Coal_Foreign_Imports'!C127
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L127,"")'''
    @eval_fn
    def C127():
        l127_1 = Input_EIA_Imports_Coal_Foreign.L127()
        var_1 = IFERROR(l127_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D127():
    # 'Coal_Foreign_Imports'!D127
    value = None
    formula = '''=IFERROR(C127/B127,"")'''
    @eval_fn
    def D127():
        c127_1 = Coal_Foreign_Imports.C127()
        b127_1 = Coal_Foreign_Imports.B127()
        var_1 = divide(c127_1, b127_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A128():
    # 'Coal_Foreign_Imports'!A128
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A128,"")'''
    @eval_fn
    def A128():
        a128_1 = Input_EIA_Imports_Coal_Foreign.A128()
        var_1 = IFERROR(a128_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B128():
    # 'Coal_Foreign_Imports'!B128
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K128,"")'''
    @eval_fn
    def B128():
        k128_1 = Input_EIA_Imports_Coal_Foreign.K128()
        var_1 = IFERROR(k128_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C128():
    # 'Coal_Foreign_Imports'!C128
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L128,"")'''
    @eval_fn
    def C128():
        l128_1 = Input_EIA_Imports_Coal_Foreign.L128()
        var_1 = IFERROR(l128_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D128():
    # 'Coal_Foreign_Imports'!D128
    value = None
    formula = '''=IFERROR(C128/B128,"")'''
    @eval_fn
    def D128():
        c128_1 = Coal_Foreign_Imports.C128()
        b128_1 = Coal_Foreign_Imports.B128()
        var_1 = divide(c128_1, b128_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A129():
    # 'Coal_Foreign_Imports'!A129
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A129,"")'''
    @eval_fn
    def A129():
        a129_1 = Input_EIA_Imports_Coal_Foreign.A129()
        var_1 = IFERROR(a129_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B129():
    # 'Coal_Foreign_Imports'!B129
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K129,"")'''
    @eval_fn
    def B129():
        k129_1 = Input_EIA_Imports_Coal_Foreign.K129()
        var_1 = IFERROR(k129_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C129():
    # 'Coal_Foreign_Imports'!C129
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L129,"")'''
    @eval_fn
    def C129():
        l129_1 = Input_EIA_Imports_Coal_Foreign.L129()
        var_1 = IFERROR(l129_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D129():
    # 'Coal_Foreign_Imports'!D129
    value = None
    formula = '''=IFERROR(C129/B129,"")'''
    @eval_fn
    def D129():
        c129_1 = Coal_Foreign_Imports.C129()
        b129_1 = Coal_Foreign_Imports.B129()
        var_1 = divide(c129_1, b129_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A130():
    # 'Coal_Foreign_Imports'!A130
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A130,"")'''
    @eval_fn
    def A130():
        a130_1 = Input_EIA_Imports_Coal_Foreign.A130()
        var_1 = IFERROR(a130_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B130():
    # 'Coal_Foreign_Imports'!B130
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K130,"")'''
    @eval_fn
    def B130():
        k130_1 = Input_EIA_Imports_Coal_Foreign.K130()
        var_1 = IFERROR(k130_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C130():
    # 'Coal_Foreign_Imports'!C130
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L130,"")'''
    @eval_fn
    def C130():
        l130_1 = Input_EIA_Imports_Coal_Foreign.L130()
        var_1 = IFERROR(l130_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D130():
    # 'Coal_Foreign_Imports'!D130
    value = None
    formula = '''=IFERROR(C130/B130,"")'''
    @eval_fn
    def D130():
        c130_1 = Coal_Foreign_Imports.C130()
        b130_1 = Coal_Foreign_Imports.B130()
        var_1 = divide(c130_1, b130_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A131():
    # 'Coal_Foreign_Imports'!A131
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A131,"")'''
    @eval_fn
    def A131():
        a131_1 = Input_EIA_Imports_Coal_Foreign.A131()
        var_1 = IFERROR(a131_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B131():
    # 'Coal_Foreign_Imports'!B131
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K131,"")'''
    @eval_fn
    def B131():
        k131_1 = Input_EIA_Imports_Coal_Foreign.K131()
        var_1 = IFERROR(k131_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C131():
    # 'Coal_Foreign_Imports'!C131
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L131,"")'''
    @eval_fn
    def C131():
        l131_1 = Input_EIA_Imports_Coal_Foreign.L131()
        var_1 = IFERROR(l131_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D131():
    # 'Coal_Foreign_Imports'!D131
    value = None
    formula = '''=IFERROR(C131/B131,"")'''
    @eval_fn
    def D131():
        c131_1 = Coal_Foreign_Imports.C131()
        b131_1 = Coal_Foreign_Imports.B131()
        var_1 = divide(c131_1, b131_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A132():
    # 'Coal_Foreign_Imports'!A132
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A132,"")'''
    @eval_fn
    def A132():
        a132_1 = Input_EIA_Imports_Coal_Foreign.A132()
        var_1 = IFERROR(a132_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B132():
    # 'Coal_Foreign_Imports'!B132
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K132,"")'''
    @eval_fn
    def B132():
        k132_1 = Input_EIA_Imports_Coal_Foreign.K132()
        var_1 = IFERROR(k132_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C132():
    # 'Coal_Foreign_Imports'!C132
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L132,"")'''
    @eval_fn
    def C132():
        l132_1 = Input_EIA_Imports_Coal_Foreign.L132()
        var_1 = IFERROR(l132_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D132():
    # 'Coal_Foreign_Imports'!D132
    value = None
    formula = '''=IFERROR(C132/B132,"")'''
    @eval_fn
    def D132():
        c132_1 = Coal_Foreign_Imports.C132()
        b132_1 = Coal_Foreign_Imports.B132()
        var_1 = divide(c132_1, b132_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A133():
    # 'Coal_Foreign_Imports'!A133
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A133,"")'''
    @eval_fn
    def A133():
        a133_1 = Input_EIA_Imports_Coal_Foreign.A133()
        var_1 = IFERROR(a133_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B133():
    # 'Coal_Foreign_Imports'!B133
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K133,"")'''
    @eval_fn
    def B133():
        k133_1 = Input_EIA_Imports_Coal_Foreign.K133()
        var_1 = IFERROR(k133_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C133():
    # 'Coal_Foreign_Imports'!C133
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L133,"")'''
    @eval_fn
    def C133():
        l133_1 = Input_EIA_Imports_Coal_Foreign.L133()
        var_1 = IFERROR(l133_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D133():
    # 'Coal_Foreign_Imports'!D133
    value = None
    formula = '''=IFERROR(C133/B133,"")'''
    @eval_fn
    def D133():
        c133_1 = Coal_Foreign_Imports.C133()
        b133_1 = Coal_Foreign_Imports.B133()
        var_1 = divide(c133_1, b133_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A134():
    # 'Coal_Foreign_Imports'!A134
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A134,"")'''
    @eval_fn
    def A134():
        a134_1 = Input_EIA_Imports_Coal_Foreign.A134()
        var_1 = IFERROR(a134_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B134():
    # 'Coal_Foreign_Imports'!B134
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K134,"")'''
    @eval_fn
    def B134():
        k134_1 = Input_EIA_Imports_Coal_Foreign.K134()
        var_1 = IFERROR(k134_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C134():
    # 'Coal_Foreign_Imports'!C134
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L134,"")'''
    @eval_fn
    def C134():
        l134_1 = Input_EIA_Imports_Coal_Foreign.L134()
        var_1 = IFERROR(l134_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D134():
    # 'Coal_Foreign_Imports'!D134
    value = None
    formula = '''=IFERROR(C134/B134,"")'''
    @eval_fn
    def D134():
        c134_1 = Coal_Foreign_Imports.C134()
        b134_1 = Coal_Foreign_Imports.B134()
        var_1 = divide(c134_1, b134_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A135():
    # 'Coal_Foreign_Imports'!A135
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A135,"")'''
    @eval_fn
    def A135():
        a135_1 = Input_EIA_Imports_Coal_Foreign.A135()
        var_1 = IFERROR(a135_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B135():
    # 'Coal_Foreign_Imports'!B135
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K135,"")'''
    @eval_fn
    def B135():
        k135_1 = Input_EIA_Imports_Coal_Foreign.K135()
        var_1 = IFERROR(k135_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C135():
    # 'Coal_Foreign_Imports'!C135
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L135,"")'''
    @eval_fn
    def C135():
        l135_1 = Input_EIA_Imports_Coal_Foreign.L135()
        var_1 = IFERROR(l135_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D135():
    # 'Coal_Foreign_Imports'!D135
    value = None
    formula = '''=IFERROR(C135/B135,"")'''
    @eval_fn
    def D135():
        c135_1 = Coal_Foreign_Imports.C135()
        b135_1 = Coal_Foreign_Imports.B135()
        var_1 = divide(c135_1, b135_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A136():
    # 'Coal_Foreign_Imports'!A136
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A136,"")'''
    @eval_fn
    def A136():
        a136_1 = Input_EIA_Imports_Coal_Foreign.A136()
        var_1 = IFERROR(a136_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B136():
    # 'Coal_Foreign_Imports'!B136
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K136,"")'''
    @eval_fn
    def B136():
        k136_1 = Input_EIA_Imports_Coal_Foreign.K136()
        var_1 = IFERROR(k136_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C136():
    # 'Coal_Foreign_Imports'!C136
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L136,"")'''
    @eval_fn
    def C136():
        l136_1 = Input_EIA_Imports_Coal_Foreign.L136()
        var_1 = IFERROR(l136_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D136():
    # 'Coal_Foreign_Imports'!D136
    value = None
    formula = '''=IFERROR(C136/B136,"")'''
    @eval_fn
    def D136():
        c136_1 = Coal_Foreign_Imports.C136()
        b136_1 = Coal_Foreign_Imports.B136()
        var_1 = divide(c136_1, b136_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A137():
    # 'Coal_Foreign_Imports'!A137
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A137,"")'''
    @eval_fn
    def A137():
        a137_1 = Input_EIA_Imports_Coal_Foreign.A137()
        var_1 = IFERROR(a137_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B137():
    # 'Coal_Foreign_Imports'!B137
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K137,"")'''
    @eval_fn
    def B137():
        k137_1 = Input_EIA_Imports_Coal_Foreign.K137()
        var_1 = IFERROR(k137_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C137():
    # 'Coal_Foreign_Imports'!C137
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L137,"")'''
    @eval_fn
    def C137():
        l137_1 = Input_EIA_Imports_Coal_Foreign.L137()
        var_1 = IFERROR(l137_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D137():
    # 'Coal_Foreign_Imports'!D137
    value = None
    formula = '''=IFERROR(C137/B137,"")'''
    @eval_fn
    def D137():
        c137_1 = Coal_Foreign_Imports.C137()
        b137_1 = Coal_Foreign_Imports.B137()
        var_1 = divide(c137_1, b137_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A138():
    # 'Coal_Foreign_Imports'!A138
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A138,"")'''
    @eval_fn
    def A138():
        a138_1 = Input_EIA_Imports_Coal_Foreign.A138()
        var_1 = IFERROR(a138_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B138():
    # 'Coal_Foreign_Imports'!B138
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K138,"")'''
    @eval_fn
    def B138():
        k138_1 = Input_EIA_Imports_Coal_Foreign.K138()
        var_1 = IFERROR(k138_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C138():
    # 'Coal_Foreign_Imports'!C138
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L138,"")'''
    @eval_fn
    def C138():
        l138_1 = Input_EIA_Imports_Coal_Foreign.L138()
        var_1 = IFERROR(l138_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D138():
    # 'Coal_Foreign_Imports'!D138
    value = None
    formula = '''=IFERROR(C138/B138,"")'''
    @eval_fn
    def D138():
        c138_1 = Coal_Foreign_Imports.C138()
        b138_1 = Coal_Foreign_Imports.B138()
        var_1 = divide(c138_1, b138_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A139():
    # 'Coal_Foreign_Imports'!A139
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A139,"")'''
    @eval_fn
    def A139():
        a139_1 = Input_EIA_Imports_Coal_Foreign.A139()
        var_1 = IFERROR(a139_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B139():
    # 'Coal_Foreign_Imports'!B139
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K139,"")'''
    @eval_fn
    def B139():
        k139_1 = Input_EIA_Imports_Coal_Foreign.K139()
        var_1 = IFERROR(k139_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C139():
    # 'Coal_Foreign_Imports'!C139
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L139,"")'''
    @eval_fn
    def C139():
        l139_1 = Input_EIA_Imports_Coal_Foreign.L139()
        var_1 = IFERROR(l139_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D139():
    # 'Coal_Foreign_Imports'!D139
    value = None
    formula = '''=IFERROR(C139/B139,"")'''
    @eval_fn
    def D139():
        c139_1 = Coal_Foreign_Imports.C139()
        b139_1 = Coal_Foreign_Imports.B139()
        var_1 = divide(c139_1, b139_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A140():
    # 'Coal_Foreign_Imports'!A140
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A140,"")'''
    @eval_fn
    def A140():
        a140_1 = Input_EIA_Imports_Coal_Foreign.A140()
        var_1 = IFERROR(a140_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B140():
    # 'Coal_Foreign_Imports'!B140
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K140,"")'''
    @eval_fn
    def B140():
        k140_1 = Input_EIA_Imports_Coal_Foreign.K140()
        var_1 = IFERROR(k140_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C140():
    # 'Coal_Foreign_Imports'!C140
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L140,"")'''
    @eval_fn
    def C140():
        l140_1 = Input_EIA_Imports_Coal_Foreign.L140()
        var_1 = IFERROR(l140_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D140():
    # 'Coal_Foreign_Imports'!D140
    value = None
    formula = '''=IFERROR(C140/B140,"")'''
    @eval_fn
    def D140():
        c140_1 = Coal_Foreign_Imports.C140()
        b140_1 = Coal_Foreign_Imports.B140()
        var_1 = divide(c140_1, b140_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A141():
    # 'Coal_Foreign_Imports'!A141
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A141,"")'''
    @eval_fn
    def A141():
        a141_1 = Input_EIA_Imports_Coal_Foreign.A141()
        var_1 = IFERROR(a141_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B141():
    # 'Coal_Foreign_Imports'!B141
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K141,"")'''
    @eval_fn
    def B141():
        k141_1 = Input_EIA_Imports_Coal_Foreign.K141()
        var_1 = IFERROR(k141_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C141():
    # 'Coal_Foreign_Imports'!C141
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L141,"")'''
    @eval_fn
    def C141():
        l141_1 = Input_EIA_Imports_Coal_Foreign.L141()
        var_1 = IFERROR(l141_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D141():
    # 'Coal_Foreign_Imports'!D141
    value = None
    formula = '''=IFERROR(C141/B141,"")'''
    @eval_fn
    def D141():
        c141_1 = Coal_Foreign_Imports.C141()
        b141_1 = Coal_Foreign_Imports.B141()
        var_1 = divide(c141_1, b141_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A142():
    # 'Coal_Foreign_Imports'!A142
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A142,"")'''
    @eval_fn
    def A142():
        a142_1 = Input_EIA_Imports_Coal_Foreign.A142()
        var_1 = IFERROR(a142_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B142():
    # 'Coal_Foreign_Imports'!B142
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K142,"")'''
    @eval_fn
    def B142():
        k142_1 = Input_EIA_Imports_Coal_Foreign.K142()
        var_1 = IFERROR(k142_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C142():
    # 'Coal_Foreign_Imports'!C142
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L142,"")'''
    @eval_fn
    def C142():
        l142_1 = Input_EIA_Imports_Coal_Foreign.L142()
        var_1 = IFERROR(l142_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D142():
    # 'Coal_Foreign_Imports'!D142
    value = None
    formula = '''=IFERROR(C142/B142,"")'''
    @eval_fn
    def D142():
        c142_1 = Coal_Foreign_Imports.C142()
        b142_1 = Coal_Foreign_Imports.B142()
        var_1 = divide(c142_1, b142_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A143():
    # 'Coal_Foreign_Imports'!A143
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A143,"")'''
    @eval_fn
    def A143():
        a143_1 = Input_EIA_Imports_Coal_Foreign.A143()
        var_1 = IFERROR(a143_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B143():
    # 'Coal_Foreign_Imports'!B143
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K143,"")'''
    @eval_fn
    def B143():
        k143_1 = Input_EIA_Imports_Coal_Foreign.K143()
        var_1 = IFERROR(k143_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C143():
    # 'Coal_Foreign_Imports'!C143
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L143,"")'''
    @eval_fn
    def C143():
        l143_1 = Input_EIA_Imports_Coal_Foreign.L143()
        var_1 = IFERROR(l143_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D143():
    # 'Coal_Foreign_Imports'!D143
    value = None
    formula = '''=IFERROR(C143/B143,"")'''
    @eval_fn
    def D143():
        c143_1 = Coal_Foreign_Imports.C143()
        b143_1 = Coal_Foreign_Imports.B143()
        var_1 = divide(c143_1, b143_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A144():
    # 'Coal_Foreign_Imports'!A144
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A144,"")'''
    @eval_fn
    def A144():
        a144_1 = Input_EIA_Imports_Coal_Foreign.A144()
        var_1 = IFERROR(a144_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B144():
    # 'Coal_Foreign_Imports'!B144
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K144,"")'''
    @eval_fn
    def B144():
        k144_1 = Input_EIA_Imports_Coal_Foreign.K144()
        var_1 = IFERROR(k144_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C144():
    # 'Coal_Foreign_Imports'!C144
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L144,"")'''
    @eval_fn
    def C144():
        l144_1 = Input_EIA_Imports_Coal_Foreign.L144()
        var_1 = IFERROR(l144_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D144():
    # 'Coal_Foreign_Imports'!D144
    value = None
    formula = '''=IFERROR(C144/B144,"")'''
    @eval_fn
    def D144():
        c144_1 = Coal_Foreign_Imports.C144()
        b144_1 = Coal_Foreign_Imports.B144()
        var_1 = divide(c144_1, b144_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A145():
    # 'Coal_Foreign_Imports'!A145
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A145,"")'''
    @eval_fn
    def A145():
        a145_1 = Input_EIA_Imports_Coal_Foreign.A145()
        var_1 = IFERROR(a145_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B145():
    # 'Coal_Foreign_Imports'!B145
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K145,"")'''
    @eval_fn
    def B145():
        k145_1 = Input_EIA_Imports_Coal_Foreign.K145()
        var_1 = IFERROR(k145_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C145():
    # 'Coal_Foreign_Imports'!C145
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L145,"")'''
    @eval_fn
    def C145():
        l145_1 = Input_EIA_Imports_Coal_Foreign.L145()
        var_1 = IFERROR(l145_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D145():
    # 'Coal_Foreign_Imports'!D145
    value = None
    formula = '''=IFERROR(C145/B145,"")'''
    @eval_fn
    def D145():
        c145_1 = Coal_Foreign_Imports.C145()
        b145_1 = Coal_Foreign_Imports.B145()
        var_1 = divide(c145_1, b145_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A146():
    # 'Coal_Foreign_Imports'!A146
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A146,"")'''
    @eval_fn
    def A146():
        a146_1 = Input_EIA_Imports_Coal_Foreign.A146()
        var_1 = IFERROR(a146_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B146():
    # 'Coal_Foreign_Imports'!B146
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K146,"")'''
    @eval_fn
    def B146():
        k146_1 = Input_EIA_Imports_Coal_Foreign.K146()
        var_1 = IFERROR(k146_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C146():
    # 'Coal_Foreign_Imports'!C146
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L146,"")'''
    @eval_fn
    def C146():
        l146_1 = Input_EIA_Imports_Coal_Foreign.L146()
        var_1 = IFERROR(l146_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D146():
    # 'Coal_Foreign_Imports'!D146
    value = None
    formula = '''=IFERROR(C146/B146,"")'''
    @eval_fn
    def D146():
        c146_1 = Coal_Foreign_Imports.C146()
        b146_1 = Coal_Foreign_Imports.B146()
        var_1 = divide(c146_1, b146_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A147():
    # 'Coal_Foreign_Imports'!A147
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A147,"")'''
    @eval_fn
    def A147():
        a147_1 = Input_EIA_Imports_Coal_Foreign.A147()
        var_1 = IFERROR(a147_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B147():
    # 'Coal_Foreign_Imports'!B147
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K147,"")'''
    @eval_fn
    def B147():
        k147_1 = Input_EIA_Imports_Coal_Foreign.K147()
        var_1 = IFERROR(k147_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C147():
    # 'Coal_Foreign_Imports'!C147
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L147,"")'''
    @eval_fn
    def C147():
        l147_1 = Input_EIA_Imports_Coal_Foreign.L147()
        var_1 = IFERROR(l147_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D147():
    # 'Coal_Foreign_Imports'!D147
    value = None
    formula = '''=IFERROR(C147/B147,"")'''
    @eval_fn
    def D147():
        c147_1 = Coal_Foreign_Imports.C147()
        b147_1 = Coal_Foreign_Imports.B147()
        var_1 = divide(c147_1, b147_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A148():
    # 'Coal_Foreign_Imports'!A148
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A148,"")'''
    @eval_fn
    def A148():
        a148_1 = Input_EIA_Imports_Coal_Foreign.A148()
        var_1 = IFERROR(a148_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B148():
    # 'Coal_Foreign_Imports'!B148
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K148,"")'''
    @eval_fn
    def B148():
        k148_1 = Input_EIA_Imports_Coal_Foreign.K148()
        var_1 = IFERROR(k148_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C148():
    # 'Coal_Foreign_Imports'!C148
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L148,"")'''
    @eval_fn
    def C148():
        l148_1 = Input_EIA_Imports_Coal_Foreign.L148()
        var_1 = IFERROR(l148_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D148():
    # 'Coal_Foreign_Imports'!D148
    value = None
    formula = '''=IFERROR(C148/B148,"")'''
    @eval_fn
    def D148():
        c148_1 = Coal_Foreign_Imports.C148()
        b148_1 = Coal_Foreign_Imports.B148()
        var_1 = divide(c148_1, b148_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A149():
    # 'Coal_Foreign_Imports'!A149
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A149,"")'''
    @eval_fn
    def A149():
        a149_1 = Input_EIA_Imports_Coal_Foreign.A149()
        var_1 = IFERROR(a149_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B149():
    # 'Coal_Foreign_Imports'!B149
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K149,"")'''
    @eval_fn
    def B149():
        k149_1 = Input_EIA_Imports_Coal_Foreign.K149()
        var_1 = IFERROR(k149_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C149():
    # 'Coal_Foreign_Imports'!C149
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L149,"")'''
    @eval_fn
    def C149():
        l149_1 = Input_EIA_Imports_Coal_Foreign.L149()
        var_1 = IFERROR(l149_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D149():
    # 'Coal_Foreign_Imports'!D149
    value = None
    formula = '''=IFERROR(C149/B149,"")'''
    @eval_fn
    def D149():
        c149_1 = Coal_Foreign_Imports.C149()
        b149_1 = Coal_Foreign_Imports.B149()
        var_1 = divide(c149_1, b149_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A150():
    # 'Coal_Foreign_Imports'!A150
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A150,"")'''
    @eval_fn
    def A150():
        a150_1 = Input_EIA_Imports_Coal_Foreign.A150()
        var_1 = IFERROR(a150_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B150():
    # 'Coal_Foreign_Imports'!B150
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K150,"")'''
    @eval_fn
    def B150():
        k150_1 = Input_EIA_Imports_Coal_Foreign.K150()
        var_1 = IFERROR(k150_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C150():
    # 'Coal_Foreign_Imports'!C150
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L150,"")'''
    @eval_fn
    def C150():
        l150_1 = Input_EIA_Imports_Coal_Foreign.L150()
        var_1 = IFERROR(l150_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D150():
    # 'Coal_Foreign_Imports'!D150
    value = None
    formula = '''=IFERROR(C150/B150,"")'''
    @eval_fn
    def D150():
        c150_1 = Coal_Foreign_Imports.C150()
        b150_1 = Coal_Foreign_Imports.B150()
        var_1 = divide(c150_1, b150_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A151():
    # 'Coal_Foreign_Imports'!A151
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A151,"")'''
    @eval_fn
    def A151():
        a151_1 = Input_EIA_Imports_Coal_Foreign.A151()
        var_1 = IFERROR(a151_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B151():
    # 'Coal_Foreign_Imports'!B151
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K151,"")'''
    @eval_fn
    def B151():
        k151_1 = Input_EIA_Imports_Coal_Foreign.K151()
        var_1 = IFERROR(k151_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C151():
    # 'Coal_Foreign_Imports'!C151
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L151,"")'''
    @eval_fn
    def C151():
        l151_1 = Input_EIA_Imports_Coal_Foreign.L151()
        var_1 = IFERROR(l151_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D151():
    # 'Coal_Foreign_Imports'!D151
    value = None
    formula = '''=IFERROR(C151/B151,"")'''
    @eval_fn
    def D151():
        c151_1 = Coal_Foreign_Imports.C151()
        b151_1 = Coal_Foreign_Imports.B151()
        var_1 = divide(c151_1, b151_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A152():
    # 'Coal_Foreign_Imports'!A152
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A152,"")'''
    @eval_fn
    def A152():
        a152_1 = Input_EIA_Imports_Coal_Foreign.A152()
        var_1 = IFERROR(a152_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B152():
    # 'Coal_Foreign_Imports'!B152
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K152,"")'''
    @eval_fn
    def B152():
        k152_1 = Input_EIA_Imports_Coal_Foreign.K152()
        var_1 = IFERROR(k152_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C152():
    # 'Coal_Foreign_Imports'!C152
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L152,"")'''
    @eval_fn
    def C152():
        l152_1 = Input_EIA_Imports_Coal_Foreign.L152()
        var_1 = IFERROR(l152_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D152():
    # 'Coal_Foreign_Imports'!D152
    value = None
    formula = '''=IFERROR(C152/B152,"")'''
    @eval_fn
    def D152():
        c152_1 = Coal_Foreign_Imports.C152()
        b152_1 = Coal_Foreign_Imports.B152()
        var_1 = divide(c152_1, b152_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A153():
    # 'Coal_Foreign_Imports'!A153
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A153,"")'''
    @eval_fn
    def A153():
        a153_1 = Input_EIA_Imports_Coal_Foreign.A153()
        var_1 = IFERROR(a153_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B153():
    # 'Coal_Foreign_Imports'!B153
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K153,"")'''
    @eval_fn
    def B153():
        k153_1 = Input_EIA_Imports_Coal_Foreign.K153()
        var_1 = IFERROR(k153_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C153():
    # 'Coal_Foreign_Imports'!C153
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L153,"")'''
    @eval_fn
    def C153():
        l153_1 = Input_EIA_Imports_Coal_Foreign.L153()
        var_1 = IFERROR(l153_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D153():
    # 'Coal_Foreign_Imports'!D153
    value = None
    formula = '''=IFERROR(C153/B153,"")'''
    @eval_fn
    def D153():
        c153_1 = Coal_Foreign_Imports.C153()
        b153_1 = Coal_Foreign_Imports.B153()
        var_1 = divide(c153_1, b153_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A154():
    # 'Coal_Foreign_Imports'!A154
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A154,"")'''
    @eval_fn
    def A154():
        a154_1 = Input_EIA_Imports_Coal_Foreign.A154()
        var_1 = IFERROR(a154_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B154():
    # 'Coal_Foreign_Imports'!B154
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K154,"")'''
    @eval_fn
    def B154():
        k154_1 = Input_EIA_Imports_Coal_Foreign.K154()
        var_1 = IFERROR(k154_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C154():
    # 'Coal_Foreign_Imports'!C154
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L154,"")'''
    @eval_fn
    def C154():
        l154_1 = Input_EIA_Imports_Coal_Foreign.L154()
        var_1 = IFERROR(l154_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D154():
    # 'Coal_Foreign_Imports'!D154
    value = None
    formula = '''=IFERROR(C154/B154,"")'''
    @eval_fn
    def D154():
        c154_1 = Coal_Foreign_Imports.C154()
        b154_1 = Coal_Foreign_Imports.B154()
        var_1 = divide(c154_1, b154_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A155():
    # 'Coal_Foreign_Imports'!A155
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A155,"")'''
    @eval_fn
    def A155():
        a155_1 = Input_EIA_Imports_Coal_Foreign.A155()
        var_1 = IFERROR(a155_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B155():
    # 'Coal_Foreign_Imports'!B155
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K155,"")'''
    @eval_fn
    def B155():
        k155_1 = Input_EIA_Imports_Coal_Foreign.K155()
        var_1 = IFERROR(k155_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C155():
    # 'Coal_Foreign_Imports'!C155
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L155,"")'''
    @eval_fn
    def C155():
        l155_1 = Input_EIA_Imports_Coal_Foreign.L155()
        var_1 = IFERROR(l155_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D155():
    # 'Coal_Foreign_Imports'!D155
    value = None
    formula = '''=IFERROR(C155/B155,"")'''
    @eval_fn
    def D155():
        c155_1 = Coal_Foreign_Imports.C155()
        b155_1 = Coal_Foreign_Imports.B155()
        var_1 = divide(c155_1, b155_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A156():
    # 'Coal_Foreign_Imports'!A156
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A156,"")'''
    @eval_fn
    def A156():
        a156_1 = Input_EIA_Imports_Coal_Foreign.A156()
        var_1 = IFERROR(a156_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B156():
    # 'Coal_Foreign_Imports'!B156
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K156,"")'''
    @eval_fn
    def B156():
        k156_1 = Input_EIA_Imports_Coal_Foreign.K156()
        var_1 = IFERROR(k156_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C156():
    # 'Coal_Foreign_Imports'!C156
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L156,"")'''
    @eval_fn
    def C156():
        l156_1 = Input_EIA_Imports_Coal_Foreign.L156()
        var_1 = IFERROR(l156_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D156():
    # 'Coal_Foreign_Imports'!D156
    value = None
    formula = '''=IFERROR(C156/B156,"")'''
    @eval_fn
    def D156():
        c156_1 = Coal_Foreign_Imports.C156()
        b156_1 = Coal_Foreign_Imports.B156()
        var_1 = divide(c156_1, b156_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A157():
    # 'Coal_Foreign_Imports'!A157
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A157,"")'''
    @eval_fn
    def A157():
        a157_1 = Input_EIA_Imports_Coal_Foreign.A157()
        var_1 = IFERROR(a157_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B157():
    # 'Coal_Foreign_Imports'!B157
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K157,"")'''
    @eval_fn
    def B157():
        k157_1 = Input_EIA_Imports_Coal_Foreign.K157()
        var_1 = IFERROR(k157_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C157():
    # 'Coal_Foreign_Imports'!C157
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L157,"")'''
    @eval_fn
    def C157():
        l157_1 = Input_EIA_Imports_Coal_Foreign.L157()
        var_1 = IFERROR(l157_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D157():
    # 'Coal_Foreign_Imports'!D157
    value = None
    formula = '''=IFERROR(C157/B157,"")'''
    @eval_fn
    def D157():
        c157_1 = Coal_Foreign_Imports.C157()
        b157_1 = Coal_Foreign_Imports.B157()
        var_1 = divide(c157_1, b157_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A158():
    # 'Coal_Foreign_Imports'!A158
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A158,"")'''
    @eval_fn
    def A158():
        a158_1 = Input_EIA_Imports_Coal_Foreign.A158()
        var_1 = IFERROR(a158_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B158():
    # 'Coal_Foreign_Imports'!B158
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K158,"")'''
    @eval_fn
    def B158():
        k158_1 = Input_EIA_Imports_Coal_Foreign.K158()
        var_1 = IFERROR(k158_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C158():
    # 'Coal_Foreign_Imports'!C158
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L158,"")'''
    @eval_fn
    def C158():
        l158_1 = Input_EIA_Imports_Coal_Foreign.L158()
        var_1 = IFERROR(l158_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D158():
    # 'Coal_Foreign_Imports'!D158
    value = None
    formula = '''=IFERROR(C158/B158,"")'''
    @eval_fn
    def D158():
        c158_1 = Coal_Foreign_Imports.C158()
        b158_1 = Coal_Foreign_Imports.B158()
        var_1 = divide(c158_1, b158_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A159():
    # 'Coal_Foreign_Imports'!A159
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A159,"")'''
    @eval_fn
    def A159():
        a159_1 = Input_EIA_Imports_Coal_Foreign.A159()
        var_1 = IFERROR(a159_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B159():
    # 'Coal_Foreign_Imports'!B159
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K159,"")'''
    @eval_fn
    def B159():
        k159_1 = Input_EIA_Imports_Coal_Foreign.K159()
        var_1 = IFERROR(k159_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C159():
    # 'Coal_Foreign_Imports'!C159
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L159,"")'''
    @eval_fn
    def C159():
        l159_1 = Input_EIA_Imports_Coal_Foreign.L159()
        var_1 = IFERROR(l159_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D159():
    # 'Coal_Foreign_Imports'!D159
    value = None
    formula = '''=IFERROR(C159/B159,"")'''
    @eval_fn
    def D159():
        c159_1 = Coal_Foreign_Imports.C159()
        b159_1 = Coal_Foreign_Imports.B159()
        var_1 = divide(c159_1, b159_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A160():
    # 'Coal_Foreign_Imports'!A160
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A160,"")'''
    @eval_fn
    def A160():
        a160_1 = Input_EIA_Imports_Coal_Foreign.A160()
        var_1 = IFERROR(a160_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B160():
    # 'Coal_Foreign_Imports'!B160
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K160,"")'''
    @eval_fn
    def B160():
        k160_1 = Input_EIA_Imports_Coal_Foreign.K160()
        var_1 = IFERROR(k160_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C160():
    # 'Coal_Foreign_Imports'!C160
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L160,"")'''
    @eval_fn
    def C160():
        l160_1 = Input_EIA_Imports_Coal_Foreign.L160()
        var_1 = IFERROR(l160_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D160():
    # 'Coal_Foreign_Imports'!D160
    value = None
    formula = '''=IFERROR(C160/B160,"")'''
    @eval_fn
    def D160():
        c160_1 = Coal_Foreign_Imports.C160()
        b160_1 = Coal_Foreign_Imports.B160()
        var_1 = divide(c160_1, b160_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A161():
    # 'Coal_Foreign_Imports'!A161
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A161,"")'''
    @eval_fn
    def A161():
        a161_1 = Input_EIA_Imports_Coal_Foreign.A161()
        var_1 = IFERROR(a161_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B161():
    # 'Coal_Foreign_Imports'!B161
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K161,"")'''
    @eval_fn
    def B161():
        k161_1 = Input_EIA_Imports_Coal_Foreign.K161()
        var_1 = IFERROR(k161_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C161():
    # 'Coal_Foreign_Imports'!C161
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L161,"")'''
    @eval_fn
    def C161():
        l161_1 = Input_EIA_Imports_Coal_Foreign.L161()
        var_1 = IFERROR(l161_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D161():
    # 'Coal_Foreign_Imports'!D161
    value = None
    formula = '''=IFERROR(C161/B161,"")'''
    @eval_fn
    def D161():
        c161_1 = Coal_Foreign_Imports.C161()
        b161_1 = Coal_Foreign_Imports.B161()
        var_1 = divide(c161_1, b161_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A162():
    # 'Coal_Foreign_Imports'!A162
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A162,"")'''
    @eval_fn
    def A162():
        a162_1 = Input_EIA_Imports_Coal_Foreign.A162()
        var_1 = IFERROR(a162_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B162():
    # 'Coal_Foreign_Imports'!B162
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K162,"")'''
    @eval_fn
    def B162():
        k162_1 = Input_EIA_Imports_Coal_Foreign.K162()
        var_1 = IFERROR(k162_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C162():
    # 'Coal_Foreign_Imports'!C162
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L162,"")'''
    @eval_fn
    def C162():
        l162_1 = Input_EIA_Imports_Coal_Foreign.L162()
        var_1 = IFERROR(l162_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D162():
    # 'Coal_Foreign_Imports'!D162
    value = None
    formula = '''=IFERROR(C162/B162,"")'''
    @eval_fn
    def D162():
        c162_1 = Coal_Foreign_Imports.C162()
        b162_1 = Coal_Foreign_Imports.B162()
        var_1 = divide(c162_1, b162_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A163():
    # 'Coal_Foreign_Imports'!A163
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A163,"")'''
    @eval_fn
    def A163():
        a163_1 = Input_EIA_Imports_Coal_Foreign.A163()
        var_1 = IFERROR(a163_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B163():
    # 'Coal_Foreign_Imports'!B163
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K163,"")'''
    @eval_fn
    def B163():
        k163_1 = Input_EIA_Imports_Coal_Foreign.K163()
        var_1 = IFERROR(k163_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C163():
    # 'Coal_Foreign_Imports'!C163
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L163,"")'''
    @eval_fn
    def C163():
        l163_1 = Input_EIA_Imports_Coal_Foreign.L163()
        var_1 = IFERROR(l163_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D163():
    # 'Coal_Foreign_Imports'!D163
    value = None
    formula = '''=IFERROR(C163/B163,"")'''
    @eval_fn
    def D163():
        c163_1 = Coal_Foreign_Imports.C163()
        b163_1 = Coal_Foreign_Imports.B163()
        var_1 = divide(c163_1, b163_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A164():
    # 'Coal_Foreign_Imports'!A164
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A164,"")'''
    @eval_fn
    def A164():
        a164_1 = Input_EIA_Imports_Coal_Foreign.A164()
        var_1 = IFERROR(a164_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B164():
    # 'Coal_Foreign_Imports'!B164
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K164,"")'''
    @eval_fn
    def B164():
        k164_1 = Input_EIA_Imports_Coal_Foreign.K164()
        var_1 = IFERROR(k164_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C164():
    # 'Coal_Foreign_Imports'!C164
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L164,"")'''
    @eval_fn
    def C164():
        l164_1 = Input_EIA_Imports_Coal_Foreign.L164()
        var_1 = IFERROR(l164_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D164():
    # 'Coal_Foreign_Imports'!D164
    value = None
    formula = '''=IFERROR(C164/B164,"")'''
    @eval_fn
    def D164():
        c164_1 = Coal_Foreign_Imports.C164()
        b164_1 = Coal_Foreign_Imports.B164()
        var_1 = divide(c164_1, b164_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A165():
    # 'Coal_Foreign_Imports'!A165
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A165,"")'''
    @eval_fn
    def A165():
        a165_1 = Input_EIA_Imports_Coal_Foreign.A165()
        var_1 = IFERROR(a165_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B165():
    # 'Coal_Foreign_Imports'!B165
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K165,"")'''
    @eval_fn
    def B165():
        k165_1 = Input_EIA_Imports_Coal_Foreign.K165()
        var_1 = IFERROR(k165_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C165():
    # 'Coal_Foreign_Imports'!C165
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L165,"")'''
    @eval_fn
    def C165():
        l165_1 = Input_EIA_Imports_Coal_Foreign.L165()
        var_1 = IFERROR(l165_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D165():
    # 'Coal_Foreign_Imports'!D165
    value = None
    formula = '''=IFERROR(C165/B165,"")'''
    @eval_fn
    def D165():
        c165_1 = Coal_Foreign_Imports.C165()
        b165_1 = Coal_Foreign_Imports.B165()
        var_1 = divide(c165_1, b165_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A166():
    # 'Coal_Foreign_Imports'!A166
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A166,"")'''
    @eval_fn
    def A166():
        a166_1 = Input_EIA_Imports_Coal_Foreign.A166()
        var_1 = IFERROR(a166_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B166():
    # 'Coal_Foreign_Imports'!B166
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K166,"")'''
    @eval_fn
    def B166():
        k166_1 = Input_EIA_Imports_Coal_Foreign.K166()
        var_1 = IFERROR(k166_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C166():
    # 'Coal_Foreign_Imports'!C166
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L166,"")'''
    @eval_fn
    def C166():
        l166_1 = Input_EIA_Imports_Coal_Foreign.L166()
        var_1 = IFERROR(l166_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D166():
    # 'Coal_Foreign_Imports'!D166
    value = None
    formula = '''=IFERROR(C166/B166,"")'''
    @eval_fn
    def D166():
        c166_1 = Coal_Foreign_Imports.C166()
        b166_1 = Coal_Foreign_Imports.B166()
        var_1 = divide(c166_1, b166_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A167():
    # 'Coal_Foreign_Imports'!A167
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A167,"")'''
    @eval_fn
    def A167():
        a167_1 = Input_EIA_Imports_Coal_Foreign.A167()
        var_1 = IFERROR(a167_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B167():
    # 'Coal_Foreign_Imports'!B167
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K167,"")'''
    @eval_fn
    def B167():
        k167_1 = Input_EIA_Imports_Coal_Foreign.K167()
        var_1 = IFERROR(k167_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C167():
    # 'Coal_Foreign_Imports'!C167
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L167,"")'''
    @eval_fn
    def C167():
        l167_1 = Input_EIA_Imports_Coal_Foreign.L167()
        var_1 = IFERROR(l167_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D167():
    # 'Coal_Foreign_Imports'!D167
    value = None
    formula = '''=IFERROR(C167/B167,"")'''
    @eval_fn
    def D167():
        c167_1 = Coal_Foreign_Imports.C167()
        b167_1 = Coal_Foreign_Imports.B167()
        var_1 = divide(c167_1, b167_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A168():
    # 'Coal_Foreign_Imports'!A168
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A168,"")'''
    @eval_fn
    def A168():
        a168_1 = Input_EIA_Imports_Coal_Foreign.A168()
        var_1 = IFERROR(a168_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B168():
    # 'Coal_Foreign_Imports'!B168
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K168,"")'''
    @eval_fn
    def B168():
        k168_1 = Input_EIA_Imports_Coal_Foreign.K168()
        var_1 = IFERROR(k168_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C168():
    # 'Coal_Foreign_Imports'!C168
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L168,"")'''
    @eval_fn
    def C168():
        l168_1 = Input_EIA_Imports_Coal_Foreign.L168()
        var_1 = IFERROR(l168_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D168():
    # 'Coal_Foreign_Imports'!D168
    value = None
    formula = '''=IFERROR(C168/B168,"")'''
    @eval_fn
    def D168():
        c168_1 = Coal_Foreign_Imports.C168()
        b168_1 = Coal_Foreign_Imports.B168()
        var_1 = divide(c168_1, b168_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A169():
    # 'Coal_Foreign_Imports'!A169
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A169,"")'''
    @eval_fn
    def A169():
        a169_1 = Input_EIA_Imports_Coal_Foreign.A169()
        var_1 = IFERROR(a169_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B169():
    # 'Coal_Foreign_Imports'!B169
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K169,"")'''
    @eval_fn
    def B169():
        k169_1 = Input_EIA_Imports_Coal_Foreign.K169()
        var_1 = IFERROR(k169_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C169():
    # 'Coal_Foreign_Imports'!C169
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L169,"")'''
    @eval_fn
    def C169():
        l169_1 = Input_EIA_Imports_Coal_Foreign.L169()
        var_1 = IFERROR(l169_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D169():
    # 'Coal_Foreign_Imports'!D169
    value = None
    formula = '''=IFERROR(C169/B169,"")'''
    @eval_fn
    def D169():
        c169_1 = Coal_Foreign_Imports.C169()
        b169_1 = Coal_Foreign_Imports.B169()
        var_1 = divide(c169_1, b169_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A170():
    # 'Coal_Foreign_Imports'!A170
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A170,"")'''
    @eval_fn
    def A170():
        a170_1 = Input_EIA_Imports_Coal_Foreign.A170()
        var_1 = IFERROR(a170_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B170():
    # 'Coal_Foreign_Imports'!B170
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K170,"")'''
    @eval_fn
    def B170():
        k170_1 = Input_EIA_Imports_Coal_Foreign.K170()
        var_1 = IFERROR(k170_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C170():
    # 'Coal_Foreign_Imports'!C170
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L170,"")'''
    @eval_fn
    def C170():
        l170_1 = Input_EIA_Imports_Coal_Foreign.L170()
        var_1 = IFERROR(l170_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D170():
    # 'Coal_Foreign_Imports'!D170
    value = None
    formula = '''=IFERROR(C170/B170,"")'''
    @eval_fn
    def D170():
        c170_1 = Coal_Foreign_Imports.C170()
        b170_1 = Coal_Foreign_Imports.B170()
        var_1 = divide(c170_1, b170_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A171():
    # 'Coal_Foreign_Imports'!A171
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A171,"")'''
    @eval_fn
    def A171():
        a171_1 = Input_EIA_Imports_Coal_Foreign.A171()
        var_1 = IFERROR(a171_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B171():
    # 'Coal_Foreign_Imports'!B171
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K171,"")'''
    @eval_fn
    def B171():
        k171_1 = Input_EIA_Imports_Coal_Foreign.K171()
        var_1 = IFERROR(k171_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C171():
    # 'Coal_Foreign_Imports'!C171
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L171,"")'''
    @eval_fn
    def C171():
        l171_1 = Input_EIA_Imports_Coal_Foreign.L171()
        var_1 = IFERROR(l171_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D171():
    # 'Coal_Foreign_Imports'!D171
    value = None
    formula = '''=IFERROR(C171/B171,"")'''
    @eval_fn
    def D171():
        c171_1 = Coal_Foreign_Imports.C171()
        b171_1 = Coal_Foreign_Imports.B171()
        var_1 = divide(c171_1, b171_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A172():
    # 'Coal_Foreign_Imports'!A172
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A172,"")'''
    @eval_fn
    def A172():
        a172_1 = Input_EIA_Imports_Coal_Foreign.A172()
        var_1 = IFERROR(a172_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B172():
    # 'Coal_Foreign_Imports'!B172
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K172,"")'''
    @eval_fn
    def B172():
        k172_1 = Input_EIA_Imports_Coal_Foreign.K172()
        var_1 = IFERROR(k172_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C172():
    # 'Coal_Foreign_Imports'!C172
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L172,"")'''
    @eval_fn
    def C172():
        l172_1 = Input_EIA_Imports_Coal_Foreign.L172()
        var_1 = IFERROR(l172_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D172():
    # 'Coal_Foreign_Imports'!D172
    value = None
    formula = '''=IFERROR(C172/B172,"")'''
    @eval_fn
    def D172():
        c172_1 = Coal_Foreign_Imports.C172()
        b172_1 = Coal_Foreign_Imports.B172()
        var_1 = divide(c172_1, b172_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A173():
    # 'Coal_Foreign_Imports'!A173
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A173,"")'''
    @eval_fn
    def A173():
        a173_1 = Input_EIA_Imports_Coal_Foreign.A173()
        var_1 = IFERROR(a173_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B173():
    # 'Coal_Foreign_Imports'!B173
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K173,"")'''
    @eval_fn
    def B173():
        k173_1 = Input_EIA_Imports_Coal_Foreign.K173()
        var_1 = IFERROR(k173_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C173():
    # 'Coal_Foreign_Imports'!C173
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L173,"")'''
    @eval_fn
    def C173():
        l173_1 = Input_EIA_Imports_Coal_Foreign.L173()
        var_1 = IFERROR(l173_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D173():
    # 'Coal_Foreign_Imports'!D173
    value = None
    formula = '''=IFERROR(C173/B173,"")'''
    @eval_fn
    def D173():
        c173_1 = Coal_Foreign_Imports.C173()
        b173_1 = Coal_Foreign_Imports.B173()
        var_1 = divide(c173_1, b173_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A174():
    # 'Coal_Foreign_Imports'!A174
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A174,"")'''
    @eval_fn
    def A174():
        a174_1 = Input_EIA_Imports_Coal_Foreign.A174()
        var_1 = IFERROR(a174_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B174():
    # 'Coal_Foreign_Imports'!B174
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K174,"")'''
    @eval_fn
    def B174():
        k174_1 = Input_EIA_Imports_Coal_Foreign.K174()
        var_1 = IFERROR(k174_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C174():
    # 'Coal_Foreign_Imports'!C174
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L174,"")'''
    @eval_fn
    def C174():
        l174_1 = Input_EIA_Imports_Coal_Foreign.L174()
        var_1 = IFERROR(l174_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D174():
    # 'Coal_Foreign_Imports'!D174
    value = None
    formula = '''=IFERROR(C174/B174,"")'''
    @eval_fn
    def D174():
        c174_1 = Coal_Foreign_Imports.C174()
        b174_1 = Coal_Foreign_Imports.B174()
        var_1 = divide(c174_1, b174_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A175():
    # 'Coal_Foreign_Imports'!A175
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A175,"")'''
    @eval_fn
    def A175():
        a175_1 = Input_EIA_Imports_Coal_Foreign.A175()
        var_1 = IFERROR(a175_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B175():
    # 'Coal_Foreign_Imports'!B175
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K175,"")'''
    @eval_fn
    def B175():
        k175_1 = Input_EIA_Imports_Coal_Foreign.K175()
        var_1 = IFERROR(k175_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C175():
    # 'Coal_Foreign_Imports'!C175
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L175,"")'''
    @eval_fn
    def C175():
        l175_1 = Input_EIA_Imports_Coal_Foreign.L175()
        var_1 = IFERROR(l175_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D175():
    # 'Coal_Foreign_Imports'!D175
    value = None
    formula = '''=IFERROR(C175/B175,"")'''
    @eval_fn
    def D175():
        c175_1 = Coal_Foreign_Imports.C175()
        b175_1 = Coal_Foreign_Imports.B175()
        var_1 = divide(c175_1, b175_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A176():
    # 'Coal_Foreign_Imports'!A176
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A176,"")'''
    @eval_fn
    def A176():
        a176_1 = Input_EIA_Imports_Coal_Foreign.A176()
        var_1 = IFERROR(a176_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B176():
    # 'Coal_Foreign_Imports'!B176
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K176,"")'''
    @eval_fn
    def B176():
        k176_1 = Input_EIA_Imports_Coal_Foreign.K176()
        var_1 = IFERROR(k176_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C176():
    # 'Coal_Foreign_Imports'!C176
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L176,"")'''
    @eval_fn
    def C176():
        l176_1 = Input_EIA_Imports_Coal_Foreign.L176()
        var_1 = IFERROR(l176_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D176():
    # 'Coal_Foreign_Imports'!D176
    value = None
    formula = '''=IFERROR(C176/B176,"")'''
    @eval_fn
    def D176():
        c176_1 = Coal_Foreign_Imports.C176()
        b176_1 = Coal_Foreign_Imports.B176()
        var_1 = divide(c176_1, b176_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A177():
    # 'Coal_Foreign_Imports'!A177
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A177,"")'''
    @eval_fn
    def A177():
        a177_1 = Input_EIA_Imports_Coal_Foreign.A177()
        var_1 = IFERROR(a177_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B177():
    # 'Coal_Foreign_Imports'!B177
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K177,"")'''
    @eval_fn
    def B177():
        k177_1 = Input_EIA_Imports_Coal_Foreign.K177()
        var_1 = IFERROR(k177_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C177():
    # 'Coal_Foreign_Imports'!C177
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L177,"")'''
    @eval_fn
    def C177():
        l177_1 = Input_EIA_Imports_Coal_Foreign.L177()
        var_1 = IFERROR(l177_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D177():
    # 'Coal_Foreign_Imports'!D177
    value = None
    formula = '''=IFERROR(C177/B177,"")'''
    @eval_fn
    def D177():
        c177_1 = Coal_Foreign_Imports.C177()
        b177_1 = Coal_Foreign_Imports.B177()
        var_1 = divide(c177_1, b177_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A178():
    # 'Coal_Foreign_Imports'!A178
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A178,"")'''
    @eval_fn
    def A178():
        a178_1 = Input_EIA_Imports_Coal_Foreign.A178()
        var_1 = IFERROR(a178_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B178():
    # 'Coal_Foreign_Imports'!B178
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K178,"")'''
    @eval_fn
    def B178():
        k178_1 = Input_EIA_Imports_Coal_Foreign.K178()
        var_1 = IFERROR(k178_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C178():
    # 'Coal_Foreign_Imports'!C178
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L178,"")'''
    @eval_fn
    def C178():
        l178_1 = Input_EIA_Imports_Coal_Foreign.L178()
        var_1 = IFERROR(l178_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D178():
    # 'Coal_Foreign_Imports'!D178
    value = None
    formula = '''=IFERROR(C178/B178,"")'''
    @eval_fn
    def D178():
        c178_1 = Coal_Foreign_Imports.C178()
        b178_1 = Coal_Foreign_Imports.B178()
        var_1 = divide(c178_1, b178_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A179():
    # 'Coal_Foreign_Imports'!A179
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A179,"")'''
    @eval_fn
    def A179():
        a179_1 = Input_EIA_Imports_Coal_Foreign.A179()
        var_1 = IFERROR(a179_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B179():
    # 'Coal_Foreign_Imports'!B179
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K179,"")'''
    @eval_fn
    def B179():
        k179_1 = Input_EIA_Imports_Coal_Foreign.K179()
        var_1 = IFERROR(k179_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C179():
    # 'Coal_Foreign_Imports'!C179
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L179,"")'''
    @eval_fn
    def C179():
        l179_1 = Input_EIA_Imports_Coal_Foreign.L179()
        var_1 = IFERROR(l179_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D179():
    # 'Coal_Foreign_Imports'!D179
    value = None
    formula = '''=IFERROR(C179/B179,"")'''
    @eval_fn
    def D179():
        c179_1 = Coal_Foreign_Imports.C179()
        b179_1 = Coal_Foreign_Imports.B179()
        var_1 = divide(c179_1, b179_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A180():
    # 'Coal_Foreign_Imports'!A180
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A180,"")'''
    @eval_fn
    def A180():
        a180_1 = Input_EIA_Imports_Coal_Foreign.A180()
        var_1 = IFERROR(a180_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B180():
    # 'Coal_Foreign_Imports'!B180
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K180,"")'''
    @eval_fn
    def B180():
        k180_1 = Input_EIA_Imports_Coal_Foreign.K180()
        var_1 = IFERROR(k180_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C180():
    # 'Coal_Foreign_Imports'!C180
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L180,"")'''
    @eval_fn
    def C180():
        l180_1 = Input_EIA_Imports_Coal_Foreign.L180()
        var_1 = IFERROR(l180_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D180():
    # 'Coal_Foreign_Imports'!D180
    value = None
    formula = '''=IFERROR(C180/B180,"")'''
    @eval_fn
    def D180():
        c180_1 = Coal_Foreign_Imports.C180()
        b180_1 = Coal_Foreign_Imports.B180()
        var_1 = divide(c180_1, b180_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A181():
    # 'Coal_Foreign_Imports'!A181
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A181,"")'''
    @eval_fn
    def A181():
        a181_1 = Input_EIA_Imports_Coal_Foreign.A181()
        var_1 = IFERROR(a181_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B181():
    # 'Coal_Foreign_Imports'!B181
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K181,"")'''
    @eval_fn
    def B181():
        k181_1 = Input_EIA_Imports_Coal_Foreign.K181()
        var_1 = IFERROR(k181_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C181():
    # 'Coal_Foreign_Imports'!C181
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L181,"")'''
    @eval_fn
    def C181():
        l181_1 = Input_EIA_Imports_Coal_Foreign.L181()
        var_1 = IFERROR(l181_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D181():
    # 'Coal_Foreign_Imports'!D181
    value = None
    formula = '''=IFERROR(C181/B181,"")'''
    @eval_fn
    def D181():
        c181_1 = Coal_Foreign_Imports.C181()
        b181_1 = Coal_Foreign_Imports.B181()
        var_1 = divide(c181_1, b181_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A182():
    # 'Coal_Foreign_Imports'!A182
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A182,"")'''
    @eval_fn
    def A182():
        a182_1 = Input_EIA_Imports_Coal_Foreign.A182()
        var_1 = IFERROR(a182_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B182():
    # 'Coal_Foreign_Imports'!B182
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K182,"")'''
    @eval_fn
    def B182():
        k182_1 = Input_EIA_Imports_Coal_Foreign.K182()
        var_1 = IFERROR(k182_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C182():
    # 'Coal_Foreign_Imports'!C182
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L182,"")'''
    @eval_fn
    def C182():
        l182_1 = Input_EIA_Imports_Coal_Foreign.L182()
        var_1 = IFERROR(l182_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D182():
    # 'Coal_Foreign_Imports'!D182
    value = None
    formula = '''=IFERROR(C182/B182,"")'''
    @eval_fn
    def D182():
        c182_1 = Coal_Foreign_Imports.C182()
        b182_1 = Coal_Foreign_Imports.B182()
        var_1 = divide(c182_1, b182_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A183():
    # 'Coal_Foreign_Imports'!A183
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A183,"")'''
    @eval_fn
    def A183():
        a183_1 = Input_EIA_Imports_Coal_Foreign.A183()
        var_1 = IFERROR(a183_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B183():
    # 'Coal_Foreign_Imports'!B183
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K183,"")'''
    @eval_fn
    def B183():
        k183_1 = Input_EIA_Imports_Coal_Foreign.K183()
        var_1 = IFERROR(k183_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C183():
    # 'Coal_Foreign_Imports'!C183
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L183,"")'''
    @eval_fn
    def C183():
        l183_1 = Input_EIA_Imports_Coal_Foreign.L183()
        var_1 = IFERROR(l183_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D183():
    # 'Coal_Foreign_Imports'!D183
    value = None
    formula = '''=IFERROR(C183/B183,"")'''
    @eval_fn
    def D183():
        c183_1 = Coal_Foreign_Imports.C183()
        b183_1 = Coal_Foreign_Imports.B183()
        var_1 = divide(c183_1, b183_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A184():
    # 'Coal_Foreign_Imports'!A184
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A184,"")'''
    @eval_fn
    def A184():
        a184_1 = Input_EIA_Imports_Coal_Foreign.A184()
        var_1 = IFERROR(a184_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B184():
    # 'Coal_Foreign_Imports'!B184
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K184,"")'''
    @eval_fn
    def B184():
        k184_1 = Input_EIA_Imports_Coal_Foreign.K184()
        var_1 = IFERROR(k184_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C184():
    # 'Coal_Foreign_Imports'!C184
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L184,"")'''
    @eval_fn
    def C184():
        l184_1 = Input_EIA_Imports_Coal_Foreign.L184()
        var_1 = IFERROR(l184_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D184():
    # 'Coal_Foreign_Imports'!D184
    value = None
    formula = '''=IFERROR(C184/B184,"")'''
    @eval_fn
    def D184():
        c184_1 = Coal_Foreign_Imports.C184()
        b184_1 = Coal_Foreign_Imports.B184()
        var_1 = divide(c184_1, b184_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A185():
    # 'Coal_Foreign_Imports'!A185
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A185,"")'''
    @eval_fn
    def A185():
        a185_1 = Input_EIA_Imports_Coal_Foreign.A185()
        var_1 = IFERROR(a185_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B185():
    # 'Coal_Foreign_Imports'!B185
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K185,"")'''
    @eval_fn
    def B185():
        k185_1 = Input_EIA_Imports_Coal_Foreign.K185()
        var_1 = IFERROR(k185_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C185():
    # 'Coal_Foreign_Imports'!C185
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L185,"")'''
    @eval_fn
    def C185():
        l185_1 = Input_EIA_Imports_Coal_Foreign.L185()
        var_1 = IFERROR(l185_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D185():
    # 'Coal_Foreign_Imports'!D185
    value = None
    formula = '''=IFERROR(C185/B185,"")'''
    @eval_fn
    def D185():
        c185_1 = Coal_Foreign_Imports.C185()
        b185_1 = Coal_Foreign_Imports.B185()
        var_1 = divide(c185_1, b185_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A186():
    # 'Coal_Foreign_Imports'!A186
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A186,"")'''
    @eval_fn
    def A186():
        a186_1 = Input_EIA_Imports_Coal_Foreign.A186()
        var_1 = IFERROR(a186_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B186():
    # 'Coal_Foreign_Imports'!B186
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K186,"")'''
    @eval_fn
    def B186():
        k186_1 = Input_EIA_Imports_Coal_Foreign.K186()
        var_1 = IFERROR(k186_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C186():
    # 'Coal_Foreign_Imports'!C186
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L186,"")'''
    @eval_fn
    def C186():
        l186_1 = Input_EIA_Imports_Coal_Foreign.L186()
        var_1 = IFERROR(l186_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D186():
    # 'Coal_Foreign_Imports'!D186
    value = None
    formula = '''=IFERROR(C186/B186,"")'''
    @eval_fn
    def D186():
        c186_1 = Coal_Foreign_Imports.C186()
        b186_1 = Coal_Foreign_Imports.B186()
        var_1 = divide(c186_1, b186_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A187():
    # 'Coal_Foreign_Imports'!A187
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A187,"")'''
    @eval_fn
    def A187():
        a187_1 = Input_EIA_Imports_Coal_Foreign.A187()
        var_1 = IFERROR(a187_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B187():
    # 'Coal_Foreign_Imports'!B187
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K187,"")'''
    @eval_fn
    def B187():
        k187_1 = Input_EIA_Imports_Coal_Foreign.K187()
        var_1 = IFERROR(k187_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C187():
    # 'Coal_Foreign_Imports'!C187
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L187,"")'''
    @eval_fn
    def C187():
        l187_1 = Input_EIA_Imports_Coal_Foreign.L187()
        var_1 = IFERROR(l187_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D187():
    # 'Coal_Foreign_Imports'!D187
    value = None
    formula = '''=IFERROR(C187/B187,"")'''
    @eval_fn
    def D187():
        c187_1 = Coal_Foreign_Imports.C187()
        b187_1 = Coal_Foreign_Imports.B187()
        var_1 = divide(c187_1, b187_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A188():
    # 'Coal_Foreign_Imports'!A188
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A188,"")'''
    @eval_fn
    def A188():
        a188_1 = Input_EIA_Imports_Coal_Foreign.A188()
        var_1 = IFERROR(a188_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B188():
    # 'Coal_Foreign_Imports'!B188
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K188,"")'''
    @eval_fn
    def B188():
        k188_1 = Input_EIA_Imports_Coal_Foreign.K188()
        var_1 = IFERROR(k188_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C188():
    # 'Coal_Foreign_Imports'!C188
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L188,"")'''
    @eval_fn
    def C188():
        l188_1 = Input_EIA_Imports_Coal_Foreign.L188()
        var_1 = IFERROR(l188_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D188():
    # 'Coal_Foreign_Imports'!D188
    value = None
    formula = '''=IFERROR(C188/B188,"")'''
    @eval_fn
    def D188():
        c188_1 = Coal_Foreign_Imports.C188()
        b188_1 = Coal_Foreign_Imports.B188()
        var_1 = divide(c188_1, b188_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A189():
    # 'Coal_Foreign_Imports'!A189
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A189,"")'''
    @eval_fn
    def A189():
        a189_1 = Input_EIA_Imports_Coal_Foreign.A189()
        var_1 = IFERROR(a189_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B189():
    # 'Coal_Foreign_Imports'!B189
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K189,"")'''
    @eval_fn
    def B189():
        k189_1 = Input_EIA_Imports_Coal_Foreign.K189()
        var_1 = IFERROR(k189_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C189():
    # 'Coal_Foreign_Imports'!C189
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L189,"")'''
    @eval_fn
    def C189():
        l189_1 = Input_EIA_Imports_Coal_Foreign.L189()
        var_1 = IFERROR(l189_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D189():
    # 'Coal_Foreign_Imports'!D189
    value = None
    formula = '''=IFERROR(C189/B189,"")'''
    @eval_fn
    def D189():
        c189_1 = Coal_Foreign_Imports.C189()
        b189_1 = Coal_Foreign_Imports.B189()
        var_1 = divide(c189_1, b189_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A190():
    # 'Coal_Foreign_Imports'!A190
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A190,"")'''
    @eval_fn
    def A190():
        a190_1 = Input_EIA_Imports_Coal_Foreign.A190()
        var_1 = IFERROR(a190_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B190():
    # 'Coal_Foreign_Imports'!B190
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K190,"")'''
    @eval_fn
    def B190():
        k190_1 = Input_EIA_Imports_Coal_Foreign.K190()
        var_1 = IFERROR(k190_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C190():
    # 'Coal_Foreign_Imports'!C190
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L190,"")'''
    @eval_fn
    def C190():
        l190_1 = Input_EIA_Imports_Coal_Foreign.L190()
        var_1 = IFERROR(l190_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D190():
    # 'Coal_Foreign_Imports'!D190
    value = None
    formula = '''=IFERROR(C190/B190,"")'''
    @eval_fn
    def D190():
        c190_1 = Coal_Foreign_Imports.C190()
        b190_1 = Coal_Foreign_Imports.B190()
        var_1 = divide(c190_1, b190_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A191():
    # 'Coal_Foreign_Imports'!A191
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A191,"")'''
    @eval_fn
    def A191():
        a191_1 = Input_EIA_Imports_Coal_Foreign.A191()
        var_1 = IFERROR(a191_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B191():
    # 'Coal_Foreign_Imports'!B191
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K191,"")'''
    @eval_fn
    def B191():
        k191_1 = Input_EIA_Imports_Coal_Foreign.K191()
        var_1 = IFERROR(k191_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C191():
    # 'Coal_Foreign_Imports'!C191
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L191,"")'''
    @eval_fn
    def C191():
        l191_1 = Input_EIA_Imports_Coal_Foreign.L191()
        var_1 = IFERROR(l191_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D191():
    # 'Coal_Foreign_Imports'!D191
    value = None
    formula = '''=IFERROR(C191/B191,"")'''
    @eval_fn
    def D191():
        c191_1 = Coal_Foreign_Imports.C191()
        b191_1 = Coal_Foreign_Imports.B191()
        var_1 = divide(c191_1, b191_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A192():
    # 'Coal_Foreign_Imports'!A192
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A192,"")'''
    @eval_fn
    def A192():
        a192_1 = Input_EIA_Imports_Coal_Foreign.A192()
        var_1 = IFERROR(a192_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B192():
    # 'Coal_Foreign_Imports'!B192
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K192,"")'''
    @eval_fn
    def B192():
        k192_1 = Input_EIA_Imports_Coal_Foreign.K192()
        var_1 = IFERROR(k192_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C192():
    # 'Coal_Foreign_Imports'!C192
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L192,"")'''
    @eval_fn
    def C192():
        l192_1 = Input_EIA_Imports_Coal_Foreign.L192()
        var_1 = IFERROR(l192_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D192():
    # 'Coal_Foreign_Imports'!D192
    value = None
    formula = '''=IFERROR(C192/B192,"")'''
    @eval_fn
    def D192():
        c192_1 = Coal_Foreign_Imports.C192()
        b192_1 = Coal_Foreign_Imports.B192()
        var_1 = divide(c192_1, b192_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A193():
    # 'Coal_Foreign_Imports'!A193
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A193,"")'''
    @eval_fn
    def A193():
        a193_1 = Input_EIA_Imports_Coal_Foreign.A193()
        var_1 = IFERROR(a193_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B193():
    # 'Coal_Foreign_Imports'!B193
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K193,"")'''
    @eval_fn
    def B193():
        k193_1 = Input_EIA_Imports_Coal_Foreign.K193()
        var_1 = IFERROR(k193_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C193():
    # 'Coal_Foreign_Imports'!C193
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L193,"")'''
    @eval_fn
    def C193():
        l193_1 = Input_EIA_Imports_Coal_Foreign.L193()
        var_1 = IFERROR(l193_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D193():
    # 'Coal_Foreign_Imports'!D193
    value = None
    formula = '''=IFERROR(C193/B193,"")'''
    @eval_fn
    def D193():
        c193_1 = Coal_Foreign_Imports.C193()
        b193_1 = Coal_Foreign_Imports.B193()
        var_1 = divide(c193_1, b193_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A194():
    # 'Coal_Foreign_Imports'!A194
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A194,"")'''
    @eval_fn
    def A194():
        a194_1 = Input_EIA_Imports_Coal_Foreign.A194()
        var_1 = IFERROR(a194_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B194():
    # 'Coal_Foreign_Imports'!B194
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K194,"")'''
    @eval_fn
    def B194():
        k194_1 = Input_EIA_Imports_Coal_Foreign.K194()
        var_1 = IFERROR(k194_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C194():
    # 'Coal_Foreign_Imports'!C194
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L194,"")'''
    @eval_fn
    def C194():
        l194_1 = Input_EIA_Imports_Coal_Foreign.L194()
        var_1 = IFERROR(l194_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D194():
    # 'Coal_Foreign_Imports'!D194
    value = None
    formula = '''=IFERROR(C194/B194,"")'''
    @eval_fn
    def D194():
        c194_1 = Coal_Foreign_Imports.C194()
        b194_1 = Coal_Foreign_Imports.B194()
        var_1 = divide(c194_1, b194_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A195():
    # 'Coal_Foreign_Imports'!A195
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A195,"")'''
    @eval_fn
    def A195():
        a195_1 = Input_EIA_Imports_Coal_Foreign.A195()
        var_1 = IFERROR(a195_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B195():
    # 'Coal_Foreign_Imports'!B195
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K195,"")'''
    @eval_fn
    def B195():
        k195_1 = Input_EIA_Imports_Coal_Foreign.K195()
        var_1 = IFERROR(k195_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C195():
    # 'Coal_Foreign_Imports'!C195
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L195,"")'''
    @eval_fn
    def C195():
        l195_1 = Input_EIA_Imports_Coal_Foreign.L195()
        var_1 = IFERROR(l195_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D195():
    # 'Coal_Foreign_Imports'!D195
    value = None
    formula = '''=IFERROR(C195/B195,"")'''
    @eval_fn
    def D195():
        c195_1 = Coal_Foreign_Imports.C195()
        b195_1 = Coal_Foreign_Imports.B195()
        var_1 = divide(c195_1, b195_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A196():
    # 'Coal_Foreign_Imports'!A196
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A196,"")'''
    @eval_fn
    def A196():
        a196_1 = Input_EIA_Imports_Coal_Foreign.A196()
        var_1 = IFERROR(a196_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B196():
    # 'Coal_Foreign_Imports'!B196
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K196,"")'''
    @eval_fn
    def B196():
        k196_1 = Input_EIA_Imports_Coal_Foreign.K196()
        var_1 = IFERROR(k196_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C196():
    # 'Coal_Foreign_Imports'!C196
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L196,"")'''
    @eval_fn
    def C196():
        l196_1 = Input_EIA_Imports_Coal_Foreign.L196()
        var_1 = IFERROR(l196_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D196():
    # 'Coal_Foreign_Imports'!D196
    value = None
    formula = '''=IFERROR(C196/B196,"")'''
    @eval_fn
    def D196():
        c196_1 = Coal_Foreign_Imports.C196()
        b196_1 = Coal_Foreign_Imports.B196()
        var_1 = divide(c196_1, b196_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A197():
    # 'Coal_Foreign_Imports'!A197
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A197,"")'''
    @eval_fn
    def A197():
        a197_1 = Input_EIA_Imports_Coal_Foreign.A197()
        var_1 = IFERROR(a197_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B197():
    # 'Coal_Foreign_Imports'!B197
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K197,"")'''
    @eval_fn
    def B197():
        k197_1 = Input_EIA_Imports_Coal_Foreign.K197()
        var_1 = IFERROR(k197_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C197():
    # 'Coal_Foreign_Imports'!C197
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L197,"")'''
    @eval_fn
    def C197():
        l197_1 = Input_EIA_Imports_Coal_Foreign.L197()
        var_1 = IFERROR(l197_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D197():
    # 'Coal_Foreign_Imports'!D197
    value = None
    formula = '''=IFERROR(C197/B197,"")'''
    @eval_fn
    def D197():
        c197_1 = Coal_Foreign_Imports.C197()
        b197_1 = Coal_Foreign_Imports.B197()
        var_1 = divide(c197_1, b197_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A198():
    # 'Coal_Foreign_Imports'!A198
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A198,"")'''
    @eval_fn
    def A198():
        a198_1 = Input_EIA_Imports_Coal_Foreign.A198()
        var_1 = IFERROR(a198_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B198():
    # 'Coal_Foreign_Imports'!B198
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K198,"")'''
    @eval_fn
    def B198():
        k198_1 = Input_EIA_Imports_Coal_Foreign.K198()
        var_1 = IFERROR(k198_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C198():
    # 'Coal_Foreign_Imports'!C198
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L198,"")'''
    @eval_fn
    def C198():
        l198_1 = Input_EIA_Imports_Coal_Foreign.L198()
        var_1 = IFERROR(l198_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D198():
    # 'Coal_Foreign_Imports'!D198
    value = None
    formula = '''=IFERROR(C198/B198,"")'''
    @eval_fn
    def D198():
        c198_1 = Coal_Foreign_Imports.C198()
        b198_1 = Coal_Foreign_Imports.B198()
        var_1 = divide(c198_1, b198_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A199():
    # 'Coal_Foreign_Imports'!A199
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A199,"")'''
    @eval_fn
    def A199():
        a199_1 = Input_EIA_Imports_Coal_Foreign.A199()
        var_1 = IFERROR(a199_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B199():
    # 'Coal_Foreign_Imports'!B199
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K199,"")'''
    @eval_fn
    def B199():
        k199_1 = Input_EIA_Imports_Coal_Foreign.K199()
        var_1 = IFERROR(k199_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C199():
    # 'Coal_Foreign_Imports'!C199
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L199,"")'''
    @eval_fn
    def C199():
        l199_1 = Input_EIA_Imports_Coal_Foreign.L199()
        var_1 = IFERROR(l199_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D199():
    # 'Coal_Foreign_Imports'!D199
    value = None
    formula = '''=IFERROR(C199/B199,"")'''
    @eval_fn
    def D199():
        c199_1 = Coal_Foreign_Imports.C199()
        b199_1 = Coal_Foreign_Imports.B199()
        var_1 = divide(c199_1, b199_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A200():
    # 'Coal_Foreign_Imports'!A200
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A200,"")'''
    @eval_fn
    def A200():
        a200_1 = Input_EIA_Imports_Coal_Foreign.A200()
        var_1 = IFERROR(a200_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B200():
    # 'Coal_Foreign_Imports'!B200
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K200,"")'''
    @eval_fn
    def B200():
        k200_1 = Input_EIA_Imports_Coal_Foreign.K200()
        var_1 = IFERROR(k200_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C200():
    # 'Coal_Foreign_Imports'!C200
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L200,"")'''
    @eval_fn
    def C200():
        l200_1 = Input_EIA_Imports_Coal_Foreign.L200()
        var_1 = IFERROR(l200_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D200():
    # 'Coal_Foreign_Imports'!D200
    value = None
    formula = '''=IFERROR(C200/B200,"")'''
    @eval_fn
    def D200():
        c200_1 = Coal_Foreign_Imports.C200()
        b200_1 = Coal_Foreign_Imports.B200()
        var_1 = divide(c200_1, b200_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A201():
    # 'Coal_Foreign_Imports'!A201
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A201,"")'''
    @eval_fn
    def A201():
        a201_1 = Input_EIA_Imports_Coal_Foreign.A201()
        var_1 = IFERROR(a201_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B201():
    # 'Coal_Foreign_Imports'!B201
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K201,"")'''
    @eval_fn
    def B201():
        k201_1 = Input_EIA_Imports_Coal_Foreign.K201()
        var_1 = IFERROR(k201_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C201():
    # 'Coal_Foreign_Imports'!C201
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L201,"")'''
    @eval_fn
    def C201():
        l201_1 = Input_EIA_Imports_Coal_Foreign.L201()
        var_1 = IFERROR(l201_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D201():
    # 'Coal_Foreign_Imports'!D201
    value = None
    formula = '''=IFERROR(C201/B201,"")'''
    @eval_fn
    def D201():
        c201_1 = Coal_Foreign_Imports.C201()
        b201_1 = Coal_Foreign_Imports.B201()
        var_1 = divide(c201_1, b201_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A202():
    # 'Coal_Foreign_Imports'!A202
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A202,"")'''
    @eval_fn
    def A202():
        a202_1 = Input_EIA_Imports_Coal_Foreign.A202()
        var_1 = IFERROR(a202_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B202():
    # 'Coal_Foreign_Imports'!B202
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K202,"")'''
    @eval_fn
    def B202():
        k202_1 = Input_EIA_Imports_Coal_Foreign.K202()
        var_1 = IFERROR(k202_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C202():
    # 'Coal_Foreign_Imports'!C202
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L202,"")'''
    @eval_fn
    def C202():
        l202_1 = Input_EIA_Imports_Coal_Foreign.L202()
        var_1 = IFERROR(l202_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D202():
    # 'Coal_Foreign_Imports'!D202
    value = None
    formula = '''=IFERROR(C202/B202,"")'''
    @eval_fn
    def D202():
        c202_1 = Coal_Foreign_Imports.C202()
        b202_1 = Coal_Foreign_Imports.B202()
        var_1 = divide(c202_1, b202_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A203():
    # 'Coal_Foreign_Imports'!A203
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A203,"")'''
    @eval_fn
    def A203():
        a203_1 = Input_EIA_Imports_Coal_Foreign.A203()
        var_1 = IFERROR(a203_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B203():
    # 'Coal_Foreign_Imports'!B203
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K203,"")'''
    @eval_fn
    def B203():
        k203_1 = Input_EIA_Imports_Coal_Foreign.K203()
        var_1 = IFERROR(k203_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C203():
    # 'Coal_Foreign_Imports'!C203
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L203,"")'''
    @eval_fn
    def C203():
        l203_1 = Input_EIA_Imports_Coal_Foreign.L203()
        var_1 = IFERROR(l203_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D203():
    # 'Coal_Foreign_Imports'!D203
    value = None
    formula = '''=IFERROR(C203/B203,"")'''
    @eval_fn
    def D203():
        c203_1 = Coal_Foreign_Imports.C203()
        b203_1 = Coal_Foreign_Imports.B203()
        var_1 = divide(c203_1, b203_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A204():
    # 'Coal_Foreign_Imports'!A204
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A204,"")'''
    @eval_fn
    def A204():
        a204_1 = Input_EIA_Imports_Coal_Foreign.A204()
        var_1 = IFERROR(a204_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B204():
    # 'Coal_Foreign_Imports'!B204
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K204,"")'''
    @eval_fn
    def B204():
        k204_1 = Input_EIA_Imports_Coal_Foreign.K204()
        var_1 = IFERROR(k204_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C204():
    # 'Coal_Foreign_Imports'!C204
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L204,"")'''
    @eval_fn
    def C204():
        l204_1 = Input_EIA_Imports_Coal_Foreign.L204()
        var_1 = IFERROR(l204_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D204():
    # 'Coal_Foreign_Imports'!D204
    value = None
    formula = '''=IFERROR(C204/B204,"")'''
    @eval_fn
    def D204():
        c204_1 = Coal_Foreign_Imports.C204()
        b204_1 = Coal_Foreign_Imports.B204()
        var_1 = divide(c204_1, b204_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A205():
    # 'Coal_Foreign_Imports'!A205
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A205,"")'''
    @eval_fn
    def A205():
        a205_1 = Input_EIA_Imports_Coal_Foreign.A205()
        var_1 = IFERROR(a205_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B205():
    # 'Coal_Foreign_Imports'!B205
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K205,"")'''
    @eval_fn
    def B205():
        k205_1 = Input_EIA_Imports_Coal_Foreign.K205()
        var_1 = IFERROR(k205_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C205():
    # 'Coal_Foreign_Imports'!C205
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L205,"")'''
    @eval_fn
    def C205():
        l205_1 = Input_EIA_Imports_Coal_Foreign.L205()
        var_1 = IFERROR(l205_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D205():
    # 'Coal_Foreign_Imports'!D205
    value = None
    formula = '''=IFERROR(C205/B205,"")'''
    @eval_fn
    def D205():
        c205_1 = Coal_Foreign_Imports.C205()
        b205_1 = Coal_Foreign_Imports.B205()
        var_1 = divide(c205_1, b205_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A206():
    # 'Coal_Foreign_Imports'!A206
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A206,"")'''
    @eval_fn
    def A206():
        a206_1 = Input_EIA_Imports_Coal_Foreign.A206()
        var_1 = IFERROR(a206_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B206():
    # 'Coal_Foreign_Imports'!B206
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K206,"")'''
    @eval_fn
    def B206():
        k206_1 = Input_EIA_Imports_Coal_Foreign.K206()
        var_1 = IFERROR(k206_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C206():
    # 'Coal_Foreign_Imports'!C206
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L206,"")'''
    @eval_fn
    def C206():
        l206_1 = Input_EIA_Imports_Coal_Foreign.L206()
        var_1 = IFERROR(l206_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D206():
    # 'Coal_Foreign_Imports'!D206
    value = None
    formula = '''=IFERROR(C206/B206,"")'''
    @eval_fn
    def D206():
        c206_1 = Coal_Foreign_Imports.C206()
        b206_1 = Coal_Foreign_Imports.B206()
        var_1 = divide(c206_1, b206_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A207():
    # 'Coal_Foreign_Imports'!A207
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A207,"")'''
    @eval_fn
    def A207():
        a207_1 = Input_EIA_Imports_Coal_Foreign.A207()
        var_1 = IFERROR(a207_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B207():
    # 'Coal_Foreign_Imports'!B207
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K207,"")'''
    @eval_fn
    def B207():
        k207_1 = Input_EIA_Imports_Coal_Foreign.K207()
        var_1 = IFERROR(k207_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C207():
    # 'Coal_Foreign_Imports'!C207
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L207,"")'''
    @eval_fn
    def C207():
        l207_1 = Input_EIA_Imports_Coal_Foreign.L207()
        var_1 = IFERROR(l207_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D207():
    # 'Coal_Foreign_Imports'!D207
    value = None
    formula = '''=IFERROR(C207/B207,"")'''
    @eval_fn
    def D207():
        c207_1 = Coal_Foreign_Imports.C207()
        b207_1 = Coal_Foreign_Imports.B207()
        var_1 = divide(c207_1, b207_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A208():
    # 'Coal_Foreign_Imports'!A208
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A208,"")'''
    @eval_fn
    def A208():
        a208_1 = Input_EIA_Imports_Coal_Foreign.A208()
        var_1 = IFERROR(a208_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B208():
    # 'Coal_Foreign_Imports'!B208
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K208,"")'''
    @eval_fn
    def B208():
        k208_1 = Input_EIA_Imports_Coal_Foreign.K208()
        var_1 = IFERROR(k208_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C208():
    # 'Coal_Foreign_Imports'!C208
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L208,"")'''
    @eval_fn
    def C208():
        l208_1 = Input_EIA_Imports_Coal_Foreign.L208()
        var_1 = IFERROR(l208_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D208():
    # 'Coal_Foreign_Imports'!D208
    value = None
    formula = '''=IFERROR(C208/B208,"")'''
    @eval_fn
    def D208():
        c208_1 = Coal_Foreign_Imports.C208()
        b208_1 = Coal_Foreign_Imports.B208()
        var_1 = divide(c208_1, b208_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A209():
    # 'Coal_Foreign_Imports'!A209
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A209,"")'''
    @eval_fn
    def A209():
        a209_1 = Input_EIA_Imports_Coal_Foreign.A209()
        var_1 = IFERROR(a209_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B209():
    # 'Coal_Foreign_Imports'!B209
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K209,"")'''
    @eval_fn
    def B209():
        k209_1 = Input_EIA_Imports_Coal_Foreign.K209()
        var_1 = IFERROR(k209_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C209():
    # 'Coal_Foreign_Imports'!C209
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L209,"")'''
    @eval_fn
    def C209():
        l209_1 = Input_EIA_Imports_Coal_Foreign.L209()
        var_1 = IFERROR(l209_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D209():
    # 'Coal_Foreign_Imports'!D209
    value = None
    formula = '''=IFERROR(C209/B209,"")'''
    @eval_fn
    def D209():
        c209_1 = Coal_Foreign_Imports.C209()
        b209_1 = Coal_Foreign_Imports.B209()
        var_1 = divide(c209_1, b209_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A210():
    # 'Coal_Foreign_Imports'!A210
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A210,"")'''
    @eval_fn
    def A210():
        a210_1 = Input_EIA_Imports_Coal_Foreign.A210()
        var_1 = IFERROR(a210_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B210():
    # 'Coal_Foreign_Imports'!B210
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K210,"")'''
    @eval_fn
    def B210():
        k210_1 = Input_EIA_Imports_Coal_Foreign.K210()
        var_1 = IFERROR(k210_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C210():
    # 'Coal_Foreign_Imports'!C210
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L210,"")'''
    @eval_fn
    def C210():
        l210_1 = Input_EIA_Imports_Coal_Foreign.L210()
        var_1 = IFERROR(l210_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D210():
    # 'Coal_Foreign_Imports'!D210
    value = None
    formula = '''=IFERROR(C210/B210,"")'''
    @eval_fn
    def D210():
        c210_1 = Coal_Foreign_Imports.C210()
        b210_1 = Coal_Foreign_Imports.B210()
        var_1 = divide(c210_1, b210_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A211():
    # 'Coal_Foreign_Imports'!A211
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A211,"")'''
    @eval_fn
    def A211():
        a211_1 = Input_EIA_Imports_Coal_Foreign.A211()
        var_1 = IFERROR(a211_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B211():
    # 'Coal_Foreign_Imports'!B211
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K211,"")'''
    @eval_fn
    def B211():
        k211_1 = Input_EIA_Imports_Coal_Foreign.K211()
        var_1 = IFERROR(k211_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C211():
    # 'Coal_Foreign_Imports'!C211
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L211,"")'''
    @eval_fn
    def C211():
        l211_1 = Input_EIA_Imports_Coal_Foreign.L211()
        var_1 = IFERROR(l211_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D211():
    # 'Coal_Foreign_Imports'!D211
    value = None
    formula = '''=IFERROR(C211/B211,"")'''
    @eval_fn
    def D211():
        c211_1 = Coal_Foreign_Imports.C211()
        b211_1 = Coal_Foreign_Imports.B211()
        var_1 = divide(c211_1, b211_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A212():
    # 'Coal_Foreign_Imports'!A212
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A212,"")'''
    @eval_fn
    def A212():
        a212_1 = Input_EIA_Imports_Coal_Foreign.A212()
        var_1 = IFERROR(a212_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B212():
    # 'Coal_Foreign_Imports'!B212
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K212,"")'''
    @eval_fn
    def B212():
        k212_1 = Input_EIA_Imports_Coal_Foreign.K212()
        var_1 = IFERROR(k212_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C212():
    # 'Coal_Foreign_Imports'!C212
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L212,"")'''
    @eval_fn
    def C212():
        l212_1 = Input_EIA_Imports_Coal_Foreign.L212()
        var_1 = IFERROR(l212_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D212():
    # 'Coal_Foreign_Imports'!D212
    value = None
    formula = '''=IFERROR(C212/B212,"")'''
    @eval_fn
    def D212():
        c212_1 = Coal_Foreign_Imports.C212()
        b212_1 = Coal_Foreign_Imports.B212()
        var_1 = divide(c212_1, b212_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A213():
    # 'Coal_Foreign_Imports'!A213
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A213,"")'''
    @eval_fn
    def A213():
        a213_1 = Input_EIA_Imports_Coal_Foreign.A213()
        var_1 = IFERROR(a213_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B213():
    # 'Coal_Foreign_Imports'!B213
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K213,"")'''
    @eval_fn
    def B213():
        k213_1 = Input_EIA_Imports_Coal_Foreign.K213()
        var_1 = IFERROR(k213_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C213():
    # 'Coal_Foreign_Imports'!C213
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L213,"")'''
    @eval_fn
    def C213():
        l213_1 = Input_EIA_Imports_Coal_Foreign.L213()
        var_1 = IFERROR(l213_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D213():
    # 'Coal_Foreign_Imports'!D213
    value = None
    formula = '''=IFERROR(C213/B213,"")'''
    @eval_fn
    def D213():
        c213_1 = Coal_Foreign_Imports.C213()
        b213_1 = Coal_Foreign_Imports.B213()
        var_1 = divide(c213_1, b213_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A214():
    # 'Coal_Foreign_Imports'!A214
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A214,"")'''
    @eval_fn
    def A214():
        a214_1 = Input_EIA_Imports_Coal_Foreign.A214()
        var_1 = IFERROR(a214_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B214():
    # 'Coal_Foreign_Imports'!B214
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K214,"")'''
    @eval_fn
    def B214():
        k214_1 = Input_EIA_Imports_Coal_Foreign.K214()
        var_1 = IFERROR(k214_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C214():
    # 'Coal_Foreign_Imports'!C214
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L214,"")'''
    @eval_fn
    def C214():
        l214_1 = Input_EIA_Imports_Coal_Foreign.L214()
        var_1 = IFERROR(l214_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D214():
    # 'Coal_Foreign_Imports'!D214
    value = None
    formula = '''=IFERROR(C214/B214,"")'''
    @eval_fn
    def D214():
        c214_1 = Coal_Foreign_Imports.C214()
        b214_1 = Coal_Foreign_Imports.B214()
        var_1 = divide(c214_1, b214_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A215():
    # 'Coal_Foreign_Imports'!A215
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A215,"")'''
    @eval_fn
    def A215():
        a215_1 = Input_EIA_Imports_Coal_Foreign.A215()
        var_1 = IFERROR(a215_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B215():
    # 'Coal_Foreign_Imports'!B215
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K215,"")'''
    @eval_fn
    def B215():
        k215_1 = Input_EIA_Imports_Coal_Foreign.K215()
        var_1 = IFERROR(k215_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C215():
    # 'Coal_Foreign_Imports'!C215
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L215,"")'''
    @eval_fn
    def C215():
        l215_1 = Input_EIA_Imports_Coal_Foreign.L215()
        var_1 = IFERROR(l215_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D215():
    # 'Coal_Foreign_Imports'!D215
    value = None
    formula = '''=IFERROR(C215/B215,"")'''
    @eval_fn
    def D215():
        c215_1 = Coal_Foreign_Imports.C215()
        b215_1 = Coal_Foreign_Imports.B215()
        var_1 = divide(c215_1, b215_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A216():
    # 'Coal_Foreign_Imports'!A216
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A216,"")'''
    @eval_fn
    def A216():
        a216_1 = Input_EIA_Imports_Coal_Foreign.A216()
        var_1 = IFERROR(a216_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B216():
    # 'Coal_Foreign_Imports'!B216
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K216,"")'''
    @eval_fn
    def B216():
        k216_1 = Input_EIA_Imports_Coal_Foreign.K216()
        var_1 = IFERROR(k216_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C216():
    # 'Coal_Foreign_Imports'!C216
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L216,"")'''
    @eval_fn
    def C216():
        l216_1 = Input_EIA_Imports_Coal_Foreign.L216()
        var_1 = IFERROR(l216_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D216():
    # 'Coal_Foreign_Imports'!D216
    value = None
    formula = '''=IFERROR(C216/B216,"")'''
    @eval_fn
    def D216():
        c216_1 = Coal_Foreign_Imports.C216()
        b216_1 = Coal_Foreign_Imports.B216()
        var_1 = divide(c216_1, b216_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A217():
    # 'Coal_Foreign_Imports'!A217
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A217,"")'''
    @eval_fn
    def A217():
        a217_1 = Input_EIA_Imports_Coal_Foreign.A217()
        var_1 = IFERROR(a217_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B217():
    # 'Coal_Foreign_Imports'!B217
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K217,"")'''
    @eval_fn
    def B217():
        k217_1 = Input_EIA_Imports_Coal_Foreign.K217()
        var_1 = IFERROR(k217_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C217():
    # 'Coal_Foreign_Imports'!C217
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L217,"")'''
    @eval_fn
    def C217():
        l217_1 = Input_EIA_Imports_Coal_Foreign.L217()
        var_1 = IFERROR(l217_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D217():
    # 'Coal_Foreign_Imports'!D217
    value = None
    formula = '''=IFERROR(C217/B217,"")'''
    @eval_fn
    def D217():
        c217_1 = Coal_Foreign_Imports.C217()
        b217_1 = Coal_Foreign_Imports.B217()
        var_1 = divide(c217_1, b217_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A218():
    # 'Coal_Foreign_Imports'!A218
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A218,"")'''
    @eval_fn
    def A218():
        a218_1 = Input_EIA_Imports_Coal_Foreign.A218()
        var_1 = IFERROR(a218_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B218():
    # 'Coal_Foreign_Imports'!B218
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K218,"")'''
    @eval_fn
    def B218():
        k218_1 = Input_EIA_Imports_Coal_Foreign.K218()
        var_1 = IFERROR(k218_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C218():
    # 'Coal_Foreign_Imports'!C218
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L218,"")'''
    @eval_fn
    def C218():
        l218_1 = Input_EIA_Imports_Coal_Foreign.L218()
        var_1 = IFERROR(l218_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D218():
    # 'Coal_Foreign_Imports'!D218
    value = None
    formula = '''=IFERROR(C218/B218,"")'''
    @eval_fn
    def D218():
        c218_1 = Coal_Foreign_Imports.C218()
        b218_1 = Coal_Foreign_Imports.B218()
        var_1 = divide(c218_1, b218_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A219():
    # 'Coal_Foreign_Imports'!A219
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A219,"")'''
    @eval_fn
    def A219():
        a219_1 = Input_EIA_Imports_Coal_Foreign.A219()
        var_1 = IFERROR(a219_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B219():
    # 'Coal_Foreign_Imports'!B219
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K219,"")'''
    @eval_fn
    def B219():
        k219_1 = Input_EIA_Imports_Coal_Foreign.K219()
        var_1 = IFERROR(k219_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C219():
    # 'Coal_Foreign_Imports'!C219
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L219,"")'''
    @eval_fn
    def C219():
        l219_1 = Input_EIA_Imports_Coal_Foreign.L219()
        var_1 = IFERROR(l219_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D219():
    # 'Coal_Foreign_Imports'!D219
    value = None
    formula = '''=IFERROR(C219/B219,"")'''
    @eval_fn
    def D219():
        c219_1 = Coal_Foreign_Imports.C219()
        b219_1 = Coal_Foreign_Imports.B219()
        var_1 = divide(c219_1, b219_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A220():
    # 'Coal_Foreign_Imports'!A220
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A220,"")'''
    @eval_fn
    def A220():
        a220_1 = Input_EIA_Imports_Coal_Foreign.A220()
        var_1 = IFERROR(a220_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B220():
    # 'Coal_Foreign_Imports'!B220
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K220,"")'''
    @eval_fn
    def B220():
        k220_1 = Input_EIA_Imports_Coal_Foreign.K220()
        var_1 = IFERROR(k220_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C220():
    # 'Coal_Foreign_Imports'!C220
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L220,"")'''
    @eval_fn
    def C220():
        l220_1 = Input_EIA_Imports_Coal_Foreign.L220()
        var_1 = IFERROR(l220_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D220():
    # 'Coal_Foreign_Imports'!D220
    value = None
    formula = '''=IFERROR(C220/B220,"")'''
    @eval_fn
    def D220():
        c220_1 = Coal_Foreign_Imports.C220()
        b220_1 = Coal_Foreign_Imports.B220()
        var_1 = divide(c220_1, b220_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A221():
    # 'Coal_Foreign_Imports'!A221
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A221,"")'''
    @eval_fn
    def A221():
        a221_1 = Input_EIA_Imports_Coal_Foreign.A221()
        var_1 = IFERROR(a221_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B221():
    # 'Coal_Foreign_Imports'!B221
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K221,"")'''
    @eval_fn
    def B221():
        k221_1 = Input_EIA_Imports_Coal_Foreign.K221()
        var_1 = IFERROR(k221_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C221():
    # 'Coal_Foreign_Imports'!C221
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L221,"")'''
    @eval_fn
    def C221():
        l221_1 = Input_EIA_Imports_Coal_Foreign.L221()
        var_1 = IFERROR(l221_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D221():
    # 'Coal_Foreign_Imports'!D221
    value = None
    formula = '''=IFERROR(C221/B221,"")'''
    @eval_fn
    def D221():
        c221_1 = Coal_Foreign_Imports.C221()
        b221_1 = Coal_Foreign_Imports.B221()
        var_1 = divide(c221_1, b221_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A222():
    # 'Coal_Foreign_Imports'!A222
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A222,"")'''
    @eval_fn
    def A222():
        a222_1 = Input_EIA_Imports_Coal_Foreign.A222()
        var_1 = IFERROR(a222_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B222():
    # 'Coal_Foreign_Imports'!B222
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K222,"")'''
    @eval_fn
    def B222():
        k222_1 = Input_EIA_Imports_Coal_Foreign.K222()
        var_1 = IFERROR(k222_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C222():
    # 'Coal_Foreign_Imports'!C222
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L222,"")'''
    @eval_fn
    def C222():
        l222_1 = Input_EIA_Imports_Coal_Foreign.L222()
        var_1 = IFERROR(l222_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D222():
    # 'Coal_Foreign_Imports'!D222
    value = None
    formula = '''=IFERROR(C222/B222,"")'''
    @eval_fn
    def D222():
        c222_1 = Coal_Foreign_Imports.C222()
        b222_1 = Coal_Foreign_Imports.B222()
        var_1 = divide(c222_1, b222_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A223():
    # 'Coal_Foreign_Imports'!A223
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A223,"")'''
    @eval_fn
    def A223():
        a223_1 = Input_EIA_Imports_Coal_Foreign.A223()
        var_1 = IFERROR(a223_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B223():
    # 'Coal_Foreign_Imports'!B223
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K223,"")'''
    @eval_fn
    def B223():
        k223_1 = Input_EIA_Imports_Coal_Foreign.K223()
        var_1 = IFERROR(k223_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C223():
    # 'Coal_Foreign_Imports'!C223
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L223,"")'''
    @eval_fn
    def C223():
        l223_1 = Input_EIA_Imports_Coal_Foreign.L223()
        var_1 = IFERROR(l223_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D223():
    # 'Coal_Foreign_Imports'!D223
    value = None
    formula = '''=IFERROR(C223/B223,"")'''
    @eval_fn
    def D223():
        c223_1 = Coal_Foreign_Imports.C223()
        b223_1 = Coal_Foreign_Imports.B223()
        var_1 = divide(c223_1, b223_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A224():
    # 'Coal_Foreign_Imports'!A224
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A224,"")'''
    @eval_fn
    def A224():
        a224_1 = Input_EIA_Imports_Coal_Foreign.A224()
        var_1 = IFERROR(a224_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B224():
    # 'Coal_Foreign_Imports'!B224
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K224,"")'''
    @eval_fn
    def B224():
        k224_1 = Input_EIA_Imports_Coal_Foreign.K224()
        var_1 = IFERROR(k224_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C224():
    # 'Coal_Foreign_Imports'!C224
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L224,"")'''
    @eval_fn
    def C224():
        l224_1 = Input_EIA_Imports_Coal_Foreign.L224()
        var_1 = IFERROR(l224_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D224():
    # 'Coal_Foreign_Imports'!D224
    value = None
    formula = '''=IFERROR(C224/B224,"")'''
    @eval_fn
    def D224():
        c224_1 = Coal_Foreign_Imports.C224()
        b224_1 = Coal_Foreign_Imports.B224()
        var_1 = divide(c224_1, b224_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A225():
    # 'Coal_Foreign_Imports'!A225
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A225,"")'''
    @eval_fn
    def A225():
        a225_1 = Input_EIA_Imports_Coal_Foreign.A225()
        var_1 = IFERROR(a225_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B225():
    # 'Coal_Foreign_Imports'!B225
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K225,"")'''
    @eval_fn
    def B225():
        k225_1 = Input_EIA_Imports_Coal_Foreign.K225()
        var_1 = IFERROR(k225_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C225():
    # 'Coal_Foreign_Imports'!C225
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L225,"")'''
    @eval_fn
    def C225():
        l225_1 = Input_EIA_Imports_Coal_Foreign.L225()
        var_1 = IFERROR(l225_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D225():
    # 'Coal_Foreign_Imports'!D225
    value = None
    formula = '''=IFERROR(C225/B225,"")'''
    @eval_fn
    def D225():
        c225_1 = Coal_Foreign_Imports.C225()
        b225_1 = Coal_Foreign_Imports.B225()
        var_1 = divide(c225_1, b225_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A226():
    # 'Coal_Foreign_Imports'!A226
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A226,"")'''
    @eval_fn
    def A226():
        a226_1 = Input_EIA_Imports_Coal_Foreign.A226()
        var_1 = IFERROR(a226_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B226():
    # 'Coal_Foreign_Imports'!B226
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K226,"")'''
    @eval_fn
    def B226():
        k226_1 = Input_EIA_Imports_Coal_Foreign.K226()
        var_1 = IFERROR(k226_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C226():
    # 'Coal_Foreign_Imports'!C226
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L226,"")'''
    @eval_fn
    def C226():
        l226_1 = Input_EIA_Imports_Coal_Foreign.L226()
        var_1 = IFERROR(l226_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D226():
    # 'Coal_Foreign_Imports'!D226
    value = None
    formula = '''=IFERROR(C226/B226,"")'''
    @eval_fn
    def D226():
        c226_1 = Coal_Foreign_Imports.C226()
        b226_1 = Coal_Foreign_Imports.B226()
        var_1 = divide(c226_1, b226_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A227():
    # 'Coal_Foreign_Imports'!A227
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A227,"")'''
    @eval_fn
    def A227():
        a227_1 = Input_EIA_Imports_Coal_Foreign.A227()
        var_1 = IFERROR(a227_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B227():
    # 'Coal_Foreign_Imports'!B227
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K227,"")'''
    @eval_fn
    def B227():
        k227_1 = Input_EIA_Imports_Coal_Foreign.K227()
        var_1 = IFERROR(k227_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C227():
    # 'Coal_Foreign_Imports'!C227
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L227,"")'''
    @eval_fn
    def C227():
        l227_1 = Input_EIA_Imports_Coal_Foreign.L227()
        var_1 = IFERROR(l227_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D227():
    # 'Coal_Foreign_Imports'!D227
    value = None
    formula = '''=IFERROR(C227/B227,"")'''
    @eval_fn
    def D227():
        c227_1 = Coal_Foreign_Imports.C227()
        b227_1 = Coal_Foreign_Imports.B227()
        var_1 = divide(c227_1, b227_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A228():
    # 'Coal_Foreign_Imports'!A228
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A228,"")'''
    @eval_fn
    def A228():
        a228_1 = Input_EIA_Imports_Coal_Foreign.A228()
        var_1 = IFERROR(a228_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B228():
    # 'Coal_Foreign_Imports'!B228
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K228,"")'''
    @eval_fn
    def B228():
        k228_1 = Input_EIA_Imports_Coal_Foreign.K228()
        var_1 = IFERROR(k228_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C228():
    # 'Coal_Foreign_Imports'!C228
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L228,"")'''
    @eval_fn
    def C228():
        l228_1 = Input_EIA_Imports_Coal_Foreign.L228()
        var_1 = IFERROR(l228_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D228():
    # 'Coal_Foreign_Imports'!D228
    value = None
    formula = '''=IFERROR(C228/B228,"")'''
    @eval_fn
    def D228():
        c228_1 = Coal_Foreign_Imports.C228()
        b228_1 = Coal_Foreign_Imports.B228()
        var_1 = divide(c228_1, b228_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A229():
    # 'Coal_Foreign_Imports'!A229
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A229,"")'''
    @eval_fn
    def A229():
        a229_1 = Input_EIA_Imports_Coal_Foreign.A229()
        var_1 = IFERROR(a229_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B229():
    # 'Coal_Foreign_Imports'!B229
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K229,"")'''
    @eval_fn
    def B229():
        k229_1 = Input_EIA_Imports_Coal_Foreign.K229()
        var_1 = IFERROR(k229_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C229():
    # 'Coal_Foreign_Imports'!C229
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L229,"")'''
    @eval_fn
    def C229():
        l229_1 = Input_EIA_Imports_Coal_Foreign.L229()
        var_1 = IFERROR(l229_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D229():
    # 'Coal_Foreign_Imports'!D229
    value = None
    formula = '''=IFERROR(C229/B229,"")'''
    @eval_fn
    def D229():
        c229_1 = Coal_Foreign_Imports.C229()
        b229_1 = Coal_Foreign_Imports.B229()
        var_1 = divide(c229_1, b229_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A230():
    # 'Coal_Foreign_Imports'!A230
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A230,"")'''
    @eval_fn
    def A230():
        a230_1 = Input_EIA_Imports_Coal_Foreign.A230()
        var_1 = IFERROR(a230_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B230():
    # 'Coal_Foreign_Imports'!B230
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K230,"")'''
    @eval_fn
    def B230():
        k230_1 = Input_EIA_Imports_Coal_Foreign.K230()
        var_1 = IFERROR(k230_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C230():
    # 'Coal_Foreign_Imports'!C230
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L230,"")'''
    @eval_fn
    def C230():
        l230_1 = Input_EIA_Imports_Coal_Foreign.L230()
        var_1 = IFERROR(l230_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D230():
    # 'Coal_Foreign_Imports'!D230
    value = None
    formula = '''=IFERROR(C230/B230,"")'''
    @eval_fn
    def D230():
        c230_1 = Coal_Foreign_Imports.C230()
        b230_1 = Coal_Foreign_Imports.B230()
        var_1 = divide(c230_1, b230_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A231():
    # 'Coal_Foreign_Imports'!A231
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A231,"")'''
    @eval_fn
    def A231():
        a231_1 = Input_EIA_Imports_Coal_Foreign.A231()
        var_1 = IFERROR(a231_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B231():
    # 'Coal_Foreign_Imports'!B231
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K231,"")'''
    @eval_fn
    def B231():
        k231_1 = Input_EIA_Imports_Coal_Foreign.K231()
        var_1 = IFERROR(k231_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C231():
    # 'Coal_Foreign_Imports'!C231
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L231,"")'''
    @eval_fn
    def C231():
        l231_1 = Input_EIA_Imports_Coal_Foreign.L231()
        var_1 = IFERROR(l231_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D231():
    # 'Coal_Foreign_Imports'!D231
    value = None
    formula = '''=IFERROR(C231/B231,"")'''
    @eval_fn
    def D231():
        c231_1 = Coal_Foreign_Imports.C231()
        b231_1 = Coal_Foreign_Imports.B231()
        var_1 = divide(c231_1, b231_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A232():
    # 'Coal_Foreign_Imports'!A232
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A232,"")'''
    @eval_fn
    def A232():
        a232_1 = Input_EIA_Imports_Coal_Foreign.A232()
        var_1 = IFERROR(a232_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B232():
    # 'Coal_Foreign_Imports'!B232
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K232,"")'''
    @eval_fn
    def B232():
        k232_1 = Input_EIA_Imports_Coal_Foreign.K232()
        var_1 = IFERROR(k232_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C232():
    # 'Coal_Foreign_Imports'!C232
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L232,"")'''
    @eval_fn
    def C232():
        l232_1 = Input_EIA_Imports_Coal_Foreign.L232()
        var_1 = IFERROR(l232_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D232():
    # 'Coal_Foreign_Imports'!D232
    value = None
    formula = '''=IFERROR(C232/B232,"")'''
    @eval_fn
    def D232():
        c232_1 = Coal_Foreign_Imports.C232()
        b232_1 = Coal_Foreign_Imports.B232()
        var_1 = divide(c232_1, b232_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A233():
    # 'Coal_Foreign_Imports'!A233
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A233,"")'''
    @eval_fn
    def A233():
        a233_1 = Input_EIA_Imports_Coal_Foreign.A233()
        var_1 = IFERROR(a233_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B233():
    # 'Coal_Foreign_Imports'!B233
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K233,"")'''
    @eval_fn
    def B233():
        k233_1 = Input_EIA_Imports_Coal_Foreign.K233()
        var_1 = IFERROR(k233_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C233():
    # 'Coal_Foreign_Imports'!C233
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L233,"")'''
    @eval_fn
    def C233():
        l233_1 = Input_EIA_Imports_Coal_Foreign.L233()
        var_1 = IFERROR(l233_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D233():
    # 'Coal_Foreign_Imports'!D233
    value = None
    formula = '''=IFERROR(C233/B233,"")'''
    @eval_fn
    def D233():
        c233_1 = Coal_Foreign_Imports.C233()
        b233_1 = Coal_Foreign_Imports.B233()
        var_1 = divide(c233_1, b233_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A234():
    # 'Coal_Foreign_Imports'!A234
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A234,"")'''
    @eval_fn
    def A234():
        a234_1 = Input_EIA_Imports_Coal_Foreign.A234()
        var_1 = IFERROR(a234_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B234():
    # 'Coal_Foreign_Imports'!B234
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K234,"")'''
    @eval_fn
    def B234():
        k234_1 = Input_EIA_Imports_Coal_Foreign.K234()
        var_1 = IFERROR(k234_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C234():
    # 'Coal_Foreign_Imports'!C234
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L234,"")'''
    @eval_fn
    def C234():
        l234_1 = Input_EIA_Imports_Coal_Foreign.L234()
        var_1 = IFERROR(l234_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D234():
    # 'Coal_Foreign_Imports'!D234
    value = None
    formula = '''=IFERROR(C234/B234,"")'''
    @eval_fn
    def D234():
        c234_1 = Coal_Foreign_Imports.C234()
        b234_1 = Coal_Foreign_Imports.B234()
        var_1 = divide(c234_1, b234_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A235():
    # 'Coal_Foreign_Imports'!A235
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A235,"")'''
    @eval_fn
    def A235():
        a235_1 = Input_EIA_Imports_Coal_Foreign.A235()
        var_1 = IFERROR(a235_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B235():
    # 'Coal_Foreign_Imports'!B235
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K235,"")'''
    @eval_fn
    def B235():
        k235_1 = Input_EIA_Imports_Coal_Foreign.K235()
        var_1 = IFERROR(k235_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C235():
    # 'Coal_Foreign_Imports'!C235
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L235,"")'''
    @eval_fn
    def C235():
        l235_1 = Input_EIA_Imports_Coal_Foreign.L235()
        var_1 = IFERROR(l235_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D235():
    # 'Coal_Foreign_Imports'!D235
    value = None
    formula = '''=IFERROR(C235/B235,"")'''
    @eval_fn
    def D235():
        c235_1 = Coal_Foreign_Imports.C235()
        b235_1 = Coal_Foreign_Imports.B235()
        var_1 = divide(c235_1, b235_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A236():
    # 'Coal_Foreign_Imports'!A236
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A236,"")'''
    @eval_fn
    def A236():
        a236_1 = Input_EIA_Imports_Coal_Foreign.A236()
        var_1 = IFERROR(a236_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B236():
    # 'Coal_Foreign_Imports'!B236
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K236,"")'''
    @eval_fn
    def B236():
        k236_1 = Input_EIA_Imports_Coal_Foreign.K236()
        var_1 = IFERROR(k236_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C236():
    # 'Coal_Foreign_Imports'!C236
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L236,"")'''
    @eval_fn
    def C236():
        l236_1 = Input_EIA_Imports_Coal_Foreign.L236()
        var_1 = IFERROR(l236_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D236():
    # 'Coal_Foreign_Imports'!D236
    value = None
    formula = '''=IFERROR(C236/B236,"")'''
    @eval_fn
    def D236():
        c236_1 = Coal_Foreign_Imports.C236()
        b236_1 = Coal_Foreign_Imports.B236()
        var_1 = divide(c236_1, b236_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A237():
    # 'Coal_Foreign_Imports'!A237
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A237,"")'''
    @eval_fn
    def A237():
        a237_1 = Input_EIA_Imports_Coal_Foreign.A237()
        var_1 = IFERROR(a237_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B237():
    # 'Coal_Foreign_Imports'!B237
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K237,"")'''
    @eval_fn
    def B237():
        k237_1 = Input_EIA_Imports_Coal_Foreign.K237()
        var_1 = IFERROR(k237_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C237():
    # 'Coal_Foreign_Imports'!C237
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L237,"")'''
    @eval_fn
    def C237():
        l237_1 = Input_EIA_Imports_Coal_Foreign.L237()
        var_1 = IFERROR(l237_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D237():
    # 'Coal_Foreign_Imports'!D237
    value = None
    formula = '''=IFERROR(C237/B237,"")'''
    @eval_fn
    def D237():
        c237_1 = Coal_Foreign_Imports.C237()
        b237_1 = Coal_Foreign_Imports.B237()
        var_1 = divide(c237_1, b237_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A238():
    # 'Coal_Foreign_Imports'!A238
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A238,"")'''
    @eval_fn
    def A238():
        a238_1 = Input_EIA_Imports_Coal_Foreign.A238()
        var_1 = IFERROR(a238_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B238():
    # 'Coal_Foreign_Imports'!B238
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K238,"")'''
    @eval_fn
    def B238():
        k238_1 = Input_EIA_Imports_Coal_Foreign.K238()
        var_1 = IFERROR(k238_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C238():
    # 'Coal_Foreign_Imports'!C238
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L238,"")'''
    @eval_fn
    def C238():
        l238_1 = Input_EIA_Imports_Coal_Foreign.L238()
        var_1 = IFERROR(l238_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D238():
    # 'Coal_Foreign_Imports'!D238
    value = None
    formula = '''=IFERROR(C238/B238,"")'''
    @eval_fn
    def D238():
        c238_1 = Coal_Foreign_Imports.C238()
        b238_1 = Coal_Foreign_Imports.B238()
        var_1 = divide(c238_1, b238_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A239():
    # 'Coal_Foreign_Imports'!A239
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A239,"")'''
    @eval_fn
    def A239():
        a239_1 = Input_EIA_Imports_Coal_Foreign.A239()
        var_1 = IFERROR(a239_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B239():
    # 'Coal_Foreign_Imports'!B239
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K239,"")'''
    @eval_fn
    def B239():
        k239_1 = Input_EIA_Imports_Coal_Foreign.K239()
        var_1 = IFERROR(k239_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C239():
    # 'Coal_Foreign_Imports'!C239
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L239,"")'''
    @eval_fn
    def C239():
        l239_1 = Input_EIA_Imports_Coal_Foreign.L239()
        var_1 = IFERROR(l239_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D239():
    # 'Coal_Foreign_Imports'!D239
    value = None
    formula = '''=IFERROR(C239/B239,"")'''
    @eval_fn
    def D239():
        c239_1 = Coal_Foreign_Imports.C239()
        b239_1 = Coal_Foreign_Imports.B239()
        var_1 = divide(c239_1, b239_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A240():
    # 'Coal_Foreign_Imports'!A240
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A240,"")'''
    @eval_fn
    def A240():
        a240_1 = Input_EIA_Imports_Coal_Foreign.A240()
        var_1 = IFERROR(a240_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B240():
    # 'Coal_Foreign_Imports'!B240
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K240,"")'''
    @eval_fn
    def B240():
        k240_1 = Input_EIA_Imports_Coal_Foreign.K240()
        var_1 = IFERROR(k240_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C240():
    # 'Coal_Foreign_Imports'!C240
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L240,"")'''
    @eval_fn
    def C240():
        l240_1 = Input_EIA_Imports_Coal_Foreign.L240()
        var_1 = IFERROR(l240_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D240():
    # 'Coal_Foreign_Imports'!D240
    value = None
    formula = '''=IFERROR(C240/B240,"")'''
    @eval_fn
    def D240():
        c240_1 = Coal_Foreign_Imports.C240()
        b240_1 = Coal_Foreign_Imports.B240()
        var_1 = divide(c240_1, b240_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A241():
    # 'Coal_Foreign_Imports'!A241
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A241,"")'''
    @eval_fn
    def A241():
        a241_1 = Input_EIA_Imports_Coal_Foreign.A241()
        var_1 = IFERROR(a241_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B241():
    # 'Coal_Foreign_Imports'!B241
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K241,"")'''
    @eval_fn
    def B241():
        k241_1 = Input_EIA_Imports_Coal_Foreign.K241()
        var_1 = IFERROR(k241_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C241():
    # 'Coal_Foreign_Imports'!C241
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L241,"")'''
    @eval_fn
    def C241():
        l241_1 = Input_EIA_Imports_Coal_Foreign.L241()
        var_1 = IFERROR(l241_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D241():
    # 'Coal_Foreign_Imports'!D241
    value = None
    formula = '''=IFERROR(C241/B241,"")'''
    @eval_fn
    def D241():
        c241_1 = Coal_Foreign_Imports.C241()
        b241_1 = Coal_Foreign_Imports.B241()
        var_1 = divide(c241_1, b241_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A242():
    # 'Coal_Foreign_Imports'!A242
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A242,"")'''
    @eval_fn
    def A242():
        a242_1 = Input_EIA_Imports_Coal_Foreign.A242()
        var_1 = IFERROR(a242_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B242():
    # 'Coal_Foreign_Imports'!B242
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K242,"")'''
    @eval_fn
    def B242():
        k242_1 = Input_EIA_Imports_Coal_Foreign.K242()
        var_1 = IFERROR(k242_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C242():
    # 'Coal_Foreign_Imports'!C242
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L242,"")'''
    @eval_fn
    def C242():
        l242_1 = Input_EIA_Imports_Coal_Foreign.L242()
        var_1 = IFERROR(l242_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D242():
    # 'Coal_Foreign_Imports'!D242
    value = None
    formula = '''=IFERROR(C242/B242,"")'''
    @eval_fn
    def D242():
        c242_1 = Coal_Foreign_Imports.C242()
        b242_1 = Coal_Foreign_Imports.B242()
        var_1 = divide(c242_1, b242_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A243():
    # 'Coal_Foreign_Imports'!A243
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A243,"")'''
    @eval_fn
    def A243():
        a243_1 = Input_EIA_Imports_Coal_Foreign.A243()
        var_1 = IFERROR(a243_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B243():
    # 'Coal_Foreign_Imports'!B243
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K243,"")'''
    @eval_fn
    def B243():
        k243_1 = Input_EIA_Imports_Coal_Foreign.K243()
        var_1 = IFERROR(k243_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C243():
    # 'Coal_Foreign_Imports'!C243
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L243,"")'''
    @eval_fn
    def C243():
        l243_1 = Input_EIA_Imports_Coal_Foreign.L243()
        var_1 = IFERROR(l243_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D243():
    # 'Coal_Foreign_Imports'!D243
    value = None
    formula = '''=IFERROR(C243/B243,"")'''
    @eval_fn
    def D243():
        c243_1 = Coal_Foreign_Imports.C243()
        b243_1 = Coal_Foreign_Imports.B243()
        var_1 = divide(c243_1, b243_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A244():
    # 'Coal_Foreign_Imports'!A244
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A244,"")'''
    @eval_fn
    def A244():
        a244_1 = Input_EIA_Imports_Coal_Foreign.A244()
        var_1 = IFERROR(a244_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B244():
    # 'Coal_Foreign_Imports'!B244
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K244,"")'''
    @eval_fn
    def B244():
        k244_1 = Input_EIA_Imports_Coal_Foreign.K244()
        var_1 = IFERROR(k244_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C244():
    # 'Coal_Foreign_Imports'!C244
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L244,"")'''
    @eval_fn
    def C244():
        l244_1 = Input_EIA_Imports_Coal_Foreign.L244()
        var_1 = IFERROR(l244_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D244():
    # 'Coal_Foreign_Imports'!D244
    value = None
    formula = '''=IFERROR(C244/B244,"")'''
    @eval_fn
    def D244():
        c244_1 = Coal_Foreign_Imports.C244()
        b244_1 = Coal_Foreign_Imports.B244()
        var_1 = divide(c244_1, b244_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A245():
    # 'Coal_Foreign_Imports'!A245
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A245,"")'''
    @eval_fn
    def A245():
        a245_1 = Input_EIA_Imports_Coal_Foreign.A245()
        var_1 = IFERROR(a245_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B245():
    # 'Coal_Foreign_Imports'!B245
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K245,"")'''
    @eval_fn
    def B245():
        k245_1 = Input_EIA_Imports_Coal_Foreign.K245()
        var_1 = IFERROR(k245_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C245():
    # 'Coal_Foreign_Imports'!C245
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L245,"")'''
    @eval_fn
    def C245():
        l245_1 = Input_EIA_Imports_Coal_Foreign.L245()
        var_1 = IFERROR(l245_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D245():
    # 'Coal_Foreign_Imports'!D245
    value = None
    formula = '''=IFERROR(C245/B245,"")'''
    @eval_fn
    def D245():
        c245_1 = Coal_Foreign_Imports.C245()
        b245_1 = Coal_Foreign_Imports.B245()
        var_1 = divide(c245_1, b245_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A246():
    # 'Coal_Foreign_Imports'!A246
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A246,"")'''
    @eval_fn
    def A246():
        a246_1 = Input_EIA_Imports_Coal_Foreign.A246()
        var_1 = IFERROR(a246_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B246():
    # 'Coal_Foreign_Imports'!B246
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K246,"")'''
    @eval_fn
    def B246():
        k246_1 = Input_EIA_Imports_Coal_Foreign.K246()
        var_1 = IFERROR(k246_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C246():
    # 'Coal_Foreign_Imports'!C246
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L246,"")'''
    @eval_fn
    def C246():
        l246_1 = Input_EIA_Imports_Coal_Foreign.L246()
        var_1 = IFERROR(l246_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D246():
    # 'Coal_Foreign_Imports'!D246
    value = None
    formula = '''=IFERROR(C246/B246,"")'''
    @eval_fn
    def D246():
        c246_1 = Coal_Foreign_Imports.C246()
        b246_1 = Coal_Foreign_Imports.B246()
        var_1 = divide(c246_1, b246_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A247():
    # 'Coal_Foreign_Imports'!A247
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A247,"")'''
    @eval_fn
    def A247():
        a247_1 = Input_EIA_Imports_Coal_Foreign.A247()
        var_1 = IFERROR(a247_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B247():
    # 'Coal_Foreign_Imports'!B247
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K247,"")'''
    @eval_fn
    def B247():
        k247_1 = Input_EIA_Imports_Coal_Foreign.K247()
        var_1 = IFERROR(k247_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C247():
    # 'Coal_Foreign_Imports'!C247
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L247,"")'''
    @eval_fn
    def C247():
        l247_1 = Input_EIA_Imports_Coal_Foreign.L247()
        var_1 = IFERROR(l247_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D247():
    # 'Coal_Foreign_Imports'!D247
    value = None
    formula = '''=IFERROR(C247/B247,"")'''
    @eval_fn
    def D247():
        c247_1 = Coal_Foreign_Imports.C247()
        b247_1 = Coal_Foreign_Imports.B247()
        var_1 = divide(c247_1, b247_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A248():
    # 'Coal_Foreign_Imports'!A248
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A248,"")'''
    @eval_fn
    def A248():
        a248_1 = Input_EIA_Imports_Coal_Foreign.A248()
        var_1 = IFERROR(a248_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B248():
    # 'Coal_Foreign_Imports'!B248
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K248,"")'''
    @eval_fn
    def B248():
        k248_1 = Input_EIA_Imports_Coal_Foreign.K248()
        var_1 = IFERROR(k248_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C248():
    # 'Coal_Foreign_Imports'!C248
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L248,"")'''
    @eval_fn
    def C248():
        l248_1 = Input_EIA_Imports_Coal_Foreign.L248()
        var_1 = IFERROR(l248_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D248():
    # 'Coal_Foreign_Imports'!D248
    value = None
    formula = '''=IFERROR(C248/B248,"")'''
    @eval_fn
    def D248():
        c248_1 = Coal_Foreign_Imports.C248()
        b248_1 = Coal_Foreign_Imports.B248()
        var_1 = divide(c248_1, b248_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A249():
    # 'Coal_Foreign_Imports'!A249
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A249,"")'''
    @eval_fn
    def A249():
        a249_1 = Input_EIA_Imports_Coal_Foreign.A249()
        var_1 = IFERROR(a249_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B249():
    # 'Coal_Foreign_Imports'!B249
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K249,"")'''
    @eval_fn
    def B249():
        k249_1 = Input_EIA_Imports_Coal_Foreign.K249()
        var_1 = IFERROR(k249_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C249():
    # 'Coal_Foreign_Imports'!C249
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L249,"")'''
    @eval_fn
    def C249():
        l249_1 = Input_EIA_Imports_Coal_Foreign.L249()
        var_1 = IFERROR(l249_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D249():
    # 'Coal_Foreign_Imports'!D249
    value = None
    formula = '''=IFERROR(C249/B249,"")'''
    @eval_fn
    def D249():
        c249_1 = Coal_Foreign_Imports.C249()
        b249_1 = Coal_Foreign_Imports.B249()
        var_1 = divide(c249_1, b249_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A250():
    # 'Coal_Foreign_Imports'!A250
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A250,"")'''
    @eval_fn
    def A250():
        a250_1 = Input_EIA_Imports_Coal_Foreign.A250()
        var_1 = IFERROR(a250_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B250():
    # 'Coal_Foreign_Imports'!B250
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K250,"")'''
    @eval_fn
    def B250():
        k250_1 = Input_EIA_Imports_Coal_Foreign.K250()
        var_1 = IFERROR(k250_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C250():
    # 'Coal_Foreign_Imports'!C250
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L250,"")'''
    @eval_fn
    def C250():
        l250_1 = Input_EIA_Imports_Coal_Foreign.L250()
        var_1 = IFERROR(l250_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D250():
    # 'Coal_Foreign_Imports'!D250
    value = None
    formula = '''=IFERROR(C250/B250,"")'''
    @eval_fn
    def D250():
        c250_1 = Coal_Foreign_Imports.C250()
        b250_1 = Coal_Foreign_Imports.B250()
        var_1 = divide(c250_1, b250_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A251():
    # 'Coal_Foreign_Imports'!A251
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A251,"")'''
    @eval_fn
    def A251():
        a251_1 = Input_EIA_Imports_Coal_Foreign.A251()
        var_1 = IFERROR(a251_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B251():
    # 'Coal_Foreign_Imports'!B251
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K251,"")'''
    @eval_fn
    def B251():
        k251_1 = Input_EIA_Imports_Coal_Foreign.K251()
        var_1 = IFERROR(k251_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C251():
    # 'Coal_Foreign_Imports'!C251
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L251,"")'''
    @eval_fn
    def C251():
        l251_1 = Input_EIA_Imports_Coal_Foreign.L251()
        var_1 = IFERROR(l251_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D251():
    # 'Coal_Foreign_Imports'!D251
    value = None
    formula = '''=IFERROR(C251/B251,"")'''
    @eval_fn
    def D251():
        c251_1 = Coal_Foreign_Imports.C251()
        b251_1 = Coal_Foreign_Imports.B251()
        var_1 = divide(c251_1, b251_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A252():
    # 'Coal_Foreign_Imports'!A252
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A252,"")'''
    @eval_fn
    def A252():
        a252_1 = Input_EIA_Imports_Coal_Foreign.A252()
        var_1 = IFERROR(a252_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B252():
    # 'Coal_Foreign_Imports'!B252
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K252,"")'''
    @eval_fn
    def B252():
        k252_1 = Input_EIA_Imports_Coal_Foreign.K252()
        var_1 = IFERROR(k252_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C252():
    # 'Coal_Foreign_Imports'!C252
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L252,"")'''
    @eval_fn
    def C252():
        l252_1 = Input_EIA_Imports_Coal_Foreign.L252()
        var_1 = IFERROR(l252_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D252():
    # 'Coal_Foreign_Imports'!D252
    value = None
    formula = '''=IFERROR(C252/B252,"")'''
    @eval_fn
    def D252():
        c252_1 = Coal_Foreign_Imports.C252()
        b252_1 = Coal_Foreign_Imports.B252()
        var_1 = divide(c252_1, b252_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A253():
    # 'Coal_Foreign_Imports'!A253
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A253,"")'''
    @eval_fn
    def A253():
        a253_1 = Input_EIA_Imports_Coal_Foreign.A253()
        var_1 = IFERROR(a253_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B253():
    # 'Coal_Foreign_Imports'!B253
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K253,"")'''
    @eval_fn
    def B253():
        k253_1 = Input_EIA_Imports_Coal_Foreign.K253()
        var_1 = IFERROR(k253_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C253():
    # 'Coal_Foreign_Imports'!C253
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L253,"")'''
    @eval_fn
    def C253():
        l253_1 = Input_EIA_Imports_Coal_Foreign.L253()
        var_1 = IFERROR(l253_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D253():
    # 'Coal_Foreign_Imports'!D253
    value = None
    formula = '''=IFERROR(C253/B253,"")'''
    @eval_fn
    def D253():
        c253_1 = Coal_Foreign_Imports.C253()
        b253_1 = Coal_Foreign_Imports.B253()
        var_1 = divide(c253_1, b253_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A254():
    # 'Coal_Foreign_Imports'!A254
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A254,"")'''
    @eval_fn
    def A254():
        a254_1 = Input_EIA_Imports_Coal_Foreign.A254()
        var_1 = IFERROR(a254_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B254():
    # 'Coal_Foreign_Imports'!B254
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K254,"")'''
    @eval_fn
    def B254():
        k254_1 = Input_EIA_Imports_Coal_Foreign.K254()
        var_1 = IFERROR(k254_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C254():
    # 'Coal_Foreign_Imports'!C254
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L254,"")'''
    @eval_fn
    def C254():
        l254_1 = Input_EIA_Imports_Coal_Foreign.L254()
        var_1 = IFERROR(l254_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D254():
    # 'Coal_Foreign_Imports'!D254
    value = None
    formula = '''=IFERROR(C254/B254,"")'''
    @eval_fn
    def D254():
        c254_1 = Coal_Foreign_Imports.C254()
        b254_1 = Coal_Foreign_Imports.B254()
        var_1 = divide(c254_1, b254_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A255():
    # 'Coal_Foreign_Imports'!A255
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A255,"")'''
    @eval_fn
    def A255():
        a255_1 = Input_EIA_Imports_Coal_Foreign.A255()
        var_1 = IFERROR(a255_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B255():
    # 'Coal_Foreign_Imports'!B255
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K255,"")'''
    @eval_fn
    def B255():
        k255_1 = Input_EIA_Imports_Coal_Foreign.K255()
        var_1 = IFERROR(k255_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C255():
    # 'Coal_Foreign_Imports'!C255
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L255,"")'''
    @eval_fn
    def C255():
        l255_1 = Input_EIA_Imports_Coal_Foreign.L255()
        var_1 = IFERROR(l255_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D255():
    # 'Coal_Foreign_Imports'!D255
    value = None
    formula = '''=IFERROR(C255/B255,"")'''
    @eval_fn
    def D255():
        c255_1 = Coal_Foreign_Imports.C255()
        b255_1 = Coal_Foreign_Imports.B255()
        var_1 = divide(c255_1, b255_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A256():
    # 'Coal_Foreign_Imports'!A256
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A256,"")'''
    @eval_fn
    def A256():
        a256_1 = Input_EIA_Imports_Coal_Foreign.A256()
        var_1 = IFERROR(a256_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B256():
    # 'Coal_Foreign_Imports'!B256
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K256,"")'''
    @eval_fn
    def B256():
        k256_1 = Input_EIA_Imports_Coal_Foreign.K256()
        var_1 = IFERROR(k256_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C256():
    # 'Coal_Foreign_Imports'!C256
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L256,"")'''
    @eval_fn
    def C256():
        l256_1 = Input_EIA_Imports_Coal_Foreign.L256()
        var_1 = IFERROR(l256_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D256():
    # 'Coal_Foreign_Imports'!D256
    value = None
    formula = '''=IFERROR(C256/B256,"")'''
    @eval_fn
    def D256():
        c256_1 = Coal_Foreign_Imports.C256()
        b256_1 = Coal_Foreign_Imports.B256()
        var_1 = divide(c256_1, b256_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A257():
    # 'Coal_Foreign_Imports'!A257
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A257,"")'''
    @eval_fn
    def A257():
        a257_1 = Input_EIA_Imports_Coal_Foreign.A257()
        var_1 = IFERROR(a257_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B257():
    # 'Coal_Foreign_Imports'!B257
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K257,"")'''
    @eval_fn
    def B257():
        k257_1 = Input_EIA_Imports_Coal_Foreign.K257()
        var_1 = IFERROR(k257_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C257():
    # 'Coal_Foreign_Imports'!C257
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L257,"")'''
    @eval_fn
    def C257():
        l257_1 = Input_EIA_Imports_Coal_Foreign.L257()
        var_1 = IFERROR(l257_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D257():
    # 'Coal_Foreign_Imports'!D257
    value = None
    formula = '''=IFERROR(C257/B257,"")'''
    @eval_fn
    def D257():
        c257_1 = Coal_Foreign_Imports.C257()
        b257_1 = Coal_Foreign_Imports.B257()
        var_1 = divide(c257_1, b257_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A258():
    # 'Coal_Foreign_Imports'!A258
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A258,"")'''
    @eval_fn
    def A258():
        a258_1 = Input_EIA_Imports_Coal_Foreign.A258()
        var_1 = IFERROR(a258_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B258():
    # 'Coal_Foreign_Imports'!B258
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K258,"")'''
    @eval_fn
    def B258():
        k258_1 = Input_EIA_Imports_Coal_Foreign.K258()
        var_1 = IFERROR(k258_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C258():
    # 'Coal_Foreign_Imports'!C258
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L258,"")'''
    @eval_fn
    def C258():
        l258_1 = Input_EIA_Imports_Coal_Foreign.L258()
        var_1 = IFERROR(l258_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D258():
    # 'Coal_Foreign_Imports'!D258
    value = None
    formula = '''=IFERROR(C258/B258,"")'''
    @eval_fn
    def D258():
        c258_1 = Coal_Foreign_Imports.C258()
        b258_1 = Coal_Foreign_Imports.B258()
        var_1 = divide(c258_1, b258_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A259():
    # 'Coal_Foreign_Imports'!A259
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A259,"")'''
    @eval_fn
    def A259():
        a259_1 = Input_EIA_Imports_Coal_Foreign.A259()
        var_1 = IFERROR(a259_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B259():
    # 'Coal_Foreign_Imports'!B259
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K259,"")'''
    @eval_fn
    def B259():
        k259_1 = Input_EIA_Imports_Coal_Foreign.K259()
        var_1 = IFERROR(k259_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C259():
    # 'Coal_Foreign_Imports'!C259
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L259,"")'''
    @eval_fn
    def C259():
        l259_1 = Input_EIA_Imports_Coal_Foreign.L259()
        var_1 = IFERROR(l259_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D259():
    # 'Coal_Foreign_Imports'!D259
    value = None
    formula = '''=IFERROR(C259/B259,"")'''
    @eval_fn
    def D259():
        c259_1 = Coal_Foreign_Imports.C259()
        b259_1 = Coal_Foreign_Imports.B259()
        var_1 = divide(c259_1, b259_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A260():
    # 'Coal_Foreign_Imports'!A260
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A260,"")'''
    @eval_fn
    def A260():
        a260_1 = Input_EIA_Imports_Coal_Foreign.A260()
        var_1 = IFERROR(a260_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B260():
    # 'Coal_Foreign_Imports'!B260
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K260,"")'''
    @eval_fn
    def B260():
        k260_1 = Input_EIA_Imports_Coal_Foreign.K260()
        var_1 = IFERROR(k260_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C260():
    # 'Coal_Foreign_Imports'!C260
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L260,"")'''
    @eval_fn
    def C260():
        l260_1 = Input_EIA_Imports_Coal_Foreign.L260()
        var_1 = IFERROR(l260_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D260():
    # 'Coal_Foreign_Imports'!D260
    value = None
    formula = '''=IFERROR(C260/B260,"")'''
    @eval_fn
    def D260():
        c260_1 = Coal_Foreign_Imports.C260()
        b260_1 = Coal_Foreign_Imports.B260()
        var_1 = divide(c260_1, b260_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A261():
    # 'Coal_Foreign_Imports'!A261
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A261,"")'''
    @eval_fn
    def A261():
        a261_1 = Input_EIA_Imports_Coal_Foreign.A261()
        var_1 = IFERROR(a261_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B261():
    # 'Coal_Foreign_Imports'!B261
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K261,"")'''
    @eval_fn
    def B261():
        k261_1 = Input_EIA_Imports_Coal_Foreign.K261()
        var_1 = IFERROR(k261_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C261():
    # 'Coal_Foreign_Imports'!C261
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L261,"")'''
    @eval_fn
    def C261():
        l261_1 = Input_EIA_Imports_Coal_Foreign.L261()
        var_1 = IFERROR(l261_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D261():
    # 'Coal_Foreign_Imports'!D261
    value = None
    formula = '''=IFERROR(C261/B261,"")'''
    @eval_fn
    def D261():
        c261_1 = Coal_Foreign_Imports.C261()
        b261_1 = Coal_Foreign_Imports.B261()
        var_1 = divide(c261_1, b261_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A262():
    # 'Coal_Foreign_Imports'!A262
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A262,"")'''
    @eval_fn
    def A262():
        a262_1 = Input_EIA_Imports_Coal_Foreign.A262()
        var_1 = IFERROR(a262_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B262():
    # 'Coal_Foreign_Imports'!B262
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K262,"")'''
    @eval_fn
    def B262():
        k262_1 = Input_EIA_Imports_Coal_Foreign.K262()
        var_1 = IFERROR(k262_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C262():
    # 'Coal_Foreign_Imports'!C262
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L262,"")'''
    @eval_fn
    def C262():
        l262_1 = Input_EIA_Imports_Coal_Foreign.L262()
        var_1 = IFERROR(l262_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D262():
    # 'Coal_Foreign_Imports'!D262
    value = None
    formula = '''=IFERROR(C262/B262,"")'''
    @eval_fn
    def D262():
        c262_1 = Coal_Foreign_Imports.C262()
        b262_1 = Coal_Foreign_Imports.B262()
        var_1 = divide(c262_1, b262_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A263():
    # 'Coal_Foreign_Imports'!A263
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A263,"")'''
    @eval_fn
    def A263():
        a263_1 = Input_EIA_Imports_Coal_Foreign.A263()
        var_1 = IFERROR(a263_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B263():
    # 'Coal_Foreign_Imports'!B263
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K263,"")'''
    @eval_fn
    def B263():
        k263_1 = Input_EIA_Imports_Coal_Foreign.K263()
        var_1 = IFERROR(k263_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C263():
    # 'Coal_Foreign_Imports'!C263
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L263,"")'''
    @eval_fn
    def C263():
        l263_1 = Input_EIA_Imports_Coal_Foreign.L263()
        var_1 = IFERROR(l263_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D263():
    # 'Coal_Foreign_Imports'!D263
    value = None
    formula = '''=IFERROR(C263/B263,"")'''
    @eval_fn
    def D263():
        c263_1 = Coal_Foreign_Imports.C263()
        b263_1 = Coal_Foreign_Imports.B263()
        var_1 = divide(c263_1, b263_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A264():
    # 'Coal_Foreign_Imports'!A264
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A264,"")'''
    @eval_fn
    def A264():
        a264_1 = Input_EIA_Imports_Coal_Foreign.A264()
        var_1 = IFERROR(a264_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B264():
    # 'Coal_Foreign_Imports'!B264
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K264,"")'''
    @eval_fn
    def B264():
        k264_1 = Input_EIA_Imports_Coal_Foreign.K264()
        var_1 = IFERROR(k264_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C264():
    # 'Coal_Foreign_Imports'!C264
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L264,"")'''
    @eval_fn
    def C264():
        l264_1 = Input_EIA_Imports_Coal_Foreign.L264()
        var_1 = IFERROR(l264_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D264():
    # 'Coal_Foreign_Imports'!D264
    value = None
    formula = '''=IFERROR(C264/B264,"")'''
    @eval_fn
    def D264():
        c264_1 = Coal_Foreign_Imports.C264()
        b264_1 = Coal_Foreign_Imports.B264()
        var_1 = divide(c264_1, b264_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A265():
    # 'Coal_Foreign_Imports'!A265
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A265,"")'''
    @eval_fn
    def A265():
        a265_1 = Input_EIA_Imports_Coal_Foreign.A265()
        var_1 = IFERROR(a265_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B265():
    # 'Coal_Foreign_Imports'!B265
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K265,"")'''
    @eval_fn
    def B265():
        k265_1 = Input_EIA_Imports_Coal_Foreign.K265()
        var_1 = IFERROR(k265_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C265():
    # 'Coal_Foreign_Imports'!C265
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L265,"")'''
    @eval_fn
    def C265():
        l265_1 = Input_EIA_Imports_Coal_Foreign.L265()
        var_1 = IFERROR(l265_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D265():
    # 'Coal_Foreign_Imports'!D265
    value = None
    formula = '''=IFERROR(C265/B265,"")'''
    @eval_fn
    def D265():
        c265_1 = Coal_Foreign_Imports.C265()
        b265_1 = Coal_Foreign_Imports.B265()
        var_1 = divide(c265_1, b265_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A266():
    # 'Coal_Foreign_Imports'!A266
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A266,"")'''
    @eval_fn
    def A266():
        a266_1 = Input_EIA_Imports_Coal_Foreign.A266()
        var_1 = IFERROR(a266_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B266():
    # 'Coal_Foreign_Imports'!B266
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K266,"")'''
    @eval_fn
    def B266():
        k266_1 = Input_EIA_Imports_Coal_Foreign.K266()
        var_1 = IFERROR(k266_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C266():
    # 'Coal_Foreign_Imports'!C266
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L266,"")'''
    @eval_fn
    def C266():
        l266_1 = Input_EIA_Imports_Coal_Foreign.L266()
        var_1 = IFERROR(l266_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D266():
    # 'Coal_Foreign_Imports'!D266
    value = None
    formula = '''=IFERROR(C266/B266,"")'''
    @eval_fn
    def D266():
        c266_1 = Coal_Foreign_Imports.C266()
        b266_1 = Coal_Foreign_Imports.B266()
        var_1 = divide(c266_1, b266_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A267():
    # 'Coal_Foreign_Imports'!A267
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A267,"")'''
    @eval_fn
    def A267():
        a267_1 = Input_EIA_Imports_Coal_Foreign.A267()
        var_1 = IFERROR(a267_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B267():
    # 'Coal_Foreign_Imports'!B267
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K267,"")'''
    @eval_fn
    def B267():
        k267_1 = Input_EIA_Imports_Coal_Foreign.K267()
        var_1 = IFERROR(k267_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C267():
    # 'Coal_Foreign_Imports'!C267
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L267,"")'''
    @eval_fn
    def C267():
        l267_1 = Input_EIA_Imports_Coal_Foreign.L267()
        var_1 = IFERROR(l267_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D267():
    # 'Coal_Foreign_Imports'!D267
    value = None
    formula = '''=IFERROR(C267/B267,"")'''
    @eval_fn
    def D267():
        c267_1 = Coal_Foreign_Imports.C267()
        b267_1 = Coal_Foreign_Imports.B267()
        var_1 = divide(c267_1, b267_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A268():
    # 'Coal_Foreign_Imports'!A268
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A268,"")'''
    @eval_fn
    def A268():
        a268_1 = Input_EIA_Imports_Coal_Foreign.A268()
        var_1 = IFERROR(a268_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B268():
    # 'Coal_Foreign_Imports'!B268
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K268,"")'''
    @eval_fn
    def B268():
        k268_1 = Input_EIA_Imports_Coal_Foreign.K268()
        var_1 = IFERROR(k268_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C268():
    # 'Coal_Foreign_Imports'!C268
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L268,"")'''
    @eval_fn
    def C268():
        l268_1 = Input_EIA_Imports_Coal_Foreign.L268()
        var_1 = IFERROR(l268_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D268():
    # 'Coal_Foreign_Imports'!D268
    value = None
    formula = '''=IFERROR(C268/B268,"")'''
    @eval_fn
    def D268():
        c268_1 = Coal_Foreign_Imports.C268()
        b268_1 = Coal_Foreign_Imports.B268()
        var_1 = divide(c268_1, b268_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A269():
    # 'Coal_Foreign_Imports'!A269
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A269,"")'''
    @eval_fn
    def A269():
        a269_1 = Input_EIA_Imports_Coal_Foreign.A269()
        var_1 = IFERROR(a269_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B269():
    # 'Coal_Foreign_Imports'!B269
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K269,"")'''
    @eval_fn
    def B269():
        k269_1 = Input_EIA_Imports_Coal_Foreign.K269()
        var_1 = IFERROR(k269_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C269():
    # 'Coal_Foreign_Imports'!C269
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L269,"")'''
    @eval_fn
    def C269():
        l269_1 = Input_EIA_Imports_Coal_Foreign.L269()
        var_1 = IFERROR(l269_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D269():
    # 'Coal_Foreign_Imports'!D269
    value = None
    formula = '''=IFERROR(C269/B269,"")'''
    @eval_fn
    def D269():
        c269_1 = Coal_Foreign_Imports.C269()
        b269_1 = Coal_Foreign_Imports.B269()
        var_1 = divide(c269_1, b269_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A270():
    # 'Coal_Foreign_Imports'!A270
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A270,"")'''
    @eval_fn
    def A270():
        a270_1 = Input_EIA_Imports_Coal_Foreign.A270()
        var_1 = IFERROR(a270_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B270():
    # 'Coal_Foreign_Imports'!B270
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K270,"")'''
    @eval_fn
    def B270():
        k270_1 = Input_EIA_Imports_Coal_Foreign.K270()
        var_1 = IFERROR(k270_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C270():
    # 'Coal_Foreign_Imports'!C270
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L270,"")'''
    @eval_fn
    def C270():
        l270_1 = Input_EIA_Imports_Coal_Foreign.L270()
        var_1 = IFERROR(l270_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D270():
    # 'Coal_Foreign_Imports'!D270
    value = None
    formula = '''=IFERROR(C270/B270,"")'''
    @eval_fn
    def D270():
        c270_1 = Coal_Foreign_Imports.C270()
        b270_1 = Coal_Foreign_Imports.B270()
        var_1 = divide(c270_1, b270_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A271():
    # 'Coal_Foreign_Imports'!A271
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A271,"")'''
    @eval_fn
    def A271():
        a271_1 = Input_EIA_Imports_Coal_Foreign.A271()
        var_1 = IFERROR(a271_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B271():
    # 'Coal_Foreign_Imports'!B271
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K271,"")'''
    @eval_fn
    def B271():
        k271_1 = Input_EIA_Imports_Coal_Foreign.K271()
        var_1 = IFERROR(k271_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C271():
    # 'Coal_Foreign_Imports'!C271
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L271,"")'''
    @eval_fn
    def C271():
        l271_1 = Input_EIA_Imports_Coal_Foreign.L271()
        var_1 = IFERROR(l271_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D271():
    # 'Coal_Foreign_Imports'!D271
    value = None
    formula = '''=IFERROR(C271/B271,"")'''
    @eval_fn
    def D271():
        c271_1 = Coal_Foreign_Imports.C271()
        b271_1 = Coal_Foreign_Imports.B271()
        var_1 = divide(c271_1, b271_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A272():
    # 'Coal_Foreign_Imports'!A272
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A272,"")'''
    @eval_fn
    def A272():
        a272_1 = Input_EIA_Imports_Coal_Foreign.A272()
        var_1 = IFERROR(a272_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B272():
    # 'Coal_Foreign_Imports'!B272
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K272,"")'''
    @eval_fn
    def B272():
        k272_1 = Input_EIA_Imports_Coal_Foreign.K272()
        var_1 = IFERROR(k272_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C272():
    # 'Coal_Foreign_Imports'!C272
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L272,"")'''
    @eval_fn
    def C272():
        l272_1 = Input_EIA_Imports_Coal_Foreign.L272()
        var_1 = IFERROR(l272_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D272():
    # 'Coal_Foreign_Imports'!D272
    value = None
    formula = '''=IFERROR(C272/B272,"")'''
    @eval_fn
    def D272():
        c272_1 = Coal_Foreign_Imports.C272()
        b272_1 = Coal_Foreign_Imports.B272()
        var_1 = divide(c272_1, b272_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A273():
    # 'Coal_Foreign_Imports'!A273
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A273,"")'''
    @eval_fn
    def A273():
        a273_1 = Input_EIA_Imports_Coal_Foreign.A273()
        var_1 = IFERROR(a273_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B273():
    # 'Coal_Foreign_Imports'!B273
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K273,"")'''
    @eval_fn
    def B273():
        k273_1 = Input_EIA_Imports_Coal_Foreign.K273()
        var_1 = IFERROR(k273_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C273():
    # 'Coal_Foreign_Imports'!C273
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L273,"")'''
    @eval_fn
    def C273():
        l273_1 = Input_EIA_Imports_Coal_Foreign.L273()
        var_1 = IFERROR(l273_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D273():
    # 'Coal_Foreign_Imports'!D273
    value = None
    formula = '''=IFERROR(C273/B273,"")'''
    @eval_fn
    def D273():
        c273_1 = Coal_Foreign_Imports.C273()
        b273_1 = Coal_Foreign_Imports.B273()
        var_1 = divide(c273_1, b273_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A274():
    # 'Coal_Foreign_Imports'!A274
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A274,"")'''
    @eval_fn
    def A274():
        a274_1 = Input_EIA_Imports_Coal_Foreign.A274()
        var_1 = IFERROR(a274_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B274():
    # 'Coal_Foreign_Imports'!B274
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K274,"")'''
    @eval_fn
    def B274():
        k274_1 = Input_EIA_Imports_Coal_Foreign.K274()
        var_1 = IFERROR(k274_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C274():
    # 'Coal_Foreign_Imports'!C274
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L274,"")'''
    @eval_fn
    def C274():
        l274_1 = Input_EIA_Imports_Coal_Foreign.L274()
        var_1 = IFERROR(l274_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D274():
    # 'Coal_Foreign_Imports'!D274
    value = None
    formula = '''=IFERROR(C274/B274,"")'''
    @eval_fn
    def D274():
        c274_1 = Coal_Foreign_Imports.C274()
        b274_1 = Coal_Foreign_Imports.B274()
        var_1 = divide(c274_1, b274_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A275():
    # 'Coal_Foreign_Imports'!A275
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A275,"")'''
    @eval_fn
    def A275():
        a275_1 = Input_EIA_Imports_Coal_Foreign.A275()
        var_1 = IFERROR(a275_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B275():
    # 'Coal_Foreign_Imports'!B275
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K275,"")'''
    @eval_fn
    def B275():
        k275_1 = Input_EIA_Imports_Coal_Foreign.K275()
        var_1 = IFERROR(k275_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C275():
    # 'Coal_Foreign_Imports'!C275
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L275,"")'''
    @eval_fn
    def C275():
        l275_1 = Input_EIA_Imports_Coal_Foreign.L275()
        var_1 = IFERROR(l275_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D275():
    # 'Coal_Foreign_Imports'!D275
    value = None
    formula = '''=IFERROR(C275/B275,"")'''
    @eval_fn
    def D275():
        c275_1 = Coal_Foreign_Imports.C275()
        b275_1 = Coal_Foreign_Imports.B275()
        var_1 = divide(c275_1, b275_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A276():
    # 'Coal_Foreign_Imports'!A276
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A276,"")'''
    @eval_fn
    def A276():
        a276_1 = Input_EIA_Imports_Coal_Foreign.A276()
        var_1 = IFERROR(a276_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B276():
    # 'Coal_Foreign_Imports'!B276
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K276,"")'''
    @eval_fn
    def B276():
        k276_1 = Input_EIA_Imports_Coal_Foreign.K276()
        var_1 = IFERROR(k276_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C276():
    # 'Coal_Foreign_Imports'!C276
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L276,"")'''
    @eval_fn
    def C276():
        l276_1 = Input_EIA_Imports_Coal_Foreign.L276()
        var_1 = IFERROR(l276_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D276():
    # 'Coal_Foreign_Imports'!D276
    value = None
    formula = '''=IFERROR(C276/B276,"")'''
    @eval_fn
    def D276():
        c276_1 = Coal_Foreign_Imports.C276()
        b276_1 = Coal_Foreign_Imports.B276()
        var_1 = divide(c276_1, b276_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A277():
    # 'Coal_Foreign_Imports'!A277
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A277,"")'''
    @eval_fn
    def A277():
        a277_1 = Input_EIA_Imports_Coal_Foreign.A277()
        var_1 = IFERROR(a277_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B277():
    # 'Coal_Foreign_Imports'!B277
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K277,"")'''
    @eval_fn
    def B277():
        k277_1 = Input_EIA_Imports_Coal_Foreign.K277()
        var_1 = IFERROR(k277_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C277():
    # 'Coal_Foreign_Imports'!C277
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L277,"")'''
    @eval_fn
    def C277():
        l277_1 = Input_EIA_Imports_Coal_Foreign.L277()
        var_1 = IFERROR(l277_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D277():
    # 'Coal_Foreign_Imports'!D277
    value = None
    formula = '''=IFERROR(C277/B277,"")'''
    @eval_fn
    def D277():
        c277_1 = Coal_Foreign_Imports.C277()
        b277_1 = Coal_Foreign_Imports.B277()
        var_1 = divide(c277_1, b277_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A278():
    # 'Coal_Foreign_Imports'!A278
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A278,"")'''
    @eval_fn
    def A278():
        a278_1 = Input_EIA_Imports_Coal_Foreign.A278()
        var_1 = IFERROR(a278_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B278():
    # 'Coal_Foreign_Imports'!B278
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K278,"")'''
    @eval_fn
    def B278():
        k278_1 = Input_EIA_Imports_Coal_Foreign.K278()
        var_1 = IFERROR(k278_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C278():
    # 'Coal_Foreign_Imports'!C278
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L278,"")'''
    @eval_fn
    def C278():
        l278_1 = Input_EIA_Imports_Coal_Foreign.L278()
        var_1 = IFERROR(l278_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D278():
    # 'Coal_Foreign_Imports'!D278
    value = None
    formula = '''=IFERROR(C278/B278,"")'''
    @eval_fn
    def D278():
        c278_1 = Coal_Foreign_Imports.C278()
        b278_1 = Coal_Foreign_Imports.B278()
        var_1 = divide(c278_1, b278_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A279():
    # 'Coal_Foreign_Imports'!A279
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A279,"")'''
    @eval_fn
    def A279():
        a279_1 = Input_EIA_Imports_Coal_Foreign.A279()
        var_1 = IFERROR(a279_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B279():
    # 'Coal_Foreign_Imports'!B279
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K279,"")'''
    @eval_fn
    def B279():
        k279_1 = Input_EIA_Imports_Coal_Foreign.K279()
        var_1 = IFERROR(k279_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C279():
    # 'Coal_Foreign_Imports'!C279
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L279,"")'''
    @eval_fn
    def C279():
        l279_1 = Input_EIA_Imports_Coal_Foreign.L279()
        var_1 = IFERROR(l279_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D279():
    # 'Coal_Foreign_Imports'!D279
    value = None
    formula = '''=IFERROR(C279/B279,"")'''
    @eval_fn
    def D279():
        c279_1 = Coal_Foreign_Imports.C279()
        b279_1 = Coal_Foreign_Imports.B279()
        var_1 = divide(c279_1, b279_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A280():
    # 'Coal_Foreign_Imports'!A280
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A280,"")'''
    @eval_fn
    def A280():
        a280_1 = Input_EIA_Imports_Coal_Foreign.A280()
        var_1 = IFERROR(a280_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B280():
    # 'Coal_Foreign_Imports'!B280
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K280,"")'''
    @eval_fn
    def B280():
        k280_1 = Input_EIA_Imports_Coal_Foreign.K280()
        var_1 = IFERROR(k280_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C280():
    # 'Coal_Foreign_Imports'!C280
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L280,"")'''
    @eval_fn
    def C280():
        l280_1 = Input_EIA_Imports_Coal_Foreign.L280()
        var_1 = IFERROR(l280_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D280():
    # 'Coal_Foreign_Imports'!D280
    value = None
    formula = '''=IFERROR(C280/B280,"")'''
    @eval_fn
    def D280():
        c280_1 = Coal_Foreign_Imports.C280()
        b280_1 = Coal_Foreign_Imports.B280()
        var_1 = divide(c280_1, b280_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A281():
    # 'Coal_Foreign_Imports'!A281
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A281,"")'''
    @eval_fn
    def A281():
        a281_1 = Input_EIA_Imports_Coal_Foreign.A281()
        var_1 = IFERROR(a281_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B281():
    # 'Coal_Foreign_Imports'!B281
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K281,"")'''
    @eval_fn
    def B281():
        k281_1 = Input_EIA_Imports_Coal_Foreign.K281()
        var_1 = IFERROR(k281_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C281():
    # 'Coal_Foreign_Imports'!C281
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L281,"")'''
    @eval_fn
    def C281():
        l281_1 = Input_EIA_Imports_Coal_Foreign.L281()
        var_1 = IFERROR(l281_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D281():
    # 'Coal_Foreign_Imports'!D281
    value = None
    formula = '''=IFERROR(C281/B281,"")'''
    @eval_fn
    def D281():
        c281_1 = Coal_Foreign_Imports.C281()
        b281_1 = Coal_Foreign_Imports.B281()
        var_1 = divide(c281_1, b281_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A282():
    # 'Coal_Foreign_Imports'!A282
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A282,"")'''
    @eval_fn
    def A282():
        a282_1 = Input_EIA_Imports_Coal_Foreign.A282()
        var_1 = IFERROR(a282_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B282():
    # 'Coal_Foreign_Imports'!B282
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K282,"")'''
    @eval_fn
    def B282():
        k282_1 = Input_EIA_Imports_Coal_Foreign.K282()
        var_1 = IFERROR(k282_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C282():
    # 'Coal_Foreign_Imports'!C282
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L282,"")'''
    @eval_fn
    def C282():
        l282_1 = Input_EIA_Imports_Coal_Foreign.L282()
        var_1 = IFERROR(l282_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D282():
    # 'Coal_Foreign_Imports'!D282
    value = None
    formula = '''=IFERROR(C282/B282,"")'''
    @eval_fn
    def D282():
        c282_1 = Coal_Foreign_Imports.C282()
        b282_1 = Coal_Foreign_Imports.B282()
        var_1 = divide(c282_1, b282_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A283():
    # 'Coal_Foreign_Imports'!A283
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A283,"")'''
    @eval_fn
    def A283():
        a283_1 = Input_EIA_Imports_Coal_Foreign.A283()
        var_1 = IFERROR(a283_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B283():
    # 'Coal_Foreign_Imports'!B283
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K283,"")'''
    @eval_fn
    def B283():
        k283_1 = Input_EIA_Imports_Coal_Foreign.K283()
        var_1 = IFERROR(k283_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C283():
    # 'Coal_Foreign_Imports'!C283
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L283,"")'''
    @eval_fn
    def C283():
        l283_1 = Input_EIA_Imports_Coal_Foreign.L283()
        var_1 = IFERROR(l283_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D283():
    # 'Coal_Foreign_Imports'!D283
    value = None
    formula = '''=IFERROR(C283/B283,"")'''
    @eval_fn
    def D283():
        c283_1 = Coal_Foreign_Imports.C283()
        b283_1 = Coal_Foreign_Imports.B283()
        var_1 = divide(c283_1, b283_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A284():
    # 'Coal_Foreign_Imports'!A284
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A284,"")'''
    @eval_fn
    def A284():
        a284_1 = Input_EIA_Imports_Coal_Foreign.A284()
        var_1 = IFERROR(a284_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B284():
    # 'Coal_Foreign_Imports'!B284
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K284,"")'''
    @eval_fn
    def B284():
        k284_1 = Input_EIA_Imports_Coal_Foreign.K284()
        var_1 = IFERROR(k284_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C284():
    # 'Coal_Foreign_Imports'!C284
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L284,"")'''
    @eval_fn
    def C284():
        l284_1 = Input_EIA_Imports_Coal_Foreign.L284()
        var_1 = IFERROR(l284_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D284():
    # 'Coal_Foreign_Imports'!D284
    value = None
    formula = '''=IFERROR(C284/B284,"")'''
    @eval_fn
    def D284():
        c284_1 = Coal_Foreign_Imports.C284()
        b284_1 = Coal_Foreign_Imports.B284()
        var_1 = divide(c284_1, b284_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A285():
    # 'Coal_Foreign_Imports'!A285
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A285,"")'''
    @eval_fn
    def A285():
        a285_1 = Input_EIA_Imports_Coal_Foreign.A285()
        var_1 = IFERROR(a285_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B285():
    # 'Coal_Foreign_Imports'!B285
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K285,"")'''
    @eval_fn
    def B285():
        k285_1 = Input_EIA_Imports_Coal_Foreign.K285()
        var_1 = IFERROR(k285_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C285():
    # 'Coal_Foreign_Imports'!C285
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L285,"")'''
    @eval_fn
    def C285():
        l285_1 = Input_EIA_Imports_Coal_Foreign.L285()
        var_1 = IFERROR(l285_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D285():
    # 'Coal_Foreign_Imports'!D285
    value = None
    formula = '''=IFERROR(C285/B285,"")'''
    @eval_fn
    def D285():
        c285_1 = Coal_Foreign_Imports.C285()
        b285_1 = Coal_Foreign_Imports.B285()
        var_1 = divide(c285_1, b285_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A286():
    # 'Coal_Foreign_Imports'!A286
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A286,"")'''
    @eval_fn
    def A286():
        a286_1 = Input_EIA_Imports_Coal_Foreign.A286()
        var_1 = IFERROR(a286_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B286():
    # 'Coal_Foreign_Imports'!B286
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K286,"")'''
    @eval_fn
    def B286():
        k286_1 = Input_EIA_Imports_Coal_Foreign.K286()
        var_1 = IFERROR(k286_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C286():
    # 'Coal_Foreign_Imports'!C286
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L286,"")'''
    @eval_fn
    def C286():
        l286_1 = Input_EIA_Imports_Coal_Foreign.L286()
        var_1 = IFERROR(l286_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D286():
    # 'Coal_Foreign_Imports'!D286
    value = None
    formula = '''=IFERROR(C286/B286,"")'''
    @eval_fn
    def D286():
        c286_1 = Coal_Foreign_Imports.C286()
        b286_1 = Coal_Foreign_Imports.B286()
        var_1 = divide(c286_1, b286_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A287():
    # 'Coal_Foreign_Imports'!A287
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A287,"")'''
    @eval_fn
    def A287():
        a287_1 = Input_EIA_Imports_Coal_Foreign.A287()
        var_1 = IFERROR(a287_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B287():
    # 'Coal_Foreign_Imports'!B287
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K287,"")'''
    @eval_fn
    def B287():
        k287_1 = Input_EIA_Imports_Coal_Foreign.K287()
        var_1 = IFERROR(k287_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C287():
    # 'Coal_Foreign_Imports'!C287
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L287,"")'''
    @eval_fn
    def C287():
        l287_1 = Input_EIA_Imports_Coal_Foreign.L287()
        var_1 = IFERROR(l287_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D287():
    # 'Coal_Foreign_Imports'!D287
    value = None
    formula = '''=IFERROR(C287/B287,"")'''
    @eval_fn
    def D287():
        c287_1 = Coal_Foreign_Imports.C287()
        b287_1 = Coal_Foreign_Imports.B287()
        var_1 = divide(c287_1, b287_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A288():
    # 'Coal_Foreign_Imports'!A288
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A288,"")'''
    @eval_fn
    def A288():
        a288_1 = Input_EIA_Imports_Coal_Foreign.A288()
        var_1 = IFERROR(a288_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B288():
    # 'Coal_Foreign_Imports'!B288
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K288,"")'''
    @eval_fn
    def B288():
        k288_1 = Input_EIA_Imports_Coal_Foreign.K288()
        var_1 = IFERROR(k288_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C288():
    # 'Coal_Foreign_Imports'!C288
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L288,"")'''
    @eval_fn
    def C288():
        l288_1 = Input_EIA_Imports_Coal_Foreign.L288()
        var_1 = IFERROR(l288_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D288():
    # 'Coal_Foreign_Imports'!D288
    value = None
    formula = '''=IFERROR(C288/B288,"")'''
    @eval_fn
    def D288():
        c288_1 = Coal_Foreign_Imports.C288()
        b288_1 = Coal_Foreign_Imports.B288()
        var_1 = divide(c288_1, b288_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A289():
    # 'Coal_Foreign_Imports'!A289
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A289,"")'''
    @eval_fn
    def A289():
        a289_1 = Input_EIA_Imports_Coal_Foreign.A289()
        var_1 = IFERROR(a289_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B289():
    # 'Coal_Foreign_Imports'!B289
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K289,"")'''
    @eval_fn
    def B289():
        k289_1 = Input_EIA_Imports_Coal_Foreign.K289()
        var_1 = IFERROR(k289_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C289():
    # 'Coal_Foreign_Imports'!C289
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L289,"")'''
    @eval_fn
    def C289():
        l289_1 = Input_EIA_Imports_Coal_Foreign.L289()
        var_1 = IFERROR(l289_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D289():
    # 'Coal_Foreign_Imports'!D289
    value = None
    formula = '''=IFERROR(C289/B289,"")'''
    @eval_fn
    def D289():
        c289_1 = Coal_Foreign_Imports.C289()
        b289_1 = Coal_Foreign_Imports.B289()
        var_1 = divide(c289_1, b289_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A290():
    # 'Coal_Foreign_Imports'!A290
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A290,"")'''
    @eval_fn
    def A290():
        a290_1 = Input_EIA_Imports_Coal_Foreign.A290()
        var_1 = IFERROR(a290_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B290():
    # 'Coal_Foreign_Imports'!B290
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K290,"")'''
    @eval_fn
    def B290():
        k290_1 = Input_EIA_Imports_Coal_Foreign.K290()
        var_1 = IFERROR(k290_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C290():
    # 'Coal_Foreign_Imports'!C290
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L290,"")'''
    @eval_fn
    def C290():
        l290_1 = Input_EIA_Imports_Coal_Foreign.L290()
        var_1 = IFERROR(l290_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D290():
    # 'Coal_Foreign_Imports'!D290
    value = None
    formula = '''=IFERROR(C290/B290,"")'''
    @eval_fn
    def D290():
        c290_1 = Coal_Foreign_Imports.C290()
        b290_1 = Coal_Foreign_Imports.B290()
        var_1 = divide(c290_1, b290_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A291():
    # 'Coal_Foreign_Imports'!A291
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A291,"")'''
    @eval_fn
    def A291():
        a291_1 = Input_EIA_Imports_Coal_Foreign.A291()
        var_1 = IFERROR(a291_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B291():
    # 'Coal_Foreign_Imports'!B291
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K291,"")'''
    @eval_fn
    def B291():
        k291_1 = Input_EIA_Imports_Coal_Foreign.K291()
        var_1 = IFERROR(k291_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C291():
    # 'Coal_Foreign_Imports'!C291
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L291,"")'''
    @eval_fn
    def C291():
        l291_1 = Input_EIA_Imports_Coal_Foreign.L291()
        var_1 = IFERROR(l291_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D291():
    # 'Coal_Foreign_Imports'!D291
    value = None
    formula = '''=IFERROR(C291/B291,"")'''
    @eval_fn
    def D291():
        c291_1 = Coal_Foreign_Imports.C291()
        b291_1 = Coal_Foreign_Imports.B291()
        var_1 = divide(c291_1, b291_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A292():
    # 'Coal_Foreign_Imports'!A292
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A292,"")'''
    @eval_fn
    def A292():
        a292_1 = Input_EIA_Imports_Coal_Foreign.A292()
        var_1 = IFERROR(a292_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B292():
    # 'Coal_Foreign_Imports'!B292
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K292,"")'''
    @eval_fn
    def B292():
        k292_1 = Input_EIA_Imports_Coal_Foreign.K292()
        var_1 = IFERROR(k292_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C292():
    # 'Coal_Foreign_Imports'!C292
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L292,"")'''
    @eval_fn
    def C292():
        l292_1 = Input_EIA_Imports_Coal_Foreign.L292()
        var_1 = IFERROR(l292_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D292():
    # 'Coal_Foreign_Imports'!D292
    value = None
    formula = '''=IFERROR(C292/B292,"")'''
    @eval_fn
    def D292():
        c292_1 = Coal_Foreign_Imports.C292()
        b292_1 = Coal_Foreign_Imports.B292()
        var_1 = divide(c292_1, b292_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A293():
    # 'Coal_Foreign_Imports'!A293
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A293,"")'''
    @eval_fn
    def A293():
        a293_1 = Input_EIA_Imports_Coal_Foreign.A293()
        var_1 = IFERROR(a293_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B293():
    # 'Coal_Foreign_Imports'!B293
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K293,"")'''
    @eval_fn
    def B293():
        k293_1 = Input_EIA_Imports_Coal_Foreign.K293()
        var_1 = IFERROR(k293_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C293():
    # 'Coal_Foreign_Imports'!C293
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L293,"")'''
    @eval_fn
    def C293():
        l293_1 = Input_EIA_Imports_Coal_Foreign.L293()
        var_1 = IFERROR(l293_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D293():
    # 'Coal_Foreign_Imports'!D293
    value = None
    formula = '''=IFERROR(C293/B293,"")'''
    @eval_fn
    def D293():
        c293_1 = Coal_Foreign_Imports.C293()
        b293_1 = Coal_Foreign_Imports.B293()
        var_1 = divide(c293_1, b293_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A294():
    # 'Coal_Foreign_Imports'!A294
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A294,"")'''
    @eval_fn
    def A294():
        a294_1 = Input_EIA_Imports_Coal_Foreign.A294()
        var_1 = IFERROR(a294_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B294():
    # 'Coal_Foreign_Imports'!B294
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K294,"")'''
    @eval_fn
    def B294():
        k294_1 = Input_EIA_Imports_Coal_Foreign.K294()
        var_1 = IFERROR(k294_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C294():
    # 'Coal_Foreign_Imports'!C294
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L294,"")'''
    @eval_fn
    def C294():
        l294_1 = Input_EIA_Imports_Coal_Foreign.L294()
        var_1 = IFERROR(l294_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D294():
    # 'Coal_Foreign_Imports'!D294
    value = None
    formula = '''=IFERROR(C294/B294,"")'''
    @eval_fn
    def D294():
        c294_1 = Coal_Foreign_Imports.C294()
        b294_1 = Coal_Foreign_Imports.B294()
        var_1 = divide(c294_1, b294_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A295():
    # 'Coal_Foreign_Imports'!A295
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A295,"")'''
    @eval_fn
    def A295():
        a295_1 = Input_EIA_Imports_Coal_Foreign.A295()
        var_1 = IFERROR(a295_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B295():
    # 'Coal_Foreign_Imports'!B295
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K295,"")'''
    @eval_fn
    def B295():
        k295_1 = Input_EIA_Imports_Coal_Foreign.K295()
        var_1 = IFERROR(k295_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C295():
    # 'Coal_Foreign_Imports'!C295
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L295,"")'''
    @eval_fn
    def C295():
        l295_1 = Input_EIA_Imports_Coal_Foreign.L295()
        var_1 = IFERROR(l295_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D295():
    # 'Coal_Foreign_Imports'!D295
    value = None
    formula = '''=IFERROR(C295/B295,"")'''
    @eval_fn
    def D295():
        c295_1 = Coal_Foreign_Imports.C295()
        b295_1 = Coal_Foreign_Imports.B295()
        var_1 = divide(c295_1, b295_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A296():
    # 'Coal_Foreign_Imports'!A296
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A296,"")'''
    @eval_fn
    def A296():
        a296_1 = Input_EIA_Imports_Coal_Foreign.A296()
        var_1 = IFERROR(a296_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B296():
    # 'Coal_Foreign_Imports'!B296
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K296,"")'''
    @eval_fn
    def B296():
        k296_1 = Input_EIA_Imports_Coal_Foreign.K296()
        var_1 = IFERROR(k296_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C296():
    # 'Coal_Foreign_Imports'!C296
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L296,"")'''
    @eval_fn
    def C296():
        l296_1 = Input_EIA_Imports_Coal_Foreign.L296()
        var_1 = IFERROR(l296_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D296():
    # 'Coal_Foreign_Imports'!D296
    value = None
    formula = '''=IFERROR(C296/B296,"")'''
    @eval_fn
    def D296():
        c296_1 = Coal_Foreign_Imports.C296()
        b296_1 = Coal_Foreign_Imports.B296()
        var_1 = divide(c296_1, b296_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A297():
    # 'Coal_Foreign_Imports'!A297
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A297,"")'''
    @eval_fn
    def A297():
        a297_1 = Input_EIA_Imports_Coal_Foreign.A297()
        var_1 = IFERROR(a297_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B297():
    # 'Coal_Foreign_Imports'!B297
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K297,"")'''
    @eval_fn
    def B297():
        k297_1 = Input_EIA_Imports_Coal_Foreign.K297()
        var_1 = IFERROR(k297_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C297():
    # 'Coal_Foreign_Imports'!C297
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L297,"")'''
    @eval_fn
    def C297():
        l297_1 = Input_EIA_Imports_Coal_Foreign.L297()
        var_1 = IFERROR(l297_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D297():
    # 'Coal_Foreign_Imports'!D297
    value = None
    formula = '''=IFERROR(C297/B297,"")'''
    @eval_fn
    def D297():
        c297_1 = Coal_Foreign_Imports.C297()
        b297_1 = Coal_Foreign_Imports.B297()
        var_1 = divide(c297_1, b297_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A298():
    # 'Coal_Foreign_Imports'!A298
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A298,"")'''
    @eval_fn
    def A298():
        a298_1 = Input_EIA_Imports_Coal_Foreign.A298()
        var_1 = IFERROR(a298_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B298():
    # 'Coal_Foreign_Imports'!B298
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K298,"")'''
    @eval_fn
    def B298():
        k298_1 = Input_EIA_Imports_Coal_Foreign.K298()
        var_1 = IFERROR(k298_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C298():
    # 'Coal_Foreign_Imports'!C298
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L298,"")'''
    @eval_fn
    def C298():
        l298_1 = Input_EIA_Imports_Coal_Foreign.L298()
        var_1 = IFERROR(l298_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D298():
    # 'Coal_Foreign_Imports'!D298
    value = None
    formula = '''=IFERROR(C298/B298,"")'''
    @eval_fn
    def D298():
        c298_1 = Coal_Foreign_Imports.C298()
        b298_1 = Coal_Foreign_Imports.B298()
        var_1 = divide(c298_1, b298_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A299():
    # 'Coal_Foreign_Imports'!A299
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A299,"")'''
    @eval_fn
    def A299():
        a299_1 = Input_EIA_Imports_Coal_Foreign.A299()
        var_1 = IFERROR(a299_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B299():
    # 'Coal_Foreign_Imports'!B299
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K299,"")'''
    @eval_fn
    def B299():
        k299_1 = Input_EIA_Imports_Coal_Foreign.K299()
        var_1 = IFERROR(k299_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C299():
    # 'Coal_Foreign_Imports'!C299
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L299,"")'''
    @eval_fn
    def C299():
        l299_1 = Input_EIA_Imports_Coal_Foreign.L299()
        var_1 = IFERROR(l299_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D299():
    # 'Coal_Foreign_Imports'!D299
    value = None
    formula = '''=IFERROR(C299/B299,"")'''
    @eval_fn
    def D299():
        c299_1 = Coal_Foreign_Imports.C299()
        b299_1 = Coal_Foreign_Imports.B299()
        var_1 = divide(c299_1, b299_1)
        var_2 = IFERROR(var_1, "")
        return var_2

@register(Coal_Foreign_Imports)
class A300():
    # 'Coal_Foreign_Imports'!A300
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!A300,"")'''
    @eval_fn
    def A300():
        a300_1 = Input_EIA_Imports_Coal_Foreign.A300()
        var_1 = IFERROR(a300_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class B300():
    # 'Coal_Foreign_Imports'!B300
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!K300,"")'''
    @eval_fn
    def B300():
        k300_1 = Input_EIA_Imports_Coal_Foreign.K300()
        var_1 = IFERROR(k300_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class C300():
    # 'Coal_Foreign_Imports'!C300
    value = 0
    formula = '''=IFERROR('Input EIA Imports Coal Foreign'!L300,"")'''
    @eval_fn
    def C300():
        l300_1 = Input_EIA_Imports_Coal_Foreign.L300()
        var_1 = IFERROR(l300_1, "")
        return var_1

@register(Coal_Foreign_Imports)
class D300():
    # 'Coal_Foreign_Imports'!D300
    value = None
    formula = '''=IFERROR(C300/B300,"")'''
    @eval_fn
    def D300():
        c300_1 = Coal_Foreign_Imports.C300()
        b300_1 = Coal_Foreign_Imports.B300()
        var_1 = divide(c300_1, b300_1)
        var_2 = IFERROR(var_1, "")
        return var_2