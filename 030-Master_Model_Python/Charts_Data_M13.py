# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_Data_M13 = Worksheet('Charts_Data_M13', 10, 10)



@register(Charts_Data_M13)
class A1():
    # 'Charts_Data_M13'!A1
    value = "Metric 13:"

@register(Charts_Data_M13)
class F1():
    # 'Charts_Data_M13'!F1
    value = "Notes"

@register(Charts_Data_M13)
class G1():
    # 'Charts_Data_M13'!G1
    value = 1990

@register(Charts_Data_M13)
class H1():
    # 'Charts_Data_M13'!H1
    value = 1991

@register(Charts_Data_M13)
class I1():
    # 'Charts_Data_M13'!I1
    value = 1992

@register(Charts_Data_M13)
class J1():
    # 'Charts_Data_M13'!J1
    value = 1993

@register(Charts_Data_M13)
class K1():
    # 'Charts_Data_M13'!K1
    value = 1994

@register(Charts_Data_M13)
class L1():
    # 'Charts_Data_M13'!L1
    value = 1995

@register(Charts_Data_M13)
class M1():
    # 'Charts_Data_M13'!M1
    value = 1996

@register(Charts_Data_M13)
class N1():
    # 'Charts_Data_M13'!N1
    value = 1997

@register(Charts_Data_M13)
class O1():
    # 'Charts_Data_M13'!O1
    value = 1998

@register(Charts_Data_M13)
class P1():
    # 'Charts_Data_M13'!P1
    value = 1999

@register(Charts_Data_M13)
class Q1():
    # 'Charts_Data_M13'!Q1
    value = 2000

@register(Charts_Data_M13)
class R1():
    # 'Charts_Data_M13'!R1
    value = 2001

@register(Charts_Data_M13)
class S1():
    # 'Charts_Data_M13'!S1
    value = 2002

@register(Charts_Data_M13)
class T1():
    # 'Charts_Data_M13'!T1
    value = 2003

@register(Charts_Data_M13)
class U1():
    # 'Charts_Data_M13'!U1
    value = 2004

@register(Charts_Data_M13)
class V1():
    # 'Charts_Data_M13'!V1
    value = 2005

@register(Charts_Data_M13)
class W1():
    # 'Charts_Data_M13'!W1
    value = 2006

@register(Charts_Data_M13)
class X1():
    # 'Charts_Data_M13'!X1
    value = 2007

@register(Charts_Data_M13)
class Y1():
    # 'Charts_Data_M13'!Y1
    value = 2008

@register(Charts_Data_M13)
class Z1():
    # 'Charts_Data_M13'!Z1
    value = 2009

@register(Charts_Data_M13)
class AA1():
    # 'Charts_Data_M13'!AA1
    value = 2010

@register(Charts_Data_M13)
class AB1():
    # 'Charts_Data_M13'!AB1
    value = 2011

@register(Charts_Data_M13)
class AC1():
    # 'Charts_Data_M13'!AC1
    value = 2012

@register(Charts_Data_M13)
class AD1():
    # 'Charts_Data_M13'!AD1
    value = 2013

@register(Charts_Data_M13)
class AE1():
    # 'Charts_Data_M13'!AE1
    value = 2014

@register(Charts_Data_M13)
class AF1():
    # 'Charts_Data_M13'!AF1
    value = 2015

@register(Charts_Data_M13)
class AG1():
    # 'Charts_Data_M13'!AG1
    value = 2016

@register(Charts_Data_M13)
class AH1():
    # 'Charts_Data_M13'!AH1
    value = 2017

@register(Charts_Data_M13)
class AI1():
    # 'Charts_Data_M13'!AI1
    value = 2018

@register(Charts_Data_M13)
class AJ1():
    # 'Charts_Data_M13'!AJ1
    value = 2019

@register(Charts_Data_M13)
class AK1():
    # 'Charts_Data_M13'!AK1
    value = 2020

@register(Charts_Data_M13)
class AL1():
    # 'Charts_Data_M13'!AL1
    value = 2021

@register(Charts_Data_M13)
class AM1():
    # 'Charts_Data_M13'!AM1
    value = 2022

@register(Charts_Data_M13)
class AN1():
    # 'Charts_Data_M13'!AN1
    value = 2023

@register(Charts_Data_M13)
class AO1():
    # 'Charts_Data_M13'!AO1
    value = 2024

@register(Charts_Data_M13)
class AP1():
    # 'Charts_Data_M13'!AP1
    value = 2025

@register(Charts_Data_M13)
class AQ1():
    # 'Charts_Data_M13'!AQ1
    value = 2026

@register(Charts_Data_M13)
class AR1():
    # 'Charts_Data_M13'!AR1
    value = 2027

@register(Charts_Data_M13)
class AS1():
    # 'Charts_Data_M13'!AS1
    value = 2028

@register(Charts_Data_M13)
class AT1():
    # 'Charts_Data_M13'!AT1
    value = 2029

@register(Charts_Data_M13)
class AU1():
    # 'Charts_Data_M13'!AU1
    value = 2030

@register(Charts_Data_M13)
class A2():
    # 'Charts_Data_M13'!A2
    value = "Graph Input"

@register(Charts_Data_M13)
class B2():
    # 'Charts_Data_M13'!B2
    value = "Percent of 1990 levels"

@register(Charts_Data_M13)
class C2():
    # 'Charts_Data_M13'!C2
    value = "   Commercial Energy Sector"
    formula = '''=IF($B$4="Percent of 1990 levels","",'Dashboard M13'!B15)'''
    @eval_fn
    def C2():
        b4_1 = Charts_Data_M13.B4()
        var_1 = equal(b4_1, "Percent of 1990 levels")
        b15_1 = Dashboard_M13.B15()
        var_2 = IF(var_1, "", b15_1)
        return var_2

@register(Charts_Data_M13)
class F2():
    # 'Charts_Data_M13'!F2
    value = "Notes"

@register(Charts_Data_M13)
class G2():
    # 'Charts_Data_M13'!G2
    value = 0.754428115757
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!G6,"")'''
    @eval_fn
    def G2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        g6_1 = Dashboard_M13.G6()
        var_2 = IF(var_1, g6_1, "")
        return var_2

@register(Charts_Data_M13)
class H2():
    # 'Charts_Data_M13'!H2
    value = 0.435180378659
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!H6,"")'''
    @eval_fn
    def H2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        h6_1 = Dashboard_M13.H6()
        var_2 = IF(var_1, h6_1, "")
        return var_2

@register(Charts_Data_M13)
class I2():
    # 'Charts_Data_M13'!I2
    value = 0.920871969121
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!I6,"")'''
    @eval_fn
    def I2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        i6_1 = Dashboard_M13.I6()
        var_2 = IF(var_1, i6_1, "")
        return var_2

@register(Charts_Data_M13)
class J2():
    # 'Charts_Data_M13'!J2
    value = 0.333504956037
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!J6,"")'''
    @eval_fn
    def J2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        j6_1 = Dashboard_M13.J6()
        var_2 = IF(var_1, j6_1, "")
        return var_2

@register(Charts_Data_M13)
class K2():
    # 'Charts_Data_M13'!K2
    value = 0.513863487004
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!K6,"")'''
    @eval_fn
    def K2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        k6_1 = Dashboard_M13.K6()
        var_2 = IF(var_1, k6_1, "")
        return var_2

@register(Charts_Data_M13)
class L2():
    # 'Charts_Data_M13'!L2
    value = 0.318442892246
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!L6,"")'''
    @eval_fn
    def L2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        l6_1 = Dashboard_M13.L6()
        var_2 = IF(var_1, l6_1, "")
        return var_2

@register(Charts_Data_M13)
class M2():
    # 'Charts_Data_M13'!M2
    value = 0.244364891755
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!M6,"")'''
    @eval_fn
    def M2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        m6_1 = Dashboard_M13.M6()
        var_2 = IF(var_1, m6_1, "")
        return var_2

@register(Charts_Data_M13)
class N2():
    # 'Charts_Data_M13'!N2
    value = 0.308156846412
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!N6,"")'''
    @eval_fn
    def N2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        n6_1 = Dashboard_M13.N6()
        var_2 = IF(var_1, n6_1, "")
        return var_2

@register(Charts_Data_M13)
class O2():
    # 'Charts_Data_M13'!O2
    value = 1.09377157967
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!O6,"")'''
    @eval_fn
    def O2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        o6_1 = Dashboard_M13.O6()
        var_2 = IF(var_1, o6_1, "")
        return var_2

@register(Charts_Data_M13)
class P2():
    # 'Charts_Data_M13'!P2
    value = 0.27195740756
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!P6,"")'''
    @eval_fn
    def P2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        p6_1 = Dashboard_M13.P6()
        var_2 = IF(var_1, p6_1, "")
        return var_2

@register(Charts_Data_M13)
class Q2():
    # 'Charts_Data_M13'!Q2
    value = 0.276442083883
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Q6,"")'''
    @eval_fn
    def Q2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        q6_1 = Dashboard_M13.Q6()
        var_2 = IF(var_1, q6_1, "")
        return var_2

@register(Charts_Data_M13)
class R2():
    # 'Charts_Data_M13'!R2
    value = 0.238465883308
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!R6,"")'''
    @eval_fn
    def R2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        r6_1 = Dashboard_M13.R6()
        var_2 = IF(var_1, r6_1, "")
        return var_2

@register(Charts_Data_M13)
class S2():
    # 'Charts_Data_M13'!S2
    value = 0.311535298359
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!S6,"")'''
    @eval_fn
    def S2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        s6_1 = Dashboard_M13.S6()
        var_2 = IF(var_1, s6_1, "")
        return var_2

@register(Charts_Data_M13)
class T2():
    # 'Charts_Data_M13'!T2
    value = 0.280284505939
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!T6,"")'''
    @eval_fn
    def T2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        t6_1 = Dashboard_M13.T6()
        var_2 = IF(var_1, t6_1, "")
        return var_2

@register(Charts_Data_M13)
class U2():
    # 'Charts_Data_M13'!U2
    value = 0.329107025018
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!U6,"")'''
    @eval_fn
    def U2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        u6_1 = Dashboard_M13.U6()
        var_2 = IF(var_1, u6_1, "")
        return var_2

@register(Charts_Data_M13)
class V2():
    # 'Charts_Data_M13'!V2
    value = 0.331705363332
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!V6,"")'''
    @eval_fn
    def V2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        v6_1 = Dashboard_M13.V6()
        var_2 = IF(var_1, v6_1, "")
        return var_2

@register(Charts_Data_M13)
class W2():
    # 'Charts_Data_M13'!W2
    value = 0.33495875651
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!W6,"")'''
    @eval_fn
    def W2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        w6_1 = Dashboard_M13.W6()
        var_2 = IF(var_1, w6_1, "")
        return var_2

@register(Charts_Data_M13)
class X2():
    # 'Charts_Data_M13'!X2
    value = 0.279597654134
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!X6,"")'''
    @eval_fn
    def X2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        x6_1 = Dashboard_M13.X6()
        var_2 = IF(var_1, x6_1, "")
        return var_2

