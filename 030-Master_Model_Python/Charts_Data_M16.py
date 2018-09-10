# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_Data_M16 = Worksheet('Charts_Data_M16', 10, 10)



@register(Charts_Data_M16)
class A1():
    # 'Charts_Data_M16'!A1
    value = "Metric 16: EEPS"

@register(Charts_Data_M16)
class D1():
    # 'Charts_Data_M16'!D1
    value = "Units"

@register(Charts_Data_M16)
class E1():
    # 'Charts_Data_M16'!E1
    value = "Source"

@register(Charts_Data_M16)
class F1():
    # 'Charts_Data_M16'!F1
    value = "Notes"

@register(Charts_Data_M16)
class G1():
    # 'Charts_Data_M16'!G1
    value = 1999

@register(Charts_Data_M16)
class H1():
    # 'Charts_Data_M16'!H1
    value = 2000

@register(Charts_Data_M16)
class I1():
    # 'Charts_Data_M16'!I1
    value = 2001

@register(Charts_Data_M16)
class J1():
    # 'Charts_Data_M16'!J1
    value = 2002

@register(Charts_Data_M16)
class K1():
    # 'Charts_Data_M16'!K1
    value = 2003

@register(Charts_Data_M16)
class L1():
    # 'Charts_Data_M16'!L1
    value = 2004

@register(Charts_Data_M16)
class M1():
    # 'Charts_Data_M16'!M1
    value = 2005

@register(Charts_Data_M16)
class N1():
    # 'Charts_Data_M16'!N1
    value = 2006

@register(Charts_Data_M16)
class O1():
    # 'Charts_Data_M16'!O1
    value = 2007

@register(Charts_Data_M16)
class P1():
    # 'Charts_Data_M16'!P1
    value = 2008

@register(Charts_Data_M16)
class Q1():
    # 'Charts_Data_M16'!Q1
    value = 2009

@register(Charts_Data_M16)
class R1():
    # 'Charts_Data_M16'!R1
    value = 2010

@register(Charts_Data_M16)
class S1():
    # 'Charts_Data_M16'!S1
    value = 2011

@register(Charts_Data_M16)
class T1():
    # 'Charts_Data_M16'!T1
    value = 2012

@register(Charts_Data_M16)
class U1():
    # 'Charts_Data_M16'!U1
    value = 2013

@register(Charts_Data_M16)
class V1():
    # 'Charts_Data_M16'!V1
    value = 2014

@register(Charts_Data_M16)
class W1():
    # 'Charts_Data_M16'!W1
    value = 2015

@register(Charts_Data_M16)
class X1():
    # 'Charts_Data_M16'!X1
    value = 2016

@register(Charts_Data_M16)
class Y1():
    # 'Charts_Data_M16'!Y1
    value = 2017

@register(Charts_Data_M16)
class Z1():
    # 'Charts_Data_M16'!Z1
    value = 2018

@register(Charts_Data_M16)
class AA1():
    # 'Charts_Data_M16'!AA1
    value = 2019

@register(Charts_Data_M16)
class AB1():
    # 'Charts_Data_M16'!AB1
    value = 2020

@register(Charts_Data_M16)
class AC1():
    # 'Charts_Data_M16'!AC1
    value = 2021

@register(Charts_Data_M16)
class AD1():
    # 'Charts_Data_M16'!AD1
    value = 2022

@register(Charts_Data_M16)
class AE1():
    # 'Charts_Data_M16'!AE1
    value = 2023

@register(Charts_Data_M16)
class AF1():
    # 'Charts_Data_M16'!AF1
    value = 2024

@register(Charts_Data_M16)
class AG1():
    # 'Charts_Data_M16'!AG1
    value = 2025

@register(Charts_Data_M16)
class AH1():
    # 'Charts_Data_M16'!AH1
    value = 2026

@register(Charts_Data_M16)
class AI1():
    # 'Charts_Data_M16'!AI1
    value = 2027

@register(Charts_Data_M16)
class AJ1():
    # 'Charts_Data_M16'!AJ1
    value = 2028

@register(Charts_Data_M16)
class AK1():
    # 'Charts_Data_M16'!AK1
    value = 2029

@register(Charts_Data_M16)
class AL1():
    # 'Charts_Data_M16'!AL1
    value = 2030

@register(Charts_Data_M16)
class A2():
    # 'Charts_Data_M16'!A2
    value = "EEPS Chart 2 Title"

@register(Charts_Data_M16)
class B2():
    # 'Charts_Data_M16'!B2
    value = "Electricity Saved in 2009"
    formula = '''="Electricity Saved in "&VLOOKUP('Charts M16'!$B$28,'Charts Interactive LookupTables'!$W:$AA,4,FALSE)'''
    @eval_fn
    def B2():
        b28_1 = Charts_M16.B28()
        range_1 = Charts_Interactive_LookupTables(23, 0, 27, 0)
        var_1 = VLOOKUP(b28_1, range_1, 4, "FALSE")
        var_2 = concat("Electricity Saved in ", var_1)
        return var_2

@register(Charts_Data_M16)
class F2():
    # 'Charts_Data_M16'!F2
    value = "Notes"

@register(Charts_Data_M16)
class A3():
    # 'Charts_Data_M16'!A3
    value = "Line Graph Input 1"

@register(Charts_Data_M16)
class C3():
    # 'Charts_Data_M16'!C3
    value = "#N/A"
    formula = '''=D3&VLOOKUP('Charts M16'!$B$2,'Charts Interactive LookupTables'!$W:$AA,5,FALSE)&"Total EE"'''
    @eval_fn
    def C3():
        d3_1 = Charts_Data_M16.D3()
        b2_1 = Charts_M16.B2()
        range_1 = Charts_Interactive_LookupTables(23, 0, 27, 0)
        var_1 = VLOOKUP(b2_1, range_1, 5, "FALSE")
        var_2 = concat(d3_1, var_1)
        var_3 = concat(var_2, "Total EE")
        return var_3

@register(Charts_Data_M16)
class D3():
    # 'Charts_Data_M16'!D3
    value = "HECO"

@register(Charts_Data_M16)
class F3():
    # 'Charts_Data_M16'!F3
    value = "Notes"

@register(Charts_Data_M16)
class G3():
    # 'Charts_Data_M16'!G3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!G17=0,NA(),'Dashboard M16 EEPS'!G17)"
    @eval_fn
    def G3():
        g17_1 = Dashboard_M16_EEPS.G17()
        var_1 = equal(g17_1, 0)
        var_2 = NA()
        g17_2 = Dashboard_M16_EEPS.G17()
        var_3 = IF(var_1, var_2, g17_2)
        return var_3

@register(Charts_Data_M16)
class H3():
    # 'Charts_Data_M16'!H3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!H17=0,NA(),'Dashboard M16 EEPS'!H17)"
    @eval_fn
    def H3():
        h17_1 = Dashboard_M16_EEPS.H17()
        var_1 = equal(h17_1, 0)
        var_2 = NA()
        h17_2 = Dashboard_M16_EEPS.H17()
        var_3 = IF(var_1, var_2, h17_2)
        return var_3

@register(Charts_Data_M16)
class I3():
    # 'Charts_Data_M16'!I3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!I17=0,NA(),'Dashboard M16 EEPS'!I17)"
    @eval_fn
    def I3():
        i17_1 = Dashboard_M16_EEPS.I17()
        var_1 = equal(i17_1, 0)
        var_2 = NA()
        i17_2 = Dashboard_M16_EEPS.I17()
        var_3 = IF(var_1, var_2, i17_2)
        return var_3

@register(Charts_Data_M16)
class J3():
    # 'Charts_Data_M16'!J3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!J17=0,NA(),'Dashboard M16 EEPS'!J17)"
    @eval_fn
    def J3():
        j17_1 = Dashboard_M16_EEPS.J17()
        var_1 = equal(j17_1, 0)
        var_2 = NA()
        j17_2 = Dashboard_M16_EEPS.J17()
        var_3 = IF(var_1, var_2, j17_2)
        return var_3

@register(Charts_Data_M16)
class K3():
    # 'Charts_Data_M16'!K3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!K17=0,NA(),'Dashboard M16 EEPS'!K17)"
    @eval_fn
    def K3():
        k17_1 = Dashboard_M16_EEPS.K17()
        var_1 = equal(k17_1, 0)
        var_2 = NA()
        k17_2 = Dashboard_M16_EEPS.K17()
        var_3 = IF(var_1, var_2, k17_2)
        return var_3

@register(Charts_Data_M16)
class L3():
    # 'Charts_Data_M16'!L3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!L17=0,NA(),'Dashboard M16 EEPS'!L17)"
    @eval_fn
    def L3():
        l17_1 = Dashboard_M16_EEPS.L17()
        var_1 = equal(l17_1, 0)
        var_2 = NA()
        l17_2 = Dashboard_M16_EEPS.L17()
        var_3 = IF(var_1, var_2, l17_2)
        return var_3

@register(Charts_Data_M16)
class M3():
    # 'Charts_Data_M16'!M3
    value = 292000
    formula = "=IF('Dashboard M16 EEPS'!M17=0,NA(),'Dashboard M16 EEPS'!M17)"
    @eval_fn
    def M3():
        m17_1 = Dashboard_M16_EEPS.M17()
        var_1 = equal(m17_1, 0)
        var_2 = NA()
        m17_2 = Dashboard_M16_EEPS.M17()
        var_3 = IF(var_1, var_2, m17_2)
        return var_3

@register(Charts_Data_M16)
class N3():
    # 'Charts_Data_M16'!N3
    value = 340000
    formula = "=IF('Dashboard M16 EEPS'!N17=0,NA(),'Dashboard M16 EEPS'!N17)"
    @eval_fn
    def N3():
        n17_1 = Dashboard_M16_EEPS.N17()
        var_1 = equal(n17_1, 0)
        var_2 = NA()
        n17_2 = Dashboard_M16_EEPS.N17()
        var_3 = IF(var_1, var_2, n17_2)
        return var_3

@register(Charts_Data_M16)
class O3():
    # 'Charts_Data_M16'!O3
    value = 453000
    formula = "=IF('Dashboard M16 EEPS'!O17=0,NA(),'Dashboard M16 EEPS'!O17)"
    @eval_fn
    def O3():
        o17_1 = Dashboard_M16_EEPS.O17()
        var_1 = equal(o17_1, 0)
        var_2 = NA()
        o17_2 = Dashboard_M16_EEPS.O17()
        var_3 = IF(var_1, var_2, o17_2)
        return var_3

@register(Charts_Data_M16)
class P3():
    # 'Charts_Data_M16'!P3
    value = 604007
    formula = "=IF('Dashboard M16 EEPS'!P17=0,NA(),'Dashboard M16 EEPS'!P17)"
    @eval_fn
    def P3():
        p17_1 = Dashboard_M16_EEPS.P17()
        var_1 = equal(p17_1, 0)
        var_2 = NA()
        p17_2 = Dashboard_M16_EEPS.P17()
        var_3 = IF(var_1, var_2, p17_2)
        return var_3

@register(Charts_Data_M16)
class Q3():
    # 'Charts_Data_M16'!Q3
    value = 651278
    formula = "=IF('Dashboard M16 EEPS'!Q17=0,NA(),'Dashboard M16 EEPS'!Q17)"
    @eval_fn
    def Q3():
        q17_1 = Dashboard_M16_EEPS.Q17()
        var_1 = equal(q17_1, 0)
        var_2 = NA()
        q17_2 = Dashboard_M16_EEPS.Q17()
        var_3 = IF(var_1, var_2, q17_2)
        return var_3

@register(Charts_Data_M16)
class R3():
    # 'Charts_Data_M16'!R3
    value = 738337
    formula = "=IF('Dashboard M16 EEPS'!R17=0,NA(),'Dashboard M16 EEPS'!R17)"
    @eval_fn
    def R3():
        r17_1 = Dashboard_M16_EEPS.R17()
        var_1 = equal(r17_1, 0)
        var_2 = NA()
        r17_2 = Dashboard_M16_EEPS.R17()
        var_3 = IF(var_1, var_2, r17_2)
        return var_3

@register(Charts_Data_M16)
class S3():
    # 'Charts_Data_M16'!S3
    value = 821136
    formula = "=IF('Dashboard M16 EEPS'!S17=0,NA(),'Dashboard M16 EEPS'!S17)"
    @eval_fn
    def S3():
        s17_1 = Dashboard_M16_EEPS.S17()
        var_1 = equal(s17_1, 0)
        var_2 = NA()
        s17_2 = Dashboard_M16_EEPS.S17()
        var_3 = IF(var_1, var_2, s17_2)
        return var_3

@register(Charts_Data_M16)
class T3():
    # 'Charts_Data_M16'!T3
    value = 958155
    formula = "=IF('Dashboard M16 EEPS'!T17=0,NA(),'Dashboard M16 EEPS'!T17)"
    @eval_fn
    def T3():
        t17_1 = Dashboard_M16_EEPS.T17()
        var_1 = equal(t17_1, 0)
        var_2 = NA()
        t17_2 = Dashboard_M16_EEPS.T17()
        var_3 = IF(var_1, var_2, t17_2)
        return var_3

@register(Charts_Data_M16)
class U3():
    # 'Charts_Data_M16'!U3
    value = 1039167
    formula = "=IF('Dashboard M16 EEPS'!U17=0,NA(),'Dashboard M16 EEPS'!U17)"
    @eval_fn
    def U3():
        u17_1 = Dashboard_M16_EEPS.U17()
        var_1 = equal(u17_1, 0)
        var_2 = NA()
        u17_2 = Dashboard_M16_EEPS.U17()
        var_3 = IF(var_1, var_2, u17_2)
        return var_3

@register(Charts_Data_M16)
class V3():
    # 'Charts_Data_M16'!V3
    value = 1117117
    formula = "=IF('Dashboard M16 EEPS'!V17=0,NA(),'Dashboard M16 EEPS'!V17)"
    @eval_fn
    def V3():
        v17_1 = Dashboard_M16_EEPS.V17()
        var_1 = equal(v17_1, 0)
        var_2 = NA()
        v17_2 = Dashboard_M16_EEPS.V17()
        var_3 = IF(var_1, var_2, v17_2)
        return var_3

@register(Charts_Data_M16)
class W3():
    # 'Charts_Data_M16'!W3
    value = 1195067
    formula = "=IF('Dashboard M16 EEPS'!W17=0,NA(),'Dashboard M16 EEPS'!W17)"
    @eval_fn
    def W3():
        w17_1 = Dashboard_M16_EEPS.W17()
        var_1 = equal(w17_1, 0)
        var_2 = NA()
        w17_2 = Dashboard_M16_EEPS.W17()
        var_3 = IF(var_1, var_2, w17_2)
        return var_3

@register(Charts_Data_M16)
class X3():
    # 'Charts_Data_M16'!X3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!X17=0,NA(),'Dashboard M16 EEPS'!X17)"
    @eval_fn
    def X3():
        x17_1 = Dashboard_M16_EEPS.X17()
        var_1 = equal(x17_1, 0)
        var_2 = NA()
        x17_2 = Dashboard_M16_EEPS.X17()
        var_3 = IF(var_1, var_2, x17_2)
        return var_3

@register(Charts_Data_M16)
class Y3():
    # 'Charts_Data_M16'!Y3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!Y17=0,NA(),'Dashboard M16 EEPS'!Y17)"
    @eval_fn
    def Y3():
        y17_1 = Dashboard_M16_EEPS.Y17()
        var_1 = equal(y17_1, 0)
        var_2 = NA()
        y17_2 = Dashboard_M16_EEPS.Y17()
        var_3 = IF(var_1, var_2, y17_2)
        return var_3

@register(Charts_Data_M16)
class Z3():
    # 'Charts_Data_M16'!Z3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!Z17=0,NA(),'Dashboard M16 EEPS'!Z17)"
    @eval_fn
    def Z3():
        z17_1 = Dashboard_M16_EEPS.Z17()
        var_1 = equal(z17_1, 0)
        var_2 = NA()
        z17_2 = Dashboard_M16_EEPS.Z17()
        var_3 = IF(var_1, var_2, z17_2)
        return var_3

@register(Charts_Data_M16)
class AA3():
    # 'Charts_Data_M16'!AA3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AA17=0,NA(),'Dashboard M16 EEPS'!AA17)"
    @eval_fn
    def AA3():
        aa17_1 = Dashboard_M16_EEPS.AA17()
        var_1 = equal(aa17_1, 0)
        var_2 = NA()
        aa17_2 = Dashboard_M16_EEPS.AA17()
        var_3 = IF(var_1, var_2, aa17_2)
        return var_3

@register(Charts_Data_M16)
class AB3():
    # 'Charts_Data_M16'!AB3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AB17=0,NA(),'Dashboard M16 EEPS'!AB17)"
    @eval_fn
    def AB3():
        ab17_1 = Dashboard_M16_EEPS.AB17()
        var_1 = equal(ab17_1, 0)
        var_2 = NA()
        ab17_2 = Dashboard_M16_EEPS.AB17()
        var_3 = IF(var_1, var_2, ab17_2)
        return var_3

@register(Charts_Data_M16)
class AC3():
    # 'Charts_Data_M16'!AC3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AC17=0,NA(),'Dashboard M16 EEPS'!AC17)"
    @eval_fn
    def AC3():
        ac17_1 = Dashboard_M16_EEPS.AC17()
        var_1 = equal(ac17_1, 0)
        var_2 = NA()
        ac17_2 = Dashboard_M16_EEPS.AC17()
        var_3 = IF(var_1, var_2, ac17_2)
        return var_3

@register(Charts_Data_M16)
class AD3():
    # 'Charts_Data_M16'!AD3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AD17=0,NA(),'Dashboard M16 EEPS'!AD17)"
    @eval_fn
    def AD3():
        ad17_1 = Dashboard_M16_EEPS.AD17()
        var_1 = equal(ad17_1, 0)
        var_2 = NA()
        ad17_2 = Dashboard_M16_EEPS.AD17()
        var_3 = IF(var_1, var_2, ad17_2)
        return var_3

