# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Input_EIA_New_Plants = Worksheet('Input_EIA_New_Plants', 10, 10)



@register(Input_EIA_New_Plants)
class B1():
    # 'Input_EIA_New_Plants'!B1
    value = "Generating Unit Additions in the United States by State, 2003-2012"

@register(Input_EIA_New_Plants)
class B2():
    # 'Input_EIA_New_Plants'!B2
    value = "Note: Descriptions of field names and codes can be obtained from the record layout in the Form EIA-860 source data file at www.eia.gov/cneaf/electricity/page/eia860.html."

@register(Input_EIA_New_Plants)
class B3():
    # 'Input_EIA_New_Plants'!B3
    value = '''Source: U.S. Energy Information Administration, Form EIA-860, "Annual Electric Generator Report."'''

@register(Input_EIA_New_Plants)
class B4():
    # 'Input_EIA_New_Plants'!B4
    value = "http://www.eia.gov/electricity/capacity/"

@register(Input_EIA_New_Plants)
class B5():
    # 'Input_EIA_New_Plants'!B5
    value = "State"

@register(Input_EIA_New_Plants)
class C5():
    # 'Input_EIA_New_Plants'!C5
    value = "County"

@register(Input_EIA_New_Plants)
class D5():
    # 'Input_EIA_New_Plants'!D5
    value = "Utility ID"

@register(Input_EIA_New_Plants)
class E5():
    # 'Input_EIA_New_Plants'!E5
    value = "Company"

@register(Input_EIA_New_Plants)
class F5():
    # 'Input_EIA_New_Plants'!F5
    value = "Plant ID"

@register(Input_EIA_New_Plants)
class G5():
    # 'Input_EIA_New_Plants'!G5
    value = "Plant Name"

@register(Input_EIA_New_Plants)
class H5():
    # 'Input_EIA_New_Plants'!H5
    value = "Generator ID"

@register(Input_EIA_New_Plants)
class I5():
    # 'Input_EIA_New_Plants'!I5
    value = "Unit Code"

@register(Input_EIA_New_Plants)
class J5():
    # 'Input_EIA_New_Plants'!J5
    value = "Unit Status"

@register(Input_EIA_New_Plants)
class K5():
    # 'Input_EIA_New_Plants'!K5
    value = "Nameplate Capacity (Megawatts) "

@register(Input_EIA_New_Plants)
class L5():
    # 'Input_EIA_New_Plants'!L5
    value = "Summer Capacity (Megawatts)"

@register(Input_EIA_New_Plants)
class M5():
    # 'Input_EIA_New_Plants'!M5
    value = "Winter Capacity (Megawatts)"

@register(Input_EIA_New_Plants)
class N5():
    # 'Input_EIA_New_Plants'!N5
    value = "Primary Purpose Code"

@register(Input_EIA_New_Plants)
class O5():
    # 'Input_EIA_New_Plants'!O5
    value = "Prime Mover"

@register(Input_EIA_New_Plants)
class P5():
    # 'Input_EIA_New_Plants'!P5
    value = "Energy Source 1"

@register(Input_EIA_New_Plants)
class Q5():
    # 'Input_EIA_New_Plants'!Q5
    value = "Energy Source 2"

@register(Input_EIA_New_Plants)
class R5():
    # 'Input_EIA_New_Plants'!R5
    value = "Initial Month of Operation"

@register(Input_EIA_New_Plants)
class S5():
    # 'Input_EIA_New_Plants'!S5
    value = "Initial Year of Operation"

@register(Input_EIA_New_Plants)
class T5():
    # 'Input_EIA_New_Plants'!T5
    value = "Number of Wind Turbines"

@register(Input_EIA_New_Plants)
class U5():
    # 'Input_EIA_New_Plants'!U5
    value = "Multigenerator Code"

@register(Input_EIA_New_Plants)
class A6():
    # 'Input_EIA_New_Plants'!A6
    value = "Distillate Fuel Oil2004"
    formula = "=V6&S6"
    @eval_fn
    def A6():
        v6_1 = Input_EIA_New_Plants.V6()
        s6_1 = Input_EIA_New_Plants.S6()
        var_1 = concat(v6_1, s6_1)
        return var_1

@register(Input_EIA_New_Plants)
class B6():
    # 'Input_EIA_New_Plants'!B6
    value = "HI"

@register(Input_EIA_New_Plants)
class C6():
    # 'Input_EIA_New_Plants'!C6
    value = "Hawaii"

@register(Input_EIA_New_Plants)
class D6():
    # 'Input_EIA_New_Plants'!D6
    value = 8287

@register(Input_EIA_New_Plants)
class E6():
    # 'Input_EIA_New_Plants'!E6
    value = "Hawaii Electric Light Co Inc"

@register(Input_EIA_New_Plants)
class F6():
    # 'Input_EIA_New_Plants'!F6
    value = 8083

@register(Input_EIA_New_Plants)
class G6():
    # 'Input_EIA_New_Plants'!G6
    value = "Keahole"

@register(Input_EIA_New_Plants)
class H6():
    # 'Input_EIA_New_Plants'!H6
    value = "CT4"

@register(Input_EIA_New_Plants)
class J6():
    # 'Input_EIA_New_Plants'!J6
    value = "OP"

@register(Input_EIA_New_Plants)
class K6():
    # 'Input_EIA_New_Plants'!K6
    value = 23

@register(Input_EIA_New_Plants)
class L6():
    # 'Input_EIA_New_Plants'!L6
    value = 19.8

@register(Input_EIA_New_Plants)
class M6():
    # 'Input_EIA_New_Plants'!M6
    value = 21.6

@register(Input_EIA_New_Plants)
class N6():
    # 'Input_EIA_New_Plants'!N6
    value = 22

@register(Input_EIA_New_Plants)
class O6():
    # 'Input_EIA_New_Plants'!O6
    value = "CT"

@register(Input_EIA_New_Plants)
class P6():
    # 'Input_EIA_New_Plants'!P6
    value = "DFO"

@register(Input_EIA_New_Plants)
class R6():
    # 'Input_EIA_New_Plants'!R6
    value = 5

@register(Input_EIA_New_Plants)
class S6():
    # 'Input_EIA_New_Plants'!S6
    value = 2004

@register(Input_EIA_New_Plants)
class V6():
    # 'Input_EIA_New_Plants'!V6
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A7():
    # 'Input_EIA_New_Plants'!A7
    value = "Distillate Fuel Oil2004"
    formula = "=V7&S7"
    @eval_fn
    def A7():
        v7_1 = Input_EIA_New_Plants.V7()
        s7_1 = Input_EIA_New_Plants.S7()
        var_1 = concat(v7_1, s7_1)
        return var_1

@register(Input_EIA_New_Plants)
class B7():
    # 'Input_EIA_New_Plants'!B7
    value = "HI"

@register(Input_EIA_New_Plants)
class C7():
    # 'Input_EIA_New_Plants'!C7
    value = "Hawaii"

@register(Input_EIA_New_Plants)
class D7():
    # 'Input_EIA_New_Plants'!D7
    value = 8287

@register(Input_EIA_New_Plants)
class E7():
    # 'Input_EIA_New_Plants'!E7
    value = "Hawaii Electric Light Co Inc"

@register(Input_EIA_New_Plants)
class F7():
    # 'Input_EIA_New_Plants'!F7
    value = 8083

@register(Input_EIA_New_Plants)
class G7():
    # 'Input_EIA_New_Plants'!G7
    value = "Keahole"

@register(Input_EIA_New_Plants)
class H7():
    # 'Input_EIA_New_Plants'!H7
    value = "CT5"

@register(Input_EIA_New_Plants)
class J7():
    # 'Input_EIA_New_Plants'!J7
    value = "OP"

@register(Input_EIA_New_Plants)
class K7():
    # 'Input_EIA_New_Plants'!K7
    value = 23

@register(Input_EIA_New_Plants)
class L7():
    # 'Input_EIA_New_Plants'!L7
    value = 19.8

@register(Input_EIA_New_Plants)
class M7():
    # 'Input_EIA_New_Plants'!M7
    value = 21.6

@register(Input_EIA_New_Plants)
class N7():
    # 'Input_EIA_New_Plants'!N7
    value = 22

@register(Input_EIA_New_Plants)
class O7():
    # 'Input_EIA_New_Plants'!O7
    value = "CT"

@register(Input_EIA_New_Plants)
class P7():
    # 'Input_EIA_New_Plants'!P7
    value = "DFO"

@register(Input_EIA_New_Plants)
class R7():
    # 'Input_EIA_New_Plants'!R7
    value = 6

@register(Input_EIA_New_Plants)
class S7():
    # 'Input_EIA_New_Plants'!S7
    value = 2004

@register(Input_EIA_New_Plants)
class V7():
    # 'Input_EIA_New_Plants'!V7
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A8():
    # 'Input_EIA_New_Plants'!A8
    value = "Hydroelectric2005"
    formula = "=V8&S8"
    @eval_fn
    def A8():
        v8_1 = Input_EIA_New_Plants.V8()
        s8_1 = Input_EIA_New_Plants.S8()
        var_1 = concat(v8_1, s8_1)
        return var_1

@register(Input_EIA_New_Plants)
class B8():
    # 'Input_EIA_New_Plants'!B8
    value = "HI"

@register(Input_EIA_New_Plants)
class C8():
    # 'Input_EIA_New_Plants'!C8
    value = "Hawaii"

@register(Input_EIA_New_Plants)
class D8():
    # 'Input_EIA_New_Plants'!D8
    value = 8287

@register(Input_EIA_New_Plants)
class E8():
    # 'Input_EIA_New_Plants'!E8
    value = "Hawaii Electric Light Co Inc"

@register(Input_EIA_New_Plants)
class F8():
    # 'Input_EIA_New_Plants'!F8
    value = 771

@register(Input_EIA_New_Plants)
class G8():
    # 'Input_EIA_New_Plants'!G8
    value = "Puueo"

@register(Input_EIA_New_Plants)
class H8():
    # 'Input_EIA_New_Plants'!H8
    value = "2A"

@register(Input_EIA_New_Plants)
class J8():
    # 'Input_EIA_New_Plants'!J8
    value = "OP"

@register(Input_EIA_New_Plants)
class K8():
    # 'Input_EIA_New_Plants'!K8
    value = 2.4

@register(Input_EIA_New_Plants)
class L8():
    # 'Input_EIA_New_Plants'!L8
    value = 2.4

@register(Input_EIA_New_Plants)
class M8():
    # 'Input_EIA_New_Plants'!M8
    value = 2.4

@register(Input_EIA_New_Plants)
class N8():
    # 'Input_EIA_New_Plants'!N8
    value = 22

@register(Input_EIA_New_Plants)
class O8():
    # 'Input_EIA_New_Plants'!O8
    value = "HY"

@register(Input_EIA_New_Plants)
class P8():
    # 'Input_EIA_New_Plants'!P8
    value = "WAT"

@register(Input_EIA_New_Plants)
class R8():
    # 'Input_EIA_New_Plants'!R8
    value = 10

@register(Input_EIA_New_Plants)
class S8():
    # 'Input_EIA_New_Plants'!S8
    value = 2005

@register(Input_EIA_New_Plants)
class V8():
    # 'Input_EIA_New_Plants'!V8
    value = "Hydroelectric"

@register(Input_EIA_New_Plants)
class A9():
    # 'Input_EIA_New_Plants'!A9
    value = "Distillate Fuel Oil2005"
    formula = "=V9&S9"
    @eval_fn
    def A9():
        v9_1 = Input_EIA_New_Plants.V9()
        s9_1 = Input_EIA_New_Plants.S9()
        var_1 = concat(v9_1, s9_1)
        return var_1

@register(Input_EIA_New_Plants)
class B9():
    # 'Input_EIA_New_Plants'!B9
    value = "HI"

@register(Input_EIA_New_Plants)
class C9():
    # 'Input_EIA_New_Plants'!C9
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D9():
    # 'Input_EIA_New_Plants'!D9
    value = 19547

@register(Input_EIA_New_Plants)
class E9():
    # 'Input_EIA_New_Plants'!E9
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F9():
    # 'Input_EIA_New_Plants'!F9
    value = 56330

@register(Input_EIA_New_Plants)
class G9():
    # 'Input_EIA_New_Plants'!G9
    value = "Ewa Nui Substation DG"

@register(Input_EIA_New_Plants)
class H9():
    # 'Input_EIA_New_Plants'!H9
    value = "DG1"

@register(Input_EIA_New_Plants)
class J9():
    # 'Input_EIA_New_Plants'!J9
    value = "SB"

@register(Input_EIA_New_Plants)
class K9():
    # 'Input_EIA_New_Plants'!K9
    value = 1.6

@register(Input_EIA_New_Plants)
class L9():
    # 'Input_EIA_New_Plants'!L9
    value = 1.64

@register(Input_EIA_New_Plants)
class M9():
    # 'Input_EIA_New_Plants'!M9
    value = 1.64

@register(Input_EIA_New_Plants)
class N9():
    # 'Input_EIA_New_Plants'!N9
    value = 22

@register(Input_EIA_New_Plants)
class O9():
    # 'Input_EIA_New_Plants'!O9
    value = "IC"

@register(Input_EIA_New_Plants)
class P9():
    # 'Input_EIA_New_Plants'!P9
    value = "DFO"

@register(Input_EIA_New_Plants)
class R9():
    # 'Input_EIA_New_Plants'!R9
    value = 10

@register(Input_EIA_New_Plants)
class S9():
    # 'Input_EIA_New_Plants'!S9
    value = 2005

