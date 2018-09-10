# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Dashboard_M16_EEPS = Worksheet('Dashboard_M16_EEPS', 10, 10)



@register(Dashboard_M16_EEPS)
class A1():
    # 'Dashboard_M16_EEPS'!A1
    value = "Metric 16: MWh and MWh per year energy savings from energy efficiency programs"

@register(Dashboard_M16_EEPS)
class A2():
    # 'Dashboard_M16_EEPS'!A2
    value = "http://puc.hawaii.gov/reports/puc-annual-reports "

@register(Dashboard_M16_EEPS)
class A3():
    # 'Dashboard_M16_EEPS'!A3
    value = "Q: Use displacement technolgoies too?"

@register(Dashboard_M16_EEPS)
class T3():
    # 'Dashboard_M16_EEPS'!T3
    value = 30

@register(Dashboard_M16_EEPS)
class A4():
    # 'Dashboard_M16_EEPS'!A4
    value = "http://www.eia.gov/electricity/data/state/annual_generation_state.xls"

@register(Dashboard_M16_EEPS)
class T4():
    # 'Dashboard_M16_EEPS'!T4
    value = 30

@register(Dashboard_M16_EEPS)
class D5():
    # 'Dashboard_M16_EEPS'!D5
    value = "Units"

@register(Dashboard_M16_EEPS)
class E5():
    # 'Dashboard_M16_EEPS'!E5
    value = "Source"

@register(Dashboard_M16_EEPS)
class F5():
    # 'Dashboard_M16_EEPS'!F5
    value = "Notes"

@register(Dashboard_M16_EEPS)
class G5():
    # 'Dashboard_M16_EEPS'!G5
    value = 1999

@register(Dashboard_M16_EEPS)
class H5():
    # 'Dashboard_M16_EEPS'!H5
    value = 2000

@register(Dashboard_M16_EEPS)
class I5():
    # 'Dashboard_M16_EEPS'!I5
    value = 2001

@register(Dashboard_M16_EEPS)
class J5():
    # 'Dashboard_M16_EEPS'!J5
    value = 2002

@register(Dashboard_M16_EEPS)
class K5():
    # 'Dashboard_M16_EEPS'!K5
    value = 2003

@register(Dashboard_M16_EEPS)
class L5():
    # 'Dashboard_M16_EEPS'!L5
    value = 2004

@register(Dashboard_M16_EEPS)
class M5():
    # 'Dashboard_M16_EEPS'!M5
    value = 2005

@register(Dashboard_M16_EEPS)
class N5():
    # 'Dashboard_M16_EEPS'!N5
    value = 2006

@register(Dashboard_M16_EEPS)
class O5():
    # 'Dashboard_M16_EEPS'!O5
    value = 2007

@register(Dashboard_M16_EEPS)
class P5():
    # 'Dashboard_M16_EEPS'!P5
    value = 2008

@register(Dashboard_M16_EEPS)
class Q5():
    # 'Dashboard_M16_EEPS'!Q5
    value = 2009

@register(Dashboard_M16_EEPS)
class R5():
    # 'Dashboard_M16_EEPS'!R5
    value = 2010

@register(Dashboard_M16_EEPS)
class S5():
    # 'Dashboard_M16_EEPS'!S5
    value = 2011

@register(Dashboard_M16_EEPS)
class T5():
    # 'Dashboard_M16_EEPS'!T5
    value = 2012

@register(Dashboard_M16_EEPS)
class U5():
    # 'Dashboard_M16_EEPS'!U5
    value = 2013

@register(Dashboard_M16_EEPS)
class V5():
    # 'Dashboard_M16_EEPS'!V5
    value = 2014

@register(Dashboard_M16_EEPS)
class W5():
    # 'Dashboard_M16_EEPS'!W5
    value = 2015

@register(Dashboard_M16_EEPS)
class X5():
    # 'Dashboard_M16_EEPS'!X5
    value = 2016

@register(Dashboard_M16_EEPS)
class Y5():
    # 'Dashboard_M16_EEPS'!Y5
    value = 2017

@register(Dashboard_M16_EEPS)
class Z5():
    # 'Dashboard_M16_EEPS'!Z5
    value = 2018

@register(Dashboard_M16_EEPS)
class AA5():
    # 'Dashboard_M16_EEPS'!AA5
    value = 2019

@register(Dashboard_M16_EEPS)
class AB5():
    # 'Dashboard_M16_EEPS'!AB5
    value = 2020

@register(Dashboard_M16_EEPS)
class AC5():
    # 'Dashboard_M16_EEPS'!AC5
    value = 2021

@register(Dashboard_M16_EEPS)
class AD5():
    # 'Dashboard_M16_EEPS'!AD5
    value = 2022

@register(Dashboard_M16_EEPS)
class AE5():
    # 'Dashboard_M16_EEPS'!AE5
    value = 2023

@register(Dashboard_M16_EEPS)
class AF5():
    # 'Dashboard_M16_EEPS'!AF5
    value = 2024

@register(Dashboard_M16_EEPS)
class AG5():
    # 'Dashboard_M16_EEPS'!AG5
    value = 2025

@register(Dashboard_M16_EEPS)
class AH5():
    # 'Dashboard_M16_EEPS'!AH5
    value = 2026

@register(Dashboard_M16_EEPS)
class AI5():
    # 'Dashboard_M16_EEPS'!AI5
    value = 2027

@register(Dashboard_M16_EEPS)
class AJ5():
    # 'Dashboard_M16_EEPS'!AJ5
    value = 2028

@register(Dashboard_M16_EEPS)
class AK5():
    # 'Dashboard_M16_EEPS'!AK5
    value = 2029

@register(Dashboard_M16_EEPS)
class AL5():
    # 'Dashboard_M16_EEPS'!AL5
    value = 2030

@register(Dashboard_M16_EEPS)
class A6():
    # 'Dashboard_M16_EEPS'!A6
    value = '''TEusy - Total Energy source "s" sold by utilitiy "u" in year "y"'''

@register(Dashboard_M16_EEPS)
class A7():
    # 'Dashboard_M16_EEPS'!A7
    value = "HECOTotal Renewable"
    formula = "=CONCATENATE(C7,B7)"
    @eval_fn
    def A7():
        c7_1 = Dashboard_M16_EEPS.C7()
        b7_1 = Dashboard_M16_EEPS.B7()
        var_1 = CONCATENATE(c7_1, b7_1)
        return var_1

@register(Dashboard_M16_EEPS)
class B7():
    # 'Dashboard_M16_EEPS'!B7
    value = "Total Renewable"

@register(Dashboard_M16_EEPS)
class C7():
    # 'Dashboard_M16_EEPS'!C7
    value = "HECO"

@register(Dashboard_M16_EEPS)
class D7():
    # 'Dashboard_M16_EEPS'!D7
    value = "MWh"

@register(Dashboard_M16_EEPS)
class E7():
    # 'Dashboard_M16_EEPS'!E7
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Dashboard_M16_EEPS)
class G7():
    # 'Dashboard_M16_EEPS'!G7
    value = 8998000
    formula = "='Input RPS'!G125"
    @eval_fn
    def G7():
        g125_1 = Input_RPS.G125()
        return g125_1

@register(Dashboard_M16_EEPS)
class H7():
    # 'Dashboard_M16_EEPS'!H7
    value = 7212000
    formula = "='Input RPS'!H125"
    @eval_fn
    def H7():
        h125_1 = Input_RPS.H125()
        return h125_1

@register(Dashboard_M16_EEPS)
class I7():
    # 'Dashboard_M16_EEPS'!I7
    value = 7277000
    formula = "='Input RPS'!I125"
    @eval_fn
    def I7():
        i125_1 = Input_RPS.I125()
        return i125_1

@register(Dashboard_M16_EEPS)
class J7():
    # 'Dashboard_M16_EEPS'!J7
    value = 7390000
    formula = "='Input RPS'!J125"
    @eval_fn
    def J7():
        j125_1 = Input_RPS.J125()
        return j125_1

@register(Dashboard_M16_EEPS)
class K7():
    # 'Dashboard_M16_EEPS'!K7
    value = 7522000
    formula = "='Input RPS'!K125"
    @eval_fn
    def K7():
        k125_1 = Input_RPS.K125()
        return k125_1

@register(Dashboard_M16_EEPS)
class L7():
    # 'Dashboard_M16_EEPS'!L7
    value = 7733000
    formula = "='Input RPS'!L125"
    @eval_fn
    def L7():
        l125_1 = Input_RPS.L125()
        return l125_1

@register(Dashboard_M16_EEPS)
class M7():
    # 'Dashboard_M16_EEPS'!M7
    value = 7721000
    formula = "='Input RPS'!M125"
    @eval_fn
    def M7():
        m125_1 = Input_RPS.M125()
        return m125_1

@register(Dashboard_M16_EEPS)
class N7():
    # 'Dashboard_M16_EEPS'!N7
    value = 7701000
    formula = "='Input RPS'!N125"
    @eval_fn
    def N7():
        n125_1 = Input_RPS.N125()
        return n125_1

@register(Dashboard_M16_EEPS)
class O7():
    # 'Dashboard_M16_EEPS'!O7
    value = 7675000
    formula = "='Input RPS'!O125"
    @eval_fn
    def O7():
        o125_1 = Input_RPS.O125()
        return o125_1

@register(Dashboard_M16_EEPS)
class P7():
    # 'Dashboard_M16_EEPS'!P7
    value = 7555962
    formula = "='Input RPS'!P125"
    @eval_fn
    def P7():
        p125_1 = Input_RPS.P125()
        return p125_1

@register(Dashboard_M16_EEPS)
class Q7():
    # 'Dashboard_M16_EEPS'!Q7
    value = 7377537
    formula = "='Input RPS'!Q125"
    @eval_fn
    def Q7():
        q125_1 = Input_RPS.Q125()
        return q125_1

@register(Dashboard_M16_EEPS)
class R7():
    # 'Dashboard_M16_EEPS'!R7
    value = 7277229
    formula = "='Input RPS'!R125"
    @eval_fn
    def R7():
        r125_1 = Input_RPS.R125()
        return r125_1

@register(Dashboard_M16_EEPS)
class S7():
    # 'Dashboard_M16_EEPS'!S7
    value = 7242311
    formula = "='Input RPS'!S125"
    @eval_fn
    def S7():
        s125_1 = Input_RPS.S125()
        return s125_1

@register(Dashboard_M16_EEPS)
class T7():
    # 'Dashboard_M16_EEPS'!T7
    value = 6975996
    formula = "='Input RPS'!T125"
    @eval_fn
    def T7():
        t125_1 = Input_RPS.T125()
        return t125_1

@register(Dashboard_M16_EEPS)
class U7():
    # 'Dashboard_M16_EEPS'!U7
    value = 6858536
    formula = "='Input RPS'!U125"
    @eval_fn
    def U7():
        u125_1 = Input_RPS.U125()
        return u125_1

@register(Dashboard_M16_EEPS)
class V7():
    # 'Dashboard_M16_EEPS'!V7
    value = 6781665
    formula = "='Input RPS'!V125"
    @eval_fn
    def V7():
        v125_1 = Input_RPS.V125()
        return v125_1

@register(Dashboard_M16_EEPS)
class W7():
    # 'Dashboard_M16_EEPS'!W7
    value = 6754083
    formula = "='Input RPS'!W125"
    @eval_fn
    def W7():
        w125_1 = Input_RPS.W125()
        return w125_1

@register(Dashboard_M16_EEPS)
class X7():
    # 'Dashboard_M16_EEPS'!X7
    value = 0
    formula = "='Input RPS'!X125"
    @eval_fn
    def X7():
        x125_1 = Input_RPS.X125()
        return x125_1

@register(Dashboard_M16_EEPS)
class Y7():
    # 'Dashboard_M16_EEPS'!Y7
    value = 0
    formula = "='Input RPS'!Y125"
    @eval_fn
    def Y7():
        y125_1 = Input_RPS.Y125()
        return y125_1

@register(Dashboard_M16_EEPS)
class Z7():
    # 'Dashboard_M16_EEPS'!Z7
    value = 0
    formula = "='Input RPS'!Z125"
    @eval_fn
    def Z7():
        z125_1 = Input_RPS.Z125()
        return z125_1

@register(Dashboard_M16_EEPS)
class AA7():
    # 'Dashboard_M16_EEPS'!AA7
    value = 0
    formula = "='Input RPS'!AA125"
    @eval_fn
    def AA7():
        aa125_1 = Input_RPS.AA125()
        return aa125_1

@register(Dashboard_M16_EEPS)
class AB7():
    # 'Dashboard_M16_EEPS'!AB7
    value = 0
    formula = "='Input RPS'!AB125"
    @eval_fn
    def AB7():
        ab125_1 = Input_RPS.AB125()
        return ab125_1

@register(Dashboard_M16_EEPS)
class AC7():
    # 'Dashboard_M16_EEPS'!AC7
    value = 0
    formula = "='Input RPS'!AC125"
    @eval_fn
    def AC7():
        ac125_1 = Input_RPS.AC125()
        return ac125_1

@register(Dashboard_M16_EEPS)
class AD7():
    # 'Dashboard_M16_EEPS'!AD7
    value = 0
    formula = "='Input RPS'!AD125"
    @eval_fn
    def AD7():
        ad125_1 = Input_RPS.AD125()
        return ad125_1

@register(Dashboard_M16_EEPS)
class AE7():
    # 'Dashboard_M16_EEPS'!AE7
    value = 0
    formula = "='Input RPS'!AE125"
    @eval_fn
    def AE7():
        ae125_1 = Input_RPS.AE125()
        return ae125_1

@register(Dashboard_M16_EEPS)
class AF7():
    # 'Dashboard_M16_EEPS'!AF7
    value = 0
    formula = "='Input RPS'!AF125"
    @eval_fn
    def AF7():
        af125_1 = Input_RPS.AF125()
        return af125_1

@register(Dashboard_M16_EEPS)
class AG7():
    # 'Dashboard_M16_EEPS'!AG7
    value = 0
    formula = "='Input RPS'!AG125"
    @eval_fn
    def AG7():
        ag125_1 = Input_RPS.AG125()
        return ag125_1

@register(Dashboard_M16_EEPS)
class AH7():
    # 'Dashboard_M16_EEPS'!AH7
    value = 0
    formula = "='Input RPS'!AH125"
    @eval_fn
    def AH7():
        ah125_1 = Input_RPS.AH125()
        return ah125_1

@register(Dashboard_M16_EEPS)
class AI7():
    # 'Dashboard_M16_EEPS'!AI7
    value = 0
    formula = "='Input RPS'!AI125"
    @eval_fn
    def AI7():
        ai125_1 = Input_RPS.AI125()
        return ai125_1

@register(Dashboard_M16_EEPS)
class AJ7():
    # 'Dashboard_M16_EEPS'!AJ7
    value = 0
    formula = "='Input RPS'!AJ125"
    @eval_fn
    def AJ7():
        aj125_1 = Input_RPS.AJ125()
        return aj125_1

@register(Dashboard_M16_EEPS)
class AK7():
    # 'Dashboard_M16_EEPS'!AK7
    value = 0
    formula = "='Input RPS'!AK125"
    @eval_fn
    def AK7():
        ak125_1 = Input_RPS.AK125()
        return ak125_1

@register(Dashboard_M16_EEPS)
class AL7():
    # 'Dashboard_M16_EEPS'!AL7
    value = 0
    formula = "='Input RPS'!AL125"
    @eval_fn
    def AL7():
        al125_1 = Input_RPS.AL125()
        return al125_1

@register(Dashboard_M16_EEPS)
class A8():
    # 'Dashboard_M16_EEPS'!A8
    value = "HELCOTotal Renewable"
    formula = "=CONCATENATE(C8,B8)"
    @eval_fn
    def A8():
        c8_1 = Dashboard_M16_EEPS.C8()
        b8_1 = Dashboard_M16_EEPS.B8()
        var_1 = CONCATENATE(c8_1, b8_1)
        return var_1

@register(Dashboard_M16_EEPS)
class B8():
    # 'Dashboard_M16_EEPS'!B8
    value = "Total Renewable"

@register(Dashboard_M16_EEPS)
class C8():
    # 'Dashboard_M16_EEPS'!C8
    value = "HELCO"

@register(Dashboard_M16_EEPS)
class D8():
    # 'Dashboard_M16_EEPS'!D8
    value = "MWh"

@register(Dashboard_M16_EEPS)
class E8():
    # 'Dashboard_M16_EEPS'!E8
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Dashboard_M16_EEPS)
class G8():
    # 'Dashboard_M16_EEPS'!G8
    value = 922000
    formula = "='Input RPS'!G126"
    @eval_fn
    def G8():
        g126_1 = Input_RPS.G126()
        return g126_1

@register(Dashboard_M16_EEPS)
class H8():
    # 'Dashboard_M16_EEPS'!H8
    value = 954000
    formula = "='Input RPS'!H126"
    @eval_fn
    def H8():
        h126_1 = Input_RPS.H126()
        return h126_1

@register(Dashboard_M16_EEPS)
class I8():
    # 'Dashboard_M16_EEPS'!I8
    value = 959000
    formula = "='Input RPS'!I126"
    @eval_fn
    def I8():
        i126_1 = Input_RPS.I126()
        return i126_1

@register(Dashboard_M16_EEPS)
class J8():
    # 'Dashboard_M16_EEPS'!J8
    value = 995000
    formula = "='Input RPS'!J126"
    @eval_fn
    def J8():
        j126_1 = Input_RPS.J126()
        return j126_1

@register(Dashboard_M16_EEPS)
class K8():
    # 'Dashboard_M16_EEPS'!K8
    value = 1046000
    formula = "='Input RPS'!K126"
    @eval_fn
    def K8():
        k126_1 = Input_RPS.K126()
        return k126_1

@register(Dashboard_M16_EEPS)
class L8():
    # 'Dashboard_M16_EEPS'!L8
    value = 1083000
    formula = "='Input RPS'!L126"
    @eval_fn
    def L8():
        l126_1 = Input_RPS.L126()
        return l126_1

@register(Dashboard_M16_EEPS)
class M8():
    # 'Dashboard_M16_EEPS'!M8
    value = 1117000
    formula = "='Input RPS'!M126"
    @eval_fn
    def M8():
        m126_1 = Input_RPS.M126()
        return m126_1

@register(Dashboard_M16_EEPS)
class N8():
    # 'Dashboard_M16_EEPS'!N8
    value = 1149000
    formula = "='Input RPS'!N126"
    @eval_fn
    def N8():
        n126_1 = Input_RPS.N126()
        return n126_1

@register(Dashboard_M16_EEPS)
class O8():
    # 'Dashboard_M16_EEPS'!O8
    value = 1163000
    formula = "='Input RPS'!O126"
    @eval_fn
    def O8():
        o126_1 = Input_RPS.O126()
        return o126_1

@register(Dashboard_M16_EEPS)
class P8():
    # 'Dashboard_M16_EEPS'!P8
    value = 1141030
    formula = "='Input RPS'!P126"
    @eval_fn
    def P8():
        p126_1 = Input_RPS.P126()
        return p126_1

@register(Dashboard_M16_EEPS)
class Q8():
    # 'Dashboard_M16_EEPS'!Q8
    value = 1119881
    formula = "='Input RPS'!Q126"
    @eval_fn
    def Q8():
        q126_1 = Input_RPS.Q126()
        return q126_1

@register(Dashboard_M16_EEPS)
class R8():
    # 'Dashboard_M16_EEPS'!R8
    value = 1109783
    formula = "='Input RPS'!R126"
    @eval_fn
    def R8():
        r126_1 = Input_RPS.R126()
        return r126_1

@register(Dashboard_M16_EEPS)
class S8():
    # 'Dashboard_M16_EEPS'!S8
    value = 1103572
    formula = "='Input RPS'!S126"
    @eval_fn
    def S8():
        s126_1 = Input_RPS.S126()
        return s126_1

@register(Dashboard_M16_EEPS)
class T8():
    # 'Dashboard_M16_EEPS'!T8
    value = 1085171
    formula = "='Input RPS'!T126"
    @eval_fn
    def T8():
        t126_1 = Input_RPS.T126()
        return t126_1

@register(Dashboard_M16_EEPS)
class U8():
    # 'Dashboard_M16_EEPS'!U8
    value = 1076104
    formula = "='Input RPS'!U126"
    @eval_fn
    def U8():
        u126_1 = Input_RPS.U126()
        return u126_1

@register(Dashboard_M16_EEPS)
class V8():
    # 'Dashboard_M16_EEPS'!V8
    value = 1062521
    formula = "='Input RPS'!V126"
    @eval_fn
    def V8():
        v126_1 = Input_RPS.V126()
        return v126_1

@register(Dashboard_M16_EEPS)
class W8():
    # 'Dashboard_M16_EEPS'!W8
    value = 1064785
    formula = "='Input RPS'!W126"
    @eval_fn
    def W8():
        w126_1 = Input_RPS.W126()
        return w126_1

@register(Dashboard_M16_EEPS)
class X8():
    # 'Dashboard_M16_EEPS'!X8
    value = 0
    formula = "='Input RPS'!X126"
    @eval_fn
    def X8():
        x126_1 = Input_RPS.X126()
        return x126_1

@register(Dashboard_M16_EEPS)
class Y8():
    # 'Dashboard_M16_EEPS'!Y8
    value = 0
    formula = "='Input RPS'!Y126"
    @eval_fn
    def Y8():
        y126_1 = Input_RPS.Y126()
        return y126_1

@register(Dashboard_M16_EEPS)
class Z8():
    # 'Dashboard_M16_EEPS'!Z8
    value = 0
    formula = "='Input RPS'!Z126"
    @eval_fn
    def Z8():
        z126_1 = Input_RPS.Z126()
        return z126_1

@register(Dashboard_M16_EEPS)
class AA8():
    # 'Dashboard_M16_EEPS'!AA8
    value = 0
    formula = "='Input RPS'!AA126"
    @eval_fn
    def AA8():
        aa126_1 = Input_RPS.AA126()
        return aa126_1

@register(Dashboard_M16_EEPS)
class AB8():
    # 'Dashboard_M16_EEPS'!AB8
    value = 0
    formula = "='Input RPS'!AB126"
    @eval_fn
    def AB8():
        ab126_1 = Input_RPS.AB126()
        return ab126_1

@register(Dashboard_M16_EEPS)
class AC8():
    # 'Dashboard_M16_EEPS'!AC8
    value = 0
    formula = "='Input RPS'!AC126"
    @eval_fn
    def AC8():
        ac126_1 = Input_RPS.AC126()
        return ac126_1

@register(Dashboard_M16_EEPS)
class AD8():
    # 'Dashboard_M16_EEPS'!AD8
    value = 0
    formula = "='Input RPS'!AD126"
    @eval_fn
    def AD8():
        ad126_1 = Input_RPS.AD126()
        return ad126_1

@register(Dashboard_M16_EEPS)
class AE8():
    # 'Dashboard_M16_EEPS'!AE8
    value = 0
    formula = "='Input RPS'!AE126"
    @eval_fn
    def AE8():
        ae126_1 = Input_RPS.AE126()
        return ae126_1

@register(Dashboard_M16_EEPS)
class AF8():
    # 'Dashboard_M16_EEPS'!AF8
    value = 0
    formula = "='Input RPS'!AF126"
    @eval_fn
    def AF8():
        af126_1 = Input_RPS.AF126()
        return af126_1

@register(Dashboard_M16_EEPS)
class AG8():
    # 'Dashboard_M16_EEPS'!AG8
    value = 0
    formula = "='Input RPS'!AG126"
    @eval_fn
    def AG8():
        ag126_1 = Input_RPS.AG126()
        return ag126_1

@register(Dashboard_M16_EEPS)
class AH8():
    # 'Dashboard_M16_EEPS'!AH8
    value = 0
    formula = "='Input RPS'!AH126"
    @eval_fn
    def AH8():
        ah126_1 = Input_RPS.AH126()
        return ah126_1

@register(Dashboard_M16_EEPS)
class AI8():
    # 'Dashboard_M16_EEPS'!AI8
    value = 0
    formula = "='Input RPS'!AI126"
    @eval_fn
    def AI8():
        ai126_1 = Input_RPS.AI126()
        return ai126_1

@register(Dashboard_M16_EEPS)
class AJ8():
    # 'Dashboard_M16_EEPS'!AJ8
    value = 0
    formula = "='Input RPS'!AJ126"
    @eval_fn
    def AJ8():
        aj126_1 = Input_RPS.AJ126()
        return aj126_1

@register(Dashboard_M16_EEPS)
class AK8():
    # 'Dashboard_M16_EEPS'!AK8
    value = 0
    formula = "='Input RPS'!AK126"
    @eval_fn
    def AK8():
        ak126_1 = Input_RPS.AK126()
        return ak126_1

@register(Dashboard_M16_EEPS)
class AL8():
    # 'Dashboard_M16_EEPS'!AL8
    value = 0
    formula = "='Input RPS'!AL126"
    @eval_fn
    def AL8():
        al126_1 = Input_RPS.AL126()
        return al126_1

@register(Dashboard_M16_EEPS)
class A9():
    # 'Dashboard_M16_EEPS'!A9
    value = "MECOTotal Renewable"
    formula = "=CONCATENATE(C9,B9)"
    @eval_fn
    def A9():
        c9_1 = Dashboard_M16_EEPS.C9()
        b9_1 = Dashboard_M16_EEPS.B9()
        var_1 = CONCATENATE(c9_1, b9_1)
        return var_1

@register(Dashboard_M16_EEPS)
class B9():
    # 'Dashboard_M16_EEPS'!B9
    value = "Total Renewable"

@register(Dashboard_M16_EEPS)
class C9():
    # 'Dashboard_M16_EEPS'!C9
    value = "MECO"

@register(Dashboard_M16_EEPS)
class D9():
    # 'Dashboard_M16_EEPS'!D9
    value = "MWh"

@register(Dashboard_M16_EEPS)
class E9():
    # 'Dashboard_M16_EEPS'!E9
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Dashboard_M16_EEPS)
class G9():
    # 'Dashboard_M16_EEPS'!G9
    value = 1065000
    formula = "='Input RPS'!G127"
    @eval_fn
    def G9():
        g127_1 = Input_RPS.G127()
        return g127_1

@register(Dashboard_M16_EEPS)
class H9():
    # 'Dashboard_M16_EEPS'!H9
    value = 1106000
    formula = "='Input RPS'!H127"
    @eval_fn
    def H9():
        h127_1 = Input_RPS.H127()
        return h127_1

@register(Dashboard_M16_EEPS)
class I9():
    # 'Dashboard_M16_EEPS'!I9
    value = 1134000
    formula = "='Input RPS'!I127"
    @eval_fn
    def I9():
        i127_1 = Input_RPS.I127()
        return i127_1

@register(Dashboard_M16_EEPS)
class J9():
    # 'Dashboard_M16_EEPS'!J9
    value = 1159000
    formula = "='Input RPS'!J127"
    @eval_fn
    def J9():
        j127_1 = Input_RPS.J127()
        return j127_1

@register(Dashboard_M16_EEPS)
class K9():
    # 'Dashboard_M16_EEPS'!K9
    value = 1207000
    formula = "='Input RPS'!K127"
    @eval_fn
    def K9():
        k127_1 = Input_RPS.K127()
        return k127_1

@register(Dashboard_M16_EEPS)
class L9():
    # 'Dashboard_M16_EEPS'!L9
    value = 1247000
    formula = "='Input RPS'!L127"
    @eval_fn
    def L9():
        l127_1 = Input_RPS.L127()
        return l127_1

@register(Dashboard_M16_EEPS)
class M9():
    # 'Dashboard_M16_EEPS'!M9
    value = 1252000
    formula = "='Input RPS'!M127"
    @eval_fn
    def M9():
        m127_1 = Input_RPS.M127()
        return m127_1

@register(Dashboard_M16_EEPS)
class N9():
    # 'Dashboard_M16_EEPS'!N9
    value = 1266000
    formula = "='Input RPS'!N127"
    @eval_fn
    def N9():
        n127_1 = Input_RPS.N127()
        return n127_1

@register(Dashboard_M16_EEPS)
class O9():
    # 'Dashboard_M16_EEPS'!O9
    value = 1280000
    formula = "='Input RPS'!O127"
    @eval_fn
    def O9():
        o127_1 = Input_RPS.O127()
        return o127_1

@register(Dashboard_M16_EEPS)
class P9():
    # 'Dashboard_M16_EEPS'!P9
    value = 1239228
    formula = "='Input RPS'!P127"
    @eval_fn
    def P9():
        p127_1 = Input_RPS.P127()
        return p127_1

@register(Dashboard_M16_EEPS)
class Q9():
    # 'Dashboard_M16_EEPS'!Q9
    value = 1192243
    formula = "='Input RPS'!Q127"
    @eval_fn
    def Q9():
        q127_1 = Input_RPS.Q127()
        return q127_1

