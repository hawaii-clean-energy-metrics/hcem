# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M15 = Worksheet('Charts_M15', 10, 10)



@register(Charts_M15)
class C2():
    # 'Charts_M15'!C2
    value = "Metric 15: MW of renewable energy projects installed (since benchmark date)"

@register(Charts_M15)
class C6():
    # 'Charts_M15'!C6
    value = 2000

@register(Charts_M15)
class D6():
    # 'Charts_M15'!D6
    value = 2001

@register(Charts_M15)
class E6():
    # 'Charts_M15'!E6
    value = 2002

@register(Charts_M15)
class F6():
    # 'Charts_M15'!F6
    value = 2003

@register(Charts_M15)
class G6():
    # 'Charts_M15'!G6
    value = 2004

@register(Charts_M15)
class H6():
    # 'Charts_M15'!H6
    value = 2005

@register(Charts_M15)
class I6():
    # 'Charts_M15'!I6
    value = 2006

@register(Charts_M15)
class J6():
    # 'Charts_M15'!J6
    value = 2007

@register(Charts_M15)
class K6():
    # 'Charts_M15'!K6
    value = 2008

@register(Charts_M15)
class L6():
    # 'Charts_M15'!L6
    value = 2009

@register(Charts_M15)
class M6():
    # 'Charts_M15'!M6
    value = 2010

@register(Charts_M15)
class N6():
    # 'Charts_M15'!N6
    value = 2011

@register(Charts_M15)
class O6():
    # 'Charts_M15'!O6
    value = 2012

@register(Charts_M15)
class P6():
    # 'Charts_M15'!P6
    value = 2013

@register(Charts_M15)
class Q6():
    # 'Charts_M15'!Q6
    value = 2014

@register(Charts_M15)
class R6():
    # 'Charts_M15'!R6
    value = 2015

@register(Charts_M15)
class S6():
    # 'Charts_M15'!S6
    value = 2016

@register(Charts_M15)
class T6():
    # 'Charts_M15'!T6
    value = 2017

@register(Charts_M15)
class U6():
    # 'Charts_M15'!U6
    value = 2018

@register(Charts_M15)
class V6():
    # 'Charts_M15'!V6
    value = 2019

@register(Charts_M15)
class W6():
    # 'Charts_M15'!W6
    value = 2020

@register(Charts_M15)
class B7():
    # 'Charts_M15'!B7
    value = "All Renewables"

@register(Charts_M15)
class C7():
    # 'Charts_M15'!C7
    value = 0
    formula = "='Charts Data M15'!G6"
    @eval_fn
    def C7():
        g6_1 = Charts_Data_M15.G6()
        return g6_1

@register(Charts_M15)
class D7():
    # 'Charts_M15'!D7
    value = -6
    formula = "='Charts Data M15'!H6"
    @eval_fn
    def D7():
        h6_1 = Charts_Data_M15.H6()
        return h6_1

@register(Charts_M15)
class E7():
    # 'Charts_M15'!E7
    value = -42
    formula = "='Charts Data M15'!I6"
    @eval_fn
    def E7():
        i6_1 = Charts_Data_M15.I6()
        return i6_1

@register(Charts_M15)
class F7():
    # 'Charts_M15'!F7
    value = 2
    formula = "='Charts Data M15'!J6"
    @eval_fn
    def F7():
        j6_1 = Charts_Data_M15.J6()
        return j6_1

@register(Charts_M15)
class G7():
    # 'Charts_M15'!G7
    value = 0
    formula = "='Charts Data M15'!K6"
    @eval_fn
    def G7():
        k6_1 = Charts_Data_M15.K6()
        return k6_1

@register(Charts_M15)
class H7():
    # 'Charts_M15'!H7
    value = 3.8
    formula = "='Charts Data M15'!L6"
    @eval_fn
    def H7():
        l6_1 = Charts_Data_M15.L6()
        return l6_1

@register(Charts_M15)
class I7():
    # 'Charts_M15'!I7
    value = 32.6
    formula = "='Charts Data M15'!M6"
    @eval_fn
    def I7():
        m6_1 = Charts_Data_M15.M6()
        return m6_1

@register(Charts_M15)
class J7():
    # 'Charts_M15'!J7
    value = 23.844
    formula = "='Charts Data M15'!N6"
    @eval_fn
    def J7():
        n6_1 = Charts_Data_M15.N6()
        return n6_1

@register(Charts_M15)
class K7():
    # 'Charts_M15'!K7
    value = 8.925
    formula = "='Charts Data M15'!O6"
    @eval_fn
    def K7():
        o6_1 = Charts_Data_M15.O6()
        return o6_1

@register(Charts_M15)
class L7():
    # 'Charts_M15'!L7
    value = 125.27
    formula = "='Charts Data M15'!P6"
    @eval_fn
    def L7():
        p6_1 = Charts_Data_M15.P6()
        return p6_1

@register(Charts_M15)
class M7():
    # 'Charts_M15'!M7
    value = 15.166
    formula = "='Charts Data M15'!Q6"
    @eval_fn
    def M7():
        q6_1 = Charts_Data_M15.Q6()
        return q6_1

