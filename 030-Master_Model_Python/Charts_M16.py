# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M16 = Worksheet('Charts_M16', 10, 10)



@register(Charts_M16)
class D2():
    # 'Charts_M16'!D2
    value = "Metric 16: MWh and MWh per year energy savings from energy efficiency programs"

@register(Charts_M16)
class D7():
    # 'Charts_M16'!D7
    value = 1999
    formula = "='Dashboard M16 EEPS'!G5"
    @eval_fn
    def D7():
        g5_1 = Dashboard_M16_EEPS.G5()
        return g5_1

@register(Charts_M16)
class E7():
    # 'Charts_M16'!E7
    value = 2000
    formula = "='Dashboard M16 EEPS'!H5"
    @eval_fn
    def E7():
        h5_1 = Dashboard_M16_EEPS.H5()
        return h5_1

@register(Charts_M16)
class F7():
    # 'Charts_M16'!F7
    value = 2001
    formula = "='Dashboard M16 EEPS'!I5"
    @eval_fn
    def F7():
        i5_1 = Dashboard_M16_EEPS.I5()
        return i5_1

@register(Charts_M16)
class G7():
    # 'Charts_M16'!G7
    value = 2002
    formula = "='Dashboard M16 EEPS'!J5"
    @eval_fn
    def G7():
        j5_1 = Dashboard_M16_EEPS.J5()
        return j5_1

@register(Charts_M16)
class H7():
    # 'Charts_M16'!H7
    value = 2003
    formula = "='Dashboard M16 EEPS'!K5"
    @eval_fn
    def H7():
        k5_1 = Dashboard_M16_EEPS.K5()
        return k5_1

@register(Charts_M16)
class I7():
    # 'Charts_M16'!I7
    value = 2004
    formula = "='Dashboard M16 EEPS'!L5"
    @eval_fn
    def I7():
        l5_1 = Dashboard_M16_EEPS.L5()
        return l5_1

@register(Charts_M16)
class J7():
    # 'Charts_M16'!J7
    value = 2005
    formula = "='Dashboard M16 EEPS'!M5"
    @eval_fn
    def J7():
        m5_1 = Dashboard_M16_EEPS.M5()
        return m5_1

@register(Charts_M16)
class K7():
    # 'Charts_M16'!K7
    value = 2006
    formula = "='Dashboard M16 EEPS'!N5"
    @eval_fn
    def K7():
        n5_1 = Dashboard_M16_EEPS.N5()
        return n5_1

@register(Charts_M16)
class L7():
    # 'Charts_M16'!L7
    value = 2007
    formula = "='Dashboard M16 EEPS'!O5"
    @eval_fn
    def L7():
        o5_1 = Dashboard_M16_EEPS.O5()
        return o5_1

@register(Charts_M16)
class M7():
    # 'Charts_M16'!M7
    value = 2008
    formula = "='Dashboard M16 EEPS'!P5"
    @eval_fn
    def M7():
        p5_1 = Dashboard_M16_EEPS.P5()
        return p5_1

@register(Charts_M16)
class N7():
    # 'Charts_M16'!N7
    value = 2009
    formula = "='Dashboard M16 EEPS'!Q5"
    @eval_fn
    def N7():
        q5_1 = Dashboard_M16_EEPS.Q5()
        return q5_1

@register(Charts_M16)
class O7():
    # 'Charts_M16'!O7
    value = 2010
    formula = "='Dashboard M16 EEPS'!R5"
    @eval_fn
    def O7():
        r5_1 = Dashboard_M16_EEPS.R5()
        return r5_1

@register(Charts_M16)
class P7():
    # 'Charts_M16'!P7
    value = 2011
    formula = "='Dashboard M16 EEPS'!S5"
    @eval_fn
    def P7():
        s5_1 = Dashboard_M16_EEPS.S5()
        return s5_1

@register(Charts_M16)
class B8():
    # 'Charts_M16'!B8
    value = "HECO"
    formula = "='Charts Data M16'!D3"
    @eval_fn
    def B8():
        d3_1 = Charts_Data_M16.D3()
        return d3_1

@register(Charts_M16)
class D8():
    # 'Charts_M16'!D8
    value = "#N/A"
    formula = "='Charts Data M16'!G3"
    @eval_fn
    def D8():
        g3_1 = Charts_Data_M16.G3()
        return g3_1