@register(Charts_Data_M16)
class AE3():
    # 'Charts_Data_M16'!AE3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AE17=0,NA(),'Dashboard M16 EEPS'!AE17)"
    @eval_fn
    def AE3():
        ae17_1 = Dashboard_M16_EEPS.AE17()
        var_1 = equal(ae17_1, 0)
        var_2 = NA()
        ae17_2 = Dashboard_M16_EEPS.AE17()
        var_3 = IF(var_1, var_2, ae17_2)
        return var_3

@register(Charts_Data_M16)
class AF3():
    # 'Charts_Data_M16'!AF3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AF17=0,NA(),'Dashboard M16 EEPS'!AF17)"
    @eval_fn
    def AF3():
        af17_1 = Dashboard_M16_EEPS.AF17()
        var_1 = equal(af17_1, 0)
        var_2 = NA()
        af17_2 = Dashboard_M16_EEPS.AF17()
        var_3 = IF(var_1, var_2, af17_2)
        return var_3

@register(Charts_Data_M16)
class AG3():
    # 'Charts_Data_M16'!AG3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AG17=0,NA(),'Dashboard M16 EEPS'!AG17)"
    @eval_fn
    def AG3():
        ag17_1 = Dashboard_M16_EEPS.AG17()
        var_1 = equal(ag17_1, 0)
        var_2 = NA()
        ag17_2 = Dashboard_M16_EEPS.AG17()
        var_3 = IF(var_1, var_2, ag17_2)
        return var_3

@register(Charts_Data_M16)
class AH3():
    # 'Charts_Data_M16'!AH3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AH17=0,NA(),'Dashboard M16 EEPS'!AH17)"
    @eval_fn
    def AH3():
        ah17_1 = Dashboard_M16_EEPS.AH17()
        var_1 = equal(ah17_1, 0)
        var_2 = NA()
        ah17_2 = Dashboard_M16_EEPS.AH17()
        var_3 = IF(var_1, var_2, ah17_2)
        return var_3

@register(Charts_Data_M16)
class AI3():
    # 'Charts_Data_M16'!AI3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AI17=0,NA(),'Dashboard M16 EEPS'!AI17)"
    @eval_fn
    def AI3():
        ai17_1 = Dashboard_M16_EEPS.AI17()
        var_1 = equal(ai17_1, 0)
        var_2 = NA()
        ai17_2 = Dashboard_M16_EEPS.AI17()
        var_3 = IF(var_1, var_2, ai17_2)
        return var_3

@register(Charts_Data_M16)
class AJ3():
    # 'Charts_Data_M16'!AJ3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AJ17=0,NA(),'Dashboard M16 EEPS'!AJ17)"
    @eval_fn
    def AJ3():
        aj17_1 = Dashboard_M16_EEPS.AJ17()
        var_1 = equal(aj17_1, 0)
        var_2 = NA()
        aj17_2 = Dashboard_M16_EEPS.AJ17()
        var_3 = IF(var_1, var_2, aj17_2)
        return var_3

@register(Charts_Data_M16)
class AK3():
    # 'Charts_Data_M16'!AK3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AK17=0,NA(),'Dashboard M16 EEPS'!AK17)"
    @eval_fn
    def AK3():
        ak17_1 = Dashboard_M16_EEPS.AK17()
        var_1 = equal(ak17_1, 0)
        var_2 = NA()
        ak17_2 = Dashboard_M16_EEPS.AK17()
        var_3 = IF(var_1, var_2, ak17_2)
        return var_3

@register(Charts_Data_M16)
class AL3():
    # 'Charts_Data_M16'!AL3
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AL17=0,NA(),'Dashboard M16 EEPS'!AL17)"
    @eval_fn
    def AL3():
        al17_1 = Dashboard_M16_EEPS.AL17()
        var_1 = equal(al17_1, 0)
        var_2 = NA()
        al17_2 = Dashboard_M16_EEPS.AL17()
        var_3 = IF(var_1, var_2, al17_2)
        return var_3

@register(Charts_Data_M16)
class C4():
    # 'Charts_Data_M16'!C4
    value = "#N/A"
    formula = '''=D4&VLOOKUP('Charts M16'!$B$2,'Charts Interactive LookupTables'!$W:$AA,5,FALSE)&"Total EE"'''
    @eval_fn
    def C4():
        d4_1 = Charts_Data_M16.D4()
        b2_1 = Charts_M16.B2()
        range_1 = Charts_Interactive_LookupTables(23, 0, 27, 0)
        var_1 = VLOOKUP(b2_1, range_1, 5, "FALSE")
        var_2 = concat(d4_1, var_1)
        var_3 = concat(var_2, "Total EE")
        return var_3

@register(Charts_Data_M16)
class D4():
    # 'Charts_Data_M16'!D4
    value = "HELCO"

@register(Charts_Data_M16)
class F4():
    # 'Charts_Data_M16'!F4
    value = "Notes"

@register(Charts_Data_M16)
class G4():
    # 'Charts_Data_M16'!G4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!G21=0,NA(),'Dashboard M16 EEPS'!G21)"
    @eval_fn
    def G4():
        g21_1 = Dashboard_M16_EEPS.G21()
        var_1 = equal(g21_1, 0)
        var_2 = NA()
        g21_2 = Dashboard_M16_EEPS.G21()
        var_3 = IF(var_1, var_2, g21_2)
        return var_3

@register(Charts_Data_M16)
class H4():
    # 'Charts_Data_M16'!H4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!H21=0,NA(),'Dashboard M16 EEPS'!H21)"
    @eval_fn
    def H4():
        h21_1 = Dashboard_M16_EEPS.H21()
        var_1 = equal(h21_1, 0)
        var_2 = NA()
        h21_2 = Dashboard_M16_EEPS.H21()
        var_3 = IF(var_1, var_2, h21_2)
        return var_3

@register(Charts_Data_M16)
class I4():
    # 'Charts_Data_M16'!I4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!I21=0,NA(),'Dashboard M16 EEPS'!I21)"
    @eval_fn
    def I4():
        i21_1 = Dashboard_M16_EEPS.I21()
        var_1 = equal(i21_1, 0)
        var_2 = NA()
        i21_2 = Dashboard_M16_EEPS.I21()
        var_3 = IF(var_1, var_2, i21_2)
        return var_3

@register(Charts_Data_M16)
class J4():
    # 'Charts_Data_M16'!J4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!J21=0,NA(),'Dashboard M16 EEPS'!J21)"
    @eval_fn
    def J4():
        j21_1 = Dashboard_M16_EEPS.J21()
        var_1 = equal(j21_1, 0)
        var_2 = NA()
        j21_2 = Dashboard_M16_EEPS.J21()
        var_3 = IF(var_1, var_2, j21_2)
        return var_3

@register(Charts_Data_M16)
class K4():
    # 'Charts_Data_M16'!K4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!K21=0,NA(),'Dashboard M16 EEPS'!K21)"
    @eval_fn
    def K4():
        k21_1 = Dashboard_M16_EEPS.K21()
        var_1 = equal(k21_1, 0)
        var_2 = NA()
        k21_2 = Dashboard_M16_EEPS.K21()
        var_3 = IF(var_1, var_2, k21_2)
        return var_3

@register(Charts_Data_M16)
class L4():
    # 'Charts_Data_M16'!L4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!L21=0,NA(),'Dashboard M16 EEPS'!L21)"
    @eval_fn
    def L4():
        l21_1 = Dashboard_M16_EEPS.L21()
        var_1 = equal(l21_1, 0)
        var_2 = NA()
        l21_2 = Dashboard_M16_EEPS.L21()
        var_3 = IF(var_1, var_2, l21_2)
        return var_3

@register(Charts_Data_M16)
class M4():
    # 'Charts_Data_M16'!M4
    value = 49000
    formula = "=IF('Dashboard M16 EEPS'!M21=0,NA(),'Dashboard M16 EEPS'!M21)"
    @eval_fn
    def M4():
        m21_1 = Dashboard_M16_EEPS.M21()
        var_1 = equal(m21_1, 0)
        var_2 = NA()
        m21_2 = Dashboard_M16_EEPS.M21()
        var_3 = IF(var_1, var_2, m21_2)
        return var_3

@register(Charts_Data_M16)
class N4():
    # 'Charts_Data_M16'!N4
    value = 54000
    formula = "=IF('Dashboard M16 EEPS'!N21=0,NA(),'Dashboard M16 EEPS'!N21)"
    @eval_fn
    def N4():
        n21_1 = Dashboard_M16_EEPS.N21()
        var_1 = equal(n21_1, 0)
        var_2 = NA()
        n21_2 = Dashboard_M16_EEPS.N21()
        var_3 = IF(var_1, var_2, n21_2)
        return var_3

@register(Charts_Data_M16)
class O4():
    # 'Charts_Data_M16'!O4
    value = 57000
    formula = "=IF('Dashboard M16 EEPS'!O21=0,NA(),'Dashboard M16 EEPS'!O21)"
    @eval_fn
    def O4():
        o21_1 = Dashboard_M16_EEPS.O21()
        var_1 = equal(o21_1, 0)
        var_2 = NA()
        o21_2 = Dashboard_M16_EEPS.O21()
        var_3 = IF(var_1, var_2, o21_2)
        return var_3

@register(Charts_Data_M16)
class P4():
    # 'Charts_Data_M16'!P4
    value = 47051
    formula = "=IF('Dashboard M16 EEPS'!P21=0,NA(),'Dashboard M16 EEPS'!P21)"
    @eval_fn
    def P4():
        p21_1 = Dashboard_M16_EEPS.P21()
        var_1 = equal(p21_1, 0)
        var_2 = NA()
        p21_2 = Dashboard_M16_EEPS.P21()
        var_3 = IF(var_1, var_2, p21_2)
        return var_3

@register(Charts_Data_M16)
class Q4():
    # 'Charts_Data_M16'!Q4
    value = 49760
    formula = "=IF('Dashboard M16 EEPS'!Q21=0,NA(),'Dashboard M16 EEPS'!Q21)"
    @eval_fn
    def Q4():
        q21_1 = Dashboard_M16_EEPS.Q21()
        var_1 = equal(q21_1, 0)
        var_2 = NA()
        q21_2 = Dashboard_M16_EEPS.Q21()
        var_3 = IF(var_1, var_2, q21_2)
        return var_3

@register(Charts_Data_M16)
class R4():
    # 'Charts_Data_M16'!R4
    value = 62359
    formula = "=IF('Dashboard M16 EEPS'!R21=0,NA(),'Dashboard M16 EEPS'!R21)"
    @eval_fn
    def R4():
        r21_1 = Dashboard_M16_EEPS.R21()
        var_1 = equal(r21_1, 0)
        var_2 = NA()
        r21_2 = Dashboard_M16_EEPS.R21()
        var_3 = IF(var_1, var_2, r21_2)
        return var_3

@register(Charts_Data_M16)
class S4():
    # 'Charts_Data_M16'!S4
    value = 76622
    formula = "=IF('Dashboard M16 EEPS'!S21=0,NA(),'Dashboard M16 EEPS'!S21)"
    @eval_fn
    def S4():
        s21_1 = Dashboard_M16_EEPS.S21()
        var_1 = equal(s21_1, 0)
        var_2 = NA()
        s21_2 = Dashboard_M16_EEPS.S21()
        var_3 = IF(var_1, var_2, s21_2)
        return var_3

@register(Charts_Data_M16)
class T4():
    # 'Charts_Data_M16'!T4
    value = 97765
    formula = "=IF('Dashboard M16 EEPS'!T21=0,NA(),'Dashboard M16 EEPS'!T21)"
    @eval_fn
    def T4():
        t21_1 = Dashboard_M16_EEPS.T21()
        var_1 = equal(t21_1, 0)
        var_2 = NA()
        t21_2 = Dashboard_M16_EEPS.T21()
        var_3 = IF(var_1, var_2, t21_2)
        return var_3

@register(Charts_Data_M16)
class U4():
    # 'Charts_Data_M16'!U4
    value = 114116
    formula = "=IF('Dashboard M16 EEPS'!U21=0,NA(),'Dashboard M16 EEPS'!U21)"
    @eval_fn
    def U4():
        u21_1 = Dashboard_M16_EEPS.U21()
        var_1 = equal(u21_1, 0)
        var_2 = NA()
        u21_2 = Dashboard_M16_EEPS.U21()
        var_3 = IF(var_1, var_2, u21_2)
        return var_3

@register(Charts_Data_M16)
class V4():
    # 'Charts_Data_M16'!V4
    value = 123070
    formula = "=IF('Dashboard M16 EEPS'!V21=0,NA(),'Dashboard M16 EEPS'!V21)"
    @eval_fn
    def V4():
        v21_1 = Dashboard_M16_EEPS.V21()
        var_1 = equal(v21_1, 0)
        var_2 = NA()
        v21_2 = Dashboard_M16_EEPS.V21()
        var_3 = IF(var_1, var_2, v21_2)
        return var_3

@register(Charts_Data_M16)
class W4():
    # 'Charts_Data_M16'!W4
    value = 132024
    formula = "=IF('Dashboard M16 EEPS'!W21=0,NA(),'Dashboard M16 EEPS'!W21)"
    @eval_fn
    def W4():
        w21_1 = Dashboard_M16_EEPS.W21()
        var_1 = equal(w21_1, 0)
        var_2 = NA()
        w21_2 = Dashboard_M16_EEPS.W21()
        var_3 = IF(var_1, var_2, w21_2)
        return var_3

@register(Charts_Data_M16)
class X4():
    # 'Charts_Data_M16'!X4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!X21=0,NA(),'Dashboard M16 EEPS'!X21)"
    @eval_fn
    def X4():
        x21_1 = Dashboard_M16_EEPS.X21()
        var_1 = equal(x21_1, 0)
        var_2 = NA()
        x21_2 = Dashboard_M16_EEPS.X21()
        var_3 = IF(var_1, var_2, x21_2)
        return var_3

@register(Charts_Data_M16)
class Y4():
    # 'Charts_Data_M16'!Y4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!Y21=0,NA(),'Dashboard M16 EEPS'!Y21)"
    @eval_fn
    def Y4():
        y21_1 = Dashboard_M16_EEPS.Y21()
        var_1 = equal(y21_1, 0)
        var_2 = NA()
        y21_2 = Dashboard_M16_EEPS.Y21()
        var_3 = IF(var_1, var_2, y21_2)
        return var_3

@register(Charts_Data_M16)
class Z4():
    # 'Charts_Data_M16'!Z4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!Z21=0,NA(),'Dashboard M16 EEPS'!Z21)"
    @eval_fn
    def Z4():
        z21_1 = Dashboard_M16_EEPS.Z21()
        var_1 = equal(z21_1, 0)
        var_2 = NA()
        z21_2 = Dashboard_M16_EEPS.Z21()
        var_3 = IF(var_1, var_2, z21_2)
        return var_3

@register(Charts_Data_M16)
class AA4():
    # 'Charts_Data_M16'!AA4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AA21=0,NA(),'Dashboard M16 EEPS'!AA21)"
    @eval_fn
    def AA4():
        aa21_1 = Dashboard_M16_EEPS.AA21()
        var_1 = equal(aa21_1, 0)
        var_2 = NA()
        aa21_2 = Dashboard_M16_EEPS.AA21()
        var_3 = IF(var_1, var_2, aa21_2)
        return var_3

@register(Charts_Data_M16)
class AB4():
    # 'Charts_Data_M16'!AB4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AB21=0,NA(),'Dashboard M16 EEPS'!AB21)"
    @eval_fn
    def AB4():
        ab21_1 = Dashboard_M16_EEPS.AB21()
        var_1 = equal(ab21_1, 0)
        var_2 = NA()
        ab21_2 = Dashboard_M16_EEPS.AB21()
        var_3 = IF(var_1, var_2, ab21_2)
        return var_3

@register(Charts_Data_M16)
class AC4():
    # 'Charts_Data_M16'!AC4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AC21=0,NA(),'Dashboard M16 EEPS'!AC21)"
    @eval_fn
    def AC4():
        ac21_1 = Dashboard_M16_EEPS.AC21()
        var_1 = equal(ac21_1, 0)
        var_2 = NA()
        ac21_2 = Dashboard_M16_EEPS.AC21()
        var_3 = IF(var_1, var_2, ac21_2)
        return var_3

@register(Charts_Data_M16)
class AD4():
    # 'Charts_Data_M16'!AD4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AD21=0,NA(),'Dashboard M16 EEPS'!AD21)"
    @eval_fn
    def AD4():
        ad21_1 = Dashboard_M16_EEPS.AD21()
        var_1 = equal(ad21_1, 0)
        var_2 = NA()
        ad21_2 = Dashboard_M16_EEPS.AD21()
        var_3 = IF(var_1, var_2, ad21_2)
        return var_3

@register(Charts_Data_M16)
class AE4():
    # 'Charts_Data_M16'!AE4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AE21=0,NA(),'Dashboard M16 EEPS'!AE21)"
    @eval_fn
    def AE4():
        ae21_1 = Dashboard_M16_EEPS.AE21()
        var_1 = equal(ae21_1, 0)
        var_2 = NA()
        ae21_2 = Dashboard_M16_EEPS.AE21()
        var_3 = IF(var_1, var_2, ae21_2)
        return var_3

@register(Charts_Data_M16)
class AF4():
    # 'Charts_Data_M16'!AF4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AF21=0,NA(),'Dashboard M16 EEPS'!AF21)"
    @eval_fn
    def AF4():
        af21_1 = Dashboard_M16_EEPS.AF21()
        var_1 = equal(af21_1, 0)
        var_2 = NA()
        af21_2 = Dashboard_M16_EEPS.AF21()
        var_3 = IF(var_1, var_2, af21_2)
        return var_3

@register(Charts_Data_M16)
class AG4():
    # 'Charts_Data_M16'!AG4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AG21=0,NA(),'Dashboard M16 EEPS'!AG21)"
    @eval_fn
    def AG4():
        ag21_1 = Dashboard_M16_EEPS.AG21()
        var_1 = equal(ag21_1, 0)
        var_2 = NA()
        ag21_2 = Dashboard_M16_EEPS.AG21()
        var_3 = IF(var_1, var_2, ag21_2)
        return var_3

