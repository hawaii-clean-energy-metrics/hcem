# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_Data_M2 = Worksheet('Charts_Data_M2', 10, 10)



@register(Charts_Data_M2)
class A1():
    # 'Charts_Data_M2'!A1
    value = "Metric 2: Expenditures on fuel imports to Hawai‘i"
    formula = "='Dashboard M2 Annual'!A1"
    @eval_fn
    def A1():
        a1_1 = Dashboard_M2_Annual.A1()
        return a1_1

@register(Charts_Data_M2)
class F1():
    # 'Charts_Data_M2'!F1
    value = "Notes"

@register(Charts_Data_M2)
class G1():
    # 'Charts_Data_M2'!G1
    value = 1990

@register(Charts_Data_M2)
class H1():
    # 'Charts_Data_M2'!H1
    value = 1991

@register(Charts_Data_M2)
class I1():
    # 'Charts_Data_M2'!I1
    value = 1992

@register(Charts_Data_M2)
class J1():
    # 'Charts_Data_M2'!J1
    value = 1993

@register(Charts_Data_M2)
class K1():
    # 'Charts_Data_M2'!K1
    value = 1994

@register(Charts_Data_M2)
class L1():
    # 'Charts_Data_M2'!L1
    value = 1995

@register(Charts_Data_M2)
class M1():
    # 'Charts_Data_M2'!M1
    value = 1996

@register(Charts_Data_M2)
class N1():
    # 'Charts_Data_M2'!N1
    value = 1997

@register(Charts_Data_M2)
class O1():
    # 'Charts_Data_M2'!O1
    value = 1998

@register(Charts_Data_M2)
class P1():
    # 'Charts_Data_M2'!P1
    value = 1999

@register(Charts_Data_M2)
class Q1():
    # 'Charts_Data_M2'!Q1
    value = 2000

@register(Charts_Data_M2)
class R1():
    # 'Charts_Data_M2'!R1
    value = 2001

@register(Charts_Data_M2)
class S1():
    # 'Charts_Data_M2'!S1
    value = 2002

@register(Charts_Data_M2)
class T1():
    # 'Charts_Data_M2'!T1
    value = 2003

@register(Charts_Data_M2)
class U1():
    # 'Charts_Data_M2'!U1
    value = 2004

@register(Charts_Data_M2)
class V1():
    # 'Charts_Data_M2'!V1
    value = 2005

@register(Charts_Data_M2)
class W1():
    # 'Charts_Data_M2'!W1
    value = 2006

@register(Charts_Data_M2)
class X1():
    # 'Charts_Data_M2'!X1
    value = 2007

@register(Charts_Data_M2)
class Y1():
    # 'Charts_Data_M2'!Y1
    value = 2008

@register(Charts_Data_M2)
class Z1():
    # 'Charts_Data_M2'!Z1
    value = 2009

@register(Charts_Data_M2)
class AA1():
    # 'Charts_Data_M2'!AA1
    value = 2010

@register(Charts_Data_M2)
class AB1():
    # 'Charts_Data_M2'!AB1
    value = 2011

@register(Charts_Data_M2)
class AC1():
    # 'Charts_Data_M2'!AC1
    value = 2012

@register(Charts_Data_M2)
class AD1():
    # 'Charts_Data_M2'!AD1
    value = 2013

@register(Charts_Data_M2)
class AE1():
    # 'Charts_Data_M2'!AE1
    value = 2014

@register(Charts_Data_M2)
class AF1():
    # 'Charts_Data_M2'!AF1
    value = 2015

@register(Charts_Data_M2)
class AG1():
    # 'Charts_Data_M2'!AG1
    value = 2016

@register(Charts_Data_M2)
class AH1():
    # 'Charts_Data_M2'!AH1
    value = 2017

@register(Charts_Data_M2)
class AI1():
    # 'Charts_Data_M2'!AI1
    value = 2018

@register(Charts_Data_M2)
class AJ1():
    # 'Charts_Data_M2'!AJ1
    value = 2019

@register(Charts_Data_M2)
class AK1():
    # 'Charts_Data_M2'!AK1
    value = 2020

@register(Charts_Data_M2)
class AL1():
    # 'Charts_Data_M2'!AL1
    value = 2021

@register(Charts_Data_M2)
class AM1():
    # 'Charts_Data_M2'!AM1
    value = 2022

@register(Charts_Data_M2)
class AN1():
    # 'Charts_Data_M2'!AN1
    value = 2023

@register(Charts_Data_M2)
class AO1():
    # 'Charts_Data_M2'!AO1
    value = 2024

@register(Charts_Data_M2)
class AP1():
    # 'Charts_Data_M2'!AP1
    value = 2025

@register(Charts_Data_M2)
class AQ1():
    # 'Charts_Data_M2'!AQ1
    value = 2026

@register(Charts_Data_M2)
class AR1():
    # 'Charts_Data_M2'!AR1
    value = 2027

@register(Charts_Data_M2)
class AS1():
    # 'Charts_Data_M2'!AS1
    value = 2028

@register(Charts_Data_M2)
class AT1():
    # 'Charts_Data_M2'!AT1
    value = 2029

@register(Charts_Data_M2)
class AU1():
    # 'Charts_Data_M2'!AU1
    value = 2030

@register(Charts_Data_M2)
class A2():
    # 'Charts_Data_M2'!A2
    value = "Graph Titles"

@register(Charts_Data_M2)
class B2():
    # 'Charts_Data_M2'!B2
    value = 2010
    formula = "=VLOOKUP('Charts M2'!B2,'Charts Interactive LookupTables'!G:I,3,FALSE)"
    @eval_fn
    def B2():
        b2_1 = Charts_M2.B2()
        range_1 = Charts_Interactive_LookupTables(7, 0, 9, 0)
        var_1 = VLOOKUP(b2_1, range_1, 3, "FALSE")
        return var_1

@register(Charts_Data_M2)
class C2():
    # 'Charts_Data_M2'!C2
    value = "Expenditures on     Residual Fuel Oil (Foreign)"
    formula = '''="Expenditures on "&VLOOKUP('Charts M2'!$B$3,'Charts Interactive LookupTables'!G:I,2,FALSE)'''
    @eval_fn
    def C2():
        b3_1 = Charts_M2.B3()
        range_1 = Charts_Interactive_LookupTables(7, 0, 9, 0)
        var_1 = VLOOKUP(b3_1, range_1, 2, "FALSE")
        var_2 = concat("Expenditures on ", var_1)
        return var_2

@register(Charts_Data_M2)
class F2():
    # 'Charts_Data_M2'!F2
    value = "Notes"

@register(Charts_Data_M2)
class C3():
    # 'Charts_Data_M2'!C3
    value = "Expenditures per Fuel Source in 2010"
    formula = '''="Expenditures per Fuel Source in "&B2'''
    @eval_fn
    def C3():
        b2_1 = Charts_Data_M2.B2()
        var_1 = concat("Expenditures per Fuel Source in ", b2_1)
        return var_1

@register(Charts_Data_M2)
class F3():
    # 'Charts_Data_M2'!F3
    value = "Notes"

@register(Charts_Data_M2)
class A4():
    # 'Charts_Data_M2'!A4
    value = "Graph Inputs (Bottom Line)"

@register(Charts_Data_M2)
class C4():
    # 'Charts_Data_M2'!C4
    value = "Expenditures on All fuel Purchases"

@register(Charts_Data_M2)
class E4():
    # 'Charts_Data_M2'!E4
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F4():
    # 'Charts_Data_M2'!F4
    value = "Notes"

