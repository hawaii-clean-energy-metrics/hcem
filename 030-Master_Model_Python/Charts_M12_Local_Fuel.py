# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M12_Local_Fuel = Worksheet('Charts_M12_Local_Fuel', 10, 10)



@register(Charts_M12_Local_Fuel)
class B2():
    # 'Charts_M12_Local_Fuel'!B2
    value = "       Metric 12: Locally Produced Renewable Fuel"

@register(Charts_M12_Local_Fuel)
class D6():
    # 'Charts_M12_Local_Fuel'!D6
    value = 1999
    formula = "='Dashboard M10 RPS'!G5"
    @eval_fn
    def D6():
        g5_1 = Dashboard_M10_RPS.G5()
        return g5_1

@register(Charts_M12_Local_Fuel)
class E6():
    # 'Charts_M12_Local_Fuel'!E6
    value = 2000
    formula = "='Dashboard M10 RPS'!H5"
    @eval_fn
    def E6():
        h5_1 = Dashboard_M10_RPS.H5()
        return h5_1

@register(Charts_M12_Local_Fuel)
class F6():
    # 'Charts_M12_Local_Fuel'!F6
    value = 2001
    formula = "='Dashboard M10 RPS'!I5"
    @eval_fn
    def F6():
        i5_1 = Dashboard_M10_RPS.I5()
        return i5_1

@register(Charts_M12_Local_Fuel)
class G6():
    # 'Charts_M12_Local_Fuel'!G6
    value = 2002
    formula = "='Dashboard M10 RPS'!J5"
    @eval_fn
    def G6():
        j5_1 = Dashboard_M10_RPS.J5()
        return j5_1

@register(Charts_M12_Local_Fuel)
class H6():
    # 'Charts_M12_Local_Fuel'!H6
    value = 2003
    formula = "='Dashboard M10 RPS'!K5"
    @eval_fn
    def H6():
        k5_1 = Dashboard_M10_RPS.K5()
        return k5_1

@register(Charts_M12_Local_Fuel)
class I6():
    # 'Charts_M12_Local_Fuel'!I6
    value = 2004
    formula = "='Dashboard M10 RPS'!L5"
    @eval_fn
    def I6():
        l5_1 = Dashboard_M10_RPS.L5()
        return l5_1

@register(Charts_M12_Local_Fuel)
class J6():
    # 'Charts_M12_Local_Fuel'!J6
    value = 2005
    formula = "='Dashboard M10 RPS'!M5"
    @eval_fn
    def J6():
        m5_1 = Dashboard_M10_RPS.M5()
        return m5_1

@register(Charts_M12_Local_Fuel)
class K6():
    # 'Charts_M12_Local_Fuel'!K6
    value = 2006
    formula = "='Dashboard M10 RPS'!N5"
    @eval_fn
    def K6():
        n5_1 = Dashboard_M10_RPS.N5()
        return n5_1

@register(Charts_M12_Local_Fuel)
class L6():
    # 'Charts_M12_Local_Fuel'!L6
    value = 2007
    formula = "='Dashboard M10 RPS'!O5"
    @eval_fn
    def L6():
        o5_1 = Dashboard_M10_RPS.O5()
        return o5_1

@register(Charts_M12_Local_Fuel)
class M6():
    # 'Charts_M12_Local_Fuel'!M6
    value = 2008
    formula = "='Dashboard M10 RPS'!P5"
    @eval_fn
    def M6():
        p5_1 = Dashboard_M10_RPS.P5()
        return p5_1

@register(Charts_M12_Local_Fuel)
class N6():
    # 'Charts_M12_Local_Fuel'!N6
    value = 2009
    formula = "='Dashboard M10 RPS'!Q5"
    @eval_fn
    def N6():
        q5_1 = Dashboard_M10_RPS.Q5()
        return q5_1

@register(Charts_M12_Local_Fuel)
class O6():
    # 'Charts_M12_Local_Fuel'!O6
    value = 2010
    formula = "='Dashboard M10 RPS'!R5"
    @eval_fn
    def O6():
        r5_1 = Dashboard_M10_RPS.R5()
        return r5_1

@register(Charts_M12_Local_Fuel)
class P6():
    # 'Charts_M12_Local_Fuel'!P6
    value = 2011
    formula = "='Dashboard M10 RPS'!S5"
    @eval_fn
    def P6():
        s5_1 = Dashboard_M10_RPS.S5()
        return s5_1

@register(Charts_M12_Local_Fuel)
class Q6():
    # 'Charts_M12_Local_Fuel'!Q6
    value = 2012
    formula = "='Dashboard M10 RPS'!T5"
    @eval_fn
    def Q6():
        t5_1 = Dashboard_M10_RPS.T5()
        return t5_1

@register(Charts_M12_Local_Fuel)
class R6():
    # 'Charts_M12_Local_Fuel'!R6
    value = 2013
    formula = "='Dashboard M10 RPS'!U5"
    @eval_fn
    def R6():
        u5_1 = Dashboard_M10_RPS.U5()
        return u5_1

@register(Charts_M12_Local_Fuel)
class S6():
    # 'Charts_M12_Local_Fuel'!S6
    value = 2014
    formula = "='Dashboard M10 RPS'!V5"
    @eval_fn
    def S6():
        v5_1 = Dashboard_M10_RPS.V5()
        return v5_1

@register(Charts_M12_Local_Fuel)
class B7():
    # 'Charts_M12_Local_Fuel'!B7
    value = "Hydro"
    formula = "='Dashboard M12 Local Fuel'!C20"
    @eval_fn
    def B7():
        c20_1 = Dashboard_M12_Local_Fuel.C20()
        return c20_1

