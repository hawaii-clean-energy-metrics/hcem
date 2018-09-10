# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
OLD_Input_Population = Worksheet('OLD_Input_Population', 10, 10)



@register(OLD_Input_Population)
class A1():
    # 'OLD_Input_Population'!A1
    value = "Population of Hawaii"

@register(OLD_Input_Population)
class A2():
    # 'OLD_Input_Population'!A2
    value = "http://dbedt.hawaii.gov/economic/databook/2014-individual/_01/"

@register(OLD_Input_Population)
class A3():
    # 'OLD_Input_Population'!A3
    value = "Year"

@register(OLD_Input_Population)
class B3():
    # 'OLD_Input_Population'!B3
    value = "Date"

@register(OLD_Input_Population)
class C3():
    # 'OLD_Input_Population'!C3
    value = "Resident Population (Thousands)"

@register(OLD_Input_Population)
class D3():
    # 'OLD_Input_Population'!D3
    value = "Resident Population (%Change)"

@register(OLD_Input_Population)
class E3():
    # 'OLD_Input_Population'!E3
    value = '''De Facto Population
(Thousands)'''

@register(OLD_Input_Population)
class F3():
    # 'OLD_Input_Population'!F3
    value = "De Facto Population (% Change)"

@register(OLD_Input_Population)
class G3():
    # 'OLD_Input_Population'!G3
    value = "DBEDT Resident Population"

@register(OLD_Input_Population)
class H3():
    # 'OLD_Input_Population'!H3
    value = "DBEDT De Facto Population"

@register(OLD_Input_Population)
class A4():
    # 'OLD_Input_Population'!A4
    value = 1965
    formula = "=YEAR(B4)"
    @eval_fn
    def A4():
        b4_1 = OLD_Input_Population.B4()
        var_1 = YEAR(b4_1)
        return var_1

@register(OLD_Input_Population)
class B4():
    # 'OLD_Input_Population'!B4
    value = 23924
    isdatetime = True

@register(OLD_Input_Population)
class C4():
    # 'OLD_Input_Population'!C4
    value = 703.8

@register(OLD_Input_Population)
class E4():
    # 'OLD_Input_Population'!E4
    value = 715.4

@register(OLD_Input_Population)
class A5():
    # 'OLD_Input_Population'!A5
    value = 1966
    formula = "=YEAR(B5)"
    @eval_fn
    def A5():
        b5_1 = OLD_Input_Population.B5()
        var_1 = YEAR(b5_1)
        return var_1

@register(OLD_Input_Population)
class B5():
    # 'OLD_Input_Population'!B5
    value = 24289
    isdatetime = True

@register(OLD_Input_Population)
class C5():
    # 'OLD_Input_Population'!C5
    value = 710.3

@register(OLD_Input_Population)
class D5():
    # 'OLD_Input_Population'!D5
    value = 0.9

@register(OLD_Input_Population)
class E5():
    # 'OLD_Input_Population'!E5
    value = 724.6

@register(OLD_Input_Population)
class F5():
    # 'OLD_Input_Population'!F5
    value = 1.3

@register(OLD_Input_Population)
class A6():
    # 'OLD_Input_Population'!A6
    value = 1967
    formula = "=YEAR(B6)"
    @eval_fn
    def A6():
        b6_1 = OLD_Input_Population.B6()
        var_1 = YEAR(b6_1)
        return var_1

@register(OLD_Input_Population)
class B6():
    # 'OLD_Input_Population'!B6
    value = 24654
    isdatetime = True

@register(OLD_Input_Population)
class C6():
    # 'OLD_Input_Population'!C6
    value = 722.5

@register(OLD_Input_Population)
class D6():
    # 'OLD_Input_Population'!D6
    value = 1.7

@register(OLD_Input_Population)
class E6():
    # 'OLD_Input_Population'!E6
    value = 742.6

@register(OLD_Input_Population)
class F6():
    # 'OLD_Input_Population'!F6
    value = 2.5

@register(OLD_Input_Population)
class A7():
    # 'OLD_Input_Population'!A7
    value = 1968
    formula = "=YEAR(B7)"
    @eval_fn
    def A7():
        b7_1 = OLD_Input_Population.B7()
        var_1 = YEAR(b7_1)
        return var_1

@register(OLD_Input_Population)
class B7():
    # 'OLD_Input_Population'!B7
    value = 25020
    isdatetime = True

@register(OLD_Input_Population)
class C7():
    # 'OLD_Input_Population'!C7
    value = 734.5

@register(OLD_Input_Population)
class D7():
    # 'OLD_Input_Population'!D7
    value = 1.7

@register(OLD_Input_Population)
class E7():
    # 'OLD_Input_Population'!E7
    value = 758.8

@register(OLD_Input_Population)
class F7():
    # 'OLD_Input_Population'!F7
    value = 2.2

@register(OLD_Input_Population)
class A8():
    # 'OLD_Input_Population'!A8
    value = 1969
    formula = "=YEAR(B8)"
    @eval_fn
    def A8():
        b8_1 = OLD_Input_Population.B8()
        var_1 = YEAR(b8_1)
        return var_1

@register(OLD_Input_Population)
class B8():
    # 'OLD_Input_Population'!B8
    value = 25385
    isdatetime = True

@register(OLD_Input_Population)
class C8():
    # 'OLD_Input_Population'!C8
    value = 750.2

@register(OLD_Input_Population)
class D8():
    # 'OLD_Input_Population'!D8
    value = 2.1

@register(OLD_Input_Population)
class E8():
    # 'OLD_Input_Population'!E8
    value = 778.8

@register(OLD_Input_Population)
class F8():
    # 'OLD_Input_Population'!F8
    value = 2.6

@register(OLD_Input_Population)
class A9():
    # 'OLD_Input_Population'!A9
    value = 1970
    formula = "=YEAR(B9)"
    @eval_fn
    def A9():
        b9_1 = OLD_Input_Population.B9()
        var_1 = YEAR(b9_1)
        return var_1

@register(OLD_Input_Population)
class B9():
    # 'OLD_Input_Population'!B9
    value = 25750
    isdatetime = True

@register(OLD_Input_Population)
class C9():
    # 'OLD_Input_Population'!C9
    value = 771.6

@register(OLD_Input_Population)
class D9():
    # 'OLD_Input_Population'!D9
    value = 2.9

@register(OLD_Input_Population)
class E9():
    # 'OLD_Input_Population'!E9
    value = 798.6

@register(OLD_Input_Population)
class F9():
    # 'OLD_Input_Population'!F9
    value = 2.5

@register(OLD_Input_Population)
class A10():
    # 'OLD_Input_Population'!A10
    value = 1971
    formula = "=YEAR(B10)"
    @eval_fn
    def A10():
        b10_1 = OLD_Input_Population.B10()
        var_1 = YEAR(b10_1)
        return var_1

@register(OLD_Input_Population)
class B10():
    # 'OLD_Input_Population'!B10
    value = 26115
    isdatetime = True

@register(OLD_Input_Population)
class C10():
    # 'OLD_Input_Population'!C10
    value = 801.6

@register(OLD_Input_Population)
class D10():
    # 'OLD_Input_Population'!D10
    value = 3.9

@register(OLD_Input_Population)
class E10():
    # 'OLD_Input_Population'!E10
    value = 833.1

@register(OLD_Input_Population)
class F10():
    # 'OLD_Input_Population'!F10
    value = 4.3

@register(OLD_Input_Population)
class A11():
    # 'OLD_Input_Population'!A11
    value = 1972
    formula = "=YEAR(B11)"
    @eval_fn
    def A11():
        b11_1 = OLD_Input_Population.B11()
        var_1 = YEAR(b11_1)
        return var_1

@register(OLD_Input_Population)
class B11():
    # 'OLD_Input_Population'!B11
    value = 26481
    isdatetime = True