@register(Charts_Data_M13)
class Y2():
    # 'Charts_Data_M13'!Y2
    value = 0.292587539466
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Y6,"")'''
    @eval_fn
    def Y2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        y6_1 = Dashboard_M13.Y6()
        var_2 = IF(var_1, y6_1, "")
        return var_2

@register(Charts_Data_M13)
class Z2():
    # 'Charts_Data_M13'!Z2
    value = 0.345927797314
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Z6,"")'''
    @eval_fn
    def Z2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        z6_1 = Dashboard_M13.Z6()
        var_2 = IF(var_1, z6_1, "")
        return var_2

@register(Charts_Data_M13)
class AA2():
    # 'Charts_Data_M13'!AA2
    value = 0.342057717279
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AA6,"")'''
    @eval_fn
    def AA2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aa6_1 = Dashboard_M13.AA6()
        var_2 = IF(var_1, aa6_1, "")
        return var_2

@register(Charts_Data_M13)
class AB2():
    # 'Charts_Data_M13'!AB2
    value = 0.384616764301
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AB6,"")'''
    @eval_fn
    def AB2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ab6_1 = Dashboard_M13.AB6()
        var_2 = IF(var_1, ab6_1, "")
        return var_2

@register(Charts_Data_M13)
class AC2():
    # 'Charts_Data_M13'!AC2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AC6,"")'''
    @eval_fn
    def AC2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ac6_1 = Dashboard_M13.AC6()
        var_2 = IF(var_1, ac6_1, "")
        return var_2

@register(Charts_Data_M13)
class AD2():
    # 'Charts_Data_M13'!AD2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AD6,"")'''
    @eval_fn
    def AD2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ad6_1 = Dashboard_M13.AD6()
        var_2 = IF(var_1, ad6_1, "")
        return var_2

@register(Charts_Data_M13)
class AE2():
    # 'Charts_Data_M13'!AE2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AE6,"")'''
    @eval_fn
    def AE2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ae6_1 = Dashboard_M13.AE6()
        var_2 = IF(var_1, ae6_1, "")
        return var_2

@register(Charts_Data_M13)
class AF2():
    # 'Charts_Data_M13'!AF2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AF6,"")'''
    @eval_fn
    def AF2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        af6_1 = Dashboard_M13.AF6()
        var_2 = IF(var_1, af6_1, "")
        return var_2

@register(Charts_Data_M13)
class AG2():
    # 'Charts_Data_M13'!AG2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AG6,"")'''
    @eval_fn
    def AG2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ag6_1 = Dashboard_M13.AG6()
        var_2 = IF(var_1, ag6_1, "")
        return var_2

@register(Charts_Data_M13)
class AH2():
    # 'Charts_Data_M13'!AH2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AH6,"")'''
    @eval_fn
    def AH2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ah6_1 = Dashboard_M13.AH6()
        var_2 = IF(var_1, ah6_1, "")
        return var_2

@register(Charts_Data_M13)
class AI2():
    # 'Charts_Data_M13'!AI2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AI6,"")'''
    @eval_fn
    def AI2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ai6_1 = Dashboard_M13.AI6()
        var_2 = IF(var_1, ai6_1, "")
        return var_2

@register(Charts_Data_M13)
class AJ2():
    # 'Charts_Data_M13'!AJ2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AJ6,"")'''
    @eval_fn
    def AJ2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aj6_1 = Dashboard_M13.AJ6()
        var_2 = IF(var_1, aj6_1, "")
        return var_2

@register(Charts_Data_M13)
class AK2():
    # 'Charts_Data_M13'!AK2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AK6,"")'''
    @eval_fn
    def AK2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ak6_1 = Dashboard_M13.AK6()
        var_2 = IF(var_1, ak6_1, "")
        return var_2

@register(Charts_Data_M13)
class AL2():
    # 'Charts_Data_M13'!AL2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AL6,"")'''
    @eval_fn
    def AL2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        al6_1 = Dashboard_M13.AL6()
        var_2 = IF(var_1, al6_1, "")
        return var_2

@register(Charts_Data_M13)
class AM2():
    # 'Charts_Data_M13'!AM2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AM6,"")'''
    @eval_fn
    def AM2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        am6_1 = Dashboard_M13.AM6()
        var_2 = IF(var_1, am6_1, "")
        return var_2

@register(Charts_Data_M13)
class AN2():
    # 'Charts_Data_M13'!AN2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AN6,"")'''
    @eval_fn
    def AN2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        an6_1 = Dashboard_M13.AN6()
        var_2 = IF(var_1, an6_1, "")
        return var_2

@register(Charts_Data_M13)
class AO2():
    # 'Charts_Data_M13'!AO2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AO6,"")'''
    @eval_fn
    def AO2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ao6_1 = Dashboard_M13.AO6()
        var_2 = IF(var_1, ao6_1, "")
        return var_2

@register(Charts_Data_M13)
class AP2():
    # 'Charts_Data_M13'!AP2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AP6,"")'''
    @eval_fn
    def AP2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ap6_1 = Dashboard_M13.AP6()
        var_2 = IF(var_1, ap6_1, "")
        return var_2

@register(Charts_Data_M13)
class AQ2():
    # 'Charts_Data_M13'!AQ2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AQ6,"")'''
    @eval_fn
    def AQ2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aq6_1 = Dashboard_M13.AQ6()
        var_2 = IF(var_1, aq6_1, "")
        return var_2

@register(Charts_Data_M13)
class AR2():
    # 'Charts_Data_M13'!AR2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AR6,"")'''
    @eval_fn
    def AR2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ar6_1 = Dashboard_M13.AR6()
        var_2 = IF(var_1, ar6_1, "")
        return var_2

@register(Charts_Data_M13)
class AS2():
    # 'Charts_Data_M13'!AS2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AS6,"")'''
    @eval_fn
    def AS2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        as6_1 = Dashboard_M13.AS6()
        var_2 = IF(var_1, as6_1, "")
        return var_2

@register(Charts_Data_M13)
class AT2():
    # 'Charts_Data_M13'!AT2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AT6,"")'''
    @eval_fn
    def AT2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        at6_1 = Dashboard_M13.AT6()
        var_2 = IF(var_1, at6_1, "")
        return var_2

@register(Charts_Data_M13)
class AU2():
    # 'Charts_Data_M13'!AU2
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AU6,"")'''
    @eval_fn
    def AU2():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        au6_1 = Dashboard_M13.AU6()
        var_2 = IF(var_1, au6_1, "")
        return var_2

@register(Charts_Data_M13)
class B3():
    # 'Charts_Data_M13'!B3
    value = "Total Emissions (MMTCO2E)"

@register(Charts_Data_M13)
class C3():
    # 'Charts_Data_M13'!C3
    value = "   Industrial Energy Sector"
    formula = '''=IF($B$4="Percent of 1990 levels","",'Dashboard M13'!B16)'''
    @eval_fn
    def C3():
        b4_1 = Charts_Data_M13.B4()
        var_1 = equal(b4_1, "Percent of 1990 levels")
        b16_1 = Dashboard_M13.B16()
        var_2 = IF(var_1, "", b16_1)
        return var_2

@register(Charts_Data_M13)
class F3():
    # 'Charts_Data_M13'!F3
    value = "Notes"

@register(Charts_Data_M13)
class G3():
    # 'Charts_Data_M13'!G3
    value = 2.11513682963
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!G7,"")'''
    @eval_fn
    def G3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        g7_1 = Dashboard_M13.G7()
        var_2 = IF(var_1, g7_1, "")
        return var_2

@register(Charts_Data_M13)
class H3():
    # 'Charts_Data_M13'!H3
    value = 2.02067534262
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!H7,"")'''
    @eval_fn
    def H3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        h7_1 = Dashboard_M13.H7()
        var_2 = IF(var_1, h7_1, "")
        return var_2

@register(Charts_Data_M13)
class I3():
    # 'Charts_Data_M13'!I3
    value = 1.98026408929
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!I7,"")'''
    @eval_fn
    def I3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        i7_1 = Dashboard_M13.I7()
        var_2 = IF(var_1, i7_1, "")
        return var_2

@register(Charts_Data_M13)
class J3():
    # 'Charts_Data_M13'!J3
    value = 1.83940515634
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!J7,"")'''
    @eval_fn
    def J3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        j7_1 = Dashboard_M13.J7()
        var_2 = IF(var_1, j7_1, "")
        return var_2

@register(Charts_Data_M13)
class K3():
    # 'Charts_Data_M13'!K3
    value = 2.03053367591
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!K7,"")'''
    @eval_fn
    def K3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        k7_1 = Dashboard_M13.K7()
        var_2 = IF(var_1, k7_1, "")
        return var_2

@register(Charts_Data_M13)
class L3():
    # 'Charts_Data_M13'!L3
    value = 1.98092370133
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!L7,"")'''
    @eval_fn
    def L3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        l7_1 = Dashboard_M13.L7()
        var_2 = IF(var_1, l7_1, "")
        return var_2

@register(Charts_Data_M13)
class M3():
    # 'Charts_Data_M13'!M3
    value = 2.07918105152
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!M7,"")'''
    @eval_fn
    def M3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        m7_1 = Dashboard_M13.M7()
        var_2 = IF(var_1, m7_1, "")
        return var_2

@register(Charts_Data_M13)
class N3():
    # 'Charts_Data_M13'!N3
    value = 1.96927163465
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!N7,"")'''
    @eval_fn
    def N3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        n7_1 = Dashboard_M13.N7()
        var_2 = IF(var_1, n7_1, "")
        return var_2

@register(Charts_Data_M13)
class O3():
    # 'Charts_Data_M13'!O3
    value = 1.47786913976
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!O7,"")'''
    @eval_fn
    def O3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        o7_1 = Dashboard_M13.O7()
        var_2 = IF(var_1, o7_1, "")
        return var_2

@register(Charts_Data_M13)
class P3():
    # 'Charts_Data_M13'!P3
    value = 1.31042751719
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!P7,"")'''
    @eval_fn
    def P3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        p7_1 = Dashboard_M13.P7()
        var_2 = IF(var_1, p7_1, "")
        return var_2

@register(Charts_Data_M13)
class Q3():
    # 'Charts_Data_M13'!Q3
    value = 1.33767560375
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Q7,"")'''
    @eval_fn
    def Q3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        q7_1 = Dashboard_M13.Q7()
        var_2 = IF(var_1, q7_1, "")
        return var_2

@register(Charts_Data_M13)
class R3():
    # 'Charts_Data_M13'!R3
    value = 1.34088405453
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!R7,"")'''
    @eval_fn
    def R3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        r7_1 = Dashboard_M13.R7()
        var_2 = IF(var_1, r7_1, "")
        return var_2

@register(Charts_Data_M13)
class S3():
    # 'Charts_Data_M13'!S3
    value = 1.50302190878
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!S7,"")'''
    @eval_fn
    def S3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        s7_1 = Dashboard_M13.S7()
        var_2 = IF(var_1, s7_1, "")
        return var_2

@register(Charts_Data_M13)
class T3():
    # 'Charts_Data_M13'!T3
    value = 1.52792941107
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!T7,"")'''
    @eval_fn
    def T3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        t7_1 = Dashboard_M13.T7()
        var_2 = IF(var_1, t7_1, "")
        return var_2

@register(Charts_Data_M13)
class U3():
    # 'Charts_Data_M13'!U3
    value = 1.51256484209
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!U7,"")'''
    @eval_fn
    def U3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        u7_1 = Dashboard_M13.U7()
        var_2 = IF(var_1, u7_1, "")
        return var_2