@register(Input_EIA_New_Plants)
class V9():
    # 'Input_EIA_New_Plants'!V9
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A10():
    # 'Input_EIA_New_Plants'!A10
    value = "Distillate Fuel Oil2005"
    formula = "=V10&S10"
    @eval_fn
    def A10():
        v10_1 = Input_EIA_New_Plants.V10()
        s10_1 = Input_EIA_New_Plants.S10()
        var_1 = concat(v10_1, s10_1)
        return var_1

@register(Input_EIA_New_Plants)
class B10():
    # 'Input_EIA_New_Plants'!B10
    value = "HI"

@register(Input_EIA_New_Plants)
class C10():
    # 'Input_EIA_New_Plants'!C10
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D10():
    # 'Input_EIA_New_Plants'!D10
    value = 19547

@register(Input_EIA_New_Plants)
class E10():
    # 'Input_EIA_New_Plants'!E10
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F10():
    # 'Input_EIA_New_Plants'!F10
    value = 56330

@register(Input_EIA_New_Plants)
class G10():
    # 'Input_EIA_New_Plants'!G10
    value = "Ewa Nui Substation DG"

@register(Input_EIA_New_Plants)
class H10():
    # 'Input_EIA_New_Plants'!H10
    value = "DG2"

@register(Input_EIA_New_Plants)
class J10():
    # 'Input_EIA_New_Plants'!J10
    value = "SB"

@register(Input_EIA_New_Plants)
class K10():
    # 'Input_EIA_New_Plants'!K10
    value = 1.6

@register(Input_EIA_New_Plants)
class L10():
    # 'Input_EIA_New_Plants'!L10
    value = 1.64

@register(Input_EIA_New_Plants)
class M10():
    # 'Input_EIA_New_Plants'!M10
    value = 1.64

@register(Input_EIA_New_Plants)
class N10():
    # 'Input_EIA_New_Plants'!N10
    value = 22

@register(Input_EIA_New_Plants)
class O10():
    # 'Input_EIA_New_Plants'!O10
    value = "IC"

@register(Input_EIA_New_Plants)
class P10():
    # 'Input_EIA_New_Plants'!P10
    value = "DFO"

@register(Input_EIA_New_Plants)
class R10():
    # 'Input_EIA_New_Plants'!R10
    value = 10

@register(Input_EIA_New_Plants)
class S10():
    # 'Input_EIA_New_Plants'!S10
    value = 2005

@register(Input_EIA_New_Plants)
class V10():
    # 'Input_EIA_New_Plants'!V10
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A11():
    # 'Input_EIA_New_Plants'!A11
    value = "Distillate Fuel Oil2005"
    formula = "=V11&S11"
    @eval_fn
    def A11():
        v11_1 = Input_EIA_New_Plants.V11()
        s11_1 = Input_EIA_New_Plants.S11()
        var_1 = concat(v11_1, s11_1)
        return var_1

@register(Input_EIA_New_Plants)
class B11():
    # 'Input_EIA_New_Plants'!B11
    value = "HI"

@register(Input_EIA_New_Plants)
class C11():
    # 'Input_EIA_New_Plants'!C11
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D11():
    # 'Input_EIA_New_Plants'!D11
    value = 19547

@register(Input_EIA_New_Plants)
class E11():
    # 'Input_EIA_New_Plants'!E11
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F11():
    # 'Input_EIA_New_Plants'!F11
    value = 56330

@register(Input_EIA_New_Plants)
class G11():
    # 'Input_EIA_New_Plants'!G11
    value = "Ewa Nui Substation DG"

@register(Input_EIA_New_Plants)
class H11():
    # 'Input_EIA_New_Plants'!H11
    value = "DG3"

@register(Input_EIA_New_Plants)
class J11():
    # 'Input_EIA_New_Plants'!J11
    value = "SB"

@register(Input_EIA_New_Plants)
class K11():
    # 'Input_EIA_New_Plants'!K11
    value = 1.6

@register(Input_EIA_New_Plants)
class L11():
    # 'Input_EIA_New_Plants'!L11
    value = 1.64

@register(Input_EIA_New_Plants)
class M11():
    # 'Input_EIA_New_Plants'!M11
    value = 1.64

@register(Input_EIA_New_Plants)
class N11():
    # 'Input_EIA_New_Plants'!N11
    value = 22

@register(Input_EIA_New_Plants)
class O11():
    # 'Input_EIA_New_Plants'!O11
    value = "IC"

@register(Input_EIA_New_Plants)
class P11():
    # 'Input_EIA_New_Plants'!P11
    value = "DFO"

@register(Input_EIA_New_Plants)
class R11():
    # 'Input_EIA_New_Plants'!R11
    value = 10

@register(Input_EIA_New_Plants)
class S11():
    # 'Input_EIA_New_Plants'!S11
    value = 2005

@register(Input_EIA_New_Plants)
class V11():
    # 'Input_EIA_New_Plants'!V11
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A12():
    # 'Input_EIA_New_Plants'!A12
    value = "Distillate Fuel Oil2005"
    formula = "=V12&S12"
    @eval_fn
    def A12():
        v12_1 = Input_EIA_New_Plants.V12()
        s12_1 = Input_EIA_New_Plants.S12()
        var_1 = concat(v12_1, s12_1)
        return var_1

@register(Input_EIA_New_Plants)
class B12():
    # 'Input_EIA_New_Plants'!B12
    value = "HI"

@register(Input_EIA_New_Plants)
class C12():
    # 'Input_EIA_New_Plants'!C12
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D12():
    # 'Input_EIA_New_Plants'!D12
    value = 19547

@register(Input_EIA_New_Plants)
class E12():
    # 'Input_EIA_New_Plants'!E12
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F12():
    # 'Input_EIA_New_Plants'!F12
    value = 56332

@register(Input_EIA_New_Plants)
class G12():
    # 'Input_EIA_New_Plants'!G12
    value = "Helemano Substation DG"

@register(Input_EIA_New_Plants)
class H12():
    # 'Input_EIA_New_Plants'!H12
    value = "DG1"

@register(Input_EIA_New_Plants)
class J12():
    # 'Input_EIA_New_Plants'!J12
    value = "SB"

@register(Input_EIA_New_Plants)
class K12():
    # 'Input_EIA_New_Plants'!K12
    value = 1.6

@register(Input_EIA_New_Plants)
class L12():
    # 'Input_EIA_New_Plants'!L12
    value = 1.64

@register(Input_EIA_New_Plants)
class M12():
    # 'Input_EIA_New_Plants'!M12
    value = 1.64

@register(Input_EIA_New_Plants)
class N12():
    # 'Input_EIA_New_Plants'!N12
    value = 22

@register(Input_EIA_New_Plants)
class O12():
    # 'Input_EIA_New_Plants'!O12
    value = "IC"

@register(Input_EIA_New_Plants)
class P12():
    # 'Input_EIA_New_Plants'!P12
    value = "DFO"

@register(Input_EIA_New_Plants)
class R12():
    # 'Input_EIA_New_Plants'!R12
    value = 11

@register(Input_EIA_New_Plants)
class S12():
    # 'Input_EIA_New_Plants'!S12
    value = 2005

@register(Input_EIA_New_Plants)
class V12():
    # 'Input_EIA_New_Plants'!V12
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A13():
    # 'Input_EIA_New_Plants'!A13
    value = "Distillate Fuel Oil2005"
    formula = "=V13&S13"
    @eval_fn
    def A13():
        v13_1 = Input_EIA_New_Plants.V13()
        s13_1 = Input_EIA_New_Plants.S13()
        var_1 = concat(v13_1, s13_1)
        return var_1

@register(Input_EIA_New_Plants)
class B13():
    # 'Input_EIA_New_Plants'!B13
    value = "HI"

@register(Input_EIA_New_Plants)
class C13():
    # 'Input_EIA_New_Plants'!C13
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D13():
    # 'Input_EIA_New_Plants'!D13
    value = 19547

@register(Input_EIA_New_Plants)
class E13():
    # 'Input_EIA_New_Plants'!E13
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F13():
    # 'Input_EIA_New_Plants'!F13
    value = 56332

@register(Input_EIA_New_Plants)
class G13():
    # 'Input_EIA_New_Plants'!G13
    value = "Helemano Substation DG"

@register(Input_EIA_New_Plants)
class H13():
    # 'Input_EIA_New_Plants'!H13
    value = "DG2"

@register(Input_EIA_New_Plants)
class J13():
    # 'Input_EIA_New_Plants'!J13
    value = "SB"

@register(Input_EIA_New_Plants)
class K13():
    # 'Input_EIA_New_Plants'!K13
    value = 1.6

@register(Input_EIA_New_Plants)
class L13():
    # 'Input_EIA_New_Plants'!L13
    value = 1.64

@register(Input_EIA_New_Plants)
class M13():
    # 'Input_EIA_New_Plants'!M13
    value = 1.64

@register(Input_EIA_New_Plants)
class N13():
    # 'Input_EIA_New_Plants'!N13
    value = 22

@register(Input_EIA_New_Plants)
class O13():
    # 'Input_EIA_New_Plants'!O13
    value = "IC"

@register(Input_EIA_New_Plants)
class P13():
    # 'Input_EIA_New_Plants'!P13
    value = "DFO"

@register(Input_EIA_New_Plants)
class R13():
    # 'Input_EIA_New_Plants'!R13
    value = 11

@register(Input_EIA_New_Plants)
class S13():
    # 'Input_EIA_New_Plants'!S13
    value = 2005

@register(Input_EIA_New_Plants)
class V13():
    # 'Input_EIA_New_Plants'!V13
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A14():
    # 'Input_EIA_New_Plants'!A14
    value = "Distillate Fuel Oil2005"
    formula = "=V14&S14"
    @eval_fn
    def A14():
        v14_1 = Input_EIA_New_Plants.V14()
        s14_1 = Input_EIA_New_Plants.S14()
        var_1 = concat(v14_1, s14_1)
        return var_1

@register(Input_EIA_New_Plants)
class B14():
    # 'Input_EIA_New_Plants'!B14
    value = "HI"

@register(Input_EIA_New_Plants)
class C14():
    # 'Input_EIA_New_Plants'!C14
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D14():
    # 'Input_EIA_New_Plants'!D14
    value = 19547

@register(Input_EIA_New_Plants)
class E14():
    # 'Input_EIA_New_Plants'!E14
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F14():
    # 'Input_EIA_New_Plants'!F14
    value = 56332

@register(Input_EIA_New_Plants)
class G14():
    # 'Input_EIA_New_Plants'!G14
    value = "Helemano Substation DG"

@register(Input_EIA_New_Plants)
class H14():
    # 'Input_EIA_New_Plants'!H14
    value = "DG3"

@register(Input_EIA_New_Plants)
class J14():
    # 'Input_EIA_New_Plants'!J14
    value = "SB"

@register(Input_EIA_New_Plants)
class K14():
    # 'Input_EIA_New_Plants'!K14
    value = 1.6

@register(Input_EIA_New_Plants)
class L14():
    # 'Input_EIA_New_Plants'!L14
    value = 1.64

@register(Input_EIA_New_Plants)
class M14():
    # 'Input_EIA_New_Plants'!M14
    value = 1.64

@register(Input_EIA_New_Plants)
class N14():
    # 'Input_EIA_New_Plants'!N14
    value = 22

@register(Input_EIA_New_Plants)
class O14():
    # 'Input_EIA_New_Plants'!O14
    value = "IC"

@register(Input_EIA_New_Plants)
class P14():
    # 'Input_EIA_New_Plants'!P14
    value = "DFO"

@register(Input_EIA_New_Plants)
class R14():
    # 'Input_EIA_New_Plants'!R14
    value = 11

@register(Input_EIA_New_Plants)
class S14():
    # 'Input_EIA_New_Plants'!S14
    value = 2005

@register(Input_EIA_New_Plants)
class V14():
    # 'Input_EIA_New_Plants'!V14
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A15():
    # 'Input_EIA_New_Plants'!A15
    value = "Distillate Fuel Oil2005"
    formula = "=V15&S15"
    @eval_fn
    def A15():
        v15_1 = Input_EIA_New_Plants.V15()
        s15_1 = Input_EIA_New_Plants.S15()
        var_1 = concat(v15_1, s15_1)
        return var_1

@register(Input_EIA_New_Plants)
class B15():
    # 'Input_EIA_New_Plants'!B15
    value = "HI"

@register(Input_EIA_New_Plants)
class C15():
    # 'Input_EIA_New_Plants'!C15
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D15():
    # 'Input_EIA_New_Plants'!D15
    value = 19547

@register(Input_EIA_New_Plants)
class E15():
    # 'Input_EIA_New_Plants'!E15
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F15():
    # 'Input_EIA_New_Plants'!F15
    value = 56331

@register(Input_EIA_New_Plants)
class G15():
    # 'Input_EIA_New_Plants'!G15
    value = "Iwilei Tank Farm DG"

@register(Input_EIA_New_Plants)
class H15():
    # 'Input_EIA_New_Plants'!H15
    value = "DG1"

@register(Input_EIA_New_Plants)
class J15():
    # 'Input_EIA_New_Plants'!J15
    value = "SB"

@register(Input_EIA_New_Plants)
class K15():
    # 'Input_EIA_New_Plants'!K15
    value = 1.6

@register(Input_EIA_New_Plants)
class L15():
    # 'Input_EIA_New_Plants'!L15
    value = 1.64

@register(Input_EIA_New_Plants)
class M15():
    # 'Input_EIA_New_Plants'!M15
    value = 1.64

@register(Input_EIA_New_Plants)
class N15():
    # 'Input_EIA_New_Plants'!N15
    value = 22

@register(Input_EIA_New_Plants)
class O15():
    # 'Input_EIA_New_Plants'!O15
    value = "IC"

@register(Input_EIA_New_Plants)
class P15():
    # 'Input_EIA_New_Plants'!P15
    value = "DFO"