@register(Charts_M12_Local_Fuel)
class D7():
    # 'Charts_M12_Local_Fuel'!D7
    value = 0
    formula = "='Dashboard M12 Local Fuel'!G20"
    @eval_fn
    def D7():
        g20_1 = Dashboard_M12_Local_Fuel.G20()
        return g20_1

@register(Charts_M12_Local_Fuel)
class E7():
    # 'Charts_M12_Local_Fuel'!E7
    value = 0
    formula = "='Dashboard M12 Local Fuel'!H20"
    @eval_fn
    def E7():
        h20_1 = Dashboard_M12_Local_Fuel.H20()
        return h20_1

@register(Charts_M12_Local_Fuel)
class F7():
    # 'Charts_M12_Local_Fuel'!F7
    value = 0
    formula = "='Dashboard M12 Local Fuel'!I20"
    @eval_fn
    def F7():
        i20_1 = Dashboard_M12_Local_Fuel.I20()
        return i20_1

@register(Charts_M12_Local_Fuel)
class G7():
    # 'Charts_M12_Local_Fuel'!G7
    value = 0
    formula = "='Dashboard M12 Local Fuel'!J20"
    @eval_fn
    def G7():
        j20_1 = Dashboard_M12_Local_Fuel.J20()
        return j20_1

@register(Charts_M12_Local_Fuel)
class H7():
    # 'Charts_M12_Local_Fuel'!H7
    value = 25490
    formula = "='Dashboard M12 Local Fuel'!K20"
    @eval_fn
    def H7():
        k20_1 = Dashboard_M12_Local_Fuel.K20()
        return k20_1

@register(Charts_M12_Local_Fuel)
class I7():
    # 'Charts_M12_Local_Fuel'!I7
    value = 12001
    formula = "='Dashboard M12 Local Fuel'!L20"
    @eval_fn
    def I7():
        l20_1 = Dashboard_M12_Local_Fuel.L20()
        return l20_1

@register(Charts_M12_Local_Fuel)
class J7():
    # 'Charts_M12_Local_Fuel'!J7
    value = 115000
    formula = "='Dashboard M12 Local Fuel'!M20"
    @eval_fn
    def J7():
        m20_1 = Dashboard_M12_Local_Fuel.M20()
        return m20_1

@register(Charts_M12_Local_Fuel)
class K7():
    # 'Charts_M12_Local_Fuel'!K7
    value = 19628
    formula = "='Dashboard M12 Local Fuel'!N20"
    @eval_fn
    def K7():
        n20_1 = Dashboard_M12_Local_Fuel.N20()
        return n20_1

@register(Charts_M12_Local_Fuel)
class L7():
    # 'Charts_M12_Local_Fuel'!L7
    value = -34357
    formula = "='Dashboard M12 Local Fuel'!O20"
    @eval_fn
    def L7():
        o20_1 = Dashboard_M12_Local_Fuel.O20()
        return o20_1

@register(Charts_M12_Local_Fuel)
class M7():
    # 'Charts_M12_Local_Fuel'!M7
    value = -60191
    formula = "='Dashboard M12 Local Fuel'!P20"
    @eval_fn
    def M7():
        p20_1 = Dashboard_M12_Local_Fuel.P20()
        return p20_1

@register(Charts_M12_Local_Fuel)
class N7():
    # 'Charts_M12_Local_Fuel'!N7
    value = 29257
    formula = "='Dashboard M12 Local Fuel'!Q20"
    @eval_fn
    def N7():
        q20_1 = Dashboard_M12_Local_Fuel.Q20()
        return q20_1

@register(Charts_M12_Local_Fuel)
class O7():
    # 'Charts_M12_Local_Fuel'!O7
    value = -36733
    formula = "='Dashboard M12 Local Fuel'!R20"
    @eval_fn
    def O7():
        r20_1 = Dashboard_M12_Local_Fuel.R20()
        return r20_1

@register(Charts_M12_Local_Fuel)
class P7():
    # 'Charts_M12_Local_Fuel'!P7
    value = 20328
    formula = "='Dashboard M12 Local Fuel'!S20"
    @eval_fn
    def P7():
        s20_1 = Dashboard_M12_Local_Fuel.S20()
        return s20_1

@register(Charts_M12_Local_Fuel)
class Q7():
    # 'Charts_M12_Local_Fuel'!Q7
    value = 13555
    formula = "='Dashboard M12 Local Fuel'!T20"
    @eval_fn
    def Q7():
        t20_1 = Dashboard_M12_Local_Fuel.T20()
        return t20_1

@register(Charts_M12_Local_Fuel)
class R7():
    # 'Charts_M12_Local_Fuel'!R7
    value = -30472
    formula = "='Dashboard M12 Local Fuel'!U20"
    @eval_fn
    def R7():
        u20_1 = Dashboard_M12_Local_Fuel.U20()
        return u20_1

@register(Charts_M12_Local_Fuel)
class S7():
    # 'Charts_M12_Local_Fuel'!S7
    value = 11940
    formula = "='Dashboard M12 Local Fuel'!V20"
    @eval_fn
    def S7():
        v20_1 = Dashboard_M12_Local_Fuel.V20()
        return v20_1

@register(Charts_M12_Local_Fuel)
class B8():
    # 'Charts_M12_Local_Fuel'!B8
    value = "Geothermal"
    formula = "='Dashboard M12 Local Fuel'!C21"
    @eval_fn
    def B8():
        c21_1 = Dashboard_M12_Local_Fuel.C21()
        return c21_1

@register(Charts_M12_Local_Fuel)
class D8():
    # 'Charts_M12_Local_Fuel'!D8
    value = 0
    formula = "='Dashboard M12 Local Fuel'!G21"
    @eval_fn
    def D8():
        g21_1 = Dashboard_M12_Local_Fuel.G21()
        return g21_1

