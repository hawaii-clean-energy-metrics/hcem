# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_Data_M14 = Worksheet('Charts_Data_M14', 10, 10)



@register(Charts_Data_M14)
class A1():
    # 'Charts_Data_M14'!A1
    value = "Metric 14:"

@register(Charts_Data_M14)
class F1():
    # 'Charts_Data_M14'!F1
    value = "Notes"

@register(Charts_Data_M14)
class G1():
    # 'Charts_Data_M14'!G1
    value = 1990

@register(Charts_Data_M14)
class H1():
    # 'Charts_Data_M14'!H1
    value = 1991

@register(Charts_Data_M14)
class I1():
    # 'Charts_Data_M14'!I1
    value = 1992

@register(Charts_Data_M14)
class J1():
    # 'Charts_Data_M14'!J1
    value = 1993

@register(Charts_Data_M14)
class K1():
    # 'Charts_Data_M14'!K1
    value = 1994

@register(Charts_Data_M14)
class L1():
    # 'Charts_Data_M14'!L1
    value = 1995

@register(Charts_Data_M14)
class M1():
    # 'Charts_Data_M14'!M1
    value = 1996

@register(Charts_Data_M14)
class N1():
    # 'Charts_Data_M14'!N1
    value = 1997

@register(Charts_Data_M14)
class O1():
    # 'Charts_Data_M14'!O1
    value = 1998

@register(Charts_Data_M14)
class P1():
    # 'Charts_Data_M14'!P1
    value = 1999

@register(Charts_Data_M14)
class Q1():
    # 'Charts_Data_M14'!Q1
    value = 2000

@register(Charts_Data_M14)
class R1():
    # 'Charts_Data_M14'!R1
    value = 2001

@register(Charts_Data_M14)
class S1():
    # 'Charts_Data_M14'!S1
    value = 2002

@register(Charts_Data_M14)
class T1():
    # 'Charts_Data_M14'!T1
    value = 2003

@register(Charts_Data_M14)
class U1():
    # 'Charts_Data_M14'!U1
    value = 2004

@register(Charts_Data_M14)
class V1():
    # 'Charts_Data_M14'!V1
    value = 2005

@register(Charts_Data_M14)
class W1():
    # 'Charts_Data_M14'!W1
    value = 2006

@register(Charts_Data_M14)
class X1():
    # 'Charts_Data_M14'!X1
    value = 2007

@register(Charts_Data_M14)
class Y1():
    # 'Charts_Data_M14'!Y1
    value = 2008

@register(Charts_Data_M14)
class Z1():
    # 'Charts_Data_M14'!Z1
    value = 2009

@register(Charts_Data_M14)
class AA1():
    # 'Charts_Data_M14'!AA1
    value = 2010

@register(Charts_Data_M14)
class AB1():
    # 'Charts_Data_M14'!AB1
    value = 2011

@register(Charts_Data_M14)
class AC1():
    # 'Charts_Data_M14'!AC1
    value = 2012

@register(Charts_Data_M14)
class AD1():
    # 'Charts_Data_M14'!AD1
    value = 2013

@register(Charts_Data_M14)
class AE1():
    # 'Charts_Data_M14'!AE1
    value = 2014

@register(Charts_Data_M14)
class AF1():
    # 'Charts_Data_M14'!AF1
    value = 2015

@register(Charts_Data_M14)
class AG1():
    # 'Charts_Data_M14'!AG1
    value = 2016

@register(Charts_Data_M14)
class AH1():
    # 'Charts_Data_M14'!AH1
    value = 2017

@register(Charts_Data_M14)
class AI1():
    # 'Charts_Data_M14'!AI1
    value = 2018

@register(Charts_Data_M14)
class AJ1():
    # 'Charts_Data_M14'!AJ1
    value = 2019

@register(Charts_Data_M14)
class AK1():
    # 'Charts_Data_M14'!AK1
    value = 2020

@register(Charts_Data_M14)
class AL1():
    # 'Charts_Data_M14'!AL1
    value = 2021

@register(Charts_Data_M14)
class AM1():
    # 'Charts_Data_M14'!AM1
    value = 2022

@register(Charts_Data_M14)
class AN1():
    # 'Charts_Data_M14'!AN1
    value = 2023

@register(Charts_Data_M14)
class AO1():
    # 'Charts_Data_M14'!AO1
    value = 2024

@register(Charts_Data_M14)
class AP1():
    # 'Charts_Data_M14'!AP1
    value = 2025

@register(Charts_Data_M14)
class AQ1():
    # 'Charts_Data_M14'!AQ1
    value = 2026

@register(Charts_Data_M14)
class AR1():
    # 'Charts_Data_M14'!AR1
    value = 2027

@register(Charts_Data_M14)
class AS1():
    # 'Charts_Data_M14'!AS1
    value = 2028

@register(Charts_Data_M14)
class AT1():
    # 'Charts_Data_M14'!AT1
    value = 2029

@register(Charts_Data_M14)
class AU1():
    # 'Charts_Data_M14'!AU1
    value = 2030

@register(Charts_Data_M14)
class A2():
    # 'Charts_Data_M14'!A2
    value = "Graph Input"

@register(Charts_Data_M14)
class B2():
    # 'Charts_Data_M14'!B2
    value = "Percent of 1990 levels"

@register(Charts_Data_M14)
class C2():
    # 'Charts_Data_M14'!C2
    value = "   Commercial Energy Sector"

@register(Charts_Data_M14)
class F2():
    # 'Charts_Data_M14'!F2
    value = "Notes"

@register(Charts_Data_M14)
class G2():
    # 'Charts_Data_M14'!G2
    value = 0.754428115757
    formula = "=IF($B$4=$B$3,'Dashboard M14'!G6,'Dashboard M14'!G16)"
    @eval_fn
    def G2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        g6_1 = Dashboard_M14.G6()
        g16_1 = Dashboard_M14.G16()
        var_2 = IF(var_1, g6_1, g16_1)
        return var_2

@register(Charts_Data_M14)
class H2():
    # 'Charts_Data_M14'!H2
    value = 0.435180378659
    formula = "=IF($B$4=$B$3,'Dashboard M14'!H6,'Dashboard M14'!H16)"
    @eval_fn
    def H2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        h6_1 = Dashboard_M14.H6()
        h16_1 = Dashboard_M14.H16()
        var_2 = IF(var_1, h6_1, h16_1)
        return var_2

@register(Charts_Data_M14)
class I2():
    # 'Charts_Data_M14'!I2
    value = 0.920871969121
    formula = "=IF($B$4=$B$3,'Dashboard M14'!I6,'Dashboard M14'!I16)"
    @eval_fn
    def I2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        i6_1 = Dashboard_M14.I6()
        i16_1 = Dashboard_M14.I16()
        var_2 = IF(var_1, i6_1, i16_1)
        return var_2

@register(Charts_Data_M14)
class J2():
    # 'Charts_Data_M14'!J2
    value = 0.333504956037
    formula = "=IF($B$4=$B$3,'Dashboard M14'!J6,'Dashboard M14'!J16)"
    @eval_fn
    def J2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        j6_1 = Dashboard_M14.J6()
        j16_1 = Dashboard_M14.J16()
        var_2 = IF(var_1, j6_1, j16_1)
        return var_2

@register(Charts_Data_M14)
class K2():
    # 'Charts_Data_M14'!K2
    value = 0.513863487004
    formula = "=IF($B$4=$B$3,'Dashboard M14'!K6,'Dashboard M14'!K16)"
    @eval_fn
    def K2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        k6_1 = Dashboard_M14.K6()
        k16_1 = Dashboard_M14.K16()
        var_2 = IF(var_1, k6_1, k16_1)
        return var_2

@register(Charts_Data_M14)
class L2():
    # 'Charts_Data_M14'!L2
    value = 0.318442892246
    formula = "=IF($B$4=$B$3,'Dashboard M14'!L6,'Dashboard M14'!L16)"
    @eval_fn
    def L2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        l6_1 = Dashboard_M14.L6()
        l16_1 = Dashboard_M14.L16()
        var_2 = IF(var_1, l6_1, l16_1)
        return var_2

@register(Charts_Data_M14)
class M2():
    # 'Charts_Data_M14'!M2
    value = 0.244364891755
    formula = "=IF($B$4=$B$3,'Dashboard M14'!M6,'Dashboard M14'!M16)"
    @eval_fn
    def M2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        m6_1 = Dashboard_M14.M6()
        m16_1 = Dashboard_M14.M16()
        var_2 = IF(var_1, m6_1, m16_1)
        return var_2

@register(Charts_Data_M14)
class N2():
    # 'Charts_Data_M14'!N2
    value = 0.308156846412
    formula = "=IF($B$4=$B$3,'Dashboard M14'!N6,'Dashboard M14'!N16)"
    @eval_fn
    def N2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        n6_1 = Dashboard_M14.N6()
        n16_1 = Dashboard_M14.N16()
        var_2 = IF(var_1, n6_1, n16_1)
        return var_2

@register(Charts_Data_M14)
class O2():
    # 'Charts_Data_M14'!O2
    value = 1.09377157967
    formula = "=IF($B$4=$B$3,'Dashboard M14'!O6,'Dashboard M14'!O16)"
    @eval_fn
    def O2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        o6_1 = Dashboard_M14.O6()
        o16_1 = Dashboard_M14.O16()
        var_2 = IF(var_1, o6_1, o16_1)
        return var_2

@register(Charts_Data_M14)
class P2():
    # 'Charts_Data_M14'!P2
    value = 0.27195740756
    formula = "=IF($B$4=$B$3,'Dashboard M14'!P6,'Dashboard M14'!P16)"
    @eval_fn
    def P2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        p6_1 = Dashboard_M14.P6()
        p16_1 = Dashboard_M14.P16()
        var_2 = IF(var_1, p6_1, p16_1)
        return var_2

@register(Charts_Data_M14)
class Q2():
    # 'Charts_Data_M14'!Q2
    value = 0.276442083883
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Q6,'Dashboard M14'!Q16)"
    @eval_fn
    def Q2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        q6_1 = Dashboard_M14.Q6()
        q16_1 = Dashboard_M14.Q16()
        var_2 = IF(var_1, q6_1, q16_1)
        return var_2

@register(Charts_Data_M14)
class R2():
    # 'Charts_Data_M14'!R2
    value = 0.238465883308
    formula = "=IF($B$4=$B$3,'Dashboard M14'!R6,'Dashboard M14'!R16)"
    @eval_fn
    def R2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        r6_1 = Dashboard_M14.R6()
        r16_1 = Dashboard_M14.R16()
        var_2 = IF(var_1, r6_1, r16_1)
        return var_2

@register(Charts_Data_M14)
class S2():
    # 'Charts_Data_M14'!S2
    value = 0.311535298359
    formula = "=IF($B$4=$B$3,'Dashboard M14'!S6,'Dashboard M14'!S16)"
    @eval_fn
    def S2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        s6_1 = Dashboard_M14.S6()
        s16_1 = Dashboard_M14.S16()
        var_2 = IF(var_1, s6_1, s16_1)
        return var_2

@register(Charts_Data_M14)
class T2():
    # 'Charts_Data_M14'!T2
    value = 0.280284505939
    formula = "=IF($B$4=$B$3,'Dashboard M14'!T6,'Dashboard M14'!T16)"
    @eval_fn
    def T2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        t6_1 = Dashboard_M14.T6()
        t16_1 = Dashboard_M14.T16()
        var_2 = IF(var_1, t6_1, t16_1)
        return var_2

@register(Charts_Data_M14)
class U2():
    # 'Charts_Data_M14'!U2
    value = 0.329107025018
    formula = "=IF($B$4=$B$3,'Dashboard M14'!U6,'Dashboard M14'!U16)"
    @eval_fn
    def U2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        u6_1 = Dashboard_M14.U6()
        u16_1 = Dashboard_M14.U16()
        var_2 = IF(var_1, u6_1, u16_1)
        return var_2

@register(Charts_Data_M14)
class V2():
    # 'Charts_Data_M14'!V2
    value = 0.331705363332
    formula = "=IF($B$4=$B$3,'Dashboard M14'!V6,'Dashboard M14'!V16)"
    @eval_fn
    def V2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        v6_1 = Dashboard_M14.V6()
        v16_1 = Dashboard_M14.V16()
        var_2 = IF(var_1, v6_1, v16_1)
        return var_2

@register(Charts_Data_M14)
class W2():
    # 'Charts_Data_M14'!W2
    value = 0.33495875651
    formula = "=IF($B$4=$B$3,'Dashboard M14'!W6,'Dashboard M14'!W16)"
    @eval_fn
    def W2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        w6_1 = Dashboard_M14.W6()
        w16_1 = Dashboard_M14.W16()
        var_2 = IF(var_1, w6_1, w16_1)
        return var_2

@register(Charts_Data_M14)
class X2():
    # 'Charts_Data_M14'!X2
    value = 0.279597654134
    formula = "=IF($B$4=$B$3,'Dashboard M14'!X6,'Dashboard M14'!X16)"
    @eval_fn
    def X2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        x6_1 = Dashboard_M14.X6()
        x16_1 = Dashboard_M14.X16()
        var_2 = IF(var_1, x6_1, x16_1)
        return var_2

@register(Charts_Data_M14)
class Y2():
    # 'Charts_Data_M14'!Y2
    value = 0.292587539466
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Y6,'Dashboard M14'!Y16)"
    @eval_fn
    def Y2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        y6_1 = Dashboard_M14.Y6()
        y16_1 = Dashboard_M14.Y16()
        var_2 = IF(var_1, y6_1, y16_1)
        return var_2

@register(Charts_Data_M14)
class Z2():
    # 'Charts_Data_M14'!Z2
    value = 0.345927797314
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Z6,'Dashboard M14'!Z16)"
    @eval_fn
    def Z2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        z6_1 = Dashboard_M14.Z6()
        z16_1 = Dashboard_M14.Z16()
        var_2 = IF(var_1, z6_1, z16_1)
        return var_2

@register(Charts_Data_M14)
class AA2():
    # 'Charts_Data_M14'!AA2
    value = 0.342057717279
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AA6,'Dashboard M14'!AA16)"
    @eval_fn
    def AA2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aa6_1 = Dashboard_M14.AA6()
        aa16_1 = Dashboard_M14.AA16()
        var_2 = IF(var_1, aa6_1, aa16_1)
        return var_2

@register(Charts_Data_M14)
class AB2():
    # 'Charts_Data_M14'!AB2
    value = 0.384616764301
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AB6,'Dashboard M14'!AB16)"
    @eval_fn
    def AB2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ab6_1 = Dashboard_M14.AB6()
        ab16_1 = Dashboard_M14.AB16()
        var_2 = IF(var_1, ab6_1, ab16_1)
        return var_2

@register(Charts_Data_M14)
class AC2():
    # 'Charts_Data_M14'!AC2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AC6,'Dashboard M14'!AC16)"
    @eval_fn
    def AC2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ac6_1 = Dashboard_M14.AC6()
        ac16_1 = Dashboard_M14.AC16()
        var_2 = IF(var_1, ac6_1, ac16_1)
        return var_2

@register(Charts_Data_M14)
class AD2():
    # 'Charts_Data_M14'!AD2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AD6,'Dashboard M14'!AD16)"
    @eval_fn
    def AD2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ad6_1 = Dashboard_M14.AD6()
        ad16_1 = Dashboard_M14.AD16()
        var_2 = IF(var_1, ad6_1, ad16_1)
        return var_2

@register(Charts_Data_M14)
class AE2():
    # 'Charts_Data_M14'!AE2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AE6,'Dashboard M14'!AE16)"
    @eval_fn
    def AE2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ae6_1 = Dashboard_M14.AE6()
        ae16_1 = Dashboard_M14.AE16()
        var_2 = IF(var_1, ae6_1, ae16_1)
        return var_2

@register(Charts_Data_M14)
class AF2():
    # 'Charts_Data_M14'!AF2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AF6,'Dashboard M14'!AF16)"
    @eval_fn
    def AF2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        af6_1 = Dashboard_M14.AF6()
        af16_1 = Dashboard_M14.AF16()
        var_2 = IF(var_1, af6_1, af16_1)
        return var_2

@register(Charts_Data_M14)
class AG2():
    # 'Charts_Data_M14'!AG2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AG6,'Dashboard M14'!AG16)"
    @eval_fn
    def AG2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ag6_1 = Dashboard_M14.AG6()
        ag16_1 = Dashboard_M14.AG16()
        var_2 = IF(var_1, ag6_1, ag16_1)
        return var_2

@register(Charts_Data_M14)
class AH2():
    # 'Charts_Data_M14'!AH2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AH6,'Dashboard M14'!AH16)"
    @eval_fn
    def AH2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ah6_1 = Dashboard_M14.AH6()
        ah16_1 = Dashboard_M14.AH16()
        var_2 = IF(var_1, ah6_1, ah16_1)
        return var_2

@register(Charts_Data_M14)
class AI2():
    # 'Charts_Data_M14'!AI2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AI6,'Dashboard M14'!AI16)"
    @eval_fn
    def AI2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ai6_1 = Dashboard_M14.AI6()
        ai16_1 = Dashboard_M14.AI16()
        var_2 = IF(var_1, ai6_1, ai16_1)
        return var_2

@register(Charts_Data_M14)
class AJ2():
    # 'Charts_Data_M14'!AJ2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AJ6,'Dashboard M14'!AJ16)"
    @eval_fn
    def AJ2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aj6_1 = Dashboard_M14.AJ6()
        aj16_1 = Dashboard_M14.AJ16()
        var_2 = IF(var_1, aj6_1, aj16_1)
        return var_2

@register(Charts_Data_M14)
class AK2():
    # 'Charts_Data_M14'!AK2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AK6,'Dashboard M14'!AK16)"
    @eval_fn
    def AK2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ak6_1 = Dashboard_M14.AK6()
        ak16_1 = Dashboard_M14.AK16()
        var_2 = IF(var_1, ak6_1, ak16_1)
        return var_2

@register(Charts_Data_M14)
class AL2():
    # 'Charts_Data_M14'!AL2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AL6,'Dashboard M14'!AL16)"
    @eval_fn
    def AL2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        al6_1 = Dashboard_M14.AL6()
        al16_1 = Dashboard_M14.AL16()
        var_2 = IF(var_1, al6_1, al16_1)
        return var_2

@register(Charts_Data_M14)
class AM2():
    # 'Charts_Data_M14'!AM2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AM6,'Dashboard M14'!AM16)"
    @eval_fn
    def AM2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        am6_1 = Dashboard_M14.AM6()
        am16_1 = Dashboard_M14.AM16()
        var_2 = IF(var_1, am6_1, am16_1)
        return var_2

@register(Charts_Data_M14)
class AN2():
    # 'Charts_Data_M14'!AN2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AN6,'Dashboard M14'!AN16)"
    @eval_fn
    def AN2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        an6_1 = Dashboard_M14.AN6()
        an16_1 = Dashboard_M14.AN16()
        var_2 = IF(var_1, an6_1, an16_1)
        return var_2

@register(Charts_Data_M14)
class AO2():
    # 'Charts_Data_M14'!AO2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AO6,'Dashboard M14'!AO16)"
    @eval_fn
    def AO2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ao6_1 = Dashboard_M14.AO6()
        ao16_1 = Dashboard_M14.AO16()
        var_2 = IF(var_1, ao6_1, ao16_1)
        return var_2

@register(Charts_Data_M14)
class AP2():
    # 'Charts_Data_M14'!AP2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AP6,'Dashboard M14'!AP16)"
    @eval_fn
    def AP2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ap6_1 = Dashboard_M14.AP6()
        ap16_1 = Dashboard_M14.AP16()
        var_2 = IF(var_1, ap6_1, ap16_1)
        return var_2

@register(Charts_Data_M14)
class AQ2():
    # 'Charts_Data_M14'!AQ2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AQ6,'Dashboard M14'!AQ16)"
    @eval_fn
    def AQ2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aq6_1 = Dashboard_M14.AQ6()
        aq16_1 = Dashboard_M14.AQ16()
        var_2 = IF(var_1, aq6_1, aq16_1)
        return var_2

@register(Charts_Data_M14)
class AR2():
    # 'Charts_Data_M14'!AR2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AR6,'Dashboard M14'!AR16)"
    @eval_fn
    def AR2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ar6_1 = Dashboard_M14.AR6()
        ar16_1 = Dashboard_M14.AR16()
        var_2 = IF(var_1, ar6_1, ar16_1)
        return var_2

@register(Charts_Data_M14)
class AS2():
    # 'Charts_Data_M14'!AS2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AS6,'Dashboard M14'!AS16)"
    @eval_fn
    def AS2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        as6_1 = Dashboard_M14.AS6()
        as16_1 = Dashboard_M14.AS16()
        var_2 = IF(var_1, as6_1, as16_1)
        return var_2

@register(Charts_Data_M14)
class AT2():
    # 'Charts_Data_M14'!AT2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AT6,'Dashboard M14'!AT16)"
    @eval_fn
    def AT2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        at6_1 = Dashboard_M14.AT6()
        at16_1 = Dashboard_M14.AT16()
        var_2 = IF(var_1, at6_1, at16_1)
        return var_2

