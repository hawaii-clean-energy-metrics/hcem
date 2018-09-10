# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M10_RPS = Worksheet('Charts_M10_RPS', 10, 10)



@register(Charts_M10_RPS)
class B2():
    # 'Charts_M10_RPS'!B2
    value = 5

@register(Charts_M10_RPS)
class D2():
    # 'Charts_M10_RPS'!D2
    value = "       Metric 10: Percentage attainment of the Renewable Portfolio Standard (RPS)"

@register(Charts_M10_RPS)
class R2():
    # 'Charts_M10_RPS'!R2
    value = "NOTE: Distrubted PV included as rnewable, not displaced energy/EE"

@register(Charts_M10_RPS)
class D5():
    # 'Charts_M10_RPS'!D5
    value = 1999
    formula = "='Dashboard M10 RPS'!G5"
    @eval_fn
    def D5():
        g5_1 = Dashboard_M10_RPS.G5()
        return g5_1

@register(Charts_M10_RPS)
class E5():
    # 'Charts_M10_RPS'!E5
    value = 2000
    formula = "='Dashboard M10 RPS'!H5"
    @eval_fn
    def E5():
        h5_1 = Dashboard_M10_RPS.H5()
        return h5_1

@register(Charts_M10_RPS)
class F5():
    # 'Charts_M10_RPS'!F5
    value = 2001
    formula = "='Dashboard M10 RPS'!I5"
    @eval_fn
    def F5():
        i5_1 = Dashboard_M10_RPS.I5()
        return i5_1

@register(Charts_M10_RPS)
class G5():
    # 'Charts_M10_RPS'!G5
    value = 2002
    formula = "='Dashboard M10 RPS'!J5"
    @eval_fn
    def G5():
        j5_1 = Dashboard_M10_RPS.J5()
        return j5_1

@register(Charts_M10_RPS)
class H5():
    # 'Charts_M10_RPS'!H5
    value = 2003
    formula = "='Dashboard M10 RPS'!K5"
    @eval_fn
    def H5():
        k5_1 = Dashboard_M10_RPS.K5()
        return k5_1

@register(Charts_M10_RPS)
class I5():
    # 'Charts_M10_RPS'!I5
    value = 2004
    formula = "='Dashboard M10 RPS'!L5"
    @eval_fn
    def I5():
        l5_1 = Dashboard_M10_RPS.L5()
        return l5_1

@register(Charts_M10_RPS)
class J5():
    # 'Charts_M10_RPS'!J5
    value = 2005
    formula = "='Dashboard M10 RPS'!M5"
    @eval_fn
    def J5():
        m5_1 = Dashboard_M10_RPS.M5()
        return m5_1

@register(Charts_M10_RPS)
class K5():
    # 'Charts_M10_RPS'!K5
    value = 2006
    formula = "='Dashboard M10 RPS'!N5"
    @eval_fn
    def K5():
        n5_1 = Dashboard_M10_RPS.N5()
        return n5_1

@register(Charts_M10_RPS)
class L5():
    # 'Charts_M10_RPS'!L5
    value = 2007
    formula = "='Dashboard M10 RPS'!O5"
    @eval_fn
    def L5():
        o5_1 = Dashboard_M10_RPS.O5()
        return o5_1

@register(Charts_M10_RPS)
class M5():
    # 'Charts_M10_RPS'!M5
    value = 2008
    formula = "='Dashboard M10 RPS'!P5"
    @eval_fn
    def M5():
        p5_1 = Dashboard_M10_RPS.P5()
        return p5_1

@register(Charts_M10_RPS)
class N5():
    # 'Charts_M10_RPS'!N5
    value = 2009
    formula = "='Dashboard M10 RPS'!Q5"
    @eval_fn
    def N5():
        q5_1 = Dashboard_M10_RPS.Q5()
        return q5_1

@register(Charts_M10_RPS)
class O5():
    # 'Charts_M10_RPS'!O5
    value = 2010
    formula = "='Dashboard M10 RPS'!R5"
    @eval_fn
    def O5():
        r5_1 = Dashboard_M10_RPS.R5()
        return r5_1

@register(Charts_M10_RPS)
class P5():
    # 'Charts_M10_RPS'!P5
    value = 2011
    formula = "='Dashboard M10 RPS'!S5"
    @eval_fn
    def P5():
        s5_1 = Dashboard_M10_RPS.S5()
        return s5_1