@register(Charts_M12_Local_Fuel)
class E8():
    # 'Charts_M12_Local_Fuel'!E8
    value = 0
    formula = "='Dashboard M12 Local Fuel'!H21"
    @eval_fn
    def E8():
        h21_1 = Dashboard_M12_Local_Fuel.H21()
        return h21_1

@register(Charts_M12_Local_Fuel)
class F8():
    # 'Charts_M12_Local_Fuel'!F8
    value = 0
    formula = "='Dashboard M12 Local Fuel'!I21"
    @eval_fn
    def F8():
        i21_1 = Dashboard_M12_Local_Fuel.I21()
        return i21_1

@register(Charts_M12_Local_Fuel)
class G8():
    # 'Charts_M12_Local_Fuel'!G8
    value = 0
    formula = "='Dashboard M12 Local Fuel'!J21"
    @eval_fn
    def G8():
        j21_1 = Dashboard_M12_Local_Fuel.J21()
        return j21_1

@register(Charts_M12_Local_Fuel)
class H8():
    # 'Charts_M12_Local_Fuel'!H8
    value = 0
    formula = "='Dashboard M12 Local Fuel'!K21"
    @eval_fn
    def H8():
        k21_1 = Dashboard_M12_Local_Fuel.K21()
        return k21_1

@register(Charts_M12_Local_Fuel)
class I8():
    # 'Charts_M12_Local_Fuel'!I8
    value = 0
    formula = "='Dashboard M12 Local Fuel'!L21"
    @eval_fn
    def I8():
        l21_1 = Dashboard_M12_Local_Fuel.L21()
        return l21_1

@register(Charts_M12_Local_Fuel)
class J8():
    # 'Charts_M12_Local_Fuel'!J8
    value = 221000
    formula = "='Dashboard M12 Local Fuel'!M21"
    @eval_fn
    def J8():
        m21_1 = Dashboard_M12_Local_Fuel.M21()
        return m21_1

@register(Charts_M12_Local_Fuel)
class K8():
    # 'Charts_M12_Local_Fuel'!K8
    value = -9000
    formula = "='Dashboard M12 Local Fuel'!N21"
    @eval_fn
    def K8():
        n21_1 = Dashboard_M12_Local_Fuel.N21()
        return n21_1

@register(Charts_M12_Local_Fuel)
class L8():
    # 'Charts_M12_Local_Fuel'!L8
    value = 18000
    formula = "='Dashboard M12 Local Fuel'!O21"
    @eval_fn
    def L8():
        o21_1 = Dashboard_M12_Local_Fuel.O21()
        return o21_1

@register(Charts_M12_Local_Fuel)
class M8():
    # 'Charts_M12_Local_Fuel'!M8
    value = 4334
    formula = "='Dashboard M12 Local Fuel'!P21"
    @eval_fn
    def M8():
        p21_1 = Dashboard_M12_Local_Fuel.P21()
        return p21_1

@register(Charts_M12_Local_Fuel)
class N8():
    # 'Charts_M12_Local_Fuel'!N8
    value = -66743
    formula = "='Dashboard M12 Local Fuel'!Q21"
    @eval_fn
    def N8():
        q21_1 = Dashboard_M12_Local_Fuel.Q21()
        return q21_1

@register(Charts_M12_Local_Fuel)
class O8():
    # 'Charts_M12_Local_Fuel'!O8
    value = 33996
    formula = "='Dashboard M12 Local Fuel'!R21"
    @eval_fn
    def O8():
        r21_1 = Dashboard_M12_Local_Fuel.R21()
        return r21_1

@register(Charts_M12_Local_Fuel)
class P8():
    # 'Charts_M12_Local_Fuel'!P8
    value = 31319
    formula = "='Dashboard M12 Local Fuel'!S21"
    @eval_fn
    def P8():
        s21_1 = Dashboard_M12_Local_Fuel.S21()
        return s21_1

@register(Charts_M12_Local_Fuel)
class Q8():
    # 'Charts_M12_Local_Fuel'!Q8
    value = 33328
    formula = "='Dashboard M12 Local Fuel'!T21"
    @eval_fn
    def Q8():
        t21_1 = Dashboard_M12_Local_Fuel.T21()
        return t21_1

@register(Charts_M12_Local_Fuel)
class R8():
    # 'Charts_M12_Local_Fuel'!R8
    value = 15183
    formula = "='Dashboard M12 Local Fuel'!U21"
    @eval_fn
    def R8():
        u21_1 = Dashboard_M12_Local_Fuel.U21()
        return u21_1

@register(Charts_M12_Local_Fuel)
class S8():
    # 'Charts_M12_Local_Fuel'!S8
    value = -26390
    formula = "='Dashboard M12 Local Fuel'!V21"
    @eval_fn
    def S8():
        v21_1 = Dashboard_M12_Local_Fuel.V21()
        return v21_1

@register(Charts_M12_Local_Fuel)
class B9():
    # 'Charts_M12_Local_Fuel'!B9
    value = "Wind "
    formula = "='Dashboard M12 Local Fuel'!C22"
    @eval_fn
    def B9():
        c22_1 = Dashboard_M12_Local_Fuel.C22()
        return c22_1

@register(Charts_M12_Local_Fuel)
class D9():
    # 'Charts_M12_Local_Fuel'!D9
    value = 0
    formula = "='Dashboard M12 Local Fuel'!G22"
    @eval_fn
    def D9():
        g22_1 = Dashboard_M12_Local_Fuel.G22()
        return g22_1

@register(Charts_M12_Local_Fuel)
class E9():
    # 'Charts_M12_Local_Fuel'!E9
    value = 0
    formula = "='Dashboard M12 Local Fuel'!H22"
    @eval_fn
    def E9():
        h22_1 = Dashboard_M12_Local_Fuel.H22()
        return h22_1