@register(Charts_M15)
class N7():
    # 'Charts_M15'!N7
    value = 72.04
    formula = "='Charts Data M15'!R6"
    @eval_fn
    def N7():
        r6_1 = Charts_Data_M15.R6()
        return r6_1

@register(Charts_M15)
class O7():
    # 'Charts_M15'!O7
    value = 223.352
    formula = "='Charts Data M15'!S6"
    @eval_fn
    def O7():
        s6_1 = Charts_Data_M15.S6()
        return s6_1

@register(Charts_M15)
class P7():
    # 'Charts_M15'!P7
    value = 128.403
    formula = "='Charts Data M15'!T6"
    @eval_fn
    def P7():
        t6_1 = Charts_Data_M15.T6()
        return t6_1

@register(Charts_M15)
class Q7():
    # 'Charts_M15'!Q7
    value = -248
    formula = "='Charts Data M15'!U6"
    @eval_fn
    def Q7():
        u6_1 = Charts_Data_M15.U6()
        return u6_1

@register(Charts_M15)
class R7():
    # 'Charts_M15'!R7
    value = 15
    formula = "='Charts Data M15'!V6"
    @eval_fn
    def R7():
        v6_1 = Charts_Data_M15.V6()
        return v6_1

@register(Charts_M15)
class S7():
    # 'Charts_M15'!S7
    value = "#N/A"
    formula = "='Charts Data M15'!W6"
    @eval_fn
    def S7():
        w6_1 = Charts_Data_M15.W6()
        return w6_1

@register(Charts_M15)
class T7():
    # 'Charts_M15'!T7
    value = "#N/A"
    formula = "='Charts Data M15'!X6"
    @eval_fn
    def T7():
        x6_1 = Charts_Data_M15.X6()
        return x6_1

@register(Charts_M15)
class U7():
    # 'Charts_M15'!U7
    value = "#N/A"
    formula = "='Charts Data M15'!Y6"
    @eval_fn
    def U7():
        y6_1 = Charts_Data_M15.Y6()
        return y6_1

@register(Charts_M15)
class V7():
    # 'Charts_M15'!V7
    value = "#N/A"
    formula = "='Charts Data M15'!Z6"
    @eval_fn
    def V7():
        z6_1 = Charts_Data_M15.Z6()
        return z6_1

@register(Charts_M15)
class W7():
    # 'Charts_M15'!W7
    value = "#N/A"
    formula = "='Charts Data M15'!AA6"
    @eval_fn
    def W7():
        aa6_1 = Charts_Data_M15.AA6()
        return aa6_1

@register(Charts_M15)
class B8():
    # 'Charts_M15'!B8
    value = "Geothermal"

@register(Charts_M15)
class C8():
    # 'Charts_M15'!C8
    value = 0
    formula = "='Charts Data M15'!G7"
    @eval_fn
    def C8():
        g7_1 = Charts_Data_M15.G7()
        return g7_1

@register(Charts_M15)
class D8():
    # 'Charts_M15'!D8
    value = 0
    formula = "='Charts Data M15'!H7"
    @eval_fn
    def D8():
        h7_1 = Charts_Data_M15.H7()
        return h7_1

@register(Charts_M15)
class E8():
    # 'Charts_M15'!E8
    value = 0
    formula = "='Charts Data M15'!I7"
    @eval_fn
    def E8():
        i7_1 = Charts_Data_M15.I7()
        return i7_1

@register(Charts_M15)
class F8():
    # 'Charts_M15'!F8
    value = 0
    formula = "='Charts Data M15'!J7"
    @eval_fn
    def F8():
        j7_1 = Charts_Data_M15.J7()
        return j7_1

@register(Charts_M15)
class G8():
    # 'Charts_M15'!G8
    value = 0
    formula = "='Charts Data M15'!K7"
    @eval_fn
    def G8():
        k7_1 = Charts_Data_M15.K7()
        return k7_1

@register(Charts_M15)
class H8():
    # 'Charts_M15'!H8
    value = 0
    formula = "='Charts Data M15'!L7"
    @eval_fn
    def H8():
        l7_1 = Charts_Data_M15.L7()
        return l7_1

@register(Charts_M15)
class I8():
    # 'Charts_M15'!I8
    value = 0
    formula = "='Charts Data M15'!M7"
    @eval_fn
    def I8():
        m7_1 = Charts_Data_M15.M7()
        return m7_1

@register(Charts_M15)
class J8():
    # 'Charts_M15'!J8
    value = 0
    formula = "='Charts Data M15'!N7"
    @eval_fn
    def J8():
        n7_1 = Charts_Data_M15.N7()
        return n7_1

@register(Charts_M15)
class K8():
    # 'Charts_M15'!K8
    value = 0
    formula = "='Charts Data M15'!O7"
    @eval_fn
    def K8():
        o7_1 = Charts_Data_M15.O7()
        return o7_1