@register(Charts_Data_M14)
class AU2():
    # 'Charts_Data_M14'!AU2
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AU6,'Dashboard M14'!AU16)"
    @eval_fn
    def AU2():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        au6_1 = Dashboard_M14.AU6()
        au16_1 = Dashboard_M14.AU16()
        var_2 = IF(var_1, au6_1, au16_1)
        return var_2

@register(Charts_Data_M14)
class B3():
    # 'Charts_Data_M14'!B3
    value = "Total Emissions (MMTCO2E)"

@register(Charts_Data_M14)
class C3():
    # 'Charts_Data_M14'!C3
    value = "   Industrial Energy Sector"

@register(Charts_Data_M14)
class F3():
    # 'Charts_Data_M14'!F3
    value = "Notes"

@register(Charts_Data_M14)
class G3():
    # 'Charts_Data_M14'!G3
    value = 2.11513682963
    formula = "=IF($B$4=$B$3,'Dashboard M14'!G7,'Dashboard M14'!G17)"
    @eval_fn
    def G3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        g7_1 = Dashboard_M14.G7()
        g17_1 = Dashboard_M14.G17()
        var_2 = IF(var_1, g7_1, g17_1)
        return var_2

@register(Charts_Data_M14)
class H3():
    # 'Charts_Data_M14'!H3
    value = 2.02067534262
    formula = "=IF($B$4=$B$3,'Dashboard M14'!H7,'Dashboard M14'!H17)"
    @eval_fn
    def H3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        h7_1 = Dashboard_M14.H7()
        h17_1 = Dashboard_M14.H17()
        var_2 = IF(var_1, h7_1, h17_1)
        return var_2

@register(Charts_Data_M14)
class I3():
    # 'Charts_Data_M14'!I3
    value = 1.98026408929
    formula = "=IF($B$4=$B$3,'Dashboard M14'!I7,'Dashboard M14'!I17)"
    @eval_fn
    def I3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        i7_1 = Dashboard_M14.I7()
        i17_1 = Dashboard_M14.I17()
        var_2 = IF(var_1, i7_1, i17_1)
        return var_2

@register(Charts_Data_M14)
class J3():
    # 'Charts_Data_M14'!J3
    value = 1.83940515634
    formula = "=IF($B$4=$B$3,'Dashboard M14'!J7,'Dashboard M14'!J17)"
    @eval_fn
    def J3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        j7_1 = Dashboard_M14.J7()
        j17_1 = Dashboard_M14.J17()
        var_2 = IF(var_1, j7_1, j17_1)
        return var_2

@register(Charts_Data_M14)
class K3():
    # 'Charts_Data_M14'!K3
    value = 2.03053367591
    formula = "=IF($B$4=$B$3,'Dashboard M14'!K7,'Dashboard M14'!K17)"
    @eval_fn
    def K3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        k7_1 = Dashboard_M14.K7()
        k17_1 = Dashboard_M14.K17()
        var_2 = IF(var_1, k7_1, k17_1)
        return var_2

@register(Charts_Data_M14)
class L3():
    # 'Charts_Data_M14'!L3
    value = 1.98092370133
    formula = "=IF($B$4=$B$3,'Dashboard M14'!L7,'Dashboard M14'!L17)"
    @eval_fn
    def L3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        l7_1 = Dashboard_M14.L7()
        l17_1 = Dashboard_M14.L17()
        var_2 = IF(var_1, l7_1, l17_1)
        return var_2

@register(Charts_Data_M14)
class M3():
    # 'Charts_Data_M14'!M3
    value = 2.07918105152
    formula = "=IF($B$4=$B$3,'Dashboard M14'!M7,'Dashboard M14'!M17)"
    @eval_fn
    def M3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        m7_1 = Dashboard_M14.M7()
        m17_1 = Dashboard_M14.M17()
        var_2 = IF(var_1, m7_1, m17_1)
        return var_2

@register(Charts_Data_M14)
class N3():
    # 'Charts_Data_M14'!N3
    value = 1.96927163465
    formula = "=IF($B$4=$B$3,'Dashboard M14'!N7,'Dashboard M14'!N17)"
    @eval_fn
    def N3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        n7_1 = Dashboard_M14.N7()
        n17_1 = Dashboard_M14.N17()
        var_2 = IF(var_1, n7_1, n17_1)
        return var_2

@register(Charts_Data_M14)
class O3():
    # 'Charts_Data_M14'!O3
    value = 1.47786913976
    formula = "=IF($B$4=$B$3,'Dashboard M14'!O7,'Dashboard M14'!O17)"
    @eval_fn
    def O3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        o7_1 = Dashboard_M14.O7()
        o17_1 = Dashboard_M14.O17()
        var_2 = IF(var_1, o7_1, o17_1)
        return var_2

@register(Charts_Data_M14)
class P3():
    # 'Charts_Data_M14'!P3
    value = 1.31042751719
    formula = "=IF($B$4=$B$3,'Dashboard M14'!P7,'Dashboard M14'!P17)"
    @eval_fn
    def P3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        p7_1 = Dashboard_M14.P7()
        p17_1 = Dashboard_M14.P17()
        var_2 = IF(var_1, p7_1, p17_1)
        return var_2

@register(Charts_Data_M14)
class Q3():
    # 'Charts_Data_M14'!Q3
    value = 1.33767560375
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Q7,'Dashboard M14'!Q17)"
    @eval_fn
    def Q3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        q7_1 = Dashboard_M14.Q7()
        q17_1 = Dashboard_M14.Q17()
        var_2 = IF(var_1, q7_1, q17_1)
        return var_2

@register(Charts_Data_M14)
class R3():
    # 'Charts_Data_M14'!R3
    value = 1.34088405453
    formula = "=IF($B$4=$B$3,'Dashboard M14'!R7,'Dashboard M14'!R17)"
    @eval_fn
    def R3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        r7_1 = Dashboard_M14.R7()
        r17_1 = Dashboard_M14.R17()
        var_2 = IF(var_1, r7_1, r17_1)
        return var_2

@register(Charts_Data_M14)
class S3():
    # 'Charts_Data_M14'!S3
    value = 1.50302190878
    formula = "=IF($B$4=$B$3,'Dashboard M14'!S7,'Dashboard M14'!S17)"
    @eval_fn
    def S3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        s7_1 = Dashboard_M14.S7()
        s17_1 = Dashboard_M14.S17()
        var_2 = IF(var_1, s7_1, s17_1)
        return var_2

@register(Charts_Data_M14)
class T3():
    # 'Charts_Data_M14'!T3
    value = 1.52792941107
    formula = "=IF($B$4=$B$3,'Dashboard M14'!T7,'Dashboard M14'!T17)"
    @eval_fn
    def T3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        t7_1 = Dashboard_M14.T7()
        t17_1 = Dashboard_M14.T17()
        var_2 = IF(var_1, t7_1, t17_1)
        return var_2

@register(Charts_Data_M14)
class U3():
    # 'Charts_Data_M14'!U3
    value = 1.51256484209
    formula = "=IF($B$4=$B$3,'Dashboard M14'!U7,'Dashboard M14'!U17)"
    @eval_fn
    def U3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        u7_1 = Dashboard_M14.U7()
        u17_1 = Dashboard_M14.U17()
        var_2 = IF(var_1, u7_1, u17_1)
        return var_2

@register(Charts_Data_M14)
class V3():
    # 'Charts_Data_M14'!V3
    value = 1.76591433937
    formula = "=IF($B$4=$B$3,'Dashboard M14'!V7,'Dashboard M14'!V17)"
    @eval_fn
    def V3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        v7_1 = Dashboard_M14.V7()
        v17_1 = Dashboard_M14.V17()
        var_2 = IF(var_1, v7_1, v17_1)
        return var_2

@register(Charts_Data_M14)
class W3():
    # 'Charts_Data_M14'!W3
    value = 1.79678470986
    formula = "=IF($B$4=$B$3,'Dashboard M14'!W7,'Dashboard M14'!W17)"
    @eval_fn
    def W3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        w7_1 = Dashboard_M14.W7()
        w17_1 = Dashboard_M14.W17()
        var_2 = IF(var_1, w7_1, w17_1)
        return var_2

@register(Charts_Data_M14)
class X3():
    # 'Charts_Data_M14'!X3
    value = 1.62942254952
    formula = "=IF($B$4=$B$3,'Dashboard M14'!X7,'Dashboard M14'!X17)"
    @eval_fn
    def X3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        x7_1 = Dashboard_M14.X7()
        x17_1 = Dashboard_M14.X17()
        var_2 = IF(var_1, x7_1, x17_1)
        return var_2

@register(Charts_Data_M14)
class Y3():
    # 'Charts_Data_M14'!Y3
    value = 1.42537982957
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Y7,'Dashboard M14'!Y17)"
    @eval_fn
    def Y3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        y7_1 = Dashboard_M14.Y7()
        y17_1 = Dashboard_M14.Y17()
        var_2 = IF(var_1, y7_1, y17_1)
        return var_2

@register(Charts_Data_M14)
class Z3():
    # 'Charts_Data_M14'!Z3
    value = 1.40620451924
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Z7,'Dashboard M14'!Z17)"
    @eval_fn
    def Z3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        z7_1 = Dashboard_M14.Z7()
        z17_1 = Dashboard_M14.Z17()
        var_2 = IF(var_1, z7_1, z17_1)
        return var_2

@register(Charts_Data_M14)
class AA3():
    # 'Charts_Data_M14'!AA3
    value = 1.39046598306
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AA7,'Dashboard M14'!AA17)"
    @eval_fn
    def AA3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aa7_1 = Dashboard_M14.AA7()
        aa17_1 = Dashboard_M14.AA17()
        var_2 = IF(var_1, aa7_1, aa17_1)
        return var_2

@register(Charts_Data_M14)
class AB3():
    # 'Charts_Data_M14'!AB3
    value = 1.43228488783
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AB7,'Dashboard M14'!AB17)"
    @eval_fn
    def AB3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ab7_1 = Dashboard_M14.AB7()
        ab17_1 = Dashboard_M14.AB17()
        var_2 = IF(var_1, ab7_1, ab17_1)
        return var_2

@register(Charts_Data_M14)
class AC3():
    # 'Charts_Data_M14'!AC3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AC7,'Dashboard M14'!AC17)"
    @eval_fn
    def AC3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ac7_1 = Dashboard_M14.AC7()
        ac17_1 = Dashboard_M14.AC17()
        var_2 = IF(var_1, ac7_1, ac17_1)
        return var_2

@register(Charts_Data_M14)
class AD3():
    # 'Charts_Data_M14'!AD3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AD7,'Dashboard M14'!AD17)"
    @eval_fn
    def AD3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ad7_1 = Dashboard_M14.AD7()
        ad17_1 = Dashboard_M14.AD17()
        var_2 = IF(var_1, ad7_1, ad17_1)
        return var_2

@register(Charts_Data_M14)
class AE3():
    # 'Charts_Data_M14'!AE3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AE7,'Dashboard M14'!AE17)"
    @eval_fn
    def AE3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ae7_1 = Dashboard_M14.AE7()
        ae17_1 = Dashboard_M14.AE17()
        var_2 = IF(var_1, ae7_1, ae17_1)
        return var_2

@register(Charts_Data_M14)
class AF3():
    # 'Charts_Data_M14'!AF3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AF7,'Dashboard M14'!AF17)"
    @eval_fn
    def AF3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        af7_1 = Dashboard_M14.AF7()
        af17_1 = Dashboard_M14.AF17()
        var_2 = IF(var_1, af7_1, af17_1)
        return var_2

@register(Charts_Data_M14)
class AG3():
    # 'Charts_Data_M14'!AG3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AG7,'Dashboard M14'!AG17)"
    @eval_fn
    def AG3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ag7_1 = Dashboard_M14.AG7()
        ag17_1 = Dashboard_M14.AG17()
        var_2 = IF(var_1, ag7_1, ag17_1)
        return var_2

@register(Charts_Data_M14)
class AH3():
    # 'Charts_Data_M14'!AH3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AH7,'Dashboard M14'!AH17)"
    @eval_fn
    def AH3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ah7_1 = Dashboard_M14.AH7()
        ah17_1 = Dashboard_M14.AH17()
        var_2 = IF(var_1, ah7_1, ah17_1)
        return var_2

@register(Charts_Data_M14)
class AI3():
    # 'Charts_Data_M14'!AI3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AI7,'Dashboard M14'!AI17)"
    @eval_fn
    def AI3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ai7_1 = Dashboard_M14.AI7()
        ai17_1 = Dashboard_M14.AI17()
        var_2 = IF(var_1, ai7_1, ai17_1)
        return var_2

@register(Charts_Data_M14)
class AJ3():
    # 'Charts_Data_M14'!AJ3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AJ7,'Dashboard M14'!AJ17)"
    @eval_fn
    def AJ3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aj7_1 = Dashboard_M14.AJ7()
        aj17_1 = Dashboard_M14.AJ17()
        var_2 = IF(var_1, aj7_1, aj17_1)
        return var_2

@register(Charts_Data_M14)
class AK3():
    # 'Charts_Data_M14'!AK3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AK7,'Dashboard M14'!AK17)"
    @eval_fn
    def AK3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ak7_1 = Dashboard_M14.AK7()
        ak17_1 = Dashboard_M14.AK17()
        var_2 = IF(var_1, ak7_1, ak17_1)
        return var_2

@register(Charts_Data_M14)
class AL3():
    # 'Charts_Data_M14'!AL3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AL7,'Dashboard M14'!AL17)"
    @eval_fn
    def AL3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        al7_1 = Dashboard_M14.AL7()
        al17_1 = Dashboard_M14.AL17()
        var_2 = IF(var_1, al7_1, al17_1)
        return var_2

@register(Charts_Data_M14)
class AM3():
    # 'Charts_Data_M14'!AM3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AM7,'Dashboard M14'!AM17)"
    @eval_fn
    def AM3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        am7_1 = Dashboard_M14.AM7()
        am17_1 = Dashboard_M14.AM17()
        var_2 = IF(var_1, am7_1, am17_1)
        return var_2

@register(Charts_Data_M14)
class AN3():
    # 'Charts_Data_M14'!AN3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AN7,'Dashboard M14'!AN17)"
    @eval_fn
    def AN3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        an7_1 = Dashboard_M14.AN7()
        an17_1 = Dashboard_M14.AN17()
        var_2 = IF(var_1, an7_1, an17_1)
        return var_2

@register(Charts_Data_M14)
class AO3():
    # 'Charts_Data_M14'!AO3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AO7,'Dashboard M14'!AO17)"
    @eval_fn
    def AO3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ao7_1 = Dashboard_M14.AO7()
        ao17_1 = Dashboard_M14.AO17()
        var_2 = IF(var_1, ao7_1, ao17_1)
        return var_2

@register(Charts_Data_M14)
class AP3():
    # 'Charts_Data_M14'!AP3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AP7,'Dashboard M14'!AP17)"
    @eval_fn
    def AP3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ap7_1 = Dashboard_M14.AP7()
        ap17_1 = Dashboard_M14.AP17()
        var_2 = IF(var_1, ap7_1, ap17_1)
        return var_2

@register(Charts_Data_M14)
class AQ3():
    # 'Charts_Data_M14'!AQ3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AQ7,'Dashboard M14'!AQ17)"
    @eval_fn
    def AQ3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aq7_1 = Dashboard_M14.AQ7()
        aq17_1 = Dashboard_M14.AQ17()
        var_2 = IF(var_1, aq7_1, aq17_1)
        return var_2

@register(Charts_Data_M14)
class AR3():
    # 'Charts_Data_M14'!AR3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AR7,'Dashboard M14'!AR17)"
    @eval_fn
    def AR3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ar7_1 = Dashboard_M14.AR7()
        ar17_1 = Dashboard_M14.AR17()
        var_2 = IF(var_1, ar7_1, ar17_1)
        return var_2

@register(Charts_Data_M14)
class AS3():
    # 'Charts_Data_M14'!AS3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AS7,'Dashboard M14'!AS17)"
    @eval_fn
    def AS3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        as7_1 = Dashboard_M14.AS7()
        as17_1 = Dashboard_M14.AS17()
        var_2 = IF(var_1, as7_1, as17_1)
        return var_2

@register(Charts_Data_M14)
class AT3():
    # 'Charts_Data_M14'!AT3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AT7,'Dashboard M14'!AT17)"
    @eval_fn
    def AT3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        at7_1 = Dashboard_M14.AT7()
        at17_1 = Dashboard_M14.AT17()
        var_2 = IF(var_1, at7_1, at17_1)
        return var_2

@register(Charts_Data_M14)
class AU3():
    # 'Charts_Data_M14'!AU3
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AU7,'Dashboard M14'!AU17)"
    @eval_fn
    def AU3():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        au7_1 = Dashboard_M14.AU7()
        au17_1 = Dashboard_M14.AU17()
        var_2 = IF(var_1, au7_1, au17_1)
        return var_2

@register(Charts_Data_M14)
class B4():
    # 'Charts_Data_M14'!B4
    value = "Total Emissions (MMTCO2E)"
    formula = "=IF('Charts M14'!A1=1,'Charts Data M14'!B2,'Charts Data M14'!B3)"
    @eval_fn
    def B4():
        a1_1 = Charts_M14.A1()
        var_1 = equal(a1_1, 1)
        b2_1 = Charts_Data_M14.B2()
        b3_1 = Charts_Data_M14.B3()
        var_2 = IF(var_1, b2_1, b3_1)
        return var_2

@register(Charts_Data_M14)
class C4():
    # 'Charts_Data_M14'!C4
    value = "   Residential Energy Sector"

@register(Charts_Data_M14)
class F4():
    # 'Charts_Data_M14'!F4
    value = "Notes"

@register(Charts_Data_M14)
class G4():
    # 'Charts_Data_M14'!G4
    value = 0.0456336688721
    formula = "=IF($B$4=$B$3,'Dashboard M14'!G8,'Dashboard M14'!G18)"
    @eval_fn
    def G4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        g8_1 = Dashboard_M14.G8()
        g18_1 = Dashboard_M14.G18()
        var_2 = IF(var_1, g8_1, g18_1)
        return var_2

@register(Charts_Data_M14)
class H4():
    # 'Charts_Data_M14'!H4
    value = 0.0451296345613
    formula = "=IF($B$4=$B$3,'Dashboard M14'!H8,'Dashboard M14'!H18)"
    @eval_fn
    def H4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        h8_1 = Dashboard_M14.H8()
        h18_1 = Dashboard_M14.H18()
        var_2 = IF(var_1, h8_1, h18_1)
        return var_2

@register(Charts_Data_M14)
class I4():
    # 'Charts_Data_M14'!I4
    value = 0.074969711129
    formula = "=IF($B$4=$B$3,'Dashboard M14'!I8,'Dashboard M14'!I18)"
    @eval_fn
    def I4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        i8_1 = Dashboard_M14.I8()
        i18_1 = Dashboard_M14.I18()
        var_2 = IF(var_1, i8_1, i18_1)
        return var_2

@register(Charts_Data_M14)
class J4():
    # 'Charts_Data_M14'!J4
    value = 0.0413900137658
    formula = "=IF($B$4=$B$3,'Dashboard M14'!J8,'Dashboard M14'!J18)"
    @eval_fn
    def J4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        j8_1 = Dashboard_M14.J8()
        j18_1 = Dashboard_M14.J18()
        var_2 = IF(var_1, j8_1, j18_1)
        return var_2

@register(Charts_Data_M14)
class K4():
    # 'Charts_Data_M14'!K4
    value = 0.0423649906708
    formula = "=IF($B$4=$B$3,'Dashboard M14'!K8,'Dashboard M14'!K18)"
    @eval_fn
    def K4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        k8_1 = Dashboard_M14.K8()
        k18_1 = Dashboard_M14.K18()
        var_2 = IF(var_1, k8_1, k18_1)
        return var_2

@register(Charts_Data_M14)
class L4():
    # 'Charts_Data_M14'!L4
    value = 0.0416641679553
    formula = "=IF($B$4=$B$3,'Dashboard M14'!L8,'Dashboard M14'!L18)"
    @eval_fn
    def L4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        l8_1 = Dashboard_M14.L8()
        l18_1 = Dashboard_M14.L18()
        var_2 = IF(var_1, l8_1, l18_1)
        return var_2

@register(Charts_Data_M14)
class M4():
    # 'Charts_Data_M14'!M4
    value = 0.0415642015681
    formula = "=IF($B$4=$B$3,'Dashboard M14'!M8,'Dashboard M14'!M18)"
    @eval_fn
    def M4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        m8_1 = Dashboard_M14.M8()
        m18_1 = Dashboard_M14.M18()
        var_2 = IF(var_1, m8_1, m18_1)
        return var_2

@register(Charts_Data_M14)
class N4():
    # 'Charts_Data_M14'!N4
    value = 0.0492828747902
    formula = "=IF($B$4=$B$3,'Dashboard M14'!N8,'Dashboard M14'!N18)"
    @eval_fn
    def N4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        n8_1 = Dashboard_M14.N8()
        n18_1 = Dashboard_M14.N18()
        var_2 = IF(var_1, n8_1, n18_1)
        return var_2

