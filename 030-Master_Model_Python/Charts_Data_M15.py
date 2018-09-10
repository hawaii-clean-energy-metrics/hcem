# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_Data_M15 = Worksheet('Charts_Data_M15', 10, 10)



@register(Charts_Data_M15)
class A1():
    # 'Charts_Data_M15'!A1
    value = "Metric 15:"

@register(Charts_Data_M15)
class F1():
    # 'Charts_Data_M15'!F1
    value = "Notes"

@register(Charts_Data_M15)
class G1():
    # 'Charts_Data_M15'!G1
    value = 2000

@register(Charts_Data_M15)
class H1():
    # 'Charts_Data_M15'!H1
    value = 2001

@register(Charts_Data_M15)
class I1():
    # 'Charts_Data_M15'!I1
    value = 2002

@register(Charts_Data_M15)
class J1():
    # 'Charts_Data_M15'!J1
    value = 2003

@register(Charts_Data_M15)
class K1():
    # 'Charts_Data_M15'!K1
    value = 2004

@register(Charts_Data_M15)
class L1():
    # 'Charts_Data_M15'!L1
    value = 2005

@register(Charts_Data_M15)
class M1():
    # 'Charts_Data_M15'!M1
    value = 2006

@register(Charts_Data_M15)
class N1():
    # 'Charts_Data_M15'!N1
    value = 2007

@register(Charts_Data_M15)
class O1():
    # 'Charts_Data_M15'!O1
    value = 2008

@register(Charts_Data_M15)
class P1():
    # 'Charts_Data_M15'!P1
    value = 2009

@register(Charts_Data_M15)
class Q1():
    # 'Charts_Data_M15'!Q1
    value = 2010

@register(Charts_Data_M15)
class R1():
    # 'Charts_Data_M15'!R1
    value = 2011

@register(Charts_Data_M15)
class S1():
    # 'Charts_Data_M15'!S1
    value = 2012

@register(Charts_Data_M15)
class T1():
    # 'Charts_Data_M15'!T1
    value = 2013

@register(Charts_Data_M15)
class U1():
    # 'Charts_Data_M15'!U1
    value = 2014

@register(Charts_Data_M15)
class V1():
    # 'Charts_Data_M15'!V1
    value = 2015

@register(Charts_Data_M15)
class W1():
    # 'Charts_Data_M15'!W1
    value = 2016

@register(Charts_Data_M15)
class X1():
    # 'Charts_Data_M15'!X1
    value = 2017

@register(Charts_Data_M15)
class Y1():
    # 'Charts_Data_M15'!Y1
    value = 2018

@register(Charts_Data_M15)
class Z1():
    # 'Charts_Data_M15'!Z1
    value = 2019

@register(Charts_Data_M15)
class AA1():
    # 'Charts_Data_M15'!AA1
    value = 2020

@register(Charts_Data_M15)
class AB1():
    # 'Charts_Data_M15'!AB1
    value = 2021

@register(Charts_Data_M15)
class AC1():
    # 'Charts_Data_M15'!AC1
    value = 2022

@register(Charts_Data_M15)
class AD1():
    # 'Charts_Data_M15'!AD1
    value = 2023

@register(Charts_Data_M15)
class AE1():
    # 'Charts_Data_M15'!AE1
    value = 2024

@register(Charts_Data_M15)
class AF1():
    # 'Charts_Data_M15'!AF1
    value = 2025

@register(Charts_Data_M15)
class AG1():
    # 'Charts_Data_M15'!AG1
    value = 2026

@register(Charts_Data_M15)
class AH1():
    # 'Charts_Data_M15'!AH1
    value = 2027

@register(Charts_Data_M15)
class AI1():
    # 'Charts_Data_M15'!AI1
    value = 2028

@register(Charts_Data_M15)
class AJ1():
    # 'Charts_Data_M15'!AJ1
    value = 2029

@register(Charts_Data_M15)
class AK1():
    # 'Charts_Data_M15'!AK1
    value = 2030

