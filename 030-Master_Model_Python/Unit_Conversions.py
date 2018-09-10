# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Unit_Conversions = Worksheet('Unit_Conversions', 10, 10)



@register(Unit_Conversions)
class A1():
    # 'Unit_Conversions'!A1
    value = " http://www.eia.gov/forecasts/aeo/pdf/appg.pdf "

@register(Unit_Conversions)
class A2():
    # 'Unit_Conversions'!A2
    value = "Petroleum products and other liquids"

@register(Unit_Conversions)
class C3():
    # 'Unit_Conversions'!C3
    value = "US gallons per bbl"

@register(Unit_Conversions)
class D3():
    # 'Unit_Conversions'!D3
    value = 42

@register(Unit_Conversions)
class C4():
    # 'Unit_Conversions'!C4
    value = "bbl per US gallon"

@register(Unit_Conversions)
class D4():
    # 'Unit_Conversions'!D4
    value = 0.0238095238095
    formula = "=1/D3"
    @eval_fn
    def D4():
        d3_1 = Unit_Conversions.D3()
        var_1 = divide(1, d3_1)
        return var_1

@register(Unit_Conversions)
class B5():
    # 'Unit_Conversions'!B5
    value = "Fuel"

@register(Unit_Conversions)
class C5():
    # 'Unit_Conversions'!C5
    value = "Units"

@register(Unit_Conversions)
class D5():
    # 'Unit_Conversions'!D5
    value = "Approximate heat Content"

@register(Unit_Conversions)
class E5():
    # 'Unit_Conversions'!E5
    value = "Units"

@register(Unit_Conversions)
class F5():
    # 'Unit_Conversions'!F5
    value = "Approximate heat Content"

@register(Unit_Conversions)
class B6():
    # 'Unit_Conversions'!B6
    value = " Consumption"

@register(Unit_Conversions)
class C6():
    # 'Unit_Conversions'!C6
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D6():
    # 'Unit_Conversions'!D6
    value = 0.125095238095
    formula = "=F6*$D$4"
    @eval_fn
    def D6():
        f6_1 = Unit_Conversions.F6()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f6_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E6():
    # 'Unit_Conversions'!E6
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F6():
    # 'Unit_Conversions'!F6
    value = 5.254

@register(Unit_Conversions)
class B7():
    # 'Unit_Conversions'!B7
    value = "    Motor gasoline"

@register(Unit_Conversions)
class C7():
    # 'Unit_Conversions'!C7
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D7():
    # 'Unit_Conversions'!D7
    value = 0.121428571429
    formula = "=F7*$D$4"
    @eval_fn
    def D7():
        f7_1 = Unit_Conversions.F7()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f7_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E7():
    # 'Unit_Conversions'!E7
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F7():
    # 'Unit_Conversions'!F7
    value = 5.1

@register(Unit_Conversions)
class B8():
    # 'Unit_Conversions'!B8
    value = "     Jet  fuel   "

@register(Unit_Conversions)
class C8():
    # 'Unit_Conversions'!C8
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D8():
    # 'Unit_Conversions'!D8
    value = 0.135
    formula = "=F8*$D$4"
    @eval_fn
    def D8():
        f8_1 = Unit_Conversions.F8()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f8_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E8():
    # 'Unit_Conversions'!E8
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F8():
    # 'Unit_Conversions'!F8
    value = 5.67

@register(Unit_Conversions)
class B9():
    # 'Unit_Conversions'!B9
    value = "    Distillate fuel oil"

@register(Unit_Conversions)
class C9():
    # 'Unit_Conversions'!C9
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D9():
    # 'Unit_Conversions'!D9
    value = 0.137404761905
    formula = "=F9*$D$4"
    @eval_fn
    def D9():
        f9_1 = Unit_Conversions.F9()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f9_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E9():
    # 'Unit_Conversions'!E9
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F9():
    # 'Unit_Conversions'!F9
    value = 5.771