@register(OLD_Input_Population)
class C11():
    # 'OLD_Input_Population'!C11
    value = 828.3

@register(OLD_Input_Population)
class D11():
    # 'OLD_Input_Population'!D11
    value = 3.3

@register(OLD_Input_Population)
class E11():
    # 'OLD_Input_Population'!E11
    value = 869.8

@register(OLD_Input_Population)
class F11():
    # 'OLD_Input_Population'!F11
    value = 4.4

@register(OLD_Input_Population)
class A12():
    # 'OLD_Input_Population'!A12
    value = 1973
    formula = "=YEAR(B12)"
    @eval_fn
    def A12():
        b12_1 = OLD_Input_Population.B12()
        var_1 = YEAR(b12_1)
        return var_1

@register(OLD_Input_Population)
class B12():
    # 'OLD_Input_Population'!B12
    value = 26846
    isdatetime = True

@register(OLD_Input_Population)
class C12():
    # 'OLD_Input_Population'!C12
    value = 851.6

@register(OLD_Input_Population)
class D12():
    # 'OLD_Input_Population'!D12
    value = 2.8

@register(OLD_Input_Population)
class E12():
    # 'OLD_Input_Population'!E12
    value = 901.3

@register(OLD_Input_Population)
class F12():
    # 'OLD_Input_Population'!F12
    value = 3.6

@register(OLD_Input_Population)
class A13():
    # 'OLD_Input_Population'!A13
    value = 1974
    formula = "=YEAR(B13)"
    @eval_fn
    def A13():
        b13_1 = OLD_Input_Population.B13()
        var_1 = YEAR(b13_1)
        return var_1

@register(OLD_Input_Population)
class B13():
    # 'OLD_Input_Population'!B13
    value = 27211
    isdatetime = True

@register(OLD_Input_Population)
class C13():
    # 'OLD_Input_Population'!C13
    value = 868

@register(OLD_Input_Population)
class D13():
    # 'OLD_Input_Population'!D13
    value = 1.9

@register(OLD_Input_Population)
class E13():
    # 'OLD_Input_Population'!E13
    value = 923.7

@register(OLD_Input_Population)
class F13():
    # 'OLD_Input_Population'!F13
    value = 2.5

@register(OLD_Input_Population)
class A14():
    # 'OLD_Input_Population'!A14
    value = 1975
    formula = "=YEAR(B14)"
    @eval_fn
    def A14():
        b14_1 = OLD_Input_Population.B14()
        var_1 = YEAR(b14_1)
        return var_1

@register(OLD_Input_Population)
class B14():
    # 'OLD_Input_Population'!B14
    value = 27576
    isdatetime = True

@register(OLD_Input_Population)
class C14():
    # 'OLD_Input_Population'!C14
    value = 886.2

@register(OLD_Input_Population)
class D14():
    # 'OLD_Input_Population'!D14
    value = 2.1

@register(OLD_Input_Population)
class E14():
    # 'OLD_Input_Population'!E14
    value = 943.5

@register(OLD_Input_Population)
class F14():
    # 'OLD_Input_Population'!F14
    value = 2.1

@register(OLD_Input_Population)
class A15():
    # 'OLD_Input_Population'!A15
    value = 1976
    formula = "=YEAR(B15)"
    @eval_fn
    def A15():
        b15_1 = OLD_Input_Population.B15()
        var_1 = YEAR(b15_1)
        return var_1

@register(OLD_Input_Population)
class B15():
    # 'OLD_Input_Population'!B15
    value = 27942
    isdatetime = True

@register(OLD_Input_Population)
class C15():
    # 'OLD_Input_Population'!C15
    value = 904.2

@register(OLD_Input_Population)
class D15():
    # 'OLD_Input_Population'!D15
    value = 2

@register(OLD_Input_Population)
class E15():
    # 'OLD_Input_Population'!E15
    value = 970.3

@register(OLD_Input_Population)
class F15():
    # 'OLD_Input_Population'!F15
    value = 2.8

@register(OLD_Input_Population)
class A16():
    # 'OLD_Input_Population'!A16
    value = 1977
    formula = "=YEAR(B16)"
    @eval_fn
    def A16():
        b16_1 = OLD_Input_Population.B16()
        var_1 = YEAR(b16_1)
        return var_1

@register(OLD_Input_Population)
class B16():
    # 'OLD_Input_Population'!B16
    value = 28307
    isdatetime = True

@register(OLD_Input_Population)
class C16():
    # 'OLD_Input_Population'!C16
    value = 918.3

@register(OLD_Input_Population)
class D16():
    # 'OLD_Input_Population'!D16
    value = 1.6

@register(OLD_Input_Population)
class E16():
    # 'OLD_Input_Population'!E16
    value = 992.3

@register(OLD_Input_Population)
class F16():
    # 'OLD_Input_Population'!F16
    value = 2.3

@register(OLD_Input_Population)
class A17():
    # 'OLD_Input_Population'!A17
    value = 1978
    formula = "=YEAR(B17)"
    @eval_fn
    def A17():
        b17_1 = OLD_Input_Population.B17()
        var_1 = YEAR(b17_1)
        return var_1

@register(OLD_Input_Population)
class B17():
    # 'OLD_Input_Population'!B17
    value = 28672
    isdatetime = True

@register(OLD_Input_Population)
class C17():
    # 'OLD_Input_Population'!C17
    value = 931.6

@register(OLD_Input_Population)
class D17():
    # 'OLD_Input_Population'!D17
    value = 1.4

@register(OLD_Input_Population)
class E17():
    # 'OLD_Input_Population'!E17
    value = 1014.3

@register(OLD_Input_Population)
class F17():
    # 'OLD_Input_Population'!F17
    value = 2.2

@register(OLD_Input_Population)
class A18():
    # 'OLD_Input_Population'!A18
    value = 1979
    formula = "=YEAR(B18)"
    @eval_fn
    def A18():
        b18_1 = OLD_Input_Population.B18()
        var_1 = YEAR(b18_1)
        return var_1

@register(OLD_Input_Population)
class B18():
    # 'OLD_Input_Population'!B18
    value = 29037
    isdatetime = True

@register(OLD_Input_Population)
class C18():
    # 'OLD_Input_Population'!C18
    value = 953.3

@register(OLD_Input_Population)
class D18():
    # 'OLD_Input_Population'!D18
    value = 2.3

@register(OLD_Input_Population)
class E18():
    # 'OLD_Input_Population'!E18
    value = 1042.7

@register(OLD_Input_Population)
class F18():
    # 'OLD_Input_Population'!F18
    value = 2.8

@register(OLD_Input_Population)
class A19():
    # 'OLD_Input_Population'!A19
    value = 1980
    formula = "=YEAR(B19)"
    @eval_fn
    def A19():
        b19_1 = OLD_Input_Population.B19()
        var_1 = YEAR(b19_1)
        return var_1

@register(OLD_Input_Population)
class B19():
    # 'OLD_Input_Population'!B19
    value = 29403
    isdatetime = True

@register(OLD_Input_Population)
class C19():
    # 'OLD_Input_Population'!C19
    value = 967.7

@register(OLD_Input_Population)
class D19():
    # 'OLD_Input_Population'!D19
    value = 1.5

@register(OLD_Input_Population)
class E19():
    # 'OLD_Input_Population'!E19
    value = 1054.2

@register(OLD_Input_Population)
class F19():
    # 'OLD_Input_Population'!F19
    value = 1.1

@register(OLD_Input_Population)
class A20():
    # 'OLD_Input_Population'!A20
    value = 1981
    formula = "=YEAR(B20)"
    @eval_fn
    def A20():
        b20_1 = OLD_Input_Population.B20()
        var_1 = YEAR(b20_1)
        return var_1

@register(OLD_Input_Population)
class B20():
    # 'OLD_Input_Population'!B20
    value = 29768
    isdatetime = True