@register(Charts_Data_M13)
class V3():
    # 'Charts_Data_M13'!V3
    value = 1.76591433937
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!V7,"")'''
    @eval_fn
    def V3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        v7_1 = Dashboard_M13.V7()
        var_2 = IF(var_1, v7_1, "")
        return var_2

@register(Charts_Data_M13)
class W3():
    # 'Charts_Data_M13'!W3
    value = 1.79678470986
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!W7,"")'''
    @eval_fn
    def W3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        w7_1 = Dashboard_M13.W7()
        var_2 = IF(var_1, w7_1, "")
        return var_2

@register(Charts_Data_M13)
class X3():
    # 'Charts_Data_M13'!X3
    value = 1.62942254952
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!X7,"")'''
    @eval_fn
    def X3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        x7_1 = Dashboard_M13.X7()
        var_2 = IF(var_1, x7_1, "")
        return var_2

@register(Charts_Data_M13)
class Y3():
    # 'Charts_Data_M13'!Y3
    value = 1.42537982957
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Y7,"")'''
    @eval_fn
    def Y3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        y7_1 = Dashboard_M13.Y7()
        var_2 = IF(var_1, y7_1, "")
        return var_2

@register(Charts_Data_M13)
class Z3():
    # 'Charts_Data_M13'!Z3
    value = 1.40620451924
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Z7,"")'''
    @eval_fn
    def Z3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        z7_1 = Dashboard_M13.Z7()
        var_2 = IF(var_1, z7_1, "")
        return var_2

@register(Charts_Data_M13)
class AA3():
    # 'Charts_Data_M13'!AA3
    value = 1.39046598306
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AA7,"")'''
    @eval_fn
    def AA3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aa7_1 = Dashboard_M13.AA7()
        var_2 = IF(var_1, aa7_1, "")
        return var_2

@register(Charts_Data_M13)
class AB3():
    # 'Charts_Data_M13'!AB3
    value = 1.43228488783
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AB7,"")'''
    @eval_fn
    def AB3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ab7_1 = Dashboard_M13.AB7()
        var_2 = IF(var_1, ab7_1, "")
        return var_2

@register(Charts_Data_M13)
class AC3():
    # 'Charts_Data_M13'!AC3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AC7,"")'''
    @eval_fn
    def AC3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ac7_1 = Dashboard_M13.AC7()
        var_2 = IF(var_1, ac7_1, "")
        return var_2

@register(Charts_Data_M13)
class AD3():
    # 'Charts_Data_M13'!AD3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AD7,"")'''
    @eval_fn
    def AD3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ad7_1 = Dashboard_M13.AD7()
        var_2 = IF(var_1, ad7_1, "")
        return var_2

@register(Charts_Data_M13)
class AE3():
    # 'Charts_Data_M13'!AE3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AE7,"")'''
    @eval_fn
    def AE3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ae7_1 = Dashboard_M13.AE7()
        var_2 = IF(var_1, ae7_1, "")
        return var_2

@register(Charts_Data_M13)
class AF3():
    # 'Charts_Data_M13'!AF3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AF7,"")'''
    @eval_fn
    def AF3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        af7_1 = Dashboard_M13.AF7()
        var_2 = IF(var_1, af7_1, "")
        return var_2

@register(Charts_Data_M13)
class AG3():
    # 'Charts_Data_M13'!AG3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AG7,"")'''
    @eval_fn
    def AG3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ag7_1 = Dashboard_M13.AG7()
        var_2 = IF(var_1, ag7_1, "")
        return var_2

@register(Charts_Data_M13)
class AH3():
    # 'Charts_Data_M13'!AH3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AH7,"")'''
    @eval_fn
    def AH3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ah7_1 = Dashboard_M13.AH7()
        var_2 = IF(var_1, ah7_1, "")
        return var_2

@register(Charts_Data_M13)
class AI3():
    # 'Charts_Data_M13'!AI3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AI7,"")'''
    @eval_fn
    def AI3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ai7_1 = Dashboard_M13.AI7()
        var_2 = IF(var_1, ai7_1, "")
        return var_2

@register(Charts_Data_M13)
class AJ3():
    # 'Charts_Data_M13'!AJ3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AJ7,"")'''
    @eval_fn
    def AJ3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aj7_1 = Dashboard_M13.AJ7()
        var_2 = IF(var_1, aj7_1, "")
        return var_2

@register(Charts_Data_M13)
class AK3():
    # 'Charts_Data_M13'!AK3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AK7,"")'''
    @eval_fn
    def AK3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ak7_1 = Dashboard_M13.AK7()
        var_2 = IF(var_1, ak7_1, "")
        return var_2

@register(Charts_Data_M13)
class AL3():
    # 'Charts_Data_M13'!AL3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AL7,"")'''
    @eval_fn
    def AL3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        al7_1 = Dashboard_M13.AL7()
        var_2 = IF(var_1, al7_1, "")
        return var_2

@register(Charts_Data_M13)
class AM3():
    # 'Charts_Data_M13'!AM3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AM7,"")'''
    @eval_fn
    def AM3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        am7_1 = Dashboard_M13.AM7()
        var_2 = IF(var_1, am7_1, "")
        return var_2

@register(Charts_Data_M13)
class AN3():
    # 'Charts_Data_M13'!AN3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AN7,"")'''
    @eval_fn
    def AN3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        an7_1 = Dashboard_M13.AN7()
        var_2 = IF(var_1, an7_1, "")
        return var_2

@register(Charts_Data_M13)
class AO3():
    # 'Charts_Data_M13'!AO3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AO7,"")'''
    @eval_fn
    def AO3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ao7_1 = Dashboard_M13.AO7()
        var_2 = IF(var_1, ao7_1, "")
        return var_2

@register(Charts_Data_M13)
class AP3():
    # 'Charts_Data_M13'!AP3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AP7,"")'''
    @eval_fn
    def AP3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ap7_1 = Dashboard_M13.AP7()
        var_2 = IF(var_1, ap7_1, "")
        return var_2

@register(Charts_Data_M13)
class AQ3():
    # 'Charts_Data_M13'!AQ3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AQ7,"")'''
    @eval_fn
    def AQ3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aq7_1 = Dashboard_M13.AQ7()
        var_2 = IF(var_1, aq7_1, "")
        return var_2

@register(Charts_Data_M13)
class AR3():
    # 'Charts_Data_M13'!AR3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AR7,"")'''
    @eval_fn
    def AR3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ar7_1 = Dashboard_M13.AR7()
        var_2 = IF(var_1, ar7_1, "")
        return var_2

@register(Charts_Data_M13)
class AS3():
    # 'Charts_Data_M13'!AS3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AS7,"")'''
    @eval_fn
    def AS3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        as7_1 = Dashboard_M13.AS7()
        var_2 = IF(var_1, as7_1, "")
        return var_2

@register(Charts_Data_M13)
class AT3():
    # 'Charts_Data_M13'!AT3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AT7,"")'''
    @eval_fn
    def AT3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        at7_1 = Dashboard_M13.AT7()
        var_2 = IF(var_1, at7_1, "")
        return var_2

@register(Charts_Data_M13)
class AU3():
    # 'Charts_Data_M13'!AU3
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AU7,"")'''
    @eval_fn
    def AU3():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        au7_1 = Dashboard_M13.AU7()
        var_2 = IF(var_1, au7_1, "")
        return var_2

@register(Charts_Data_M13)
class B4():
    # 'Charts_Data_M13'!B4
    value = "Total Emissions (MMTCO2E)"
    formula = "=IF('Charts M13'!A1=1,'Charts Data M13'!B2,'Charts Data M13'!B3)"
    @eval_fn
    def B4():
        a1_1 = Charts_M13.A1()
        var_1 = equal(a1_1, 1)
        b2_1 = Charts_Data_M13.B2()
        b3_1 = Charts_Data_M13.B3()
        var_2 = IF(var_1, b2_1, b3_1)
        return var_2

@register(Charts_Data_M13)
class C4():
    # 'Charts_Data_M13'!C4
    value = "   Residential Energy Sector"
    formula = '''=IF($B$4="Percent of 1990 levels","",'Dashboard M13'!B17)'''
    @eval_fn
    def C4():
        b4_1 = Charts_Data_M13.B4()
        var_1 = equal(b4_1, "Percent of 1990 levels")
        b17_1 = Dashboard_M13.B17()
        var_2 = IF(var_1, "", b17_1)
        return var_2

@register(Charts_Data_M13)
class F4():
    # 'Charts_Data_M13'!F4
    value = "Notes"

@register(Charts_Data_M13)
class G4():
    # 'Charts_Data_M13'!G4
    value = 0.0456336688721
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!G8,"")'''
    @eval_fn
    def G4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        g8_1 = Dashboard_M13.G8()
        var_2 = IF(var_1, g8_1, "")
        return var_2

@register(Charts_Data_M13)
class H4():
    # 'Charts_Data_M13'!H4
    value = 0.0451296345613
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!H8,"")'''
    @eval_fn
    def H4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        h8_1 = Dashboard_M13.H8()
        var_2 = IF(var_1, h8_1, "")
        return var_2

@register(Charts_Data_M13)
class I4():
    # 'Charts_Data_M13'!I4
    value = 0.074969711129
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!I8,"")'''
    @eval_fn
    def I4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        i8_1 = Dashboard_M13.I8()
        var_2 = IF(var_1, i8_1, "")
        return var_2

@register(Charts_Data_M13)
class J4():
    # 'Charts_Data_M13'!J4
    value = 0.0413900137658
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!J8,"")'''
    @eval_fn
    def J4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        j8_1 = Dashboard_M13.J8()
        var_2 = IF(var_1, j8_1, "")
        return var_2

@register(Charts_Data_M13)
class K4():
    # 'Charts_Data_M13'!K4
    value = 0.0423649906708
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!K8,"")'''
    @eval_fn
    def K4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        k8_1 = Dashboard_M13.K8()
        var_2 = IF(var_1, k8_1, "")
        return var_2

@register(Charts_Data_M13)
class L4():
    # 'Charts_Data_M13'!L4
    value = 0.0416641679553
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!L8,"")'''
    @eval_fn
    def L4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        l8_1 = Dashboard_M13.L8()
        var_2 = IF(var_1, l8_1, "")
        return var_2

@register(Charts_Data_M13)
class M4():
    # 'Charts_Data_M13'!M4
    value = 0.0415642015681
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!M8,"")'''
    @eval_fn
    def M4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        m8_1 = Dashboard_M13.M8()
        var_2 = IF(var_1, m8_1, "")
        return var_2

@register(Charts_Data_M13)
class N4():
    # 'Charts_Data_M13'!N4
    value = 0.0492828747902
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!N8,"")'''
    @eval_fn
    def N4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        n8_1 = Dashboard_M13.N8()
        var_2 = IF(var_1, n8_1, "")
        return var_2

@register(Charts_Data_M13)
class O4():
    # 'Charts_Data_M13'!O4
    value = 0.0891578162787
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!O8,"")'''
    @eval_fn
    def O4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        o8_1 = Dashboard_M13.O8()
        var_2 = IF(var_1, o8_1, "")
        return var_2