@register(Input_EIA_New_Plants)
class R15():
    # 'Input_EIA_New_Plants'!R15
    value = 11

@register(Input_EIA_New_Plants)
class S15():
    # 'Input_EIA_New_Plants'!S15
    value = 2005

@register(Input_EIA_New_Plants)
class V15():
    # 'Input_EIA_New_Plants'!V15
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A16():
    # 'Input_EIA_New_Plants'!A16
    value = "Distillate Fuel Oil2005"
    formula = "=V16&S16"
    @eval_fn
    def A16():
        v16_1 = Input_EIA_New_Plants.V16()
        s16_1 = Input_EIA_New_Plants.S16()
        var_1 = concat(v16_1, s16_1)
        return var_1

@register(Input_EIA_New_Plants)
class B16():
    # 'Input_EIA_New_Plants'!B16
    value = "HI"

@register(Input_EIA_New_Plants)
class C16():
    # 'Input_EIA_New_Plants'!C16
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D16():
    # 'Input_EIA_New_Plants'!D16
    value = 19547

@register(Input_EIA_New_Plants)
class E16():
    # 'Input_EIA_New_Plants'!E16
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F16():
    # 'Input_EIA_New_Plants'!F16
    value = 56331

@register(Input_EIA_New_Plants)
class G16():
    # 'Input_EIA_New_Plants'!G16
    value = "Iwilei Tank Farm DG"

@register(Input_EIA_New_Plants)
class H16():
    # 'Input_EIA_New_Plants'!H16
    value = "DG2"

@register(Input_EIA_New_Plants)
class J16():
    # 'Input_EIA_New_Plants'!J16
    value = "SB"

@register(Input_EIA_New_Plants)
class K16():
    # 'Input_EIA_New_Plants'!K16
    value = 1.6

@register(Input_EIA_New_Plants)
class L16():
    # 'Input_EIA_New_Plants'!L16
    value = 1.64

@register(Input_EIA_New_Plants)
class M16():
    # 'Input_EIA_New_Plants'!M16
    value = 1.64

@register(Input_EIA_New_Plants)
class N16():
    # 'Input_EIA_New_Plants'!N16
    value = 22

@register(Input_EIA_New_Plants)
class O16():
    # 'Input_EIA_New_Plants'!O16
    value = "IC"

@register(Input_EIA_New_Plants)
class P16():
    # 'Input_EIA_New_Plants'!P16
    value = "DFO"

@register(Input_EIA_New_Plants)
class R16():
    # 'Input_EIA_New_Plants'!R16
    value = 11

@register(Input_EIA_New_Plants)
class S16():
    # 'Input_EIA_New_Plants'!S16
    value = 2005

@register(Input_EIA_New_Plants)
class V16():
    # 'Input_EIA_New_Plants'!V16
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A17():
    # 'Input_EIA_New_Plants'!A17
    value = "Distillate Fuel Oil2005"
    formula = "=V17&S17"
    @eval_fn
    def A17():
        v17_1 = Input_EIA_New_Plants.V17()
        s17_1 = Input_EIA_New_Plants.S17()
        var_1 = concat(v17_1, s17_1)
        return var_1

@register(Input_EIA_New_Plants)
class B17():
    # 'Input_EIA_New_Plants'!B17
    value = "HI"

@register(Input_EIA_New_Plants)
class C17():
    # 'Input_EIA_New_Plants'!C17
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D17():
    # 'Input_EIA_New_Plants'!D17
    value = 19547

@register(Input_EIA_New_Plants)
class E17():
    # 'Input_EIA_New_Plants'!E17
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F17():
    # 'Input_EIA_New_Plants'!F17
    value = 56331

@register(Input_EIA_New_Plants)
class G17():
    # 'Input_EIA_New_Plants'!G17
    value = "Iwilei Tank Farm DG"

@register(Input_EIA_New_Plants)
class H17():
    # 'Input_EIA_New_Plants'!H17
    value = "DG3"

@register(Input_EIA_New_Plants)
class J17():
    # 'Input_EIA_New_Plants'!J17
    value = "SB"

@register(Input_EIA_New_Plants)
class K17():
    # 'Input_EIA_New_Plants'!K17
    value = 1.6

@register(Input_EIA_New_Plants)
class L17():
    # 'Input_EIA_New_Plants'!L17
    value = 1.64

@register(Input_EIA_New_Plants)
class M17():
    # 'Input_EIA_New_Plants'!M17
    value = 1.64

@register(Input_EIA_New_Plants)
class N17():
    # 'Input_EIA_New_Plants'!N17
    value = 22

@register(Input_EIA_New_Plants)
class O17():
    # 'Input_EIA_New_Plants'!O17
    value = "IC"

@register(Input_EIA_New_Plants)
class P17():
    # 'Input_EIA_New_Plants'!P17
    value = "DFO"

@register(Input_EIA_New_Plants)
class R17():
    # 'Input_EIA_New_Plants'!R17
    value = 11

@register(Input_EIA_New_Plants)
class S17():
    # 'Input_EIA_New_Plants'!S17
    value = 2005

@register(Input_EIA_New_Plants)
class V17():
    # 'Input_EIA_New_Plants'!V17
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A18():
    # 'Input_EIA_New_Plants'!A18
    value = "Distillate Fuel Oil2006"
    formula = "=V18&S18"
    @eval_fn
    def A18():
        v18_1 = Input_EIA_New_Plants.V18()
        s18_1 = Input_EIA_New_Plants.S18()
        var_1 = concat(v18_1, s18_1)
        return var_1

@register(Input_EIA_New_Plants)
class B18():
    # 'Input_EIA_New_Plants'!B18
    value = "HI"

@register(Input_EIA_New_Plants)
class C18():
    # 'Input_EIA_New_Plants'!C18
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D18():
    # 'Input_EIA_New_Plants'!D18
    value = 19547

@register(Input_EIA_New_Plants)
class E18():
    # 'Input_EIA_New_Plants'!E18
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F18():
    # 'Input_EIA_New_Plants'!F18
    value = 56515

@register(Input_EIA_New_Plants)
class G18():
    # 'Input_EIA_New_Plants'!G18
    value = "CEIP Substation DG"

@register(Input_EIA_New_Plants)
class H18():
    # 'Input_EIA_New_Plants'!H18
    value = "DG1"

@register(Input_EIA_New_Plants)
class J18():
    # 'Input_EIA_New_Plants'!J18
    value = "SB"

@register(Input_EIA_New_Plants)
class K18():
    # 'Input_EIA_New_Plants'!K18
    value = 1.6

@register(Input_EIA_New_Plants)
class L18():
    # 'Input_EIA_New_Plants'!L18
    value = 1.64

@register(Input_EIA_New_Plants)
class M18():
    # 'Input_EIA_New_Plants'!M18
    value = 1.64

@register(Input_EIA_New_Plants)
class N18():
    # 'Input_EIA_New_Plants'!N18
    value = 22

@register(Input_EIA_New_Plants)
class O18():
    # 'Input_EIA_New_Plants'!O18
    value = "IC"

@register(Input_EIA_New_Plants)
class P18():
    # 'Input_EIA_New_Plants'!P18
    value = "DFO"

@register(Input_EIA_New_Plants)
class R18():
    # 'Input_EIA_New_Plants'!R18
    value = 11

@register(Input_EIA_New_Plants)
class S18():
    # 'Input_EIA_New_Plants'!S18
    value = 2006

@register(Input_EIA_New_Plants)
class V18():
    # 'Input_EIA_New_Plants'!V18
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A19():
    # 'Input_EIA_New_Plants'!A19
    value = "Distillate Fuel Oil2006"
    formula = "=V19&S19"
    @eval_fn
    def A19():
        v19_1 = Input_EIA_New_Plants.V19()
        s19_1 = Input_EIA_New_Plants.S19()
        var_1 = concat(v19_1, s19_1)
        return var_1

@register(Input_EIA_New_Plants)
class B19():
    # 'Input_EIA_New_Plants'!B19
    value = "HI"

@register(Input_EIA_New_Plants)
class C19():
    # 'Input_EIA_New_Plants'!C19
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D19():
    # 'Input_EIA_New_Plants'!D19
    value = 19547

@register(Input_EIA_New_Plants)
class E19():
    # 'Input_EIA_New_Plants'!E19
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F19():
    # 'Input_EIA_New_Plants'!F19
    value = 56515

@register(Input_EIA_New_Plants)
class G19():
    # 'Input_EIA_New_Plants'!G19
    value = "CEIP Substation DG"

@register(Input_EIA_New_Plants)
class H19():
    # 'Input_EIA_New_Plants'!H19
    value = "DG2"

@register(Input_EIA_New_Plants)
class J19():
    # 'Input_EIA_New_Plants'!J19
    value = "SB"

@register(Input_EIA_New_Plants)
class K19():
    # 'Input_EIA_New_Plants'!K19
    value = 1.6

@register(Input_EIA_New_Plants)
class L19():
    # 'Input_EIA_New_Plants'!L19
    value = 1.64

@register(Input_EIA_New_Plants)
class M19():
    # 'Input_EIA_New_Plants'!M19
    value = 1.64

@register(Input_EIA_New_Plants)
class N19():
    # 'Input_EIA_New_Plants'!N19
    value = 22

@register(Input_EIA_New_Plants)
class O19():
    # 'Input_EIA_New_Plants'!O19
    value = "IC"

@register(Input_EIA_New_Plants)
class P19():
    # 'Input_EIA_New_Plants'!P19
    value = "DFO"

@register(Input_EIA_New_Plants)
class R19():
    # 'Input_EIA_New_Plants'!R19
    value = 11

@register(Input_EIA_New_Plants)
class S19():
    # 'Input_EIA_New_Plants'!S19
    value = 2006

@register(Input_EIA_New_Plants)
class V19():
    # 'Input_EIA_New_Plants'!V19
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A20():
    # 'Input_EIA_New_Plants'!A20
    value = "Distillate Fuel Oil2006"
    formula = "=V20&S20"
    @eval_fn
    def A20():
        v20_1 = Input_EIA_New_Plants.V20()
        s20_1 = Input_EIA_New_Plants.S20()
        var_1 = concat(v20_1, s20_1)
        return var_1

@register(Input_EIA_New_Plants)
class B20():
    # 'Input_EIA_New_Plants'!B20
    value = "HI"

@register(Input_EIA_New_Plants)
class C20():
    # 'Input_EIA_New_Plants'!C20
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D20():
    # 'Input_EIA_New_Plants'!D20
    value = 19547

@register(Input_EIA_New_Plants)
class E20():
    # 'Input_EIA_New_Plants'!E20
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F20():
    # 'Input_EIA_New_Plants'!F20
    value = 56515

@register(Input_EIA_New_Plants)
class G20():
    # 'Input_EIA_New_Plants'!G20
    value = "CEIP Substation DG"

@register(Input_EIA_New_Plants)
class H20():
    # 'Input_EIA_New_Plants'!H20
    value = "DG3"

@register(Input_EIA_New_Plants)
class J20():
    # 'Input_EIA_New_Plants'!J20
    value = "SB"

@register(Input_EIA_New_Plants)
class K20():
    # 'Input_EIA_New_Plants'!K20
    value = 1.6

@register(Input_EIA_New_Plants)
class L20():
    # 'Input_EIA_New_Plants'!L20
    value = 1.64

@register(Input_EIA_New_Plants)
class M20():
    # 'Input_EIA_New_Plants'!M20
    value = 1.64

@register(Input_EIA_New_Plants)
class N20():
    # 'Input_EIA_New_Plants'!N20
    value = 22

@register(Input_EIA_New_Plants)
class O20():
    # 'Input_EIA_New_Plants'!O20
    value = "IC"

@register(Input_EIA_New_Plants)
class P20():
    # 'Input_EIA_New_Plants'!P20
    value = "DFO"

@register(Input_EIA_New_Plants)
class R20():
    # 'Input_EIA_New_Plants'!R20
    value = 11

@register(Input_EIA_New_Plants)
class S20():
    # 'Input_EIA_New_Plants'!S20
    value = 2006

@register(Input_EIA_New_Plants)
class V20():
    # 'Input_EIA_New_Plants'!V20
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A21():
    # 'Input_EIA_New_Plants'!A21
    value = "Distillate Fuel Oil2006"
    formula = "=V21&S21"
    @eval_fn
    def A21():
        v21_1 = Input_EIA_New_Plants.V21()
        s21_1 = Input_EIA_New_Plants.S21()
        var_1 = concat(v21_1, s21_1)
        return var_1

@register(Input_EIA_New_Plants)
class B21():
    # 'Input_EIA_New_Plants'!B21
    value = "HI"

@register(Input_EIA_New_Plants)
class C21():
    # 'Input_EIA_New_Plants'!C21
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D21():
    # 'Input_EIA_New_Plants'!D21
    value = 19547

@register(Input_EIA_New_Plants)
class E21():
    # 'Input_EIA_New_Plants'!E21
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F21():
    # 'Input_EIA_New_Plants'!F21
    value = 56514

@register(Input_EIA_New_Plants)
class G21():
    # 'Input_EIA_New_Plants'!G21
    value = "Kalaeoloa Pole Yard DG"

@register(Input_EIA_New_Plants)
class H21():
    # 'Input_EIA_New_Plants'!H21
    value = "DG1"

@register(Input_EIA_New_Plants)
class J21():
    # 'Input_EIA_New_Plants'!J21
    value = "SB"

@register(Input_EIA_New_Plants)
class K21():
    # 'Input_EIA_New_Plants'!K21
    value = 1.6

@register(Input_EIA_New_Plants)
class L21():
    # 'Input_EIA_New_Plants'!L21
    value = 1.64

@register(Input_EIA_New_Plants)
class M21():
    # 'Input_EIA_New_Plants'!M21
    value = 1.64