@register(Charts_Data_M16)
class AH4():
    # 'Charts_Data_M16'!AH4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AH21=0,NA(),'Dashboard M16 EEPS'!AH21)"
    @eval_fn
    def AH4():
        ah21_1 = Dashboard_M16_EEPS.AH21()
        var_1 = equal(ah21_1, 0)
        var_2 = NA()
        ah21_2 = Dashboard_M16_EEPS.AH21()
        var_3 = IF(var_1, var_2, ah21_2)
        return var_3

@register(Charts_Data_M16)
class AI4():
    # 'Charts_Data_M16'!AI4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AI21=0,NA(),'Dashboard M16 EEPS'!AI21)"
    @eval_fn
    def AI4():
        ai21_1 = Dashboard_M16_EEPS.AI21()
        var_1 = equal(ai21_1, 0)
        var_2 = NA()
        ai21_2 = Dashboard_M16_EEPS.AI21()
        var_3 = IF(var_1, var_2, ai21_2)
        return var_3

@register(Charts_Data_M16)
class AJ4():
    # 'Charts_Data_M16'!AJ4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AJ21=0,NA(),'Dashboard M16 EEPS'!AJ21)"
    @eval_fn
    def AJ4():
        aj21_1 = Dashboard_M16_EEPS.AJ21()
        var_1 = equal(aj21_1, 0)
        var_2 = NA()
        aj21_2 = Dashboard_M16_EEPS.AJ21()
        var_3 = IF(var_1, var_2, aj21_2)
        return var_3

@register(Charts_Data_M16)
class AK4():
    # 'Charts_Data_M16'!AK4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AK21=0,NA(),'Dashboard M16 EEPS'!AK21)"
    @eval_fn
    def AK4():
        ak21_1 = Dashboard_M16_EEPS.AK21()
        var_1 = equal(ak21_1, 0)
        var_2 = NA()
        ak21_2 = Dashboard_M16_EEPS.AK21()
        var_3 = IF(var_1, var_2, ak21_2)
        return var_3

@register(Charts_Data_M16)
class AL4():
    # 'Charts_Data_M16'!AL4
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AL21=0,NA(),'Dashboard M16 EEPS'!AL21)"
    @eval_fn
    def AL4():
        al21_1 = Dashboard_M16_EEPS.AL21()
        var_1 = equal(al21_1, 0)
        var_2 = NA()
        al21_2 = Dashboard_M16_EEPS.AL21()
        var_3 = IF(var_1, var_2, al21_2)
        return var_3

@register(Charts_Data_M16)
class C5():
    # 'Charts_Data_M16'!C5
    value = "#N/A"
    formula = '''=D5&VLOOKUP('Charts M16'!$B$2,'Charts Interactive LookupTables'!$W:$AA,5,FALSE)&"Total EE"'''
    @eval_fn
    def C5():
        d5_1 = Charts_Data_M16.D5()
        b2_1 = Charts_M16.B2()
        range_1 = Charts_Interactive_LookupTables(23, 0, 27, 0)
        var_1 = VLOOKUP(b2_1, range_1, 5, "FALSE")
        var_2 = concat(d5_1, var_1)
        var_3 = concat(var_2, "Total EE")
        return var_3

@register(Charts_Data_M16)
class D5():
    # 'Charts_Data_M16'!D5
    value = "MECO"

@register(Charts_Data_M16)
class F5():
    # 'Charts_Data_M16'!F5
    value = "Notes"

@register(Charts_Data_M16)
class G5():
    # 'Charts_Data_M16'!G5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!G25=0,NA(),'Dashboard M16 EEPS'!G25)"
    @eval_fn
    def G5():
        g25_1 = Dashboard_M16_EEPS.G25()
        var_1 = equal(g25_1, 0)
        var_2 = NA()
        g25_2 = Dashboard_M16_EEPS.G25()
        var_3 = IF(var_1, var_2, g25_2)
        return var_3

@register(Charts_Data_M16)
class H5():
    # 'Charts_Data_M16'!H5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!H25=0,NA(),'Dashboard M16 EEPS'!H25)"
    @eval_fn
    def H5():
        h25_1 = Dashboard_M16_EEPS.H25()
        var_1 = equal(h25_1, 0)
        var_2 = NA()
        h25_2 = Dashboard_M16_EEPS.H25()
        var_3 = IF(var_1, var_2, h25_2)
        return var_3

@register(Charts_Data_M16)
class I5():
    # 'Charts_Data_M16'!I5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!I25=0,NA(),'Dashboard M16 EEPS'!I25)"
    @eval_fn
    def I5():
        i25_1 = Dashboard_M16_EEPS.I25()
        var_1 = equal(i25_1, 0)
        var_2 = NA()
        i25_2 = Dashboard_M16_EEPS.I25()
        var_3 = IF(var_1, var_2, i25_2)
        return var_3

@register(Charts_Data_M16)
class J5():
    # 'Charts_Data_M16'!J5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!J25=0,NA(),'Dashboard M16 EEPS'!J25)"
    @eval_fn
    def J5():
        j25_1 = Dashboard_M16_EEPS.J25()
        var_1 = equal(j25_1, 0)
        var_2 = NA()
        j25_2 = Dashboard_M16_EEPS.J25()
        var_3 = IF(var_1, var_2, j25_2)
        return var_3

@register(Charts_Data_M16)
class K5():
    # 'Charts_Data_M16'!K5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!K25=0,NA(),'Dashboard M16 EEPS'!K25)"
    @eval_fn
    def K5():
        k25_1 = Dashboard_M16_EEPS.K25()
        var_1 = equal(k25_1, 0)
        var_2 = NA()
        k25_2 = Dashboard_M16_EEPS.K25()
        var_3 = IF(var_1, var_2, k25_2)
        return var_3

@register(Charts_Data_M16)
class L5():
    # 'Charts_Data_M16'!L5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!L25=0,NA(),'Dashboard M16 EEPS'!L25)"
    @eval_fn
    def L5():
        l25_1 = Dashboard_M16_EEPS.L25()
        var_1 = equal(l25_1, 0)
        var_2 = NA()
        l25_2 = Dashboard_M16_EEPS.L25()
        var_3 = IF(var_1, var_2, l25_2)
        return var_3

@register(Charts_Data_M16)
class M5():
    # 'Charts_Data_M16'!M5
    value = 77000
    formula = "=IF('Dashboard M16 EEPS'!M25=0,NA(),'Dashboard M16 EEPS'!M25)"
    @eval_fn
    def M5():
        m25_1 = Dashboard_M16_EEPS.M25()
        var_1 = equal(m25_1, 0)
        var_2 = NA()
        m25_2 = Dashboard_M16_EEPS.M25()
        var_3 = IF(var_1, var_2, m25_2)
        return var_3

@register(Charts_Data_M16)
class N5():
    # 'Charts_Data_M16'!N5
    value = 82000
    formula = "=IF('Dashboard M16 EEPS'!N25=0,NA(),'Dashboard M16 EEPS'!N25)"
    @eval_fn
    def N5():
        n25_1 = Dashboard_M16_EEPS.N25()
        var_1 = equal(n25_1, 0)
        var_2 = NA()
        n25_2 = Dashboard_M16_EEPS.N25()
        var_3 = IF(var_1, var_2, n25_2)
        return var_3

@register(Charts_Data_M16)
class O5():
    # 'Charts_Data_M16'!O5
    value = 88000
    formula = "=IF('Dashboard M16 EEPS'!O25=0,NA(),'Dashboard M16 EEPS'!O25)"
    @eval_fn
    def O5():
        o25_1 = Dashboard_M16_EEPS.O25()
        var_1 = equal(o25_1, 0)
        var_2 = NA()
        o25_2 = Dashboard_M16_EEPS.O25()
        var_3 = IF(var_1, var_2, o25_2)
        return var_3

@register(Charts_Data_M16)
class P5():
    # 'Charts_Data_M16'!P5
    value = 79835
    formula = "=IF('Dashboard M16 EEPS'!P25=0,NA(),'Dashboard M16 EEPS'!P25)"
    @eval_fn
    def P5():
        p25_1 = Dashboard_M16_EEPS.P25()
        var_1 = equal(p25_1, 0)
        var_2 = NA()
        p25_2 = Dashboard_M16_EEPS.P25()
        var_3 = IF(var_1, var_2, p25_2)
        return var_3

@register(Charts_Data_M16)
class Q5():
    # 'Charts_Data_M16'!Q5
    value = 88593
    formula = "=IF('Dashboard M16 EEPS'!Q25=0,NA(),'Dashboard M16 EEPS'!Q25)"
    @eval_fn
    def Q5():
        q25_1 = Dashboard_M16_EEPS.Q25()
        var_1 = equal(q25_1, 0)
        var_2 = NA()
        q25_2 = Dashboard_M16_EEPS.Q25()
        var_3 = IF(var_1, var_2, q25_2)
        return var_3

@register(Charts_Data_M16)
class R5():
    # 'Charts_Data_M16'!R5
    value = 98813
    formula = "=IF('Dashboard M16 EEPS'!R25=0,NA(),'Dashboard M16 EEPS'!R25)"
    @eval_fn
    def R5():
        r25_1 = Dashboard_M16_EEPS.R25()
        var_1 = equal(r25_1, 0)
        var_2 = NA()
        r25_2 = Dashboard_M16_EEPS.R25()
        var_3 = IF(var_1, var_2, r25_2)
        return var_3

@register(Charts_Data_M16)
class S5():
    # 'Charts_Data_M16'!S5
    value = 111306
    formula = "=IF('Dashboard M16 EEPS'!S25=0,NA(),'Dashboard M16 EEPS'!S25)"
    @eval_fn
    def S5():
        s25_1 = Dashboard_M16_EEPS.S25()
        var_1 = equal(s25_1, 0)
        var_2 = NA()
        s25_2 = Dashboard_M16_EEPS.S25()
        var_3 = IF(var_1, var_2, s25_2)
        return var_3

@register(Charts_Data_M16)
class T5():
    # 'Charts_Data_M16'!T5
    value = 129340
    formula = "=IF('Dashboard M16 EEPS'!T25=0,NA(),'Dashboard M16 EEPS'!T25)"
    @eval_fn
    def T5():
        t25_1 = Dashboard_M16_EEPS.T25()
        var_1 = equal(t25_1, 0)
        var_2 = NA()
        t25_2 = Dashboard_M16_EEPS.T25()
        var_3 = IF(var_1, var_2, t25_2)
        return var_3

@register(Charts_Data_M16)
class U5():
    # 'Charts_Data_M16'!U5
    value = 144281
    formula = "=IF('Dashboard M16 EEPS'!U25=0,NA(),'Dashboard M16 EEPS'!U25)"
    @eval_fn
    def U5():
        u25_1 = Dashboard_M16_EEPS.U25()
        var_1 = equal(u25_1, 0)
        var_2 = NA()
        u25_2 = Dashboard_M16_EEPS.U25()
        var_3 = IF(var_1, var_2, u25_2)
        return var_3

@register(Charts_Data_M16)
class V5():
    # 'Charts_Data_M16'!V5
    value = 154216
    formula = "=IF('Dashboard M16 EEPS'!V25=0,NA(),'Dashboard M16 EEPS'!V25)"
    @eval_fn
    def V5():
        v25_1 = Dashboard_M16_EEPS.V25()
        var_1 = equal(v25_1, 0)
        var_2 = NA()
        v25_2 = Dashboard_M16_EEPS.V25()
        var_3 = IF(var_1, var_2, v25_2)
        return var_3

@register(Charts_Data_M16)
class W5():
    # 'Charts_Data_M16'!W5
    value = 164151
    formula = "=IF('Dashboard M16 EEPS'!W25=0,NA(),'Dashboard M16 EEPS'!W25)"
    @eval_fn
    def W5():
        w25_1 = Dashboard_M16_EEPS.W25()
        var_1 = equal(w25_1, 0)
        var_2 = NA()
        w25_2 = Dashboard_M16_EEPS.W25()
        var_3 = IF(var_1, var_2, w25_2)
        return var_3

@register(Charts_Data_M16)
class X5():
    # 'Charts_Data_M16'!X5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!X25=0,NA(),'Dashboard M16 EEPS'!X25)"
    @eval_fn
    def X5():
        x25_1 = Dashboard_M16_EEPS.X25()
        var_1 = equal(x25_1, 0)
        var_2 = NA()
        x25_2 = Dashboard_M16_EEPS.X25()
        var_3 = IF(var_1, var_2, x25_2)
        return var_3

@register(Charts_Data_M16)
class Y5():
    # 'Charts_Data_M16'!Y5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!Y25=0,NA(),'Dashboard M16 EEPS'!Y25)"
    @eval_fn
    def Y5():
        y25_1 = Dashboard_M16_EEPS.Y25()
        var_1 = equal(y25_1, 0)
        var_2 = NA()
        y25_2 = Dashboard_M16_EEPS.Y25()
        var_3 = IF(var_1, var_2, y25_2)
        return var_3

@register(Charts_Data_M16)
class Z5():
    # 'Charts_Data_M16'!Z5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!Z25=0,NA(),'Dashboard M16 EEPS'!Z25)"
    @eval_fn
    def Z5():
        z25_1 = Dashboard_M16_EEPS.Z25()
        var_1 = equal(z25_1, 0)
        var_2 = NA()
        z25_2 = Dashboard_M16_EEPS.Z25()
        var_3 = IF(var_1, var_2, z25_2)
        return var_3

@register(Charts_Data_M16)
class AA5():
    # 'Charts_Data_M16'!AA5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AA25=0,NA(),'Dashboard M16 EEPS'!AA25)"
    @eval_fn
    def AA5():
        aa25_1 = Dashboard_M16_EEPS.AA25()
        var_1 = equal(aa25_1, 0)
        var_2 = NA()
        aa25_2 = Dashboard_M16_EEPS.AA25()
        var_3 = IF(var_1, var_2, aa25_2)
        return var_3

@register(Charts_Data_M16)
class AB5():
    # 'Charts_Data_M16'!AB5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AB25=0,NA(),'Dashboard M16 EEPS'!AB25)"
    @eval_fn
    def AB5():
        ab25_1 = Dashboard_M16_EEPS.AB25()
        var_1 = equal(ab25_1, 0)
        var_2 = NA()
        ab25_2 = Dashboard_M16_EEPS.AB25()
        var_3 = IF(var_1, var_2, ab25_2)
        return var_3

@register(Charts_Data_M16)
class AC5():
    # 'Charts_Data_M16'!AC5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AC25=0,NA(),'Dashboard M16 EEPS'!AC25)"
    @eval_fn
    def AC5():
        ac25_1 = Dashboard_M16_EEPS.AC25()
        var_1 = equal(ac25_1, 0)
        var_2 = NA()
        ac25_2 = Dashboard_M16_EEPS.AC25()
        var_3 = IF(var_1, var_2, ac25_2)
        return var_3

@register(Charts_Data_M16)
class AD5():
    # 'Charts_Data_M16'!AD5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AD25=0,NA(),'Dashboard M16 EEPS'!AD25)"
    @eval_fn
    def AD5():
        ad25_1 = Dashboard_M16_EEPS.AD25()
        var_1 = equal(ad25_1, 0)
        var_2 = NA()
        ad25_2 = Dashboard_M16_EEPS.AD25()
        var_3 = IF(var_1, var_2, ad25_2)
        return var_3

@register(Charts_Data_M16)
class AE5():
    # 'Charts_Data_M16'!AE5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AE25=0,NA(),'Dashboard M16 EEPS'!AE25)"
    @eval_fn
    def AE5():
        ae25_1 = Dashboard_M16_EEPS.AE25()
        var_1 = equal(ae25_1, 0)
        var_2 = NA()
        ae25_2 = Dashboard_M16_EEPS.AE25()
        var_3 = IF(var_1, var_2, ae25_2)
        return var_3

@register(Charts_Data_M16)
class AF5():
    # 'Charts_Data_M16'!AF5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AF25=0,NA(),'Dashboard M16 EEPS'!AF25)"
    @eval_fn
    def AF5():
        af25_1 = Dashboard_M16_EEPS.AF25()
        var_1 = equal(af25_1, 0)
        var_2 = NA()
        af25_2 = Dashboard_M16_EEPS.AF25()
        var_3 = IF(var_1, var_2, af25_2)
        return var_3

@register(Charts_Data_M16)
class AG5():
    # 'Charts_Data_M16'!AG5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AG25=0,NA(),'Dashboard M16 EEPS'!AG25)"
    @eval_fn
    def AG5():
        ag25_1 = Dashboard_M16_EEPS.AG25()
        var_1 = equal(ag25_1, 0)
        var_2 = NA()
        ag25_2 = Dashboard_M16_EEPS.AG25()
        var_3 = IF(var_1, var_2, ag25_2)
        return var_3

@register(Charts_Data_M16)
class AH5():
    # 'Charts_Data_M16'!AH5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AH25=0,NA(),'Dashboard M16 EEPS'!AH25)"
    @eval_fn
    def AH5():
        ah25_1 = Dashboard_M16_EEPS.AH25()
        var_1 = equal(ah25_1, 0)
        var_2 = NA()
        ah25_2 = Dashboard_M16_EEPS.AH25()
        var_3 = IF(var_1, var_2, ah25_2)
        return var_3

@register(Charts_Data_M16)
class AI5():
    # 'Charts_Data_M16'!AI5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AI25=0,NA(),'Dashboard M16 EEPS'!AI25)"
    @eval_fn
    def AI5():
        ai25_1 = Dashboard_M16_EEPS.AI25()
        var_1 = equal(ai25_1, 0)
        var_2 = NA()
        ai25_2 = Dashboard_M16_EEPS.AI25()
        var_3 = IF(var_1, var_2, ai25_2)
        return var_3

@register(Charts_Data_M16)
class AJ5():
    # 'Charts_Data_M16'!AJ5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AJ25=0,NA(),'Dashboard M16 EEPS'!AJ25)"
    @eval_fn
    def AJ5():
        aj25_1 = Dashboard_M16_EEPS.AJ25()
        var_1 = equal(aj25_1, 0)
        var_2 = NA()
        aj25_2 = Dashboard_M16_EEPS.AJ25()
        var_3 = IF(var_1, var_2, aj25_2)
        return var_3