@register(Charts_M15)
class L8():
    # 'Charts_M15'!L8
    value = 0
    formula = "='Charts Data M15'!P7"
    @eval_fn
    def L8():
        p7_1 = Charts_Data_M15.P7()
        return p7_1

@register(Charts_M15)
class M8():
    # 'Charts_M15'!M8
    value = 0
    formula = "='Charts Data M15'!Q7"
    @eval_fn
    def M8():
        q7_1 = Charts_Data_M15.Q7()
        return q7_1

@register(Charts_M15)
class N8():
    # 'Charts_M15'!N8
    value = 0
    formula = "='Charts Data M15'!R7"
    @eval_fn
    def N8():
        r7_1 = Charts_Data_M15.R7()
        return r7_1

@register(Charts_M15)
class O8():
    # 'Charts_M15'!O8
    value = 16
    formula = "='Charts Data M15'!S7"
    @eval_fn
    def O8():
        s7_1 = Charts_Data_M15.S7()
        return s7_1

@register(Charts_M15)
class P8():
    # 'Charts_M15'!P8
    value = 0
    formula = "='Charts Data M15'!T7"
    @eval_fn
    def P8():
        t7_1 = Charts_Data_M15.T7()
        return t7_1

@register(Charts_M15)
class Q8():
    # 'Charts_M15'!Q8
    value = 0
    formula = "='Charts Data M15'!U7"
    @eval_fn
    def Q8():
        u7_1 = Charts_Data_M15.U7()
        return u7_1

@register(Charts_M15)
class R8():
    # 'Charts_M15'!R8
    value = 0
    formula = "='Charts Data M15'!V7"
    @eval_fn
    def R8():
        v7_1 = Charts_Data_M15.V7()
        return v7_1

@register(Charts_M15)
class S8():
    # 'Charts_M15'!S8
    value = "#N/A"
    formula = "='Charts Data M15'!W7"
    @eval_fn
    def S8():
        w7_1 = Charts_Data_M15.W7()
        return w7_1

@register(Charts_M15)
class T8():
    # 'Charts_M15'!T8
    value = "#N/A"
    formula = "='Charts Data M15'!X7"
    @eval_fn
    def T8():
        x7_1 = Charts_Data_M15.X7()
        return x7_1

@register(Charts_M15)
class U8():
    # 'Charts_M15'!U8
    value = "#N/A"
    formula = "='Charts Data M15'!Y7"
    @eval_fn
    def U8():
        y7_1 = Charts_Data_M15.Y7()
        return y7_1

@register(Charts_M15)
class V8():
    # 'Charts_M15'!V8
    value = "#N/A"
    formula = "='Charts Data M15'!Z7"
    @eval_fn
    def V8():
        z7_1 = Charts_Data_M15.Z7()
        return z7_1

@register(Charts_M15)
class W8():
    # 'Charts_M15'!W8
    value = "#N/A"
    formula = "='Charts Data M15'!AA7"
    @eval_fn
    def W8():
        aa7_1 = Charts_Data_M15.AA7()
        return aa7_1

@register(Charts_M15)
class B9():
    # 'Charts_M15'!B9
    value = "Hydroelectric"

@register(Charts_M15)
class C9():
    # 'Charts_M15'!C9
    value = 0
    formula = "='Charts Data M15'!G8"
    @eval_fn
    def C9():
        g8_1 = Charts_Data_M15.G8()
        return g8_1

@register(Charts_M15)
class D9():
    # 'Charts_M15'!D9
    value = -1
    formula = "='Charts Data M15'!H8"
    @eval_fn
    def D9():
        h8_1 = Charts_Data_M15.H8()
        return h8_1

@register(Charts_M15)
class E9():
    # 'Charts_M15'!E9
    value = -1
    formula = "='Charts Data M15'!I8"
    @eval_fn
    def E9():
        i8_1 = Charts_Data_M15.I8()
        return i8_1

@register(Charts_M15)
class F9():
    # 'Charts_M15'!F9
    value = -2
    formula = "='Charts Data M15'!J8"
    @eval_fn
    def F9():
        j8_1 = Charts_Data_M15.J8()
        return j8_1

@register(Charts_M15)
class G9():
    # 'Charts_M15'!G9
    value = 0
    formula = "='Charts Data M15'!K8"
    @eval_fn
    def G9():
        k8_1 = Charts_Data_M15.K8()
        return k8_1

@register(Charts_M15)
class H9():
    # 'Charts_M15'!H9
    value = 2
    formula = "='Charts Data M15'!L8"
    @eval_fn
    def H9():
        l8_1 = Charts_Data_M15.L8()
        return l8_1

@register(Charts_M15)
class I9():
    # 'Charts_M15'!I9
    value = 0
    formula = "='Charts Data M15'!M8"
    @eval_fn
    def I9():
        m8_1 = Charts_Data_M15.M8()
        return m8_1

@register(Charts_M15)
class J9():
    # 'Charts_M15'!J9
    value = 0
    formula = "='Charts Data M15'!N8"
    @eval_fn
    def J9():
        n8_1 = Charts_Data_M15.N8()
        return n8_1