@register(Unit_Conversions)
class B10():
    # 'Unit_Conversions'!B10
    value = "    Diesel fuel"

@register(Unit_Conversions)
class C10():
    # 'Unit_Conversions'!C10
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D10():
    # 'Unit_Conversions'!D10
    value = 0.13719047619
    formula = "=F10*$D$4"
    @eval_fn
    def D10():
        f10_1 = Unit_Conversions.F10()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f10_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E10():
    # 'Unit_Conversions'!E10
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F10():
    # 'Unit_Conversions'!F10
    value = 5.762

@register(Unit_Conversions)
class B11():
    # 'Unit_Conversions'!B11
    value = "    Residual fuel oil              "

@register(Unit_Conversions)
class C11():
    # 'Unit_Conversions'!C11
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D11():
    # 'Unit_Conversions'!D11
    value = 0.14969047619
    formula = "=F11*$D$4"
    @eval_fn
    def D11():
        f11_1 = Unit_Conversions.F11()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f11_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E11():
    # 'Unit_Conversions'!E11
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F11():
    # 'Unit_Conversions'!F11
    value = 6.287

@register(Unit_Conversions)
class B12():
    # 'Unit_Conversions'!B12
    value = "    Liquefied petroleum gases"

@register(Unit_Conversions)
class C12():
    # 'Unit_Conversions'!C12
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D12():
    # 'Unit_Conversions'!D12
    value = 0.0846904761905
    formula = "=F12*$D$4"
    @eval_fn
    def D12():
        f12_1 = Unit_Conversions.F12()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f12_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E12():
    # 'Unit_Conversions'!E12
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F12():
    # 'Unit_Conversions'!F12
    value = 3.557

@register(Unit_Conversions)
class B13():
    # 'Unit_Conversions'!B13
    value = "    Kerosene              "

@register(Unit_Conversions)
class C13():
    # 'Unit_Conversions'!C13
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D13():
    # 'Unit_Conversions'!D13
    value = 0.135
    formula = "=F13*$D$4"
    @eval_fn
    def D13():
        f13_1 = Unit_Conversions.F13()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f13_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E13():
    # 'Unit_Conversions'!E13
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F13():
    # 'Unit_Conversions'!F13
    value = 5.67

@register(Unit_Conversions)
class B14():
    # 'Unit_Conversions'!B14
    value = "    Petrochemical feedstocks"

@register(Unit_Conversions)
class C14():
    # 'Unit_Conversions'!C14
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D14():
    # 'Unit_Conversions'!D14
    value = 0.13119047619
    formula = "=F14*$D$4"
    @eval_fn
    def D14():
        f14_1 = Unit_Conversions.F14()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f14_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E14():
    # 'Unit_Conversions'!E14
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F14():
    # 'Unit_Conversions'!F14
    value = 5.51

@register(Unit_Conversions)
class B15():
    # 'Unit_Conversions'!B15
    value = "    Unfinished oils"

@register(Unit_Conversions)
class C15():
    # 'Unit_Conversions'!C15
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D15():
    # 'Unit_Conversions'!D15
    value = 0.145666666667
    formula = "=F15*$D$4"
    @eval_fn
    def D15():
        f15_1 = Unit_Conversions.F15()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f15_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E15():
    # 'Unit_Conversions'!E15
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F15():
    # 'Unit_Conversions'!F15
    value = 6.118

@register(Unit_Conversions)
class B16():
    # 'Unit_Conversions'!B16
    value = "  Ethanol                 "

@register(Unit_Conversions)
class C16():
    # 'Unit_Conversions'!C16
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D16():
    # 'Unit_Conversions'!D16
    value = 0.0847857142857
    formula = "=F16*$D$4"
    @eval_fn
    def D16():
        f16_1 = Unit_Conversions.F16()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f16_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E16():
    # 'Unit_Conversions'!E16
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F16():
    # 'Unit_Conversions'!F16
    value = 3.561

@register(Unit_Conversions)
class B17():
    # 'Unit_Conversions'!B17
    value = "  Biodiesel  "