@register(Input_EIA_New_Plants)
class N21():
    # 'Input_EIA_New_Plants'!N21
    value = 22

@register(Input_EIA_New_Plants)
class O21():
    # 'Input_EIA_New_Plants'!O21
    value = "IC"

@register(Input_EIA_New_Plants)
class P21():
    # 'Input_EIA_New_Plants'!P21
    value = "DFO"

@register(Input_EIA_New_Plants)
class R21():
    # 'Input_EIA_New_Plants'!R21
    value = 12

@register(Input_EIA_New_Plants)
class S21():
    # 'Input_EIA_New_Plants'!S21
    value = 2006

@register(Input_EIA_New_Plants)
class V21():
    # 'Input_EIA_New_Plants'!V21
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A22():
    # 'Input_EIA_New_Plants'!A22
    value = "Distillate Fuel Oil2006"
    formula = "=V22&S22"
    @eval_fn
    def A22():
        v22_1 = Input_EIA_New_Plants.V22()
        s22_1 = Input_EIA_New_Plants.S22()
        var_1 = concat(v22_1, s22_1)
        return var_1

@register(Input_EIA_New_Plants)
class B22():
    # 'Input_EIA_New_Plants'!B22
    value = "HI"

@register(Input_EIA_New_Plants)
class C22():
    # 'Input_EIA_New_Plants'!C22
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D22():
    # 'Input_EIA_New_Plants'!D22
    value = 19547

@register(Input_EIA_New_Plants)
class E22():
    # 'Input_EIA_New_Plants'!E22
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F22():
    # 'Input_EIA_New_Plants'!F22
    value = 56514

@register(Input_EIA_New_Plants)
class G22():
    # 'Input_EIA_New_Plants'!G22
    value = "Kalaeoloa Pole Yard DG"

@register(Input_EIA_New_Plants)
class H22():
    # 'Input_EIA_New_Plants'!H22
    value = "DG2"

@register(Input_EIA_New_Plants)
class J22():
    # 'Input_EIA_New_Plants'!J22
    value = "SB"

@register(Input_EIA_New_Plants)
class K22():
    # 'Input_EIA_New_Plants'!K22
    value = 1.6

@register(Input_EIA_New_Plants)
class L22():
    # 'Input_EIA_New_Plants'!L22
    value = 1.64

@register(Input_EIA_New_Plants)
class M22():
    # 'Input_EIA_New_Plants'!M22
    value = 1.64

@register(Input_EIA_New_Plants)
class N22():
    # 'Input_EIA_New_Plants'!N22
    value = 22

@register(Input_EIA_New_Plants)
class O22():
    # 'Input_EIA_New_Plants'!O22
    value = "IC"

@register(Input_EIA_New_Plants)
class P22():
    # 'Input_EIA_New_Plants'!P22
    value = "DFO"

@register(Input_EIA_New_Plants)
class R22():
    # 'Input_EIA_New_Plants'!R22
    value = 12

@register(Input_EIA_New_Plants)
class S22():
    # 'Input_EIA_New_Plants'!S22
    value = 2006

@register(Input_EIA_New_Plants)
class V22():
    # 'Input_EIA_New_Plants'!V22
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A23():
    # 'Input_EIA_New_Plants'!A23
    value = "Distillate Fuel Oil2006"
    formula = "=V23&S23"
    @eval_fn
    def A23():
        v23_1 = Input_EIA_New_Plants.V23()
        s23_1 = Input_EIA_New_Plants.S23()
        var_1 = concat(v23_1, s23_1)
        return var_1

@register(Input_EIA_New_Plants)
class B23():
    # 'Input_EIA_New_Plants'!B23
    value = "HI"

@register(Input_EIA_New_Plants)
class C23():
    # 'Input_EIA_New_Plants'!C23
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D23():
    # 'Input_EIA_New_Plants'!D23
    value = 19547

@register(Input_EIA_New_Plants)
class E23():
    # 'Input_EIA_New_Plants'!E23
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F23():
    # 'Input_EIA_New_Plants'!F23
    value = 56514

@register(Input_EIA_New_Plants)
class G23():
    # 'Input_EIA_New_Plants'!G23
    value = "Kalaeoloa Pole Yard DG"

@register(Input_EIA_New_Plants)
class H23():
    # 'Input_EIA_New_Plants'!H23
    value = "DG3"

@register(Input_EIA_New_Plants)
class J23():
    # 'Input_EIA_New_Plants'!J23
    value = "SB"

@register(Input_EIA_New_Plants)
class K23():
    # 'Input_EIA_New_Plants'!K23
    value = 1.6

@register(Input_EIA_New_Plants)
class L23():
    # 'Input_EIA_New_Plants'!L23
    value = 1.64

@register(Input_EIA_New_Plants)
class M23():
    # 'Input_EIA_New_Plants'!M23
    value = 1.64

@register(Input_EIA_New_Plants)
class N23():
    # 'Input_EIA_New_Plants'!N23
    value = 22

@register(Input_EIA_New_Plants)
class O23():
    # 'Input_EIA_New_Plants'!O23
    value = "IC"

@register(Input_EIA_New_Plants)
class P23():
    # 'Input_EIA_New_Plants'!P23
    value = "DFO"

@register(Input_EIA_New_Plants)
class R23():
    # 'Input_EIA_New_Plants'!R23
    value = 12

@register(Input_EIA_New_Plants)
class S23():
    # 'Input_EIA_New_Plants'!S23
    value = 2006

@register(Input_EIA_New_Plants)
class V23():
    # 'Input_EIA_New_Plants'!V23
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A24():
    # 'Input_EIA_New_Plants'!A24
    value = "Wind2006"
    formula = "=V24&S24"
    @eval_fn
    def A24():
        v24_1 = Input_EIA_New_Plants.V24()
        s24_1 = Input_EIA_New_Plants.S24()
        var_1 = concat(v24_1, s24_1)
        return var_1

@register(Input_EIA_New_Plants)
class B24():
    # 'Input_EIA_New_Plants'!B24
    value = "HI"

@register(Input_EIA_New_Plants)
class C24():
    # 'Input_EIA_New_Plants'!C24
    value = "Hawaii"

@register(Input_EIA_New_Plants)
class D24():
    # 'Input_EIA_New_Plants'!D24
    value = 54846

@register(Input_EIA_New_Plants)
class E24():
    # 'Input_EIA_New_Plants'!E24
    value = "Hawi Renewable Development LLC"

@register(Input_EIA_New_Plants)
class F24():
    # 'Input_EIA_New_Plants'!F24
    value = 56447

@register(Input_EIA_New_Plants)
class G24():
    # 'Input_EIA_New_Plants'!G24
    value = "Hawi  Wind Farm"

@register(Input_EIA_New_Plants)
class H24():
    # 'Input_EIA_New_Plants'!H24
    value = "V-47"

@register(Input_EIA_New_Plants)
class J24():
    # 'Input_EIA_New_Plants'!J24
    value = "OP"

@register(Input_EIA_New_Plants)
class K24():
    # 'Input_EIA_New_Plants'!K24
    value = 10.6

@register(Input_EIA_New_Plants)
class L24():
    # 'Input_EIA_New_Plants'!L24
    value = 10.6

@register(Input_EIA_New_Plants)
class M24():
    # 'Input_EIA_New_Plants'!M24
    value = 10.6

@register(Input_EIA_New_Plants)
class N24():
    # 'Input_EIA_New_Plants'!N24
    value = 22

@register(Input_EIA_New_Plants)
class O24():
    # 'Input_EIA_New_Plants'!O24
    value = "WT"

@register(Input_EIA_New_Plants)
class P24():
    # 'Input_EIA_New_Plants'!P24
    value = "WND"

@register(Input_EIA_New_Plants)
class R24():
    # 'Input_EIA_New_Plants'!R24
    value = 5

@register(Input_EIA_New_Plants)
class S24():
    # 'Input_EIA_New_Plants'!S24
    value = 2006

@register(Input_EIA_New_Plants)
class T24():
    # 'Input_EIA_New_Plants'!T24
    value = 16

@register(Input_EIA_New_Plants)
class V24():
    # 'Input_EIA_New_Plants'!V24
    value = "Wind"

@register(Input_EIA_New_Plants)
class A25():
    # 'Input_EIA_New_Plants'!A25
    value = "Wind2006"
    formula = "=V25&S25"
    @eval_fn
    def A25():
        v25_1 = Input_EIA_New_Plants.V25()
        s25_1 = Input_EIA_New_Plants.S25()
        var_1 = concat(v25_1, s25_1)
        return var_1

@register(Input_EIA_New_Plants)
class B25():
    # 'Input_EIA_New_Plants'!B25
    value = "HI"

@register(Input_EIA_New_Plants)
class C25():
    # 'Input_EIA_New_Plants'!C25
    value = "Maui"

@register(Input_EIA_New_Plants)
class D25():
    # 'Input_EIA_New_Plants'!D25
    value = 54854

@register(Input_EIA_New_Plants)
class E25():
    # 'Input_EIA_New_Plants'!E25
    value = "Kaheawa Wind Power LLC"

@register(Input_EIA_New_Plants)
class F25():
    # 'Input_EIA_New_Plants'!F25
    value = 56449

@register(Input_EIA_New_Plants)
class G25():
    # 'Input_EIA_New_Plants'!G25
    value = "Kaheawa Pastures Wind Farm"

@register(Input_EIA_New_Plants)
class H25():
    # 'Input_EIA_New_Plants'!H25
    value = "1"

@register(Input_EIA_New_Plants)
class J25():
    # 'Input_EIA_New_Plants'!J25
    value = "OP"

@register(Input_EIA_New_Plants)
class K25():
    # 'Input_EIA_New_Plants'!K25
    value = 30

@register(Input_EIA_New_Plants)
class L25():
    # 'Input_EIA_New_Plants'!L25
    value = 30

@register(Input_EIA_New_Plants)
class M25():
    # 'Input_EIA_New_Plants'!M25
    value = 30

@register(Input_EIA_New_Plants)
class N25():
    # 'Input_EIA_New_Plants'!N25
    value = 22

@register(Input_EIA_New_Plants)
class O25():
    # 'Input_EIA_New_Plants'!O25
    value = "WT"

@register(Input_EIA_New_Plants)
class P25():
    # 'Input_EIA_New_Plants'!P25
    value = "WND"

@register(Input_EIA_New_Plants)
class R25():
    # 'Input_EIA_New_Plants'!R25
    value = 1

@register(Input_EIA_New_Plants)
class S25():
    # 'Input_EIA_New_Plants'!S25
    value = 2006

@register(Input_EIA_New_Plants)
class T25():
    # 'Input_EIA_New_Plants'!T25
    value = 20

@register(Input_EIA_New_Plants)
class V25():
    # 'Input_EIA_New_Plants'!V25
    value = "Wind"

@register(Input_EIA_New_Plants)
class A26():
    # 'Input_EIA_New_Plants'!A26
    value = "Distillate Fuel Oil2006"
    formula = "=V26&S26"
    @eval_fn
    def A26():
        v26_1 = Input_EIA_New_Plants.V26()
        s26_1 = Input_EIA_New_Plants.S26()
        var_1 = concat(v26_1, s26_1)
        return var_1

@register(Input_EIA_New_Plants)
class B26():
    # 'Input_EIA_New_Plants'!B26
    value = "HI"

@register(Input_EIA_New_Plants)
class C26():
    # 'Input_EIA_New_Plants'!C26
    value = "Maui"

@register(Input_EIA_New_Plants)
class D26():
    # 'Input_EIA_New_Plants'!D26
    value = 11843

@register(Input_EIA_New_Plants)
class E26():
    # 'Input_EIA_New_Plants'!E26
    value = "Maui Electric Co Ltd"

@register(Input_EIA_New_Plants)
class F26():
    # 'Input_EIA_New_Plants'!F26
    value = 6504

@register(Input_EIA_New_Plants)
class G26():
    # 'Input_EIA_New_Plants'!G26
    value = "Maalaea"

@register(Input_EIA_New_Plants)
class H26():
    # 'Input_EIA_New_Plants'!H26
    value = "18"

@register(Input_EIA_New_Plants)
class J26():
    # 'Input_EIA_New_Plants'!J26
    value = "OP"

@register(Input_EIA_New_Plants)
class K26():
    # 'Input_EIA_New_Plants'!K26
    value = 18

@register(Input_EIA_New_Plants)
class L26():
    # 'Input_EIA_New_Plants'!L26
    value = 15

@register(Input_EIA_New_Plants)
class M26():
    # 'Input_EIA_New_Plants'!M26
    value = 15

@register(Input_EIA_New_Plants)
class N26():
    # 'Input_EIA_New_Plants'!N26
    value = 22

@register(Input_EIA_New_Plants)
class O26():
    # 'Input_EIA_New_Plants'!O26
    value = "CA"

@register(Input_EIA_New_Plants)
class P26():
    # 'Input_EIA_New_Plants'!P26
    value = "DFO"

@register(Input_EIA_New_Plants)
class R26():
    # 'Input_EIA_New_Plants'!R26
    value = 10

@register(Input_EIA_New_Plants)
class S26():
    # 'Input_EIA_New_Plants'!S26
    value = 2006

@register(Input_EIA_New_Plants)
class V26():
    # 'Input_EIA_New_Plants'!V26
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A27():
    # 'Input_EIA_New_Plants'!A27
    value = "Wind2007"
    formula = "=V27&S27"
    @eval_fn
    def A27():
        v27_1 = Input_EIA_New_Plants.V27()
        s27_1 = Input_EIA_New_Plants.S27()
        var_1 = concat(v27_1, s27_1)
        return var_1

@register(Input_EIA_New_Plants)
class B27():
    # 'Input_EIA_New_Plants'!B27
    value = "HI"