@register(Charts_M12_Local_Fuel)
class F9():
    # 'Charts_M12_Local_Fuel'!F9
    value = 0
    formula = "='Dashboard M12 Local Fuel'!I22"
    @eval_fn
    def F9():
        i22_1 = Dashboard_M12_Local_Fuel.I22()
        return i22_1

@register(Charts_M12_Local_Fuel)
class G9():
    # 'Charts_M12_Local_Fuel'!G9
    value = 0
    formula = "='Dashboard M12 Local Fuel'!J22"
    @eval_fn
    def G9():
        j22_1 = Dashboard_M12_Local_Fuel.J22()
        return j22_1

@register(Charts_M12_Local_Fuel)
class H9():
    # 'Charts_M12_Local_Fuel'!H9
    value = 0
    formula = "='Dashboard M12 Local Fuel'!K22"
    @eval_fn
    def H9():
        k22_1 = Dashboard_M12_Local_Fuel.K22()
        return k22_1

@register(Charts_M12_Local_Fuel)
class I9():
    # 'Charts_M12_Local_Fuel'!I9
    value = 0
    formula = "='Dashboard M12 Local Fuel'!L22"
    @eval_fn
    def I9():
        l22_1 = Dashboard_M12_Local_Fuel.L22()
        return l22_1

@register(Charts_M12_Local_Fuel)
class J9():
    # 'Charts_M12_Local_Fuel'!J9
    value = 7000
    formula = "='Dashboard M12 Local Fuel'!M22"
    @eval_fn
    def J9():
        m22_1 = Dashboard_M12_Local_Fuel.M22()
        return m22_1

@register(Charts_M12_Local_Fuel)
class K9():
    # 'Charts_M12_Local_Fuel'!K9
    value = 75000
    formula = "='Dashboard M12 Local Fuel'!N22"
    @eval_fn
    def K9():
        n22_1 = Dashboard_M12_Local_Fuel.N22()
        return n22_1

@register(Charts_M12_Local_Fuel)
class L9():
    # 'Charts_M12_Local_Fuel'!L9
    value = 160400
    formula = "='Dashboard M12 Local Fuel'!O22"
    @eval_fn
    def L9():
        o22_1 = Dashboard_M12_Local_Fuel.O22()
        return o22_1

@register(Charts_M12_Local_Fuel)
class M9():
    # 'Charts_M12_Local_Fuel'!M9
    value = -5107
    formula = "='Dashboard M12 Local Fuel'!P22"
    @eval_fn
    def M9():
        p22_1 = Dashboard_M12_Local_Fuel.P22()
        return p22_1

@register(Charts_M12_Local_Fuel)
class N9():
    # 'Charts_M12_Local_Fuel'!N9
    value = 13062
    formula = "='Dashboard M12 Local Fuel'!Q22"
    @eval_fn
    def N9():
        q22_1 = Dashboard_M12_Local_Fuel.Q22()
        return q22_1

@register(Charts_M12_Local_Fuel)
class O9():
    # 'Charts_M12_Local_Fuel'!O9
    value = 10851
    formula = "='Dashboard M12 Local Fuel'!R22"
    @eval_fn
    def O9():
        r22_1 = Dashboard_M12_Local_Fuel.R22()
        return r22_1

@register(Charts_M12_Local_Fuel)
class P9():
    # 'Charts_M12_Local_Fuel'!P9
    value = 83170
    formula = "='Dashboard M12 Local Fuel'!S22"
    @eval_fn
    def P9():
        s22_1 = Dashboard_M12_Local_Fuel.S22()
        return s22_1

@register(Charts_M12_Local_Fuel)
class Q9():
    # 'Charts_M12_Local_Fuel'!Q9
    value = 43880
    formula = "='Dashboard M12 Local Fuel'!T22"
    @eval_fn
    def Q9():
        t22_1 = Dashboard_M12_Local_Fuel.T22()
        return t22_1

@register(Charts_M12_Local_Fuel)
class R9():
    # 'Charts_M12_Local_Fuel'!R9
    value = 115292
    formula = "='Dashboard M12 Local Fuel'!U22"
    @eval_fn
    def R9():
        u22_1 = Dashboard_M12_Local_Fuel.U22()
        return u22_1

@register(Charts_M12_Local_Fuel)
class S9():
    # 'Charts_M12_Local_Fuel'!S9
    value = 74319
    formula = "='Dashboard M12 Local Fuel'!V22"
    @eval_fn
    def S9():
        v22_1 = Dashboard_M12_Local_Fuel.V22()
        return v22_1

@register(Charts_M12_Local_Fuel)
class B10():
    # 'Charts_M12_Local_Fuel'!B10
    value = "Biomass "
    formula = "='Dashboard M12 Local Fuel'!C23"
    @eval_fn
    def B10():
        c23_1 = Dashboard_M12_Local_Fuel.C23()
        return c23_1

@register(Charts_M12_Local_Fuel)
class D10():
    # 'Charts_M12_Local_Fuel'!D10
    value = 0
    formula = "='Dashboard M12 Local Fuel'!G23"
    @eval_fn
    def D10():
        g23_1 = Dashboard_M12_Local_Fuel.G23()
        return g23_1

@register(Charts_M12_Local_Fuel)
class E10():
    # 'Charts_M12_Local_Fuel'!E10
    value = 0
    formula = "='Dashboard M12 Local Fuel'!H23"
    @eval_fn
    def E10():
        h23_1 = Dashboard_M12_Local_Fuel.H23()
        return h23_1