@register(Charts_Data_M13)
class P4():
    # 'Charts_Data_M13'!P4
    value = 0.0629892925889
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!P8,"")'''
    @eval_fn
    def P4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        p8_1 = Dashboard_M13.P8()
        var_2 = IF(var_1, p8_1, "")
        return var_2

@register(Charts_Data_M13)
class Q4():
    # 'Charts_Data_M13'!Q4
    value = 0.0758022324814
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Q8,"")'''
    @eval_fn
    def Q4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        q8_1 = Dashboard_M13.Q8()
        var_2 = IF(var_1, q8_1, "")
        return var_2

@register(Charts_Data_M13)
class R4():
    # 'Charts_Data_M13'!R4
    value = 0.0762450327054
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!R8,"")'''
    @eval_fn
    def R4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        r8_1 = Dashboard_M13.R8()
        var_2 = IF(var_1, r8_1, "")
        return var_2

@register(Charts_Data_M13)
class S4():
    # 'Charts_Data_M13'!S4
    value = 0.0771355434496
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!S8,"")'''
    @eval_fn
    def S4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        s8_1 = Dashboard_M13.S8()
        var_2 = IF(var_1, s8_1, "")
        return var_2

@register(Charts_Data_M13)
class T4():
    # 'Charts_Data_M13'!T4
    value = 0.0645523054587
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!T8,"")'''
    @eval_fn
    def T4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        t8_1 = Dashboard_M13.T8()
        var_2 = IF(var_1, t8_1, "")
        return var_2

@register(Charts_Data_M13)
class U4():
    # 'Charts_Data_M13'!U4
    value = 0.0645690261298
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!U8,"")'''
    @eval_fn
    def U4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        u8_1 = Dashboard_M13.U8()
        var_2 = IF(var_1, u8_1, "")
        return var_2

@register(Charts_Data_M13)
class V4():
    # 'Charts_Data_M13'!V4
    value = 0.0644251804163
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!V8,"")'''
    @eval_fn
    def V4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        v8_1 = Dashboard_M13.V8()
        var_2 = IF(var_1, v8_1, "")
        return var_2

@register(Charts_Data_M13)
class W4():
    # 'Charts_Data_M13'!W4
    value = 0.0669868948928
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!W8,"")'''
    @eval_fn
    def W4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        w8_1 = Dashboard_M13.W8()
        var_2 = IF(var_1, w8_1, "")
        return var_2

@register(Charts_Data_M13)
class X4():
    # 'Charts_Data_M13'!X4
    value = 0.058944768794
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!X8,"")'''
    @eval_fn
    def X4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        x8_1 = Dashboard_M13.X8()
        var_2 = IF(var_1, x8_1, "")
        return var_2

@register(Charts_Data_M13)
class Y4():
    # 'Charts_Data_M13'!Y4
    value = 0.0918702240999
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Y8,"")'''
    @eval_fn
    def Y4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        y8_1 = Dashboard_M13.Y8()
        var_2 = IF(var_1, y8_1, "")
        return var_2

@register(Charts_Data_M13)
class Z4():
    # 'Charts_Data_M13'!Z4
    value = 0.0859343526633
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Z8,"")'''
    @eval_fn
    def Z4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        z8_1 = Dashboard_M13.Z8()
        var_2 = IF(var_1, z8_1, "")
        return var_2

@register(Charts_Data_M13)
class AA4():
    # 'Charts_Data_M13'!AA4
    value = 0.0847729324443
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AA8,"")'''
    @eval_fn
    def AA4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aa8_1 = Dashboard_M13.AA8()
        var_2 = IF(var_1, aa8_1, "")
        return var_2

@register(Charts_Data_M13)
class AB4():
    # 'Charts_Data_M13'!AB4
    value = 0.0813057340829
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AB8,"")'''
    @eval_fn
    def AB4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ab8_1 = Dashboard_M13.AB8()
        var_2 = IF(var_1, ab8_1, "")
        return var_2

@register(Charts_Data_M13)
class AC4():
    # 'Charts_Data_M13'!AC4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AC8,"")'''
    @eval_fn
    def AC4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ac8_1 = Dashboard_M13.AC8()
        var_2 = IF(var_1, ac8_1, "")
        return var_2

@register(Charts_Data_M13)
class AD4():
    # 'Charts_Data_M13'!AD4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AD8,"")'''
    @eval_fn
    def AD4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ad8_1 = Dashboard_M13.AD8()
        var_2 = IF(var_1, ad8_1, "")
        return var_2

@register(Charts_Data_M13)
class AE4():
    # 'Charts_Data_M13'!AE4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AE8,"")'''
    @eval_fn
    def AE4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ae8_1 = Dashboard_M13.AE8()
        var_2 = IF(var_1, ae8_1, "")
        return var_2

@register(Charts_Data_M13)
class AF4():
    # 'Charts_Data_M13'!AF4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AF8,"")'''
    @eval_fn
    def AF4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        af8_1 = Dashboard_M13.AF8()
        var_2 = IF(var_1, af8_1, "")
        return var_2

@register(Charts_Data_M13)
class AG4():
    # 'Charts_Data_M13'!AG4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AG8,"")'''
    @eval_fn
    def AG4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ag8_1 = Dashboard_M13.AG8()
        var_2 = IF(var_1, ag8_1, "")
        return var_2

@register(Charts_Data_M13)
class AH4():
    # 'Charts_Data_M13'!AH4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AH8,"")'''
    @eval_fn
    def AH4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ah8_1 = Dashboard_M13.AH8()
        var_2 = IF(var_1, ah8_1, "")
        return var_2

@register(Charts_Data_M13)
class AI4():
    # 'Charts_Data_M13'!AI4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AI8,"")'''
    @eval_fn
    def AI4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ai8_1 = Dashboard_M13.AI8()
        var_2 = IF(var_1, ai8_1, "")
        return var_2

@register(Charts_Data_M13)
class AJ4():
    # 'Charts_Data_M13'!AJ4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AJ8,"")'''
    @eval_fn
    def AJ4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aj8_1 = Dashboard_M13.AJ8()
        var_2 = IF(var_1, aj8_1, "")
        return var_2

@register(Charts_Data_M13)
class AK4():
    # 'Charts_Data_M13'!AK4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AK8,"")'''
    @eval_fn
    def AK4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ak8_1 = Dashboard_M13.AK8()
        var_2 = IF(var_1, ak8_1, "")
        return var_2

@register(Charts_Data_M13)
class AL4():
    # 'Charts_Data_M13'!AL4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AL8,"")'''
    @eval_fn
    def AL4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        al8_1 = Dashboard_M13.AL8()
        var_2 = IF(var_1, al8_1, "")
        return var_2

@register(Charts_Data_M13)
class AM4():
    # 'Charts_Data_M13'!AM4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AM8,"")'''
    @eval_fn
    def AM4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        am8_1 = Dashboard_M13.AM8()
        var_2 = IF(var_1, am8_1, "")
        return var_2

@register(Charts_Data_M13)
class AN4():
    # 'Charts_Data_M13'!AN4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AN8,"")'''
    @eval_fn
    def AN4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        an8_1 = Dashboard_M13.AN8()
        var_2 = IF(var_1, an8_1, "")
        return var_2

@register(Charts_Data_M13)
class AO4():
    # 'Charts_Data_M13'!AO4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AO8,"")'''
    @eval_fn
    def AO4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ao8_1 = Dashboard_M13.AO8()
        var_2 = IF(var_1, ao8_1, "")
        return var_2

@register(Charts_Data_M13)
class AP4():
    # 'Charts_Data_M13'!AP4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AP8,"")'''
    @eval_fn
    def AP4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ap8_1 = Dashboard_M13.AP8()
        var_2 = IF(var_1, ap8_1, "")
        return var_2

@register(Charts_Data_M13)
class AQ4():
    # 'Charts_Data_M13'!AQ4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AQ8,"")'''
    @eval_fn
    def AQ4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aq8_1 = Dashboard_M13.AQ8()
        var_2 = IF(var_1, aq8_1, "")
        return var_2

@register(Charts_Data_M13)
class AR4():
    # 'Charts_Data_M13'!AR4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AR8,"")'''
    @eval_fn
    def AR4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ar8_1 = Dashboard_M13.AR8()
        var_2 = IF(var_1, ar8_1, "")
        return var_2

@register(Charts_Data_M13)
class AS4():
    # 'Charts_Data_M13'!AS4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AS8,"")'''
    @eval_fn
    def AS4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        as8_1 = Dashboard_M13.AS8()
        var_2 = IF(var_1, as8_1, "")
        return var_2

@register(Charts_Data_M13)
class AT4():
    # 'Charts_Data_M13'!AT4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AT8,"")'''
    @eval_fn
    def AT4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        at8_1 = Dashboard_M13.AT8()
        var_2 = IF(var_1, at8_1, "")
        return var_2

@register(Charts_Data_M13)
class AU4():
    # 'Charts_Data_M13'!AU4
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AU8,"")'''
    @eval_fn
    def AU4():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        au8_1 = Dashboard_M13.AU8()
        var_2 = IF(var_1, au8_1, "")
        return var_2

@register(Charts_Data_M13)
class C5():
    # 'Charts_Data_M13'!C5
    value = "   Transportation Sector"
    formula = '''=IF($B$4="Percent of 1990 levels","",'Dashboard M13'!B18)'''
    @eval_fn
    def C5():
        b4_1 = Charts_Data_M13.B4()
        var_1 = equal(b4_1, "Percent of 1990 levels")
        b18_1 = Dashboard_M13.B18()
        var_2 = IF(var_1, "", b18_1)
        return var_2

@register(Charts_Data_M13)
class F5():
    # 'Charts_Data_M13'!F5
    value = "Notes"

@register(Charts_Data_M13)
class G5():
    # 'Charts_Data_M13'!G5
    value = 11.1255441285
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!G9,"")'''
    @eval_fn
    def G5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        g9_1 = Dashboard_M13.G9()
        var_2 = IF(var_1, g9_1, "")
        return var_2

@register(Charts_Data_M13)
class H5():
    # 'Charts_Data_M13'!H5
    value = 10.8803386157
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!H9,"")'''
    @eval_fn
    def H5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        h9_1 = Dashboard_M13.H9()
        var_2 = IF(var_1, h9_1, "")
        return var_2

@register(Charts_Data_M13)
class I5():
    # 'Charts_Data_M13'!I5
    value = 10.3854658306
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!I9,"")'''
    @eval_fn
    def I5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        i9_1 = Dashboard_M13.I9()
        var_2 = IF(var_1, i9_1, "")
        return var_2

@register(Charts_Data_M13)
class J5():
    # 'Charts_Data_M13'!J5
    value = 9.36711395891
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!J9,"")'''
    @eval_fn
    def J5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        j9_1 = Dashboard_M13.J9()
        var_2 = IF(var_1, j9_1, "")
        return var_2

@register(Charts_Data_M13)
class K5():
    # 'Charts_Data_M13'!K5
    value = 10.0494111526
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!K9,"")'''
    @eval_fn
    def K5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        k9_1 = Dashboard_M13.K9()
        var_2 = IF(var_1, k9_1, "")
        return var_2

@register(Charts_Data_M13)
class L5():
    # 'Charts_Data_M13'!L5
    value = 9.89780907391
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!L9,"")'''
    @eval_fn
    def L5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        l9_1 = Dashboard_M13.L9()
        var_2 = IF(var_1, l9_1, "")
        return var_2

@register(Charts_Data_M13)
class M5():
    # 'Charts_Data_M13'!M5
    value = 8.73529217969
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!M9,"")'''
    @eval_fn
    def M5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        m9_1 = Dashboard_M13.M9()
        var_2 = IF(var_1, m9_1, "")
        return var_2