@register(Dashboard_M16_EEPS)
class R9():
    # 'Dashboard_M16_EEPS'!R9
    value = 1191559
    formula = "='Input RPS'!R127"
    @eval_fn
    def R9():
        r127_1 = Input_RPS.R127()
        return r127_1

@register(Dashboard_M16_EEPS)
class S9():
    # 'Dashboard_M16_EEPS'!S9
    value = 1181026
    formula = "='Input RPS'!S127"
    @eval_fn
    def S9():
        s127_1 = Input_RPS.S127()
        return s127_1

@register(Dashboard_M16_EEPS)
class T9():
    # 'Dashboard_M16_EEPS'!T9
    value = 1144832
    formula = "='Input RPS'!T127"
    @eval_fn
    def T9():
        t127_1 = Input_RPS.T127()
        return t127_1

@register(Dashboard_M16_EEPS)
class U9():
    # 'Dashboard_M16_EEPS'!U9
    value = 1134873
    formula = "='Input RPS'!U127"
    @eval_fn
    def U9():
        u127_1 = Input_RPS.U127()
        return u127_1

@register(Dashboard_M16_EEPS)
class V9():
    # 'Dashboard_M16_EEPS'!V9
    value = 1132056
    formula = "='Input RPS'!V127"
    @eval_fn
    def V9():
        v127_1 = Input_RPS.V127()
        return v127_1

@register(Dashboard_M16_EEPS)
class W9():
    # 'Dashboard_M16_EEPS'!W9
    value = 1137630
    formula = "='Input RPS'!W127"
    @eval_fn
    def W9():
        w127_1 = Input_RPS.W127()
        return w127_1

@register(Dashboard_M16_EEPS)
class X9():
    # 'Dashboard_M16_EEPS'!X9
    value = 0
    formula = "='Input RPS'!X127"
    @eval_fn
    def X9():
        x127_1 = Input_RPS.X127()
        return x127_1

@register(Dashboard_M16_EEPS)
class Y9():
    # 'Dashboard_M16_EEPS'!Y9
    value = 0
    formula = "='Input RPS'!Y127"
    @eval_fn
    def Y9():
        y127_1 = Input_RPS.Y127()
        return y127_1

@register(Dashboard_M16_EEPS)
class Z9():
    # 'Dashboard_M16_EEPS'!Z9
    value = 0
    formula = "='Input RPS'!Z127"
    @eval_fn
    def Z9():
        z127_1 = Input_RPS.Z127()
        return z127_1

@register(Dashboard_M16_EEPS)
class AA9():
    # 'Dashboard_M16_EEPS'!AA9
    value = 0
    formula = "='Input RPS'!AA127"
    @eval_fn
    def AA9():
        aa127_1 = Input_RPS.AA127()
        return aa127_1

@register(Dashboard_M16_EEPS)
class AB9():
    # 'Dashboard_M16_EEPS'!AB9
    value = 0
    formula = "='Input RPS'!AB127"
    @eval_fn
    def AB9():
        ab127_1 = Input_RPS.AB127()
        return ab127_1

@register(Dashboard_M16_EEPS)
class AC9():
    # 'Dashboard_M16_EEPS'!AC9
    value = 0
    formula = "='Input RPS'!AC127"
    @eval_fn
    def AC9():
        ac127_1 = Input_RPS.AC127()
        return ac127_1

@register(Dashboard_M16_EEPS)
class AD9():
    # 'Dashboard_M16_EEPS'!AD9
    value = 0
    formula = "='Input RPS'!AD127"
    @eval_fn
    def AD9():
        ad127_1 = Input_RPS.AD127()
        return ad127_1

@register(Dashboard_M16_EEPS)
class AE9():
    # 'Dashboard_M16_EEPS'!AE9
    value = 0
    formula = "='Input RPS'!AE127"
    @eval_fn
    def AE9():
        ae127_1 = Input_RPS.AE127()
        return ae127_1

@register(Dashboard_M16_EEPS)
class AF9():
    # 'Dashboard_M16_EEPS'!AF9
    value = 0
    formula = "='Input RPS'!AF127"
    @eval_fn
    def AF9():
        af127_1 = Input_RPS.AF127()
        return af127_1

@register(Dashboard_M16_EEPS)
class AG9():
    # 'Dashboard_M16_EEPS'!AG9
    value = 0
    formula = "='Input RPS'!AG127"
    @eval_fn
    def AG9():
        ag127_1 = Input_RPS.AG127()
        return ag127_1

@register(Dashboard_M16_EEPS)
class AH9():
    # 'Dashboard_M16_EEPS'!AH9
    value = 0
    formula = "='Input RPS'!AH127"
    @eval_fn
    def AH9():
        ah127_1 = Input_RPS.AH127()
        return ah127_1

@register(Dashboard_M16_EEPS)
class AI9():
    # 'Dashboard_M16_EEPS'!AI9
    value = 0
    formula = "='Input RPS'!AI127"
    @eval_fn
    def AI9():
        ai127_1 = Input_RPS.AI127()
        return ai127_1

@register(Dashboard_M16_EEPS)
class AJ9():
    # 'Dashboard_M16_EEPS'!AJ9
    value = 0
    formula = "='Input RPS'!AJ127"
    @eval_fn
    def AJ9():
        aj127_1 = Input_RPS.AJ127()
        return aj127_1

@register(Dashboard_M16_EEPS)
class AK9():
    # 'Dashboard_M16_EEPS'!AK9
    value = 0
    formula = "='Input RPS'!AK127"
    @eval_fn
    def AK9():
        ak127_1 = Input_RPS.AK127()
        return ak127_1

@register(Dashboard_M16_EEPS)
class AL9():
    # 'Dashboard_M16_EEPS'!AL9
    value = 0
    formula = "='Input RPS'!AL127"
    @eval_fn
    def AL9():
        al127_1 = Input_RPS.AL127()
        return al127_1

@register(Dashboard_M16_EEPS)
class A10():
    # 'Dashboard_M16_EEPS'!A10
    value = "KIUCTotal Renewable"
    formula = "=CONCATENATE(C10,B10)"
    @eval_fn
    def A10():
        c10_1 = Dashboard_M16_EEPS.C10()
        b10_1 = Dashboard_M16_EEPS.B10()
        var_1 = CONCATENATE(c10_1, b10_1)
        return var_1

@register(Dashboard_M16_EEPS)
class B10():
    # 'Dashboard_M16_EEPS'!B10
    value = "Total Renewable"

@register(Dashboard_M16_EEPS)
class C10():
    # 'Dashboard_M16_EEPS'!C10
    value = "KIUC"

@register(Dashboard_M16_EEPS)
class D10():
    # 'Dashboard_M16_EEPS'!D10
    value = "MWh"

@register(Dashboard_M16_EEPS)
class E10():
    # 'Dashboard_M16_EEPS'!E10
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://dms.puc.hawaii.gov/dms/OpenDocServlet?RT=&document_id=91+3+ICM4+LSDB15+PC_DocketReport59+26+A1001001A12D04B24000E5143818+A12D04B24000E514381+14+1960'''

@register(Dashboard_M16_EEPS)
class G10():
    # 'Dashboard_M16_EEPS'!G10
    value = 423389
    formula = "='Input RPS'!G128"
    @eval_fn
    def G10():
        g128_1 = Input_RPS.G128()
        return g128_1

@register(Dashboard_M16_EEPS)
class H10():
    # 'Dashboard_M16_EEPS'!H10
    value = 452699
    formula = "='Input RPS'!H128"
    @eval_fn
    def H10():
        h128_1 = Input_RPS.H128()
        return h128_1

@register(Dashboard_M16_EEPS)
class I10():
    # 'Dashboard_M16_EEPS'!I10
    value = 443798
    formula = "='Input RPS'!I128"
    @eval_fn
    def I10():
        i128_1 = Input_RPS.I128()
        return i128_1

@register(Dashboard_M16_EEPS)
class J10():
    # 'Dashboard_M16_EEPS'!J10
    value = 452631
    formula = "='Input RPS'!J128"
    @eval_fn
    def J10():
        j128_1 = Input_RPS.J128()
        return j128_1

@register(Dashboard_M16_EEPS)
class K10():
    # 'Dashboard_M16_EEPS'!K10
    value = 438768
    formula = "='Input RPS'!K128"
    @eval_fn
    def K10():
        k128_1 = Input_RPS.K128()
        return k128_1

@register(Dashboard_M16_EEPS)
class L10():
    # 'Dashboard_M16_EEPS'!L10
    value = 473608
    formula = "='Input RPS'!L128"
    @eval_fn
    def L10():
        l128_1 = Input_RPS.L128()
        return l128_1

@register(Dashboard_M16_EEPS)
class M10():
    # 'Dashboard_M16_EEPS'!M10
    value = 477255
    formula = "='Input RPS'!M128"
    @eval_fn
    def M10():
        m128_1 = Input_RPS.M128()
        return m128_1

@register(Dashboard_M16_EEPS)
class N10():
    # 'Dashboard_M16_EEPS'!N10
    value = 481461
    formula = "='Input RPS'!N128"
    @eval_fn
    def N10():
        n128_1 = Input_RPS.N128()
        return n128_1

@register(Dashboard_M16_EEPS)
class O10():
    # 'Dashboard_M16_EEPS'!O10
    value = 496718
    formula = "='Input RPS'!O128"
    @eval_fn
    def O10():
        o128_1 = Input_RPS.O128()
        return o128_1

@register(Dashboard_M16_EEPS)
class P10():
    # 'Dashboard_M16_EEPS'!P10
    value = 476948
    formula = "='Input RPS'!P128"
    @eval_fn
    def P10():
        p128_1 = Input_RPS.P128()
        return p128_1

@register(Dashboard_M16_EEPS)
class Q10():
    # 'Dashboard_M16_EEPS'!Q10
    value = 460513
    formula = "='Input RPS'!Q128"
    @eval_fn
    def Q10():
        q128_1 = Input_RPS.Q128()
        return q128_1

@register(Dashboard_M16_EEPS)
class R10():
    # 'Dashboard_M16_EEPS'!R10
    value = 457274
    formula = "='Input RPS'!R128"
    @eval_fn
    def R10():
        r128_1 = Input_RPS.R128()
        return r128_1

@register(Dashboard_M16_EEPS)
class S10():
    # 'Dashboard_M16_EEPS'!S10
    value = 460971
    formula = "='Input RPS'!S128"
    @eval_fn
    def S10():
        s128_1 = Input_RPS.S128()
        return s128_1

@register(Dashboard_M16_EEPS)
class T10():
    # 'Dashboard_M16_EEPS'!T10
    value = 433159
    formula = "='Input RPS'!T128"
    @eval_fn
    def T10():
        t128_1 = Input_RPS.T128()
        return t128_1

@register(Dashboard_M16_EEPS)
class U10():
    # 'Dashboard_M16_EEPS'!U10
    value = 431478
    formula = "='Input RPS'!U128"
    @eval_fn
    def U10():
        u128_1 = Input_RPS.U128()
        return u128_1

@register(Dashboard_M16_EEPS)
class V10():
    # 'Dashboard_M16_EEPS'!V10
    value = 429924
    formula = "='Input RPS'!V128"
    @eval_fn
    def V10():
        v128_1 = Input_RPS.V128()
        return v128_1

@register(Dashboard_M16_EEPS)
class W10():
    # 'Dashboard_M16_EEPS'!W10
    value = 432078
    formula = "='Input RPS'!W128"
    @eval_fn
    def W10():
        w128_1 = Input_RPS.W128()
        return w128_1

@register(Dashboard_M16_EEPS)
class X10():
    # 'Dashboard_M16_EEPS'!X10
    value = 0
    formula = "='Input RPS'!X128"
    @eval_fn
    def X10():
        x128_1 = Input_RPS.X128()
        return x128_1

@register(Dashboard_M16_EEPS)
class Y10():
    # 'Dashboard_M16_EEPS'!Y10
    value = 0
    formula = "='Input RPS'!Y128"
    @eval_fn
    def Y10():
        y128_1 = Input_RPS.Y128()
        return y128_1

@register(Dashboard_M16_EEPS)
class Z10():
    # 'Dashboard_M16_EEPS'!Z10
    value = 0
    formula = "='Input RPS'!Z128"
    @eval_fn
    def Z10():
        z128_1 = Input_RPS.Z128()
        return z128_1

@register(Dashboard_M16_EEPS)
class AA10():
    # 'Dashboard_M16_EEPS'!AA10
    value = 0
    formula = "='Input RPS'!AA128"
    @eval_fn
    def AA10():
        aa128_1 = Input_RPS.AA128()
        return aa128_1

@register(Dashboard_M16_EEPS)
class AB10():
    # 'Dashboard_M16_EEPS'!AB10
    value = 0
    formula = "='Input RPS'!AB128"
    @eval_fn
    def AB10():
        ab128_1 = Input_RPS.AB128()
        return ab128_1

@register(Dashboard_M16_EEPS)
class AC10():
    # 'Dashboard_M16_EEPS'!AC10
    value = 0
    formula = "='Input RPS'!AC128"
    @eval_fn
    def AC10():
        ac128_1 = Input_RPS.AC128()
        return ac128_1

@register(Dashboard_M16_EEPS)
class AD10():
    # 'Dashboard_M16_EEPS'!AD10
    value = 0
    formula = "='Input RPS'!AD128"
    @eval_fn
    def AD10():
        ad128_1 = Input_RPS.AD128()
        return ad128_1

@register(Dashboard_M16_EEPS)
class AE10():
    # 'Dashboard_M16_EEPS'!AE10
    value = 0
    formula = "='Input RPS'!AE128"
    @eval_fn
    def AE10():
        ae128_1 = Input_RPS.AE128()
        return ae128_1

@register(Dashboard_M16_EEPS)
class AF10():
    # 'Dashboard_M16_EEPS'!AF10
    value = 0
    formula = "='Input RPS'!AF128"
    @eval_fn
    def AF10():
        af128_1 = Input_RPS.AF128()
        return af128_1

@register(Dashboard_M16_EEPS)
class AG10():
    # 'Dashboard_M16_EEPS'!AG10
    value = 0
    formula = "='Input RPS'!AG128"
    @eval_fn
    def AG10():
        ag128_1 = Input_RPS.AG128()
        return ag128_1

@register(Dashboard_M16_EEPS)
class AH10():
    # 'Dashboard_M16_EEPS'!AH10
    value = 0
    formula = "='Input RPS'!AH128"
    @eval_fn
    def AH10():
        ah128_1 = Input_RPS.AH128()
        return ah128_1

@register(Dashboard_M16_EEPS)
class AI10():
    # 'Dashboard_M16_EEPS'!AI10
    value = 0
    formula = "='Input RPS'!AI128"
    @eval_fn
    def AI10():
        ai128_1 = Input_RPS.AI128()
        return ai128_1

@register(Dashboard_M16_EEPS)
class AJ10():
    # 'Dashboard_M16_EEPS'!AJ10
    value = 0
    formula = "='Input RPS'!AJ128"
    @eval_fn
    def AJ10():
        aj128_1 = Input_RPS.AJ128()
        return aj128_1

@register(Dashboard_M16_EEPS)
class AK10():
    # 'Dashboard_M16_EEPS'!AK10
    value = 0
    formula = "='Input RPS'!AK128"
    @eval_fn
    def AK10():
        ak128_1 = Input_RPS.AK128()
        return ak128_1

@register(Dashboard_M16_EEPS)
class AL10():
    # 'Dashboard_M16_EEPS'!AL10
    value = 0
    formula = "='Input RPS'!AL128"
    @eval_fn
    def AL10():
        al128_1 = Input_RPS.AL128()
        return al128_1

@register(Dashboard_M16_EEPS)
class A11():
    # 'Dashboard_M16_EEPS'!A11
    value = "TotalTotal Renewable"
    formula = "=CONCATENATE(C11,B11)"
    @eval_fn
    def A11():
        c11_1 = Dashboard_M16_EEPS.C11()
        b11_1 = Dashboard_M16_EEPS.B11()
        var_1 = CONCATENATE(c11_1, b11_1)
        return var_1

@register(Dashboard_M16_EEPS)
class B11():
    # 'Dashboard_M16_EEPS'!B11
    value = "Total Renewable"

@register(Dashboard_M16_EEPS)
class C11():
    # 'Dashboard_M16_EEPS'!C11
    value = "Total"

@register(Dashboard_M16_EEPS)
class D11():
    # 'Dashboard_M16_EEPS'!D11
    value = "MWh"

@register(Dashboard_M16_EEPS)
class G11():
    # 'Dashboard_M16_EEPS'!G11
    value = 11408389
    formula = "='Input RPS'!G129"
    @eval_fn
    def G11():
        g129_1 = Input_RPS.G129()
        return g129_1

@register(Dashboard_M16_EEPS)
class H11():
    # 'Dashboard_M16_EEPS'!H11
    value = 9724699
    formula = "='Input RPS'!H129"
    @eval_fn
    def H11():
        h129_1 = Input_RPS.H129()
        return h129_1

@register(Dashboard_M16_EEPS)
class I11():
    # 'Dashboard_M16_EEPS'!I11
    value = 9813798
    formula = "='Input RPS'!I129"
    @eval_fn
    def I11():
        i129_1 = Input_RPS.I129()
        return i129_1

@register(Dashboard_M16_EEPS)
class J11():
    # 'Dashboard_M16_EEPS'!J11
    value = 9996631
    formula = "='Input RPS'!J129"
    @eval_fn
    def J11():
        j129_1 = Input_RPS.J129()
        return j129_1

@register(Dashboard_M16_EEPS)
class K11():
    # 'Dashboard_M16_EEPS'!K11
    value = 10213768
    formula = "='Input RPS'!K129"
    @eval_fn
    def K11():
        k129_1 = Input_RPS.K129()
        return k129_1

@register(Dashboard_M16_EEPS)
class L11():
    # 'Dashboard_M16_EEPS'!L11
    value = 10536608
    formula = "='Input RPS'!L129"
    @eval_fn
    def L11():
        l129_1 = Input_RPS.L129()
        return l129_1

@register(Dashboard_M16_EEPS)
class M11():
    # 'Dashboard_M16_EEPS'!M11
    value = 10567255
    formula = "='Input RPS'!M129"
    @eval_fn
    def M11():
        m129_1 = Input_RPS.M129()
        return m129_1

@register(Dashboard_M16_EEPS)
class N11():
    # 'Dashboard_M16_EEPS'!N11
    value = 10597461
    formula = "='Input RPS'!N129"
    @eval_fn
    def N11():
        n129_1 = Input_RPS.N129()
        return n129_1

@register(Dashboard_M16_EEPS)
class O11():
    # 'Dashboard_M16_EEPS'!O11
    value = 10614718
    formula = "='Input RPS'!O129"
    @eval_fn
    def O11():
        o129_1 = Input_RPS.O129()
        return o129_1

@register(Dashboard_M16_EEPS)
class P11():
    # 'Dashboard_M16_EEPS'!P11
    value = 10413168
    formula = "='Input RPS'!P129"
    @eval_fn
    def P11():
        p129_1 = Input_RPS.P129()
        return p129_1

@register(Dashboard_M16_EEPS)
class Q11():
    # 'Dashboard_M16_EEPS'!Q11
    value = 10150174
    formula = "='Input RPS'!Q129"
    @eval_fn
    def Q11():
        q129_1 = Input_RPS.Q129()
        return q129_1

@register(Dashboard_M16_EEPS)
class R11():
    # 'Dashboard_M16_EEPS'!R11
    value = 10035845
    formula = "='Input RPS'!R129"
    @eval_fn
    def R11():
        r129_1 = Input_RPS.R129()
        return r129_1

@register(Dashboard_M16_EEPS)
class S11():
    # 'Dashboard_M16_EEPS'!S11
    value = 9987880
    formula = "='Input RPS'!S129"
    @eval_fn
    def S11():
        s129_1 = Input_RPS.S129()
        return s129_1

@register(Dashboard_M16_EEPS)
class T11():
    # 'Dashboard_M16_EEPS'!T11
    value = 9639158
    formula = "='Input RPS'!T129"
    @eval_fn
    def T11():
        t129_1 = Input_RPS.T129()
        return t129_1

@register(Dashboard_M16_EEPS)
class U11():
    # 'Dashboard_M16_EEPS'!U11
    value = 9500991
    formula = "='Input RPS'!U129"
    @eval_fn
    def U11():
        u129_1 = Input_RPS.U129()
        return u129_1

@register(Dashboard_M16_EEPS)
class V11():
    # 'Dashboard_M16_EEPS'!V11
    value = 9406166
    formula = "='Input RPS'!V129"
    @eval_fn
    def V11():
        v129_1 = Input_RPS.V129()
        return v129_1

@register(Dashboard_M16_EEPS)
class W11():
    # 'Dashboard_M16_EEPS'!W11
    value = 9388576
    formula = "='Input RPS'!W129"
    @eval_fn
    def W11():
        w129_1 = Input_RPS.W129()
        return w129_1

@register(Dashboard_M16_EEPS)
class X11():
    # 'Dashboard_M16_EEPS'!X11
    value = 0
    formula = "='Input RPS'!X129"
    @eval_fn
    def X11():
        x129_1 = Input_RPS.X129()
        return x129_1

@register(Dashboard_M16_EEPS)
class Y11():
    # 'Dashboard_M16_EEPS'!Y11
    value = 0
    formula = "='Input RPS'!Y129"
    @eval_fn
    def Y11():
        y129_1 = Input_RPS.Y129()
        return y129_1

@register(Dashboard_M16_EEPS)
class Z11():
    # 'Dashboard_M16_EEPS'!Z11
    value = 0
    formula = "='Input RPS'!Z129"
    @eval_fn
    def Z11():
        z129_1 = Input_RPS.Z129()
        return z129_1

@register(Dashboard_M16_EEPS)
class AA11():
    # 'Dashboard_M16_EEPS'!AA11
    value = 0
    formula = "='Input RPS'!AA129"
    @eval_fn
    def AA11():
        aa129_1 = Input_RPS.AA129()
        return aa129_1

@register(Dashboard_M16_EEPS)
class AB11():
    # 'Dashboard_M16_EEPS'!AB11
    value = 0
    formula = "='Input RPS'!AB129"
    @eval_fn
    def AB11():
        ab129_1 = Input_RPS.AB129()
        return ab129_1

@register(Dashboard_M16_EEPS)
class AC11():
    # 'Dashboard_M16_EEPS'!AC11
    value = 0
    formula = "='Input RPS'!AC129"
    @eval_fn
    def AC11():
        ac129_1 = Input_RPS.AC129()
        return ac129_1

@register(Dashboard_M16_EEPS)
class AD11():
    # 'Dashboard_M16_EEPS'!AD11
    value = 0
    formula = "='Input RPS'!AD129"
    @eval_fn
    def AD11():
        ad129_1 = Input_RPS.AD129()
        return ad129_1

@register(Dashboard_M16_EEPS)
class AE11():
    # 'Dashboard_M16_EEPS'!AE11
    value = 0
    formula = "='Input RPS'!AE129"
    @eval_fn
    def AE11():
        ae129_1 = Input_RPS.AE129()
        return ae129_1

@register(Dashboard_M16_EEPS)
class AF11():
    # 'Dashboard_M16_EEPS'!AF11
    value = 0
    formula = "='Input RPS'!AF129"
    @eval_fn
    def AF11():
        af129_1 = Input_RPS.AF129()
        return af129_1

@register(Dashboard_M16_EEPS)
class AG11():
    # 'Dashboard_M16_EEPS'!AG11
    value = 0
    formula = "='Input RPS'!AG129"
    @eval_fn
    def AG11():
        ag129_1 = Input_RPS.AG129()
        return ag129_1

@register(Dashboard_M16_EEPS)
class AH11():
    # 'Dashboard_M16_EEPS'!AH11
    value = 0
    formula = "='Input RPS'!AH129"
    @eval_fn
    def AH11():
        ah129_1 = Input_RPS.AH129()
        return ah129_1

@register(Dashboard_M16_EEPS)
class AI11():
    # 'Dashboard_M16_EEPS'!AI11
    value = 0
    formula = "='Input RPS'!AI129"
    @eval_fn
    def AI11():
        ai129_1 = Input_RPS.AI129()
        return ai129_1

@register(Dashboard_M16_EEPS)
class AJ11():
    # 'Dashboard_M16_EEPS'!AJ11
    value = 0
    formula = "='Input RPS'!AJ129"
    @eval_fn
    def AJ11():
        aj129_1 = Input_RPS.AJ129()
        return aj129_1

@register(Dashboard_M16_EEPS)
class AK11():
    # 'Dashboard_M16_EEPS'!AK11
    value = 0
    formula = "='Input RPS'!AK129"
    @eval_fn
    def AK11():
        ak129_1 = Input_RPS.AK129()
        return ak129_1

@register(Dashboard_M16_EEPS)
class AL11():
    # 'Dashboard_M16_EEPS'!AL11
    value = 0
    formula = "='Input RPS'!AL129"
    @eval_fn
    def AL11():
        al129_1 = Input_RPS.AL129()
        return al129_1

@register(Dashboard_M16_EEPS)
class A13():
    # 'Dashboard_M16_EEPS'!A13
    value = "REu,s,y Aggregate renewable electricity sold from source s by utility u in year y "

@register(Dashboard_M16_EEPS)
class A14():
    # 'Dashboard_M16_EEPS'!A14
    value = "ES"

@register(Dashboard_M16_EEPS)
class C15():
    # 'Dashboard_M16_EEPS'!C15
    value = "HECO"

@register(Dashboard_M16_EEPS)
class D15():
    # 'Dashboard_M16_EEPS'!D15
    value = "MWh"

@register(Dashboard_M16_EEPS)
class C16():
    # 'Dashboard_M16_EEPS'!C16
    value = "  Displacement Tech: Solar Water Heating"

@register(Dashboard_M16_EEPS)
class G16():
    # 'Dashboard_M16_EEPS'!G16
    value = 0
    formula = "='Input RPS'!G101"
    @eval_fn
    def G16():
        g101_1 = Input_RPS.G101()
        return g101_1

@register(Dashboard_M16_EEPS)
class H16():
    # 'Dashboard_M16_EEPS'!H16
    value = 0
    formula = "='Input RPS'!H101"
    @eval_fn
    def H16():
        h101_1 = Input_RPS.H101()
        return h101_1

@register(Dashboard_M16_EEPS)
class I16():
    # 'Dashboard_M16_EEPS'!I16
    value = 0
    formula = "='Input RPS'!I101"
    @eval_fn
    def I16():
        i101_1 = Input_RPS.I101()
        return i101_1

@register(Dashboard_M16_EEPS)
class J16():
    # 'Dashboard_M16_EEPS'!J16
    value = 0
    formula = "='Input RPS'!J101"
    @eval_fn
    def J16():
        j101_1 = Input_RPS.J101()
        return j101_1

@register(Dashboard_M16_EEPS)
class K16():
    # 'Dashboard_M16_EEPS'!K16
    value = 0
    formula = "='Input RPS'!K101"
    @eval_fn
    def K16():
        k101_1 = Input_RPS.K101()
        return k101_1

@register(Dashboard_M16_EEPS)
class L16():
    # 'Dashboard_M16_EEPS'!L16
    value = 0
    formula = "='Input RPS'!L101"
    @eval_fn
    def L16():
        l101_1 = Input_RPS.L101()
        return l101_1

@register(Dashboard_M16_EEPS)
class M16():
    # 'Dashboard_M16_EEPS'!M16
    value = 51000
    formula = "='Input RPS'!M101"
    @eval_fn
    def M16():
        m101_1 = Input_RPS.M101()
        return m101_1

@register(Dashboard_M16_EEPS)
class N16():
    # 'Dashboard_M16_EEPS'!N16
    value = 58000
    formula = "='Input RPS'!N101"
    @eval_fn
    def N16():
        n101_1 = Input_RPS.N101()
        return n101_1

@register(Dashboard_M16_EEPS)
class O16():
    # 'Dashboard_M16_EEPS'!O16
    value = 66000
    formula = "='Input RPS'!O101"
    @eval_fn
    def O16():
        o101_1 = Input_RPS.O101()
        return o101_1

@register(Dashboard_M16_EEPS)
class P16():
    # 'Dashboard_M16_EEPS'!P16
    value = 75988
    formula = "='Input RPS'!P101"
    @eval_fn
    def P16():
        p101_1 = Input_RPS.P101()
        return p101_1

@register(Dashboard_M16_EEPS)
class Q16():
    # 'Dashboard_M16_EEPS'!Q16
    value = 86967
    formula = "='Input RPS'!Q101"
    @eval_fn
    def Q16():
        q101_1 = Input_RPS.Q101()
        return q101_1