@register(Charts_Data_M14)
class O4():
    # 'Charts_Data_M14'!O4
    value = 0.0891578162787
    formula = "=IF($B$4=$B$3,'Dashboard M14'!O8,'Dashboard M14'!O18)"
    @eval_fn
    def O4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        o8_1 = Dashboard_M14.O8()
        o18_1 = Dashboard_M14.O18()
        var_2 = IF(var_1, o8_1, o18_1)
        return var_2

@register(Charts_Data_M14)
class P4():
    # 'Charts_Data_M14'!P4
    value = 0.0629892925889
    formula = "=IF($B$4=$B$3,'Dashboard M14'!P8,'Dashboard M14'!P18)"
    @eval_fn
    def P4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        p8_1 = Dashboard_M14.P8()
        p18_1 = Dashboard_M14.P18()
        var_2 = IF(var_1, p8_1, p18_1)
        return var_2

@register(Charts_Data_M14)
class Q4():
    # 'Charts_Data_M14'!Q4
    value = 0.0758022324814
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Q8,'Dashboard M14'!Q18)"
    @eval_fn
    def Q4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        q8_1 = Dashboard_M14.Q8()
        q18_1 = Dashboard_M14.Q18()
        var_2 = IF(var_1, q8_1, q18_1)
        return var_2

@register(Charts_Data_M14)
class R4():
    # 'Charts_Data_M14'!R4
    value = 0.0762450327054
    formula = "=IF($B$4=$B$3,'Dashboard M14'!R8,'Dashboard M14'!R18)"
    @eval_fn
    def R4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        r8_1 = Dashboard_M14.R8()
        r18_1 = Dashboard_M14.R18()
        var_2 = IF(var_1, r8_1, r18_1)
        return var_2

@register(Charts_Data_M14)
class S4():
    # 'Charts_Data_M14'!S4
    value = 0.0771355434496
    formula = "=IF($B$4=$B$3,'Dashboard M14'!S8,'Dashboard M14'!S18)"
    @eval_fn
    def S4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        s8_1 = Dashboard_M14.S8()
        s18_1 = Dashboard_M14.S18()
        var_2 = IF(var_1, s8_1, s18_1)
        return var_2

@register(Charts_Data_M14)
class T4():
    # 'Charts_Data_M14'!T4
    value = 0.0645523054587
    formula = "=IF($B$4=$B$3,'Dashboard M14'!T8,'Dashboard M14'!T18)"
    @eval_fn
    def T4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        t8_1 = Dashboard_M14.T8()
        t18_1 = Dashboard_M14.T18()
        var_2 = IF(var_1, t8_1, t18_1)
        return var_2

@register(Charts_Data_M14)
class U4():
    # 'Charts_Data_M14'!U4
    value = 0.0645690261298
    formula = "=IF($B$4=$B$3,'Dashboard M14'!U8,'Dashboard M14'!U18)"
    @eval_fn
    def U4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        u8_1 = Dashboard_M14.U8()
        u18_1 = Dashboard_M14.U18()
        var_2 = IF(var_1, u8_1, u18_1)
        return var_2

@register(Charts_Data_M14)
class V4():
    # 'Charts_Data_M14'!V4
    value = 0.0644251804163
    formula = "=IF($B$4=$B$3,'Dashboard M14'!V8,'Dashboard M14'!V18)"
    @eval_fn
    def V4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        v8_1 = Dashboard_M14.V8()
        v18_1 = Dashboard_M14.V18()
        var_2 = IF(var_1, v8_1, v18_1)
        return var_2

@register(Charts_Data_M14)
class W4():
    # 'Charts_Data_M14'!W4
    value = 0.0669868948928
    formula = "=IF($B$4=$B$3,'Dashboard M14'!W8,'Dashboard M14'!W18)"
    @eval_fn
    def W4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        w8_1 = Dashboard_M14.W8()
        w18_1 = Dashboard_M14.W18()
        var_2 = IF(var_1, w8_1, w18_1)
        return var_2

@register(Charts_Data_M14)
class X4():
    # 'Charts_Data_M14'!X4
    value = 0.058944768794
    formula = "=IF($B$4=$B$3,'Dashboard M14'!X8,'Dashboard M14'!X18)"
    @eval_fn
    def X4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        x8_1 = Dashboard_M14.X8()
        x18_1 = Dashboard_M14.X18()
        var_2 = IF(var_1, x8_1, x18_1)
        return var_2

@register(Charts_Data_M14)
class Y4():
    # 'Charts_Data_M14'!Y4
    value = 0.0918702240999
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Y8,'Dashboard M14'!Y18)"
    @eval_fn
    def Y4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        y8_1 = Dashboard_M14.Y8()
        y18_1 = Dashboard_M14.Y18()
        var_2 = IF(var_1, y8_1, y18_1)
        return var_2

@register(Charts_Data_M14)
class Z4():
    # 'Charts_Data_M14'!Z4
    value = 0.0859343526633
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Z8,'Dashboard M14'!Z18)"
    @eval_fn
    def Z4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        z8_1 = Dashboard_M14.Z8()
        z18_1 = Dashboard_M14.Z18()
        var_2 = IF(var_1, z8_1, z18_1)
        return var_2

@register(Charts_Data_M14)
class AA4():
    # 'Charts_Data_M14'!AA4
    value = 0.0847729324443
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AA8,'Dashboard M14'!AA18)"
    @eval_fn
    def AA4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aa8_1 = Dashboard_M14.AA8()
        aa18_1 = Dashboard_M14.AA18()
        var_2 = IF(var_1, aa8_1, aa18_1)
        return var_2

@register(Charts_Data_M14)
class AB4():
    # 'Charts_Data_M14'!AB4
    value = 0.0813057340829
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AB8,'Dashboard M14'!AB18)"
    @eval_fn
    def AB4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ab8_1 = Dashboard_M14.AB8()
        ab18_1 = Dashboard_M14.AB18()
        var_2 = IF(var_1, ab8_1, ab18_1)
        return var_2

@register(Charts_Data_M14)
class AC4():
    # 'Charts_Data_M14'!AC4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AC8,'Dashboard M14'!AC18)"
    @eval_fn
    def AC4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ac8_1 = Dashboard_M14.AC8()
        ac18_1 = Dashboard_M14.AC18()
        var_2 = IF(var_1, ac8_1, ac18_1)
        return var_2

@register(Charts_Data_M14)
class AD4():
    # 'Charts_Data_M14'!AD4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AD8,'Dashboard M14'!AD18)"
    @eval_fn
    def AD4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ad8_1 = Dashboard_M14.AD8()
        ad18_1 = Dashboard_M14.AD18()
        var_2 = IF(var_1, ad8_1, ad18_1)
        return var_2

@register(Charts_Data_M14)
class AE4():
    # 'Charts_Data_M14'!AE4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AE8,'Dashboard M14'!AE18)"
    @eval_fn
    def AE4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ae8_1 = Dashboard_M14.AE8()
        ae18_1 = Dashboard_M14.AE18()
        var_2 = IF(var_1, ae8_1, ae18_1)
        return var_2

@register(Charts_Data_M14)
class AF4():
    # 'Charts_Data_M14'!AF4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AF8,'Dashboard M14'!AF18)"
    @eval_fn
    def AF4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        af8_1 = Dashboard_M14.AF8()
        af18_1 = Dashboard_M14.AF18()
        var_2 = IF(var_1, af8_1, af18_1)
        return var_2

@register(Charts_Data_M14)
class AG4():
    # 'Charts_Data_M14'!AG4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AG8,'Dashboard M14'!AG18)"
    @eval_fn
    def AG4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ag8_1 = Dashboard_M14.AG8()
        ag18_1 = Dashboard_M14.AG18()
        var_2 = IF(var_1, ag8_1, ag18_1)
        return var_2

@register(Charts_Data_M14)
class AH4():
    # 'Charts_Data_M14'!AH4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AH8,'Dashboard M14'!AH18)"
    @eval_fn
    def AH4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ah8_1 = Dashboard_M14.AH8()
        ah18_1 = Dashboard_M14.AH18()
        var_2 = IF(var_1, ah8_1, ah18_1)
        return var_2

@register(Charts_Data_M14)
class AI4():
    # 'Charts_Data_M14'!AI4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AI8,'Dashboard M14'!AI18)"
    @eval_fn
    def AI4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ai8_1 = Dashboard_M14.AI8()
        ai18_1 = Dashboard_M14.AI18()
        var_2 = IF(var_1, ai8_1, ai18_1)
        return var_2

@register(Charts_Data_M14)
class AJ4():
    # 'Charts_Data_M14'!AJ4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AJ8,'Dashboard M14'!AJ18)"
    @eval_fn
    def AJ4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aj8_1 = Dashboard_M14.AJ8()
        aj18_1 = Dashboard_M14.AJ18()
        var_2 = IF(var_1, aj8_1, aj18_1)
        return var_2

@register(Charts_Data_M14)
class AK4():
    # 'Charts_Data_M14'!AK4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AK8,'Dashboard M14'!AK18)"
    @eval_fn
    def AK4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ak8_1 = Dashboard_M14.AK8()
        ak18_1 = Dashboard_M14.AK18()
        var_2 = IF(var_1, ak8_1, ak18_1)
        return var_2

@register(Charts_Data_M14)
class AL4():
    # 'Charts_Data_M14'!AL4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AL8,'Dashboard M14'!AL18)"
    @eval_fn
    def AL4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        al8_1 = Dashboard_M14.AL8()
        al18_1 = Dashboard_M14.AL18()
        var_2 = IF(var_1, al8_1, al18_1)
        return var_2

@register(Charts_Data_M14)
class AM4():
    # 'Charts_Data_M14'!AM4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AM8,'Dashboard M14'!AM18)"
    @eval_fn
    def AM4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        am8_1 = Dashboard_M14.AM8()
        am18_1 = Dashboard_M14.AM18()
        var_2 = IF(var_1, am8_1, am18_1)
        return var_2

@register(Charts_Data_M14)
class AN4():
    # 'Charts_Data_M14'!AN4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AN8,'Dashboard M14'!AN18)"
    @eval_fn
    def AN4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        an8_1 = Dashboard_M14.AN8()
        an18_1 = Dashboard_M14.AN18()
        var_2 = IF(var_1, an8_1, an18_1)
        return var_2

@register(Charts_Data_M14)
class AO4():
    # 'Charts_Data_M14'!AO4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AO8,'Dashboard M14'!AO18)"
    @eval_fn
    def AO4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ao8_1 = Dashboard_M14.AO8()
        ao18_1 = Dashboard_M14.AO18()
        var_2 = IF(var_1, ao8_1, ao18_1)
        return var_2

@register(Charts_Data_M14)
class AP4():
    # 'Charts_Data_M14'!AP4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AP8,'Dashboard M14'!AP18)"
    @eval_fn
    def AP4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ap8_1 = Dashboard_M14.AP8()
        ap18_1 = Dashboard_M14.AP18()
        var_2 = IF(var_1, ap8_1, ap18_1)
        return var_2

@register(Charts_Data_M14)
class AQ4():
    # 'Charts_Data_M14'!AQ4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AQ8,'Dashboard M14'!AQ18)"
    @eval_fn
    def AQ4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aq8_1 = Dashboard_M14.AQ8()
        aq18_1 = Dashboard_M14.AQ18()
        var_2 = IF(var_1, aq8_1, aq18_1)
        return var_2

@register(Charts_Data_M14)
class AR4():
    # 'Charts_Data_M14'!AR4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AR8,'Dashboard M14'!AR18)"
    @eval_fn
    def AR4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ar8_1 = Dashboard_M14.AR8()
        ar18_1 = Dashboard_M14.AR18()
        var_2 = IF(var_1, ar8_1, ar18_1)
        return var_2

@register(Charts_Data_M14)
class AS4():
    # 'Charts_Data_M14'!AS4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AS8,'Dashboard M14'!AS18)"
    @eval_fn
    def AS4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        as8_1 = Dashboard_M14.AS8()
        as18_1 = Dashboard_M14.AS18()
        var_2 = IF(var_1, as8_1, as18_1)
        return var_2

@register(Charts_Data_M14)
class AT4():
    # 'Charts_Data_M14'!AT4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AT8,'Dashboard M14'!AT18)"
    @eval_fn
    def AT4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        at8_1 = Dashboard_M14.AT8()
        at18_1 = Dashboard_M14.AT18()
        var_2 = IF(var_1, at8_1, at18_1)
        return var_2

@register(Charts_Data_M14)
class AU4():
    # 'Charts_Data_M14'!AU4
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AU8,'Dashboard M14'!AU18)"
    @eval_fn
    def AU4():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        au8_1 = Dashboard_M14.AU8()
        au18_1 = Dashboard_M14.AU18()
        var_2 = IF(var_1, au8_1, au18_1)
        return var_2

@register(Charts_Data_M14)
class B5():
    # 'Charts_Data_M14'!B5
    value = "Percent Progress"

@register(Charts_Data_M14)
class C5():
    # 'Charts_Data_M14'!C5
    value = "   Transportation Sector"

@register(Charts_Data_M14)
class F5():
    # 'Charts_Data_M14'!F5
    value = "Notes"

@register(Charts_Data_M14)
class G5():
    # 'Charts_Data_M14'!G5
    value = 11.1255441285
    formula = "=IF($B$4=$B$3,'Dashboard M14'!G9,'Dashboard M14'!G19)"
    @eval_fn
    def G5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        g9_1 = Dashboard_M14.G9()
        g19_1 = Dashboard_M14.G19()
        var_2 = IF(var_1, g9_1, g19_1)
        return var_2

@register(Charts_Data_M14)
class H5():
    # 'Charts_Data_M14'!H5
    value = 10.8803386157
    formula = "=IF($B$4=$B$3,'Dashboard M14'!H9,'Dashboard M14'!H19)"
    @eval_fn
    def H5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        h9_1 = Dashboard_M14.H9()
        h19_1 = Dashboard_M14.H19()
        var_2 = IF(var_1, h9_1, h19_1)
        return var_2

@register(Charts_Data_M14)
class I5():
    # 'Charts_Data_M14'!I5
    value = 10.3854658306
    formula = "=IF($B$4=$B$3,'Dashboard M14'!I9,'Dashboard M14'!I19)"
    @eval_fn
    def I5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        i9_1 = Dashboard_M14.I9()
        i19_1 = Dashboard_M14.I19()
        var_2 = IF(var_1, i9_1, i19_1)
        return var_2

@register(Charts_Data_M14)
class J5():
    # 'Charts_Data_M14'!J5
    value = 9.36711395891
    formula = "=IF($B$4=$B$3,'Dashboard M14'!J9,'Dashboard M14'!J19)"
    @eval_fn
    def J5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        j9_1 = Dashboard_M14.J9()
        j19_1 = Dashboard_M14.J19()
        var_2 = IF(var_1, j9_1, j19_1)
        return var_2

@register(Charts_Data_M14)
class K5():
    # 'Charts_Data_M14'!K5
    value = 10.0494111526
    formula = "=IF($B$4=$B$3,'Dashboard M14'!K9,'Dashboard M14'!K19)"
    @eval_fn
    def K5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        k9_1 = Dashboard_M14.K9()
        k19_1 = Dashboard_M14.K19()
        var_2 = IF(var_1, k9_1, k19_1)
        return var_2

@register(Charts_Data_M14)
class L5():
    # 'Charts_Data_M14'!L5
    value = 9.89780907391
    formula = "=IF($B$4=$B$3,'Dashboard M14'!L9,'Dashboard M14'!L19)"
    @eval_fn
    def L5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        l9_1 = Dashboard_M14.L9()
        l19_1 = Dashboard_M14.L19()
        var_2 = IF(var_1, l9_1, l19_1)
        return var_2

@register(Charts_Data_M14)
class M5():
    # 'Charts_Data_M14'!M5
    value = 8.73529217969
    formula = "=IF($B$4=$B$3,'Dashboard M14'!M9,'Dashboard M14'!M19)"
    @eval_fn
    def M5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        m9_1 = Dashboard_M14.M9()
        m19_1 = Dashboard_M14.M19()
        var_2 = IF(var_1, m9_1, m19_1)
        return var_2

@register(Charts_Data_M14)
class N5():
    # 'Charts_Data_M14'!N5
    value = 8.41440929536
    formula = "=IF($B$4=$B$3,'Dashboard M14'!N9,'Dashboard M14'!N19)"
    @eval_fn
    def N5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        n9_1 = Dashboard_M14.N9()
        n19_1 = Dashboard_M14.N19()
        var_2 = IF(var_1, n9_1, n19_1)
        return var_2

@register(Charts_Data_M14)
class O5():
    # 'Charts_Data_M14'!O5
    value = 8.22250707626
    formula = "=IF($B$4=$B$3,'Dashboard M14'!O9,'Dashboard M14'!O19)"
    @eval_fn
    def O5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        o9_1 = Dashboard_M14.O9()
        o19_1 = Dashboard_M14.O19()
        var_2 = IF(var_1, o9_1, o19_1)
        return var_2

@register(Charts_Data_M14)
class P5():
    # 'Charts_Data_M14'!P5
    value = 8.86615764676
    formula = "=IF($B$4=$B$3,'Dashboard M14'!P9,'Dashboard M14'!P19)"
    @eval_fn
    def P5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        p9_1 = Dashboard_M14.P9()
        p19_1 = Dashboard_M14.P19()
        var_2 = IF(var_1, p9_1, p19_1)
        return var_2

@register(Charts_Data_M14)
class Q5():
    # 'Charts_Data_M14'!Q5
    value = 9.02372551066
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Q9,'Dashboard M14'!Q19)"
    @eval_fn
    def Q5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        q9_1 = Dashboard_M14.Q9()
        q19_1 = Dashboard_M14.Q19()
        var_2 = IF(var_1, q9_1, q19_1)
        return var_2

@register(Charts_Data_M14)
class R5():
    # 'Charts_Data_M14'!R5
    value = 9.53791014042
    formula = "=IF($B$4=$B$3,'Dashboard M14'!R9,'Dashboard M14'!R19)"
    @eval_fn
    def R5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        r9_1 = Dashboard_M14.R9()
        r19_1 = Dashboard_M14.R19()
        var_2 = IF(var_1, r9_1, r19_1)
        return var_2

@register(Charts_Data_M14)
class S5():
    # 'Charts_Data_M14'!S5
    value = 10.1166929516
    formula = "=IF($B$4=$B$3,'Dashboard M14'!S9,'Dashboard M14'!S19)"
    @eval_fn
    def S5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        s9_1 = Dashboard_M14.S9()
        s19_1 = Dashboard_M14.S19()
        var_2 = IF(var_1, s9_1, s19_1)
        return var_2

@register(Charts_Data_M14)
class T5():
    # 'Charts_Data_M14'!T5
    value = 11.7645031556
    formula = "=IF($B$4=$B$3,'Dashboard M14'!T9,'Dashboard M14'!T19)"
    @eval_fn
    def T5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        t9_1 = Dashboard_M14.T9()
        t19_1 = Dashboard_M14.T19()
        var_2 = IF(var_1, t9_1, t19_1)
        return var_2

@register(Charts_Data_M14)
class U5():
    # 'Charts_Data_M14'!U5
    value = 12.4457281307
    formula = "=IF($B$4=$B$3,'Dashboard M14'!U9,'Dashboard M14'!U19)"
    @eval_fn
    def U5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        u9_1 = Dashboard_M14.U9()
        u19_1 = Dashboard_M14.U19()
        var_2 = IF(var_1, u9_1, u19_1)
        return var_2

@register(Charts_Data_M14)
class V5():
    # 'Charts_Data_M14'!V5
    value = 12.8499519637
    formula = "=IF($B$4=$B$3,'Dashboard M14'!V9,'Dashboard M14'!V19)"
    @eval_fn
    def V5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        v9_1 = Dashboard_M14.V9()
        v19_1 = Dashboard_M14.V19()
        var_2 = IF(var_1, v9_1, v19_1)
        return var_2

@register(Charts_Data_M14)
class W5():
    # 'Charts_Data_M14'!W5
    value = 13.0429453009
    formula = "=IF($B$4=$B$3,'Dashboard M14'!W9,'Dashboard M14'!W19)"
    @eval_fn
    def W5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        w9_1 = Dashboard_M14.W9()
        w19_1 = Dashboard_M14.W19()
        var_2 = IF(var_1, w9_1, w19_1)
        return var_2

@register(Charts_Data_M14)
class X5():
    # 'Charts_Data_M14'!X5
    value = 14.0937993271
    formula = "=IF($B$4=$B$3,'Dashboard M14'!X9,'Dashboard M14'!X19)"
    @eval_fn
    def X5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        x9_1 = Dashboard_M14.X9()
        x19_1 = Dashboard_M14.X19()
        var_2 = IF(var_1, x9_1, x19_1)
        return var_2

@register(Charts_Data_M14)
class Y5():
    # 'Charts_Data_M14'!Y5
    value = 9.71021621483
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Y9,'Dashboard M14'!Y19)"
    @eval_fn
    def Y5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        y9_1 = Dashboard_M14.Y9()
        y19_1 = Dashboard_M14.Y19()
        var_2 = IF(var_1, y9_1, y19_1)
        return var_2

@register(Charts_Data_M14)
class Z5():
    # 'Charts_Data_M14'!Z5
    value = 9.44888105592
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Z9,'Dashboard M14'!Z19)"
    @eval_fn
    def Z5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        z9_1 = Dashboard_M14.Z9()
        z19_1 = Dashboard_M14.Z19()
        var_2 = IF(var_1, z9_1, z19_1)
        return var_2