@register(Charts_Data_M13)
class N5():
    # 'Charts_Data_M13'!N5
    value = 8.41440929536
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!N9,"")'''
    @eval_fn
    def N5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        n9_1 = Dashboard_M13.N9()
        var_2 = IF(var_1, n9_1, "")
        return var_2

@register(Charts_Data_M13)
class O5():
    # 'Charts_Data_M13'!O5
    value = 8.22250707626
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!O9,"")'''
    @eval_fn
    def O5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        o9_1 = Dashboard_M13.O9()
        var_2 = IF(var_1, o9_1, "")
        return var_2

@register(Charts_Data_M13)
class P5():
    # 'Charts_Data_M13'!P5
    value = 8.86615764676
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!P9,"")'''
    @eval_fn
    def P5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        p9_1 = Dashboard_M13.P9()
        var_2 = IF(var_1, p9_1, "")
        return var_2

@register(Charts_Data_M13)
class Q5():
    # 'Charts_Data_M13'!Q5
    value = 9.02372551066
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Q9,"")'''
    @eval_fn
    def Q5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        q9_1 = Dashboard_M13.Q9()
        var_2 = IF(var_1, q9_1, "")
        return var_2

@register(Charts_Data_M13)
class R5():
    # 'Charts_Data_M13'!R5
    value = 9.53791014042
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!R9,"")'''
    @eval_fn
    def R5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        r9_1 = Dashboard_M13.R9()
        var_2 = IF(var_1, r9_1, "")
        return var_2

@register(Charts_Data_M13)
class S5():
    # 'Charts_Data_M13'!S5
    value = 10.1166929516
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!S9,"")'''
    @eval_fn
    def S5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        s9_1 = Dashboard_M13.S9()
        var_2 = IF(var_1, s9_1, "")
        return var_2

@register(Charts_Data_M13)
class T5():
    # 'Charts_Data_M13'!T5
    value = 11.7645031556
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!T9,"")'''
    @eval_fn
    def T5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        t9_1 = Dashboard_M13.T9()
        var_2 = IF(var_1, t9_1, "")
        return var_2

@register(Charts_Data_M13)
class U5():
    # 'Charts_Data_M13'!U5
    value = 12.4457281307
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!U9,"")'''
    @eval_fn
    def U5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        u9_1 = Dashboard_M13.U9()
        var_2 = IF(var_1, u9_1, "")
        return var_2

@register(Charts_Data_M13)
class V5():
    # 'Charts_Data_M13'!V5
    value = 12.8499519637
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!V9,"")'''
    @eval_fn
    def V5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        v9_1 = Dashboard_M13.V9()
        var_2 = IF(var_1, v9_1, "")
        return var_2

@register(Charts_Data_M13)
class W5():
    # 'Charts_Data_M13'!W5
    value = 13.0429453009
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!W9,"")'''
    @eval_fn
    def W5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        w9_1 = Dashboard_M13.W9()
        var_2 = IF(var_1, w9_1, "")
        return var_2

@register(Charts_Data_M13)
class X5():
    # 'Charts_Data_M13'!X5
    value = 14.0937993271
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!X9,"")'''
    @eval_fn
    def X5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        x9_1 = Dashboard_M13.X9()
        var_2 = IF(var_1, x9_1, "")
        return var_2

@register(Charts_Data_M13)
class Y5():
    # 'Charts_Data_M13'!Y5
    value = 9.71021621483
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Y9,"")'''
    @eval_fn
    def Y5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        y9_1 = Dashboard_M13.Y9()
        var_2 = IF(var_1, y9_1, "")
        return var_2

@register(Charts_Data_M13)
class Z5():
    # 'Charts_Data_M13'!Z5
    value = 9.44888105592
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Z9,"")'''
    @eval_fn
    def Z5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        z9_1 = Dashboard_M13.Z9()
        var_2 = IF(var_1, z9_1, "")
        return var_2

@register(Charts_Data_M13)
class AA5():
    # 'Charts_Data_M13'!AA5
    value = 9.65984910336
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AA9,"")'''
    @eval_fn
    def AA5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aa9_1 = Dashboard_M13.AA9()
        var_2 = IF(var_1, aa9_1, "")
        return var_2

@register(Charts_Data_M13)
class AB5():
    # 'Charts_Data_M13'!AB5
    value = 10.2312281736
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AB9,"")'''
    @eval_fn
    def AB5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ab9_1 = Dashboard_M13.AB9()
        var_2 = IF(var_1, ab9_1, "")
        return var_2

@register(Charts_Data_M13)
class AC5():
    # 'Charts_Data_M13'!AC5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AC9,"")'''
    @eval_fn
    def AC5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ac9_1 = Dashboard_M13.AC9()
        var_2 = IF(var_1, ac9_1, "")
        return var_2

@register(Charts_Data_M13)
class AD5():
    # 'Charts_Data_M13'!AD5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AD9,"")'''
    @eval_fn
    def AD5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ad9_1 = Dashboard_M13.AD9()
        var_2 = IF(var_1, ad9_1, "")
        return var_2

@register(Charts_Data_M13)
class AE5():
    # 'Charts_Data_M13'!AE5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AE9,"")'''
    @eval_fn
    def AE5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ae9_1 = Dashboard_M13.AE9()
        var_2 = IF(var_1, ae9_1, "")
        return var_2

@register(Charts_Data_M13)
class AF5():
    # 'Charts_Data_M13'!AF5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AF9,"")'''
    @eval_fn
    def AF5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        af9_1 = Dashboard_M13.AF9()
        var_2 = IF(var_1, af9_1, "")
        return var_2

@register(Charts_Data_M13)
class AG5():
    # 'Charts_Data_M13'!AG5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AG9,"")'''
    @eval_fn
    def AG5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ag9_1 = Dashboard_M13.AG9()
        var_2 = IF(var_1, ag9_1, "")
        return var_2

@register(Charts_Data_M13)
class AH5():
    # 'Charts_Data_M13'!AH5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AH9,"")'''
    @eval_fn
    def AH5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ah9_1 = Dashboard_M13.AH9()
        var_2 = IF(var_1, ah9_1, "")
        return var_2

@register(Charts_Data_M13)
class AI5():
    # 'Charts_Data_M13'!AI5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AI9,"")'''
    @eval_fn
    def AI5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ai9_1 = Dashboard_M13.AI9()
        var_2 = IF(var_1, ai9_1, "")
        return var_2

@register(Charts_Data_M13)
class AJ5():
    # 'Charts_Data_M13'!AJ5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AJ9,"")'''
    @eval_fn
    def AJ5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aj9_1 = Dashboard_M13.AJ9()
        var_2 = IF(var_1, aj9_1, "")
        return var_2

@register(Charts_Data_M13)
class AK5():
    # 'Charts_Data_M13'!AK5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AK9,"")'''
    @eval_fn
    def AK5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ak9_1 = Dashboard_M13.AK9()
        var_2 = IF(var_1, ak9_1, "")
        return var_2

@register(Charts_Data_M13)
class AL5():
    # 'Charts_Data_M13'!AL5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AL9,"")'''
    @eval_fn
    def AL5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        al9_1 = Dashboard_M13.AL9()
        var_2 = IF(var_1, al9_1, "")
        return var_2

@register(Charts_Data_M13)
class AM5():
    # 'Charts_Data_M13'!AM5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AM9,"")'''
    @eval_fn
    def AM5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        am9_1 = Dashboard_M13.AM9()
        var_2 = IF(var_1, am9_1, "")
        return var_2

@register(Charts_Data_M13)
class AN5():
    # 'Charts_Data_M13'!AN5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AN9,"")'''
    @eval_fn
    def AN5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        an9_1 = Dashboard_M13.AN9()
        var_2 = IF(var_1, an9_1, "")
        return var_2

@register(Charts_Data_M13)
class AO5():
    # 'Charts_Data_M13'!AO5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AO9,"")'''
    @eval_fn
    def AO5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ao9_1 = Dashboard_M13.AO9()
        var_2 = IF(var_1, ao9_1, "")
        return var_2

@register(Charts_Data_M13)
class AP5():
    # 'Charts_Data_M13'!AP5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AP9,"")'''
    @eval_fn
    def AP5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ap9_1 = Dashboard_M13.AP9()
        var_2 = IF(var_1, ap9_1, "")
        return var_2

@register(Charts_Data_M13)
class AQ5():
    # 'Charts_Data_M13'!AQ5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AQ9,"")'''
    @eval_fn
    def AQ5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aq9_1 = Dashboard_M13.AQ9()
        var_2 = IF(var_1, aq9_1, "")
        return var_2

@register(Charts_Data_M13)
class AR5():
    # 'Charts_Data_M13'!AR5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AR9,"")'''
    @eval_fn
    def AR5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ar9_1 = Dashboard_M13.AR9()
        var_2 = IF(var_1, ar9_1, "")
        return var_2

@register(Charts_Data_M13)
class AS5():
    # 'Charts_Data_M13'!AS5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AS9,"")'''
    @eval_fn
    def AS5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        as9_1 = Dashboard_M13.AS9()
        var_2 = IF(var_1, as9_1, "")
        return var_2

@register(Charts_Data_M13)
class AT5():
    # 'Charts_Data_M13'!AT5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AT9,"")'''
    @eval_fn
    def AT5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        at9_1 = Dashboard_M13.AT9()
        var_2 = IF(var_1, at9_1, "")
        return var_2

@register(Charts_Data_M13)
class AU5():
    # 'Charts_Data_M13'!AU5
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AU9,"")'''
    @eval_fn
    def AU5():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        au9_1 = Dashboard_M13.AU9()
        var_2 = IF(var_1, au9_1, "")
        return var_2

@register(Charts_Data_M13)
class C6():
    # 'Charts_Data_M13'!C6
    value = "   Electric Power Sector"
    formula = '''=IF($B$4="Percent of 1990 levels","",'Dashboard M13'!B19)'''
    @eval_fn
    def C6():
        b4_1 = Charts_Data_M13.B4()
        var_1 = equal(b4_1, "Percent of 1990 levels")
        b19_1 = Dashboard_M13.B19()
        var_2 = IF(var_1, "", b19_1)
        return var_2

@register(Charts_Data_M13)
class F6():
    # 'Charts_Data_M13'!F6
    value = "Notes"

@register(Charts_Data_M13)
class G6():
    # 'Charts_Data_M13'!G6
    value = 7.31298102704
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!G10,"")'''
    @eval_fn
    def G6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        g10_1 = Dashboard_M13.G10()
        var_2 = IF(var_1, g10_1, "")
        return var_2

@register(Charts_Data_M13)
class H6():
    # 'Charts_Data_M13'!H6
    value = 6.0292140767
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!H10,"")'''
    @eval_fn
    def H6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        h10_1 = Dashboard_M13.H10()
        var_2 = IF(var_1, h10_1, "")
        return var_2

@register(Charts_Data_M13)
class I6():
    # 'Charts_Data_M13'!I6
    value = 6.97813738834
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!I10,"")'''
    @eval_fn
    def I6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        i10_1 = Dashboard_M13.I10()
        var_2 = IF(var_1, i10_1, "")
        return var_2

