# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Input_RPS = Worksheet('Input_RPS', 10, 10)



@register(Input_RPS)
class A1():
    # 'Input_RPS'!A1
    value = "http://puc.hawaii.gov/reports/energy-reports/renewable-portfolio-standards-rps-annual-reports/"

@register(Input_RPS)
class D1():
    # 'Input_RPS'!D1
    value = "Units"

@register(Input_RPS)
class E1():
    # 'Input_RPS'!E1
    value = "Source"

@register(Input_RPS)
class F1():
    # 'Input_RPS'!F1
    value = "Notes"

@register(Input_RPS)
class G1():
    # 'Input_RPS'!G1
    value = 1999

@register(Input_RPS)
class H1():
    # 'Input_RPS'!H1
    value = 2000

@register(Input_RPS)
class I1():
    # 'Input_RPS'!I1
    value = 2001

@register(Input_RPS)
class J1():
    # 'Input_RPS'!J1
    value = 2002

@register(Input_RPS)
class K1():
    # 'Input_RPS'!K1
    value = 2003

@register(Input_RPS)
class L1():
    # 'Input_RPS'!L1
    value = 2004

@register(Input_RPS)
class M1():
    # 'Input_RPS'!M1
    value = 2005

@register(Input_RPS)
class N1():
    # 'Input_RPS'!N1
    value = 2006

@register(Input_RPS)
class O1():
    # 'Input_RPS'!O1
    value = 2007

@register(Input_RPS)
class P1():
    # 'Input_RPS'!P1
    value = 2008

@register(Input_RPS)
class Q1():
    # 'Input_RPS'!Q1
    value = 2009

@register(Input_RPS)
class R1():
    # 'Input_RPS'!R1
    value = 2010

@register(Input_RPS)
class S1():
    # 'Input_RPS'!S1
    value = 2011

@register(Input_RPS)
class T1():
    # 'Input_RPS'!T1
    value = 2012

@register(Input_RPS)
class U1():
    # 'Input_RPS'!U1
    value = 2013

@register(Input_RPS)
class V1():
    # 'Input_RPS'!V1
    value = 2014

@register(Input_RPS)
class W1():
    # 'Input_RPS'!W1
    value = 2015

@register(Input_RPS)
class X1():
    # 'Input_RPS'!X1
    value = 2016

@register(Input_RPS)
class Y1():
    # 'Input_RPS'!Y1
    value = 2017

@register(Input_RPS)
class Z1():
    # 'Input_RPS'!Z1
    value = 2018

@register(Input_RPS)
class AA1():
    # 'Input_RPS'!AA1
    value = 2019

@register(Input_RPS)
class AB1():
    # 'Input_RPS'!AB1
    value = 2020

@register(Input_RPS)
class AC1():
    # 'Input_RPS'!AC1
    value = 2021

@register(Input_RPS)
class AD1():
    # 'Input_RPS'!AD1
    value = 2022

@register(Input_RPS)
class AE1():
    # 'Input_RPS'!AE1
    value = 2023

@register(Input_RPS)
class AF1():
    # 'Input_RPS'!AF1
    value = 2024

@register(Input_RPS)
class AG1():
    # 'Input_RPS'!AG1
    value = 2025

@register(Input_RPS)
class AH1():
    # 'Input_RPS'!AH1
    value = 2026

@register(Input_RPS)
class AI1():
    # 'Input_RPS'!AI1
    value = 2027

@register(Input_RPS)
class AJ1():
    # 'Input_RPS'!AJ1
    value = 2028

@register(Input_RPS)
class AK1():
    # 'Input_RPS'!AK1
    value = 2029

@register(Input_RPS)
class AL1():
    # 'Input_RPS'!AL1
    value = 2030

@register(Input_RPS)
class A2():
    # 'Input_RPS'!A2
    value = "RPS"

@register(Input_RPS)
class A3():
    # 'Input_RPS'!A3
    value = "HECORenewable Electricity"
    formula = "=CONCATENATE(C3,B3)"
    @eval_fn
    def A3():
        c3_1 = Input_RPS.C3()
        b3_1 = Input_RPS.B3()
        var_1 = CONCATENATE(c3_1, b3_1)
        return var_1

@register(Input_RPS)
class B3():
    # 'Input_RPS'!B3
    value = "Renewable Electricity"

@register(Input_RPS)
class C3():
    # 'Input_RPS'!C3
    value = "HECO"

@register(Input_RPS)
class D3():
    # 'Input_RPS'!D3
    value = "MWh"

@register(Input_RPS)
class E3():
    # 'Input_RPS'!E3
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Input_RPS)
class F3():
    # 'Input_RPS'!F3
    value = "1999-2004 includes HPOWER, kapaa landfill gas, minucipal solid waste, and photovoltaic systems"

@register(Input_RPS)
class G3():
    # 'Input_RPS'!G3
    value = 327000

@register(Input_RPS)
class H3():
    # 'Input_RPS'!H3
    value = 325000

@register(Input_RPS)
class I3():
    # 'Input_RPS'!I3
    value = 303000

@register(Input_RPS)
class J3():
    # 'Input_RPS'!J3
    value = 327000

@register(Input_RPS)
class K3():
    # 'Input_RPS'!K3
    value = 368200

@register(Input_RPS)
class L3():
    # 'Input_RPS'!L3
    value = 369400

@register(Input_RPS)
class M3():
    # 'Input_RPS'!M3
    value = 333400
    formula = "=M4+M10+M12+M18+M21+M24"
    @eval_fn
    def M3():
        m4_1 = Input_RPS.M4()
        m10_1 = Input_RPS.M10()
        var_1 = add(m4_1, m10_1)
        m12_1 = Input_RPS.M12()
        var_2 = add(var_1, m12_1)
        m18_1 = Input_RPS.M18()
        var_3 = add(var_2, m18_1)
        m21_1 = Input_RPS.M21()
        var_4 = add(var_3, m21_1)
        m24_1 = Input_RPS.M24()
        var_5 = add(var_4, m24_1)
        return var_5

@register(Input_RPS)
class N3():
    # 'Input_RPS'!N3
    value = 395500
    formula = "=N4+N10+N12+N18+N21+N24"
    @eval_fn
    def N3():
        n4_1 = Input_RPS.N4()
        n10_1 = Input_RPS.N10()
        var_1 = add(n4_1, n10_1)
        n12_1 = Input_RPS.N12()
        var_2 = add(var_1, n12_1)
        n18_1 = Input_RPS.N18()
        var_3 = add(var_2, n18_1)
        n21_1 = Input_RPS.N21()
        var_4 = add(var_3, n21_1)
        n24_1 = Input_RPS.N24()
        var_5 = add(var_4, n24_1)
        return var_5

@register(Input_RPS)
class O3():
    # 'Input_RPS'!O3
    value = 327700
    formula = "=O4+O10+O12+O18+O21+O24"
    @eval_fn
    def O3():
        o4_1 = Input_RPS.O4()
        o10_1 = Input_RPS.O10()
        var_1 = add(o4_1, o10_1)
        o12_1 = Input_RPS.O12()
        var_2 = add(var_1, o12_1)
        o18_1 = Input_RPS.O18()
        var_3 = add(var_2, o18_1)
        o21_1 = Input_RPS.O21()
        var_4 = add(var_3, o21_1)
        o24_1 = Input_RPS.O24()
        var_5 = add(var_4, o24_1)
        return var_5

@register(Input_RPS)
class P3():
    # 'Input_RPS'!P3
    value = 363014
    formula = "=P4+P10+P12+P18+P21+P24"
    @eval_fn
    def P3():
        p4_1 = Input_RPS.P4()
        p10_1 = Input_RPS.P10()
        var_1 = add(p4_1, p10_1)
        p12_1 = Input_RPS.P12()
        var_2 = add(var_1, p12_1)
        p18_1 = Input_RPS.P18()
        var_3 = add(var_2, p18_1)
        p21_1 = Input_RPS.P21()
        var_4 = add(var_3, p21_1)
        p24_1 = Input_RPS.P24()
        var_5 = add(var_4, p24_1)
        return var_5

@register(Input_RPS)
class Q3():
    # 'Input_RPS'!Q3
    value = 379298
    formula = "=Q4+Q10+Q12+Q18+Q21+Q24"
    @eval_fn
    def Q3():
        q4_1 = Input_RPS.Q4()
        q10_1 = Input_RPS.Q10()
        var_1 = add(q4_1, q10_1)
        q12_1 = Input_RPS.Q12()
        var_2 = add(var_1, q12_1)
        q18_1 = Input_RPS.Q18()
        var_3 = add(var_2, q18_1)
        q21_1 = Input_RPS.Q21()
        var_4 = add(var_3, q21_1)
        q24_1 = Input_RPS.Q24()
        var_5 = add(var_4, q24_1)
        return var_5

@register(Input_RPS)
class R3():
    # 'Input_RPS'!R3
    value = 344809
    formula = "=R4+R10+R12+R18+R21+R24"
    @eval_fn
    def R3():
        r4_1 = Input_RPS.R4()
        r10_1 = Input_RPS.R10()
        var_1 = add(r4_1, r10_1)
        r12_1 = Input_RPS.R12()
        var_2 = add(var_1, r12_1)
        r18_1 = Input_RPS.R18()
        var_3 = add(var_2, r18_1)
        r21_1 = Input_RPS.R21()
        var_4 = add(var_3, r21_1)
        r24_1 = Input_RPS.R24()
        var_5 = add(var_4, r24_1)
        return var_5

@register(Input_RPS)
class S3():
    # 'Input_RPS'!S3
    value = 484826
    formula = "=S4+S10+S12+S18+S21+S24"
    @eval_fn
    def S3():
        s4_1 = Input_RPS.S4()
        s10_1 = Input_RPS.S10()
        var_1 = add(s4_1, s10_1)
        s12_1 = Input_RPS.S12()
        var_2 = add(var_1, s12_1)
        s18_1 = Input_RPS.S18()
        var_3 = add(var_2, s18_1)
        s21_1 = Input_RPS.S21()
        var_4 = add(var_3, s21_1)
        s24_1 = Input_RPS.S24()
        var_5 = add(var_4, s24_1)
        return var_5

@register(Input_RPS)
class T3():
    # 'Input_RPS'!T3
    value = 530853
    formula = "=T4+T10+T12+T18+T21+T24"
    @eval_fn
    def T3():
        t4_1 = Input_RPS.T4()
        t10_1 = Input_RPS.T10()
        var_1 = add(t4_1, t10_1)
        t12_1 = Input_RPS.T12()
        var_2 = add(var_1, t12_1)
        t18_1 = Input_RPS.T18()
        var_3 = add(var_2, t18_1)
        t21_1 = Input_RPS.T21()
        var_4 = add(var_3, t21_1)
        t24_1 = Input_RPS.T24()
        var_5 = add(var_4, t24_1)
        return var_5

@register(Input_RPS)
class U3():
    # 'Input_RPS'!U3
    value = 801009
    formula = "=U4+U10+U12+U18+U21+U24"
    @eval_fn
    def U3():
        u4_1 = Input_RPS.U4()
        u10_1 = Input_RPS.U10()
        var_1 = add(u4_1, u10_1)
        u12_1 = Input_RPS.U12()
        var_2 = add(var_1, u12_1)
        u18_1 = Input_RPS.U18()
        var_3 = add(var_2, u18_1)
        u21_1 = Input_RPS.U21()
        var_4 = add(var_3, u21_1)
        u24_1 = Input_RPS.U24()
        var_5 = add(var_4, u24_1)
        return var_5

@register(Input_RPS)
class V3():
    # 'Input_RPS'!V3
    value = 1029070
    formula = "=V4+V10+V12+V18+V21+V24"
    @eval_fn
    def V3():
        v4_1 = Input_RPS.V4()
        v10_1 = Input_RPS.V10()
        var_1 = add(v4_1, v10_1)
        v12_1 = Input_RPS.V12()
        var_2 = add(var_1, v12_1)
        v18_1 = Input_RPS.V18()
        var_3 = add(var_2, v18_1)
        v21_1 = Input_RPS.V21()
        var_4 = add(var_3, v21_1)
        v24_1 = Input_RPS.V24()
        var_5 = add(var_4, v24_1)
        return var_5

@register(Input_RPS)
class W3():
    # 'Input_RPS'!W3
    value = 1159629
    formula = "=W4+W10+W12+W18+W21+W24"
    @eval_fn
    def W3():
        w4_1 = Input_RPS.W4()
        w10_1 = Input_RPS.W10()
        var_1 = add(w4_1, w10_1)
        w12_1 = Input_RPS.W12()
        var_2 = add(var_1, w12_1)
        w18_1 = Input_RPS.W18()
        var_3 = add(var_2, w18_1)
        w21_1 = Input_RPS.W21()
        var_4 = add(var_3, w21_1)
        w24_1 = Input_RPS.W24()
        var_5 = add(var_4, w24_1)
        return var_5

@register(Input_RPS)
class X3():
    # 'Input_RPS'!X3
    value = 0
    formula = "=X4+X10+X12+X18+X21+X24"
    @eval_fn
    def X3():
        x4_1 = Input_RPS.X4()
        x10_1 = Input_RPS.X10()
        var_1 = add(x4_1, x10_1)
        x12_1 = Input_RPS.X12()
        var_2 = add(var_1, x12_1)
        x18_1 = Input_RPS.X18()
        var_3 = add(var_2, x18_1)
        x21_1 = Input_RPS.X21()
        var_4 = add(var_3, x21_1)
        x24_1 = Input_RPS.X24()
        var_5 = add(var_4, x24_1)
        return var_5

@register(Input_RPS)
class Y3():
    # 'Input_RPS'!Y3
    value = 0
    formula = "=Y4+Y10+Y12+Y18+Y21+Y24"
    @eval_fn
    def Y3():
        y4_1 = Input_RPS.Y4()
        y10_1 = Input_RPS.Y10()
        var_1 = add(y4_1, y10_1)
        y12_1 = Input_RPS.Y12()
        var_2 = add(var_1, y12_1)
        y18_1 = Input_RPS.Y18()
        var_3 = add(var_2, y18_1)
        y21_1 = Input_RPS.Y21()
        var_4 = add(var_3, y21_1)
        y24_1 = Input_RPS.Y24()
        var_5 = add(var_4, y24_1)
        return var_5

@register(Input_RPS)
class Z3():
    # 'Input_RPS'!Z3
    value = 0
    formula = "=Z4+Z10+Z12+Z18+Z21+Z24"
    @eval_fn
    def Z3():
        z4_1 = Input_RPS.Z4()
        z10_1 = Input_RPS.Z10()
        var_1 = add(z4_1, z10_1)
        z12_1 = Input_RPS.Z12()
        var_2 = add(var_1, z12_1)
        z18_1 = Input_RPS.Z18()
        var_3 = add(var_2, z18_1)
        z21_1 = Input_RPS.Z21()
        var_4 = add(var_3, z21_1)
        z24_1 = Input_RPS.Z24()
        var_5 = add(var_4, z24_1)
        return var_5

@register(Input_RPS)
class AA3():
    # 'Input_RPS'!AA3
    value = 0
    formula = "=AA4+AA10+AA12+AA18+AA21+AA24"
    @eval_fn
    def AA3():
        aa4_1 = Input_RPS.AA4()
        aa10_1 = Input_RPS.AA10()
        var_1 = add(aa4_1, aa10_1)
        aa12_1 = Input_RPS.AA12()
        var_2 = add(var_1, aa12_1)
        aa18_1 = Input_RPS.AA18()
        var_3 = add(var_2, aa18_1)
        aa21_1 = Input_RPS.AA21()
        var_4 = add(var_3, aa21_1)
        aa24_1 = Input_RPS.AA24()
        var_5 = add(var_4, aa24_1)
        return var_5

@register(Input_RPS)
class AB3():
    # 'Input_RPS'!AB3
    value = 0
    formula = "=AB4+AB10+AB12+AB18+AB21+AB24"
    @eval_fn
    def AB3():
        ab4_1 = Input_RPS.AB4()
        ab10_1 = Input_RPS.AB10()
        var_1 = add(ab4_1, ab10_1)
        ab12_1 = Input_RPS.AB12()
        var_2 = add(var_1, ab12_1)
        ab18_1 = Input_RPS.AB18()
        var_3 = add(var_2, ab18_1)
        ab21_1 = Input_RPS.AB21()
        var_4 = add(var_3, ab21_1)
        ab24_1 = Input_RPS.AB24()
        var_5 = add(var_4, ab24_1)
        return var_5

@register(Input_RPS)
class AC3():
    # 'Input_RPS'!AC3
    value = 0
    formula = "=AC4+AC10+AC12+AC18+AC21+AC24"
    @eval_fn
    def AC3():
        ac4_1 = Input_RPS.AC4()
        ac10_1 = Input_RPS.AC10()
        var_1 = add(ac4_1, ac10_1)
        ac12_1 = Input_RPS.AC12()
        var_2 = add(var_1, ac12_1)
        ac18_1 = Input_RPS.AC18()
        var_3 = add(var_2, ac18_1)
        ac21_1 = Input_RPS.AC21()
        var_4 = add(var_3, ac21_1)
        ac24_1 = Input_RPS.AC24()
        var_5 = add(var_4, ac24_1)
        return var_5

@register(Input_RPS)
class AD3():
    # 'Input_RPS'!AD3
    value = 0
    formula = "=AD4+AD10+AD12+AD18+AD21+AD24"
    @eval_fn
    def AD3():
        ad4_1 = Input_RPS.AD4()
        ad10_1 = Input_RPS.AD10()
        var_1 = add(ad4_1, ad10_1)
        ad12_1 = Input_RPS.AD12()
        var_2 = add(var_1, ad12_1)
        ad18_1 = Input_RPS.AD18()
        var_3 = add(var_2, ad18_1)
        ad21_1 = Input_RPS.AD21()
        var_4 = add(var_3, ad21_1)
        ad24_1 = Input_RPS.AD24()
        var_5 = add(var_4, ad24_1)
        return var_5

@register(Input_RPS)
class AE3():
    # 'Input_RPS'!AE3
    value = 0
    formula = "=AE4+AE10+AE12+AE18+AE21+AE24"
    @eval_fn
    def AE3():
        ae4_1 = Input_RPS.AE4()
        ae10_1 = Input_RPS.AE10()
        var_1 = add(ae4_1, ae10_1)
        ae12_1 = Input_RPS.AE12()
        var_2 = add(var_1, ae12_1)
        ae18_1 = Input_RPS.AE18()
        var_3 = add(var_2, ae18_1)
        ae21_1 = Input_RPS.AE21()
        var_4 = add(var_3, ae21_1)
        ae24_1 = Input_RPS.AE24()
        var_5 = add(var_4, ae24_1)
        return var_5

@register(Input_RPS)
class AF3():
    # 'Input_RPS'!AF3
    value = 0
    formula = "=AF4+AF10+AF12+AF18+AF21+AF24"
    @eval_fn
    def AF3():
        af4_1 = Input_RPS.AF4()
        af10_1 = Input_RPS.AF10()
        var_1 = add(af4_1, af10_1)
        af12_1 = Input_RPS.AF12()
        var_2 = add(var_1, af12_1)
        af18_1 = Input_RPS.AF18()
        var_3 = add(var_2, af18_1)
        af21_1 = Input_RPS.AF21()
        var_4 = add(var_3, af21_1)
        af24_1 = Input_RPS.AF24()
        var_5 = add(var_4, af24_1)
        return var_5

@register(Input_RPS)
class AG3():
    # 'Input_RPS'!AG3
    value = 0
    formula = "=AG4+AG10+AG12+AG18+AG21+AG24"
    @eval_fn
    def AG3():
        ag4_1 = Input_RPS.AG4()
        ag10_1 = Input_RPS.AG10()
        var_1 = add(ag4_1, ag10_1)
        ag12_1 = Input_RPS.AG12()
        var_2 = add(var_1, ag12_1)
        ag18_1 = Input_RPS.AG18()
        var_3 = add(var_2, ag18_1)
        ag21_1 = Input_RPS.AG21()
        var_4 = add(var_3, ag21_1)
        ag24_1 = Input_RPS.AG24()
        var_5 = add(var_4, ag24_1)
        return var_5

@register(Input_RPS)
class AH3():
    # 'Input_RPS'!AH3
    value = 0
    formula = "=AH4+AH10+AH12+AH18+AH21+AH24"
    @eval_fn
    def AH3():
        ah4_1 = Input_RPS.AH4()
        ah10_1 = Input_RPS.AH10()
        var_1 = add(ah4_1, ah10_1)
        ah12_1 = Input_RPS.AH12()
        var_2 = add(var_1, ah12_1)
        ah18_1 = Input_RPS.AH18()
        var_3 = add(var_2, ah18_1)
        ah21_1 = Input_RPS.AH21()
        var_4 = add(var_3, ah21_1)
        ah24_1 = Input_RPS.AH24()
        var_5 = add(var_4, ah24_1)
        return var_5

@register(Input_RPS)
class AI3():
    # 'Input_RPS'!AI3
    value = 0
    formula = "=AI4+AI10+AI12+AI18+AI21+AI24"
    @eval_fn
    def AI3():
        ai4_1 = Input_RPS.AI4()
        ai10_1 = Input_RPS.AI10()
        var_1 = add(ai4_1, ai10_1)
        ai12_1 = Input_RPS.AI12()
        var_2 = add(var_1, ai12_1)
        ai18_1 = Input_RPS.AI18()
        var_3 = add(var_2, ai18_1)
        ai21_1 = Input_RPS.AI21()
        var_4 = add(var_3, ai21_1)
        ai24_1 = Input_RPS.AI24()
        var_5 = add(var_4, ai24_1)
        return var_5

@register(Input_RPS)
class AJ3():
    # 'Input_RPS'!AJ3
    value = 0
    formula = "=AJ4+AJ10+AJ12+AJ18+AJ21+AJ24"
    @eval_fn
    def AJ3():
        aj4_1 = Input_RPS.AJ4()
        aj10_1 = Input_RPS.AJ10()
        var_1 = add(aj4_1, aj10_1)
        aj12_1 = Input_RPS.AJ12()
        var_2 = add(var_1, aj12_1)
        aj18_1 = Input_RPS.AJ18()
        var_3 = add(var_2, aj18_1)
        aj21_1 = Input_RPS.AJ21()
        var_4 = add(var_3, aj21_1)
        aj24_1 = Input_RPS.AJ24()
        var_5 = add(var_4, aj24_1)
        return var_5

@register(Input_RPS)
class AK3():
    # 'Input_RPS'!AK3
    value = 0
    formula = "=AK4+AK10+AK12+AK18+AK21+AK24"
    @eval_fn
    def AK3():
        ak4_1 = Input_RPS.AK4()
        ak10_1 = Input_RPS.AK10()
        var_1 = add(ak4_1, ak10_1)
        ak12_1 = Input_RPS.AK12()
        var_2 = add(var_1, ak12_1)
        ak18_1 = Input_RPS.AK18()
        var_3 = add(var_2, ak18_1)
        ak21_1 = Input_RPS.AK21()
        var_4 = add(var_3, ak21_1)
        ak24_1 = Input_RPS.AK24()
        var_5 = add(var_4, ak24_1)
        return var_5

@register(Input_RPS)
class AL3():
    # 'Input_RPS'!AL3
    value = 0
    formula = "=AL4+AL10+AL12+AL18+AL21+AL24"
    @eval_fn
    def AL3():
        al4_1 = Input_RPS.AL4()
        al10_1 = Input_RPS.AL10()
        var_1 = add(al4_1, al10_1)
        al12_1 = Input_RPS.AL12()
        var_2 = add(var_1, al12_1)
        al18_1 = Input_RPS.AL18()
        var_3 = add(var_2, al18_1)
        al21_1 = Input_RPS.AL21()
        var_4 = add(var_3, al21_1)
        al24_1 = Input_RPS.AL24()
        var_5 = add(var_4, al24_1)
        return var_5

@register(Input_RPS)
class C4():
    # 'Input_RPS'!C4
    value = "Hydro:"