@register(Charts_Data_M16)
class AK5():
    # 'Charts_Data_M16'!AK5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AK25=0,NA(),'Dashboard M16 EEPS'!AK25)"
    @eval_fn
    def AK5():
        ak25_1 = Dashboard_M16_EEPS.AK25()
        var_1 = equal(ak25_1, 0)
        var_2 = NA()
        ak25_2 = Dashboard_M16_EEPS.AK25()
        var_3 = IF(var_1, var_2, ak25_2)
        return var_3

@register(Charts_Data_M16)
class AL5():
    # 'Charts_Data_M16'!AL5
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AL25=0,NA(),'Dashboard M16 EEPS'!AL25)"
    @eval_fn
    def AL5():
        al25_1 = Dashboard_M16_EEPS.AL25()
        var_1 = equal(al25_1, 0)
        var_2 = NA()
        al25_2 = Dashboard_M16_EEPS.AL25()
        var_3 = IF(var_1, var_2, al25_2)
        return var_3

@register(Charts_Data_M16)
class C6():
    # 'Charts_Data_M16'!C6
    value = "#N/A"
    formula = '''=D6&VLOOKUP('Charts M16'!$B$2,'Charts Interactive LookupTables'!$W:$AA,5,FALSE)&"Total EE"'''
    @eval_fn
    def C6():
        d6_1 = Charts_Data_M16.D6()
        b2_1 = Charts_M16.B2()
        range_1 = Charts_Interactive_LookupTables(23, 0, 27, 0)
        var_1 = VLOOKUP(b2_1, range_1, 5, "FALSE")
        var_2 = concat(d6_1, var_1)
        var_3 = concat(var_2, "Total EE")
        return var_3

@register(Charts_Data_M16)
class D6():
    # 'Charts_Data_M16'!D6
    value = "KIUC"

@register(Charts_Data_M16)
class F6():
    # 'Charts_Data_M16'!F6
    value = "Notes"

@register(Charts_Data_M16)
class G6():
    # 'Charts_Data_M16'!G6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!G29=0,NA(),'Dashboard M16 EEPS'!G29)"
    @eval_fn
    def G6():
        g29_1 = Dashboard_M16_EEPS.G29()
        var_1 = equal(g29_1, 0)
        var_2 = NA()
        g29_2 = Dashboard_M16_EEPS.G29()
        var_3 = IF(var_1, var_2, g29_2)
        return var_3

@register(Charts_Data_M16)
class H6():
    # 'Charts_Data_M16'!H6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!H29=0,NA(),'Dashboard M16 EEPS'!H29)"
    @eval_fn
    def H6():
        h29_1 = Dashboard_M16_EEPS.H29()
        var_1 = equal(h29_1, 0)
        var_2 = NA()
        h29_2 = Dashboard_M16_EEPS.H29()
        var_3 = IF(var_1, var_2, h29_2)
        return var_3

@register(Charts_Data_M16)
class I6():
    # 'Charts_Data_M16'!I6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!I29=0,NA(),'Dashboard M16 EEPS'!I29)"
    @eval_fn
    def I6():
        i29_1 = Dashboard_M16_EEPS.I29()
        var_1 = equal(i29_1, 0)
        var_2 = NA()
        i29_2 = Dashboard_M16_EEPS.I29()
        var_3 = IF(var_1, var_2, i29_2)
        return var_3

@register(Charts_Data_M16)
class J6():
    # 'Charts_Data_M16'!J6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!J29=0,NA(),'Dashboard M16 EEPS'!J29)"
    @eval_fn
    def J6():
        j29_1 = Dashboard_M16_EEPS.J29()
        var_1 = equal(j29_1, 0)
        var_2 = NA()
        j29_2 = Dashboard_M16_EEPS.J29()
        var_3 = IF(var_1, var_2, j29_2)
        return var_3

@register(Charts_Data_M16)
class K6():
    # 'Charts_Data_M16'!K6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!K29=0,NA(),'Dashboard M16 EEPS'!K29)"
    @eval_fn
    def K6():
        k29_1 = Dashboard_M16_EEPS.K29()
        var_1 = equal(k29_1, 0)
        var_2 = NA()
        k29_2 = Dashboard_M16_EEPS.K29()
        var_3 = IF(var_1, var_2, k29_2)
        return var_3

@register(Charts_Data_M16)
class L6():
    # 'Charts_Data_M16'!L6
    value = 19037
    formula = "=IF('Dashboard M16 EEPS'!L29=0,NA(),'Dashboard M16 EEPS'!L29)"
    @eval_fn
    def L6():
        l29_1 = Dashboard_M16_EEPS.L29()
        var_1 = equal(l29_1, 0)
        var_2 = NA()
        l29_2 = Dashboard_M16_EEPS.L29()
        var_3 = IF(var_1, var_2, l29_2)
        return var_3

@register(Charts_Data_M16)
class M6():
    # 'Charts_Data_M16'!M6
    value = 20855
    formula = "=IF('Dashboard M16 EEPS'!M29=0,NA(),'Dashboard M16 EEPS'!M29)"
    @eval_fn
    def M6():
        m29_1 = Dashboard_M16_EEPS.M29()
        var_1 = equal(m29_1, 0)
        var_2 = NA()
        m29_2 = Dashboard_M16_EEPS.M29()
        var_3 = IF(var_1, var_2, m29_2)
        return var_3

@register(Charts_Data_M16)
class N6():
    # 'Charts_Data_M16'!N6
    value = 21349
    formula = "=IF('Dashboard M16 EEPS'!N29=0,NA(),'Dashboard M16 EEPS'!N29)"
    @eval_fn
    def N6():
        n29_1 = Dashboard_M16_EEPS.N29()
        var_1 = equal(n29_1, 0)
        var_2 = NA()
        n29_2 = Dashboard_M16_EEPS.N29()
        var_3 = IF(var_1, var_2, n29_2)
        return var_3

@register(Charts_Data_M16)
class O6():
    # 'Charts_Data_M16'!O6
    value = 21361
    formula = "=IF('Dashboard M16 EEPS'!O29=0,NA(),'Dashboard M16 EEPS'!O29)"
    @eval_fn
    def O6():
        o29_1 = Dashboard_M16_EEPS.O29()
        var_1 = equal(o29_1, 0)
        var_2 = NA()
        o29_2 = Dashboard_M16_EEPS.O29()
        var_3 = IF(var_1, var_2, o29_2)
        return var_3

@register(Charts_Data_M16)
class P6():
    # 'Charts_Data_M16'!P6
    value = 19233
    formula = "=IF('Dashboard M16 EEPS'!P29=0,NA(),'Dashboard M16 EEPS'!P29)"
    @eval_fn
    def P6():
        p29_1 = Dashboard_M16_EEPS.P29()
        var_1 = equal(p29_1, 0)
        var_2 = NA()
        p29_2 = Dashboard_M16_EEPS.P29()
        var_3 = IF(var_1, var_2, p29_2)
        return var_3

@register(Charts_Data_M16)
class Q6():
    # 'Charts_Data_M16'!Q6
    value = 19217
    formula = "=IF('Dashboard M16 EEPS'!Q29=0,NA(),'Dashboard M16 EEPS'!Q29)"
    @eval_fn
    def Q6():
        q29_1 = Dashboard_M16_EEPS.Q29()
        var_1 = equal(q29_1, 0)
        var_2 = NA()
        q29_2 = Dashboard_M16_EEPS.Q29()
        var_3 = IF(var_1, var_2, q29_2)
        return var_3

@register(Charts_Data_M16)
class R6():
    # 'Charts_Data_M16'!R6
    value = 16911
    formula = "=IF('Dashboard M16 EEPS'!R29=0,NA(),'Dashboard M16 EEPS'!R29)"
    @eval_fn
    def R6():
        r29_1 = Dashboard_M16_EEPS.R29()
        var_1 = equal(r29_1, 0)
        var_2 = NA()
        r29_2 = Dashboard_M16_EEPS.R29()
        var_3 = IF(var_1, var_2, r29_2)
        return var_3

@register(Charts_Data_M16)
class S6():
    # 'Charts_Data_M16'!S6
    value = 18264
    formula = "=IF('Dashboard M16 EEPS'!S29=0,NA(),'Dashboard M16 EEPS'!S29)"
    @eval_fn
    def S6():
        s29_1 = Dashboard_M16_EEPS.S29()
        var_1 = equal(s29_1, 0)
        var_2 = NA()
        s29_2 = Dashboard_M16_EEPS.S29()
        var_3 = IF(var_1, var_2, s29_2)
        return var_3

@register(Charts_Data_M16)
class T6():
    # 'Charts_Data_M16'!T6
    value = 24368
    formula = "=IF('Dashboard M16 EEPS'!T29=0,NA(),'Dashboard M16 EEPS'!T29)"
    @eval_fn
    def T6():
        t29_1 = Dashboard_M16_EEPS.T29()
        var_1 = equal(t29_1, 0)
        var_2 = NA()
        t29_2 = Dashboard_M16_EEPS.T29()
        var_3 = IF(var_1, var_2, t29_2)
        return var_3

@register(Charts_Data_M16)
class U6():
    # 'Charts_Data_M16'!U6
    value = 22441
    formula = "=IF('Dashboard M16 EEPS'!U29=0,NA(),'Dashboard M16 EEPS'!U29)"
    @eval_fn
    def U6():
        u29_1 = Dashboard_M16_EEPS.U29()
        var_1 = equal(u29_1, 0)
        var_2 = NA()
        u29_2 = Dashboard_M16_EEPS.U29()
        var_3 = IF(var_1, var_2, u29_2)
        return var_3

@register(Charts_Data_M16)
class V6():
    # 'Charts_Data_M16'!V6
    value = 21370
    formula = "=IF('Dashboard M16 EEPS'!V29=0,NA(),'Dashboard M16 EEPS'!V29)"
    @eval_fn
    def V6():
        v29_1 = Dashboard_M16_EEPS.V29()
        var_1 = equal(v29_1, 0)
        var_2 = NA()
        v29_2 = Dashboard_M16_EEPS.V29()
        var_3 = IF(var_1, var_2, v29_2)
        return var_3

@register(Charts_Data_M16)
class W6():
    # 'Charts_Data_M16'!W6
    value = 19947
    formula = "=IF('Dashboard M16 EEPS'!W29=0,NA(),'Dashboard M16 EEPS'!W29)"
    @eval_fn
    def W6():
        w29_1 = Dashboard_M16_EEPS.W29()
        var_1 = equal(w29_1, 0)
        var_2 = NA()
        w29_2 = Dashboard_M16_EEPS.W29()
        var_3 = IF(var_1, var_2, w29_2)
        return var_3

@register(Charts_Data_M16)
class X6():
    # 'Charts_Data_M16'!X6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!X29=0,NA(),'Dashboard M16 EEPS'!X29)"
    @eval_fn
    def X6():
        x29_1 = Dashboard_M16_EEPS.X29()
        var_1 = equal(x29_1, 0)
        var_2 = NA()
        x29_2 = Dashboard_M16_EEPS.X29()
        var_3 = IF(var_1, var_2, x29_2)
        return var_3

@register(Charts_Data_M16)
class Y6():
    # 'Charts_Data_M16'!Y6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!Y29=0,NA(),'Dashboard M16 EEPS'!Y29)"
    @eval_fn
    def Y6():
        y29_1 = Dashboard_M16_EEPS.Y29()
        var_1 = equal(y29_1, 0)
        var_2 = NA()
        y29_2 = Dashboard_M16_EEPS.Y29()
        var_3 = IF(var_1, var_2, y29_2)
        return var_3

@register(Charts_Data_M16)
class Z6():
    # 'Charts_Data_M16'!Z6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!Z29=0,NA(),'Dashboard M16 EEPS'!Z29)"
    @eval_fn
    def Z6():
        z29_1 = Dashboard_M16_EEPS.Z29()
        var_1 = equal(z29_1, 0)
        var_2 = NA()
        z29_2 = Dashboard_M16_EEPS.Z29()
        var_3 = IF(var_1, var_2, z29_2)
        return var_3

@register(Charts_Data_M16)
class AA6():
    # 'Charts_Data_M16'!AA6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AA29=0,NA(),'Dashboard M16 EEPS'!AA29)"
    @eval_fn
    def AA6():
        aa29_1 = Dashboard_M16_EEPS.AA29()
        var_1 = equal(aa29_1, 0)
        var_2 = NA()
        aa29_2 = Dashboard_M16_EEPS.AA29()
        var_3 = IF(var_1, var_2, aa29_2)
        return var_3

@register(Charts_Data_M16)
class AB6():
    # 'Charts_Data_M16'!AB6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AB29=0,NA(),'Dashboard M16 EEPS'!AB29)"
    @eval_fn
    def AB6():
        ab29_1 = Dashboard_M16_EEPS.AB29()
        var_1 = equal(ab29_1, 0)
        var_2 = NA()
        ab29_2 = Dashboard_M16_EEPS.AB29()
        var_3 = IF(var_1, var_2, ab29_2)
        return var_3

@register(Charts_Data_M16)
class AC6():
    # 'Charts_Data_M16'!AC6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AC29=0,NA(),'Dashboard M16 EEPS'!AC29)"
    @eval_fn
    def AC6():
        ac29_1 = Dashboard_M16_EEPS.AC29()
        var_1 = equal(ac29_1, 0)
        var_2 = NA()
        ac29_2 = Dashboard_M16_EEPS.AC29()
        var_3 = IF(var_1, var_2, ac29_2)
        return var_3

@register(Charts_Data_M16)
class AD6():
    # 'Charts_Data_M16'!AD6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AD29=0,NA(),'Dashboard M16 EEPS'!AD29)"
    @eval_fn
    def AD6():
        ad29_1 = Dashboard_M16_EEPS.AD29()
        var_1 = equal(ad29_1, 0)
        var_2 = NA()
        ad29_2 = Dashboard_M16_EEPS.AD29()
        var_3 = IF(var_1, var_2, ad29_2)
        return var_3

@register(Charts_Data_M16)
class AE6():
    # 'Charts_Data_M16'!AE6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AE29=0,NA(),'Dashboard M16 EEPS'!AE29)"
    @eval_fn
    def AE6():
        ae29_1 = Dashboard_M16_EEPS.AE29()
        var_1 = equal(ae29_1, 0)
        var_2 = NA()
        ae29_2 = Dashboard_M16_EEPS.AE29()
        var_3 = IF(var_1, var_2, ae29_2)
        return var_3

@register(Charts_Data_M16)
class AF6():
    # 'Charts_Data_M16'!AF6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AF29=0,NA(),'Dashboard M16 EEPS'!AF29)"
    @eval_fn
    def AF6():
        af29_1 = Dashboard_M16_EEPS.AF29()
        var_1 = equal(af29_1, 0)
        var_2 = NA()
        af29_2 = Dashboard_M16_EEPS.AF29()
        var_3 = IF(var_1, var_2, af29_2)
        return var_3

@register(Charts_Data_M16)
class AG6():
    # 'Charts_Data_M16'!AG6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AG29=0,NA(),'Dashboard M16 EEPS'!AG29)"
    @eval_fn
    def AG6():
        ag29_1 = Dashboard_M16_EEPS.AG29()
        var_1 = equal(ag29_1, 0)
        var_2 = NA()
        ag29_2 = Dashboard_M16_EEPS.AG29()
        var_3 = IF(var_1, var_2, ag29_2)
        return var_3

@register(Charts_Data_M16)
class AH6():
    # 'Charts_Data_M16'!AH6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AH29=0,NA(),'Dashboard M16 EEPS'!AH29)"
    @eval_fn
    def AH6():
        ah29_1 = Dashboard_M16_EEPS.AH29()
        var_1 = equal(ah29_1, 0)
        var_2 = NA()
        ah29_2 = Dashboard_M16_EEPS.AH29()
        var_3 = IF(var_1, var_2, ah29_2)
        return var_3

@register(Charts_Data_M16)
class AI6():
    # 'Charts_Data_M16'!AI6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AI29=0,NA(),'Dashboard M16 EEPS'!AI29)"
    @eval_fn
    def AI6():
        ai29_1 = Dashboard_M16_EEPS.AI29()
        var_1 = equal(ai29_1, 0)
        var_2 = NA()
        ai29_2 = Dashboard_M16_EEPS.AI29()
        var_3 = IF(var_1, var_2, ai29_2)
        return var_3

@register(Charts_Data_M16)
class AJ6():
    # 'Charts_Data_M16'!AJ6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AJ29=0,NA(),'Dashboard M16 EEPS'!AJ29)"
    @eval_fn
    def AJ6():
        aj29_1 = Dashboard_M16_EEPS.AJ29()
        var_1 = equal(aj29_1, 0)
        var_2 = NA()
        aj29_2 = Dashboard_M16_EEPS.AJ29()
        var_3 = IF(var_1, var_2, aj29_2)
        return var_3

@register(Charts_Data_M16)
class AK6():
    # 'Charts_Data_M16'!AK6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AK29=0,NA(),'Dashboard M16 EEPS'!AK29)"
    @eval_fn
    def AK6():
        ak29_1 = Dashboard_M16_EEPS.AK29()
        var_1 = equal(ak29_1, 0)
        var_2 = NA()
        ak29_2 = Dashboard_M16_EEPS.AK29()
        var_3 = IF(var_1, var_2, ak29_2)
        return var_3

@register(Charts_Data_M16)
class AL6():
    # 'Charts_Data_M16'!AL6
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AL29=0,NA(),'Dashboard M16 EEPS'!AL29)"
    @eval_fn
    def AL6():
        al29_1 = Dashboard_M16_EEPS.AL29()
        var_1 = equal(al29_1, 0)
        var_2 = NA()
        al29_2 = Dashboard_M16_EEPS.AL29()
        var_3 = IF(var_1, var_2, al29_2)
        return var_3