@register(OLD_Input_Population)
class C20():
    # 'OLD_Input_Population'!C20
    value = 978.2

@register(OLD_Input_Population)
class D20():
    # 'OLD_Input_Population'!D20
    value = 1.1

@register(OLD_Input_Population)
class E20():
    # 'OLD_Input_Population'!E20
    value = 1061.6

@register(OLD_Input_Population)
class F20():
    # 'OLD_Input_Population'!F20
    value = 0.7

@register(OLD_Input_Population)
class A21():
    # 'OLD_Input_Population'!A21
    value = 1982
    formula = "=YEAR(B21)"
    @eval_fn
    def A21():
        b21_1 = OLD_Input_Population.B21()
        var_1 = YEAR(b21_1)
        return var_1

@register(OLD_Input_Population)
class B21():
    # 'OLD_Input_Population'!B21
    value = 30133
    isdatetime = True

@register(OLD_Input_Population)
class C21():
    # 'OLD_Input_Population'!C21
    value = 993.8

@register(OLD_Input_Population)
class D21():
    # 'OLD_Input_Population'!D21
    value = 1.6

@register(OLD_Input_Population)
class E21():
    # 'OLD_Input_Population'!E21
    value = 1082.3

@register(OLD_Input_Population)
class F21():
    # 'OLD_Input_Population'!F21
    value = 2

@register(OLD_Input_Population)
class A22():
    # 'OLD_Input_Population'!A22
    value = 1983
    formula = "=YEAR(B22)"
    @eval_fn
    def A22():
        b22_1 = OLD_Input_Population.B22()
        var_1 = YEAR(b22_1)
        return var_1

@register(OLD_Input_Population)
class B22():
    # 'OLD_Input_Population'!B22
    value = 30498
    isdatetime = True

@register(OLD_Input_Population)
class C22():
    # 'OLD_Input_Population'!C22
    value = 1012.7

@register(OLD_Input_Population)
class D22():
    # 'OLD_Input_Population'!D22
    value = 1.9

@register(OLD_Input_Population)
class E22():
    # 'OLD_Input_Population'!E22
    value = 1107.6

@register(OLD_Input_Population)
class F22():
    # 'OLD_Input_Population'!F22
    value = 2.3

@register(OLD_Input_Population)
class A23():
    # 'OLD_Input_Population'!A23
    value = 1984
    formula = "=YEAR(B23)"
    @eval_fn
    def A23():
        b23_1 = OLD_Input_Population.B23()
        var_1 = YEAR(b23_1)
        return var_1

@register(OLD_Input_Population)
class B23():
    # 'OLD_Input_Population'!B23
    value = 30864
    isdatetime = True

@register(OLD_Input_Population)
class C23():
    # 'OLD_Input_Population'!C23
    value = 1027.9

@register(OLD_Input_Population)
class D23():
    # 'OLD_Input_Population'!D23
    value = 1.5

@register(OLD_Input_Population)
class E23():
    # 'OLD_Input_Population'!E23
    value = 1129.1

@register(OLD_Input_Population)
class F23():
    # 'OLD_Input_Population'!F23
    value = 1.9

@register(OLD_Input_Population)
class A24():
    # 'OLD_Input_Population'!A24
    value = 1985
    formula = "=YEAR(B24)"
    @eval_fn
    def A24():
        b24_1 = OLD_Input_Population.B24()
        var_1 = YEAR(b24_1)
        return var_1

@register(OLD_Input_Population)
class B24():
    # 'OLD_Input_Population'!B24
    value = 31229
    isdatetime = True

@register(OLD_Input_Population)
class C24():
    # 'OLD_Input_Population'!C24
    value = 1039.7

@register(OLD_Input_Population)
class D24():
    # 'OLD_Input_Population'!D24
    value = 1.1

@register(OLD_Input_Population)
class E24():
    # 'OLD_Input_Population'!E24
    value = 1136.2

@register(OLD_Input_Population)
class F24():
    # 'OLD_Input_Population'!F24
    value = 0.6

@register(OLD_Input_Population)
class A25():
    # 'OLD_Input_Population'!A25
    value = 1986
    formula = "=YEAR(B25)"
    @eval_fn
    def A25():
        b25_1 = OLD_Input_Population.B25()
        var_1 = YEAR(b25_1)
        return var_1

@register(OLD_Input_Population)
class B25():
    # 'OLD_Input_Population'!B25
    value = 31594
    isdatetime = True

@register(OLD_Input_Population)
class C25():
    # 'OLD_Input_Population'!C25
    value = 1051.8

@register(OLD_Input_Population)
class D25():
    # 'OLD_Input_Population'!D25
    value = 1.2

@register(OLD_Input_Population)
class E25():
    # 'OLD_Input_Population'!E25
    value = 1165.8

@register(OLD_Input_Population)
class F25():
    # 'OLD_Input_Population'!F25
    value = 2.6

@register(OLD_Input_Population)
class A26():
    # 'OLD_Input_Population'!A26
    value = 1987
    formula = "=YEAR(B26)"
    @eval_fn
    def A26():
        b26_1 = OLD_Input_Population.B26()
        var_1 = YEAR(b26_1)
        return var_1

@register(OLD_Input_Population)
class B26():
    # 'OLD_Input_Population'!B26
    value = 31959
    isdatetime = True

@register(OLD_Input_Population)
class C26():
    # 'OLD_Input_Population'!C26
    value = 1067.9

@register(OLD_Input_Population)
class D26():
    # 'OLD_Input_Population'!D26
    value = 1.5

@register(OLD_Input_Population)
class E26():
    # 'OLD_Input_Population'!E26
    value = 1185.4

@register(OLD_Input_Population)
class F26():
    # 'OLD_Input_Population'!F26
    value = 1.7

@register(OLD_Input_Population)
class A27():
    # 'OLD_Input_Population'!A27
    value = 1988
    formula = "=YEAR(B27)"
    @eval_fn
    def A27():
        b27_1 = OLD_Input_Population.B27()
        var_1 = YEAR(b27_1)
        return var_1

@register(OLD_Input_Population)
class B27():
    # 'OLD_Input_Population'!B27
    value = 32325
    isdatetime = True

@register(OLD_Input_Population)
class C27():
    # 'OLD_Input_Population'!C27
    value = 1079.8

@register(OLD_Input_Population)
class D27():
    # 'OLD_Input_Population'!D27
    value = 1.1

@register(OLD_Input_Population)
class E27():
    # 'OLD_Input_Population'!E27
    value = 1198.6

@register(OLD_Input_Population)
class F27():
    # 'OLD_Input_Population'!F27
    value = 1.1

@register(OLD_Input_Population)
class A28():
    # 'OLD_Input_Population'!A28
    value = 1989
    formula = "=YEAR(B28)"
    @eval_fn
    def A28():
        b28_1 = OLD_Input_Population.B28()
        var_1 = YEAR(b28_1)
        return var_1

@register(OLD_Input_Population)
class B28():
    # 'OLD_Input_Population'!B28
    value = 32690
    isdatetime = True

@register(OLD_Input_Population)
class C28():
    # 'OLD_Input_Population'!C28
    value = 1094.6

@register(OLD_Input_Population)
class D28():
    # 'OLD_Input_Population'!D28
    value = 1.4

@register(OLD_Input_Population)
class E28():
    # 'OLD_Input_Population'!E28
    value = 1234.6

@register(OLD_Input_Population)
class F28():
    # 'OLD_Input_Population'!F28
    value = 3

@register(OLD_Input_Population)
class A29():
    # 'OLD_Input_Population'!A29
    value = 1990
    formula = "=YEAR(B29)"
    @eval_fn
    def A29():
        b29_1 = OLD_Input_Population.B29()
        var_1 = YEAR(b29_1)
        return var_1

@register(OLD_Input_Population)
class B29():
    # 'OLD_Input_Population'!B29
    value = 33055
    isdatetime = True

