# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
SNG = Worksheet('SNG', 10, 10)



@register(SNG)
class A1():
    # 'SNG'!A1
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(SNG)
class C1():
    # 'SNG'!C1
    value = "Green Indicates final values used"

@register(SNG)
class I1():
    # 'SNG'!I1
    value = "Yellow Indicates Intermediate Calculation"

@register(SNG)
class I3():
    # 'SNG'!I3
    value = "NGTXD"

@register(SNG)
class A4():
    # 'SNG'!A4
    value = "Sourcekey"

@register(SNG)
class C4():
    # 'SNG'!C4
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(SNG)
class I4():
    # 'SNG'!I4
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(SNG)
class A5():
    # 'SNG'!A5
    value = "Date"

@register(SNG)
class B5():
    # 'SNG'!B5
    value = "Year"

@register(SNG)
class C5():
    # 'SNG'!C5
    value = "Hawaii Annual SNG Price Average based on EIA ($/Thousand Cubic Foot)"

@register(SNG)
class I5():
    # 'SNG'!I5
    value = "From EIA Consumption data (Dollars per million Btu)"

@register(SNG)
class J5():
    # 'SNG'!J5
    value = "Mont Belvieu, TX Propane Spot Price FOB (Dollars per Gallon)"

@register(SNG)
class K5():
    # 'SNG'!K5
    value = "Mont Belvieu, TX Propane Spot Price FOB (Dollars per MMBTU)"

@register(SNG)
class L5():
    # 'SNG'!L5
    value = "HI-Specific Factor"

@register(SNG)
class A6():
    # 'SNG'!A6
    value = 33770
    isdatetime = True

@register(SNG)
class B6():
    # 'SNG'!B6
    value = 1992
    formula = "=YEAR(A6)"
    @eval_fn
    def B6():
        a6_1 = SNG.A6()
        var_1 = YEAR(a6_1)
        return var_1

@register(SNG)
class C6():
    # 'SNG'!C6
    value = 13.33
    formula = "=VLOOKUP(B6,$H:$I,2,FALSE)"
    @eval_fn
    def C6():
        b6_1 = SNG.B6()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b6_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H6():
    # 'SNG'!H6
    value = 1970

@register(SNG)
class I6():
    # 'SNG'!I6
    value = 0
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H6,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I6():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h6_1 = SNG.H6()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h6_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A7():
    # 'SNG'!A7
    value = 33800
    isdatetime = True

@register(SNG)
class B7():
    # 'SNG'!B7
    value = 1992
    formula = "=YEAR(A7)"
    @eval_fn
    def B7():
        a7_1 = SNG.A7()
        var_1 = YEAR(a7_1)
        return var_1

@register(SNG)
class C7():
    # 'SNG'!C7
    value = 13.33
    formula = "=VLOOKUP(B7,$H:$I,2,FALSE)"
    @eval_fn
    def C7():
        b7_1 = SNG.B7()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b7_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H7():
    # 'SNG'!H7
    value = 1971

@register(SNG)
class I7():
    # 'SNG'!I7
    value = 0
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H7,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I7():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h7_1 = SNG.H7()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h7_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A8():
    # 'SNG'!A8
    value = 33831
    isdatetime = True

@register(SNG)
class B8():
    # 'SNG'!B8
    value = 1992
    formula = "=YEAR(A8)"
    @eval_fn
    def B8():
        a8_1 = SNG.A8()
        var_1 = YEAR(a8_1)
        return var_1

@register(SNG)
class C8():
    # 'SNG'!C8
    value = 13.33
    formula = "=VLOOKUP(B8,$H:$I,2,FALSE)"
    @eval_fn
    def C8():
        b8_1 = SNG.B8()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b8_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H8():
    # 'SNG'!H8
    value = 1972

@register(SNG)
class I8():
    # 'SNG'!I8
    value = 0
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H8,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I8():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h8_1 = SNG.H8()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h8_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A9():
    # 'SNG'!A9
    value = 33862
    isdatetime = True

@register(SNG)
class B9():
    # 'SNG'!B9
    value = 1992
    formula = "=YEAR(A9)"
    @eval_fn
    def B9():
        a9_1 = SNG.A9()
        var_1 = YEAR(a9_1)
        return var_1

@register(SNG)
class C9():
    # 'SNG'!C9
    value = 13.33
    formula = "=VLOOKUP(B9,$H:$I,2,FALSE)"
    @eval_fn
    def C9():
        b9_1 = SNG.B9()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b9_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H9():
    # 'SNG'!H9
    value = 1973

@register(SNG)
class I9():
    # 'SNG'!I9
    value = 0
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H9,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I9():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h9_1 = SNG.H9()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A10():
    # 'SNG'!A10
    value = 33892
    isdatetime = True

@register(SNG)
class B10():
    # 'SNG'!B10
    value = 1992
    formula = "=YEAR(A10)"
    @eval_fn
    def B10():
        a10_1 = SNG.A10()
        var_1 = YEAR(a10_1)
        return var_1

@register(SNG)
class C10():
    # 'SNG'!C10
    value = 13.33
    formula = "=VLOOKUP(B10,$H:$I,2,FALSE)"
    @eval_fn
    def C10():
        b10_1 = SNG.B10()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b10_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H10():
    # 'SNG'!H10
    value = 1974

@register(SNG)
class I10():
    # 'SNG'!I10
    value = 0
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H10,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I10():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h10_1 = SNG.H10()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h10_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A11():
    # 'SNG'!A11
    value = 33923
    isdatetime = True

@register(SNG)
class B11():
    # 'SNG'!B11
    value = 1992
    formula = "=YEAR(A11)"
    @eval_fn
    def B11():
        a11_1 = SNG.A11()
        var_1 = YEAR(a11_1)
        return var_1

@register(SNG)
class C11():
    # 'SNG'!C11
    value = 13.33
    formula = "=VLOOKUP(B11,$H:$I,2,FALSE)"
    @eval_fn
    def C11():
        b11_1 = SNG.B11()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b11_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H11():
    # 'SNG'!H11
    value = 1975

@register(SNG)
class I11():
    # 'SNG'!I11
    value = 0
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H11,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I11():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h11_1 = SNG.H11()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h11_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A12():
    # 'SNG'!A12
    value = 33953
    isdatetime = True

@register(SNG)
class B12():
    # 'SNG'!B12
    value = 1992
    formula = "=YEAR(A12)"
    @eval_fn
    def B12():
        a12_1 = SNG.A12()
        var_1 = YEAR(a12_1)
        return var_1

@register(SNG)
class C12():
    # 'SNG'!C12
    value = 13.33
    formula = "=VLOOKUP(B12,$H:$I,2,FALSE)"
    @eval_fn
    def C12():
        b12_1 = SNG.B12()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b12_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H12():
    # 'SNG'!H12
    value = 1976

@register(SNG)
class I12():
    # 'SNG'!I12
    value = 0
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H12,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I12():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h12_1 = SNG.H12()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h12_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A13():
    # 'SNG'!A13
    value = 33984
    isdatetime = True

@register(SNG)
class B13():
    # 'SNG'!B13
    value = 1993
    formula = "=YEAR(A13)"
    @eval_fn
    def B13():
        a13_1 = SNG.A13()
        var_1 = YEAR(a13_1)
        return var_1

@register(SNG)
class C13():
    # 'SNG'!C13
    value = 13.05
    formula = "=VLOOKUP(B13,$H:$I,2,FALSE)"
    @eval_fn
    def C13():
        b13_1 = SNG.B13()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b13_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H13():
    # 'SNG'!H13
    value = 1977

@register(SNG)
class I13():
    # 'SNG'!I13
    value = 0
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H13,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I13():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h13_1 = SNG.H13()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h13_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A14():
    # 'SNG'!A14
    value = 34015
    isdatetime = True

@register(SNG)
class B14():
    # 'SNG'!B14
    value = 1993
    formula = "=YEAR(A14)"
    @eval_fn
    def B14():
        a14_1 = SNG.A14()
        var_1 = YEAR(a14_1)
        return var_1

@register(SNG)
class C14():
    # 'SNG'!C14
    value = 13.05
    formula = "=VLOOKUP(B14,$H:$I,2,FALSE)"
    @eval_fn
    def C14():
        b14_1 = SNG.B14()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b14_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H14():
    # 'SNG'!H14
    value = 1978

@register(SNG)
class I14():
    # 'SNG'!I14
    value = 0
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H14,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I14():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h14_1 = SNG.H14()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h14_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A15():
    # 'SNG'!A15
    value = 34043
    isdatetime = True

@register(SNG)
class B15():
    # 'SNG'!B15
    value = 1993
    formula = "=YEAR(A15)"
    @eval_fn
    def B15():
        a15_1 = SNG.A15()
        var_1 = YEAR(a15_1)
        return var_1

@register(SNG)
class C15():
    # 'SNG'!C15
    value = 13.05
    formula = "=VLOOKUP(B15,$H:$I,2,FALSE)"
    @eval_fn
    def C15():
        b15_1 = SNG.B15()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b15_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H15():
    # 'SNG'!H15
    value = 1979

@register(SNG)
class I15():
    # 'SNG'!I15
    value = 0
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H15,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I15():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h15_1 = SNG.H15()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h15_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A16():
    # 'SNG'!A16
    value = 34074
    isdatetime = True

@register(SNG)
class B16():
    # 'SNG'!B16
    value = 1993
    formula = "=YEAR(A16)"
    @eval_fn
    def B16():
        a16_1 = SNG.A16()
        var_1 = YEAR(a16_1)
        return var_1

@register(SNG)
class C16():
    # 'SNG'!C16
    value = 13.05
    formula = "=VLOOKUP(B16,$H:$I,2,FALSE)"
    @eval_fn
    def C16():
        b16_1 = SNG.B16()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b16_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H16():
    # 'SNG'!H16
    value = 1980

@register(SNG)
class I16():
    # 'SNG'!I16
    value = 13.06
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H16,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I16():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h16_1 = SNG.H16()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h16_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A17():
    # 'SNG'!A17
    value = 34104
    isdatetime = True

@register(SNG)
class B17():
    # 'SNG'!B17
    value = 1993
    formula = "=YEAR(A17)"
    @eval_fn
    def B17():
        a17_1 = SNG.A17()
        var_1 = YEAR(a17_1)
        return var_1

@register(SNG)
class C17():
    # 'SNG'!C17
    value = 13.05
    formula = "=VLOOKUP(B17,$H:$I,2,FALSE)"
    @eval_fn
    def C17():
        b17_1 = SNG.B17()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b17_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H17():
    # 'SNG'!H17
    value = 1981

@register(SNG)
class I17():
    # 'SNG'!I17
    value = 15.76
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H17,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I17():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h17_1 = SNG.H17()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h17_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A18():
    # 'SNG'!A18
    value = 34135
    isdatetime = True

@register(SNG)
class B18():
    # 'SNG'!B18
    value = 1993
    formula = "=YEAR(A18)"
    @eval_fn
    def B18():
        a18_1 = SNG.A18()
        var_1 = YEAR(a18_1)
        return var_1

@register(SNG)
class C18():
    # 'SNG'!C18
    value = 13.05
    formula = "=VLOOKUP(B18,$H:$I,2,FALSE)"
    @eval_fn
    def C18():
        b18_1 = SNG.B18()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b18_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H18():
    # 'SNG'!H18
    value = 1982

@register(SNG)
class I18():
    # 'SNG'!I18
    value = 15.02
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H18,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I18():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h18_1 = SNG.H18()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h18_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A19():
    # 'SNG'!A19
    value = 34165
    isdatetime = True

@register(SNG)
class B19():
    # 'SNG'!B19
    value = 1993
    formula = "=YEAR(A19)"
    @eval_fn
    def B19():
        a19_1 = SNG.A19()
        var_1 = YEAR(a19_1)
        return var_1

@register(SNG)
class C19():
    # 'SNG'!C19
    value = 13.05
    formula = "=VLOOKUP(B19,$H:$I,2,FALSE)"
    @eval_fn
    def C19():
        b19_1 = SNG.B19()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b19_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H19():
    # 'SNG'!H19
    value = 1983

@register(SNG)
class I19():
    # 'SNG'!I19
    value = 15.1
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H19,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I19():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h19_1 = SNG.H19()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h19_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A20():
    # 'SNG'!A20
    value = 34196
    isdatetime = True

@register(SNG)
class B20():
    # 'SNG'!B20
    value = 1993
    formula = "=YEAR(A20)"
    @eval_fn
    def B20():
        a20_1 = SNG.A20()
        var_1 = YEAR(a20_1)
        return var_1

@register(SNG)
class C20():
    # 'SNG'!C20
    value = 13.05
    formula = "=VLOOKUP(B20,$H:$I,2,FALSE)"
    @eval_fn
    def C20():
        b20_1 = SNG.B20()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b20_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H20():
    # 'SNG'!H20
    value = 1984

@register(SNG)
class I20():
    # 'SNG'!I20
    value = 16.91
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H20,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I20():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h20_1 = SNG.H20()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h20_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A21():
    # 'SNG'!A21
    value = 34227
    isdatetime = True

@register(SNG)
class B21():
    # 'SNG'!B21
    value = 1993
    formula = "=YEAR(A21)"
    @eval_fn
    def B21():
        a21_1 = SNG.A21()
        var_1 = YEAR(a21_1)
        return var_1

@register(SNG)
class C21():
    # 'SNG'!C21
    value = 13.05
    formula = "=VLOOKUP(B21,$H:$I,2,FALSE)"
    @eval_fn
    def C21():
        b21_1 = SNG.B21()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b21_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H21():
    # 'SNG'!H21
    value = 1985

@register(SNG)
class I21():
    # 'SNG'!I21
    value = 14.2
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H21,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I21():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h21_1 = SNG.H21()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h21_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A22():
    # 'SNG'!A22
    value = 34257
    isdatetime = True

@register(SNG)
class B22():
    # 'SNG'!B22
    value = 1993
    formula = "=YEAR(A22)"
    @eval_fn
    def B22():
        a22_1 = SNG.A22()
        var_1 = YEAR(a22_1)
        return var_1

@register(SNG)
class C22():
    # 'SNG'!C22
    value = 13.05
    formula = "=VLOOKUP(B22,$H:$I,2,FALSE)"
    @eval_fn
    def C22():
        b22_1 = SNG.B22()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b22_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H22():
    # 'SNG'!H22
    value = 1986

@register(SNG)
class I22():
    # 'SNG'!I22
    value = 11.96
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H22,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I22():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h22_1 = SNG.H22()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h22_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A23():
    # 'SNG'!A23
    value = 34288
    isdatetime = True

@register(SNG)
class B23():
    # 'SNG'!B23
    value = 1993
    formula = "=YEAR(A23)"
    @eval_fn
    def B23():
        a23_1 = SNG.A23()
        var_1 = YEAR(a23_1)
        return var_1

@register(SNG)
class C23():
    # 'SNG'!C23
    value = 13.05
    formula = "=VLOOKUP(B23,$H:$I,2,FALSE)"
    @eval_fn
    def C23():
        b23_1 = SNG.B23()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b23_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H23():
    # 'SNG'!H23
    value = 1987

@register(SNG)
class I23():
    # 'SNG'!I23
    value = 11.89
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H23,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I23():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h23_1 = SNG.H23()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h23_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A24():
    # 'SNG'!A24
    value = 34318
    isdatetime = True

@register(SNG)
class B24():
    # 'SNG'!B24
    value = 1993
    formula = "=YEAR(A24)"
    @eval_fn
    def B24():
        a24_1 = SNG.A24()
        var_1 = YEAR(a24_1)
        return var_1

@register(SNG)
class C24():
    # 'SNG'!C24
    value = 13.05
    formula = "=VLOOKUP(B24,$H:$I,2,FALSE)"
    @eval_fn
    def C24():
        b24_1 = SNG.B24()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b24_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H24():
    # 'SNG'!H24
    value = 1988

@register(SNG)
class I24():
    # 'SNG'!I24
    value = 11.52
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H24,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I24():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h24_1 = SNG.H24()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h24_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A25():
    # 'SNG'!A25
    value = 34349
    isdatetime = True

@register(SNG)
class B25():
    # 'SNG'!B25
    value = 1994
    formula = "=YEAR(A25)"
    @eval_fn
    def B25():
        a25_1 = SNG.A25()
        var_1 = YEAR(a25_1)
        return var_1

@register(SNG)
class C25():
    # 'SNG'!C25
    value = 12.68
    formula = "=VLOOKUP(B25,$H:$I,2,FALSE)"
    @eval_fn
    def C25():
        b25_1 = SNG.B25()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b25_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H25():
    # 'SNG'!H25
    value = 1989

@register(SNG)
class I25():
    # 'SNG'!I25
    value = 11.41
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H25,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I25():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h25_1 = SNG.H25()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h25_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A26():
    # 'SNG'!A26
    value = 34380
    isdatetime = True

@register(SNG)
class B26():
    # 'SNG'!B26
    value = 1994
    formula = "=YEAR(A26)"
    @eval_fn
    def B26():
        a26_1 = SNG.A26()
        var_1 = YEAR(a26_1)
        return var_1

@register(SNG)
class C26():
    # 'SNG'!C26
    value = 12.68
    formula = "=VLOOKUP(B26,$H:$I,2,FALSE)"
    @eval_fn
    def C26():
        b26_1 = SNG.B26()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b26_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H26():
    # 'SNG'!H26
    value = 1990

@register(SNG)
class I26():
    # 'SNG'!I26
    value = 12.24
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H26,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I26():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h26_1 = SNG.H26()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h26_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A27():
    # 'SNG'!A27
    value = 34408
    isdatetime = True

@register(SNG)
class B27():
    # 'SNG'!B27
    value = 1994
    formula = "=YEAR(A27)"
    @eval_fn
    def B27():
        a27_1 = SNG.A27()
        var_1 = YEAR(a27_1)
        return var_1

@register(SNG)
class C27():
    # 'SNG'!C27
    value = 12.68
    formula = "=VLOOKUP(B27,$H:$I,2,FALSE)"
    @eval_fn
    def C27():
        b27_1 = SNG.B27()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b27_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H27():
    # 'SNG'!H27
    value = 1991

@register(SNG)
class I27():
    # 'SNG'!I27
    value = 14.16
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H27,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I27():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h27_1 = SNG.H27()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h27_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A28():
    # 'SNG'!A28
    value = 34439
    isdatetime = True

@register(SNG)
class B28():
    # 'SNG'!B28
    value = 1994
    formula = "=YEAR(A28)"
    @eval_fn
    def B28():
        a28_1 = SNG.A28()
        var_1 = YEAR(a28_1)
        return var_1

@register(SNG)
class C28():
    # 'SNG'!C28
    value = 12.68
    formula = "=VLOOKUP(B28,$H:$I,2,FALSE)"
    @eval_fn
    def C28():
        b28_1 = SNG.B28()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b28_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H28():
    # 'SNG'!H28
    value = 1992

@register(SNG)
class I28():
    # 'SNG'!I28
    value = 13.33
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H28,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I28():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h28_1 = SNG.H28()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h28_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A29():
    # 'SNG'!A29
    value = 34469
    isdatetime = True

@register(SNG)
class B29():
    # 'SNG'!B29
    value = 1994
    formula = "=YEAR(A29)"
    @eval_fn
    def B29():
        a29_1 = SNG.A29()
        var_1 = YEAR(a29_1)
        return var_1

@register(SNG)
class C29():
    # 'SNG'!C29
    value = 12.68
    formula = "=VLOOKUP(B29,$H:$I,2,FALSE)"
    @eval_fn
    def C29():
        b29_1 = SNG.B29()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b29_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H29():
    # 'SNG'!H29
    value = 1993

@register(SNG)
class I29():
    # 'SNG'!I29
    value = 13.05
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H29,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I29():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h29_1 = SNG.H29()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h29_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A30():
    # 'SNG'!A30
    value = 34500
    isdatetime = True

@register(SNG)
class B30():
    # 'SNG'!B30
    value = 1994
    formula = "=YEAR(A30)"
    @eval_fn
    def B30():
        a30_1 = SNG.A30()
        var_1 = YEAR(a30_1)
        return var_1

@register(SNG)
class C30():
    # 'SNG'!C30
    value = 12.68
    formula = "=VLOOKUP(B30,$H:$I,2,FALSE)"
    @eval_fn
    def C30():
        b30_1 = SNG.B30()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b30_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H30():
    # 'SNG'!H30
    value = 1994

@register(SNG)
class I30():
    # 'SNG'!I30
    value = 12.68
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H30,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I30():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h30_1 = SNG.H30()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h30_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A31():
    # 'SNG'!A31
    value = 34530
    isdatetime = True

@register(SNG)
class B31():
    # 'SNG'!B31
    value = 1994
    formula = "=YEAR(A31)"
    @eval_fn
    def B31():
        a31_1 = SNG.A31()
        var_1 = YEAR(a31_1)
        return var_1

@register(SNG)
class C31():
    # 'SNG'!C31
    value = 12.68
    formula = "=VLOOKUP(B31,$H:$I,2,FALSE)"
    @eval_fn
    def C31():
        b31_1 = SNG.B31()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b31_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H31():
    # 'SNG'!H31
    value = 1995

@register(SNG)
class I31():
    # 'SNG'!I31
    value = 13.3
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H31,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I31():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h31_1 = SNG.H31()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h31_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A32():
    # 'SNG'!A32
    value = 34561
    isdatetime = True

@register(SNG)
class B32():
    # 'SNG'!B32
    value = 1994
    formula = "=YEAR(A32)"
    @eval_fn
    def B32():
        a32_1 = SNG.A32()
        var_1 = YEAR(a32_1)
        return var_1

@register(SNG)
class C32():
    # 'SNG'!C32
    value = 12.68
    formula = "=VLOOKUP(B32,$H:$I,2,FALSE)"
    @eval_fn
    def C32():
        b32_1 = SNG.B32()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b32_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H32():
    # 'SNG'!H32
    value = 1996

@register(SNG)
class I32():
    # 'SNG'!I32
    value = 14.66
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H32,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I32():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h32_1 = SNG.H32()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h32_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A33():
    # 'SNG'!A33
    value = 34592
    isdatetime = True

@register(SNG)
class B33():
    # 'SNG'!B33
    value = 1994
    formula = "=YEAR(A33)"
    @eval_fn
    def B33():
        a33_1 = SNG.A33()
        var_1 = YEAR(a33_1)
        return var_1

@register(SNG)
class C33():
    # 'SNG'!C33
    value = 12.68
    formula = "=VLOOKUP(B33,$H:$I,2,FALSE)"
    @eval_fn
    def C33():
        b33_1 = SNG.B33()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b33_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H33():
    # 'SNG'!H33
    value = 1997

@register(SNG)
class I33():
    # 'SNG'!I33
    value = 15.88
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H33,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I33():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h33_1 = SNG.H33()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h33_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A34():
    # 'SNG'!A34
    value = 34622
    isdatetime = True

@register(SNG)
class B34():
    # 'SNG'!B34
    value = 1994
    formula = "=YEAR(A34)"
    @eval_fn
    def B34():
        a34_1 = SNG.A34()
        var_1 = YEAR(a34_1)
        return var_1

@register(SNG)
class C34():
    # 'SNG'!C34
    value = 12.68
    formula = "=VLOOKUP(B34,$H:$I,2,FALSE)"
    @eval_fn
    def C34():
        b34_1 = SNG.B34()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b34_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H34():
    # 'SNG'!H34
    value = 1998

@register(SNG)
class I34():
    # 'SNG'!I34
    value = 13.71
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H34,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I34():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h34_1 = SNG.H34()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h34_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A35():
    # 'SNG'!A35
    value = 34653
    isdatetime = True

@register(SNG)
class B35():
    # 'SNG'!B35
    value = 1994
    formula = "=YEAR(A35)"
    @eval_fn
    def B35():
        a35_1 = SNG.A35()
        var_1 = YEAR(a35_1)
        return var_1

@register(SNG)
class C35():
    # 'SNG'!C35
    value = 12.68
    formula = "=VLOOKUP(B35,$H:$I,2,FALSE)"
    @eval_fn
    def C35():
        b35_1 = SNG.B35()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b35_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H35():
    # 'SNG'!H35
    value = 1999

@register(SNG)
class I35():
    # 'SNG'!I35
    value = 13.54
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H35,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I35():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h35_1 = SNG.H35()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h35_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A36():
    # 'SNG'!A36
    value = 34683
    isdatetime = True

@register(SNG)
class B36():
    # 'SNG'!B36
    value = 1994
    formula = "=YEAR(A36)"
    @eval_fn
    def B36():
        a36_1 = SNG.A36()
        var_1 = YEAR(a36_1)
        return var_1

@register(SNG)
class C36():
    # 'SNG'!C36
    value = 12.68
    formula = "=VLOOKUP(B36,$H:$I,2,FALSE)"
    @eval_fn
    def C36():
        b36_1 = SNG.B36()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b36_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H36():
    # 'SNG'!H36
    value = 2000

@register(SNG)
class I36():
    # 'SNG'!I36
    value = 16.18
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H36,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I36():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h36_1 = SNG.H36()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h36_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A37():
    # 'SNG'!A37
    value = 34714
    isdatetime = True

@register(SNG)
class B37():
    # 'SNG'!B37
    value = 1995
    formula = "=YEAR(A37)"
    @eval_fn
    def B37():
        a37_1 = SNG.A37()
        var_1 = YEAR(a37_1)
        return var_1

@register(SNG)
class C37():
    # 'SNG'!C37
    value = 13.3
    formula = "=VLOOKUP(B37,$H:$I,2,FALSE)"
    @eval_fn
    def C37():
        b37_1 = SNG.B37()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b37_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H37():
    # 'SNG'!H37
    value = 2001

@register(SNG)
class I37():
    # 'SNG'!I37
    value = 16.85
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H37,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I37():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h37_1 = SNG.H37()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h37_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A38():
    # 'SNG'!A38
    value = 34745
    isdatetime = True

@register(SNG)
class B38():
    # 'SNG'!B38
    value = 1995
    formula = "=YEAR(A38)"
    @eval_fn
    def B38():
        a38_1 = SNG.A38()
        var_1 = YEAR(a38_1)
        return var_1

@register(SNG)
class C38():
    # 'SNG'!C38
    value = 13.3
    formula = "=VLOOKUP(B38,$H:$I,2,FALSE)"
    @eval_fn
    def C38():
        b38_1 = SNG.B38()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b38_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H38():
    # 'SNG'!H38
    value = 2002

@register(SNG)
class I38():
    # 'SNG'!I38
    value = 16.67
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H38,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I38():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h38_1 = SNG.H38()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h38_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A39():
    # 'SNG'!A39
    value = 34773
    isdatetime = True

@register(SNG)
class B39():
    # 'SNG'!B39
    value = 1995
    formula = "=YEAR(A39)"
    @eval_fn
    def B39():
        a39_1 = SNG.A39()
        var_1 = YEAR(a39_1)
        return var_1

@register(SNG)
class C39():
    # 'SNG'!C39
    value = 13.3
    formula = "=VLOOKUP(B39,$H:$I,2,FALSE)"
    @eval_fn
    def C39():
        b39_1 = SNG.B39()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b39_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H39():
    # 'SNG'!H39
    value = 2003

@register(SNG)
class I39():
    # 'SNG'!I39
    value = 19.03
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H39,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I39():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h39_1 = SNG.H39()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h39_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A40():
    # 'SNG'!A40
    value = 34804
    isdatetime = True

@register(SNG)
class B40():
    # 'SNG'!B40
    value = 1995
    formula = "=YEAR(A40)"
    @eval_fn
    def B40():
        a40_1 = SNG.A40()
        var_1 = YEAR(a40_1)
        return var_1

@register(SNG)
class C40():
    # 'SNG'!C40
    value = 13.3
    formula = "=VLOOKUP(B40,$H:$I,2,FALSE)"
    @eval_fn
    def C40():
        b40_1 = SNG.B40()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b40_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H40():
    # 'SNG'!H40
    value = 2004

@register(SNG)
class I40():
    # 'SNG'!I40
    value = 20.33
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H40,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I40():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h40_1 = SNG.H40()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h40_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A41():
    # 'SNG'!A41
    value = 34834
    isdatetime = True

@register(SNG)
class B41():
    # 'SNG'!B41
    value = 1995
    formula = "=YEAR(A41)"
    @eval_fn
    def B41():
        a41_1 = SNG.A41()
        var_1 = YEAR(a41_1)
        return var_1

@register(SNG)
class C41():
    # 'SNG'!C41
    value = 13.3
    formula = "=VLOOKUP(B41,$H:$I,2,FALSE)"
    @eval_fn
    def C41():
        b41_1 = SNG.B41()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b41_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H41():
    # 'SNG'!H41
    value = 2005

@register(SNG)
class I41():
    # 'SNG'!I41
    value = 24.3
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H41,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I41():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h41_1 = SNG.H41()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h41_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A42():
    # 'SNG'!A42
    value = 34865
    isdatetime = True

@register(SNG)
class B42():
    # 'SNG'!B42
    value = 1995
    formula = "=YEAR(A42)"
    @eval_fn
    def B42():
        a42_1 = SNG.A42()
        var_1 = YEAR(a42_1)
        return var_1

@register(SNG)
class C42():
    # 'SNG'!C42
    value = 13.3
    formula = "=VLOOKUP(B42,$H:$I,2,FALSE)"
    @eval_fn
    def C42():
        b42_1 = SNG.B42()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b42_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H42():
    # 'SNG'!H42
    value = 2006

@register(SNG)
class I42():
    # 'SNG'!I42
    value = 27.54
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H42,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I42():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h42_1 = SNG.H42()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h42_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A43():
    # 'SNG'!A43
    value = 34895
    isdatetime = True

@register(SNG)
class B43():
    # 'SNG'!B43
    value = 1995
    formula = "=YEAR(A43)"
    @eval_fn
    def B43():
        a43_1 = SNG.A43()
        var_1 = YEAR(a43_1)
        return var_1

@register(SNG)
class C43():
    # 'SNG'!C43
    value = 13.3
    formula = "=VLOOKUP(B43,$H:$I,2,FALSE)"
    @eval_fn
    def C43():
        b43_1 = SNG.B43()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b43_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H43():
    # 'SNG'!H43
    value = 2007

@register(SNG)
class I43():
    # 'SNG'!I43
    value = 26.83
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H43,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I43():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h43_1 = SNG.H43()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h43_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A44():
    # 'SNG'!A44
    value = 34926
    isdatetime = True

@register(SNG)
class B44():
    # 'SNG'!B44
    value = 1995
    formula = "=YEAR(A44)"
    @eval_fn
    def B44():
        a44_1 = SNG.A44()
        var_1 = YEAR(a44_1)
        return var_1

@register(SNG)
class C44():
    # 'SNG'!C44
    value = 13.3
    formula = "=VLOOKUP(B44,$H:$I,2,FALSE)"
    @eval_fn
    def C44():
        b44_1 = SNG.B44()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b44_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H44():
    # 'SNG'!H44
    value = 2008

@register(SNG)
class I44():
    # 'SNG'!I44
    value = 36.73
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H44,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I44():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h44_1 = SNG.H44()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h44_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A45():
    # 'SNG'!A45
    value = 34957
    isdatetime = True

@register(SNG)
class B45():
    # 'SNG'!B45
    value = 1995
    formula = "=YEAR(A45)"
    @eval_fn
    def B45():
        a45_1 = SNG.A45()
        var_1 = YEAR(a45_1)
        return var_1

@register(SNG)
class C45():
    # 'SNG'!C45
    value = 13.3
    formula = "=VLOOKUP(B45,$H:$I,2,FALSE)"
    @eval_fn
    def C45():
        b45_1 = SNG.B45()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b45_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H45():
    # 'SNG'!H45
    value = 2009

@register(SNG)
class I45():
    # 'SNG'!I45
    value = 28.82
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H45,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I45():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h45_1 = SNG.H45()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h45_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A46():
    # 'SNG'!A46
    value = 34987
    isdatetime = True

@register(SNG)
class B46():
    # 'SNG'!B46
    value = 1995
    formula = "=YEAR(A46)"
    @eval_fn
    def B46():
        a46_1 = SNG.A46()
        var_1 = YEAR(a46_1)
        return var_1

@register(SNG)
class C46():
    # 'SNG'!C46
    value = 13.3
    formula = "=VLOOKUP(B46,$H:$I,2,FALSE)"
    @eval_fn
    def C46():
        b46_1 = SNG.B46()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b46_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H46():
    # 'SNG'!H46
    value = 2010

@register(SNG)
class I46():
    # 'SNG'!I46
    value = 35.29
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H46,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I46():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h46_1 = SNG.H46()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h46_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A47():
    # 'SNG'!A47
    value = 35018
    isdatetime = True

@register(SNG)
class B47():
    # 'SNG'!B47
    value = 1995
    formula = "=YEAR(A47)"
    @eval_fn
    def B47():
        a47_1 = SNG.A47()
        var_1 = YEAR(a47_1)
        return var_1

@register(SNG)
class C47():
    # 'SNG'!C47
    value = 13.3
    formula = "=VLOOKUP(B47,$H:$I,2,FALSE)"
    @eval_fn
    def C47():
        b47_1 = SNG.B47()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b47_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H47():
    # 'SNG'!H47
    value = 2011

@register(SNG)
class I47():
    # 'SNG'!I47
    value = 43.43
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H47,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I47():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h47_1 = SNG.H47()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h47_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A48():
    # 'SNG'!A48
    value = 35048
    isdatetime = True

@register(SNG)
class B48():
    # 'SNG'!B48
    value = 1995
    formula = "=YEAR(A48)"
    @eval_fn
    def B48():
        a48_1 = SNG.A48()
        var_1 = YEAR(a48_1)
        return var_1

@register(SNG)
class C48():
    # 'SNG'!C48
    value = 13.3
    formula = "=VLOOKUP(B48,$H:$I,2,FALSE)"
    @eval_fn
    def C48():
        b48_1 = SNG.B48()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b48_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H48():
    # 'SNG'!H48
    value = 2012

@register(SNG)
class I48():
    # 'SNG'!I48
    value = 44.19
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H48,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I48():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h48_1 = SNG.H48()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h48_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A49():
    # 'SNG'!A49
    value = 35079
    isdatetime = True

@register(SNG)
class B49():
    # 'SNG'!B49
    value = 1996
    formula = "=YEAR(A49)"
    @eval_fn
    def B49():
        a49_1 = SNG.A49()
        var_1 = YEAR(a49_1)
        return var_1