@register(Unit_Conversions)
class C17():
    # 'Unit_Conversions'!C17
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D17():
    # 'Unit_Conversions'!D17
    value = 0.127595238095
    formula = "=F17*$D$4"
    @eval_fn
    def D17():
        f17_1 = Unit_Conversions.F17()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f17_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E17():
    # 'Unit_Conversions'!E17
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F17():
    # 'Unit_Conversions'!F17
    value = 5.359

@register(Unit_Conversions)
class B19():
    # 'Unit_Conversions'!B19
    value = "Electricity"

@register(Unit_Conversions)
class C19():
    # 'Unit_Conversions'!C19
    value = "Btu per KWh"

@register(Unit_Conversions)
class D19():
    # 'Unit_Conversions'!D19
    value = 3412

@register(Unit_Conversions)
class E19():
    # 'Unit_Conversions'!E19
    value = "Btu per KWh"

@register(Unit_Conversions)
class F19():
    # 'Unit_Conversions'!F19
    value = 3412

@register(Unit_Conversions)
class A21():
    # 'Unit_Conversions'!A21
    value = "Crude Oil"

@register(Unit_Conversions)
class B22():
    # 'Unit_Conversions'!B22
    value = "Production"

@register(Unit_Conversions)
class C22():
    # 'Unit_Conversions'!C22
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D22():
    # 'Unit_Conversions'!D22
    value = 0.138095238095
    formula = "=F22*$D$4"
    @eval_fn
    def D22():
        f22_1 = Unit_Conversions.F22()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f22_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E22():
    # 'Unit_Conversions'!E22
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F22():
    # 'Unit_Conversions'!F22
    value = 5.8

@register(Unit_Conversions)
class B23():
    # 'Unit_Conversions'!B23
    value = "Imports"

@register(Unit_Conversions)
class C23():
    # 'Unit_Conversions'!C23
    value = "million Btu per Gallon"

@register(Unit_Conversions)
class D23():
    # 'Unit_Conversions'!D23
    value = 0.142595238095
    formula = "=F23*$D$4"
    @eval_fn
    def D23():
        f23_1 = Unit_Conversions.F23()
        d4_1 = Unit_Conversions.D4()
        var_1 = mult(f23_1, d4_1)
        return var_1

@register(Unit_Conversions)
class E23():
    # 'Unit_Conversions'!E23
    value = "million Btu per barrel"

@register(Unit_Conversions)
class F23():
    # 'Unit_Conversions'!F23
    value = 5.989

@register(Unit_Conversions)
class A25():
    # 'Unit_Conversions'!A25
    value = "Natural Gas"

@register(Unit_Conversions)
class B25():
    # 'Unit_Conversions'!B25
    value = "Year"

@register(Unit_Conversions)
class B26():
    # 'Unit_Conversions'!B26
    value = 1984

@register(Unit_Conversions)
class C26():
    # 'Unit_Conversions'!C26
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D26():
    # 'Unit_Conversions'!D26
    value = 0.974569319114

@register(Unit_Conversions)
class B27():
    # 'Unit_Conversions'!B27
    value = 1985

@register(Unit_Conversions)
class C27():
    # 'Unit_Conversions'!C27
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D27():
    # 'Unit_Conversions'!D27
    value = 0.9240788984

@register(Unit_Conversions)
class B28():
    # 'Unit_Conversions'!B28
    value = 1986

@register(Unit_Conversions)
class C28():
    # 'Unit_Conversions'!C28
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D28():
    # 'Unit_Conversions'!D28
    value = 0.92071802543

@register(Unit_Conversions)
class B29():
    # 'Unit_Conversions'!B29
    value = 1987

@register(Unit_Conversions)
class C29():
    # 'Unit_Conversions'!C29
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D29():
    # 'Unit_Conversions'!D29
    value = 0.936490850377

@register(Unit_Conversions)
class B30():
    # 'Unit_Conversions'!B30
    value = 1988