@register(Charts_Data_M14)
class AA5():
    # 'Charts_Data_M14'!AA5
    value = 9.65984910336
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AA9,'Dashboard M14'!AA19)"
    @eval_fn
    def AA5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aa9_1 = Dashboard_M14.AA9()
        aa19_1 = Dashboard_M14.AA19()
        var_2 = IF(var_1, aa9_1, aa19_1)
        return var_2

@register(Charts_Data_M14)
class AB5():
    # 'Charts_Data_M14'!AB5
    value = 10.2312281736
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AB9,'Dashboard M14'!AB19)"
    @eval_fn
    def AB5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ab9_1 = Dashboard_M14.AB9()
        ab19_1 = Dashboard_M14.AB19()
        var_2 = IF(var_1, ab9_1, ab19_1)
        return var_2

@register(Charts_Data_M14)
class AC5():
    # 'Charts_Data_M14'!AC5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AC9,'Dashboard M14'!AC19)"
    @eval_fn
    def AC5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ac9_1 = Dashboard_M14.AC9()
        ac19_1 = Dashboard_M14.AC19()
        var_2 = IF(var_1, ac9_1, ac19_1)
        return var_2

@register(Charts_Data_M14)
class AD5():
    # 'Charts_Data_M14'!AD5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AD9,'Dashboard M14'!AD19)"
    @eval_fn
    def AD5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ad9_1 = Dashboard_M14.AD9()
        ad19_1 = Dashboard_M14.AD19()
        var_2 = IF(var_1, ad9_1, ad19_1)
        return var_2

@register(Charts_Data_M14)
class AE5():
    # 'Charts_Data_M14'!AE5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AE9,'Dashboard M14'!AE19)"
    @eval_fn
    def AE5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ae9_1 = Dashboard_M14.AE9()
        ae19_1 = Dashboard_M14.AE19()
        var_2 = IF(var_1, ae9_1, ae19_1)
        return var_2

@register(Charts_Data_M14)
class AF5():
    # 'Charts_Data_M14'!AF5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AF9,'Dashboard M14'!AF19)"
    @eval_fn
    def AF5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        af9_1 = Dashboard_M14.AF9()
        af19_1 = Dashboard_M14.AF19()
        var_2 = IF(var_1, af9_1, af19_1)
        return var_2

@register(Charts_Data_M14)
class AG5():
    # 'Charts_Data_M14'!AG5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AG9,'Dashboard M14'!AG19)"
    @eval_fn
    def AG5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ag9_1 = Dashboard_M14.AG9()
        ag19_1 = Dashboard_M14.AG19()
        var_2 = IF(var_1, ag9_1, ag19_1)
        return var_2

@register(Charts_Data_M14)
class AH5():
    # 'Charts_Data_M14'!AH5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AH9,'Dashboard M14'!AH19)"
    @eval_fn
    def AH5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ah9_1 = Dashboard_M14.AH9()
        ah19_1 = Dashboard_M14.AH19()
        var_2 = IF(var_1, ah9_1, ah19_1)
        return var_2

@register(Charts_Data_M14)
class AI5():
    # 'Charts_Data_M14'!AI5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AI9,'Dashboard M14'!AI19)"
    @eval_fn
    def AI5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ai9_1 = Dashboard_M14.AI9()
        ai19_1 = Dashboard_M14.AI19()
        var_2 = IF(var_1, ai9_1, ai19_1)
        return var_2

@register(Charts_Data_M14)
class AJ5():
    # 'Charts_Data_M14'!AJ5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AJ9,'Dashboard M14'!AJ19)"
    @eval_fn
    def AJ5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aj9_1 = Dashboard_M14.AJ9()
        aj19_1 = Dashboard_M14.AJ19()
        var_2 = IF(var_1, aj9_1, aj19_1)
        return var_2

@register(Charts_Data_M14)
class AK5():
    # 'Charts_Data_M14'!AK5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AK9,'Dashboard M14'!AK19)"
    @eval_fn
    def AK5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ak9_1 = Dashboard_M14.AK9()
        ak19_1 = Dashboard_M14.AK19()
        var_2 = IF(var_1, ak9_1, ak19_1)
        return var_2

@register(Charts_Data_M14)
class AL5():
    # 'Charts_Data_M14'!AL5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AL9,'Dashboard M14'!AL19)"
    @eval_fn
    def AL5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        al9_1 = Dashboard_M14.AL9()
        al19_1 = Dashboard_M14.AL19()
        var_2 = IF(var_1, al9_1, al19_1)
        return var_2

@register(Charts_Data_M14)
class AM5():
    # 'Charts_Data_M14'!AM5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AM9,'Dashboard M14'!AM19)"
    @eval_fn
    def AM5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        am9_1 = Dashboard_M14.AM9()
        am19_1 = Dashboard_M14.AM19()
        var_2 = IF(var_1, am9_1, am19_1)
        return var_2

@register(Charts_Data_M14)
class AN5():
    # 'Charts_Data_M14'!AN5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AN9,'Dashboard M14'!AN19)"
    @eval_fn
    def AN5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        an9_1 = Dashboard_M14.AN9()
        an19_1 = Dashboard_M14.AN19()
        var_2 = IF(var_1, an9_1, an19_1)
        return var_2

@register(Charts_Data_M14)
class AO5():
    # 'Charts_Data_M14'!AO5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AO9,'Dashboard M14'!AO19)"
    @eval_fn
    def AO5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ao9_1 = Dashboard_M14.AO9()
        ao19_1 = Dashboard_M14.AO19()
        var_2 = IF(var_1, ao9_1, ao19_1)
        return var_2

@register(Charts_Data_M14)
class AP5():
    # 'Charts_Data_M14'!AP5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AP9,'Dashboard M14'!AP19)"
    @eval_fn
    def AP5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ap9_1 = Dashboard_M14.AP9()
        ap19_1 = Dashboard_M14.AP19()
        var_2 = IF(var_1, ap9_1, ap19_1)
        return var_2

@register(Charts_Data_M14)
class AQ5():
    # 'Charts_Data_M14'!AQ5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AQ9,'Dashboard M14'!AQ19)"
    @eval_fn
    def AQ5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aq9_1 = Dashboard_M14.AQ9()
        aq19_1 = Dashboard_M14.AQ19()
        var_2 = IF(var_1, aq9_1, aq19_1)
        return var_2

@register(Charts_Data_M14)
class AR5():
    # 'Charts_Data_M14'!AR5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AR9,'Dashboard M14'!AR19)"
    @eval_fn
    def AR5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ar9_1 = Dashboard_M14.AR9()
        ar19_1 = Dashboard_M14.AR19()
        var_2 = IF(var_1, ar9_1, ar19_1)
        return var_2

@register(Charts_Data_M14)
class AS5():
    # 'Charts_Data_M14'!AS5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AS9,'Dashboard M14'!AS19)"
    @eval_fn
    def AS5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        as9_1 = Dashboard_M14.AS9()
        as19_1 = Dashboard_M14.AS19()
        var_2 = IF(var_1, as9_1, as19_1)
        return var_2

@register(Charts_Data_M14)
class AT5():
    # 'Charts_Data_M14'!AT5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AT9,'Dashboard M14'!AT19)"
    @eval_fn
    def AT5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        at9_1 = Dashboard_M14.AT9()
        at19_1 = Dashboard_M14.AT19()
        var_2 = IF(var_1, at9_1, at19_1)
        return var_2

@register(Charts_Data_M14)
class AU5():
    # 'Charts_Data_M14'!AU5
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AU9,'Dashboard M14'!AU19)"
    @eval_fn
    def AU5():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        au9_1 = Dashboard_M14.AU9()
        au19_1 = Dashboard_M14.AU19()
        var_2 = IF(var_1, au9_1, au19_1)
        return var_2

@register(Charts_Data_M14)
class C6():
    # 'Charts_Data_M14'!C6
    value = "   Electric Power Sector"

@register(Charts_Data_M14)
class F6():
    # 'Charts_Data_M14'!F6
    value = "Notes"

@register(Charts_Data_M14)
class G6():
    # 'Charts_Data_M14'!G6
    value = 7.31298102704
    formula = "=IF($B$4=$B$3,'Dashboard M14'!G10,'Dashboard M14'!G20)"
    @eval_fn
    def G6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        g10_1 = Dashboard_M14.G10()
        g20_1 = Dashboard_M14.G20()
        var_2 = IF(var_1, g10_1, g20_1)
        return var_2

@register(Charts_Data_M14)
class H6():
    # 'Charts_Data_M14'!H6
    value = 6.0292140767
    formula = "=IF($B$4=$B$3,'Dashboard M14'!H10,'Dashboard M14'!H20)"
    @eval_fn
    def H6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        h10_1 = Dashboard_M14.H10()
        h20_1 = Dashboard_M14.H20()
        var_2 = IF(var_1, h10_1, h20_1)
        return var_2

@register(Charts_Data_M14)
class I6():
    # 'Charts_Data_M14'!I6
    value = 6.97813738834
    formula = "=IF($B$4=$B$3,'Dashboard M14'!I10,'Dashboard M14'!I20)"
    @eval_fn
    def I6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        i10_1 = Dashboard_M14.I10()
        i20_1 = Dashboard_M14.I20()
        var_2 = IF(var_1, i10_1, i20_1)
        return var_2

@register(Charts_Data_M14)
class J6():
    # 'Charts_Data_M14'!J6
    value = 7.00157536793
    formula = "=IF($B$4=$B$3,'Dashboard M14'!J10,'Dashboard M14'!J20)"
    @eval_fn
    def J6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        j10_1 = Dashboard_M14.J10()
        j20_1 = Dashboard_M14.J20()
        var_2 = IF(var_1, j10_1, j20_1)
        return var_2

@register(Charts_Data_M14)
class K6():
    # 'Charts_Data_M14'!K6
    value = 7.23262410047
    formula = "=IF($B$4=$B$3,'Dashboard M14'!K10,'Dashboard M14'!K20)"
    @eval_fn
    def K6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        k10_1 = Dashboard_M14.K10()
        k20_1 = Dashboard_M14.K20()
        var_2 = IF(var_1, k10_1, k20_1)
        return var_2

@register(Charts_Data_M14)
class L6():
    # 'Charts_Data_M14'!L6
    value = 7.49937226898
    formula = "=IF($B$4=$B$3,'Dashboard M14'!L10,'Dashboard M14'!L20)"
    @eval_fn
    def L6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        l10_1 = Dashboard_M14.L10()
        l20_1 = Dashboard_M14.L20()
        var_2 = IF(var_1, l10_1, l20_1)
        return var_2

@register(Charts_Data_M14)
class M6():
    # 'Charts_Data_M14'!M6
    value = 7.77095587653
    formula = "=IF($B$4=$B$3,'Dashboard M14'!M10,'Dashboard M14'!M20)"
    @eval_fn
    def M6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        m10_1 = Dashboard_M14.M10()
        m20_1 = Dashboard_M14.M20()
        var_2 = IF(var_1, m10_1, m20_1)
        return var_2

@register(Charts_Data_M14)
class N6():
    # 'Charts_Data_M14'!N6
    value = 7.70847864624
    formula = "=IF($B$4=$B$3,'Dashboard M14'!N10,'Dashboard M14'!N20)"
    @eval_fn
    def N6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        n10_1 = Dashboard_M14.N10()
        n20_1 = Dashboard_M14.N20()
        var_2 = IF(var_1, n10_1, n20_1)
        return var_2

@register(Charts_Data_M14)
class O6():
    # 'Charts_Data_M14'!O6
    value = 7.53582139003
    formula = "=IF($B$4=$B$3,'Dashboard M14'!O10,'Dashboard M14'!O20)"
    @eval_fn
    def O6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        o10_1 = Dashboard_M14.O10()
        o20_1 = Dashboard_M14.O20()
        var_2 = IF(var_1, o10_1, o20_1)
        return var_2

@register(Charts_Data_M14)
class P6():
    # 'Charts_Data_M14'!P6
    value = 7.63319898563
    formula = "=IF($B$4=$B$3,'Dashboard M14'!P10,'Dashboard M14'!P20)"
    @eval_fn
    def P6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        p10_1 = Dashboard_M14.P10()
        p20_1 = Dashboard_M14.P20()
        var_2 = IF(var_1, p10_1, p20_1)
        return var_2

@register(Charts_Data_M14)
class Q6():
    # 'Charts_Data_M14'!Q6
    value = 7.75212421191
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Q10,'Dashboard M14'!Q20)"
    @eval_fn
    def Q6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        q10_1 = Dashboard_M14.Q10()
        q20_1 = Dashboard_M14.Q20()
        var_2 = IF(var_1, q10_1, q20_1)
        return var_2

@register(Charts_Data_M14)
class R6():
    # 'Charts_Data_M14'!R6
    value = 7.74745814551
    formula = "=IF($B$4=$B$3,'Dashboard M14'!R10,'Dashboard M14'!R20)"
    @eval_fn
    def R6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        r10_1 = Dashboard_M14.R10()
        r20_1 = Dashboard_M14.R20()
        var_2 = IF(var_1, r10_1, r20_1)
        return var_2

@register(Charts_Data_M14)
class S6():
    # 'Charts_Data_M14'!S6
    value = 8.31874416772
    formula = "=IF($B$4=$B$3,'Dashboard M14'!S10,'Dashboard M14'!S20)"
    @eval_fn
    def S6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        s10_1 = Dashboard_M14.S10()
        s20_1 = Dashboard_M14.S20()
        var_2 = IF(var_1, s10_1, s20_1)
        return var_2

@register(Charts_Data_M14)
class T6():
    # 'Charts_Data_M14'!T6
    value = 7.74418017721
    formula = "=IF($B$4=$B$3,'Dashboard M14'!T10,'Dashboard M14'!T20)"
    @eval_fn
    def T6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        t10_1 = Dashboard_M14.T10()
        t20_1 = Dashboard_M14.T20()
        var_2 = IF(var_1, t10_1, t20_1)
        return var_2

@register(Charts_Data_M14)
class U6():
    # 'Charts_Data_M14'!U6
    value = 8.03315536883
    formula = "=IF($B$4=$B$3,'Dashboard M14'!U10,'Dashboard M14'!U20)"
    @eval_fn
    def U6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        u10_1 = Dashboard_M14.U10()
        u20_1 = Dashboard_M14.U20()
        var_2 = IF(var_1, u10_1, u20_1)
        return var_2

@register(Charts_Data_M14)
class V6():
    # 'Charts_Data_M14'!V6
    value = 7.98087266698
    formula = "=IF($B$4=$B$3,'Dashboard M14'!V10,'Dashboard M14'!V20)"
    @eval_fn
    def V6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        v10_1 = Dashboard_M14.V10()
        v20_1 = Dashboard_M14.V20()
        var_2 = IF(var_1, v10_1, v20_1)
        return var_2

@register(Charts_Data_M14)
class W6():
    # 'Charts_Data_M14'!W6
    value = 7.95547617647
    formula = "=IF($B$4=$B$3,'Dashboard M14'!W10,'Dashboard M14'!W20)"
    @eval_fn
    def W6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        w10_1 = Dashboard_M14.W10()
        w20_1 = Dashboard_M14.W20()
        var_2 = IF(var_1, w10_1, w20_1)
        return var_2

@register(Charts_Data_M14)
class X6():
    # 'Charts_Data_M14'!X6
    value = 7.98325048568
    formula = "=IF($B$4=$B$3,'Dashboard M14'!X10,'Dashboard M14'!X20)"
    @eval_fn
    def X6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        x10_1 = Dashboard_M14.X10()
        x20_1 = Dashboard_M14.X20()
        var_2 = IF(var_1, x10_1, x20_1)
        return var_2

@register(Charts_Data_M14)
class Y6():
    # 'Charts_Data_M14'!Y6
    value = 7.79709317658
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Y10,'Dashboard M14'!Y20)"
    @eval_fn
    def Y6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        y10_1 = Dashboard_M14.Y10()
        y20_1 = Dashboard_M14.Y20()
        var_2 = IF(var_1, y10_1, y20_1)
        return var_2

@register(Charts_Data_M14)
class Z6():
    # 'Charts_Data_M14'!Z6
    value = 7.58929347671
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Z10,'Dashboard M14'!Z20)"
    @eval_fn
    def Z6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        z10_1 = Dashboard_M14.Z10()
        z20_1 = Dashboard_M14.Z20()
        var_2 = IF(var_1, z10_1, z20_1)
        return var_2

@register(Charts_Data_M14)
class AA6():
    # 'Charts_Data_M14'!AA6
    value = 7.31338889643
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AA10,'Dashboard M14'!AA20)"
    @eval_fn
    def AA6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aa10_1 = Dashboard_M14.AA10()
        aa20_1 = Dashboard_M14.AA20()
        var_2 = IF(var_1, aa10_1, aa20_1)
        return var_2

@register(Charts_Data_M14)
class AB6():
    # 'Charts_Data_M14'!AB6
    value = 7.18344446769
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AB10,'Dashboard M14'!AB20)"
    @eval_fn
    def AB6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ab10_1 = Dashboard_M14.AB10()
        ab20_1 = Dashboard_M14.AB20()
        var_2 = IF(var_1, ab10_1, ab20_1)
        return var_2

@register(Charts_Data_M14)
class AC6():
    # 'Charts_Data_M14'!AC6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AC10,'Dashboard M14'!AC20)"
    @eval_fn
    def AC6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ac10_1 = Dashboard_M14.AC10()
        ac20_1 = Dashboard_M14.AC20()
        var_2 = IF(var_1, ac10_1, ac20_1)
        return var_2

@register(Charts_Data_M14)
class AD6():
    # 'Charts_Data_M14'!AD6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AD10,'Dashboard M14'!AD20)"
    @eval_fn
    def AD6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ad10_1 = Dashboard_M14.AD10()
        ad20_1 = Dashboard_M14.AD20()
        var_2 = IF(var_1, ad10_1, ad20_1)
        return var_2

@register(Charts_Data_M14)
class AE6():
    # 'Charts_Data_M14'!AE6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AE10,'Dashboard M14'!AE20)"
    @eval_fn
    def AE6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ae10_1 = Dashboard_M14.AE10()
        ae20_1 = Dashboard_M14.AE20()
        var_2 = IF(var_1, ae10_1, ae20_1)
        return var_2

@register(Charts_Data_M14)
class AF6():
    # 'Charts_Data_M14'!AF6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AF10,'Dashboard M14'!AF20)"
    @eval_fn
    def AF6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        af10_1 = Dashboard_M14.AF10()
        af20_1 = Dashboard_M14.AF20()
        var_2 = IF(var_1, af10_1, af20_1)
        return var_2

@register(Charts_Data_M14)
class AG6():
    # 'Charts_Data_M14'!AG6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AG10,'Dashboard M14'!AG20)"
    @eval_fn
    def AG6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ag10_1 = Dashboard_M14.AG10()
        ag20_1 = Dashboard_M14.AG20()
        var_2 = IF(var_1, ag10_1, ag20_1)
        return var_2

@register(Charts_Data_M14)
class AH6():
    # 'Charts_Data_M14'!AH6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AH10,'Dashboard M14'!AH20)"
    @eval_fn
    def AH6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ah10_1 = Dashboard_M14.AH10()
        ah20_1 = Dashboard_M14.AH20()
        var_2 = IF(var_1, ah10_1, ah20_1)
        return var_2

@register(Charts_Data_M14)
class AI6():
    # 'Charts_Data_M14'!AI6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AI10,'Dashboard M14'!AI20)"
    @eval_fn
    def AI6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ai10_1 = Dashboard_M14.AI10()
        ai20_1 = Dashboard_M14.AI20()
        var_2 = IF(var_1, ai10_1, ai20_1)
        return var_2

@register(Charts_Data_M14)
class AJ6():
    # 'Charts_Data_M14'!AJ6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AJ10,'Dashboard M14'!AJ20)"
    @eval_fn
    def AJ6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aj10_1 = Dashboard_M14.AJ10()
        aj20_1 = Dashboard_M14.AJ20()
        var_2 = IF(var_1, aj10_1, aj20_1)
        return var_2

@register(Charts_Data_M14)
class AK6():
    # 'Charts_Data_M14'!AK6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AK10,'Dashboard M14'!AK20)"
    @eval_fn
    def AK6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ak10_1 = Dashboard_M14.AK10()
        ak20_1 = Dashboard_M14.AK20()
        var_2 = IF(var_1, ak10_1, ak20_1)
        return var_2

@register(Charts_Data_M14)
class AL6():
    # 'Charts_Data_M14'!AL6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AL10,'Dashboard M14'!AL20)"
    @eval_fn
    def AL6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        al10_1 = Dashboard_M14.AL10()
        al20_1 = Dashboard_M14.AL20()
        var_2 = IF(var_1, al10_1, al20_1)
        return var_2

@register(Charts_Data_M14)
class AM6():
    # 'Charts_Data_M14'!AM6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AM10,'Dashboard M14'!AM20)"
    @eval_fn
    def AM6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        am10_1 = Dashboard_M14.AM10()
        am20_1 = Dashboard_M14.AM20()
        var_2 = IF(var_1, am10_1, am20_1)
        return var_2