@register(Charts_M10_RPS)
class Q5():
    # 'Charts_M10_RPS'!Q5
    value = 2012
    formula = "='Dashboard M10 RPS'!T5"
    @eval_fn
    def Q5():
        t5_1 = Dashboard_M10_RPS.T5()
        return t5_1

@register(Charts_M10_RPS)
class R5():
    # 'Charts_M10_RPS'!R5
    value = 2013
    formula = "='Dashboard M10 RPS'!U5"
    @eval_fn
    def R5():
        u5_1 = Dashboard_M10_RPS.U5()
        return u5_1

@register(Charts_M10_RPS)
class S5():
    # 'Charts_M10_RPS'!S5
    value = 2014
    formula = "='Dashboard M10 RPS'!V5"
    @eval_fn
    def S5():
        v5_1 = Dashboard_M10_RPS.V5()
        return v5_1

@register(Charts_M10_RPS)
class B6():
    # 'Charts_M10_RPS'!B6
    value = "HECO"
    formula = "='Charts Data M10'!D5"
    @eval_fn
    def B6():
        d5_1 = Charts_Data_M10.D5()
        return d5_1

@register(Charts_M10_RPS)
class D6():
    # 'Charts_M10_RPS'!D6
    value = 0.0908535230051
    formula = "='Charts Data M10'!G5"
    @eval_fn
    def D6():
        g5_1 = Charts_Data_M10.G5()
        return g5_1

@register(Charts_M10_RPS)
class E6():
    # 'Charts_M10_RPS'!E6
    value = 0.112659456461
    formula = "='Charts Data M10'!H5"
    @eval_fn
    def E6():
        h5_1 = Charts_Data_M10.H5()
        return h5_1

@register(Charts_M10_RPS)
class F6():
    # 'Charts_M10_RPS'!F6
    value = 0.104095094132
    formula = "='Charts Data M10'!I5"
    @eval_fn
    def F6():
        i5_1 = Charts_Data_M10.I5()
        return i5_1

@register(Charts_M10_RPS)
class G6():
    # 'Charts_M10_RPS'!G6
    value = 0.110622462788
    formula = "='Charts Data M10'!J5"
    @eval_fn
    def G6():
        j5_1 = Charts_Data_M10.J5()
        return j5_1

@register(Charts_M10_RPS)
class H6():
    # 'Charts_M10_RPS'!H6
    value = 0.122374368519
    formula = "='Charts Data M10'!K5"
    @eval_fn
    def H6():
        k5_1 = Charts_Data_M10.K5()
        return k5_1

@register(Charts_M10_RPS)
class I6():
    # 'Charts_M10_RPS'!I6
    value = 0.119423251002
    formula = "='Charts Data M10'!L5"
    @eval_fn
    def I6():
        l5_1 = Charts_Data_M10.L5()
        return l5_1

@register(Charts_M10_RPS)
class J6():
    # 'Charts_M10_RPS'!J6
    value = 0.10795233778
    formula = "='Charts Data M10'!M5"
    @eval_fn
    def J6():
        m5_1 = Charts_Data_M10.M5()
        return m5_1

@register(Charts_M10_RPS)
class K6():
    # 'Charts_M10_RPS'!K6
    value = 0.128392416569
    formula = "='Charts Data M10'!N5"
    @eval_fn
    def K6():
        n5_1 = Charts_Data_M10.N5()
        return n5_1

@register(Charts_M10_RPS)
class L6():
    # 'Charts_M10_RPS'!L6
    value = 0.10674267101
    formula = "='Charts Data M10'!O5"
    @eval_fn
    def L6():
        o5_1 = Charts_Data_M10.O5()
        return o5_1

@register(Charts_M10_RPS)
class M6():
    # 'Charts_M10_RPS'!M6
    value = 0.120108465342
    formula = "='Charts Data M10'!P5"
    @eval_fn
    def M6():
        p5_1 = Charts_Data_M10.P5()
        return p5_1

@register(Charts_M10_RPS)
class N6():
    # 'Charts_M10_RPS'!N6
    value = 0.128531378426
    formula = "='Charts Data M10'!Q5"
    @eval_fn
    def N6():
        q5_1 = Charts_Data_M10.Q5()
        return q5_1