@register(Charts_M12_Local_Fuel)
class F10():
    # 'Charts_M12_Local_Fuel'!F10
    value = 0
    formula = "='Dashboard M12 Local Fuel'!I23"
    @eval_fn
    def F10():
        i23_1 = Dashboard_M12_Local_Fuel.I23()
        return i23_1

@register(Charts_M12_Local_Fuel)
class G10():
    # 'Charts_M12_Local_Fuel'!G10
    value = 0
    formula = "='Dashboard M12 Local Fuel'!J23"
    @eval_fn
    def G10():
        j23_1 = Dashboard_M12_Local_Fuel.J23()
        return j23_1

@register(Charts_M12_Local_Fuel)
class H10():
    # 'Charts_M12_Local_Fuel'!H10
    value = 0
    formula = "='Dashboard M12 Local Fuel'!K23"
    @eval_fn
    def H10():
        k23_1 = Dashboard_M12_Local_Fuel.K23()
        return k23_1

@register(Charts_M12_Local_Fuel)
class I10():
    # 'Charts_M12_Local_Fuel'!I10
    value = 0
    formula = "='Dashboard M12 Local Fuel'!L23"
    @eval_fn
    def I10():
        l23_1 = Dashboard_M12_Local_Fuel.L23()
        return l23_1

@register(Charts_M12_Local_Fuel)
class J10():
    # 'Charts_M12_Local_Fuel'!J10
    value = 333000
    formula = "='Dashboard M12 Local Fuel'!M23"
    @eval_fn
    def J10():
        m23_1 = Dashboard_M12_Local_Fuel.M23()
        return m23_1

@register(Charts_M12_Local_Fuel)
class K10():
    # 'Charts_M12_Local_Fuel'!K10
    value = 62000
    formula = "='Dashboard M12 Local Fuel'!N23"
    @eval_fn
    def K10():
        n23_1 = Dashboard_M12_Local_Fuel.N23()
        return n23_1

@register(Charts_M12_Local_Fuel)
class L10():
    # 'Charts_M12_Local_Fuel'!L10
    value = -69000
    formula = "='Dashboard M12 Local Fuel'!O23"
    @eval_fn
    def L10():
        o23_1 = Dashboard_M12_Local_Fuel.O23()
        return o23_1

@register(Charts_M12_Local_Fuel)
class M10():
    # 'Charts_M12_Local_Fuel'!M10
    value = 86598
    formula = "='Dashboard M12 Local Fuel'!P23"
    @eval_fn
    def M10():
        p23_1 = Dashboard_M12_Local_Fuel.P23()
        return p23_1

@register(Charts_M12_Local_Fuel)
class N10():
    # 'Charts_M12_Local_Fuel'!N10
    value = -13843
    formula = "='Dashboard M12 Local Fuel'!Q23"
    @eval_fn
    def N10():
        q23_1 = Dashboard_M12_Local_Fuel.Q23()
        return q23_1

@register(Charts_M12_Local_Fuel)
class O10():
    # 'Charts_M12_Local_Fuel'!O10
    value = -39903
    formula = "='Dashboard M12 Local Fuel'!R23"
    @eval_fn
    def O10():
        r23_1 = Dashboard_M12_Local_Fuel.R23()
        return r23_1

@register(Charts_M12_Local_Fuel)
class P10():
    # 'Charts_M12_Local_Fuel'!P10
    value = 6414
    formula = "='Dashboard M12 Local Fuel'!S23"
    @eval_fn
    def P10():
        s23_1 = Dashboard_M12_Local_Fuel.S23()
        return s23_1

@register(Charts_M12_Local_Fuel)
class Q10():
    # 'Charts_M12_Local_Fuel'!Q10
    value = -23476
    formula = "='Dashboard M12 Local Fuel'!T23"
    @eval_fn
    def Q10():
        t23_1 = Dashboard_M12_Local_Fuel.T23()
        return t23_1

@register(Charts_M12_Local_Fuel)
class R10():
    # 'Charts_M12_Local_Fuel'!R10
    value = 73901
    formula = "='Dashboard M12 Local Fuel'!U23"
    @eval_fn
    def R10():
        u23_1 = Dashboard_M12_Local_Fuel.U23()
        return u23_1

@register(Charts_M12_Local_Fuel)
class S10():
    # 'Charts_M12_Local_Fuel'!S10
    value = 17473
    formula = "='Dashboard M12 Local Fuel'!V23"
    @eval_fn
    def S10():
        v23_1 = Dashboard_M12_Local_Fuel.V23()
        return v23_1

@register(Charts_M12_Local_Fuel)
class B11():
    # 'Charts_M12_Local_Fuel'!B11
    value = "Solar "
    formula = "='Dashboard M12 Local Fuel'!C24"
    @eval_fn
    def B11():
        c24_1 = Dashboard_M12_Local_Fuel.C24()
        return c24_1

@register(Charts_M12_Local_Fuel)
class D11():
    # 'Charts_M12_Local_Fuel'!D11
    value = 0
    formula = "='Dashboard M12 Local Fuel'!G24"
    @eval_fn
    def D11():
        g24_1 = Dashboard_M12_Local_Fuel.G24()
        return g24_1

@register(Charts_M12_Local_Fuel)
class E11():
    # 'Charts_M12_Local_Fuel'!E11
    value = 0
    formula = "='Dashboard M12 Local Fuel'!H24"
    @eval_fn
    def E11():
        h24_1 = Dashboard_M12_Local_Fuel.H24()
        return h24_1

@register(Charts_M12_Local_Fuel)
class F11():
    # 'Charts_M12_Local_Fuel'!F11
    value = 0
    formula = "='Dashboard M12 Local Fuel'!I24"
    @eval_fn
    def F11():
        i24_1 = Dashboard_M12_Local_Fuel.I24()
        return i24_1