@register(Charts_Data_M14)
class AN6():
    # 'Charts_Data_M14'!AN6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AN10,'Dashboard M14'!AN20)"
    @eval_fn
    def AN6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        an10_1 = Dashboard_M14.AN10()
        an20_1 = Dashboard_M14.AN20()
        var_2 = IF(var_1, an10_1, an20_1)
        return var_2

@register(Charts_Data_M14)
class AO6():
    # 'Charts_Data_M14'!AO6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AO10,'Dashboard M14'!AO20)"
    @eval_fn
    def AO6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ao10_1 = Dashboard_M14.AO10()
        ao20_1 = Dashboard_M14.AO20()
        var_2 = IF(var_1, ao10_1, ao20_1)
        return var_2

@register(Charts_Data_M14)
class AP6():
    # 'Charts_Data_M14'!AP6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AP10,'Dashboard M14'!AP20)"
    @eval_fn
    def AP6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ap10_1 = Dashboard_M14.AP10()
        ap20_1 = Dashboard_M14.AP20()
        var_2 = IF(var_1, ap10_1, ap20_1)
        return var_2

@register(Charts_Data_M14)
class AQ6():
    # 'Charts_Data_M14'!AQ6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AQ10,'Dashboard M14'!AQ20)"
    @eval_fn
    def AQ6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aq10_1 = Dashboard_M14.AQ10()
        aq20_1 = Dashboard_M14.AQ20()
        var_2 = IF(var_1, aq10_1, aq20_1)
        return var_2

@register(Charts_Data_M14)
class AR6():
    # 'Charts_Data_M14'!AR6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AR10,'Dashboard M14'!AR20)"
    @eval_fn
    def AR6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ar10_1 = Dashboard_M14.AR10()
        ar20_1 = Dashboard_M14.AR20()
        var_2 = IF(var_1, ar10_1, ar20_1)
        return var_2

@register(Charts_Data_M14)
class AS6():
    # 'Charts_Data_M14'!AS6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AS10,'Dashboard M14'!AS20)"
    @eval_fn
    def AS6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        as10_1 = Dashboard_M14.AS10()
        as20_1 = Dashboard_M14.AS20()
        var_2 = IF(var_1, as10_1, as20_1)
        return var_2

@register(Charts_Data_M14)
class AT6():
    # 'Charts_Data_M14'!AT6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AT10,'Dashboard M14'!AT20)"
    @eval_fn
    def AT6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        at10_1 = Dashboard_M14.AT10()
        at20_1 = Dashboard_M14.AT20()
        var_2 = IF(var_1, at10_1, at20_1)
        return var_2

@register(Charts_Data_M14)
class AU6():
    # 'Charts_Data_M14'!AU6
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AU10,'Dashboard M14'!AU20)"
    @eval_fn
    def AU6():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        au10_1 = Dashboard_M14.AU10()
        au20_1 = Dashboard_M14.AU20()
        var_2 = IF(var_1, au10_1, au20_1)
        return var_2

@register(Charts_Data_M14)
class C7():
    # 'Charts_Data_M14'!C7
    value = "Total"

@register(Charts_Data_M14)
class F7():
    # 'Charts_Data_M14'!F7
    value = "Notes"

@register(Charts_Data_M14)
class G7():
    # 'Charts_Data_M14'!G7
    value = 21.3537237698
    formula = "=IF($B$4=$B$3,'Dashboard M14'!G11,'Dashboard M14'!G21)"
    @eval_fn
    def G7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        g11_1 = Dashboard_M14.G11()
        g21_1 = Dashboard_M14.G21()
        var_2 = IF(var_1, g11_1, g21_1)
        return var_2

@register(Charts_Data_M14)
class H7():
    # 'Charts_Data_M14'!H7
    value = 19.4105380482
    formula = "=IF($B$4=$B$3,'Dashboard M14'!H11,'Dashboard M14'!H21)"
    @eval_fn
    def H7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        h11_1 = Dashboard_M14.H11()
        h21_1 = Dashboard_M14.H21()
        var_2 = IF(var_1, h11_1, h21_1)
        return var_2

@register(Charts_Data_M14)
class I7():
    # 'Charts_Data_M14'!I7
    value = 20.3397089885
    formula = "=IF($B$4=$B$3,'Dashboard M14'!I11,'Dashboard M14'!I21)"
    @eval_fn
    def I7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        i11_1 = Dashboard_M14.I11()
        i21_1 = Dashboard_M14.I21()
        var_2 = IF(var_1, i11_1, i21_1)
        return var_2

@register(Charts_Data_M14)
class J7():
    # 'Charts_Data_M14'!J7
    value = 18.582989453
    formula = "=IF($B$4=$B$3,'Dashboard M14'!J11,'Dashboard M14'!J21)"
    @eval_fn
    def J7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        j11_1 = Dashboard_M14.J11()
        j21_1 = Dashboard_M14.J21()
        var_2 = IF(var_1, j11_1, j21_1)
        return var_2

@register(Charts_Data_M14)
class K7():
    # 'Charts_Data_M14'!K7
    value = 19.8687974066
    formula = "=IF($B$4=$B$3,'Dashboard M14'!K11,'Dashboard M14'!K21)"
    @eval_fn
    def K7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        k11_1 = Dashboard_M14.K11()
        k21_1 = Dashboard_M14.K21()
        var_2 = IF(var_1, k11_1, k21_1)
        return var_2

@register(Charts_Data_M14)
class L7():
    # 'Charts_Data_M14'!L7
    value = 19.7382121044
    formula = "=IF($B$4=$B$3,'Dashboard M14'!L11,'Dashboard M14'!L21)"
    @eval_fn
    def L7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        l11_1 = Dashboard_M14.L11()
        l21_1 = Dashboard_M14.L21()
        var_2 = IF(var_1, l11_1, l21_1)
        return var_2

@register(Charts_Data_M14)
class M7():
    # 'Charts_Data_M14'!M7
    value = 18.8713582011
    formula = "=IF($B$4=$B$3,'Dashboard M14'!M11,'Dashboard M14'!M21)"
    @eval_fn
    def M7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        m11_1 = Dashboard_M14.M11()
        m21_1 = Dashboard_M14.M21()
        var_2 = IF(var_1, m11_1, m21_1)
        return var_2

@register(Charts_Data_M14)
class N7():
    # 'Charts_Data_M14'!N7
    value = 18.4495992975
    formula = "=IF($B$4=$B$3,'Dashboard M14'!N11,'Dashboard M14'!N21)"
    @eval_fn
    def N7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        n11_1 = Dashboard_M14.N11()
        n21_1 = Dashboard_M14.N21()
        var_2 = IF(var_1, n11_1, n21_1)
        return var_2

@register(Charts_Data_M14)
class O7():
    # 'Charts_Data_M14'!O7
    value = 18.419127002
    formula = "=IF($B$4=$B$3,'Dashboard M14'!O11,'Dashboard M14'!O21)"
    @eval_fn
    def O7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        o11_1 = Dashboard_M14.O11()
        o21_1 = Dashboard_M14.O21()
        var_2 = IF(var_1, o11_1, o21_1)
        return var_2

@register(Charts_Data_M14)
class P7():
    # 'Charts_Data_M14'!P7
    value = 18.1447308497
    formula = "=IF($B$4=$B$3,'Dashboard M14'!P11,'Dashboard M14'!P21)"
    @eval_fn
    def P7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        p11_1 = Dashboard_M14.P11()
        p21_1 = Dashboard_M14.P21()
        var_2 = IF(var_1, p11_1, p21_1)
        return var_2

@register(Charts_Data_M14)
class Q7():
    # 'Charts_Data_M14'!Q7
    value = 18.4657696427
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Q11,'Dashboard M14'!Q21)"
    @eval_fn
    def Q7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        q11_1 = Dashboard_M14.Q11()
        q21_1 = Dashboard_M14.Q21()
        var_2 = IF(var_1, q11_1, q21_1)
        return var_2

@register(Charts_Data_M14)
class R7():
    # 'Charts_Data_M14'!R7
    value = 18.9409632565
    formula = "=IF($B$4=$B$3,'Dashboard M14'!R11,'Dashboard M14'!R21)"
    @eval_fn
    def R7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        r11_1 = Dashboard_M14.R11()
        r21_1 = Dashboard_M14.R21()
        var_2 = IF(var_1, r11_1, r21_1)
        return var_2

@register(Charts_Data_M14)
class S7():
    # 'Charts_Data_M14'!S7
    value = 20.3271298699
    formula = "=IF($B$4=$B$3,'Dashboard M14'!S11,'Dashboard M14'!S21)"
    @eval_fn
    def S7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        s11_1 = Dashboard_M14.S11()
        s21_1 = Dashboard_M14.S21()
        var_2 = IF(var_1, s11_1, s21_1)
        return var_2

@register(Charts_Data_M14)
class T7():
    # 'Charts_Data_M14'!T7
    value = 21.3814495553
    formula = "=IF($B$4=$B$3,'Dashboard M14'!T11,'Dashboard M14'!T21)"
    @eval_fn
    def T7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        t11_1 = Dashboard_M14.T11()
        t21_1 = Dashboard_M14.T21()
        var_2 = IF(var_1, t11_1, t21_1)
        return var_2

@register(Charts_Data_M14)
class U7():
    # 'Charts_Data_M14'!U7
    value = 22.3851243928
    formula = "=IF($B$4=$B$3,'Dashboard M14'!U11,'Dashboard M14'!U21)"
    @eval_fn
    def U7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        u11_1 = Dashboard_M14.U11()
        u21_1 = Dashboard_M14.U21()
        var_2 = IF(var_1, u11_1, u21_1)
        return var_2

@register(Charts_Data_M14)
class V7():
    # 'Charts_Data_M14'!V7
    value = 22.9928695139
    formula = "=IF($B$4=$B$3,'Dashboard M14'!V11,'Dashboard M14'!V21)"
    @eval_fn
    def V7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        v11_1 = Dashboard_M14.V11()
        v21_1 = Dashboard_M14.V21()
        var_2 = IF(var_1, v11_1, v21_1)
        return var_2

@register(Charts_Data_M14)
class W7():
    # 'Charts_Data_M14'!W7
    value = 23.1971518386
    formula = "=IF($B$4=$B$3,'Dashboard M14'!W11,'Dashboard M14'!W21)"
    @eval_fn
    def W7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        w11_1 = Dashboard_M14.W11()
        w21_1 = Dashboard_M14.W21()
        var_2 = IF(var_1, w11_1, w21_1)
        return var_2

@register(Charts_Data_M14)
class X7():
    # 'Charts_Data_M14'!X7
    value = 24.0450147852
    formula = "=IF($B$4=$B$3,'Dashboard M14'!X11,'Dashboard M14'!X21)"
    @eval_fn
    def X7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        x11_1 = Dashboard_M14.X11()
        x21_1 = Dashboard_M14.X21()
        var_2 = IF(var_1, x11_1, x21_1)
        return var_2

@register(Charts_Data_M14)
class Y7():
    # 'Charts_Data_M14'!Y7
    value = 19.3171469845
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Y11,'Dashboard M14'!Y21)"
    @eval_fn
    def Y7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        y11_1 = Dashboard_M14.Y11()
        y21_1 = Dashboard_M14.Y21()
        var_2 = IF(var_1, y11_1, y21_1)
        return var_2

@register(Charts_Data_M14)
class Z7():
    # 'Charts_Data_M14'!Z7
    value = 18.8762412018
    formula = "=IF($B$4=$B$3,'Dashboard M14'!Z11,'Dashboard M14'!Z21)"
    @eval_fn
    def Z7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        z11_1 = Dashboard_M14.Z11()
        z21_1 = Dashboard_M14.Z21()
        var_2 = IF(var_1, z11_1, z21_1)
        return var_2

@register(Charts_Data_M14)
class AA7():
    # 'Charts_Data_M14'!AA7
    value = 18.7905346326
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AA11,'Dashboard M14'!AA21)"
    @eval_fn
    def AA7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aa11_1 = Dashboard_M14.AA11()
        aa21_1 = Dashboard_M14.AA21()
        var_2 = IF(var_1, aa11_1, aa21_1)
        return var_2

@register(Charts_Data_M14)
class AB7():
    # 'Charts_Data_M14'!AB7
    value = 19.3128800275
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AB11,'Dashboard M14'!AB21)"
    @eval_fn
    def AB7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ab11_1 = Dashboard_M14.AB11()
        ab21_1 = Dashboard_M14.AB21()
        var_2 = IF(var_1, ab11_1, ab21_1)
        return var_2

@register(Charts_Data_M14)
class AC7():
    # 'Charts_Data_M14'!AC7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AC11,'Dashboard M14'!AC21)"
    @eval_fn
    def AC7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ac11_1 = Dashboard_M14.AC11()
        ac21_1 = Dashboard_M14.AC21()
        var_2 = IF(var_1, ac11_1, ac21_1)
        return var_2

@register(Charts_Data_M14)
class AD7():
    # 'Charts_Data_M14'!AD7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AD11,'Dashboard M14'!AD21)"
    @eval_fn
    def AD7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ad11_1 = Dashboard_M14.AD11()
        ad21_1 = Dashboard_M14.AD21()
        var_2 = IF(var_1, ad11_1, ad21_1)
        return var_2

@register(Charts_Data_M14)
class AE7():
    # 'Charts_Data_M14'!AE7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AE11,'Dashboard M14'!AE21)"
    @eval_fn
    def AE7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ae11_1 = Dashboard_M14.AE11()
        ae21_1 = Dashboard_M14.AE21()
        var_2 = IF(var_1, ae11_1, ae21_1)
        return var_2

@register(Charts_Data_M14)
class AF7():
    # 'Charts_Data_M14'!AF7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AF11,'Dashboard M14'!AF21)"
    @eval_fn
    def AF7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        af11_1 = Dashboard_M14.AF11()
        af21_1 = Dashboard_M14.AF21()
        var_2 = IF(var_1, af11_1, af21_1)
        return var_2

@register(Charts_Data_M14)
class AG7():
    # 'Charts_Data_M14'!AG7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AG11,'Dashboard M14'!AG21)"
    @eval_fn
    def AG7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ag11_1 = Dashboard_M14.AG11()
        ag21_1 = Dashboard_M14.AG21()
        var_2 = IF(var_1, ag11_1, ag21_1)
        return var_2

@register(Charts_Data_M14)
class AH7():
    # 'Charts_Data_M14'!AH7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AH11,'Dashboard M14'!AH21)"
    @eval_fn
    def AH7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ah11_1 = Dashboard_M14.AH11()
        ah21_1 = Dashboard_M14.AH21()
        var_2 = IF(var_1, ah11_1, ah21_1)
        return var_2

@register(Charts_Data_M14)
class AI7():
    # 'Charts_Data_M14'!AI7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AI11,'Dashboard M14'!AI21)"
    @eval_fn
    def AI7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ai11_1 = Dashboard_M14.AI11()
        ai21_1 = Dashboard_M14.AI21()
        var_2 = IF(var_1, ai11_1, ai21_1)
        return var_2

@register(Charts_Data_M14)
class AJ7():
    # 'Charts_Data_M14'!AJ7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AJ11,'Dashboard M14'!AJ21)"
    @eval_fn
    def AJ7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aj11_1 = Dashboard_M14.AJ11()
        aj21_1 = Dashboard_M14.AJ21()
        var_2 = IF(var_1, aj11_1, aj21_1)
        return var_2

@register(Charts_Data_M14)
class AK7():
    # 'Charts_Data_M14'!AK7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AK11,'Dashboard M14'!AK21)"
    @eval_fn
    def AK7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ak11_1 = Dashboard_M14.AK11()
        ak21_1 = Dashboard_M14.AK21()
        var_2 = IF(var_1, ak11_1, ak21_1)
        return var_2

@register(Charts_Data_M14)
class AL7():
    # 'Charts_Data_M14'!AL7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AL11,'Dashboard M14'!AL21)"
    @eval_fn
    def AL7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        al11_1 = Dashboard_M14.AL11()
        al21_1 = Dashboard_M14.AL21()
        var_2 = IF(var_1, al11_1, al21_1)
        return var_2

@register(Charts_Data_M14)
class AM7():
    # 'Charts_Data_M14'!AM7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AM11,'Dashboard M14'!AM21)"
    @eval_fn
    def AM7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        am11_1 = Dashboard_M14.AM11()
        am21_1 = Dashboard_M14.AM21()
        var_2 = IF(var_1, am11_1, am21_1)
        return var_2

@register(Charts_Data_M14)
class AN7():
    # 'Charts_Data_M14'!AN7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AN11,'Dashboard M14'!AN21)"
    @eval_fn
    def AN7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        an11_1 = Dashboard_M14.AN11()
        an21_1 = Dashboard_M14.AN21()
        var_2 = IF(var_1, an11_1, an21_1)
        return var_2

@register(Charts_Data_M14)
class AO7():
    # 'Charts_Data_M14'!AO7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AO11,'Dashboard M14'!AO21)"
    @eval_fn
    def AO7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ao11_1 = Dashboard_M14.AO11()
        ao21_1 = Dashboard_M14.AO21()
        var_2 = IF(var_1, ao11_1, ao21_1)
        return var_2

@register(Charts_Data_M14)
class AP7():
    # 'Charts_Data_M14'!AP7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AP11,'Dashboard M14'!AP21)"
    @eval_fn
    def AP7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ap11_1 = Dashboard_M14.AP11()
        ap21_1 = Dashboard_M14.AP21()
        var_2 = IF(var_1, ap11_1, ap21_1)
        return var_2

@register(Charts_Data_M14)
class AQ7():
    # 'Charts_Data_M14'!AQ7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AQ11,'Dashboard M14'!AQ21)"
    @eval_fn
    def AQ7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        aq11_1 = Dashboard_M14.AQ11()
        aq21_1 = Dashboard_M14.AQ21()
        var_2 = IF(var_1, aq11_1, aq21_1)
        return var_2

@register(Charts_Data_M14)
class AR7():
    # 'Charts_Data_M14'!AR7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AR11,'Dashboard M14'!AR21)"
    @eval_fn
    def AR7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        ar11_1 = Dashboard_M14.AR11()
        ar21_1 = Dashboard_M14.AR21()
        var_2 = IF(var_1, ar11_1, ar21_1)
        return var_2

@register(Charts_Data_M14)
class AS7():
    # 'Charts_Data_M14'!AS7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AS11,'Dashboard M14'!AS21)"
    @eval_fn
    def AS7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        as11_1 = Dashboard_M14.AS11()
        as21_1 = Dashboard_M14.AS21()
        var_2 = IF(var_1, as11_1, as21_1)
        return var_2

@register(Charts_Data_M14)
class AT7():
    # 'Charts_Data_M14'!AT7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AT11,'Dashboard M14'!AT21)"
    @eval_fn
    def AT7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        at11_1 = Dashboard_M14.AT11()
        at21_1 = Dashboard_M14.AT21()
        var_2 = IF(var_1, at11_1, at21_1)
        return var_2

@register(Charts_Data_M14)
class AU7():
    # 'Charts_Data_M14'!AU7
    value = 0
    formula = "=IF($B$4=$B$3,'Dashboard M14'!AU11,'Dashboard M14'!AU21)"
    @eval_fn
    def AU7():
        b4_1 = Charts_Data_M14.B4()
        b3_1 = Charts_Data_M14.B3()
        var_1 = equal(b4_1, b3_1)
        au11_1 = Dashboard_M14.AU11()
        au21_1 = Dashboard_M14.AU21()
        var_2 = IF(var_1, au11_1, au21_1)
        return var_2

@register(Charts_Data_M14)
class A8():
    # 'Charts_Data_M14'!A8
    value = "Graph Input"

@register(Charts_Data_M14)
class B8():
    # 'Charts_Data_M14'!B8
    value = "Percent of 1990 levels"

@register(Charts_Data_M14)
class C8():
    # 'Charts_Data_M14'!C8
    value = "   Commercial Energy Sector"

@register(Charts_Data_M14)
class F8():
    # 'Charts_Data_M14'!F8
    value = "Notes"

@register(Charts_Data_M14)
class I8():
    # 'Charts_Data_M14'!I8
    value = 1.52136267238
    formula = "='Dashboard M14'!I16"
    @eval_fn
    def I8():
        i16_1 = Dashboard_M14.I16()
        return i16_1

@register(Charts_Data_M14)
class J8():
    # 'Charts_Data_M14'!J8
    value = 3.52891982019
    formula = "='Dashboard M14'!J16"
    @eval_fn
    def J8():
        j16_1 = Dashboard_M14.J16()
        return j16_1

@register(Charts_Data_M14)
class K8():
    # 'Charts_Data_M14'!K8
    value = 0.428483267795
    formula = "='Dashboard M14'!K16"
    @eval_fn
    def K8():
        k16_1 = Dashboard_M14.K16()
        return k16_1

@register(Charts_Data_M14)
class L8():
    # 'Charts_Data_M14'!L8
    value = -0.812341347817
    formula = "='Dashboard M14'!L16"
    @eval_fn
    def L8():
        l16_1 = Dashboard_M14.L16()
        return l16_1