@register(Charts_M10_RPS)
class O6():
    # 'Charts_M10_RPS'!O6
    value = 0.118454771727
    formula = "='Charts Data M10'!R5"
    @eval_fn
    def O6():
        r5_1 = Charts_Data_M10.R5()
        return r5_1

@register(Charts_M10_RPS)
class P6():
    # 'Charts_M10_RPS'!P6
    value = 0.167358872051
    formula = "='Charts Data M10'!S5"
    @eval_fn
    def P6():
        s5_1 = Charts_Data_M10.S5()
        return s5_1

@register(Charts_M10_RPS)
class Q6():
    # 'Charts_M10_RPS'!Q6
    value = 0.19024272663
    formula = "='Charts Data M10'!T5"
    @eval_fn
    def Q6():
        t5_1 = Charts_Data_M10.T5()
        return t5_1

@register(Charts_M10_RPS)
class R6():
    # 'Charts_M10_RPS'!R6
    value = 0.29197521162
    formula = "='Charts Data M10'!U5"
    @eval_fn
    def R6():
        u5_1 = Charts_Data_M10.U5()
        return u5_1

@register(Charts_M10_RPS)
class S6():
    # 'Charts_M10_RPS'!S6
    value = 0.379357429186
    formula = "='Charts Data M10'!V5"
    @eval_fn
    def S6():
        v5_1 = Charts_Data_M10.V5()
        return v5_1

@register(Charts_M10_RPS)
class B7():
    # 'Charts_M10_RPS'!B7
    value = "HELCO"
    formula = "='Charts Data M10'!D6"
    @eval_fn
    def B7():
        d6_1 = Charts_Data_M10.D6()
        return d6_1

@register(Charts_M10_RPS)
class D7():
    # 'Charts_M10_RPS'!D7
    value = 0.704989154013
    formula = "='Charts Data M10'!G6"
    @eval_fn
    def D7():
        g6_1 = Charts_Data_M10.G6()
        return g6_1

@register(Charts_M10_RPS)
class E7():
    # 'Charts_M10_RPS'!E7
    value = 0.81498951782
    formula = "='Charts Data M10'!H6"
    @eval_fn
    def E7():
        h6_1 = Charts_Data_M10.H6()
        return h6_1

@register(Charts_M10_RPS)
class F7():
    # 'Charts_M10_RPS'!F7
    value = 0.714285714286
    formula = "='Charts Data M10'!I6"
    @eval_fn
    def F7():
        i6_1 = Charts_Data_M10.I6()
        return i6_1

@register(Charts_M10_RPS)
class G7():
    # 'Charts_M10_RPS'!G7
    value = 0.309045226131
    formula = "='Charts Data M10'!J6"
    @eval_fn
    def G7():
        j6_1 = Charts_Data_M10.J6()
        return j6_1

@register(Charts_M10_RPS)
class H7():
    # 'Charts_M10_RPS'!H7
    value = 0.517208413002
    formula = "='Charts Data M10'!K6"
    @eval_fn
    def H7():
        k6_1 = Charts_Data_M10.K6()
        return k6_1

@register(Charts_M10_RPS)
class I7():
    # 'Charts_M10_RPS'!I7
    value = 0.592105263158
    formula = "='Charts Data M10'!L6"
    @eval_fn
    def I7():
        l6_1 = Charts_Data_M10.L6()
        return l6_1

@register(Charts_M10_RPS)
class J7():
    # 'Charts_M10_RPS'!J7
    value = 0.603401969561
    formula = "='Charts Data M10'!M6"
    @eval_fn
    def J7():
        m6_1 = Charts_Data_M10.M6()
        return m6_1

@register(Charts_M10_RPS)
class K7():
    # 'Charts_M10_RPS'!K7
    value = 0.642297650131
    formula = "='Charts Data M10'!N6"
    @eval_fn
    def K7():
        n6_1 = Charts_Data_M10.N6()
        return n6_1

@register(Charts_M10_RPS)
class L7():
    # 'Charts_M10_RPS'!L7
    value = 0.845012897678
    formula = "='Charts Data M10'!O6"
    @eval_fn
    def L7():
        o6_1 = Charts_Data_M10.O6()
        return o6_1