@register(Charts_M12_Local_Fuel)
class G11():
    # 'Charts_M12_Local_Fuel'!G11
    value = 0
    formula = "='Dashboard M12 Local Fuel'!J24"
    @eval_fn
    def G11():
        j24_1 = Dashboard_M12_Local_Fuel.J24()
        return j24_1

@register(Charts_M12_Local_Fuel)
class H11():
    # 'Charts_M12_Local_Fuel'!H11
    value = 66
    formula = "='Dashboard M12 Local Fuel'!K24"
    @eval_fn
    def H11():
        k24_1 = Dashboard_M12_Local_Fuel.K24()
        return k24_1

@register(Charts_M12_Local_Fuel)
class I11():
    # 'Charts_M12_Local_Fuel'!I11
    value = 24
    formula = "='Dashboard M12 Local Fuel'!L24"
    @eval_fn
    def I11():
        l24_1 = Dashboard_M12_Local_Fuel.L24()
        return l24_1

@register(Charts_M12_Local_Fuel)
class J11():
    # 'Charts_M12_Local_Fuel'!J11
    value = -90
    formula = "='Dashboard M12 Local Fuel'!M24"
    @eval_fn
    def J11():
        m24_1 = Dashboard_M12_Local_Fuel.M24()
        return m24_1

@register(Charts_M12_Local_Fuel)
class K11():
    # 'Charts_M12_Local_Fuel'!K11
    value = 0
    formula = "='Dashboard M12 Local Fuel'!N24"
    @eval_fn
    def K11():
        n24_1 = Dashboard_M12_Local_Fuel.N24()
        return n24_1

@register(Charts_M12_Local_Fuel)
class L11():
    # 'Charts_M12_Local_Fuel'!L11
    value = 7913.58339639
    formula = "='Dashboard M12 Local Fuel'!O24"
    @eval_fn
    def L11():
        o24_1 = Dashboard_M12_Local_Fuel.O24()
        return o24_1

@register(Charts_M12_Local_Fuel)
class M11():
    # 'Charts_M12_Local_Fuel'!M11
    value = 6350.23260361
    formula = "='Dashboard M12 Local Fuel'!P24"
    @eval_fn
    def M11():
        p24_1 = Dashboard_M12_Local_Fuel.P24()
        return p24_1

@register(Charts_M12_Local_Fuel)
class N11():
    # 'Charts_M12_Local_Fuel'!N11
    value = 22147.448
    formula = "='Dashboard M12 Local Fuel'!Q24"
    @eval_fn
    def N11():
        q24_1 = Dashboard_M12_Local_Fuel.Q24()
        return q24_1

@register(Charts_M12_Local_Fuel)
class O11():
    # 'Charts_M12_Local_Fuel'!O11
    value = 20106.509
    formula = "='Dashboard M12 Local Fuel'!R24"
    @eval_fn
    def O11():
        r24_1 = Dashboard_M12_Local_Fuel.R24()
        return r24_1

@register(Charts_M12_Local_Fuel)
class P11():
    # 'Charts_M12_Local_Fuel'!P11
    value = 40509.337
    formula = "='Dashboard M12 Local Fuel'!S24"
    @eval_fn
    def P11():
        s24_1 = Dashboard_M12_Local_Fuel.S24()
        return s24_1

@register(Charts_M12_Local_Fuel)
class Q11():
    # 'Charts_M12_Local_Fuel'!Q11
    value = 110382.655
    formula = "='Dashboard M12 Local Fuel'!T24"
    @eval_fn
    def Q11():
        t24_1 = Dashboard_M12_Local_Fuel.T24()
        return t24_1

@register(Charts_M12_Local_Fuel)
class R11():
    # 'Charts_M12_Local_Fuel'!R11
    value = 194708.763253
    formula = "='Dashboard M12 Local Fuel'!U24"
    @eval_fn
    def R11():
        u24_1 = Dashboard_M12_Local_Fuel.U24()
        return u24_1

@register(Charts_M12_Local_Fuel)
class S11():
    # 'Charts_M12_Local_Fuel'!S11
    value = 191109.415379
    formula = "='Dashboard M12 Local Fuel'!V24"
    @eval_fn
    def S11():
        v24_1 = Dashboard_M12_Local_Fuel.V24()
        return v24_1

@register(Charts_M12_Local_Fuel)
class B12():
    # 'Charts_M12_Local_Fuel'!B12
    value = "Biofuels "
    formula = "='Dashboard M12 Local Fuel'!C25"
    @eval_fn
    def B12():
        c25_1 = Dashboard_M12_Local_Fuel.C25()
        return c25_1

@register(Charts_M12_Local_Fuel)
class D12():
    # 'Charts_M12_Local_Fuel'!D12
    value = 0
    formula = "='Dashboard M12 Local Fuel'!G25"
    @eval_fn
    def D12():
        g25_1 = Dashboard_M12_Local_Fuel.G25()
        return g25_1

@register(Charts_M12_Local_Fuel)
class E12():
    # 'Charts_M12_Local_Fuel'!E12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!H25"
    @eval_fn
    def E12():
        h25_1 = Dashboard_M12_Local_Fuel.H25()
        return h25_1

@register(Charts_M12_Local_Fuel)
class F12():
    # 'Charts_M12_Local_Fuel'!F12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!I25"
    @eval_fn
    def F12():
        i25_1 = Dashboard_M12_Local_Fuel.I25()
        return i25_1

@register(Charts_M12_Local_Fuel)
class G12():
    # 'Charts_M12_Local_Fuel'!G12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!J25"
    @eval_fn
    def G12():
        j25_1 = Dashboard_M12_Local_Fuel.J25()
        return j25_1