@register(Charts_M16)
class E8():
    # 'Charts_M16'!E8
    value = "#N/A"
    formula = "='Charts Data M16'!H3"
    @eval_fn
    def E8():
        h3_1 = Charts_Data_M16.H3()
        return h3_1

@register(Charts_M16)
class F8():
    # 'Charts_M16'!F8
    value = "#N/A"
    formula = "='Charts Data M16'!I3"
    @eval_fn
    def F8():
        i3_1 = Charts_Data_M16.I3()
        return i3_1

@register(Charts_M16)
class G8():
    # 'Charts_M16'!G8
    value = "#N/A"
    formula = "='Charts Data M16'!J3"
    @eval_fn
    def G8():
        j3_1 = Charts_Data_M16.J3()
        return j3_1

@register(Charts_M16)
class H8():
    # 'Charts_M16'!H8
    value = "#N/A"
    formula = "='Charts Data M16'!K3"
    @eval_fn
    def H8():
        k3_1 = Charts_Data_M16.K3()
        return k3_1

@register(Charts_M16)
class I8():
    # 'Charts_M16'!I8
    value = "#N/A"
    formula = "='Charts Data M16'!L3"
    @eval_fn
    def I8():
        l3_1 = Charts_Data_M16.L3()
        return l3_1

@register(Charts_M16)
class J8():
    # 'Charts_M16'!J8
    value = 292000
    formula = "='Charts Data M16'!M3"
    @eval_fn
    def J8():
        m3_1 = Charts_Data_M16.M3()
        return m3_1

@register(Charts_M16)
class K8():
    # 'Charts_M16'!K8
    value = 340000
    formula = "='Charts Data M16'!N3"
    @eval_fn
    def K8():
        n3_1 = Charts_Data_M16.N3()
        return n3_1

@register(Charts_M16)
class L8():
    # 'Charts_M16'!L8
    value = 453000
    formula = "='Charts Data M16'!O3"
    @eval_fn
    def L8():
        o3_1 = Charts_Data_M16.O3()
        return o3_1

@register(Charts_M16)
class M8():
    # 'Charts_M16'!M8
    value = 604007
    formula = "='Charts Data M16'!P3"
    @eval_fn
    def M8():
        p3_1 = Charts_Data_M16.P3()
        return p3_1

@register(Charts_M16)
class N8():
    # 'Charts_M16'!N8
    value = 651278
    formula = "='Charts Data M16'!Q3"
    @eval_fn
    def N8():
        q3_1 = Charts_Data_M16.Q3()
        return q3_1

@register(Charts_M16)
class O8():
    # 'Charts_M16'!O8
    value = 738337
    formula = "='Charts Data M16'!R3"
    @eval_fn
    def O8():
        r3_1 = Charts_Data_M16.R3()
        return r3_1

@register(Charts_M16)
class P8():
    # 'Charts_M16'!P8
    value = 821136
    formula = "='Charts Data M16'!S3"
    @eval_fn
    def P8():
        s3_1 = Charts_Data_M16.S3()
        return s3_1

@register(Charts_M16)
class B9():
    # 'Charts_M16'!B9
    value = "HELCO"
    formula = "='Charts Data M16'!D4"
    @eval_fn
    def B9():
        d4_1 = Charts_Data_M16.D4()
        return d4_1

@register(Charts_M16)
class D9():
    # 'Charts_M16'!D9
    value = "#N/A"
    formula = "='Charts Data M16'!G4"
    @eval_fn
    def D9():
        g4_1 = Charts_Data_M16.G4()
        return g4_1

@register(Charts_M16)
class E9():
    # 'Charts_M16'!E9
    value = "#N/A"
    formula = "='Charts Data M16'!H4"
    @eval_fn
    def E9():
        h4_1 = Charts_Data_M16.H4()
        return h4_1

@register(Charts_M16)
class F9():
    # 'Charts_M16'!F9
    value = "#N/A"
    formula = "='Charts Data M16'!I4"
    @eval_fn
    def F9():
        i4_1 = Charts_Data_M16.I4()
        return i4_1

@register(Charts_M16)
class G9():
    # 'Charts_M16'!G9
    value = "#N/A"
    formula = "='Charts Data M16'!J4"
    @eval_fn
    def G9():
        j4_1 = Charts_Data_M16.J4()
        return j4_1

@register(Charts_M16)
class H9():
    # 'Charts_M16'!H9
    value = "#N/A"
    formula = "='Charts Data M16'!K4"
    @eval_fn
    def H9():
        k4_1 = Charts_Data_M16.K4()
        return k4_1

