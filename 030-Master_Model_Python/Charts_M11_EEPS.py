# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M11_EEPS = Worksheet('Charts_M11_EEPS', 10, 10)



@register(Charts_M11_EEPS)
class B2():
    # 'Charts_M11_EEPS'!B2
    value = 1

@register(Charts_M11_EEPS)
class D2():
    # 'Charts_M11_EEPS'!D2
    value = "       Metric 11: Percentage attainment of the Energy Efficiency Portfolio Standard (EEPS)"

@register(Charts_M11_EEPS)
class B3():
    # 'Charts_M11_EEPS'!B3
    value = 5

@register(Charts_M11_EEPS)
class B5():
    # 'Charts_M11_EEPS'!B5
    value = "Fixed Reduction Input:"

@register(Charts_M11_EEPS)
class D5():
    # 'Charts_M11_EEPS'!D5
    value = 0.3

@register(Charts_M11_EEPS)
class D7():
    # 'Charts_M11_EEPS'!D7
    value = 1999
    formula = "='Dashboard M10 RPS'!G5"
    @eval_fn
    def D7():
        g5_1 = Dashboard_M10_RPS.G5()
        return g5_1

@register(Charts_M11_EEPS)
class E7():
    # 'Charts_M11_EEPS'!E7
    value = 2000
    formula = "='Dashboard M10 RPS'!H5"
    @eval_fn
    def E7():
        h5_1 = Dashboard_M10_RPS.H5()
        return h5_1

@register(Charts_M11_EEPS)
class F7():
    # 'Charts_M11_EEPS'!F7
    value = 2001
    formula = "='Dashboard M10 RPS'!I5"
    @eval_fn
    def F7():
        i5_1 = Dashboard_M10_RPS.I5()
        return i5_1

@register(Charts_M11_EEPS)
class G7():
    # 'Charts_M11_EEPS'!G7
    value = 2002
    formula = "='Dashboard M10 RPS'!J5"
    @eval_fn
    def G7():
        j5_1 = Dashboard_M10_RPS.J5()
        return j5_1

@register(Charts_M11_EEPS)
class H7():
    # 'Charts_M11_EEPS'!H7
    value = 2003
    formula = "='Dashboard M10 RPS'!K5"
    @eval_fn
    def H7():
        k5_1 = Dashboard_M10_RPS.K5()
        return k5_1

@register(Charts_M11_EEPS)
class I7():
    # 'Charts_M11_EEPS'!I7
    value = 2004
    formula = "='Dashboard M10 RPS'!L5"
    @eval_fn
    def I7():
        l5_1 = Dashboard_M10_RPS.L5()
        return l5_1

@register(Charts_M11_EEPS)
class J7():
    # 'Charts_M11_EEPS'!J7
    value = 2005
    formula = "='Dashboard M10 RPS'!M5"
    @eval_fn
    def J7():
        m5_1 = Dashboard_M10_RPS.M5()
        return m5_1

@register(Charts_M11_EEPS)
class K7():
    # 'Charts_M11_EEPS'!K7
    value = 2006
    formula = "='Dashboard M10 RPS'!N5"
    @eval_fn
    def K7():
        n5_1 = Dashboard_M10_RPS.N5()
        return n5_1

@register(Charts_M11_EEPS)
class L7():
    # 'Charts_M11_EEPS'!L7
    value = 2007
    formula = "='Dashboard M10 RPS'!O5"
    @eval_fn
    def L7():
        o5_1 = Dashboard_M10_RPS.O5()
        return o5_1

@register(Charts_M11_EEPS)
class M7():
    # 'Charts_M11_EEPS'!M7
    value = 2008
    formula = "='Dashboard M10 RPS'!P5"
    @eval_fn
    def M7():
        p5_1 = Dashboard_M10_RPS.P5()
        return p5_1

@register(Charts_M11_EEPS)
class N7():
    # 'Charts_M11_EEPS'!N7
    value = 2009
    formula = "='Dashboard M10 RPS'!Q5"
    @eval_fn
    def N7():
        q5_1 = Dashboard_M10_RPS.Q5()
        return q5_1

@register(Charts_M11_EEPS)
class O7():
    # 'Charts_M11_EEPS'!O7
    value = 2010
    formula = "='Dashboard M10 RPS'!R5"
    @eval_fn
    def O7():
        r5_1 = Dashboard_M10_RPS.R5()
        return r5_1