@register(Charts_Data_M16)
class C7():
    # 'Charts_Data_M16'!C7
    value = "#N/A"
    formula = '''=D7&VLOOKUP('Charts M16'!$B$2,'Charts Interactive LookupTables'!$W:$AA,5,FALSE)&"Total EE"'''
    @eval_fn
    def C7():
        d7_1 = Charts_Data_M16.D7()
        b2_1 = Charts_M16.B2()
        range_1 = Charts_Interactive_LookupTables(23, 0, 27, 0)
        var_1 = VLOOKUP(b2_1, range_1, 5, "FALSE")
        var_2 = concat(d7_1, var_1)
        var_3 = concat(var_2, "Total EE")
        return var_3

@register(Charts_Data_M16)
class D7():
    # 'Charts_Data_M16'!D7
    value = "Total"

@register(Charts_Data_M16)
class F7():
    # 'Charts_Data_M16'!F7
    value = "Notes"

@register(Charts_Data_M16)
class G7():
    # 'Charts_Data_M16'!G7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!G33=0,NA(),'Dashboard M16 EEPS'!G33)"
    @eval_fn
    def G7():
        g33_1 = Dashboard_M16_EEPS.G33()
        var_1 = equal(g33_1, 0)
        var_2 = NA()
        g33_2 = Dashboard_M16_EEPS.G33()
        var_3 = IF(var_1, var_2, g33_2)
        return var_3

@register(Charts_Data_M16)
class H7():
    # 'Charts_Data_M16'!H7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!H33=0,NA(),'Dashboard M16 EEPS'!H33)"
    @eval_fn
    def H7():
        h33_1 = Dashboard_M16_EEPS.H33()
        var_1 = equal(h33_1, 0)
        var_2 = NA()
        h33_2 = Dashboard_M16_EEPS.H33()
        var_3 = IF(var_1, var_2, h33_2)
        return var_3

@register(Charts_Data_M16)
class I7():
    # 'Charts_Data_M16'!I7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!I33=0,NA(),'Dashboard M16 EEPS'!I33)"
    @eval_fn
    def I7():
        i33_1 = Dashboard_M16_EEPS.I33()
        var_1 = equal(i33_1, 0)
        var_2 = NA()
        i33_2 = Dashboard_M16_EEPS.I33()
        var_3 = IF(var_1, var_2, i33_2)
        return var_3

@register(Charts_Data_M16)
class J7():
    # 'Charts_Data_M16'!J7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!J33=0,NA(),'Dashboard M16 EEPS'!J33)"
    @eval_fn
    def J7():
        j33_1 = Dashboard_M16_EEPS.J33()
        var_1 = equal(j33_1, 0)
        var_2 = NA()
        j33_2 = Dashboard_M16_EEPS.J33()
        var_3 = IF(var_1, var_2, j33_2)
        return var_3

@register(Charts_Data_M16)
class K7():
    # 'Charts_Data_M16'!K7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!K33=0,NA(),'Dashboard M16 EEPS'!K33)"
    @eval_fn
    def K7():
        k33_1 = Dashboard_M16_EEPS.K33()
        var_1 = equal(k33_1, 0)
        var_2 = NA()
        k33_2 = Dashboard_M16_EEPS.K33()
        var_3 = IF(var_1, var_2, k33_2)
        return var_3

@register(Charts_Data_M16)
class L7():
    # 'Charts_Data_M16'!L7
    value = 19037
    formula = "=IF('Dashboard M16 EEPS'!L33=0,NA(),'Dashboard M16 EEPS'!L33)"
    @eval_fn
    def L7():
        l33_1 = Dashboard_M16_EEPS.L33()
        var_1 = equal(l33_1, 0)
        var_2 = NA()
        l33_2 = Dashboard_M16_EEPS.L33()
        var_3 = IF(var_1, var_2, l33_2)
        return var_3

@register(Charts_Data_M16)
class M7():
    # 'Charts_Data_M16'!M7
    value = 438855
    formula = "=IF('Dashboard M16 EEPS'!M33=0,NA(),'Dashboard M16 EEPS'!M33)"
    @eval_fn
    def M7():
        m33_1 = Dashboard_M16_EEPS.M33()
        var_1 = equal(m33_1, 0)
        var_2 = NA()
        m33_2 = Dashboard_M16_EEPS.M33()
        var_3 = IF(var_1, var_2, m33_2)
        return var_3

@register(Charts_Data_M16)
class N7():
    # 'Charts_Data_M16'!N7
    value = 497349
    formula = "=IF('Dashboard M16 EEPS'!N33=0,NA(),'Dashboard M16 EEPS'!N33)"
    @eval_fn
    def N7():
        n33_1 = Dashboard_M16_EEPS.N33()
        var_1 = equal(n33_1, 0)
        var_2 = NA()
        n33_2 = Dashboard_M16_EEPS.N33()
        var_3 = IF(var_1, var_2, n33_2)
        return var_3

@register(Charts_Data_M16)
class O7():
    # 'Charts_Data_M16'!O7
    value = 619361
    formula = "=IF('Dashboard M16 EEPS'!O33=0,NA(),'Dashboard M16 EEPS'!O33)"
    @eval_fn
    def O7():
        o33_1 = Dashboard_M16_EEPS.O33()
        var_1 = equal(o33_1, 0)
        var_2 = NA()
        o33_2 = Dashboard_M16_EEPS.O33()
        var_3 = IF(var_1, var_2, o33_2)
        return var_3

@register(Charts_Data_M16)
class P7():
    # 'Charts_Data_M16'!P7
    value = 750126
    formula = "=IF('Dashboard M16 EEPS'!P33=0,NA(),'Dashboard M16 EEPS'!P33)"
    @eval_fn
    def P7():
        p33_1 = Dashboard_M16_EEPS.P33()
        var_1 = equal(p33_1, 0)
        var_2 = NA()
        p33_2 = Dashboard_M16_EEPS.P33()
        var_3 = IF(var_1, var_2, p33_2)
        return var_3

@register(Charts_Data_M16)
class Q7():
    # 'Charts_Data_M16'!Q7
    value = 808848
    formula = "=IF('Dashboard M16 EEPS'!Q33=0,NA(),'Dashboard M16 EEPS'!Q33)"
    @eval_fn
    def Q7():
        q33_1 = Dashboard_M16_EEPS.Q33()
        var_1 = equal(q33_1, 0)
        var_2 = NA()
        q33_2 = Dashboard_M16_EEPS.Q33()
        var_3 = IF(var_1, var_2, q33_2)
        return var_3

@register(Charts_Data_M16)
class R7():
    # 'Charts_Data_M16'!R7
    value = 916420
    formula = "=IF('Dashboard M16 EEPS'!R33=0,NA(),'Dashboard M16 EEPS'!R33)"
    @eval_fn
    def R7():
        r33_1 = Dashboard_M16_EEPS.R33()
        var_1 = equal(r33_1, 0)
        var_2 = NA()
        r33_2 = Dashboard_M16_EEPS.R33()
        var_3 = IF(var_1, var_2, r33_2)
        return var_3

@register(Charts_Data_M16)
class S7():
    # 'Charts_Data_M16'!S7
    value = 1027328
    formula = "=IF('Dashboard M16 EEPS'!S33=0,NA(),'Dashboard M16 EEPS'!S33)"
    @eval_fn
    def S7():
        s33_1 = Dashboard_M16_EEPS.S33()
        var_1 = equal(s33_1, 0)
        var_2 = NA()
        s33_2 = Dashboard_M16_EEPS.S33()
        var_3 = IF(var_1, var_2, s33_2)
        return var_3

@register(Charts_Data_M16)
class T7():
    # 'Charts_Data_M16'!T7
    value = 1209628
    formula = "=IF('Dashboard M16 EEPS'!T33=0,NA(),'Dashboard M16 EEPS'!T33)"
    @eval_fn
    def T7():
        t33_1 = Dashboard_M16_EEPS.T33()
        var_1 = equal(t33_1, 0)
        var_2 = NA()
        t33_2 = Dashboard_M16_EEPS.T33()
        var_3 = IF(var_1, var_2, t33_2)
        return var_3

@register(Charts_Data_M16)
class U7():
    # 'Charts_Data_M16'!U7
    value = 1320005
    formula = "=IF('Dashboard M16 EEPS'!U33=0,NA(),'Dashboard M16 EEPS'!U33)"
    @eval_fn
    def U7():
        u33_1 = Dashboard_M16_EEPS.U33()
        var_1 = equal(u33_1, 0)
        var_2 = NA()
        u33_2 = Dashboard_M16_EEPS.U33()
        var_3 = IF(var_1, var_2, u33_2)
        return var_3

@register(Charts_Data_M16)
class V7():
    # 'Charts_Data_M16'!V7
    value = 1415773
    formula = "=IF('Dashboard M16 EEPS'!V33=0,NA(),'Dashboard M16 EEPS'!V33)"
    @eval_fn
    def V7():
        v33_1 = Dashboard_M16_EEPS.V33()
        var_1 = equal(v33_1, 0)
        var_2 = NA()
        v33_2 = Dashboard_M16_EEPS.V33()
        var_3 = IF(var_1, var_2, v33_2)
        return var_3

@register(Charts_Data_M16)
class W7():
    # 'Charts_Data_M16'!W7
    value = 1511189
    formula = "=IF('Dashboard M16 EEPS'!W33=0,NA(),'Dashboard M16 EEPS'!W33)"
    @eval_fn
    def W7():
        w33_1 = Dashboard_M16_EEPS.W33()
        var_1 = equal(w33_1, 0)
        var_2 = NA()
        w33_2 = Dashboard_M16_EEPS.W33()
        var_3 = IF(var_1, var_2, w33_2)
        return var_3

@register(Charts_Data_M16)
class X7():
    # 'Charts_Data_M16'!X7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!X33=0,NA(),'Dashboard M16 EEPS'!X33)"
    @eval_fn
    def X7():
        x33_1 = Dashboard_M16_EEPS.X33()
        var_1 = equal(x33_1, 0)
        var_2 = NA()
        x33_2 = Dashboard_M16_EEPS.X33()
        var_3 = IF(var_1, var_2, x33_2)
        return var_3

@register(Charts_Data_M16)
class Y7():
    # 'Charts_Data_M16'!Y7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!Y33=0,NA(),'Dashboard M16 EEPS'!Y33)"
    @eval_fn
    def Y7():
        y33_1 = Dashboard_M16_EEPS.Y33()
        var_1 = equal(y33_1, 0)
        var_2 = NA()
        y33_2 = Dashboard_M16_EEPS.Y33()
        var_3 = IF(var_1, var_2, y33_2)
        return var_3

@register(Charts_Data_M16)
class Z7():
    # 'Charts_Data_M16'!Z7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!Z33=0,NA(),'Dashboard M16 EEPS'!Z33)"
    @eval_fn
    def Z7():
        z33_1 = Dashboard_M16_EEPS.Z33()
        var_1 = equal(z33_1, 0)
        var_2 = NA()
        z33_2 = Dashboard_M16_EEPS.Z33()
        var_3 = IF(var_1, var_2, z33_2)
        return var_3

@register(Charts_Data_M16)
class AA7():
    # 'Charts_Data_M16'!AA7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AA33=0,NA(),'Dashboard M16 EEPS'!AA33)"
    @eval_fn
    def AA7():
        aa33_1 = Dashboard_M16_EEPS.AA33()
        var_1 = equal(aa33_1, 0)
        var_2 = NA()
        aa33_2 = Dashboard_M16_EEPS.AA33()
        var_3 = IF(var_1, var_2, aa33_2)
        return var_3

@register(Charts_Data_M16)
class AB7():
    # 'Charts_Data_M16'!AB7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AB33=0,NA(),'Dashboard M16 EEPS'!AB33)"
    @eval_fn
    def AB7():
        ab33_1 = Dashboard_M16_EEPS.AB33()
        var_1 = equal(ab33_1, 0)
        var_2 = NA()
        ab33_2 = Dashboard_M16_EEPS.AB33()
        var_3 = IF(var_1, var_2, ab33_2)
        return var_3

@register(Charts_Data_M16)
class AC7():
    # 'Charts_Data_M16'!AC7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AC33=0,NA(),'Dashboard M16 EEPS'!AC33)"
    @eval_fn
    def AC7():
        ac33_1 = Dashboard_M16_EEPS.AC33()
        var_1 = equal(ac33_1, 0)
        var_2 = NA()
        ac33_2 = Dashboard_M16_EEPS.AC33()
        var_3 = IF(var_1, var_2, ac33_2)
        return var_3

@register(Charts_Data_M16)
class AD7():
    # 'Charts_Data_M16'!AD7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AD33=0,NA(),'Dashboard M16 EEPS'!AD33)"
    @eval_fn
    def AD7():
        ad33_1 = Dashboard_M16_EEPS.AD33()
        var_1 = equal(ad33_1, 0)
        var_2 = NA()
        ad33_2 = Dashboard_M16_EEPS.AD33()
        var_3 = IF(var_1, var_2, ad33_2)
        return var_3

@register(Charts_Data_M16)
class AE7():
    # 'Charts_Data_M16'!AE7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AE33=0,NA(),'Dashboard M16 EEPS'!AE33)"
    @eval_fn
    def AE7():
        ae33_1 = Dashboard_M16_EEPS.AE33()
        var_1 = equal(ae33_1, 0)
        var_2 = NA()
        ae33_2 = Dashboard_M16_EEPS.AE33()
        var_3 = IF(var_1, var_2, ae33_2)
        return var_3

@register(Charts_Data_M16)
class AF7():
    # 'Charts_Data_M16'!AF7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AF33=0,NA(),'Dashboard M16 EEPS'!AF33)"
    @eval_fn
    def AF7():
        af33_1 = Dashboard_M16_EEPS.AF33()
        var_1 = equal(af33_1, 0)
        var_2 = NA()
        af33_2 = Dashboard_M16_EEPS.AF33()
        var_3 = IF(var_1, var_2, af33_2)
        return var_3

@register(Charts_Data_M16)
class AG7():
    # 'Charts_Data_M16'!AG7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AG33=0,NA(),'Dashboard M16 EEPS'!AG33)"
    @eval_fn
    def AG7():
        ag33_1 = Dashboard_M16_EEPS.AG33()
        var_1 = equal(ag33_1, 0)
        var_2 = NA()
        ag33_2 = Dashboard_M16_EEPS.AG33()
        var_3 = IF(var_1, var_2, ag33_2)
        return var_3

@register(Charts_Data_M16)
class AH7():
    # 'Charts_Data_M16'!AH7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AH33=0,NA(),'Dashboard M16 EEPS'!AH33)"
    @eval_fn
    def AH7():
        ah33_1 = Dashboard_M16_EEPS.AH33()
        var_1 = equal(ah33_1, 0)
        var_2 = NA()
        ah33_2 = Dashboard_M16_EEPS.AH33()
        var_3 = IF(var_1, var_2, ah33_2)
        return var_3

@register(Charts_Data_M16)
class AI7():
    # 'Charts_Data_M16'!AI7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AI33=0,NA(),'Dashboard M16 EEPS'!AI33)"
    @eval_fn
    def AI7():
        ai33_1 = Dashboard_M16_EEPS.AI33()
        var_1 = equal(ai33_1, 0)
        var_2 = NA()
        ai33_2 = Dashboard_M16_EEPS.AI33()
        var_3 = IF(var_1, var_2, ai33_2)
        return var_3

@register(Charts_Data_M16)
class AJ7():
    # 'Charts_Data_M16'!AJ7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AJ33=0,NA(),'Dashboard M16 EEPS'!AJ33)"
    @eval_fn
    def AJ7():
        aj33_1 = Dashboard_M16_EEPS.AJ33()
        var_1 = equal(aj33_1, 0)
        var_2 = NA()
        aj33_2 = Dashboard_M16_EEPS.AJ33()
        var_3 = IF(var_1, var_2, aj33_2)
        return var_3

@register(Charts_Data_M16)
class AK7():
    # 'Charts_Data_M16'!AK7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AK33=0,NA(),'Dashboard M16 EEPS'!AK33)"
    @eval_fn
    def AK7():
        ak33_1 = Dashboard_M16_EEPS.AK33()
        var_1 = equal(ak33_1, 0)
        var_2 = NA()
        ak33_2 = Dashboard_M16_EEPS.AK33()
        var_3 = IF(var_1, var_2, ak33_2)
        return var_3

@register(Charts_Data_M16)
class AL7():
    # 'Charts_Data_M16'!AL7
    value = "#N/A"
    formula = "=IF('Dashboard M16 EEPS'!AL33=0,NA(),'Dashboard M16 EEPS'!AL33)"
    @eval_fn
    def AL7():
        al33_1 = Dashboard_M16_EEPS.AL33()
        var_1 = equal(al33_1, 0)
        var_2 = NA()
        al33_2 = Dashboard_M16_EEPS.AL33()
        var_3 = IF(var_1, var_2, al33_2)
        return var_3

@register(Charts_Data_M16)
class A8():
    # 'Charts_Data_M16'!A8
    value = "Bar Chart input/ Pie Graph Input"

@register(Charts_Data_M16)
class F8():
    # 'Charts_Data_M16'!F8
    value = "Notes"

@register(Charts_Data_M16)
class B9():
    # 'Charts_Data_M16'!B9
    value = "Year"

@register(Charts_Data_M16)
class C9():
    # 'Charts_Data_M16'!C9
    value = 2009
    formula = "=VLOOKUP('Charts M16'!B28,'Charts Interactive LookupTables'!$W:$AA,4,FALSE)"
    @eval_fn
    def C9():
        b28_1 = Charts_M16.B28()
        range_1 = Charts_Interactive_LookupTables(23, 0, 27, 0)
        var_1 = VLOOKUP(b28_1, range_1, 4, "FALSE")
        return var_1

@register(Charts_Data_M16)
class F9():
    # 'Charts_Data_M16'!F9
    value = "Notes"

@register(Charts_Data_M16)
class G9():
    # 'Charts_Data_M16'!G9
    value = "Energy Efficiency"

@register(Charts_Data_M16)
class H9():
    # 'Charts_Data_M16'!H9
    value = "Total Electricity Sales"