@register(Dashboard_M16_EEPS)
class R16():
    # 'Dashboard_M16_EEPS'!R16
    value = 122801
    formula = "='Input RPS'!R101"
    @eval_fn
    def R16():
        r101_1 = Input_RPS.R101()
        return r101_1

@register(Dashboard_M16_EEPS)
class S16():
    # 'Dashboard_M16_EEPS'!S16
    value = 129314
    formula = "='Input RPS'!S101"
    @eval_fn
    def S16():
        s101_1 = Input_RPS.S101()
        return s101_1

@register(Dashboard_M16_EEPS)
class T16():
    # 'Dashboard_M16_EEPS'!T16
    value = 113541
    formula = "='Input RPS'!T101"
    @eval_fn
    def T16():
        t101_1 = Input_RPS.T101()
        return t101_1

@register(Dashboard_M16_EEPS)
class U16():
    # 'Dashboard_M16_EEPS'!U16
    value = 100997
    formula = "='Input RPS'!U101"
    @eval_fn
    def U16():
        u101_1 = Input_RPS.U101()
        return u101_1

@register(Dashboard_M16_EEPS)
class V16():
    # 'Dashboard_M16_EEPS'!V16
    value = 86719
    formula = "='Input RPS'!V101"
    @eval_fn
    def V16():
        v101_1 = Input_RPS.V101()
        return v101_1

@register(Dashboard_M16_EEPS)
class W16():
    # 'Dashboard_M16_EEPS'!W16
    value = 72441
    formula = "='Input RPS'!W101"
    @eval_fn
    def W16():
        w101_1 = Input_RPS.W101()
        return w101_1

@register(Dashboard_M16_EEPS)
class X16():
    # 'Dashboard_M16_EEPS'!X16
    value = 0
    formula = "='Input RPS'!X101"
    @eval_fn
    def X16():
        x101_1 = Input_RPS.X101()
        return x101_1

@register(Dashboard_M16_EEPS)
class Y16():
    # 'Dashboard_M16_EEPS'!Y16
    value = 0
    formula = "='Input RPS'!Y101"
    @eval_fn
    def Y16():
        y101_1 = Input_RPS.Y101()
        return y101_1

@register(Dashboard_M16_EEPS)
class Z16():
    # 'Dashboard_M16_EEPS'!Z16
    value = 0
    formula = "='Input RPS'!Z101"
    @eval_fn
    def Z16():
        z101_1 = Input_RPS.Z101()
        return z101_1

@register(Dashboard_M16_EEPS)
class AA16():
    # 'Dashboard_M16_EEPS'!AA16
    value = 0
    formula = "='Input RPS'!AA101"
    @eval_fn
    def AA16():
        aa101_1 = Input_RPS.AA101()
        return aa101_1

@register(Dashboard_M16_EEPS)
class AB16():
    # 'Dashboard_M16_EEPS'!AB16
    value = 0
    formula = "='Input RPS'!AB101"
    @eval_fn
    def AB16():
        ab101_1 = Input_RPS.AB101()
        return ab101_1

@register(Dashboard_M16_EEPS)
class AC16():
    # 'Dashboard_M16_EEPS'!AC16
    value = 0
    formula = "='Input RPS'!AC101"
    @eval_fn
    def AC16():
        ac101_1 = Input_RPS.AC101()
        return ac101_1

@register(Dashboard_M16_EEPS)
class AD16():
    # 'Dashboard_M16_EEPS'!AD16
    value = 0
    formula = "='Input RPS'!AD101"
    @eval_fn
    def AD16():
        ad101_1 = Input_RPS.AD101()
        return ad101_1

@register(Dashboard_M16_EEPS)
class AE16():
    # 'Dashboard_M16_EEPS'!AE16
    value = 0
    formula = "='Input RPS'!AE101"
    @eval_fn
    def AE16():
        ae101_1 = Input_RPS.AE101()
        return ae101_1

@register(Dashboard_M16_EEPS)
class AF16():
    # 'Dashboard_M16_EEPS'!AF16
    value = 0
    formula = "='Input RPS'!AF101"
    @eval_fn
    def AF16():
        af101_1 = Input_RPS.AF101()
        return af101_1

@register(Dashboard_M16_EEPS)
class AG16():
    # 'Dashboard_M16_EEPS'!AG16
    value = 0
    formula = "='Input RPS'!AG101"
    @eval_fn
    def AG16():
        ag101_1 = Input_RPS.AG101()
        return ag101_1

@register(Dashboard_M16_EEPS)
class AH16():
    # 'Dashboard_M16_EEPS'!AH16
    value = 0
    formula = "='Input RPS'!AH101"
    @eval_fn
    def AH16():
        ah101_1 = Input_RPS.AH101()
        return ah101_1

@register(Dashboard_M16_EEPS)
class AI16():
    # 'Dashboard_M16_EEPS'!AI16
    value = 0
    formula = "='Input RPS'!AI101"
    @eval_fn
    def AI16():
        ai101_1 = Input_RPS.AI101()
        return ai101_1

@register(Dashboard_M16_EEPS)
class AJ16():
    # 'Dashboard_M16_EEPS'!AJ16
    value = 0
    formula = "='Input RPS'!AJ101"
    @eval_fn
    def AJ16():
        aj101_1 = Input_RPS.AJ101()
        return aj101_1

@register(Dashboard_M16_EEPS)
class AK16():
    # 'Dashboard_M16_EEPS'!AK16
    value = 0
    formula = "='Input RPS'!AK101"
    @eval_fn
    def AK16():
        ak101_1 = Input_RPS.AK101()
        return ak101_1

@register(Dashboard_M16_EEPS)
class AL16():
    # 'Dashboard_M16_EEPS'!AL16
    value = 0
    formula = "='Input RPS'!AL101"
    @eval_fn
    def AL16():
        al101_1 = Input_RPS.AL101()
        return al101_1

@register(Dashboard_M16_EEPS)
class C17():
    # 'Dashboard_M16_EEPS'!C17
    value = "  Energy Efficiency Technologies"

@register(Dashboard_M16_EEPS)
class G17():
    # 'Dashboard_M16_EEPS'!G17
    value = 0
    formula = "='Input RPS'!G103"
    @eval_fn
    def G17():
        g103_1 = Input_RPS.G103()
        return g103_1

@register(Dashboard_M16_EEPS)
class H17():
    # 'Dashboard_M16_EEPS'!H17
    value = 0
    formula = "='Input RPS'!H103"
    @eval_fn
    def H17():
        h103_1 = Input_RPS.H103()
        return h103_1

@register(Dashboard_M16_EEPS)
class I17():
    # 'Dashboard_M16_EEPS'!I17
    value = 0
    formula = "='Input RPS'!I103"
    @eval_fn
    def I17():
        i103_1 = Input_RPS.I103()
        return i103_1

@register(Dashboard_M16_EEPS)
class J17():
    # 'Dashboard_M16_EEPS'!J17
    value = 0
    formula = "='Input RPS'!J103"
    @eval_fn
    def J17():
        j103_1 = Input_RPS.J103()
        return j103_1

@register(Dashboard_M16_EEPS)
class K17():
    # 'Dashboard_M16_EEPS'!K17
    value = 0
    formula = "='Input RPS'!K103"
    @eval_fn
    def K17():
        k103_1 = Input_RPS.K103()
        return k103_1

@register(Dashboard_M16_EEPS)
class L17():
    # 'Dashboard_M16_EEPS'!L17
    value = 0
    formula = "='Input RPS'!L103"
    @eval_fn
    def L17():
        l103_1 = Input_RPS.L103()
        return l103_1

@register(Dashboard_M16_EEPS)
class M17():
    # 'Dashboard_M16_EEPS'!M17
    value = 292000
    formula = "='Input RPS'!M103"
    @eval_fn
    def M17():
        m103_1 = Input_RPS.M103()
        return m103_1

@register(Dashboard_M16_EEPS)
class N17():
    # 'Dashboard_M16_EEPS'!N17
    value = 340000
    formula = "='Input RPS'!N103"
    @eval_fn
    def N17():
        n103_1 = Input_RPS.N103()
        return n103_1

@register(Dashboard_M16_EEPS)
class O17():
    # 'Dashboard_M16_EEPS'!O17
    value = 453000
    formula = "='Input RPS'!O103"
    @eval_fn
    def O17():
        o103_1 = Input_RPS.O103()
        return o103_1

@register(Dashboard_M16_EEPS)
class P17():
    # 'Dashboard_M16_EEPS'!P17
    value = 604007
    formula = "='Input RPS'!P103"
    @eval_fn
    def P17():
        p103_1 = Input_RPS.P103()
        return p103_1

@register(Dashboard_M16_EEPS)
class Q17():
    # 'Dashboard_M16_EEPS'!Q17
    value = 651278
    formula = "='Input RPS'!Q103"
    @eval_fn
    def Q17():
        q103_1 = Input_RPS.Q103()
        return q103_1

@register(Dashboard_M16_EEPS)
class R17():
    # 'Dashboard_M16_EEPS'!R17
    value = 738337
    formula = "='Input RPS'!R103"
    @eval_fn
    def R17():
        r103_1 = Input_RPS.R103()
        return r103_1

@register(Dashboard_M16_EEPS)
class S17():
    # 'Dashboard_M16_EEPS'!S17
    value = 821136
    formula = "='Input RPS'!S103"
    @eval_fn
    def S17():
        s103_1 = Input_RPS.S103()
        return s103_1

@register(Dashboard_M16_EEPS)
class T17():
    # 'Dashboard_M16_EEPS'!T17
    value = 958155
    formula = "='Input RPS'!T103"
    @eval_fn
    def T17():
        t103_1 = Input_RPS.T103()
        return t103_1

@register(Dashboard_M16_EEPS)
class U17():
    # 'Dashboard_M16_EEPS'!U17
    value = 1039167
    formula = "='Input RPS'!U103"
    @eval_fn
    def U17():
        u103_1 = Input_RPS.U103()
        return u103_1

@register(Dashboard_M16_EEPS)
class V17():
    # 'Dashboard_M16_EEPS'!V17
    value = 1117117
    formula = "='Input RPS'!V103"
    @eval_fn
    def V17():
        v103_1 = Input_RPS.V103()
        return v103_1

@register(Dashboard_M16_EEPS)
class W17():
    # 'Dashboard_M16_EEPS'!W17
    value = 1195067
    formula = "='Input RPS'!W103"
    @eval_fn
    def W17():
        w103_1 = Input_RPS.W103()
        return w103_1

@register(Dashboard_M16_EEPS)
class X17():
    # 'Dashboard_M16_EEPS'!X17
    value = 0
    formula = "='Input RPS'!X103"
    @eval_fn
    def X17():
        x103_1 = Input_RPS.X103()
        return x103_1

@register(Dashboard_M16_EEPS)
class Y17():
    # 'Dashboard_M16_EEPS'!Y17
    value = 0
    formula = "='Input RPS'!Y103"
    @eval_fn
    def Y17():
        y103_1 = Input_RPS.Y103()
        return y103_1

@register(Dashboard_M16_EEPS)
class Z17():
    # 'Dashboard_M16_EEPS'!Z17
    value = 0
    formula = "='Input RPS'!Z103"
    @eval_fn
    def Z17():
        z103_1 = Input_RPS.Z103()
        return z103_1

@register(Dashboard_M16_EEPS)
class AA17():
    # 'Dashboard_M16_EEPS'!AA17
    value = 0
    formula = "='Input RPS'!AA103"
    @eval_fn
    def AA17():
        aa103_1 = Input_RPS.AA103()
        return aa103_1

@register(Dashboard_M16_EEPS)
class AB17():
    # 'Dashboard_M16_EEPS'!AB17
    value = 0
    formula = "='Input RPS'!AB103"
    @eval_fn
    def AB17():
        ab103_1 = Input_RPS.AB103()
        return ab103_1

@register(Dashboard_M16_EEPS)
class AC17():
    # 'Dashboard_M16_EEPS'!AC17
    value = 0
    formula = "='Input RPS'!AC103"
    @eval_fn
    def AC17():
        ac103_1 = Input_RPS.AC103()
        return ac103_1

@register(Dashboard_M16_EEPS)
class AD17():
    # 'Dashboard_M16_EEPS'!AD17
    value = 0
    formula = "='Input RPS'!AD103"
    @eval_fn
    def AD17():
        ad103_1 = Input_RPS.AD103()
        return ad103_1

@register(Dashboard_M16_EEPS)
class AE17():
    # 'Dashboard_M16_EEPS'!AE17
    value = 0
    formula = "='Input RPS'!AE103"
    @eval_fn
    def AE17():
        ae103_1 = Input_RPS.AE103()
        return ae103_1

@register(Dashboard_M16_EEPS)
class AF17():
    # 'Dashboard_M16_EEPS'!AF17
    value = 0
    formula = "='Input RPS'!AF103"
    @eval_fn
    def AF17():
        af103_1 = Input_RPS.AF103()
        return af103_1

@register(Dashboard_M16_EEPS)
class AG17():
    # 'Dashboard_M16_EEPS'!AG17
    value = 0
    formula = "='Input RPS'!AG103"
    @eval_fn
    def AG17():
        ag103_1 = Input_RPS.AG103()
        return ag103_1

@register(Dashboard_M16_EEPS)
class AH17():
    # 'Dashboard_M16_EEPS'!AH17
    value = 0
    formula = "='Input RPS'!AH103"
    @eval_fn
    def AH17():
        ah103_1 = Input_RPS.AH103()
        return ah103_1

@register(Dashboard_M16_EEPS)
class AI17():
    # 'Dashboard_M16_EEPS'!AI17
    value = 0
    formula = "='Input RPS'!AI103"
    @eval_fn
    def AI17():
        ai103_1 = Input_RPS.AI103()
        return ai103_1

@register(Dashboard_M16_EEPS)
class AJ17():
    # 'Dashboard_M16_EEPS'!AJ17
    value = 0
    formula = "='Input RPS'!AJ103"
    @eval_fn
    def AJ17():
        aj103_1 = Input_RPS.AJ103()
        return aj103_1

@register(Dashboard_M16_EEPS)
class AK17():
    # 'Dashboard_M16_EEPS'!AK17
    value = 0
    formula = "='Input RPS'!AK103"
    @eval_fn
    def AK17():
        ak103_1 = Input_RPS.AK103()
        return ak103_1

@register(Dashboard_M16_EEPS)
class AL17():
    # 'Dashboard_M16_EEPS'!AL17
    value = 0
    formula = "='Input RPS'!AL103"
    @eval_fn
    def AL17():
        al103_1 = Input_RPS.AL103()
        return al103_1

@register(Dashboard_M16_EEPS)
class A18():
    # 'Dashboard_M16_EEPS'!A18
    value = "Total EEHECO"
    formula = "=C18&C15"
    @eval_fn
    def A18():
        c18_1 = Dashboard_M16_EEPS.C18()
        c15_1 = Dashboard_M16_EEPS.C15()
        var_1 = concat(c18_1, c15_1)
        return var_1

@register(Dashboard_M16_EEPS)
class C18():
    # 'Dashboard_M16_EEPS'!C18
    value = "Total EE"

@register(Dashboard_M16_EEPS)
class G18():
    # 'Dashboard_M16_EEPS'!G18
    value = 0
    formula = "='Input RPS'!G104"
    @eval_fn
    def G18():
        g104_1 = Input_RPS.G104()
        return g104_1

@register(Dashboard_M16_EEPS)
class H18():
    # 'Dashboard_M16_EEPS'!H18
    value = 0
    formula = "='Input RPS'!H104"
    @eval_fn
    def H18():
        h104_1 = Input_RPS.H104()
        return h104_1

@register(Dashboard_M16_EEPS)
class I18():
    # 'Dashboard_M16_EEPS'!I18
    value = 0
    formula = "='Input RPS'!I104"
    @eval_fn
    def I18():
        i104_1 = Input_RPS.I104()
        return i104_1

@register(Dashboard_M16_EEPS)
class J18():
    # 'Dashboard_M16_EEPS'!J18
    value = 0
    formula = "='Input RPS'!J104"
    @eval_fn
    def J18():
        j104_1 = Input_RPS.J104()
        return j104_1

@register(Dashboard_M16_EEPS)
class K18():
    # 'Dashboard_M16_EEPS'!K18
    value = 0
    formula = "='Input RPS'!K104"
    @eval_fn
    def K18():
        k104_1 = Input_RPS.K104()
        return k104_1

@register(Dashboard_M16_EEPS)
class L18():
    # 'Dashboard_M16_EEPS'!L18
    value = 0
    formula = "='Input RPS'!L104"
    @eval_fn
    def L18():
        l104_1 = Input_RPS.L104()
        return l104_1

@register(Dashboard_M16_EEPS)
class M18():
    # 'Dashboard_M16_EEPS'!M18
    value = 343000
    formula = "='Input RPS'!M104"
    @eval_fn
    def M18():
        m104_1 = Input_RPS.M104()
        return m104_1

@register(Dashboard_M16_EEPS)
class N18():
    # 'Dashboard_M16_EEPS'!N18
    value = 398000
    formula = "='Input RPS'!N104"
    @eval_fn
    def N18():
        n104_1 = Input_RPS.N104()
        return n104_1

@register(Dashboard_M16_EEPS)
class O18():
    # 'Dashboard_M16_EEPS'!O18
    value = 519000
    formula = "='Input RPS'!O104"
    @eval_fn
    def O18():
        o104_1 = Input_RPS.O104()
        return o104_1

@register(Dashboard_M16_EEPS)
class P18():
    # 'Dashboard_M16_EEPS'!P18
    value = 679995
    formula = "='Input RPS'!P104"
    @eval_fn
    def P18():
        p104_1 = Input_RPS.P104()
        return p104_1

@register(Dashboard_M16_EEPS)
class Q18():
    # 'Dashboard_M16_EEPS'!Q18
    value = 738245
    formula = "='Input RPS'!Q104"
    @eval_fn
    def Q18():
        q104_1 = Input_RPS.Q104()
        return q104_1

@register(Dashboard_M16_EEPS)
class R18():
    # 'Dashboard_M16_EEPS'!R18
    value = 861138
    formula = "='Input RPS'!R104"
    @eval_fn
    def R18():
        r104_1 = Input_RPS.R104()
        return r104_1

@register(Dashboard_M16_EEPS)
class S18():
    # 'Dashboard_M16_EEPS'!S18
    value = 950450
    formula = "='Input RPS'!S104"
    @eval_fn
    def S18():
        s104_1 = Input_RPS.S104()
        return s104_1

@register(Dashboard_M16_EEPS)
class T18():
    # 'Dashboard_M16_EEPS'!T18
    value = 1090167
    formula = "='Input RPS'!T104"
    @eval_fn
    def T18():
        t104_1 = Input_RPS.T104()
        return t104_1

@register(Dashboard_M16_EEPS)
class U18():
    # 'Dashboard_M16_EEPS'!U18
    value = 1162109
    formula = "='Input RPS'!U104"
    @eval_fn
    def U18():
        u104_1 = Input_RPS.U104()
        return u104_1

@register(Dashboard_M16_EEPS)
class V18():
    # 'Dashboard_M16_EEPS'!V18
    value = 1228751
    formula = "='Input RPS'!V104"
    @eval_fn
    def V18():
        v104_1 = Input_RPS.V104()
        return v104_1

@register(Dashboard_M16_EEPS)
class W18():
    # 'Dashboard_M16_EEPS'!W18
    value = 1295393
    formula = "='Input RPS'!W104"
    @eval_fn
    def W18():
        w104_1 = Input_RPS.W104()
        return w104_1

@register(Dashboard_M16_EEPS)
class X18():
    # 'Dashboard_M16_EEPS'!X18
    value = 0
    formula = "='Input RPS'!X104"
    @eval_fn
    def X18():
        x104_1 = Input_RPS.X104()
        return x104_1

@register(Dashboard_M16_EEPS)
class Y18():
    # 'Dashboard_M16_EEPS'!Y18
    value = 0
    formula = "='Input RPS'!Y104"
    @eval_fn
    def Y18():
        y104_1 = Input_RPS.Y104()
        return y104_1

@register(Dashboard_M16_EEPS)
class Z18():
    # 'Dashboard_M16_EEPS'!Z18
    value = 0
    formula = "='Input RPS'!Z104"
    @eval_fn
    def Z18():
        z104_1 = Input_RPS.Z104()
        return z104_1

@register(Dashboard_M16_EEPS)
class AA18():
    # 'Dashboard_M16_EEPS'!AA18
    value = 0
    formula = "='Input RPS'!AA104"
    @eval_fn
    def AA18():
        aa104_1 = Input_RPS.AA104()
        return aa104_1

@register(Dashboard_M16_EEPS)
class AB18():
    # 'Dashboard_M16_EEPS'!AB18
    value = 0
    formula = "='Input RPS'!AB104"
    @eval_fn
    def AB18():
        ab104_1 = Input_RPS.AB104()
        return ab104_1

@register(Dashboard_M16_EEPS)
class AC18():
    # 'Dashboard_M16_EEPS'!AC18
    value = 0
    formula = "='Input RPS'!AC104"
    @eval_fn
    def AC18():
        ac104_1 = Input_RPS.AC104()
        return ac104_1

@register(Dashboard_M16_EEPS)
class AD18():
    # 'Dashboard_M16_EEPS'!AD18
    value = 0
    formula = "='Input RPS'!AD104"
    @eval_fn
    def AD18():
        ad104_1 = Input_RPS.AD104()
        return ad104_1

@register(Dashboard_M16_EEPS)
class AE18():
    # 'Dashboard_M16_EEPS'!AE18
    value = 0
    formula = "='Input RPS'!AE104"
    @eval_fn
    def AE18():
        ae104_1 = Input_RPS.AE104()
        return ae104_1

@register(Dashboard_M16_EEPS)
class AF18():
    # 'Dashboard_M16_EEPS'!AF18
    value = 0
    formula = "='Input RPS'!AF104"
    @eval_fn
    def AF18():
        af104_1 = Input_RPS.AF104()
        return af104_1

@register(Dashboard_M16_EEPS)
class AG18():
    # 'Dashboard_M16_EEPS'!AG18
    value = 0
    formula = "='Input RPS'!AG104"
    @eval_fn
    def AG18():
        ag104_1 = Input_RPS.AG104()
        return ag104_1

@register(Dashboard_M16_EEPS)
class AH18():
    # 'Dashboard_M16_EEPS'!AH18
    value = 0
    formula = "='Input RPS'!AH104"
    @eval_fn
    def AH18():
        ah104_1 = Input_RPS.AH104()
        return ah104_1

@register(Dashboard_M16_EEPS)
class AI18():
    # 'Dashboard_M16_EEPS'!AI18
    value = 0
    formula = "='Input RPS'!AI104"
    @eval_fn
    def AI18():
        ai104_1 = Input_RPS.AI104()
        return ai104_1

@register(Dashboard_M16_EEPS)
class AJ18():
    # 'Dashboard_M16_EEPS'!AJ18
    value = 0
    formula = "='Input RPS'!AJ104"
    @eval_fn
    def AJ18():
        aj104_1 = Input_RPS.AJ104()
        return aj104_1

@register(Dashboard_M16_EEPS)
class AK18():
    # 'Dashboard_M16_EEPS'!AK18
    value = 0
    formula = "='Input RPS'!AK104"
    @eval_fn
    def AK18():
        ak104_1 = Input_RPS.AK104()
        return ak104_1

@register(Dashboard_M16_EEPS)
class AL18():
    # 'Dashboard_M16_EEPS'!AL18
    value = 0
    formula = "='Input RPS'!AL104"
    @eval_fn
    def AL18():
        al104_1 = Input_RPS.AL104()
        return al104_1

@register(Dashboard_M16_EEPS)
class C19():
    # 'Dashboard_M16_EEPS'!C19
    value = "HELCO"

@register(Dashboard_M16_EEPS)
class D19():
    # 'Dashboard_M16_EEPS'!D19
    value = "MWh"

@register(Dashboard_M16_EEPS)
class C20():
    # 'Dashboard_M16_EEPS'!C20
    value = "  Displacement Tech: Solar Water Heating"

@register(Dashboard_M16_EEPS)
class G20():
    # 'Dashboard_M16_EEPS'!G20
    value = 0
    formula = "='Input RPS'!G107"
    @eval_fn
    def G20():
        g107_1 = Input_RPS.G107()
        return g107_1

@register(Dashboard_M16_EEPS)
class H20():
    # 'Dashboard_M16_EEPS'!H20
    value = 0
    formula = "='Input RPS'!H107"
    @eval_fn
    def H20():
        h107_1 = Input_RPS.H107()
        return h107_1

@register(Dashboard_M16_EEPS)
class I20():
    # 'Dashboard_M16_EEPS'!I20
    value = 0
    formula = "='Input RPS'!I107"
    @eval_fn
    def I20():
        i107_1 = Input_RPS.I107()
        return i107_1

@register(Dashboard_M16_EEPS)
class J20():
    # 'Dashboard_M16_EEPS'!J20
    value = 0
    formula = "='Input RPS'!J107"
    @eval_fn
    def J20():
        j107_1 = Input_RPS.J107()
        return j107_1

@register(Dashboard_M16_EEPS)
class K20():
    # 'Dashboard_M16_EEPS'!K20
    value = 0
    formula = "='Input RPS'!K107"
    @eval_fn
    def K20():
        k107_1 = Input_RPS.K107()
        return k107_1

@register(Dashboard_M16_EEPS)
class L20():
    # 'Dashboard_M16_EEPS'!L20
    value = 0
    formula = "='Input RPS'!L107"
    @eval_fn
    def L20():
        l107_1 = Input_RPS.L107()
        return l107_1

@register(Dashboard_M16_EEPS)
class M20():
    # 'Dashboard_M16_EEPS'!M20
    value = 10000
    formula = "='Input RPS'!M107"
    @eval_fn
    def M20():
        m107_1 = Input_RPS.M107()
        return m107_1

@register(Dashboard_M16_EEPS)
class N20():
    # 'Dashboard_M16_EEPS'!N20
    value = 11000
    formula = "='Input RPS'!N107"
    @eval_fn
    def N20():
        n107_1 = Input_RPS.N107()
        return n107_1

@register(Dashboard_M16_EEPS)
class O20():
    # 'Dashboard_M16_EEPS'!O20
    value = 13000
    formula = "='Input RPS'!O107"
    @eval_fn
    def O20():
        o107_1 = Input_RPS.O107()
        return o107_1

@register(Dashboard_M16_EEPS)
class P20():
    # 'Dashboard_M16_EEPS'!P20
    value = 13862
    formula = "='Input RPS'!P107"
    @eval_fn
    def P20():
        p107_1 = Input_RPS.P107()
        return p107_1

@register(Dashboard_M16_EEPS)
class Q20():
    # 'Dashboard_M16_EEPS'!Q20
    value = 14501
    formula = "='Input RPS'!Q107"
    @eval_fn
    def Q20():
        q107_1 = Input_RPS.Q107()
        return q107_1

@register(Dashboard_M16_EEPS)
class R20():
    # 'Dashboard_M16_EEPS'!R20
    value = 19572
    formula = "='Input RPS'!R107"
    @eval_fn
    def R20():
        r107_1 = Input_RPS.R107()
        return r107_1

@register(Dashboard_M16_EEPS)
class S20():
    # 'Dashboard_M16_EEPS'!S20
    value = 20678
    formula = "='Input RPS'!S107"
    @eval_fn
    def S20():
        s107_1 = Input_RPS.S107()
        return s107_1

@register(Dashboard_M16_EEPS)
class T20():
    # 'Dashboard_M16_EEPS'!T20
    value = 17919
    formula = "='Input RPS'!T107"
    @eval_fn
    def T20():
        t107_1 = Input_RPS.T107()
        return t107_1

@register(Dashboard_M16_EEPS)
class U20():
    # 'Dashboard_M16_EEPS'!U20
    value = 16678
    formula = "='Input RPS'!U107"
    @eval_fn
    def U20():
        u107_1 = Input_RPS.U107()
        return u107_1

@register(Dashboard_M16_EEPS)
class V20():
    # 'Dashboard_M16_EEPS'!V20
    value = 15317
    formula = "='Input RPS'!V107"
    @eval_fn
    def V20():
        v107_1 = Input_RPS.V107()
        return v107_1

@register(Dashboard_M16_EEPS)
class W20():
    # 'Dashboard_M16_EEPS'!W20
    value = 13956
    formula = "='Input RPS'!W107"
    @eval_fn
    def W20():
        w107_1 = Input_RPS.W107()
        return w107_1

@register(Dashboard_M16_EEPS)
class X20():
    # 'Dashboard_M16_EEPS'!X20
    value = 0
    formula = "='Input RPS'!X107"
    @eval_fn
    def X20():
        x107_1 = Input_RPS.X107()
        return x107_1