@register(Charts_M10_RPS)
class M7():
    # 'Charts_M10_RPS'!M7
    value = 0.884038982323
    formula = "='Charts Data M10'!P6"
    @eval_fn
    def M7():
        p6_1 = Charts_Data_M10.P6()
        return p6_1

@register(Charts_M10_RPS)
class N7():
    # 'Charts_M10_RPS'!N7
    value = 0.843236915351
    formula = "='Charts Data M10'!Q6"
    @eval_fn
    def N7():
        q6_1 = Charts_Data_M10.Q6()
        return q6_1

@register(Charts_M10_RPS)
class O7():
    # 'Charts_M10_RPS'!O7
    value = 0.864182457291
    formula = "='Charts Data M10'!R6"
    @eval_fn
    def O7():
        r6_1 = Charts_Data_M10.R6()
        return r6_1

@register(Charts_M10_RPS)
class P7():
    # 'Charts_M10_RPS'!P7
    value = 1.02700367534
    formula = "='Charts Data M10'!S6"
    @eval_fn
    def P7():
        s6_1 = Charts_Data_M10.S6()
        return s6_1

@register(Charts_M10_RPS)
class Q7():
    # 'Charts_M10_RPS'!Q7
    value = 1.16816151556
    formula = "='Charts Data M10'!T6"
    @eval_fn
    def Q7():
        t6_1 = Charts_Data_M10.T6()
        return t6_1

@register(Charts_M10_RPS)
class R7():
    # 'Charts_M10_RPS'!R7
    value = 1.20196328608
    formula = "='Charts Data M10'!U6"
    @eval_fn
    def R7():
        u6_1 = Charts_Data_M10.U6()
        return u6_1

@register(Charts_M10_RPS)
class S7():
    # 'Charts_M10_RPS'!S7
    value = 1.18383542537
    formula = "='Charts Data M10'!V6"
    @eval_fn
    def S7():
        v6_1 = Charts_Data_M10.V6()
        return v6_1

@register(Charts_M10_RPS)
class B8():
    # 'Charts_M10_RPS'!B8
    value = "MECO"
    formula = "='Charts Data M10'!D7"
    @eval_fn
    def B8():
        d7_1 = Charts_Data_M10.D7()
        return d7_1

@register(Charts_M10_RPS)
class D8():
    # 'Charts_M10_RPS'!D8
    value = 0.129107981221
    formula = "='Charts Data M10'!G7"
    @eval_fn
    def D8():
        g7_1 = Charts_Data_M10.G7()
        return g7_1

@register(Charts_M10_RPS)
class E8():
    # 'Charts_M10_RPS'!E8
    value = 0.101717902351
    formula = "='Charts Data M10'!H7"
    @eval_fn
    def E8():
        h7_1 = Charts_Data_M10.H7()
        return h7_1

@register(Charts_M10_RPS)
class F8():
    # 'Charts_M10_RPS'!F8
    value = 0.0837742504409
    formula = "='Charts Data M10'!I7"
    @eval_fn
    def F8():
        i7_1 = Charts_Data_M10.I7()
        return i7_1

@register(Charts_M10_RPS)
class G8():
    # 'Charts_M10_RPS'!G8
    value = 0.148835202761
    formula = "='Charts Data M10'!J7"
    @eval_fn
    def G8():
        j7_1 = Charts_Data_M10.J7()
        return j7_1

@register(Charts_M10_RPS)
class H8():
    # 'Charts_M10_RPS'!H8
    value = 0.136702568351
    formula = "='Charts Data M10'!K7"
    @eval_fn
    def H8():
        k7_1 = Charts_Data_M10.K7()
        return k7_1

@register(Charts_M10_RPS)
class I8():
    # 'Charts_M10_RPS'!I8
    value = 0.14875701684
    formula = "='Charts Data M10'!L7"
    @eval_fn
    def I8():
        l7_1 = Charts_Data_M10.L7()
        return l7_1

@register(Charts_M10_RPS)
class J8():
    # 'Charts_M10_RPS'!J8
    value = 0.150559105431
    formula = "='Charts Data M10'!M7"
    @eval_fn
    def J8():
        m7_1 = Charts_Data_M10.M7()
        return m7_1