@register(Charts_Data_M16)
class B10():
    # 'Charts_Data_M16'!B10
    value = "Total EE"

@register(Charts_Data_M16)
class C10():
    # 'Charts_Data_M16'!C10
    value = "Total EEHECO"
    formula = "=$B$10&D10"
    @eval_fn
    def C10():
        b10_1 = Charts_Data_M16.B10()
        d10_1 = Charts_Data_M16.D10()
        var_1 = concat(b10_1, d10_1)
        return var_1

@register(Charts_Data_M16)
class D10():
    # 'Charts_Data_M16'!D10
    value = "HECO"

@register(Charts_Data_M16)
class F10():
    # 'Charts_Data_M16'!F10
    value = "Notes"

@register(Charts_Data_M16)
class G10():
    # 'Charts_Data_M16'!G10
    value = 738245
    formula = "=INDEX('Dashboard M16 EEPS'!$A$15:$T$35,MATCH($C10,'Dashboard M16 EEPS'!$A$15:$A$35,0),MATCH($C$9,'Dashboard M16 EEPS'!$A$5:$T$5,0))"
    @eval_fn
    def G10():
        range_1 = Dashboard_M16_EEPS(1, 15, 20, 35)
        c10_1 = Charts_Data_M16.C10()
        range_2 = Dashboard_M16_EEPS(1, 15, 1, 35)
        var_1 = MATCH(c10_1, range_2, 0)
        c9_1 = Charts_Data_M16.C9()
        range_3 = Dashboard_M16_EEPS(1, 5, 20, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M16)
class H10():
    # 'Charts_Data_M16'!H10
    value = 7377537
    formula = "=INDEX('Dashboard M16 EEPS'!$A$7:$T$11,MATCH($D$10,'Dashboard M16 EEPS'!$C$7:$C$11,0),MATCH($C$9,'Dashboard M16 EEPS'!$A$5:$T$5,0))"
    @eval_fn
    def H10():
        range_1 = Dashboard_M16_EEPS(1, 7, 20, 11)
        d10_1 = Charts_Data_M16.D10()
        range_2 = Dashboard_M16_EEPS(3, 7, 3, 11)
        var_1 = MATCH(d10_1, range_2, 0)
        c9_1 = Charts_Data_M16.C9()
        range_3 = Dashboard_M16_EEPS(1, 5, 20, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M16)
class C11():
    # 'Charts_Data_M16'!C11
    value = "Total EEHELCO"
    formula = "=$B$10&D11"
    @eval_fn
    def C11():
        b10_1 = Charts_Data_M16.B10()
        d11_1 = Charts_Data_M16.D11()
        var_1 = concat(b10_1, d11_1)
        return var_1

@register(Charts_Data_M16)
class D11():
    # 'Charts_Data_M16'!D11
    value = "HELCO"

@register(Charts_Data_M16)
class F11():
    # 'Charts_Data_M16'!F11
    value = "Notes"

@register(Charts_Data_M16)
class G11():
    # 'Charts_Data_M16'!G11
    value = 64261
    formula = "=INDEX('Dashboard M16 EEPS'!$A$15:$T$35,MATCH($C11,'Dashboard M16 EEPS'!$A$15:$A$35,0),MATCH($C$9,'Dashboard M16 EEPS'!$A$5:$T$5,0))"
    @eval_fn
    def G11():
        range_1 = Dashboard_M16_EEPS(1, 15, 20, 35)
        c11_1 = Charts_Data_M16.C11()
        range_2 = Dashboard_M16_EEPS(1, 15, 1, 35)
        var_1 = MATCH(c11_1, range_2, 0)
        c9_1 = Charts_Data_M16.C9()
        range_3 = Dashboard_M16_EEPS(1, 5, 20, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M16)
class H11():
    # 'Charts_Data_M16'!H11
    value = 1119881
    formula = "=INDEX('Dashboard M16 EEPS'!$A$7:$T$11,MATCH($D$11,'Dashboard M16 EEPS'!$C$7:$C$11,0),MATCH($C$9,'Dashboard M16 EEPS'!$A$5:$T$5,0))"
    @eval_fn
    def H11():
        range_1 = Dashboard_M16_EEPS(1, 7, 20, 11)
        d11_1 = Charts_Data_M16.D11()
        range_2 = Dashboard_M16_EEPS(3, 7, 3, 11)
        var_1 = MATCH(d11_1, range_2, 0)
        c9_1 = Charts_Data_M16.C9()
        range_3 = Dashboard_M16_EEPS(1, 5, 20, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M16)
class C12():
    # 'Charts_Data_M16'!C12
    value = "Total EEMECO"
    formula = "=$B$10&D12"
    @eval_fn
    def C12():
        b10_1 = Charts_Data_M16.B10()
        d12_1 = Charts_Data_M16.D12()
        var_1 = concat(b10_1, d12_1)
        return var_1

@register(Charts_Data_M16)
class D12():
    # 'Charts_Data_M16'!D12
    value = "MECO"

@register(Charts_Data_M16)
class F12():
    # 'Charts_Data_M16'!F12
    value = "Notes"

@register(Charts_Data_M16)
class G12():
    # 'Charts_Data_M16'!G12
    value = 117085
    formula = "=INDEX('Dashboard M16 EEPS'!$A$15:$T$35,MATCH($C12,'Dashboard M16 EEPS'!$A$15:$A$35,0),MATCH($C$9,'Dashboard M16 EEPS'!$A$5:$T$5,0))"
    @eval_fn
    def G12():
        range_1 = Dashboard_M16_EEPS(1, 15, 20, 35)
        c12_1 = Charts_Data_M16.C12()
        range_2 = Dashboard_M16_EEPS(1, 15, 1, 35)
        var_1 = MATCH(c12_1, range_2, 0)
        c9_1 = Charts_Data_M16.C9()
        range_3 = Dashboard_M16_EEPS(1, 5, 20, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M16)
class H12():
    # 'Charts_Data_M16'!H12
    value = 1192243
    formula = "=INDEX('Dashboard M16 EEPS'!$A$7:$T$11,MATCH($D$12,'Dashboard M16 EEPS'!$C$7:$C$11,0),MATCH($C$9,'Dashboard M16 EEPS'!$A$5:$T$5,0))"
    @eval_fn
    def H12():
        range_1 = Dashboard_M16_EEPS(1, 7, 20, 11)
        d12_1 = Charts_Data_M16.D12()
        range_2 = Dashboard_M16_EEPS(3, 7, 3, 11)
        var_1 = MATCH(d12_1, range_2, 0)
        c9_1 = Charts_Data_M16.C9()
        range_3 = Dashboard_M16_EEPS(1, 5, 20, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M16)
class C13():
    # 'Charts_Data_M16'!C13
    value = "Total EEKIUC"
    formula = "=$B$10&D13"
    @eval_fn
    def C13():
        b10_1 = Charts_Data_M16.B10()
        d13_1 = Charts_Data_M16.D13()
        var_1 = concat(b10_1, d13_1)
        return var_1

@register(Charts_Data_M16)
class D13():
    # 'Charts_Data_M16'!D13
    value = "KIUC"

@register(Charts_Data_M16)
class F13():
    # 'Charts_Data_M16'!F13
    value = "Notes"

@register(Charts_Data_M16)
class G13():
    # 'Charts_Data_M16'!G13
    value = 19217
    formula = "=INDEX('Dashboard M16 EEPS'!$A$15:$T$35,MATCH($C13,'Dashboard M16 EEPS'!$A$15:$A$35,0),MATCH($C$9,'Dashboard M16 EEPS'!$A$5:$T$5,0))"
    @eval_fn
    def G13():
        range_1 = Dashboard_M16_EEPS(1, 15, 20, 35)
        c13_1 = Charts_Data_M16.C13()
        range_2 = Dashboard_M16_EEPS(1, 15, 1, 35)
        var_1 = MATCH(c13_1, range_2, 0)
        c9_1 = Charts_Data_M16.C9()
        range_3 = Dashboard_M16_EEPS(1, 5, 20, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M16)
class H13():
    # 'Charts_Data_M16'!H13
    value = 460513
    formula = "=INDEX('Dashboard M16 EEPS'!$A$7:$T$11,MATCH($D$13,'Dashboard M16 EEPS'!$C$7:$C$11,0),MATCH($C$9,'Dashboard M16 EEPS'!$A$5:$T$5,0))"
    @eval_fn
    def H13():
        range_1 = Dashboard_M16_EEPS(1, 7, 20, 11)
        d13_1 = Charts_Data_M16.D13()
        range_2 = Dashboard_M16_EEPS(3, 7, 3, 11)
        var_1 = MATCH(d13_1, range_2, 0)
        c9_1 = Charts_Data_M16.C9()
        range_3 = Dashboard_M16_EEPS(1, 5, 20, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M16)
class C14():
    # 'Charts_Data_M16'!C14
    value = "Total EETotal"
    formula = "=$B$10&D14"
    @eval_fn
    def C14():
        b10_1 = Charts_Data_M16.B10()
        d14_1 = Charts_Data_M16.D14()
        var_1 = concat(b10_1, d14_1)
        return var_1

@register(Charts_Data_M16)
class D14():
    # 'Charts_Data_M16'!D14
    value = "Total"

@register(Charts_Data_M16)
class F14():
    # 'Charts_Data_M16'!F14
    value = "Notes"

@register(Charts_Data_M16)
class G14():
    # 'Charts_Data_M16'!G14
    value = 938808
    formula = "=INDEX('Dashboard M16 EEPS'!$A$15:$T$35,MATCH($C14,'Dashboard M16 EEPS'!$A$15:$A$35,0),MATCH($C$9,'Dashboard M16 EEPS'!$A$5:$T$5,0))"
    @eval_fn
    def G14():
        range_1 = Dashboard_M16_EEPS(1, 15, 20, 35)
        c14_1 = Charts_Data_M16.C14()
        range_2 = Dashboard_M16_EEPS(1, 15, 1, 35)
        var_1 = MATCH(c14_1, range_2, 0)
        c9_1 = Charts_Data_M16.C9()
        range_3 = Dashboard_M16_EEPS(1, 5, 20, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M16)
class H14():
    # 'Charts_Data_M16'!H14
    value = 10150174
    formula = "=INDEX('Dashboard M16 EEPS'!$A$7:$T$11,MATCH($D$14,'Dashboard M16 EEPS'!$C$7:$C$11,0),MATCH($C$9,'Dashboard M16 EEPS'!$A$5:$T$5,0))"
    @eval_fn
    def H14():
        range_1 = Dashboard_M16_EEPS(1, 7, 20, 11)
        d14_1 = Charts_Data_M16.D14()
        range_2 = Dashboard_M16_EEPS(3, 7, 3, 11)
        var_1 = MATCH(d14_1, range_2, 0)
        c9_1 = Charts_Data_M16.C9()
        range_3 = Dashboard_M16_EEPS(1, 5, 20, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M16)
class A15():
    # 'Charts_Data_M16'!A15
    value = "Line Graph Input Final"

@register(Charts_Data_M16)
class C15():
    # 'Charts_Data_M16'!C15
    value = "#N/A"
    formula = "=VLOOKUP('Charts M16'!B3,'Charts Interactive LookupTables'!$W:$AA,2,FALSE)"
    @eval_fn
    def C15():
        b3_1 = Charts_M16.B3()
        range_1 = Charts_Interactive_LookupTables(23, 0, 27, 0)
        var_1 = VLOOKUP(b3_1, range_1, 2, "FALSE")
        return var_1

@register(Charts_Data_M16)
class D15():
    # 'Charts_Data_M16'!D15
    value = "#N/A"
    formula = '''=IF(OR($C$15="Total",$C$15="HECO"),"HECO",NA())'''
    @eval_fn
    def D15():
        c15_1 = Charts_Data_M16.C15()
        var_1 = equal(c15_1, "Total")
        c15_2 = Charts_Data_M16.C15()
        var_2 = equal(c15_2, "HECO")
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        var_5 = IF(var_3, "HECO", var_4)
        return var_5

@register(Charts_Data_M16)
class F15():
    # 'Charts_Data_M16'!F15
    value = "Notes"

@register(Charts_Data_M16)
class G15():
    # 'Charts_Data_M16'!G15
    value = "#N/A"
    formula = "=G3"
    @eval_fn
    def G15():
        g3_1 = Charts_Data_M16.G3()
        return g3_1

@register(Charts_Data_M16)
class H15():
    # 'Charts_Data_M16'!H15
    value = "#N/A"
    formula = "=H3"
    @eval_fn
    def H15():
        h3_1 = Charts_Data_M16.H3()
        return h3_1

@register(Charts_Data_M16)
class I15():
    # 'Charts_Data_M16'!I15
    value = "#N/A"
    formula = "=I3"
    @eval_fn
    def I15():
        i3_1 = Charts_Data_M16.I3()
        return i3_1

@register(Charts_Data_M16)
class J15():
    # 'Charts_Data_M16'!J15
    value = "#N/A"
    formula = "=J3"
    @eval_fn
    def J15():
        j3_1 = Charts_Data_M16.J3()
        return j3_1

@register(Charts_Data_M16)
class K15():
    # 'Charts_Data_M16'!K15
    value = "#N/A"
    formula = "=K3"
    @eval_fn
    def K15():
        k3_1 = Charts_Data_M16.K3()
        return k3_1

@register(Charts_Data_M16)
class L15():
    # 'Charts_Data_M16'!L15
    value = "#N/A"
    formula = "=L3"
    @eval_fn
    def L15():
        l3_1 = Charts_Data_M16.L3()
        return l3_1

@register(Charts_Data_M16)
class M15():
    # 'Charts_Data_M16'!M15
    value = 292000
    formula = "=M3"
    @eval_fn
    def M15():
        m3_1 = Charts_Data_M16.M3()
        return m3_1

@register(Charts_Data_M16)
class N15():
    # 'Charts_Data_M16'!N15
    value = 340000
    formula = "=N3"
    @eval_fn
    def N15():
        n3_1 = Charts_Data_M16.N3()
        return n3_1

@register(Charts_Data_M16)
class O15():
    # 'Charts_Data_M16'!O15
    value = 453000
    formula = "=O3"
    @eval_fn
    def O15():
        o3_1 = Charts_Data_M16.O3()
        return o3_1

@register(Charts_Data_M16)
class P15():
    # 'Charts_Data_M16'!P15
    value = 604007
    formula = "=P3"
    @eval_fn
    def P15():
        p3_1 = Charts_Data_M16.P3()
        return p3_1

@register(Charts_Data_M16)
class Q15():
    # 'Charts_Data_M16'!Q15
    value = 651278
    formula = "=Q3"
    @eval_fn
    def Q15():
        q3_1 = Charts_Data_M16.Q3()
        return q3_1

@register(Charts_Data_M16)
class R15():
    # 'Charts_Data_M16'!R15
    value = 738337
    formula = "=R3"
    @eval_fn
    def R15():
        r3_1 = Charts_Data_M16.R3()
        return r3_1

@register(Charts_Data_M16)
class S15():
    # 'Charts_Data_M16'!S15
    value = 821136
    formula = "=S3"
    @eval_fn
    def S15():
        s3_1 = Charts_Data_M16.S3()
        return s3_1

@register(Charts_Data_M16)
class T15():
    # 'Charts_Data_M16'!T15
    value = 958155
    formula = "=T3"
    @eval_fn
    def T15():
        t3_1 = Charts_Data_M16.T3()
        return t3_1

@register(Charts_Data_M16)
class U15():
    # 'Charts_Data_M16'!U15
    value = 1039167
    formula = "=U3"
    @eval_fn
    def U15():
        u3_1 = Charts_Data_M16.U3()
        return u3_1

@register(Charts_Data_M16)
class V15():
    # 'Charts_Data_M16'!V15
    value = 1117117
    formula = "=V3"
    @eval_fn
    def V15():
        v3_1 = Charts_Data_M16.V3()
        return v3_1

@register(Charts_Data_M16)
class W15():
    # 'Charts_Data_M16'!W15
    value = 1195067
    formula = "=W3"
    @eval_fn
    def W15():
        w3_1 = Charts_Data_M16.W3()
        return w3_1

@register(Charts_Data_M16)
class X15():
    # 'Charts_Data_M16'!X15
    value = "#N/A"
    formula = "=X3"
    @eval_fn
    def X15():
        x3_1 = Charts_Data_M16.X3()
        return x3_1

@register(Charts_Data_M16)
class Y15():
    # 'Charts_Data_M16'!Y15
    value = "#N/A"
    formula = "=Y3"
    @eval_fn
    def Y15():
        y3_1 = Charts_Data_M16.Y3()
        return y3_1

@register(Charts_Data_M16)
class Z15():
    # 'Charts_Data_M16'!Z15
    value = "#N/A"
    formula = "=Z3"
    @eval_fn
    def Z15():
        z3_1 = Charts_Data_M16.Z3()
        return z3_1

@register(Charts_Data_M16)
class AA15():
    # 'Charts_Data_M16'!AA15
    value = "#N/A"
    formula = "=AA3"
    @eval_fn
    def AA15():
        aa3_1 = Charts_Data_M16.AA3()
        return aa3_1

@register(Charts_Data_M16)
class AB15():
    # 'Charts_Data_M16'!AB15
    value = "#N/A"
    formula = "=AB3"
    @eval_fn
    def AB15():
        ab3_1 = Charts_Data_M16.AB3()
        return ab3_1

@register(Charts_Data_M16)
class AC15():
    # 'Charts_Data_M16'!AC15
    value = "#N/A"
    formula = "=AC3"
    @eval_fn
    def AC15():
        ac3_1 = Charts_Data_M16.AC3()
        return ac3_1

@register(Charts_Data_M16)
class AD15():
    # 'Charts_Data_M16'!AD15
    value = "#N/A"
    formula = "=AD3"
    @eval_fn
    def AD15():
        ad3_1 = Charts_Data_M16.AD3()
        return ad3_1

@register(Charts_Data_M16)
class AE15():
    # 'Charts_Data_M16'!AE15
    value = "#N/A"
    formula = "=AE3"
    @eval_fn
    def AE15():
        ae3_1 = Charts_Data_M16.AE3()
        return ae3_1