@register(SNG)
class C49():
    # 'SNG'!C49
    value = 14.66
    formula = "=VLOOKUP(B49,$H:$I,2,FALSE)"
    @eval_fn
    def C49():
        b49_1 = SNG.B49()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b49_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H49():
    # 'SNG'!H49
    value = 2013

@register(SNG)
class I49():
    # 'SNG'!I49
    value = 41.19
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H49,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I49():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h49_1 = SNG.H49()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h49_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A50():
    # 'SNG'!A50
    value = 35110
    isdatetime = True

@register(SNG)
class B50():
    # 'SNG'!B50
    value = 1996
    formula = "=YEAR(A50)"
    @eval_fn
    def B50():
        a50_1 = SNG.A50()
        var_1 = YEAR(a50_1)
        return var_1

@register(SNG)
class C50():
    # 'SNG'!C50
    value = 14.66
    formula = "=VLOOKUP(B50,$H:$I,2,FALSE)"
    @eval_fn
    def C50():
        b50_1 = SNG.B50()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b50_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H50():
    # 'SNG'!H50
    value = 2014

@register(SNG)
class I50():
    # 'SNG'!I50
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H50,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I50():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h50_1 = SNG.H50()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h50_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A51():
    # 'SNG'!A51
    value = 35139
    isdatetime = True

@register(SNG)
class B51():
    # 'SNG'!B51
    value = 1996
    formula = "=YEAR(A51)"
    @eval_fn
    def B51():
        a51_1 = SNG.A51()
        var_1 = YEAR(a51_1)
        return var_1

@register(SNG)
class C51():
    # 'SNG'!C51
    value = 14.66
    formula = "=VLOOKUP(B51,$H:$I,2,FALSE)"
    @eval_fn
    def C51():
        b51_1 = SNG.B51()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b51_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H51():
    # 'SNG'!H51
    value = 2015

@register(SNG)
class I51():
    # 'SNG'!I51
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H51,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I51():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h51_1 = SNG.H51()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h51_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A52():
    # 'SNG'!A52
    value = 35170
    isdatetime = True

@register(SNG)
class B52():
    # 'SNG'!B52
    value = 1996
    formula = "=YEAR(A52)"
    @eval_fn
    def B52():
        a52_1 = SNG.A52()
        var_1 = YEAR(a52_1)
        return var_1

@register(SNG)
class C52():
    # 'SNG'!C52
    value = 14.66
    formula = "=VLOOKUP(B52,$H:$I,2,FALSE)"
    @eval_fn
    def C52():
        b52_1 = SNG.B52()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b52_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H52():
    # 'SNG'!H52
    value = 2016

@register(SNG)
class I52():
    # 'SNG'!I52
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H52,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I52():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h52_1 = SNG.H52()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h52_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A53():
    # 'SNG'!A53
    value = 35200
    isdatetime = True

@register(SNG)
class B53():
    # 'SNG'!B53
    value = 1996
    formula = "=YEAR(A53)"
    @eval_fn
    def B53():
        a53_1 = SNG.A53()
        var_1 = YEAR(a53_1)
        return var_1

@register(SNG)
class C53():
    # 'SNG'!C53
    value = 14.66
    formula = "=VLOOKUP(B53,$H:$I,2,FALSE)"
    @eval_fn
    def C53():
        b53_1 = SNG.B53()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b53_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H53():
    # 'SNG'!H53
    value = 2017

@register(SNG)
class I53():
    # 'SNG'!I53
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H53,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I53():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h53_1 = SNG.H53()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h53_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A54():
    # 'SNG'!A54
    value = 35231
    isdatetime = True

@register(SNG)
class B54():
    # 'SNG'!B54
    value = 1996
    formula = "=YEAR(A54)"
    @eval_fn
    def B54():
        a54_1 = SNG.A54()
        var_1 = YEAR(a54_1)
        return var_1

@register(SNG)
class C54():
    # 'SNG'!C54
    value = 14.66
    formula = "=VLOOKUP(B54,$H:$I,2,FALSE)"
    @eval_fn
    def C54():
        b54_1 = SNG.B54()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b54_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H54():
    # 'SNG'!H54
    value = 2018

@register(SNG)
class I54():
    # 'SNG'!I54
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H54,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I54():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h54_1 = SNG.H54()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h54_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A55():
    # 'SNG'!A55
    value = 35261
    isdatetime = True

@register(SNG)
class B55():
    # 'SNG'!B55
    value = 1996
    formula = "=YEAR(A55)"
    @eval_fn
    def B55():
        a55_1 = SNG.A55()
        var_1 = YEAR(a55_1)
        return var_1

@register(SNG)
class C55():
    # 'SNG'!C55
    value = 14.66
    formula = "=VLOOKUP(B55,$H:$I,2,FALSE)"
    @eval_fn
    def C55():
        b55_1 = SNG.B55()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b55_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H55():
    # 'SNG'!H55
    value = 2019

@register(SNG)
class I55():
    # 'SNG'!I55
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H55,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I55():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h55_1 = SNG.H55()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h55_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A56():
    # 'SNG'!A56
    value = 35292
    isdatetime = True

@register(SNG)
class B56():
    # 'SNG'!B56
    value = 1996
    formula = "=YEAR(A56)"
    @eval_fn
    def B56():
        a56_1 = SNG.A56()
        var_1 = YEAR(a56_1)
        return var_1

@register(SNG)
class C56():
    # 'SNG'!C56
    value = 14.66
    formula = "=VLOOKUP(B56,$H:$I,2,FALSE)"
    @eval_fn
    def C56():
        b56_1 = SNG.B56()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b56_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H56():
    # 'SNG'!H56
    value = 2020

@register(SNG)
class I56():
    # 'SNG'!I56
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H56,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I56():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h56_1 = SNG.H56()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h56_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A57():
    # 'SNG'!A57
    value = 35323
    isdatetime = True

@register(SNG)
class B57():
    # 'SNG'!B57
    value = 1996
    formula = "=YEAR(A57)"
    @eval_fn
    def B57():
        a57_1 = SNG.A57()
        var_1 = YEAR(a57_1)
        return var_1

@register(SNG)
class C57():
    # 'SNG'!C57
    value = 14.66
    formula = "=VLOOKUP(B57,$H:$I,2,FALSE)"
    @eval_fn
    def C57():
        b57_1 = SNG.B57()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b57_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H57():
    # 'SNG'!H57
    value = 2021

@register(SNG)
class I57():
    # 'SNG'!I57
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H57,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I57():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h57_1 = SNG.H57()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h57_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A58():
    # 'SNG'!A58
    value = 35353
    isdatetime = True

@register(SNG)
class B58():
    # 'SNG'!B58
    value = 1996
    formula = "=YEAR(A58)"
    @eval_fn
    def B58():
        a58_1 = SNG.A58()
        var_1 = YEAR(a58_1)
        return var_1

@register(SNG)
class C58():
    # 'SNG'!C58
    value = 14.66
    formula = "=VLOOKUP(B58,$H:$I,2,FALSE)"
    @eval_fn
    def C58():
        b58_1 = SNG.B58()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b58_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H58():
    # 'SNG'!H58
    value = 2022

@register(SNG)
class I58():
    # 'SNG'!I58
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H58,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I58():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h58_1 = SNG.H58()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h58_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A59():
    # 'SNG'!A59
    value = 35384
    isdatetime = True

@register(SNG)
class B59():
    # 'SNG'!B59
    value = 1996
    formula = "=YEAR(A59)"
    @eval_fn
    def B59():
        a59_1 = SNG.A59()
        var_1 = YEAR(a59_1)
        return var_1

@register(SNG)
class C59():
    # 'SNG'!C59
    value = 14.66
    formula = "=VLOOKUP(B59,$H:$I,2,FALSE)"
    @eval_fn
    def C59():
        b59_1 = SNG.B59()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b59_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H59():
    # 'SNG'!H59
    value = 2023

@register(SNG)
class I59():
    # 'SNG'!I59
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H59,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I59():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h59_1 = SNG.H59()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h59_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A60():
    # 'SNG'!A60
    value = 35414
    isdatetime = True

@register(SNG)
class B60():
    # 'SNG'!B60
    value = 1996
    formula = "=YEAR(A60)"
    @eval_fn
    def B60():
        a60_1 = SNG.A60()
        var_1 = YEAR(a60_1)
        return var_1

@register(SNG)
class C60():
    # 'SNG'!C60
    value = 14.66
    formula = "=VLOOKUP(B60,$H:$I,2,FALSE)"
    @eval_fn
    def C60():
        b60_1 = SNG.B60()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b60_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H60():
    # 'SNG'!H60
    value = 2024

@register(SNG)
class I60():
    # 'SNG'!I60
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H60,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I60():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h60_1 = SNG.H60()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A61():
    # 'SNG'!A61
    value = 35445
    isdatetime = True

@register(SNG)
class B61():
    # 'SNG'!B61
    value = 1997
    formula = "=YEAR(A61)"
    @eval_fn
    def B61():
        a61_1 = SNG.A61()
        var_1 = YEAR(a61_1)
        return var_1

@register(SNG)
class C61():
    # 'SNG'!C61
    value = 15.88
    formula = "=VLOOKUP(B61,$H:$I,2,FALSE)"
    @eval_fn
    def C61():
        b61_1 = SNG.B61()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b61_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H61():
    # 'SNG'!H61
    value = 2025

@register(SNG)
class I61():
    # 'SNG'!I61
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H61,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I61():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h61_1 = SNG.H61()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h61_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A62():
    # 'SNG'!A62
    value = 35476
    isdatetime = True

@register(SNG)
class B62():
    # 'SNG'!B62
    value = 1997
    formula = "=YEAR(A62)"
    @eval_fn
    def B62():
        a62_1 = SNG.A62()
        var_1 = YEAR(a62_1)
        return var_1

@register(SNG)
class C62():
    # 'SNG'!C62
    value = 15.88
    formula = "=VLOOKUP(B62,$H:$I,2,FALSE)"
    @eval_fn
    def C62():
        b62_1 = SNG.B62()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b62_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H62():
    # 'SNG'!H62
    value = 2026

@register(SNG)
class I62():
    # 'SNG'!I62
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H62,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I62():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h62_1 = SNG.H62()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h62_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A63():
    # 'SNG'!A63
    value = 35504
    isdatetime = True

@register(SNG)
class B63():
    # 'SNG'!B63
    value = 1997
    formula = "=YEAR(A63)"
    @eval_fn
    def B63():
        a63_1 = SNG.A63()
        var_1 = YEAR(a63_1)
        return var_1

@register(SNG)
class C63():
    # 'SNG'!C63
    value = 15.88
    formula = "=VLOOKUP(B63,$H:$I,2,FALSE)"
    @eval_fn
    def C63():
        b63_1 = SNG.B63()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b63_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H63():
    # 'SNG'!H63
    value = 2027

@register(SNG)
class I63():
    # 'SNG'!I63
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H63,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I63():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h63_1 = SNG.H63()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h63_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A64():
    # 'SNG'!A64
    value = 35535
    isdatetime = True

@register(SNG)
class B64():
    # 'SNG'!B64
    value = 1997
    formula = "=YEAR(A64)"
    @eval_fn
    def B64():
        a64_1 = SNG.A64()
        var_1 = YEAR(a64_1)
        return var_1

@register(SNG)
class C64():
    # 'SNG'!C64
    value = 15.88
    formula = "=VLOOKUP(B64,$H:$I,2,FALSE)"
    @eval_fn
    def C64():
        b64_1 = SNG.B64()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b64_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H64():
    # 'SNG'!H64
    value = 2028

@register(SNG)
class I64():
    # 'SNG'!I64
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H64,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I64():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h64_1 = SNG.H64()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h64_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A65():
    # 'SNG'!A65
    value = 35565
    isdatetime = True

@register(SNG)
class B65():
    # 'SNG'!B65
    value = 1997
    formula = "=YEAR(A65)"
    @eval_fn
    def B65():
        a65_1 = SNG.A65()
        var_1 = YEAR(a65_1)
        return var_1

@register(SNG)
class C65():
    # 'SNG'!C65
    value = 15.88
    formula = "=VLOOKUP(B65,$H:$I,2,FALSE)"
    @eval_fn
    def C65():
        b65_1 = SNG.B65()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b65_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H65():
    # 'SNG'!H65
    value = 2029

@register(SNG)
class I65():
    # 'SNG'!I65
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H65,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I65():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h65_1 = SNG.H65()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h65_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A66():
    # 'SNG'!A66
    value = 35596
    isdatetime = True

@register(SNG)
class B66():
    # 'SNG'!B66
    value = 1997
    formula = "=YEAR(A66)"
    @eval_fn
    def B66():
        a66_1 = SNG.A66()
        var_1 = YEAR(a66_1)
        return var_1

@register(SNG)
class C66():
    # 'SNG'!C66
    value = 15.88
    formula = "=VLOOKUP(B66,$H:$I,2,FALSE)"
    @eval_fn
    def C66():
        b66_1 = SNG.B66()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b66_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H66():
    # 'SNG'!H66
    value = 2030