@register(Input_EIA_New_Plants)
class C27():
    # 'Input_EIA_New_Plants'!C27
    value = "Hawaii"

@register(Input_EIA_New_Plants)
class D27():
    # 'Input_EIA_New_Plants'!D27
    value = 794

@register(Input_EIA_New_Plants)
class E27():
    # 'Input_EIA_New_Plants'!E27
    value = "Apollo Energy Corp"

@register(Input_EIA_New_Plants)
class F27():
    # 'Input_EIA_New_Plants'!F27
    value = 56378

@register(Input_EIA_New_Plants)
class G27():
    # 'Input_EIA_New_Plants'!G27
    value = "Pakini Nui Wind Farm"

@register(Input_EIA_New_Plants)
class H27():
    # 'Input_EIA_New_Plants'!H27
    value = "1"

@register(Input_EIA_New_Plants)
class J27():
    # 'Input_EIA_New_Plants'!J27
    value = "OP"

@register(Input_EIA_New_Plants)
class K27():
    # 'Input_EIA_New_Plants'!K27
    value = 21

@register(Input_EIA_New_Plants)
class L27():
    # 'Input_EIA_New_Plants'!L27
    value = 21

@register(Input_EIA_New_Plants)
class M27():
    # 'Input_EIA_New_Plants'!M27
    value = 21

@register(Input_EIA_New_Plants)
class N27():
    # 'Input_EIA_New_Plants'!N27
    value = 22

@register(Input_EIA_New_Plants)
class O27():
    # 'Input_EIA_New_Plants'!O27
    value = "WT"

@register(Input_EIA_New_Plants)
class P27():
    # 'Input_EIA_New_Plants'!P27
    value = "WND"

@register(Input_EIA_New_Plants)
class R27():
    # 'Input_EIA_New_Plants'!R27
    value = 4

@register(Input_EIA_New_Plants)
class S27():
    # 'Input_EIA_New_Plants'!S27
    value = 2007

@register(Input_EIA_New_Plants)
class T27():
    # 'Input_EIA_New_Plants'!T27
    value = 14

@register(Input_EIA_New_Plants)
class V27():
    # 'Input_EIA_New_Plants'!V27
    value = "Wind"

@register(Input_EIA_New_Plants)
class A28():
    # 'Input_EIA_New_Plants'!A28
    value = "Distillate Fuel Oil2007"
    formula = "=V28&S28"
    @eval_fn
    def A28():
        v28_1 = Input_EIA_New_Plants.V28()
        s28_1 = Input_EIA_New_Plants.S28()
        var_1 = concat(v28_1, s28_1)
        return var_1

@register(Input_EIA_New_Plants)
class B28():
    # 'Input_EIA_New_Plants'!B28
    value = "HI"

@register(Input_EIA_New_Plants)
class C28():
    # 'Input_EIA_New_Plants'!C28
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D28():
    # 'Input_EIA_New_Plants'!D28
    value = 19547

@register(Input_EIA_New_Plants)
class E28():
    # 'Input_EIA_New_Plants'!E28
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F28():
    # 'Input_EIA_New_Plants'!F28
    value = 56330

@register(Input_EIA_New_Plants)
class G28():
    # 'Input_EIA_New_Plants'!G28
    value = "Ewa Nui Substation DG"

@register(Input_EIA_New_Plants)
class H28():
    # 'Input_EIA_New_Plants'!H28
    value = "DG4"

@register(Input_EIA_New_Plants)
class J28():
    # 'Input_EIA_New_Plants'!J28
    value = "OP"

@register(Input_EIA_New_Plants)
class K28():
    # 'Input_EIA_New_Plants'!K28
    value = 1.6

@register(Input_EIA_New_Plants)
class L28():
    # 'Input_EIA_New_Plants'!L28
    value = 1.6

@register(Input_EIA_New_Plants)
class M28():
    # 'Input_EIA_New_Plants'!M28
    value = 1.6

@register(Input_EIA_New_Plants)
class N28():
    # 'Input_EIA_New_Plants'!N28
    value = 22

@register(Input_EIA_New_Plants)
class O28():
    # 'Input_EIA_New_Plants'!O28
    value = "IC"

@register(Input_EIA_New_Plants)
class P28():
    # 'Input_EIA_New_Plants'!P28
    value = "DFO"

@register(Input_EIA_New_Plants)
class R28():
    # 'Input_EIA_New_Plants'!R28
    value = 5

@register(Input_EIA_New_Plants)
class S28():
    # 'Input_EIA_New_Plants'!S28
    value = 2007

@register(Input_EIA_New_Plants)
class V28():
    # 'Input_EIA_New_Plants'!V28
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A29():
    # 'Input_EIA_New_Plants'!A29
    value = "Distillate Fuel Oil2007"
    formula = "=V29&S29"
    @eval_fn
    def A29():
        v29_1 = Input_EIA_New_Plants.V29()
        s29_1 = Input_EIA_New_Plants.S29()
        var_1 = concat(v29_1, s29_1)
        return var_1

@register(Input_EIA_New_Plants)
class B29():
    # 'Input_EIA_New_Plants'!B29
    value = "HI"

@register(Input_EIA_New_Plants)
class C29():
    # 'Input_EIA_New_Plants'!C29
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D29():
    # 'Input_EIA_New_Plants'!D29
    value = 19547

@register(Input_EIA_New_Plants)
class E29():
    # 'Input_EIA_New_Plants'!E29
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F29():
    # 'Input_EIA_New_Plants'!F29
    value = 56330

@register(Input_EIA_New_Plants)
class G29():
    # 'Input_EIA_New_Plants'!G29
    value = "Ewa Nui Substation DG"

@register(Input_EIA_New_Plants)
class H29():
    # 'Input_EIA_New_Plants'!H29
    value = "DG5"

@register(Input_EIA_New_Plants)
class J29():
    # 'Input_EIA_New_Plants'!J29
    value = "OP"

@register(Input_EIA_New_Plants)
class K29():
    # 'Input_EIA_New_Plants'!K29
    value = 1.6

@register(Input_EIA_New_Plants)
class L29():
    # 'Input_EIA_New_Plants'!L29
    value = 1.6

@register(Input_EIA_New_Plants)
class M29():
    # 'Input_EIA_New_Plants'!M29
    value = 1.6

@register(Input_EIA_New_Plants)
class N29():
    # 'Input_EIA_New_Plants'!N29
    value = 22

@register(Input_EIA_New_Plants)
class O29():
    # 'Input_EIA_New_Plants'!O29
    value = "IC"

@register(Input_EIA_New_Plants)
class P29():
    # 'Input_EIA_New_Plants'!P29
    value = "DFO"

@register(Input_EIA_New_Plants)
class R29():
    # 'Input_EIA_New_Plants'!R29
    value = 5

@register(Input_EIA_New_Plants)
class S29():
    # 'Input_EIA_New_Plants'!S29
    value = 2007

@register(Input_EIA_New_Plants)
class V29():
    # 'Input_EIA_New_Plants'!V29
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A30():
    # 'Input_EIA_New_Plants'!A30
    value = "Distillate Fuel Oil2007"
    formula = "=V30&S30"
    @eval_fn
    def A30():
        v30_1 = Input_EIA_New_Plants.V30()
        s30_1 = Input_EIA_New_Plants.S30()
        var_1 = concat(v30_1, s30_1)
        return var_1

@register(Input_EIA_New_Plants)
class B30():
    # 'Input_EIA_New_Plants'!B30
    value = "HI"

@register(Input_EIA_New_Plants)
class C30():
    # 'Input_EIA_New_Plants'!C30
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D30():
    # 'Input_EIA_New_Plants'!D30
    value = 19547

@register(Input_EIA_New_Plants)
class E30():
    # 'Input_EIA_New_Plants'!E30
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F30():
    # 'Input_EIA_New_Plants'!F30
    value = 56330

@register(Input_EIA_New_Plants)
class G30():
    # 'Input_EIA_New_Plants'!G30
    value = "Ewa Nui Substation DG"

@register(Input_EIA_New_Plants)
class H30():
    # 'Input_EIA_New_Plants'!H30
    value = "DG6"

@register(Input_EIA_New_Plants)
class J30():
    # 'Input_EIA_New_Plants'!J30
    value = "OP"

@register(Input_EIA_New_Plants)
class K30():
    # 'Input_EIA_New_Plants'!K30
    value = 1.6

@register(Input_EIA_New_Plants)
class L30():
    # 'Input_EIA_New_Plants'!L30
    value = 1.6

@register(Input_EIA_New_Plants)
class M30():
    # 'Input_EIA_New_Plants'!M30
    value = 1.6

@register(Input_EIA_New_Plants)
class N30():
    # 'Input_EIA_New_Plants'!N30
    value = 22

@register(Input_EIA_New_Plants)
class O30():
    # 'Input_EIA_New_Plants'!O30
    value = "IC"

@register(Input_EIA_New_Plants)
class P30():
    # 'Input_EIA_New_Plants'!P30
    value = "DFO"

@register(Input_EIA_New_Plants)
class R30():
    # 'Input_EIA_New_Plants'!R30
    value = 5

@register(Input_EIA_New_Plants)
class S30():
    # 'Input_EIA_New_Plants'!S30
    value = 2007

@register(Input_EIA_New_Plants)
class V30():
    # 'Input_EIA_New_Plants'!V30
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A31():
    # 'Input_EIA_New_Plants'!A31
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V31&S31"
    @eval_fn
    def A31():
        v31_1 = Input_EIA_New_Plants.V31()
        s31_1 = Input_EIA_New_Plants.S31()
        var_1 = concat(v31_1, s31_1)
        return var_1

@register(Input_EIA_New_Plants)
class B31():
    # 'Input_EIA_New_Plants'!B31
    value = "HI"

@register(Input_EIA_New_Plants)
class C31():
    # 'Input_EIA_New_Plants'!C31
    value = "Maui"

@register(Input_EIA_New_Plants)
class D31():
    # 'Input_EIA_New_Plants'!D31
    value = 55910

@register(Input_EIA_New_Plants)
class E31():
    # 'Input_EIA_New_Plants'!E31
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F31():
    # 'Input_EIA_New_Plants'!F31
    value = 56667

@register(Input_EIA_New_Plants)
class G31():
    # 'Input_EIA_New_Plants'!G31
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H31():
    # 'Input_EIA_New_Plants'!H31
    value = "0001"

@register(Input_EIA_New_Plants)
class J31():
    # 'Input_EIA_New_Plants'!J31
    value = "OP"

@register(Input_EIA_New_Plants)
class K31():
    # 'Input_EIA_New_Plants'!K31
    value = 0.1

@register(Input_EIA_New_Plants)
class L31():
    # 'Input_EIA_New_Plants'!L31
    value = 0.1

@register(Input_EIA_New_Plants)
class M31():
    # 'Input_EIA_New_Plants'!M31
    value = 0.1

@register(Input_EIA_New_Plants)
class N31():
    # 'Input_EIA_New_Plants'!N31
    value = 22

@register(Input_EIA_New_Plants)
class O31():
    # 'Input_EIA_New_Plants'!O31
    value = "PV"

@register(Input_EIA_New_Plants)
class P31():
    # 'Input_EIA_New_Plants'!P31
    value = "SUN"

@register(Input_EIA_New_Plants)
class R31():
    # 'Input_EIA_New_Plants'!R31
    value = 12

@register(Input_EIA_New_Plants)
class S31():
    # 'Input_EIA_New_Plants'!S31
    value = 2008

@register(Input_EIA_New_Plants)
class V31():
    # 'Input_EIA_New_Plants'!V31
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A32():
    # 'Input_EIA_New_Plants'!A32
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V32&S32"
    @eval_fn
    def A32():
        v32_1 = Input_EIA_New_Plants.V32()
        s32_1 = Input_EIA_New_Plants.S32()
        var_1 = concat(v32_1, s32_1)
        return var_1

@register(Input_EIA_New_Plants)
class B32():
    # 'Input_EIA_New_Plants'!B32
    value = "HI"

@register(Input_EIA_New_Plants)
class C32():
    # 'Input_EIA_New_Plants'!C32
    value = "Maui"

@register(Input_EIA_New_Plants)
class D32():
    # 'Input_EIA_New_Plants'!D32
    value = 55910

@register(Input_EIA_New_Plants)
class E32():
    # 'Input_EIA_New_Plants'!E32
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F32():
    # 'Input_EIA_New_Plants'!F32
    value = 56667

@register(Input_EIA_New_Plants)
class G32():
    # 'Input_EIA_New_Plants'!G32
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H32():
    # 'Input_EIA_New_Plants'!H32
    value = "0002"

@register(Input_EIA_New_Plants)
class J32():
    # 'Input_EIA_New_Plants'!J32
    value = "OP"

@register(Input_EIA_New_Plants)
class K32():
    # 'Input_EIA_New_Plants'!K32
    value = 0.1

@register(Input_EIA_New_Plants)
class L32():
    # 'Input_EIA_New_Plants'!L32
    value = 0.1

@register(Input_EIA_New_Plants)
class M32():
    # 'Input_EIA_New_Plants'!M32
    value = 0.1

@register(Input_EIA_New_Plants)
class N32():
    # 'Input_EIA_New_Plants'!N32
    value = 22

@register(Input_EIA_New_Plants)
class O32():
    # 'Input_EIA_New_Plants'!O32
    value = "PV"

@register(Input_EIA_New_Plants)
class P32():
    # 'Input_EIA_New_Plants'!P32
    value = "SUN"

@register(Input_EIA_New_Plants)
class R32():
    # 'Input_EIA_New_Plants'!R32
    value = 12

@register(Input_EIA_New_Plants)
class S32():
    # 'Input_EIA_New_Plants'!S32
    value = 2008