@register(Charts_Data_M16)
class AF15():
    # 'Charts_Data_M16'!AF15
    value = "#N/A"
    formula = "=AF3"
    @eval_fn
    def AF15():
        af3_1 = Charts_Data_M16.AF3()
        return af3_1

@register(Charts_Data_M16)
class AG15():
    # 'Charts_Data_M16'!AG15
    value = "#N/A"
    formula = "=AG3"
    @eval_fn
    def AG15():
        ag3_1 = Charts_Data_M16.AG3()
        return ag3_1

@register(Charts_Data_M16)
class AH15():
    # 'Charts_Data_M16'!AH15
    value = "#N/A"
    formula = "=AH3"
    @eval_fn
    def AH15():
        ah3_1 = Charts_Data_M16.AH3()
        return ah3_1

@register(Charts_Data_M16)
class AI15():
    # 'Charts_Data_M16'!AI15
    value = "#N/A"
    formula = "=AI3"
    @eval_fn
    def AI15():
        ai3_1 = Charts_Data_M16.AI3()
        return ai3_1

@register(Charts_Data_M16)
class AJ15():
    # 'Charts_Data_M16'!AJ15
    value = "#N/A"
    formula = "=AJ3"
    @eval_fn
    def AJ15():
        aj3_1 = Charts_Data_M16.AJ3()
        return aj3_1

@register(Charts_Data_M16)
class AK15():
    # 'Charts_Data_M16'!AK15
    value = "#N/A"
    formula = "=AK3"
    @eval_fn
    def AK15():
        ak3_1 = Charts_Data_M16.AK3()
        return ak3_1

@register(Charts_Data_M16)
class AL15():
    # 'Charts_Data_M16'!AL15
    value = "#N/A"
    formula = "=AL3"
    @eval_fn
    def AL15():
        al3_1 = Charts_Data_M16.AL3()
        return al3_1

@register(Charts_Data_M16)
class D16():
    # 'Charts_Data_M16'!D16
    value = "#N/A"
    formula = '''=IF(OR($C$15="Total",$C$15="HELCO"),"HELCO",NA())'''
    @eval_fn
    def D16():
        c15_1 = Charts_Data_M16.C15()
        var_1 = equal(c15_1, "Total")
        c15_2 = Charts_Data_M16.C15()
        var_2 = equal(c15_2, "HELCO")
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        var_5 = IF(var_3, "HELCO", var_4)
        return var_5

@register(Charts_Data_M16)
class F16():
    # 'Charts_Data_M16'!F16
    value = "Notes"

@register(Charts_Data_M16)
class G16():
    # 'Charts_Data_M16'!G16
    value = "#N/A"
    formula = "=G4"
    @eval_fn
    def G16():
        g4_1 = Charts_Data_M16.G4()
        return g4_1

@register(Charts_Data_M16)
class H16():
    # 'Charts_Data_M16'!H16
    value = "#N/A"
    formula = "=H4"
    @eval_fn
    def H16():
        h4_1 = Charts_Data_M16.H4()
        return h4_1

@register(Charts_Data_M16)
class I16():
    # 'Charts_Data_M16'!I16
    value = "#N/A"
    formula = "=I4"
    @eval_fn
    def I16():
        i4_1 = Charts_Data_M16.I4()
        return i4_1

@register(Charts_Data_M16)
class J16():
    # 'Charts_Data_M16'!J16
    value = "#N/A"
    formula = "=J4"
    @eval_fn
    def J16():
        j4_1 = Charts_Data_M16.J4()
        return j4_1

@register(Charts_Data_M16)
class K16():
    # 'Charts_Data_M16'!K16
    value = "#N/A"
    formula = "=K4"
    @eval_fn
    def K16():
        k4_1 = Charts_Data_M16.K4()
        return k4_1

@register(Charts_Data_M16)
class L16():
    # 'Charts_Data_M16'!L16
    value = "#N/A"
    formula = "=L4"
    @eval_fn
    def L16():
        l4_1 = Charts_Data_M16.L4()
        return l4_1

@register(Charts_Data_M16)
class M16():
    # 'Charts_Data_M16'!M16
    value = 49000
    formula = "=M4"
    @eval_fn
    def M16():
        m4_1 = Charts_Data_M16.M4()
        return m4_1

@register(Charts_Data_M16)
class N16():
    # 'Charts_Data_M16'!N16
    value = 54000
    formula = "=N4"
    @eval_fn
    def N16():
        n4_1 = Charts_Data_M16.N4()
        return n4_1

@register(Charts_Data_M16)
class O16():
    # 'Charts_Data_M16'!O16
    value = 57000
    formula = "=O4"
    @eval_fn
    def O16():
        o4_1 = Charts_Data_M16.O4()
        return o4_1

@register(Charts_Data_M16)
class P16():
    # 'Charts_Data_M16'!P16
    value = 47051
    formula = "=P4"
    @eval_fn
    def P16():
        p4_1 = Charts_Data_M16.P4()
        return p4_1

@register(Charts_Data_M16)
class Q16():
    # 'Charts_Data_M16'!Q16
    value = 49760
    formula = "=Q4"
    @eval_fn
    def Q16():
        q4_1 = Charts_Data_M16.Q4()
        return q4_1

@register(Charts_Data_M16)
class R16():
    # 'Charts_Data_M16'!R16
    value = 62359
    formula = "=R4"
    @eval_fn
    def R16():
        r4_1 = Charts_Data_M16.R4()
        return r4_1

@register(Charts_Data_M16)
class S16():
    # 'Charts_Data_M16'!S16
    value = 76622
    formula = "=S4"
    @eval_fn
    def S16():
        s4_1 = Charts_Data_M16.S4()
        return s4_1

@register(Charts_Data_M16)
class T16():
    # 'Charts_Data_M16'!T16
    value = 97765
    formula = "=T4"
    @eval_fn
    def T16():
        t4_1 = Charts_Data_M16.T4()
        return t4_1

@register(Charts_Data_M16)
class U16():
    # 'Charts_Data_M16'!U16
    value = 114116
    formula = "=U4"
    @eval_fn
    def U16():
        u4_1 = Charts_Data_M16.U4()
        return u4_1

@register(Charts_Data_M16)
class V16():
    # 'Charts_Data_M16'!V16
    value = 123070
    formula = "=V4"
    @eval_fn
    def V16():
        v4_1 = Charts_Data_M16.V4()
        return v4_1

@register(Charts_Data_M16)
class W16():
    # 'Charts_Data_M16'!W16
    value = 132024
    formula = "=W4"
    @eval_fn
    def W16():
        w4_1 = Charts_Data_M16.W4()
        return w4_1

@register(Charts_Data_M16)
class X16():
    # 'Charts_Data_M16'!X16
    value = "#N/A"
    formula = "=X4"
    @eval_fn
    def X16():
        x4_1 = Charts_Data_M16.X4()
        return x4_1

@register(Charts_Data_M16)
class Y16():
    # 'Charts_Data_M16'!Y16
    value = "#N/A"
    formula = "=Y4"
    @eval_fn
    def Y16():
        y4_1 = Charts_Data_M16.Y4()
        return y4_1

@register(Charts_Data_M16)
class Z16():
    # 'Charts_Data_M16'!Z16
    value = "#N/A"
    formula = "=Z4"
    @eval_fn
    def Z16():
        z4_1 = Charts_Data_M16.Z4()
        return z4_1

@register(Charts_Data_M16)
class AA16():
    # 'Charts_Data_M16'!AA16
    value = "#N/A"
    formula = "=AA4"
    @eval_fn
    def AA16():
        aa4_1 = Charts_Data_M16.AA4()
        return aa4_1

@register(Charts_Data_M16)
class AB16():
    # 'Charts_Data_M16'!AB16
    value = "#N/A"
    formula = "=AB4"
    @eval_fn
    def AB16():
        ab4_1 = Charts_Data_M16.AB4()
        return ab4_1

@register(Charts_Data_M16)
class AC16():
    # 'Charts_Data_M16'!AC16
    value = "#N/A"
    formula = "=AC4"
    @eval_fn
    def AC16():
        ac4_1 = Charts_Data_M16.AC4()
        return ac4_1

@register(Charts_Data_M16)
class AD16():
    # 'Charts_Data_M16'!AD16
    value = "#N/A"
    formula = "=AD4"
    @eval_fn
    def AD16():
        ad4_1 = Charts_Data_M16.AD4()
        return ad4_1

@register(Charts_Data_M16)
class AE16():
    # 'Charts_Data_M16'!AE16
    value = "#N/A"
    formula = "=AE4"
    @eval_fn
    def AE16():
        ae4_1 = Charts_Data_M16.AE4()
        return ae4_1

@register(Charts_Data_M16)
class AF16():
    # 'Charts_Data_M16'!AF16
    value = "#N/A"
    formula = "=AF4"
    @eval_fn
    def AF16():
        af4_1 = Charts_Data_M16.AF4()
        return af4_1

@register(Charts_Data_M16)
class AG16():
    # 'Charts_Data_M16'!AG16
    value = "#N/A"
    formula = "=AG4"
    @eval_fn
    def AG16():
        ag4_1 = Charts_Data_M16.AG4()
        return ag4_1

@register(Charts_Data_M16)
class AH16():
    # 'Charts_Data_M16'!AH16
    value = "#N/A"
    formula = "=AH4"
    @eval_fn
    def AH16():
        ah4_1 = Charts_Data_M16.AH4()
        return ah4_1

@register(Charts_Data_M16)
class AI16():
    # 'Charts_Data_M16'!AI16
    value = "#N/A"
    formula = "=AI4"
    @eval_fn
    def AI16():
        ai4_1 = Charts_Data_M16.AI4()
        return ai4_1

@register(Charts_Data_M16)
class AJ16():
    # 'Charts_Data_M16'!AJ16
    value = "#N/A"
    formula = "=AJ4"
    @eval_fn
    def AJ16():
        aj4_1 = Charts_Data_M16.AJ4()
        return aj4_1

@register(Charts_Data_M16)
class AK16():
    # 'Charts_Data_M16'!AK16
    value = "#N/A"
    formula = "=AK4"
    @eval_fn
    def AK16():
        ak4_1 = Charts_Data_M16.AK4()
        return ak4_1

@register(Charts_Data_M16)
class AL16():
    # 'Charts_Data_M16'!AL16
    value = "#N/A"
    formula = "=AL4"
    @eval_fn
    def AL16():
        al4_1 = Charts_Data_M16.AL4()
        return al4_1

@register(Charts_Data_M16)
class D17():
    # 'Charts_Data_M16'!D17
    value = "#N/A"
    formula = '''=IF(OR($C$15="Total",$C$15="MECO"),"MECO",NA())'''
    @eval_fn
    def D17():
        c15_1 = Charts_Data_M16.C15()
        var_1 = equal(c15_1, "Total")
        c15_2 = Charts_Data_M16.C15()
        var_2 = equal(c15_2, "MECO")
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        var_5 = IF(var_3, "MECO", var_4)
        return var_5

@register(Charts_Data_M16)
class F17():
    # 'Charts_Data_M16'!F17
    value = "Notes"

@register(Charts_Data_M16)
class G17():
    # 'Charts_Data_M16'!G17
    value = "#N/A"
    formula = "=G5"
    @eval_fn
    def G17():
        g5_1 = Charts_Data_M16.G5()
        return g5_1

@register(Charts_Data_M16)
class H17():
    # 'Charts_Data_M16'!H17
    value = "#N/A"
    formula = "=H5"
    @eval_fn
    def H17():
        h5_1 = Charts_Data_M16.H5()
        return h5_1

@register(Charts_Data_M16)
class I17():
    # 'Charts_Data_M16'!I17
    value = "#N/A"
    formula = "=I5"
    @eval_fn
    def I17():
        i5_1 = Charts_Data_M16.I5()
        return i5_1

@register(Charts_Data_M16)
class J17():
    # 'Charts_Data_M16'!J17
    value = "#N/A"
    formula = "=J5"
    @eval_fn
    def J17():
        j5_1 = Charts_Data_M16.J5()
        return j5_1

@register(Charts_Data_M16)
class K17():
    # 'Charts_Data_M16'!K17
    value = "#N/A"
    formula = "=K5"
    @eval_fn
    def K17():
        k5_1 = Charts_Data_M16.K5()
        return k5_1

@register(Charts_Data_M16)
class L17():
    # 'Charts_Data_M16'!L17
    value = "#N/A"
    formula = "=L5"
    @eval_fn
    def L17():
        l5_1 = Charts_Data_M16.L5()
        return l5_1

@register(Charts_Data_M16)
class M17():
    # 'Charts_Data_M16'!M17
    value = 77000
    formula = "=M5"
    @eval_fn
    def M17():
        m5_1 = Charts_Data_M16.M5()
        return m5_1

@register(Charts_Data_M16)
class N17():
    # 'Charts_Data_M16'!N17
    value = 82000
    formula = "=N5"
    @eval_fn
    def N17():
        n5_1 = Charts_Data_M16.N5()
        return n5_1

@register(Charts_Data_M16)
class O17():
    # 'Charts_Data_M16'!O17
    value = 88000
    formula = "=O5"
    @eval_fn
    def O17():
        o5_1 = Charts_Data_M16.O5()
        return o5_1

@register(Charts_Data_M16)
class P17():
    # 'Charts_Data_M16'!P17
    value = 79835
    formula = "=P5"
    @eval_fn
    def P17():
        p5_1 = Charts_Data_M16.P5()
        return p5_1

@register(Charts_Data_M16)
class Q17():
    # 'Charts_Data_M16'!Q17
    value = 88593
    formula = "=Q5"
    @eval_fn
    def Q17():
        q5_1 = Charts_Data_M16.Q5()
        return q5_1

@register(Charts_Data_M16)
class R17():
    # 'Charts_Data_M16'!R17
    value = 98813
    formula = "=R5"
    @eval_fn
    def R17():
        r5_1 = Charts_Data_M16.R5()
        return r5_1

@register(Charts_Data_M16)
class S17():
    # 'Charts_Data_M16'!S17
    value = 111306
    formula = "=S5"
    @eval_fn
    def S17():
        s5_1 = Charts_Data_M16.S5()
        return s5_1

@register(Charts_Data_M16)
class T17():
    # 'Charts_Data_M16'!T17
    value = 129340
    formula = "=T5"
    @eval_fn
    def T17():
        t5_1 = Charts_Data_M16.T5()
        return t5_1

@register(Charts_Data_M16)
class U17():
    # 'Charts_Data_M16'!U17
    value = 144281
    formula = "=U5"
    @eval_fn
    def U17():
        u5_1 = Charts_Data_M16.U5()
        return u5_1

@register(Charts_Data_M16)
class V17():
    # 'Charts_Data_M16'!V17
    value = 154216
    formula = "=V5"
    @eval_fn
    def V17():
        v5_1 = Charts_Data_M16.V5()
        return v5_1

@register(Charts_Data_M16)
class W17():
    # 'Charts_Data_M16'!W17
    value = 164151
    formula = "=W5"
    @eval_fn
    def W17():
        w5_1 = Charts_Data_M16.W5()
        return w5_1

@register(Charts_Data_M16)
class X17():
    # 'Charts_Data_M16'!X17
    value = "#N/A"
    formula = "=X5"
    @eval_fn
    def X17():
        x5_1 = Charts_Data_M16.X5()
        return x5_1

@register(Charts_Data_M16)
class Y17():
    # 'Charts_Data_M16'!Y17
    value = "#N/A"
    formula = "=Y5"
    @eval_fn
    def Y17():
        y5_1 = Charts_Data_M16.Y5()
        return y5_1

@register(Charts_Data_M16)
class Z17():
    # 'Charts_Data_M16'!Z17
    value = "#N/A"
    formula = "=Z5"
    @eval_fn
    def Z17():
        z5_1 = Charts_Data_M16.Z5()
        return z5_1

@register(Charts_Data_M16)
class AA17():
    # 'Charts_Data_M16'!AA17
    value = "#N/A"
    formula = "=AA5"
    @eval_fn
    def AA17():
        aa5_1 = Charts_Data_M16.AA5()
        return aa5_1

@register(Charts_Data_M16)
class AB17():
    # 'Charts_Data_M16'!AB17
    value = "#N/A"
    formula = "=AB5"
    @eval_fn
    def AB17():
        ab5_1 = Charts_Data_M16.AB5()
        return ab5_1

@register(Charts_Data_M16)
class AC17():
    # 'Charts_Data_M16'!AC17
    value = "#N/A"
    formula = "=AC5"
    @eval_fn
    def AC17():
        ac5_1 = Charts_Data_M16.AC5()
        return ac5_1

@register(Charts_Data_M16)
class AD17():
    # 'Charts_Data_M16'!AD17
    value = "#N/A"
    formula = "=AD5"
    @eval_fn
    def AD17():
        ad5_1 = Charts_Data_M16.AD5()
        return ad5_1

@register(Charts_Data_M16)
class AE17():
    # 'Charts_Data_M16'!AE17
    value = "#N/A"
    formula = "=AE5"
    @eval_fn
    def AE17():
        ae5_1 = Charts_Data_M16.AE5()
        return ae5_1

@register(Charts_Data_M16)
class AF17():
    # 'Charts_Data_M16'!AF17
    value = "#N/A"
    formula = "=AF5"
    @eval_fn
    def AF17():
        af5_1 = Charts_Data_M16.AF5()
        return af5_1

@register(Charts_Data_M16)
class AG17():
    # 'Charts_Data_M16'!AG17
    value = "#N/A"
    formula = "=AG5"
    @eval_fn
    def AG17():
        ag5_1 = Charts_Data_M16.AG5()
        return ag5_1

@register(Charts_Data_M16)
class AH17():
    # 'Charts_Data_M16'!AH17
    value = "#N/A"
    formula = "=AH5"
    @eval_fn
    def AH17():
        ah5_1 = Charts_Data_M16.AH5()
        return ah5_1