@register(Charts_M15)
class K9():
    # 'Charts_M15'!K9
    value = 0
    formula = "='Charts Data M15'!O8"
    @eval_fn
    def K9():
        o8_1 = Charts_Data_M15.O8()
        return o8_1

@register(Charts_M15)
class L9():
    # 'Charts_M15'!L9
    value = 0
    formula = "='Charts Data M15'!P8"
    @eval_fn
    def L9():
        p8_1 = Charts_Data_M15.P8()
        return p8_1

@register(Charts_M15)
class M9():
    # 'Charts_M15'!M9
    value = 0
    formula = "='Charts Data M15'!Q8"
    @eval_fn
    def M9():
        q8_1 = Charts_Data_M15.Q8()
        return q8_1

@register(Charts_M15)
class N9():
    # 'Charts_M15'!N9
    value = -0.1
    formula = "='Charts Data M15'!R8"
    @eval_fn
    def N9():
        r8_1 = Charts_Data_M15.R8()
        return r8_1

@register(Charts_M15)
class O9():
    # 'Charts_M15'!O9
    value = 1.3
    formula = "='Charts Data M15'!S8"
    @eval_fn
    def O9():
        s8_1 = Charts_Data_M15.S8()
        return s8_1

@register(Charts_M15)
class P9():
    # 'Charts_M15'!P9
    value = 0
    formula = "='Charts Data M15'!T8"
    @eval_fn
    def P9():
        t8_1 = Charts_Data_M15.T8()
        return t8_1

@register(Charts_M15)
class Q9():
    # 'Charts_M15'!Q9
    value = 0
    formula = "='Charts Data M15'!U8"
    @eval_fn
    def Q9():
        u8_1 = Charts_Data_M15.U8()
        return u8_1

@register(Charts_M15)
class R9():
    # 'Charts_M15'!R9
    value = 0
    formula = "='Charts Data M15'!V8"
    @eval_fn
    def R9():
        v8_1 = Charts_Data_M15.V8()
        return v8_1

@register(Charts_M15)
class S9():
    # 'Charts_M15'!S9
    value = "#N/A"
    formula = "='Charts Data M15'!W8"
    @eval_fn
    def S9():
        w8_1 = Charts_Data_M15.W8()
        return w8_1

@register(Charts_M15)
class T9():
    # 'Charts_M15'!T9
    value = "#N/A"
    formula = "='Charts Data M15'!X8"
    @eval_fn
    def T9():
        x8_1 = Charts_Data_M15.X8()
        return x8_1

@register(Charts_M15)
class U9():
    # 'Charts_M15'!U9
    value = "#N/A"
    formula = "='Charts Data M15'!Y8"
    @eval_fn
    def U9():
        y8_1 = Charts_Data_M15.Y8()
        return y8_1

@register(Charts_M15)
class V9():
    # 'Charts_M15'!V9
    value = "#N/A"
    formula = "='Charts Data M15'!Z8"
    @eval_fn
    def V9():
        z8_1 = Charts_Data_M15.Z8()
        return z8_1

@register(Charts_M15)
class W9():
    # 'Charts_M15'!W9
    value = "#N/A"
    formula = "='Charts Data M15'!AA8"
    @eval_fn
    def W9():
        aa8_1 = Charts_Data_M15.AA8()
        return aa8_1

@register(Charts_M15)
class B10():
    # 'Charts_M15'!B10
    value = "Other Biomass"

@register(Charts_M15)
class C10():
    # 'Charts_M15'!C10
    value = 0
    formula = "='Charts Data M15'!G9"
    @eval_fn
    def C10():
        g9_1 = Charts_Data_M15.G9()
        return g9_1

@register(Charts_M15)
class D10():
    # 'Charts_M15'!D10
    value = -4
    formula = "='Charts Data M15'!H9"
    @eval_fn
    def D10():
        h9_1 = Charts_Data_M15.H9()
        return h9_1

@register(Charts_M15)
class E10():
    # 'Charts_M15'!E10
    value = -41
    formula = "='Charts Data M15'!I9"
    @eval_fn
    def E10():
        i9_1 = Charts_Data_M15.I9()
        return i9_1

@register(Charts_M15)
class F10():
    # 'Charts_M15'!F10
    value = 4
    formula = "='Charts Data M15'!J9"
    @eval_fn
    def F10():
        j9_1 = Charts_Data_M15.J9()
        return j9_1

@register(Charts_M15)
class G10():
    # 'Charts_M15'!G10
    value = 0
    formula = "='Charts Data M15'!K9"
    @eval_fn
    def G10():
        k9_1 = Charts_Data_M15.K9()
        return k9_1

@register(Charts_M15)
class H10():
    # 'Charts_M15'!H10
    value = 0
    formula = "='Charts Data M15'!L9"
    @eval_fn
    def H10():
        l9_1 = Charts_Data_M15.L9()
        return l9_1

@register(Charts_M15)
class I10():
    # 'Charts_M15'!I10
    value = 0
    formula = "='Charts Data M15'!M9"
    @eval_fn
    def I10():
        m9_1 = Charts_Data_M15.M9()
        return m9_1