@register(Input_RPS)
class G4():
    # 'Input_RPS'!G4
    value = 0
    formula = "=SUM(G5:G9)"
    @eval_fn
    def G4():
        range_1 = Input_RPS(7, 5, 7, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H4():
    # 'Input_RPS'!H4
    value = 0
    formula = "=SUM(H5:H9)"
    @eval_fn
    def H4():
        range_1 = Input_RPS(8, 5, 8, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I4():
    # 'Input_RPS'!I4
    value = 0
    formula = "=SUM(I5:I9)"
    @eval_fn
    def I4():
        range_1 = Input_RPS(9, 5, 9, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J4():
    # 'Input_RPS'!J4
    value = 0
    formula = "=SUM(J5:J9)"
    @eval_fn
    def J4():
        range_1 = Input_RPS(10, 5, 10, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K4():
    # 'Input_RPS'!K4
    value = 0
    formula = "=SUM(K5:K9)"
    @eval_fn
    def K4():
        range_1 = Input_RPS(11, 5, 11, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L4():
    # 'Input_RPS'!L4
    value = 0
    formula = "=SUM(L5:L9)"
    @eval_fn
    def L4():
        range_1 = Input_RPS(12, 5, 12, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M4():
    # 'Input_RPS'!M4
    value = 0
    formula = "=SUM(M5:M9)"
    @eval_fn
    def M4():
        range_1 = Input_RPS(13, 5, 13, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N4():
    # 'Input_RPS'!N4
    value = 0
    formula = "=SUM(N5:N9)"
    @eval_fn
    def N4():
        range_1 = Input_RPS(14, 5, 14, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O4():
    # 'Input_RPS'!O4
    value = 0
    formula = "=SUM(O5:O9)"
    @eval_fn
    def O4():
        range_1 = Input_RPS(15, 5, 15, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P4():
    # 'Input_RPS'!P4
    value = 0
    formula = "=SUM(P5:P9)"
    @eval_fn
    def P4():
        range_1 = Input_RPS(16, 5, 16, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q4():
    # 'Input_RPS'!Q4
    value = 0
    formula = "=SUM(Q5:Q9)"
    @eval_fn
    def Q4():
        range_1 = Input_RPS(17, 5, 17, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R4():
    # 'Input_RPS'!R4
    value = 0
    formula = "=SUM(R5:R9)"
    @eval_fn
    def R4():
        range_1 = Input_RPS(18, 5, 18, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S4():
    # 'Input_RPS'!S4
    value = 0
    formula = "=SUM(S5:S9)"
    @eval_fn
    def S4():
        range_1 = Input_RPS(19, 5, 19, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T4():
    # 'Input_RPS'!T4
    value = 0
    formula = "=SUM(T5:T9)"
    @eval_fn
    def T4():
        range_1 = Input_RPS(20, 5, 20, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U4():
    # 'Input_RPS'!U4
    value = 0
    formula = "=SUM(U5:U9)"
    @eval_fn
    def U4():
        range_1 = Input_RPS(21, 5, 21, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V4():
    # 'Input_RPS'!V4
    value = 0
    formula = "=SUM(V5:V9)"
    @eval_fn
    def V4():
        range_1 = Input_RPS(22, 5, 22, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W4():
    # 'Input_RPS'!W4
    value = 0
    formula = "=SUM(W5:W9)"
    @eval_fn
    def W4():
        range_1 = Input_RPS(23, 5, 23, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class X4():
    # 'Input_RPS'!X4
    value = 0
    formula = "=SUM(X5:X9)"
    @eval_fn
    def X4():
        range_1 = Input_RPS(24, 5, 24, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y4():
    # 'Input_RPS'!Y4
    value = 0
    formula = "=SUM(Y5:Y9)"
    @eval_fn
    def Y4():
        range_1 = Input_RPS(25, 5, 25, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z4():
    # 'Input_RPS'!Z4
    value = 0
    formula = "=SUM(Z5:Z9)"
    @eval_fn
    def Z4():
        range_1 = Input_RPS(26, 5, 26, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA4():
    # 'Input_RPS'!AA4
    value = 0
    formula = "=SUM(AA5:AA9)"
    @eval_fn
    def AA4():
        range_1 = Input_RPS(27, 5, 27, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB4():
    # 'Input_RPS'!AB4
    value = 0
    formula = "=SUM(AB5:AB9)"
    @eval_fn
    def AB4():
        range_1 = Input_RPS(28, 5, 28, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC4():
    # 'Input_RPS'!AC4
    value = 0
    formula = "=SUM(AC5:AC9)"
    @eval_fn
    def AC4():
        range_1 = Input_RPS(29, 5, 29, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD4():
    # 'Input_RPS'!AD4
    value = 0
    formula = "=SUM(AD5:AD9)"
    @eval_fn
    def AD4():
        range_1 = Input_RPS(30, 5, 30, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE4():
    # 'Input_RPS'!AE4
    value = 0
    formula = "=SUM(AE5:AE9)"
    @eval_fn
    def AE4():
        range_1 = Input_RPS(31, 5, 31, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF4():
    # 'Input_RPS'!AF4
    value = 0
    formula = "=SUM(AF5:AF9)"
    @eval_fn
    def AF4():
        range_1 = Input_RPS(32, 5, 32, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG4():
    # 'Input_RPS'!AG4
    value = 0
    formula = "=SUM(AG5:AG9)"
    @eval_fn
    def AG4():
        range_1 = Input_RPS(33, 5, 33, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH4():
    # 'Input_RPS'!AH4
    value = 0
    formula = "=SUM(AH5:AH9)"
    @eval_fn
    def AH4():
        range_1 = Input_RPS(34, 5, 34, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI4():
    # 'Input_RPS'!AI4
    value = 0
    formula = "=SUM(AI5:AI9)"
    @eval_fn
    def AI4():
        range_1 = Input_RPS(35, 5, 35, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ4():
    # 'Input_RPS'!AJ4
    value = 0
    formula = "=SUM(AJ5:AJ9)"
    @eval_fn
    def AJ4():
        range_1 = Input_RPS(36, 5, 36, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK4():
    # 'Input_RPS'!AK4
    value = 0
    formula = "=SUM(AK5:AK9)"
    @eval_fn
    def AK4():
        range_1 = Input_RPS(37, 5, 37, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL4():
    # 'Input_RPS'!AL4
    value = 0
    formula = "=SUM(AL5:AL9)"
    @eval_fn
    def AL4():
        range_1 = Input_RPS(38, 5, 38, 9)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C5():
    # 'Input_RPS'!C5
    value = "               Hydro-Wailuku"

@register(Input_RPS)
class N5():
    # 'Input_RPS'!N5
    value = 0

@register(Input_RPS)
class O5():
    # 'Input_RPS'!O5
    value = 0

@register(Input_RPS)
class P5():
    # 'Input_RPS'!P5
    value = 0

@register(Input_RPS)
class Q5():
    # 'Input_RPS'!Q5
    value = 0

@register(Input_RPS)
class R5():
    # 'Input_RPS'!R5
    value = 0

@register(Input_RPS)
class S5():
    # 'Input_RPS'!S5
    value = 0

@register(Input_RPS)
class C6():
    # 'Input_RPS'!C6
    value = "               Small Hydro"

@register(Input_RPS)
class N6():
    # 'Input_RPS'!N6
    value = 0

@register(Input_RPS)
class O6():
    # 'Input_RPS'!O6
    value = 0

@register(Input_RPS)
class P6():
    # 'Input_RPS'!P6
    value = 0

@register(Input_RPS)
class Q6():
    # 'Input_RPS'!Q6
    value = 0

@register(Input_RPS)
class R6():
    # 'Input_RPS'!R6
    value = 0

@register(Input_RPS)
class S6():
    # 'Input_RPS'!S6
    value = 0

@register(Input_RPS)
class C7():
    # 'Input_RPS'!C7
    value = "               Hydro-Helco owned"

@register(Input_RPS)
class N7():
    # 'Input_RPS'!N7
    value = 0

@register(Input_RPS)
class O7():
    # 'Input_RPS'!O7
    value = 0

@register(Input_RPS)
class P7():
    # 'Input_RPS'!P7
    value = 0

@register(Input_RPS)
class Q7():
    # 'Input_RPS'!Q7
    value = 0

@register(Input_RPS)
class R7():
    # 'Input_RPS'!R7
    value = 0

@register(Input_RPS)
class S7():
    # 'Input_RPS'!S7
    value = 0

@register(Input_RPS)
class C8():
    # 'Input_RPS'!C8
    value = "               Biomass & Hyrdro HC&S"

@register(Input_RPS)
class N8():
    # 'Input_RPS'!N8
    value = 0

@register(Input_RPS)
class O8():
    # 'Input_RPS'!O8
    value = 0

@register(Input_RPS)
class P8():
    # 'Input_RPS'!P8
    value = 0

@register(Input_RPS)
class Q8():
    # 'Input_RPS'!Q8
    value = 0

@register(Input_RPS)
class R8():
    # 'Input_RPS'!R8
    value = 0

@register(Input_RPS)
class S8():
    # 'Input_RPS'!S8
    value = 0

@register(Input_RPS)
class C10():
    # 'Input_RPS'!C10
    value = "Geothermal:"

@register(Input_RPS)
class G10():
    # 'Input_RPS'!G10
    value = 0
    formula = "=SUM(G11)"
    @eval_fn
    def G10():
        g11_1 = Input_RPS.G11()
        var_1 = SUM(g11_1)
        return var_1

@register(Input_RPS)
class H10():
    # 'Input_RPS'!H10
    value = 0
    formula = "=SUM(H11)"
    @eval_fn
    def H10():
        h11_1 = Input_RPS.H11()
        var_1 = SUM(h11_1)
        return var_1

@register(Input_RPS)
class I10():
    # 'Input_RPS'!I10
    value = 0
    formula = "=SUM(I11)"
    @eval_fn
    def I10():
        i11_1 = Input_RPS.I11()
        var_1 = SUM(i11_1)
        return var_1

@register(Input_RPS)
class J10():
    # 'Input_RPS'!J10
    value = 0
    formula = "=SUM(J11)"
    @eval_fn
    def J10():
        j11_1 = Input_RPS.J11()
        var_1 = SUM(j11_1)
        return var_1

@register(Input_RPS)
class K10():
    # 'Input_RPS'!K10
    value = 0
    formula = "=SUM(K11)"
    @eval_fn
    def K10():
        k11_1 = Input_RPS.K11()
        var_1 = SUM(k11_1)
        return var_1

@register(Input_RPS)
class L10():
    # 'Input_RPS'!L10
    value = 0
    formula = "=SUM(L11)"
    @eval_fn
    def L10():
        l11_1 = Input_RPS.L11()
        var_1 = SUM(l11_1)
        return var_1

@register(Input_RPS)
class M10():
    # 'Input_RPS'!M10
    value = 0
    formula = "=SUM(M11)"
    @eval_fn
    def M10():
        m11_1 = Input_RPS.M11()
        var_1 = SUM(m11_1)
        return var_1

@register(Input_RPS)
class N10():
    # 'Input_RPS'!N10
    value = 0
    formula = "=SUM(N11)"
    @eval_fn
    def N10():
        n11_1 = Input_RPS.N11()
        var_1 = SUM(n11_1)
        return var_1

@register(Input_RPS)
class O10():
    # 'Input_RPS'!O10
    value = 0
    formula = "=SUM(O11)"
    @eval_fn
    def O10():
        o11_1 = Input_RPS.O11()
        var_1 = SUM(o11_1)
        return var_1

@register(Input_RPS)
class P10():
    # 'Input_RPS'!P10
    value = 0
    formula = "=SUM(P11)"
    @eval_fn
    def P10():
        p11_1 = Input_RPS.P11()
        var_1 = SUM(p11_1)
        return var_1

@register(Input_RPS)
class Q10():
    # 'Input_RPS'!Q10
    value = 0
    formula = "=SUM(Q11)"
    @eval_fn
    def Q10():
        q11_1 = Input_RPS.Q11()
        var_1 = SUM(q11_1)
        return var_1

@register(Input_RPS)
class R10():
    # 'Input_RPS'!R10
    value = 0
    formula = "=SUM(R11)"
    @eval_fn
    def R10():
        r11_1 = Input_RPS.R11()
        var_1 = SUM(r11_1)
        return var_1

@register(Input_RPS)
class S10():
    # 'Input_RPS'!S10
    value = 0
    formula = "=SUM(S11)"
    @eval_fn
    def S10():
        s11_1 = Input_RPS.S11()
        var_1 = SUM(s11_1)
        return var_1

@register(Input_RPS)
class T10():
    # 'Input_RPS'!T10
    value = 0
    formula = "=SUM(T11)"
    @eval_fn
    def T10():
        t11_1 = Input_RPS.T11()
        var_1 = SUM(t11_1)
        return var_1

@register(Input_RPS)
class U10():
    # 'Input_RPS'!U10
    value = 0
    formula = "=SUM(U11)"
    @eval_fn
    def U10():
        u11_1 = Input_RPS.U11()
        var_1 = SUM(u11_1)
        return var_1

@register(Input_RPS)
class V10():
    # 'Input_RPS'!V10
    value = 0
    formula = "=SUM(V11)"
    @eval_fn
    def V10():
        v11_1 = Input_RPS.V11()
        var_1 = SUM(v11_1)
        return var_1

@register(Input_RPS)
class W10():
    # 'Input_RPS'!W10
    value = 0
    formula = "=SUM(W11)"
    @eval_fn
    def W10():
        w11_1 = Input_RPS.W11()
        var_1 = SUM(w11_1)
        return var_1

@register(Input_RPS)
class X10():
    # 'Input_RPS'!X10
    value = 0
    formula = "=SUM(X11)"
    @eval_fn
    def X10():
        x11_1 = Input_RPS.X11()
        var_1 = SUM(x11_1)
        return var_1

@register(Input_RPS)
class Y10():
    # 'Input_RPS'!Y10
    value = 0
    formula = "=SUM(Y11)"
    @eval_fn
    def Y10():
        y11_1 = Input_RPS.Y11()
        var_1 = SUM(y11_1)
        return var_1

@register(Input_RPS)
class Z10():
    # 'Input_RPS'!Z10
    value = 0
    formula = "=SUM(Z11)"
    @eval_fn
    def Z10():
        z11_1 = Input_RPS.Z11()
        var_1 = SUM(z11_1)
        return var_1

@register(Input_RPS)
class AA10():
    # 'Input_RPS'!AA10
    value = 0
    formula = "=SUM(AA11)"
    @eval_fn
    def AA10():
        aa11_1 = Input_RPS.AA11()
        var_1 = SUM(aa11_1)
        return var_1

@register(Input_RPS)
class AB10():
    # 'Input_RPS'!AB10
    value = 0
    formula = "=SUM(AB11)"
    @eval_fn
    def AB10():
        ab11_1 = Input_RPS.AB11()
        var_1 = SUM(ab11_1)
        return var_1

@register(Input_RPS)
class AC10():
    # 'Input_RPS'!AC10
    value = 0
    formula = "=SUM(AC11)"
    @eval_fn
    def AC10():
        ac11_1 = Input_RPS.AC11()
        var_1 = SUM(ac11_1)
        return var_1

@register(Input_RPS)
class AD10():
    # 'Input_RPS'!AD10
    value = 0
    formula = "=SUM(AD11)"
    @eval_fn
    def AD10():
        ad11_1 = Input_RPS.AD11()
        var_1 = SUM(ad11_1)
        return var_1

@register(Input_RPS)
class AE10():
    # 'Input_RPS'!AE10
    value = 0
    formula = "=SUM(AE11)"
    @eval_fn
    def AE10():
        ae11_1 = Input_RPS.AE11()
        var_1 = SUM(ae11_1)
        return var_1

@register(Input_RPS)
class AF10():
    # 'Input_RPS'!AF10
    value = 0
    formula = "=SUM(AF11)"
    @eval_fn
    def AF10():
        af11_1 = Input_RPS.AF11()
        var_1 = SUM(af11_1)
        return var_1

@register(Input_RPS)
class AG10():
    # 'Input_RPS'!AG10
    value = 0
    formula = "=SUM(AG11)"
    @eval_fn
    def AG10():
        ag11_1 = Input_RPS.AG11()
        var_1 = SUM(ag11_1)
        return var_1

@register(Input_RPS)
class AH10():
    # 'Input_RPS'!AH10
    value = 0
    formula = "=SUM(AH11)"
    @eval_fn
    def AH10():
        ah11_1 = Input_RPS.AH11()
        var_1 = SUM(ah11_1)
        return var_1

@register(Input_RPS)
class AI10():
    # 'Input_RPS'!AI10
    value = 0
    formula = "=SUM(AI11)"
    @eval_fn
    def AI10():
        ai11_1 = Input_RPS.AI11()
        var_1 = SUM(ai11_1)
        return var_1

@register(Input_RPS)
class AJ10():
    # 'Input_RPS'!AJ10
    value = 0
    formula = "=SUM(AJ11)"
    @eval_fn
    def AJ10():
        aj11_1 = Input_RPS.AJ11()
        var_1 = SUM(aj11_1)
        return var_1

@register(Input_RPS)
class AK10():
    # 'Input_RPS'!AK10
    value = 0
    formula = "=SUM(AK11)"
    @eval_fn
    def AK10():
        ak11_1 = Input_RPS.AK11()
        var_1 = SUM(ak11_1)
        return var_1

@register(Input_RPS)
class AL10():
    # 'Input_RPS'!AL10
    value = 0
    formula = "=SUM(AL11)"
    @eval_fn
    def AL10():
        al11_1 = Input_RPS.AL11()
        var_1 = SUM(al11_1)
        return var_1

@register(Input_RPS)
class C11():
    # 'Input_RPS'!C11
    value = "               PGV"

@register(Input_RPS)
class N11():
    # 'Input_RPS'!N11
    value = 0

@register(Input_RPS)
class O11():
    # 'Input_RPS'!O11
    value = 0

@register(Input_RPS)
class P11():
    # 'Input_RPS'!P11
    value = 0

@register(Input_RPS)
class Q11():
    # 'Input_RPS'!Q11
    value = 0

@register(Input_RPS)
class R11():
    # 'Input_RPS'!R11
    value = 0

@register(Input_RPS)
class S11():
    # 'Input_RPS'!S11
    value = 0

@register(Input_RPS)
class C12():
    # 'Input_RPS'!C12
    value = "Wind: "

@register(Input_RPS)
class G12():
    # 'Input_RPS'!G12
    value = 0
    formula = "=SUM(G13:G17)"
    @eval_fn
    def G12():
        range_1 = Input_RPS(7, 13, 7, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H12():
    # 'Input_RPS'!H12
    value = 0
    formula = "=SUM(H13:H17)"
    @eval_fn
    def H12():
        range_1 = Input_RPS(8, 13, 8, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I12():
    # 'Input_RPS'!I12
    value = 0
    formula = "=SUM(I13:I17)"
    @eval_fn
    def I12():
        range_1 = Input_RPS(9, 13, 9, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J12():
    # 'Input_RPS'!J12
    value = 0
    formula = "=SUM(J13:J17)"
    @eval_fn
    def J12():
        range_1 = Input_RPS(10, 13, 10, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K12():
    # 'Input_RPS'!K12
    value = 0
    formula = "=SUM(K13:K17)"
    @eval_fn
    def K12():
        range_1 = Input_RPS(11, 13, 11, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L12():
    # 'Input_RPS'!L12
    value = 0
    formula = "=SUM(L13:L17)"
    @eval_fn
    def L12():
        range_1 = Input_RPS(12, 13, 12, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M12():
    # 'Input_RPS'!M12
    value = 0
    formula = "=SUM(M13:M17)"
    @eval_fn
    def M12():
        range_1 = Input_RPS(13, 13, 13, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N12():
    # 'Input_RPS'!N12
    value = 0
    formula = "=SUM(N13:N17)"
    @eval_fn
    def N12():
        range_1 = Input_RPS(14, 13, 14, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O12():
    # 'Input_RPS'!O12
    value = 0
    formula = "=SUM(O13:O17)"
    @eval_fn
    def O12():
        range_1 = Input_RPS(15, 13, 15, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P12():
    # 'Input_RPS'!P12
    value = 0
    formula = "=SUM(P13:P17)"
    @eval_fn
    def P12():
        range_1 = Input_RPS(16, 13, 16, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q12():
    # 'Input_RPS'!Q12
    value = 0
    formula = "=SUM(Q13:Q17)"
    @eval_fn
    def Q12():
        range_1 = Input_RPS(17, 13, 17, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R12():
    # 'Input_RPS'!R12
    value = 23
    formula = "=SUM(R13:R17)"
    @eval_fn
    def R12():
        range_1 = Input_RPS(18, 13, 18, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S12():
    # 'Input_RPS'!S12
    value = 64024
    formula = "=SUM(S13:S17)"
    @eval_fn
    def S12():
        range_1 = Input_RPS(19, 13, 19, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T12():
    # 'Input_RPS'!T12
    value = 75410
    formula = "=SUM(T13:T17)"
    @eval_fn
    def T12():
        range_1 = Input_RPS(20, 13, 20, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U12():
    # 'Input_RPS'!U12
    value = 121691
    formula = "=SUM(U13:U17)"
    @eval_fn
    def U12():
        range_1 = Input_RPS(21, 13, 21, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V12():
    # 'Input_RPS'!V12
    value = 183864
    formula = "=SUM(V13:V17)"
    @eval_fn
    def V12():
        range_1 = Input_RPS(22, 13, 22, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W12():
    # 'Input_RPS'!W12
    value = 216197

@register(Input_RPS)
class X12():
    # 'Input_RPS'!X12
    value = 0
    formula = "=SUM(X13:X17)"
    @eval_fn
    def X12():
        range_1 = Input_RPS(24, 13, 24, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y12():
    # 'Input_RPS'!Y12
    value = 0
    formula = "=SUM(Y13:Y17)"
    @eval_fn
    def Y12():
        range_1 = Input_RPS(25, 13, 25, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z12():
    # 'Input_RPS'!Z12
    value = 0
    formula = "=SUM(Z13:Z17)"
    @eval_fn
    def Z12():
        range_1 = Input_RPS(26, 13, 26, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA12():
    # 'Input_RPS'!AA12
    value = 0
    formula = "=SUM(AA13:AA17)"
    @eval_fn
    def AA12():
        range_1 = Input_RPS(27, 13, 27, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB12():
    # 'Input_RPS'!AB12
    value = 0
    formula = "=SUM(AB13:AB17)"
    @eval_fn
    def AB12():
        range_1 = Input_RPS(28, 13, 28, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC12():
    # 'Input_RPS'!AC12
    value = 0
    formula = "=SUM(AC13:AC17)"
    @eval_fn
    def AC12():
        range_1 = Input_RPS(29, 13, 29, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD12():
    # 'Input_RPS'!AD12
    value = 0
    formula = "=SUM(AD13:AD17)"
    @eval_fn
    def AD12():
        range_1 = Input_RPS(30, 13, 30, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE12():
    # 'Input_RPS'!AE12
    value = 0
    formula = "=SUM(AE13:AE17)"
    @eval_fn
    def AE12():
        range_1 = Input_RPS(31, 13, 31, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF12():
    # 'Input_RPS'!AF12
    value = 0
    formula = "=SUM(AF13:AF17)"
    @eval_fn
    def AF12():
        range_1 = Input_RPS(32, 13, 32, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG12():
    # 'Input_RPS'!AG12
    value = 0
    formula = "=SUM(AG13:AG17)"
    @eval_fn
    def AG12():
        range_1 = Input_RPS(33, 13, 33, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH12():
    # 'Input_RPS'!AH12
    value = 0
    formula = "=SUM(AH13:AH17)"
    @eval_fn
    def AH12():
        range_1 = Input_RPS(34, 13, 34, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI12():
    # 'Input_RPS'!AI12
    value = 0
    formula = "=SUM(AI13:AI17)"
    @eval_fn
    def AI12():
        range_1 = Input_RPS(35, 13, 35, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ12():
    # 'Input_RPS'!AJ12
    value = 0
    formula = "=SUM(AJ13:AJ17)"
    @eval_fn
    def AJ12():
        range_1 = Input_RPS(36, 13, 36, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK12():
    # 'Input_RPS'!AK12
    value = 0
    formula = "=SUM(AK13:AK17)"
    @eval_fn
    def AK12():
        range_1 = Input_RPS(37, 13, 37, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL12():
    # 'Input_RPS'!AL12
    value = 0
    formula = "=SUM(AL13:AL17)"
    @eval_fn
    def AL12():
        range_1 = Input_RPS(38, 13, 38, 17)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C13():
    # 'Input_RPS'!C13
    value = "           HRD"

@register(Input_RPS)
class N13():
    # 'Input_RPS'!N13
    value = 0

@register(Input_RPS)
class O13():
    # 'Input_RPS'!O13
    value = 0

@register(Input_RPS)
class P13():
    # 'Input_RPS'!P13
    value = 0

@register(Input_RPS)
class Q13():
    # 'Input_RPS'!Q13
    value = 0

@register(Input_RPS)
class C14():
    # 'Input_RPS'!C14
    value = "           Kaheawa Wind Power (KWP)"

@register(Input_RPS)
class N14():
    # 'Input_RPS'!N14
    value = 0

@register(Input_RPS)
class O14():
    # 'Input_RPS'!O14
    value = 0

@register(Input_RPS)
class P14():
    # 'Input_RPS'!P14
    value = 0

@register(Input_RPS)
class Q14():
    # 'Input_RPS'!Q14
    value = 0

@register(Input_RPS)
class C15():
    # 'Input_RPS'!C15
    value = "           Lalamilo Wind Farm"

@register(Input_RPS)
class N15():
    # 'Input_RPS'!N15
    value = 0

@register(Input_RPS)
class O15():
    # 'Input_RPS'!O15
    value = 0

@register(Input_RPS)
class P15():
    # 'Input_RPS'!P15
    value = 0

@register(Input_RPS)
class Q15():
    # 'Input_RPS'!Q15
    value = 0

@register(Input_RPS)
class C16():
    # 'Input_RPS'!C16
    value = "           Pikini Nui"

@register(Input_RPS)
class N16():
    # 'Input_RPS'!N16
    value = 0

@register(Input_RPS)
class O16():
    # 'Input_RPS'!O16
    value = 0

@register(Input_RPS)
class P16():
    # 'Input_RPS'!P16
    value = 0

@register(Input_RPS)
class Q16():
    # 'Input_RPS'!Q16
    value = 0

@register(Input_RPS)
class C17():
    # 'Input_RPS'!C17
    value = "           Other wind including Kamaoa"

@register(Input_RPS)
class N17():
    # 'Input_RPS'!N17
    value = 0

@register(Input_RPS)
class O17():
    # 'Input_RPS'!O17
    value = 0

@register(Input_RPS)
class P17():
    # 'Input_RPS'!P17
    value = 0

@register(Input_RPS)
class Q17():
    # 'Input_RPS'!Q17
    value = 0

@register(Input_RPS)
class R17():
    # 'Input_RPS'!R17
    value = 23

@register(Input_RPS)
class S17():
    # 'Input_RPS'!S17
    value = 64024

@register(Input_RPS)
class T17():
    # 'Input_RPS'!T17
    value = 75410

@register(Input_RPS)
class U17():
    # 'Input_RPS'!U17
    value = 121691

@register(Input_RPS)
class V17():
    # 'Input_RPS'!V17
    value = 183864

@register(Input_RPS)
class C18():
    # 'Input_RPS'!C18
    value = "Biomass: "

@register(Input_RPS)
class G18():
    # 'Input_RPS'!G18
    value = 0
    formula = "=SUM(G19:G20)"
    @eval_fn
    def G18():
        range_1 = Input_RPS(7, 19, 7, 20)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H18():
    # 'Input_RPS'!H18
    value = 0
    formula = "=SUM(H19:H20)"
    @eval_fn
    def H18():
        range_1 = Input_RPS(8, 19, 8, 20)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I18():
    # 'Input_RPS'!I18
    value = 0
    formula = "=SUM(I19:I20)"
    @eval_fn
    def I18():
        range_1 = Input_RPS(9, 19, 9, 20)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J18():
    # 'Input_RPS'!J18
    value = 0
    formula = "=SUM(J19:J20)"
    @eval_fn
    def J18():
        range_1 = Input_RPS(10, 19, 10, 20)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K18():
    # 'Input_RPS'!K18
    value = 0
    formula = "=SUM(K19:K20)"
    @eval_fn
    def K18():
        range_1 = Input_RPS(11, 19, 11, 20)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L18():
    # 'Input_RPS'!L18
    value = 0
    formula = "=SUM(L19:L20)"
    @eval_fn
    def L18():
        range_1 = Input_RPS(12, 19, 12, 20)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M18():
    # 'Input_RPS'!M18
    value = 333000

@register(Input_RPS)
class N18():
    # 'Input_RPS'!N18
    value = 395000

@register(Input_RPS)
class O18():
    # 'Input_RPS'!O18
    value = 326000

@register(Input_RPS)
class P18():
    # 'Input_RPS'!P18
    value = 359011

@register(Input_RPS)
class Q18():
    # 'Input_RPS'!Q18
    value = 360323

@register(Input_RPS)
class R18():
    # 'Input_RPS'!R18
    value = 314614

@register(Input_RPS)
class S18():
    # 'Input_RPS'!S18
    value = 321689

@register(Input_RPS)
class T18():
    # 'Input_RPS'!T18
    value = 302398

@register(Input_RPS)
class U18():
    # 'Input_RPS'!U18
    value = 374569

@register(Input_RPS)
class V18():
    # 'Input_RPS'!V18
    value = 390011

@register(Input_RPS)
class W18():
    # 'Input_RPS'!W18
    value = 385846

@register(Input_RPS)
class C19():
    # 'Input_RPS'!C19
    value = "                  Biomass"

@register(Input_RPS)
class N19():
    # 'Input_RPS'!N19
    value = 0

@register(Input_RPS)
class O19():
    # 'Input_RPS'!O19
    value = 0

@register(Input_RPS)
class C20():
    # 'Input_RPS'!C20
    value = "                  Municipal Solid Waste"

@register(Input_RPS)
class M20():
    # 'Input_RPS'!M20
    value = 40000

@register(Input_RPS)
class N20():
    # 'Input_RPS'!N20
    value = 56000

@register(Input_RPS)
class O20():
    # 'Input_RPS'!O20
    value = 24000

@register(Input_RPS)
class P20():
    # 'Input_RPS'!P20
    value = 0

@register(Input_RPS)
class Q20():
    # 'Input_RPS'!Q20
    value = 0

@register(Input_RPS)
class C21():
    # 'Input_RPS'!C21
    value = "Solar: "

@register(Input_RPS)
class G21():
    # 'Input_RPS'!G21
    value = 0
    formula = "=SUM(G22)"
    @eval_fn
    def G21():
        g22_1 = Input_RPS.G22()
        var_1 = SUM(g22_1)
        return var_1

@register(Input_RPS)
class H21():
    # 'Input_RPS'!H21
    value = 0
    formula = "=SUM(H22)"
    @eval_fn
    def H21():
        h22_1 = Input_RPS.H22()
        var_1 = SUM(h22_1)
        return var_1

@register(Input_RPS)
class I21():
    # 'Input_RPS'!I21
    value = 0
    formula = "=SUM(I22)"
    @eval_fn
    def I21():
        i22_1 = Input_RPS.I22()
        var_1 = SUM(i22_1)
        return var_1

@register(Input_RPS)
class J21():
    # 'Input_RPS'!J21
    value = 0
    formula = "=SUM(J22)"
    @eval_fn
    def J21():
        j22_1 = Input_RPS.J22()
        var_1 = SUM(j22_1)
        return var_1

@register(Input_RPS)
class K21():
    # 'Input_RPS'!K21
    value = 0
    formula = "=SUM(K22)"
    @eval_fn
    def K21():
        k22_1 = Input_RPS.K22()
        var_1 = SUM(k22_1)
        return var_1

@register(Input_RPS)
class L21():
    # 'Input_RPS'!L21
    value = 0
    formula = "=SUM(L22)"
    @eval_fn
    def L21():
        l22_1 = Input_RPS.L22()
        var_1 = SUM(l22_1)
        return var_1

@register(Input_RPS)
class M21():
    # 'Input_RPS'!M21
    value = 400
    formula = "=SUM(M22:M23)"
    @eval_fn
    def M21():
        range_1 = Input_RPS(13, 22, 13, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N21():
    # 'Input_RPS'!N21
    value = 500
    formula = "=SUM(N22:N23)"
    @eval_fn
    def N21():
        range_1 = Input_RPS(14, 22, 14, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O21():
    # 'Input_RPS'!O21
    value = 1700
    formula = "=SUM(O22:O23)"
    @eval_fn
    def O21():
        range_1 = Input_RPS(15, 22, 15, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P21():
    # 'Input_RPS'!P21
    value = 4003
    formula = "=SUM(P22:P23)"
    @eval_fn
    def P21():
        range_1 = Input_RPS(16, 22, 16, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q21():
    # 'Input_RPS'!Q21
    value = 15668
    formula = "=SUM(Q22:Q23)"
    @eval_fn
    def Q21():
        range_1 = Input_RPS(17, 22, 17, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R21():
    # 'Input_RPS'!R21
    value = 28597
    formula = "=SUM(R22:R23)"
    @eval_fn
    def R21():
        range_1 = Input_RPS(18, 22, 18, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S21():
    # 'Input_RPS'!S21
    value = 54391
    formula = "=SUM(S22:S23)"
    @eval_fn
    def S21():
        range_1 = Input_RPS(19, 22, 19, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T21():
    # 'Input_RPS'!T21
    value = 131786
    formula = "=SUM(T22:T23)"
    @eval_fn
    def T21():
        range_1 = Input_RPS(20, 22, 20, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U21():
    # 'Input_RPS'!U21
    value = 276241
    formula = "=SUM(U22:U23)"
    @eval_fn
    def U21():
        range_1 = Input_RPS(21, 22, 21, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V21():
    # 'Input_RPS'!V21
    value = 419020
    formula = "=SUM(V22:V23)"
    @eval_fn
    def V21():
        range_1 = Input_RPS(22, 22, 22, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W21():
    # 'Input_RPS'!W21
    value = 505162
    formula = "=SUM(W22:W23)"
    @eval_fn
    def W21():
        range_1 = Input_RPS(23, 22, 23, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class X21():
    # 'Input_RPS'!X21
    value = 0
    formula = "=SUM(X22:X23)"
    @eval_fn
    def X21():
        range_1 = Input_RPS(24, 22, 24, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y21():
    # 'Input_RPS'!Y21
    value = 0
    formula = "=SUM(Y22:Y23)"
    @eval_fn
    def Y21():
        range_1 = Input_RPS(25, 22, 25, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z21():
    # 'Input_RPS'!Z21
    value = 0
    formula = "=SUM(Z22:Z23)"
    @eval_fn
    def Z21():
        range_1 = Input_RPS(26, 22, 26, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA21():
    # 'Input_RPS'!AA21
    value = 0
    formula = "=SUM(AA22:AA23)"
    @eval_fn
    def AA21():
        range_1 = Input_RPS(27, 22, 27, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB21():
    # 'Input_RPS'!AB21
    value = 0
    formula = "=SUM(AB22:AB23)"
    @eval_fn
    def AB21():
        range_1 = Input_RPS(28, 22, 28, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC21():
    # 'Input_RPS'!AC21
    value = 0
    formula = "=SUM(AC22:AC23)"
    @eval_fn
    def AC21():
        range_1 = Input_RPS(29, 22, 29, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD21():
    # 'Input_RPS'!AD21
    value = 0
    formula = "=SUM(AD22:AD23)"
    @eval_fn
    def AD21():
        range_1 = Input_RPS(30, 22, 30, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE21():
    # 'Input_RPS'!AE21
    value = 0
    formula = "=SUM(AE22:AE23)"
    @eval_fn
    def AE21():
        range_1 = Input_RPS(31, 22, 31, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF21():
    # 'Input_RPS'!AF21
    value = 0
    formula = "=SUM(AF22:AF23)"
    @eval_fn
    def AF21():
        range_1 = Input_RPS(32, 22, 32, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG21():
    # 'Input_RPS'!AG21
    value = 0
    formula = "=SUM(AG22:AG23)"
    @eval_fn
    def AG21():
        range_1 = Input_RPS(33, 22, 33, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH21():
    # 'Input_RPS'!AH21
    value = 0
    formula = "=SUM(AH22:AH23)"
    @eval_fn
    def AH21():
        range_1 = Input_RPS(34, 22, 34, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI21():
    # 'Input_RPS'!AI21
    value = 0
    formula = "=SUM(AI22:AI23)"
    @eval_fn
    def AI21():
        range_1 = Input_RPS(35, 22, 35, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ21():
    # 'Input_RPS'!AJ21
    value = 0
    formula = "=SUM(AJ22:AJ23)"
    @eval_fn
    def AJ21():
        range_1 = Input_RPS(36, 22, 36, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK21():
    # 'Input_RPS'!AK21
    value = 0
    formula = "=SUM(AK22:AK23)"
    @eval_fn
    def AK21():
        range_1 = Input_RPS(37, 22, 37, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL21():
    # 'Input_RPS'!AL21
    value = 0
    formula = "=SUM(AL22:AL23)"
    @eval_fn
    def AL21():
        range_1 = Input_RPS(38, 22, 38, 23)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C22():
    # 'Input_RPS'!C22
    value = "            Photovoltaic"

@register(Input_RPS)
class M22():
    # 'Input_RPS'!M22
    value = 400

@register(Input_RPS)
class N22():
    # 'Input_RPS'!N22
    value = 500

@register(Input_RPS)
class O22():
    # 'Input_RPS'!O22
    value = 1700

@register(Input_RPS)
class P22():
    # 'Input_RPS'!P22
    value = 4003

@register(Input_RPS)
class Q22():
    # 'Input_RPS'!Q22
    value = 15668

@register(Input_RPS)
class R22():
    # 'Input_RPS'!R22
    value = 28597

@register(Input_RPS)
class S22():
    # 'Input_RPS'!S22
    value = 54189

@register(Input_RPS)
class T22():
    # 'Input_RPS'!T22
    value = 125882

@register(Input_RPS)
class U22():
    # 'Input_RPS'!U22
    value = 248938

@register(Input_RPS)
class V22():
    # 'Input_RPS'!V22
    value = 381657

@register(Input_RPS)
class W22():
    # 'Input_RPS'!W22
    value = 464412

@register(Input_RPS)
class C23():
    # 'Input_RPS'!C23
    value = "            Utility Solar"

@register(Input_RPS)
class M23():
    # 'Input_RPS'!M23
    value = 0

@register(Input_RPS)
class N23():
    # 'Input_RPS'!N23
    value = 0

@register(Input_RPS)
class O23():
    # 'Input_RPS'!O23
    value = 0

@register(Input_RPS)
class P23():
    # 'Input_RPS'!P23
    value = 0

@register(Input_RPS)
class Q23():
    # 'Input_RPS'!Q23
    value = 0

@register(Input_RPS)
class R23():
    # 'Input_RPS'!R23
    value = 0

@register(Input_RPS)
class S23():
    # 'Input_RPS'!S23
    value = 202

@register(Input_RPS)
class T23():
    # 'Input_RPS'!T23
    value = 5904

@register(Input_RPS)
class U23():
    # 'Input_RPS'!U23
    value = 27303

@register(Input_RPS)
class V23():
    # 'Input_RPS'!V23
    value = 37363

@register(Input_RPS)
class W23():
    # 'Input_RPS'!W23
    value = 40750

@register(Input_RPS)
class C24():
    # 'Input_RPS'!C24
    value = "Biofuels: "

@register(Input_RPS)
class G24():
    # 'Input_RPS'!G24
    value = 0
    formula = "=SUM(G25)"
    @eval_fn
    def G24():
        g25_1 = Input_RPS.G25()
        var_1 = SUM(g25_1)
        return var_1

@register(Input_RPS)
class H24():
    # 'Input_RPS'!H24
    value = 0
    formula = "=SUM(H25)"
    @eval_fn
    def H24():
        h25_1 = Input_RPS.H25()
        var_1 = SUM(h25_1)
        return var_1

@register(Input_RPS)
class I24():
    # 'Input_RPS'!I24
    value = 0
    formula = "=SUM(I25)"
    @eval_fn
    def I24():
        i25_1 = Input_RPS.I25()
        var_1 = SUM(i25_1)
        return var_1

@register(Input_RPS)
class J24():
    # 'Input_RPS'!J24
    value = 0
    formula = "=SUM(J25)"
    @eval_fn
    def J24():
        j25_1 = Input_RPS.J25()
        var_1 = SUM(j25_1)
        return var_1

@register(Input_RPS)
class K24():
    # 'Input_RPS'!K24
    value = 0
    formula = "=SUM(K25)"
    @eval_fn
    def K24():
        k25_1 = Input_RPS.K25()
        var_1 = SUM(k25_1)
        return var_1

@register(Input_RPS)
class L24():
    # 'Input_RPS'!L24
    value = 0
    formula = "=SUM(L25)"
    @eval_fn
    def L24():
        l25_1 = Input_RPS.L25()
        var_1 = SUM(l25_1)
        return var_1

@register(Input_RPS)
class M24():
    # 'Input_RPS'!M24
    value = 0
    formula = "=SUM(M25)"
    @eval_fn
    def M24():
        m25_1 = Input_RPS.M25()
        var_1 = SUM(m25_1)
        return var_1

@register(Input_RPS)
class N24():
    # 'Input_RPS'!N24
    value = 0

@register(Input_RPS)
class O24():
    # 'Input_RPS'!O24
    value = 0

@register(Input_RPS)
class P24():
    # 'Input_RPS'!P24
    value = 0

@register(Input_RPS)
class Q24():
    # 'Input_RPS'!Q24
    value = 3307

@register(Input_RPS)
class R24():
    # 'Input_RPS'!R24
    value = 1575

@register(Input_RPS)
class S24():
    # 'Input_RPS'!S24
    value = 44722

@register(Input_RPS)
class T24():
    # 'Input_RPS'!T24
    value = 21259

@register(Input_RPS)
class U24():
    # 'Input_RPS'!U24
    value = 28508

@register(Input_RPS)
class V24():
    # 'Input_RPS'!V24
    value = 36175

@register(Input_RPS)
class W24():
    # 'Input_RPS'!W24
    value = 52424

@register(Input_RPS)
class C25():
    # 'Input_RPS'!C25
    value = "            Biodiesel"

@register(Input_RPS)
class N25():
    # 'Input_RPS'!N25
    value = 0

@register(Input_RPS)
class O25():
    # 'Input_RPS'!O25
    value = 0

@register(Input_RPS)
class P25():
    # 'Input_RPS'!P25
    value = 0

@register(Input_RPS)
class A26():
    # 'Input_RPS'!A26
    value = "HELCORenewable Electricity"
    formula = "=CONCATENATE(C26,B26)"
    @eval_fn
    def A26():
        c26_1 = Input_RPS.C26()
        b26_1 = Input_RPS.B26()
        var_1 = CONCATENATE(c26_1, b26_1)
        return var_1

@register(Input_RPS)
class B26():
    # 'Input_RPS'!B26
    value = "Renewable Electricity"

@register(Input_RPS)
class C26():
    # 'Input_RPS'!C26
    value = "HELCO"

@register(Input_RPS)
class D26():
    # 'Input_RPS'!D26
    value = "MWh"

@register(Input_RPS)
class E26():
    # 'Input_RPS'!E26
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Input_RPS)
class F26():
    # 'Input_RPS'!F26
    value = "1999-2004 includes PGV, hydro, wind, other hydro, wind-kamoa, photovoltaic"

@register(Input_RPS)
class G26():
    # 'Input_RPS'!G26
    value = 260000

@register(Input_RPS)
class H26():
    # 'Input_RPS'!H26
    value = 311000

@register(Input_RPS)
class I26():
    # 'Input_RPS'!I26
    value = 274000

@register(Input_RPS)
class J26():
    # 'Input_RPS'!J26
    value = 123000

@register(Input_RPS)
class K26():
    # 'Input_RPS'!K26
    value = 216400

@register(Input_RPS)
class L26():
    # 'Input_RPS'!L26
    value = 256500

@register(Input_RPS)
class M26():
    # 'Input_RPS'!M26
    value = 269600
    formula = "=M27+M33+M35+M44"
    @eval_fn
    def M26():
        m27_1 = Input_RPS.M27()
        m33_1 = Input_RPS.M33()
        var_1 = add(m27_1, m33_1)
        m35_1 = Input_RPS.M35()
        var_2 = add(var_1, m35_1)
        m44_1 = Input_RPS.M44()
        var_3 = add(var_2, m44_1)
        return var_3

@register(Input_RPS)
class N26():
    # 'Input_RPS'!N26
    value = 295200
    formula = "=N27+N33+N35+N44"
    @eval_fn
    def N26():
        n27_1 = Input_RPS.N27()
        n33_1 = Input_RPS.N33()
        var_1 = add(n27_1, n33_1)
        n35_1 = Input_RPS.N35()
        var_2 = add(var_1, n35_1)
        n44_1 = Input_RPS.N44()
        var_3 = add(var_2, n44_1)
        return var_3

@register(Input_RPS)
class O26():
    # 'Input_RPS'!O26
    value = 393100
    formula = "=O27+O33+O35+O44"
    @eval_fn
    def O26():
        o27_1 = Input_RPS.O27()
        o33_1 = Input_RPS.O33()
        var_1 = add(o27_1, o33_1)
        o35_1 = Input_RPS.O35()
        var_2 = add(var_1, o35_1)
        o44_1 = Input_RPS.O44()
        var_3 = add(var_2, o44_1)
        return var_3

@register(Input_RPS)
class P26():
    # 'Input_RPS'!P26
    value = 403486
    formula = "=P27+P33+P35+P44"
    @eval_fn
    def P26():
        p27_1 = Input_RPS.P27()
        p33_1 = Input_RPS.P33()
        var_1 = add(p27_1, p33_1)
        p35_1 = Input_RPS.P35()
        var_2 = add(var_1, p35_1)
        p44_1 = Input_RPS.P44()
        var_3 = add(var_2, p44_1)
        return var_3

@register(Input_RPS)
class Q26():
    # 'Input_RPS'!Q26
    value = 377730
    formula = "=Q27+Q33+Q35+Q44"
    @eval_fn
    def Q26():
        q27_1 = Input_RPS.Q27()
        q33_1 = Input_RPS.Q33()
        var_1 = add(q27_1, q33_1)
        q35_1 = Input_RPS.Q35()
        var_2 = add(var_1, q35_1)
        q44_1 = Input_RPS.Q44()
        var_3 = add(var_2, q44_1)
        return var_3

@register(Input_RPS)
class R26():
    # 'Input_RPS'!R26
    value = 383622
    formula = "=R27+R33+R35+R44"
    @eval_fn
    def R26():
        r27_1 = Input_RPS.R27()
        r33_1 = Input_RPS.R33()
        var_1 = add(r27_1, r33_1)
        r35_1 = Input_RPS.R35()
        var_2 = add(var_1, r35_1)
        r44_1 = Input_RPS.R44()
        var_3 = add(var_2, r44_1)
        return var_3

@register(Input_RPS)
class S26():
    # 'Input_RPS'!S26
    value = 453349
    formula = "=S27+S33+S35+S44"
    @eval_fn
    def S26():
        s27_1 = Input_RPS.S27()
        s33_1 = Input_RPS.S33()
        var_1 = add(s27_1, s33_1)
        s35_1 = Input_RPS.S35()
        var_2 = add(var_1, s35_1)
        s44_1 = Input_RPS.S44()
        var_3 = add(var_2, s44_1)
        return var_3

@register(Input_RPS)
class T26():
    # 'Input_RPS'!T26
    value = 507062
    formula = "=T27+T33+T35+T41+T44+T47"
    @eval_fn
    def T26():
        t27_1 = Input_RPS.T27()
        t33_1 = Input_RPS.T33()
        var_1 = add(t27_1, t33_1)
        t35_1 = Input_RPS.T35()
        var_2 = add(var_1, t35_1)
        t41_1 = Input_RPS.T41()
        var_3 = add(var_2, t41_1)
        t44_1 = Input_RPS.T44()
        var_4 = add(var_3, t44_1)
        t47_1 = Input_RPS.T47()
        var_5 = add(var_4, t47_1)
        return var_5

@register(Input_RPS)
class U26():
    # 'Input_RPS'!U26
    value = 517375
    formula = "=U27+U33+U35+U41+U44+U47"
    @eval_fn
    def U26():
        u27_1 = Input_RPS.U27()
        u33_1 = Input_RPS.U33()
        var_1 = add(u27_1, u33_1)
        u35_1 = Input_RPS.U35()
        var_2 = add(var_1, u35_1)
        u41_1 = Input_RPS.U41()
        var_3 = add(var_2, u41_1)
        u44_1 = Input_RPS.U44()
        var_4 = add(var_3, u44_1)
        u47_1 = Input_RPS.U47()
        var_5 = add(var_4, u47_1)
        return var_5

@register(Input_RPS)
class V26():
    # 'Input_RPS'!V26
    value = 503140
    formula = "=V27+V33+V35+V41+V44+V47"
    @eval_fn
    def V26():
        v27_1 = Input_RPS.V27()
        v33_1 = Input_RPS.V33()
        var_1 = add(v27_1, v33_1)
        v35_1 = Input_RPS.V35()
        var_2 = add(var_1, v35_1)
        v41_1 = Input_RPS.V41()
        var_3 = add(var_2, v41_1)
        v44_1 = Input_RPS.V44()
        var_4 = add(var_3, v44_1)
        v47_1 = Input_RPS.V47()
        var_5 = add(var_4, v47_1)
        return var_5

@register(Input_RPS)
class W26():
    # 'Input_RPS'!W26
    value = 518311
    formula = "=W27+W33+W35+W41+W44+W47"
    @eval_fn
    def W26():
        w27_1 = Input_RPS.W27()
        w33_1 = Input_RPS.W33()
        var_1 = add(w27_1, w33_1)
        w35_1 = Input_RPS.W35()
        var_2 = add(var_1, w35_1)
        w41_1 = Input_RPS.W41()
        var_3 = add(var_2, w41_1)
        w44_1 = Input_RPS.W44()
        var_4 = add(var_3, w44_1)
        w47_1 = Input_RPS.W47()
        var_5 = add(var_4, w47_1)
        return var_5

@register(Input_RPS)
class X26():
    # 'Input_RPS'!X26
    value = 0
    formula = "=X27+X33+X35+X41+X44+X47"
    @eval_fn
    def X26():
        x27_1 = Input_RPS.X27()
        x33_1 = Input_RPS.X33()
        var_1 = add(x27_1, x33_1)
        x35_1 = Input_RPS.X35()
        var_2 = add(var_1, x35_1)
        x41_1 = Input_RPS.X41()
        var_3 = add(var_2, x41_1)
        x44_1 = Input_RPS.X44()
        var_4 = add(var_3, x44_1)
        x47_1 = Input_RPS.X47()
        var_5 = add(var_4, x47_1)
        return var_5

@register(Input_RPS)
class Y26():
    # 'Input_RPS'!Y26
    value = 0
    formula = "=Y27+Y33+Y35+Y41+Y44+Y47"
    @eval_fn
    def Y26():
        y27_1 = Input_RPS.Y27()
        y33_1 = Input_RPS.Y33()
        var_1 = add(y27_1, y33_1)
        y35_1 = Input_RPS.Y35()
        var_2 = add(var_1, y35_1)
        y41_1 = Input_RPS.Y41()
        var_3 = add(var_2, y41_1)
        y44_1 = Input_RPS.Y44()
        var_4 = add(var_3, y44_1)
        y47_1 = Input_RPS.Y47()
        var_5 = add(var_4, y47_1)
        return var_5

@register(Input_RPS)
class Z26():
    # 'Input_RPS'!Z26
    value = 0
    formula = "=Z27+Z33+Z35+Z41+Z44+Z47"
    @eval_fn
    def Z26():
        z27_1 = Input_RPS.Z27()
        z33_1 = Input_RPS.Z33()
        var_1 = add(z27_1, z33_1)
        z35_1 = Input_RPS.Z35()
        var_2 = add(var_1, z35_1)
        z41_1 = Input_RPS.Z41()
        var_3 = add(var_2, z41_1)
        z44_1 = Input_RPS.Z44()
        var_4 = add(var_3, z44_1)
        z47_1 = Input_RPS.Z47()
        var_5 = add(var_4, z47_1)
        return var_5

@register(Input_RPS)
class AA26():
    # 'Input_RPS'!AA26
    value = 0
    formula = "=AA27+AA33+AA35+AA41+AA44+AA47"
    @eval_fn
    def AA26():
        aa27_1 = Input_RPS.AA27()
        aa33_1 = Input_RPS.AA33()
        var_1 = add(aa27_1, aa33_1)
        aa35_1 = Input_RPS.AA35()
        var_2 = add(var_1, aa35_1)
        aa41_1 = Input_RPS.AA41()
        var_3 = add(var_2, aa41_1)
        aa44_1 = Input_RPS.AA44()
        var_4 = add(var_3, aa44_1)
        aa47_1 = Input_RPS.AA47()
        var_5 = add(var_4, aa47_1)
        return var_5

@register(Input_RPS)
class AB26():
    # 'Input_RPS'!AB26
    value = 0
    formula = "=AB27+AB33+AB35+AB41+AB44+AB47"
    @eval_fn
    def AB26():
        ab27_1 = Input_RPS.AB27()
        ab33_1 = Input_RPS.AB33()
        var_1 = add(ab27_1, ab33_1)
        ab35_1 = Input_RPS.AB35()
        var_2 = add(var_1, ab35_1)
        ab41_1 = Input_RPS.AB41()
        var_3 = add(var_2, ab41_1)
        ab44_1 = Input_RPS.AB44()
        var_4 = add(var_3, ab44_1)
        ab47_1 = Input_RPS.AB47()
        var_5 = add(var_4, ab47_1)
        return var_5

@register(Input_RPS)
class AC26():
    # 'Input_RPS'!AC26
    value = 0
    formula = "=AC27+AC33+AC35+AC41+AC44+AC47"
    @eval_fn
    def AC26():
        ac27_1 = Input_RPS.AC27()
        ac33_1 = Input_RPS.AC33()
        var_1 = add(ac27_1, ac33_1)
        ac35_1 = Input_RPS.AC35()
        var_2 = add(var_1, ac35_1)
        ac41_1 = Input_RPS.AC41()
        var_3 = add(var_2, ac41_1)
        ac44_1 = Input_RPS.AC44()
        var_4 = add(var_3, ac44_1)
        ac47_1 = Input_RPS.AC47()
        var_5 = add(var_4, ac47_1)
        return var_5

@register(Input_RPS)
class AD26():
    # 'Input_RPS'!AD26
    value = 0
    formula = "=AD27+AD33+AD35+AD41+AD44+AD47"
    @eval_fn
    def AD26():
        ad27_1 = Input_RPS.AD27()
        ad33_1 = Input_RPS.AD33()
        var_1 = add(ad27_1, ad33_1)
        ad35_1 = Input_RPS.AD35()
        var_2 = add(var_1, ad35_1)
        ad41_1 = Input_RPS.AD41()
        var_3 = add(var_2, ad41_1)
        ad44_1 = Input_RPS.AD44()
        var_4 = add(var_3, ad44_1)
        ad47_1 = Input_RPS.AD47()
        var_5 = add(var_4, ad47_1)
        return var_5

@register(Input_RPS)
class AE26():
    # 'Input_RPS'!AE26
    value = 0
    formula = "=AE27+AE33+AE35+AE41+AE44+AE47"
    @eval_fn
    def AE26():
        ae27_1 = Input_RPS.AE27()
        ae33_1 = Input_RPS.AE33()
        var_1 = add(ae27_1, ae33_1)
        ae35_1 = Input_RPS.AE35()
        var_2 = add(var_1, ae35_1)
        ae41_1 = Input_RPS.AE41()
        var_3 = add(var_2, ae41_1)
        ae44_1 = Input_RPS.AE44()
        var_4 = add(var_3, ae44_1)
        ae47_1 = Input_RPS.AE47()
        var_5 = add(var_4, ae47_1)
        return var_5

@register(Input_RPS)
class AF26():
    # 'Input_RPS'!AF26
    value = 0
    formula = "=AF27+AF33+AF35+AF41+AF44+AF47"
    @eval_fn
    def AF26():
        af27_1 = Input_RPS.AF27()
        af33_1 = Input_RPS.AF33()
        var_1 = add(af27_1, af33_1)
        af35_1 = Input_RPS.AF35()
        var_2 = add(var_1, af35_1)
        af41_1 = Input_RPS.AF41()
        var_3 = add(var_2, af41_1)
        af44_1 = Input_RPS.AF44()
        var_4 = add(var_3, af44_1)
        af47_1 = Input_RPS.AF47()
        var_5 = add(var_4, af47_1)
        return var_5

@register(Input_RPS)
class AG26():
    # 'Input_RPS'!AG26
    value = 0
    formula = "=AG27+AG33+AG35+AG41+AG44+AG47"
    @eval_fn
    def AG26():
        ag27_1 = Input_RPS.AG27()
        ag33_1 = Input_RPS.AG33()
        var_1 = add(ag27_1, ag33_1)
        ag35_1 = Input_RPS.AG35()
        var_2 = add(var_1, ag35_1)
        ag41_1 = Input_RPS.AG41()
        var_3 = add(var_2, ag41_1)
        ag44_1 = Input_RPS.AG44()
        var_4 = add(var_3, ag44_1)
        ag47_1 = Input_RPS.AG47()
        var_5 = add(var_4, ag47_1)
        return var_5

@register(Input_RPS)
class AH26():
    # 'Input_RPS'!AH26
    value = 0
    formula = "=AH27+AH33+AH35+AH41+AH44+AH47"
    @eval_fn
    def AH26():
        ah27_1 = Input_RPS.AH27()
        ah33_1 = Input_RPS.AH33()
        var_1 = add(ah27_1, ah33_1)
        ah35_1 = Input_RPS.AH35()
        var_2 = add(var_1, ah35_1)
        ah41_1 = Input_RPS.AH41()
        var_3 = add(var_2, ah41_1)
        ah44_1 = Input_RPS.AH44()
        var_4 = add(var_3, ah44_1)
        ah47_1 = Input_RPS.AH47()
        var_5 = add(var_4, ah47_1)
        return var_5

@register(Input_RPS)
class AI26():
    # 'Input_RPS'!AI26
    value = 0
    formula = "=AI27+AI33+AI35+AI41+AI44+AI47"
    @eval_fn
    def AI26():
        ai27_1 = Input_RPS.AI27()
        ai33_1 = Input_RPS.AI33()
        var_1 = add(ai27_1, ai33_1)
        ai35_1 = Input_RPS.AI35()
        var_2 = add(var_1, ai35_1)
        ai41_1 = Input_RPS.AI41()
        var_3 = add(var_2, ai41_1)
        ai44_1 = Input_RPS.AI44()
        var_4 = add(var_3, ai44_1)
        ai47_1 = Input_RPS.AI47()
        var_5 = add(var_4, ai47_1)
        return var_5

@register(Input_RPS)
class AJ26():
    # 'Input_RPS'!AJ26
    value = 0
    formula = "=AJ27+AJ33+AJ35+AJ41+AJ44+AJ47"
    @eval_fn
    def AJ26():
        aj27_1 = Input_RPS.AJ27()
        aj33_1 = Input_RPS.AJ33()
        var_1 = add(aj27_1, aj33_1)
        aj35_1 = Input_RPS.AJ35()
        var_2 = add(var_1, aj35_1)
        aj41_1 = Input_RPS.AJ41()
        var_3 = add(var_2, aj41_1)
        aj44_1 = Input_RPS.AJ44()
        var_4 = add(var_3, aj44_1)
        aj47_1 = Input_RPS.AJ47()
        var_5 = add(var_4, aj47_1)
        return var_5

@register(Input_RPS)
class AK26():
    # 'Input_RPS'!AK26
    value = 0
    formula = "=AK27+AK33+AK35+AK41+AK44+AK47"
    @eval_fn
    def AK26():
        ak27_1 = Input_RPS.AK27()
        ak33_1 = Input_RPS.AK33()
        var_1 = add(ak27_1, ak33_1)
        ak35_1 = Input_RPS.AK35()
        var_2 = add(var_1, ak35_1)
        ak41_1 = Input_RPS.AK41()
        var_3 = add(var_2, ak41_1)
        ak44_1 = Input_RPS.AK44()
        var_4 = add(var_3, ak44_1)
        ak47_1 = Input_RPS.AK47()
        var_5 = add(var_4, ak47_1)
        return var_5

@register(Input_RPS)
class AL26():
    # 'Input_RPS'!AL26
    value = 0
    formula = "=AL27+AL33+AL35+AL41+AL44+AL47"
    @eval_fn
    def AL26():
        al27_1 = Input_RPS.AL27()
        al33_1 = Input_RPS.AL33()
        var_1 = add(al27_1, al33_1)
        al35_1 = Input_RPS.AL35()
        var_2 = add(var_1, al35_1)
        al41_1 = Input_RPS.AL41()
        var_3 = add(var_2, al41_1)
        al44_1 = Input_RPS.AL44()
        var_4 = add(var_3, al44_1)
        al47_1 = Input_RPS.AL47()
        var_5 = add(var_4, al47_1)
        return var_5

@register(Input_RPS)
class C27():
    # 'Input_RPS'!C27
    value = "Hydro:"

@register(Input_RPS)
class G27():
    # 'Input_RPS'!G27
    value = 0
    formula = "=SUM(G28:G32)"
    @eval_fn
    def G27():
        range_1 = Input_RPS(7, 28, 7, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H27():
    # 'Input_RPS'!H27
    value = 0
    formula = "=SUM(H28:H32)"
    @eval_fn
    def H27():
        range_1 = Input_RPS(8, 28, 8, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I27():
    # 'Input_RPS'!I27
    value = 0
    formula = "=SUM(I28:I32)"
    @eval_fn
    def I27():
        range_1 = Input_RPS(9, 28, 9, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J27():
    # 'Input_RPS'!J27
    value = 0
    formula = "=SUM(J28:J32)"
    @eval_fn
    def J27():
        range_1 = Input_RPS(10, 28, 10, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K27():
    # 'Input_RPS'!K27
    value = 0
    formula = "=SUM(K28:K32)"
    @eval_fn
    def K27():
        range_1 = Input_RPS(11, 28, 11, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L27():
    # 'Input_RPS'!L27
    value = 0
    formula = "=SUM(L28:L32)"
    @eval_fn
    def L27():
        range_1 = Input_RPS(12, 28, 12, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M27():
    # 'Input_RPS'!M27
    value = 40000
    formula = "=SUM(M28:M32)"
    @eval_fn
    def M27():
        range_1 = Input_RPS(13, 28, 13, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N27():
    # 'Input_RPS'!N27
    value = 56000
    formula = "=SUM(N28:N32)"
    @eval_fn
    def N27():
        range_1 = Input_RPS(14, 28, 14, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O27():
    # 'Input_RPS'!O27
    value = 42300
    formula = "=SUM(O28:O32)"
    @eval_fn
    def O27():
        range_1 = Input_RPS(15, 28, 15, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P27():
    # 'Input_RPS'!P27
    value = 36053

@register(Input_RPS)
class Q27():
    # 'Input_RPS'!Q27
    value = 59889

@register(Input_RPS)
class R27():
    # 'Input_RPS'!R27
    value = 29189

@register(Input_RPS)
class S27():
    # 'Input_RPS'!S27
    value = 45300

@register(Input_RPS)
class T27():
    # 'Input_RPS'!T27
    value = 57613

@register(Input_RPS)
class U27():
    # 'Input_RPS'!U27
    value = 35410

@register(Input_RPS)
class V27():
    # 'Input_RPS'!V27
    value = 43005

@register(Input_RPS)
class W27():
    # 'Input_RPS'!W27
    value = 63275

@register(Input_RPS)
class X27():
    # 'Input_RPS'!X27
    value = 0
    formula = "=SUM(X28:X32)"
    @eval_fn
    def X27():
        range_1 = Input_RPS(24, 28, 24, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y27():
    # 'Input_RPS'!Y27
    value = 0
    formula = "=SUM(Y28:Y32)"
    @eval_fn
    def Y27():
        range_1 = Input_RPS(25, 28, 25, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z27():
    # 'Input_RPS'!Z27
    value = 0
    formula = "=SUM(Z28:Z32)"
    @eval_fn
    def Z27():
        range_1 = Input_RPS(26, 28, 26, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA27():
    # 'Input_RPS'!AA27
    value = 0
    formula = "=SUM(AA28:AA32)"
    @eval_fn
    def AA27():
        range_1 = Input_RPS(27, 28, 27, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB27():
    # 'Input_RPS'!AB27
    value = 0
    formula = "=SUM(AB28:AB32)"
    @eval_fn
    def AB27():
        range_1 = Input_RPS(28, 28, 28, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC27():
    # 'Input_RPS'!AC27
    value = 0
    formula = "=SUM(AC28:AC32)"
    @eval_fn
    def AC27():
        range_1 = Input_RPS(29, 28, 29, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD27():
    # 'Input_RPS'!AD27
    value = 0
    formula = "=SUM(AD28:AD32)"
    @eval_fn
    def AD27():
        range_1 = Input_RPS(30, 28, 30, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE27():
    # 'Input_RPS'!AE27
    value = 0
    formula = "=SUM(AE28:AE32)"
    @eval_fn
    def AE27():
        range_1 = Input_RPS(31, 28, 31, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF27():
    # 'Input_RPS'!AF27
    value = 0
    formula = "=SUM(AF28:AF32)"
    @eval_fn
    def AF27():
        range_1 = Input_RPS(32, 28, 32, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG27():
    # 'Input_RPS'!AG27
    value = 0
    formula = "=SUM(AG28:AG32)"
    @eval_fn
    def AG27():
        range_1 = Input_RPS(33, 28, 33, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH27():
    # 'Input_RPS'!AH27
    value = 0
    formula = "=SUM(AH28:AH32)"
    @eval_fn
    def AH27():
        range_1 = Input_RPS(34, 28, 34, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI27():
    # 'Input_RPS'!AI27
    value = 0
    formula = "=SUM(AI28:AI32)"
    @eval_fn
    def AI27():
        range_1 = Input_RPS(35, 28, 35, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ27():
    # 'Input_RPS'!AJ27
    value = 0
    formula = "=SUM(AJ28:AJ32)"
    @eval_fn
    def AJ27():
        range_1 = Input_RPS(36, 28, 36, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK27():
    # 'Input_RPS'!AK27
    value = 0
    formula = "=SUM(AK28:AK32)"
    @eval_fn
    def AK27():
        range_1 = Input_RPS(37, 28, 37, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL27():
    # 'Input_RPS'!AL27
    value = 0
    formula = "=SUM(AL28:AL32)"
    @eval_fn
    def AL27():
        range_1 = Input_RPS(38, 28, 38, 32)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C28():
    # 'Input_RPS'!C28
    value = "               Hydro-Wailuku"

@register(Input_RPS)
class M28():
    # 'Input_RPS'!M28
    value = 30000

@register(Input_RPS)
class N28():
    # 'Input_RPS'!N28
    value = 31000

@register(Input_RPS)
class O28():
    # 'Input_RPS'!O28
    value = 27000

@register(Input_RPS)
class C29():
    # 'Input_RPS'!C29
    value = "               Small Hydro"

@register(Input_RPS)
class M29():
    # 'Input_RPS'!M29
    value = 1000

@register(Input_RPS)
class N29():
    # 'Input_RPS'!N29
    value = 1000

@register(Input_RPS)
class O29():
    # 'Input_RPS'!O29
    value = 300

@register(Input_RPS)
class C30():
    # 'Input_RPS'!C30
    value = "               Hydro-Helco owned"

@register(Input_RPS)
class M30():
    # 'Input_RPS'!M30
    value = 9000

@register(Input_RPS)
class N30():
    # 'Input_RPS'!N30
    value = 24000

@register(Input_RPS)
class O30():
    # 'Input_RPS'!O30
    value = 15000

@register(Input_RPS)
class C31():
    # 'Input_RPS'!C31
    value = "               Biomass & Hyrdro HC&S"

@register(Input_RPS)
class N31():
    # 'Input_RPS'!N31
    value = 0

@register(Input_RPS)
class O31():
    # 'Input_RPS'!O31
    value = 0

@register(Input_RPS)
class C33():
    # 'Input_RPS'!C33
    value = "Geothermal:"

@register(Input_RPS)
class G33():
    # 'Input_RPS'!G33
    value = 0
    formula = "=SUM(G34)"
    @eval_fn
    def G33():
        g34_1 = Input_RPS.G34()
        var_1 = SUM(g34_1)
        return var_1

@register(Input_RPS)
class H33():
    # 'Input_RPS'!H33
    value = 0
    formula = "=SUM(H34)"
    @eval_fn
    def H33():
        h34_1 = Input_RPS.H34()
        var_1 = SUM(h34_1)
        return var_1

@register(Input_RPS)
class I33():
    # 'Input_RPS'!I33
    value = 0
    formula = "=SUM(I34)"
    @eval_fn
    def I33():
        i34_1 = Input_RPS.I34()
        var_1 = SUM(i34_1)
        return var_1

@register(Input_RPS)
class J33():
    # 'Input_RPS'!J33
    value = 0
    formula = "=SUM(J34)"
    @eval_fn
    def J33():
        j34_1 = Input_RPS.J34()
        var_1 = SUM(j34_1)
        return var_1

@register(Input_RPS)
class K33():
    # 'Input_RPS'!K33
    value = 0
    formula = "=SUM(K34)"
    @eval_fn
    def K33():
        k34_1 = Input_RPS.K34()
        var_1 = SUM(k34_1)
        return var_1

@register(Input_RPS)
class L33():
    # 'Input_RPS'!L33
    value = 0
    formula = "=SUM(L34)"
    @eval_fn
    def L33():
        l34_1 = Input_RPS.L34()
        var_1 = SUM(l34_1)
        return var_1

@register(Input_RPS)
class M33():
    # 'Input_RPS'!M33
    value = 221000

@register(Input_RPS)
class N33():
    # 'Input_RPS'!N33
    value = 212000
    formula = "=N34"
    @eval_fn
    def N33():
        n34_1 = Input_RPS.N34()
        return n34_1

@register(Input_RPS)
class O33():
    # 'Input_RPS'!O33
    value = 230000
    formula = "=O34"
    @eval_fn
    def O33():
        o34_1 = Input_RPS.O34()
        return o34_1

@register(Input_RPS)
class P33():
    # 'Input_RPS'!P33
    value = 234334

@register(Input_RPS)
class Q33():
    # 'Input_RPS'!Q33
    value = 167591

@register(Input_RPS)
class R33():
    # 'Input_RPS'!R33
    value = 201587

@register(Input_RPS)
class S33():
    # 'Input_RPS'!S33
    value = 232906

@register(Input_RPS)
class T33():
    # 'Input_RPS'!T33
    value = 266234

@register(Input_RPS)
class U33():
    # 'Input_RPS'!U33
    value = 281417

@register(Input_RPS)
class V33():
    # 'Input_RPS'!V33
    value = 255027

@register(Input_RPS)
class W33():
    # 'Input_RPS'!W33
    value = 230495

@register(Input_RPS)
class X33():
    # 'Input_RPS'!X33
    value = 0
    formula = "=SUM(X34)"
    @eval_fn
    def X33():
        x34_1 = Input_RPS.X34()
        var_1 = SUM(x34_1)
        return var_1

@register(Input_RPS)
class Y33():
    # 'Input_RPS'!Y33
    value = 0
    formula = "=SUM(Y34)"
    @eval_fn
    def Y33():
        y34_1 = Input_RPS.Y34()
        var_1 = SUM(y34_1)
        return var_1

@register(Input_RPS)
class Z33():
    # 'Input_RPS'!Z33
    value = 0
    formula = "=SUM(Z34)"
    @eval_fn
    def Z33():
        z34_1 = Input_RPS.Z34()
        var_1 = SUM(z34_1)
        return var_1

@register(Input_RPS)
class AA33():
    # 'Input_RPS'!AA33
    value = 0
    formula = "=SUM(AA34)"
    @eval_fn
    def AA33():
        aa34_1 = Input_RPS.AA34()
        var_1 = SUM(aa34_1)
        return var_1

@register(Input_RPS)
class AB33():
    # 'Input_RPS'!AB33
    value = 0
    formula = "=SUM(AB34)"
    @eval_fn
    def AB33():
        ab34_1 = Input_RPS.AB34()
        var_1 = SUM(ab34_1)
        return var_1

@register(Input_RPS)
class AC33():
    # 'Input_RPS'!AC33
    value = 0
    formula = "=SUM(AC34)"
    @eval_fn
    def AC33():
        ac34_1 = Input_RPS.AC34()
        var_1 = SUM(ac34_1)
        return var_1

@register(Input_RPS)
class AD33():
    # 'Input_RPS'!AD33
    value = 0
    formula = "=SUM(AD34)"
    @eval_fn
    def AD33():
        ad34_1 = Input_RPS.AD34()
        var_1 = SUM(ad34_1)
        return var_1

@register(Input_RPS)
class AE33():
    # 'Input_RPS'!AE33
    value = 0
    formula = "=SUM(AE34)"
    @eval_fn
    def AE33():
        ae34_1 = Input_RPS.AE34()
        var_1 = SUM(ae34_1)
        return var_1

@register(Input_RPS)
class AF33():
    # 'Input_RPS'!AF33
    value = 0
    formula = "=SUM(AF34)"
    @eval_fn
    def AF33():
        af34_1 = Input_RPS.AF34()
        var_1 = SUM(af34_1)
        return var_1

@register(Input_RPS)
class AG33():
    # 'Input_RPS'!AG33
    value = 0
    formula = "=SUM(AG34)"
    @eval_fn
    def AG33():
        ag34_1 = Input_RPS.AG34()
        var_1 = SUM(ag34_1)
        return var_1

@register(Input_RPS)
class AH33():
    # 'Input_RPS'!AH33
    value = 0
    formula = "=SUM(AH34)"
    @eval_fn
    def AH33():
        ah34_1 = Input_RPS.AH34()
        var_1 = SUM(ah34_1)
        return var_1

@register(Input_RPS)
class AI33():
    # 'Input_RPS'!AI33
    value = 0
    formula = "=SUM(AI34)"
    @eval_fn
    def AI33():
        ai34_1 = Input_RPS.AI34()
        var_1 = SUM(ai34_1)
        return var_1

@register(Input_RPS)
class AJ33():
    # 'Input_RPS'!AJ33
    value = 0
    formula = "=SUM(AJ34)"
    @eval_fn
    def AJ33():
        aj34_1 = Input_RPS.AJ34()
        var_1 = SUM(aj34_1)
        return var_1

@register(Input_RPS)
class AK33():
    # 'Input_RPS'!AK33
    value = 0
    formula = "=SUM(AK34)"
    @eval_fn
    def AK33():
        ak34_1 = Input_RPS.AK34()
        var_1 = SUM(ak34_1)
        return var_1

@register(Input_RPS)
class AL33():
    # 'Input_RPS'!AL33
    value = 0
    formula = "=SUM(AL34)"
    @eval_fn
    def AL33():
        al34_1 = Input_RPS.AL34()
        var_1 = SUM(al34_1)
        return var_1

@register(Input_RPS)
class C34():
    # 'Input_RPS'!C34
    value = "               PGV"

@register(Input_RPS)
class M34():
    # 'Input_RPS'!M34
    value = 221000

@register(Input_RPS)
class N34():
    # 'Input_RPS'!N34
    value = 212000

@register(Input_RPS)
class O34():
    # 'Input_RPS'!O34
    value = 230000

@register(Input_RPS)
class C35():
    # 'Input_RPS'!C35
    value = "Wind: "

@register(Input_RPS)
class G35():
    # 'Input_RPS'!G35
    value = 0
    formula = "=SUM(G36:G40)"
    @eval_fn
    def G35():
        range_1 = Input_RPS(7, 36, 7, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H35():
    # 'Input_RPS'!H35
    value = 0
    formula = "=SUM(H36:H40)"
    @eval_fn
    def H35():
        range_1 = Input_RPS(8, 36, 8, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I35():
    # 'Input_RPS'!I35
    value = 0
    formula = "=SUM(I36:I40)"
    @eval_fn
    def I35():
        range_1 = Input_RPS(9, 36, 9, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J35():
    # 'Input_RPS'!J35
    value = 0
    formula = "=SUM(J36:J40)"
    @eval_fn
    def J35():
        range_1 = Input_RPS(10, 36, 10, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K35():
    # 'Input_RPS'!K35
    value = 0
    formula = "=SUM(K36:K40)"
    @eval_fn
    def K35():
        range_1 = Input_RPS(11, 36, 11, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L35():
    # 'Input_RPS'!L35
    value = 0
    formula = "=SUM(L36:L40)"
    @eval_fn
    def L35():
        range_1 = Input_RPS(12, 36, 12, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M35():
    # 'Input_RPS'!M35
    value = 7000
    formula = "=SUM(M36:M40)"
    @eval_fn
    def M35():
        range_1 = Input_RPS(13, 36, 13, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N35():
    # 'Input_RPS'!N35
    value = 25000
    formula = "=SUM(N36:N40)"
    @eval_fn
    def N35():
        range_1 = Input_RPS(14, 36, 14, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O35():
    # 'Input_RPS'!O35
    value = 116400
    formula = "=SUM(O36:O40)"
    @eval_fn
    def O35():
        range_1 = Input_RPS(15, 36, 15, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P35():
    # 'Input_RPS'!P35
    value = 128306

@register(Input_RPS)
class Q35():
    # 'Input_RPS'!Q35
    value = 140687

@register(Input_RPS)
class R35():
    # 'Input_RPS'!R35
    value = 140956

@register(Input_RPS)
class S35():
    # 'Input_RPS'!S35
    value = 157329

@register(Input_RPS)
class T35():
    # 'Input_RPS'!T35
    value = 154688

@register(Input_RPS)
class U35():
    # 'Input_RPS'!U35
    value = 151552

@register(Input_RPS)
class V35():
    # 'Input_RPS'!V35
    value = 136096

@register(Input_RPS)
class W35():
    # 'Input_RPS'!W35
    value = 132293

@register(Input_RPS)
class X35():
    # 'Input_RPS'!X35
    value = 0
    formula = "=SUM(X36:X40)"
    @eval_fn
    def X35():
        range_1 = Input_RPS(24, 36, 24, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y35():
    # 'Input_RPS'!Y35
    value = 0
    formula = "=SUM(Y36:Y40)"
    @eval_fn
    def Y35():
        range_1 = Input_RPS(25, 36, 25, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z35():
    # 'Input_RPS'!Z35
    value = 0
    formula = "=SUM(Z36:Z40)"
    @eval_fn
    def Z35():
        range_1 = Input_RPS(26, 36, 26, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA35():
    # 'Input_RPS'!AA35
    value = 0
    formula = "=SUM(AA36:AA40)"
    @eval_fn
    def AA35():
        range_1 = Input_RPS(27, 36, 27, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB35():
    # 'Input_RPS'!AB35
    value = 0
    formula = "=SUM(AB36:AB40)"
    @eval_fn
    def AB35():
        range_1 = Input_RPS(28, 36, 28, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC35():
    # 'Input_RPS'!AC35
    value = 0
    formula = "=SUM(AC36:AC40)"
    @eval_fn
    def AC35():
        range_1 = Input_RPS(29, 36, 29, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD35():
    # 'Input_RPS'!AD35
    value = 0
    formula = "=SUM(AD36:AD40)"
    @eval_fn
    def AD35():
        range_1 = Input_RPS(30, 36, 30, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE35():
    # 'Input_RPS'!AE35
    value = 0
    formula = "=SUM(AE36:AE40)"
    @eval_fn
    def AE35():
        range_1 = Input_RPS(31, 36, 31, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF35():
    # 'Input_RPS'!AF35
    value = 0
    formula = "=SUM(AF36:AF40)"
    @eval_fn
    def AF35():
        range_1 = Input_RPS(32, 36, 32, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG35():
    # 'Input_RPS'!AG35
    value = 0
    formula = "=SUM(AG36:AG40)"
    @eval_fn
    def AG35():
        range_1 = Input_RPS(33, 36, 33, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH35():
    # 'Input_RPS'!AH35
    value = 0
    formula = "=SUM(AH36:AH40)"
    @eval_fn
    def AH35():
        range_1 = Input_RPS(34, 36, 34, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI35():
    # 'Input_RPS'!AI35
    value = 0
    formula = "=SUM(AI36:AI40)"
    @eval_fn
    def AI35():
        range_1 = Input_RPS(35, 36, 35, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ35():
    # 'Input_RPS'!AJ35
    value = 0
    formula = "=SUM(AJ36:AJ40)"
    @eval_fn
    def AJ35():
        range_1 = Input_RPS(36, 36, 36, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK35():
    # 'Input_RPS'!AK35
    value = 0
    formula = "=SUM(AK36:AK40)"
    @eval_fn
    def AK35():
        range_1 = Input_RPS(37, 36, 37, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL35():
    # 'Input_RPS'!AL35
    value = 0
    formula = "=SUM(AL36:AL40)"
    @eval_fn
    def AL35():
        range_1 = Input_RPS(38, 36, 38, 40)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C36():
    # 'Input_RPS'!C36
    value = "           HRD"

@register(Input_RPS)
class M36():
    # 'Input_RPS'!M36
    value = 0

@register(Input_RPS)
class N36():
    # 'Input_RPS'!N36
    value = 23000

@register(Input_RPS)
class O36():
    # 'Input_RPS'!O36
    value = 34000

@register(Input_RPS)
class C37():
    # 'Input_RPS'!C37
    value = "           Kaheawa Wind Power (KWP)"

@register(Input_RPS)
class M37():
    # 'Input_RPS'!M37
    value = 0

@register(Input_RPS)
class N37():
    # 'Input_RPS'!N37
    value = 0

@register(Input_RPS)
class O37():
    # 'Input_RPS'!O37
    value = 0

@register(Input_RPS)
class C38():
    # 'Input_RPS'!C38
    value = "           Lalamilo Wind Farm"

@register(Input_RPS)
class M38():
    # 'Input_RPS'!M38
    value = 2000

@register(Input_RPS)
class N38():
    # 'Input_RPS'!N38
    value = 1000

@register(Input_RPS)
class O38():
    # 'Input_RPS'!O38
    value = 400

@register(Input_RPS)
class C39():
    # 'Input_RPS'!C39
    value = "           Pikini Nui"

@register(Input_RPS)
class M39():
    # 'Input_RPS'!M39
    value = 5000

@register(Input_RPS)
class N39():
    # 'Input_RPS'!N39
    value = 0

@register(Input_RPS)
class O39():
    # 'Input_RPS'!O39
    value = 82000

@register(Input_RPS)
class C40():
    # 'Input_RPS'!C40
    value = "           Other wind including Kamaoa"

@register(Input_RPS)
class N40():
    # 'Input_RPS'!N40
    value = 1000

@register(Input_RPS)
class O40():
    # 'Input_RPS'!O40
    value = 0

@register(Input_RPS)
class C41():
    # 'Input_RPS'!C41
    value = "Biomass: "

@register(Input_RPS)
class G41():
    # 'Input_RPS'!G41
    value = 0
    formula = "=SUM(G42:G43)"
    @eval_fn
    def G41():
        range_1 = Input_RPS(7, 42, 7, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H41():
    # 'Input_RPS'!H41
    value = 0
    formula = "=SUM(H42:H43)"
    @eval_fn
    def H41():
        range_1 = Input_RPS(8, 42, 8, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I41():
    # 'Input_RPS'!I41
    value = 0
    formula = "=SUM(I42:I43)"
    @eval_fn
    def I41():
        range_1 = Input_RPS(9, 42, 9, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J41():
    # 'Input_RPS'!J41
    value = 0
    formula = "=SUM(J42:J43)"
    @eval_fn
    def J41():
        range_1 = Input_RPS(10, 42, 10, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K41():
    # 'Input_RPS'!K41
    value = 0
    formula = "=SUM(K42:K43)"
    @eval_fn
    def K41():
        range_1 = Input_RPS(11, 42, 11, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L41():
    # 'Input_RPS'!L41
    value = 0
    formula = "=SUM(L42:L43)"
    @eval_fn
    def L41():
        range_1 = Input_RPS(12, 42, 12, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M41():
    # 'Input_RPS'!M41
    value = 0
    formula = "=SUM(M42:M43)"
    @eval_fn
    def M41():
        range_1 = Input_RPS(13, 42, 13, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N41():
    # 'Input_RPS'!N41
    value = 0
    formula = "=SUM(N42:N43)"
    @eval_fn
    def N41():
        range_1 = Input_RPS(14, 42, 14, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O41():
    # 'Input_RPS'!O41
    value = 0
    formula = "=SUM(O42:O43)"
    @eval_fn
    def O41():
        range_1 = Input_RPS(15, 42, 15, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P41():
    # 'Input_RPS'!P41
    value = 0
    formula = "=SUM(P42:P43)"
    @eval_fn
    def P41():
        range_1 = Input_RPS(16, 42, 16, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q41():
    # 'Input_RPS'!Q41
    value = 0
    formula = "=SUM(Q42:Q43)"
    @eval_fn
    def Q41():
        range_1 = Input_RPS(17, 42, 17, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R41():
    # 'Input_RPS'!R41
    value = 0
    formula = "=SUM(R42:R43)"
    @eval_fn
    def R41():
        range_1 = Input_RPS(18, 42, 18, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S41():
    # 'Input_RPS'!S41
    value = 0
    formula = "=SUM(S42:S43)"
    @eval_fn
    def S41():
        range_1 = Input_RPS(19, 42, 19, 43)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C42():
    # 'Input_RPS'!C42
    value = "                  Biomass"

@register(Input_RPS)
class N42():
    # 'Input_RPS'!N42
    value = 0

@register(Input_RPS)
class O42():
    # 'Input_RPS'!O42
    value = 0

@register(Input_RPS)
class P42():
    # 'Input_RPS'!P42
    value = 0

@register(Input_RPS)
class Q42():
    # 'Input_RPS'!Q42
    value = 0

@register(Input_RPS)
class R42():
    # 'Input_RPS'!R42
    value = 0

@register(Input_RPS)
class S42():
    # 'Input_RPS'!S42
    value = 0

@register(Input_RPS)
class C43():
    # 'Input_RPS'!C43
    value = "                  Municipal Solid Waste"

@register(Input_RPS)
class N43():
    # 'Input_RPS'!N43
    value = 0

@register(Input_RPS)
class O43():
    # 'Input_RPS'!O43
    value = 0

@register(Input_RPS)
class P43():
    # 'Input_RPS'!P43
    value = 0

@register(Input_RPS)
class Q43():
    # 'Input_RPS'!Q43
    value = 0

@register(Input_RPS)
class R43():
    # 'Input_RPS'!R43
    value = 0

@register(Input_RPS)
class S43():
    # 'Input_RPS'!S43
    value = 0

@register(Input_RPS)
class C44():
    # 'Input_RPS'!C44
    value = "Solar: "

@register(Input_RPS)
class G44():
    # 'Input_RPS'!G44
    value = 0
    formula = "=SUM(G45)"
    @eval_fn
    def G44():
        g45_1 = Input_RPS.G45()
        var_1 = SUM(g45_1)
        return var_1

@register(Input_RPS)
class H44():
    # 'Input_RPS'!H44
    value = 0
    formula = "=SUM(H45)"
    @eval_fn
    def H44():
        h45_1 = Input_RPS.H45()
        var_1 = SUM(h45_1)
        return var_1

@register(Input_RPS)
class I44():
    # 'Input_RPS'!I44
    value = 0
    formula = "=SUM(I45)"
    @eval_fn
    def I44():
        i45_1 = Input_RPS.I45()
        var_1 = SUM(i45_1)
        return var_1

@register(Input_RPS)
class J44():
    # 'Input_RPS'!J44
    value = 0
    formula = "=SUM(J45)"
    @eval_fn
    def J44():
        j45_1 = Input_RPS.J45()
        var_1 = SUM(j45_1)
        return var_1

@register(Input_RPS)
class K44():
    # 'Input_RPS'!K44
    value = 0
    formula = "=SUM(K45)"
    @eval_fn
    def K44():
        k45_1 = Input_RPS.K45()
        var_1 = SUM(k45_1)
        return var_1

@register(Input_RPS)
class L44():
    # 'Input_RPS'!L44
    value = 0
    formula = "=SUM(L45)"
    @eval_fn
    def L44():
        l45_1 = Input_RPS.L45()
        var_1 = SUM(l45_1)
        return var_1

@register(Input_RPS)
class M44():
    # 'Input_RPS'!M44
    value = 1600
    formula = "=SUM(M45:M46)"
    @eval_fn
    def M44():
        range_1 = Input_RPS(13, 45, 13, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N44():
    # 'Input_RPS'!N44
    value = 2200
    formula = "=SUM(N45:N46)"
    @eval_fn
    def N44():
        range_1 = Input_RPS(14, 45, 14, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O44():
    # 'Input_RPS'!O44
    value = 4400
    formula = "=SUM(O45:O46)"
    @eval_fn
    def O44():
        range_1 = Input_RPS(15, 45, 15, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P44():
    # 'Input_RPS'!P44
    value = 4793
    formula = "=SUM(P45:P46)"
    @eval_fn
    def P44():
        range_1 = Input_RPS(16, 45, 16, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q44():
    # 'Input_RPS'!Q44
    value = 9563
    formula = "=SUM(Q45:Q46)"
    @eval_fn
    def Q44():
        range_1 = Input_RPS(17, 45, 17, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R44():
    # 'Input_RPS'!R44
    value = 11890
    formula = "=SUM(R45:R46)"
    @eval_fn
    def R44():
        range_1 = Input_RPS(18, 45, 18, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S44():
    # 'Input_RPS'!S44
    value = 17814
    formula = "=SUM(S45:S46)"
    @eval_fn
    def S44():
        range_1 = Input_RPS(19, 45, 19, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T44():
    # 'Input_RPS'!T44
    value = 28527
    formula = "=SUM(T45:T46)"
    @eval_fn
    def T44():
        range_1 = Input_RPS(20, 45, 20, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U44():
    # 'Input_RPS'!U44
    value = 48996
    formula = "=SUM(U45:U46)"
    @eval_fn
    def U44():
        range_1 = Input_RPS(21, 45, 21, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V44():
    # 'Input_RPS'!V44
    value = 69012
    formula = "=SUM(V45:V46)"
    @eval_fn
    def V44():
        range_1 = Input_RPS(22, 45, 22, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W44():
    # 'Input_RPS'!W44
    value = 92248
    formula = "=SUM(W45:W46)"
    @eval_fn
    def W44():
        range_1 = Input_RPS(23, 45, 23, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class X44():
    # 'Input_RPS'!X44
    value = 0
    formula = "=SUM(X45:X46)"
    @eval_fn
    def X44():
        range_1 = Input_RPS(24, 45, 24, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y44():
    # 'Input_RPS'!Y44
    value = 0
    formula = "=SUM(Y45:Y46)"
    @eval_fn
    def Y44():
        range_1 = Input_RPS(25, 45, 25, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z44():
    # 'Input_RPS'!Z44
    value = 0
    formula = "=SUM(Z45:Z46)"
    @eval_fn
    def Z44():
        range_1 = Input_RPS(26, 45, 26, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA44():
    # 'Input_RPS'!AA44
    value = 0
    formula = "=SUM(AA45:AA46)"
    @eval_fn
    def AA44():
        range_1 = Input_RPS(27, 45, 27, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB44():
    # 'Input_RPS'!AB44
    value = 0
    formula = "=SUM(AB45:AB46)"
    @eval_fn
    def AB44():
        range_1 = Input_RPS(28, 45, 28, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC44():
    # 'Input_RPS'!AC44
    value = 0
    formula = "=SUM(AC45:AC46)"
    @eval_fn
    def AC44():
        range_1 = Input_RPS(29, 45, 29, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD44():
    # 'Input_RPS'!AD44
    value = 0
    formula = "=SUM(AD45:AD46)"
    @eval_fn
    def AD44():
        range_1 = Input_RPS(30, 45, 30, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE44():
    # 'Input_RPS'!AE44
    value = 0
    formula = "=SUM(AE45:AE46)"
    @eval_fn
    def AE44():
        range_1 = Input_RPS(31, 45, 31, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF44():
    # 'Input_RPS'!AF44
    value = 0
    formula = "=SUM(AF45:AF46)"
    @eval_fn
    def AF44():
        range_1 = Input_RPS(32, 45, 32, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG44():
    # 'Input_RPS'!AG44
    value = 0
    formula = "=SUM(AG45:AG46)"
    @eval_fn
    def AG44():
        range_1 = Input_RPS(33, 45, 33, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH44():
    # 'Input_RPS'!AH44
    value = 0
    formula = "=SUM(AH45:AH46)"
    @eval_fn
    def AH44():
        range_1 = Input_RPS(34, 45, 34, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI44():
    # 'Input_RPS'!AI44
    value = 0
    formula = "=SUM(AI45:AI46)"
    @eval_fn
    def AI44():
        range_1 = Input_RPS(35, 45, 35, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ44():
    # 'Input_RPS'!AJ44
    value = 0
    formula = "=SUM(AJ45:AJ46)"
    @eval_fn
    def AJ44():
        range_1 = Input_RPS(36, 45, 36, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK44():
    # 'Input_RPS'!AK44
    value = 0
    formula = "=SUM(AK45:AK46)"
    @eval_fn
    def AK44():
        range_1 = Input_RPS(37, 45, 37, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL44():
    # 'Input_RPS'!AL44
    value = 0
    formula = "=SUM(AL45:AL46)"
    @eval_fn
    def AL44():
        range_1 = Input_RPS(38, 45, 38, 46)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C45():
    # 'Input_RPS'!C45
    value = "            Photovoltaic"

@register(Input_RPS)
class M45():
    # 'Input_RPS'!M45
    value = 1600

@register(Input_RPS)
class N45():
    # 'Input_RPS'!N45
    value = 2200

@register(Input_RPS)
class O45():
    # 'Input_RPS'!O45
    value = 4400

@register(Input_RPS)
class P45():
    # 'Input_RPS'!P45
    value = 4793

@register(Input_RPS)
class Q45():
    # 'Input_RPS'!Q45
    value = 9563

@register(Input_RPS)
class R45():
    # 'Input_RPS'!R45
    value = 11873

@register(Input_RPS)
class S45():
    # 'Input_RPS'!S45
    value = 17738

@register(Input_RPS)
class T45():
    # 'Input_RPS'!T45
    value = 28282

@register(Input_RPS)
class U45():
    # 'Input_RPS'!U45
    value = 47471

@register(Input_RPS)
class V45():
    # 'Input_RPS'!V45
    value = 67444

@register(Input_RPS)
class W45():
    # 'Input_RPS'!W45
    value = 89691

@register(Input_RPS)
class C46():
    # 'Input_RPS'!C46
    value = "            Utility Solar"

@register(Input_RPS)
class M46():
    # 'Input_RPS'!M46
    value = 0

@register(Input_RPS)
class N46():
    # 'Input_RPS'!N46
    value = 0

@register(Input_RPS)
class O46():
    # 'Input_RPS'!O46
    value = 0

@register(Input_RPS)
class P46():
    # 'Input_RPS'!P46
    value = 0

@register(Input_RPS)
class Q46():
    # 'Input_RPS'!Q46
    value = 0

@register(Input_RPS)
class R46():
    # 'Input_RPS'!R46
    value = 17

@register(Input_RPS)
class S46():
    # 'Input_RPS'!S46
    value = 76

@register(Input_RPS)
class T46():
    # 'Input_RPS'!T46
    value = 245

@register(Input_RPS)
class U46():
    # 'Input_RPS'!U46
    value = 1525

@register(Input_RPS)
class V46():
    # 'Input_RPS'!V46
    value = 1568

@register(Input_RPS)
class W46():
    # 'Input_RPS'!W46
    value = 2557

@register(Input_RPS)
class C47():
    # 'Input_RPS'!C47
    value = "Biofuels: "

@register(Input_RPS)
class G47():
    # 'Input_RPS'!G47
    value = 0
    formula = "=SUM(G48)"
    @eval_fn
    def G47():
        g48_1 = Input_RPS.G48()
        var_1 = SUM(g48_1)
        return var_1

@register(Input_RPS)
class H47():
    # 'Input_RPS'!H47
    value = 0
    formula = "=SUM(H48)"
    @eval_fn
    def H47():
        h48_1 = Input_RPS.H48()
        var_1 = SUM(h48_1)
        return var_1

@register(Input_RPS)
class I47():
    # 'Input_RPS'!I47
    value = 0
    formula = "=SUM(I48)"
    @eval_fn
    def I47():
        i48_1 = Input_RPS.I48()
        var_1 = SUM(i48_1)
        return var_1

@register(Input_RPS)
class J47():
    # 'Input_RPS'!J47
    value = 0
    formula = "=SUM(J48)"
    @eval_fn
    def J47():
        j48_1 = Input_RPS.J48()
        var_1 = SUM(j48_1)
        return var_1

@register(Input_RPS)
class K47():
    # 'Input_RPS'!K47
    value = 0
    formula = "=SUM(K48)"
    @eval_fn
    def K47():
        k48_1 = Input_RPS.K48()
        var_1 = SUM(k48_1)
        return var_1

@register(Input_RPS)
class L47():
    # 'Input_RPS'!L47
    value = 0
    formula = "=SUM(L48)"
    @eval_fn
    def L47():
        l48_1 = Input_RPS.L48()
        var_1 = SUM(l48_1)
        return var_1

@register(Input_RPS)
class M47():
    # 'Input_RPS'!M47
    value = 0
    formula = "=SUM(M48)"
    @eval_fn
    def M47():
        m48_1 = Input_RPS.M48()
        var_1 = SUM(m48_1)
        return var_1

@register(Input_RPS)
class N47():
    # 'Input_RPS'!N47
    value = 0
    formula = "=N48"
    @eval_fn
    def N47():
        n48_1 = Input_RPS.N48()
        return n48_1

@register(Input_RPS)
class O47():
    # 'Input_RPS'!O47
    value = 0
    formula = "=O48"
    @eval_fn
    def O47():
        o48_1 = Input_RPS.O48()
        return o48_1

@register(Input_RPS)
class P47():
    # 'Input_RPS'!P47
    value = 0
    formula = "=P48"
    @eval_fn
    def P47():
        p48_1 = Input_RPS.P48()
        return p48_1

@register(Input_RPS)
class Q47():
    # 'Input_RPS'!Q47
    value = 0
    formula = "=Q48"
    @eval_fn
    def Q47():
        q48_1 = Input_RPS.Q48()
        return q48_1

@register(Input_RPS)
class R47():
    # 'Input_RPS'!R47
    value = 0
    formula = "=R48"
    @eval_fn
    def R47():
        r48_1 = Input_RPS.R48()
        return r48_1

@register(Input_RPS)
class S47():
    # 'Input_RPS'!S47
    value = 0
    formula = "=S48"
    @eval_fn
    def S47():
        s48_1 = Input_RPS.S48()
        return s48_1

@register(Input_RPS)
class C48():
    # 'Input_RPS'!C48
    value = "            Biodiesel"

@register(Input_RPS)
class N48():
    # 'Input_RPS'!N48
    value = 0

@register(Input_RPS)
class O48():
    # 'Input_RPS'!O48
    value = 0

@register(Input_RPS)
class P48():
    # 'Input_RPS'!P48
    value = 0

@register(Input_RPS)
class Q48():
    # 'Input_RPS'!Q48
    value = 0

@register(Input_RPS)
class R48():
    # 'Input_RPS'!R48
    value = 0

@register(Input_RPS)
class S48():
    # 'Input_RPS'!S48
    value = 0

@register(Input_RPS)
class A49():
    # 'Input_RPS'!A49
    value = "MECORenewable Electricity"
    formula = "=CONCATENATE(C49,B49)"
    @eval_fn
    def A49():
        c49_1 = Input_RPS.C49()
        b49_1 = Input_RPS.B49()
        var_1 = CONCATENATE(c49_1, b49_1)
        return var_1

@register(Input_RPS)
class B49():
    # 'Input_RPS'!B49
    value = "Renewable Electricity"

@register(Input_RPS)
class C49():
    # 'Input_RPS'!C49
    value = "MECO"

@register(Input_RPS)
class D49():
    # 'Input_RPS'!D49
    value = "MWh"

@register(Input_RPS)
class E49():
    # 'Input_RPS'!E49
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Input_RPS)
class F49():
    # 'Input_RPS'!F49
    value = "199-2004 includes biomass and hydro, biomass, photovoltaic"

@register(Input_RPS)
class G49():
    # 'Input_RPS'!G49
    value = 55000

@register(Input_RPS)
class H49():
    # 'Input_RPS'!H49
    value = 45000

@register(Input_RPS)
class I49():
    # 'Input_RPS'!I49
    value = 38000

@register(Input_RPS)
class J49():
    # 'Input_RPS'!J49
    value = 69000

@register(Input_RPS)
class K49():
    # 'Input_RPS'!K49
    value = 66000

@register(Input_RPS)
class L49():
    # 'Input_RPS'!L49
    value = 74200

@register(Input_RPS)
class M49():
    # 'Input_RPS'!M49
    value = 75400
    formula = "=M50+M56+M58+M64+M67+M70"
    @eval_fn
    def M49():
        m50_1 = Input_RPS.M50()
        m56_1 = Input_RPS.M56()
        var_1 = add(m50_1, m56_1)
        m58_1 = Input_RPS.M58()
        var_2 = add(var_1, m58_1)
        m64_1 = Input_RPS.M64()
        var_3 = add(var_2, m64_1)
        m67_1 = Input_RPS.M67()
        var_4 = add(var_3, m67_1)
        m70_1 = Input_RPS.M70()
        var_5 = add(var_4, m70_1)
        return var_5

@register(Input_RPS)
class N49():
    # 'Input_RPS'!N49
    value = 136900
    formula = "=N50+N56+N58+N64+N67+N70"
    @eval_fn
    def N49():
        n50_1 = Input_RPS.N50()
        n56_1 = Input_RPS.N56()
        var_1 = add(n50_1, n56_1)
        n58_1 = Input_RPS.N58()
        var_2 = add(var_1, n58_1)
        n64_1 = Input_RPS.N64()
        var_3 = add(var_2, n64_1)
        n67_1 = Input_RPS.N67()
        var_4 = add(var_3, n67_1)
        n70_1 = Input_RPS.N70()
        var_5 = add(var_4, n70_1)
        return var_5

@register(Input_RPS)
class O49():
    # 'Input_RPS'!O49
    value = 197700
    formula = "=O50+O56+O58+O64+O67+O70"
    @eval_fn
    def O49():
        o50_1 = Input_RPS.O50()
        o56_1 = Input_RPS.O56()
        var_1 = add(o50_1, o56_1)
        o58_1 = Input_RPS.O58()
        var_2 = add(var_1, o58_1)
        o64_1 = Input_RPS.O64()
        var_3 = add(var_2, o64_1)
        o67_1 = Input_RPS.O67()
        var_4 = add(var_3, o67_1)
        o70_1 = Input_RPS.O70()
        var_5 = add(var_4, o70_1)
        return var_5

@register(Input_RPS)
class P49():
    # 'Input_RPS'!P49
    value = 171929
    formula = "=P50+P56+P58+P64+P67+P70"
    @eval_fn
    def P49():
        p50_1 = Input_RPS.P50()
        p56_1 = Input_RPS.P56()
        var_1 = add(p50_1, p56_1)
        p58_1 = Input_RPS.P58()
        var_2 = add(var_1, p58_1)
        p64_1 = Input_RPS.P64()
        var_3 = add(var_2, p64_1)
        p67_1 = Input_RPS.P67()
        var_4 = add(var_3, p67_1)
        p70_1 = Input_RPS.P70()
        var_5 = add(var_4, p70_1)
        return var_5

@register(Input_RPS)
class Q49():
    # 'Input_RPS'!Q49
    value = 165835
    formula = "=Q50+Q56+Q58+Q64+Q67+Q70"
    @eval_fn
    def Q49():
        q50_1 = Input_RPS.Q50()
        q56_1 = Input_RPS.Q56()
        var_1 = add(q50_1, q56_1)
        q58_1 = Input_RPS.Q58()
        var_2 = add(var_1, q58_1)
        q64_1 = Input_RPS.Q64()
        var_3 = add(var_2, q64_1)
        q67_1 = Input_RPS.Q67()
        var_4 = add(var_3, q67_1)
        q70_1 = Input_RPS.Q70()
        var_5 = add(var_4, q70_1)
        return var_5

@register(Input_RPS)
class R49():
    # 'Input_RPS'!R49
    value = 182560
    formula = "=R50+R56+R58+R64+R67+R70"
    @eval_fn
    def R49():
        r50_1 = Input_RPS.R50()
        r56_1 = Input_RPS.R56()
        var_1 = add(r50_1, r56_1)
        r58_1 = Input_RPS.R58()
        var_2 = add(var_1, r58_1)
        r64_1 = Input_RPS.R64()
        var_3 = add(var_2, r64_1)
        r67_1 = Input_RPS.R67()
        var_4 = add(var_3, r67_1)
        r70_1 = Input_RPS.R70()
        var_5 = add(var_4, r70_1)
        return var_5

@register(Input_RPS)
class S49():
    # 'Input_RPS'!S49
    value = 202270
    formula = "=S50+S56+S58+S64+S67+S70"
    @eval_fn
    def S49():
        s50_1 = Input_RPS.S50()
        s56_1 = Input_RPS.S56()
        var_1 = add(s50_1, s56_1)
        s58_1 = Input_RPS.S58()
        var_2 = add(var_1, s58_1)
        s64_1 = Input_RPS.S64()
        var_3 = add(var_2, s64_1)
        s67_1 = Input_RPS.S67()
        var_4 = add(var_3, s67_1)
        s70_1 = Input_RPS.S70()
        var_5 = add(var_4, s70_1)
        return var_5

@register(Input_RPS)
class T49():
    # 'Input_RPS'!T49
    value = 238319
    formula = "=T50+T56+T58+T64+T67+T70"
    @eval_fn
    def T49():
        t50_1 = Input_RPS.T50()
        t56_1 = Input_RPS.T56()
        var_1 = add(t50_1, t56_1)
        t58_1 = Input_RPS.T58()
        var_2 = add(var_1, t58_1)
        t64_1 = Input_RPS.T64()
        var_3 = add(var_2, t64_1)
        t67_1 = Input_RPS.T67()
        var_4 = add(var_3, t67_1)
        t70_1 = Input_RPS.T70()
        var_5 = add(var_4, t70_1)
        return var_5

@register(Input_RPS)
class U49():
    # 'Input_RPS'!U49
    value = 330067
    formula = "=U50+U56+U58+U64+U67+U70"
    @eval_fn
    def U49():
        u50_1 = Input_RPS.U50()
        u56_1 = Input_RPS.U56()
        var_1 = add(u50_1, u56_1)
        u58_1 = Input_RPS.U58()
        var_2 = add(var_1, u58_1)
        u64_1 = Input_RPS.U64()
        var_3 = add(var_2, u64_1)
        u67_1 = Input_RPS.U67()
        var_4 = add(var_3, u67_1)
        u70_1 = Input_RPS.U70()
        var_5 = add(var_4, u70_1)
        return var_5

@register(Input_RPS)
class V49():
    # 'Input_RPS'!V49
    value = 381351
    formula = "=V50+V56+V58+V64+V67+V70"
    @eval_fn
    def V49():
        v50_1 = Input_RPS.V50()
        v56_1 = Input_RPS.V56()
        var_1 = add(v50_1, v56_1)
        v58_1 = Input_RPS.V58()
        var_2 = add(var_1, v58_1)
        v64_1 = Input_RPS.V64()
        var_3 = add(var_2, v64_1)
        v67_1 = Input_RPS.V67()
        var_4 = add(var_3, v67_1)
        v70_1 = Input_RPS.V70()
        var_5 = add(var_4, v70_1)
        return var_5

@register(Input_RPS)
class W49():
    # 'Input_RPS'!W49
    value = 402832
    formula = "=W50+W56+W58+W64+W67+W70"
    @eval_fn
    def W49():
        w50_1 = Input_RPS.W50()
        w56_1 = Input_RPS.W56()
        var_1 = add(w50_1, w56_1)
        w58_1 = Input_RPS.W58()
        var_2 = add(var_1, w58_1)
        w64_1 = Input_RPS.W64()
        var_3 = add(var_2, w64_1)
        w67_1 = Input_RPS.W67()
        var_4 = add(var_3, w67_1)
        w70_1 = Input_RPS.W70()
        var_5 = add(var_4, w70_1)
        return var_5

@register(Input_RPS)
class X49():
    # 'Input_RPS'!X49
    value = 0
    formula = "=X50+X56+X58+X64+X67+X70"
    @eval_fn
    def X49():
        x50_1 = Input_RPS.X50()
        x56_1 = Input_RPS.X56()
        var_1 = add(x50_1, x56_1)
        x58_1 = Input_RPS.X58()
        var_2 = add(var_1, x58_1)
        x64_1 = Input_RPS.X64()
        var_3 = add(var_2, x64_1)
        x67_1 = Input_RPS.X67()
        var_4 = add(var_3, x67_1)
        x70_1 = Input_RPS.X70()
        var_5 = add(var_4, x70_1)
        return var_5

@register(Input_RPS)
class Y49():
    # 'Input_RPS'!Y49
    value = 0
    formula = "=Y50+Y56+Y58+Y64+Y67+Y70"
    @eval_fn
    def Y49():
        y50_1 = Input_RPS.Y50()
        y56_1 = Input_RPS.Y56()
        var_1 = add(y50_1, y56_1)
        y58_1 = Input_RPS.Y58()
        var_2 = add(var_1, y58_1)
        y64_1 = Input_RPS.Y64()
        var_3 = add(var_2, y64_1)
        y67_1 = Input_RPS.Y67()
        var_4 = add(var_3, y67_1)
        y70_1 = Input_RPS.Y70()
        var_5 = add(var_4, y70_1)
        return var_5

@register(Input_RPS)
class Z49():
    # 'Input_RPS'!Z49
    value = 0
    formula = "=Z50+Z56+Z58+Z64+Z67+Z70"
    @eval_fn
    def Z49():
        z50_1 = Input_RPS.Z50()
        z56_1 = Input_RPS.Z56()
        var_1 = add(z50_1, z56_1)
        z58_1 = Input_RPS.Z58()
        var_2 = add(var_1, z58_1)
        z64_1 = Input_RPS.Z64()
        var_3 = add(var_2, z64_1)
        z67_1 = Input_RPS.Z67()
        var_4 = add(var_3, z67_1)
        z70_1 = Input_RPS.Z70()
        var_5 = add(var_4, z70_1)
        return var_5

@register(Input_RPS)
class AA49():
    # 'Input_RPS'!AA49
    value = 0
    formula = "=AA50+AA56+AA58+AA64+AA67+AA70"
    @eval_fn
    def AA49():
        aa50_1 = Input_RPS.AA50()
        aa56_1 = Input_RPS.AA56()
        var_1 = add(aa50_1, aa56_1)
        aa58_1 = Input_RPS.AA58()
        var_2 = add(var_1, aa58_1)
        aa64_1 = Input_RPS.AA64()
        var_3 = add(var_2, aa64_1)
        aa67_1 = Input_RPS.AA67()
        var_4 = add(var_3, aa67_1)
        aa70_1 = Input_RPS.AA70()
        var_5 = add(var_4, aa70_1)
        return var_5

@register(Input_RPS)
class AB49():
    # 'Input_RPS'!AB49
    value = 0
    formula = "=AB50+AB56+AB58+AB64+AB67+AB70"
    @eval_fn
    def AB49():
        ab50_1 = Input_RPS.AB50()
        ab56_1 = Input_RPS.AB56()
        var_1 = add(ab50_1, ab56_1)
        ab58_1 = Input_RPS.AB58()
        var_2 = add(var_1, ab58_1)
        ab64_1 = Input_RPS.AB64()
        var_3 = add(var_2, ab64_1)
        ab67_1 = Input_RPS.AB67()
        var_4 = add(var_3, ab67_1)
        ab70_1 = Input_RPS.AB70()
        var_5 = add(var_4, ab70_1)
        return var_5

@register(Input_RPS)
class AC49():
    # 'Input_RPS'!AC49
    value = 0
    formula = "=AC50+AC56+AC58+AC64+AC67+AC70"
    @eval_fn
    def AC49():
        ac50_1 = Input_RPS.AC50()
        ac56_1 = Input_RPS.AC56()
        var_1 = add(ac50_1, ac56_1)
        ac58_1 = Input_RPS.AC58()
        var_2 = add(var_1, ac58_1)
        ac64_1 = Input_RPS.AC64()
        var_3 = add(var_2, ac64_1)
        ac67_1 = Input_RPS.AC67()
        var_4 = add(var_3, ac67_1)
        ac70_1 = Input_RPS.AC70()
        var_5 = add(var_4, ac70_1)
        return var_5

@register(Input_RPS)
class AD49():
    # 'Input_RPS'!AD49
    value = 0
    formula = "=AD50+AD56+AD58+AD64+AD67+AD70"
    @eval_fn
    def AD49():
        ad50_1 = Input_RPS.AD50()
        ad56_1 = Input_RPS.AD56()
        var_1 = add(ad50_1, ad56_1)
        ad58_1 = Input_RPS.AD58()
        var_2 = add(var_1, ad58_1)
        ad64_1 = Input_RPS.AD64()
        var_3 = add(var_2, ad64_1)
        ad67_1 = Input_RPS.AD67()
        var_4 = add(var_3, ad67_1)
        ad70_1 = Input_RPS.AD70()
        var_5 = add(var_4, ad70_1)
        return var_5

@register(Input_RPS)
class AE49():
    # 'Input_RPS'!AE49
    value = 0
    formula = "=AE50+AE56+AE58+AE64+AE67+AE70"
    @eval_fn
    def AE49():
        ae50_1 = Input_RPS.AE50()
        ae56_1 = Input_RPS.AE56()
        var_1 = add(ae50_1, ae56_1)
        ae58_1 = Input_RPS.AE58()
        var_2 = add(var_1, ae58_1)
        ae64_1 = Input_RPS.AE64()
        var_3 = add(var_2, ae64_1)
        ae67_1 = Input_RPS.AE67()
        var_4 = add(var_3, ae67_1)
        ae70_1 = Input_RPS.AE70()
        var_5 = add(var_4, ae70_1)
        return var_5

@register(Input_RPS)
class AF49():
    # 'Input_RPS'!AF49
    value = 0
    formula = "=AF50+AF56+AF58+AF64+AF67+AF70"
    @eval_fn
    def AF49():
        af50_1 = Input_RPS.AF50()
        af56_1 = Input_RPS.AF56()
        var_1 = add(af50_1, af56_1)
        af58_1 = Input_RPS.AF58()
        var_2 = add(var_1, af58_1)
        af64_1 = Input_RPS.AF64()
        var_3 = add(var_2, af64_1)
        af67_1 = Input_RPS.AF67()
        var_4 = add(var_3, af67_1)
        af70_1 = Input_RPS.AF70()
        var_5 = add(var_4, af70_1)
        return var_5

@register(Input_RPS)
class AG49():
    # 'Input_RPS'!AG49
    value = 0
    formula = "=AG50+AG56+AG58+AG64+AG67+AG70"
    @eval_fn
    def AG49():
        ag50_1 = Input_RPS.AG50()
        ag56_1 = Input_RPS.AG56()
        var_1 = add(ag50_1, ag56_1)
        ag58_1 = Input_RPS.AG58()
        var_2 = add(var_1, ag58_1)
        ag64_1 = Input_RPS.AG64()
        var_3 = add(var_2, ag64_1)
        ag67_1 = Input_RPS.AG67()
        var_4 = add(var_3, ag67_1)
        ag70_1 = Input_RPS.AG70()
        var_5 = add(var_4, ag70_1)
        return var_5

@register(Input_RPS)
class AH49():
    # 'Input_RPS'!AH49
    value = 0
    formula = "=AH50+AH56+AH58+AH64+AH67+AH70"
    @eval_fn
    def AH49():
        ah50_1 = Input_RPS.AH50()
        ah56_1 = Input_RPS.AH56()
        var_1 = add(ah50_1, ah56_1)
        ah58_1 = Input_RPS.AH58()
        var_2 = add(var_1, ah58_1)
        ah64_1 = Input_RPS.AH64()
        var_3 = add(var_2, ah64_1)
        ah67_1 = Input_RPS.AH67()
        var_4 = add(var_3, ah67_1)
        ah70_1 = Input_RPS.AH70()
        var_5 = add(var_4, ah70_1)
        return var_5

@register(Input_RPS)
class AI49():
    # 'Input_RPS'!AI49
    value = 0
    formula = "=AI50+AI56+AI58+AI64+AI67+AI70"
    @eval_fn
    def AI49():
        ai50_1 = Input_RPS.AI50()
        ai56_1 = Input_RPS.AI56()
        var_1 = add(ai50_1, ai56_1)
        ai58_1 = Input_RPS.AI58()
        var_2 = add(var_1, ai58_1)
        ai64_1 = Input_RPS.AI64()
        var_3 = add(var_2, ai64_1)
        ai67_1 = Input_RPS.AI67()
        var_4 = add(var_3, ai67_1)
        ai70_1 = Input_RPS.AI70()
        var_5 = add(var_4, ai70_1)
        return var_5

@register(Input_RPS)
class AJ49():
    # 'Input_RPS'!AJ49
    value = 0
    formula = "=AJ50+AJ56+AJ58+AJ64+AJ67+AJ70"
    @eval_fn
    def AJ49():
        aj50_1 = Input_RPS.AJ50()
        aj56_1 = Input_RPS.AJ56()
        var_1 = add(aj50_1, aj56_1)
        aj58_1 = Input_RPS.AJ58()
        var_2 = add(var_1, aj58_1)
        aj64_1 = Input_RPS.AJ64()
        var_3 = add(var_2, aj64_1)
        aj67_1 = Input_RPS.AJ67()
        var_4 = add(var_3, aj67_1)
        aj70_1 = Input_RPS.AJ70()
        var_5 = add(var_4, aj70_1)
        return var_5

@register(Input_RPS)
class AK49():
    # 'Input_RPS'!AK49
    value = 0
    formula = "=AK50+AK56+AK58+AK64+AK67+AK70"
    @eval_fn
    def AK49():
        ak50_1 = Input_RPS.AK50()
        ak56_1 = Input_RPS.AK56()
        var_1 = add(ak50_1, ak56_1)
        ak58_1 = Input_RPS.AK58()
        var_2 = add(var_1, ak58_1)
        ak64_1 = Input_RPS.AK64()
        var_3 = add(var_2, ak64_1)
        ak67_1 = Input_RPS.AK67()
        var_4 = add(var_3, ak67_1)
        ak70_1 = Input_RPS.AK70()
        var_5 = add(var_4, ak70_1)
        return var_5

@register(Input_RPS)
class AL49():
    # 'Input_RPS'!AL49
    value = 0
    formula = "=AL50+AL56+AL58+AL64+AL67+AL70"
    @eval_fn
    def AL49():
        al50_1 = Input_RPS.AL50()
        al56_1 = Input_RPS.AL56()
        var_1 = add(al50_1, al56_1)
        al58_1 = Input_RPS.AL58()
        var_2 = add(var_1, al58_1)
        al64_1 = Input_RPS.AL64()
        var_3 = add(var_2, al64_1)
        al67_1 = Input_RPS.AL67()
        var_4 = add(var_3, al67_1)
        al70_1 = Input_RPS.AL70()
        var_5 = add(var_4, al70_1)
        return var_5

@register(Input_RPS)
class C50():
    # 'Input_RPS'!C50
    value = "Hydro:"

@register(Input_RPS)
class G50():
    # 'Input_RPS'!G50
    value = 0
    formula = "=SUM(G51:G55)"
    @eval_fn
    def G50():
        range_1 = Input_RPS(7, 51, 7, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H50():
    # 'Input_RPS'!H50
    value = 0
    formula = "=SUM(H51:H55)"
    @eval_fn
    def H50():
        range_1 = Input_RPS(8, 51, 8, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I50():
    # 'Input_RPS'!I50
    value = 0
    formula = "=SUM(I51:I55)"
    @eval_fn
    def I50():
        range_1 = Input_RPS(9, 51, 9, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J50():
    # 'Input_RPS'!J50
    value = 0
    formula = "=SUM(J51:J55)"
    @eval_fn
    def J50():
        range_1 = Input_RPS(10, 51, 10, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K50():
    # 'Input_RPS'!K50
    value = 0
    formula = "=SUM(K51:K55)"
    @eval_fn
    def K50():
        range_1 = Input_RPS(11, 51, 11, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L50():
    # 'Input_RPS'!L50
    value = 0
    formula = "=SUM(L51:L55)"
    @eval_fn
    def L50():
        range_1 = Input_RPS(12, 51, 12, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M50():
    # 'Input_RPS'!M50
    value = 75000
    formula = "=SUM(M51:M55)"
    @eval_fn
    def M50():
        range_1 = Input_RPS(13, 51, 13, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N50():
    # 'Input_RPS'!N50
    value = 79000
    formula = "=SUM(N51:N55)"
    @eval_fn
    def N50():
        range_1 = Input_RPS(14, 51, 14, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O50():
    # 'Input_RPS'!O50
    value = 69000
    formula = "=SUM(O51:O55)"
    @eval_fn
    def O50():
        range_1 = Input_RPS(15, 51, 15, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P50():
    # 'Input_RPS'!P50
    value = 5910

@register(Input_RPS)
class Q50():
    # 'Input_RPS'!Q50
    value = 10009

@register(Input_RPS)
class R50():
    # 'Input_RPS'!R50
    value = 6701

@register(Input_RPS)
class S50():
    # 'Input_RPS'!S50
    value = 6206

@register(Input_RPS)
class T50():
    # 'Input_RPS'!T50
    value = 7453

@register(Input_RPS)
class U50():
    # 'Input_RPS'!U50
    value = 4745

@register(Input_RPS)
class V50():
    # 'Input_RPS'!V50
    value = 8150

@register(Input_RPS)
class W50():
    # 'Input_RPS'!W50
    value = 9823

@register(Input_RPS)
class X50():
    # 'Input_RPS'!X50
    value = 0
    formula = "=SUM(X51:X55)"
    @eval_fn
    def X50():
        range_1 = Input_RPS(24, 51, 24, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y50():
    # 'Input_RPS'!Y50
    value = 0
    formula = "=SUM(Y51:Y55)"
    @eval_fn
    def Y50():
        range_1 = Input_RPS(25, 51, 25, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z50():
    # 'Input_RPS'!Z50
    value = 0
    formula = "=SUM(Z51:Z55)"
    @eval_fn
    def Z50():
        range_1 = Input_RPS(26, 51, 26, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA50():
    # 'Input_RPS'!AA50
    value = 0
    formula = "=SUM(AA51:AA55)"
    @eval_fn
    def AA50():
        range_1 = Input_RPS(27, 51, 27, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB50():
    # 'Input_RPS'!AB50
    value = 0
    formula = "=SUM(AB51:AB55)"
    @eval_fn
    def AB50():
        range_1 = Input_RPS(28, 51, 28, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC50():
    # 'Input_RPS'!AC50
    value = 0
    formula = "=SUM(AC51:AC55)"
    @eval_fn
    def AC50():
        range_1 = Input_RPS(29, 51, 29, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD50():
    # 'Input_RPS'!AD50
    value = 0
    formula = "=SUM(AD51:AD55)"
    @eval_fn
    def AD50():
        range_1 = Input_RPS(30, 51, 30, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE50():
    # 'Input_RPS'!AE50
    value = 0
    formula = "=SUM(AE51:AE55)"
    @eval_fn
    def AE50():
        range_1 = Input_RPS(31, 51, 31, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF50():
    # 'Input_RPS'!AF50
    value = 0
    formula = "=SUM(AF51:AF55)"
    @eval_fn
    def AF50():
        range_1 = Input_RPS(32, 51, 32, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG50():
    # 'Input_RPS'!AG50
    value = 0
    formula = "=SUM(AG51:AG55)"
    @eval_fn
    def AG50():
        range_1 = Input_RPS(33, 51, 33, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH50():
    # 'Input_RPS'!AH50
    value = 0
    formula = "=SUM(AH51:AH55)"
    @eval_fn
    def AH50():
        range_1 = Input_RPS(34, 51, 34, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI50():
    # 'Input_RPS'!AI50
    value = 0
    formula = "=SUM(AI51:AI55)"
    @eval_fn
    def AI50():
        range_1 = Input_RPS(35, 51, 35, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ50():
    # 'Input_RPS'!AJ50
    value = 0
    formula = "=SUM(AJ51:AJ55)"
    @eval_fn
    def AJ50():
        range_1 = Input_RPS(36, 51, 36, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK50():
    # 'Input_RPS'!AK50
    value = 0
    formula = "=SUM(AK51:AK55)"
    @eval_fn
    def AK50():
        range_1 = Input_RPS(37, 51, 37, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL50():
    # 'Input_RPS'!AL50
    value = 0
    formula = "=SUM(AL51:AL55)"
    @eval_fn
    def AL50():
        range_1 = Input_RPS(38, 51, 38, 55)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C51():
    # 'Input_RPS'!C51
    value = "               Hydro"

@register(Input_RPS)
class N51():
    # 'Input_RPS'!N51
    value = 0

@register(Input_RPS)
class O51():
    # 'Input_RPS'!O51
    value = 0

@register(Input_RPS)
class C52():
    # 'Input_RPS'!C52
    value = "               Small Hydro"

@register(Input_RPS)
class N52():
    # 'Input_RPS'!N52
    value = 0

@register(Input_RPS)
class O52():
    # 'Input_RPS'!O52
    value = 0

@register(Input_RPS)
class C53():
    # 'Input_RPS'!C53
    value = "               Hydro-Helco owned"

@register(Input_RPS)
class N53():
    # 'Input_RPS'!N53
    value = 0

@register(Input_RPS)
class O53():
    # 'Input_RPS'!O53
    value = 0

@register(Input_RPS)
class C54():
    # 'Input_RPS'!C54
    value = "               Biomass & Hyrdro HC&S"

@register(Input_RPS)
class M54():
    # 'Input_RPS'!M54
    value = 75000

@register(Input_RPS)
class N54():
    # 'Input_RPS'!N54
    value = 79000

@register(Input_RPS)
class O54():
    # 'Input_RPS'!O54
    value = 69000

@register(Input_RPS)
class C56():
    # 'Input_RPS'!C56
    value = "Geothermal:"

@register(Input_RPS)
class G56():
    # 'Input_RPS'!G56
    value = 0
    formula = "=SUM(G57)"
    @eval_fn
    def G56():
        g57_1 = Input_RPS.G57()
        var_1 = SUM(g57_1)
        return var_1

@register(Input_RPS)
class H56():
    # 'Input_RPS'!H56
    value = 0
    formula = "=SUM(H57)"
    @eval_fn
    def H56():
        h57_1 = Input_RPS.H57()
        var_1 = SUM(h57_1)
        return var_1

@register(Input_RPS)
class I56():
    # 'Input_RPS'!I56
    value = 0
    formula = "=SUM(I57)"
    @eval_fn
    def I56():
        i57_1 = Input_RPS.I57()
        var_1 = SUM(i57_1)
        return var_1

@register(Input_RPS)
class J56():
    # 'Input_RPS'!J56
    value = 0
    formula = "=SUM(J57)"
    @eval_fn
    def J56():
        j57_1 = Input_RPS.J57()
        var_1 = SUM(j57_1)
        return var_1

@register(Input_RPS)
class K56():
    # 'Input_RPS'!K56
    value = 0
    formula = "=SUM(K57)"
    @eval_fn
    def K56():
        k57_1 = Input_RPS.K57()
        var_1 = SUM(k57_1)
        return var_1

@register(Input_RPS)
class L56():
    # 'Input_RPS'!L56
    value = 0
    formula = "=SUM(L57)"
    @eval_fn
    def L56():
        l57_1 = Input_RPS.L57()
        var_1 = SUM(l57_1)
        return var_1

@register(Input_RPS)
class M56():
    # 'Input_RPS'!M56
    value = 0
    formula = "=SUM(M57)"
    @eval_fn
    def M56():
        m57_1 = Input_RPS.M57()
        var_1 = SUM(m57_1)
        return var_1

@register(Input_RPS)
class N56():
    # 'Input_RPS'!N56
    value = 0
    formula = "=N57"
    @eval_fn
    def N56():
        n57_1 = Input_RPS.N57()
        return n57_1

@register(Input_RPS)
class O56():
    # 'Input_RPS'!O56
    value = 0
    formula = "=O57"
    @eval_fn
    def O56():
        o57_1 = Input_RPS.O57()
        return o57_1

@register(Input_RPS)
class P56():
    # 'Input_RPS'!P56
    value = 0
    formula = "=P57"
    @eval_fn
    def P56():
        p57_1 = Input_RPS.P57()
        return p57_1

@register(Input_RPS)
class Q56():
    # 'Input_RPS'!Q56
    value = 0
    formula = "=Q57"
    @eval_fn
    def Q56():
        q57_1 = Input_RPS.Q57()
        return q57_1

@register(Input_RPS)
class R56():
    # 'Input_RPS'!R56
    value = 0
    formula = "=R57"
    @eval_fn
    def R56():
        r57_1 = Input_RPS.R57()
        return r57_1

@register(Input_RPS)
class S56():
    # 'Input_RPS'!S56
    value = 0
    formula = "=S57"
    @eval_fn
    def S56():
        s57_1 = Input_RPS.S57()
        return s57_1

@register(Input_RPS)
class T56():
    # 'Input_RPS'!T56
    value = 0
    formula = "=SUM(T57)"
    @eval_fn
    def T56():
        t57_1 = Input_RPS.T57()
        var_1 = SUM(t57_1)
        return var_1

@register(Input_RPS)
class U56():
    # 'Input_RPS'!U56
    value = 0
    formula = "=SUM(U57)"
    @eval_fn
    def U56():
        u57_1 = Input_RPS.U57()
        var_1 = SUM(u57_1)
        return var_1

@register(Input_RPS)
class V56():
    # 'Input_RPS'!V56
    value = 0
    formula = "=SUM(V57)"
    @eval_fn
    def V56():
        v57_1 = Input_RPS.V57()
        var_1 = SUM(v57_1)
        return var_1

@register(Input_RPS)
class W56():
    # 'Input_RPS'!W56
    value = 0
    formula = "=SUM(W57)"
    @eval_fn
    def W56():
        w57_1 = Input_RPS.W57()
        var_1 = SUM(w57_1)
        return var_1

@register(Input_RPS)
class X56():
    # 'Input_RPS'!X56
    value = 0
    formula = "=SUM(X57)"
    @eval_fn
    def X56():
        x57_1 = Input_RPS.X57()
        var_1 = SUM(x57_1)
        return var_1

@register(Input_RPS)
class Y56():
    # 'Input_RPS'!Y56
    value = 0
    formula = "=SUM(Y57)"
    @eval_fn
    def Y56():
        y57_1 = Input_RPS.Y57()
        var_1 = SUM(y57_1)
        return var_1

@register(Input_RPS)
class Z56():
    # 'Input_RPS'!Z56
    value = 0
    formula = "=SUM(Z57)"
    @eval_fn
    def Z56():
        z57_1 = Input_RPS.Z57()
        var_1 = SUM(z57_1)
        return var_1

@register(Input_RPS)
class AA56():
    # 'Input_RPS'!AA56
    value = 0
    formula = "=SUM(AA57)"
    @eval_fn
    def AA56():
        aa57_1 = Input_RPS.AA57()
        var_1 = SUM(aa57_1)
        return var_1

@register(Input_RPS)
class AB56():
    # 'Input_RPS'!AB56
    value = 0
    formula = "=SUM(AB57)"
    @eval_fn
    def AB56():
        ab57_1 = Input_RPS.AB57()
        var_1 = SUM(ab57_1)
        return var_1

@register(Input_RPS)
class AC56():
    # 'Input_RPS'!AC56
    value = 0
    formula = "=SUM(AC57)"
    @eval_fn
    def AC56():
        ac57_1 = Input_RPS.AC57()
        var_1 = SUM(ac57_1)
        return var_1

@register(Input_RPS)
class AD56():
    # 'Input_RPS'!AD56
    value = 0
    formula = "=SUM(AD57)"
    @eval_fn
    def AD56():
        ad57_1 = Input_RPS.AD57()
        var_1 = SUM(ad57_1)
        return var_1

@register(Input_RPS)
class AE56():
    # 'Input_RPS'!AE56
    value = 0
    formula = "=SUM(AE57)"
    @eval_fn
    def AE56():
        ae57_1 = Input_RPS.AE57()
        var_1 = SUM(ae57_1)
        return var_1

@register(Input_RPS)
class AF56():
    # 'Input_RPS'!AF56
    value = 0
    formula = "=SUM(AF57)"
    @eval_fn
    def AF56():
        af57_1 = Input_RPS.AF57()
        var_1 = SUM(af57_1)
        return var_1

@register(Input_RPS)
class AG56():
    # 'Input_RPS'!AG56
    value = 0
    formula = "=SUM(AG57)"
    @eval_fn
    def AG56():
        ag57_1 = Input_RPS.AG57()
        var_1 = SUM(ag57_1)
        return var_1

@register(Input_RPS)
class AH56():
    # 'Input_RPS'!AH56
    value = 0
    formula = "=SUM(AH57)"
    @eval_fn
    def AH56():
        ah57_1 = Input_RPS.AH57()
        var_1 = SUM(ah57_1)
        return var_1

@register(Input_RPS)
class AI56():
    # 'Input_RPS'!AI56
    value = 0
    formula = "=SUM(AI57)"
    @eval_fn
    def AI56():
        ai57_1 = Input_RPS.AI57()
        var_1 = SUM(ai57_1)
        return var_1

@register(Input_RPS)
class AJ56():
    # 'Input_RPS'!AJ56
    value = 0
    formula = "=SUM(AJ57)"
    @eval_fn
    def AJ56():
        aj57_1 = Input_RPS.AJ57()
        var_1 = SUM(aj57_1)
        return var_1

@register(Input_RPS)
class AK56():
    # 'Input_RPS'!AK56
    value = 0
    formula = "=SUM(AK57)"
    @eval_fn
    def AK56():
        ak57_1 = Input_RPS.AK57()
        var_1 = SUM(ak57_1)
        return var_1

@register(Input_RPS)
class AL56():
    # 'Input_RPS'!AL56
    value = 0
    formula = "=SUM(AL57)"
    @eval_fn
    def AL56():
        al57_1 = Input_RPS.AL57()
        var_1 = SUM(al57_1)
        return var_1

@register(Input_RPS)
class C57():
    # 'Input_RPS'!C57
    value = "               PGV"

@register(Input_RPS)
class N57():
    # 'Input_RPS'!N57
    value = 0

@register(Input_RPS)
class O57():
    # 'Input_RPS'!O57
    value = 0

@register(Input_RPS)
class P57():
    # 'Input_RPS'!P57
    value = 0

@register(Input_RPS)
class Q57():
    # 'Input_RPS'!Q57
    value = 0

@register(Input_RPS)
class R57():
    # 'Input_RPS'!R57
    value = 0

@register(Input_RPS)
class S57():
    # 'Input_RPS'!S57
    value = 0

@register(Input_RPS)
class C58():
    # 'Input_RPS'!C58
    value = "Wind: "

@register(Input_RPS)
class G58():
    # 'Input_RPS'!G58
    value = 0
    formula = "=SUM(G59:G63)"
    @eval_fn
    def G58():
        range_1 = Input_RPS(7, 59, 7, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H58():
    # 'Input_RPS'!H58
    value = 0
    formula = "=SUM(H59:H63)"
    @eval_fn
    def H58():
        range_1 = Input_RPS(8, 59, 8, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I58():
    # 'Input_RPS'!I58
    value = 0
    formula = "=SUM(I59:I63)"
    @eval_fn
    def I58():
        range_1 = Input_RPS(9, 59, 9, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J58():
    # 'Input_RPS'!J58
    value = 0
    formula = "=SUM(J59:J63)"
    @eval_fn
    def J58():
        range_1 = Input_RPS(10, 59, 10, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K58():
    # 'Input_RPS'!K58
    value = 0
    formula = "=SUM(K59:K63)"
    @eval_fn
    def K58():
        range_1 = Input_RPS(11, 59, 11, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L58():
    # 'Input_RPS'!L58
    value = 0
    formula = "=SUM(L59:L63)"
    @eval_fn
    def L58():
        range_1 = Input_RPS(12, 59, 12, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M58():
    # 'Input_RPS'!M58
    value = 0
    formula = "=SUM(M59:M63)"
    @eval_fn
    def M58():
        range_1 = Input_RPS(13, 59, 13, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N58():
    # 'Input_RPS'!N58
    value = 57000
    formula = "=SUM(N59:N63)"
    @eval_fn
    def N58():
        range_1 = Input_RPS(14, 59, 14, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O58():
    # 'Input_RPS'!O58
    value = 126000
    formula = "=SUM(O59:O63)"
    @eval_fn
    def O58():
        range_1 = Input_RPS(15, 59, 15, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P58():
    # 'Input_RPS'!P58
    value = 108987

@register(Input_RPS)
class Q58():
    # 'Input_RPS'!Q58
    value = 109668

@register(Input_RPS)
class R58():
    # 'Input_RPS'!R58
    value = 120227

@register(Input_RPS)
class S58():
    # 'Input_RPS'!S58
    value = 123023

@register(Input_RPS)
class T58():
    # 'Input_RPS'!T58
    value = 158158

@register(Input_RPS)
class U58():
    # 'Input_RPS'!U58
    value = 230305

@register(Input_RPS)
class V58():
    # 'Input_RPS'!V58
    value = 257907

@register(Input_RPS)
class W58():
    # 'Input_RPS'!W58
    value = 264291

@register(Input_RPS)
class X58():
    # 'Input_RPS'!X58
    value = 0
    formula = "=SUM(X59:X63)"
    @eval_fn
    def X58():
        range_1 = Input_RPS(24, 59, 24, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y58():
    # 'Input_RPS'!Y58
    value = 0
    formula = "=SUM(Y59:Y63)"
    @eval_fn
    def Y58():
        range_1 = Input_RPS(25, 59, 25, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z58():
    # 'Input_RPS'!Z58
    value = 0
    formula = "=SUM(Z59:Z63)"
    @eval_fn
    def Z58():
        range_1 = Input_RPS(26, 59, 26, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA58():
    # 'Input_RPS'!AA58
    value = 0
    formula = "=SUM(AA59:AA63)"
    @eval_fn
    def AA58():
        range_1 = Input_RPS(27, 59, 27, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB58():
    # 'Input_RPS'!AB58
    value = 0
    formula = "=SUM(AB59:AB63)"
    @eval_fn
    def AB58():
        range_1 = Input_RPS(28, 59, 28, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC58():
    # 'Input_RPS'!AC58
    value = 0
    formula = "=SUM(AC59:AC63)"
    @eval_fn
    def AC58():
        range_1 = Input_RPS(29, 59, 29, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD58():
    # 'Input_RPS'!AD58
    value = 0
    formula = "=SUM(AD59:AD63)"
    @eval_fn
    def AD58():
        range_1 = Input_RPS(30, 59, 30, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE58():
    # 'Input_RPS'!AE58
    value = 0
    formula = "=SUM(AE59:AE63)"
    @eval_fn
    def AE58():
        range_1 = Input_RPS(31, 59, 31, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF58():
    # 'Input_RPS'!AF58
    value = 0
    formula = "=SUM(AF59:AF63)"
    @eval_fn
    def AF58():
        range_1 = Input_RPS(32, 59, 32, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG58():
    # 'Input_RPS'!AG58
    value = 0
    formula = "=SUM(AG59:AG63)"
    @eval_fn
    def AG58():
        range_1 = Input_RPS(33, 59, 33, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH58():
    # 'Input_RPS'!AH58
    value = 0
    formula = "=SUM(AH59:AH63)"
    @eval_fn
    def AH58():
        range_1 = Input_RPS(34, 59, 34, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI58():
    # 'Input_RPS'!AI58
    value = 0
    formula = "=SUM(AI59:AI63)"
    @eval_fn
    def AI58():
        range_1 = Input_RPS(35, 59, 35, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ58():
    # 'Input_RPS'!AJ58
    value = 0
    formula = "=SUM(AJ59:AJ63)"
    @eval_fn
    def AJ58():
        range_1 = Input_RPS(36, 59, 36, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK58():
    # 'Input_RPS'!AK58
    value = 0
    formula = "=SUM(AK59:AK63)"
    @eval_fn
    def AK58():
        range_1 = Input_RPS(37, 59, 37, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL58():
    # 'Input_RPS'!AL58
    value = 0
    formula = "=SUM(AL59:AL63)"
    @eval_fn
    def AL58():
        range_1 = Input_RPS(38, 59, 38, 63)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C59():
    # 'Input_RPS'!C59
    value = "           HRD"

@register(Input_RPS)
class N59():
    # 'Input_RPS'!N59
    value = 0

@register(Input_RPS)
class O59():
    # 'Input_RPS'!O59
    value = 0

@register(Input_RPS)
class C60():
    # 'Input_RPS'!C60
    value = "           Kaheawa Wind Power (KWP)"

@register(Input_RPS)
class M60():
    # 'Input_RPS'!M60
    value = 0

@register(Input_RPS)
class N60():
    # 'Input_RPS'!N60
    value = 57000

@register(Input_RPS)
class O60():
    # 'Input_RPS'!O60
    value = 126000

@register(Input_RPS)
class C61():
    # 'Input_RPS'!C61
    value = "           Lalamilo Wind Farm"

@register(Input_RPS)
class N61():
    # 'Input_RPS'!N61
    value = 0

@register(Input_RPS)
class O61():
    # 'Input_RPS'!O61
    value = 0

@register(Input_RPS)
class C62():
    # 'Input_RPS'!C62
    value = "           Pikini Nui"

@register(Input_RPS)
class N62():
    # 'Input_RPS'!N62
    value = 0

@register(Input_RPS)
class O62():
    # 'Input_RPS'!O62
    value = 0

@register(Input_RPS)
class C63():
    # 'Input_RPS'!C63
    value = "           Other wind including Kamaoa"

@register(Input_RPS)
class N63():
    # 'Input_RPS'!N63
    value = 0

@register(Input_RPS)
class O63():
    # 'Input_RPS'!O63
    value = 0

@register(Input_RPS)
class C64():
    # 'Input_RPS'!C64
    value = "Biomass: "

@register(Input_RPS)
class G64():
    # 'Input_RPS'!G64
    value = 0
    formula = "=SUM(G65:G66)"
    @eval_fn
    def G64():
        range_1 = Input_RPS(7, 65, 7, 66)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H64():
    # 'Input_RPS'!H64
    value = 0
    formula = "=SUM(H65:H66)"
    @eval_fn
    def H64():
        range_1 = Input_RPS(8, 65, 8, 66)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I64():
    # 'Input_RPS'!I64
    value = 0
    formula = "=SUM(I65:I66)"
    @eval_fn
    def I64():
        range_1 = Input_RPS(9, 65, 9, 66)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J64():
    # 'Input_RPS'!J64
    value = 0
    formula = "=SUM(J65:J66)"
    @eval_fn
    def J64():
        range_1 = Input_RPS(10, 65, 10, 66)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K64():
    # 'Input_RPS'!K64
    value = 0
    formula = "=SUM(K65:K66)"
    @eval_fn
    def K64():
        range_1 = Input_RPS(11, 65, 11, 66)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L64():
    # 'Input_RPS'!L64
    value = 0
    formula = "=SUM(L65:L66)"
    @eval_fn
    def L64():
        range_1 = Input_RPS(12, 65, 12, 66)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M64():
    # 'Input_RPS'!M64
    value = 0
    formula = "=SUM(M65:M66)"
    @eval_fn
    def M64():
        range_1 = Input_RPS(13, 65, 13, 66)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N64():
    # 'Input_RPS'!N64
    value = 0
    formula = "=SUM(N65:N66)"
    @eval_fn
    def N64():
        range_1 = Input_RPS(14, 65, 14, 66)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O64():
    # 'Input_RPS'!O64
    value = 0
    formula = "=SUM(O65:O66)"
    @eval_fn
    def O64():
        range_1 = Input_RPS(15, 65, 15, 66)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P64():
    # 'Input_RPS'!P64
    value = 53587

@register(Input_RPS)
class Q64():
    # 'Input_RPS'!Q64
    value = 38432

@register(Input_RPS)
class R64():
    # 'Input_RPS'!R64
    value = 44238

@register(Input_RPS)
class S64():
    # 'Input_RPS'!S64
    value = 43577

@register(Input_RPS)
class T64():
    # 'Input_RPS'!T64
    value = 39392

@register(Input_RPS)
class U64():
    # 'Input_RPS'!U64
    value = 41122

@register(Input_RPS)
class V64():
    # 'Input_RPS'!V64
    value = 43153

@register(Input_RPS)
class W64():
    # 'Input_RPS'!W64
    value = 30870

@register(Input_RPS)
class C65():
    # 'Input_RPS'!C65
    value = "                  Biomass"

@register(Input_RPS)
class N65():
    # 'Input_RPS'!N65
    value = 0

@register(Input_RPS)
class O65():
    # 'Input_RPS'!O65
    value = 0

@register(Input_RPS)
class C66():
    # 'Input_RPS'!C66
    value = "                  Municipal Solid Waste"

@register(Input_RPS)
class N66():
    # 'Input_RPS'!N66
    value = 0

@register(Input_RPS)
class O66():
    # 'Input_RPS'!O66
    value = 0

@register(Input_RPS)
class C67():
    # 'Input_RPS'!C67
    value = "Solar: "

@register(Input_RPS)
class G67():
    # 'Input_RPS'!G67
    value = 0
    formula = "=SUM(G68)"
    @eval_fn
    def G67():
        g68_1 = Input_RPS.G68()
        var_1 = SUM(g68_1)
        return var_1

@register(Input_RPS)
class H67():
    # 'Input_RPS'!H67
    value = 0
    formula = "=SUM(H68)"
    @eval_fn
    def H67():
        h68_1 = Input_RPS.H68()
        var_1 = SUM(h68_1)
        return var_1

@register(Input_RPS)
class I67():
    # 'Input_RPS'!I67
    value = 0
    formula = "=SUM(I68)"
    @eval_fn
    def I67():
        i68_1 = Input_RPS.I68()
        var_1 = SUM(i68_1)
        return var_1

@register(Input_RPS)
class J67():
    # 'Input_RPS'!J67
    value = 0
    formula = "=SUM(J68)"
    @eval_fn
    def J67():
        j68_1 = Input_RPS.J68()
        var_1 = SUM(j68_1)
        return var_1

@register(Input_RPS)
class K67():
    # 'Input_RPS'!K67
    value = 0
    formula = "=SUM(K68)"
    @eval_fn
    def K67():
        k68_1 = Input_RPS.K68()
        var_1 = SUM(k68_1)
        return var_1

@register(Input_RPS)
class L67():
    # 'Input_RPS'!L67
    value = 0
    formula = "=SUM(L68)"
    @eval_fn
    def L67():
        l68_1 = Input_RPS.L68()
        var_1 = SUM(l68_1)
        return var_1

@register(Input_RPS)
class M67():
    # 'Input_RPS'!M67
    value = 300
    formula = "=SUM(M68:M69)"
    @eval_fn
    def M67():
        range_1 = Input_RPS(13, 68, 13, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N67():
    # 'Input_RPS'!N67
    value = 700
    formula = "=SUM(N68:N69)"
    @eval_fn
    def N67():
        range_1 = Input_RPS(14, 68, 14, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O67():
    # 'Input_RPS'!O67
    value = 1300
    formula = "=SUM(O68:O69)"
    @eval_fn
    def O67():
        range_1 = Input_RPS(15, 68, 15, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P67():
    # 'Input_RPS'!P67
    value = 1906
    formula = "=SUM(P68:P69)"
    @eval_fn
    def P67():
        range_1 = Input_RPS(16, 68, 16, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q67():
    # 'Input_RPS'!Q67
    value = 6156
    formula = "=SUM(Q68:Q69)"
    @eval_fn
    def Q67():
        range_1 = Input_RPS(17, 68, 17, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R67():
    # 'Input_RPS'!R67
    value = 9809
    formula = "=SUM(R68:R69)"
    @eval_fn
    def R67():
        range_1 = Input_RPS(18, 68, 18, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S67():
    # 'Input_RPS'!S67
    value = 14932
    formula = "=SUM(S68:S69)"
    @eval_fn
    def S67():
        range_1 = Input_RPS(19, 68, 19, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T67():
    # 'Input_RPS'!T67
    value = 31968
    formula = "=SUM(T68:T69)"
    @eval_fn
    def T67():
        range_1 = Input_RPS(20, 68, 20, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U67():
    # 'Input_RPS'!U67
    value = 52614
    formula = "=SUM(U68:U69)"
    @eval_fn
    def U67():
        range_1 = Input_RPS(21, 68, 21, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V67():
    # 'Input_RPS'!V67
    value = 71223
    formula = "=SUM(V68:V69)"
    @eval_fn
    def V67():
        range_1 = Input_RPS(22, 68, 22, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W67():
    # 'Input_RPS'!W67
    value = 96860
    formula = "=SUM(W68:W69)"
    @eval_fn
    def W67():
        range_1 = Input_RPS(23, 68, 23, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class X67():
    # 'Input_RPS'!X67
    value = 0
    formula = "=SUM(X68:X69)"
    @eval_fn
    def X67():
        range_1 = Input_RPS(24, 68, 24, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y67():
    # 'Input_RPS'!Y67
    value = 0
    formula = "=SUM(Y68:Y69)"
    @eval_fn
    def Y67():
        range_1 = Input_RPS(25, 68, 25, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z67():
    # 'Input_RPS'!Z67
    value = 0
    formula = "=SUM(Z68:Z69)"
    @eval_fn
    def Z67():
        range_1 = Input_RPS(26, 68, 26, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA67():
    # 'Input_RPS'!AA67
    value = 0
    formula = "=SUM(AA68:AA69)"
    @eval_fn
    def AA67():
        range_1 = Input_RPS(27, 68, 27, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB67():
    # 'Input_RPS'!AB67
    value = 0
    formula = "=SUM(AB68:AB69)"
    @eval_fn
    def AB67():
        range_1 = Input_RPS(28, 68, 28, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC67():
    # 'Input_RPS'!AC67
    value = 0
    formula = "=SUM(AC68:AC69)"
    @eval_fn
    def AC67():
        range_1 = Input_RPS(29, 68, 29, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD67():
    # 'Input_RPS'!AD67
    value = 0
    formula = "=SUM(AD68:AD69)"
    @eval_fn
    def AD67():
        range_1 = Input_RPS(30, 68, 30, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE67():
    # 'Input_RPS'!AE67
    value = 0
    formula = "=SUM(AE68:AE69)"
    @eval_fn
    def AE67():
        range_1 = Input_RPS(31, 68, 31, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF67():
    # 'Input_RPS'!AF67
    value = 0
    formula = "=SUM(AF68:AF69)"
    @eval_fn
    def AF67():
        range_1 = Input_RPS(32, 68, 32, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG67():
    # 'Input_RPS'!AG67
    value = 0
    formula = "=SUM(AG68:AG69)"
    @eval_fn
    def AG67():
        range_1 = Input_RPS(33, 68, 33, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH67():
    # 'Input_RPS'!AH67
    value = 0
    formula = "=SUM(AH68:AH69)"
    @eval_fn
    def AH67():
        range_1 = Input_RPS(34, 68, 34, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI67():
    # 'Input_RPS'!AI67
    value = 0
    formula = "=SUM(AI68:AI69)"
    @eval_fn
    def AI67():
        range_1 = Input_RPS(35, 68, 35, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ67():
    # 'Input_RPS'!AJ67
    value = 0
    formula = "=SUM(AJ68:AJ69)"
    @eval_fn
    def AJ67():
        range_1 = Input_RPS(36, 68, 36, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK67():
    # 'Input_RPS'!AK67
    value = 0
    formula = "=SUM(AK68:AK69)"
    @eval_fn
    def AK67():
        range_1 = Input_RPS(37, 68, 37, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL67():
    # 'Input_RPS'!AL67
    value = 0
    formula = "=SUM(AL68:AL69)"
    @eval_fn
    def AL67():
        range_1 = Input_RPS(38, 68, 38, 69)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C68():
    # 'Input_RPS'!C68
    value = "            Photovoltaic"

@register(Input_RPS)
class M68():
    # 'Input_RPS'!M68
    value = 300

@register(Input_RPS)
class N68():
    # 'Input_RPS'!N68
    value = 700

@register(Input_RPS)
class O68():
    # 'Input_RPS'!O68
    value = 1300

@register(Input_RPS)
class P68():
    # 'Input_RPS'!P68
    value = 1906

@register(Input_RPS)
class Q68():
    # 'Input_RPS'!Q68
    value = 4766

@register(Input_RPS)
class R68():
    # 'Input_RPS'!R68
    value = 8039

@register(Input_RPS)
class S68():
    # 'Input_RPS'!S68
    value = 13041

@register(Input_RPS)
class T68():
    # 'Input_RPS'!T68
    value = 28474

@register(Input_RPS)
class U68():
    # 'Input_RPS'!U68
    value = 47517

@register(Input_RPS)
class V68():
    # 'Input_RPS'!V68
    value = 65899

@register(Input_RPS)
class W68():
    # 'Input_RPS'!W68
    value = 88956

@register(Input_RPS)
class C69():
    # 'Input_RPS'!C69
    value = "            Utility Solar"

@register(Input_RPS)
class M69():
    # 'Input_RPS'!M69
    value = 0

@register(Input_RPS)
class N69():
    # 'Input_RPS'!N69
    value = 0

@register(Input_RPS)
class O69():
    # 'Input_RPS'!O69
    value = 0

@register(Input_RPS)
class P69():
    # 'Input_RPS'!P69
    value = 0

@register(Input_RPS)
class Q69():
    # 'Input_RPS'!Q69
    value = 1390

@register(Input_RPS)
class R69():
    # 'Input_RPS'!R69
    value = 1770

@register(Input_RPS)
class S69():
    # 'Input_RPS'!S69
    value = 1891

@register(Input_RPS)
class T69():
    # 'Input_RPS'!T69
    value = 3494

@register(Input_RPS)
class U69():
    # 'Input_RPS'!U69
    value = 5097

@register(Input_RPS)
class V69():
    # 'Input_RPS'!V69
    value = 5324

@register(Input_RPS)
class W69():
    # 'Input_RPS'!W69
    value = 7904

@register(Input_RPS)
class C70():
    # 'Input_RPS'!C70
    value = "Biofuels: "

@register(Input_RPS)
class G70():
    # 'Input_RPS'!G70
    value = 0
    formula = "=SUM(G71)"
    @eval_fn
    def G70():
        g71_1 = Input_RPS.G71()
        var_1 = SUM(g71_1)
        return var_1

@register(Input_RPS)
class H70():
    # 'Input_RPS'!H70
    value = 0
    formula = "=SUM(H71)"
    @eval_fn
    def H70():
        h71_1 = Input_RPS.H71()
        var_1 = SUM(h71_1)
        return var_1

@register(Input_RPS)
class I70():
    # 'Input_RPS'!I70
    value = 0
    formula = "=SUM(I71)"
    @eval_fn
    def I70():
        i71_1 = Input_RPS.I71()
        var_1 = SUM(i71_1)
        return var_1

@register(Input_RPS)
class J70():
    # 'Input_RPS'!J70
    value = 0
    formula = "=SUM(J71)"
    @eval_fn
    def J70():
        j71_1 = Input_RPS.J71()
        var_1 = SUM(j71_1)
        return var_1

@register(Input_RPS)
class K70():
    # 'Input_RPS'!K70
    value = 0
    formula = "=SUM(K71)"
    @eval_fn
    def K70():
        k71_1 = Input_RPS.K71()
        var_1 = SUM(k71_1)
        return var_1

@register(Input_RPS)
class L70():
    # 'Input_RPS'!L70
    value = 0
    formula = "=SUM(L71)"
    @eval_fn
    def L70():
        l71_1 = Input_RPS.L71()
        var_1 = SUM(l71_1)
        return var_1

@register(Input_RPS)
class M70():
    # 'Input_RPS'!M70
    value = 100
    formula = "=SUM(M71)"
    @eval_fn
    def M70():
        m71_1 = Input_RPS.M71()
        var_1 = SUM(m71_1)
        return var_1

@register(Input_RPS)
class N70():
    # 'Input_RPS'!N70
    value = 200
    formula = "=SUM(N71)"
    @eval_fn
    def N70():
        n71_1 = Input_RPS.N71()
        var_1 = SUM(n71_1)
        return var_1

@register(Input_RPS)
class O70():
    # 'Input_RPS'!O70
    value = 1400
    formula = "=SUM(O71)"
    @eval_fn
    def O70():
        o71_1 = Input_RPS.O71()
        var_1 = SUM(o71_1)
        return var_1

@register(Input_RPS)
class P70():
    # 'Input_RPS'!P70
    value = 1539

@register(Input_RPS)
class Q70():
    # 'Input_RPS'!Q70
    value = 1570

@register(Input_RPS)
class R70():
    # 'Input_RPS'!R70
    value = 1585

@register(Input_RPS)
class S70():
    # 'Input_RPS'!S70
    value = 14532

@register(Input_RPS)
class T70():
    # 'Input_RPS'!T70
    value = 1348

@register(Input_RPS)
class U70():
    # 'Input_RPS'!U70
    value = 1281

@register(Input_RPS)
class V70():
    # 'Input_RPS'!V70
    value = 918

@register(Input_RPS)
class W70():
    # 'Input_RPS'!W70
    value = 988

@register(Input_RPS)
class C71():
    # 'Input_RPS'!C71
    value = "            Biodiesel"

@register(Input_RPS)
class M71():
    # 'Input_RPS'!M71
    value = 100

@register(Input_RPS)
class N71():
    # 'Input_RPS'!N71
    value = 200

@register(Input_RPS)
class O71():
    # 'Input_RPS'!O71
    value = 1400

@register(Input_RPS)
class A72():
    # 'Input_RPS'!A72
    value = "KIUCRenewable Electricity"
    formula = "=CONCATENATE(C72,B72)"
    @eval_fn
    def A72():
        c72_1 = Input_RPS.C72()
        b72_1 = Input_RPS.B72()
        var_1 = CONCATENATE(c72_1, b72_1)
        return var_1

@register(Input_RPS)
class B72():
    # 'Input_RPS'!B72
    value = "Renewable Electricity"

@register(Input_RPS)
class C72():
    # 'Input_RPS'!C72
    value = "KIUC"

@register(Input_RPS)
class D72():
    # 'Input_RPS'!D72
    value = "MWh"

@register(Input_RPS)
class E72():
    # 'Input_RPS'!E72
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://kauai.coopwebbuilder.com/sites/kauai.coopwebbuilder.com/files/irp2008_2008_kiuc_irp.pdf'''

@register(Input_RPS)
class K72():
    # 'Input_RPS'!K72
    value = 25556
    formula = "=SUM(K73:K96)"
    @eval_fn
    def K72():
        range_1 = Input_RPS(11, 73, 11, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L72():
    # 'Input_RPS'!L72
    value = 37838
    formula = "=SUM(L73:L96)"
    @eval_fn
    def L72():
        range_1 = Input_RPS(12, 73, 12, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M72():
    # 'Input_RPS'!M72
    value = 38131.8790708
    formula = "=SUM(M73:M96)"
    @eval_fn
    def M72():
        range_1 = Input_RPS(13, 73, 13, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N72():
    # 'Input_RPS'!N72
    value = 37735.2024614
    formula = "=SUM(N73:N96)"
    @eval_fn
    def N72():
        range_1 = Input_RPS(14, 73, 14, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O72():
    # 'Input_RPS'!O72
    value = 27408.5833964
    formula = "=SUM(O73:O96)"
    @eval_fn
    def O72():
        range_1 = Input_RPS(15, 73, 15, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P72():
    # 'Input_RPS'!P72
    value = 39169.816
    formula = "=SUM(P73:P96)"
    @eval_fn
    def P72():
        range_1 = Input_RPS(16, 73, 16, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q72():
    # 'Input_RPS'!Q72
    value = 41954.264
    formula = "=SUM(Q73:Q96)"
    @eval_fn
    def Q72():
        range_1 = Input_RPS(17, 73, 17, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R72():
    # 'Input_RPS'!R72
    value = 40426.773
    formula = "=SUM(R73:R96)"
    @eval_fn
    def R72():
        range_1 = Input_RPS(18, 73, 18, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S72():
    # 'Input_RPS'!S72
    value = 48828.11
    formula = "=SUM(S73:S96)"
    @eval_fn
    def S72():
        range_1 = Input_RPS(19, 73, 19, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T72():
    # 'Input_RPS'!T72
    value = 54063.765
    formula = "=SUM(T73:T96)"
    @eval_fn
    def T72():
        range_1 = Input_RPS(20, 73, 20, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U72():
    # 'Input_RPS'!U72
    value = 70115.5282527
    formula = "=SUM(U73:U96)"
    @eval_fn
    def U72():
        range_1 = Input_RPS(21, 73, 21, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V72():
    # 'Input_RPS'!V72
    value = 90605.9436318
    formula = "=SUM(V73:V96)"
    @eval_fn
    def V72():
        range_1 = Input_RPS(22, 73, 22, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W72():
    # 'Input_RPS'!W72
    value = 118014
    formula = "=SUM(W73:W96)"
    @eval_fn
    def W72():
        range_1 = Input_RPS(23, 73, 23, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class X72():
    # 'Input_RPS'!X72
    value = 0
    formula = "=SUM(X73:X96)"
    @eval_fn
    def X72():
        range_1 = Input_RPS(24, 73, 24, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y72():
    # 'Input_RPS'!Y72
    value = 0
    formula = "=SUM(Y73:Y96)"
    @eval_fn
    def Y72():
        range_1 = Input_RPS(25, 73, 25, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z72():
    # 'Input_RPS'!Z72
    value = 0
    formula = "=SUM(Z73:Z96)"
    @eval_fn
    def Z72():
        range_1 = Input_RPS(26, 73, 26, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA72():
    # 'Input_RPS'!AA72
    value = 0
    formula = "=SUM(AA73:AA96)"
    @eval_fn
    def AA72():
        range_1 = Input_RPS(27, 73, 27, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB72():
    # 'Input_RPS'!AB72
    value = 0
    formula = "=SUM(AB73:AB96)"
    @eval_fn
    def AB72():
        range_1 = Input_RPS(28, 73, 28, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC72():
    # 'Input_RPS'!AC72
    value = 0
    formula = "=SUM(AC73:AC96)"
    @eval_fn
    def AC72():
        range_1 = Input_RPS(29, 73, 29, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD72():
    # 'Input_RPS'!AD72
    value = 0
    formula = "=SUM(AD73:AD96)"
    @eval_fn
    def AD72():
        range_1 = Input_RPS(30, 73, 30, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE72():
    # 'Input_RPS'!AE72
    value = 0
    formula = "=SUM(AE73:AE96)"
    @eval_fn
    def AE72():
        range_1 = Input_RPS(31, 73, 31, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF72():
    # 'Input_RPS'!AF72
    value = 0
    formula = "=SUM(AF73:AF96)"
    @eval_fn
    def AF72():
        range_1 = Input_RPS(32, 73, 32, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG72():
    # 'Input_RPS'!AG72
    value = 0
    formula = "=SUM(AG73:AG96)"
    @eval_fn
    def AG72():
        range_1 = Input_RPS(33, 73, 33, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH72():
    # 'Input_RPS'!AH72
    value = 0
    formula = "=SUM(AH73:AH96)"
    @eval_fn
    def AH72():
        range_1 = Input_RPS(34, 73, 34, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI72():
    # 'Input_RPS'!AI72
    value = 0
    formula = "=SUM(AI73:AI96)"
    @eval_fn
    def AI72():
        range_1 = Input_RPS(35, 73, 35, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ72():
    # 'Input_RPS'!AJ72
    value = 0
    formula = "=SUM(AJ73:AJ96)"
    @eval_fn
    def AJ72():
        range_1 = Input_RPS(36, 73, 36, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK72():
    # 'Input_RPS'!AK72
    value = 0
    formula = "=SUM(AK73:AK96)"
    @eval_fn
    def AK72():
        range_1 = Input_RPS(37, 73, 37, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL72():
    # 'Input_RPS'!AL72
    value = 0
    formula = "=SUM(AL73:AL96)"
    @eval_fn
    def AL72():
        range_1 = Input_RPS(38, 73, 38, 96)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class B73():
    # 'Input_RPS'!B73
    value = "hydro"

@register(Input_RPS)
class C73():
    # 'Input_RPS'!C73
    value = "  KIUC Hydro"

@register(Input_RPS)
class K73():
    # 'Input_RPS'!K73
    value = 558

@register(Input_RPS)
class L73():
    # 'Input_RPS'!L73
    value = 4232

@register(Input_RPS)
class M73():
    # 'Input_RPS'!M73
    value = 4232

@register(Input_RPS)
class N73():
    # 'Input_RPS'!N73
    value = 4561

@register(Input_RPS)
class O73():
    # 'Input_RPS'!O73
    value = 926

@register(Input_RPS)
class P73():
    # 'Input_RPS'!P73
    value = 7968

@register(Input_RPS)
class Q73():
    # 'Input_RPS'!Q73
    value = 7454

@register(Input_RPS)
class R73():
    # 'Input_RPS'!R73
    value = 7896

@register(Input_RPS)
class S73():
    # 'Input_RPS'!S73
    value = 6974

@register(Input_RPS)
class T73():
    # 'Input_RPS'!T73
    value = 7591

@register(Input_RPS)
class U73():
    # 'Input_RPS'!U73
    value = 8063

@register(Input_RPS)
class V73():
    # 'Input_RPS'!V73
    value = 7598

@register(Input_RPS)
class W73():
    # 'Input_RPS'!W73
    value = 6961

@register(Input_RPS)
class B74():
    # 'Input_RPS'!B74
    value = "hydro"

@register(Input_RPS)
class C74():
    # 'Input_RPS'!C74
    value = "  Gay & Robinson"

@register(Input_RPS)
class K74():
    # 'Input_RPS'!K74
    value = 2521

@register(Input_RPS)
class L74():
    # 'Input_RPS'!L74
    value = 3501

@register(Input_RPS)
class M74():
    # 'Input_RPS'!M74
    value = 3501

@register(Input_RPS)
class N74():
    # 'Input_RPS'!N74
    value = 3921

@register(Input_RPS)
class O74():
    # 'Input_RPS'!O74
    value = 2845

@register(Input_RPS)
class P74():
    # 'Input_RPS'!P74
    value = 2385

@register(Input_RPS)
class Q74():
    # 'Input_RPS'!Q74
    value = 3574

@register(Input_RPS)
class R74():
    # 'Input_RPS'!R74
    value = 3450

@register(Input_RPS)
class S74():
    # 'Input_RPS'!S74
    value = 4871

@register(Input_RPS)
class T74():
    # 'Input_RPS'!T74
    value = 4142

@register(Input_RPS)
class U74():
    # 'Input_RPS'!U74
    value = 3355

@register(Input_RPS)
class V74():
    # 'Input_RPS'!V74
    value = 2878

@register(Input_RPS)
class W74():
    # 'Input_RPS'!W74
    value = 3051

@register(Input_RPS)
class B75():
    # 'Input_RPS'!B75
    value = "hydro"

@register(Input_RPS)
class C75():
    # 'Input_RPS'!C75
    value = "  Kauai Coffee"

@register(Input_RPS)
class K75():
    # 'Input_RPS'!K75
    value = 20331

@register(Input_RPS)
class L75():
    # 'Input_RPS'!L75
    value = 26292

@register(Input_RPS)
class M75():
    # 'Input_RPS'!M75
    value = 26292

@register(Input_RPS)
class N75():
    # 'Input_RPS'!N75
    value = 25613

@register(Input_RPS)
class O75():
    # 'Input_RPS'!O75
    value = 20612

@register(Input_RPS)
class P75():
    # 'Input_RPS'!P75
    value = 22149

@register(Input_RPS)
class Q75():
    # 'Input_RPS'!Q75
    value = 21756

@register(Input_RPS)
class R75():
    # 'Input_RPS'!R75
    value = 18296

@register(Input_RPS)
class S75():
    # 'Input_RPS'!S75
    value = 21208

@register(Input_RPS)
class T75():
    # 'Input_RPS'!T75
    value = 23038

@register(Input_RPS)
class U75():
    # 'Input_RPS'!U75
    value = 18501

@register(Input_RPS)
class V75():
    # 'Input_RPS'!V75
    value = 18693

@register(Input_RPS)
class W75():
    # 'Input_RPS'!W75
    value = 19556

@register(Input_RPS)
class B76():
    # 'Input_RPS'!B76
    value = "hydro"

@register(Input_RPS)
class C76():
    # 'Input_RPS'!C76
    value = "  KAA"

@register(Input_RPS)
class K76():
    # 'Input_RPS'!K76
    value = 2080

@register(Input_RPS)
class L76():
    # 'Input_RPS'!L76
    value = 3466

@register(Input_RPS)
class M76():
    # 'Input_RPS'!M76
    value = 3466

@register(Input_RPS)
class N76():
    # 'Input_RPS'!N76
    value = 3024

@register(Input_RPS)
class O76():
    # 'Input_RPS'!O76
    value = 2079

@register(Input_RPS)
class P76():
    # 'Input_RPS'!P76
    value = 3106

@register(Input_RPS)
class Q76():
    # 'Input_RPS'!Q76
    value = 4141

@register(Input_RPS)
class R76():
    # 'Input_RPS'!R76
    value = 4374

@register(Input_RPS)
class S76():
    # 'Input_RPS'!S76
    value = 5457

@register(Input_RPS)
class T76():
    # 'Input_RPS'!T76
    value = 3775

@register(Input_RPS)
class U76():
    # 'Input_RPS'!U76
    value = 3154

@register(Input_RPS)
class V76():
    # 'Input_RPS'!V76
    value = 4922

@register(Input_RPS)
class W76():
    # 'Input_RPS'!W76
    value = 3915

@register(Input_RPS)
class B77():
    # 'Input_RPS'!B77
    value = "hydro"

@register(Input_RPS)
class C77():
    # 'Input_RPS'!C77
    value = "  Green Energy Hydro"

@register(Input_RPS)
class K77():
    # 'Input_RPS'!K77
    value = 0

@register(Input_RPS)
class L77():
    # 'Input_RPS'!L77
    value = 0

@register(Input_RPS)
class M77():
    # 'Input_RPS'!M77
    value = 0

@register(Input_RPS)
class N77():
    # 'Input_RPS'!N77
    value = 0

@register(Input_RPS)
class O77():
    # 'Input_RPS'!O77
    value = 0

@register(Input_RPS)
class P77():
    # 'Input_RPS'!P77
    value = 0

@register(Input_RPS)
class Q77():
    # 'Input_RPS'!Q77
    value = 5

@register(Input_RPS)
class R77():
    # 'Input_RPS'!R77
    value = 189

@register(Input_RPS)
class S77():
    # 'Input_RPS'!S77
    value = 407

@register(Input_RPS)
class T77():
    # 'Input_RPS'!T77
    value = 366

@register(Input_RPS)
class U77():
    # 'Input_RPS'!U77
    value = 278

@register(Input_RPS)
class V77():
    # 'Input_RPS'!V77
    value = 200

@register(Input_RPS)
class W77():
    # 'Input_RPS'!W77
    value = 153

@register(Input_RPS)
class B78():
    # 'Input_RPS'!B78
    value = "solar"

@register(Input_RPS)
class C78():
    # 'Input_RPS'!C78
    value = "  Pioneer Solar"

@register(Input_RPS)
class S78():
    # 'Input_RPS'!S78
    value = 21

@register(Input_RPS)
class T78():
    # 'Input_RPS'!T78
    value = 23

@register(Input_RPS)
class U78():
    # 'Input_RPS'!U78
    value = 22

@register(Input_RPS)
class V78():
    # 'Input_RPS'!V78
    value = 372

@register(Input_RPS)
class W78():
    # 'Input_RPS'!W78
    value = 434

@register(Input_RPS)
class B79():
    # 'Input_RPS'!B79
    value = "solar"

@register(Input_RPS)
class C79():
    # 'Input_RPS'!C79
    value = "  Kapaa Solar"

@register(Input_RPS)
class K79():
    # 'Input_RPS'!K79
    value = 0

@register(Input_RPS)
class L79():
    # 'Input_RPS'!L79
    value = 0

@register(Input_RPS)
class M79():
    # 'Input_RPS'!M79
    value = 0

@register(Input_RPS)
class N79():
    # 'Input_RPS'!N79
    value = 0

@register(Input_RPS)
class O79():
    # 'Input_RPS'!O79
    value = 0

@register(Input_RPS)
class P79():
    # 'Input_RPS'!P79
    value = 0

@register(Input_RPS)
class Q79():
    # 'Input_RPS'!Q79
    value = 0

@register(Input_RPS)
class R79():
    # 'Input_RPS'!R79
    value = 0

@register(Input_RPS)
class S79():
    # 'Input_RPS'!S79
    value = 1468

@register(Input_RPS)
class T79():
    # 'Input_RPS'!T79
    value = 1858

@register(Input_RPS)
class U79():
    # 'Input_RPS'!U79
    value = 1827

@register(Input_RPS)
class V79():
    # 'Input_RPS'!V79
    value = 1759

@register(Input_RPS)
class W79():
    # 'Input_RPS'!W79
    value = 1787

@register(Input_RPS)
class B80():
    # 'Input_RPS'!B80
    value = "solar"

@register(Input_RPS)
class C80():
    # 'Input_RPS'!C80
    value = "  MP2 Kaneshiro Solar"

@register(Input_RPS)
class K80():
    # 'Input_RPS'!K80
    value = 0

@register(Input_RPS)
class L80():
    # 'Input_RPS'!L80
    value = 0

@register(Input_RPS)
class M80():
    # 'Input_RPS'!M80
    value = 0

@register(Input_RPS)
class N80():
    # 'Input_RPS'!N80
    value = 0

@register(Input_RPS)
class O80():
    # 'Input_RPS'!O80
    value = 0

@register(Input_RPS)
class P80():
    # 'Input_RPS'!P80
    value = 0

@register(Input_RPS)
class Q80():
    # 'Input_RPS'!Q80
    value = 0

@register(Input_RPS)
class R80():
    # 'Input_RPS'!R80
    value = 0

@register(Input_RPS)
class S80():
    # 'Input_RPS'!S80
    value = 0

@register(Input_RPS)
class T80():
    # 'Input_RPS'!T80
    value = 0

@register(Input_RPS)
class U80():
    # 'Input_RPS'!U80
    value = 530

@register(Input_RPS)
class V80():
    # 'Input_RPS'!V80
    value = 535

@register(Input_RPS)
class W80():
    # 'Input_RPS'!W80
    value = 547

@register(Input_RPS)
class B81():
    # 'Input_RPS'!B81
    value = "solar"

@register(Input_RPS)
class C81():
    # 'Input_RPS'!C81
    value = "  McBryde Solar"

@register(Input_RPS)
class K81():
    # 'Input_RPS'!K81
    value = 0

@register(Input_RPS)
class L81():
    # 'Input_RPS'!L81
    value = 0

@register(Input_RPS)
class M81():
    # 'Input_RPS'!M81
    value = 0

@register(Input_RPS)
class N81():
    # 'Input_RPS'!N81
    value = 0

@register(Input_RPS)
class O81():
    # 'Input_RPS'!O81
    value = 0

@register(Input_RPS)
class P81():
    # 'Input_RPS'!P81
    value = 0

@register(Input_RPS)
class Q81():
    # 'Input_RPS'!Q81
    value = 0

@register(Input_RPS)
class R81():
    # 'Input_RPS'!R81
    value = 0

@register(Input_RPS)
class S81():
    # 'Input_RPS'!S81
    value = 0

@register(Input_RPS)
class T81():
    # 'Input_RPS'!T81
    value = 0

@register(Input_RPS)
class U81():
    # 'Input_RPS'!U81
    value = 11945

@register(Input_RPS)
class V81():
    # 'Input_RPS'!V81
    value = 11393

@register(Input_RPS)
class W81():
    # 'Input_RPS'!W81
    value = 10772

@register(Input_RPS)
class B82():
    # 'Input_RPS'!B82
    value = "solar"

@register(Input_RPS)
class C82():
    # 'Input_RPS'!C82
    value = "  KRS2 Koloa Solar"

@register(Input_RPS)
class K82():
    # 'Input_RPS'!K82
    value = 0

@register(Input_RPS)
class L82():
    # 'Input_RPS'!L82
    value = 0

@register(Input_RPS)
class M82():
    # 'Input_RPS'!M82
    value = 0

@register(Input_RPS)
class N82():
    # 'Input_RPS'!N82
    value = 0

@register(Input_RPS)
class O82():
    # 'Input_RPS'!O82
    value = 0

@register(Input_RPS)
class P82():
    # 'Input_RPS'!P82
    value = 0

@register(Input_RPS)
class Q82():
    # 'Input_RPS'!Q82
    value = 0

@register(Input_RPS)
class R82():
    # 'Input_RPS'!R82
    value = 0

@register(Input_RPS)
class S82():
    # 'Input_RPS'!S82
    value = 0

@register(Input_RPS)
class T82():
    # 'Input_RPS'!T82
    value = 0

@register(Input_RPS)
class V82():
    # 'Input_RPS'!V82
    value = 10042

@register(Input_RPS)
class W82():
    # 'Input_RPS'!W82
    value = 20654

@register(Input_RPS)
class C83():
    # 'Input_RPS'!C83
    value = "KRS1 Anahola Solar"

@register(Input_RPS)
class W83():
    # 'Input_RPS'!W83
    value = 6456

@register(Input_RPS)
class C84():
    # 'Input_RPS'!C84
    value = "Green Energy Biomass"

@register(Input_RPS)
class W84():
    # 'Input_RPS'!W84
    value = 5465

@register(Input_RPS)
class C85():
    # 'Input_RPS'!C85
    value = "SolarCity / Tesla Solar and Storage"

@register(Input_RPS)
class C86():
    # 'Input_RPS'!C86
    value = "<empty row for future use>"

@register(Input_RPS)
class C87():
    # 'Input_RPS'!C87
    value = "<empty row for future use>"

@register(Input_RPS)
class C88():
    # 'Input_RPS'!C88
    value = "<empty row for future use>"

@register(Input_RPS)
class C89():
    # 'Input_RPS'!C89
    value = "<empty row for future use>"

@register(Input_RPS)
class C90():
    # 'Input_RPS'!C90
    value = "<empty row for future use>"

@register(Input_RPS)
class C91():
    # 'Input_RPS'!C91
    value = "NEM"

@register(Input_RPS)
class W91():
    # 'Input_RPS'!W91
    value = 1256

@register(Input_RPS)
class C92():
    # 'Input_RPS'!C92
    value = "NEM Pilot"

@register(Input_RPS)
class W92():
    # 'Input_RPS'!W92
    value = 3601

@register(Input_RPS)
class C93():
    # 'Input_RPS'!C93
    value = "Larger Systems (no buyback)"

@register(Input_RPS)
class W93():
    # 'Input_RPS'!W93
    value = 6912

@register(Input_RPS)
class C94():
    # 'Input_RPS'!C94
    value = "Schedule Q"

@register(Input_RPS)
class W94():
    # 'Input_RPS'!W94
    value = 26494

@register(Input_RPS)
class B95():
    # 'Input_RPS'!B95
    value = "biofuel"

@register(Input_RPS)
class C95():
    # 'Input_RPS'!C95
    value = "Waste Oil"

@register(Input_RPS)
class L95():
    # 'Input_RPS'!L95
    value = 257

@register(Input_RPS)
class M95():
    # 'Input_RPS'!M95
    value = 409

@register(Input_RPS)
class N95():
    # 'Input_RPS'!N95
    value = 323

@register(Input_RPS)
class O95():
    # 'Input_RPS'!O95
    value = 433

@register(Input_RPS)
class C96():
    # 'Input_RPS'!C96
    value = "Customer-Side Generation"

@register(Input_RPS)
class D96():
    # 'Input_RPS'!D96
    value = '''KIUC reports only customer "own use" portion of PV. These stats inlcude estimate of full PV generation. Annualized based on installed capacity'''

@register(Input_RPS)
class K96():
    # 'Input_RPS'!K96
    value = 66

@register(Input_RPS)
class L96():
    # 'Input_RPS'!L96
    value = 90

@register(Input_RPS)
class M96():
    # 'Input_RPS'!M96
    value = 231.879070758

@register(Input_RPS)
class N96():
    # 'Input_RPS'!N96
    value = 293.202461372

@register(Input_RPS)
class O96():
    # 'Input_RPS'!O96
    value = 513.58339639

@register(Input_RPS)
class P96():
    # 'Input_RPS'!P96
    value = 3561.816

@register(Input_RPS)
class Q96():
    # 'Input_RPS'!Q96
    value = 5024.264

@register(Input_RPS)
class R96():
    # 'Input_RPS'!R96
    value = 6221.773

@register(Input_RPS)
class S96():
    # 'Input_RPS'!S96
    value = 8422.11

@register(Input_RPS)
class T96():
    # 'Input_RPS'!T96
    value = 13270.765

@register(Input_RPS)
class U96():
    # 'Input_RPS'!U96
    value = 22440.5282527
    formula = "=+U98*$T$96/$T$98"
    @eval_fn
    def U96():
        u98_1 = Input_RPS.U98()
        t96_1 = Input_RPS.T96()
        var_1 = mult(u98_1, t96_1)
        t98_1 = Input_RPS.T98()
        var_2 = divide(var_1, t98_1)
        return var_2

@register(Input_RPS)
class V96():
    # 'Input_RPS'!V96
    value = 32213.9436318
    formula = "=+V98*$T$96/$T$98"
    @eval_fn
    def V96():
        v98_1 = Input_RPS.V98()
        t96_1 = Input_RPS.T96()
        var_1 = mult(v98_1, t96_1)
        t98_1 = Input_RPS.T98()
        var_2 = divide(var_1, t98_1)
        return var_2

@register(Input_RPS)
class A97():
    # 'Input_RPS'!A97
    value = "TotalRenewable Electricity"
    formula = "=CONCATENATE(C97,B97)"
    @eval_fn
    def A97():
        c97_1 = Input_RPS.C97()
        b97_1 = Input_RPS.B97()
        var_1 = CONCATENATE(c97_1, b97_1)
        return var_1

@register(Input_RPS)
class B97():
    # 'Input_RPS'!B97
    value = "Renewable Electricity"

@register(Input_RPS)
class C97():
    # 'Input_RPS'!C97
    value = "Total"

@register(Input_RPS)
class D97():
    # 'Input_RPS'!D97
    value = "MWh"

@register(Input_RPS)
class G97():
    # 'Input_RPS'!G97
    value = 642000
    formula = "=SUM(G3,G26,G49,G72)"
    @eval_fn
    def G97():
        g3_1 = Input_RPS.G3()
        g26_1 = Input_RPS.G26()
        g49_1 = Input_RPS.G49()
        g72_1 = Input_RPS.G72()
        var_1 = SUM(g3_1, g26_1, g49_1, g72_1)
        return var_1

@register(Input_RPS)
class H97():
    # 'Input_RPS'!H97
    value = 681000
    formula = "=SUM(H3,H26,H49,H72)"
    @eval_fn
    def H97():
        h3_1 = Input_RPS.H3()
        h26_1 = Input_RPS.H26()
        h49_1 = Input_RPS.H49()
        h72_1 = Input_RPS.H72()
        var_1 = SUM(h3_1, h26_1, h49_1, h72_1)
        return var_1

@register(Input_RPS)
class I97():
    # 'Input_RPS'!I97
    value = 615000
    formula = "=SUM(I3,I26,I49,I72)"
    @eval_fn
    def I97():
        i3_1 = Input_RPS.I3()
        i26_1 = Input_RPS.I26()
        i49_1 = Input_RPS.I49()
        i72_1 = Input_RPS.I72()
        var_1 = SUM(i3_1, i26_1, i49_1, i72_1)
        return var_1

@register(Input_RPS)
class J97():
    # 'Input_RPS'!J97
    value = 519000
    formula = "=SUM(J3,J26,J49,J72)"
    @eval_fn
    def J97():
        j3_1 = Input_RPS.J3()
        j26_1 = Input_RPS.J26()
        j49_1 = Input_RPS.J49()
        j72_1 = Input_RPS.J72()
        var_1 = SUM(j3_1, j26_1, j49_1, j72_1)
        return var_1

@register(Input_RPS)
class K97():
    # 'Input_RPS'!K97
    value = 676156
    formula = "=SUM(K3,K26,K49,K72)"
    @eval_fn
    def K97():
        k3_1 = Input_RPS.K3()
        k26_1 = Input_RPS.K26()
        k49_1 = Input_RPS.K49()
        k72_1 = Input_RPS.K72()
        var_1 = SUM(k3_1, k26_1, k49_1, k72_1)
        return var_1

@register(Input_RPS)
class L97():
    # 'Input_RPS'!L97
    value = 737938
    formula = "=SUM(L3,L26,L49,L72)"
    @eval_fn
    def L97():
        l3_1 = Input_RPS.L3()
        l26_1 = Input_RPS.L26()
        l49_1 = Input_RPS.L49()
        l72_1 = Input_RPS.L72()
        var_1 = SUM(l3_1, l26_1, l49_1, l72_1)
        return var_1

@register(Input_RPS)
class M97():
    # 'Input_RPS'!M97
    value = 716531.879071
    formula = "=SUM(M3,M26,M49,M72)"
    @eval_fn
    def M97():
        m3_1 = Input_RPS.M3()
        m26_1 = Input_RPS.M26()
        m49_1 = Input_RPS.M49()
        m72_1 = Input_RPS.M72()
        var_1 = SUM(m3_1, m26_1, m49_1, m72_1)
        return var_1

@register(Input_RPS)
class N97():
    # 'Input_RPS'!N97
    value = 865335.202461
    formula = "=SUM(N3,N26,N49,N72)"
    @eval_fn
    def N97():
        n3_1 = Input_RPS.N3()
        n26_1 = Input_RPS.N26()
        n49_1 = Input_RPS.N49()
        n72_1 = Input_RPS.N72()
        var_1 = SUM(n3_1, n26_1, n49_1, n72_1)
        return var_1

@register(Input_RPS)
class O97():
    # 'Input_RPS'!O97
    value = 945908.583396
    formula = "=SUM(O3,O26,O49,O72)"
    @eval_fn
    def O97():
        o3_1 = Input_RPS.O3()
        o26_1 = Input_RPS.O26()
        o49_1 = Input_RPS.O49()
        o72_1 = Input_RPS.O72()
        var_1 = SUM(o3_1, o26_1, o49_1, o72_1)
        return var_1

@register(Input_RPS)
class P97():
    # 'Input_RPS'!P97
    value = 977598.816
    formula = "=SUM(P3,P26,P49,P72)"
    @eval_fn
    def P97():
        p3_1 = Input_RPS.P3()
        p26_1 = Input_RPS.P26()
        p49_1 = Input_RPS.P49()
        p72_1 = Input_RPS.P72()
        var_1 = SUM(p3_1, p26_1, p49_1, p72_1)
        return var_1

@register(Input_RPS)
class Q97():
    # 'Input_RPS'!Q97
    value = 964817.264
    formula = "=SUM(Q3,Q26,Q49,Q72)"
    @eval_fn
    def Q97():
        q3_1 = Input_RPS.Q3()
        q26_1 = Input_RPS.Q26()
        q49_1 = Input_RPS.Q49()
        q72_1 = Input_RPS.Q72()
        var_1 = SUM(q3_1, q26_1, q49_1, q72_1)
        return var_1

@register(Input_RPS)
class R97():
    # 'Input_RPS'!R97
    value = 951417.773
    formula = "=SUM(R3,R26,R49,R72)"
    @eval_fn
    def R97():
        r3_1 = Input_RPS.R3()
        r26_1 = Input_RPS.R26()
        r49_1 = Input_RPS.R49()
        r72_1 = Input_RPS.R72()
        var_1 = SUM(r3_1, r26_1, r49_1, r72_1)
        return var_1

@register(Input_RPS)
class S97():
    # 'Input_RPS'!S97
    value = 1189273.11
    formula = "=SUM(S3,S26,S49,S72)"
    @eval_fn
    def S97():
        s3_1 = Input_RPS.S3()
        s26_1 = Input_RPS.S26()
        s49_1 = Input_RPS.S49()
        s72_1 = Input_RPS.S72()
        var_1 = SUM(s3_1, s26_1, s49_1, s72_1)
        return var_1

@register(Input_RPS)
class T97():
    # 'Input_RPS'!T97
    value = 1330297.765
    formula = "=SUM(T3,T26,T49,T72)"
    @eval_fn
    def T97():
        t3_1 = Input_RPS.T3()
        t26_1 = Input_RPS.T26()
        t49_1 = Input_RPS.T49()
        t72_1 = Input_RPS.T72()
        var_1 = SUM(t3_1, t26_1, t49_1, t72_1)
        return var_1

@register(Input_RPS)
class U97():
    # 'Input_RPS'!U97
    value = 1718566.52825
    formula = "=SUM(U3,U26,U49,U72)"
    @eval_fn
    def U97():
        u3_1 = Input_RPS.U3()
        u26_1 = Input_RPS.U26()
        u49_1 = Input_RPS.U49()
        u72_1 = Input_RPS.U72()
        var_1 = SUM(u3_1, u26_1, u49_1, u72_1)
        return var_1

@register(Input_RPS)
class V97():
    # 'Input_RPS'!V97
    value = 2004166.94363
    formula = "=SUM(V3,V26,V49,V72)"
    @eval_fn
    def V97():
        v3_1 = Input_RPS.V3()
        v26_1 = Input_RPS.V26()
        v49_1 = Input_RPS.V49()
        v72_1 = Input_RPS.V72()
        var_1 = SUM(v3_1, v26_1, v49_1, v72_1)
        return var_1

@register(Input_RPS)
class W97():
    # 'Input_RPS'!W97
    value = 2198786
    formula = "=SUM(W3,W26,W49,W72)"
    @eval_fn
    def W97():
        w3_1 = Input_RPS.W3()
        w26_1 = Input_RPS.W26()
        w49_1 = Input_RPS.W49()
        w72_1 = Input_RPS.W72()
        var_1 = SUM(w3_1, w26_1, w49_1, w72_1)
        return var_1

@register(Input_RPS)
class X97():
    # 'Input_RPS'!X97
    value = 0
    formula = "=SUM(X3,X26,X49,X72)"
    @eval_fn
    def X97():
        x3_1 = Input_RPS.X3()
        x26_1 = Input_RPS.X26()
        x49_1 = Input_RPS.X49()
        x72_1 = Input_RPS.X72()
        var_1 = SUM(x3_1, x26_1, x49_1, x72_1)
        return var_1

@register(Input_RPS)
class Y97():
    # 'Input_RPS'!Y97
    value = 0
    formula = "=SUM(Y3,Y26,Y49,Y72)"
    @eval_fn
    def Y97():
        y3_1 = Input_RPS.Y3()
        y26_1 = Input_RPS.Y26()
        y49_1 = Input_RPS.Y49()
        y72_1 = Input_RPS.Y72()
        var_1 = SUM(y3_1, y26_1, y49_1, y72_1)
        return var_1

@register(Input_RPS)
class Z97():
    # 'Input_RPS'!Z97
    value = 0
    formula = "=SUM(Z3,Z26,Z49,Z72)"
    @eval_fn
    def Z97():
        z3_1 = Input_RPS.Z3()
        z26_1 = Input_RPS.Z26()
        z49_1 = Input_RPS.Z49()
        z72_1 = Input_RPS.Z72()
        var_1 = SUM(z3_1, z26_1, z49_1, z72_1)
        return var_1

@register(Input_RPS)
class AA97():
    # 'Input_RPS'!AA97
    value = 0
    formula = "=SUM(AA3,AA26,AA49,AA72)"
    @eval_fn
    def AA97():
        aa3_1 = Input_RPS.AA3()
        aa26_1 = Input_RPS.AA26()
        aa49_1 = Input_RPS.AA49()
        aa72_1 = Input_RPS.AA72()
        var_1 = SUM(aa3_1, aa26_1, aa49_1, aa72_1)
        return var_1

@register(Input_RPS)
class AB97():
    # 'Input_RPS'!AB97
    value = 0
    formula = "=SUM(AB3,AB26,AB49,AB72)"
    @eval_fn
    def AB97():
        ab3_1 = Input_RPS.AB3()
        ab26_1 = Input_RPS.AB26()
        ab49_1 = Input_RPS.AB49()
        ab72_1 = Input_RPS.AB72()
        var_1 = SUM(ab3_1, ab26_1, ab49_1, ab72_1)
        return var_1

@register(Input_RPS)
class AC97():
    # 'Input_RPS'!AC97
    value = 0
    formula = "=SUM(AC3,AC26,AC49,AC72)"
    @eval_fn
    def AC97():
        ac3_1 = Input_RPS.AC3()
        ac26_1 = Input_RPS.AC26()
        ac49_1 = Input_RPS.AC49()
        ac72_1 = Input_RPS.AC72()
        var_1 = SUM(ac3_1, ac26_1, ac49_1, ac72_1)
        return var_1

@register(Input_RPS)
class AD97():
    # 'Input_RPS'!AD97
    value = 0
    formula = "=SUM(AD3,AD26,AD49,AD72)"
    @eval_fn
    def AD97():
        ad3_1 = Input_RPS.AD3()
        ad26_1 = Input_RPS.AD26()
        ad49_1 = Input_RPS.AD49()
        ad72_1 = Input_RPS.AD72()
        var_1 = SUM(ad3_1, ad26_1, ad49_1, ad72_1)
        return var_1

@register(Input_RPS)
class AE97():
    # 'Input_RPS'!AE97
    value = 0
    formula = "=SUM(AE3,AE26,AE49,AE72)"
    @eval_fn
    def AE97():
        ae3_1 = Input_RPS.AE3()
        ae26_1 = Input_RPS.AE26()
        ae49_1 = Input_RPS.AE49()
        ae72_1 = Input_RPS.AE72()
        var_1 = SUM(ae3_1, ae26_1, ae49_1, ae72_1)
        return var_1

@register(Input_RPS)
class AF97():
    # 'Input_RPS'!AF97
    value = 0
    formula = "=SUM(AF3,AF26,AF49,AF72)"
    @eval_fn
    def AF97():
        af3_1 = Input_RPS.AF3()
        af26_1 = Input_RPS.AF26()
        af49_1 = Input_RPS.AF49()
        af72_1 = Input_RPS.AF72()
        var_1 = SUM(af3_1, af26_1, af49_1, af72_1)
        return var_1

@register(Input_RPS)
class AG97():
    # 'Input_RPS'!AG97
    value = 0
    formula = "=SUM(AG3,AG26,AG49,AG72)"
    @eval_fn
    def AG97():
        ag3_1 = Input_RPS.AG3()
        ag26_1 = Input_RPS.AG26()
        ag49_1 = Input_RPS.AG49()
        ag72_1 = Input_RPS.AG72()
        var_1 = SUM(ag3_1, ag26_1, ag49_1, ag72_1)
        return var_1

@register(Input_RPS)
class AH97():
    # 'Input_RPS'!AH97
    value = 0
    formula = "=SUM(AH3,AH26,AH49,AH72)"
    @eval_fn
    def AH97():
        ah3_1 = Input_RPS.AH3()
        ah26_1 = Input_RPS.AH26()
        ah49_1 = Input_RPS.AH49()
        ah72_1 = Input_RPS.AH72()
        var_1 = SUM(ah3_1, ah26_1, ah49_1, ah72_1)
        return var_1

@register(Input_RPS)
class AI97():
    # 'Input_RPS'!AI97
    value = 0
    formula = "=SUM(AI3,AI26,AI49,AI72)"
    @eval_fn
    def AI97():
        ai3_1 = Input_RPS.AI3()
        ai26_1 = Input_RPS.AI26()
        ai49_1 = Input_RPS.AI49()
        ai72_1 = Input_RPS.AI72()
        var_1 = SUM(ai3_1, ai26_1, ai49_1, ai72_1)
        return var_1

@register(Input_RPS)
class AJ97():
    # 'Input_RPS'!AJ97
    value = 0
    formula = "=SUM(AJ3,AJ26,AJ49,AJ72)"
    @eval_fn
    def AJ97():
        aj3_1 = Input_RPS.AJ3()
        aj26_1 = Input_RPS.AJ26()
        aj49_1 = Input_RPS.AJ49()
        aj72_1 = Input_RPS.AJ72()
        var_1 = SUM(aj3_1, aj26_1, aj49_1, aj72_1)
        return var_1

@register(Input_RPS)
class AK97():
    # 'Input_RPS'!AK97
    value = 0
    formula = "=SUM(AK3,AK26,AK49,AK72)"
    @eval_fn
    def AK97():
        ak3_1 = Input_RPS.AK3()
        ak26_1 = Input_RPS.AK26()
        ak49_1 = Input_RPS.AK49()
        ak72_1 = Input_RPS.AK72()
        var_1 = SUM(ak3_1, ak26_1, ak49_1, ak72_1)
        return var_1

@register(Input_RPS)
class AL97():
    # 'Input_RPS'!AL97
    value = 0
    formula = "=SUM(AL3,AL26,AL49,AL72)"
    @eval_fn
    def AL97():
        al3_1 = Input_RPS.AL3()
        al26_1 = Input_RPS.AL26()
        al49_1 = Input_RPS.AL49()
        al72_1 = Input_RPS.AL72()
        var_1 = SUM(al3_1, al26_1, al49_1, al72_1)
        return var_1

@register(Input_RPS)
class A98():
    # 'Input_RPS'!A98
    value = "EEPS"

@register(Input_RPS)
class M98():
    # 'Input_RPS'!M98
    value = 121

@register(Input_RPS)
class N98():
    # 'Input_RPS'!N98
    value = 153

@register(Input_RPS)
class O98():
    # 'Input_RPS'!O98
    value = 268

@register(Input_RPS)
class P98():
    # 'Input_RPS'!P98
    value = 1712

@register(Input_RPS)
class Q98():
    # 'Input_RPS'!Q98
    value = 3316

@register(Input_RPS)
class R98():
    # 'Input_RPS'!R98
    value = 4499

@register(Input_RPS)
class S98():
    # 'Input_RPS'!S98
    value = 5176

@register(Input_RPS)
class T98():
    # 'Input_RPS'!T98
    value = 6925

@register(Input_RPS)
class U98():
    # 'Input_RPS'!U98
    value = 11710

@register(Input_RPS)
class V98():
    # 'Input_RPS'!V98
    value = 16810

@register(Input_RPS)
class C99():
    # 'Input_RPS'!C99
    value = "HECO"

@register(Input_RPS)
class D99():
    # 'Input_RPS'!D99
    value = "MWh"

@register(Input_RPS)
class E99():
    # 'Input_RPS'!E99
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Input_RPS)
class X99():
    # 'Input_RPS'!X99
    value = "Quantities estimated: HECO does not report these statistics on RPS reports starting 2015"

@register(Input_RPS)
class C100():
    # 'Input_RPS'!C100
    value = "  Displacement Tech: Photovoltaic Systems"

@register(Input_RPS)
class C101():
    # 'Input_RPS'!C101
    value = "  Displacement Tech: Solar Water Heating Utility"

@register(Input_RPS)
class M101():
    # 'Input_RPS'!M101
    value = 51000

@register(Input_RPS)
class N101():
    # 'Input_RPS'!N101
    value = 58000

@register(Input_RPS)
class O101():
    # 'Input_RPS'!O101
    value = 66000

@register(Input_RPS)
class P101():
    # 'Input_RPS'!P101
    value = 75988

@register(Input_RPS)
class Q101():
    # 'Input_RPS'!Q101
    value = 86967

@register(Input_RPS)
class R101():
    # 'Input_RPS'!R101
    value = 122801

@register(Input_RPS)
class S101():
    # 'Input_RPS'!S101
    value = 129314

@register(Input_RPS)
class T101():
    # 'Input_RPS'!T101
    value = 113541

@register(Input_RPS)
class U101():
    # 'Input_RPS'!U101
    value = 100997

@register(Input_RPS)
class V101():
    # 'Input_RPS'!V101
    value = 86719

@register(Input_RPS)
class W101():
    # 'Input_RPS'!W101
    value = 72441
    formula = "=+V101+V101-U101"
    @eval_fn
    def W101():
        v101_1 = Input_RPS.V101()
        v101_2 = Input_RPS.V101()
        var_1 = add(v101_1, v101_2)
        u101_1 = Input_RPS.U101()
        var_2 = sub(var_1, u101_1)
        return var_2

@register(Input_RPS)
class C102():
    # 'Input_RPS'!C102
    value = "  Displacement Tech: Solar Water Heating PBFA"

@register(Input_RPS)
class M102():
    # 'Input_RPS'!M102
    value = 0

@register(Input_RPS)
class N102():
    # 'Input_RPS'!N102
    value = 0

@register(Input_RPS)
class O102():
    # 'Input_RPS'!O102
    value = 0

@register(Input_RPS)
class P102():
    # 'Input_RPS'!P102
    value = 0

@register(Input_RPS)
class Q102():
    # 'Input_RPS'!Q102
    value = 0

@register(Input_RPS)
class R102():
    # 'Input_RPS'!R102
    value = 0

@register(Input_RPS)
class S102():
    # 'Input_RPS'!S102
    value = 0

@register(Input_RPS)
class T102():
    # 'Input_RPS'!T102
    value = 18471

@register(Input_RPS)
class U102():
    # 'Input_RPS'!U102
    value = 21945

@register(Input_RPS)
class V102():
    # 'Input_RPS'!V102
    value = 24915

@register(Input_RPS)
class W102():
    # 'Input_RPS'!W102
    value = 27885
    formula = "=+V102+V102-U102"
    @eval_fn
    def W102():
        v102_1 = Input_RPS.V102()
        v102_2 = Input_RPS.V102()
        var_1 = add(v102_1, v102_2)
        u102_1 = Input_RPS.U102()
        var_2 = sub(var_1, u102_1)
        return var_2

@register(Input_RPS)
class C103():
    # 'Input_RPS'!C103
    value = "  Energy Efficiency Technologies Total"

@register(Input_RPS)
class M103():
    # 'Input_RPS'!M103
    value = 292000

@register(Input_RPS)
class N103():
    # 'Input_RPS'!N103
    value = 340000

@register(Input_RPS)
class O103():
    # 'Input_RPS'!O103
    value = 453000

@register(Input_RPS)
class P103():
    # 'Input_RPS'!P103
    value = 604007

@register(Input_RPS)
class Q103():
    # 'Input_RPS'!Q103
    value = 651278

@register(Input_RPS)
class R103():
    # 'Input_RPS'!R103
    value = 738337

@register(Input_RPS)
class S103():
    # 'Input_RPS'!S103
    value = 821136

@register(Input_RPS)
class T103():
    # 'Input_RPS'!T103
    value = 958155

@register(Input_RPS)
class U103():
    # 'Input_RPS'!U103
    value = 1039167

@register(Input_RPS)
class V103():
    # 'Input_RPS'!V103
    value = 1117117

@register(Input_RPS)
class W103():
    # 'Input_RPS'!W103
    value = 1195067
    formula = "=+V103+V103-U103"
    @eval_fn
    def W103():
        v103_1 = Input_RPS.V103()
        v103_2 = Input_RPS.V103()
        var_1 = add(v103_1, v103_2)
        u103_1 = Input_RPS.U103()
        var_2 = sub(var_1, u103_1)
        return var_2

@register(Input_RPS)
class C104():
    # 'Input_RPS'!C104
    value = "Total EE"

@register(Input_RPS)
class M104():
    # 'Input_RPS'!M104
    value = 343000
    formula = "=SUM(M100:M103)"
    @eval_fn
    def M104():
        range_1 = Input_RPS(13, 100, 13, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N104():
    # 'Input_RPS'!N104
    value = 398000
    formula = "=SUM(N100:N103)"
    @eval_fn
    def N104():
        range_1 = Input_RPS(14, 100, 14, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O104():
    # 'Input_RPS'!O104
    value = 519000
    formula = "=SUM(O100:O103)"
    @eval_fn
    def O104():
        range_1 = Input_RPS(15, 100, 15, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P104():
    # 'Input_RPS'!P104
    value = 679995
    formula = "=SUM(P100:P103)"
    @eval_fn
    def P104():
        range_1 = Input_RPS(16, 100, 16, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q104():
    # 'Input_RPS'!Q104
    value = 738245
    formula = "=SUM(Q100:Q103)"
    @eval_fn
    def Q104():
        range_1 = Input_RPS(17, 100, 17, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R104():
    # 'Input_RPS'!R104
    value = 861138
    formula = "=SUM(R100:R103)"
    @eval_fn
    def R104():
        range_1 = Input_RPS(18, 100, 18, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S104():
    # 'Input_RPS'!S104
    value = 950450
    formula = "=SUM(S100:S103)"
    @eval_fn
    def S104():
        range_1 = Input_RPS(19, 100, 19, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T104():
    # 'Input_RPS'!T104
    value = 1090167
    formula = "=SUM(T100:T103)"
    @eval_fn
    def T104():
        range_1 = Input_RPS(20, 100, 20, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U104():
    # 'Input_RPS'!U104
    value = 1162109
    formula = "=SUM(U100:U103)"
    @eval_fn
    def U104():
        range_1 = Input_RPS(21, 100, 21, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V104():
    # 'Input_RPS'!V104
    value = 1228751
    formula = "=SUM(V100:V103)"
    @eval_fn
    def V104():
        range_1 = Input_RPS(22, 100, 22, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W104():
    # 'Input_RPS'!W104
    value = 1295393
    formula = "=SUM(W100:W103)"
    @eval_fn
    def W104():
        range_1 = Input_RPS(23, 100, 23, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class X104():
    # 'Input_RPS'!X104
    value = 0
    formula = "=SUM(X100:X103)"
    @eval_fn
    def X104():
        range_1 = Input_RPS(24, 100, 24, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y104():
    # 'Input_RPS'!Y104
    value = 0
    formula = "=SUM(Y100:Y103)"
    @eval_fn
    def Y104():
        range_1 = Input_RPS(25, 100, 25, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z104():
    # 'Input_RPS'!Z104
    value = 0
    formula = "=SUM(Z100:Z103)"
    @eval_fn
    def Z104():
        range_1 = Input_RPS(26, 100, 26, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA104():
    # 'Input_RPS'!AA104
    value = 0
    formula = "=SUM(AA100:AA103)"
    @eval_fn
    def AA104():
        range_1 = Input_RPS(27, 100, 27, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB104():
    # 'Input_RPS'!AB104
    value = 0
    formula = "=SUM(AB100:AB103)"
    @eval_fn
    def AB104():
        range_1 = Input_RPS(28, 100, 28, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC104():
    # 'Input_RPS'!AC104
    value = 0
    formula = "=SUM(AC100:AC103)"
    @eval_fn
    def AC104():
        range_1 = Input_RPS(29, 100, 29, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD104():
    # 'Input_RPS'!AD104
    value = 0
    formula = "=SUM(AD100:AD103)"
    @eval_fn
    def AD104():
        range_1 = Input_RPS(30, 100, 30, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE104():
    # 'Input_RPS'!AE104
    value = 0
    formula = "=SUM(AE100:AE103)"
    @eval_fn
    def AE104():
        range_1 = Input_RPS(31, 100, 31, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF104():
    # 'Input_RPS'!AF104
    value = 0
    formula = "=SUM(AF100:AF103)"
    @eval_fn
    def AF104():
        range_1 = Input_RPS(32, 100, 32, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG104():
    # 'Input_RPS'!AG104
    value = 0
    formula = "=SUM(AG100:AG103)"
    @eval_fn
    def AG104():
        range_1 = Input_RPS(33, 100, 33, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH104():
    # 'Input_RPS'!AH104
    value = 0
    formula = "=SUM(AH100:AH103)"
    @eval_fn
    def AH104():
        range_1 = Input_RPS(34, 100, 34, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI104():
    # 'Input_RPS'!AI104
    value = 0
    formula = "=SUM(AI100:AI103)"
    @eval_fn
    def AI104():
        range_1 = Input_RPS(35, 100, 35, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ104():
    # 'Input_RPS'!AJ104
    value = 0
    formula = "=SUM(AJ100:AJ103)"
    @eval_fn
    def AJ104():
        range_1 = Input_RPS(36, 100, 36, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK104():
    # 'Input_RPS'!AK104
    value = 0
    formula = "=SUM(AK100:AK103)"
    @eval_fn
    def AK104():
        range_1 = Input_RPS(37, 100, 37, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL104():
    # 'Input_RPS'!AL104
    value = 0
    formula = "=SUM(AL100:AL103)"
    @eval_fn
    def AL104():
        range_1 = Input_RPS(38, 100, 38, 103)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C105():
    # 'Input_RPS'!C105
    value = "HELCO"

@register(Input_RPS)
class D105():
    # 'Input_RPS'!D105
    value = "MWh"

@register(Input_RPS)
class E105():
    # 'Input_RPS'!E105
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Input_RPS)
class C106():
    # 'Input_RPS'!C106
    value = "  Displacement Tech: Photovoltaic Systems"

@register(Input_RPS)
class C107():
    # 'Input_RPS'!C107
    value = "  Displacement Tech: Solar Water Heating Utility"

@register(Input_RPS)
class M107():
    # 'Input_RPS'!M107
    value = 10000

@register(Input_RPS)
class N107():
    # 'Input_RPS'!N107
    value = 11000

@register(Input_RPS)
class O107():
    # 'Input_RPS'!O107
    value = 13000

@register(Input_RPS)
class P107():
    # 'Input_RPS'!P107
    value = 13862

@register(Input_RPS)
class Q107():
    # 'Input_RPS'!Q107
    value = 14501

@register(Input_RPS)
class R107():
    # 'Input_RPS'!R107
    value = 19572

@register(Input_RPS)
class S107():
    # 'Input_RPS'!S107
    value = 20678

@register(Input_RPS)
class T107():
    # 'Input_RPS'!T107
    value = 17919

@register(Input_RPS)
class U107():
    # 'Input_RPS'!U107
    value = 16678

@register(Input_RPS)
class V107():
    # 'Input_RPS'!V107
    value = 15317

@register(Input_RPS)
class W107():
    # 'Input_RPS'!W107
    value = 13956
    formula = "=+V107+V107-U107"
    @eval_fn
    def W107():
        v107_1 = Input_RPS.V107()
        v107_2 = Input_RPS.V107()
        var_1 = add(v107_1, v107_2)
        u107_1 = Input_RPS.U107()
        var_2 = sub(var_1, u107_1)
        return var_2

@register(Input_RPS)
class C108():
    # 'Input_RPS'!C108
    value = "  Displacement Tech: Solar Water Heating PBFA"

@register(Input_RPS)
class M108():
    # 'Input_RPS'!M108
    value = 0

@register(Input_RPS)
class N108():
    # 'Input_RPS'!N108
    value = 0

@register(Input_RPS)
class O108():
    # 'Input_RPS'!O108
    value = 0

@register(Input_RPS)
class P108():
    # 'Input_RPS'!P108
    value = 0

@register(Input_RPS)
class Q108():
    # 'Input_RPS'!Q108
    value = 0

@register(Input_RPS)
class R108():
    # 'Input_RPS'!R108
    value = 0

@register(Input_RPS)
class S108():
    # 'Input_RPS'!S108
    value = 0

@register(Input_RPS)
class T108():
    # 'Input_RPS'!T108
    value = 3934

@register(Input_RPS)
class U108():
    # 'Input_RPS'!U108
    value = 4628

@register(Input_RPS)
class V108():
    # 'Input_RPS'!V108
    value = 5081

@register(Input_RPS)
class W108():
    # 'Input_RPS'!W108
    value = 5534
    formula = "=+V108+V108-U108"
    @eval_fn
    def W108():
        v108_1 = Input_RPS.V108()
        v108_2 = Input_RPS.V108()
        var_1 = add(v108_1, v108_2)
        u108_1 = Input_RPS.U108()
        var_2 = sub(var_1, u108_1)
        return var_2

@register(Input_RPS)
class C109():
    # 'Input_RPS'!C109
    value = "  Energy Efficiency Technologies Total"

@register(Input_RPS)
class M109():
    # 'Input_RPS'!M109
    value = 49000

@register(Input_RPS)
class N109():
    # 'Input_RPS'!N109
    value = 54000

@register(Input_RPS)
class O109():
    # 'Input_RPS'!O109
    value = 57000

@register(Input_RPS)
class P109():
    # 'Input_RPS'!P109
    value = 47051

@register(Input_RPS)
class Q109():
    # 'Input_RPS'!Q109
    value = 49760

@register(Input_RPS)
class R109():
    # 'Input_RPS'!R109
    value = 62359

@register(Input_RPS)
class S109():
    # 'Input_RPS'!S109
    value = 76622

@register(Input_RPS)
class T109():
    # 'Input_RPS'!T109
    value = 97765

@register(Input_RPS)
class U109():
    # 'Input_RPS'!U109
    value = 114116

@register(Input_RPS)
class V109():
    # 'Input_RPS'!V109
    value = 123070

@register(Input_RPS)
class W109():
    # 'Input_RPS'!W109
    value = 132024
    formula = "=+V109+V109-U109"
    @eval_fn
    def W109():
        v109_1 = Input_RPS.V109()
        v109_2 = Input_RPS.V109()
        var_1 = add(v109_1, v109_2)
        u109_1 = Input_RPS.U109()
        var_2 = sub(var_1, u109_1)
        return var_2

@register(Input_RPS)
class C110():
    # 'Input_RPS'!C110
    value = "Total EE"

@register(Input_RPS)
class M110():
    # 'Input_RPS'!M110
    value = 59000
    formula = "=SUM(M106:M109)"
    @eval_fn
    def M110():
        range_1 = Input_RPS(13, 106, 13, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N110():
    # 'Input_RPS'!N110
    value = 65000
    formula = "=SUM(N106:N109)"
    @eval_fn
    def N110():
        range_1 = Input_RPS(14, 106, 14, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O110():
    # 'Input_RPS'!O110
    value = 70000
    formula = "=SUM(O106:O109)"
    @eval_fn
    def O110():
        range_1 = Input_RPS(15, 106, 15, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P110():
    # 'Input_RPS'!P110
    value = 60913
    formula = "=SUM(P106:P109)"
    @eval_fn
    def P110():
        range_1 = Input_RPS(16, 106, 16, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q110():
    # 'Input_RPS'!Q110
    value = 64261
    formula = "=SUM(Q106:Q109)"
    @eval_fn
    def Q110():
        range_1 = Input_RPS(17, 106, 17, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R110():
    # 'Input_RPS'!R110
    value = 81931
    formula = "=SUM(R106:R109)"
    @eval_fn
    def R110():
        range_1 = Input_RPS(18, 106, 18, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S110():
    # 'Input_RPS'!S110
    value = 97300
    formula = "=SUM(S106:S109)"
    @eval_fn
    def S110():
        range_1 = Input_RPS(19, 106, 19, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T110():
    # 'Input_RPS'!T110
    value = 119618
    formula = "=SUM(T106:T109)"
    @eval_fn
    def T110():
        range_1 = Input_RPS(20, 106, 20, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U110():
    # 'Input_RPS'!U110
    value = 135422
    formula = "=SUM(U106:U109)"
    @eval_fn
    def U110():
        range_1 = Input_RPS(21, 106, 21, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V110():
    # 'Input_RPS'!V110
    value = 143468
    formula = "=SUM(V106:V109)"
    @eval_fn
    def V110():
        range_1 = Input_RPS(22, 106, 22, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W110():
    # 'Input_RPS'!W110
    value = 151514
    formula = "=SUM(W106:W109)"
    @eval_fn
    def W110():
        range_1 = Input_RPS(23, 106, 23, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class X110():
    # 'Input_RPS'!X110
    value = 0
    formula = "=SUM(X106:X109)"
    @eval_fn
    def X110():
        range_1 = Input_RPS(24, 106, 24, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y110():
    # 'Input_RPS'!Y110
    value = 0
    formula = "=SUM(Y106:Y109)"
    @eval_fn
    def Y110():
        range_1 = Input_RPS(25, 106, 25, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z110():
    # 'Input_RPS'!Z110
    value = 0
    formula = "=SUM(Z106:Z109)"
    @eval_fn
    def Z110():
        range_1 = Input_RPS(26, 106, 26, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA110():
    # 'Input_RPS'!AA110
    value = 0
    formula = "=SUM(AA106:AA109)"
    @eval_fn
    def AA110():
        range_1 = Input_RPS(27, 106, 27, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB110():
    # 'Input_RPS'!AB110
    value = 0
    formula = "=SUM(AB106:AB109)"
    @eval_fn
    def AB110():
        range_1 = Input_RPS(28, 106, 28, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC110():
    # 'Input_RPS'!AC110
    value = 0
    formula = "=SUM(AC106:AC109)"
    @eval_fn
    def AC110():
        range_1 = Input_RPS(29, 106, 29, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD110():
    # 'Input_RPS'!AD110
    value = 0
    formula = "=SUM(AD106:AD109)"
    @eval_fn
    def AD110():
        range_1 = Input_RPS(30, 106, 30, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE110():
    # 'Input_RPS'!AE110
    value = 0
    formula = "=SUM(AE106:AE109)"
    @eval_fn
    def AE110():
        range_1 = Input_RPS(31, 106, 31, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF110():
    # 'Input_RPS'!AF110
    value = 0
    formula = "=SUM(AF106:AF109)"
    @eval_fn
    def AF110():
        range_1 = Input_RPS(32, 106, 32, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG110():
    # 'Input_RPS'!AG110
    value = 0
    formula = "=SUM(AG106:AG109)"
    @eval_fn
    def AG110():
        range_1 = Input_RPS(33, 106, 33, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH110():
    # 'Input_RPS'!AH110
    value = 0
    formula = "=SUM(AH106:AH109)"
    @eval_fn
    def AH110():
        range_1 = Input_RPS(34, 106, 34, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI110():
    # 'Input_RPS'!AI110
    value = 0
    formula = "=SUM(AI106:AI109)"
    @eval_fn
    def AI110():
        range_1 = Input_RPS(35, 106, 35, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ110():
    # 'Input_RPS'!AJ110
    value = 0
    formula = "=SUM(AJ106:AJ109)"
    @eval_fn
    def AJ110():
        range_1 = Input_RPS(36, 106, 36, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK110():
    # 'Input_RPS'!AK110
    value = 0
    formula = "=SUM(AK106:AK109)"
    @eval_fn
    def AK110():
        range_1 = Input_RPS(37, 106, 37, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL110():
    # 'Input_RPS'!AL110
    value = 0
    formula = "=SUM(AL106:AL109)"
    @eval_fn
    def AL110():
        range_1 = Input_RPS(38, 106, 38, 109)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C111():
    # 'Input_RPS'!C111
    value = "MECO"

@register(Input_RPS)
class D111():
    # 'Input_RPS'!D111
    value = "MWh"

@register(Input_RPS)
class E111():
    # 'Input_RPS'!E111
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Input_RPS)
class C112():
    # 'Input_RPS'!C112
    value = "  Displacement Tech: Photovoltaic Systems"

@register(Input_RPS)
class C113():
    # 'Input_RPS'!C113
    value = "  Displacement Tech: Solar Water Heating Utility"

@register(Input_RPS)
class M113():
    # 'Input_RPS'!M113
    value = 23000

@register(Input_RPS)
class N113():
    # 'Input_RPS'!N113
    value = 26000

@register(Input_RPS)
class O113():
    # 'Input_RPS'!O113
    value = 30000

@register(Input_RPS)
class P113():
    # 'Input_RPS'!P113
    value = 27429

@register(Input_RPS)
class Q113():
    # 'Input_RPS'!Q113
    value = 28492

@register(Input_RPS)
class R113():
    # 'Input_RPS'!R113
    value = 29683

@register(Input_RPS)
class S113():
    # 'Input_RPS'!S113
    value = 30181

@register(Input_RPS)
class T113():
    # 'Input_RPS'!T113
    value = 28341

@register(Input_RPS)
class U113():
    # 'Input_RPS'!U113
    value = 26774

@register(Input_RPS)
class V113():
    # 'Input_RPS'!V113
    value = 24216

@register(Input_RPS)
class W113():
    # 'Input_RPS'!W113
    value = 21658
    formula = "=+V113+V113-U113"
    @eval_fn
    def W113():
        v113_1 = Input_RPS.V113()
        v113_2 = Input_RPS.V113()
        var_1 = add(v113_1, v113_2)
        u113_1 = Input_RPS.U113()
        var_2 = sub(var_1, u113_1)
        return var_2

@register(Input_RPS)
class C114():
    # 'Input_RPS'!C114
    value = "  Displacement Tech: Solar Water Heating PBFA"

@register(Input_RPS)
class M114():
    # 'Input_RPS'!M114
    value = 0

@register(Input_RPS)
class N114():
    # 'Input_RPS'!N114
    value = 0

@register(Input_RPS)
class O114():
    # 'Input_RPS'!O114
    value = 0

@register(Input_RPS)
class P114():
    # 'Input_RPS'!P114
    value = 0

@register(Input_RPS)
class Q114():
    # 'Input_RPS'!Q114
    value = 0

@register(Input_RPS)
class R114():
    # 'Input_RPS'!R114
    value = 0

@register(Input_RPS)
class S114():
    # 'Input_RPS'!S114
    value = 0

@register(Input_RPS)
class T114():
    # 'Input_RPS'!T114
    value = 2505

@register(Input_RPS)
class U114():
    # 'Input_RPS'!U114
    value = 3161

@register(Input_RPS)
class V114():
    # 'Input_RPS'!V114
    value = 4102

@register(Input_RPS)
class W114():
    # 'Input_RPS'!W114
    value = 5043
    formula = "=+V114+V114-U114"
    @eval_fn
    def W114():
        v114_1 = Input_RPS.V114()
        v114_2 = Input_RPS.V114()
        var_1 = add(v114_1, v114_2)
        u114_1 = Input_RPS.U114()
        var_2 = sub(var_1, u114_1)
        return var_2

@register(Input_RPS)
class C115():
    # 'Input_RPS'!C115
    value = "  Energy Efficiency Technologies Total"

@register(Input_RPS)
class M115():
    # 'Input_RPS'!M115
    value = 77000

@register(Input_RPS)
class N115():
    # 'Input_RPS'!N115
    value = 82000

@register(Input_RPS)
class O115():
    # 'Input_RPS'!O115
    value = 88000

@register(Input_RPS)
class P115():
    # 'Input_RPS'!P115
    value = 79835

@register(Input_RPS)
class Q115():
    # 'Input_RPS'!Q115
    value = 88593

@register(Input_RPS)
class R115():
    # 'Input_RPS'!R115
    value = 98813

@register(Input_RPS)
class S115():
    # 'Input_RPS'!S115
    value = 111306

@register(Input_RPS)
class T115():
    # 'Input_RPS'!T115
    value = 129340

@register(Input_RPS)
class U115():
    # 'Input_RPS'!U115
    value = 144281

@register(Input_RPS)
class V115():
    # 'Input_RPS'!V115
    value = 154216

@register(Input_RPS)
class W115():
    # 'Input_RPS'!W115
    value = 164151
    formula = "=+V115+V115-U115"
    @eval_fn
    def W115():
        v115_1 = Input_RPS.V115()
        v115_2 = Input_RPS.V115()
        var_1 = add(v115_1, v115_2)
        u115_1 = Input_RPS.U115()
        var_2 = sub(var_1, u115_1)
        return var_2

@register(Input_RPS)
class C116():
    # 'Input_RPS'!C116
    value = "Total EE"

@register(Input_RPS)
class M116():
    # 'Input_RPS'!M116
    value = 100000
    formula = "=SUM(M112:M115)"
    @eval_fn
    def M116():
        range_1 = Input_RPS(13, 112, 13, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N116():
    # 'Input_RPS'!N116
    value = 108000
    formula = "=SUM(N112:N115)"
    @eval_fn
    def N116():
        range_1 = Input_RPS(14, 112, 14, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O116():
    # 'Input_RPS'!O116
    value = 118000
    formula = "=SUM(O112:O115)"
    @eval_fn
    def O116():
        range_1 = Input_RPS(15, 112, 15, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P116():
    # 'Input_RPS'!P116
    value = 107264
    formula = "=SUM(P112:P115)"
    @eval_fn
    def P116():
        range_1 = Input_RPS(16, 112, 16, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q116():
    # 'Input_RPS'!Q116
    value = 117085
    formula = "=SUM(Q112:Q115)"
    @eval_fn
    def Q116():
        range_1 = Input_RPS(17, 112, 17, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R116():
    # 'Input_RPS'!R116
    value = 128496
    formula = "=SUM(R112:R115)"
    @eval_fn
    def R116():
        range_1 = Input_RPS(18, 112, 18, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S116():
    # 'Input_RPS'!S116
    value = 141487
    formula = "=SUM(S112:S115)"
    @eval_fn
    def S116():
        range_1 = Input_RPS(19, 112, 19, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T116():
    # 'Input_RPS'!T116
    value = 160186
    formula = "=SUM(T112:T115)"
    @eval_fn
    def T116():
        range_1 = Input_RPS(20, 112, 20, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U116():
    # 'Input_RPS'!U116
    value = 174216
    formula = "=SUM(U112:U115)"
    @eval_fn
    def U116():
        range_1 = Input_RPS(21, 112, 21, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V116():
    # 'Input_RPS'!V116
    value = 182534
    formula = "=SUM(V112:V115)"
    @eval_fn
    def V116():
        range_1 = Input_RPS(22, 112, 22, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W116():
    # 'Input_RPS'!W116
    value = 190852
    formula = "=SUM(W112:W115)"
    @eval_fn
    def W116():
        range_1 = Input_RPS(23, 112, 23, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class X116():
    # 'Input_RPS'!X116
    value = 0
    formula = "=SUM(X112:X115)"
    @eval_fn
    def X116():
        range_1 = Input_RPS(24, 112, 24, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y116():
    # 'Input_RPS'!Y116
    value = 0
    formula = "=SUM(Y112:Y115)"
    @eval_fn
    def Y116():
        range_1 = Input_RPS(25, 112, 25, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z116():
    # 'Input_RPS'!Z116
    value = 0
    formula = "=SUM(Z112:Z115)"
    @eval_fn
    def Z116():
        range_1 = Input_RPS(26, 112, 26, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA116():
    # 'Input_RPS'!AA116
    value = 0
    formula = "=SUM(AA112:AA115)"
    @eval_fn
    def AA116():
        range_1 = Input_RPS(27, 112, 27, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB116():
    # 'Input_RPS'!AB116
    value = 0
    formula = "=SUM(AB112:AB115)"
    @eval_fn
    def AB116():
        range_1 = Input_RPS(28, 112, 28, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC116():
    # 'Input_RPS'!AC116
    value = 0
    formula = "=SUM(AC112:AC115)"
    @eval_fn
    def AC116():
        range_1 = Input_RPS(29, 112, 29, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD116():
    # 'Input_RPS'!AD116
    value = 0
    formula = "=SUM(AD112:AD115)"
    @eval_fn
    def AD116():
        range_1 = Input_RPS(30, 112, 30, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE116():
    # 'Input_RPS'!AE116
    value = 0
    formula = "=SUM(AE112:AE115)"
    @eval_fn
    def AE116():
        range_1 = Input_RPS(31, 112, 31, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF116():
    # 'Input_RPS'!AF116
    value = 0
    formula = "=SUM(AF112:AF115)"
    @eval_fn
    def AF116():
        range_1 = Input_RPS(32, 112, 32, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG116():
    # 'Input_RPS'!AG116
    value = 0
    formula = "=SUM(AG112:AG115)"
    @eval_fn
    def AG116():
        range_1 = Input_RPS(33, 112, 33, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH116():
    # 'Input_RPS'!AH116
    value = 0
    formula = "=SUM(AH112:AH115)"
    @eval_fn
    def AH116():
        range_1 = Input_RPS(34, 112, 34, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI116():
    # 'Input_RPS'!AI116
    value = 0
    formula = "=SUM(AI112:AI115)"
    @eval_fn
    def AI116():
        range_1 = Input_RPS(35, 112, 35, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ116():
    # 'Input_RPS'!AJ116
    value = 0
    formula = "=SUM(AJ112:AJ115)"
    @eval_fn
    def AJ116():
        range_1 = Input_RPS(36, 112, 36, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK116():
    # 'Input_RPS'!AK116
    value = 0
    formula = "=SUM(AK112:AK115)"
    @eval_fn
    def AK116():
        range_1 = Input_RPS(37, 112, 37, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL116():
    # 'Input_RPS'!AL116
    value = 0
    formula = "=SUM(AL112:AL115)"
    @eval_fn
    def AL116():
        range_1 = Input_RPS(38, 112, 38, 115)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C117():
    # 'Input_RPS'!C117
    value = "KIUC"

@register(Input_RPS)
class D117():
    # 'Input_RPS'!D117
    value = "MWh"

@register(Input_RPS)
class E117():
    # 'Input_RPS'!E117
    value = "http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf"

@register(Input_RPS)
class C118():
    # 'Input_RPS'!C118
    value = "  Customer Renewable Generation"

@register(Input_RPS)
class D118():
    # 'Input_RPS'!D118
    value = "MWh"

@register(Input_RPS)
class C119():
    # 'Input_RPS'!C119
    value = "  Solar Water Heating"

@register(Input_RPS)
class D119():
    # 'Input_RPS'!D119
    value = "MWh"

@register(Input_RPS)
class K119():
    # 'Input_RPS'!K119
    value = 7387

@register(Input_RPS)
class L119():
    # 'Input_RPS'!L119
    value = 7558

@register(Input_RPS)
class M119():
    # 'Input_RPS'!M119
    value = 7659

@register(Input_RPS)
class N119():
    # 'Input_RPS'!N119
    value = 7831

@register(Input_RPS)
class O119():
    # 'Input_RPS'!O119
    value = 7937

@register(Input_RPS)
class C120():
    # 'Input_RPS'!C120
    value = "  Net Energy Metering"

@register(Input_RPS)
class D120():
    # 'Input_RPS'!D120
    value = "MWh"

@register(Input_RPS)
class C121():
    # 'Input_RPS'!C121
    value = "  Demand Side Management"

@register(Input_RPS)
class D121():
    # 'Input_RPS'!D121
    value = "MWh"

@register(Input_RPS)
class K121():
    # 'Input_RPS'!K121
    value = 0

@register(Input_RPS)
class L121():
    # 'Input_RPS'!L121
    value = 19037

@register(Input_RPS)
class M121():
    # 'Input_RPS'!M121
    value = 20855

@register(Input_RPS)
class N121():
    # 'Input_RPS'!N121
    value = 21349

@register(Input_RPS)
class O121():
    # 'Input_RPS'!O121
    value = 21361

@register(Input_RPS)
class P121():
    # 'Input_RPS'!P121
    value = 19233

@register(Input_RPS)
class Q121():
    # 'Input_RPS'!Q121
    value = 19217

@register(Input_RPS)
class R121():
    # 'Input_RPS'!R121
    value = 16911

@register(Input_RPS)
class S121():
    # 'Input_RPS'!S121
    value = 18264

@register(Input_RPS)
class T121():
    # 'Input_RPS'!T121
    value = 24368

@register(Input_RPS)
class U121():
    # 'Input_RPS'!U121
    value = 22441

@register(Input_RPS)
class V121():
    # 'Input_RPS'!V121
    value = 21370

@register(Input_RPS)
class W121():
    # 'Input_RPS'!W121
    value = 19947

@register(Input_RPS)
class C122():
    # 'Input_RPS'!C122
    value = "Total EE"

@register(Input_RPS)
class G122():
    # 'Input_RPS'!G122
    value = 0
    formula = "=SUM(G118:G121)"
    @eval_fn
    def G122():
        range_1 = Input_RPS(7, 118, 7, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H122():
    # 'Input_RPS'!H122
    value = 0
    formula = "=SUM(H118:H121)"
    @eval_fn
    def H122():
        range_1 = Input_RPS(8, 118, 8, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I122():
    # 'Input_RPS'!I122
    value = 0
    formula = "=SUM(I118:I121)"
    @eval_fn
    def I122():
        range_1 = Input_RPS(9, 118, 9, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J122():
    # 'Input_RPS'!J122
    value = 0
    formula = "=SUM(J118:J121)"
    @eval_fn
    def J122():
        range_1 = Input_RPS(10, 118, 10, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K122():
    # 'Input_RPS'!K122
    value = 7387
    formula = "=SUM(K118:K121)"
    @eval_fn
    def K122():
        range_1 = Input_RPS(11, 118, 11, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L122():
    # 'Input_RPS'!L122
    value = 26595
    formula = "=SUM(L118:L121)"
    @eval_fn
    def L122():
        range_1 = Input_RPS(12, 118, 12, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M122():
    # 'Input_RPS'!M122
    value = 28514
    formula = "=SUM(M118:M121)"
    @eval_fn
    def M122():
        range_1 = Input_RPS(13, 118, 13, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N122():
    # 'Input_RPS'!N122
    value = 29180
    formula = "=SUM(N118:N121)"
    @eval_fn
    def N122():
        range_1 = Input_RPS(14, 118, 14, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O122():
    # 'Input_RPS'!O122
    value = 29298
    formula = "=SUM(O118:O121)"
    @eval_fn
    def O122():
        range_1 = Input_RPS(15, 118, 15, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P122():
    # 'Input_RPS'!P122
    value = 19233
    formula = "=SUM(P118:P121)"
    @eval_fn
    def P122():
        range_1 = Input_RPS(16, 118, 16, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q122():
    # 'Input_RPS'!Q122
    value = 19217
    formula = "=SUM(Q118:Q121)"
    @eval_fn
    def Q122():
        range_1 = Input_RPS(17, 118, 17, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R122():
    # 'Input_RPS'!R122
    value = 16911
    formula = "=SUM(R118:R121)"
    @eval_fn
    def R122():
        range_1 = Input_RPS(18, 118, 18, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S122():
    # 'Input_RPS'!S122
    value = 18264
    formula = "=SUM(S118:S121)"
    @eval_fn
    def S122():
        range_1 = Input_RPS(19, 118, 19, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T122():
    # 'Input_RPS'!T122
    value = 24368
    formula = "=SUM(T118:T121)"
    @eval_fn
    def T122():
        range_1 = Input_RPS(20, 118, 20, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U122():
    # 'Input_RPS'!U122
    value = 22441
    formula = "=SUM(U118:U121)"
    @eval_fn
    def U122():
        range_1 = Input_RPS(21, 118, 21, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V122():
    # 'Input_RPS'!V122
    value = 21370
    formula = "=SUM(V118:V121)"
    @eval_fn
    def V122():
        range_1 = Input_RPS(22, 118, 22, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W122():
    # 'Input_RPS'!W122
    value = 19947
    formula = "=SUM(W118:W121)"
    @eval_fn
    def W122():
        range_1 = Input_RPS(23, 118, 23, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class X122():
    # 'Input_RPS'!X122
    value = 0
    formula = "=SUM(X118:X121)"
    @eval_fn
    def X122():
        range_1 = Input_RPS(24, 118, 24, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y122():
    # 'Input_RPS'!Y122
    value = 0
    formula = "=SUM(Y118:Y121)"
    @eval_fn
    def Y122():
        range_1 = Input_RPS(25, 118, 25, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z122():
    # 'Input_RPS'!Z122
    value = 0
    formula = "=SUM(Z118:Z121)"
    @eval_fn
    def Z122():
        range_1 = Input_RPS(26, 118, 26, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA122():
    # 'Input_RPS'!AA122
    value = 0
    formula = "=SUM(AA118:AA121)"
    @eval_fn
    def AA122():
        range_1 = Input_RPS(27, 118, 27, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB122():
    # 'Input_RPS'!AB122
    value = 0
    formula = "=SUM(AB118:AB121)"
    @eval_fn
    def AB122():
        range_1 = Input_RPS(28, 118, 28, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC122():
    # 'Input_RPS'!AC122
    value = 0
    formula = "=SUM(AC118:AC121)"
    @eval_fn
    def AC122():
        range_1 = Input_RPS(29, 118, 29, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD122():
    # 'Input_RPS'!AD122
    value = 0
    formula = "=SUM(AD118:AD121)"
    @eval_fn
    def AD122():
        range_1 = Input_RPS(30, 118, 30, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE122():
    # 'Input_RPS'!AE122
    value = 0
    formula = "=SUM(AE118:AE121)"
    @eval_fn
    def AE122():
        range_1 = Input_RPS(31, 118, 31, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF122():
    # 'Input_RPS'!AF122
    value = 0
    formula = "=SUM(AF118:AF121)"
    @eval_fn
    def AF122():
        range_1 = Input_RPS(32, 118, 32, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG122():
    # 'Input_RPS'!AG122
    value = 0
    formula = "=SUM(AG118:AG121)"
    @eval_fn
    def AG122():
        range_1 = Input_RPS(33, 118, 33, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH122():
    # 'Input_RPS'!AH122
    value = 0
    formula = "=SUM(AH118:AH121)"
    @eval_fn
    def AH122():
        range_1 = Input_RPS(34, 118, 34, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI122():
    # 'Input_RPS'!AI122
    value = 0
    formula = "=SUM(AI118:AI121)"
    @eval_fn
    def AI122():
        range_1 = Input_RPS(35, 118, 35, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ122():
    # 'Input_RPS'!AJ122
    value = 0
    formula = "=SUM(AJ118:AJ121)"
    @eval_fn
    def AJ122():
        range_1 = Input_RPS(36, 118, 36, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK122():
    # 'Input_RPS'!AK122
    value = 0
    formula = "=SUM(AK118:AK121)"
    @eval_fn
    def AK122():
        range_1 = Input_RPS(37, 118, 37, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL122():
    # 'Input_RPS'!AL122
    value = 0
    formula = "=SUM(AL118:AL121)"
    @eval_fn
    def AL122():
        range_1 = Input_RPS(38, 118, 38, 121)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class C123():
    # 'Input_RPS'!C123
    value = "Total"

@register(Input_RPS)
class D123():
    # 'Input_RPS'!D123
    value = "MWh"

@register(Input_RPS)
class G123():
    # 'Input_RPS'!G123
    value = 0
    formula = "=SUM(G122,G116,G110,G104)"
    @eval_fn
    def G123():
        g122_1 = Input_RPS.G122()
        g116_1 = Input_RPS.G116()
        g110_1 = Input_RPS.G110()
        g104_1 = Input_RPS.G104()
        var_1 = SUM(g122_1, g116_1, g110_1, g104_1)
        return var_1

@register(Input_RPS)
class H123():
    # 'Input_RPS'!H123
    value = 0
    formula = "=SUM(H122,H116,H110,H104)"
    @eval_fn
    def H123():
        h122_1 = Input_RPS.H122()
        h116_1 = Input_RPS.H116()
        h110_1 = Input_RPS.H110()
        h104_1 = Input_RPS.H104()
        var_1 = SUM(h122_1, h116_1, h110_1, h104_1)
        return var_1

@register(Input_RPS)
class I123():
    # 'Input_RPS'!I123
    value = 0
    formula = "=SUM(I122,I116,I110,I104)"
    @eval_fn
    def I123():
        i122_1 = Input_RPS.I122()
        i116_1 = Input_RPS.I116()
        i110_1 = Input_RPS.I110()
        i104_1 = Input_RPS.I104()
        var_1 = SUM(i122_1, i116_1, i110_1, i104_1)
        return var_1

@register(Input_RPS)
class J123():
    # 'Input_RPS'!J123
    value = 0
    formula = "=SUM(J122,J116,J110,J104)"
    @eval_fn
    def J123():
        j122_1 = Input_RPS.J122()
        j116_1 = Input_RPS.J116()
        j110_1 = Input_RPS.J110()
        j104_1 = Input_RPS.J104()
        var_1 = SUM(j122_1, j116_1, j110_1, j104_1)
        return var_1

@register(Input_RPS)
class K123():
    # 'Input_RPS'!K123
    value = 7387
    formula = "=SUM(K122,K116,K110,K104)"
    @eval_fn
    def K123():
        k122_1 = Input_RPS.K122()
        k116_1 = Input_RPS.K116()
        k110_1 = Input_RPS.K110()
        k104_1 = Input_RPS.K104()
        var_1 = SUM(k122_1, k116_1, k110_1, k104_1)
        return var_1

@register(Input_RPS)
class L123():
    # 'Input_RPS'!L123
    value = 26595
    formula = "=SUM(L122,L116,L110,L104)"
    @eval_fn
    def L123():
        l122_1 = Input_RPS.L122()
        l116_1 = Input_RPS.L116()
        l110_1 = Input_RPS.L110()
        l104_1 = Input_RPS.L104()
        var_1 = SUM(l122_1, l116_1, l110_1, l104_1)
        return var_1

@register(Input_RPS)
class M123():
    # 'Input_RPS'!M123
    value = 530514
    formula = "=SUM(M122,M116,M110,M104)"
    @eval_fn
    def M123():
        m122_1 = Input_RPS.M122()
        m116_1 = Input_RPS.M116()
        m110_1 = Input_RPS.M110()
        m104_1 = Input_RPS.M104()
        var_1 = SUM(m122_1, m116_1, m110_1, m104_1)
        return var_1

@register(Input_RPS)
class N123():
    # 'Input_RPS'!N123
    value = 600180
    formula = "=SUM(N122,N116,N110,N104)"
    @eval_fn
    def N123():
        n122_1 = Input_RPS.N122()
        n116_1 = Input_RPS.N116()
        n110_1 = Input_RPS.N110()
        n104_1 = Input_RPS.N104()
        var_1 = SUM(n122_1, n116_1, n110_1, n104_1)
        return var_1

@register(Input_RPS)
class O123():
    # 'Input_RPS'!O123
    value = 736298
    formula = "=SUM(O122,O116,O110,O104)"
    @eval_fn
    def O123():
        o122_1 = Input_RPS.O122()
        o116_1 = Input_RPS.O116()
        o110_1 = Input_RPS.O110()
        o104_1 = Input_RPS.O104()
        var_1 = SUM(o122_1, o116_1, o110_1, o104_1)
        return var_1

@register(Input_RPS)
class P123():
    # 'Input_RPS'!P123
    value = 867405
    formula = "=SUM(P122,P116,P110,P104)"
    @eval_fn
    def P123():
        p122_1 = Input_RPS.P122()
        p116_1 = Input_RPS.P116()
        p110_1 = Input_RPS.P110()
        p104_1 = Input_RPS.P104()
        var_1 = SUM(p122_1, p116_1, p110_1, p104_1)
        return var_1

@register(Input_RPS)
class Q123():
    # 'Input_RPS'!Q123
    value = 938808
    formula = "=SUM(Q122,Q116,Q110,Q104)"
    @eval_fn
    def Q123():
        q122_1 = Input_RPS.Q122()
        q116_1 = Input_RPS.Q116()
        q110_1 = Input_RPS.Q110()
        q104_1 = Input_RPS.Q104()
        var_1 = SUM(q122_1, q116_1, q110_1, q104_1)
        return var_1

@register(Input_RPS)
class R123():
    # 'Input_RPS'!R123
    value = 1088476
    formula = "=SUM(R122,R116,R110,R104)"
    @eval_fn
    def R123():
        r122_1 = Input_RPS.R122()
        r116_1 = Input_RPS.R116()
        r110_1 = Input_RPS.R110()
        r104_1 = Input_RPS.R104()
        var_1 = SUM(r122_1, r116_1, r110_1, r104_1)
        return var_1

@register(Input_RPS)
class S123():
    # 'Input_RPS'!S123
    value = 1207501
    formula = "=SUM(S122,S116,S110,S104)"
    @eval_fn
    def S123():
        s122_1 = Input_RPS.S122()
        s116_1 = Input_RPS.S116()
        s110_1 = Input_RPS.S110()
        s104_1 = Input_RPS.S104()
        var_1 = SUM(s122_1, s116_1, s110_1, s104_1)
        return var_1

@register(Input_RPS)
class T123():
    # 'Input_RPS'!T123
    value = 1394339
    formula = "=SUM(T122,T116,T110,T104)"
    @eval_fn
    def T123():
        t122_1 = Input_RPS.T122()
        t116_1 = Input_RPS.T116()
        t110_1 = Input_RPS.T110()
        t104_1 = Input_RPS.T104()
        var_1 = SUM(t122_1, t116_1, t110_1, t104_1)
        return var_1

@register(Input_RPS)
class U123():
    # 'Input_RPS'!U123
    value = 1494188
    formula = "=SUM(U122,U116,U110,U104)"
    @eval_fn
    def U123():
        u122_1 = Input_RPS.U122()
        u116_1 = Input_RPS.U116()
        u110_1 = Input_RPS.U110()
        u104_1 = Input_RPS.U104()
        var_1 = SUM(u122_1, u116_1, u110_1, u104_1)
        return var_1

@register(Input_RPS)
class V123():
    # 'Input_RPS'!V123
    value = 1576123
    formula = "=SUM(V122,V116,V110,V104)"
    @eval_fn
    def V123():
        v122_1 = Input_RPS.V122()
        v116_1 = Input_RPS.V116()
        v110_1 = Input_RPS.V110()
        v104_1 = Input_RPS.V104()
        var_1 = SUM(v122_1, v116_1, v110_1, v104_1)
        return var_1

@register(Input_RPS)
class W123():
    # 'Input_RPS'!W123
    value = 1657706
    formula = "=SUM(W122,W116,W110,W104)"
    @eval_fn
    def W123():
        w122_1 = Input_RPS.W122()
        w116_1 = Input_RPS.W116()
        w110_1 = Input_RPS.W110()
        w104_1 = Input_RPS.W104()
        var_1 = SUM(w122_1, w116_1, w110_1, w104_1)
        return var_1

@register(Input_RPS)
class X123():
    # 'Input_RPS'!X123
    value = 0
    formula = "=SUM(X122,X116,X110,X104)"
    @eval_fn
    def X123():
        x122_1 = Input_RPS.X122()
        x116_1 = Input_RPS.X116()
        x110_1 = Input_RPS.X110()
        x104_1 = Input_RPS.X104()
        var_1 = SUM(x122_1, x116_1, x110_1, x104_1)
        return var_1

@register(Input_RPS)
class Y123():
    # 'Input_RPS'!Y123
    value = 0
    formula = "=SUM(Y122,Y116,Y110,Y104)"
    @eval_fn
    def Y123():
        y122_1 = Input_RPS.Y122()
        y116_1 = Input_RPS.Y116()
        y110_1 = Input_RPS.Y110()
        y104_1 = Input_RPS.Y104()
        var_1 = SUM(y122_1, y116_1, y110_1, y104_1)
        return var_1

@register(Input_RPS)
class Z123():
    # 'Input_RPS'!Z123
    value = 0
    formula = "=SUM(Z122,Z116,Z110,Z104)"
    @eval_fn
    def Z123():
        z122_1 = Input_RPS.Z122()
        z116_1 = Input_RPS.Z116()
        z110_1 = Input_RPS.Z110()
        z104_1 = Input_RPS.Z104()
        var_1 = SUM(z122_1, z116_1, z110_1, z104_1)
        return var_1

@register(Input_RPS)
class AA123():
    # 'Input_RPS'!AA123
    value = 0
    formula = "=SUM(AA122,AA116,AA110,AA104)"
    @eval_fn
    def AA123():
        aa122_1 = Input_RPS.AA122()
        aa116_1 = Input_RPS.AA116()
        aa110_1 = Input_RPS.AA110()
        aa104_1 = Input_RPS.AA104()
        var_1 = SUM(aa122_1, aa116_1, aa110_1, aa104_1)
        return var_1

@register(Input_RPS)
class AB123():
    # 'Input_RPS'!AB123
    value = 0
    formula = "=SUM(AB122,AB116,AB110,AB104)"
    @eval_fn
    def AB123():
        ab122_1 = Input_RPS.AB122()
        ab116_1 = Input_RPS.AB116()
        ab110_1 = Input_RPS.AB110()
        ab104_1 = Input_RPS.AB104()
        var_1 = SUM(ab122_1, ab116_1, ab110_1, ab104_1)
        return var_1

@register(Input_RPS)
class AC123():
    # 'Input_RPS'!AC123
    value = 0
    formula = "=SUM(AC122,AC116,AC110,AC104)"
    @eval_fn
    def AC123():
        ac122_1 = Input_RPS.AC122()
        ac116_1 = Input_RPS.AC116()
        ac110_1 = Input_RPS.AC110()
        ac104_1 = Input_RPS.AC104()
        var_1 = SUM(ac122_1, ac116_1, ac110_1, ac104_1)
        return var_1

@register(Input_RPS)
class AD123():
    # 'Input_RPS'!AD123
    value = 0
    formula = "=SUM(AD122,AD116,AD110,AD104)"
    @eval_fn
    def AD123():
        ad122_1 = Input_RPS.AD122()
        ad116_1 = Input_RPS.AD116()
        ad110_1 = Input_RPS.AD110()
        ad104_1 = Input_RPS.AD104()
        var_1 = SUM(ad122_1, ad116_1, ad110_1, ad104_1)
        return var_1

@register(Input_RPS)
class AE123():
    # 'Input_RPS'!AE123
    value = 0
    formula = "=SUM(AE122,AE116,AE110,AE104)"
    @eval_fn
    def AE123():
        ae122_1 = Input_RPS.AE122()
        ae116_1 = Input_RPS.AE116()
        ae110_1 = Input_RPS.AE110()
        ae104_1 = Input_RPS.AE104()
        var_1 = SUM(ae122_1, ae116_1, ae110_1, ae104_1)
        return var_1

@register(Input_RPS)
class AF123():
    # 'Input_RPS'!AF123
    value = 0
    formula = "=SUM(AF122,AF116,AF110,AF104)"
    @eval_fn
    def AF123():
        af122_1 = Input_RPS.AF122()
        af116_1 = Input_RPS.AF116()
        af110_1 = Input_RPS.AF110()
        af104_1 = Input_RPS.AF104()
        var_1 = SUM(af122_1, af116_1, af110_1, af104_1)
        return var_1

@register(Input_RPS)
class AG123():
    # 'Input_RPS'!AG123
    value = 0
    formula = "=SUM(AG122,AG116,AG110,AG104)"
    @eval_fn
    def AG123():
        ag122_1 = Input_RPS.AG122()
        ag116_1 = Input_RPS.AG116()
        ag110_1 = Input_RPS.AG110()
        ag104_1 = Input_RPS.AG104()
        var_1 = SUM(ag122_1, ag116_1, ag110_1, ag104_1)
        return var_1

@register(Input_RPS)
class AH123():
    # 'Input_RPS'!AH123
    value = 0
    formula = "=SUM(AH122,AH116,AH110,AH104)"
    @eval_fn
    def AH123():
        ah122_1 = Input_RPS.AH122()
        ah116_1 = Input_RPS.AH116()
        ah110_1 = Input_RPS.AH110()
        ah104_1 = Input_RPS.AH104()
        var_1 = SUM(ah122_1, ah116_1, ah110_1, ah104_1)
        return var_1

@register(Input_RPS)
class AI123():
    # 'Input_RPS'!AI123
    value = 0
    formula = "=SUM(AI122,AI116,AI110,AI104)"
    @eval_fn
    def AI123():
        ai122_1 = Input_RPS.AI122()
        ai116_1 = Input_RPS.AI116()
        ai110_1 = Input_RPS.AI110()
        ai104_1 = Input_RPS.AI104()
        var_1 = SUM(ai122_1, ai116_1, ai110_1, ai104_1)
        return var_1

@register(Input_RPS)
class AJ123():
    # 'Input_RPS'!AJ123
    value = 0
    formula = "=SUM(AJ122,AJ116,AJ110,AJ104)"
    @eval_fn
    def AJ123():
        aj122_1 = Input_RPS.AJ122()
        aj116_1 = Input_RPS.AJ116()
        aj110_1 = Input_RPS.AJ110()
        aj104_1 = Input_RPS.AJ104()
        var_1 = SUM(aj122_1, aj116_1, aj110_1, aj104_1)
        return var_1

@register(Input_RPS)
class AK123():
    # 'Input_RPS'!AK123
    value = 0
    formula = "=SUM(AK122,AK116,AK110,AK104)"
    @eval_fn
    def AK123():
        ak122_1 = Input_RPS.AK122()
        ak116_1 = Input_RPS.AK116()
        ak110_1 = Input_RPS.AK110()
        ak104_1 = Input_RPS.AK104()
        var_1 = SUM(ak122_1, ak116_1, ak110_1, ak104_1)
        return var_1

@register(Input_RPS)
class AL123():
    # 'Input_RPS'!AL123
    value = 0
    formula = "=SUM(AL122,AL116,AL110,AL104)"
    @eval_fn
    def AL123():
        al122_1 = Input_RPS.AL122()
        al116_1 = Input_RPS.AL116()
        al110_1 = Input_RPS.AL110()
        al104_1 = Input_RPS.AL104()
        var_1 = SUM(al122_1, al116_1, al110_1, al104_1)
        return var_1

@register(Input_RPS)
class A124():
    # 'Input_RPS'!A124
    value = '''TEusy - Total Energy source "s" sold by utilitiy "u" in year "y"'''

@register(Input_RPS)
class A125():
    # 'Input_RPS'!A125
    value = "HECOTotal Renewable"
    formula = "=CONCATENATE(C125,B125)"
    @eval_fn
    def A125():
        c125_1 = Input_RPS.C125()
        b125_1 = Input_RPS.B125()
        var_1 = CONCATENATE(c125_1, b125_1)
        return var_1

@register(Input_RPS)
class B125():
    # 'Input_RPS'!B125
    value = "Total Renewable"

@register(Input_RPS)
class C125():
    # 'Input_RPS'!C125
    value = "HECO"

@register(Input_RPS)
class D125():
    # 'Input_RPS'!D125
    value = "MWh"

@register(Input_RPS)
class E125():
    # 'Input_RPS'!E125
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Input_RPS)
class G125():
    # 'Input_RPS'!G125
    value = 8998000

@register(Input_RPS)
class H125():
    # 'Input_RPS'!H125
    value = 7212000

@register(Input_RPS)
class I125():
    # 'Input_RPS'!I125
    value = 7277000

@register(Input_RPS)
class J125():
    # 'Input_RPS'!J125
    value = 7390000

@register(Input_RPS)
class K125():
    # 'Input_RPS'!K125
    value = 7522000

@register(Input_RPS)
class L125():
    # 'Input_RPS'!L125
    value = 7733000

@register(Input_RPS)
class M125():
    # 'Input_RPS'!M125
    value = 7721000

@register(Input_RPS)
class N125():
    # 'Input_RPS'!N125
    value = 7701000

@register(Input_RPS)
class O125():
    # 'Input_RPS'!O125
    value = 7675000

@register(Input_RPS)
class P125():
    # 'Input_RPS'!P125
    value = 7555962

@register(Input_RPS)
class Q125():
    # 'Input_RPS'!Q125
    value = 7377537

@register(Input_RPS)
class R125():
    # 'Input_RPS'!R125
    value = 7277229

@register(Input_RPS)
class S125():
    # 'Input_RPS'!S125
    value = 7242311

@register(Input_RPS)
class T125():
    # 'Input_RPS'!T125
    value = 6975996

@register(Input_RPS)
class U125():
    # 'Input_RPS'!U125
    value = 6858536

@register(Input_RPS)
class V125():
    # 'Input_RPS'!V125
    value = 6781665

@register(Input_RPS)
class W125():
    # 'Input_RPS'!W125
    value = 6754083

@register(Input_RPS)
class A126():
    # 'Input_RPS'!A126
    value = "HELCOTotal Renewable"
    formula = "=CONCATENATE(C126,B126)"
    @eval_fn
    def A126():
        c126_1 = Input_RPS.C126()
        b126_1 = Input_RPS.B126()
        var_1 = CONCATENATE(c126_1, b126_1)
        return var_1

@register(Input_RPS)
class B126():
    # 'Input_RPS'!B126
    value = "Total Renewable"

@register(Input_RPS)
class C126():
    # 'Input_RPS'!C126
    value = "HELCO"

@register(Input_RPS)
class D126():
    # 'Input_RPS'!D126
    value = "MWh"

@register(Input_RPS)
class E126():
    # 'Input_RPS'!E126
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Input_RPS)
class G126():
    # 'Input_RPS'!G126
    value = 922000

@register(Input_RPS)
class H126():
    # 'Input_RPS'!H126
    value = 954000

@register(Input_RPS)
class I126():
    # 'Input_RPS'!I126
    value = 959000

@register(Input_RPS)
class J126():
    # 'Input_RPS'!J126
    value = 995000

@register(Input_RPS)
class K126():
    # 'Input_RPS'!K126
    value = 1046000

@register(Input_RPS)
class L126():
    # 'Input_RPS'!L126
    value = 1083000

@register(Input_RPS)
class M126():
    # 'Input_RPS'!M126
    value = 1117000

@register(Input_RPS)
class N126():
    # 'Input_RPS'!N126
    value = 1149000

@register(Input_RPS)
class O126():
    # 'Input_RPS'!O126
    value = 1163000

@register(Input_RPS)
class P126():
    # 'Input_RPS'!P126
    value = 1141030

@register(Input_RPS)
class Q126():
    # 'Input_RPS'!Q126
    value = 1119881

@register(Input_RPS)
class R126():
    # 'Input_RPS'!R126
    value = 1109783

@register(Input_RPS)
class S126():
    # 'Input_RPS'!S126
    value = 1103572

@register(Input_RPS)
class T126():
    # 'Input_RPS'!T126
    value = 1085171

@register(Input_RPS)
class U126():
    # 'Input_RPS'!U126
    value = 1076104

@register(Input_RPS)
class V126():
    # 'Input_RPS'!V126
    value = 1062521

@register(Input_RPS)
class W126():
    # 'Input_RPS'!W126
    value = 1064785

@register(Input_RPS)
class A127():
    # 'Input_RPS'!A127
    value = "MECOTotal Renewable"
    formula = "=CONCATENATE(C127,B127)"
    @eval_fn
    def A127():
        c127_1 = Input_RPS.C127()
        b127_1 = Input_RPS.B127()
        var_1 = CONCATENATE(c127_1, b127_1)
        return var_1

@register(Input_RPS)
class B127():
    # 'Input_RPS'!B127
    value = "Total Renewable"

@register(Input_RPS)
class C127():
    # 'Input_RPS'!C127
    value = "MECO"

@register(Input_RPS)
class D127():
    # 'Input_RPS'!D127
    value = "MWh"

@register(Input_RPS)
class E127():
    # 'Input_RPS'!E127
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2006_RPS_Report_to_PUC_Filed_wo_Cover_Ltr.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2007_RPs_Report-to-PUC_draft_080530_FINAL.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/HECO_RPS_2008_Status_Report.pdf
www.heco.com/vcmcontent/StaticFiles/pdf/2009_rps.pdf
http://www.heco.com/vcmcontent/StaticFiles/pdf/2010_rps.pdf
 http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  '''

@register(Input_RPS)
class G127():
    # 'Input_RPS'!G127
    value = 1065000

@register(Input_RPS)
class H127():
    # 'Input_RPS'!H127
    value = 1106000

@register(Input_RPS)
class I127():
    # 'Input_RPS'!I127
    value = 1134000

@register(Input_RPS)
class J127():
    # 'Input_RPS'!J127
    value = 1159000

@register(Input_RPS)
class K127():
    # 'Input_RPS'!K127
    value = 1207000

@register(Input_RPS)
class L127():
    # 'Input_RPS'!L127
    value = 1247000

@register(Input_RPS)
class M127():
    # 'Input_RPS'!M127
    value = 1252000

@register(Input_RPS)
class N127():
    # 'Input_RPS'!N127
    value = 1266000

@register(Input_RPS)
class O127():
    # 'Input_RPS'!O127
    value = 1280000

@register(Input_RPS)
class P127():
    # 'Input_RPS'!P127
    value = 1239228

@register(Input_RPS)
class Q127():
    # 'Input_RPS'!Q127
    value = 1192243

@register(Input_RPS)
class R127():
    # 'Input_RPS'!R127
    value = 1191559

@register(Input_RPS)
class S127():
    # 'Input_RPS'!S127
    value = 1181026

@register(Input_RPS)
class T127():
    # 'Input_RPS'!T127
    value = 1144832

@register(Input_RPS)
class U127():
    # 'Input_RPS'!U127
    value = 1134873

@register(Input_RPS)
class V127():
    # 'Input_RPS'!V127
    value = 1132056

@register(Input_RPS)
class W127():
    # 'Input_RPS'!W127
    value = 1137630

@register(Input_RPS)
class A128():
    # 'Input_RPS'!A128
    value = "KIUCTotal Renewable"
    formula = "=CONCATENATE(C128,B128)"
    @eval_fn
    def A128():
        c128_1 = Input_RPS.C128()
        b128_1 = Input_RPS.B128()
        var_1 = CONCATENATE(c128_1, b128_1)
        return var_1

@register(Input_RPS)
class B128():
    # 'Input_RPS'!B128
    value = "Total Renewable"

@register(Input_RPS)
class C128():
    # 'Input_RPS'!C128
    value = "KIUC"

@register(Input_RPS)
class D128():
    # 'Input_RPS'!D128
    value = "MWh"

@register(Input_RPS)
class E128():
    # 'Input_RPS'!E128
    value = '''http://puc.hawaii.gov/reports/Report%20to%20Leg.kks.2008-11-12%20puc.pdf
http://dms.puc.hawaii.gov/dms/OpenDocServlet?RT=&document_id=91+3+ICM4+LSDB15+PC_DocketReport59+26+A1001001A12D04B24000E5143818+A12D04B24000E514381+14+1960'''

@register(Input_RPS)
class G128():
    # 'Input_RPS'!G128
    value = 423389

@register(Input_RPS)
class H128():
    # 'Input_RPS'!H128
    value = 452699

@register(Input_RPS)
class I128():
    # 'Input_RPS'!I128
    value = 443798

@register(Input_RPS)
class J128():
    # 'Input_RPS'!J128
    value = 452631

@register(Input_RPS)
class K128():
    # 'Input_RPS'!K128
    value = 438768

@register(Input_RPS)
class L128():
    # 'Input_RPS'!L128
    value = 473608

@register(Input_RPS)
class M128():
    # 'Input_RPS'!M128
    value = 477255

@register(Input_RPS)
class N128():
    # 'Input_RPS'!N128
    value = 481461

@register(Input_RPS)
class O128():
    # 'Input_RPS'!O128
    value = 496718

@register(Input_RPS)
class P128():
    # 'Input_RPS'!P128
    value = 476948

@register(Input_RPS)
class Q128():
    # 'Input_RPS'!Q128
    value = 460513

@register(Input_RPS)
class R128():
    # 'Input_RPS'!R128
    value = 457274

@register(Input_RPS)
class S128():
    # 'Input_RPS'!S128
    value = 460971

@register(Input_RPS)
class T128():
    # 'Input_RPS'!T128
    value = 433159

@register(Input_RPS)
class U128():
    # 'Input_RPS'!U128
    value = 431478

@register(Input_RPS)
class V128():
    # 'Input_RPS'!V128
    value = 429924

@register(Input_RPS)
class W128():
    # 'Input_RPS'!W128
    value = 432078

@register(Input_RPS)
class A129():
    # 'Input_RPS'!A129
    value = "TotalTotal Renewable"
    formula = "=CONCATENATE(C129,B129)"
    @eval_fn
    def A129():
        c129_1 = Input_RPS.C129()
        b129_1 = Input_RPS.B129()
        var_1 = CONCATENATE(c129_1, b129_1)
        return var_1

@register(Input_RPS)
class B129():
    # 'Input_RPS'!B129
    value = "Total Renewable"

@register(Input_RPS)
class C129():
    # 'Input_RPS'!C129
    value = "Total"

@register(Input_RPS)
class D129():
    # 'Input_RPS'!D129
    value = "MWh"

@register(Input_RPS)
class G129():
    # 'Input_RPS'!G129
    value = 11408389
    formula = "=SUM(G125:G128)"
    @eval_fn
    def G129():
        range_1 = Input_RPS(7, 125, 7, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class H129():
    # 'Input_RPS'!H129
    value = 9724699
    formula = "=SUM(H125:H128)"
    @eval_fn
    def H129():
        range_1 = Input_RPS(8, 125, 8, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class I129():
    # 'Input_RPS'!I129
    value = 9813798
    formula = "=SUM(I125:I128)"
    @eval_fn
    def I129():
        range_1 = Input_RPS(9, 125, 9, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class J129():
    # 'Input_RPS'!J129
    value = 9996631
    formula = "=SUM(J125:J128)"
    @eval_fn
    def J129():
        range_1 = Input_RPS(10, 125, 10, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class K129():
    # 'Input_RPS'!K129
    value = 10213768
    formula = "=SUM(K125:K128)"
    @eval_fn
    def K129():
        range_1 = Input_RPS(11, 125, 11, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class L129():
    # 'Input_RPS'!L129
    value = 10536608
    formula = "=SUM(L125:L128)"
    @eval_fn
    def L129():
        range_1 = Input_RPS(12, 125, 12, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class M129():
    # 'Input_RPS'!M129
    value = 10567255
    formula = "=SUM(M125:M128)"
    @eval_fn
    def M129():
        range_1 = Input_RPS(13, 125, 13, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class N129():
    # 'Input_RPS'!N129
    value = 10597461
    formula = "=SUM(N125:N128)"
    @eval_fn
    def N129():
        range_1 = Input_RPS(14, 125, 14, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class O129():
    # 'Input_RPS'!O129
    value = 10614718
    formula = "=SUM(O125:O128)"
    @eval_fn
    def O129():
        range_1 = Input_RPS(15, 125, 15, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class P129():
    # 'Input_RPS'!P129
    value = 10413168
    formula = "=SUM(P125:P128)"
    @eval_fn
    def P129():
        range_1 = Input_RPS(16, 125, 16, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Q129():
    # 'Input_RPS'!Q129
    value = 10150174
    formula = "=SUM(Q125:Q128)"
    @eval_fn
    def Q129():
        range_1 = Input_RPS(17, 125, 17, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class R129():
    # 'Input_RPS'!R129
    value = 10035845
    formula = "=SUM(R125:R128)"
    @eval_fn
    def R129():
        range_1 = Input_RPS(18, 125, 18, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class S129():
    # 'Input_RPS'!S129
    value = 9987880
    formula = "=SUM(S125:S128)"
    @eval_fn
    def S129():
        range_1 = Input_RPS(19, 125, 19, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class T129():
    # 'Input_RPS'!T129
    value = 9639158
    formula = "=SUM(T125:T128)"
    @eval_fn
    def T129():
        range_1 = Input_RPS(20, 125, 20, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class U129():
    # 'Input_RPS'!U129
    value = 9500991
    formula = "=SUM(U125:U128)"
    @eval_fn
    def U129():
        range_1 = Input_RPS(21, 125, 21, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V129():
    # 'Input_RPS'!V129
    value = 9406166
    formula = "=SUM(V125:V128)"
    @eval_fn
    def V129():
        range_1 = Input_RPS(22, 125, 22, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class W129():
    # 'Input_RPS'!W129
    value = 9388576
    formula = "=SUM(W125:W128)"
    @eval_fn
    def W129():
        range_1 = Input_RPS(23, 125, 23, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class X129():
    # 'Input_RPS'!X129
    value = 0
    formula = "=SUM(X125:X128)"
    @eval_fn
    def X129():
        range_1 = Input_RPS(24, 125, 24, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Y129():
    # 'Input_RPS'!Y129
    value = 0
    formula = "=SUM(Y125:Y128)"
    @eval_fn
    def Y129():
        range_1 = Input_RPS(25, 125, 25, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class Z129():
    # 'Input_RPS'!Z129
    value = 0
    formula = "=SUM(Z125:Z128)"
    @eval_fn
    def Z129():
        range_1 = Input_RPS(26, 125, 26, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AA129():
    # 'Input_RPS'!AA129
    value = 0
    formula = "=SUM(AA125:AA128)"
    @eval_fn
    def AA129():
        range_1 = Input_RPS(27, 125, 27, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AB129():
    # 'Input_RPS'!AB129
    value = 0
    formula = "=SUM(AB125:AB128)"
    @eval_fn
    def AB129():
        range_1 = Input_RPS(28, 125, 28, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AC129():
    # 'Input_RPS'!AC129
    value = 0
    formula = "=SUM(AC125:AC128)"
    @eval_fn
    def AC129():
        range_1 = Input_RPS(29, 125, 29, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AD129():
    # 'Input_RPS'!AD129
    value = 0
    formula = "=SUM(AD125:AD128)"
    @eval_fn
    def AD129():
        range_1 = Input_RPS(30, 125, 30, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AE129():
    # 'Input_RPS'!AE129
    value = 0
    formula = "=SUM(AE125:AE128)"
    @eval_fn
    def AE129():
        range_1 = Input_RPS(31, 125, 31, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AF129():
    # 'Input_RPS'!AF129
    value = 0
    formula = "=SUM(AF125:AF128)"
    @eval_fn
    def AF129():
        range_1 = Input_RPS(32, 125, 32, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AG129():
    # 'Input_RPS'!AG129
    value = 0
    formula = "=SUM(AG125:AG128)"
    @eval_fn
    def AG129():
        range_1 = Input_RPS(33, 125, 33, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AH129():
    # 'Input_RPS'!AH129
    value = 0
    formula = "=SUM(AH125:AH128)"
    @eval_fn
    def AH129():
        range_1 = Input_RPS(34, 125, 34, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AI129():
    # 'Input_RPS'!AI129
    value = 0
    formula = "=SUM(AI125:AI128)"
    @eval_fn
    def AI129():
        range_1 = Input_RPS(35, 125, 35, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AJ129():
    # 'Input_RPS'!AJ129
    value = 0
    formula = "=SUM(AJ125:AJ128)"
    @eval_fn
    def AJ129():
        range_1 = Input_RPS(36, 125, 36, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AK129():
    # 'Input_RPS'!AK129
    value = 0
    formula = "=SUM(AK125:AK128)"
    @eval_fn
    def AK129():
        range_1 = Input_RPS(37, 125, 37, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class AL129():
    # 'Input_RPS'!AL129
    value = 0
    formula = "=SUM(AL125:AL128)"
    @eval_fn
    def AL129():
        range_1 = Input_RPS(38, 125, 38, 128)
        var_1 = SUM(range_1)
        return var_1

@register(Input_RPS)
class V130():
    # 'Input_RPS'!V130
    value = 0
    formula = "=SUM(V125:V128)-V129"
    @eval_fn
    def V130():
        range_1 = Input_RPS(22, 125, 22, 128)
        var_1 = SUM(range_1)
        v129_1 = Input_RPS.V129()
        var_2 = sub(var_1, v129_1)
        return var_2

@register(Input_RPS)
class C133():
    # 'Input_RPS'!C133
    value = "HECO DSM Programs"

@register(Input_RPS)
class E133():
    # 'Input_RPS'!E133
    value = "HECO IRP4 Table 6.1-1 pg 6-8"

@register(Input_RPS)
class H133():
    # 'Input_RPS'!H133
    value = 91500

@register(Input_RPS)
class I133():
    # 'Input_RPS'!I133
    value = 109600

@register(Input_RPS)
class J133():
    # 'Input_RPS'!J133
    value = 121100

@register(Input_RPS)
class K133():
    # 'Input_RPS'!K133
    value = 135100

@register(Input_RPS)
class L133():
    # 'Input_RPS'!L133
    value = 149300

@register(Input_RPS)
class M133():
    # 'Input_RPS'!M133
    value = 164900

@register(Input_RPS)
class N133():
    # 'Input_RPS'!N133
    value = 189300

@register(Input_RPS)
class C134():
    # 'Input_RPS'!C134
    value = "RPS Report Total DSM Program Impact"

@register(Input_RPS)
class L134():
    # 'Input_RPS'!L134
    value = 0
    formula = "=+L104"
    @eval_fn
    def L134():
        l104_1 = Input_RPS.L104()
        return l104_1

@register(Input_RPS)
class M134():
    # 'Input_RPS'!M134
    value = 343000
    formula = "=+M104"
    @eval_fn
    def M134():
        m104_1 = Input_RPS.M104()
        return m104_1

@register(Input_RPS)
class N134():
    # 'Input_RPS'!N134
    value = 398000
    formula = "=+N104"
    @eval_fn
    def N134():
        n104_1 = Input_RPS.N104()
        return n104_1

@register(Input_RPS)
class L135():
    # 'Input_RPS'!L135
    value = -149300
    formula = "=+L134-L133"
    @eval_fn
    def L135():
        l134_1 = Input_RPS.L134()
        l133_1 = Input_RPS.L133()
        var_1 = sub(l134_1, l133_1)
        return var_1

@register(Input_RPS)
class M135():
    # 'Input_RPS'!M135
    value = 178100
    formula = "=+M134-M133"
    @eval_fn
    def M135():
        m134_1 = Input_RPS.M134()
        m133_1 = Input_RPS.M133()
        var_1 = sub(m134_1, m133_1)
        return var_1

@register(Input_RPS)
class N135():
    # 'Input_RPS'!N135
    value = 208700
    formula = "=+N134-N133"
    @eval_fn
    def N135():
        n134_1 = Input_RPS.N134()
        n133_1 = Input_RPS.N133()
        var_1 = sub(n134_1, n133_1)
        return var_1

@register(Input_RPS)
class C136():
    # 'Input_RPS'!C136
    value = "Reconstructed"

@register(Input_RPS)
class H136():
    # 'Input_RPS'!H136
    value = 269900
    formula = "=+H133+178400"
    @eval_fn
    def H136():
        h133_1 = Input_RPS.H133()
        var_1 = add(h133_1, 178400)
        return var_1

@register(Input_RPS)
class I136():
    # 'Input_RPS'!I136
    value = 288000
    formula = "=+I133+178400"
    @eval_fn
    def I136():
        i133_1 = Input_RPS.I133()
        var_1 = add(i133_1, 178400)
        return var_1

@register(Input_RPS)
class J136():
    # 'Input_RPS'!J136
    value = 299500
    formula = "=+J133+178400"
    @eval_fn
    def J136():
        j133_1 = Input_RPS.J133()
        var_1 = add(j133_1, 178400)
        return var_1

@register(Input_RPS)
class K136():
    # 'Input_RPS'!K136
    value = 313500
    formula = "=+K133+178400"
    @eval_fn
    def K136():
        k133_1 = Input_RPS.K133()
        var_1 = add(k133_1, 178400)
        return var_1

@register(Input_RPS)
class L136():
    # 'Input_RPS'!L136
    value = 0
    formula = "=+L134"
    @eval_fn
    def L136():
        l134_1 = Input_RPS.L134()
        return l134_1

@register(Input_RPS)
class M136():
    # 'Input_RPS'!M136
    value = 343000
    formula = "=+M134"
    @eval_fn
    def M136():
        m134_1 = Input_RPS.M134()
        return m134_1

@register(Input_RPS)
class N136():
    # 'Input_RPS'!N136
    value = 398000
    formula = "=+N134"
    @eval_fn
    def N136():
        n134_1 = Input_RPS.N134()
        return n134_1

@register(Input_RPS)
class H137():
    # 'Input_RPS'!H137
    value = 0
    formula = "=+H101"
    @eval_fn
    def H137():
        h101_1 = Input_RPS.H101()
        return h101_1

@register(Input_RPS)
class I137():
    # 'Input_RPS'!I137
    value = 0
    formula = "=+I101"
    @eval_fn
    def I137():
        i101_1 = Input_RPS.I101()
        return i101_1

@register(Input_RPS)
class J137():
    # 'Input_RPS'!J137
    value = 0
    formula = "=+J101"
    @eval_fn
    def J137():
        j101_1 = Input_RPS.J101()
        return j101_1

@register(Input_RPS)
class K137():
    # 'Input_RPS'!K137
    value = 0
    formula = "=+K101"
    @eval_fn
    def K137():
        k101_1 = Input_RPS.K101()
        return k101_1

@register(Input_RPS)
class H138():
    # 'Input_RPS'!H138
    value = 269900
    formula = "=+H136-H137"
    @eval_fn
    def H138():
        h136_1 = Input_RPS.H136()
        h137_1 = Input_RPS.H137()
        var_1 = sub(h136_1, h137_1)
        return var_1

@register(Input_RPS)
class I138():
    # 'Input_RPS'!I138
    value = 288000
    formula = "=+I136-I137"
    @eval_fn
    def I138():
        i136_1 = Input_RPS.I136()
        i137_1 = Input_RPS.I137()
        var_1 = sub(i136_1, i137_1)
        return var_1

@register(Input_RPS)
class J138():
    # 'Input_RPS'!J138
    value = 299500
    formula = "=+J136-J137"
    @eval_fn
    def J138():
        j136_1 = Input_RPS.J136()
        j137_1 = Input_RPS.J137()
        var_1 = sub(j136_1, j137_1)
        return var_1

@register(Input_RPS)
class K138():
    # 'Input_RPS'!K138
    value = 313500
    formula = "=+K136-K137"
    @eval_fn
    def K138():
        k136_1 = Input_RPS.K136()
        k137_1 = Input_RPS.K137()
        var_1 = sub(k136_1, k137_1)
        return var_1