@register(Input_EIA_New_Plants)
class V32():
    # 'Input_EIA_New_Plants'!V32
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A33():
    # 'Input_EIA_New_Plants'!A33
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V33&S33"
    @eval_fn
    def A33():
        v33_1 = Input_EIA_New_Plants.V33()
        s33_1 = Input_EIA_New_Plants.S33()
        var_1 = concat(v33_1, s33_1)
        return var_1

@register(Input_EIA_New_Plants)
class B33():
    # 'Input_EIA_New_Plants'!B33
    value = "HI"

@register(Input_EIA_New_Plants)
class C33():
    # 'Input_EIA_New_Plants'!C33
    value = "Maui"

@register(Input_EIA_New_Plants)
class D33():
    # 'Input_EIA_New_Plants'!D33
    value = 55910

@register(Input_EIA_New_Plants)
class E33():
    # 'Input_EIA_New_Plants'!E33
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F33():
    # 'Input_EIA_New_Plants'!F33
    value = 56667

@register(Input_EIA_New_Plants)
class G33():
    # 'Input_EIA_New_Plants'!G33
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H33():
    # 'Input_EIA_New_Plants'!H33
    value = "0003"

@register(Input_EIA_New_Plants)
class J33():
    # 'Input_EIA_New_Plants'!J33
    value = "OP"

@register(Input_EIA_New_Plants)
class K33():
    # 'Input_EIA_New_Plants'!K33
    value = 0.1

@register(Input_EIA_New_Plants)
class L33():
    # 'Input_EIA_New_Plants'!L33
    value = 0.1

@register(Input_EIA_New_Plants)
class M33():
    # 'Input_EIA_New_Plants'!M33
    value = 0.1

@register(Input_EIA_New_Plants)
class N33():
    # 'Input_EIA_New_Plants'!N33
    value = 22

@register(Input_EIA_New_Plants)
class O33():
    # 'Input_EIA_New_Plants'!O33
    value = "PV"

@register(Input_EIA_New_Plants)
class P33():
    # 'Input_EIA_New_Plants'!P33
    value = "SUN"

@register(Input_EIA_New_Plants)
class R33():
    # 'Input_EIA_New_Plants'!R33
    value = 12

@register(Input_EIA_New_Plants)
class S33():
    # 'Input_EIA_New_Plants'!S33
    value = 2008

@register(Input_EIA_New_Plants)
class V33():
    # 'Input_EIA_New_Plants'!V33
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A34():
    # 'Input_EIA_New_Plants'!A34
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V34&S34"
    @eval_fn
    def A34():
        v34_1 = Input_EIA_New_Plants.V34()
        s34_1 = Input_EIA_New_Plants.S34()
        var_1 = concat(v34_1, s34_1)
        return var_1

@register(Input_EIA_New_Plants)
class B34():
    # 'Input_EIA_New_Plants'!B34
    value = "HI"

@register(Input_EIA_New_Plants)
class C34():
    # 'Input_EIA_New_Plants'!C34
    value = "Maui"

@register(Input_EIA_New_Plants)
class D34():
    # 'Input_EIA_New_Plants'!D34
    value = 55910

@register(Input_EIA_New_Plants)
class E34():
    # 'Input_EIA_New_Plants'!E34
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F34():
    # 'Input_EIA_New_Plants'!F34
    value = 56667

@register(Input_EIA_New_Plants)
class G34():
    # 'Input_EIA_New_Plants'!G34
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H34():
    # 'Input_EIA_New_Plants'!H34
    value = "0004"

@register(Input_EIA_New_Plants)
class J34():
    # 'Input_EIA_New_Plants'!J34
    value = "OP"

@register(Input_EIA_New_Plants)
class K34():
    # 'Input_EIA_New_Plants'!K34
    value = 0.1

@register(Input_EIA_New_Plants)
class L34():
    # 'Input_EIA_New_Plants'!L34
    value = 0.1

@register(Input_EIA_New_Plants)
class M34():
    # 'Input_EIA_New_Plants'!M34
    value = 0.1

@register(Input_EIA_New_Plants)
class N34():
    # 'Input_EIA_New_Plants'!N34
    value = 22

@register(Input_EIA_New_Plants)
class O34():
    # 'Input_EIA_New_Plants'!O34
    value = "PV"

@register(Input_EIA_New_Plants)
class P34():
    # 'Input_EIA_New_Plants'!P34
    value = "SUN"

@register(Input_EIA_New_Plants)
class R34():
    # 'Input_EIA_New_Plants'!R34
    value = 12

@register(Input_EIA_New_Plants)
class S34():
    # 'Input_EIA_New_Plants'!S34
    value = 2008

@register(Input_EIA_New_Plants)
class V34():
    # 'Input_EIA_New_Plants'!V34
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A35():
    # 'Input_EIA_New_Plants'!A35
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V35&S35"
    @eval_fn
    def A35():
        v35_1 = Input_EIA_New_Plants.V35()
        s35_1 = Input_EIA_New_Plants.S35()
        var_1 = concat(v35_1, s35_1)
        return var_1

@register(Input_EIA_New_Plants)
class B35():
    # 'Input_EIA_New_Plants'!B35
    value = "HI"

@register(Input_EIA_New_Plants)
class C35():
    # 'Input_EIA_New_Plants'!C35
    value = "Maui"

@register(Input_EIA_New_Plants)
class D35():
    # 'Input_EIA_New_Plants'!D35
    value = 55910

@register(Input_EIA_New_Plants)
class E35():
    # 'Input_EIA_New_Plants'!E35
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F35():
    # 'Input_EIA_New_Plants'!F35
    value = 56667

@register(Input_EIA_New_Plants)
class G35():
    # 'Input_EIA_New_Plants'!G35
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H35():
    # 'Input_EIA_New_Plants'!H35
    value = "0005"

@register(Input_EIA_New_Plants)
class J35():
    # 'Input_EIA_New_Plants'!J35
    value = "OP"

@register(Input_EIA_New_Plants)
class K35():
    # 'Input_EIA_New_Plants'!K35
    value = 0.1

@register(Input_EIA_New_Plants)
class L35():
    # 'Input_EIA_New_Plants'!L35
    value = 0.1

@register(Input_EIA_New_Plants)
class M35():
    # 'Input_EIA_New_Plants'!M35
    value = 0.1

@register(Input_EIA_New_Plants)
class N35():
    # 'Input_EIA_New_Plants'!N35
    value = 22

@register(Input_EIA_New_Plants)
class O35():
    # 'Input_EIA_New_Plants'!O35
    value = "PV"

@register(Input_EIA_New_Plants)
class P35():
    # 'Input_EIA_New_Plants'!P35
    value = "SUN"

@register(Input_EIA_New_Plants)
class R35():
    # 'Input_EIA_New_Plants'!R35
    value = 12

@register(Input_EIA_New_Plants)
class S35():
    # 'Input_EIA_New_Plants'!S35
    value = 2008

@register(Input_EIA_New_Plants)
class V35():
    # 'Input_EIA_New_Plants'!V35
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A36():
    # 'Input_EIA_New_Plants'!A36
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V36&S36"
    @eval_fn
    def A36():
        v36_1 = Input_EIA_New_Plants.V36()
        s36_1 = Input_EIA_New_Plants.S36()
        var_1 = concat(v36_1, s36_1)
        return var_1

@register(Input_EIA_New_Plants)
class B36():
    # 'Input_EIA_New_Plants'!B36
    value = "HI"

@register(Input_EIA_New_Plants)
class C36():
    # 'Input_EIA_New_Plants'!C36
    value = "Maui"

@register(Input_EIA_New_Plants)
class D36():
    # 'Input_EIA_New_Plants'!D36
    value = 55910

@register(Input_EIA_New_Plants)
class E36():
    # 'Input_EIA_New_Plants'!E36
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F36():
    # 'Input_EIA_New_Plants'!F36
    value = 56667

@register(Input_EIA_New_Plants)
class G36():
    # 'Input_EIA_New_Plants'!G36
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H36():
    # 'Input_EIA_New_Plants'!H36
    value = "0006"

@register(Input_EIA_New_Plants)
class J36():
    # 'Input_EIA_New_Plants'!J36
    value = "OP"

@register(Input_EIA_New_Plants)
class K36():
    # 'Input_EIA_New_Plants'!K36
    value = 0.1

@register(Input_EIA_New_Plants)
class L36():
    # 'Input_EIA_New_Plants'!L36
    value = 0.1

@register(Input_EIA_New_Plants)
class M36():
    # 'Input_EIA_New_Plants'!M36
    value = 0.1

@register(Input_EIA_New_Plants)
class N36():
    # 'Input_EIA_New_Plants'!N36
    value = 22

@register(Input_EIA_New_Plants)
class O36():
    # 'Input_EIA_New_Plants'!O36
    value = "PV"

@register(Input_EIA_New_Plants)
class P36():
    # 'Input_EIA_New_Plants'!P36
    value = "SUN"

@register(Input_EIA_New_Plants)
class R36():
    # 'Input_EIA_New_Plants'!R36
    value = 12

@register(Input_EIA_New_Plants)
class S36():
    # 'Input_EIA_New_Plants'!S36
    value = 2008

@register(Input_EIA_New_Plants)
class V36():
    # 'Input_EIA_New_Plants'!V36
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A37():
    # 'Input_EIA_New_Plants'!A37
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V37&S37"
    @eval_fn
    def A37():
        v37_1 = Input_EIA_New_Plants.V37()
        s37_1 = Input_EIA_New_Plants.S37()
        var_1 = concat(v37_1, s37_1)
        return var_1

@register(Input_EIA_New_Plants)
class B37():
    # 'Input_EIA_New_Plants'!B37
    value = "HI"

@register(Input_EIA_New_Plants)
class C37():
    # 'Input_EIA_New_Plants'!C37
    value = "Maui"

@register(Input_EIA_New_Plants)
class D37():
    # 'Input_EIA_New_Plants'!D37
    value = 55910

@register(Input_EIA_New_Plants)
class E37():
    # 'Input_EIA_New_Plants'!E37
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F37():
    # 'Input_EIA_New_Plants'!F37
    value = 56667

@register(Input_EIA_New_Plants)
class G37():
    # 'Input_EIA_New_Plants'!G37
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H37():
    # 'Input_EIA_New_Plants'!H37
    value = "0007"

@register(Input_EIA_New_Plants)
class J37():
    # 'Input_EIA_New_Plants'!J37
    value = "OP"

@register(Input_EIA_New_Plants)
class K37():
    # 'Input_EIA_New_Plants'!K37
    value = 0.1

@register(Input_EIA_New_Plants)
class L37():
    # 'Input_EIA_New_Plants'!L37
    value = 0.1

@register(Input_EIA_New_Plants)
class M37():
    # 'Input_EIA_New_Plants'!M37
    value = 0.1

@register(Input_EIA_New_Plants)
class N37():
    # 'Input_EIA_New_Plants'!N37
    value = 22

@register(Input_EIA_New_Plants)
class O37():
    # 'Input_EIA_New_Plants'!O37
    value = "PV"

@register(Input_EIA_New_Plants)
class P37():
    # 'Input_EIA_New_Plants'!P37
    value = "SUN"

@register(Input_EIA_New_Plants)
class R37():
    # 'Input_EIA_New_Plants'!R37
    value = 12

@register(Input_EIA_New_Plants)
class S37():
    # 'Input_EIA_New_Plants'!S37
    value = 2008

@register(Input_EIA_New_Plants)
class V37():
    # 'Input_EIA_New_Plants'!V37
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A38():
    # 'Input_EIA_New_Plants'!A38
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V38&S38"
    @eval_fn
    def A38():
        v38_1 = Input_EIA_New_Plants.V38()
        s38_1 = Input_EIA_New_Plants.S38()
        var_1 = concat(v38_1, s38_1)
        return var_1

@register(Input_EIA_New_Plants)
class B38():
    # 'Input_EIA_New_Plants'!B38
    value = "HI"

@register(Input_EIA_New_Plants)
class C38():
    # 'Input_EIA_New_Plants'!C38
    value = "Maui"

@register(Input_EIA_New_Plants)
class D38():
    # 'Input_EIA_New_Plants'!D38
    value = 55910

@register(Input_EIA_New_Plants)
class E38():
    # 'Input_EIA_New_Plants'!E38
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F38():
    # 'Input_EIA_New_Plants'!F38
    value = 56667

@register(Input_EIA_New_Plants)
class G38():
    # 'Input_EIA_New_Plants'!G38
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H38():
    # 'Input_EIA_New_Plants'!H38
    value = "0008"

@register(Input_EIA_New_Plants)
class J38():
    # 'Input_EIA_New_Plants'!J38
    value = "OP"

@register(Input_EIA_New_Plants)
class K38():
    # 'Input_EIA_New_Plants'!K38
    value = 0.1

@register(Input_EIA_New_Plants)
class L38():
    # 'Input_EIA_New_Plants'!L38
    value = 0.1

@register(Input_EIA_New_Plants)
class M38():
    # 'Input_EIA_New_Plants'!M38
    value = 0.1

@register(Input_EIA_New_Plants)
class N38():
    # 'Input_EIA_New_Plants'!N38
    value = 22

@register(Input_EIA_New_Plants)
class O38():
    # 'Input_EIA_New_Plants'!O38
    value = "PV"

@register(Input_EIA_New_Plants)
class P38():
    # 'Input_EIA_New_Plants'!P38
    value = "SUN"

@register(Input_EIA_New_Plants)
class R38():
    # 'Input_EIA_New_Plants'!R38
    value = 12

@register(Input_EIA_New_Plants)
class S38():
    # 'Input_EIA_New_Plants'!S38
    value = 2008