@register(Charts_M12_Local_Fuel)
class H12():
    # 'Charts_M12_Local_Fuel'!H12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!K25"
    @eval_fn
    def H12():
        k25_1 = Dashboard_M12_Local_Fuel.K25()
        return k25_1

@register(Charts_M12_Local_Fuel)
class I12():
    # 'Charts_M12_Local_Fuel'!I12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!L25"
    @eval_fn
    def I12():
        l25_1 = Dashboard_M12_Local_Fuel.L25()
        return l25_1

@register(Charts_M12_Local_Fuel)
class J12():
    # 'Charts_M12_Local_Fuel'!J12
    value = 252
    formula = "='Dashboard M12 Local Fuel'!M25"
    @eval_fn
    def J12():
        m25_1 = Dashboard_M12_Local_Fuel.M25()
        return m25_1

@register(Charts_M12_Local_Fuel)
class K12():
    # 'Charts_M12_Local_Fuel'!K12
    value = 14
    formula = "='Dashboard M12 Local Fuel'!N25"
    @eval_fn
    def K12():
        n25_1 = Dashboard_M12_Local_Fuel.N25()
        return n25_1

@register(Charts_M12_Local_Fuel)
class L12():
    # 'Charts_M12_Local_Fuel'!L12
    value = 1310
    formula = "='Dashboard M12 Local Fuel'!O25"
    @eval_fn
    def L12():
        o25_1 = Dashboard_M12_Local_Fuel.O25()
        return o25_1

@register(Charts_M12_Local_Fuel)
class M12():
    # 'Charts_M12_Local_Fuel'!M12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!P25"
    @eval_fn
    def M12():
        p25_1 = Dashboard_M12_Local_Fuel.P25()
        return p25_1

@register(Charts_M12_Local_Fuel)
class N12():
    # 'Charts_M12_Local_Fuel'!N12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!Q25"
    @eval_fn
    def N12():
        q25_1 = Dashboard_M12_Local_Fuel.Q25()
        return q25_1

@register(Charts_M12_Local_Fuel)
class O12():
    # 'Charts_M12_Local_Fuel'!O12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!R25"
    @eval_fn
    def O12():
        r25_1 = Dashboard_M12_Local_Fuel.R25()
        return r25_1

@register(Charts_M12_Local_Fuel)
class P12():
    # 'Charts_M12_Local_Fuel'!P12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!S25"
    @eval_fn
    def P12():
        s25_1 = Dashboard_M12_Local_Fuel.S25()
        return s25_1

@register(Charts_M12_Local_Fuel)
class Q12():
    # 'Charts_M12_Local_Fuel'!Q12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!T25"
    @eval_fn
    def Q12():
        t25_1 = Dashboard_M12_Local_Fuel.T25()
        return t25_1

@register(Charts_M12_Local_Fuel)
class R12():
    # 'Charts_M12_Local_Fuel'!R12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!U25"
    @eval_fn
    def R12():
        u25_1 = Dashboard_M12_Local_Fuel.U25()
        return u25_1

@register(Charts_M12_Local_Fuel)
class S12():
    # 'Charts_M12_Local_Fuel'!S12
    value = "#REF!"
    formula = "='Dashboard M12 Local Fuel'!V25"
    @eval_fn
    def S12():
        v25_1 = Dashboard_M12_Local_Fuel.V25()
        return v25_1

@register(Charts_M12_Local_Fuel)
class B13():
    # 'Charts_M12_Local_Fuel'!B13
    value = "Total"
    formula = "='Dashboard M12 Local Fuel'!C26"
    @eval_fn
    def B13():
        c26_1 = Dashboard_M12_Local_Fuel.C26()
        return c26_1

@register(Charts_M12_Local_Fuel)
class D13():
    # 'Charts_M12_Local_Fuel'!D13
    value = 0
    formula = "='Dashboard M12 Local Fuel'!G26"
    @eval_fn
    def D13():
        g26_1 = Dashboard_M12_Local_Fuel.G26()
        return g26_1

@register(Charts_M12_Local_Fuel)
class E13():
    # 'Charts_M12_Local_Fuel'!E13
    value = 39000
    formula = "='Dashboard M12 Local Fuel'!H26"
    @eval_fn
    def E13():
        h26_1 = Dashboard_M12_Local_Fuel.H26()
        return h26_1

@register(Charts_M12_Local_Fuel)
class F13():
    # 'Charts_M12_Local_Fuel'!F13
    value = -66000
    formula = "='Dashboard M12 Local Fuel'!I26"
    @eval_fn
    def F13():
        i26_1 = Dashboard_M12_Local_Fuel.I26()
        return i26_1

@register(Charts_M12_Local_Fuel)
class G13():
    # 'Charts_M12_Local_Fuel'!G13
    value = -96000
    formula = "='Dashboard M12 Local Fuel'!J26"
    @eval_fn
    def G13():
        j26_1 = Dashboard_M12_Local_Fuel.J26()
        return j26_1

@register(Charts_M12_Local_Fuel)
class H13():
    # 'Charts_M12_Local_Fuel'!H13
    value = 157156
    formula = "='Dashboard M12 Local Fuel'!K26"
    @eval_fn
    def H13():
        k26_1 = Dashboard_M12_Local_Fuel.K26()
        return k26_1

@register(Charts_M12_Local_Fuel)
class I13():
    # 'Charts_M12_Local_Fuel'!I13
    value = 61782
    formula = "='Dashboard M12 Local Fuel'!L26"
    @eval_fn
    def I13():
        l26_1 = Dashboard_M12_Local_Fuel.L26()
        return l26_1

@register(Charts_M12_Local_Fuel)
class J13():
    # 'Charts_M12_Local_Fuel'!J13
    value = -21406.1209292
    formula = "='Dashboard M12 Local Fuel'!M26"
    @eval_fn
    def J13():
        m26_1 = Dashboard_M12_Local_Fuel.M26()
        return m26_1