@register(Dashboard_M16_EEPS)
class Y20():
    # 'Dashboard_M16_EEPS'!Y20
    value = 0
    formula = "='Input RPS'!Y107"
    @eval_fn
    def Y20():
        y107_1 = Input_RPS.Y107()
        return y107_1

@register(Dashboard_M16_EEPS)
class Z20():
    # 'Dashboard_M16_EEPS'!Z20
    value = 0
    formula = "='Input RPS'!Z107"
    @eval_fn
    def Z20():
        z107_1 = Input_RPS.Z107()
        return z107_1

@register(Dashboard_M16_EEPS)
class AA20():
    # 'Dashboard_M16_EEPS'!AA20
    value = 0
    formula = "='Input RPS'!AA107"
    @eval_fn
    def AA20():
        aa107_1 = Input_RPS.AA107()
        return aa107_1

@register(Dashboard_M16_EEPS)
class AB20():
    # 'Dashboard_M16_EEPS'!AB20
    value = 0
    formula = "='Input RPS'!AB107"
    @eval_fn
    def AB20():
        ab107_1 = Input_RPS.AB107()
        return ab107_1

@register(Dashboard_M16_EEPS)
class AC20():
    # 'Dashboard_M16_EEPS'!AC20
    value = 0
    formula = "='Input RPS'!AC107"
    @eval_fn
    def AC20():
        ac107_1 = Input_RPS.AC107()
        return ac107_1

@register(Dashboard_M16_EEPS)
class AD20():
    # 'Dashboard_M16_EEPS'!AD20
    value = 0
    formula = "='Input RPS'!AD107"
    @eval_fn
    def AD20():
        ad107_1 = Input_RPS.AD107()
        return ad107_1

@register(Dashboard_M16_EEPS)
class AE20():
    # 'Dashboard_M16_EEPS'!AE20
    value = 0
    formula = "='Input RPS'!AE107"
    @eval_fn
    def AE20():
        ae107_1 = Input_RPS.AE107()
        return ae107_1

@register(Dashboard_M16_EEPS)
class AF20():
    # 'Dashboard_M16_EEPS'!AF20
    value = 0
    formula = "='Input RPS'!AF107"
    @eval_fn
    def AF20():
        af107_1 = Input_RPS.AF107()
        return af107_1

@register(Dashboard_M16_EEPS)
class AG20():
    # 'Dashboard_M16_EEPS'!AG20
    value = 0
    formula = "='Input RPS'!AG107"
    @eval_fn
    def AG20():
        ag107_1 = Input_RPS.AG107()
        return ag107_1

@register(Dashboard_M16_EEPS)
class AH20():
    # 'Dashboard_M16_EEPS'!AH20
    value = 0
    formula = "='Input RPS'!AH107"
    @eval_fn
    def AH20():
        ah107_1 = Input_RPS.AH107()
        return ah107_1

@register(Dashboard_M16_EEPS)
class AI20():
    # 'Dashboard_M16_EEPS'!AI20
    value = 0
    formula = "='Input RPS'!AI107"
    @eval_fn
    def AI20():
        ai107_1 = Input_RPS.AI107()
        return ai107_1

@register(Dashboard_M16_EEPS)
class AJ20():
    # 'Dashboard_M16_EEPS'!AJ20
    value = 0
    formula = "='Input RPS'!AJ107"
    @eval_fn
    def AJ20():
        aj107_1 = Input_RPS.AJ107()
        return aj107_1

@register(Dashboard_M16_EEPS)
class AK20():
    # 'Dashboard_M16_EEPS'!AK20
    value = 0
    formula = "='Input RPS'!AK107"
    @eval_fn
    def AK20():
        ak107_1 = Input_RPS.AK107()
        return ak107_1

@register(Dashboard_M16_EEPS)
class AL20():
    # 'Dashboard_M16_EEPS'!AL20
    value = 0
    formula = "='Input RPS'!AL107"
    @eval_fn
    def AL20():
        al107_1 = Input_RPS.AL107()
        return al107_1

@register(Dashboard_M16_EEPS)
class C21():
    # 'Dashboard_M16_EEPS'!C21
    value = "  Energy Efficiency Technologies"

@register(Dashboard_M16_EEPS)
class G21():
    # 'Dashboard_M16_EEPS'!G21
    value = 0
    formula = "='Input RPS'!G109"
    @eval_fn
    def G21():
        g109_1 = Input_RPS.G109()
        return g109_1

@register(Dashboard_M16_EEPS)
class H21():
    # 'Dashboard_M16_EEPS'!H21
    value = 0
    formula = "='Input RPS'!H109"
    @eval_fn
    def H21():
        h109_1 = Input_RPS.H109()
        return h109_1

@register(Dashboard_M16_EEPS)
class I21():
    # 'Dashboard_M16_EEPS'!I21
    value = 0
    formula = "='Input RPS'!I109"
    @eval_fn
    def I21():
        i109_1 = Input_RPS.I109()
        return i109_1

@register(Dashboard_M16_EEPS)
class J21():
    # 'Dashboard_M16_EEPS'!J21
    value = 0
    formula = "='Input RPS'!J109"
    @eval_fn
    def J21():
        j109_1 = Input_RPS.J109()
        return j109_1

@register(Dashboard_M16_EEPS)
class K21():
    # 'Dashboard_M16_EEPS'!K21
    value = 0
    formula = "='Input RPS'!K109"
    @eval_fn
    def K21():
        k109_1 = Input_RPS.K109()
        return k109_1

@register(Dashboard_M16_EEPS)
class L21():
    # 'Dashboard_M16_EEPS'!L21
    value = 0
    formula = "='Input RPS'!L109"
    @eval_fn
    def L21():
        l109_1 = Input_RPS.L109()
        return l109_1

@register(Dashboard_M16_EEPS)
class M21():
    # 'Dashboard_M16_EEPS'!M21
    value = 49000
    formula = "='Input RPS'!M109"
    @eval_fn
    def M21():
        m109_1 = Input_RPS.M109()
        return m109_1

@register(Dashboard_M16_EEPS)
class N21():
    # 'Dashboard_M16_EEPS'!N21
    value = 54000
    formula = "='Input RPS'!N109"
    @eval_fn
    def N21():
        n109_1 = Input_RPS.N109()
        return n109_1

@register(Dashboard_M16_EEPS)
class O21():
    # 'Dashboard_M16_EEPS'!O21
    value = 57000
    formula = "='Input RPS'!O109"
    @eval_fn
    def O21():
        o109_1 = Input_RPS.O109()
        return o109_1

@register(Dashboard_M16_EEPS)
class P21():
    # 'Dashboard_M16_EEPS'!P21
    value = 47051
    formula = "='Input RPS'!P109"
    @eval_fn
    def P21():
        p109_1 = Input_RPS.P109()
        return p109_1

@register(Dashboard_M16_EEPS)
class Q21():
    # 'Dashboard_M16_EEPS'!Q21
    value = 49760
    formula = "='Input RPS'!Q109"
    @eval_fn
    def Q21():
        q109_1 = Input_RPS.Q109()
        return q109_1

@register(Dashboard_M16_EEPS)
class R21():
    # 'Dashboard_M16_EEPS'!R21
    value = 62359
    formula = "='Input RPS'!R109"
    @eval_fn
    def R21():
        r109_1 = Input_RPS.R109()
        return r109_1

@register(Dashboard_M16_EEPS)
class S21():
    # 'Dashboard_M16_EEPS'!S21
    value = 76622
    formula = "='Input RPS'!S109"
    @eval_fn
    def S21():
        s109_1 = Input_RPS.S109()
        return s109_1

@register(Dashboard_M16_EEPS)
class T21():
    # 'Dashboard_M16_EEPS'!T21
    value = 97765
    formula = "='Input RPS'!T109"
    @eval_fn
    def T21():
        t109_1 = Input_RPS.T109()
        return t109_1

@register(Dashboard_M16_EEPS)
class U21():
    # 'Dashboard_M16_EEPS'!U21
    value = 114116
    formula = "='Input RPS'!U109"
    @eval_fn
    def U21():
        u109_1 = Input_RPS.U109()
        return u109_1

@register(Dashboard_M16_EEPS)
class V21():
    # 'Dashboard_M16_EEPS'!V21
    value = 123070
    formula = "='Input RPS'!V109"
    @eval_fn
    def V21():
        v109_1 = Input_RPS.V109()
        return v109_1

@register(Dashboard_M16_EEPS)
class W21():
    # 'Dashboard_M16_EEPS'!W21
    value = 132024
    formula = "='Input RPS'!W109"
    @eval_fn
    def W21():
        w109_1 = Input_RPS.W109()
        return w109_1

@register(Dashboard_M16_EEPS)
class X21():
    # 'Dashboard_M16_EEPS'!X21
    value = 0
    formula = "='Input RPS'!X109"
    @eval_fn
    def X21():
        x109_1 = Input_RPS.X109()
        return x109_1

@register(Dashboard_M16_EEPS)
class Y21():
    # 'Dashboard_M16_EEPS'!Y21
    value = 0
    formula = "='Input RPS'!Y109"
    @eval_fn
    def Y21():
        y109_1 = Input_RPS.Y109()
        return y109_1

@register(Dashboard_M16_EEPS)
class Z21():
    # 'Dashboard_M16_EEPS'!Z21
    value = 0
    formula = "='Input RPS'!Z109"
    @eval_fn
    def Z21():
        z109_1 = Input_RPS.Z109()
        return z109_1

@register(Dashboard_M16_EEPS)
class AA21():
    # 'Dashboard_M16_EEPS'!AA21
    value = 0
    formula = "='Input RPS'!AA109"
    @eval_fn
    def AA21():
        aa109_1 = Input_RPS.AA109()
        return aa109_1

@register(Dashboard_M16_EEPS)
class AB21():
    # 'Dashboard_M16_EEPS'!AB21
    value = 0
    formula = "='Input RPS'!AB109"
    @eval_fn
    def AB21():
        ab109_1 = Input_RPS.AB109()
        return ab109_1

@register(Dashboard_M16_EEPS)
class AC21():
    # 'Dashboard_M16_EEPS'!AC21
    value = 0
    formula = "='Input RPS'!AC109"
    @eval_fn
    def AC21():
        ac109_1 = Input_RPS.AC109()
        return ac109_1

@register(Dashboard_M16_EEPS)
class AD21():
    # 'Dashboard_M16_EEPS'!AD21
    value = 0
    formula = "='Input RPS'!AD109"
    @eval_fn
    def AD21():
        ad109_1 = Input_RPS.AD109()
        return ad109_1

@register(Dashboard_M16_EEPS)
class AE21():
    # 'Dashboard_M16_EEPS'!AE21
    value = 0
    formula = "='Input RPS'!AE109"
    @eval_fn
    def AE21():
        ae109_1 = Input_RPS.AE109()
        return ae109_1

@register(Dashboard_M16_EEPS)
class AF21():
    # 'Dashboard_M16_EEPS'!AF21
    value = 0
    formula = "='Input RPS'!AF109"
    @eval_fn
    def AF21():
        af109_1 = Input_RPS.AF109()
        return af109_1

@register(Dashboard_M16_EEPS)
class AG21():
    # 'Dashboard_M16_EEPS'!AG21
    value = 0
    formula = "='Input RPS'!AG109"
    @eval_fn
    def AG21():
        ag109_1 = Input_RPS.AG109()
        return ag109_1

@register(Dashboard_M16_EEPS)
class AH21():
    # 'Dashboard_M16_EEPS'!AH21
    value = 0
    formula = "='Input RPS'!AH109"
    @eval_fn
    def AH21():
        ah109_1 = Input_RPS.AH109()
        return ah109_1

@register(Dashboard_M16_EEPS)
class AI21():
    # 'Dashboard_M16_EEPS'!AI21
    value = 0
    formula = "='Input RPS'!AI109"
    @eval_fn
    def AI21():
        ai109_1 = Input_RPS.AI109()
        return ai109_1

@register(Dashboard_M16_EEPS)
class AJ21():
    # 'Dashboard_M16_EEPS'!AJ21
    value = 0
    formula = "='Input RPS'!AJ109"
    @eval_fn
    def AJ21():
        aj109_1 = Input_RPS.AJ109()
        return aj109_1

@register(Dashboard_M16_EEPS)
class AK21():
    # 'Dashboard_M16_EEPS'!AK21
    value = 0
    formula = "='Input RPS'!AK109"
    @eval_fn
    def AK21():
        ak109_1 = Input_RPS.AK109()
        return ak109_1

@register(Dashboard_M16_EEPS)
class AL21():
    # 'Dashboard_M16_EEPS'!AL21
    value = 0
    formula = "='Input RPS'!AL109"
    @eval_fn
    def AL21():
        al109_1 = Input_RPS.AL109()
        return al109_1

@register(Dashboard_M16_EEPS)
class A22():
    # 'Dashboard_M16_EEPS'!A22
    value = "Total EEHELCO"
    formula = "=C22&C19"
    @eval_fn
    def A22():
        c22_1 = Dashboard_M16_EEPS.C22()
        c19_1 = Dashboard_M16_EEPS.C19()
        var_1 = concat(c22_1, c19_1)
        return var_1

@register(Dashboard_M16_EEPS)
class C22():
    # 'Dashboard_M16_EEPS'!C22
    value = "Total EE"

@register(Dashboard_M16_EEPS)
class G22():
    # 'Dashboard_M16_EEPS'!G22
    value = 0
    formula = "='Input RPS'!G110"
    @eval_fn
    def G22():
        g110_1 = Input_RPS.G110()
        return g110_1

@register(Dashboard_M16_EEPS)
class H22():
    # 'Dashboard_M16_EEPS'!H22
    value = 0
    formula = "='Input RPS'!H110"
    @eval_fn
    def H22():
        h110_1 = Input_RPS.H110()
        return h110_1

@register(Dashboard_M16_EEPS)
class I22():
    # 'Dashboard_M16_EEPS'!I22
    value = 0
    formula = "='Input RPS'!I110"
    @eval_fn
    def I22():
        i110_1 = Input_RPS.I110()
        return i110_1

@register(Dashboard_M16_EEPS)
class J22():
    # 'Dashboard_M16_EEPS'!J22
    value = 0
    formula = "='Input RPS'!J110"
    @eval_fn
    def J22():
        j110_1 = Input_RPS.J110()
        return j110_1

@register(Dashboard_M16_EEPS)
class K22():
    # 'Dashboard_M16_EEPS'!K22
    value = 0
    formula = "='Input RPS'!K110"
    @eval_fn
    def K22():
        k110_1 = Input_RPS.K110()
        return k110_1

@register(Dashboard_M16_EEPS)
class L22():
    # 'Dashboard_M16_EEPS'!L22
    value = 0
    formula = "='Input RPS'!L110"
    @eval_fn
    def L22():
        l110_1 = Input_RPS.L110()
        return l110_1

@register(Dashboard_M16_EEPS)
class M22():
    # 'Dashboard_M16_EEPS'!M22
    value = 59000
    formula = "='Input RPS'!M110"
    @eval_fn
    def M22():
        m110_1 = Input_RPS.M110()
        return m110_1

@register(Dashboard_M16_EEPS)
class N22():
    # 'Dashboard_M16_EEPS'!N22
    value = 65000
    formula = "='Input RPS'!N110"
    @eval_fn
    def N22():
        n110_1 = Input_RPS.N110()
        return n110_1

@register(Dashboard_M16_EEPS)
class O22():
    # 'Dashboard_M16_EEPS'!O22
    value = 70000
    formula = "='Input RPS'!O110"
    @eval_fn
    def O22():
        o110_1 = Input_RPS.O110()
        return o110_1

@register(Dashboard_M16_EEPS)
class P22():
    # 'Dashboard_M16_EEPS'!P22
    value = 60913
    formula = "='Input RPS'!P110"
    @eval_fn
    def P22():
        p110_1 = Input_RPS.P110()
        return p110_1

@register(Dashboard_M16_EEPS)
class Q22():
    # 'Dashboard_M16_EEPS'!Q22
    value = 64261
    formula = "='Input RPS'!Q110"
    @eval_fn
    def Q22():
        q110_1 = Input_RPS.Q110()
        return q110_1

@register(Dashboard_M16_EEPS)
class R22():
    # 'Dashboard_M16_EEPS'!R22
    value = 81931
    formula = "='Input RPS'!R110"
    @eval_fn
    def R22():
        r110_1 = Input_RPS.R110()
        return r110_1

@register(Dashboard_M16_EEPS)
class S22():
    # 'Dashboard_M16_EEPS'!S22
    value = 97300
    formula = "='Input RPS'!S110"
    @eval_fn
    def S22():
        s110_1 = Input_RPS.S110()
        return s110_1

@register(Dashboard_M16_EEPS)
class T22():
    # 'Dashboard_M16_EEPS'!T22
    value = 119618
    formula = "='Input RPS'!T110"
    @eval_fn
    def T22():
        t110_1 = Input_RPS.T110()
        return t110_1

@register(Dashboard_M16_EEPS)
class U22():
    # 'Dashboard_M16_EEPS'!U22
    value = 135422
    formula = "='Input RPS'!U110"
    @eval_fn
    def U22():
        u110_1 = Input_RPS.U110()
        return u110_1

@register(Dashboard_M16_EEPS)
class V22():
    # 'Dashboard_M16_EEPS'!V22
    value = 143468
    formula = "='Input RPS'!V110"
    @eval_fn
    def V22():
        v110_1 = Input_RPS.V110()
        return v110_1

@register(Dashboard_M16_EEPS)
class W22():
    # 'Dashboard_M16_EEPS'!W22
    value = 151514
    formula = "='Input RPS'!W110"
    @eval_fn
    def W22():
        w110_1 = Input_RPS.W110()
        return w110_1

@register(Dashboard_M16_EEPS)
class X22():
    # 'Dashboard_M16_EEPS'!X22
    value = 0
    formula = "='Input RPS'!X110"
    @eval_fn
    def X22():
        x110_1 = Input_RPS.X110()
        return x110_1

@register(Dashboard_M16_EEPS)
class Y22():
    # 'Dashboard_M16_EEPS'!Y22
    value = 0
    formula = "='Input RPS'!Y110"
    @eval_fn
    def Y22():
        y110_1 = Input_RPS.Y110()
        return y110_1

@register(Dashboard_M16_EEPS)
class Z22():
    # 'Dashboard_M16_EEPS'!Z22
    value = 0
    formula = "='Input RPS'!Z110"
    @eval_fn
    def Z22():
        z110_1 = Input_RPS.Z110()
        return z110_1

@register(Dashboard_M16_EEPS)
class AA22():
    # 'Dashboard_M16_EEPS'!AA22
    value = 0
    formula = "='Input RPS'!AA110"
    @eval_fn
    def AA22():
        aa110_1 = Input_RPS.AA110()
        return aa110_1

@register(Dashboard_M16_EEPS)
class AB22():
    # 'Dashboard_M16_EEPS'!AB22
    value = 0
    formula = "='Input RPS'!AB110"
    @eval_fn
    def AB22():
        ab110_1 = Input_RPS.AB110()
        return ab110_1

@register(Dashboard_M16_EEPS)
class AC22():
    # 'Dashboard_M16_EEPS'!AC22
    value = 0
    formula = "='Input RPS'!AC110"
    @eval_fn
    def AC22():
        ac110_1 = Input_RPS.AC110()
        return ac110_1

@register(Dashboard_M16_EEPS)
class AD22():
    # 'Dashboard_M16_EEPS'!AD22
    value = 0
    formula = "='Input RPS'!AD110"
    @eval_fn
    def AD22():
        ad110_1 = Input_RPS.AD110()
        return ad110_1

@register(Dashboard_M16_EEPS)
class AE22():
    # 'Dashboard_M16_EEPS'!AE22
    value = 0
    formula = "='Input RPS'!AE110"
    @eval_fn
    def AE22():
        ae110_1 = Input_RPS.AE110()
        return ae110_1

@register(Dashboard_M16_EEPS)
class AF22():
    # 'Dashboard_M16_EEPS'!AF22
    value = 0
    formula = "='Input RPS'!AF110"
    @eval_fn
    def AF22():
        af110_1 = Input_RPS.AF110()
        return af110_1

@register(Dashboard_M16_EEPS)
class AG22():
    # 'Dashboard_M16_EEPS'!AG22
    value = 0
    formula = "='Input RPS'!AG110"
    @eval_fn
    def AG22():
        ag110_1 = Input_RPS.AG110()
        return ag110_1

@register(Dashboard_M16_EEPS)
class AH22():
    # 'Dashboard_M16_EEPS'!AH22
    value = 0
    formula = "='Input RPS'!AH110"
    @eval_fn
    def AH22():
        ah110_1 = Input_RPS.AH110()
        return ah110_1

@register(Dashboard_M16_EEPS)
class AI22():
    # 'Dashboard_M16_EEPS'!AI22
    value = 0
    formula = "='Input RPS'!AI110"
    @eval_fn
    def AI22():
        ai110_1 = Input_RPS.AI110()
        return ai110_1

@register(Dashboard_M16_EEPS)
class AJ22():
    # 'Dashboard_M16_EEPS'!AJ22
    value = 0
    formula = "='Input RPS'!AJ110"
    @eval_fn
    def AJ22():
        aj110_1 = Input_RPS.AJ110()
        return aj110_1

@register(Dashboard_M16_EEPS)
class AK22():
    # 'Dashboard_M16_EEPS'!AK22
    value = 0
    formula = "='Input RPS'!AK110"
    @eval_fn
    def AK22():
        ak110_1 = Input_RPS.AK110()
        return ak110_1

@register(Dashboard_M16_EEPS)
class AL22():
    # 'Dashboard_M16_EEPS'!AL22
    value = 0
    formula = "='Input RPS'!AL110"
    @eval_fn
    def AL22():
        al110_1 = Input_RPS.AL110()
        return al110_1

@register(Dashboard_M16_EEPS)
class C23():
    # 'Dashboard_M16_EEPS'!C23
    value = "MECO"

@register(Dashboard_M16_EEPS)
class D23():
    # 'Dashboard_M16_EEPS'!D23
    value = "MWh"

@register(Dashboard_M16_EEPS)
class C24():
    # 'Dashboard_M16_EEPS'!C24
    value = "  Displacement Tech: Solar Water Heating"

@register(Dashboard_M16_EEPS)
class G24():
    # 'Dashboard_M16_EEPS'!G24
    value = 0
    formula = "='Input RPS'!G113"
    @eval_fn
    def G24():
        g113_1 = Input_RPS.G113()
        return g113_1

@register(Dashboard_M16_EEPS)
class H24():
    # 'Dashboard_M16_EEPS'!H24
    value = 0
    formula = "='Input RPS'!H113"
    @eval_fn
    def H24():
        h113_1 = Input_RPS.H113()
        return h113_1

@register(Dashboard_M16_EEPS)
class I24():
    # 'Dashboard_M16_EEPS'!I24
    value = 0
    formula = "='Input RPS'!I113"
    @eval_fn
    def I24():
        i113_1 = Input_RPS.I113()
        return i113_1

@register(Dashboard_M16_EEPS)
class J24():
    # 'Dashboard_M16_EEPS'!J24
    value = 0
    formula = "='Input RPS'!J113"
    @eval_fn
    def J24():
        j113_1 = Input_RPS.J113()
        return j113_1

@register(Dashboard_M16_EEPS)
class K24():
    # 'Dashboard_M16_EEPS'!K24
    value = 0
    formula = "='Input RPS'!K113"
    @eval_fn
    def K24():
        k113_1 = Input_RPS.K113()
        return k113_1

@register(Dashboard_M16_EEPS)
class L24():
    # 'Dashboard_M16_EEPS'!L24
    value = 0
    formula = "='Input RPS'!L113"
    @eval_fn
    def L24():
        l113_1 = Input_RPS.L113()
        return l113_1

@register(Dashboard_M16_EEPS)
class M24():
    # 'Dashboard_M16_EEPS'!M24
    value = 23000
    formula = "='Input RPS'!M113"
    @eval_fn
    def M24():
        m113_1 = Input_RPS.M113()
        return m113_1

@register(Dashboard_M16_EEPS)
class N24():
    # 'Dashboard_M16_EEPS'!N24
    value = 26000
    formula = "='Input RPS'!N113"
    @eval_fn
    def N24():
        n113_1 = Input_RPS.N113()
        return n113_1

@register(Dashboard_M16_EEPS)
class O24():
    # 'Dashboard_M16_EEPS'!O24
    value = 30000
    formula = "='Input RPS'!O113"
    @eval_fn
    def O24():
        o113_1 = Input_RPS.O113()
        return o113_1

@register(Dashboard_M16_EEPS)
class P24():
    # 'Dashboard_M16_EEPS'!P24
    value = 27429
    formula = "='Input RPS'!P113"
    @eval_fn
    def P24():
        p113_1 = Input_RPS.P113()
        return p113_1

@register(Dashboard_M16_EEPS)
class Q24():
    # 'Dashboard_M16_EEPS'!Q24
    value = 28492
    formula = "='Input RPS'!Q113"
    @eval_fn
    def Q24():
        q113_1 = Input_RPS.Q113()
        return q113_1

@register(Dashboard_M16_EEPS)
class R24():
    # 'Dashboard_M16_EEPS'!R24
    value = 29683
    formula = "='Input RPS'!R113"
    @eval_fn
    def R24():
        r113_1 = Input_RPS.R113()
        return r113_1

@register(Dashboard_M16_EEPS)
class S24():
    # 'Dashboard_M16_EEPS'!S24
    value = 30181
    formula = "='Input RPS'!S113"
    @eval_fn
    def S24():
        s113_1 = Input_RPS.S113()
        return s113_1

@register(Dashboard_M16_EEPS)
class T24():
    # 'Dashboard_M16_EEPS'!T24
    value = 28341
    formula = "='Input RPS'!T113"
    @eval_fn
    def T24():
        t113_1 = Input_RPS.T113()
        return t113_1

@register(Dashboard_M16_EEPS)
class U24():
    # 'Dashboard_M16_EEPS'!U24
    value = 26774
    formula = "='Input RPS'!U113"
    @eval_fn
    def U24():
        u113_1 = Input_RPS.U113()
        return u113_1

@register(Dashboard_M16_EEPS)
class V24():
    # 'Dashboard_M16_EEPS'!V24
    value = 24216
    formula = "='Input RPS'!V113"
    @eval_fn
    def V24():
        v113_1 = Input_RPS.V113()
        return v113_1

@register(Dashboard_M16_EEPS)
class W24():
    # 'Dashboard_M16_EEPS'!W24
    value = 21658
    formula = "='Input RPS'!W113"
    @eval_fn
    def W24():
        w113_1 = Input_RPS.W113()
        return w113_1

@register(Dashboard_M16_EEPS)
class X24():
    # 'Dashboard_M16_EEPS'!X24
    value = 0
    formula = "='Input RPS'!X113"
    @eval_fn
    def X24():
        x113_1 = Input_RPS.X113()
        return x113_1

@register(Dashboard_M16_EEPS)
class Y24():
    # 'Dashboard_M16_EEPS'!Y24
    value = 0
    formula = "='Input RPS'!Y113"
    @eval_fn
    def Y24():
        y113_1 = Input_RPS.Y113()
        return y113_1

@register(Dashboard_M16_EEPS)
class Z24():
    # 'Dashboard_M16_EEPS'!Z24
    value = 0
    formula = "='Input RPS'!Z113"
    @eval_fn
    def Z24():
        z113_1 = Input_RPS.Z113()
        return z113_1

@register(Dashboard_M16_EEPS)
class AA24():
    # 'Dashboard_M16_EEPS'!AA24
    value = 0
    formula = "='Input RPS'!AA113"
    @eval_fn
    def AA24():
        aa113_1 = Input_RPS.AA113()
        return aa113_1

@register(Dashboard_M16_EEPS)
class AB24():
    # 'Dashboard_M16_EEPS'!AB24
    value = 0
    formula = "='Input RPS'!AB113"
    @eval_fn
    def AB24():
        ab113_1 = Input_RPS.AB113()
        return ab113_1

@register(Dashboard_M16_EEPS)
class AC24():
    # 'Dashboard_M16_EEPS'!AC24
    value = 0
    formula = "='Input RPS'!AC113"
    @eval_fn
    def AC24():
        ac113_1 = Input_RPS.AC113()
        return ac113_1

@register(Dashboard_M16_EEPS)
class AD24():
    # 'Dashboard_M16_EEPS'!AD24
    value = 0
    formula = "='Input RPS'!AD113"
    @eval_fn
    def AD24():
        ad113_1 = Input_RPS.AD113()
        return ad113_1

@register(Dashboard_M16_EEPS)
class AE24():
    # 'Dashboard_M16_EEPS'!AE24
    value = 0
    formula = "='Input RPS'!AE113"
    @eval_fn
    def AE24():
        ae113_1 = Input_RPS.AE113()
        return ae113_1