@register(SNG)
class I66():
    # 'SNG'!I66
    value = "#N/A"
    formula = "=INDEX('EIA Expenditures'!$A:$EH,MATCH(SNG!$I$3,'EIA Expenditures'!$C:$C,0),MATCH(SNG!H66,'EIA Expenditures'!$2:$2,0))"
    @eval_fn
    def I66():
        range_1 = EIA_Expenditures(1, 0, 138, 0)
        i3_1 = SNG.I3()
        range_2 = EIA_Expenditures(3, 0, 3, 0)
        var_1 = MATCH(i3_1, range_2, 0)
        h66_1 = SNG.H66()
        range_3 = EIA_Expenditures(0, 2, 0, 2)
        var_2 = MATCH(h66_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(SNG)
class A67():
    # 'SNG'!A67
    value = 35626
    isdatetime = True

@register(SNG)
class B67():
    # 'SNG'!B67
    value = 1997
    formula = "=YEAR(A67)"
    @eval_fn
    def B67():
        a67_1 = SNG.A67()
        var_1 = YEAR(a67_1)
        return var_1

@register(SNG)
class C67():
    # 'SNG'!C67
    value = 15.88
    formula = "=VLOOKUP(B67,$H:$I,2,FALSE)"
    @eval_fn
    def C67():
        b67_1 = SNG.B67()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b67_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A68():
    # 'SNG'!A68
    value = 35657
    isdatetime = True

@register(SNG)
class B68():
    # 'SNG'!B68
    value = 1997
    formula = "=YEAR(A68)"
    @eval_fn
    def B68():
        a68_1 = SNG.A68()
        var_1 = YEAR(a68_1)
        return var_1

@register(SNG)
class C68():
    # 'SNG'!C68
    value = 15.88
    formula = "=VLOOKUP(B68,$H:$I,2,FALSE)"
    @eval_fn
    def C68():
        b68_1 = SNG.B68()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b68_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A69():
    # 'SNG'!A69
    value = 35688
    isdatetime = True

@register(SNG)
class B69():
    # 'SNG'!B69
    value = 1997
    formula = "=YEAR(A69)"
    @eval_fn
    def B69():
        a69_1 = SNG.A69()
        var_1 = YEAR(a69_1)
        return var_1

@register(SNG)
class C69():
    # 'SNG'!C69
    value = 15.88
    formula = "=VLOOKUP(B69,$H:$I,2,FALSE)"
    @eval_fn
    def C69():
        b69_1 = SNG.B69()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b69_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A70():
    # 'SNG'!A70
    value = 35718
    isdatetime = True

@register(SNG)
class B70():
    # 'SNG'!B70
    value = 1997
    formula = "=YEAR(A70)"
    @eval_fn
    def B70():
        a70_1 = SNG.A70()
        var_1 = YEAR(a70_1)
        return var_1

@register(SNG)
class C70():
    # 'SNG'!C70
    value = 15.88
    formula = "=VLOOKUP(B70,$H:$I,2,FALSE)"
    @eval_fn
    def C70():
        b70_1 = SNG.B70()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b70_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A71():
    # 'SNG'!A71
    value = 35749
    isdatetime = True

@register(SNG)
class B71():
    # 'SNG'!B71
    value = 1997
    formula = "=YEAR(A71)"
    @eval_fn
    def B71():
        a71_1 = SNG.A71()
        var_1 = YEAR(a71_1)
        return var_1

@register(SNG)
class C71():
    # 'SNG'!C71
    value = 15.88
    formula = "=VLOOKUP(B71,$H:$I,2,FALSE)"
    @eval_fn
    def C71():
        b71_1 = SNG.B71()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b71_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A72():
    # 'SNG'!A72
    value = 35779
    isdatetime = True

@register(SNG)
class B72():
    # 'SNG'!B72
    value = 1997
    formula = "=YEAR(A72)"
    @eval_fn
    def B72():
        a72_1 = SNG.A72()
        var_1 = YEAR(a72_1)
        return var_1

@register(SNG)
class C72():
    # 'SNG'!C72
    value = 15.88
    formula = "=VLOOKUP(B72,$H:$I,2,FALSE)"
    @eval_fn
    def C72():
        b72_1 = SNG.B72()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b72_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A73():
    # 'SNG'!A73
    value = 35810
    isdatetime = True

@register(SNG)
class B73():
    # 'SNG'!B73
    value = 1998
    formula = "=YEAR(A73)"
    @eval_fn
    def B73():
        a73_1 = SNG.A73()
        var_1 = YEAR(a73_1)
        return var_1

@register(SNG)
class C73():
    # 'SNG'!C73
    value = 13.71
    formula = "=VLOOKUP(B73,$H:$I,2,FALSE)"
    @eval_fn
    def C73():
        b73_1 = SNG.B73()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b73_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A74():
    # 'SNG'!A74
    value = 35841
    isdatetime = True

@register(SNG)
class B74():
    # 'SNG'!B74
    value = 1998
    formula = "=YEAR(A74)"
    @eval_fn
    def B74():
        a74_1 = SNG.A74()
        var_1 = YEAR(a74_1)
        return var_1

@register(SNG)
class C74():
    # 'SNG'!C74
    value = 13.71
    formula = "=VLOOKUP(B74,$H:$I,2,FALSE)"
    @eval_fn
    def C74():
        b74_1 = SNG.B74()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b74_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A75():
    # 'SNG'!A75
    value = 35869
    isdatetime = True

@register(SNG)
class B75():
    # 'SNG'!B75
    value = 1998
    formula = "=YEAR(A75)"
    @eval_fn
    def B75():
        a75_1 = SNG.A75()
        var_1 = YEAR(a75_1)
        return var_1

@register(SNG)
class C75():
    # 'SNG'!C75
    value = 13.71
    formula = "=VLOOKUP(B75,$H:$I,2,FALSE)"
    @eval_fn
    def C75():
        b75_1 = SNG.B75()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b75_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A76():
    # 'SNG'!A76
    value = 35900
    isdatetime = True

@register(SNG)
class B76():
    # 'SNG'!B76
    value = 1998
    formula = "=YEAR(A76)"
    @eval_fn
    def B76():
        a76_1 = SNG.A76()
        var_1 = YEAR(a76_1)
        return var_1

@register(SNG)
class C76():
    # 'SNG'!C76
    value = 13.71
    formula = "=VLOOKUP(B76,$H:$I,2,FALSE)"
    @eval_fn
    def C76():
        b76_1 = SNG.B76()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b76_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A77():
    # 'SNG'!A77
    value = 35930
    isdatetime = True

@register(SNG)
class B77():
    # 'SNG'!B77
    value = 1998
    formula = "=YEAR(A77)"
    @eval_fn
    def B77():
        a77_1 = SNG.A77()
        var_1 = YEAR(a77_1)
        return var_1

@register(SNG)
class C77():
    # 'SNG'!C77
    value = 13.71
    formula = "=VLOOKUP(B77,$H:$I,2,FALSE)"
    @eval_fn
    def C77():
        b77_1 = SNG.B77()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b77_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H77():
    # 'SNG'!H77
    value = "Conversion Factors (Unit Conversions Tab)"

@register(SNG)
class A78():
    # 'SNG'!A78
    value = 35961
    isdatetime = True

@register(SNG)
class B78():
    # 'SNG'!B78
    value = 1998
    formula = "=YEAR(A78)"
    @eval_fn
    def B78():
        a78_1 = SNG.A78()
        var_1 = YEAR(a78_1)
        return var_1

@register(SNG)
class C78():
    # 'SNG'!C78
    value = 13.71
    formula = "=VLOOKUP(B78,$H:$I,2,FALSE)"
    @eval_fn
    def C78():
        b78_1 = SNG.B78()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b78_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class H78():
    # 'SNG'!H78
    value = "    Liquefied petroleum gases"

@register(SNG)
class I78():
    # 'SNG'!I78
    value = "million Btu per Gallon"

@register(SNG)
class J78():
    # 'SNG'!J78
    value = 0.0846904761905
    formula = "='Unit Conversions'!D12"
    @eval_fn
    def J78():
        d12_1 = Unit_Conversions.D12()
        return d12_1

@register(SNG)
class K78():
    # 'SNG'!K78
    value = "million Btu per barrel"

@register(SNG)
class L78():
    # 'SNG'!L78
    value = 3.557
    formula = "='Unit Conversions'!F12"
    @eval_fn
    def L78():
        f12_1 = Unit_Conversions.F12()
        return f12_1

@register(SNG)
class A79():
    # 'SNG'!A79
    value = 35991
    isdatetime = True

@register(SNG)
class B79():
    # 'SNG'!B79
    value = 1998
    formula = "=YEAR(A79)"
    @eval_fn
    def B79():
        a79_1 = SNG.A79()
        var_1 = YEAR(a79_1)
        return var_1

@register(SNG)
class C79():
    # 'SNG'!C79
    value = 13.71
    formula = "=VLOOKUP(B79,$H:$I,2,FALSE)"
    @eval_fn
    def C79():
        b79_1 = SNG.B79()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b79_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A80():
    # 'SNG'!A80
    value = 36022
    isdatetime = True

@register(SNG)
class B80():
    # 'SNG'!B80
    value = 1998
    formula = "=YEAR(A80)"
    @eval_fn
    def B80():
        a80_1 = SNG.A80()
        var_1 = YEAR(a80_1)
        return var_1

@register(SNG)
class C80():
    # 'SNG'!C80
    value = 13.71
    formula = "=VLOOKUP(B80,$H:$I,2,FALSE)"
    @eval_fn
    def C80():
        b80_1 = SNG.B80()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b80_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A81():
    # 'SNG'!A81
    value = 36053
    isdatetime = True

@register(SNG)
class B81():
    # 'SNG'!B81
    value = 1998
    formula = "=YEAR(A81)"
    @eval_fn
    def B81():
        a81_1 = SNG.A81()
        var_1 = YEAR(a81_1)
        return var_1

@register(SNG)
class C81():
    # 'SNG'!C81
    value = 13.71
    formula = "=VLOOKUP(B81,$H:$I,2,FALSE)"
    @eval_fn
    def C81():
        b81_1 = SNG.B81()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b81_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A82():
    # 'SNG'!A82
    value = 36083
    isdatetime = True

@register(SNG)
class B82():
    # 'SNG'!B82
    value = 1998
    formula = "=YEAR(A82)"
    @eval_fn
    def B82():
        a82_1 = SNG.A82()
        var_1 = YEAR(a82_1)
        return var_1

@register(SNG)
class C82():
    # 'SNG'!C82
    value = 13.71
    formula = "=VLOOKUP(B82,$H:$I,2,FALSE)"
    @eval_fn
    def C82():
        b82_1 = SNG.B82()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b82_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A83():
    # 'SNG'!A83
    value = 36114
    isdatetime = True

@register(SNG)
class B83():
    # 'SNG'!B83
    value = 1998
    formula = "=YEAR(A83)"
    @eval_fn
    def B83():
        a83_1 = SNG.A83()
        var_1 = YEAR(a83_1)
        return var_1

@register(SNG)
class C83():
    # 'SNG'!C83
    value = 13.71
    formula = "=VLOOKUP(B83,$H:$I,2,FALSE)"
    @eval_fn
    def C83():
        b83_1 = SNG.B83()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b83_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A84():
    # 'SNG'!A84
    value = 36144
    isdatetime = True

@register(SNG)
class B84():
    # 'SNG'!B84
    value = 1998
    formula = "=YEAR(A84)"
    @eval_fn
    def B84():
        a84_1 = SNG.A84()
        var_1 = YEAR(a84_1)
        return var_1

@register(SNG)
class C84():
    # 'SNG'!C84
    value = 13.71
    formula = "=VLOOKUP(B84,$H:$I,2,FALSE)"
    @eval_fn
    def C84():
        b84_1 = SNG.B84()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b84_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A85():
    # 'SNG'!A85
    value = 36175
    isdatetime = True

@register(SNG)
class B85():
    # 'SNG'!B85
    value = 1999
    formula = "=YEAR(A85)"
    @eval_fn
    def B85():
        a85_1 = SNG.A85()
        var_1 = YEAR(a85_1)
        return var_1

@register(SNG)
class C85():
    # 'SNG'!C85
    value = 13.54
    formula = "=VLOOKUP(B85,$H:$I,2,FALSE)"
    @eval_fn
    def C85():
        b85_1 = SNG.B85()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b85_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A86():
    # 'SNG'!A86
    value = 36206
    isdatetime = True

@register(SNG)
class B86():
    # 'SNG'!B86
    value = 1999
    formula = "=YEAR(A86)"
    @eval_fn
    def B86():
        a86_1 = SNG.A86()
        var_1 = YEAR(a86_1)
        return var_1

@register(SNG)
class C86():
    # 'SNG'!C86
    value = 13.54
    formula = "=VLOOKUP(B86,$H:$I,2,FALSE)"
    @eval_fn
    def C86():
        b86_1 = SNG.B86()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b86_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A87():
    # 'SNG'!A87
    value = 36234
    isdatetime = True

@register(SNG)
class B87():
    # 'SNG'!B87
    value = 1999
    formula = "=YEAR(A87)"
    @eval_fn
    def B87():
        a87_1 = SNG.A87()
        var_1 = YEAR(a87_1)
        return var_1

@register(SNG)
class C87():
    # 'SNG'!C87
    value = 13.54
    formula = "=VLOOKUP(B87,$H:$I,2,FALSE)"
    @eval_fn
    def C87():
        b87_1 = SNG.B87()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b87_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A88():
    # 'SNG'!A88
    value = 36265
    isdatetime = True

@register(SNG)
class B88():
    # 'SNG'!B88
    value = 1999
    formula = "=YEAR(A88)"
    @eval_fn
    def B88():
        a88_1 = SNG.A88()
        var_1 = YEAR(a88_1)
        return var_1

@register(SNG)
class C88():
    # 'SNG'!C88
    value = 13.54
    formula = "=VLOOKUP(B88,$H:$I,2,FALSE)"
    @eval_fn
    def C88():
        b88_1 = SNG.B88()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b88_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A89():
    # 'SNG'!A89
    value = 36295
    isdatetime = True

@register(SNG)
class B89():
    # 'SNG'!B89
    value = 1999
    formula = "=YEAR(A89)"
    @eval_fn
    def B89():
        a89_1 = SNG.A89()
        var_1 = YEAR(a89_1)
        return var_1

@register(SNG)
class C89():
    # 'SNG'!C89
    value = 13.54
    formula = "=VLOOKUP(B89,$H:$I,2,FALSE)"
    @eval_fn
    def C89():
        b89_1 = SNG.B89()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b89_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A90():
    # 'SNG'!A90
    value = 36326
    isdatetime = True

@register(SNG)
class B90():
    # 'SNG'!B90
    value = 1999
    formula = "=YEAR(A90)"
    @eval_fn
    def B90():
        a90_1 = SNG.A90()
        var_1 = YEAR(a90_1)
        return var_1

@register(SNG)
class C90():
    # 'SNG'!C90
    value = 13.54
    formula = "=VLOOKUP(B90,$H:$I,2,FALSE)"
    @eval_fn
    def C90():
        b90_1 = SNG.B90()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b90_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A91():
    # 'SNG'!A91
    value = 36356
    isdatetime = True

@register(SNG)
class B91():
    # 'SNG'!B91
    value = 1999
    formula = "=YEAR(A91)"
    @eval_fn
    def B91():
        a91_1 = SNG.A91()
        var_1 = YEAR(a91_1)
        return var_1

@register(SNG)
class C91():
    # 'SNG'!C91
    value = 13.54
    formula = "=VLOOKUP(B91,$H:$I,2,FALSE)"
    @eval_fn
    def C91():
        b91_1 = SNG.B91()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b91_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A92():
    # 'SNG'!A92
    value = 36387
    isdatetime = True

@register(SNG)
class B92():
    # 'SNG'!B92
    value = 1999
    formula = "=YEAR(A92)"
    @eval_fn
    def B92():
        a92_1 = SNG.A92()
        var_1 = YEAR(a92_1)
        return var_1

@register(SNG)
class C92():
    # 'SNG'!C92
    value = 13.54
    formula = "=VLOOKUP(B92,$H:$I,2,FALSE)"
    @eval_fn
    def C92():
        b92_1 = SNG.B92()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b92_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A93():
    # 'SNG'!A93
    value = 36418
    isdatetime = True

@register(SNG)
class B93():
    # 'SNG'!B93
    value = 1999
    formula = "=YEAR(A93)"
    @eval_fn
    def B93():
        a93_1 = SNG.A93()
        var_1 = YEAR(a93_1)
        return var_1

@register(SNG)
class C93():
    # 'SNG'!C93
    value = 13.54
    formula = "=VLOOKUP(B93,$H:$I,2,FALSE)"
    @eval_fn
    def C93():
        b93_1 = SNG.B93()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b93_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A94():
    # 'SNG'!A94
    value = 36448
    isdatetime = True

@register(SNG)
class B94():
    # 'SNG'!B94
    value = 1999
    formula = "=YEAR(A94)"
    @eval_fn
    def B94():
        a94_1 = SNG.A94()
        var_1 = YEAR(a94_1)
        return var_1

@register(SNG)
class C94():
    # 'SNG'!C94
    value = 13.54
    formula = "=VLOOKUP(B94,$H:$I,2,FALSE)"
    @eval_fn
    def C94():
        b94_1 = SNG.B94()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b94_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A95():
    # 'SNG'!A95
    value = 36479
    isdatetime = True

@register(SNG)
class B95():
    # 'SNG'!B95
    value = 1999
    formula = "=YEAR(A95)"
    @eval_fn
    def B95():
        a95_1 = SNG.A95()
        var_1 = YEAR(a95_1)
        return var_1

@register(SNG)
class C95():
    # 'SNG'!C95
    value = 13.54
    formula = "=VLOOKUP(B95,$H:$I,2,FALSE)"
    @eval_fn
    def C95():
        b95_1 = SNG.B95()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b95_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A96():
    # 'SNG'!A96
    value = 36509
    isdatetime = True

@register(SNG)
class B96():
    # 'SNG'!B96
    value = 1999
    formula = "=YEAR(A96)"
    @eval_fn
    def B96():
        a96_1 = SNG.A96()
        var_1 = YEAR(a96_1)
        return var_1

@register(SNG)
class C96():
    # 'SNG'!C96
    value = 13.54
    formula = "=VLOOKUP(B96,$H:$I,2,FALSE)"
    @eval_fn
    def C96():
        b96_1 = SNG.B96()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b96_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A97():
    # 'SNG'!A97
    value = 36540
    isdatetime = True

@register(SNG)
class B97():
    # 'SNG'!B97
    value = 2000
    formula = "=YEAR(A97)"
    @eval_fn
    def B97():
        a97_1 = SNG.A97()
        var_1 = YEAR(a97_1)
        return var_1

@register(SNG)
class C97():
    # 'SNG'!C97
    value = 16.18
    formula = "=VLOOKUP(B97,$H:$I,2,FALSE)"
    @eval_fn
    def C97():
        b97_1 = SNG.B97()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b97_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A98():
    # 'SNG'!A98
    value = 36571
    isdatetime = True

@register(SNG)
class B98():
    # 'SNG'!B98
    value = 2000
    formula = "=YEAR(A98)"
    @eval_fn
    def B98():
        a98_1 = SNG.A98()
        var_1 = YEAR(a98_1)
        return var_1

@register(SNG)
class C98():
    # 'SNG'!C98
    value = 16.18
    formula = "=VLOOKUP(B98,$H:$I,2,FALSE)"
    @eval_fn
    def C98():
        b98_1 = SNG.B98()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b98_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A99():
    # 'SNG'!A99
    value = 36600
    isdatetime = True

@register(SNG)
class B99():
    # 'SNG'!B99
    value = 2000
    formula = "=YEAR(A99)"
    @eval_fn
    def B99():
        a99_1 = SNG.A99()
        var_1 = YEAR(a99_1)
        return var_1

@register(SNG)
class C99():
    # 'SNG'!C99
    value = 16.18
    formula = "=VLOOKUP(B99,$H:$I,2,FALSE)"
    @eval_fn
    def C99():
        b99_1 = SNG.B99()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b99_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A100():
    # 'SNG'!A100
    value = 36631
    isdatetime = True

@register(SNG)
class B100():
    # 'SNG'!B100
    value = 2000
    formula = "=YEAR(A100)"
    @eval_fn
    def B100():
        a100_1 = SNG.A100()
        var_1 = YEAR(a100_1)
        return var_1

@register(SNG)
class C100():
    # 'SNG'!C100
    value = 16.18
    formula = "=VLOOKUP(B100,$H:$I,2,FALSE)"
    @eval_fn
    def C100():
        b100_1 = SNG.B100()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b100_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A101():
    # 'SNG'!A101
    value = 36661
    isdatetime = True

@register(SNG)
class B101():
    # 'SNG'!B101
    value = 2000
    formula = "=YEAR(A101)"
    @eval_fn
    def B101():
        a101_1 = SNG.A101()
        var_1 = YEAR(a101_1)
        return var_1

@register(SNG)
class C101():
    # 'SNG'!C101
    value = 16.18
    formula = "=VLOOKUP(B101,$H:$I,2,FALSE)"
    @eval_fn
    def C101():
        b101_1 = SNG.B101()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b101_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A102():
    # 'SNG'!A102
    value = 36692
    isdatetime = True

@register(SNG)
class B102():
    # 'SNG'!B102
    value = 2000
    formula = "=YEAR(A102)"
    @eval_fn
    def B102():
        a102_1 = SNG.A102()
        var_1 = YEAR(a102_1)
        return var_1

@register(SNG)
class C102():
    # 'SNG'!C102
    value = 16.18
    formula = "=VLOOKUP(B102,$H:$I,2,FALSE)"
    @eval_fn
    def C102():
        b102_1 = SNG.B102()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b102_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A103():
    # 'SNG'!A103
    value = 36722
    isdatetime = True

@register(SNG)
class B103():
    # 'SNG'!B103
    value = 2000
    formula = "=YEAR(A103)"
    @eval_fn
    def B103():
        a103_1 = SNG.A103()
        var_1 = YEAR(a103_1)
        return var_1

@register(SNG)
class C103():
    # 'SNG'!C103
    value = 16.18
    formula = "=VLOOKUP(B103,$H:$I,2,FALSE)"
    @eval_fn
    def C103():
        b103_1 = SNG.B103()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b103_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A104():
    # 'SNG'!A104
    value = 36753
    isdatetime = True

@register(SNG)
class B104():
    # 'SNG'!B104
    value = 2000
    formula = "=YEAR(A104)"
    @eval_fn
    def B104():
        a104_1 = SNG.A104()
        var_1 = YEAR(a104_1)
        return var_1

@register(SNG)
class C104():
    # 'SNG'!C104
    value = 16.18
    formula = "=VLOOKUP(B104,$H:$I,2,FALSE)"
    @eval_fn
    def C104():
        b104_1 = SNG.B104()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b104_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A105():
    # 'SNG'!A105
    value = 36784
    isdatetime = True

@register(SNG)
class B105():
    # 'SNG'!B105
    value = 2000
    formula = "=YEAR(A105)"
    @eval_fn
    def B105():
        a105_1 = SNG.A105()
        var_1 = YEAR(a105_1)
        return var_1

@register(SNG)
class C105():
    # 'SNG'!C105
    value = 16.18
    formula = "=VLOOKUP(B105,$H:$I,2,FALSE)"
    @eval_fn
    def C105():
        b105_1 = SNG.B105()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b105_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A106():
    # 'SNG'!A106
    value = 36814
    isdatetime = True

@register(SNG)
class B106():
    # 'SNG'!B106
    value = 2000
    formula = "=YEAR(A106)"
    @eval_fn
    def B106():
        a106_1 = SNG.A106()
        var_1 = YEAR(a106_1)
        return var_1

@register(SNG)
class C106():
    # 'SNG'!C106
    value = 16.18
    formula = "=VLOOKUP(B106,$H:$I,2,FALSE)"
    @eval_fn
    def C106():
        b106_1 = SNG.B106()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b106_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A107():
    # 'SNG'!A107
    value = 36845
    isdatetime = True

@register(SNG)
class B107():
    # 'SNG'!B107
    value = 2000
    formula = "=YEAR(A107)"
    @eval_fn
    def B107():
        a107_1 = SNG.A107()
        var_1 = YEAR(a107_1)
        return var_1

@register(SNG)
class C107():
    # 'SNG'!C107
    value = 16.18
    formula = "=VLOOKUP(B107,$H:$I,2,FALSE)"
    @eval_fn
    def C107():
        b107_1 = SNG.B107()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b107_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A108():
    # 'SNG'!A108
    value = 36875
    isdatetime = True

@register(SNG)
class B108():
    # 'SNG'!B108
    value = 2000
    formula = "=YEAR(A108)"
    @eval_fn
    def B108():
        a108_1 = SNG.A108()
        var_1 = YEAR(a108_1)
        return var_1

@register(SNG)
class C108():
    # 'SNG'!C108
    value = 16.18
    formula = "=VLOOKUP(B108,$H:$I,2,FALSE)"
    @eval_fn
    def C108():
        b108_1 = SNG.B108()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b108_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A109():
    # 'SNG'!A109
    value = 36906
    isdatetime = True

@register(SNG)
class B109():
    # 'SNG'!B109
    value = 2001
    formula = "=YEAR(A109)"
    @eval_fn
    def B109():
        a109_1 = SNG.A109()
        var_1 = YEAR(a109_1)
        return var_1

@register(SNG)
class C109():
    # 'SNG'!C109
    value = 16.85
    formula = "=VLOOKUP(B109,$H:$I,2,FALSE)"
    @eval_fn
    def C109():
        b109_1 = SNG.B109()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b109_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A110():
    # 'SNG'!A110
    value = 36937
    isdatetime = True

@register(SNG)
class B110():
    # 'SNG'!B110
    value = 2001
    formula = "=YEAR(A110)"
    @eval_fn
    def B110():
        a110_1 = SNG.A110()
        var_1 = YEAR(a110_1)
        return var_1

@register(SNG)
class C110():
    # 'SNG'!C110
    value = 16.85
    formula = "=VLOOKUP(B110,$H:$I,2,FALSE)"
    @eval_fn
    def C110():
        b110_1 = SNG.B110()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b110_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A111():
    # 'SNG'!A111
    value = 36965
    isdatetime = True

@register(SNG)
class B111():
    # 'SNG'!B111
    value = 2001
    formula = "=YEAR(A111)"
    @eval_fn
    def B111():
        a111_1 = SNG.A111()
        var_1 = YEAR(a111_1)
        return var_1

@register(SNG)
class C111():
    # 'SNG'!C111
    value = 16.85
    formula = "=VLOOKUP(B111,$H:$I,2,FALSE)"
    @eval_fn
    def C111():
        b111_1 = SNG.B111()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b111_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A112():
    # 'SNG'!A112
    value = 36996
    isdatetime = True

@register(SNG)
class B112():
    # 'SNG'!B112
    value = 2001
    formula = "=YEAR(A112)"
    @eval_fn
    def B112():
        a112_1 = SNG.A112()
        var_1 = YEAR(a112_1)
        return var_1

@register(SNG)
class C112():
    # 'SNG'!C112
    value = 16.85
    formula = "=VLOOKUP(B112,$H:$I,2,FALSE)"
    @eval_fn
    def C112():
        b112_1 = SNG.B112()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b112_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A113():
    # 'SNG'!A113
    value = 37026
    isdatetime = True

@register(SNG)
class B113():
    # 'SNG'!B113
    value = 2001
    formula = "=YEAR(A113)"
    @eval_fn
    def B113():
        a113_1 = SNG.A113()
        var_1 = YEAR(a113_1)
        return var_1

@register(SNG)
class C113():
    # 'SNG'!C113
    value = 16.85
    formula = "=VLOOKUP(B113,$H:$I,2,FALSE)"
    @eval_fn
    def C113():
        b113_1 = SNG.B113()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b113_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A114():
    # 'SNG'!A114
    value = 37057
    isdatetime = True

@register(SNG)
class B114():
    # 'SNG'!B114
    value = 2001
    formula = "=YEAR(A114)"
    @eval_fn
    def B114():
        a114_1 = SNG.A114()
        var_1 = YEAR(a114_1)
        return var_1

@register(SNG)
class C114():
    # 'SNG'!C114
    value = 16.85
    formula = "=VLOOKUP(B114,$H:$I,2,FALSE)"
    @eval_fn
    def C114():
        b114_1 = SNG.B114()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b114_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A115():
    # 'SNG'!A115
    value = 37087
    isdatetime = True

@register(SNG)
class B115():
    # 'SNG'!B115
    value = 2001
    formula = "=YEAR(A115)"
    @eval_fn
    def B115():
        a115_1 = SNG.A115()
        var_1 = YEAR(a115_1)
        return var_1

@register(SNG)
class C115():
    # 'SNG'!C115
    value = 16.85
    formula = "=VLOOKUP(B115,$H:$I,2,FALSE)"
    @eval_fn
    def C115():
        b115_1 = SNG.B115()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b115_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A116():
    # 'SNG'!A116
    value = 37118
    isdatetime = True

@register(SNG)
class B116():
    # 'SNG'!B116
    value = 2001
    formula = "=YEAR(A116)"
    @eval_fn
    def B116():
        a116_1 = SNG.A116()
        var_1 = YEAR(a116_1)
        return var_1

@register(SNG)
class C116():
    # 'SNG'!C116
    value = 16.85
    formula = "=VLOOKUP(B116,$H:$I,2,FALSE)"
    @eval_fn
    def C116():
        b116_1 = SNG.B116()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b116_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A117():
    # 'SNG'!A117
    value = 37149
    isdatetime = True

@register(SNG)
class B117():
    # 'SNG'!B117
    value = 2001
    formula = "=YEAR(A117)"
    @eval_fn
    def B117():
        a117_1 = SNG.A117()
        var_1 = YEAR(a117_1)
        return var_1

@register(SNG)
class C117():
    # 'SNG'!C117
    value = 16.85
    formula = "=VLOOKUP(B117,$H:$I,2,FALSE)"
    @eval_fn
    def C117():
        b117_1 = SNG.B117()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b117_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A118():
    # 'SNG'!A118
    value = 37179
    isdatetime = True

@register(SNG)
class B118():
    # 'SNG'!B118
    value = 2001
    formula = "=YEAR(A118)"
    @eval_fn
    def B118():
        a118_1 = SNG.A118()
        var_1 = YEAR(a118_1)
        return var_1

@register(SNG)
class C118():
    # 'SNG'!C118
    value = 16.85
    formula = "=VLOOKUP(B118,$H:$I,2,FALSE)"
    @eval_fn
    def C118():
        b118_1 = SNG.B118()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b118_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A119():
    # 'SNG'!A119
    value = 37210
    isdatetime = True

@register(SNG)
class B119():
    # 'SNG'!B119
    value = 2001
    formula = "=YEAR(A119)"
    @eval_fn
    def B119():
        a119_1 = SNG.A119()
        var_1 = YEAR(a119_1)
        return var_1

@register(SNG)
class C119():
    # 'SNG'!C119
    value = 16.85
    formula = "=VLOOKUP(B119,$H:$I,2,FALSE)"
    @eval_fn
    def C119():
        b119_1 = SNG.B119()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b119_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A120():
    # 'SNG'!A120
    value = 37240
    isdatetime = True

@register(SNG)
class B120():
    # 'SNG'!B120
    value = 2001
    formula = "=YEAR(A120)"
    @eval_fn
    def B120():
        a120_1 = SNG.A120()
        var_1 = YEAR(a120_1)
        return var_1

@register(SNG)
class C120():
    # 'SNG'!C120
    value = 16.85
    formula = "=VLOOKUP(B120,$H:$I,2,FALSE)"
    @eval_fn
    def C120():
        b120_1 = SNG.B120()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b120_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A121():
    # 'SNG'!A121
    value = 37271
    isdatetime = True

@register(SNG)
class B121():
    # 'SNG'!B121
    value = 2002
    formula = "=YEAR(A121)"
    @eval_fn
    def B121():
        a121_1 = SNG.A121()
        var_1 = YEAR(a121_1)
        return var_1

@register(SNG)
class C121():
    # 'SNG'!C121
    value = 16.67
    formula = "=VLOOKUP(B121,$H:$I,2,FALSE)"
    @eval_fn
    def C121():
        b121_1 = SNG.B121()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b121_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A122():
    # 'SNG'!A122
    value = 37302
    isdatetime = True

@register(SNG)
class B122():
    # 'SNG'!B122
    value = 2002
    formula = "=YEAR(A122)"
    @eval_fn
    def B122():
        a122_1 = SNG.A122()
        var_1 = YEAR(a122_1)
        return var_1

@register(SNG)
class C122():
    # 'SNG'!C122
    value = 16.67
    formula = "=VLOOKUP(B122,$H:$I,2,FALSE)"
    @eval_fn
    def C122():
        b122_1 = SNG.B122()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b122_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A123():
    # 'SNG'!A123
    value = 37330
    isdatetime = True

@register(SNG)
class B123():
    # 'SNG'!B123
    value = 2002
    formula = "=YEAR(A123)"
    @eval_fn
    def B123():
        a123_1 = SNG.A123()
        var_1 = YEAR(a123_1)
        return var_1

@register(SNG)
class C123():
    # 'SNG'!C123
    value = 16.67
    formula = "=VLOOKUP(B123,$H:$I,2,FALSE)"
    @eval_fn
    def C123():
        b123_1 = SNG.B123()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b123_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A124():
    # 'SNG'!A124
    value = 37361
    isdatetime = True

@register(SNG)
class B124():
    # 'SNG'!B124
    value = 2002
    formula = "=YEAR(A124)"
    @eval_fn
    def B124():
        a124_1 = SNG.A124()
        var_1 = YEAR(a124_1)
        return var_1

@register(SNG)
class C124():
    # 'SNG'!C124
    value = 16.67
    formula = "=VLOOKUP(B124,$H:$I,2,FALSE)"
    @eval_fn
    def C124():
        b124_1 = SNG.B124()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b124_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A125():
    # 'SNG'!A125
    value = 37391
    isdatetime = True

@register(SNG)
class B125():
    # 'SNG'!B125
    value = 2002
    formula = "=YEAR(A125)"
    @eval_fn
    def B125():
        a125_1 = SNG.A125()
        var_1 = YEAR(a125_1)
        return var_1

@register(SNG)
class C125():
    # 'SNG'!C125
    value = 16.67
    formula = "=VLOOKUP(B125,$H:$I,2,FALSE)"
    @eval_fn
    def C125():
        b125_1 = SNG.B125()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b125_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A126():
    # 'SNG'!A126
    value = 37422
    isdatetime = True

@register(SNG)
class B126():
    # 'SNG'!B126
    value = 2002
    formula = "=YEAR(A126)"
    @eval_fn
    def B126():
        a126_1 = SNG.A126()
        var_1 = YEAR(a126_1)
        return var_1

@register(SNG)
class C126():
    # 'SNG'!C126
    value = 16.67
    formula = "=VLOOKUP(B126,$H:$I,2,FALSE)"
    @eval_fn
    def C126():
        b126_1 = SNG.B126()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b126_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A127():
    # 'SNG'!A127
    value = 37452
    isdatetime = True

@register(SNG)
class B127():
    # 'SNG'!B127
    value = 2002
    formula = "=YEAR(A127)"
    @eval_fn
    def B127():
        a127_1 = SNG.A127()
        var_1 = YEAR(a127_1)
        return var_1

@register(SNG)
class C127():
    # 'SNG'!C127
    value = 16.67
    formula = "=VLOOKUP(B127,$H:$I,2,FALSE)"
    @eval_fn
    def C127():
        b127_1 = SNG.B127()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b127_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A128():
    # 'SNG'!A128
    value = 37483
    isdatetime = True

@register(SNG)
class B128():
    # 'SNG'!B128
    value = 2002
    formula = "=YEAR(A128)"
    @eval_fn
    def B128():
        a128_1 = SNG.A128()
        var_1 = YEAR(a128_1)
        return var_1

@register(SNG)
class C128():
    # 'SNG'!C128
    value = 16.67
    formula = "=VLOOKUP(B128,$H:$I,2,FALSE)"
    @eval_fn
    def C128():
        b128_1 = SNG.B128()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b128_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A129():
    # 'SNG'!A129
    value = 37514
    isdatetime = True

@register(SNG)
class B129():
    # 'SNG'!B129
    value = 2002
    formula = "=YEAR(A129)"
    @eval_fn
    def B129():
        a129_1 = SNG.A129()
        var_1 = YEAR(a129_1)
        return var_1

@register(SNG)
class C129():
    # 'SNG'!C129
    value = 16.67
    formula = "=VLOOKUP(B129,$H:$I,2,FALSE)"
    @eval_fn
    def C129():
        b129_1 = SNG.B129()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b129_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A130():
    # 'SNG'!A130
    value = 37544
    isdatetime = True

@register(SNG)
class B130():
    # 'SNG'!B130
    value = 2002
    formula = "=YEAR(A130)"
    @eval_fn
    def B130():
        a130_1 = SNG.A130()
        var_1 = YEAR(a130_1)
        return var_1

@register(SNG)
class C130():
    # 'SNG'!C130
    value = 16.67
    formula = "=VLOOKUP(B130,$H:$I,2,FALSE)"
    @eval_fn
    def C130():
        b130_1 = SNG.B130()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b130_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A131():
    # 'SNG'!A131
    value = 37575
    isdatetime = True

@register(SNG)
class B131():
    # 'SNG'!B131
    value = 2002
    formula = "=YEAR(A131)"
    @eval_fn
    def B131():
        a131_1 = SNG.A131()
        var_1 = YEAR(a131_1)
        return var_1

@register(SNG)
class C131():
    # 'SNG'!C131
    value = 16.67
    formula = "=VLOOKUP(B131,$H:$I,2,FALSE)"
    @eval_fn
    def C131():
        b131_1 = SNG.B131()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b131_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A132():
    # 'SNG'!A132
    value = 37605
    isdatetime = True

@register(SNG)
class B132():
    # 'SNG'!B132
    value = 2002
    formula = "=YEAR(A132)"
    @eval_fn
    def B132():
        a132_1 = SNG.A132()
        var_1 = YEAR(a132_1)
        return var_1

@register(SNG)
class C132():
    # 'SNG'!C132
    value = 16.67
    formula = "=VLOOKUP(B132,$H:$I,2,FALSE)"
    @eval_fn
    def C132():
        b132_1 = SNG.B132()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b132_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A133():
    # 'SNG'!A133
    value = 37636
    isdatetime = True

@register(SNG)
class B133():
    # 'SNG'!B133
    value = 2003
    formula = "=YEAR(A133)"
    @eval_fn
    def B133():
        a133_1 = SNG.A133()
        var_1 = YEAR(a133_1)
        return var_1

@register(SNG)
class C133():
    # 'SNG'!C133
    value = 19.03
    formula = "=VLOOKUP(B133,$H:$I,2,FALSE)"
    @eval_fn
    def C133():
        b133_1 = SNG.B133()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b133_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A134():
    # 'SNG'!A134
    value = 37667
    isdatetime = True

@register(SNG)
class B134():
    # 'SNG'!B134
    value = 2003
    formula = "=YEAR(A134)"
    @eval_fn
    def B134():
        a134_1 = SNG.A134()
        var_1 = YEAR(a134_1)
        return var_1

@register(SNG)
class C134():
    # 'SNG'!C134
    value = 19.03
    formula = "=VLOOKUP(B134,$H:$I,2,FALSE)"
    @eval_fn
    def C134():
        b134_1 = SNG.B134()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b134_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A135():
    # 'SNG'!A135
    value = 37695
    isdatetime = True

@register(SNG)
class B135():
    # 'SNG'!B135
    value = 2003
    formula = "=YEAR(A135)"
    @eval_fn
    def B135():
        a135_1 = SNG.A135()
        var_1 = YEAR(a135_1)
        return var_1

@register(SNG)
class C135():
    # 'SNG'!C135
    value = 19.03
    formula = "=VLOOKUP(B135,$H:$I,2,FALSE)"
    @eval_fn
    def C135():
        b135_1 = SNG.B135()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b135_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A136():
    # 'SNG'!A136
    value = 37726
    isdatetime = True

@register(SNG)
class B136():
    # 'SNG'!B136
    value = 2003
    formula = "=YEAR(A136)"
    @eval_fn
    def B136():
        a136_1 = SNG.A136()
        var_1 = YEAR(a136_1)
        return var_1

@register(SNG)
class C136():
    # 'SNG'!C136
    value = 19.03
    formula = "=VLOOKUP(B136,$H:$I,2,FALSE)"
    @eval_fn
    def C136():
        b136_1 = SNG.B136()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b136_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A137():
    # 'SNG'!A137
    value = 37756
    isdatetime = True

@register(SNG)
class B137():
    # 'SNG'!B137
    value = 2003
    formula = "=YEAR(A137)"
    @eval_fn
    def B137():
        a137_1 = SNG.A137()
        var_1 = YEAR(a137_1)
        return var_1

@register(SNG)
class C137():
    # 'SNG'!C137
    value = 19.03
    formula = "=VLOOKUP(B137,$H:$I,2,FALSE)"
    @eval_fn
    def C137():
        b137_1 = SNG.B137()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b137_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A138():
    # 'SNG'!A138
    value = 37787
    isdatetime = True

@register(SNG)
class B138():
    # 'SNG'!B138
    value = 2003
    formula = "=YEAR(A138)"
    @eval_fn
    def B138():
        a138_1 = SNG.A138()
        var_1 = YEAR(a138_1)
        return var_1

@register(SNG)
class C138():
    # 'SNG'!C138
    value = 19.03
    formula = "=VLOOKUP(B138,$H:$I,2,FALSE)"
    @eval_fn
    def C138():
        b138_1 = SNG.B138()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b138_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A139():
    # 'SNG'!A139
    value = 37817
    isdatetime = True

@register(SNG)
class B139():
    # 'SNG'!B139
    value = 2003
    formula = "=YEAR(A139)"
    @eval_fn
    def B139():
        a139_1 = SNG.A139()
        var_1 = YEAR(a139_1)
        return var_1

@register(SNG)
class C139():
    # 'SNG'!C139
    value = 19.03
    formula = "=VLOOKUP(B139,$H:$I,2,FALSE)"
    @eval_fn
    def C139():
        b139_1 = SNG.B139()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b139_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A140():
    # 'SNG'!A140
    value = 37848
    isdatetime = True

@register(SNG)
class B140():
    # 'SNG'!B140
    value = 2003
    formula = "=YEAR(A140)"
    @eval_fn
    def B140():
        a140_1 = SNG.A140()
        var_1 = YEAR(a140_1)
        return var_1

@register(SNG)
class C140():
    # 'SNG'!C140
    value = 19.03
    formula = "=VLOOKUP(B140,$H:$I,2,FALSE)"
    @eval_fn
    def C140():
        b140_1 = SNG.B140()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b140_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A141():
    # 'SNG'!A141
    value = 37879
    isdatetime = True

@register(SNG)
class B141():
    # 'SNG'!B141
    value = 2003
    formula = "=YEAR(A141)"
    @eval_fn
    def B141():
        a141_1 = SNG.A141()
        var_1 = YEAR(a141_1)
        return var_1

@register(SNG)
class C141():
    # 'SNG'!C141
    value = 19.03
    formula = "=VLOOKUP(B141,$H:$I,2,FALSE)"
    @eval_fn
    def C141():
        b141_1 = SNG.B141()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b141_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A142():
    # 'SNG'!A142
    value = 37909
    isdatetime = True

@register(SNG)
class B142():
    # 'SNG'!B142
    value = 2003
    formula = "=YEAR(A142)"
    @eval_fn
    def B142():
        a142_1 = SNG.A142()
        var_1 = YEAR(a142_1)
        return var_1

@register(SNG)
class C142():
    # 'SNG'!C142
    value = 19.03
    formula = "=VLOOKUP(B142,$H:$I,2,FALSE)"
    @eval_fn
    def C142():
        b142_1 = SNG.B142()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b142_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A143():
    # 'SNG'!A143
    value = 37940
    isdatetime = True

@register(SNG)
class B143():
    # 'SNG'!B143
    value = 2003
    formula = "=YEAR(A143)"
    @eval_fn
    def B143():
        a143_1 = SNG.A143()
        var_1 = YEAR(a143_1)
        return var_1

@register(SNG)
class C143():
    # 'SNG'!C143
    value = 19.03
    formula = "=VLOOKUP(B143,$H:$I,2,FALSE)"
    @eval_fn
    def C143():
        b143_1 = SNG.B143()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b143_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A144():
    # 'SNG'!A144
    value = 37970
    isdatetime = True

@register(SNG)
class B144():
    # 'SNG'!B144
    value = 2003
    formula = "=YEAR(A144)"
    @eval_fn
    def B144():
        a144_1 = SNG.A144()
        var_1 = YEAR(a144_1)
        return var_1

@register(SNG)
class C144():
    # 'SNG'!C144
    value = 19.03
    formula = "=VLOOKUP(B144,$H:$I,2,FALSE)"
    @eval_fn
    def C144():
        b144_1 = SNG.B144()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b144_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A145():
    # 'SNG'!A145
    value = 38001
    isdatetime = True

@register(SNG)
class B145():
    # 'SNG'!B145
    value = 2004
    formula = "=YEAR(A145)"
    @eval_fn
    def B145():
        a145_1 = SNG.A145()
        var_1 = YEAR(a145_1)
        return var_1

@register(SNG)
class C145():
    # 'SNG'!C145
    value = 20.33
    formula = "=VLOOKUP(B145,$H:$I,2,FALSE)"
    @eval_fn
    def C145():
        b145_1 = SNG.B145()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b145_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A146():
    # 'SNG'!A146
    value = 38032
    isdatetime = True

@register(SNG)
class B146():
    # 'SNG'!B146
    value = 2004
    formula = "=YEAR(A146)"
    @eval_fn
    def B146():
        a146_1 = SNG.A146()
        var_1 = YEAR(a146_1)
        return var_1

@register(SNG)
class C146():
    # 'SNG'!C146
    value = 20.33
    formula = "=VLOOKUP(B146,$H:$I,2,FALSE)"
    @eval_fn
    def C146():
        b146_1 = SNG.B146()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b146_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A147():
    # 'SNG'!A147
    value = 38061
    isdatetime = True

@register(SNG)
class B147():
    # 'SNG'!B147
    value = 2004
    formula = "=YEAR(A147)"
    @eval_fn
    def B147():
        a147_1 = SNG.A147()
        var_1 = YEAR(a147_1)
        return var_1

@register(SNG)
class C147():
    # 'SNG'!C147
    value = 20.33
    formula = "=VLOOKUP(B147,$H:$I,2,FALSE)"
    @eval_fn
    def C147():
        b147_1 = SNG.B147()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b147_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A148():
    # 'SNG'!A148
    value = 38092
    isdatetime = True

@register(SNG)
class B148():
    # 'SNG'!B148
    value = 2004
    formula = "=YEAR(A148)"
    @eval_fn
    def B148():
        a148_1 = SNG.A148()
        var_1 = YEAR(a148_1)
        return var_1

@register(SNG)
class C148():
    # 'SNG'!C148
    value = 20.33
    formula = "=VLOOKUP(B148,$H:$I,2,FALSE)"
    @eval_fn
    def C148():
        b148_1 = SNG.B148()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b148_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A149():
    # 'SNG'!A149
    value = 38122
    isdatetime = True

@register(SNG)
class B149():
    # 'SNG'!B149
    value = 2004
    formula = "=YEAR(A149)"
    @eval_fn
    def B149():
        a149_1 = SNG.A149()
        var_1 = YEAR(a149_1)
        return var_1

@register(SNG)
class C149():
    # 'SNG'!C149
    value = 20.33
    formula = "=VLOOKUP(B149,$H:$I,2,FALSE)"
    @eval_fn
    def C149():
        b149_1 = SNG.B149()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b149_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A150():
    # 'SNG'!A150
    value = 38153
    isdatetime = True

@register(SNG)
class B150():
    # 'SNG'!B150
    value = 2004
    formula = "=YEAR(A150)"
    @eval_fn
    def B150():
        a150_1 = SNG.A150()
        var_1 = YEAR(a150_1)
        return var_1

@register(SNG)
class C150():
    # 'SNG'!C150
    value = 20.33
    formula = "=VLOOKUP(B150,$H:$I,2,FALSE)"
    @eval_fn
    def C150():
        b150_1 = SNG.B150()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b150_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A151():
    # 'SNG'!A151
    value = 38183
    isdatetime = True

@register(SNG)
class B151():
    # 'SNG'!B151
    value = 2004
    formula = "=YEAR(A151)"
    @eval_fn
    def B151():
        a151_1 = SNG.A151()
        var_1 = YEAR(a151_1)
        return var_1

@register(SNG)
class C151():
    # 'SNG'!C151
    value = 20.33
    formula = "=VLOOKUP(B151,$H:$I,2,FALSE)"
    @eval_fn
    def C151():
        b151_1 = SNG.B151()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b151_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A152():
    # 'SNG'!A152
    value = 38214
    isdatetime = True

@register(SNG)
class B152():
    # 'SNG'!B152
    value = 2004
    formula = "=YEAR(A152)"
    @eval_fn
    def B152():
        a152_1 = SNG.A152()
        var_1 = YEAR(a152_1)
        return var_1

@register(SNG)
class C152():
    # 'SNG'!C152
    value = 20.33
    formula = "=VLOOKUP(B152,$H:$I,2,FALSE)"
    @eval_fn
    def C152():
        b152_1 = SNG.B152()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b152_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A153():
    # 'SNG'!A153
    value = 38245
    isdatetime = True

@register(SNG)
class B153():
    # 'SNG'!B153
    value = 2004
    formula = "=YEAR(A153)"
    @eval_fn
    def B153():
        a153_1 = SNG.A153()
        var_1 = YEAR(a153_1)
        return var_1

@register(SNG)
class C153():
    # 'SNG'!C153
    value = 20.33
    formula = "=VLOOKUP(B153,$H:$I,2,FALSE)"
    @eval_fn
    def C153():
        b153_1 = SNG.B153()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b153_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A154():
    # 'SNG'!A154
    value = 38275
    isdatetime = True

@register(SNG)
class B154():
    # 'SNG'!B154
    value = 2004
    formula = "=YEAR(A154)"
    @eval_fn
    def B154():
        a154_1 = SNG.A154()
        var_1 = YEAR(a154_1)
        return var_1

@register(SNG)
class C154():
    # 'SNG'!C154
    value = 20.33
    formula = "=VLOOKUP(B154,$H:$I,2,FALSE)"
    @eval_fn
    def C154():
        b154_1 = SNG.B154()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b154_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A155():
    # 'SNG'!A155
    value = 38306
    isdatetime = True

@register(SNG)
class B155():
    # 'SNG'!B155
    value = 2004
    formula = "=YEAR(A155)"
    @eval_fn
    def B155():
        a155_1 = SNG.A155()
        var_1 = YEAR(a155_1)
        return var_1

@register(SNG)
class C155():
    # 'SNG'!C155
    value = 20.33
    formula = "=VLOOKUP(B155,$H:$I,2,FALSE)"
    @eval_fn
    def C155():
        b155_1 = SNG.B155()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b155_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A156():
    # 'SNG'!A156
    value = 38336
    isdatetime = True

@register(SNG)
class B156():
    # 'SNG'!B156
    value = 2004
    formula = "=YEAR(A156)"
    @eval_fn
    def B156():
        a156_1 = SNG.A156()
        var_1 = YEAR(a156_1)
        return var_1

@register(SNG)
class C156():
    # 'SNG'!C156
    value = 20.33
    formula = "=VLOOKUP(B156,$H:$I,2,FALSE)"
    @eval_fn
    def C156():
        b156_1 = SNG.B156()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b156_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A157():
    # 'SNG'!A157
    value = 38367
    isdatetime = True

@register(SNG)
class B157():
    # 'SNG'!B157
    value = 2005
    formula = "=YEAR(A157)"
    @eval_fn
    def B157():
        a157_1 = SNG.A157()
        var_1 = YEAR(a157_1)
        return var_1

@register(SNG)
class C157():
    # 'SNG'!C157
    value = 24.3
    formula = "=VLOOKUP(B157,$H:$I,2,FALSE)"
    @eval_fn
    def C157():
        b157_1 = SNG.B157()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b157_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A158():
    # 'SNG'!A158
    value = 38398
    isdatetime = True

@register(SNG)
class B158():
    # 'SNG'!B158
    value = 2005
    formula = "=YEAR(A158)"
    @eval_fn
    def B158():
        a158_1 = SNG.A158()
        var_1 = YEAR(a158_1)
        return var_1

@register(SNG)
class C158():
    # 'SNG'!C158
    value = 24.3
    formula = "=VLOOKUP(B158,$H:$I,2,FALSE)"
    @eval_fn
    def C158():
        b158_1 = SNG.B158()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b158_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A159():
    # 'SNG'!A159
    value = 38426
    isdatetime = True

@register(SNG)
class B159():
    # 'SNG'!B159
    value = 2005
    formula = "=YEAR(A159)"
    @eval_fn
    def B159():
        a159_1 = SNG.A159()
        var_1 = YEAR(a159_1)
        return var_1

@register(SNG)
class C159():
    # 'SNG'!C159
    value = 24.3
    formula = "=VLOOKUP(B159,$H:$I,2,FALSE)"
    @eval_fn
    def C159():
        b159_1 = SNG.B159()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b159_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A160():
    # 'SNG'!A160
    value = 38457
    isdatetime = True

@register(SNG)
class B160():
    # 'SNG'!B160
    value = 2005
    formula = "=YEAR(A160)"
    @eval_fn
    def B160():
        a160_1 = SNG.A160()
        var_1 = YEAR(a160_1)
        return var_1

@register(SNG)
class C160():
    # 'SNG'!C160
    value = 24.3
    formula = "=VLOOKUP(B160,$H:$I,2,FALSE)"
    @eval_fn
    def C160():
        b160_1 = SNG.B160()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b160_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A161():
    # 'SNG'!A161
    value = 38487
    isdatetime = True

@register(SNG)
class B161():
    # 'SNG'!B161
    value = 2005
    formula = "=YEAR(A161)"
    @eval_fn
    def B161():
        a161_1 = SNG.A161()
        var_1 = YEAR(a161_1)
        return var_1

@register(SNG)
class C161():
    # 'SNG'!C161
    value = 24.3
    formula = "=VLOOKUP(B161,$H:$I,2,FALSE)"
    @eval_fn
    def C161():
        b161_1 = SNG.B161()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b161_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A162():
    # 'SNG'!A162
    value = 38518
    isdatetime = True

@register(SNG)
class B162():
    # 'SNG'!B162
    value = 2005
    formula = "=YEAR(A162)"
    @eval_fn
    def B162():
        a162_1 = SNG.A162()
        var_1 = YEAR(a162_1)
        return var_1

@register(SNG)
class C162():
    # 'SNG'!C162
    value = 24.3
    formula = "=VLOOKUP(B162,$H:$I,2,FALSE)"
    @eval_fn
    def C162():
        b162_1 = SNG.B162()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b162_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A163():
    # 'SNG'!A163
    value = 38548
    isdatetime = True

@register(SNG)
class B163():
    # 'SNG'!B163
    value = 2005
    formula = "=YEAR(A163)"
    @eval_fn
    def B163():
        a163_1 = SNG.A163()
        var_1 = YEAR(a163_1)
        return var_1

@register(SNG)
class C163():
    # 'SNG'!C163
    value = 24.3
    formula = "=VLOOKUP(B163,$H:$I,2,FALSE)"
    @eval_fn
    def C163():
        b163_1 = SNG.B163()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b163_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A164():
    # 'SNG'!A164
    value = 38579
    isdatetime = True

@register(SNG)
class B164():
    # 'SNG'!B164
    value = 2005
    formula = "=YEAR(A164)"
    @eval_fn
    def B164():
        a164_1 = SNG.A164()
        var_1 = YEAR(a164_1)
        return var_1

@register(SNG)
class C164():
    # 'SNG'!C164
    value = 24.3
    formula = "=VLOOKUP(B164,$H:$I,2,FALSE)"
    @eval_fn
    def C164():
        b164_1 = SNG.B164()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b164_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A165():
    # 'SNG'!A165
    value = 38610
    isdatetime = True

@register(SNG)
class B165():
    # 'SNG'!B165
    value = 2005
    formula = "=YEAR(A165)"
    @eval_fn
    def B165():
        a165_1 = SNG.A165()
        var_1 = YEAR(a165_1)
        return var_1

@register(SNG)
class C165():
    # 'SNG'!C165
    value = 24.3
    formula = "=VLOOKUP(B165,$H:$I,2,FALSE)"
    @eval_fn
    def C165():
        b165_1 = SNG.B165()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b165_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A166():
    # 'SNG'!A166
    value = 38640
    isdatetime = True

@register(SNG)
class B166():
    # 'SNG'!B166
    value = 2005
    formula = "=YEAR(A166)"
    @eval_fn
    def B166():
        a166_1 = SNG.A166()
        var_1 = YEAR(a166_1)
        return var_1

@register(SNG)
class C166():
    # 'SNG'!C166
    value = 24.3
    formula = "=VLOOKUP(B166,$H:$I,2,FALSE)"
    @eval_fn
    def C166():
        b166_1 = SNG.B166()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b166_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A167():
    # 'SNG'!A167
    value = 38671
    isdatetime = True

@register(SNG)
class B167():
    # 'SNG'!B167
    value = 2005
    formula = "=YEAR(A167)"
    @eval_fn
    def B167():
        a167_1 = SNG.A167()
        var_1 = YEAR(a167_1)
        return var_1

@register(SNG)
class C167():
    # 'SNG'!C167
    value = 24.3
    formula = "=VLOOKUP(B167,$H:$I,2,FALSE)"
    @eval_fn
    def C167():
        b167_1 = SNG.B167()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b167_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A168():
    # 'SNG'!A168
    value = 38701
    isdatetime = True

@register(SNG)
class B168():
    # 'SNG'!B168
    value = 2005
    formula = "=YEAR(A168)"
    @eval_fn
    def B168():
        a168_1 = SNG.A168()
        var_1 = YEAR(a168_1)
        return var_1

@register(SNG)
class C168():
    # 'SNG'!C168
    value = 24.3
    formula = "=VLOOKUP(B168,$H:$I,2,FALSE)"
    @eval_fn
    def C168():
        b168_1 = SNG.B168()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b168_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A169():
    # 'SNG'!A169
    value = 38732
    isdatetime = True

@register(SNG)
class B169():
    # 'SNG'!B169
    value = 2006
    formula = "=YEAR(A169)"
    @eval_fn
    def B169():
        a169_1 = SNG.A169()
        var_1 = YEAR(a169_1)
        return var_1

@register(SNG)
class C169():
    # 'SNG'!C169
    value = 27.54
    formula = "=VLOOKUP(B169,$H:$I,2,FALSE)"
    @eval_fn
    def C169():
        b169_1 = SNG.B169()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b169_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A170():
    # 'SNG'!A170
    value = 38763
    isdatetime = True

@register(SNG)
class B170():
    # 'SNG'!B170
    value = 2006
    formula = "=YEAR(A170)"
    @eval_fn
    def B170():
        a170_1 = SNG.A170()
        var_1 = YEAR(a170_1)
        return var_1

@register(SNG)
class C170():
    # 'SNG'!C170
    value = 27.54
    formula = "=VLOOKUP(B170,$H:$I,2,FALSE)"
    @eval_fn
    def C170():
        b170_1 = SNG.B170()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b170_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A171():
    # 'SNG'!A171
    value = 38791
    isdatetime = True

@register(SNG)
class B171():
    # 'SNG'!B171
    value = 2006
    formula = "=YEAR(A171)"
    @eval_fn
    def B171():
        a171_1 = SNG.A171()
        var_1 = YEAR(a171_1)
        return var_1

@register(SNG)
class C171():
    # 'SNG'!C171
    value = 27.54
    formula = "=VLOOKUP(B171,$H:$I,2,FALSE)"
    @eval_fn
    def C171():
        b171_1 = SNG.B171()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b171_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A172():
    # 'SNG'!A172
    value = 38822
    isdatetime = True

@register(SNG)
class B172():
    # 'SNG'!B172
    value = 2006
    formula = "=YEAR(A172)"
    @eval_fn
    def B172():
        a172_1 = SNG.A172()
        var_1 = YEAR(a172_1)
        return var_1

@register(SNG)
class C172():
    # 'SNG'!C172
    value = 27.54
    formula = "=VLOOKUP(B172,$H:$I,2,FALSE)"
    @eval_fn
    def C172():
        b172_1 = SNG.B172()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b172_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A173():
    # 'SNG'!A173
    value = 38852
    isdatetime = True

@register(SNG)
class B173():
    # 'SNG'!B173
    value = 2006
    formula = "=YEAR(A173)"
    @eval_fn
    def B173():
        a173_1 = SNG.A173()
        var_1 = YEAR(a173_1)
        return var_1

@register(SNG)
class C173():
    # 'SNG'!C173
    value = 27.54
    formula = "=VLOOKUP(B173,$H:$I,2,FALSE)"
    @eval_fn
    def C173():
        b173_1 = SNG.B173()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b173_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A174():
    # 'SNG'!A174
    value = 38883
    isdatetime = True

@register(SNG)
class B174():
    # 'SNG'!B174
    value = 2006
    formula = "=YEAR(A174)"
    @eval_fn
    def B174():
        a174_1 = SNG.A174()
        var_1 = YEAR(a174_1)
        return var_1

@register(SNG)
class C174():
    # 'SNG'!C174
    value = 27.54
    formula = "=VLOOKUP(B174,$H:$I,2,FALSE)"
    @eval_fn
    def C174():
        b174_1 = SNG.B174()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b174_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A175():
    # 'SNG'!A175
    value = 38913
    isdatetime = True

@register(SNG)
class B175():
    # 'SNG'!B175
    value = 2006
    formula = "=YEAR(A175)"
    @eval_fn
    def B175():
        a175_1 = SNG.A175()
        var_1 = YEAR(a175_1)
        return var_1

@register(SNG)
class C175():
    # 'SNG'!C175
    value = 27.54
    formula = "=VLOOKUP(B175,$H:$I,2,FALSE)"
    @eval_fn
    def C175():
        b175_1 = SNG.B175()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b175_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A176():
    # 'SNG'!A176
    value = 38944
    isdatetime = True

@register(SNG)
class B176():
    # 'SNG'!B176
    value = 2006
    formula = "=YEAR(A176)"
    @eval_fn
    def B176():
        a176_1 = SNG.A176()
        var_1 = YEAR(a176_1)
        return var_1

@register(SNG)
class C176():
    # 'SNG'!C176
    value = 27.54
    formula = "=VLOOKUP(B176,$H:$I,2,FALSE)"
    @eval_fn
    def C176():
        b176_1 = SNG.B176()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b176_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A177():
    # 'SNG'!A177
    value = 38975
    isdatetime = True

@register(SNG)
class B177():
    # 'SNG'!B177
    value = 2006
    formula = "=YEAR(A177)"
    @eval_fn
    def B177():
        a177_1 = SNG.A177()
        var_1 = YEAR(a177_1)
        return var_1

@register(SNG)
class C177():
    # 'SNG'!C177
    value = 27.54
    formula = "=VLOOKUP(B177,$H:$I,2,FALSE)"
    @eval_fn
    def C177():
        b177_1 = SNG.B177()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b177_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A178():
    # 'SNG'!A178
    value = 39005
    isdatetime = True

@register(SNG)
class B178():
    # 'SNG'!B178
    value = 2006
    formula = "=YEAR(A178)"
    @eval_fn
    def B178():
        a178_1 = SNG.A178()
        var_1 = YEAR(a178_1)
        return var_1

@register(SNG)
class C178():
    # 'SNG'!C178
    value = 27.54
    formula = "=VLOOKUP(B178,$H:$I,2,FALSE)"
    @eval_fn
    def C178():
        b178_1 = SNG.B178()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b178_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A179():
    # 'SNG'!A179
    value = 39036
    isdatetime = True

@register(SNG)
class B179():
    # 'SNG'!B179
    value = 2006
    formula = "=YEAR(A179)"
    @eval_fn
    def B179():
        a179_1 = SNG.A179()
        var_1 = YEAR(a179_1)
        return var_1

@register(SNG)
class C179():
    # 'SNG'!C179
    value = 27.54
    formula = "=VLOOKUP(B179,$H:$I,2,FALSE)"
    @eval_fn
    def C179():
        b179_1 = SNG.B179()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b179_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A180():
    # 'SNG'!A180
    value = 39066
    isdatetime = True

@register(SNG)
class B180():
    # 'SNG'!B180
    value = 2006
    formula = "=YEAR(A180)"
    @eval_fn
    def B180():
        a180_1 = SNG.A180()
        var_1 = YEAR(a180_1)
        return var_1

@register(SNG)
class C180():
    # 'SNG'!C180
    value = 27.54
    formula = "=VLOOKUP(B180,$H:$I,2,FALSE)"
    @eval_fn
    def C180():
        b180_1 = SNG.B180()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b180_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A181():
    # 'SNG'!A181
    value = 39097
    isdatetime = True

@register(SNG)
class B181():
    # 'SNG'!B181
    value = 2007
    formula = "=YEAR(A181)"
    @eval_fn
    def B181():
        a181_1 = SNG.A181()
        var_1 = YEAR(a181_1)
        return var_1

@register(SNG)
class C181():
    # 'SNG'!C181
    value = 26.83
    formula = "=VLOOKUP(B181,$H:$I,2,FALSE)"
    @eval_fn
    def C181():
        b181_1 = SNG.B181()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b181_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A182():
    # 'SNG'!A182
    value = 39128
    isdatetime = True

@register(SNG)
class B182():
    # 'SNG'!B182
    value = 2007
    formula = "=YEAR(A182)"
    @eval_fn
    def B182():
        a182_1 = SNG.A182()
        var_1 = YEAR(a182_1)
        return var_1

@register(SNG)
class C182():
    # 'SNG'!C182
    value = 26.83
    formula = "=VLOOKUP(B182,$H:$I,2,FALSE)"
    @eval_fn
    def C182():
        b182_1 = SNG.B182()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b182_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A183():
    # 'SNG'!A183
    value = 39156
    isdatetime = True

@register(SNG)
class B183():
    # 'SNG'!B183
    value = 2007
    formula = "=YEAR(A183)"
    @eval_fn
    def B183():
        a183_1 = SNG.A183()
        var_1 = YEAR(a183_1)
        return var_1

@register(SNG)
class C183():
    # 'SNG'!C183
    value = 26.83
    formula = "=VLOOKUP(B183,$H:$I,2,FALSE)"
    @eval_fn
    def C183():
        b183_1 = SNG.B183()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b183_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A184():
    # 'SNG'!A184
    value = 39187
    isdatetime = True

@register(SNG)
class B184():
    # 'SNG'!B184
    value = 2007
    formula = "=YEAR(A184)"
    @eval_fn
    def B184():
        a184_1 = SNG.A184()
        var_1 = YEAR(a184_1)
        return var_1

@register(SNG)
class C184():
    # 'SNG'!C184
    value = 26.83
    formula = "=VLOOKUP(B184,$H:$I,2,FALSE)"
    @eval_fn
    def C184():
        b184_1 = SNG.B184()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b184_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A185():
    # 'SNG'!A185
    value = 39217
    isdatetime = True

@register(SNG)
class B185():
    # 'SNG'!B185
    value = 2007
    formula = "=YEAR(A185)"
    @eval_fn
    def B185():
        a185_1 = SNG.A185()
        var_1 = YEAR(a185_1)
        return var_1

@register(SNG)
class C185():
    # 'SNG'!C185
    value = 26.83
    formula = "=VLOOKUP(B185,$H:$I,2,FALSE)"
    @eval_fn
    def C185():
        b185_1 = SNG.B185()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b185_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A186():
    # 'SNG'!A186
    value = 39248
    isdatetime = True

@register(SNG)
class B186():
    # 'SNG'!B186
    value = 2007
    formula = "=YEAR(A186)"
    @eval_fn
    def B186():
        a186_1 = SNG.A186()
        var_1 = YEAR(a186_1)
        return var_1

@register(SNG)
class C186():
    # 'SNG'!C186
    value = 26.83
    formula = "=VLOOKUP(B186,$H:$I,2,FALSE)"
    @eval_fn
    def C186():
        b186_1 = SNG.B186()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b186_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A187():
    # 'SNG'!A187
    value = 39278
    isdatetime = True

@register(SNG)
class B187():
    # 'SNG'!B187
    value = 2007
    formula = "=YEAR(A187)"
    @eval_fn
    def B187():
        a187_1 = SNG.A187()
        var_1 = YEAR(a187_1)
        return var_1

@register(SNG)
class C187():
    # 'SNG'!C187
    value = 26.83
    formula = "=VLOOKUP(B187,$H:$I,2,FALSE)"
    @eval_fn
    def C187():
        b187_1 = SNG.B187()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b187_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A188():
    # 'SNG'!A188
    value = 39309
    isdatetime = True

@register(SNG)
class B188():
    # 'SNG'!B188
    value = 2007
    formula = "=YEAR(A188)"
    @eval_fn
    def B188():
        a188_1 = SNG.A188()
        var_1 = YEAR(a188_1)
        return var_1

@register(SNG)
class C188():
    # 'SNG'!C188
    value = 26.83
    formula = "=VLOOKUP(B188,$H:$I,2,FALSE)"
    @eval_fn
    def C188():
        b188_1 = SNG.B188()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b188_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A189():
    # 'SNG'!A189
    value = 39340
    isdatetime = True

@register(SNG)
class B189():
    # 'SNG'!B189
    value = 2007
    formula = "=YEAR(A189)"
    @eval_fn
    def B189():
        a189_1 = SNG.A189()
        var_1 = YEAR(a189_1)
        return var_1

@register(SNG)
class C189():
    # 'SNG'!C189
    value = 26.83
    formula = "=VLOOKUP(B189,$H:$I,2,FALSE)"
    @eval_fn
    def C189():
        b189_1 = SNG.B189()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b189_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A190():
    # 'SNG'!A190
    value = 39370
    isdatetime = True

@register(SNG)
class B190():
    # 'SNG'!B190
    value = 2007
    formula = "=YEAR(A190)"
    @eval_fn
    def B190():
        a190_1 = SNG.A190()
        var_1 = YEAR(a190_1)
        return var_1

@register(SNG)
class C190():
    # 'SNG'!C190
    value = 26.83
    formula = "=VLOOKUP(B190,$H:$I,2,FALSE)"
    @eval_fn
    def C190():
        b190_1 = SNG.B190()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b190_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A191():
    # 'SNG'!A191
    value = 39401
    isdatetime = True

@register(SNG)
class B191():
    # 'SNG'!B191
    value = 2007
    formula = "=YEAR(A191)"
    @eval_fn
    def B191():
        a191_1 = SNG.A191()
        var_1 = YEAR(a191_1)
        return var_1

@register(SNG)
class C191():
    # 'SNG'!C191
    value = 26.83
    formula = "=VLOOKUP(B191,$H:$I,2,FALSE)"
    @eval_fn
    def C191():
        b191_1 = SNG.B191()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b191_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A192():
    # 'SNG'!A192
    value = 39431
    isdatetime = True

@register(SNG)
class B192():
    # 'SNG'!B192
    value = 2007
    formula = "=YEAR(A192)"
    @eval_fn
    def B192():
        a192_1 = SNG.A192()
        var_1 = YEAR(a192_1)
        return var_1

@register(SNG)
class C192():
    # 'SNG'!C192
    value = 26.83
    formula = "=VLOOKUP(B192,$H:$I,2,FALSE)"
    @eval_fn
    def C192():
        b192_1 = SNG.B192()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b192_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A193():
    # 'SNG'!A193
    value = 39462
    isdatetime = True

@register(SNG)
class B193():
    # 'SNG'!B193
    value = 2008
    formula = "=YEAR(A193)"
    @eval_fn
    def B193():
        a193_1 = SNG.A193()
        var_1 = YEAR(a193_1)
        return var_1

@register(SNG)
class C193():
    # 'SNG'!C193
    value = 36.73
    formula = "=VLOOKUP(B193,$H:$I,2,FALSE)"
    @eval_fn
    def C193():
        b193_1 = SNG.B193()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b193_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A194():
    # 'SNG'!A194
    value = 39493
    isdatetime = True

@register(SNG)
class B194():
    # 'SNG'!B194
    value = 2008
    formula = "=YEAR(A194)"
    @eval_fn
    def B194():
        a194_1 = SNG.A194()
        var_1 = YEAR(a194_1)
        return var_1

@register(SNG)
class C194():
    # 'SNG'!C194
    value = 36.73
    formula = "=VLOOKUP(B194,$H:$I,2,FALSE)"
    @eval_fn
    def C194():
        b194_1 = SNG.B194()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b194_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A195():
    # 'SNG'!A195
    value = 39522
    isdatetime = True

@register(SNG)
class B195():
    # 'SNG'!B195
    value = 2008
    formula = "=YEAR(A195)"
    @eval_fn
    def B195():
        a195_1 = SNG.A195()
        var_1 = YEAR(a195_1)
        return var_1

@register(SNG)
class C195():
    # 'SNG'!C195
    value = 36.73
    formula = "=VLOOKUP(B195,$H:$I,2,FALSE)"
    @eval_fn
    def C195():
        b195_1 = SNG.B195()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b195_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A196():
    # 'SNG'!A196
    value = 39553
    isdatetime = True

@register(SNG)
class B196():
    # 'SNG'!B196
    value = 2008
    formula = "=YEAR(A196)"
    @eval_fn
    def B196():
        a196_1 = SNG.A196()
        var_1 = YEAR(a196_1)
        return var_1

@register(SNG)
class C196():
    # 'SNG'!C196
    value = 36.73
    formula = "=VLOOKUP(B196,$H:$I,2,FALSE)"
    @eval_fn
    def C196():
        b196_1 = SNG.B196()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b196_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A197():
    # 'SNG'!A197
    value = 39583
    isdatetime = True

@register(SNG)
class B197():
    # 'SNG'!B197
    value = 2008
    formula = "=YEAR(A197)"
    @eval_fn
    def B197():
        a197_1 = SNG.A197()
        var_1 = YEAR(a197_1)
        return var_1

@register(SNG)
class C197():
    # 'SNG'!C197
    value = 36.73
    formula = "=VLOOKUP(B197,$H:$I,2,FALSE)"
    @eval_fn
    def C197():
        b197_1 = SNG.B197()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b197_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A198():
    # 'SNG'!A198
    value = 39614
    isdatetime = True

@register(SNG)
class B198():
    # 'SNG'!B198
    value = 2008
    formula = "=YEAR(A198)"
    @eval_fn
    def B198():
        a198_1 = SNG.A198()
        var_1 = YEAR(a198_1)
        return var_1

@register(SNG)
class C198():
    # 'SNG'!C198
    value = 36.73
    formula = "=VLOOKUP(B198,$H:$I,2,FALSE)"
    @eval_fn
    def C198():
        b198_1 = SNG.B198()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b198_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A199():
    # 'SNG'!A199
    value = 39644
    isdatetime = True

@register(SNG)
class B199():
    # 'SNG'!B199
    value = 2008
    formula = "=YEAR(A199)"
    @eval_fn
    def B199():
        a199_1 = SNG.A199()
        var_1 = YEAR(a199_1)
        return var_1

@register(SNG)
class C199():
    # 'SNG'!C199
    value = 36.73
    formula = "=VLOOKUP(B199,$H:$I,2,FALSE)"
    @eval_fn
    def C199():
        b199_1 = SNG.B199()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b199_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A200():
    # 'SNG'!A200
    value = 39675
    isdatetime = True

@register(SNG)
class B200():
    # 'SNG'!B200
    value = 2008
    formula = "=YEAR(A200)"
    @eval_fn
    def B200():
        a200_1 = SNG.A200()
        var_1 = YEAR(a200_1)
        return var_1

@register(SNG)
class C200():
    # 'SNG'!C200
    value = 36.73
    formula = "=VLOOKUP(B200,$H:$I,2,FALSE)"
    @eval_fn
    def C200():
        b200_1 = SNG.B200()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b200_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A201():
    # 'SNG'!A201
    value = 39706
    isdatetime = True

@register(SNG)
class B201():
    # 'SNG'!B201
    value = 2008
    formula = "=YEAR(A201)"
    @eval_fn
    def B201():
        a201_1 = SNG.A201()
        var_1 = YEAR(a201_1)
        return var_1

@register(SNG)
class C201():
    # 'SNG'!C201
    value = 36.73
    formula = "=VLOOKUP(B201,$H:$I,2,FALSE)"
    @eval_fn
    def C201():
        b201_1 = SNG.B201()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b201_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A202():
    # 'SNG'!A202
    value = 39736
    isdatetime = True

@register(SNG)
class B202():
    # 'SNG'!B202
    value = 2008
    formula = "=YEAR(A202)"
    @eval_fn
    def B202():
        a202_1 = SNG.A202()
        var_1 = YEAR(a202_1)
        return var_1

@register(SNG)
class C202():
    # 'SNG'!C202
    value = 36.73
    formula = "=VLOOKUP(B202,$H:$I,2,FALSE)"
    @eval_fn
    def C202():
        b202_1 = SNG.B202()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b202_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A203():
    # 'SNG'!A203
    value = 39767
    isdatetime = True

@register(SNG)
class B203():
    # 'SNG'!B203
    value = 2008
    formula = "=YEAR(A203)"
    @eval_fn
    def B203():
        a203_1 = SNG.A203()
        var_1 = YEAR(a203_1)
        return var_1

@register(SNG)
class C203():
    # 'SNG'!C203
    value = 36.73
    formula = "=VLOOKUP(B203,$H:$I,2,FALSE)"
    @eval_fn
    def C203():
        b203_1 = SNG.B203()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b203_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A204():
    # 'SNG'!A204
    value = 39797
    isdatetime = True

@register(SNG)
class B204():
    # 'SNG'!B204
    value = 2008
    formula = "=YEAR(A204)"
    @eval_fn
    def B204():
        a204_1 = SNG.A204()
        var_1 = YEAR(a204_1)
        return var_1

@register(SNG)
class C204():
    # 'SNG'!C204
    value = 36.73
    formula = "=VLOOKUP(B204,$H:$I,2,FALSE)"
    @eval_fn
    def C204():
        b204_1 = SNG.B204()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b204_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A205():
    # 'SNG'!A205
    value = 39828
    isdatetime = True

@register(SNG)
class B205():
    # 'SNG'!B205
    value = 2009
    formula = "=YEAR(A205)"
    @eval_fn
    def B205():
        a205_1 = SNG.A205()
        var_1 = YEAR(a205_1)
        return var_1

@register(SNG)
class C205():
    # 'SNG'!C205
    value = 28.82
    formula = "=VLOOKUP(B205,$H:$I,2,FALSE)"
    @eval_fn
    def C205():
        b205_1 = SNG.B205()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b205_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A206():
    # 'SNG'!A206
    value = 39859
    isdatetime = True

@register(SNG)
class B206():
    # 'SNG'!B206
    value = 2009
    formula = "=YEAR(A206)"
    @eval_fn
    def B206():
        a206_1 = SNG.A206()
        var_1 = YEAR(a206_1)
        return var_1

@register(SNG)
class C206():
    # 'SNG'!C206
    value = 28.82
    formula = "=VLOOKUP(B206,$H:$I,2,FALSE)"
    @eval_fn
    def C206():
        b206_1 = SNG.B206()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b206_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A207():
    # 'SNG'!A207
    value = 39887
    isdatetime = True

@register(SNG)
class B207():
    # 'SNG'!B207
    value = 2009
    formula = "=YEAR(A207)"
    @eval_fn
    def B207():
        a207_1 = SNG.A207()
        var_1 = YEAR(a207_1)
        return var_1

@register(SNG)
class C207():
    # 'SNG'!C207
    value = 28.82
    formula = "=VLOOKUP(B207,$H:$I,2,FALSE)"
    @eval_fn
    def C207():
        b207_1 = SNG.B207()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b207_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A208():
    # 'SNG'!A208
    value = 39918
    isdatetime = True

@register(SNG)
class B208():
    # 'SNG'!B208
    value = 2009
    formula = "=YEAR(A208)"
    @eval_fn
    def B208():
        a208_1 = SNG.A208()
        var_1 = YEAR(a208_1)
        return var_1

@register(SNG)
class C208():
    # 'SNG'!C208
    value = 28.82
    formula = "=VLOOKUP(B208,$H:$I,2,FALSE)"
    @eval_fn
    def C208():
        b208_1 = SNG.B208()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b208_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A209():
    # 'SNG'!A209
    value = 39948
    isdatetime = True

@register(SNG)
class B209():
    # 'SNG'!B209
    value = 2009
    formula = "=YEAR(A209)"
    @eval_fn
    def B209():
        a209_1 = SNG.A209()
        var_1 = YEAR(a209_1)
        return var_1

@register(SNG)
class C209():
    # 'SNG'!C209
    value = 28.82
    formula = "=VLOOKUP(B209,$H:$I,2,FALSE)"
    @eval_fn
    def C209():
        b209_1 = SNG.B209()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b209_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A210():
    # 'SNG'!A210
    value = 39979
    isdatetime = True

@register(SNG)
class B210():
    # 'SNG'!B210
    value = 2009
    formula = "=YEAR(A210)"
    @eval_fn
    def B210():
        a210_1 = SNG.A210()
        var_1 = YEAR(a210_1)
        return var_1

@register(SNG)
class C210():
    # 'SNG'!C210
    value = 28.82
    formula = "=VLOOKUP(B210,$H:$I,2,FALSE)"
    @eval_fn
    def C210():
        b210_1 = SNG.B210()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b210_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A211():
    # 'SNG'!A211
    value = 40009
    isdatetime = True

@register(SNG)
class B211():
    # 'SNG'!B211
    value = 2009
    formula = "=YEAR(A211)"
    @eval_fn
    def B211():
        a211_1 = SNG.A211()
        var_1 = YEAR(a211_1)
        return var_1

@register(SNG)
class C211():
    # 'SNG'!C211
    value = 28.82
    formula = "=VLOOKUP(B211,$H:$I,2,FALSE)"
    @eval_fn
    def C211():
        b211_1 = SNG.B211()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b211_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A212():
    # 'SNG'!A212
    value = 40040
    isdatetime = True

@register(SNG)
class B212():
    # 'SNG'!B212
    value = 2009
    formula = "=YEAR(A212)"
    @eval_fn
    def B212():
        a212_1 = SNG.A212()
        var_1 = YEAR(a212_1)
        return var_1

@register(SNG)
class C212():
    # 'SNG'!C212
    value = 28.82
    formula = "=VLOOKUP(B212,$H:$I,2,FALSE)"
    @eval_fn
    def C212():
        b212_1 = SNG.B212()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b212_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A213():
    # 'SNG'!A213
    value = 40071
    isdatetime = True

@register(SNG)
class B213():
    # 'SNG'!B213
    value = 2009
    formula = "=YEAR(A213)"
    @eval_fn
    def B213():
        a213_1 = SNG.A213()
        var_1 = YEAR(a213_1)
        return var_1

@register(SNG)
class C213():
    # 'SNG'!C213
    value = 28.82
    formula = "=VLOOKUP(B213,$H:$I,2,FALSE)"
    @eval_fn
    def C213():
        b213_1 = SNG.B213()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b213_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A214():
    # 'SNG'!A214
    value = 40101
    isdatetime = True

@register(SNG)
class B214():
    # 'SNG'!B214
    value = 2009
    formula = "=YEAR(A214)"
    @eval_fn
    def B214():
        a214_1 = SNG.A214()
        var_1 = YEAR(a214_1)
        return var_1

@register(SNG)
class C214():
    # 'SNG'!C214
    value = 28.82
    formula = "=VLOOKUP(B214,$H:$I,2,FALSE)"
    @eval_fn
    def C214():
        b214_1 = SNG.B214()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b214_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A215():
    # 'SNG'!A215
    value = 40132
    isdatetime = True

@register(SNG)
class B215():
    # 'SNG'!B215
    value = 2009
    formula = "=YEAR(A215)"
    @eval_fn
    def B215():
        a215_1 = SNG.A215()
        var_1 = YEAR(a215_1)
        return var_1

@register(SNG)
class C215():
    # 'SNG'!C215
    value = 28.82
    formula = "=VLOOKUP(B215,$H:$I,2,FALSE)"
    @eval_fn
    def C215():
        b215_1 = SNG.B215()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b215_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A216():
    # 'SNG'!A216
    value = 40162
    isdatetime = True

@register(SNG)
class B216():
    # 'SNG'!B216
    value = 2009
    formula = "=YEAR(A216)"
    @eval_fn
    def B216():
        a216_1 = SNG.A216()
        var_1 = YEAR(a216_1)
        return var_1

@register(SNG)
class C216():
    # 'SNG'!C216
    value = 28.82
    formula = "=VLOOKUP(B216,$H:$I,2,FALSE)"
    @eval_fn
    def C216():
        b216_1 = SNG.B216()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b216_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A217():
    # 'SNG'!A217
    value = 40193
    isdatetime = True

@register(SNG)
class B217():
    # 'SNG'!B217
    value = 2010
    formula = "=YEAR(A217)"
    @eval_fn
    def B217():
        a217_1 = SNG.A217()
        var_1 = YEAR(a217_1)
        return var_1

@register(SNG)
class C217():
    # 'SNG'!C217
    value = 35.29
    formula = "=VLOOKUP(B217,$H:$I,2,FALSE)"
    @eval_fn
    def C217():
        b217_1 = SNG.B217()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b217_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A218():
    # 'SNG'!A218
    value = 40224
    isdatetime = True

@register(SNG)
class B218():
    # 'SNG'!B218
    value = 2010
    formula = "=YEAR(A218)"
    @eval_fn
    def B218():
        a218_1 = SNG.A218()
        var_1 = YEAR(a218_1)
        return var_1

@register(SNG)
class C218():
    # 'SNG'!C218
    value = 35.29
    formula = "=VLOOKUP(B218,$H:$I,2,FALSE)"
    @eval_fn
    def C218():
        b218_1 = SNG.B218()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b218_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A219():
    # 'SNG'!A219
    value = 40252
    isdatetime = True

@register(SNG)
class B219():
    # 'SNG'!B219
    value = 2010
    formula = "=YEAR(A219)"
    @eval_fn
    def B219():
        a219_1 = SNG.A219()
        var_1 = YEAR(a219_1)
        return var_1

@register(SNG)
class C219():
    # 'SNG'!C219
    value = 35.29
    formula = "=VLOOKUP(B219,$H:$I,2,FALSE)"
    @eval_fn
    def C219():
        b219_1 = SNG.B219()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b219_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A220():
    # 'SNG'!A220
    value = 40283
    isdatetime = True

@register(SNG)
class B220():
    # 'SNG'!B220
    value = 2010
    formula = "=YEAR(A220)"
    @eval_fn
    def B220():
        a220_1 = SNG.A220()
        var_1 = YEAR(a220_1)
        return var_1

@register(SNG)
class C220():
    # 'SNG'!C220
    value = 35.29
    formula = "=VLOOKUP(B220,$H:$I,2,FALSE)"
    @eval_fn
    def C220():
        b220_1 = SNG.B220()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b220_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A221():
    # 'SNG'!A221
    value = 40313
    isdatetime = True

@register(SNG)
class B221():
    # 'SNG'!B221
    value = 2010
    formula = "=YEAR(A221)"
    @eval_fn
    def B221():
        a221_1 = SNG.A221()
        var_1 = YEAR(a221_1)
        return var_1

@register(SNG)
class C221():
    # 'SNG'!C221
    value = 35.29
    formula = "=VLOOKUP(B221,$H:$I,2,FALSE)"
    @eval_fn
    def C221():
        b221_1 = SNG.B221()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b221_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A222():
    # 'SNG'!A222
    value = 40344
    isdatetime = True

@register(SNG)
class B222():
    # 'SNG'!B222
    value = 2010
    formula = "=YEAR(A222)"
    @eval_fn
    def B222():
        a222_1 = SNG.A222()
        var_1 = YEAR(a222_1)
        return var_1

@register(SNG)
class C222():
    # 'SNG'!C222
    value = 35.29
    formula = "=VLOOKUP(B222,$H:$I,2,FALSE)"
    @eval_fn
    def C222():
        b222_1 = SNG.B222()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b222_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A223():
    # 'SNG'!A223
    value = 40374
    isdatetime = True

@register(SNG)
class B223():
    # 'SNG'!B223
    value = 2010
    formula = "=YEAR(A223)"
    @eval_fn
    def B223():
        a223_1 = SNG.A223()
        var_1 = YEAR(a223_1)
        return var_1

@register(SNG)
class C223():
    # 'SNG'!C223
    value = 35.29
    formula = "=VLOOKUP(B223,$H:$I,2,FALSE)"
    @eval_fn
    def C223():
        b223_1 = SNG.B223()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b223_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A224():
    # 'SNG'!A224
    value = 40405
    isdatetime = True

@register(SNG)
class B224():
    # 'SNG'!B224
    value = 2010
    formula = "=YEAR(A224)"
    @eval_fn
    def B224():
        a224_1 = SNG.A224()
        var_1 = YEAR(a224_1)
        return var_1

@register(SNG)
class C224():
    # 'SNG'!C224
    value = 35.29
    formula = "=VLOOKUP(B224,$H:$I,2,FALSE)"
    @eval_fn
    def C224():
        b224_1 = SNG.B224()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b224_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A225():
    # 'SNG'!A225
    value = 40436
    isdatetime = True

@register(SNG)
class B225():
    # 'SNG'!B225
    value = 2010
    formula = "=YEAR(A225)"
    @eval_fn
    def B225():
        a225_1 = SNG.A225()
        var_1 = YEAR(a225_1)
        return var_1

@register(SNG)
class C225():
    # 'SNG'!C225
    value = 35.29
    formula = "=VLOOKUP(B225,$H:$I,2,FALSE)"
    @eval_fn
    def C225():
        b225_1 = SNG.B225()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b225_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A226():
    # 'SNG'!A226
    value = 40466
    isdatetime = True

@register(SNG)
class B226():
    # 'SNG'!B226
    value = 2010
    formula = "=YEAR(A226)"
    @eval_fn
    def B226():
        a226_1 = SNG.A226()
        var_1 = YEAR(a226_1)
        return var_1

@register(SNG)
class C226():
    # 'SNG'!C226
    value = 35.29
    formula = "=VLOOKUP(B226,$H:$I,2,FALSE)"
    @eval_fn
    def C226():
        b226_1 = SNG.B226()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b226_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A227():
    # 'SNG'!A227
    value = 40497
    isdatetime = True

@register(SNG)
class B227():
    # 'SNG'!B227
    value = 2010
    formula = "=YEAR(A227)"
    @eval_fn
    def B227():
        a227_1 = SNG.A227()
        var_1 = YEAR(a227_1)
        return var_1

@register(SNG)
class C227():
    # 'SNG'!C227
    value = 35.29
    formula = "=VLOOKUP(B227,$H:$I,2,FALSE)"
    @eval_fn
    def C227():
        b227_1 = SNG.B227()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b227_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A228():
    # 'SNG'!A228
    value = 40527
    isdatetime = True

@register(SNG)
class B228():
    # 'SNG'!B228
    value = 2010
    formula = "=YEAR(A228)"
    @eval_fn
    def B228():
        a228_1 = SNG.A228()
        var_1 = YEAR(a228_1)
        return var_1

@register(SNG)
class C228():
    # 'SNG'!C228
    value = 35.29
    formula = "=VLOOKUP(B228,$H:$I,2,FALSE)"
    @eval_fn
    def C228():
        b228_1 = SNG.B228()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b228_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A229():
    # 'SNG'!A229
    value = 40558
    isdatetime = True

@register(SNG)
class B229():
    # 'SNG'!B229
    value = 2011
    formula = "=YEAR(A229)"
    @eval_fn
    def B229():
        a229_1 = SNG.A229()
        var_1 = YEAR(a229_1)
        return var_1

@register(SNG)
class C229():
    # 'SNG'!C229
    value = 43.43
    formula = "=VLOOKUP(B229,$H:$I,2,FALSE)"
    @eval_fn
    def C229():
        b229_1 = SNG.B229()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b229_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A230():
    # 'SNG'!A230
    value = 40589
    isdatetime = True

@register(SNG)
class B230():
    # 'SNG'!B230
    value = 2011
    formula = "=YEAR(A230)"
    @eval_fn
    def B230():
        a230_1 = SNG.A230()
        var_1 = YEAR(a230_1)
        return var_1

@register(SNG)
class C230():
    # 'SNG'!C230
    value = 43.43
    formula = "=VLOOKUP(B230,$H:$I,2,FALSE)"
    @eval_fn
    def C230():
        b230_1 = SNG.B230()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b230_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A231():
    # 'SNG'!A231
    value = 40617
    isdatetime = True

@register(SNG)
class B231():
    # 'SNG'!B231
    value = 2011
    formula = "=YEAR(A231)"
    @eval_fn
    def B231():
        a231_1 = SNG.A231()
        var_1 = YEAR(a231_1)
        return var_1

@register(SNG)
class C231():
    # 'SNG'!C231
    value = 43.43
    formula = "=VLOOKUP(B231,$H:$I,2,FALSE)"
    @eval_fn
    def C231():
        b231_1 = SNG.B231()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b231_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A232():
    # 'SNG'!A232
    value = 40648
    isdatetime = True

@register(SNG)
class B232():
    # 'SNG'!B232
    value = 2011
    formula = "=YEAR(A232)"
    @eval_fn
    def B232():
        a232_1 = SNG.A232()
        var_1 = YEAR(a232_1)
        return var_1

@register(SNG)
class C232():
    # 'SNG'!C232
    value = 43.43
    formula = "=VLOOKUP(B232,$H:$I,2,FALSE)"
    @eval_fn
    def C232():
        b232_1 = SNG.B232()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b232_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A233():
    # 'SNG'!A233
    value = 40678
    isdatetime = True

@register(SNG)
class B233():
    # 'SNG'!B233
    value = 2011
    formula = "=YEAR(A233)"
    @eval_fn
    def B233():
        a233_1 = SNG.A233()
        var_1 = YEAR(a233_1)
        return var_1

@register(SNG)
class C233():
    # 'SNG'!C233
    value = 43.43
    formula = "=VLOOKUP(B233,$H:$I,2,FALSE)"
    @eval_fn
    def C233():
        b233_1 = SNG.B233()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b233_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A234():
    # 'SNG'!A234
    value = 40709
    isdatetime = True

@register(SNG)
class B234():
    # 'SNG'!B234
    value = 2011
    formula = "=YEAR(A234)"
    @eval_fn
    def B234():
        a234_1 = SNG.A234()
        var_1 = YEAR(a234_1)
        return var_1

@register(SNG)
class C234():
    # 'SNG'!C234
    value = 43.43
    formula = "=VLOOKUP(B234,$H:$I,2,FALSE)"
    @eval_fn
    def C234():
        b234_1 = SNG.B234()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b234_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A235():
    # 'SNG'!A235
    value = 40739
    isdatetime = True

@register(SNG)
class B235():
    # 'SNG'!B235
    value = 2011
    formula = "=YEAR(A235)"
    @eval_fn
    def B235():
        a235_1 = SNG.A235()
        var_1 = YEAR(a235_1)
        return var_1

@register(SNG)
class C235():
    # 'SNG'!C235
    value = 43.43
    formula = "=VLOOKUP(B235,$H:$I,2,FALSE)"
    @eval_fn
    def C235():
        b235_1 = SNG.B235()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b235_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A236():
    # 'SNG'!A236
    value = 40770
    isdatetime = True

@register(SNG)
class B236():
    # 'SNG'!B236
    value = 2011
    formula = "=YEAR(A236)"
    @eval_fn
    def B236():
        a236_1 = SNG.A236()
        var_1 = YEAR(a236_1)
        return var_1

@register(SNG)
class C236():
    # 'SNG'!C236
    value = 43.43
    formula = "=VLOOKUP(B236,$H:$I,2,FALSE)"
    @eval_fn
    def C236():
        b236_1 = SNG.B236()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b236_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A237():
    # 'SNG'!A237
    value = 40801
    isdatetime = True

@register(SNG)
class B237():
    # 'SNG'!B237
    value = 2011
    formula = "=YEAR(A237)"
    @eval_fn
    def B237():
        a237_1 = SNG.A237()
        var_1 = YEAR(a237_1)
        return var_1

@register(SNG)
class C237():
    # 'SNG'!C237
    value = 43.43
    formula = "=VLOOKUP(B237,$H:$I,2,FALSE)"
    @eval_fn
    def C237():
        b237_1 = SNG.B237()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b237_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A238():
    # 'SNG'!A238
    value = 40831
    isdatetime = True

@register(SNG)
class B238():
    # 'SNG'!B238
    value = 2011
    formula = "=YEAR(A238)"
    @eval_fn
    def B238():
        a238_1 = SNG.A238()
        var_1 = YEAR(a238_1)
        return var_1

@register(SNG)
class C238():
    # 'SNG'!C238
    value = 43.43
    formula = "=VLOOKUP(B238,$H:$I,2,FALSE)"
    @eval_fn
    def C238():
        b238_1 = SNG.B238()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b238_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A239():
    # 'SNG'!A239
    value = 40862
    isdatetime = True

@register(SNG)
class B239():
    # 'SNG'!B239
    value = 2011
    formula = "=YEAR(A239)"
    @eval_fn
    def B239():
        a239_1 = SNG.A239()
        var_1 = YEAR(a239_1)
        return var_1

@register(SNG)
class C239():
    # 'SNG'!C239
    value = 43.43
    formula = "=VLOOKUP(B239,$H:$I,2,FALSE)"
    @eval_fn
    def C239():
        b239_1 = SNG.B239()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b239_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A240():
    # 'SNG'!A240
    value = 40892
    isdatetime = True

@register(SNG)
class B240():
    # 'SNG'!B240
    value = 2011
    formula = "=YEAR(A240)"
    @eval_fn
    def B240():
        a240_1 = SNG.A240()
        var_1 = YEAR(a240_1)
        return var_1

@register(SNG)
class C240():
    # 'SNG'!C240
    value = 43.43
    formula = "=VLOOKUP(B240,$H:$I,2,FALSE)"
    @eval_fn
    def C240():
        b240_1 = SNG.B240()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b240_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A241():
    # 'SNG'!A241
    value = 40923
    isdatetime = True

@register(SNG)
class B241():
    # 'SNG'!B241
    value = 2012
    formula = "=YEAR(A241)"
    @eval_fn
    def B241():
        a241_1 = SNG.A241()
        var_1 = YEAR(a241_1)
        return var_1

@register(SNG)
class C241():
    # 'SNG'!C241
    value = 44.19
    formula = "=VLOOKUP(B241,$H:$I,2,FALSE)"
    @eval_fn
    def C241():
        b241_1 = SNG.B241()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b241_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A242():
    # 'SNG'!A242
    value = 40954
    isdatetime = True

@register(SNG)
class B242():
    # 'SNG'!B242
    value = 2012
    formula = "=YEAR(A242)"
    @eval_fn
    def B242():
        a242_1 = SNG.A242()
        var_1 = YEAR(a242_1)
        return var_1

@register(SNG)
class C242():
    # 'SNG'!C242
    value = 44.19
    formula = "=VLOOKUP(B242,$H:$I,2,FALSE)"
    @eval_fn
    def C242():
        b242_1 = SNG.B242()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b242_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A243():
    # 'SNG'!A243
    value = 40983
    isdatetime = True

@register(SNG)
class B243():
    # 'SNG'!B243
    value = 2012
    formula = "=YEAR(A243)"
    @eval_fn
    def B243():
        a243_1 = SNG.A243()
        var_1 = YEAR(a243_1)
        return var_1

@register(SNG)
class C243():
    # 'SNG'!C243
    value = 44.19
    formula = "=VLOOKUP(B243,$H:$I,2,FALSE)"
    @eval_fn
    def C243():
        b243_1 = SNG.B243()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b243_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A244():
    # 'SNG'!A244
    value = 41014
    isdatetime = True

@register(SNG)
class B244():
    # 'SNG'!B244
    value = 2012
    formula = "=YEAR(A244)"
    @eval_fn
    def B244():
        a244_1 = SNG.A244()
        var_1 = YEAR(a244_1)
        return var_1

@register(SNG)
class C244():
    # 'SNG'!C244
    value = 44.19
    formula = "=VLOOKUP(B244,$H:$I,2,FALSE)"
    @eval_fn
    def C244():
        b244_1 = SNG.B244()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b244_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A245():
    # 'SNG'!A245
    value = 41044
    isdatetime = True

@register(SNG)
class B245():
    # 'SNG'!B245
    value = 2012
    formula = "=YEAR(A245)"
    @eval_fn
    def B245():
        a245_1 = SNG.A245()
        var_1 = YEAR(a245_1)
        return var_1

@register(SNG)
class C245():
    # 'SNG'!C245
    value = 44.19
    formula = "=VLOOKUP(B245,$H:$I,2,FALSE)"
    @eval_fn
    def C245():
        b245_1 = SNG.B245()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b245_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A246():
    # 'SNG'!A246
    value = 41075
    isdatetime = True

@register(SNG)
class B246():
    # 'SNG'!B246
    value = 2012
    formula = "=YEAR(A246)"
    @eval_fn
    def B246():
        a246_1 = SNG.A246()
        var_1 = YEAR(a246_1)
        return var_1

@register(SNG)
class C246():
    # 'SNG'!C246
    value = 44.19
    formula = "=VLOOKUP(B246,$H:$I,2,FALSE)"
    @eval_fn
    def C246():
        b246_1 = SNG.B246()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b246_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A247():
    # 'SNG'!A247
    value = 41105
    isdatetime = True

@register(SNG)
class B247():
    # 'SNG'!B247
    value = 2012
    formula = "=YEAR(A247)"
    @eval_fn
    def B247():
        a247_1 = SNG.A247()
        var_1 = YEAR(a247_1)
        return var_1

@register(SNG)
class C247():
    # 'SNG'!C247
    value = 44.19
    formula = "=VLOOKUP(B247,$H:$I,2,FALSE)"
    @eval_fn
    def C247():
        b247_1 = SNG.B247()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b247_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A248():
    # 'SNG'!A248
    value = 41136
    isdatetime = True

@register(SNG)
class B248():
    # 'SNG'!B248
    value = 2012
    formula = "=YEAR(A248)"
    @eval_fn
    def B248():
        a248_1 = SNG.A248()
        var_1 = YEAR(a248_1)
        return var_1

@register(SNG)
class C248():
    # 'SNG'!C248
    value = 44.19
    formula = "=VLOOKUP(B248,$H:$I,2,FALSE)"
    @eval_fn
    def C248():
        b248_1 = SNG.B248()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b248_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A249():
    # 'SNG'!A249
    value = 41167
    isdatetime = True

@register(SNG)
class B249():
    # 'SNG'!B249
    value = 2012
    formula = "=YEAR(A249)"
    @eval_fn
    def B249():
        a249_1 = SNG.A249()
        var_1 = YEAR(a249_1)
        return var_1

@register(SNG)
class C249():
    # 'SNG'!C249
    value = 44.19
    formula = "=VLOOKUP(B249,$H:$I,2,FALSE)"
    @eval_fn
    def C249():
        b249_1 = SNG.B249()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b249_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A250():
    # 'SNG'!A250
    value = 41197
    isdatetime = True

@register(SNG)
class B250():
    # 'SNG'!B250
    value = 2012
    formula = "=YEAR(A250)"
    @eval_fn
    def B250():
        a250_1 = SNG.A250()
        var_1 = YEAR(a250_1)
        return var_1

@register(SNG)
class C250():
    # 'SNG'!C250
    value = 44.19
    formula = "=VLOOKUP(B250,$H:$I,2,FALSE)"
    @eval_fn
    def C250():
        b250_1 = SNG.B250()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b250_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A251():
    # 'SNG'!A251
    value = 41228
    isdatetime = True

@register(SNG)
class B251():
    # 'SNG'!B251
    value = 2012
    formula = "=YEAR(A251)"
    @eval_fn
    def B251():
        a251_1 = SNG.A251()
        var_1 = YEAR(a251_1)
        return var_1

@register(SNG)
class C251():
    # 'SNG'!C251
    value = 44.19
    formula = "=VLOOKUP(B251,$H:$I,2,FALSE)"
    @eval_fn
    def C251():
        b251_1 = SNG.B251()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b251_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A252():
    # 'SNG'!A252
    value = 41258
    isdatetime = True

@register(SNG)
class B252():
    # 'SNG'!B252
    value = 2012
    formula = "=YEAR(A252)"
    @eval_fn
    def B252():
        a252_1 = SNG.A252()
        var_1 = YEAR(a252_1)
        return var_1

@register(SNG)
class C252():
    # 'SNG'!C252
    value = 44.19
    formula = "=VLOOKUP(B252,$H:$I,2,FALSE)"
    @eval_fn
    def C252():
        b252_1 = SNG.B252()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b252_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A253():
    # 'SNG'!A253
    value = 41289
    isdatetime = True

@register(SNG)
class B253():
    # 'SNG'!B253
    value = 2013
    formula = "=YEAR(A253)"
    @eval_fn
    def B253():
        a253_1 = SNG.A253()
        var_1 = YEAR(a253_1)
        return var_1

@register(SNG)
class C253():
    # 'SNG'!C253
    value = 41.19
    formula = "=VLOOKUP(B253,$H:$I,2,FALSE)"
    @eval_fn
    def C253():
        b253_1 = SNG.B253()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b253_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A254():
    # 'SNG'!A254
    value = 41320
    isdatetime = True

@register(SNG)
class B254():
    # 'SNG'!B254
    value = 2013
    formula = "=YEAR(A254)"
    @eval_fn
    def B254():
        a254_1 = SNG.A254()
        var_1 = YEAR(a254_1)
        return var_1

@register(SNG)
class C254():
    # 'SNG'!C254
    value = 41.19
    formula = "=VLOOKUP(B254,$H:$I,2,FALSE)"
    @eval_fn
    def C254():
        b254_1 = SNG.B254()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b254_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A255():
    # 'SNG'!A255
    value = 41348
    isdatetime = True

@register(SNG)
class B255():
    # 'SNG'!B255
    value = 2013
    formula = "=YEAR(A255)"
    @eval_fn
    def B255():
        a255_1 = SNG.A255()
        var_1 = YEAR(a255_1)
        return var_1

@register(SNG)
class C255():
    # 'SNG'!C255
    value = 41.19
    formula = "=VLOOKUP(B255,$H:$I,2,FALSE)"
    @eval_fn
    def C255():
        b255_1 = SNG.B255()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b255_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A256():
    # 'SNG'!A256
    value = 41379
    isdatetime = True

@register(SNG)
class B256():
    # 'SNG'!B256
    value = 2013
    formula = "=YEAR(A256)"
    @eval_fn
    def B256():
        a256_1 = SNG.A256()
        var_1 = YEAR(a256_1)
        return var_1

@register(SNG)
class C256():
    # 'SNG'!C256
    value = 41.19
    formula = "=VLOOKUP(B256,$H:$I,2,FALSE)"
    @eval_fn
    def C256():
        b256_1 = SNG.B256()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b256_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A257():
    # 'SNG'!A257
    value = 41409
    isdatetime = True

@register(SNG)
class B257():
    # 'SNG'!B257
    value = 2013
    formula = "=YEAR(A257)"
    @eval_fn
    def B257():
        a257_1 = SNG.A257()
        var_1 = YEAR(a257_1)
        return var_1

@register(SNG)
class C257():
    # 'SNG'!C257
    value = 41.19
    formula = "=VLOOKUP(B257,$H:$I,2,FALSE)"
    @eval_fn
    def C257():
        b257_1 = SNG.B257()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b257_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A258():
    # 'SNG'!A258
    value = 41440
    isdatetime = True

@register(SNG)
class B258():
    # 'SNG'!B258
    value = 2013
    formula = "=YEAR(A258)"
    @eval_fn
    def B258():
        a258_1 = SNG.A258()
        var_1 = YEAR(a258_1)
        return var_1

@register(SNG)
class C258():
    # 'SNG'!C258
    value = 41.19
    formula = "=VLOOKUP(B258,$H:$I,2,FALSE)"
    @eval_fn
    def C258():
        b258_1 = SNG.B258()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b258_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A259():
    # 'SNG'!A259
    value = 41470
    isdatetime = True

@register(SNG)
class B259():
    # 'SNG'!B259
    value = 2013
    formula = "=YEAR(A259)"
    @eval_fn
    def B259():
        a259_1 = SNG.A259()
        var_1 = YEAR(a259_1)
        return var_1

@register(SNG)
class C259():
    # 'SNG'!C259
    value = 41.19
    formula = "=VLOOKUP(B259,$H:$I,2,FALSE)"
    @eval_fn
    def C259():
        b259_1 = SNG.B259()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b259_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A260():
    # 'SNG'!A260
    value = 41501
    isdatetime = True

@register(SNG)
class B260():
    # 'SNG'!B260
    value = 2013
    formula = "=YEAR(A260)"
    @eval_fn
    def B260():
        a260_1 = SNG.A260()
        var_1 = YEAR(a260_1)
        return var_1

@register(SNG)
class C260():
    # 'SNG'!C260
    value = 41.19
    formula = "=VLOOKUP(B260,$H:$I,2,FALSE)"
    @eval_fn
    def C260():
        b260_1 = SNG.B260()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b260_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A261():
    # 'SNG'!A261
    value = 41532
    isdatetime = True

@register(SNG)
class B261():
    # 'SNG'!B261
    value = 2013
    formula = "=YEAR(A261)"
    @eval_fn
    def B261():
        a261_1 = SNG.A261()
        var_1 = YEAR(a261_1)
        return var_1

@register(SNG)
class C261():
    # 'SNG'!C261
    value = 41.19
    formula = "=VLOOKUP(B261,$H:$I,2,FALSE)"
    @eval_fn
    def C261():
        b261_1 = SNG.B261()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b261_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A262():
    # 'SNG'!A262
    value = 41562
    isdatetime = True

@register(SNG)
class B262():
    # 'SNG'!B262
    value = 2013
    formula = "=YEAR(A262)"
    @eval_fn
    def B262():
        a262_1 = SNG.A262()
        var_1 = YEAR(a262_1)
        return var_1

@register(SNG)
class C262():
    # 'SNG'!C262
    value = 41.19
    formula = "=VLOOKUP(B262,$H:$I,2,FALSE)"
    @eval_fn
    def C262():
        b262_1 = SNG.B262()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b262_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A263():
    # 'SNG'!A263
    value = 41593
    isdatetime = True

@register(SNG)
class B263():
    # 'SNG'!B263
    value = 2013
    formula = "=YEAR(A263)"
    @eval_fn
    def B263():
        a263_1 = SNG.A263()
        var_1 = YEAR(a263_1)
        return var_1

@register(SNG)
class C263():
    # 'SNG'!C263
    value = 41.19
    formula = "=VLOOKUP(B263,$H:$I,2,FALSE)"
    @eval_fn
    def C263():
        b263_1 = SNG.B263()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b263_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A264():
    # 'SNG'!A264
    value = 41623
    isdatetime = True

@register(SNG)
class B264():
    # 'SNG'!B264
    value = 2013
    formula = "=YEAR(A264)"
    @eval_fn
    def B264():
        a264_1 = SNG.A264()
        var_1 = YEAR(a264_1)
        return var_1

@register(SNG)
class C264():
    # 'SNG'!C264
    value = 41.19
    formula = "=VLOOKUP(B264,$H:$I,2,FALSE)"
    @eval_fn
    def C264():
        b264_1 = SNG.B264()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b264_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A265():
    # 'SNG'!A265
    value = 41654
    isdatetime = True

@register(SNG)
class B265():
    # 'SNG'!B265
    value = 2014
    formula = "=YEAR(A265)"
    @eval_fn
    def B265():
        a265_1 = SNG.A265()
        var_1 = YEAR(a265_1)
        return var_1

@register(SNG)
class C265():
    # 'SNG'!C265
    value = "#N/A"
    formula = "=VLOOKUP(B265,$H:$I,2,FALSE)"
    @eval_fn
    def C265():
        b265_1 = SNG.B265()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b265_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A266():
    # 'SNG'!A266
    value = 41685
    isdatetime = True

@register(SNG)
class B266():
    # 'SNG'!B266
    value = 2014
    formula = "=YEAR(A266)"
    @eval_fn
    def B266():
        a266_1 = SNG.A266()
        var_1 = YEAR(a266_1)
        return var_1

@register(SNG)
class C266():
    # 'SNG'!C266
    value = "#N/A"
    formula = "=VLOOKUP(B266,$H:$I,2,FALSE)"
    @eval_fn
    def C266():
        b266_1 = SNG.B266()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b266_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A267():
    # 'SNG'!A267
    value = 41713
    isdatetime = True

@register(SNG)
class B267():
    # 'SNG'!B267
    value = 2014
    formula = "=YEAR(A267)"
    @eval_fn
    def B267():
        a267_1 = SNG.A267()
        var_1 = YEAR(a267_1)
        return var_1

@register(SNG)
class C267():
    # 'SNG'!C267
    value = "#N/A"
    formula = "=VLOOKUP(B267,$H:$I,2,FALSE)"
    @eval_fn
    def C267():
        b267_1 = SNG.B267()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b267_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A268():
    # 'SNG'!A268
    value = 41744
    isdatetime = True

@register(SNG)
class B268():
    # 'SNG'!B268
    value = 2014
    formula = "=YEAR(A268)"
    @eval_fn
    def B268():
        a268_1 = SNG.A268()
        var_1 = YEAR(a268_1)
        return var_1

@register(SNG)
class C268():
    # 'SNG'!C268
    value = "#N/A"
    formula = "=VLOOKUP(B268,$H:$I,2,FALSE)"
    @eval_fn
    def C268():
        b268_1 = SNG.B268()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b268_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A269():
    # 'SNG'!A269
    value = 41774
    isdatetime = True

@register(SNG)
class B269():
    # 'SNG'!B269
    value = 2014
    formula = "=YEAR(A269)"
    @eval_fn
    def B269():
        a269_1 = SNG.A269()
        var_1 = YEAR(a269_1)
        return var_1

@register(SNG)
class C269():
    # 'SNG'!C269
    value = "#N/A"
    formula = "=VLOOKUP(B269,$H:$I,2,FALSE)"
    @eval_fn
    def C269():
        b269_1 = SNG.B269()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b269_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A270():
    # 'SNG'!A270
    value = 41805
    isdatetime = True

@register(SNG)
class B270():
    # 'SNG'!B270
    value = 2014
    formula = "=YEAR(A270)"
    @eval_fn
    def B270():
        a270_1 = SNG.A270()
        var_1 = YEAR(a270_1)
        return var_1

@register(SNG)
class C270():
    # 'SNG'!C270
    value = "#N/A"
    formula = "=VLOOKUP(B270,$H:$I,2,FALSE)"
    @eval_fn
    def C270():
        b270_1 = SNG.B270()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b270_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A271():
    # 'SNG'!A271
    value = 41835
    isdatetime = True

@register(SNG)
class B271():
    # 'SNG'!B271
    value = 2014
    formula = "=YEAR(A271)"
    @eval_fn
    def B271():
        a271_1 = SNG.A271()
        var_1 = YEAR(a271_1)
        return var_1

@register(SNG)
class C271():
    # 'SNG'!C271
    value = "#N/A"
    formula = "=VLOOKUP(B271,$H:$I,2,FALSE)"
    @eval_fn
    def C271():
        b271_1 = SNG.B271()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b271_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A272():
    # 'SNG'!A272
    value = 41866
    isdatetime = True

@register(SNG)
class B272():
    # 'SNG'!B272
    value = 2014
    formula = "=YEAR(A272)"
    @eval_fn
    def B272():
        a272_1 = SNG.A272()
        var_1 = YEAR(a272_1)
        return var_1

@register(SNG)
class C272():
    # 'SNG'!C272
    value = "#N/A"
    formula = "=VLOOKUP(B272,$H:$I,2,FALSE)"
    @eval_fn
    def C272():
        b272_1 = SNG.B272()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b272_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A273():
    # 'SNG'!A273
    value = 41897
    isdatetime = True

@register(SNG)
class B273():
    # 'SNG'!B273
    value = 2014
    formula = "=YEAR(A273)"
    @eval_fn
    def B273():
        a273_1 = SNG.A273()
        var_1 = YEAR(a273_1)
        return var_1

@register(SNG)
class C273():
    # 'SNG'!C273
    value = "#N/A"
    formula = "=VLOOKUP(B273,$H:$I,2,FALSE)"
    @eval_fn
    def C273():
        b273_1 = SNG.B273()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b273_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A274():
    # 'SNG'!A274
    value = 41927
    isdatetime = True

@register(SNG)
class B274():
    # 'SNG'!B274
    value = 2014
    formula = "=YEAR(A274)"
    @eval_fn
    def B274():
        a274_1 = SNG.A274()
        var_1 = YEAR(a274_1)
        return var_1

@register(SNG)
class C274():
    # 'SNG'!C274
    value = "#N/A"
    formula = "=VLOOKUP(B274,$H:$I,2,FALSE)"
    @eval_fn
    def C274():
        b274_1 = SNG.B274()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b274_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A275():
    # 'SNG'!A275
    value = 41958
    isdatetime = True

@register(SNG)
class B275():
    # 'SNG'!B275
    value = 2014
    formula = "=YEAR(A275)"
    @eval_fn
    def B275():
        a275_1 = SNG.A275()
        var_1 = YEAR(a275_1)
        return var_1

@register(SNG)
class C275():
    # 'SNG'!C275
    value = "#N/A"
    formula = "=VLOOKUP(B275,$H:$I,2,FALSE)"
    @eval_fn
    def C275():
        b275_1 = SNG.B275()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b275_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A276():
    # 'SNG'!A276
    value = 41988
    isdatetime = True

@register(SNG)
class B276():
    # 'SNG'!B276
    value = 2014
    formula = "=YEAR(A276)"
    @eval_fn
    def B276():
        a276_1 = SNG.A276()
        var_1 = YEAR(a276_1)
        return var_1

@register(SNG)
class C276():
    # 'SNG'!C276
    value = "#N/A"
    formula = "=VLOOKUP(B276,$H:$I,2,FALSE)"
    @eval_fn
    def C276():
        b276_1 = SNG.B276()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b276_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A277():
    # 'SNG'!A277
    value = 42019
    isdatetime = True

@register(SNG)
class B277():
    # 'SNG'!B277
    value = 2015
    formula = "=YEAR(A277)"
    @eval_fn
    def B277():
        a277_1 = SNG.A277()
        var_1 = YEAR(a277_1)
        return var_1

@register(SNG)
class C277():
    # 'SNG'!C277
    value = "#N/A"
    formula = "=VLOOKUP(B277,$H:$I,2,FALSE)"
    @eval_fn
    def C277():
        b277_1 = SNG.B277()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b277_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A278():
    # 'SNG'!A278
    value = 42050
    isdatetime = True

@register(SNG)
class B278():
    # 'SNG'!B278
    value = 2015
    formula = "=YEAR(A278)"
    @eval_fn
    def B278():
        a278_1 = SNG.A278()
        var_1 = YEAR(a278_1)
        return var_1

@register(SNG)
class C278():
    # 'SNG'!C278
    value = "#N/A"
    formula = "=VLOOKUP(B278,$H:$I,2,FALSE)"
    @eval_fn
    def C278():
        b278_1 = SNG.B278()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b278_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A279():
    # 'SNG'!A279
    value = 42078
    isdatetime = True

@register(SNG)
class B279():
    # 'SNG'!B279
    value = 2015
    formula = "=YEAR(A279)"
    @eval_fn
    def B279():
        a279_1 = SNG.A279()
        var_1 = YEAR(a279_1)
        return var_1

@register(SNG)
class C279():
    # 'SNG'!C279
    value = "#N/A"
    formula = "=VLOOKUP(B279,$H:$I,2,FALSE)"
    @eval_fn
    def C279():
        b279_1 = SNG.B279()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b279_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A280():
    # 'SNG'!A280
    value = 42109
    isdatetime = True

@register(SNG)
class B280():
    # 'SNG'!B280
    value = 2015
    formula = "=YEAR(A280)"
    @eval_fn
    def B280():
        a280_1 = SNG.A280()
        var_1 = YEAR(a280_1)
        return var_1

@register(SNG)
class C280():
    # 'SNG'!C280
    value = "#N/A"
    formula = "=VLOOKUP(B280,$H:$I,2,FALSE)"
    @eval_fn
    def C280():
        b280_1 = SNG.B280()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b280_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A281():
    # 'SNG'!A281
    value = 42139
    isdatetime = True

@register(SNG)
class B281():
    # 'SNG'!B281
    value = 2015
    formula = "=YEAR(A281)"
    @eval_fn
    def B281():
        a281_1 = SNG.A281()
        var_1 = YEAR(a281_1)
        return var_1

@register(SNG)
class C281():
    # 'SNG'!C281
    value = "#N/A"
    formula = "=VLOOKUP(B281,$H:$I,2,FALSE)"
    @eval_fn
    def C281():
        b281_1 = SNG.B281()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b281_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A282():
    # 'SNG'!A282
    value = 42170
    isdatetime = True

@register(SNG)
class B282():
    # 'SNG'!B282
    value = 2015
    formula = "=YEAR(A282)"
    @eval_fn
    def B282():
        a282_1 = SNG.A282()
        var_1 = YEAR(a282_1)
        return var_1

@register(SNG)
class C282():
    # 'SNG'!C282
    value = "#N/A"
    formula = "=VLOOKUP(B282,$H:$I,2,FALSE)"
    @eval_fn
    def C282():
        b282_1 = SNG.B282()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b282_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A283():
    # 'SNG'!A283
    value = 42200
    isdatetime = True

@register(SNG)
class B283():
    # 'SNG'!B283
    value = 2015
    formula = "=YEAR(A283)"
    @eval_fn
    def B283():
        a283_1 = SNG.A283()
        var_1 = YEAR(a283_1)
        return var_1

@register(SNG)
class C283():
    # 'SNG'!C283
    value = "#N/A"
    formula = "=VLOOKUP(B283,$H:$I,2,FALSE)"
    @eval_fn
    def C283():
        b283_1 = SNG.B283()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b283_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A284():
    # 'SNG'!A284
    value = 42231
    isdatetime = True

@register(SNG)
class B284():
    # 'SNG'!B284
    value = 2015
    formula = "=YEAR(A284)"
    @eval_fn
    def B284():
        a284_1 = SNG.A284()
        var_1 = YEAR(a284_1)
        return var_1

@register(SNG)
class C284():
    # 'SNG'!C284
    value = "#N/A"
    formula = "=VLOOKUP(B284,$H:$I,2,FALSE)"
    @eval_fn
    def C284():
        b284_1 = SNG.B284()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b284_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A285():
    # 'SNG'!A285
    value = 42262
    isdatetime = True

@register(SNG)
class B285():
    # 'SNG'!B285
    value = 2015
    formula = "=YEAR(A285)"
    @eval_fn
    def B285():
        a285_1 = SNG.A285()
        var_1 = YEAR(a285_1)
        return var_1

@register(SNG)
class C285():
    # 'SNG'!C285
    value = "#N/A"
    formula = "=VLOOKUP(B285,$H:$I,2,FALSE)"
    @eval_fn
    def C285():
        b285_1 = SNG.B285()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b285_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A286():
    # 'SNG'!A286
    value = 42292
    isdatetime = True

@register(SNG)
class B286():
    # 'SNG'!B286
    value = 2015
    formula = "=YEAR(A286)"
    @eval_fn
    def B286():
        a286_1 = SNG.A286()
        var_1 = YEAR(a286_1)
        return var_1

@register(SNG)
class C286():
    # 'SNG'!C286
    value = "#N/A"
    formula = "=VLOOKUP(B286,$H:$I,2,FALSE)"
    @eval_fn
    def C286():
        b286_1 = SNG.B286()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b286_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A287():
    # 'SNG'!A287
    value = 42323
    isdatetime = True

@register(SNG)
class B287():
    # 'SNG'!B287
    value = 2015
    formula = "=YEAR(A287)"
    @eval_fn
    def B287():
        a287_1 = SNG.A287()
        var_1 = YEAR(a287_1)
        return var_1

@register(SNG)
class C287():
    # 'SNG'!C287
    value = "#N/A"
    formula = "=VLOOKUP(B287,$H:$I,2,FALSE)"
    @eval_fn
    def C287():
        b287_1 = SNG.B287()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b287_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A288():
    # 'SNG'!A288
    value = 42353
    isdatetime = True

@register(SNG)
class B288():
    # 'SNG'!B288
    value = 2015
    formula = "=YEAR(A288)"
    @eval_fn
    def B288():
        a288_1 = SNG.A288()
        var_1 = YEAR(a288_1)
        return var_1

@register(SNG)
class C288():
    # 'SNG'!C288
    value = "#N/A"
    formula = "=VLOOKUP(B288,$H:$I,2,FALSE)"
    @eval_fn
    def C288():
        b288_1 = SNG.B288()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b288_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A289():
    # 'SNG'!A289
    value = 42384
    isdatetime = True

@register(SNG)
class B289():
    # 'SNG'!B289
    value = 2016
    formula = "=YEAR(A289)"
    @eval_fn
    def B289():
        a289_1 = SNG.A289()
        var_1 = YEAR(a289_1)
        return var_1

@register(SNG)
class C289():
    # 'SNG'!C289
    value = "#N/A"
    formula = "=VLOOKUP(B289,$H:$I,2,FALSE)"
    @eval_fn
    def C289():
        b289_1 = SNG.B289()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b289_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A290():
    # 'SNG'!A290
    value = 42415
    isdatetime = True

@register(SNG)
class B290():
    # 'SNG'!B290
    value = 2016
    formula = "=YEAR(A290)"
    @eval_fn
    def B290():
        a290_1 = SNG.A290()
        var_1 = YEAR(a290_1)
        return var_1

@register(SNG)
class C290():
    # 'SNG'!C290
    value = "#N/A"
    formula = "=VLOOKUP(B290,$H:$I,2,FALSE)"
    @eval_fn
    def C290():
        b290_1 = SNG.B290()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b290_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A291():
    # 'SNG'!A291
    value = 42444
    isdatetime = True

@register(SNG)
class B291():
    # 'SNG'!B291
    value = 2016
    formula = "=YEAR(A291)"
    @eval_fn
    def B291():
        a291_1 = SNG.A291()
        var_1 = YEAR(a291_1)
        return var_1

@register(SNG)
class C291():
    # 'SNG'!C291
    value = "#N/A"
    formula = "=VLOOKUP(B291,$H:$I,2,FALSE)"
    @eval_fn
    def C291():
        b291_1 = SNG.B291()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b291_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A292():
    # 'SNG'!A292
    value = 42475
    isdatetime = True

@register(SNG)
class B292():
    # 'SNG'!B292
    value = 2016
    formula = "=YEAR(A292)"
    @eval_fn
    def B292():
        a292_1 = SNG.A292()
        var_1 = YEAR(a292_1)
        return var_1

@register(SNG)
class C292():
    # 'SNG'!C292
    value = "#N/A"
    formula = "=VLOOKUP(B292,$H:$I,2,FALSE)"
    @eval_fn
    def C292():
        b292_1 = SNG.B292()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b292_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A293():
    # 'SNG'!A293
    value = 42505
    isdatetime = True

@register(SNG)
class B293():
    # 'SNG'!B293
    value = 2016
    formula = "=YEAR(A293)"
    @eval_fn
    def B293():
        a293_1 = SNG.A293()
        var_1 = YEAR(a293_1)
        return var_1

@register(SNG)
class C293():
    # 'SNG'!C293
    value = "#N/A"
    formula = "=VLOOKUP(B293,$H:$I,2,FALSE)"
    @eval_fn
    def C293():
        b293_1 = SNG.B293()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b293_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A294():
    # 'SNG'!A294
    value = 42536
    isdatetime = True

@register(SNG)
class B294():
    # 'SNG'!B294
    value = 2016
    formula = "=YEAR(A294)"
    @eval_fn
    def B294():
        a294_1 = SNG.A294()
        var_1 = YEAR(a294_1)
        return var_1

@register(SNG)
class C294():
    # 'SNG'!C294
    value = "#N/A"
    formula = "=VLOOKUP(B294,$H:$I,2,FALSE)"
    @eval_fn
    def C294():
        b294_1 = SNG.B294()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b294_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A295():
    # 'SNG'!A295
    value = 42566
    isdatetime = True

@register(SNG)
class B295():
    # 'SNG'!B295
    value = 2016
    formula = "=YEAR(A295)"
    @eval_fn
    def B295():
        a295_1 = SNG.A295()
        var_1 = YEAR(a295_1)
        return var_1

@register(SNG)
class C295():
    # 'SNG'!C295
    value = "#N/A"
    formula = "=VLOOKUP(B295,$H:$I,2,FALSE)"
    @eval_fn
    def C295():
        b295_1 = SNG.B295()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b295_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A296():
    # 'SNG'!A296
    value = 42597
    isdatetime = True

@register(SNG)
class B296():
    # 'SNG'!B296
    value = 2016
    formula = "=YEAR(A296)"
    @eval_fn
    def B296():
        a296_1 = SNG.A296()
        var_1 = YEAR(a296_1)
        return var_1

@register(SNG)
class C296():
    # 'SNG'!C296
    value = "#N/A"
    formula = "=VLOOKUP(B296,$H:$I,2,FALSE)"
    @eval_fn
    def C296():
        b296_1 = SNG.B296()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b296_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A297():
    # 'SNG'!A297
    value = 42628
    isdatetime = True

@register(SNG)
class B297():
    # 'SNG'!B297
    value = 2016
    formula = "=YEAR(A297)"
    @eval_fn
    def B297():
        a297_1 = SNG.A297()
        var_1 = YEAR(a297_1)
        return var_1

@register(SNG)
class C297():
    # 'SNG'!C297
    value = "#N/A"
    formula = "=VLOOKUP(B297,$H:$I,2,FALSE)"
    @eval_fn
    def C297():
        b297_1 = SNG.B297()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b297_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A298():
    # 'SNG'!A298
    value = 42658
    isdatetime = True

@register(SNG)
class B298():
    # 'SNG'!B298
    value = 2016
    formula = "=YEAR(A298)"
    @eval_fn
    def B298():
        a298_1 = SNG.A298()
        var_1 = YEAR(a298_1)
        return var_1

@register(SNG)
class C298():
    # 'SNG'!C298
    value = "#N/A"
    formula = "=VLOOKUP(B298,$H:$I,2,FALSE)"
    @eval_fn
    def C298():
        b298_1 = SNG.B298()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b298_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A299():
    # 'SNG'!A299
    value = 42689
    isdatetime = True

@register(SNG)
class B299():
    # 'SNG'!B299
    value = 2016
    formula = "=YEAR(A299)"
    @eval_fn
    def B299():
        a299_1 = SNG.A299()
        var_1 = YEAR(a299_1)
        return var_1

@register(SNG)
class C299():
    # 'SNG'!C299
    value = "#N/A"
    formula = "=VLOOKUP(B299,$H:$I,2,FALSE)"
    @eval_fn
    def C299():
        b299_1 = SNG.B299()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b299_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A300():
    # 'SNG'!A300
    value = 42719
    isdatetime = True

@register(SNG)
class B300():
    # 'SNG'!B300
    value = 2016
    formula = "=YEAR(A300)"
    @eval_fn
    def B300():
        a300_1 = SNG.A300()
        var_1 = YEAR(a300_1)
        return var_1

@register(SNG)
class C300():
    # 'SNG'!C300
    value = "#N/A"
    formula = "=VLOOKUP(B300,$H:$I,2,FALSE)"
    @eval_fn
    def C300():
        b300_1 = SNG.B300()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b300_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A301():
    # 'SNG'!A301
    value = 42750
    isdatetime = True

@register(SNG)
class B301():
    # 'SNG'!B301
    value = 2017
    formula = "=YEAR(A301)"
    @eval_fn
    def B301():
        a301_1 = SNG.A301()
        var_1 = YEAR(a301_1)
        return var_1

@register(SNG)
class C301():
    # 'SNG'!C301
    value = "#N/A"
    formula = "=VLOOKUP(B301,$H:$I,2,FALSE)"
    @eval_fn
    def C301():
        b301_1 = SNG.B301()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b301_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A302():
    # 'SNG'!A302
    value = 42781
    isdatetime = True

@register(SNG)
class B302():
    # 'SNG'!B302
    value = 2017
    formula = "=YEAR(A302)"
    @eval_fn
    def B302():
        a302_1 = SNG.A302()
        var_1 = YEAR(a302_1)
        return var_1

@register(SNG)
class C302():
    # 'SNG'!C302
    value = "#N/A"
    formula = "=VLOOKUP(B302,$H:$I,2,FALSE)"
    @eval_fn
    def C302():
        b302_1 = SNG.B302()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b302_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A303():
    # 'SNG'!A303
    value = 42809
    isdatetime = True

@register(SNG)
class B303():
    # 'SNG'!B303
    value = 2017
    formula = "=YEAR(A303)"
    @eval_fn
    def B303():
        a303_1 = SNG.A303()
        var_1 = YEAR(a303_1)
        return var_1

@register(SNG)
class C303():
    # 'SNG'!C303
    value = "#N/A"
    formula = "=VLOOKUP(B303,$H:$I,2,FALSE)"
    @eval_fn
    def C303():
        b303_1 = SNG.B303()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b303_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A304():
    # 'SNG'!A304
    value = 42840
    isdatetime = True

@register(SNG)
class B304():
    # 'SNG'!B304
    value = 2017
    formula = "=YEAR(A304)"
    @eval_fn
    def B304():
        a304_1 = SNG.A304()
        var_1 = YEAR(a304_1)
        return var_1

@register(SNG)
class C304():
    # 'SNG'!C304
    value = "#N/A"
    formula = "=VLOOKUP(B304,$H:$I,2,FALSE)"
    @eval_fn
    def C304():
        b304_1 = SNG.B304()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b304_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A305():
    # 'SNG'!A305
    value = 42870
    isdatetime = True

@register(SNG)
class B305():
    # 'SNG'!B305
    value = 2017
    formula = "=YEAR(A305)"
    @eval_fn
    def B305():
        a305_1 = SNG.A305()
        var_1 = YEAR(a305_1)
        return var_1

@register(SNG)
class C305():
    # 'SNG'!C305
    value = "#N/A"
    formula = "=VLOOKUP(B305,$H:$I,2,FALSE)"
    @eval_fn
    def C305():
        b305_1 = SNG.B305()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b305_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A306():
    # 'SNG'!A306
    value = 42901
    isdatetime = True

@register(SNG)
class B306():
    # 'SNG'!B306
    value = 2017
    formula = "=YEAR(A306)"
    @eval_fn
    def B306():
        a306_1 = SNG.A306()
        var_1 = YEAR(a306_1)
        return var_1

@register(SNG)
class C306():
    # 'SNG'!C306
    value = "#N/A"
    formula = "=VLOOKUP(B306,$H:$I,2,FALSE)"
    @eval_fn
    def C306():
        b306_1 = SNG.B306()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b306_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A307():
    # 'SNG'!A307
    value = 42931
    isdatetime = True

@register(SNG)
class B307():
    # 'SNG'!B307
    value = 2017
    formula = "=YEAR(A307)"
    @eval_fn
    def B307():
        a307_1 = SNG.A307()
        var_1 = YEAR(a307_1)
        return var_1

@register(SNG)
class C307():
    # 'SNG'!C307
    value = "#N/A"
    formula = "=VLOOKUP(B307,$H:$I,2,FALSE)"
    @eval_fn
    def C307():
        b307_1 = SNG.B307()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b307_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A308():
    # 'SNG'!A308
    value = 42962
    isdatetime = True

@register(SNG)
class B308():
    # 'SNG'!B308
    value = 2017
    formula = "=YEAR(A308)"
    @eval_fn
    def B308():
        a308_1 = SNG.A308()
        var_1 = YEAR(a308_1)
        return var_1

@register(SNG)
class C308():
    # 'SNG'!C308
    value = "#N/A"
    formula = "=VLOOKUP(B308,$H:$I,2,FALSE)"
    @eval_fn
    def C308():
        b308_1 = SNG.B308()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b308_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A309():
    # 'SNG'!A309
    value = 42993
    isdatetime = True

@register(SNG)
class B309():
    # 'SNG'!B309
    value = 2017
    formula = "=YEAR(A309)"
    @eval_fn
    def B309():
        a309_1 = SNG.A309()
        var_1 = YEAR(a309_1)
        return var_1

@register(SNG)
class C309():
    # 'SNG'!C309
    value = "#N/A"
    formula = "=VLOOKUP(B309,$H:$I,2,FALSE)"
    @eval_fn
    def C309():
        b309_1 = SNG.B309()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b309_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A310():
    # 'SNG'!A310
    value = 43023
    isdatetime = True

@register(SNG)
class B310():
    # 'SNG'!B310
    value = 2017
    formula = "=YEAR(A310)"
    @eval_fn
    def B310():
        a310_1 = SNG.A310()
        var_1 = YEAR(a310_1)
        return var_1

@register(SNG)
class C310():
    # 'SNG'!C310
    value = "#N/A"
    formula = "=VLOOKUP(B310,$H:$I,2,FALSE)"
    @eval_fn
    def C310():
        b310_1 = SNG.B310()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b310_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A311():
    # 'SNG'!A311
    value = 43054
    isdatetime = True

@register(SNG)
class B311():
    # 'SNG'!B311
    value = 2017
    formula = "=YEAR(A311)"
    @eval_fn
    def B311():
        a311_1 = SNG.A311()
        var_1 = YEAR(a311_1)
        return var_1

@register(SNG)
class C311():
    # 'SNG'!C311
    value = "#N/A"
    formula = "=VLOOKUP(B311,$H:$I,2,FALSE)"
    @eval_fn
    def C311():
        b311_1 = SNG.B311()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b311_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A312():
    # 'SNG'!A312
    value = 43084
    isdatetime = True

@register(SNG)
class B312():
    # 'SNG'!B312
    value = 2017
    formula = "=YEAR(A312)"
    @eval_fn
    def B312():
        a312_1 = SNG.A312()
        var_1 = YEAR(a312_1)
        return var_1

@register(SNG)
class C312():
    # 'SNG'!C312
    value = "#N/A"
    formula = "=VLOOKUP(B312,$H:$I,2,FALSE)"
    @eval_fn
    def C312():
        b312_1 = SNG.B312()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b312_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A313():
    # 'SNG'!A313
    value = 43115
    isdatetime = True

@register(SNG)
class B313():
    # 'SNG'!B313
    value = 2018
    formula = "=YEAR(A313)"
    @eval_fn
    def B313():
        a313_1 = SNG.A313()
        var_1 = YEAR(a313_1)
        return var_1

@register(SNG)
class C313():
    # 'SNG'!C313
    value = "#N/A"
    formula = "=VLOOKUP(B313,$H:$I,2,FALSE)"
    @eval_fn
    def C313():
        b313_1 = SNG.B313()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b313_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A314():
    # 'SNG'!A314
    value = 43146
    isdatetime = True

@register(SNG)
class B314():
    # 'SNG'!B314
    value = 2018
    formula = "=YEAR(A314)"
    @eval_fn
    def B314():
        a314_1 = SNG.A314()
        var_1 = YEAR(a314_1)
        return var_1

@register(SNG)
class C314():
    # 'SNG'!C314
    value = "#N/A"
    formula = "=VLOOKUP(B314,$H:$I,2,FALSE)"
    @eval_fn
    def C314():
        b314_1 = SNG.B314()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b314_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A315():
    # 'SNG'!A315
    value = 43174
    isdatetime = True

@register(SNG)
class B315():
    # 'SNG'!B315
    value = 2018
    formula = "=YEAR(A315)"
    @eval_fn
    def B315():
        a315_1 = SNG.A315()
        var_1 = YEAR(a315_1)
        return var_1

@register(SNG)
class C315():
    # 'SNG'!C315
    value = "#N/A"
    formula = "=VLOOKUP(B315,$H:$I,2,FALSE)"
    @eval_fn
    def C315():
        b315_1 = SNG.B315()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b315_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A316():
    # 'SNG'!A316
    value = 43205
    isdatetime = True

@register(SNG)
class B316():
    # 'SNG'!B316
    value = 2018
    formula = "=YEAR(A316)"
    @eval_fn
    def B316():
        a316_1 = SNG.A316()
        var_1 = YEAR(a316_1)
        return var_1

@register(SNG)
class C316():
    # 'SNG'!C316
    value = "#N/A"
    formula = "=VLOOKUP(B316,$H:$I,2,FALSE)"
    @eval_fn
    def C316():
        b316_1 = SNG.B316()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b316_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A317():
    # 'SNG'!A317
    value = 43235
    isdatetime = True

@register(SNG)
class B317():
    # 'SNG'!B317
    value = 2018
    formula = "=YEAR(A317)"
    @eval_fn
    def B317():
        a317_1 = SNG.A317()
        var_1 = YEAR(a317_1)
        return var_1

@register(SNG)
class C317():
    # 'SNG'!C317
    value = "#N/A"
    formula = "=VLOOKUP(B317,$H:$I,2,FALSE)"
    @eval_fn
    def C317():
        b317_1 = SNG.B317()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b317_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A318():
    # 'SNG'!A318
    value = 43266
    isdatetime = True

@register(SNG)
class B318():
    # 'SNG'!B318
    value = 2018
    formula = "=YEAR(A318)"
    @eval_fn
    def B318():
        a318_1 = SNG.A318()
        var_1 = YEAR(a318_1)
        return var_1

@register(SNG)
class C318():
    # 'SNG'!C318
    value = "#N/A"
    formula = "=VLOOKUP(B318,$H:$I,2,FALSE)"
    @eval_fn
    def C318():
        b318_1 = SNG.B318()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b318_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A319():
    # 'SNG'!A319
    value = 43296
    isdatetime = True

@register(SNG)
class B319():
    # 'SNG'!B319
    value = 2018
    formula = "=YEAR(A319)"
    @eval_fn
    def B319():
        a319_1 = SNG.A319()
        var_1 = YEAR(a319_1)
        return var_1

@register(SNG)
class C319():
    # 'SNG'!C319
    value = "#N/A"
    formula = "=VLOOKUP(B319,$H:$I,2,FALSE)"
    @eval_fn
    def C319():
        b319_1 = SNG.B319()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b319_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A320():
    # 'SNG'!A320
    value = 43327
    isdatetime = True

@register(SNG)
class B320():
    # 'SNG'!B320
    value = 2018
    formula = "=YEAR(A320)"
    @eval_fn
    def B320():
        a320_1 = SNG.A320()
        var_1 = YEAR(a320_1)
        return var_1

@register(SNG)
class C320():
    # 'SNG'!C320
    value = "#N/A"
    formula = "=VLOOKUP(B320,$H:$I,2,FALSE)"
    @eval_fn
    def C320():
        b320_1 = SNG.B320()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b320_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A321():
    # 'SNG'!A321
    value = 43358
    isdatetime = True

@register(SNG)
class B321():
    # 'SNG'!B321
    value = 2018
    formula = "=YEAR(A321)"
    @eval_fn
    def B321():
        a321_1 = SNG.A321()
        var_1 = YEAR(a321_1)
        return var_1

@register(SNG)
class C321():
    # 'SNG'!C321
    value = "#N/A"
    formula = "=VLOOKUP(B321,$H:$I,2,FALSE)"
    @eval_fn
    def C321():
        b321_1 = SNG.B321()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b321_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A322():
    # 'SNG'!A322
    value = 43388
    isdatetime = True

@register(SNG)
class B322():
    # 'SNG'!B322
    value = 2018
    formula = "=YEAR(A322)"
    @eval_fn
    def B322():
        a322_1 = SNG.A322()
        var_1 = YEAR(a322_1)
        return var_1

@register(SNG)
class C322():
    # 'SNG'!C322
    value = "#N/A"
    formula = "=VLOOKUP(B322,$H:$I,2,FALSE)"
    @eval_fn
    def C322():
        b322_1 = SNG.B322()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b322_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A323():
    # 'SNG'!A323
    value = 43419
    isdatetime = True

@register(SNG)
class B323():
    # 'SNG'!B323
    value = 2018
    formula = "=YEAR(A323)"
    @eval_fn
    def B323():
        a323_1 = SNG.A323()
        var_1 = YEAR(a323_1)
        return var_1

@register(SNG)
class C323():
    # 'SNG'!C323
    value = "#N/A"
    formula = "=VLOOKUP(B323,$H:$I,2,FALSE)"
    @eval_fn
    def C323():
        b323_1 = SNG.B323()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b323_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A324():
    # 'SNG'!A324
    value = 43449
    isdatetime = True

@register(SNG)
class B324():
    # 'SNG'!B324
    value = 2018
    formula = "=YEAR(A324)"
    @eval_fn
    def B324():
        a324_1 = SNG.A324()
        var_1 = YEAR(a324_1)
        return var_1

@register(SNG)
class C324():
    # 'SNG'!C324
    value = "#N/A"
    formula = "=VLOOKUP(B324,$H:$I,2,FALSE)"
    @eval_fn
    def C324():
        b324_1 = SNG.B324()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b324_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A325():
    # 'SNG'!A325
    value = 43480
    isdatetime = True

@register(SNG)
class B325():
    # 'SNG'!B325
    value = 2019
    formula = "=YEAR(A325)"
    @eval_fn
    def B325():
        a325_1 = SNG.A325()
        var_1 = YEAR(a325_1)
        return var_1

@register(SNG)
class C325():
    # 'SNG'!C325
    value = "#N/A"
    formula = "=VLOOKUP(B325,$H:$I,2,FALSE)"
    @eval_fn
    def C325():
        b325_1 = SNG.B325()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b325_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A326():
    # 'SNG'!A326
    value = 43511
    isdatetime = True

@register(SNG)
class B326():
    # 'SNG'!B326
    value = 2019
    formula = "=YEAR(A326)"
    @eval_fn
    def B326():
        a326_1 = SNG.A326()
        var_1 = YEAR(a326_1)
        return var_1

@register(SNG)
class C326():
    # 'SNG'!C326
    value = "#N/A"
    formula = "=VLOOKUP(B326,$H:$I,2,FALSE)"
    @eval_fn
    def C326():
        b326_1 = SNG.B326()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b326_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A327():
    # 'SNG'!A327
    value = 43539
    isdatetime = True

@register(SNG)
class B327():
    # 'SNG'!B327
    value = 2019
    formula = "=YEAR(A327)"
    @eval_fn
    def B327():
        a327_1 = SNG.A327()
        var_1 = YEAR(a327_1)
        return var_1

@register(SNG)
class C327():
    # 'SNG'!C327
    value = "#N/A"
    formula = "=VLOOKUP(B327,$H:$I,2,FALSE)"
    @eval_fn
    def C327():
        b327_1 = SNG.B327()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b327_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A328():
    # 'SNG'!A328
    value = 43570
    isdatetime = True

@register(SNG)
class B328():
    # 'SNG'!B328
    value = 2019
    formula = "=YEAR(A328)"
    @eval_fn
    def B328():
        a328_1 = SNG.A328()
        var_1 = YEAR(a328_1)
        return var_1

@register(SNG)
class C328():
    # 'SNG'!C328
    value = "#N/A"
    formula = "=VLOOKUP(B328,$H:$I,2,FALSE)"
    @eval_fn
    def C328():
        b328_1 = SNG.B328()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b328_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A329():
    # 'SNG'!A329
    value = 43600
    isdatetime = True

@register(SNG)
class B329():
    # 'SNG'!B329
    value = 2019
    formula = "=YEAR(A329)"
    @eval_fn
    def B329():
        a329_1 = SNG.A329()
        var_1 = YEAR(a329_1)
        return var_1

@register(SNG)
class C329():
    # 'SNG'!C329
    value = "#N/A"
    formula = "=VLOOKUP(B329,$H:$I,2,FALSE)"
    @eval_fn
    def C329():
        b329_1 = SNG.B329()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b329_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A330():
    # 'SNG'!A330
    value = 43631
    isdatetime = True

@register(SNG)
class B330():
    # 'SNG'!B330
    value = 2019
    formula = "=YEAR(A330)"
    @eval_fn
    def B330():
        a330_1 = SNG.A330()
        var_1 = YEAR(a330_1)
        return var_1

@register(SNG)
class C330():
    # 'SNG'!C330
    value = "#N/A"
    formula = "=VLOOKUP(B330,$H:$I,2,FALSE)"
    @eval_fn
    def C330():
        b330_1 = SNG.B330()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b330_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A331():
    # 'SNG'!A331
    value = 43661
    isdatetime = True

@register(SNG)
class B331():
    # 'SNG'!B331
    value = 2019
    formula = "=YEAR(A331)"
    @eval_fn
    def B331():
        a331_1 = SNG.A331()
        var_1 = YEAR(a331_1)
        return var_1

@register(SNG)
class C331():
    # 'SNG'!C331
    value = "#N/A"
    formula = "=VLOOKUP(B331,$H:$I,2,FALSE)"
    @eval_fn
    def C331():
        b331_1 = SNG.B331()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b331_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A332():
    # 'SNG'!A332
    value = 43692
    isdatetime = True

@register(SNG)
class B332():
    # 'SNG'!B332
    value = 2019
    formula = "=YEAR(A332)"
    @eval_fn
    def B332():
        a332_1 = SNG.A332()
        var_1 = YEAR(a332_1)
        return var_1

@register(SNG)
class C332():
    # 'SNG'!C332
    value = "#N/A"
    formula = "=VLOOKUP(B332,$H:$I,2,FALSE)"
    @eval_fn
    def C332():
        b332_1 = SNG.B332()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b332_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A333():
    # 'SNG'!A333
    value = 43723
    isdatetime = True

@register(SNG)
class B333():
    # 'SNG'!B333
    value = 2019
    formula = "=YEAR(A333)"
    @eval_fn
    def B333():
        a333_1 = SNG.A333()
        var_1 = YEAR(a333_1)
        return var_1

@register(SNG)
class C333():
    # 'SNG'!C333
    value = "#N/A"
    formula = "=VLOOKUP(B333,$H:$I,2,FALSE)"
    @eval_fn
    def C333():
        b333_1 = SNG.B333()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b333_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A334():
    # 'SNG'!A334
    value = 43753
    isdatetime = True

@register(SNG)
class B334():
    # 'SNG'!B334
    value = 2019
    formula = "=YEAR(A334)"
    @eval_fn
    def B334():
        a334_1 = SNG.A334()
        var_1 = YEAR(a334_1)
        return var_1

@register(SNG)
class C334():
    # 'SNG'!C334
    value = "#N/A"
    formula = "=VLOOKUP(B334,$H:$I,2,FALSE)"
    @eval_fn
    def C334():
        b334_1 = SNG.B334()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b334_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A335():
    # 'SNG'!A335
    value = 43784
    isdatetime = True

@register(SNG)
class B335():
    # 'SNG'!B335
    value = 2019
    formula = "=YEAR(A335)"
    @eval_fn
    def B335():
        a335_1 = SNG.A335()
        var_1 = YEAR(a335_1)
        return var_1

@register(SNG)
class C335():
    # 'SNG'!C335
    value = "#N/A"
    formula = "=VLOOKUP(B335,$H:$I,2,FALSE)"
    @eval_fn
    def C335():
        b335_1 = SNG.B335()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b335_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A336():
    # 'SNG'!A336
    value = 43814
    isdatetime = True

@register(SNG)
class B336():
    # 'SNG'!B336
    value = 2019
    formula = "=YEAR(A336)"
    @eval_fn
    def B336():
        a336_1 = SNG.A336()
        var_1 = YEAR(a336_1)
        return var_1

@register(SNG)
class C336():
    # 'SNG'!C336
    value = "#N/A"
    formula = "=VLOOKUP(B336,$H:$I,2,FALSE)"
    @eval_fn
    def C336():
        b336_1 = SNG.B336()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b336_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A337():
    # 'SNG'!A337
    value = 43845
    isdatetime = True

@register(SNG)
class B337():
    # 'SNG'!B337
    value = 2020
    formula = "=YEAR(A337)"
    @eval_fn
    def B337():
        a337_1 = SNG.A337()
        var_1 = YEAR(a337_1)
        return var_1

@register(SNG)
class C337():
    # 'SNG'!C337
    value = "#N/A"
    formula = "=VLOOKUP(B337,$H:$I,2,FALSE)"
    @eval_fn
    def C337():
        b337_1 = SNG.B337()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b337_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A338():
    # 'SNG'!A338
    value = 43876
    isdatetime = True

@register(SNG)
class B338():
    # 'SNG'!B338
    value = 2020
    formula = "=YEAR(A338)"
    @eval_fn
    def B338():
        a338_1 = SNG.A338()
        var_1 = YEAR(a338_1)
        return var_1

@register(SNG)
class C338():
    # 'SNG'!C338
    value = "#N/A"
    formula = "=VLOOKUP(B338,$H:$I,2,FALSE)"
    @eval_fn
    def C338():
        b338_1 = SNG.B338()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b338_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A339():
    # 'SNG'!A339
    value = 43905
    isdatetime = True

@register(SNG)
class B339():
    # 'SNG'!B339
    value = 2020
    formula = "=YEAR(A339)"
    @eval_fn
    def B339():
        a339_1 = SNG.A339()
        var_1 = YEAR(a339_1)
        return var_1

@register(SNG)
class C339():
    # 'SNG'!C339
    value = "#N/A"
    formula = "=VLOOKUP(B339,$H:$I,2,FALSE)"
    @eval_fn
    def C339():
        b339_1 = SNG.B339()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b339_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A340():
    # 'SNG'!A340
    value = 43936
    isdatetime = True

@register(SNG)
class B340():
    # 'SNG'!B340
    value = 2020
    formula = "=YEAR(A340)"
    @eval_fn
    def B340():
        a340_1 = SNG.A340()
        var_1 = YEAR(a340_1)
        return var_1

@register(SNG)
class C340():
    # 'SNG'!C340
    value = "#N/A"
    formula = "=VLOOKUP(B340,$H:$I,2,FALSE)"
    @eval_fn
    def C340():
        b340_1 = SNG.B340()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b340_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A341():
    # 'SNG'!A341
    value = 43966
    isdatetime = True

@register(SNG)
class B341():
    # 'SNG'!B341
    value = 2020
    formula = "=YEAR(A341)"
    @eval_fn
    def B341():
        a341_1 = SNG.A341()
        var_1 = YEAR(a341_1)
        return var_1

@register(SNG)
class C341():
    # 'SNG'!C341
    value = "#N/A"
    formula = "=VLOOKUP(B341,$H:$I,2,FALSE)"
    @eval_fn
    def C341():
        b341_1 = SNG.B341()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b341_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A342():
    # 'SNG'!A342
    value = 43997
    isdatetime = True

@register(SNG)
class B342():
    # 'SNG'!B342
    value = 2020
    formula = "=YEAR(A342)"
    @eval_fn
    def B342():
        a342_1 = SNG.A342()
        var_1 = YEAR(a342_1)
        return var_1

@register(SNG)
class C342():
    # 'SNG'!C342
    value = "#N/A"
    formula = "=VLOOKUP(B342,$H:$I,2,FALSE)"
    @eval_fn
    def C342():
        b342_1 = SNG.B342()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b342_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A343():
    # 'SNG'!A343
    value = 44027
    isdatetime = True

@register(SNG)
class B343():
    # 'SNG'!B343
    value = 2020
    formula = "=YEAR(A343)"
    @eval_fn
    def B343():
        a343_1 = SNG.A343()
        var_1 = YEAR(a343_1)
        return var_1

@register(SNG)
class C343():
    # 'SNG'!C343
    value = "#N/A"
    formula = "=VLOOKUP(B343,$H:$I,2,FALSE)"
    @eval_fn
    def C343():
        b343_1 = SNG.B343()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b343_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A344():
    # 'SNG'!A344
    value = 44058
    isdatetime = True

@register(SNG)
class B344():
    # 'SNG'!B344
    value = 2020
    formula = "=YEAR(A344)"
    @eval_fn
    def B344():
        a344_1 = SNG.A344()
        var_1 = YEAR(a344_1)
        return var_1

@register(SNG)
class C344():
    # 'SNG'!C344
    value = "#N/A"
    formula = "=VLOOKUP(B344,$H:$I,2,FALSE)"
    @eval_fn
    def C344():
        b344_1 = SNG.B344()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b344_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A345():
    # 'SNG'!A345
    value = 44089
    isdatetime = True

@register(SNG)
class B345():
    # 'SNG'!B345
    value = 2020
    formula = "=YEAR(A345)"
    @eval_fn
    def B345():
        a345_1 = SNG.A345()
        var_1 = YEAR(a345_1)
        return var_1

@register(SNG)
class C345():
    # 'SNG'!C345
    value = "#N/A"
    formula = "=VLOOKUP(B345,$H:$I,2,FALSE)"
    @eval_fn
    def C345():
        b345_1 = SNG.B345()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b345_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A346():
    # 'SNG'!A346
    value = 44119
    isdatetime = True

@register(SNG)
class B346():
    # 'SNG'!B346
    value = 2020
    formula = "=YEAR(A346)"
    @eval_fn
    def B346():
        a346_1 = SNG.A346()
        var_1 = YEAR(a346_1)
        return var_1

@register(SNG)
class C346():
    # 'SNG'!C346
    value = "#N/A"
    formula = "=VLOOKUP(B346,$H:$I,2,FALSE)"
    @eval_fn
    def C346():
        b346_1 = SNG.B346()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b346_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A347():
    # 'SNG'!A347
    value = 44150
    isdatetime = True

@register(SNG)
class B347():
    # 'SNG'!B347
    value = 2020
    formula = "=YEAR(A347)"
    @eval_fn
    def B347():
        a347_1 = SNG.A347()
        var_1 = YEAR(a347_1)
        return var_1

@register(SNG)
class C347():
    # 'SNG'!C347
    value = "#N/A"
    formula = "=VLOOKUP(B347,$H:$I,2,FALSE)"
    @eval_fn
    def C347():
        b347_1 = SNG.B347()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b347_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A348():
    # 'SNG'!A348
    value = 44180
    isdatetime = True

@register(SNG)
class B348():
    # 'SNG'!B348
    value = 2020
    formula = "=YEAR(A348)"
    @eval_fn
    def B348():
        a348_1 = SNG.A348()
        var_1 = YEAR(a348_1)
        return var_1

@register(SNG)
class C348():
    # 'SNG'!C348
    value = "#N/A"
    formula = "=VLOOKUP(B348,$H:$I,2,FALSE)"
    @eval_fn
    def C348():
        b348_1 = SNG.B348()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b348_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A349():
    # 'SNG'!A349
    value = 44211
    isdatetime = True

@register(SNG)
class B349():
    # 'SNG'!B349
    value = 2021
    formula = "=YEAR(A349)"
    @eval_fn
    def B349():
        a349_1 = SNG.A349()
        var_1 = YEAR(a349_1)
        return var_1

@register(SNG)
class C349():
    # 'SNG'!C349
    value = "#N/A"
    formula = "=VLOOKUP(B349,$H:$I,2,FALSE)"
    @eval_fn
    def C349():
        b349_1 = SNG.B349()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b349_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A350():
    # 'SNG'!A350
    value = 44242
    isdatetime = True

@register(SNG)
class B350():
    # 'SNG'!B350
    value = 2021
    formula = "=YEAR(A350)"
    @eval_fn
    def B350():
        a350_1 = SNG.A350()
        var_1 = YEAR(a350_1)
        return var_1

@register(SNG)
class C350():
    # 'SNG'!C350
    value = "#N/A"
    formula = "=VLOOKUP(B350,$H:$I,2,FALSE)"
    @eval_fn
    def C350():
        b350_1 = SNG.B350()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b350_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A351():
    # 'SNG'!A351
    value = 44270
    isdatetime = True

@register(SNG)
class B351():
    # 'SNG'!B351
    value = 2021
    formula = "=YEAR(A351)"
    @eval_fn
    def B351():
        a351_1 = SNG.A351()
        var_1 = YEAR(a351_1)
        return var_1

@register(SNG)
class C351():
    # 'SNG'!C351
    value = "#N/A"
    formula = "=VLOOKUP(B351,$H:$I,2,FALSE)"
    @eval_fn
    def C351():
        b351_1 = SNG.B351()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b351_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A352():
    # 'SNG'!A352
    value = 44301
    isdatetime = True

@register(SNG)
class B352():
    # 'SNG'!B352
    value = 2021
    formula = "=YEAR(A352)"
    @eval_fn
    def B352():
        a352_1 = SNG.A352()
        var_1 = YEAR(a352_1)
        return var_1

@register(SNG)
class C352():
    # 'SNG'!C352
    value = "#N/A"
    formula = "=VLOOKUP(B352,$H:$I,2,FALSE)"
    @eval_fn
    def C352():
        b352_1 = SNG.B352()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b352_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A353():
    # 'SNG'!A353
    value = 44331
    isdatetime = True

@register(SNG)
class B353():
    # 'SNG'!B353
    value = 2021
    formula = "=YEAR(A353)"
    @eval_fn
    def B353():
        a353_1 = SNG.A353()
        var_1 = YEAR(a353_1)
        return var_1

@register(SNG)
class C353():
    # 'SNG'!C353
    value = "#N/A"
    formula = "=VLOOKUP(B353,$H:$I,2,FALSE)"
    @eval_fn
    def C353():
        b353_1 = SNG.B353()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b353_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A354():
    # 'SNG'!A354
    value = 44362
    isdatetime = True

@register(SNG)
class B354():
    # 'SNG'!B354
    value = 2021
    formula = "=YEAR(A354)"
    @eval_fn
    def B354():
        a354_1 = SNG.A354()
        var_1 = YEAR(a354_1)
        return var_1

@register(SNG)
class C354():
    # 'SNG'!C354
    value = "#N/A"
    formula = "=VLOOKUP(B354,$H:$I,2,FALSE)"
    @eval_fn
    def C354():
        b354_1 = SNG.B354()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b354_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A355():
    # 'SNG'!A355
    value = 44392
    isdatetime = True

@register(SNG)
class B355():
    # 'SNG'!B355
    value = 2021
    formula = "=YEAR(A355)"
    @eval_fn
    def B355():
        a355_1 = SNG.A355()
        var_1 = YEAR(a355_1)
        return var_1

@register(SNG)
class C355():
    # 'SNG'!C355
    value = "#N/A"
    formula = "=VLOOKUP(B355,$H:$I,2,FALSE)"
    @eval_fn
    def C355():
        b355_1 = SNG.B355()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b355_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A356():
    # 'SNG'!A356
    value = 44423
    isdatetime = True

@register(SNG)
class B356():
    # 'SNG'!B356
    value = 2021
    formula = "=YEAR(A356)"
    @eval_fn
    def B356():
        a356_1 = SNG.A356()
        var_1 = YEAR(a356_1)
        return var_1

@register(SNG)
class C356():
    # 'SNG'!C356
    value = "#N/A"
    formula = "=VLOOKUP(B356,$H:$I,2,FALSE)"
    @eval_fn
    def C356():
        b356_1 = SNG.B356()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b356_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A357():
    # 'SNG'!A357
    value = 44454
    isdatetime = True

@register(SNG)
class B357():
    # 'SNG'!B357
    value = 2021
    formula = "=YEAR(A357)"
    @eval_fn
    def B357():
        a357_1 = SNG.A357()
        var_1 = YEAR(a357_1)
        return var_1

@register(SNG)
class C357():
    # 'SNG'!C357
    value = "#N/A"
    formula = "=VLOOKUP(B357,$H:$I,2,FALSE)"
    @eval_fn
    def C357():
        b357_1 = SNG.B357()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b357_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A358():
    # 'SNG'!A358
    value = 44484
    isdatetime = True

@register(SNG)
class B358():
    # 'SNG'!B358
    value = 2021
    formula = "=YEAR(A358)"
    @eval_fn
    def B358():
        a358_1 = SNG.A358()
        var_1 = YEAR(a358_1)
        return var_1

@register(SNG)
class C358():
    # 'SNG'!C358
    value = "#N/A"
    formula = "=VLOOKUP(B358,$H:$I,2,FALSE)"
    @eval_fn
    def C358():
        b358_1 = SNG.B358()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b358_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A359():
    # 'SNG'!A359
    value = 44515
    isdatetime = True

@register(SNG)
class B359():
    # 'SNG'!B359
    value = 2021
    formula = "=YEAR(A359)"
    @eval_fn
    def B359():
        a359_1 = SNG.A359()
        var_1 = YEAR(a359_1)
        return var_1

@register(SNG)
class C359():
    # 'SNG'!C359
    value = "#N/A"
    formula = "=VLOOKUP(B359,$H:$I,2,FALSE)"
    @eval_fn
    def C359():
        b359_1 = SNG.B359()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b359_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A360():
    # 'SNG'!A360
    value = 44545
    isdatetime = True

@register(SNG)
class B360():
    # 'SNG'!B360
    value = 2021
    formula = "=YEAR(A360)"
    @eval_fn
    def B360():
        a360_1 = SNG.A360()
        var_1 = YEAR(a360_1)
        return var_1

@register(SNG)
class C360():
    # 'SNG'!C360
    value = "#N/A"
    formula = "=VLOOKUP(B360,$H:$I,2,FALSE)"
    @eval_fn
    def C360():
        b360_1 = SNG.B360()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b360_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A361():
    # 'SNG'!A361
    value = 44576
    isdatetime = True

@register(SNG)
class B361():
    # 'SNG'!B361
    value = 2022
    formula = "=YEAR(A361)"
    @eval_fn
    def B361():
        a361_1 = SNG.A361()
        var_1 = YEAR(a361_1)
        return var_1

@register(SNG)
class C361():
    # 'SNG'!C361
    value = "#N/A"
    formula = "=VLOOKUP(B361,$H:$I,2,FALSE)"
    @eval_fn
    def C361():
        b361_1 = SNG.B361()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b361_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A362():
    # 'SNG'!A362
    value = 44607
    isdatetime = True

@register(SNG)
class B362():
    # 'SNG'!B362
    value = 2022
    formula = "=YEAR(A362)"
    @eval_fn
    def B362():
        a362_1 = SNG.A362()
        var_1 = YEAR(a362_1)
        return var_1

@register(SNG)
class C362():
    # 'SNG'!C362
    value = "#N/A"
    formula = "=VLOOKUP(B362,$H:$I,2,FALSE)"
    @eval_fn
    def C362():
        b362_1 = SNG.B362()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b362_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A363():
    # 'SNG'!A363
    value = 44635
    isdatetime = True

@register(SNG)
class B363():
    # 'SNG'!B363
    value = 2022
    formula = "=YEAR(A363)"
    @eval_fn
    def B363():
        a363_1 = SNG.A363()
        var_1 = YEAR(a363_1)
        return var_1

@register(SNG)
class C363():
    # 'SNG'!C363
    value = "#N/A"
    formula = "=VLOOKUP(B363,$H:$I,2,FALSE)"
    @eval_fn
    def C363():
        b363_1 = SNG.B363()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b363_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A364():
    # 'SNG'!A364
    value = 44666
    isdatetime = True

@register(SNG)
class B364():
    # 'SNG'!B364
    value = 2022
    formula = "=YEAR(A364)"
    @eval_fn
    def B364():
        a364_1 = SNG.A364()
        var_1 = YEAR(a364_1)
        return var_1

@register(SNG)
class C364():
    # 'SNG'!C364
    value = "#N/A"
    formula = "=VLOOKUP(B364,$H:$I,2,FALSE)"
    @eval_fn
    def C364():
        b364_1 = SNG.B364()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b364_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A365():
    # 'SNG'!A365
    value = 44696
    isdatetime = True

@register(SNG)
class B365():
    # 'SNG'!B365
    value = 2022
    formula = "=YEAR(A365)"
    @eval_fn
    def B365():
        a365_1 = SNG.A365()
        var_1 = YEAR(a365_1)
        return var_1

@register(SNG)
class C365():
    # 'SNG'!C365
    value = "#N/A"
    formula = "=VLOOKUP(B365,$H:$I,2,FALSE)"
    @eval_fn
    def C365():
        b365_1 = SNG.B365()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b365_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A366():
    # 'SNG'!A366
    value = 44727
    isdatetime = True

@register(SNG)
class B366():
    # 'SNG'!B366
    value = 2022
    formula = "=YEAR(A366)"
    @eval_fn
    def B366():
        a366_1 = SNG.A366()
        var_1 = YEAR(a366_1)
        return var_1

@register(SNG)
class C366():
    # 'SNG'!C366
    value = "#N/A"
    formula = "=VLOOKUP(B366,$H:$I,2,FALSE)"
    @eval_fn
    def C366():
        b366_1 = SNG.B366()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b366_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A367():
    # 'SNG'!A367
    value = 44757
    isdatetime = True

@register(SNG)
class B367():
    # 'SNG'!B367
    value = 2022
    formula = "=YEAR(A367)"
    @eval_fn
    def B367():
        a367_1 = SNG.A367()
        var_1 = YEAR(a367_1)
        return var_1

@register(SNG)
class C367():
    # 'SNG'!C367
    value = "#N/A"
    formula = "=VLOOKUP(B367,$H:$I,2,FALSE)"
    @eval_fn
    def C367():
        b367_1 = SNG.B367()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b367_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A368():
    # 'SNG'!A368
    value = 44788
    isdatetime = True

@register(SNG)
class B368():
    # 'SNG'!B368
    value = 2022
    formula = "=YEAR(A368)"
    @eval_fn
    def B368():
        a368_1 = SNG.A368()
        var_1 = YEAR(a368_1)
        return var_1

@register(SNG)
class C368():
    # 'SNG'!C368
    value = "#N/A"
    formula = "=VLOOKUP(B368,$H:$I,2,FALSE)"
    @eval_fn
    def C368():
        b368_1 = SNG.B368()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b368_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A369():
    # 'SNG'!A369
    value = 44819
    isdatetime = True

@register(SNG)
class B369():
    # 'SNG'!B369
    value = 2022
    formula = "=YEAR(A369)"
    @eval_fn
    def B369():
        a369_1 = SNG.A369()
        var_1 = YEAR(a369_1)
        return var_1

@register(SNG)
class C369():
    # 'SNG'!C369
    value = "#N/A"
    formula = "=VLOOKUP(B369,$H:$I,2,FALSE)"
    @eval_fn
    def C369():
        b369_1 = SNG.B369()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b369_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A370():
    # 'SNG'!A370
    value = 44849
    isdatetime = True

@register(SNG)
class B370():
    # 'SNG'!B370
    value = 2022
    formula = "=YEAR(A370)"
    @eval_fn
    def B370():
        a370_1 = SNG.A370()
        var_1 = YEAR(a370_1)
        return var_1

@register(SNG)
class C370():
    # 'SNG'!C370
    value = "#N/A"
    formula = "=VLOOKUP(B370,$H:$I,2,FALSE)"
    @eval_fn
    def C370():
        b370_1 = SNG.B370()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b370_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A371():
    # 'SNG'!A371
    value = 44880
    isdatetime = True

@register(SNG)
class B371():
    # 'SNG'!B371
    value = 2022
    formula = "=YEAR(A371)"
    @eval_fn
    def B371():
        a371_1 = SNG.A371()
        var_1 = YEAR(a371_1)
        return var_1

@register(SNG)
class C371():
    # 'SNG'!C371
    value = "#N/A"
    formula = "=VLOOKUP(B371,$H:$I,2,FALSE)"
    @eval_fn
    def C371():
        b371_1 = SNG.B371()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b371_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A372():
    # 'SNG'!A372
    value = 44910
    isdatetime = True

@register(SNG)
class B372():
    # 'SNG'!B372
    value = 2022
    formula = "=YEAR(A372)"
    @eval_fn
    def B372():
        a372_1 = SNG.A372()
        var_1 = YEAR(a372_1)
        return var_1

@register(SNG)
class C372():
    # 'SNG'!C372
    value = "#N/A"
    formula = "=VLOOKUP(B372,$H:$I,2,FALSE)"
    @eval_fn
    def C372():
        b372_1 = SNG.B372()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b372_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A373():
    # 'SNG'!A373
    value = 44941
    isdatetime = True

@register(SNG)
class B373():
    # 'SNG'!B373
    value = 2023
    formula = "=YEAR(A373)"
    @eval_fn
    def B373():
        a373_1 = SNG.A373()
        var_1 = YEAR(a373_1)
        return var_1

@register(SNG)
class C373():
    # 'SNG'!C373
    value = "#N/A"
    formula = "=VLOOKUP(B373,$H:$I,2,FALSE)"
    @eval_fn
    def C373():
        b373_1 = SNG.B373()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b373_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A374():
    # 'SNG'!A374
    value = 44972
    isdatetime = True

@register(SNG)
class B374():
    # 'SNG'!B374
    value = 2023
    formula = "=YEAR(A374)"
    @eval_fn
    def B374():
        a374_1 = SNG.A374()
        var_1 = YEAR(a374_1)
        return var_1

@register(SNG)
class C374():
    # 'SNG'!C374
    value = "#N/A"
    formula = "=VLOOKUP(B374,$H:$I,2,FALSE)"
    @eval_fn
    def C374():
        b374_1 = SNG.B374()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b374_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A375():
    # 'SNG'!A375
    value = 45000
    isdatetime = True

@register(SNG)
class B375():
    # 'SNG'!B375
    value = 2023
    formula = "=YEAR(A375)"
    @eval_fn
    def B375():
        a375_1 = SNG.A375()
        var_1 = YEAR(a375_1)
        return var_1

@register(SNG)
class C375():
    # 'SNG'!C375
    value = "#N/A"
    formula = "=VLOOKUP(B375,$H:$I,2,FALSE)"
    @eval_fn
    def C375():
        b375_1 = SNG.B375()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b375_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A376():
    # 'SNG'!A376
    value = 45031
    isdatetime = True

@register(SNG)
class B376():
    # 'SNG'!B376
    value = 2023
    formula = "=YEAR(A376)"
    @eval_fn
    def B376():
        a376_1 = SNG.A376()
        var_1 = YEAR(a376_1)
        return var_1

@register(SNG)
class C376():
    # 'SNG'!C376
    value = "#N/A"
    formula = "=VLOOKUP(B376,$H:$I,2,FALSE)"
    @eval_fn
    def C376():
        b376_1 = SNG.B376()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b376_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A377():
    # 'SNG'!A377
    value = 45061
    isdatetime = True

@register(SNG)
class B377():
    # 'SNG'!B377
    value = 2023
    formula = "=YEAR(A377)"
    @eval_fn
    def B377():
        a377_1 = SNG.A377()
        var_1 = YEAR(a377_1)
        return var_1

@register(SNG)
class C377():
    # 'SNG'!C377
    value = "#N/A"
    formula = "=VLOOKUP(B377,$H:$I,2,FALSE)"
    @eval_fn
    def C377():
        b377_1 = SNG.B377()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b377_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A378():
    # 'SNG'!A378
    value = 45092
    isdatetime = True

@register(SNG)
class B378():
    # 'SNG'!B378
    value = 2023
    formula = "=YEAR(A378)"
    @eval_fn
    def B378():
        a378_1 = SNG.A378()
        var_1 = YEAR(a378_1)
        return var_1

@register(SNG)
class C378():
    # 'SNG'!C378
    value = "#N/A"
    formula = "=VLOOKUP(B378,$H:$I,2,FALSE)"
    @eval_fn
    def C378():
        b378_1 = SNG.B378()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b378_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A379():
    # 'SNG'!A379
    value = 45122
    isdatetime = True

@register(SNG)
class B379():
    # 'SNG'!B379
    value = 2023
    formula = "=YEAR(A379)"
    @eval_fn
    def B379():
        a379_1 = SNG.A379()
        var_1 = YEAR(a379_1)
        return var_1

@register(SNG)
class C379():
    # 'SNG'!C379
    value = "#N/A"
    formula = "=VLOOKUP(B379,$H:$I,2,FALSE)"
    @eval_fn
    def C379():
        b379_1 = SNG.B379()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b379_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A380():
    # 'SNG'!A380
    value = 45153
    isdatetime = True

@register(SNG)
class B380():
    # 'SNG'!B380
    value = 2023
    formula = "=YEAR(A380)"
    @eval_fn
    def B380():
        a380_1 = SNG.A380()
        var_1 = YEAR(a380_1)
        return var_1

@register(SNG)
class C380():
    # 'SNG'!C380
    value = "#N/A"
    formula = "=VLOOKUP(B380,$H:$I,2,FALSE)"
    @eval_fn
    def C380():
        b380_1 = SNG.B380()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b380_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A381():
    # 'SNG'!A381
    value = 45184
    isdatetime = True

@register(SNG)
class B381():
    # 'SNG'!B381
    value = 2023
    formula = "=YEAR(A381)"
    @eval_fn
    def B381():
        a381_1 = SNG.A381()
        var_1 = YEAR(a381_1)
        return var_1

@register(SNG)
class C381():
    # 'SNG'!C381
    value = "#N/A"
    formula = "=VLOOKUP(B381,$H:$I,2,FALSE)"
    @eval_fn
    def C381():
        b381_1 = SNG.B381()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b381_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A382():
    # 'SNG'!A382
    value = 45214
    isdatetime = True

@register(SNG)
class B382():
    # 'SNG'!B382
    value = 2023
    formula = "=YEAR(A382)"
    @eval_fn
    def B382():
        a382_1 = SNG.A382()
        var_1 = YEAR(a382_1)
        return var_1

@register(SNG)
class C382():
    # 'SNG'!C382
    value = "#N/A"
    formula = "=VLOOKUP(B382,$H:$I,2,FALSE)"
    @eval_fn
    def C382():
        b382_1 = SNG.B382()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b382_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A383():
    # 'SNG'!A383
    value = 45245
    isdatetime = True

@register(SNG)
class B383():
    # 'SNG'!B383
    value = 2023
    formula = "=YEAR(A383)"
    @eval_fn
    def B383():
        a383_1 = SNG.A383()
        var_1 = YEAR(a383_1)
        return var_1

@register(SNG)
class C383():
    # 'SNG'!C383
    value = "#N/A"
    formula = "=VLOOKUP(B383,$H:$I,2,FALSE)"
    @eval_fn
    def C383():
        b383_1 = SNG.B383()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b383_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A384():
    # 'SNG'!A384
    value = 45275
    isdatetime = True

@register(SNG)
class B384():
    # 'SNG'!B384
    value = 2023
    formula = "=YEAR(A384)"
    @eval_fn
    def B384():
        a384_1 = SNG.A384()
        var_1 = YEAR(a384_1)
        return var_1

@register(SNG)
class C384():
    # 'SNG'!C384
    value = "#N/A"
    formula = "=VLOOKUP(B384,$H:$I,2,FALSE)"
    @eval_fn
    def C384():
        b384_1 = SNG.B384()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b384_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A385():
    # 'SNG'!A385
    value = 45306
    isdatetime = True

@register(SNG)
class B385():
    # 'SNG'!B385
    value = 2024
    formula = "=YEAR(A385)"
    @eval_fn
    def B385():
        a385_1 = SNG.A385()
        var_1 = YEAR(a385_1)
        return var_1

@register(SNG)
class C385():
    # 'SNG'!C385
    value = "#N/A"
    formula = "=VLOOKUP(B385,$H:$I,2,FALSE)"
    @eval_fn
    def C385():
        b385_1 = SNG.B385()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b385_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A386():
    # 'SNG'!A386
    value = 45337
    isdatetime = True

@register(SNG)
class B386():
    # 'SNG'!B386
    value = 2024
    formula = "=YEAR(A386)"
    @eval_fn
    def B386():
        a386_1 = SNG.A386()
        var_1 = YEAR(a386_1)
        return var_1

@register(SNG)
class C386():
    # 'SNG'!C386
    value = "#N/A"
    formula = "=VLOOKUP(B386,$H:$I,2,FALSE)"
    @eval_fn
    def C386():
        b386_1 = SNG.B386()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b386_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A387():
    # 'SNG'!A387
    value = 45366
    isdatetime = True

@register(SNG)
class B387():
    # 'SNG'!B387
    value = 2024
    formula = "=YEAR(A387)"
    @eval_fn
    def B387():
        a387_1 = SNG.A387()
        var_1 = YEAR(a387_1)
        return var_1

@register(SNG)
class C387():
    # 'SNG'!C387
    value = "#N/A"
    formula = "=VLOOKUP(B387,$H:$I,2,FALSE)"
    @eval_fn
    def C387():
        b387_1 = SNG.B387()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b387_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A388():
    # 'SNG'!A388
    value = 45397
    isdatetime = True

@register(SNG)
class B388():
    # 'SNG'!B388
    value = 2024
    formula = "=YEAR(A388)"
    @eval_fn
    def B388():
        a388_1 = SNG.A388()
        var_1 = YEAR(a388_1)
        return var_1

@register(SNG)
class C388():
    # 'SNG'!C388
    value = "#N/A"
    formula = "=VLOOKUP(B388,$H:$I,2,FALSE)"
    @eval_fn
    def C388():
        b388_1 = SNG.B388()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b388_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A389():
    # 'SNG'!A389
    value = 45427
    isdatetime = True

@register(SNG)
class B389():
    # 'SNG'!B389
    value = 2024
    formula = "=YEAR(A389)"
    @eval_fn
    def B389():
        a389_1 = SNG.A389()
        var_1 = YEAR(a389_1)
        return var_1

@register(SNG)
class C389():
    # 'SNG'!C389
    value = "#N/A"
    formula = "=VLOOKUP(B389,$H:$I,2,FALSE)"
    @eval_fn
    def C389():
        b389_1 = SNG.B389()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b389_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A390():
    # 'SNG'!A390
    value = 45458
    isdatetime = True

@register(SNG)
class B390():
    # 'SNG'!B390
    value = 2024
    formula = "=YEAR(A390)"
    @eval_fn
    def B390():
        a390_1 = SNG.A390()
        var_1 = YEAR(a390_1)
        return var_1

@register(SNG)
class C390():
    # 'SNG'!C390
    value = "#N/A"
    formula = "=VLOOKUP(B390,$H:$I,2,FALSE)"
    @eval_fn
    def C390():
        b390_1 = SNG.B390()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b390_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A391():
    # 'SNG'!A391
    value = 45488
    isdatetime = True

@register(SNG)
class B391():
    # 'SNG'!B391
    value = 2024
    formula = "=YEAR(A391)"
    @eval_fn
    def B391():
        a391_1 = SNG.A391()
        var_1 = YEAR(a391_1)
        return var_1

@register(SNG)
class C391():
    # 'SNG'!C391
    value = "#N/A"
    formula = "=VLOOKUP(B391,$H:$I,2,FALSE)"
    @eval_fn
    def C391():
        b391_1 = SNG.B391()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b391_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A392():
    # 'SNG'!A392
    value = 45519
    isdatetime = True

@register(SNG)
class B392():
    # 'SNG'!B392
    value = 2024
    formula = "=YEAR(A392)"
    @eval_fn
    def B392():
        a392_1 = SNG.A392()
        var_1 = YEAR(a392_1)
        return var_1

@register(SNG)
class C392():
    # 'SNG'!C392
    value = "#N/A"
    formula = "=VLOOKUP(B392,$H:$I,2,FALSE)"
    @eval_fn
    def C392():
        b392_1 = SNG.B392()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b392_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A393():
    # 'SNG'!A393
    value = 45550
    isdatetime = True

@register(SNG)
class B393():
    # 'SNG'!B393
    value = 2024
    formula = "=YEAR(A393)"
    @eval_fn
    def B393():
        a393_1 = SNG.A393()
        var_1 = YEAR(a393_1)
        return var_1

@register(SNG)
class C393():
    # 'SNG'!C393
    value = "#N/A"
    formula = "=VLOOKUP(B393,$H:$I,2,FALSE)"
    @eval_fn
    def C393():
        b393_1 = SNG.B393()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b393_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A394():
    # 'SNG'!A394
    value = 45580
    isdatetime = True

@register(SNG)
class B394():
    # 'SNG'!B394
    value = 2024
    formula = "=YEAR(A394)"
    @eval_fn
    def B394():
        a394_1 = SNG.A394()
        var_1 = YEAR(a394_1)
        return var_1

@register(SNG)
class C394():
    # 'SNG'!C394
    value = "#N/A"
    formula = "=VLOOKUP(B394,$H:$I,2,FALSE)"
    @eval_fn
    def C394():
        b394_1 = SNG.B394()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b394_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A395():
    # 'SNG'!A395
    value = 45611
    isdatetime = True

@register(SNG)
class B395():
    # 'SNG'!B395
    value = 2024
    formula = "=YEAR(A395)"
    @eval_fn
    def B395():
        a395_1 = SNG.A395()
        var_1 = YEAR(a395_1)
        return var_1

@register(SNG)
class C395():
    # 'SNG'!C395
    value = "#N/A"
    formula = "=VLOOKUP(B395,$H:$I,2,FALSE)"
    @eval_fn
    def C395():
        b395_1 = SNG.B395()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b395_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A396():
    # 'SNG'!A396
    value = 45641
    isdatetime = True

@register(SNG)
class B396():
    # 'SNG'!B396
    value = 2024
    formula = "=YEAR(A396)"
    @eval_fn
    def B396():
        a396_1 = SNG.A396()
        var_1 = YEAR(a396_1)
        return var_1

@register(SNG)
class C396():
    # 'SNG'!C396
    value = "#N/A"
    formula = "=VLOOKUP(B396,$H:$I,2,FALSE)"
    @eval_fn
    def C396():
        b396_1 = SNG.B396()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b396_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A397():
    # 'SNG'!A397
    value = 45672
    isdatetime = True

@register(SNG)
class B397():
    # 'SNG'!B397
    value = 2025
    formula = "=YEAR(A397)"
    @eval_fn
    def B397():
        a397_1 = SNG.A397()
        var_1 = YEAR(a397_1)
        return var_1

@register(SNG)
class C397():
    # 'SNG'!C397
    value = "#N/A"
    formula = "=VLOOKUP(B397,$H:$I,2,FALSE)"
    @eval_fn
    def C397():
        b397_1 = SNG.B397()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b397_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A398():
    # 'SNG'!A398
    value = 45703
    isdatetime = True

@register(SNG)
class B398():
    # 'SNG'!B398
    value = 2025
    formula = "=YEAR(A398)"
    @eval_fn
    def B398():
        a398_1 = SNG.A398()
        var_1 = YEAR(a398_1)
        return var_1

@register(SNG)
class C398():
    # 'SNG'!C398
    value = "#N/A"
    formula = "=VLOOKUP(B398,$H:$I,2,FALSE)"
    @eval_fn
    def C398():
        b398_1 = SNG.B398()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b398_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A399():
    # 'SNG'!A399
    value = 45731
    isdatetime = True

@register(SNG)
class B399():
    # 'SNG'!B399
    value = 2025
    formula = "=YEAR(A399)"
    @eval_fn
    def B399():
        a399_1 = SNG.A399()
        var_1 = YEAR(a399_1)
        return var_1

@register(SNG)
class C399():
    # 'SNG'!C399
    value = "#N/A"
    formula = "=VLOOKUP(B399,$H:$I,2,FALSE)"
    @eval_fn
    def C399():
        b399_1 = SNG.B399()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b399_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A400():
    # 'SNG'!A400
    value = 45762
    isdatetime = True

@register(SNG)
class B400():
    # 'SNG'!B400
    value = 2025
    formula = "=YEAR(A400)"
    @eval_fn
    def B400():
        a400_1 = SNG.A400()
        var_1 = YEAR(a400_1)
        return var_1

@register(SNG)
class C400():
    # 'SNG'!C400
    value = "#N/A"
    formula = "=VLOOKUP(B400,$H:$I,2,FALSE)"
    @eval_fn
    def C400():
        b400_1 = SNG.B400()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b400_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A401():
    # 'SNG'!A401
    value = 45792
    isdatetime = True

@register(SNG)
class B401():
    # 'SNG'!B401
    value = 2025
    formula = "=YEAR(A401)"
    @eval_fn
    def B401():
        a401_1 = SNG.A401()
        var_1 = YEAR(a401_1)
        return var_1

@register(SNG)
class C401():
    # 'SNG'!C401
    value = "#N/A"
    formula = "=VLOOKUP(B401,$H:$I,2,FALSE)"
    @eval_fn
    def C401():
        b401_1 = SNG.B401()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b401_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A402():
    # 'SNG'!A402
    value = 45823
    isdatetime = True

@register(SNG)
class B402():
    # 'SNG'!B402
    value = 2025
    formula = "=YEAR(A402)"
    @eval_fn
    def B402():
        a402_1 = SNG.A402()
        var_1 = YEAR(a402_1)
        return var_1

@register(SNG)
class C402():
    # 'SNG'!C402
    value = "#N/A"
    formula = "=VLOOKUP(B402,$H:$I,2,FALSE)"
    @eval_fn
    def C402():
        b402_1 = SNG.B402()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b402_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A403():
    # 'SNG'!A403
    value = 45853
    isdatetime = True

@register(SNG)
class B403():
    # 'SNG'!B403
    value = 2025
    formula = "=YEAR(A403)"
    @eval_fn
    def B403():
        a403_1 = SNG.A403()
        var_1 = YEAR(a403_1)
        return var_1

@register(SNG)
class C403():
    # 'SNG'!C403
    value = "#N/A"
    formula = "=VLOOKUP(B403,$H:$I,2,FALSE)"
    @eval_fn
    def C403():
        b403_1 = SNG.B403()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b403_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A404():
    # 'SNG'!A404
    value = 45884
    isdatetime = True

@register(SNG)
class B404():
    # 'SNG'!B404
    value = 2025
    formula = "=YEAR(A404)"
    @eval_fn
    def B404():
        a404_1 = SNG.A404()
        var_1 = YEAR(a404_1)
        return var_1

@register(SNG)
class C404():
    # 'SNG'!C404
    value = "#N/A"
    formula = "=VLOOKUP(B404,$H:$I,2,FALSE)"
    @eval_fn
    def C404():
        b404_1 = SNG.B404()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b404_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A405():
    # 'SNG'!A405
    value = 45915
    isdatetime = True

@register(SNG)
class B405():
    # 'SNG'!B405
    value = 2025
    formula = "=YEAR(A405)"
    @eval_fn
    def B405():
        a405_1 = SNG.A405()
        var_1 = YEAR(a405_1)
        return var_1

@register(SNG)
class C405():
    # 'SNG'!C405
    value = "#N/A"
    formula = "=VLOOKUP(B405,$H:$I,2,FALSE)"
    @eval_fn
    def C405():
        b405_1 = SNG.B405()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b405_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A406():
    # 'SNG'!A406
    value = 45945
    isdatetime = True

@register(SNG)
class B406():
    # 'SNG'!B406
    value = 2025
    formula = "=YEAR(A406)"
    @eval_fn
    def B406():
        a406_1 = SNG.A406()
        var_1 = YEAR(a406_1)
        return var_1

@register(SNG)
class C406():
    # 'SNG'!C406
    value = "#N/A"
    formula = "=VLOOKUP(B406,$H:$I,2,FALSE)"
    @eval_fn
    def C406():
        b406_1 = SNG.B406()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b406_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A407():
    # 'SNG'!A407
    value = 45976
    isdatetime = True

@register(SNG)
class B407():
    # 'SNG'!B407
    value = 2025
    formula = "=YEAR(A407)"
    @eval_fn
    def B407():
        a407_1 = SNG.A407()
        var_1 = YEAR(a407_1)
        return var_1

@register(SNG)
class C407():
    # 'SNG'!C407
    value = "#N/A"
    formula = "=VLOOKUP(B407,$H:$I,2,FALSE)"
    @eval_fn
    def C407():
        b407_1 = SNG.B407()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b407_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A408():
    # 'SNG'!A408
    value = 46006
    isdatetime = True

@register(SNG)
class B408():
    # 'SNG'!B408
    value = 2025
    formula = "=YEAR(A408)"
    @eval_fn
    def B408():
        a408_1 = SNG.A408()
        var_1 = YEAR(a408_1)
        return var_1

@register(SNG)
class C408():
    # 'SNG'!C408
    value = "#N/A"
    formula = "=VLOOKUP(B408,$H:$I,2,FALSE)"
    @eval_fn
    def C408():
        b408_1 = SNG.B408()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b408_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A409():
    # 'SNG'!A409
    value = 46037
    isdatetime = True

@register(SNG)
class B409():
    # 'SNG'!B409
    value = 2026
    formula = "=YEAR(A409)"
    @eval_fn
    def B409():
        a409_1 = SNG.A409()
        var_1 = YEAR(a409_1)
        return var_1

@register(SNG)
class C409():
    # 'SNG'!C409
    value = "#N/A"
    formula = "=VLOOKUP(B409,$H:$I,2,FALSE)"
    @eval_fn
    def C409():
        b409_1 = SNG.B409()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b409_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A410():
    # 'SNG'!A410
    value = 46068
    isdatetime = True

@register(SNG)
class B410():
    # 'SNG'!B410
    value = 2026
    formula = "=YEAR(A410)"
    @eval_fn
    def B410():
        a410_1 = SNG.A410()
        var_1 = YEAR(a410_1)
        return var_1

@register(SNG)
class C410():
    # 'SNG'!C410
    value = "#N/A"
    formula = "=VLOOKUP(B410,$H:$I,2,FALSE)"
    @eval_fn
    def C410():
        b410_1 = SNG.B410()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b410_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A411():
    # 'SNG'!A411
    value = 46096
    isdatetime = True

@register(SNG)
class B411():
    # 'SNG'!B411
    value = 2026
    formula = "=YEAR(A411)"
    @eval_fn
    def B411():
        a411_1 = SNG.A411()
        var_1 = YEAR(a411_1)
        return var_1

@register(SNG)
class C411():
    # 'SNG'!C411
    value = "#N/A"
    formula = "=VLOOKUP(B411,$H:$I,2,FALSE)"
    @eval_fn
    def C411():
        b411_1 = SNG.B411()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b411_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A412():
    # 'SNG'!A412
    value = 46127
    isdatetime = True

@register(SNG)
class B412():
    # 'SNG'!B412
    value = 2026
    formula = "=YEAR(A412)"
    @eval_fn
    def B412():
        a412_1 = SNG.A412()
        var_1 = YEAR(a412_1)
        return var_1

@register(SNG)
class C412():
    # 'SNG'!C412
    value = "#N/A"
    formula = "=VLOOKUP(B412,$H:$I,2,FALSE)"
    @eval_fn
    def C412():
        b412_1 = SNG.B412()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b412_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A413():
    # 'SNG'!A413
    value = 46157
    isdatetime = True

@register(SNG)
class B413():
    # 'SNG'!B413
    value = 2026
    formula = "=YEAR(A413)"
    @eval_fn
    def B413():
        a413_1 = SNG.A413()
        var_1 = YEAR(a413_1)
        return var_1

@register(SNG)
class C413():
    # 'SNG'!C413
    value = "#N/A"
    formula = "=VLOOKUP(B413,$H:$I,2,FALSE)"
    @eval_fn
    def C413():
        b413_1 = SNG.B413()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b413_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A414():
    # 'SNG'!A414
    value = 46188
    isdatetime = True

@register(SNG)
class B414():
    # 'SNG'!B414
    value = 2026
    formula = "=YEAR(A414)"
    @eval_fn
    def B414():
        a414_1 = SNG.A414()
        var_1 = YEAR(a414_1)
        return var_1

@register(SNG)
class C414():
    # 'SNG'!C414
    value = "#N/A"
    formula = "=VLOOKUP(B414,$H:$I,2,FALSE)"
    @eval_fn
    def C414():
        b414_1 = SNG.B414()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b414_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A415():
    # 'SNG'!A415
    value = 46218
    isdatetime = True

@register(SNG)
class B415():
    # 'SNG'!B415
    value = 2026
    formula = "=YEAR(A415)"
    @eval_fn
    def B415():
        a415_1 = SNG.A415()
        var_1 = YEAR(a415_1)
        return var_1

@register(SNG)
class C415():
    # 'SNG'!C415
    value = "#N/A"
    formula = "=VLOOKUP(B415,$H:$I,2,FALSE)"
    @eval_fn
    def C415():
        b415_1 = SNG.B415()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b415_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A416():
    # 'SNG'!A416
    value = 46249
    isdatetime = True

@register(SNG)
class B416():
    # 'SNG'!B416
    value = 2026
    formula = "=YEAR(A416)"
    @eval_fn
    def B416():
        a416_1 = SNG.A416()
        var_1 = YEAR(a416_1)
        return var_1

@register(SNG)
class C416():
    # 'SNG'!C416
    value = "#N/A"
    formula = "=VLOOKUP(B416,$H:$I,2,FALSE)"
    @eval_fn
    def C416():
        b416_1 = SNG.B416()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b416_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A417():
    # 'SNG'!A417
    value = 46280
    isdatetime = True

@register(SNG)
class B417():
    # 'SNG'!B417
    value = 2026
    formula = "=YEAR(A417)"
    @eval_fn
    def B417():
        a417_1 = SNG.A417()
        var_1 = YEAR(a417_1)
        return var_1

@register(SNG)
class C417():
    # 'SNG'!C417
    value = "#N/A"
    formula = "=VLOOKUP(B417,$H:$I,2,FALSE)"
    @eval_fn
    def C417():
        b417_1 = SNG.B417()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b417_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A418():
    # 'SNG'!A418
    value = 46310
    isdatetime = True

@register(SNG)
class B418():
    # 'SNG'!B418
    value = 2026
    formula = "=YEAR(A418)"
    @eval_fn
    def B418():
        a418_1 = SNG.A418()
        var_1 = YEAR(a418_1)
        return var_1

@register(SNG)
class C418():
    # 'SNG'!C418
    value = "#N/A"
    formula = "=VLOOKUP(B418,$H:$I,2,FALSE)"
    @eval_fn
    def C418():
        b418_1 = SNG.B418()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b418_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A419():
    # 'SNG'!A419
    value = 46341
    isdatetime = True

@register(SNG)
class B419():
    # 'SNG'!B419
    value = 2026
    formula = "=YEAR(A419)"
    @eval_fn
    def B419():
        a419_1 = SNG.A419()
        var_1 = YEAR(a419_1)
        return var_1

@register(SNG)
class C419():
    # 'SNG'!C419
    value = "#N/A"
    formula = "=VLOOKUP(B419,$H:$I,2,FALSE)"
    @eval_fn
    def C419():
        b419_1 = SNG.B419()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b419_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A420():
    # 'SNG'!A420
    value = 46371
    isdatetime = True

@register(SNG)
class B420():
    # 'SNG'!B420
    value = 2026
    formula = "=YEAR(A420)"
    @eval_fn
    def B420():
        a420_1 = SNG.A420()
        var_1 = YEAR(a420_1)
        return var_1

@register(SNG)
class C420():
    # 'SNG'!C420
    value = "#N/A"
    formula = "=VLOOKUP(B420,$H:$I,2,FALSE)"
    @eval_fn
    def C420():
        b420_1 = SNG.B420()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b420_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A421():
    # 'SNG'!A421
    value = 46402
    isdatetime = True

@register(SNG)
class B421():
    # 'SNG'!B421
    value = 2027
    formula = "=YEAR(A421)"
    @eval_fn
    def B421():
        a421_1 = SNG.A421()
        var_1 = YEAR(a421_1)
        return var_1

@register(SNG)
class C421():
    # 'SNG'!C421
    value = "#N/A"
    formula = "=VLOOKUP(B421,$H:$I,2,FALSE)"
    @eval_fn
    def C421():
        b421_1 = SNG.B421()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b421_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A422():
    # 'SNG'!A422
    value = 46433
    isdatetime = True

@register(SNG)
class B422():
    # 'SNG'!B422
    value = 2027
    formula = "=YEAR(A422)"
    @eval_fn
    def B422():
        a422_1 = SNG.A422()
        var_1 = YEAR(a422_1)
        return var_1

@register(SNG)
class C422():
    # 'SNG'!C422
    value = "#N/A"
    formula = "=VLOOKUP(B422,$H:$I,2,FALSE)"
    @eval_fn
    def C422():
        b422_1 = SNG.B422()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b422_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A423():
    # 'SNG'!A423
    value = 46461
    isdatetime = True

@register(SNG)
class B423():
    # 'SNG'!B423
    value = 2027
    formula = "=YEAR(A423)"
    @eval_fn
    def B423():
        a423_1 = SNG.A423()
        var_1 = YEAR(a423_1)
        return var_1

@register(SNG)
class C423():
    # 'SNG'!C423
    value = "#N/A"
    formula = "=VLOOKUP(B423,$H:$I,2,FALSE)"
    @eval_fn
    def C423():
        b423_1 = SNG.B423()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b423_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A424():
    # 'SNG'!A424
    value = 46492
    isdatetime = True

@register(SNG)
class B424():
    # 'SNG'!B424
    value = 2027
    formula = "=YEAR(A424)"
    @eval_fn
    def B424():
        a424_1 = SNG.A424()
        var_1 = YEAR(a424_1)
        return var_1

@register(SNG)
class C424():
    # 'SNG'!C424
    value = "#N/A"
    formula = "=VLOOKUP(B424,$H:$I,2,FALSE)"
    @eval_fn
    def C424():
        b424_1 = SNG.B424()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b424_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A425():
    # 'SNG'!A425
    value = 46522
    isdatetime = True

@register(SNG)
class B425():
    # 'SNG'!B425
    value = 2027
    formula = "=YEAR(A425)"
    @eval_fn
    def B425():
        a425_1 = SNG.A425()
        var_1 = YEAR(a425_1)
        return var_1

@register(SNG)
class C425():
    # 'SNG'!C425
    value = "#N/A"
    formula = "=VLOOKUP(B425,$H:$I,2,FALSE)"
    @eval_fn
    def C425():
        b425_1 = SNG.B425()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b425_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A426():
    # 'SNG'!A426
    value = 46553
    isdatetime = True

@register(SNG)
class B426():
    # 'SNG'!B426
    value = 2027
    formula = "=YEAR(A426)"
    @eval_fn
    def B426():
        a426_1 = SNG.A426()
        var_1 = YEAR(a426_1)
        return var_1

@register(SNG)
class C426():
    # 'SNG'!C426
    value = "#N/A"
    formula = "=VLOOKUP(B426,$H:$I,2,FALSE)"
    @eval_fn
    def C426():
        b426_1 = SNG.B426()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b426_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A427():
    # 'SNG'!A427
    value = 46583
    isdatetime = True

@register(SNG)
class B427():
    # 'SNG'!B427
    value = 2027
    formula = "=YEAR(A427)"
    @eval_fn
    def B427():
        a427_1 = SNG.A427()
        var_1 = YEAR(a427_1)
        return var_1

@register(SNG)
class C427():
    # 'SNG'!C427
    value = "#N/A"
    formula = "=VLOOKUP(B427,$H:$I,2,FALSE)"
    @eval_fn
    def C427():
        b427_1 = SNG.B427()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b427_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A428():
    # 'SNG'!A428
    value = 46614
    isdatetime = True

@register(SNG)
class B428():
    # 'SNG'!B428
    value = 2027
    formula = "=YEAR(A428)"
    @eval_fn
    def B428():
        a428_1 = SNG.A428()
        var_1 = YEAR(a428_1)
        return var_1

@register(SNG)
class C428():
    # 'SNG'!C428
    value = "#N/A"
    formula = "=VLOOKUP(B428,$H:$I,2,FALSE)"
    @eval_fn
    def C428():
        b428_1 = SNG.B428()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b428_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A429():
    # 'SNG'!A429
    value = 46645
    isdatetime = True

@register(SNG)
class B429():
    # 'SNG'!B429
    value = 2027
    formula = "=YEAR(A429)"
    @eval_fn
    def B429():
        a429_1 = SNG.A429()
        var_1 = YEAR(a429_1)
        return var_1

@register(SNG)
class C429():
    # 'SNG'!C429
    value = "#N/A"
    formula = "=VLOOKUP(B429,$H:$I,2,FALSE)"
    @eval_fn
    def C429():
        b429_1 = SNG.B429()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b429_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A430():
    # 'SNG'!A430
    value = 46675
    isdatetime = True

@register(SNG)
class B430():
    # 'SNG'!B430
    value = 2027
    formula = "=YEAR(A430)"
    @eval_fn
    def B430():
        a430_1 = SNG.A430()
        var_1 = YEAR(a430_1)
        return var_1

@register(SNG)
class C430():
    # 'SNG'!C430
    value = "#N/A"
    formula = "=VLOOKUP(B430,$H:$I,2,FALSE)"
    @eval_fn
    def C430():
        b430_1 = SNG.B430()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b430_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A431():
    # 'SNG'!A431
    value = 46706
    isdatetime = True

@register(SNG)
class B431():
    # 'SNG'!B431
    value = 2027
    formula = "=YEAR(A431)"
    @eval_fn
    def B431():
        a431_1 = SNG.A431()
        var_1 = YEAR(a431_1)
        return var_1

@register(SNG)
class C431():
    # 'SNG'!C431
    value = "#N/A"
    formula = "=VLOOKUP(B431,$H:$I,2,FALSE)"
    @eval_fn
    def C431():
        b431_1 = SNG.B431()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b431_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A432():
    # 'SNG'!A432
    value = 46736
    isdatetime = True

@register(SNG)
class B432():
    # 'SNG'!B432
    value = 2027
    formula = "=YEAR(A432)"
    @eval_fn
    def B432():
        a432_1 = SNG.A432()
        var_1 = YEAR(a432_1)
        return var_1

@register(SNG)
class C432():
    # 'SNG'!C432
    value = "#N/A"
    formula = "=VLOOKUP(B432,$H:$I,2,FALSE)"
    @eval_fn
    def C432():
        b432_1 = SNG.B432()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b432_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A433():
    # 'SNG'!A433
    value = 46767
    isdatetime = True

@register(SNG)
class B433():
    # 'SNG'!B433
    value = 2028
    formula = "=YEAR(A433)"
    @eval_fn
    def B433():
        a433_1 = SNG.A433()
        var_1 = YEAR(a433_1)
        return var_1

@register(SNG)
class C433():
    # 'SNG'!C433
    value = "#N/A"
    formula = "=VLOOKUP(B433,$H:$I,2,FALSE)"
    @eval_fn
    def C433():
        b433_1 = SNG.B433()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b433_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A434():
    # 'SNG'!A434
    value = 46798
    isdatetime = True

@register(SNG)
class B434():
    # 'SNG'!B434
    value = 2028
    formula = "=YEAR(A434)"
    @eval_fn
    def B434():
        a434_1 = SNG.A434()
        var_1 = YEAR(a434_1)
        return var_1

@register(SNG)
class C434():
    # 'SNG'!C434
    value = "#N/A"
    formula = "=VLOOKUP(B434,$H:$I,2,FALSE)"
    @eval_fn
    def C434():
        b434_1 = SNG.B434()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b434_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A435():
    # 'SNG'!A435
    value = 46827
    isdatetime = True

@register(SNG)
class B435():
    # 'SNG'!B435
    value = 2028
    formula = "=YEAR(A435)"
    @eval_fn
    def B435():
        a435_1 = SNG.A435()
        var_1 = YEAR(a435_1)
        return var_1

@register(SNG)
class C435():
    # 'SNG'!C435
    value = "#N/A"
    formula = "=VLOOKUP(B435,$H:$I,2,FALSE)"
    @eval_fn
    def C435():
        b435_1 = SNG.B435()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b435_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A436():
    # 'SNG'!A436
    value = 46858
    isdatetime = True

@register(SNG)
class B436():
    # 'SNG'!B436
    value = 2028
    formula = "=YEAR(A436)"
    @eval_fn
    def B436():
        a436_1 = SNG.A436()
        var_1 = YEAR(a436_1)
        return var_1

@register(SNG)
class C436():
    # 'SNG'!C436
    value = "#N/A"
    formula = "=VLOOKUP(B436,$H:$I,2,FALSE)"
    @eval_fn
    def C436():
        b436_1 = SNG.B436()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b436_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A437():
    # 'SNG'!A437
    value = 46888
    isdatetime = True

@register(SNG)
class B437():
    # 'SNG'!B437
    value = 2028
    formula = "=YEAR(A437)"
    @eval_fn
    def B437():
        a437_1 = SNG.A437()
        var_1 = YEAR(a437_1)
        return var_1

@register(SNG)
class C437():
    # 'SNG'!C437
    value = "#N/A"
    formula = "=VLOOKUP(B437,$H:$I,2,FALSE)"
    @eval_fn
    def C437():
        b437_1 = SNG.B437()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b437_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A438():
    # 'SNG'!A438
    value = 46919
    isdatetime = True

@register(SNG)
class B438():
    # 'SNG'!B438
    value = 2028
    formula = "=YEAR(A438)"
    @eval_fn
    def B438():
        a438_1 = SNG.A438()
        var_1 = YEAR(a438_1)
        return var_1

@register(SNG)
class C438():
    # 'SNG'!C438
    value = "#N/A"
    formula = "=VLOOKUP(B438,$H:$I,2,FALSE)"
    @eval_fn
    def C438():
        b438_1 = SNG.B438()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b438_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A439():
    # 'SNG'!A439
    value = 46949
    isdatetime = True

@register(SNG)
class B439():
    # 'SNG'!B439
    value = 2028
    formula = "=YEAR(A439)"
    @eval_fn
    def B439():
        a439_1 = SNG.A439()
        var_1 = YEAR(a439_1)
        return var_1

@register(SNG)
class C439():
    # 'SNG'!C439
    value = "#N/A"
    formula = "=VLOOKUP(B439,$H:$I,2,FALSE)"
    @eval_fn
    def C439():
        b439_1 = SNG.B439()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b439_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A440():
    # 'SNG'!A440
    value = 46980
    isdatetime = True

@register(SNG)
class B440():
    # 'SNG'!B440
    value = 2028
    formula = "=YEAR(A440)"
    @eval_fn
    def B440():
        a440_1 = SNG.A440()
        var_1 = YEAR(a440_1)
        return var_1

@register(SNG)
class C440():
    # 'SNG'!C440
    value = "#N/A"
    formula = "=VLOOKUP(B440,$H:$I,2,FALSE)"
    @eval_fn
    def C440():
        b440_1 = SNG.B440()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b440_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A441():
    # 'SNG'!A441
    value = 47011
    isdatetime = True

@register(SNG)
class B441():
    # 'SNG'!B441
    value = 2028
    formula = "=YEAR(A441)"
    @eval_fn
    def B441():
        a441_1 = SNG.A441()
        var_1 = YEAR(a441_1)
        return var_1

@register(SNG)
class C441():
    # 'SNG'!C441
    value = "#N/A"
    formula = "=VLOOKUP(B441,$H:$I,2,FALSE)"
    @eval_fn
    def C441():
        b441_1 = SNG.B441()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b441_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A442():
    # 'SNG'!A442
    value = 47041
    isdatetime = True

@register(SNG)
class B442():
    # 'SNG'!B442
    value = 2028
    formula = "=YEAR(A442)"
    @eval_fn
    def B442():
        a442_1 = SNG.A442()
        var_1 = YEAR(a442_1)
        return var_1

@register(SNG)
class C442():
    # 'SNG'!C442
    value = "#N/A"
    formula = "=VLOOKUP(B442,$H:$I,2,FALSE)"
    @eval_fn
    def C442():
        b442_1 = SNG.B442()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b442_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A443():
    # 'SNG'!A443
    value = 47072
    isdatetime = True

@register(SNG)
class B443():
    # 'SNG'!B443
    value = 2028
    formula = "=YEAR(A443)"
    @eval_fn
    def B443():
        a443_1 = SNG.A443()
        var_1 = YEAR(a443_1)
        return var_1

@register(SNG)
class C443():
    # 'SNG'!C443
    value = "#N/A"
    formula = "=VLOOKUP(B443,$H:$I,2,FALSE)"
    @eval_fn
    def C443():
        b443_1 = SNG.B443()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b443_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A444():
    # 'SNG'!A444
    value = 47102
    isdatetime = True

@register(SNG)
class B444():
    # 'SNG'!B444
    value = 2028
    formula = "=YEAR(A444)"
    @eval_fn
    def B444():
        a444_1 = SNG.A444()
        var_1 = YEAR(a444_1)
        return var_1

@register(SNG)
class C444():
    # 'SNG'!C444
    value = "#N/A"
    formula = "=VLOOKUP(B444,$H:$I,2,FALSE)"
    @eval_fn
    def C444():
        b444_1 = SNG.B444()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b444_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A445():
    # 'SNG'!A445
    value = 47133
    isdatetime = True

@register(SNG)
class B445():
    # 'SNG'!B445
    value = 2029
    formula = "=YEAR(A445)"
    @eval_fn
    def B445():
        a445_1 = SNG.A445()
        var_1 = YEAR(a445_1)
        return var_1

@register(SNG)
class C445():
    # 'SNG'!C445
    value = "#N/A"
    formula = "=VLOOKUP(B445,$H:$I,2,FALSE)"
    @eval_fn
    def C445():
        b445_1 = SNG.B445()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b445_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A446():
    # 'SNG'!A446
    value = 47164
    isdatetime = True

@register(SNG)
class B446():
    # 'SNG'!B446
    value = 2029
    formula = "=YEAR(A446)"
    @eval_fn
    def B446():
        a446_1 = SNG.A446()
        var_1 = YEAR(a446_1)
        return var_1

@register(SNG)
class C446():
    # 'SNG'!C446
    value = "#N/A"
    formula = "=VLOOKUP(B446,$H:$I,2,FALSE)"
    @eval_fn
    def C446():
        b446_1 = SNG.B446()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b446_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A447():
    # 'SNG'!A447
    value = 47192
    isdatetime = True

@register(SNG)
class B447():
    # 'SNG'!B447
    value = 2029
    formula = "=YEAR(A447)"
    @eval_fn
    def B447():
        a447_1 = SNG.A447()
        var_1 = YEAR(a447_1)
        return var_1

@register(SNG)
class C447():
    # 'SNG'!C447
    value = "#N/A"
    formula = "=VLOOKUP(B447,$H:$I,2,FALSE)"
    @eval_fn
    def C447():
        b447_1 = SNG.B447()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b447_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A448():
    # 'SNG'!A448
    value = 47223
    isdatetime = True

@register(SNG)
class B448():
    # 'SNG'!B448
    value = 2029
    formula = "=YEAR(A448)"
    @eval_fn
    def B448():
        a448_1 = SNG.A448()
        var_1 = YEAR(a448_1)
        return var_1

@register(SNG)
class C448():
    # 'SNG'!C448
    value = "#N/A"
    formula = "=VLOOKUP(B448,$H:$I,2,FALSE)"
    @eval_fn
    def C448():
        b448_1 = SNG.B448()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b448_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A449():
    # 'SNG'!A449
    value = 47253
    isdatetime = True

@register(SNG)
class B449():
    # 'SNG'!B449
    value = 2029
    formula = "=YEAR(A449)"
    @eval_fn
    def B449():
        a449_1 = SNG.A449()
        var_1 = YEAR(a449_1)
        return var_1

@register(SNG)
class C449():
    # 'SNG'!C449
    value = "#N/A"
    formula = "=VLOOKUP(B449,$H:$I,2,FALSE)"
    @eval_fn
    def C449():
        b449_1 = SNG.B449()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b449_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A450():
    # 'SNG'!A450
    value = 47284
    isdatetime = True

@register(SNG)
class B450():
    # 'SNG'!B450
    value = 2029
    formula = "=YEAR(A450)"
    @eval_fn
    def B450():
        a450_1 = SNG.A450()
        var_1 = YEAR(a450_1)
        return var_1

@register(SNG)
class C450():
    # 'SNG'!C450
    value = "#N/A"
    formula = "=VLOOKUP(B450,$H:$I,2,FALSE)"
    @eval_fn
    def C450():
        b450_1 = SNG.B450()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b450_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A451():
    # 'SNG'!A451
    value = 47314
    isdatetime = True

@register(SNG)
class B451():
    # 'SNG'!B451
    value = 2029
    formula = "=YEAR(A451)"
    @eval_fn
    def B451():
        a451_1 = SNG.A451()
        var_1 = YEAR(a451_1)
        return var_1

@register(SNG)
class C451():
    # 'SNG'!C451
    value = "#N/A"
    formula = "=VLOOKUP(B451,$H:$I,2,FALSE)"
    @eval_fn
    def C451():
        b451_1 = SNG.B451()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b451_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A452():
    # 'SNG'!A452
    value = 47345
    isdatetime = True

@register(SNG)
class B452():
    # 'SNG'!B452
    value = 2029
    formula = "=YEAR(A452)"
    @eval_fn
    def B452():
        a452_1 = SNG.A452()
        var_1 = YEAR(a452_1)
        return var_1

@register(SNG)
class C452():
    # 'SNG'!C452
    value = "#N/A"
    formula = "=VLOOKUP(B452,$H:$I,2,FALSE)"
    @eval_fn
    def C452():
        b452_1 = SNG.B452()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b452_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A453():
    # 'SNG'!A453
    value = 47376
    isdatetime = True

@register(SNG)
class B453():
    # 'SNG'!B453
    value = 2029
    formula = "=YEAR(A453)"
    @eval_fn
    def B453():
        a453_1 = SNG.A453()
        var_1 = YEAR(a453_1)
        return var_1

@register(SNG)
class C453():
    # 'SNG'!C453
    value = "#N/A"
    formula = "=VLOOKUP(B453,$H:$I,2,FALSE)"
    @eval_fn
    def C453():
        b453_1 = SNG.B453()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b453_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A454():
    # 'SNG'!A454
    value = 47406
    isdatetime = True

@register(SNG)
class B454():
    # 'SNG'!B454
    value = 2029
    formula = "=YEAR(A454)"
    @eval_fn
    def B454():
        a454_1 = SNG.A454()
        var_1 = YEAR(a454_1)
        return var_1

@register(SNG)
class C454():
    # 'SNG'!C454
    value = "#N/A"
    formula = "=VLOOKUP(B454,$H:$I,2,FALSE)"
    @eval_fn
    def C454():
        b454_1 = SNG.B454()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b454_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A455():
    # 'SNG'!A455
    value = 47437
    isdatetime = True

@register(SNG)
class B455():
    # 'SNG'!B455
    value = 2029
    formula = "=YEAR(A455)"
    @eval_fn
    def B455():
        a455_1 = SNG.A455()
        var_1 = YEAR(a455_1)
        return var_1

@register(SNG)
class C455():
    # 'SNG'!C455
    value = "#N/A"
    formula = "=VLOOKUP(B455,$H:$I,2,FALSE)"
    @eval_fn
    def C455():
        b455_1 = SNG.B455()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b455_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A456():
    # 'SNG'!A456
    value = 47467
    isdatetime = True

@register(SNG)
class B456():
    # 'SNG'!B456
    value = 2029
    formula = "=YEAR(A456)"
    @eval_fn
    def B456():
        a456_1 = SNG.A456()
        var_1 = YEAR(a456_1)
        return var_1

@register(SNG)
class C456():
    # 'SNG'!C456
    value = "#N/A"
    formula = "=VLOOKUP(B456,$H:$I,2,FALSE)"
    @eval_fn
    def C456():
        b456_1 = SNG.B456()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b456_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A457():
    # 'SNG'!A457
    value = 47498
    isdatetime = True

@register(SNG)
class B457():
    # 'SNG'!B457
    value = 2030
    formula = "=YEAR(A457)"
    @eval_fn
    def B457():
        a457_1 = SNG.A457()
        var_1 = YEAR(a457_1)
        return var_1

@register(SNG)
class C457():
    # 'SNG'!C457
    value = "#N/A"
    formula = "=VLOOKUP(B457,$H:$I,2,FALSE)"
    @eval_fn
    def C457():
        b457_1 = SNG.B457()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b457_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A458():
    # 'SNG'!A458
    value = 47529
    isdatetime = True

@register(SNG)
class B458():
    # 'SNG'!B458
    value = 2030
    formula = "=YEAR(A458)"
    @eval_fn
    def B458():
        a458_1 = SNG.A458()
        var_1 = YEAR(a458_1)
        return var_1

@register(SNG)
class C458():
    # 'SNG'!C458
    value = "#N/A"
    formula = "=VLOOKUP(B458,$H:$I,2,FALSE)"
    @eval_fn
    def C458():
        b458_1 = SNG.B458()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b458_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A459():
    # 'SNG'!A459
    value = 47557
    isdatetime = True

@register(SNG)
class B459():
    # 'SNG'!B459
    value = 2030
    formula = "=YEAR(A459)"
    @eval_fn
    def B459():
        a459_1 = SNG.A459()
        var_1 = YEAR(a459_1)
        return var_1

@register(SNG)
class C459():
    # 'SNG'!C459
    value = "#N/A"
    formula = "=VLOOKUP(B459,$H:$I,2,FALSE)"
    @eval_fn
    def C459():
        b459_1 = SNG.B459()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b459_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A460():
    # 'SNG'!A460
    value = 47588
    isdatetime = True

@register(SNG)
class B460():
    # 'SNG'!B460
    value = 2030
    formula = "=YEAR(A460)"
    @eval_fn
    def B460():
        a460_1 = SNG.A460()
        var_1 = YEAR(a460_1)
        return var_1

@register(SNG)
class C460():
    # 'SNG'!C460
    value = "#N/A"
    formula = "=VLOOKUP(B460,$H:$I,2,FALSE)"
    @eval_fn
    def C460():
        b460_1 = SNG.B460()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b460_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A461():
    # 'SNG'!A461
    value = 47618
    isdatetime = True

@register(SNG)
class B461():
    # 'SNG'!B461
    value = 2030
    formula = "=YEAR(A461)"
    @eval_fn
    def B461():
        a461_1 = SNG.A461()
        var_1 = YEAR(a461_1)
        return var_1

@register(SNG)
class C461():
    # 'SNG'!C461
    value = "#N/A"
    formula = "=VLOOKUP(B461,$H:$I,2,FALSE)"
    @eval_fn
    def C461():
        b461_1 = SNG.B461()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b461_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A462():
    # 'SNG'!A462
    value = 47649
    isdatetime = True

@register(SNG)
class B462():
    # 'SNG'!B462
    value = 2030
    formula = "=YEAR(A462)"
    @eval_fn
    def B462():
        a462_1 = SNG.A462()
        var_1 = YEAR(a462_1)
        return var_1

@register(SNG)
class C462():
    # 'SNG'!C462
    value = "#N/A"
    formula = "=VLOOKUP(B462,$H:$I,2,FALSE)"
    @eval_fn
    def C462():
        b462_1 = SNG.B462()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b462_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A463():
    # 'SNG'!A463
    value = 47679
    isdatetime = True

@register(SNG)
class B463():
    # 'SNG'!B463
    value = 2030
    formula = "=YEAR(A463)"
    @eval_fn
    def B463():
        a463_1 = SNG.A463()
        var_1 = YEAR(a463_1)
        return var_1

@register(SNG)
class C463():
    # 'SNG'!C463
    value = "#N/A"
    formula = "=VLOOKUP(B463,$H:$I,2,FALSE)"
    @eval_fn
    def C463():
        b463_1 = SNG.B463()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b463_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A464():
    # 'SNG'!A464
    value = 47710
    isdatetime = True

@register(SNG)
class B464():
    # 'SNG'!B464
    value = 2030
    formula = "=YEAR(A464)"
    @eval_fn
    def B464():
        a464_1 = SNG.A464()
        var_1 = YEAR(a464_1)
        return var_1

@register(SNG)
class C464():
    # 'SNG'!C464
    value = "#N/A"
    formula = "=VLOOKUP(B464,$H:$I,2,FALSE)"
    @eval_fn
    def C464():
        b464_1 = SNG.B464()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b464_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A465():
    # 'SNG'!A465
    value = 47741
    isdatetime = True

@register(SNG)
class B465():
    # 'SNG'!B465
    value = 2030
    formula = "=YEAR(A465)"
    @eval_fn
    def B465():
        a465_1 = SNG.A465()
        var_1 = YEAR(a465_1)
        return var_1

@register(SNG)
class C465():
    # 'SNG'!C465
    value = "#N/A"
    formula = "=VLOOKUP(B465,$H:$I,2,FALSE)"
    @eval_fn
    def C465():
        b465_1 = SNG.B465()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b465_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A466():
    # 'SNG'!A466
    value = 47771
    isdatetime = True

@register(SNG)
class B466():
    # 'SNG'!B466
    value = 2030
    formula = "=YEAR(A466)"
    @eval_fn
    def B466():
        a466_1 = SNG.A466()
        var_1 = YEAR(a466_1)
        return var_1

@register(SNG)
class C466():
    # 'SNG'!C466
    value = "#N/A"
    formula = "=VLOOKUP(B466,$H:$I,2,FALSE)"
    @eval_fn
    def C466():
        b466_1 = SNG.B466()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b466_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A467():
    # 'SNG'!A467
    value = 47802
    isdatetime = True

@register(SNG)
class B467():
    # 'SNG'!B467
    value = 2030
    formula = "=YEAR(A467)"
    @eval_fn
    def B467():
        a467_1 = SNG.A467()
        var_1 = YEAR(a467_1)
        return var_1

@register(SNG)
class C467():
    # 'SNG'!C467
    value = "#N/A"
    formula = "=VLOOKUP(B467,$H:$I,2,FALSE)"
    @eval_fn
    def C467():
        b467_1 = SNG.B467()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b467_1, range_1, 2, "FALSE")
        return var_1

@register(SNG)
class A468():
    # 'SNG'!A468
    value = 47832
    isdatetime = True

@register(SNG)
class B468():
    # 'SNG'!B468
    value = 2030
    formula = "=YEAR(A468)"
    @eval_fn
    def B468():
        a468_1 = SNG.A468()
        var_1 = YEAR(a468_1)
        return var_1

@register(SNG)
class C468():
    # 'SNG'!C468
    value = "#N/A"
    formula = "=VLOOKUP(B468,$H:$I,2,FALSE)"
    @eval_fn
    def C468():
        b468_1 = SNG.B468()
        range_1 = SNG(8, 0, 9, 0)
        var_1 = VLOOKUP(b468_1, range_1, 2, "FALSE")
        return var_1