@register(Charts_M10_RPS)
class K8():
    # 'Charts_M10_RPS'!K8
    value = 0.270339652449
    formula = "='Charts Data M10'!N7"
    @eval_fn
    def K8():
        n7_1 = Charts_Data_M10.N7()
        return n7_1

@register(Charts_M10_RPS)
class L8():
    # 'Charts_M10_RPS'!L8
    value = 0.3861328125
    formula = "='Charts Data M10'!O7"
    @eval_fn
    def L8():
        o7_1 = Charts_Data_M10.O7()
        return o7_1

@register(Charts_M10_RPS)
class M8():
    # 'Charts_M10_RPS'!M8
    value = 0.346846988609
    formula = "='Charts Data M10'!P7"
    @eval_fn
    def M8():
        p7_1 = Charts_Data_M10.P7()
        return p7_1

@register(Charts_M10_RPS)
class N8():
    # 'Charts_M10_RPS'!N8
    value = 0.347737415946
    formula = "='Charts Data M10'!Q7"
    @eval_fn
    def N8():
        q7_1 = Charts_Data_M10.Q7()
        return q7_1

@register(Charts_M10_RPS)
class O8():
    # 'Charts_M10_RPS'!O8
    value = 0.383027613404
    formula = "='Charts Data M10'!R7"
    @eval_fn
    def O8():
        r7_1 = Charts_Data_M10.R7()
        return r7_1

@register(Charts_M10_RPS)
class P8():
    # 'Charts_M10_RPS'!P8
    value = 0.428165849016
    formula = "='Charts Data M10'!S7"
    @eval_fn
    def P8():
        s7_1 = Charts_Data_M10.S7()
        return s7_1

@register(Charts_M10_RPS)
class Q8():
    # 'Charts_M10_RPS'!Q8
    value = 0.520423520656
    formula = "='Charts Data M10'!T7"
    @eval_fn
    def Q8():
        t7_1 = Charts_Data_M10.T7()
        return t7_1

@register(Charts_M10_RPS)
class R8():
    # 'Charts_M10_RPS'!R8
    value = 0.727101182247
    formula = "='Charts Data M10'!U7"
    @eval_fn
    def R8():
        u7_1 = Charts_Data_M10.U7()
        return u7_1

@register(Charts_M10_RPS)
class S8():
    # 'Charts_M10_RPS'!S8
    value = 0.842164610231
    formula = "='Charts Data M10'!V7"
    @eval_fn
    def S8():
        v7_1 = Charts_Data_M10.V7()
        return v7_1

@register(Charts_M10_RPS)
class B9():
    # 'Charts_M10_RPS'!B9
    value = "KIUC"
    formula = "='Charts Data M10'!D8"
    @eval_fn
    def B9():
        d8_1 = Charts_Data_M10.D8()
        return d8_1

@register(Charts_M10_RPS)
class D9():
    # 'Charts_M10_RPS'!D9
    value = 0
    formula = "='Charts Data M10'!G8"
    @eval_fn
    def D9():
        g8_1 = Charts_Data_M10.G8()
        return g8_1

@register(Charts_M10_RPS)
class E9():
    # 'Charts_M10_RPS'!E9
    value = 0
    formula = "='Charts Data M10'!H8"
    @eval_fn
    def E9():
        h8_1 = Charts_Data_M10.H8()
        return h8_1

@register(Charts_M10_RPS)
class F9():
    # 'Charts_M10_RPS'!F9
    value = 0
    formula = "='Charts Data M10'!I8"
    @eval_fn
    def F9():
        i8_1 = Charts_Data_M10.I8()
        return i8_1

@register(Charts_M10_RPS)
class G9():
    # 'Charts_M10_RPS'!G9
    value = 0
    formula = "='Charts Data M10'!J8"
    @eval_fn
    def G9():
        j8_1 = Charts_Data_M10.J8()
        return j8_1

@register(Charts_M10_RPS)
class H9():
    # 'Charts_M10_RPS'!H9
    value = 0.145612259782
    formula = "='Charts Data M10'!K8"
    @eval_fn
    def H9():
        k8_1 = Charts_Data_M10.K8()
        return k8_1