@register(Charts_Data_M2)
class G4():
    # 'Charts_Data_M2'!G4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!G5),'Dashboard M2 Annual'!G5<1),NA(),'Dashboard M2 Annual'!G5/1000000)"
    @eval_fn
    def G4():
        g5_1 = Dashboard_M2_Annual.G5()
        var_1 = ISERROR(g5_1)
        g5_2 = Dashboard_M2_Annual.G5()
        var_2 = lessthan(g5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        g5_3 = Dashboard_M2_Annual.G5()
        var_5 = divide(g5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class H4():
    # 'Charts_Data_M2'!H4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!H5),'Dashboard M2 Annual'!H5<1),NA(),'Dashboard M2 Annual'!H5/1000000)"
    @eval_fn
    def H4():
        h5_1 = Dashboard_M2_Annual.H5()
        var_1 = ISERROR(h5_1)
        h5_2 = Dashboard_M2_Annual.H5()
        var_2 = lessthan(h5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        h5_3 = Dashboard_M2_Annual.H5()
        var_5 = divide(h5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class I4():
    # 'Charts_Data_M2'!I4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!I5),'Dashboard M2 Annual'!I5<1),NA(),'Dashboard M2 Annual'!I5/1000000)"
    @eval_fn
    def I4():
        i5_1 = Dashboard_M2_Annual.I5()
        var_1 = ISERROR(i5_1)
        i5_2 = Dashboard_M2_Annual.I5()
        var_2 = lessthan(i5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        i5_3 = Dashboard_M2_Annual.I5()
        var_5 = divide(i5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class J4():
    # 'Charts_Data_M2'!J4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!J5),'Dashboard M2 Annual'!J5<1),NA(),'Dashboard M2 Annual'!J5/1000000)"
    @eval_fn
    def J4():
        j5_1 = Dashboard_M2_Annual.J5()
        var_1 = ISERROR(j5_1)
        j5_2 = Dashboard_M2_Annual.J5()
        var_2 = lessthan(j5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        j5_3 = Dashboard_M2_Annual.J5()
        var_5 = divide(j5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class K4():
    # 'Charts_Data_M2'!K4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!K5),'Dashboard M2 Annual'!K5<1),NA(),'Dashboard M2 Annual'!K5/1000000)"
    @eval_fn
    def K4():
        k5_1 = Dashboard_M2_Annual.K5()
        var_1 = ISERROR(k5_1)
        k5_2 = Dashboard_M2_Annual.K5()
        var_2 = lessthan(k5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        k5_3 = Dashboard_M2_Annual.K5()
        var_5 = divide(k5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class L4():
    # 'Charts_Data_M2'!L4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!L5),'Dashboard M2 Annual'!L5<1),NA(),'Dashboard M2 Annual'!L5/1000000)"
    @eval_fn
    def L4():
        l5_1 = Dashboard_M2_Annual.L5()
        var_1 = ISERROR(l5_1)
        l5_2 = Dashboard_M2_Annual.L5()
        var_2 = lessthan(l5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        l5_3 = Dashboard_M2_Annual.L5()
        var_5 = divide(l5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class M4():
    # 'Charts_Data_M2'!M4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!M5),'Dashboard M2 Annual'!M5<1),NA(),'Dashboard M2 Annual'!M5/1000000)"
    @eval_fn
    def M4():
        m5_1 = Dashboard_M2_Annual.M5()
        var_1 = ISERROR(m5_1)
        m5_2 = Dashboard_M2_Annual.M5()
        var_2 = lessthan(m5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        m5_3 = Dashboard_M2_Annual.M5()
        var_5 = divide(m5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class N4():
    # 'Charts_Data_M2'!N4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!N5),'Dashboard M2 Annual'!N5<1),NA(),'Dashboard M2 Annual'!N5/1000000)"
    @eval_fn
    def N4():
        n5_1 = Dashboard_M2_Annual.N5()
        var_1 = ISERROR(n5_1)
        n5_2 = Dashboard_M2_Annual.N5()
        var_2 = lessthan(n5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        n5_3 = Dashboard_M2_Annual.N5()
        var_5 = divide(n5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class O4():
    # 'Charts_Data_M2'!O4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!O5),'Dashboard M2 Annual'!O5<1),NA(),'Dashboard M2 Annual'!O5/1000000)"
    @eval_fn
    def O4():
        o5_1 = Dashboard_M2_Annual.O5()
        var_1 = ISERROR(o5_1)
        o5_2 = Dashboard_M2_Annual.O5()
        var_2 = lessthan(o5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        o5_3 = Dashboard_M2_Annual.O5()
        var_5 = divide(o5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class P4():
    # 'Charts_Data_M2'!P4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!P5),'Dashboard M2 Annual'!P5<1),NA(),'Dashboard M2 Annual'!P5/1000000)"
    @eval_fn
    def P4():
        p5_1 = Dashboard_M2_Annual.P5()
        var_1 = ISERROR(p5_1)
        p5_2 = Dashboard_M2_Annual.P5()
        var_2 = lessthan(p5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        p5_3 = Dashboard_M2_Annual.P5()
        var_5 = divide(p5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class Q4():
    # 'Charts_Data_M2'!Q4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!Q5),'Dashboard M2 Annual'!Q5<1),NA(),'Dashboard M2 Annual'!Q5/1000000)"
    @eval_fn
    def Q4():
        q5_1 = Dashboard_M2_Annual.Q5()
        var_1 = ISERROR(q5_1)
        q5_2 = Dashboard_M2_Annual.Q5()
        var_2 = lessthan(q5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        q5_3 = Dashboard_M2_Annual.Q5()
        var_5 = divide(q5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class R4():
    # 'Charts_Data_M2'!R4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!R5),'Dashboard M2 Annual'!R5<1),NA(),'Dashboard M2 Annual'!R5/1000000)"
    @eval_fn
    def R4():
        r5_1 = Dashboard_M2_Annual.R5()
        var_1 = ISERROR(r5_1)
        r5_2 = Dashboard_M2_Annual.R5()
        var_2 = lessthan(r5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        r5_3 = Dashboard_M2_Annual.R5()
        var_5 = divide(r5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class S4():
    # 'Charts_Data_M2'!S4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!S5),'Dashboard M2 Annual'!S5<1),NA(),'Dashboard M2 Annual'!S5/1000000)"
    @eval_fn
    def S4():
        s5_1 = Dashboard_M2_Annual.S5()
        var_1 = ISERROR(s5_1)
        s5_2 = Dashboard_M2_Annual.S5()
        var_2 = lessthan(s5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        s5_3 = Dashboard_M2_Annual.S5()
        var_5 = divide(s5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class T4():
    # 'Charts_Data_M2'!T4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!T5),'Dashboard M2 Annual'!T5<1),NA(),'Dashboard M2 Annual'!T5/1000000)"
    @eval_fn
    def T4():
        t5_1 = Dashboard_M2_Annual.T5()
        var_1 = ISERROR(t5_1)
        t5_2 = Dashboard_M2_Annual.T5()
        var_2 = lessthan(t5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        t5_3 = Dashboard_M2_Annual.T5()
        var_5 = divide(t5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class U4():
    # 'Charts_Data_M2'!U4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!U5),'Dashboard M2 Annual'!U5<1),NA(),'Dashboard M2 Annual'!U5/1000000)"
    @eval_fn
    def U4():
        u5_1 = Dashboard_M2_Annual.U5()
        var_1 = ISERROR(u5_1)
        u5_2 = Dashboard_M2_Annual.U5()
        var_2 = lessthan(u5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        u5_3 = Dashboard_M2_Annual.U5()
        var_5 = divide(u5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class V4():
    # 'Charts_Data_M2'!V4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!V5),'Dashboard M2 Annual'!V5<1),NA(),'Dashboard M2 Annual'!V5/1000000)"
    @eval_fn
    def V4():
        v5_1 = Dashboard_M2_Annual.V5()
        var_1 = ISERROR(v5_1)
        v5_2 = Dashboard_M2_Annual.V5()
        var_2 = lessthan(v5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        v5_3 = Dashboard_M2_Annual.V5()
        var_5 = divide(v5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class W4():
    # 'Charts_Data_M2'!W4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!W5),'Dashboard M2 Annual'!W5<1),NA(),'Dashboard M2 Annual'!W5/1000000)"
    @eval_fn
    def W4():
        w5_1 = Dashboard_M2_Annual.W5()
        var_1 = ISERROR(w5_1)
        w5_2 = Dashboard_M2_Annual.W5()
        var_2 = lessthan(w5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        w5_3 = Dashboard_M2_Annual.W5()
        var_5 = divide(w5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class X4():
    # 'Charts_Data_M2'!X4
    value = 4051.82323413
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!X5),'Dashboard M2 Annual'!X5<1),NA(),'Dashboard M2 Annual'!X5/1000000)"
    @eval_fn
    def X4():
        x5_1 = Dashboard_M2_Annual.X5()
        var_1 = ISERROR(x5_1)
        x5_2 = Dashboard_M2_Annual.X5()
        var_2 = lessthan(x5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        x5_3 = Dashboard_M2_Annual.X5()
        var_5 = divide(x5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class Y4():
    # 'Charts_Data_M2'!Y4
    value = 4783.61079181
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!Y5),'Dashboard M2 Annual'!Y5<1),NA(),'Dashboard M2 Annual'!Y5/1000000)"
    @eval_fn
    def Y4():
        y5_1 = Dashboard_M2_Annual.Y5()
        var_1 = ISERROR(y5_1)
        y5_2 = Dashboard_M2_Annual.Y5()
        var_2 = lessthan(y5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        y5_3 = Dashboard_M2_Annual.Y5()
        var_5 = divide(y5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class Z4():
    # 'Charts_Data_M2'!Z4
    value = 2800.57904975
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!Z5),'Dashboard M2 Annual'!Z5<1),NA(),'Dashboard M2 Annual'!Z5/1000000)"
    @eval_fn
    def Z4():
        z5_1 = Dashboard_M2_Annual.Z5()
        var_1 = ISERROR(z5_1)
        z5_2 = Dashboard_M2_Annual.Z5()
        var_2 = lessthan(z5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        z5_3 = Dashboard_M2_Annual.Z5()
        var_5 = divide(z5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AA4():
    # 'Charts_Data_M2'!AA4
    value = 3832.72952
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AA5),'Dashboard M2 Annual'!AA5<1),NA(),'Dashboard M2 Annual'!AA5/1000000)"
    @eval_fn
    def AA4():
        aa5_1 = Dashboard_M2_Annual.AA5()
        var_1 = ISERROR(aa5_1)
        aa5_2 = Dashboard_M2_Annual.AA5()
        var_2 = lessthan(aa5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        aa5_3 = Dashboard_M2_Annual.AA5()
        var_5 = divide(aa5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AB4():
    # 'Charts_Data_M2'!AB4
    value = 5332.901305
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AB5),'Dashboard M2 Annual'!AB5<1),NA(),'Dashboard M2 Annual'!AB5/1000000)"
    @eval_fn
    def AB4():
        ab5_1 = Dashboard_M2_Annual.AB5()
        var_1 = ISERROR(ab5_1)
        ab5_2 = Dashboard_M2_Annual.AB5()
        var_2 = lessthan(ab5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ab5_3 = Dashboard_M2_Annual.AB5()
        var_5 = divide(ab5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AC4():
    # 'Charts_Data_M2'!AC4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AC5),'Dashboard M2 Annual'!AC5<1),NA(),'Dashboard M2 Annual'!AC5/1000000)"
    @eval_fn
    def AC4():
        ac5_1 = Dashboard_M2_Annual.AC5()
        var_1 = ISERROR(ac5_1)
        ac5_2 = Dashboard_M2_Annual.AC5()
        var_2 = lessthan(ac5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ac5_3 = Dashboard_M2_Annual.AC5()
        var_5 = divide(ac5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AD4():
    # 'Charts_Data_M2'!AD4
    value = 4884.764362
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AD5),'Dashboard M2 Annual'!AD5<1),NA(),'Dashboard M2 Annual'!AD5/1000000)"
    @eval_fn
    def AD4():
        ad5_1 = Dashboard_M2_Annual.AD5()
        var_1 = ISERROR(ad5_1)
        ad5_2 = Dashboard_M2_Annual.AD5()
        var_2 = lessthan(ad5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ad5_3 = Dashboard_M2_Annual.AD5()
        var_5 = divide(ad5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AE4():
    # 'Charts_Data_M2'!AE4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AE5),'Dashboard M2 Annual'!AE5<1),NA(),'Dashboard M2 Annual'!AE5/1000000)"
    @eval_fn
    def AE4():
        ae5_1 = Dashboard_M2_Annual.AE5()
        var_1 = ISERROR(ae5_1)
        ae5_2 = Dashboard_M2_Annual.AE5()
        var_2 = lessthan(ae5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ae5_3 = Dashboard_M2_Annual.AE5()
        var_5 = divide(ae5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AF4():
    # 'Charts_Data_M2'!AF4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AF5),'Dashboard M2 Annual'!AF5<1),NA(),'Dashboard M2 Annual'!AF5/1000000)"
    @eval_fn
    def AF4():
        af5_1 = Dashboard_M2_Annual.AF5()
        var_1 = ISERROR(af5_1)
        af5_2 = Dashboard_M2_Annual.AF5()
        var_2 = lessthan(af5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        af5_3 = Dashboard_M2_Annual.AF5()
        var_5 = divide(af5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AG4():
    # 'Charts_Data_M2'!AG4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AG5),'Dashboard M2 Annual'!AG5<1),NA(),'Dashboard M2 Annual'!AG5/1000000)"
    @eval_fn
    def AG4():
        ag5_1 = Dashboard_M2_Annual.AG5()
        var_1 = ISERROR(ag5_1)
        ag5_2 = Dashboard_M2_Annual.AG5()
        var_2 = lessthan(ag5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ag5_3 = Dashboard_M2_Annual.AG5()
        var_5 = divide(ag5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AH4():
    # 'Charts_Data_M2'!AH4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AH5),'Dashboard M2 Annual'!AH5<1),NA(),'Dashboard M2 Annual'!AH5/1000000)"
    @eval_fn
    def AH4():
        ah5_1 = Dashboard_M2_Annual.AH5()
        var_1 = ISERROR(ah5_1)
        ah5_2 = Dashboard_M2_Annual.AH5()
        var_2 = lessthan(ah5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ah5_3 = Dashboard_M2_Annual.AH5()
        var_5 = divide(ah5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AI4():
    # 'Charts_Data_M2'!AI4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AI5),'Dashboard M2 Annual'!AI5<1),NA(),'Dashboard M2 Annual'!AI5/1000000)"
    @eval_fn
    def AI4():
        ai5_1 = Dashboard_M2_Annual.AI5()
        var_1 = ISERROR(ai5_1)
        ai5_2 = Dashboard_M2_Annual.AI5()
        var_2 = lessthan(ai5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ai5_3 = Dashboard_M2_Annual.AI5()
        var_5 = divide(ai5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AJ4():
    # 'Charts_Data_M2'!AJ4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AJ5),'Dashboard M2 Annual'!AJ5<1),NA(),'Dashboard M2 Annual'!AJ5/1000000)"
    @eval_fn
    def AJ4():
        aj5_1 = Dashboard_M2_Annual.AJ5()
        var_1 = ISERROR(aj5_1)
        aj5_2 = Dashboard_M2_Annual.AJ5()
        var_2 = lessthan(aj5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        aj5_3 = Dashboard_M2_Annual.AJ5()
        var_5 = divide(aj5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AK4():
    # 'Charts_Data_M2'!AK4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AK5),'Dashboard M2 Annual'!AK5<1),NA(),'Dashboard M2 Annual'!AK5/1000000)"
    @eval_fn
    def AK4():
        ak5_1 = Dashboard_M2_Annual.AK5()
        var_1 = ISERROR(ak5_1)
        ak5_2 = Dashboard_M2_Annual.AK5()
        var_2 = lessthan(ak5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ak5_3 = Dashboard_M2_Annual.AK5()
        var_5 = divide(ak5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AL4():
    # 'Charts_Data_M2'!AL4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AL5),'Dashboard M2 Annual'!AL5<1),NA(),'Dashboard M2 Annual'!AL5/1000000)"
    @eval_fn
    def AL4():
        al5_1 = Dashboard_M2_Annual.AL5()
        var_1 = ISERROR(al5_1)
        al5_2 = Dashboard_M2_Annual.AL5()
        var_2 = lessthan(al5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        al5_3 = Dashboard_M2_Annual.AL5()
        var_5 = divide(al5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AM4():
    # 'Charts_Data_M2'!AM4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AM5),'Dashboard M2 Annual'!AM5<1),NA(),'Dashboard M2 Annual'!AM5/1000000)"
    @eval_fn
    def AM4():
        am5_1 = Dashboard_M2_Annual.AM5()
        var_1 = ISERROR(am5_1)
        am5_2 = Dashboard_M2_Annual.AM5()
        var_2 = lessthan(am5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        am5_3 = Dashboard_M2_Annual.AM5()
        var_5 = divide(am5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AN4():
    # 'Charts_Data_M2'!AN4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AN5),'Dashboard M2 Annual'!AN5<1),NA(),'Dashboard M2 Annual'!AN5/1000000)"
    @eval_fn
    def AN4():
        an5_1 = Dashboard_M2_Annual.AN5()
        var_1 = ISERROR(an5_1)
        an5_2 = Dashboard_M2_Annual.AN5()
        var_2 = lessthan(an5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        an5_3 = Dashboard_M2_Annual.AN5()
        var_5 = divide(an5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AO4():
    # 'Charts_Data_M2'!AO4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AO5),'Dashboard M2 Annual'!AO5<1),NA(),'Dashboard M2 Annual'!AO5/1000000)"
    @eval_fn
    def AO4():
        ao5_1 = Dashboard_M2_Annual.AO5()
        var_1 = ISERROR(ao5_1)
        ao5_2 = Dashboard_M2_Annual.AO5()
        var_2 = lessthan(ao5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ao5_3 = Dashboard_M2_Annual.AO5()
        var_5 = divide(ao5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AP4():
    # 'Charts_Data_M2'!AP4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AP5),'Dashboard M2 Annual'!AP5<1),NA(),'Dashboard M2 Annual'!AP5/1000000)"
    @eval_fn
    def AP4():
        ap5_1 = Dashboard_M2_Annual.AP5()
        var_1 = ISERROR(ap5_1)
        ap5_2 = Dashboard_M2_Annual.AP5()
        var_2 = lessthan(ap5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ap5_3 = Dashboard_M2_Annual.AP5()
        var_5 = divide(ap5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AQ4():
    # 'Charts_Data_M2'!AQ4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AQ5),'Dashboard M2 Annual'!AQ5<1),NA(),'Dashboard M2 Annual'!AQ5/1000000)"
    @eval_fn
    def AQ4():
        aq5_1 = Dashboard_M2_Annual.AQ5()
        var_1 = ISERROR(aq5_1)
        aq5_2 = Dashboard_M2_Annual.AQ5()
        var_2 = lessthan(aq5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        aq5_3 = Dashboard_M2_Annual.AQ5()
        var_5 = divide(aq5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AR4():
    # 'Charts_Data_M2'!AR4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AR5),'Dashboard M2 Annual'!AR5<1),NA(),'Dashboard M2 Annual'!AR5/1000000)"
    @eval_fn
    def AR4():
        ar5_1 = Dashboard_M2_Annual.AR5()
        var_1 = ISERROR(ar5_1)
        ar5_2 = Dashboard_M2_Annual.AR5()
        var_2 = lessthan(ar5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ar5_3 = Dashboard_M2_Annual.AR5()
        var_5 = divide(ar5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AS4():
    # 'Charts_Data_M2'!AS4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AS5),'Dashboard M2 Annual'!AS5<1),NA(),'Dashboard M2 Annual'!AS5/1000000)"
    @eval_fn
    def AS4():
        as5_1 = Dashboard_M2_Annual.AS5()
        var_1 = ISERROR(as5_1)
        as5_2 = Dashboard_M2_Annual.AS5()
        var_2 = lessthan(as5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        as5_3 = Dashboard_M2_Annual.AS5()
        var_5 = divide(as5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AT4():
    # 'Charts_Data_M2'!AT4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AT5),'Dashboard M2 Annual'!AT5<1),NA(),'Dashboard M2 Annual'!AT5/1000000)"
    @eval_fn
    def AT4():
        at5_1 = Dashboard_M2_Annual.AT5()
        var_1 = ISERROR(at5_1)
        at5_2 = Dashboard_M2_Annual.AT5()
        var_2 = lessthan(at5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        at5_3 = Dashboard_M2_Annual.AT5()
        var_5 = divide(at5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class AU4():
    # 'Charts_Data_M2'!AU4
    value = "#N/A"
    formula = "=IF(OR(ISERROR('Dashboard M2 Annual'!AU5),'Dashboard M2 Annual'!AU5<1),NA(),'Dashboard M2 Annual'!AU5/1000000)"
    @eval_fn
    def AU4():
        au5_1 = Dashboard_M2_Annual.AU5()
        var_1 = ISERROR(au5_1)
        au5_2 = Dashboard_M2_Annual.AU5()
        var_2 = lessthan(au5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        au5_3 = Dashboard_M2_Annual.AU5()
        var_5 = divide(au5_3, 1000000)
        var_6 = IF(var_3, var_4, var_5)
        return var_6

@register(Charts_Data_M2)
class A5():
    # 'Charts_Data_M2'!A5
    value = "Graph Inputs (Top Line)"

@register(Charts_Data_M2)
class C5():
    # 'Charts_Data_M2'!C5
    value = "    Residual Fuel Oil (Foreign)"
    formula = "=VLOOKUP('Charts M2'!B3,'Charts Interactive LookupTables'!G:H,2,FALSE)"
    @eval_fn
    def C5():
        b3_1 = Charts_M2.B3()
        range_1 = Charts_Interactive_LookupTables(7, 0, 8, 0)
        var_1 = VLOOKUP(b3_1, range_1, 2, "FALSE")
        return var_1

@register(Charts_Data_M2)
class E5():
    # 'Charts_Data_M2'!E5
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F5():
    # 'Charts_Data_M2'!F5
    value = "Notes"

@register(Charts_Data_M2)
class G5():
    # 'Charts_Data_M2'!G5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!G2,FALSE)/1000000"
    @eval_fn
    def G5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        g2_1 = Dashboard_M2_Annual.G2()
        var_1 = VLOOKUP(c5_1, range_1, g2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class H5():
    # 'Charts_Data_M2'!H5
    value = 48.997662
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!H2,FALSE)/1000000"
    @eval_fn
    def H5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        h2_1 = Dashboard_M2_Annual.H2()
        var_1 = VLOOKUP(c5_1, range_1, h2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class I5():
    # 'Charts_Data_M2'!I5
    value = 28.029582
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!I2,FALSE)/1000000"
    @eval_fn
    def I5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        i2_1 = Dashboard_M2_Annual.I2()
        var_1 = VLOOKUP(c5_1, range_1, i2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class J5():
    # 'Charts_Data_M2'!J5
    value = 15.601992
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!J2,FALSE)/1000000"
    @eval_fn
    def J5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        j2_1 = Dashboard_M2_Annual.J2()
        var_1 = VLOOKUP(c5_1, range_1, j2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class K5():
    # 'Charts_Data_M2'!K5
    value = 1.3818
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!K2,FALSE)/1000000"
    @eval_fn
    def K5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        k2_1 = Dashboard_M2_Annual.K2()
        var_1 = VLOOKUP(c5_1, range_1, k2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class L5():
    # 'Charts_Data_M2'!L5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!L2,FALSE)/1000000"
    @eval_fn
    def L5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        l2_1 = Dashboard_M2_Annual.L2()
        var_1 = VLOOKUP(c5_1, range_1, l2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class M5():
    # 'Charts_Data_M2'!M5
    value = 2.7804
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!M2,FALSE)/1000000"
    @eval_fn
    def M5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        m2_1 = Dashboard_M2_Annual.M2()
        var_1 = VLOOKUP(c5_1, range_1, m2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class N5():
    # 'Charts_Data_M2'!N5
    value = 15.213618
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!N2,FALSE)/1000000"
    @eval_fn
    def N5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        n2_1 = Dashboard_M2_Annual.N2()
        var_1 = VLOOKUP(c5_1, range_1, n2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class O5():
    # 'Charts_Data_M2'!O5
    value = 13.356336
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!O2,FALSE)/1000000"
    @eval_fn
    def O5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        o2_1 = Dashboard_M2_Annual.O2()
        var_1 = VLOOKUP(c5_1, range_1, o2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class P5():
    # 'Charts_Data_M2'!P5
    value = 16.721166
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!P2,FALSE)/1000000"
    @eval_fn
    def P5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        p2_1 = Dashboard_M2_Annual.P2()
        var_1 = VLOOKUP(c5_1, range_1, p2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class Q5():
    # 'Charts_Data_M2'!Q5
    value = 19.462212
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!Q2,FALSE)/1000000"
    @eval_fn
    def Q5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        q2_1 = Dashboard_M2_Annual.Q2()
        var_1 = VLOOKUP(c5_1, range_1, q2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class R5():
    # 'Charts_Data_M2'!R5
    value = 19.921566
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!R2,FALSE)/1000000"
    @eval_fn
    def R5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        r2_1 = Dashboard_M2_Annual.R2()
        var_1 = VLOOKUP(c5_1, range_1, r2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class S5():
    # 'Charts_Data_M2'!S5
    value = 8.112636
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!S2,FALSE)/1000000"
    @eval_fn
    def S5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        s2_1 = Dashboard_M2_Annual.S2()
        var_1 = VLOOKUP(c5_1, range_1, s2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class T5():
    # 'Charts_Data_M2'!T5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!T2,FALSE)/1000000"
    @eval_fn
    def T5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        t2_1 = Dashboard_M2_Annual.T2()
        var_1 = VLOOKUP(c5_1, range_1, t2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class U5():
    # 'Charts_Data_M2'!U5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!U2,FALSE)/1000000"
    @eval_fn
    def U5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        u2_1 = Dashboard_M2_Annual.U2()
        var_1 = VLOOKUP(c5_1, range_1, u2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class V5():
    # 'Charts_Data_M2'!V5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!V2,FALSE)/1000000"
    @eval_fn
    def V5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        v2_1 = Dashboard_M2_Annual.V2()
        var_1 = VLOOKUP(c5_1, range_1, v2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class W5():
    # 'Charts_Data_M2'!W5
    value = 15.154608
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!W2,FALSE)/1000000"
    @eval_fn
    def W5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        w2_1 = Dashboard_M2_Annual.W2()
        var_1 = VLOOKUP(c5_1, range_1, w2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class X5():
    # 'Charts_Data_M2'!X5
    value = 28.199052
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!X2,FALSE)/1000000"
    @eval_fn
    def X5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        x2_1 = Dashboard_M2_Annual.X2()
        var_1 = VLOOKUP(c5_1, range_1, x2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class Y5():
    # 'Charts_Data_M2'!Y5
    value = 29.491896
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!Y2,FALSE)/1000000"
    @eval_fn
    def Y5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        y2_1 = Dashboard_M2_Annual.Y2()
        var_1 = VLOOKUP(c5_1, range_1, y2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class Z5():
    # 'Charts_Data_M2'!Z5
    value = 17.793888
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!Z2,FALSE)/1000000"
    @eval_fn
    def Z5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        z2_1 = Dashboard_M2_Annual.Z2()
        var_1 = VLOOKUP(c5_1, range_1, z2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AA5():
    # 'Charts_Data_M2'!AA5
    value = 3.033576
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AA2,FALSE)/1000000"
    @eval_fn
    def AA5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        aa2_1 = Dashboard_M2_Annual.AA2()
        var_1 = VLOOKUP(c5_1, range_1, aa2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AB5():
    # 'Charts_Data_M2'!AB5
    value = 20.320146
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AB2,FALSE)/1000000"
    @eval_fn
    def AB5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        ab2_1 = Dashboard_M2_Annual.AB2()
        var_1 = VLOOKUP(c5_1, range_1, ab2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AC5():
    # 'Charts_Data_M2'!AC5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AC2,FALSE)/1000000"
    @eval_fn
    def AC5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        ac2_1 = Dashboard_M2_Annual.AC2()
        var_1 = VLOOKUP(c5_1, range_1, ac2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AD5():
    # 'Charts_Data_M2'!AD5
    value = "#N/A"
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AD2,FALSE)/1000000"
    @eval_fn
    def AD5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        ad2_1 = Dashboard_M2_Annual.AD2()
        var_1 = VLOOKUP(c5_1, range_1, ad2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AE5():
    # 'Charts_Data_M2'!AE5
    value = 161.245728
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AE2,FALSE)/1000000"
    @eval_fn
    def AE5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        ae2_1 = Dashboard_M2_Annual.AE2()
        var_1 = VLOOKUP(c5_1, range_1, ae2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AF5():
    # 'Charts_Data_M2'!AF5
    value = 47.909316
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AF2,FALSE)/1000000"
    @eval_fn
    def AF5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        af2_1 = Dashboard_M2_Annual.AF2()
        var_1 = VLOOKUP(c5_1, range_1, af2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AG5():
    # 'Charts_Data_M2'!AG5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AG2,FALSE)/1000000"
    @eval_fn
    def AG5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        ag2_1 = Dashboard_M2_Annual.AG2()
        var_1 = VLOOKUP(c5_1, range_1, ag2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AH5():
    # 'Charts_Data_M2'!AH5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AH2,FALSE)/1000000"
    @eval_fn
    def AH5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        ah2_1 = Dashboard_M2_Annual.AH2()
        var_1 = VLOOKUP(c5_1, range_1, ah2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AI5():
    # 'Charts_Data_M2'!AI5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AI2,FALSE)/1000000"
    @eval_fn
    def AI5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        ai2_1 = Dashboard_M2_Annual.AI2()
        var_1 = VLOOKUP(c5_1, range_1, ai2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AJ5():
    # 'Charts_Data_M2'!AJ5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AJ2,FALSE)/1000000"
    @eval_fn
    def AJ5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        aj2_1 = Dashboard_M2_Annual.AJ2()
        var_1 = VLOOKUP(c5_1, range_1, aj2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AK5():
    # 'Charts_Data_M2'!AK5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AK$29,'Dashboard M2 Annual'!AK2,FALSE)/1000000"
    @eval_fn
    def AK5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 37, 29)
        ak2_1 = Dashboard_M2_Annual.AK2()
        var_1 = VLOOKUP(c5_1, range_1, ak2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AL5():
    # 'Charts_Data_M2'!AL5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AU$29,'Dashboard M2 Annual'!AL2,FALSE)/1000000"
    @eval_fn
    def AL5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 47, 29)
        al2_1 = Dashboard_M2_Annual.AL2()
        var_1 = VLOOKUP(c5_1, range_1, al2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AM5():
    # 'Charts_Data_M2'!AM5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AU$29,'Dashboard M2 Annual'!AM2,FALSE)/1000000"
    @eval_fn
    def AM5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 47, 29)
        am2_1 = Dashboard_M2_Annual.AM2()
        var_1 = VLOOKUP(c5_1, range_1, am2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AN5():
    # 'Charts_Data_M2'!AN5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AU$29,'Dashboard M2 Annual'!AN2,FALSE)/1000000"
    @eval_fn
    def AN5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 47, 29)
        an2_1 = Dashboard_M2_Annual.AN2()
        var_1 = VLOOKUP(c5_1, range_1, an2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AO5():
    # 'Charts_Data_M2'!AO5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AU$29,'Dashboard M2 Annual'!AO2,FALSE)/1000000"
    @eval_fn
    def AO5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 47, 29)
        ao2_1 = Dashboard_M2_Annual.AO2()
        var_1 = VLOOKUP(c5_1, range_1, ao2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AP5():
    # 'Charts_Data_M2'!AP5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AU$29,'Dashboard M2 Annual'!AP2,FALSE)/1000000"
    @eval_fn
    def AP5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 47, 29)
        ap2_1 = Dashboard_M2_Annual.AP2()
        var_1 = VLOOKUP(c5_1, range_1, ap2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AQ5():
    # 'Charts_Data_M2'!AQ5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AU$29,'Dashboard M2 Annual'!AQ2,FALSE)/1000000"
    @eval_fn
    def AQ5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 47, 29)
        aq2_1 = Dashboard_M2_Annual.AQ2()
        var_1 = VLOOKUP(c5_1, range_1, aq2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AR5():
    # 'Charts_Data_M2'!AR5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AU$29,'Dashboard M2 Annual'!AR2,FALSE)/1000000"
    @eval_fn
    def AR5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 47, 29)
        ar2_1 = Dashboard_M2_Annual.AR2()
        var_1 = VLOOKUP(c5_1, range_1, ar2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AS5():
    # 'Charts_Data_M2'!AS5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AU$29,'Dashboard M2 Annual'!AS2,FALSE)/1000000"
    @eval_fn
    def AS5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 47, 29)
        as2_1 = Dashboard_M2_Annual.AS2()
        var_1 = VLOOKUP(c5_1, range_1, as2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AT5():
    # 'Charts_Data_M2'!AT5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AU$29,'Dashboard M2 Annual'!AT2,FALSE)/1000000"
    @eval_fn
    def AT5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 47, 29)
        at2_1 = Dashboard_M2_Annual.AT2()
        var_1 = VLOOKUP(c5_1, range_1, at2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class AU5():
    # 'Charts_Data_M2'!AU5
    value = 0
    formula = "=VLOOKUP($C$5,'Dashboard M2 Annual'!$B$10:$AU$29,'Dashboard M2 Annual'!AU2,FALSE)/1000000"
    @eval_fn
    def AU5():
        c5_1 = Charts_Data_M2.C5()
        range_1 = Dashboard_M2_Annual(2, 10, 47, 29)
        au2_1 = Dashboard_M2_Annual.AU2()
        var_1 = VLOOKUP(c5_1, range_1, au2_1, "FALSE")
        var_2 = divide(var_1, 1000000)
        return var_2

@register(Charts_Data_M2)
class F6():
    # 'Charts_Data_M2'!F6
    value = "Notes"

@register(Charts_Data_M2)
class G6():
    # 'Charts_Data_M2'!G6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(G5),G5<1),NA(),G5)"
    @eval_fn
    def G6():
        g5_1 = Charts_Data_M2.G5()
        var_1 = ISERROR(g5_1)
        g5_2 = Charts_Data_M2.G5()
        var_2 = lessthan(g5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        g5_3 = Charts_Data_M2.G5()
        var_5 = IF(var_3, var_4, g5_3)
        return var_5

@register(Charts_Data_M2)
class H6():
    # 'Charts_Data_M2'!H6
    value = 48.997662
    formula = "=IF(OR(ISERROR(H5),H5<1),NA(),H5)"
    @eval_fn
    def H6():
        h5_1 = Charts_Data_M2.H5()
        var_1 = ISERROR(h5_1)
        h5_2 = Charts_Data_M2.H5()
        var_2 = lessthan(h5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        h5_3 = Charts_Data_M2.H5()
        var_5 = IF(var_3, var_4, h5_3)
        return var_5

@register(Charts_Data_M2)
class I6():
    # 'Charts_Data_M2'!I6
    value = 28.029582
    formula = "=IF(OR(ISERROR(I5),I5<1),NA(),I5)"
    @eval_fn
    def I6():
        i5_1 = Charts_Data_M2.I5()
        var_1 = ISERROR(i5_1)
        i5_2 = Charts_Data_M2.I5()
        var_2 = lessthan(i5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        i5_3 = Charts_Data_M2.I5()
        var_5 = IF(var_3, var_4, i5_3)
        return var_5

@register(Charts_Data_M2)
class J6():
    # 'Charts_Data_M2'!J6
    value = 15.601992
    formula = "=IF(OR(ISERROR(J5),J5<1),NA(),J5)"
    @eval_fn
    def J6():
        j5_1 = Charts_Data_M2.J5()
        var_1 = ISERROR(j5_1)
        j5_2 = Charts_Data_M2.J5()
        var_2 = lessthan(j5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        j5_3 = Charts_Data_M2.J5()
        var_5 = IF(var_3, var_4, j5_3)
        return var_5

@register(Charts_Data_M2)
class K6():
    # 'Charts_Data_M2'!K6
    value = 1.3818
    formula = "=IF(OR(ISERROR(K5),K5<1),NA(),K5)"
    @eval_fn
    def K6():
        k5_1 = Charts_Data_M2.K5()
        var_1 = ISERROR(k5_1)
        k5_2 = Charts_Data_M2.K5()
        var_2 = lessthan(k5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        k5_3 = Charts_Data_M2.K5()
        var_5 = IF(var_3, var_4, k5_3)
        return var_5

@register(Charts_Data_M2)
class L6():
    # 'Charts_Data_M2'!L6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(L5),L5<1),NA(),L5)"
    @eval_fn
    def L6():
        l5_1 = Charts_Data_M2.L5()
        var_1 = ISERROR(l5_1)
        l5_2 = Charts_Data_M2.L5()
        var_2 = lessthan(l5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        l5_3 = Charts_Data_M2.L5()
        var_5 = IF(var_3, var_4, l5_3)
        return var_5

@register(Charts_Data_M2)
class M6():
    # 'Charts_Data_M2'!M6
    value = 2.7804
    formula = "=IF(OR(ISERROR(M5),M5<1),NA(),M5)"
    @eval_fn
    def M6():
        m5_1 = Charts_Data_M2.M5()
        var_1 = ISERROR(m5_1)
        m5_2 = Charts_Data_M2.M5()
        var_2 = lessthan(m5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        m5_3 = Charts_Data_M2.M5()
        var_5 = IF(var_3, var_4, m5_3)
        return var_5

@register(Charts_Data_M2)
class N6():
    # 'Charts_Data_M2'!N6
    value = 15.213618
    formula = "=IF(OR(ISERROR(N5),N5<1),NA(),N5)"
    @eval_fn
    def N6():
        n5_1 = Charts_Data_M2.N5()
        var_1 = ISERROR(n5_1)
        n5_2 = Charts_Data_M2.N5()
        var_2 = lessthan(n5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        n5_3 = Charts_Data_M2.N5()
        var_5 = IF(var_3, var_4, n5_3)
        return var_5

@register(Charts_Data_M2)
class O6():
    # 'Charts_Data_M2'!O6
    value = 13.356336
    formula = "=IF(OR(ISERROR(O5),O5<1),NA(),O5)"
    @eval_fn
    def O6():
        o5_1 = Charts_Data_M2.O5()
        var_1 = ISERROR(o5_1)
        o5_2 = Charts_Data_M2.O5()
        var_2 = lessthan(o5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        o5_3 = Charts_Data_M2.O5()
        var_5 = IF(var_3, var_4, o5_3)
        return var_5

@register(Charts_Data_M2)
class P6():
    # 'Charts_Data_M2'!P6
    value = 16.721166
    formula = "=IF(OR(ISERROR(P5),P5<1),NA(),P5)"
    @eval_fn
    def P6():
        p5_1 = Charts_Data_M2.P5()
        var_1 = ISERROR(p5_1)
        p5_2 = Charts_Data_M2.P5()
        var_2 = lessthan(p5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        p5_3 = Charts_Data_M2.P5()
        var_5 = IF(var_3, var_4, p5_3)
        return var_5

@register(Charts_Data_M2)
class Q6():
    # 'Charts_Data_M2'!Q6
    value = 19.462212
    formula = "=IF(OR(ISERROR(Q5),Q5<1),NA(),Q5)"
    @eval_fn
    def Q6():
        q5_1 = Charts_Data_M2.Q5()
        var_1 = ISERROR(q5_1)
        q5_2 = Charts_Data_M2.Q5()
        var_2 = lessthan(q5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        q5_3 = Charts_Data_M2.Q5()
        var_5 = IF(var_3, var_4, q5_3)
        return var_5

@register(Charts_Data_M2)
class R6():
    # 'Charts_Data_M2'!R6
    value = 19.921566
    formula = "=IF(OR(ISERROR(R5),R5<1),NA(),R5)"
    @eval_fn
    def R6():
        r5_1 = Charts_Data_M2.R5()
        var_1 = ISERROR(r5_1)
        r5_2 = Charts_Data_M2.R5()
        var_2 = lessthan(r5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        r5_3 = Charts_Data_M2.R5()
        var_5 = IF(var_3, var_4, r5_3)
        return var_5

@register(Charts_Data_M2)
class S6():
    # 'Charts_Data_M2'!S6
    value = 8.112636
    formula = "=IF(OR(ISERROR(S5),S5<1),NA(),S5)"
    @eval_fn
    def S6():
        s5_1 = Charts_Data_M2.S5()
        var_1 = ISERROR(s5_1)
        s5_2 = Charts_Data_M2.S5()
        var_2 = lessthan(s5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        s5_3 = Charts_Data_M2.S5()
        var_5 = IF(var_3, var_4, s5_3)
        return var_5

@register(Charts_Data_M2)
class T6():
    # 'Charts_Data_M2'!T6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(T5),T5<1),NA(),T5)"
    @eval_fn
    def T6():
        t5_1 = Charts_Data_M2.T5()
        var_1 = ISERROR(t5_1)
        t5_2 = Charts_Data_M2.T5()
        var_2 = lessthan(t5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        t5_3 = Charts_Data_M2.T5()
        var_5 = IF(var_3, var_4, t5_3)
        return var_5

@register(Charts_Data_M2)
class U6():
    # 'Charts_Data_M2'!U6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(U5),U5<1),NA(),U5)"
    @eval_fn
    def U6():
        u5_1 = Charts_Data_M2.U5()
        var_1 = ISERROR(u5_1)
        u5_2 = Charts_Data_M2.U5()
        var_2 = lessthan(u5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        u5_3 = Charts_Data_M2.U5()
        var_5 = IF(var_3, var_4, u5_3)
        return var_5

@register(Charts_Data_M2)
class V6():
    # 'Charts_Data_M2'!V6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(V5),V5<1),NA(),V5)"
    @eval_fn
    def V6():
        v5_1 = Charts_Data_M2.V5()
        var_1 = ISERROR(v5_1)
        v5_2 = Charts_Data_M2.V5()
        var_2 = lessthan(v5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        v5_3 = Charts_Data_M2.V5()
        var_5 = IF(var_3, var_4, v5_3)
        return var_5

@register(Charts_Data_M2)
class W6():
    # 'Charts_Data_M2'!W6
    value = 15.154608
    formula = "=IF(OR(ISERROR(W5),W5<1),NA(),W5)"
    @eval_fn
    def W6():
        w5_1 = Charts_Data_M2.W5()
        var_1 = ISERROR(w5_1)
        w5_2 = Charts_Data_M2.W5()
        var_2 = lessthan(w5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        w5_3 = Charts_Data_M2.W5()
        var_5 = IF(var_3, var_4, w5_3)
        return var_5

@register(Charts_Data_M2)
class X6():
    # 'Charts_Data_M2'!X6
    value = 28.199052
    formula = "=IF(OR(ISERROR(X5),X5<1),NA(),X5)"
    @eval_fn
    def X6():
        x5_1 = Charts_Data_M2.X5()
        var_1 = ISERROR(x5_1)
        x5_2 = Charts_Data_M2.X5()
        var_2 = lessthan(x5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        x5_3 = Charts_Data_M2.X5()
        var_5 = IF(var_3, var_4, x5_3)
        return var_5

@register(Charts_Data_M2)
class Y6():
    # 'Charts_Data_M2'!Y6
    value = 29.491896
    formula = "=IF(OR(ISERROR(Y5),Y5<1),NA(),Y5)"
    @eval_fn
    def Y6():
        y5_1 = Charts_Data_M2.Y5()
        var_1 = ISERROR(y5_1)
        y5_2 = Charts_Data_M2.Y5()
        var_2 = lessthan(y5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        y5_3 = Charts_Data_M2.Y5()
        var_5 = IF(var_3, var_4, y5_3)
        return var_5

@register(Charts_Data_M2)
class Z6():
    # 'Charts_Data_M2'!Z6
    value = 17.793888
    formula = "=IF(OR(ISERROR(Z5),Z5<1),NA(),Z5)"
    @eval_fn
    def Z6():
        z5_1 = Charts_Data_M2.Z5()
        var_1 = ISERROR(z5_1)
        z5_2 = Charts_Data_M2.Z5()
        var_2 = lessthan(z5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        z5_3 = Charts_Data_M2.Z5()
        var_5 = IF(var_3, var_4, z5_3)
        return var_5

@register(Charts_Data_M2)
class AA6():
    # 'Charts_Data_M2'!AA6
    value = 3.033576
    formula = "=IF(OR(ISERROR(AA5),AA5<1),NA(),AA5)"
    @eval_fn
    def AA6():
        aa5_1 = Charts_Data_M2.AA5()
        var_1 = ISERROR(aa5_1)
        aa5_2 = Charts_Data_M2.AA5()
        var_2 = lessthan(aa5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        aa5_3 = Charts_Data_M2.AA5()
        var_5 = IF(var_3, var_4, aa5_3)
        return var_5

@register(Charts_Data_M2)
class AB6():
    # 'Charts_Data_M2'!AB6
    value = 20.320146
    formula = "=IF(OR(ISERROR(AB5),AB5<1),NA(),AB5)"
    @eval_fn
    def AB6():
        ab5_1 = Charts_Data_M2.AB5()
        var_1 = ISERROR(ab5_1)
        ab5_2 = Charts_Data_M2.AB5()
        var_2 = lessthan(ab5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ab5_3 = Charts_Data_M2.AB5()
        var_5 = IF(var_3, var_4, ab5_3)
        return var_5

@register(Charts_Data_M2)
class AC6():
    # 'Charts_Data_M2'!AC6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AC5),AC5<1),NA(),AC5)"
    @eval_fn
    def AC6():
        ac5_1 = Charts_Data_M2.AC5()
        var_1 = ISERROR(ac5_1)
        ac5_2 = Charts_Data_M2.AC5()
        var_2 = lessthan(ac5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ac5_3 = Charts_Data_M2.AC5()
        var_5 = IF(var_3, var_4, ac5_3)
        return var_5

@register(Charts_Data_M2)
class AD6():
    # 'Charts_Data_M2'!AD6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AD5),AD5<1),NA(),AD5)"
    @eval_fn
    def AD6():
        ad5_1 = Charts_Data_M2.AD5()
        var_1 = ISERROR(ad5_1)
        ad5_2 = Charts_Data_M2.AD5()
        var_2 = lessthan(ad5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ad5_3 = Charts_Data_M2.AD5()
        var_5 = IF(var_3, var_4, ad5_3)
        return var_5

@register(Charts_Data_M2)
class AE6():
    # 'Charts_Data_M2'!AE6
    value = 161.245728
    formula = "=IF(OR(ISERROR(AE5),AE5<1),NA(),AE5)"
    @eval_fn
    def AE6():
        ae5_1 = Charts_Data_M2.AE5()
        var_1 = ISERROR(ae5_1)
        ae5_2 = Charts_Data_M2.AE5()
        var_2 = lessthan(ae5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ae5_3 = Charts_Data_M2.AE5()
        var_5 = IF(var_3, var_4, ae5_3)
        return var_5

@register(Charts_Data_M2)
class AF6():
    # 'Charts_Data_M2'!AF6
    value = 47.909316
    formula = "=IF(OR(ISERROR(AF5),AF5<1),NA(),AF5)"
    @eval_fn
    def AF6():
        af5_1 = Charts_Data_M2.AF5()
        var_1 = ISERROR(af5_1)
        af5_2 = Charts_Data_M2.AF5()
        var_2 = lessthan(af5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        af5_3 = Charts_Data_M2.AF5()
        var_5 = IF(var_3, var_4, af5_3)
        return var_5

@register(Charts_Data_M2)
class AG6():
    # 'Charts_Data_M2'!AG6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AG5),AG5<1),NA(),AG5)"
    @eval_fn
    def AG6():
        ag5_1 = Charts_Data_M2.AG5()
        var_1 = ISERROR(ag5_1)
        ag5_2 = Charts_Data_M2.AG5()
        var_2 = lessthan(ag5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ag5_3 = Charts_Data_M2.AG5()
        var_5 = IF(var_3, var_4, ag5_3)
        return var_5

@register(Charts_Data_M2)
class AH6():
    # 'Charts_Data_M2'!AH6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AH5),AH5<1),NA(),AH5)"
    @eval_fn
    def AH6():
        ah5_1 = Charts_Data_M2.AH5()
        var_1 = ISERROR(ah5_1)
        ah5_2 = Charts_Data_M2.AH5()
        var_2 = lessthan(ah5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ah5_3 = Charts_Data_M2.AH5()
        var_5 = IF(var_3, var_4, ah5_3)
        return var_5

@register(Charts_Data_M2)
class AI6():
    # 'Charts_Data_M2'!AI6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AI5),AI5<1),NA(),AI5)"
    @eval_fn
    def AI6():
        ai5_1 = Charts_Data_M2.AI5()
        var_1 = ISERROR(ai5_1)
        ai5_2 = Charts_Data_M2.AI5()
        var_2 = lessthan(ai5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ai5_3 = Charts_Data_M2.AI5()
        var_5 = IF(var_3, var_4, ai5_3)
        return var_5

@register(Charts_Data_M2)
class AJ6():
    # 'Charts_Data_M2'!AJ6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AJ5),AJ5<1),NA(),AJ5)"
    @eval_fn
    def AJ6():
        aj5_1 = Charts_Data_M2.AJ5()
        var_1 = ISERROR(aj5_1)
        aj5_2 = Charts_Data_M2.AJ5()
        var_2 = lessthan(aj5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        aj5_3 = Charts_Data_M2.AJ5()
        var_5 = IF(var_3, var_4, aj5_3)
        return var_5

@register(Charts_Data_M2)
class AK6():
    # 'Charts_Data_M2'!AK6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AK5),AK5<1),NA(),AK5)"
    @eval_fn
    def AK6():
        ak5_1 = Charts_Data_M2.AK5()
        var_1 = ISERROR(ak5_1)
        ak5_2 = Charts_Data_M2.AK5()
        var_2 = lessthan(ak5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ak5_3 = Charts_Data_M2.AK5()
        var_5 = IF(var_3, var_4, ak5_3)
        return var_5

@register(Charts_Data_M2)
class AL6():
    # 'Charts_Data_M2'!AL6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AL5),AL5<1),NA(),AL5)"
    @eval_fn
    def AL6():
        al5_1 = Charts_Data_M2.AL5()
        var_1 = ISERROR(al5_1)
        al5_2 = Charts_Data_M2.AL5()
        var_2 = lessthan(al5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        al5_3 = Charts_Data_M2.AL5()
        var_5 = IF(var_3, var_4, al5_3)
        return var_5

@register(Charts_Data_M2)
class AM6():
    # 'Charts_Data_M2'!AM6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AM5),AM5<1),NA(),AM5)"
    @eval_fn
    def AM6():
        am5_1 = Charts_Data_M2.AM5()
        var_1 = ISERROR(am5_1)
        am5_2 = Charts_Data_M2.AM5()
        var_2 = lessthan(am5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        am5_3 = Charts_Data_M2.AM5()
        var_5 = IF(var_3, var_4, am5_3)
        return var_5

@register(Charts_Data_M2)
class AN6():
    # 'Charts_Data_M2'!AN6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AN5),AN5<1),NA(),AN5)"
    @eval_fn
    def AN6():
        an5_1 = Charts_Data_M2.AN5()
        var_1 = ISERROR(an5_1)
        an5_2 = Charts_Data_M2.AN5()
        var_2 = lessthan(an5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        an5_3 = Charts_Data_M2.AN5()
        var_5 = IF(var_3, var_4, an5_3)
        return var_5

@register(Charts_Data_M2)
class AO6():
    # 'Charts_Data_M2'!AO6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AO5),AO5<1),NA(),AO5)"
    @eval_fn
    def AO6():
        ao5_1 = Charts_Data_M2.AO5()
        var_1 = ISERROR(ao5_1)
        ao5_2 = Charts_Data_M2.AO5()
        var_2 = lessthan(ao5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ao5_3 = Charts_Data_M2.AO5()
        var_5 = IF(var_3, var_4, ao5_3)
        return var_5

@register(Charts_Data_M2)
class AP6():
    # 'Charts_Data_M2'!AP6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AP5),AP5<1),NA(),AP5)"
    @eval_fn
    def AP6():
        ap5_1 = Charts_Data_M2.AP5()
        var_1 = ISERROR(ap5_1)
        ap5_2 = Charts_Data_M2.AP5()
        var_2 = lessthan(ap5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ap5_3 = Charts_Data_M2.AP5()
        var_5 = IF(var_3, var_4, ap5_3)
        return var_5

@register(Charts_Data_M2)
class AQ6():
    # 'Charts_Data_M2'!AQ6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AQ5),AQ5<1),NA(),AQ5)"
    @eval_fn
    def AQ6():
        aq5_1 = Charts_Data_M2.AQ5()
        var_1 = ISERROR(aq5_1)
        aq5_2 = Charts_Data_M2.AQ5()
        var_2 = lessthan(aq5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        aq5_3 = Charts_Data_M2.AQ5()
        var_5 = IF(var_3, var_4, aq5_3)
        return var_5

@register(Charts_Data_M2)
class AR6():
    # 'Charts_Data_M2'!AR6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AR5),AR5<1),NA(),AR5)"
    @eval_fn
    def AR6():
        ar5_1 = Charts_Data_M2.AR5()
        var_1 = ISERROR(ar5_1)
        ar5_2 = Charts_Data_M2.AR5()
        var_2 = lessthan(ar5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        ar5_3 = Charts_Data_M2.AR5()
        var_5 = IF(var_3, var_4, ar5_3)
        return var_5

@register(Charts_Data_M2)
class AS6():
    # 'Charts_Data_M2'!AS6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AS5),AS5<1),NA(),AS5)"
    @eval_fn
    def AS6():
        as5_1 = Charts_Data_M2.AS5()
        var_1 = ISERROR(as5_1)
        as5_2 = Charts_Data_M2.AS5()
        var_2 = lessthan(as5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        as5_3 = Charts_Data_M2.AS5()
        var_5 = IF(var_3, var_4, as5_3)
        return var_5

@register(Charts_Data_M2)
class AT6():
    # 'Charts_Data_M2'!AT6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AT5),AT5<1),NA(),AT5)"
    @eval_fn
    def AT6():
        at5_1 = Charts_Data_M2.AT5()
        var_1 = ISERROR(at5_1)
        at5_2 = Charts_Data_M2.AT5()
        var_2 = lessthan(at5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        at5_3 = Charts_Data_M2.AT5()
        var_5 = IF(var_3, var_4, at5_3)
        return var_5

@register(Charts_Data_M2)
class AU6():
    # 'Charts_Data_M2'!AU6
    value = "#N/A"
    formula = "=IF(OR(ISERROR(AU5),AU5<1),NA(),AU5)"
    @eval_fn
    def AU6():
        au5_1 = Charts_Data_M2.AU5()
        var_1 = ISERROR(au5_1)
        au5_2 = Charts_Data_M2.AU5()
        var_2 = lessthan(au5_2, 1)
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        au5_3 = Charts_Data_M2.AU5()
        var_5 = IF(var_3, var_4, au5_3)
        return var_5

@register(Charts_Data_M2)
class A7():
    # 'Charts_Data_M2'!A7
    value = "Graph Inputs (Top Line)"

@register(Charts_Data_M2)
class C7():
    # 'Charts_Data_M2'!C7
    value = "    Crude Oil (Foreign)"

@register(Charts_Data_M2)
class E7():
    # 'Charts_Data_M2'!E7
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F7():
    # 'Charts_Data_M2'!F7
    value = "Notes"

@register(Charts_Data_M2)
class G7():
    # 'Charts_Data_M2'!G7
    value = 3370999820
    formula = "=INDEX('Dashboard M2 Annual'!$A$9:$AK$29,MATCH($C7,'Dashboard M2 Annual'!$B$9:$B$29,0),MATCH($B$2,'Dashboard M2 Annual'!$A$9:$AK$9,0))"
    @eval_fn
    def G7():
        range_1 = Dashboard_M2_Annual(1, 9, 37, 29)
        c7_1 = Charts_Data_M2.C7()
        range_2 = Dashboard_M2_Annual(2, 9, 2, 29)
        var_1 = MATCH(c7_1, range_2, 0)
        b2_1 = Charts_Data_M2.B2()
        range_3 = Dashboard_M2_Annual(1, 9, 37, 9)
        var_2 = MATCH(b2_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M2)
class C8():
    # 'Charts_Data_M2'!C8
    value = "    Jet Fuel, Kerosene Type (Foreign)"

@register(Charts_Data_M2)
class E8():
    # 'Charts_Data_M2'!E8
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F8():
    # 'Charts_Data_M2'!F8
    value = "Notes"

@register(Charts_Data_M2)
class G8():
    # 'Charts_Data_M2'!G8
    value = 341916834
    formula = "=INDEX('Dashboard M2 Annual'!$A$9:$AK$29,MATCH($C8,'Dashboard M2 Annual'!$B$9:$B$29,0),MATCH($B$2,'Dashboard M2 Annual'!$A$9:$AK$9,0))"
    @eval_fn
    def G8():
        range_1 = Dashboard_M2_Annual(1, 9, 37, 29)
        c8_1 = Charts_Data_M2.C8()
        range_2 = Dashboard_M2_Annual(2, 9, 2, 29)
        var_1 = MATCH(c8_1, range_2, 0)
        b2_1 = Charts_Data_M2.B2()
        range_3 = Dashboard_M2_Annual(1, 9, 37, 9)
        var_2 = MATCH(b2_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M2)
class C9():
    # 'Charts_Data_M2'!C9
    value = "    Residual Fuel Oil (Foreign)"

@register(Charts_Data_M2)
class E9():
    # 'Charts_Data_M2'!E9
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F9():
    # 'Charts_Data_M2'!F9
    value = "Notes"

@register(Charts_Data_M2)
class G9():
    # 'Charts_Data_M2'!G9
    value = 20320146
    formula = "=INDEX('Dashboard M2 Annual'!$A$9:$AK$29,MATCH($C9,'Dashboard M2 Annual'!$B$9:$B$29,0),MATCH($B$2,'Dashboard M2 Annual'!$A$9:$AK$9,0))"
    @eval_fn
    def G9():
        range_1 = Dashboard_M2_Annual(1, 9, 37, 29)
        c9_1 = Charts_Data_M2.C9()
        range_2 = Dashboard_M2_Annual(2, 9, 2, 29)
        var_1 = MATCH(c9_1, range_2, 0)
        b2_1 = Charts_Data_M2.B2()
        range_3 = Dashboard_M2_Annual(1, 9, 37, 9)
        var_2 = MATCH(b2_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M2)
class C10():
    # 'Charts_Data_M2'!C10
    value = "    Others (Foreign)"

@register(Charts_Data_M2)
class E10():
    # 'Charts_Data_M2'!E10
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F10():
    # 'Charts_Data_M2'!F10
    value = "Notes"

@register(Charts_Data_M2)
class G10():
    # 'Charts_Data_M2'!G10
    value = 47614938
    formula = "=INDEX('Dashboard M2 Annual'!$A$9:$AK$29,MATCH($C10,'Dashboard M2 Annual'!$B$9:$B$29,0),MATCH($B$2,'Dashboard M2 Annual'!$A$9:$AK$9,0))"
    @eval_fn
    def G10():
        range_1 = Dashboard_M2_Annual(1, 9, 37, 29)
        c10_1 = Charts_Data_M2.C10()
        range_2 = Dashboard_M2_Annual(2, 9, 2, 29)
        var_1 = MATCH(c10_1, range_2, 0)
        b2_1 = Charts_Data_M2.B2()
        range_3 = Dashboard_M2_Annual(1, 9, 37, 9)
        var_2 = MATCH(b2_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M2)
class C11():
    # 'Charts_Data_M2'!C11
    value = "  Biofuels (Foreign)"

@register(Charts_Data_M2)
class E11():
    # 'Charts_Data_M2'!E11
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F11():
    # 'Charts_Data_M2'!F11
    value = "Notes"

@register(Charts_Data_M2)
class G11():
    # 'Charts_Data_M2'!G11
    value = 1698101
    formula = "=INDEX('Dashboard M2 Annual'!$A$9:$AK$29,MATCH($C11,'Dashboard M2 Annual'!$B$9:$B$29,0),MATCH($B$2,'Dashboard M2 Annual'!$A$9:$AK$9,0))"
    @eval_fn
    def G11():
        range_1 = Dashboard_M2_Annual(1, 9, 37, 29)
        c11_1 = Charts_Data_M2.C11()
        range_2 = Dashboard_M2_Annual(2, 9, 2, 29)
        var_1 = MATCH(c11_1, range_2, 0)
        b2_1 = Charts_Data_M2.B2()
        range_3 = Dashboard_M2_Annual(1, 9, 37, 9)
        var_2 = MATCH(b2_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M2)
class C12():
    # 'Charts_Data_M2'!C12
    value = "    Ethanol (Foreign)"

@register(Charts_Data_M2)
class E12():
    # 'Charts_Data_M2'!E12
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F12():
    # 'Charts_Data_M2'!F12
    value = "Notes"

@register(Charts_Data_M2)
class G12():
    # 'Charts_Data_M2'!G12
    value = 0
    formula = "=INDEX('Dashboard M2 Annual'!$A$9:$AK$29,MATCH($C12,'Dashboard M2 Annual'!$B$9:$B$29,0),MATCH($B$2,'Dashboard M2 Annual'!$A$9:$AK$9,0))"
    @eval_fn
    def G12():
        range_1 = Dashboard_M2_Annual(1, 9, 37, 29)
        c12_1 = Charts_Data_M2.C12()
        range_2 = Dashboard_M2_Annual(2, 9, 2, 29)
        var_1 = MATCH(c12_1, range_2, 0)
        b2_1 = Charts_Data_M2.B2()
        range_3 = Dashboard_M2_Annual(1, 9, 37, 9)
        var_2 = MATCH(b2_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M2)
class C13():
    # 'Charts_Data_M2'!C13
    value = "    Biodiesel (Foreign)"

@register(Charts_Data_M2)
class E13():
    # 'Charts_Data_M2'!E13
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F13():
    # 'Charts_Data_M2'!F13
    value = "Notes"

@register(Charts_Data_M2)
class G13():
    # 'Charts_Data_M2'!G13
    value = 1698101
    formula = "=INDEX('Dashboard M2 Annual'!$A$9:$AK$29,MATCH($C13,'Dashboard M2 Annual'!$B$9:$B$29,0),MATCH($B$2,'Dashboard M2 Annual'!$A$9:$AK$9,0))"
    @eval_fn
    def G13():
        range_1 = Dashboard_M2_Annual(1, 9, 37, 29)
        c13_1 = Charts_Data_M2.C13()
        range_2 = Dashboard_M2_Annual(2, 9, 2, 29)
        var_1 = MATCH(c13_1, range_2, 0)
        b2_1 = Charts_Data_M2.B2()
        range_3 = Dashboard_M2_Annual(1, 9, 37, 9)
        var_2 = MATCH(b2_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M2)
class C14():
    # 'Charts_Data_M2'!C14
    value = "  Coal (Foreign)"

@register(Charts_Data_M2)
class E14():
    # 'Charts_Data_M2'!E14
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F14():
    # 'Charts_Data_M2'!F14
    value = "Notes"

@register(Charts_Data_M2)
class G14():
    # 'Charts_Data_M2'!G14
    value = 48481580
    formula = "=INDEX('Dashboard M2 Annual'!$A$9:$AK$29,MATCH($C14,'Dashboard M2 Annual'!$B$9:$B$29,0),MATCH($B$2,'Dashboard M2 Annual'!$A$9:$AK$9,0))"
    @eval_fn
    def G14():
        range_1 = Dashboard_M2_Annual(1, 9, 37, 29)
        c14_1 = Charts_Data_M2.C14()
        range_2 = Dashboard_M2_Annual(2, 9, 2, 29)
        var_1 = MATCH(c14_1, range_2, 0)
        b2_1 = Charts_Data_M2.B2()
        range_3 = Dashboard_M2_Annual(1, 9, 37, 9)
        var_2 = MATCH(b2_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M2)
class C15():
    # 'Charts_Data_M2'!C15
    value = "  Petroleum (Domestic)"

@register(Charts_Data_M2)
class E15():
    # 'Charts_Data_M2'!E15
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F15():
    # 'Charts_Data_M2'!F15
    value = "Notes"

@register(Charts_Data_M2)
class G15():
    # 'Charts_Data_M2'!G15
    value = 0
    formula = "=INDEX('Dashboard M2 Annual'!$A$9:$AK$29,MATCH($C15,'Dashboard M2 Annual'!$B$9:$B$29,0),MATCH($B$2,'Dashboard M2 Annual'!$A$9:$AK$9,0))"
    @eval_fn
    def G15():
        range_1 = Dashboard_M2_Annual(1, 9, 37, 29)
        c15_1 = Charts_Data_M2.C15()
        range_2 = Dashboard_M2_Annual(2, 9, 2, 29)
        var_1 = MATCH(c15_1, range_2, 0)
        b2_1 = Charts_Data_M2.B2()
        range_3 = Dashboard_M2_Annual(1, 9, 37, 9)
        var_2 = MATCH(b2_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M2)
class C16():
    # 'Charts_Data_M2'!C16
    value = "  Coal (Domestic)"

@register(Charts_Data_M2)
class E16():
    # 'Charts_Data_M2'!E16
    value = "Dollars (Millions)"

@register(Charts_Data_M2)
class F16():
    # 'Charts_Data_M2'!F16
    value = "Notes"

@register(Charts_Data_M2)
class G16():
    # 'Charts_Data_M2'!G16
    value = 0
    formula = "=INDEX('Dashboard M2 Annual'!$A$9:$AK$29,MATCH($C16,'Dashboard M2 Annual'!$B$9:$B$29,0),MATCH($B$2,'Dashboard M2 Annual'!$A$9:$AK$9,0))"
    @eval_fn
    def G16():
        range_1 = Dashboard_M2_Annual(1, 9, 37, 29)
        c16_1 = Charts_Data_M2.C16()
        range_2 = Dashboard_M2_Annual(2, 9, 2, 29)
        var_1 = MATCH(c16_1, range_2, 0)
        b2_1 = Charts_Data_M2.B2()
        range_3 = Dashboard_M2_Annual(1, 9, 37, 9)
        var_2 = MATCH(b2_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3