@register(Charts_Data_M13)
class J6():
    # 'Charts_Data_M13'!J6
    value = 7.00157536793
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!J10,"")'''
    @eval_fn
    def J6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        j10_1 = Dashboard_M13.J10()
        var_2 = IF(var_1, j10_1, "")
        return var_2

@register(Charts_Data_M13)
class K6():
    # 'Charts_Data_M13'!K6
    value = 7.23262410047
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!K10,"")'''
    @eval_fn
    def K6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        k10_1 = Dashboard_M13.K10()
        var_2 = IF(var_1, k10_1, "")
        return var_2

@register(Charts_Data_M13)
class L6():
    # 'Charts_Data_M13'!L6
    value = 7.49937226898
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!L10,"")'''
    @eval_fn
    def L6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        l10_1 = Dashboard_M13.L10()
        var_2 = IF(var_1, l10_1, "")
        return var_2

@register(Charts_Data_M13)
class M6():
    # 'Charts_Data_M13'!M6
    value = 7.77095587653
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!M10,"")'''
    @eval_fn
    def M6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        m10_1 = Dashboard_M13.M10()
        var_2 = IF(var_1, m10_1, "")
        return var_2

@register(Charts_Data_M13)
class N6():
    # 'Charts_Data_M13'!N6
    value = 7.70847864624
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!N10,"")'''
    @eval_fn
    def N6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        n10_1 = Dashboard_M13.N10()
        var_2 = IF(var_1, n10_1, "")
        return var_2

@register(Charts_Data_M13)
class O6():
    # 'Charts_Data_M13'!O6
    value = 7.53582139003
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!O10,"")'''
    @eval_fn
    def O6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        o10_1 = Dashboard_M13.O10()
        var_2 = IF(var_1, o10_1, "")
        return var_2

@register(Charts_Data_M13)
class P6():
    # 'Charts_Data_M13'!P6
    value = 7.63319898563
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!P10,"")'''
    @eval_fn
    def P6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        p10_1 = Dashboard_M13.P10()
        var_2 = IF(var_1, p10_1, "")
        return var_2

@register(Charts_Data_M13)
class Q6():
    # 'Charts_Data_M13'!Q6
    value = 7.75212421191
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Q10,"")'''
    @eval_fn
    def Q6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        q10_1 = Dashboard_M13.Q10()
        var_2 = IF(var_1, q10_1, "")
        return var_2

@register(Charts_Data_M13)
class R6():
    # 'Charts_Data_M13'!R6
    value = 7.74745814551
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!R10,"")'''
    @eval_fn
    def R6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        r10_1 = Dashboard_M13.R10()
        var_2 = IF(var_1, r10_1, "")
        return var_2

@register(Charts_Data_M13)
class S6():
    # 'Charts_Data_M13'!S6
    value = 8.31874416772
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!S10,"")'''
    @eval_fn
    def S6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        s10_1 = Dashboard_M13.S10()
        var_2 = IF(var_1, s10_1, "")
        return var_2

@register(Charts_Data_M13)
class T6():
    # 'Charts_Data_M13'!T6
    value = 7.74418017721
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!T10,"")'''
    @eval_fn
    def T6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        t10_1 = Dashboard_M13.T10()
        var_2 = IF(var_1, t10_1, "")
        return var_2

@register(Charts_Data_M13)
class U6():
    # 'Charts_Data_M13'!U6
    value = 8.03315536883
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!U10,"")'''
    @eval_fn
    def U6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        u10_1 = Dashboard_M13.U10()
        var_2 = IF(var_1, u10_1, "")
        return var_2

@register(Charts_Data_M13)
class V6():
    # 'Charts_Data_M13'!V6
    value = 7.98087266698
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!V10,"")'''
    @eval_fn
    def V6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        v10_1 = Dashboard_M13.V10()
        var_2 = IF(var_1, v10_1, "")
        return var_2

@register(Charts_Data_M13)
class W6():
    # 'Charts_Data_M13'!W6
    value = 7.95547617647
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!W10,"")'''
    @eval_fn
    def W6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        w10_1 = Dashboard_M13.W10()
        var_2 = IF(var_1, w10_1, "")
        return var_2

@register(Charts_Data_M13)
class X6():
    # 'Charts_Data_M13'!X6
    value = 7.98325048568
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!X10,"")'''
    @eval_fn
    def X6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        x10_1 = Dashboard_M13.X10()
        var_2 = IF(var_1, x10_1, "")
        return var_2

@register(Charts_Data_M13)
class Y6():
    # 'Charts_Data_M13'!Y6
    value = 7.79709317658
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Y10,"")'''
    @eval_fn
    def Y6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        y10_1 = Dashboard_M13.Y10()
        var_2 = IF(var_1, y10_1, "")
        return var_2

@register(Charts_Data_M13)
class Z6():
    # 'Charts_Data_M13'!Z6
    value = 7.58929347671
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!Z10,"")'''
    @eval_fn
    def Z6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        z10_1 = Dashboard_M13.Z10()
        var_2 = IF(var_1, z10_1, "")
        return var_2

@register(Charts_Data_M13)
class AA6():
    # 'Charts_Data_M13'!AA6
    value = 7.31338889643
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AA10,"")'''
    @eval_fn
    def AA6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aa10_1 = Dashboard_M13.AA10()
        var_2 = IF(var_1, aa10_1, "")
        return var_2

@register(Charts_Data_M13)
class AB6():
    # 'Charts_Data_M13'!AB6
    value = 7.18344446769
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AB10,"")'''
    @eval_fn
    def AB6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ab10_1 = Dashboard_M13.AB10()
        var_2 = IF(var_1, ab10_1, "")
        return var_2

@register(Charts_Data_M13)
class AC6():
    # 'Charts_Data_M13'!AC6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AC10,"")'''
    @eval_fn
    def AC6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ac10_1 = Dashboard_M13.AC10()
        var_2 = IF(var_1, ac10_1, "")
        return var_2

@register(Charts_Data_M13)
class AD6():
    # 'Charts_Data_M13'!AD6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AD10,"")'''
    @eval_fn
    def AD6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ad10_1 = Dashboard_M13.AD10()
        var_2 = IF(var_1, ad10_1, "")
        return var_2

@register(Charts_Data_M13)
class AE6():
    # 'Charts_Data_M13'!AE6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AE10,"")'''
    @eval_fn
    def AE6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ae10_1 = Dashboard_M13.AE10()
        var_2 = IF(var_1, ae10_1, "")
        return var_2

@register(Charts_Data_M13)
class AF6():
    # 'Charts_Data_M13'!AF6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AF10,"")'''
    @eval_fn
    def AF6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        af10_1 = Dashboard_M13.AF10()
        var_2 = IF(var_1, af10_1, "")
        return var_2

@register(Charts_Data_M13)
class AG6():
    # 'Charts_Data_M13'!AG6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AG10,"")'''
    @eval_fn
    def AG6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ag10_1 = Dashboard_M13.AG10()
        var_2 = IF(var_1, ag10_1, "")
        return var_2

@register(Charts_Data_M13)
class AH6():
    # 'Charts_Data_M13'!AH6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AH10,"")'''
    @eval_fn
    def AH6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ah10_1 = Dashboard_M13.AH10()
        var_2 = IF(var_1, ah10_1, "")
        return var_2

@register(Charts_Data_M13)
class AI6():
    # 'Charts_Data_M13'!AI6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AI10,"")'''
    @eval_fn
    def AI6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ai10_1 = Dashboard_M13.AI10()
        var_2 = IF(var_1, ai10_1, "")
        return var_2

@register(Charts_Data_M13)
class AJ6():
    # 'Charts_Data_M13'!AJ6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AJ10,"")'''
    @eval_fn
    def AJ6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aj10_1 = Dashboard_M13.AJ10()
        var_2 = IF(var_1, aj10_1, "")
        return var_2

@register(Charts_Data_M13)
class AK6():
    # 'Charts_Data_M13'!AK6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AK10,"")'''
    @eval_fn
    def AK6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ak10_1 = Dashboard_M13.AK10()
        var_2 = IF(var_1, ak10_1, "")
        return var_2

@register(Charts_Data_M13)
class AL6():
    # 'Charts_Data_M13'!AL6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AL10,"")'''
    @eval_fn
    def AL6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        al10_1 = Dashboard_M13.AL10()
        var_2 = IF(var_1, al10_1, "")
        return var_2

@register(Charts_Data_M13)
class AM6():
    # 'Charts_Data_M13'!AM6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AM10,"")'''
    @eval_fn
    def AM6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        am10_1 = Dashboard_M13.AM10()
        var_2 = IF(var_1, am10_1, "")
        return var_2

@register(Charts_Data_M13)
class AN6():
    # 'Charts_Data_M13'!AN6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AN10,"")'''
    @eval_fn
    def AN6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        an10_1 = Dashboard_M13.AN10()
        var_2 = IF(var_1, an10_1, "")
        return var_2

@register(Charts_Data_M13)
class AO6():
    # 'Charts_Data_M13'!AO6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AO10,"")'''
    @eval_fn
    def AO6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ao10_1 = Dashboard_M13.AO10()
        var_2 = IF(var_1, ao10_1, "")
        return var_2

@register(Charts_Data_M13)
class AP6():
    # 'Charts_Data_M13'!AP6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AP10,"")'''
    @eval_fn
    def AP6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ap10_1 = Dashboard_M13.AP10()
        var_2 = IF(var_1, ap10_1, "")
        return var_2

@register(Charts_Data_M13)
class AQ6():
    # 'Charts_Data_M13'!AQ6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AQ10,"")'''
    @eval_fn
    def AQ6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aq10_1 = Dashboard_M13.AQ10()
        var_2 = IF(var_1, aq10_1, "")
        return var_2

@register(Charts_Data_M13)
class AR6():
    # 'Charts_Data_M13'!AR6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AR10,"")'''
    @eval_fn
    def AR6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ar10_1 = Dashboard_M13.AR10()
        var_2 = IF(var_1, ar10_1, "")
        return var_2

@register(Charts_Data_M13)
class AS6():
    # 'Charts_Data_M13'!AS6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AS10,"")'''
    @eval_fn
    def AS6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        as10_1 = Dashboard_M13.AS10()
        var_2 = IF(var_1, as10_1, "")
        return var_2

@register(Charts_Data_M13)
class AT6():
    # 'Charts_Data_M13'!AT6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AT10,"")'''
    @eval_fn
    def AT6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        at10_1 = Dashboard_M13.AT10()
        var_2 = IF(var_1, at10_1, "")
        return var_2

@register(Charts_Data_M13)
class AU6():
    # 'Charts_Data_M13'!AU6
    value = 0
    formula = '''=IF($B$4=$B$3,'Dashboard M13'!AU10,"")'''
    @eval_fn
    def AU6():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        au10_1 = Dashboard_M13.AU10()
        var_2 = IF(var_1, au10_1, "")
        return var_2

@register(Charts_Data_M13)
class C7():
    # 'Charts_Data_M13'!C7
    value = None
    formula = '''=IF($B$4="Percent of 1990 levels","All Sectors","")'''
    @eval_fn
    def C7():
        b4_1 = Charts_Data_M13.B4()
        var_1 = equal(b4_1, "Percent of 1990 levels")
        var_2 = IF(var_1, "All Sectors", "")
        return var_2