@register(Charts_Data_M15)
class A2():
    # 'Charts_Data_M15'!A2
    value = "AnChangeSolar Thermal and Photovoltaic"
    formula = "=VLOOKUP('Charts M15'!$B$17,'Charts Interactive LookupTables'!$R:$U,4,FALSE)&VLOOKUP('Charts M15'!$B$16,'Charts Interactive LookupTables'!$R:$U,2,FALSE)"
    @eval_fn
    def A2():
        b17_1 = Charts_M15.B17()
        range_1 = Charts_Interactive_LookupTables(18, 0, 21, 0)
        var_1 = VLOOKUP(b17_1, range_1, 4, "FALSE")
        b16_1 = Charts_M15.B16()
        range_2 = Charts_Interactive_LookupTables(18, 0, 21, 0)
        var_2 = VLOOKUP(b16_1, range_2, 2, "FALSE")
        var_3 = concat(var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class B2():
    # 'Charts_Data_M15'!B2
    value = "Annual Change in MW"
    formula = "=VLOOKUP('Charts M15'!$B$17,'Charts Interactive LookupTables'!$R:$V,5,FALSE)"
    @eval_fn
    def B2():
        b17_1 = Charts_M15.B17()
        range_1 = Charts_Interactive_LookupTables(18, 0, 22, 0)
        var_1 = VLOOKUP(b17_1, range_1, 5, "FALSE")
        return var_1

@register(Charts_Data_M15)
class D2():
    # 'Charts_Data_M15'!D2
    value = "Unit"

@register(Charts_Data_M15)
class F2():
    # 'Charts_Data_M15'!F2
    value = "Notes"

@register(Charts_Data_M15)
class B3():
    # 'Charts_Data_M15'!B3
    value = "Solar Thermal and Photovoltaic"
    formula = "=VLOOKUP(A2,'Dashboard M15'!$A$6:$B$35,2,FALSE)"
    @eval_fn
    def B3():
        a2_1 = Charts_Data_M15.A2()
        range_1 = Dashboard_M15(1, 6, 2, 35)
        var_1 = VLOOKUP(a2_1, range_1, 2, "FALSE")
        return var_1

@register(Charts_Data_M15)
class D3():
    # 'Charts_Data_M15'!D3
    value = "MW"

@register(Charts_Data_M15)
class F3():
    # 'Charts_Data_M15'!F3
    value = "Notes"

@register(Charts_Data_M15)
class G3():
    # 'Charts_Data_M15'!G3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!G$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def G3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        g3_1 = Dashboard_M15.G3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(g3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class H3():
    # 'Charts_Data_M15'!H3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!H$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def H3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        h3_1 = Dashboard_M15.H3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(h3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class I3():
    # 'Charts_Data_M15'!I3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!I$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def I3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        i3_1 = Dashboard_M15.I3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(i3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class J3():
    # 'Charts_Data_M15'!J3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!J$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def J3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        j3_1 = Dashboard_M15.J3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(j3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class K3():
    # 'Charts_Data_M15'!K3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!K$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def K3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        k3_1 = Dashboard_M15.K3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(k3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class L3():
    # 'Charts_Data_M15'!L3
    value = 1.8
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!L$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def L3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        l3_1 = Dashboard_M15.L3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(l3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class M3():
    # 'Charts_Data_M15'!M3
    value = 0.6
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!M$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def M3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        m3_1 = Dashboard_M15.M3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(m3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class N3():
    # 'Charts_Data_M15'!N3
    value = 2.844
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!N$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def N3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        n3_1 = Dashboard_M15.N3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(n3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class O3():
    # 'Charts_Data_M15'!O3
    value = 8.925
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!O$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def O3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        o3_1 = Dashboard_M15.O3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(o3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class P3():
    # 'Charts_Data_M15'!P3
    value = 12.27
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!P$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def P3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        p3_1 = Dashboard_M15.P3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(p3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class Q3():
    # 'Charts_Data_M15'!Q3
    value = 17.166
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!Q$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Q3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        q3_1 = Dashboard_M15.Q3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(q3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class R3():
    # 'Charts_Data_M15'!R3
    value = 39.54
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!R$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def R3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        r3_1 = Dashboard_M15.R3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(r3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class S3():
    # 'Charts_Data_M15'!S3
    value = 98.252
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!S$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def S3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        s3_1 = Dashboard_M15.S3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(s3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class T3():
    # 'Charts_Data_M15'!T3
    value = 94.803
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!T$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def T3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        t3_1 = Dashboard_M15.T3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(t3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class U3():
    # 'Charts_Data_M15'!U3
    value = -244
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!U$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def U3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        u3_1 = Dashboard_M15.U3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(u3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class V3():
    # 'Charts_Data_M15'!V3
    value = 12
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!V$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def V3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        v3_1 = Dashboard_M15.V3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(v3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class W3():
    # 'Charts_Data_M15'!W3
    value = -44.2
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!W$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def W3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        w3_1 = Dashboard_M15.W3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(w3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class X3():
    # 'Charts_Data_M15'!X3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!X$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def X3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        x3_1 = Dashboard_M15.X3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(x3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class Y3():
    # 'Charts_Data_M15'!Y3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!Y$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Y3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        y3_1 = Dashboard_M15.Y3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(y3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class Z3():
    # 'Charts_Data_M15'!Z3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!Z$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Z3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        z3_1 = Dashboard_M15.Z3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(z3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AA3():
    # 'Charts_Data_M15'!AA3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AA$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AA3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        aa3_1 = Dashboard_M15.AA3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(aa3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AB3():
    # 'Charts_Data_M15'!AB3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AB$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AB3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        ab3_1 = Dashboard_M15.AB3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(ab3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AC3():
    # 'Charts_Data_M15'!AC3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AC$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AC3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        ac3_1 = Dashboard_M15.AC3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(ac3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AD3():
    # 'Charts_Data_M15'!AD3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AD$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AD3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        ad3_1 = Dashboard_M15.AD3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(ad3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AE3():
    # 'Charts_Data_M15'!AE3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AE$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AE3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        ae3_1 = Dashboard_M15.AE3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(ae3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AF3():
    # 'Charts_Data_M15'!AF3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AF$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AF3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        af3_1 = Dashboard_M15.AF3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(af3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AG3():
    # 'Charts_Data_M15'!AG3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AG$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AG3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        ag3_1 = Dashboard_M15.AG3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(ag3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AH3():
    # 'Charts_Data_M15'!AH3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AH$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AH3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        ah3_1 = Dashboard_M15.AH3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(ah3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AI3():
    # 'Charts_Data_M15'!AI3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AI$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AI3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        ai3_1 = Dashboard_M15.AI3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(ai3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AJ3():
    # 'Charts_Data_M15'!AJ3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AJ$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AJ3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        aj3_1 = Dashboard_M15.AJ3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(aj3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class AK3():
    # 'Charts_Data_M15'!AK3
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$2,'Dashboard M15'!$A$4:$A$35,0),MATCH('Dashboard M15'!AK$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AK3():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a2_1 = Charts_Data_M15.A2()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a2_1, range_2, 0)
        ak3_1 = Dashboard_M15.AK3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_2 = MATCH(ak3_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M15)
class A4():
    # 'Charts_Data_M15'!A4
    value = "Annual Change in MW"

@register(Charts_Data_M15)
class F4():
    # 'Charts_Data_M15'!F4
    value = "Notes"

@register(Charts_Data_M15)
class A5():
    # 'Charts_Data_M15'!A5
    value = "AnChange"
    formula = "=VLOOKUP('Charts M15'!$B$17,'Charts Interactive LookupTables'!$R:$U,4,FALSE)"
    @eval_fn
    def A5():
        b17_1 = Charts_M15.B17()
        range_1 = Charts_Interactive_LookupTables(18, 0, 21, 0)
        var_1 = VLOOKUP(b17_1, range_1, 4, "FALSE")
        return var_1

@register(Charts_Data_M15)
class B5():
    # 'Charts_Data_M15'!B5
    value = "Annual Change in MW"
    formula = "=VLOOKUP('Charts M15'!$B$17,'Charts Interactive LookupTables'!$R:$V,5,FALSE)"
    @eval_fn
    def B5():
        b17_1 = Charts_M15.B17()
        range_1 = Charts_Interactive_LookupTables(18, 0, 22, 0)
        var_1 = VLOOKUP(b17_1, range_1, 5, "FALSE")
        return var_1

@register(Charts_Data_M15)
class D5():
    # 'Charts_Data_M15'!D5
    value = "Unit"

@register(Charts_Data_M15)
class F5():
    # 'Charts_Data_M15'!F5
    value = "Notes"

@register(Charts_Data_M15)
class A6():
    # 'Charts_Data_M15'!A6
    value = "AnChangeAll Renewables"
    formula = "='Dashboard M15'!$A$27&B6"
    @eval_fn
    def A6():
        a27_1 = Dashboard_M15.A27()
        b6_1 = Charts_Data_M15.B6()
        var_1 = concat(a27_1, b6_1)
        return var_1

@register(Charts_Data_M15)
class B6():
    # 'Charts_Data_M15'!B6
    value = "All Renewables"

@register(Charts_Data_M15)
class D6():
    # 'Charts_Data_M15'!D6
    value = "MW"

@register(Charts_Data_M15)
class F6():
    # 'Charts_Data_M15'!F6
    value = "Notes"

@register(Charts_Data_M15)
class G6():
    # 'Charts_Data_M15'!G6
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!G$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def G6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        g3_1 = Dashboard_M15.G3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(g3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class H6():
    # 'Charts_Data_M15'!H6
    value = -6
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!H$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def H6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        h3_1 = Dashboard_M15.H3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(h3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class I6():
    # 'Charts_Data_M15'!I6
    value = -42
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!I$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def I6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        i3_1 = Dashboard_M15.I3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(i3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class J6():
    # 'Charts_Data_M15'!J6
    value = 2
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!J$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def J6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        j3_1 = Dashboard_M15.J3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(j3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class K6():
    # 'Charts_Data_M15'!K6
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!K$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def K6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        k3_1 = Dashboard_M15.K3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(k3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class L6():
    # 'Charts_Data_M15'!L6
    value = 3.8
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!L$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def L6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        l3_1 = Dashboard_M15.L3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(l3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class M6():
    # 'Charts_Data_M15'!M6
    value = 32.6
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!M$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def M6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        m3_1 = Dashboard_M15.M3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(m3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class N6():
    # 'Charts_Data_M15'!N6
    value = 23.844
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!N$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def N6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        n3_1 = Dashboard_M15.N3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(n3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class O6():
    # 'Charts_Data_M15'!O6
    value = 8.925
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!O$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def O6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        o3_1 = Dashboard_M15.O3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(o3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class P6():
    # 'Charts_Data_M15'!P6
    value = 125.27
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!P$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def P6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        p3_1 = Dashboard_M15.P3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(p3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Q6():
    # 'Charts_Data_M15'!Q6
    value = 15.166
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!Q$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Q6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        q3_1 = Dashboard_M15.Q3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(q3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class R6():
    # 'Charts_Data_M15'!R6
    value = 72.04
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!R$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def R6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        r3_1 = Dashboard_M15.R3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(r3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class S6():
    # 'Charts_Data_M15'!S6
    value = 223.352
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!S$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def S6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        s3_1 = Dashboard_M15.S3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(s3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class T6():
    # 'Charts_Data_M15'!T6
    value = 128.403
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!T$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def T6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        t3_1 = Dashboard_M15.T3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(t3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class U6():
    # 'Charts_Data_M15'!U6
    value = -248
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!U$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def U6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        u3_1 = Dashboard_M15.U3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(u3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class V6():
    # 'Charts_Data_M15'!V6
    value = 15
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!V$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def V6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        v3_1 = Dashboard_M15.V3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(v3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class W6():
    # 'Charts_Data_M15'!W6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!W$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def W6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        w3_1 = Dashboard_M15.W3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(w3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class X6():
    # 'Charts_Data_M15'!X6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!X$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def X6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        x3_1 = Dashboard_M15.X3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(x3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Y6():
    # 'Charts_Data_M15'!Y6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!Y$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Y6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        y3_1 = Dashboard_M15.Y3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(y3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Z6():
    # 'Charts_Data_M15'!Z6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!Z$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Z6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        z3_1 = Dashboard_M15.Z3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(z3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AA6():
    # 'Charts_Data_M15'!AA6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AA$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AA6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        aa3_1 = Dashboard_M15.AA3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aa3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AB6():
    # 'Charts_Data_M15'!AB6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AB$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AB6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        ab3_1 = Dashboard_M15.AB3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ab3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AC6():
    # 'Charts_Data_M15'!AC6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AC$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AC6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        ac3_1 = Dashboard_M15.AC3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ac3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AD6():
    # 'Charts_Data_M15'!AD6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AD$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AD6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        ad3_1 = Dashboard_M15.AD3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ad3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AE6():
    # 'Charts_Data_M15'!AE6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AE$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AE6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        ae3_1 = Dashboard_M15.AE3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ae3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AF6():
    # 'Charts_Data_M15'!AF6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AF$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AF6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        af3_1 = Dashboard_M15.AF3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(af3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AG6():
    # 'Charts_Data_M15'!AG6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AG$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AG6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        ag3_1 = Dashboard_M15.AG3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ag3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AH6():
    # 'Charts_Data_M15'!AH6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AH$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AH6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        ah3_1 = Dashboard_M15.AH3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ah3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AI6():
    # 'Charts_Data_M15'!AI6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AI$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AI6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        ai3_1 = Dashboard_M15.AI3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ai3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AJ6():
    # 'Charts_Data_M15'!AJ6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AJ$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AJ6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        aj3_1 = Dashboard_M15.AJ3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aj3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AK6():
    # 'Charts_Data_M15'!AK6
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+1,MATCH('Dashboard M15'!AK$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AK6():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 1)
        ak3_1 = Dashboard_M15.AK3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ak3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class A7():
    # 'Charts_Data_M15'!A7
    value = "AnChangeGeothermal"
    formula = "='Dashboard M15'!$A$27&B7"
    @eval_fn
    def A7():
        a27_1 = Dashboard_M15.A27()
        b7_1 = Charts_Data_M15.B7()
        var_1 = concat(a27_1, b7_1)
        return var_1

@register(Charts_Data_M15)
class B7():
    # 'Charts_Data_M15'!B7
    value = "Geothermal"

@register(Charts_Data_M15)
class D7():
    # 'Charts_Data_M15'!D7
    value = "MW"

@register(Charts_Data_M15)
class F7():
    # 'Charts_Data_M15'!F7
    value = "Notes"

@register(Charts_Data_M15)
class G7():
    # 'Charts_Data_M15'!G7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!G$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def G7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        g3_1 = Dashboard_M15.G3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(g3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class H7():
    # 'Charts_Data_M15'!H7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!H$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def H7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        h3_1 = Dashboard_M15.H3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(h3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class I7():
    # 'Charts_Data_M15'!I7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!I$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def I7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        i3_1 = Dashboard_M15.I3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(i3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class J7():
    # 'Charts_Data_M15'!J7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!J$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def J7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        j3_1 = Dashboard_M15.J3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(j3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class K7():
    # 'Charts_Data_M15'!K7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!K$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def K7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        k3_1 = Dashboard_M15.K3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(k3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class L7():
    # 'Charts_Data_M15'!L7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!L$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def L7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        l3_1 = Dashboard_M15.L3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(l3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class M7():
    # 'Charts_Data_M15'!M7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!M$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def M7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        m3_1 = Dashboard_M15.M3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(m3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class N7():
    # 'Charts_Data_M15'!N7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!N$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def N7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        n3_1 = Dashboard_M15.N3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(n3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class O7():
    # 'Charts_Data_M15'!O7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!O$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def O7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        o3_1 = Dashboard_M15.O3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(o3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class P7():
    # 'Charts_Data_M15'!P7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!P$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def P7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        p3_1 = Dashboard_M15.P3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(p3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Q7():
    # 'Charts_Data_M15'!Q7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!Q$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Q7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        q3_1 = Dashboard_M15.Q3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(q3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class R7():
    # 'Charts_Data_M15'!R7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!R$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def R7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        r3_1 = Dashboard_M15.R3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(r3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class S7():
    # 'Charts_Data_M15'!S7
    value = 16
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!S$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def S7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        s3_1 = Dashboard_M15.S3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(s3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class T7():
    # 'Charts_Data_M15'!T7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!T$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def T7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        t3_1 = Dashboard_M15.T3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(t3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class U7():
    # 'Charts_Data_M15'!U7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!U$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def U7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        u3_1 = Dashboard_M15.U3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(u3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class V7():
    # 'Charts_Data_M15'!V7
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!V$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def V7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        v3_1 = Dashboard_M15.V3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(v3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class W7():
    # 'Charts_Data_M15'!W7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!W$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def W7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        w3_1 = Dashboard_M15.W3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(w3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class X7():
    # 'Charts_Data_M15'!X7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!X$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def X7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        x3_1 = Dashboard_M15.X3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(x3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Y7():
    # 'Charts_Data_M15'!Y7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!Y$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Y7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        y3_1 = Dashboard_M15.Y3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(y3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Z7():
    # 'Charts_Data_M15'!Z7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!Z$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Z7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        z3_1 = Dashboard_M15.Z3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(z3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AA7():
    # 'Charts_Data_M15'!AA7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AA$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AA7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        aa3_1 = Dashboard_M15.AA3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aa3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AB7():
    # 'Charts_Data_M15'!AB7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AB$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AB7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        ab3_1 = Dashboard_M15.AB3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ab3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AC7():
    # 'Charts_Data_M15'!AC7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AC$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AC7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        ac3_1 = Dashboard_M15.AC3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ac3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AD7():
    # 'Charts_Data_M15'!AD7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AD$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AD7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        ad3_1 = Dashboard_M15.AD3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ad3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AE7():
    # 'Charts_Data_M15'!AE7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AE$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AE7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        ae3_1 = Dashboard_M15.AE3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ae3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AF7():
    # 'Charts_Data_M15'!AF7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AF$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AF7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        af3_1 = Dashboard_M15.AF3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(af3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AG7():
    # 'Charts_Data_M15'!AG7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AG$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AG7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        ag3_1 = Dashboard_M15.AG3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ag3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AH7():
    # 'Charts_Data_M15'!AH7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AH$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AH7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        ah3_1 = Dashboard_M15.AH3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ah3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AI7():
    # 'Charts_Data_M15'!AI7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AI$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AI7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        ai3_1 = Dashboard_M15.AI3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ai3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AJ7():
    # 'Charts_Data_M15'!AJ7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AJ$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AJ7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        aj3_1 = Dashboard_M15.AJ3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aj3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AK7():
    # 'Charts_Data_M15'!AK7
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+2,MATCH('Dashboard M15'!AK$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AK7():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 2)
        ak3_1 = Dashboard_M15.AK3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ak3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class A8():
    # 'Charts_Data_M15'!A8
    value = "AnChangeHydroelectric"
    formula = "='Dashboard M15'!$A$27&B8"
    @eval_fn
    def A8():
        a27_1 = Dashboard_M15.A27()
        b8_1 = Charts_Data_M15.B8()
        var_1 = concat(a27_1, b8_1)
        return var_1

@register(Charts_Data_M15)
class B8():
    # 'Charts_Data_M15'!B8
    value = "Hydroelectric"

@register(Charts_Data_M15)
class D8():
    # 'Charts_Data_M15'!D8
    value = "MW"

@register(Charts_Data_M15)
class F8():
    # 'Charts_Data_M15'!F8
    value = "Notes"

@register(Charts_Data_M15)
class G8():
    # 'Charts_Data_M15'!G8
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!G$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def G8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        g3_1 = Dashboard_M15.G3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(g3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class H8():
    # 'Charts_Data_M15'!H8
    value = -1
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!H$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def H8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        h3_1 = Dashboard_M15.H3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(h3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class I8():
    # 'Charts_Data_M15'!I8
    value = -1
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!I$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def I8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        i3_1 = Dashboard_M15.I3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(i3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class J8():
    # 'Charts_Data_M15'!J8
    value = -2
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!J$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def J8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        j3_1 = Dashboard_M15.J3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(j3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class K8():
    # 'Charts_Data_M15'!K8
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!K$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def K8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        k3_1 = Dashboard_M15.K3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(k3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class L8():
    # 'Charts_Data_M15'!L8
    value = 2
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!L$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def L8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        l3_1 = Dashboard_M15.L3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(l3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class M8():
    # 'Charts_Data_M15'!M8
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!M$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def M8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        m3_1 = Dashboard_M15.M3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(m3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class N8():
    # 'Charts_Data_M15'!N8
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!N$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def N8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        n3_1 = Dashboard_M15.N3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(n3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class O8():
    # 'Charts_Data_M15'!O8
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!O$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def O8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        o3_1 = Dashboard_M15.O3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(o3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class P8():
    # 'Charts_Data_M15'!P8
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!P$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def P8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        p3_1 = Dashboard_M15.P3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(p3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Q8():
    # 'Charts_Data_M15'!Q8
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!Q$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Q8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        q3_1 = Dashboard_M15.Q3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(q3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class R8():
    # 'Charts_Data_M15'!R8
    value = -0.1
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!R$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def R8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        r3_1 = Dashboard_M15.R3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(r3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class S8():
    # 'Charts_Data_M15'!S8
    value = 1.3
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!S$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def S8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        s3_1 = Dashboard_M15.S3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(s3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class T8():
    # 'Charts_Data_M15'!T8
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!T$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def T8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        t3_1 = Dashboard_M15.T3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(t3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class U8():
    # 'Charts_Data_M15'!U8
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!U$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def U8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        u3_1 = Dashboard_M15.U3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(u3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class V8():
    # 'Charts_Data_M15'!V8
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!V$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def V8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        v3_1 = Dashboard_M15.V3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(v3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class W8():
    # 'Charts_Data_M15'!W8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!W$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def W8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        w3_1 = Dashboard_M15.W3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(w3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class X8():
    # 'Charts_Data_M15'!X8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!X$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def X8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        x3_1 = Dashboard_M15.X3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(x3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Y8():
    # 'Charts_Data_M15'!Y8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!Y$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Y8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        y3_1 = Dashboard_M15.Y3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(y3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Z8():
    # 'Charts_Data_M15'!Z8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!Z$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Z8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        z3_1 = Dashboard_M15.Z3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(z3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AA8():
    # 'Charts_Data_M15'!AA8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AA$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AA8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        aa3_1 = Dashboard_M15.AA3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aa3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AB8():
    # 'Charts_Data_M15'!AB8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AB$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AB8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        ab3_1 = Dashboard_M15.AB3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ab3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AC8():
    # 'Charts_Data_M15'!AC8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AC$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AC8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        ac3_1 = Dashboard_M15.AC3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ac3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AD8():
    # 'Charts_Data_M15'!AD8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AD$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AD8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        ad3_1 = Dashboard_M15.AD3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ad3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AE8():
    # 'Charts_Data_M15'!AE8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AE$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AE8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        ae3_1 = Dashboard_M15.AE3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ae3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AF8():
    # 'Charts_Data_M15'!AF8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AF$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AF8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        af3_1 = Dashboard_M15.AF3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(af3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AG8():
    # 'Charts_Data_M15'!AG8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AG$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AG8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        ag3_1 = Dashboard_M15.AG3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ag3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AH8():
    # 'Charts_Data_M15'!AH8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AH$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AH8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        ah3_1 = Dashboard_M15.AH3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ah3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AI8():
    # 'Charts_Data_M15'!AI8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AI$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AI8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        ai3_1 = Dashboard_M15.AI3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ai3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AJ8():
    # 'Charts_Data_M15'!AJ8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AJ$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AJ8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        aj3_1 = Dashboard_M15.AJ3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aj3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AK8():
    # 'Charts_Data_M15'!AK8
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+3,MATCH('Dashboard M15'!AK$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AK8():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 3)
        ak3_1 = Dashboard_M15.AK3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ak3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class A9():
    # 'Charts_Data_M15'!A9
    value = "AnChangeOther Biomass"
    formula = "='Dashboard M15'!$A$27&B9"
    @eval_fn
    def A9():
        a27_1 = Dashboard_M15.A27()
        b9_1 = Charts_Data_M15.B9()
        var_1 = concat(a27_1, b9_1)
        return var_1

@register(Charts_Data_M15)
class B9():
    # 'Charts_Data_M15'!B9
    value = "Other Biomass"

@register(Charts_Data_M15)
class D9():
    # 'Charts_Data_M15'!D9
    value = "MW"

@register(Charts_Data_M15)
class F9():
    # 'Charts_Data_M15'!F9
    value = "Notes"

@register(Charts_Data_M15)
class G9():
    # 'Charts_Data_M15'!G9
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!G$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def G9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        g3_1 = Dashboard_M15.G3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(g3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class H9():
    # 'Charts_Data_M15'!H9
    value = -4
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!H$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def H9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        h3_1 = Dashboard_M15.H3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(h3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class I9():
    # 'Charts_Data_M15'!I9
    value = -41
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!I$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def I9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        i3_1 = Dashboard_M15.I3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(i3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class J9():
    # 'Charts_Data_M15'!J9
    value = 4
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!J$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def J9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        j3_1 = Dashboard_M15.J3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(j3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class K9():
    # 'Charts_Data_M15'!K9
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!K$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def K9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        k3_1 = Dashboard_M15.K3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(k3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class L9():
    # 'Charts_Data_M15'!L9
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!L$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def L9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        l3_1 = Dashboard_M15.L3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(l3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class M9():
    # 'Charts_Data_M15'!M9
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!M$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def M9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        m3_1 = Dashboard_M15.M3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(m3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class N9():
    # 'Charts_Data_M15'!N9
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!N$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def N9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        n3_1 = Dashboard_M15.N3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(n3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class O9():
    # 'Charts_Data_M15'!O9
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!O$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def O9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        o3_1 = Dashboard_M15.O3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(o3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class P9():
    # 'Charts_Data_M15'!P9
    value = 113
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!P$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def P9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        p3_1 = Dashboard_M15.P3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(p3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Q9():
    # 'Charts_Data_M15'!Q9
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!Q$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Q9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        q3_1 = Dashboard_M15.Q3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(q3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class R9():
    # 'Charts_Data_M15'!R9
    value = -0.2
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!R$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def R9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        r3_1 = Dashboard_M15.R3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(r3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class S9():
    # 'Charts_Data_M15'!S9
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!S$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def S9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        s3_1 = Dashboard_M15.S3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(s3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class T9():
    # 'Charts_Data_M15'!T9
    value = 33.6
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!T$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def T9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        t3_1 = Dashboard_M15.T3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(t3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class U9():
    # 'Charts_Data_M15'!U9
    value = -4
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!U$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def U9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        u3_1 = Dashboard_M15.U3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(u3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class V9():
    # 'Charts_Data_M15'!V9
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!V$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def V9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        v3_1 = Dashboard_M15.V3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(v3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class W9():
    # 'Charts_Data_M15'!W9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!W$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def W9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        w3_1 = Dashboard_M15.W3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(w3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class X9():
    # 'Charts_Data_M15'!X9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!X$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def X9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        x3_1 = Dashboard_M15.X3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(x3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Y9():
    # 'Charts_Data_M15'!Y9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!Y$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Y9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        y3_1 = Dashboard_M15.Y3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(y3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Z9():
    # 'Charts_Data_M15'!Z9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!Z$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Z9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        z3_1 = Dashboard_M15.Z3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(z3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AA9():
    # 'Charts_Data_M15'!AA9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AA$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AA9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        aa3_1 = Dashboard_M15.AA3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aa3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AB9():
    # 'Charts_Data_M15'!AB9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AB$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AB9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        ab3_1 = Dashboard_M15.AB3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ab3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AC9():
    # 'Charts_Data_M15'!AC9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AC$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AC9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        ac3_1 = Dashboard_M15.AC3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ac3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AD9():
    # 'Charts_Data_M15'!AD9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AD$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AD9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        ad3_1 = Dashboard_M15.AD3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ad3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AE9():
    # 'Charts_Data_M15'!AE9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AE$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AE9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        ae3_1 = Dashboard_M15.AE3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ae3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AF9():
    # 'Charts_Data_M15'!AF9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AF$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AF9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        af3_1 = Dashboard_M15.AF3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(af3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AG9():
    # 'Charts_Data_M15'!AG9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AG$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AG9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        ag3_1 = Dashboard_M15.AG3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ag3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AH9():
    # 'Charts_Data_M15'!AH9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AH$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AH9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        ah3_1 = Dashboard_M15.AH3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ah3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AI9():
    # 'Charts_Data_M15'!AI9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AI$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AI9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        ai3_1 = Dashboard_M15.AI3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ai3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AJ9():
    # 'Charts_Data_M15'!AJ9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AJ$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AJ9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        aj3_1 = Dashboard_M15.AJ3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aj3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AK9():
    # 'Charts_Data_M15'!AK9
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+4,MATCH('Dashboard M15'!AK$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AK9():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 4)
        ak3_1 = Dashboard_M15.AK3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ak3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class A10():
    # 'Charts_Data_M15'!A10
    value = "AnChangeOther Gases"
    formula = "='Dashboard M15'!$A$27&B10"
    @eval_fn
    def A10():
        a27_1 = Dashboard_M15.A27()
        b10_1 = Charts_Data_M15.B10()
        var_1 = concat(a27_1, b10_1)
        return var_1

@register(Charts_Data_M15)
class B10():
    # 'Charts_Data_M15'!B10
    value = "Other Gases"

@register(Charts_Data_M15)
class D10():
    # 'Charts_Data_M15'!D10
    value = "MW"

@register(Charts_Data_M15)
class F10():
    # 'Charts_Data_M15'!F10
    value = "Notes"

@register(Charts_Data_M15)
class G10():
    # 'Charts_Data_M15'!G10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!G$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def G10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        g3_1 = Dashboard_M15.G3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(g3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class H10():
    # 'Charts_Data_M15'!H10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!H$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def H10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        h3_1 = Dashboard_M15.H3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(h3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class I10():
    # 'Charts_Data_M15'!I10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!I$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def I10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        i3_1 = Dashboard_M15.I3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(i3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class J10():
    # 'Charts_Data_M15'!J10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!J$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def J10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        j3_1 = Dashboard_M15.J3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(j3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class K10():
    # 'Charts_Data_M15'!K10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!K$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def K10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        k3_1 = Dashboard_M15.K3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(k3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class L10():
    # 'Charts_Data_M15'!L10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!L$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def L10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        l3_1 = Dashboard_M15.L3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(l3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class M10():
    # 'Charts_Data_M15'!M10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!M$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def M10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        m3_1 = Dashboard_M15.M3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(m3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class N10():
    # 'Charts_Data_M15'!N10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!N$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def N10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        n3_1 = Dashboard_M15.N3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(n3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class O10():
    # 'Charts_Data_M15'!O10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!O$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def O10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        o3_1 = Dashboard_M15.O3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(o3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class P10():
    # 'Charts_Data_M15'!P10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!P$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def P10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        p3_1 = Dashboard_M15.P3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(p3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Q10():
    # 'Charts_Data_M15'!Q10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!Q$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Q10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        q3_1 = Dashboard_M15.Q3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(q3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class R10():
    # 'Charts_Data_M15'!R10
    value = 3.2
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!R$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def R10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        r3_1 = Dashboard_M15.R3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(r3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class S10():
    # 'Charts_Data_M15'!S10
    value = -6.2
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!S$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def S10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        s3_1 = Dashboard_M15.S3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(s3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class T10():
    # 'Charts_Data_M15'!T10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!T$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def T10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        t3_1 = Dashboard_M15.T3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(t3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class U10():
    # 'Charts_Data_M15'!U10
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!U$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def U10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        u3_1 = Dashboard_M15.U3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(u3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class V10():
    # 'Charts_Data_M15'!V10
    value = 3
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!V$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def V10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        v3_1 = Dashboard_M15.V3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(v3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class W10():
    # 'Charts_Data_M15'!W10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!W$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def W10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        w3_1 = Dashboard_M15.W3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(w3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class X10():
    # 'Charts_Data_M15'!X10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!X$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def X10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        x3_1 = Dashboard_M15.X3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(x3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Y10():
    # 'Charts_Data_M15'!Y10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!Y$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Y10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        y3_1 = Dashboard_M15.Y3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(y3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Z10():
    # 'Charts_Data_M15'!Z10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!Z$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Z10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        z3_1 = Dashboard_M15.Z3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(z3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AA10():
    # 'Charts_Data_M15'!AA10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AA$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AA10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        aa3_1 = Dashboard_M15.AA3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aa3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AB10():
    # 'Charts_Data_M15'!AB10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AB$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AB10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        ab3_1 = Dashboard_M15.AB3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ab3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AC10():
    # 'Charts_Data_M15'!AC10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AC$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AC10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        ac3_1 = Dashboard_M15.AC3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ac3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AD10():
    # 'Charts_Data_M15'!AD10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AD$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AD10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        ad3_1 = Dashboard_M15.AD3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ad3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AE10():
    # 'Charts_Data_M15'!AE10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AE$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AE10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        ae3_1 = Dashboard_M15.AE3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ae3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AF10():
    # 'Charts_Data_M15'!AF10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AF$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AF10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        af3_1 = Dashboard_M15.AF3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(af3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AG10():
    # 'Charts_Data_M15'!AG10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AG$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AG10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        ag3_1 = Dashboard_M15.AG3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ag3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AH10():
    # 'Charts_Data_M15'!AH10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AH$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AH10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        ah3_1 = Dashboard_M15.AH3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ah3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AI10():
    # 'Charts_Data_M15'!AI10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AI$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AI10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        ai3_1 = Dashboard_M15.AI3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ai3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AJ10():
    # 'Charts_Data_M15'!AJ10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AJ$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AJ10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        aj3_1 = Dashboard_M15.AJ3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aj3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AK10():
    # 'Charts_Data_M15'!AK10
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+5,MATCH('Dashboard M15'!AK$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AK10():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 5)
        ak3_1 = Dashboard_M15.AK3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ak3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class A11():
    # 'Charts_Data_M15'!A11
    value = "AnChangeSolar Thermal and Photovoltaic"
    formula = "='Dashboard M15'!$A$27&B11"
    @eval_fn
    def A11():
        a27_1 = Dashboard_M15.A27()
        b11_1 = Charts_Data_M15.B11()
        var_1 = concat(a27_1, b11_1)
        return var_1

@register(Charts_Data_M15)
class B11():
    # 'Charts_Data_M15'!B11
    value = "Solar Thermal and Photovoltaic"

@register(Charts_Data_M15)
class D11():
    # 'Charts_Data_M15'!D11
    value = "MW"

@register(Charts_Data_M15)
class F11():
    # 'Charts_Data_M15'!F11
    value = "Notes"

@register(Charts_Data_M15)
class G11():
    # 'Charts_Data_M15'!G11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!G$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def G11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        g3_1 = Dashboard_M15.G3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(g3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class H11():
    # 'Charts_Data_M15'!H11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!H$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def H11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        h3_1 = Dashboard_M15.H3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(h3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class I11():
    # 'Charts_Data_M15'!I11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!I$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def I11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        i3_1 = Dashboard_M15.I3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(i3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class J11():
    # 'Charts_Data_M15'!J11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!J$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def J11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        j3_1 = Dashboard_M15.J3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(j3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class K11():
    # 'Charts_Data_M15'!K11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!K$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def K11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        k3_1 = Dashboard_M15.K3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(k3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class L11():
    # 'Charts_Data_M15'!L11
    value = 1.8
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!L$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def L11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        l3_1 = Dashboard_M15.L3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(l3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class M11():
    # 'Charts_Data_M15'!M11
    value = 0.6
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!M$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def M11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        m3_1 = Dashboard_M15.M3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(m3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class N11():
    # 'Charts_Data_M15'!N11
    value = 2.844
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!N$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def N11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        n3_1 = Dashboard_M15.N3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(n3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class O11():
    # 'Charts_Data_M15'!O11
    value = 8.925
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!O$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def O11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        o3_1 = Dashboard_M15.O3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(o3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class P11():
    # 'Charts_Data_M15'!P11
    value = 12.27
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!P$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def P11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        p3_1 = Dashboard_M15.P3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(p3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Q11():
    # 'Charts_Data_M15'!Q11
    value = 17.166
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!Q$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Q11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        q3_1 = Dashboard_M15.Q3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(q3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class R11():
    # 'Charts_Data_M15'!R11
    value = 39.54
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!R$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def R11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        r3_1 = Dashboard_M15.R3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(r3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class S11():
    # 'Charts_Data_M15'!S11
    value = 98.252
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!S$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def S11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        s3_1 = Dashboard_M15.S3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(s3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class T11():
    # 'Charts_Data_M15'!T11
    value = 94.803
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!T$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def T11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        t3_1 = Dashboard_M15.T3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(t3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class U11():
    # 'Charts_Data_M15'!U11
    value = -244
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!U$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def U11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        u3_1 = Dashboard_M15.U3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(u3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class V11():
    # 'Charts_Data_M15'!V11
    value = 12
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!V$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def V11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        v3_1 = Dashboard_M15.V3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(v3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class W11():
    # 'Charts_Data_M15'!W11
    value = -44.2
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!W$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def W11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        w3_1 = Dashboard_M15.W3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(w3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class X11():
    # 'Charts_Data_M15'!X11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!X$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def X11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        x3_1 = Dashboard_M15.X3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(x3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Y11():
    # 'Charts_Data_M15'!Y11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!Y$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Y11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        y3_1 = Dashboard_M15.Y3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(y3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Z11():
    # 'Charts_Data_M15'!Z11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!Z$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Z11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        z3_1 = Dashboard_M15.Z3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(z3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AA11():
    # 'Charts_Data_M15'!AA11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AA$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AA11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        aa3_1 = Dashboard_M15.AA3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aa3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AB11():
    # 'Charts_Data_M15'!AB11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AB$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AB11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        ab3_1 = Dashboard_M15.AB3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ab3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AC11():
    # 'Charts_Data_M15'!AC11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AC$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AC11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        ac3_1 = Dashboard_M15.AC3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ac3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AD11():
    # 'Charts_Data_M15'!AD11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AD$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AD11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        ad3_1 = Dashboard_M15.AD3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ad3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AE11():
    # 'Charts_Data_M15'!AE11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AE$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AE11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        ae3_1 = Dashboard_M15.AE3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ae3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AF11():
    # 'Charts_Data_M15'!AF11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AF$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AF11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        af3_1 = Dashboard_M15.AF3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(af3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AG11():
    # 'Charts_Data_M15'!AG11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AG$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AG11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        ag3_1 = Dashboard_M15.AG3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ag3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AH11():
    # 'Charts_Data_M15'!AH11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AH$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AH11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        ah3_1 = Dashboard_M15.AH3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ah3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AI11():
    # 'Charts_Data_M15'!AI11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AI$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AI11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        ai3_1 = Dashboard_M15.AI3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ai3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AJ11():
    # 'Charts_Data_M15'!AJ11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AJ$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AJ11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        aj3_1 = Dashboard_M15.AJ3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aj3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AK11():
    # 'Charts_Data_M15'!AK11
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+6,MATCH('Dashboard M15'!AK$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AK11():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 6)
        ak3_1 = Dashboard_M15.AK3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ak3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class A12():
    # 'Charts_Data_M15'!A12
    value = "AnChangeWind"
    formula = "='Dashboard M15'!$A$27&B12"
    @eval_fn
    def A12():
        a27_1 = Dashboard_M15.A27()
        b12_1 = Charts_Data_M15.B12()
        var_1 = concat(a27_1, b12_1)
        return var_1

@register(Charts_Data_M15)
class B12():
    # 'Charts_Data_M15'!B12
    value = "Wind"

@register(Charts_Data_M15)
class D12():
    # 'Charts_Data_M15'!D12
    value = "MW"

@register(Charts_Data_M15)
class F12():
    # 'Charts_Data_M15'!F12
    value = "Notes"

@register(Charts_Data_M15)
class G12():
    # 'Charts_Data_M15'!G12
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!G$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def G12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        g3_1 = Dashboard_M15.G3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(g3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class H12():
    # 'Charts_Data_M15'!H12
    value = -1
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!H$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def H12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        h3_1 = Dashboard_M15.H3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(h3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class I12():
    # 'Charts_Data_M15'!I12
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!I$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def I12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        i3_1 = Dashboard_M15.I3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(i3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class J12():
    # 'Charts_Data_M15'!J12
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!J$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def J12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        j3_1 = Dashboard_M15.J3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(j3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class K12():
    # 'Charts_Data_M15'!K12
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!K$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def K12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        k3_1 = Dashboard_M15.K3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(k3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class L12():
    # 'Charts_Data_M15'!L12
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!L$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def L12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        l3_1 = Dashboard_M15.L3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(l3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class M12():
    # 'Charts_Data_M15'!M12
    value = 32
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!M$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def M12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        m3_1 = Dashboard_M15.M3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(m3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class N12():
    # 'Charts_Data_M15'!N12
    value = 21
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!N$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def N12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        n3_1 = Dashboard_M15.N3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(n3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class O12():
    # 'Charts_Data_M15'!O12
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!O$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def O12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        o3_1 = Dashboard_M15.O3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(o3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class P12():
    # 'Charts_Data_M15'!P12
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!P$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def P12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        p3_1 = Dashboard_M15.P3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(p3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Q12():
    # 'Charts_Data_M15'!Q12
    value = -2
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!Q$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Q12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        q3_1 = Dashboard_M15.Q3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(q3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class R12():
    # 'Charts_Data_M15'!R12
    value = 29.6
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!R$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def R12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        r3_1 = Dashboard_M15.R3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(r3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class S12():
    # 'Charts_Data_M15'!S12
    value = 114
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!S$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def S12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        s3_1 = Dashboard_M15.S3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(s3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class T12():
    # 'Charts_Data_M15'!T12
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!T$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def T12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        t3_1 = Dashboard_M15.T3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(t3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class U12():
    # 'Charts_Data_M15'!U12
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!U$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def U12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        u3_1 = Dashboard_M15.U3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(u3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class V12():
    # 'Charts_Data_M15'!V12
    value = 0
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!V$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def V12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        v3_1 = Dashboard_M15.V3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(v3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class W12():
    # 'Charts_Data_M15'!W12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!W$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def W12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        w3_1 = Dashboard_M15.W3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(w3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class X12():
    # 'Charts_Data_M15'!X12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!X$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def X12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        x3_1 = Dashboard_M15.X3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(x3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Y12():
    # 'Charts_Data_M15'!Y12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!Y$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Y12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        y3_1 = Dashboard_M15.Y3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(y3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class Z12():
    # 'Charts_Data_M15'!Z12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!Z$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def Z12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        z3_1 = Dashboard_M15.Z3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(z3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AA12():
    # 'Charts_Data_M15'!AA12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AA$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AA12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        aa3_1 = Dashboard_M15.AA3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aa3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AB12():
    # 'Charts_Data_M15'!AB12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AB$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AB12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        ab3_1 = Dashboard_M15.AB3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ab3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AC12():
    # 'Charts_Data_M15'!AC12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AC$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AC12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        ac3_1 = Dashboard_M15.AC3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ac3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AD12():
    # 'Charts_Data_M15'!AD12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AD$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AD12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        ad3_1 = Dashboard_M15.AD3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ad3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AE12():
    # 'Charts_Data_M15'!AE12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AE$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AE12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        ae3_1 = Dashboard_M15.AE3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ae3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AF12():
    # 'Charts_Data_M15'!AF12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AF$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AF12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        af3_1 = Dashboard_M15.AF3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(af3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AG12():
    # 'Charts_Data_M15'!AG12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AG$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AG12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        ag3_1 = Dashboard_M15.AG3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ag3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AH12():
    # 'Charts_Data_M15'!AH12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AH$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AH12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        ah3_1 = Dashboard_M15.AH3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ah3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AI12():
    # 'Charts_Data_M15'!AI12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AI$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AI12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        ai3_1 = Dashboard_M15.AI3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ai3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AJ12():
    # 'Charts_Data_M15'!AJ12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AJ$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AJ12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        aj3_1 = Dashboard_M15.AJ3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(aj3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M15)
class AK12():
    # 'Charts_Data_M15'!AK12
    value = "#N/A"
    formula = "=INDEX('Dashboard M15'!$A$4:$AK$35,MATCH($A$5,'Dashboard M15'!$A$4:$A$35,0)+7,MATCH('Dashboard M15'!AK$3,'Dashboard M15'!$A$3:$AK$3,0))"
    @eval_fn
    def AK12():
        range_1 = Dashboard_M15(1, 4, 37, 35)
        a5_1 = Charts_Data_M15.A5()
        range_2 = Dashboard_M15(1, 4, 1, 35)
        var_1 = MATCH(a5_1, range_2, 0)
        var_2 = add(var_1, 7)
        ak3_1 = Dashboard_M15.AK3()
        range_3 = Dashboard_M15(1, 3, 37, 3)
        var_3 = MATCH(ak3_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4