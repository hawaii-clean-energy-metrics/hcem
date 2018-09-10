# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
OLD_Input_EIA_Imports_Coal_Fore = Worksheet('OLD_Input_EIA_Imports_Coal_Fore', 10, 10)



@register(OLD_Input_EIA_Imports_Coal_Fore)
class A1():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A1
    value = "http://www.eia.gov/coal/data.cfm#imports "

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A2():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A2
    value = "U.S. Coal Imports by Year and Quarter (2002-2011)"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A3
    value = "Year"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B3
    value = "Quarter"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C3
    value = "Port"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D3
    value = "Region"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E3
    value = "Country"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F3
    value = "Anthracite"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G3
    value = "Coking Coal"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H3
    value = "Sub Bituminous"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I3
    value = "Other Bituminous"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J3
    value = "Lignite"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K3
    value = "Total Coal Imports (tons)"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L3
    value = "Coke"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M3
    value = "Total Imports Price (dollars)"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N3():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N3
    value = "price per ton"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A4
    value = 2002

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B4
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C4
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D4
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E4
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F4
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G4
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H4
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I4
    value = 119940

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J4
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K4
    value = 119940

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L4
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M4
    value = 5833497

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N4():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N4
    value = 48.6367933967
    formula = "=M4/K4"
    @eval_fn
    def N4():
        m4_1 = OLD_Input_EIA_Imports_Coal_Fore.M4()
        k4_1 = OLD_Input_EIA_Imports_Coal_Fore.K4()
        var_1 = divide(m4_1, k4_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A5
    value = 2002

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B5
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C5
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D5
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E5
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F5
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G5
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H5
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I5
    value = 51305

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J5
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K5
    value = 51305

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L5
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M5
    value = 1603689

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N5():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N5
    value = 31.2579475685
    formula = "=M5/K5"
    @eval_fn
    def N5():
        m5_1 = OLD_Input_EIA_Imports_Coal_Fore.M5()
        k5_1 = OLD_Input_EIA_Imports_Coal_Fore.K5()
        var_1 = divide(m5_1, k5_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A6
    value = 2002

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B6
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C6
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D6
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E6
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F6
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G6
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H6
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I6
    value = 115358

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J6
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K6
    value = 115358

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L6
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M6
    value = 5631204

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N6():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N6
    value = 48.8150279998
    formula = "=M6/K6"
    @eval_fn
    def N6():
        m6_1 = OLD_Input_EIA_Imports_Coal_Fore.M6()
        k6_1 = OLD_Input_EIA_Imports_Coal_Fore.K6()
        var_1 = divide(m6_1, k6_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A7
    value = 2002

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B7
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C7
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D7
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E7
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F7
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G7
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H7
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I7
    value = 27822

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J7
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K7
    value = 27822

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L7
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M7
    value = 858487

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N7():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N7
    value = 30.8564085975
    formula = "=M7/K7"
    @eval_fn
    def N7():
        m7_1 = OLD_Input_EIA_Imports_Coal_Fore.M7()
        k7_1 = OLD_Input_EIA_Imports_Coal_Fore.K7()
        var_1 = divide(m7_1, k7_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A8
    value = 2002

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B8
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C8
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D8
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E8
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F8
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G8
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H8
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I8
    value = 180609

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J8
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K8
    value = 180609

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L8
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M8
    value = 9031872

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N8():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N8
    value = 50.0078733618
    formula = "=M8/K8"
    @eval_fn
    def N8():
        m8_1 = OLD_Input_EIA_Imports_Coal_Fore.M8()
        k8_1 = OLD_Input_EIA_Imports_Coal_Fore.K8()
        var_1 = divide(m8_1, k8_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A9
    value = 2002

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B9
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C9
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D9
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E9
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F9
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G9
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H9
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I9
    value = 32995

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J9
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K9
    value = 32995

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L9
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M9
    value = 1053396

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N9():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N9
    value = 31.9259281709
    formula = "=M9/K9"
    @eval_fn
    def N9():
        m9_1 = OLD_Input_EIA_Imports_Coal_Fore.M9()
        k9_1 = OLD_Input_EIA_Imports_Coal_Fore.K9()
        var_1 = divide(m9_1, k9_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A10
    value = 2002

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B10
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C10
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D10
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E10
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F10
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G10
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H10
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I10
    value = 58473

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J10
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K10
    value = 58473

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L10
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M10
    value = 2977213

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N10():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N10
    value = 50.9160296205
    formula = "=M10/K10"
    @eval_fn
    def N10():
        m10_1 = OLD_Input_EIA_Imports_Coal_Fore.M10()
        k10_1 = OLD_Input_EIA_Imports_Coal_Fore.K10()
        var_1 = divide(m10_1, k10_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A11
    value = 2003

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B11
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C11
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D11
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E11
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F11
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G11
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H11
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I11
    value = 39683

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J11
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K11
    value = 39683

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L11
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M11
    value = 1184335

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N11():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N11
    value = 29.8448957992
    formula = "=M11/K11"
    @eval_fn
    def N11():
        m11_1 = OLD_Input_EIA_Imports_Coal_Fore.M11()
        k11_1 = OLD_Input_EIA_Imports_Coal_Fore.K11()
        var_1 = divide(m11_1, k11_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A12
    value = 2003

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B12
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C12
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D12
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E12
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F12
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G12
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H12
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I12
    value = 178834

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J12
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K12
    value = 178834

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L12
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M12
    value = 8990546

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N12():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N12
    value = 50.2731359809
    formula = "=M12/K12"
    @eval_fn
    def N12():
        m12_1 = OLD_Input_EIA_Imports_Coal_Fore.M12()
        k12_1 = OLD_Input_EIA_Imports_Coal_Fore.K12()
        var_1 = divide(m12_1, k12_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A13
    value = 2003

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B13
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C13
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D13
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E13
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F13
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G13
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H13
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I13
    value = 20170

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J13
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K13
    value = 20170

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L13
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M13
    value = 606912

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N13():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N13
    value = 30.0898363907
    formula = "=M13/K13"
    @eval_fn
    def N13():
        m13_1 = OLD_Input_EIA_Imports_Coal_Fore.M13()
        k13_1 = OLD_Input_EIA_Imports_Coal_Fore.K13()
        var_1 = divide(m13_1, k13_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A14
    value = 2003

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B14
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C14
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D14
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E14
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F14
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G14
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H14
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I14
    value = 179549

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J14
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K14
    value = 179549

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L14
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M14
    value = 8951277

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N14():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N14
    value = 49.8542292076
    formula = "=M14/K14"
    @eval_fn
    def N14():
        m14_1 = OLD_Input_EIA_Imports_Coal_Fore.M14()
        k14_1 = OLD_Input_EIA_Imports_Coal_Fore.K14()
        var_1 = divide(m14_1, k14_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A15
    value = 2003

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B15
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C15
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D15
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E15
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F15
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G15
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H15
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I15
    value = 27448

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J15
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K15
    value = 27448

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L15
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M15
    value = 853764

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N15():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N15
    value = 31.1047799475
    formula = "=M15/K15"
    @eval_fn
    def N15():
        m15_1 = OLD_Input_EIA_Imports_Coal_Fore.M15()
        k15_1 = OLD_Input_EIA_Imports_Coal_Fore.K15()
        var_1 = divide(m15_1, k15_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A16
    value = 2003

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B16
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C16
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D16
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E16
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F16
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G16
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H16
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I16
    value = 177342

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J16
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K16
    value = 177342

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L16
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M16
    value = 7292900

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N16():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N16
    value = 41.1233661513
    formula = "=M16/K16"
    @eval_fn
    def N16():
        m16_1 = OLD_Input_EIA_Imports_Coal_Fore.M16()
        k16_1 = OLD_Input_EIA_Imports_Coal_Fore.K16()
        var_1 = divide(m16_1, k16_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A17
    value = 2003

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B17
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C17
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D17
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E17
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F17
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G17
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H17
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I17
    value = 23082

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J17
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K17
    value = 23082

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L17
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M17
    value = 701131

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N17():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N17
    value = 30.375660688
    formula = "=M17/K17"
    @eval_fn
    def N17():
        m17_1 = OLD_Input_EIA_Imports_Coal_Fore.M17()
        k17_1 = OLD_Input_EIA_Imports_Coal_Fore.K17()
        var_1 = divide(m17_1, k17_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A18
    value = 2003

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B18
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C18
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D18
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E18
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F18
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G18
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H18
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I18
    value = 179209

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J18
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K18
    value = 179209

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L18
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M18
    value = 3699339

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N18():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N18
    value = 20.642596075
    formula = "=M18/K18"
    @eval_fn
    def N18():
        m18_1 = OLD_Input_EIA_Imports_Coal_Fore.M18()
        k18_1 = OLD_Input_EIA_Imports_Coal_Fore.K18()
        var_1 = divide(m18_1, k18_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A19
    value = 2004

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B19
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C19
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D19
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E19
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F19
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G19
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H19
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I19
    value = 32990

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J19
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K19
    value = 32990

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L19
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M19
    value = 1029793

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N19():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N19
    value = 31.215307669
    formula = "=M19/K19"
    @eval_fn
    def N19():
        m19_1 = OLD_Input_EIA_Imports_Coal_Fore.M19()
        k19_1 = OLD_Input_EIA_Imports_Coal_Fore.K19()
        var_1 = divide(m19_1, k19_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A20
    value = 2004

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B20
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C20
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D20
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E20
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F20
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G20
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H20
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I20
    value = 176064

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J20
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K20
    value = 176064

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L20
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M20
    value = 3588792

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N20():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N20
    value = 20.3834514722
    formula = "=M20/K20"
    @eval_fn
    def N20():
        m20_1 = OLD_Input_EIA_Imports_Coal_Fore.M20()
        k20_1 = OLD_Input_EIA_Imports_Coal_Fore.K20()
        var_1 = divide(m20_1, k20_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A21
    value = 2004

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B21
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C21
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D21
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E21
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F21
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G21
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H21
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I21
    value = 33841

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J21
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K21
    value = 33841

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L21
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M21
    value = 1074295

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N21():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N21
    value = 31.7453680447
    formula = "=M21/K21"
    @eval_fn
    def N21():
        m21_1 = OLD_Input_EIA_Imports_Coal_Fore.M21()
        k21_1 = OLD_Input_EIA_Imports_Coal_Fore.K21()
        var_1 = divide(m21_1, k21_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A22
    value = 2004

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B22
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C22
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D22
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E22
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F22
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G22
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H22
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I22
    value = 122116

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J22
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K22
    value = 122116

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L22
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M22
    value = 2318274

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N22():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N22
    value = 18.9841953552
    formula = "=M22/K22"
    @eval_fn
    def N22():
        m22_1 = OLD_Input_EIA_Imports_Coal_Fore.M22()
        k22_1 = OLD_Input_EIA_Imports_Coal_Fore.K22()
        var_1 = divide(m22_1, k22_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A23
    value = 2004

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B23
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C23
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D23
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E23
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F23
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G23
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H23
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I23
    value = 27784

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J23
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K23
    value = 27784

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L23
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M23
    value = 864222

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N23():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N23
    value = 31.1050244745
    formula = "=M23/K23"
    @eval_fn
    def N23():
        m23_1 = OLD_Input_EIA_Imports_Coal_Fore.M23()
        k23_1 = OLD_Input_EIA_Imports_Coal_Fore.K23()
        var_1 = divide(m23_1, k23_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A24
    value = 2004

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B24
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C24
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D24
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E24
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F24
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G24
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H24
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I24
    value = 237538

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J24
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K24
    value = 237538

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L24
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M24
    value = 4575647

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N24():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N24
    value = 19.2628000573
    formula = "=M24/K24"
    @eval_fn
    def N24():
        m24_1 = OLD_Input_EIA_Imports_Coal_Fore.M24()
        k24_1 = OLD_Input_EIA_Imports_Coal_Fore.K24()
        var_1 = divide(m24_1, k24_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A25
    value = 2004

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B25
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C25
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D25
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E25
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F25
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G25
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H25
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I25
    value = 117349

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J25
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K25
    value = 117349

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L25
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M25
    value = 2186283

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N25():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N25
    value = 18.6306061407
    formula = "=M25/K25"
    @eval_fn
    def N25():
        m25_1 = OLD_Input_EIA_Imports_Coal_Fore.M25()
        k25_1 = OLD_Input_EIA_Imports_Coal_Fore.K25()
        var_1 = divide(m25_1, k25_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A26
    value = 2005

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B26
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C26
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D26
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E26
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F26
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G26
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H26
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I26
    value = 19846

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J26
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K26
    value = 19846

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L26
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M26
    value = 612354

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N26():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N26
    value = 30.8552856999
    formula = "=M26/K26"
    @eval_fn
    def N26():
        m26_1 = OLD_Input_EIA_Imports_Coal_Fore.M26()
        k26_1 = OLD_Input_EIA_Imports_Coal_Fore.K26()
        var_1 = divide(m26_1, k26_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A27
    value = 2005

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B27
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C27
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D27
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E27
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F27
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G27
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H27
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I27
    value = 176780

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J27
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K27
    value = 176780

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L27
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M27
    value = 3283050

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N27():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N27
    value = 18.5713881661
    formula = "=M27/K27"
    @eval_fn
    def N27():
        m27_1 = OLD_Input_EIA_Imports_Coal_Fore.M27()
        k27_1 = OLD_Input_EIA_Imports_Coal_Fore.K27()
        var_1 = divide(m27_1, k27_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A28
    value = 2005

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B28
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C28
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D28
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E28
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F28
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G28
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H28
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I28
    value = 28087

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J28
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K28
    value = 28087

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L28
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M28
    value = 911013

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N28():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N28
    value = 32.4353971588
    formula = "=M28/K28"
    @eval_fn
    def N28():
        m28_1 = OLD_Input_EIA_Imports_Coal_Fore.M28()
        k28_1 = OLD_Input_EIA_Imports_Coal_Fore.K28()
        var_1 = divide(m28_1, k28_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A29
    value = 2005

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B29
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C29
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D29
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E29
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F29
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G29
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H29
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I29
    value = 178000

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J29
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K29
    value = 178000

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L29
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M29
    value = 3388451

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N29():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N29
    value = 19.036241573
    formula = "=M29/K29"
    @eval_fn
    def N29():
        m29_1 = OLD_Input_EIA_Imports_Coal_Fore.M29()
        k29_1 = OLD_Input_EIA_Imports_Coal_Fore.K29()
        var_1 = divide(m29_1, k29_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A30
    value = 2005

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B30
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C30
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D30
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E30
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F30
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G30
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H30
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I30
    value = 179978

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J30
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K30
    value = 179978

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L30
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M30
    value = 3481699

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N30():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N30
    value = 19.3451366278
    formula = "=M30/K30"
    @eval_fn
    def N30():
        m30_1 = OLD_Input_EIA_Imports_Coal_Fore.M30()
        k30_1 = OLD_Input_EIA_Imports_Coal_Fore.K30()
        var_1 = divide(m30_1, k30_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A31
    value = 2005

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B31
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C31
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D31
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E31
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F31
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G31
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H31
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I31
    value = 24744

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J31
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K31
    value = 24744

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L31
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M31
    value = 790445

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N31():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N31
    value = 31.9449159392
    formula = "=M31/K31"
    @eval_fn
    def N31():
        m31_1 = OLD_Input_EIA_Imports_Coal_Fore.M31()
        k31_1 = OLD_Input_EIA_Imports_Coal_Fore.K31()
        var_1 = divide(m31_1, k31_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A32
    value = 2005

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B32
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C32
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D32
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E32
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F32
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G32
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H32
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I32
    value = 241479

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J32
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K32
    value = 241479

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L32
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M32
    value = 4670947

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N32():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N32
    value = 19.3430774519
    formula = "=M32/K32"
    @eval_fn
    def N32():
        m32_1 = OLD_Input_EIA_Imports_Coal_Fore.M32()
        k32_1 = OLD_Input_EIA_Imports_Coal_Fore.K32()
        var_1 = divide(m32_1, k32_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A33
    value = 2006

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B33
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C33
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D33
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E33
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F33
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G33
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H33
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I33
    value = 19127

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J33
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K33
    value = 19127

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L33
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M33
    value = 583186

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N33():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N33
    value = 30.4901971036
    formula = "=M33/K33"
    @eval_fn
    def N33():
        m33_1 = OLD_Input_EIA_Imports_Coal_Fore.M33()
        k33_1 = OLD_Input_EIA_Imports_Coal_Fore.K33()
        var_1 = divide(m33_1, k33_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A34
    value = 2006

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B34
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C34
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D34
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E34
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F34
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G34
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H34
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I34
    value = 179045

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J34
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K34
    value = 179045

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L34
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M34
    value = 3505051

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N34():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N34
    value = 19.5763690692
    formula = "=M34/K34"
    @eval_fn
    def N34():
        m34_1 = OLD_Input_EIA_Imports_Coal_Fore.M34()
        k34_1 = OLD_Input_EIA_Imports_Coal_Fore.K34()
        var_1 = divide(m34_1, k34_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A35
    value = 2006

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B35
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C35
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D35
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E35
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F35
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G35
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H35
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I35
    value = 120696

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J35
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K35
    value = 120696

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L35
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M35
    value = 2377551

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N35():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N35
    value = 19.6986726983
    formula = "=M35/K35"
    @eval_fn
    def N35():
        m35_1 = OLD_Input_EIA_Imports_Coal_Fore.M35()
        k35_1 = OLD_Input_EIA_Imports_Coal_Fore.K35()
        var_1 = divide(m35_1, k35_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A36
    value = 2006

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B36
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C36
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D36
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E36
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F36
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G36
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H36
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I36
    value = 26375

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J36
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K36
    value = 26375

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L36
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M36
    value = 803902

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N36():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N36
    value = 30.4796966825
    formula = "=M36/K36"
    @eval_fn
    def N36():
        m36_1 = OLD_Input_EIA_Imports_Coal_Fore.M36()
        k36_1 = OLD_Input_EIA_Imports_Coal_Fore.K36()
        var_1 = divide(m36_1, k36_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A37
    value = 2006

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B37
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C37
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D37
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E37
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F37
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G37
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H37
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I37
    value = 242203

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J37
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K37
    value = 242203

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L37
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M37
    value = 4623461

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N37():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N37
    value = 19.0891979042
    formula = "=M37/K37"
    @eval_fn
    def N37():
        m37_1 = OLD_Input_EIA_Imports_Coal_Fore.M37()
        k37_1 = OLD_Input_EIA_Imports_Coal_Fore.K37()
        var_1 = divide(m37_1, k37_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A38
    value = 2006

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B38
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C38
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D38
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E38
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F38
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G38
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H38
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I38
    value = 118549

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J38
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K38
    value = 118549

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L38
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M38
    value = 2252284

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N38():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N38
    value = 18.9987600064
    formula = "=M38/K38"
    @eval_fn
    def N38():
        m38_1 = OLD_Input_EIA_Imports_Coal_Fore.M38()
        k38_1 = OLD_Input_EIA_Imports_Coal_Fore.K38()
        var_1 = divide(m38_1, k38_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A39
    value = 2007

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B39
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C39
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D39
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E39
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F39
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G39
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H39
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I39
    value = 27580

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J39
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K39
    value = 27580

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L39
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M39
    value = 864895

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N39():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N39
    value = 31.3594996374
    formula = "=M39/K39"
    @eval_fn
    def N39():
        m39_1 = OLD_Input_EIA_Imports_Coal_Fore.M39()
        k39_1 = OLD_Input_EIA_Imports_Coal_Fore.K39()
        var_1 = divide(m39_1, k39_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A40
    value = 2007

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B40
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C40
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D40
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E40
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F40
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G40
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H40
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I40
    value = 176243

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J40
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K40
    value = 176243

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L40
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M40
    value = 3435907

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N40():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N40
    value = 19.4952820821
    formula = "=M40/K40"
    @eval_fn
    def N40():
        m40_1 = OLD_Input_EIA_Imports_Coal_Fore.M40()
        k40_1 = OLD_Input_EIA_Imports_Coal_Fore.K40()
        var_1 = divide(m40_1, k40_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A41
    value = 2007

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B41
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C41
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D41
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E41
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F41
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G41
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H41
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I41
    value = 19748

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J41
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K41
    value = 19748

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L41
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M41
    value = 621263

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N41():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N41
    value = 31.4595402066
    formula = "=M41/K41"
    @eval_fn
    def N41():
        m41_1 = OLD_Input_EIA_Imports_Coal_Fore.M41()
        k41_1 = OLD_Input_EIA_Imports_Coal_Fore.K41()
        var_1 = divide(m41_1, k41_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A42
    value = 2007

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B42
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C42
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D42
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E42
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F42
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G42
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H42
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I42
    value = 178075

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J42
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K42
    value = 178075

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L42
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M42
    value = 3482341

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N42():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N42
    value = 19.5554738172
    formula = "=M42/K42"
    @eval_fn
    def N42():
        m42_1 = OLD_Input_EIA_Imports_Coal_Fore.M42()
        k42_1 = OLD_Input_EIA_Imports_Coal_Fore.K42()
        var_1 = divide(m42_1, k42_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A43
    value = 2007

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B43
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C43
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D43
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E43
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F43
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G43
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H43
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I43
    value = 168080

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J43
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K43
    value = 168080

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L43
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M43
    value = 3311551

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N43():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N43
    value = 19.7022310804
    formula = "=M43/K43"
    @eval_fn
    def N43():
        m43_1 = OLD_Input_EIA_Imports_Coal_Fore.M43()
        k43_1 = OLD_Input_EIA_Imports_Coal_Fore.K43()
        var_1 = divide(m43_1, k43_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A44
    value = 2007

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B44
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C44
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D44
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E44
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F44
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G44
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H44
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I44
    value = 18310

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J44
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K44
    value = 18310

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L44
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M44
    value = 593986

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N44():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N44
    value = 32.4405243037
    formula = "=M44/K44"
    @eval_fn
    def N44():
        m44_1 = OLD_Input_EIA_Imports_Coal_Fore.M44()
        k44_1 = OLD_Input_EIA_Imports_Coal_Fore.K44()
        var_1 = divide(m44_1, k44_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A45
    value = 2007

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B45
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C45
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D45
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E45
    value = "Canada"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F45
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G45
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H45
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I45
    value = 60572

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J45
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K45
    value = 60572

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L45
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M45
    value = 3468444

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N45():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N45
    value = 57.2615069669
    formula = "=M45/K45"
    @eval_fn
    def N45():
        m45_1 = OLD_Input_EIA_Imports_Coal_Fore.M45()
        k45_1 = OLD_Input_EIA_Imports_Coal_Fore.K45()
        var_1 = divide(m45_1, k45_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A46
    value = 2007

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B46
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C46
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D46
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E46
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F46
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G46
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H46
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I46
    value = 120241

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J46
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K46
    value = 120241

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L46
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M46
    value = 4849555

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N46():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N46
    value = 40.331958317
    formula = "=M46/K46"
    @eval_fn
    def N46():
        m46_1 = OLD_Input_EIA_Imports_Coal_Fore.M46()
        k46_1 = OLD_Input_EIA_Imports_Coal_Fore.K46()
        var_1 = divide(m46_1, k46_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A47
    value = 2008

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B47
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C47
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D47
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E47
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F47
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G47
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H47
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I47
    value = 39004

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J47
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K47
    value = 39004

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L47
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M47
    value = 2208384

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N47():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N47
    value = 56.6194236489
    formula = "=M47/K47"
    @eval_fn
    def N47():
        m47_1 = OLD_Input_EIA_Imports_Coal_Fore.M47()
        k47_1 = OLD_Input_EIA_Imports_Coal_Fore.K47()
        var_1 = divide(m47_1, k47_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A48
    value = 2008

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B48
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C48
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D48
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E48
    value = "Canada"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F48
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G48
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H48
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I48
    value = 59172

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J48
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K48
    value = 59172

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L48
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M48
    value = 2305556

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N48():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N48
    value = 38.9636314473
    formula = "=M48/K48"
    @eval_fn
    def N48():
        m48_1 = OLD_Input_EIA_Imports_Coal_Fore.M48()
        k48_1 = OLD_Input_EIA_Imports_Coal_Fore.K48()
        var_1 = divide(m48_1, k48_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A49
    value = 2008

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B49
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C49
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D49
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E49
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F49
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G49
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H49
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I49
    value = 117887

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J49
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K49
    value = 117887

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L49
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M49
    value = 4755424

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N49():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N49
    value = 40.3388329502
    formula = "=M49/K49"
    @eval_fn
    def N49():
        m49_1 = OLD_Input_EIA_Imports_Coal_Fore.M49()
        k49_1 = OLD_Input_EIA_Imports_Coal_Fore.K49()
        var_1 = divide(m49_1, k49_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A50
    value = 2008

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B50
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C50
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D50
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E50
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F50
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G50
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H50
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I50
    value = 17234

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J50
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K50
    value = 17234

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L50
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M50
    value = 963367

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N50():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N50
    value = 55.8992108622
    formula = "=M50/K50"
    @eval_fn
    def N50():
        m50_1 = OLD_Input_EIA_Imports_Coal_Fore.M50()
        k50_1 = OLD_Input_EIA_Imports_Coal_Fore.K50()
        var_1 = divide(m50_1, k50_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A51
    value = 2008

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B51
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C51
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D51
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E51
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F51
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G51
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H51
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I51
    value = 176159

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J51
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K51
    value = 176159

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L51
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M51
    value = 16145260

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N51():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N51
    value = 91.6516328998
    formula = "=M51/K51"
    @eval_fn
    def N51():
        m51_1 = OLD_Input_EIA_Imports_Coal_Fore.M51()
        k51_1 = OLD_Input_EIA_Imports_Coal_Fore.K51()
        var_1 = divide(m51_1, k51_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A52
    value = 2008

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B52
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C52
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D52
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E52
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F52
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G52
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H52
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I52
    value = 24692

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J52
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K52
    value = 24692

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L52
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M52
    value = 1406720

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N52():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N52
    value = 56.9706787624
    formula = "=M52/K52"
    @eval_fn
    def N52():
        m52_1 = OLD_Input_EIA_Imports_Coal_Fore.M52()
        k52_1 = OLD_Input_EIA_Imports_Coal_Fore.K52()
        var_1 = divide(m52_1, k52_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A53
    value = 2008

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B53
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C53
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D53
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E53
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F53
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G53
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H53
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I53
    value = 184843

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J53
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K53
    value = 184843

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L53
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M53
    value = 8706644

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N53():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N53
    value = 47.1029143652
    formula = "=M53/K53"
    @eval_fn
    def N53():
        m53_1 = OLD_Input_EIA_Imports_Coal_Fore.M53()
        k53_1 = OLD_Input_EIA_Imports_Coal_Fore.K53()
        var_1 = divide(m53_1, k53_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A54
    value = 2008

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B54
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C54
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D54
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E54
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F54
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G54
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H54
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I54
    value = 68414

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J54
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K54
    value = 68414

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L54
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M54
    value = 3364517

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N54():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N54
    value = 49.1787791972
    formula = "=M54/K54"
    @eval_fn
    def N54():
        m54_1 = OLD_Input_EIA_Imports_Coal_Fore.M54()
        k54_1 = OLD_Input_EIA_Imports_Coal_Fore.K54()
        var_1 = divide(m54_1, k54_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A55
    value = 2008

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B55
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C55
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D55
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E55
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F55
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G55
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H55
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I55
    value = 59293

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J55
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K55
    value = 59293

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L55
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M55
    value = 2409254

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N55():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N55
    value = 40.6330258209
    formula = "=M55/K55"
    @eval_fn
    def N55():
        m55_1 = OLD_Input_EIA_Imports_Coal_Fore.M55()
        k55_1 = OLD_Input_EIA_Imports_Coal_Fore.K55()
        var_1 = divide(m55_1, k55_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A56
    value = 2009

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B56
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C56
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D56
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E56
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F56
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G56
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H56
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I56
    value = 59563

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J56
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K56
    value = 59563

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L56
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M56
    value = 3461216

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N56():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N56
    value = 58.1101690647
    formula = "=M56/K56"
    @eval_fn
    def N56():
        m56_1 = OLD_Input_EIA_Imports_Coal_Fore.M56()
        k56_1 = OLD_Input_EIA_Imports_Coal_Fore.K56()
        var_1 = divide(m56_1, k56_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A57
    value = 2009

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B57
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C57
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D57
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E57
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F57
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G57
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H57
    value = 172130

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I57
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J57
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K57
    value = 172130

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L57
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M57
    value = 7123314

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N57():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N57
    value = 41.3833381746
    formula = "=M57/K57"
    @eval_fn
    def N57():
        m57_1 = OLD_Input_EIA_Imports_Coal_Fore.M57()
        k57_1 = OLD_Input_EIA_Imports_Coal_Fore.K57()
        var_1 = divide(m57_1, k57_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A58
    value = 2009

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B58
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C58
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D58
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E58
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F58
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G58
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H58
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I58
    value = 170607

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J58
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K58
    value = 170607

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L58
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M58
    value = 10616975

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N58():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N58
    value = 62.2305942898
    formula = "=M58/K58"
    @eval_fn
    def N58():
        m58_1 = OLD_Input_EIA_Imports_Coal_Fore.M58()
        k58_1 = OLD_Input_EIA_Imports_Coal_Fore.K58()
        var_1 = divide(m58_1, k58_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A59
    value = 2009

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B59
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C59
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D59
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E59
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F59
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G59
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H59
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I59
    value = 33951

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J59
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K59
    value = 33951

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L59
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M59
    value = 2007939

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N59():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N59
    value = 59.1422638508
    formula = "=M59/K59"
    @eval_fn
    def N59():
        m59_1 = OLD_Input_EIA_Imports_Coal_Fore.M59()
        k59_1 = OLD_Input_EIA_Imports_Coal_Fore.K59()
        var_1 = divide(m59_1, k59_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A60
    value = 2009

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B60
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C60
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D60
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E60
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F60
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G60
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H60
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I60
    value = 177870

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J60
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K60
    value = 177870

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L60
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M60
    value = 10229824

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N60():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N60
    value = 57.5129251701
    formula = "=M60/K60"
    @eval_fn
    def N60():
        m60_1 = OLD_Input_EIA_Imports_Coal_Fore.M60()
        k60_1 = OLD_Input_EIA_Imports_Coal_Fore.K60()
        var_1 = divide(m60_1, k60_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A61
    value = 2009

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B61
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C61
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D61
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E61
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F61
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G61
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H61
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I61
    value = 58224

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J61
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K61
    value = 58224

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L61
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M61
    value = 3261836

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N61():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N61
    value = 56.0221901621
    formula = "=M61/K61"
    @eval_fn
    def N61():
        m61_1 = OLD_Input_EIA_Imports_Coal_Fore.M61()
        k61_1 = OLD_Input_EIA_Imports_Coal_Fore.K61()
        var_1 = divide(m61_1, k61_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A62
    value = 2009

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B62
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C62
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D62
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E62
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F62
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G62
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H62
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I62
    value = 121200

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J62
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K62
    value = 121200

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L62
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M62
    value = 6494746

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N62():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N62
    value = 53.5870132013
    formula = "=M62/K62"
    @eval_fn
    def N62():
        m62_1 = OLD_Input_EIA_Imports_Coal_Fore.M62()
        k62_1 = OLD_Input_EIA_Imports_Coal_Fore.K62()
        var_1 = divide(m62_1, k62_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A63
    value = 2010

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B63
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C63
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D63
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E63
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F63
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G63
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H63
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I63
    value = 91604

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J63
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K63
    value = 91604

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L63
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M63
    value = 4977310

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N63():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N63
    value = 54.3350727042
    formula = "=M63/K63"
    @eval_fn
    def N63():
        m63_1 = OLD_Input_EIA_Imports_Coal_Fore.M63()
        k63_1 = OLD_Input_EIA_Imports_Coal_Fore.K63()
        var_1 = divide(m63_1, k63_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A64
    value = 2010

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B64
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C64
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D64
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E64
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F64
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G64
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H64
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I64
    value = 110523

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J64
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K64
    value = 110523

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L64
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M64
    value = 5922653

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N64():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N64
    value = 53.5875157207
    formula = "=M64/K64"
    @eval_fn
    def N64():
        m64_1 = OLD_Input_EIA_Imports_Coal_Fore.M64()
        k64_1 = OLD_Input_EIA_Imports_Coal_Fore.K64()
        var_1 = divide(m64_1, k64_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A65
    value = 2010

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B65
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C65
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D65
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E65
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F65
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G65
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H65
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I65
    value = 169012

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J65
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K65
    value = 169012

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L65
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M65
    value = 11161217

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N65():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N65
    value = 66.0380150522
    formula = "=M65/K65"
    @eval_fn
    def N65():
        m65_1 = OLD_Input_EIA_Imports_Coal_Fore.M65()
        k65_1 = OLD_Input_EIA_Imports_Coal_Fore.K65()
        var_1 = divide(m65_1, k65_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A66
    value = 2010

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B66
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C66
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D66
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E66
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F66
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G66
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H66
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I66
    value = 81103

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J66
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K66
    value = 81103

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L66
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M66
    value = 4258140

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N66():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N66
    value = 52.502866725
    formula = "=M66/K66"
    @eval_fn
    def N66():
        m66_1 = OLD_Input_EIA_Imports_Coal_Fore.M66()
        k66_1 = OLD_Input_EIA_Imports_Coal_Fore.K66()
        var_1 = divide(m66_1, k66_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A67
    value = 2010

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B67
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C67
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D67
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E67
    value = "Colombia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F67
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G67
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H67
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I67
    value = 58492

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J67
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K67
    value = 58492

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L67
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M67
    value = 3555208

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N67():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N67
    value = 60.7810982698
    formula = "=M67/K67"
    @eval_fn
    def N67():
        m67_1 = OLD_Input_EIA_Imports_Coal_Fore.M67()
        k67_1 = OLD_Input_EIA_Imports_Coal_Fore.K67()
        var_1 = divide(m67_1, k67_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A68
    value = 2010

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B68
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C68
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D68
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E68
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F68
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G68
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H68
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I68
    value = 116748

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J68
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K68
    value = 116748

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L68
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M68
    value = 6256221

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N68():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N68
    value = 53.5873933601
    formula = "=M68/K68"
    @eval_fn
    def N68():
        m68_1 = OLD_Input_EIA_Imports_Coal_Fore.M68()
        k68_1 = OLD_Input_EIA_Imports_Coal_Fore.K68()
        var_1 = divide(m68_1, k68_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A69
    value = 2010

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B69
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C69
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D69
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E69
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F69
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G69
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H69
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I69
    value = 207697

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J69
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K69
    value = 207697

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L69
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M69
    value = 12350831

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N69():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N69
    value = 59.4656205915
    formula = "=M69/K69"
    @eval_fn
    def N69():
        m69_1 = OLD_Input_EIA_Imports_Coal_Fore.M69()
        k69_1 = OLD_Input_EIA_Imports_Coal_Fore.K69()
        var_1 = divide(m69_1, k69_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A70
    value = 2011

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B70
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C70
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D70
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E70
    value = "Australia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F70
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G70
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H70
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I70
    value = 61745

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J70
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K70
    value = 61745

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L70
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M70
    value = 3254974

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N70():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N70
    value = 52.7163980889
    formula = "=M70/K70"
    @eval_fn
    def N70():
        m70_1 = OLD_Input_EIA_Imports_Coal_Fore.M70()
        k70_1 = OLD_Input_EIA_Imports_Coal_Fore.K70()
        var_1 = divide(m70_1, k70_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A71
    value = 2011

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B71
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C71
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D71
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E71
    value = "Colombia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F71
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G71
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H71
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I71
    value = 56942

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J71
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K71
    value = 56942

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L71
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M71
    value = 2686164

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N71():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N71
    value = 47.1736855045
    formula = "=M71/K71"
    @eval_fn
    def N71():
        m71_1 = OLD_Input_EIA_Imports_Coal_Fore.M71()
        k71_1 = OLD_Input_EIA_Imports_Coal_Fore.K71()
        var_1 = divide(m71_1, k71_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A72
    value = 2011

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B72
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C72
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D72
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E72
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F72
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G72
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H72
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I72
    value = 60189

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J72
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K72
    value = 60189

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L72
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M72
    value = 3112371

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N72():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N72
    value = 51.7099636146
    formula = "=M72/K72"
    @eval_fn
    def N72():
        m72_1 = OLD_Input_EIA_Imports_Coal_Fore.M72()
        k72_1 = OLD_Input_EIA_Imports_Coal_Fore.K72()
        var_1 = divide(m72_1, k72_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A73
    value = 2011

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B73
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C73
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D73
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E73
    value = "Colombia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F73
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G73
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H73
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I73
    value = 63202

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J73
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K73
    value = 63202

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L73
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M73
    value = 2981457

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N73():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N73
    value = 47.1734597006
    formula = "=M73/K73"
    @eval_fn
    def N73():
        m73_1 = OLD_Input_EIA_Imports_Coal_Fore.M73()
        k73_1 = OLD_Input_EIA_Imports_Coal_Fore.K73()
        var_1 = divide(m73_1, k73_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A74
    value = 2011

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B74
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C74
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D74
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E74
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F74
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G74
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H74
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I74
    value = 237787

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J74
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K74
    value = 237787

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L74
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M74
    value = 12560141

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N74():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N74
    value = 52.8209742332
    formula = "=M74/K74"
    @eval_fn
    def N74():
        m74_1 = OLD_Input_EIA_Imports_Coal_Fore.M74()
        k74_1 = OLD_Input_EIA_Imports_Coal_Fore.K74()
        var_1 = divide(m74_1, k74_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A75
    value = 2011

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B75
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C75
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D75
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E75
    value = "Colombia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F75
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G75
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H75
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I75
    value = 121866

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J75
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K75
    value = 121866

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L75
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M75
    value = 5634013

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N75
    value = 46.2312129716
    formula = "=M75/K75"
    @eval_fn
    def N75():
        m75_1 = OLD_Input_EIA_Imports_Coal_Fore.M75()
        k75_1 = OLD_Input_EIA_Imports_Coal_Fore.K75()
        var_1 = divide(m75_1, k75_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class Z75():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!Z75
    value = "a"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A76
    value = 2011

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B76
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C76
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D76
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E76
    value = "Colombia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F76
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G76
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H76
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I76
    value = 120995

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J76
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K76
    value = 120995

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L76
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M76
    value = 5382691

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N76():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N76
    value = 44.4868878879
    formula = "=M76/K76"
    @eval_fn
    def N76():
        m76_1 = OLD_Input_EIA_Imports_Coal_Fore.M76()
        k76_1 = OLD_Input_EIA_Imports_Coal_Fore.K76()
        var_1 = divide(m76_1, k76_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A77
    value = 2011

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B77
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C77
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D77
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E77
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class F77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!F77
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class G77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!G77
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class H77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!H77
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I77
    value = 122613

@register(OLD_Input_EIA_Imports_Coal_Fore)
class J77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!J77
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K77
    value = 122613

@register(OLD_Input_EIA_Imports_Coal_Fore)
class L77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!L77
    value = 0

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M77
    value = 5894780

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N77():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N77
    value = 48.0763051226
    formula = "=M77/K77"
    @eval_fn
    def N77():
        m77_1 = OLD_Input_EIA_Imports_Coal_Fore.M77()
        k77_1 = OLD_Input_EIA_Imports_Coal_Fore.K77()
        var_1 = divide(m77_1, k77_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A78():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A78
    value = 2012

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B78():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B78
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C78():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C78
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D78():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D78
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E78():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E78
    value = "Colombia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I78():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I78
    value = 118081

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K78():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K78
    value = 118081

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M78():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M78
    value = 6158969

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N78():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N78
    value = 52.158848587
    formula = "=M78/K78"
    @eval_fn
    def N78():
        m78_1 = OLD_Input_EIA_Imports_Coal_Fore.M78()
        k78_1 = OLD_Input_EIA_Imports_Coal_Fore.K78()
        var_1 = divide(m78_1, k78_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A79():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A79
    value = 2012

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B79():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B79
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C79():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C79
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D79():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D79
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E79():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E79
    value = "Colombia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I79():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I79
    value = 181879

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K79():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K79
    value = 181879

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M79():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M79
    value = 9031732

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N79():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N79
    value = 49.6579154273
    formula = "=M79/K79"
    @eval_fn
    def N79():
        m79_1 = OLD_Input_EIA_Imports_Coal_Fore.M79()
        k79_1 = OLD_Input_EIA_Imports_Coal_Fore.K79()
        var_1 = divide(m79_1, k79_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A80():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A80
    value = 2012

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B80():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B80
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C80():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C80
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D80():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D80
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E80():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E80
    value = "Colombia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I80():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I80
    value = 120912

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K80():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K80
    value = 120912

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M80():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M80
    value = 6066056

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N80():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N80
    value = 50.1691808919
    formula = "=M80/K80"
    @eval_fn
    def N80():
        m80_1 = OLD_Input_EIA_Imports_Coal_Fore.M80()
        k80_1 = OLD_Input_EIA_Imports_Coal_Fore.K80()
        var_1 = divide(m80_1, k80_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A81():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A81
    value = 2012

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B81():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B81
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C81():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C81
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D81():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D81
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E81():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E81
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I81():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I81
    value = 117500

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K81():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K81
    value = 117500

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M81():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M81
    value = 6624014

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N81():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N81
    value = 56.374587234
    formula = "=M81/K81"
    @eval_fn
    def N81():
        m81_1 = OLD_Input_EIA_Imports_Coal_Fore.M81()
        k81_1 = OLD_Input_EIA_Imports_Coal_Fore.K81()
        var_1 = divide(m81_1, k81_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A82():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A82
    value = 2012

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B82():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B82
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C82():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C82
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D82():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D82
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E82():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E82
    value = "Colombia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I82():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I82
    value = 59280

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K82():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K82
    value = 59280

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M82():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M82
    value = 2821733

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N82():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N82
    value = 47.6000843455
    formula = "=M82/K82"
    @eval_fn
    def N82():
        m82_1 = OLD_Input_EIA_Imports_Coal_Fore.M82()
        k82_1 = OLD_Input_EIA_Imports_Coal_Fore.K82()
        var_1 = divide(m82_1, k82_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A83():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A83
    value = 2012

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B83():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B83
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C83():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C83
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class D83():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!D83
    value = "Western"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E83():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E83
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I83():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I83
    value = 120129

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K83():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K83
    value = 120129

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M83():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M83
    value = 6911620

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N83():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N83
    value = 57.5349832264
    formula = "=M83/K83"
    @eval_fn
    def N83():
        m83_1 = OLD_Input_EIA_Imports_Coal_Fore.M83()
        k83_1 = OLD_Input_EIA_Imports_Coal_Fore.K83()
        var_1 = divide(m83_1, k83_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A84():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A84
    value = 2013

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B84():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B84
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C84():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C84
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E84():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E84
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I84():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I84
    value = 117481

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K84():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K84
    value = 117481

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M84():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M84
    value = 7107782

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N84():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N84
    value = 60.5015449307
    formula = "=M84/K84"
    @eval_fn
    def N84():
        m84_1 = OLD_Input_EIA_Imports_Coal_Fore.M84()
        k84_1 = OLD_Input_EIA_Imports_Coal_Fore.K84()
        var_1 = divide(m84_1, k84_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A85():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A85
    value = 2013

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B85():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B85
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C85():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C85
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E85():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E85
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I85():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I85
    value = 180355

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K85():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K85
    value = 180355

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M85():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M85
    value = 11208629

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N85():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N85
    value = 62.1475922486
    formula = "=M85/K85"
    @eval_fn
    def N85():
        m85_1 = OLD_Input_EIA_Imports_Coal_Fore.M85()
        k85_1 = OLD_Input_EIA_Imports_Coal_Fore.K85()
        var_1 = divide(m85_1, k85_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A86():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A86
    value = 2013

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B86():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B86
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C86():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C86
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E86():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E86
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I86():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I86
    value = 187311

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K86():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K86
    value = 187311

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M86():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M86
    value = 11958306

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N86():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N86
    value = 63.8419847206
    formula = "=M86/K86"
    @eval_fn
    def N86():
        m86_1 = OLD_Input_EIA_Imports_Coal_Fore.M86()
        k86_1 = OLD_Input_EIA_Imports_Coal_Fore.K86()
        var_1 = divide(m86_1, k86_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A87():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A87
    value = 2013

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B87():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B87
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C87():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C87
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E87():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E87
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I87():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I87
    value = 181496

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K87():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K87
    value = 181496

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M87():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M87
    value = 10426789

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N87():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N87
    value = 57.449139375
    formula = "=M87/K87"
    @eval_fn
    def N87():
        m87_1 = OLD_Input_EIA_Imports_Coal_Fore.M87()
        k87_1 = OLD_Input_EIA_Imports_Coal_Fore.K87()
        var_1 = divide(m87_1, k87_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A88():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A88
    value = 2014

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B88():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B88
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C88():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C88
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E88():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E88
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I88():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I88
    value = 183238

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K88():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K88
    value = 183238

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M88():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M88
    value = 11722287

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N88():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N88
    value = 63.9730132396
    formula = "=M88/K88"
    @eval_fn
    def N88():
        m88_1 = OLD_Input_EIA_Imports_Coal_Fore.M88()
        k88_1 = OLD_Input_EIA_Imports_Coal_Fore.K88()
        var_1 = divide(m88_1, k88_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A89():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A89
    value = 2014

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B89():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B89
    value = 2

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C89():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C89
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E89():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E89
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I89():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I89
    value = 178525

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K89():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K89
    value = 178525

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M89():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M89
    value = 11482729

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N89():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N89
    value = 64.3200056015
    formula = "=M89/K89"
    @eval_fn
    def N89():
        m89_1 = OLD_Input_EIA_Imports_Coal_Fore.M89()
        k89_1 = OLD_Input_EIA_Imports_Coal_Fore.K89()
        var_1 = divide(m89_1, k89_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A90():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A90
    value = 2014

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B90():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B90
    value = 3

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C90():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C90
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E90():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E90
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I90():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I90
    value = 184083

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K90():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K90
    value = 184083

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M90():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M90
    value = 11673484

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N90():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N90
    value = 63.4142424884
    formula = "=M90/K90"
    @eval_fn
    def N90():
        m90_1 = OLD_Input_EIA_Imports_Coal_Fore.M90()
        k90_1 = OLD_Input_EIA_Imports_Coal_Fore.K90()
        var_1 = divide(m90_1, k90_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A91():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A91
    value = 2014

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B91():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B91
    value = 4

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C91():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C91
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E91():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E91
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I91():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I91
    value = 179281

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K91():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K91
    value = 179281

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M91():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M91
    value = 11465355

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N91():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N91
    value = 63.9518688539
    formula = "=M91/K91"
    @eval_fn
    def N91():
        m91_1 = OLD_Input_EIA_Imports_Coal_Fore.M91()
        k91_1 = OLD_Input_EIA_Imports_Coal_Fore.K91()
        var_1 = divide(m91_1, k91_1)
        return var_1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class A92():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!A92
    value = 2015

@register(OLD_Input_EIA_Imports_Coal_Fore)
class B92():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!B92
    value = 1

@register(OLD_Input_EIA_Imports_Coal_Fore)
class C92():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!C92
    value = "Honolulu, HI"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class E92():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!E92
    value = "Indonesia"

@register(OLD_Input_EIA_Imports_Coal_Fore)
class I92():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!I92
    value = 238083

@register(OLD_Input_EIA_Imports_Coal_Fore)
class K92():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!K92
    value = 238083

@register(OLD_Input_EIA_Imports_Coal_Fore)
class M92():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!M92
    value = 14722877

@register(OLD_Input_EIA_Imports_Coal_Fore)
class N92():
    # 'OLD_Input_EIA_Imports_Coal_Fore'!N92
    value = 61.8392619381
    formula = "=M92/K92"
    @eval_fn
    def N92():
        m92_1 = OLD_Input_EIA_Imports_Coal_Fore.M92()
        k92_1 = OLD_Input_EIA_Imports_Coal_Fore.K92()
        var_1 = divide(m92_1, k92_1)
        return var_1