@register(Charts_M16)
class I9():
    # 'Charts_M16'!I9
    value = "#N/A"
    formula = "='Charts Data M16'!L4"
    @eval_fn
    def I9():
        l4_1 = Charts_Data_M16.L4()
        return l4_1

@register(Charts_M16)
class J9():
    # 'Charts_M16'!J9
    value = 49000
    formula = "='Charts Data M16'!M4"
    @eval_fn
    def J9():
        m4_1 = Charts_Data_M16.M4()
        return m4_1

@register(Charts_M16)
class K9():
    # 'Charts_M16'!K9
    value = 54000
    formula = "='Charts Data M16'!N4"
    @eval_fn
    def K9():
        n4_1 = Charts_Data_M16.N4()
        return n4_1

@register(Charts_M16)
class L9():
    # 'Charts_M16'!L9
    value = 57000
    formula = "='Charts Data M16'!O4"
    @eval_fn
    def L9():
        o4_1 = Charts_Data_M16.O4()
        return o4_1

@register(Charts_M16)
class M9():
    # 'Charts_M16'!M9
    value = 47051
    formula = "='Charts Data M16'!P4"
    @eval_fn
    def M9():
        p4_1 = Charts_Data_M16.P4()
        return p4_1

@register(Charts_M16)
class N9():
    # 'Charts_M16'!N9
    value = 49760
    formula = "='Charts Data M16'!Q4"
    @eval_fn
    def N9():
        q4_1 = Charts_Data_M16.Q4()
        return q4_1

@register(Charts_M16)
class O9():
    # 'Charts_M16'!O9
    value = 62359
    formula = "='Charts Data M16'!R4"
    @eval_fn
    def O9():
        r4_1 = Charts_Data_M16.R4()
        return r4_1

@register(Charts_M16)
class P9():
    # 'Charts_M16'!P9
    value = 76622
    formula = "='Charts Data M16'!S4"
    @eval_fn
    def P9():
        s4_1 = Charts_Data_M16.S4()
        return s4_1

@register(Charts_M16)
class B10():
    # 'Charts_M16'!B10
    value = "MECO"
    formula = "='Charts Data M16'!D5"
    @eval_fn
    def B10():
        d5_1 = Charts_Data_M16.D5()
        return d5_1

@register(Charts_M16)
class D10():
    # 'Charts_M16'!D10
    value = "#N/A"
    formula = "='Charts Data M16'!G5"
    @eval_fn
    def D10():
        g5_1 = Charts_Data_M16.G5()
        return g5_1

@register(Charts_M16)
class E10():
    # 'Charts_M16'!E10
    value = "#N/A"
    formula = "='Charts Data M16'!H5"
    @eval_fn
    def E10():
        h5_1 = Charts_Data_M16.H5()
        return h5_1

@register(Charts_M16)
class F10():
    # 'Charts_M16'!F10
    value = "#N/A"
    formula = "='Charts Data M16'!I5"
    @eval_fn
    def F10():
        i5_1 = Charts_Data_M16.I5()
        return i5_1

@register(Charts_M16)
class G10():
    # 'Charts_M16'!G10
    value = "#N/A"
    formula = "='Charts Data M16'!J5"
    @eval_fn
    def G10():
        j5_1 = Charts_Data_M16.J5()
        return j5_1

@register(Charts_M16)
class H10():
    # 'Charts_M16'!H10
    value = "#N/A"
    formula = "='Charts Data M16'!K5"
    @eval_fn
    def H10():
        k5_1 = Charts_Data_M16.K5()
        return k5_1

@register(Charts_M16)
class I10():
    # 'Charts_M16'!I10
    value = "#N/A"
    formula = "='Charts Data M16'!L5"
    @eval_fn
    def I10():
        l5_1 = Charts_Data_M16.L5()
        return l5_1

@register(Charts_M16)
class J10():
    # 'Charts_M16'!J10
    value = 77000
    formula = "='Charts Data M16'!M5"
    @eval_fn
    def J10():
        m5_1 = Charts_Data_M16.M5()
        return m5_1

@register(Charts_M16)
class K10():
    # 'Charts_M16'!K10
    value = 82000
    formula = "='Charts Data M16'!N5"
    @eval_fn
    def K10():
        n5_1 = Charts_Data_M16.N5()
        return n5_1