@register(Input_EIA_New_Plants)
class V38():
    # 'Input_EIA_New_Plants'!V38
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A39():
    # 'Input_EIA_New_Plants'!A39
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V39&S39"
    @eval_fn
    def A39():
        v39_1 = Input_EIA_New_Plants.V39()
        s39_1 = Input_EIA_New_Plants.S39()
        var_1 = concat(v39_1, s39_1)
        return var_1

@register(Input_EIA_New_Plants)
class B39():
    # 'Input_EIA_New_Plants'!B39
    value = "HI"

@register(Input_EIA_New_Plants)
class C39():
    # 'Input_EIA_New_Plants'!C39
    value = "Maui"

@register(Input_EIA_New_Plants)
class D39():
    # 'Input_EIA_New_Plants'!D39
    value = 55910

@register(Input_EIA_New_Plants)
class E39():
    # 'Input_EIA_New_Plants'!E39
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F39():
    # 'Input_EIA_New_Plants'!F39
    value = 56667

@register(Input_EIA_New_Plants)
class G39():
    # 'Input_EIA_New_Plants'!G39
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H39():
    # 'Input_EIA_New_Plants'!H39
    value = "0009"

@register(Input_EIA_New_Plants)
class J39():
    # 'Input_EIA_New_Plants'!J39
    value = "OP"

@register(Input_EIA_New_Plants)
class K39():
    # 'Input_EIA_New_Plants'!K39
    value = 0.1

@register(Input_EIA_New_Plants)
class L39():
    # 'Input_EIA_New_Plants'!L39
    value = 0.1

@register(Input_EIA_New_Plants)
class M39():
    # 'Input_EIA_New_Plants'!M39
    value = 0.1

@register(Input_EIA_New_Plants)
class N39():
    # 'Input_EIA_New_Plants'!N39
    value = 22

@register(Input_EIA_New_Plants)
class O39():
    # 'Input_EIA_New_Plants'!O39
    value = "PV"

@register(Input_EIA_New_Plants)
class P39():
    # 'Input_EIA_New_Plants'!P39
    value = "SUN"

@register(Input_EIA_New_Plants)
class R39():
    # 'Input_EIA_New_Plants'!R39
    value = 12

@register(Input_EIA_New_Plants)
class S39():
    # 'Input_EIA_New_Plants'!S39
    value = 2008

@register(Input_EIA_New_Plants)
class V39():
    # 'Input_EIA_New_Plants'!V39
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A40():
    # 'Input_EIA_New_Plants'!A40
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V40&S40"
    @eval_fn
    def A40():
        v40_1 = Input_EIA_New_Plants.V40()
        s40_1 = Input_EIA_New_Plants.S40()
        var_1 = concat(v40_1, s40_1)
        return var_1

@register(Input_EIA_New_Plants)
class B40():
    # 'Input_EIA_New_Plants'!B40
    value = "HI"

@register(Input_EIA_New_Plants)
class C40():
    # 'Input_EIA_New_Plants'!C40
    value = "Maui"

@register(Input_EIA_New_Plants)
class D40():
    # 'Input_EIA_New_Plants'!D40
    value = 55910

@register(Input_EIA_New_Plants)
class E40():
    # 'Input_EIA_New_Plants'!E40
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F40():
    # 'Input_EIA_New_Plants'!F40
    value = 56667

@register(Input_EIA_New_Plants)
class G40():
    # 'Input_EIA_New_Plants'!G40
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H40():
    # 'Input_EIA_New_Plants'!H40
    value = "0010"

@register(Input_EIA_New_Plants)
class J40():
    # 'Input_EIA_New_Plants'!J40
    value = "OP"

@register(Input_EIA_New_Plants)
class K40():
    # 'Input_EIA_New_Plants'!K40
    value = 0.1

@register(Input_EIA_New_Plants)
class L40():
    # 'Input_EIA_New_Plants'!L40
    value = 0.1

@register(Input_EIA_New_Plants)
class M40():
    # 'Input_EIA_New_Plants'!M40
    value = 0.1

@register(Input_EIA_New_Plants)
class N40():
    # 'Input_EIA_New_Plants'!N40
    value = 22

@register(Input_EIA_New_Plants)
class O40():
    # 'Input_EIA_New_Plants'!O40
    value = "PV"

@register(Input_EIA_New_Plants)
class P40():
    # 'Input_EIA_New_Plants'!P40
    value = "SUN"

@register(Input_EIA_New_Plants)
class R40():
    # 'Input_EIA_New_Plants'!R40
    value = 12

@register(Input_EIA_New_Plants)
class S40():
    # 'Input_EIA_New_Plants'!S40
    value = 2008

@register(Input_EIA_New_Plants)
class V40():
    # 'Input_EIA_New_Plants'!V40
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A41():
    # 'Input_EIA_New_Plants'!A41
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V41&S41"
    @eval_fn
    def A41():
        v41_1 = Input_EIA_New_Plants.V41()
        s41_1 = Input_EIA_New_Plants.S41()
        var_1 = concat(v41_1, s41_1)
        return var_1

@register(Input_EIA_New_Plants)
class B41():
    # 'Input_EIA_New_Plants'!B41
    value = "HI"

@register(Input_EIA_New_Plants)
class C41():
    # 'Input_EIA_New_Plants'!C41
    value = "Maui"

@register(Input_EIA_New_Plants)
class D41():
    # 'Input_EIA_New_Plants'!D41
    value = 55910

@register(Input_EIA_New_Plants)
class E41():
    # 'Input_EIA_New_Plants'!E41
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F41():
    # 'Input_EIA_New_Plants'!F41
    value = 56667

@register(Input_EIA_New_Plants)
class G41():
    # 'Input_EIA_New_Plants'!G41
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H41():
    # 'Input_EIA_New_Plants'!H41
    value = "0011"

@register(Input_EIA_New_Plants)
class J41():
    # 'Input_EIA_New_Plants'!J41
    value = "OP"

@register(Input_EIA_New_Plants)
class K41():
    # 'Input_EIA_New_Plants'!K41
    value = 0.1

@register(Input_EIA_New_Plants)
class L41():
    # 'Input_EIA_New_Plants'!L41
    value = 0.1

@register(Input_EIA_New_Plants)
class M41():
    # 'Input_EIA_New_Plants'!M41
    value = 0.1

@register(Input_EIA_New_Plants)
class N41():
    # 'Input_EIA_New_Plants'!N41
    value = 22

@register(Input_EIA_New_Plants)
class O41():
    # 'Input_EIA_New_Plants'!O41
    value = "PV"

@register(Input_EIA_New_Plants)
class P41():
    # 'Input_EIA_New_Plants'!P41
    value = "SUN"

@register(Input_EIA_New_Plants)
class R41():
    # 'Input_EIA_New_Plants'!R41
    value = 12

@register(Input_EIA_New_Plants)
class S41():
    # 'Input_EIA_New_Plants'!S41
    value = 2008

@register(Input_EIA_New_Plants)
class V41():
    # 'Input_EIA_New_Plants'!V41
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A42():
    # 'Input_EIA_New_Plants'!A42
    value = "Solar Thermal and Photovoltaic2008"
    formula = "=V42&S42"
    @eval_fn
    def A42():
        v42_1 = Input_EIA_New_Plants.V42()
        s42_1 = Input_EIA_New_Plants.S42()
        var_1 = concat(v42_1, s42_1)
        return var_1

@register(Input_EIA_New_Plants)
class B42():
    # 'Input_EIA_New_Plants'!B42
    value = "HI"

@register(Input_EIA_New_Plants)
class C42():
    # 'Input_EIA_New_Plants'!C42
    value = "Maui"

@register(Input_EIA_New_Plants)
class D42():
    # 'Input_EIA_New_Plants'!D42
    value = 55910

@register(Input_EIA_New_Plants)
class E42():
    # 'Input_EIA_New_Plants'!E42
    value = "Lanai Sustainability Research LLC"

@register(Input_EIA_New_Plants)
class F42():
    # 'Input_EIA_New_Plants'!F42
    value = 56667

@register(Input_EIA_New_Plants)
class G42():
    # 'Input_EIA_New_Plants'!G42
    value = "Lanai Solar-Electric Plant"

@register(Input_EIA_New_Plants)
class H42():
    # 'Input_EIA_New_Plants'!H42
    value = "0012"

@register(Input_EIA_New_Plants)
class J42():
    # 'Input_EIA_New_Plants'!J42
    value = "OP"

@register(Input_EIA_New_Plants)
class K42():
    # 'Input_EIA_New_Plants'!K42
    value = 0.1

@register(Input_EIA_New_Plants)
class L42():
    # 'Input_EIA_New_Plants'!L42
    value = 0.1

@register(Input_EIA_New_Plants)
class M42():
    # 'Input_EIA_New_Plants'!M42
    value = 0.1

@register(Input_EIA_New_Plants)
class N42():
    # 'Input_EIA_New_Plants'!N42
    value = 22

@register(Input_EIA_New_Plants)
class O42():
    # 'Input_EIA_New_Plants'!O42
    value = "PV"

@register(Input_EIA_New_Plants)
class P42():
    # 'Input_EIA_New_Plants'!P42
    value = "SUN"

@register(Input_EIA_New_Plants)
class R42():
    # 'Input_EIA_New_Plants'!R42
    value = 12

@register(Input_EIA_New_Plants)
class S42():
    # 'Input_EIA_New_Plants'!S42
    value = 2008

@register(Input_EIA_New_Plants)
class V42():
    # 'Input_EIA_New_Plants'!V42
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A43():
    # 'Input_EIA_New_Plants'!A43
    value = "Distillate Fuel Oil2009"
    formula = "=V43&S43"
    @eval_fn
    def A43():
        v43_1 = Input_EIA_New_Plants.V43()
        s43_1 = Input_EIA_New_Plants.S43()
        var_1 = concat(v43_1, s43_1)
        return var_1

@register(Input_EIA_New_Plants)
class B43():
    # 'Input_EIA_New_Plants'!B43
    value = "HI"

@register(Input_EIA_New_Plants)
class C43():
    # 'Input_EIA_New_Plants'!C43
    value = "Hawaii"

@register(Input_EIA_New_Plants)
class D43():
    # 'Input_EIA_New_Plants'!D43
    value = 8287

@register(Input_EIA_New_Plants)
class E43():
    # 'Input_EIA_New_Plants'!E43
    value = "Hawaii Electric Light Co Inc"

@register(Input_EIA_New_Plants)
class F43():
    # 'Input_EIA_New_Plants'!F43
    value = 8083

@register(Input_EIA_New_Plants)
class G43():
    # 'Input_EIA_New_Plants'!G43
    value = "Keahole"

@register(Input_EIA_New_Plants)
class H43():
    # 'Input_EIA_New_Plants'!H43
    value = "7"

@register(Input_EIA_New_Plants)
class J43():
    # 'Input_EIA_New_Plants'!J43
    value = "OP"

@register(Input_EIA_New_Plants)
class K43():
    # 'Input_EIA_New_Plants'!K43
    value = 18

@register(Input_EIA_New_Plants)
class L43():
    # 'Input_EIA_New_Plants'!L43
    value = 16

@register(Input_EIA_New_Plants)
class M43():
    # 'Input_EIA_New_Plants'!M43
    value = 16

@register(Input_EIA_New_Plants)
class N43():
    # 'Input_EIA_New_Plants'!N43
    value = 22

@register(Input_EIA_New_Plants)
class O43():
    # 'Input_EIA_New_Plants'!O43
    value = "CA"

@register(Input_EIA_New_Plants)
class P43():
    # 'Input_EIA_New_Plants'!P43
    value = "DFO"

@register(Input_EIA_New_Plants)
class R43():
    # 'Input_EIA_New_Plants'!R43
    value = 6

@register(Input_EIA_New_Plants)
class S43():
    # 'Input_EIA_New_Plants'!S43
    value = 2009

@register(Input_EIA_New_Plants)
class V43():
    # 'Input_EIA_New_Plants'!V43
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A44():
    # 'Input_EIA_New_Plants'!A44
    value = "Other Biomass2009"
    formula = "=V44&S44"
    @eval_fn
    def A44():
        v44_1 = Input_EIA_New_Plants.V44()
        s44_1 = Input_EIA_New_Plants.S44()
        var_1 = concat(v44_1, s44_1)
        return var_1

@register(Input_EIA_New_Plants)
class B44():
    # 'Input_EIA_New_Plants'!B44
    value = "HI"

@register(Input_EIA_New_Plants)
class C44():
    # 'Input_EIA_New_Plants'!C44
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D44():
    # 'Input_EIA_New_Plants'!D44
    value = 19547

@register(Input_EIA_New_Plants)
class E44():
    # 'Input_EIA_New_Plants'!E44
    value = "Hawaiian Electric Co Inc"

@register(Input_EIA_New_Plants)
class F44():
    # 'Input_EIA_New_Plants'!F44
    value = 56329

@register(Input_EIA_New_Plants)
class G44():
    # 'Input_EIA_New_Plants'!G44
    value = "Campbell Indust. Park Generating Station"

@register(Input_EIA_New_Plants)
class H44():
    # 'Input_EIA_New_Plants'!H44
    value = "CIP1"

@register(Input_EIA_New_Plants)
class J44():
    # 'Input_EIA_New_Plants'!J44
    value = "OP"

@register(Input_EIA_New_Plants)
class K44():
    # 'Input_EIA_New_Plants'!K44
    value = 113

@register(Input_EIA_New_Plants)
class L44():
    # 'Input_EIA_New_Plants'!L44
    value = 113

@register(Input_EIA_New_Plants)
class M44():
    # 'Input_EIA_New_Plants'!M44
    value = 113

@register(Input_EIA_New_Plants)
class N44():
    # 'Input_EIA_New_Plants'!N44
    value = 22