@register(Dashboard_M16_EEPS)
class AF24():
    # 'Dashboard_M16_EEPS'!AF24
    value = 0
    formula = "='Input RPS'!AF113"
    @eval_fn
    def AF24():
        af113_1 = Input_RPS.AF113()
        return af113_1

@register(Dashboard_M16_EEPS)
class AG24():
    # 'Dashboard_M16_EEPS'!AG24
    value = 0
    formula = "='Input RPS'!AG113"
    @eval_fn
    def AG24():
        ag113_1 = Input_RPS.AG113()
        return ag113_1

@register(Dashboard_M16_EEPS)
class AH24():
    # 'Dashboard_M16_EEPS'!AH24
    value = 0
    formula = "='Input RPS'!AH113"
    @eval_fn
    def AH24():
        ah113_1 = Input_RPS.AH113()
        return ah113_1

@register(Dashboard_M16_EEPS)
class AI24():
    # 'Dashboard_M16_EEPS'!AI24
    value = 0
    formula = "='Input RPS'!AI113"
    @eval_fn
    def AI24():
        ai113_1 = Input_RPS.AI113()
        return ai113_1

@register(Dashboard_M16_EEPS)
class AJ24():
    # 'Dashboard_M16_EEPS'!AJ24
    value = 0
    formula = "='Input RPS'!AJ113"
    @eval_fn
    def AJ24():
        aj113_1 = Input_RPS.AJ113()
        return aj113_1

@register(Dashboard_M16_EEPS)
class AK24():
    # 'Dashboard_M16_EEPS'!AK24
    value = 0
    formula = "='Input RPS'!AK113"
    @eval_fn
    def AK24():
        ak113_1 = Input_RPS.AK113()
        return ak113_1

@register(Dashboard_M16_EEPS)
class AL24():
    # 'Dashboard_M16_EEPS'!AL24
    value = 0
    formula = "='Input RPS'!AL113"
    @eval_fn
    def AL24():
        al113_1 = Input_RPS.AL113()
        return al113_1

@register(Dashboard_M16_EEPS)
class C25():
    # 'Dashboard_M16_EEPS'!C25
    value = "  Energy Efficiency Technologies"

@register(Dashboard_M16_EEPS)
class G25():
    # 'Dashboard_M16_EEPS'!G25
    value = 0
    formula = "='Input RPS'!G115"
    @eval_fn
    def G25():
        g115_1 = Input_RPS.G115()
        return g115_1

@register(Dashboard_M16_EEPS)
class H25():
    # 'Dashboard_M16_EEPS'!H25
    value = 0
    formula = "='Input RPS'!H115"
    @eval_fn
    def H25():
        h115_1 = Input_RPS.H115()
        return h115_1

@register(Dashboard_M16_EEPS)
class I25():
    # 'Dashboard_M16_EEPS'!I25
    value = 0
    formula = "='Input RPS'!I115"
    @eval_fn
    def I25():
        i115_1 = Input_RPS.I115()
        return i115_1

@register(Dashboard_M16_EEPS)
class J25():
    # 'Dashboard_M16_EEPS'!J25
    value = 0
    formula = "='Input RPS'!J115"
    @eval_fn
    def J25():
        j115_1 = Input_RPS.J115()
        return j115_1

@register(Dashboard_M16_EEPS)
class K25():
    # 'Dashboard_M16_EEPS'!K25
    value = 0
    formula = "='Input RPS'!K115"
    @eval_fn
    def K25():
        k115_1 = Input_RPS.K115()
        return k115_1

@register(Dashboard_M16_EEPS)
class L25():
    # 'Dashboard_M16_EEPS'!L25
    value = 0
    formula = "='Input RPS'!L115"
    @eval_fn
    def L25():
        l115_1 = Input_RPS.L115()
        return l115_1

@register(Dashboard_M16_EEPS)
class M25():
    # 'Dashboard_M16_EEPS'!M25
    value = 77000
    formula = "='Input RPS'!M115"
    @eval_fn
    def M25():
        m115_1 = Input_RPS.M115()
        return m115_1

@register(Dashboard_M16_EEPS)
class N25():
    # 'Dashboard_M16_EEPS'!N25
    value = 82000
    formula = "='Input RPS'!N115"
    @eval_fn
    def N25():
        n115_1 = Input_RPS.N115()
        return n115_1

@register(Dashboard_M16_EEPS)
class O25():
    # 'Dashboard_M16_EEPS'!O25
    value = 88000
    formula = "='Input RPS'!O115"
    @eval_fn
    def O25():
        o115_1 = Input_RPS.O115()
        return o115_1

@register(Dashboard_M16_EEPS)
class P25():
    # 'Dashboard_M16_EEPS'!P25
    value = 79835
    formula = "='Input RPS'!P115"
    @eval_fn
    def P25():
        p115_1 = Input_RPS.P115()
        return p115_1

@register(Dashboard_M16_EEPS)
class Q25():
    # 'Dashboard_M16_EEPS'!Q25
    value = 88593
    formula = "='Input RPS'!Q115"
    @eval_fn
    def Q25():
        q115_1 = Input_RPS.Q115()
        return q115_1

@register(Dashboard_M16_EEPS)
class R25():
    # 'Dashboard_M16_EEPS'!R25
    value = 98813
    formula = "='Input RPS'!R115"
    @eval_fn
    def R25():
        r115_1 = Input_RPS.R115()
        return r115_1

@register(Dashboard_M16_EEPS)
class S25():
    # 'Dashboard_M16_EEPS'!S25
    value = 111306
    formula = "='Input RPS'!S115"
    @eval_fn
    def S25():
        s115_1 = Input_RPS.S115()
        return s115_1

@register(Dashboard_M16_EEPS)
class T25():
    # 'Dashboard_M16_EEPS'!T25
    value = 129340
    formula = "='Input RPS'!T115"
    @eval_fn
    def T25():
        t115_1 = Input_RPS.T115()
        return t115_1

@register(Dashboard_M16_EEPS)
class U25():
    # 'Dashboard_M16_EEPS'!U25
    value = 144281
    formula = "='Input RPS'!U115"
    @eval_fn
    def U25():
        u115_1 = Input_RPS.U115()
        return u115_1

@register(Dashboard_M16_EEPS)
class V25():
    # 'Dashboard_M16_EEPS'!V25
    value = 154216
    formula = "='Input RPS'!V115"
    @eval_fn
    def V25():
        v115_1 = Input_RPS.V115()
        return v115_1

@register(Dashboard_M16_EEPS)
class W25():
    # 'Dashboard_M16_EEPS'!W25
    value = 164151
    formula = "='Input RPS'!W115"
    @eval_fn
    def W25():
        w115_1 = Input_RPS.W115()
        return w115_1

@register(Dashboard_M16_EEPS)
class X25():
    # 'Dashboard_M16_EEPS'!X25
    value = 0
    formula = "='Input RPS'!X115"
    @eval_fn
    def X25():
        x115_1 = Input_RPS.X115()
        return x115_1

@register(Dashboard_M16_EEPS)
class Y25():
    # 'Dashboard_M16_EEPS'!Y25
    value = 0
    formula = "='Input RPS'!Y115"
    @eval_fn
    def Y25():
        y115_1 = Input_RPS.Y115()
        return y115_1

@register(Dashboard_M16_EEPS)
class Z25():
    # 'Dashboard_M16_EEPS'!Z25
    value = 0
    formula = "='Input RPS'!Z115"
    @eval_fn
    def Z25():
        z115_1 = Input_RPS.Z115()
        return z115_1

@register(Dashboard_M16_EEPS)
class AA25():
    # 'Dashboard_M16_EEPS'!AA25
    value = 0
    formula = "='Input RPS'!AA115"
    @eval_fn
    def AA25():
        aa115_1 = Input_RPS.AA115()
        return aa115_1

@register(Dashboard_M16_EEPS)
class AB25():
    # 'Dashboard_M16_EEPS'!AB25
    value = 0
    formula = "='Input RPS'!AB115"
    @eval_fn
    def AB25():
        ab115_1 = Input_RPS.AB115()
        return ab115_1

@register(Dashboard_M16_EEPS)
class AC25():
    # 'Dashboard_M16_EEPS'!AC25
    value = 0
    formula = "='Input RPS'!AC115"
    @eval_fn
    def AC25():
        ac115_1 = Input_RPS.AC115()
        return ac115_1

@register(Dashboard_M16_EEPS)
class AD25():
    # 'Dashboard_M16_EEPS'!AD25
    value = 0
    formula = "='Input RPS'!AD115"
    @eval_fn
    def AD25():
        ad115_1 = Input_RPS.AD115()
        return ad115_1

@register(Dashboard_M16_EEPS)
class AE25():
    # 'Dashboard_M16_EEPS'!AE25
    value = 0
    formula = "='Input RPS'!AE115"
    @eval_fn
    def AE25():
        ae115_1 = Input_RPS.AE115()
        return ae115_1

@register(Dashboard_M16_EEPS)
class AF25():
    # 'Dashboard_M16_EEPS'!AF25
    value = 0
    formula = "='Input RPS'!AF115"
    @eval_fn
    def AF25():
        af115_1 = Input_RPS.AF115()
        return af115_1

@register(Dashboard_M16_EEPS)
class AG25():
    # 'Dashboard_M16_EEPS'!AG25
    value = 0
    formula = "='Input RPS'!AG115"
    @eval_fn
    def AG25():
        ag115_1 = Input_RPS.AG115()
        return ag115_1

@register(Dashboard_M16_EEPS)
class AH25():
    # 'Dashboard_M16_EEPS'!AH25
    value = 0
    formula = "='Input RPS'!AH115"
    @eval_fn
    def AH25():
        ah115_1 = Input_RPS.AH115()
        return ah115_1

@register(Dashboard_M16_EEPS)
class AI25():
    # 'Dashboard_M16_EEPS'!AI25
    value = 0
    formula = "='Input RPS'!AI115"
    @eval_fn
    def AI25():
        ai115_1 = Input_RPS.AI115()
        return ai115_1

@register(Dashboard_M16_EEPS)
class AJ25():
    # 'Dashboard_M16_EEPS'!AJ25
    value = 0
    formula = "='Input RPS'!AJ115"
    @eval_fn
    def AJ25():
        aj115_1 = Input_RPS.AJ115()
        return aj115_1

@register(Dashboard_M16_EEPS)
class AK25():
    # 'Dashboard_M16_EEPS'!AK25
    value = 0
    formula = "='Input RPS'!AK115"
    @eval_fn
    def AK25():
        ak115_1 = Input_RPS.AK115()
        return ak115_1

@register(Dashboard_M16_EEPS)
class AL25():
    # 'Dashboard_M16_EEPS'!AL25
    value = 0
    formula = "='Input RPS'!AL115"
    @eval_fn
    def AL25():
        al115_1 = Input_RPS.AL115()
        return al115_1

@register(Dashboard_M16_EEPS)
class A26():
    # 'Dashboard_M16_EEPS'!A26
    value = "Total EEMECO"
    formula = "=C26&C23"
    @eval_fn
    def A26():
        c26_1 = Dashboard_M16_EEPS.C26()
        c23_1 = Dashboard_M16_EEPS.C23()
        var_1 = concat(c26_1, c23_1)
        return var_1

@register(Dashboard_M16_EEPS)
class C26():
    # 'Dashboard_M16_EEPS'!C26
    value = "Total EE"

@register(Dashboard_M16_EEPS)
class G26():
    # 'Dashboard_M16_EEPS'!G26
    value = 0
    formula = "='Input RPS'!G116"
    @eval_fn
    def G26():
        g116_1 = Input_RPS.G116()
        return g116_1

@register(Dashboard_M16_EEPS)
class H26():
    # 'Dashboard_M16_EEPS'!H26
    value = 0
    formula = "='Input RPS'!H116"
    @eval_fn
    def H26():
        h116_1 = Input_RPS.H116()
        return h116_1

@register(Dashboard_M16_EEPS)
class I26():
    # 'Dashboard_M16_EEPS'!I26
    value = 0
    formula = "='Input RPS'!I116"
    @eval_fn
    def I26():
        i116_1 = Input_RPS.I116()
        return i116_1

@register(Dashboard_M16_EEPS)
class J26():
    # 'Dashboard_M16_EEPS'!J26
    value = 0
    formula = "='Input RPS'!J116"
    @eval_fn
    def J26():
        j116_1 = Input_RPS.J116()
        return j116_1

@register(Dashboard_M16_EEPS)
class K26():
    # 'Dashboard_M16_EEPS'!K26
    value = 0
    formula = "='Input RPS'!K116"
    @eval_fn
    def K26():
        k116_1 = Input_RPS.K116()
        return k116_1

@register(Dashboard_M16_EEPS)
class L26():
    # 'Dashboard_M16_EEPS'!L26
    value = 0
    formula = "='Input RPS'!L116"
    @eval_fn
    def L26():
        l116_1 = Input_RPS.L116()
        return l116_1

@register(Dashboard_M16_EEPS)
class M26():
    # 'Dashboard_M16_EEPS'!M26
    value = 100000
    formula = "='Input RPS'!M116"
    @eval_fn
    def M26():
        m116_1 = Input_RPS.M116()
        return m116_1

@register(Dashboard_M16_EEPS)
class N26():
    # 'Dashboard_M16_EEPS'!N26
    value = 108000
    formula = "='Input RPS'!N116"
    @eval_fn
    def N26():
        n116_1 = Input_RPS.N116()
        return n116_1

@register(Dashboard_M16_EEPS)
class O26():
    # 'Dashboard_M16_EEPS'!O26
    value = 118000
    formula = "='Input RPS'!O116"
    @eval_fn
    def O26():
        o116_1 = Input_RPS.O116()
        return o116_1

@register(Dashboard_M16_EEPS)
class P26():
    # 'Dashboard_M16_EEPS'!P26
    value = 107264
    formula = "='Input RPS'!P116"
    @eval_fn
    def P26():
        p116_1 = Input_RPS.P116()
        return p116_1

@register(Dashboard_M16_EEPS)
class Q26():
    # 'Dashboard_M16_EEPS'!Q26
    value = 117085
    formula = "='Input RPS'!Q116"
    @eval_fn
    def Q26():
        q116_1 = Input_RPS.Q116()
        return q116_1

@register(Dashboard_M16_EEPS)
class R26():
    # 'Dashboard_M16_EEPS'!R26
    value = 128496
    formula = "='Input RPS'!R116"
    @eval_fn
    def R26():
        r116_1 = Input_RPS.R116()
        return r116_1

@register(Dashboard_M16_EEPS)
class S26():
    # 'Dashboard_M16_EEPS'!S26
    value = 141487
    formula = "='Input RPS'!S116"
    @eval_fn
    def S26():
        s116_1 = Input_RPS.S116()
        return s116_1

@register(Dashboard_M16_EEPS)
class T26():
    # 'Dashboard_M16_EEPS'!T26
    value = 160186
    formula = "='Input RPS'!T116"
    @eval_fn
    def T26():
        t116_1 = Input_RPS.T116()
        return t116_1

@register(Dashboard_M16_EEPS)
class U26():
    # 'Dashboard_M16_EEPS'!U26
    value = 174216
    formula = "='Input RPS'!U116"
    @eval_fn
    def U26():
        u116_1 = Input_RPS.U116()
        return u116_1

@register(Dashboard_M16_EEPS)
class V26():
    # 'Dashboard_M16_EEPS'!V26
    value = 182534
    formula = "='Input RPS'!V116"
    @eval_fn
    def V26():
        v116_1 = Input_RPS.V116()
        return v116_1

@register(Dashboard_M16_EEPS)
class W26():
    # 'Dashboard_M16_EEPS'!W26
    value = 190852
    formula = "='Input RPS'!W116"
    @eval_fn
    def W26():
        w116_1 = Input_RPS.W116()
        return w116_1

@register(Dashboard_M16_EEPS)
class X26():
    # 'Dashboard_M16_EEPS'!X26
    value = 0
    formula = "='Input RPS'!X116"
    @eval_fn
    def X26():
        x116_1 = Input_RPS.X116()
        return x116_1

@register(Dashboard_M16_EEPS)
class Y26():
    # 'Dashboard_M16_EEPS'!Y26
    value = 0
    formula = "='Input RPS'!Y116"
    @eval_fn
    def Y26():
        y116_1 = Input_RPS.Y116()
        return y116_1

@register(Dashboard_M16_EEPS)
class Z26():
    # 'Dashboard_M16_EEPS'!Z26
    value = 0
    formula = "='Input RPS'!Z116"
    @eval_fn
    def Z26():
        z116_1 = Input_RPS.Z116()
        return z116_1

@register(Dashboard_M16_EEPS)
class AA26():
    # 'Dashboard_M16_EEPS'!AA26
    value = 0
    formula = "='Input RPS'!AA116"
    @eval_fn
    def AA26():
        aa116_1 = Input_RPS.AA116()
        return aa116_1

@register(Dashboard_M16_EEPS)
class AB26():
    # 'Dashboard_M16_EEPS'!AB26
    value = 0
    formula = "='Input RPS'!AB116"
    @eval_fn
    def AB26():
        ab116_1 = Input_RPS.AB116()
        return ab116_1

@register(Dashboard_M16_EEPS)
class AC26():
    # 'Dashboard_M16_EEPS'!AC26
    value = 0
    formula = "='Input RPS'!AC116"
    @eval_fn
    def AC26():
        ac116_1 = Input_RPS.AC116()
        return ac116_1

@register(Dashboard_M16_EEPS)
class AD26():
    # 'Dashboard_M16_EEPS'!AD26
    value = 0
    formula = "='Input RPS'!AD116"
    @eval_fn
    def AD26():
        ad116_1 = Input_RPS.AD116()
        return ad116_1

@register(Dashboard_M16_EEPS)
class AE26():
    # 'Dashboard_M16_EEPS'!AE26
    value = 0
    formula = "='Input RPS'!AE116"
    @eval_fn
    def AE26():
        ae116_1 = Input_RPS.AE116()
        return ae116_1

@register(Dashboard_M16_EEPS)
class AF26():
    # 'Dashboard_M16_EEPS'!AF26
    value = 0
    formula = "='Input RPS'!AF116"
    @eval_fn
    def AF26():
        af116_1 = Input_RPS.AF116()
        return af116_1

@register(Dashboard_M16_EEPS)
class AG26():
    # 'Dashboard_M16_EEPS'!AG26
    value = 0
    formula = "='Input RPS'!AG116"
    @eval_fn
    def AG26():
        ag116_1 = Input_RPS.AG116()
        return ag116_1

@register(Dashboard_M16_EEPS)
class AH26():
    # 'Dashboard_M16_EEPS'!AH26
    value = 0
    formula = "='Input RPS'!AH116"
    @eval_fn
    def AH26():
        ah116_1 = Input_RPS.AH116()
        return ah116_1

@register(Dashboard_M16_EEPS)
class AI26():
    # 'Dashboard_M16_EEPS'!AI26
    value = 0
    formula = "='Input RPS'!AI116"
    @eval_fn
    def AI26():
        ai116_1 = Input_RPS.AI116()
        return ai116_1

@register(Dashboard_M16_EEPS)
class AJ26():
    # 'Dashboard_M16_EEPS'!AJ26
    value = 0
    formula = "='Input RPS'!AJ116"
    @eval_fn
    def AJ26():
        aj116_1 = Input_RPS.AJ116()
        return aj116_1

@register(Dashboard_M16_EEPS)
class AK26():
    # 'Dashboard_M16_EEPS'!AK26
    value = 0
    formula = "='Input RPS'!AK116"
    @eval_fn
    def AK26():
        ak116_1 = Input_RPS.AK116()
        return ak116_1

@register(Dashboard_M16_EEPS)
class AL26():
    # 'Dashboard_M16_EEPS'!AL26
    value = 0
    formula = "='Input RPS'!AL116"
    @eval_fn
    def AL26():
        al116_1 = Input_RPS.AL116()
        return al116_1

@register(Dashboard_M16_EEPS)
class C27():
    # 'Dashboard_M16_EEPS'!C27
    value = "KIUC"

@register(Dashboard_M16_EEPS)
class D27():
    # 'Dashboard_M16_EEPS'!D27
    value = "MWh"

@register(Dashboard_M16_EEPS)
class C28():
    # 'Dashboard_M16_EEPS'!C28
    value = "  Displacement Tech: Solar Water Heating"

@register(Dashboard_M16_EEPS)
class G28():
    # 'Dashboard_M16_EEPS'!G28
    value = 0
    formula = "='Input RPS'!G119"
    @eval_fn
    def G28():
        g119_1 = Input_RPS.G119()
        return g119_1

@register(Dashboard_M16_EEPS)
class H28():
    # 'Dashboard_M16_EEPS'!H28
    value = 0
    formula = "='Input RPS'!H119"
    @eval_fn
    def H28():
        h119_1 = Input_RPS.H119()
        return h119_1

@register(Dashboard_M16_EEPS)
class I28():
    # 'Dashboard_M16_EEPS'!I28
    value = 0
    formula = "='Input RPS'!I119"
    @eval_fn
    def I28():
        i119_1 = Input_RPS.I119()
        return i119_1

@register(Dashboard_M16_EEPS)
class J28():
    # 'Dashboard_M16_EEPS'!J28
    value = 0
    formula = "='Input RPS'!J119"
    @eval_fn
    def J28():
        j119_1 = Input_RPS.J119()
        return j119_1

@register(Dashboard_M16_EEPS)
class K28():
    # 'Dashboard_M16_EEPS'!K28
    value = 7387
    formula = "='Input RPS'!K119"
    @eval_fn
    def K28():
        k119_1 = Input_RPS.K119()
        return k119_1

@register(Dashboard_M16_EEPS)
class L28():
    # 'Dashboard_M16_EEPS'!L28
    value = 7558
    formula = "='Input RPS'!L119"
    @eval_fn
    def L28():
        l119_1 = Input_RPS.L119()
        return l119_1

@register(Dashboard_M16_EEPS)
class M28():
    # 'Dashboard_M16_EEPS'!M28
    value = 7659
    formula = "='Input RPS'!M119"
    @eval_fn
    def M28():
        m119_1 = Input_RPS.M119()
        return m119_1

@register(Dashboard_M16_EEPS)
class N28():
    # 'Dashboard_M16_EEPS'!N28
    value = 7831
    formula = "='Input RPS'!N119"
    @eval_fn
    def N28():
        n119_1 = Input_RPS.N119()
        return n119_1

@register(Dashboard_M16_EEPS)
class O28():
    # 'Dashboard_M16_EEPS'!O28
    value = 7937
    formula = "='Input RPS'!O119"
    @eval_fn
    def O28():
        o119_1 = Input_RPS.O119()
        return o119_1

@register(Dashboard_M16_EEPS)
class P28():
    # 'Dashboard_M16_EEPS'!P28
    value = 0
    formula = "='Input RPS'!P119"
    @eval_fn
    def P28():
        p119_1 = Input_RPS.P119()
        return p119_1

@register(Dashboard_M16_EEPS)
class Q28():
    # 'Dashboard_M16_EEPS'!Q28
    value = 0
    formula = "='Input RPS'!Q119"
    @eval_fn
    def Q28():
        q119_1 = Input_RPS.Q119()
        return q119_1

@register(Dashboard_M16_EEPS)
class R28():
    # 'Dashboard_M16_EEPS'!R28
    value = 0
    formula = "='Input RPS'!R119"
    @eval_fn
    def R28():
        r119_1 = Input_RPS.R119()
        return r119_1

@register(Dashboard_M16_EEPS)
class S28():
    # 'Dashboard_M16_EEPS'!S28
    value = 0
    formula = "='Input RPS'!S119"
    @eval_fn
    def S28():
        s119_1 = Input_RPS.S119()
        return s119_1

@register(Dashboard_M16_EEPS)
class T28():
    # 'Dashboard_M16_EEPS'!T28
    value = 0
    formula = "='Input RPS'!T119"
    @eval_fn
    def T28():
        t119_1 = Input_RPS.T119()
        return t119_1

@register(Dashboard_M16_EEPS)
class U28():
    # 'Dashboard_M16_EEPS'!U28
    value = 0
    formula = "='Input RPS'!U119"
    @eval_fn
    def U28():
        u119_1 = Input_RPS.U119()
        return u119_1

@register(Dashboard_M16_EEPS)
class V28():
    # 'Dashboard_M16_EEPS'!V28
    value = 0
    formula = "='Input RPS'!V119"
    @eval_fn
    def V28():
        v119_1 = Input_RPS.V119()
        return v119_1

@register(Dashboard_M16_EEPS)
class W28():
    # 'Dashboard_M16_EEPS'!W28
    value = 0
    formula = "='Input RPS'!W119"
    @eval_fn
    def W28():
        w119_1 = Input_RPS.W119()
        return w119_1

@register(Dashboard_M16_EEPS)
class X28():
    # 'Dashboard_M16_EEPS'!X28
    value = 0
    formula = "='Input RPS'!X119"
    @eval_fn
    def X28():
        x119_1 = Input_RPS.X119()
        return x119_1

@register(Dashboard_M16_EEPS)
class Y28():
    # 'Dashboard_M16_EEPS'!Y28
    value = 0
    formula = "='Input RPS'!Y119"
    @eval_fn
    def Y28():
        y119_1 = Input_RPS.Y119()
        return y119_1

@register(Dashboard_M16_EEPS)
class Z28():
    # 'Dashboard_M16_EEPS'!Z28
    value = 0
    formula = "='Input RPS'!Z119"
    @eval_fn
    def Z28():
        z119_1 = Input_RPS.Z119()
        return z119_1

@register(Dashboard_M16_EEPS)
class AA28():
    # 'Dashboard_M16_EEPS'!AA28
    value = 0
    formula = "='Input RPS'!AA119"
    @eval_fn
    def AA28():
        aa119_1 = Input_RPS.AA119()
        return aa119_1

@register(Dashboard_M16_EEPS)
class AB28():
    # 'Dashboard_M16_EEPS'!AB28
    value = 0
    formula = "='Input RPS'!AB119"
    @eval_fn
    def AB28():
        ab119_1 = Input_RPS.AB119()
        return ab119_1

@register(Dashboard_M16_EEPS)
class AC28():
    # 'Dashboard_M16_EEPS'!AC28
    value = 0
    formula = "='Input RPS'!AC119"
    @eval_fn
    def AC28():
        ac119_1 = Input_RPS.AC119()
        return ac119_1

@register(Dashboard_M16_EEPS)
class AD28():
    # 'Dashboard_M16_EEPS'!AD28
    value = 0
    formula = "='Input RPS'!AD119"
    @eval_fn
    def AD28():
        ad119_1 = Input_RPS.AD119()
        return ad119_1

@register(Dashboard_M16_EEPS)
class AE28():
    # 'Dashboard_M16_EEPS'!AE28
    value = 0
    formula = "='Input RPS'!AE119"
    @eval_fn
    def AE28():
        ae119_1 = Input_RPS.AE119()
        return ae119_1

@register(Dashboard_M16_EEPS)
class AF28():
    # 'Dashboard_M16_EEPS'!AF28
    value = 0
    formula = "='Input RPS'!AF119"
    @eval_fn
    def AF28():
        af119_1 = Input_RPS.AF119()
        return af119_1

@register(Dashboard_M16_EEPS)
class AG28():
    # 'Dashboard_M16_EEPS'!AG28
    value = 0
    formula = "='Input RPS'!AG119"
    @eval_fn
    def AG28():
        ag119_1 = Input_RPS.AG119()
        return ag119_1

@register(Dashboard_M16_EEPS)
class AH28():
    # 'Dashboard_M16_EEPS'!AH28
    value = 0
    formula = "='Input RPS'!AH119"
    @eval_fn
    def AH28():
        ah119_1 = Input_RPS.AH119()
        return ah119_1

@register(Dashboard_M16_EEPS)
class AI28():
    # 'Dashboard_M16_EEPS'!AI28
    value = 0
    formula = "='Input RPS'!AI119"
    @eval_fn
    def AI28():
        ai119_1 = Input_RPS.AI119()
        return ai119_1

@register(Dashboard_M16_EEPS)
class AJ28():
    # 'Dashboard_M16_EEPS'!AJ28
    value = 0
    formula = "='Input RPS'!AJ119"
    @eval_fn
    def AJ28():
        aj119_1 = Input_RPS.AJ119()
        return aj119_1

@register(Dashboard_M16_EEPS)
class AK28():
    # 'Dashboard_M16_EEPS'!AK28
    value = 0
    formula = "='Input RPS'!AK119"
    @eval_fn
    def AK28():
        ak119_1 = Input_RPS.AK119()
        return ak119_1

@register(Dashboard_M16_EEPS)
class AL28():
    # 'Dashboard_M16_EEPS'!AL28
    value = 0
    formula = "='Input RPS'!AL119"
    @eval_fn
    def AL28():
        al119_1 = Input_RPS.AL119()
        return al119_1