@register(Unit_Conversions)
class C30():
    # 'Unit_Conversions'!C30
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D30():
    # 'Unit_Conversions'!D30
    value = 0.927556818182

@register(Unit_Conversions)
class B31():
    # 'Unit_Conversions'!B31
    value = 1989

@register(Unit_Conversions)
class C31():
    # 'Unit_Conversions'!C31
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D31():
    # 'Unit_Conversions'!D31
    value = 0.926091440358

@register(Unit_Conversions)
class B32():
    # 'Unit_Conversions'!B32
    value = 1990

@register(Unit_Conversions)
class C32():
    # 'Unit_Conversions'!C32
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D32():
    # 'Unit_Conversions'!D32
    value = 0.934629567549

@register(Unit_Conversions)
class B33():
    # 'Unit_Conversions'!B33
    value = 1991

@register(Unit_Conversions)
class C33():
    # 'Unit_Conversions'!C33
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D33():
    # 'Unit_Conversions'!D33
    value = 0.926091440358

@register(Unit_Conversions)
class B34():
    # 'Unit_Conversions'!B34
    value = 1992

@register(Unit_Conversions)
class C34():
    # 'Unit_Conversions'!C34
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D34():
    # 'Unit_Conversions'!D34
    value = 0.931881051176

@register(Unit_Conversions)
class B35():
    # 'Unit_Conversions'!B35
    value = 1993

@register(Unit_Conversions)
class C35():
    # 'Unit_Conversions'!C35
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D35():
    # 'Unit_Conversions'!D35
    value = 0.941693010186

@register(Unit_Conversions)
class B36():
    # 'Unit_Conversions'!B36
    value = 1994

@register(Unit_Conversions)
class C36():
    # 'Unit_Conversions'!C36
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D36():
    # 'Unit_Conversions'!D36
    value = 0.951369863014

@register(Unit_Conversions)
class B37():
    # 'Unit_Conversions'!B37
    value = 1995

@register(Unit_Conversions)
class C37():
    # 'Unit_Conversions'!C37
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D37():
    # 'Unit_Conversions'!D37
    value = 0.954232622161

@register(Unit_Conversions)
class B38():
    # 'Unit_Conversions'!B38
    value = 1996

@register(Unit_Conversions)
class C38():
    # 'Unit_Conversions'!C38
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D38():
    # 'Unit_Conversions'!D38
    value = 0.945840707965

@register(Unit_Conversions)
class B39():
    # 'Unit_Conversions'!B39
    value = 1997

@register(Unit_Conversions)
class C39():
    # 'Unit_Conversions'!C39
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D39():
    # 'Unit_Conversions'!D39
    value = 0.970992934176

@register(Unit_Conversions)
class B40():
    # 'Unit_Conversions'!B40
    value = 1998

@register(Unit_Conversions)
class C40():
    # 'Unit_Conversions'!C40
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D40():
    # 'Unit_Conversions'!D40
    value = 0.946842668569

@register(Unit_Conversions)
class B41():
    # 'Unit_Conversions'!B41
    value = 1999

@register(Unit_Conversions)
class C41():
    # 'Unit_Conversions'!C41
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D41():
    # 'Unit_Conversions'!D41
    value = 0.947678447678

@register(Unit_Conversions)
class B42():
    # 'Unit_Conversions'!B42
    value = 2000

@register(Unit_Conversions)
class C42():
    # 'Unit_Conversions'!C42
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D42():
    # 'Unit_Conversions'!D42
    value = 0.954957983193

@register(Unit_Conversions)
class B43():
    # 'Unit_Conversions'!B43
    value = 2001

@register(Unit_Conversions)
class C43():
    # 'Unit_Conversions'!C43
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D43():
    # 'Unit_Conversions'!D43
    value = 0.965068493151

@register(Unit_Conversions)
class B44():
    # 'Unit_Conversions'!B44
    value = 2002