@register(Charts_M15)
class J10():
    # 'Charts_M15'!J10
    value = 0
    formula = "='Charts Data M15'!N9"
    @eval_fn
    def J10():
        n9_1 = Charts_Data_M15.N9()
        return n9_1

@register(Charts_M15)
class K10():
    # 'Charts_M15'!K10
    value = 0
    formula = "='Charts Data M15'!O9"
    @eval_fn
    def K10():
        o9_1 = Charts_Data_M15.O9()
        return o9_1

@register(Charts_M15)
class L10():
    # 'Charts_M15'!L10
    value = 113
    formula = "='Charts Data M15'!P9"
    @eval_fn
    def L10():
        p9_1 = Charts_Data_M15.P9()
        return p9_1

@register(Charts_M15)
class M10():
    # 'Charts_M15'!M10
    value = 0
    formula = "='Charts Data M15'!Q9"
    @eval_fn
    def M10():
        q9_1 = Charts_Data_M15.Q9()
        return q9_1

@register(Charts_M15)
class N10():
    # 'Charts_M15'!N10
    value = -0.2
    formula = "='Charts Data M15'!R9"
    @eval_fn
    def N10():
        r9_1 = Charts_Data_M15.R9()
        return r9_1

@register(Charts_M15)
class O10():
    # 'Charts_M15'!O10
    value = 0
    formula = "='Charts Data M15'!S9"
    @eval_fn
    def O10():
        s9_1 = Charts_Data_M15.S9()
        return s9_1

@register(Charts_M15)
class P10():
    # 'Charts_M15'!P10
    value = 33.6
    formula = "='Charts Data M15'!T9"
    @eval_fn
    def P10():
        t9_1 = Charts_Data_M15.T9()
        return t9_1

@register(Charts_M15)
class Q10():
    # 'Charts_M15'!Q10
    value = -4
    formula = "='Charts Data M15'!U9"
    @eval_fn
    def Q10():
        u9_1 = Charts_Data_M15.U9()
        return u9_1

@register(Charts_M15)
class R10():
    # 'Charts_M15'!R10
    value = 0
    formula = "='Charts Data M15'!V9"
    @eval_fn
    def R10():
        v9_1 = Charts_Data_M15.V9()
        return v9_1

@register(Charts_M15)
class S10():
    # 'Charts_M15'!S10
    value = "#N/A"
    formula = "='Charts Data M15'!W9"
    @eval_fn
    def S10():
        w9_1 = Charts_Data_M15.W9()
        return w9_1

@register(Charts_M15)
class T10():
    # 'Charts_M15'!T10
    value = "#N/A"
    formula = "='Charts Data M15'!X9"
    @eval_fn
    def T10():
        x9_1 = Charts_Data_M15.X9()
        return x9_1

@register(Charts_M15)
class U10():
    # 'Charts_M15'!U10
    value = "#N/A"
    formula = "='Charts Data M15'!Y9"
    @eval_fn
    def U10():
        y9_1 = Charts_Data_M15.Y9()
        return y9_1

@register(Charts_M15)
class V10():
    # 'Charts_M15'!V10
    value = "#N/A"
    formula = "='Charts Data M15'!Z9"
    @eval_fn
    def V10():
        z9_1 = Charts_Data_M15.Z9()
        return z9_1

@register(Charts_M15)
class W10():
    # 'Charts_M15'!W10
    value = "#N/A"
    formula = "='Charts Data M15'!AA9"
    @eval_fn
    def W10():
        aa9_1 = Charts_Data_M15.AA9()
        return aa9_1

@register(Charts_M15)
class B11():
    # 'Charts_M15'!B11
    value = "Other Gases"

@register(Charts_M15)
class C11():
    # 'Charts_M15'!C11
    value = 0
    formula = "='Charts Data M15'!G10"
    @eval_fn
    def C11():
        g10_1 = Charts_Data_M15.G10()
        return g10_1

@register(Charts_M15)
class D11():
    # 'Charts_M15'!D11
    value = 0
    formula = "='Charts Data M15'!H10"
    @eval_fn
    def D11():
        h10_1 = Charts_Data_M15.H10()
        return h10_1

@register(Charts_M15)
class E11():
    # 'Charts_M15'!E11
    value = 0
    formula = "='Charts Data M15'!I10"
    @eval_fn
    def E11():
        i10_1 = Charts_Data_M15.I10()
        return i10_1

@register(Charts_M15)
class F11():
    # 'Charts_M15'!F11
    value = 0
    formula = "='Charts Data M15'!J10"
    @eval_fn
    def F11():
        j10_1 = Charts_Data_M15.J10()
        return j10_1

@register(Charts_M15)
class G11():
    # 'Charts_M15'!G11
    value = 0
    formula = "='Charts Data M15'!K10"
    @eval_fn
    def G11():
        k10_1 = Charts_Data_M15.K10()
        return k10_1

@register(Charts_M15)
class H11():
    # 'Charts_M15'!H11
    value = 0
    formula = "='Charts Data M15'!L10"
    @eval_fn
    def H11():
        l10_1 = Charts_Data_M15.L10()
        return l10_1