@register(OLD_Input_Population)
class C29():
    # 'OLD_Input_Population'!C29
    value = 1113.5

@register(OLD_Input_Population)
class D29():
    # 'OLD_Input_Population'!D29
    value = 1.7

@register(OLD_Input_Population)
class E29():
    # 'OLD_Input_Population'!E29
    value = 1257.319
    formula = "=H29/1000"
    @eval_fn
    def E29():
        h29_1 = OLD_Input_Population.H29()
        var_1 = divide(h29_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F29():
    # 'OLD_Input_Population'!F29
    value = 1.8

@register(OLD_Input_Population)
class H29():
    # 'OLD_Input_Population'!H29
    value = 1257319

@register(OLD_Input_Population)
class A30():
    # 'OLD_Input_Population'!A30
    value = 1991
    formula = "=YEAR(B30)"
    @eval_fn
    def A30():
        b30_1 = OLD_Input_Population.B30()
        var_1 = YEAR(b30_1)
        return var_1

@register(OLD_Input_Population)
class B30():
    # 'OLD_Input_Population'!B30
    value = 33420
    isdatetime = True

@register(OLD_Input_Population)
class C30():
    # 'OLD_Input_Population'!C30
    value = 1136.8

@register(OLD_Input_Population)
class D30():
    # 'OLD_Input_Population'!D30
    value = 2.1

@register(OLD_Input_Population)
class E30():
    # 'OLD_Input_Population'!E30
    value = 1252.265
    formula = "=H30/1000"
    @eval_fn
    def E30():
        h30_1 = OLD_Input_Population.H30()
        var_1 = divide(h30_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F30():
    # 'OLD_Input_Population'!F30
    value = -0.4

@register(OLD_Input_Population)
class H30():
    # 'OLD_Input_Population'!H30
    value = 1252265

@register(OLD_Input_Population)
class A31():
    # 'OLD_Input_Population'!A31
    value = 1992
    formula = "=YEAR(B31)"
    @eval_fn
    def A31():
        b31_1 = OLD_Input_Population.B31()
        var_1 = YEAR(b31_1)
        return var_1

@register(OLD_Input_Population)
class B31():
    # 'OLD_Input_Population'!B31
    value = 33786
    isdatetime = True

@register(OLD_Input_Population)
class C31():
    # 'OLD_Input_Population'!C31
    value = 1158.6

@register(OLD_Input_Population)
class D31():
    # 'OLD_Input_Population'!D31
    value = 1.9

@register(OLD_Input_Population)
class E31():
    # 'OLD_Input_Population'!E31
    value = 1271.662
    formula = "=H31/1000"
    @eval_fn
    def E31():
        h31_1 = OLD_Input_Population.H31()
        var_1 = divide(h31_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F31():
    # 'OLD_Input_Population'!F31
    value = 1.5

@register(OLD_Input_Population)
class H31():
    # 'OLD_Input_Population'!H31
    value = 1271662

@register(OLD_Input_Population)
class A32():
    # 'OLD_Input_Population'!A32
    value = 1993
    formula = "=YEAR(B32)"
    @eval_fn
    def A32():
        b32_1 = OLD_Input_Population.B32()
        var_1 = YEAR(b32_1)
        return var_1

@register(OLD_Input_Population)
class B32():
    # 'OLD_Input_Population'!B32
    value = 34151
    isdatetime = True

@register(OLD_Input_Population)
class C32():
    # 'OLD_Input_Population'!C32
    value = 1172.8

@register(OLD_Input_Population)
class D32():
    # 'OLD_Input_Population'!D32
    value = 1.2

@register(OLD_Input_Population)
class E32():
    # 'OLD_Input_Population'!E32
    value = 1267.849
    formula = "=H32/1000"
    @eval_fn
    def E32():
        h32_1 = OLD_Input_Population.H32()
        var_1 = divide(h32_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F32():
    # 'OLD_Input_Population'!F32
    value = -0.3

@register(OLD_Input_Population)
class H32():
    # 'OLD_Input_Population'!H32
    value = 1267849

@register(OLD_Input_Population)
class A33():
    # 'OLD_Input_Population'!A33
    value = 1994
    formula = "=YEAR(B33)"
    @eval_fn
    def A33():
        b33_1 = OLD_Input_Population.B33()
        var_1 = YEAR(b33_1)
        return var_1

@register(OLD_Input_Population)
class B33():
    # 'OLD_Input_Population'!B33
    value = 34516
    isdatetime = True

@register(OLD_Input_Population)
class C33():
    # 'OLD_Input_Population'!C33
    value = 1187.5

@register(OLD_Input_Population)
class D33():
    # 'OLD_Input_Population'!D33
    value = 1.3

@register(OLD_Input_Population)
class E33():
    # 'OLD_Input_Population'!E33
    value = 1289.804
    formula = "=H33/1000"
    @eval_fn
    def E33():
        h33_1 = OLD_Input_Population.H33()
        var_1 = divide(h33_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F33():
    # 'OLD_Input_Population'!F33
    value = 1.7

@register(OLD_Input_Population)
class H33():
    # 'OLD_Input_Population'!H33
    value = 1289804

@register(OLD_Input_Population)
class A34():
    # 'OLD_Input_Population'!A34
    value = 1995
    formula = "=YEAR(B34)"
    @eval_fn
    def A34():
        b34_1 = OLD_Input_Population.B34()
        var_1 = YEAR(b34_1)
        return var_1

@register(OLD_Input_Population)
class B34():
    # 'OLD_Input_Population'!B34
    value = 34881
    isdatetime = True

@register(OLD_Input_Population)
class C34():
    # 'OLD_Input_Population'!C34
    value = 1196.9

@register(OLD_Input_Population)
class D34():
    # 'OLD_Input_Population'!D34
    value = 0.8

@register(OLD_Input_Population)
class E34():
    # 'OLD_Input_Population'!E34
    value = 1298.096
    formula = "=H34/1000"
    @eval_fn
    def E34():
        h34_1 = OLD_Input_Population.H34()
        var_1 = divide(h34_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F34():
    # 'OLD_Input_Population'!F34
    value = 0.6

@register(OLD_Input_Population)
class H34():
    # 'OLD_Input_Population'!H34
    value = 1298096

@register(OLD_Input_Population)
class A35():
    # 'OLD_Input_Population'!A35
    value = 1996
    formula = "=YEAR(B35)"
    @eval_fn
    def A35():
        b35_1 = OLD_Input_Population.B35()
        var_1 = YEAR(b35_1)
        return var_1

@register(OLD_Input_Population)
class B35():
    # 'OLD_Input_Population'!B35
    value = 35247
    isdatetime = True

@register(OLD_Input_Population)
class C35():
    # 'OLD_Input_Population'!C35
    value = 1203.8

@register(OLD_Input_Population)
class D35():
    # 'OLD_Input_Population'!D35
    value = 0.6

@register(OLD_Input_Population)
class E35():
    # 'OLD_Input_Population'!E35
    value = 1303.915
    formula = "=H35/1000"
    @eval_fn
    def E35():
        h35_1 = OLD_Input_Population.H35()
        var_1 = divide(h35_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F35():
    # 'OLD_Input_Population'!F35
    value = 0.4

@register(OLD_Input_Population)
class H35():
    # 'OLD_Input_Population'!H35
    value = 1303915

@register(OLD_Input_Population)
class A36():
    # 'OLD_Input_Population'!A36
    value = 1997
    formula = "=YEAR(B36)"
    @eval_fn
    def A36():
        b36_1 = OLD_Input_Population.B36()
        var_1 = YEAR(b36_1)
        return var_1

@register(OLD_Input_Population)
class B36():
    # 'OLD_Input_Population'!B36
    value = 35612
    isdatetime = True

@register(OLD_Input_Population)
class C36():
    # 'OLD_Input_Population'!C36
    value = 1211.6

@register(OLD_Input_Population)
class D36():
    # 'OLD_Input_Population'!D36
    value = 0.7

@register(OLD_Input_Population)
class E36():
    # 'OLD_Input_Population'!E36
    value = 1327.93
    formula = "=H36/1000"
    @eval_fn
    def E36():
        h36_1 = OLD_Input_Population.H36()
        var_1 = divide(h36_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F36():
    # 'OLD_Input_Population'!F36
    value = 1.8

@register(OLD_Input_Population)
class H36():
    # 'OLD_Input_Population'!H36
    value = 1327930

@register(OLD_Input_Population)
class A37():
    # 'OLD_Input_Population'!A37
    value = 1998
    formula = "=YEAR(B37)"
    @eval_fn
    def A37():
        b37_1 = OLD_Input_Population.B37()
        var_1 = YEAR(b37_1)
        return var_1

@register(OLD_Input_Population)
class B37():
    # 'OLD_Input_Population'!B37
    value = 35977
    isdatetime = True

@register(OLD_Input_Population)
class C37():
    # 'OLD_Input_Population'!C37
    value = 1215.2

@register(OLD_Input_Population)
class D37():
    # 'OLD_Input_Population'!D37
    value = 0.3

@register(OLD_Input_Population)
class E37():
    # 'OLD_Input_Population'!E37
    value = 1334.125
    formula = "=H37/1000"
    @eval_fn
    def E37():
        h37_1 = OLD_Input_Population.H37()
        var_1 = divide(h37_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F37():
    # 'OLD_Input_Population'!F37
    value = 0.5

@register(OLD_Input_Population)
class H37():
    # 'OLD_Input_Population'!H37
    value = 1334125

@register(OLD_Input_Population)
class A38():
    # 'OLD_Input_Population'!A38
    value = 1999
    formula = "=YEAR(B38)"
    @eval_fn
    def A38():
        b38_1 = OLD_Input_Population.B38()
        var_1 = YEAR(b38_1)
        return var_1

@register(OLD_Input_Population)
class B38():
    # 'OLD_Input_Population'!B38
    value = 36342
    isdatetime = True

@register(OLD_Input_Population)
class C38():
    # 'OLD_Input_Population'!C38
    value = 1210.3

@register(OLD_Input_Population)
class D38():
    # 'OLD_Input_Population'!D38
    value = -0.4

@register(OLD_Input_Population)
class E38():
    # 'OLD_Input_Population'!E38
    value = 1332.442
    formula = "=H38/1000"
    @eval_fn
    def E38():
        h38_1 = OLD_Input_Population.H38()
        var_1 = divide(h38_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F38():
    # 'OLD_Input_Population'!F38
    value = -0.1

@register(OLD_Input_Population)
class H38():
    # 'OLD_Input_Population'!H38
    value = 1332442

@register(OLD_Input_Population)
class A39():
    # 'OLD_Input_Population'!A39
    value = 2000
    formula = "=YEAR(B39)"
    @eval_fn
    def A39():
        b39_1 = OLD_Input_Population.B39()
        var_1 = YEAR(b39_1)
        return var_1

@register(OLD_Input_Population)
class B39():
    # 'OLD_Input_Population'!B39
    value = 36708
    isdatetime = True

@register(OLD_Input_Population)
class C39():
    # 'OLD_Input_Population'!C39
    value = 1213.519
    formula = "=G39/1000"
    @eval_fn
    def C39():
        g39_1 = OLD_Input_Population.G39()
        var_1 = divide(g39_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D39():
    # 'OLD_Input_Population'!D39
    value = 0.3

@register(OLD_Input_Population)
class E39():
    # 'OLD_Input_Population'!E39
    value = 1336.005
    formula = "=H39/1000"
    @eval_fn
    def E39():
        h39_1 = OLD_Input_Population.H39()
        var_1 = divide(h39_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F39():
    # 'OLD_Input_Population'!F39
    value = 0.3

@register(OLD_Input_Population)
class G39():
    # 'OLD_Input_Population'!G39
    value = 1213519

@register(OLD_Input_Population)
class H39():
    # 'OLD_Input_Population'!H39
    value = 1336005

@register(OLD_Input_Population)
class A40():
    # 'OLD_Input_Population'!A40
    value = 2001
    formula = "=YEAR(B40)"
    @eval_fn
    def A40():
        b40_1 = OLD_Input_Population.B40()
        var_1 = YEAR(b40_1)
        return var_1

@register(OLD_Input_Population)
class B40():
    # 'OLD_Input_Population'!B40
    value = 37073
    isdatetime = True

@register(OLD_Input_Population)
class C40():
    # 'OLD_Input_Population'!C40
    value = 1225.948
    formula = "=G40/1000"
    @eval_fn
    def C40():
        g40_1 = OLD_Input_Population.G40()
        var_1 = divide(g40_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D40():
    # 'OLD_Input_Population'!D40
    value = 1

@register(OLD_Input_Population)
class E40():
    # 'OLD_Input_Population'!E40
    value = 1337.629
    formula = "=H40/1000"
    @eval_fn
    def E40():
        h40_1 = OLD_Input_Population.H40()
        var_1 = divide(h40_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F40():
    # 'OLD_Input_Population'!F40
    value = 0.1

@register(OLD_Input_Population)
class G40():
    # 'OLD_Input_Population'!G40
    value = 1225948

@register(OLD_Input_Population)
class H40():
    # 'OLD_Input_Population'!H40
    value = 1337629

@register(OLD_Input_Population)
class A41():
    # 'OLD_Input_Population'!A41
    value = 2002
    formula = "=YEAR(B41)"
    @eval_fn
    def A41():
        b41_1 = OLD_Input_Population.B41()
        var_1 = YEAR(b41_1)
        return var_1

@register(OLD_Input_Population)
class B41():
    # 'OLD_Input_Population'!B41
    value = 37438
    isdatetime = True

@register(OLD_Input_Population)
class C41():
    # 'OLD_Input_Population'!C41
    value = 1239.613
    formula = "=G41/1000"
    @eval_fn
    def C41():
        g41_1 = OLD_Input_Population.G41()
        var_1 = divide(g41_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D41():
    # 'OLD_Input_Population'!D41
    value = 1.1

@register(OLD_Input_Population)
class E41():
    # 'OLD_Input_Population'!E41
    value = 1353.051
    formula = "=H41/1000"
    @eval_fn
    def E41():
        h41_1 = OLD_Input_Population.H41()
        var_1 = divide(h41_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F41():
    # 'OLD_Input_Population'!F41
    value = 1.2

@register(OLD_Input_Population)
class G41():
    # 'OLD_Input_Population'!G41
    value = 1239613

@register(OLD_Input_Population)
class H41():
    # 'OLD_Input_Population'!H41
    value = 1353051

@register(OLD_Input_Population)
class A42():
    # 'OLD_Input_Population'!A42
    value = 2003
    formula = "=YEAR(B42)"
    @eval_fn
    def A42():
        b42_1 = OLD_Input_Population.B42()
        var_1 = YEAR(b42_1)
        return var_1

@register(OLD_Input_Population)
class B42():
    # 'OLD_Input_Population'!B42
    value = 37803
    isdatetime = True

@register(OLD_Input_Population)
class C42():
    # 'OLD_Input_Population'!C42
    value = 1251.154
    formula = "=G42/1000"
    @eval_fn
    def C42():
        g42_1 = OLD_Input_Population.G42()
        var_1 = divide(g42_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D42():
    # 'OLD_Input_Population'!D42
    value = 0.9

@register(OLD_Input_Population)
class E42():
    # 'OLD_Input_Population'!E42
    value = 1358.755
    formula = "=H42/1000"
    @eval_fn
    def E42():
        h42_1 = OLD_Input_Population.H42()
        var_1 = divide(h42_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F42():
    # 'OLD_Input_Population'!F42
    value = 0.4

@register(OLD_Input_Population)
class G42():
    # 'OLD_Input_Population'!G42
    value = 1251154

@register(OLD_Input_Population)
class H42():
    # 'OLD_Input_Population'!H42
    value = 1358755

@register(OLD_Input_Population)
class A43():
    # 'OLD_Input_Population'!A43
    value = 2004
    formula = "=YEAR(B43)"
    @eval_fn
    def A43():
        b43_1 = OLD_Input_Population.B43()
        var_1 = YEAR(b43_1)
        return var_1

@register(OLD_Input_Population)
class B43():
    # 'OLD_Input_Population'!B43
    value = 38169
    isdatetime = True

@register(OLD_Input_Population)
class C43():
    # 'OLD_Input_Population'!C43
    value = 1273.569
    formula = "=G43/1000"
    @eval_fn
    def C43():
        g43_1 = OLD_Input_Population.G43()
        var_1 = divide(g43_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D43():
    # 'OLD_Input_Population'!D43
    value = 1.8

@register(OLD_Input_Population)
class E43():
    # 'OLD_Input_Population'!E43
    value = 1387.569
    formula = "=H43/1000"
    @eval_fn
    def E43():
        h43_1 = OLD_Input_Population.H43()
        var_1 = divide(h43_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F43():
    # 'OLD_Input_Population'!F43
    value = 2.1

@register(OLD_Input_Population)
class G43():
    # 'OLD_Input_Population'!G43
    value = 1273569

@register(OLD_Input_Population)
class H43():
    # 'OLD_Input_Population'!H43
    value = 1387569

@register(OLD_Input_Population)
class A44():
    # 'OLD_Input_Population'!A44
    value = 2005
    formula = "=YEAR(B44)"
    @eval_fn
    def A44():
        b44_1 = OLD_Input_Population.B44()
        var_1 = YEAR(b44_1)
        return var_1

@register(OLD_Input_Population)
class B44():
    # 'OLD_Input_Population'!B44
    value = 38534
    isdatetime = True

@register(OLD_Input_Population)
class C44():
    # 'OLD_Input_Population'!C44
    value = 1292.729
    formula = "=G44/1000"
    @eval_fn
    def C44():
        g44_1 = OLD_Input_Population.G44()
        var_1 = divide(g44_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D44():
    # 'OLD_Input_Population'!D44
    value = 1.5

@register(OLD_Input_Population)
class E44():
    # 'OLD_Input_Population'!E44
    value = 1412.5
    formula = "=H44/1000"
    @eval_fn
    def E44():
        h44_1 = OLD_Input_Population.H44()
        var_1 = divide(h44_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F44():
    # 'OLD_Input_Population'!F44
    value = 1.8

@register(OLD_Input_Population)
class G44():
    # 'OLD_Input_Population'!G44
    value = 1292729

@register(OLD_Input_Population)
class H44():
    # 'OLD_Input_Population'!H44
    value = 1412500

@register(OLD_Input_Population)
class A45():
    # 'OLD_Input_Population'!A45
    value = 2006
    formula = "=YEAR(B45)"
    @eval_fn
    def A45():
        b45_1 = OLD_Input_Population.B45()
        var_1 = YEAR(b45_1)
        return var_1

@register(OLD_Input_Population)
class B45():
    # 'OLD_Input_Population'!B45
    value = 38899
    isdatetime = True

@register(OLD_Input_Population)
class C45():
    # 'OLD_Input_Population'!C45
    value = 1309.731
    formula = "=G45/1000"
    @eval_fn
    def C45():
        g45_1 = OLD_Input_Population.G45()
        var_1 = divide(g45_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D45():
    # 'OLD_Input_Population'!D45
    value = 1.3

@register(OLD_Input_Population)
class E45():
    # 'OLD_Input_Population'!E45
    value = 1430.516
    formula = "=H45/1000"
    @eval_fn
    def E45():
        h45_1 = OLD_Input_Population.H45()
        var_1 = divide(h45_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F45():
    # 'OLD_Input_Population'!F45
    value = 1.3

@register(OLD_Input_Population)
class G45():
    # 'OLD_Input_Population'!G45
    value = 1309731

@register(OLD_Input_Population)
class H45():
    # 'OLD_Input_Population'!H45
    value = 1430516

@register(OLD_Input_Population)
class A46():
    # 'OLD_Input_Population'!A46
    value = 2007
    formula = "=YEAR(B46)"
    @eval_fn
    def A46():
        b46_1 = OLD_Input_Population.B46()
        var_1 = YEAR(b46_1)
        return var_1

@register(OLD_Input_Population)
class B46():
    # 'OLD_Input_Population'!B46
    value = 39264
    isdatetime = True

@register(OLD_Input_Population)
class C46():
    # 'OLD_Input_Population'!C46
    value = 1315.675
    formula = "=G46/1000"
    @eval_fn
    def C46():
        g46_1 = OLD_Input_Population.G46()
        var_1 = divide(g46_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D46():
    # 'OLD_Input_Population'!D46
    value = 0.5

@register(OLD_Input_Population)
class E46():
    # 'OLD_Input_Population'!E46
    value = 1433.461
    formula = "=H46/1000"
    @eval_fn
    def E46():
        h46_1 = OLD_Input_Population.H46()
        var_1 = divide(h46_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F46():
    # 'OLD_Input_Population'!F46
    value = 0.2

@register(OLD_Input_Population)
class G46():
    # 'OLD_Input_Population'!G46
    value = 1315675

@register(OLD_Input_Population)
class H46():
    # 'OLD_Input_Population'!H46
    value = 1433461

@register(OLD_Input_Population)
class A47():
    # 'OLD_Input_Population'!A47
    value = 2008
    formula = "=YEAR(B47)"
    @eval_fn
    def A47():
        b47_1 = OLD_Input_Population.B47()
        var_1 = YEAR(b47_1)
        return var_1

@register(OLD_Input_Population)
class B47():
    # 'OLD_Input_Population'!B47
    value = 39630
    isdatetime = True

@register(OLD_Input_Population)
class C47():
    # 'OLD_Input_Population'!C47
    value = 1332.213
    formula = "=G47/1000"
    @eval_fn
    def C47():
        g47_1 = OLD_Input_Population.G47()
        var_1 = divide(g47_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D47():
    # 'OLD_Input_Population'!D47
    value = 1.3

@register(OLD_Input_Population)
class E47():
    # 'OLD_Input_Population'!E47
    value = 1432.62
    formula = "=H47/1000"
    @eval_fn
    def E47():
        h47_1 = OLD_Input_Population.H47()
        var_1 = divide(h47_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F47():
    # 'OLD_Input_Population'!F47
    value = -0.1

@register(OLD_Input_Population)
class G47():
    # 'OLD_Input_Population'!G47
    value = 1332213

@register(OLD_Input_Population)
class H47():
    # 'OLD_Input_Population'!H47
    value = 1432620

@register(OLD_Input_Population)
class A48():
    # 'OLD_Input_Population'!A48
    value = 2009
    formula = "=YEAR(B48)"
    @eval_fn
    def A48():
        b48_1 = OLD_Input_Population.B48()
        var_1 = YEAR(b48_1)
        return var_1

@register(OLD_Input_Population)
class B48():
    # 'OLD_Input_Population'!B48
    value = 39995
    isdatetime = True

@register(OLD_Input_Population)
class C48():
    # 'OLD_Input_Population'!C48
    value = 1346.717
    formula = "=G48/1000"
    @eval_fn
    def C48():
        g48_1 = OLD_Input_Population.G48()
        var_1 = divide(g48_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D48():
    # 'OLD_Input_Population'!D48
    value = 1.1

@register(OLD_Input_Population)
class E48():
    # 'OLD_Input_Population'!E48
    value = 1442.556
    formula = "=H48/1000"
    @eval_fn
    def E48():
        h48_1 = OLD_Input_Population.H48()
        var_1 = divide(h48_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F48():
    # 'OLD_Input_Population'!F48
    value = 0.7

@register(OLD_Input_Population)
class G48():
    # 'OLD_Input_Population'!G48
    value = 1346717

@register(OLD_Input_Population)
class H48():
    # 'OLD_Input_Population'!H48
    value = 1442556

@register(OLD_Input_Population)
class A49():
    # 'OLD_Input_Population'!A49
    value = 2010
    formula = "=YEAR(B49)"
    @eval_fn
    def A49():
        b49_1 = OLD_Input_Population.B49()
        var_1 = YEAR(b49_1)
        return var_1

@register(OLD_Input_Population)
class B49():
    # 'OLD_Input_Population'!B49
    value = 40360
    isdatetime = True

@register(OLD_Input_Population)
class C49():
    # 'OLD_Input_Population'!C49
    value = 1363.95
    formula = "=G49/1000"
    @eval_fn
    def C49():
        g49_1 = OLD_Input_Population.G49()
        var_1 = divide(g49_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D49():
    # 'OLD_Input_Population'!D49
    value = 1.3

@register(OLD_Input_Population)
class E49():
    # 'OLD_Input_Population'!E49
    value = 1468.682
    formula = "=H49/1000"
    @eval_fn
    def E49():
        h49_1 = OLD_Input_Population.H49()
        var_1 = divide(h49_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F49():
    # 'OLD_Input_Population'!F49
    value = 1.8

@register(OLD_Input_Population)
class G49():
    # 'OLD_Input_Population'!G49
    value = 1363950

@register(OLD_Input_Population)
class H49():
    # 'OLD_Input_Population'!H49
    value = 1468682

@register(OLD_Input_Population)
class A50():
    # 'OLD_Input_Population'!A50
    value = 2011
    formula = "=YEAR(B50)"
    @eval_fn
    def A50():
        b50_1 = OLD_Input_Population.B50()
        var_1 = YEAR(b50_1)
        return var_1

@register(OLD_Input_Population)
class B50():
    # 'OLD_Input_Population'!B50
    value = 40725
    isdatetime = True

@register(OLD_Input_Population)
class C50():
    # 'OLD_Input_Population'!C50
    value = 1378.251
    formula = "=G50/1000"
    @eval_fn
    def C50():
        g50_1 = OLD_Input_Population.G50()
        var_1 = divide(g50_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D50():
    # 'OLD_Input_Population'!D50
    value = 1

@register(OLD_Input_Population)
class E50():
    # 'OLD_Input_Population'!E50
    value = 1490.212
    formula = "=H50/1000"
    @eval_fn
    def E50():
        h50_1 = OLD_Input_Population.H50()
        var_1 = divide(h50_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F50():
    # 'OLD_Input_Population'!F50
    value = 1.3

@register(OLD_Input_Population)
class G50():
    # 'OLD_Input_Population'!G50
    value = 1378251

@register(OLD_Input_Population)
class H50():
    # 'OLD_Input_Population'!H50
    value = 1490212

@register(OLD_Input_Population)
class A51():
    # 'OLD_Input_Population'!A51
    value = 2012
    formula = "=YEAR(B51)"
    @eval_fn
    def A51():
        b51_1 = OLD_Input_Population.B51()
        var_1 = YEAR(b51_1)
        return var_1

@register(OLD_Input_Population)
class B51():
    # 'OLD_Input_Population'!B51
    value = 41091
    isdatetime = True

@register(OLD_Input_Population)
class C51():
    # 'OLD_Input_Population'!C51
    value = 1392.766
    formula = "=G51/1000"
    @eval_fn
    def C51():
        g51_1 = OLD_Input_Population.G51()
        var_1 = divide(g51_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D51():
    # 'OLD_Input_Population'!D51
    value = 1

@register(OLD_Input_Population)
class E51():
    # 'OLD_Input_Population'!E51
    value = 1518.048
    formula = "=H51/1000"
    @eval_fn
    def E51():
        h51_1 = OLD_Input_Population.H51()
        var_1 = divide(h51_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F51():
    # 'OLD_Input_Population'!F51
    value = 1.3

@register(OLD_Input_Population)
class G51():
    # 'OLD_Input_Population'!G51
    value = 1392766

@register(OLD_Input_Population)
class H51():
    # 'OLD_Input_Population'!H51
    value = 1518048

@register(OLD_Input_Population)
class A52():
    # 'OLD_Input_Population'!A52
    value = 2013
    formula = "=YEAR(B52)"
    @eval_fn
    def A52():
        b52_1 = OLD_Input_Population.B52()
        var_1 = YEAR(b52_1)
        return var_1

@register(OLD_Input_Population)
class B52():
    # 'OLD_Input_Population'!B52
    value = 41456
    isdatetime = True

@register(OLD_Input_Population)
class C52():
    # 'OLD_Input_Population'!C52
    value = 1408.987
    formula = "=G52/1000"
    @eval_fn
    def C52():
        g52_1 = OLD_Input_Population.G52()
        var_1 = divide(g52_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D52():
    # 'OLD_Input_Population'!D52
    value = 1.16466082601
    formula = "=100*C52/C51-100"
    @eval_fn
    def D52():
        c52_1 = OLD_Input_Population.C52()
        var_1 = mult(100, c52_1)
        c51_1 = OLD_Input_Population.C51()
        var_2 = divide(var_1, c51_1)
        var_3 = sub(var_2, 100)
        return var_3

@register(OLD_Input_Population)
class E52():
    # 'OLD_Input_Population'!E52
    value = 1542.917
    formula = "=H52/1000"
    @eval_fn
    def E52():
        h52_1 = OLD_Input_Population.H52()
        var_1 = divide(h52_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F52():
    # 'OLD_Input_Population'!F52
    value = 1.6382222433
    formula = "=100*E52/E51-100"
    @eval_fn
    def F52():
        e52_1 = OLD_Input_Population.E52()
        var_1 = mult(100, e52_1)
        e51_1 = OLD_Input_Population.E51()
        var_2 = divide(var_1, e51_1)
        var_3 = sub(var_2, 100)
        return var_3

@register(OLD_Input_Population)
class G52():
    # 'OLD_Input_Population'!G52
    value = 1408987

@register(OLD_Input_Population)
class H52():
    # 'OLD_Input_Population'!H52
    value = 1542917

@register(OLD_Input_Population)
class A53():
    # 'OLD_Input_Population'!A53
    value = 2014
    formula = "=YEAR(B53)"
    @eval_fn
    def A53():
        b53_1 = OLD_Input_Population.B53()
        var_1 = YEAR(b53_1)
        return var_1

@register(OLD_Input_Population)
class B53():
    # 'OLD_Input_Population'!B53
    value = 41821
    isdatetime = True

@register(OLD_Input_Population)
class C53():
    # 'OLD_Input_Population'!C53
    value = 1419.561
    formula = "=G53/1000"
    @eval_fn
    def C53():
        g53_1 = OLD_Input_Population.G53()
        var_1 = divide(g53_1, 1000)
        return var_1

@register(OLD_Input_Population)
class D53():
    # 'OLD_Input_Population'!D53
    value = 0.750468244207
    formula = "=100*C53/C52-100"
    @eval_fn
    def D53():
        c53_1 = OLD_Input_Population.C53()
        var_1 = mult(100, c53_1)
        c52_1 = OLD_Input_Population.C52()
        var_2 = divide(var_1, c52_1)
        var_3 = sub(var_2, 100)
        return var_3

@register(OLD_Input_Population)
class E53():
    # 'OLD_Input_Population'!E53
    value = 1559.469
    formula = "=H53/1000"
    @eval_fn
    def E53():
        h53_1 = OLD_Input_Population.H53()
        var_1 = divide(h53_1, 1000)
        return var_1

@register(OLD_Input_Population)
class F53():
    # 'OLD_Input_Population'!F53
    value = 1.07277319519
    formula = "=100*E53/E52-100"
    @eval_fn
    def F53():
        e53_1 = OLD_Input_Population.E53()
        var_1 = mult(100, e53_1)
        e52_1 = OLD_Input_Population.E52()
        var_2 = divide(var_1, e52_1)
        var_3 = sub(var_2, 100)
        return var_3

@register(OLD_Input_Population)
class G53():
    # 'OLD_Input_Population'!G53
    value = 1419561

@register(OLD_Input_Population)
class H53():
    # 'OLD_Input_Population'!H53
    value = 1559469

@register(OLD_Input_Population)
class A54():
    # 'OLD_Input_Population'!A54
    value = 2015
    formula = "=YEAR(B54)"
    @eval_fn
    def A54():
        b54_1 = OLD_Input_Population.B54()
        var_1 = YEAR(b54_1)
        return var_1

@register(OLD_Input_Population)
class B54():
    # 'OLD_Input_Population'!B54
    value = 42186
    isdatetime = True

@register(OLD_Input_Population)
class A55():
    # 'OLD_Input_Population'!A55
    value = 2016
    formula = "=YEAR(B55)"
    @eval_fn
    def A55():
        b55_1 = OLD_Input_Population.B55()
        var_1 = YEAR(b55_1)
        return var_1

@register(OLD_Input_Population)
class B55():
    # 'OLD_Input_Population'!B55
    value = 42552
    isdatetime = True

@register(OLD_Input_Population)
class A56():
    # 'OLD_Input_Population'!A56
    value = 2017
    formula = "=YEAR(B56)"
    @eval_fn
    def A56():
        b56_1 = OLD_Input_Population.B56()
        var_1 = YEAR(b56_1)
        return var_1

@register(OLD_Input_Population)
class B56():
    # 'OLD_Input_Population'!B56
    value = 42917
    isdatetime = True

@register(OLD_Input_Population)
class A57():
    # 'OLD_Input_Population'!A57
    value = 2018
    formula = "=YEAR(B57)"
    @eval_fn
    def A57():
        b57_1 = OLD_Input_Population.B57()
        var_1 = YEAR(b57_1)
        return var_1

@register(OLD_Input_Population)
class B57():
    # 'OLD_Input_Population'!B57
    value = 43282
    isdatetime = True

@register(OLD_Input_Population)
class A58():
    # 'OLD_Input_Population'!A58
    value = 2019
    formula = "=YEAR(B58)"
    @eval_fn
    def A58():
        b58_1 = OLD_Input_Population.B58()
        var_1 = YEAR(b58_1)
        return var_1

@register(OLD_Input_Population)
class B58():
    # 'OLD_Input_Population'!B58
    value = 43647
    isdatetime = True

@register(OLD_Input_Population)
class A59():
    # 'OLD_Input_Population'!A59
    value = 2020
    formula = "=YEAR(B59)"
    @eval_fn
    def A59():
        b59_1 = OLD_Input_Population.B59()
        var_1 = YEAR(b59_1)
        return var_1

@register(OLD_Input_Population)
class B59():
    # 'OLD_Input_Population'!B59
    value = 44013
    isdatetime = True

@register(OLD_Input_Population)
class A60():
    # 'OLD_Input_Population'!A60
    value = 2021
    formula = "=YEAR(B60)"
    @eval_fn
    def A60():
        b60_1 = OLD_Input_Population.B60()
        var_1 = YEAR(b60_1)
        return var_1

@register(OLD_Input_Population)
class B60():
    # 'OLD_Input_Population'!B60
    value = 44378
    isdatetime = True

@register(OLD_Input_Population)
class A61():
    # 'OLD_Input_Population'!A61
    value = 2022
    formula = "=YEAR(B61)"
    @eval_fn
    def A61():
        b61_1 = OLD_Input_Population.B61()
        var_1 = YEAR(b61_1)
        return var_1

@register(OLD_Input_Population)
class B61():
    # 'OLD_Input_Population'!B61
    value = 44743
    isdatetime = True

@register(OLD_Input_Population)
class A62():
    # 'OLD_Input_Population'!A62
    value = 2023
    formula = "=YEAR(B62)"
    @eval_fn
    def A62():
        b62_1 = OLD_Input_Population.B62()
        var_1 = YEAR(b62_1)
        return var_1

@register(OLD_Input_Population)
class B62():
    # 'OLD_Input_Population'!B62
    value = 45108
    isdatetime = True

@register(OLD_Input_Population)
class A63():
    # 'OLD_Input_Population'!A63
    value = 2024
    formula = "=YEAR(B63)"
    @eval_fn
    def A63():
        b63_1 = OLD_Input_Population.B63()
        var_1 = YEAR(b63_1)
        return var_1

@register(OLD_Input_Population)
class B63():
    # 'OLD_Input_Population'!B63
    value = 45474
    isdatetime = True

@register(OLD_Input_Population)
class A64():
    # 'OLD_Input_Population'!A64
    value = 2025
    formula = "=YEAR(B64)"
    @eval_fn
    def A64():
        b64_1 = OLD_Input_Population.B64()
        var_1 = YEAR(b64_1)
        return var_1

@register(OLD_Input_Population)
class B64():
    # 'OLD_Input_Population'!B64
    value = 45839
    isdatetime = True

@register(OLD_Input_Population)
class A65():
    # 'OLD_Input_Population'!A65
    value = 2026
    formula = "=YEAR(B65)"
    @eval_fn
    def A65():
        b65_1 = OLD_Input_Population.B65()
        var_1 = YEAR(b65_1)
        return var_1

@register(OLD_Input_Population)
class B65():
    # 'OLD_Input_Population'!B65
    value = 46204
    isdatetime = True

@register(OLD_Input_Population)
class A66():
    # 'OLD_Input_Population'!A66
    value = 2027
    formula = "=YEAR(B66)"
    @eval_fn
    def A66():
        b66_1 = OLD_Input_Population.B66()
        var_1 = YEAR(b66_1)
        return var_1

@register(OLD_Input_Population)
class B66():
    # 'OLD_Input_Population'!B66
    value = 46569
    isdatetime = True

@register(OLD_Input_Population)
class A67():
    # 'OLD_Input_Population'!A67
    value = 2028
    formula = "=YEAR(B67)"
    @eval_fn
    def A67():
        b67_1 = OLD_Input_Population.B67()
        var_1 = YEAR(b67_1)
        return var_1

@register(OLD_Input_Population)
class B67():
    # 'OLD_Input_Population'!B67
    value = 46935
    isdatetime = True

@register(OLD_Input_Population)
class A68():
    # 'OLD_Input_Population'!A68
    value = 2029
    formula = "=YEAR(B68)"
    @eval_fn
    def A68():
        b68_1 = OLD_Input_Population.B68()
        var_1 = YEAR(b68_1)
        return var_1

@register(OLD_Input_Population)
class B68():
    # 'OLD_Input_Population'!B68
    value = 47300
    isdatetime = True

@register(OLD_Input_Population)
class A69():
    # 'OLD_Input_Population'!A69
    value = 2030
    formula = "=YEAR(B69)"
    @eval_fn
    def A69():
        b69_1 = OLD_Input_Population.B69()
        var_1 = YEAR(b69_1)
        return var_1

@register(OLD_Input_Population)
class B69():
    # 'OLD_Input_Population'!B69
    value = 47665
    isdatetime = True

@register(OLD_Input_Population)
class B70():
    # 'OLD_Input_Population'!B70
    value = '''2015 update notes: Yellow areas indicate cells changed in this update.  Exact figures for resident population and de facto population from DBEDT 2014 databook have been used.  Population % change is calculated from actual figures now.  Armed Forces & Components of Change are not updated as they are not utilized anywhwere.

Additionally, the entire table was reversed to oldest year at top, newest at bottom'''