@register(Charts_M12_Local_Fuel)
class K13():
    # 'Charts_M12_Local_Fuel'!K13
    value = 148803.323391
    formula = "='Dashboard M12 Local Fuel'!N26"
    @eval_fn
    def K13():
        n26_1 = Dashboard_M12_Local_Fuel.N26()
        return n26_1

@register(Charts_M12_Local_Fuel)
class L13():
    # 'Charts_M12_Local_Fuel'!L13
    value = 80573.380935
    formula = "='Dashboard M12 Local Fuel'!O26"
    @eval_fn
    def L13():
        o26_1 = Dashboard_M12_Local_Fuel.O26()
        return o26_1

@register(Charts_M12_Local_Fuel)
class M13():
    # 'Charts_M12_Local_Fuel'!M13
    value = 31690.2326036
    formula = "='Dashboard M12 Local Fuel'!P26"
    @eval_fn
    def M13():
        p26_1 = Dashboard_M12_Local_Fuel.P26()
        return p26_1

@register(Charts_M12_Local_Fuel)
class N13():
    # 'Charts_M12_Local_Fuel'!N13
    value = -12781.552
    formula = "='Dashboard M12 Local Fuel'!Q26"
    @eval_fn
    def N13():
        q26_1 = Dashboard_M12_Local_Fuel.Q26()
        return q26_1

@register(Charts_M12_Local_Fuel)
class O13():
    # 'Charts_M12_Local_Fuel'!O13
    value = -13399.491
    formula = "='Dashboard M12 Local Fuel'!R26"
    @eval_fn
    def O13():
        r26_1 = Dashboard_M12_Local_Fuel.R26()
        return r26_1

@register(Charts_M12_Local_Fuel)
class P13():
    # 'Charts_M12_Local_Fuel'!P13
    value = 237855.337
    formula = "='Dashboard M12 Local Fuel'!S26"
    @eval_fn
    def P13():
        s26_1 = Dashboard_M12_Local_Fuel.S26()
        return s26_1

@register(Charts_M12_Local_Fuel)
class Q13():
    # 'Charts_M12_Local_Fuel'!Q13
    value = 141024.655
    formula = "='Dashboard M12 Local Fuel'!T26"
    @eval_fn
    def Q13():
        t26_1 = Dashboard_M12_Local_Fuel.T26()
        return t26_1

@register(Charts_M12_Local_Fuel)
class R13():
    # 'Charts_M12_Local_Fuel'!R13
    value = 388268.763253
    formula = "='Dashboard M12 Local Fuel'!U26"
    @eval_fn
    def R13():
        u26_1 = Dashboard_M12_Local_Fuel.U26()
        return u26_1

@register(Charts_M12_Local_Fuel)
class S13():
    # 'Charts_M12_Local_Fuel'!S13
    value = 285600.415379
    formula = "='Dashboard M12 Local Fuel'!V26"
    @eval_fn
    def S13():
        v26_1 = Dashboard_M12_Local_Fuel.V26()
        return v26_1

@register(Charts_M12_Local_Fuel)
class T13():
    # 'Charts_M12_Local_Fuel'!T13
    value = "Distributed PV Included in renewable generation"

@register(Charts_M12_Local_Fuel)
class B16():
    # 'Charts_M12_Local_Fuel'!B16
    value = "Annual Change in Production of Local Renewable Fuels"

@register(Charts_M12_Local_Fuel)
class O16():
    # 'Charts_M12_Local_Fuel'!O16
    value = "Hawaii Renewable Generation by Fuel"

@register(Charts_M12_Local_Fuel)
class B17():
    # 'Charts_M12_Local_Fuel'!B17
    value = False

@register(Charts_M12_Local_Fuel)
class B21():
    # 'Charts_M12_Local_Fuel'!B21
    value = True

@register(Charts_M12_Local_Fuel)
class C21():
    # 'Charts_M12_Local_Fuel'!C21
    value = True

@register(Charts_M12_Local_Fuel)
class D21():
    # 'Charts_M12_Local_Fuel'!D21
    value = True

@register(Charts_M12_Local_Fuel)
class E21():
    # 'Charts_M12_Local_Fuel'!E21
    value = True

@register(Charts_M12_Local_Fuel)
class F21():
    # 'Charts_M12_Local_Fuel'!F21
    value = True

@register(Charts_M12_Local_Fuel)
class G21():
    # 'Charts_M12_Local_Fuel'!G21
    value = True

@register(Charts_M12_Local_Fuel)
class H21():
    # 'Charts_M12_Local_Fuel'!H21
    value = True

@register(Charts_M12_Local_Fuel)
class Q21():
    # 'Charts_M12_Local_Fuel'!Q21
    value = True

@register(Charts_M12_Local_Fuel)
class R21():
    # 'Charts_M12_Local_Fuel'!R21
    value = True

@register(Charts_M12_Local_Fuel)
class S21():
    # 'Charts_M12_Local_Fuel'!S21
    value = True

@register(Charts_M12_Local_Fuel)
class T21():
    # 'Charts_M12_Local_Fuel'!T21
    value = True

@register(Charts_M12_Local_Fuel)
class U21():
    # 'Charts_M12_Local_Fuel'!U21
    value = True

@register(Charts_M12_Local_Fuel)
class V21():
    # 'Charts_M12_Local_Fuel'!V21
    value = True

@register(Charts_M12_Local_Fuel)
class W21():
    # 'Charts_M12_Local_Fuel'!W21
    value = True

@register(Charts_M12_Local_Fuel)
class O37():
    # 'Charts_M12_Local_Fuel'!O37
    value = "Percent of Total Hawaii  Energy Consumption by Fuel"