@register(Charts_M10_RPS)
class I9():
    # 'Charts_M10_RPS'!I9
    value = 0.199732690326
    formula = "='Charts Data M10'!L8"
    @eval_fn
    def I9():
        l8_1 = Charts_Data_M10.L8()
        return l8_1

@register(Charts_M10_RPS)
class J9():
    # 'Charts_M10_RPS'!J9
    value = 0.199745833311
    formula = "='Charts Data M10'!M8"
    @eval_fn
    def J9():
        m8_1 = Charts_Data_M10.M8()
        return m8_1

@register(Charts_M10_RPS)
class K9():
    # 'Charts_M10_RPS'!K9
    value = 0.195941117045
    formula = "='Charts Data M10'!N8"
    @eval_fn
    def K9():
        n8_1 = Charts_Data_M10.N8()
        return n8_1

@register(Charts_M10_RPS)
class L9():
    # 'Charts_M10_RPS'!L9
    value = 0.137948410347
    formula = "='Charts Data M10'!O8"
    @eval_fn
    def L9():
        o8_1 = Charts_Data_M10.O8()
        return o8_1

@register(Charts_M10_RPS)
class M9():
    # 'Charts_M10_RPS'!M9
    value = 0.205314919027
    formula = "='Charts Data M10'!P8"
    @eval_fn
    def M9():
        p8_1 = Charts_Data_M10.P8()
        return p8_1

@register(Charts_M10_RPS)
class N9():
    # 'Charts_M10_RPS'!N9
    value = 0.227758304326
    formula = "='Charts Data M10'!Q8"
    @eval_fn
    def N9():
        q8_1 = Charts_Data_M10.Q8()
        return q8_1

@register(Charts_M10_RPS)
class O9():
    # 'Charts_M10_RPS'!O9
    value = 0.221020509585
    formula = "='Charts Data M10'!R8"
    @eval_fn
    def O9():
        r8_1 = Charts_Data_M10.R8()
        return r8_1

@register(Charts_M10_RPS)
class P9():
    # 'Charts_M10_RPS'!P9
    value = 0.264811181181
    formula = "='Charts Data M10'!S8"
    @eval_fn
    def P9():
        s8_1 = Charts_Data_M10.S8()
        return s8_1

@register(Charts_M10_RPS)
class Q9():
    # 'Charts_M10_RPS'!Q9
    value = 0.31203186936
    formula = "='Charts Data M10'!T8"
    @eval_fn
    def Q9():
        t8_1 = Charts_Data_M10.T8()
        return t8_1

@register(Charts_M10_RPS)
class R9():
    # 'Charts_M10_RPS'!R9
    value = 0.40625204676
    formula = "='Charts Data M10'!U8"
    @eval_fn
    def R9():
        u8_1 = Charts_Data_M10.U8()
        return u8_1

@register(Charts_M10_RPS)
class S9():
    # 'Charts_M10_RPS'!S9
    value = 0.526871863584
    formula = "='Charts Data M10'!V8"
    @eval_fn
    def S9():
        v8_1 = Charts_Data_M10.V8()
        return v8_1

@register(Charts_M10_RPS)
class B10():
    # 'Charts_M10_RPS'!B10
    value = "Total"

@register(Charts_M10_RPS)
class D10():
    # 'Charts_M10_RPS'!D10
    value = 0.140685946105
    formula = "='Charts Data M10'!G4"
    @eval_fn
    def D10():
        g4_1 = Charts_Data_M10.G4()
        return g4_1

@register(Charts_M10_RPS)
class E10():
    # 'Charts_M10_RPS'!E10
    value = 0.175069685961
    formula = "='Charts Data M10'!H4"
    @eval_fn
    def E10():
        h4_1 = Charts_Data_M10.H4()
        return h4_1

@register(Charts_M10_RPS)
class F10():
    # 'Charts_M10_RPS'!F10
    value = 0.156667174115
    formula = "='Charts Data M10'!I4"
    @eval_fn
    def F10():
        i4_1 = Charts_Data_M10.I4()
        return i4_1

@register(Charts_M10_RPS)
class G10():
    # 'Charts_M10_RPS'!G10
    value = 0.129793727507
    formula = "='Charts Data M10'!J4"
    @eval_fn
    def G10():
        j4_1 = Charts_Data_M10.J4()
        return j4_1