@register(Charts_M15)
class I11():
    # 'Charts_M15'!I11
    value = 0
    formula = "='Charts Data M15'!M10"
    @eval_fn
    def I11():
        m10_1 = Charts_Data_M15.M10()
        return m10_1

@register(Charts_M15)
class J11():
    # 'Charts_M15'!J11
    value = 0
    formula = "='Charts Data M15'!N10"
    @eval_fn
    def J11():
        n10_1 = Charts_Data_M15.N10()
        return n10_1

@register(Charts_M15)
class K11():
    # 'Charts_M15'!K11
    value = 0
    formula = "='Charts Data M15'!O10"
    @eval_fn
    def K11():
        o10_1 = Charts_Data_M15.O10()
        return o10_1

@register(Charts_M15)
class L11():
    # 'Charts_M15'!L11
    value = 0
    formula = "='Charts Data M15'!P10"
    @eval_fn
    def L11():
        p10_1 = Charts_Data_M15.P10()
        return p10_1

@register(Charts_M15)
class M11():
    # 'Charts_M15'!M11
    value = 0
    formula = "='Charts Data M15'!Q10"
    @eval_fn
    def M11():
        q10_1 = Charts_Data_M15.Q10()
        return q10_1

@register(Charts_M15)
class N11():
    # 'Charts_M15'!N11
    value = 3.2
    formula = "='Charts Data M15'!R10"
    @eval_fn
    def N11():
        r10_1 = Charts_Data_M15.R10()
        return r10_1

@register(Charts_M15)
class O11():
    # 'Charts_M15'!O11
    value = -6.2
    formula = "='Charts Data M15'!S10"
    @eval_fn
    def O11():
        s10_1 = Charts_Data_M15.S10()
        return s10_1

@register(Charts_M15)
class P11():
    # 'Charts_M15'!P11
    value = 0
    formula = "='Charts Data M15'!T10"
    @eval_fn
    def P11():
        t10_1 = Charts_Data_M15.T10()
        return t10_1

@register(Charts_M15)
class Q11():
    # 'Charts_M15'!Q11
    value = 0
    formula = "='Charts Data M15'!U10"
    @eval_fn
    def Q11():
        u10_1 = Charts_Data_M15.U10()
        return u10_1

@register(Charts_M15)
class R11():
    # 'Charts_M15'!R11
    value = 3
    formula = "='Charts Data M15'!V10"
    @eval_fn
    def R11():
        v10_1 = Charts_Data_M15.V10()
        return v10_1

@register(Charts_M15)
class S11():
    # 'Charts_M15'!S11
    value = "#N/A"
    formula = "='Charts Data M15'!W10"
    @eval_fn
    def S11():
        w10_1 = Charts_Data_M15.W10()
        return w10_1

@register(Charts_M15)
class T11():
    # 'Charts_M15'!T11
    value = "#N/A"
    formula = "='Charts Data M15'!X10"
    @eval_fn
    def T11():
        x10_1 = Charts_Data_M15.X10()
        return x10_1

@register(Charts_M15)
class U11():
    # 'Charts_M15'!U11
    value = "#N/A"
    formula = "='Charts Data M15'!Y10"
    @eval_fn
    def U11():
        y10_1 = Charts_Data_M15.Y10()
        return y10_1

@register(Charts_M15)
class V11():
    # 'Charts_M15'!V11
    value = "#N/A"
    formula = "='Charts Data M15'!Z10"
    @eval_fn
    def V11():
        z10_1 = Charts_Data_M15.Z10()
        return z10_1

@register(Charts_M15)
class W11():
    # 'Charts_M15'!W11
    value = "#N/A"
    formula = "='Charts Data M15'!AA10"
    @eval_fn
    def W11():
        aa10_1 = Charts_Data_M15.AA10()
        return aa10_1

@register(Charts_M15)
class B12():
    # 'Charts_M15'!B12
    value = "Solar Thermal and Photovoltaic"

@register(Charts_M15)
class C12():
    # 'Charts_M15'!C12
    value = 0
    formula = "='Charts Data M15'!G11"
    @eval_fn
    def C12():
        g11_1 = Charts_Data_M15.G11()
        return g11_1

@register(Charts_M15)
class D12():
    # 'Charts_M15'!D12
    value = 0
    formula = "='Charts Data M15'!H11"
    @eval_fn
    def D12():
        h11_1 = Charts_Data_M15.H11()
        return h11_1

@register(Charts_M15)
class E12():
    # 'Charts_M15'!E12
    value = 0
    formula = "='Charts Data M15'!I11"
    @eval_fn
    def E12():
        i11_1 = Charts_Data_M15.I11()
        return i11_1

@register(Charts_M15)
class F12():
    # 'Charts_M15'!F12
    value = 0
    formula = "='Charts Data M15'!J11"
    @eval_fn
    def F12():
        j11_1 = Charts_Data_M15.J11()
        return j11_1