@register(Charts_Data_M13)
class F7():
    # 'Charts_Data_M13'!F7
    value = "Notes"

@register(Charts_Data_M13)
class G7():
    # 'Charts_Data_M13'!G7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!G20)'''
    @eval_fn
    def G7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        g20_1 = Dashboard_M13.G20()
        var_2 = IF(var_1, "", g20_1)
        return var_2

@register(Charts_Data_M13)
class H7():
    # 'Charts_Data_M13'!H7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!H20)'''
    @eval_fn
    def H7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        h20_1 = Dashboard_M13.H20()
        var_2 = IF(var_1, "", h20_1)
        return var_2

@register(Charts_Data_M13)
class I7():
    # 'Charts_Data_M13'!I7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!I20)'''
    @eval_fn
    def I7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        i20_1 = Dashboard_M13.I20()
        var_2 = IF(var_1, "", i20_1)
        return var_2

@register(Charts_Data_M13)
class J7():
    # 'Charts_Data_M13'!J7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!J20)'''
    @eval_fn
    def J7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        j20_1 = Dashboard_M13.J20()
        var_2 = IF(var_1, "", j20_1)
        return var_2

@register(Charts_Data_M13)
class K7():
    # 'Charts_Data_M13'!K7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!K20)'''
    @eval_fn
    def K7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        k20_1 = Dashboard_M13.K20()
        var_2 = IF(var_1, "", k20_1)
        return var_2

@register(Charts_Data_M13)
class L7():
    # 'Charts_Data_M13'!L7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!L20)'''
    @eval_fn
    def L7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        l20_1 = Dashboard_M13.L20()
        var_2 = IF(var_1, "", l20_1)
        return var_2

@register(Charts_Data_M13)
class M7():
    # 'Charts_Data_M13'!M7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!M20)'''
    @eval_fn
    def M7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        m20_1 = Dashboard_M13.M20()
        var_2 = IF(var_1, "", m20_1)
        return var_2

@register(Charts_Data_M13)
class N7():
    # 'Charts_Data_M13'!N7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!N20)'''
    @eval_fn
    def N7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        n20_1 = Dashboard_M13.N20()
        var_2 = IF(var_1, "", n20_1)
        return var_2

@register(Charts_Data_M13)
class O7():
    # 'Charts_Data_M13'!O7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!O20)'''
    @eval_fn
    def O7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        o20_1 = Dashboard_M13.O20()
        var_2 = IF(var_1, "", o20_1)
        return var_2

@register(Charts_Data_M13)
class P7():
    # 'Charts_Data_M13'!P7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!P20)'''
    @eval_fn
    def P7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        p20_1 = Dashboard_M13.P20()
        var_2 = IF(var_1, "", p20_1)
        return var_2

@register(Charts_Data_M13)
class Q7():
    # 'Charts_Data_M13'!Q7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!Q20)'''
    @eval_fn
    def Q7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        q20_1 = Dashboard_M13.Q20()
        var_2 = IF(var_1, "", q20_1)
        return var_2

@register(Charts_Data_M13)
class R7():
    # 'Charts_Data_M13'!R7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!R20)'''
    @eval_fn
    def R7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        r20_1 = Dashboard_M13.R20()
        var_2 = IF(var_1, "", r20_1)
        return var_2

@register(Charts_Data_M13)
class S7():
    # 'Charts_Data_M13'!S7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!S20)'''
    @eval_fn
    def S7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        s20_1 = Dashboard_M13.S20()
        var_2 = IF(var_1, "", s20_1)
        return var_2

@register(Charts_Data_M13)
class T7():
    # 'Charts_Data_M13'!T7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!T20)'''
    @eval_fn
    def T7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        t20_1 = Dashboard_M13.T20()
        var_2 = IF(var_1, "", t20_1)
        return var_2

@register(Charts_Data_M13)
class U7():
    # 'Charts_Data_M13'!U7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!U20)'''
    @eval_fn
    def U7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        u20_1 = Dashboard_M13.U20()
        var_2 = IF(var_1, "", u20_1)
        return var_2

@register(Charts_Data_M13)
class V7():
    # 'Charts_Data_M13'!V7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!V20)'''
    @eval_fn
    def V7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        v20_1 = Dashboard_M13.V20()
        var_2 = IF(var_1, "", v20_1)
        return var_2

@register(Charts_Data_M13)
class W7():
    # 'Charts_Data_M13'!W7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!W20)'''
    @eval_fn
    def W7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        w20_1 = Dashboard_M13.W20()
        var_2 = IF(var_1, "", w20_1)
        return var_2

@register(Charts_Data_M13)
class X7():
    # 'Charts_Data_M13'!X7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!X20)'''
    @eval_fn
    def X7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        x20_1 = Dashboard_M13.X20()
        var_2 = IF(var_1, "", x20_1)
        return var_2

@register(Charts_Data_M13)
class Y7():
    # 'Charts_Data_M13'!Y7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!Y20)'''
    @eval_fn
    def Y7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        y20_1 = Dashboard_M13.Y20()
        var_2 = IF(var_1, "", y20_1)
        return var_2

@register(Charts_Data_M13)
class Z7():
    # 'Charts_Data_M13'!Z7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!Z20)'''
    @eval_fn
    def Z7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        z20_1 = Dashboard_M13.Z20()
        var_2 = IF(var_1, "", z20_1)
        return var_2

@register(Charts_Data_M13)
class AA7():
    # 'Charts_Data_M13'!AA7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AA20)'''
    @eval_fn
    def AA7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aa20_1 = Dashboard_M13.AA20()
        var_2 = IF(var_1, "", aa20_1)
        return var_2

@register(Charts_Data_M13)
class AB7():
    # 'Charts_Data_M13'!AB7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AB20)'''
    @eval_fn
    def AB7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ab20_1 = Dashboard_M13.AB20()
        var_2 = IF(var_1, "", ab20_1)
        return var_2

@register(Charts_Data_M13)
class AC7():
    # 'Charts_Data_M13'!AC7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AC20)'''
    @eval_fn
    def AC7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ac20_1 = Dashboard_M13.AC20()
        var_2 = IF(var_1, "", ac20_1)
        return var_2

@register(Charts_Data_M13)
class AD7():
    # 'Charts_Data_M13'!AD7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AD20)'''
    @eval_fn
    def AD7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ad20_1 = Dashboard_M13.AD20()
        var_2 = IF(var_1, "", ad20_1)
        return var_2

@register(Charts_Data_M13)
class AE7():
    # 'Charts_Data_M13'!AE7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AE20)'''
    @eval_fn
    def AE7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ae20_1 = Dashboard_M13.AE20()
        var_2 = IF(var_1, "", ae20_1)
        return var_2

@register(Charts_Data_M13)
class AF7():
    # 'Charts_Data_M13'!AF7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AF20)'''
    @eval_fn
    def AF7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        af20_1 = Dashboard_M13.AF20()
        var_2 = IF(var_1, "", af20_1)
        return var_2

@register(Charts_Data_M13)
class AG7():
    # 'Charts_Data_M13'!AG7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AG20)'''
    @eval_fn
    def AG7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ag20_1 = Dashboard_M13.AG20()
        var_2 = IF(var_1, "", ag20_1)
        return var_2

@register(Charts_Data_M13)
class AH7():
    # 'Charts_Data_M13'!AH7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AH20)'''
    @eval_fn
    def AH7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ah20_1 = Dashboard_M13.AH20()
        var_2 = IF(var_1, "", ah20_1)
        return var_2

@register(Charts_Data_M13)
class AI7():
    # 'Charts_Data_M13'!AI7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AI20)'''
    @eval_fn
    def AI7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ai20_1 = Dashboard_M13.AI20()
        var_2 = IF(var_1, "", ai20_1)
        return var_2

@register(Charts_Data_M13)
class AJ7():
    # 'Charts_Data_M13'!AJ7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AJ20)'''
    @eval_fn
    def AJ7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aj20_1 = Dashboard_M13.AJ20()
        var_2 = IF(var_1, "", aj20_1)
        return var_2

@register(Charts_Data_M13)
class AK7():
    # 'Charts_Data_M13'!AK7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AK20)'''
    @eval_fn
    def AK7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ak20_1 = Dashboard_M13.AK20()
        var_2 = IF(var_1, "", ak20_1)
        return var_2

@register(Charts_Data_M13)
class AL7():
    # 'Charts_Data_M13'!AL7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AL20)'''
    @eval_fn
    def AL7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        al20_1 = Dashboard_M13.AL20()
        var_2 = IF(var_1, "", al20_1)
        return var_2

@register(Charts_Data_M13)
class AM7():
    # 'Charts_Data_M13'!AM7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AM20)'''
    @eval_fn
    def AM7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        am20_1 = Dashboard_M13.AM20()
        var_2 = IF(var_1, "", am20_1)
        return var_2

@register(Charts_Data_M13)
class AN7():
    # 'Charts_Data_M13'!AN7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AN20)'''
    @eval_fn
    def AN7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        an20_1 = Dashboard_M13.AN20()
        var_2 = IF(var_1, "", an20_1)
        return var_2

@register(Charts_Data_M13)
class AO7():
    # 'Charts_Data_M13'!AO7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AO20)'''
    @eval_fn
    def AO7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ao20_1 = Dashboard_M13.AO20()
        var_2 = IF(var_1, "", ao20_1)
        return var_2

@register(Charts_Data_M13)
class AP7():
    # 'Charts_Data_M13'!AP7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AP20)'''
    @eval_fn
    def AP7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ap20_1 = Dashboard_M13.AP20()
        var_2 = IF(var_1, "", ap20_1)
        return var_2

@register(Charts_Data_M13)
class AQ7():
    # 'Charts_Data_M13'!AQ7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AQ20)'''
    @eval_fn
    def AQ7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        aq20_1 = Dashboard_M13.AQ20()
        var_2 = IF(var_1, "", aq20_1)
        return var_2

@register(Charts_Data_M13)
class AR7():
    # 'Charts_Data_M13'!AR7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AR20)'''
    @eval_fn
    def AR7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        ar20_1 = Dashboard_M13.AR20()
        var_2 = IF(var_1, "", ar20_1)
        return var_2

@register(Charts_Data_M13)
class AS7():
    # 'Charts_Data_M13'!AS7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AS20)'''
    @eval_fn
    def AS7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        as20_1 = Dashboard_M13.AS20()
        var_2 = IF(var_1, "", as20_1)
        return var_2

@register(Charts_Data_M13)
class AT7():
    # 'Charts_Data_M13'!AT7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AT20)'''
    @eval_fn
    def AT7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        at20_1 = Dashboard_M13.AT20()
        var_2 = IF(var_1, "", at20_1)
        return var_2

@register(Charts_Data_M13)
class AU7():
    # 'Charts_Data_M13'!AU7
    value = None
    formula = '''=IF($B$4=$B$3,"",'Dashboard M13'!AU20)'''
    @eval_fn
    def AU7():
        b4_1 = Charts_Data_M13.B4()
        b3_1 = Charts_Data_M13.B3()
        var_1 = equal(b4_1, b3_1)
        au20_1 = Dashboard_M13.AU20()
        var_2 = IF(var_1, "", au20_1)
        return var_2