@register(Unit_Conversions)
class C44():
    # 'Unit_Conversions'!C44
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D44():
    # 'Unit_Conversions'!D44
    value = 0.943409247757

@register(Unit_Conversions)
class B45():
    # 'Unit_Conversions'!B45
    value = 2003

@register(Unit_Conversions)
class C45():
    # 'Unit_Conversions'!C45
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D45():
    # 'Unit_Conversions'!D45
    value = 0.954910870325

@register(Unit_Conversions)
class B46():
    # 'Unit_Conversions'!B46
    value = 2004

@register(Unit_Conversions)
class C46():
    # 'Unit_Conversions'!C46
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D46():
    # 'Unit_Conversions'!D46
    value = 0.954248366013

@register(Unit_Conversions)
class B47():
    # 'Unit_Conversions'!B47
    value = 2005

@register(Unit_Conversions)
class C47():
    # 'Unit_Conversions'!C47
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D47():
    # 'Unit_Conversions'!D47
    value = 0.964458247067

@register(Unit_Conversions)
class B48():
    # 'Unit_Conversions'!B48
    value = 2006

@register(Unit_Conversions)
class C48():
    # 'Unit_Conversions'!C48
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D48():
    # 'Unit_Conversions'!D48
    value = 0.955044612217

@register(Unit_Conversions)
class B49():
    # 'Unit_Conversions'!B49
    value = 2007

@register(Unit_Conversions)
class C49():
    # 'Unit_Conversions'!C49
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D49():
    # 'Unit_Conversions'!D49
    value = 0.964140730717

@register(Unit_Conversions)
class B50():
    # 'Unit_Conversions'!B50
    value = 2008

@register(Unit_Conversions)
class C50():
    # 'Unit_Conversions'!C50
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D50():
    # 'Unit_Conversions'!D50
    value = 0.95882144125

@register(Unit_Conversions)
class B51():
    # 'Unit_Conversions'!B51
    value = 2009

@register(Unit_Conversions)
class C51():
    # 'Unit_Conversions'!C51
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D51():
    # 'Unit_Conversions'!D51
    value = 0.961651917404

@register(Unit_Conversions)
class B52():
    # 'Unit_Conversions'!B52
    value = 2010

@register(Unit_Conversions)
class C52():
    # 'Unit_Conversions'!C52
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D52():
    # 'Unit_Conversions'!D52
    value = 0.961566617862

@register(Unit_Conversions)
class B53():
    # 'Unit_Conversions'!B53
    value = 2011

@register(Unit_Conversions)
class C53():
    # 'Unit_Conversions'!C53
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D53():
    # 'Unit_Conversions'!D53
    value = 0.961566617862
    formula = "=D52"
    @eval_fn
    def D53():
        d52_1 = Unit_Conversions.D52()
        return d52_1

@register(Unit_Conversions)
class E53():
    # 'Unit_Conversions'!E53
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B54():
    # 'Unit_Conversions'!B54
    value = 2012

@register(Unit_Conversions)
class C54():
    # 'Unit_Conversions'!C54
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D54():
    # 'Unit_Conversions'!D54
    value = 0.961566617862
    formula = "=D53"
    @eval_fn
    def D54():
        d53_1 = Unit_Conversions.D53()
        return d53_1

@register(Unit_Conversions)
class E54():
    # 'Unit_Conversions'!E54
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B55():
    # 'Unit_Conversions'!B55
    value = 2013

@register(Unit_Conversions)
class C55():
    # 'Unit_Conversions'!C55
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D55():
    # 'Unit_Conversions'!D55
    value = 0.961566617862
    formula = "=D54"
    @eval_fn
    def D55():
        d54_1 = Unit_Conversions.D54()
        return d54_1

@register(Unit_Conversions)
class E55():
    # 'Unit_Conversions'!E55
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B56():
    # 'Unit_Conversions'!B56
    value = 2014