@register(Charts_M11_EEPS)
class P7():
    # 'Charts_M11_EEPS'!P7
    value = 2011
    formula = "='Dashboard M10 RPS'!S5"
    @eval_fn
    def P7():
        s5_1 = Dashboard_M10_RPS.S5()
        return s5_1

@register(Charts_M11_EEPS)
class Q7():
    # 'Charts_M11_EEPS'!Q7
    value = 2012
    formula = "='Dashboard M10 RPS'!T5"
    @eval_fn
    def Q7():
        t5_1 = Dashboard_M10_RPS.T5()
        return t5_1

@register(Charts_M11_EEPS)
class R7():
    # 'Charts_M11_EEPS'!R7
    value = 2013
    formula = "='Dashboard M10 RPS'!U5"
    @eval_fn
    def R7():
        u5_1 = Dashboard_M10_RPS.U5()
        return u5_1

@register(Charts_M11_EEPS)
class S7():
    # 'Charts_M11_EEPS'!S7
    value = 2014
    formula = "='Dashboard M10 RPS'!V5"
    @eval_fn
    def S7():
        v5_1 = Dashboard_M10_RPS.V5()
        return v5_1

@register(Charts_M11_EEPS)
class B8():
    # 'Charts_M11_EEPS'!B8
    value = "HECO"
    formula = "='Charts Data M10'!D5"
    @eval_fn
    def B8():
        d5_1 = Charts_Data_M10.D5()
        return d5_1