@register(Charts_Data_M13)
class C8():
    # 'Charts_Data_M13'!C8
    value = "Percent of 1990 levels"
    formula = "=B2"
    @eval_fn
    def C8():
        b2_1 = Charts_Data_M13.B2()
        return b2_1

@register(Charts_Data_M13)
class F8():
    # 'Charts_Data_M13'!F8
    value = "Notes"

@register(Charts_Data_M13)
class G8():
    # 'Charts_Data_M13'!G8
    value = 1
    formula = "='Dashboard M13'!G20"
    @eval_fn
    def G8():
        g20_1 = Dashboard_M13.G20()
        return g20_1

@register(Charts_Data_M13)
class H8():
    # 'Charts_Data_M13'!H8
    value = 0.909000147115
    formula = "='Dashboard M13'!H20"
    @eval_fn
    def H8():
        h20_1 = Dashboard_M13.H20()
        return h20_1

@register(Charts_Data_M13)
class I8():
    # 'Charts_Data_M13'!I8
    value = 0.952513444856
    formula = "='Dashboard M13'!I20"
    @eval_fn
    def I8():
        i20_1 = Dashboard_M13.I20()
        return i20_1

@register(Charts_Data_M13)
class J8():
    # 'Charts_Data_M13'!J8
    value = 0.870245848139
    formula = "='Dashboard M13'!J20"
    @eval_fn
    def J8():
        j20_1 = Dashboard_M13.J20()
        return j20_1

@register(Charts_Data_M13)
class K8():
    # 'Charts_Data_M13'!K8
    value = 0.930460542658
    formula = "='Dashboard M13'!K20"
    @eval_fn
    def K8():
        k20_1 = Dashboard_M13.K20()
        return k20_1

@register(Charts_Data_M13)
class L8():
    # 'Charts_Data_M13'!L8
    value = 0.924345201671
    formula = "='Dashboard M13'!L20"
    @eval_fn
    def L8():
        l20_1 = Dashboard_M13.L20()
        return l20_1

@register(Charts_Data_M13)
class M8():
    # 'Charts_Data_M13'!M8
    value = 0.883750225698
    formula = "='Dashboard M13'!M20"
    @eval_fn
    def M8():
        m20_1 = Dashboard_M13.M20()
        return m20_1

@register(Charts_Data_M13)
class N8():
    # 'Charts_Data_M13'!N8
    value = 0.863999155199
    formula = "='Dashboard M13'!N20"
    @eval_fn
    def N8():
        n20_1 = Dashboard_M13.N20()
        return n20_1

@register(Charts_Data_M13)
class O8():
    # 'Charts_Data_M13'!O8
    value = 0.862572130302
    formula = "='Dashboard M13'!O20"
    @eval_fn
    def O8():
        o20_1 = Dashboard_M13.O20()
        return o20_1

@register(Charts_Data_M13)
class P8():
    # 'Charts_Data_M13'!P8
    value = 0.849722092752
    formula = "='Dashboard M13'!P20"
    @eval_fn
    def P8():
        p20_1 = Dashboard_M13.P20()
        return p20_1

@register(Charts_Data_M13)
class Q8():
    # 'Charts_Data_M13'!Q8
    value = 0.86475641634
    formula = "='Dashboard M13'!Q20"
    @eval_fn
    def Q8():
        q20_1 = Dashboard_M13.Q20()
        return q20_1

@register(Charts_Data_M13)
class R8():
    # 'Charts_Data_M13'!R8
    value = 0.887009847119
    formula = "='Dashboard M13'!R20"
    @eval_fn
    def R8():
        r20_1 = Dashboard_M13.R20()
        return r20_1

@register(Charts_Data_M13)
class S8():
    # 'Charts_Data_M13'!S8
    value = 0.95192436172
    formula = "='Dashboard M13'!S20"
    @eval_fn
    def S8():
        s20_1 = Dashboard_M13.S20()
        return s20_1

@register(Charts_Data_M13)
class T8():
    # 'Charts_Data_M13'!T8
    value = 1.00129840518
    formula = "='Dashboard M13'!T20"
    @eval_fn
    def T8():
        t20_1 = Dashboard_M13.T20()
        return t20_1

@register(Charts_Data_M13)
class U8():
    # 'Charts_Data_M13'!U8
    value = 1.04830073827
    formula = "='Dashboard M13'!U20"
    @eval_fn
    def U8():
        u20_1 = Dashboard_M13.U20()
        return u20_1

@register(Charts_Data_M13)
class V8():
    # 'Charts_Data_M13'!V8
    value = 1.0767615879
    formula = "='Dashboard M13'!V20"
    @eval_fn
    def V8():
        v20_1 = Dashboard_M13.V20()
        return v20_1

@register(Charts_Data_M13)
class W8():
    # 'Charts_Data_M13'!W8
    value = 1.08632817811
    formula = "='Dashboard M13'!W20"
    @eval_fn
    def W8():
        w20_1 = Dashboard_M13.W20()
        return w20_1

@register(Charts_Data_M13)
class X8():
    # 'Charts_Data_M13'!X8
    value = 1.12603380302
    formula = "='Dashboard M13'!X20"
    @eval_fn
    def X8():
        x20_1 = Dashboard_M13.X20()
        return x20_1

@register(Charts_Data_M13)
class Y8():
    # 'Charts_Data_M13'!Y8
    value = 0.904626621229
    formula = "='Dashboard M13'!Y20"
    @eval_fn
    def Y8():
        y20_1 = Dashboard_M13.Y20()
        return y20_1

@register(Charts_Data_M13)
class Z8():
    # 'Charts_Data_M13'!Z8
    value = 0.883978897794
    formula = "='Dashboard M13'!Z20"
    @eval_fn
    def Z8():
        z20_1 = Dashboard_M13.Z20()
        return z20_1

@register(Charts_Data_M13)
class AA8():
    # 'Charts_Data_M13'!AA8
    value = 0.879965238623
    formula = "='Dashboard M13'!AA20"
    @eval_fn
    def AA8():
        aa20_1 = Dashboard_M13.AA20()
        return aa20_1

@register(Charts_Data_M13)
class AB8():
    # 'Charts_Data_M13'!AB8
    value = 0.904426798608
    formula = "='Dashboard M13'!AB20"
    @eval_fn
    def AB8():
        ab20_1 = Dashboard_M13.AB20()
        return ab20_1

@register(Charts_Data_M13)
class AC8():
    # 'Charts_Data_M13'!AC8
    value = 0
    formula = "='Dashboard M13'!AC20"
    @eval_fn
    def AC8():
        ac20_1 = Dashboard_M13.AC20()
        return ac20_1

@register(Charts_Data_M13)
class AD8():
    # 'Charts_Data_M13'!AD8
    value = 0
    formula = "='Dashboard M13'!AD20"
    @eval_fn
    def AD8():
        ad20_1 = Dashboard_M13.AD20()
        return ad20_1

@register(Charts_Data_M13)
class AE8():
    # 'Charts_Data_M13'!AE8
    value = 0
    formula = "='Dashboard M13'!AE20"
    @eval_fn
    def AE8():
        ae20_1 = Dashboard_M13.AE20()
        return ae20_1

@register(Charts_Data_M13)
class AF8():
    # 'Charts_Data_M13'!AF8
    value = 0
    formula = "='Dashboard M13'!AF20"
    @eval_fn
    def AF8():
        af20_1 = Dashboard_M13.AF20()
        return af20_1

@register(Charts_Data_M13)
class AG8():
    # 'Charts_Data_M13'!AG8
    value = 0
    formula = "='Dashboard M13'!AG20"
    @eval_fn
    def AG8():
        ag20_1 = Dashboard_M13.AG20()
        return ag20_1

@register(Charts_Data_M13)
class AH8():
    # 'Charts_Data_M13'!AH8
    value = 0
    formula = "='Dashboard M13'!AH20"
    @eval_fn
    def AH8():
        ah20_1 = Dashboard_M13.AH20()
        return ah20_1

@register(Charts_Data_M13)
class AI8():
    # 'Charts_Data_M13'!AI8
    value = 0
    formula = "='Dashboard M13'!AI20"
    @eval_fn
    def AI8():
        ai20_1 = Dashboard_M13.AI20()
        return ai20_1

@register(Charts_Data_M13)
class AJ8():
    # 'Charts_Data_M13'!AJ8
    value = 0
    formula = "='Dashboard M13'!AJ20"
    @eval_fn
    def AJ8():
        aj20_1 = Dashboard_M13.AJ20()
        return aj20_1

@register(Charts_Data_M13)
class AK8():
    # 'Charts_Data_M13'!AK8
    value = 0
    formula = "='Dashboard M13'!AK20"
    @eval_fn
    def AK8():
        ak20_1 = Dashboard_M13.AK20()
        return ak20_1

@register(Charts_Data_M13)
class AL8():
    # 'Charts_Data_M13'!AL8
    value = 0
    formula = "='Dashboard M13'!AL20"
    @eval_fn
    def AL8():
        al20_1 = Dashboard_M13.AL20()
        return al20_1

@register(Charts_Data_M13)
class AM8():
    # 'Charts_Data_M13'!AM8
    value = 0
    formula = "='Dashboard M13'!AM20"
    @eval_fn
    def AM8():
        am20_1 = Dashboard_M13.AM20()
        return am20_1

@register(Charts_Data_M13)
class AN8():
    # 'Charts_Data_M13'!AN8
    value = 0
    formula = "='Dashboard M13'!AN20"
    @eval_fn
    def AN8():
        an20_1 = Dashboard_M13.AN20()
        return an20_1

@register(Charts_Data_M13)
class AO8():
    # 'Charts_Data_M13'!AO8
    value = 0
    formula = "='Dashboard M13'!AO20"
    @eval_fn
    def AO8():
        ao20_1 = Dashboard_M13.AO20()
        return ao20_1

@register(Charts_Data_M13)
class AP8():
    # 'Charts_Data_M13'!AP8
    value = 0
    formula = "='Dashboard M13'!AP20"
    @eval_fn
    def AP8():
        ap20_1 = Dashboard_M13.AP20()
        return ap20_1

@register(Charts_Data_M13)
class AQ8():
    # 'Charts_Data_M13'!AQ8
    value = 0
    formula = "='Dashboard M13'!AQ20"
    @eval_fn
    def AQ8():
        aq20_1 = Dashboard_M13.AQ20()
        return aq20_1

@register(Charts_Data_M13)
class AR8():
    # 'Charts_Data_M13'!AR8
    value = 0
    formula = "='Dashboard M13'!AR20"
    @eval_fn
    def AR8():
        ar20_1 = Dashboard_M13.AR20()
        return ar20_1

@register(Charts_Data_M13)
class AS8():
    # 'Charts_Data_M13'!AS8
    value = 0
    formula = "='Dashboard M13'!AS20"
    @eval_fn
    def AS8():
        as20_1 = Dashboard_M13.AS20()
        return as20_1

@register(Charts_Data_M13)
class AT8():
    # 'Charts_Data_M13'!AT8
    value = 0
    formula = "='Dashboard M13'!AT20"
    @eval_fn
    def AT8():
        at20_1 = Dashboard_M13.AT20()
        return at20_1

@register(Charts_Data_M13)
class AU8():
    # 'Charts_Data_M13'!AU8
    value = 0
    formula = "='Dashboard M13'!AU20"
    @eval_fn
    def AU8():
        au20_1 = Dashboard_M13.AU20()
        return au20_1