@register(Charts_Data_M14)
class M8():
    # 'Charts_Data_M14'!M8
    value = -0.169909429256
    formula = "='Dashboard M14'!M16"
    @eval_fn
    def M8():
        m16_1 = Dashboard_M14.M16()
        return m16_1

@register(Charts_Data_M14)
class N8():
    # 'Charts_Data_M14'!N8
    value = 0.125066759677
    formula = "='Dashboard M14'!N16"
    @eval_fn
    def N8():
        n16_1 = Dashboard_M14.N16()
        return n16_1

@register(Charts_Data_M14)
class O8():
    # 'Charts_Data_M14'!O8
    value = 1.76039729021
    formula = "='Dashboard M14'!O16"
    @eval_fn
    def O8():
        o16_1 = Dashboard_M14.O16()
        return o16_1

@register(Charts_Data_M14)
class P8():
    # 'Charts_Data_M14'!P8
    value = 2.4217769296
    formula = "='Dashboard M14'!P16"
    @eval_fn
    def P8():
        p16_1 = Dashboard_M14.P16()
        return p16_1

@register(Charts_Data_M14)
class Q8():
    # 'Charts_Data_M14'!Q8
    value = 0.00929523025231
    formula = "='Dashboard M14'!Q16"
    @eval_fn
    def Q8():
        q16_1 = Dashboard_M14.Q16()
        return q16_1

@register(Charts_Data_M14)
class R8():
    # 'Charts_Data_M14'!R8
    value = -0.0794504400591
    formula = "='Dashboard M14'!R16"
    @eval_fn
    def R8():
        r16_1 = Dashboard_M14.R16()
        return r16_1

@register(Charts_Data_M14)
class S8():
    # 'Charts_Data_M14'!S8
    value = 0.141617758927
    formula = "='Dashboard M14'!S16"
    @eval_fn
    def S8():
        s16_1 = Dashboard_M14.S16()
        return s16_1

@register(Charts_Data_M14)
class T8():
    # 'Charts_Data_M14'!T8
    value = -0.0705606214239
    formula = "='Dashboard M14'!T16"
    @eval_fn
    def T8():
        t16_1 = Dashboard_M14.T16()
        return t16_1

@register(Charts_Data_M14)
class U8():
    # 'Charts_Data_M14'!U8
    value = 0.10296989787
    formula = "='Dashboard M14'!U16"
    @eval_fn
    def U8():
        u16_1 = Dashboard_M14.U16()
        return u16_1

@register(Charts_Data_M14)
class V8():
    # 'Charts_Data_M14'!V8
    value = 0.00610912172076
    formula = "='Dashboard M14'!V16"
    @eval_fn
    def V8():
        v16_1 = Dashboard_M14.V16()
        return v16_1

@register(Charts_Data_M14)
class W8():
    # 'Charts_Data_M14'!W8
    value = 0.00769628121406
    formula = "='Dashboard M14'!W16"
    @eval_fn
    def W8():
        w16_1 = Dashboard_M14.W16()
        return w16_1

@register(Charts_Data_M14)
class X8():
    # 'Charts_Data_M14'!X8
    value = -0.131978894658
    formula = "='Dashboard M14'!X16"
    @eval_fn
    def X8():
        x16_1 = Dashboard_M14.X16()
        return x16_1

@register(Charts_Data_M14)
class Y8():
    # 'Charts_Data_M14'!Y8
    value = 0.0273568913166
    formula = "='Dashboard M14'!Y16"
    @eval_fn
    def Y8():
        y16_1 = Dashboard_M14.Y16()
        return y16_1

@register(Charts_Data_M14)
class Z8():
    # 'Charts_Data_M14'!Z8
    value = 0.115494957755
    formula = "='Dashboard M14'!Z16"
    @eval_fn
    def Z8():
        z16_1 = Dashboard_M14.Z16()
        return z16_1

@register(Charts_Data_M14)
class AA8():
    # 'Charts_Data_M14'!AA8
    value = -0.00947387275083
    formula = "='Dashboard M14'!AA16"
    @eval_fn
    def AA8():
        aa16_1 = Dashboard_M14.AA16()
        return aa16_1

@register(Charts_Data_M14)
class AB8():
    # 'Charts_Data_M14'!AB8
    value = 0.103205873116
    formula = "='Dashboard M14'!AB16"
    @eval_fn
    def AB8():
        ab16_1 = Dashboard_M14.AB16()
        return ab16_1

@register(Charts_Data_M14)
class AC8():
    # 'Charts_Data_M14'!AC8
    value = -1.04003504161
    formula = "='Dashboard M14'!AC16"
    @eval_fn
    def AC8():
        ac16_1 = Dashboard_M14.AC16()
        return ac16_1

@register(Charts_Data_M14)
class AD8():
    # 'Charts_Data_M14'!AD8
    value = 0
    formula = "='Dashboard M14'!AD16"
    @eval_fn
    def AD8():
        ad16_1 = Dashboard_M14.AD16()
        return ad16_1

@register(Charts_Data_M14)
class AE8():
    # 'Charts_Data_M14'!AE8
    value = 0
    formula = "='Dashboard M14'!AE16"
    @eval_fn
    def AE8():
        ae16_1 = Dashboard_M14.AE16()
        return ae16_1

@register(Charts_Data_M14)
class AF8():
    # 'Charts_Data_M14'!AF8
    value = 0
    formula = "='Dashboard M14'!AF16"
    @eval_fn
    def AF8():
        af16_1 = Dashboard_M14.AF16()
        return af16_1

@register(Charts_Data_M14)
class AG8():
    # 'Charts_Data_M14'!AG8
    value = 0
    formula = "='Dashboard M14'!AG16"
    @eval_fn
    def AG8():
        ag16_1 = Dashboard_M14.AG16()
        return ag16_1

@register(Charts_Data_M14)
class AH8():
    # 'Charts_Data_M14'!AH8
    value = 0
    formula = "='Dashboard M14'!AH16"
    @eval_fn
    def AH8():
        ah16_1 = Dashboard_M14.AH16()
        return ah16_1

@register(Charts_Data_M14)
class AI8():
    # 'Charts_Data_M14'!AI8
    value = 0
    formula = "='Dashboard M14'!AI16"
    @eval_fn
    def AI8():
        ai16_1 = Dashboard_M14.AI16()
        return ai16_1

@register(Charts_Data_M14)
class AJ8():
    # 'Charts_Data_M14'!AJ8
    value = 0
    formula = "='Dashboard M14'!AJ16"
    @eval_fn
    def AJ8():
        aj16_1 = Dashboard_M14.AJ16()
        return aj16_1

@register(Charts_Data_M14)
class AK8():
    # 'Charts_Data_M14'!AK8
    value = 0
    formula = "='Dashboard M14'!AK16"
    @eval_fn
    def AK8():
        ak16_1 = Dashboard_M14.AK16()
        return ak16_1

@register(Charts_Data_M14)
class AL8():
    # 'Charts_Data_M14'!AL8
    value = 0
    formula = "='Dashboard M14'!AL16"
    @eval_fn
    def AL8():
        al16_1 = Dashboard_M14.AL16()
        return al16_1

@register(Charts_Data_M14)
class AM8():
    # 'Charts_Data_M14'!AM8
    value = 0
    formula = "='Dashboard M14'!AM16"
    @eval_fn
    def AM8():
        am16_1 = Dashboard_M14.AM16()
        return am16_1

@register(Charts_Data_M14)
class AN8():
    # 'Charts_Data_M14'!AN8
    value = 0
    formula = "='Dashboard M14'!AN16"
    @eval_fn
    def AN8():
        an16_1 = Dashboard_M14.AN16()
        return an16_1

@register(Charts_Data_M14)
class AO8():
    # 'Charts_Data_M14'!AO8
    value = 0
    formula = "='Dashboard M14'!AO16"
    @eval_fn
    def AO8():
        ao16_1 = Dashboard_M14.AO16()
        return ao16_1

@register(Charts_Data_M14)
class AP8():
    # 'Charts_Data_M14'!AP8
    value = 0
    formula = "='Dashboard M14'!AP16"
    @eval_fn
    def AP8():
        ap16_1 = Dashboard_M14.AP16()
        return ap16_1

@register(Charts_Data_M14)
class AQ8():
    # 'Charts_Data_M14'!AQ8
    value = 0
    formula = "='Dashboard M14'!AQ16"
    @eval_fn
    def AQ8():
        aq16_1 = Dashboard_M14.AQ16()
        return aq16_1

@register(Charts_Data_M14)
class AR8():
    # 'Charts_Data_M14'!AR8
    value = 0
    formula = "='Dashboard M14'!AR16"
    @eval_fn
    def AR8():
        ar16_1 = Dashboard_M14.AR16()
        return ar16_1

@register(Charts_Data_M14)
class AS8():
    # 'Charts_Data_M14'!AS8
    value = 0
    formula = "='Dashboard M14'!AS16"
    @eval_fn
    def AS8():
        as16_1 = Dashboard_M14.AS16()
        return as16_1

@register(Charts_Data_M14)
class AT8():
    # 'Charts_Data_M14'!AT8
    value = 0
    formula = "='Dashboard M14'!AT16"
    @eval_fn
    def AT8():
        at16_1 = Dashboard_M14.AT16()
        return at16_1

@register(Charts_Data_M14)
class AU8():
    # 'Charts_Data_M14'!AU8
    value = 0
    formula = "='Dashboard M14'!AU16"
    @eval_fn
    def AU8():
        au16_1 = Dashboard_M14.AU16()
        return au16_1

@register(Charts_Data_M14)
class B9():
    # 'Charts_Data_M14'!B9
    value = "Total Emissions (MMTCO2E)"

@register(Charts_Data_M14)
class C9():
    # 'Charts_Data_M14'!C9
    value = "   Industrial Energy Sector"

@register(Charts_Data_M14)
class F9():
    # 'Charts_Data_M14'!F9
    value = "Notes"

@register(Charts_Data_M14)
class I9():
    # 'Charts_Data_M14'!I9
    value = -0.427806660804
    formula = "='Dashboard M14'!I17"
    @eval_fn
    def I9():
        i17_1 = Dashboard_M14.I17()
        return i17_1

@register(Charts_Data_M14)
class J9():
    # 'Charts_Data_M14'!J9
    value = -1.04438400673
    formula = "='Dashboard M14'!J17"
    @eval_fn
    def J9():
        j17_1 = Dashboard_M14.J17()
        return j17_1

@register(Charts_Data_M14)
class K9():
    # 'Charts_Data_M14'!K9
    value = 0.693168533332
    formula = "='Dashboard M14'!K17"
    @eval_fn
    def K9():
        k17_1 = Dashboard_M14.K17()
        return k17_1

@register(Charts_Data_M14)
class L9():
    # 'Charts_Data_M14'!L9
    value = -0.586384459565
    formula = "='Dashboard M14'!L17"
    @eval_fn
    def L9():
        l17_1 = Dashboard_M14.L17()
        return l17_1

@register(Charts_Data_M14)
class M9():
    # 'Charts_Data_M14'!M9
    value = 0.732099396199
    formula = "='Dashboard M14'!M17"
    @eval_fn
    def M9():
        m17_1 = Dashboard_M14.M17()
        return m17_1

@register(Charts_Data_M14)
class N9():
    # 'Charts_Data_M14'!N9
    value = -3.0567942804
    formula = "='Dashboard M14'!N17"
    @eval_fn
    def N9():
        n17_1 = Dashboard_M14.N17()
        return n17_1

@register(Charts_Data_M14)
class O9():
    # 'Charts_Data_M14'!O9
    value = -3.36888107533
    formula = "='Dashboard M14'!O17"
    @eval_fn
    def O9():
        o17_1 = Dashboard_M14.O17()
        return o17_1

@register(Charts_Data_M14)
class P9():
    # 'Charts_Data_M14'!P9
    value = -0.262749273548
    formula = "='Dashboard M14'!P17"
    @eval_fn
    def P9():
        p17_1 = Dashboard_M14.P17()
        return p17_1

@register(Charts_Data_M14)
class Q9():
    # 'Charts_Data_M14'!Q9
    value = 0.0338607819509
    formula = "='Dashboard M14'!Q17"
    @eval_fn
    def Q9():
        q17_1 = Dashboard_M14.Q17()
        return q17_1

@register(Charts_Data_M14)
class R9():
    # 'Charts_Data_M14'!R9
    value = 0.00412683060018
    formula = "='Dashboard M14'!R17"
    @eval_fn
    def R9():
        r17_1 = Dashboard_M14.R17()
        return r17_1

@register(Charts_Data_M14)
class S9():
    # 'Charts_Data_M14'!S9
    value = 0.209412041474
    formula = "='Dashboard M14'!S17"
    @eval_fn
    def S9():
        s17_1 = Dashboard_M14.S17()
        return s17_1

@register(Charts_Data_M14)
class T9():
    # 'Charts_Data_M14'!T9
    value = 0.0406908922553
    formula = "='Dashboard M14'!T17"
    @eval_fn
    def T9():
        t17_1 = Dashboard_M14.T17()
        return t17_1

@register(Charts_Data_M14)
class U9():
    # 'Charts_Data_M14'!U9
    value = -0.026165488532
    formula = "='Dashboard M14'!U17"
    @eval_fn
    def U9():
        u17_1 = Dashboard_M14.U17()
        return u17_1

@register(Charts_Data_M14)
class V9():
    # 'Charts_Data_M14'!V9
    value = 0.420446855348
    formula = "='Dashboard M14'!V17"
    @eval_fn
    def V9():
        v17_1 = Dashboard_M14.V17()
        return v17_1

@register(Charts_Data_M14)
class W9():
    # 'Charts_Data_M14'!W9
    value = 0.0883974295686
    formula = "='Dashboard M14'!W17"
    @eval_fn
    def W9():
        w17_1 = Dashboard_M14.W17()
        return w17_1

@register(Charts_Data_M14)
class X9():
    # 'Charts_Data_M14'!X9
    value = -0.525713981308
    formula = "='Dashboard M14'!X17"
    @eval_fn
    def X9():
        x17_1 = Dashboard_M14.X17()
        return x17_1

@register(Charts_Data_M14)
class Y9():
    # 'Charts_Data_M14'!Y9
    value = -0.420087957673
    formula = "='Dashboard M14'!Y17"
    @eval_fn
    def Y9():
        y17_1 = Dashboard_M14.Y17()
        return y17_1

@register(Charts_Data_M14)
class Z9():
    # 'Charts_Data_M14'!Z9
    value = -0.027800095301
    formula = "='Dashboard M14'!Z17"
    @eval_fn
    def Z9():
        z17_1 = Dashboard_M14.Z17()
        return z17_1

@register(Charts_Data_M14)
class AA9():
    # 'Charts_Data_M14'!AA9
    value = -0.0222003369594
    formula = "='Dashboard M14'!AA17"
    @eval_fn
    def AA9():
        aa17_1 = Dashboard_M14.AA17()
        return aa17_1

@register(Charts_Data_M14)
class AB9():
    # 'Charts_Data_M14'!AB9
    value = 0.0577074474014
    formula = "='Dashboard M14'!AB17"
    @eval_fn
    def AB9():
        ab17_1 = Dashboard_M14.AB17()
        return ab17_1

@register(Charts_Data_M14)
class AC9():
    # 'Charts_Data_M14'!AC9
    value = -2.09750430532
    formula = "='Dashboard M14'!AC17"
    @eval_fn
    def AC9():
        ac17_1 = Dashboard_M14.AC17()
        return ac17_1

@register(Charts_Data_M14)
class AD9():
    # 'Charts_Data_M14'!AD9
    value = 0
    formula = "='Dashboard M14'!AD17"
    @eval_fn
    def AD9():
        ad17_1 = Dashboard_M14.AD17()
        return ad17_1

@register(Charts_Data_M14)
class AE9():
    # 'Charts_Data_M14'!AE9
    value = 0
    formula = "='Dashboard M14'!AE17"
    @eval_fn
    def AE9():
        ae17_1 = Dashboard_M14.AE17()
        return ae17_1

@register(Charts_Data_M14)
class AF9():
    # 'Charts_Data_M14'!AF9
    value = 0
    formula = "='Dashboard M14'!AF17"
    @eval_fn
    def AF9():
        af17_1 = Dashboard_M14.AF17()
        return af17_1

@register(Charts_Data_M14)
class AG9():
    # 'Charts_Data_M14'!AG9
    value = 0
    formula = "='Dashboard M14'!AG17"
    @eval_fn
    def AG9():
        ag17_1 = Dashboard_M14.AG17()
        return ag17_1

@register(Charts_Data_M14)
class AH9():
    # 'Charts_Data_M14'!AH9
    value = 0
    formula = "='Dashboard M14'!AH17"
    @eval_fn
    def AH9():
        ah17_1 = Dashboard_M14.AH17()
        return ah17_1

@register(Charts_Data_M14)
class AI9():
    # 'Charts_Data_M14'!AI9
    value = 0
    formula = "='Dashboard M14'!AI17"
    @eval_fn
    def AI9():
        ai17_1 = Dashboard_M14.AI17()
        return ai17_1

@register(Charts_Data_M14)
class AJ9():
    # 'Charts_Data_M14'!AJ9
    value = 0
    formula = "='Dashboard M14'!AJ17"
    @eval_fn
    def AJ9():
        aj17_1 = Dashboard_M14.AJ17()
        return aj17_1

@register(Charts_Data_M14)
class AK9():
    # 'Charts_Data_M14'!AK9
    value = 0
    formula = "='Dashboard M14'!AK17"
    @eval_fn
    def AK9():
        ak17_1 = Dashboard_M14.AK17()
        return ak17_1

@register(Charts_Data_M14)
class AL9():
    # 'Charts_Data_M14'!AL9
    value = 0
    formula = "='Dashboard M14'!AL17"
    @eval_fn
    def AL9():
        al17_1 = Dashboard_M14.AL17()
        return al17_1

@register(Charts_Data_M14)
class AM9():
    # 'Charts_Data_M14'!AM9
    value = 0
    formula = "='Dashboard M14'!AM17"
    @eval_fn
    def AM9():
        am17_1 = Dashboard_M14.AM17()
        return am17_1

@register(Charts_Data_M14)
class AN9():
    # 'Charts_Data_M14'!AN9
    value = 0
    formula = "='Dashboard M14'!AN17"
    @eval_fn
    def AN9():
        an17_1 = Dashboard_M14.AN17()
        return an17_1

@register(Charts_Data_M14)
class AO9():
    # 'Charts_Data_M14'!AO9
    value = 0
    formula = "='Dashboard M14'!AO17"
    @eval_fn
    def AO9():
        ao17_1 = Dashboard_M14.AO17()
        return ao17_1

@register(Charts_Data_M14)
class AP9():
    # 'Charts_Data_M14'!AP9
    value = 0
    formula = "='Dashboard M14'!AP17"
    @eval_fn
    def AP9():
        ap17_1 = Dashboard_M14.AP17()
        return ap17_1

@register(Charts_Data_M14)
class AQ9():
    # 'Charts_Data_M14'!AQ9
    value = 0
    formula = "='Dashboard M14'!AQ17"
    @eval_fn
    def AQ9():
        aq17_1 = Dashboard_M14.AQ17()
        return aq17_1

@register(Charts_Data_M14)
class AR9():
    # 'Charts_Data_M14'!AR9
    value = 0
    formula = "='Dashboard M14'!AR17"
    @eval_fn
    def AR9():
        ar17_1 = Dashboard_M14.AR17()
        return ar17_1

@register(Charts_Data_M14)
class AS9():
    # 'Charts_Data_M14'!AS9
    value = 0
    formula = "='Dashboard M14'!AS17"
    @eval_fn
    def AS9():
        as17_1 = Dashboard_M14.AS17()
        return as17_1

@register(Charts_Data_M14)
class AT9():
    # 'Charts_Data_M14'!AT9
    value = 0
    formula = "='Dashboard M14'!AT17"
    @eval_fn
    def AT9():
        at17_1 = Dashboard_M14.AT17()
        return at17_1

@register(Charts_Data_M14)
class AU9():
    # 'Charts_Data_M14'!AU9
    value = 0
    formula = "='Dashboard M14'!AU17"
    @eval_fn
    def AU9():
        au17_1 = Dashboard_M14.AU17()
        return au17_1

@register(Charts_Data_M14)
class B10():
    # 'Charts_Data_M14'!B10
    value = "Total Emissions (MMTCO2E)"
    formula = "=IF('Charts M14'!A8=1,'Charts Data M14'!B8,'Charts Data M14'!B9)"
    @eval_fn
    def B10():
        a8_1 = Charts_M14.A8()
        var_1 = equal(a8_1, 1)
        b8_1 = Charts_Data_M14.B8()
        b9_1 = Charts_Data_M14.B9()
        var_2 = IF(var_1, b8_1, b9_1)
        return var_2

@register(Charts_Data_M14)
class C10():
    # 'Charts_Data_M14'!C10
    value = "   Residential Energy Sector"

@register(Charts_Data_M14)
class F10():
    # 'Charts_Data_M14'!F10
    value = "Notes"

@register(Charts_Data_M14)
class I10():
    # 'Charts_Data_M14'!I10
    value = 59.2024708066
    formula = "='Dashboard M14'!I18"
    @eval_fn
    def I10():
        i18_1 = Dashboard_M14.I18()
        return i18_1