@register(Input_EIA_New_Plants)
class O44():
    # 'Input_EIA_New_Plants'!O44
    value = "GT"

@register(Input_EIA_New_Plants)
class P44():
    # 'Input_EIA_New_Plants'!P44
    value = "OBL"

@register(Input_EIA_New_Plants)
class Q44():
    # 'Input_EIA_New_Plants'!Q44
    value = "DFO"

@register(Input_EIA_New_Plants)
class R44():
    # 'Input_EIA_New_Plants'!R44
    value = 7

@register(Input_EIA_New_Plants)
class S44():
    # 'Input_EIA_New_Plants'!S44
    value = 2009

@register(Input_EIA_New_Plants)
class V44():
    # 'Input_EIA_New_Plants'!V44
    value = "Other Biomass"

@register(Input_EIA_New_Plants)
class A45():
    # 'Input_EIA_New_Plants'!A45
    value = "Distillate Fuel Oil2010"
    formula = "=V45&S45"
    @eval_fn
    def A45():
        v45_1 = Input_EIA_New_Plants.V45()
        s45_1 = Input_EIA_New_Plants.S45()
        var_1 = concat(v45_1, s45_1)
        return var_1

@register(Input_EIA_New_Plants)
class B45():
    # 'Input_EIA_New_Plants'!B45
    value = "HI"

@register(Input_EIA_New_Plants)
class C45():
    # 'Input_EIA_New_Plants'!C45
    value = "KAUAI"

@register(Input_EIA_New_Plants)
class D45():
    # 'Input_EIA_New_Plants'!D45
    value = 7019

@register(Input_EIA_New_Plants)
class E45():
    # 'Input_EIA_New_Plants'!E45
    value = "Gay & Robinson Inc"

@register(Input_EIA_New_Plants)
class F45():
    # 'Input_EIA_New_Plants'!F45
    value = 50333

@register(Input_EIA_New_Plants)
class G45():
    # 'Input_EIA_New_Plants'!G45
    value = "Gay Robinson"

@register(Input_EIA_New_Plants)
class H45():
    # 'Input_EIA_New_Plants'!H45
    value = "DSL5"

@register(Input_EIA_New_Plants)
class J45():
    # 'Input_EIA_New_Plants'!J45
    value = "SB"

@register(Input_EIA_New_Plants)
class K45():
    # 'Input_EIA_New_Plants'!K45
    value = 0.5

@register(Input_EIA_New_Plants)
class L45():
    # 'Input_EIA_New_Plants'!L45
    value = 0.5

@register(Input_EIA_New_Plants)
class M45():
    # 'Input_EIA_New_Plants'!M45
    value = 0.5

@register(Input_EIA_New_Plants)
class N45():
    # 'Input_EIA_New_Plants'!N45
    value = 311

@register(Input_EIA_New_Plants)
class O45():
    # 'Input_EIA_New_Plants'!O45
    value = "IC"

@register(Input_EIA_New_Plants)
class P45():
    # 'Input_EIA_New_Plants'!P45
    value = "DFO"

@register(Input_EIA_New_Plants)
class R45():
    # 'Input_EIA_New_Plants'!R45
    value = 4

@register(Input_EIA_New_Plants)
class S45():
    # 'Input_EIA_New_Plants'!S45
    value = 2010

@register(Input_EIA_New_Plants)
class V45():
    # 'Input_EIA_New_Plants'!V45
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A46():
    # 'Input_EIA_New_Plants'!A46
    value = "Distillate Fuel Oil2010"
    formula = "=V46&S46"
    @eval_fn
    def A46():
        v46_1 = Input_EIA_New_Plants.V46()
        s46_1 = Input_EIA_New_Plants.S46()
        var_1 = concat(v46_1, s46_1)
        return var_1

@register(Input_EIA_New_Plants)
class B46():
    # 'Input_EIA_New_Plants'!B46
    value = "HI"

@register(Input_EIA_New_Plants)
class C46():
    # 'Input_EIA_New_Plants'!C46
    value = "KAUAI"

@register(Input_EIA_New_Plants)
class D46():
    # 'Input_EIA_New_Plants'!D46
    value = 7019

@register(Input_EIA_New_Plants)
class E46():
    # 'Input_EIA_New_Plants'!E46
    value = "Gay & Robinson Inc"

@register(Input_EIA_New_Plants)
class F46():
    # 'Input_EIA_New_Plants'!F46
    value = 50333

@register(Input_EIA_New_Plants)
class G46():
    # 'Input_EIA_New_Plants'!G46
    value = "Gay Robinson"

@register(Input_EIA_New_Plants)
class H46():
    # 'Input_EIA_New_Plants'!H46
    value = "DSL6"

@register(Input_EIA_New_Plants)
class J46():
    # 'Input_EIA_New_Plants'!J46
    value = "SB"

@register(Input_EIA_New_Plants)
class K46():
    # 'Input_EIA_New_Plants'!K46
    value = 0.5

@register(Input_EIA_New_Plants)
class L46():
    # 'Input_EIA_New_Plants'!L46
    value = 0.5

@register(Input_EIA_New_Plants)
class M46():
    # 'Input_EIA_New_Plants'!M46
    value = 0.5

@register(Input_EIA_New_Plants)
class N46():
    # 'Input_EIA_New_Plants'!N46
    value = 311

@register(Input_EIA_New_Plants)
class O46():
    # 'Input_EIA_New_Plants'!O46
    value = "IC"

@register(Input_EIA_New_Plants)
class P46():
    # 'Input_EIA_New_Plants'!P46
    value = "DFO"

@register(Input_EIA_New_Plants)
class R46():
    # 'Input_EIA_New_Plants'!R46
    value = 4

@register(Input_EIA_New_Plants)
class S46():
    # 'Input_EIA_New_Plants'!S46
    value = 2010

@register(Input_EIA_New_Plants)
class V46():
    # 'Input_EIA_New_Plants'!V46
    value = "Distillate Fuel Oil"

@register(Input_EIA_New_Plants)
class A47():
    # 'Input_EIA_New_Plants'!A47
    value = "Solar Thermal and Photovoltaic2010"
    formula = "=V47&S47"
    @eval_fn
    def A47():
        v47_1 = Input_EIA_New_Plants.V47()
        s47_1 = Input_EIA_New_Plants.S47()
        var_1 = concat(v47_1, s47_1)
        return var_1

@register(Input_EIA_New_Plants)
class B47():
    # 'Input_EIA_New_Plants'!B47
    value = "HI"

@register(Input_EIA_New_Plants)
class C47():
    # 'Input_EIA_New_Plants'!C47
    value = "Kauai"

@register(Input_EIA_New_Plants)
class D47():
    # 'Input_EIA_New_Plants'!D47
    value = 56863

@register(Input_EIA_New_Plants)
class E47():
    # 'Input_EIA_New_Plants'!E47
    value = "Kapaa Solar LLC"

@register(Input_EIA_New_Plants)
class F47():
    # 'Input_EIA_New_Plants'!F47
    value = 57525

@register(Input_EIA_New_Plants)
class G47():
    # 'Input_EIA_New_Plants'!G47
    value = "Kapaa Photovoltaic Project"

@register(Input_EIA_New_Plants)
class H47():
    # 'Input_EIA_New_Plants'!H47
    value = "KSPV"

@register(Input_EIA_New_Plants)
class J47():
    # 'Input_EIA_New_Plants'!J47
    value = "OP"

@register(Input_EIA_New_Plants)
class K47():
    # 'Input_EIA_New_Plants'!K47
    value = 1

@register(Input_EIA_New_Plants)
class L47():
    # 'Input_EIA_New_Plants'!L47
    value = 1

@register(Input_EIA_New_Plants)
class M47():
    # 'Input_EIA_New_Plants'!M47
    value = 1

@register(Input_EIA_New_Plants)
class N47():
    # 'Input_EIA_New_Plants'!N47
    value = 22

@register(Input_EIA_New_Plants)
class O47():
    # 'Input_EIA_New_Plants'!O47
    value = "PV"

@register(Input_EIA_New_Plants)
class P47():
    # 'Input_EIA_New_Plants'!P47
    value = "SUN"

@register(Input_EIA_New_Plants)
class R47():
    # 'Input_EIA_New_Plants'!R47
    value = 12

@register(Input_EIA_New_Plants)
class S47():
    # 'Input_EIA_New_Plants'!S47
    value = 2010

@register(Input_EIA_New_Plants)
class T47():
    # 'Input_EIA_New_Plants'!T47
    value = 4

@register(Input_EIA_New_Plants)
class V47():
    # 'Input_EIA_New_Plants'!V47
    value = "Solar Thermal and Photovoltaic"

@register(Input_EIA_New_Plants)
class A48():
    # 'Input_EIA_New_Plants'!A48
    value = "Cogenerator2011"
    formula = "=V48&S48"
    @eval_fn
    def A48():
        v48_1 = Input_EIA_New_Plants.V48()
        s48_1 = Input_EIA_New_Plants.S48()
        var_1 = concat(v48_1, s48_1)
        return var_1

@register(Input_EIA_New_Plants)
class B48():
    # 'Input_EIA_New_Plants'!B48
    value = "HI"

@register(Input_EIA_New_Plants)
class C48():
    # 'Input_EIA_New_Plants'!C48
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D48():
    # 'Input_EIA_New_Plants'!D48
    value = 3453

@register(Input_EIA_New_Plants)
class E48():
    # 'Input_EIA_New_Plants'!E48
    value = "Chevron Refinery-Hawaii"

@register(Input_EIA_New_Plants)
class F48():
    # 'Input_EIA_New_Plants'!F48
    value = 10194

@register(Input_EIA_New_Plants)
class G48():
    # 'Input_EIA_New_Plants'!G48
    value = "Hawaii Cogen"

@register(Input_EIA_New_Plants)
class H48():
    # 'Input_EIA_New_Plants'!H48
    value = "GEN4"

@register(Input_EIA_New_Plants)
class J48():
    # 'Input_EIA_New_Plants'!J48
    value = "OP"

@register(Input_EIA_New_Plants)
class K48():
    # 'Input_EIA_New_Plants'!K48
    value = 3.2

@register(Input_EIA_New_Plants)
class L48():
    # 'Input_EIA_New_Plants'!L48
    value = 3.2

@register(Input_EIA_New_Plants)
class M48():
    # 'Input_EIA_New_Plants'!M48
    value = 3.2

@register(Input_EIA_New_Plants)
class N48():
    # 'Input_EIA_New_Plants'!N48
    value = 32411

@register(Input_EIA_New_Plants)
class O48():
    # 'Input_EIA_New_Plants'!O48
    value = "GT"

@register(Input_EIA_New_Plants)
class P48():
    # 'Input_EIA_New_Plants'!P48
    value = "OG"

@register(Input_EIA_New_Plants)
class Q48():
    # 'Input_EIA_New_Plants'!Q48
    value = "DFO"

@register(Input_EIA_New_Plants)
class R48():
    # 'Input_EIA_New_Plants'!R48
    value = 6

@register(Input_EIA_New_Plants)
class S48():
    # 'Input_EIA_New_Plants'!S48
    value = 2011

@register(Input_EIA_New_Plants)
class V48():
    # 'Input_EIA_New_Plants'!V48
    value = "Cogenerator"

@register(Input_EIA_New_Plants)
class A49():
    # 'Input_EIA_New_Plants'!A49
    value = "Wind2011"
    formula = "=V49&S49"
    @eval_fn
    def A49():
        v49_1 = Input_EIA_New_Plants.V49()
        s49_1 = Input_EIA_New_Plants.S49()
        var_1 = concat(v49_1, s49_1)
        return var_1

@register(Input_EIA_New_Plants)
class B49():
    # 'Input_EIA_New_Plants'!B49
    value = "HI"

@register(Input_EIA_New_Plants)
class C49():
    # 'Input_EIA_New_Plants'!C49
    value = "Honolulu"

@register(Input_EIA_New_Plants)
class D49():
    # 'Input_EIA_New_Plants'!D49
    value = 56338

@register(Input_EIA_New_Plants)
class E49():
    # 'Input_EIA_New_Plants'!E49
    value = "Kahuku Wind Power LLC"

@register(Input_EIA_New_Plants)
class F49():
    # 'Input_EIA_New_Plants'!F49
    value = 57087

@register(Input_EIA_New_Plants)
class G49():
    # 'Input_EIA_New_Plants'!G49
    value = "Kahuku Wind Power LLC"

@register(Input_EIA_New_Plants)
class H49():
    # 'Input_EIA_New_Plants'!H49
    value = "1"

@register(Input_EIA_New_Plants)
class J49():
    # 'Input_EIA_New_Plants'!J49
    value = "OP"

@register(Input_EIA_New_Plants)
class K49():
    # 'Input_EIA_New_Plants'!K49
    value = 30

@register(Input_EIA_New_Plants)
class L49():
    # 'Input_EIA_New_Plants'!L49
    value = 30

@register(Input_EIA_New_Plants)
class M49():
    # 'Input_EIA_New_Plants'!M49
    value = 30

@register(Input_EIA_New_Plants)
class N49():
    # 'Input_EIA_New_Plants'!N49
    value = 22

@register(Input_EIA_New_Plants)
class O49():
    # 'Input_EIA_New_Plants'!O49
    value = "WT"

@register(Input_EIA_New_Plants)
class P49():
    # 'Input_EIA_New_Plants'!P49
    value = "WND"

@register(Input_EIA_New_Plants)
class R49():
    # 'Input_EIA_New_Plants'!R49
    value = 3

@register(Input_EIA_New_Plants)
class S49():
    # 'Input_EIA_New_Plants'!S49
    value = 2011

@register(Input_EIA_New_Plants)
class V49():
    # 'Input_EIA_New_Plants'!V49
    value = "Wind"