@register(Charts_M11_EEPS)
class D8():
    # 'Charts_M11_EEPS'!D8
    value = None
    formula = '''=IFERROR('Charts Data M11'!G4,"")'''
    @eval_fn
    def D8():
        g4_1 = Charts_Data_M11.G4()
        var_1 = IFERROR(g4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class E8():
    # 'Charts_M11_EEPS'!E8
    value = None
    formula = '''=IFERROR('Charts Data M11'!H4,"")'''
    @eval_fn
    def E8():
        h4_1 = Charts_Data_M11.H4()
        var_1 = IFERROR(h4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class F8():
    # 'Charts_M11_EEPS'!F8
    value = None
    formula = '''=IFERROR('Charts Data M11'!I4,"")'''
    @eval_fn
    def F8():
        i4_1 = Charts_Data_M11.I4()
        var_1 = IFERROR(i4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class G8():
    # 'Charts_M11_EEPS'!G8
    value = None
    formula = '''=IFERROR('Charts Data M11'!J4,"")'''
    @eval_fn
    def G8():
        j4_1 = Charts_Data_M11.J4()
        var_1 = IFERROR(j4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class H8():
    # 'Charts_M11_EEPS'!H8
    value = None
    formula = '''=IFERROR('Charts Data M11'!K4,"")'''
    @eval_fn
    def H8():
        k4_1 = Charts_Data_M11.K4()
        var_1 = IFERROR(k4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class I8():
    # 'Charts_M11_EEPS'!I8
    value = None
    formula = '''=IFERROR('Charts Data M11'!L4,"")'''
    @eval_fn
    def I8():
        l4_1 = Charts_Data_M11.L4()
        var_1 = IFERROR(l4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class J8():
    # 'Charts_M11_EEPS'!J8
    value = None
    formula = '''=IFERROR('Charts Data M11'!M4,"")'''
    @eval_fn
    def J8():
        m4_1 = Charts_Data_M11.M4()
        var_1 = IFERROR(m4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class K8():
    # 'Charts_M11_EEPS'!K8
    value = None
    formula = '''=IFERROR('Charts Data M11'!N4,"")'''
    @eval_fn
    def K8():
        n4_1 = Charts_Data_M11.N4()
        var_1 = IFERROR(n4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class L8():
    # 'Charts_M11_EEPS'!L8
    value = None
    formula = '''=IFERROR('Charts Data M11'!O4,"")'''
    @eval_fn
    def L8():
        o4_1 = Charts_Data_M11.O4()
        var_1 = IFERROR(o4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class M8():
    # 'Charts_M11_EEPS'!M8
    value = None
    formula = '''=IFERROR('Charts Data M11'!P4,"")'''
    @eval_fn
    def M8():
        p4_1 = Charts_Data_M11.P4()
        var_1 = IFERROR(p4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class N8():
    # 'Charts_M11_EEPS'!N8
    value = None
    formula = '''=IFERROR('Charts Data M11'!Q4,"")'''
    @eval_fn
    def N8():
        q4_1 = Charts_Data_M11.Q4()
        var_1 = IFERROR(q4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class O8():
    # 'Charts_M11_EEPS'!O8
    value = None
    formula = '''=IFERROR('Charts Data M11'!R4,"")'''
    @eval_fn
    def O8():
        r4_1 = Charts_Data_M11.R4()
        var_1 = IFERROR(r4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class P8():
    # 'Charts_M11_EEPS'!P8
    value = None
    formula = '''=IFERROR('Charts Data M11'!S4,"")'''
    @eval_fn
    def P8():
        s4_1 = Charts_Data_M11.S4()
        var_1 = IFERROR(s4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class Q8():
    # 'Charts_M11_EEPS'!Q8
    value = None
    formula = '''=IFERROR('Charts Data M11'!T4,"")'''
    @eval_fn
    def Q8():
        t4_1 = Charts_Data_M11.T4()
        var_1 = IFERROR(t4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class R8():
    # 'Charts_M11_EEPS'!R8
    value = None
    formula = '''=IFERROR('Charts Data M11'!U4,"")'''
    @eval_fn
    def R8():
        u4_1 = Charts_Data_M11.U4()
        var_1 = IFERROR(u4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class S8():
    # 'Charts_M11_EEPS'!S8
    value = None
    formula = '''=IFERROR('Charts Data M11'!V4,"")'''
    @eval_fn
    def S8():
        v4_1 = Charts_Data_M11.V4()
        var_1 = IFERROR(v4_1, "")
        return var_1

@register(Charts_M11_EEPS)
class B9():
    # 'Charts_M11_EEPS'!B9
    value = "HELCO"
    formula = "='Charts Data M10'!D6"
    @eval_fn
    def B9():
        d6_1 = Charts_Data_M10.D6()
        return d6_1

@register(Charts_M11_EEPS)
class D9():
    # 'Charts_M11_EEPS'!D9
    value = None
    formula = '''=IFERROR('Charts Data M11'!G5,"")'''
    @eval_fn
    def D9():
        g5_1 = Charts_Data_M11.G5()
        var_1 = IFERROR(g5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class E9():
    # 'Charts_M11_EEPS'!E9
    value = None
    formula = '''=IFERROR('Charts Data M11'!H5,"")'''
    @eval_fn
    def E9():
        h5_1 = Charts_Data_M11.H5()
        var_1 = IFERROR(h5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class F9():
    # 'Charts_M11_EEPS'!F9
    value = None
    formula = '''=IFERROR('Charts Data M11'!I5,"")'''
    @eval_fn
    def F9():
        i5_1 = Charts_Data_M11.I5()
        var_1 = IFERROR(i5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class G9():
    # 'Charts_M11_EEPS'!G9
    value = None
    formula = '''=IFERROR('Charts Data M11'!J5,"")'''
    @eval_fn
    def G9():
        j5_1 = Charts_Data_M11.J5()
        var_1 = IFERROR(j5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class H9():
    # 'Charts_M11_EEPS'!H9
    value = None
    formula = '''=IFERROR('Charts Data M11'!K5,"")'''
    @eval_fn
    def H9():
        k5_1 = Charts_Data_M11.K5()
        var_1 = IFERROR(k5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class I9():
    # 'Charts_M11_EEPS'!I9
    value = None
    formula = '''=IFERROR('Charts Data M11'!L5,"")'''
    @eval_fn
    def I9():
        l5_1 = Charts_Data_M11.L5()
        var_1 = IFERROR(l5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class J9():
    # 'Charts_M11_EEPS'!J9
    value = None
    formula = '''=IFERROR('Charts Data M11'!M5,"")'''
    @eval_fn
    def J9():
        m5_1 = Charts_Data_M11.M5()
        var_1 = IFERROR(m5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class K9():
    # 'Charts_M11_EEPS'!K9
    value = None
    formula = '''=IFERROR('Charts Data M11'!N5,"")'''
    @eval_fn
    def K9():
        n5_1 = Charts_Data_M11.N5()
        var_1 = IFERROR(n5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class L9():
    # 'Charts_M11_EEPS'!L9
    value = None
    formula = '''=IFERROR('Charts Data M11'!O5,"")'''
    @eval_fn
    def L9():
        o5_1 = Charts_Data_M11.O5()
        var_1 = IFERROR(o5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class M9():
    # 'Charts_M11_EEPS'!M9
    value = None
    formula = '''=IFERROR('Charts Data M11'!P5,"")'''
    @eval_fn
    def M9():
        p5_1 = Charts_Data_M11.P5()
        var_1 = IFERROR(p5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class N9():
    # 'Charts_M11_EEPS'!N9
    value = None
    formula = '''=IFERROR('Charts Data M11'!Q5,"")'''
    @eval_fn
    def N9():
        q5_1 = Charts_Data_M11.Q5()
        var_1 = IFERROR(q5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class O9():
    # 'Charts_M11_EEPS'!O9
    value = None
    formula = '''=IFERROR('Charts Data M11'!R5,"")'''
    @eval_fn
    def O9():
        r5_1 = Charts_Data_M11.R5()
        var_1 = IFERROR(r5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class P9():
    # 'Charts_M11_EEPS'!P9
    value = None
    formula = '''=IFERROR('Charts Data M11'!S5,"")'''
    @eval_fn
    def P9():
        s5_1 = Charts_Data_M11.S5()
        var_1 = IFERROR(s5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class Q9():
    # 'Charts_M11_EEPS'!Q9
    value = None
    formula = '''=IFERROR('Charts Data M11'!T5,"")'''
    @eval_fn
    def Q9():
        t5_1 = Charts_Data_M11.T5()
        var_1 = IFERROR(t5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class R9():
    # 'Charts_M11_EEPS'!R9
    value = None
    formula = '''=IFERROR('Charts Data M11'!U5,"")'''
    @eval_fn
    def R9():
        u5_1 = Charts_Data_M11.U5()
        var_1 = IFERROR(u5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class S9():
    # 'Charts_M11_EEPS'!S9
    value = None
    formula = '''=IFERROR('Charts Data M11'!V5,"")'''
    @eval_fn
    def S9():
        v5_1 = Charts_Data_M11.V5()
        var_1 = IFERROR(v5_1, "")
        return var_1

@register(Charts_M11_EEPS)
class B10():
    # 'Charts_M11_EEPS'!B10
    value = "MECO"
    formula = "='Charts Data M10'!D7"
    @eval_fn
    def B10():
        d7_1 = Charts_Data_M10.D7()
        return d7_1

@register(Charts_M11_EEPS)
class D10():
    # 'Charts_M11_EEPS'!D10
    value = None
    formula = '''=IFERROR('Charts Data M11'!G6,"")'''
    @eval_fn
    def D10():
        g6_1 = Charts_Data_M11.G6()
        var_1 = IFERROR(g6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class E10():
    # 'Charts_M11_EEPS'!E10
    value = None
    formula = '''=IFERROR('Charts Data M11'!H6,"")'''
    @eval_fn
    def E10():
        h6_1 = Charts_Data_M11.H6()
        var_1 = IFERROR(h6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class F10():
    # 'Charts_M11_EEPS'!F10
    value = None
    formula = '''=IFERROR('Charts Data M11'!I6,"")'''
    @eval_fn
    def F10():
        i6_1 = Charts_Data_M11.I6()
        var_1 = IFERROR(i6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class G10():
    # 'Charts_M11_EEPS'!G10
    value = None
    formula = '''=IFERROR('Charts Data M11'!J6,"")'''
    @eval_fn
    def G10():
        j6_1 = Charts_Data_M11.J6()
        var_1 = IFERROR(j6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class H10():
    # 'Charts_M11_EEPS'!H10
    value = None
    formula = '''=IFERROR('Charts Data M11'!K6,"")'''
    @eval_fn
    def H10():
        k6_1 = Charts_Data_M11.K6()
        var_1 = IFERROR(k6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class I10():
    # 'Charts_M11_EEPS'!I10
    value = None
    formula = '''=IFERROR('Charts Data M11'!L6,"")'''
    @eval_fn
    def I10():
        l6_1 = Charts_Data_M11.L6()
        var_1 = IFERROR(l6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class J10():
    # 'Charts_M11_EEPS'!J10
    value = None
    formula = '''=IFERROR('Charts Data M11'!M6,"")'''
    @eval_fn
    def J10():
        m6_1 = Charts_Data_M11.M6()
        var_1 = IFERROR(m6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class K10():
    # 'Charts_M11_EEPS'!K10
    value = None
    formula = '''=IFERROR('Charts Data M11'!N6,"")'''
    @eval_fn
    def K10():
        n6_1 = Charts_Data_M11.N6()
        var_1 = IFERROR(n6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class L10():
    # 'Charts_M11_EEPS'!L10
    value = None
    formula = '''=IFERROR('Charts Data M11'!O6,"")'''
    @eval_fn
    def L10():
        o6_1 = Charts_Data_M11.O6()
        var_1 = IFERROR(o6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class M10():
    # 'Charts_M11_EEPS'!M10
    value = None
    formula = '''=IFERROR('Charts Data M11'!P6,"")'''
    @eval_fn
    def M10():
        p6_1 = Charts_Data_M11.P6()
        var_1 = IFERROR(p6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class N10():
    # 'Charts_M11_EEPS'!N10
    value = None
    formula = '''=IFERROR('Charts Data M11'!Q6,"")'''
    @eval_fn
    def N10():
        q6_1 = Charts_Data_M11.Q6()
        var_1 = IFERROR(q6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class O10():
    # 'Charts_M11_EEPS'!O10
    value = None
    formula = '''=IFERROR('Charts Data M11'!R6,"")'''
    @eval_fn
    def O10():
        r6_1 = Charts_Data_M11.R6()
        var_1 = IFERROR(r6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class P10():
    # 'Charts_M11_EEPS'!P10
    value = None
    formula = '''=IFERROR('Charts Data M11'!S6,"")'''
    @eval_fn
    def P10():
        s6_1 = Charts_Data_M11.S6()
        var_1 = IFERROR(s6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class Q10():
    # 'Charts_M11_EEPS'!Q10
    value = None
    formula = '''=IFERROR('Charts Data M11'!T6,"")'''
    @eval_fn
    def Q10():
        t6_1 = Charts_Data_M11.T6()
        var_1 = IFERROR(t6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class R10():
    # 'Charts_M11_EEPS'!R10
    value = None
    formula = '''=IFERROR('Charts Data M11'!U6,"")'''
    @eval_fn
    def R10():
        u6_1 = Charts_Data_M11.U6()
        var_1 = IFERROR(u6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class S10():
    # 'Charts_M11_EEPS'!S10
    value = None
    formula = '''=IFERROR('Charts Data M11'!V6,"")'''
    @eval_fn
    def S10():
        v6_1 = Charts_Data_M11.V6()
        var_1 = IFERROR(v6_1, "")
        return var_1

@register(Charts_M11_EEPS)
class B11():
    # 'Charts_M11_EEPS'!B11
    value = "KIUC"
    formula = "='Charts Data M10'!D8"
    @eval_fn
    def B11():
        d8_1 = Charts_Data_M10.D8()
        return d8_1

@register(Charts_M11_EEPS)
class D11():
    # 'Charts_M11_EEPS'!D11
    value = None
    formula = '''=IFERROR('Charts Data M11'!G7,"")'''
    @eval_fn
    def D11():
        g7_1 = Charts_Data_M11.G7()
        var_1 = IFERROR(g7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class E11():
    # 'Charts_M11_EEPS'!E11
    value = None
    formula = '''=IFERROR('Charts Data M11'!H7,"")'''
    @eval_fn
    def E11():
        h7_1 = Charts_Data_M11.H7()
        var_1 = IFERROR(h7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class F11():
    # 'Charts_M11_EEPS'!F11
    value = None
    formula = '''=IFERROR('Charts Data M11'!I7,"")'''
    @eval_fn
    def F11():
        i7_1 = Charts_Data_M11.I7()
        var_1 = IFERROR(i7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class G11():
    # 'Charts_M11_EEPS'!G11
    value = None
    formula = '''=IFERROR('Charts Data M11'!J7,"")'''
    @eval_fn
    def G11():
        j7_1 = Charts_Data_M11.J7()
        var_1 = IFERROR(j7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class H11():
    # 'Charts_M11_EEPS'!H11
    value = None
    formula = '''=IFERROR('Charts Data M11'!K7,"")'''
    @eval_fn
    def H11():
        k7_1 = Charts_Data_M11.K7()
        var_1 = IFERROR(k7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class I11():
    # 'Charts_M11_EEPS'!I11
    value = None
    formula = '''=IFERROR('Charts Data M11'!L7,"")'''
    @eval_fn
    def I11():
        l7_1 = Charts_Data_M11.L7()
        var_1 = IFERROR(l7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class J11():
    # 'Charts_M11_EEPS'!J11
    value = None
    formula = '''=IFERROR('Charts Data M11'!M7,"")'''
    @eval_fn
    def J11():
        m7_1 = Charts_Data_M11.M7()
        var_1 = IFERROR(m7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class K11():
    # 'Charts_M11_EEPS'!K11
    value = None
    formula = '''=IFERROR('Charts Data M11'!N7,"")'''
    @eval_fn
    def K11():
        n7_1 = Charts_Data_M11.N7()
        var_1 = IFERROR(n7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class L11():
    # 'Charts_M11_EEPS'!L11
    value = None
    formula = '''=IFERROR('Charts Data M11'!O7,"")'''
    @eval_fn
    def L11():
        o7_1 = Charts_Data_M11.O7()
        var_1 = IFERROR(o7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class M11():
    # 'Charts_M11_EEPS'!M11
    value = None
    formula = '''=IFERROR('Charts Data M11'!P7,"")'''
    @eval_fn
    def M11():
        p7_1 = Charts_Data_M11.P7()
        var_1 = IFERROR(p7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class N11():
    # 'Charts_M11_EEPS'!N11
    value = None
    formula = '''=IFERROR('Charts Data M11'!Q7,"")'''
    @eval_fn
    def N11():
        q7_1 = Charts_Data_M11.Q7()
        var_1 = IFERROR(q7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class O11():
    # 'Charts_M11_EEPS'!O11
    value = None
    formula = '''=IFERROR('Charts Data M11'!R7,"")'''
    @eval_fn
    def O11():
        r7_1 = Charts_Data_M11.R7()
        var_1 = IFERROR(r7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class P11():
    # 'Charts_M11_EEPS'!P11
    value = None
    formula = '''=IFERROR('Charts Data M11'!S7,"")'''
    @eval_fn
    def P11():
        s7_1 = Charts_Data_M11.S7()
        var_1 = IFERROR(s7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class Q11():
    # 'Charts_M11_EEPS'!Q11
    value = None
    formula = '''=IFERROR('Charts Data M11'!T7,"")'''
    @eval_fn
    def Q11():
        t7_1 = Charts_Data_M11.T7()
        var_1 = IFERROR(t7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class R11():
    # 'Charts_M11_EEPS'!R11
    value = None
    formula = '''=IFERROR('Charts Data M11'!U7,"")'''
    @eval_fn
    def R11():
        u7_1 = Charts_Data_M11.U7()
        var_1 = IFERROR(u7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class S11():
    # 'Charts_M11_EEPS'!S11
    value = None
    formula = '''=IFERROR('Charts Data M11'!V7,"")'''
    @eval_fn
    def S11():
        v7_1 = Charts_Data_M11.V7()
        var_1 = IFERROR(v7_1, "")
        return var_1

@register(Charts_M11_EEPS)
class B12():
    # 'Charts_M11_EEPS'!B12
    value = "Total"

@register(Charts_M11_EEPS)
class D12():
    # 'Charts_M11_EEPS'!D12
    value = None
    formula = '''=IFERROR('Charts Data M11'!G8,"")'''
    @eval_fn
    def D12():
        g8_1 = Charts_Data_M11.G8()
        var_1 = IFERROR(g8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class E12():
    # 'Charts_M11_EEPS'!E12
    value = None
    formula = '''=IFERROR('Charts Data M11'!H8,"")'''
    @eval_fn
    def E12():
        h8_1 = Charts_Data_M11.H8()
        var_1 = IFERROR(h8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class F12():
    # 'Charts_M11_EEPS'!F12
    value = None
    formula = '''=IFERROR('Charts Data M11'!I8,"")'''
    @eval_fn
    def F12():
        i8_1 = Charts_Data_M11.I8()
        var_1 = IFERROR(i8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class G12():
    # 'Charts_M11_EEPS'!G12
    value = None
    formula = '''=IFERROR('Charts Data M11'!J8,"")'''
    @eval_fn
    def G12():
        j8_1 = Charts_Data_M11.J8()
        var_1 = IFERROR(j8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class H12():
    # 'Charts_M11_EEPS'!H12
    value = None
    formula = '''=IFERROR('Charts Data M11'!K8,"")'''
    @eval_fn
    def H12():
        k8_1 = Charts_Data_M11.K8()
        var_1 = IFERROR(k8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class I12():
    # 'Charts_M11_EEPS'!I12
    value = None
    formula = '''=IFERROR('Charts Data M11'!L8,"")'''
    @eval_fn
    def I12():
        l8_1 = Charts_Data_M11.L8()
        var_1 = IFERROR(l8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class J12():
    # 'Charts_M11_EEPS'!J12
    value = None
    formula = '''=IFERROR('Charts Data M11'!M8,"")'''
    @eval_fn
    def J12():
        m8_1 = Charts_Data_M11.M8()
        var_1 = IFERROR(m8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class K12():
    # 'Charts_M11_EEPS'!K12
    value = None
    formula = '''=IFERROR('Charts Data M11'!N8,"")'''
    @eval_fn
    def K12():
        n8_1 = Charts_Data_M11.N8()
        var_1 = IFERROR(n8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class L12():
    # 'Charts_M11_EEPS'!L12
    value = None
    formula = '''=IFERROR('Charts Data M11'!O8,"")'''
    @eval_fn
    def L12():
        o8_1 = Charts_Data_M11.O8()
        var_1 = IFERROR(o8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class M12():
    # 'Charts_M11_EEPS'!M12
    value = None
    formula = '''=IFERROR('Charts Data M11'!P8,"")'''
    @eval_fn
    def M12():
        p8_1 = Charts_Data_M11.P8()
        var_1 = IFERROR(p8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class N12():
    # 'Charts_M11_EEPS'!N12
    value = None
    formula = '''=IFERROR('Charts Data M11'!Q8,"")'''
    @eval_fn
    def N12():
        q8_1 = Charts_Data_M11.Q8()
        var_1 = IFERROR(q8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class O12():
    # 'Charts_M11_EEPS'!O12
    value = None
    formula = '''=IFERROR('Charts Data M11'!R8,"")'''
    @eval_fn
    def O12():
        r8_1 = Charts_Data_M11.R8()
        var_1 = IFERROR(r8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class P12():
    # 'Charts_M11_EEPS'!P12
    value = None
    formula = '''=IFERROR('Charts Data M11'!S8,"")'''
    @eval_fn
    def P12():
        s8_1 = Charts_Data_M11.S8()
        var_1 = IFERROR(s8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class Q12():
    # 'Charts_M11_EEPS'!Q12
    value = None
    formula = '''=IFERROR('Charts Data M11'!T8,"")'''
    @eval_fn
    def Q12():
        t8_1 = Charts_Data_M11.T8()
        var_1 = IFERROR(t8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class R12():
    # 'Charts_M11_EEPS'!R12
    value = None
    formula = '''=IFERROR('Charts Data M11'!U8,"")'''
    @eval_fn
    def R12():
        u8_1 = Charts_Data_M11.U8()
        var_1 = IFERROR(u8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class S12():
    # 'Charts_M11_EEPS'!S12
    value = None
    formula = '''=IFERROR('Charts Data M11'!V8,"")'''
    @eval_fn
    def S12():
        v8_1 = Charts_Data_M11.V8()
        var_1 = IFERROR(v8_1, "")
        return var_1

@register(Charts_M11_EEPS)
class B14():
    # 'Charts_M11_EEPS'!B14
    value = "Electricity Saved as Percent of Percent of 4,300 GWh"
    formula = "='Charts Data M11'!$B$2"
    @eval_fn
    def B14():
        b2_1 = Charts_Data_M11.B2()
        return b2_1

@register(Charts_M11_EEPS)
class Q14():
    # 'Charts_M11_EEPS'!Q14
    value = "Note: Contributing data, cell formulae, and goals are all subject to amendment basded on the Public Utility Commission's goals to be submitted in January 2014"

@register(Charts_M11_EEPS)
class B23():
    # 'Charts_M11_EEPS'!B23
    value = 13

@register(Charts_M11_EEPS)
class B25():
    # 'Charts_M11_EEPS'!B25
    value = "Electricity Saved in 2011"
    formula = "='Charts Data M11'!$B$3"
    @eval_fn
    def B25():
        b3_1 = Charts_Data_M11.B3()
        return b3_1