@register(Charts_M10_RPS)
class H10():
    # 'Charts_M10_RPS'!H10
    value = 0.165501115749
    formula = "='Charts Data M10'!K4"
    @eval_fn
    def H10():
        k4_1 = Charts_Data_M10.K4()
        return k4_1

@register(Charts_M10_RPS)
class I10():
    # 'Charts_M10_RPS'!I10
    value = 0.175089079901
    formula = "='Charts Data M10'!L4"
    @eval_fn
    def I10():
        l4_1 = Charts_Data_M10.L4()
        return l4_1

@register(Charts_M10_RPS)
class J10():
    # 'Charts_M10_RPS'!J10
    value = 0.169517031403
    formula = "='Charts Data M10'!M4"
    @eval_fn
    def J10():
        m4_1 = Charts_Data_M10.M4()
        return m4_1

@register(Charts_M10_RPS)
class K10():
    # 'Charts_M10_RPS'!K10
    value = 0.204137387828
    formula = "='Charts Data M10'!N4"
    @eval_fn
    def K10():
        n4_1 = Charts_Data_M10.N4()
        return n4_1

@register(Charts_M10_RPS)
class L10():
    # 'Charts_M10_RPS'!L10
    value = 0.222782315884
    formula = "='Charts Data M10'!O4"
    @eval_fn
    def L10():
        o4_1 = Charts_Data_M10.O4()
        return o4_1

@register(Charts_M10_RPS)
class M10():
    # 'Charts_M10_RPS'!M10
    value = 0.234702545853
    formula = "='Charts Data M10'!P4"
    @eval_fn
    def M10():
        p4_1 = Charts_Data_M10.P4()
        return p4_1

@register(Charts_M10_RPS)
class N10():
    # 'Charts_M10_RPS'!N10
    value = 0.237635646443
    formula = "='Charts Data M10'!Q4"
    @eval_fn
    def N10():
        q4_1 = Charts_Data_M10.Q4()
        return q4_1

@register(Charts_M10_RPS)
class O10():
    # 'Charts_M10_RPS'!O10
    value = 0.237004899189
    formula = "='Charts Data M10'!R4"
    @eval_fn
    def O10():
        r4_1 = Charts_Data_M10.R4()
        return r4_1

@register(Charts_M10_RPS)
class P10():
    # 'Charts_M10_RPS'!P10
    value = 0.297679064526
    formula = "='Charts Data M10'!S4"
    @eval_fn
    def P10():
        s4_1 = Charts_Data_M10.S4()
        return s4_1

@register(Charts_M10_RPS)
class Q10():
    # 'Charts_M10_RPS'!Q10
    value = 0.345024369608
    formula = "='Charts Data M10'!T4"
    @eval_fn
    def Q10():
        t4_1 = Charts_Data_M10.T4()
        return t4_1

@register(Charts_M10_RPS)
class R10():
    # 'Charts_M10_RPS'!R10
    value = 0.452207177191
    formula = "='Charts Data M10'!U4"
    @eval_fn
    def R10():
        u4_1 = Charts_Data_M10.U4()
        return u4_1

@register(Charts_M10_RPS)
class S10():
    # 'Charts_M10_RPS'!S10
    value = 0.532673712018
    formula = "='Charts Data M10'!V4"
    @eval_fn
    def S10():
        v4_1 = Charts_Data_M10.V4()
        return v4_1

@register(Charts_M10_RPS)
class B12():
    # 'Charts_M10_RPS'!B12
    value = "Percentage Attain of RPS"

@register(Charts_M10_RPS)
class C23():
    # 'Charts_M10_RPS'!C23
    value = 17

@register(Charts_M10_RPS)
class B26():
    # 'Charts_M10_RPS'!B26
    value = "Renewable Electricity Generated in 2015"
    formula = "='Charts Data M10'!$B$2"
    @eval_fn
    def B26():
        b2_1 = Charts_Data_M10.B2()
        return b2_1

@register(Charts_M10_RPS)
class B44():
    # 'Charts_M10_RPS'!B44
    value = "Renewable Generation as Percent of Total Sales in 2015"
    formula = "='Charts Data M10'!$B$3"
    @eval_fn
    def B44():
        b3_1 = Charts_Data_M10.B3()
        return b3_1