@register(Charts_M16)
class L10():
    # 'Charts_M16'!L10
    value = 88000
    formula = "='Charts Data M16'!O5"
    @eval_fn
    def L10():
        o5_1 = Charts_Data_M16.O5()
        return o5_1

@register(Charts_M16)
class M10():
    # 'Charts_M16'!M10
    value = 79835
    formula = "='Charts Data M16'!P5"
    @eval_fn
    def M10():
        p5_1 = Charts_Data_M16.P5()
        return p5_1

@register(Charts_M16)
class N10():
    # 'Charts_M16'!N10
    value = 88593
    formula = "='Charts Data M16'!Q5"
    @eval_fn
    def N10():
        q5_1 = Charts_Data_M16.Q5()
        return q5_1

@register(Charts_M16)
class O10():
    # 'Charts_M16'!O10
    value = 98813
    formula = "='Charts Data M16'!R5"
    @eval_fn
    def O10():
        r5_1 = Charts_Data_M16.R5()
        return r5_1

@register(Charts_M16)
class P10():
    # 'Charts_M16'!P10
    value = 111306
    formula = "='Charts Data M16'!S5"
    @eval_fn
    def P10():
        s5_1 = Charts_Data_M16.S5()
        return s5_1

@register(Charts_M16)
class B11():
    # 'Charts_M16'!B11
    value = "KIUC"
    formula = "='Charts Data M16'!D6"
    @eval_fn
    def B11():
        d6_1 = Charts_Data_M16.D6()
        return d6_1

@register(Charts_M16)
class D11():
    # 'Charts_M16'!D11
    value = "#N/A"
    formula = "='Charts Data M16'!G6"
    @eval_fn
    def D11():
        g6_1 = Charts_Data_M16.G6()
        return g6_1

@register(Charts_M16)
class E11():
    # 'Charts_M16'!E11
    value = "#N/A"
    formula = "='Charts Data M16'!H6"
    @eval_fn
    def E11():
        h6_1 = Charts_Data_M16.H6()
        return h6_1

@register(Charts_M16)
class F11():
    # 'Charts_M16'!F11
    value = "#N/A"
    formula = "='Charts Data M16'!I6"
    @eval_fn
    def F11():
        i6_1 = Charts_Data_M16.I6()
        return i6_1

@register(Charts_M16)
class G11():
    # 'Charts_M16'!G11
    value = "#N/A"
    formula = "='Charts Data M16'!J6"
    @eval_fn
    def G11():
        j6_1 = Charts_Data_M16.J6()
        return j6_1

@register(Charts_M16)
class H11():
    # 'Charts_M16'!H11
    value = "#N/A"
    formula = "='Charts Data M16'!K6"
    @eval_fn
    def H11():
        k6_1 = Charts_Data_M16.K6()
        return k6_1

@register(Charts_M16)
class I11():
    # 'Charts_M16'!I11
    value = 19037
    formula = "='Charts Data M16'!L6"
    @eval_fn
    def I11():
        l6_1 = Charts_Data_M16.L6()
        return l6_1

@register(Charts_M16)
class J11():
    # 'Charts_M16'!J11
    value = 20855
    formula = "='Charts Data M16'!M6"
    @eval_fn
    def J11():
        m6_1 = Charts_Data_M16.M6()
        return m6_1

@register(Charts_M16)
class K11():
    # 'Charts_M16'!K11
    value = 21349
    formula = "='Charts Data M16'!N6"
    @eval_fn
    def K11():
        n6_1 = Charts_Data_M16.N6()
        return n6_1

@register(Charts_M16)
class L11():
    # 'Charts_M16'!L11
    value = 21361
    formula = "='Charts Data M16'!O6"
    @eval_fn
    def L11():
        o6_1 = Charts_Data_M16.O6()
        return o6_1

@register(Charts_M16)
class M11():
    # 'Charts_M16'!M11
    value = 19233
    formula = "='Charts Data M16'!P6"
    @eval_fn
    def M11():
        p6_1 = Charts_Data_M16.P6()
        return p6_1

@register(Charts_M16)
class N11():
    # 'Charts_M16'!N11
    value = 19217
    formula = "='Charts Data M16'!Q6"
    @eval_fn
    def N11():
        q6_1 = Charts_Data_M16.Q6()
        return q6_1

@register(Charts_M16)
class O11():
    # 'Charts_M16'!O11
    value = 16911
    formula = "='Charts Data M16'!R6"
    @eval_fn
    def O11():
        r6_1 = Charts_Data_M16.R6()
        return r6_1

