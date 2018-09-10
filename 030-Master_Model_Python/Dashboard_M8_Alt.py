# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Dashboard_M8_Alt = Worksheet('Dashboard_M8_Alt', 10, 10)



@register(Dashboard_M8_Alt)
class A1():
    # 'Dashboard_M8_Alt'!A1
    value = "Metric 8: Maintaining affordability of energy costs (Alternative Calculation)"

@register(Dashboard_M8_Alt)
class F1():
    # 'Dashboard_M8_Alt'!F1
    value = "Notes"

@register(Dashboard_M8_Alt)
class A2():
    # 'Dashboard_M8_Alt'!A2
    value = "Variable BEC(2005): Baseline Electricity Consumption in 2005"
    formula = '''="Variable BEC("&D4&"): Baseline Electricity Consumption in "&D4'''
    @eval_fn
    def A2():
        d4_1 = Dashboard_M8_Alt.D4()
        var_1 = concat("Variable BEC(", d4_1)
        var_2 = concat(var_1, "): Baseline Electricity Consumption in ")
        d4_2 = Dashboard_M8_Alt.D4()
        var_3 = concat(var_2, d4_2)
        return var_3

@register(Dashboard_M8_Alt)
class C2():
    # 'Dashboard_M8_Alt'!C2
    value = "Note: Data point taken from EIA Consumption"

@register(Dashboard_M8_Alt)
class M2():
    # 'Dashboard_M8_Alt'!M2
    value = '''Note: Results from this calculation are only valid when viewed as "All Fuels"'''

@register(Dashboard_M8_Alt)
class C3():
    # 'Dashboard_M8_Alt'!C3
    value = "Source"

@register(Dashboard_M8_Alt)
class B4():
    # 'Dashboard_M8_Alt'!B4
    value = "Year:"

@register(Dashboard_M8_Alt)
class D4():
    # 'Dashboard_M8_Alt'!D4
    value = 2005

@register(Dashboard_M8_Alt)
class A5():
    # 'Dashboard_M8_Alt'!A5
    value = "ESTXP"

@register(Dashboard_M8_Alt)
class B5():
    # 'Dashboard_M8_Alt'!B5
    value = "Fossil-Based Electricity consumed (Million kWh)"

@register(Dashboard_M8_Alt)
class C5():
    # 'Dashboard_M8_Alt'!C5
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(Dashboard_M8_Alt)
class D5():
    # 'Dashboard_M8_Alt'!D5
    value = 9850.72312093
    formula = "=HLOOKUP(D4,G24:AA28,5,FALSE)"
    @eval_fn
    def D5():
        d4_1 = Dashboard_M8_Alt.D4()
        range_1 = Dashboard_M8_Alt(7, 24, 27, 28)
        var_1 = HLOOKUP(d4_1, range_1, 5, "FALSE")
        return var_1

@register(Dashboard_M8_Alt)
class A7():
    # 'Dashboard_M8_Alt'!A7
    value = "Variable FC(2005,c,p): Fuel Consumed in Power Sector in 2005"
    formula = '''="Variable FC("&D4&",c,p): Fuel Consumed in Power Sector in "&D4'''
    @eval_fn
    def A7():
        d4_1 = Dashboard_M8_Alt.D4()
        var_1 = concat("Variable FC(", d4_1)
        var_2 = concat(var_1, ",c,p): Fuel Consumed in Power Sector in ")
        d4_2 = Dashboard_M8_Alt.D4()
        var_3 = concat(var_2, d4_2)
        return var_3

@register(Dashboard_M8_Alt)
class C7():
    # 'Dashboard_M8_Alt'!C7
    value = "Note: Data taken from EIA Consumption"

@register(Dashboard_M8_Alt)
class C8():
    # 'Dashboard_M8_Alt'!C8
    value = "Source"

@register(Dashboard_M8_Alt)
class D9():
    # 'Dashboard_M8_Alt'!D9
    value = "Billion Btu"

@register(Dashboard_M8_Alt)
class A10():
    # 'Dashboard_M8_Alt'!A10
    value = "DKEIB"

@register(Dashboard_M8_Alt)
class B10():
    # 'Dashboard_M8_Alt'!B10
    value = "Diesel"

@register(Dashboard_M8_Alt)
class C10():
    # 'Dashboard_M8_Alt'!C10
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(Dashboard_M8_Alt)
class D10():
    # 'Dashboard_M8_Alt'!D10
    value = 15053
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!D4,'EIA Consumption'!$E$50:$CD$50)"
    @eval_fn
    def D10():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        d4_1 = Dashboard_M8_Alt.D4()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, d4_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class A11():
    # 'Dashboard_M8_Alt'!A11
    value = "RFEIB"

@register(Dashboard_M8_Alt)
class B11():
    # 'Dashboard_M8_Alt'!B11
    value = "Fuel Oil"

@register(Dashboard_M8_Alt)
class C11():
    # 'Dashboard_M8_Alt'!C11
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(Dashboard_M8_Alt)
class D11():
    # 'Dashboard_M8_Alt'!D11
    value = 71070
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,D4,'EIA Consumption'!$E$246:$CD$246)"
    @eval_fn
    def D11():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        d4_1 = Dashboard_M8_Alt.D4()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, d4_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class A12():
    # 'Dashboard_M8_Alt'!A12
    value = "NGEIB"

@register(Dashboard_M8_Alt)
class B12():
    # 'Dashboard_M8_Alt'!B12
    value = "SNG"

@register(Dashboard_M8_Alt)
class C12():
    # 'Dashboard_M8_Alt'!C12
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(Dashboard_M8_Alt)
class D12():
    # 'Dashboard_M8_Alt'!D12
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!D4,'EIA Consumption'!$E$176:$CD$176)"
    @eval_fn
    def D12():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        d4_1 = Dashboard_M8_Alt.D4()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, d4_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class A13():
    # 'Dashboard_M8_Alt'!A13
    value = "CLEIB"

@register(Dashboard_M8_Alt)
class B13():
    # 'Dashboard_M8_Alt'!B13
    value = "Coal"

@register(Dashboard_M8_Alt)
class C13():
    # 'Dashboard_M8_Alt'!C13
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(Dashboard_M8_Alt)
class D13():
    # 'Dashboard_M8_Alt'!D13
    value = 16545
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!D4,'EIA Consumption'!$E$22:$CD$22)"
    @eval_fn
    def D13():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        d4_1 = Dashboard_M8_Alt.D4()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, d4_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class B14():
    # 'Dashboard_M8_Alt'!B14
    value = "All Fuels"

@register(Dashboard_M8_Alt)
class D14():
    # 'Dashboard_M8_Alt'!D14
    value = 102668
    formula = "=SUM(D10:D13)"
    @eval_fn
    def D14():
        range_1 = Dashboard_M8_Alt(4, 10, 4, 13)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class A15():
    # 'Dashboard_M8_Alt'!A15
    value = "Variable HR(2005,c,p): Aggregate Sales Heat Rate for power sector by fuel in 2005"
    formula = '''="Variable HR("&D4&",c,p): Aggregate Sales Heat Rate for power sector by fuel in "&D4'''
    @eval_fn
    def A15():
        d4_1 = Dashboard_M8_Alt.D4()
        var_1 = concat("Variable HR(", d4_1)
        var_2 = concat(var_1, ",c,p): Aggregate Sales Heat Rate for power sector by fuel in ")
        d4_2 = Dashboard_M8_Alt.D4()
        var_3 = concat(var_2, d4_2)
        return var_3

@register(Dashboard_M8_Alt)
class C15():
    # 'Dashboard_M8_Alt'!C15
    value = "Divide Billion Btu by Million kWh and multiply by 1,000"

@register(Dashboard_M8_Alt)
class C17():
    # 'Dashboard_M8_Alt'!C17
    value = "Source"

@register(Dashboard_M8_Alt)
class D18():
    # 'Dashboard_M8_Alt'!D18
    value = "Btu/kWh"

@register(Dashboard_M8_Alt)
class A19():
    # 'Dashboard_M8_Alt'!A19
    value = "DKEIB"

@register(Dashboard_M8_Alt)
class B19():
    # 'Dashboard_M8_Alt'!B19
    value = "Diesel"

@register(Dashboard_M8_Alt)
class C19():
    # 'Dashboard_M8_Alt'!C19
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(Dashboard_M8_Alt)
class D19():
    # 'Dashboard_M8_Alt'!D19
    value = 1528.11116658
    formula = "=D10/($D$5/1000)"
    @eval_fn
    def D19():
        d10_1 = Dashboard_M8_Alt.D10()
        d5_1 = Dashboard_M8_Alt.D5()
        var_1 = divide(d5_1, 1000)
        var_2 = divide(d10_1, var_1)
        return var_2

@register(Dashboard_M8_Alt)
class A20():
    # 'Dashboard_M8_Alt'!A20
    value = "RFEIB"

@register(Dashboard_M8_Alt)
class B20():
    # 'Dashboard_M8_Alt'!B20
    value = "Fuel Oil"

@register(Dashboard_M8_Alt)
class C20():
    # 'Dashboard_M8_Alt'!C20
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(Dashboard_M8_Alt)
class D20():
    # 'Dashboard_M8_Alt'!D20
    value = 7214.69877161
    formula = "=D11/($D$5/1000)"
    @eval_fn
    def D20():
        d11_1 = Dashboard_M8_Alt.D11()
        d5_1 = Dashboard_M8_Alt.D5()
        var_1 = divide(d5_1, 1000)
        var_2 = divide(d11_1, var_1)
        return var_2

@register(Dashboard_M8_Alt)
class A21():
    # 'Dashboard_M8_Alt'!A21
    value = "NGEIB"

@register(Dashboard_M8_Alt)
class B21():
    # 'Dashboard_M8_Alt'!B21
    value = "SNG"

@register(Dashboard_M8_Alt)
class C21():
    # 'Dashboard_M8_Alt'!C21
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(Dashboard_M8_Alt)
class D21():
    # 'Dashboard_M8_Alt'!D21
    value = 0
    formula = "=D12/($D$5/1000)"
    @eval_fn
    def D21():
        d12_1 = Dashboard_M8_Alt.D12()
        d5_1 = Dashboard_M8_Alt.D5()
        var_1 = divide(d5_1, 1000)
        var_2 = divide(d12_1, var_1)
        return var_2

@register(Dashboard_M8_Alt)
class A22():
    # 'Dashboard_M8_Alt'!A22
    value = "CLEIB"

@register(Dashboard_M8_Alt)
class B22():
    # 'Dashboard_M8_Alt'!B22
    value = "Coal"

@register(Dashboard_M8_Alt)
class C22():
    # 'Dashboard_M8_Alt'!C22
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(Dashboard_M8_Alt)
class D22():
    # 'Dashboard_M8_Alt'!D22
    value = 1679.57212855
    formula = "=D13/($D$5/1000)"
    @eval_fn
    def D22():
        d13_1 = Dashboard_M8_Alt.D13()
        d5_1 = Dashboard_M8_Alt.D5()
        var_1 = divide(d5_1, 1000)
        var_2 = divide(d13_1, var_1)
        return var_2

@register(Dashboard_M8_Alt)
class B23():
    # 'Dashboard_M8_Alt'!B23
    value = "All Fuels"

@register(Dashboard_M8_Alt)
class D23():
    # 'Dashboard_M8_Alt'!D23
    value = 10422.3820667
    formula = "=D14/($D$5/1000)"
    @eval_fn
    def D23():
        d14_1 = Dashboard_M8_Alt.D14()
        d5_1 = Dashboard_M8_Alt.D5()
        var_1 = divide(d5_1, 1000)
        var_2 = divide(d14_1, var_1)
        return var_2

@register(Dashboard_M8_Alt)
class G24():
    # 'Dashboard_M8_Alt'!G24
    value = 2000

@register(Dashboard_M8_Alt)
class H24():
    # 'Dashboard_M8_Alt'!H24
    value = 2001

@register(Dashboard_M8_Alt)
class I24():
    # 'Dashboard_M8_Alt'!I24
    value = 2002

@register(Dashboard_M8_Alt)
class J24():
    # 'Dashboard_M8_Alt'!J24
    value = 2003

@register(Dashboard_M8_Alt)
class K24():
    # 'Dashboard_M8_Alt'!K24
    value = 2004

@register(Dashboard_M8_Alt)
class L24():
    # 'Dashboard_M8_Alt'!L24
    value = 2005

@register(Dashboard_M8_Alt)
class M24():
    # 'Dashboard_M8_Alt'!M24
    value = 2006

@register(Dashboard_M8_Alt)
class N24():
    # 'Dashboard_M8_Alt'!N24
    value = 2007

@register(Dashboard_M8_Alt)
class O24():
    # 'Dashboard_M8_Alt'!O24
    value = 2008

@register(Dashboard_M8_Alt)
class P24():
    # 'Dashboard_M8_Alt'!P24
    value = 2009

@register(Dashboard_M8_Alt)
class Q24():
    # 'Dashboard_M8_Alt'!Q24
    value = 2010

@register(Dashboard_M8_Alt)
class R24():
    # 'Dashboard_M8_Alt'!R24
    value = 2011

@register(Dashboard_M8_Alt)
class S24():
    # 'Dashboard_M8_Alt'!S24
    value = 2012

@register(Dashboard_M8_Alt)
class T24():
    # 'Dashboard_M8_Alt'!T24
    value = 2013

@register(Dashboard_M8_Alt)
class U24():
    # 'Dashboard_M8_Alt'!U24
    value = 2014

@register(Dashboard_M8_Alt)
class V24():
    # 'Dashboard_M8_Alt'!V24
    value = 2015

@register(Dashboard_M8_Alt)
class W24():
    # 'Dashboard_M8_Alt'!W24
    value = 2016

@register(Dashboard_M8_Alt)
class X24():
    # 'Dashboard_M8_Alt'!X24
    value = 2017

@register(Dashboard_M8_Alt)
class Y24():
    # 'Dashboard_M8_Alt'!Y24
    value = 2018

@register(Dashboard_M8_Alt)
class Z24():
    # 'Dashboard_M8_Alt'!Z24
    value = 2019

@register(Dashboard_M8_Alt)
class AA24():
    # 'Dashboard_M8_Alt'!AA24
    value = 2020

@register(Dashboard_M8_Alt)
class AB24():
    # 'Dashboard_M8_Alt'!AB24
    value = 2021

@register(Dashboard_M8_Alt)
class AC24():
    # 'Dashboard_M8_Alt'!AC24
    value = 2022

@register(Dashboard_M8_Alt)
class AD24():
    # 'Dashboard_M8_Alt'!AD24
    value = 2023

@register(Dashboard_M8_Alt)
class AE24():
    # 'Dashboard_M8_Alt'!AE24
    value = 2024

@register(Dashboard_M8_Alt)
class AF24():
    # 'Dashboard_M8_Alt'!AF24
    value = 2025

@register(Dashboard_M8_Alt)
class AG24():
    # 'Dashboard_M8_Alt'!AG24
    value = 2026

@register(Dashboard_M8_Alt)
class AH24():
    # 'Dashboard_M8_Alt'!AH24
    value = 2027

@register(Dashboard_M8_Alt)
class AI24():
    # 'Dashboard_M8_Alt'!AI24
    value = 2028

@register(Dashboard_M8_Alt)
class AJ24():
    # 'Dashboard_M8_Alt'!AJ24
    value = 2029

@register(Dashboard_M8_Alt)
class AK24():
    # 'Dashboard_M8_Alt'!AK24
    value = 2030

@register(Dashboard_M8_Alt)
class A25():
    # 'Dashboard_M8_Alt'!A25
    value = "Variable ES(y): Electricity sales by Year"

@register(Dashboard_M8_Alt)
class D26():
    # 'Dashboard_M8_Alt'!D26
    value = "Source"

@register(Dashboard_M8_Alt)
class B27():
    # 'Dashboard_M8_Alt'!B27
    value = "Total Electricity consumed (Million kWh)"

@register(Dashboard_M8_Alt)
class C27():
    # 'Dashboard_M8_Alt'!C27
    value = "Million kWh"

@register(Dashboard_M8_Alt)
class D27():
    # 'Dashboard_M8_Alt'!D27
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://dms.puc.hawaii.gov/dms/OpenDocServlet?RT=&document_id=91+3+ICM4+LSDB15+PC_DocketReport59+26+A1001001A12D04B24000E5143818+A12D04B24000E514381+14+1960'''

@register(Dashboard_M8_Alt)
class G27():
    # 'Dashboard_M8_Alt'!G27
    value = 9724.699
    formula = "='Input RPS'!H129/1000"
    @eval_fn
    def G27():
        h129_1 = Input_RPS.H129()
        var_1 = divide(h129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class H27():
    # 'Dashboard_M8_Alt'!H27
    value = 9813.798
    formula = "='Input RPS'!I129/1000"
    @eval_fn
    def H27():
        i129_1 = Input_RPS.I129()
        var_1 = divide(i129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class I27():
    # 'Dashboard_M8_Alt'!I27
    value = 9996.631
    formula = "='Input RPS'!J129/1000"
    @eval_fn
    def I27():
        j129_1 = Input_RPS.J129()
        var_1 = divide(j129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class J27():
    # 'Dashboard_M8_Alt'!J27
    value = 10213.768
    formula = "='Input RPS'!K129/1000"
    @eval_fn
    def J27():
        k129_1 = Input_RPS.K129()
        var_1 = divide(k129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class K27():
    # 'Dashboard_M8_Alt'!K27
    value = 10536.608
    formula = "='Input RPS'!L129/1000"
    @eval_fn
    def K27():
        l129_1 = Input_RPS.L129()
        var_1 = divide(l129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class L27():
    # 'Dashboard_M8_Alt'!L27
    value = 10567.255
    formula = "='Input RPS'!M129/1000"
    @eval_fn
    def L27():
        m129_1 = Input_RPS.M129()
        var_1 = divide(m129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class M27():
    # 'Dashboard_M8_Alt'!M27
    value = 10597.461
    formula = "='Input RPS'!N129/1000"
    @eval_fn
    def M27():
        n129_1 = Input_RPS.N129()
        var_1 = divide(n129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class N27():
    # 'Dashboard_M8_Alt'!N27
    value = 10614.718
    formula = "='Input RPS'!O129/1000"
    @eval_fn
    def N27():
        o129_1 = Input_RPS.O129()
        var_1 = divide(o129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class O27():
    # 'Dashboard_M8_Alt'!O27
    value = 10413.168
    formula = "='Input RPS'!P129/1000"
    @eval_fn
    def O27():
        p129_1 = Input_RPS.P129()
        var_1 = divide(p129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class P27():
    # 'Dashboard_M8_Alt'!P27
    value = 10150.174
    formula = "='Input RPS'!Q129/1000"
    @eval_fn
    def P27():
        q129_1 = Input_RPS.Q129()
        var_1 = divide(q129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class Q27():
    # 'Dashboard_M8_Alt'!Q27
    value = 10035.845
    formula = "='Input RPS'!R129/1000"
    @eval_fn
    def Q27():
        r129_1 = Input_RPS.R129()
        var_1 = divide(r129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class R27():
    # 'Dashboard_M8_Alt'!R27
    value = 9987.88
    formula = "='Input RPS'!S129/1000"
    @eval_fn
    def R27():
        s129_1 = Input_RPS.S129()
        var_1 = divide(s129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class S27():
    # 'Dashboard_M8_Alt'!S27
    value = 9639.158
    formula = "='Input RPS'!T129/1000"
    @eval_fn
    def S27():
        t129_1 = Input_RPS.T129()
        var_1 = divide(t129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class T27():
    # 'Dashboard_M8_Alt'!T27
    value = 9500.991
    formula = "='Input RPS'!U129/1000"
    @eval_fn
    def T27():
        u129_1 = Input_RPS.U129()
        var_1 = divide(u129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class U27():
    # 'Dashboard_M8_Alt'!U27
    value = 9406.166
    formula = "='Input RPS'!V129/1000"
    @eval_fn
    def U27():
        v129_1 = Input_RPS.V129()
        var_1 = divide(v129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class V27():
    # 'Dashboard_M8_Alt'!V27
    value = 9388.576
    formula = "='Input RPS'!W129/1000"
    @eval_fn
    def V27():
        w129_1 = Input_RPS.W129()
        var_1 = divide(w129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class W27():
    # 'Dashboard_M8_Alt'!W27
    value = 0
    formula = "='Input RPS'!X129/1000"
    @eval_fn
    def W27():
        x129_1 = Input_RPS.X129()
        var_1 = divide(x129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class X27():
    # 'Dashboard_M8_Alt'!X27
    value = 0
    formula = "='Input RPS'!Y129/1000"
    @eval_fn
    def X27():
        y129_1 = Input_RPS.Y129()
        var_1 = divide(y129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class Y27():
    # 'Dashboard_M8_Alt'!Y27
    value = 0
    formula = "='Input RPS'!Z129/1000"
    @eval_fn
    def Y27():
        z129_1 = Input_RPS.Z129()
        var_1 = divide(z129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class Z27():
    # 'Dashboard_M8_Alt'!Z27
    value = 0
    formula = "='Input RPS'!AA129/1000"
    @eval_fn
    def Z27():
        aa129_1 = Input_RPS.AA129()
        var_1 = divide(aa129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AA27():
    # 'Dashboard_M8_Alt'!AA27
    value = 0
    formula = "='Input RPS'!AB129/1000"
    @eval_fn
    def AA27():
        ab129_1 = Input_RPS.AB129()
        var_1 = divide(ab129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AB27():
    # 'Dashboard_M8_Alt'!AB27
    value = 0
    formula = "='Input RPS'!AC129/1000"
    @eval_fn
    def AB27():
        ac129_1 = Input_RPS.AC129()
        var_1 = divide(ac129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AC27():
    # 'Dashboard_M8_Alt'!AC27
    value = 0
    formula = "='Input RPS'!AD129/1000"
    @eval_fn
    def AC27():
        ad129_1 = Input_RPS.AD129()
        var_1 = divide(ad129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AD27():
    # 'Dashboard_M8_Alt'!AD27
    value = 0
    formula = "='Input RPS'!AE129/1000"
    @eval_fn
    def AD27():
        ae129_1 = Input_RPS.AE129()
        var_1 = divide(ae129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AE27():
    # 'Dashboard_M8_Alt'!AE27
    value = 0
    formula = "='Input RPS'!AF129/1000"
    @eval_fn
    def AE27():
        af129_1 = Input_RPS.AF129()
        var_1 = divide(af129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AF27():
    # 'Dashboard_M8_Alt'!AF27
    value = 0
    formula = "='Input RPS'!AG129/1000"
    @eval_fn
    def AF27():
        ag129_1 = Input_RPS.AG129()
        var_1 = divide(ag129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AG27():
    # 'Dashboard_M8_Alt'!AG27
    value = 0
    formula = "='Input RPS'!AH129/1000"
    @eval_fn
    def AG27():
        ah129_1 = Input_RPS.AH129()
        var_1 = divide(ah129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AH27():
    # 'Dashboard_M8_Alt'!AH27
    value = 0
    formula = "='Input RPS'!AI129/1000"
    @eval_fn
    def AH27():
        ai129_1 = Input_RPS.AI129()
        var_1 = divide(ai129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AI27():
    # 'Dashboard_M8_Alt'!AI27
    value = 0
    formula = "='Input RPS'!AJ129/1000"
    @eval_fn
    def AI27():
        aj129_1 = Input_RPS.AJ129()
        var_1 = divide(aj129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AJ27():
    # 'Dashboard_M8_Alt'!AJ27
    value = 0
    formula = "='Input RPS'!AK129/1000"
    @eval_fn
    def AJ27():
        ak129_1 = Input_RPS.AK129()
        var_1 = divide(ak129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class AK27():
    # 'Dashboard_M8_Alt'!AK27
    value = 0
    formula = "='Input RPS'!AL129/1000"
    @eval_fn
    def AK27():
        al129_1 = Input_RPS.AL129()
        var_1 = divide(al129_1, 1000)
        return var_1

@register(Dashboard_M8_Alt)
class B28():
    # 'Dashboard_M8_Alt'!B28
    value = "Total Fossil-Based Electricity Consumed (Million kWh)"

@register(Dashboard_M8_Alt)
class C28():
    # 'Dashboard_M8_Alt'!C28
    value = "Million kWh"

@register(Dashboard_M8_Alt)
class D28():
    # 'Dashboard_M8_Alt'!D28
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://dms.puc.hawaii.gov/dms/OpenDocServlet?RT=&document_id=91+3+ICM4+LSDB15+PC_DocketReport59+26+A1001001A12D04B24000E5143818+A12D04B24000E514381+14+1960'''

@register(Dashboard_M8_Alt)
class G28():
    # 'Dashboard_M8_Alt'!G28
    value = 9043.699
    formula = "=('Input RPS'!H129-'Input RPS'!H97)/1000"
    @eval_fn
    def G28():
        h129_1 = Input_RPS.H129()
        h97_1 = Input_RPS.H97()
        var_1 = sub(h129_1, h97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class H28():
    # 'Dashboard_M8_Alt'!H28
    value = 9198.798
    formula = "=('Input RPS'!I129-'Input RPS'!I97)/1000"
    @eval_fn
    def H28():
        i129_1 = Input_RPS.I129()
        i97_1 = Input_RPS.I97()
        var_1 = sub(i129_1, i97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class I28():
    # 'Dashboard_M8_Alt'!I28
    value = 9477.631
    formula = "=('Input RPS'!J129-'Input RPS'!J97)/1000"
    @eval_fn
    def I28():
        j129_1 = Input_RPS.J129()
        j97_1 = Input_RPS.J97()
        var_1 = sub(j129_1, j97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class J28():
    # 'Dashboard_M8_Alt'!J28
    value = 9537.612
    formula = "=('Input RPS'!K129-'Input RPS'!K97)/1000"
    @eval_fn
    def J28():
        k129_1 = Input_RPS.K129()
        k97_1 = Input_RPS.K97()
        var_1 = sub(k129_1, k97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class K28():
    # 'Dashboard_M8_Alt'!K28
    value = 9798.67
    formula = "=('Input RPS'!L129-'Input RPS'!L97)/1000"
    @eval_fn
    def K28():
        l129_1 = Input_RPS.L129()
        l97_1 = Input_RPS.L97()
        var_1 = sub(l129_1, l97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class L28():
    # 'Dashboard_M8_Alt'!L28
    value = 9850.72312093
    formula = "=('Input RPS'!M129-'Input RPS'!M97)/1000"
    @eval_fn
    def L28():
        m129_1 = Input_RPS.M129()
        m97_1 = Input_RPS.M97()
        var_1 = sub(m129_1, m97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class M28():
    # 'Dashboard_M8_Alt'!M28
    value = 9732.12579754
    formula = "=('Input RPS'!N129-'Input RPS'!N97)/1000"
    @eval_fn
    def M28():
        n129_1 = Input_RPS.N129()
        n97_1 = Input_RPS.N97()
        var_1 = sub(n129_1, n97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class N28():
    # 'Dashboard_M8_Alt'!N28
    value = 9668.8094166
    formula = "=('Input RPS'!O129-'Input RPS'!O97)/1000"
    @eval_fn
    def N28():
        o129_1 = Input_RPS.O129()
        o97_1 = Input_RPS.O97()
        var_1 = sub(o129_1, o97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class O28():
    # 'Dashboard_M8_Alt'!O28
    value = 9435.569184
    formula = "=('Input RPS'!P129-'Input RPS'!P97)/1000"
    @eval_fn
    def O28():
        p129_1 = Input_RPS.P129()
        p97_1 = Input_RPS.P97()
        var_1 = sub(p129_1, p97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class P28():
    # 'Dashboard_M8_Alt'!P28
    value = 9185.356736
    formula = "=('Input RPS'!Q129-'Input RPS'!Q97)/1000"
    @eval_fn
    def P28():
        q129_1 = Input_RPS.Q129()
        q97_1 = Input_RPS.Q97()
        var_1 = sub(q129_1, q97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Q28():
    # 'Dashboard_M8_Alt'!Q28
    value = 9084.427227
    formula = "=('Input RPS'!R129-'Input RPS'!R97)/1000"
    @eval_fn
    def Q28():
        r129_1 = Input_RPS.R129()
        r97_1 = Input_RPS.R97()
        var_1 = sub(r129_1, r97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class R28():
    # 'Dashboard_M8_Alt'!R28
    value = 8798.60689
    formula = "=('Input RPS'!S129-'Input RPS'!S97)/1000"
    @eval_fn
    def R28():
        s129_1 = Input_RPS.S129()
        s97_1 = Input_RPS.S97()
        var_1 = sub(s129_1, s97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class S28():
    # 'Dashboard_M8_Alt'!S28
    value = 8308.860235
    formula = "=('Input RPS'!T129-'Input RPS'!T97)/1000"
    @eval_fn
    def S28():
        t129_1 = Input_RPS.T129()
        t97_1 = Input_RPS.T97()
        var_1 = sub(t129_1, t97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class T28():
    # 'Dashboard_M8_Alt'!T28
    value = 7782.42447175
    formula = "=('Input RPS'!U129-'Input RPS'!U97)/1000"
    @eval_fn
    def T28():
        u129_1 = Input_RPS.U129()
        u97_1 = Input_RPS.U97()
        var_1 = sub(u129_1, u97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class U28():
    # 'Dashboard_M8_Alt'!U28
    value = 7401.99905637
    formula = "=('Input RPS'!V129-'Input RPS'!V97)/1000"
    @eval_fn
    def U28():
        v129_1 = Input_RPS.V129()
        v97_1 = Input_RPS.V97()
        var_1 = sub(v129_1, v97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class V28():
    # 'Dashboard_M8_Alt'!V28
    value = 7189.79
    formula = "=('Input RPS'!W129-'Input RPS'!W97)/1000"
    @eval_fn
    def V28():
        w129_1 = Input_RPS.W129()
        w97_1 = Input_RPS.W97()
        var_1 = sub(w129_1, w97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class W28():
    # 'Dashboard_M8_Alt'!W28
    value = 0
    formula = "=('Input RPS'!X129-'Input RPS'!X97)/1000"
    @eval_fn
    def W28():
        x129_1 = Input_RPS.X129()
        x97_1 = Input_RPS.X97()
        var_1 = sub(x129_1, x97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class X28():
    # 'Dashboard_M8_Alt'!X28
    value = 0
    formula = "=('Input RPS'!Y129-'Input RPS'!Y97)/1000"
    @eval_fn
    def X28():
        y129_1 = Input_RPS.Y129()
        y97_1 = Input_RPS.Y97()
        var_1 = sub(y129_1, y97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Y28():
    # 'Dashboard_M8_Alt'!Y28
    value = 0
    formula = "=('Input RPS'!Z129-'Input RPS'!Z97)/1000"
    @eval_fn
    def Y28():
        z129_1 = Input_RPS.Z129()
        z97_1 = Input_RPS.Z97()
        var_1 = sub(z129_1, z97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Z28():
    # 'Dashboard_M8_Alt'!Z28
    value = 0
    formula = "=('Input RPS'!AA129-'Input RPS'!AA97)/1000"
    @eval_fn
    def Z28():
        aa129_1 = Input_RPS.AA129()
        aa97_1 = Input_RPS.AA97()
        var_1 = sub(aa129_1, aa97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AA28():
    # 'Dashboard_M8_Alt'!AA28
    value = 0
    formula = "=('Input RPS'!AB129-'Input RPS'!AB97)/1000"
    @eval_fn
    def AA28():
        ab129_1 = Input_RPS.AB129()
        ab97_1 = Input_RPS.AB97()
        var_1 = sub(ab129_1, ab97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AB28():
    # 'Dashboard_M8_Alt'!AB28
    value = 0
    formula = "=('Input RPS'!AC129-'Input RPS'!AC97)/1000"
    @eval_fn
    def AB28():
        ac129_1 = Input_RPS.AC129()
        ac97_1 = Input_RPS.AC97()
        var_1 = sub(ac129_1, ac97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AC28():
    # 'Dashboard_M8_Alt'!AC28
    value = 0
    formula = "=('Input RPS'!AD129-'Input RPS'!AD97)/1000"
    @eval_fn
    def AC28():
        ad129_1 = Input_RPS.AD129()
        ad97_1 = Input_RPS.AD97()
        var_1 = sub(ad129_1, ad97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AD28():
    # 'Dashboard_M8_Alt'!AD28
    value = 0
    formula = "=('Input RPS'!AE129-'Input RPS'!AE97)/1000"
    @eval_fn
    def AD28():
        ae129_1 = Input_RPS.AE129()
        ae97_1 = Input_RPS.AE97()
        var_1 = sub(ae129_1, ae97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AE28():
    # 'Dashboard_M8_Alt'!AE28
    value = 0
    formula = "=('Input RPS'!AF129-'Input RPS'!AF97)/1000"
    @eval_fn
    def AE28():
        af129_1 = Input_RPS.AF129()
        af97_1 = Input_RPS.AF97()
        var_1 = sub(af129_1, af97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AF28():
    # 'Dashboard_M8_Alt'!AF28
    value = 0
    formula = "=('Input RPS'!AG129-'Input RPS'!AG97)/1000"
    @eval_fn
    def AF28():
        ag129_1 = Input_RPS.AG129()
        ag97_1 = Input_RPS.AG97()
        var_1 = sub(ag129_1, ag97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AG28():
    # 'Dashboard_M8_Alt'!AG28
    value = 0
    formula = "=('Input RPS'!AH129-'Input RPS'!AH97)/1000"
    @eval_fn
    def AG28():
        ah129_1 = Input_RPS.AH129()
        ah97_1 = Input_RPS.AH97()
        var_1 = sub(ah129_1, ah97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AH28():
    # 'Dashboard_M8_Alt'!AH28
    value = 0
    formula = "=('Input RPS'!AI129-'Input RPS'!AI97)/1000"
    @eval_fn
    def AH28():
        ai129_1 = Input_RPS.AI129()
        ai97_1 = Input_RPS.AI97()
        var_1 = sub(ai129_1, ai97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AI28():
    # 'Dashboard_M8_Alt'!AI28
    value = 0
    formula = "=('Input RPS'!AJ129-'Input RPS'!AJ97)/1000"
    @eval_fn
    def AI28():
        aj129_1 = Input_RPS.AJ129()
        aj97_1 = Input_RPS.AJ97()
        var_1 = sub(aj129_1, aj97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ28():
    # 'Dashboard_M8_Alt'!AJ28
    value = 0
    formula = "=('Input RPS'!AK129-'Input RPS'!AK97)/1000"
    @eval_fn
    def AJ28():
        ak129_1 = Input_RPS.AK129()
        ak97_1 = Input_RPS.AK97()
        var_1 = sub(ak129_1, ak97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AK28():
    # 'Dashboard_M8_Alt'!AK28
    value = 0
    formula = "=('Input RPS'!AL129-'Input RPS'!AL97)/1000"
    @eval_fn
    def AK28():
        al129_1 = Input_RPS.AL129()
        al97_1 = Input_RPS.AL97()
        var_1 = sub(al129_1, al97_1)
        var_2 = divide(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class B29():
    # 'Dashboard_M8_Alt'!B29
    value = "  Displacement Tech: Photovoltaic Systems"

@register(Dashboard_M8_Alt)
class C29():
    # 'Dashboard_M8_Alt'!C29
    value = "Million kWh"

@register(Dashboard_M8_Alt)
class D29():
    # 'Dashboard_M8_Alt'!D29
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://dms.puc.hawaii.gov/dms/OpenDocServlet?RT=&document_id=91+3+ICM4+LSDB15+PC_DocketReport59+26+A1001001A12D04B24000E5143818+A12D04B24000E514381+14+1960'''

@register(Dashboard_M8_Alt)
class G29():
    # 'Dashboard_M8_Alt'!G29
    value = 0
    formula = "=('Input RPS'!H118+'Input RPS'!H112+'Input RPS'!H106+'Input RPS'!H100)/1000"
    @eval_fn
    def G29():
        h118_1 = Input_RPS.H118()
        h112_1 = Input_RPS.H112()
        var_1 = add(h118_1, h112_1)
        h106_1 = Input_RPS.H106()
        var_2 = add(var_1, h106_1)
        h100_1 = Input_RPS.H100()
        var_3 = add(var_2, h100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class H29():
    # 'Dashboard_M8_Alt'!H29
    value = 0
    formula = "=('Input RPS'!I118+'Input RPS'!I112+'Input RPS'!I106+'Input RPS'!I100)/1000"
    @eval_fn
    def H29():
        i118_1 = Input_RPS.I118()
        i112_1 = Input_RPS.I112()
        var_1 = add(i118_1, i112_1)
        i106_1 = Input_RPS.I106()
        var_2 = add(var_1, i106_1)
        i100_1 = Input_RPS.I100()
        var_3 = add(var_2, i100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class I29():
    # 'Dashboard_M8_Alt'!I29
    value = 0
    formula = "=('Input RPS'!J118+'Input RPS'!J112+'Input RPS'!J106+'Input RPS'!J100)/1000"
    @eval_fn
    def I29():
        j118_1 = Input_RPS.J118()
        j112_1 = Input_RPS.J112()
        var_1 = add(j118_1, j112_1)
        j106_1 = Input_RPS.J106()
        var_2 = add(var_1, j106_1)
        j100_1 = Input_RPS.J100()
        var_3 = add(var_2, j100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class J29():
    # 'Dashboard_M8_Alt'!J29
    value = 0
    formula = "=('Input RPS'!K118+'Input RPS'!K112+'Input RPS'!K106+'Input RPS'!K100)/1000"
    @eval_fn
    def J29():
        k118_1 = Input_RPS.K118()
        k112_1 = Input_RPS.K112()
        var_1 = add(k118_1, k112_1)
        k106_1 = Input_RPS.K106()
        var_2 = add(var_1, k106_1)
        k100_1 = Input_RPS.K100()
        var_3 = add(var_2, k100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class K29():
    # 'Dashboard_M8_Alt'!K29
    value = 0
    formula = "=('Input RPS'!L118+'Input RPS'!L112+'Input RPS'!L106+'Input RPS'!L100)/1000"
    @eval_fn
    def K29():
        l118_1 = Input_RPS.L118()
        l112_1 = Input_RPS.L112()
        var_1 = add(l118_1, l112_1)
        l106_1 = Input_RPS.L106()
        var_2 = add(var_1, l106_1)
        l100_1 = Input_RPS.L100()
        var_3 = add(var_2, l100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class L29():
    # 'Dashboard_M8_Alt'!L29
    value = 0
    formula = "=('Input RPS'!M118+'Input RPS'!M112+'Input RPS'!M106+'Input RPS'!M100)/1000"
    @eval_fn
    def L29():
        m118_1 = Input_RPS.M118()
        m112_1 = Input_RPS.M112()
        var_1 = add(m118_1, m112_1)
        m106_1 = Input_RPS.M106()
        var_2 = add(var_1, m106_1)
        m100_1 = Input_RPS.M100()
        var_3 = add(var_2, m100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class M29():
    # 'Dashboard_M8_Alt'!M29
    value = 0
    formula = "=('Input RPS'!N118+'Input RPS'!N112+'Input RPS'!N106+'Input RPS'!N100)/1000"
    @eval_fn
    def M29():
        n118_1 = Input_RPS.N118()
        n112_1 = Input_RPS.N112()
        var_1 = add(n118_1, n112_1)
        n106_1 = Input_RPS.N106()
        var_2 = add(var_1, n106_1)
        n100_1 = Input_RPS.N100()
        var_3 = add(var_2, n100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class N29():
    # 'Dashboard_M8_Alt'!N29
    value = 0
    formula = "=('Input RPS'!O118+'Input RPS'!O112+'Input RPS'!O106+'Input RPS'!O100)/1000"
    @eval_fn
    def N29():
        o118_1 = Input_RPS.O118()
        o112_1 = Input_RPS.O112()
        var_1 = add(o118_1, o112_1)
        o106_1 = Input_RPS.O106()
        var_2 = add(var_1, o106_1)
        o100_1 = Input_RPS.O100()
        var_3 = add(var_2, o100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class O29():
    # 'Dashboard_M8_Alt'!O29
    value = 0
    formula = "=('Input RPS'!P118+'Input RPS'!P112+'Input RPS'!P106+'Input RPS'!P100)/1000"
    @eval_fn
    def O29():
        p118_1 = Input_RPS.P118()
        p112_1 = Input_RPS.P112()
        var_1 = add(p118_1, p112_1)
        p106_1 = Input_RPS.P106()
        var_2 = add(var_1, p106_1)
        p100_1 = Input_RPS.P100()
        var_3 = add(var_2, p100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class P29():
    # 'Dashboard_M8_Alt'!P29
    value = 0
    formula = "=('Input RPS'!Q118+'Input RPS'!Q112+'Input RPS'!Q106+'Input RPS'!Q100)/1000"
    @eval_fn
    def P29():
        q118_1 = Input_RPS.Q118()
        q112_1 = Input_RPS.Q112()
        var_1 = add(q118_1, q112_1)
        q106_1 = Input_RPS.Q106()
        var_2 = add(var_1, q106_1)
        q100_1 = Input_RPS.Q100()
        var_3 = add(var_2, q100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class Q29():
    # 'Dashboard_M8_Alt'!Q29
    value = 0
    formula = "=('Input RPS'!R118+'Input RPS'!R112+'Input RPS'!R106+'Input RPS'!R100)/1000"
    @eval_fn
    def Q29():
        r118_1 = Input_RPS.R118()
        r112_1 = Input_RPS.R112()
        var_1 = add(r118_1, r112_1)
        r106_1 = Input_RPS.R106()
        var_2 = add(var_1, r106_1)
        r100_1 = Input_RPS.R100()
        var_3 = add(var_2, r100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class R29():
    # 'Dashboard_M8_Alt'!R29
    value = 0
    formula = "=('Input RPS'!S118+'Input RPS'!S112+'Input RPS'!S106+'Input RPS'!S100)/1000"
    @eval_fn
    def R29():
        s118_1 = Input_RPS.S118()
        s112_1 = Input_RPS.S112()
        var_1 = add(s118_1, s112_1)
        s106_1 = Input_RPS.S106()
        var_2 = add(var_1, s106_1)
        s100_1 = Input_RPS.S100()
        var_3 = add(var_2, s100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class S29():
    # 'Dashboard_M8_Alt'!S29
    value = 0
    formula = "=('Input RPS'!T118+'Input RPS'!T112+'Input RPS'!T106+'Input RPS'!T100)/1000"
    @eval_fn
    def S29():
        t118_1 = Input_RPS.T118()
        t112_1 = Input_RPS.T112()
        var_1 = add(t118_1, t112_1)
        t106_1 = Input_RPS.T106()
        var_2 = add(var_1, t106_1)
        t100_1 = Input_RPS.T100()
        var_3 = add(var_2, t100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class T29():
    # 'Dashboard_M8_Alt'!T29
    value = 0
    formula = "=('Input RPS'!U118+'Input RPS'!U112+'Input RPS'!U106+'Input RPS'!U100)/1000"
    @eval_fn
    def T29():
        u118_1 = Input_RPS.U118()
        u112_1 = Input_RPS.U112()
        var_1 = add(u118_1, u112_1)
        u106_1 = Input_RPS.U106()
        var_2 = add(var_1, u106_1)
        u100_1 = Input_RPS.U100()
        var_3 = add(var_2, u100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class U29():
    # 'Dashboard_M8_Alt'!U29
    value = 0
    formula = "=('Input RPS'!V118+'Input RPS'!V112+'Input RPS'!V106+'Input RPS'!V100)/1000"
    @eval_fn
    def U29():
        v118_1 = Input_RPS.V118()
        v112_1 = Input_RPS.V112()
        var_1 = add(v118_1, v112_1)
        v106_1 = Input_RPS.V106()
        var_2 = add(var_1, v106_1)
        v100_1 = Input_RPS.V100()
        var_3 = add(var_2, v100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class V29():
    # 'Dashboard_M8_Alt'!V29
    value = 0
    formula = "=('Input RPS'!W118+'Input RPS'!W112+'Input RPS'!W106+'Input RPS'!W100)/1000"
    @eval_fn
    def V29():
        w118_1 = Input_RPS.W118()
        w112_1 = Input_RPS.W112()
        var_1 = add(w118_1, w112_1)
        w106_1 = Input_RPS.W106()
        var_2 = add(var_1, w106_1)
        w100_1 = Input_RPS.W100()
        var_3 = add(var_2, w100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class W29():
    # 'Dashboard_M8_Alt'!W29
    value = 0
    formula = "=('Input RPS'!X118+'Input RPS'!X112+'Input RPS'!X106+'Input RPS'!X100)/1000"
    @eval_fn
    def W29():
        x118_1 = Input_RPS.X118()
        x112_1 = Input_RPS.X112()
        var_1 = add(x118_1, x112_1)
        x106_1 = Input_RPS.X106()
        var_2 = add(var_1, x106_1)
        x100_1 = Input_RPS.X100()
        var_3 = add(var_2, x100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class X29():
    # 'Dashboard_M8_Alt'!X29
    value = 0
    formula = "=('Input RPS'!Y118+'Input RPS'!Y112+'Input RPS'!Y106+'Input RPS'!Y100)/1000"
    @eval_fn
    def X29():
        y118_1 = Input_RPS.Y118()
        y112_1 = Input_RPS.Y112()
        var_1 = add(y118_1, y112_1)
        y106_1 = Input_RPS.Y106()
        var_2 = add(var_1, y106_1)
        y100_1 = Input_RPS.Y100()
        var_3 = add(var_2, y100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class Y29():
    # 'Dashboard_M8_Alt'!Y29
    value = 0
    formula = "=('Input RPS'!Z118+'Input RPS'!Z112+'Input RPS'!Z106+'Input RPS'!Z100)/1000"
    @eval_fn
    def Y29():
        z118_1 = Input_RPS.Z118()
        z112_1 = Input_RPS.Z112()
        var_1 = add(z118_1, z112_1)
        z106_1 = Input_RPS.Z106()
        var_2 = add(var_1, z106_1)
        z100_1 = Input_RPS.Z100()
        var_3 = add(var_2, z100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class Z29():
    # 'Dashboard_M8_Alt'!Z29
    value = 0
    formula = "=('Input RPS'!AA118+'Input RPS'!AA112+'Input RPS'!AA106+'Input RPS'!AA100)/1000"
    @eval_fn
    def Z29():
        aa118_1 = Input_RPS.AA118()
        aa112_1 = Input_RPS.AA112()
        var_1 = add(aa118_1, aa112_1)
        aa106_1 = Input_RPS.AA106()
        var_2 = add(var_1, aa106_1)
        aa100_1 = Input_RPS.AA100()
        var_3 = add(var_2, aa100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AA29():
    # 'Dashboard_M8_Alt'!AA29
    value = 0
    formula = "=('Input RPS'!AB118+'Input RPS'!AB112+'Input RPS'!AB106+'Input RPS'!AB100)/1000"
    @eval_fn
    def AA29():
        ab118_1 = Input_RPS.AB118()
        ab112_1 = Input_RPS.AB112()
        var_1 = add(ab118_1, ab112_1)
        ab106_1 = Input_RPS.AB106()
        var_2 = add(var_1, ab106_1)
        ab100_1 = Input_RPS.AB100()
        var_3 = add(var_2, ab100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AB29():
    # 'Dashboard_M8_Alt'!AB29
    value = 0
    formula = "=('Input RPS'!AC118+'Input RPS'!AC112+'Input RPS'!AC106+'Input RPS'!AC100)/1000"
    @eval_fn
    def AB29():
        ac118_1 = Input_RPS.AC118()
        ac112_1 = Input_RPS.AC112()
        var_1 = add(ac118_1, ac112_1)
        ac106_1 = Input_RPS.AC106()
        var_2 = add(var_1, ac106_1)
        ac100_1 = Input_RPS.AC100()
        var_3 = add(var_2, ac100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AC29():
    # 'Dashboard_M8_Alt'!AC29
    value = 0
    formula = "=('Input RPS'!AD118+'Input RPS'!AD112+'Input RPS'!AD106+'Input RPS'!AD100)/1000"
    @eval_fn
    def AC29():
        ad118_1 = Input_RPS.AD118()
        ad112_1 = Input_RPS.AD112()
        var_1 = add(ad118_1, ad112_1)
        ad106_1 = Input_RPS.AD106()
        var_2 = add(var_1, ad106_1)
        ad100_1 = Input_RPS.AD100()
        var_3 = add(var_2, ad100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AD29():
    # 'Dashboard_M8_Alt'!AD29
    value = 0
    formula = "=('Input RPS'!AE118+'Input RPS'!AE112+'Input RPS'!AE106+'Input RPS'!AE100)/1000"
    @eval_fn
    def AD29():
        ae118_1 = Input_RPS.AE118()
        ae112_1 = Input_RPS.AE112()
        var_1 = add(ae118_1, ae112_1)
        ae106_1 = Input_RPS.AE106()
        var_2 = add(var_1, ae106_1)
        ae100_1 = Input_RPS.AE100()
        var_3 = add(var_2, ae100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AE29():
    # 'Dashboard_M8_Alt'!AE29
    value = 0
    formula = "=('Input RPS'!AF118+'Input RPS'!AF112+'Input RPS'!AF106+'Input RPS'!AF100)/1000"
    @eval_fn
    def AE29():
        af118_1 = Input_RPS.AF118()
        af112_1 = Input_RPS.AF112()
        var_1 = add(af118_1, af112_1)
        af106_1 = Input_RPS.AF106()
        var_2 = add(var_1, af106_1)
        af100_1 = Input_RPS.AF100()
        var_3 = add(var_2, af100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AF29():
    # 'Dashboard_M8_Alt'!AF29
    value = 0
    formula = "=('Input RPS'!AG118+'Input RPS'!AG112+'Input RPS'!AG106+'Input RPS'!AG100)/1000"
    @eval_fn
    def AF29():
        ag118_1 = Input_RPS.AG118()
        ag112_1 = Input_RPS.AG112()
        var_1 = add(ag118_1, ag112_1)
        ag106_1 = Input_RPS.AG106()
        var_2 = add(var_1, ag106_1)
        ag100_1 = Input_RPS.AG100()
        var_3 = add(var_2, ag100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AG29():
    # 'Dashboard_M8_Alt'!AG29
    value = 0
    formula = "=('Input RPS'!AH118+'Input RPS'!AH112+'Input RPS'!AH106+'Input RPS'!AH100)/1000"
    @eval_fn
    def AG29():
        ah118_1 = Input_RPS.AH118()
        ah112_1 = Input_RPS.AH112()
        var_1 = add(ah118_1, ah112_1)
        ah106_1 = Input_RPS.AH106()
        var_2 = add(var_1, ah106_1)
        ah100_1 = Input_RPS.AH100()
        var_3 = add(var_2, ah100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AH29():
    # 'Dashboard_M8_Alt'!AH29
    value = 0
    formula = "=('Input RPS'!AI118+'Input RPS'!AI112+'Input RPS'!AI106+'Input RPS'!AI100)/1000"
    @eval_fn
    def AH29():
        ai118_1 = Input_RPS.AI118()
        ai112_1 = Input_RPS.AI112()
        var_1 = add(ai118_1, ai112_1)
        ai106_1 = Input_RPS.AI106()
        var_2 = add(var_1, ai106_1)
        ai100_1 = Input_RPS.AI100()
        var_3 = add(var_2, ai100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AI29():
    # 'Dashboard_M8_Alt'!AI29
    value = 0
    formula = "=('Input RPS'!AJ118+'Input RPS'!AJ112+'Input RPS'!AJ106+'Input RPS'!AJ100)/1000"
    @eval_fn
    def AI29():
        aj118_1 = Input_RPS.AJ118()
        aj112_1 = Input_RPS.AJ112()
        var_1 = add(aj118_1, aj112_1)
        aj106_1 = Input_RPS.AJ106()
        var_2 = add(var_1, aj106_1)
        aj100_1 = Input_RPS.AJ100()
        var_3 = add(var_2, aj100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AJ29():
    # 'Dashboard_M8_Alt'!AJ29
    value = 0
    formula = "=('Input RPS'!AK118+'Input RPS'!AK112+'Input RPS'!AK106+'Input RPS'!AK100)/1000"
    @eval_fn
    def AJ29():
        ak118_1 = Input_RPS.AK118()
        ak112_1 = Input_RPS.AK112()
        var_1 = add(ak118_1, ak112_1)
        ak106_1 = Input_RPS.AK106()
        var_2 = add(var_1, ak106_1)
        ak100_1 = Input_RPS.AK100()
        var_3 = add(var_2, ak100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AK29():
    # 'Dashboard_M8_Alt'!AK29
    value = 0
    formula = "=('Input RPS'!AL118+'Input RPS'!AL112+'Input RPS'!AL106+'Input RPS'!AL100)/1000"
    @eval_fn
    def AK29():
        al118_1 = Input_RPS.AL118()
        al112_1 = Input_RPS.AL112()
        var_1 = add(al118_1, al112_1)
        al106_1 = Input_RPS.AL106()
        var_2 = add(var_1, al106_1)
        al100_1 = Input_RPS.AL100()
        var_3 = add(var_2, al100_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class B30():
    # 'Dashboard_M8_Alt'!B30
    value = "  Displacement Tech: Solar Water Heating"

@register(Dashboard_M8_Alt)
class C30():
    # 'Dashboard_M8_Alt'!C30
    value = "Million kWh"

@register(Dashboard_M8_Alt)
class D30():
    # 'Dashboard_M8_Alt'!D30
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://dms.puc.hawaii.gov/dms/OpenDocServlet?RT=&document_id=91+3+ICM4+LSDB15+PC_DocketReport59+26+A1001001A12D04B24000E5143818+A12D04B24000E514381+14+1960'''

@register(Dashboard_M8_Alt)
class G30():
    # 'Dashboard_M8_Alt'!G30
    value = 0
    formula = "=('Input RPS'!H119+'Input RPS'!H114+'Input RPS'!H108+'Input RPS'!H102)/1000"
    @eval_fn
    def G30():
        h119_1 = Input_RPS.H119()
        h114_1 = Input_RPS.H114()
        var_1 = add(h119_1, h114_1)
        h108_1 = Input_RPS.H108()
        var_2 = add(var_1, h108_1)
        h102_1 = Input_RPS.H102()
        var_3 = add(var_2, h102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class H30():
    # 'Dashboard_M8_Alt'!H30
    value = 0
    formula = "=('Input RPS'!I119+'Input RPS'!I114+'Input RPS'!I108+'Input RPS'!I102)/1000"
    @eval_fn
    def H30():
        i119_1 = Input_RPS.I119()
        i114_1 = Input_RPS.I114()
        var_1 = add(i119_1, i114_1)
        i108_1 = Input_RPS.I108()
        var_2 = add(var_1, i108_1)
        i102_1 = Input_RPS.I102()
        var_3 = add(var_2, i102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class I30():
    # 'Dashboard_M8_Alt'!I30
    value = 0
    formula = "=('Input RPS'!J119+'Input RPS'!J114+'Input RPS'!J108+'Input RPS'!J102)/1000"
    @eval_fn
    def I30():
        j119_1 = Input_RPS.J119()
        j114_1 = Input_RPS.J114()
        var_1 = add(j119_1, j114_1)
        j108_1 = Input_RPS.J108()
        var_2 = add(var_1, j108_1)
        j102_1 = Input_RPS.J102()
        var_3 = add(var_2, j102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class J30():
    # 'Dashboard_M8_Alt'!J30
    value = 7.387
    formula = "=('Input RPS'!K119+'Input RPS'!K114+'Input RPS'!K108+'Input RPS'!K102)/1000"
    @eval_fn
    def J30():
        k119_1 = Input_RPS.K119()
        k114_1 = Input_RPS.K114()
        var_1 = add(k119_1, k114_1)
        k108_1 = Input_RPS.K108()
        var_2 = add(var_1, k108_1)
        k102_1 = Input_RPS.K102()
        var_3 = add(var_2, k102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class K30():
    # 'Dashboard_M8_Alt'!K30
    value = 7.558
    formula = "=('Input RPS'!L119+'Input RPS'!L114+'Input RPS'!L108+'Input RPS'!L102)/1000"
    @eval_fn
    def K30():
        l119_1 = Input_RPS.L119()
        l114_1 = Input_RPS.L114()
        var_1 = add(l119_1, l114_1)
        l108_1 = Input_RPS.L108()
        var_2 = add(var_1, l108_1)
        l102_1 = Input_RPS.L102()
        var_3 = add(var_2, l102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class L30():
    # 'Dashboard_M8_Alt'!L30
    value = 7.659
    formula = "=('Input RPS'!M119+'Input RPS'!M114+'Input RPS'!M108+'Input RPS'!M102)/1000"
    @eval_fn
    def L30():
        m119_1 = Input_RPS.M119()
        m114_1 = Input_RPS.M114()
        var_1 = add(m119_1, m114_1)
        m108_1 = Input_RPS.M108()
        var_2 = add(var_1, m108_1)
        m102_1 = Input_RPS.M102()
        var_3 = add(var_2, m102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class M30():
    # 'Dashboard_M8_Alt'!M30
    value = 7.831
    formula = "=('Input RPS'!N119+'Input RPS'!N114+'Input RPS'!N108+'Input RPS'!N102)/1000"
    @eval_fn
    def M30():
        n119_1 = Input_RPS.N119()
        n114_1 = Input_RPS.N114()
        var_1 = add(n119_1, n114_1)
        n108_1 = Input_RPS.N108()
        var_2 = add(var_1, n108_1)
        n102_1 = Input_RPS.N102()
        var_3 = add(var_2, n102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class N30():
    # 'Dashboard_M8_Alt'!N30
    value = 7.937
    formula = "=('Input RPS'!O119+'Input RPS'!O114+'Input RPS'!O108+'Input RPS'!O102)/1000"
    @eval_fn
    def N30():
        o119_1 = Input_RPS.O119()
        o114_1 = Input_RPS.O114()
        var_1 = add(o119_1, o114_1)
        o108_1 = Input_RPS.O108()
        var_2 = add(var_1, o108_1)
        o102_1 = Input_RPS.O102()
        var_3 = add(var_2, o102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class O30():
    # 'Dashboard_M8_Alt'!O30
    value = 0
    formula = "=('Input RPS'!P119+'Input RPS'!P114+'Input RPS'!P108+'Input RPS'!P102)/1000"
    @eval_fn
    def O30():
        p119_1 = Input_RPS.P119()
        p114_1 = Input_RPS.P114()
        var_1 = add(p119_1, p114_1)
        p108_1 = Input_RPS.P108()
        var_2 = add(var_1, p108_1)
        p102_1 = Input_RPS.P102()
        var_3 = add(var_2, p102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class P30():
    # 'Dashboard_M8_Alt'!P30
    value = 0
    formula = "=('Input RPS'!Q119+'Input RPS'!Q114+'Input RPS'!Q108+'Input RPS'!Q102)/1000"
    @eval_fn
    def P30():
        q119_1 = Input_RPS.Q119()
        q114_1 = Input_RPS.Q114()
        var_1 = add(q119_1, q114_1)
        q108_1 = Input_RPS.Q108()
        var_2 = add(var_1, q108_1)
        q102_1 = Input_RPS.Q102()
        var_3 = add(var_2, q102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class Q30():
    # 'Dashboard_M8_Alt'!Q30
    value = 0
    formula = "=('Input RPS'!R119+'Input RPS'!R114+'Input RPS'!R108+'Input RPS'!R102)/1000"
    @eval_fn
    def Q30():
        r119_1 = Input_RPS.R119()
        r114_1 = Input_RPS.R114()
        var_1 = add(r119_1, r114_1)
        r108_1 = Input_RPS.R108()
        var_2 = add(var_1, r108_1)
        r102_1 = Input_RPS.R102()
        var_3 = add(var_2, r102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class R30():
    # 'Dashboard_M8_Alt'!R30
    value = 0
    formula = "=('Input RPS'!S119+'Input RPS'!S114+'Input RPS'!S108+'Input RPS'!S102)/1000"
    @eval_fn
    def R30():
        s119_1 = Input_RPS.S119()
        s114_1 = Input_RPS.S114()
        var_1 = add(s119_1, s114_1)
        s108_1 = Input_RPS.S108()
        var_2 = add(var_1, s108_1)
        s102_1 = Input_RPS.S102()
        var_3 = add(var_2, s102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class S30():
    # 'Dashboard_M8_Alt'!S30
    value = 24.91
    formula = "=('Input RPS'!T119+'Input RPS'!T114+'Input RPS'!T108+'Input RPS'!T102)/1000"
    @eval_fn
    def S30():
        t119_1 = Input_RPS.T119()
        t114_1 = Input_RPS.T114()
        var_1 = add(t119_1, t114_1)
        t108_1 = Input_RPS.T108()
        var_2 = add(var_1, t108_1)
        t102_1 = Input_RPS.T102()
        var_3 = add(var_2, t102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class T30():
    # 'Dashboard_M8_Alt'!T30
    value = 29.734
    formula = "=('Input RPS'!U119+'Input RPS'!U114+'Input RPS'!U108+'Input RPS'!U102)/1000"
    @eval_fn
    def T30():
        u119_1 = Input_RPS.U119()
        u114_1 = Input_RPS.U114()
        var_1 = add(u119_1, u114_1)
        u108_1 = Input_RPS.U108()
        var_2 = add(var_1, u108_1)
        u102_1 = Input_RPS.U102()
        var_3 = add(var_2, u102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class U30():
    # 'Dashboard_M8_Alt'!U30
    value = 34.098
    formula = "=('Input RPS'!V119+'Input RPS'!V114+'Input RPS'!V108+'Input RPS'!V102)/1000"
    @eval_fn
    def U30():
        v119_1 = Input_RPS.V119()
        v114_1 = Input_RPS.V114()
        var_1 = add(v119_1, v114_1)
        v108_1 = Input_RPS.V108()
        var_2 = add(var_1, v108_1)
        v102_1 = Input_RPS.V102()
        var_3 = add(var_2, v102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class V30():
    # 'Dashboard_M8_Alt'!V30
    value = 38.462
    formula = "=('Input RPS'!W119+'Input RPS'!W114+'Input RPS'!W108+'Input RPS'!W102)/1000"
    @eval_fn
    def V30():
        w119_1 = Input_RPS.W119()
        w114_1 = Input_RPS.W114()
        var_1 = add(w119_1, w114_1)
        w108_1 = Input_RPS.W108()
        var_2 = add(var_1, w108_1)
        w102_1 = Input_RPS.W102()
        var_3 = add(var_2, w102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class W30():
    # 'Dashboard_M8_Alt'!W30
    value = 0
    formula = "=('Input RPS'!X119+'Input RPS'!X114+'Input RPS'!X108+'Input RPS'!X102)/1000"
    @eval_fn
    def W30():
        x119_1 = Input_RPS.X119()
        x114_1 = Input_RPS.X114()
        var_1 = add(x119_1, x114_1)
        x108_1 = Input_RPS.X108()
        var_2 = add(var_1, x108_1)
        x102_1 = Input_RPS.X102()
        var_3 = add(var_2, x102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class X30():
    # 'Dashboard_M8_Alt'!X30
    value = 0
    formula = "=('Input RPS'!Y119+'Input RPS'!Y114+'Input RPS'!Y108+'Input RPS'!Y102)/1000"
    @eval_fn
    def X30():
        y119_1 = Input_RPS.Y119()
        y114_1 = Input_RPS.Y114()
        var_1 = add(y119_1, y114_1)
        y108_1 = Input_RPS.Y108()
        var_2 = add(var_1, y108_1)
        y102_1 = Input_RPS.Y102()
        var_3 = add(var_2, y102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class Y30():
    # 'Dashboard_M8_Alt'!Y30
    value = 0
    formula = "=('Input RPS'!Z119+'Input RPS'!Z114+'Input RPS'!Z108+'Input RPS'!Z102)/1000"
    @eval_fn
    def Y30():
        z119_1 = Input_RPS.Z119()
        z114_1 = Input_RPS.Z114()
        var_1 = add(z119_1, z114_1)
        z108_1 = Input_RPS.Z108()
        var_2 = add(var_1, z108_1)
        z102_1 = Input_RPS.Z102()
        var_3 = add(var_2, z102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class Z30():
    # 'Dashboard_M8_Alt'!Z30
    value = 0
    formula = "=('Input RPS'!AA119+'Input RPS'!AA114+'Input RPS'!AA108+'Input RPS'!AA102)/1000"
    @eval_fn
    def Z30():
        aa119_1 = Input_RPS.AA119()
        aa114_1 = Input_RPS.AA114()
        var_1 = add(aa119_1, aa114_1)
        aa108_1 = Input_RPS.AA108()
        var_2 = add(var_1, aa108_1)
        aa102_1 = Input_RPS.AA102()
        var_3 = add(var_2, aa102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AA30():
    # 'Dashboard_M8_Alt'!AA30
    value = 0
    formula = "=('Input RPS'!AB119+'Input RPS'!AB114+'Input RPS'!AB108+'Input RPS'!AB102)/1000"
    @eval_fn
    def AA30():
        ab119_1 = Input_RPS.AB119()
        ab114_1 = Input_RPS.AB114()
        var_1 = add(ab119_1, ab114_1)
        ab108_1 = Input_RPS.AB108()
        var_2 = add(var_1, ab108_1)
        ab102_1 = Input_RPS.AB102()
        var_3 = add(var_2, ab102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AB30():
    # 'Dashboard_M8_Alt'!AB30
    value = 0
    formula = "=('Input RPS'!AC119+'Input RPS'!AC114+'Input RPS'!AC108+'Input RPS'!AC102)/1000"
    @eval_fn
    def AB30():
        ac119_1 = Input_RPS.AC119()
        ac114_1 = Input_RPS.AC114()
        var_1 = add(ac119_1, ac114_1)
        ac108_1 = Input_RPS.AC108()
        var_2 = add(var_1, ac108_1)
        ac102_1 = Input_RPS.AC102()
        var_3 = add(var_2, ac102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AC30():
    # 'Dashboard_M8_Alt'!AC30
    value = 0
    formula = "=('Input RPS'!AD119+'Input RPS'!AD114+'Input RPS'!AD108+'Input RPS'!AD102)/1000"
    @eval_fn
    def AC30():
        ad119_1 = Input_RPS.AD119()
        ad114_1 = Input_RPS.AD114()
        var_1 = add(ad119_1, ad114_1)
        ad108_1 = Input_RPS.AD108()
        var_2 = add(var_1, ad108_1)
        ad102_1 = Input_RPS.AD102()
        var_3 = add(var_2, ad102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AD30():
    # 'Dashboard_M8_Alt'!AD30
    value = 0
    formula = "=('Input RPS'!AE119+'Input RPS'!AE114+'Input RPS'!AE108+'Input RPS'!AE102)/1000"
    @eval_fn
    def AD30():
        ae119_1 = Input_RPS.AE119()
        ae114_1 = Input_RPS.AE114()
        var_1 = add(ae119_1, ae114_1)
        ae108_1 = Input_RPS.AE108()
        var_2 = add(var_1, ae108_1)
        ae102_1 = Input_RPS.AE102()
        var_3 = add(var_2, ae102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AE30():
    # 'Dashboard_M8_Alt'!AE30
    value = 0
    formula = "=('Input RPS'!AF119+'Input RPS'!AF114+'Input RPS'!AF108+'Input RPS'!AF102)/1000"
    @eval_fn
    def AE30():
        af119_1 = Input_RPS.AF119()
        af114_1 = Input_RPS.AF114()
        var_1 = add(af119_1, af114_1)
        af108_1 = Input_RPS.AF108()
        var_2 = add(var_1, af108_1)
        af102_1 = Input_RPS.AF102()
        var_3 = add(var_2, af102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AF30():
    # 'Dashboard_M8_Alt'!AF30
    value = 0
    formula = "=('Input RPS'!AG119+'Input RPS'!AG114+'Input RPS'!AG108+'Input RPS'!AG102)/1000"
    @eval_fn
    def AF30():
        ag119_1 = Input_RPS.AG119()
        ag114_1 = Input_RPS.AG114()
        var_1 = add(ag119_1, ag114_1)
        ag108_1 = Input_RPS.AG108()
        var_2 = add(var_1, ag108_1)
        ag102_1 = Input_RPS.AG102()
        var_3 = add(var_2, ag102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AG30():
    # 'Dashboard_M8_Alt'!AG30
    value = 0
    formula = "=('Input RPS'!AH119+'Input RPS'!AH114+'Input RPS'!AH108+'Input RPS'!AH102)/1000"
    @eval_fn
    def AG30():
        ah119_1 = Input_RPS.AH119()
        ah114_1 = Input_RPS.AH114()
        var_1 = add(ah119_1, ah114_1)
        ah108_1 = Input_RPS.AH108()
        var_2 = add(var_1, ah108_1)
        ah102_1 = Input_RPS.AH102()
        var_3 = add(var_2, ah102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AH30():
    # 'Dashboard_M8_Alt'!AH30
    value = 0
    formula = "=('Input RPS'!AI119+'Input RPS'!AI114+'Input RPS'!AI108+'Input RPS'!AI102)/1000"
    @eval_fn
    def AH30():
        ai119_1 = Input_RPS.AI119()
        ai114_1 = Input_RPS.AI114()
        var_1 = add(ai119_1, ai114_1)
        ai108_1 = Input_RPS.AI108()
        var_2 = add(var_1, ai108_1)
        ai102_1 = Input_RPS.AI102()
        var_3 = add(var_2, ai102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AI30():
    # 'Dashboard_M8_Alt'!AI30
    value = 0
    formula = "=('Input RPS'!AJ119+'Input RPS'!AJ114+'Input RPS'!AJ108+'Input RPS'!AJ102)/1000"
    @eval_fn
    def AI30():
        aj119_1 = Input_RPS.AJ119()
        aj114_1 = Input_RPS.AJ114()
        var_1 = add(aj119_1, aj114_1)
        aj108_1 = Input_RPS.AJ108()
        var_2 = add(var_1, aj108_1)
        aj102_1 = Input_RPS.AJ102()
        var_3 = add(var_2, aj102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AJ30():
    # 'Dashboard_M8_Alt'!AJ30
    value = 0
    formula = "=('Input RPS'!AK119+'Input RPS'!AK114+'Input RPS'!AK108+'Input RPS'!AK102)/1000"
    @eval_fn
    def AJ30():
        ak119_1 = Input_RPS.AK119()
        ak114_1 = Input_RPS.AK114()
        var_1 = add(ak119_1, ak114_1)
        ak108_1 = Input_RPS.AK108()
        var_2 = add(var_1, ak108_1)
        ak102_1 = Input_RPS.AK102()
        var_3 = add(var_2, ak102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AK30():
    # 'Dashboard_M8_Alt'!AK30
    value = 0
    formula = "=('Input RPS'!AL119+'Input RPS'!AL114+'Input RPS'!AL108+'Input RPS'!AL102)/1000"
    @eval_fn
    def AK30():
        al119_1 = Input_RPS.AL119()
        al114_1 = Input_RPS.AL114()
        var_1 = add(al119_1, al114_1)
        al108_1 = Input_RPS.AL108()
        var_2 = add(var_1, al108_1)
        al102_1 = Input_RPS.AL102()
        var_3 = add(var_2, al102_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class B31():
    # 'Dashboard_M8_Alt'!B31
    value = "  Energy Efficiency Technologies"

@register(Dashboard_M8_Alt)
class C31():
    # 'Dashboard_M8_Alt'!C31
    value = "Million kWh"

@register(Dashboard_M8_Alt)
class D31():
    # 'Dashboard_M8_Alt'!D31
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://dms.puc.hawaii.gov/dms/OpenDocServlet?RT=&document_id=91+3+ICM4+LSDB15+PC_DocketReport59+26+A1001001A12D04B24000E5143818+A12D04B24000E514381+14+1960'''

@register(Dashboard_M8_Alt)
class G31():
    # 'Dashboard_M8_Alt'!G31
    value = 0
    formula = "=('Input RPS'!H120+'Input RPS'!H115+'Input RPS'!H109+'Input RPS'!H103)/1000"
    @eval_fn
    def G31():
        h120_1 = Input_RPS.H120()
        h115_1 = Input_RPS.H115()
        var_1 = add(h120_1, h115_1)
        h109_1 = Input_RPS.H109()
        var_2 = add(var_1, h109_1)
        h103_1 = Input_RPS.H103()
        var_3 = add(var_2, h103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class H31():
    # 'Dashboard_M8_Alt'!H31
    value = 0
    formula = "=('Input RPS'!I120+'Input RPS'!I115+'Input RPS'!I109+'Input RPS'!I103)/1000"
    @eval_fn
    def H31():
        i120_1 = Input_RPS.I120()
        i115_1 = Input_RPS.I115()
        var_1 = add(i120_1, i115_1)
        i109_1 = Input_RPS.I109()
        var_2 = add(var_1, i109_1)
        i103_1 = Input_RPS.I103()
        var_3 = add(var_2, i103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class I31():
    # 'Dashboard_M8_Alt'!I31
    value = 0
    formula = "=('Input RPS'!J120+'Input RPS'!J115+'Input RPS'!J109+'Input RPS'!J103)/1000"
    @eval_fn
    def I31():
        j120_1 = Input_RPS.J120()
        j115_1 = Input_RPS.J115()
        var_1 = add(j120_1, j115_1)
        j109_1 = Input_RPS.J109()
        var_2 = add(var_1, j109_1)
        j103_1 = Input_RPS.J103()
        var_3 = add(var_2, j103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class J31():
    # 'Dashboard_M8_Alt'!J31
    value = 0
    formula = "=('Input RPS'!K120+'Input RPS'!K115+'Input RPS'!K109+'Input RPS'!K103)/1000"
    @eval_fn
    def J31():
        k120_1 = Input_RPS.K120()
        k115_1 = Input_RPS.K115()
        var_1 = add(k120_1, k115_1)
        k109_1 = Input_RPS.K109()
        var_2 = add(var_1, k109_1)
        k103_1 = Input_RPS.K103()
        var_3 = add(var_2, k103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class K31():
    # 'Dashboard_M8_Alt'!K31
    value = 0
    formula = "=('Input RPS'!L120+'Input RPS'!L115+'Input RPS'!L109+'Input RPS'!L103)/1000"
    @eval_fn
    def K31():
        l120_1 = Input_RPS.L120()
        l115_1 = Input_RPS.L115()
        var_1 = add(l120_1, l115_1)
        l109_1 = Input_RPS.L109()
        var_2 = add(var_1, l109_1)
        l103_1 = Input_RPS.L103()
        var_3 = add(var_2, l103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class L31():
    # 'Dashboard_M8_Alt'!L31
    value = 418
    formula = "=('Input RPS'!M120+'Input RPS'!M115+'Input RPS'!M109+'Input RPS'!M103)/1000"
    @eval_fn
    def L31():
        m120_1 = Input_RPS.M120()
        m115_1 = Input_RPS.M115()
        var_1 = add(m120_1, m115_1)
        m109_1 = Input_RPS.M109()
        var_2 = add(var_1, m109_1)
        m103_1 = Input_RPS.M103()
        var_3 = add(var_2, m103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class M31():
    # 'Dashboard_M8_Alt'!M31
    value = 476
    formula = "=('Input RPS'!N120+'Input RPS'!N115+'Input RPS'!N109+'Input RPS'!N103)/1000"
    @eval_fn
    def M31():
        n120_1 = Input_RPS.N120()
        n115_1 = Input_RPS.N115()
        var_1 = add(n120_1, n115_1)
        n109_1 = Input_RPS.N109()
        var_2 = add(var_1, n109_1)
        n103_1 = Input_RPS.N103()
        var_3 = add(var_2, n103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class N31():
    # 'Dashboard_M8_Alt'!N31
    value = 598
    formula = "=('Input RPS'!O120+'Input RPS'!O115+'Input RPS'!O109+'Input RPS'!O103)/1000"
    @eval_fn
    def N31():
        o120_1 = Input_RPS.O120()
        o115_1 = Input_RPS.O115()
        var_1 = add(o120_1, o115_1)
        o109_1 = Input_RPS.O109()
        var_2 = add(var_1, o109_1)
        o103_1 = Input_RPS.O103()
        var_3 = add(var_2, o103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class O31():
    # 'Dashboard_M8_Alt'!O31
    value = 730.893
    formula = "=('Input RPS'!P120+'Input RPS'!P115+'Input RPS'!P109+'Input RPS'!P103)/1000"
    @eval_fn
    def O31():
        p120_1 = Input_RPS.P120()
        p115_1 = Input_RPS.P115()
        var_1 = add(p120_1, p115_1)
        p109_1 = Input_RPS.P109()
        var_2 = add(var_1, p109_1)
        p103_1 = Input_RPS.P103()
        var_3 = add(var_2, p103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class P31():
    # 'Dashboard_M8_Alt'!P31
    value = 789.631
    formula = "=('Input RPS'!Q120+'Input RPS'!Q115+'Input RPS'!Q109+'Input RPS'!Q103)/1000"
    @eval_fn
    def P31():
        q120_1 = Input_RPS.Q120()
        q115_1 = Input_RPS.Q115()
        var_1 = add(q120_1, q115_1)
        q109_1 = Input_RPS.Q109()
        var_2 = add(var_1, q109_1)
        q103_1 = Input_RPS.Q103()
        var_3 = add(var_2, q103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class Q31():
    # 'Dashboard_M8_Alt'!Q31
    value = 899.509
    formula = "=('Input RPS'!R120+'Input RPS'!R115+'Input RPS'!R109+'Input RPS'!R103)/1000"
    @eval_fn
    def Q31():
        r120_1 = Input_RPS.R120()
        r115_1 = Input_RPS.R115()
        var_1 = add(r120_1, r115_1)
        r109_1 = Input_RPS.R109()
        var_2 = add(var_1, r109_1)
        r103_1 = Input_RPS.R103()
        var_3 = add(var_2, r103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class R31():
    # 'Dashboard_M8_Alt'!R31
    value = 1009.064
    formula = "=('Input RPS'!S120+'Input RPS'!S115+'Input RPS'!S109+'Input RPS'!S103)/1000"
    @eval_fn
    def R31():
        s120_1 = Input_RPS.S120()
        s115_1 = Input_RPS.S115()
        var_1 = add(s120_1, s115_1)
        s109_1 = Input_RPS.S109()
        var_2 = add(var_1, s109_1)
        s103_1 = Input_RPS.S103()
        var_3 = add(var_2, s103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class S31():
    # 'Dashboard_M8_Alt'!S31
    value = 1185.26
    formula = "=('Input RPS'!T120+'Input RPS'!T115+'Input RPS'!T109+'Input RPS'!T103)/1000"
    @eval_fn
    def S31():
        t120_1 = Input_RPS.T120()
        t115_1 = Input_RPS.T115()
        var_1 = add(t120_1, t115_1)
        t109_1 = Input_RPS.T109()
        var_2 = add(var_1, t109_1)
        t103_1 = Input_RPS.T103()
        var_3 = add(var_2, t103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class T31():
    # 'Dashboard_M8_Alt'!T31
    value = 1297.564
    formula = "=('Input RPS'!U120+'Input RPS'!U115+'Input RPS'!U109+'Input RPS'!U103)/1000"
    @eval_fn
    def T31():
        u120_1 = Input_RPS.U120()
        u115_1 = Input_RPS.U115()
        var_1 = add(u120_1, u115_1)
        u109_1 = Input_RPS.U109()
        var_2 = add(var_1, u109_1)
        u103_1 = Input_RPS.U103()
        var_3 = add(var_2, u103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class U31():
    # 'Dashboard_M8_Alt'!U31
    value = 1394.403
    formula = "=('Input RPS'!V120+'Input RPS'!V115+'Input RPS'!V109+'Input RPS'!V103)/1000"
    @eval_fn
    def U31():
        v120_1 = Input_RPS.V120()
        v115_1 = Input_RPS.V115()
        var_1 = add(v120_1, v115_1)
        v109_1 = Input_RPS.V109()
        var_2 = add(var_1, v109_1)
        v103_1 = Input_RPS.V103()
        var_3 = add(var_2, v103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class V31():
    # 'Dashboard_M8_Alt'!V31
    value = 1491.242
    formula = "=('Input RPS'!W120+'Input RPS'!W115+'Input RPS'!W109+'Input RPS'!W103)/1000"
    @eval_fn
    def V31():
        w120_1 = Input_RPS.W120()
        w115_1 = Input_RPS.W115()
        var_1 = add(w120_1, w115_1)
        w109_1 = Input_RPS.W109()
        var_2 = add(var_1, w109_1)
        w103_1 = Input_RPS.W103()
        var_3 = add(var_2, w103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class W31():
    # 'Dashboard_M8_Alt'!W31
    value = 0
    formula = "=('Input RPS'!X120+'Input RPS'!X115+'Input RPS'!X109+'Input RPS'!X103)/1000"
    @eval_fn
    def W31():
        x120_1 = Input_RPS.X120()
        x115_1 = Input_RPS.X115()
        var_1 = add(x120_1, x115_1)
        x109_1 = Input_RPS.X109()
        var_2 = add(var_1, x109_1)
        x103_1 = Input_RPS.X103()
        var_3 = add(var_2, x103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class X31():
    # 'Dashboard_M8_Alt'!X31
    value = 0
    formula = "=('Input RPS'!Y120+'Input RPS'!Y115+'Input RPS'!Y109+'Input RPS'!Y103)/1000"
    @eval_fn
    def X31():
        y120_1 = Input_RPS.Y120()
        y115_1 = Input_RPS.Y115()
        var_1 = add(y120_1, y115_1)
        y109_1 = Input_RPS.Y109()
        var_2 = add(var_1, y109_1)
        y103_1 = Input_RPS.Y103()
        var_3 = add(var_2, y103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class Y31():
    # 'Dashboard_M8_Alt'!Y31
    value = 0
    formula = "=('Input RPS'!Z120+'Input RPS'!Z115+'Input RPS'!Z109+'Input RPS'!Z103)/1000"
    @eval_fn
    def Y31():
        z120_1 = Input_RPS.Z120()
        z115_1 = Input_RPS.Z115()
        var_1 = add(z120_1, z115_1)
        z109_1 = Input_RPS.Z109()
        var_2 = add(var_1, z109_1)
        z103_1 = Input_RPS.Z103()
        var_3 = add(var_2, z103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class Z31():
    # 'Dashboard_M8_Alt'!Z31
    value = 0
    formula = "=('Input RPS'!AA120+'Input RPS'!AA115+'Input RPS'!AA109+'Input RPS'!AA103)/1000"
    @eval_fn
    def Z31():
        aa120_1 = Input_RPS.AA120()
        aa115_1 = Input_RPS.AA115()
        var_1 = add(aa120_1, aa115_1)
        aa109_1 = Input_RPS.AA109()
        var_2 = add(var_1, aa109_1)
        aa103_1 = Input_RPS.AA103()
        var_3 = add(var_2, aa103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AA31():
    # 'Dashboard_M8_Alt'!AA31
    value = 0
    formula = "=('Input RPS'!AB120+'Input RPS'!AB115+'Input RPS'!AB109+'Input RPS'!AB103)/1000"
    @eval_fn
    def AA31():
        ab120_1 = Input_RPS.AB120()
        ab115_1 = Input_RPS.AB115()
        var_1 = add(ab120_1, ab115_1)
        ab109_1 = Input_RPS.AB109()
        var_2 = add(var_1, ab109_1)
        ab103_1 = Input_RPS.AB103()
        var_3 = add(var_2, ab103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AB31():
    # 'Dashboard_M8_Alt'!AB31
    value = 0
    formula = "=('Input RPS'!AC120+'Input RPS'!AC115+'Input RPS'!AC109+'Input RPS'!AC103)/1000"
    @eval_fn
    def AB31():
        ac120_1 = Input_RPS.AC120()
        ac115_1 = Input_RPS.AC115()
        var_1 = add(ac120_1, ac115_1)
        ac109_1 = Input_RPS.AC109()
        var_2 = add(var_1, ac109_1)
        ac103_1 = Input_RPS.AC103()
        var_3 = add(var_2, ac103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AC31():
    # 'Dashboard_M8_Alt'!AC31
    value = 0
    formula = "=('Input RPS'!AD120+'Input RPS'!AD115+'Input RPS'!AD109+'Input RPS'!AD103)/1000"
    @eval_fn
    def AC31():
        ad120_1 = Input_RPS.AD120()
        ad115_1 = Input_RPS.AD115()
        var_1 = add(ad120_1, ad115_1)
        ad109_1 = Input_RPS.AD109()
        var_2 = add(var_1, ad109_1)
        ad103_1 = Input_RPS.AD103()
        var_3 = add(var_2, ad103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AD31():
    # 'Dashboard_M8_Alt'!AD31
    value = 0
    formula = "=('Input RPS'!AE120+'Input RPS'!AE115+'Input RPS'!AE109+'Input RPS'!AE103)/1000"
    @eval_fn
    def AD31():
        ae120_1 = Input_RPS.AE120()
        ae115_1 = Input_RPS.AE115()
        var_1 = add(ae120_1, ae115_1)
        ae109_1 = Input_RPS.AE109()
        var_2 = add(var_1, ae109_1)
        ae103_1 = Input_RPS.AE103()
        var_3 = add(var_2, ae103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AE31():
    # 'Dashboard_M8_Alt'!AE31
    value = 0
    formula = "=('Input RPS'!AF120+'Input RPS'!AF115+'Input RPS'!AF109+'Input RPS'!AF103)/1000"
    @eval_fn
    def AE31():
        af120_1 = Input_RPS.AF120()
        af115_1 = Input_RPS.AF115()
        var_1 = add(af120_1, af115_1)
        af109_1 = Input_RPS.AF109()
        var_2 = add(var_1, af109_1)
        af103_1 = Input_RPS.AF103()
        var_3 = add(var_2, af103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AF31():
    # 'Dashboard_M8_Alt'!AF31
    value = 0
    formula = "=('Input RPS'!AG120+'Input RPS'!AG115+'Input RPS'!AG109+'Input RPS'!AG103)/1000"
    @eval_fn
    def AF31():
        ag120_1 = Input_RPS.AG120()
        ag115_1 = Input_RPS.AG115()
        var_1 = add(ag120_1, ag115_1)
        ag109_1 = Input_RPS.AG109()
        var_2 = add(var_1, ag109_1)
        ag103_1 = Input_RPS.AG103()
        var_3 = add(var_2, ag103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AG31():
    # 'Dashboard_M8_Alt'!AG31
    value = 0
    formula = "=('Input RPS'!AH120+'Input RPS'!AH115+'Input RPS'!AH109+'Input RPS'!AH103)/1000"
    @eval_fn
    def AG31():
        ah120_1 = Input_RPS.AH120()
        ah115_1 = Input_RPS.AH115()
        var_1 = add(ah120_1, ah115_1)
        ah109_1 = Input_RPS.AH109()
        var_2 = add(var_1, ah109_1)
        ah103_1 = Input_RPS.AH103()
        var_3 = add(var_2, ah103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AH31():
    # 'Dashboard_M8_Alt'!AH31
    value = 0
    formula = "=('Input RPS'!AI120+'Input RPS'!AI115+'Input RPS'!AI109+'Input RPS'!AI103)/1000"
    @eval_fn
    def AH31():
        ai120_1 = Input_RPS.AI120()
        ai115_1 = Input_RPS.AI115()
        var_1 = add(ai120_1, ai115_1)
        ai109_1 = Input_RPS.AI109()
        var_2 = add(var_1, ai109_1)
        ai103_1 = Input_RPS.AI103()
        var_3 = add(var_2, ai103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AI31():
    # 'Dashboard_M8_Alt'!AI31
    value = 0
    formula = "=('Input RPS'!AJ120+'Input RPS'!AJ115+'Input RPS'!AJ109+'Input RPS'!AJ103)/1000"
    @eval_fn
    def AI31():
        aj120_1 = Input_RPS.AJ120()
        aj115_1 = Input_RPS.AJ115()
        var_1 = add(aj120_1, aj115_1)
        aj109_1 = Input_RPS.AJ109()
        var_2 = add(var_1, aj109_1)
        aj103_1 = Input_RPS.AJ103()
        var_3 = add(var_2, aj103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AJ31():
    # 'Dashboard_M8_Alt'!AJ31
    value = 0
    formula = "=('Input RPS'!AK120+'Input RPS'!AK115+'Input RPS'!AK109+'Input RPS'!AK103)/1000"
    @eval_fn
    def AJ31():
        ak120_1 = Input_RPS.AK120()
        ak115_1 = Input_RPS.AK115()
        var_1 = add(ak120_1, ak115_1)
        ak109_1 = Input_RPS.AK109()
        var_2 = add(var_1, ak109_1)
        ak103_1 = Input_RPS.AK103()
        var_3 = add(var_2, ak103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class AK31():
    # 'Dashboard_M8_Alt'!AK31
    value = 0
    formula = "=('Input RPS'!AL120+'Input RPS'!AL115+'Input RPS'!AL109+'Input RPS'!AL103)/1000"
    @eval_fn
    def AK31():
        al120_1 = Input_RPS.AL120()
        al115_1 = Input_RPS.AL115()
        var_1 = add(al120_1, al115_1)
        al109_1 = Input_RPS.AL109()
        var_2 = add(var_1, al109_1)
        al103_1 = Input_RPS.AL103()
        var_3 = add(var_2, al103_1)
        var_4 = divide(var_3, 1000)
        return var_4

@register(Dashboard_M8_Alt)
class B32():
    # 'Dashboard_M8_Alt'!B32
    value = "Baseline Comparative Consumption"

@register(Dashboard_M8_Alt)
class C32():
    # 'Dashboard_M8_Alt'!C32
    value = "Million kWh"

@register(Dashboard_M8_Alt)
class D32():
    # 'Dashboard_M8_Alt'!D32
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://dms.puc.hawaii.gov/dms/OpenDocServlet?RT=&document_id=91+3+ICM4+LSDB15+PC_DocketReport59+26+A1001001A12D04B24000E5143818+A12D04B24000E514381+14+1960'''

@register(Dashboard_M8_Alt)
class G32():
    # 'Dashboard_M8_Alt'!G32
    value = 9043.699
    formula = "=SUM(G28:G31)"
    @eval_fn
    def G32():
        range_1 = Dashboard_M8_Alt(7, 28, 7, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class H32():
    # 'Dashboard_M8_Alt'!H32
    value = 9198.798
    formula = "=SUM(H28:H31)"
    @eval_fn
    def H32():
        range_1 = Dashboard_M8_Alt(8, 28, 8, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class I32():
    # 'Dashboard_M8_Alt'!I32
    value = 9477.631
    formula = "=SUM(I28:I31)"
    @eval_fn
    def I32():
        range_1 = Dashboard_M8_Alt(9, 28, 9, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class J32():
    # 'Dashboard_M8_Alt'!J32
    value = 9544.999
    formula = "=SUM(J28:J31)"
    @eval_fn
    def J32():
        range_1 = Dashboard_M8_Alt(10, 28, 10, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class K32():
    # 'Dashboard_M8_Alt'!K32
    value = 9806.228
    formula = "=SUM(K28:K31)"
    @eval_fn
    def K32():
        range_1 = Dashboard_M8_Alt(11, 28, 11, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class L32():
    # 'Dashboard_M8_Alt'!L32
    value = 10276.3821209
    formula = "=SUM(L28:L31)"
    @eval_fn
    def L32():
        range_1 = Dashboard_M8_Alt(12, 28, 12, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class M32():
    # 'Dashboard_M8_Alt'!M32
    value = 10215.9567975
    formula = "=SUM(M28:M31)"
    @eval_fn
    def M32():
        range_1 = Dashboard_M8_Alt(13, 28, 13, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class N32():
    # 'Dashboard_M8_Alt'!N32
    value = 10274.7464166
    formula = "=SUM(N28:N31)"
    @eval_fn
    def N32():
        range_1 = Dashboard_M8_Alt(14, 28, 14, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class O32():
    # 'Dashboard_M8_Alt'!O32
    value = 10166.462184
    formula = "=SUM(O28:O31)"
    @eval_fn
    def O32():
        range_1 = Dashboard_M8_Alt(15, 28, 15, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class P32():
    # 'Dashboard_M8_Alt'!P32
    value = 9974.987736
    formula = "=SUM(P28:P31)"
    @eval_fn
    def P32():
        range_1 = Dashboard_M8_Alt(16, 28, 16, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q32():
    # 'Dashboard_M8_Alt'!Q32
    value = 9983.936227
    formula = "=SUM(Q28:Q31)"
    @eval_fn
    def Q32():
        range_1 = Dashboard_M8_Alt(17, 28, 17, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class R32():
    # 'Dashboard_M8_Alt'!R32
    value = 9807.67089
    formula = "=SUM(R28:R31)"
    @eval_fn
    def R32():
        range_1 = Dashboard_M8_Alt(18, 28, 18, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class S32():
    # 'Dashboard_M8_Alt'!S32
    value = 9519.030235
    formula = "=SUM(S28:S31)"
    @eval_fn
    def S32():
        range_1 = Dashboard_M8_Alt(19, 28, 19, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class T32():
    # 'Dashboard_M8_Alt'!T32
    value = 9109.72247175
    formula = "=SUM(T28:T31)"
    @eval_fn
    def T32():
        range_1 = Dashboard_M8_Alt(20, 28, 20, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class U32():
    # 'Dashboard_M8_Alt'!U32
    value = 8830.50005637
    formula = "=SUM(U28:U31)"
    @eval_fn
    def U32():
        range_1 = Dashboard_M8_Alt(21, 28, 21, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class V32():
    # 'Dashboard_M8_Alt'!V32
    value = 8719.494
    formula = "=SUM(V28:V31)"
    @eval_fn
    def V32():
        range_1 = Dashboard_M8_Alt(22, 28, 22, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class W32():
    # 'Dashboard_M8_Alt'!W32
    value = 0
    formula = "=SUM(W28:W31)"
    @eval_fn
    def W32():
        range_1 = Dashboard_M8_Alt(23, 28, 23, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class X32():
    # 'Dashboard_M8_Alt'!X32
    value = 0
    formula = "=SUM(X28:X31)"
    @eval_fn
    def X32():
        range_1 = Dashboard_M8_Alt(24, 28, 24, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y32():
    # 'Dashboard_M8_Alt'!Y32
    value = 0
    formula = "=SUM(Y28:Y31)"
    @eval_fn
    def Y32():
        range_1 = Dashboard_M8_Alt(25, 28, 25, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z32():
    # 'Dashboard_M8_Alt'!Z32
    value = 0
    formula = "=SUM(Z28:Z31)"
    @eval_fn
    def Z32():
        range_1 = Dashboard_M8_Alt(26, 28, 26, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA32():
    # 'Dashboard_M8_Alt'!AA32
    value = 0
    formula = "=SUM(AA28:AA31)"
    @eval_fn
    def AA32():
        range_1 = Dashboard_M8_Alt(27, 28, 27, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB32():
    # 'Dashboard_M8_Alt'!AB32
    value = 0
    formula = "=SUM(AB28:AB31)"
    @eval_fn
    def AB32():
        range_1 = Dashboard_M8_Alt(28, 28, 28, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC32():
    # 'Dashboard_M8_Alt'!AC32
    value = 0
    formula = "=SUM(AC28:AC31)"
    @eval_fn
    def AC32():
        range_1 = Dashboard_M8_Alt(29, 28, 29, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD32():
    # 'Dashboard_M8_Alt'!AD32
    value = 0
    formula = "=SUM(AD28:AD31)"
    @eval_fn
    def AD32():
        range_1 = Dashboard_M8_Alt(30, 28, 30, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE32():
    # 'Dashboard_M8_Alt'!AE32
    value = 0
    formula = "=SUM(AE28:AE31)"
    @eval_fn
    def AE32():
        range_1 = Dashboard_M8_Alt(31, 28, 31, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF32():
    # 'Dashboard_M8_Alt'!AF32
    value = 0
    formula = "=SUM(AF28:AF31)"
    @eval_fn
    def AF32():
        range_1 = Dashboard_M8_Alt(32, 28, 32, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG32():
    # 'Dashboard_M8_Alt'!AG32
    value = 0
    formula = "=SUM(AG28:AG31)"
    @eval_fn
    def AG32():
        range_1 = Dashboard_M8_Alt(33, 28, 33, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH32():
    # 'Dashboard_M8_Alt'!AH32
    value = 0
    formula = "=SUM(AH28:AH31)"
    @eval_fn
    def AH32():
        range_1 = Dashboard_M8_Alt(34, 28, 34, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI32():
    # 'Dashboard_M8_Alt'!AI32
    value = 0
    formula = "=SUM(AI28:AI31)"
    @eval_fn
    def AI32():
        range_1 = Dashboard_M8_Alt(35, 28, 35, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ32():
    # 'Dashboard_M8_Alt'!AJ32
    value = 0
    formula = "=SUM(AJ28:AJ31)"
    @eval_fn
    def AJ32():
        range_1 = Dashboard_M8_Alt(36, 28, 36, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK32():
    # 'Dashboard_M8_Alt'!AK32
    value = 0
    formula = "=SUM(AK28:AK31)"
    @eval_fn
    def AK32():
        range_1 = Dashboard_M8_Alt(37, 28, 37, 31)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class A34():
    # 'Dashboard_M8_Alt'!A34
    value = "Variable HF(2005,c,p,y): Hypothetical Power Sector Fuel Consumption by energy source and year"
    formula = '''="Variable HF("&$D$4&",c,p,y): Hypothetical Power Sector Fuel Consumption by energy source and year"'''
    @eval_fn
    def A34():
        d4_1 = Dashboard_M8_Alt.D4()
        var_1 = concat("Variable HF(", d4_1)
        var_2 = concat(var_1, ",c,p,y): Hypothetical Power Sector Fuel Consumption by energy source and year")
        return var_2

@register(Dashboard_M8_Alt)
class B36():
    # 'Dashboard_M8_Alt'!B36
    value = "Diesel"

@register(Dashboard_M8_Alt)
class C36():
    # 'Dashboard_M8_Alt'!C36
    value = "MMBtu"

@register(Dashboard_M8_Alt)
class I36():
    # 'Dashboard_M8_Alt'!I36
    value = 14482873.7638
    formula = "=I$32*$D19"
    @eval_fn
    def I36():
        i32_1 = Dashboard_M8_Alt.I32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(i32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class J36():
    # 'Dashboard_M8_Alt'!J36
    value = 14585819.5569
    formula = "=J$32*$D19"
    @eval_fn
    def J36():
        j32_1 = Dashboard_M8_Alt.J32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(j32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class K36():
    # 'Dashboard_M8_Alt'!K36
    value = 14985006.5088
    formula = "=K$32*$D19"
    @eval_fn
    def K36():
        k32_1 = Dashboard_M8_Alt.K32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(k32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class L36():
    # 'Dashboard_M8_Alt'!L36
    value = 15703454.2711
    formula = "=L$32*$D19"
    @eval_fn
    def L36():
        l32_1 = Dashboard_M8_Alt.L32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(l32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class M36():
    # 'Dashboard_M8_Alt'!M36
    value = 15611117.6596
    formula = "=M$32*$D19"
    @eval_fn
    def M36():
        m32_1 = Dashboard_M8_Alt.M32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(m32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class N36():
    # 'Dashboard_M8_Alt'!N36
    value = 15700954.733
    formula = "=N$32*$D19"
    @eval_fn
    def N36():
        n32_1 = Dashboard_M8_Alt.N32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(n32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class O36():
    # 'Dashboard_M8_Alt'!O36
    value = 15535484.388
    formula = "=O$32*$D19"
    @eval_fn
    def O36():
        o32_1 = Dashboard_M8_Alt.O32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(o32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class P36():
    # 'Dashboard_M8_Alt'!P36
    value = 15242890.1459
    formula = "=P$32*$D19"
    @eval_fn
    def P36():
        p32_1 = Dashboard_M8_Alt.P32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(p32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q36():
    # 'Dashboard_M8_Alt'!Q36
    value = 15256564.4349
    formula = "=Q$32*$D19"
    @eval_fn
    def Q36():
        q32_1 = Dashboard_M8_Alt.Q32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(q32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class R36():
    # 'Dashboard_M8_Alt'!R36
    value = 14987211.4052
    formula = "=R$32*$D19"
    @eval_fn
    def R36():
        r32_1 = Dashboard_M8_Alt.R32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(r32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class S36():
    # 'Dashboard_M8_Alt'!S36
    value = 14546136.3971
    formula = "=S$32*$D19"
    @eval_fn
    def S36():
        s32_1 = Dashboard_M8_Alt.S32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(s32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class T36():
    # 'Dashboard_M8_Alt'!T36
    value = 13920668.6335
    formula = "=T$32*$D19"
    @eval_fn
    def T36():
        t32_1 = Dashboard_M8_Alt.T32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(t32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class U36():
    # 'Dashboard_M8_Alt'!U36
    value = 13493985.7426
    formula = "=U$32*$D19"
    @eval_fn
    def U36():
        u32_1 = Dashboard_M8_Alt.U32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(u32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class V36():
    # 'Dashboard_M8_Alt'!V36
    value = 13324356.1483
    formula = "=V$32*$D19"
    @eval_fn
    def V36():
        v32_1 = Dashboard_M8_Alt.V32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(v32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class W36():
    # 'Dashboard_M8_Alt'!W36
    value = 0
    formula = "=W$32*$D19"
    @eval_fn
    def W36():
        w32_1 = Dashboard_M8_Alt.W32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(w32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class X36():
    # 'Dashboard_M8_Alt'!X36
    value = 0
    formula = "=X$32*$D19"
    @eval_fn
    def X36():
        x32_1 = Dashboard_M8_Alt.X32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(x32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y36():
    # 'Dashboard_M8_Alt'!Y36
    value = 0
    formula = "=Y$32*$D19"
    @eval_fn
    def Y36():
        y32_1 = Dashboard_M8_Alt.Y32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(y32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z36():
    # 'Dashboard_M8_Alt'!Z36
    value = 0
    formula = "=Z$32*$D19"
    @eval_fn
    def Z36():
        z32_1 = Dashboard_M8_Alt.Z32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(z32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA36():
    # 'Dashboard_M8_Alt'!AA36
    value = 0
    formula = "=AA$32*$D19"
    @eval_fn
    def AA36():
        aa32_1 = Dashboard_M8_Alt.AA32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(aa32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB36():
    # 'Dashboard_M8_Alt'!AB36
    value = 0
    formula = "=AB$32*$D19"
    @eval_fn
    def AB36():
        ab32_1 = Dashboard_M8_Alt.AB32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(ab32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC36():
    # 'Dashboard_M8_Alt'!AC36
    value = 0
    formula = "=AC$32*$D19"
    @eval_fn
    def AC36():
        ac32_1 = Dashboard_M8_Alt.AC32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(ac32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD36():
    # 'Dashboard_M8_Alt'!AD36
    value = 0
    formula = "=AD$32*$D19"
    @eval_fn
    def AD36():
        ad32_1 = Dashboard_M8_Alt.AD32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(ad32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE36():
    # 'Dashboard_M8_Alt'!AE36
    value = 0
    formula = "=AE$32*$D19"
    @eval_fn
    def AE36():
        ae32_1 = Dashboard_M8_Alt.AE32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(ae32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF36():
    # 'Dashboard_M8_Alt'!AF36
    value = 0
    formula = "=AF$32*$D19"
    @eval_fn
    def AF36():
        af32_1 = Dashboard_M8_Alt.AF32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(af32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG36():
    # 'Dashboard_M8_Alt'!AG36
    value = 0
    formula = "=AG$32*$D19"
    @eval_fn
    def AG36():
        ag32_1 = Dashboard_M8_Alt.AG32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(ag32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH36():
    # 'Dashboard_M8_Alt'!AH36
    value = 0
    formula = "=AH$32*$D19"
    @eval_fn
    def AH36():
        ah32_1 = Dashboard_M8_Alt.AH32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(ah32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI36():
    # 'Dashboard_M8_Alt'!AI36
    value = 0
    formula = "=AI$32*$D19"
    @eval_fn
    def AI36():
        ai32_1 = Dashboard_M8_Alt.AI32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(ai32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ36():
    # 'Dashboard_M8_Alt'!AJ36
    value = 0
    formula = "=AJ$32*$D19"
    @eval_fn
    def AJ36():
        aj32_1 = Dashboard_M8_Alt.AJ32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(aj32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK36():
    # 'Dashboard_M8_Alt'!AK36
    value = 0
    formula = "=AK$32*$D19"
    @eval_fn
    def AK36():
        ak32_1 = Dashboard_M8_Alt.AK32()
        d19_1 = Dashboard_M8_Alt.D19()
        var_1 = mult(ak32_1, d19_1)
        return var_1

@register(Dashboard_M8_Alt)
class B37():
    # 'Dashboard_M8_Alt'!B37
    value = "Fuel Oil"

@register(Dashboard_M8_Alt)
class C37():
    # 'Dashboard_M8_Alt'!C37
    value = "MMBtu"

@register(Dashboard_M8_Alt)
class I37():
    # 'Dashboard_M8_Alt'!I37
    value = 68378252.7334
    formula = "=I$32*$D20"
    @eval_fn
    def I37():
        i32_1 = Dashboard_M8_Alt.I32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(i32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class J37():
    # 'Dashboard_M8_Alt'!J37
    value = 68864292.5603
    formula = "=J$32*$D20"
    @eval_fn
    def J37():
        j32_1 = Dashboard_M8_Alt.J32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(j32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class K37():
    # 'Dashboard_M8_Alt'!K37
    value = 70748981.1057
    formula = "=K$32*$D20"
    @eval_fn
    def K37():
        k32_1 = Dashboard_M8_Alt.K32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(k32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class L37():
    # 'Dashboard_M8_Alt'!L37
    value = 74141001.4644
    formula = "=L$32*$D20"
    @eval_fn
    def L37():
        l32_1 = Dashboard_M8_Alt.L32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(l32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class M37():
    # 'Dashboard_M8_Alt'!M37
    value = 73705050.958
    formula = "=M$32*$D20"
    @eval_fn
    def M37():
        m32_1 = Dashboard_M8_Alt.M32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(m32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class N37():
    # 'Dashboard_M8_Alt'!N37
    value = 74129200.3504
    formula = "=N$32*$D20"
    @eval_fn
    def N37():
        n32_1 = Dashboard_M8_Alt.N32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(n32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class O37():
    # 'Dashboard_M8_Alt'!O37
    value = 73347962.2305
    formula = "=O$32*$D20"
    @eval_fn
    def O37():
        o32_1 = Dashboard_M8_Alt.O32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(o32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class P37():
    # 'Dashboard_M8_Alt'!P37
    value = 71966531.7657
    formula = "=P$32*$D20"
    @eval_fn
    def P37():
        p32_1 = Dashboard_M8_Alt.P32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(p32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q37():
    # 'Dashboard_M8_Alt'!Q37
    value = 72031092.4327
    formula = "=Q$32*$D20"
    @eval_fn
    def Q37():
        q32_1 = Dashboard_M8_Alt.Q32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(q32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class R37():
    # 'Dashboard_M8_Alt'!R37
    value = 70759391.1224
    formula = "=R$32*$D20"
    @eval_fn
    def R37():
        r32_1 = Dashboard_M8_Alt.R32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(r32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class S37():
    # 'Dashboard_M8_Alt'!S37
    value = 68676935.7433
    formula = "=S$32*$D20"
    @eval_fn
    def S37():
        s32_1 = Dashboard_M8_Alt.S32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(s32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class T37():
    # 'Dashboard_M8_Alt'!T37
    value = 65723903.5266
    formula = "=T$32*$D20"
    @eval_fn
    def T37():
        t32_1 = Dashboard_M8_Alt.T32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(t32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class U37():
    # 'Dashboard_M8_Alt'!U37
    value = 63709397.9093
    formula = "=U$32*$D20"
    @eval_fn
    def U37():
        u32_1 = Dashboard_M8_Alt.U32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(u32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class V37():
    # 'Dashboard_M8_Alt'!V37
    value = 62908522.6508
    formula = "=V$32*$D20"
    @eval_fn
    def V37():
        v32_1 = Dashboard_M8_Alt.V32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(v32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class W37():
    # 'Dashboard_M8_Alt'!W37
    value = 0
    formula = "=W$32*$D20"
    @eval_fn
    def W37():
        w32_1 = Dashboard_M8_Alt.W32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(w32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class X37():
    # 'Dashboard_M8_Alt'!X37
    value = 0
    formula = "=X$32*$D20"
    @eval_fn
    def X37():
        x32_1 = Dashboard_M8_Alt.X32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(x32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y37():
    # 'Dashboard_M8_Alt'!Y37
    value = 0
    formula = "=Y$32*$D20"
    @eval_fn
    def Y37():
        y32_1 = Dashboard_M8_Alt.Y32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(y32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z37():
    # 'Dashboard_M8_Alt'!Z37
    value = 0
    formula = "=Z$32*$D20"
    @eval_fn
    def Z37():
        z32_1 = Dashboard_M8_Alt.Z32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(z32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA37():
    # 'Dashboard_M8_Alt'!AA37
    value = 0
    formula = "=AA$32*$D20"
    @eval_fn
    def AA37():
        aa32_1 = Dashboard_M8_Alt.AA32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(aa32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB37():
    # 'Dashboard_M8_Alt'!AB37
    value = 0
    formula = "=AB$32*$D20"
    @eval_fn
    def AB37():
        ab32_1 = Dashboard_M8_Alt.AB32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(ab32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC37():
    # 'Dashboard_M8_Alt'!AC37
    value = 0
    formula = "=AC$32*$D20"
    @eval_fn
    def AC37():
        ac32_1 = Dashboard_M8_Alt.AC32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(ac32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD37():
    # 'Dashboard_M8_Alt'!AD37
    value = 0
    formula = "=AD$32*$D20"
    @eval_fn
    def AD37():
        ad32_1 = Dashboard_M8_Alt.AD32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(ad32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE37():
    # 'Dashboard_M8_Alt'!AE37
    value = 0
    formula = "=AE$32*$D20"
    @eval_fn
    def AE37():
        ae32_1 = Dashboard_M8_Alt.AE32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(ae32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF37():
    # 'Dashboard_M8_Alt'!AF37
    value = 0
    formula = "=AF$32*$D20"
    @eval_fn
    def AF37():
        af32_1 = Dashboard_M8_Alt.AF32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(af32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG37():
    # 'Dashboard_M8_Alt'!AG37
    value = 0
    formula = "=AG$32*$D20"
    @eval_fn
    def AG37():
        ag32_1 = Dashboard_M8_Alt.AG32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(ag32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH37():
    # 'Dashboard_M8_Alt'!AH37
    value = 0
    formula = "=AH$32*$D20"
    @eval_fn
    def AH37():
        ah32_1 = Dashboard_M8_Alt.AH32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(ah32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI37():
    # 'Dashboard_M8_Alt'!AI37
    value = 0
    formula = "=AI$32*$D20"
    @eval_fn
    def AI37():
        ai32_1 = Dashboard_M8_Alt.AI32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(ai32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ37():
    # 'Dashboard_M8_Alt'!AJ37
    value = 0
    formula = "=AJ$32*$D20"
    @eval_fn
    def AJ37():
        aj32_1 = Dashboard_M8_Alt.AJ32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(aj32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK37():
    # 'Dashboard_M8_Alt'!AK37
    value = 0
    formula = "=AK$32*$D20"
    @eval_fn
    def AK37():
        ak32_1 = Dashboard_M8_Alt.AK32()
        d20_1 = Dashboard_M8_Alt.D20()
        var_1 = mult(ak32_1, d20_1)
        return var_1

@register(Dashboard_M8_Alt)
class B38():
    # 'Dashboard_M8_Alt'!B38
    value = "SNG"

@register(Dashboard_M8_Alt)
class C38():
    # 'Dashboard_M8_Alt'!C38
    value = "MMBtu"

@register(Dashboard_M8_Alt)
class I38():
    # 'Dashboard_M8_Alt'!I38
    value = 0
    formula = "=I$32*$D21"
    @eval_fn
    def I38():
        i32_1 = Dashboard_M8_Alt.I32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(i32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class J38():
    # 'Dashboard_M8_Alt'!J38
    value = 0
    formula = "=J$32*$D21"
    @eval_fn
    def J38():
        j32_1 = Dashboard_M8_Alt.J32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(j32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class K38():
    # 'Dashboard_M8_Alt'!K38
    value = 0
    formula = "=K$32*$D21"
    @eval_fn
    def K38():
        k32_1 = Dashboard_M8_Alt.K32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(k32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class L38():
    # 'Dashboard_M8_Alt'!L38
    value = 0
    formula = "=L$32*$D21"
    @eval_fn
    def L38():
        l32_1 = Dashboard_M8_Alt.L32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(l32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class M38():
    # 'Dashboard_M8_Alt'!M38
    value = 0
    formula = "=M$32*$D21"
    @eval_fn
    def M38():
        m32_1 = Dashboard_M8_Alt.M32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(m32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class N38():
    # 'Dashboard_M8_Alt'!N38
    value = 0
    formula = "=N$32*$D21"
    @eval_fn
    def N38():
        n32_1 = Dashboard_M8_Alt.N32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(n32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class O38():
    # 'Dashboard_M8_Alt'!O38
    value = 0
    formula = "=O$32*$D21"
    @eval_fn
    def O38():
        o32_1 = Dashboard_M8_Alt.O32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(o32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class P38():
    # 'Dashboard_M8_Alt'!P38
    value = 0
    formula = "=P$32*$D21"
    @eval_fn
    def P38():
        p32_1 = Dashboard_M8_Alt.P32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(p32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q38():
    # 'Dashboard_M8_Alt'!Q38
    value = 0
    formula = "=Q$32*$D21"
    @eval_fn
    def Q38():
        q32_1 = Dashboard_M8_Alt.Q32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(q32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class R38():
    # 'Dashboard_M8_Alt'!R38
    value = 0
    formula = "=R$32*$D21"
    @eval_fn
    def R38():
        r32_1 = Dashboard_M8_Alt.R32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(r32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class S38():
    # 'Dashboard_M8_Alt'!S38
    value = 0
    formula = "=S$32*$D21"
    @eval_fn
    def S38():
        s32_1 = Dashboard_M8_Alt.S32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(s32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class T38():
    # 'Dashboard_M8_Alt'!T38
    value = 0
    formula = "=T$32*$D21"
    @eval_fn
    def T38():
        t32_1 = Dashboard_M8_Alt.T32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(t32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class U38():
    # 'Dashboard_M8_Alt'!U38
    value = 0
    formula = "=U$32*$D21"
    @eval_fn
    def U38():
        u32_1 = Dashboard_M8_Alt.U32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(u32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class V38():
    # 'Dashboard_M8_Alt'!V38
    value = 0
    formula = "=V$32*$D21"
    @eval_fn
    def V38():
        v32_1 = Dashboard_M8_Alt.V32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(v32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class W38():
    # 'Dashboard_M8_Alt'!W38
    value = 0
    formula = "=W$32*$D21"
    @eval_fn
    def W38():
        w32_1 = Dashboard_M8_Alt.W32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(w32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class X38():
    # 'Dashboard_M8_Alt'!X38
    value = 0
    formula = "=X$32*$D21"
    @eval_fn
    def X38():
        x32_1 = Dashboard_M8_Alt.X32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(x32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y38():
    # 'Dashboard_M8_Alt'!Y38
    value = 0
    formula = "=Y$32*$D21"
    @eval_fn
    def Y38():
        y32_1 = Dashboard_M8_Alt.Y32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(y32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z38():
    # 'Dashboard_M8_Alt'!Z38
    value = 0
    formula = "=Z$32*$D21"
    @eval_fn
    def Z38():
        z32_1 = Dashboard_M8_Alt.Z32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(z32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA38():
    # 'Dashboard_M8_Alt'!AA38
    value = 0
    formula = "=AA$32*$D21"
    @eval_fn
    def AA38():
        aa32_1 = Dashboard_M8_Alt.AA32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(aa32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB38():
    # 'Dashboard_M8_Alt'!AB38
    value = 0
    formula = "=AB$32*$D21"
    @eval_fn
    def AB38():
        ab32_1 = Dashboard_M8_Alt.AB32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(ab32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC38():
    # 'Dashboard_M8_Alt'!AC38
    value = 0
    formula = "=AC$32*$D21"
    @eval_fn
    def AC38():
        ac32_1 = Dashboard_M8_Alt.AC32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(ac32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD38():
    # 'Dashboard_M8_Alt'!AD38
    value = 0
    formula = "=AD$32*$D21"
    @eval_fn
    def AD38():
        ad32_1 = Dashboard_M8_Alt.AD32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(ad32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE38():
    # 'Dashboard_M8_Alt'!AE38
    value = 0
    formula = "=AE$32*$D21"
    @eval_fn
    def AE38():
        ae32_1 = Dashboard_M8_Alt.AE32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(ae32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF38():
    # 'Dashboard_M8_Alt'!AF38
    value = 0
    formula = "=AF$32*$D21"
    @eval_fn
    def AF38():
        af32_1 = Dashboard_M8_Alt.AF32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(af32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG38():
    # 'Dashboard_M8_Alt'!AG38
    value = 0
    formula = "=AG$32*$D21"
    @eval_fn
    def AG38():
        ag32_1 = Dashboard_M8_Alt.AG32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(ag32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH38():
    # 'Dashboard_M8_Alt'!AH38
    value = 0
    formula = "=AH$32*$D21"
    @eval_fn
    def AH38():
        ah32_1 = Dashboard_M8_Alt.AH32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(ah32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI38():
    # 'Dashboard_M8_Alt'!AI38
    value = 0
    formula = "=AI$32*$D21"
    @eval_fn
    def AI38():
        ai32_1 = Dashboard_M8_Alt.AI32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(ai32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ38():
    # 'Dashboard_M8_Alt'!AJ38
    value = 0
    formula = "=AJ$32*$D21"
    @eval_fn
    def AJ38():
        aj32_1 = Dashboard_M8_Alt.AJ32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(aj32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK38():
    # 'Dashboard_M8_Alt'!AK38
    value = 0
    formula = "=AK$32*$D21"
    @eval_fn
    def AK38():
        ak32_1 = Dashboard_M8_Alt.AK32()
        d21_1 = Dashboard_M8_Alt.D21()
        var_1 = mult(ak32_1, d21_1)
        return var_1

@register(Dashboard_M8_Alt)
class B39():
    # 'Dashboard_M8_Alt'!B39
    value = "Coal"

@register(Dashboard_M8_Alt)
class C39():
    # 'Dashboard_M8_Alt'!C39
    value = "MMBtu"

@register(Dashboard_M8_Alt)
class I39():
    # 'Dashboard_M8_Alt'!I39
    value = 15918364.8723
    formula = "=I$32*$D22"
    @eval_fn
    def I39():
        i32_1 = Dashboard_M8_Alt.I32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(i32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class J39():
    # 'Dashboard_M8_Alt'!J39
    value = 16031514.2875
    formula = "=J$32*$D22"
    @eval_fn
    def J39():
        j32_1 = Dashboard_M8_Alt.J32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(j32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class K39():
    # 'Dashboard_M8_Alt'!K39
    value = 16470267.235
    formula = "=K$32*$D22"
    @eval_fn
    def K39():
        k32_1 = Dashboard_M8_Alt.K32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(k32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class L39():
    # 'Dashboard_M8_Alt'!L39
    value = 17259924.9927
    formula = "=L$32*$D22"
    @eval_fn
    def L39():
        l32_1 = Dashboard_M8_Alt.L32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(l32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class M39():
    # 'Dashboard_M8_Alt'!M39
    value = 17158436.3036
    formula = "=M$32*$D22"
    @eval_fn
    def M39():
        m32_1 = Dashboard_M8_Alt.M32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(m32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class N39():
    # 'Dashboard_M8_Alt'!N39
    value = 17257177.7093
    formula = "=N$32*$D22"
    @eval_fn
    def N39():
        n32_1 = Dashboard_M8_Alt.N32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(n32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class O39():
    # 'Dashboard_M8_Alt'!O39
    value = 17075306.5302
    formula = "=O$32*$D22"
    @eval_fn
    def O39():
        o32_1 = Dashboard_M8_Alt.O32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(o32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class P39():
    # 'Dashboard_M8_Alt'!P39
    value = 16753711.384
    formula = "=P$32*$D22"
    @eval_fn
    def P39():
        p32_1 = Dashboard_M8_Alt.P32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(p32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q39():
    # 'Dashboard_M8_Alt'!Q39
    value = 16768741.0201
    formula = "=Q$32*$D22"
    @eval_fn
    def Q39():
        q32_1 = Dashboard_M8_Alt.Q32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(q32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class R39():
    # 'Dashboard_M8_Alt'!R39
    value = 16472690.6729
    formula = "=R$32*$D22"
    @eval_fn
    def R39():
        r32_1 = Dashboard_M8_Alt.R32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(r32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class S39():
    # 'Dashboard_M8_Alt'!S39
    value = 15987897.8736
    formula = "=S$32*$D22"
    @eval_fn
    def S39():
        s32_1 = Dashboard_M8_Alt.S32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(s32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class T39():
    # 'Dashboard_M8_Alt'!T39
    value = 15300435.9624
    formula = "=T$32*$D22"
    @eval_fn
    def T39():
        t32_1 = Dashboard_M8_Alt.T32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(t32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class U39():
    # 'Dashboard_M8_Alt'!U39
    value = 14831461.7759
    formula = "=U$32*$D22"
    @eval_fn
    def U39():
        u32_1 = Dashboard_M8_Alt.U32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(u32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class V39():
    # 'Dashboard_M8_Alt'!V39
    value = 14645019.0975
    formula = "=V$32*$D22"
    @eval_fn
    def V39():
        v32_1 = Dashboard_M8_Alt.V32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(v32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class W39():
    # 'Dashboard_M8_Alt'!W39
    value = 0
    formula = "=W$32*$D22"
    @eval_fn
    def W39():
        w32_1 = Dashboard_M8_Alt.W32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(w32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class X39():
    # 'Dashboard_M8_Alt'!X39
    value = 0
    formula = "=X$32*$D22"
    @eval_fn
    def X39():
        x32_1 = Dashboard_M8_Alt.X32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(x32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y39():
    # 'Dashboard_M8_Alt'!Y39
    value = 0
    formula = "=Y$32*$D22"
    @eval_fn
    def Y39():
        y32_1 = Dashboard_M8_Alt.Y32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(y32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z39():
    # 'Dashboard_M8_Alt'!Z39
    value = 0
    formula = "=Z$32*$D22"
    @eval_fn
    def Z39():
        z32_1 = Dashboard_M8_Alt.Z32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(z32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA39():
    # 'Dashboard_M8_Alt'!AA39
    value = 0
    formula = "=AA$32*$D22"
    @eval_fn
    def AA39():
        aa32_1 = Dashboard_M8_Alt.AA32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(aa32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB39():
    # 'Dashboard_M8_Alt'!AB39
    value = 0
    formula = "=AB$32*$D22"
    @eval_fn
    def AB39():
        ab32_1 = Dashboard_M8_Alt.AB32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(ab32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC39():
    # 'Dashboard_M8_Alt'!AC39
    value = 0
    formula = "=AC$32*$D22"
    @eval_fn
    def AC39():
        ac32_1 = Dashboard_M8_Alt.AC32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(ac32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD39():
    # 'Dashboard_M8_Alt'!AD39
    value = 0
    formula = "=AD$32*$D22"
    @eval_fn
    def AD39():
        ad32_1 = Dashboard_M8_Alt.AD32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(ad32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE39():
    # 'Dashboard_M8_Alt'!AE39
    value = 0
    formula = "=AE$32*$D22"
    @eval_fn
    def AE39():
        ae32_1 = Dashboard_M8_Alt.AE32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(ae32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF39():
    # 'Dashboard_M8_Alt'!AF39
    value = 0
    formula = "=AF$32*$D22"
    @eval_fn
    def AF39():
        af32_1 = Dashboard_M8_Alt.AF32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(af32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG39():
    # 'Dashboard_M8_Alt'!AG39
    value = 0
    formula = "=AG$32*$D22"
    @eval_fn
    def AG39():
        ag32_1 = Dashboard_M8_Alt.AG32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(ag32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH39():
    # 'Dashboard_M8_Alt'!AH39
    value = 0
    formula = "=AH$32*$D22"
    @eval_fn
    def AH39():
        ah32_1 = Dashboard_M8_Alt.AH32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(ah32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI39():
    # 'Dashboard_M8_Alt'!AI39
    value = 0
    formula = "=AI$32*$D22"
    @eval_fn
    def AI39():
        ai32_1 = Dashboard_M8_Alt.AI32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(ai32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ39():
    # 'Dashboard_M8_Alt'!AJ39
    value = 0
    formula = "=AJ$32*$D22"
    @eval_fn
    def AJ39():
        aj32_1 = Dashboard_M8_Alt.AJ32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(aj32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK39():
    # 'Dashboard_M8_Alt'!AK39
    value = 0
    formula = "=AK$32*$D22"
    @eval_fn
    def AK39():
        ak32_1 = Dashboard_M8_Alt.AK32()
        d22_1 = Dashboard_M8_Alt.D22()
        var_1 = mult(ak32_1, d22_1)
        return var_1

@register(Dashboard_M8_Alt)
class B40():
    # 'Dashboard_M8_Alt'!B40
    value = "All Fuels"

@register(Dashboard_M8_Alt)
class C40():
    # 'Dashboard_M8_Alt'!C40
    value = "MMBtu"

@register(Dashboard_M8_Alt)
class I40():
    # 'Dashboard_M8_Alt'!I40
    value = 98779491.3696
    formula = "=I$32*$D23"
    @eval_fn
    def I40():
        i32_1 = Dashboard_M8_Alt.I32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(i32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class J40():
    # 'Dashboard_M8_Alt'!J40
    value = 99481626.4047
    formula = "=J$32*$D23"
    @eval_fn
    def J40():
        j32_1 = Dashboard_M8_Alt.J32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(j32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class K40():
    # 'Dashboard_M8_Alt'!K40
    value = 102204254.85
    formula = "=K$32*$D23"
    @eval_fn
    def K40():
        k32_1 = Dashboard_M8_Alt.K32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(k32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class L40():
    # 'Dashboard_M8_Alt'!L40
    value = 107104380.728
    formula = "=L$32*$D23"
    @eval_fn
    def L40():
        l32_1 = Dashboard_M8_Alt.L32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(l32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class M40():
    # 'Dashboard_M8_Alt'!M40
    value = 106474604.921
    formula = "=M$32*$D23"
    @eval_fn
    def M40():
        m32_1 = Dashboard_M8_Alt.M32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(m32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class N40():
    # 'Dashboard_M8_Alt'!N40
    value = 107087332.793
    formula = "=N$32*$D23"
    @eval_fn
    def N40():
        n32_1 = Dashboard_M8_Alt.N32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(n32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class O40():
    # 'Dashboard_M8_Alt'!O40
    value = 105958753.149
    formula = "=O$32*$D23"
    @eval_fn
    def O40():
        o32_1 = Dashboard_M8_Alt.O32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(o32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class P40():
    # 'Dashboard_M8_Alt'!P40
    value = 103963133.296
    formula = "=P$32*$D23"
    @eval_fn
    def P40():
        p32_1 = Dashboard_M8_Alt.P32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(p32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q40():
    # 'Dashboard_M8_Alt'!Q40
    value = 104056397.888
    formula = "=Q$32*$D23"
    @eval_fn
    def Q40():
        q32_1 = Dashboard_M8_Alt.Q32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(q32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class R40():
    # 'Dashboard_M8_Alt'!R40
    value = 102219293.2
    formula = "=R$32*$D23"
    @eval_fn
    def R40():
        r32_1 = Dashboard_M8_Alt.R32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(r32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class S40():
    # 'Dashboard_M8_Alt'!S40
    value = 99210970.014
    formula = "=S$32*$D23"
    @eval_fn
    def S40():
        s32_1 = Dashboard_M8_Alt.S32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(s32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class T40():
    # 'Dashboard_M8_Alt'!T40
    value = 94945008.1225
    formula = "=T$32*$D23"
    @eval_fn
    def T40():
        t32_1 = Dashboard_M8_Alt.T32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(t32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class U40():
    # 'Dashboard_M8_Alt'!U40
    value = 92034845.4278
    formula = "=U$32*$D23"
    @eval_fn
    def U40():
        u32_1 = Dashboard_M8_Alt.U32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(u32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class V40():
    # 'Dashboard_M8_Alt'!V40
    value = 90877897.8967
    formula = "=V$32*$D23"
    @eval_fn
    def V40():
        v32_1 = Dashboard_M8_Alt.V32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(v32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class W40():
    # 'Dashboard_M8_Alt'!W40
    value = 0
    formula = "=W$32*$D23"
    @eval_fn
    def W40():
        w32_1 = Dashboard_M8_Alt.W32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(w32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class X40():
    # 'Dashboard_M8_Alt'!X40
    value = 0
    formula = "=X$32*$D23"
    @eval_fn
    def X40():
        x32_1 = Dashboard_M8_Alt.X32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(x32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y40():
    # 'Dashboard_M8_Alt'!Y40
    value = 0
    formula = "=Y$32*$D23"
    @eval_fn
    def Y40():
        y32_1 = Dashboard_M8_Alt.Y32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(y32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z40():
    # 'Dashboard_M8_Alt'!Z40
    value = 0
    formula = "=Z$32*$D23"
    @eval_fn
    def Z40():
        z32_1 = Dashboard_M8_Alt.Z32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(z32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA40():
    # 'Dashboard_M8_Alt'!AA40
    value = 0
    formula = "=AA$32*$D23"
    @eval_fn
    def AA40():
        aa32_1 = Dashboard_M8_Alt.AA32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(aa32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB40():
    # 'Dashboard_M8_Alt'!AB40
    value = 0
    formula = "=AB$32*$D23"
    @eval_fn
    def AB40():
        ab32_1 = Dashboard_M8_Alt.AB32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(ab32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC40():
    # 'Dashboard_M8_Alt'!AC40
    value = 0
    formula = "=AC$32*$D23"
    @eval_fn
    def AC40():
        ac32_1 = Dashboard_M8_Alt.AC32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(ac32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD40():
    # 'Dashboard_M8_Alt'!AD40
    value = 0
    formula = "=AD$32*$D23"
    @eval_fn
    def AD40():
        ad32_1 = Dashboard_M8_Alt.AD32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(ad32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE40():
    # 'Dashboard_M8_Alt'!AE40
    value = 0
    formula = "=AE$32*$D23"
    @eval_fn
    def AE40():
        ae32_1 = Dashboard_M8_Alt.AE32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(ae32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF40():
    # 'Dashboard_M8_Alt'!AF40
    value = 0
    formula = "=AF$32*$D23"
    @eval_fn
    def AF40():
        af32_1 = Dashboard_M8_Alt.AF32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(af32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG40():
    # 'Dashboard_M8_Alt'!AG40
    value = 0
    formula = "=AG$32*$D23"
    @eval_fn
    def AG40():
        ag32_1 = Dashboard_M8_Alt.AG32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(ag32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH40():
    # 'Dashboard_M8_Alt'!AH40
    value = 0
    formula = "=AH$32*$D23"
    @eval_fn
    def AH40():
        ah32_1 = Dashboard_M8_Alt.AH32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(ah32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI40():
    # 'Dashboard_M8_Alt'!AI40
    value = 0
    formula = "=AI$32*$D23"
    @eval_fn
    def AI40():
        ai32_1 = Dashboard_M8_Alt.AI32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(ai32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ40():
    # 'Dashboard_M8_Alt'!AJ40
    value = 0
    formula = "=AJ$32*$D23"
    @eval_fn
    def AJ40():
        aj32_1 = Dashboard_M8_Alt.AJ32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(aj32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK40():
    # 'Dashboard_M8_Alt'!AK40
    value = 0
    formula = "=AK$32*$D23"
    @eval_fn
    def AK40():
        ak32_1 = Dashboard_M8_Alt.AK32()
        d23_1 = Dashboard_M8_Alt.D23()
        var_1 = mult(ak32_1, d23_1)
        return var_1

@register(Dashboard_M8_Alt)
class A42():
    # 'Dashboard_M8_Alt'!A42
    value = "Variable FP (y,f): Fuel Price by Year and Fuel"

@register(Dashboard_M8_Alt)
class B44():
    # 'Dashboard_M8_Alt'!B44
    value = "Diesel"

@register(Dashboard_M8_Alt)
class C44():
    # 'Dashboard_M8_Alt'!C44
    value = "$/million Btu"

@register(Dashboard_M8_Alt)
class I44():
    # 'Dashboard_M8_Alt'!I44
    value = 5.72
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,I$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def I44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        i24_1 = Dashboard_M8_Alt.I24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, i24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class J44():
    # 'Dashboard_M8_Alt'!J44
    value = 7.49
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,J$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def J44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        j24_1 = Dashboard_M8_Alt.J24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, j24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class K44():
    # 'Dashboard_M8_Alt'!K44
    value = 8.97
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,K$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def K44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        k24_1 = Dashboard_M8_Alt.K24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, k24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class L44():
    # 'Dashboard_M8_Alt'!L44
    value = 10.26
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,L$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def L44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        l24_1 = Dashboard_M8_Alt.L24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, l24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class M44():
    # 'Dashboard_M8_Alt'!M44
    value = 15.42
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,M$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def M44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        m24_1 = Dashboard_M8_Alt.M24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, m24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class N44():
    # 'Dashboard_M8_Alt'!N44
    value = 16.19
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,N$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def N44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        n24_1 = Dashboard_M8_Alt.N24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, n24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class O44():
    # 'Dashboard_M8_Alt'!O44
    value = 22.86
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,O$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def O44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        o24_1 = Dashboard_M8_Alt.O24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, o24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class P44():
    # 'Dashboard_M8_Alt'!P44
    value = 13.73
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,P$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def P44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        p24_1 = Dashboard_M8_Alt.P24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, p24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Q44():
    # 'Dashboard_M8_Alt'!Q44
    value = 17.45
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Q$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def Q44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        q24_1 = Dashboard_M8_Alt.Q24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, q24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class R44():
    # 'Dashboard_M8_Alt'!R44
    value = 23.57
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,R$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def R44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        r24_1 = Dashboard_M8_Alt.R24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, r24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class S44():
    # 'Dashboard_M8_Alt'!S44
    value = 24.87
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,S$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def S44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        s24_1 = Dashboard_M8_Alt.S24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, s24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class T44():
    # 'Dashboard_M8_Alt'!T44
    value = 23.77
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,T$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def T44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        t24_1 = Dashboard_M8_Alt.T24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, t24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class U44():
    # 'Dashboard_M8_Alt'!U44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,U$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def U44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        u24_1 = Dashboard_M8_Alt.U24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, u24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class V44():
    # 'Dashboard_M8_Alt'!V44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,V$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def V44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        v24_1 = Dashboard_M8_Alt.V24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, v24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class W44():
    # 'Dashboard_M8_Alt'!W44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,W$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def W44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        w24_1 = Dashboard_M8_Alt.W24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, w24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class X44():
    # 'Dashboard_M8_Alt'!X44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,X$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def X44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        x24_1 = Dashboard_M8_Alt.X24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, x24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Y44():
    # 'Dashboard_M8_Alt'!Y44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Y$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def Y44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        y24_1 = Dashboard_M8_Alt.Y24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, y24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Z44():
    # 'Dashboard_M8_Alt'!Z44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Z$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def Z44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        z24_1 = Dashboard_M8_Alt.Z24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, z24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AA44():
    # 'Dashboard_M8_Alt'!AA44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AA$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AA44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aa24_1 = Dashboard_M8_Alt.AA24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, aa24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AB44():
    # 'Dashboard_M8_Alt'!AB44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AB$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AB44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ab24_1 = Dashboard_M8_Alt.AB24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, ab24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AC44():
    # 'Dashboard_M8_Alt'!AC44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AC$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AC44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ac24_1 = Dashboard_M8_Alt.AC24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, ac24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AD44():
    # 'Dashboard_M8_Alt'!AD44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AD$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AD44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ad24_1 = Dashboard_M8_Alt.AD24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, ad24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AE44():
    # 'Dashboard_M8_Alt'!AE44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AE$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AE44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ae24_1 = Dashboard_M8_Alt.AE24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, ae24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AF44():
    # 'Dashboard_M8_Alt'!AF44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AF$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AF44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        af24_1 = Dashboard_M8_Alt.AF24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, af24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AG44():
    # 'Dashboard_M8_Alt'!AG44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AG$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AG44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ag24_1 = Dashboard_M8_Alt.AG24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, ag24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AH44():
    # 'Dashboard_M8_Alt'!AH44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AH$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AH44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ah24_1 = Dashboard_M8_Alt.AH24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, ah24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AI44():
    # 'Dashboard_M8_Alt'!AI44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AI$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AI44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ai24_1 = Dashboard_M8_Alt.AI24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, ai24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AJ44():
    # 'Dashboard_M8_Alt'!AJ44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AJ$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AJ44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aj24_1 = Dashboard_M8_Alt.AJ24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, aj24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AK44():
    # 'Dashboard_M8_Alt'!AK44
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AK$24,'EIA Expenditures'!$E$41:$CD$41)"
    @eval_fn
    def AK44():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ak24_1 = Dashboard_M8_Alt.AK24()
        range_2 = EIA_Expenditures(5, 41, 82, 41)
        var_1 = SUMIF(range_1, ak24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class B45():
    # 'Dashboard_M8_Alt'!B45
    value = "Fuel Oil"

@register(Dashboard_M8_Alt)
class C45():
    # 'Dashboard_M8_Alt'!C45
    value = "$/million Btu"

@register(Dashboard_M8_Alt)
class I45():
    # 'Dashboard_M8_Alt'!I45
    value = 4.87
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,I$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def I45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        i24_1 = Dashboard_M8_Alt.I24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, i24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class J45():
    # 'Dashboard_M8_Alt'!J45
    value = 4.87
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,J$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def J45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        j24_1 = Dashboard_M8_Alt.J24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, j24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class K45():
    # 'Dashboard_M8_Alt'!K45
    value = 5.04
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,K$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def K45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        k24_1 = Dashboard_M8_Alt.K24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, k24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class L45():
    # 'Dashboard_M8_Alt'!L45
    value = 8.69
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,L$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def L45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        l24_1 = Dashboard_M8_Alt.L24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, l24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class M45():
    # 'Dashboard_M8_Alt'!M45
    value = 9.89
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,M$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def M45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        m24_1 = Dashboard_M8_Alt.M24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, m24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class N45():
    # 'Dashboard_M8_Alt'!N45
    value = 10.94
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,N$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def N45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        n24_1 = Dashboard_M8_Alt.N24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, n24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class O45():
    # 'Dashboard_M8_Alt'!O45
    value = 16.21
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,O$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def O45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        o24_1 = Dashboard_M8_Alt.O24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, o24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class P45():
    # 'Dashboard_M8_Alt'!P45
    value = 9.43
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,P$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def P45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        p24_1 = Dashboard_M8_Alt.P24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, p24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Q45():
    # 'Dashboard_M8_Alt'!Q45
    value = 13.49
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Q$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def Q45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        q24_1 = Dashboard_M8_Alt.Q24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, q24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class R45():
    # 'Dashboard_M8_Alt'!R45
    value = 19.52
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,R$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def R45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        r24_1 = Dashboard_M8_Alt.R24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, r24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class S45():
    # 'Dashboard_M8_Alt'!S45
    value = 21.39
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,S$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def S45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        s24_1 = Dashboard_M8_Alt.S24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, s24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class T45():
    # 'Dashboard_M8_Alt'!T45
    value = 20.18
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,T$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def T45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        t24_1 = Dashboard_M8_Alt.T24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, t24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class U45():
    # 'Dashboard_M8_Alt'!U45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,U$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def U45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        u24_1 = Dashboard_M8_Alt.U24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, u24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class V45():
    # 'Dashboard_M8_Alt'!V45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,V$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def V45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        v24_1 = Dashboard_M8_Alt.V24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, v24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class W45():
    # 'Dashboard_M8_Alt'!W45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,W$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def W45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        w24_1 = Dashboard_M8_Alt.W24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, w24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class X45():
    # 'Dashboard_M8_Alt'!X45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,X$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def X45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        x24_1 = Dashboard_M8_Alt.X24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, x24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Y45():
    # 'Dashboard_M8_Alt'!Y45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Y$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def Y45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        y24_1 = Dashboard_M8_Alt.Y24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, y24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Z45():
    # 'Dashboard_M8_Alt'!Z45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Z$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def Z45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        z24_1 = Dashboard_M8_Alt.Z24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, z24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AA45():
    # 'Dashboard_M8_Alt'!AA45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AA$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AA45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aa24_1 = Dashboard_M8_Alt.AA24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, aa24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AB45():
    # 'Dashboard_M8_Alt'!AB45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AB$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AB45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ab24_1 = Dashboard_M8_Alt.AB24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, ab24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AC45():
    # 'Dashboard_M8_Alt'!AC45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AC$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AC45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ac24_1 = Dashboard_M8_Alt.AC24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, ac24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AD45():
    # 'Dashboard_M8_Alt'!AD45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AD$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AD45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ad24_1 = Dashboard_M8_Alt.AD24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, ad24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AE45():
    # 'Dashboard_M8_Alt'!AE45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AE$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AE45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ae24_1 = Dashboard_M8_Alt.AE24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, ae24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AF45():
    # 'Dashboard_M8_Alt'!AF45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AF$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AF45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        af24_1 = Dashboard_M8_Alt.AF24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, af24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AG45():
    # 'Dashboard_M8_Alt'!AG45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AG$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AG45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ag24_1 = Dashboard_M8_Alt.AG24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, ag24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AH45():
    # 'Dashboard_M8_Alt'!AH45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AH$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AH45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ah24_1 = Dashboard_M8_Alt.AH24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, ah24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AI45():
    # 'Dashboard_M8_Alt'!AI45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AI$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AI45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ai24_1 = Dashboard_M8_Alt.AI24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, ai24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AJ45():
    # 'Dashboard_M8_Alt'!AJ45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AJ$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AJ45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aj24_1 = Dashboard_M8_Alt.AJ24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, aj24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AK45():
    # 'Dashboard_M8_Alt'!AK45
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AK$24,'EIA Expenditures'!$E$206:$CD$206)"
    @eval_fn
    def AK45():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ak24_1 = Dashboard_M8_Alt.AK24()
        range_2 = EIA_Expenditures(5, 206, 82, 206)
        var_1 = SUMIF(range_1, ak24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class B46():
    # 'Dashboard_M8_Alt'!B46
    value = "SNG"

@register(Dashboard_M8_Alt)
class C46():
    # 'Dashboard_M8_Alt'!C46
    value = "$/million Btu"

@register(Dashboard_M8_Alt)
class I46():
    # 'Dashboard_M8_Alt'!I46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,I$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def I46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        i24_1 = Dashboard_M8_Alt.I24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, i24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class J46():
    # 'Dashboard_M8_Alt'!J46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,J$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def J46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        j24_1 = Dashboard_M8_Alt.J24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, j24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class K46():
    # 'Dashboard_M8_Alt'!K46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,K$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def K46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        k24_1 = Dashboard_M8_Alt.K24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, k24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class L46():
    # 'Dashboard_M8_Alt'!L46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,L$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def L46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        l24_1 = Dashboard_M8_Alt.L24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, l24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class M46():
    # 'Dashboard_M8_Alt'!M46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,M$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def M46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        m24_1 = Dashboard_M8_Alt.M24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, m24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class N46():
    # 'Dashboard_M8_Alt'!N46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,N$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def N46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        n24_1 = Dashboard_M8_Alt.N24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, n24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class O46():
    # 'Dashboard_M8_Alt'!O46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,O$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def O46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        o24_1 = Dashboard_M8_Alt.O24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, o24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class P46():
    # 'Dashboard_M8_Alt'!P46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,P$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def P46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        p24_1 = Dashboard_M8_Alt.P24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, p24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Q46():
    # 'Dashboard_M8_Alt'!Q46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Q$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def Q46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        q24_1 = Dashboard_M8_Alt.Q24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, q24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class R46():
    # 'Dashboard_M8_Alt'!R46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,R$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def R46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        r24_1 = Dashboard_M8_Alt.R24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, r24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class S46():
    # 'Dashboard_M8_Alt'!S46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,S$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def S46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        s24_1 = Dashboard_M8_Alt.S24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, s24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class T46():
    # 'Dashboard_M8_Alt'!T46
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,T$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def T46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        t24_1 = Dashboard_M8_Alt.T24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, t24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class U46():
    # 'Dashboard_M8_Alt'!U46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,U$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def U46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        u24_1 = Dashboard_M8_Alt.U24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, u24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class V46():
    # 'Dashboard_M8_Alt'!V46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,V$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def V46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        v24_1 = Dashboard_M8_Alt.V24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, v24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class W46():
    # 'Dashboard_M8_Alt'!W46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,W$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def W46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        w24_1 = Dashboard_M8_Alt.W24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, w24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class X46():
    # 'Dashboard_M8_Alt'!X46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,X$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def X46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        x24_1 = Dashboard_M8_Alt.X24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, x24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Y46():
    # 'Dashboard_M8_Alt'!Y46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Y$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def Y46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        y24_1 = Dashboard_M8_Alt.Y24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, y24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Z46():
    # 'Dashboard_M8_Alt'!Z46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Z$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def Z46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        z24_1 = Dashboard_M8_Alt.Z24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, z24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AA46():
    # 'Dashboard_M8_Alt'!AA46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AA$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AA46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aa24_1 = Dashboard_M8_Alt.AA24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, aa24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AB46():
    # 'Dashboard_M8_Alt'!AB46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AB$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AB46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ab24_1 = Dashboard_M8_Alt.AB24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, ab24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AC46():
    # 'Dashboard_M8_Alt'!AC46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AC$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AC46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ac24_1 = Dashboard_M8_Alt.AC24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, ac24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AD46():
    # 'Dashboard_M8_Alt'!AD46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AD$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AD46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ad24_1 = Dashboard_M8_Alt.AD24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, ad24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AE46():
    # 'Dashboard_M8_Alt'!AE46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AE$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AE46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ae24_1 = Dashboard_M8_Alt.AE24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, ae24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AF46():
    # 'Dashboard_M8_Alt'!AF46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AF$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AF46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        af24_1 = Dashboard_M8_Alt.AF24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, af24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AG46():
    # 'Dashboard_M8_Alt'!AG46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AG$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AG46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ag24_1 = Dashboard_M8_Alt.AG24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, ag24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AH46():
    # 'Dashboard_M8_Alt'!AH46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AH$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AH46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ah24_1 = Dashboard_M8_Alt.AH24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, ah24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AI46():
    # 'Dashboard_M8_Alt'!AI46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AI$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AI46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ai24_1 = Dashboard_M8_Alt.AI24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, ai24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AJ46():
    # 'Dashboard_M8_Alt'!AJ46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AJ$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AJ46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aj24_1 = Dashboard_M8_Alt.AJ24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, aj24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AK46():
    # 'Dashboard_M8_Alt'!AK46
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AK$24,'EIA Expenditures'!$E$138:$CD$138)"
    @eval_fn
    def AK46():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ak24_1 = Dashboard_M8_Alt.AK24()
        range_2 = EIA_Expenditures(5, 138, 82, 138)
        var_1 = SUMIF(range_1, ak24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class B47():
    # 'Dashboard_M8_Alt'!B47
    value = "Coal"

@register(Dashboard_M8_Alt)
class C47():
    # 'Dashboard_M8_Alt'!C47
    value = "$/million Btu"

@register(Dashboard_M8_Alt)
class I47():
    # 'Dashboard_M8_Alt'!I47
    value = 1.6
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,I$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def I47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        i24_1 = Dashboard_M8_Alt.I24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, i24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class J47():
    # 'Dashboard_M8_Alt'!J47
    value = 2.96
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,J$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def J47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        j24_1 = Dashboard_M8_Alt.J24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, j24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class K47():
    # 'Dashboard_M8_Alt'!K47
    value = 1.88
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,K$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def K47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        k24_1 = Dashboard_M8_Alt.K24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, k24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class L47():
    # 'Dashboard_M8_Alt'!L47
    value = 1.43
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,L$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def L47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        l24_1 = Dashboard_M8_Alt.L24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, l24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class M47():
    # 'Dashboard_M8_Alt'!M47
    value = 1.68
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,M$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def M47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        m24_1 = Dashboard_M8_Alt.M24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, m24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class N47():
    # 'Dashboard_M8_Alt'!N47
    value = 1.85
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,N$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def N47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        n24_1 = Dashboard_M8_Alt.N24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, n24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class O47():
    # 'Dashboard_M8_Alt'!O47
    value = 2.19
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,O$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def O47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        o24_1 = Dashboard_M8_Alt.O24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, o24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class P47():
    # 'Dashboard_M8_Alt'!P47
    value = 2.24
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,P$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def P47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        p24_1 = Dashboard_M8_Alt.P24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, p24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Q47():
    # 'Dashboard_M8_Alt'!Q47
    value = 2.22
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Q$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def Q47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        q24_1 = Dashboard_M8_Alt.Q24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, q24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class R47():
    # 'Dashboard_M8_Alt'!R47
    value = 1.66
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,R$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def R47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        r24_1 = Dashboard_M8_Alt.R24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, r24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class S47():
    # 'Dashboard_M8_Alt'!S47
    value = 1.89
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,S$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def S47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        s24_1 = Dashboard_M8_Alt.S24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, s24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class T47():
    # 'Dashboard_M8_Alt'!T47
    value = 1.96
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,T$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def T47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        t24_1 = Dashboard_M8_Alt.T24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, t24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class U47():
    # 'Dashboard_M8_Alt'!U47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,U$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def U47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        u24_1 = Dashboard_M8_Alt.U24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, u24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class V47():
    # 'Dashboard_M8_Alt'!V47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,V$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def V47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        v24_1 = Dashboard_M8_Alt.V24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, v24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class W47():
    # 'Dashboard_M8_Alt'!W47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,W$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def W47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        w24_1 = Dashboard_M8_Alt.W24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, w24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class X47():
    # 'Dashboard_M8_Alt'!X47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,X$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def X47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        x24_1 = Dashboard_M8_Alt.X24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, x24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Y47():
    # 'Dashboard_M8_Alt'!Y47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Y$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def Y47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        y24_1 = Dashboard_M8_Alt.Y24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, y24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class Z47():
    # 'Dashboard_M8_Alt'!Z47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Z$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def Z47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        z24_1 = Dashboard_M8_Alt.Z24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, z24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AA47():
    # 'Dashboard_M8_Alt'!AA47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AA$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AA47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aa24_1 = Dashboard_M8_Alt.AA24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, aa24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AB47():
    # 'Dashboard_M8_Alt'!AB47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AB$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AB47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ab24_1 = Dashboard_M8_Alt.AB24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, ab24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AC47():
    # 'Dashboard_M8_Alt'!AC47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AC$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AC47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ac24_1 = Dashboard_M8_Alt.AC24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, ac24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AD47():
    # 'Dashboard_M8_Alt'!AD47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AD$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AD47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ad24_1 = Dashboard_M8_Alt.AD24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, ad24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AE47():
    # 'Dashboard_M8_Alt'!AE47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AE$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AE47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ae24_1 = Dashboard_M8_Alt.AE24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, ae24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AF47():
    # 'Dashboard_M8_Alt'!AF47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AF$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AF47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        af24_1 = Dashboard_M8_Alt.AF24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, af24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AG47():
    # 'Dashboard_M8_Alt'!AG47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AG$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AG47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ag24_1 = Dashboard_M8_Alt.AG24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, ag24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AH47():
    # 'Dashboard_M8_Alt'!AH47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AH$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AH47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ah24_1 = Dashboard_M8_Alt.AH24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, ah24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AI47():
    # 'Dashboard_M8_Alt'!AI47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AI$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AI47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ai24_1 = Dashboard_M8_Alt.AI24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, ai24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AJ47():
    # 'Dashboard_M8_Alt'!AJ47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AJ$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AJ47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aj24_1 = Dashboard_M8_Alt.AJ24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, aj24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class AK47():
    # 'Dashboard_M8_Alt'!AK47
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AK$24,'EIA Expenditures'!$E$19:$CD$19)"
    @eval_fn
    def AK47():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ak24_1 = Dashboard_M8_Alt.AK24()
        range_2 = EIA_Expenditures(5, 19, 82, 19)
        var_1 = SUMIF(range_1, ak24_1, range_2)
        return var_1

@register(Dashboard_M8_Alt)
class B48():
    # 'Dashboard_M8_Alt'!B48
    value = "All Fuels"

@register(Dashboard_M8_Alt)
class C48():
    # 'Dashboard_M8_Alt'!C48
    value = "$/million Btu"

@register(Dashboard_M8_Alt)
class I48():
    # 'Dashboard_M8_Alt'!I48
    value = 12.19
    formula = "=SUM(I44:I47)"
    @eval_fn
    def I48():
        range_1 = Dashboard_M8_Alt(9, 44, 9, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class J48():
    # 'Dashboard_M8_Alt'!J48
    value = 15.32
    formula = "=SUM(J44:J47)"
    @eval_fn
    def J48():
        range_1 = Dashboard_M8_Alt(10, 44, 10, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class K48():
    # 'Dashboard_M8_Alt'!K48
    value = 15.89
    formula = "=SUM(K44:K47)"
    @eval_fn
    def K48():
        range_1 = Dashboard_M8_Alt(11, 44, 11, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class L48():
    # 'Dashboard_M8_Alt'!L48
    value = 20.38
    formula = "=SUM(L44:L47)"
    @eval_fn
    def L48():
        range_1 = Dashboard_M8_Alt(12, 44, 12, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class M48():
    # 'Dashboard_M8_Alt'!M48
    value = 26.99
    formula = "=SUM(M44:M47)"
    @eval_fn
    def M48():
        range_1 = Dashboard_M8_Alt(13, 44, 13, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class N48():
    # 'Dashboard_M8_Alt'!N48
    value = 28.98
    formula = "=SUM(N44:N47)"
    @eval_fn
    def N48():
        range_1 = Dashboard_M8_Alt(14, 44, 14, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class O48():
    # 'Dashboard_M8_Alt'!O48
    value = 41.26
    formula = "=SUM(O44:O47)"
    @eval_fn
    def O48():
        range_1 = Dashboard_M8_Alt(15, 44, 15, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class P48():
    # 'Dashboard_M8_Alt'!P48
    value = 25.4
    formula = "=SUM(P44:P47)"
    @eval_fn
    def P48():
        range_1 = Dashboard_M8_Alt(16, 44, 16, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q48():
    # 'Dashboard_M8_Alt'!Q48
    value = 33.16
    formula = "=SUM(Q44:Q47)"
    @eval_fn
    def Q48():
        range_1 = Dashboard_M8_Alt(17, 44, 17, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class R48():
    # 'Dashboard_M8_Alt'!R48
    value = 44.75
    formula = "=SUM(R44:R47)"
    @eval_fn
    def R48():
        range_1 = Dashboard_M8_Alt(18, 44, 18, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class S48():
    # 'Dashboard_M8_Alt'!S48
    value = 48.15
    formula = "=SUM(S44:S47)"
    @eval_fn
    def S48():
        range_1 = Dashboard_M8_Alt(19, 44, 19, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class T48():
    # 'Dashboard_M8_Alt'!T48
    value = 45.91
    formula = "=SUM(T44:T47)"
    @eval_fn
    def T48():
        range_1 = Dashboard_M8_Alt(20, 44, 20, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class U48():
    # 'Dashboard_M8_Alt'!U48
    value = "#N/A"
    formula = "=SUM(U44:U47)"
    @eval_fn
    def U48():
        range_1 = Dashboard_M8_Alt(21, 44, 21, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class V48():
    # 'Dashboard_M8_Alt'!V48
    value = "#N/A"
    formula = "=SUM(V44:V47)"
    @eval_fn
    def V48():
        range_1 = Dashboard_M8_Alt(22, 44, 22, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class W48():
    # 'Dashboard_M8_Alt'!W48
    value = "#N/A"
    formula = "=SUM(W44:W47)"
    @eval_fn
    def W48():
        range_1 = Dashboard_M8_Alt(23, 44, 23, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class X48():
    # 'Dashboard_M8_Alt'!X48
    value = "#N/A"
    formula = "=SUM(X44:X47)"
    @eval_fn
    def X48():
        range_1 = Dashboard_M8_Alt(24, 44, 24, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y48():
    # 'Dashboard_M8_Alt'!Y48
    value = "#N/A"
    formula = "=SUM(Y44:Y47)"
    @eval_fn
    def Y48():
        range_1 = Dashboard_M8_Alt(25, 44, 25, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z48():
    # 'Dashboard_M8_Alt'!Z48
    value = "#N/A"
    formula = "=SUM(Z44:Z47)"
    @eval_fn
    def Z48():
        range_1 = Dashboard_M8_Alt(26, 44, 26, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA48():
    # 'Dashboard_M8_Alt'!AA48
    value = "#N/A"
    formula = "=SUM(AA44:AA47)"
    @eval_fn
    def AA48():
        range_1 = Dashboard_M8_Alt(27, 44, 27, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB48():
    # 'Dashboard_M8_Alt'!AB48
    value = "#N/A"
    formula = "=SUM(AB44:AB47)"
    @eval_fn
    def AB48():
        range_1 = Dashboard_M8_Alt(28, 44, 28, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC48():
    # 'Dashboard_M8_Alt'!AC48
    value = "#N/A"
    formula = "=SUM(AC44:AC47)"
    @eval_fn
    def AC48():
        range_1 = Dashboard_M8_Alt(29, 44, 29, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD48():
    # 'Dashboard_M8_Alt'!AD48
    value = "#N/A"
    formula = "=SUM(AD44:AD47)"
    @eval_fn
    def AD48():
        range_1 = Dashboard_M8_Alt(30, 44, 30, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE48():
    # 'Dashboard_M8_Alt'!AE48
    value = "#N/A"
    formula = "=SUM(AE44:AE47)"
    @eval_fn
    def AE48():
        range_1 = Dashboard_M8_Alt(31, 44, 31, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF48():
    # 'Dashboard_M8_Alt'!AF48
    value = "#N/A"
    formula = "=SUM(AF44:AF47)"
    @eval_fn
    def AF48():
        range_1 = Dashboard_M8_Alt(32, 44, 32, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG48():
    # 'Dashboard_M8_Alt'!AG48
    value = "#N/A"
    formula = "=SUM(AG44:AG47)"
    @eval_fn
    def AG48():
        range_1 = Dashboard_M8_Alt(33, 44, 33, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH48():
    # 'Dashboard_M8_Alt'!AH48
    value = "#N/A"
    formula = "=SUM(AH44:AH47)"
    @eval_fn
    def AH48():
        range_1 = Dashboard_M8_Alt(34, 44, 34, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI48():
    # 'Dashboard_M8_Alt'!AI48
    value = "#N/A"
    formula = "=SUM(AI44:AI47)"
    @eval_fn
    def AI48():
        range_1 = Dashboard_M8_Alt(35, 44, 35, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ48():
    # 'Dashboard_M8_Alt'!AJ48
    value = "#N/A"
    formula = "=SUM(AJ44:AJ47)"
    @eval_fn
    def AJ48():
        range_1 = Dashboard_M8_Alt(36, 44, 36, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK48():
    # 'Dashboard_M8_Alt'!AK48
    value = "#N/A"
    formula = "=SUM(AK44:AK47)"
    @eval_fn
    def AK48():
        range_1 = Dashboard_M8_Alt(37, 44, 37, 47)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class A50():
    # 'Dashboard_M8_Alt'!A50
    value = "Variabl HFE(2005,y,p,f): Hyopthetical Fuel Expenditure for Power Sector by Year and Fuel"
    formula = '''="Variabl HFE("&$D$4&",y,p,f): Hyopthetical Fuel Expenditure for Power Sector by Year and Fuel"'''
    @eval_fn
    def A50():
        d4_1 = Dashboard_M8_Alt.D4()
        var_1 = concat("Variabl HFE(", d4_1)
        var_2 = concat(var_1, ",y,p,f): Hyopthetical Fuel Expenditure for Power Sector by Year and Fuel")
        return var_2

@register(Dashboard_M8_Alt)
class B52():
    # 'Dashboard_M8_Alt'!B52
    value = "Diesel"

@register(Dashboard_M8_Alt)
class C52():
    # 'Dashboard_M8_Alt'!C52
    value = "Million Dollars"

@register(Dashboard_M8_Alt)
class I52():
    # 'Dashboard_M8_Alt'!I52
    value = 82.8420379292
    formula = "=I36*I44/1000000"
    @eval_fn
    def I52():
        i36_1 = Dashboard_M8_Alt.I36()
        i44_1 = Dashboard_M8_Alt.I44()
        var_1 = mult(i36_1, i44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class J52():
    # 'Dashboard_M8_Alt'!J52
    value = 109.247788481
    formula = "=J36*J44/1000000"
    @eval_fn
    def J52():
        j36_1 = Dashboard_M8_Alt.J36()
        j44_1 = Dashboard_M8_Alt.J44()
        var_1 = mult(j36_1, j44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class K52():
    # 'Dashboard_M8_Alt'!K52
    value = 134.415508384
    formula = "=K36*K44/1000000"
    @eval_fn
    def K52():
        k36_1 = Dashboard_M8_Alt.K36()
        k44_1 = Dashboard_M8_Alt.K44()
        var_1 = mult(k36_1, k44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class L52():
    # 'Dashboard_M8_Alt'!L52
    value = 161.117440821
    formula = "=L36*L44/1000000"
    @eval_fn
    def L52():
        l36_1 = Dashboard_M8_Alt.L36()
        l44_1 = Dashboard_M8_Alt.L44()
        var_1 = mult(l36_1, l44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class M52():
    # 'Dashboard_M8_Alt'!M52
    value = 240.723434312
    formula = "=M36*M44/1000000"
    @eval_fn
    def M52():
        m36_1 = Dashboard_M8_Alt.M36()
        m44_1 = Dashboard_M8_Alt.M44()
        var_1 = mult(m36_1, m44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class N52():
    # 'Dashboard_M8_Alt'!N52
    value = 254.198457127
    formula = "=N36*N44/1000000"
    @eval_fn
    def N52():
        n36_1 = Dashboard_M8_Alt.N36()
        n44_1 = Dashboard_M8_Alt.N44()
        var_1 = mult(n36_1, n44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class O52():
    # 'Dashboard_M8_Alt'!O52
    value = 355.14117311
    formula = "=O36*O44/1000000"
    @eval_fn
    def O52():
        o36_1 = Dashboard_M8_Alt.O36()
        o44_1 = Dashboard_M8_Alt.O44()
        var_1 = mult(o36_1, o44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class P52():
    # 'Dashboard_M8_Alt'!P52
    value = 209.284881703
    formula = "=P36*P44/1000000"
    @eval_fn
    def P52():
        p36_1 = Dashboard_M8_Alt.P36()
        p44_1 = Dashboard_M8_Alt.P44()
        var_1 = mult(p36_1, p44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Q52():
    # 'Dashboard_M8_Alt'!Q52
    value = 266.227049389
    formula = "=Q36*Q44/1000000"
    @eval_fn
    def Q52():
        q36_1 = Dashboard_M8_Alt.Q36()
        q44_1 = Dashboard_M8_Alt.Q44()
        var_1 = mult(q36_1, q44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class R52():
    # 'Dashboard_M8_Alt'!R52
    value = 353.24857282
    formula = "=R36*R44/1000000"
    @eval_fn
    def R52():
        r36_1 = Dashboard_M8_Alt.R36()
        r44_1 = Dashboard_M8_Alt.R44()
        var_1 = mult(r36_1, r44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class S52():
    # 'Dashboard_M8_Alt'!S52
    value = 361.762412197
    formula = "=S36*S44/1000000"
    @eval_fn
    def S52():
        s36_1 = Dashboard_M8_Alt.S36()
        s44_1 = Dashboard_M8_Alt.S44()
        var_1 = mult(s36_1, s44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class T52():
    # 'Dashboard_M8_Alt'!T52
    value = 330.894293419
    formula = "=T36*T44/1000000"
    @eval_fn
    def T52():
        t36_1 = Dashboard_M8_Alt.T36()
        t44_1 = Dashboard_M8_Alt.T44()
        var_1 = mult(t36_1, t44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class U52():
    # 'Dashboard_M8_Alt'!U52
    value = "#N/A"
    formula = "=U36*U44/1000000"
    @eval_fn
    def U52():
        u36_1 = Dashboard_M8_Alt.U36()
        u44_1 = Dashboard_M8_Alt.U44()
        var_1 = mult(u36_1, u44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class V52():
    # 'Dashboard_M8_Alt'!V52
    value = "#N/A"
    formula = "=V36*V44/1000000"
    @eval_fn
    def V52():
        v36_1 = Dashboard_M8_Alt.V36()
        v44_1 = Dashboard_M8_Alt.V44()
        var_1 = mult(v36_1, v44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class W52():
    # 'Dashboard_M8_Alt'!W52
    value = "#N/A"
    formula = "=W36*W44/1000000"
    @eval_fn
    def W52():
        w36_1 = Dashboard_M8_Alt.W36()
        w44_1 = Dashboard_M8_Alt.W44()
        var_1 = mult(w36_1, w44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class X52():
    # 'Dashboard_M8_Alt'!X52
    value = "#N/A"
    formula = "=X36*X44/1000000"
    @eval_fn
    def X52():
        x36_1 = Dashboard_M8_Alt.X36()
        x44_1 = Dashboard_M8_Alt.X44()
        var_1 = mult(x36_1, x44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Y52():
    # 'Dashboard_M8_Alt'!Y52
    value = "#N/A"
    formula = "=Y36*Y44/1000000"
    @eval_fn
    def Y52():
        y36_1 = Dashboard_M8_Alt.Y36()
        y44_1 = Dashboard_M8_Alt.Y44()
        var_1 = mult(y36_1, y44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Z52():
    # 'Dashboard_M8_Alt'!Z52
    value = "#N/A"
    formula = "=Z36*Z44/1000000"
    @eval_fn
    def Z52():
        z36_1 = Dashboard_M8_Alt.Z36()
        z44_1 = Dashboard_M8_Alt.Z44()
        var_1 = mult(z36_1, z44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AA52():
    # 'Dashboard_M8_Alt'!AA52
    value = "#N/A"
    formula = "=AA36*AA44/1000000"
    @eval_fn
    def AA52():
        aa36_1 = Dashboard_M8_Alt.AA36()
        aa44_1 = Dashboard_M8_Alt.AA44()
        var_1 = mult(aa36_1, aa44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AB52():
    # 'Dashboard_M8_Alt'!AB52
    value = "#N/A"
    formula = "=AB36*AB44/1000000"
    @eval_fn
    def AB52():
        ab36_1 = Dashboard_M8_Alt.AB36()
        ab44_1 = Dashboard_M8_Alt.AB44()
        var_1 = mult(ab36_1, ab44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AC52():
    # 'Dashboard_M8_Alt'!AC52
    value = "#N/A"
    formula = "=AC36*AC44/1000000"
    @eval_fn
    def AC52():
        ac36_1 = Dashboard_M8_Alt.AC36()
        ac44_1 = Dashboard_M8_Alt.AC44()
        var_1 = mult(ac36_1, ac44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AD52():
    # 'Dashboard_M8_Alt'!AD52
    value = "#N/A"
    formula = "=AD36*AD44/1000000"
    @eval_fn
    def AD52():
        ad36_1 = Dashboard_M8_Alt.AD36()
        ad44_1 = Dashboard_M8_Alt.AD44()
        var_1 = mult(ad36_1, ad44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AE52():
    # 'Dashboard_M8_Alt'!AE52
    value = "#N/A"
    formula = "=AE36*AE44/1000000"
    @eval_fn
    def AE52():
        ae36_1 = Dashboard_M8_Alt.AE36()
        ae44_1 = Dashboard_M8_Alt.AE44()
        var_1 = mult(ae36_1, ae44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AF52():
    # 'Dashboard_M8_Alt'!AF52
    value = "#N/A"
    formula = "=AF36*AF44/1000000"
    @eval_fn
    def AF52():
        af36_1 = Dashboard_M8_Alt.AF36()
        af44_1 = Dashboard_M8_Alt.AF44()
        var_1 = mult(af36_1, af44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AG52():
    # 'Dashboard_M8_Alt'!AG52
    value = "#N/A"
    formula = "=AG36*AG44/1000000"
    @eval_fn
    def AG52():
        ag36_1 = Dashboard_M8_Alt.AG36()
        ag44_1 = Dashboard_M8_Alt.AG44()
        var_1 = mult(ag36_1, ag44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AH52():
    # 'Dashboard_M8_Alt'!AH52
    value = "#N/A"
    formula = "=AH36*AH44/1000000"
    @eval_fn
    def AH52():
        ah36_1 = Dashboard_M8_Alt.AH36()
        ah44_1 = Dashboard_M8_Alt.AH44()
        var_1 = mult(ah36_1, ah44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AI52():
    # 'Dashboard_M8_Alt'!AI52
    value = "#N/A"
    formula = "=AI36*AI44/1000000"
    @eval_fn
    def AI52():
        ai36_1 = Dashboard_M8_Alt.AI36()
        ai44_1 = Dashboard_M8_Alt.AI44()
        var_1 = mult(ai36_1, ai44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ52():
    # 'Dashboard_M8_Alt'!AJ52
    value = "#N/A"
    formula = "=AJ36*AJ44/1000000"
    @eval_fn
    def AJ52():
        aj36_1 = Dashboard_M8_Alt.AJ36()
        aj44_1 = Dashboard_M8_Alt.AJ44()
        var_1 = mult(aj36_1, aj44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AK52():
    # 'Dashboard_M8_Alt'!AK52
    value = "#N/A"
    formula = "=AK36*AK44/1000000"
    @eval_fn
    def AK52():
        ak36_1 = Dashboard_M8_Alt.AK36()
        ak44_1 = Dashboard_M8_Alt.AK44()
        var_1 = mult(ak36_1, ak44_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class B53():
    # 'Dashboard_M8_Alt'!B53
    value = "Fuel Oil"

@register(Dashboard_M8_Alt)
class C53():
    # 'Dashboard_M8_Alt'!C53
    value = "Million Dollars"

@register(Dashboard_M8_Alt)
class I53():
    # 'Dashboard_M8_Alt'!I53
    value = 333.002090812
    formula = "=I37*I45/1000000"
    @eval_fn
    def I53():
        i37_1 = Dashboard_M8_Alt.I37()
        i45_1 = Dashboard_M8_Alt.I45()
        var_1 = mult(i37_1, i45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class J53():
    # 'Dashboard_M8_Alt'!J53
    value = 335.369104769
    formula = "=J37*J45/1000000"
    @eval_fn
    def J53():
        j37_1 = Dashboard_M8_Alt.J37()
        j45_1 = Dashboard_M8_Alt.J45()
        var_1 = mult(j37_1, j45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class K53():
    # 'Dashboard_M8_Alt'!K53
    value = 356.574864773
    formula = "=K37*K45/1000000"
    @eval_fn
    def K53():
        k37_1 = Dashboard_M8_Alt.K37()
        k45_1 = Dashboard_M8_Alt.K45()
        var_1 = mult(k37_1, k45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class L53():
    # 'Dashboard_M8_Alt'!L53
    value = 644.285302726
    formula = "=L37*L45/1000000"
    @eval_fn
    def L53():
        l37_1 = Dashboard_M8_Alt.L37()
        l45_1 = Dashboard_M8_Alt.L45()
        var_1 = mult(l37_1, l45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class M53():
    # 'Dashboard_M8_Alt'!M53
    value = 728.942953974
    formula = "=M37*M45/1000000"
    @eval_fn
    def M53():
        m37_1 = Dashboard_M8_Alt.M37()
        m45_1 = Dashboard_M8_Alt.M45()
        var_1 = mult(m37_1, m45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class N53():
    # 'Dashboard_M8_Alt'!N53
    value = 810.973451834
    formula = "=N37*N45/1000000"
    @eval_fn
    def N53():
        n37_1 = Dashboard_M8_Alt.N37()
        n45_1 = Dashboard_M8_Alt.N45()
        var_1 = mult(n37_1, n45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class O53():
    # 'Dashboard_M8_Alt'!O53
    value = 1188.97046776
    formula = "=O37*O45/1000000"
    @eval_fn
    def O53():
        o37_1 = Dashboard_M8_Alt.O37()
        o45_1 = Dashboard_M8_Alt.O45()
        var_1 = mult(o37_1, o45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class P53():
    # 'Dashboard_M8_Alt'!P53
    value = 678.644394551
    formula = "=P37*P45/1000000"
    @eval_fn
    def P53():
        p37_1 = Dashboard_M8_Alt.P37()
        p45_1 = Dashboard_M8_Alt.P45()
        var_1 = mult(p37_1, p45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Q53():
    # 'Dashboard_M8_Alt'!Q53
    value = 971.699436918
    formula = "=Q37*Q45/1000000"
    @eval_fn
    def Q53():
        q37_1 = Dashboard_M8_Alt.Q37()
        q45_1 = Dashboard_M8_Alt.Q45()
        var_1 = mult(q37_1, q45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class R53():
    # 'Dashboard_M8_Alt'!R53
    value = 1381.22331471
    formula = "=R37*R45/1000000"
    @eval_fn
    def R53():
        r37_1 = Dashboard_M8_Alt.R37()
        r45_1 = Dashboard_M8_Alt.R45()
        var_1 = mult(r37_1, r45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class S53():
    # 'Dashboard_M8_Alt'!S53
    value = 1468.99965555
    formula = "=S37*S45/1000000"
    @eval_fn
    def S53():
        s37_1 = Dashboard_M8_Alt.S37()
        s45_1 = Dashboard_M8_Alt.S45()
        var_1 = mult(s37_1, s45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class T53():
    # 'Dashboard_M8_Alt'!T53
    value = 1326.30837317
    formula = "=T37*T45/1000000"
    @eval_fn
    def T53():
        t37_1 = Dashboard_M8_Alt.T37()
        t45_1 = Dashboard_M8_Alt.T45()
        var_1 = mult(t37_1, t45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class U53():
    # 'Dashboard_M8_Alt'!U53
    value = "#N/A"
    formula = "=U37*U45/1000000"
    @eval_fn
    def U53():
        u37_1 = Dashboard_M8_Alt.U37()
        u45_1 = Dashboard_M8_Alt.U45()
        var_1 = mult(u37_1, u45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class V53():
    # 'Dashboard_M8_Alt'!V53
    value = "#N/A"
    formula = "=V37*V45/1000000"
    @eval_fn
    def V53():
        v37_1 = Dashboard_M8_Alt.V37()
        v45_1 = Dashboard_M8_Alt.V45()
        var_1 = mult(v37_1, v45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class W53():
    # 'Dashboard_M8_Alt'!W53
    value = "#N/A"
    formula = "=W37*W45/1000000"
    @eval_fn
    def W53():
        w37_1 = Dashboard_M8_Alt.W37()
        w45_1 = Dashboard_M8_Alt.W45()
        var_1 = mult(w37_1, w45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class X53():
    # 'Dashboard_M8_Alt'!X53
    value = "#N/A"
    formula = "=X37*X45/1000000"
    @eval_fn
    def X53():
        x37_1 = Dashboard_M8_Alt.X37()
        x45_1 = Dashboard_M8_Alt.X45()
        var_1 = mult(x37_1, x45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Y53():
    # 'Dashboard_M8_Alt'!Y53
    value = "#N/A"
    formula = "=Y37*Y45/1000000"
    @eval_fn
    def Y53():
        y37_1 = Dashboard_M8_Alt.Y37()
        y45_1 = Dashboard_M8_Alt.Y45()
        var_1 = mult(y37_1, y45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Z53():
    # 'Dashboard_M8_Alt'!Z53
    value = "#N/A"
    formula = "=Z37*Z45/1000000"
    @eval_fn
    def Z53():
        z37_1 = Dashboard_M8_Alt.Z37()
        z45_1 = Dashboard_M8_Alt.Z45()
        var_1 = mult(z37_1, z45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AA53():
    # 'Dashboard_M8_Alt'!AA53
    value = "#N/A"
    formula = "=AA37*AA45/1000000"
    @eval_fn
    def AA53():
        aa37_1 = Dashboard_M8_Alt.AA37()
        aa45_1 = Dashboard_M8_Alt.AA45()
        var_1 = mult(aa37_1, aa45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AB53():
    # 'Dashboard_M8_Alt'!AB53
    value = "#N/A"
    formula = "=AB37*AB45/1000000"
    @eval_fn
    def AB53():
        ab37_1 = Dashboard_M8_Alt.AB37()
        ab45_1 = Dashboard_M8_Alt.AB45()
        var_1 = mult(ab37_1, ab45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AC53():
    # 'Dashboard_M8_Alt'!AC53
    value = "#N/A"
    formula = "=AC37*AC45/1000000"
    @eval_fn
    def AC53():
        ac37_1 = Dashboard_M8_Alt.AC37()
        ac45_1 = Dashboard_M8_Alt.AC45()
        var_1 = mult(ac37_1, ac45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AD53():
    # 'Dashboard_M8_Alt'!AD53
    value = "#N/A"
    formula = "=AD37*AD45/1000000"
    @eval_fn
    def AD53():
        ad37_1 = Dashboard_M8_Alt.AD37()
        ad45_1 = Dashboard_M8_Alt.AD45()
        var_1 = mult(ad37_1, ad45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AE53():
    # 'Dashboard_M8_Alt'!AE53
    value = "#N/A"
    formula = "=AE37*AE45/1000000"
    @eval_fn
    def AE53():
        ae37_1 = Dashboard_M8_Alt.AE37()
        ae45_1 = Dashboard_M8_Alt.AE45()
        var_1 = mult(ae37_1, ae45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AF53():
    # 'Dashboard_M8_Alt'!AF53
    value = "#N/A"
    formula = "=AF37*AF45/1000000"
    @eval_fn
    def AF53():
        af37_1 = Dashboard_M8_Alt.AF37()
        af45_1 = Dashboard_M8_Alt.AF45()
        var_1 = mult(af37_1, af45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AG53():
    # 'Dashboard_M8_Alt'!AG53
    value = "#N/A"
    formula = "=AG37*AG45/1000000"
    @eval_fn
    def AG53():
        ag37_1 = Dashboard_M8_Alt.AG37()
        ag45_1 = Dashboard_M8_Alt.AG45()
        var_1 = mult(ag37_1, ag45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AH53():
    # 'Dashboard_M8_Alt'!AH53
    value = "#N/A"
    formula = "=AH37*AH45/1000000"
    @eval_fn
    def AH53():
        ah37_1 = Dashboard_M8_Alt.AH37()
        ah45_1 = Dashboard_M8_Alt.AH45()
        var_1 = mult(ah37_1, ah45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AI53():
    # 'Dashboard_M8_Alt'!AI53
    value = "#N/A"
    formula = "=AI37*AI45/1000000"
    @eval_fn
    def AI53():
        ai37_1 = Dashboard_M8_Alt.AI37()
        ai45_1 = Dashboard_M8_Alt.AI45()
        var_1 = mult(ai37_1, ai45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ53():
    # 'Dashboard_M8_Alt'!AJ53
    value = "#N/A"
    formula = "=AJ37*AJ45/1000000"
    @eval_fn
    def AJ53():
        aj37_1 = Dashboard_M8_Alt.AJ37()
        aj45_1 = Dashboard_M8_Alt.AJ45()
        var_1 = mult(aj37_1, aj45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AK53():
    # 'Dashboard_M8_Alt'!AK53
    value = "#N/A"
    formula = "=AK37*AK45/1000000"
    @eval_fn
    def AK53():
        ak37_1 = Dashboard_M8_Alt.AK37()
        ak45_1 = Dashboard_M8_Alt.AK45()
        var_1 = mult(ak37_1, ak45_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class B54():
    # 'Dashboard_M8_Alt'!B54
    value = "SNG"

@register(Dashboard_M8_Alt)
class C54():
    # 'Dashboard_M8_Alt'!C54
    value = "Million Dollars"

@register(Dashboard_M8_Alt)
class I54():
    # 'Dashboard_M8_Alt'!I54
    value = 0
    formula = "=I38*I46/1000000"
    @eval_fn
    def I54():
        i38_1 = Dashboard_M8_Alt.I38()
        i46_1 = Dashboard_M8_Alt.I46()
        var_1 = mult(i38_1, i46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class J54():
    # 'Dashboard_M8_Alt'!J54
    value = 0
    formula = "=J38*J46/1000000"
    @eval_fn
    def J54():
        j38_1 = Dashboard_M8_Alt.J38()
        j46_1 = Dashboard_M8_Alt.J46()
        var_1 = mult(j38_1, j46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class K54():
    # 'Dashboard_M8_Alt'!K54
    value = 0
    formula = "=K38*K46/1000000"
    @eval_fn
    def K54():
        k38_1 = Dashboard_M8_Alt.K38()
        k46_1 = Dashboard_M8_Alt.K46()
        var_1 = mult(k38_1, k46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class L54():
    # 'Dashboard_M8_Alt'!L54
    value = 0
    formula = "=L38*L46/1000000"
    @eval_fn
    def L54():
        l38_1 = Dashboard_M8_Alt.L38()
        l46_1 = Dashboard_M8_Alt.L46()
        var_1 = mult(l38_1, l46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class M54():
    # 'Dashboard_M8_Alt'!M54
    value = 0
    formula = "=M38*M46/1000000"
    @eval_fn
    def M54():
        m38_1 = Dashboard_M8_Alt.M38()
        m46_1 = Dashboard_M8_Alt.M46()
        var_1 = mult(m38_1, m46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class N54():
    # 'Dashboard_M8_Alt'!N54
    value = 0
    formula = "=N38*N46/1000000"
    @eval_fn
    def N54():
        n38_1 = Dashboard_M8_Alt.N38()
        n46_1 = Dashboard_M8_Alt.N46()
        var_1 = mult(n38_1, n46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class O54():
    # 'Dashboard_M8_Alt'!O54
    value = 0
    formula = "=O38*O46/1000000"
    @eval_fn
    def O54():
        o38_1 = Dashboard_M8_Alt.O38()
        o46_1 = Dashboard_M8_Alt.O46()
        var_1 = mult(o38_1, o46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class P54():
    # 'Dashboard_M8_Alt'!P54
    value = 0
    formula = "=P38*P46/1000000"
    @eval_fn
    def P54():
        p38_1 = Dashboard_M8_Alt.P38()
        p46_1 = Dashboard_M8_Alt.P46()
        var_1 = mult(p38_1, p46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Q54():
    # 'Dashboard_M8_Alt'!Q54
    value = 0
    formula = "=Q38*Q46/1000000"
    @eval_fn
    def Q54():
        q38_1 = Dashboard_M8_Alt.Q38()
        q46_1 = Dashboard_M8_Alt.Q46()
        var_1 = mult(q38_1, q46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class R54():
    # 'Dashboard_M8_Alt'!R54
    value = 0
    formula = "=R38*R46/1000000"
    @eval_fn
    def R54():
        r38_1 = Dashboard_M8_Alt.R38()
        r46_1 = Dashboard_M8_Alt.R46()
        var_1 = mult(r38_1, r46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class S54():
    # 'Dashboard_M8_Alt'!S54
    value = 0
    formula = "=S38*S46/1000000"
    @eval_fn
    def S54():
        s38_1 = Dashboard_M8_Alt.S38()
        s46_1 = Dashboard_M8_Alt.S46()
        var_1 = mult(s38_1, s46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class T54():
    # 'Dashboard_M8_Alt'!T54
    value = 0
    formula = "=T38*T46/1000000"
    @eval_fn
    def T54():
        t38_1 = Dashboard_M8_Alt.T38()
        t46_1 = Dashboard_M8_Alt.T46()
        var_1 = mult(t38_1, t46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class U54():
    # 'Dashboard_M8_Alt'!U54
    value = "#N/A"
    formula = "=U38*U46/1000000"
    @eval_fn
    def U54():
        u38_1 = Dashboard_M8_Alt.U38()
        u46_1 = Dashboard_M8_Alt.U46()
        var_1 = mult(u38_1, u46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class V54():
    # 'Dashboard_M8_Alt'!V54
    value = "#N/A"
    formula = "=V38*V46/1000000"
    @eval_fn
    def V54():
        v38_1 = Dashboard_M8_Alt.V38()
        v46_1 = Dashboard_M8_Alt.V46()
        var_1 = mult(v38_1, v46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class W54():
    # 'Dashboard_M8_Alt'!W54
    value = "#N/A"
    formula = "=W38*W46/1000000"
    @eval_fn
    def W54():
        w38_1 = Dashboard_M8_Alt.W38()
        w46_1 = Dashboard_M8_Alt.W46()
        var_1 = mult(w38_1, w46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class X54():
    # 'Dashboard_M8_Alt'!X54
    value = "#N/A"
    formula = "=X38*X46/1000000"
    @eval_fn
    def X54():
        x38_1 = Dashboard_M8_Alt.X38()
        x46_1 = Dashboard_M8_Alt.X46()
        var_1 = mult(x38_1, x46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Y54():
    # 'Dashboard_M8_Alt'!Y54
    value = "#N/A"
    formula = "=Y38*Y46/1000000"
    @eval_fn
    def Y54():
        y38_1 = Dashboard_M8_Alt.Y38()
        y46_1 = Dashboard_M8_Alt.Y46()
        var_1 = mult(y38_1, y46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Z54():
    # 'Dashboard_M8_Alt'!Z54
    value = "#N/A"
    formula = "=Z38*Z46/1000000"
    @eval_fn
    def Z54():
        z38_1 = Dashboard_M8_Alt.Z38()
        z46_1 = Dashboard_M8_Alt.Z46()
        var_1 = mult(z38_1, z46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AA54():
    # 'Dashboard_M8_Alt'!AA54
    value = "#N/A"
    formula = "=AA38*AA46/1000000"
    @eval_fn
    def AA54():
        aa38_1 = Dashboard_M8_Alt.AA38()
        aa46_1 = Dashboard_M8_Alt.AA46()
        var_1 = mult(aa38_1, aa46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AB54():
    # 'Dashboard_M8_Alt'!AB54
    value = "#N/A"
    formula = "=AB38*AB46/1000000"
    @eval_fn
    def AB54():
        ab38_1 = Dashboard_M8_Alt.AB38()
        ab46_1 = Dashboard_M8_Alt.AB46()
        var_1 = mult(ab38_1, ab46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AC54():
    # 'Dashboard_M8_Alt'!AC54
    value = "#N/A"
    formula = "=AC38*AC46/1000000"
    @eval_fn
    def AC54():
        ac38_1 = Dashboard_M8_Alt.AC38()
        ac46_1 = Dashboard_M8_Alt.AC46()
        var_1 = mult(ac38_1, ac46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AD54():
    # 'Dashboard_M8_Alt'!AD54
    value = "#N/A"
    formula = "=AD38*AD46/1000000"
    @eval_fn
    def AD54():
        ad38_1 = Dashboard_M8_Alt.AD38()
        ad46_1 = Dashboard_M8_Alt.AD46()
        var_1 = mult(ad38_1, ad46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AE54():
    # 'Dashboard_M8_Alt'!AE54
    value = "#N/A"
    formula = "=AE38*AE46/1000000"
    @eval_fn
    def AE54():
        ae38_1 = Dashboard_M8_Alt.AE38()
        ae46_1 = Dashboard_M8_Alt.AE46()
        var_1 = mult(ae38_1, ae46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AF54():
    # 'Dashboard_M8_Alt'!AF54
    value = "#N/A"
    formula = "=AF38*AF46/1000000"
    @eval_fn
    def AF54():
        af38_1 = Dashboard_M8_Alt.AF38()
        af46_1 = Dashboard_M8_Alt.AF46()
        var_1 = mult(af38_1, af46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AG54():
    # 'Dashboard_M8_Alt'!AG54
    value = "#N/A"
    formula = "=AG38*AG46/1000000"
    @eval_fn
    def AG54():
        ag38_1 = Dashboard_M8_Alt.AG38()
        ag46_1 = Dashboard_M8_Alt.AG46()
        var_1 = mult(ag38_1, ag46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AH54():
    # 'Dashboard_M8_Alt'!AH54
    value = "#N/A"
    formula = "=AH38*AH46/1000000"
    @eval_fn
    def AH54():
        ah38_1 = Dashboard_M8_Alt.AH38()
        ah46_1 = Dashboard_M8_Alt.AH46()
        var_1 = mult(ah38_1, ah46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AI54():
    # 'Dashboard_M8_Alt'!AI54
    value = "#N/A"
    formula = "=AI38*AI46/1000000"
    @eval_fn
    def AI54():
        ai38_1 = Dashboard_M8_Alt.AI38()
        ai46_1 = Dashboard_M8_Alt.AI46()
        var_1 = mult(ai38_1, ai46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ54():
    # 'Dashboard_M8_Alt'!AJ54
    value = "#N/A"
    formula = "=AJ38*AJ46/1000000"
    @eval_fn
    def AJ54():
        aj38_1 = Dashboard_M8_Alt.AJ38()
        aj46_1 = Dashboard_M8_Alt.AJ46()
        var_1 = mult(aj38_1, aj46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AK54():
    # 'Dashboard_M8_Alt'!AK54
    value = "#N/A"
    formula = "=AK38*AK46/1000000"
    @eval_fn
    def AK54():
        ak38_1 = Dashboard_M8_Alt.AK38()
        ak46_1 = Dashboard_M8_Alt.AK46()
        var_1 = mult(ak38_1, ak46_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class B55():
    # 'Dashboard_M8_Alt'!B55
    value = "Coal"

@register(Dashboard_M8_Alt)
class C55():
    # 'Dashboard_M8_Alt'!C55
    value = "Million Dollars"

@register(Dashboard_M8_Alt)
class I55():
    # 'Dashboard_M8_Alt'!I55
    value = 25.4693837957
    formula = "=I39*I47/1000000"
    @eval_fn
    def I55():
        i39_1 = Dashboard_M8_Alt.I39()
        i47_1 = Dashboard_M8_Alt.I47()
        var_1 = mult(i39_1, i47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class J55():
    # 'Dashboard_M8_Alt'!J55
    value = 47.4532822909
    formula = "=J39*J47/1000000"
    @eval_fn
    def J55():
        j39_1 = Dashboard_M8_Alt.J39()
        j47_1 = Dashboard_M8_Alt.J47()
        var_1 = mult(j39_1, j47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class K55():
    # 'Dashboard_M8_Alt'!K55
    value = 30.9641024019
    formula = "=K39*K47/1000000"
    @eval_fn
    def K55():
        k39_1 = Dashboard_M8_Alt.K39()
        k47_1 = Dashboard_M8_Alt.K47()
        var_1 = mult(k39_1, k47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class L55():
    # 'Dashboard_M8_Alt'!L55
    value = 24.6816927395
    formula = "=L39*L47/1000000"
    @eval_fn
    def L55():
        l39_1 = Dashboard_M8_Alt.L39()
        l47_1 = Dashboard_M8_Alt.L47()
        var_1 = mult(l39_1, l47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class M55():
    # 'Dashboard_M8_Alt'!M55
    value = 28.8261729901
    formula = "=M39*M47/1000000"
    @eval_fn
    def M55():
        m39_1 = Dashboard_M8_Alt.M39()
        m47_1 = Dashboard_M8_Alt.M47()
        var_1 = mult(m39_1, m47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class N55():
    # 'Dashboard_M8_Alt'!N55
    value = 31.9257787622
    formula = "=N39*N47/1000000"
    @eval_fn
    def N55():
        n39_1 = Dashboard_M8_Alt.N39()
        n47_1 = Dashboard_M8_Alt.N47()
        var_1 = mult(n39_1, n47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class O55():
    # 'Dashboard_M8_Alt'!O55
    value = 37.3949213012
    formula = "=O39*O47/1000000"
    @eval_fn
    def O55():
        o39_1 = Dashboard_M8_Alt.O39()
        o47_1 = Dashboard_M8_Alt.O47()
        var_1 = mult(o39_1, o47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class P55():
    # 'Dashboard_M8_Alt'!P55
    value = 37.5283135002
    formula = "=P39*P47/1000000"
    @eval_fn
    def P55():
        p39_1 = Dashboard_M8_Alt.P39()
        p47_1 = Dashboard_M8_Alt.P47()
        var_1 = mult(p39_1, p47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Q55():
    # 'Dashboard_M8_Alt'!Q55
    value = 37.2266050647
    formula = "=Q39*Q47/1000000"
    @eval_fn
    def Q55():
        q39_1 = Dashboard_M8_Alt.Q39()
        q47_1 = Dashboard_M8_Alt.Q47()
        var_1 = mult(q39_1, q47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class R55():
    # 'Dashboard_M8_Alt'!R55
    value = 27.3446665169
    formula = "=R39*R47/1000000"
    @eval_fn
    def R55():
        r39_1 = Dashboard_M8_Alt.R39()
        r47_1 = Dashboard_M8_Alt.R47()
        var_1 = mult(r39_1, r47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class S55():
    # 'Dashboard_M8_Alt'!S55
    value = 30.217126981
    formula = "=S39*S47/1000000"
    @eval_fn
    def S55():
        s39_1 = Dashboard_M8_Alt.S39()
        s47_1 = Dashboard_M8_Alt.S47()
        var_1 = mult(s39_1, s47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class T55():
    # 'Dashboard_M8_Alt'!T55
    value = 29.9888544863
    formula = "=T39*T47/1000000"
    @eval_fn
    def T55():
        t39_1 = Dashboard_M8_Alt.T39()
        t47_1 = Dashboard_M8_Alt.T47()
        var_1 = mult(t39_1, t47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class U55():
    # 'Dashboard_M8_Alt'!U55
    value = "#N/A"
    formula = "=U39*U47/1000000"
    @eval_fn
    def U55():
        u39_1 = Dashboard_M8_Alt.U39()
        u47_1 = Dashboard_M8_Alt.U47()
        var_1 = mult(u39_1, u47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class V55():
    # 'Dashboard_M8_Alt'!V55
    value = "#N/A"
    formula = "=V39*V47/1000000"
    @eval_fn
    def V55():
        v39_1 = Dashboard_M8_Alt.V39()
        v47_1 = Dashboard_M8_Alt.V47()
        var_1 = mult(v39_1, v47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class W55():
    # 'Dashboard_M8_Alt'!W55
    value = "#N/A"
    formula = "=W39*W47/1000000"
    @eval_fn
    def W55():
        w39_1 = Dashboard_M8_Alt.W39()
        w47_1 = Dashboard_M8_Alt.W47()
        var_1 = mult(w39_1, w47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class X55():
    # 'Dashboard_M8_Alt'!X55
    value = "#N/A"
    formula = "=X39*X47/1000000"
    @eval_fn
    def X55():
        x39_1 = Dashboard_M8_Alt.X39()
        x47_1 = Dashboard_M8_Alt.X47()
        var_1 = mult(x39_1, x47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Y55():
    # 'Dashboard_M8_Alt'!Y55
    value = "#N/A"
    formula = "=Y39*Y47/1000000"
    @eval_fn
    def Y55():
        y39_1 = Dashboard_M8_Alt.Y39()
        y47_1 = Dashboard_M8_Alt.Y47()
        var_1 = mult(y39_1, y47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Z55():
    # 'Dashboard_M8_Alt'!Z55
    value = "#N/A"
    formula = "=Z39*Z47/1000000"
    @eval_fn
    def Z55():
        z39_1 = Dashboard_M8_Alt.Z39()
        z47_1 = Dashboard_M8_Alt.Z47()
        var_1 = mult(z39_1, z47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AA55():
    # 'Dashboard_M8_Alt'!AA55
    value = "#N/A"
    formula = "=AA39*AA47/1000000"
    @eval_fn
    def AA55():
        aa39_1 = Dashboard_M8_Alt.AA39()
        aa47_1 = Dashboard_M8_Alt.AA47()
        var_1 = mult(aa39_1, aa47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AB55():
    # 'Dashboard_M8_Alt'!AB55
    value = "#N/A"
    formula = "=AB39*AB47/1000000"
    @eval_fn
    def AB55():
        ab39_1 = Dashboard_M8_Alt.AB39()
        ab47_1 = Dashboard_M8_Alt.AB47()
        var_1 = mult(ab39_1, ab47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AC55():
    # 'Dashboard_M8_Alt'!AC55
    value = "#N/A"
    formula = "=AC39*AC47/1000000"
    @eval_fn
    def AC55():
        ac39_1 = Dashboard_M8_Alt.AC39()
        ac47_1 = Dashboard_M8_Alt.AC47()
        var_1 = mult(ac39_1, ac47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AD55():
    # 'Dashboard_M8_Alt'!AD55
    value = "#N/A"
    formula = "=AD39*AD47/1000000"
    @eval_fn
    def AD55():
        ad39_1 = Dashboard_M8_Alt.AD39()
        ad47_1 = Dashboard_M8_Alt.AD47()
        var_1 = mult(ad39_1, ad47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AE55():
    # 'Dashboard_M8_Alt'!AE55
    value = "#N/A"
    formula = "=AE39*AE47/1000000"
    @eval_fn
    def AE55():
        ae39_1 = Dashboard_M8_Alt.AE39()
        ae47_1 = Dashboard_M8_Alt.AE47()
        var_1 = mult(ae39_1, ae47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AF55():
    # 'Dashboard_M8_Alt'!AF55
    value = "#N/A"
    formula = "=AF39*AF47/1000000"
    @eval_fn
    def AF55():
        af39_1 = Dashboard_M8_Alt.AF39()
        af47_1 = Dashboard_M8_Alt.AF47()
        var_1 = mult(af39_1, af47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AG55():
    # 'Dashboard_M8_Alt'!AG55
    value = "#N/A"
    formula = "=AG39*AG47/1000000"
    @eval_fn
    def AG55():
        ag39_1 = Dashboard_M8_Alt.AG39()
        ag47_1 = Dashboard_M8_Alt.AG47()
        var_1 = mult(ag39_1, ag47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AH55():
    # 'Dashboard_M8_Alt'!AH55
    value = "#N/A"
    formula = "=AH39*AH47/1000000"
    @eval_fn
    def AH55():
        ah39_1 = Dashboard_M8_Alt.AH39()
        ah47_1 = Dashboard_M8_Alt.AH47()
        var_1 = mult(ah39_1, ah47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AI55():
    # 'Dashboard_M8_Alt'!AI55
    value = "#N/A"
    formula = "=AI39*AI47/1000000"
    @eval_fn
    def AI55():
        ai39_1 = Dashboard_M8_Alt.AI39()
        ai47_1 = Dashboard_M8_Alt.AI47()
        var_1 = mult(ai39_1, ai47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ55():
    # 'Dashboard_M8_Alt'!AJ55
    value = "#N/A"
    formula = "=AJ39*AJ47/1000000"
    @eval_fn
    def AJ55():
        aj39_1 = Dashboard_M8_Alt.AJ39()
        aj47_1 = Dashboard_M8_Alt.AJ47()
        var_1 = mult(aj39_1, aj47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AK55():
    # 'Dashboard_M8_Alt'!AK55
    value = "#N/A"
    formula = "=AK39*AK47/1000000"
    @eval_fn
    def AK55():
        ak39_1 = Dashboard_M8_Alt.AK39()
        ak47_1 = Dashboard_M8_Alt.AK47()
        var_1 = mult(ak39_1, ak47_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class B56():
    # 'Dashboard_M8_Alt'!B56
    value = "All Fuels"

@register(Dashboard_M8_Alt)
class C56():
    # 'Dashboard_M8_Alt'!C56
    value = "Million Dollars"

@register(Dashboard_M8_Alt)
class I56():
    # 'Dashboard_M8_Alt'!I56
    value = 441.313512537
    formula = "=SUM(I52:I55)"
    @eval_fn
    def I56():
        range_1 = Dashboard_M8_Alt(9, 52, 9, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class J56():
    # 'Dashboard_M8_Alt'!J56
    value = 492.070175541
    formula = "=SUM(J52:J55)"
    @eval_fn
    def J56():
        range_1 = Dashboard_M8_Alt(10, 52, 10, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class K56():
    # 'Dashboard_M8_Alt'!K56
    value = 521.954475559
    formula = "=SUM(K52:K55)"
    @eval_fn
    def K56():
        range_1 = Dashboard_M8_Alt(11, 52, 11, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class L56():
    # 'Dashboard_M8_Alt'!L56
    value = 830.084436286
    formula = "=SUM(L52:L55)"
    @eval_fn
    def L56():
        range_1 = Dashboard_M8_Alt(12, 52, 12, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class M56():
    # 'Dashboard_M8_Alt'!M56
    value = 998.492561276
    formula = "=SUM(M52:M55)"
    @eval_fn
    def M56():
        range_1 = Dashboard_M8_Alt(13, 52, 13, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class N56():
    # 'Dashboard_M8_Alt'!N56
    value = 1097.09768772
    formula = "=SUM(N52:N55)"
    @eval_fn
    def N56():
        range_1 = Dashboard_M8_Alt(14, 52, 14, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class O56():
    # 'Dashboard_M8_Alt'!O56
    value = 1581.50656217
    formula = "=SUM(O52:O55)"
    @eval_fn
    def O56():
        range_1 = Dashboard_M8_Alt(15, 52, 15, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class P56():
    # 'Dashboard_M8_Alt'!P56
    value = 925.457589754
    formula = "=SUM(P52:P55)"
    @eval_fn
    def P56():
        range_1 = Dashboard_M8_Alt(16, 52, 16, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q56():
    # 'Dashboard_M8_Alt'!Q56
    value = 1275.15309137
    formula = "=SUM(Q52:Q55)"
    @eval_fn
    def Q56():
        range_1 = Dashboard_M8_Alt(17, 52, 17, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class R56():
    # 'Dashboard_M8_Alt'!R56
    value = 1761.81655405
    formula = "=SUM(R52:R55)"
    @eval_fn
    def R56():
        range_1 = Dashboard_M8_Alt(18, 52, 18, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class S56():
    # 'Dashboard_M8_Alt'!S56
    value = 1860.97919473
    formula = "=SUM(S52:S55)"
    @eval_fn
    def S56():
        range_1 = Dashboard_M8_Alt(19, 52, 19, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class T56():
    # 'Dashboard_M8_Alt'!T56
    value = 1687.19152107
    formula = "=SUM(T52:T55)"
    @eval_fn
    def T56():
        range_1 = Dashboard_M8_Alt(20, 52, 20, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class U56():
    # 'Dashboard_M8_Alt'!U56
    value = "#N/A"
    formula = "=SUM(U52:U55)"
    @eval_fn
    def U56():
        range_1 = Dashboard_M8_Alt(21, 52, 21, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class V56():
    # 'Dashboard_M8_Alt'!V56
    value = "#N/A"
    formula = "=SUM(V52:V55)"
    @eval_fn
    def V56():
        range_1 = Dashboard_M8_Alt(22, 52, 22, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class W56():
    # 'Dashboard_M8_Alt'!W56
    value = "#N/A"
    formula = "=SUM(W52:W55)"
    @eval_fn
    def W56():
        range_1 = Dashboard_M8_Alt(23, 52, 23, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class X56():
    # 'Dashboard_M8_Alt'!X56
    value = "#N/A"
    formula = "=SUM(X52:X55)"
    @eval_fn
    def X56():
        range_1 = Dashboard_M8_Alt(24, 52, 24, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y56():
    # 'Dashboard_M8_Alt'!Y56
    value = "#N/A"
    formula = "=SUM(Y52:Y55)"
    @eval_fn
    def Y56():
        range_1 = Dashboard_M8_Alt(25, 52, 25, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z56():
    # 'Dashboard_M8_Alt'!Z56
    value = "#N/A"
    formula = "=SUM(Z52:Z55)"
    @eval_fn
    def Z56():
        range_1 = Dashboard_M8_Alt(26, 52, 26, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA56():
    # 'Dashboard_M8_Alt'!AA56
    value = "#N/A"
    formula = "=SUM(AA52:AA55)"
    @eval_fn
    def AA56():
        range_1 = Dashboard_M8_Alt(27, 52, 27, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB56():
    # 'Dashboard_M8_Alt'!AB56
    value = "#N/A"
    formula = "=SUM(AB52:AB55)"
    @eval_fn
    def AB56():
        range_1 = Dashboard_M8_Alt(28, 52, 28, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC56():
    # 'Dashboard_M8_Alt'!AC56
    value = "#N/A"
    formula = "=SUM(AC52:AC55)"
    @eval_fn
    def AC56():
        range_1 = Dashboard_M8_Alt(29, 52, 29, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD56():
    # 'Dashboard_M8_Alt'!AD56
    value = "#N/A"
    formula = "=SUM(AD52:AD55)"
    @eval_fn
    def AD56():
        range_1 = Dashboard_M8_Alt(30, 52, 30, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE56():
    # 'Dashboard_M8_Alt'!AE56
    value = "#N/A"
    formula = "=SUM(AE52:AE55)"
    @eval_fn
    def AE56():
        range_1 = Dashboard_M8_Alt(31, 52, 31, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF56():
    # 'Dashboard_M8_Alt'!AF56
    value = "#N/A"
    formula = "=SUM(AF52:AF55)"
    @eval_fn
    def AF56():
        range_1 = Dashboard_M8_Alt(32, 52, 32, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG56():
    # 'Dashboard_M8_Alt'!AG56
    value = "#N/A"
    formula = "=SUM(AG52:AG55)"
    @eval_fn
    def AG56():
        range_1 = Dashboard_M8_Alt(33, 52, 33, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH56():
    # 'Dashboard_M8_Alt'!AH56
    value = "#N/A"
    formula = "=SUM(AH52:AH55)"
    @eval_fn
    def AH56():
        range_1 = Dashboard_M8_Alt(34, 52, 34, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI56():
    # 'Dashboard_M8_Alt'!AI56
    value = "#N/A"
    formula = "=SUM(AI52:AI55)"
    @eval_fn
    def AI56():
        range_1 = Dashboard_M8_Alt(35, 52, 35, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ56():
    # 'Dashboard_M8_Alt'!AJ56
    value = "#N/A"
    formula = "=SUM(AJ52:AJ55)"
    @eval_fn
    def AJ56():
        range_1 = Dashboard_M8_Alt(36, 52, 36, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK56():
    # 'Dashboard_M8_Alt'!AK56
    value = "#N/A"
    formula = "=SUM(AK52:AK55)"
    @eval_fn
    def AK56():
        range_1 = Dashboard_M8_Alt(37, 52, 37, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class A58():
    # 'Dashboard_M8_Alt'!A58
    value = "Variabl AFC(Actual,y,p,f): Actual Fuel Consumption for Power Sector by Year and Fuel"

@register(Dashboard_M8_Alt)
class B59():
    # 'Dashboard_M8_Alt'!B59
    value = "Diesel"

@register(Dashboard_M8_Alt)
class C59():
    # 'Dashboard_M8_Alt'!C59
    value = "Billion Btu"

@register(Dashboard_M8_Alt)
class I59():
    # 'Dashboard_M8_Alt'!I59
    value = 23223000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!I24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def I59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        i24_1 = Dashboard_M8_Alt.I24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, i24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class J59():
    # 'Dashboard_M8_Alt'!J59
    value = 13381000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!J24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def J59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        j24_1 = Dashboard_M8_Alt.J24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, j24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class K59():
    # 'Dashboard_M8_Alt'!K59
    value = 14482000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!K24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def K59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        k24_1 = Dashboard_M8_Alt.K24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, k24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class L59():
    # 'Dashboard_M8_Alt'!L59
    value = 15053000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!L24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def L59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        l24_1 = Dashboard_M8_Alt.L24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, l24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class M59():
    # 'Dashboard_M8_Alt'!M59
    value = 14290000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!M24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def M59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        m24_1 = Dashboard_M8_Alt.M24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, m24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class N59():
    # 'Dashboard_M8_Alt'!N59
    value = 13472000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!N24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def N59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        n24_1 = Dashboard_M8_Alt.N24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, n24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class O59():
    # 'Dashboard_M8_Alt'!O59
    value = 12811000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!O24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def O59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        o24_1 = Dashboard_M8_Alt.O24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, o24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class P59():
    # 'Dashboard_M8_Alt'!P59
    value = 13107000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!P24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def P59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        p24_1 = Dashboard_M8_Alt.P24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, p24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Q59():
    # 'Dashboard_M8_Alt'!Q59
    value = 13083000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!Q24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def Q59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        q24_1 = Dashboard_M8_Alt.Q24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, q24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class R59():
    # 'Dashboard_M8_Alt'!R59
    value = 13186000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!R24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def R59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        r24_1 = Dashboard_M8_Alt.R24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, r24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class S59():
    # 'Dashboard_M8_Alt'!S59
    value = 12607000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!S24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def S59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        s24_1 = Dashboard_M8_Alt.S24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, s24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class T59():
    # 'Dashboard_M8_Alt'!T59
    value = 12003000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!T24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def T59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        t24_1 = Dashboard_M8_Alt.T24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, t24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class U59():
    # 'Dashboard_M8_Alt'!U59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!U24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def U59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        u24_1 = Dashboard_M8_Alt.U24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, u24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class V59():
    # 'Dashboard_M8_Alt'!V59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!V24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def V59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        v24_1 = Dashboard_M8_Alt.V24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, v24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class W59():
    # 'Dashboard_M8_Alt'!W59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!W24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def W59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        w24_1 = Dashboard_M8_Alt.W24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, w24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class X59():
    # 'Dashboard_M8_Alt'!X59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!X24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def X59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        x24_1 = Dashboard_M8_Alt.X24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, x24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Y59():
    # 'Dashboard_M8_Alt'!Y59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!Y24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def Y59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        y24_1 = Dashboard_M8_Alt.Y24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, y24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Z59():
    # 'Dashboard_M8_Alt'!Z59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!Z24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def Z59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        z24_1 = Dashboard_M8_Alt.Z24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, z24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AA59():
    # 'Dashboard_M8_Alt'!AA59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AA24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AA59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aa24_1 = Dashboard_M8_Alt.AA24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, aa24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AB59():
    # 'Dashboard_M8_Alt'!AB59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AB24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AB59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ab24_1 = Dashboard_M8_Alt.AB24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, ab24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AC59():
    # 'Dashboard_M8_Alt'!AC59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AC24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AC59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ac24_1 = Dashboard_M8_Alt.AC24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, ac24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AD59():
    # 'Dashboard_M8_Alt'!AD59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AD24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AD59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ad24_1 = Dashboard_M8_Alt.AD24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, ad24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AE59():
    # 'Dashboard_M8_Alt'!AE59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AE24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AE59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ae24_1 = Dashboard_M8_Alt.AE24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, ae24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AF59():
    # 'Dashboard_M8_Alt'!AF59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AF24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AF59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        af24_1 = Dashboard_M8_Alt.AF24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, af24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AG59():
    # 'Dashboard_M8_Alt'!AG59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AG24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AG59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ag24_1 = Dashboard_M8_Alt.AG24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, ag24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AH59():
    # 'Dashboard_M8_Alt'!AH59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AH24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AH59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ah24_1 = Dashboard_M8_Alt.AH24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, ah24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AI59():
    # 'Dashboard_M8_Alt'!AI59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AI24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AI59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ai24_1 = Dashboard_M8_Alt.AI24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, ai24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ59():
    # 'Dashboard_M8_Alt'!AJ59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AJ24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AJ59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aj24_1 = Dashboard_M8_Alt.AJ24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, aj24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AK59():
    # 'Dashboard_M8_Alt'!AK59
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AK24,'EIA Consumption'!$E$50:$CD$50)*1000"
    @eval_fn
    def AK59():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ak24_1 = Dashboard_M8_Alt.AK24()
        range_2 = EIA_Consumption(5, 50, 82, 50)
        var_1 = SUMIF(range_1, ak24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class B60():
    # 'Dashboard_M8_Alt'!B60
    value = "Fuel Oil"

@register(Dashboard_M8_Alt)
class C60():
    # 'Dashboard_M8_Alt'!C60
    value = "Billion Btu"

@register(Dashboard_M8_Alt)
class I60():
    # 'Dashboard_M8_Alt'!I60
    value = 68247000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,I24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def I60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        i24_1 = Dashboard_M8_Alt.I24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, i24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class J60():
    # 'Dashboard_M8_Alt'!J60
    value = 67907000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,J24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def J60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        j24_1 = Dashboard_M8_Alt.J24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, j24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class K60():
    # 'Dashboard_M8_Alt'!K60
    value = 70527000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,K24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def K60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        k24_1 = Dashboard_M8_Alt.K24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, k24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class L60():
    # 'Dashboard_M8_Alt'!L60
    value = 71070000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,L24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def L60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        l24_1 = Dashboard_M8_Alt.L24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, l24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class M60():
    # 'Dashboard_M8_Alt'!M60
    value = 72295000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,M24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def M60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        m24_1 = Dashboard_M8_Alt.M24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, m24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class N60():
    # 'Dashboard_M8_Alt'!N60
    value = 71832000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,N24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def N60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        n24_1 = Dashboard_M8_Alt.N24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, n24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class O60():
    # 'Dashboard_M8_Alt'!O60
    value = 69217000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,O24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def O60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        o24_1 = Dashboard_M8_Alt.O24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, o24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class P60():
    # 'Dashboard_M8_Alt'!P60
    value = 67297000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,P24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def P60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        p24_1 = Dashboard_M8_Alt.P24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, p24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Q60():
    # 'Dashboard_M8_Alt'!Q60
    value = 65157000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Q24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def Q60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        q24_1 = Dashboard_M8_Alt.Q24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, q24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class R60():
    # 'Dashboard_M8_Alt'!R60
    value = 64471000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,R24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def R60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        r24_1 = Dashboard_M8_Alt.R24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, r24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class S60():
    # 'Dashboard_M8_Alt'!S60
    value = 59686000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,S24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def S60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        s24_1 = Dashboard_M8_Alt.S24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, s24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class T60():
    # 'Dashboard_M8_Alt'!T60
    value = 57940000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,T24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def T60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        t24_1 = Dashboard_M8_Alt.T24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, t24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class U60():
    # 'Dashboard_M8_Alt'!U60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,U24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def U60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        u24_1 = Dashboard_M8_Alt.U24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, u24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class V60():
    # 'Dashboard_M8_Alt'!V60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,V24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def V60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        v24_1 = Dashboard_M8_Alt.V24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, v24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class W60():
    # 'Dashboard_M8_Alt'!W60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,W24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def W60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        w24_1 = Dashboard_M8_Alt.W24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, w24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class X60():
    # 'Dashboard_M8_Alt'!X60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,X24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def X60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        x24_1 = Dashboard_M8_Alt.X24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, x24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Y60():
    # 'Dashboard_M8_Alt'!Y60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Y24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def Y60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        y24_1 = Dashboard_M8_Alt.Y24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, y24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Z60():
    # 'Dashboard_M8_Alt'!Z60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,Z24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def Z60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        z24_1 = Dashboard_M8_Alt.Z24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, z24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AA60():
    # 'Dashboard_M8_Alt'!AA60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AA24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AA60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aa24_1 = Dashboard_M8_Alt.AA24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, aa24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AB60():
    # 'Dashboard_M8_Alt'!AB60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AB24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AB60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ab24_1 = Dashboard_M8_Alt.AB24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, ab24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AC60():
    # 'Dashboard_M8_Alt'!AC60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AC24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AC60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ac24_1 = Dashboard_M8_Alt.AC24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, ac24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AD60():
    # 'Dashboard_M8_Alt'!AD60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AD24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AD60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ad24_1 = Dashboard_M8_Alt.AD24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, ad24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AE60():
    # 'Dashboard_M8_Alt'!AE60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AE24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AE60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ae24_1 = Dashboard_M8_Alt.AE24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, ae24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AF60():
    # 'Dashboard_M8_Alt'!AF60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AF24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AF60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        af24_1 = Dashboard_M8_Alt.AF24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, af24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AG60():
    # 'Dashboard_M8_Alt'!AG60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AG24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AG60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ag24_1 = Dashboard_M8_Alt.AG24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, ag24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AH60():
    # 'Dashboard_M8_Alt'!AH60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AH24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AH60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ah24_1 = Dashboard_M8_Alt.AH24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, ah24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AI60():
    # 'Dashboard_M8_Alt'!AI60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AI24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AI60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ai24_1 = Dashboard_M8_Alt.AI24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, ai24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ60():
    # 'Dashboard_M8_Alt'!AJ60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AJ24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AJ60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aj24_1 = Dashboard_M8_Alt.AJ24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, aj24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AK60():
    # 'Dashboard_M8_Alt'!AK60
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,AK24,'EIA Consumption'!$E$246:$CD$246)*1000"
    @eval_fn
    def AK60():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ak24_1 = Dashboard_M8_Alt.AK24()
        range_2 = EIA_Consumption(5, 246, 82, 246)
        var_1 = SUMIF(range_1, ak24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class B61():
    # 'Dashboard_M8_Alt'!B61
    value = "SNG"

@register(Dashboard_M8_Alt)
class C61():
    # 'Dashboard_M8_Alt'!C61
    value = "Billion Btu"

@register(Dashboard_M8_Alt)
class I61():
    # 'Dashboard_M8_Alt'!I61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!I24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def I61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        i24_1 = Dashboard_M8_Alt.I24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, i24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class J61():
    # 'Dashboard_M8_Alt'!J61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!J24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def J61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        j24_1 = Dashboard_M8_Alt.J24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, j24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class K61():
    # 'Dashboard_M8_Alt'!K61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!K24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def K61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        k24_1 = Dashboard_M8_Alt.K24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, k24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class L61():
    # 'Dashboard_M8_Alt'!L61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!L24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def L61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        l24_1 = Dashboard_M8_Alt.L24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, l24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class M61():
    # 'Dashboard_M8_Alt'!M61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!M24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def M61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        m24_1 = Dashboard_M8_Alt.M24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, m24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class N61():
    # 'Dashboard_M8_Alt'!N61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!N24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def N61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        n24_1 = Dashboard_M8_Alt.N24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, n24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class O61():
    # 'Dashboard_M8_Alt'!O61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!O24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def O61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        o24_1 = Dashboard_M8_Alt.O24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, o24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class P61():
    # 'Dashboard_M8_Alt'!P61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!P24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def P61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        p24_1 = Dashboard_M8_Alt.P24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, p24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Q61():
    # 'Dashboard_M8_Alt'!Q61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!Q24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def Q61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        q24_1 = Dashboard_M8_Alt.Q24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, q24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class R61():
    # 'Dashboard_M8_Alt'!R61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!R24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def R61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        r24_1 = Dashboard_M8_Alt.R24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, r24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class S61():
    # 'Dashboard_M8_Alt'!S61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!S24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def S61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        s24_1 = Dashboard_M8_Alt.S24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, s24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class T61():
    # 'Dashboard_M8_Alt'!T61
    value = 0
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!T24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def T61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        t24_1 = Dashboard_M8_Alt.T24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, t24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class U61():
    # 'Dashboard_M8_Alt'!U61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!U24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def U61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        u24_1 = Dashboard_M8_Alt.U24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, u24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class V61():
    # 'Dashboard_M8_Alt'!V61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!V24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def V61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        v24_1 = Dashboard_M8_Alt.V24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, v24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class W61():
    # 'Dashboard_M8_Alt'!W61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!W24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def W61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        w24_1 = Dashboard_M8_Alt.W24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, w24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class X61():
    # 'Dashboard_M8_Alt'!X61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!X24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def X61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        x24_1 = Dashboard_M8_Alt.X24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, x24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Y61():
    # 'Dashboard_M8_Alt'!Y61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!Y24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def Y61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        y24_1 = Dashboard_M8_Alt.Y24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, y24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Z61():
    # 'Dashboard_M8_Alt'!Z61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!Z24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def Z61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        z24_1 = Dashboard_M8_Alt.Z24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, z24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AA61():
    # 'Dashboard_M8_Alt'!AA61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AA24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AA61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aa24_1 = Dashboard_M8_Alt.AA24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, aa24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AB61():
    # 'Dashboard_M8_Alt'!AB61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AB24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AB61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ab24_1 = Dashboard_M8_Alt.AB24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, ab24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AC61():
    # 'Dashboard_M8_Alt'!AC61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AC24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AC61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ac24_1 = Dashboard_M8_Alt.AC24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, ac24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AD61():
    # 'Dashboard_M8_Alt'!AD61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AD24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AD61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ad24_1 = Dashboard_M8_Alt.AD24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, ad24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AE61():
    # 'Dashboard_M8_Alt'!AE61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AE24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AE61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ae24_1 = Dashboard_M8_Alt.AE24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, ae24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AF61():
    # 'Dashboard_M8_Alt'!AF61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AF24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AF61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        af24_1 = Dashboard_M8_Alt.AF24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, af24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AG61():
    # 'Dashboard_M8_Alt'!AG61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AG24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AG61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ag24_1 = Dashboard_M8_Alt.AG24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, ag24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AH61():
    # 'Dashboard_M8_Alt'!AH61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AH24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AH61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ah24_1 = Dashboard_M8_Alt.AH24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, ah24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AI61():
    # 'Dashboard_M8_Alt'!AI61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AI24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AI61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ai24_1 = Dashboard_M8_Alt.AI24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, ai24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ61():
    # 'Dashboard_M8_Alt'!AJ61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AJ24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AJ61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aj24_1 = Dashboard_M8_Alt.AJ24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, aj24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AK61():
    # 'Dashboard_M8_Alt'!AK61
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AK24,'EIA Consumption'!$E$176:$CD$176)*1000"
    @eval_fn
    def AK61():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ak24_1 = Dashboard_M8_Alt.AK24()
        range_2 = EIA_Consumption(5, 176, 82, 176)
        var_1 = SUMIF(range_1, ak24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class B62():
    # 'Dashboard_M8_Alt'!B62
    value = "Coal"

@register(Dashboard_M8_Alt)
class C62():
    # 'Dashboard_M8_Alt'!C62
    value = "Billion Btu"

@register(Dashboard_M8_Alt)
class I62():
    # 'Dashboard_M8_Alt'!I62
    value = 15963000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!I24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def I62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        i24_1 = Dashboard_M8_Alt.I24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, i24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class J62():
    # 'Dashboard_M8_Alt'!J62
    value = 17882000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!J24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def J62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        j24_1 = Dashboard_M8_Alt.J24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, j24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class K62():
    # 'Dashboard_M8_Alt'!K62
    value = 18001000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!K24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def K62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        k24_1 = Dashboard_M8_Alt.K24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, k24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class L62():
    # 'Dashboard_M8_Alt'!L62
    value = 16545000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!L24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def L62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        l24_1 = Dashboard_M8_Alt.L24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, l24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class M62():
    # 'Dashboard_M8_Alt'!M62
    value = 15889000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!M24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def M62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        m24_1 = Dashboard_M8_Alt.M24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, m24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class N62():
    # 'Dashboard_M8_Alt'!N62
    value = 17213000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!N24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def N62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        n24_1 = Dashboard_M8_Alt.N24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, n24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class O62():
    # 'Dashboard_M8_Alt'!O62
    value = 17847000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!O24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def O62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        o24_1 = Dashboard_M8_Alt.O24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, o24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class P62():
    # 'Dashboard_M8_Alt'!P62
    value = 16925000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!P24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def P62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        p24_1 = Dashboard_M8_Alt.P24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, p24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Q62():
    # 'Dashboard_M8_Alt'!Q62
    value = 15702000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!Q24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def Q62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        q24_1 = Dashboard_M8_Alt.Q24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, q24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class R62():
    # 'Dashboard_M8_Alt'!R62
    value = 14775000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!R24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def R62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        r24_1 = Dashboard_M8_Alt.R24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, r24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class S62():
    # 'Dashboard_M8_Alt'!S62
    value = 15432000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!S24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def S62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        s24_1 = Dashboard_M8_Alt.S24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, s24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class T62():
    # 'Dashboard_M8_Alt'!T62
    value = 13948000
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!T24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def T62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        t24_1 = Dashboard_M8_Alt.T24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, t24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class U62():
    # 'Dashboard_M8_Alt'!U62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!U24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def U62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        u24_1 = Dashboard_M8_Alt.U24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, u24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class V62():
    # 'Dashboard_M8_Alt'!V62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!V24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def V62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        v24_1 = Dashboard_M8_Alt.V24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, v24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class W62():
    # 'Dashboard_M8_Alt'!W62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!W24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def W62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        w24_1 = Dashboard_M8_Alt.W24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, w24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class X62():
    # 'Dashboard_M8_Alt'!X62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!X24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def X62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        x24_1 = Dashboard_M8_Alt.X24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, x24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Y62():
    # 'Dashboard_M8_Alt'!Y62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!Y24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def Y62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        y24_1 = Dashboard_M8_Alt.Y24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, y24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class Z62():
    # 'Dashboard_M8_Alt'!Z62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!Z24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def Z62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        z24_1 = Dashboard_M8_Alt.Z24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, z24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AA62():
    # 'Dashboard_M8_Alt'!AA62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AA24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AA62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aa24_1 = Dashboard_M8_Alt.AA24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, aa24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AB62():
    # 'Dashboard_M8_Alt'!AB62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AB24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AB62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ab24_1 = Dashboard_M8_Alt.AB24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, ab24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AC62():
    # 'Dashboard_M8_Alt'!AC62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AC24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AC62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ac24_1 = Dashboard_M8_Alt.AC24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, ac24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AD62():
    # 'Dashboard_M8_Alt'!AD62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AD24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AD62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ad24_1 = Dashboard_M8_Alt.AD24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, ad24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AE62():
    # 'Dashboard_M8_Alt'!AE62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AE24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AE62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ae24_1 = Dashboard_M8_Alt.AE24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, ae24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AF62():
    # 'Dashboard_M8_Alt'!AF62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AF24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AF62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        af24_1 = Dashboard_M8_Alt.AF24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, af24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AG62():
    # 'Dashboard_M8_Alt'!AG62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AG24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AG62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ag24_1 = Dashboard_M8_Alt.AG24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, ag24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AH62():
    # 'Dashboard_M8_Alt'!AH62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AH24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AH62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ah24_1 = Dashboard_M8_Alt.AH24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, ah24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AI62():
    # 'Dashboard_M8_Alt'!AI62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AI24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AI62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ai24_1 = Dashboard_M8_Alt.AI24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, ai24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ62():
    # 'Dashboard_M8_Alt'!AJ62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AJ24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AJ62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        aj24_1 = Dashboard_M8_Alt.AJ24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, aj24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class AK62():
    # 'Dashboard_M8_Alt'!AK62
    value = "#N/A"
    formula = "=SUMIF('EIA Consumption'!$E$2:$CD$2,'Dashboard M8 Alt'!AK24,'EIA Consumption'!$E$22:$CD$22)*1000"
    @eval_fn
    def AK62():
        range_1 = EIA_Consumption(5, 2, 82, 2)
        ak24_1 = Dashboard_M8_Alt.AK24()
        range_2 = EIA_Consumption(5, 22, 82, 22)
        var_1 = SUMIF(range_1, ak24_1, range_2)
        var_2 = mult(var_1, 1000)
        return var_2

@register(Dashboard_M8_Alt)
class B63():
    # 'Dashboard_M8_Alt'!B63
    value = "All Fuels"

@register(Dashboard_M8_Alt)
class C63():
    # 'Dashboard_M8_Alt'!C63
    value = "Billion Btu"

@register(Dashboard_M8_Alt)
class I63():
    # 'Dashboard_M8_Alt'!I63
    value = 107433000
    formula = "=SUM(I59:I62)"
    @eval_fn
    def I63():
        range_1 = Dashboard_M8_Alt(9, 59, 9, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class J63():
    # 'Dashboard_M8_Alt'!J63
    value = 99170000
    formula = "=SUM(J59:J62)"
    @eval_fn
    def J63():
        range_1 = Dashboard_M8_Alt(10, 59, 10, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class K63():
    # 'Dashboard_M8_Alt'!K63
    value = 103010000
    formula = "=SUM(K59:K62)"
    @eval_fn
    def K63():
        range_1 = Dashboard_M8_Alt(11, 59, 11, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class L63():
    # 'Dashboard_M8_Alt'!L63
    value = 102668000
    formula = "=SUM(L59:L62)"
    @eval_fn
    def L63():
        range_1 = Dashboard_M8_Alt(12, 59, 12, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class M63():
    # 'Dashboard_M8_Alt'!M63
    value = 102474000
    formula = "=SUM(M59:M62)"
    @eval_fn
    def M63():
        range_1 = Dashboard_M8_Alt(13, 59, 13, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class N63():
    # 'Dashboard_M8_Alt'!N63
    value = 102517000
    formula = "=SUM(N59:N62)"
    @eval_fn
    def N63():
        range_1 = Dashboard_M8_Alt(14, 59, 14, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class O63():
    # 'Dashboard_M8_Alt'!O63
    value = 99875000
    formula = "=SUM(O59:O62)"
    @eval_fn
    def O63():
        range_1 = Dashboard_M8_Alt(15, 59, 15, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class P63():
    # 'Dashboard_M8_Alt'!P63
    value = 97329000
    formula = "=SUM(P59:P62)"
    @eval_fn
    def P63():
        range_1 = Dashboard_M8_Alt(16, 59, 16, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q63():
    # 'Dashboard_M8_Alt'!Q63
    value = 93942000
    formula = "=SUM(Q59:Q62)"
    @eval_fn
    def Q63():
        range_1 = Dashboard_M8_Alt(17, 59, 17, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class R63():
    # 'Dashboard_M8_Alt'!R63
    value = 92432000
    formula = "=SUM(R59:R62)"
    @eval_fn
    def R63():
        range_1 = Dashboard_M8_Alt(18, 59, 18, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class S63():
    # 'Dashboard_M8_Alt'!S63
    value = 87725000
    formula = "=SUM(S59:S62)"
    @eval_fn
    def S63():
        range_1 = Dashboard_M8_Alt(19, 59, 19, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class T63():
    # 'Dashboard_M8_Alt'!T63
    value = 83891000
    formula = "=SUM(T59:T62)"
    @eval_fn
    def T63():
        range_1 = Dashboard_M8_Alt(20, 59, 20, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class U63():
    # 'Dashboard_M8_Alt'!U63
    value = "#N/A"
    formula = "=SUM(U59:U62)"
    @eval_fn
    def U63():
        range_1 = Dashboard_M8_Alt(21, 59, 21, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class V63():
    # 'Dashboard_M8_Alt'!V63
    value = "#N/A"
    formula = "=SUM(V59:V62)"
    @eval_fn
    def V63():
        range_1 = Dashboard_M8_Alt(22, 59, 22, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class W63():
    # 'Dashboard_M8_Alt'!W63
    value = "#N/A"
    formula = "=SUM(W59:W62)"
    @eval_fn
    def W63():
        range_1 = Dashboard_M8_Alt(23, 59, 23, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class X63():
    # 'Dashboard_M8_Alt'!X63
    value = "#N/A"
    formula = "=SUM(X59:X62)"
    @eval_fn
    def X63():
        range_1 = Dashboard_M8_Alt(24, 59, 24, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y63():
    # 'Dashboard_M8_Alt'!Y63
    value = "#N/A"
    formula = "=SUM(Y59:Y62)"
    @eval_fn
    def Y63():
        range_1 = Dashboard_M8_Alt(25, 59, 25, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z63():
    # 'Dashboard_M8_Alt'!Z63
    value = "#N/A"
    formula = "=SUM(Z59:Z62)"
    @eval_fn
    def Z63():
        range_1 = Dashboard_M8_Alt(26, 59, 26, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA63():
    # 'Dashboard_M8_Alt'!AA63
    value = "#N/A"
    formula = "=SUM(AA59:AA62)"
    @eval_fn
    def AA63():
        range_1 = Dashboard_M8_Alt(27, 59, 27, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB63():
    # 'Dashboard_M8_Alt'!AB63
    value = "#N/A"
    formula = "=SUM(AB59:AB62)"
    @eval_fn
    def AB63():
        range_1 = Dashboard_M8_Alt(28, 59, 28, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC63():
    # 'Dashboard_M8_Alt'!AC63
    value = "#N/A"
    formula = "=SUM(AC59:AC62)"
    @eval_fn
    def AC63():
        range_1 = Dashboard_M8_Alt(29, 59, 29, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD63():
    # 'Dashboard_M8_Alt'!AD63
    value = "#N/A"
    formula = "=SUM(AD59:AD62)"
    @eval_fn
    def AD63():
        range_1 = Dashboard_M8_Alt(30, 59, 30, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE63():
    # 'Dashboard_M8_Alt'!AE63
    value = "#N/A"
    formula = "=SUM(AE59:AE62)"
    @eval_fn
    def AE63():
        range_1 = Dashboard_M8_Alt(31, 59, 31, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF63():
    # 'Dashboard_M8_Alt'!AF63
    value = "#N/A"
    formula = "=SUM(AF59:AF62)"
    @eval_fn
    def AF63():
        range_1 = Dashboard_M8_Alt(32, 59, 32, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG63():
    # 'Dashboard_M8_Alt'!AG63
    value = "#N/A"
    formula = "=SUM(AG59:AG62)"
    @eval_fn
    def AG63():
        range_1 = Dashboard_M8_Alt(33, 59, 33, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH63():
    # 'Dashboard_M8_Alt'!AH63
    value = "#N/A"
    formula = "=SUM(AH59:AH62)"
    @eval_fn
    def AH63():
        range_1 = Dashboard_M8_Alt(34, 59, 34, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI63():
    # 'Dashboard_M8_Alt'!AI63
    value = "#N/A"
    formula = "=SUM(AI59:AI62)"
    @eval_fn
    def AI63():
        range_1 = Dashboard_M8_Alt(35, 59, 35, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ63():
    # 'Dashboard_M8_Alt'!AJ63
    value = "#N/A"
    formula = "=SUM(AJ59:AJ62)"
    @eval_fn
    def AJ63():
        range_1 = Dashboard_M8_Alt(36, 59, 36, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK63():
    # 'Dashboard_M8_Alt'!AK63
    value = "#N/A"
    formula = "=SUM(AK59:AK62)"
    @eval_fn
    def AK63():
        range_1 = Dashboard_M8_Alt(37, 59, 37, 62)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class A65():
    # 'Dashboard_M8_Alt'!A65
    value = "Variabl AFE(Actual,y,p,f): Actual Fuel Expenditure for Power Sector by Year and Fuel"

@register(Dashboard_M8_Alt)
class B66():
    # 'Dashboard_M8_Alt'!B66
    value = "Diesel"

@register(Dashboard_M8_Alt)
class C66():
    # 'Dashboard_M8_Alt'!C66
    value = "Million Dollars"

@register(Dashboard_M8_Alt)
class I66():
    # 'Dashboard_M8_Alt'!I66
    value = 132.83556
    formula = "=I44*I59/1000000"
    @eval_fn
    def I66():
        i44_1 = Dashboard_M8_Alt.I44()
        i59_1 = Dashboard_M8_Alt.I59()
        var_1 = mult(i44_1, i59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class J66():
    # 'Dashboard_M8_Alt'!J66
    value = 100.22369
    formula = "=J44*J59/1000000"
    @eval_fn
    def J66():
        j44_1 = Dashboard_M8_Alt.J44()
        j59_1 = Dashboard_M8_Alt.J59()
        var_1 = mult(j44_1, j59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class K66():
    # 'Dashboard_M8_Alt'!K66
    value = 129.90354
    formula = "=K44*K59/1000000"
    @eval_fn
    def K66():
        k44_1 = Dashboard_M8_Alt.K44()
        k59_1 = Dashboard_M8_Alt.K59()
        var_1 = mult(k44_1, k59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class L66():
    # 'Dashboard_M8_Alt'!L66
    value = 154.44378
    formula = "=L44*L59/1000000"
    @eval_fn
    def L66():
        l44_1 = Dashboard_M8_Alt.L44()
        l59_1 = Dashboard_M8_Alt.L59()
        var_1 = mult(l44_1, l59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class M66():
    # 'Dashboard_M8_Alt'!M66
    value = 220.3518
    formula = "=M44*M59/1000000"
    @eval_fn
    def M66():
        m44_1 = Dashboard_M8_Alt.M44()
        m59_1 = Dashboard_M8_Alt.M59()
        var_1 = mult(m44_1, m59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class N66():
    # 'Dashboard_M8_Alt'!N66
    value = 218.11168
    formula = "=N44*N59/1000000"
    @eval_fn
    def N66():
        n44_1 = Dashboard_M8_Alt.N44()
        n59_1 = Dashboard_M8_Alt.N59()
        var_1 = mult(n44_1, n59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class O66():
    # 'Dashboard_M8_Alt'!O66
    value = 292.85946
    formula = "=O44*O59/1000000"
    @eval_fn
    def O66():
        o44_1 = Dashboard_M8_Alt.O44()
        o59_1 = Dashboard_M8_Alt.O59()
        var_1 = mult(o44_1, o59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class P66():
    # 'Dashboard_M8_Alt'!P66
    value = 179.95911
    formula = "=P44*P59/1000000"
    @eval_fn
    def P66():
        p44_1 = Dashboard_M8_Alt.P44()
        p59_1 = Dashboard_M8_Alt.P59()
        var_1 = mult(p44_1, p59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Q66():
    # 'Dashboard_M8_Alt'!Q66
    value = 228.29835
    formula = "=Q44*Q59/1000000"
    @eval_fn
    def Q66():
        q44_1 = Dashboard_M8_Alt.Q44()
        q59_1 = Dashboard_M8_Alt.Q59()
        var_1 = mult(q44_1, q59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class R66():
    # 'Dashboard_M8_Alt'!R66
    value = 310.79402
    formula = "=R44*R59/1000000"
    @eval_fn
    def R66():
        r44_1 = Dashboard_M8_Alt.R44()
        r59_1 = Dashboard_M8_Alt.R59()
        var_1 = mult(r44_1, r59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class S66():
    # 'Dashboard_M8_Alt'!S66
    value = 313.53609
    formula = "=S44*S59/1000000"
    @eval_fn
    def S66():
        s44_1 = Dashboard_M8_Alt.S44()
        s59_1 = Dashboard_M8_Alt.S59()
        var_1 = mult(s44_1, s59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class T66():
    # 'Dashboard_M8_Alt'!T66
    value = 285.31131
    formula = "=T44*T59/1000000"
    @eval_fn
    def T66():
        t44_1 = Dashboard_M8_Alt.T44()
        t59_1 = Dashboard_M8_Alt.T59()
        var_1 = mult(t44_1, t59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class U66():
    # 'Dashboard_M8_Alt'!U66
    value = "#N/A"
    formula = "=U44*U59/1000000"
    @eval_fn
    def U66():
        u44_1 = Dashboard_M8_Alt.U44()
        u59_1 = Dashboard_M8_Alt.U59()
        var_1 = mult(u44_1, u59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class V66():
    # 'Dashboard_M8_Alt'!V66
    value = "#N/A"
    formula = "=V44*V59/1000000"
    @eval_fn
    def V66():
        v44_1 = Dashboard_M8_Alt.V44()
        v59_1 = Dashboard_M8_Alt.V59()
        var_1 = mult(v44_1, v59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class W66():
    # 'Dashboard_M8_Alt'!W66
    value = "#N/A"
    formula = "=W44*W59/1000000"
    @eval_fn
    def W66():
        w44_1 = Dashboard_M8_Alt.W44()
        w59_1 = Dashboard_M8_Alt.W59()
        var_1 = mult(w44_1, w59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class X66():
    # 'Dashboard_M8_Alt'!X66
    value = "#N/A"
    formula = "=X44*X59/1000000"
    @eval_fn
    def X66():
        x44_1 = Dashboard_M8_Alt.X44()
        x59_1 = Dashboard_M8_Alt.X59()
        var_1 = mult(x44_1, x59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Y66():
    # 'Dashboard_M8_Alt'!Y66
    value = "#N/A"
    formula = "=Y44*Y59/1000000"
    @eval_fn
    def Y66():
        y44_1 = Dashboard_M8_Alt.Y44()
        y59_1 = Dashboard_M8_Alt.Y59()
        var_1 = mult(y44_1, y59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Z66():
    # 'Dashboard_M8_Alt'!Z66
    value = "#N/A"
    formula = "=Z44*Z59/1000000"
    @eval_fn
    def Z66():
        z44_1 = Dashboard_M8_Alt.Z44()
        z59_1 = Dashboard_M8_Alt.Z59()
        var_1 = mult(z44_1, z59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AA66():
    # 'Dashboard_M8_Alt'!AA66
    value = "#N/A"
    formula = "=AA44*AA59/1000000"
    @eval_fn
    def AA66():
        aa44_1 = Dashboard_M8_Alt.AA44()
        aa59_1 = Dashboard_M8_Alt.AA59()
        var_1 = mult(aa44_1, aa59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AB66():
    # 'Dashboard_M8_Alt'!AB66
    value = "#N/A"
    formula = "=AB44*AB59/1000000"
    @eval_fn
    def AB66():
        ab44_1 = Dashboard_M8_Alt.AB44()
        ab59_1 = Dashboard_M8_Alt.AB59()
        var_1 = mult(ab44_1, ab59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AC66():
    # 'Dashboard_M8_Alt'!AC66
    value = "#N/A"
    formula = "=AC44*AC59/1000000"
    @eval_fn
    def AC66():
        ac44_1 = Dashboard_M8_Alt.AC44()
        ac59_1 = Dashboard_M8_Alt.AC59()
        var_1 = mult(ac44_1, ac59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AD66():
    # 'Dashboard_M8_Alt'!AD66
    value = "#N/A"
    formula = "=AD44*AD59/1000000"
    @eval_fn
    def AD66():
        ad44_1 = Dashboard_M8_Alt.AD44()
        ad59_1 = Dashboard_M8_Alt.AD59()
        var_1 = mult(ad44_1, ad59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AE66():
    # 'Dashboard_M8_Alt'!AE66
    value = "#N/A"
    formula = "=AE44*AE59/1000000"
    @eval_fn
    def AE66():
        ae44_1 = Dashboard_M8_Alt.AE44()
        ae59_1 = Dashboard_M8_Alt.AE59()
        var_1 = mult(ae44_1, ae59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AF66():
    # 'Dashboard_M8_Alt'!AF66
    value = "#N/A"
    formula = "=AF44*AF59/1000000"
    @eval_fn
    def AF66():
        af44_1 = Dashboard_M8_Alt.AF44()
        af59_1 = Dashboard_M8_Alt.AF59()
        var_1 = mult(af44_1, af59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AG66():
    # 'Dashboard_M8_Alt'!AG66
    value = "#N/A"
    formula = "=AG44*AG59/1000000"
    @eval_fn
    def AG66():
        ag44_1 = Dashboard_M8_Alt.AG44()
        ag59_1 = Dashboard_M8_Alt.AG59()
        var_1 = mult(ag44_1, ag59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AH66():
    # 'Dashboard_M8_Alt'!AH66
    value = "#N/A"
    formula = "=AH44*AH59/1000000"
    @eval_fn
    def AH66():
        ah44_1 = Dashboard_M8_Alt.AH44()
        ah59_1 = Dashboard_M8_Alt.AH59()
        var_1 = mult(ah44_1, ah59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AI66():
    # 'Dashboard_M8_Alt'!AI66
    value = "#N/A"
    formula = "=AI44*AI59/1000000"
    @eval_fn
    def AI66():
        ai44_1 = Dashboard_M8_Alt.AI44()
        ai59_1 = Dashboard_M8_Alt.AI59()
        var_1 = mult(ai44_1, ai59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ66():
    # 'Dashboard_M8_Alt'!AJ66
    value = "#N/A"
    formula = "=AJ44*AJ59/1000000"
    @eval_fn
    def AJ66():
        aj44_1 = Dashboard_M8_Alt.AJ44()
        aj59_1 = Dashboard_M8_Alt.AJ59()
        var_1 = mult(aj44_1, aj59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AK66():
    # 'Dashboard_M8_Alt'!AK66
    value = "#N/A"
    formula = "=AK44*AK59/1000000"
    @eval_fn
    def AK66():
        ak44_1 = Dashboard_M8_Alt.AK44()
        ak59_1 = Dashboard_M8_Alt.AK59()
        var_1 = mult(ak44_1, ak59_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class B67():
    # 'Dashboard_M8_Alt'!B67
    value = "Fuel Oil"

@register(Dashboard_M8_Alt)
class C67():
    # 'Dashboard_M8_Alt'!C67
    value = "Million Dollars"

@register(Dashboard_M8_Alt)
class I67():
    # 'Dashboard_M8_Alt'!I67
    value = 332.36289
    formula = "=I45*I60/1000000"
    @eval_fn
    def I67():
        i45_1 = Dashboard_M8_Alt.I45()
        i60_1 = Dashboard_M8_Alt.I60()
        var_1 = mult(i45_1, i60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class J67():
    # 'Dashboard_M8_Alt'!J67
    value = 330.70709
    formula = "=J45*J60/1000000"
    @eval_fn
    def J67():
        j45_1 = Dashboard_M8_Alt.J45()
        j60_1 = Dashboard_M8_Alt.J60()
        var_1 = mult(j45_1, j60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class K67():
    # 'Dashboard_M8_Alt'!K67
    value = 355.45608
    formula = "=K45*K60/1000000"
    @eval_fn
    def K67():
        k45_1 = Dashboard_M8_Alt.K45()
        k60_1 = Dashboard_M8_Alt.K60()
        var_1 = mult(k45_1, k60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class L67():
    # 'Dashboard_M8_Alt'!L67
    value = 617.5983
    formula = "=L45*L60/1000000"
    @eval_fn
    def L67():
        l45_1 = Dashboard_M8_Alt.L45()
        l60_1 = Dashboard_M8_Alt.L60()
        var_1 = mult(l45_1, l60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class M67():
    # 'Dashboard_M8_Alt'!M67
    value = 714.99755
    formula = "=M45*M60/1000000"
    @eval_fn
    def M67():
        m45_1 = Dashboard_M8_Alt.M45()
        m60_1 = Dashboard_M8_Alt.M60()
        var_1 = mult(m45_1, m60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class N67():
    # 'Dashboard_M8_Alt'!N67
    value = 785.84208
    formula = "=N45*N60/1000000"
    @eval_fn
    def N67():
        n45_1 = Dashboard_M8_Alt.N45()
        n60_1 = Dashboard_M8_Alt.N60()
        var_1 = mult(n45_1, n60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class O67():
    # 'Dashboard_M8_Alt'!O67
    value = 1122.00757
    formula = "=O45*O60/1000000"
    @eval_fn
    def O67():
        o45_1 = Dashboard_M8_Alt.O45()
        o60_1 = Dashboard_M8_Alt.O60()
        var_1 = mult(o45_1, o60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class P67():
    # 'Dashboard_M8_Alt'!P67
    value = 634.61071
    formula = "=P45*P60/1000000"
    @eval_fn
    def P67():
        p45_1 = Dashboard_M8_Alt.P45()
        p60_1 = Dashboard_M8_Alt.P60()
        var_1 = mult(p45_1, p60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Q67():
    # 'Dashboard_M8_Alt'!Q67
    value = 878.96793
    formula = "=Q45*Q60/1000000"
    @eval_fn
    def Q67():
        q45_1 = Dashboard_M8_Alt.Q45()
        q60_1 = Dashboard_M8_Alt.Q60()
        var_1 = mult(q45_1, q60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class R67():
    # 'Dashboard_M8_Alt'!R67
    value = 1258.47392
    formula = "=R45*R60/1000000"
    @eval_fn
    def R67():
        r45_1 = Dashboard_M8_Alt.R45()
        r60_1 = Dashboard_M8_Alt.R60()
        var_1 = mult(r45_1, r60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class S67():
    # 'Dashboard_M8_Alt'!S67
    value = 1276.68354
    formula = "=S45*S60/1000000"
    @eval_fn
    def S67():
        s45_1 = Dashboard_M8_Alt.S45()
        s60_1 = Dashboard_M8_Alt.S60()
        var_1 = mult(s45_1, s60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class T67():
    # 'Dashboard_M8_Alt'!T67
    value = 1169.2292
    formula = "=T45*T60/1000000"
    @eval_fn
    def T67():
        t45_1 = Dashboard_M8_Alt.T45()
        t60_1 = Dashboard_M8_Alt.T60()
        var_1 = mult(t45_1, t60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class U67():
    # 'Dashboard_M8_Alt'!U67
    value = "#N/A"
    formula = "=U45*U60/1000000"
    @eval_fn
    def U67():
        u45_1 = Dashboard_M8_Alt.U45()
        u60_1 = Dashboard_M8_Alt.U60()
        var_1 = mult(u45_1, u60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class V67():
    # 'Dashboard_M8_Alt'!V67
    value = "#N/A"
    formula = "=V45*V60/1000000"
    @eval_fn
    def V67():
        v45_1 = Dashboard_M8_Alt.V45()
        v60_1 = Dashboard_M8_Alt.V60()
        var_1 = mult(v45_1, v60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class W67():
    # 'Dashboard_M8_Alt'!W67
    value = "#N/A"
    formula = "=W45*W60/1000000"
    @eval_fn
    def W67():
        w45_1 = Dashboard_M8_Alt.W45()
        w60_1 = Dashboard_M8_Alt.W60()
        var_1 = mult(w45_1, w60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class X67():
    # 'Dashboard_M8_Alt'!X67
    value = "#N/A"
    formula = "=X45*X60/1000000"
    @eval_fn
    def X67():
        x45_1 = Dashboard_M8_Alt.X45()
        x60_1 = Dashboard_M8_Alt.X60()
        var_1 = mult(x45_1, x60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Y67():
    # 'Dashboard_M8_Alt'!Y67
    value = "#N/A"
    formula = "=Y45*Y60/1000000"
    @eval_fn
    def Y67():
        y45_1 = Dashboard_M8_Alt.Y45()
        y60_1 = Dashboard_M8_Alt.Y60()
        var_1 = mult(y45_1, y60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Z67():
    # 'Dashboard_M8_Alt'!Z67
    value = "#N/A"
    formula = "=Z45*Z60/1000000"
    @eval_fn
    def Z67():
        z45_1 = Dashboard_M8_Alt.Z45()
        z60_1 = Dashboard_M8_Alt.Z60()
        var_1 = mult(z45_1, z60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AA67():
    # 'Dashboard_M8_Alt'!AA67
    value = "#N/A"
    formula = "=AA45*AA60/1000000"
    @eval_fn
    def AA67():
        aa45_1 = Dashboard_M8_Alt.AA45()
        aa60_1 = Dashboard_M8_Alt.AA60()
        var_1 = mult(aa45_1, aa60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AB67():
    # 'Dashboard_M8_Alt'!AB67
    value = "#N/A"
    formula = "=AB45*AB60/1000000"
    @eval_fn
    def AB67():
        ab45_1 = Dashboard_M8_Alt.AB45()
        ab60_1 = Dashboard_M8_Alt.AB60()
        var_1 = mult(ab45_1, ab60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AC67():
    # 'Dashboard_M8_Alt'!AC67
    value = "#N/A"
    formula = "=AC45*AC60/1000000"
    @eval_fn
    def AC67():
        ac45_1 = Dashboard_M8_Alt.AC45()
        ac60_1 = Dashboard_M8_Alt.AC60()
        var_1 = mult(ac45_1, ac60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AD67():
    # 'Dashboard_M8_Alt'!AD67
    value = "#N/A"
    formula = "=AD45*AD60/1000000"
    @eval_fn
    def AD67():
        ad45_1 = Dashboard_M8_Alt.AD45()
        ad60_1 = Dashboard_M8_Alt.AD60()
        var_1 = mult(ad45_1, ad60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AE67():
    # 'Dashboard_M8_Alt'!AE67
    value = "#N/A"
    formula = "=AE45*AE60/1000000"
    @eval_fn
    def AE67():
        ae45_1 = Dashboard_M8_Alt.AE45()
        ae60_1 = Dashboard_M8_Alt.AE60()
        var_1 = mult(ae45_1, ae60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AF67():
    # 'Dashboard_M8_Alt'!AF67
    value = "#N/A"
    formula = "=AF45*AF60/1000000"
    @eval_fn
    def AF67():
        af45_1 = Dashboard_M8_Alt.AF45()
        af60_1 = Dashboard_M8_Alt.AF60()
        var_1 = mult(af45_1, af60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AG67():
    # 'Dashboard_M8_Alt'!AG67
    value = "#N/A"
    formula = "=AG45*AG60/1000000"
    @eval_fn
    def AG67():
        ag45_1 = Dashboard_M8_Alt.AG45()
        ag60_1 = Dashboard_M8_Alt.AG60()
        var_1 = mult(ag45_1, ag60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AH67():
    # 'Dashboard_M8_Alt'!AH67
    value = "#N/A"
    formula = "=AH45*AH60/1000000"
    @eval_fn
    def AH67():
        ah45_1 = Dashboard_M8_Alt.AH45()
        ah60_1 = Dashboard_M8_Alt.AH60()
        var_1 = mult(ah45_1, ah60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AI67():
    # 'Dashboard_M8_Alt'!AI67
    value = "#N/A"
    formula = "=AI45*AI60/1000000"
    @eval_fn
    def AI67():
        ai45_1 = Dashboard_M8_Alt.AI45()
        ai60_1 = Dashboard_M8_Alt.AI60()
        var_1 = mult(ai45_1, ai60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ67():
    # 'Dashboard_M8_Alt'!AJ67
    value = "#N/A"
    formula = "=AJ45*AJ60/1000000"
    @eval_fn
    def AJ67():
        aj45_1 = Dashboard_M8_Alt.AJ45()
        aj60_1 = Dashboard_M8_Alt.AJ60()
        var_1 = mult(aj45_1, aj60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AK67():
    # 'Dashboard_M8_Alt'!AK67
    value = "#N/A"
    formula = "=AK45*AK60/1000000"
    @eval_fn
    def AK67():
        ak45_1 = Dashboard_M8_Alt.AK45()
        ak60_1 = Dashboard_M8_Alt.AK60()
        var_1 = mult(ak45_1, ak60_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class B68():
    # 'Dashboard_M8_Alt'!B68
    value = "SNG"

@register(Dashboard_M8_Alt)
class C68():
    # 'Dashboard_M8_Alt'!C68
    value = "Million Dollars"

@register(Dashboard_M8_Alt)
class I68():
    # 'Dashboard_M8_Alt'!I68
    value = 0
    formula = "=I46*I61/1000000"
    @eval_fn
    def I68():
        i46_1 = Dashboard_M8_Alt.I46()
        i61_1 = Dashboard_M8_Alt.I61()
        var_1 = mult(i46_1, i61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class J68():
    # 'Dashboard_M8_Alt'!J68
    value = 0
    formula = "=J46*J61/1000000"
    @eval_fn
    def J68():
        j46_1 = Dashboard_M8_Alt.J46()
        j61_1 = Dashboard_M8_Alt.J61()
        var_1 = mult(j46_1, j61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class K68():
    # 'Dashboard_M8_Alt'!K68
    value = 0
    formula = "=K46*K61/1000000"
    @eval_fn
    def K68():
        k46_1 = Dashboard_M8_Alt.K46()
        k61_1 = Dashboard_M8_Alt.K61()
        var_1 = mult(k46_1, k61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class L68():
    # 'Dashboard_M8_Alt'!L68
    value = 0
    formula = "=L46*L61/1000000"
    @eval_fn
    def L68():
        l46_1 = Dashboard_M8_Alt.L46()
        l61_1 = Dashboard_M8_Alt.L61()
        var_1 = mult(l46_1, l61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class M68():
    # 'Dashboard_M8_Alt'!M68
    value = 0
    formula = "=M46*M61/1000000"
    @eval_fn
    def M68():
        m46_1 = Dashboard_M8_Alt.M46()
        m61_1 = Dashboard_M8_Alt.M61()
        var_1 = mult(m46_1, m61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class N68():
    # 'Dashboard_M8_Alt'!N68
    value = 0
    formula = "=N46*N61/1000000"
    @eval_fn
    def N68():
        n46_1 = Dashboard_M8_Alt.N46()
        n61_1 = Dashboard_M8_Alt.N61()
        var_1 = mult(n46_1, n61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class O68():
    # 'Dashboard_M8_Alt'!O68
    value = 0
    formula = "=O46*O61/1000000"
    @eval_fn
    def O68():
        o46_1 = Dashboard_M8_Alt.O46()
        o61_1 = Dashboard_M8_Alt.O61()
        var_1 = mult(o46_1, o61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class P68():
    # 'Dashboard_M8_Alt'!P68
    value = 0
    formula = "=P46*P61/1000000"
    @eval_fn
    def P68():
        p46_1 = Dashboard_M8_Alt.P46()
        p61_1 = Dashboard_M8_Alt.P61()
        var_1 = mult(p46_1, p61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Q68():
    # 'Dashboard_M8_Alt'!Q68
    value = 0
    formula = "=Q46*Q61/1000000"
    @eval_fn
    def Q68():
        q46_1 = Dashboard_M8_Alt.Q46()
        q61_1 = Dashboard_M8_Alt.Q61()
        var_1 = mult(q46_1, q61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class R68():
    # 'Dashboard_M8_Alt'!R68
    value = 0
    formula = "=R46*R61/1000000"
    @eval_fn
    def R68():
        r46_1 = Dashboard_M8_Alt.R46()
        r61_1 = Dashboard_M8_Alt.R61()
        var_1 = mult(r46_1, r61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class S68():
    # 'Dashboard_M8_Alt'!S68
    value = 0
    formula = "=S46*S61/1000000"
    @eval_fn
    def S68():
        s46_1 = Dashboard_M8_Alt.S46()
        s61_1 = Dashboard_M8_Alt.S61()
        var_1 = mult(s46_1, s61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class T68():
    # 'Dashboard_M8_Alt'!T68
    value = 0
    formula = "=T46*T61/1000000"
    @eval_fn
    def T68():
        t46_1 = Dashboard_M8_Alt.T46()
        t61_1 = Dashboard_M8_Alt.T61()
        var_1 = mult(t46_1, t61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class U68():
    # 'Dashboard_M8_Alt'!U68
    value = "#N/A"
    formula = "=U46*U61/1000000"
    @eval_fn
    def U68():
        u46_1 = Dashboard_M8_Alt.U46()
        u61_1 = Dashboard_M8_Alt.U61()
        var_1 = mult(u46_1, u61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class V68():
    # 'Dashboard_M8_Alt'!V68
    value = "#N/A"
    formula = "=V46*V61/1000000"
    @eval_fn
    def V68():
        v46_1 = Dashboard_M8_Alt.V46()
        v61_1 = Dashboard_M8_Alt.V61()
        var_1 = mult(v46_1, v61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class W68():
    # 'Dashboard_M8_Alt'!W68
    value = "#N/A"
    formula = "=W46*W61/1000000"
    @eval_fn
    def W68():
        w46_1 = Dashboard_M8_Alt.W46()
        w61_1 = Dashboard_M8_Alt.W61()
        var_1 = mult(w46_1, w61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class X68():
    # 'Dashboard_M8_Alt'!X68
    value = "#N/A"
    formula = "=X46*X61/1000000"
    @eval_fn
    def X68():
        x46_1 = Dashboard_M8_Alt.X46()
        x61_1 = Dashboard_M8_Alt.X61()
        var_1 = mult(x46_1, x61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Y68():
    # 'Dashboard_M8_Alt'!Y68
    value = "#N/A"
    formula = "=Y46*Y61/1000000"
    @eval_fn
    def Y68():
        y46_1 = Dashboard_M8_Alt.Y46()
        y61_1 = Dashboard_M8_Alt.Y61()
        var_1 = mult(y46_1, y61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Z68():
    # 'Dashboard_M8_Alt'!Z68
    value = "#N/A"
    formula = "=Z46*Z61/1000000"
    @eval_fn
    def Z68():
        z46_1 = Dashboard_M8_Alt.Z46()
        z61_1 = Dashboard_M8_Alt.Z61()
        var_1 = mult(z46_1, z61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AA68():
    # 'Dashboard_M8_Alt'!AA68
    value = "#N/A"
    formula = "=AA46*AA61/1000000"
    @eval_fn
    def AA68():
        aa46_1 = Dashboard_M8_Alt.AA46()
        aa61_1 = Dashboard_M8_Alt.AA61()
        var_1 = mult(aa46_1, aa61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AB68():
    # 'Dashboard_M8_Alt'!AB68
    value = "#N/A"
    formula = "=AB46*AB61/1000000"
    @eval_fn
    def AB68():
        ab46_1 = Dashboard_M8_Alt.AB46()
        ab61_1 = Dashboard_M8_Alt.AB61()
        var_1 = mult(ab46_1, ab61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AC68():
    # 'Dashboard_M8_Alt'!AC68
    value = "#N/A"
    formula = "=AC46*AC61/1000000"
    @eval_fn
    def AC68():
        ac46_1 = Dashboard_M8_Alt.AC46()
        ac61_1 = Dashboard_M8_Alt.AC61()
        var_1 = mult(ac46_1, ac61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AD68():
    # 'Dashboard_M8_Alt'!AD68
    value = "#N/A"
    formula = "=AD46*AD61/1000000"
    @eval_fn
    def AD68():
        ad46_1 = Dashboard_M8_Alt.AD46()
        ad61_1 = Dashboard_M8_Alt.AD61()
        var_1 = mult(ad46_1, ad61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AE68():
    # 'Dashboard_M8_Alt'!AE68
    value = "#N/A"
    formula = "=AE46*AE61/1000000"
    @eval_fn
    def AE68():
        ae46_1 = Dashboard_M8_Alt.AE46()
        ae61_1 = Dashboard_M8_Alt.AE61()
        var_1 = mult(ae46_1, ae61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AF68():
    # 'Dashboard_M8_Alt'!AF68
    value = "#N/A"
    formula = "=AF46*AF61/1000000"
    @eval_fn
    def AF68():
        af46_1 = Dashboard_M8_Alt.AF46()
        af61_1 = Dashboard_M8_Alt.AF61()
        var_1 = mult(af46_1, af61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AG68():
    # 'Dashboard_M8_Alt'!AG68
    value = "#N/A"
    formula = "=AG46*AG61/1000000"
    @eval_fn
    def AG68():
        ag46_1 = Dashboard_M8_Alt.AG46()
        ag61_1 = Dashboard_M8_Alt.AG61()
        var_1 = mult(ag46_1, ag61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AH68():
    # 'Dashboard_M8_Alt'!AH68
    value = "#N/A"
    formula = "=AH46*AH61/1000000"
    @eval_fn
    def AH68():
        ah46_1 = Dashboard_M8_Alt.AH46()
        ah61_1 = Dashboard_M8_Alt.AH61()
        var_1 = mult(ah46_1, ah61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AI68():
    # 'Dashboard_M8_Alt'!AI68
    value = "#N/A"
    formula = "=AI46*AI61/1000000"
    @eval_fn
    def AI68():
        ai46_1 = Dashboard_M8_Alt.AI46()
        ai61_1 = Dashboard_M8_Alt.AI61()
        var_1 = mult(ai46_1, ai61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ68():
    # 'Dashboard_M8_Alt'!AJ68
    value = "#N/A"
    formula = "=AJ46*AJ61/1000000"
    @eval_fn
    def AJ68():
        aj46_1 = Dashboard_M8_Alt.AJ46()
        aj61_1 = Dashboard_M8_Alt.AJ61()
        var_1 = mult(aj46_1, aj61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AK68():
    # 'Dashboard_M8_Alt'!AK68
    value = "#N/A"
    formula = "=AK46*AK61/1000000"
    @eval_fn
    def AK68():
        ak46_1 = Dashboard_M8_Alt.AK46()
        ak61_1 = Dashboard_M8_Alt.AK61()
        var_1 = mult(ak46_1, ak61_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class B69():
    # 'Dashboard_M8_Alt'!B69
    value = "Coal"

@register(Dashboard_M8_Alt)
class C69():
    # 'Dashboard_M8_Alt'!C69
    value = "Million Dollars"

@register(Dashboard_M8_Alt)
class I69():
    # 'Dashboard_M8_Alt'!I69
    value = 25.5408
    formula = "=I47*I62/1000000"
    @eval_fn
    def I69():
        i47_1 = Dashboard_M8_Alt.I47()
        i62_1 = Dashboard_M8_Alt.I62()
        var_1 = mult(i47_1, i62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class J69():
    # 'Dashboard_M8_Alt'!J69
    value = 52.93072
    formula = "=J47*J62/1000000"
    @eval_fn
    def J69():
        j47_1 = Dashboard_M8_Alt.J47()
        j62_1 = Dashboard_M8_Alt.J62()
        var_1 = mult(j47_1, j62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class K69():
    # 'Dashboard_M8_Alt'!K69
    value = 33.84188
    formula = "=K47*K62/1000000"
    @eval_fn
    def K69():
        k47_1 = Dashboard_M8_Alt.K47()
        k62_1 = Dashboard_M8_Alt.K62()
        var_1 = mult(k47_1, k62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class L69():
    # 'Dashboard_M8_Alt'!L69
    value = 23.65935
    formula = "=L47*L62/1000000"
    @eval_fn
    def L69():
        l47_1 = Dashboard_M8_Alt.L47()
        l62_1 = Dashboard_M8_Alt.L62()
        var_1 = mult(l47_1, l62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class M69():
    # 'Dashboard_M8_Alt'!M69
    value = 26.69352
    formula = "=M47*M62/1000000"
    @eval_fn
    def M69():
        m47_1 = Dashboard_M8_Alt.M47()
        m62_1 = Dashboard_M8_Alt.M62()
        var_1 = mult(m47_1, m62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class N69():
    # 'Dashboard_M8_Alt'!N69
    value = 31.84405
    formula = "=N47*N62/1000000"
    @eval_fn
    def N69():
        n47_1 = Dashboard_M8_Alt.N47()
        n62_1 = Dashboard_M8_Alt.N62()
        var_1 = mult(n47_1, n62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class O69():
    # 'Dashboard_M8_Alt'!O69
    value = 39.08493
    formula = "=O47*O62/1000000"
    @eval_fn
    def O69():
        o47_1 = Dashboard_M8_Alt.O47()
        o62_1 = Dashboard_M8_Alt.O62()
        var_1 = mult(o47_1, o62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class P69():
    # 'Dashboard_M8_Alt'!P69
    value = 37.912
    formula = "=P47*P62/1000000"
    @eval_fn
    def P69():
        p47_1 = Dashboard_M8_Alt.P47()
        p62_1 = Dashboard_M8_Alt.P62()
        var_1 = mult(p47_1, p62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Q69():
    # 'Dashboard_M8_Alt'!Q69
    value = 34.85844
    formula = "=Q47*Q62/1000000"
    @eval_fn
    def Q69():
        q47_1 = Dashboard_M8_Alt.Q47()
        q62_1 = Dashboard_M8_Alt.Q62()
        var_1 = mult(q47_1, q62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class R69():
    # 'Dashboard_M8_Alt'!R69
    value = 24.5265
    formula = "=R47*R62/1000000"
    @eval_fn
    def R69():
        r47_1 = Dashboard_M8_Alt.R47()
        r62_1 = Dashboard_M8_Alt.R62()
        var_1 = mult(r47_1, r62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class S69():
    # 'Dashboard_M8_Alt'!S69
    value = 29.16648
    formula = "=S47*S62/1000000"
    @eval_fn
    def S69():
        s47_1 = Dashboard_M8_Alt.S47()
        s62_1 = Dashboard_M8_Alt.S62()
        var_1 = mult(s47_1, s62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class T69():
    # 'Dashboard_M8_Alt'!T69
    value = 27.33808
    formula = "=T47*T62/1000000"
    @eval_fn
    def T69():
        t47_1 = Dashboard_M8_Alt.T47()
        t62_1 = Dashboard_M8_Alt.T62()
        var_1 = mult(t47_1, t62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class U69():
    # 'Dashboard_M8_Alt'!U69
    value = "#N/A"
    formula = "=U47*U62/1000000"
    @eval_fn
    def U69():
        u47_1 = Dashboard_M8_Alt.U47()
        u62_1 = Dashboard_M8_Alt.U62()
        var_1 = mult(u47_1, u62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class V69():
    # 'Dashboard_M8_Alt'!V69
    value = "#N/A"
    formula = "=V47*V62/1000000"
    @eval_fn
    def V69():
        v47_1 = Dashboard_M8_Alt.V47()
        v62_1 = Dashboard_M8_Alt.V62()
        var_1 = mult(v47_1, v62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class W69():
    # 'Dashboard_M8_Alt'!W69
    value = "#N/A"
    formula = "=W47*W62/1000000"
    @eval_fn
    def W69():
        w47_1 = Dashboard_M8_Alt.W47()
        w62_1 = Dashboard_M8_Alt.W62()
        var_1 = mult(w47_1, w62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class X69():
    # 'Dashboard_M8_Alt'!X69
    value = "#N/A"
    formula = "=X47*X62/1000000"
    @eval_fn
    def X69():
        x47_1 = Dashboard_M8_Alt.X47()
        x62_1 = Dashboard_M8_Alt.X62()
        var_1 = mult(x47_1, x62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Y69():
    # 'Dashboard_M8_Alt'!Y69
    value = "#N/A"
    formula = "=Y47*Y62/1000000"
    @eval_fn
    def Y69():
        y47_1 = Dashboard_M8_Alt.Y47()
        y62_1 = Dashboard_M8_Alt.Y62()
        var_1 = mult(y47_1, y62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class Z69():
    # 'Dashboard_M8_Alt'!Z69
    value = "#N/A"
    formula = "=Z47*Z62/1000000"
    @eval_fn
    def Z69():
        z47_1 = Dashboard_M8_Alt.Z47()
        z62_1 = Dashboard_M8_Alt.Z62()
        var_1 = mult(z47_1, z62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AA69():
    # 'Dashboard_M8_Alt'!AA69
    value = "#N/A"
    formula = "=AA47*AA62/1000000"
    @eval_fn
    def AA69():
        aa47_1 = Dashboard_M8_Alt.AA47()
        aa62_1 = Dashboard_M8_Alt.AA62()
        var_1 = mult(aa47_1, aa62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AB69():
    # 'Dashboard_M8_Alt'!AB69
    value = "#N/A"
    formula = "=AB47*AB62/1000000"
    @eval_fn
    def AB69():
        ab47_1 = Dashboard_M8_Alt.AB47()
        ab62_1 = Dashboard_M8_Alt.AB62()
        var_1 = mult(ab47_1, ab62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AC69():
    # 'Dashboard_M8_Alt'!AC69
    value = "#N/A"
    formula = "=AC47*AC62/1000000"
    @eval_fn
    def AC69():
        ac47_1 = Dashboard_M8_Alt.AC47()
        ac62_1 = Dashboard_M8_Alt.AC62()
        var_1 = mult(ac47_1, ac62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AD69():
    # 'Dashboard_M8_Alt'!AD69
    value = "#N/A"
    formula = "=AD47*AD62/1000000"
    @eval_fn
    def AD69():
        ad47_1 = Dashboard_M8_Alt.AD47()
        ad62_1 = Dashboard_M8_Alt.AD62()
        var_1 = mult(ad47_1, ad62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AE69():
    # 'Dashboard_M8_Alt'!AE69
    value = "#N/A"
    formula = "=AE47*AE62/1000000"
    @eval_fn
    def AE69():
        ae47_1 = Dashboard_M8_Alt.AE47()
        ae62_1 = Dashboard_M8_Alt.AE62()
        var_1 = mult(ae47_1, ae62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AF69():
    # 'Dashboard_M8_Alt'!AF69
    value = "#N/A"
    formula = "=AF47*AF62/1000000"
    @eval_fn
    def AF69():
        af47_1 = Dashboard_M8_Alt.AF47()
        af62_1 = Dashboard_M8_Alt.AF62()
        var_1 = mult(af47_1, af62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AG69():
    # 'Dashboard_M8_Alt'!AG69
    value = "#N/A"
    formula = "=AG47*AG62/1000000"
    @eval_fn
    def AG69():
        ag47_1 = Dashboard_M8_Alt.AG47()
        ag62_1 = Dashboard_M8_Alt.AG62()
        var_1 = mult(ag47_1, ag62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AH69():
    # 'Dashboard_M8_Alt'!AH69
    value = "#N/A"
    formula = "=AH47*AH62/1000000"
    @eval_fn
    def AH69():
        ah47_1 = Dashboard_M8_Alt.AH47()
        ah62_1 = Dashboard_M8_Alt.AH62()
        var_1 = mult(ah47_1, ah62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AI69():
    # 'Dashboard_M8_Alt'!AI69
    value = "#N/A"
    formula = "=AI47*AI62/1000000"
    @eval_fn
    def AI69():
        ai47_1 = Dashboard_M8_Alt.AI47()
        ai62_1 = Dashboard_M8_Alt.AI62()
        var_1 = mult(ai47_1, ai62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AJ69():
    # 'Dashboard_M8_Alt'!AJ69
    value = "#N/A"
    formula = "=AJ47*AJ62/1000000"
    @eval_fn
    def AJ69():
        aj47_1 = Dashboard_M8_Alt.AJ47()
        aj62_1 = Dashboard_M8_Alt.AJ62()
        var_1 = mult(aj47_1, aj62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class AK69():
    # 'Dashboard_M8_Alt'!AK69
    value = "#N/A"
    formula = "=AK47*AK62/1000000"
    @eval_fn
    def AK69():
        ak47_1 = Dashboard_M8_Alt.AK47()
        ak62_1 = Dashboard_M8_Alt.AK62()
        var_1 = mult(ak47_1, ak62_1)
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Dashboard_M8_Alt)
class B70():
    # 'Dashboard_M8_Alt'!B70
    value = "All Fuels"

@register(Dashboard_M8_Alt)
class C70():
    # 'Dashboard_M8_Alt'!C70
    value = "Million Dollars"

@register(Dashboard_M8_Alt)
class I70():
    # 'Dashboard_M8_Alt'!I70
    value = 490.73925
    formula = "=SUM(I66:I69)"
    @eval_fn
    def I70():
        range_1 = Dashboard_M8_Alt(9, 66, 9, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class J70():
    # 'Dashboard_M8_Alt'!J70
    value = 483.8615
    formula = "=SUM(J66:J69)"
    @eval_fn
    def J70():
        range_1 = Dashboard_M8_Alt(10, 66, 10, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class K70():
    # 'Dashboard_M8_Alt'!K70
    value = 519.2015
    formula = "=SUM(K66:K69)"
    @eval_fn
    def K70():
        range_1 = Dashboard_M8_Alt(11, 66, 11, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class L70():
    # 'Dashboard_M8_Alt'!L70
    value = 795.70143
    formula = "=SUM(L66:L69)"
    @eval_fn
    def L70():
        range_1 = Dashboard_M8_Alt(12, 66, 12, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class M70():
    # 'Dashboard_M8_Alt'!M70
    value = 962.04287
    formula = "=SUM(M66:M69)"
    @eval_fn
    def M70():
        range_1 = Dashboard_M8_Alt(13, 66, 13, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class N70():
    # 'Dashboard_M8_Alt'!N70
    value = 1035.79781
    formula = "=SUM(N66:N69)"
    @eval_fn
    def N70():
        range_1 = Dashboard_M8_Alt(14, 66, 14, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class O70():
    # 'Dashboard_M8_Alt'!O70
    value = 1453.95196
    formula = "=SUM(O66:O69)"
    @eval_fn
    def O70():
        range_1 = Dashboard_M8_Alt(15, 66, 15, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class P70():
    # 'Dashboard_M8_Alt'!P70
    value = 852.48182
    formula = "=SUM(P66:P69)"
    @eval_fn
    def P70():
        range_1 = Dashboard_M8_Alt(16, 66, 16, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q70():
    # 'Dashboard_M8_Alt'!Q70
    value = 1142.12472
    formula = "=SUM(Q66:Q69)"
    @eval_fn
    def Q70():
        range_1 = Dashboard_M8_Alt(17, 66, 17, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class R70():
    # 'Dashboard_M8_Alt'!R70
    value = 1593.79444
    formula = "=SUM(R66:R69)"
    @eval_fn
    def R70():
        range_1 = Dashboard_M8_Alt(18, 66, 18, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class S70():
    # 'Dashboard_M8_Alt'!S70
    value = 1619.38611
    formula = "=SUM(S66:S69)"
    @eval_fn
    def S70():
        range_1 = Dashboard_M8_Alt(19, 66, 19, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class T70():
    # 'Dashboard_M8_Alt'!T70
    value = 1481.87859
    formula = "=SUM(T66:T69)"
    @eval_fn
    def T70():
        range_1 = Dashboard_M8_Alt(20, 66, 20, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class U70():
    # 'Dashboard_M8_Alt'!U70
    value = "#N/A"
    formula = "=SUM(U66:U69)"
    @eval_fn
    def U70():
        range_1 = Dashboard_M8_Alt(21, 66, 21, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class V70():
    # 'Dashboard_M8_Alt'!V70
    value = "#N/A"
    formula = "=SUM(V66:V69)"
    @eval_fn
    def V70():
        range_1 = Dashboard_M8_Alt(22, 66, 22, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class W70():
    # 'Dashboard_M8_Alt'!W70
    value = "#N/A"
    formula = "=SUM(W66:W69)"
    @eval_fn
    def W70():
        range_1 = Dashboard_M8_Alt(23, 66, 23, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class X70():
    # 'Dashboard_M8_Alt'!X70
    value = "#N/A"
    formula = "=SUM(X66:X69)"
    @eval_fn
    def X70():
        range_1 = Dashboard_M8_Alt(24, 66, 24, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y70():
    # 'Dashboard_M8_Alt'!Y70
    value = "#N/A"
    formula = "=SUM(Y66:Y69)"
    @eval_fn
    def Y70():
        range_1 = Dashboard_M8_Alt(25, 66, 25, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z70():
    # 'Dashboard_M8_Alt'!Z70
    value = "#N/A"
    formula = "=SUM(Z66:Z69)"
    @eval_fn
    def Z70():
        range_1 = Dashboard_M8_Alt(26, 66, 26, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA70():
    # 'Dashboard_M8_Alt'!AA70
    value = "#N/A"
    formula = "=SUM(AA66:AA69)"
    @eval_fn
    def AA70():
        range_1 = Dashboard_M8_Alt(27, 66, 27, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB70():
    # 'Dashboard_M8_Alt'!AB70
    value = "#N/A"
    formula = "=SUM(AB66:AB69)"
    @eval_fn
    def AB70():
        range_1 = Dashboard_M8_Alt(28, 66, 28, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC70():
    # 'Dashboard_M8_Alt'!AC70
    value = "#N/A"
    formula = "=SUM(AC66:AC69)"
    @eval_fn
    def AC70():
        range_1 = Dashboard_M8_Alt(29, 66, 29, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD70():
    # 'Dashboard_M8_Alt'!AD70
    value = "#N/A"
    formula = "=SUM(AD66:AD69)"
    @eval_fn
    def AD70():
        range_1 = Dashboard_M8_Alt(30, 66, 30, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE70():
    # 'Dashboard_M8_Alt'!AE70
    value = "#N/A"
    formula = "=SUM(AE66:AE69)"
    @eval_fn
    def AE70():
        range_1 = Dashboard_M8_Alt(31, 66, 31, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF70():
    # 'Dashboard_M8_Alt'!AF70
    value = "#N/A"
    formula = "=SUM(AF66:AF69)"
    @eval_fn
    def AF70():
        range_1 = Dashboard_M8_Alt(32, 66, 32, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG70():
    # 'Dashboard_M8_Alt'!AG70
    value = "#N/A"
    formula = "=SUM(AG66:AG69)"
    @eval_fn
    def AG70():
        range_1 = Dashboard_M8_Alt(33, 66, 33, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH70():
    # 'Dashboard_M8_Alt'!AH70
    value = "#N/A"
    formula = "=SUM(AH66:AH69)"
    @eval_fn
    def AH70():
        range_1 = Dashboard_M8_Alt(34, 66, 34, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI70():
    # 'Dashboard_M8_Alt'!AI70
    value = "#N/A"
    formula = "=SUM(AI66:AI69)"
    @eval_fn
    def AI70():
        range_1 = Dashboard_M8_Alt(35, 66, 35, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ70():
    # 'Dashboard_M8_Alt'!AJ70
    value = "#N/A"
    formula = "=SUM(AJ66:AJ69)"
    @eval_fn
    def AJ70():
        range_1 = Dashboard_M8_Alt(36, 66, 36, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK70():
    # 'Dashboard_M8_Alt'!AK70
    value = "#N/A"
    formula = "=SUM(AK66:AK69)"
    @eval_fn
    def AK70():
        range_1 = Dashboard_M8_Alt(37, 66, 37, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Dashboard_M8_Alt)
class A72():
    # 'Dashboard_M8_Alt'!A72
    value = "Ratio AFE:HFE (y,p,f): Actual Expenditures to Hypothetical Expenditures in the Power Sector by Year and Fuel"

@register(Dashboard_M8_Alt)
class B74():
    # 'Dashboard_M8_Alt'!B74
    value = "Diesel"

@register(Dashboard_M8_Alt)
class I74():
    # 'Dashboard_M8_Alt'!I74
    value = 1.6034801089
    formula = "=I66/I52"
    @eval_fn
    def I74():
        i66_1 = Dashboard_M8_Alt.I66()
        i52_1 = Dashboard_M8_Alt.I52()
        var_1 = divide(i66_1, i52_1)
        return var_1

@register(Dashboard_M8_Alt)
class J74():
    # 'Dashboard_M8_Alt'!J74
    value = 0.917397884143
    formula = "=J66/J52"
    @eval_fn
    def J74():
        j66_1 = Dashboard_M8_Alt.J66()
        j52_1 = Dashboard_M8_Alt.J52()
        var_1 = divide(j66_1, j52_1)
        return var_1

@register(Dashboard_M8_Alt)
class K74():
    # 'Dashboard_M8_Alt'!K74
    value = 0.966432679989
    formula = "=K66/K52"
    @eval_fn
    def K74():
        k66_1 = Dashboard_M8_Alt.K66()
        k52_1 = Dashboard_M8_Alt.K52()
        var_1 = divide(k66_1, k52_1)
        return var_1

@register(Dashboard_M8_Alt)
class L74():
    # 'Dashboard_M8_Alt'!L74
    value = 0.958578905008
    formula = "=L66/L52"
    @eval_fn
    def L74():
        l66_1 = Dashboard_M8_Alt.L66()
        l52_1 = Dashboard_M8_Alt.L52()
        var_1 = divide(l66_1, l52_1)
        return var_1

@register(Dashboard_M8_Alt)
class M74():
    # 'Dashboard_M8_Alt'!M74
    value = 0.915373281501
    formula = "=M66/M52"
    @eval_fn
    def M74():
        m66_1 = Dashboard_M8_Alt.M66()
        m52_1 = Dashboard_M8_Alt.M52()
        var_1 = divide(m66_1, m52_1)
        return var_1

@register(Dashboard_M8_Alt)
class N74():
    # 'Dashboard_M8_Alt'!N74
    value = 0.85803699387
    formula = "=N66/N52"
    @eval_fn
    def N74():
        n66_1 = Dashboard_M8_Alt.N66()
        n52_1 = Dashboard_M8_Alt.N52()
        var_1 = divide(n66_1, n52_1)
        return var_1

@register(Dashboard_M8_Alt)
class O74():
    # 'Dashboard_M8_Alt'!O74
    value = 0.824628294815
    formula = "=O66/O52"
    @eval_fn
    def O74():
        o66_1 = Dashboard_M8_Alt.O66()
        o52_1 = Dashboard_M8_Alt.O52()
        var_1 = divide(o66_1, o52_1)
        return var_1

@register(Dashboard_M8_Alt)
class P74():
    # 'Dashboard_M8_Alt'!P74
    value = 0.859876301314
    formula = "=P66/P52"
    @eval_fn
    def P74():
        p66_1 = Dashboard_M8_Alt.P66()
        p52_1 = Dashboard_M8_Alt.P52()
        var_1 = divide(p66_1, p52_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q74():
    # 'Dashboard_M8_Alt'!Q74
    value = 0.857532510403
    formula = "=Q66/Q52"
    @eval_fn
    def Q74():
        q66_1 = Dashboard_M8_Alt.Q66()
        q52_1 = Dashboard_M8_Alt.Q52()
        var_1 = divide(q66_1, q52_1)
        return var_1

@register(Dashboard_M8_Alt)
class R74():
    # 'Dashboard_M8_Alt'!R74
    value = 0.879816774684
    formula = "=R66/R52"
    @eval_fn
    def R74():
        r66_1 = Dashboard_M8_Alt.R66()
        r52_1 = Dashboard_M8_Alt.R52()
        var_1 = divide(r66_1, r52_1)
        return var_1

@register(Dashboard_M8_Alt)
class S74():
    # 'Dashboard_M8_Alt'!S74
    value = 0.866690621881
    formula = "=S66/S52"
    @eval_fn
    def S74():
        s66_1 = Dashboard_M8_Alt.S66()
        s52_1 = Dashboard_M8_Alt.S52()
        var_1 = divide(s66_1, s52_1)
        return var_1

@register(Dashboard_M8_Alt)
class T74():
    # 'Dashboard_M8_Alt'!T74
    value = 0.862243065759
    formula = "=T66/T52"
    @eval_fn
    def T74():
        t66_1 = Dashboard_M8_Alt.T66()
        t52_1 = Dashboard_M8_Alt.T52()
        var_1 = divide(t66_1, t52_1)
        return var_1

@register(Dashboard_M8_Alt)
class U74():
    # 'Dashboard_M8_Alt'!U74
    value = "#N/A"
    formula = "=U66/U52"
    @eval_fn
    def U74():
        u66_1 = Dashboard_M8_Alt.U66()
        u52_1 = Dashboard_M8_Alt.U52()
        var_1 = divide(u66_1, u52_1)
        return var_1

@register(Dashboard_M8_Alt)
class V74():
    # 'Dashboard_M8_Alt'!V74
    value = "#N/A"
    formula = "=V66/V52"
    @eval_fn
    def V74():
        v66_1 = Dashboard_M8_Alt.V66()
        v52_1 = Dashboard_M8_Alt.V52()
        var_1 = divide(v66_1, v52_1)
        return var_1

@register(Dashboard_M8_Alt)
class W74():
    # 'Dashboard_M8_Alt'!W74
    value = "#N/A"
    formula = "=W66/W52"
    @eval_fn
    def W74():
        w66_1 = Dashboard_M8_Alt.W66()
        w52_1 = Dashboard_M8_Alt.W52()
        var_1 = divide(w66_1, w52_1)
        return var_1

@register(Dashboard_M8_Alt)
class X74():
    # 'Dashboard_M8_Alt'!X74
    value = "#N/A"
    formula = "=X66/X52"
    @eval_fn
    def X74():
        x66_1 = Dashboard_M8_Alt.X66()
        x52_1 = Dashboard_M8_Alt.X52()
        var_1 = divide(x66_1, x52_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y74():
    # 'Dashboard_M8_Alt'!Y74
    value = "#N/A"
    formula = "=Y66/Y52"
    @eval_fn
    def Y74():
        y66_1 = Dashboard_M8_Alt.Y66()
        y52_1 = Dashboard_M8_Alt.Y52()
        var_1 = divide(y66_1, y52_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z74():
    # 'Dashboard_M8_Alt'!Z74
    value = "#N/A"
    formula = "=Z66/Z52"
    @eval_fn
    def Z74():
        z66_1 = Dashboard_M8_Alt.Z66()
        z52_1 = Dashboard_M8_Alt.Z52()
        var_1 = divide(z66_1, z52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA74():
    # 'Dashboard_M8_Alt'!AA74
    value = "#N/A"
    formula = "=AA66/AA52"
    @eval_fn
    def AA74():
        aa66_1 = Dashboard_M8_Alt.AA66()
        aa52_1 = Dashboard_M8_Alt.AA52()
        var_1 = divide(aa66_1, aa52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB74():
    # 'Dashboard_M8_Alt'!AB74
    value = "#N/A"
    formula = "=AB66/AB52"
    @eval_fn
    def AB74():
        ab66_1 = Dashboard_M8_Alt.AB66()
        ab52_1 = Dashboard_M8_Alt.AB52()
        var_1 = divide(ab66_1, ab52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC74():
    # 'Dashboard_M8_Alt'!AC74
    value = "#N/A"
    formula = "=AC66/AC52"
    @eval_fn
    def AC74():
        ac66_1 = Dashboard_M8_Alt.AC66()
        ac52_1 = Dashboard_M8_Alt.AC52()
        var_1 = divide(ac66_1, ac52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD74():
    # 'Dashboard_M8_Alt'!AD74
    value = "#N/A"
    formula = "=AD66/AD52"
    @eval_fn
    def AD74():
        ad66_1 = Dashboard_M8_Alt.AD66()
        ad52_1 = Dashboard_M8_Alt.AD52()
        var_1 = divide(ad66_1, ad52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE74():
    # 'Dashboard_M8_Alt'!AE74
    value = "#N/A"
    formula = "=AE66/AE52"
    @eval_fn
    def AE74():
        ae66_1 = Dashboard_M8_Alt.AE66()
        ae52_1 = Dashboard_M8_Alt.AE52()
        var_1 = divide(ae66_1, ae52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF74():
    # 'Dashboard_M8_Alt'!AF74
    value = "#N/A"
    formula = "=AF66/AF52"
    @eval_fn
    def AF74():
        af66_1 = Dashboard_M8_Alt.AF66()
        af52_1 = Dashboard_M8_Alt.AF52()
        var_1 = divide(af66_1, af52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG74():
    # 'Dashboard_M8_Alt'!AG74
    value = "#N/A"
    formula = "=AG66/AG52"
    @eval_fn
    def AG74():
        ag66_1 = Dashboard_M8_Alt.AG66()
        ag52_1 = Dashboard_M8_Alt.AG52()
        var_1 = divide(ag66_1, ag52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH74():
    # 'Dashboard_M8_Alt'!AH74
    value = "#N/A"
    formula = "=AH66/AH52"
    @eval_fn
    def AH74():
        ah66_1 = Dashboard_M8_Alt.AH66()
        ah52_1 = Dashboard_M8_Alt.AH52()
        var_1 = divide(ah66_1, ah52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI74():
    # 'Dashboard_M8_Alt'!AI74
    value = "#N/A"
    formula = "=AI66/AI52"
    @eval_fn
    def AI74():
        ai66_1 = Dashboard_M8_Alt.AI66()
        ai52_1 = Dashboard_M8_Alt.AI52()
        var_1 = divide(ai66_1, ai52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ74():
    # 'Dashboard_M8_Alt'!AJ74
    value = "#N/A"
    formula = "=AJ66/AJ52"
    @eval_fn
    def AJ74():
        aj66_1 = Dashboard_M8_Alt.AJ66()
        aj52_1 = Dashboard_M8_Alt.AJ52()
        var_1 = divide(aj66_1, aj52_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK74():
    # 'Dashboard_M8_Alt'!AK74
    value = "#N/A"
    formula = "=AK66/AK52"
    @eval_fn
    def AK74():
        ak66_1 = Dashboard_M8_Alt.AK66()
        ak52_1 = Dashboard_M8_Alt.AK52()
        var_1 = divide(ak66_1, ak52_1)
        return var_1

@register(Dashboard_M8_Alt)
class B75():
    # 'Dashboard_M8_Alt'!B75
    value = "Fuel Oil"

@register(Dashboard_M8_Alt)
class I75():
    # 'Dashboard_M8_Alt'!I75
    value = 0.998080490095
    formula = "=I67/I53"
    @eval_fn
    def I75():
        i67_1 = Dashboard_M8_Alt.I67()
        i53_1 = Dashboard_M8_Alt.I53()
        var_1 = divide(i67_1, i53_1)
        return var_1

@register(Dashboard_M8_Alt)
class J75():
    # 'Dashboard_M8_Alt'!J75
    value = 0.98609885436
    formula = "=J67/J53"
    @eval_fn
    def J75():
        j67_1 = Dashboard_M8_Alt.J67()
        j53_1 = Dashboard_M8_Alt.J53()
        var_1 = divide(j67_1, j53_1)
        return var_1

@register(Dashboard_M8_Alt)
class K75():
    # 'Dashboard_M8_Alt'!K75
    value = 0.996862412685
    formula = "=K67/K53"
    @eval_fn
    def K75():
        k67_1 = Dashboard_M8_Alt.K67()
        k53_1 = Dashboard_M8_Alt.K53()
        var_1 = divide(k67_1, k53_1)
        return var_1

@register(Dashboard_M8_Alt)
class L75():
    # 'Dashboard_M8_Alt'!L75
    value = 0.958578905008
    formula = "=L67/L53"
    @eval_fn
    def L75():
        l67_1 = Dashboard_M8_Alt.L67()
        l53_1 = Dashboard_M8_Alt.L53()
        var_1 = divide(l67_1, l53_1)
        return var_1

@register(Dashboard_M8_Alt)
class M75():
    # 'Dashboard_M8_Alt'!M75
    value = 0.980869005046
    formula = "=M67/M53"
    @eval_fn
    def M75():
        m67_1 = Dashboard_M8_Alt.M67()
        m53_1 = Dashboard_M8_Alt.M53()
        var_1 = divide(m67_1, m53_1)
        return var_1

@register(Dashboard_M8_Alt)
class N75():
    # 'Dashboard_M8_Alt'!N75
    value = 0.969010857536
    formula = "=N67/N53"
    @eval_fn
    def N75():
        n67_1 = Dashboard_M8_Alt.N67()
        n53_1 = Dashboard_M8_Alt.N53()
        var_1 = divide(n67_1, n53_1)
        return var_1

@register(Dashboard_M8_Alt)
class O75():
    # 'Dashboard_M8_Alt'!O75
    value = 0.943679931864
    formula = "=O67/O53"
    @eval_fn
    def O75():
        o67_1 = Dashboard_M8_Alt.O67()
        o53_1 = Dashboard_M8_Alt.O53()
        var_1 = divide(o67_1, o53_1)
        return var_1

@register(Dashboard_M8_Alt)
class P75():
    # 'Dashboard_M8_Alt'!P75
    value = 0.935115231329
    formula = "=P67/P53"
    @eval_fn
    def P75():
        p67_1 = Dashboard_M8_Alt.P67()
        p53_1 = Dashboard_M8_Alt.P53()
        var_1 = divide(p67_1, p53_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q75():
    # 'Dashboard_M8_Alt'!Q75
    value = 0.904567705409
    formula = "=Q67/Q53"
    @eval_fn
    def Q75():
        q67_1 = Dashboard_M8_Alt.Q67()
        q53_1 = Dashboard_M8_Alt.Q53()
        var_1 = divide(q67_1, q53_1)
        return var_1

@register(Dashboard_M8_Alt)
class R75():
    # 'Dashboard_M8_Alt'!R75
    value = 0.911129942999
    formula = "=R67/R53"
    @eval_fn
    def R75():
        r67_1 = Dashboard_M8_Alt.R67()
        r53_1 = Dashboard_M8_Alt.R53()
        var_1 = divide(r67_1, r53_1)
        return var_1

@register(Dashboard_M8_Alt)
class S75():
    # 'Dashboard_M8_Alt'!S75
    value = 0.869083621073
    formula = "=S67/S53"
    @eval_fn
    def S75():
        s67_1 = Dashboard_M8_Alt.S67()
        s53_1 = Dashboard_M8_Alt.S53()
        var_1 = divide(s67_1, s53_1)
        return var_1

@register(Dashboard_M8_Alt)
class T75():
    # 'Dashboard_M8_Alt'!T75
    value = 0.881566627834
    formula = "=T67/T53"
    @eval_fn
    def T75():
        t67_1 = Dashboard_M8_Alt.T67()
        t53_1 = Dashboard_M8_Alt.T53()
        var_1 = divide(t67_1, t53_1)
        return var_1

@register(Dashboard_M8_Alt)
class U75():
    # 'Dashboard_M8_Alt'!U75
    value = "#N/A"
    formula = "=U67/U53"
    @eval_fn
    def U75():
        u67_1 = Dashboard_M8_Alt.U67()
        u53_1 = Dashboard_M8_Alt.U53()
        var_1 = divide(u67_1, u53_1)
        return var_1

@register(Dashboard_M8_Alt)
class V75():
    # 'Dashboard_M8_Alt'!V75
    value = "#N/A"
    formula = "=V67/V53"
    @eval_fn
    def V75():
        v67_1 = Dashboard_M8_Alt.V67()
        v53_1 = Dashboard_M8_Alt.V53()
        var_1 = divide(v67_1, v53_1)
        return var_1

@register(Dashboard_M8_Alt)
class W75():
    # 'Dashboard_M8_Alt'!W75
    value = "#N/A"
    formula = "=W67/W53"
    @eval_fn
    def W75():
        w67_1 = Dashboard_M8_Alt.W67()
        w53_1 = Dashboard_M8_Alt.W53()
        var_1 = divide(w67_1, w53_1)
        return var_1

@register(Dashboard_M8_Alt)
class X75():
    # 'Dashboard_M8_Alt'!X75
    value = "#N/A"
    formula = "=X67/X53"
    @eval_fn
    def X75():
        x67_1 = Dashboard_M8_Alt.X67()
        x53_1 = Dashboard_M8_Alt.X53()
        var_1 = divide(x67_1, x53_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y75():
    # 'Dashboard_M8_Alt'!Y75
    value = "#N/A"
    formula = "=Y67/Y53"
    @eval_fn
    def Y75():
        y67_1 = Dashboard_M8_Alt.Y67()
        y53_1 = Dashboard_M8_Alt.Y53()
        var_1 = divide(y67_1, y53_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z75():
    # 'Dashboard_M8_Alt'!Z75
    value = "#N/A"
    formula = "=Z67/Z53"
    @eval_fn
    def Z75():
        z67_1 = Dashboard_M8_Alt.Z67()
        z53_1 = Dashboard_M8_Alt.Z53()
        var_1 = divide(z67_1, z53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA75():
    # 'Dashboard_M8_Alt'!AA75
    value = "#N/A"
    formula = "=AA67/AA53"
    @eval_fn
    def AA75():
        aa67_1 = Dashboard_M8_Alt.AA67()
        aa53_1 = Dashboard_M8_Alt.AA53()
        var_1 = divide(aa67_1, aa53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB75():
    # 'Dashboard_M8_Alt'!AB75
    value = "#N/A"
    formula = "=AB67/AB53"
    @eval_fn
    def AB75():
        ab67_1 = Dashboard_M8_Alt.AB67()
        ab53_1 = Dashboard_M8_Alt.AB53()
        var_1 = divide(ab67_1, ab53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC75():
    # 'Dashboard_M8_Alt'!AC75
    value = "#N/A"
    formula = "=AC67/AC53"
    @eval_fn
    def AC75():
        ac67_1 = Dashboard_M8_Alt.AC67()
        ac53_1 = Dashboard_M8_Alt.AC53()
        var_1 = divide(ac67_1, ac53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD75():
    # 'Dashboard_M8_Alt'!AD75
    value = "#N/A"
    formula = "=AD67/AD53"
    @eval_fn
    def AD75():
        ad67_1 = Dashboard_M8_Alt.AD67()
        ad53_1 = Dashboard_M8_Alt.AD53()
        var_1 = divide(ad67_1, ad53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE75():
    # 'Dashboard_M8_Alt'!AE75
    value = "#N/A"
    formula = "=AE67/AE53"
    @eval_fn
    def AE75():
        ae67_1 = Dashboard_M8_Alt.AE67()
        ae53_1 = Dashboard_M8_Alt.AE53()
        var_1 = divide(ae67_1, ae53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF75():
    # 'Dashboard_M8_Alt'!AF75
    value = "#N/A"
    formula = "=AF67/AF53"
    @eval_fn
    def AF75():
        af67_1 = Dashboard_M8_Alt.AF67()
        af53_1 = Dashboard_M8_Alt.AF53()
        var_1 = divide(af67_1, af53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG75():
    # 'Dashboard_M8_Alt'!AG75
    value = "#N/A"
    formula = "=AG67/AG53"
    @eval_fn
    def AG75():
        ag67_1 = Dashboard_M8_Alt.AG67()
        ag53_1 = Dashboard_M8_Alt.AG53()
        var_1 = divide(ag67_1, ag53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH75():
    # 'Dashboard_M8_Alt'!AH75
    value = "#N/A"
    formula = "=AH67/AH53"
    @eval_fn
    def AH75():
        ah67_1 = Dashboard_M8_Alt.AH67()
        ah53_1 = Dashboard_M8_Alt.AH53()
        var_1 = divide(ah67_1, ah53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI75():
    # 'Dashboard_M8_Alt'!AI75
    value = "#N/A"
    formula = "=AI67/AI53"
    @eval_fn
    def AI75():
        ai67_1 = Dashboard_M8_Alt.AI67()
        ai53_1 = Dashboard_M8_Alt.AI53()
        var_1 = divide(ai67_1, ai53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ75():
    # 'Dashboard_M8_Alt'!AJ75
    value = "#N/A"
    formula = "=AJ67/AJ53"
    @eval_fn
    def AJ75():
        aj67_1 = Dashboard_M8_Alt.AJ67()
        aj53_1 = Dashboard_M8_Alt.AJ53()
        var_1 = divide(aj67_1, aj53_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK75():
    # 'Dashboard_M8_Alt'!AK75
    value = "#N/A"
    formula = "=AK67/AK53"
    @eval_fn
    def AK75():
        ak67_1 = Dashboard_M8_Alt.AK67()
        ak53_1 = Dashboard_M8_Alt.AK53()
        var_1 = divide(ak67_1, ak53_1)
        return var_1

@register(Dashboard_M8_Alt)
class B76():
    # 'Dashboard_M8_Alt'!B76
    value = "SNG"

@register(Dashboard_M8_Alt)
class I76():
    # 'Dashboard_M8_Alt'!I76
    value = "#DIV/0!"
    formula = "=I68/I54"
    @eval_fn
    def I76():
        i68_1 = Dashboard_M8_Alt.I68()
        i54_1 = Dashboard_M8_Alt.I54()
        var_1 = divide(i68_1, i54_1)
        return var_1

@register(Dashboard_M8_Alt)
class J76():
    # 'Dashboard_M8_Alt'!J76
    value = "#DIV/0!"
    formula = "=J68/J54"
    @eval_fn
    def J76():
        j68_1 = Dashboard_M8_Alt.J68()
        j54_1 = Dashboard_M8_Alt.J54()
        var_1 = divide(j68_1, j54_1)
        return var_1

@register(Dashboard_M8_Alt)
class K76():
    # 'Dashboard_M8_Alt'!K76
    value = "#DIV/0!"
    formula = "=K68/K54"
    @eval_fn
    def K76():
        k68_1 = Dashboard_M8_Alt.K68()
        k54_1 = Dashboard_M8_Alt.K54()
        var_1 = divide(k68_1, k54_1)
        return var_1

@register(Dashboard_M8_Alt)
class L76():
    # 'Dashboard_M8_Alt'!L76
    value = "#DIV/0!"
    formula = "=L68/L54"
    @eval_fn
    def L76():
        l68_1 = Dashboard_M8_Alt.L68()
        l54_1 = Dashboard_M8_Alt.L54()
        var_1 = divide(l68_1, l54_1)
        return var_1

@register(Dashboard_M8_Alt)
class M76():
    # 'Dashboard_M8_Alt'!M76
    value = "#DIV/0!"
    formula = "=M68/M54"
    @eval_fn
    def M76():
        m68_1 = Dashboard_M8_Alt.M68()
        m54_1 = Dashboard_M8_Alt.M54()
        var_1 = divide(m68_1, m54_1)
        return var_1

@register(Dashboard_M8_Alt)
class N76():
    # 'Dashboard_M8_Alt'!N76
    value = "#DIV/0!"
    formula = "=N68/N54"
    @eval_fn
    def N76():
        n68_1 = Dashboard_M8_Alt.N68()
        n54_1 = Dashboard_M8_Alt.N54()
        var_1 = divide(n68_1, n54_1)
        return var_1

@register(Dashboard_M8_Alt)
class O76():
    # 'Dashboard_M8_Alt'!O76
    value = "#DIV/0!"
    formula = "=O68/O54"
    @eval_fn
    def O76():
        o68_1 = Dashboard_M8_Alt.O68()
        o54_1 = Dashboard_M8_Alt.O54()
        var_1 = divide(o68_1, o54_1)
        return var_1

@register(Dashboard_M8_Alt)
class P76():
    # 'Dashboard_M8_Alt'!P76
    value = "#DIV/0!"
    formula = "=P68/P54"
    @eval_fn
    def P76():
        p68_1 = Dashboard_M8_Alt.P68()
        p54_1 = Dashboard_M8_Alt.P54()
        var_1 = divide(p68_1, p54_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q76():
    # 'Dashboard_M8_Alt'!Q76
    value = "#DIV/0!"
    formula = "=Q68/Q54"
    @eval_fn
    def Q76():
        q68_1 = Dashboard_M8_Alt.Q68()
        q54_1 = Dashboard_M8_Alt.Q54()
        var_1 = divide(q68_1, q54_1)
        return var_1

@register(Dashboard_M8_Alt)
class R76():
    # 'Dashboard_M8_Alt'!R76
    value = "#DIV/0!"
    formula = "=R68/R54"
    @eval_fn
    def R76():
        r68_1 = Dashboard_M8_Alt.R68()
        r54_1 = Dashboard_M8_Alt.R54()
        var_1 = divide(r68_1, r54_1)
        return var_1

@register(Dashboard_M8_Alt)
class S76():
    # 'Dashboard_M8_Alt'!S76
    value = "#DIV/0!"
    formula = "=S68/S54"
    @eval_fn
    def S76():
        s68_1 = Dashboard_M8_Alt.S68()
        s54_1 = Dashboard_M8_Alt.S54()
        var_1 = divide(s68_1, s54_1)
        return var_1

@register(Dashboard_M8_Alt)
class T76():
    # 'Dashboard_M8_Alt'!T76
    value = "#DIV/0!"
    formula = "=T68/T54"
    @eval_fn
    def T76():
        t68_1 = Dashboard_M8_Alt.T68()
        t54_1 = Dashboard_M8_Alt.T54()
        var_1 = divide(t68_1, t54_1)
        return var_1

@register(Dashboard_M8_Alt)
class U76():
    # 'Dashboard_M8_Alt'!U76
    value = "#N/A"
    formula = "=U68/U54"
    @eval_fn
    def U76():
        u68_1 = Dashboard_M8_Alt.U68()
        u54_1 = Dashboard_M8_Alt.U54()
        var_1 = divide(u68_1, u54_1)
        return var_1

@register(Dashboard_M8_Alt)
class V76():
    # 'Dashboard_M8_Alt'!V76
    value = "#N/A"
    formula = "=V68/V54"
    @eval_fn
    def V76():
        v68_1 = Dashboard_M8_Alt.V68()
        v54_1 = Dashboard_M8_Alt.V54()
        var_1 = divide(v68_1, v54_1)
        return var_1

@register(Dashboard_M8_Alt)
class W76():
    # 'Dashboard_M8_Alt'!W76
    value = "#N/A"
    formula = "=W68/W54"
    @eval_fn
    def W76():
        w68_1 = Dashboard_M8_Alt.W68()
        w54_1 = Dashboard_M8_Alt.W54()
        var_1 = divide(w68_1, w54_1)
        return var_1

@register(Dashboard_M8_Alt)
class X76():
    # 'Dashboard_M8_Alt'!X76
    value = "#N/A"
    formula = "=X68/X54"
    @eval_fn
    def X76():
        x68_1 = Dashboard_M8_Alt.X68()
        x54_1 = Dashboard_M8_Alt.X54()
        var_1 = divide(x68_1, x54_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y76():
    # 'Dashboard_M8_Alt'!Y76
    value = "#N/A"
    formula = "=Y68/Y54"
    @eval_fn
    def Y76():
        y68_1 = Dashboard_M8_Alt.Y68()
        y54_1 = Dashboard_M8_Alt.Y54()
        var_1 = divide(y68_1, y54_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z76():
    # 'Dashboard_M8_Alt'!Z76
    value = "#N/A"
    formula = "=Z68/Z54"
    @eval_fn
    def Z76():
        z68_1 = Dashboard_M8_Alt.Z68()
        z54_1 = Dashboard_M8_Alt.Z54()
        var_1 = divide(z68_1, z54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA76():
    # 'Dashboard_M8_Alt'!AA76
    value = "#N/A"
    formula = "=AA68/AA54"
    @eval_fn
    def AA76():
        aa68_1 = Dashboard_M8_Alt.AA68()
        aa54_1 = Dashboard_M8_Alt.AA54()
        var_1 = divide(aa68_1, aa54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB76():
    # 'Dashboard_M8_Alt'!AB76
    value = "#N/A"
    formula = "=AB68/AB54"
    @eval_fn
    def AB76():
        ab68_1 = Dashboard_M8_Alt.AB68()
        ab54_1 = Dashboard_M8_Alt.AB54()
        var_1 = divide(ab68_1, ab54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC76():
    # 'Dashboard_M8_Alt'!AC76
    value = "#N/A"
    formula = "=AC68/AC54"
    @eval_fn
    def AC76():
        ac68_1 = Dashboard_M8_Alt.AC68()
        ac54_1 = Dashboard_M8_Alt.AC54()
        var_1 = divide(ac68_1, ac54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD76():
    # 'Dashboard_M8_Alt'!AD76
    value = "#N/A"
    formula = "=AD68/AD54"
    @eval_fn
    def AD76():
        ad68_1 = Dashboard_M8_Alt.AD68()
        ad54_1 = Dashboard_M8_Alt.AD54()
        var_1 = divide(ad68_1, ad54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE76():
    # 'Dashboard_M8_Alt'!AE76
    value = "#N/A"
    formula = "=AE68/AE54"
    @eval_fn
    def AE76():
        ae68_1 = Dashboard_M8_Alt.AE68()
        ae54_1 = Dashboard_M8_Alt.AE54()
        var_1 = divide(ae68_1, ae54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF76():
    # 'Dashboard_M8_Alt'!AF76
    value = "#N/A"
    formula = "=AF68/AF54"
    @eval_fn
    def AF76():
        af68_1 = Dashboard_M8_Alt.AF68()
        af54_1 = Dashboard_M8_Alt.AF54()
        var_1 = divide(af68_1, af54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG76():
    # 'Dashboard_M8_Alt'!AG76
    value = "#N/A"
    formula = "=AG68/AG54"
    @eval_fn
    def AG76():
        ag68_1 = Dashboard_M8_Alt.AG68()
        ag54_1 = Dashboard_M8_Alt.AG54()
        var_1 = divide(ag68_1, ag54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH76():
    # 'Dashboard_M8_Alt'!AH76
    value = "#N/A"
    formula = "=AH68/AH54"
    @eval_fn
    def AH76():
        ah68_1 = Dashboard_M8_Alt.AH68()
        ah54_1 = Dashboard_M8_Alt.AH54()
        var_1 = divide(ah68_1, ah54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI76():
    # 'Dashboard_M8_Alt'!AI76
    value = "#N/A"
    formula = "=AI68/AI54"
    @eval_fn
    def AI76():
        ai68_1 = Dashboard_M8_Alt.AI68()
        ai54_1 = Dashboard_M8_Alt.AI54()
        var_1 = divide(ai68_1, ai54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ76():
    # 'Dashboard_M8_Alt'!AJ76
    value = "#N/A"
    formula = "=AJ68/AJ54"
    @eval_fn
    def AJ76():
        aj68_1 = Dashboard_M8_Alt.AJ68()
        aj54_1 = Dashboard_M8_Alt.AJ54()
        var_1 = divide(aj68_1, aj54_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK76():
    # 'Dashboard_M8_Alt'!AK76
    value = "#N/A"
    formula = "=AK68/AK54"
    @eval_fn
    def AK76():
        ak68_1 = Dashboard_M8_Alt.AK68()
        ak54_1 = Dashboard_M8_Alt.AK54()
        var_1 = divide(ak68_1, ak54_1)
        return var_1

@register(Dashboard_M8_Alt)
class B77():
    # 'Dashboard_M8_Alt'!B77
    value = "Coal"

@register(Dashboard_M8_Alt)
class I77():
    # 'Dashboard_M8_Alt'!I77
    value = 1.00280400205
    formula = "=I69/I55"
    @eval_fn
    def I77():
        i69_1 = Dashboard_M8_Alt.I69()
        i55_1 = Dashboard_M8_Alt.I55()
        var_1 = divide(i69_1, i55_1)
        return var_1

@register(Dashboard_M8_Alt)
class J77():
    # 'Dashboard_M8_Alt'!J77
    value = 1.11542800508
    formula = "=J69/J55"
    @eval_fn
    def J77():
        j69_1 = Dashboard_M8_Alt.J69()
        j55_1 = Dashboard_M8_Alt.J55()
        var_1 = divide(j69_1, j55_1)
        return var_1

@register(Dashboard_M8_Alt)
class K77():
    # 'Dashboard_M8_Alt'!K77
    value = 1.09293915776
    formula = "=K69/K55"
    @eval_fn
    def K77():
        k69_1 = Dashboard_M8_Alt.K69()
        k55_1 = Dashboard_M8_Alt.K55()
        var_1 = divide(k69_1, k55_1)
        return var_1

@register(Dashboard_M8_Alt)
class L77():
    # 'Dashboard_M8_Alt'!L77
    value = 0.958578905008
    formula = "=L69/L55"
    @eval_fn
    def L77():
        l69_1 = Dashboard_M8_Alt.L69()
        l55_1 = Dashboard_M8_Alt.L55()
        var_1 = divide(l69_1, l55_1)
        return var_1

@register(Dashboard_M8_Alt)
class M77():
    # 'Dashboard_M8_Alt'!M77
    value = 0.926016783745
    formula = "=M69/M55"
    @eval_fn
    def M77():
        m69_1 = Dashboard_M8_Alt.M69()
        m55_1 = Dashboard_M8_Alt.M55()
        var_1 = divide(m69_1, m55_1)
        return var_1

@register(Dashboard_M8_Alt)
class N77():
    # 'Dashboard_M8_Alt'!N77
    value = 0.997440038573
    formula = "=N69/N55"
    @eval_fn
    def N77():
        n69_1 = Dashboard_M8_Alt.N69()
        n55_1 = Dashboard_M8_Alt.N55()
        var_1 = divide(n69_1, n55_1)
        return var_1

@register(Dashboard_M8_Alt)
class O77():
    # 'Dashboard_M8_Alt'!O77
    value = 1.04519353538
    formula = "=O69/O55"
    @eval_fn
    def O77():
        o69_1 = Dashboard_M8_Alt.O69()
        o55_1 = Dashboard_M8_Alt.O55()
        var_1 = divide(o69_1, o55_1)
        return var_1

@register(Dashboard_M8_Alt)
class P77():
    # 'Dashboard_M8_Alt'!P77
    value = 1.01022392066
    formula = "=P69/P55"
    @eval_fn
    def P77():
        p69_1 = Dashboard_M8_Alt.P69()
        p55_1 = Dashboard_M8_Alt.P55()
        var_1 = divide(p69_1, p55_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q77():
    # 'Dashboard_M8_Alt'!Q77
    value = 0.936385145502
    formula = "=Q69/Q55"
    @eval_fn
    def Q77():
        q69_1 = Dashboard_M8_Alt.Q69()
        q55_1 = Dashboard_M8_Alt.Q55()
        var_1 = divide(q69_1, q55_1)
        return var_1

@register(Dashboard_M8_Alt)
class R77():
    # 'Dashboard_M8_Alt'!R77
    value = 0.896939078953
    formula = "=R69/R55"
    @eval_fn
    def R77():
        r69_1 = Dashboard_M8_Alt.R69()
        r55_1 = Dashboard_M8_Alt.R55()
        var_1 = divide(r69_1, r55_1)
        return var_1

@register(Dashboard_M8_Alt)
class S77():
    # 'Dashboard_M8_Alt'!S77
    value = 0.965230083533
    formula = "=S69/S55"
    @eval_fn
    def S77():
        s69_1 = Dashboard_M8_Alt.S69()
        s55_1 = Dashboard_M8_Alt.S55()
        var_1 = divide(s69_1, s55_1)
        return var_1

@register(Dashboard_M8_Alt)
class T77():
    # 'Dashboard_M8_Alt'!T77
    value = 0.911608011319
    formula = "=T69/T55"
    @eval_fn
    def T77():
        t69_1 = Dashboard_M8_Alt.T69()
        t55_1 = Dashboard_M8_Alt.T55()
        var_1 = divide(t69_1, t55_1)
        return var_1

@register(Dashboard_M8_Alt)
class U77():
    # 'Dashboard_M8_Alt'!U77
    value = "#N/A"
    formula = "=U69/U55"
    @eval_fn
    def U77():
        u69_1 = Dashboard_M8_Alt.U69()
        u55_1 = Dashboard_M8_Alt.U55()
        var_1 = divide(u69_1, u55_1)
        return var_1

@register(Dashboard_M8_Alt)
class V77():
    # 'Dashboard_M8_Alt'!V77
    value = "#N/A"
    formula = "=V69/V55"
    @eval_fn
    def V77():
        v69_1 = Dashboard_M8_Alt.V69()
        v55_1 = Dashboard_M8_Alt.V55()
        var_1 = divide(v69_1, v55_1)
        return var_1

@register(Dashboard_M8_Alt)
class W77():
    # 'Dashboard_M8_Alt'!W77
    value = "#N/A"
    formula = "=W69/W55"
    @eval_fn
    def W77():
        w69_1 = Dashboard_M8_Alt.W69()
        w55_1 = Dashboard_M8_Alt.W55()
        var_1 = divide(w69_1, w55_1)
        return var_1

@register(Dashboard_M8_Alt)
class X77():
    # 'Dashboard_M8_Alt'!X77
    value = "#N/A"
    formula = "=X69/X55"
    @eval_fn
    def X77():
        x69_1 = Dashboard_M8_Alt.X69()
        x55_1 = Dashboard_M8_Alt.X55()
        var_1 = divide(x69_1, x55_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y77():
    # 'Dashboard_M8_Alt'!Y77
    value = "#N/A"
    formula = "=Y69/Y55"
    @eval_fn
    def Y77():
        y69_1 = Dashboard_M8_Alt.Y69()
        y55_1 = Dashboard_M8_Alt.Y55()
        var_1 = divide(y69_1, y55_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z77():
    # 'Dashboard_M8_Alt'!Z77
    value = "#N/A"
    formula = "=Z69/Z55"
    @eval_fn
    def Z77():
        z69_1 = Dashboard_M8_Alt.Z69()
        z55_1 = Dashboard_M8_Alt.Z55()
        var_1 = divide(z69_1, z55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA77():
    # 'Dashboard_M8_Alt'!AA77
    value = "#N/A"
    formula = "=AA69/AA55"
    @eval_fn
    def AA77():
        aa69_1 = Dashboard_M8_Alt.AA69()
        aa55_1 = Dashboard_M8_Alt.AA55()
        var_1 = divide(aa69_1, aa55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB77():
    # 'Dashboard_M8_Alt'!AB77
    value = "#N/A"
    formula = "=AB69/AB55"
    @eval_fn
    def AB77():
        ab69_1 = Dashboard_M8_Alt.AB69()
        ab55_1 = Dashboard_M8_Alt.AB55()
        var_1 = divide(ab69_1, ab55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC77():
    # 'Dashboard_M8_Alt'!AC77
    value = "#N/A"
    formula = "=AC69/AC55"
    @eval_fn
    def AC77():
        ac69_1 = Dashboard_M8_Alt.AC69()
        ac55_1 = Dashboard_M8_Alt.AC55()
        var_1 = divide(ac69_1, ac55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD77():
    # 'Dashboard_M8_Alt'!AD77
    value = "#N/A"
    formula = "=AD69/AD55"
    @eval_fn
    def AD77():
        ad69_1 = Dashboard_M8_Alt.AD69()
        ad55_1 = Dashboard_M8_Alt.AD55()
        var_1 = divide(ad69_1, ad55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE77():
    # 'Dashboard_M8_Alt'!AE77
    value = "#N/A"
    formula = "=AE69/AE55"
    @eval_fn
    def AE77():
        ae69_1 = Dashboard_M8_Alt.AE69()
        ae55_1 = Dashboard_M8_Alt.AE55()
        var_1 = divide(ae69_1, ae55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF77():
    # 'Dashboard_M8_Alt'!AF77
    value = "#N/A"
    formula = "=AF69/AF55"
    @eval_fn
    def AF77():
        af69_1 = Dashboard_M8_Alt.AF69()
        af55_1 = Dashboard_M8_Alt.AF55()
        var_1 = divide(af69_1, af55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG77():
    # 'Dashboard_M8_Alt'!AG77
    value = "#N/A"
    formula = "=AG69/AG55"
    @eval_fn
    def AG77():
        ag69_1 = Dashboard_M8_Alt.AG69()
        ag55_1 = Dashboard_M8_Alt.AG55()
        var_1 = divide(ag69_1, ag55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH77():
    # 'Dashboard_M8_Alt'!AH77
    value = "#N/A"
    formula = "=AH69/AH55"
    @eval_fn
    def AH77():
        ah69_1 = Dashboard_M8_Alt.AH69()
        ah55_1 = Dashboard_M8_Alt.AH55()
        var_1 = divide(ah69_1, ah55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI77():
    # 'Dashboard_M8_Alt'!AI77
    value = "#N/A"
    formula = "=AI69/AI55"
    @eval_fn
    def AI77():
        ai69_1 = Dashboard_M8_Alt.AI69()
        ai55_1 = Dashboard_M8_Alt.AI55()
        var_1 = divide(ai69_1, ai55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ77():
    # 'Dashboard_M8_Alt'!AJ77
    value = "#N/A"
    formula = "=AJ69/AJ55"
    @eval_fn
    def AJ77():
        aj69_1 = Dashboard_M8_Alt.AJ69()
        aj55_1 = Dashboard_M8_Alt.AJ55()
        var_1 = divide(aj69_1, aj55_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK77():
    # 'Dashboard_M8_Alt'!AK77
    value = "#N/A"
    formula = "=AK69/AK55"
    @eval_fn
    def AK77():
        ak69_1 = Dashboard_M8_Alt.AK69()
        ak55_1 = Dashboard_M8_Alt.AK55()
        var_1 = divide(ak69_1, ak55_1)
        return var_1

@register(Dashboard_M8_Alt)
class B78():
    # 'Dashboard_M8_Alt'!B78
    value = "All Fuels"

@register(Dashboard_M8_Alt)
class I78():
    # 'Dashboard_M8_Alt'!I78
    value = 1.11199688217
    formula = "=I70/I56"
    @eval_fn
    def I78():
        i70_1 = Dashboard_M8_Alt.I70()
        i56_1 = Dashboard_M8_Alt.I56()
        var_1 = divide(i70_1, i56_1)
        return var_1

@register(Dashboard_M8_Alt)
class J78():
    # 'Dashboard_M8_Alt'!J78
    value = 0.983318079516
    formula = "=J70/J56"
    @eval_fn
    def J78():
        j70_1 = Dashboard_M8_Alt.J70()
        j56_1 = Dashboard_M8_Alt.J56()
        var_1 = divide(j70_1, j56_1)
        return var_1

@register(Dashboard_M8_Alt)
class K78():
    # 'Dashboard_M8_Alt'!K78
    value = 0.994725640477
    formula = "=K70/K56"
    @eval_fn
    def K78():
        k70_1 = Dashboard_M8_Alt.K70()
        k56_1 = Dashboard_M8_Alt.K56()
        var_1 = divide(k70_1, k56_1)
        return var_1

@register(Dashboard_M8_Alt)
class L78():
    # 'Dashboard_M8_Alt'!L78
    value = 0.958578905008
    formula = "=L70/L56"
    @eval_fn
    def L78():
        l70_1 = Dashboard_M8_Alt.L70()
        l56_1 = Dashboard_M8_Alt.L56()
        var_1 = divide(l70_1, l56_1)
        return var_1

@register(Dashboard_M8_Alt)
class M78():
    # 'Dashboard_M8_Alt'!M78
    value = 0.963495280095
    formula = "=M70/M56"
    @eval_fn
    def M78():
        m70_1 = Dashboard_M8_Alt.M70()
        m56_1 = Dashboard_M8_Alt.M56()
        var_1 = divide(m70_1, m56_1)
        return var_1

@register(Dashboard_M8_Alt)
class N78():
    # 'Dashboard_M8_Alt'!N78
    value = 0.944125415258
    formula = "=N70/N56"
    @eval_fn
    def N78():
        n70_1 = Dashboard_M8_Alt.N70()
        n56_1 = Dashboard_M8_Alt.N56()
        var_1 = divide(n70_1, n56_1)
        return var_1

@register(Dashboard_M8_Alt)
class O78():
    # 'Dashboard_M8_Alt'!O78
    value = 0.919346144228
    formula = "=O70/O56"
    @eval_fn
    def O78():
        o70_1 = Dashboard_M8_Alt.O70()
        o56_1 = Dashboard_M8_Alt.O56()
        var_1 = divide(o70_1, o56_1)
        return var_1

@register(Dashboard_M8_Alt)
class P78():
    # 'Dashboard_M8_Alt'!P78
    value = 0.921146284214
    formula = "=P70/P56"
    @eval_fn
    def P78():
        p70_1 = Dashboard_M8_Alt.P70()
        p56_1 = Dashboard_M8_Alt.P56()
        var_1 = divide(p70_1, p56_1)
        return var_1

@register(Dashboard_M8_Alt)
class Q78():
    # 'Dashboard_M8_Alt'!Q78
    value = 0.895676548744
    formula = "=Q70/Q56"
    @eval_fn
    def Q78():
        q70_1 = Dashboard_M8_Alt.Q70()
        q56_1 = Dashboard_M8_Alt.Q56()
        var_1 = divide(q70_1, q56_1)
        return var_1

@register(Dashboard_M8_Alt)
class R78():
    # 'Dashboard_M8_Alt'!R78
    value = 0.904631322904
    formula = "=R70/R56"
    @eval_fn
    def R78():
        r70_1 = Dashboard_M8_Alt.R70()
        r56_1 = Dashboard_M8_Alt.R56()
        var_1 = divide(r70_1, r56_1)
        return var_1

@register(Dashboard_M8_Alt)
class S78():
    # 'Dashboard_M8_Alt'!S78
    value = 0.870179588567
    formula = "=S70/S56"
    @eval_fn
    def S78():
        s70_1 = Dashboard_M8_Alt.S70()
        s56_1 = Dashboard_M8_Alt.S56()
        var_1 = divide(s70_1, s56_1)
        return var_1

@register(Dashboard_M8_Alt)
class T78():
    # 'Dashboard_M8_Alt'!T78
    value = 0.87831083282
    formula = "=T70/T56"
    @eval_fn
    def T78():
        t70_1 = Dashboard_M8_Alt.T70()
        t56_1 = Dashboard_M8_Alt.T56()
        var_1 = divide(t70_1, t56_1)
        return var_1

@register(Dashboard_M8_Alt)
class U78():
    # 'Dashboard_M8_Alt'!U78
    value = "#N/A"
    formula = "=U70/U56"
    @eval_fn
    def U78():
        u70_1 = Dashboard_M8_Alt.U70()
        u56_1 = Dashboard_M8_Alt.U56()
        var_1 = divide(u70_1, u56_1)
        return var_1

@register(Dashboard_M8_Alt)
class V78():
    # 'Dashboard_M8_Alt'!V78
    value = "#N/A"
    formula = "=V70/V56"
    @eval_fn
    def V78():
        v70_1 = Dashboard_M8_Alt.V70()
        v56_1 = Dashboard_M8_Alt.V56()
        var_1 = divide(v70_1, v56_1)
        return var_1

@register(Dashboard_M8_Alt)
class W78():
    # 'Dashboard_M8_Alt'!W78
    value = "#N/A"
    formula = "=W70/W56"
    @eval_fn
    def W78():
        w70_1 = Dashboard_M8_Alt.W70()
        w56_1 = Dashboard_M8_Alt.W56()
        var_1 = divide(w70_1, w56_1)
        return var_1

@register(Dashboard_M8_Alt)
class X78():
    # 'Dashboard_M8_Alt'!X78
    value = "#N/A"
    formula = "=X70/X56"
    @eval_fn
    def X78():
        x70_1 = Dashboard_M8_Alt.X70()
        x56_1 = Dashboard_M8_Alt.X56()
        var_1 = divide(x70_1, x56_1)
        return var_1

@register(Dashboard_M8_Alt)
class Y78():
    # 'Dashboard_M8_Alt'!Y78
    value = "#N/A"
    formula = "=Y70/Y56"
    @eval_fn
    def Y78():
        y70_1 = Dashboard_M8_Alt.Y70()
        y56_1 = Dashboard_M8_Alt.Y56()
        var_1 = divide(y70_1, y56_1)
        return var_1

@register(Dashboard_M8_Alt)
class Z78():
    # 'Dashboard_M8_Alt'!Z78
    value = "#N/A"
    formula = "=Z70/Z56"
    @eval_fn
    def Z78():
        z70_1 = Dashboard_M8_Alt.Z70()
        z56_1 = Dashboard_M8_Alt.Z56()
        var_1 = divide(z70_1, z56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AA78():
    # 'Dashboard_M8_Alt'!AA78
    value = "#N/A"
    formula = "=AA70/AA56"
    @eval_fn
    def AA78():
        aa70_1 = Dashboard_M8_Alt.AA70()
        aa56_1 = Dashboard_M8_Alt.AA56()
        var_1 = divide(aa70_1, aa56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AB78():
    # 'Dashboard_M8_Alt'!AB78
    value = "#N/A"
    formula = "=AB70/AB56"
    @eval_fn
    def AB78():
        ab70_1 = Dashboard_M8_Alt.AB70()
        ab56_1 = Dashboard_M8_Alt.AB56()
        var_1 = divide(ab70_1, ab56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AC78():
    # 'Dashboard_M8_Alt'!AC78
    value = "#N/A"
    formula = "=AC70/AC56"
    @eval_fn
    def AC78():
        ac70_1 = Dashboard_M8_Alt.AC70()
        ac56_1 = Dashboard_M8_Alt.AC56()
        var_1 = divide(ac70_1, ac56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AD78():
    # 'Dashboard_M8_Alt'!AD78
    value = "#N/A"
    formula = "=AD70/AD56"
    @eval_fn
    def AD78():
        ad70_1 = Dashboard_M8_Alt.AD70()
        ad56_1 = Dashboard_M8_Alt.AD56()
        var_1 = divide(ad70_1, ad56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AE78():
    # 'Dashboard_M8_Alt'!AE78
    value = "#N/A"
    formula = "=AE70/AE56"
    @eval_fn
    def AE78():
        ae70_1 = Dashboard_M8_Alt.AE70()
        ae56_1 = Dashboard_M8_Alt.AE56()
        var_1 = divide(ae70_1, ae56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AF78():
    # 'Dashboard_M8_Alt'!AF78
    value = "#N/A"
    formula = "=AF70/AF56"
    @eval_fn
    def AF78():
        af70_1 = Dashboard_M8_Alt.AF70()
        af56_1 = Dashboard_M8_Alt.AF56()
        var_1 = divide(af70_1, af56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AG78():
    # 'Dashboard_M8_Alt'!AG78
    value = "#N/A"
    formula = "=AG70/AG56"
    @eval_fn
    def AG78():
        ag70_1 = Dashboard_M8_Alt.AG70()
        ag56_1 = Dashboard_M8_Alt.AG56()
        var_1 = divide(ag70_1, ag56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AH78():
    # 'Dashboard_M8_Alt'!AH78
    value = "#N/A"
    formula = "=AH70/AH56"
    @eval_fn
    def AH78():
        ah70_1 = Dashboard_M8_Alt.AH70()
        ah56_1 = Dashboard_M8_Alt.AH56()
        var_1 = divide(ah70_1, ah56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AI78():
    # 'Dashboard_M8_Alt'!AI78
    value = "#N/A"
    formula = "=AI70/AI56"
    @eval_fn
    def AI78():
        ai70_1 = Dashboard_M8_Alt.AI70()
        ai56_1 = Dashboard_M8_Alt.AI56()
        var_1 = divide(ai70_1, ai56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AJ78():
    # 'Dashboard_M8_Alt'!AJ78
    value = "#N/A"
    formula = "=AJ70/AJ56"
    @eval_fn
    def AJ78():
        aj70_1 = Dashboard_M8_Alt.AJ70()
        aj56_1 = Dashboard_M8_Alt.AJ56()
        var_1 = divide(aj70_1, aj56_1)
        return var_1

@register(Dashboard_M8_Alt)
class AK78():
    # 'Dashboard_M8_Alt'!AK78
    value = "#N/A"
    formula = "=AK70/AK56"
    @eval_fn
    def AK78():
        ak70_1 = Dashboard_M8_Alt.AK70()
        ak56_1 = Dashboard_M8_Alt.AK56()
        var_1 = divide(ak70_1, ak56_1)
        return var_1

@register(Dashboard_M8_Alt)
class B81():
    # 'Dashboard_M8_Alt'!B81
    value = "All Fuels (Savings)"

@register(Dashboard_M8_Alt)
class I81():
    # 'Dashboard_M8_Alt'!I81
    value = 441.313512537
    formula = "=I56"
    @eval_fn
    def I81():
        i56_1 = Dashboard_M8_Alt.I56()
        return i56_1

@register(Dashboard_M8_Alt)
class J81():
    # 'Dashboard_M8_Alt'!J81
    value = 492.070175541
    formula = "=J56"
    @eval_fn
    def J81():
        j56_1 = Dashboard_M8_Alt.J56()
        return j56_1

@register(Dashboard_M8_Alt)
class K81():
    # 'Dashboard_M8_Alt'!K81
    value = 521.954475559
    formula = "=K56"
    @eval_fn
    def K81():
        k56_1 = Dashboard_M8_Alt.K56()
        return k56_1

@register(Dashboard_M8_Alt)
class L81():
    # 'Dashboard_M8_Alt'!L81
    value = 830.084436286
    formula = "=L56"
    @eval_fn
    def L81():
        l56_1 = Dashboard_M8_Alt.L56()
        return l56_1

@register(Dashboard_M8_Alt)
class M81():
    # 'Dashboard_M8_Alt'!M81
    value = 998.492561276
    formula = "=M56"
    @eval_fn
    def M81():
        m56_1 = Dashboard_M8_Alt.M56()
        return m56_1

@register(Dashboard_M8_Alt)
class N81():
    # 'Dashboard_M8_Alt'!N81
    value = 1097.09768772
    formula = "=N56"
    @eval_fn
    def N81():
        n56_1 = Dashboard_M8_Alt.N56()
        return n56_1

@register(Dashboard_M8_Alt)
class O81():
    # 'Dashboard_M8_Alt'!O81
    value = 1581.50656217
    formula = "=O56"
    @eval_fn
    def O81():
        o56_1 = Dashboard_M8_Alt.O56()
        return o56_1

@register(Dashboard_M8_Alt)
class P81():
    # 'Dashboard_M8_Alt'!P81
    value = 925.457589754
    formula = "=P56"
    @eval_fn
    def P81():
        p56_1 = Dashboard_M8_Alt.P56()
        return p56_1

@register(Dashboard_M8_Alt)
class Q81():
    # 'Dashboard_M8_Alt'!Q81
    value = 1275.15309137
    formula = "=Q56"
    @eval_fn
    def Q81():
        q56_1 = Dashboard_M8_Alt.Q56()
        return q56_1

@register(Dashboard_M8_Alt)
class R81():
    # 'Dashboard_M8_Alt'!R81
    value = 1761.81655405
    formula = "=R56"
    @eval_fn
    def R81():
        r56_1 = Dashboard_M8_Alt.R56()
        return r56_1

@register(Dashboard_M8_Alt)
class S81():
    # 'Dashboard_M8_Alt'!S81
    value = 1860.97919473
    formula = "=S56"
    @eval_fn
    def S81():
        s56_1 = Dashboard_M8_Alt.S56()
        return s56_1

@register(Dashboard_M8_Alt)
class T81():
    # 'Dashboard_M8_Alt'!T81
    value = 1687.19152107
    formula = "=T56"
    @eval_fn
    def T81():
        t56_1 = Dashboard_M8_Alt.T56()
        return t56_1

@register(Dashboard_M8_Alt)
class U81():
    # 'Dashboard_M8_Alt'!U81
    value = "#N/A"
    formula = "=U56"
    @eval_fn
    def U81():
        u56_1 = Dashboard_M8_Alt.U56()
        return u56_1

@register(Dashboard_M8_Alt)
class V81():
    # 'Dashboard_M8_Alt'!V81
    value = "#N/A"
    formula = "=V56"
    @eval_fn
    def V81():
        v56_1 = Dashboard_M8_Alt.V56()
        return v56_1

@register(Dashboard_M8_Alt)
class W81():
    # 'Dashboard_M8_Alt'!W81
    value = "#N/A"
    formula = "=W56"
    @eval_fn
    def W81():
        w56_1 = Dashboard_M8_Alt.W56()
        return w56_1

@register(Dashboard_M8_Alt)
class X81():
    # 'Dashboard_M8_Alt'!X81
    value = "#N/A"
    formula = "=X56"
    @eval_fn
    def X81():
        x56_1 = Dashboard_M8_Alt.X56()
        return x56_1

@register(Dashboard_M8_Alt)
class Y81():
    # 'Dashboard_M8_Alt'!Y81
    value = "#N/A"
    formula = "=Y56"
    @eval_fn
    def Y81():
        y56_1 = Dashboard_M8_Alt.Y56()
        return y56_1

@register(Dashboard_M8_Alt)
class Z81():
    # 'Dashboard_M8_Alt'!Z81
    value = "#N/A"
    formula = "=Z56"
    @eval_fn
    def Z81():
        z56_1 = Dashboard_M8_Alt.Z56()
        return z56_1

@register(Dashboard_M8_Alt)
class AA81():
    # 'Dashboard_M8_Alt'!AA81
    value = "#N/A"
    formula = "=AA56"
    @eval_fn
    def AA81():
        aa56_1 = Dashboard_M8_Alt.AA56()
        return aa56_1

@register(Dashboard_M8_Alt)
class AB81():
    # 'Dashboard_M8_Alt'!AB81
    value = "#N/A"
    formula = "=AB56"
    @eval_fn
    def AB81():
        ab56_1 = Dashboard_M8_Alt.AB56()
        return ab56_1

@register(Dashboard_M8_Alt)
class AC81():
    # 'Dashboard_M8_Alt'!AC81
    value = "#N/A"
    formula = "=AC56"
    @eval_fn
    def AC81():
        ac56_1 = Dashboard_M8_Alt.AC56()
        return ac56_1

@register(Dashboard_M8_Alt)
class AD81():
    # 'Dashboard_M8_Alt'!AD81
    value = "#N/A"
    formula = "=AD56"
    @eval_fn
    def AD81():
        ad56_1 = Dashboard_M8_Alt.AD56()
        return ad56_1

@register(Dashboard_M8_Alt)
class AE81():
    # 'Dashboard_M8_Alt'!AE81
    value = "#N/A"
    formula = "=AE56"
    @eval_fn
    def AE81():
        ae56_1 = Dashboard_M8_Alt.AE56()
        return ae56_1

@register(Dashboard_M8_Alt)
class AF81():
    # 'Dashboard_M8_Alt'!AF81
    value = "#N/A"
    formula = "=AF56"
    @eval_fn
    def AF81():
        af56_1 = Dashboard_M8_Alt.AF56()
        return af56_1

@register(Dashboard_M8_Alt)
class AG81():
    # 'Dashboard_M8_Alt'!AG81
    value = "#N/A"
    formula = "=AG56"
    @eval_fn
    def AG81():
        ag56_1 = Dashboard_M8_Alt.AG56()
        return ag56_1

@register(Dashboard_M8_Alt)
class AH81():
    # 'Dashboard_M8_Alt'!AH81
    value = "#N/A"
    formula = "=AH56"
    @eval_fn
    def AH81():
        ah56_1 = Dashboard_M8_Alt.AH56()
        return ah56_1

@register(Dashboard_M8_Alt)
class AI81():
    # 'Dashboard_M8_Alt'!AI81
    value = "#N/A"
    formula = "=AI56"
    @eval_fn
    def AI81():
        ai56_1 = Dashboard_M8_Alt.AI56()
        return ai56_1

@register(Dashboard_M8_Alt)
class AJ81():
    # 'Dashboard_M8_Alt'!AJ81
    value = "#N/A"
    formula = "=AJ56"
    @eval_fn
    def AJ81():
        aj56_1 = Dashboard_M8_Alt.AJ56()
        return aj56_1

@register(Dashboard_M8_Alt)
class AK81():
    # 'Dashboard_M8_Alt'!AK81
    value = "#N/A"
    formula = "=AK56"
    @eval_fn
    def AK81():
        ak56_1 = Dashboard_M8_Alt.AK56()
        return ak56_1

@register(Dashboard_M8_Alt)
class B82():
    # 'Dashboard_M8_Alt'!B82
    value = "All Fuels (Actual)"

@register(Dashboard_M8_Alt)
class I82():
    # 'Dashboard_M8_Alt'!I82
    value = 490.73925
    formula = "=I70"
    @eval_fn
    def I82():
        i70_1 = Dashboard_M8_Alt.I70()
        return i70_1

@register(Dashboard_M8_Alt)
class J82():
    # 'Dashboard_M8_Alt'!J82
    value = 483.8615
    formula = "=J70"
    @eval_fn
    def J82():
        j70_1 = Dashboard_M8_Alt.J70()
        return j70_1

@register(Dashboard_M8_Alt)
class K82():
    # 'Dashboard_M8_Alt'!K82
    value = 519.2015
    formula = "=K70"
    @eval_fn
    def K82():
        k70_1 = Dashboard_M8_Alt.K70()
        return k70_1

@register(Dashboard_M8_Alt)
class L82():
    # 'Dashboard_M8_Alt'!L82
    value = 795.70143
    formula = "=L70"
    @eval_fn
    def L82():
        l70_1 = Dashboard_M8_Alt.L70()
        return l70_1

@register(Dashboard_M8_Alt)
class M82():
    # 'Dashboard_M8_Alt'!M82
    value = 962.04287
    formula = "=M70"
    @eval_fn
    def M82():
        m70_1 = Dashboard_M8_Alt.M70()
        return m70_1

@register(Dashboard_M8_Alt)
class N82():
    # 'Dashboard_M8_Alt'!N82
    value = 1035.79781
    formula = "=N70"
    @eval_fn
    def N82():
        n70_1 = Dashboard_M8_Alt.N70()
        return n70_1

@register(Dashboard_M8_Alt)
class O82():
    # 'Dashboard_M8_Alt'!O82
    value = 1453.95196
    formula = "=O70"
    @eval_fn
    def O82():
        o70_1 = Dashboard_M8_Alt.O70()
        return o70_1

@register(Dashboard_M8_Alt)
class P82():
    # 'Dashboard_M8_Alt'!P82
    value = 852.48182
    formula = "=P70"
    @eval_fn
    def P82():
        p70_1 = Dashboard_M8_Alt.P70()
        return p70_1

@register(Dashboard_M8_Alt)
class Q82():
    # 'Dashboard_M8_Alt'!Q82
    value = 1142.12472
    formula = "=Q70"
    @eval_fn
    def Q82():
        q70_1 = Dashboard_M8_Alt.Q70()
        return q70_1

@register(Dashboard_M8_Alt)
class R82():
    # 'Dashboard_M8_Alt'!R82
    value = 1593.79444
    formula = "=R70"
    @eval_fn
    def R82():
        r70_1 = Dashboard_M8_Alt.R70()
        return r70_1

@register(Dashboard_M8_Alt)
class S82():
    # 'Dashboard_M8_Alt'!S82
    value = 1619.38611
    formula = "=S70"
    @eval_fn
    def S82():
        s70_1 = Dashboard_M8_Alt.S70()
        return s70_1

@register(Dashboard_M8_Alt)
class T82():
    # 'Dashboard_M8_Alt'!T82
    value = 1481.87859
    formula = "=T70"
    @eval_fn
    def T82():
        t70_1 = Dashboard_M8_Alt.T70()
        return t70_1

@register(Dashboard_M8_Alt)
class U82():
    # 'Dashboard_M8_Alt'!U82
    value = "#N/A"
    formula = "=U70"
    @eval_fn
    def U82():
        u70_1 = Dashboard_M8_Alt.U70()
        return u70_1

@register(Dashboard_M8_Alt)
class V82():
    # 'Dashboard_M8_Alt'!V82
    value = "#N/A"
    formula = "=V70"
    @eval_fn
    def V82():
        v70_1 = Dashboard_M8_Alt.V70()
        return v70_1

@register(Dashboard_M8_Alt)
class W82():
    # 'Dashboard_M8_Alt'!W82
    value = "#N/A"
    formula = "=W70"
    @eval_fn
    def W82():
        w70_1 = Dashboard_M8_Alt.W70()
        return w70_1

@register(Dashboard_M8_Alt)
class X82():
    # 'Dashboard_M8_Alt'!X82
    value = "#N/A"
    formula = "=X70"
    @eval_fn
    def X82():
        x70_1 = Dashboard_M8_Alt.X70()
        return x70_1

@register(Dashboard_M8_Alt)
class Y82():
    # 'Dashboard_M8_Alt'!Y82
    value = "#N/A"
    formula = "=Y70"
    @eval_fn
    def Y82():
        y70_1 = Dashboard_M8_Alt.Y70()
        return y70_1

@register(Dashboard_M8_Alt)
class Z82():
    # 'Dashboard_M8_Alt'!Z82
    value = "#N/A"
    formula = "=Z70"
    @eval_fn
    def Z82():
        z70_1 = Dashboard_M8_Alt.Z70()
        return z70_1

@register(Dashboard_M8_Alt)
class AA82():
    # 'Dashboard_M8_Alt'!AA82
    value = "#N/A"
    formula = "=AA70"
    @eval_fn
    def AA82():
        aa70_1 = Dashboard_M8_Alt.AA70()
        return aa70_1

@register(Dashboard_M8_Alt)
class AB82():
    # 'Dashboard_M8_Alt'!AB82
    value = "#N/A"
    formula = "=AB70"
    @eval_fn
    def AB82():
        ab70_1 = Dashboard_M8_Alt.AB70()
        return ab70_1

@register(Dashboard_M8_Alt)
class AC82():
    # 'Dashboard_M8_Alt'!AC82
    value = "#N/A"
    formula = "=AC70"
    @eval_fn
    def AC82():
        ac70_1 = Dashboard_M8_Alt.AC70()
        return ac70_1

@register(Dashboard_M8_Alt)
class AD82():
    # 'Dashboard_M8_Alt'!AD82
    value = "#N/A"
    formula = "=AD70"
    @eval_fn
    def AD82():
        ad70_1 = Dashboard_M8_Alt.AD70()
        return ad70_1

@register(Dashboard_M8_Alt)
class AE82():
    # 'Dashboard_M8_Alt'!AE82
    value = "#N/A"
    formula = "=AE70"
    @eval_fn
    def AE82():
        ae70_1 = Dashboard_M8_Alt.AE70()
        return ae70_1

@register(Dashboard_M8_Alt)
class AF82():
    # 'Dashboard_M8_Alt'!AF82
    value = "#N/A"
    formula = "=AF70"
    @eval_fn
    def AF82():
        af70_1 = Dashboard_M8_Alt.AF70()
        return af70_1

@register(Dashboard_M8_Alt)
class AG82():
    # 'Dashboard_M8_Alt'!AG82
    value = "#N/A"
    formula = "=AG70"
    @eval_fn
    def AG82():
        ag70_1 = Dashboard_M8_Alt.AG70()
        return ag70_1

@register(Dashboard_M8_Alt)
class AH82():
    # 'Dashboard_M8_Alt'!AH82
    value = "#N/A"
    formula = "=AH70"
    @eval_fn
    def AH82():
        ah70_1 = Dashboard_M8_Alt.AH70()
        return ah70_1

@register(Dashboard_M8_Alt)
class AI82():
    # 'Dashboard_M8_Alt'!AI82
    value = "#N/A"
    formula = "=AI70"
    @eval_fn
    def AI82():
        ai70_1 = Dashboard_M8_Alt.AI70()
        return ai70_1

@register(Dashboard_M8_Alt)
class AJ82():
    # 'Dashboard_M8_Alt'!AJ82
    value = "#N/A"
    formula = "=AJ70"
    @eval_fn
    def AJ82():
        aj70_1 = Dashboard_M8_Alt.AJ70()
        return aj70_1

@register(Dashboard_M8_Alt)
class AK82():
    # 'Dashboard_M8_Alt'!AK82
    value = "#N/A"
    formula = "=AK70"
    @eval_fn
    def AK82():
        ak70_1 = Dashboard_M8_Alt.AK70()
        return ak70_1