@register(Dashboard_M16_EEPS)
class C29():
    # 'Dashboard_M16_EEPS'!C29
    value = "  Energy Efficiency Technologies"

@register(Dashboard_M16_EEPS)
class G29():
    # 'Dashboard_M16_EEPS'!G29
    value = 0
    formula = "='Input RPS'!G121"
    @eval_fn
    def G29():
        g121_1 = Input_RPS.G121()
        return g121_1

@register(Dashboard_M16_EEPS)
class H29():
    # 'Dashboard_M16_EEPS'!H29
    value = 0
    formula = "='Input RPS'!H121"
    @eval_fn
    def H29():
        h121_1 = Input_RPS.H121()
        return h121_1

@register(Dashboard_M16_EEPS)
class I29():
    # 'Dashboard_M16_EEPS'!I29
    value = 0
    formula = "='Input RPS'!I121"
    @eval_fn
    def I29():
        i121_1 = Input_RPS.I121()
        return i121_1

@register(Dashboard_M16_EEPS)
class J29():
    # 'Dashboard_M16_EEPS'!J29
    value = 0
    formula = "='Input RPS'!J121"
    @eval_fn
    def J29():
        j121_1 = Input_RPS.J121()
        return j121_1

@register(Dashboard_M16_EEPS)
class K29():
    # 'Dashboard_M16_EEPS'!K29
    value = 0
    formula = "='Input RPS'!K121"
    @eval_fn
    def K29():
        k121_1 = Input_RPS.K121()
        return k121_1

@register(Dashboard_M16_EEPS)
class L29():
    # 'Dashboard_M16_EEPS'!L29
    value = 19037
    formula = "='Input RPS'!L121"
    @eval_fn
    def L29():
        l121_1 = Input_RPS.L121()
        return l121_1

@register(Dashboard_M16_EEPS)
class M29():
    # 'Dashboard_M16_EEPS'!M29
    value = 20855
    formula = "='Input RPS'!M121"
    @eval_fn
    def M29():
        m121_1 = Input_RPS.M121()
        return m121_1

@register(Dashboard_M16_EEPS)
class N29():
    # 'Dashboard_M16_EEPS'!N29
    value = 21349
    formula = "='Input RPS'!N121"
    @eval_fn
    def N29():
        n121_1 = Input_RPS.N121()
        return n121_1

@register(Dashboard_M16_EEPS)
class O29():
    # 'Dashboard_M16_EEPS'!O29
    value = 21361
    formula = "='Input RPS'!O121"
    @eval_fn
    def O29():
        o121_1 = Input_RPS.O121()
        return o121_1

@register(Dashboard_M16_EEPS)
class P29():
    # 'Dashboard_M16_EEPS'!P29
    value = 19233
    formula = "='Input RPS'!P121"
    @eval_fn
    def P29():
        p121_1 = Input_RPS.P121()
        return p121_1

@register(Dashboard_M16_EEPS)
class Q29():
    # 'Dashboard_M16_EEPS'!Q29
    value = 19217
    formula = "='Input RPS'!Q121"
    @eval_fn
    def Q29():
        q121_1 = Input_RPS.Q121()
        return q121_1

@register(Dashboard_M16_EEPS)
class R29():
    # 'Dashboard_M16_EEPS'!R29
    value = 16911
    formula = "='Input RPS'!R121"
    @eval_fn
    def R29():
        r121_1 = Input_RPS.R121()
        return r121_1

@register(Dashboard_M16_EEPS)
class S29():
    # 'Dashboard_M16_EEPS'!S29
    value = 18264
    formula = "='Input RPS'!S121"
    @eval_fn
    def S29():
        s121_1 = Input_RPS.S121()
        return s121_1

@register(Dashboard_M16_EEPS)
class T29():
    # 'Dashboard_M16_EEPS'!T29
    value = 24368
    formula = "='Input RPS'!T121"
    @eval_fn
    def T29():
        t121_1 = Input_RPS.T121()
        return t121_1

@register(Dashboard_M16_EEPS)
class U29():
    # 'Dashboard_M16_EEPS'!U29
    value = 22441
    formula = "='Input RPS'!U121"
    @eval_fn
    def U29():
        u121_1 = Input_RPS.U121()
        return u121_1

@register(Dashboard_M16_EEPS)
class V29():
    # 'Dashboard_M16_EEPS'!V29
    value = 21370
    formula = "='Input RPS'!V121"
    @eval_fn
    def V29():
        v121_1 = Input_RPS.V121()
        return v121_1

@register(Dashboard_M16_EEPS)
class W29():
    # 'Dashboard_M16_EEPS'!W29
    value = 19947
    formula = "='Input RPS'!W121"
    @eval_fn
    def W29():
        w121_1 = Input_RPS.W121()
        return w121_1

@register(Dashboard_M16_EEPS)
class X29():
    # 'Dashboard_M16_EEPS'!X29
    value = 0
    formula = "='Input RPS'!X121"
    @eval_fn
    def X29():
        x121_1 = Input_RPS.X121()
        return x121_1

@register(Dashboard_M16_EEPS)
class Y29():
    # 'Dashboard_M16_EEPS'!Y29
    value = 0
    formula = "='Input RPS'!Y121"
    @eval_fn
    def Y29():
        y121_1 = Input_RPS.Y121()
        return y121_1

@register(Dashboard_M16_EEPS)
class Z29():
    # 'Dashboard_M16_EEPS'!Z29
    value = 0
    formula = "='Input RPS'!Z121"
    @eval_fn
    def Z29():
        z121_1 = Input_RPS.Z121()
        return z121_1

@register(Dashboard_M16_EEPS)
class AA29():
    # 'Dashboard_M16_EEPS'!AA29
    value = 0
    formula = "='Input RPS'!AA121"
    @eval_fn
    def AA29():
        aa121_1 = Input_RPS.AA121()
        return aa121_1

@register(Dashboard_M16_EEPS)
class AB29():
    # 'Dashboard_M16_EEPS'!AB29
    value = 0
    formula = "='Input RPS'!AB121"
    @eval_fn
    def AB29():
        ab121_1 = Input_RPS.AB121()
        return ab121_1

@register(Dashboard_M16_EEPS)
class AC29():
    # 'Dashboard_M16_EEPS'!AC29
    value = 0
    formula = "='Input RPS'!AC121"
    @eval_fn
    def AC29():
        ac121_1 = Input_RPS.AC121()
        return ac121_1

@register(Dashboard_M16_EEPS)
class AD29():
    # 'Dashboard_M16_EEPS'!AD29
    value = 0
    formula = "='Input RPS'!AD121"
    @eval_fn
    def AD29():
        ad121_1 = Input_RPS.AD121()
        return ad121_1

@register(Dashboard_M16_EEPS)
class AE29():
    # 'Dashboard_M16_EEPS'!AE29
    value = 0
    formula = "='Input RPS'!AE121"
    @eval_fn
    def AE29():
        ae121_1 = Input_RPS.AE121()
        return ae121_1

@register(Dashboard_M16_EEPS)
class AF29():
    # 'Dashboard_M16_EEPS'!AF29
    value = 0
    formula = "='Input RPS'!AF121"
    @eval_fn
    def AF29():
        af121_1 = Input_RPS.AF121()
        return af121_1

@register(Dashboard_M16_EEPS)
class AG29():
    # 'Dashboard_M16_EEPS'!AG29
    value = 0
    formula = "='Input RPS'!AG121"
    @eval_fn
    def AG29():
        ag121_1 = Input_RPS.AG121()
        return ag121_1

@register(Dashboard_M16_EEPS)
class AH29():
    # 'Dashboard_M16_EEPS'!AH29
    value = 0
    formula = "='Input RPS'!AH121"
    @eval_fn
    def AH29():
        ah121_1 = Input_RPS.AH121()
        return ah121_1

@register(Dashboard_M16_EEPS)
class AI29():
    # 'Dashboard_M16_EEPS'!AI29
    value = 0
    formula = "='Input RPS'!AI121"
    @eval_fn
    def AI29():
        ai121_1 = Input_RPS.AI121()
        return ai121_1

@register(Dashboard_M16_EEPS)
class AJ29():
    # 'Dashboard_M16_EEPS'!AJ29
    value = 0
    formula = "='Input RPS'!AJ121"
    @eval_fn
    def AJ29():
        aj121_1 = Input_RPS.AJ121()
        return aj121_1

@register(Dashboard_M16_EEPS)
class AK29():
    # 'Dashboard_M16_EEPS'!AK29
    value = 0
    formula = "='Input RPS'!AK121"
    @eval_fn
    def AK29():
        ak121_1 = Input_RPS.AK121()
        return ak121_1

@register(Dashboard_M16_EEPS)
class AL29():
    # 'Dashboard_M16_EEPS'!AL29
    value = 0
    formula = "='Input RPS'!AL121"
    @eval_fn
    def AL29():
        al121_1 = Input_RPS.AL121()
        return al121_1

@register(Dashboard_M16_EEPS)
class A30():
    # 'Dashboard_M16_EEPS'!A30
    value = "Total EEKIUC"
    formula = "=C30&C27"
    @eval_fn
    def A30():
        c30_1 = Dashboard_M16_EEPS.C30()
        c27_1 = Dashboard_M16_EEPS.C27()
        var_1 = concat(c30_1, c27_1)
        return var_1

@register(Dashboard_M16_EEPS)
class C30():
    # 'Dashboard_M16_EEPS'!C30
    value = "Total EE"

@register(Dashboard_M16_EEPS)
class G30():
    # 'Dashboard_M16_EEPS'!G30
    value = 0
    formula = "='Input RPS'!G122"
    @eval_fn
    def G30():
        g122_1 = Input_RPS.G122()
        return g122_1

@register(Dashboard_M16_EEPS)
class H30():
    # 'Dashboard_M16_EEPS'!H30
    value = 0
    formula = "='Input RPS'!H122"
    @eval_fn
    def H30():
        h122_1 = Input_RPS.H122()
        return h122_1

@register(Dashboard_M16_EEPS)
class I30():
    # 'Dashboard_M16_EEPS'!I30
    value = 0
    formula = "='Input RPS'!I122"
    @eval_fn
    def I30():
        i122_1 = Input_RPS.I122()
        return i122_1

@register(Dashboard_M16_EEPS)
class J30():
    # 'Dashboard_M16_EEPS'!J30
    value = 0
    formula = "='Input RPS'!J122"
    @eval_fn
    def J30():
        j122_1 = Input_RPS.J122()
        return j122_1

@register(Dashboard_M16_EEPS)
class K30():
    # 'Dashboard_M16_EEPS'!K30
    value = 7387
    formula = "='Input RPS'!K122"
    @eval_fn
    def K30():
        k122_1 = Input_RPS.K122()
        return k122_1

@register(Dashboard_M16_EEPS)
class L30():
    # 'Dashboard_M16_EEPS'!L30
    value = 26595
    formula = "='Input RPS'!L122"
    @eval_fn
    def L30():
        l122_1 = Input_RPS.L122()
        return l122_1

@register(Dashboard_M16_EEPS)
class M30():
    # 'Dashboard_M16_EEPS'!M30
    value = 28514
    formula = "='Input RPS'!M122"
    @eval_fn
    def M30():
        m122_1 = Input_RPS.M122()
        return m122_1

@register(Dashboard_M16_EEPS)
class N30():
    # 'Dashboard_M16_EEPS'!N30
    value = 29180
    formula = "='Input RPS'!N122"
    @eval_fn
    def N30():
        n122_1 = Input_RPS.N122()
        return n122_1

@register(Dashboard_M16_EEPS)
class O30():
    # 'Dashboard_M16_EEPS'!O30
    value = 29298
    formula = "='Input RPS'!O122"
    @eval_fn
    def O30():
        o122_1 = Input_RPS.O122()
        return o122_1

@register(Dashboard_M16_EEPS)
class P30():
    # 'Dashboard_M16_EEPS'!P30
    value = 19233
    formula = "='Input RPS'!P122"
    @eval_fn
    def P30():
        p122_1 = Input_RPS.P122()
        return p122_1

@register(Dashboard_M16_EEPS)
class Q30():
    # 'Dashboard_M16_EEPS'!Q30
    value = 19217
    formula = "='Input RPS'!Q122"
    @eval_fn
    def Q30():
        q122_1 = Input_RPS.Q122()
        return q122_1

@register(Dashboard_M16_EEPS)
class R30():
    # 'Dashboard_M16_EEPS'!R30
    value = 16911
    formula = "='Input RPS'!R122"
    @eval_fn
    def R30():
        r122_1 = Input_RPS.R122()
        return r122_1

@register(Dashboard_M16_EEPS)
class S30():
    # 'Dashboard_M16_EEPS'!S30
    value = 18264
    formula = "='Input RPS'!S122"
    @eval_fn
    def S30():
        s122_1 = Input_RPS.S122()
        return s122_1

@register(Dashboard_M16_EEPS)
class T30():
    # 'Dashboard_M16_EEPS'!T30
    value = 24368
    formula = "='Input RPS'!T122"
    @eval_fn
    def T30():
        t122_1 = Input_RPS.T122()
        return t122_1

@register(Dashboard_M16_EEPS)
class U30():
    # 'Dashboard_M16_EEPS'!U30
    value = 22441
    formula = "='Input RPS'!U122"
    @eval_fn
    def U30():
        u122_1 = Input_RPS.U122()
        return u122_1

@register(Dashboard_M16_EEPS)
class V30():
    # 'Dashboard_M16_EEPS'!V30
    value = 21370
    formula = "='Input RPS'!V122"
    @eval_fn
    def V30():
        v122_1 = Input_RPS.V122()
        return v122_1

@register(Dashboard_M16_EEPS)
class W30():
    # 'Dashboard_M16_EEPS'!W30
    value = 19947
    formula = "='Input RPS'!W122"
    @eval_fn
    def W30():
        w122_1 = Input_RPS.W122()
        return w122_1

@register(Dashboard_M16_EEPS)
class X30():
    # 'Dashboard_M16_EEPS'!X30
    value = 0
    formula = "='Input RPS'!X122"
    @eval_fn
    def X30():
        x122_1 = Input_RPS.X122()
        return x122_1

@register(Dashboard_M16_EEPS)
class Y30():
    # 'Dashboard_M16_EEPS'!Y30
    value = 0
    formula = "='Input RPS'!Y122"
    @eval_fn
    def Y30():
        y122_1 = Input_RPS.Y122()
        return y122_1

@register(Dashboard_M16_EEPS)
class Z30():
    # 'Dashboard_M16_EEPS'!Z30
    value = 0
    formula = "='Input RPS'!Z122"
    @eval_fn
    def Z30():
        z122_1 = Input_RPS.Z122()
        return z122_1

@register(Dashboard_M16_EEPS)
class AA30():
    # 'Dashboard_M16_EEPS'!AA30
    value = 0
    formula = "='Input RPS'!AA122"
    @eval_fn
    def AA30():
        aa122_1 = Input_RPS.AA122()
        return aa122_1

@register(Dashboard_M16_EEPS)
class AB30():
    # 'Dashboard_M16_EEPS'!AB30
    value = 0
    formula = "='Input RPS'!AB122"
    @eval_fn
    def AB30():
        ab122_1 = Input_RPS.AB122()
        return ab122_1

@register(Dashboard_M16_EEPS)
class AC30():
    # 'Dashboard_M16_EEPS'!AC30
    value = 0
    formula = "='Input RPS'!AC122"
    @eval_fn
    def AC30():
        ac122_1 = Input_RPS.AC122()
        return ac122_1

@register(Dashboard_M16_EEPS)
class AD30():
    # 'Dashboard_M16_EEPS'!AD30
    value = 0
    formula = "='Input RPS'!AD122"
    @eval_fn
    def AD30():
        ad122_1 = Input_RPS.AD122()
        return ad122_1

@register(Dashboard_M16_EEPS)
class AE30():
    # 'Dashboard_M16_EEPS'!AE30
    value = 0
    formula = "='Input RPS'!AE122"
    @eval_fn
    def AE30():
        ae122_1 = Input_RPS.AE122()
        return ae122_1

@register(Dashboard_M16_EEPS)
class AF30():
    # 'Dashboard_M16_EEPS'!AF30
    value = 0
    formula = "='Input RPS'!AF122"
    @eval_fn
    def AF30():
        af122_1 = Input_RPS.AF122()
        return af122_1

@register(Dashboard_M16_EEPS)
class AG30():
    # 'Dashboard_M16_EEPS'!AG30
    value = 0
    formula = "='Input RPS'!AG122"
    @eval_fn
    def AG30():
        ag122_1 = Input_RPS.AG122()
        return ag122_1

@register(Dashboard_M16_EEPS)
class AH30():
    # 'Dashboard_M16_EEPS'!AH30
    value = 0
    formula = "='Input RPS'!AH122"
    @eval_fn
    def AH30():
        ah122_1 = Input_RPS.AH122()
        return ah122_1

@register(Dashboard_M16_EEPS)
class AI30():
    # 'Dashboard_M16_EEPS'!AI30
    value = 0
    formula = "='Input RPS'!AI122"
    @eval_fn
    def AI30():
        ai122_1 = Input_RPS.AI122()
        return ai122_1

@register(Dashboard_M16_EEPS)
class AJ30():
    # 'Dashboard_M16_EEPS'!AJ30
    value = 0
    formula = "='Input RPS'!AJ122"
    @eval_fn
    def AJ30():
        aj122_1 = Input_RPS.AJ122()
        return aj122_1

@register(Dashboard_M16_EEPS)
class AK30():
    # 'Dashboard_M16_EEPS'!AK30
    value = 0
    formula = "='Input RPS'!AK122"
    @eval_fn
    def AK30():
        ak122_1 = Input_RPS.AK122()
        return ak122_1

@register(Dashboard_M16_EEPS)
class AL30():
    # 'Dashboard_M16_EEPS'!AL30
    value = 0
    formula = "='Input RPS'!AL122"
    @eval_fn
    def AL30():
        al122_1 = Input_RPS.AL122()
        return al122_1

@register(Dashboard_M16_EEPS)
class C31():
    # 'Dashboard_M16_EEPS'!C31
    value = "All Utilities"

@register(Dashboard_M16_EEPS)
class D31():
    # 'Dashboard_M16_EEPS'!D31
    value = "MWh"

@register(Dashboard_M16_EEPS)
class C32():
    # 'Dashboard_M16_EEPS'!C32
    value = "  Displacement Tech: Solar Water Heating"