@register(Charts_M16)
class P11():
    # 'Charts_M16'!P11
    value = 18264
    formula = "='Charts Data M16'!S6"
    @eval_fn
    def P11():
        s6_1 = Charts_Data_M16.S6()
        return s6_1

@register(Charts_M16)
class B12():
    # 'Charts_M16'!B12
    value = "Total"
    formula = "='Charts Data M16'!D7"
    @eval_fn
    def B12():
        d7_1 = Charts_Data_M16.D7()
        return d7_1

@register(Charts_M16)
class D12():
    # 'Charts_M16'!D12
    value = "#N/A"
    formula = "='Charts Data M16'!G7"
    @eval_fn
    def D12():
        g7_1 = Charts_Data_M16.G7()
        return g7_1

@register(Charts_M16)
class E12():
    # 'Charts_M16'!E12
    value = "#N/A"
    formula = "='Charts Data M16'!H7"
    @eval_fn
    def E12():
        h7_1 = Charts_Data_M16.H7()
        return h7_1

@register(Charts_M16)
class F12():
    # 'Charts_M16'!F12
    value = "#N/A"
    formula = "='Charts Data M16'!I7"
    @eval_fn
    def F12():
        i7_1 = Charts_Data_M16.I7()
        return i7_1

@register(Charts_M16)
class G12():
    # 'Charts_M16'!G12
    value = "#N/A"
    formula = "='Charts Data M16'!J7"
    @eval_fn
    def G12():
        j7_1 = Charts_Data_M16.J7()
        return j7_1

@register(Charts_M16)
class H12():
    # 'Charts_M16'!H12
    value = "#N/A"
    formula = "='Charts Data M16'!K7"
    @eval_fn
    def H12():
        k7_1 = Charts_Data_M16.K7()
        return k7_1

@register(Charts_M16)
class I12():
    # 'Charts_M16'!I12
    value = 19037
    formula = "='Charts Data M16'!L7"
    @eval_fn
    def I12():
        l7_1 = Charts_Data_M16.L7()
        return l7_1

@register(Charts_M16)
class J12():
    # 'Charts_M16'!J12
    value = 438855
    formula = "='Charts Data M16'!M7"
    @eval_fn
    def J12():
        m7_1 = Charts_Data_M16.M7()
        return m7_1

@register(Charts_M16)
class K12():
    # 'Charts_M16'!K12
    value = 497349
    formula = "='Charts Data M16'!N7"
    @eval_fn
    def K12():
        n7_1 = Charts_Data_M16.N7()
        return n7_1

@register(Charts_M16)
class L12():
    # 'Charts_M16'!L12
    value = 619361
    formula = "='Charts Data M16'!O7"
    @eval_fn
    def L12():
        o7_1 = Charts_Data_M16.O7()
        return o7_1

@register(Charts_M16)
class M12():
    # 'Charts_M16'!M12
    value = 750126
    formula = "='Charts Data M16'!P7"
    @eval_fn
    def M12():
        p7_1 = Charts_Data_M16.P7()
        return p7_1

@register(Charts_M16)
class N12():
    # 'Charts_M16'!N12
    value = 808848
    formula = "='Charts Data M16'!Q7"
    @eval_fn
    def N12():
        q7_1 = Charts_Data_M16.Q7()
        return q7_1

@register(Charts_M16)
class O12():
    # 'Charts_M16'!O12
    value = 916420
    formula = "='Charts Data M16'!R7"
    @eval_fn
    def O12():
        r7_1 = Charts_Data_M16.R7()
        return r7_1

@register(Charts_M16)
class P12():
    # 'Charts_M16'!P12
    value = 1027328
    formula = "='Charts Data M16'!S7"
    @eval_fn
    def P12():
        s7_1 = Charts_Data_M16.S7()
        return s7_1

@register(Charts_M16)
class B14():
    # 'Charts_M16'!B14
    value = "Electricity Saved Annually"

@register(Charts_M16)
class N14():
    # 'Charts_M16'!N14
    value = "Total Hawaii Generation and Energy Efficiency"

@register(Charts_M16)
class B26():
    # 'Charts_M16'!B26
    value = "Electricity Saved in 2009"
    formula = "='Charts Data M16'!$B$2"
    @eval_fn
    def B26():
        b2_1 = Charts_Data_M16.B2()
        return b2_1

@register(Charts_M16)
class B28():
    # 'Charts_M16'!B28
    value = 11