@register(Charts_Data_M14)
class J10():
    # 'Charts_Data_M14'!J10
    value = 1.14465670144
    formula = "='Dashboard M14'!J18"
    @eval_fn
    def J10():
        j18_1 = Dashboard_M14.J18()
        return j18_1

@register(Charts_Data_M14)
class K10():
    # 'Charts_Data_M14'!K10
    value = 0.229749327068
    formula = "='Dashboard M14'!K18"
    @eval_fn
    def K10():
        k18_1 = Dashboard_M14.K18()
        return k18_1

@register(Charts_Data_M14)
class L10():
    # 'Charts_Data_M14'!L10
    value = -0.214405540205
    formula = "='Dashboard M14'!L18"
    @eval_fn
    def L10():
        l18_1 = Dashboard_M14.L18()
        return l18_1

@register(Charts_Data_M14)
class M10():
    # 'Charts_Data_M14'!M10
    value = -0.0251836160989
    formula = "='Dashboard M14'!M18"
    @eval_fn
    def M10():
        m18_1 = Dashboard_M14.M18()
        return m18_1

@register(Charts_Data_M14)
class N10():
    # 'Charts_Data_M14'!N10
    value = 1.89672815766
    formula = "='Dashboard M14'!N18"
    @eval_fn
    def N10():
        n18_1 = Dashboard_M14.N18()
        return n18_1

@register(Charts_Data_M14)
class O10():
    # 'Charts_Data_M14'!O10
    value = -10.9270187497
    formula = "='Dashboard M14'!O18"
    @eval_fn
    def O10():
        o18_1 = Dashboard_M14.O18()
        return o18_1

@register(Charts_Data_M14)
class P10():
    # 'Charts_Data_M14'!P10
    value = 0.601241500386
    formula = "='Dashboard M14'!P18"
    @eval_fn
    def P10():
        p18_1 = Dashboard_M14.P18()
        return p18_1

@register(Charts_Data_M14)
class Q10():
    # 'Charts_Data_M14'!Q10
    value = -0.738258682117
    formula = "='Dashboard M14'!Q18"
    @eval_fn
    def Q10():
        q18_1 = Dashboard_M14.Q18()
        return q18_1

@register(Charts_Data_M14)
class R10():
    # 'Charts_Data_M14'!R10
    value = -0.0146775375104
    formula = "='Dashboard M14'!R18"
    @eval_fn
    def R10():
        r18_1 = Dashboard_M14.R18()
        return r18_1

@register(Charts_Data_M14)
class S10():
    # 'Charts_Data_M14'!S10
    value = -0.0290908549203
    formula = "='Dashboard M14'!S18"
    @eval_fn
    def S10():
        s18_1 = Dashboard_M14.S18()
        return s18_1

@register(Charts_Data_M14)
class T10():
    # 'Charts_Data_M14'!T10
    value = 0.399444101651
    formula = "='Dashboard M14'!T18"
    @eval_fn
    def T10():
        t18_1 = Dashboard_M14.T18()
        return t18_1

@register(Charts_Data_M14)
class U10():
    # 'Charts_Data_M14'!U10
    value = -0.00088382009241
    formula = "='Dashboard M14'!U18"
    @eval_fn
    def U10():
        u18_1 = Dashboard_M14.U18()
        return u18_1

@register(Charts_Data_M14)
class V10():
    # 'Charts_Data_M14'!V10
    value = 0.00759667280284
    formula = "='Dashboard M14'!V18"
    @eval_fn
    def V10():
        v18_1 = Dashboard_M14.V18()
        return v18_1

@register(Charts_Data_M14)
class W10():
    # 'Charts_Data_M14'!W10
    value = -0.136322959995
    formula = "='Dashboard M14'!W18"
    @eval_fn
    def W10():
        w18_1 = Dashboard_M14.W18()
        return w18_1

@register(Charts_Data_M14)
class X10():
    # 'Charts_Data_M14'!X10
    value = 0.3766234709
    formula = "='Dashboard M14'!X18"
    @eval_fn
    def X10():
        x18_1 = Dashboard_M14.X18()
        return x18_1

@register(Charts_Data_M14)
class Y10():
    # 'Charts_Data_M14'!Y10
    value = -2.47353378
    formula = "='Dashboard M14'!Y18"
    @eval_fn
    def Y10():
        y18_1 = Dashboard_M14.Y18()
        return y18_1

@register(Charts_Data_M14)
class Z10():
    # 'Charts_Data_M14'!Z10
    value = 0.128380486119
    formula = "='Dashboard M14'!Z18"
    @eval_fn
    def Z10():
        z18_1 = Dashboard_M14.Z18()
        return z18_1

@register(Charts_Data_M14)
class AA10():
    # 'Charts_Data_M14'!AA10
    value = 0.0288188712864
    formula = "='Dashboard M14'!AA18"
    @eval_fn
    def AA10():
        aa18_1 = Dashboard_M14.AA18()
        return aa18_1

@register(Charts_Data_M14)
class AB10():
    # 'Charts_Data_M14'!AB10
    value = 0.0885861931199
    formula = "='Dashboard M14'!AB18"
    @eval_fn
    def AB10():
        ab18_1 = Dashboard_M14.AB18()
        return ab18_1

@register(Charts_Data_M14)
class AC10():
    # 'Charts_Data_M14'!AC10
    value = 2.27925503058
    formula = "='Dashboard M14'!AC18"
    @eval_fn
    def AC10():
        ac18_1 = Dashboard_M14.AC18()
        return ac18_1

@register(Charts_Data_M14)
class AD10():
    # 'Charts_Data_M14'!AD10
    value = 0
    formula = "='Dashboard M14'!AD18"
    @eval_fn
    def AD10():
        ad18_1 = Dashboard_M14.AD18()
        return ad18_1

@register(Charts_Data_M14)
class AE10():
    # 'Charts_Data_M14'!AE10
    value = 0
    formula = "='Dashboard M14'!AE18"
    @eval_fn
    def AE10():
        ae18_1 = Dashboard_M14.AE18()
        return ae18_1

@register(Charts_Data_M14)
class AF10():
    # 'Charts_Data_M14'!AF10
    value = 0
    formula = "='Dashboard M14'!AF18"
    @eval_fn
    def AF10():
        af18_1 = Dashboard_M14.AF18()
        return af18_1

@register(Charts_Data_M14)
class AG10():
    # 'Charts_Data_M14'!AG10
    value = 0
    formula = "='Dashboard M14'!AG18"
    @eval_fn
    def AG10():
        ag18_1 = Dashboard_M14.AG18()
        return ag18_1

@register(Charts_Data_M14)
class AH10():
    # 'Charts_Data_M14'!AH10
    value = 0
    formula = "='Dashboard M14'!AH18"
    @eval_fn
    def AH10():
        ah18_1 = Dashboard_M14.AH18()
        return ah18_1

@register(Charts_Data_M14)
class AI10():
    # 'Charts_Data_M14'!AI10
    value = 0
    formula = "='Dashboard M14'!AI18"
    @eval_fn
    def AI10():
        ai18_1 = Dashboard_M14.AI18()
        return ai18_1

@register(Charts_Data_M14)
class AJ10():
    # 'Charts_Data_M14'!AJ10
    value = 0
    formula = "='Dashboard M14'!AJ18"
    @eval_fn
    def AJ10():
        aj18_1 = Dashboard_M14.AJ18()
        return aj18_1

@register(Charts_Data_M14)
class AK10():
    # 'Charts_Data_M14'!AK10
    value = 0
    formula = "='Dashboard M14'!AK18"
    @eval_fn
    def AK10():
        ak18_1 = Dashboard_M14.AK18()
        return ak18_1

@register(Charts_Data_M14)
class AL10():
    # 'Charts_Data_M14'!AL10
    value = 0
    formula = "='Dashboard M14'!AL18"
    @eval_fn
    def AL10():
        al18_1 = Dashboard_M14.AL18()
        return al18_1

@register(Charts_Data_M14)
class AM10():
    # 'Charts_Data_M14'!AM10
    value = 0
    formula = "='Dashboard M14'!AM18"
    @eval_fn
    def AM10():
        am18_1 = Dashboard_M14.AM18()
        return am18_1

@register(Charts_Data_M14)
class AN10():
    # 'Charts_Data_M14'!AN10
    value = 0
    formula = "='Dashboard M14'!AN18"
    @eval_fn
    def AN10():
        an18_1 = Dashboard_M14.AN18()
        return an18_1

@register(Charts_Data_M14)
class AO10():
    # 'Charts_Data_M14'!AO10
    value = 0
    formula = "='Dashboard M14'!AO18"
    @eval_fn
    def AO10():
        ao18_1 = Dashboard_M14.AO18()
        return ao18_1

@register(Charts_Data_M14)
class AP10():
    # 'Charts_Data_M14'!AP10
    value = 0
    formula = "='Dashboard M14'!AP18"
    @eval_fn
    def AP10():
        ap18_1 = Dashboard_M14.AP18()
        return ap18_1

@register(Charts_Data_M14)
class AQ10():
    # 'Charts_Data_M14'!AQ10
    value = 0
    formula = "='Dashboard M14'!AQ18"
    @eval_fn
    def AQ10():
        aq18_1 = Dashboard_M14.AQ18()
        return aq18_1

@register(Charts_Data_M14)
class AR10():
    # 'Charts_Data_M14'!AR10
    value = 0
    formula = "='Dashboard M14'!AR18"
    @eval_fn
    def AR10():
        ar18_1 = Dashboard_M14.AR18()
        return ar18_1

@register(Charts_Data_M14)
class AS10():
    # 'Charts_Data_M14'!AS10
    value = 0
    formula = "='Dashboard M14'!AS18"
    @eval_fn
    def AS10():
        as18_1 = Dashboard_M14.AS18()
        return as18_1

@register(Charts_Data_M14)
class AT10():
    # 'Charts_Data_M14'!AT10
    value = 0
    formula = "='Dashboard M14'!AT18"
    @eval_fn
    def AT10():
        at18_1 = Dashboard_M14.AT18()
        return at18_1

@register(Charts_Data_M14)
class AU10():
    # 'Charts_Data_M14'!AU10
    value = 0
    formula = "='Dashboard M14'!AU18"
    @eval_fn
    def AU10():
        au18_1 = Dashboard_M14.AU18()
        return au18_1

@register(Charts_Data_M14)
class C11():
    # 'Charts_Data_M14'!C11
    value = "   Transportation Sector"

@register(Charts_Data_M14)
class F11():
    # 'Charts_Data_M14'!F11
    value = "Notes"

@register(Charts_Data_M14)
class I11():
    # 'Charts_Data_M14'!I11
    value = -2.01819599964
    formula = "='Dashboard M14'!I19"
    @eval_fn
    def I11():
        i19_1 = Dashboard_M14.I19()
        return i19_1

@register(Charts_Data_M14)
class J11():
    # 'Charts_Data_M14'!J11
    value = -1.37600558558
    formula = "='Dashboard M14'!J19"
    @eval_fn
    def J11():
        j19_1 = Dashboard_M14.J19()
        return j19_1

@register(Charts_Data_M14)
class K11():
    # 'Charts_Data_M14'!K11
    value = 0.38801494962
    formula = "='Dashboard M14'!K19"
    @eval_fn
    def K11():
        k19_1 = Dashboard_M14.K19()
        return k19_1

@register(Charts_Data_M14)
class L11():
    # 'Charts_Data_M14'!L11
    value = -0.140876715109
    formula = "='Dashboard M14'!L19"
    @eval_fn
    def L11():
        l19_1 = Dashboard_M14.L19()
        return l19_1

@register(Charts_Data_M14)
class M11():
    # 'Charts_Data_M14'!M11
    value = -0.946879287893
    formula = "='Dashboard M14'!M19"
    @eval_fn
    def M11():
        m19_1 = Dashboard_M14.M19()
        return m19_1

@register(Charts_Data_M14)
class N11():
    # 'Charts_Data_M14'!N11
    value = -0.134246469074
    formula = "='Dashboard M14'!N19"
    @eval_fn
    def N11():
        n19_1 = Dashboard_M14.N19()
        return n19_1

@register(Charts_Data_M14)
class O11():
    # 'Charts_Data_M14'!O11
    value = -0.0707829860594
    formula = "='Dashboard M14'!O19"
    @eval_fn
    def O11():
        o19_1 = Dashboard_M14.O19()
        return o19_1

@register(Charts_Data_M14)
class P11():
    # 'Charts_Data_M14'!P11
    value = 0.221716278129
    formula = "='Dashboard M14'!P19"
    @eval_fn
    def P11():
        p19_1 = Dashboard_M14.P19()
        return p19_1

@register(Charts_Data_M14)
class Q11():
    # 'Charts_Data_M14'!Q11
    value = 0.0697392257468
    formula = "='Dashboard M14'!Q19"
    @eval_fn
    def Q11():
        q19_1 = Dashboard_M14.Q19()
        return q19_1

@register(Charts_Data_M14)
class R11():
    # 'Charts_Data_M14'!R11
    value = 0.244637965138
    formula = "='Dashboard M14'!R19"
    @eval_fn
    def R11():
        r19_1 = Dashboard_M14.R19()
        return r19_1

@register(Charts_Data_M14)
class S11():
    # 'Charts_Data_M14'!S11
    value = 0.364556828304
    formula = "='Dashboard M14'!S19"
    @eval_fn
    def S11():
        s19_1 = Dashboard_M14.S19()
        return s19_1

@register(Charts_Data_M14)
class T11():
    # 'Charts_Data_M14'!T11
    value = 1.63335310672
    formula = "='Dashboard M14'!T19"
    @eval_fn
    def T11():
        t19_1 = Dashboard_M14.T19()
        return t19_1

@register(Charts_Data_M14)
class U11():
    # 'Charts_Data_M14'!U11
    value = -1.06614813506
    formula = "='Dashboard M14'!U19"
    @eval_fn
    def U11():
        u19_1 = Dashboard_M14.U19()
        return u19_1

@register(Charts_Data_M14)
class V11():
    # 'Charts_Data_M14'!V11
    value = -0.306187495333
    formula = "='Dashboard M14'!V19"
    @eval_fn
    def V11():
        v19_1 = Dashboard_M14.V19()
        return v19_1

@register(Charts_Data_M14)
class W11():
    # 'Charts_Data_M14'!W11
    value = -0.111918615312
    formula = "='Dashboard M14'!W19"
    @eval_fn
    def W11():
        w19_1 = Dashboard_M14.W19()
        return w19_1

@register(Charts_Data_M14)
class X11():
    # 'Charts_Data_M14'!X11
    value = -0.548061637464
    formula = "='Dashboard M14'!X19"
    @eval_fn
    def X11():
        x19_1 = Dashboard_M14.X19()
        return x19_1

@register(Charts_Data_M14)
class Y11():
    # 'Charts_Data_M14'!Y11
    value = 1.47682150589
    formula = "='Dashboard M14'!Y19"
    @eval_fn
    def Y11():
        y19_1 = Dashboard_M14.Y19()
        return y19_1

@register(Charts_Data_M14)
class Z11():
    # 'Charts_Data_M14'!Z11
    value = -0.184646368088
    formula = "='Dashboard M14'!Z19"
    @eval_fn
    def Z11():
        z19_1 = Dashboard_M14.Z19()
        return z19_1

@register(Charts_Data_M14)
class AA11():
    # 'Charts_Data_M14'!AA11
    value = 0.125826142946
    formula = "='Dashboard M14'!AA19"
    @eval_fn
    def AA11():
        aa19_1 = Dashboard_M14.AA19()
        return aa19_1

@register(Charts_Data_M14)
class AB11():
    # 'Charts_Data_M14'!AB11
    value = 0.389834897718
    formula = "='Dashboard M14'!AB19"
    @eval_fn
    def AB11():
        ab19_1 = Dashboard_M14.AB19()
        return ab19_1

@register(Charts_Data_M14)
class AC11():
    # 'Charts_Data_M14'!AC11
    value = -11.4402836237
    formula = "='Dashboard M14'!AC19"
    @eval_fn
    def AC11():
        ac19_1 = Dashboard_M14.AC19()
        return ac19_1

@register(Charts_Data_M14)
class AD11():
    # 'Charts_Data_M14'!AD11
    value = 0
    formula = "='Dashboard M14'!AD19"
    @eval_fn
    def AD11():
        ad19_1 = Dashboard_M14.AD19()
        return ad19_1

@register(Charts_Data_M14)
class AE11():
    # 'Charts_Data_M14'!AE11
    value = 0
    formula = "='Dashboard M14'!AE19"
    @eval_fn
    def AE11():
        ae19_1 = Dashboard_M14.AE19()
        return ae19_1

@register(Charts_Data_M14)
class AF11():
    # 'Charts_Data_M14'!AF11
    value = 0
    formula = "='Dashboard M14'!AF19"
    @eval_fn
    def AF11():
        af19_1 = Dashboard_M14.AF19()
        return af19_1

@register(Charts_Data_M14)
class AG11():
    # 'Charts_Data_M14'!AG11
    value = 0
    formula = "='Dashboard M14'!AG19"
    @eval_fn
    def AG11():
        ag19_1 = Dashboard_M14.AG19()
        return ag19_1

@register(Charts_Data_M14)
class AH11():
    # 'Charts_Data_M14'!AH11
    value = 0
    formula = "='Dashboard M14'!AH19"
    @eval_fn
    def AH11():
        ah19_1 = Dashboard_M14.AH19()
        return ah19_1

@register(Charts_Data_M14)
class AI11():
    # 'Charts_Data_M14'!AI11
    value = 0
    formula = "='Dashboard M14'!AI19"
    @eval_fn
    def AI11():
        ai19_1 = Dashboard_M14.AI19()
        return ai19_1

@register(Charts_Data_M14)
class AJ11():
    # 'Charts_Data_M14'!AJ11
    value = 0
    formula = "='Dashboard M14'!AJ19"
    @eval_fn
    def AJ11():
        aj19_1 = Dashboard_M14.AJ19()
        return aj19_1

@register(Charts_Data_M14)
class AK11():
    # 'Charts_Data_M14'!AK11
    value = 0
    formula = "='Dashboard M14'!AK19"
    @eval_fn
    def AK11():
        ak19_1 = Dashboard_M14.AK19()
        return ak19_1

@register(Charts_Data_M14)
class AL11():
    # 'Charts_Data_M14'!AL11
    value = 0
    formula = "='Dashboard M14'!AL19"
    @eval_fn
    def AL11():
        al19_1 = Dashboard_M14.AL19()
        return al19_1

@register(Charts_Data_M14)
class AM11():
    # 'Charts_Data_M14'!AM11
    value = 0
    formula = "='Dashboard M14'!AM19"
    @eval_fn
    def AM11():
        am19_1 = Dashboard_M14.AM19()
        return am19_1

@register(Charts_Data_M14)
class AN11():
    # 'Charts_Data_M14'!AN11
    value = 0
    formula = "='Dashboard M14'!AN19"
    @eval_fn
    def AN11():
        an19_1 = Dashboard_M14.AN19()
        return an19_1

@register(Charts_Data_M14)
class AO11():
    # 'Charts_Data_M14'!AO11
    value = 0
    formula = "='Dashboard M14'!AO19"
    @eval_fn
    def AO11():
        ao19_1 = Dashboard_M14.AO19()
        return ao19_1

@register(Charts_Data_M14)
class AP11():
    # 'Charts_Data_M14'!AP11
    value = 0
    formula = "='Dashboard M14'!AP19"
    @eval_fn
    def AP11():
        ap19_1 = Dashboard_M14.AP19()
        return ap19_1

@register(Charts_Data_M14)
class AQ11():
    # 'Charts_Data_M14'!AQ11
    value = 0
    formula = "='Dashboard M14'!AQ19"
    @eval_fn
    def AQ11():
        aq19_1 = Dashboard_M14.AQ19()
        return aq19_1

@register(Charts_Data_M14)
class AR11():
    # 'Charts_Data_M14'!AR11
    value = 0
    formula = "='Dashboard M14'!AR19"
    @eval_fn
    def AR11():
        ar19_1 = Dashboard_M14.AR19()
        return ar19_1

@register(Charts_Data_M14)
class AS11():
    # 'Charts_Data_M14'!AS11
    value = 0
    formula = "='Dashboard M14'!AS19"
    @eval_fn
    def AS11():
        as19_1 = Dashboard_M14.AS19()
        return as19_1

@register(Charts_Data_M14)
class AT11():
    # 'Charts_Data_M14'!AT11
    value = 0
    formula = "='Dashboard M14'!AT19"
    @eval_fn
    def AT11():
        at19_1 = Dashboard_M14.AT19()
        return at19_1

@register(Charts_Data_M14)
class AU11():
    # 'Charts_Data_M14'!AU11
    value = 0
    formula = "='Dashboard M14'!AU19"
    @eval_fn
    def AU11():
        au19_1 = Dashboard_M14.AU19()
        return au19_1

@register(Charts_Data_M14)
class C12():
    # 'Charts_Data_M14'!C12
    value = "   Electric Power Sector"

@register(Charts_Data_M14)
class F12():
    # 'Charts_Data_M14'!F12
    value = "Notes"