@register(Charts_M15)
class G12():
    # 'Charts_M15'!G12
    value = 0
    formula = "='Charts Data M15'!K11"
    @eval_fn
    def G12():
        k11_1 = Charts_Data_M15.K11()
        return k11_1

@register(Charts_M15)
class H12():
    # 'Charts_M15'!H12
    value = 1.8
    formula = "='Charts Data M15'!L11"
    @eval_fn
    def H12():
        l11_1 = Charts_Data_M15.L11()
        return l11_1

@register(Charts_M15)
class I12():
    # 'Charts_M15'!I12
    value = 0.6
    formula = "='Charts Data M15'!M11"
    @eval_fn
    def I12():
        m11_1 = Charts_Data_M15.M11()
        return m11_1

@register(Charts_M15)
class J12():
    # 'Charts_M15'!J12
    value = 2.844
    formula = "='Charts Data M15'!N11"
    @eval_fn
    def J12():
        n11_1 = Charts_Data_M15.N11()
        return n11_1

@register(Charts_M15)
class K12():
    # 'Charts_M15'!K12
    value = 8.925
    formula = "='Charts Data M15'!O11"
    @eval_fn
    def K12():
        o11_1 = Charts_Data_M15.O11()
        return o11_1

@register(Charts_M15)
class L12():
    # 'Charts_M15'!L12
    value = 12.27
    formula = "='Charts Data M15'!P11"
    @eval_fn
    def L12():
        p11_1 = Charts_Data_M15.P11()
        return p11_1

@register(Charts_M15)
class M12():
    # 'Charts_M15'!M12
    value = 17.166
    formula = "='Charts Data M15'!Q11"
    @eval_fn
    def M12():
        q11_1 = Charts_Data_M15.Q11()
        return q11_1

@register(Charts_M15)
class N12():
    # 'Charts_M15'!N12
    value = 39.54
    formula = "='Charts Data M15'!R11"
    @eval_fn
    def N12():
        r11_1 = Charts_Data_M15.R11()
        return r11_1

@register(Charts_M15)
class O12():
    # 'Charts_M15'!O12
    value = 98.252
    formula = "='Charts Data M15'!S11"
    @eval_fn
    def O12():
        s11_1 = Charts_Data_M15.S11()
        return s11_1

@register(Charts_M15)
class P12():
    # 'Charts_M15'!P12
    value = 94.803
    formula = "='Charts Data M15'!T11"
    @eval_fn
    def P12():
        t11_1 = Charts_Data_M15.T11()
        return t11_1

@register(Charts_M15)
class Q12():
    # 'Charts_M15'!Q12
    value = -244
    formula = "='Charts Data M15'!U11"
    @eval_fn
    def Q12():
        u11_1 = Charts_Data_M15.U11()
        return u11_1

@register(Charts_M15)
class R12():
    # 'Charts_M15'!R12
    value = 12
    formula = "='Charts Data M15'!V11"
    @eval_fn
    def R12():
        v11_1 = Charts_Data_M15.V11()
        return v11_1

@register(Charts_M15)
class S12():
    # 'Charts_M15'!S12
    value = -44.2
    formula = "='Charts Data M15'!W11"
    @eval_fn
    def S12():
        w11_1 = Charts_Data_M15.W11()
        return w11_1

@register(Charts_M15)
class T12():
    # 'Charts_M15'!T12
    value = 0
    formula = "='Charts Data M15'!X11"
    @eval_fn
    def T12():
        x11_1 = Charts_Data_M15.X11()
        return x11_1

@register(Charts_M15)
class U12():
    # 'Charts_M15'!U12
    value = 0
    formula = "='Charts Data M15'!Y11"
    @eval_fn
    def U12():
        y11_1 = Charts_Data_M15.Y11()
        return y11_1

@register(Charts_M15)
class V12():
    # 'Charts_M15'!V12
    value = 0
    formula = "='Charts Data M15'!Z11"
    @eval_fn
    def V12():
        z11_1 = Charts_Data_M15.Z11()
        return z11_1

@register(Charts_M15)
class W12():
    # 'Charts_M15'!W12
    value = 0
    formula = "='Charts Data M15'!AA11"
    @eval_fn
    def W12():
        aa11_1 = Charts_Data_M15.AA11()
        return aa11_1

@register(Charts_M15)
class B13():
    # 'Charts_M15'!B13
    value = "Wind"

@register(Charts_M15)
class C13():
    # 'Charts_M15'!C13
    value = 0
    formula = "='Charts Data M15'!G12"
    @eval_fn
    def C13():
        g12_1 = Charts_Data_M15.G12()
        return g12_1

@register(Charts_M15)
class D13():
    # 'Charts_M15'!D13
    value = -1
    formula = "='Charts Data M15'!H12"
    @eval_fn
    def D13():
        h12_1 = Charts_Data_M15.H12()
        return h12_1

@register(Charts_M15)
class E13():
    # 'Charts_M15'!E13
    value = 0
    formula = "='Charts Data M15'!I12"
    @eval_fn
    def E13():
        i12_1 = Charts_Data_M15.I12()
        return i12_1

