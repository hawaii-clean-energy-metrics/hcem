# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Metric_4_5_7_8_Data_QC = Worksheet('Metric_4_5_7_8_Data_QC', 10, 10)



@register(Metric_4_5_7_8_Data_QC)
class B2():
    # 'Metric_4_5_7_8_Data_QC'!B2
    value = "The Following tables compare 2006 EIA reported expenditures to 2006 expenditures as calculated in this model. Overall, sector-level expenditures appear to be fairly close, within or close to 10%. Industrial appears to be calculated higher than EIA's report by about 18%. The total portfolio difference is around 6%."

@register(Metric_4_5_7_8_Data_QC)
class A8():
    # 'Metric_4_5_7_8_Data_QC'!A8
    value = "Residential"

@register(Metric_4_5_7_8_Data_QC)
class E8():
    # 'Metric_4_5_7_8_Data_QC'!E8
    value = "EIA Reported Expenditures"

@register(Metric_4_5_7_8_Data_QC)
class F8():
    # 'Metric_4_5_7_8_Data_QC'!F8
    value = "Calculated Expenditures"

@register(Metric_4_5_7_8_Data_QC)
class G8():
    # 'Metric_4_5_7_8_Data_QC'!G8
    value = "Difference"

@register(Metric_4_5_7_8_Data_QC)
class H8():
    # 'Metric_4_5_7_8_Data_QC'!H8
    value = "Difference as % of EIA"

@register(Metric_4_5_7_8_Data_QC)
class I8():
    # 'Metric_4_5_7_8_Data_QC'!I8
    value = "Difference as % of Sector Total"

@register(Metric_4_5_7_8_Data_QC)
class B9():
    # 'Metric_4_5_7_8_Data_QC'!B9
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class C9():
    # 'Metric_4_5_7_8_Data_QC'!C9
    value = "ESRCV"

@register(Metric_4_5_7_8_Data_QC)
class D9():
    # 'Metric_4_5_7_8_Data_QC'!D9
    value = "#N/A"
    formula = "=VLOOKUP(C9,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D9():
        c9_1 = Metric_4_5_7_8_Data_QC.C9()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c9_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E9():
    # 'Metric_4_5_7_8_Data_QC'!E9
    value = "#N/A"
    formula = "=VLOOKUP(C9,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E9():
        c9_1 = Metric_4_5_7_8_Data_QC.C9()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c9_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F9():
    # 'Metric_4_5_7_8_Data_QC'!F9
    value = 658719385.108
    formula = "=SUM('Dashboard M4 Cost Monthly'!G8:R8)"
    @eval_fn
    def F9():
        range_1 = Dashboard_M4_Cost_Monthly(7, 8, 18, 8)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G9():
    # 'Metric_4_5_7_8_Data_QC'!G9
    value = "#N/A"
    formula = "=F9-E9"
    @eval_fn
    def G9():
        f9_1 = Metric_4_5_7_8_Data_QC.F9()
        e9_1 = Metric_4_5_7_8_Data_QC.E9()
        var_1 = sub(f9_1, e9_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H9():
    # 'Metric_4_5_7_8_Data_QC'!H9
    value = "#N/A"
    formula = "=G9/E9"
    @eval_fn
    def H9():
        g9_1 = Metric_4_5_7_8_Data_QC.G9()
        e9_1 = Metric_4_5_7_8_Data_QC.E9()
        var_1 = divide(g9_1, e9_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I9():
    # 'Metric_4_5_7_8_Data_QC'!I9
    value = "#N/A"
    formula = "=G9/E18"
    @eval_fn
    def I9():
        g9_1 = Metric_4_5_7_8_Data_QC.G9()
        e18_1 = Metric_4_5_7_8_Data_QC.E18()
        var_1 = divide(g9_1, e18_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B10():
    # 'Metric_4_5_7_8_Data_QC'!B10
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class C10():
    # 'Metric_4_5_7_8_Data_QC'!C10
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E10():
    # 'Metric_4_5_7_8_Data_QC'!E10
    value = 0
    formula = "=VLOOKUP(C10,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E10():
        c10_1 = Metric_4_5_7_8_Data_QC.C10()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c10_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F10():
    # 'Metric_4_5_7_8_Data_QC'!F10
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G9:R9)"
    @eval_fn
    def F10():
        range_1 = Dashboard_M4_Cost_Monthly(7, 9, 18, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G10():
    # 'Metric_4_5_7_8_Data_QC'!G10
    value = 0
    formula = "=F10-E10"
    @eval_fn
    def G10():
        f10_1 = Metric_4_5_7_8_Data_QC.F10()
        e10_1 = Metric_4_5_7_8_Data_QC.E10()
        var_1 = sub(f10_1, e10_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I10():
    # 'Metric_4_5_7_8_Data_QC'!I10
    value = "#N/A"
    formula = "=G10/E18"
    @eval_fn
    def I10():
        g10_1 = Metric_4_5_7_8_Data_QC.G10()
        e18_1 = Metric_4_5_7_8_Data_QC.E18()
        var_1 = divide(g10_1, e18_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B11():
    # 'Metric_4_5_7_8_Data_QC'!B11
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class C11():
    # 'Metric_4_5_7_8_Data_QC'!C11
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E11():
    # 'Metric_4_5_7_8_Data_QC'!E11
    value = 0
    formula = "=VLOOKUP(C11,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E11():
        c11_1 = Metric_4_5_7_8_Data_QC.C11()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c11_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F11():
    # 'Metric_4_5_7_8_Data_QC'!F11
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G10:R10)"
    @eval_fn
    def F11():
        range_1 = Dashboard_M4_Cost_Monthly(7, 10, 18, 10)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G11():
    # 'Metric_4_5_7_8_Data_QC'!G11
    value = 0
    formula = "=F11-E11"
    @eval_fn
    def G11():
        f11_1 = Metric_4_5_7_8_Data_QC.F11()
        e11_1 = Metric_4_5_7_8_Data_QC.E11()
        var_1 = sub(f11_1, e11_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I11():
    # 'Metric_4_5_7_8_Data_QC'!I11
    value = "#N/A"
    formula = "=G11/E18"
    @eval_fn
    def I11():
        g11_1 = Metric_4_5_7_8_Data_QC.G11()
        e18_1 = Metric_4_5_7_8_Data_QC.E18()
        var_1 = divide(g11_1, e18_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B12():
    # 'Metric_4_5_7_8_Data_QC'!B12
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class C12():
    # 'Metric_4_5_7_8_Data_QC'!C12
    value = "DFRCV"

@register(Metric_4_5_7_8_Data_QC)
class D12():
    # 'Metric_4_5_7_8_Data_QC'!D12
    value = "#N/A"
    formula = "=VLOOKUP(C12,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D12():
        c12_1 = Metric_4_5_7_8_Data_QC.C12()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c12_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E12():
    # 'Metric_4_5_7_8_Data_QC'!E12
    value = "#N/A"
    formula = "=VLOOKUP(C12,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E12():
        c12_1 = Metric_4_5_7_8_Data_QC.C12()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c12_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F12():
    # 'Metric_4_5_7_8_Data_QC'!F12
    value = 475045.314404
    formula = "=SUM('Dashboard M4 Cost Monthly'!G11:R11)"
    @eval_fn
    def F12():
        range_1 = Dashboard_M4_Cost_Monthly(7, 11, 18, 11)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G12():
    # 'Metric_4_5_7_8_Data_QC'!G12
    value = "#N/A"
    formula = "=F12-E12"
    @eval_fn
    def G12():
        f12_1 = Metric_4_5_7_8_Data_QC.F12()
        e12_1 = Metric_4_5_7_8_Data_QC.E12()
        var_1 = sub(f12_1, e12_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H12():
    # 'Metric_4_5_7_8_Data_QC'!H12
    value = "#N/A"
    formula = "=G12/E12"
    @eval_fn
    def H12():
        g12_1 = Metric_4_5_7_8_Data_QC.G12()
        e12_1 = Metric_4_5_7_8_Data_QC.E12()
        var_1 = divide(g12_1, e12_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I12():
    # 'Metric_4_5_7_8_Data_QC'!I12
    value = "#N/A"
    formula = "=G12/E18"
    @eval_fn
    def I12():
        g12_1 = Metric_4_5_7_8_Data_QC.G12()
        e18_1 = Metric_4_5_7_8_Data_QC.E18()
        var_1 = divide(g12_1, e18_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B13():
    # 'Metric_4_5_7_8_Data_QC'!B13
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class C13():
    # 'Metric_4_5_7_8_Data_QC'!C13
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E13():
    # 'Metric_4_5_7_8_Data_QC'!E13
    value = 0
    formula = "=VLOOKUP(C13,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E13():
        c13_1 = Metric_4_5_7_8_Data_QC.C13()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c13_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F13():
    # 'Metric_4_5_7_8_Data_QC'!F13
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G12:R12)"
    @eval_fn
    def F13():
        range_1 = Dashboard_M4_Cost_Monthly(7, 12, 18, 12)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G13():
    # 'Metric_4_5_7_8_Data_QC'!G13
    value = 0
    formula = "=F13-E13"
    @eval_fn
    def G13():
        f13_1 = Metric_4_5_7_8_Data_QC.F13()
        e13_1 = Metric_4_5_7_8_Data_QC.E13()
        var_1 = sub(f13_1, e13_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I13():
    # 'Metric_4_5_7_8_Data_QC'!I13
    value = "#N/A"
    formula = "=G13/E18"
    @eval_fn
    def I13():
        g13_1 = Metric_4_5_7_8_Data_QC.G13()
        e18_1 = Metric_4_5_7_8_Data_QC.E18()
        var_1 = divide(g13_1, e18_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B14():
    # 'Metric_4_5_7_8_Data_QC'!B14
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class C14():
    # 'Metric_4_5_7_8_Data_QC'!C14
    value = "LGRCV"

@register(Metric_4_5_7_8_Data_QC)
class D14():
    # 'Metric_4_5_7_8_Data_QC'!D14
    value = "#N/A"
    formula = "=VLOOKUP(C14,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D14():
        c14_1 = Metric_4_5_7_8_Data_QC.C14()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c14_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E14():
    # 'Metric_4_5_7_8_Data_QC'!E14
    value = "#N/A"
    formula = "=VLOOKUP(C14,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E14():
        c14_1 = Metric_4_5_7_8_Data_QC.C14()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c14_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F14():
    # 'Metric_4_5_7_8_Data_QC'!F14
    value = 20387945.546
    formula = "=SUM('Dashboard M4 Cost Monthly'!G13:R13)"
    @eval_fn
    def F14():
        range_1 = Dashboard_M4_Cost_Monthly(7, 13, 18, 13)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G14():
    # 'Metric_4_5_7_8_Data_QC'!G14
    value = "#N/A"
    formula = "=F14-E14"
    @eval_fn
    def G14():
        f14_1 = Metric_4_5_7_8_Data_QC.F14()
        e14_1 = Metric_4_5_7_8_Data_QC.E14()
        var_1 = sub(f14_1, e14_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H14():
    # 'Metric_4_5_7_8_Data_QC'!H14
    value = "#N/A"
    formula = "=G14/E14"
    @eval_fn
    def H14():
        g14_1 = Metric_4_5_7_8_Data_QC.G14()
        e14_1 = Metric_4_5_7_8_Data_QC.E14()
        var_1 = divide(g14_1, e14_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I14():
    # 'Metric_4_5_7_8_Data_QC'!I14
    value = "#N/A"
    formula = "=G14/E18"
    @eval_fn
    def I14():
        g14_1 = Metric_4_5_7_8_Data_QC.G14()
        e18_1 = Metric_4_5_7_8_Data_QC.E18()
        var_1 = divide(g14_1, e18_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B15():
    # 'Metric_4_5_7_8_Data_QC'!B15
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class C15():
    # 'Metric_4_5_7_8_Data_QC'!C15
    value = "NGRCV"

@register(Metric_4_5_7_8_Data_QC)
class D15():
    # 'Metric_4_5_7_8_Data_QC'!D15
    value = "#N/A"
    formula = "=VLOOKUP(C15,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D15():
        c15_1 = Metric_4_5_7_8_Data_QC.C15()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c15_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E15():
    # 'Metric_4_5_7_8_Data_QC'!E15
    value = "#N/A"
    formula = "=VLOOKUP(C15,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E15():
        c15_1 = Metric_4_5_7_8_Data_QC.C15()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c15_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F15():
    # 'Metric_4_5_7_8_Data_QC'!F15
    value = 14255645.3123
    formula = "=SUM('Dashboard M4 Cost Monthly'!G14:R14)"
    @eval_fn
    def F15():
        range_1 = Dashboard_M4_Cost_Monthly(7, 14, 18, 14)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G15():
    # 'Metric_4_5_7_8_Data_QC'!G15
    value = "#N/A"
    formula = "=F15-E15"
    @eval_fn
    def G15():
        f15_1 = Metric_4_5_7_8_Data_QC.F15()
        e15_1 = Metric_4_5_7_8_Data_QC.E15()
        var_1 = sub(f15_1, e15_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H15():
    # 'Metric_4_5_7_8_Data_QC'!H15
    value = "#N/A"
    formula = "=G15/E15"
    @eval_fn
    def H15():
        g15_1 = Metric_4_5_7_8_Data_QC.G15()
        e15_1 = Metric_4_5_7_8_Data_QC.E15()
        var_1 = divide(g15_1, e15_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I15():
    # 'Metric_4_5_7_8_Data_QC'!I15
    value = "#N/A"
    formula = "=G15/E18"
    @eval_fn
    def I15():
        g15_1 = Metric_4_5_7_8_Data_QC.G15()
        e18_1 = Metric_4_5_7_8_Data_QC.E18()
        var_1 = divide(g15_1, e18_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B16():
    # 'Metric_4_5_7_8_Data_QC'!B16
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class C16():
    # 'Metric_4_5_7_8_Data_QC'!C16
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E16():
    # 'Metric_4_5_7_8_Data_QC'!E16
    value = 0
    formula = "=VLOOKUP(C16,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E16():
        c16_1 = Metric_4_5_7_8_Data_QC.C16()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c16_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F16():
    # 'Metric_4_5_7_8_Data_QC'!F16
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G15:R15)"
    @eval_fn
    def F16():
        range_1 = Dashboard_M4_Cost_Monthly(7, 15, 18, 15)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G16():
    # 'Metric_4_5_7_8_Data_QC'!G16
    value = 0
    formula = "=F16-E16"
    @eval_fn
    def G16():
        f16_1 = Metric_4_5_7_8_Data_QC.F16()
        e16_1 = Metric_4_5_7_8_Data_QC.E16()
        var_1 = sub(f16_1, e16_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I16():
    # 'Metric_4_5_7_8_Data_QC'!I16
    value = "#N/A"
    formula = "=G16/E18"
    @eval_fn
    def I16():
        g16_1 = Metric_4_5_7_8_Data_QC.G16()
        e18_1 = Metric_4_5_7_8_Data_QC.E18()
        var_1 = divide(g16_1, e18_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B17():
    # 'Metric_4_5_7_8_Data_QC'!B17
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class C17():
    # 'Metric_4_5_7_8_Data_QC'!C17
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E17():
    # 'Metric_4_5_7_8_Data_QC'!E17
    value = 0
    formula = "=VLOOKUP(C17,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E17():
        c17_1 = Metric_4_5_7_8_Data_QC.C17()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c17_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F17():
    # 'Metric_4_5_7_8_Data_QC'!F17
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G16:R16)"
    @eval_fn
    def F17():
        range_1 = Dashboard_M4_Cost_Monthly(7, 16, 18, 16)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G17():
    # 'Metric_4_5_7_8_Data_QC'!G17
    value = 0
    formula = "=F17-E17"
    @eval_fn
    def G17():
        f17_1 = Metric_4_5_7_8_Data_QC.F17()
        e17_1 = Metric_4_5_7_8_Data_QC.E17()
        var_1 = sub(f17_1, e17_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I17():
    # 'Metric_4_5_7_8_Data_QC'!I17
    value = "#N/A"
    formula = "=G17/E18"
    @eval_fn
    def I17():
        g17_1 = Metric_4_5_7_8_Data_QC.G17()
        e18_1 = Metric_4_5_7_8_Data_QC.E18()
        var_1 = divide(g17_1, e18_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B18():
    # 'Metric_4_5_7_8_Data_QC'!B18
    value = "Total"

@register(Metric_4_5_7_8_Data_QC)
class E18():
    # 'Metric_4_5_7_8_Data_QC'!E18
    value = "#N/A"
    formula = "=SUM(E9:E16)"
    @eval_fn
    def E18():
        range_1 = Metric_4_5_7_8_Data_QC(5, 9, 5, 16)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F18():
    # 'Metric_4_5_7_8_Data_QC'!F18
    value = 693838021.28
    formula = "=SUM(F9:F16)"
    @eval_fn
    def F18():
        range_1 = Metric_4_5_7_8_Data_QC(6, 9, 6, 16)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G18():
    # 'Metric_4_5_7_8_Data_QC'!G18
    value = "#N/A"
    formula = "=SUM(G9:G16)"
    @eval_fn
    def G18():
        range_1 = Metric_4_5_7_8_Data_QC(7, 9, 7, 16)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H18():
    # 'Metric_4_5_7_8_Data_QC'!H18
    value = "#N/A"
    formula = "=G18/E18"
    @eval_fn
    def H18():
        g18_1 = Metric_4_5_7_8_Data_QC.G18()
        e18_1 = Metric_4_5_7_8_Data_QC.E18()
        var_1 = divide(g18_1, e18_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class A19():
    # 'Metric_4_5_7_8_Data_QC'!A19
    value = "Commercial"

@register(Metric_4_5_7_8_Data_QC)
class E19():
    # 'Metric_4_5_7_8_Data_QC'!E19
    value = "EIA Reported"

@register(Metric_4_5_7_8_Data_QC)
class F19():
    # 'Metric_4_5_7_8_Data_QC'!F19
    value = "Calculated Expenditures"

@register(Metric_4_5_7_8_Data_QC)
class G19():
    # 'Metric_4_5_7_8_Data_QC'!G19
    value = "Difference"

@register(Metric_4_5_7_8_Data_QC)
class H19():
    # 'Metric_4_5_7_8_Data_QC'!H19
    value = "Difference as % of EIA"

@register(Metric_4_5_7_8_Data_QC)
class I19():
    # 'Metric_4_5_7_8_Data_QC'!I19
    value = "Difference as % of Sector Total"

@register(Metric_4_5_7_8_Data_QC)
class B20():
    # 'Metric_4_5_7_8_Data_QC'!B20
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class C20():
    # 'Metric_4_5_7_8_Data_QC'!C20
    value = "ESCCV"

@register(Metric_4_5_7_8_Data_QC)
class D20():
    # 'Metric_4_5_7_8_Data_QC'!D20
    value = "#N/A"
    formula = "=VLOOKUP(C20,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D20():
        c20_1 = Metric_4_5_7_8_Data_QC.C20()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c20_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E20():
    # 'Metric_4_5_7_8_Data_QC'!E20
    value = "#N/A"
    formula = "=VLOOKUP(C20,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E20():
        c20_1 = Metric_4_5_7_8_Data_QC.C20()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c20_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F20():
    # 'Metric_4_5_7_8_Data_QC'!F20
    value = 722358787.85
    formula = "=SUM('Dashboard M4 Cost Monthly'!G19:R19)"
    @eval_fn
    def F20():
        range_1 = Dashboard_M4_Cost_Monthly(7, 19, 18, 19)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G20():
    # 'Metric_4_5_7_8_Data_QC'!G20
    value = "#N/A"
    formula = "=F20-E20"
    @eval_fn
    def G20():
        f20_1 = Metric_4_5_7_8_Data_QC.F20()
        e20_1 = Metric_4_5_7_8_Data_QC.E20()
        var_1 = sub(f20_1, e20_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H20():
    # 'Metric_4_5_7_8_Data_QC'!H20
    value = "#N/A"
    formula = "=G20/E20"
    @eval_fn
    def H20():
        g20_1 = Metric_4_5_7_8_Data_QC.G20()
        e20_1 = Metric_4_5_7_8_Data_QC.E20()
        var_1 = divide(g20_1, e20_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I20():
    # 'Metric_4_5_7_8_Data_QC'!I20
    value = "#N/A"
    formula = "=G20/E29"
    @eval_fn
    def I20():
        g20_1 = Metric_4_5_7_8_Data_QC.G20()
        e29_1 = Metric_4_5_7_8_Data_QC.E29()
        var_1 = divide(g20_1, e29_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B21():
    # 'Metric_4_5_7_8_Data_QC'!B21
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class C21():
    # 'Metric_4_5_7_8_Data_QC'!C21
    value = "MGCCV"

@register(Metric_4_5_7_8_Data_QC)
class D21():
    # 'Metric_4_5_7_8_Data_QC'!D21
    value = "#N/A"
    formula = "=VLOOKUP(C21,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D21():
        c21_1 = Metric_4_5_7_8_Data_QC.C21()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c21_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E21():
    # 'Metric_4_5_7_8_Data_QC'!E21
    value = "#N/A"
    formula = "=VLOOKUP(C21,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E21():
        c21_1 = Metric_4_5_7_8_Data_QC.C21()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c21_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F21():
    # 'Metric_4_5_7_8_Data_QC'!F21
    value = 1605466.45815
    formula = "=SUM('Dashboard M4 Cost Monthly'!G20:R20)"
    @eval_fn
    def F21():
        range_1 = Dashboard_M4_Cost_Monthly(7, 20, 18, 20)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G21():
    # 'Metric_4_5_7_8_Data_QC'!G21
    value = "#N/A"
    formula = "=F21-E21"
    @eval_fn
    def G21():
        f21_1 = Metric_4_5_7_8_Data_QC.F21()
        e21_1 = Metric_4_5_7_8_Data_QC.E21()
        var_1 = sub(f21_1, e21_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H21():
    # 'Metric_4_5_7_8_Data_QC'!H21
    value = "#N/A"
    formula = "=G21/E21"
    @eval_fn
    def H21():
        g21_1 = Metric_4_5_7_8_Data_QC.G21()
        e21_1 = Metric_4_5_7_8_Data_QC.E21()
        var_1 = divide(g21_1, e21_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I21():
    # 'Metric_4_5_7_8_Data_QC'!I21
    value = "#N/A"
    formula = "=G21/E29"
    @eval_fn
    def I21():
        g21_1 = Metric_4_5_7_8_Data_QC.G21()
        e29_1 = Metric_4_5_7_8_Data_QC.E29()
        var_1 = divide(g21_1, e29_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B22():
    # 'Metric_4_5_7_8_Data_QC'!B22
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class C22():
    # 'Metric_4_5_7_8_Data_QC'!C22
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E22():
    # 'Metric_4_5_7_8_Data_QC'!E22
    value = 0
    formula = "=VLOOKUP(C22,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E22():
        c22_1 = Metric_4_5_7_8_Data_QC.C22()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c22_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F22():
    # 'Metric_4_5_7_8_Data_QC'!F22
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G21:R21)"
    @eval_fn
    def F22():
        range_1 = Dashboard_M4_Cost_Monthly(7, 21, 18, 21)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G22():
    # 'Metric_4_5_7_8_Data_QC'!G22
    value = 0
    formula = "=F22-E22"
    @eval_fn
    def G22():
        f22_1 = Metric_4_5_7_8_Data_QC.F22()
        e22_1 = Metric_4_5_7_8_Data_QC.E22()
        var_1 = sub(f22_1, e22_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I22():
    # 'Metric_4_5_7_8_Data_QC'!I22
    value = "#N/A"
    formula = "=G22/E29"
    @eval_fn
    def I22():
        g22_1 = Metric_4_5_7_8_Data_QC.G22()
        e29_1 = Metric_4_5_7_8_Data_QC.E29()
        var_1 = divide(g22_1, e29_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B23():
    # 'Metric_4_5_7_8_Data_QC'!B23
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class C23():
    # 'Metric_4_5_7_8_Data_QC'!C23
    value = "DFCCV"

@register(Metric_4_5_7_8_Data_QC)
class D23():
    # 'Metric_4_5_7_8_Data_QC'!D23
    value = "#N/A"
    formula = "=VLOOKUP(C23,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D23():
        c23_1 = Metric_4_5_7_8_Data_QC.C23()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c23_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E23():
    # 'Metric_4_5_7_8_Data_QC'!E23
    value = "#N/A"
    formula = "=VLOOKUP(C23,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E23():
        c23_1 = Metric_4_5_7_8_Data_QC.C23()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c23_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F23():
    # 'Metric_4_5_7_8_Data_QC'!F23
    value = 57055442.4985
    formula = "=SUM('Dashboard M4 Cost Monthly'!G22:R22)"
    @eval_fn
    def F23():
        range_1 = Dashboard_M4_Cost_Monthly(7, 22, 18, 22)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G23():
    # 'Metric_4_5_7_8_Data_QC'!G23
    value = "#N/A"
    formula = "=F23-E23"
    @eval_fn
    def G23():
        f23_1 = Metric_4_5_7_8_Data_QC.F23()
        e23_1 = Metric_4_5_7_8_Data_QC.E23()
        var_1 = sub(f23_1, e23_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H23():
    # 'Metric_4_5_7_8_Data_QC'!H23
    value = "#N/A"
    formula = "=G23/E23"
    @eval_fn
    def H23():
        g23_1 = Metric_4_5_7_8_Data_QC.G23()
        e23_1 = Metric_4_5_7_8_Data_QC.E23()
        var_1 = divide(g23_1, e23_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I23():
    # 'Metric_4_5_7_8_Data_QC'!I23
    value = "#N/A"
    formula = "=G23/E29"
    @eval_fn
    def I23():
        g23_1 = Metric_4_5_7_8_Data_QC.G23()
        e29_1 = Metric_4_5_7_8_Data_QC.E29()
        var_1 = divide(g23_1, e29_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B24():
    # 'Metric_4_5_7_8_Data_QC'!B24
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class C24():
    # 'Metric_4_5_7_8_Data_QC'!C24
    value = "RFCCV"

@register(Metric_4_5_7_8_Data_QC)
class D24():
    # 'Metric_4_5_7_8_Data_QC'!D24
    value = "#N/A"
    formula = "=VLOOKUP(C24,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D24():
        c24_1 = Metric_4_5_7_8_Data_QC.C24()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c24_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E24():
    # 'Metric_4_5_7_8_Data_QC'!E24
    value = "#N/A"
    formula = "=VLOOKUP(C24,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E24():
        c24_1 = Metric_4_5_7_8_Data_QC.C24()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c24_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F24():
    # 'Metric_4_5_7_8_Data_QC'!F24
    value = 48064.5124858
    formula = "=SUM('Dashboard M4 Cost Monthly'!G23:R23)"
    @eval_fn
    def F24():
        range_1 = Dashboard_M4_Cost_Monthly(7, 23, 18, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G24():
    # 'Metric_4_5_7_8_Data_QC'!G24
    value = "#N/A"
    formula = "=F24-E24"
    @eval_fn
    def G24():
        f24_1 = Metric_4_5_7_8_Data_QC.F24()
        e24_1 = Metric_4_5_7_8_Data_QC.E24()
        var_1 = sub(f24_1, e24_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H24():
    # 'Metric_4_5_7_8_Data_QC'!H24
    value = "#N/A"
    formula = "=G24/E24"
    @eval_fn
    def H24():
        g24_1 = Metric_4_5_7_8_Data_QC.G24()
        e24_1 = Metric_4_5_7_8_Data_QC.E24()
        var_1 = divide(g24_1, e24_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I24():
    # 'Metric_4_5_7_8_Data_QC'!I24
    value = "#N/A"
    formula = "=G24/E29"
    @eval_fn
    def I24():
        g24_1 = Metric_4_5_7_8_Data_QC.G24()
        e29_1 = Metric_4_5_7_8_Data_QC.E29()
        var_1 = divide(g24_1, e29_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B25():
    # 'Metric_4_5_7_8_Data_QC'!B25
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class C25():
    # 'Metric_4_5_7_8_Data_QC'!C25
    value = "LGCCV"

@register(Metric_4_5_7_8_Data_QC)
class D25():
    # 'Metric_4_5_7_8_Data_QC'!D25
    value = "#N/A"
    formula = "=VLOOKUP(C25,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D25():
        c25_1 = Metric_4_5_7_8_Data_QC.C25()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c25_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E25():
    # 'Metric_4_5_7_8_Data_QC'!E25
    value = "#N/A"
    formula = "=VLOOKUP(C25,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E25():
        c25_1 = Metric_4_5_7_8_Data_QC.C25()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c25_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F25():
    # 'Metric_4_5_7_8_Data_QC'!F25
    value = 33706703.943
    formula = "=SUM('Dashboard M4 Cost Monthly'!G24:R24)"
    @eval_fn
    def F25():
        range_1 = Dashboard_M4_Cost_Monthly(7, 24, 18, 24)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G25():
    # 'Metric_4_5_7_8_Data_QC'!G25
    value = "#N/A"
    formula = "=F25-E25"
    @eval_fn
    def G25():
        f25_1 = Metric_4_5_7_8_Data_QC.F25()
        e25_1 = Metric_4_5_7_8_Data_QC.E25()
        var_1 = sub(f25_1, e25_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H25():
    # 'Metric_4_5_7_8_Data_QC'!H25
    value = "#N/A"
    formula = "=G25/E25"
    @eval_fn
    def H25():
        g25_1 = Metric_4_5_7_8_Data_QC.G25()
        e25_1 = Metric_4_5_7_8_Data_QC.E25()
        var_1 = divide(g25_1, e25_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I25():
    # 'Metric_4_5_7_8_Data_QC'!I25
    value = "#N/A"
    formula = "=G25/E29"
    @eval_fn
    def I25():
        g25_1 = Metric_4_5_7_8_Data_QC.G25()
        e29_1 = Metric_4_5_7_8_Data_QC.E29()
        var_1 = divide(g25_1, e29_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B26():
    # 'Metric_4_5_7_8_Data_QC'!B26
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class C26():
    # 'Metric_4_5_7_8_Data_QC'!C26
    value = "NGCCV"

@register(Metric_4_5_7_8_Data_QC)
class D26():
    # 'Metric_4_5_7_8_Data_QC'!D26
    value = "#N/A"
    formula = "=VLOOKUP(C26,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D26():
        c26_1 = Metric_4_5_7_8_Data_QC.C26()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c26_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E26():
    # 'Metric_4_5_7_8_Data_QC'!E26
    value = "#N/A"
    formula = "=VLOOKUP(C26,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E26():
        c26_1 = Metric_4_5_7_8_Data_QC.C26()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c26_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F26():
    # 'Metric_4_5_7_8_Data_QC'!F26
    value = 49921060.5216
    formula = "=SUM('Dashboard M4 Cost Monthly'!G25:R25)"
    @eval_fn
    def F26():
        range_1 = Dashboard_M4_Cost_Monthly(7, 25, 18, 25)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G26():
    # 'Metric_4_5_7_8_Data_QC'!G26
    value = "#N/A"
    formula = "=F26-E26"
    @eval_fn
    def G26():
        f26_1 = Metric_4_5_7_8_Data_QC.F26()
        e26_1 = Metric_4_5_7_8_Data_QC.E26()
        var_1 = sub(f26_1, e26_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H26():
    # 'Metric_4_5_7_8_Data_QC'!H26
    value = "#N/A"
    formula = "=G26/E26"
    @eval_fn
    def H26():
        g26_1 = Metric_4_5_7_8_Data_QC.G26()
        e26_1 = Metric_4_5_7_8_Data_QC.E26()
        var_1 = divide(g26_1, e26_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I26():
    # 'Metric_4_5_7_8_Data_QC'!I26
    value = "#N/A"
    formula = "=G26/E29"
    @eval_fn
    def I26():
        g26_1 = Metric_4_5_7_8_Data_QC.G26()
        e29_1 = Metric_4_5_7_8_Data_QC.E29()
        var_1 = divide(g26_1, e29_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B27():
    # 'Metric_4_5_7_8_Data_QC'!B27
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class C27():
    # 'Metric_4_5_7_8_Data_QC'!C27
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E27():
    # 'Metric_4_5_7_8_Data_QC'!E27
    value = 0
    formula = "=VLOOKUP(C27,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E27():
        c27_1 = Metric_4_5_7_8_Data_QC.C27()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c27_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F27():
    # 'Metric_4_5_7_8_Data_QC'!F27
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G26:R26)"
    @eval_fn
    def F27():
        range_1 = Dashboard_M4_Cost_Monthly(7, 26, 18, 26)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G27():
    # 'Metric_4_5_7_8_Data_QC'!G27
    value = 0
    formula = "=F27-E27"
    @eval_fn
    def G27():
        f27_1 = Metric_4_5_7_8_Data_QC.F27()
        e27_1 = Metric_4_5_7_8_Data_QC.E27()
        var_1 = sub(f27_1, e27_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I27():
    # 'Metric_4_5_7_8_Data_QC'!I27
    value = "#N/A"
    formula = "=G27/E29"
    @eval_fn
    def I27():
        g27_1 = Metric_4_5_7_8_Data_QC.G27()
        e29_1 = Metric_4_5_7_8_Data_QC.E29()
        var_1 = divide(g27_1, e29_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B28():
    # 'Metric_4_5_7_8_Data_QC'!B28
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class C28():
    # 'Metric_4_5_7_8_Data_QC'!C28
    value = "EMCCV"

@register(Metric_4_5_7_8_Data_QC)
class D28():
    # 'Metric_4_5_7_8_Data_QC'!D28
    value = "#N/A"
    formula = "=VLOOKUP(C28,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D28():
        c28_1 = Metric_4_5_7_8_Data_QC.C28()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c28_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E28():
    # 'Metric_4_5_7_8_Data_QC'!E28
    value = "#N/A"
    formula = "=VLOOKUP(C28,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E28():
        c28_1 = Metric_4_5_7_8_Data_QC.C28()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c28_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F28():
    # 'Metric_4_5_7_8_Data_QC'!F28
    value = 28470.2417462
    formula = "=SUM('Dashboard M4 Cost Monthly'!G27:R27)"
    @eval_fn
    def F28():
        range_1 = Dashboard_M4_Cost_Monthly(7, 27, 18, 27)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G28():
    # 'Metric_4_5_7_8_Data_QC'!G28
    value = "#N/A"
    formula = "=F28-E28"
    @eval_fn
    def G28():
        f28_1 = Metric_4_5_7_8_Data_QC.F28()
        e28_1 = Metric_4_5_7_8_Data_QC.E28()
        var_1 = sub(f28_1, e28_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I28():
    # 'Metric_4_5_7_8_Data_QC'!I28
    value = "#N/A"
    formula = "=G28/E29"
    @eval_fn
    def I28():
        g28_1 = Metric_4_5_7_8_Data_QC.G28()
        e29_1 = Metric_4_5_7_8_Data_QC.E29()
        var_1 = divide(g28_1, e29_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B29():
    # 'Metric_4_5_7_8_Data_QC'!B29
    value = "Total"

@register(Metric_4_5_7_8_Data_QC)
class E29():
    # 'Metric_4_5_7_8_Data_QC'!E29
    value = "#N/A"
    formula = "=SUM(E20:E27)"
    @eval_fn
    def E29():
        range_1 = Metric_4_5_7_8_Data_QC(5, 20, 5, 27)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F29():
    # 'Metric_4_5_7_8_Data_QC'!F29
    value = 864695525.784
    formula = "=SUM(F20:F27)"
    @eval_fn
    def F29():
        range_1 = Metric_4_5_7_8_Data_QC(6, 20, 6, 27)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G29():
    # 'Metric_4_5_7_8_Data_QC'!G29
    value = "#N/A"
    formula = "=SUM(G20:G27)"
    @eval_fn
    def G29():
        range_1 = Metric_4_5_7_8_Data_QC(7, 20, 7, 27)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H29():
    # 'Metric_4_5_7_8_Data_QC'!H29
    value = "#N/A"
    formula = "=G29/E29"
    @eval_fn
    def H29():
        g29_1 = Metric_4_5_7_8_Data_QC.G29()
        e29_1 = Metric_4_5_7_8_Data_QC.E29()
        var_1 = divide(g29_1, e29_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class A30():
    # 'Metric_4_5_7_8_Data_QC'!A30
    value = "Industrial"

@register(Metric_4_5_7_8_Data_QC)
class E30():
    # 'Metric_4_5_7_8_Data_QC'!E30
    value = "EIA Reported"

@register(Metric_4_5_7_8_Data_QC)
class F30():
    # 'Metric_4_5_7_8_Data_QC'!F30
    value = "Calculated Expenditures"

@register(Metric_4_5_7_8_Data_QC)
class G30():
    # 'Metric_4_5_7_8_Data_QC'!G30
    value = "Difference"

@register(Metric_4_5_7_8_Data_QC)
class H30():
    # 'Metric_4_5_7_8_Data_QC'!H30
    value = "Difference as % of EIA"

@register(Metric_4_5_7_8_Data_QC)
class I30():
    # 'Metric_4_5_7_8_Data_QC'!I30
    value = "Difference as % of Sector Total"

@register(Metric_4_5_7_8_Data_QC)
class A31():
    # 'Metric_4_5_7_8_Data_QC'!A31
    value = "ESRFB"

@register(Metric_4_5_7_8_Data_QC)
class B31():
    # 'Metric_4_5_7_8_Data_QC'!B31
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class C31():
    # 'Metric_4_5_7_8_Data_QC'!C31
    value = "ESICV"

@register(Metric_4_5_7_8_Data_QC)
class D31():
    # 'Metric_4_5_7_8_Data_QC'!D31
    value = "#N/A"
    formula = "=VLOOKUP(C31,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D31():
        c31_1 = Metric_4_5_7_8_Data_QC.C31()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c31_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E31():
    # 'Metric_4_5_7_8_Data_QC'!E31
    value = "#N/A"
    formula = "=VLOOKUP(C31,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E31():
        c31_1 = Metric_4_5_7_8_Data_QC.C31()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c31_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F31():
    # 'Metric_4_5_7_8_Data_QC'!F31
    value = 762702165.184
    formula = "=SUM('Dashboard M4 Cost Monthly'!G30:R30)"
    @eval_fn
    def F31():
        range_1 = Dashboard_M4_Cost_Monthly(7, 30, 18, 30)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G31():
    # 'Metric_4_5_7_8_Data_QC'!G31
    value = "#N/A"
    formula = "=F31-E31"
    @eval_fn
    def G31():
        f31_1 = Metric_4_5_7_8_Data_QC.F31()
        e31_1 = Metric_4_5_7_8_Data_QC.E31()
        var_1 = sub(f31_1, e31_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H31():
    # 'Metric_4_5_7_8_Data_QC'!H31
    value = "#N/A"
    formula = "=G31/E31"
    @eval_fn
    def H31():
        g31_1 = Metric_4_5_7_8_Data_QC.G31()
        e31_1 = Metric_4_5_7_8_Data_QC.E31()
        var_1 = divide(g31_1, e31_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I31():
    # 'Metric_4_5_7_8_Data_QC'!I31
    value = "#N/A"
    formula = "=G31/E40"
    @eval_fn
    def I31():
        g31_1 = Metric_4_5_7_8_Data_QC.G31()
        e40_1 = Metric_4_5_7_8_Data_QC.E40()
        var_1 = divide(g31_1, e40_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B32():
    # 'Metric_4_5_7_8_Data_QC'!B32
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class C32():
    # 'Metric_4_5_7_8_Data_QC'!C32
    value = "MGICV"

@register(Metric_4_5_7_8_Data_QC)
class D32():
    # 'Metric_4_5_7_8_Data_QC'!D32
    value = "#N/A"
    formula = "=VLOOKUP(C32,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D32():
        c32_1 = Metric_4_5_7_8_Data_QC.C32()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c32_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E32():
    # 'Metric_4_5_7_8_Data_QC'!E32
    value = "#N/A"
    formula = "=VLOOKUP(C32,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E32():
        c32_1 = Metric_4_5_7_8_Data_QC.C32()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c32_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F32():
    # 'Metric_4_5_7_8_Data_QC'!F32
    value = 18781409.2009
    formula = "=SUM('Dashboard M4 Cost Monthly'!G31:R31)"
    @eval_fn
    def F32():
        range_1 = Dashboard_M4_Cost_Monthly(7, 31, 18, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G32():
    # 'Metric_4_5_7_8_Data_QC'!G32
    value = "#N/A"
    formula = "=F32-E32"
    @eval_fn
    def G32():
        f32_1 = Metric_4_5_7_8_Data_QC.F32()
        e32_1 = Metric_4_5_7_8_Data_QC.E32()
        var_1 = sub(f32_1, e32_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H32():
    # 'Metric_4_5_7_8_Data_QC'!H32
    value = "#N/A"
    formula = "=G32/E32"
    @eval_fn
    def H32():
        g32_1 = Metric_4_5_7_8_Data_QC.G32()
        e32_1 = Metric_4_5_7_8_Data_QC.E32()
        var_1 = divide(g32_1, e32_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I32():
    # 'Metric_4_5_7_8_Data_QC'!I32
    value = "#N/A"
    formula = "=G32/E40"
    @eval_fn
    def I32():
        g32_1 = Metric_4_5_7_8_Data_QC.G32()
        e40_1 = Metric_4_5_7_8_Data_QC.E40()
        var_1 = divide(g32_1, e40_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B33():
    # 'Metric_4_5_7_8_Data_QC'!B33
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class C33():
    # 'Metric_4_5_7_8_Data_QC'!C33
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E33():
    # 'Metric_4_5_7_8_Data_QC'!E33
    value = 0
    formula = "=VLOOKUP(C33,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E33():
        c33_1 = Metric_4_5_7_8_Data_QC.C33()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c33_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F33():
    # 'Metric_4_5_7_8_Data_QC'!F33
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G32:R32)"
    @eval_fn
    def F33():
        range_1 = Dashboard_M4_Cost_Monthly(7, 32, 18, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G33():
    # 'Metric_4_5_7_8_Data_QC'!G33
    value = 0
    formula = "=F33-E33"
    @eval_fn
    def G33():
        f33_1 = Metric_4_5_7_8_Data_QC.F33()
        e33_1 = Metric_4_5_7_8_Data_QC.E33()
        var_1 = sub(f33_1, e33_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I33():
    # 'Metric_4_5_7_8_Data_QC'!I33
    value = "#N/A"
    formula = "=G33/E40"
    @eval_fn
    def I33():
        g33_1 = Metric_4_5_7_8_Data_QC.G33()
        e40_1 = Metric_4_5_7_8_Data_QC.E40()
        var_1 = divide(g33_1, e40_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B34():
    # 'Metric_4_5_7_8_Data_QC'!B34
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class C34():
    # 'Metric_4_5_7_8_Data_QC'!C34
    value = "DFICV"

@register(Metric_4_5_7_8_Data_QC)
class D34():
    # 'Metric_4_5_7_8_Data_QC'!D34
    value = "#N/A"
    formula = "=VLOOKUP(C34,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D34():
        c34_1 = Metric_4_5_7_8_Data_QC.C34()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c34_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E34():
    # 'Metric_4_5_7_8_Data_QC'!E34
    value = "#N/A"
    formula = "=VLOOKUP(C34,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E34():
        c34_1 = Metric_4_5_7_8_Data_QC.C34()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c34_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F34():
    # 'Metric_4_5_7_8_Data_QC'!F34
    value = 65731270.0826
    formula = "=SUM('Dashboard M4 Cost Monthly'!G33:R33)"
    @eval_fn
    def F34():
        range_1 = Dashboard_M4_Cost_Monthly(7, 33, 18, 33)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G34():
    # 'Metric_4_5_7_8_Data_QC'!G34
    value = "#N/A"
    formula = "=F34-E34"
    @eval_fn
    def G34():
        f34_1 = Metric_4_5_7_8_Data_QC.F34()
        e34_1 = Metric_4_5_7_8_Data_QC.E34()
        var_1 = sub(f34_1, e34_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H34():
    # 'Metric_4_5_7_8_Data_QC'!H34
    value = "#N/A"
    formula = "=G34/E34"
    @eval_fn
    def H34():
        g34_1 = Metric_4_5_7_8_Data_QC.G34()
        e34_1 = Metric_4_5_7_8_Data_QC.E34()
        var_1 = divide(g34_1, e34_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I34():
    # 'Metric_4_5_7_8_Data_QC'!I34
    value = "#N/A"
    formula = "=G34/E40"
    @eval_fn
    def I34():
        g34_1 = Metric_4_5_7_8_Data_QC.G34()
        e40_1 = Metric_4_5_7_8_Data_QC.E40()
        var_1 = divide(g34_1, e40_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B35():
    # 'Metric_4_5_7_8_Data_QC'!B35
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class C35():
    # 'Metric_4_5_7_8_Data_QC'!C35
    value = "RFICV"

@register(Metric_4_5_7_8_Data_QC)
class D35():
    # 'Metric_4_5_7_8_Data_QC'!D35
    value = "#N/A"
    formula = "=VLOOKUP(C35,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D35():
        c35_1 = Metric_4_5_7_8_Data_QC.C35()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c35_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E35():
    # 'Metric_4_5_7_8_Data_QC'!E35
    value = "#N/A"
    formula = "=VLOOKUP(C35,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E35():
        c35_1 = Metric_4_5_7_8_Data_QC.C35()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c35_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F35():
    # 'Metric_4_5_7_8_Data_QC'!F35
    value = 8113289.7076
    formula = "=SUM('Dashboard M4 Cost Monthly'!G34:R34)"
    @eval_fn
    def F35():
        range_1 = Dashboard_M4_Cost_Monthly(7, 34, 18, 34)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G35():
    # 'Metric_4_5_7_8_Data_QC'!G35
    value = "#N/A"
    formula = "=F35-E35"
    @eval_fn
    def G35():
        f35_1 = Metric_4_5_7_8_Data_QC.F35()
        e35_1 = Metric_4_5_7_8_Data_QC.E35()
        var_1 = sub(f35_1, e35_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H35():
    # 'Metric_4_5_7_8_Data_QC'!H35
    value = "#N/A"
    formula = "=G35/E35"
    @eval_fn
    def H35():
        g35_1 = Metric_4_5_7_8_Data_QC.G35()
        e35_1 = Metric_4_5_7_8_Data_QC.E35()
        var_1 = divide(g35_1, e35_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I35():
    # 'Metric_4_5_7_8_Data_QC'!I35
    value = "#N/A"
    formula = "=G35/E40"
    @eval_fn
    def I35():
        g35_1 = Metric_4_5_7_8_Data_QC.G35()
        e40_1 = Metric_4_5_7_8_Data_QC.E40()
        var_1 = divide(g35_1, e40_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B36():
    # 'Metric_4_5_7_8_Data_QC'!B36
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class C36():
    # 'Metric_4_5_7_8_Data_QC'!C36
    value = "LGICV"

@register(Metric_4_5_7_8_Data_QC)
class D36():
    # 'Metric_4_5_7_8_Data_QC'!D36
    value = "#N/A"
    formula = "=VLOOKUP(C36,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D36():
        c36_1 = Metric_4_5_7_8_Data_QC.C36()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c36_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E36():
    # 'Metric_4_5_7_8_Data_QC'!E36
    value = "#N/A"
    formula = "=VLOOKUP(C36,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E36():
        c36_1 = Metric_4_5_7_8_Data_QC.C36()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c36_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F36():
    # 'Metric_4_5_7_8_Data_QC'!F36
    value = 2868655.65472
    formula = "=SUM('Dashboard M4 Cost Monthly'!G35:R35)"
    @eval_fn
    def F36():
        range_1 = Dashboard_M4_Cost_Monthly(7, 35, 18, 35)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G36():
    # 'Metric_4_5_7_8_Data_QC'!G36
    value = "#N/A"
    formula = "=F36-E36"
    @eval_fn
    def G36():
        f36_1 = Metric_4_5_7_8_Data_QC.F36()
        e36_1 = Metric_4_5_7_8_Data_QC.E36()
        var_1 = sub(f36_1, e36_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H36():
    # 'Metric_4_5_7_8_Data_QC'!H36
    value = "#N/A"
    formula = "=G36/E36"
    @eval_fn
    def H36():
        g36_1 = Metric_4_5_7_8_Data_QC.G36()
        e36_1 = Metric_4_5_7_8_Data_QC.E36()
        var_1 = divide(g36_1, e36_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I36():
    # 'Metric_4_5_7_8_Data_QC'!I36
    value = "#N/A"
    formula = "=G36/E40"
    @eval_fn
    def I36():
        g36_1 = Metric_4_5_7_8_Data_QC.G36()
        e40_1 = Metric_4_5_7_8_Data_QC.E40()
        var_1 = divide(g36_1, e40_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B37():
    # 'Metric_4_5_7_8_Data_QC'!B37
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class C37():
    # 'Metric_4_5_7_8_Data_QC'!C37
    value = "NGICV"

@register(Metric_4_5_7_8_Data_QC)
class D37():
    # 'Metric_4_5_7_8_Data_QC'!D37
    value = "#N/A"
    formula = "=VLOOKUP(C37,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D37():
        c37_1 = Metric_4_5_7_8_Data_QC.C37()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c37_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E37():
    # 'Metric_4_5_7_8_Data_QC'!E37
    value = "#N/A"
    formula = "=VLOOKUP(C37,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E37():
        c37_1 = Metric_4_5_7_8_Data_QC.C37()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c37_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F37():
    # 'Metric_4_5_7_8_Data_QC'!F37
    value = 11073111.9492
    formula = "=SUM('Dashboard M4 Cost Monthly'!G36:R36)"
    @eval_fn
    def F37():
        range_1 = Dashboard_M4_Cost_Monthly(7, 36, 18, 36)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G37():
    # 'Metric_4_5_7_8_Data_QC'!G37
    value = "#N/A"
    formula = "=F37-E37"
    @eval_fn
    def G37():
        f37_1 = Metric_4_5_7_8_Data_QC.F37()
        e37_1 = Metric_4_5_7_8_Data_QC.E37()
        var_1 = sub(f37_1, e37_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H37():
    # 'Metric_4_5_7_8_Data_QC'!H37
    value = "#N/A"
    formula = "=G37/E37"
    @eval_fn
    def H37():
        g37_1 = Metric_4_5_7_8_Data_QC.G37()
        e37_1 = Metric_4_5_7_8_Data_QC.E37()
        var_1 = divide(g37_1, e37_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I37():
    # 'Metric_4_5_7_8_Data_QC'!I37
    value = "#N/A"
    formula = "=G37/E40"
    @eval_fn
    def I37():
        g37_1 = Metric_4_5_7_8_Data_QC.G37()
        e40_1 = Metric_4_5_7_8_Data_QC.E40()
        var_1 = divide(g37_1, e40_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B38():
    # 'Metric_4_5_7_8_Data_QC'!B38
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class C38():
    # 'Metric_4_5_7_8_Data_QC'!C38
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E38():
    # 'Metric_4_5_7_8_Data_QC'!E38
    value = 0
    formula = "=VLOOKUP(C38,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E38():
        c38_1 = Metric_4_5_7_8_Data_QC.C38()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c38_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F38():
    # 'Metric_4_5_7_8_Data_QC'!F38
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G37:R37)"
    @eval_fn
    def F38():
        range_1 = Dashboard_M4_Cost_Monthly(7, 37, 18, 37)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G38():
    # 'Metric_4_5_7_8_Data_QC'!G38
    value = 0
    formula = "=F38-E38"
    @eval_fn
    def G38():
        f38_1 = Metric_4_5_7_8_Data_QC.F38()
        e38_1 = Metric_4_5_7_8_Data_QC.E38()
        var_1 = sub(f38_1, e38_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I38():
    # 'Metric_4_5_7_8_Data_QC'!I38
    value = "#N/A"
    formula = "=G38/E40"
    @eval_fn
    def I38():
        g38_1 = Metric_4_5_7_8_Data_QC.G38()
        e40_1 = Metric_4_5_7_8_Data_QC.E40()
        var_1 = divide(g38_1, e40_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B39():
    # 'Metric_4_5_7_8_Data_QC'!B39
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class C39():
    # 'Metric_4_5_7_8_Data_QC'!C39
    value = "EMICV"

@register(Metric_4_5_7_8_Data_QC)
class D39():
    # 'Metric_4_5_7_8_Data_QC'!D39
    value = "#N/A"
    formula = "=VLOOKUP(C39,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D39():
        c39_1 = Metric_4_5_7_8_Data_QC.C39()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c39_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E39():
    # 'Metric_4_5_7_8_Data_QC'!E39
    value = "#N/A"
    formula = "=VLOOKUP(C39,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E39():
        c39_1 = Metric_4_5_7_8_Data_QC.C39()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c39_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F39():
    # 'Metric_4_5_7_8_Data_QC'!F39
    value = 483994.109686
    formula = "=SUM('Dashboard M4 Cost Monthly'!G38:R38)"
    @eval_fn
    def F39():
        range_1 = Dashboard_M4_Cost_Monthly(7, 38, 18, 38)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G39():
    # 'Metric_4_5_7_8_Data_QC'!G39
    value = "#N/A"
    formula = "=F39-E39"
    @eval_fn
    def G39():
        f39_1 = Metric_4_5_7_8_Data_QC.F39()
        e39_1 = Metric_4_5_7_8_Data_QC.E39()
        var_1 = sub(f39_1, e39_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H39():
    # 'Metric_4_5_7_8_Data_QC'!H39
    value = "#N/A"
    formula = "=G39/E39"
    @eval_fn
    def H39():
        g39_1 = Metric_4_5_7_8_Data_QC.G39()
        e39_1 = Metric_4_5_7_8_Data_QC.E39()
        var_1 = divide(g39_1, e39_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I39():
    # 'Metric_4_5_7_8_Data_QC'!I39
    value = "#N/A"
    formula = "=G39/E40"
    @eval_fn
    def I39():
        g39_1 = Metric_4_5_7_8_Data_QC.G39()
        e40_1 = Metric_4_5_7_8_Data_QC.E40()
        var_1 = divide(g39_1, e40_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B40():
    # 'Metric_4_5_7_8_Data_QC'!B40
    value = "Total"

@register(Metric_4_5_7_8_Data_QC)
class E40():
    # 'Metric_4_5_7_8_Data_QC'!E40
    value = "#N/A"
    formula = "=SUM(E31:E38)"
    @eval_fn
    def E40():
        range_1 = Metric_4_5_7_8_Data_QC(5, 31, 5, 38)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F40():
    # 'Metric_4_5_7_8_Data_QC'!F40
    value = 869269901.779
    formula = "=SUM(F31:F38)"
    @eval_fn
    def F40():
        range_1 = Metric_4_5_7_8_Data_QC(6, 31, 6, 38)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G40():
    # 'Metric_4_5_7_8_Data_QC'!G40
    value = "#N/A"
    formula = "=SUM(G31:G38)"
    @eval_fn
    def G40():
        range_1 = Metric_4_5_7_8_Data_QC(7, 31, 7, 38)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H40():
    # 'Metric_4_5_7_8_Data_QC'!H40
    value = "#N/A"
    formula = "=G40/E40"
    @eval_fn
    def H40():
        g40_1 = Metric_4_5_7_8_Data_QC.G40()
        e40_1 = Metric_4_5_7_8_Data_QC.E40()
        var_1 = divide(g40_1, e40_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class A41():
    # 'Metric_4_5_7_8_Data_QC'!A41
    value = "Ground and Water Transportation"

@register(Metric_4_5_7_8_Data_QC)
class E41():
    # 'Metric_4_5_7_8_Data_QC'!E41
    value = "EIA Reported"

@register(Metric_4_5_7_8_Data_QC)
class F41():
    # 'Metric_4_5_7_8_Data_QC'!F41
    value = "Calculated Expenditures"

@register(Metric_4_5_7_8_Data_QC)
class G41():
    # 'Metric_4_5_7_8_Data_QC'!G41
    value = "Difference"

@register(Metric_4_5_7_8_Data_QC)
class H41():
    # 'Metric_4_5_7_8_Data_QC'!H41
    value = "Difference as % of EIA"

@register(Metric_4_5_7_8_Data_QC)
class I41():
    # 'Metric_4_5_7_8_Data_QC'!I41
    value = "Difference as % of Sector Total"

@register(Metric_4_5_7_8_Data_QC)
class B42():
    # 'Metric_4_5_7_8_Data_QC'!B42
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class C42():
    # 'Metric_4_5_7_8_Data_QC'!C42
    value = "ESACV"

@register(Metric_4_5_7_8_Data_QC)
class D42():
    # 'Metric_4_5_7_8_Data_QC'!D42
    value = "#N/A"
    formula = "=VLOOKUP(C42,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D42():
        c42_1 = Metric_4_5_7_8_Data_QC.C42()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c42_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E42():
    # 'Metric_4_5_7_8_Data_QC'!E42
    value = "#N/A"
    formula = "=VLOOKUP(C42,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E42():
        c42_1 = Metric_4_5_7_8_Data_QC.C42()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c42_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F42():
    # 'Metric_4_5_7_8_Data_QC'!F42
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G41:R41)"
    @eval_fn
    def F42():
        range_1 = Dashboard_M4_Cost_Monthly(7, 41, 18, 41)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G42():
    # 'Metric_4_5_7_8_Data_QC'!G42
    value = "#N/A"
    formula = "=F42-E42"
    @eval_fn
    def G42():
        f42_1 = Metric_4_5_7_8_Data_QC.F42()
        e42_1 = Metric_4_5_7_8_Data_QC.E42()
        var_1 = sub(f42_1, e42_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I42():
    # 'Metric_4_5_7_8_Data_QC'!I42
    value = "#N/A"
    formula = "=G42/E51"
    @eval_fn
    def I42():
        g42_1 = Metric_4_5_7_8_Data_QC.G42()
        e51_1 = Metric_4_5_7_8_Data_QC.E51()
        var_1 = divide(g42_1, e51_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B43():
    # 'Metric_4_5_7_8_Data_QC'!B43
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class C43():
    # 'Metric_4_5_7_8_Data_QC'!C43
    value = "MGACV"

@register(Metric_4_5_7_8_Data_QC)
class D43():
    # 'Metric_4_5_7_8_Data_QC'!D43
    value = "#N/A"
    formula = "=VLOOKUP(C43,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D43():
        c43_1 = Metric_4_5_7_8_Data_QC.C43()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c43_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E43():
    # 'Metric_4_5_7_8_Data_QC'!E43
    value = "#N/A"
    formula = "=VLOOKUP(C43,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E43():
        c43_1 = Metric_4_5_7_8_Data_QC.C43()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c43_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F43():
    # 'Metric_4_5_7_8_Data_QC'!F43
    value = 1513139395.01
    formula = "=SUM('Dashboard M4 Cost Monthly'!G42:R42)"
    @eval_fn
    def F43():
        range_1 = Dashboard_M4_Cost_Monthly(7, 42, 18, 42)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G43():
    # 'Metric_4_5_7_8_Data_QC'!G43
    value = "#N/A"
    formula = "=F43-E43"
    @eval_fn
    def G43():
        f43_1 = Metric_4_5_7_8_Data_QC.F43()
        e43_1 = Metric_4_5_7_8_Data_QC.E43()
        var_1 = sub(f43_1, e43_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H43():
    # 'Metric_4_5_7_8_Data_QC'!H43
    value = "#N/A"
    formula = "=G43/E43"
    @eval_fn
    def H43():
        g43_1 = Metric_4_5_7_8_Data_QC.G43()
        e43_1 = Metric_4_5_7_8_Data_QC.E43()
        var_1 = divide(g43_1, e43_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I43():
    # 'Metric_4_5_7_8_Data_QC'!I43
    value = "#N/A"
    formula = "=G43/E51"
    @eval_fn
    def I43():
        g43_1 = Metric_4_5_7_8_Data_QC.G43()
        e51_1 = Metric_4_5_7_8_Data_QC.E51()
        var_1 = divide(g43_1, e51_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B44():
    # 'Metric_4_5_7_8_Data_QC'!B44
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class C44():
    # 'Metric_4_5_7_8_Data_QC'!C44
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E44():
    # 'Metric_4_5_7_8_Data_QC'!E44
    value = 0
    formula = "=VLOOKUP(C44,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E44():
        c44_1 = Metric_4_5_7_8_Data_QC.C44()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c44_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F44():
    # 'Metric_4_5_7_8_Data_QC'!F44
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G43:R43)"
    @eval_fn
    def F44():
        range_1 = Dashboard_M4_Cost_Monthly(7, 43, 18, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G44():
    # 'Metric_4_5_7_8_Data_QC'!G44
    value = 0
    formula = "=F44-E44"
    @eval_fn
    def G44():
        f44_1 = Metric_4_5_7_8_Data_QC.F44()
        e44_1 = Metric_4_5_7_8_Data_QC.E44()
        var_1 = sub(f44_1, e44_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I44():
    # 'Metric_4_5_7_8_Data_QC'!I44
    value = "#N/A"
    formula = "=G44/E51"
    @eval_fn
    def I44():
        g44_1 = Metric_4_5_7_8_Data_QC.G44()
        e51_1 = Metric_4_5_7_8_Data_QC.E51()
        var_1 = divide(g44_1, e51_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B45():
    # 'Metric_4_5_7_8_Data_QC'!B45
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class C45():
    # 'Metric_4_5_7_8_Data_QC'!C45
    value = "DFACV"

@register(Metric_4_5_7_8_Data_QC)
class D45():
    # 'Metric_4_5_7_8_Data_QC'!D45
    value = "#N/A"
    formula = "=VLOOKUP(C45,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D45():
        c45_1 = Metric_4_5_7_8_Data_QC.C45()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c45_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E45():
    # 'Metric_4_5_7_8_Data_QC'!E45
    value = "#N/A"
    formula = "=VLOOKUP(C45,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E45():
        c45_1 = Metric_4_5_7_8_Data_QC.C45()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c45_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F45():
    # 'Metric_4_5_7_8_Data_QC'!F45
    value = 493247050.662
    formula = "=SUM('Dashboard M4 Cost Monthly'!G44:R44)"
    @eval_fn
    def F45():
        range_1 = Dashboard_M4_Cost_Monthly(7, 44, 18, 44)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G45():
    # 'Metric_4_5_7_8_Data_QC'!G45
    value = "#N/A"
    formula = "=F45-E45"
    @eval_fn
    def G45():
        f45_1 = Metric_4_5_7_8_Data_QC.F45()
        e45_1 = Metric_4_5_7_8_Data_QC.E45()
        var_1 = sub(f45_1, e45_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H45():
    # 'Metric_4_5_7_8_Data_QC'!H45
    value = "#N/A"
    formula = "=G45/E45"
    @eval_fn
    def H45():
        g45_1 = Metric_4_5_7_8_Data_QC.G45()
        e45_1 = Metric_4_5_7_8_Data_QC.E45()
        var_1 = divide(g45_1, e45_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I45():
    # 'Metric_4_5_7_8_Data_QC'!I45
    value = "#N/A"
    formula = "=G45/E51"
    @eval_fn
    def I45():
        g45_1 = Metric_4_5_7_8_Data_QC.G45()
        e51_1 = Metric_4_5_7_8_Data_QC.E51()
        var_1 = divide(g45_1, e51_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B46():
    # 'Metric_4_5_7_8_Data_QC'!B46
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class C46():
    # 'Metric_4_5_7_8_Data_QC'!C46
    value = "RFACV"

@register(Metric_4_5_7_8_Data_QC)
class D46():
    # 'Metric_4_5_7_8_Data_QC'!D46
    value = "#N/A"
    formula = "=VLOOKUP(C46,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D46():
        c46_1 = Metric_4_5_7_8_Data_QC.C46()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c46_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E46():
    # 'Metric_4_5_7_8_Data_QC'!E46
    value = "#N/A"
    formula = "=VLOOKUP(C46,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E46():
        c46_1 = Metric_4_5_7_8_Data_QC.C46()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c46_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F46():
    # 'Metric_4_5_7_8_Data_QC'!F46
    value = 143549472.99
    formula = "=SUM('Dashboard M4 Cost Monthly'!G45:R45)"
    @eval_fn
    def F46():
        range_1 = Dashboard_M4_Cost_Monthly(7, 45, 18, 45)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G46():
    # 'Metric_4_5_7_8_Data_QC'!G46
    value = "#N/A"
    formula = "=F46-E46"
    @eval_fn
    def G46():
        f46_1 = Metric_4_5_7_8_Data_QC.F46()
        e46_1 = Metric_4_5_7_8_Data_QC.E46()
        var_1 = sub(f46_1, e46_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H46():
    # 'Metric_4_5_7_8_Data_QC'!H46
    value = "#N/A"
    formula = "=G46/E46"
    @eval_fn
    def H46():
        g46_1 = Metric_4_5_7_8_Data_QC.G46()
        e46_1 = Metric_4_5_7_8_Data_QC.E46()
        var_1 = divide(g46_1, e46_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I46():
    # 'Metric_4_5_7_8_Data_QC'!I46
    value = "#N/A"
    formula = "=G46/E51"
    @eval_fn
    def I46():
        g46_1 = Metric_4_5_7_8_Data_QC.G46()
        e51_1 = Metric_4_5_7_8_Data_QC.E51()
        var_1 = divide(g46_1, e51_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B47():
    # 'Metric_4_5_7_8_Data_QC'!B47
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class C47():
    # 'Metric_4_5_7_8_Data_QC'!C47
    value = "LGACV"

@register(Metric_4_5_7_8_Data_QC)
class D47():
    # 'Metric_4_5_7_8_Data_QC'!D47
    value = "#N/A"
    formula = "=VLOOKUP(C47,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D47():
        c47_1 = Metric_4_5_7_8_Data_QC.C47()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c47_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E47():
    # 'Metric_4_5_7_8_Data_QC'!E47
    value = "#N/A"
    formula = "=VLOOKUP(C47,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E47():
        c47_1 = Metric_4_5_7_8_Data_QC.C47()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c47_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F47():
    # 'Metric_4_5_7_8_Data_QC'!F47
    value = 2185642.4036
    formula = "=SUM('Dashboard M4 Cost Monthly'!G46:R46)"
    @eval_fn
    def F47():
        range_1 = Dashboard_M4_Cost_Monthly(7, 46, 18, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G47():
    # 'Metric_4_5_7_8_Data_QC'!G47
    value = "#N/A"
    formula = "=F47-E47"
    @eval_fn
    def G47():
        f47_1 = Metric_4_5_7_8_Data_QC.F47()
        e47_1 = Metric_4_5_7_8_Data_QC.E47()
        var_1 = sub(f47_1, e47_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H47():
    # 'Metric_4_5_7_8_Data_QC'!H47
    value = "#N/A"
    formula = "=G47/E47"
    @eval_fn
    def H47():
        g47_1 = Metric_4_5_7_8_Data_QC.G47()
        e47_1 = Metric_4_5_7_8_Data_QC.E47()
        var_1 = divide(g47_1, e47_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I47():
    # 'Metric_4_5_7_8_Data_QC'!I47
    value = "#N/A"
    formula = "=G47/E51"
    @eval_fn
    def I47():
        g47_1 = Metric_4_5_7_8_Data_QC.G47()
        e51_1 = Metric_4_5_7_8_Data_QC.E51()
        var_1 = divide(g47_1, e51_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B48():
    # 'Metric_4_5_7_8_Data_QC'!B48
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class C48():
    # 'Metric_4_5_7_8_Data_QC'!C48
    value = "NGACV"

@register(Metric_4_5_7_8_Data_QC)
class D48():
    # 'Metric_4_5_7_8_Data_QC'!D48
    value = "#N/A"
    formula = "=VLOOKUP(C48,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D48():
        c48_1 = Metric_4_5_7_8_Data_QC.C48()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c48_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E48():
    # 'Metric_4_5_7_8_Data_QC'!E48
    value = "#N/A"
    formula = "=VLOOKUP(C48,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E48():
        c48_1 = Metric_4_5_7_8_Data_QC.C48()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c48_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F48():
    # 'Metric_4_5_7_8_Data_QC'!F48
    value = 52603.8572409
    formula = "=SUM('Dashboard M4 Cost Monthly'!G47:R47)"
    @eval_fn
    def F48():
        range_1 = Dashboard_M4_Cost_Monthly(7, 47, 18, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G48():
    # 'Metric_4_5_7_8_Data_QC'!G48
    value = "#N/A"
    formula = "=F48-E48"
    @eval_fn
    def G48():
        f48_1 = Metric_4_5_7_8_Data_QC.F48()
        e48_1 = Metric_4_5_7_8_Data_QC.E48()
        var_1 = sub(f48_1, e48_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H48():
    # 'Metric_4_5_7_8_Data_QC'!H48
    value = "#N/A"
    formula = "=G48/E48"
    @eval_fn
    def H48():
        g48_1 = Metric_4_5_7_8_Data_QC.G48()
        e48_1 = Metric_4_5_7_8_Data_QC.E48()
        var_1 = divide(g48_1, e48_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I48():
    # 'Metric_4_5_7_8_Data_QC'!I48
    value = "#N/A"
    formula = "=G48/E51"
    @eval_fn
    def I48():
        g48_1 = Metric_4_5_7_8_Data_QC.G48()
        e51_1 = Metric_4_5_7_8_Data_QC.E51()
        var_1 = divide(g48_1, e51_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class A49():
    # 'Metric_4_5_7_8_Data_QC'!A49
    value = ".55 factor to divide biodiesel between transportation and power"

@register(Metric_4_5_7_8_Data_QC)
class B49():
    # 'Metric_4_5_7_8_Data_QC'!B49
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class C49():
    # 'Metric_4_5_7_8_Data_QC'!C49
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E49():
    # 'Metric_4_5_7_8_Data_QC'!E49
    value = 0
    formula = "=VLOOKUP(C49,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E49():
        c49_1 = Metric_4_5_7_8_Data_QC.C49()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c49_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F49():
    # 'Metric_4_5_7_8_Data_QC'!F49
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G48:R48)"
    @eval_fn
    def F49():
        range_1 = Dashboard_M4_Cost_Monthly(7, 48, 18, 48)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G49():
    # 'Metric_4_5_7_8_Data_QC'!G49
    value = 0
    formula = "=F49-E49"
    @eval_fn
    def G49():
        f49_1 = Metric_4_5_7_8_Data_QC.F49()
        e49_1 = Metric_4_5_7_8_Data_QC.E49()
        var_1 = sub(f49_1, e49_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I49():
    # 'Metric_4_5_7_8_Data_QC'!I49
    value = "#N/A"
    formula = "=G49/E51"
    @eval_fn
    def I49():
        g49_1 = Metric_4_5_7_8_Data_QC.G49()
        e51_1 = Metric_4_5_7_8_Data_QC.E51()
        var_1 = divide(g49_1, e51_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B50():
    # 'Metric_4_5_7_8_Data_QC'!B50
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class C50():
    # 'Metric_4_5_7_8_Data_QC'!C50
    value = "EMACV"

@register(Metric_4_5_7_8_Data_QC)
class D50():
    # 'Metric_4_5_7_8_Data_QC'!D50
    value = "#N/A"
    formula = "=VLOOKUP(C50,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D50():
        c50_1 = Metric_4_5_7_8_Data_QC.C50()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c50_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E50():
    # 'Metric_4_5_7_8_Data_QC'!E50
    value = "#N/A"
    formula = "=VLOOKUP(C50,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E50():
        c50_1 = Metric_4_5_7_8_Data_QC.C50()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c50_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F50():
    # 'Metric_4_5_7_8_Data_QC'!F50
    value = 37950832.2477
    formula = "=SUM('Dashboard M4 Cost Monthly'!G49:R49)"
    @eval_fn
    def F50():
        range_1 = Dashboard_M4_Cost_Monthly(7, 49, 18, 49)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G50():
    # 'Metric_4_5_7_8_Data_QC'!G50
    value = "#N/A"
    formula = "=F50-E50"
    @eval_fn
    def G50():
        f50_1 = Metric_4_5_7_8_Data_QC.F50()
        e50_1 = Metric_4_5_7_8_Data_QC.E50()
        var_1 = sub(f50_1, e50_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H50():
    # 'Metric_4_5_7_8_Data_QC'!H50
    value = "#N/A"
    formula = "=G50/E50"
    @eval_fn
    def H50():
        g50_1 = Metric_4_5_7_8_Data_QC.G50()
        e50_1 = Metric_4_5_7_8_Data_QC.E50()
        var_1 = divide(g50_1, e50_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I50():
    # 'Metric_4_5_7_8_Data_QC'!I50
    value = "#N/A"
    formula = "=G50/E51"
    @eval_fn
    def I50():
        g50_1 = Metric_4_5_7_8_Data_QC.G50()
        e51_1 = Metric_4_5_7_8_Data_QC.E51()
        var_1 = divide(g50_1, e51_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B51():
    # 'Metric_4_5_7_8_Data_QC'!B51
    value = "Total"

@register(Metric_4_5_7_8_Data_QC)
class E51():
    # 'Metric_4_5_7_8_Data_QC'!E51
    value = "#N/A"
    formula = "=SUM(E42:E49)"
    @eval_fn
    def E51():
        range_1 = Metric_4_5_7_8_Data_QC(5, 42, 5, 49)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F51():
    # 'Metric_4_5_7_8_Data_QC'!F51
    value = 2152174164.92
    formula = "=SUM(F42:F49)"
    @eval_fn
    def F51():
        range_1 = Metric_4_5_7_8_Data_QC(6, 42, 6, 49)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G51():
    # 'Metric_4_5_7_8_Data_QC'!G51
    value = "#N/A"
    formula = "=SUM(G42:G49)"
    @eval_fn
    def G51():
        range_1 = Metric_4_5_7_8_Data_QC(7, 42, 7, 49)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H51():
    # 'Metric_4_5_7_8_Data_QC'!H51
    value = "#N/A"
    formula = "=G51/E51"
    @eval_fn
    def H51():
        g51_1 = Metric_4_5_7_8_Data_QC.G51()
        e51_1 = Metric_4_5_7_8_Data_QC.E51()
        var_1 = divide(g51_1, e51_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class A52():
    # 'Metric_4_5_7_8_Data_QC'!A52
    value = "Air Transportation"

@register(Metric_4_5_7_8_Data_QC)
class E52():
    # 'Metric_4_5_7_8_Data_QC'!E52
    value = "EIA Reported"

@register(Metric_4_5_7_8_Data_QC)
class F52():
    # 'Metric_4_5_7_8_Data_QC'!F52
    value = "Calculated Expenditures"

@register(Metric_4_5_7_8_Data_QC)
class G52():
    # 'Metric_4_5_7_8_Data_QC'!G52
    value = "Difference"

@register(Metric_4_5_7_8_Data_QC)
class H52():
    # 'Metric_4_5_7_8_Data_QC'!H52
    value = "Difference as % of EIA"

@register(Metric_4_5_7_8_Data_QC)
class I52():
    # 'Metric_4_5_7_8_Data_QC'!I52
    value = "Difference as % of Sector Total"

@register(Metric_4_5_7_8_Data_QC)
class B53():
    # 'Metric_4_5_7_8_Data_QC'!B53
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class C53():
    # 'Metric_4_5_7_8_Data_QC'!C53
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E53():
    # 'Metric_4_5_7_8_Data_QC'!E53
    value = 0
    formula = "=VLOOKUP(C53,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E53():
        c53_1 = Metric_4_5_7_8_Data_QC.C53()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c53_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F53():
    # 'Metric_4_5_7_8_Data_QC'!F53
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G52:R52)"
    @eval_fn
    def F53():
        range_1 = Dashboard_M4_Cost_Monthly(7, 52, 18, 52)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G53():
    # 'Metric_4_5_7_8_Data_QC'!G53
    value = 0
    formula = "=F53-E53"
    @eval_fn
    def G53():
        f53_1 = Metric_4_5_7_8_Data_QC.F53()
        e53_1 = Metric_4_5_7_8_Data_QC.E53()
        var_1 = sub(f53_1, e53_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I53():
    # 'Metric_4_5_7_8_Data_QC'!I53
    value = "#N/A"
    formula = "=G53/E62"
    @eval_fn
    def I53():
        g53_1 = Metric_4_5_7_8_Data_QC.G53()
        e62_1 = Metric_4_5_7_8_Data_QC.E62()
        var_1 = divide(g53_1, e62_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B54():
    # 'Metric_4_5_7_8_Data_QC'!B54
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class C54():
    # 'Metric_4_5_7_8_Data_QC'!C54
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E54():
    # 'Metric_4_5_7_8_Data_QC'!E54
    value = 0
    formula = "=VLOOKUP(C54,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E54():
        c54_1 = Metric_4_5_7_8_Data_QC.C54()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c54_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F54():
    # 'Metric_4_5_7_8_Data_QC'!F54
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G53:R53)"
    @eval_fn
    def F54():
        range_1 = Dashboard_M4_Cost_Monthly(7, 53, 18, 53)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G54():
    # 'Metric_4_5_7_8_Data_QC'!G54
    value = 0
    formula = "=F54-E54"
    @eval_fn
    def G54():
        f54_1 = Metric_4_5_7_8_Data_QC.F54()
        e54_1 = Metric_4_5_7_8_Data_QC.E54()
        var_1 = sub(f54_1, e54_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I54():
    # 'Metric_4_5_7_8_Data_QC'!I54
    value = "#N/A"
    formula = "=G54/E62"
    @eval_fn
    def I54():
        g54_1 = Metric_4_5_7_8_Data_QC.G54()
        e62_1 = Metric_4_5_7_8_Data_QC.E62()
        var_1 = divide(g54_1, e62_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B55():
    # 'Metric_4_5_7_8_Data_QC'!B55
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class C55():
    # 'Metric_4_5_7_8_Data_QC'!C55
    value = "JFACV"

@register(Metric_4_5_7_8_Data_QC)
class D55():
    # 'Metric_4_5_7_8_Data_QC'!D55
    value = "#N/A"
    formula = "=VLOOKUP(C55,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D55():
        c55_1 = Metric_4_5_7_8_Data_QC.C55()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c55_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E55():
    # 'Metric_4_5_7_8_Data_QC'!E55
    value = "#N/A"
    formula = "=VLOOKUP(C55,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E55():
        c55_1 = Metric_4_5_7_8_Data_QC.C55()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c55_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F55():
    # 'Metric_4_5_7_8_Data_QC'!F55
    value = 1456279791.06
    formula = "=SUM('Dashboard M4 Cost Monthly'!G54:R54)"
    @eval_fn
    def F55():
        range_1 = Dashboard_M4_Cost_Monthly(7, 54, 18, 54)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G55():
    # 'Metric_4_5_7_8_Data_QC'!G55
    value = "#N/A"
    formula = "=F55-E55"
    @eval_fn
    def G55():
        f55_1 = Metric_4_5_7_8_Data_QC.F55()
        e55_1 = Metric_4_5_7_8_Data_QC.E55()
        var_1 = sub(f55_1, e55_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H55():
    # 'Metric_4_5_7_8_Data_QC'!H55
    value = "#N/A"
    formula = "=G55/E55"
    @eval_fn
    def H55():
        g55_1 = Metric_4_5_7_8_Data_QC.G55()
        e55_1 = Metric_4_5_7_8_Data_QC.E55()
        var_1 = divide(g55_1, e55_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I55():
    # 'Metric_4_5_7_8_Data_QC'!I55
    value = "#N/A"
    formula = "=G55/E62"
    @eval_fn
    def I55():
        g55_1 = Metric_4_5_7_8_Data_QC.G55()
        e62_1 = Metric_4_5_7_8_Data_QC.E62()
        var_1 = divide(g55_1, e62_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B56():
    # 'Metric_4_5_7_8_Data_QC'!B56
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class C56():
    # 'Metric_4_5_7_8_Data_QC'!C56
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E56():
    # 'Metric_4_5_7_8_Data_QC'!E56
    value = 0
    formula = "=VLOOKUP(C56,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E56():
        c56_1 = Metric_4_5_7_8_Data_QC.C56()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c56_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F56():
    # 'Metric_4_5_7_8_Data_QC'!F56
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G55:R55)"
    @eval_fn
    def F56():
        range_1 = Dashboard_M4_Cost_Monthly(7, 55, 18, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G56():
    # 'Metric_4_5_7_8_Data_QC'!G56
    value = 0
    formula = "=F56-E56"
    @eval_fn
    def G56():
        f56_1 = Metric_4_5_7_8_Data_QC.F56()
        e56_1 = Metric_4_5_7_8_Data_QC.E56()
        var_1 = sub(f56_1, e56_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I56():
    # 'Metric_4_5_7_8_Data_QC'!I56
    value = "#N/A"
    formula = "=G56/E62"
    @eval_fn
    def I56():
        g56_1 = Metric_4_5_7_8_Data_QC.G56()
        e62_1 = Metric_4_5_7_8_Data_QC.E62()
        var_1 = divide(g56_1, e62_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B57():
    # 'Metric_4_5_7_8_Data_QC'!B57
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class C57():
    # 'Metric_4_5_7_8_Data_QC'!C57
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E57():
    # 'Metric_4_5_7_8_Data_QC'!E57
    value = 0
    formula = "=VLOOKUP(C57,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E57():
        c57_1 = Metric_4_5_7_8_Data_QC.C57()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c57_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F57():
    # 'Metric_4_5_7_8_Data_QC'!F57
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G56:R56)"
    @eval_fn
    def F57():
        range_1 = Dashboard_M4_Cost_Monthly(7, 56, 18, 56)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G57():
    # 'Metric_4_5_7_8_Data_QC'!G57
    value = 0
    formula = "=F57-E57"
    @eval_fn
    def G57():
        f57_1 = Metric_4_5_7_8_Data_QC.F57()
        e57_1 = Metric_4_5_7_8_Data_QC.E57()
        var_1 = sub(f57_1, e57_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I57():
    # 'Metric_4_5_7_8_Data_QC'!I57
    value = "#N/A"
    formula = "=G57/E62"
    @eval_fn
    def I57():
        g57_1 = Metric_4_5_7_8_Data_QC.G57()
        e62_1 = Metric_4_5_7_8_Data_QC.E62()
        var_1 = divide(g57_1, e62_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B58():
    # 'Metric_4_5_7_8_Data_QC'!B58
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class C58():
    # 'Metric_4_5_7_8_Data_QC'!C58
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E58():
    # 'Metric_4_5_7_8_Data_QC'!E58
    value = 0
    formula = "=VLOOKUP(C58,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E58():
        c58_1 = Metric_4_5_7_8_Data_QC.C58()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c58_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F58():
    # 'Metric_4_5_7_8_Data_QC'!F58
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G57:R57)"
    @eval_fn
    def F58():
        range_1 = Dashboard_M4_Cost_Monthly(7, 57, 18, 57)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G58():
    # 'Metric_4_5_7_8_Data_QC'!G58
    value = 0
    formula = "=F58-E58"
    @eval_fn
    def G58():
        f58_1 = Metric_4_5_7_8_Data_QC.F58()
        e58_1 = Metric_4_5_7_8_Data_QC.E58()
        var_1 = sub(f58_1, e58_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I58():
    # 'Metric_4_5_7_8_Data_QC'!I58
    value = "#N/A"
    formula = "=G58/E62"
    @eval_fn
    def I58():
        g58_1 = Metric_4_5_7_8_Data_QC.G58()
        e62_1 = Metric_4_5_7_8_Data_QC.E62()
        var_1 = divide(g58_1, e62_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B59():
    # 'Metric_4_5_7_8_Data_QC'!B59
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class C59():
    # 'Metric_4_5_7_8_Data_QC'!C59
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E59():
    # 'Metric_4_5_7_8_Data_QC'!E59
    value = 0
    formula = "=VLOOKUP(C59,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E59():
        c59_1 = Metric_4_5_7_8_Data_QC.C59()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c59_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F59():
    # 'Metric_4_5_7_8_Data_QC'!F59
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G58:R58)"
    @eval_fn
    def F59():
        range_1 = Dashboard_M4_Cost_Monthly(7, 58, 18, 58)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G59():
    # 'Metric_4_5_7_8_Data_QC'!G59
    value = 0
    formula = "=F59-E59"
    @eval_fn
    def G59():
        f59_1 = Metric_4_5_7_8_Data_QC.F59()
        e59_1 = Metric_4_5_7_8_Data_QC.E59()
        var_1 = sub(f59_1, e59_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I59():
    # 'Metric_4_5_7_8_Data_QC'!I59
    value = "#N/A"
    formula = "=G59/E62"
    @eval_fn
    def I59():
        g59_1 = Metric_4_5_7_8_Data_QC.G59()
        e62_1 = Metric_4_5_7_8_Data_QC.E62()
        var_1 = divide(g59_1, e62_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B60():
    # 'Metric_4_5_7_8_Data_QC'!B60
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class C60():
    # 'Metric_4_5_7_8_Data_QC'!C60
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E60():
    # 'Metric_4_5_7_8_Data_QC'!E60
    value = 0
    formula = "=VLOOKUP(C60,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E60():
        c60_1 = Metric_4_5_7_8_Data_QC.C60()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c60_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F60():
    # 'Metric_4_5_7_8_Data_QC'!F60
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G59:R59)"
    @eval_fn
    def F60():
        range_1 = Dashboard_M4_Cost_Monthly(7, 59, 18, 59)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G60():
    # 'Metric_4_5_7_8_Data_QC'!G60
    value = 0
    formula = "=F60-E60"
    @eval_fn
    def G60():
        f60_1 = Metric_4_5_7_8_Data_QC.F60()
        e60_1 = Metric_4_5_7_8_Data_QC.E60()
        var_1 = sub(f60_1, e60_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I60():
    # 'Metric_4_5_7_8_Data_QC'!I60
    value = "#N/A"
    formula = "=G60/E62"
    @eval_fn
    def I60():
        g60_1 = Metric_4_5_7_8_Data_QC.G60()
        e62_1 = Metric_4_5_7_8_Data_QC.E62()
        var_1 = divide(g60_1, e62_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B61():
    # 'Metric_4_5_7_8_Data_QC'!B61
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class C61():
    # 'Metric_4_5_7_8_Data_QC'!C61
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E61():
    # 'Metric_4_5_7_8_Data_QC'!E61
    value = 0
    formula = "=VLOOKUP(C61,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)*1000000"
    @eval_fn
    def E61():
        c61_1 = Metric_4_5_7_8_Data_QC.C61()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c61_1, range_1, g1_1, "FALSE")
        var_2 = mult(var_1, 1000000)
        return var_2

@register(Metric_4_5_7_8_Data_QC)
class F61():
    # 'Metric_4_5_7_8_Data_QC'!F61
    value = 0
    formula = "=SUM('Dashboard M4 Cost Monthly'!G60:R60)"
    @eval_fn
    def F61():
        range_1 = Dashboard_M4_Cost_Monthly(7, 60, 18, 60)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G61():
    # 'Metric_4_5_7_8_Data_QC'!G61
    value = 0
    formula = "=F61-E61"
    @eval_fn
    def G61():
        f61_1 = Metric_4_5_7_8_Data_QC.F61()
        e61_1 = Metric_4_5_7_8_Data_QC.E61()
        var_1 = sub(f61_1, e61_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I61():
    # 'Metric_4_5_7_8_Data_QC'!I61
    value = "#N/A"
    formula = "=G61/E62"
    @eval_fn
    def I61():
        g61_1 = Metric_4_5_7_8_Data_QC.G61()
        e62_1 = Metric_4_5_7_8_Data_QC.E62()
        var_1 = divide(g61_1, e62_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B62():
    # 'Metric_4_5_7_8_Data_QC'!B62
    value = "Total"

@register(Metric_4_5_7_8_Data_QC)
class E62():
    # 'Metric_4_5_7_8_Data_QC'!E62
    value = "#N/A"
    formula = "=SUM(E53:E60)"
    @eval_fn
    def E62():
        range_1 = Metric_4_5_7_8_Data_QC(5, 53, 5, 60)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F62():
    # 'Metric_4_5_7_8_Data_QC'!F62
    value = 1456279791.06
    formula = "=SUM(F53:F60)"
    @eval_fn
    def F62():
        range_1 = Metric_4_5_7_8_Data_QC(6, 53, 6, 60)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G62():
    # 'Metric_4_5_7_8_Data_QC'!G62
    value = "#N/A"
    formula = "=SUM(G53:G60)"
    @eval_fn
    def G62():
        range_1 = Metric_4_5_7_8_Data_QC(7, 53, 7, 60)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H62():
    # 'Metric_4_5_7_8_Data_QC'!H62
    value = "#N/A"
    formula = "=G62/E62"
    @eval_fn
    def H62():
        g62_1 = Metric_4_5_7_8_Data_QC.G62()
        e62_1 = Metric_4_5_7_8_Data_QC.E62()
        var_1 = divide(g62_1, e62_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class A64():
    # 'Metric_4_5_7_8_Data_QC'!A64
    value = "All Sectors"

@register(Metric_4_5_7_8_Data_QC)
class E64():
    # 'Metric_4_5_7_8_Data_QC'!E64
    value = "EIA Reported"

@register(Metric_4_5_7_8_Data_QC)
class F64():
    # 'Metric_4_5_7_8_Data_QC'!F64
    value = "Calculated Expenditures"

@register(Metric_4_5_7_8_Data_QC)
class G64():
    # 'Metric_4_5_7_8_Data_QC'!G64
    value = "Difference"

@register(Metric_4_5_7_8_Data_QC)
class H64():
    # 'Metric_4_5_7_8_Data_QC'!H64
    value = "Difference as % of EIA"

@register(Metric_4_5_7_8_Data_QC)
class I64():
    # 'Metric_4_5_7_8_Data_QC'!I64
    value = "Difference as % of Sector Total"

@register(Metric_4_5_7_8_Data_QC)
class B65():
    # 'Metric_4_5_7_8_Data_QC'!B65
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class E65():
    # 'Metric_4_5_7_8_Data_QC'!E65
    value = "#N/A"
    formula = "=E53+E42+E31+E20+E9"
    @eval_fn
    def E65():
        e53_1 = Metric_4_5_7_8_Data_QC.E53()
        e42_1 = Metric_4_5_7_8_Data_QC.E42()
        var_1 = add(e53_1, e42_1)
        e31_1 = Metric_4_5_7_8_Data_QC.E31()
        var_2 = add(var_1, e31_1)
        e20_1 = Metric_4_5_7_8_Data_QC.E20()
        var_3 = add(var_2, e20_1)
        e9_1 = Metric_4_5_7_8_Data_QC.E9()
        var_4 = add(var_3, e9_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class F65():
    # 'Metric_4_5_7_8_Data_QC'!F65
    value = 2143780338.14
    formula = "=F53+F42+F31+F20+F9"
    @eval_fn
    def F65():
        f53_1 = Metric_4_5_7_8_Data_QC.F53()
        f42_1 = Metric_4_5_7_8_Data_QC.F42()
        var_1 = add(f53_1, f42_1)
        f31_1 = Metric_4_5_7_8_Data_QC.F31()
        var_2 = add(var_1, f31_1)
        f20_1 = Metric_4_5_7_8_Data_QC.F20()
        var_3 = add(var_2, f20_1)
        f9_1 = Metric_4_5_7_8_Data_QC.F9()
        var_4 = add(var_3, f9_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class G65():
    # 'Metric_4_5_7_8_Data_QC'!G65
    value = "#N/A"
    formula = "=F65-E65"
    @eval_fn
    def G65():
        f65_1 = Metric_4_5_7_8_Data_QC.F65()
        e65_1 = Metric_4_5_7_8_Data_QC.E65()
        var_1 = sub(f65_1, e65_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H65():
    # 'Metric_4_5_7_8_Data_QC'!H65
    value = "#N/A"
    formula = "=G65/E65"
    @eval_fn
    def H65():
        g65_1 = Metric_4_5_7_8_Data_QC.G65()
        e65_1 = Metric_4_5_7_8_Data_QC.E65()
        var_1 = divide(g65_1, e65_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I65():
    # 'Metric_4_5_7_8_Data_QC'!I65
    value = "#N/A"
    formula = "=G65/E74"
    @eval_fn
    def I65():
        g65_1 = Metric_4_5_7_8_Data_QC.G65()
        e74_1 = Metric_4_5_7_8_Data_QC.E74()
        var_1 = divide(g65_1, e74_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B66():
    # 'Metric_4_5_7_8_Data_QC'!B66
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class E66():
    # 'Metric_4_5_7_8_Data_QC'!E66
    value = "#N/A"
    formula = "=E54+E43+E32+E21+E10"
    @eval_fn
    def E66():
        e54_1 = Metric_4_5_7_8_Data_QC.E54()
        e43_1 = Metric_4_5_7_8_Data_QC.E43()
        var_1 = add(e54_1, e43_1)
        e32_1 = Metric_4_5_7_8_Data_QC.E32()
        var_2 = add(var_1, e32_1)
        e21_1 = Metric_4_5_7_8_Data_QC.E21()
        var_3 = add(var_2, e21_1)
        e10_1 = Metric_4_5_7_8_Data_QC.E10()
        var_4 = add(var_3, e10_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class F66():
    # 'Metric_4_5_7_8_Data_QC'!F66
    value = 1533526270.67
    formula = "=F54+F43+F32+F21+F10"
    @eval_fn
    def F66():
        f54_1 = Metric_4_5_7_8_Data_QC.F54()
        f43_1 = Metric_4_5_7_8_Data_QC.F43()
        var_1 = add(f54_1, f43_1)
        f32_1 = Metric_4_5_7_8_Data_QC.F32()
        var_2 = add(var_1, f32_1)
        f21_1 = Metric_4_5_7_8_Data_QC.F21()
        var_3 = add(var_2, f21_1)
        f10_1 = Metric_4_5_7_8_Data_QC.F10()
        var_4 = add(var_3, f10_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class G66():
    # 'Metric_4_5_7_8_Data_QC'!G66
    value = "#N/A"
    formula = "=F66-E66"
    @eval_fn
    def G66():
        f66_1 = Metric_4_5_7_8_Data_QC.F66()
        e66_1 = Metric_4_5_7_8_Data_QC.E66()
        var_1 = sub(f66_1, e66_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H66():
    # 'Metric_4_5_7_8_Data_QC'!H66
    value = "#N/A"
    formula = "=G66/E66"
    @eval_fn
    def H66():
        g66_1 = Metric_4_5_7_8_Data_QC.G66()
        e66_1 = Metric_4_5_7_8_Data_QC.E66()
        var_1 = divide(g66_1, e66_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I66():
    # 'Metric_4_5_7_8_Data_QC'!I66
    value = "#N/A"
    formula = "=G66/E74"
    @eval_fn
    def I66():
        g66_1 = Metric_4_5_7_8_Data_QC.G66()
        e74_1 = Metric_4_5_7_8_Data_QC.E74()
        var_1 = divide(g66_1, e74_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B67():
    # 'Metric_4_5_7_8_Data_QC'!B67
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class E67():
    # 'Metric_4_5_7_8_Data_QC'!E67
    value = "#N/A"
    formula = "=E55+E44+E33+E22+E11"
    @eval_fn
    def E67():
        e55_1 = Metric_4_5_7_8_Data_QC.E55()
        e44_1 = Metric_4_5_7_8_Data_QC.E44()
        var_1 = add(e55_1, e44_1)
        e33_1 = Metric_4_5_7_8_Data_QC.E33()
        var_2 = add(var_1, e33_1)
        e22_1 = Metric_4_5_7_8_Data_QC.E22()
        var_3 = add(var_2, e22_1)
        e11_1 = Metric_4_5_7_8_Data_QC.E11()
        var_4 = add(var_3, e11_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class F67():
    # 'Metric_4_5_7_8_Data_QC'!F67
    value = 1456279791.06
    formula = "=F55+F44+F33+F22+F11"
    @eval_fn
    def F67():
        f55_1 = Metric_4_5_7_8_Data_QC.F55()
        f44_1 = Metric_4_5_7_8_Data_QC.F44()
        var_1 = add(f55_1, f44_1)
        f33_1 = Metric_4_5_7_8_Data_QC.F33()
        var_2 = add(var_1, f33_1)
        f22_1 = Metric_4_5_7_8_Data_QC.F22()
        var_3 = add(var_2, f22_1)
        f11_1 = Metric_4_5_7_8_Data_QC.F11()
        var_4 = add(var_3, f11_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class G67():
    # 'Metric_4_5_7_8_Data_QC'!G67
    value = "#N/A"
    formula = "=F67-E67"
    @eval_fn
    def G67():
        f67_1 = Metric_4_5_7_8_Data_QC.F67()
        e67_1 = Metric_4_5_7_8_Data_QC.E67()
        var_1 = sub(f67_1, e67_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H67():
    # 'Metric_4_5_7_8_Data_QC'!H67
    value = "#N/A"
    formula = "=G67/E67"
    @eval_fn
    def H67():
        g67_1 = Metric_4_5_7_8_Data_QC.G67()
        e67_1 = Metric_4_5_7_8_Data_QC.E67()
        var_1 = divide(g67_1, e67_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I67():
    # 'Metric_4_5_7_8_Data_QC'!I67
    value = "#N/A"
    formula = "=G67/E74"
    @eval_fn
    def I67():
        g67_1 = Metric_4_5_7_8_Data_QC.G67()
        e74_1 = Metric_4_5_7_8_Data_QC.E74()
        var_1 = divide(g67_1, e74_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B68():
    # 'Metric_4_5_7_8_Data_QC'!B68
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class E68():
    # 'Metric_4_5_7_8_Data_QC'!E68
    value = "#N/A"
    formula = "=E56+E45+E34+E23+E12"
    @eval_fn
    def E68():
        e56_1 = Metric_4_5_7_8_Data_QC.E56()
        e45_1 = Metric_4_5_7_8_Data_QC.E45()
        var_1 = add(e56_1, e45_1)
        e34_1 = Metric_4_5_7_8_Data_QC.E34()
        var_2 = add(var_1, e34_1)
        e23_1 = Metric_4_5_7_8_Data_QC.E23()
        var_3 = add(var_2, e23_1)
        e12_1 = Metric_4_5_7_8_Data_QC.E12()
        var_4 = add(var_3, e12_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class F68():
    # 'Metric_4_5_7_8_Data_QC'!F68
    value = 616508808.557
    formula = "=F56+F45+F34+F23+F12"
    @eval_fn
    def F68():
        f56_1 = Metric_4_5_7_8_Data_QC.F56()
        f45_1 = Metric_4_5_7_8_Data_QC.F45()
        var_1 = add(f56_1, f45_1)
        f34_1 = Metric_4_5_7_8_Data_QC.F34()
        var_2 = add(var_1, f34_1)
        f23_1 = Metric_4_5_7_8_Data_QC.F23()
        var_3 = add(var_2, f23_1)
        f12_1 = Metric_4_5_7_8_Data_QC.F12()
        var_4 = add(var_3, f12_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class G68():
    # 'Metric_4_5_7_8_Data_QC'!G68
    value = "#N/A"
    formula = "=F68-E68"
    @eval_fn
    def G68():
        f68_1 = Metric_4_5_7_8_Data_QC.F68()
        e68_1 = Metric_4_5_7_8_Data_QC.E68()
        var_1 = sub(f68_1, e68_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H68():
    # 'Metric_4_5_7_8_Data_QC'!H68
    value = "#N/A"
    formula = "=G68/E68"
    @eval_fn
    def H68():
        g68_1 = Metric_4_5_7_8_Data_QC.G68()
        e68_1 = Metric_4_5_7_8_Data_QC.E68()
        var_1 = divide(g68_1, e68_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I68():
    # 'Metric_4_5_7_8_Data_QC'!I68
    value = "#N/A"
    formula = "=G68/E74"
    @eval_fn
    def I68():
        g68_1 = Metric_4_5_7_8_Data_QC.G68()
        e74_1 = Metric_4_5_7_8_Data_QC.E74()
        var_1 = divide(g68_1, e74_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B69():
    # 'Metric_4_5_7_8_Data_QC'!B69
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class E69():
    # 'Metric_4_5_7_8_Data_QC'!E69
    value = "#N/A"
    formula = "=E57+E46+E35+E24+E13"
    @eval_fn
    def E69():
        e57_1 = Metric_4_5_7_8_Data_QC.E57()
        e46_1 = Metric_4_5_7_8_Data_QC.E46()
        var_1 = add(e57_1, e46_1)
        e35_1 = Metric_4_5_7_8_Data_QC.E35()
        var_2 = add(var_1, e35_1)
        e24_1 = Metric_4_5_7_8_Data_QC.E24()
        var_3 = add(var_2, e24_1)
        e13_1 = Metric_4_5_7_8_Data_QC.E13()
        var_4 = add(var_3, e13_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class F69():
    # 'Metric_4_5_7_8_Data_QC'!F69
    value = 151710827.21
    formula = "=F57+F46+F35+F24+F13"
    @eval_fn
    def F69():
        f57_1 = Metric_4_5_7_8_Data_QC.F57()
        f46_1 = Metric_4_5_7_8_Data_QC.F46()
        var_1 = add(f57_1, f46_1)
        f35_1 = Metric_4_5_7_8_Data_QC.F35()
        var_2 = add(var_1, f35_1)
        f24_1 = Metric_4_5_7_8_Data_QC.F24()
        var_3 = add(var_2, f24_1)
        f13_1 = Metric_4_5_7_8_Data_QC.F13()
        var_4 = add(var_3, f13_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class G69():
    # 'Metric_4_5_7_8_Data_QC'!G69
    value = "#N/A"
    formula = "=F69-E69"
    @eval_fn
    def G69():
        f69_1 = Metric_4_5_7_8_Data_QC.F69()
        e69_1 = Metric_4_5_7_8_Data_QC.E69()
        var_1 = sub(f69_1, e69_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H69():
    # 'Metric_4_5_7_8_Data_QC'!H69
    value = "#N/A"
    formula = "=G69/E69"
    @eval_fn
    def H69():
        g69_1 = Metric_4_5_7_8_Data_QC.G69()
        e69_1 = Metric_4_5_7_8_Data_QC.E69()
        var_1 = divide(g69_1, e69_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I69():
    # 'Metric_4_5_7_8_Data_QC'!I69
    value = "#N/A"
    formula = "=G69/E74"
    @eval_fn
    def I69():
        g69_1 = Metric_4_5_7_8_Data_QC.G69()
        e74_1 = Metric_4_5_7_8_Data_QC.E74()
        var_1 = divide(g69_1, e74_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B70():
    # 'Metric_4_5_7_8_Data_QC'!B70
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class E70():
    # 'Metric_4_5_7_8_Data_QC'!E70
    value = "#N/A"
    formula = "=E58+E47+E36+E25+E14"
    @eval_fn
    def E70():
        e58_1 = Metric_4_5_7_8_Data_QC.E58()
        e47_1 = Metric_4_5_7_8_Data_QC.E47()
        var_1 = add(e58_1, e47_1)
        e36_1 = Metric_4_5_7_8_Data_QC.E36()
        var_2 = add(var_1, e36_1)
        e25_1 = Metric_4_5_7_8_Data_QC.E25()
        var_3 = add(var_2, e25_1)
        e14_1 = Metric_4_5_7_8_Data_QC.E14()
        var_4 = add(var_3, e14_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class F70():
    # 'Metric_4_5_7_8_Data_QC'!F70
    value = 59148947.5473
    formula = "=F58+F47+F36+F25+F14"
    @eval_fn
    def F70():
        f58_1 = Metric_4_5_7_8_Data_QC.F58()
        f47_1 = Metric_4_5_7_8_Data_QC.F47()
        var_1 = add(f58_1, f47_1)
        f36_1 = Metric_4_5_7_8_Data_QC.F36()
        var_2 = add(var_1, f36_1)
        f25_1 = Metric_4_5_7_8_Data_QC.F25()
        var_3 = add(var_2, f25_1)
        f14_1 = Metric_4_5_7_8_Data_QC.F14()
        var_4 = add(var_3, f14_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class G70():
    # 'Metric_4_5_7_8_Data_QC'!G70
    value = "#N/A"
    formula = "=F70-E70"
    @eval_fn
    def G70():
        f70_1 = Metric_4_5_7_8_Data_QC.F70()
        e70_1 = Metric_4_5_7_8_Data_QC.E70()
        var_1 = sub(f70_1, e70_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H70():
    # 'Metric_4_5_7_8_Data_QC'!H70
    value = "#N/A"
    formula = "=G70/E70"
    @eval_fn
    def H70():
        g70_1 = Metric_4_5_7_8_Data_QC.G70()
        e70_1 = Metric_4_5_7_8_Data_QC.E70()
        var_1 = divide(g70_1, e70_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I70():
    # 'Metric_4_5_7_8_Data_QC'!I70
    value = "#N/A"
    formula = "=G70/E74"
    @eval_fn
    def I70():
        g70_1 = Metric_4_5_7_8_Data_QC.G70()
        e74_1 = Metric_4_5_7_8_Data_QC.E74()
        var_1 = divide(g70_1, e74_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B71():
    # 'Metric_4_5_7_8_Data_QC'!B71
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class E71():
    # 'Metric_4_5_7_8_Data_QC'!E71
    value = "#N/A"
    formula = "=E59+E48+E37+E26+E15"
    @eval_fn
    def E71():
        e59_1 = Metric_4_5_7_8_Data_QC.E59()
        e48_1 = Metric_4_5_7_8_Data_QC.E48()
        var_1 = add(e59_1, e48_1)
        e37_1 = Metric_4_5_7_8_Data_QC.E37()
        var_2 = add(var_1, e37_1)
        e26_1 = Metric_4_5_7_8_Data_QC.E26()
        var_3 = add(var_2, e26_1)
        e15_1 = Metric_4_5_7_8_Data_QC.E15()
        var_4 = add(var_3, e15_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class F71():
    # 'Metric_4_5_7_8_Data_QC'!F71
    value = 75302421.6404
    formula = "=F59+F48+F37+F26+F15"
    @eval_fn
    def F71():
        f59_1 = Metric_4_5_7_8_Data_QC.F59()
        f48_1 = Metric_4_5_7_8_Data_QC.F48()
        var_1 = add(f59_1, f48_1)
        f37_1 = Metric_4_5_7_8_Data_QC.F37()
        var_2 = add(var_1, f37_1)
        f26_1 = Metric_4_5_7_8_Data_QC.F26()
        var_3 = add(var_2, f26_1)
        f15_1 = Metric_4_5_7_8_Data_QC.F15()
        var_4 = add(var_3, f15_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class G71():
    # 'Metric_4_5_7_8_Data_QC'!G71
    value = "#N/A"
    formula = "=F71-E71"
    @eval_fn
    def G71():
        f71_1 = Metric_4_5_7_8_Data_QC.F71()
        e71_1 = Metric_4_5_7_8_Data_QC.E71()
        var_1 = sub(f71_1, e71_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H71():
    # 'Metric_4_5_7_8_Data_QC'!H71
    value = "#N/A"
    formula = "=G71/E71"
    @eval_fn
    def H71():
        g71_1 = Metric_4_5_7_8_Data_QC.G71()
        e71_1 = Metric_4_5_7_8_Data_QC.E71()
        var_1 = divide(g71_1, e71_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I71():
    # 'Metric_4_5_7_8_Data_QC'!I71
    value = "#N/A"
    formula = "=G71/E74"
    @eval_fn
    def I71():
        g71_1 = Metric_4_5_7_8_Data_QC.G71()
        e74_1 = Metric_4_5_7_8_Data_QC.E74()
        var_1 = divide(g71_1, e74_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B72():
    # 'Metric_4_5_7_8_Data_QC'!B72
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class E72():
    # 'Metric_4_5_7_8_Data_QC'!E72
    value = 0
    formula = "=E60+E49+E38+E27+E16"
    @eval_fn
    def E72():
        e60_1 = Metric_4_5_7_8_Data_QC.E60()
        e49_1 = Metric_4_5_7_8_Data_QC.E49()
        var_1 = add(e60_1, e49_1)
        e38_1 = Metric_4_5_7_8_Data_QC.E38()
        var_2 = add(var_1, e38_1)
        e27_1 = Metric_4_5_7_8_Data_QC.E27()
        var_3 = add(var_2, e27_1)
        e16_1 = Metric_4_5_7_8_Data_QC.E16()
        var_4 = add(var_3, e16_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class F72():
    # 'Metric_4_5_7_8_Data_QC'!F72
    value = 0
    formula = "=F60+F49+F38+F27+F16"
    @eval_fn
    def F72():
        f60_1 = Metric_4_5_7_8_Data_QC.F60()
        f49_1 = Metric_4_5_7_8_Data_QC.F49()
        var_1 = add(f60_1, f49_1)
        f38_1 = Metric_4_5_7_8_Data_QC.F38()
        var_2 = add(var_1, f38_1)
        f27_1 = Metric_4_5_7_8_Data_QC.F27()
        var_3 = add(var_2, f27_1)
        f16_1 = Metric_4_5_7_8_Data_QC.F16()
        var_4 = add(var_3, f16_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class G72():
    # 'Metric_4_5_7_8_Data_QC'!G72
    value = 0
    formula = "=F72-E72"
    @eval_fn
    def G72():
        f72_1 = Metric_4_5_7_8_Data_QC.F72()
        e72_1 = Metric_4_5_7_8_Data_QC.E72()
        var_1 = sub(f72_1, e72_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I72():
    # 'Metric_4_5_7_8_Data_QC'!I72
    value = "#N/A"
    formula = "=G72/E74"
    @eval_fn
    def I72():
        g72_1 = Metric_4_5_7_8_Data_QC.G72()
        e74_1 = Metric_4_5_7_8_Data_QC.E74()
        var_1 = divide(g72_1, e74_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B73():
    # 'Metric_4_5_7_8_Data_QC'!B73
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class E73():
    # 'Metric_4_5_7_8_Data_QC'!E73
    value = "#N/A"
    formula = "=E61+E50+E39+E28+E17"
    @eval_fn
    def E73():
        e61_1 = Metric_4_5_7_8_Data_QC.E61()
        e50_1 = Metric_4_5_7_8_Data_QC.E50()
        var_1 = add(e61_1, e50_1)
        e39_1 = Metric_4_5_7_8_Data_QC.E39()
        var_2 = add(var_1, e39_1)
        e28_1 = Metric_4_5_7_8_Data_QC.E28()
        var_3 = add(var_2, e28_1)
        e17_1 = Metric_4_5_7_8_Data_QC.E17()
        var_4 = add(var_3, e17_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class F73():
    # 'Metric_4_5_7_8_Data_QC'!F73
    value = 38463296.5991
    formula = "=F61+F50+F39+F28+F17"
    @eval_fn
    def F73():
        f61_1 = Metric_4_5_7_8_Data_QC.F61()
        f50_1 = Metric_4_5_7_8_Data_QC.F50()
        var_1 = add(f61_1, f50_1)
        f39_1 = Metric_4_5_7_8_Data_QC.F39()
        var_2 = add(var_1, f39_1)
        f28_1 = Metric_4_5_7_8_Data_QC.F28()
        var_3 = add(var_2, f28_1)
        f17_1 = Metric_4_5_7_8_Data_QC.F17()
        var_4 = add(var_3, f17_1)
        return var_4

@register(Metric_4_5_7_8_Data_QC)
class G73():
    # 'Metric_4_5_7_8_Data_QC'!G73
    value = "#N/A"
    formula = "=F73-E73"
    @eval_fn
    def G73():
        f73_1 = Metric_4_5_7_8_Data_QC.F73()
        e73_1 = Metric_4_5_7_8_Data_QC.E73()
        var_1 = sub(f73_1, e73_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H73():
    # 'Metric_4_5_7_8_Data_QC'!H73
    value = "#N/A"
    formula = "=G73/E73"
    @eval_fn
    def H73():
        g73_1 = Metric_4_5_7_8_Data_QC.G73()
        e73_1 = Metric_4_5_7_8_Data_QC.E73()
        var_1 = divide(g73_1, e73_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class I73():
    # 'Metric_4_5_7_8_Data_QC'!I73
    value = "#N/A"
    formula = "=G73/E74"
    @eval_fn
    def I73():
        g73_1 = Metric_4_5_7_8_Data_QC.G73()
        e74_1 = Metric_4_5_7_8_Data_QC.E74()
        var_1 = divide(g73_1, e74_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B74():
    # 'Metric_4_5_7_8_Data_QC'!B74
    value = "Total"

@register(Metric_4_5_7_8_Data_QC)
class E74():
    # 'Metric_4_5_7_8_Data_QC'!E74
    value = "#N/A"
    formula = "=SUM(E65:E72)"
    @eval_fn
    def E74():
        range_1 = Metric_4_5_7_8_Data_QC(5, 65, 5, 72)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F74():
    # 'Metric_4_5_7_8_Data_QC'!F74
    value = 6036257404.83
    formula = "=SUM(F65:F72)"
    @eval_fn
    def F74():
        range_1 = Metric_4_5_7_8_Data_QC(6, 65, 6, 72)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G74():
    # 'Metric_4_5_7_8_Data_QC'!G74
    value = "#N/A"
    formula = "=SUM(G65:G72)"
    @eval_fn
    def G74():
        range_1 = Metric_4_5_7_8_Data_QC(7, 65, 7, 72)
        var_1 = SUM(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H74():
    # 'Metric_4_5_7_8_Data_QC'!H74
    value = "#N/A"
    formula = "=G74/E74"
    @eval_fn
    def H74():
        g74_1 = Metric_4_5_7_8_Data_QC.G74()
        e74_1 = Metric_4_5_7_8_Data_QC.E74()
        var_1 = divide(g74_1, e74_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B77():
    # 'Metric_4_5_7_8_Data_QC'!B77
    value = "The Following tables compare 2006 EIA reported sector portfolio price to 2006 sector portfolio price as calculated in this model. Overall, prices do appear to vary somewhat significantly, but the largest variations are in less important fuels (Residual Fuel Oil, LPG and SNG) and in the commercial and Industrial sectors, where it is significantly more difficult to get these values."

@register(Metric_4_5_7_8_Data_QC)
class A84():
    # 'Metric_4_5_7_8_Data_QC'!A84
    value = "DBEDT Fuel Prices (monthly)"

@register(Metric_4_5_7_8_Data_QC)
class E84():
    # 'Metric_4_5_7_8_Data_QC'!E84
    value = 38718
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class F84():
    # 'Metric_4_5_7_8_Data_QC'!F84
    value = 38749
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class G84():
    # 'Metric_4_5_7_8_Data_QC'!G84
    value = 38777
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class H84():
    # 'Metric_4_5_7_8_Data_QC'!H84
    value = 38808
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class I84():
    # 'Metric_4_5_7_8_Data_QC'!I84
    value = 38930

@register(Metric_4_5_7_8_Data_QC)
class J84():
    # 'Metric_4_5_7_8_Data_QC'!J84
    value = 38961
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class K84():
    # 'Metric_4_5_7_8_Data_QC'!K84
    value = 38991
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class L84():
    # 'Metric_4_5_7_8_Data_QC'!L84
    value = 39022
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class M84():
    # 'Metric_4_5_7_8_Data_QC'!M84
    value = 39052
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class N84():
    # 'Metric_4_5_7_8_Data_QC'!N84
    value = 39083
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class O84():
    # 'Metric_4_5_7_8_Data_QC'!O84
    value = 39114
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class P84():
    # 'Metric_4_5_7_8_Data_QC'!P84
    value = 39142
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class Q84():
    # 'Metric_4_5_7_8_Data_QC'!Q84
    value = 39173
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class R84():
    # 'Metric_4_5_7_8_Data_QC'!R84
    value = 39203
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class S84():
    # 'Metric_4_5_7_8_Data_QC'!S84
    value = 39234
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class T84():
    # 'Metric_4_5_7_8_Data_QC'!T84
    value = 39264
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class U84():
    # 'Metric_4_5_7_8_Data_QC'!U84
    value = 39295
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class V84():
    # 'Metric_4_5_7_8_Data_QC'!V84
    value = 39326
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class W84():
    # 'Metric_4_5_7_8_Data_QC'!W84
    value = 39356
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class X84():
    # 'Metric_4_5_7_8_Data_QC'!X84
    value = 39387
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class Y84():
    # 'Metric_4_5_7_8_Data_QC'!Y84
    value = 39417
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class Z84():
    # 'Metric_4_5_7_8_Data_QC'!Z84
    value = 39448
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AA84():
    # 'Metric_4_5_7_8_Data_QC'!AA84
    value = 39479
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AB84():
    # 'Metric_4_5_7_8_Data_QC'!AB84
    value = 39508
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AC84():
    # 'Metric_4_5_7_8_Data_QC'!AC84
    value = 39539
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AD84():
    # 'Metric_4_5_7_8_Data_QC'!AD84
    value = 39569
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AE84():
    # 'Metric_4_5_7_8_Data_QC'!AE84
    value = 39600
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AF84():
    # 'Metric_4_5_7_8_Data_QC'!AF84
    value = 39630
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AG84():
    # 'Metric_4_5_7_8_Data_QC'!AG84
    value = 39661
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AH84():
    # 'Metric_4_5_7_8_Data_QC'!AH84
    value = 39692
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AI84():
    # 'Metric_4_5_7_8_Data_QC'!AI84
    value = 39722
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AJ84():
    # 'Metric_4_5_7_8_Data_QC'!AJ84
    value = 39753
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AK84():
    # 'Metric_4_5_7_8_Data_QC'!AK84
    value = 39783
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AL84():
    # 'Metric_4_5_7_8_Data_QC'!AL84
    value = 39814
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AM84():
    # 'Metric_4_5_7_8_Data_QC'!AM84
    value = 39845
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AN84():
    # 'Metric_4_5_7_8_Data_QC'!AN84
    value = 39873
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AO84():
    # 'Metric_4_5_7_8_Data_QC'!AO84
    value = 39904
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AP84():
    # 'Metric_4_5_7_8_Data_QC'!AP84
    value = 39934
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AQ84():
    # 'Metric_4_5_7_8_Data_QC'!AQ84
    value = 39965
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AR84():
    # 'Metric_4_5_7_8_Data_QC'!AR84
    value = 39995
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AS84():
    # 'Metric_4_5_7_8_Data_QC'!AS84
    value = 40026
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AT84():
    # 'Metric_4_5_7_8_Data_QC'!AT84
    value = 40057
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AU84():
    # 'Metric_4_5_7_8_Data_QC'!AU84
    value = 40087
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AV84():
    # 'Metric_4_5_7_8_Data_QC'!AV84
    value = 40118
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AW84():
    # 'Metric_4_5_7_8_Data_QC'!AW84
    value = 40148
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AX84():
    # 'Metric_4_5_7_8_Data_QC'!AX84
    value = 40179
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AY84():
    # 'Metric_4_5_7_8_Data_QC'!AY84
    value = 40210
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class AZ84():
    # 'Metric_4_5_7_8_Data_QC'!AZ84
    value = 40238
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BA84():
    # 'Metric_4_5_7_8_Data_QC'!BA84
    value = 40269
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BB84():
    # 'Metric_4_5_7_8_Data_QC'!BB84
    value = 40299
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BC84():
    # 'Metric_4_5_7_8_Data_QC'!BC84
    value = 40330
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BD84():
    # 'Metric_4_5_7_8_Data_QC'!BD84
    value = 40360
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BE84():
    # 'Metric_4_5_7_8_Data_QC'!BE84
    value = 40391
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BF84():
    # 'Metric_4_5_7_8_Data_QC'!BF84
    value = 40422
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BG84():
    # 'Metric_4_5_7_8_Data_QC'!BG84
    value = 40452
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BH84():
    # 'Metric_4_5_7_8_Data_QC'!BH84
    value = 40483
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BI84():
    # 'Metric_4_5_7_8_Data_QC'!BI84
    value = 40513
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BJ84():
    # 'Metric_4_5_7_8_Data_QC'!BJ84
    value = 40544
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BK84():
    # 'Metric_4_5_7_8_Data_QC'!BK84
    value = 40575
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BL84():
    # 'Metric_4_5_7_8_Data_QC'!BL84
    value = 40603
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BM84():
    # 'Metric_4_5_7_8_Data_QC'!BM84
    value = 40634
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BN84():
    # 'Metric_4_5_7_8_Data_QC'!BN84
    value = 40664
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BO84():
    # 'Metric_4_5_7_8_Data_QC'!BO84
    value = 40695
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BP84():
    # 'Metric_4_5_7_8_Data_QC'!BP84
    value = 40725
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BQ84():
    # 'Metric_4_5_7_8_Data_QC'!BQ84
    value = 40756
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BR84():
    # 'Metric_4_5_7_8_Data_QC'!BR84
    value = 40787
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BS84():
    # 'Metric_4_5_7_8_Data_QC'!BS84
    value = 40817
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BT84():
    # 'Metric_4_5_7_8_Data_QC'!BT84
    value = 40848
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BU84():
    # 'Metric_4_5_7_8_Data_QC'!BU84
    value = 40878
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BV84():
    # 'Metric_4_5_7_8_Data_QC'!BV84
    value = 40909
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BW84():
    # 'Metric_4_5_7_8_Data_QC'!BW84
    value = 40940
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BX84():
    # 'Metric_4_5_7_8_Data_QC'!BX84
    value = 40969
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BY84():
    # 'Metric_4_5_7_8_Data_QC'!BY84
    value = 41000
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class BZ84():
    # 'Metric_4_5_7_8_Data_QC'!BZ84
    value = 41030
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class CA84():
    # 'Metric_4_5_7_8_Data_QC'!CA84
    value = 41061
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class CB84():
    # 'Metric_4_5_7_8_Data_QC'!CB84
    value = 41091
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class CC84():
    # 'Metric_4_5_7_8_Data_QC'!CC84
    value = 41122
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class CD84():
    # 'Metric_4_5_7_8_Data_QC'!CD84
    value = 41153
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class CE84():
    # 'Metric_4_5_7_8_Data_QC'!CE84
    value = 41183
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class CF84():
    # 'Metric_4_5_7_8_Data_QC'!CF84
    value = 41214
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class CG84():
    # 'Metric_4_5_7_8_Data_QC'!CG84
    value = 41244
    isdatetime = True

@register(Metric_4_5_7_8_Data_QC)
class B85():
    # 'Metric_4_5_7_8_Data_QC'!B85
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class E85():
    # 'Metric_4_5_7_8_Data_QC'!E85
    value = 59.3688212844
    formula = "='Dashboard M4 Price Monthly'!H111"
    @eval_fn
    def E85():
        h111_1 = Dashboard_M4_Price_Monthly.H111()
        return h111_1

@register(Metric_4_5_7_8_Data_QC)
class F85():
    # 'Metric_4_5_7_8_Data_QC'!F85
    value = 60.0979385567
    formula = "='Dashboard M4 Price Monthly'!I111"
    @eval_fn
    def F85():
        i111_1 = Dashboard_M4_Price_Monthly.I111()
        return i111_1

@register(Metric_4_5_7_8_Data_QC)
class G85():
    # 'Metric_4_5_7_8_Data_QC'!G85
    value = 58.6370992283
    formula = "='Dashboard M4 Price Monthly'!J111"
    @eval_fn
    def G85():
        j111_1 = Dashboard_M4_Price_Monthly.J111()
        return j111_1

@register(Metric_4_5_7_8_Data_QC)
class H85():
    # 'Metric_4_5_7_8_Data_QC'!H85
    value = 60.9911026684
    formula = "='Dashboard M4 Price Monthly'!K111"
    @eval_fn
    def H85():
        k111_1 = Dashboard_M4_Price_Monthly.K111()
        return k111_1

@register(Metric_4_5_7_8_Data_QC)
class I85():
    # 'Metric_4_5_7_8_Data_QC'!I85
    value = 63.693201838
    formula = "='Dashboard M4 Price Monthly'!O111"
    @eval_fn
    def I85():
        o111_1 = Dashboard_M4_Price_Monthly.O111()
        return o111_1

@register(Metric_4_5_7_8_Data_QC)
class J85():
    # 'Metric_4_5_7_8_Data_QC'!J85
    value = 63.0470597208
    formula = "='Dashboard M4 Price Monthly'!P111"
    @eval_fn
    def J85():
        p111_1 = Dashboard_M4_Price_Monthly.P111()
        return p111_1

@register(Metric_4_5_7_8_Data_QC)
class K85():
    # 'Metric_4_5_7_8_Data_QC'!K85
    value = 60.2293358445
    formula = "='Dashboard M4 Price Monthly'!Q111"
    @eval_fn
    def K85():
        q111_1 = Dashboard_M4_Price_Monthly.Q111()
        return q111_1

@register(Metric_4_5_7_8_Data_QC)
class L85():
    # 'Metric_4_5_7_8_Data_QC'!L85
    value = 58.655242225
    formula = "='Dashboard M4 Price Monthly'!R111"
    @eval_fn
    def L85():
        r111_1 = Dashboard_M4_Price_Monthly.R111()
        return r111_1

@register(Metric_4_5_7_8_Data_QC)
class M85():
    # 'Metric_4_5_7_8_Data_QC'!M85
    value = 56.2353821339
    formula = "='Dashboard M4 Price Monthly'!S111"
    @eval_fn
    def M85():
        s111_1 = Dashboard_M4_Price_Monthly.S111()
        return s111_1

@register(Metric_4_5_7_8_Data_QC)
class N85():
    # 'Metric_4_5_7_8_Data_QC'!N85
    value = 55.7087179784
    formula = "='Dashboard M4 Price Monthly'!T111"
    @eval_fn
    def N85():
        t111_1 = Dashboard_M4_Price_Monthly.T111()
        return t111_1

@register(Metric_4_5_7_8_Data_QC)
class O85():
    # 'Metric_4_5_7_8_Data_QC'!O85
    value = 57.6056065549
    formula = "='Dashboard M4 Price Monthly'!U111"
    @eval_fn
    def O85():
        u111_1 = Dashboard_M4_Price_Monthly.U111()
        return u111_1

@register(Metric_4_5_7_8_Data_QC)
class P85():
    # 'Metric_4_5_7_8_Data_QC'!P85
    value = 54.8850711401
    formula = "='Dashboard M4 Price Monthly'!V111"
    @eval_fn
    def P85():
        v111_1 = Dashboard_M4_Price_Monthly.V111()
        return v111_1

@register(Metric_4_5_7_8_Data_QC)
class Q85():
    # 'Metric_4_5_7_8_Data_QC'!Q85
    value = 57.6217484501
    formula = "='Dashboard M4 Price Monthly'!W111"
    @eval_fn
    def Q85():
        w111_1 = Dashboard_M4_Price_Monthly.W111()
        return w111_1

@register(Metric_4_5_7_8_Data_QC)
class R85():
    # 'Metric_4_5_7_8_Data_QC'!R85
    value = 59.1452564804
    formula = "='Dashboard M4 Price Monthly'!X111"
    @eval_fn
    def R85():
        x111_1 = Dashboard_M4_Price_Monthly.X111()
        return x111_1

@register(Metric_4_5_7_8_Data_QC)
class S85():
    # 'Metric_4_5_7_8_Data_QC'!S85
    value = 60.9862193057
    formula = "='Dashboard M4 Price Monthly'!Y111"
    @eval_fn
    def S85():
        y111_1 = Dashboard_M4_Price_Monthly.Y111()
        return y111_1

@register(Metric_4_5_7_8_Data_QC)
class T85():
    # 'Metric_4_5_7_8_Data_QC'!T85
    value = 63.6672217733
    formula = "='Dashboard M4 Price Monthly'!Z111"
    @eval_fn
    def T85():
        z111_1 = Dashboard_M4_Price_Monthly.Z111()
        return z111_1

@register(Metric_4_5_7_8_Data_QC)
class U85():
    # 'Metric_4_5_7_8_Data_QC'!U85
    value = 65.6474259698
    formula = "='Dashboard M4 Price Monthly'!AA111"
    @eval_fn
    def U85():
        aa111_1 = Dashboard_M4_Price_Monthly.AA111()
        return aa111_1

@register(Metric_4_5_7_8_Data_QC)
class V85():
    # 'Metric_4_5_7_8_Data_QC'!V85
    value = 61.1619064606
    formula = "='Dashboard M4 Price Monthly'!AB111"
    @eval_fn
    def V85():
        ab111_1 = Dashboard_M4_Price_Monthly.AB111()
        return ab111_1

@register(Metric_4_5_7_8_Data_QC)
class W85():
    # 'Metric_4_5_7_8_Data_QC'!W85
    value = 67.74183614
    formula = "='Dashboard M4 Price Monthly'!AC111"
    @eval_fn
    def W85():
        ac111_1 = Dashboard_M4_Price_Monthly.AC111()
        return ac111_1

@register(Metric_4_5_7_8_Data_QC)
class X85():
    # 'Metric_4_5_7_8_Data_QC'!X85
    value = 69.3830882541
    formula = "='Dashboard M4 Price Monthly'!AD111"
    @eval_fn
    def X85():
        ad111_1 = Dashboard_M4_Price_Monthly.AD111()
        return ad111_1

@register(Metric_4_5_7_8_Data_QC)
class Y85():
    # 'Metric_4_5_7_8_Data_QC'!Y85
    value = 73.8786782643
    formula = "='Dashboard M4 Price Monthly'!AE111"
    @eval_fn
    def Y85():
        ae111_1 = Dashboard_M4_Price_Monthly.AE111()
        return ae111_1

@register(Metric_4_5_7_8_Data_QC)
class Z85():
    # 'Metric_4_5_7_8_Data_QC'!Z85
    value = 74.3357133569
    formula = "='Dashboard M4 Price Monthly'!AF111"
    @eval_fn
    def Z85():
        af111_1 = Dashboard_M4_Price_Monthly.AF111()
        return af111_1

@register(Metric_4_5_7_8_Data_QC)
class AA85():
    # 'Metric_4_5_7_8_Data_QC'!AA85
    value = 78.5026309105
    formula = "='Dashboard M4 Price Monthly'!AG111"
    @eval_fn
    def AA85():
        ag111_1 = Dashboard_M4_Price_Monthly.AG111()
        return ag111_1

@register(Metric_4_5_7_8_Data_QC)
class AB85():
    # 'Metric_4_5_7_8_Data_QC'!AB85
    value = 78.8984762547
    formula = "='Dashboard M4 Price Monthly'!AH111"
    @eval_fn
    def AB85():
        ah111_1 = Dashboard_M4_Price_Monthly.AH111()
        return ah111_1

@register(Metric_4_5_7_8_Data_QC)
class AC85():
    # 'Metric_4_5_7_8_Data_QC'!AC85
    value = 79.0181584455
    formula = "='Dashboard M4 Price Monthly'!AI111"
    @eval_fn
    def AC85():
        ai111_1 = Dashboard_M4_Price_Monthly.AI111()
        return ai111_1

@register(Metric_4_5_7_8_Data_QC)
class AD85():
    # 'Metric_4_5_7_8_Data_QC'!AD85
    value = 82.0758612892
    formula = "='Dashboard M4 Price Monthly'!AJ111"
    @eval_fn
    def AD85():
        aj111_1 = Dashboard_M4_Price_Monthly.AJ111()
        return aj111_1

@register(Metric_4_5_7_8_Data_QC)
class AE85():
    # 'Metric_4_5_7_8_Data_QC'!AE85
    value = 87.8204345878
    formula = "='Dashboard M4 Price Monthly'!AK111"
    @eval_fn
    def AE85():
        ak111_1 = Dashboard_M4_Price_Monthly.AK111()
        return ak111_1

@register(Metric_4_5_7_8_Data_QC)
class AF85():
    # 'Metric_4_5_7_8_Data_QC'!AF85
    value = 92.4889735196
    formula = "='Dashboard M4 Price Monthly'!AL111"
    @eval_fn
    def AF85():
        al111_1 = Dashboard_M4_Price_Monthly.AL111()
        return al111_1

@register(Metric_4_5_7_8_Data_QC)
class AG85():
    # 'Metric_4_5_7_8_Data_QC'!AG85
    value = 95.6873957325
    formula = "='Dashboard M4 Price Monthly'!AM111"
    @eval_fn
    def AG85():
        am111_1 = Dashboard_M4_Price_Monthly.AM111()
        return am111_1

@register(Metric_4_5_7_8_Data_QC)
class AH85():
    # 'Metric_4_5_7_8_Data_QC'!AH85
    value = 97.6554459683
    formula = "='Dashboard M4 Price Monthly'!AN111"
    @eval_fn
    def AH85():
        an111_1 = Dashboard_M4_Price_Monthly.AN111()
        return an111_1

@register(Metric_4_5_7_8_Data_QC)
class AI85():
    # 'Metric_4_5_7_8_Data_QC'!AI85
    value = 94.6100859657
    formula = "='Dashboard M4 Price Monthly'!AO111"
    @eval_fn
    def AI85():
        ao111_1 = Dashboard_M4_Price_Monthly.AO111()
        return ao111_1

@register(Metric_4_5_7_8_Data_QC)
class AJ85():
    # 'Metric_4_5_7_8_Data_QC'!AJ85
    value = 87.7628992365
    formula = "='Dashboard M4 Price Monthly'!AP111"
    @eval_fn
    def AJ85():
        ap111_1 = Dashboard_M4_Price_Monthly.AP111()
        return ap111_1

@register(Metric_4_5_7_8_Data_QC)
class AK85():
    # 'Metric_4_5_7_8_Data_QC'!AK85
    value = 75.5506860191
    formula = "='Dashboard M4 Price Monthly'!AQ111"
    @eval_fn
    def AK85():
        aq111_1 = Dashboard_M4_Price_Monthly.AQ111()
        return aq111_1

@register(Metric_4_5_7_8_Data_QC)
class AL85():
    # 'Metric_4_5_7_8_Data_QC'!AL85
    value = 66.7073180333
    formula = "='Dashboard M4 Price Monthly'!AR111"
    @eval_fn
    def AL85():
        ar111_1 = Dashboard_M4_Price_Monthly.AR111()
        return ar111_1

@register(Metric_4_5_7_8_Data_QC)
class AM85():
    # 'Metric_4_5_7_8_Data_QC'!AM85
    value = 60.1897473971
    formula = "='Dashboard M4 Price Monthly'!AS111"
    @eval_fn
    def AM85():
        as111_1 = Dashboard_M4_Price_Monthly.AS111()
        return as111_1

@register(Metric_4_5_7_8_Data_QC)
class AN85():
    # 'Metric_4_5_7_8_Data_QC'!AN85
    value = 55.3306352022
    formula = "='Dashboard M4 Price Monthly'!AT111"
    @eval_fn
    def AN85():
        at111_1 = Dashboard_M4_Price_Monthly.AT111()
        return at111_1

@register(Metric_4_5_7_8_Data_QC)
class AO85():
    # 'Metric_4_5_7_8_Data_QC'!AO85
    value = 55.6034763563
    formula = "='Dashboard M4 Price Monthly'!AU111"
    @eval_fn
    def AO85():
        au111_1 = Dashboard_M4_Price_Monthly.AU111()
        return au111_1

@register(Metric_4_5_7_8_Data_QC)
class AP85():
    # 'Metric_4_5_7_8_Data_QC'!AP85
    value = 55.4754169774
    formula = "='Dashboard M4 Price Monthly'!AV111"
    @eval_fn
    def AP85():
        av111_1 = Dashboard_M4_Price_Monthly.AV111()
        return av111_1

@register(Metric_4_5_7_8_Data_QC)
class AQ85():
    # 'Metric_4_5_7_8_Data_QC'!AQ85
    value = 55.8356342098
    formula = "='Dashboard M4 Price Monthly'!AW111"
    @eval_fn
    def AQ85():
        aw111_1 = Dashboard_M4_Price_Monthly.AW111()
        return aw111_1

@register(Metric_4_5_7_8_Data_QC)
class AR85():
    # 'Metric_4_5_7_8_Data_QC'!AR85
    value = 58.7793260894
    formula = "='Dashboard M4 Price Monthly'!AX111"
    @eval_fn
    def AR85():
        ax111_1 = Dashboard_M4_Price_Monthly.AX111()
        return ax111_1

@register(Metric_4_5_7_8_Data_QC)
class AS85():
    # 'Metric_4_5_7_8_Data_QC'!AS85
    value = 65.0442739674
    formula = "='Dashboard M4 Price Monthly'!AY111"
    @eval_fn
    def AS85():
        ay111_1 = Dashboard_M4_Price_Monthly.AY111()
        return ay111_1

@register(Metric_4_5_7_8_Data_QC)
class AT85():
    # 'Metric_4_5_7_8_Data_QC'!AT85
    value = 66.1736565754
    formula = "='Dashboard M4 Price Monthly'!AZ111"
    @eval_fn
    def AT85():
        az111_1 = Dashboard_M4_Price_Monthly.AZ111()
        return az111_1

@register(Metric_4_5_7_8_Data_QC)
class AU85():
    # 'Metric_4_5_7_8_Data_QC'!AU85
    value = 69.0811501565
    formula = "='Dashboard M4 Price Monthly'!BA111"
    @eval_fn
    def AU85():
        ba111_1 = Dashboard_M4_Price_Monthly.BA111()
        return ba111_1

@register(Metric_4_5_7_8_Data_QC)
class AV85():
    # 'Metric_4_5_7_8_Data_QC'!AV85
    value = 68.1040141906
    formula = "='Dashboard M4 Price Monthly'!BB111"
    @eval_fn
    def AV85():
        bb111_1 = Dashboard_M4_Price_Monthly.BB111()
        return bb111_1

@register(Metric_4_5_7_8_Data_QC)
class AW85():
    # 'Metric_4_5_7_8_Data_QC'!AW85
    value = 68.2416287994
    formula = "='Dashboard M4 Price Monthly'!BC111"
    @eval_fn
    def AW85():
        bc111_1 = Dashboard_M4_Price_Monthly.BC111()
        return bc111_1

@register(Metric_4_5_7_8_Data_QC)
class AX85():
    # 'Metric_4_5_7_8_Data_QC'!AX85
    value = 69.6619220901
    formula = "='Dashboard M4 Price Monthly'!BD111"
    @eval_fn
    def AX85():
        bd111_1 = Dashboard_M4_Price_Monthly.BD111()
        return bd111_1

@register(Metric_4_5_7_8_Data_QC)
class AY85():
    # 'Metric_4_5_7_8_Data_QC'!AY85
    value = 72.0261986093
    formula = "='Dashboard M4 Price Monthly'!BE111"
    @eval_fn
    def AY85():
        be111_1 = Dashboard_M4_Price_Monthly.BE111()
        return be111_1

@register(Metric_4_5_7_8_Data_QC)
class AZ85():
    # 'Metric_4_5_7_8_Data_QC'!AZ85
    value = 73.5027566676
    formula = "='Dashboard M4 Price Monthly'!BF111"
    @eval_fn
    def AZ85():
        bf111_1 = Dashboard_M4_Price_Monthly.BF111()
        return bf111_1

@register(Metric_4_5_7_8_Data_QC)
class BA85():
    # 'Metric_4_5_7_8_Data_QC'!BA85
    value = 71.0133603052
    formula = "='Dashboard M4 Price Monthly'!BG111"
    @eval_fn
    def BA85():
        bg111_1 = Dashboard_M4_Price_Monthly.BG111()
        return bg111_1

@register(Metric_4_5_7_8_Data_QC)
class BB85():
    # 'Metric_4_5_7_8_Data_QC'!BB85
    value = 74.0029829857
    formula = "='Dashboard M4 Price Monthly'!BH111"
    @eval_fn
    def BB85():
        bh111_1 = Dashboard_M4_Price_Monthly.BH111()
        return bh111_1

@register(Metric_4_5_7_8_Data_QC)
class BC85():
    # 'Metric_4_5_7_8_Data_QC'!BC85
    value = 74.2219973259
    formula = "='Dashboard M4 Price Monthly'!BI111"
    @eval_fn
    def BC85():
        bi111_1 = Dashboard_M4_Price_Monthly.BI111()
        return bi111_1

@register(Metric_4_5_7_8_Data_QC)
class BD85():
    # 'Metric_4_5_7_8_Data_QC'!BD85
    value = 74.1391877036
    formula = "='Dashboard M4 Price Monthly'!BJ111"
    @eval_fn
    def BD85():
        bj111_1 = Dashboard_M4_Price_Monthly.BJ111()
        return bj111_1

@register(Metric_4_5_7_8_Data_QC)
class BE85():
    # 'Metric_4_5_7_8_Data_QC'!BE85
    value = 74.7740879074
    formula = "='Dashboard M4 Price Monthly'!BK111"
    @eval_fn
    def BE85():
        bk111_1 = Dashboard_M4_Price_Monthly.BK111()
        return bk111_1

@register(Metric_4_5_7_8_Data_QC)
class BF85():
    # 'Metric_4_5_7_8_Data_QC'!BF85
    value = 73.419950667
    formula = "='Dashboard M4 Price Monthly'!BL111"
    @eval_fn
    def BF85():
        bl111_1 = Dashboard_M4_Price_Monthly.BL111()
        return bl111_1

@register(Metric_4_5_7_8_Data_QC)
class BG85():
    # 'Metric_4_5_7_8_Data_QC'!BG85
    value = 74.4938851301
    formula = "='Dashboard M4 Price Monthly'!BM111"
    @eval_fn
    def BG85():
        bm111_1 = Dashboard_M4_Price_Monthly.BM111()
        return bm111_1

@register(Metric_4_5_7_8_Data_QC)
class BH85():
    # 'Metric_4_5_7_8_Data_QC'!BH85
    value = 75.6559494936
    formula = "='Dashboard M4 Price Monthly'!BN111"
    @eval_fn
    def BH85():
        bn111_1 = Dashboard_M4_Price_Monthly.BN111()
        return bn111_1

@register(Metric_4_5_7_8_Data_QC)
class BI85():
    # 'Metric_4_5_7_8_Data_QC'!BI85
    value = 76.2609137193
    formula = "='Dashboard M4 Price Monthly'!BO111"
    @eval_fn
    def BI85():
        bo111_1 = Dashboard_M4_Price_Monthly.BO111()
        return bo111_1

@register(Metric_4_5_7_8_Data_QC)
class BJ85():
    # 'Metric_4_5_7_8_Data_QC'!BJ85
    value = 79.677029886
    formula = "='Dashboard M4 Price Monthly'!BP111"
    @eval_fn
    def BJ85():
        bp111_1 = Dashboard_M4_Price_Monthly.BP111()
        return bp111_1

@register(Metric_4_5_7_8_Data_QC)
class BK85():
    # 'Metric_4_5_7_8_Data_QC'!BK85
    value = 81.6531783994
    formula = "='Dashboard M4 Price Monthly'!BQ111"
    @eval_fn
    def BK85():
        bq111_1 = Dashboard_M4_Price_Monthly.BQ111()
        return bq111_1

@register(Metric_4_5_7_8_Data_QC)
class BL85():
    # 'Metric_4_5_7_8_Data_QC'!BL85
    value = 83.5521828248
    formula = "='Dashboard M4 Price Monthly'!BR111"
    @eval_fn
    def BL85():
        br111_1 = Dashboard_M4_Price_Monthly.BR111()
        return br111_1

@register(Metric_4_5_7_8_Data_QC)
class BM85():
    # 'Metric_4_5_7_8_Data_QC'!BM85
    value = 87.1319681242
    formula = "='Dashboard M4 Price Monthly'!BS111"
    @eval_fn
    def BM85():
        bs111_1 = Dashboard_M4_Price_Monthly.BS111()
        return bs111_1

@register(Metric_4_5_7_8_Data_QC)
class BN85():
    # 'Metric_4_5_7_8_Data_QC'!BN85
    value = 91.7072640217
    formula = "='Dashboard M4 Price Monthly'!BT111"
    @eval_fn
    def BN85():
        bt111_1 = Dashboard_M4_Price_Monthly.BT111()
        return bt111_1

@register(Metric_4_5_7_8_Data_QC)
class BO85():
    # 'Metric_4_5_7_8_Data_QC'!BO85
    value = 96.3333526556
    formula = "='Dashboard M4 Price Monthly'!BU111"
    @eval_fn
    def BO85():
        bu111_1 = Dashboard_M4_Price_Monthly.BU111()
        return bu111_1

@register(Metric_4_5_7_8_Data_QC)
class BP85():
    # 'Metric_4_5_7_8_Data_QC'!BP85
    value = 96.8551159057
    formula = "='Dashboard M4 Price Monthly'!BV111"
    @eval_fn
    def BP85():
        bv111_1 = Dashboard_M4_Price_Monthly.BV111()
        return bv111_1

@register(Metric_4_5_7_8_Data_QC)
class BQ85():
    # 'Metric_4_5_7_8_Data_QC'!BQ85
    value = 99.381875397
    formula = "='Dashboard M4 Price Monthly'!BW111"
    @eval_fn
    def BQ85():
        bw111_1 = Dashboard_M4_Price_Monthly.BW111()
        return bw111_1

@register(Metric_4_5_7_8_Data_QC)
class BR85():
    # 'Metric_4_5_7_8_Data_QC'!BR85
    value = 100.606891374
    formula = "='Dashboard M4 Price Monthly'!BX111"
    @eval_fn
    def BR85():
        bx111_1 = Dashboard_M4_Price_Monthly.BX111()
        return bx111_1

@register(Metric_4_5_7_8_Data_QC)
class BS85():
    # 'Metric_4_5_7_8_Data_QC'!BS85
    value = 98.6857555448
    formula = "='Dashboard M4 Price Monthly'!BY111"
    @eval_fn
    def BS85():
        by111_1 = Dashboard_M4_Price_Monthly.BY111()
        return by111_1

@register(Metric_4_5_7_8_Data_QC)
class BT85():
    # 'Metric_4_5_7_8_Data_QC'!BT85
    value = 97.988122415
    formula = "='Dashboard M4 Price Monthly'!BZ111"
    @eval_fn
    def BT85():
        bz111_1 = Dashboard_M4_Price_Monthly.BZ111()
        return bz111_1

@register(Metric_4_5_7_8_Data_QC)
class BU85():
    # 'Metric_4_5_7_8_Data_QC'!BU85
    value = 96.6139768224
    formula = "='Dashboard M4 Price Monthly'!CA111"
    @eval_fn
    def BU85():
        ca111_1 = Dashboard_M4_Price_Monthly.CA111()
        return ca111_1

@register(Metric_4_5_7_8_Data_QC)
class BV85():
    # 'Metric_4_5_7_8_Data_QC'!BV85
    value = 97.0052337354
    formula = "='Dashboard M4 Price Monthly'!CB111"
    @eval_fn
    def BV85():
        cb111_1 = Dashboard_M4_Price_Monthly.CB111()
        return cb111_1

@register(Metric_4_5_7_8_Data_QC)
class BW85():
    # 'Metric_4_5_7_8_Data_QC'!BW85
    value = 98.5079759755
    formula = "='Dashboard M4 Price Monthly'!CC111"
    @eval_fn
    def BW85():
        cc111_1 = Dashboard_M4_Price_Monthly.CC111()
        return cc111_1

@register(Metric_4_5_7_8_Data_QC)
class BX85():
    # 'Metric_4_5_7_8_Data_QC'!BX85
    value = 99.5328528039
    formula = "='Dashboard M4 Price Monthly'!CD111"
    @eval_fn
    def BX85():
        cd111_1 = Dashboard_M4_Price_Monthly.CD111()
        return cd111_1

@register(Metric_4_5_7_8_Data_QC)
class BY85():
    # 'Metric_4_5_7_8_Data_QC'!BY85
    value = 100.873742414
    formula = "='Dashboard M4 Price Monthly'!CE111"
    @eval_fn
    def BY85():
        ce111_1 = Dashboard_M4_Price_Monthly.CE111()
        return ce111_1

@register(Metric_4_5_7_8_Data_QC)
class BZ85():
    # 'Metric_4_5_7_8_Data_QC'!BZ85
    value = 102.615251081
    formula = "='Dashboard M4 Price Monthly'!CF111"
    @eval_fn
    def BZ85():
        cf111_1 = Dashboard_M4_Price_Monthly.CF111()
        return cf111_1

@register(Metric_4_5_7_8_Data_QC)
class CA85():
    # 'Metric_4_5_7_8_Data_QC'!CA85
    value = 106.599945797
    formula = "='Dashboard M4 Price Monthly'!CG111"
    @eval_fn
    def CA85():
        cg111_1 = Dashboard_M4_Price_Monthly.CG111()
        return cg111_1

@register(Metric_4_5_7_8_Data_QC)
class CB85():
    # 'Metric_4_5_7_8_Data_QC'!CB85
    value = 101.432442555
    formula = "='Dashboard M4 Price Monthly'!CH111"
    @eval_fn
    def CB85():
        ch111_1 = Dashboard_M4_Price_Monthly.CH111()
        return ch111_1

@register(Metric_4_5_7_8_Data_QC)
class CC85():
    # 'Metric_4_5_7_8_Data_QC'!CC85
    value = 98.4516889802
    formula = "='Dashboard M4 Price Monthly'!CI111"
    @eval_fn
    def CC85():
        ci111_1 = Dashboard_M4_Price_Monthly.CI111()
        return ci111_1

@register(Metric_4_5_7_8_Data_QC)
class CD85():
    # 'Metric_4_5_7_8_Data_QC'!CD85
    value = 99.4606878657
    formula = "='Dashboard M4 Price Monthly'!CJ111"
    @eval_fn
    def CD85():
        cj111_1 = Dashboard_M4_Price_Monthly.CJ111()
        return cj111_1

@register(Metric_4_5_7_8_Data_QC)
class CE85():
    # 'Metric_4_5_7_8_Data_QC'!CE85
    value = 98.364133086
    formula = "='Dashboard M4 Price Monthly'!CK111"
    @eval_fn
    def CE85():
        ck111_1 = Dashboard_M4_Price_Monthly.CK111()
        return ck111_1

@register(Metric_4_5_7_8_Data_QC)
class B86():
    # 'Metric_4_5_7_8_Data_QC'!B86
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class E86():
    # 'Metric_4_5_7_8_Data_QC'!E86
    value = 23.0569019608
    formula = "='Dashboard M4 Price Monthly'!H112"
    @eval_fn
    def E86():
        h112_1 = Dashboard_M4_Price_Monthly.H112()
        return h112_1

@register(Metric_4_5_7_8_Data_QC)
class F86():
    # 'Metric_4_5_7_8_Data_QC'!F86
    value = 23.2794117647
    formula = "='Dashboard M4 Price Monthly'!I112"
    @eval_fn
    def F86():
        i112_1 = Dashboard_M4_Price_Monthly.I112()
        return i112_1

@register(Metric_4_5_7_8_Data_QC)
class G86():
    # 'Metric_4_5_7_8_Data_QC'!G86
    value = 23.070512334
    formula = "='Dashboard M4 Price Monthly'!J112"
    @eval_fn
    def G86():
        j112_1 = Dashboard_M4_Price_Monthly.J112()
        return j112_1

@register(Metric_4_5_7_8_Data_QC)
class H86():
    # 'Metric_4_5_7_8_Data_QC'!H86
    value = 25.6234077079
    formula = "='Dashboard M4 Price Monthly'!K112"
    @eval_fn
    def H86():
        k112_1 = Dashboard_M4_Price_Monthly.K112()
        return k112_1

@register(Metric_4_5_7_8_Data_QC)
class I86():
    # 'Metric_4_5_7_8_Data_QC'!I86
    value = 27.7104364326
    formula = "='Dashboard M4 Price Monthly'!O112"
    @eval_fn
    def I86():
        o112_1 = Dashboard_M4_Price_Monthly.O112()
        return o112_1

@register(Metric_4_5_7_8_Data_QC)
class J86():
    # 'Metric_4_5_7_8_Data_QC'!J86
    value = 26.6538039216
    formula = "='Dashboard M4 Price Monthly'!P112"
    @eval_fn
    def J86():
        p112_1 = Dashboard_M4_Price_Monthly.P112()
        return p112_1

@register(Metric_4_5_7_8_Data_QC)
class K86():
    # 'Metric_4_5_7_8_Data_QC'!K86
    value = 24.6367058824
    formula = "='Dashboard M4 Price Monthly'!Q112"
    @eval_fn
    def K86():
        q112_1 = Dashboard_M4_Price_Monthly.Q112()
        return q112_1

@register(Metric_4_5_7_8_Data_QC)
class L86():
    # 'Metric_4_5_7_8_Data_QC'!L86
    value = 23.5587058824
    formula = "='Dashboard M4 Price Monthly'!R112"
    @eval_fn
    def L86():
        r112_1 = Dashboard_M4_Price_Monthly.R112()
        return r112_1

@register(Metric_4_5_7_8_Data_QC)
class M86():
    # 'Metric_4_5_7_8_Data_QC'!M86
    value = 23.3098671727
    formula = "='Dashboard M4 Price Monthly'!S112"
    @eval_fn
    def M86():
        s112_1 = Dashboard_M4_Price_Monthly.S112()
        return s112_1

@register(Metric_4_5_7_8_Data_QC)
class N86():
    # 'Metric_4_5_7_8_Data_QC'!N86
    value = 23.9471726755
    formula = "='Dashboard M4 Price Monthly'!T112"
    @eval_fn
    def N86():
        t112_1 = Dashboard_M4_Price_Monthly.T112()
        return t112_1

@register(Metric_4_5_7_8_Data_QC)
class O86():
    # 'Metric_4_5_7_8_Data_QC'!O86
    value = 23.5864705882
    formula = "='Dashboard M4 Price Monthly'!U112"
    @eval_fn
    def O86():
        u112_1 = Dashboard_M4_Price_Monthly.U112()
        return u112_1

@register(Metric_4_5_7_8_Data_QC)
class P86():
    # 'Metric_4_5_7_8_Data_QC'!P86
    value = 24.1363187856
    formula = "='Dashboard M4 Price Monthly'!V112"
    @eval_fn
    def P86():
        v112_1 = Dashboard_M4_Price_Monthly.V112()
        return v112_1

@register(Metric_4_5_7_8_Data_QC)
class Q86():
    # 'Metric_4_5_7_8_Data_QC'!Q86
    value = 25.3603137255
    formula = "='Dashboard M4 Price Monthly'!W112"
    @eval_fn
    def Q86():
        w112_1 = Dashboard_M4_Price_Monthly.W112()
        return w112_1

@register(Metric_4_5_7_8_Data_QC)
class R86():
    # 'Metric_4_5_7_8_Data_QC'!R86
    value = 27.5789373814
    formula = "='Dashboard M4 Price Monthly'!X112"
    @eval_fn
    def R86():
        x112_1 = Dashboard_M4_Price_Monthly.X112()
        return x112_1

@register(Metric_4_5_7_8_Data_QC)
class S86():
    # 'Metric_4_5_7_8_Data_QC'!S86
    value = 28.099372549
    formula = "='Dashboard M4 Price Monthly'!Y112"
    @eval_fn
    def S86():
        y112_1 = Dashboard_M4_Price_Monthly.Y112()
        return y112_1

@register(Metric_4_5_7_8_Data_QC)
class T86():
    # 'Metric_4_5_7_8_Data_QC'!T86
    value = 27.0808349146
    formula = "='Dashboard M4 Price Monthly'!Z112"
    @eval_fn
    def T86():
        z112_1 = Dashboard_M4_Price_Monthly.Z112()
        return z112_1

@register(Metric_4_5_7_8_Data_QC)
class U86():
    # 'Metric_4_5_7_8_Data_QC'!U86
    value = 26.815711575
    formula = "='Dashboard M4 Price Monthly'!AA112"
    @eval_fn
    def U86():
        aa112_1 = Dashboard_M4_Price_Monthly.AA112()
        return aa112_1

@register(Metric_4_5_7_8_Data_QC)
class V86():
    # 'Metric_4_5_7_8_Data_QC'!V86
    value = 26.4943137255
    formula = "='Dashboard M4 Price Monthly'!AB112"
    @eval_fn
    def V86():
        ab112_1 = Dashboard_M4_Price_Monthly.AB112()
        return ab112_1

@register(Metric_4_5_7_8_Data_QC)
class W86():
    # 'Metric_4_5_7_8_Data_QC'!W86
    value = 26.3603529412
    formula = "='Dashboard M4 Price Monthly'!AC112"
    @eval_fn
    def W86():
        ac112_1 = Dashboard_M4_Price_Monthly.AC112()
        return ac112_1

@register(Metric_4_5_7_8_Data_QC)
class X86():
    # 'Metric_4_5_7_8_Data_QC'!X86
    value = 27.4084313725
    formula = "='Dashboard M4 Price Monthly'!AD112"
    @eval_fn
    def X86():
        ad112_1 = Dashboard_M4_Price_Monthly.AD112()
        return ad112_1

@register(Metric_4_5_7_8_Data_QC)
class Y86():
    # 'Metric_4_5_7_8_Data_QC'!Y86
    value = 28.4941176471
    formula = "='Dashboard M4 Price Monthly'!AE112"
    @eval_fn
    def Y86():
        ae112_1 = Dashboard_M4_Price_Monthly.AE112()
        return ae112_1

@register(Metric_4_5_7_8_Data_QC)
class Z86():
    # 'Metric_4_5_7_8_Data_QC'!Z86
    value = 28.6540417457
    formula = "='Dashboard M4 Price Monthly'!AF112"
    @eval_fn
    def Z86():
        af112_1 = Dashboard_M4_Price_Monthly.AF112()
        return af112_1

@register(Metric_4_5_7_8_Data_QC)
class AA86():
    # 'Metric_4_5_7_8_Data_QC'!AA86
    value = 28.7332352941
    formula = "='Dashboard M4 Price Monthly'!AG112"
    @eval_fn
    def AA86():
        ag112_1 = Dashboard_M4_Price_Monthly.AG112()
        return ag112_1

@register(Metric_4_5_7_8_Data_QC)
class AB86():
    # 'Metric_4_5_7_8_Data_QC'!AB86
    value = 29.7432258065
    formula = "='Dashboard M4 Price Monthly'!AH112"
    @eval_fn
    def AB86():
        ah112_1 = Dashboard_M4_Price_Monthly.AH112()
        return ah112_1

@register(Metric_4_5_7_8_Data_QC)
class AC86():
    # 'Metric_4_5_7_8_Data_QC'!AC86
    value = 30.7170791075
    formula = "='Dashboard M4 Price Monthly'!AI112"
    @eval_fn
    def AC86():
        ai112_1 = Dashboard_M4_Price_Monthly.AI112()
        return ai112_1

@register(Metric_4_5_7_8_Data_QC)
class AD86():
    # 'Metric_4_5_7_8_Data_QC'!AD86
    value = 32.5434914611
    formula = "='Dashboard M4 Price Monthly'!AJ112"
    @eval_fn
    def AD86():
        aj112_1 = Dashboard_M4_Price_Monthly.AJ112()
        return aj112_1

@register(Metric_4_5_7_8_Data_QC)
class AE86():
    # 'Metric_4_5_7_8_Data_QC'!AE86
    value = 35.3585098039
    formula = "='Dashboard M4 Price Monthly'!AK112"
    @eval_fn
    def AE86():
        ak112_1 = Dashboard_M4_Price_Monthly.AK112()
        return ak112_1

@register(Metric_4_5_7_8_Data_QC)
class AF86():
    # 'Metric_4_5_7_8_Data_QC'!AF86
    value = 36.8234535104
    formula = "='Dashboard M4 Price Monthly'!AL112"
    @eval_fn
    def AF86():
        al112_1 = Dashboard_M4_Price_Monthly.AL112()
        return al112_1

@register(Metric_4_5_7_8_Data_QC)
class AG86():
    # 'Metric_4_5_7_8_Data_QC'!AG86
    value = 36.4905882353
    formula = "='Dashboard M4 Price Monthly'!AM112"
    @eval_fn
    def AG86():
        am112_1 = Dashboard_M4_Price_Monthly.AM112()
        return am112_1

@register(Metric_4_5_7_8_Data_QC)
class AH86():
    # 'Metric_4_5_7_8_Data_QC'!AH86
    value = 35.4562352941
    formula = "='Dashboard M4 Price Monthly'!AN112"
    @eval_fn
    def AH86():
        an112_1 = Dashboard_M4_Price_Monthly.AN112()
        return an112_1

@register(Metric_4_5_7_8_Data_QC)
class AI86():
    # 'Metric_4_5_7_8_Data_QC'!AI86
    value = 31.815597723
    formula = "='Dashboard M4 Price Monthly'!AO112"
    @eval_fn
    def AI86():
        ao112_1 = Dashboard_M4_Price_Monthly.AO112()
        return ao112_1

@register(Metric_4_5_7_8_Data_QC)
class AJ86():
    # 'Metric_4_5_7_8_Data_QC'!AJ86
    value = 24.991372549
    formula = "='Dashboard M4 Price Monthly'!AP112"
    @eval_fn
    def AJ86():
        ap112_1 = Dashboard_M4_Price_Monthly.AP112()
        return ap112_1

@register(Metric_4_5_7_8_Data_QC)
class AK86():
    # 'Metric_4_5_7_8_Data_QC'!AK86
    value = 20.1942694497
    formula = "='Dashboard M4 Price Monthly'!AQ112"
    @eval_fn
    def AK86():
        aq112_1 = Dashboard_M4_Price_Monthly.AQ112()
        return aq112_1

@register(Metric_4_5_7_8_Data_QC)
class AL86():
    # 'Metric_4_5_7_8_Data_QC'!AL86
    value = 19.1388235294
    formula = "='Dashboard M4 Price Monthly'!AR112"
    @eval_fn
    def AL86():
        ar112_1 = Dashboard_M4_Price_Monthly.AR112()
        return ar112_1

@register(Metric_4_5_7_8_Data_QC)
class AM86():
    # 'Metric_4_5_7_8_Data_QC'!AM86
    value = 19.7770588235
    formula = "='Dashboard M4 Price Monthly'!AS112"
    @eval_fn
    def AM86():
        as112_1 = Dashboard_M4_Price_Monthly.AS112()
        return as112_1

@register(Metric_4_5_7_8_Data_QC)
class AN86():
    # 'Metric_4_5_7_8_Data_QC'!AN86
    value = 20.0978368121
    formula = "='Dashboard M4 Price Monthly'!AT112"
    @eval_fn
    def AN86():
        at112_1 = Dashboard_M4_Price_Monthly.AT112()
        return at112_1

@register(Metric_4_5_7_8_Data_QC)
class AO86():
    # 'Metric_4_5_7_8_Data_QC'!AO86
    value = 20.2363137255
    formula = "='Dashboard M4 Price Monthly'!AU112"
    @eval_fn
    def AO86():
        au112_1 = Dashboard_M4_Price_Monthly.AU112()
        return au112_1

@register(Metric_4_5_7_8_Data_QC)
class AP86():
    # 'Metric_4_5_7_8_Data_QC'!AP86
    value = 21.5188235294
    formula = "='Dashboard M4 Price Monthly'!AV112"
    @eval_fn
    def AP86():
        av112_1 = Dashboard_M4_Price_Monthly.AV112()
        return av112_1

@register(Metric_4_5_7_8_Data_QC)
class AQ86():
    # 'Metric_4_5_7_8_Data_QC'!AQ86
    value = 24.6583921569
    formula = "='Dashboard M4 Price Monthly'!AW112"
    @eval_fn
    def AQ86():
        aw112_1 = Dashboard_M4_Price_Monthly.AW112()
        return aw112_1

@register(Metric_4_5_7_8_Data_QC)
class AR86():
    # 'Metric_4_5_7_8_Data_QC'!AR86
    value = 26.4517647059
    formula = "='Dashboard M4 Price Monthly'!AX112"
    @eval_fn
    def AR86():
        ax112_1 = Dashboard_M4_Price_Monthly.AX112()
        return ax112_1

@register(Metric_4_5_7_8_Data_QC)
class AS86():
    # 'Metric_4_5_7_8_Data_QC'!AS86
    value = 26.6329411765
    formula = "='Dashboard M4 Price Monthly'!AY112"
    @eval_fn
    def AS86():
        ay112_1 = Dashboard_M4_Price_Monthly.AY112()
        return ay112_1

@register(Metric_4_5_7_8_Data_QC)
class AT86():
    # 'Metric_4_5_7_8_Data_QC'!AT86
    value = 27.58
    formula = "='Dashboard M4 Price Monthly'!AZ112"
    @eval_fn
    def AT86():
        az112_1 = Dashboard_M4_Price_Monthly.AZ112()
        return az112_1

@register(Metric_4_5_7_8_Data_QC)
class AU86():
    # 'Metric_4_5_7_8_Data_QC'!AU86
    value = 26.8635294118
    formula = "='Dashboard M4 Price Monthly'!BA112"
    @eval_fn
    def AU86():
        ba112_1 = Dashboard_M4_Price_Monthly.BA112()
        return ba112_1

@register(Metric_4_5_7_8_Data_QC)
class AV86():
    # 'Metric_4_5_7_8_Data_QC'!AV86
    value = 27.4482352941
    formula = "='Dashboard M4 Price Monthly'!BB112"
    @eval_fn
    def AV86():
        bb112_1 = Dashboard_M4_Price_Monthly.BB112()
        return bb112_1

@register(Metric_4_5_7_8_Data_QC)
class AW86():
    # 'Metric_4_5_7_8_Data_QC'!AW86
    value = 27.4482352941
    formula = "='Dashboard M4 Price Monthly'!BC112"
    @eval_fn
    def AW86():
        bc112_1 = Dashboard_M4_Price_Monthly.BC112()
        return bc112_1

@register(Metric_4_5_7_8_Data_QC)
class AX86():
    # 'Metric_4_5_7_8_Data_QC'!AX86
    value = 27.8517647059
    formula = "='Dashboard M4 Price Monthly'!BD112"
    @eval_fn
    def AX86():
        bd112_1 = Dashboard_M4_Price_Monthly.BD112()
        return bd112_1

@register(Metric_4_5_7_8_Data_QC)
class AY86():
    # 'Metric_4_5_7_8_Data_QC'!AY86
    value = 28.2388235294
    formula = "='Dashboard M4 Price Monthly'!BE112"
    @eval_fn
    def AY86():
        be112_1 = Dashboard_M4_Price_Monthly.BE112()
        return be112_1

@register(Metric_4_5_7_8_Data_QC)
class AZ86():
    # 'Metric_4_5_7_8_Data_QC'!AZ86
    value = 28.5517647059
    formula = "='Dashboard M4 Price Monthly'!BF112"
    @eval_fn
    def AZ86():
        bf112_1 = Dashboard_M4_Price_Monthly.BF112()
        return bf112_1

@register(Metric_4_5_7_8_Data_QC)
class BA86():
    # 'Metric_4_5_7_8_Data_QC'!BA86
    value = 29.1858823529
    formula = "='Dashboard M4 Price Monthly'!BG112"
    @eval_fn
    def BA86():
        bg112_1 = Dashboard_M4_Price_Monthly.BG112()
        return bg112_1

@register(Metric_4_5_7_8_Data_QC)
class BB86():
    # 'Metric_4_5_7_8_Data_QC'!BB86
    value = 29.3415559772
    formula = "='Dashboard M4 Price Monthly'!BH112"
    @eval_fn
    def BB86():
        bh112_1 = Dashboard_M4_Price_Monthly.BH112()
        return bh112_1

@register(Metric_4_5_7_8_Data_QC)
class BC86():
    # 'Metric_4_5_7_8_Data_QC'!BC86
    value = 28.6176470588
    formula = "='Dashboard M4 Price Monthly'!BI112"
    @eval_fn
    def BC86():
        bi112_1 = Dashboard_M4_Price_Monthly.BI112()
        return bi112_1

@register(Metric_4_5_7_8_Data_QC)
class BD86():
    # 'Metric_4_5_7_8_Data_QC'!BD86
    value = 28.5023529412
    formula = "='Dashboard M4 Price Monthly'!BJ112"
    @eval_fn
    def BD86():
        bj112_1 = Dashboard_M4_Price_Monthly.BJ112()
        return bj112_1

@register(Metric_4_5_7_8_Data_QC)
class BE86():
    # 'Metric_4_5_7_8_Data_QC'!BE86
    value = 28.7082352941
    formula = "='Dashboard M4 Price Monthly'!BK112"
    @eval_fn
    def BE86():
        bk112_1 = Dashboard_M4_Price_Monthly.BK112()
        return bk112_1

@register(Metric_4_5_7_8_Data_QC)
class BF86():
    # 'Metric_4_5_7_8_Data_QC'!BF86
    value = 28.3952941176
    formula = "='Dashboard M4 Price Monthly'!BL112"
    @eval_fn
    def BF86():
        bl112_1 = Dashboard_M4_Price_Monthly.BL112()
        return bl112_1

@register(Metric_4_5_7_8_Data_QC)
class BG86():
    # 'Metric_4_5_7_8_Data_QC'!BG86
    value = 28.6670588235
    formula = "='Dashboard M4 Price Monthly'!BM112"
    @eval_fn
    def BG86():
        bm112_1 = Dashboard_M4_Price_Monthly.BM112()
        return bm112_1

@register(Metric_4_5_7_8_Data_QC)
class BH86():
    # 'Metric_4_5_7_8_Data_QC'!BH86
    value = 28.98
    formula = "='Dashboard M4 Price Monthly'!BN112"
    @eval_fn
    def BH86():
        bn112_1 = Dashboard_M4_Price_Monthly.BN112()
        return bn112_1

@register(Metric_4_5_7_8_Data_QC)
class BI86():
    # 'Metric_4_5_7_8_Data_QC'!BI86
    value = 29.5976470588
    formula = "='Dashboard M4 Price Monthly'!BO112"
    @eval_fn
    def BI86():
        bo112_1 = Dashboard_M4_Price_Monthly.BO112()
        return bo112_1

@register(Metric_4_5_7_8_Data_QC)
class BJ86():
    # 'Metric_4_5_7_8_Data_QC'!BJ86
    value = 30.4211764706
    formula = "='Dashboard M4 Price Monthly'!BP112"
    @eval_fn
    def BJ86():
        bp112_1 = Dashboard_M4_Price_Monthly.BP112()
        return bp112_1

@register(Metric_4_5_7_8_Data_QC)
class BK86():
    # 'Metric_4_5_7_8_Data_QC'!BK86
    value = 30.8494117647
    formula = "='Dashboard M4 Price Monthly'!BQ112"
    @eval_fn
    def BK86():
        bq112_1 = Dashboard_M4_Price_Monthly.BQ112()
        return bq112_1

@register(Metric_4_5_7_8_Data_QC)
class BL86():
    # 'Metric_4_5_7_8_Data_QC'!BL86
    value = 33.3282352941
    formula = "='Dashboard M4 Price Monthly'!BR112"
    @eval_fn
    def BL86():
        br112_1 = Dashboard_M4_Price_Monthly.BR112()
        return br112_1

@register(Metric_4_5_7_8_Data_QC)
class BM86():
    # 'Metric_4_5_7_8_Data_QC'!BM86
    value = 36.7376470588
    formula = "='Dashboard M4 Price Monthly'!BS112"
    @eval_fn
    def BM86():
        bs112_1 = Dashboard_M4_Price_Monthly.BS112()
        return bs112_1

@register(Metric_4_5_7_8_Data_QC)
class BN86():
    # 'Metric_4_5_7_8_Data_QC'!BN86
    value = 36.0458823529
    formula = "='Dashboard M4 Price Monthly'!BT112"
    @eval_fn
    def BN86():
        bt112_1 = Dashboard_M4_Price_Monthly.BT112()
        return bt112_1

@register(Metric_4_5_7_8_Data_QC)
class BO86():
    # 'Metric_4_5_7_8_Data_QC'!BO86
    value = 33.3282352941
    formula = "='Dashboard M4 Price Monthly'!BU112"
    @eval_fn
    def BO86():
        bu112_1 = Dashboard_M4_Price_Monthly.BU112()
        return bu112_1

@register(Metric_4_5_7_8_Data_QC)
class BP86():
    # 'Metric_4_5_7_8_Data_QC'!BP86
    value = 33.46
    formula = "='Dashboard M4 Price Monthly'!BV112"
    @eval_fn
    def BP86():
        bv112_1 = Dashboard_M4_Price_Monthly.BV112()
        return bv112_1

@register(Metric_4_5_7_8_Data_QC)
class BQ86():
    # 'Metric_4_5_7_8_Data_QC'!BQ86
    value = 33.8964705882
    formula = "='Dashboard M4 Price Monthly'!BW112"
    @eval_fn
    def BQ86():
        bw112_1 = Dashboard_M4_Price_Monthly.BW112()
        return bw112_1

@register(Metric_4_5_7_8_Data_QC)
class BR86():
    # 'Metric_4_5_7_8_Data_QC'!BR86
    value = 34.5058823529
    formula = "='Dashboard M4 Price Monthly'!BX112"
    @eval_fn
    def BR86():
        bx112_1 = Dashboard_M4_Price_Monthly.BX112()
        return bx112_1

@register(Metric_4_5_7_8_Data_QC)
class BS86():
    # 'Metric_4_5_7_8_Data_QC'!BS86
    value = 34.6870588235
    formula = "='Dashboard M4 Price Monthly'!BY112"
    @eval_fn
    def BS86():
        by112_1 = Dashboard_M4_Price_Monthly.BY112()
        return by112_1

@register(Metric_4_5_7_8_Data_QC)
class BT86():
    # 'Metric_4_5_7_8_Data_QC'!BT86
    value = 34.1682352941
    formula = "='Dashboard M4 Price Monthly'!BZ112"
    @eval_fn
    def BT86():
        bz112_1 = Dashboard_M4_Price_Monthly.BZ112()
        return bz112_1

@register(Metric_4_5_7_8_Data_QC)
class BU86():
    # 'Metric_4_5_7_8_Data_QC'!BU86
    value = 33.3364705882
    formula = "='Dashboard M4 Price Monthly'!CA112"
    @eval_fn
    def BU86():
        ca112_1 = Dashboard_M4_Price_Monthly.CA112()
        return ca112_1

@register(Metric_4_5_7_8_Data_QC)
class BV86():
    # 'Metric_4_5_7_8_Data_QC'!BV86
    value = 33.4475142315
    formula = "='Dashboard M4 Price Monthly'!CB112"
    @eval_fn
    def BV86():
        cb112_1 = Dashboard_M4_Price_Monthly.CB112()
        return cb112_1

@register(Metric_4_5_7_8_Data_QC)
class BW86():
    # 'Metric_4_5_7_8_Data_QC'!BW86
    value = 34.8003651116
    formula = "='Dashboard M4 Price Monthly'!CC112"
    @eval_fn
    def BW86():
        cc112_1 = Dashboard_M4_Price_Monthly.CC112()
        return cc112_1

@register(Metric_4_5_7_8_Data_QC)
class BX86():
    # 'Metric_4_5_7_8_Data_QC'!BX86
    value = 36.8415180266
    formula = "='Dashboard M4 Price Monthly'!CD112"
    @eval_fn
    def BX86():
        cd112_1 = Dashboard_M4_Price_Monthly.CD112()
        return cd112_1

@register(Metric_4_5_7_8_Data_QC)
class BY86():
    # 'Metric_4_5_7_8_Data_QC'!BY86
    value = 37.9389019608
    formula = "='Dashboard M4 Price Monthly'!CE112"
    @eval_fn
    def BY86():
        ce112_1 = Dashboard_M4_Price_Monthly.CE112()
        return ce112_1

@register(Metric_4_5_7_8_Data_QC)
class BZ86():
    # 'Metric_4_5_7_8_Data_QC'!BZ86
    value = 37.4432258065
    formula = "='Dashboard M4 Price Monthly'!CF112"
    @eval_fn
    def BZ86():
        cf112_1 = Dashboard_M4_Price_Monthly.CF112()
        return cf112_1

@register(Metric_4_5_7_8_Data_QC)
class CA86():
    # 'Metric_4_5_7_8_Data_QC'!CA86
    value = 36.3050196078
    formula = "='Dashboard M4 Price Monthly'!CG112"
    @eval_fn
    def CA86():
        cg112_1 = Dashboard_M4_Price_Monthly.CG112()
        return cg112_1

@register(Metric_4_5_7_8_Data_QC)
class CB86():
    # 'Metric_4_5_7_8_Data_QC'!CB86
    value = 34.5420113852
    formula = "='Dashboard M4 Price Monthly'!CH112"
    @eval_fn
    def CB86():
        ch112_1 = Dashboard_M4_Price_Monthly.CH112()
        return ch112_1

@register(Metric_4_5_7_8_Data_QC)
class CC86():
    # 'Metric_4_5_7_8_Data_QC'!CC86
    value = 34.6982163188
    formula = "='Dashboard M4 Price Monthly'!CI112"
    @eval_fn
    def CC86():
        ci112_1 = Dashboard_M4_Price_Monthly.CI112()
        return ci112_1

@register(Metric_4_5_7_8_Data_QC)
class CD86():
    # 'Metric_4_5_7_8_Data_QC'!CD86
    value = 36.1803921569
    formula = "='Dashboard M4 Price Monthly'!CJ112"
    @eval_fn
    def CD86():
        cj112_1 = Dashboard_M4_Price_Monthly.CJ112()
        return cj112_1

@register(Metric_4_5_7_8_Data_QC)
class CE86():
    # 'Metric_4_5_7_8_Data_QC'!CE86
    value = 36.3033017078
    formula = "='Dashboard M4 Price Monthly'!CK112"
    @eval_fn
    def CE86():
        ck112_1 = Dashboard_M4_Price_Monthly.CK112()
        return ck112_1

@register(Metric_4_5_7_8_Data_QC)
class B87():
    # 'Metric_4_5_7_8_Data_QC'!B87
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class E87():
    # 'Metric_4_5_7_8_Data_QC'!E87
    value = 15.7904127403
    formula = "='Dashboard M4 Price Monthly'!H113"
    @eval_fn
    def E87():
        h113_1 = Dashboard_M4_Price_Monthly.H113()
        return h113_1

@register(Metric_4_5_7_8_Data_QC)
class F87():
    # 'Metric_4_5_7_8_Data_QC'!F87
    value = 15.2513127459
    formula = "='Dashboard M4 Price Monthly'!I113"
    @eval_fn
    def F87():
        i113_1 = Dashboard_M4_Price_Monthly.I113()
        return i113_1

@register(Metric_4_5_7_8_Data_QC)
class G87():
    # 'Metric_4_5_7_8_Data_QC'!G87
    value = 16.3034272511
    formula = "='Dashboard M4 Price Monthly'!J113"
    @eval_fn
    def G87():
        j113_1 = Dashboard_M4_Price_Monthly.J113()
        return j113_1

@register(Metric_4_5_7_8_Data_QC)
class H87():
    # 'Metric_4_5_7_8_Data_QC'!H87
    value = 18.0337643301
    formula = "='Dashboard M4 Price Monthly'!K113"
    @eval_fn
    def H87():
        k113_1 = Dashboard_M4_Price_Monthly.K113()
        return k113_1

@register(Metric_4_5_7_8_Data_QC)
class I87():
    # 'Metric_4_5_7_8_Data_QC'!I87
    value = 18.5467788409
    formula = "='Dashboard M4 Price Monthly'!O113"
    @eval_fn
    def I87():
        o113_1 = Dashboard_M4_Price_Monthly.O113()
        return o113_1

@register(Metric_4_5_7_8_Data_QC)
class J87():
    # 'Metric_4_5_7_8_Data_QC'!J87
    value = 15.7382417731
    formula = "='Dashboard M4 Price Monthly'!P113"
    @eval_fn
    def J87():
        p113_1 = Dashboard_M4_Price_Monthly.P113()
        return p113_1

@register(Metric_4_5_7_8_Data_QC)
class K87():
    # 'Metric_4_5_7_8_Data_QC'!K87
    value = 15.1208853278
    formula = "='Dashboard M4 Price Monthly'!Q113"
    @eval_fn
    def K87():
        q113_1 = Dashboard_M4_Price_Monthly.Q113()
        return q113_1

@register(Metric_4_5_7_8_Data_QC)
class L87():
    # 'Metric_4_5_7_8_Data_QC'!L87
    value = 15.0687143606
    formula = "='Dashboard M4 Price Monthly'!R113"
    @eval_fn
    def L87():
        r113_1 = Dashboard_M4_Price_Monthly.R113()
        return r113_1

@register(Metric_4_5_7_8_Data_QC)
class M87():
    # 'Metric_4_5_7_8_Data_QC'!M87
    value = 15.7382417731
    formula = "='Dashboard M4 Price Monthly'!S113"
    @eval_fn
    def M87():
        s113_1 = Dashboard_M4_Price_Monthly.S113()
        return s113_1

@register(Metric_4_5_7_8_Data_QC)
class N87():
    # 'Metric_4_5_7_8_Data_QC'!N87
    value = 14.3817966258
    formula = "='Dashboard M4 Price Monthly'!T113"
    @eval_fn
    def N87():
        t113_1 = Dashboard_M4_Price_Monthly.T113()
        return t113_1

@register(Metric_4_5_7_8_Data_QC)
class O87():
    # 'Metric_4_5_7_8_Data_QC'!O87
    value = 15.129580489
    formula = "='Dashboard M4 Price Monthly'!U113"
    @eval_fn
    def O87():
        u113_1 = Dashboard_M4_Price_Monthly.U113()
        return u113_1

@register(Metric_4_5_7_8_Data_QC)
class P87():
    # 'Metric_4_5_7_8_Data_QC'!P87
    value = 16.0512675763
    formula = "='Dashboard M4 Price Monthly'!V113"
    @eval_fn
    def P87():
        v113_1 = Dashboard_M4_Price_Monthly.V113()
        return v113_1

@register(Metric_4_5_7_8_Data_QC)
class Q87():
    # 'Metric_4_5_7_8_Data_QC'!Q87
    value = 17.7033482044
    formula = "='Dashboard M4 Price Monthly'!W113"
    @eval_fn
    def Q87():
        w113_1 = Dashboard_M4_Price_Monthly.W113()
        return w113_1

@register(Metric_4_5_7_8_Data_QC)
class R87():
    # 'Metric_4_5_7_8_Data_QC'!R87
    value = 17.772909494
    formula = "='Dashboard M4 Price Monthly'!X113"
    @eval_fn
    def R87():
        x113_1 = Dashboard_M4_Price_Monthly.X113()
        return x113_1

@register(Metric_4_5_7_8_Data_QC)
class S87():
    # 'Metric_4_5_7_8_Data_QC'!S87
    value = 18.2511433601
    formula = "='Dashboard M4 Price Monthly'!Y113"
    @eval_fn
    def S87():
        y113_1 = Dashboard_M4_Price_Monthly.Y113()
        return y113_1

@register(Metric_4_5_7_8_Data_QC)
class T87():
    # 'Metric_4_5_7_8_Data_QC'!T87
    value = 18.5815594857
    formula = "='Dashboard M4 Price Monthly'!Z113"
    @eval_fn
    def T87():
        z113_1 = Dashboard_M4_Price_Monthly.Z113()
        return z113_1

@register(Metric_4_5_7_8_Data_QC)
class U87():
    # 'Metric_4_5_7_8_Data_QC'!U87
    value = 18.1902772317
    formula = "='Dashboard M4 Price Monthly'!AA113"
    @eval_fn
    def U87():
        aa113_1 = Dashboard_M4_Price_Monthly.AA113()
        return aa113_1

@register(Metric_4_5_7_8_Data_QC)
class V87():
    # 'Metric_4_5_7_8_Data_QC'!V87
    value = 19.6945401194
    formula = "='Dashboard M4 Price Monthly'!AB113"
    @eval_fn
    def V87():
        ab113_1 = Dashboard_M4_Price_Monthly.AB113()
        return ab113_1

@register(Metric_4_5_7_8_Data_QC)
class W87():
    # 'Metric_4_5_7_8_Data_QC'!W87
    value = 20.6249223678
    formula = "='Dashboard M4 Price Monthly'!AC113"
    @eval_fn
    def W87():
        ac113_1 = Dashboard_M4_Price_Monthly.AC113()
        return ac113_1

@register(Metric_4_5_7_8_Data_QC)
class X87():
    # 'Metric_4_5_7_8_Data_QC'!X87
    value = 23.2421658892
    formula = "='Dashboard M4 Price Monthly'!AD113"
    @eval_fn
    def X87():
        ad113_1 = Dashboard_M4_Price_Monthly.AD113()
        return ad113_1

@register(Metric_4_5_7_8_Data_QC)
class Y87():
    # 'Metric_4_5_7_8_Data_QC'!Y87
    value = 22.6161142828
    formula = "='Dashboard M4 Price Monthly'!AE113"
    @eval_fn
    def Y87():
        ae113_1 = Dashboard_M4_Price_Monthly.AE113()
        return ae113_1

@register(Metric_4_5_7_8_Data_QC)
class Z87():
    # 'Metric_4_5_7_8_Data_QC'!Z87
    value = 22.6508949276
    formula = "='Dashboard M4 Price Monthly'!AF113"
    @eval_fn
    def Z87():
        af113_1 = Dashboard_M4_Price_Monthly.AF113()
        return af113_1

@register(Metric_4_5_7_8_Data_QC)
class AA87():
    # 'Metric_4_5_7_8_Data_QC'!AA87
    value = 23.7203997552
    formula = "='Dashboard M4 Price Monthly'!AG113"
    @eval_fn
    def AA87():
        ag113_1 = Dashboard_M4_Price_Monthly.AG113()
        return ag113_1

@register(Metric_4_5_7_8_Data_QC)
class AB87():
    # 'Metric_4_5_7_8_Data_QC'!AB87
    value = 27.1636835907
    formula = "='Dashboard M4 Price Monthly'!AH113"
    @eval_fn
    def AB87():
        ah113_1 = Dashboard_M4_Price_Monthly.AH113()
        return ah113_1

@register(Metric_4_5_7_8_Data_QC)
class AC87():
    # 'Metric_4_5_7_8_Data_QC'!AC87
    value = 29.25921744
    formula = "='Dashboard M4 Price Monthly'!AI113"
    @eval_fn
    def AC87():
        ai113_1 = Dashboard_M4_Price_Monthly.AI113()
        return ai113_1

@register(Metric_4_5_7_8_Data_QC)
class AD87():
    # 'Metric_4_5_7_8_Data_QC'!AD87
    value = 32.5025125679
    formula = "='Dashboard M4 Price Monthly'!AJ113"
    @eval_fn
    def AD87():
        aj113_1 = Dashboard_M4_Price_Monthly.AJ113()
        return aj113_1

@register(Metric_4_5_7_8_Data_QC)
class AE87():
    # 'Metric_4_5_7_8_Data_QC'!AE87
    value = 33.7198351359
    formula = "='Dashboard M4 Price Monthly'!AK113"
    @eval_fn
    def AE87():
        ak113_1 = Dashboard_M4_Price_Monthly.AK113()
        return ak113_1

@register(Metric_4_5_7_8_Data_QC)
class AF87():
    # 'Metric_4_5_7_8_Data_QC'!AF87
    value = 33.7893964255
    formula = "='Dashboard M4 Price Monthly'!AL113"
    @eval_fn
    def AF87():
        al113_1 = Dashboard_M4_Price_Monthly.AL113()
        return al113_1

@register(Metric_4_5_7_8_Data_QC)
class AG87():
    # 'Metric_4_5_7_8_Data_QC'!AG87
    value = 28.4418722872
    formula = "='Dashboard M4 Price Monthly'!AM113"
    @eval_fn
    def AG87():
        am113_1 = Dashboard_M4_Price_Monthly.AM113()
        return am113_1

@register(Metric_4_5_7_8_Data_QC)
class AH87():
    # 'Metric_4_5_7_8_Data_QC'!AH87
    value = 29.346169052
    formula = "='Dashboard M4 Price Monthly'!AN113"
    @eval_fn
    def AH87():
        an113_1 = Dashboard_M4_Price_Monthly.AN113()
        return an113_1

@register(Metric_4_5_7_8_Data_QC)
class AI87():
    # 'Metric_4_5_7_8_Data_QC'!AI87
    value = 20.1292981794
    formula = "='Dashboard M4 Price Monthly'!AO113"
    @eval_fn
    def AI87():
        ao113_1 = Dashboard_M4_Price_Monthly.AO113()
        return ao113_1

@register(Metric_4_5_7_8_Data_QC)
class AJ87():
    # 'Metric_4_5_7_8_Data_QC'!AJ87
    value = 16.3469030571
    formula = "='Dashboard M4 Price Monthly'!AP113"
    @eval_fn
    def AJ87():
        ap113_1 = Dashboard_M4_Price_Monthly.AP113()
        return ap113_1

@register(Metric_4_5_7_8_Data_QC)
class AK87():
    # 'Metric_4_5_7_8_Data_QC'!AK87
    value = 11.9558466508
    formula = "='Dashboard M4 Price Monthly'!AQ113"
    @eval_fn
    def AK87():
        aq113_1 = Dashboard_M4_Price_Monthly.AQ113()
        return aq113_1

@register(Metric_4_5_7_8_Data_QC)
class AL87():
    # 'Metric_4_5_7_8_Data_QC'!AL87
    value = 12.7731918037
    formula = "='Dashboard M4 Price Monthly'!AR113"
    @eval_fn
    def AL87():
        ar113_1 = Dashboard_M4_Price_Monthly.AR113()
        return ar113_1

@register(Metric_4_5_7_8_Data_QC)
class AM87():
    # 'Metric_4_5_7_8_Data_QC'!AM87
    value = 10.9472079516
    formula = "='Dashboard M4 Price Monthly'!AS113"
    @eval_fn
    def AM87():
        as113_1 = Dashboard_M4_Price_Monthly.AS113()
        return as113_1

@register(Metric_4_5_7_8_Data_QC)
class AN87():
    # 'Metric_4_5_7_8_Data_QC'!AN87
    value = 11.0254644024
    formula = "='Dashboard M4 Price Monthly'!AT113"
    @eval_fn
    def AN87():
        at113_1 = Dashboard_M4_Price_Monthly.AT113()
        return at113_1

@register(Metric_4_5_7_8_Data_QC)
class AO87():
    # 'Metric_4_5_7_8_Data_QC'!AO87
    value = 11.9036756836
    formula = "='Dashboard M4 Price Monthly'!AU113"
    @eval_fn
    def AO87():
        au113_1 = Dashboard_M4_Price_Monthly.AU113()
        return au113_1

@register(Metric_4_5_7_8_Data_QC)
class AP87():
    # 'Metric_4_5_7_8_Data_QC'!AP87
    value = 12.9383998665
    formula = "='Dashboard M4 Price Monthly'!AV113"
    @eval_fn
    def AP87():
        av113_1 = Dashboard_M4_Price_Monthly.AV113()
        return av113_1

@register(Metric_4_5_7_8_Data_QC)
class AQ87():
    # 'Metric_4_5_7_8_Data_QC'!AQ87
    value = 15.6947659671
    formula = "='Dashboard M4 Price Monthly'!AW113"
    @eval_fn
    def AQ87():
        aw113_1 = Dashboard_M4_Price_Monthly.AW113()
        return aw113_1

@register(Metric_4_5_7_8_Data_QC)
class AR87():
    # 'Metric_4_5_7_8_Data_QC'!AR87
    value = 14.8861159754
    formula = "='Dashboard M4 Price Monthly'!AX113"
    @eval_fn
    def AR87():
        ax113_1 = Dashboard_M4_Price_Monthly.AX113()
        return ax113_1

@register(Metric_4_5_7_8_Data_QC)
class AS87():
    # 'Metric_4_5_7_8_Data_QC'!AS87
    value = 16.3903788631
    formula = "='Dashboard M4 Price Monthly'!AY113"
    @eval_fn
    def AS87():
        ay113_1 = Dashboard_M4_Price_Monthly.AY113()
        return ay113_1

@register(Metric_4_5_7_8_Data_QC)
class AT87():
    # 'Metric_4_5_7_8_Data_QC'!AT87
    value = 15.2078369399
    formula = "='Dashboard M4 Price Monthly'!AZ113"
    @eval_fn
    def AT87():
        az113_1 = Dashboard_M4_Price_Monthly.AZ113()
        return az113_1

@register(Metric_4_5_7_8_Data_QC)
class AU87():
    # 'Metric_4_5_7_8_Data_QC'!AU87
    value = 16.8860030516
    formula = "='Dashboard M4 Price Monthly'!BA113"
    @eval_fn
    def AU87():
        ba113_1 = Dashboard_M4_Price_Monthly.BA113()
        return ba113_1

@register(Metric_4_5_7_8_Data_QC)
class AV87():
    # 'Metric_4_5_7_8_Data_QC'!AV87
    value = 17.2685901444
    formula = "='Dashboard M4 Price Monthly'!BB113"
    @eval_fn
    def AV87():
        bb113_1 = Dashboard_M4_Price_Monthly.BB113()
        return bb113_1

@register(Metric_4_5_7_8_Data_QC)
class AW87():
    # 'Metric_4_5_7_8_Data_QC'!AW87
    value = 17.207724016
    formula = "='Dashboard M4 Price Monthly'!BC113"
    @eval_fn
    def AW87():
        bc113_1 = Dashboard_M4_Price_Monthly.BC113()
        return bc113_1

@register(Metric_4_5_7_8_Data_QC)
class AX87():
    # 'Metric_4_5_7_8_Data_QC'!AX87
    value = 17.8424707836
    formula = "='Dashboard M4 Price Monthly'!BD113"
    @eval_fn
    def AX87():
        bd113_1 = Dashboard_M4_Price_Monthly.BD113()
        return bd113_1

@register(Metric_4_5_7_8_Data_QC)
class AY87():
    # 'Metric_4_5_7_8_Data_QC'!AY87
    value = 17.294675628
    formula = "='Dashboard M4 Price Monthly'!BE113"
    @eval_fn
    def AY87():
        be113_1 = Dashboard_M4_Price_Monthly.BE113()
        return be113_1

@register(Metric_4_5_7_8_Data_QC)
class AZ87():
    # 'Metric_4_5_7_8_Data_QC'!AZ87
    value = 18.3293998109
    formula = "='Dashboard M4 Price Monthly'!BF113"
    @eval_fn
    def AZ87():
        bf113_1 = Dashboard_M4_Price_Monthly.BF113()
        return bf113_1

@register(Metric_4_5_7_8_Data_QC)
class BA87():
    # 'Metric_4_5_7_8_Data_QC'!BA87
    value = 19.503246573
    formula = "='Dashboard M4 Price Monthly'!BG113"
    @eval_fn
    def BA87():
        bg113_1 = Dashboard_M4_Price_Monthly.BG113()
        return bg113_1

@register(Metric_4_5_7_8_Data_QC)
class BB87():
    # 'Metric_4_5_7_8_Data_QC'!BB87
    value = 17.9381175568
    formula = "='Dashboard M4 Price Monthly'!BH113"
    @eval_fn
    def BB87():
        bh113_1 = Dashboard_M4_Price_Monthly.BH113()
        return bh113_1

@register(Metric_4_5_7_8_Data_QC)
class BC87():
    # 'Metric_4_5_7_8_Data_QC'!BC87
    value = 17.8946417508
    formula = "='Dashboard M4 Price Monthly'!BI113"
    @eval_fn
    def BC87():
        bi113_1 = Dashboard_M4_Price_Monthly.BI113()
        return bi113_1

@register(Metric_4_5_7_8_Data_QC)
class BD87():
    # 'Metric_4_5_7_8_Data_QC'!BD87
    value = 17.555530464
    formula = "='Dashboard M4 Price Monthly'!BJ113"
    @eval_fn
    def BD87():
        bj113_1 = Dashboard_M4_Price_Monthly.BJ113()
        return bj113_1

@register(Metric_4_5_7_8_Data_QC)
class BE87():
    # 'Metric_4_5_7_8_Data_QC'!BE87
    value = 18.1120207809
    formula = "='Dashboard M4 Price Monthly'!BK113"
    @eval_fn
    def BE87():
        bk113_1 = Dashboard_M4_Price_Monthly.BK113()
        return bk113_1

@register(Metric_4_5_7_8_Data_QC)
class BF87():
    # 'Metric_4_5_7_8_Data_QC'!BF87
    value = 18.3815707781
    formula = "='Dashboard M4 Price Monthly'!BL113"
    @eval_fn
    def BF87():
        bl113_1 = Dashboard_M4_Price_Monthly.BL113()
        return bl113_1

@register(Metric_4_5_7_8_Data_QC)
class BG87():
    # 'Metric_4_5_7_8_Data_QC'!BG87
    value = 19.546722379
    formula = "='Dashboard M4 Price Monthly'!BM113"
    @eval_fn
    def BG87():
        bm113_1 = Dashboard_M4_Price_Monthly.BM113()
        return bm113_1

@register(Metric_4_5_7_8_Data_QC)
class BH87():
    # 'Metric_4_5_7_8_Data_QC'!BH87
    value = 20.198859469
    formula = "='Dashboard M4 Price Monthly'!BN113"
    @eval_fn
    def BH87():
        bn113_1 = Dashboard_M4_Price_Monthly.BN113()
        return bn113_1

@register(Metric_4_5_7_8_Data_QC)
class BI87():
    # 'Metric_4_5_7_8_Data_QC'!BI87
    value = 21.3292304251
    formula = "='Dashboard M4 Price Monthly'!BO113"
    @eval_fn
    def BI87():
        bo113_1 = Dashboard_M4_Price_Monthly.BO113()
        return bo113_1

@register(Metric_4_5_7_8_Data_QC)
class BJ87():
    # 'Metric_4_5_7_8_Data_QC'!BJ87
    value = 22.7726271844
    formula = "='Dashboard M4 Price Monthly'!BP113"
    @eval_fn
    def BJ87():
        bp113_1 = Dashboard_M4_Price_Monthly.BP113()
        return bp113_1

@register(Metric_4_5_7_8_Data_QC)
class BK87():
    # 'Metric_4_5_7_8_Data_QC'!BK87
    value = 24.6855626485
    formula = "='Dashboard M4 Price Monthly'!BQ113"
    @eval_fn
    def BK87():
        bq113_1 = Dashboard_M4_Price_Monthly.BQ113()
        return bq113_1

@register(Metric_4_5_7_8_Data_QC)
class BL87():
    # 'Metric_4_5_7_8_Data_QC'!BL87
    value = 27.1723787519
    formula = "='Dashboard M4 Price Monthly'!BR113"
    @eval_fn
    def BL87():
        br113_1 = Dashboard_M4_Price_Monthly.BR113()
        return br113_1

@register(Metric_4_5_7_8_Data_QC)
class BM87():
    # 'Metric_4_5_7_8_Data_QC'!BM87
    value = 28.4070916424
    formula = "='Dashboard M4 Price Monthly'!BS113"
    @eval_fn
    def BM87():
        bs113_1 = Dashboard_M4_Price_Monthly.BS113()
        return bs113_1

@register(Metric_4_5_7_8_Data_QC)
class BN87():
    # 'Metric_4_5_7_8_Data_QC'!BN87
    value = 26.8245723039
    formula = "='Dashboard M4 Price Monthly'!BT113"
    @eval_fn
    def BN87():
        bt113_1 = Dashboard_M4_Price_Monthly.BT113()
        return bt113_1

@register(Metric_4_5_7_8_Data_QC)
class BO87():
    # 'Metric_4_5_7_8_Data_QC'!BO87
    value = 26.485461017
    formula = "='Dashboard M4 Price Monthly'!BU113"
    @eval_fn
    def BO87():
        bu113_1 = Dashboard_M4_Price_Monthly.BU113()
        return bu113_1

@register(Metric_4_5_7_8_Data_QC)
class BP87():
    # 'Metric_4_5_7_8_Data_QC'!BP87
    value = 27.2245497191
    formula = "='Dashboard M4 Price Monthly'!BV113"
    @eval_fn
    def BP87():
        bv113_1 = Dashboard_M4_Price_Monthly.BV113()
        return bv113_1

@register(Metric_4_5_7_8_Data_QC)
class BQ87():
    # 'Metric_4_5_7_8_Data_QC'!BQ87
    value = 26.1550448914
    formula = "='Dashboard M4 Price Monthly'!BW113"
    @eval_fn
    def BQ87():
        bw113_1 = Dashboard_M4_Price_Monthly.BW113()
        return bw113_1

@register(Metric_4_5_7_8_Data_QC)
class BR87():
    # 'Metric_4_5_7_8_Data_QC'!BR87
    value = 25.6333352194
    formula = "='Dashboard M4 Price Monthly'!BX113"
    @eval_fn
    def BR87():
        bx113_1 = Dashboard_M4_Price_Monthly.BX113()
        return bx113_1

@register(Metric_4_5_7_8_Data_QC)
class BS87():
    # 'Metric_4_5_7_8_Data_QC'!BS87
    value = 25.789848121
    formula = "='Dashboard M4 Price Monthly'!BY113"
    @eval_fn
    def BS87():
        by113_1 = Dashboard_M4_Price_Monthly.BY113()
        return by113_1

@register(Metric_4_5_7_8_Data_QC)
class BT87():
    # 'Metric_4_5_7_8_Data_QC'!BT87
    value = 26.485461017
    formula = "='Dashboard M4 Price Monthly'!BZ113"
    @eval_fn
    def BT87():
        bz113_1 = Dashboard_M4_Price_Monthly.BZ113()
        return bz113_1

@register(Metric_4_5_7_8_Data_QC)
class BU87():
    # 'Metric_4_5_7_8_Data_QC'!BU87
    value = 24.9811981293
    formula = "='Dashboard M4 Price Monthly'!CA113"
    @eval_fn
    def BU87():
        ca113_1 = Dashboard_M4_Price_Monthly.CA113()
        return ca113_1

@register(Metric_4_5_7_8_Data_QC)
class BV87():
    # 'Metric_4_5_7_8_Data_QC'!BV87
    value = 26.8419626263
    formula = "='Dashboard M4 Price Monthly'!CB113"
    @eval_fn
    def BV87():
        cb113_1 = Dashboard_M4_Price_Monthly.CB113()
        return cb113_1

@register(Metric_4_5_7_8_Data_QC)
class BW87():
    # 'Metric_4_5_7_8_Data_QC'!BW87
    value = 27.8853819703
    formula = "='Dashboard M4 Price Monthly'!CC113"
    @eval_fn
    def BW87():
        cc113_1 = Dashboard_M4_Price_Monthly.CC113()
        return cc113_1

@register(Metric_4_5_7_8_Data_QC)
class BX87():
    # 'Metric_4_5_7_8_Data_QC'!BX87
    value = 28.3114448692
    formula = "='Dashboard M4 Price Monthly'!CD113"
    @eval_fn
    def BX87():
        cd113_1 = Dashboard_M4_Price_Monthly.CD113()
        return cd113_1

@register(Metric_4_5_7_8_Data_QC)
class BY87():
    # 'Metric_4_5_7_8_Data_QC'!BY87
    value = 28.0505900331
    formula = "='Dashboard M4 Price Monthly'!CE113"
    @eval_fn
    def BY87():
        ce113_1 = Dashboard_M4_Price_Monthly.CE113()
        return ce113_1

@register(Metric_4_5_7_8_Data_QC)
class BZ87():
    # 'Metric_4_5_7_8_Data_QC'!BZ87
    value = 25.8594094106
    formula = "='Dashboard M4 Price Monthly'!CF113"
    @eval_fn
    def BZ87():
        cf113_1 = Dashboard_M4_Price_Monthly.CF113()
        return cf113_1

@register(Metric_4_5_7_8_Data_QC)
class CA87():
    # 'Metric_4_5_7_8_Data_QC'!CA87
    value = 23.2856416952
    formula = "='Dashboard M4 Price Monthly'!CG113"
    @eval_fn
    def CA87():
        cg113_1 = Dashboard_M4_Price_Monthly.CG113()
        return cg113_1

@register(Metric_4_5_7_8_Data_QC)
class CB87():
    # 'Metric_4_5_7_8_Data_QC'!CB87
    value = 25.1464061921
    formula = "='Dashboard M4 Price Monthly'!CH113"
    @eval_fn
    def CB87():
        ch113_1 = Dashboard_M4_Price_Monthly.CH113()
        return ch113_1

@register(Metric_4_5_7_8_Data_QC)
class CC87():
    # 'Metric_4_5_7_8_Data_QC'!CC87
    value = 27.4419287491
    formula = "='Dashboard M4 Price Monthly'!CI113"
    @eval_fn
    def CC87():
        ci113_1 = Dashboard_M4_Price_Monthly.CI113()
        return ci113_1

@register(Metric_4_5_7_8_Data_QC)
class CD87():
    # 'Metric_4_5_7_8_Data_QC'!CD87
    value = 27.7462593911
    formula = "='Dashboard M4 Price Monthly'!CJ113"
    @eval_fn
    def CD87():
        cj113_1 = Dashboard_M4_Price_Monthly.CJ113()
        return cj113_1

@register(Metric_4_5_7_8_Data_QC)
class CE87():
    # 'Metric_4_5_7_8_Data_QC'!CE87
    value = 27.0506464951
    formula = "='Dashboard M4 Price Monthly'!CK113"
    @eval_fn
    def CE87():
        ck113_1 = Dashboard_M4_Price_Monthly.CK113()
        return ck113_1

@register(Metric_4_5_7_8_Data_QC)
class B88():
    # 'Metric_4_5_7_8_Data_QC'!B88
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class E88():
    # 'Metric_4_5_7_8_Data_QC'!E88
    value = 23.8398472753
    formula = "='Dashboard M4 Price Monthly'!H114"
    @eval_fn
    def E88():
        h114_1 = Dashboard_M4_Price_Monthly.H114()
        return h114_1

@register(Metric_4_5_7_8_Data_QC)
class F88():
    # 'Metric_4_5_7_8_Data_QC'!F88
    value = 23.7948628948
    formula = "='Dashboard M4 Price Monthly'!I114"
    @eval_fn
    def F88():
        i114_1 = Dashboard_M4_Price_Monthly.I114()
        return i114_1

@register(Metric_4_5_7_8_Data_QC)
class G88():
    # 'Metric_4_5_7_8_Data_QC'!G88
    value = 23.8876734109
    formula = "='Dashboard M4 Price Monthly'!J114"
    @eval_fn
    def G88():
        j114_1 = Dashboard_M4_Price_Monthly.J114()
        return j114_1

@register(Metric_4_5_7_8_Data_QC)
class H88():
    # 'Metric_4_5_7_8_Data_QC'!H88
    value = 24.3726076913
    formula = "='Dashboard M4 Price Monthly'!K114"
    @eval_fn
    def H88():
        k114_1 = Dashboard_M4_Price_Monthly.K114()
        return k114_1

@register(Metric_4_5_7_8_Data_QC)
class I88():
    # 'Metric_4_5_7_8_Data_QC'!I88
    value = 25.6977304027
    formula = "='Dashboard M4 Price Monthly'!O114"
    @eval_fn
    def I88():
        o114_1 = Dashboard_M4_Price_Monthly.O114()
        return o114_1

@register(Metric_4_5_7_8_Data_QC)
class J88():
    # 'Metric_4_5_7_8_Data_QC'!J88
    value = 25.7053800764
    formula = "='Dashboard M4 Price Monthly'!P114"
    @eval_fn
    def J88():
        p114_1 = Dashboard_M4_Price_Monthly.P114()
        return p114_1

@register(Metric_4_5_7_8_Data_QC)
class K88():
    # 'Metric_4_5_7_8_Data_QC'!K88
    value = 25.4837903506
    formula = "='Dashboard M4 Price Monthly'!Q114"
    @eval_fn
    def K88():
        q114_1 = Dashboard_M4_Price_Monthly.Q114()
        return q114_1

@register(Metric_4_5_7_8_Data_QC)
class L88():
    # 'Metric_4_5_7_8_Data_QC'!L88
    value = 25.3098229781
    formula = "='Dashboard M4 Price Monthly'!R114"
    @eval_fn
    def L88():
        r114_1 = Dashboard_M4_Price_Monthly.R114()
        return r114_1

@register(Metric_4_5_7_8_Data_QC)
class M88():
    # 'Metric_4_5_7_8_Data_QC'!M88
    value = 25.4200378453
    formula = "='Dashboard M4 Price Monthly'!S114"
    @eval_fn
    def M88():
        s114_1 = Dashboard_M4_Price_Monthly.S114()
        return s114_1

@register(Metric_4_5_7_8_Data_QC)
class N88():
    # 'Metric_4_5_7_8_Data_QC'!N88
    value = 25.5049210064
    formula = "='Dashboard M4 Price Monthly'!T114"
    @eval_fn
    def N88():
        t114_1 = Dashboard_M4_Price_Monthly.T114()
        return t114_1

@register(Metric_4_5_7_8_Data_QC)
class O88():
    # 'Metric_4_5_7_8_Data_QC'!O88
    value = 25.2696112461
    formula = "='Dashboard M4 Price Monthly'!U114"
    @eval_fn
    def O88():
        u114_1 = Dashboard_M4_Price_Monthly.U114()
        return u114_1

@register(Metric_4_5_7_8_Data_QC)
class P88():
    # 'Metric_4_5_7_8_Data_QC'!P88
    value = 25.2505066565
    formula = "='Dashboard M4 Price Monthly'!V114"
    @eval_fn
    def P88():
        v114_1 = Dashboard_M4_Price_Monthly.V114()
        return v114_1

@register(Metric_4_5_7_8_Data_QC)
class Q88():
    # 'Metric_4_5_7_8_Data_QC'!Q88
    value = 25.5338424158
    formula = "='Dashboard M4 Price Monthly'!W114"
    @eval_fn
    def Q88():
        w114_1 = Dashboard_M4_Price_Monthly.W114()
        return w114_1

@register(Metric_4_5_7_8_Data_QC)
class R88():
    # 'Metric_4_5_7_8_Data_QC'!R88
    value = 25.8907749325
    formula = "='Dashboard M4 Price Monthly'!X114"
    @eval_fn
    def R88():
        x114_1 = Dashboard_M4_Price_Monthly.X114()
        return x114_1

@register(Metric_4_5_7_8_Data_QC)
class S88():
    # 'Metric_4_5_7_8_Data_QC'!S88
    value = 25.9721624436
    formula = "='Dashboard M4 Price Monthly'!Y114"
    @eval_fn
    def S88():
        y114_1 = Dashboard_M4_Price_Monthly.Y114()
        return y114_1

@register(Metric_4_5_7_8_Data_QC)
class T88():
    # 'Metric_4_5_7_8_Data_QC'!T88
    value = 26.0965166665
    formula = "='Dashboard M4 Price Monthly'!Z114"
    @eval_fn
    def T88():
        z114_1 = Dashboard_M4_Price_Monthly.Z114()
        return z114_1

@register(Metric_4_5_7_8_Data_QC)
class U88():
    # 'Metric_4_5_7_8_Data_QC'!U88
    value = 26.2575830525
    formula = "='Dashboard M4 Price Monthly'!AA114"
    @eval_fn
    def U88():
        aa114_1 = Dashboard_M4_Price_Monthly.AA114()
        return aa114_1

@register(Metric_4_5_7_8_Data_QC)
class V88():
    # 'Metric_4_5_7_8_Data_QC'!V88
    value = 26.3043040611
    formula = "='Dashboard M4 Price Monthly'!AB114"
    @eval_fn
    def V88():
        ab114_1 = Dashboard_M4_Price_Monthly.AB114()
        return ab114_1

@register(Metric_4_5_7_8_Data_QC)
class W88():
    # 'Metric_4_5_7_8_Data_QC'!W88
    value = 26.6719194724
    formula = "='Dashboard M4 Price Monthly'!AC114"
    @eval_fn
    def W88():
        ac114_1 = Dashboard_M4_Price_Monthly.AC114()
        return ac114_1

@register(Metric_4_5_7_8_Data_QC)
class X88():
    # 'Metric_4_5_7_8_Data_QC'!X88
    value = 27.7378340854
    formula = "='Dashboard M4 Price Monthly'!AD114"
    @eval_fn
    def X88():
        ad114_1 = Dashboard_M4_Price_Monthly.AD114()
        return ad114_1

@register(Metric_4_5_7_8_Data_QC)
class Y88():
    # 'Metric_4_5_7_8_Data_QC'!Y88
    value = 28.3496355432
    formula = "='Dashboard M4 Price Monthly'!AE114"
    @eval_fn
    def Y88():
        ae114_1 = Dashboard_M4_Price_Monthly.AE114()
        return ae114_1

@register(Metric_4_5_7_8_Data_QC)
class Z88():
    # 'Metric_4_5_7_8_Data_QC'!Z88
    value = 28.4598425726
    formula = "='Dashboard M4 Price Monthly'!AF114"
    @eval_fn
    def Z88():
        af114_1 = Dashboard_M4_Price_Monthly.AF114()
        return af114_1

@register(Metric_4_5_7_8_Data_QC)
class AA88():
    # 'Metric_4_5_7_8_Data_QC'!AA88
    value = 28.4070635196
    formula = "='Dashboard M4 Price Monthly'!AG114"
    @eval_fn
    def AA88():
        ag114_1 = Dashboard_M4_Price_Monthly.AG114()
        return ag114_1

@register(Metric_4_5_7_8_Data_QC)
class AB88():
    # 'Metric_4_5_7_8_Data_QC'!AB88
    value = 29.6369204241
    formula = "='Dashboard M4 Price Monthly'!AH114"
    @eval_fn
    def AB88():
        ah114_1 = Dashboard_M4_Price_Monthly.AH114()
        return ah114_1

@register(Metric_4_5_7_8_Data_QC)
class AC88():
    # 'Metric_4_5_7_8_Data_QC'!AC88
    value = 31.4063723085
    formula = "='Dashboard M4 Price Monthly'!AI114"
    @eval_fn
    def AC88():
        ai114_1 = Dashboard_M4_Price_Monthly.AI114()
        return ai114_1

@register(Metric_4_5_7_8_Data_QC)
class AD88():
    # 'Metric_4_5_7_8_Data_QC'!AD88
    value = 34.3492290983
    formula = "='Dashboard M4 Price Monthly'!AJ114"
    @eval_fn
    def AD88():
        aj114_1 = Dashboard_M4_Price_Monthly.AJ114()
        return aj114_1

@register(Metric_4_5_7_8_Data_QC)
class AE88():
    # 'Metric_4_5_7_8_Data_QC'!AE88
    value = 38.001423117
    formula = "='Dashboard M4 Price Monthly'!AK114"
    @eval_fn
    def AE88():
        ak114_1 = Dashboard_M4_Price_Monthly.AK114()
        return ak114_1

@register(Metric_4_5_7_8_Data_QC)
class AF88():
    # 'Metric_4_5_7_8_Data_QC'!AF88
    value = 39.2115528882
    formula = "='Dashboard M4 Price Monthly'!AL114"
    @eval_fn
    def AF88():
        al114_1 = Dashboard_M4_Price_Monthly.AL114()
        return al114_1

@register(Metric_4_5_7_8_Data_QC)
class AG88():
    # 'Metric_4_5_7_8_Data_QC'!AG88
    value = 38.8793093796
    formula = "='Dashboard M4 Price Monthly'!AM114"
    @eval_fn
    def AG88():
        am114_1 = Dashboard_M4_Price_Monthly.AM114()
        return am114_1

@register(Metric_4_5_7_8_Data_QC)
class AH88():
    # 'Metric_4_5_7_8_Data_QC'!AH88
    value = 37.7548073586
    formula = "='Dashboard M4 Price Monthly'!AN114"
    @eval_fn
    def AH88():
        an114_1 = Dashboard_M4_Price_Monthly.AN114()
        return an114_1

@register(Metric_4_5_7_8_Data_QC)
class AI88():
    # 'Metric_4_5_7_8_Data_QC'!AI88
    value = 36.1806832305
    formula = "='Dashboard M4 Price Monthly'!AO114"
    @eval_fn
    def AI88():
        ao114_1 = Dashboard_M4_Price_Monthly.AO114()
        return ao114_1

@register(Metric_4_5_7_8_Data_QC)
class AJ88():
    # 'Metric_4_5_7_8_Data_QC'!AJ88
    value = 33.2474488025
    formula = "='Dashboard M4 Price Monthly'!AP114"
    @eval_fn
    def AJ88():
        ap114_1 = Dashboard_M4_Price_Monthly.AP114()
        return ap114_1

@register(Metric_4_5_7_8_Data_QC)
class AK88():
    # 'Metric_4_5_7_8_Data_QC'!AK88
    value = 29.7145144495
    formula = "='Dashboard M4 Price Monthly'!AQ114"
    @eval_fn
    def AK88():
        aq114_1 = Dashboard_M4_Price_Monthly.AQ114()
        return aq114_1

@register(Metric_4_5_7_8_Data_QC)
class AL88():
    # 'Metric_4_5_7_8_Data_QC'!AL88
    value = 28.6622924388
    formula = "='Dashboard M4 Price Monthly'!AR114"
    @eval_fn
    def AL88():
        ar114_1 = Dashboard_M4_Price_Monthly.AR114()
        return ar114_1

@register(Metric_4_5_7_8_Data_QC)
class AM88():
    # 'Metric_4_5_7_8_Data_QC'!AM88
    value = 28.3341721624
    formula = "='Dashboard M4 Price Monthly'!AS114"
    @eval_fn
    def AM88():
        as114_1 = Dashboard_M4_Price_Monthly.AS114()
        return as114_1

@register(Metric_4_5_7_8_Data_QC)
class AN88():
    # 'Metric_4_5_7_8_Data_QC'!AN88
    value = 27.976878548
    formula = "='Dashboard M4 Price Monthly'!AT114"
    @eval_fn
    def AN88():
        at114_1 = Dashboard_M4_Price_Monthly.AT114()
        return at114_1

@register(Metric_4_5_7_8_Data_QC)
class AO88():
    # 'Metric_4_5_7_8_Data_QC'!AO88
    value = 27.8753557792
    formula = "='Dashboard M4 Price Monthly'!AU114"
    @eval_fn
    def AO88():
        au114_1 = Dashboard_M4_Price_Monthly.AU114()
        return au114_1

@register(Metric_4_5_7_8_Data_QC)
class AP88():
    # 'Metric_4_5_7_8_Data_QC'!AP88
    value = 27.7716070809
    formula = "='Dashboard M4 Price Monthly'!AV114"
    @eval_fn
    def AP88():
        av114_1 = Dashboard_M4_Price_Monthly.AV114()
        return av114_1

@register(Metric_4_5_7_8_Data_QC)
class AQ88():
    # 'Metric_4_5_7_8_Data_QC'!AQ88
    value = 28.2376258244
    formula = "='Dashboard M4 Price Monthly'!AW114"
    @eval_fn
    def AQ88():
        aw114_1 = Dashboard_M4_Price_Monthly.AW114()
        return aw114_1

@register(Metric_4_5_7_8_Data_QC)
class AR88():
    # 'Metric_4_5_7_8_Data_QC'!AR88
    value = 28.3620270739
    formula = "='Dashboard M4 Price Monthly'!AX114"
    @eval_fn
    def AR88():
        ax114_1 = Dashboard_M4_Price_Monthly.AX114()
        return ax114_1

@register(Metric_4_5_7_8_Data_QC)
class AS88():
    # 'Metric_4_5_7_8_Data_QC'!AS88
    value = 28.6025685526
    formula = "='Dashboard M4 Price Monthly'!AY114"
    @eval_fn
    def AS88():
        ay114_1 = Dashboard_M4_Price_Monthly.AY114()
        return ay114_1

@register(Metric_4_5_7_8_Data_QC)
class AT88():
    # 'Metric_4_5_7_8_Data_QC'!AT88
    value = 28.6025685526
    formula = "='Dashboard M4 Price Monthly'!AZ114"
    @eval_fn
    def AT88():
        az114_1 = Dashboard_M4_Price_Monthly.AZ114()
        return az114_1

@register(Metric_4_5_7_8_Data_QC)
class AU88():
    # 'Metric_4_5_7_8_Data_QC'!AU88
    value = 28.3911836168
    formula = "='Dashboard M4 Price Monthly'!BA114"
    @eval_fn
    def AU88():
        ba114_1 = Dashboard_M4_Price_Monthly.BA114()
        return ba114_1

@register(Metric_4_5_7_8_Data_QC)
class AV88():
    # 'Metric_4_5_7_8_Data_QC'!AV88
    value = 28.5369663311
    formula = "='Dashboard M4 Price Monthly'!BB114"
    @eval_fn
    def AV88():
        bb114_1 = Dashboard_M4_Price_Monthly.BB114()
        return bb114_1

@register(Metric_4_5_7_8_Data_QC)
class AW88():
    # 'Metric_4_5_7_8_Data_QC'!AW88
    value = 28.5078097883
    formula = "='Dashboard M4 Price Monthly'!BC114"
    @eval_fn
    def AW88():
        bc114_1 = Dashboard_M4_Price_Monthly.BC114()
        return bc114_1

@register(Metric_4_5_7_8_Data_QC)
class AX88():
    # 'Metric_4_5_7_8_Data_QC'!AX88
    value = 28.668170774
    formula = "='Dashboard M4 Price Monthly'!BD114"
    @eval_fn
    def AX88():
        bd114_1 = Dashboard_M4_Price_Monthly.BD114()
        return bd114_1

@register(Metric_4_5_7_8_Data_QC)
class AY88():
    # 'Metric_4_5_7_8_Data_QC'!AY88
    value = 28.6098576883
    formula = "='Dashboard M4 Price Monthly'!BE114"
    @eval_fn
    def AY88():
        be114_1 = Dashboard_M4_Price_Monthly.BE114()
        return be114_1

@register(Metric_4_5_7_8_Data_QC)
class AZ88():
    # 'Metric_4_5_7_8_Data_QC'!AZ88
    value = 28.6754599098
    formula = "='Dashboard M4 Price Monthly'!BF114"
    @eval_fn
    def AZ88():
        bf114_1 = Dashboard_M4_Price_Monthly.BF114()
        return bf114_1

@register(Metric_4_5_7_8_Data_QC)
class BA88():
    # 'Metric_4_5_7_8_Data_QC'!BA88
    value = 28.8941339813
    formula = "='Dashboard M4 Price Monthly'!BG114"
    @eval_fn
    def BA88():
        bg114_1 = Dashboard_M4_Price_Monthly.BG114()
        return bg114_1

@register(Metric_4_5_7_8_Data_QC)
class BB88():
    # 'Metric_4_5_7_8_Data_QC'!BB88
    value = 29.1081053846
    formula = "='Dashboard M4 Price Monthly'!BH114"
    @eval_fn
    def BB88():
        bh114_1 = Dashboard_M4_Price_Monthly.BH114()
        return bh114_1

@register(Metric_4_5_7_8_Data_QC)
class BC88():
    # 'Metric_4_5_7_8_Data_QC'!BC88
    value = 28.8576883027
    formula = "='Dashboard M4 Price Monthly'!BI114"
    @eval_fn
    def BC88():
        bi114_1 = Dashboard_M4_Price_Monthly.BI114()
        return bi114_1

@register(Metric_4_5_7_8_Data_QC)
class BD88():
    # 'Metric_4_5_7_8_Data_QC'!BD88
    value = 28.9888927456
    formula = "='Dashboard M4 Price Monthly'!BJ114"
    @eval_fn
    def BD88():
        bj114_1 = Dashboard_M4_Price_Monthly.BJ114()
        return bj114_1

@register(Metric_4_5_7_8_Data_QC)
class BE88():
    # 'Metric_4_5_7_8_Data_QC'!BE88
    value = 29.0763623742
    formula = "='Dashboard M4 Price Monthly'!BK114"
    @eval_fn
    def BE88():
        bk114_1 = Dashboard_M4_Price_Monthly.BK114()
        return bk114_1

@register(Metric_4_5_7_8_Data_QC)
class BF88():
    # 'Metric_4_5_7_8_Data_QC'!BF88
    value = 28.9961818813
    formula = "='Dashboard M4 Price Monthly'!BL114"
    @eval_fn
    def BF88():
        bl114_1 = Dashboard_M4_Price_Monthly.BL114()
        return bl114_1

@register(Metric_4_5_7_8_Data_QC)
class BG88():
    # 'Metric_4_5_7_8_Data_QC'!BG88
    value = 29.4699757029
    formula = "='Dashboard M4 Price Monthly'!BM114"
    @eval_fn
    def BG88():
        bm114_1 = Dashboard_M4_Price_Monthly.BM114()
        return bm114_1

@register(Metric_4_5_7_8_Data_QC)
class BH88():
    # 'Metric_4_5_7_8_Data_QC'!BH88
    value = 29.6449149601
    formula = "='Dashboard M4 Price Monthly'!BN114"
    @eval_fn
    def BH88():
        bn114_1 = Dashboard_M4_Price_Monthly.BN114()
        return bn114_1

@register(Metric_4_5_7_8_Data_QC)
class BI88():
    # 'Metric_4_5_7_8_Data_QC'!BI88
    value = 29.7906976744
    formula = "='Dashboard M4 Price Monthly'!BO114"
    @eval_fn
    def BI88():
        bo114_1 = Dashboard_M4_Price_Monthly.BO114()
        return bo114_1

@register(Metric_4_5_7_8_Data_QC)
class BJ88():
    # 'Metric_4_5_7_8_Data_QC'!BJ88
    value = 29.9875043388
    formula = "='Dashboard M4 Price Monthly'!BP114"
    @eval_fn
    def BJ88():
        bp114_1 = Dashboard_M4_Price_Monthly.BP114()
        return bp114_1

@register(Metric_4_5_7_8_Data_QC)
class BK88():
    # 'Metric_4_5_7_8_Data_QC'!BK88
    value = 30.4175633461
    formula = "='Dashboard M4 Price Monthly'!BQ114"
    @eval_fn
    def BK88():
        bq114_1 = Dashboard_M4_Price_Monthly.BQ114()
        return bq114_1

@register(Metric_4_5_7_8_Data_QC)
class BL88():
    # 'Metric_4_5_7_8_Data_QC'!BL88
    value = 32.4730996182
    formula = "='Dashboard M4 Price Monthly'!BR114"
    @eval_fn
    def BL88():
        br114_1 = Dashboard_M4_Price_Monthly.BR114()
        return br114_1

@register(Metric_4_5_7_8_Data_QC)
class BM88():
    # 'Metric_4_5_7_8_Data_QC'!BM88
    value = 34.8639361333
    formula = "='Dashboard M4 Price Monthly'!BS114"
    @eval_fn
    def BM88():
        bs114_1 = Dashboard_M4_Price_Monthly.BS114()
        return bs114_1

@register(Metric_4_5_7_8_Data_QC)
class BN88():
    # 'Metric_4_5_7_8_Data_QC'!BN88
    value = 35.3231516834
    formula = "='Dashboard M4 Price Monthly'!BT114"
    @eval_fn
    def BN88():
        bt114_1 = Dashboard_M4_Price_Monthly.BT114()
        return bt114_1

@register(Metric_4_5_7_8_Data_QC)
class BO88():
    # 'Metric_4_5_7_8_Data_QC'!BO88
    value = 34.7254425547
    formula = "='Dashboard M4 Price Monthly'!BU114"
    @eval_fn
    def BO88():
        bu114_1 = Dashboard_M4_Price_Monthly.BU114()
        return bu114_1

@register(Metric_4_5_7_8_Data_QC)
class BP88():
    # 'Metric_4_5_7_8_Data_QC'!BP88
    value = 34.4557445331
    formula = "='Dashboard M4 Price Monthly'!BV114"
    @eval_fn
    def BP88():
        bv114_1 = Dashboard_M4_Price_Monthly.BV114()
        return bv114_1

@register(Metric_4_5_7_8_Data_QC)
class BQ88():
    # 'Metric_4_5_7_8_Data_QC'!BQ88
    value = 34.3536966331
    formula = "='Dashboard M4 Price Monthly'!BW114"
    @eval_fn
    def BQ88():
        bw114_1 = Dashboard_M4_Price_Monthly.BW114()
        return bw114_1

@register(Metric_4_5_7_8_Data_QC)
class BR88():
    # 'Metric_4_5_7_8_Data_QC'!BR88
    value = 34.6379729261
    formula = "='Dashboard M4 Price Monthly'!BX114"
    @eval_fn
    def BR88():
        bx114_1 = Dashboard_M4_Price_Monthly.BX114()
        return bx114_1

@register(Metric_4_5_7_8_Data_QC)
class BS88():
    # 'Metric_4_5_7_8_Data_QC'!BS88
    value = 34.6233946546
    formula = "='Dashboard M4 Price Monthly'!BY114"
    @eval_fn
    def BS88():
        by114_1 = Dashboard_M4_Price_Monthly.BY114()
        return by114_1

@register(Metric_4_5_7_8_Data_QC)
class BT88():
    # 'Metric_4_5_7_8_Data_QC'!BT88
    value = 35.0898993405
    formula = "='Dashboard M4 Price Monthly'!BZ114"
    @eval_fn
    def BT88():
        bz114_1 = Dashboard_M4_Price_Monthly.BZ114()
        return bz114_1

@register(Metric_4_5_7_8_Data_QC)
class BU88():
    # 'Metric_4_5_7_8_Data_QC'!BU88
    value = 34.9003818119
    formula = "='Dashboard M4 Price Monthly'!CA114"
    @eval_fn
    def BU88():
        ca114_1 = Dashboard_M4_Price_Monthly.CA114()
        return ca114_1

@register(Metric_4_5_7_8_Data_QC)
class BV88():
    # 'Metric_4_5_7_8_Data_QC'!BV88
    value = 34.8850981402
    formula = "='Dashboard M4 Price Monthly'!CB114"
    @eval_fn
    def BV88():
        cb114_1 = Dashboard_M4_Price_Monthly.CB114()
        return cb114_1

@register(Metric_4_5_7_8_Data_QC)
class BW88():
    # 'Metric_4_5_7_8_Data_QC'!BW88
    value = 35.106488408
    formula = "='Dashboard M4 Price Monthly'!CC114"
    @eval_fn
    def BW88():
        cc114_1 = Dashboard_M4_Price_Monthly.CC114()
        return cc114_1

@register(Metric_4_5_7_8_Data_QC)
class BX88():
    # 'Metric_4_5_7_8_Data_QC'!BX88
    value = 36.1677508929
    formula = "='Dashboard M4 Price Monthly'!CD114"
    @eval_fn
    def BX88():
        cd114_1 = Dashboard_M4_Price_Monthly.CD114()
        return cd114_1

@register(Metric_4_5_7_8_Data_QC)
class BY88():
    # 'Metric_4_5_7_8_Data_QC'!BY88
    value = 36.4194376952
    formula = "='Dashboard M4 Price Monthly'!CE114"
    @eval_fn
    def BY88():
        ce114_1 = Dashboard_M4_Price_Monthly.CE114()
        return ce114_1

@register(Metric_4_5_7_8_Data_QC)
class BZ88():
    # 'Metric_4_5_7_8_Data_QC'!BZ88
    value = 36.2533394543
    formula = "='Dashboard M4 Price Monthly'!CF114"
    @eval_fn
    def BZ88():
        cf114_1 = Dashboard_M4_Price_Monthly.CF114()
        return cf114_1

@register(Metric_4_5_7_8_Data_QC)
class CA88():
    # 'Metric_4_5_7_8_Data_QC'!CA88
    value = 35.3224227699
    formula = "='Dashboard M4 Price Monthly'!CG114"
    @eval_fn
    def CA88():
        cg114_1 = Dashboard_M4_Price_Monthly.CG114()
        return cg114_1

@register(Metric_4_5_7_8_Data_QC)
class CB88():
    # 'Metric_4_5_7_8_Data_QC'!CB88
    value = 34.5443898288
    formula = "='Dashboard M4 Price Monthly'!CH114"
    @eval_fn
    def CB88():
        ch114_1 = Dashboard_M4_Price_Monthly.CH114()
        return ch114_1

@register(Metric_4_5_7_8_Data_QC)
class CC88():
    # 'Metric_4_5_7_8_Data_QC'!CC88
    value = 34.8599388653
    formula = "='Dashboard M4 Price Monthly'!CI114"
    @eval_fn
    def CC88():
        ci114_1 = Dashboard_M4_Price_Monthly.CI114()
        return ci114_1

@register(Metric_4_5_7_8_Data_QC)
class CD88():
    # 'Metric_4_5_7_8_Data_QC'!CD88
    value = 36.0894828185
    formula = "='Dashboard M4 Price Monthly'!CJ114"
    @eval_fn
    def CD88():
        cj114_1 = Dashboard_M4_Price_Monthly.CJ114()
        return cj114_1

@register(Metric_4_5_7_8_Data_QC)
class CE88():
    # 'Metric_4_5_7_8_Data_QC'!CE88
    value = 36.2194802432
    formula = "='Dashboard M4 Price Monthly'!CK114"
    @eval_fn
    def CE88():
        ck114_1 = Dashboard_M4_Price_Monthly.CK114()
        return ck114_1

@register(Metric_4_5_7_8_Data_QC)
class B89():
    # 'Metric_4_5_7_8_Data_QC'!B89
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class E89():
    # 'Metric_4_5_7_8_Data_QC'!E89
    value = 9.07937012884
    formula = "='Dashboard M4 Price Monthly'!H115"
    @eval_fn
    def E89():
        h115_1 = Dashboard_M4_Price_Monthly.H115()
        return h115_1

@register(Metric_4_5_7_8_Data_QC)
class F89():
    # 'Metric_4_5_7_8_Data_QC'!F89
    value = 8.79895021473
    formula = "='Dashboard M4 Price Monthly'!I115"
    @eval_fn
    def F89():
        i115_1 = Dashboard_M4_Price_Monthly.I115()
        return i115_1

@register(Metric_4_5_7_8_Data_QC)
class G89():
    # 'Metric_4_5_7_8_Data_QC'!G89
    value = 9.09198875987
    formula = "='Dashboard M4 Price Monthly'!J115"
    @eval_fn
    def G89():
        j115_1 = Dashboard_M4_Price_Monthly.J115()
        return j115_1

@register(Metric_4_5_7_8_Data_QC)
class H89():
    # 'Metric_4_5_7_8_Data_QC'!H89
    value = 9.37410529664
    formula = "='Dashboard M4 Price Monthly'!K115"
    @eval_fn
    def H89():
        k115_1 = Dashboard_M4_Price_Monthly.K115()
        return k115_1

@register(Metric_4_5_7_8_Data_QC)
class I89():
    # 'Metric_4_5_7_8_Data_QC'!I89
    value = 10.0215259
    formula = "='Dashboard M4 Price Monthly'!O115"
    @eval_fn
    def I89():
        o115_1 = Dashboard_M4_Price_Monthly.O115()
        return o115_1

@register(Metric_4_5_7_8_Data_QC)
class J89():
    # 'Metric_4_5_7_8_Data_QC'!J89
    value = 9.98828269975
    formula = "='Dashboard M4 Price Monthly'!P115"
    @eval_fn
    def J89():
        p115_1 = Dashboard_M4_Price_Monthly.P115()
        return p115_1

@register(Metric_4_5_7_8_Data_QC)
class K89():
    # 'Metric_4_5_7_8_Data_QC'!K89
    value = 9.7375536822
    formula = "='Dashboard M4 Price Monthly'!Q115"
    @eval_fn
    def K89():
        q115_1 = Dashboard_M4_Price_Monthly.Q115()
        return q115_1

@register(Metric_4_5_7_8_Data_QC)
class L89():
    # 'Metric_4_5_7_8_Data_QC'!L89
    value = 8.93754307831
    formula = "='Dashboard M4 Price Monthly'!R115"
    @eval_fn
    def L89():
        r115_1 = Dashboard_M4_Price_Monthly.R115()
        return r115_1

@register(Metric_4_5_7_8_Data_QC)
class M89():
    # 'Metric_4_5_7_8_Data_QC'!M89
    value = 8.51116059594
    formula = "='Dashboard M4 Price Monthly'!S115"
    @eval_fn
    def M89():
        s115_1 = Dashboard_M4_Price_Monthly.S115()
        return s115_1

@register(Metric_4_5_7_8_Data_QC)
class N89():
    # 'Metric_4_5_7_8_Data_QC'!N89
    value = 8.26626371878
    formula = "='Dashboard M4 Price Monthly'!T115"
    @eval_fn
    def N89():
        t115_1 = Dashboard_M4_Price_Monthly.T115()
        return t115_1

@register(Metric_4_5_7_8_Data_QC)
class O89():
    # 'Metric_4_5_7_8_Data_QC'!O89
    value = 8.54048035629
    formula = "='Dashboard M4 Price Monthly'!U115"
    @eval_fn
    def O89():
        u115_1 = Dashboard_M4_Price_Monthly.U115()
        return u115_1

@register(Metric_4_5_7_8_Data_QC)
class P89():
    # 'Metric_4_5_7_8_Data_QC'!P89
    value = 8.26833147765
    formula = "='Dashboard M4 Price Monthly'!V115"
    @eval_fn
    def P89():
        v115_1 = Dashboard_M4_Price_Monthly.V115()
        return v115_1

@register(Metric_4_5_7_8_Data_QC)
class Q89():
    # 'Metric_4_5_7_8_Data_QC'!Q89
    value = 8.66984783416
    formula = "='Dashboard M4 Price Monthly'!W115"
    @eval_fn
    def Q89():
        w115_1 = Dashboard_M4_Price_Monthly.W115()
        return w115_1

@register(Metric_4_5_7_8_Data_QC)
class R89():
    # 'Metric_4_5_7_8_Data_QC'!R89
    value = 8.88526589258
    formula = "='Dashboard M4 Price Monthly'!X115"
    @eval_fn
    def R89():
        x115_1 = Dashboard_M4_Price_Monthly.X115()
        return x115_1

@register(Metric_4_5_7_8_Data_QC)
class S89():
    # 'Metric_4_5_7_8_Data_QC'!S89
    value = 9.35310959122
    formula = "='Dashboard M4 Price Monthly'!Y115"
    @eval_fn
    def S89():
        y115_1 = Dashboard_M4_Price_Monthly.Y115()
        return y115_1

@register(Metric_4_5_7_8_Data_QC)
class T89():
    # 'Metric_4_5_7_8_Data_QC'!T89
    value = 10.2290970786
    formula = "='Dashboard M4 Price Monthly'!Z115"
    @eval_fn
    def T89():
        z115_1 = Dashboard_M4_Price_Monthly.Z115()
        return z115_1

@register(Metric_4_5_7_8_Data_QC)
class U89():
    # 'Metric_4_5_7_8_Data_QC'!U89
    value = 10.4848629447
    formula = "='Dashboard M4 Price Monthly'!AA115"
    @eval_fn
    def U89():
        aa115_1 = Dashboard_M4_Price_Monthly.AA115()
        return aa115_1

@register(Metric_4_5_7_8_Data_QC)
class V89():
    # 'Metric_4_5_7_8_Data_QC'!V89
    value = 10.9281586342
    formula = "='Dashboard M4 Price Monthly'!AB115"
    @eval_fn
    def V89():
        ab115_1 = Dashboard_M4_Price_Monthly.AB115()
        return ab115_1

@register(Metric_4_5_7_8_Data_QC)
class W89():
    # 'Metric_4_5_7_8_Data_QC'!W89
    value = 10.9030274111
    formula = "='Dashboard M4 Price Monthly'!AC115"
    @eval_fn
    def W89():
        ac115_1 = Dashboard_M4_Price_Monthly.AC115()
        return ac115_1

@register(Metric_4_5_7_8_Data_QC)
class X89():
    # 'Metric_4_5_7_8_Data_QC'!X89
    value = 11.0811727904
    formula = "='Dashboard M4 Price Monthly'!AD115"
    @eval_fn
    def X89():
        ad115_1 = Dashboard_M4_Price_Monthly.AD115()
        return ad115_1

@register(Metric_4_5_7_8_Data_QC)
class Y89():
    # 'Metric_4_5_7_8_Data_QC'!Y89
    value = 11.3031652617
    formula = "='Dashboard M4 Price Monthly'!AE115"
    @eval_fn
    def Y89():
        ae115_1 = Dashboard_M4_Price_Monthly.AE115()
        return ae115_1

@register(Metric_4_5_7_8_Data_QC)
class Z89():
    # 'Metric_4_5_7_8_Data_QC'!Z89
    value = 13.090504215
    formula = "='Dashboard M4 Price Monthly'!AF115"
    @eval_fn
    def Z89():
        af115_1 = Dashboard_M4_Price_Monthly.AF115()
        return af115_1

@register(Metric_4_5_7_8_Data_QC)
class AA89():
    # 'Metric_4_5_7_8_Data_QC'!AA89
    value = 14.6460951169
    formula = "='Dashboard M4 Price Monthly'!AG115"
    @eval_fn
    def AA89():
        ag115_1 = Dashboard_M4_Price_Monthly.AG115()
        return ag115_1

@register(Metric_4_5_7_8_Data_QC)
class AB89():
    # 'Metric_4_5_7_8_Data_QC'!AB89
    value = 14.5840623509
    formula = "='Dashboard M4 Price Monthly'!AH115"
    @eval_fn
    def AB89():
        ah115_1 = Dashboard_M4_Price_Monthly.AH115()
        return ah115_1

@register(Metric_4_5_7_8_Data_QC)
class AC89():
    # 'Metric_4_5_7_8_Data_QC'!AC89
    value = 14.3772864641
    formula = "='Dashboard M4 Price Monthly'!AI115"
    @eval_fn
    def AC89():
        ai115_1 = Dashboard_M4_Price_Monthly.AI115()
        return ai115_1

@register(Metric_4_5_7_8_Data_QC)
class AD89():
    # 'Metric_4_5_7_8_Data_QC'!AD89
    value = 15.6624781295
    formula = "='Dashboard M4 Price Monthly'!AJ115"
    @eval_fn
    def AD89():
        aj115_1 = Dashboard_M4_Price_Monthly.AJ115()
        return aj115_1

@register(Metric_4_5_7_8_Data_QC)
class AE89():
    # 'Metric_4_5_7_8_Data_QC'!AE89
    value = 16.685223477
    formula = "='Dashboard M4 Price Monthly'!AK115"
    @eval_fn
    def AE89():
        ak115_1 = Dashboard_M4_Price_Monthly.AK115()
        return ak115_1

@register(Metric_4_5_7_8_Data_QC)
class AF89():
    # 'Metric_4_5_7_8_Data_QC'!AF89
    value = 18.6163512009
    formula = "='Dashboard M4 Price Monthly'!AL115"
    @eval_fn
    def AF89():
        al115_1 = Dashboard_M4_Price_Monthly.AL115()
        return al115_1

@register(Metric_4_5_7_8_Data_QC)
class AG89():
    # 'Metric_4_5_7_8_Data_QC'!AG89
    value = 20.3079370129
    formula = "='Dashboard M4 Price Monthly'!AM115"
    @eval_fn
    def AG89():
        am115_1 = Dashboard_M4_Price_Monthly.AM115()
        return am115_1

@register(Metric_4_5_7_8_Data_QC)
class AH89():
    # 'Metric_4_5_7_8_Data_QC'!AH89
    value = 22.0637824081
    formula = "='Dashboard M4 Price Monthly'!AN115"
    @eval_fn
    def AH89():
        an115_1 = Dashboard_M4_Price_Monthly.AN115()
        return an115_1

@register(Metric_4_5_7_8_Data_QC)
class AI89():
    # 'Metric_4_5_7_8_Data_QC'!AI89
    value = 21.1968061397
    formula = "='Dashboard M4 Price Monthly'!AO115"
    @eval_fn
    def AI89():
        ao115_1 = Dashboard_M4_Price_Monthly.AO115()
        return ao115_1

@register(Metric_4_5_7_8_Data_QC)
class AJ89():
    # 'Metric_4_5_7_8_Data_QC'!AJ89
    value = 19.8855780659
    formula = "='Dashboard M4 Price Monthly'!AP115"
    @eval_fn
    def AJ89():
        ap115_1 = Dashboard_M4_Price_Monthly.AP115()
        return ap115_1

@register(Metric_4_5_7_8_Data_QC)
class AK89():
    # 'Metric_4_5_7_8_Data_QC'!AK89
    value = 16.1397669954
    formula = "='Dashboard M4 Price Monthly'!AQ115"
    @eval_fn
    def AK89():
        aq115_1 = Dashboard_M4_Price_Monthly.AQ115()
        return aq115_1

@register(Metric_4_5_7_8_Data_QC)
class AL89():
    # 'Metric_4_5_7_8_Data_QC'!AL89
    value = 11.3138221727
    formula = "='Dashboard M4 Price Monthly'!AR115"
    @eval_fn
    def AL89():
        ar115_1 = Dashboard_M4_Price_Monthly.AR115()
        return ar115_1

@register(Metric_4_5_7_8_Data_QC)
class AM89():
    # 'Metric_4_5_7_8_Data_QC'!AM89
    value = 7.85589311277
    formula = "='Dashboard M4 Price Monthly'!AS115"
    @eval_fn
    def AM89():
        as115_1 = Dashboard_M4_Price_Monthly.AS115()
        return as115_1

@register(Metric_4_5_7_8_Data_QC)
class AN89():
    # 'Metric_4_5_7_8_Data_QC'!AN89
    value = 7.56799745507
    formula = "='Dashboard M4 Price Monthly'!AT115"
    @eval_fn
    def AN89():
        at115_1 = Dashboard_M4_Price_Monthly.AT115()
        return at115_1

@register(Metric_4_5_7_8_Data_QC)
class AO89():
    # 'Metric_4_5_7_8_Data_QC'!AO89
    value = 7.35485923334
    formula = "='Dashboard M4 Price Monthly'!AU115"
    @eval_fn
    def AO89():
        au115_1 = Dashboard_M4_Price_Monthly.AU115()
        return au115_1

@register(Metric_4_5_7_8_Data_QC)
class AP89():
    # 'Metric_4_5_7_8_Data_QC'!AP89
    value = 7.2419277875
    formula = "='Dashboard M4 Price Monthly'!AV115"
    @eval_fn
    def AP89():
        av115_1 = Dashboard_M4_Price_Monthly.AV115()
        return av115_1

@register(Metric_4_5_7_8_Data_QC)
class AQ89():
    # 'Metric_4_5_7_8_Data_QC'!AQ89
    value = 7.63321138858
    formula = "='Dashboard M4 Price Monthly'!AW115"
    @eval_fn
    def AQ89():
        aw115_1 = Dashboard_M4_Price_Monthly.AW115()
        return aw115_1

@register(Metric_4_5_7_8_Data_QC)
class AR89():
    # 'Metric_4_5_7_8_Data_QC'!AR89
    value = 8.49530777795
    formula = "='Dashboard M4 Price Monthly'!AX115"
    @eval_fn
    def AR89():
        ax115_1 = Dashboard_M4_Price_Monthly.AX115()
        return ax115_1

@register(Metric_4_5_7_8_Data_QC)
class AS89():
    # 'Metric_4_5_7_8_Data_QC'!AS89
    value = 10.4024176873
    formula = "='Dashboard M4 Price Monthly'!AY115"
    @eval_fn
    def AS89():
        ay115_1 = Dashboard_M4_Price_Monthly.AY115()
        return ay115_1

@register(Metric_4_5_7_8_Data_QC)
class AT89():
    # 'Metric_4_5_7_8_Data_QC'!AT89
    value = 11.4156195324
    formula = "='Dashboard M4 Price Monthly'!AZ115"
    @eval_fn
    def AT89():
        az115_1 = Dashboard_M4_Price_Monthly.AZ115()
        return az115_1

@register(Metric_4_5_7_8_Data_QC)
class AU89():
    # 'Metric_4_5_7_8_Data_QC'!AU89
    value = 12.0820741212
    formula = "='Dashboard M4 Price Monthly'!BA115"
    @eval_fn
    def AU89():
        ba115_1 = Dashboard_M4_Price_Monthly.BA115()
        return ba115_1

@register(Metric_4_5_7_8_Data_QC)
class AV89():
    # 'Metric_4_5_7_8_Data_QC'!AV89
    value = 11.7512327024
    formula = "='Dashboard M4 Price Monthly'!BB115"
    @eval_fn
    def AV89():
        bb115_1 = Dashboard_M4_Price_Monthly.BB115()
        return bb115_1

@register(Metric_4_5_7_8_Data_QC)
class AW89():
    # 'Metric_4_5_7_8_Data_QC'!AW89
    value = 11.7894067123
    formula = "='Dashboard M4 Price Monthly'!BC115"
    @eval_fn
    def AW89():
        bc115_1 = Dashboard_M4_Price_Monthly.BC115()
        return bc115_1

@register(Metric_4_5_7_8_Data_QC)
class AX89():
    # 'Metric_4_5_7_8_Data_QC'!AX89
    value = 12.1119343057
    formula = "='Dashboard M4 Price Monthly'!BD115"
    @eval_fn
    def AX89():
        bd115_1 = Dashboard_M4_Price_Monthly.BD115()
        return bd115_1

@register(Metric_4_5_7_8_Data_QC)
class AY89():
    # 'Metric_4_5_7_8_Data_QC'!AY89
    value = 12.0924994512
    formula = "='Dashboard M4 Price Monthly'!BE115"
    @eval_fn
    def AY89():
        be115_1 = Dashboard_M4_Price_Monthly.BE115()
        return be115_1

@register(Metric_4_5_7_8_Data_QC)
class AZ89():
    # 'Metric_4_5_7_8_Data_QC'!AZ89
    value = 13.4259410339
    formula = "='Dashboard M4 Price Monthly'!BF115"
    @eval_fn
    def AZ89():
        bf115_1 = Dashboard_M4_Price_Monthly.BF115()
        return bf115_1

@register(Metric_4_5_7_8_Data_QC)
class BA89():
    # 'Metric_4_5_7_8_Data_QC'!BA89
    value = 12.9512861237
    formula = "='Dashboard M4 Price Monthly'!BG115"
    @eval_fn
    def BA89():
        bg115_1 = Dashboard_M4_Price_Monthly.BG115()
        return bg115_1

@register(Metric_4_5_7_8_Data_QC)
class BB89():
    # 'Metric_4_5_7_8_Data_QC'!BB89
    value = 13.2229856959
    formula = "='Dashboard M4 Price Monthly'!BH115"
    @eval_fn
    def BB89():
        bh115_1 = Dashboard_M4_Price_Monthly.BH115()
        return bh115_1

@register(Metric_4_5_7_8_Data_QC)
class BC89():
    # 'Metric_4_5_7_8_Data_QC'!BC89
    value = 13.9079423366
    formula = "='Dashboard M4 Price Monthly'!BI115"
    @eval_fn
    def BC89():
        bi115_1 = Dashboard_M4_Price_Monthly.BI115()
        return bi115_1

@register(Metric_4_5_7_8_Data_QC)
class BD89():
    # 'Metric_4_5_7_8_Data_QC'!BD89
    value = 14.2451496193
    formula = "='Dashboard M4 Price Monthly'!BJ115"
    @eval_fn
    def BD89():
        bj115_1 = Dashboard_M4_Price_Monthly.BJ115()
        return bj115_1

@register(Metric_4_5_7_8_Data_QC)
class BE89():
    # 'Metric_4_5_7_8_Data_QC'!BE89
    value = 13.8423488292
    formula = "='Dashboard M4 Price Monthly'!BK115"
    @eval_fn
    def BE89():
        bk115_1 = Dashboard_M4_Price_Monthly.BK115()
        return bk115_1

@register(Metric_4_5_7_8_Data_QC)
class BF89():
    # 'Metric_4_5_7_8_Data_QC'!BF89
    value = 13.6175498867
    formula = "='Dashboard M4 Price Monthly'!BL115"
    @eval_fn
    def BF89():
        bl115_1 = Dashboard_M4_Price_Monthly.BL115()
        return bl115_1

@register(Metric_4_5_7_8_Data_QC)
class BG89():
    # 'Metric_4_5_7_8_Data_QC'!BG89
    value = 13.8582275741
    formula = "='Dashboard M4 Price Monthly'!BM115"
    @eval_fn
    def BG89():
        bm115_1 = Dashboard_M4_Price_Monthly.BM115()
        return bm115_1

@register(Metric_4_5_7_8_Data_QC)
class BH89():
    # 'Metric_4_5_7_8_Data_QC'!BH89
    value = 14.0673890175
    formula = "='Dashboard M4 Price Monthly'!BN115"
    @eval_fn
    def BH89():
        bn115_1 = Dashboard_M4_Price_Monthly.BN115()
        return bn115_1

@register(Metric_4_5_7_8_Data_QC)
class BI89():
    # 'Metric_4_5_7_8_Data_QC'!BI89
    value = 14.3206190154
    formula = "='Dashboard M4 Price Monthly'!BO115"
    @eval_fn
    def BI89():
        bo115_1 = Dashboard_M4_Price_Monthly.BO115()
        return bo115_1

@register(Metric_4_5_7_8_Data_QC)
class BJ89():
    # 'Metric_4_5_7_8_Data_QC'!BJ89
    value = 15.1146787504
    formula = "='Dashboard M4 Price Monthly'!BP115"
    @eval_fn
    def BJ89():
        bp115_1 = Dashboard_M4_Price_Monthly.BP115()
        return bp115_1

@register(Metric_4_5_7_8_Data_QC)
class BK89():
    # 'Metric_4_5_7_8_Data_QC'!BK89
    value = 16.1521867725
    formula = "='Dashboard M4 Price Monthly'!BQ115"
    @eval_fn
    def BK89():
        bq115_1 = Dashboard_M4_Price_Monthly.BQ115()
        return bq115_1

@register(Metric_4_5_7_8_Data_QC)
class BL89():
    # 'Metric_4_5_7_8_Data_QC'!BL89
    value = 14.9919753163
    formula = "='Dashboard M4 Price Monthly'!BR115"
    @eval_fn
    def BL89():
        br115_1 = Dashboard_M4_Price_Monthly.BR115()
        return br115_1

@register(Metric_4_5_7_8_Data_QC)
class BM89():
    # 'Metric_4_5_7_8_Data_QC'!BM89
    value = 18.0231456308
    formula = "='Dashboard M4 Price Monthly'!BS115"
    @eval_fn
    def BM89():
        bs115_1 = Dashboard_M4_Price_Monthly.BS115()
        return bs115_1

@register(Metric_4_5_7_8_Data_QC)
class BN89():
    # 'Metric_4_5_7_8_Data_QC'!BN89
    value = 19.1561297186
    formula = "='Dashboard M4 Price Monthly'!BT115"
    @eval_fn
    def BN89():
        bt115_1 = Dashboard_M4_Price_Monthly.BT115()
        return bt115_1

@register(Metric_4_5_7_8_Data_QC)
class BO89():
    # 'Metric_4_5_7_8_Data_QC'!BO89
    value = 20.243201897
    formula = "='Dashboard M4 Price Monthly'!BU115"
    @eval_fn
    def BO89():
        bu115_1 = Dashboard_M4_Price_Monthly.BU115()
        return bu115_1

@register(Metric_4_5_7_8_Data_QC)
class BP89():
    # 'Metric_4_5_7_8_Data_QC'!BP89
    value = 21.2081423441
    formula = "='Dashboard M4 Price Monthly'!BV115"
    @eval_fn
    def BP89():
        bv115_1 = Dashboard_M4_Price_Monthly.BV115()
        return bv115_1

@register(Metric_4_5_7_8_Data_QC)
class BQ89():
    # 'Metric_4_5_7_8_Data_QC'!BQ89
    value = 20.6247406824
    formula = "='Dashboard M4 Price Monthly'!BW115"
    @eval_fn
    def BQ89():
        bw115_1 = Dashboard_M4_Price_Monthly.BW115()
        return bw115_1

@register(Metric_4_5_7_8_Data_QC)
class BR89():
    # 'Metric_4_5_7_8_Data_QC'!BR89
    value = 21.2167517601
    formula = "='Dashboard M4 Price Monthly'!BX115"
    @eval_fn
    def BR89():
        bx115_1 = Dashboard_M4_Price_Monthly.BX115()
        return bx115_1

@register(Metric_4_5_7_8_Data_QC)
class BS89():
    # 'Metric_4_5_7_8_Data_QC'!BS89
    value = 21.0283390611
    formula = "='Dashboard M4 Price Monthly'!BY115"
    @eval_fn
    def BS89():
        by115_1 = Dashboard_M4_Price_Monthly.BY115()
        return by115_1

@register(Metric_4_5_7_8_Data_QC)
class BT89():
    # 'Metric_4_5_7_8_Data_QC'!BT89
    value = 21.0912103553
    formula = "='Dashboard M4 Price Monthly'!BZ115"
    @eval_fn
    def BT89():
        bz115_1 = Dashboard_M4_Price_Monthly.BZ115()
        return bz115_1

@register(Metric_4_5_7_8_Data_QC)
class BU89():
    # 'Metric_4_5_7_8_Data_QC'!BU89
    value = 20.6299326789
    formula = "='Dashboard M4 Price Monthly'!CA115"
    @eval_fn
    def BU89():
        ca115_1 = Dashboard_M4_Price_Monthly.CA115()
        return ca115_1

@register(Metric_4_5_7_8_Data_QC)
class BV89():
    # 'Metric_4_5_7_8_Data_QC'!BV89
    value = 20.9930609765
    formula = "='Dashboard M4 Price Monthly'!CB115"
    @eval_fn
    def BV89():
        cb115_1 = Dashboard_M4_Price_Monthly.CB115()
        return cb115_1

@register(Metric_4_5_7_8_Data_QC)
class BW89():
    # 'Metric_4_5_7_8_Data_QC'!BW89
    value = 20.90502431
    formula = "='Dashboard M4 Price Monthly'!CC115"
    @eval_fn
    def BW89():
        cc115_1 = Dashboard_M4_Price_Monthly.CC115()
        return cc115_1

@register(Metric_4_5_7_8_Data_QC)
class BX89():
    # 'Metric_4_5_7_8_Data_QC'!BX89
    value = 21.185586725
    formula = "='Dashboard M4 Price Monthly'!CD115"
    @eval_fn
    def BX89():
        cd115_1 = Dashboard_M4_Price_Monthly.CD115()
        return cd115_1

@register(Metric_4_5_7_8_Data_QC)
class BY89():
    # 'Metric_4_5_7_8_Data_QC'!BY89
    value = 22.063667822
    formula = "='Dashboard M4 Price Monthly'!CE115"
    @eval_fn
    def BY89():
        ce115_1 = Dashboard_M4_Price_Monthly.CE115()
        return ce115_1

@register(Metric_4_5_7_8_Data_QC)
class BZ89():
    # 'Metric_4_5_7_8_Data_QC'!BZ89
    value = 22.7955760689
    formula = "='Dashboard M4 Price Monthly'!CF115"
    @eval_fn
    def BZ89():
        cf115_1 = Dashboard_M4_Price_Monthly.CF115()
        return cf115_1

@register(Metric_4_5_7_8_Data_QC)
class CA89():
    # 'Metric_4_5_7_8_Data_QC'!CA89
    value = 23.2238434539
    formula = "='Dashboard M4 Price Monthly'!CG115"
    @eval_fn
    def CA89():
        cg115_1 = Dashboard_M4_Price_Monthly.CG115()
        return cg115_1

@register(Metric_4_5_7_8_Data_QC)
class CB89():
    # 'Metric_4_5_7_8_Data_QC'!CB89
    value = 23.3359201176
    formula = "='Dashboard M4 Price Monthly'!CH115"
    @eval_fn
    def CB89():
        ch115_1 = Dashboard_M4_Price_Monthly.CH115()
        return ch115_1

@register(Metric_4_5_7_8_Data_QC)
class CC89():
    # 'Metric_4_5_7_8_Data_QC'!CC89
    value = 21.9390398045
    formula = "='Dashboard M4 Price Monthly'!CI115"
    @eval_fn
    def CC89():
        ci115_1 = Dashboard_M4_Price_Monthly.CI115()
        return ci115_1

@register(Metric_4_5_7_8_Data_QC)
class CD89():
    # 'Metric_4_5_7_8_Data_QC'!CD89
    value = 20.9105347188
    formula = "='Dashboard M4 Price Monthly'!CJ115"
    @eval_fn
    def CD89():
        cj115_1 = Dashboard_M4_Price_Monthly.CJ115()
        return cj115_1

@register(Metric_4_5_7_8_Data_QC)
class CE89():
    # 'Metric_4_5_7_8_Data_QC'!CE89
    value = 20.8226046709
    formula = "='Dashboard M4 Price Monthly'!CK115"
    @eval_fn
    def CE89():
        ck115_1 = Dashboard_M4_Price_Monthly.CK115()
        return ck115_1

@register(Metric_4_5_7_8_Data_QC)
class B90():
    # 'Metric_4_5_7_8_Data_QC'!B90
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class E90():
    # 'Metric_4_5_7_8_Data_QC'!E90
    value = 33.2172964361
    formula = "='Dashboard M4 Price Monthly'!H116"
    @eval_fn
    def E90():
        h116_1 = Dashboard_M4_Price_Monthly.H116()
        return h116_1

@register(Metric_4_5_7_8_Data_QC)
class F90():
    # 'Metric_4_5_7_8_Data_QC'!F90
    value = 30.8662238876
    formula = "='Dashboard M4 Price Monthly'!I116"
    @eval_fn
    def F90():
        i116_1 = Dashboard_M4_Price_Monthly.I116()
        return i116_1

@register(Metric_4_5_7_8_Data_QC)
class G90():
    # 'Metric_4_5_7_8_Data_QC'!G90
    value = 31.1013311424
    formula = "='Dashboard M4 Price Monthly'!J116"
    @eval_fn
    def G90():
        j116_1 = Dashboard_M4_Price_Monthly.J116()
        return j116_1

@register(Metric_4_5_7_8_Data_QC)
class H90():
    # 'Metric_4_5_7_8_Data_QC'!H90
    value = 34.1241387049
    formula = "='Dashboard M4 Price Monthly'!K116"
    @eval_fn
    def H90():
        k116_1 = Dashboard_M4_Price_Monthly.K116()
        return k116_1

@register(Metric_4_5_7_8_Data_QC)
class I90():
    # 'Metric_4_5_7_8_Data_QC'!I90
    value = 38.2217222895
    formula = "='Dashboard M4 Price Monthly'!O116"
    @eval_fn
    def I90():
        o116_1 = Dashboard_M4_Price_Monthly.O116()
        return o116_1

@register(Metric_4_5_7_8_Data_QC)
class J90():
    # 'Metric_4_5_7_8_Data_QC'!J90
    value = 33.9897917021
    formula = "='Dashboard M4 Price Monthly'!P116"
    @eval_fn
    def J90():
        p116_1 = Dashboard_M4_Price_Monthly.P116()
        return p116_1

@register(Metric_4_5_7_8_Data_QC)
class K90():
    # 'Metric_4_5_7_8_Data_QC'!K90
    value = 31.5043721507
    formula = "='Dashboard M4 Price Monthly'!Q116"
    @eval_fn
    def K90():
        q116_1 = Dashboard_M4_Price_Monthly.Q116()
        return q116_1

@register(Metric_4_5_7_8_Data_QC)
class L90():
    # 'Metric_4_5_7_8_Data_QC'!L90
    value = 32.0417601618
    formula = "='Dashboard M4 Price Monthly'!R116"
    @eval_fn
    def L90():
        r116_1 = Dashboard_M4_Price_Monthly.R116()
        return r116_1

@register(Metric_4_5_7_8_Data_QC)
class M90():
    # 'Metric_4_5_7_8_Data_QC'!M90
    value = 32.4448011702
    formula = "='Dashboard M4 Price Monthly'!S116"
    @eval_fn
    def M90():
        s116_1 = Dashboard_M4_Price_Monthly.S116()
        return s116_1

@register(Metric_4_5_7_8_Data_QC)
class N90():
    # 'Metric_4_5_7_8_Data_QC'!N90
    value = 29.9929683695
    formula = "='Dashboard M4 Price Monthly'!T116"
    @eval_fn
    def N90():
        t116_1 = Dashboard_M4_Price_Monthly.T116()
        return t116_1

@register(Metric_4_5_7_8_Data_QC)
class O90():
    # 'Metric_4_5_7_8_Data_QC'!O90
    value = 32.7470819264
    formula = "='Dashboard M4 Price Monthly'!U116"
    @eval_fn
    def O90():
        u116_1 = Dashboard_M4_Price_Monthly.U116()
        return u116_1

@register(Metric_4_5_7_8_Data_QC)
class P90():
    # 'Metric_4_5_7_8_Data_QC'!P90
    value = 34.8294604694
    formula = "='Dashboard M4 Price Monthly'!V116"
    @eval_fn
    def P90():
        v116_1 = Dashboard_M4_Price_Monthly.V116()
        return v116_1

@register(Metric_4_5_7_8_Data_QC)
class Q90():
    # 'Metric_4_5_7_8_Data_QC'!Q90
    value = 37.2141197687
    formula = "='Dashboard M4 Price Monthly'!W116"
    @eval_fn
    def Q90():
        w116_1 = Dashboard_M4_Price_Monthly.W116()
        return w116_1

@register(Metric_4_5_7_8_Data_QC)
class R90():
    # 'Metric_4_5_7_8_Data_QC'!R90
    value = 38.5911765471
    formula = "='Dashboard M4 Price Monthly'!X116"
    @eval_fn
    def R90():
        x116_1 = Dashboard_M4_Price_Monthly.X116()
        return x116_1

@register(Metric_4_5_7_8_Data_QC)
class S90():
    # 'Metric_4_5_7_8_Data_QC'!S90
    value = 38.2553090402
    formula = "='Dashboard M4 Price Monthly'!Y116"
    @eval_fn
    def S90():
        y116_1 = Dashboard_M4_Price_Monthly.Y116()
        return y116_1

@register(Metric_4_5_7_8_Data_QC)
class T90():
    # 'Metric_4_5_7_8_Data_QC'!T90
    value = 39.9682333256
    formula = "='Dashboard M4 Price Monthly'!Z116"
    @eval_fn
    def T90():
        z116_1 = Dashboard_M4_Price_Monthly.Z116()
        return z116_1

@register(Metric_4_5_7_8_Data_QC)
class U90():
    # 'Metric_4_5_7_8_Data_QC'!U90
    value = 39.8338863228
    formula = "='Dashboard M4 Price Monthly'!AA116"
    @eval_fn
    def U90():
        aa116_1 = Dashboard_M4_Price_Monthly.AA116()
        return aa116_1

@register(Metric_4_5_7_8_Data_QC)
class V90():
    # 'Metric_4_5_7_8_Data_QC'!V90
    value = 43.4948421484
    formula = "='Dashboard M4 Price Monthly'!AB116"
    @eval_fn
    def V90():
        ab116_1 = Dashboard_M4_Price_Monthly.AB116()
        return ab116_1

@register(Metric_4_5_7_8_Data_QC)
class W90():
    # 'Metric_4_5_7_8_Data_QC'!W90
    value = 48.0962269935
    formula = "='Dashboard M4 Price Monthly'!AC116"
    @eval_fn
    def W90():
        ac116_1 = Dashboard_M4_Price_Monthly.AC116()
        return ac116_1

@register(Metric_4_5_7_8_Data_QC)
class X90():
    # 'Metric_4_5_7_8_Data_QC'!X90
    value = 52.2609840795
    formula = "='Dashboard M4 Price Monthly'!AD116"
    @eval_fn
    def X90():
        ad116_1 = Dashboard_M4_Price_Monthly.AD116()
        return ad116_1

@register(Metric_4_5_7_8_Data_QC)
class Y90():
    # 'Metric_4_5_7_8_Data_QC'!Y90
    value = 51.3541418108
    formula = "='Dashboard M4 Price Monthly'!AE116"
    @eval_fn
    def Y90():
        ae116_1 = Dashboard_M4_Price_Monthly.AE116()
        return ae116_1

@register(Metric_4_5_7_8_Data_QC)
class Z90():
    # 'Metric_4_5_7_8_Data_QC'!Z90
    value = 50.5816465448
    formula = "='Dashboard M4 Price Monthly'!AF116"
    @eval_fn
    def Z90():
        af116_1 = Dashboard_M4_Price_Monthly.AF116()
        return af116_1

@register(Metric_4_5_7_8_Data_QC)
class AA90():
    # 'Metric_4_5_7_8_Data_QC'!AA90
    value = 47.8611197386
    formula = "='Dashboard M4 Price Monthly'!AG116"
    @eval_fn
    def AA90():
        ag116_1 = Dashboard_M4_Price_Monthly.AG116()
        return ag116_1

@register(Metric_4_5_7_8_Data_QC)
class AB90():
    # 'Metric_4_5_7_8_Data_QC'!AB90
    value = 49.5404572733
    formula = "='Dashboard M4 Price Monthly'!AH116"
    @eval_fn
    def AB90():
        ah116_1 = Dashboard_M4_Price_Monthly.AH116()
        return ah116_1

@register(Metric_4_5_7_8_Data_QC)
class AC90():
    # 'Metric_4_5_7_8_Data_QC'!AC90
    value = 53.4029336031
    formula = "='Dashboard M4 Price Monthly'!AI116"
    @eval_fn
    def AC90():
        ai116_1 = Dashboard_M4_Price_Monthly.AI116()
        return ai116_1

@register(Metric_4_5_7_8_Data_QC)
class AD90():
    # 'Metric_4_5_7_8_Data_QC'!AD90
    value = 57.0974761794
    formula = "='Dashboard M4 Price Monthly'!AJ116"
    @eval_fn
    def AD90():
        aj116_1 = Dashboard_M4_Price_Monthly.AJ116()
        return aj116_1

@register(Metric_4_5_7_8_Data_QC)
class AE90():
    # 'Metric_4_5_7_8_Data_QC'!AE90
    value = 60.8927790078
    formula = "='Dashboard M4 Price Monthly'!AK116"
    @eval_fn
    def AE90():
        ak116_1 = Dashboard_M4_Price_Monthly.AK116()
        return ak116_1

@register(Metric_4_5_7_8_Data_QC)
class AF90():
    # 'Metric_4_5_7_8_Data_QC'!AF90
    value = 62.5385297918
    formula = "='Dashboard M4 Price Monthly'!AL116"
    @eval_fn
    def AF90():
        al116_1 = Dashboard_M4_Price_Monthly.AL116()
        return al116_1

@register(Metric_4_5_7_8_Data_QC)
class AG90():
    # 'Metric_4_5_7_8_Data_QC'!AG90
    value = 55.4517253954
    formula = "='Dashboard M4 Price Monthly'!AM116"
    @eval_fn
    def AG90():
        am116_1 = Dashboard_M4_Price_Monthly.AM116()
        return am116_1

@register(Metric_4_5_7_8_Data_QC)
class AH90():
    # 'Metric_4_5_7_8_Data_QC'!AH90
    value = 51.3877285615
    formula = "='Dashboard M4 Price Monthly'!AN116"
    @eval_fn
    def AH90():
        an116_1 = Dashboard_M4_Price_Monthly.AN116()
        return an116_1

@register(Metric_4_5_7_8_Data_QC)
class AI90():
    # 'Metric_4_5_7_8_Data_QC'!AI90
    value = 35.098154475
    formula = "='Dashboard M4 Price Monthly'!AO116"
    @eval_fn
    def AI90():
        ao116_1 = Dashboard_M4_Price_Monthly.AO116()
        return ao116_1

@register(Metric_4_5_7_8_Data_QC)
class AJ90():
    # 'Metric_4_5_7_8_Data_QC'!AJ90
    value = 24.787022012
    formula = "='Dashboard M4 Price Monthly'!AP116"
    @eval_fn
    def AJ90():
        ap116_1 = Dashboard_M4_Price_Monthly.AP116()
        return ap116_1

@register(Metric_4_5_7_8_Data_QC)
class AK90():
    # 'Metric_4_5_7_8_Data_QC'!AK90
    value = 20.4879179232
    formula = "='Dashboard M4 Price Monthly'!AQ116"
    @eval_fn
    def AK90():
        aq116_1 = Dashboard_M4_Price_Monthly.AQ116()
        return aq116_1

@register(Metric_4_5_7_8_Data_QC)
class AL90():
    # 'Metric_4_5_7_8_Data_QC'!AL90
    value = 24.4175677544
    formula = "='Dashboard M4 Price Monthly'!AR116"
    @eval_fn
    def AL90():
        ar116_1 = Dashboard_M4_Price_Monthly.AR116()
        return ar116_1

@register(Metric_4_5_7_8_Data_QC)
class AM90():
    # 'Metric_4_5_7_8_Data_QC'!AM90
    value = 22.1336687072
    formula = "='Dashboard M4 Price Monthly'!AS116"
    @eval_fn
    def AM90():
        as116_1 = Dashboard_M4_Price_Monthly.AS116()
        return as116_1

@register(Metric_4_5_7_8_Data_QC)
class AN90():
    # 'Metric_4_5_7_8_Data_QC'!AN90
    value = 21.932148203
    formula = "='Dashboard M4 Price Monthly'!AT116"
    @eval_fn
    def AN90():
        at116_1 = Dashboard_M4_Price_Monthly.AT116()
        return at116_1

@register(Metric_4_5_7_8_Data_QC)
class AO90():
    # 'Metric_4_5_7_8_Data_QC'!AO90
    value = 21.4283469426
    formula = "='Dashboard M4 Price Monthly'!AU116"
    @eval_fn
    def AO90():
        au116_1 = Dashboard_M4_Price_Monthly.AU116()
        return au116_1

@register(Metric_4_5_7_8_Data_QC)
class AP90():
    # 'Metric_4_5_7_8_Data_QC'!AP90
    value = 23.5443122363
    formula = "='Dashboard M4 Price Monthly'!AV116"
    @eval_fn
    def AP90():
        av116_1 = Dashboard_M4_Price_Monthly.AV116()
        return av116_1

@register(Metric_4_5_7_8_Data_QC)
class AQ90():
    # 'Metric_4_5_7_8_Data_QC'!AQ90
    value = 28.4143910869
    formula = "='Dashboard M4 Price Monthly'!AW116"
    @eval_fn
    def AQ90():
        aw116_1 = Dashboard_M4_Price_Monthly.AW116()
        return aw116_1

@register(Metric_4_5_7_8_Data_QC)
class AR90():
    # 'Metric_4_5_7_8_Data_QC'!AR90
    value = 25.2572365217
    formula = "='Dashboard M4 Price Monthly'!AX116"
    @eval_fn
    def AR90():
        ax116_1 = Dashboard_M4_Price_Monthly.AX116()
        return ax116_1

@register(Metric_4_5_7_8_Data_QC)
class AS90():
    # 'Metric_4_5_7_8_Data_QC'!AS90
    value = 30.4295961285
    formula = "='Dashboard M4 Price Monthly'!AY116"
    @eval_fn
    def AS90():
        ay116_1 = Dashboard_M4_Price_Monthly.AY116()
        return ay116_1

@register(Metric_4_5_7_8_Data_QC)
class AT90():
    # 'Metric_4_5_7_8_Data_QC'!AT90
    value = 31.7730661563
    formula = "='Dashboard M4 Price Monthly'!AZ116"
    @eval_fn
    def AT90():
        az116_1 = Dashboard_M4_Price_Monthly.AZ116()
        return az116_1

@register(Metric_4_5_7_8_Data_QC)
class AU90():
    # 'Metric_4_5_7_8_Data_QC'!AU90
    value = 33.8554446993
    formula = "='Dashboard M4 Price Monthly'!BA116"
    @eval_fn
    def AU90():
        ba116_1 = Dashboard_M4_Price_Monthly.BA116()
        return ba116_1

@register(Metric_4_5_7_8_Data_QC)
class AV90():
    # 'Metric_4_5_7_8_Data_QC'!AV90
    value = 36.1393437465
    formula = "='Dashboard M4 Price Monthly'!BB116"
    @eval_fn
    def AV90():
        bb116_1 = Dashboard_M4_Price_Monthly.BB116()
        return bb116_1

@register(Metric_4_5_7_8_Data_QC)
class AW90():
    # 'Metric_4_5_7_8_Data_QC'!AW90
    value = 39.9682333256
    formula = "='Dashboard M4 Price Monthly'!BC116"
    @eval_fn
    def AW90():
        bc116_1 = Dashboard_M4_Price_Monthly.BC116()
        return bc116_1

@register(Metric_4_5_7_8_Data_QC)
class AX90():
    # 'Metric_4_5_7_8_Data_QC'!AX90
    value = 44.0658169102
    formula = "='Dashboard M4 Price Monthly'!BD116"
    @eval_fn
    def AX90():
        bd116_1 = Dashboard_M4_Price_Monthly.BD116()
        return bd116_1

@register(Metric_4_5_7_8_Data_QC)
class AY90():
    # 'Metric_4_5_7_8_Data_QC'!AY90
    value = 43.1253878908
    formula = "='Dashboard M4 Price Monthly'!BE116"
    @eval_fn
    def AY90():
        be116_1 = Dashboard_M4_Price_Monthly.BE116()
        return be116_1

@register(Metric_4_5_7_8_Data_QC)
class AZ90():
    # 'Metric_4_5_7_8_Data_QC'!AZ90
    value = 38.1545487881
    formula = "='Dashboard M4 Price Monthly'!BF116"
    @eval_fn
    def AZ90():
        bf116_1 = Dashboard_M4_Price_Monthly.BF116()
        return bf116_1

@register(Metric_4_5_7_8_Data_QC)
class BA90():
    # 'Metric_4_5_7_8_Data_QC'!BA90
    value = 38.1881355388
    formula = "='Dashboard M4 Price Monthly'!BG116"
    @eval_fn
    def BA90():
        bg116_1 = Dashboard_M4_Price_Monthly.BG116()
        return bg116_1

@register(Metric_4_5_7_8_Data_QC)
class BB90():
    # 'Metric_4_5_7_8_Data_QC'!BB90
    value = 36.3408642506
    formula = "='Dashboard M4 Price Monthly'!BH116"
    @eval_fn
    def BB90():
        bh116_1 = Dashboard_M4_Price_Monthly.BH116()
        return bh116_1

@register(Metric_4_5_7_8_Data_QC)
class BC90():
    # 'Metric_4_5_7_8_Data_QC'!BC90
    value = 34.8294604694
    formula = "='Dashboard M4 Price Monthly'!BI116"
    @eval_fn
    def BC90():
        bi116_1 = Dashboard_M4_Price_Monthly.BI116()
        return bi116_1

@register(Metric_4_5_7_8_Data_QC)
class BD90():
    # 'Metric_4_5_7_8_Data_QC'!BD90
    value = 33.9226182007
    formula = "='Dashboard M4 Price Monthly'!BJ116"
    @eval_fn
    def BD90():
        bj116_1 = Dashboard_M4_Price_Monthly.BJ116()
        return bj116_1

@register(Metric_4_5_7_8_Data_QC)
class BE90():
    # 'Metric_4_5_7_8_Data_QC'!BE90
    value = 36.0049967437
    formula = "='Dashboard M4 Price Monthly'!BK116"
    @eval_fn
    def BE90():
        bk116_1 = Dashboard_M4_Price_Monthly.BK116()
        return bk116_1

@register(Metric_4_5_7_8_Data_QC)
class BF90():
    # 'Metric_4_5_7_8_Data_QC'!BF90
    value = 38.0202017853
    formula = "='Dashboard M4 Price Monthly'!BL116"
    @eval_fn
    def BF90():
        bl116_1 = Dashboard_M4_Price_Monthly.BL116()
        return bl116_1

@register(Metric_4_5_7_8_Data_QC)
class BG90():
    # 'Metric_4_5_7_8_Data_QC'!BG90
    value = 41.4460503561
    formula = "='Dashboard M4 Price Monthly'!BM116"
    @eval_fn
    def BG90():
        bm116_1 = Dashboard_M4_Price_Monthly.BM116()
        return bm116_1

@register(Metric_4_5_7_8_Data_QC)
class BH90():
    # 'Metric_4_5_7_8_Data_QC'!BH90
    value = 42.11778537
    formula = "='Dashboard M4 Price Monthly'!BN116"
    @eval_fn
    def BH90():
        bn116_1 = Dashboard_M4_Price_Monthly.BN116()
        return bn116_1

@register(Metric_4_5_7_8_Data_QC)
class BI90():
    # 'Metric_4_5_7_8_Data_QC'!BI90
    value = 43.5284288991
    formula = "='Dashboard M4 Price Monthly'!BO116"
    @eval_fn
    def BI90():
        bo116_1 = Dashboard_M4_Price_Monthly.BO116()
        return bo116_1

@register(Metric_4_5_7_8_Data_QC)
class BJ90():
    # 'Metric_4_5_7_8_Data_QC'!BJ90
    value = 45.2749399352
    formula = "='Dashboard M4 Price Monthly'!BP116"
    @eval_fn
    def BJ90():
        bp116_1 = Dashboard_M4_Price_Monthly.BP116()
        return bp116_1

@register(Metric_4_5_7_8_Data_QC)
class BK90():
    # 'Metric_4_5_7_8_Data_QC'!BK90
    value = 46.3161292067
    formula = "='Dashboard M4 Price Monthly'!BQ116"
    @eval_fn
    def BK90():
        bq116_1 = Dashboard_M4_Price_Monthly.BQ116()
        return bq116_1

@register(Metric_4_5_7_8_Data_QC)
class BL90():
    # 'Metric_4_5_7_8_Data_QC'!BL90
    value = 46.9206907192
    formula = "='Dashboard M4 Price Monthly'!BR116"
    @eval_fn
    def BL90():
        br116_1 = Dashboard_M4_Price_Monthly.BR116()
        return br116_1

@register(Metric_4_5_7_8_Data_QC)
class BM90():
    # 'Metric_4_5_7_8_Data_QC'!BM90
    value = 48.8351355087
    formula = "='Dashboard M4 Price Monthly'!BS116"
    @eval_fn
    def BM90():
        bs116_1 = Dashboard_M4_Price_Monthly.BS116()
        return bs116_1

@register(Metric_4_5_7_8_Data_QC)
class BN90():
    # 'Metric_4_5_7_8_Data_QC'!BN90
    value = 51.0854478052
    formula = "='Dashboard M4 Price Monthly'!BT116"
    @eval_fn
    def BN90():
        bt116_1 = Dashboard_M4_Price_Monthly.BT116()
        return bt116_1

@register(Metric_4_5_7_8_Data_QC)
class BO90():
    # 'Metric_4_5_7_8_Data_QC'!BO90
    value = 51.0518610545
    formula = "='Dashboard M4 Price Monthly'!BU116"
    @eval_fn
    def BO90():
        bu116_1 = Dashboard_M4_Price_Monthly.BU116()
        return bu116_1

@register(Metric_4_5_7_8_Data_QC)
class BP90():
    # 'Metric_4_5_7_8_Data_QC'!BP90
    value = 51.3205550601
    formula = "='Dashboard M4 Price Monthly'!BV116"
    @eval_fn
    def BP90():
        bv116_1 = Dashboard_M4_Price_Monthly.BV116()
        return bv116_1

@register(Metric_4_5_7_8_Data_QC)
class BQ90():
    # 'Metric_4_5_7_8_Data_QC'!BQ90
    value = 51.3205550601
    formula = "='Dashboard M4 Price Monthly'!BW116"
    @eval_fn
    def BQ90():
        bw116_1 = Dashboard_M4_Price_Monthly.BW116()
        return bw116_1

@register(Metric_4_5_7_8_Data_QC)
class BR90():
    # 'Metric_4_5_7_8_Data_QC'!BR90
    value = 52.3953310823
    formula = "='Dashboard M4 Price Monthly'!BX116"
    @eval_fn
    def BR90():
        bx116_1 = Dashboard_M4_Price_Monthly.BX116()
        return bx116_1

@register(Metric_4_5_7_8_Data_QC)
class BS90():
    # 'Metric_4_5_7_8_Data_QC'!BS90
    value = 49.4396970212
    formula = "='Dashboard M4 Price Monthly'!BY116"
    @eval_fn
    def BS90():
        by116_1 = Dashboard_M4_Price_Monthly.BY116()
        return by116_1

@register(Metric_4_5_7_8_Data_QC)
class BT90():
    # 'Metric_4_5_7_8_Data_QC'!BT90
    value = 48.9694825115
    formula = "='Dashboard M4 Price Monthly'!BZ116"
    @eval_fn
    def BT90():
        bz116_1 = Dashboard_M4_Price_Monthly.BZ116()
        return bz116_1

@register(Metric_4_5_7_8_Data_QC)
class BU90():
    # 'Metric_4_5_7_8_Data_QC'!BU90
    value = 46.8535172178
    formula = "='Dashboard M4 Price Monthly'!CA116"
    @eval_fn
    def BU90():
        ca116_1 = Dashboard_M4_Price_Monthly.CA116()
        return ca116_1

@register(Metric_4_5_7_8_Data_QC)
class BV90():
    # 'Metric_4_5_7_8_Data_QC'!BV90
    value = 43.4612553977
    formula = "='Dashboard M4 Price Monthly'!CB116"
    @eval_fn
    def BV90():
        cb116_1 = Dashboard_M4_Price_Monthly.CB116()
        return cb116_1

@register(Metric_4_5_7_8_Data_QC)
class BW90():
    # 'Metric_4_5_7_8_Data_QC'!BW90
    value = 40.9758358464
    formula = "='Dashboard M4 Price Monthly'!CC116"
    @eval_fn
    def BW90():
        cc116_1 = Dashboard_M4_Price_Monthly.CC116()
        return cc116_1

@register(Metric_4_5_7_8_Data_QC)
class BX90():
    # 'Metric_4_5_7_8_Data_QC'!BX90
    value = 42.3528926248
    formula = "='Dashboard M4 Price Monthly'!CD116"
    @eval_fn
    def BX90():
        cd116_1 = Dashboard_M4_Price_Monthly.CD116()
        return cd116_1

@register(Metric_4_5_7_8_Data_QC)
class BY90():
    # 'Metric_4_5_7_8_Data_QC'!BY90
    value = 40.1697538297
    formula = "='Dashboard M4 Price Monthly'!CE116"
    @eval_fn
    def BY90():
        ce116_1 = Dashboard_M4_Price_Monthly.CE116()
        return ce116_1

@register(Metric_4_5_7_8_Data_QC)
class BZ90():
    # 'Metric_4_5_7_8_Data_QC'!BZ90
    value = 32.0417601618
    formula = "='Dashboard M4 Price Monthly'!CF116"
    @eval_fn
    def BZ90():
        cf116_1 = Dashboard_M4_Price_Monthly.CF116()
        return cf116_1

@register(Metric_4_5_7_8_Data_QC)
class CA90():
    # 'Metric_4_5_7_8_Data_QC'!CA90
    value = 26.4663595467
    formula = "='Dashboard M4 Price Monthly'!CG116"
    @eval_fn
    def CA90():
        cg116_1 = Dashboard_M4_Price_Monthly.CG116()
        return cg116_1

@register(Metric_4_5_7_8_Data_QC)
class CB90():
    # 'Metric_4_5_7_8_Data_QC'!CB90
    value = 29.3548201063
    formula = "='Dashboard M4 Price Monthly'!CH116"
    @eval_fn
    def CB90():
        ch116_1 = Dashboard_M4_Price_Monthly.CH116()
        return ch116_1

@register(Metric_4_5_7_8_Data_QC)
class CC90():
    # 'Metric_4_5_7_8_Data_QC'!CC90
    value = 30.2616623751
    formula = "='Dashboard M4 Price Monthly'!CI116"
    @eval_fn
    def CC90():
        ci116_1 = Dashboard_M4_Price_Monthly.CI116()
        return ci116_1

@register(Metric_4_5_7_8_Data_QC)
class CD90():
    # 'Metric_4_5_7_8_Data_QC'!CD90
    value = 30.5639431313
    formula = "='Dashboard M4 Price Monthly'!CJ116"
    @eval_fn
    def CD90():
        cj116_1 = Dashboard_M4_Price_Monthly.CJ116()
        return cj116_1

@register(Metric_4_5_7_8_Data_QC)
class CE90():
    # 'Metric_4_5_7_8_Data_QC'!CE90
    value = 32.3104541674
    formula = "='Dashboard M4 Price Monthly'!CK116"
    @eval_fn
    def CE90():
        ck116_1 = Dashboard_M4_Price_Monthly.CK116()
        return ck116_1

@register(Metric_4_5_7_8_Data_QC)
class B91():
    # 'Metric_4_5_7_8_Data_QC'!B91
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class E91():
    # 'Metric_4_5_7_8_Data_QC'!E91
    value = 26.3019286205
    formula = "='Dashboard M4 Price Monthly'!H117"
    @eval_fn
    def E91():
        h117_1 = Dashboard_M4_Price_Monthly.H117()
        return h117_1

@register(Metric_4_5_7_8_Data_QC)
class F91():
    # 'Metric_4_5_7_8_Data_QC'!F91
    value = 26.3019286205
    formula = "='Dashboard M4 Price Monthly'!I117"
    @eval_fn
    def F91():
        i117_1 = Dashboard_M4_Price_Monthly.I117()
        return i117_1

@register(Metric_4_5_7_8_Data_QC)
class G91():
    # 'Metric_4_5_7_8_Data_QC'!G91
    value = 26.3019286205
    formula = "='Dashboard M4 Price Monthly'!J117"
    @eval_fn
    def G91():
        j117_1 = Dashboard_M4_Price_Monthly.J117()
        return j117_1

@register(Metric_4_5_7_8_Data_QC)
class H91():
    # 'Metric_4_5_7_8_Data_QC'!H91
    value = 26.3019286205
    formula = "='Dashboard M4 Price Monthly'!K117"
    @eval_fn
    def H91():
        k117_1 = Dashboard_M4_Price_Monthly.K117()
        return k117_1

@register(Metric_4_5_7_8_Data_QC)
class I91():
    # 'Metric_4_5_7_8_Data_QC'!I91
    value = 26.3019286205
    formula = "='Dashboard M4 Price Monthly'!O117"
    @eval_fn
    def I91():
        o117_1 = Dashboard_M4_Price_Monthly.O117()
        return o117_1

@register(Metric_4_5_7_8_Data_QC)
class J91():
    # 'Metric_4_5_7_8_Data_QC'!J91
    value = 26.3019286205
    formula = "='Dashboard M4 Price Monthly'!P117"
    @eval_fn
    def J91():
        p117_1 = Dashboard_M4_Price_Monthly.P117()
        return p117_1

@register(Metric_4_5_7_8_Data_QC)
class K91():
    # 'Metric_4_5_7_8_Data_QC'!K91
    value = 26.3019286205
    formula = "='Dashboard M4 Price Monthly'!Q117"
    @eval_fn
    def K91():
        q117_1 = Dashboard_M4_Price_Monthly.Q117()
        return q117_1

@register(Metric_4_5_7_8_Data_QC)
class L91():
    # 'Metric_4_5_7_8_Data_QC'!L91
    value = 26.3019286205
    formula = "='Dashboard M4 Price Monthly'!R117"
    @eval_fn
    def L91():
        r117_1 = Dashboard_M4_Price_Monthly.R117()
        return r117_1

@register(Metric_4_5_7_8_Data_QC)
class M91():
    # 'Metric_4_5_7_8_Data_QC'!M91
    value = 26.3019286205
    formula = "='Dashboard M4 Price Monthly'!S117"
    @eval_fn
    def M91():
        s117_1 = Dashboard_M4_Price_Monthly.S117()
        return s117_1

@register(Metric_4_5_7_8_Data_QC)
class N91():
    # 'Metric_4_5_7_8_Data_QC'!N91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!T117"
    @eval_fn
    def N91():
        t117_1 = Dashboard_M4_Price_Monthly.T117()
        return t117_1

@register(Metric_4_5_7_8_Data_QC)
class O91():
    # 'Metric_4_5_7_8_Data_QC'!O91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!U117"
    @eval_fn
    def O91():
        u117_1 = Dashboard_M4_Price_Monthly.U117()
        return u117_1

@register(Metric_4_5_7_8_Data_QC)
class P91():
    # 'Metric_4_5_7_8_Data_QC'!P91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!V117"
    @eval_fn
    def P91():
        v117_1 = Dashboard_M4_Price_Monthly.V117()
        return v117_1

@register(Metric_4_5_7_8_Data_QC)
class Q91():
    # 'Metric_4_5_7_8_Data_QC'!Q91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!W117"
    @eval_fn
    def Q91():
        w117_1 = Dashboard_M4_Price_Monthly.W117()
        return w117_1

@register(Metric_4_5_7_8_Data_QC)
class R91():
    # 'Metric_4_5_7_8_Data_QC'!R91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!X117"
    @eval_fn
    def R91():
        x117_1 = Dashboard_M4_Price_Monthly.X117()
        return x117_1

@register(Metric_4_5_7_8_Data_QC)
class S91():
    # 'Metric_4_5_7_8_Data_QC'!S91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!Y117"
    @eval_fn
    def S91():
        y117_1 = Dashboard_M4_Price_Monthly.Y117()
        return y117_1

@register(Metric_4_5_7_8_Data_QC)
class T91():
    # 'Metric_4_5_7_8_Data_QC'!T91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!Z117"
    @eval_fn
    def T91():
        z117_1 = Dashboard_M4_Price_Monthly.Z117()
        return z117_1

@register(Metric_4_5_7_8_Data_QC)
class U91():
    # 'Metric_4_5_7_8_Data_QC'!U91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!AA117"
    @eval_fn
    def U91():
        aa117_1 = Dashboard_M4_Price_Monthly.AA117()
        return aa117_1

@register(Metric_4_5_7_8_Data_QC)
class V91():
    # 'Metric_4_5_7_8_Data_QC'!V91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!AB117"
    @eval_fn
    def V91():
        ab117_1 = Dashboard_M4_Price_Monthly.AB117()
        return ab117_1

@register(Metric_4_5_7_8_Data_QC)
class W91():
    # 'Metric_4_5_7_8_Data_QC'!W91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!AC117"
    @eval_fn
    def W91():
        ac117_1 = Dashboard_M4_Price_Monthly.AC117()
        return ac117_1

@register(Metric_4_5_7_8_Data_QC)
class X91():
    # 'Metric_4_5_7_8_Data_QC'!X91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!AD117"
    @eval_fn
    def X91():
        ad117_1 = Dashboard_M4_Price_Monthly.AD117()
        return ad117_1

@register(Metric_4_5_7_8_Data_QC)
class Y91():
    # 'Metric_4_5_7_8_Data_QC'!Y91
    value = 25.8678958051
    formula = "='Dashboard M4 Price Monthly'!AE117"
    @eval_fn
    def Y91():
        ae117_1 = Dashboard_M4_Price_Monthly.AE117()
        return ae117_1

@register(Metric_4_5_7_8_Data_QC)
class Z91():
    # 'Metric_4_5_7_8_Data_QC'!Z91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AF117"
    @eval_fn
    def Z91():
        af117_1 = Dashboard_M4_Price_Monthly.AF117()
        return af117_1

@register(Metric_4_5_7_8_Data_QC)
class AA91():
    # 'Metric_4_5_7_8_Data_QC'!AA91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AG117"
    @eval_fn
    def AA91():
        ag117_1 = Dashboard_M4_Price_Monthly.AG117()
        return ag117_1

@register(Metric_4_5_7_8_Data_QC)
class AB91():
    # 'Metric_4_5_7_8_Data_QC'!AB91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AH117"
    @eval_fn
    def AB91():
        ah117_1 = Dashboard_M4_Price_Monthly.AH117()
        return ah117_1

@register(Metric_4_5_7_8_Data_QC)
class AC91():
    # 'Metric_4_5_7_8_Data_QC'!AC91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AI117"
    @eval_fn
    def AC91():
        ai117_1 = Dashboard_M4_Price_Monthly.AI117()
        return ai117_1

@register(Metric_4_5_7_8_Data_QC)
class AD91():
    # 'Metric_4_5_7_8_Data_QC'!AD91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AJ117"
    @eval_fn
    def AD91():
        aj117_1 = Dashboard_M4_Price_Monthly.AJ117()
        return aj117_1

@register(Metric_4_5_7_8_Data_QC)
class AE91():
    # 'Metric_4_5_7_8_Data_QC'!AE91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AK117"
    @eval_fn
    def AE91():
        ak117_1 = Dashboard_M4_Price_Monthly.AK117()
        return ak117_1

@register(Metric_4_5_7_8_Data_QC)
class AF91():
    # 'Metric_4_5_7_8_Data_QC'!AF91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AL117"
    @eval_fn
    def AF91():
        al117_1 = Dashboard_M4_Price_Monthly.AL117()
        return al117_1

@register(Metric_4_5_7_8_Data_QC)
class AG91():
    # 'Metric_4_5_7_8_Data_QC'!AG91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AM117"
    @eval_fn
    def AG91():
        am117_1 = Dashboard_M4_Price_Monthly.AM117()
        return am117_1

@register(Metric_4_5_7_8_Data_QC)
class AH91():
    # 'Metric_4_5_7_8_Data_QC'!AH91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AN117"
    @eval_fn
    def AH91():
        an117_1 = Dashboard_M4_Price_Monthly.AN117()
        return an117_1

@register(Metric_4_5_7_8_Data_QC)
class AI91():
    # 'Metric_4_5_7_8_Data_QC'!AI91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AO117"
    @eval_fn
    def AI91():
        ao117_1 = Dashboard_M4_Price_Monthly.AO117()
        return ao117_1

@register(Metric_4_5_7_8_Data_QC)
class AJ91():
    # 'Metric_4_5_7_8_Data_QC'!AJ91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AP117"
    @eval_fn
    def AJ91():
        ap117_1 = Dashboard_M4_Price_Monthly.AP117()
        return ap117_1

@register(Metric_4_5_7_8_Data_QC)
class AK91():
    # 'Metric_4_5_7_8_Data_QC'!AK91
    value = 35.2175115371
    formula = "='Dashboard M4 Price Monthly'!AQ117"
    @eval_fn
    def AK91():
        aq117_1 = Dashboard_M4_Price_Monthly.AQ117()
        return aq117_1

@register(Metric_4_5_7_8_Data_QC)
class AL91():
    # 'Metric_4_5_7_8_Data_QC'!AL91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!AR117"
    @eval_fn
    def AL91():
        ar117_1 = Dashboard_M4_Price_Monthly.AR117()
        return ar117_1

@register(Metric_4_5_7_8_Data_QC)
class AM91():
    # 'Metric_4_5_7_8_Data_QC'!AM91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!AS117"
    @eval_fn
    def AM91():
        as117_1 = Dashboard_M4_Price_Monthly.AS117()
        return as117_1

@register(Metric_4_5_7_8_Data_QC)
class AN91():
    # 'Metric_4_5_7_8_Data_QC'!AN91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!AT117"
    @eval_fn
    def AN91():
        at117_1 = Dashboard_M4_Price_Monthly.AT117()
        return at117_1

@register(Metric_4_5_7_8_Data_QC)
class AO91():
    # 'Metric_4_5_7_8_Data_QC'!AO91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!AU117"
    @eval_fn
    def AO91():
        au117_1 = Dashboard_M4_Price_Monthly.AU117()
        return au117_1

@register(Metric_4_5_7_8_Data_QC)
class AP91():
    # 'Metric_4_5_7_8_Data_QC'!AP91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!AV117"
    @eval_fn
    def AP91():
        av117_1 = Dashboard_M4_Price_Monthly.AV117()
        return av117_1

@register(Metric_4_5_7_8_Data_QC)
class AQ91():
    # 'Metric_4_5_7_8_Data_QC'!AQ91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!AW117"
    @eval_fn
    def AQ91():
        aw117_1 = Dashboard_M4_Price_Monthly.AW117()
        return aw117_1

@register(Metric_4_5_7_8_Data_QC)
class AR91():
    # 'Metric_4_5_7_8_Data_QC'!AR91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!AX117"
    @eval_fn
    def AR91():
        ax117_1 = Dashboard_M4_Price_Monthly.AX117()
        return ax117_1

@register(Metric_4_5_7_8_Data_QC)
class AS91():
    # 'Metric_4_5_7_8_Data_QC'!AS91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!AY117"
    @eval_fn
    def AS91():
        ay117_1 = Dashboard_M4_Price_Monthly.AY117()
        return ay117_1

@register(Metric_4_5_7_8_Data_QC)
class AT91():
    # 'Metric_4_5_7_8_Data_QC'!AT91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!AZ117"
    @eval_fn
    def AT91():
        az117_1 = Dashboard_M4_Price_Monthly.AZ117()
        return az117_1

@register(Metric_4_5_7_8_Data_QC)
class AU91():
    # 'Metric_4_5_7_8_Data_QC'!AU91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!BA117"
    @eval_fn
    def AU91():
        ba117_1 = Dashboard_M4_Price_Monthly.BA117()
        return ba117_1

@register(Metric_4_5_7_8_Data_QC)
class AV91():
    # 'Metric_4_5_7_8_Data_QC'!AV91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!BB117"
    @eval_fn
    def AV91():
        bb117_1 = Dashboard_M4_Price_Monthly.BB117()
        return bb117_1

@register(Metric_4_5_7_8_Data_QC)
class AW91():
    # 'Metric_4_5_7_8_Data_QC'!AW91
    value = 27.7148082596
    formula = "='Dashboard M4 Price Monthly'!BC117"
    @eval_fn
    def AW91():
        bc117_1 = Dashboard_M4_Price_Monthly.BC117()
        return bc117_1

@register(Metric_4_5_7_8_Data_QC)
class AX91():
    # 'Metric_4_5_7_8_Data_QC'!AX91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BD117"
    @eval_fn
    def AX91():
        bd117_1 = Dashboard_M4_Price_Monthly.BD117()
        return bd117_1

@register(Metric_4_5_7_8_Data_QC)
class AY91():
    # 'Metric_4_5_7_8_Data_QC'!AY91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BE117"
    @eval_fn
    def AY91():
        be117_1 = Dashboard_M4_Price_Monthly.BE117()
        return be117_1

@register(Metric_4_5_7_8_Data_QC)
class AZ91():
    # 'Metric_4_5_7_8_Data_QC'!AZ91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BF117"
    @eval_fn
    def AZ91():
        bf117_1 = Dashboard_M4_Price_Monthly.BF117()
        return bf117_1

@register(Metric_4_5_7_8_Data_QC)
class BA91():
    # 'Metric_4_5_7_8_Data_QC'!BA91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BG117"
    @eval_fn
    def BA91():
        bg117_1 = Dashboard_M4_Price_Monthly.BG117()
        return bg117_1

@register(Metric_4_5_7_8_Data_QC)
class BB91():
    # 'Metric_4_5_7_8_Data_QC'!BB91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BH117"
    @eval_fn
    def BB91():
        bh117_1 = Dashboard_M4_Price_Monthly.BH117()
        return bh117_1

@register(Metric_4_5_7_8_Data_QC)
class BC91():
    # 'Metric_4_5_7_8_Data_QC'!BC91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BI117"
    @eval_fn
    def BC91():
        bi117_1 = Dashboard_M4_Price_Monthly.BI117()
        return bi117_1

@register(Metric_4_5_7_8_Data_QC)
class BD91():
    # 'Metric_4_5_7_8_Data_QC'!BD91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BJ117"
    @eval_fn
    def BD91():
        bj117_1 = Dashboard_M4_Price_Monthly.BJ117()
        return bj117_1

@register(Metric_4_5_7_8_Data_QC)
class BE91():
    # 'Metric_4_5_7_8_Data_QC'!BE91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BK117"
    @eval_fn
    def BE91():
        bk117_1 = Dashboard_M4_Price_Monthly.BK117()
        return bk117_1

@register(Metric_4_5_7_8_Data_QC)
class BF91():
    # 'Metric_4_5_7_8_Data_QC'!BF91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BL117"
    @eval_fn
    def BF91():
        bl117_1 = Dashboard_M4_Price_Monthly.BL117()
        return bl117_1

@register(Metric_4_5_7_8_Data_QC)
class BG91():
    # 'Metric_4_5_7_8_Data_QC'!BG91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BM117"
    @eval_fn
    def BG91():
        bm117_1 = Dashboard_M4_Price_Monthly.BM117()
        return bm117_1

@register(Metric_4_5_7_8_Data_QC)
class BH91():
    # 'Metric_4_5_7_8_Data_QC'!BH91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BN117"
    @eval_fn
    def BH91():
        bn117_1 = Dashboard_M4_Price_Monthly.BN117()
        return bn117_1

@register(Metric_4_5_7_8_Data_QC)
class BI91():
    # 'Metric_4_5_7_8_Data_QC'!BI91
    value = 33.9336859444
    formula = "='Dashboard M4 Price Monthly'!BO117"
    @eval_fn
    def BI91():
        bo117_1 = Dashboard_M4_Price_Monthly.BO117()
        return bo117_1

@register(Metric_4_5_7_8_Data_QC)
class BJ91():
    # 'Metric_4_5_7_8_Data_QC'!BJ91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BP117"
    @eval_fn
    def BJ91():
        bp117_1 = Dashboard_M4_Price_Monthly.BP117()
        return bp117_1

@register(Metric_4_5_7_8_Data_QC)
class BK91():
    # 'Metric_4_5_7_8_Data_QC'!BK91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BQ117"
    @eval_fn
    def BK91():
        bq117_1 = Dashboard_M4_Price_Monthly.BQ117()
        return bq117_1

@register(Metric_4_5_7_8_Data_QC)
class BL91():
    # 'Metric_4_5_7_8_Data_QC'!BL91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BR117"
    @eval_fn
    def BL91():
        br117_1 = Dashboard_M4_Price_Monthly.BR117()
        return br117_1

@register(Metric_4_5_7_8_Data_QC)
class BM91():
    # 'Metric_4_5_7_8_Data_QC'!BM91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BS117"
    @eval_fn
    def BM91():
        bs117_1 = Dashboard_M4_Price_Monthly.BS117()
        return bs117_1

@register(Metric_4_5_7_8_Data_QC)
class BN91():
    # 'Metric_4_5_7_8_Data_QC'!BN91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BT117"
    @eval_fn
    def BN91():
        bt117_1 = Dashboard_M4_Price_Monthly.BT117()
        return bt117_1

@register(Metric_4_5_7_8_Data_QC)
class BO91():
    # 'Metric_4_5_7_8_Data_QC'!BO91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BU117"
    @eval_fn
    def BO91():
        bu117_1 = Dashboard_M4_Price_Monthly.BU117()
        return bu117_1

@register(Metric_4_5_7_8_Data_QC)
class BP91():
    # 'Metric_4_5_7_8_Data_QC'!BP91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BV117"
    @eval_fn
    def BP91():
        bv117_1 = Dashboard_M4_Price_Monthly.BV117()
        return bv117_1

@register(Metric_4_5_7_8_Data_QC)
class BQ91():
    # 'Metric_4_5_7_8_Data_QC'!BQ91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BW117"
    @eval_fn
    def BQ91():
        bw117_1 = Dashboard_M4_Price_Monthly.BW117()
        return bw117_1

@register(Metric_4_5_7_8_Data_QC)
class BR91():
    # 'Metric_4_5_7_8_Data_QC'!BR91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BX117"
    @eval_fn
    def BR91():
        bx117_1 = Dashboard_M4_Price_Monthly.BX117()
        return bx117_1

@register(Metric_4_5_7_8_Data_QC)
class BS91():
    # 'Metric_4_5_7_8_Data_QC'!BS91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BY117"
    @eval_fn
    def BS91():
        by117_1 = Dashboard_M4_Price_Monthly.BY117()
        return by117_1

@register(Metric_4_5_7_8_Data_QC)
class BT91():
    # 'Metric_4_5_7_8_Data_QC'!BT91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!BZ117"
    @eval_fn
    def BT91():
        bz117_1 = Dashboard_M4_Price_Monthly.BZ117()
        return bz117_1

@register(Metric_4_5_7_8_Data_QC)
class BU91():
    # 'Metric_4_5_7_8_Data_QC'!BU91
    value = 41.7608382138
    formula = "='Dashboard M4 Price Monthly'!CA117"
    @eval_fn
    def BU91():
        ca117_1 = Dashboard_M4_Price_Monthly.CA117()
        return ca117_1

@register(Metric_4_5_7_8_Data_QC)
class BV91():
    # 'Metric_4_5_7_8_Data_QC'!BV91
    value = 42.4916288433
    formula = "='Dashboard M4 Price Monthly'!CB117"
    @eval_fn
    def BV91():
        cb117_1 = Dashboard_M4_Price_Monthly.CB117()
        return cb117_1

@register(Metric_4_5_7_8_Data_QC)
class BW91():
    # 'Metric_4_5_7_8_Data_QC'!BW91
    value = 42.4916288433
    formula = "='Dashboard M4 Price Monthly'!CC117"
    @eval_fn
    def BW91():
        cc117_1 = Dashboard_M4_Price_Monthly.CC117()
        return cc117_1

@register(Metric_4_5_7_8_Data_QC)
class BX91():
    # 'Metric_4_5_7_8_Data_QC'!BX91
    value = 42.4916288433
    formula = "='Dashboard M4 Price Monthly'!CD117"
    @eval_fn
    def BX91():
        cd117_1 = Dashboard_M4_Price_Monthly.CD117()
        return cd117_1

@register(Metric_4_5_7_8_Data_QC)
class BY91():
    # 'Metric_4_5_7_8_Data_QC'!BY91
    value = 42.4916288433
    formula = "='Dashboard M4 Price Monthly'!CE117"
    @eval_fn
    def BY91():
        ce117_1 = Dashboard_M4_Price_Monthly.CE117()
        return ce117_1

@register(Metric_4_5_7_8_Data_QC)
class BZ91():
    # 'Metric_4_5_7_8_Data_QC'!BZ91
    value = 42.4916288433
    formula = "='Dashboard M4 Price Monthly'!CF117"
    @eval_fn
    def BZ91():
        cf117_1 = Dashboard_M4_Price_Monthly.CF117()
        return cf117_1

@register(Metric_4_5_7_8_Data_QC)
class CA91():
    # 'Metric_4_5_7_8_Data_QC'!CA91
    value = 42.4916288433
    formula = "='Dashboard M4 Price Monthly'!CG117"
    @eval_fn
    def CA91():
        cg117_1 = Dashboard_M4_Price_Monthly.CG117()
        return cg117_1

@register(Metric_4_5_7_8_Data_QC)
class CB91():
    # 'Metric_4_5_7_8_Data_QC'!CB91
    value = 42.4916288433
    formula = "='Dashboard M4 Price Monthly'!CH117"
    @eval_fn
    def CB91():
        ch117_1 = Dashboard_M4_Price_Monthly.CH117()
        return ch117_1

@register(Metric_4_5_7_8_Data_QC)
class CC91():
    # 'Metric_4_5_7_8_Data_QC'!CC91
    value = 42.4916288433
    formula = "='Dashboard M4 Price Monthly'!CI117"
    @eval_fn
    def CC91():
        ci117_1 = Dashboard_M4_Price_Monthly.CI117()
        return ci117_1

@register(Metric_4_5_7_8_Data_QC)
class CD91():
    # 'Metric_4_5_7_8_Data_QC'!CD91
    value = 42.4916288433
    formula = "='Dashboard M4 Price Monthly'!CJ117"
    @eval_fn
    def CD91():
        cj117_1 = Dashboard_M4_Price_Monthly.CJ117()
        return cj117_1

@register(Metric_4_5_7_8_Data_QC)
class CE91():
    # 'Metric_4_5_7_8_Data_QC'!CE91
    value = 42.4916288433
    formula = "='Dashboard M4 Price Monthly'!CK117"
    @eval_fn
    def CE91():
        ck117_1 = Dashboard_M4_Price_Monthly.CK117()
        return ck117_1

@register(Metric_4_5_7_8_Data_QC)
class B92():
    # 'Metric_4_5_7_8_Data_QC'!B92
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class E92():
    # 'Metric_4_5_7_8_Data_QC'!E92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!H118"
    @eval_fn
    def E92():
        h118_1 = Dashboard_M4_Price_Monthly.H118()
        return h118_1

@register(Metric_4_5_7_8_Data_QC)
class F92():
    # 'Metric_4_5_7_8_Data_QC'!F92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!I118"
    @eval_fn
    def F92():
        i118_1 = Dashboard_M4_Price_Monthly.I118()
        return i118_1

@register(Metric_4_5_7_8_Data_QC)
class G92():
    # 'Metric_4_5_7_8_Data_QC'!G92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!J118"
    @eval_fn
    def G92():
        j118_1 = Dashboard_M4_Price_Monthly.J118()
        return j118_1

@register(Metric_4_5_7_8_Data_QC)
class H92():
    # 'Metric_4_5_7_8_Data_QC'!H92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!K118"
    @eval_fn
    def H92():
        k118_1 = Dashboard_M4_Price_Monthly.K118()
        return k118_1

@register(Metric_4_5_7_8_Data_QC)
class I92():
    # 'Metric_4_5_7_8_Data_QC'!I92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!O118"
    @eval_fn
    def I92():
        o118_1 = Dashboard_M4_Price_Monthly.O118()
        return o118_1

@register(Metric_4_5_7_8_Data_QC)
class J92():
    # 'Metric_4_5_7_8_Data_QC'!J92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!P118"
    @eval_fn
    def J92():
        p118_1 = Dashboard_M4_Price_Monthly.P118()
        return p118_1

@register(Metric_4_5_7_8_Data_QC)
class K92():
    # 'Metric_4_5_7_8_Data_QC'!K92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!Q118"
    @eval_fn
    def K92():
        q118_1 = Dashboard_M4_Price_Monthly.Q118()
        return q118_1

@register(Metric_4_5_7_8_Data_QC)
class L92():
    # 'Metric_4_5_7_8_Data_QC'!L92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!R118"
    @eval_fn
    def L92():
        r118_1 = Dashboard_M4_Price_Monthly.R118()
        return r118_1

@register(Metric_4_5_7_8_Data_QC)
class M92():
    # 'Metric_4_5_7_8_Data_QC'!M92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!S118"
    @eval_fn
    def M92():
        s118_1 = Dashboard_M4_Price_Monthly.S118()
        return s118_1

@register(Metric_4_5_7_8_Data_QC)
class N92():
    # 'Metric_4_5_7_8_Data_QC'!N92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!T118"
    @eval_fn
    def N92():
        t118_1 = Dashboard_M4_Price_Monthly.T118()
        return t118_1

@register(Metric_4_5_7_8_Data_QC)
class O92():
    # 'Metric_4_5_7_8_Data_QC'!O92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!U118"
    @eval_fn
    def O92():
        u118_1 = Dashboard_M4_Price_Monthly.U118()
        return u118_1

@register(Metric_4_5_7_8_Data_QC)
class P92():
    # 'Metric_4_5_7_8_Data_QC'!P92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!V118"
    @eval_fn
    def P92():
        v118_1 = Dashboard_M4_Price_Monthly.V118()
        return v118_1

@register(Metric_4_5_7_8_Data_QC)
class Q92():
    # 'Metric_4_5_7_8_Data_QC'!Q92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!W118"
    @eval_fn
    def Q92():
        w118_1 = Dashboard_M4_Price_Monthly.W118()
        return w118_1

@register(Metric_4_5_7_8_Data_QC)
class R92():
    # 'Metric_4_5_7_8_Data_QC'!R92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!X118"
    @eval_fn
    def R92():
        x118_1 = Dashboard_M4_Price_Monthly.X118()
        return x118_1

@register(Metric_4_5_7_8_Data_QC)
class S92():
    # 'Metric_4_5_7_8_Data_QC'!S92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!Y118"
    @eval_fn
    def S92():
        y118_1 = Dashboard_M4_Price_Monthly.Y118()
        return y118_1

@register(Metric_4_5_7_8_Data_QC)
class T92():
    # 'Metric_4_5_7_8_Data_QC'!T92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!Z118"
    @eval_fn
    def T92():
        z118_1 = Dashboard_M4_Price_Monthly.Z118()
        return z118_1

@register(Metric_4_5_7_8_Data_QC)
class U92():
    # 'Metric_4_5_7_8_Data_QC'!U92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AA118"
    @eval_fn
    def U92():
        aa118_1 = Dashboard_M4_Price_Monthly.AA118()
        return aa118_1

@register(Metric_4_5_7_8_Data_QC)
class V92():
    # 'Metric_4_5_7_8_Data_QC'!V92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AB118"
    @eval_fn
    def V92():
        ab118_1 = Dashboard_M4_Price_Monthly.AB118()
        return ab118_1

@register(Metric_4_5_7_8_Data_QC)
class W92():
    # 'Metric_4_5_7_8_Data_QC'!W92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AC118"
    @eval_fn
    def W92():
        ac118_1 = Dashboard_M4_Price_Monthly.AC118()
        return ac118_1

@register(Metric_4_5_7_8_Data_QC)
class X92():
    # 'Metric_4_5_7_8_Data_QC'!X92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AD118"
    @eval_fn
    def X92():
        ad118_1 = Dashboard_M4_Price_Monthly.AD118()
        return ad118_1

@register(Metric_4_5_7_8_Data_QC)
class Y92():
    # 'Metric_4_5_7_8_Data_QC'!Y92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AE118"
    @eval_fn
    def Y92():
        ae118_1 = Dashboard_M4_Price_Monthly.AE118()
        return ae118_1

@register(Metric_4_5_7_8_Data_QC)
class Z92():
    # 'Metric_4_5_7_8_Data_QC'!Z92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AF118"
    @eval_fn
    def Z92():
        af118_1 = Dashboard_M4_Price_Monthly.AF118()
        return af118_1

@register(Metric_4_5_7_8_Data_QC)
class AA92():
    # 'Metric_4_5_7_8_Data_QC'!AA92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AG118"
    @eval_fn
    def AA92():
        ag118_1 = Dashboard_M4_Price_Monthly.AG118()
        return ag118_1

@register(Metric_4_5_7_8_Data_QC)
class AB92():
    # 'Metric_4_5_7_8_Data_QC'!AB92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AH118"
    @eval_fn
    def AB92():
        ah118_1 = Dashboard_M4_Price_Monthly.AH118()
        return ah118_1

@register(Metric_4_5_7_8_Data_QC)
class AC92():
    # 'Metric_4_5_7_8_Data_QC'!AC92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AI118"
    @eval_fn
    def AC92():
        ai118_1 = Dashboard_M4_Price_Monthly.AI118()
        return ai118_1

@register(Metric_4_5_7_8_Data_QC)
class AD92():
    # 'Metric_4_5_7_8_Data_QC'!AD92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AJ118"
    @eval_fn
    def AD92():
        aj118_1 = Dashboard_M4_Price_Monthly.AJ118()
        return aj118_1

@register(Metric_4_5_7_8_Data_QC)
class AE92():
    # 'Metric_4_5_7_8_Data_QC'!AE92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AK118"
    @eval_fn
    def AE92():
        ak118_1 = Dashboard_M4_Price_Monthly.AK118()
        return ak118_1

@register(Metric_4_5_7_8_Data_QC)
class AF92():
    # 'Metric_4_5_7_8_Data_QC'!AF92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AL118"
    @eval_fn
    def AF92():
        al118_1 = Dashboard_M4_Price_Monthly.AL118()
        return al118_1

@register(Metric_4_5_7_8_Data_QC)
class AG92():
    # 'Metric_4_5_7_8_Data_QC'!AG92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AM118"
    @eval_fn
    def AG92():
        am118_1 = Dashboard_M4_Price_Monthly.AM118()
        return am118_1

@register(Metric_4_5_7_8_Data_QC)
class AH92():
    # 'Metric_4_5_7_8_Data_QC'!AH92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AN118"
    @eval_fn
    def AH92():
        an118_1 = Dashboard_M4_Price_Monthly.AN118()
        return an118_1

@register(Metric_4_5_7_8_Data_QC)
class AI92():
    # 'Metric_4_5_7_8_Data_QC'!AI92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AO118"
    @eval_fn
    def AI92():
        ao118_1 = Dashboard_M4_Price_Monthly.AO118()
        return ao118_1

@register(Metric_4_5_7_8_Data_QC)
class AJ92():
    # 'Metric_4_5_7_8_Data_QC'!AJ92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AP118"
    @eval_fn
    def AJ92():
        ap118_1 = Dashboard_M4_Price_Monthly.AP118()
        return ap118_1

@register(Metric_4_5_7_8_Data_QC)
class AK92():
    # 'Metric_4_5_7_8_Data_QC'!AK92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AQ118"
    @eval_fn
    def AK92():
        aq118_1 = Dashboard_M4_Price_Monthly.AQ118()
        return aq118_1

@register(Metric_4_5_7_8_Data_QC)
class AL92():
    # 'Metric_4_5_7_8_Data_QC'!AL92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AR118"
    @eval_fn
    def AL92():
        ar118_1 = Dashboard_M4_Price_Monthly.AR118()
        return ar118_1

@register(Metric_4_5_7_8_Data_QC)
class AM92():
    # 'Metric_4_5_7_8_Data_QC'!AM92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AS118"
    @eval_fn
    def AM92():
        as118_1 = Dashboard_M4_Price_Monthly.AS118()
        return as118_1

@register(Metric_4_5_7_8_Data_QC)
class AN92():
    # 'Metric_4_5_7_8_Data_QC'!AN92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AT118"
    @eval_fn
    def AN92():
        at118_1 = Dashboard_M4_Price_Monthly.AT118()
        return at118_1

@register(Metric_4_5_7_8_Data_QC)
class AO92():
    # 'Metric_4_5_7_8_Data_QC'!AO92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AU118"
    @eval_fn
    def AO92():
        au118_1 = Dashboard_M4_Price_Monthly.AU118()
        return au118_1

@register(Metric_4_5_7_8_Data_QC)
class AP92():
    # 'Metric_4_5_7_8_Data_QC'!AP92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AV118"
    @eval_fn
    def AP92():
        av118_1 = Dashboard_M4_Price_Monthly.AV118()
        return av118_1

@register(Metric_4_5_7_8_Data_QC)
class AQ92():
    # 'Metric_4_5_7_8_Data_QC'!AQ92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AW118"
    @eval_fn
    def AQ92():
        aw118_1 = Dashboard_M4_Price_Monthly.AW118()
        return aw118_1

@register(Metric_4_5_7_8_Data_QC)
class AR92():
    # 'Metric_4_5_7_8_Data_QC'!AR92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AX118"
    @eval_fn
    def AR92():
        ax118_1 = Dashboard_M4_Price_Monthly.AX118()
        return ax118_1

@register(Metric_4_5_7_8_Data_QC)
class AS92():
    # 'Metric_4_5_7_8_Data_QC'!AS92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AY118"
    @eval_fn
    def AS92():
        ay118_1 = Dashboard_M4_Price_Monthly.AY118()
        return ay118_1

@register(Metric_4_5_7_8_Data_QC)
class AT92():
    # 'Metric_4_5_7_8_Data_QC'!AT92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!AZ118"
    @eval_fn
    def AT92():
        az118_1 = Dashboard_M4_Price_Monthly.AZ118()
        return az118_1

@register(Metric_4_5_7_8_Data_QC)
class AU92():
    # 'Metric_4_5_7_8_Data_QC'!AU92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BA118"
    @eval_fn
    def AU92():
        ba118_1 = Dashboard_M4_Price_Monthly.BA118()
        return ba118_1

@register(Metric_4_5_7_8_Data_QC)
class AV92():
    # 'Metric_4_5_7_8_Data_QC'!AV92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BB118"
    @eval_fn
    def AV92():
        bb118_1 = Dashboard_M4_Price_Monthly.BB118()
        return bb118_1

@register(Metric_4_5_7_8_Data_QC)
class AW92():
    # 'Metric_4_5_7_8_Data_QC'!AW92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BC118"
    @eval_fn
    def AW92():
        bc118_1 = Dashboard_M4_Price_Monthly.BC118()
        return bc118_1

@register(Metric_4_5_7_8_Data_QC)
class AX92():
    # 'Metric_4_5_7_8_Data_QC'!AX92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BD118"
    @eval_fn
    def AX92():
        bd118_1 = Dashboard_M4_Price_Monthly.BD118()
        return bd118_1

@register(Metric_4_5_7_8_Data_QC)
class AY92():
    # 'Metric_4_5_7_8_Data_QC'!AY92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BE118"
    @eval_fn
    def AY92():
        be118_1 = Dashboard_M4_Price_Monthly.BE118()
        return be118_1

@register(Metric_4_5_7_8_Data_QC)
class AZ92():
    # 'Metric_4_5_7_8_Data_QC'!AZ92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BF118"
    @eval_fn
    def AZ92():
        bf118_1 = Dashboard_M4_Price_Monthly.BF118()
        return bf118_1

@register(Metric_4_5_7_8_Data_QC)
class BA92():
    # 'Metric_4_5_7_8_Data_QC'!BA92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BG118"
    @eval_fn
    def BA92():
        bg118_1 = Dashboard_M4_Price_Monthly.BG118()
        return bg118_1

@register(Metric_4_5_7_8_Data_QC)
class BB92():
    # 'Metric_4_5_7_8_Data_QC'!BB92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BH118"
    @eval_fn
    def BB92():
        bh118_1 = Dashboard_M4_Price_Monthly.BH118()
        return bh118_1

@register(Metric_4_5_7_8_Data_QC)
class BC92():
    # 'Metric_4_5_7_8_Data_QC'!BC92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BI118"
    @eval_fn
    def BC92():
        bi118_1 = Dashboard_M4_Price_Monthly.BI118()
        return bi118_1

@register(Metric_4_5_7_8_Data_QC)
class BD92():
    # 'Metric_4_5_7_8_Data_QC'!BD92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BJ118"
    @eval_fn
    def BD92():
        bj118_1 = Dashboard_M4_Price_Monthly.BJ118()
        return bj118_1

@register(Metric_4_5_7_8_Data_QC)
class BE92():
    # 'Metric_4_5_7_8_Data_QC'!BE92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BK118"
    @eval_fn
    def BE92():
        bk118_1 = Dashboard_M4_Price_Monthly.BK118()
        return bk118_1

@register(Metric_4_5_7_8_Data_QC)
class BF92():
    # 'Metric_4_5_7_8_Data_QC'!BF92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BL118"
    @eval_fn
    def BF92():
        bl118_1 = Dashboard_M4_Price_Monthly.BL118()
        return bl118_1

@register(Metric_4_5_7_8_Data_QC)
class BG92():
    # 'Metric_4_5_7_8_Data_QC'!BG92
    value = 41.2135914095
    formula = "='Dashboard M4 Price Monthly'!BM118"
    @eval_fn
    def BG92():
        bm118_1 = Dashboard_M4_Price_Monthly.BM118()
        return bm118_1

@register(Metric_4_5_7_8_Data_QC)
class BH92():
    # 'Metric_4_5_7_8_Data_QC'!BH92
    value = 0
    formula = "='Dashboard M4 Price Monthly'!BN118"
    @eval_fn
    def BH92():
        bn118_1 = Dashboard_M4_Price_Monthly.BN118()
        return bn118_1

@register(Metric_4_5_7_8_Data_QC)
class BI92():
    # 'Metric_4_5_7_8_Data_QC'!BI92
    value = 43.1456932786
    formula = "='Dashboard M4 Price Monthly'!BO118"
    @eval_fn
    def BI92():
        bo118_1 = Dashboard_M4_Price_Monthly.BO118()
        return bo118_1

@register(Metric_4_5_7_8_Data_QC)
class BJ92():
    # 'Metric_4_5_7_8_Data_QC'!BJ92
    value = 41.8382564343
    formula = "='Dashboard M4 Price Monthly'!BP118"
    @eval_fn
    def BJ92():
        bp118_1 = Dashboard_M4_Price_Monthly.BP118()
        return bp118_1

@register(Metric_4_5_7_8_Data_QC)
class BK92():
    # 'Metric_4_5_7_8_Data_QC'!BK92
    value = 31.380949689
    formula = "='Dashboard M4 Price Monthly'!BQ118"
    @eval_fn
    def BK92():
        bq118_1 = Dashboard_M4_Price_Monthly.BQ118()
        return bq118_1

@register(Metric_4_5_7_8_Data_QC)
class BL92():
    # 'Metric_4_5_7_8_Data_QC'!BL92
    value = 31.4462401423
    formula = "='Dashboard M4 Price Monthly'!BR118"
    @eval_fn
    def BL92():
        br118_1 = Dashboard_M4_Price_Monthly.BR118()
        return br118_1

@register(Metric_4_5_7_8_Data_QC)
class BM92():
    # 'Metric_4_5_7_8_Data_QC'!BM92
    value = 35.8646486169
    formula = "='Dashboard M4 Price Monthly'!BS118"
    @eval_fn
    def BM92():
        bs118_1 = Dashboard_M4_Price_Monthly.BS118()
        return bs118_1

@register(Metric_4_5_7_8_Data_QC)
class BN92():
    # 'Metric_4_5_7_8_Data_QC'!BN92
    value = 18.910604953
    formula = "='Dashboard M4 Price Monthly'!BT118"
    @eval_fn
    def BN92():
        bt118_1 = Dashboard_M4_Price_Monthly.BT118()
        return bt118_1

@register(Metric_4_5_7_8_Data_QC)
class BO92():
    # 'Metric_4_5_7_8_Data_QC'!BO92
    value = 29.8140923054
    formula = "='Dashboard M4 Price Monthly'!BU118"
    @eval_fn
    def BO92():
        bu118_1 = Dashboard_M4_Price_Monthly.BU118()
        return bu118_1

@register(Metric_4_5_7_8_Data_QC)
class BP92():
    # 'Metric_4_5_7_8_Data_QC'!BP92
    value = 32.8161218308
    formula = "='Dashboard M4 Price Monthly'!BV118"
    @eval_fn
    def BP92():
        bv118_1 = Dashboard_M4_Price_Monthly.BV118()
        return bv118_1

@register(Metric_4_5_7_8_Data_QC)
class BQ92():
    # 'Metric_4_5_7_8_Data_QC'!BQ92
    value = 36.704459036
    formula = "='Dashboard M4 Price Monthly'!BW118"
    @eval_fn
    def BQ92():
        bw118_1 = Dashboard_M4_Price_Monthly.BW118()
        return bw118_1

@register(Metric_4_5_7_8_Data_QC)
class BR92():
    # 'Metric_4_5_7_8_Data_QC'!BR92
    value = 48.5317449533
    formula = "='Dashboard M4 Price Monthly'!BX118"
    @eval_fn
    def BR92():
        bx118_1 = Dashboard_M4_Price_Monthly.BX118()
        return bx118_1

@register(Metric_4_5_7_8_Data_QC)
class BS92():
    # 'Metric_4_5_7_8_Data_QC'!BS92
    value = 104.350101291
    formula = "='Dashboard M4 Price Monthly'!BY118"
    @eval_fn
    def BS92():
        by118_1 = Dashboard_M4_Price_Monthly.BY118()
        return by118_1

@register(Metric_4_5_7_8_Data_QC)
class BT92():
    # 'Metric_4_5_7_8_Data_QC'!BT92
    value = 72.9301307081
    formula = "='Dashboard M4 Price Monthly'!BZ118"
    @eval_fn
    def BT92():
        bz118_1 = Dashboard_M4_Price_Monthly.BZ118()
        return bz118_1

@register(Metric_4_5_7_8_Data_QC)
class BU92():
    # 'Metric_4_5_7_8_Data_QC'!BU92
    value = 102.886543514
    formula = "='Dashboard M4 Price Monthly'!CA118"
    @eval_fn
    def BU92():
        ca118_1 = Dashboard_M4_Price_Monthly.CA118()
        return ca118_1

@register(Metric_4_5_7_8_Data_QC)
class BV92():
    # 'Metric_4_5_7_8_Data_QC'!BV92
    value = 44.886895709
    formula = "='Dashboard M4 Price Monthly'!CB118"
    @eval_fn
    def BV92():
        cb118_1 = Dashboard_M4_Price_Monthly.CB118()
        return cb118_1

@register(Metric_4_5_7_8_Data_QC)
class BW92():
    # 'Metric_4_5_7_8_Data_QC'!BW92
    value = 45.3069899675
    formula = "='Dashboard M4 Price Monthly'!CC118"
    @eval_fn
    def BW92():
        cc118_1 = Dashboard_M4_Price_Monthly.CC118()
        return cc118_1

@register(Metric_4_5_7_8_Data_QC)
class BX92():
    # 'Metric_4_5_7_8_Data_QC'!BX92
    value = 46.4984199484
    formula = "='Dashboard M4 Price Monthly'!CD118"
    @eval_fn
    def BX92():
        cd118_1 = Dashboard_M4_Price_Monthly.CD118()
        return cd118_1

@register(Metric_4_5_7_8_Data_QC)
class BY92():
    # 'Metric_4_5_7_8_Data_QC'!BY92
    value = 47.2256830276
    formula = "='Dashboard M4 Price Monthly'!CE118"
    @eval_fn
    def BY92():
        ce118_1 = Dashboard_M4_Price_Monthly.CE118()
        return ce118_1

@register(Metric_4_5_7_8_Data_QC)
class BZ92():
    # 'Metric_4_5_7_8_Data_QC'!BZ92
    value = 47.410443915
    formula = "='Dashboard M4 Price Monthly'!CF118"
    @eval_fn
    def BZ92():
        cf118_1 = Dashboard_M4_Price_Monthly.CF118()
        return cf118_1

@register(Metric_4_5_7_8_Data_QC)
class CA92():
    # 'Metric_4_5_7_8_Data_QC'!CA92
    value = 47.5419411984
    formula = "='Dashboard M4 Price Monthly'!CG118"
    @eval_fn
    def CA92():
        cg118_1 = Dashboard_M4_Price_Monthly.CG118()
        return cg118_1

@register(Metric_4_5_7_8_Data_QC)
class CB92():
    # 'Metric_4_5_7_8_Data_QC'!CB92
    value = 48.1800784425
    formula = "='Dashboard M4 Price Monthly'!CH118"
    @eval_fn
    def CB92():
        ch118_1 = Dashboard_M4_Price_Monthly.CH118()
        return ch118_1

@register(Metric_4_5_7_8_Data_QC)
class CC92():
    # 'Metric_4_5_7_8_Data_QC'!CC92
    value = 50.0320213266
    formula = "='Dashboard M4 Price Monthly'!CI118"
    @eval_fn
    def CC92():
        ci118_1 = Dashboard_M4_Price_Monthly.CI118()
        return ci118_1

@register(Metric_4_5_7_8_Data_QC)
class CD92():
    # 'Metric_4_5_7_8_Data_QC'!CD92
    value = 48.0739819321
    formula = "='Dashboard M4 Price Monthly'!CJ118"
    @eval_fn
    def CD92():
        cj118_1 = Dashboard_M4_Price_Monthly.CJ118()
        return cj118_1

@register(Metric_4_5_7_8_Data_QC)
class CE92():
    # 'Metric_4_5_7_8_Data_QC'!CE92
    value = 48.4266352535
    formula = "='Dashboard M4 Price Monthly'!CK118"
    @eval_fn
    def CE92():
        ck118_1 = Dashboard_M4_Price_Monthly.CK118()
        return ck118_1

@register(Metric_4_5_7_8_Data_QC)
class B93():
    # 'Metric_4_5_7_8_Data_QC'!B93
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class E93():
    # 'Metric_4_5_7_8_Data_QC'!E93
    value = 32.7885425442
    formula = "='Dashboard M4 Price Monthly'!H119"
    @eval_fn
    def E93():
        h119_1 = Dashboard_M4_Price_Monthly.H119()
        return h119_1

@register(Metric_4_5_7_8_Data_QC)
class F93():
    # 'Metric_4_5_7_8_Data_QC'!F93
    value = 32.7885425442
    formula = "='Dashboard M4 Price Monthly'!I119"
    @eval_fn
    def F93():
        i119_1 = Dashboard_M4_Price_Monthly.I119()
        return i119_1

@register(Metric_4_5_7_8_Data_QC)
class G93():
    # 'Metric_4_5_7_8_Data_QC'!G93
    value = 32.7885425442
    formula = "='Dashboard M4 Price Monthly'!J119"
    @eval_fn
    def G93():
        j119_1 = Dashboard_M4_Price_Monthly.J119()
        return j119_1

@register(Metric_4_5_7_8_Data_QC)
class H93():
    # 'Metric_4_5_7_8_Data_QC'!H93
    value = 32.7885425442
    formula = "='Dashboard M4 Price Monthly'!K119"
    @eval_fn
    def H93():
        k119_1 = Dashboard_M4_Price_Monthly.K119()
        return k119_1

@register(Metric_4_5_7_8_Data_QC)
class I93():
    # 'Metric_4_5_7_8_Data_QC'!I93
    value = 24.5324347094
    formula = "='Dashboard M4 Price Monthly'!O119"
    @eval_fn
    def I93():
        o119_1 = Dashboard_M4_Price_Monthly.O119()
        return o119_1

@register(Metric_4_5_7_8_Data_QC)
class J93():
    # 'Metric_4_5_7_8_Data_QC'!J93
    value = 24.5324347094
    formula = "='Dashboard M4 Price Monthly'!P119"
    @eval_fn
    def J93():
        p119_1 = Dashboard_M4_Price_Monthly.P119()
        return p119_1

@register(Metric_4_5_7_8_Data_QC)
class K93():
    # 'Metric_4_5_7_8_Data_QC'!K93
    value = 24.5324347094
    formula = "='Dashboard M4 Price Monthly'!Q119"
    @eval_fn
    def K93():
        q119_1 = Dashboard_M4_Price_Monthly.Q119()
        return q119_1

@register(Metric_4_5_7_8_Data_QC)
class L93():
    # 'Metric_4_5_7_8_Data_QC'!L93
    value = 23.7068239259
    formula = "='Dashboard M4 Price Monthly'!R119"
    @eval_fn
    def L93():
        r119_1 = Dashboard_M4_Price_Monthly.R119()
        return r119_1

@register(Metric_4_5_7_8_Data_QC)
class M93():
    # 'Metric_4_5_7_8_Data_QC'!M93
    value = 23.7068239259
    formula = "='Dashboard M4 Price Monthly'!S119"
    @eval_fn
    def M93():
        s119_1 = Dashboard_M4_Price_Monthly.S119()
        return s119_1

@register(Metric_4_5_7_8_Data_QC)
class N93():
    # 'Metric_4_5_7_8_Data_QC'!N93
    value = 23.7068239259
    formula = "='Dashboard M4 Price Monthly'!T119"
    @eval_fn
    def N93():
        t119_1 = Dashboard_M4_Price_Monthly.T119()
        return t119_1

@register(Metric_4_5_7_8_Data_QC)
class O93():
    # 'Metric_4_5_7_8_Data_QC'!O93
    value = 23.7068239259
    formula = "='Dashboard M4 Price Monthly'!U119"
    @eval_fn
    def O93():
        u119_1 = Dashboard_M4_Price_Monthly.U119()
        return u119_1

@register(Metric_4_5_7_8_Data_QC)
class P93():
    # 'Metric_4_5_7_8_Data_QC'!P93
    value = 23.7068239259
    formula = "='Dashboard M4 Price Monthly'!V119"
    @eval_fn
    def P93():
        v119_1 = Dashboard_M4_Price_Monthly.V119()
        return v119_1

@register(Metric_4_5_7_8_Data_QC)
class Q93():
    # 'Metric_4_5_7_8_Data_QC'!Q93
    value = 30.547598989
    formula = "='Dashboard M4 Price Monthly'!W119"
    @eval_fn
    def Q93():
        w119_1 = Dashboard_M4_Price_Monthly.W119()
        return w119_1

@register(Metric_4_5_7_8_Data_QC)
class R93():
    # 'Metric_4_5_7_8_Data_QC'!R93
    value = 30.547598989
    formula = "='Dashboard M4 Price Monthly'!X119"
    @eval_fn
    def R93():
        x119_1 = Dashboard_M4_Price_Monthly.X119()
        return x119_1

@register(Metric_4_5_7_8_Data_QC)
class S93():
    # 'Metric_4_5_7_8_Data_QC'!S93
    value = 30.547598989
    formula = "='Dashboard M4 Price Monthly'!Y119"
    @eval_fn
    def S93():
        y119_1 = Dashboard_M4_Price_Monthly.Y119()
        return y119_1

@register(Metric_4_5_7_8_Data_QC)
class T93():
    # 'Metric_4_5_7_8_Data_QC'!T93
    value = 30.547598989
    formula = "='Dashboard M4 Price Monthly'!Z119"
    @eval_fn
    def T93():
        z119_1 = Dashboard_M4_Price_Monthly.Z119()
        return z119_1

@register(Metric_4_5_7_8_Data_QC)
class U93():
    # 'Metric_4_5_7_8_Data_QC'!U93
    value = 30.1937657961
    formula = "='Dashboard M4 Price Monthly'!AA119"
    @eval_fn
    def U93():
        aa119_1 = Dashboard_M4_Price_Monthly.AA119()
        return aa119_1

@register(Metric_4_5_7_8_Data_QC)
class V93():
    # 'Metric_4_5_7_8_Data_QC'!V93
    value = 30.1937657961
    formula = "='Dashboard M4 Price Monthly'!AB119"
    @eval_fn
    def V93():
        ab119_1 = Dashboard_M4_Price_Monthly.AB119()
        return ab119_1

@register(Metric_4_5_7_8_Data_QC)
class W93():
    # 'Metric_4_5_7_8_Data_QC'!W93
    value = 30.1937657961
    formula = "='Dashboard M4 Price Monthly'!AC119"
    @eval_fn
    def W93():
        ac119_1 = Dashboard_M4_Price_Monthly.AC119()
        return ac119_1

@register(Metric_4_5_7_8_Data_QC)
class X93():
    # 'Metric_4_5_7_8_Data_QC'!X93
    value = 30.7834877843
    formula = "='Dashboard M4 Price Monthly'!AD119"
    @eval_fn
    def X93():
        ad119_1 = Dashboard_M4_Price_Monthly.AD119()
        return ad119_1

@register(Metric_4_5_7_8_Data_QC)
class Y93():
    # 'Metric_4_5_7_8_Data_QC'!Y93
    value = 30.7834877843
    formula = "='Dashboard M4 Price Monthly'!AE119"
    @eval_fn
    def Y93():
        ae119_1 = Dashboard_M4_Price_Monthly.AE119()
        return ae119_1

@register(Metric_4_5_7_8_Data_QC)
class Z93():
    # 'Metric_4_5_7_8_Data_QC'!Z93
    value = 30.7834877843
    formula = "='Dashboard M4 Price Monthly'!AF119"
    @eval_fn
    def Z93():
        af119_1 = Dashboard_M4_Price_Monthly.AF119()
        return af119_1

@register(Metric_4_5_7_8_Data_QC)
class AA93():
    # 'Metric_4_5_7_8_Data_QC'!AA93
    value = 35.7371524853
    formula = "='Dashboard M4 Price Monthly'!AG119"
    @eval_fn
    def AA93():
        ag119_1 = Dashboard_M4_Price_Monthly.AG119()
        return ag119_1

@register(Metric_4_5_7_8_Data_QC)
class AB93():
    # 'Metric_4_5_7_8_Data_QC'!AB93
    value = 35.7371524853
    formula = "='Dashboard M4 Price Monthly'!AH119"
    @eval_fn
    def AB93():
        ah119_1 = Dashboard_M4_Price_Monthly.AH119()
        return ah119_1

@register(Metric_4_5_7_8_Data_QC)
class AC93():
    # 'Metric_4_5_7_8_Data_QC'!AC93
    value = 35.7371524853
    formula = "='Dashboard M4 Price Monthly'!AI119"
    @eval_fn
    def AC93():
        ai119_1 = Dashboard_M4_Price_Monthly.AI119()
        return ai119_1

@register(Metric_4_5_7_8_Data_QC)
class AD93():
    # 'Metric_4_5_7_8_Data_QC'!AD93
    value = 39.9831508003
    formula = "='Dashboard M4 Price Monthly'!AJ119"
    @eval_fn
    def AD93():
        aj119_1 = Dashboard_M4_Price_Monthly.AJ119()
        return aj119_1

@register(Metric_4_5_7_8_Data_QC)
class AE93():
    # 'Metric_4_5_7_8_Data_QC'!AE93
    value = 39.9831508003
    formula = "='Dashboard M4 Price Monthly'!AK119"
    @eval_fn
    def AE93():
        ak119_1 = Dashboard_M4_Price_Monthly.AK119()
        return ak119_1

@register(Metric_4_5_7_8_Data_QC)
class AF93():
    # 'Metric_4_5_7_8_Data_QC'!AF93
    value = 39.9831508003
    formula = "='Dashboard M4 Price Monthly'!AL119"
    @eval_fn
    def AF93():
        al119_1 = Dashboard_M4_Price_Monthly.AL119()
        return al119_1

@register(Metric_4_5_7_8_Data_QC)
class AG93():
    # 'Metric_4_5_7_8_Data_QC'!AG93
    value = 33.7320977254
    formula = "='Dashboard M4 Price Monthly'!AM119"
    @eval_fn
    def AG93():
        am119_1 = Dashboard_M4_Price_Monthly.AM119()
        return am119_1

@register(Metric_4_5_7_8_Data_QC)
class AH93():
    # 'Metric_4_5_7_8_Data_QC'!AH93
    value = 33.7320977254
    formula = "='Dashboard M4 Price Monthly'!AN119"
    @eval_fn
    def AH93():
        an119_1 = Dashboard_M4_Price_Monthly.AN119()
        return an119_1

@register(Metric_4_5_7_8_Data_QC)
class AI93():
    # 'Metric_4_5_7_8_Data_QC'!AI93
    value = 33.7320977254
    formula = "='Dashboard M4 Price Monthly'!AO119"
    @eval_fn
    def AI93():
        ao119_1 = Dashboard_M4_Price_Monthly.AO119()
        return ao119_1

@register(Metric_4_5_7_8_Data_QC)
class AJ93():
    # 'Metric_4_5_7_8_Data_QC'!AJ93
    value = 20.8761583825
    formula = "='Dashboard M4 Price Monthly'!AP119"
    @eval_fn
    def AJ93():
        ap119_1 = Dashboard_M4_Price_Monthly.AP119()
        return ap119_1

@register(Metric_4_5_7_8_Data_QC)
class AK93():
    # 'Metric_4_5_7_8_Data_QC'!AK93
    value = 20.8761583825
    formula = "='Dashboard M4 Price Monthly'!AQ119"
    @eval_fn
    def AK93():
        aq119_1 = Dashboard_M4_Price_Monthly.AQ119()
        return aq119_1

@register(Metric_4_5_7_8_Data_QC)
class AL93():
    # 'Metric_4_5_7_8_Data_QC'!AL93
    value = 20.8761583825
    formula = "='Dashboard M4 Price Monthly'!AR119"
    @eval_fn
    def AL93():
        ar119_1 = Dashboard_M4_Price_Monthly.AR119()
        return ar119_1

@register(Metric_4_5_7_8_Data_QC)
class AM93():
    # 'Metric_4_5_7_8_Data_QC'!AM93
    value = 20.4043807919
    formula = "='Dashboard M4 Price Monthly'!AS119"
    @eval_fn
    def AM93():
        as119_1 = Dashboard_M4_Price_Monthly.AS119()
        return as119_1

@register(Metric_4_5_7_8_Data_QC)
class AN93():
    # 'Metric_4_5_7_8_Data_QC'!AN93
    value = 20.4043807919
    formula = "='Dashboard M4 Price Monthly'!AT119"
    @eval_fn
    def AN93():
        at119_1 = Dashboard_M4_Price_Monthly.AT119()
        return at119_1

@register(Metric_4_5_7_8_Data_QC)
class AO93():
    # 'Metric_4_5_7_8_Data_QC'!AO93
    value = 20.4043807919
    formula = "='Dashboard M4 Price Monthly'!AU119"
    @eval_fn
    def AO93():
        au119_1 = Dashboard_M4_Price_Monthly.AU119()
        return au119_1

@register(Metric_4_5_7_8_Data_QC)
class AP93():
    # 'Metric_4_5_7_8_Data_QC'!AP93
    value = 23.7068239259
    formula = "='Dashboard M4 Price Monthly'!AV119"
    @eval_fn
    def AP93():
        av119_1 = Dashboard_M4_Price_Monthly.AV119()
        return av119_1

@register(Metric_4_5_7_8_Data_QC)
class AQ93():
    # 'Metric_4_5_7_8_Data_QC'!AQ93
    value = 23.7068239259
    formula = "='Dashboard M4 Price Monthly'!AW119"
    @eval_fn
    def AQ93():
        aw119_1 = Dashboard_M4_Price_Monthly.AW119()
        return aw119_1

@register(Metric_4_5_7_8_Data_QC)
class AR93():
    # 'Metric_4_5_7_8_Data_QC'!AR93
    value = 23.7068239259
    formula = "='Dashboard M4 Price Monthly'!AX119"
    @eval_fn
    def AR93():
        ax119_1 = Dashboard_M4_Price_Monthly.AX119()
        return ax119_1

@register(Metric_4_5_7_8_Data_QC)
class AS93():
    # 'Metric_4_5_7_8_Data_QC'!AS93
    value = 25.5939342881
    formula = "='Dashboard M4 Price Monthly'!AY119"
    @eval_fn
    def AS93():
        ay119_1 = Dashboard_M4_Price_Monthly.AY119()
        return ay119_1

@register(Metric_4_5_7_8_Data_QC)
class AT93():
    # 'Metric_4_5_7_8_Data_QC'!AT93
    value = 25.5939342881
    formula = "='Dashboard M4 Price Monthly'!AZ119"
    @eval_fn
    def AT93():
        az119_1 = Dashboard_M4_Price_Monthly.AZ119()
        return az119_1

@register(Metric_4_5_7_8_Data_QC)
class AU93():
    # 'Metric_4_5_7_8_Data_QC'!AU93
    value = 25.5939342881
    formula = "='Dashboard M4 Price Monthly'!BA119"
    @eval_fn
    def AU93():
        ba119_1 = Dashboard_M4_Price_Monthly.BA119()
        return ba119_1

@register(Metric_4_5_7_8_Data_QC)
class AV93():
    # 'Metric_4_5_7_8_Data_QC'!AV93
    value = 28.0707666386
    formula = "='Dashboard M4 Price Monthly'!BB119"
    @eval_fn
    def AV93():
        bb119_1 = Dashboard_M4_Price_Monthly.BB119()
        return bb119_1

@register(Metric_4_5_7_8_Data_QC)
class AW93():
    # 'Metric_4_5_7_8_Data_QC'!AW93
    value = 28.0707666386
    formula = "='Dashboard M4 Price Monthly'!BC119"
    @eval_fn
    def AW93():
        bc119_1 = Dashboard_M4_Price_Monthly.BC119()
        return bc119_1

@register(Metric_4_5_7_8_Data_QC)
class AX93():
    # 'Metric_4_5_7_8_Data_QC'!AX93
    value = 28.0707666386
    formula = "='Dashboard M4 Price Monthly'!BD119"
    @eval_fn
    def AX93():
        bd119_1 = Dashboard_M4_Price_Monthly.BD119()
        return bd119_1

@register(Metric_4_5_7_8_Data_QC)
class AY93():
    # 'Metric_4_5_7_8_Data_QC'!AY93
    value = 28.3066554339
    formula = "='Dashboard M4 Price Monthly'!BE119"
    @eval_fn
    def AY93():
        be119_1 = Dashboard_M4_Price_Monthly.BE119()
        return be119_1

@register(Metric_4_5_7_8_Data_QC)
class AZ93():
    # 'Metric_4_5_7_8_Data_QC'!AZ93
    value = 28.3066554339
    formula = "='Dashboard M4 Price Monthly'!BF119"
    @eval_fn
    def AZ93():
        bf119_1 = Dashboard_M4_Price_Monthly.BF119()
        return bf119_1

@register(Metric_4_5_7_8_Data_QC)
class BA93():
    # 'Metric_4_5_7_8_Data_QC'!BA93
    value = 28.3066554339
    formula = "='Dashboard M4 Price Monthly'!BG119"
    @eval_fn
    def BA93():
        bg119_1 = Dashboard_M4_Price_Monthly.BG119()
        return bg119_1

@register(Metric_4_5_7_8_Data_QC)
class BB93():
    # 'Metric_4_5_7_8_Data_QC'!BB93
    value = 26.301600674
    formula = "='Dashboard M4 Price Monthly'!BH119"
    @eval_fn
    def BB93():
        bh119_1 = Dashboard_M4_Price_Monthly.BH119()
        return bh119_1

@register(Metric_4_5_7_8_Data_QC)
class BC93():
    # 'Metric_4_5_7_8_Data_QC'!BC93
    value = 26.301600674
    formula = "='Dashboard M4 Price Monthly'!BI119"
    @eval_fn
    def BC93():
        bi119_1 = Dashboard_M4_Price_Monthly.BI119()
        return bi119_1

@register(Metric_4_5_7_8_Data_QC)
class BD93():
    # 'Metric_4_5_7_8_Data_QC'!BD93
    value = 26.301600674
    formula = "='Dashboard M4 Price Monthly'!BJ119"
    @eval_fn
    def BD93():
        bj119_1 = Dashboard_M4_Price_Monthly.BJ119()
        return bj119_1

@register(Metric_4_5_7_8_Data_QC)
class BE93():
    # 'Metric_4_5_7_8_Data_QC'!BE93
    value = 27.598989048
    formula = "='Dashboard M4 Price Monthly'!BK119"
    @eval_fn
    def BE93():
        bk119_1 = Dashboard_M4_Price_Monthly.BK119()
        return bk119_1

@register(Metric_4_5_7_8_Data_QC)
class BF93():
    # 'Metric_4_5_7_8_Data_QC'!BF93
    value = 27.598989048
    formula = "='Dashboard M4 Price Monthly'!BL119"
    @eval_fn
    def BF93():
        bl119_1 = Dashboard_M4_Price_Monthly.BL119()
        return bl119_1

@register(Metric_4_5_7_8_Data_QC)
class BG93():
    # 'Metric_4_5_7_8_Data_QC'!BG93
    value = 27.598989048
    formula = "='Dashboard M4 Price Monthly'!BM119"
    @eval_fn
    def BG93():
        bm119_1 = Dashboard_M4_Price_Monthly.BM119()
        return bm119_1

@register(Metric_4_5_7_8_Data_QC)
class BH93():
    # 'Metric_4_5_7_8_Data_QC'!BH93
    value = 31.7270429655
    formula = "='Dashboard M4 Price Monthly'!BN119"
    @eval_fn
    def BH93():
        bn119_1 = Dashboard_M4_Price_Monthly.BN119()
        return bn119_1

@register(Metric_4_5_7_8_Data_QC)
class BI93():
    # 'Metric_4_5_7_8_Data_QC'!BI93
    value = 31.7270429655
    formula = "='Dashboard M4 Price Monthly'!BO119"
    @eval_fn
    def BI93():
        bo119_1 = Dashboard_M4_Price_Monthly.BO119()
        return bo119_1

@register(Metric_4_5_7_8_Data_QC)
class BJ93():
    # 'Metric_4_5_7_8_Data_QC'!BJ93
    value = 31.7270429655
    formula = "='Dashboard M4 Price Monthly'!BP119"
    @eval_fn
    def BJ93():
        bp119_1 = Dashboard_M4_Price_Monthly.BP119()
        return bp119_1

@register(Metric_4_5_7_8_Data_QC)
class BK93():
    # 'Metric_4_5_7_8_Data_QC'!BK93
    value = 38.449873631
    formula = "='Dashboard M4 Price Monthly'!BQ119"
    @eval_fn
    def BK93():
        bq119_1 = Dashboard_M4_Price_Monthly.BQ119()
        return bq119_1

@register(Metric_4_5_7_8_Data_QC)
class BL93():
    # 'Metric_4_5_7_8_Data_QC'!BL93
    value = 38.449873631
    formula = "='Dashboard M4 Price Monthly'!BR119"
    @eval_fn
    def BL93():
        br119_1 = Dashboard_M4_Price_Monthly.BR119()
        return br119_1

@register(Metric_4_5_7_8_Data_QC)
class BM93():
    # 'Metric_4_5_7_8_Data_QC'!BM93
    value = 38.449873631
    formula = "='Dashboard M4 Price Monthly'!BS119"
    @eval_fn
    def BM93():
        bs119_1 = Dashboard_M4_Price_Monthly.BS119()
        return bs119_1

@register(Metric_4_5_7_8_Data_QC)
class BN93():
    # 'Metric_4_5_7_8_Data_QC'!BN93
    value = 38.9216512216
    formula = "='Dashboard M4 Price Monthly'!BT119"
    @eval_fn
    def BN93():
        bt119_1 = Dashboard_M4_Price_Monthly.BT119()
        return bt119_1

@register(Metric_4_5_7_8_Data_QC)
class BO93():
    # 'Metric_4_5_7_8_Data_QC'!BO93
    value = 38.9216512216
    formula = "='Dashboard M4 Price Monthly'!BU119"
    @eval_fn
    def BO93():
        bu119_1 = Dashboard_M4_Price_Monthly.BU119()
        return bu119_1

@register(Metric_4_5_7_8_Data_QC)
class BP93():
    # 'Metric_4_5_7_8_Data_QC'!BP93
    value = 38.9216512216
    formula = "='Dashboard M4 Price Monthly'!BV119"
    @eval_fn
    def BP93():
        bv119_1 = Dashboard_M4_Price_Monthly.BV119()
        return bv119_1

@register(Metric_4_5_7_8_Data_QC)
class BQ93():
    # 'Metric_4_5_7_8_Data_QC'!BQ93
    value = 35.8550968829
    formula = "='Dashboard M4 Price Monthly'!BW119"
    @eval_fn
    def BQ93():
        bw119_1 = Dashboard_M4_Price_Monthly.BW119()
        return bw119_1

@register(Metric_4_5_7_8_Data_QC)
class BR93():
    # 'Metric_4_5_7_8_Data_QC'!BR93
    value = 35.8550968829
    formula = "='Dashboard M4 Price Monthly'!BX119"
    @eval_fn
    def BR93():
        bx119_1 = Dashboard_M4_Price_Monthly.BX119()
        return bx119_1

@register(Metric_4_5_7_8_Data_QC)
class BS93():
    # 'Metric_4_5_7_8_Data_QC'!BS93
    value = 35.8550968829
    formula = "='Dashboard M4 Price Monthly'!BY119"
    @eval_fn
    def BS93():
        by119_1 = Dashboard_M4_Price_Monthly.BY119()
        return by119_1

@register(Metric_4_5_7_8_Data_QC)
class BT93():
    # 'Metric_4_5_7_8_Data_QC'!BT93
    value = 35.9730412805
    formula = "='Dashboard M4 Price Monthly'!BZ119"
    @eval_fn
    def BT93():
        bz119_1 = Dashboard_M4_Price_Monthly.BZ119()
        return bz119_1

@register(Metric_4_5_7_8_Data_QC)
class BU93():
    # 'Metric_4_5_7_8_Data_QC'!BU93
    value = 35.9730412805
    formula = "='Dashboard M4 Price Monthly'!CA119"
    @eval_fn
    def BU93():
        ca119_1 = Dashboard_M4_Price_Monthly.CA119()
        return ca119_1

@register(Metric_4_5_7_8_Data_QC)
class BV93():
    # 'Metric_4_5_7_8_Data_QC'!BV93
    value = 35.9730412805
    formula = "='Dashboard M4 Price Monthly'!CB119"
    @eval_fn
    def BV93():
        cb119_1 = Dashboard_M4_Price_Monthly.CB119()
        return cb119_1

@register(Metric_4_5_7_8_Data_QC)
class BW93():
    # 'Metric_4_5_7_8_Data_QC'!BW93
    value = 40.6908171862
    formula = "='Dashboard M4 Price Monthly'!CC119"
    @eval_fn
    def BW93():
        cc119_1 = Dashboard_M4_Price_Monthly.CC119()
        return cc119_1

@register(Metric_4_5_7_8_Data_QC)
class BX93():
    # 'Metric_4_5_7_8_Data_QC'!BX93
    value = 40.6908171862
    formula = "='Dashboard M4 Price Monthly'!CD119"
    @eval_fn
    def BX93():
        cd119_1 = Dashboard_M4_Price_Monthly.CD119()
        return cd119_1

@register(Metric_4_5_7_8_Data_QC)
class BY93():
    # 'Metric_4_5_7_8_Data_QC'!BY93
    value = 40.6908171862
    formula = "='Dashboard M4 Price Monthly'!CE119"
    @eval_fn
    def BY93():
        ce119_1 = Dashboard_M4_Price_Monthly.CE119()
        return ce119_1

@register(Metric_4_5_7_8_Data_QC)
class BZ93():
    # 'Metric_4_5_7_8_Data_QC'!BZ93
    value = 35.9730412805
    formula = "='Dashboard M4 Price Monthly'!CF119"
    @eval_fn
    def BZ93():
        cf119_1 = Dashboard_M4_Price_Monthly.CF119()
        return cf119_1

@register(Metric_4_5_7_8_Data_QC)
class CA93():
    # 'Metric_4_5_7_8_Data_QC'!CA93
    value = 35.9730412805
    formula = "='Dashboard M4 Price Monthly'!CG119"
    @eval_fn
    def CA93():
        cg119_1 = Dashboard_M4_Price_Monthly.CG119()
        return cg119_1

@register(Metric_4_5_7_8_Data_QC)
class CB93():
    # 'Metric_4_5_7_8_Data_QC'!CB93
    value = 35.9730412805
    formula = "='Dashboard M4 Price Monthly'!CH119"
    @eval_fn
    def CB93():
        ch119_1 = Dashboard_M4_Price_Monthly.CH119()
        return ch119_1

@register(Metric_4_5_7_8_Data_QC)
class CC93():
    # 'Metric_4_5_7_8_Data_QC'!CC93
    value = 39.1575400168
    formula = "='Dashboard M4 Price Monthly'!CI119"
    @eval_fn
    def CC93():
        ci119_1 = Dashboard_M4_Price_Monthly.CI119()
        return ci119_1

@register(Metric_4_5_7_8_Data_QC)
class CD93():
    # 'Metric_4_5_7_8_Data_QC'!CD93
    value = 39.1575400168
    formula = "='Dashboard M4 Price Monthly'!CJ119"
    @eval_fn
    def CD93():
        cj119_1 = Dashboard_M4_Price_Monthly.CJ119()
        return cj119_1

@register(Metric_4_5_7_8_Data_QC)
class CE93():
    # 'Metric_4_5_7_8_Data_QC'!CE93
    value = 39.1575400168
    formula = "='Dashboard M4 Price Monthly'!CK119"
    @eval_fn
    def CE93():
        ck119_1 = Dashboard_M4_Price_Monthly.CK119()
        return ck119_1

@register(Metric_4_5_7_8_Data_QC)
class A95():
    # 'Metric_4_5_7_8_Data_QC'!A95
    value = "Residential"

@register(Metric_4_5_7_8_Data_QC)
class E95():
    # 'Metric_4_5_7_8_Data_QC'!E95
    value = "EIA Price"

@register(Metric_4_5_7_8_Data_QC)
class F95():
    # 'Metric_4_5_7_8_Data_QC'!F95
    value = "Average DEBDT Price"

@register(Metric_4_5_7_8_Data_QC)
class G95():
    # 'Metric_4_5_7_8_Data_QC'!G95
    value = "Difference"

@register(Metric_4_5_7_8_Data_QC)
class H95():
    # 'Metric_4_5_7_8_Data_QC'!H95
    value = "Difference as % of EIA"

@register(Metric_4_5_7_8_Data_QC)
class B96():
    # 'Metric_4_5_7_8_Data_QC'!B96
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class C96():
    # 'Metric_4_5_7_8_Data_QC'!C96
    value = "ESRCD"

@register(Metric_4_5_7_8_Data_QC)
class D96():
    # 'Metric_4_5_7_8_Data_QC'!D96
    value = "#N/A"
    formula = "=VLOOKUP(C96,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D96():
        c96_1 = Metric_4_5_7_8_Data_QC.C96()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c96_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E96():
    # 'Metric_4_5_7_8_Data_QC'!E96
    value = "#N/A"
    formula = "=VLOOKUP(C96,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E96():
        c96_1 = Metric_4_5_7_8_Data_QC.C96()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c96_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F96():
    # 'Metric_4_5_7_8_Data_QC'!F96
    value = 60.1061315
    formula = "=AVERAGE(E85:M85)"
    @eval_fn
    def F96():
        range_1 = Metric_4_5_7_8_Data_QC(5, 85, 13, 85)
        var_1 = AVERAGE(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G96():
    # 'Metric_4_5_7_8_Data_QC'!G96
    value = "#N/A"
    formula = "=F96-E96"
    @eval_fn
    def G96():
        f96_1 = Metric_4_5_7_8_Data_QC.F96()
        e96_1 = Metric_4_5_7_8_Data_QC.E96()
        var_1 = sub(f96_1, e96_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H96():
    # 'Metric_4_5_7_8_Data_QC'!H96
    value = "#N/A"
    formula = "=G96/E96"
    @eval_fn
    def H96():
        g96_1 = Metric_4_5_7_8_Data_QC.G96()
        e96_1 = Metric_4_5_7_8_Data_QC.E96()
        var_1 = divide(g96_1, e96_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B97():
    # 'Metric_4_5_7_8_Data_QC'!B97
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class C97():
    # 'Metric_4_5_7_8_Data_QC'!C97
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E97():
    # 'Metric_4_5_7_8_Data_QC'!E97
    value = 0
    formula = "=VLOOKUP(C97,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E97():
        c97_1 = Metric_4_5_7_8_Data_QC.C97()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c97_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F97():
    # 'Metric_4_5_7_8_Data_QC'!F97
    value = 24.5444170066
    formula = "=AVERAGE(E86:M86)"
    @eval_fn
    def F97():
        range_1 = Metric_4_5_7_8_Data_QC(5, 86, 13, 86)
        var_1 = AVERAGE(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B98():
    # 'Metric_4_5_7_8_Data_QC'!B98
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class C98():
    # 'Metric_4_5_7_8_Data_QC'!C98
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E98():
    # 'Metric_4_5_7_8_Data_QC'!E98
    value = 0
    formula = "=VLOOKUP(C98,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E98():
        c98_1 = Metric_4_5_7_8_Data_QC.C98()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c98_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F98():
    # 'Metric_4_5_7_8_Data_QC'!F98
    value = 16.1768643492
    formula = "=AVERAGE(E87:M87)"
    @eval_fn
    def F98():
        range_1 = Metric_4_5_7_8_Data_QC(5, 87, 13, 87)
        var_1 = AVERAGE(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B99():
    # 'Metric_4_5_7_8_Data_QC'!B99
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class C99():
    # 'Metric_4_5_7_8_Data_QC'!C99
    value = "DFRCD"

@register(Metric_4_5_7_8_Data_QC)
class D99():
    # 'Metric_4_5_7_8_Data_QC'!D99
    value = "#N/A"
    formula = "=VLOOKUP(C99,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D99():
        c99_1 = Metric_4_5_7_8_Data_QC.C99()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c99_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E99():
    # 'Metric_4_5_7_8_Data_QC'!E99
    value = "#N/A"
    formula = "=VLOOKUP(C99,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E99():
        c99_1 = Metric_4_5_7_8_Data_QC.C99()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c99_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F99():
    # 'Metric_4_5_7_8_Data_QC'!F99
    value = 24.8346392139
    formula = "=AVERAGE(E88:M88)"
    @eval_fn
    def F99():
        range_1 = Metric_4_5_7_8_Data_QC(5, 88, 13, 88)
        var_1 = AVERAGE(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G99():
    # 'Metric_4_5_7_8_Data_QC'!G99
    value = "#N/A"
    formula = "=F99-E99"
    @eval_fn
    def G99():
        f99_1 = Metric_4_5_7_8_Data_QC.F99()
        e99_1 = Metric_4_5_7_8_Data_QC.E99()
        var_1 = sub(f99_1, e99_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H99():
    # 'Metric_4_5_7_8_Data_QC'!H99
    value = "#N/A"
    formula = "=G99/E99"
    @eval_fn
    def H99():
        g99_1 = Metric_4_5_7_8_Data_QC.G99()
        e99_1 = Metric_4_5_7_8_Data_QC.E99()
        var_1 = divide(g99_1, e99_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B100():
    # 'Metric_4_5_7_8_Data_QC'!B100
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class C100():
    # 'Metric_4_5_7_8_Data_QC'!C100
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E100():
    # 'Metric_4_5_7_8_Data_QC'!E100
    value = 0
    formula = "=VLOOKUP(C100,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E100():
        c100_1 = Metric_4_5_7_8_Data_QC.C100()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c100_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F100():
    # 'Metric_4_5_7_8_Data_QC'!F100
    value = 9.28227559514
    formula = "=AVERAGE(E89:M89)"
    @eval_fn
    def F100():
        range_1 = Metric_4_5_7_8_Data_QC(5, 89, 13, 89)
        var_1 = AVERAGE(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B101():
    # 'Metric_4_5_7_8_Data_QC'!B101
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class C101():
    # 'Metric_4_5_7_8_Data_QC'!C101
    value = "LGRCD"

@register(Metric_4_5_7_8_Data_QC)
class D101():
    # 'Metric_4_5_7_8_Data_QC'!D101
    value = "#N/A"
    formula = "=VLOOKUP(C101,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D101():
        c101_1 = Metric_4_5_7_8_Data_QC.C101()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c101_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E101():
    # 'Metric_4_5_7_8_Data_QC'!E101
    value = "#N/A"
    formula = "=VLOOKUP(C101,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E101():
        c101_1 = Metric_4_5_7_8_Data_QC.C101()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c101_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F101():
    # 'Metric_4_5_7_8_Data_QC'!F101
    value = 33.056826405
    formula = "=AVERAGE(E90:M90)"
    @eval_fn
    def F101():
        range_1 = Metric_4_5_7_8_Data_QC(5, 90, 13, 90)
        var_1 = AVERAGE(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G101():
    # 'Metric_4_5_7_8_Data_QC'!G101
    value = "#N/A"
    formula = "=F101-E101"
    @eval_fn
    def G101():
        f101_1 = Metric_4_5_7_8_Data_QC.F101()
        e101_1 = Metric_4_5_7_8_Data_QC.E101()
        var_1 = sub(f101_1, e101_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H101():
    # 'Metric_4_5_7_8_Data_QC'!H101
    value = "#N/A"
    formula = "=G101/E101"
    @eval_fn
    def H101():
        g101_1 = Metric_4_5_7_8_Data_QC.G101()
        e101_1 = Metric_4_5_7_8_Data_QC.E101()
        var_1 = divide(g101_1, e101_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B102():
    # 'Metric_4_5_7_8_Data_QC'!B102
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class C102():
    # 'Metric_4_5_7_8_Data_QC'!C102
    value = "NGRCD"

@register(Metric_4_5_7_8_Data_QC)
class D102():
    # 'Metric_4_5_7_8_Data_QC'!D102
    value = "#N/A"
    formula = "=VLOOKUP(C102,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D102():
        c102_1 = Metric_4_5_7_8_Data_QC.C102()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c102_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E102():
    # 'Metric_4_5_7_8_Data_QC'!E102
    value = "#N/A"
    formula = "=VLOOKUP(C102,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E102():
        c102_1 = Metric_4_5_7_8_Data_QC.C102()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c102_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F102():
    # 'Metric_4_5_7_8_Data_QC'!F102
    value = 26.3019286205
    formula = "=AVERAGE(E91:M91)"
    @eval_fn
    def F102():
        range_1 = Metric_4_5_7_8_Data_QC(5, 91, 13, 91)
        var_1 = AVERAGE(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class G102():
    # 'Metric_4_5_7_8_Data_QC'!G102
    value = "#N/A"
    formula = "=F102-E102"
    @eval_fn
    def G102():
        f102_1 = Metric_4_5_7_8_Data_QC.F102()
        e102_1 = Metric_4_5_7_8_Data_QC.E102()
        var_1 = sub(f102_1, e102_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H102():
    # 'Metric_4_5_7_8_Data_QC'!H102
    value = "#N/A"
    formula = "=G102/E102"
    @eval_fn
    def H102():
        g102_1 = Metric_4_5_7_8_Data_QC.G102()
        e102_1 = Metric_4_5_7_8_Data_QC.E102()
        var_1 = divide(g102_1, e102_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B103():
    # 'Metric_4_5_7_8_Data_QC'!B103
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class C103():
    # 'Metric_4_5_7_8_Data_QC'!C103
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E103():
    # 'Metric_4_5_7_8_Data_QC'!E103
    value = 0
    formula = "=VLOOKUP(C103,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E103():
        c103_1 = Metric_4_5_7_8_Data_QC.C103()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c103_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F103():
    # 'Metric_4_5_7_8_Data_QC'!F103
    value = 0
    formula = "=AVERAGE(E92:M92)"
    @eval_fn
    def F103():
        range_1 = Metric_4_5_7_8_Data_QC(5, 92, 13, 92)
        var_1 = AVERAGE(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B104():
    # 'Metric_4_5_7_8_Data_QC'!B104
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class C104():
    # 'Metric_4_5_7_8_Data_QC'!C104
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E104():
    # 'Metric_4_5_7_8_Data_QC'!E104
    value = 0
    formula = "=VLOOKUP(C104,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E104():
        c104_1 = Metric_4_5_7_8_Data_QC.C104()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c104_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F104():
    # 'Metric_4_5_7_8_Data_QC'!F104
    value = 28.0183469063
    formula = "=AVERAGE(E93:M93)"
    @eval_fn
    def F104():
        range_1 = Metric_4_5_7_8_Data_QC(5, 93, 13, 93)
        var_1 = AVERAGE(range_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class A106():
    # 'Metric_4_5_7_8_Data_QC'!A106
    value = "Commercial"

@register(Metric_4_5_7_8_Data_QC)
class B107():
    # 'Metric_4_5_7_8_Data_QC'!B107
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class C107():
    # 'Metric_4_5_7_8_Data_QC'!C107
    value = "ESCCD"

@register(Metric_4_5_7_8_Data_QC)
class D107():
    # 'Metric_4_5_7_8_Data_QC'!D107
    value = "#N/A"
    formula = "=VLOOKUP(C107,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D107():
        c107_1 = Metric_4_5_7_8_Data_QC.C107()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c107_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E107():
    # 'Metric_4_5_7_8_Data_QC'!E107
    value = "#N/A"
    formula = "=VLOOKUP(C107,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E107():
        c107_1 = Metric_4_5_7_8_Data_QC.C107()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c107_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F107():
    # 'Metric_4_5_7_8_Data_QC'!F107
    value = 60.1061315
    formula = "=F96"
    @eval_fn
    def F107():
        f96_1 = Metric_4_5_7_8_Data_QC.F96()
        return f96_1

@register(Metric_4_5_7_8_Data_QC)
class G107():
    # 'Metric_4_5_7_8_Data_QC'!G107
    value = "#N/A"
    formula = "=F107-E107"
    @eval_fn
    def G107():
        f107_1 = Metric_4_5_7_8_Data_QC.F107()
        e107_1 = Metric_4_5_7_8_Data_QC.E107()
        var_1 = sub(f107_1, e107_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H107():
    # 'Metric_4_5_7_8_Data_QC'!H107
    value = "#N/A"
    formula = "=G107/E107"
    @eval_fn
    def H107():
        g107_1 = Metric_4_5_7_8_Data_QC.G107()
        e107_1 = Metric_4_5_7_8_Data_QC.E107()
        var_1 = divide(g107_1, e107_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B108():
    # 'Metric_4_5_7_8_Data_QC'!B108
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class C108():
    # 'Metric_4_5_7_8_Data_QC'!C108
    value = "MGCCD"

@register(Metric_4_5_7_8_Data_QC)
class D108():
    # 'Metric_4_5_7_8_Data_QC'!D108
    value = "#N/A"
    formula = "=VLOOKUP(C108,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D108():
        c108_1 = Metric_4_5_7_8_Data_QC.C108()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c108_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E108():
    # 'Metric_4_5_7_8_Data_QC'!E108
    value = "#N/A"
    formula = "=VLOOKUP(C108,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E108():
        c108_1 = Metric_4_5_7_8_Data_QC.C108()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c108_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F108():
    # 'Metric_4_5_7_8_Data_QC'!F108
    value = 24.5444170066
    formula = "=F97"
    @eval_fn
    def F108():
        f97_1 = Metric_4_5_7_8_Data_QC.F97()
        return f97_1

@register(Metric_4_5_7_8_Data_QC)
class G108():
    # 'Metric_4_5_7_8_Data_QC'!G108
    value = "#N/A"
    formula = "=F108-E108"
    @eval_fn
    def G108():
        f108_1 = Metric_4_5_7_8_Data_QC.F108()
        e108_1 = Metric_4_5_7_8_Data_QC.E108()
        var_1 = sub(f108_1, e108_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H108():
    # 'Metric_4_5_7_8_Data_QC'!H108
    value = "#N/A"
    formula = "=G108/E108"
    @eval_fn
    def H108():
        g108_1 = Metric_4_5_7_8_Data_QC.G108()
        e108_1 = Metric_4_5_7_8_Data_QC.E108()
        var_1 = divide(g108_1, e108_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B109():
    # 'Metric_4_5_7_8_Data_QC'!B109
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class C109():
    # 'Metric_4_5_7_8_Data_QC'!C109
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E109():
    # 'Metric_4_5_7_8_Data_QC'!E109
    value = 0
    formula = "=VLOOKUP(C109,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E109():
        c109_1 = Metric_4_5_7_8_Data_QC.C109()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c109_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F109():
    # 'Metric_4_5_7_8_Data_QC'!F109
    value = 16.1768643492
    formula = "=F98"
    @eval_fn
    def F109():
        f98_1 = Metric_4_5_7_8_Data_QC.F98()
        return f98_1

@register(Metric_4_5_7_8_Data_QC)
class B110():
    # 'Metric_4_5_7_8_Data_QC'!B110
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class C110():
    # 'Metric_4_5_7_8_Data_QC'!C110
    value = "DFCCD"

@register(Metric_4_5_7_8_Data_QC)
class D110():
    # 'Metric_4_5_7_8_Data_QC'!D110
    value = "#N/A"
    formula = "=VLOOKUP(C110,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D110():
        c110_1 = Metric_4_5_7_8_Data_QC.C110()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c110_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E110():
    # 'Metric_4_5_7_8_Data_QC'!E110
    value = "#N/A"
    formula = "=VLOOKUP(C110,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E110():
        c110_1 = Metric_4_5_7_8_Data_QC.C110()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c110_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F110():
    # 'Metric_4_5_7_8_Data_QC'!F110
    value = 24.8346392139
    formula = "=F99"
    @eval_fn
    def F110():
        f99_1 = Metric_4_5_7_8_Data_QC.F99()
        return f99_1

@register(Metric_4_5_7_8_Data_QC)
class G110():
    # 'Metric_4_5_7_8_Data_QC'!G110
    value = "#N/A"
    formula = "=F110-E110"
    @eval_fn
    def G110():
        f110_1 = Metric_4_5_7_8_Data_QC.F110()
        e110_1 = Metric_4_5_7_8_Data_QC.E110()
        var_1 = sub(f110_1, e110_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H110():
    # 'Metric_4_5_7_8_Data_QC'!H110
    value = "#N/A"
    formula = "=G110/E110"
    @eval_fn
    def H110():
        g110_1 = Metric_4_5_7_8_Data_QC.G110()
        e110_1 = Metric_4_5_7_8_Data_QC.E110()
        var_1 = divide(g110_1, e110_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B111():
    # 'Metric_4_5_7_8_Data_QC'!B111
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class C111():
    # 'Metric_4_5_7_8_Data_QC'!C111
    value = "RFCCD"

@register(Metric_4_5_7_8_Data_QC)
class D111():
    # 'Metric_4_5_7_8_Data_QC'!D111
    value = "#N/A"
    formula = "=VLOOKUP(C111,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D111():
        c111_1 = Metric_4_5_7_8_Data_QC.C111()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c111_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E111():
    # 'Metric_4_5_7_8_Data_QC'!E111
    value = "#N/A"
    formula = "=VLOOKUP(C111,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E111():
        c111_1 = Metric_4_5_7_8_Data_QC.C111()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c111_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F111():
    # 'Metric_4_5_7_8_Data_QC'!F111
    value = 9.28227559514
    formula = "=F100"
    @eval_fn
    def F111():
        f100_1 = Metric_4_5_7_8_Data_QC.F100()
        return f100_1

@register(Metric_4_5_7_8_Data_QC)
class G111():
    # 'Metric_4_5_7_8_Data_QC'!G111
    value = "#N/A"
    formula = "=F111-E111"
    @eval_fn
    def G111():
        f111_1 = Metric_4_5_7_8_Data_QC.F111()
        e111_1 = Metric_4_5_7_8_Data_QC.E111()
        var_1 = sub(f111_1, e111_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H111():
    # 'Metric_4_5_7_8_Data_QC'!H111
    value = "#N/A"
    formula = "=G111/E111"
    @eval_fn
    def H111():
        g111_1 = Metric_4_5_7_8_Data_QC.G111()
        e111_1 = Metric_4_5_7_8_Data_QC.E111()
        var_1 = divide(g111_1, e111_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B112():
    # 'Metric_4_5_7_8_Data_QC'!B112
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class C112():
    # 'Metric_4_5_7_8_Data_QC'!C112
    value = "LGCCD"

@register(Metric_4_5_7_8_Data_QC)
class D112():
    # 'Metric_4_5_7_8_Data_QC'!D112
    value = "#N/A"
    formula = "=VLOOKUP(C112,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D112():
        c112_1 = Metric_4_5_7_8_Data_QC.C112()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c112_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E112():
    # 'Metric_4_5_7_8_Data_QC'!E112
    value = "#N/A"
    formula = "=VLOOKUP(C112,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E112():
        c112_1 = Metric_4_5_7_8_Data_QC.C112()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c112_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F112():
    # 'Metric_4_5_7_8_Data_QC'!F112
    value = 33.056826405
    formula = "=F101"
    @eval_fn
    def F112():
        f101_1 = Metric_4_5_7_8_Data_QC.F101()
        return f101_1

@register(Metric_4_5_7_8_Data_QC)
class G112():
    # 'Metric_4_5_7_8_Data_QC'!G112
    value = "#N/A"
    formula = "=F112-E112"
    @eval_fn
    def G112():
        f112_1 = Metric_4_5_7_8_Data_QC.F112()
        e112_1 = Metric_4_5_7_8_Data_QC.E112()
        var_1 = sub(f112_1, e112_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H112():
    # 'Metric_4_5_7_8_Data_QC'!H112
    value = "#N/A"
    formula = "=G112/E112"
    @eval_fn
    def H112():
        g112_1 = Metric_4_5_7_8_Data_QC.G112()
        e112_1 = Metric_4_5_7_8_Data_QC.E112()
        var_1 = divide(g112_1, e112_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B113():
    # 'Metric_4_5_7_8_Data_QC'!B113
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class C113():
    # 'Metric_4_5_7_8_Data_QC'!C113
    value = "NGCCD"

@register(Metric_4_5_7_8_Data_QC)
class D113():
    # 'Metric_4_5_7_8_Data_QC'!D113
    value = "#N/A"
    formula = "=VLOOKUP(C113,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D113():
        c113_1 = Metric_4_5_7_8_Data_QC.C113()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c113_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E113():
    # 'Metric_4_5_7_8_Data_QC'!E113
    value = "#N/A"
    formula = "=VLOOKUP(C113,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E113():
        c113_1 = Metric_4_5_7_8_Data_QC.C113()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c113_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F113():
    # 'Metric_4_5_7_8_Data_QC'!F113
    value = 26.3019286205
    formula = "=F102"
    @eval_fn
    def F113():
        f102_1 = Metric_4_5_7_8_Data_QC.F102()
        return f102_1

@register(Metric_4_5_7_8_Data_QC)
class G113():
    # 'Metric_4_5_7_8_Data_QC'!G113
    value = "#N/A"
    formula = "=F113-E113"
    @eval_fn
    def G113():
        f113_1 = Metric_4_5_7_8_Data_QC.F113()
        e113_1 = Metric_4_5_7_8_Data_QC.E113()
        var_1 = sub(f113_1, e113_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H113():
    # 'Metric_4_5_7_8_Data_QC'!H113
    value = "#N/A"
    formula = "=G113/E113"
    @eval_fn
    def H113():
        g113_1 = Metric_4_5_7_8_Data_QC.G113()
        e113_1 = Metric_4_5_7_8_Data_QC.E113()
        var_1 = divide(g113_1, e113_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B114():
    # 'Metric_4_5_7_8_Data_QC'!B114
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class C114():
    # 'Metric_4_5_7_8_Data_QC'!C114
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E114():
    # 'Metric_4_5_7_8_Data_QC'!E114
    value = 0
    formula = "=VLOOKUP(C114,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E114():
        c114_1 = Metric_4_5_7_8_Data_QC.C114()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c114_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F114():
    # 'Metric_4_5_7_8_Data_QC'!F114
    value = 0
    formula = "=F103"
    @eval_fn
    def F114():
        f103_1 = Metric_4_5_7_8_Data_QC.F103()
        return f103_1

@register(Metric_4_5_7_8_Data_QC)
class B115():
    # 'Metric_4_5_7_8_Data_QC'!B115
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class C115():
    # 'Metric_4_5_7_8_Data_QC'!C115
    value = "EMCCD"

@register(Metric_4_5_7_8_Data_QC)
class E115():
    # 'Metric_4_5_7_8_Data_QC'!E115
    value = "#N/A"
    formula = "=VLOOKUP(C115,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E115():
        c115_1 = Metric_4_5_7_8_Data_QC.C115()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c115_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F115():
    # 'Metric_4_5_7_8_Data_QC'!F115
    value = 28.0183469063
    formula = "=F104"
    @eval_fn
    def F115():
        f104_1 = Metric_4_5_7_8_Data_QC.F104()
        return f104_1

@register(Metric_4_5_7_8_Data_QC)
class A117():
    # 'Metric_4_5_7_8_Data_QC'!A117
    value = "Industrial"

@register(Metric_4_5_7_8_Data_QC)
class A118():
    # 'Metric_4_5_7_8_Data_QC'!A118
    value = "NGICV"

@register(Metric_4_5_7_8_Data_QC)
class B118():
    # 'Metric_4_5_7_8_Data_QC'!B118
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class C118():
    # 'Metric_4_5_7_8_Data_QC'!C118
    value = "ESICD"

@register(Metric_4_5_7_8_Data_QC)
class D118():
    # 'Metric_4_5_7_8_Data_QC'!D118
    value = "#N/A"
    formula = "=VLOOKUP(C118,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D118():
        c118_1 = Metric_4_5_7_8_Data_QC.C118()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c118_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E118():
    # 'Metric_4_5_7_8_Data_QC'!E118
    value = "#N/A"
    formula = "=VLOOKUP(C118,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E118():
        c118_1 = Metric_4_5_7_8_Data_QC.C118()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c118_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F118():
    # 'Metric_4_5_7_8_Data_QC'!F118
    value = 60.1061315
    formula = "=F107"
    @eval_fn
    def F118():
        f107_1 = Metric_4_5_7_8_Data_QC.F107()
        return f107_1

@register(Metric_4_5_7_8_Data_QC)
class G118():
    # 'Metric_4_5_7_8_Data_QC'!G118
    value = "#N/A"
    formula = "=F118-E118"
    @eval_fn
    def G118():
        f118_1 = Metric_4_5_7_8_Data_QC.F118()
        e118_1 = Metric_4_5_7_8_Data_QC.E118()
        var_1 = sub(f118_1, e118_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H118():
    # 'Metric_4_5_7_8_Data_QC'!H118
    value = "#N/A"
    formula = "=G118/E118"
    @eval_fn
    def H118():
        g118_1 = Metric_4_5_7_8_Data_QC.G118()
        e118_1 = Metric_4_5_7_8_Data_QC.E118()
        var_1 = divide(g118_1, e118_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B119():
    # 'Metric_4_5_7_8_Data_QC'!B119
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class C119():
    # 'Metric_4_5_7_8_Data_QC'!C119
    value = "MGICD"

@register(Metric_4_5_7_8_Data_QC)
class D119():
    # 'Metric_4_5_7_8_Data_QC'!D119
    value = "#N/A"
    formula = "=VLOOKUP(C119,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D119():
        c119_1 = Metric_4_5_7_8_Data_QC.C119()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c119_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E119():
    # 'Metric_4_5_7_8_Data_QC'!E119
    value = "#N/A"
    formula = "=VLOOKUP(C119,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E119():
        c119_1 = Metric_4_5_7_8_Data_QC.C119()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c119_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F119():
    # 'Metric_4_5_7_8_Data_QC'!F119
    value = 24.5444170066
    formula = "=F108"
    @eval_fn
    def F119():
        f108_1 = Metric_4_5_7_8_Data_QC.F108()
        return f108_1

@register(Metric_4_5_7_8_Data_QC)
class G119():
    # 'Metric_4_5_7_8_Data_QC'!G119
    value = "#N/A"
    formula = "=F119-E119"
    @eval_fn
    def G119():
        f119_1 = Metric_4_5_7_8_Data_QC.F119()
        e119_1 = Metric_4_5_7_8_Data_QC.E119()
        var_1 = sub(f119_1, e119_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H119():
    # 'Metric_4_5_7_8_Data_QC'!H119
    value = "#N/A"
    formula = "=G119/E119"
    @eval_fn
    def H119():
        g119_1 = Metric_4_5_7_8_Data_QC.G119()
        e119_1 = Metric_4_5_7_8_Data_QC.E119()
        var_1 = divide(g119_1, e119_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B120():
    # 'Metric_4_5_7_8_Data_QC'!B120
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class C120():
    # 'Metric_4_5_7_8_Data_QC'!C120
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E120():
    # 'Metric_4_5_7_8_Data_QC'!E120
    value = 0
    formula = "=VLOOKUP(C120,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E120():
        c120_1 = Metric_4_5_7_8_Data_QC.C120()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c120_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F120():
    # 'Metric_4_5_7_8_Data_QC'!F120
    value = 16.1768643492
    formula = "=F109"
    @eval_fn
    def F120():
        f109_1 = Metric_4_5_7_8_Data_QC.F109()
        return f109_1

@register(Metric_4_5_7_8_Data_QC)
class B121():
    # 'Metric_4_5_7_8_Data_QC'!B121
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class C121():
    # 'Metric_4_5_7_8_Data_QC'!C121
    value = "DFICD"

@register(Metric_4_5_7_8_Data_QC)
class D121():
    # 'Metric_4_5_7_8_Data_QC'!D121
    value = "#N/A"
    formula = "=VLOOKUP(C121,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D121():
        c121_1 = Metric_4_5_7_8_Data_QC.C121()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c121_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E121():
    # 'Metric_4_5_7_8_Data_QC'!E121
    value = "#N/A"
    formula = "=VLOOKUP(C121,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E121():
        c121_1 = Metric_4_5_7_8_Data_QC.C121()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c121_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F121():
    # 'Metric_4_5_7_8_Data_QC'!F121
    value = 24.8346392139
    formula = "=F110"
    @eval_fn
    def F121():
        f110_1 = Metric_4_5_7_8_Data_QC.F110()
        return f110_1

@register(Metric_4_5_7_8_Data_QC)
class G121():
    # 'Metric_4_5_7_8_Data_QC'!G121
    value = "#N/A"
    formula = "=F121-E121"
    @eval_fn
    def G121():
        f121_1 = Metric_4_5_7_8_Data_QC.F121()
        e121_1 = Metric_4_5_7_8_Data_QC.E121()
        var_1 = sub(f121_1, e121_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H121():
    # 'Metric_4_5_7_8_Data_QC'!H121
    value = "#N/A"
    formula = "=G121/E121"
    @eval_fn
    def H121():
        g121_1 = Metric_4_5_7_8_Data_QC.G121()
        e121_1 = Metric_4_5_7_8_Data_QC.E121()
        var_1 = divide(g121_1, e121_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B122():
    # 'Metric_4_5_7_8_Data_QC'!B122
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class C122():
    # 'Metric_4_5_7_8_Data_QC'!C122
    value = "RFICD"

@register(Metric_4_5_7_8_Data_QC)
class D122():
    # 'Metric_4_5_7_8_Data_QC'!D122
    value = "#N/A"
    formula = "=VLOOKUP(C122,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D122():
        c122_1 = Metric_4_5_7_8_Data_QC.C122()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c122_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E122():
    # 'Metric_4_5_7_8_Data_QC'!E122
    value = "#N/A"
    formula = "=VLOOKUP(C122,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E122():
        c122_1 = Metric_4_5_7_8_Data_QC.C122()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c122_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F122():
    # 'Metric_4_5_7_8_Data_QC'!F122
    value = 9.28227559514
    formula = "=F111"
    @eval_fn
    def F122():
        f111_1 = Metric_4_5_7_8_Data_QC.F111()
        return f111_1

@register(Metric_4_5_7_8_Data_QC)
class G122():
    # 'Metric_4_5_7_8_Data_QC'!G122
    value = "#N/A"
    formula = "=F122-E122"
    @eval_fn
    def G122():
        f122_1 = Metric_4_5_7_8_Data_QC.F122()
        e122_1 = Metric_4_5_7_8_Data_QC.E122()
        var_1 = sub(f122_1, e122_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H122():
    # 'Metric_4_5_7_8_Data_QC'!H122
    value = "#N/A"
    formula = "=G122/E122"
    @eval_fn
    def H122():
        g122_1 = Metric_4_5_7_8_Data_QC.G122()
        e122_1 = Metric_4_5_7_8_Data_QC.E122()
        var_1 = divide(g122_1, e122_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B123():
    # 'Metric_4_5_7_8_Data_QC'!B123
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class C123():
    # 'Metric_4_5_7_8_Data_QC'!C123
    value = "LGICD"

@register(Metric_4_5_7_8_Data_QC)
class D123():
    # 'Metric_4_5_7_8_Data_QC'!D123
    value = "#N/A"
    formula = "=VLOOKUP(C123,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D123():
        c123_1 = Metric_4_5_7_8_Data_QC.C123()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c123_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E123():
    # 'Metric_4_5_7_8_Data_QC'!E123
    value = "#N/A"
    formula = "=VLOOKUP(C123,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E123():
        c123_1 = Metric_4_5_7_8_Data_QC.C123()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c123_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F123():
    # 'Metric_4_5_7_8_Data_QC'!F123
    value = 33.056826405
    formula = "=F112"
    @eval_fn
    def F123():
        f112_1 = Metric_4_5_7_8_Data_QC.F112()
        return f112_1

@register(Metric_4_5_7_8_Data_QC)
class G123():
    # 'Metric_4_5_7_8_Data_QC'!G123
    value = "#N/A"
    formula = "=F123-E123"
    @eval_fn
    def G123():
        f123_1 = Metric_4_5_7_8_Data_QC.F123()
        e123_1 = Metric_4_5_7_8_Data_QC.E123()
        var_1 = sub(f123_1, e123_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H123():
    # 'Metric_4_5_7_8_Data_QC'!H123
    value = "#N/A"
    formula = "=G123/E123"
    @eval_fn
    def H123():
        g123_1 = Metric_4_5_7_8_Data_QC.G123()
        e123_1 = Metric_4_5_7_8_Data_QC.E123()
        var_1 = divide(g123_1, e123_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B124():
    # 'Metric_4_5_7_8_Data_QC'!B124
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class C124():
    # 'Metric_4_5_7_8_Data_QC'!C124
    value = "NGICD"

@register(Metric_4_5_7_8_Data_QC)
class D124():
    # 'Metric_4_5_7_8_Data_QC'!D124
    value = "#N/A"
    formula = "=VLOOKUP(C124,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D124():
        c124_1 = Metric_4_5_7_8_Data_QC.C124()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c124_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E124():
    # 'Metric_4_5_7_8_Data_QC'!E124
    value = "#N/A"
    formula = "=VLOOKUP(C124,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E124():
        c124_1 = Metric_4_5_7_8_Data_QC.C124()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c124_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F124():
    # 'Metric_4_5_7_8_Data_QC'!F124
    value = 26.3019286205
    formula = "=F113"
    @eval_fn
    def F124():
        f113_1 = Metric_4_5_7_8_Data_QC.F113()
        return f113_1

@register(Metric_4_5_7_8_Data_QC)
class G124():
    # 'Metric_4_5_7_8_Data_QC'!G124
    value = "#N/A"
    formula = "=F124-E124"
    @eval_fn
    def G124():
        f124_1 = Metric_4_5_7_8_Data_QC.F124()
        e124_1 = Metric_4_5_7_8_Data_QC.E124()
        var_1 = sub(f124_1, e124_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H124():
    # 'Metric_4_5_7_8_Data_QC'!H124
    value = "#N/A"
    formula = "=G124/E124"
    @eval_fn
    def H124():
        g124_1 = Metric_4_5_7_8_Data_QC.G124()
        e124_1 = Metric_4_5_7_8_Data_QC.E124()
        var_1 = divide(g124_1, e124_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B125():
    # 'Metric_4_5_7_8_Data_QC'!B125
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class C125():
    # 'Metric_4_5_7_8_Data_QC'!C125
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E125():
    # 'Metric_4_5_7_8_Data_QC'!E125
    value = 0
    formula = "=VLOOKUP(C125,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E125():
        c125_1 = Metric_4_5_7_8_Data_QC.C125()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c125_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F125():
    # 'Metric_4_5_7_8_Data_QC'!F125
    value = 0
    formula = "=F114"
    @eval_fn
    def F125():
        f114_1 = Metric_4_5_7_8_Data_QC.F114()
        return f114_1

@register(Metric_4_5_7_8_Data_QC)
class B126():
    # 'Metric_4_5_7_8_Data_QC'!B126
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class C126():
    # 'Metric_4_5_7_8_Data_QC'!C126
    value = "EMICD"

@register(Metric_4_5_7_8_Data_QC)
class E126():
    # 'Metric_4_5_7_8_Data_QC'!E126
    value = "#N/A"
    formula = "=VLOOKUP(C126,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E126():
        c126_1 = Metric_4_5_7_8_Data_QC.C126()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c126_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F126():
    # 'Metric_4_5_7_8_Data_QC'!F126
    value = 28.0183469063
    formula = "=F115"
    @eval_fn
    def F126():
        f115_1 = Metric_4_5_7_8_Data_QC.F115()
        return f115_1

@register(Metric_4_5_7_8_Data_QC)
class G126():
    # 'Metric_4_5_7_8_Data_QC'!G126
    value = "#N/A"
    formula = "=F126-E126"
    @eval_fn
    def G126():
        f126_1 = Metric_4_5_7_8_Data_QC.F126()
        e126_1 = Metric_4_5_7_8_Data_QC.E126()
        var_1 = sub(f126_1, e126_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H126():
    # 'Metric_4_5_7_8_Data_QC'!H126
    value = "#N/A"
    formula = "=G126/E126"
    @eval_fn
    def H126():
        g126_1 = Metric_4_5_7_8_Data_QC.G126()
        e126_1 = Metric_4_5_7_8_Data_QC.E126()
        var_1 = divide(g126_1, e126_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class A128():
    # 'Metric_4_5_7_8_Data_QC'!A128
    value = "Ground and Water Transportation"

@register(Metric_4_5_7_8_Data_QC)
class B129():
    # 'Metric_4_5_7_8_Data_QC'!B129
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class C129():
    # 'Metric_4_5_7_8_Data_QC'!C129
    value = "ESACD"

@register(Metric_4_5_7_8_Data_QC)
class D129():
    # 'Metric_4_5_7_8_Data_QC'!D129
    value = "#N/A"
    formula = "=VLOOKUP(C129,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D129():
        c129_1 = Metric_4_5_7_8_Data_QC.C129()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c129_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E129():
    # 'Metric_4_5_7_8_Data_QC'!E129
    value = "#N/A"
    formula = "=VLOOKUP(C129,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E129():
        c129_1 = Metric_4_5_7_8_Data_QC.C129()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c129_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F129():
    # 'Metric_4_5_7_8_Data_QC'!F129
    value = 60.1061315
    formula = "=F118"
    @eval_fn
    def F129():
        f118_1 = Metric_4_5_7_8_Data_QC.F118()
        return f118_1

@register(Metric_4_5_7_8_Data_QC)
class B130():
    # 'Metric_4_5_7_8_Data_QC'!B130
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class C130():
    # 'Metric_4_5_7_8_Data_QC'!C130
    value = "MGACD"

@register(Metric_4_5_7_8_Data_QC)
class D130():
    # 'Metric_4_5_7_8_Data_QC'!D130
    value = "#N/A"
    formula = "=VLOOKUP(C130,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D130():
        c130_1 = Metric_4_5_7_8_Data_QC.C130()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c130_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E130():
    # 'Metric_4_5_7_8_Data_QC'!E130
    value = "#N/A"
    formula = "=VLOOKUP(C130,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E130():
        c130_1 = Metric_4_5_7_8_Data_QC.C130()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c130_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F130():
    # 'Metric_4_5_7_8_Data_QC'!F130
    value = 24.5444170066
    formula = "=F119"
    @eval_fn
    def F130():
        f119_1 = Metric_4_5_7_8_Data_QC.F119()
        return f119_1

@register(Metric_4_5_7_8_Data_QC)
class G130():
    # 'Metric_4_5_7_8_Data_QC'!G130
    value = "#N/A"
    formula = "=F130-E130"
    @eval_fn
    def G130():
        f130_1 = Metric_4_5_7_8_Data_QC.F130()
        e130_1 = Metric_4_5_7_8_Data_QC.E130()
        var_1 = sub(f130_1, e130_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H130():
    # 'Metric_4_5_7_8_Data_QC'!H130
    value = "#N/A"
    formula = "=G130/E130"
    @eval_fn
    def H130():
        g130_1 = Metric_4_5_7_8_Data_QC.G130()
        e130_1 = Metric_4_5_7_8_Data_QC.E130()
        var_1 = divide(g130_1, e130_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B131():
    # 'Metric_4_5_7_8_Data_QC'!B131
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class C131():
    # 'Metric_4_5_7_8_Data_QC'!C131
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E131():
    # 'Metric_4_5_7_8_Data_QC'!E131
    value = 0
    formula = "=VLOOKUP(C131,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E131():
        c131_1 = Metric_4_5_7_8_Data_QC.C131()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c131_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F131():
    # 'Metric_4_5_7_8_Data_QC'!F131
    value = 16.1768643492
    formula = "=F120"
    @eval_fn
    def F131():
        f120_1 = Metric_4_5_7_8_Data_QC.F120()
        return f120_1

@register(Metric_4_5_7_8_Data_QC)
class B132():
    # 'Metric_4_5_7_8_Data_QC'!B132
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class C132():
    # 'Metric_4_5_7_8_Data_QC'!C132
    value = "DFACD"

@register(Metric_4_5_7_8_Data_QC)
class D132():
    # 'Metric_4_5_7_8_Data_QC'!D132
    value = "#N/A"
    formula = "=VLOOKUP(C132,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D132():
        c132_1 = Metric_4_5_7_8_Data_QC.C132()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c132_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E132():
    # 'Metric_4_5_7_8_Data_QC'!E132
    value = "#N/A"
    formula = "=VLOOKUP(C132,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E132():
        c132_1 = Metric_4_5_7_8_Data_QC.C132()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c132_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F132():
    # 'Metric_4_5_7_8_Data_QC'!F132
    value = 24.8346392139
    formula = "=F121"
    @eval_fn
    def F132():
        f121_1 = Metric_4_5_7_8_Data_QC.F121()
        return f121_1

@register(Metric_4_5_7_8_Data_QC)
class G132():
    # 'Metric_4_5_7_8_Data_QC'!G132
    value = "#N/A"
    formula = "=F132-E132"
    @eval_fn
    def G132():
        f132_1 = Metric_4_5_7_8_Data_QC.F132()
        e132_1 = Metric_4_5_7_8_Data_QC.E132()
        var_1 = sub(f132_1, e132_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H132():
    # 'Metric_4_5_7_8_Data_QC'!H132
    value = "#N/A"
    formula = "=G132/E132"
    @eval_fn
    def H132():
        g132_1 = Metric_4_5_7_8_Data_QC.G132()
        e132_1 = Metric_4_5_7_8_Data_QC.E132()
        var_1 = divide(g132_1, e132_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B133():
    # 'Metric_4_5_7_8_Data_QC'!B133
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class C133():
    # 'Metric_4_5_7_8_Data_QC'!C133
    value = "RFACD"

@register(Metric_4_5_7_8_Data_QC)
class D133():
    # 'Metric_4_5_7_8_Data_QC'!D133
    value = "#N/A"
    formula = "=VLOOKUP(C133,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D133():
        c133_1 = Metric_4_5_7_8_Data_QC.C133()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c133_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E133():
    # 'Metric_4_5_7_8_Data_QC'!E133
    value = "#N/A"
    formula = "=VLOOKUP(C133,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E133():
        c133_1 = Metric_4_5_7_8_Data_QC.C133()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c133_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F133():
    # 'Metric_4_5_7_8_Data_QC'!F133
    value = 9.28227559514
    formula = "=F122"
    @eval_fn
    def F133():
        f122_1 = Metric_4_5_7_8_Data_QC.F122()
        return f122_1

@register(Metric_4_5_7_8_Data_QC)
class G133():
    # 'Metric_4_5_7_8_Data_QC'!G133
    value = "#N/A"
    formula = "=F133-E133"
    @eval_fn
    def G133():
        f133_1 = Metric_4_5_7_8_Data_QC.F133()
        e133_1 = Metric_4_5_7_8_Data_QC.E133()
        var_1 = sub(f133_1, e133_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H133():
    # 'Metric_4_5_7_8_Data_QC'!H133
    value = "#N/A"
    formula = "=G133/E133"
    @eval_fn
    def H133():
        g133_1 = Metric_4_5_7_8_Data_QC.G133()
        e133_1 = Metric_4_5_7_8_Data_QC.E133()
        var_1 = divide(g133_1, e133_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B134():
    # 'Metric_4_5_7_8_Data_QC'!B134
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class C134():
    # 'Metric_4_5_7_8_Data_QC'!C134
    value = "LGACD"

@register(Metric_4_5_7_8_Data_QC)
class D134():
    # 'Metric_4_5_7_8_Data_QC'!D134
    value = "#N/A"
    formula = "=VLOOKUP(C134,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D134():
        c134_1 = Metric_4_5_7_8_Data_QC.C134()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c134_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E134():
    # 'Metric_4_5_7_8_Data_QC'!E134
    value = "#N/A"
    formula = "=VLOOKUP(C134,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E134():
        c134_1 = Metric_4_5_7_8_Data_QC.C134()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c134_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F134():
    # 'Metric_4_5_7_8_Data_QC'!F134
    value = 33.056826405
    formula = "=F123"
    @eval_fn
    def F134():
        f123_1 = Metric_4_5_7_8_Data_QC.F123()
        return f123_1

@register(Metric_4_5_7_8_Data_QC)
class G134():
    # 'Metric_4_5_7_8_Data_QC'!G134
    value = "#N/A"
    formula = "=F134-E134"
    @eval_fn
    def G134():
        f134_1 = Metric_4_5_7_8_Data_QC.F134()
        e134_1 = Metric_4_5_7_8_Data_QC.E134()
        var_1 = sub(f134_1, e134_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H134():
    # 'Metric_4_5_7_8_Data_QC'!H134
    value = "#N/A"
    formula = "=G134/E134"
    @eval_fn
    def H134():
        g134_1 = Metric_4_5_7_8_Data_QC.G134()
        e134_1 = Metric_4_5_7_8_Data_QC.E134()
        var_1 = divide(g134_1, e134_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B135():
    # 'Metric_4_5_7_8_Data_QC'!B135
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class C135():
    # 'Metric_4_5_7_8_Data_QC'!C135
    value = "NGACD"

@register(Metric_4_5_7_8_Data_QC)
class D135():
    # 'Metric_4_5_7_8_Data_QC'!D135
    value = "#N/A"
    formula = "=VLOOKUP(C135,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D135():
        c135_1 = Metric_4_5_7_8_Data_QC.C135()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c135_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E135():
    # 'Metric_4_5_7_8_Data_QC'!E135
    value = "#N/A"
    formula = "=VLOOKUP(C135,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E135():
        c135_1 = Metric_4_5_7_8_Data_QC.C135()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c135_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F135():
    # 'Metric_4_5_7_8_Data_QC'!F135
    value = 26.3019286205
    formula = "=F124"
    @eval_fn
    def F135():
        f124_1 = Metric_4_5_7_8_Data_QC.F124()
        return f124_1

@register(Metric_4_5_7_8_Data_QC)
class G135():
    # 'Metric_4_5_7_8_Data_QC'!G135
    value = "#N/A"
    formula = "=F135-E135"
    @eval_fn
    def G135():
        f135_1 = Metric_4_5_7_8_Data_QC.F135()
        e135_1 = Metric_4_5_7_8_Data_QC.E135()
        var_1 = sub(f135_1, e135_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H135():
    # 'Metric_4_5_7_8_Data_QC'!H135
    value = "#N/A"
    formula = "=G135/E135"
    @eval_fn
    def H135():
        g135_1 = Metric_4_5_7_8_Data_QC.G135()
        e135_1 = Metric_4_5_7_8_Data_QC.E135()
        var_1 = divide(g135_1, e135_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class A136():
    # 'Metric_4_5_7_8_Data_QC'!A136
    value = ".55 factor to divide biodiesel between transportation and power"

@register(Metric_4_5_7_8_Data_QC)
class B136():
    # 'Metric_4_5_7_8_Data_QC'!B136
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class C136():
    # 'Metric_4_5_7_8_Data_QC'!C136
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class E136():
    # 'Metric_4_5_7_8_Data_QC'!E136
    value = 0
    formula = "=VLOOKUP(C136,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E136():
        c136_1 = Metric_4_5_7_8_Data_QC.C136()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c136_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F136():
    # 'Metric_4_5_7_8_Data_QC'!F136
    value = 0
    formula = "=F125"
    @eval_fn
    def F136():
        f125_1 = Metric_4_5_7_8_Data_QC.F125()
        return f125_1

@register(Metric_4_5_7_8_Data_QC)
class B137():
    # 'Metric_4_5_7_8_Data_QC'!B137
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class C137():
    # 'Metric_4_5_7_8_Data_QC'!C137
    value = "EMACD"

@register(Metric_4_5_7_8_Data_QC)
class E137():
    # 'Metric_4_5_7_8_Data_QC'!E137
    value = "#N/A"
    formula = "=VLOOKUP(C137,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E137():
        c137_1 = Metric_4_5_7_8_Data_QC.C137()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c137_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F137():
    # 'Metric_4_5_7_8_Data_QC'!F137
    value = 28.0183469063
    formula = "=F126"
    @eval_fn
    def F137():
        f126_1 = Metric_4_5_7_8_Data_QC.F126()
        return f126_1

@register(Metric_4_5_7_8_Data_QC)
class G137():
    # 'Metric_4_5_7_8_Data_QC'!G137
    value = "#N/A"
    formula = "=F137-E137"
    @eval_fn
    def G137():
        f137_1 = Metric_4_5_7_8_Data_QC.F137()
        e137_1 = Metric_4_5_7_8_Data_QC.E137()
        var_1 = sub(f137_1, e137_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H137():
    # 'Metric_4_5_7_8_Data_QC'!H137
    value = "#N/A"
    formula = "=G137/E137"
    @eval_fn
    def H137():
        g137_1 = Metric_4_5_7_8_Data_QC.G137()
        e137_1 = Metric_4_5_7_8_Data_QC.E137()
        var_1 = divide(g137_1, e137_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class A139():
    # 'Metric_4_5_7_8_Data_QC'!A139
    value = "Air Transportation"

@register(Metric_4_5_7_8_Data_QC)
class B140():
    # 'Metric_4_5_7_8_Data_QC'!B140
    value = "Electrictiy"

@register(Metric_4_5_7_8_Data_QC)
class C140():
    # 'Metric_4_5_7_8_Data_QC'!C140
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class D140():
    # 'Metric_4_5_7_8_Data_QC'!D140
    value = 0
    formula = "=VLOOKUP(C140,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D140():
        c140_1 = Metric_4_5_7_8_Data_QC.C140()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c140_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E140():
    # 'Metric_4_5_7_8_Data_QC'!E140
    value = 0
    formula = "=VLOOKUP(C140,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E140():
        c140_1 = Metric_4_5_7_8_Data_QC.C140()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c140_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F140():
    # 'Metric_4_5_7_8_Data_QC'!F140
    value = 60.1061315
    formula = "=F129"
    @eval_fn
    def F140():
        f129_1 = Metric_4_5_7_8_Data_QC.F129()
        return f129_1

@register(Metric_4_5_7_8_Data_QC)
class B141():
    # 'Metric_4_5_7_8_Data_QC'!B141
    value = "Gasoline"

@register(Metric_4_5_7_8_Data_QC)
class C141():
    # 'Metric_4_5_7_8_Data_QC'!C141
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class D141():
    # 'Metric_4_5_7_8_Data_QC'!D141
    value = 0
    formula = "=VLOOKUP(C141,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D141():
        c141_1 = Metric_4_5_7_8_Data_QC.C141()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c141_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E141():
    # 'Metric_4_5_7_8_Data_QC'!E141
    value = 0
    formula = "=VLOOKUP(C141,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E141():
        c141_1 = Metric_4_5_7_8_Data_QC.C141()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c141_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F141():
    # 'Metric_4_5_7_8_Data_QC'!F141
    value = 24.5444170066
    formula = "=F130"
    @eval_fn
    def F141():
        f130_1 = Metric_4_5_7_8_Data_QC.F130()
        return f130_1

@register(Metric_4_5_7_8_Data_QC)
class B142():
    # 'Metric_4_5_7_8_Data_QC'!B142
    value = "Jet Fuel"

@register(Metric_4_5_7_8_Data_QC)
class C142():
    # 'Metric_4_5_7_8_Data_QC'!C142
    value = "JFACD"

@register(Metric_4_5_7_8_Data_QC)
class D142():
    # 'Metric_4_5_7_8_Data_QC'!D142
    value = "#N/A"
    formula = "=VLOOKUP(C142,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D142():
        c142_1 = Metric_4_5_7_8_Data_QC.C142()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c142_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E142():
    # 'Metric_4_5_7_8_Data_QC'!E142
    value = "#N/A"
    formula = "=VLOOKUP(C142,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E142():
        c142_1 = Metric_4_5_7_8_Data_QC.C142()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c142_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F142():
    # 'Metric_4_5_7_8_Data_QC'!F142
    value = 16.1768643492
    formula = "=F131"
    @eval_fn
    def F142():
        f131_1 = Metric_4_5_7_8_Data_QC.F131()
        return f131_1

@register(Metric_4_5_7_8_Data_QC)
class G142():
    # 'Metric_4_5_7_8_Data_QC'!G142
    value = "#N/A"
    formula = "=F142-E142"
    @eval_fn
    def G142():
        f142_1 = Metric_4_5_7_8_Data_QC.F142()
        e142_1 = Metric_4_5_7_8_Data_QC.E142()
        var_1 = sub(f142_1, e142_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class H142():
    # 'Metric_4_5_7_8_Data_QC'!H142
    value = "#N/A"
    formula = "=G142/E142"
    @eval_fn
    def H142():
        g142_1 = Metric_4_5_7_8_Data_QC.G142()
        e142_1 = Metric_4_5_7_8_Data_QC.E142()
        var_1 = divide(g142_1, e142_1)
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class B143():
    # 'Metric_4_5_7_8_Data_QC'!B143
    value = "Diesel"

@register(Metric_4_5_7_8_Data_QC)
class C143():
    # 'Metric_4_5_7_8_Data_QC'!C143
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class D143():
    # 'Metric_4_5_7_8_Data_QC'!D143
    value = 0
    formula = "=VLOOKUP(C143,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D143():
        c143_1 = Metric_4_5_7_8_Data_QC.C143()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c143_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E143():
    # 'Metric_4_5_7_8_Data_QC'!E143
    value = 0
    formula = "=VLOOKUP(C143,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E143():
        c143_1 = Metric_4_5_7_8_Data_QC.C143()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c143_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F143():
    # 'Metric_4_5_7_8_Data_QC'!F143
    value = 24.8346392139
    formula = "=F132"
    @eval_fn
    def F143():
        f132_1 = Metric_4_5_7_8_Data_QC.F132()
        return f132_1

@register(Metric_4_5_7_8_Data_QC)
class B144():
    # 'Metric_4_5_7_8_Data_QC'!B144
    value = "Fuel Oil"

@register(Metric_4_5_7_8_Data_QC)
class C144():
    # 'Metric_4_5_7_8_Data_QC'!C144
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class D144():
    # 'Metric_4_5_7_8_Data_QC'!D144
    value = 0
    formula = "=VLOOKUP(C144,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D144():
        c144_1 = Metric_4_5_7_8_Data_QC.C144()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c144_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E144():
    # 'Metric_4_5_7_8_Data_QC'!E144
    value = 0
    formula = "=VLOOKUP(C144,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E144():
        c144_1 = Metric_4_5_7_8_Data_QC.C144()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c144_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F144():
    # 'Metric_4_5_7_8_Data_QC'!F144
    value = 9.28227559514
    formula = "=F133"
    @eval_fn
    def F144():
        f133_1 = Metric_4_5_7_8_Data_QC.F133()
        return f133_1

@register(Metric_4_5_7_8_Data_QC)
class B145():
    # 'Metric_4_5_7_8_Data_QC'!B145
    value = "LPG"

@register(Metric_4_5_7_8_Data_QC)
class C145():
    # 'Metric_4_5_7_8_Data_QC'!C145
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class D145():
    # 'Metric_4_5_7_8_Data_QC'!D145
    value = 0
    formula = "=VLOOKUP(C145,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D145():
        c145_1 = Metric_4_5_7_8_Data_QC.C145()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c145_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E145():
    # 'Metric_4_5_7_8_Data_QC'!E145
    value = 0
    formula = "=VLOOKUP(C145,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E145():
        c145_1 = Metric_4_5_7_8_Data_QC.C145()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c145_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F145():
    # 'Metric_4_5_7_8_Data_QC'!F145
    value = 33.056826405
    formula = "=F134"
    @eval_fn
    def F145():
        f134_1 = Metric_4_5_7_8_Data_QC.F134()
        return f134_1

@register(Metric_4_5_7_8_Data_QC)
class B146():
    # 'Metric_4_5_7_8_Data_QC'!B146
    value = "SNG"

@register(Metric_4_5_7_8_Data_QC)
class C146():
    # 'Metric_4_5_7_8_Data_QC'!C146
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class D146():
    # 'Metric_4_5_7_8_Data_QC'!D146
    value = 0
    formula = "=VLOOKUP(C146,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D146():
        c146_1 = Metric_4_5_7_8_Data_QC.C146()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c146_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E146():
    # 'Metric_4_5_7_8_Data_QC'!E146
    value = 0
    formula = "=VLOOKUP(C146,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E146():
        c146_1 = Metric_4_5_7_8_Data_QC.C146()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c146_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F146():
    # 'Metric_4_5_7_8_Data_QC'!F146
    value = 26.3019286205
    formula = "=F135"
    @eval_fn
    def F146():
        f135_1 = Metric_4_5_7_8_Data_QC.F135()
        return f135_1

@register(Metric_4_5_7_8_Data_QC)
class B147():
    # 'Metric_4_5_7_8_Data_QC'!B147
    value = "Biodiesel"

@register(Metric_4_5_7_8_Data_QC)
class C147():
    # 'Metric_4_5_7_8_Data_QC'!C147
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class D147():
    # 'Metric_4_5_7_8_Data_QC'!D147
    value = 0
    formula = "=VLOOKUP(C147,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D147():
        c147_1 = Metric_4_5_7_8_Data_QC.C147()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c147_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E147():
    # 'Metric_4_5_7_8_Data_QC'!E147
    value = 0
    formula = "=VLOOKUP(C147,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E147():
        c147_1 = Metric_4_5_7_8_Data_QC.C147()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c147_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F147():
    # 'Metric_4_5_7_8_Data_QC'!F147
    value = 0
    formula = "=F136"
    @eval_fn
    def F147():
        f136_1 = Metric_4_5_7_8_Data_QC.F136()
        return f136_1

@register(Metric_4_5_7_8_Data_QC)
class B148():
    # 'Metric_4_5_7_8_Data_QC'!B148
    value = "Ethanol"

@register(Metric_4_5_7_8_Data_QC)
class C148():
    # 'Metric_4_5_7_8_Data_QC'!C148
    value = "-"

@register(Metric_4_5_7_8_Data_QC)
class D148():
    # 'Metric_4_5_7_8_Data_QC'!D148
    value = 0
    formula = "=VLOOKUP(C148,'EIA Consumption'!$C:$BZ,3,FALSE)"
    @eval_fn
    def D148():
        c148_1 = Metric_4_5_7_8_Data_QC.C148()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        var_1 = VLOOKUP(c148_1, range_1, 3, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class E148():
    # 'Metric_4_5_7_8_Data_QC'!E148
    value = 0
    formula = "=VLOOKUP(C148,'EIA Consumption'!$C:$BZ,'Dashboard M4 Cost Monthly'!$G$1,FALSE)"
    @eval_fn
    def E148():
        c148_1 = Metric_4_5_7_8_Data_QC.C148()
        range_1 = EIA_Consumption(3, 0, 78, 0)
        g1_1 = Dashboard_M4_Cost_Monthly.G1()
        var_1 = VLOOKUP(c148_1, range_1, g1_1, "FALSE")
        return var_1

@register(Metric_4_5_7_8_Data_QC)
class F148():
    # 'Metric_4_5_7_8_Data_QC'!F148
    value = 28.0183469063
    formula = "=F137"
    @eval_fn
    def F148():
        f137_1 = Metric_4_5_7_8_Data_QC.F137()
        return f137_1

@register(Metric_4_5_7_8_Data_QC)
class E149():
    # 'Metric_4_5_7_8_Data_QC'!E149
    value = "#N/A"
    formula = "=SUM(E96:E148)"
    @eval_fn
    def E149():
        range_1 = Metric_4_5_7_8_Data_QC(5, 96, 5, 148)
        var_1 = SUM(range_1)
        return var_1