@register(Charts_Data_M14)
class I12():
    # 'Charts_Data_M14'!I12
    value = 0.739171008713
    formula = "='Dashboard M14'!I20"
    @eval_fn
    def I12():
        i20_1 = Dashboard_M14.I20()
        return i20_1

@register(Charts_Data_M14)
class J12():
    # 'Charts_Data_M14'!J12
    value = 0.0699967891904
    formula = "='Dashboard M14'!J20"
    @eval_fn
    def J12():
        j20_1 = Dashboard_M14.J20()
        return j20_1

@register(Charts_Data_M14)
class K12():
    # 'Charts_Data_M14'!K12
    value = 0.741954186703
    formula = "='Dashboard M14'!K20"
    @eval_fn
    def K12():
        k20_1 = Dashboard_M14.K20()
        return k20_1

@register(Charts_Data_M14)
class L12():
    # 'Charts_Data_M14'!L12
    value = 3.3195416984
    formula = "='Dashboard M14'!L20"
    @eval_fn
    def L12():
        l20_1 = Dashboard_M14.L20()
        return l20_1

@register(Charts_Data_M14)
class M12():
    # 'Charts_Data_M14'!M12
    value = -1.45706206325
    formula = "='Dashboard M14'!M20"
    @eval_fn
    def M12():
        m20_1 = Dashboard_M14.M20()
        return m20_1

@register(Charts_Data_M14)
class N12():
    # 'Charts_Data_M14'!N12
    value = 0.136420657958
    formula = "='Dashboard M14'!N20"
    @eval_fn
    def N12():
        n20_1 = Dashboard_M14.N20()
        return n20_1

@register(Charts_Data_M14)
class O12():
    # 'Charts_Data_M14'!O12
    value = 0.436557005225
    formula = "='Dashboard M14'!O20"
    @eval_fn
    def O12():
        o20_1 = Dashboard_M14.O20()
        return o20_1

@register(Charts_Data_M14)
class P12():
    # 'Charts_Data_M14'!P12
    value = -0.436983651881
    formula = "='Dashboard M14'!P20"
    @eval_fn
    def P12():
        p20_1 = Dashboard_M14.P20()
        return p20_1

@register(Charts_Data_M14)
class Q12():
    # 'Charts_Data_M14'!Q12
    value = -0.371388371864
    formula = "='Dashboard M14'!Q20"
    @eval_fn
    def Q12():
        q20_1 = Dashboard_M14.Q20()
        return q20_1

@register(Charts_Data_M14)
class R12():
    # 'Charts_Data_M14'!R12
    value = 0.0106253872571
    formula = "='Dashboard M14'!R20"
    @eval_fn
    def R12():
        r20_1 = Dashboard_M14.R20()
        return r20_1

@register(Charts_Data_M14)
class S12():
    # 'Charts_Data_M14'!S12
    value = -1.31488172315
    formula = "='Dashboard M14'!S20"
    @eval_fn
    def S12():
        s20_1 = Dashboard_M14.S20()
        return s20_1

@register(Charts_Data_M14)
class T12():
    # 'Charts_Data_M14'!T12
    value = 0.571271671501
    formula = "='Dashboard M14'!T20"
    @eval_fn
    def T12():
        t20_1 = Dashboard_M14.T20()
        return t20_1

@register(Charts_Data_M14)
class U12():
    # 'Charts_Data_M14'!U12
    value = -0.670166421962
    formula = "='Dashboard M14'!U20"
    @eval_fn
    def U12():
        u20_1 = Dashboard_M14.U20()
        return u20_1

@register(Charts_Data_M14)
class V12():
    # 'Charts_Data_M14'!V12
    value = 0.0725972848696
    formula = "='Dashboard M14'!V20"
    @eval_fn
    def V12():
        v20_1 = Dashboard_M14.V20()
        return v20_1

@register(Charts_Data_M14)
class W12():
    # 'Charts_Data_M14'!W12
    value = 0.0380248666082
    formula = "='Dashboard M14'!W20"
    @eval_fn
    def W12():
        w20_1 = Dashboard_M14.W20()
        return w20_1

@register(Charts_Data_M14)
class X12():
    # 'Charts_Data_M14'!X12
    value = -0.0432288231891
    formula = "='Dashboard M14'!X20"
    @eval_fn
    def X12():
        x20_1 = Dashboard_M14.X20()
        return x20_1

@register(Charts_Data_M14)
class Y12():
    # 'Charts_Data_M14'!Y12
    value = 0.277735031347
    formula = "='Dashboard M14'!Y20"
    @eval_fn
    def Y12():
        y20_1 = Dashboard_M14.Y20()
        return y20_1

@register(Charts_Data_M14)
class Z12():
    # 'Charts_Data_M14'!Z12
    value = 0.429238762277
    formula = "='Dashboard M14'!Z20"
    @eval_fn
    def Z12():
        z20_1 = Dashboard_M14.Z20()
        return z20_1

@register(Charts_Data_M14)
class AA12():
    # 'Charts_Data_M14'!AA12
    value = 0.998523883436
    formula = "='Dashboard M14'!AA20"
    @eval_fn
    def AA12():
        aa20_1 = Dashboard_M14.AA20()
        return aa20_1

@register(Charts_Data_M14)
class AB12():
    # 'Charts_Data_M14'!AB12
    value = 318.59324072
    formula = "='Dashboard M14'!AB20"
    @eval_fn
    def AB12():
        ab20_1 = Dashboard_M14.AB20()
        return ab20_1

@register(Charts_Data_M14)
class AC12():
    # 'Charts_Data_M14'!AC12
    value = -55.4549580727
    formula = "='Dashboard M14'!AC20"
    @eval_fn
    def AC12():
        ac20_1 = Dashboard_M14.AC20()
        return ac20_1

@register(Charts_Data_M14)
class AD12():
    # 'Charts_Data_M14'!AD12
    value = 0
    formula = "='Dashboard M14'!AD20"
    @eval_fn
    def AD12():
        ad20_1 = Dashboard_M14.AD20()
        return ad20_1

@register(Charts_Data_M14)
class AE12():
    # 'Charts_Data_M14'!AE12
    value = 0
    formula = "='Dashboard M14'!AE20"
    @eval_fn
    def AE12():
        ae20_1 = Dashboard_M14.AE20()
        return ae20_1

@register(Charts_Data_M14)
class AF12():
    # 'Charts_Data_M14'!AF12
    value = 0
    formula = "='Dashboard M14'!AF20"
    @eval_fn
    def AF12():
        af20_1 = Dashboard_M14.AF20()
        return af20_1

@register(Charts_Data_M14)
class AG12():
    # 'Charts_Data_M14'!AG12
    value = 0
    formula = "='Dashboard M14'!AG20"
    @eval_fn
    def AG12():
        ag20_1 = Dashboard_M14.AG20()
        return ag20_1

@register(Charts_Data_M14)
class AH12():
    # 'Charts_Data_M14'!AH12
    value = 0
    formula = "='Dashboard M14'!AH20"
    @eval_fn
    def AH12():
        ah20_1 = Dashboard_M14.AH20()
        return ah20_1

@register(Charts_Data_M14)
class AI12():
    # 'Charts_Data_M14'!AI12
    value = 0
    formula = "='Dashboard M14'!AI20"
    @eval_fn
    def AI12():
        ai20_1 = Dashboard_M14.AI20()
        return ai20_1

@register(Charts_Data_M14)
class AJ12():
    # 'Charts_Data_M14'!AJ12
    value = 0
    formula = "='Dashboard M14'!AJ20"
    @eval_fn
    def AJ12():
        aj20_1 = Dashboard_M14.AJ20()
        return aj20_1

@register(Charts_Data_M14)
class AK12():
    # 'Charts_Data_M14'!AK12
    value = 0
    formula = "='Dashboard M14'!AK20"
    @eval_fn
    def AK12():
        ak20_1 = Dashboard_M14.AK20()
        return ak20_1

@register(Charts_Data_M14)
class AL12():
    # 'Charts_Data_M14'!AL12
    value = 0
    formula = "='Dashboard M14'!AL20"
    @eval_fn
    def AL12():
        al20_1 = Dashboard_M14.AL20()
        return al20_1

@register(Charts_Data_M14)
class AM12():
    # 'Charts_Data_M14'!AM12
    value = 0
    formula = "='Dashboard M14'!AM20"
    @eval_fn
    def AM12():
        am20_1 = Dashboard_M14.AM20()
        return am20_1

@register(Charts_Data_M14)
class AN12():
    # 'Charts_Data_M14'!AN12
    value = 0
    formula = "='Dashboard M14'!AN20"
    @eval_fn
    def AN12():
        an20_1 = Dashboard_M14.AN20()
        return an20_1

@register(Charts_Data_M14)
class AO12():
    # 'Charts_Data_M14'!AO12
    value = 0
    formula = "='Dashboard M14'!AO20"
    @eval_fn
    def AO12():
        ao20_1 = Dashboard_M14.AO20()
        return ao20_1

@register(Charts_Data_M14)
class AP12():
    # 'Charts_Data_M14'!AP12
    value = 0
    formula = "='Dashboard M14'!AP20"
    @eval_fn
    def AP12():
        ap20_1 = Dashboard_M14.AP20()
        return ap20_1

@register(Charts_Data_M14)
class AQ12():
    # 'Charts_Data_M14'!AQ12
    value = 0
    formula = "='Dashboard M14'!AQ20"
    @eval_fn
    def AQ12():
        aq20_1 = Dashboard_M14.AQ20()
        return aq20_1

@register(Charts_Data_M14)
class AR12():
    # 'Charts_Data_M14'!AR12
    value = 0
    formula = "='Dashboard M14'!AR20"
    @eval_fn
    def AR12():
        ar20_1 = Dashboard_M14.AR20()
        return ar20_1

@register(Charts_Data_M14)
class AS12():
    # 'Charts_Data_M14'!AS12
    value = 0
    formula = "='Dashboard M14'!AS20"
    @eval_fn
    def AS12():
        as20_1 = Dashboard_M14.AS20()
        return as20_1

@register(Charts_Data_M14)
class AT12():
    # 'Charts_Data_M14'!AT12
    value = 0
    formula = "='Dashboard M14'!AT20"
    @eval_fn
    def AT12():
        at20_1 = Dashboard_M14.AT20()
        return at20_1

@register(Charts_Data_M14)
class AU12():
    # 'Charts_Data_M14'!AU12
    value = 0
    formula = "='Dashboard M14'!AU20"
    @eval_fn
    def AU12():
        au20_1 = Dashboard_M14.AU20()
        return au20_1

@register(Charts_Data_M14)
class C13():
    # 'Charts_Data_M14'!C13
    value = "Percent of 1990 levels"
    formula = "=B2"
    @eval_fn
    def C13():
        b2_1 = Charts_Data_M14.B2()
        return b2_1

@register(Charts_Data_M14)
class F13():
    # 'Charts_Data_M14'!F13
    value = "Notes"

@register(Charts_Data_M14)
class I13():
    # 'Charts_Data_M14'!I13
    value = 0.478168880071
    formula = "='Dashboard M14'!I21"
    @eval_fn
    def I13():
        i21_1 = Dashboard_M14.I21()
        return i21_1

@register(Charts_Data_M14)
class J13():
    # 'Charts_Data_M14'!J13
    value = -1.73243977094
    formula = "='Dashboard M14'!J21"
    @eval_fn
    def J13():
        j21_1 = Dashboard_M14.J21()
        return j21_1

@register(Charts_Data_M14)
class K13():
    # 'Charts_Data_M14'!K13
    value = 0.464067574375
    formula = "='Dashboard M14'!K21"
    @eval_fn
    def K13():
        k21_1 = Dashboard_M14.K21()
        return k21_1

@register(Charts_Data_M14)
class L13():
    # 'Charts_Data_M14'!L13
    value = -0.0879405911585
    formula = "='Dashboard M14'!L21"
    @eval_fn
    def L13():
        l21_1 = Dashboard_M14.L21()
        return l21_1

@register(Charts_Data_M14)
class M13():
    # 'Charts_Data_M14'!M13
    value = -0.536581642793
    formula = "='Dashboard M14'!M21"
    @eval_fn
    def M13():
        m21_1 = Dashboard_M14.M21()
        return m21_1

@register(Charts_Data_M14)
class N13():
    # 'Charts_Data_M14'!N13
    value = -0.169902011581
    formula = "='Dashboard M14'!N21"
    @eval_fn
    def N13():
        n21_1 = Dashboard_M14.N21()
        return n21_1

@register(Charts_Data_M14)
class O13():
    # 'Charts_Data_M14'!O13
    value = -0.0104927649464
    formula = "='Dashboard M14'!O21"
    @eval_fn
    def O13():
        o21_1 = Dashboard_M14.O21()
        return o21_1

@register(Charts_Data_M14)
class P13():
    # 'Charts_Data_M14'!P13
    value = -0.0935038691775
    formula = "='Dashboard M14'!P21"
    @eval_fn
    def P13():
        p21_1 = Dashboard_M14.P21()
        return p21_1

@register(Charts_Data_M14)
class Q13():
    # 'Charts_Data_M14'!Q13
    value = 0.100043471879
    formula = "='Dashboard M14'!Q21"
    @eval_fn
    def Q13():
        q21_1 = Dashboard_M14.Q21()
        return q21_1

@register(Charts_Data_M14)
class R13():
    # 'Charts_Data_M14'!R13
    value = 0.164543338595
    formula = "='Dashboard M14'!R21"
    @eval_fn
    def R13():
        r21_1 = Dashboard_M14.R21()
        return r21_1

@register(Charts_Data_M14)
class S13():
    # 'Charts_Data_M14'!S13
    value = 0.574514795726
    formula = "='Dashboard M14'!S21"
    @eval_fn
    def S13():
        s21_1 = Dashboard_M14.S21()
        return s21_1

@register(Charts_Data_M14)
class T13():
    # 'Charts_Data_M14'!T13
    value = 1.02700754941
    formula = "='Dashboard M14'!T21"
    @eval_fn
    def T13():
        t21_1 = Dashboard_M14.T21()
        return t21_1

@register(Charts_Data_M14)
class U13():
    # 'Charts_Data_M14'!U13
    value = "#N/A"
    formula = "='Dashboard M14'!U21"
    @eval_fn
    def U13():
        u21_1 = Dashboard_M14.U21()
        return u21_1

@register(Charts_Data_M14)
class V13():
    # 'Charts_Data_M14'!V13
    value = -0.589242538257
    formula = "='Dashboard M14'!V21"
    @eval_fn
    def V13():
        v21_1 = Dashboard_M14.V21()
        return v21_1

@register(Charts_Data_M14)
class W13():
    # 'Charts_Data_M14'!W13
    value = -0.124627309999
    formula = "='Dashboard M14'!W21"
    @eval_fn
    def W13():
        w21_1 = Dashboard_M14.W21()
        return w21_1

@register(Charts_Data_M14)
class X13():
    # 'Charts_Data_M14'!X13
    value = -0.459938177657
    formula = "='Dashboard M14'!X21"
    @eval_fn
    def X13():
        x21_1 = Dashboard_M14.X21()
        return x21_1

@register(Charts_Data_M14)
class Y13():
    # 'Charts_Data_M14'!Y13
    value = 1.75672856394
    formula = "='Dashboard M14'!Y21"
    @eval_fn
    def Y13():
        y21_1 = Dashboard_M14.Y21()
        return y21_1

@register(Charts_Data_M14)
class Z13():
    # 'Charts_Data_M14'!Z13
    value = -0.216493571908
    formula = "='Dashboard M14'!Z21"
    @eval_fn
    def Z13():
        z21_1 = Dashboard_M14.Z21()
        return z21_1

@register(Charts_Data_M14)
class AA13():
    # 'Charts_Data_M14'!AA13
    value = -0.034594216876
    formula = "='Dashboard M14'!AA21"
    @eval_fn
    def AA13():
        aa21_1 = Dashboard_M14.AA21()
        return aa21_1

@register(Charts_Data_M14)
class AB13():
    # 'Charts_Data_M14'!AB13
    value = 0.203787300482
    formula = "='Dashboard M14'!AB21"
    @eval_fn
    def AB13():
        ab21_1 = Dashboard_M14.AB21()
        return ab21_1

@register(Charts_Data_M14)
class AC13():
    # 'Charts_Data_M14'!AC13
    value = -9.4631840875
    formula = "='Dashboard M14'!AC21"
    @eval_fn
    def AC13():
        ac21_1 = Dashboard_M14.AC21()
        return ac21_1

@register(Charts_Data_M14)
class AD13():
    # 'Charts_Data_M14'!AD13
    value = 0
    formula = "='Dashboard M14'!AD21"
    @eval_fn
    def AD13():
        ad21_1 = Dashboard_M14.AD21()
        return ad21_1

@register(Charts_Data_M14)
class AE13():
    # 'Charts_Data_M14'!AE13
    value = 0
    formula = "='Dashboard M14'!AE21"
    @eval_fn
    def AE13():
        ae21_1 = Dashboard_M14.AE21()
        return ae21_1

@register(Charts_Data_M14)
class AF13():
    # 'Charts_Data_M14'!AF13
    value = 0
    formula = "='Dashboard M14'!AF21"
    @eval_fn
    def AF13():
        af21_1 = Dashboard_M14.AF21()
        return af21_1

@register(Charts_Data_M14)
class AG13():
    # 'Charts_Data_M14'!AG13
    value = 0
    formula = "='Dashboard M14'!AG21"
    @eval_fn
    def AG13():
        ag21_1 = Dashboard_M14.AG21()
        return ag21_1

@register(Charts_Data_M14)
class AH13():
    # 'Charts_Data_M14'!AH13
    value = 0
    formula = "='Dashboard M14'!AH21"
    @eval_fn
    def AH13():
        ah21_1 = Dashboard_M14.AH21()
        return ah21_1

@register(Charts_Data_M14)
class AI13():
    # 'Charts_Data_M14'!AI13
    value = 0
    formula = "='Dashboard M14'!AI21"
    @eval_fn
    def AI13():
        ai21_1 = Dashboard_M14.AI21()
        return ai21_1

@register(Charts_Data_M14)
class AJ13():
    # 'Charts_Data_M14'!AJ13
    value = 0
    formula = "='Dashboard M14'!AJ21"
    @eval_fn
    def AJ13():
        aj21_1 = Dashboard_M14.AJ21()
        return aj21_1

@register(Charts_Data_M14)
class AK13():
    # 'Charts_Data_M14'!AK13
    value = 0
    formula = "='Dashboard M14'!AK21"
    @eval_fn
    def AK13():
        ak21_1 = Dashboard_M14.AK21()
        return ak21_1

@register(Charts_Data_M14)
class AL13():
    # 'Charts_Data_M14'!AL13
    value = 0
    formula = "='Dashboard M14'!AL21"
    @eval_fn
    def AL13():
        al21_1 = Dashboard_M14.AL21()
        return al21_1

@register(Charts_Data_M14)
class AM13():
    # 'Charts_Data_M14'!AM13
    value = 0
    formula = "='Dashboard M14'!AM21"
    @eval_fn
    def AM13():
        am21_1 = Dashboard_M14.AM21()
        return am21_1

@register(Charts_Data_M14)
class AN13():
    # 'Charts_Data_M14'!AN13
    value = 0
    formula = "='Dashboard M14'!AN21"
    @eval_fn
    def AN13():
        an21_1 = Dashboard_M14.AN21()
        return an21_1

@register(Charts_Data_M14)
class AO13():
    # 'Charts_Data_M14'!AO13
    value = 0
    formula = "='Dashboard M14'!AO21"
    @eval_fn
    def AO13():
        ao21_1 = Dashboard_M14.AO21()
        return ao21_1

@register(Charts_Data_M14)
class AP13():
    # 'Charts_Data_M14'!AP13
    value = 0
    formula = "='Dashboard M14'!AP21"
    @eval_fn
    def AP13():
        ap21_1 = Dashboard_M14.AP21()
        return ap21_1

@register(Charts_Data_M14)
class AQ13():
    # 'Charts_Data_M14'!AQ13
    value = 0
    formula = "='Dashboard M14'!AQ21"
    @eval_fn
    def AQ13():
        aq21_1 = Dashboard_M14.AQ21()
        return aq21_1

@register(Charts_Data_M14)
class AR13():
    # 'Charts_Data_M14'!AR13
    value = 0
    formula = "='Dashboard M14'!AR21"
    @eval_fn
    def AR13():
        ar21_1 = Dashboard_M14.AR21()
        return ar21_1

@register(Charts_Data_M14)
class AS13():
    # 'Charts_Data_M14'!AS13
    value = 0
    formula = "='Dashboard M14'!AS21"
    @eval_fn
    def AS13():
        as21_1 = Dashboard_M14.AS21()
        return as21_1

@register(Charts_Data_M14)
class AT13():
    # 'Charts_Data_M14'!AT13
    value = 0
    formula = "='Dashboard M14'!AT21"
    @eval_fn
    def AT13():
        at21_1 = Dashboard_M14.AT21()
        return at21_1

@register(Charts_Data_M14)
class AU13():
    # 'Charts_Data_M14'!AU13
    value = 0
    formula = "='Dashboard M14'!AU21"
    @eval_fn
    def AU13():
        au21_1 = Dashboard_M14.AU21()
        return au21_1