@register(Charts_Data_M16)
class AI17():
    # 'Charts_Data_M16'!AI17
    value = "#N/A"
    formula = "=AI5"
    @eval_fn
    def AI17():
        ai5_1 = Charts_Data_M16.AI5()
        return ai5_1

@register(Charts_Data_M16)
class AJ17():
    # 'Charts_Data_M16'!AJ17
    value = "#N/A"
    formula = "=AJ5"
    @eval_fn
    def AJ17():
        aj5_1 = Charts_Data_M16.AJ5()
        return aj5_1

@register(Charts_Data_M16)
class AK17():
    # 'Charts_Data_M16'!AK17
    value = "#N/A"
    formula = "=AK5"
    @eval_fn
    def AK17():
        ak5_1 = Charts_Data_M16.AK5()
        return ak5_1

@register(Charts_Data_M16)
class AL17():
    # 'Charts_Data_M16'!AL17
    value = "#N/A"
    formula = "=AL5"
    @eval_fn
    def AL17():
        al5_1 = Charts_Data_M16.AL5()
        return al5_1

@register(Charts_Data_M16)
class D18():
    # 'Charts_Data_M16'!D18
    value = "#N/A"
    formula = '''=IF(OR($C$15="Total",$C$15="KIUC"),"KIUC",NA())'''
    @eval_fn
    def D18():
        c15_1 = Charts_Data_M16.C15()
        var_1 = equal(c15_1, "Total")
        c15_2 = Charts_Data_M16.C15()
        var_2 = equal(c15_2, "KIUC")
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        var_5 = IF(var_3, "KIUC", var_4)
        return var_5

@register(Charts_Data_M16)
class F18():
    # 'Charts_Data_M16'!F18
    value = "Notes"

@register(Charts_Data_M16)
class G18():
    # 'Charts_Data_M16'!G18
    value = "#N/A"
    formula = "=G6"
    @eval_fn
    def G18():
        g6_1 = Charts_Data_M16.G6()
        return g6_1

@register(Charts_Data_M16)
class H18():
    # 'Charts_Data_M16'!H18
    value = "#N/A"
    formula = "=H6"
    @eval_fn
    def H18():
        h6_1 = Charts_Data_M16.H6()
        return h6_1

@register(Charts_Data_M16)
class I18():
    # 'Charts_Data_M16'!I18
    value = "#N/A"
    formula = "=I6"
    @eval_fn
    def I18():
        i6_1 = Charts_Data_M16.I6()
        return i6_1

@register(Charts_Data_M16)
class J18():
    # 'Charts_Data_M16'!J18
    value = "#N/A"
    formula = "=J6"
    @eval_fn
    def J18():
        j6_1 = Charts_Data_M16.J6()
        return j6_1

@register(Charts_Data_M16)
class K18():
    # 'Charts_Data_M16'!K18
    value = "#N/A"
    formula = "=K6"
    @eval_fn
    def K18():
        k6_1 = Charts_Data_M16.K6()
        return k6_1

@register(Charts_Data_M16)
class L18():
    # 'Charts_Data_M16'!L18
    value = 19037
    formula = "=L6"
    @eval_fn
    def L18():
        l6_1 = Charts_Data_M16.L6()
        return l6_1

@register(Charts_Data_M16)
class M18():
    # 'Charts_Data_M16'!M18
    value = 20855
    formula = "=M6"
    @eval_fn
    def M18():
        m6_1 = Charts_Data_M16.M6()
        return m6_1

@register(Charts_Data_M16)
class N18():
    # 'Charts_Data_M16'!N18
    value = 21349
    formula = "=N6"
    @eval_fn
    def N18():
        n6_1 = Charts_Data_M16.N6()
        return n6_1

@register(Charts_Data_M16)
class O18():
    # 'Charts_Data_M16'!O18
    value = 21361
    formula = "=O6"
    @eval_fn
    def O18():
        o6_1 = Charts_Data_M16.O6()
        return o6_1

@register(Charts_Data_M16)
class P18():
    # 'Charts_Data_M16'!P18
    value = 19233
    formula = "=P6"
    @eval_fn
    def P18():
        p6_1 = Charts_Data_M16.P6()
        return p6_1

@register(Charts_Data_M16)
class Q18():
    # 'Charts_Data_M16'!Q18
    value = 19217
    formula = "=Q6"
    @eval_fn
    def Q18():
        q6_1 = Charts_Data_M16.Q6()
        return q6_1

@register(Charts_Data_M16)
class R18():
    # 'Charts_Data_M16'!R18
    value = 16911
    formula = "=R6"
    @eval_fn
    def R18():
        r6_1 = Charts_Data_M16.R6()
        return r6_1

@register(Charts_Data_M16)
class S18():
    # 'Charts_Data_M16'!S18
    value = 18264
    formula = "=S6"
    @eval_fn
    def S18():
        s6_1 = Charts_Data_M16.S6()
        return s6_1

@register(Charts_Data_M16)
class T18():
    # 'Charts_Data_M16'!T18
    value = 24368
    formula = "=T6"
    @eval_fn
    def T18():
        t6_1 = Charts_Data_M16.T6()
        return t6_1

@register(Charts_Data_M16)
class U18():
    # 'Charts_Data_M16'!U18
    value = 22441
    formula = "=U6"
    @eval_fn
    def U18():
        u6_1 = Charts_Data_M16.U6()
        return u6_1

@register(Charts_Data_M16)
class V18():
    # 'Charts_Data_M16'!V18
    value = 21370
    formula = "=V6"
    @eval_fn
    def V18():
        v6_1 = Charts_Data_M16.V6()
        return v6_1

@register(Charts_Data_M16)
class W18():
    # 'Charts_Data_M16'!W18
    value = 19947
    formula = "=W6"
    @eval_fn
    def W18():
        w6_1 = Charts_Data_M16.W6()
        return w6_1

@register(Charts_Data_M16)
class X18():
    # 'Charts_Data_M16'!X18
    value = "#N/A"
    formula = "=X6"
    @eval_fn
    def X18():
        x6_1 = Charts_Data_M16.X6()
        return x6_1

@register(Charts_Data_M16)
class Y18():
    # 'Charts_Data_M16'!Y18
    value = "#N/A"
    formula = "=Y6"
    @eval_fn
    def Y18():
        y6_1 = Charts_Data_M16.Y6()
        return y6_1

@register(Charts_Data_M16)
class Z18():
    # 'Charts_Data_M16'!Z18
    value = "#N/A"
    formula = "=Z6"
    @eval_fn
    def Z18():
        z6_1 = Charts_Data_M16.Z6()
        return z6_1

@register(Charts_Data_M16)
class AA18():
    # 'Charts_Data_M16'!AA18
    value = "#N/A"
    formula = "=AA6"
    @eval_fn
    def AA18():
        aa6_1 = Charts_Data_M16.AA6()
        return aa6_1

@register(Charts_Data_M16)
class AB18():
    # 'Charts_Data_M16'!AB18
    value = "#N/A"
    formula = "=AB6"
    @eval_fn
    def AB18():
        ab6_1 = Charts_Data_M16.AB6()
        return ab6_1

@register(Charts_Data_M16)
class AC18():
    # 'Charts_Data_M16'!AC18
    value = "#N/A"
    formula = "=AC6"
    @eval_fn
    def AC18():
        ac6_1 = Charts_Data_M16.AC6()
        return ac6_1

@register(Charts_Data_M16)
class AD18():
    # 'Charts_Data_M16'!AD18
    value = "#N/A"
    formula = "=AD6"
    @eval_fn
    def AD18():
        ad6_1 = Charts_Data_M16.AD6()
        return ad6_1

@register(Charts_Data_M16)
class AE18():
    # 'Charts_Data_M16'!AE18
    value = "#N/A"
    formula = "=AE6"
    @eval_fn
    def AE18():
        ae6_1 = Charts_Data_M16.AE6()
        return ae6_1

@register(Charts_Data_M16)
class AF18():
    # 'Charts_Data_M16'!AF18
    value = "#N/A"
    formula = "=AF6"
    @eval_fn
    def AF18():
        af6_1 = Charts_Data_M16.AF6()
        return af6_1

@register(Charts_Data_M16)
class AG18():
    # 'Charts_Data_M16'!AG18
    value = "#N/A"
    formula = "=AG6"
    @eval_fn
    def AG18():
        ag6_1 = Charts_Data_M16.AG6()
        return ag6_1

@register(Charts_Data_M16)
class AH18():
    # 'Charts_Data_M16'!AH18
    value = "#N/A"
    formula = "=AH6"
    @eval_fn
    def AH18():
        ah6_1 = Charts_Data_M16.AH6()
        return ah6_1

@register(Charts_Data_M16)
class AI18():
    # 'Charts_Data_M16'!AI18
    value = "#N/A"
    formula = "=AI6"
    @eval_fn
    def AI18():
        ai6_1 = Charts_Data_M16.AI6()
        return ai6_1

@register(Charts_Data_M16)
class AJ18():
    # 'Charts_Data_M16'!AJ18
    value = "#N/A"
    formula = "=AJ6"
    @eval_fn
    def AJ18():
        aj6_1 = Charts_Data_M16.AJ6()
        return aj6_1

@register(Charts_Data_M16)
class AK18():
    # 'Charts_Data_M16'!AK18
    value = "#N/A"
    formula = "=AK6"
    @eval_fn
    def AK18():
        ak6_1 = Charts_Data_M16.AK6()
        return ak6_1

@register(Charts_Data_M16)
class AL18():
    # 'Charts_Data_M16'!AL18
    value = "#N/A"
    formula = "=AL6"
    @eval_fn
    def AL18():
        al6_1 = Charts_Data_M16.AL6()
        return al6_1

@register(Charts_Data_M16)
class D19():
    # 'Charts_Data_M16'!D19
    value = "#N/A"
    formula = '''=IF(OR($C$15="Total",$C$15="Total"),"Total",NA())'''
    @eval_fn
    def D19():
        c15_1 = Charts_Data_M16.C15()
        var_1 = equal(c15_1, "Total")
        c15_2 = Charts_Data_M16.C15()
        var_2 = equal(c15_2, "Total")
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        var_5 = IF(var_3, "Total", var_4)
        return var_5

@register(Charts_Data_M16)
class F19():
    # 'Charts_Data_M16'!F19
    value = "Notes"

@register(Charts_Data_M16)
class G19():
    # 'Charts_Data_M16'!G19
    value = "#N/A"
    formula = "=G7"
    @eval_fn
    def G19():
        g7_1 = Charts_Data_M16.G7()
        return g7_1

@register(Charts_Data_M16)
class H19():
    # 'Charts_Data_M16'!H19
    value = "#N/A"
    formula = "=H7"
    @eval_fn
    def H19():
        h7_1 = Charts_Data_M16.H7()
        return h7_1

@register(Charts_Data_M16)
class I19():
    # 'Charts_Data_M16'!I19
    value = "#N/A"
    formula = "=I7"
    @eval_fn
    def I19():
        i7_1 = Charts_Data_M16.I7()
        return i7_1

@register(Charts_Data_M16)
class J19():
    # 'Charts_Data_M16'!J19
    value = "#N/A"
    formula = "=J7"
    @eval_fn
    def J19():
        j7_1 = Charts_Data_M16.J7()
        return j7_1

@register(Charts_Data_M16)
class K19():
    # 'Charts_Data_M16'!K19
    value = "#N/A"
    formula = "=K7"
    @eval_fn
    def K19():
        k7_1 = Charts_Data_M16.K7()
        return k7_1

@register(Charts_Data_M16)
class L19():
    # 'Charts_Data_M16'!L19
    value = 19037
    formula = "=L7"
    @eval_fn
    def L19():
        l7_1 = Charts_Data_M16.L7()
        return l7_1

@register(Charts_Data_M16)
class M19():
    # 'Charts_Data_M16'!M19
    value = 438855
    formula = "=M7"
    @eval_fn
    def M19():
        m7_1 = Charts_Data_M16.M7()
        return m7_1

@register(Charts_Data_M16)
class N19():
    # 'Charts_Data_M16'!N19
    value = 497349
    formula = "=N7"
    @eval_fn
    def N19():
        n7_1 = Charts_Data_M16.N7()
        return n7_1

@register(Charts_Data_M16)
class O19():
    # 'Charts_Data_M16'!O19
    value = 619361
    formula = "=O7"
    @eval_fn
    def O19():
        o7_1 = Charts_Data_M16.O7()
        return o7_1

@register(Charts_Data_M16)
class P19():
    # 'Charts_Data_M16'!P19
    value = 750126
    formula = "=P7"
    @eval_fn
    def P19():
        p7_1 = Charts_Data_M16.P7()
        return p7_1

@register(Charts_Data_M16)
class Q19():
    # 'Charts_Data_M16'!Q19
    value = 808848
    formula = "=Q7"
    @eval_fn
    def Q19():
        q7_1 = Charts_Data_M16.Q7()
        return q7_1

@register(Charts_Data_M16)
class R19():
    # 'Charts_Data_M16'!R19
    value = 916420
    formula = "=R7"
    @eval_fn
    def R19():
        r7_1 = Charts_Data_M16.R7()
        return r7_1

@register(Charts_Data_M16)
class S19():
    # 'Charts_Data_M16'!S19
    value = 1027328
    formula = "=S7"
    @eval_fn
    def S19():
        s7_1 = Charts_Data_M16.S7()
        return s7_1

@register(Charts_Data_M16)
class T19():
    # 'Charts_Data_M16'!T19
    value = 1209628
    formula = "=T7"
    @eval_fn
    def T19():
        t7_1 = Charts_Data_M16.T7()
        return t7_1

@register(Charts_Data_M16)
class U19():
    # 'Charts_Data_M16'!U19
    value = 1320005
    formula = "=U7"
    @eval_fn
    def U19():
        u7_1 = Charts_Data_M16.U7()
        return u7_1

@register(Charts_Data_M16)
class V19():
    # 'Charts_Data_M16'!V19
    value = 1415773
    formula = "=V7"
    @eval_fn
    def V19():
        v7_1 = Charts_Data_M16.V7()
        return v7_1

@register(Charts_Data_M16)
class W19():
    # 'Charts_Data_M16'!W19
    value = 1511189
    formula = "=W7"
    @eval_fn
    def W19():
        w7_1 = Charts_Data_M16.W7()
        return w7_1

@register(Charts_Data_M16)
class X19():
    # 'Charts_Data_M16'!X19
    value = "#N/A"
    formula = "=X7"
    @eval_fn
    def X19():
        x7_1 = Charts_Data_M16.X7()
        return x7_1

@register(Charts_Data_M16)
class Y19():
    # 'Charts_Data_M16'!Y19
    value = "#N/A"
    formula = "=Y7"
    @eval_fn
    def Y19():
        y7_1 = Charts_Data_M16.Y7()
        return y7_1

@register(Charts_Data_M16)
class Z19():
    # 'Charts_Data_M16'!Z19
    value = "#N/A"
    formula = "=Z7"
    @eval_fn
    def Z19():
        z7_1 = Charts_Data_M16.Z7()
        return z7_1

@register(Charts_Data_M16)
class AA19():
    # 'Charts_Data_M16'!AA19
    value = "#N/A"
    formula = "=AA7"
    @eval_fn
    def AA19():
        aa7_1 = Charts_Data_M16.AA7()
        return aa7_1

@register(Charts_Data_M16)
class AB19():
    # 'Charts_Data_M16'!AB19
    value = "#N/A"
    formula = "=AB7"
    @eval_fn
    def AB19():
        ab7_1 = Charts_Data_M16.AB7()
        return ab7_1

@register(Charts_Data_M16)
class AC19():
    # 'Charts_Data_M16'!AC19
    value = "#N/A"
    formula = "=AC7"
    @eval_fn
    def AC19():
        ac7_1 = Charts_Data_M16.AC7()
        return ac7_1

@register(Charts_Data_M16)
class AD19():
    # 'Charts_Data_M16'!AD19
    value = "#N/A"
    formula = "=AD7"
    @eval_fn
    def AD19():
        ad7_1 = Charts_Data_M16.AD7()
        return ad7_1

@register(Charts_Data_M16)
class AE19():
    # 'Charts_Data_M16'!AE19
    value = "#N/A"
    formula = "=AE7"
    @eval_fn
    def AE19():
        ae7_1 = Charts_Data_M16.AE7()
        return ae7_1

@register(Charts_Data_M16)
class AF19():
    # 'Charts_Data_M16'!AF19
    value = "#N/A"
    formula = "=AF7"
    @eval_fn
    def AF19():
        af7_1 = Charts_Data_M16.AF7()
        return af7_1

@register(Charts_Data_M16)
class AG19():
    # 'Charts_Data_M16'!AG19
    value = "#N/A"
    formula = "=AG7"
    @eval_fn
    def AG19():
        ag7_1 = Charts_Data_M16.AG7()
        return ag7_1

@register(Charts_Data_M16)
class AH19():
    # 'Charts_Data_M16'!AH19
    value = "#N/A"
    formula = "=AH7"
    @eval_fn
    def AH19():
        ah7_1 = Charts_Data_M16.AH7()
        return ah7_1

@register(Charts_Data_M16)
class AI19():
    # 'Charts_Data_M16'!AI19
    value = "#N/A"
    formula = "=AI7"
    @eval_fn
    def AI19():
        ai7_1 = Charts_Data_M16.AI7()
        return ai7_1

@register(Charts_Data_M16)
class AJ19():
    # 'Charts_Data_M16'!AJ19
    value = "#N/A"
    formula = "=AJ7"
    @eval_fn
    def AJ19():
        aj7_1 = Charts_Data_M16.AJ7()
        return aj7_1

@register(Charts_Data_M16)
class AK19():
    # 'Charts_Data_M16'!AK19
    value = "#N/A"
    formula = "=AK7"
    @eval_fn
    def AK19():
        ak7_1 = Charts_Data_M16.AK7()
        return ak7_1

@register(Charts_Data_M16)
class AL19():
    # 'Charts_Data_M16'!AL19
    value = "#N/A"
    formula = "=AL7"
    @eval_fn
    def AL19():
        al7_1 = Charts_Data_M16.AL7()
        return al7_1