@register(Dashboard_M16_EEPS)
class G32():
    # 'Dashboard_M16_EEPS'!G32
    value = 0
    formula = "=G28+G24+G20+G16"
    @eval_fn
    def G32():
        g28_1 = Dashboard_M16_EEPS.G28()
        g24_1 = Dashboard_M16_EEPS.G24()
        var_1 = add(g28_1, g24_1)
        g20_1 = Dashboard_M16_EEPS.G20()
        var_2 = add(var_1, g20_1)
        g16_1 = Dashboard_M16_EEPS.G16()
        var_3 = add(var_2, g16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class H32():
    # 'Dashboard_M16_EEPS'!H32
    value = 0
    formula = "=H28+H24+H20+H16"
    @eval_fn
    def H32():
        h28_1 = Dashboard_M16_EEPS.H28()
        h24_1 = Dashboard_M16_EEPS.H24()
        var_1 = add(h28_1, h24_1)
        h20_1 = Dashboard_M16_EEPS.H20()
        var_2 = add(var_1, h20_1)
        h16_1 = Dashboard_M16_EEPS.H16()
        var_3 = add(var_2, h16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class I32():
    # 'Dashboard_M16_EEPS'!I32
    value = 0
    formula = "=I28+I24+I20+I16"
    @eval_fn
    def I32():
        i28_1 = Dashboard_M16_EEPS.I28()
        i24_1 = Dashboard_M16_EEPS.I24()
        var_1 = add(i28_1, i24_1)
        i20_1 = Dashboard_M16_EEPS.I20()
        var_2 = add(var_1, i20_1)
        i16_1 = Dashboard_M16_EEPS.I16()
        var_3 = add(var_2, i16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class J32():
    # 'Dashboard_M16_EEPS'!J32
    value = 0
    formula = "=J28+J24+J20+J16"
    @eval_fn
    def J32():
        j28_1 = Dashboard_M16_EEPS.J28()
        j24_1 = Dashboard_M16_EEPS.J24()
        var_1 = add(j28_1, j24_1)
        j20_1 = Dashboard_M16_EEPS.J20()
        var_2 = add(var_1, j20_1)
        j16_1 = Dashboard_M16_EEPS.J16()
        var_3 = add(var_2, j16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class K32():
    # 'Dashboard_M16_EEPS'!K32
    value = 7387
    formula = "=K28+K24+K20+K16"
    @eval_fn
    def K32():
        k28_1 = Dashboard_M16_EEPS.K28()
        k24_1 = Dashboard_M16_EEPS.K24()
        var_1 = add(k28_1, k24_1)
        k20_1 = Dashboard_M16_EEPS.K20()
        var_2 = add(var_1, k20_1)
        k16_1 = Dashboard_M16_EEPS.K16()
        var_3 = add(var_2, k16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class L32():
    # 'Dashboard_M16_EEPS'!L32
    value = 7558
    formula = "=L28+L24+L20+L16"
    @eval_fn
    def L32():
        l28_1 = Dashboard_M16_EEPS.L28()
        l24_1 = Dashboard_M16_EEPS.L24()
        var_1 = add(l28_1, l24_1)
        l20_1 = Dashboard_M16_EEPS.L20()
        var_2 = add(var_1, l20_1)
        l16_1 = Dashboard_M16_EEPS.L16()
        var_3 = add(var_2, l16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class M32():
    # 'Dashboard_M16_EEPS'!M32
    value = 91659
    formula = "=M28+M24+M20+M16"
    @eval_fn
    def M32():
        m28_1 = Dashboard_M16_EEPS.M28()
        m24_1 = Dashboard_M16_EEPS.M24()
        var_1 = add(m28_1, m24_1)
        m20_1 = Dashboard_M16_EEPS.M20()
        var_2 = add(var_1, m20_1)
        m16_1 = Dashboard_M16_EEPS.M16()
        var_3 = add(var_2, m16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class N32():
    # 'Dashboard_M16_EEPS'!N32
    value = 102831
    formula = "=N28+N24+N20+N16"
    @eval_fn
    def N32():
        n28_1 = Dashboard_M16_EEPS.N28()
        n24_1 = Dashboard_M16_EEPS.N24()
        var_1 = add(n28_1, n24_1)
        n20_1 = Dashboard_M16_EEPS.N20()
        var_2 = add(var_1, n20_1)
        n16_1 = Dashboard_M16_EEPS.N16()
        var_3 = add(var_2, n16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class O32():
    # 'Dashboard_M16_EEPS'!O32
    value = 116937
    formula = "=O28+O24+O20+O16"
    @eval_fn
    def O32():
        o28_1 = Dashboard_M16_EEPS.O28()
        o24_1 = Dashboard_M16_EEPS.O24()
        var_1 = add(o28_1, o24_1)
        o20_1 = Dashboard_M16_EEPS.O20()
        var_2 = add(var_1, o20_1)
        o16_1 = Dashboard_M16_EEPS.O16()
        var_3 = add(var_2, o16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class P32():
    # 'Dashboard_M16_EEPS'!P32
    value = 117279
    formula = "=P28+P24+P20+P16"
    @eval_fn
    def P32():
        p28_1 = Dashboard_M16_EEPS.P28()
        p24_1 = Dashboard_M16_EEPS.P24()
        var_1 = add(p28_1, p24_1)
        p20_1 = Dashboard_M16_EEPS.P20()
        var_2 = add(var_1, p20_1)
        p16_1 = Dashboard_M16_EEPS.P16()
        var_3 = add(var_2, p16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class Q32():
    # 'Dashboard_M16_EEPS'!Q32
    value = 129960
    formula = "=Q28+Q24+Q20+Q16"
    @eval_fn
    def Q32():
        q28_1 = Dashboard_M16_EEPS.Q28()
        q24_1 = Dashboard_M16_EEPS.Q24()
        var_1 = add(q28_1, q24_1)
        q20_1 = Dashboard_M16_EEPS.Q20()
        var_2 = add(var_1, q20_1)
        q16_1 = Dashboard_M16_EEPS.Q16()
        var_3 = add(var_2, q16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class R32():
    # 'Dashboard_M16_EEPS'!R32
    value = 172056
    formula = "=R28+R24+R20+R16"
    @eval_fn
    def R32():
        r28_1 = Dashboard_M16_EEPS.R28()
        r24_1 = Dashboard_M16_EEPS.R24()
        var_1 = add(r28_1, r24_1)
        r20_1 = Dashboard_M16_EEPS.R20()
        var_2 = add(var_1, r20_1)
        r16_1 = Dashboard_M16_EEPS.R16()
        var_3 = add(var_2, r16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class S32():
    # 'Dashboard_M16_EEPS'!S32
    value = 180173
    formula = "=S28+S24+S20+S16"
    @eval_fn
    def S32():
        s28_1 = Dashboard_M16_EEPS.S28()
        s24_1 = Dashboard_M16_EEPS.S24()
        var_1 = add(s28_1, s24_1)
        s20_1 = Dashboard_M16_EEPS.S20()
        var_2 = add(var_1, s20_1)
        s16_1 = Dashboard_M16_EEPS.S16()
        var_3 = add(var_2, s16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class T32():
    # 'Dashboard_M16_EEPS'!T32
    value = 159801
    formula = "=T28+T24+T20+T16"
    @eval_fn
    def T32():
        t28_1 = Dashboard_M16_EEPS.T28()
        t24_1 = Dashboard_M16_EEPS.T24()
        var_1 = add(t28_1, t24_1)
        t20_1 = Dashboard_M16_EEPS.T20()
        var_2 = add(var_1, t20_1)
        t16_1 = Dashboard_M16_EEPS.T16()
        var_3 = add(var_2, t16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class U32():
    # 'Dashboard_M16_EEPS'!U32
    value = 144449
    formula = "=U28+U24+U20+U16"
    @eval_fn
    def U32():
        u28_1 = Dashboard_M16_EEPS.U28()
        u24_1 = Dashboard_M16_EEPS.U24()
        var_1 = add(u28_1, u24_1)
        u20_1 = Dashboard_M16_EEPS.U20()
        var_2 = add(var_1, u20_1)
        u16_1 = Dashboard_M16_EEPS.U16()
        var_3 = add(var_2, u16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class V32():
    # 'Dashboard_M16_EEPS'!V32
    value = 126252
    formula = "=V28+V24+V20+V16"
    @eval_fn
    def V32():
        v28_1 = Dashboard_M16_EEPS.V28()
        v24_1 = Dashboard_M16_EEPS.V24()
        var_1 = add(v28_1, v24_1)
        v20_1 = Dashboard_M16_EEPS.V20()
        var_2 = add(var_1, v20_1)
        v16_1 = Dashboard_M16_EEPS.V16()
        var_3 = add(var_2, v16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class W32():
    # 'Dashboard_M16_EEPS'!W32
    value = 108055
    formula = "=W28+W24+W20+W16"
    @eval_fn
    def W32():
        w28_1 = Dashboard_M16_EEPS.W28()
        w24_1 = Dashboard_M16_EEPS.W24()
        var_1 = add(w28_1, w24_1)
        w20_1 = Dashboard_M16_EEPS.W20()
        var_2 = add(var_1, w20_1)
        w16_1 = Dashboard_M16_EEPS.W16()
        var_3 = add(var_2, w16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class X32():
    # 'Dashboard_M16_EEPS'!X32
    value = 0
    formula = "=X28+X24+X20+X16"
    @eval_fn
    def X32():
        x28_1 = Dashboard_M16_EEPS.X28()
        x24_1 = Dashboard_M16_EEPS.X24()
        var_1 = add(x28_1, x24_1)
        x20_1 = Dashboard_M16_EEPS.X20()
        var_2 = add(var_1, x20_1)
        x16_1 = Dashboard_M16_EEPS.X16()
        var_3 = add(var_2, x16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class Y32():
    # 'Dashboard_M16_EEPS'!Y32
    value = 0
    formula = "=Y28+Y24+Y20+Y16"
    @eval_fn
    def Y32():
        y28_1 = Dashboard_M16_EEPS.Y28()
        y24_1 = Dashboard_M16_EEPS.Y24()
        var_1 = add(y28_1, y24_1)
        y20_1 = Dashboard_M16_EEPS.Y20()
        var_2 = add(var_1, y20_1)
        y16_1 = Dashboard_M16_EEPS.Y16()
        var_3 = add(var_2, y16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class Z32():
    # 'Dashboard_M16_EEPS'!Z32
    value = 0
    formula = "=Z28+Z24+Z20+Z16"
    @eval_fn
    def Z32():
        z28_1 = Dashboard_M16_EEPS.Z28()
        z24_1 = Dashboard_M16_EEPS.Z24()
        var_1 = add(z28_1, z24_1)
        z20_1 = Dashboard_M16_EEPS.Z20()
        var_2 = add(var_1, z20_1)
        z16_1 = Dashboard_M16_EEPS.Z16()
        var_3 = add(var_2, z16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AA32():
    # 'Dashboard_M16_EEPS'!AA32
    value = 0
    formula = "=AA28+AA24+AA20+AA16"
    @eval_fn
    def AA32():
        aa28_1 = Dashboard_M16_EEPS.AA28()
        aa24_1 = Dashboard_M16_EEPS.AA24()
        var_1 = add(aa28_1, aa24_1)
        aa20_1 = Dashboard_M16_EEPS.AA20()
        var_2 = add(var_1, aa20_1)
        aa16_1 = Dashboard_M16_EEPS.AA16()
        var_3 = add(var_2, aa16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AB32():
    # 'Dashboard_M16_EEPS'!AB32
    value = 0
    formula = "=AB28+AB24+AB20+AB16"
    @eval_fn
    def AB32():
        ab28_1 = Dashboard_M16_EEPS.AB28()
        ab24_1 = Dashboard_M16_EEPS.AB24()
        var_1 = add(ab28_1, ab24_1)
        ab20_1 = Dashboard_M16_EEPS.AB20()
        var_2 = add(var_1, ab20_1)
        ab16_1 = Dashboard_M16_EEPS.AB16()
        var_3 = add(var_2, ab16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AC32():
    # 'Dashboard_M16_EEPS'!AC32
    value = 0
    formula = "=AC28+AC24+AC20+AC16"
    @eval_fn
    def AC32():
        ac28_1 = Dashboard_M16_EEPS.AC28()
        ac24_1 = Dashboard_M16_EEPS.AC24()
        var_1 = add(ac28_1, ac24_1)
        ac20_1 = Dashboard_M16_EEPS.AC20()
        var_2 = add(var_1, ac20_1)
        ac16_1 = Dashboard_M16_EEPS.AC16()
        var_3 = add(var_2, ac16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AD32():
    # 'Dashboard_M16_EEPS'!AD32
    value = 0
    formula = "=AD28+AD24+AD20+AD16"
    @eval_fn
    def AD32():
        ad28_1 = Dashboard_M16_EEPS.AD28()
        ad24_1 = Dashboard_M16_EEPS.AD24()
        var_1 = add(ad28_1, ad24_1)
        ad20_1 = Dashboard_M16_EEPS.AD20()
        var_2 = add(var_1, ad20_1)
        ad16_1 = Dashboard_M16_EEPS.AD16()
        var_3 = add(var_2, ad16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AE32():
    # 'Dashboard_M16_EEPS'!AE32
    value = 0
    formula = "=AE28+AE24+AE20+AE16"
    @eval_fn
    def AE32():
        ae28_1 = Dashboard_M16_EEPS.AE28()
        ae24_1 = Dashboard_M16_EEPS.AE24()
        var_1 = add(ae28_1, ae24_1)
        ae20_1 = Dashboard_M16_EEPS.AE20()
        var_2 = add(var_1, ae20_1)
        ae16_1 = Dashboard_M16_EEPS.AE16()
        var_3 = add(var_2, ae16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AF32():
    # 'Dashboard_M16_EEPS'!AF32
    value = 0
    formula = "=AF28+AF24+AF20+AF16"
    @eval_fn
    def AF32():
        af28_1 = Dashboard_M16_EEPS.AF28()
        af24_1 = Dashboard_M16_EEPS.AF24()
        var_1 = add(af28_1, af24_1)
        af20_1 = Dashboard_M16_EEPS.AF20()
        var_2 = add(var_1, af20_1)
        af16_1 = Dashboard_M16_EEPS.AF16()
        var_3 = add(var_2, af16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AG32():
    # 'Dashboard_M16_EEPS'!AG32
    value = 0
    formula = "=AG28+AG24+AG20+AG16"
    @eval_fn
    def AG32():
        ag28_1 = Dashboard_M16_EEPS.AG28()
        ag24_1 = Dashboard_M16_EEPS.AG24()
        var_1 = add(ag28_1, ag24_1)
        ag20_1 = Dashboard_M16_EEPS.AG20()
        var_2 = add(var_1, ag20_1)
        ag16_1 = Dashboard_M16_EEPS.AG16()
        var_3 = add(var_2, ag16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AH32():
    # 'Dashboard_M16_EEPS'!AH32
    value = 0
    formula = "=AH28+AH24+AH20+AH16"
    @eval_fn
    def AH32():
        ah28_1 = Dashboard_M16_EEPS.AH28()
        ah24_1 = Dashboard_M16_EEPS.AH24()
        var_1 = add(ah28_1, ah24_1)
        ah20_1 = Dashboard_M16_EEPS.AH20()
        var_2 = add(var_1, ah20_1)
        ah16_1 = Dashboard_M16_EEPS.AH16()
        var_3 = add(var_2, ah16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AI32():
    # 'Dashboard_M16_EEPS'!AI32
    value = 0
    formula = "=AI28+AI24+AI20+AI16"
    @eval_fn
    def AI32():
        ai28_1 = Dashboard_M16_EEPS.AI28()
        ai24_1 = Dashboard_M16_EEPS.AI24()
        var_1 = add(ai28_1, ai24_1)
        ai20_1 = Dashboard_M16_EEPS.AI20()
        var_2 = add(var_1, ai20_1)
        ai16_1 = Dashboard_M16_EEPS.AI16()
        var_3 = add(var_2, ai16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AJ32():
    # 'Dashboard_M16_EEPS'!AJ32
    value = 0
    formula = "=AJ28+AJ24+AJ20+AJ16"
    @eval_fn
    def AJ32():
        aj28_1 = Dashboard_M16_EEPS.AJ28()
        aj24_1 = Dashboard_M16_EEPS.AJ24()
        var_1 = add(aj28_1, aj24_1)
        aj20_1 = Dashboard_M16_EEPS.AJ20()
        var_2 = add(var_1, aj20_1)
        aj16_1 = Dashboard_M16_EEPS.AJ16()
        var_3 = add(var_2, aj16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AK32():
    # 'Dashboard_M16_EEPS'!AK32
    value = 0
    formula = "=AK28+AK24+AK20+AK16"
    @eval_fn
    def AK32():
        ak28_1 = Dashboard_M16_EEPS.AK28()
        ak24_1 = Dashboard_M16_EEPS.AK24()
        var_1 = add(ak28_1, ak24_1)
        ak20_1 = Dashboard_M16_EEPS.AK20()
        var_2 = add(var_1, ak20_1)
        ak16_1 = Dashboard_M16_EEPS.AK16()
        var_3 = add(var_2, ak16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AL32():
    # 'Dashboard_M16_EEPS'!AL32
    value = 0
    formula = "=AL28+AL24+AL20+AL16"
    @eval_fn
    def AL32():
        al28_1 = Dashboard_M16_EEPS.AL28()
        al24_1 = Dashboard_M16_EEPS.AL24()
        var_1 = add(al28_1, al24_1)
        al20_1 = Dashboard_M16_EEPS.AL20()
        var_2 = add(var_1, al20_1)
        al16_1 = Dashboard_M16_EEPS.AL16()
        var_3 = add(var_2, al16_1)
        return var_3

@register(Dashboard_M16_EEPS)
class C33():
    # 'Dashboard_M16_EEPS'!C33
    value = "  Energy Efficiency Technologies"

@register(Dashboard_M16_EEPS)
class G33():
    # 'Dashboard_M16_EEPS'!G33
    value = 0
    formula = "=G29+G25+G21+G17"
    @eval_fn
    def G33():
        g29_1 = Dashboard_M16_EEPS.G29()
        g25_1 = Dashboard_M16_EEPS.G25()
        var_1 = add(g29_1, g25_1)
        g21_1 = Dashboard_M16_EEPS.G21()
        var_2 = add(var_1, g21_1)
        g17_1 = Dashboard_M16_EEPS.G17()
        var_3 = add(var_2, g17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class H33():
    # 'Dashboard_M16_EEPS'!H33
    value = 0
    formula = "=H29+H25+H21+H17"
    @eval_fn
    def H33():
        h29_1 = Dashboard_M16_EEPS.H29()
        h25_1 = Dashboard_M16_EEPS.H25()
        var_1 = add(h29_1, h25_1)
        h21_1 = Dashboard_M16_EEPS.H21()
        var_2 = add(var_1, h21_1)
        h17_1 = Dashboard_M16_EEPS.H17()
        var_3 = add(var_2, h17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class I33():
    # 'Dashboard_M16_EEPS'!I33
    value = 0
    formula = "=I29+I25+I21+I17"
    @eval_fn
    def I33():
        i29_1 = Dashboard_M16_EEPS.I29()
        i25_1 = Dashboard_M16_EEPS.I25()
        var_1 = add(i29_1, i25_1)
        i21_1 = Dashboard_M16_EEPS.I21()
        var_2 = add(var_1, i21_1)
        i17_1 = Dashboard_M16_EEPS.I17()
        var_3 = add(var_2, i17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class J33():
    # 'Dashboard_M16_EEPS'!J33
    value = 0
    formula = "=J29+J25+J21+J17"
    @eval_fn
    def J33():
        j29_1 = Dashboard_M16_EEPS.J29()
        j25_1 = Dashboard_M16_EEPS.J25()
        var_1 = add(j29_1, j25_1)
        j21_1 = Dashboard_M16_EEPS.J21()
        var_2 = add(var_1, j21_1)
        j17_1 = Dashboard_M16_EEPS.J17()
        var_3 = add(var_2, j17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class K33():
    # 'Dashboard_M16_EEPS'!K33
    value = 0
    formula = "=K29+K25+K21+K17"
    @eval_fn
    def K33():
        k29_1 = Dashboard_M16_EEPS.K29()
        k25_1 = Dashboard_M16_EEPS.K25()
        var_1 = add(k29_1, k25_1)
        k21_1 = Dashboard_M16_EEPS.K21()
        var_2 = add(var_1, k21_1)
        k17_1 = Dashboard_M16_EEPS.K17()
        var_3 = add(var_2, k17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class L33():
    # 'Dashboard_M16_EEPS'!L33
    value = 19037
    formula = "=L29+L25+L21+L17"
    @eval_fn
    def L33():
        l29_1 = Dashboard_M16_EEPS.L29()
        l25_1 = Dashboard_M16_EEPS.L25()
        var_1 = add(l29_1, l25_1)
        l21_1 = Dashboard_M16_EEPS.L21()
        var_2 = add(var_1, l21_1)
        l17_1 = Dashboard_M16_EEPS.L17()
        var_3 = add(var_2, l17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class M33():
    # 'Dashboard_M16_EEPS'!M33
    value = 438855
    formula = "=M29+M25+M21+M17"
    @eval_fn
    def M33():
        m29_1 = Dashboard_M16_EEPS.M29()
        m25_1 = Dashboard_M16_EEPS.M25()
        var_1 = add(m29_1, m25_1)
        m21_1 = Dashboard_M16_EEPS.M21()
        var_2 = add(var_1, m21_1)
        m17_1 = Dashboard_M16_EEPS.M17()
        var_3 = add(var_2, m17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class N33():
    # 'Dashboard_M16_EEPS'!N33
    value = 497349
    formula = "=N29+N25+N21+N17"
    @eval_fn
    def N33():
        n29_1 = Dashboard_M16_EEPS.N29()
        n25_1 = Dashboard_M16_EEPS.N25()
        var_1 = add(n29_1, n25_1)
        n21_1 = Dashboard_M16_EEPS.N21()
        var_2 = add(var_1, n21_1)
        n17_1 = Dashboard_M16_EEPS.N17()
        var_3 = add(var_2, n17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class O33():
    # 'Dashboard_M16_EEPS'!O33
    value = 619361
    formula = "=O29+O25+O21+O17"
    @eval_fn
    def O33():
        o29_1 = Dashboard_M16_EEPS.O29()
        o25_1 = Dashboard_M16_EEPS.O25()
        var_1 = add(o29_1, o25_1)
        o21_1 = Dashboard_M16_EEPS.O21()
        var_2 = add(var_1, o21_1)
        o17_1 = Dashboard_M16_EEPS.O17()
        var_3 = add(var_2, o17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class P33():
    # 'Dashboard_M16_EEPS'!P33
    value = 750126
    formula = "=P29+P25+P21+P17"
    @eval_fn
    def P33():
        p29_1 = Dashboard_M16_EEPS.P29()
        p25_1 = Dashboard_M16_EEPS.P25()
        var_1 = add(p29_1, p25_1)
        p21_1 = Dashboard_M16_EEPS.P21()
        var_2 = add(var_1, p21_1)
        p17_1 = Dashboard_M16_EEPS.P17()
        var_3 = add(var_2, p17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class Q33():
    # 'Dashboard_M16_EEPS'!Q33
    value = 808848
    formula = "=Q29+Q25+Q21+Q17"
    @eval_fn
    def Q33():
        q29_1 = Dashboard_M16_EEPS.Q29()
        q25_1 = Dashboard_M16_EEPS.Q25()
        var_1 = add(q29_1, q25_1)
        q21_1 = Dashboard_M16_EEPS.Q21()
        var_2 = add(var_1, q21_1)
        q17_1 = Dashboard_M16_EEPS.Q17()
        var_3 = add(var_2, q17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class R33():
    # 'Dashboard_M16_EEPS'!R33
    value = 916420
    formula = "=R29+R25+R21+R17"
    @eval_fn
    def R33():
        r29_1 = Dashboard_M16_EEPS.R29()
        r25_1 = Dashboard_M16_EEPS.R25()
        var_1 = add(r29_1, r25_1)
        r21_1 = Dashboard_M16_EEPS.R21()
        var_2 = add(var_1, r21_1)
        r17_1 = Dashboard_M16_EEPS.R17()
        var_3 = add(var_2, r17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class S33():
    # 'Dashboard_M16_EEPS'!S33
    value = 1027328
    formula = "=S29+S25+S21+S17"
    @eval_fn
    def S33():
        s29_1 = Dashboard_M16_EEPS.S29()
        s25_1 = Dashboard_M16_EEPS.S25()
        var_1 = add(s29_1, s25_1)
        s21_1 = Dashboard_M16_EEPS.S21()
        var_2 = add(var_1, s21_1)
        s17_1 = Dashboard_M16_EEPS.S17()
        var_3 = add(var_2, s17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class T33():
    # 'Dashboard_M16_EEPS'!T33
    value = 1209628
    formula = "=T29+T25+T21+T17"
    @eval_fn
    def T33():
        t29_1 = Dashboard_M16_EEPS.T29()
        t25_1 = Dashboard_M16_EEPS.T25()
        var_1 = add(t29_1, t25_1)
        t21_1 = Dashboard_M16_EEPS.T21()
        var_2 = add(var_1, t21_1)
        t17_1 = Dashboard_M16_EEPS.T17()
        var_3 = add(var_2, t17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class U33():
    # 'Dashboard_M16_EEPS'!U33
    value = 1320005
    formula = "=U29+U25+U21+U17"
    @eval_fn
    def U33():
        u29_1 = Dashboard_M16_EEPS.U29()
        u25_1 = Dashboard_M16_EEPS.U25()
        var_1 = add(u29_1, u25_1)
        u21_1 = Dashboard_M16_EEPS.U21()
        var_2 = add(var_1, u21_1)
        u17_1 = Dashboard_M16_EEPS.U17()
        var_3 = add(var_2, u17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class V33():
    # 'Dashboard_M16_EEPS'!V33
    value = 1415773
    formula = "=V29+V25+V21+V17"
    @eval_fn
    def V33():
        v29_1 = Dashboard_M16_EEPS.V29()
        v25_1 = Dashboard_M16_EEPS.V25()
        var_1 = add(v29_1, v25_1)
        v21_1 = Dashboard_M16_EEPS.V21()
        var_2 = add(var_1, v21_1)
        v17_1 = Dashboard_M16_EEPS.V17()
        var_3 = add(var_2, v17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class W33():
    # 'Dashboard_M16_EEPS'!W33
    value = 1511189
    formula = "=W29+W25+W21+W17"
    @eval_fn
    def W33():
        w29_1 = Dashboard_M16_EEPS.W29()
        w25_1 = Dashboard_M16_EEPS.W25()
        var_1 = add(w29_1, w25_1)
        w21_1 = Dashboard_M16_EEPS.W21()
        var_2 = add(var_1, w21_1)
        w17_1 = Dashboard_M16_EEPS.W17()
        var_3 = add(var_2, w17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class X33():
    # 'Dashboard_M16_EEPS'!X33
    value = 0
    formula = "=X29+X25+X21+X17"
    @eval_fn
    def X33():
        x29_1 = Dashboard_M16_EEPS.X29()
        x25_1 = Dashboard_M16_EEPS.X25()
        var_1 = add(x29_1, x25_1)
        x21_1 = Dashboard_M16_EEPS.X21()
        var_2 = add(var_1, x21_1)
        x17_1 = Dashboard_M16_EEPS.X17()
        var_3 = add(var_2, x17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class Y33():
    # 'Dashboard_M16_EEPS'!Y33
    value = 0
    formula = "=Y29+Y25+Y21+Y17"
    @eval_fn
    def Y33():
        y29_1 = Dashboard_M16_EEPS.Y29()
        y25_1 = Dashboard_M16_EEPS.Y25()
        var_1 = add(y29_1, y25_1)
        y21_1 = Dashboard_M16_EEPS.Y21()
        var_2 = add(var_1, y21_1)
        y17_1 = Dashboard_M16_EEPS.Y17()
        var_3 = add(var_2, y17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class Z33():
    # 'Dashboard_M16_EEPS'!Z33
    value = 0
    formula = "=Z29+Z25+Z21+Z17"
    @eval_fn
    def Z33():
        z29_1 = Dashboard_M16_EEPS.Z29()
        z25_1 = Dashboard_M16_EEPS.Z25()
        var_1 = add(z29_1, z25_1)
        z21_1 = Dashboard_M16_EEPS.Z21()
        var_2 = add(var_1, z21_1)
        z17_1 = Dashboard_M16_EEPS.Z17()
        var_3 = add(var_2, z17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AA33():
    # 'Dashboard_M16_EEPS'!AA33
    value = 0
    formula = "=AA29+AA25+AA21+AA17"
    @eval_fn
    def AA33():
        aa29_1 = Dashboard_M16_EEPS.AA29()
        aa25_1 = Dashboard_M16_EEPS.AA25()
        var_1 = add(aa29_1, aa25_1)
        aa21_1 = Dashboard_M16_EEPS.AA21()
        var_2 = add(var_1, aa21_1)
        aa17_1 = Dashboard_M16_EEPS.AA17()
        var_3 = add(var_2, aa17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AB33():
    # 'Dashboard_M16_EEPS'!AB33
    value = 0
    formula = "=AB29+AB25+AB21+AB17"
    @eval_fn
    def AB33():
        ab29_1 = Dashboard_M16_EEPS.AB29()
        ab25_1 = Dashboard_M16_EEPS.AB25()
        var_1 = add(ab29_1, ab25_1)
        ab21_1 = Dashboard_M16_EEPS.AB21()
        var_2 = add(var_1, ab21_1)
        ab17_1 = Dashboard_M16_EEPS.AB17()
        var_3 = add(var_2, ab17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AC33():
    # 'Dashboard_M16_EEPS'!AC33
    value = 0
    formula = "=AC29+AC25+AC21+AC17"
    @eval_fn
    def AC33():
        ac29_1 = Dashboard_M16_EEPS.AC29()
        ac25_1 = Dashboard_M16_EEPS.AC25()
        var_1 = add(ac29_1, ac25_1)
        ac21_1 = Dashboard_M16_EEPS.AC21()
        var_2 = add(var_1, ac21_1)
        ac17_1 = Dashboard_M16_EEPS.AC17()
        var_3 = add(var_2, ac17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AD33():
    # 'Dashboard_M16_EEPS'!AD33
    value = 0
    formula = "=AD29+AD25+AD21+AD17"
    @eval_fn
    def AD33():
        ad29_1 = Dashboard_M16_EEPS.AD29()
        ad25_1 = Dashboard_M16_EEPS.AD25()
        var_1 = add(ad29_1, ad25_1)
        ad21_1 = Dashboard_M16_EEPS.AD21()
        var_2 = add(var_1, ad21_1)
        ad17_1 = Dashboard_M16_EEPS.AD17()
        var_3 = add(var_2, ad17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AE33():
    # 'Dashboard_M16_EEPS'!AE33
    value = 0
    formula = "=AE29+AE25+AE21+AE17"
    @eval_fn
    def AE33():
        ae29_1 = Dashboard_M16_EEPS.AE29()
        ae25_1 = Dashboard_M16_EEPS.AE25()
        var_1 = add(ae29_1, ae25_1)
        ae21_1 = Dashboard_M16_EEPS.AE21()
        var_2 = add(var_1, ae21_1)
        ae17_1 = Dashboard_M16_EEPS.AE17()
        var_3 = add(var_2, ae17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AF33():
    # 'Dashboard_M16_EEPS'!AF33
    value = 0
    formula = "=AF29+AF25+AF21+AF17"
    @eval_fn
    def AF33():
        af29_1 = Dashboard_M16_EEPS.AF29()
        af25_1 = Dashboard_M16_EEPS.AF25()
        var_1 = add(af29_1, af25_1)
        af21_1 = Dashboard_M16_EEPS.AF21()
        var_2 = add(var_1, af21_1)
        af17_1 = Dashboard_M16_EEPS.AF17()
        var_3 = add(var_2, af17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AG33():
    # 'Dashboard_M16_EEPS'!AG33
    value = 0
    formula = "=AG29+AG25+AG21+AG17"
    @eval_fn
    def AG33():
        ag29_1 = Dashboard_M16_EEPS.AG29()
        ag25_1 = Dashboard_M16_EEPS.AG25()
        var_1 = add(ag29_1, ag25_1)
        ag21_1 = Dashboard_M16_EEPS.AG21()
        var_2 = add(var_1, ag21_1)
        ag17_1 = Dashboard_M16_EEPS.AG17()
        var_3 = add(var_2, ag17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AH33():
    # 'Dashboard_M16_EEPS'!AH33
    value = 0
    formula = "=AH29+AH25+AH21+AH17"
    @eval_fn
    def AH33():
        ah29_1 = Dashboard_M16_EEPS.AH29()
        ah25_1 = Dashboard_M16_EEPS.AH25()
        var_1 = add(ah29_1, ah25_1)
        ah21_1 = Dashboard_M16_EEPS.AH21()
        var_2 = add(var_1, ah21_1)
        ah17_1 = Dashboard_M16_EEPS.AH17()
        var_3 = add(var_2, ah17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AI33():
    # 'Dashboard_M16_EEPS'!AI33
    value = 0
    formula = "=AI29+AI25+AI21+AI17"
    @eval_fn
    def AI33():
        ai29_1 = Dashboard_M16_EEPS.AI29()
        ai25_1 = Dashboard_M16_EEPS.AI25()
        var_1 = add(ai29_1, ai25_1)
        ai21_1 = Dashboard_M16_EEPS.AI21()
        var_2 = add(var_1, ai21_1)
        ai17_1 = Dashboard_M16_EEPS.AI17()
        var_3 = add(var_2, ai17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AJ33():
    # 'Dashboard_M16_EEPS'!AJ33
    value = 0
    formula = "=AJ29+AJ25+AJ21+AJ17"
    @eval_fn
    def AJ33():
        aj29_1 = Dashboard_M16_EEPS.AJ29()
        aj25_1 = Dashboard_M16_EEPS.AJ25()
        var_1 = add(aj29_1, aj25_1)
        aj21_1 = Dashboard_M16_EEPS.AJ21()
        var_2 = add(var_1, aj21_1)
        aj17_1 = Dashboard_M16_EEPS.AJ17()
        var_3 = add(var_2, aj17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AK33():
    # 'Dashboard_M16_EEPS'!AK33
    value = 0
    formula = "=AK29+AK25+AK21+AK17"
    @eval_fn
    def AK33():
        ak29_1 = Dashboard_M16_EEPS.AK29()
        ak25_1 = Dashboard_M16_EEPS.AK25()
        var_1 = add(ak29_1, ak25_1)
        ak21_1 = Dashboard_M16_EEPS.AK21()
        var_2 = add(var_1, ak21_1)
        ak17_1 = Dashboard_M16_EEPS.AK17()
        var_3 = add(var_2, ak17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class AL33():
    # 'Dashboard_M16_EEPS'!AL33
    value = 0
    formula = "=AL29+AL25+AL21+AL17"
    @eval_fn
    def AL33():
        al29_1 = Dashboard_M16_EEPS.AL29()
        al25_1 = Dashboard_M16_EEPS.AL25()
        var_1 = add(al29_1, al25_1)
        al21_1 = Dashboard_M16_EEPS.AL21()
        var_2 = add(var_1, al21_1)
        al17_1 = Dashboard_M16_EEPS.AL17()
        var_3 = add(var_2, al17_1)
        return var_3

@register(Dashboard_M16_EEPS)
class A34():
    # 'Dashboard_M16_EEPS'!A34
    value = "Total EETotal"
    formula = '''=C34&"Total"'''
    @eval_fn
    def A34():
        c34_1 = Dashboard_M16_EEPS.C34()
        var_1 = concat(c34_1, "Total")
        return var_1

@register(Dashboard_M16_EEPS)
class C34():
    # 'Dashboard_M16_EEPS'!C34
    value = "Total EE"

@register(Dashboard_M16_EEPS)
class G34():
    # 'Dashboard_M16_EEPS'!G34
    value = "#N/A"
    formula = "=IF(G30+G26+G22+G18=0,NA(),G30+G26+G22+G18)"
    @eval_fn
    def G34():
        g30_1 = Dashboard_M16_EEPS.G30()
        g26_1 = Dashboard_M16_EEPS.G26()
        var_1 = add(g30_1, g26_1)
        g22_1 = Dashboard_M16_EEPS.G22()
        var_2 = add(var_1, g22_1)
        g18_1 = Dashboard_M16_EEPS.G18()
        var_3 = add(var_2, g18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        g30_2 = Dashboard_M16_EEPS.G30()
        g26_2 = Dashboard_M16_EEPS.G26()
        var_6 = add(g30_2, g26_2)
        g22_2 = Dashboard_M16_EEPS.G22()
        var_7 = add(var_6, g22_2)
        g18_2 = Dashboard_M16_EEPS.G18()
        var_8 = add(var_7, g18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class H34():
    # 'Dashboard_M16_EEPS'!H34
    value = "#N/A"
    formula = "=IF(H30+H26+H22+H18=0,NA(),H30+H26+H22+H18)"
    @eval_fn
    def H34():
        h30_1 = Dashboard_M16_EEPS.H30()
        h26_1 = Dashboard_M16_EEPS.H26()
        var_1 = add(h30_1, h26_1)
        h22_1 = Dashboard_M16_EEPS.H22()
        var_2 = add(var_1, h22_1)
        h18_1 = Dashboard_M16_EEPS.H18()
        var_3 = add(var_2, h18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        h30_2 = Dashboard_M16_EEPS.H30()
        h26_2 = Dashboard_M16_EEPS.H26()
        var_6 = add(h30_2, h26_2)
        h22_2 = Dashboard_M16_EEPS.H22()
        var_7 = add(var_6, h22_2)
        h18_2 = Dashboard_M16_EEPS.H18()
        var_8 = add(var_7, h18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class I34():
    # 'Dashboard_M16_EEPS'!I34
    value = "#N/A"
    formula = "=IF(I30+I26+I22+I18=0,NA(),I30+I26+I22+I18)"
    @eval_fn
    def I34():
        i30_1 = Dashboard_M16_EEPS.I30()
        i26_1 = Dashboard_M16_EEPS.I26()
        var_1 = add(i30_1, i26_1)
        i22_1 = Dashboard_M16_EEPS.I22()
        var_2 = add(var_1, i22_1)
        i18_1 = Dashboard_M16_EEPS.I18()
        var_3 = add(var_2, i18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        i30_2 = Dashboard_M16_EEPS.I30()
        i26_2 = Dashboard_M16_EEPS.I26()
        var_6 = add(i30_2, i26_2)
        i22_2 = Dashboard_M16_EEPS.I22()
        var_7 = add(var_6, i22_2)
        i18_2 = Dashboard_M16_EEPS.I18()
        var_8 = add(var_7, i18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class J34():
    # 'Dashboard_M16_EEPS'!J34
    value = "#N/A"
    formula = "=IF(J30+J26+J22+J18=0,NA(),J30+J26+J22+J18)"
    @eval_fn
    def J34():
        j30_1 = Dashboard_M16_EEPS.J30()
        j26_1 = Dashboard_M16_EEPS.J26()
        var_1 = add(j30_1, j26_1)
        j22_1 = Dashboard_M16_EEPS.J22()
        var_2 = add(var_1, j22_1)
        j18_1 = Dashboard_M16_EEPS.J18()
        var_3 = add(var_2, j18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        j30_2 = Dashboard_M16_EEPS.J30()
        j26_2 = Dashboard_M16_EEPS.J26()
        var_6 = add(j30_2, j26_2)
        j22_2 = Dashboard_M16_EEPS.J22()
        var_7 = add(var_6, j22_2)
        j18_2 = Dashboard_M16_EEPS.J18()
        var_8 = add(var_7, j18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class K34():
    # 'Dashboard_M16_EEPS'!K34
    value = 7387
    formula = "=IF(K30+K26+K22+K18=0,NA(),K30+K26+K22+K18)"
    @eval_fn
    def K34():
        k30_1 = Dashboard_M16_EEPS.K30()
        k26_1 = Dashboard_M16_EEPS.K26()
        var_1 = add(k30_1, k26_1)
        k22_1 = Dashboard_M16_EEPS.K22()
        var_2 = add(var_1, k22_1)
        k18_1 = Dashboard_M16_EEPS.K18()
        var_3 = add(var_2, k18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        k30_2 = Dashboard_M16_EEPS.K30()
        k26_2 = Dashboard_M16_EEPS.K26()
        var_6 = add(k30_2, k26_2)
        k22_2 = Dashboard_M16_EEPS.K22()
        var_7 = add(var_6, k22_2)
        k18_2 = Dashboard_M16_EEPS.K18()
        var_8 = add(var_7, k18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class L34():
    # 'Dashboard_M16_EEPS'!L34
    value = 26595
    formula = "=IF(L30+L26+L22+L18=0,NA(),L30+L26+L22+L18)"
    @eval_fn
    def L34():
        l30_1 = Dashboard_M16_EEPS.L30()
        l26_1 = Dashboard_M16_EEPS.L26()
        var_1 = add(l30_1, l26_1)
        l22_1 = Dashboard_M16_EEPS.L22()
        var_2 = add(var_1, l22_1)
        l18_1 = Dashboard_M16_EEPS.L18()
        var_3 = add(var_2, l18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        l30_2 = Dashboard_M16_EEPS.L30()
        l26_2 = Dashboard_M16_EEPS.L26()
        var_6 = add(l30_2, l26_2)
        l22_2 = Dashboard_M16_EEPS.L22()
        var_7 = add(var_6, l22_2)
        l18_2 = Dashboard_M16_EEPS.L18()
        var_8 = add(var_7, l18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class M34():
    # 'Dashboard_M16_EEPS'!M34
    value = 530514
    formula = "=IF(M30+M26+M22+M18=0,NA(),M30+M26+M22+M18)"
    @eval_fn
    def M34():
        m30_1 = Dashboard_M16_EEPS.M30()
        m26_1 = Dashboard_M16_EEPS.M26()
        var_1 = add(m30_1, m26_1)
        m22_1 = Dashboard_M16_EEPS.M22()
        var_2 = add(var_1, m22_1)
        m18_1 = Dashboard_M16_EEPS.M18()
        var_3 = add(var_2, m18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        m30_2 = Dashboard_M16_EEPS.M30()
        m26_2 = Dashboard_M16_EEPS.M26()
        var_6 = add(m30_2, m26_2)
        m22_2 = Dashboard_M16_EEPS.M22()
        var_7 = add(var_6, m22_2)
        m18_2 = Dashboard_M16_EEPS.M18()
        var_8 = add(var_7, m18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class N34():
    # 'Dashboard_M16_EEPS'!N34
    value = 600180
    formula = "=IF(N30+N26+N22+N18=0,NA(),N30+N26+N22+N18)"
    @eval_fn
    def N34():
        n30_1 = Dashboard_M16_EEPS.N30()
        n26_1 = Dashboard_M16_EEPS.N26()
        var_1 = add(n30_1, n26_1)
        n22_1 = Dashboard_M16_EEPS.N22()
        var_2 = add(var_1, n22_1)
        n18_1 = Dashboard_M16_EEPS.N18()
        var_3 = add(var_2, n18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        n30_2 = Dashboard_M16_EEPS.N30()
        n26_2 = Dashboard_M16_EEPS.N26()
        var_6 = add(n30_2, n26_2)
        n22_2 = Dashboard_M16_EEPS.N22()
        var_7 = add(var_6, n22_2)
        n18_2 = Dashboard_M16_EEPS.N18()
        var_8 = add(var_7, n18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class O34():
    # 'Dashboard_M16_EEPS'!O34
    value = 736298
    formula = "=IF(O30+O26+O22+O18=0,NA(),O30+O26+O22+O18)"
    @eval_fn
    def O34():
        o30_1 = Dashboard_M16_EEPS.O30()
        o26_1 = Dashboard_M16_EEPS.O26()
        var_1 = add(o30_1, o26_1)
        o22_1 = Dashboard_M16_EEPS.O22()
        var_2 = add(var_1, o22_1)
        o18_1 = Dashboard_M16_EEPS.O18()
        var_3 = add(var_2, o18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        o30_2 = Dashboard_M16_EEPS.O30()
        o26_2 = Dashboard_M16_EEPS.O26()
        var_6 = add(o30_2, o26_2)
        o22_2 = Dashboard_M16_EEPS.O22()
        var_7 = add(var_6, o22_2)
        o18_2 = Dashboard_M16_EEPS.O18()
        var_8 = add(var_7, o18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class P34():
    # 'Dashboard_M16_EEPS'!P34
    value = 867405
    formula = "=IF(P30+P26+P22+P18=0,NA(),P30+P26+P22+P18)"
    @eval_fn
    def P34():
        p30_1 = Dashboard_M16_EEPS.P30()
        p26_1 = Dashboard_M16_EEPS.P26()
        var_1 = add(p30_1, p26_1)
        p22_1 = Dashboard_M16_EEPS.P22()
        var_2 = add(var_1, p22_1)
        p18_1 = Dashboard_M16_EEPS.P18()
        var_3 = add(var_2, p18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        p30_2 = Dashboard_M16_EEPS.P30()
        p26_2 = Dashboard_M16_EEPS.P26()
        var_6 = add(p30_2, p26_2)
        p22_2 = Dashboard_M16_EEPS.P22()
        var_7 = add(var_6, p22_2)
        p18_2 = Dashboard_M16_EEPS.P18()
        var_8 = add(var_7, p18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class Q34():
    # 'Dashboard_M16_EEPS'!Q34
    value = 938808
    formula = "=IF(Q30+Q26+Q22+Q18=0,NA(),Q30+Q26+Q22+Q18)"
    @eval_fn
    def Q34():
        q30_1 = Dashboard_M16_EEPS.Q30()
        q26_1 = Dashboard_M16_EEPS.Q26()
        var_1 = add(q30_1, q26_1)
        q22_1 = Dashboard_M16_EEPS.Q22()
        var_2 = add(var_1, q22_1)
        q18_1 = Dashboard_M16_EEPS.Q18()
        var_3 = add(var_2, q18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        q30_2 = Dashboard_M16_EEPS.Q30()
        q26_2 = Dashboard_M16_EEPS.Q26()
        var_6 = add(q30_2, q26_2)
        q22_2 = Dashboard_M16_EEPS.Q22()
        var_7 = add(var_6, q22_2)
        q18_2 = Dashboard_M16_EEPS.Q18()
        var_8 = add(var_7, q18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class R34():
    # 'Dashboard_M16_EEPS'!R34
    value = 1088476
    formula = "=IF(R30+R26+R22+R18=0,NA(),R30+R26+R22+R18)"
    @eval_fn
    def R34():
        r30_1 = Dashboard_M16_EEPS.R30()
        r26_1 = Dashboard_M16_EEPS.R26()
        var_1 = add(r30_1, r26_1)
        r22_1 = Dashboard_M16_EEPS.R22()
        var_2 = add(var_1, r22_1)
        r18_1 = Dashboard_M16_EEPS.R18()
        var_3 = add(var_2, r18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        r30_2 = Dashboard_M16_EEPS.R30()
        r26_2 = Dashboard_M16_EEPS.R26()
        var_6 = add(r30_2, r26_2)
        r22_2 = Dashboard_M16_EEPS.R22()
        var_7 = add(var_6, r22_2)
        r18_2 = Dashboard_M16_EEPS.R18()
        var_8 = add(var_7, r18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class S34():
    # 'Dashboard_M16_EEPS'!S34
    value = 1207501
    formula = "=IF(S30+S26+S22+S18=0,NA(),S30+S26+S22+S18)"
    @eval_fn
    def S34():
        s30_1 = Dashboard_M16_EEPS.S30()
        s26_1 = Dashboard_M16_EEPS.S26()
        var_1 = add(s30_1, s26_1)
        s22_1 = Dashboard_M16_EEPS.S22()
        var_2 = add(var_1, s22_1)
        s18_1 = Dashboard_M16_EEPS.S18()
        var_3 = add(var_2, s18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        s30_2 = Dashboard_M16_EEPS.S30()
        s26_2 = Dashboard_M16_EEPS.S26()
        var_6 = add(s30_2, s26_2)
        s22_2 = Dashboard_M16_EEPS.S22()
        var_7 = add(var_6, s22_2)
        s18_2 = Dashboard_M16_EEPS.S18()
        var_8 = add(var_7, s18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class T34():
    # 'Dashboard_M16_EEPS'!T34
    value = 1394339
    formula = "=IF(T30+T26+T22+T18=0,NA(),T30+T26+T22+T18)"
    @eval_fn
    def T34():
        t30_1 = Dashboard_M16_EEPS.T30()
        t26_1 = Dashboard_M16_EEPS.T26()
        var_1 = add(t30_1, t26_1)
        t22_1 = Dashboard_M16_EEPS.T22()
        var_2 = add(var_1, t22_1)
        t18_1 = Dashboard_M16_EEPS.T18()
        var_3 = add(var_2, t18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        t30_2 = Dashboard_M16_EEPS.T30()
        t26_2 = Dashboard_M16_EEPS.T26()
        var_6 = add(t30_2, t26_2)
        t22_2 = Dashboard_M16_EEPS.T22()
        var_7 = add(var_6, t22_2)
        t18_2 = Dashboard_M16_EEPS.T18()
        var_8 = add(var_7, t18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class U34():
    # 'Dashboard_M16_EEPS'!U34
    value = 1494188
    formula = "=IF(U30+U26+U22+U18=0,NA(),U30+U26+U22+U18)"
    @eval_fn
    def U34():
        u30_1 = Dashboard_M16_EEPS.U30()
        u26_1 = Dashboard_M16_EEPS.U26()
        var_1 = add(u30_1, u26_1)
        u22_1 = Dashboard_M16_EEPS.U22()
        var_2 = add(var_1, u22_1)
        u18_1 = Dashboard_M16_EEPS.U18()
        var_3 = add(var_2, u18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        u30_2 = Dashboard_M16_EEPS.U30()
        u26_2 = Dashboard_M16_EEPS.U26()
        var_6 = add(u30_2, u26_2)
        u22_2 = Dashboard_M16_EEPS.U22()
        var_7 = add(var_6, u22_2)
        u18_2 = Dashboard_M16_EEPS.U18()
        var_8 = add(var_7, u18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class V34():
    # 'Dashboard_M16_EEPS'!V34
    value = 1576123
    formula = "=IF(V30+V26+V22+V18=0,NA(),V30+V26+V22+V18)"
    @eval_fn
    def V34():
        v30_1 = Dashboard_M16_EEPS.V30()
        v26_1 = Dashboard_M16_EEPS.V26()
        var_1 = add(v30_1, v26_1)
        v22_1 = Dashboard_M16_EEPS.V22()
        var_2 = add(var_1, v22_1)
        v18_1 = Dashboard_M16_EEPS.V18()
        var_3 = add(var_2, v18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        v30_2 = Dashboard_M16_EEPS.V30()
        v26_2 = Dashboard_M16_EEPS.V26()
        var_6 = add(v30_2, v26_2)
        v22_2 = Dashboard_M16_EEPS.V22()
        var_7 = add(var_6, v22_2)
        v18_2 = Dashboard_M16_EEPS.V18()
        var_8 = add(var_7, v18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class W34():
    # 'Dashboard_M16_EEPS'!W34
    value = 1657706
    formula = "=IF(W30+W26+W22+W18=0,NA(),W30+W26+W22+W18)"
    @eval_fn
    def W34():
        w30_1 = Dashboard_M16_EEPS.W30()
        w26_1 = Dashboard_M16_EEPS.W26()
        var_1 = add(w30_1, w26_1)
        w22_1 = Dashboard_M16_EEPS.W22()
        var_2 = add(var_1, w22_1)
        w18_1 = Dashboard_M16_EEPS.W18()
        var_3 = add(var_2, w18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        w30_2 = Dashboard_M16_EEPS.W30()
        w26_2 = Dashboard_M16_EEPS.W26()
        var_6 = add(w30_2, w26_2)
        w22_2 = Dashboard_M16_EEPS.W22()
        var_7 = add(var_6, w22_2)
        w18_2 = Dashboard_M16_EEPS.W18()
        var_8 = add(var_7, w18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class X34():
    # 'Dashboard_M16_EEPS'!X34
    value = "#N/A"
    formula = "=IF(X30+X26+X22+X18=0,NA(),X30+X26+X22+X18)"
    @eval_fn
    def X34():
        x30_1 = Dashboard_M16_EEPS.X30()
        x26_1 = Dashboard_M16_EEPS.X26()
        var_1 = add(x30_1, x26_1)
        x22_1 = Dashboard_M16_EEPS.X22()
        var_2 = add(var_1, x22_1)
        x18_1 = Dashboard_M16_EEPS.X18()
        var_3 = add(var_2, x18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        x30_2 = Dashboard_M16_EEPS.X30()
        x26_2 = Dashboard_M16_EEPS.X26()
        var_6 = add(x30_2, x26_2)
        x22_2 = Dashboard_M16_EEPS.X22()
        var_7 = add(var_6, x22_2)
        x18_2 = Dashboard_M16_EEPS.X18()
        var_8 = add(var_7, x18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class Y34():
    # 'Dashboard_M16_EEPS'!Y34
    value = "#N/A"
    formula = "=IF(Y30+Y26+Y22+Y18=0,NA(),Y30+Y26+Y22+Y18)"
    @eval_fn
    def Y34():
        y30_1 = Dashboard_M16_EEPS.Y30()
        y26_1 = Dashboard_M16_EEPS.Y26()
        var_1 = add(y30_1, y26_1)
        y22_1 = Dashboard_M16_EEPS.Y22()
        var_2 = add(var_1, y22_1)
        y18_1 = Dashboard_M16_EEPS.Y18()
        var_3 = add(var_2, y18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        y30_2 = Dashboard_M16_EEPS.Y30()
        y26_2 = Dashboard_M16_EEPS.Y26()
        var_6 = add(y30_2, y26_2)
        y22_2 = Dashboard_M16_EEPS.Y22()
        var_7 = add(var_6, y22_2)
        y18_2 = Dashboard_M16_EEPS.Y18()
        var_8 = add(var_7, y18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class Z34():
    # 'Dashboard_M16_EEPS'!Z34
    value = "#N/A"
    formula = "=IF(Z30+Z26+Z22+Z18=0,NA(),Z30+Z26+Z22+Z18)"
    @eval_fn
    def Z34():
        z30_1 = Dashboard_M16_EEPS.Z30()
        z26_1 = Dashboard_M16_EEPS.Z26()
        var_1 = add(z30_1, z26_1)
        z22_1 = Dashboard_M16_EEPS.Z22()
        var_2 = add(var_1, z22_1)
        z18_1 = Dashboard_M16_EEPS.Z18()
        var_3 = add(var_2, z18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        z30_2 = Dashboard_M16_EEPS.Z30()
        z26_2 = Dashboard_M16_EEPS.Z26()
        var_6 = add(z30_2, z26_2)
        z22_2 = Dashboard_M16_EEPS.Z22()
        var_7 = add(var_6, z22_2)
        z18_2 = Dashboard_M16_EEPS.Z18()
        var_8 = add(var_7, z18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AA34():
    # 'Dashboard_M16_EEPS'!AA34
    value = "#N/A"
    formula = "=IF(AA30+AA26+AA22+AA18=0,NA(),AA30+AA26+AA22+AA18)"
    @eval_fn
    def AA34():
        aa30_1 = Dashboard_M16_EEPS.AA30()
        aa26_1 = Dashboard_M16_EEPS.AA26()
        var_1 = add(aa30_1, aa26_1)
        aa22_1 = Dashboard_M16_EEPS.AA22()
        var_2 = add(var_1, aa22_1)
        aa18_1 = Dashboard_M16_EEPS.AA18()
        var_3 = add(var_2, aa18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        aa30_2 = Dashboard_M16_EEPS.AA30()
        aa26_2 = Dashboard_M16_EEPS.AA26()
        var_6 = add(aa30_2, aa26_2)
        aa22_2 = Dashboard_M16_EEPS.AA22()
        var_7 = add(var_6, aa22_2)
        aa18_2 = Dashboard_M16_EEPS.AA18()
        var_8 = add(var_7, aa18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AB34():
    # 'Dashboard_M16_EEPS'!AB34
    value = "#N/A"
    formula = "=IF(AB30+AB26+AB22+AB18=0,NA(),AB30+AB26+AB22+AB18)"
    @eval_fn
    def AB34():
        ab30_1 = Dashboard_M16_EEPS.AB30()
        ab26_1 = Dashboard_M16_EEPS.AB26()
        var_1 = add(ab30_1, ab26_1)
        ab22_1 = Dashboard_M16_EEPS.AB22()
        var_2 = add(var_1, ab22_1)
        ab18_1 = Dashboard_M16_EEPS.AB18()
        var_3 = add(var_2, ab18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        ab30_2 = Dashboard_M16_EEPS.AB30()
        ab26_2 = Dashboard_M16_EEPS.AB26()
        var_6 = add(ab30_2, ab26_2)
        ab22_2 = Dashboard_M16_EEPS.AB22()
        var_7 = add(var_6, ab22_2)
        ab18_2 = Dashboard_M16_EEPS.AB18()
        var_8 = add(var_7, ab18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AC34():
    # 'Dashboard_M16_EEPS'!AC34
    value = "#N/A"
    formula = "=IF(AC30+AC26+AC22+AC18=0,NA(),AC30+AC26+AC22+AC18)"
    @eval_fn
    def AC34():
        ac30_1 = Dashboard_M16_EEPS.AC30()
        ac26_1 = Dashboard_M16_EEPS.AC26()
        var_1 = add(ac30_1, ac26_1)
        ac22_1 = Dashboard_M16_EEPS.AC22()
        var_2 = add(var_1, ac22_1)
        ac18_1 = Dashboard_M16_EEPS.AC18()
        var_3 = add(var_2, ac18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        ac30_2 = Dashboard_M16_EEPS.AC30()
        ac26_2 = Dashboard_M16_EEPS.AC26()
        var_6 = add(ac30_2, ac26_2)
        ac22_2 = Dashboard_M16_EEPS.AC22()
        var_7 = add(var_6, ac22_2)
        ac18_2 = Dashboard_M16_EEPS.AC18()
        var_8 = add(var_7, ac18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AD34():
    # 'Dashboard_M16_EEPS'!AD34
    value = "#N/A"
    formula = "=IF(AD30+AD26+AD22+AD18=0,NA(),AD30+AD26+AD22+AD18)"
    @eval_fn
    def AD34():
        ad30_1 = Dashboard_M16_EEPS.AD30()
        ad26_1 = Dashboard_M16_EEPS.AD26()
        var_1 = add(ad30_1, ad26_1)
        ad22_1 = Dashboard_M16_EEPS.AD22()
        var_2 = add(var_1, ad22_1)
        ad18_1 = Dashboard_M16_EEPS.AD18()
        var_3 = add(var_2, ad18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        ad30_2 = Dashboard_M16_EEPS.AD30()
        ad26_2 = Dashboard_M16_EEPS.AD26()
        var_6 = add(ad30_2, ad26_2)
        ad22_2 = Dashboard_M16_EEPS.AD22()
        var_7 = add(var_6, ad22_2)
        ad18_2 = Dashboard_M16_EEPS.AD18()
        var_8 = add(var_7, ad18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AE34():
    # 'Dashboard_M16_EEPS'!AE34
    value = "#N/A"
    formula = "=IF(AE30+AE26+AE22+AE18=0,NA(),AE30+AE26+AE22+AE18)"
    @eval_fn
    def AE34():
        ae30_1 = Dashboard_M16_EEPS.AE30()
        ae26_1 = Dashboard_M16_EEPS.AE26()
        var_1 = add(ae30_1, ae26_1)
        ae22_1 = Dashboard_M16_EEPS.AE22()
        var_2 = add(var_1, ae22_1)
        ae18_1 = Dashboard_M16_EEPS.AE18()
        var_3 = add(var_2, ae18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        ae30_2 = Dashboard_M16_EEPS.AE30()
        ae26_2 = Dashboard_M16_EEPS.AE26()
        var_6 = add(ae30_2, ae26_2)
        ae22_2 = Dashboard_M16_EEPS.AE22()
        var_7 = add(var_6, ae22_2)
        ae18_2 = Dashboard_M16_EEPS.AE18()
        var_8 = add(var_7, ae18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AF34():
    # 'Dashboard_M16_EEPS'!AF34
    value = "#N/A"
    formula = "=IF(AF30+AF26+AF22+AF18=0,NA(),AF30+AF26+AF22+AF18)"
    @eval_fn
    def AF34():
        af30_1 = Dashboard_M16_EEPS.AF30()
        af26_1 = Dashboard_M16_EEPS.AF26()
        var_1 = add(af30_1, af26_1)
        af22_1 = Dashboard_M16_EEPS.AF22()
        var_2 = add(var_1, af22_1)
        af18_1 = Dashboard_M16_EEPS.AF18()
        var_3 = add(var_2, af18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        af30_2 = Dashboard_M16_EEPS.AF30()
        af26_2 = Dashboard_M16_EEPS.AF26()
        var_6 = add(af30_2, af26_2)
        af22_2 = Dashboard_M16_EEPS.AF22()
        var_7 = add(var_6, af22_2)
        af18_2 = Dashboard_M16_EEPS.AF18()
        var_8 = add(var_7, af18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AG34():
    # 'Dashboard_M16_EEPS'!AG34
    value = "#N/A"
    formula = "=IF(AG30+AG26+AG22+AG18=0,NA(),AG30+AG26+AG22+AG18)"
    @eval_fn
    def AG34():
        ag30_1 = Dashboard_M16_EEPS.AG30()
        ag26_1 = Dashboard_M16_EEPS.AG26()
        var_1 = add(ag30_1, ag26_1)
        ag22_1 = Dashboard_M16_EEPS.AG22()
        var_2 = add(var_1, ag22_1)
        ag18_1 = Dashboard_M16_EEPS.AG18()
        var_3 = add(var_2, ag18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        ag30_2 = Dashboard_M16_EEPS.AG30()
        ag26_2 = Dashboard_M16_EEPS.AG26()
        var_6 = add(ag30_2, ag26_2)
        ag22_2 = Dashboard_M16_EEPS.AG22()
        var_7 = add(var_6, ag22_2)
        ag18_2 = Dashboard_M16_EEPS.AG18()
        var_8 = add(var_7, ag18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AH34():
    # 'Dashboard_M16_EEPS'!AH34
    value = "#N/A"
    formula = "=IF(AH30+AH26+AH22+AH18=0,NA(),AH30+AH26+AH22+AH18)"
    @eval_fn
    def AH34():
        ah30_1 = Dashboard_M16_EEPS.AH30()
        ah26_1 = Dashboard_M16_EEPS.AH26()
        var_1 = add(ah30_1, ah26_1)
        ah22_1 = Dashboard_M16_EEPS.AH22()
        var_2 = add(var_1, ah22_1)
        ah18_1 = Dashboard_M16_EEPS.AH18()
        var_3 = add(var_2, ah18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        ah30_2 = Dashboard_M16_EEPS.AH30()
        ah26_2 = Dashboard_M16_EEPS.AH26()
        var_6 = add(ah30_2, ah26_2)
        ah22_2 = Dashboard_M16_EEPS.AH22()
        var_7 = add(var_6, ah22_2)
        ah18_2 = Dashboard_M16_EEPS.AH18()
        var_8 = add(var_7, ah18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AI34():
    # 'Dashboard_M16_EEPS'!AI34
    value = "#N/A"
    formula = "=IF(AI30+AI26+AI22+AI18=0,NA(),AI30+AI26+AI22+AI18)"
    @eval_fn
    def AI34():
        ai30_1 = Dashboard_M16_EEPS.AI30()
        ai26_1 = Dashboard_M16_EEPS.AI26()
        var_1 = add(ai30_1, ai26_1)
        ai22_1 = Dashboard_M16_EEPS.AI22()
        var_2 = add(var_1, ai22_1)
        ai18_1 = Dashboard_M16_EEPS.AI18()
        var_3 = add(var_2, ai18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        ai30_2 = Dashboard_M16_EEPS.AI30()
        ai26_2 = Dashboard_M16_EEPS.AI26()
        var_6 = add(ai30_2, ai26_2)
        ai22_2 = Dashboard_M16_EEPS.AI22()
        var_7 = add(var_6, ai22_2)
        ai18_2 = Dashboard_M16_EEPS.AI18()
        var_8 = add(var_7, ai18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AJ34():
    # 'Dashboard_M16_EEPS'!AJ34
    value = "#N/A"
    formula = "=IF(AJ30+AJ26+AJ22+AJ18=0,NA(),AJ30+AJ26+AJ22+AJ18)"
    @eval_fn
    def AJ34():
        aj30_1 = Dashboard_M16_EEPS.AJ30()
        aj26_1 = Dashboard_M16_EEPS.AJ26()
        var_1 = add(aj30_1, aj26_1)
        aj22_1 = Dashboard_M16_EEPS.AJ22()
        var_2 = add(var_1, aj22_1)
        aj18_1 = Dashboard_M16_EEPS.AJ18()
        var_3 = add(var_2, aj18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        aj30_2 = Dashboard_M16_EEPS.AJ30()
        aj26_2 = Dashboard_M16_EEPS.AJ26()
        var_6 = add(aj30_2, aj26_2)
        aj22_2 = Dashboard_M16_EEPS.AJ22()
        var_7 = add(var_6, aj22_2)
        aj18_2 = Dashboard_M16_EEPS.AJ18()
        var_8 = add(var_7, aj18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AK34():
    # 'Dashboard_M16_EEPS'!AK34
    value = "#N/A"
    formula = "=IF(AK30+AK26+AK22+AK18=0,NA(),AK30+AK26+AK22+AK18)"
    @eval_fn
    def AK34():
        ak30_1 = Dashboard_M16_EEPS.AK30()
        ak26_1 = Dashboard_M16_EEPS.AK26()
        var_1 = add(ak30_1, ak26_1)
        ak22_1 = Dashboard_M16_EEPS.AK22()
        var_2 = add(var_1, ak22_1)
        ak18_1 = Dashboard_M16_EEPS.AK18()
        var_3 = add(var_2, ak18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        ak30_2 = Dashboard_M16_EEPS.AK30()
        ak26_2 = Dashboard_M16_EEPS.AK26()
        var_6 = add(ak30_2, ak26_2)
        ak22_2 = Dashboard_M16_EEPS.AK22()
        var_7 = add(var_6, ak22_2)
        ak18_2 = Dashboard_M16_EEPS.AK18()
        var_8 = add(var_7, ak18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9

@register(Dashboard_M16_EEPS)
class AL34():
    # 'Dashboard_M16_EEPS'!AL34
    value = "#N/A"
    formula = "=IF(AL30+AL26+AL22+AL18=0,NA(),AL30+AL26+AL22+AL18)"
    @eval_fn
    def AL34():
        al30_1 = Dashboard_M16_EEPS.AL30()
        al26_1 = Dashboard_M16_EEPS.AL26()
        var_1 = add(al30_1, al26_1)
        al22_1 = Dashboard_M16_EEPS.AL22()
        var_2 = add(var_1, al22_1)
        al18_1 = Dashboard_M16_EEPS.AL18()
        var_3 = add(var_2, al18_1)
        var_4 = equal(var_3, 0)
        var_5 = NA()
        al30_2 = Dashboard_M16_EEPS.AL30()
        al26_2 = Dashboard_M16_EEPS.AL26()
        var_6 = add(al30_2, al26_2)
        al22_2 = Dashboard_M16_EEPS.AL22()
        var_7 = add(var_6, al22_2)
        al18_2 = Dashboard_M16_EEPS.AL18()
        var_8 = add(var_7, al18_2)
        var_9 = IF(var_4, var_5, var_8)
        return var_9