@register(Charts_M15)
class F13():
    # 'Charts_M15'!F13
    value = 0
    formula = "='Charts Data M15'!J12"
    @eval_fn
    def F13():
        j12_1 = Charts_Data_M15.J12()
        return j12_1

@register(Charts_M15)
class G13():
    # 'Charts_M15'!G13
    value = 0
    formula = "='Charts Data M15'!K12"
    @eval_fn
    def G13():
        k12_1 = Charts_Data_M15.K12()
        return k12_1

@register(Charts_M15)
class H13():
    # 'Charts_M15'!H13
    value = 0
    formula = "='Charts Data M15'!L12"
    @eval_fn
    def H13():
        l12_1 = Charts_Data_M15.L12()
        return l12_1

@register(Charts_M15)
class I13():
    # 'Charts_M15'!I13
    value = 32
    formula = "='Charts Data M15'!M12"
    @eval_fn
    def I13():
        m12_1 = Charts_Data_M15.M12()
        return m12_1

@register(Charts_M15)
class J13():
    # 'Charts_M15'!J13
    value = 21
    formula = "='Charts Data M15'!N12"
    @eval_fn
    def J13():
        n12_1 = Charts_Data_M15.N12()
        return n12_1

@register(Charts_M15)
class K13():
    # 'Charts_M15'!K13
    value = 0
    formula = "='Charts Data M15'!O12"
    @eval_fn
    def K13():
        o12_1 = Charts_Data_M15.O12()
        return o12_1

@register(Charts_M15)
class L13():
    # 'Charts_M15'!L13
    value = 0
    formula = "='Charts Data M15'!P12"
    @eval_fn
    def L13():
        p12_1 = Charts_Data_M15.P12()
        return p12_1

@register(Charts_M15)
class M13():
    # 'Charts_M15'!M13
    value = -2
    formula = "='Charts Data M15'!Q12"
    @eval_fn
    def M13():
        q12_1 = Charts_Data_M15.Q12()
        return q12_1

@register(Charts_M15)
class N13():
    # 'Charts_M15'!N13
    value = 29.6
    formula = "='Charts Data M15'!R12"
    @eval_fn
    def N13():
        r12_1 = Charts_Data_M15.R12()
        return r12_1

@register(Charts_M15)
class O13():
    # 'Charts_M15'!O13
    value = 114
    formula = "='Charts Data M15'!S12"
    @eval_fn
    def O13():
        s12_1 = Charts_Data_M15.S12()
        return s12_1

@register(Charts_M15)
class P13():
    # 'Charts_M15'!P13
    value = 0
    formula = "='Charts Data M15'!T12"
    @eval_fn
    def P13():
        t12_1 = Charts_Data_M15.T12()
        return t12_1

@register(Charts_M15)
class Q13():
    # 'Charts_M15'!Q13
    value = 0
    formula = "='Charts Data M15'!U12"
    @eval_fn
    def Q13():
        u12_1 = Charts_Data_M15.U12()
        return u12_1

@register(Charts_M15)
class R13():
    # 'Charts_M15'!R13
    value = 0
    formula = "='Charts Data M15'!V12"
    @eval_fn
    def R13():
        v12_1 = Charts_Data_M15.V12()
        return v12_1

@register(Charts_M15)
class S13():
    # 'Charts_M15'!S13
    value = "#N/A"
    formula = "='Charts Data M15'!W12"
    @eval_fn
    def S13():
        w12_1 = Charts_Data_M15.W12()
        return w12_1

@register(Charts_M15)
class T13():
    # 'Charts_M15'!T13
    value = "#N/A"
    formula = "='Charts Data M15'!X12"
    @eval_fn
    def T13():
        x12_1 = Charts_Data_M15.X12()
        return x12_1

@register(Charts_M15)
class U13():
    # 'Charts_M15'!U13
    value = "#N/A"
    formula = "='Charts Data M15'!Y12"
    @eval_fn
    def U13():
        y12_1 = Charts_Data_M15.Y12()
        return y12_1

@register(Charts_M15)
class V13():
    # 'Charts_M15'!V13
    value = "#N/A"
    formula = "='Charts Data M15'!Z12"
    @eval_fn
    def V13():
        z12_1 = Charts_Data_M15.Z12()
        return z12_1

@register(Charts_M15)
class W13():
    # 'Charts_M15'!W13
    value = "#N/A"
    formula = "='Charts Data M15'!AA12"
    @eval_fn
    def W13():
        aa12_1 = Charts_Data_M15.AA12()
        return aa12_1

@register(Charts_M15)
class B15():
    # 'Charts_M15'!B15
    value = "Annual Change in MW"
    formula = "='Charts Data M15'!$B$2"
    @eval_fn
    def B15():
        b2_1 = Charts_Data_M15.B2()
        return b2_1

@register(Charts_M15)
class B16():
    # 'Charts_M15'!B16
    value = 6

@register(Charts_M15)
class B17():
    # 'Charts_M15'!B17
    value = 3

@register(Charts_M15)
class B31():
    # 'Charts_M15'!B31
    value = "MW of Renewable Generation by Fuel Source"