@register(Unit_Conversions)
class C56():
    # 'Unit_Conversions'!C56
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D56():
    # 'Unit_Conversions'!D56
    value = 0.961566617862
    formula = "=D55"
    @eval_fn
    def D56():
        d55_1 = Unit_Conversions.D55()
        return d55_1

@register(Unit_Conversions)
class E56():
    # 'Unit_Conversions'!E56
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B57():
    # 'Unit_Conversions'!B57
    value = 2015

@register(Unit_Conversions)
class C57():
    # 'Unit_Conversions'!C57
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D57():
    # 'Unit_Conversions'!D57
    value = 0.961566617862
    formula = "=D56"
    @eval_fn
    def D57():
        d56_1 = Unit_Conversions.D56()
        return d56_1

@register(Unit_Conversions)
class E57():
    # 'Unit_Conversions'!E57
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B58():
    # 'Unit_Conversions'!B58
    value = 2016

@register(Unit_Conversions)
class C58():
    # 'Unit_Conversions'!C58
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D58():
    # 'Unit_Conversions'!D58
    value = 0.961566617862
    formula = "=D57"
    @eval_fn
    def D58():
        d57_1 = Unit_Conversions.D57()
        return d57_1

@register(Unit_Conversions)
class E58():
    # 'Unit_Conversions'!E58
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B59():
    # 'Unit_Conversions'!B59
    value = 2017

@register(Unit_Conversions)
class C59():
    # 'Unit_Conversions'!C59
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D59():
    # 'Unit_Conversions'!D59
    value = 0.961566617862
    formula = "=D58"
    @eval_fn
    def D59():
        d58_1 = Unit_Conversions.D58()
        return d58_1

@register(Unit_Conversions)
class E59():
    # 'Unit_Conversions'!E59
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B60():
    # 'Unit_Conversions'!B60
    value = 2018

@register(Unit_Conversions)
class C60():
    # 'Unit_Conversions'!C60
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D60():
    # 'Unit_Conversions'!D60
    value = 0.961566617862
    formula = "=D59"
    @eval_fn
    def D60():
        d59_1 = Unit_Conversions.D59()
        return d59_1

@register(Unit_Conversions)
class E60():
    # 'Unit_Conversions'!E60
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B61():
    # 'Unit_Conversions'!B61
    value = 2019

@register(Unit_Conversions)
class C61():
    # 'Unit_Conversions'!C61
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D61():
    # 'Unit_Conversions'!D61
    value = 0.961566617862
    formula = "=D60"
    @eval_fn
    def D61():
        d60_1 = Unit_Conversions.D60()
        return d60_1

@register(Unit_Conversions)
class E61():
    # 'Unit_Conversions'!E61
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B62():
    # 'Unit_Conversions'!B62
    value = 2020

@register(Unit_Conversions)
class C62():
    # 'Unit_Conversions'!C62
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D62():
    # 'Unit_Conversions'!D62
    value = 0.961566617862
    formula = "=D61"
    @eval_fn
    def D62():
        d61_1 = Unit_Conversions.D61()
        return d61_1

@register(Unit_Conversions)
class E62():
    # 'Unit_Conversions'!E62
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B63():
    # 'Unit_Conversions'!B63
    value = 2021

@register(Unit_Conversions)
class C63():
    # 'Unit_Conversions'!C63
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D63():
    # 'Unit_Conversions'!D63
    value = 0.961566617862
    formula = "=D62"
    @eval_fn
    def D63():
        d62_1 = Unit_Conversions.D62()
        return d62_1

@register(Unit_Conversions)
class E63():
    # 'Unit_Conversions'!E63
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B64():
    # 'Unit_Conversions'!B64
    value = 2022

@register(Unit_Conversions)
class C64():
    # 'Unit_Conversions'!C64
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D64():
    # 'Unit_Conversions'!D64
    value = 0.961566617862
    formula = "=D63"
    @eval_fn
    def D64():
        d63_1 = Unit_Conversions.D63()
        return d63_1

@register(Unit_Conversions)
class E64():
    # 'Unit_Conversions'!E64
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B65():
    # 'Unit_Conversions'!B65
    value = 2023

@register(Unit_Conversions)
class C65():
    # 'Unit_Conversions'!C65
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D65():
    # 'Unit_Conversions'!D65
    value = 0.961566617862
    formula = "=D64"
    @eval_fn
    def D65():
        d64_1 = Unit_Conversions.D64()
        return d64_1

@register(Unit_Conversions)
class E65():
    # 'Unit_Conversions'!E65
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B66():
    # 'Unit_Conversions'!B66
    value = 2024

@register(Unit_Conversions)
class C66():
    # 'Unit_Conversions'!C66
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D66():
    # 'Unit_Conversions'!D66
    value = 0.961566617862
    formula = "=D65"
    @eval_fn
    def D66():
        d65_1 = Unit_Conversions.D65()
        return d65_1

@register(Unit_Conversions)
class E66():
    # 'Unit_Conversions'!E66
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B67():
    # 'Unit_Conversions'!B67
    value = 2025

@register(Unit_Conversions)
class C67():
    # 'Unit_Conversions'!C67
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D67():
    # 'Unit_Conversions'!D67
    value = 0.961566617862
    formula = "=D66"
    @eval_fn
    def D67():
        d66_1 = Unit_Conversions.D66()
        return d66_1

@register(Unit_Conversions)
class E67():
    # 'Unit_Conversions'!E67
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B68():
    # 'Unit_Conversions'!B68
    value = 2026

@register(Unit_Conversions)
class C68():
    # 'Unit_Conversions'!C68
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D68():
    # 'Unit_Conversions'!D68
    value = 0.961566617862
    formula = "=D67"
    @eval_fn
    def D68():
        d67_1 = Unit_Conversions.D67()
        return d67_1

@register(Unit_Conversions)
class E68():
    # 'Unit_Conversions'!E68
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B69():
    # 'Unit_Conversions'!B69
    value = 2027

@register(Unit_Conversions)
class C69():
    # 'Unit_Conversions'!C69
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D69():
    # 'Unit_Conversions'!D69
    value = 0.961566617862
    formula = "=D68"
    @eval_fn
    def D69():
        d68_1 = Unit_Conversions.D68()
        return d68_1

@register(Unit_Conversions)
class E69():
    # 'Unit_Conversions'!E69
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B70():
    # 'Unit_Conversions'!B70
    value = 2028

@register(Unit_Conversions)
class C70():
    # 'Unit_Conversions'!C70
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D70():
    # 'Unit_Conversions'!D70
    value = 0.961566617862
    formula = "=D69"
    @eval_fn
    def D70():
        d69_1 = Unit_Conversions.D69()
        return d69_1

@register(Unit_Conversions)
class E70():
    # 'Unit_Conversions'!E70
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B71():
    # 'Unit_Conversions'!B71
    value = 2029

@register(Unit_Conversions)
class C71():
    # 'Unit_Conversions'!C71
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D71():
    # 'Unit_Conversions'!D71
    value = 0.961566617862
    formula = "=D70"
    @eval_fn
    def D71():
        d70_1 = Unit_Conversions.D70()
        return d70_1

@register(Unit_Conversions)
class E71():
    # 'Unit_Conversions'!E71
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class B72():
    # 'Unit_Conversions'!B72
    value = 2030

@register(Unit_Conversions)
class C72():
    # 'Unit_Conversions'!C72
    value = "Thousand Cubic Ft per Million btu"

@register(Unit_Conversions)
class D72():
    # 'Unit_Conversions'!D72
    value = 0.961566617862
    formula = "=D71"
    @eval_fn
    def D72():
        d71_1 = Unit_Conversions.D71()
        return d71_1

@register(Unit_Conversions)
class E72():
    # 'Unit_Conversions'!E72
    value = "Used as proxy until new data become available"

@register(Unit_Conversions)
class A73():
    # 'Unit_Conversions'!A73
    value = "Baseline Hyopthetical Power Sector Cost $"