# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_Data_M12_Local_Fuel = Worksheet('Charts_Data_M12_Local_Fuel', 10, 10)



@register(Charts_Data_M12_Local_Fuel)
class A1():
    # 'Charts_Data_M12_Local_Fuel'!A1
    value = "Metric 12: Local Fuel"

@register(Charts_Data_M12_Local_Fuel)
class D1():
    # 'Charts_Data_M12_Local_Fuel'!D1
    value = "Units"

@register(Charts_Data_M12_Local_Fuel)
class E1():
    # 'Charts_Data_M12_Local_Fuel'!E1
    value = "Source"

@register(Charts_Data_M12_Local_Fuel)
class F1():
    # 'Charts_Data_M12_Local_Fuel'!F1
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G1():
    # 'Charts_Data_M12_Local_Fuel'!G1
    value = 1999

@register(Charts_Data_M12_Local_Fuel)
class H1():
    # 'Charts_Data_M12_Local_Fuel'!H1
    value = 2000

@register(Charts_Data_M12_Local_Fuel)
class I1():
    # 'Charts_Data_M12_Local_Fuel'!I1
    value = 2001

@register(Charts_Data_M12_Local_Fuel)
class J1():
    # 'Charts_Data_M12_Local_Fuel'!J1
    value = 2002

@register(Charts_Data_M12_Local_Fuel)
class K1():
    # 'Charts_Data_M12_Local_Fuel'!K1
    value = 2003

@register(Charts_Data_M12_Local_Fuel)
class L1():
    # 'Charts_Data_M12_Local_Fuel'!L1
    value = 2004

@register(Charts_Data_M12_Local_Fuel)
class M1():
    # 'Charts_Data_M12_Local_Fuel'!M1
    value = 2005

@register(Charts_Data_M12_Local_Fuel)
class N1():
    # 'Charts_Data_M12_Local_Fuel'!N1
    value = 2006

@register(Charts_Data_M12_Local_Fuel)
class O1():
    # 'Charts_Data_M12_Local_Fuel'!O1
    value = 2007

@register(Charts_Data_M12_Local_Fuel)
class P1():
    # 'Charts_Data_M12_Local_Fuel'!P1
    value = 2008

@register(Charts_Data_M12_Local_Fuel)
class Q1():
    # 'Charts_Data_M12_Local_Fuel'!Q1
    value = 2009

@register(Charts_Data_M12_Local_Fuel)
class R1():
    # 'Charts_Data_M12_Local_Fuel'!R1
    value = 2010

@register(Charts_Data_M12_Local_Fuel)
class S1():
    # 'Charts_Data_M12_Local_Fuel'!S1
    value = 2011

@register(Charts_Data_M12_Local_Fuel)
class T1():
    # 'Charts_Data_M12_Local_Fuel'!T1
    value = 2012

@register(Charts_Data_M12_Local_Fuel)
class U1():
    # 'Charts_Data_M12_Local_Fuel'!U1
    value = 2013

@register(Charts_Data_M12_Local_Fuel)
class V1():
    # 'Charts_Data_M12_Local_Fuel'!V1
    value = 2014

@register(Charts_Data_M12_Local_Fuel)
class W1():
    # 'Charts_Data_M12_Local_Fuel'!W1
    value = 2015

@register(Charts_Data_M12_Local_Fuel)
class X1():
    # 'Charts_Data_M12_Local_Fuel'!X1
    value = 2016

@register(Charts_Data_M12_Local_Fuel)
class Y1():
    # 'Charts_Data_M12_Local_Fuel'!Y1
    value = 2017

@register(Charts_Data_M12_Local_Fuel)
class Z1():
    # 'Charts_Data_M12_Local_Fuel'!Z1
    value = 2018

@register(Charts_Data_M12_Local_Fuel)
class AA1():
    # 'Charts_Data_M12_Local_Fuel'!AA1
    value = 2019

@register(Charts_Data_M12_Local_Fuel)
class AB1():
    # 'Charts_Data_M12_Local_Fuel'!AB1
    value = 2020

@register(Charts_Data_M12_Local_Fuel)
class AC1():
    # 'Charts_Data_M12_Local_Fuel'!AC1
    value = 2021

@register(Charts_Data_M12_Local_Fuel)
class AD1():
    # 'Charts_Data_M12_Local_Fuel'!AD1
    value = 2022

@register(Charts_Data_M12_Local_Fuel)
class AE1():
    # 'Charts_Data_M12_Local_Fuel'!AE1
    value = 2023

@register(Charts_Data_M12_Local_Fuel)
class AF1():
    # 'Charts_Data_M12_Local_Fuel'!AF1
    value = 2024

@register(Charts_Data_M12_Local_Fuel)
class AG1():
    # 'Charts_Data_M12_Local_Fuel'!AG1
    value = 2025

@register(Charts_Data_M12_Local_Fuel)
class AH1():
    # 'Charts_Data_M12_Local_Fuel'!AH1
    value = 2026

@register(Charts_Data_M12_Local_Fuel)
class AI1():
    # 'Charts_Data_M12_Local_Fuel'!AI1
    value = 2027

@register(Charts_Data_M12_Local_Fuel)
class AJ1():
    # 'Charts_Data_M12_Local_Fuel'!AJ1
    value = 2028

@register(Charts_Data_M12_Local_Fuel)
class AK1():
    # 'Charts_Data_M12_Local_Fuel'!AK1
    value = 2029

@register(Charts_Data_M12_Local_Fuel)
class AL1():
    # 'Charts_Data_M12_Local_Fuel'!AL1
    value = 2030

@register(Charts_Data_M12_Local_Fuel)
class A2():
    # 'Charts_Data_M12_Local_Fuel'!A2
    value = "Line Graph Input 1"

@register(Charts_Data_M12_Local_Fuel)
class D2():
    # 'Charts_Data_M12_Local_Fuel'!D2
    value = "Hydro"

@register(Charts_Data_M12_Local_Fuel)
class F2():
    # 'Charts_Data_M12_Local_Fuel'!F2
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G2():
    # 'Charts_Data_M12_Local_Fuel'!G2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!G20,NA())"
    @eval_fn
    def G2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        g20_1 = Dashboard_M12_Local_Fuel.G20()
        var_1 = NA()
        var_2 = IF(c21_1, g20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H2():
    # 'Charts_Data_M12_Local_Fuel'!H2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!H20,NA())"
    @eval_fn
    def H2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        h20_1 = Dashboard_M12_Local_Fuel.H20()
        var_1 = NA()
        var_2 = IF(c21_1, h20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I2():
    # 'Charts_Data_M12_Local_Fuel'!I2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!I20,NA())"
    @eval_fn
    def I2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        i20_1 = Dashboard_M12_Local_Fuel.I20()
        var_1 = NA()
        var_2 = IF(c21_1, i20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J2():
    # 'Charts_Data_M12_Local_Fuel'!J2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!J20,NA())"
    @eval_fn
    def J2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        j20_1 = Dashboard_M12_Local_Fuel.J20()
        var_1 = NA()
        var_2 = IF(c21_1, j20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K2():
    # 'Charts_Data_M12_Local_Fuel'!K2
    value = 25490
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!K20,NA())"
    @eval_fn
    def K2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        k20_1 = Dashboard_M12_Local_Fuel.K20()
        var_1 = NA()
        var_2 = IF(c21_1, k20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L2():
    # 'Charts_Data_M12_Local_Fuel'!L2
    value = 12001
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!L20,NA())"
    @eval_fn
    def L2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        l20_1 = Dashboard_M12_Local_Fuel.L20()
        var_1 = NA()
        var_2 = IF(c21_1, l20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M2():
    # 'Charts_Data_M12_Local_Fuel'!M2
    value = 115000
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!M20,NA())"
    @eval_fn
    def M2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        m20_1 = Dashboard_M12_Local_Fuel.M20()
        var_1 = NA()
        var_2 = IF(c21_1, m20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N2():
    # 'Charts_Data_M12_Local_Fuel'!N2
    value = 19628
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!N20,NA())"
    @eval_fn
    def N2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        n20_1 = Dashboard_M12_Local_Fuel.N20()
        var_1 = NA()
        var_2 = IF(c21_1, n20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O2():
    # 'Charts_Data_M12_Local_Fuel'!O2
    value = -34357
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!O20,NA())"
    @eval_fn
    def O2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        o20_1 = Dashboard_M12_Local_Fuel.O20()
        var_1 = NA()
        var_2 = IF(c21_1, o20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P2():
    # 'Charts_Data_M12_Local_Fuel'!P2
    value = -60191
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!P20,NA())"
    @eval_fn
    def P2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        p20_1 = Dashboard_M12_Local_Fuel.P20()
        var_1 = NA()
        var_2 = IF(c21_1, p20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q2():
    # 'Charts_Data_M12_Local_Fuel'!Q2
    value = 29257
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!Q20,NA())"
    @eval_fn
    def Q2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        q20_1 = Dashboard_M12_Local_Fuel.Q20()
        var_1 = NA()
        var_2 = IF(c21_1, q20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R2():
    # 'Charts_Data_M12_Local_Fuel'!R2
    value = -36733
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!R20,NA())"
    @eval_fn
    def R2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        r20_1 = Dashboard_M12_Local_Fuel.R20()
        var_1 = NA()
        var_2 = IF(c21_1, r20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S2():
    # 'Charts_Data_M12_Local_Fuel'!S2
    value = 20328
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!S20,NA())"
    @eval_fn
    def S2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        s20_1 = Dashboard_M12_Local_Fuel.S20()
        var_1 = NA()
        var_2 = IF(c21_1, s20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T2():
    # 'Charts_Data_M12_Local_Fuel'!T2
    value = 13555
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!T20,NA())"
    @eval_fn
    def T2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        t20_1 = Dashboard_M12_Local_Fuel.T20()
        var_1 = NA()
        var_2 = IF(c21_1, t20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U2():
    # 'Charts_Data_M12_Local_Fuel'!U2
    value = -30472
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!U20,NA())"
    @eval_fn
    def U2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        u20_1 = Dashboard_M12_Local_Fuel.U20()
        var_1 = NA()
        var_2 = IF(c21_1, u20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V2():
    # 'Charts_Data_M12_Local_Fuel'!V2
    value = 11940
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!V20,NA())"
    @eval_fn
    def V2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        v20_1 = Dashboard_M12_Local_Fuel.V20()
        var_1 = NA()
        var_2 = IF(c21_1, v20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W2():
    # 'Charts_Data_M12_Local_Fuel'!W2
    value = 21288
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!W20,NA())"
    @eval_fn
    def W2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        w20_1 = Dashboard_M12_Local_Fuel.W20()
        var_1 = NA()
        var_2 = IF(c21_1, w20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X2():
    # 'Charts_Data_M12_Local_Fuel'!X2
    value = -106734
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!X20,NA())"
    @eval_fn
    def X2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        x20_1 = Dashboard_M12_Local_Fuel.X20()
        var_1 = NA()
        var_2 = IF(c21_1, x20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y2():
    # 'Charts_Data_M12_Local_Fuel'!Y2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!Y20,NA())"
    @eval_fn
    def Y2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        y20_1 = Dashboard_M12_Local_Fuel.Y20()
        var_1 = NA()
        var_2 = IF(c21_1, y20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z2():
    # 'Charts_Data_M12_Local_Fuel'!Z2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!Z20,NA())"
    @eval_fn
    def Z2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        z20_1 = Dashboard_M12_Local_Fuel.Z20()
        var_1 = NA()
        var_2 = IF(c21_1, z20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA2():
    # 'Charts_Data_M12_Local_Fuel'!AA2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AA20,NA())"
    @eval_fn
    def AA2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        aa20_1 = Dashboard_M12_Local_Fuel.AA20()
        var_1 = NA()
        var_2 = IF(c21_1, aa20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB2():
    # 'Charts_Data_M12_Local_Fuel'!AB2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AB20,NA())"
    @eval_fn
    def AB2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        ab20_1 = Dashboard_M12_Local_Fuel.AB20()
        var_1 = NA()
        var_2 = IF(c21_1, ab20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC2():
    # 'Charts_Data_M12_Local_Fuel'!AC2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AC20,NA())"
    @eval_fn
    def AC2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        ac20_1 = Dashboard_M12_Local_Fuel.AC20()
        var_1 = NA()
        var_2 = IF(c21_1, ac20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD2():
    # 'Charts_Data_M12_Local_Fuel'!AD2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AD20,NA())"
    @eval_fn
    def AD2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        ad20_1 = Dashboard_M12_Local_Fuel.AD20()
        var_1 = NA()
        var_2 = IF(c21_1, ad20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE2():
    # 'Charts_Data_M12_Local_Fuel'!AE2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AE20,NA())"
    @eval_fn
    def AE2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        ae20_1 = Dashboard_M12_Local_Fuel.AE20()
        var_1 = NA()
        var_2 = IF(c21_1, ae20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF2():
    # 'Charts_Data_M12_Local_Fuel'!AF2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AF20,NA())"
    @eval_fn
    def AF2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        af20_1 = Dashboard_M12_Local_Fuel.AF20()
        var_1 = NA()
        var_2 = IF(c21_1, af20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG2():
    # 'Charts_Data_M12_Local_Fuel'!AG2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AG20,NA())"
    @eval_fn
    def AG2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        ag20_1 = Dashboard_M12_Local_Fuel.AG20()
        var_1 = NA()
        var_2 = IF(c21_1, ag20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH2():
    # 'Charts_Data_M12_Local_Fuel'!AH2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AH20,NA())"
    @eval_fn
    def AH2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        ah20_1 = Dashboard_M12_Local_Fuel.AH20()
        var_1 = NA()
        var_2 = IF(c21_1, ah20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI2():
    # 'Charts_Data_M12_Local_Fuel'!AI2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AI20,NA())"
    @eval_fn
    def AI2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        ai20_1 = Dashboard_M12_Local_Fuel.AI20()
        var_1 = NA()
        var_2 = IF(c21_1, ai20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ2():
    # 'Charts_Data_M12_Local_Fuel'!AJ2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AJ20,NA())"
    @eval_fn
    def AJ2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        aj20_1 = Dashboard_M12_Local_Fuel.AJ20()
        var_1 = NA()
        var_2 = IF(c21_1, aj20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK2():
    # 'Charts_Data_M12_Local_Fuel'!AK2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AK20,NA())"
    @eval_fn
    def AK2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        ak20_1 = Dashboard_M12_Local_Fuel.AK20()
        var_1 = NA()
        var_2 = IF(c21_1, ak20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL2():
    # 'Charts_Data_M12_Local_Fuel'!AL2
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$C$21,'Dashboard M12 Local Fuel'!AL20,NA())"
    @eval_fn
    def AL2():
        c21_1 = Charts_M12_Local_Fuel.C21()
        al20_1 = Dashboard_M12_Local_Fuel.AL20()
        var_1 = NA()
        var_2 = IF(c21_1, al20_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D3():
    # 'Charts_Data_M12_Local_Fuel'!D3
    value = "Geothermal"

@register(Charts_Data_M12_Local_Fuel)
class F3():
    # 'Charts_Data_M12_Local_Fuel'!F3
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G3():
    # 'Charts_Data_M12_Local_Fuel'!G3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!G21,NA())"
    @eval_fn
    def G3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        g21_1 = Dashboard_M12_Local_Fuel.G21()
        var_1 = NA()
        var_2 = IF(d21_1, g21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H3():
    # 'Charts_Data_M12_Local_Fuel'!H3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!H21,NA())"
    @eval_fn
    def H3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        h21_1 = Dashboard_M12_Local_Fuel.H21()
        var_1 = NA()
        var_2 = IF(d21_1, h21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I3():
    # 'Charts_Data_M12_Local_Fuel'!I3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!I21,NA())"
    @eval_fn
    def I3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        i21_1 = Dashboard_M12_Local_Fuel.I21()
        var_1 = NA()
        var_2 = IF(d21_1, i21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J3():
    # 'Charts_Data_M12_Local_Fuel'!J3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!J21,NA())"
    @eval_fn
    def J3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        j21_1 = Dashboard_M12_Local_Fuel.J21()
        var_1 = NA()
        var_2 = IF(d21_1, j21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K3():
    # 'Charts_Data_M12_Local_Fuel'!K3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!K21,NA())"
    @eval_fn
    def K3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        k21_1 = Dashboard_M12_Local_Fuel.K21()
        var_1 = NA()
        var_2 = IF(d21_1, k21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L3():
    # 'Charts_Data_M12_Local_Fuel'!L3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!L21,NA())"
    @eval_fn
    def L3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        l21_1 = Dashboard_M12_Local_Fuel.L21()
        var_1 = NA()
        var_2 = IF(d21_1, l21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M3():
    # 'Charts_Data_M12_Local_Fuel'!M3
    value = 221000
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!M21,NA())"
    @eval_fn
    def M3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        m21_1 = Dashboard_M12_Local_Fuel.M21()
        var_1 = NA()
        var_2 = IF(d21_1, m21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N3():
    # 'Charts_Data_M12_Local_Fuel'!N3
    value = -9000
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!N21,NA())"
    @eval_fn
    def N3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        n21_1 = Dashboard_M12_Local_Fuel.N21()
        var_1 = NA()
        var_2 = IF(d21_1, n21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O3():
    # 'Charts_Data_M12_Local_Fuel'!O3
    value = 18000
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!O21,NA())"
    @eval_fn
    def O3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        o21_1 = Dashboard_M12_Local_Fuel.O21()
        var_1 = NA()
        var_2 = IF(d21_1, o21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P3():
    # 'Charts_Data_M12_Local_Fuel'!P3
    value = 4334
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!P21,NA())"
    @eval_fn
    def P3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        p21_1 = Dashboard_M12_Local_Fuel.P21()
        var_1 = NA()
        var_2 = IF(d21_1, p21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q3():
    # 'Charts_Data_M12_Local_Fuel'!Q3
    value = -66743
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!Q21,NA())"
    @eval_fn
    def Q3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        q21_1 = Dashboard_M12_Local_Fuel.Q21()
        var_1 = NA()
        var_2 = IF(d21_1, q21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R3():
    # 'Charts_Data_M12_Local_Fuel'!R3
    value = 33996
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!R21,NA())"
    @eval_fn
    def R3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        r21_1 = Dashboard_M12_Local_Fuel.R21()
        var_1 = NA()
        var_2 = IF(d21_1, r21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S3():
    # 'Charts_Data_M12_Local_Fuel'!S3
    value = 31319
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!S21,NA())"
    @eval_fn
    def S3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        s21_1 = Dashboard_M12_Local_Fuel.S21()
        var_1 = NA()
        var_2 = IF(d21_1, s21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T3():
    # 'Charts_Data_M12_Local_Fuel'!T3
    value = 33328
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!T21,NA())"
    @eval_fn
    def T3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        t21_1 = Dashboard_M12_Local_Fuel.T21()
        var_1 = NA()
        var_2 = IF(d21_1, t21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U3():
    # 'Charts_Data_M12_Local_Fuel'!U3
    value = 15183
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!U21,NA())"
    @eval_fn
    def U3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        u21_1 = Dashboard_M12_Local_Fuel.U21()
        var_1 = NA()
        var_2 = IF(d21_1, u21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V3():
    # 'Charts_Data_M12_Local_Fuel'!V3
    value = -26390
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!V21,NA())"
    @eval_fn
    def V3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        v21_1 = Dashboard_M12_Local_Fuel.V21()
        var_1 = NA()
        var_2 = IF(d21_1, v21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W3():
    # 'Charts_Data_M12_Local_Fuel'!W3
    value = -24532
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!W21,NA())"
    @eval_fn
    def W3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        w21_1 = Dashboard_M12_Local_Fuel.W21()
        var_1 = NA()
        var_2 = IF(d21_1, w21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X3():
    # 'Charts_Data_M12_Local_Fuel'!X3
    value = -230495
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!X21,NA())"
    @eval_fn
    def X3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        x21_1 = Dashboard_M12_Local_Fuel.X21()
        var_1 = NA()
        var_2 = IF(d21_1, x21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y3():
    # 'Charts_Data_M12_Local_Fuel'!Y3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!Y21,NA())"
    @eval_fn
    def Y3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        y21_1 = Dashboard_M12_Local_Fuel.Y21()
        var_1 = NA()
        var_2 = IF(d21_1, y21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z3():
    # 'Charts_Data_M12_Local_Fuel'!Z3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!Z21,NA())"
    @eval_fn
    def Z3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        z21_1 = Dashboard_M12_Local_Fuel.Z21()
        var_1 = NA()
        var_2 = IF(d21_1, z21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA3():
    # 'Charts_Data_M12_Local_Fuel'!AA3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AA21,NA())"
    @eval_fn
    def AA3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        aa21_1 = Dashboard_M12_Local_Fuel.AA21()
        var_1 = NA()
        var_2 = IF(d21_1, aa21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB3():
    # 'Charts_Data_M12_Local_Fuel'!AB3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AB21,NA())"
    @eval_fn
    def AB3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        ab21_1 = Dashboard_M12_Local_Fuel.AB21()
        var_1 = NA()
        var_2 = IF(d21_1, ab21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC3():
    # 'Charts_Data_M12_Local_Fuel'!AC3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AC21,NA())"
    @eval_fn
    def AC3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        ac21_1 = Dashboard_M12_Local_Fuel.AC21()
        var_1 = NA()
        var_2 = IF(d21_1, ac21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD3():
    # 'Charts_Data_M12_Local_Fuel'!AD3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AD21,NA())"
    @eval_fn
    def AD3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        ad21_1 = Dashboard_M12_Local_Fuel.AD21()
        var_1 = NA()
        var_2 = IF(d21_1, ad21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE3():
    # 'Charts_Data_M12_Local_Fuel'!AE3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AE21,NA())"
    @eval_fn
    def AE3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        ae21_1 = Dashboard_M12_Local_Fuel.AE21()
        var_1 = NA()
        var_2 = IF(d21_1, ae21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF3():
    # 'Charts_Data_M12_Local_Fuel'!AF3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AF21,NA())"
    @eval_fn
    def AF3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        af21_1 = Dashboard_M12_Local_Fuel.AF21()
        var_1 = NA()
        var_2 = IF(d21_1, af21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG3():
    # 'Charts_Data_M12_Local_Fuel'!AG3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AG21,NA())"
    @eval_fn
    def AG3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        ag21_1 = Dashboard_M12_Local_Fuel.AG21()
        var_1 = NA()
        var_2 = IF(d21_1, ag21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH3():
    # 'Charts_Data_M12_Local_Fuel'!AH3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AH21,NA())"
    @eval_fn
    def AH3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        ah21_1 = Dashboard_M12_Local_Fuel.AH21()
        var_1 = NA()
        var_2 = IF(d21_1, ah21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI3():
    # 'Charts_Data_M12_Local_Fuel'!AI3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AI21,NA())"
    @eval_fn
    def AI3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        ai21_1 = Dashboard_M12_Local_Fuel.AI21()
        var_1 = NA()
        var_2 = IF(d21_1, ai21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ3():
    # 'Charts_Data_M12_Local_Fuel'!AJ3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AJ21,NA())"
    @eval_fn
    def AJ3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        aj21_1 = Dashboard_M12_Local_Fuel.AJ21()
        var_1 = NA()
        var_2 = IF(d21_1, aj21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK3():
    # 'Charts_Data_M12_Local_Fuel'!AK3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AK21,NA())"
    @eval_fn
    def AK3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        ak21_1 = Dashboard_M12_Local_Fuel.AK21()
        var_1 = NA()
        var_2 = IF(d21_1, ak21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL3():
    # 'Charts_Data_M12_Local_Fuel'!AL3
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$D$21,'Dashboard M12 Local Fuel'!AL21,NA())"
    @eval_fn
    def AL3():
        d21_1 = Charts_M12_Local_Fuel.D21()
        al21_1 = Dashboard_M12_Local_Fuel.AL21()
        var_1 = NA()
        var_2 = IF(d21_1, al21_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D4():
    # 'Charts_Data_M12_Local_Fuel'!D4
    value = "Wind "

@register(Charts_Data_M12_Local_Fuel)
class F4():
    # 'Charts_Data_M12_Local_Fuel'!F4
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G4():
    # 'Charts_Data_M12_Local_Fuel'!G4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!G22,NA())"
    @eval_fn
    def G4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        g22_1 = Dashboard_M12_Local_Fuel.G22()
        var_1 = NA()
        var_2 = IF(e21_1, g22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H4():
    # 'Charts_Data_M12_Local_Fuel'!H4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!H22,NA())"
    @eval_fn
    def H4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        h22_1 = Dashboard_M12_Local_Fuel.H22()
        var_1 = NA()
        var_2 = IF(e21_1, h22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I4():
    # 'Charts_Data_M12_Local_Fuel'!I4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!I22,NA())"
    @eval_fn
    def I4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        i22_1 = Dashboard_M12_Local_Fuel.I22()
        var_1 = NA()
        var_2 = IF(e21_1, i22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J4():
    # 'Charts_Data_M12_Local_Fuel'!J4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!J22,NA())"
    @eval_fn
    def J4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        j22_1 = Dashboard_M12_Local_Fuel.J22()
        var_1 = NA()
        var_2 = IF(e21_1, j22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K4():
    # 'Charts_Data_M12_Local_Fuel'!K4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!K22,NA())"
    @eval_fn
    def K4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        k22_1 = Dashboard_M12_Local_Fuel.K22()
        var_1 = NA()
        var_2 = IF(e21_1, k22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L4():
    # 'Charts_Data_M12_Local_Fuel'!L4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!L22,NA())"
    @eval_fn
    def L4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        l22_1 = Dashboard_M12_Local_Fuel.L22()
        var_1 = NA()
        var_2 = IF(e21_1, l22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M4():
    # 'Charts_Data_M12_Local_Fuel'!M4
    value = 7000
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!M22,NA())"
    @eval_fn
    def M4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        m22_1 = Dashboard_M12_Local_Fuel.M22()
        var_1 = NA()
        var_2 = IF(e21_1, m22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N4():
    # 'Charts_Data_M12_Local_Fuel'!N4
    value = 75000
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!N22,NA())"
    @eval_fn
    def N4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        n22_1 = Dashboard_M12_Local_Fuel.N22()
        var_1 = NA()
        var_2 = IF(e21_1, n22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O4():
    # 'Charts_Data_M12_Local_Fuel'!O4
    value = 160400
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!O22,NA())"
    @eval_fn
    def O4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        o22_1 = Dashboard_M12_Local_Fuel.O22()
        var_1 = NA()
        var_2 = IF(e21_1, o22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P4():
    # 'Charts_Data_M12_Local_Fuel'!P4
    value = -5107
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!P22,NA())"
    @eval_fn
    def P4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        p22_1 = Dashboard_M12_Local_Fuel.P22()
        var_1 = NA()
        var_2 = IF(e21_1, p22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q4():
    # 'Charts_Data_M12_Local_Fuel'!Q4
    value = 13062
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!Q22,NA())"
    @eval_fn
    def Q4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        q22_1 = Dashboard_M12_Local_Fuel.Q22()
        var_1 = NA()
        var_2 = IF(e21_1, q22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R4():
    # 'Charts_Data_M12_Local_Fuel'!R4
    value = 10851
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!R22,NA())"
    @eval_fn
    def R4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        r22_1 = Dashboard_M12_Local_Fuel.R22()
        var_1 = NA()
        var_2 = IF(e21_1, r22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S4():
    # 'Charts_Data_M12_Local_Fuel'!S4
    value = 83170
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!S22,NA())"
    @eval_fn
    def S4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        s22_1 = Dashboard_M12_Local_Fuel.S22()
        var_1 = NA()
        var_2 = IF(e21_1, s22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T4():
    # 'Charts_Data_M12_Local_Fuel'!T4
    value = 43880
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!T22,NA())"
    @eval_fn
    def T4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        t22_1 = Dashboard_M12_Local_Fuel.T22()
        var_1 = NA()
        var_2 = IF(e21_1, t22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U4():
    # 'Charts_Data_M12_Local_Fuel'!U4
    value = 115292
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!U22,NA())"
    @eval_fn
    def U4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        u22_1 = Dashboard_M12_Local_Fuel.U22()
        var_1 = NA()
        var_2 = IF(e21_1, u22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V4():
    # 'Charts_Data_M12_Local_Fuel'!V4
    value = 74319
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!V22,NA())"
    @eval_fn
    def V4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        v22_1 = Dashboard_M12_Local_Fuel.V22()
        var_1 = NA()
        var_2 = IF(e21_1, v22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W4():
    # 'Charts_Data_M12_Local_Fuel'!W4
    value = 34914
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!W22,NA())"
    @eval_fn
    def W4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        w22_1 = Dashboard_M12_Local_Fuel.W22()
        var_1 = NA()
        var_2 = IF(e21_1, w22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X4():
    # 'Charts_Data_M12_Local_Fuel'!X4
    value = -612781
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!X22,NA())"
    @eval_fn
    def X4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        x22_1 = Dashboard_M12_Local_Fuel.X22()
        var_1 = NA()
        var_2 = IF(e21_1, x22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y4():
    # 'Charts_Data_M12_Local_Fuel'!Y4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!Y22,NA())"
    @eval_fn
    def Y4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        y22_1 = Dashboard_M12_Local_Fuel.Y22()
        var_1 = NA()
        var_2 = IF(e21_1, y22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z4():
    # 'Charts_Data_M12_Local_Fuel'!Z4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!Z22,NA())"
    @eval_fn
    def Z4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        z22_1 = Dashboard_M12_Local_Fuel.Z22()
        var_1 = NA()
        var_2 = IF(e21_1, z22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA4():
    # 'Charts_Data_M12_Local_Fuel'!AA4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AA22,NA())"
    @eval_fn
    def AA4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        aa22_1 = Dashboard_M12_Local_Fuel.AA22()
        var_1 = NA()
        var_2 = IF(e21_1, aa22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB4():
    # 'Charts_Data_M12_Local_Fuel'!AB4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AB22,NA())"
    @eval_fn
    def AB4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        ab22_1 = Dashboard_M12_Local_Fuel.AB22()
        var_1 = NA()
        var_2 = IF(e21_1, ab22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC4():
    # 'Charts_Data_M12_Local_Fuel'!AC4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AC22,NA())"
    @eval_fn
    def AC4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        ac22_1 = Dashboard_M12_Local_Fuel.AC22()
        var_1 = NA()
        var_2 = IF(e21_1, ac22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD4():
    # 'Charts_Data_M12_Local_Fuel'!AD4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AD22,NA())"
    @eval_fn
    def AD4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        ad22_1 = Dashboard_M12_Local_Fuel.AD22()
        var_1 = NA()
        var_2 = IF(e21_1, ad22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE4():
    # 'Charts_Data_M12_Local_Fuel'!AE4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AE22,NA())"
    @eval_fn
    def AE4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        ae22_1 = Dashboard_M12_Local_Fuel.AE22()
        var_1 = NA()
        var_2 = IF(e21_1, ae22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF4():
    # 'Charts_Data_M12_Local_Fuel'!AF4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AF22,NA())"
    @eval_fn
    def AF4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        af22_1 = Dashboard_M12_Local_Fuel.AF22()
        var_1 = NA()
        var_2 = IF(e21_1, af22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG4():
    # 'Charts_Data_M12_Local_Fuel'!AG4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AG22,NA())"
    @eval_fn
    def AG4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        ag22_1 = Dashboard_M12_Local_Fuel.AG22()
        var_1 = NA()
        var_2 = IF(e21_1, ag22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH4():
    # 'Charts_Data_M12_Local_Fuel'!AH4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AH22,NA())"
    @eval_fn
    def AH4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        ah22_1 = Dashboard_M12_Local_Fuel.AH22()
        var_1 = NA()
        var_2 = IF(e21_1, ah22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI4():
    # 'Charts_Data_M12_Local_Fuel'!AI4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AI22,NA())"
    @eval_fn
    def AI4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        ai22_1 = Dashboard_M12_Local_Fuel.AI22()
        var_1 = NA()
        var_2 = IF(e21_1, ai22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ4():
    # 'Charts_Data_M12_Local_Fuel'!AJ4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AJ22,NA())"
    @eval_fn
    def AJ4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        aj22_1 = Dashboard_M12_Local_Fuel.AJ22()
        var_1 = NA()
        var_2 = IF(e21_1, aj22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK4():
    # 'Charts_Data_M12_Local_Fuel'!AK4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AK22,NA())"
    @eval_fn
    def AK4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        ak22_1 = Dashboard_M12_Local_Fuel.AK22()
        var_1 = NA()
        var_2 = IF(e21_1, ak22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL4():
    # 'Charts_Data_M12_Local_Fuel'!AL4
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$E$21,'Dashboard M12 Local Fuel'!AL22,NA())"
    @eval_fn
    def AL4():
        e21_1 = Charts_M12_Local_Fuel.E21()
        al22_1 = Dashboard_M12_Local_Fuel.AL22()
        var_1 = NA()
        var_2 = IF(e21_1, al22_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D5():
    # 'Charts_Data_M12_Local_Fuel'!D5
    value = "Biomass "

@register(Charts_Data_M12_Local_Fuel)
class F5():
    # 'Charts_Data_M12_Local_Fuel'!F5
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G5():
    # 'Charts_Data_M12_Local_Fuel'!G5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!G23,NA())"
    @eval_fn
    def G5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        g23_1 = Dashboard_M12_Local_Fuel.G23()
        var_1 = NA()
        var_2 = IF(f21_1, g23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H5():
    # 'Charts_Data_M12_Local_Fuel'!H5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!H23,NA())"
    @eval_fn
    def H5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        h23_1 = Dashboard_M12_Local_Fuel.H23()
        var_1 = NA()
        var_2 = IF(f21_1, h23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I5():
    # 'Charts_Data_M12_Local_Fuel'!I5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!I23,NA())"
    @eval_fn
    def I5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        i23_1 = Dashboard_M12_Local_Fuel.I23()
        var_1 = NA()
        var_2 = IF(f21_1, i23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J5():
    # 'Charts_Data_M12_Local_Fuel'!J5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!J23,NA())"
    @eval_fn
    def J5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        j23_1 = Dashboard_M12_Local_Fuel.J23()
        var_1 = NA()
        var_2 = IF(f21_1, j23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K5():
    # 'Charts_Data_M12_Local_Fuel'!K5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!K23,NA())"
    @eval_fn
    def K5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        k23_1 = Dashboard_M12_Local_Fuel.K23()
        var_1 = NA()
        var_2 = IF(f21_1, k23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L5():
    # 'Charts_Data_M12_Local_Fuel'!L5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!L23,NA())"
    @eval_fn
    def L5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        l23_1 = Dashboard_M12_Local_Fuel.L23()
        var_1 = NA()
        var_2 = IF(f21_1, l23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M5():
    # 'Charts_Data_M12_Local_Fuel'!M5
    value = 333000
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!M23,NA())"
    @eval_fn
    def M5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        m23_1 = Dashboard_M12_Local_Fuel.M23()
        var_1 = NA()
        var_2 = IF(f21_1, m23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N5():
    # 'Charts_Data_M12_Local_Fuel'!N5
    value = 62000
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!N23,NA())"
    @eval_fn
    def N5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        n23_1 = Dashboard_M12_Local_Fuel.N23()
        var_1 = NA()
        var_2 = IF(f21_1, n23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O5():
    # 'Charts_Data_M12_Local_Fuel'!O5
    value = -69000
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!O23,NA())"
    @eval_fn
    def O5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        o23_1 = Dashboard_M12_Local_Fuel.O23()
        var_1 = NA()
        var_2 = IF(f21_1, o23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P5():
    # 'Charts_Data_M12_Local_Fuel'!P5
    value = 86598
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!P23,NA())"
    @eval_fn
    def P5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        p23_1 = Dashboard_M12_Local_Fuel.P23()
        var_1 = NA()
        var_2 = IF(f21_1, p23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q5():
    # 'Charts_Data_M12_Local_Fuel'!Q5
    value = -13843
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!Q23,NA())"
    @eval_fn
    def Q5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        q23_1 = Dashboard_M12_Local_Fuel.Q23()
        var_1 = NA()
        var_2 = IF(f21_1, q23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R5():
    # 'Charts_Data_M12_Local_Fuel'!R5
    value = -39903
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!R23,NA())"
    @eval_fn
    def R5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        r23_1 = Dashboard_M12_Local_Fuel.R23()
        var_1 = NA()
        var_2 = IF(f21_1, r23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S5():
    # 'Charts_Data_M12_Local_Fuel'!S5
    value = 6414
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!S23,NA())"
    @eval_fn
    def S5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        s23_1 = Dashboard_M12_Local_Fuel.S23()
        var_1 = NA()
        var_2 = IF(f21_1, s23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T5():
    # 'Charts_Data_M12_Local_Fuel'!T5
    value = -23476
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!T23,NA())"
    @eval_fn
    def T5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        t23_1 = Dashboard_M12_Local_Fuel.T23()
        var_1 = NA()
        var_2 = IF(f21_1, t23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U5():
    # 'Charts_Data_M12_Local_Fuel'!U5
    value = 73901
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!U23,NA())"
    @eval_fn
    def U5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        u23_1 = Dashboard_M12_Local_Fuel.U23()
        var_1 = NA()
        var_2 = IF(f21_1, u23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V5():
    # 'Charts_Data_M12_Local_Fuel'!V5
    value = 17473
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!V23,NA())"
    @eval_fn
    def V5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        v23_1 = Dashboard_M12_Local_Fuel.V23()
        var_1 = NA()
        var_2 = IF(f21_1, v23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W5():
    # 'Charts_Data_M12_Local_Fuel'!W5
    value = -16448
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!W23,NA())"
    @eval_fn
    def W5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        w23_1 = Dashboard_M12_Local_Fuel.W23()
        var_1 = NA()
        var_2 = IF(f21_1, w23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X5():
    # 'Charts_Data_M12_Local_Fuel'!X5
    value = -416716
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!X23,NA())"
    @eval_fn
    def X5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        x23_1 = Dashboard_M12_Local_Fuel.X23()
        var_1 = NA()
        var_2 = IF(f21_1, x23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y5():
    # 'Charts_Data_M12_Local_Fuel'!Y5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!Y23,NA())"
    @eval_fn
    def Y5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        y23_1 = Dashboard_M12_Local_Fuel.Y23()
        var_1 = NA()
        var_2 = IF(f21_1, y23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z5():
    # 'Charts_Data_M12_Local_Fuel'!Z5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!Z23,NA())"
    @eval_fn
    def Z5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        z23_1 = Dashboard_M12_Local_Fuel.Z23()
        var_1 = NA()
        var_2 = IF(f21_1, z23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA5():
    # 'Charts_Data_M12_Local_Fuel'!AA5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AA23,NA())"
    @eval_fn
    def AA5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        aa23_1 = Dashboard_M12_Local_Fuel.AA23()
        var_1 = NA()
        var_2 = IF(f21_1, aa23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB5():
    # 'Charts_Data_M12_Local_Fuel'!AB5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AB23,NA())"
    @eval_fn
    def AB5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        ab23_1 = Dashboard_M12_Local_Fuel.AB23()
        var_1 = NA()
        var_2 = IF(f21_1, ab23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC5():
    # 'Charts_Data_M12_Local_Fuel'!AC5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AC23,NA())"
    @eval_fn
    def AC5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        ac23_1 = Dashboard_M12_Local_Fuel.AC23()
        var_1 = NA()
        var_2 = IF(f21_1, ac23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD5():
    # 'Charts_Data_M12_Local_Fuel'!AD5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AD23,NA())"
    @eval_fn
    def AD5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        ad23_1 = Dashboard_M12_Local_Fuel.AD23()
        var_1 = NA()
        var_2 = IF(f21_1, ad23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE5():
    # 'Charts_Data_M12_Local_Fuel'!AE5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AE23,NA())"
    @eval_fn
    def AE5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        ae23_1 = Dashboard_M12_Local_Fuel.AE23()
        var_1 = NA()
        var_2 = IF(f21_1, ae23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF5():
    # 'Charts_Data_M12_Local_Fuel'!AF5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AF23,NA())"
    @eval_fn
    def AF5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        af23_1 = Dashboard_M12_Local_Fuel.AF23()
        var_1 = NA()
        var_2 = IF(f21_1, af23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG5():
    # 'Charts_Data_M12_Local_Fuel'!AG5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AG23,NA())"
    @eval_fn
    def AG5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        ag23_1 = Dashboard_M12_Local_Fuel.AG23()
        var_1 = NA()
        var_2 = IF(f21_1, ag23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH5():
    # 'Charts_Data_M12_Local_Fuel'!AH5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AH23,NA())"
    @eval_fn
    def AH5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        ah23_1 = Dashboard_M12_Local_Fuel.AH23()
        var_1 = NA()
        var_2 = IF(f21_1, ah23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI5():
    # 'Charts_Data_M12_Local_Fuel'!AI5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AI23,NA())"
    @eval_fn
    def AI5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        ai23_1 = Dashboard_M12_Local_Fuel.AI23()
        var_1 = NA()
        var_2 = IF(f21_1, ai23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ5():
    # 'Charts_Data_M12_Local_Fuel'!AJ5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AJ23,NA())"
    @eval_fn
    def AJ5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        aj23_1 = Dashboard_M12_Local_Fuel.AJ23()
        var_1 = NA()
        var_2 = IF(f21_1, aj23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK5():
    # 'Charts_Data_M12_Local_Fuel'!AK5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AK23,NA())"
    @eval_fn
    def AK5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        ak23_1 = Dashboard_M12_Local_Fuel.AK23()
        var_1 = NA()
        var_2 = IF(f21_1, ak23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL5():
    # 'Charts_Data_M12_Local_Fuel'!AL5
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$F$21,'Dashboard M12 Local Fuel'!AL23,NA())"
    @eval_fn
    def AL5():
        f21_1 = Charts_M12_Local_Fuel.F21()
        al23_1 = Dashboard_M12_Local_Fuel.AL23()
        var_1 = NA()
        var_2 = IF(f21_1, al23_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D6():
    # 'Charts_Data_M12_Local_Fuel'!D6
    value = "Solar "

@register(Charts_Data_M12_Local_Fuel)
class F6():
    # 'Charts_Data_M12_Local_Fuel'!F6
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G6():
    # 'Charts_Data_M12_Local_Fuel'!G6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!G24,NA())"
    @eval_fn
    def G6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        g24_1 = Dashboard_M12_Local_Fuel.G24()
        var_1 = NA()
        var_2 = IF(g21_1, g24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H6():
    # 'Charts_Data_M12_Local_Fuel'!H6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!H24,NA())"
    @eval_fn
    def H6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        h24_1 = Dashboard_M12_Local_Fuel.H24()
        var_1 = NA()
        var_2 = IF(g21_1, h24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I6():
    # 'Charts_Data_M12_Local_Fuel'!I6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!I24,NA())"
    @eval_fn
    def I6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        i24_1 = Dashboard_M12_Local_Fuel.I24()
        var_1 = NA()
        var_2 = IF(g21_1, i24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J6():
    # 'Charts_Data_M12_Local_Fuel'!J6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!J24,NA())"
    @eval_fn
    def J6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        j24_1 = Dashboard_M12_Local_Fuel.J24()
        var_1 = NA()
        var_2 = IF(g21_1, j24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K6():
    # 'Charts_Data_M12_Local_Fuel'!K6
    value = 66
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!K24,NA())"
    @eval_fn
    def K6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        k24_1 = Dashboard_M12_Local_Fuel.K24()
        var_1 = NA()
        var_2 = IF(g21_1, k24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L6():
    # 'Charts_Data_M12_Local_Fuel'!L6
    value = 24
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!L24,NA())"
    @eval_fn
    def L6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        l24_1 = Dashboard_M12_Local_Fuel.L24()
        var_1 = NA()
        var_2 = IF(g21_1, l24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M6():
    # 'Charts_Data_M12_Local_Fuel'!M6
    value = -90
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!M24,NA())"
    @eval_fn
    def M6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        m24_1 = Dashboard_M12_Local_Fuel.M24()
        var_1 = NA()
        var_2 = IF(g21_1, m24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N6():
    # 'Charts_Data_M12_Local_Fuel'!N6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!N24,NA())"
    @eval_fn
    def N6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        n24_1 = Dashboard_M12_Local_Fuel.N24()
        var_1 = NA()
        var_2 = IF(g21_1, n24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O6():
    # 'Charts_Data_M12_Local_Fuel'!O6
    value = 7913.58339639
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!O24,NA())"
    @eval_fn
    def O6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        o24_1 = Dashboard_M12_Local_Fuel.O24()
        var_1 = NA()
        var_2 = IF(g21_1, o24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P6():
    # 'Charts_Data_M12_Local_Fuel'!P6
    value = 6350.23260361
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!P24,NA())"
    @eval_fn
    def P6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        p24_1 = Dashboard_M12_Local_Fuel.P24()
        var_1 = NA()
        var_2 = IF(g21_1, p24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q6():
    # 'Charts_Data_M12_Local_Fuel'!Q6
    value = 22147.448
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!Q24,NA())"
    @eval_fn
    def Q6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        q24_1 = Dashboard_M12_Local_Fuel.Q24()
        var_1 = NA()
        var_2 = IF(g21_1, q24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R6():
    # 'Charts_Data_M12_Local_Fuel'!R6
    value = 20106.509
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!R24,NA())"
    @eval_fn
    def R6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        r24_1 = Dashboard_M12_Local_Fuel.R24()
        var_1 = NA()
        var_2 = IF(g21_1, r24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S6():
    # 'Charts_Data_M12_Local_Fuel'!S6
    value = 40509.337
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!S24,NA())"
    @eval_fn
    def S6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        s24_1 = Dashboard_M12_Local_Fuel.S24()
        var_1 = NA()
        var_2 = IF(g21_1, s24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T6():
    # 'Charts_Data_M12_Local_Fuel'!T6
    value = 110382.655
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!T24,NA())"
    @eval_fn
    def T6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        t24_1 = Dashboard_M12_Local_Fuel.T24()
        var_1 = NA()
        var_2 = IF(g21_1, t24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U6():
    # 'Charts_Data_M12_Local_Fuel'!U6
    value = 194708.763253
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!U24,NA())"
    @eval_fn
    def U6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        u24_1 = Dashboard_M12_Local_Fuel.U24()
        var_1 = NA()
        var_2 = IF(g21_1, u24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V6():
    # 'Charts_Data_M12_Local_Fuel'!V6
    value = 191109.415379
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!V24,NA())"
    @eval_fn
    def V6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        v24_1 = Dashboard_M12_Local_Fuel.V24()
        var_1 = NA()
        var_2 = IF(g21_1, v24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W6():
    # 'Charts_Data_M12_Local_Fuel'!W6
    value = 102829.056368
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!W24,NA())"
    @eval_fn
    def W6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        w24_1 = Dashboard_M12_Local_Fuel.W24()
        var_1 = NA()
        var_2 = IF(g21_1, w24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X6():
    # 'Charts_Data_M12_Local_Fuel'!X6
    value = -696057
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!X24,NA())"
    @eval_fn
    def X6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        x24_1 = Dashboard_M12_Local_Fuel.X24()
        var_1 = NA()
        var_2 = IF(g21_1, x24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y6():
    # 'Charts_Data_M12_Local_Fuel'!Y6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!Y24,NA())"
    @eval_fn
    def Y6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        y24_1 = Dashboard_M12_Local_Fuel.Y24()
        var_1 = NA()
        var_2 = IF(g21_1, y24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z6():
    # 'Charts_Data_M12_Local_Fuel'!Z6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!Z24,NA())"
    @eval_fn
    def Z6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        z24_1 = Dashboard_M12_Local_Fuel.Z24()
        var_1 = NA()
        var_2 = IF(g21_1, z24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA6():
    # 'Charts_Data_M12_Local_Fuel'!AA6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AA24,NA())"
    @eval_fn
    def AA6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        aa24_1 = Dashboard_M12_Local_Fuel.AA24()
        var_1 = NA()
        var_2 = IF(g21_1, aa24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB6():
    # 'Charts_Data_M12_Local_Fuel'!AB6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AB24,NA())"
    @eval_fn
    def AB6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        ab24_1 = Dashboard_M12_Local_Fuel.AB24()
        var_1 = NA()
        var_2 = IF(g21_1, ab24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC6():
    # 'Charts_Data_M12_Local_Fuel'!AC6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AC24,NA())"
    @eval_fn
    def AC6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        ac24_1 = Dashboard_M12_Local_Fuel.AC24()
        var_1 = NA()
        var_2 = IF(g21_1, ac24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD6():
    # 'Charts_Data_M12_Local_Fuel'!AD6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AD24,NA())"
    @eval_fn
    def AD6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        ad24_1 = Dashboard_M12_Local_Fuel.AD24()
        var_1 = NA()
        var_2 = IF(g21_1, ad24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE6():
    # 'Charts_Data_M12_Local_Fuel'!AE6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AE24,NA())"
    @eval_fn
    def AE6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        ae24_1 = Dashboard_M12_Local_Fuel.AE24()
        var_1 = NA()
        var_2 = IF(g21_1, ae24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF6():
    # 'Charts_Data_M12_Local_Fuel'!AF6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AF24,NA())"
    @eval_fn
    def AF6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        af24_1 = Dashboard_M12_Local_Fuel.AF24()
        var_1 = NA()
        var_2 = IF(g21_1, af24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG6():
    # 'Charts_Data_M12_Local_Fuel'!AG6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AG24,NA())"
    @eval_fn
    def AG6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        ag24_1 = Dashboard_M12_Local_Fuel.AG24()
        var_1 = NA()
        var_2 = IF(g21_1, ag24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH6():
    # 'Charts_Data_M12_Local_Fuel'!AH6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AH24,NA())"
    @eval_fn
    def AH6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        ah24_1 = Dashboard_M12_Local_Fuel.AH24()
        var_1 = NA()
        var_2 = IF(g21_1, ah24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI6():
    # 'Charts_Data_M12_Local_Fuel'!AI6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AI24,NA())"
    @eval_fn
    def AI6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        ai24_1 = Dashboard_M12_Local_Fuel.AI24()
        var_1 = NA()
        var_2 = IF(g21_1, ai24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ6():
    # 'Charts_Data_M12_Local_Fuel'!AJ6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AJ24,NA())"
    @eval_fn
    def AJ6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        aj24_1 = Dashboard_M12_Local_Fuel.AJ24()
        var_1 = NA()
        var_2 = IF(g21_1, aj24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK6():
    # 'Charts_Data_M12_Local_Fuel'!AK6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AK24,NA())"
    @eval_fn
    def AK6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        ak24_1 = Dashboard_M12_Local_Fuel.AK24()
        var_1 = NA()
        var_2 = IF(g21_1, ak24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL6():
    # 'Charts_Data_M12_Local_Fuel'!AL6
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$G$21,'Dashboard M12 Local Fuel'!AL24,NA())"
    @eval_fn
    def AL6():
        g21_1 = Charts_M12_Local_Fuel.G21()
        al24_1 = Dashboard_M12_Local_Fuel.AL24()
        var_1 = NA()
        var_2 = IF(g21_1, al24_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D7():
    # 'Charts_Data_M12_Local_Fuel'!D7
    value = "Biofuels "

@register(Charts_Data_M12_Local_Fuel)
class F7():
    # 'Charts_Data_M12_Local_Fuel'!F7
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G7():
    # 'Charts_Data_M12_Local_Fuel'!G7
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!G25,NA())"
    @eval_fn
    def G7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        g25_1 = Dashboard_M12_Local_Fuel.G25()
        var_1 = NA()
        var_2 = IF(h21_1, g25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H7():
    # 'Charts_Data_M12_Local_Fuel'!H7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!H25,NA())"
    @eval_fn
    def H7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        h25_1 = Dashboard_M12_Local_Fuel.H25()
        var_1 = NA()
        var_2 = IF(h21_1, h25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I7():
    # 'Charts_Data_M12_Local_Fuel'!I7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!I25,NA())"
    @eval_fn
    def I7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        i25_1 = Dashboard_M12_Local_Fuel.I25()
        var_1 = NA()
        var_2 = IF(h21_1, i25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J7():
    # 'Charts_Data_M12_Local_Fuel'!J7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!J25,NA())"
    @eval_fn
    def J7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        j25_1 = Dashboard_M12_Local_Fuel.J25()
        var_1 = NA()
        var_2 = IF(h21_1, j25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K7():
    # 'Charts_Data_M12_Local_Fuel'!K7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!K25,NA())"
    @eval_fn
    def K7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        k25_1 = Dashboard_M12_Local_Fuel.K25()
        var_1 = NA()
        var_2 = IF(h21_1, k25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L7():
    # 'Charts_Data_M12_Local_Fuel'!L7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!L25,NA())"
    @eval_fn
    def L7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        l25_1 = Dashboard_M12_Local_Fuel.L25()
        var_1 = NA()
        var_2 = IF(h21_1, l25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M7():
    # 'Charts_Data_M12_Local_Fuel'!M7
    value = 252
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!M25,NA())"
    @eval_fn
    def M7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        m25_1 = Dashboard_M12_Local_Fuel.M25()
        var_1 = NA()
        var_2 = IF(h21_1, m25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N7():
    # 'Charts_Data_M12_Local_Fuel'!N7
    value = 14
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!N25,NA())"
    @eval_fn
    def N7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        n25_1 = Dashboard_M12_Local_Fuel.N25()
        var_1 = NA()
        var_2 = IF(h21_1, n25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O7():
    # 'Charts_Data_M12_Local_Fuel'!O7
    value = 1310
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!O25,NA())"
    @eval_fn
    def O7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        o25_1 = Dashboard_M12_Local_Fuel.O25()
        var_1 = NA()
        var_2 = IF(h21_1, o25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P7():
    # 'Charts_Data_M12_Local_Fuel'!P7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!P25,NA())"
    @eval_fn
    def P7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        p25_1 = Dashboard_M12_Local_Fuel.P25()
        var_1 = NA()
        var_2 = IF(h21_1, p25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q7():
    # 'Charts_Data_M12_Local_Fuel'!Q7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!Q25,NA())"
    @eval_fn
    def Q7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        q25_1 = Dashboard_M12_Local_Fuel.Q25()
        var_1 = NA()
        var_2 = IF(h21_1, q25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R7():
    # 'Charts_Data_M12_Local_Fuel'!R7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!R25,NA())"
    @eval_fn
    def R7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        r25_1 = Dashboard_M12_Local_Fuel.R25()
        var_1 = NA()
        var_2 = IF(h21_1, r25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S7():
    # 'Charts_Data_M12_Local_Fuel'!S7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!S25,NA())"
    @eval_fn
    def S7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        s25_1 = Dashboard_M12_Local_Fuel.S25()
        var_1 = NA()
        var_2 = IF(h21_1, s25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T7():
    # 'Charts_Data_M12_Local_Fuel'!T7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!T25,NA())"
    @eval_fn
    def T7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        t25_1 = Dashboard_M12_Local_Fuel.T25()
        var_1 = NA()
        var_2 = IF(h21_1, t25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U7():
    # 'Charts_Data_M12_Local_Fuel'!U7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!U25,NA())"
    @eval_fn
    def U7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        u25_1 = Dashboard_M12_Local_Fuel.U25()
        var_1 = NA()
        var_2 = IF(h21_1, u25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V7():
    # 'Charts_Data_M12_Local_Fuel'!V7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!V25,NA())"
    @eval_fn
    def V7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        v25_1 = Dashboard_M12_Local_Fuel.V25()
        var_1 = NA()
        var_2 = IF(h21_1, v25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W7():
    # 'Charts_Data_M12_Local_Fuel'!W7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!W25,NA())"
    @eval_fn
    def W7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        w25_1 = Dashboard_M12_Local_Fuel.W25()
        var_1 = NA()
        var_2 = IF(h21_1, w25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X7():
    # 'Charts_Data_M12_Local_Fuel'!X7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!X25,NA())"
    @eval_fn
    def X7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        x25_1 = Dashboard_M12_Local_Fuel.X25()
        var_1 = NA()
        var_2 = IF(h21_1, x25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y7():
    # 'Charts_Data_M12_Local_Fuel'!Y7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!Y25,NA())"
    @eval_fn
    def Y7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        y25_1 = Dashboard_M12_Local_Fuel.Y25()
        var_1 = NA()
        var_2 = IF(h21_1, y25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z7():
    # 'Charts_Data_M12_Local_Fuel'!Z7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!Z25,NA())"
    @eval_fn
    def Z7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        z25_1 = Dashboard_M12_Local_Fuel.Z25()
        var_1 = NA()
        var_2 = IF(h21_1, z25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA7():
    # 'Charts_Data_M12_Local_Fuel'!AA7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AA25,NA())"
    @eval_fn
    def AA7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        aa25_1 = Dashboard_M12_Local_Fuel.AA25()
        var_1 = NA()
        var_2 = IF(h21_1, aa25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB7():
    # 'Charts_Data_M12_Local_Fuel'!AB7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AB25,NA())"
    @eval_fn
    def AB7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        ab25_1 = Dashboard_M12_Local_Fuel.AB25()
        var_1 = NA()
        var_2 = IF(h21_1, ab25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC7():
    # 'Charts_Data_M12_Local_Fuel'!AC7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AC25,NA())"
    @eval_fn
    def AC7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        ac25_1 = Dashboard_M12_Local_Fuel.AC25()
        var_1 = NA()
        var_2 = IF(h21_1, ac25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD7():
    # 'Charts_Data_M12_Local_Fuel'!AD7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AD25,NA())"
    @eval_fn
    def AD7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        ad25_1 = Dashboard_M12_Local_Fuel.AD25()
        var_1 = NA()
        var_2 = IF(h21_1, ad25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE7():
    # 'Charts_Data_M12_Local_Fuel'!AE7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AE25,NA())"
    @eval_fn
    def AE7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        ae25_1 = Dashboard_M12_Local_Fuel.AE25()
        var_1 = NA()
        var_2 = IF(h21_1, ae25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF7():
    # 'Charts_Data_M12_Local_Fuel'!AF7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AF25,NA())"
    @eval_fn
    def AF7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        af25_1 = Dashboard_M12_Local_Fuel.AF25()
        var_1 = NA()
        var_2 = IF(h21_1, af25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG7():
    # 'Charts_Data_M12_Local_Fuel'!AG7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AG25,NA())"
    @eval_fn
    def AG7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        ag25_1 = Dashboard_M12_Local_Fuel.AG25()
        var_1 = NA()
        var_2 = IF(h21_1, ag25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH7():
    # 'Charts_Data_M12_Local_Fuel'!AH7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AH25,NA())"
    @eval_fn
    def AH7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        ah25_1 = Dashboard_M12_Local_Fuel.AH25()
        var_1 = NA()
        var_2 = IF(h21_1, ah25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI7():
    # 'Charts_Data_M12_Local_Fuel'!AI7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AI25,NA())"
    @eval_fn
    def AI7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        ai25_1 = Dashboard_M12_Local_Fuel.AI25()
        var_1 = NA()
        var_2 = IF(h21_1, ai25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ7():
    # 'Charts_Data_M12_Local_Fuel'!AJ7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AJ25,NA())"
    @eval_fn
    def AJ7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        aj25_1 = Dashboard_M12_Local_Fuel.AJ25()
        var_1 = NA()
        var_2 = IF(h21_1, aj25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK7():
    # 'Charts_Data_M12_Local_Fuel'!AK7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AK25,NA())"
    @eval_fn
    def AK7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        ak25_1 = Dashboard_M12_Local_Fuel.AK25()
        var_1 = NA()
        var_2 = IF(h21_1, ak25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL7():
    # 'Charts_Data_M12_Local_Fuel'!AL7
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$H$21,'Dashboard M12 Local Fuel'!AL25,NA())"
    @eval_fn
    def AL7():
        h21_1 = Charts_M12_Local_Fuel.H21()
        al25_1 = Dashboard_M12_Local_Fuel.AL25()
        var_1 = NA()
        var_2 = IF(h21_1, al25_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D8():
    # 'Charts_Data_M12_Local_Fuel'!D8
    value = "Total"

@register(Charts_Data_M12_Local_Fuel)
class F8():
    # 'Charts_Data_M12_Local_Fuel'!F8
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G8():
    # 'Charts_Data_M12_Local_Fuel'!G8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!G26,NA())"
    @eval_fn
    def G8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        g26_1 = Dashboard_M12_Local_Fuel.G26()
        var_1 = NA()
        var_2 = IF(b21_1, g26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H8():
    # 'Charts_Data_M12_Local_Fuel'!H8
    value = 39000
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!H26,NA())"
    @eval_fn
    def H8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        h26_1 = Dashboard_M12_Local_Fuel.H26()
        var_1 = NA()
        var_2 = IF(b21_1, h26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I8():
    # 'Charts_Data_M12_Local_Fuel'!I8
    value = -66000
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!I26,NA())"
    @eval_fn
    def I8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        i26_1 = Dashboard_M12_Local_Fuel.I26()
        var_1 = NA()
        var_2 = IF(b21_1, i26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J8():
    # 'Charts_Data_M12_Local_Fuel'!J8
    value = -96000
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!J26,NA())"
    @eval_fn
    def J8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        j26_1 = Dashboard_M12_Local_Fuel.J26()
        var_1 = NA()
        var_2 = IF(b21_1, j26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K8():
    # 'Charts_Data_M12_Local_Fuel'!K8
    value = 157156
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!K26,NA())"
    @eval_fn
    def K8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        k26_1 = Dashboard_M12_Local_Fuel.K26()
        var_1 = NA()
        var_2 = IF(b21_1, k26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L8():
    # 'Charts_Data_M12_Local_Fuel'!L8
    value = 61782
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!L26,NA())"
    @eval_fn
    def L8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        l26_1 = Dashboard_M12_Local_Fuel.L26()
        var_1 = NA()
        var_2 = IF(b21_1, l26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M8():
    # 'Charts_Data_M12_Local_Fuel'!M8
    value = -21406.1209292
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!M26,NA())"
    @eval_fn
    def M8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        m26_1 = Dashboard_M12_Local_Fuel.M26()
        var_1 = NA()
        var_2 = IF(b21_1, m26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N8():
    # 'Charts_Data_M12_Local_Fuel'!N8
    value = 148803.323391
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!N26,NA())"
    @eval_fn
    def N8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        n26_1 = Dashboard_M12_Local_Fuel.N26()
        var_1 = NA()
        var_2 = IF(b21_1, n26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O8():
    # 'Charts_Data_M12_Local_Fuel'!O8
    value = 80573.380935
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!O26,NA())"
    @eval_fn
    def O8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        o26_1 = Dashboard_M12_Local_Fuel.O26()
        var_1 = NA()
        var_2 = IF(b21_1, o26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P8():
    # 'Charts_Data_M12_Local_Fuel'!P8
    value = 31690.2326036
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!P26,NA())"
    @eval_fn
    def P8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        p26_1 = Dashboard_M12_Local_Fuel.P26()
        var_1 = NA()
        var_2 = IF(b21_1, p26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q8():
    # 'Charts_Data_M12_Local_Fuel'!Q8
    value = -12781.552
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!Q26,NA())"
    @eval_fn
    def Q8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        q26_1 = Dashboard_M12_Local_Fuel.Q26()
        var_1 = NA()
        var_2 = IF(b21_1, q26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R8():
    # 'Charts_Data_M12_Local_Fuel'!R8
    value = -13399.491
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!R26,NA())"
    @eval_fn
    def R8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        r26_1 = Dashboard_M12_Local_Fuel.R26()
        var_1 = NA()
        var_2 = IF(b21_1, r26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S8():
    # 'Charts_Data_M12_Local_Fuel'!S8
    value = 237855.337
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!S26,NA())"
    @eval_fn
    def S8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        s26_1 = Dashboard_M12_Local_Fuel.S26()
        var_1 = NA()
        var_2 = IF(b21_1, s26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T8():
    # 'Charts_Data_M12_Local_Fuel'!T8
    value = 141024.655
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!T26,NA())"
    @eval_fn
    def T8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        t26_1 = Dashboard_M12_Local_Fuel.T26()
        var_1 = NA()
        var_2 = IF(b21_1, t26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U8():
    # 'Charts_Data_M12_Local_Fuel'!U8
    value = 388268.763253
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!U26,NA())"
    @eval_fn
    def U8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        u26_1 = Dashboard_M12_Local_Fuel.U26()
        var_1 = NA()
        var_2 = IF(b21_1, u26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V8():
    # 'Charts_Data_M12_Local_Fuel'!V8
    value = 285600.415379
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!V26,NA())"
    @eval_fn
    def V8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        v26_1 = Dashboard_M12_Local_Fuel.V26()
        var_1 = NA()
        var_2 = IF(b21_1, v26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W8():
    # 'Charts_Data_M12_Local_Fuel'!W8
    value = 194619.056368
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!W26,NA())"
    @eval_fn
    def W8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        w26_1 = Dashboard_M12_Local_Fuel.W26()
        var_1 = NA()
        var_2 = IF(b21_1, w26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X8():
    # 'Charts_Data_M12_Local_Fuel'!X8
    value = -2198786
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!X26,NA())"
    @eval_fn
    def X8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        x26_1 = Dashboard_M12_Local_Fuel.X26()
        var_1 = NA()
        var_2 = IF(b21_1, x26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y8():
    # 'Charts_Data_M12_Local_Fuel'!Y8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!Y26,NA())"
    @eval_fn
    def Y8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        y26_1 = Dashboard_M12_Local_Fuel.Y26()
        var_1 = NA()
        var_2 = IF(b21_1, y26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z8():
    # 'Charts_Data_M12_Local_Fuel'!Z8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!Z26,NA())"
    @eval_fn
    def Z8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        z26_1 = Dashboard_M12_Local_Fuel.Z26()
        var_1 = NA()
        var_2 = IF(b21_1, z26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA8():
    # 'Charts_Data_M12_Local_Fuel'!AA8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AA26,NA())"
    @eval_fn
    def AA8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        aa26_1 = Dashboard_M12_Local_Fuel.AA26()
        var_1 = NA()
        var_2 = IF(b21_1, aa26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB8():
    # 'Charts_Data_M12_Local_Fuel'!AB8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AB26,NA())"
    @eval_fn
    def AB8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        ab26_1 = Dashboard_M12_Local_Fuel.AB26()
        var_1 = NA()
        var_2 = IF(b21_1, ab26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC8():
    # 'Charts_Data_M12_Local_Fuel'!AC8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AC26,NA())"
    @eval_fn
    def AC8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        ac26_1 = Dashboard_M12_Local_Fuel.AC26()
        var_1 = NA()
        var_2 = IF(b21_1, ac26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD8():
    # 'Charts_Data_M12_Local_Fuel'!AD8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AD26,NA())"
    @eval_fn
    def AD8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        ad26_1 = Dashboard_M12_Local_Fuel.AD26()
        var_1 = NA()
        var_2 = IF(b21_1, ad26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE8():
    # 'Charts_Data_M12_Local_Fuel'!AE8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AE26,NA())"
    @eval_fn
    def AE8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        ae26_1 = Dashboard_M12_Local_Fuel.AE26()
        var_1 = NA()
        var_2 = IF(b21_1, ae26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF8():
    # 'Charts_Data_M12_Local_Fuel'!AF8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AF26,NA())"
    @eval_fn
    def AF8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        af26_1 = Dashboard_M12_Local_Fuel.AF26()
        var_1 = NA()
        var_2 = IF(b21_1, af26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG8():
    # 'Charts_Data_M12_Local_Fuel'!AG8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AG26,NA())"
    @eval_fn
    def AG8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        ag26_1 = Dashboard_M12_Local_Fuel.AG26()
        var_1 = NA()
        var_2 = IF(b21_1, ag26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH8():
    # 'Charts_Data_M12_Local_Fuel'!AH8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AH26,NA())"
    @eval_fn
    def AH8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        ah26_1 = Dashboard_M12_Local_Fuel.AH26()
        var_1 = NA()
        var_2 = IF(b21_1, ah26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI8():
    # 'Charts_Data_M12_Local_Fuel'!AI8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AI26,NA())"
    @eval_fn
    def AI8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        ai26_1 = Dashboard_M12_Local_Fuel.AI26()
        var_1 = NA()
        var_2 = IF(b21_1, ai26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ8():
    # 'Charts_Data_M12_Local_Fuel'!AJ8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AJ26,NA())"
    @eval_fn
    def AJ8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        aj26_1 = Dashboard_M12_Local_Fuel.AJ26()
        var_1 = NA()
        var_2 = IF(b21_1, aj26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK8():
    # 'Charts_Data_M12_Local_Fuel'!AK8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AK26,NA())"
    @eval_fn
    def AK8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        ak26_1 = Dashboard_M12_Local_Fuel.AK26()
        var_1 = NA()
        var_2 = IF(b21_1, ak26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL8():
    # 'Charts_Data_M12_Local_Fuel'!AL8
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$B$21,'Dashboard M12 Local Fuel'!AL26,NA())"
    @eval_fn
    def AL8():
        b21_1 = Charts_M12_Local_Fuel.B21()
        al26_1 = Dashboard_M12_Local_Fuel.AL26()
        var_1 = NA()
        var_2 = IF(b21_1, al26_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class A9():
    # 'Charts_Data_M12_Local_Fuel'!A9
    value = "Line Graph Input Final"

@register(Charts_Data_M12_Local_Fuel)
class D9():
    # 'Charts_Data_M12_Local_Fuel'!D9
    value = "Hydro"

@register(Charts_Data_M12_Local_Fuel)
class F9():
    # 'Charts_Data_M12_Local_Fuel'!F9
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G9():
    # 'Charts_Data_M12_Local_Fuel'!G9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!G11,NA())"
    @eval_fn
    def G9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        g11_1 = Dashboard_M12_Local_Fuel.G11()
        var_1 = NA()
        var_2 = IF(r21_1, g11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H9():
    # 'Charts_Data_M12_Local_Fuel'!H9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!H11,NA())"
    @eval_fn
    def H9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        h11_1 = Dashboard_M12_Local_Fuel.H11()
        var_1 = NA()
        var_2 = IF(r21_1, h11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I9():
    # 'Charts_Data_M12_Local_Fuel'!I9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!I11,NA())"
    @eval_fn
    def I9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        i11_1 = Dashboard_M12_Local_Fuel.I11()
        var_1 = NA()
        var_2 = IF(r21_1, i11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J9():
    # 'Charts_Data_M12_Local_Fuel'!J9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!J11,NA())"
    @eval_fn
    def J9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        j11_1 = Dashboard_M12_Local_Fuel.J11()
        var_1 = NA()
        var_2 = IF(r21_1, j11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K9():
    # 'Charts_Data_M12_Local_Fuel'!K9
    value = 25490
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!K11,NA())"
    @eval_fn
    def K9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        k11_1 = Dashboard_M12_Local_Fuel.K11()
        var_1 = NA()
        var_2 = IF(r21_1, k11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L9():
    # 'Charts_Data_M12_Local_Fuel'!L9
    value = 37491
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!L11,NA())"
    @eval_fn
    def L9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        l11_1 = Dashboard_M12_Local_Fuel.L11()
        var_1 = NA()
        var_2 = IF(r21_1, l11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M9():
    # 'Charts_Data_M12_Local_Fuel'!M9
    value = 152491
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!M11,NA())"
    @eval_fn
    def M9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        m11_1 = Dashboard_M12_Local_Fuel.M11()
        var_1 = NA()
        var_2 = IF(r21_1, m11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N9():
    # 'Charts_Data_M12_Local_Fuel'!N9
    value = 172119
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!N11,NA())"
    @eval_fn
    def N9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        n11_1 = Dashboard_M12_Local_Fuel.N11()
        var_1 = NA()
        var_2 = IF(r21_1, n11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O9():
    # 'Charts_Data_M12_Local_Fuel'!O9
    value = 137762
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!O11,NA())"
    @eval_fn
    def O9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        o11_1 = Dashboard_M12_Local_Fuel.O11()
        var_1 = NA()
        var_2 = IF(r21_1, o11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P9():
    # 'Charts_Data_M12_Local_Fuel'!P9
    value = 77571
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!P11,NA())"
    @eval_fn
    def P9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        p11_1 = Dashboard_M12_Local_Fuel.P11()
        var_1 = NA()
        var_2 = IF(r21_1, p11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q9():
    # 'Charts_Data_M12_Local_Fuel'!Q9
    value = 106828
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!Q11,NA())"
    @eval_fn
    def Q9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        q11_1 = Dashboard_M12_Local_Fuel.Q11()
        var_1 = NA()
        var_2 = IF(r21_1, q11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R9():
    # 'Charts_Data_M12_Local_Fuel'!R9
    value = 70095
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!R11,NA())"
    @eval_fn
    def R9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        r11_1 = Dashboard_M12_Local_Fuel.R11()
        var_1 = NA()
        var_2 = IF(r21_1, r11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S9():
    # 'Charts_Data_M12_Local_Fuel'!S9
    value = 90423
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!S11,NA())"
    @eval_fn
    def S9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        s11_1 = Dashboard_M12_Local_Fuel.S11()
        var_1 = NA()
        var_2 = IF(r21_1, s11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T9():
    # 'Charts_Data_M12_Local_Fuel'!T9
    value = 103978
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!T11,NA())"
    @eval_fn
    def T9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        t11_1 = Dashboard_M12_Local_Fuel.T11()
        var_1 = NA()
        var_2 = IF(r21_1, t11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U9():
    # 'Charts_Data_M12_Local_Fuel'!U9
    value = 73506
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!U11,NA())"
    @eval_fn
    def U9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        u11_1 = Dashboard_M12_Local_Fuel.U11()
        var_1 = NA()
        var_2 = IF(r21_1, u11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V9():
    # 'Charts_Data_M12_Local_Fuel'!V9
    value = 85446
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!V11,NA())"
    @eval_fn
    def V9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        v11_1 = Dashboard_M12_Local_Fuel.V11()
        var_1 = NA()
        var_2 = IF(r21_1, v11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W9():
    # 'Charts_Data_M12_Local_Fuel'!W9
    value = 106734
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!W11,NA())"
    @eval_fn
    def W9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        w11_1 = Dashboard_M12_Local_Fuel.W11()
        var_1 = NA()
        var_2 = IF(r21_1, w11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X9():
    # 'Charts_Data_M12_Local_Fuel'!X9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!X11,NA())"
    @eval_fn
    def X9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        x11_1 = Dashboard_M12_Local_Fuel.X11()
        var_1 = NA()
        var_2 = IF(r21_1, x11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y9():
    # 'Charts_Data_M12_Local_Fuel'!Y9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!Y11,NA())"
    @eval_fn
    def Y9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        y11_1 = Dashboard_M12_Local_Fuel.Y11()
        var_1 = NA()
        var_2 = IF(r21_1, y11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z9():
    # 'Charts_Data_M12_Local_Fuel'!Z9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!Z11,NA())"
    @eval_fn
    def Z9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        z11_1 = Dashboard_M12_Local_Fuel.Z11()
        var_1 = NA()
        var_2 = IF(r21_1, z11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA9():
    # 'Charts_Data_M12_Local_Fuel'!AA9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AA11,NA())"
    @eval_fn
    def AA9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        aa11_1 = Dashboard_M12_Local_Fuel.AA11()
        var_1 = NA()
        var_2 = IF(r21_1, aa11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB9():
    # 'Charts_Data_M12_Local_Fuel'!AB9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AB11,NA())"
    @eval_fn
    def AB9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        ab11_1 = Dashboard_M12_Local_Fuel.AB11()
        var_1 = NA()
        var_2 = IF(r21_1, ab11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC9():
    # 'Charts_Data_M12_Local_Fuel'!AC9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AC11,NA())"
    @eval_fn
    def AC9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        ac11_1 = Dashboard_M12_Local_Fuel.AC11()
        var_1 = NA()
        var_2 = IF(r21_1, ac11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD9():
    # 'Charts_Data_M12_Local_Fuel'!AD9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AD11,NA())"
    @eval_fn
    def AD9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        ad11_1 = Dashboard_M12_Local_Fuel.AD11()
        var_1 = NA()
        var_2 = IF(r21_1, ad11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE9():
    # 'Charts_Data_M12_Local_Fuel'!AE9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AE11,NA())"
    @eval_fn
    def AE9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        ae11_1 = Dashboard_M12_Local_Fuel.AE11()
        var_1 = NA()
        var_2 = IF(r21_1, ae11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF9():
    # 'Charts_Data_M12_Local_Fuel'!AF9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AF11,NA())"
    @eval_fn
    def AF9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        af11_1 = Dashboard_M12_Local_Fuel.AF11()
        var_1 = NA()
        var_2 = IF(r21_1, af11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG9():
    # 'Charts_Data_M12_Local_Fuel'!AG9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AG11,NA())"
    @eval_fn
    def AG9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        ag11_1 = Dashboard_M12_Local_Fuel.AG11()
        var_1 = NA()
        var_2 = IF(r21_1, ag11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH9():
    # 'Charts_Data_M12_Local_Fuel'!AH9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AH11,NA())"
    @eval_fn
    def AH9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        ah11_1 = Dashboard_M12_Local_Fuel.AH11()
        var_1 = NA()
        var_2 = IF(r21_1, ah11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI9():
    # 'Charts_Data_M12_Local_Fuel'!AI9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AI11,NA())"
    @eval_fn
    def AI9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        ai11_1 = Dashboard_M12_Local_Fuel.AI11()
        var_1 = NA()
        var_2 = IF(r21_1, ai11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ9():
    # 'Charts_Data_M12_Local_Fuel'!AJ9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AJ11,NA())"
    @eval_fn
    def AJ9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        aj11_1 = Dashboard_M12_Local_Fuel.AJ11()
        var_1 = NA()
        var_2 = IF(r21_1, aj11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK9():
    # 'Charts_Data_M12_Local_Fuel'!AK9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AK11,NA())"
    @eval_fn
    def AK9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        ak11_1 = Dashboard_M12_Local_Fuel.AK11()
        var_1 = NA()
        var_2 = IF(r21_1, ak11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL9():
    # 'Charts_Data_M12_Local_Fuel'!AL9
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$R$21,'Dashboard M12 Local Fuel'!AL11,NA())"
    @eval_fn
    def AL9():
        r21_1 = Charts_M12_Local_Fuel.R21()
        al11_1 = Dashboard_M12_Local_Fuel.AL11()
        var_1 = NA()
        var_2 = IF(r21_1, al11_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D10():
    # 'Charts_Data_M12_Local_Fuel'!D10
    value = "Geothermal"

@register(Charts_Data_M12_Local_Fuel)
class F10():
    # 'Charts_Data_M12_Local_Fuel'!F10
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G10():
    # 'Charts_Data_M12_Local_Fuel'!G10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!G12,NA())"
    @eval_fn
    def G10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        g12_1 = Dashboard_M12_Local_Fuel.G12()
        var_1 = NA()
        var_2 = IF(s21_1, g12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H10():
    # 'Charts_Data_M12_Local_Fuel'!H10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!H12,NA())"
    @eval_fn
    def H10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        h12_1 = Dashboard_M12_Local_Fuel.H12()
        var_1 = NA()
        var_2 = IF(s21_1, h12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I10():
    # 'Charts_Data_M12_Local_Fuel'!I10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!I12,NA())"
    @eval_fn
    def I10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        i12_1 = Dashboard_M12_Local_Fuel.I12()
        var_1 = NA()
        var_2 = IF(s21_1, i12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J10():
    # 'Charts_Data_M12_Local_Fuel'!J10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!J12,NA())"
    @eval_fn
    def J10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        j12_1 = Dashboard_M12_Local_Fuel.J12()
        var_1 = NA()
        var_2 = IF(s21_1, j12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K10():
    # 'Charts_Data_M12_Local_Fuel'!K10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!K12,NA())"
    @eval_fn
    def K10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        k12_1 = Dashboard_M12_Local_Fuel.K12()
        var_1 = NA()
        var_2 = IF(s21_1, k12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L10():
    # 'Charts_Data_M12_Local_Fuel'!L10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!L12,NA())"
    @eval_fn
    def L10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        l12_1 = Dashboard_M12_Local_Fuel.L12()
        var_1 = NA()
        var_2 = IF(s21_1, l12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M10():
    # 'Charts_Data_M12_Local_Fuel'!M10
    value = 221000
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!M12,NA())"
    @eval_fn
    def M10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        m12_1 = Dashboard_M12_Local_Fuel.M12()
        var_1 = NA()
        var_2 = IF(s21_1, m12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N10():
    # 'Charts_Data_M12_Local_Fuel'!N10
    value = 212000
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!N12,NA())"
    @eval_fn
    def N10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        n12_1 = Dashboard_M12_Local_Fuel.N12()
        var_1 = NA()
        var_2 = IF(s21_1, n12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O10():
    # 'Charts_Data_M12_Local_Fuel'!O10
    value = 230000
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!O12,NA())"
    @eval_fn
    def O10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        o12_1 = Dashboard_M12_Local_Fuel.O12()
        var_1 = NA()
        var_2 = IF(s21_1, o12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P10():
    # 'Charts_Data_M12_Local_Fuel'!P10
    value = 234334
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!P12,NA())"
    @eval_fn
    def P10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        p12_1 = Dashboard_M12_Local_Fuel.P12()
        var_1 = NA()
        var_2 = IF(s21_1, p12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q10():
    # 'Charts_Data_M12_Local_Fuel'!Q10
    value = 167591
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!Q12,NA())"
    @eval_fn
    def Q10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        q12_1 = Dashboard_M12_Local_Fuel.Q12()
        var_1 = NA()
        var_2 = IF(s21_1, q12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R10():
    # 'Charts_Data_M12_Local_Fuel'!R10
    value = 201587
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!R12,NA())"
    @eval_fn
    def R10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        r12_1 = Dashboard_M12_Local_Fuel.R12()
        var_1 = NA()
        var_2 = IF(s21_1, r12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S10():
    # 'Charts_Data_M12_Local_Fuel'!S10
    value = 232906
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!S12,NA())"
    @eval_fn
    def S10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        s12_1 = Dashboard_M12_Local_Fuel.S12()
        var_1 = NA()
        var_2 = IF(s21_1, s12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T10():
    # 'Charts_Data_M12_Local_Fuel'!T10
    value = 266234
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!T12,NA())"
    @eval_fn
    def T10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        t12_1 = Dashboard_M12_Local_Fuel.T12()
        var_1 = NA()
        var_2 = IF(s21_1, t12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U10():
    # 'Charts_Data_M12_Local_Fuel'!U10
    value = 281417
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!U12,NA())"
    @eval_fn
    def U10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        u12_1 = Dashboard_M12_Local_Fuel.U12()
        var_1 = NA()
        var_2 = IF(s21_1, u12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V10():
    # 'Charts_Data_M12_Local_Fuel'!V10
    value = 255027
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!V12,NA())"
    @eval_fn
    def V10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        v12_1 = Dashboard_M12_Local_Fuel.V12()
        var_1 = NA()
        var_2 = IF(s21_1, v12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W10():
    # 'Charts_Data_M12_Local_Fuel'!W10
    value = 230495
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!W12,NA())"
    @eval_fn
    def W10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        w12_1 = Dashboard_M12_Local_Fuel.W12()
        var_1 = NA()
        var_2 = IF(s21_1, w12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X10():
    # 'Charts_Data_M12_Local_Fuel'!X10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!X12,NA())"
    @eval_fn
    def X10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        x12_1 = Dashboard_M12_Local_Fuel.X12()
        var_1 = NA()
        var_2 = IF(s21_1, x12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y10():
    # 'Charts_Data_M12_Local_Fuel'!Y10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!Y12,NA())"
    @eval_fn
    def Y10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        y12_1 = Dashboard_M12_Local_Fuel.Y12()
        var_1 = NA()
        var_2 = IF(s21_1, y12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z10():
    # 'Charts_Data_M12_Local_Fuel'!Z10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!Z12,NA())"
    @eval_fn
    def Z10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        z12_1 = Dashboard_M12_Local_Fuel.Z12()
        var_1 = NA()
        var_2 = IF(s21_1, z12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA10():
    # 'Charts_Data_M12_Local_Fuel'!AA10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AA12,NA())"
    @eval_fn
    def AA10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        aa12_1 = Dashboard_M12_Local_Fuel.AA12()
        var_1 = NA()
        var_2 = IF(s21_1, aa12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB10():
    # 'Charts_Data_M12_Local_Fuel'!AB10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AB12,NA())"
    @eval_fn
    def AB10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        ab12_1 = Dashboard_M12_Local_Fuel.AB12()
        var_1 = NA()
        var_2 = IF(s21_1, ab12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC10():
    # 'Charts_Data_M12_Local_Fuel'!AC10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AC12,NA())"
    @eval_fn
    def AC10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        ac12_1 = Dashboard_M12_Local_Fuel.AC12()
        var_1 = NA()
        var_2 = IF(s21_1, ac12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD10():
    # 'Charts_Data_M12_Local_Fuel'!AD10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AD12,NA())"
    @eval_fn
    def AD10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        ad12_1 = Dashboard_M12_Local_Fuel.AD12()
        var_1 = NA()
        var_2 = IF(s21_1, ad12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE10():
    # 'Charts_Data_M12_Local_Fuel'!AE10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AE12,NA())"
    @eval_fn
    def AE10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        ae12_1 = Dashboard_M12_Local_Fuel.AE12()
        var_1 = NA()
        var_2 = IF(s21_1, ae12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF10():
    # 'Charts_Data_M12_Local_Fuel'!AF10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AF12,NA())"
    @eval_fn
    def AF10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        af12_1 = Dashboard_M12_Local_Fuel.AF12()
        var_1 = NA()
        var_2 = IF(s21_1, af12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG10():
    # 'Charts_Data_M12_Local_Fuel'!AG10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AG12,NA())"
    @eval_fn
    def AG10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        ag12_1 = Dashboard_M12_Local_Fuel.AG12()
        var_1 = NA()
        var_2 = IF(s21_1, ag12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH10():
    # 'Charts_Data_M12_Local_Fuel'!AH10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AH12,NA())"
    @eval_fn
    def AH10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        ah12_1 = Dashboard_M12_Local_Fuel.AH12()
        var_1 = NA()
        var_2 = IF(s21_1, ah12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI10():
    # 'Charts_Data_M12_Local_Fuel'!AI10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AI12,NA())"
    @eval_fn
    def AI10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        ai12_1 = Dashboard_M12_Local_Fuel.AI12()
        var_1 = NA()
        var_2 = IF(s21_1, ai12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ10():
    # 'Charts_Data_M12_Local_Fuel'!AJ10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AJ12,NA())"
    @eval_fn
    def AJ10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        aj12_1 = Dashboard_M12_Local_Fuel.AJ12()
        var_1 = NA()
        var_2 = IF(s21_1, aj12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK10():
    # 'Charts_Data_M12_Local_Fuel'!AK10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AK12,NA())"
    @eval_fn
    def AK10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        ak12_1 = Dashboard_M12_Local_Fuel.AK12()
        var_1 = NA()
        var_2 = IF(s21_1, ak12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL10():
    # 'Charts_Data_M12_Local_Fuel'!AL10
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$S$21,'Dashboard M12 Local Fuel'!AL12,NA())"
    @eval_fn
    def AL10():
        s21_1 = Charts_M12_Local_Fuel.S21()
        al12_1 = Dashboard_M12_Local_Fuel.AL12()
        var_1 = NA()
        var_2 = IF(s21_1, al12_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D11():
    # 'Charts_Data_M12_Local_Fuel'!D11
    value = "Wind "

@register(Charts_Data_M12_Local_Fuel)
class F11():
    # 'Charts_Data_M12_Local_Fuel'!F11
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G11():
    # 'Charts_Data_M12_Local_Fuel'!G11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!G13,NA())"
    @eval_fn
    def G11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        g13_1 = Dashboard_M12_Local_Fuel.G13()
        var_1 = NA()
        var_2 = IF(t21_1, g13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H11():
    # 'Charts_Data_M12_Local_Fuel'!H11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!H13,NA())"
    @eval_fn
    def H11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        h13_1 = Dashboard_M12_Local_Fuel.H13()
        var_1 = NA()
        var_2 = IF(t21_1, h13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I11():
    # 'Charts_Data_M12_Local_Fuel'!I11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!I13,NA())"
    @eval_fn
    def I11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        i13_1 = Dashboard_M12_Local_Fuel.I13()
        var_1 = NA()
        var_2 = IF(t21_1, i13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J11():
    # 'Charts_Data_M12_Local_Fuel'!J11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!J13,NA())"
    @eval_fn
    def J11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        j13_1 = Dashboard_M12_Local_Fuel.J13()
        var_1 = NA()
        var_2 = IF(t21_1, j13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K11():
    # 'Charts_Data_M12_Local_Fuel'!K11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!K13,NA())"
    @eval_fn
    def K11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        k13_1 = Dashboard_M12_Local_Fuel.K13()
        var_1 = NA()
        var_2 = IF(t21_1, k13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L11():
    # 'Charts_Data_M12_Local_Fuel'!L11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!L13,NA())"
    @eval_fn
    def L11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        l13_1 = Dashboard_M12_Local_Fuel.L13()
        var_1 = NA()
        var_2 = IF(t21_1, l13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M11():
    # 'Charts_Data_M12_Local_Fuel'!M11
    value = 7000
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!M13,NA())"
    @eval_fn
    def M11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        m13_1 = Dashboard_M12_Local_Fuel.M13()
        var_1 = NA()
        var_2 = IF(t21_1, m13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N11():
    # 'Charts_Data_M12_Local_Fuel'!N11
    value = 82000
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!N13,NA())"
    @eval_fn
    def N11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        n13_1 = Dashboard_M12_Local_Fuel.N13()
        var_1 = NA()
        var_2 = IF(t21_1, n13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O11():
    # 'Charts_Data_M12_Local_Fuel'!O11
    value = 242400
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!O13,NA())"
    @eval_fn
    def O11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        o13_1 = Dashboard_M12_Local_Fuel.O13()
        var_1 = NA()
        var_2 = IF(t21_1, o13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P11():
    # 'Charts_Data_M12_Local_Fuel'!P11
    value = 237293
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!P13,NA())"
    @eval_fn
    def P11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        p13_1 = Dashboard_M12_Local_Fuel.P13()
        var_1 = NA()
        var_2 = IF(t21_1, p13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q11():
    # 'Charts_Data_M12_Local_Fuel'!Q11
    value = 250355
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!Q13,NA())"
    @eval_fn
    def Q11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        q13_1 = Dashboard_M12_Local_Fuel.Q13()
        var_1 = NA()
        var_2 = IF(t21_1, q13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R11():
    # 'Charts_Data_M12_Local_Fuel'!R11
    value = 261206
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!R13,NA())"
    @eval_fn
    def R11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        r13_1 = Dashboard_M12_Local_Fuel.R13()
        var_1 = NA()
        var_2 = IF(t21_1, r13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S11():
    # 'Charts_Data_M12_Local_Fuel'!S11
    value = 344376
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!S13,NA())"
    @eval_fn
    def S11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        s13_1 = Dashboard_M12_Local_Fuel.S13()
        var_1 = NA()
        var_2 = IF(t21_1, s13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T11():
    # 'Charts_Data_M12_Local_Fuel'!T11
    value = 388256
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!T13,NA())"
    @eval_fn
    def T11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        t13_1 = Dashboard_M12_Local_Fuel.T13()
        var_1 = NA()
        var_2 = IF(t21_1, t13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U11():
    # 'Charts_Data_M12_Local_Fuel'!U11
    value = 503548
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!U13,NA())"
    @eval_fn
    def U11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        u13_1 = Dashboard_M12_Local_Fuel.U13()
        var_1 = NA()
        var_2 = IF(t21_1, u13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V11():
    # 'Charts_Data_M12_Local_Fuel'!V11
    value = 577867
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!V13,NA())"
    @eval_fn
    def V11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        v13_1 = Dashboard_M12_Local_Fuel.V13()
        var_1 = NA()
        var_2 = IF(t21_1, v13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W11():
    # 'Charts_Data_M12_Local_Fuel'!W11
    value = 612781
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!W13,NA())"
    @eval_fn
    def W11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        w13_1 = Dashboard_M12_Local_Fuel.W13()
        var_1 = NA()
        var_2 = IF(t21_1, w13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X11():
    # 'Charts_Data_M12_Local_Fuel'!X11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!X13,NA())"
    @eval_fn
    def X11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        x13_1 = Dashboard_M12_Local_Fuel.X13()
        var_1 = NA()
        var_2 = IF(t21_1, x13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y11():
    # 'Charts_Data_M12_Local_Fuel'!Y11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!Y13,NA())"
    @eval_fn
    def Y11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        y13_1 = Dashboard_M12_Local_Fuel.Y13()
        var_1 = NA()
        var_2 = IF(t21_1, y13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z11():
    # 'Charts_Data_M12_Local_Fuel'!Z11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!Z13,NA())"
    @eval_fn
    def Z11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        z13_1 = Dashboard_M12_Local_Fuel.Z13()
        var_1 = NA()
        var_2 = IF(t21_1, z13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA11():
    # 'Charts_Data_M12_Local_Fuel'!AA11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AA13,NA())"
    @eval_fn
    def AA11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        aa13_1 = Dashboard_M12_Local_Fuel.AA13()
        var_1 = NA()
        var_2 = IF(t21_1, aa13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB11():
    # 'Charts_Data_M12_Local_Fuel'!AB11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AB13,NA())"
    @eval_fn
    def AB11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        ab13_1 = Dashboard_M12_Local_Fuel.AB13()
        var_1 = NA()
        var_2 = IF(t21_1, ab13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC11():
    # 'Charts_Data_M12_Local_Fuel'!AC11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AC13,NA())"
    @eval_fn
    def AC11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        ac13_1 = Dashboard_M12_Local_Fuel.AC13()
        var_1 = NA()
        var_2 = IF(t21_1, ac13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD11():
    # 'Charts_Data_M12_Local_Fuel'!AD11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AD13,NA())"
    @eval_fn
    def AD11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        ad13_1 = Dashboard_M12_Local_Fuel.AD13()
        var_1 = NA()
        var_2 = IF(t21_1, ad13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE11():
    # 'Charts_Data_M12_Local_Fuel'!AE11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AE13,NA())"
    @eval_fn
    def AE11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        ae13_1 = Dashboard_M12_Local_Fuel.AE13()
        var_1 = NA()
        var_2 = IF(t21_1, ae13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF11():
    # 'Charts_Data_M12_Local_Fuel'!AF11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AF13,NA())"
    @eval_fn
    def AF11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        af13_1 = Dashboard_M12_Local_Fuel.AF13()
        var_1 = NA()
        var_2 = IF(t21_1, af13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG11():
    # 'Charts_Data_M12_Local_Fuel'!AG11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AG13,NA())"
    @eval_fn
    def AG11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        ag13_1 = Dashboard_M12_Local_Fuel.AG13()
        var_1 = NA()
        var_2 = IF(t21_1, ag13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH11():
    # 'Charts_Data_M12_Local_Fuel'!AH11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AH13,NA())"
    @eval_fn
    def AH11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        ah13_1 = Dashboard_M12_Local_Fuel.AH13()
        var_1 = NA()
        var_2 = IF(t21_1, ah13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI11():
    # 'Charts_Data_M12_Local_Fuel'!AI11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AI13,NA())"
    @eval_fn
    def AI11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        ai13_1 = Dashboard_M12_Local_Fuel.AI13()
        var_1 = NA()
        var_2 = IF(t21_1, ai13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ11():
    # 'Charts_Data_M12_Local_Fuel'!AJ11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AJ13,NA())"
    @eval_fn
    def AJ11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        aj13_1 = Dashboard_M12_Local_Fuel.AJ13()
        var_1 = NA()
        var_2 = IF(t21_1, aj13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK11():
    # 'Charts_Data_M12_Local_Fuel'!AK11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AK13,NA())"
    @eval_fn
    def AK11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        ak13_1 = Dashboard_M12_Local_Fuel.AK13()
        var_1 = NA()
        var_2 = IF(t21_1, ak13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL11():
    # 'Charts_Data_M12_Local_Fuel'!AL11
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$T$21,'Dashboard M12 Local Fuel'!AL13,NA())"
    @eval_fn
    def AL11():
        t21_1 = Charts_M12_Local_Fuel.T21()
        al13_1 = Dashboard_M12_Local_Fuel.AL13()
        var_1 = NA()
        var_2 = IF(t21_1, al13_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D12():
    # 'Charts_Data_M12_Local_Fuel'!D12
    value = "Biomass "

@register(Charts_Data_M12_Local_Fuel)
class F12():
    # 'Charts_Data_M12_Local_Fuel'!F12
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G12():
    # 'Charts_Data_M12_Local_Fuel'!G12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!G14,NA())"
    @eval_fn
    def G12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        g14_1 = Dashboard_M12_Local_Fuel.G14()
        var_1 = NA()
        var_2 = IF(u21_1, g14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H12():
    # 'Charts_Data_M12_Local_Fuel'!H12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!H14,NA())"
    @eval_fn
    def H12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        h14_1 = Dashboard_M12_Local_Fuel.H14()
        var_1 = NA()
        var_2 = IF(u21_1, h14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I12():
    # 'Charts_Data_M12_Local_Fuel'!I12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!I14,NA())"
    @eval_fn
    def I12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        i14_1 = Dashboard_M12_Local_Fuel.I14()
        var_1 = NA()
        var_2 = IF(u21_1, i14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J12():
    # 'Charts_Data_M12_Local_Fuel'!J12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!J14,NA())"
    @eval_fn
    def J12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        j14_1 = Dashboard_M12_Local_Fuel.J14()
        var_1 = NA()
        var_2 = IF(u21_1, j14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K12():
    # 'Charts_Data_M12_Local_Fuel'!K12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!K14,NA())"
    @eval_fn
    def K12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        k14_1 = Dashboard_M12_Local_Fuel.K14()
        var_1 = NA()
        var_2 = IF(u21_1, k14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L12():
    # 'Charts_Data_M12_Local_Fuel'!L12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!L14,NA())"
    @eval_fn
    def L12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        l14_1 = Dashboard_M12_Local_Fuel.L14()
        var_1 = NA()
        var_2 = IF(u21_1, l14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M12():
    # 'Charts_Data_M12_Local_Fuel'!M12
    value = 333000
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!M14,NA())"
    @eval_fn
    def M12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        m14_1 = Dashboard_M12_Local_Fuel.M14()
        var_1 = NA()
        var_2 = IF(u21_1, m14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N12():
    # 'Charts_Data_M12_Local_Fuel'!N12
    value = 395000
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!N14,NA())"
    @eval_fn
    def N12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        n14_1 = Dashboard_M12_Local_Fuel.N14()
        var_1 = NA()
        var_2 = IF(u21_1, n14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O12():
    # 'Charts_Data_M12_Local_Fuel'!O12
    value = 326000
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!O14,NA())"
    @eval_fn
    def O12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        o14_1 = Dashboard_M12_Local_Fuel.O14()
        var_1 = NA()
        var_2 = IF(u21_1, o14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P12():
    # 'Charts_Data_M12_Local_Fuel'!P12
    value = 412598
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!P14,NA())"
    @eval_fn
    def P12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        p14_1 = Dashboard_M12_Local_Fuel.P14()
        var_1 = NA()
        var_2 = IF(u21_1, p14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q12():
    # 'Charts_Data_M12_Local_Fuel'!Q12
    value = 398755
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!Q14,NA())"
    @eval_fn
    def Q12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        q14_1 = Dashboard_M12_Local_Fuel.Q14()
        var_1 = NA()
        var_2 = IF(u21_1, q14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R12():
    # 'Charts_Data_M12_Local_Fuel'!R12
    value = 358852
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!R14,NA())"
    @eval_fn
    def R12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        r14_1 = Dashboard_M12_Local_Fuel.R14()
        var_1 = NA()
        var_2 = IF(u21_1, r14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S12():
    # 'Charts_Data_M12_Local_Fuel'!S12
    value = 365266
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!S14,NA())"
    @eval_fn
    def S12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        s14_1 = Dashboard_M12_Local_Fuel.S14()
        var_1 = NA()
        var_2 = IF(u21_1, s14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T12():
    # 'Charts_Data_M12_Local_Fuel'!T12
    value = 341790
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!T14,NA())"
    @eval_fn
    def T12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        t14_1 = Dashboard_M12_Local_Fuel.T14()
        var_1 = NA()
        var_2 = IF(u21_1, t14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U12():
    # 'Charts_Data_M12_Local_Fuel'!U12
    value = 415691
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!U14,NA())"
    @eval_fn
    def U12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        u14_1 = Dashboard_M12_Local_Fuel.U14()
        var_1 = NA()
        var_2 = IF(u21_1, u14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V12():
    # 'Charts_Data_M12_Local_Fuel'!V12
    value = 433164
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!V14,NA())"
    @eval_fn
    def V12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        v14_1 = Dashboard_M12_Local_Fuel.V14()
        var_1 = NA()
        var_2 = IF(u21_1, v14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W12():
    # 'Charts_Data_M12_Local_Fuel'!W12
    value = 416716
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!W14,NA())"
    @eval_fn
    def W12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        w14_1 = Dashboard_M12_Local_Fuel.W14()
        var_1 = NA()
        var_2 = IF(u21_1, w14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X12():
    # 'Charts_Data_M12_Local_Fuel'!X12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!X14,NA())"
    @eval_fn
    def X12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        x14_1 = Dashboard_M12_Local_Fuel.X14()
        var_1 = NA()
        var_2 = IF(u21_1, x14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y12():
    # 'Charts_Data_M12_Local_Fuel'!Y12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!Y14,NA())"
    @eval_fn
    def Y12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        y14_1 = Dashboard_M12_Local_Fuel.Y14()
        var_1 = NA()
        var_2 = IF(u21_1, y14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z12():
    # 'Charts_Data_M12_Local_Fuel'!Z12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!Z14,NA())"
    @eval_fn
    def Z12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        z14_1 = Dashboard_M12_Local_Fuel.Z14()
        var_1 = NA()
        var_2 = IF(u21_1, z14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA12():
    # 'Charts_Data_M12_Local_Fuel'!AA12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AA14,NA())"
    @eval_fn
    def AA12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        aa14_1 = Dashboard_M12_Local_Fuel.AA14()
        var_1 = NA()
        var_2 = IF(u21_1, aa14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB12():
    # 'Charts_Data_M12_Local_Fuel'!AB12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AB14,NA())"
    @eval_fn
    def AB12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        ab14_1 = Dashboard_M12_Local_Fuel.AB14()
        var_1 = NA()
        var_2 = IF(u21_1, ab14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC12():
    # 'Charts_Data_M12_Local_Fuel'!AC12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AC14,NA())"
    @eval_fn
    def AC12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        ac14_1 = Dashboard_M12_Local_Fuel.AC14()
        var_1 = NA()
        var_2 = IF(u21_1, ac14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD12():
    # 'Charts_Data_M12_Local_Fuel'!AD12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AD14,NA())"
    @eval_fn
    def AD12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        ad14_1 = Dashboard_M12_Local_Fuel.AD14()
        var_1 = NA()
        var_2 = IF(u21_1, ad14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE12():
    # 'Charts_Data_M12_Local_Fuel'!AE12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AE14,NA())"
    @eval_fn
    def AE12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        ae14_1 = Dashboard_M12_Local_Fuel.AE14()
        var_1 = NA()
        var_2 = IF(u21_1, ae14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF12():
    # 'Charts_Data_M12_Local_Fuel'!AF12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AF14,NA())"
    @eval_fn
    def AF12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        af14_1 = Dashboard_M12_Local_Fuel.AF14()
        var_1 = NA()
        var_2 = IF(u21_1, af14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG12():
    # 'Charts_Data_M12_Local_Fuel'!AG12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AG14,NA())"
    @eval_fn
    def AG12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        ag14_1 = Dashboard_M12_Local_Fuel.AG14()
        var_1 = NA()
        var_2 = IF(u21_1, ag14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH12():
    # 'Charts_Data_M12_Local_Fuel'!AH12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AH14,NA())"
    @eval_fn
    def AH12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        ah14_1 = Dashboard_M12_Local_Fuel.AH14()
        var_1 = NA()
        var_2 = IF(u21_1, ah14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI12():
    # 'Charts_Data_M12_Local_Fuel'!AI12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AI14,NA())"
    @eval_fn
    def AI12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        ai14_1 = Dashboard_M12_Local_Fuel.AI14()
        var_1 = NA()
        var_2 = IF(u21_1, ai14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ12():
    # 'Charts_Data_M12_Local_Fuel'!AJ12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AJ14,NA())"
    @eval_fn
    def AJ12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        aj14_1 = Dashboard_M12_Local_Fuel.AJ14()
        var_1 = NA()
        var_2 = IF(u21_1, aj14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK12():
    # 'Charts_Data_M12_Local_Fuel'!AK12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AK14,NA())"
    @eval_fn
    def AK12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        ak14_1 = Dashboard_M12_Local_Fuel.AK14()
        var_1 = NA()
        var_2 = IF(u21_1, ak14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL12():
    # 'Charts_Data_M12_Local_Fuel'!AL12
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$U$21,'Dashboard M12 Local Fuel'!AL14,NA())"
    @eval_fn
    def AL12():
        u21_1 = Charts_M12_Local_Fuel.U21()
        al14_1 = Dashboard_M12_Local_Fuel.AL14()
        var_1 = NA()
        var_2 = IF(u21_1, al14_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D13():
    # 'Charts_Data_M12_Local_Fuel'!D13
    value = "Solar "

@register(Charts_Data_M12_Local_Fuel)
class F13():
    # 'Charts_Data_M12_Local_Fuel'!F13
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G13():
    # 'Charts_Data_M12_Local_Fuel'!G13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!G15,NA())"
    @eval_fn
    def G13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        g15_1 = Dashboard_M12_Local_Fuel.G15()
        var_1 = NA()
        var_2 = IF(v21_1, g15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H13():
    # 'Charts_Data_M12_Local_Fuel'!H13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!H15,NA())"
    @eval_fn
    def H13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        h15_1 = Dashboard_M12_Local_Fuel.H15()
        var_1 = NA()
        var_2 = IF(v21_1, h15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I13():
    # 'Charts_Data_M12_Local_Fuel'!I13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!I15,NA())"
    @eval_fn
    def I13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        i15_1 = Dashboard_M12_Local_Fuel.I15()
        var_1 = NA()
        var_2 = IF(v21_1, i15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J13():
    # 'Charts_Data_M12_Local_Fuel'!J13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!J15,NA())"
    @eval_fn
    def J13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        j15_1 = Dashboard_M12_Local_Fuel.J15()
        var_1 = NA()
        var_2 = IF(v21_1, j15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K13():
    # 'Charts_Data_M12_Local_Fuel'!K13
    value = 66
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!K15,NA())"
    @eval_fn
    def K13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        k15_1 = Dashboard_M12_Local_Fuel.K15()
        var_1 = NA()
        var_2 = IF(v21_1, k15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L13():
    # 'Charts_Data_M12_Local_Fuel'!L13
    value = 90
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!L15,NA())"
    @eval_fn
    def L13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        l15_1 = Dashboard_M12_Local_Fuel.L15()
        var_1 = NA()
        var_2 = IF(v21_1, l15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M13():
    # 'Charts_Data_M12_Local_Fuel'!M13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!M15,NA())"
    @eval_fn
    def M13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        m15_1 = Dashboard_M12_Local_Fuel.M15()
        var_1 = NA()
        var_2 = IF(v21_1, m15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N13():
    # 'Charts_Data_M12_Local_Fuel'!N13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!N15,NA())"
    @eval_fn
    def N13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        n15_1 = Dashboard_M12_Local_Fuel.N15()
        var_1 = NA()
        var_2 = IF(v21_1, n15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O13():
    # 'Charts_Data_M12_Local_Fuel'!O13
    value = 7913.58339639
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!O15,NA())"
    @eval_fn
    def O13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        o15_1 = Dashboard_M12_Local_Fuel.O15()
        var_1 = NA()
        var_2 = IF(v21_1, o15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P13():
    # 'Charts_Data_M12_Local_Fuel'!P13
    value = 14263.816
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!P15,NA())"
    @eval_fn
    def P13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        p15_1 = Dashboard_M12_Local_Fuel.P15()
        var_1 = NA()
        var_2 = IF(v21_1, p15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q13():
    # 'Charts_Data_M12_Local_Fuel'!Q13
    value = 36411.264
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!Q15,NA())"
    @eval_fn
    def Q13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        q15_1 = Dashboard_M12_Local_Fuel.Q15()
        var_1 = NA()
        var_2 = IF(v21_1, q15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R13():
    # 'Charts_Data_M12_Local_Fuel'!R13
    value = 56517.773
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!R15,NA())"
    @eval_fn
    def R13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        r15_1 = Dashboard_M12_Local_Fuel.R15()
        var_1 = NA()
        var_2 = IF(v21_1, r15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S13():
    # 'Charts_Data_M12_Local_Fuel'!S13
    value = 97027.11
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!S15,NA())"
    @eval_fn
    def S13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        s15_1 = Dashboard_M12_Local_Fuel.S15()
        var_1 = NA()
        var_2 = IF(v21_1, s15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T13():
    # 'Charts_Data_M12_Local_Fuel'!T13
    value = 207409.765
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!T15,NA())"
    @eval_fn
    def T13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        t15_1 = Dashboard_M12_Local_Fuel.T15()
        var_1 = NA()
        var_2 = IF(v21_1, t15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U13():
    # 'Charts_Data_M12_Local_Fuel'!U13
    value = 402118.528253
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!U15,NA())"
    @eval_fn
    def U13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        u15_1 = Dashboard_M12_Local_Fuel.U15()
        var_1 = NA()
        var_2 = IF(v21_1, u15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V13():
    # 'Charts_Data_M12_Local_Fuel'!V13
    value = 593227.943632
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!V15,NA())"
    @eval_fn
    def V13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        v15_1 = Dashboard_M12_Local_Fuel.V15()
        var_1 = NA()
        var_2 = IF(v21_1, v15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W13():
    # 'Charts_Data_M12_Local_Fuel'!W13
    value = 696057
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!W15,NA())"
    @eval_fn
    def W13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        w15_1 = Dashboard_M12_Local_Fuel.W15()
        var_1 = NA()
        var_2 = IF(v21_1, w15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X13():
    # 'Charts_Data_M12_Local_Fuel'!X13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!X15,NA())"
    @eval_fn
    def X13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        x15_1 = Dashboard_M12_Local_Fuel.X15()
        var_1 = NA()
        var_2 = IF(v21_1, x15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y13():
    # 'Charts_Data_M12_Local_Fuel'!Y13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!Y15,NA())"
    @eval_fn
    def Y13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        y15_1 = Dashboard_M12_Local_Fuel.Y15()
        var_1 = NA()
        var_2 = IF(v21_1, y15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z13():
    # 'Charts_Data_M12_Local_Fuel'!Z13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!Z15,NA())"
    @eval_fn
    def Z13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        z15_1 = Dashboard_M12_Local_Fuel.Z15()
        var_1 = NA()
        var_2 = IF(v21_1, z15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA13():
    # 'Charts_Data_M12_Local_Fuel'!AA13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AA15,NA())"
    @eval_fn
    def AA13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        aa15_1 = Dashboard_M12_Local_Fuel.AA15()
        var_1 = NA()
        var_2 = IF(v21_1, aa15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB13():
    # 'Charts_Data_M12_Local_Fuel'!AB13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AB15,NA())"
    @eval_fn
    def AB13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        ab15_1 = Dashboard_M12_Local_Fuel.AB15()
        var_1 = NA()
        var_2 = IF(v21_1, ab15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC13():
    # 'Charts_Data_M12_Local_Fuel'!AC13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AC15,NA())"
    @eval_fn
    def AC13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        ac15_1 = Dashboard_M12_Local_Fuel.AC15()
        var_1 = NA()
        var_2 = IF(v21_1, ac15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD13():
    # 'Charts_Data_M12_Local_Fuel'!AD13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AD15,NA())"
    @eval_fn
    def AD13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        ad15_1 = Dashboard_M12_Local_Fuel.AD15()
        var_1 = NA()
        var_2 = IF(v21_1, ad15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE13():
    # 'Charts_Data_M12_Local_Fuel'!AE13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AE15,NA())"
    @eval_fn
    def AE13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        ae15_1 = Dashboard_M12_Local_Fuel.AE15()
        var_1 = NA()
        var_2 = IF(v21_1, ae15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF13():
    # 'Charts_Data_M12_Local_Fuel'!AF13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AF15,NA())"
    @eval_fn
    def AF13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        af15_1 = Dashboard_M12_Local_Fuel.AF15()
        var_1 = NA()
        var_2 = IF(v21_1, af15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG13():
    # 'Charts_Data_M12_Local_Fuel'!AG13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AG15,NA())"
    @eval_fn
    def AG13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        ag15_1 = Dashboard_M12_Local_Fuel.AG15()
        var_1 = NA()
        var_2 = IF(v21_1, ag15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH13():
    # 'Charts_Data_M12_Local_Fuel'!AH13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AH15,NA())"
    @eval_fn
    def AH13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        ah15_1 = Dashboard_M12_Local_Fuel.AH15()
        var_1 = NA()
        var_2 = IF(v21_1, ah15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI13():
    # 'Charts_Data_M12_Local_Fuel'!AI13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AI15,NA())"
    @eval_fn
    def AI13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        ai15_1 = Dashboard_M12_Local_Fuel.AI15()
        var_1 = NA()
        var_2 = IF(v21_1, ai15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ13():
    # 'Charts_Data_M12_Local_Fuel'!AJ13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AJ15,NA())"
    @eval_fn
    def AJ13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        aj15_1 = Dashboard_M12_Local_Fuel.AJ15()
        var_1 = NA()
        var_2 = IF(v21_1, aj15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK13():
    # 'Charts_Data_M12_Local_Fuel'!AK13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AK15,NA())"
    @eval_fn
    def AK13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        ak15_1 = Dashboard_M12_Local_Fuel.AK15()
        var_1 = NA()
        var_2 = IF(v21_1, ak15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL13():
    # 'Charts_Data_M12_Local_Fuel'!AL13
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$V$21,'Dashboard M12 Local Fuel'!AL15,NA())"
    @eval_fn
    def AL13():
        v21_1 = Charts_M12_Local_Fuel.V21()
        al15_1 = Dashboard_M12_Local_Fuel.AL15()
        var_1 = NA()
        var_2 = IF(v21_1, al15_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D14():
    # 'Charts_Data_M12_Local_Fuel'!D14
    value = "Biofuels "

@register(Charts_Data_M12_Local_Fuel)
class F14():
    # 'Charts_Data_M12_Local_Fuel'!F14
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G14():
    # 'Charts_Data_M12_Local_Fuel'!G14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!G16,NA())"
    @eval_fn
    def G14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        g16_1 = Dashboard_M12_Local_Fuel.G16()
        var_1 = NA()
        var_2 = IF(w21_1, g16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H14():
    # 'Charts_Data_M12_Local_Fuel'!H14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!H16,NA())"
    @eval_fn
    def H14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        h16_1 = Dashboard_M12_Local_Fuel.H16()
        var_1 = NA()
        var_2 = IF(w21_1, h16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I14():
    # 'Charts_Data_M12_Local_Fuel'!I14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!I16,NA())"
    @eval_fn
    def I14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        i16_1 = Dashboard_M12_Local_Fuel.I16()
        var_1 = NA()
        var_2 = IF(w21_1, i16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J14():
    # 'Charts_Data_M12_Local_Fuel'!J14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!J16,NA())"
    @eval_fn
    def J14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        j16_1 = Dashboard_M12_Local_Fuel.J16()
        var_1 = NA()
        var_2 = IF(w21_1, j16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K14():
    # 'Charts_Data_M12_Local_Fuel'!K14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!K16,NA())"
    @eval_fn
    def K14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        k16_1 = Dashboard_M12_Local_Fuel.K16()
        var_1 = NA()
        var_2 = IF(w21_1, k16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L14():
    # 'Charts_Data_M12_Local_Fuel'!L14
    value = 257
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!L16,NA())"
    @eval_fn
    def L14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        l16_1 = Dashboard_M12_Local_Fuel.L16()
        var_1 = NA()
        var_2 = IF(w21_1, l16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M14():
    # 'Charts_Data_M12_Local_Fuel'!M14
    value = 509
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!M16,NA())"
    @eval_fn
    def M14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        m16_1 = Dashboard_M12_Local_Fuel.M16()
        var_1 = NA()
        var_2 = IF(w21_1, m16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N14():
    # 'Charts_Data_M12_Local_Fuel'!N14
    value = 523
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!N16,NA())"
    @eval_fn
    def N14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        n16_1 = Dashboard_M12_Local_Fuel.N16()
        var_1 = NA()
        var_2 = IF(w21_1, n16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O14():
    # 'Charts_Data_M12_Local_Fuel'!O14
    value = 1833
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!O16,NA())"
    @eval_fn
    def O14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        o16_1 = Dashboard_M12_Local_Fuel.O16()
        var_1 = NA()
        var_2 = IF(w21_1, o16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P14():
    # 'Charts_Data_M12_Local_Fuel'!P14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!P16,NA())"
    @eval_fn
    def P14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        p16_1 = Dashboard_M12_Local_Fuel.P16()
        var_1 = NA()
        var_2 = IF(w21_1, p16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q14():
    # 'Charts_Data_M12_Local_Fuel'!Q14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!Q16,NA())"
    @eval_fn
    def Q14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        q16_1 = Dashboard_M12_Local_Fuel.Q16()
        var_1 = NA()
        var_2 = IF(w21_1, q16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R14():
    # 'Charts_Data_M12_Local_Fuel'!R14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!R16,NA())"
    @eval_fn
    def R14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        r16_1 = Dashboard_M12_Local_Fuel.R16()
        var_1 = NA()
        var_2 = IF(w21_1, r16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S14():
    # 'Charts_Data_M12_Local_Fuel'!S14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!S16,NA())"
    @eval_fn
    def S14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        s16_1 = Dashboard_M12_Local_Fuel.S16()
        var_1 = NA()
        var_2 = IF(w21_1, s16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T14():
    # 'Charts_Data_M12_Local_Fuel'!T14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!T16,NA())"
    @eval_fn
    def T14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        t16_1 = Dashboard_M12_Local_Fuel.T16()
        var_1 = NA()
        var_2 = IF(w21_1, t16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U14():
    # 'Charts_Data_M12_Local_Fuel'!U14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!U16,NA())"
    @eval_fn
    def U14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        u16_1 = Dashboard_M12_Local_Fuel.U16()
        var_1 = NA()
        var_2 = IF(w21_1, u16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V14():
    # 'Charts_Data_M12_Local_Fuel'!V14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!V16,NA())"
    @eval_fn
    def V14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        v16_1 = Dashboard_M12_Local_Fuel.V16()
        var_1 = NA()
        var_2 = IF(w21_1, v16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W14():
    # 'Charts_Data_M12_Local_Fuel'!W14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!W16,NA())"
    @eval_fn
    def W14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        w16_1 = Dashboard_M12_Local_Fuel.W16()
        var_1 = NA()
        var_2 = IF(w21_1, w16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X14():
    # 'Charts_Data_M12_Local_Fuel'!X14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!X16,NA())"
    @eval_fn
    def X14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        x16_1 = Dashboard_M12_Local_Fuel.X16()
        var_1 = NA()
        var_2 = IF(w21_1, x16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y14():
    # 'Charts_Data_M12_Local_Fuel'!Y14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!Y16,NA())"
    @eval_fn
    def Y14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        y16_1 = Dashboard_M12_Local_Fuel.Y16()
        var_1 = NA()
        var_2 = IF(w21_1, y16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z14():
    # 'Charts_Data_M12_Local_Fuel'!Z14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!Z16,NA())"
    @eval_fn
    def Z14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        z16_1 = Dashboard_M12_Local_Fuel.Z16()
        var_1 = NA()
        var_2 = IF(w21_1, z16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA14():
    # 'Charts_Data_M12_Local_Fuel'!AA14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AA16,NA())"
    @eval_fn
    def AA14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        aa16_1 = Dashboard_M12_Local_Fuel.AA16()
        var_1 = NA()
        var_2 = IF(w21_1, aa16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB14():
    # 'Charts_Data_M12_Local_Fuel'!AB14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AB16,NA())"
    @eval_fn
    def AB14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        ab16_1 = Dashboard_M12_Local_Fuel.AB16()
        var_1 = NA()
        var_2 = IF(w21_1, ab16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC14():
    # 'Charts_Data_M12_Local_Fuel'!AC14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AC16,NA())"
    @eval_fn
    def AC14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        ac16_1 = Dashboard_M12_Local_Fuel.AC16()
        var_1 = NA()
        var_2 = IF(w21_1, ac16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD14():
    # 'Charts_Data_M12_Local_Fuel'!AD14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AD16,NA())"
    @eval_fn
    def AD14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        ad16_1 = Dashboard_M12_Local_Fuel.AD16()
        var_1 = NA()
        var_2 = IF(w21_1, ad16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE14():
    # 'Charts_Data_M12_Local_Fuel'!AE14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AE16,NA())"
    @eval_fn
    def AE14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        ae16_1 = Dashboard_M12_Local_Fuel.AE16()
        var_1 = NA()
        var_2 = IF(w21_1, ae16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF14():
    # 'Charts_Data_M12_Local_Fuel'!AF14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AF16,NA())"
    @eval_fn
    def AF14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        af16_1 = Dashboard_M12_Local_Fuel.AF16()
        var_1 = NA()
        var_2 = IF(w21_1, af16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG14():
    # 'Charts_Data_M12_Local_Fuel'!AG14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AG16,NA())"
    @eval_fn
    def AG14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        ag16_1 = Dashboard_M12_Local_Fuel.AG16()
        var_1 = NA()
        var_2 = IF(w21_1, ag16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH14():
    # 'Charts_Data_M12_Local_Fuel'!AH14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AH16,NA())"
    @eval_fn
    def AH14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        ah16_1 = Dashboard_M12_Local_Fuel.AH16()
        var_1 = NA()
        var_2 = IF(w21_1, ah16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI14():
    # 'Charts_Data_M12_Local_Fuel'!AI14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AI16,NA())"
    @eval_fn
    def AI14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        ai16_1 = Dashboard_M12_Local_Fuel.AI16()
        var_1 = NA()
        var_2 = IF(w21_1, ai16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ14():
    # 'Charts_Data_M12_Local_Fuel'!AJ14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AJ16,NA())"
    @eval_fn
    def AJ14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        aj16_1 = Dashboard_M12_Local_Fuel.AJ16()
        var_1 = NA()
        var_2 = IF(w21_1, aj16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK14():
    # 'Charts_Data_M12_Local_Fuel'!AK14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AK16,NA())"
    @eval_fn
    def AK14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        ak16_1 = Dashboard_M12_Local_Fuel.AK16()
        var_1 = NA()
        var_2 = IF(w21_1, ak16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL14():
    # 'Charts_Data_M12_Local_Fuel'!AL14
    value = "#REF!"
    formula = "=IF('Charts M12 Local Fuel'!$W$21,'Dashboard M12 Local Fuel'!AL16,NA())"
    @eval_fn
    def AL14():
        w21_1 = Charts_M12_Local_Fuel.W21()
        al16_1 = Dashboard_M12_Local_Fuel.AL16()
        var_1 = NA()
        var_2 = IF(w21_1, al16_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class D15():
    # 'Charts_Data_M12_Local_Fuel'!D15
    value = "Missing"

@register(Charts_Data_M12_Local_Fuel)
class F15():
    # 'Charts_Data_M12_Local_Fuel'!F15
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G15():
    # 'Charts_Data_M12_Local_Fuel'!G15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!G17-SUM('Dashboard M12 Local Fuel'!G11:G16),0)"
    @eval_fn
    def G15():
        g17_1 = Dashboard_M12_Local_Fuel.G17()
        range_1 = Dashboard_M12_Local_Fuel(7, 11, 7, 16)
        var_1 = SUM(range_1)
        var_2 = sub(g17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class H15():
    # 'Charts_Data_M12_Local_Fuel'!H15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!H17-SUM('Dashboard M12 Local Fuel'!H11:H16),0)"
    @eval_fn
    def H15():
        h17_1 = Dashboard_M12_Local_Fuel.H17()
        range_1 = Dashboard_M12_Local_Fuel(8, 11, 8, 16)
        var_1 = SUM(range_1)
        var_2 = sub(h17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class I15():
    # 'Charts_Data_M12_Local_Fuel'!I15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!I17-SUM('Dashboard M12 Local Fuel'!I11:I16),0)"
    @eval_fn
    def I15():
        i17_1 = Dashboard_M12_Local_Fuel.I17()
        range_1 = Dashboard_M12_Local_Fuel(9, 11, 9, 16)
        var_1 = SUM(range_1)
        var_2 = sub(i17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class J15():
    # 'Charts_Data_M12_Local_Fuel'!J15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!J17-SUM('Dashboard M12 Local Fuel'!J11:J16),0)"
    @eval_fn
    def J15():
        j17_1 = Dashboard_M12_Local_Fuel.J17()
        range_1 = Dashboard_M12_Local_Fuel(10, 11, 10, 16)
        var_1 = SUM(range_1)
        var_2 = sub(j17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class K15():
    # 'Charts_Data_M12_Local_Fuel'!K15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!K17-SUM('Dashboard M12 Local Fuel'!K11:K16),0)"
    @eval_fn
    def K15():
        k17_1 = Dashboard_M12_Local_Fuel.K17()
        range_1 = Dashboard_M12_Local_Fuel(11, 11, 11, 16)
        var_1 = SUM(range_1)
        var_2 = sub(k17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class L15():
    # 'Charts_Data_M12_Local_Fuel'!L15
    value = 700100
    formula = "=MAX('Dashboard M12 Local Fuel'!L17-SUM('Dashboard M12 Local Fuel'!L11:L16),0)"
    @eval_fn
    def L15():
        l17_1 = Dashboard_M12_Local_Fuel.L17()
        range_1 = Dashboard_M12_Local_Fuel(12, 11, 12, 16)
        var_1 = SUM(range_1)
        var_2 = sub(l17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class M15():
    # 'Charts_Data_M12_Local_Fuel'!M15
    value = 2531.87907076
    formula = "=MAX('Dashboard M12 Local Fuel'!M17-SUM('Dashboard M12 Local Fuel'!M11:M16),0)"
    @eval_fn
    def M15():
        m17_1 = Dashboard_M12_Local_Fuel.M17()
        range_1 = Dashboard_M12_Local_Fuel(13, 11, 13, 16)
        var_1 = SUM(range_1)
        var_2 = sub(m17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class N15():
    # 'Charts_Data_M12_Local_Fuel'!N15
    value = 3693.20246137
    formula = "=MAX('Dashboard M12 Local Fuel'!N17-SUM('Dashboard M12 Local Fuel'!N11:N16),0)"
    @eval_fn
    def N15():
        n17_1 = Dashboard_M12_Local_Fuel.N17()
        range_1 = Dashboard_M12_Local_Fuel(14, 11, 14, 16)
        var_1 = SUM(range_1)
        var_2 = sub(n17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class O15():
    # 'Charts_Data_M12_Local_Fuel'!O15
    value = 0
    formula = "=MAX('Dashboard M12 Local Fuel'!O17-SUM('Dashboard M12 Local Fuel'!O11:O16),0)"
    @eval_fn
    def O15():
        o17_1 = Dashboard_M12_Local_Fuel.O17()
        range_1 = Dashboard_M12_Local_Fuel(15, 11, 15, 16)
        var_1 = SUM(range_1)
        var_2 = sub(o17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class P15():
    # 'Charts_Data_M12_Local_Fuel'!P15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!P17-SUM('Dashboard M12 Local Fuel'!P11:P16),0)"
    @eval_fn
    def P15():
        p17_1 = Dashboard_M12_Local_Fuel.P17()
        range_1 = Dashboard_M12_Local_Fuel(16, 11, 16, 16)
        var_1 = SUM(range_1)
        var_2 = sub(p17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class Q15():
    # 'Charts_Data_M12_Local_Fuel'!Q15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!Q17-SUM('Dashboard M12 Local Fuel'!Q11:Q16),0)"
    @eval_fn
    def Q15():
        q17_1 = Dashboard_M12_Local_Fuel.Q17()
        range_1 = Dashboard_M12_Local_Fuel(17, 11, 17, 16)
        var_1 = SUM(range_1)
        var_2 = sub(q17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class R15():
    # 'Charts_Data_M12_Local_Fuel'!R15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!R17-SUM('Dashboard M12 Local Fuel'!R11:R16),0)"
    @eval_fn
    def R15():
        r17_1 = Dashboard_M12_Local_Fuel.R17()
        range_1 = Dashboard_M12_Local_Fuel(18, 11, 18, 16)
        var_1 = SUM(range_1)
        var_2 = sub(r17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class S15():
    # 'Charts_Data_M12_Local_Fuel'!S15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!S17-SUM('Dashboard M12 Local Fuel'!S11:S16),0)"
    @eval_fn
    def S15():
        s17_1 = Dashboard_M12_Local_Fuel.S17()
        range_1 = Dashboard_M12_Local_Fuel(19, 11, 19, 16)
        var_1 = SUM(range_1)
        var_2 = sub(s17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class T15():
    # 'Charts_Data_M12_Local_Fuel'!T15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!T17-SUM('Dashboard M12 Local Fuel'!T11:T16),0)"
    @eval_fn
    def T15():
        t17_1 = Dashboard_M12_Local_Fuel.T17()
        range_1 = Dashboard_M12_Local_Fuel(20, 11, 20, 16)
        var_1 = SUM(range_1)
        var_2 = sub(t17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class U15():
    # 'Charts_Data_M12_Local_Fuel'!U15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!U17-SUM('Dashboard M12 Local Fuel'!U11:U16),0)"
    @eval_fn
    def U15():
        u17_1 = Dashboard_M12_Local_Fuel.U17()
        range_1 = Dashboard_M12_Local_Fuel(21, 11, 21, 16)
        var_1 = SUM(range_1)
        var_2 = sub(u17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class V15():
    # 'Charts_Data_M12_Local_Fuel'!V15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!V17-SUM('Dashboard M12 Local Fuel'!V11:V16),0)"
    @eval_fn
    def V15():
        v17_1 = Dashboard_M12_Local_Fuel.V17()
        range_1 = Dashboard_M12_Local_Fuel(22, 11, 22, 16)
        var_1 = SUM(range_1)
        var_2 = sub(v17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class W15():
    # 'Charts_Data_M12_Local_Fuel'!W15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!W17-SUM('Dashboard M12 Local Fuel'!W11:W16),0)"
    @eval_fn
    def W15():
        w17_1 = Dashboard_M12_Local_Fuel.W17()
        range_1 = Dashboard_M12_Local_Fuel(23, 11, 23, 16)
        var_1 = SUM(range_1)
        var_2 = sub(w17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class X15():
    # 'Charts_Data_M12_Local_Fuel'!X15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!X17-SUM('Dashboard M12 Local Fuel'!X11:X16),0)"
    @eval_fn
    def X15():
        x17_1 = Dashboard_M12_Local_Fuel.X17()
        range_1 = Dashboard_M12_Local_Fuel(24, 11, 24, 16)
        var_1 = SUM(range_1)
        var_2 = sub(x17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class Y15():
    # 'Charts_Data_M12_Local_Fuel'!Y15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!Y17-SUM('Dashboard M12 Local Fuel'!Y11:Y16),0)"
    @eval_fn
    def Y15():
        y17_1 = Dashboard_M12_Local_Fuel.Y17()
        range_1 = Dashboard_M12_Local_Fuel(25, 11, 25, 16)
        var_1 = SUM(range_1)
        var_2 = sub(y17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class Z15():
    # 'Charts_Data_M12_Local_Fuel'!Z15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!Z17-SUM('Dashboard M12 Local Fuel'!Z11:Z16),0)"
    @eval_fn
    def Z15():
        z17_1 = Dashboard_M12_Local_Fuel.Z17()
        range_1 = Dashboard_M12_Local_Fuel(26, 11, 26, 16)
        var_1 = SUM(range_1)
        var_2 = sub(z17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AA15():
    # 'Charts_Data_M12_Local_Fuel'!AA15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AA17-SUM('Dashboard M12 Local Fuel'!AA11:AA16),0)"
    @eval_fn
    def AA15():
        aa17_1 = Dashboard_M12_Local_Fuel.AA17()
        range_1 = Dashboard_M12_Local_Fuel(27, 11, 27, 16)
        var_1 = SUM(range_1)
        var_2 = sub(aa17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AB15():
    # 'Charts_Data_M12_Local_Fuel'!AB15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AB17-SUM('Dashboard M12 Local Fuel'!AB11:AB16),0)"
    @eval_fn
    def AB15():
        ab17_1 = Dashboard_M12_Local_Fuel.AB17()
        range_1 = Dashboard_M12_Local_Fuel(28, 11, 28, 16)
        var_1 = SUM(range_1)
        var_2 = sub(ab17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AC15():
    # 'Charts_Data_M12_Local_Fuel'!AC15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AC17-SUM('Dashboard M12 Local Fuel'!AC11:AC16),0)"
    @eval_fn
    def AC15():
        ac17_1 = Dashboard_M12_Local_Fuel.AC17()
        range_1 = Dashboard_M12_Local_Fuel(29, 11, 29, 16)
        var_1 = SUM(range_1)
        var_2 = sub(ac17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AD15():
    # 'Charts_Data_M12_Local_Fuel'!AD15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AD17-SUM('Dashboard M12 Local Fuel'!AD11:AD16),0)"
    @eval_fn
    def AD15():
        ad17_1 = Dashboard_M12_Local_Fuel.AD17()
        range_1 = Dashboard_M12_Local_Fuel(30, 11, 30, 16)
        var_1 = SUM(range_1)
        var_2 = sub(ad17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AE15():
    # 'Charts_Data_M12_Local_Fuel'!AE15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AE17-SUM('Dashboard M12 Local Fuel'!AE11:AE16),0)"
    @eval_fn
    def AE15():
        ae17_1 = Dashboard_M12_Local_Fuel.AE17()
        range_1 = Dashboard_M12_Local_Fuel(31, 11, 31, 16)
        var_1 = SUM(range_1)
        var_2 = sub(ae17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AF15():
    # 'Charts_Data_M12_Local_Fuel'!AF15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AF17-SUM('Dashboard M12 Local Fuel'!AF11:AF16),0)"
    @eval_fn
    def AF15():
        af17_1 = Dashboard_M12_Local_Fuel.AF17()
        range_1 = Dashboard_M12_Local_Fuel(32, 11, 32, 16)
        var_1 = SUM(range_1)
        var_2 = sub(af17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AG15():
    # 'Charts_Data_M12_Local_Fuel'!AG15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AG17-SUM('Dashboard M12 Local Fuel'!AG11:AG16),0)"
    @eval_fn
    def AG15():
        ag17_1 = Dashboard_M12_Local_Fuel.AG17()
        range_1 = Dashboard_M12_Local_Fuel(33, 11, 33, 16)
        var_1 = SUM(range_1)
        var_2 = sub(ag17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AH15():
    # 'Charts_Data_M12_Local_Fuel'!AH15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AH17-SUM('Dashboard M12 Local Fuel'!AH11:AH16),0)"
    @eval_fn
    def AH15():
        ah17_1 = Dashboard_M12_Local_Fuel.AH17()
        range_1 = Dashboard_M12_Local_Fuel(34, 11, 34, 16)
        var_1 = SUM(range_1)
        var_2 = sub(ah17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AI15():
    # 'Charts_Data_M12_Local_Fuel'!AI15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AI17-SUM('Dashboard M12 Local Fuel'!AI11:AI16),0)"
    @eval_fn
    def AI15():
        ai17_1 = Dashboard_M12_Local_Fuel.AI17()
        range_1 = Dashboard_M12_Local_Fuel(35, 11, 35, 16)
        var_1 = SUM(range_1)
        var_2 = sub(ai17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AJ15():
    # 'Charts_Data_M12_Local_Fuel'!AJ15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AJ17-SUM('Dashboard M12 Local Fuel'!AJ11:AJ16),0)"
    @eval_fn
    def AJ15():
        aj17_1 = Dashboard_M12_Local_Fuel.AJ17()
        range_1 = Dashboard_M12_Local_Fuel(36, 11, 36, 16)
        var_1 = SUM(range_1)
        var_2 = sub(aj17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AK15():
    # 'Charts_Data_M12_Local_Fuel'!AK15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AK17-SUM('Dashboard M12 Local Fuel'!AK11:AK16),0)"
    @eval_fn
    def AK15():
        ak17_1 = Dashboard_M12_Local_Fuel.AK17()
        range_1 = Dashboard_M12_Local_Fuel(37, 11, 37, 16)
        var_1 = SUM(range_1)
        var_2 = sub(ak17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class AL15():
    # 'Charts_Data_M12_Local_Fuel'!AL15
    value = "#REF!"
    formula = "=MAX('Dashboard M12 Local Fuel'!AL17-SUM('Dashboard M12 Local Fuel'!AL11:AL16),0)"
    @eval_fn
    def AL15():
        al17_1 = Dashboard_M12_Local_Fuel.AL17()
        range_1 = Dashboard_M12_Local_Fuel(38, 11, 38, 16)
        var_1 = SUM(range_1)
        var_2 = sub(al17_1, var_1)
        var_3 = MAX(var_2, 0)
        return var_3

@register(Charts_Data_M12_Local_Fuel)
class D16():
    # 'Charts_Data_M12_Local_Fuel'!D16
    value = "Total"

@register(Charts_Data_M12_Local_Fuel)
class F16():
    # 'Charts_Data_M12_Local_Fuel'!F16
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G16():
    # 'Charts_Data_M12_Local_Fuel'!G16
    value = 642000
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!G17,NA())"
    @eval_fn
    def G16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        g17_1 = Dashboard_M12_Local_Fuel.G17()
        var_1 = NA()
        var_2 = IF(q21_1, g17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class H16():
    # 'Charts_Data_M12_Local_Fuel'!H16
    value = 681000
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!H17,NA())"
    @eval_fn
    def H16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        h17_1 = Dashboard_M12_Local_Fuel.H17()
        var_1 = NA()
        var_2 = IF(q21_1, h17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class I16():
    # 'Charts_Data_M12_Local_Fuel'!I16
    value = 615000
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!I17,NA())"
    @eval_fn
    def I16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        i17_1 = Dashboard_M12_Local_Fuel.I17()
        var_1 = NA()
        var_2 = IF(q21_1, i17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class J16():
    # 'Charts_Data_M12_Local_Fuel'!J16
    value = 519000
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!J17,NA())"
    @eval_fn
    def J16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        j17_1 = Dashboard_M12_Local_Fuel.J17()
        var_1 = NA()
        var_2 = IF(q21_1, j17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class K16():
    # 'Charts_Data_M12_Local_Fuel'!K16
    value = 676156
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!K17,NA())"
    @eval_fn
    def K16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        k17_1 = Dashboard_M12_Local_Fuel.K17()
        var_1 = NA()
        var_2 = IF(q21_1, k17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class L16():
    # 'Charts_Data_M12_Local_Fuel'!L16
    value = 737938
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!L17,NA())"
    @eval_fn
    def L16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        l17_1 = Dashboard_M12_Local_Fuel.L17()
        var_1 = NA()
        var_2 = IF(q21_1, l17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class M16():
    # 'Charts_Data_M12_Local_Fuel'!M16
    value = 716531.879071
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!M17,NA())"
    @eval_fn
    def M16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        m17_1 = Dashboard_M12_Local_Fuel.M17()
        var_1 = NA()
        var_2 = IF(q21_1, m17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class N16():
    # 'Charts_Data_M12_Local_Fuel'!N16
    value = 865335.202461
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!N17,NA())"
    @eval_fn
    def N16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        n17_1 = Dashboard_M12_Local_Fuel.N17()
        var_1 = NA()
        var_2 = IF(q21_1, n17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class O16():
    # 'Charts_Data_M12_Local_Fuel'!O16
    value = 945908.583396
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!O17,NA())"
    @eval_fn
    def O16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        o17_1 = Dashboard_M12_Local_Fuel.O17()
        var_1 = NA()
        var_2 = IF(q21_1, o17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class P16():
    # 'Charts_Data_M12_Local_Fuel'!P16
    value = 977598.816
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!P17,NA())"
    @eval_fn
    def P16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        p17_1 = Dashboard_M12_Local_Fuel.P17()
        var_1 = NA()
        var_2 = IF(q21_1, p17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Q16():
    # 'Charts_Data_M12_Local_Fuel'!Q16
    value = 964817.264
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!Q17,NA())"
    @eval_fn
    def Q16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        q17_1 = Dashboard_M12_Local_Fuel.Q17()
        var_1 = NA()
        var_2 = IF(q21_1, q17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class R16():
    # 'Charts_Data_M12_Local_Fuel'!R16
    value = 951417.773
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!R17,NA())"
    @eval_fn
    def R16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        r17_1 = Dashboard_M12_Local_Fuel.R17()
        var_1 = NA()
        var_2 = IF(q21_1, r17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class S16():
    # 'Charts_Data_M12_Local_Fuel'!S16
    value = 1189273.11
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!S17,NA())"
    @eval_fn
    def S16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        s17_1 = Dashboard_M12_Local_Fuel.S17()
        var_1 = NA()
        var_2 = IF(q21_1, s17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class T16():
    # 'Charts_Data_M12_Local_Fuel'!T16
    value = 1330297.765
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!T17,NA())"
    @eval_fn
    def T16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        t17_1 = Dashboard_M12_Local_Fuel.T17()
        var_1 = NA()
        var_2 = IF(q21_1, t17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class U16():
    # 'Charts_Data_M12_Local_Fuel'!U16
    value = 1718566.52825
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!U17,NA())"
    @eval_fn
    def U16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        u17_1 = Dashboard_M12_Local_Fuel.U17()
        var_1 = NA()
        var_2 = IF(q21_1, u17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class V16():
    # 'Charts_Data_M12_Local_Fuel'!V16
    value = 2004166.94363
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!V17,NA())"
    @eval_fn
    def V16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        v17_1 = Dashboard_M12_Local_Fuel.V17()
        var_1 = NA()
        var_2 = IF(q21_1, v17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class W16():
    # 'Charts_Data_M12_Local_Fuel'!W16
    value = 2198786
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!W17,NA())"
    @eval_fn
    def W16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        w17_1 = Dashboard_M12_Local_Fuel.W17()
        var_1 = NA()
        var_2 = IF(q21_1, w17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class X16():
    # 'Charts_Data_M12_Local_Fuel'!X16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!X17,NA())"
    @eval_fn
    def X16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        x17_1 = Dashboard_M12_Local_Fuel.X17()
        var_1 = NA()
        var_2 = IF(q21_1, x17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Y16():
    # 'Charts_Data_M12_Local_Fuel'!Y16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!Y17,NA())"
    @eval_fn
    def Y16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        y17_1 = Dashboard_M12_Local_Fuel.Y17()
        var_1 = NA()
        var_2 = IF(q21_1, y17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class Z16():
    # 'Charts_Data_M12_Local_Fuel'!Z16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!Z17,NA())"
    @eval_fn
    def Z16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        z17_1 = Dashboard_M12_Local_Fuel.Z17()
        var_1 = NA()
        var_2 = IF(q21_1, z17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AA16():
    # 'Charts_Data_M12_Local_Fuel'!AA16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AA17,NA())"
    @eval_fn
    def AA16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        aa17_1 = Dashboard_M12_Local_Fuel.AA17()
        var_1 = NA()
        var_2 = IF(q21_1, aa17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AB16():
    # 'Charts_Data_M12_Local_Fuel'!AB16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AB17,NA())"
    @eval_fn
    def AB16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        ab17_1 = Dashboard_M12_Local_Fuel.AB17()
        var_1 = NA()
        var_2 = IF(q21_1, ab17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AC16():
    # 'Charts_Data_M12_Local_Fuel'!AC16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AC17,NA())"
    @eval_fn
    def AC16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        ac17_1 = Dashboard_M12_Local_Fuel.AC17()
        var_1 = NA()
        var_2 = IF(q21_1, ac17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AD16():
    # 'Charts_Data_M12_Local_Fuel'!AD16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AD17,NA())"
    @eval_fn
    def AD16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        ad17_1 = Dashboard_M12_Local_Fuel.AD17()
        var_1 = NA()
        var_2 = IF(q21_1, ad17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AE16():
    # 'Charts_Data_M12_Local_Fuel'!AE16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AE17,NA())"
    @eval_fn
    def AE16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        ae17_1 = Dashboard_M12_Local_Fuel.AE17()
        var_1 = NA()
        var_2 = IF(q21_1, ae17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AF16():
    # 'Charts_Data_M12_Local_Fuel'!AF16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AF17,NA())"
    @eval_fn
    def AF16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        af17_1 = Dashboard_M12_Local_Fuel.AF17()
        var_1 = NA()
        var_2 = IF(q21_1, af17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AG16():
    # 'Charts_Data_M12_Local_Fuel'!AG16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AG17,NA())"
    @eval_fn
    def AG16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        ag17_1 = Dashboard_M12_Local_Fuel.AG17()
        var_1 = NA()
        var_2 = IF(q21_1, ag17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AH16():
    # 'Charts_Data_M12_Local_Fuel'!AH16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AH17,NA())"
    @eval_fn
    def AH16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        ah17_1 = Dashboard_M12_Local_Fuel.AH17()
        var_1 = NA()
        var_2 = IF(q21_1, ah17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AI16():
    # 'Charts_Data_M12_Local_Fuel'!AI16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AI17,NA())"
    @eval_fn
    def AI16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        ai17_1 = Dashboard_M12_Local_Fuel.AI17()
        var_1 = NA()
        var_2 = IF(q21_1, ai17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AJ16():
    # 'Charts_Data_M12_Local_Fuel'!AJ16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AJ17,NA())"
    @eval_fn
    def AJ16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        aj17_1 = Dashboard_M12_Local_Fuel.AJ17()
        var_1 = NA()
        var_2 = IF(q21_1, aj17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AK16():
    # 'Charts_Data_M12_Local_Fuel'!AK16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AK17,NA())"
    @eval_fn
    def AK16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        ak17_1 = Dashboard_M12_Local_Fuel.AK17()
        var_1 = NA()
        var_2 = IF(q21_1, ak17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class AL16():
    # 'Charts_Data_M12_Local_Fuel'!AL16
    value = 0
    formula = "=IF('Charts M12 Local Fuel'!$Q$21,'Dashboard M12 Local Fuel'!AL17,NA())"
    @eval_fn
    def AL16():
        q21_1 = Charts_M12_Local_Fuel.Q21()
        al17_1 = Dashboard_M12_Local_Fuel.AL17()
        var_1 = NA()
        var_2 = IF(q21_1, al17_1, var_1)
        return var_2

@register(Charts_Data_M12_Local_Fuel)
class A17():
    # 'Charts_Data_M12_Local_Fuel'!A17
    value = "Line Graph Input Final"

@register(Charts_Data_M12_Local_Fuel)
class D17():
    # 'Charts_Data_M12_Local_Fuel'!D17
    value = "Hydro"

@register(Charts_Data_M12_Local_Fuel)
class F17():
    # 'Charts_Data_M12_Local_Fuel'!F17
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G17():
    # 'Charts_Data_M12_Local_Fuel'!G17
    value = 0
    formula = "=G9/'Dashboard M12 Local Fuel'!G$7"
    @eval_fn
    def G17():
        g9_1 = Charts_Data_M12_Local_Fuel.G9()
        g7_1 = Dashboard_M12_Local_Fuel.G7()
        var_1 = divide(g9_1, g7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class H17():
    # 'Charts_Data_M12_Local_Fuel'!H17
    value = 0
    formula = "=H9/'Dashboard M12 Local Fuel'!H$7"
    @eval_fn
    def H17():
        h9_1 = Charts_Data_M12_Local_Fuel.H9()
        h7_1 = Dashboard_M12_Local_Fuel.H7()
        var_1 = divide(h9_1, h7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class I17():
    # 'Charts_Data_M12_Local_Fuel'!I17
    value = 0
    formula = "=I9/'Dashboard M12 Local Fuel'!I$7"
    @eval_fn
    def I17():
        i9_1 = Charts_Data_M12_Local_Fuel.I9()
        i7_1 = Dashboard_M12_Local_Fuel.I7()
        var_1 = divide(i9_1, i7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class J17():
    # 'Charts_Data_M12_Local_Fuel'!J17
    value = 0
    formula = "=J9/'Dashboard M12 Local Fuel'!J$7"
    @eval_fn
    def J17():
        j9_1 = Charts_Data_M12_Local_Fuel.J9()
        j7_1 = Dashboard_M12_Local_Fuel.J7()
        var_1 = divide(j9_1, j7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class K17():
    # 'Charts_Data_M12_Local_Fuel'!K17
    value = 0.00249565096838
    formula = "=K9/'Dashboard M12 Local Fuel'!K$7"
    @eval_fn
    def K17():
        k9_1 = Charts_Data_M12_Local_Fuel.K9()
        k7_1 = Dashboard_M12_Local_Fuel.K7()
        var_1 = divide(k9_1, k7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class L17():
    # 'Charts_Data_M12_Local_Fuel'!L17
    value = 0.00355816596764
    formula = "=L9/'Dashboard M12 Local Fuel'!L$7"
    @eval_fn
    def L17():
        l9_1 = Charts_Data_M12_Local_Fuel.L9()
        l7_1 = Dashboard_M12_Local_Fuel.L7()
        var_1 = divide(l9_1, l7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class M17():
    # 'Charts_Data_M12_Local_Fuel'!M17
    value = 0.0144305214552
    formula = "=M9/'Dashboard M12 Local Fuel'!M$7"
    @eval_fn
    def M17():
        m9_1 = Charts_Data_M12_Local_Fuel.M9()
        m7_1 = Dashboard_M12_Local_Fuel.M7()
        var_1 = divide(m9_1, m7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class N17():
    # 'Charts_Data_M12_Local_Fuel'!N17
    value = 0.016241531816
    formula = "=N9/'Dashboard M12 Local Fuel'!N$7"
    @eval_fn
    def N17():
        n9_1 = Charts_Data_M12_Local_Fuel.N9()
        n7_1 = Dashboard_M12_Local_Fuel.N7()
        var_1 = divide(n9_1, n7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class O17():
    # 'Charts_Data_M12_Local_Fuel'!O17
    value = 0.0129783947157
    formula = "=O9/'Dashboard M12 Local Fuel'!O$7"
    @eval_fn
    def O17():
        o9_1 = Charts_Data_M12_Local_Fuel.O9()
        o7_1 = Dashboard_M12_Local_Fuel.O7()
        var_1 = divide(o9_1, o7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class P17():
    # 'Charts_Data_M12_Local_Fuel'!P17
    value = 0.00744931801734
    formula = "=P9/'Dashboard M12 Local Fuel'!P$7"
    @eval_fn
    def P17():
        p9_1 = Charts_Data_M12_Local_Fuel.P9()
        p7_1 = Dashboard_M12_Local_Fuel.P7()
        var_1 = divide(p9_1, p7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Q17():
    # 'Charts_Data_M12_Local_Fuel'!Q17
    value = 0.0105247456842
    formula = "=Q9/'Dashboard M12 Local Fuel'!Q$7"
    @eval_fn
    def Q17():
        q9_1 = Charts_Data_M12_Local_Fuel.Q9()
        q7_1 = Dashboard_M12_Local_Fuel.Q7()
        var_1 = divide(q9_1, q7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class R17():
    # 'Charts_Data_M12_Local_Fuel'!R17
    value = 0.00698446418812
    formula = "=R9/'Dashboard M12 Local Fuel'!R$7"
    @eval_fn
    def R17():
        r9_1 = Charts_Data_M12_Local_Fuel.R9()
        r7_1 = Dashboard_M12_Local_Fuel.R7()
        var_1 = divide(r9_1, r7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class S17():
    # 'Charts_Data_M12_Local_Fuel'!S17
    value = 0.00905327256635
    formula = "=S9/'Dashboard M12 Local Fuel'!S$7"
    @eval_fn
    def S17():
        s9_1 = Charts_Data_M12_Local_Fuel.S9()
        s7_1 = Dashboard_M12_Local_Fuel.S7()
        var_1 = divide(s9_1, s7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class T17():
    # 'Charts_Data_M12_Local_Fuel'!T17
    value = 0.0107870417727
    formula = "=T9/'Dashboard M12 Local Fuel'!T$7"
    @eval_fn
    def T17():
        t9_1 = Charts_Data_M12_Local_Fuel.T9()
        t7_1 = Dashboard_M12_Local_Fuel.T7()
        var_1 = divide(t9_1, t7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class U17():
    # 'Charts_Data_M12_Local_Fuel'!U17
    value = 0.00773666662772
    formula = "=U9/'Dashboard M12 Local Fuel'!U$7"
    @eval_fn
    def U17():
        u9_1 = Charts_Data_M12_Local_Fuel.U9()
        u7_1 = Dashboard_M12_Local_Fuel.U7()
        var_1 = divide(u9_1, u7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class V17():
    # 'Charts_Data_M12_Local_Fuel'!V17
    value = 0.00908404125549
    formula = "=V9/'Dashboard M12 Local Fuel'!V$7"
    @eval_fn
    def V17():
        v9_1 = Charts_Data_M12_Local_Fuel.V9()
        v7_1 = Dashboard_M12_Local_Fuel.V7()
        var_1 = divide(v9_1, v7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class W17():
    # 'Charts_Data_M12_Local_Fuel'!W17
    value = 0.0113684972034
    formula = "=W9/'Dashboard M12 Local Fuel'!W$7"
    @eval_fn
    def W17():
        w9_1 = Charts_Data_M12_Local_Fuel.W9()
        w7_1 = Dashboard_M12_Local_Fuel.W7()
        var_1 = divide(w9_1, w7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class X17():
    # 'Charts_Data_M12_Local_Fuel'!X17
    value = "#DIV/0!"
    formula = "=X9/'Dashboard M12 Local Fuel'!X$7"
    @eval_fn
    def X17():
        x9_1 = Charts_Data_M12_Local_Fuel.X9()
        x7_1 = Dashboard_M12_Local_Fuel.X7()
        var_1 = divide(x9_1, x7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Y17():
    # 'Charts_Data_M12_Local_Fuel'!Y17
    value = "#DIV/0!"
    formula = "=Y9/'Dashboard M12 Local Fuel'!Y$7"
    @eval_fn
    def Y17():
        y9_1 = Charts_Data_M12_Local_Fuel.Y9()
        y7_1 = Dashboard_M12_Local_Fuel.Y7()
        var_1 = divide(y9_1, y7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Z17():
    # 'Charts_Data_M12_Local_Fuel'!Z17
    value = "#DIV/0!"
    formula = "=Z9/'Dashboard M12 Local Fuel'!Z$7"
    @eval_fn
    def Z17():
        z9_1 = Charts_Data_M12_Local_Fuel.Z9()
        z7_1 = Dashboard_M12_Local_Fuel.Z7()
        var_1 = divide(z9_1, z7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AA17():
    # 'Charts_Data_M12_Local_Fuel'!AA17
    value = "#DIV/0!"
    formula = "=AA9/'Dashboard M12 Local Fuel'!AA$7"
    @eval_fn
    def AA17():
        aa9_1 = Charts_Data_M12_Local_Fuel.AA9()
        aa7_1 = Dashboard_M12_Local_Fuel.AA7()
        var_1 = divide(aa9_1, aa7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AB17():
    # 'Charts_Data_M12_Local_Fuel'!AB17
    value = "#DIV/0!"
    formula = "=AB9/'Dashboard M12 Local Fuel'!AB$7"
    @eval_fn
    def AB17():
        ab9_1 = Charts_Data_M12_Local_Fuel.AB9()
        ab7_1 = Dashboard_M12_Local_Fuel.AB7()
        var_1 = divide(ab9_1, ab7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AC17():
    # 'Charts_Data_M12_Local_Fuel'!AC17
    value = "#DIV/0!"
    formula = "=AC9/'Dashboard M12 Local Fuel'!AC$7"
    @eval_fn
    def AC17():
        ac9_1 = Charts_Data_M12_Local_Fuel.AC9()
        ac7_1 = Dashboard_M12_Local_Fuel.AC7()
        var_1 = divide(ac9_1, ac7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AD17():
    # 'Charts_Data_M12_Local_Fuel'!AD17
    value = "#DIV/0!"
    formula = "=AD9/'Dashboard M12 Local Fuel'!AD$7"
    @eval_fn
    def AD17():
        ad9_1 = Charts_Data_M12_Local_Fuel.AD9()
        ad7_1 = Dashboard_M12_Local_Fuel.AD7()
        var_1 = divide(ad9_1, ad7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AE17():
    # 'Charts_Data_M12_Local_Fuel'!AE17
    value = "#DIV/0!"
    formula = "=AE9/'Dashboard M12 Local Fuel'!AE$7"
    @eval_fn
    def AE17():
        ae9_1 = Charts_Data_M12_Local_Fuel.AE9()
        ae7_1 = Dashboard_M12_Local_Fuel.AE7()
        var_1 = divide(ae9_1, ae7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AF17():
    # 'Charts_Data_M12_Local_Fuel'!AF17
    value = "#DIV/0!"
    formula = "=AF9/'Dashboard M12 Local Fuel'!AF$7"
    @eval_fn
    def AF17():
        af9_1 = Charts_Data_M12_Local_Fuel.AF9()
        af7_1 = Dashboard_M12_Local_Fuel.AF7()
        var_1 = divide(af9_1, af7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AG17():
    # 'Charts_Data_M12_Local_Fuel'!AG17
    value = "#DIV/0!"
    formula = "=AG9/'Dashboard M12 Local Fuel'!AG$7"
    @eval_fn
    def AG17():
        ag9_1 = Charts_Data_M12_Local_Fuel.AG9()
        ag7_1 = Dashboard_M12_Local_Fuel.AG7()
        var_1 = divide(ag9_1, ag7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AH17():
    # 'Charts_Data_M12_Local_Fuel'!AH17
    value = "#DIV/0!"
    formula = "=AH9/'Dashboard M12 Local Fuel'!AH$7"
    @eval_fn
    def AH17():
        ah9_1 = Charts_Data_M12_Local_Fuel.AH9()
        ah7_1 = Dashboard_M12_Local_Fuel.AH7()
        var_1 = divide(ah9_1, ah7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AI17():
    # 'Charts_Data_M12_Local_Fuel'!AI17
    value = "#DIV/0!"
    formula = "=AI9/'Dashboard M12 Local Fuel'!AI$7"
    @eval_fn
    def AI17():
        ai9_1 = Charts_Data_M12_Local_Fuel.AI9()
        ai7_1 = Dashboard_M12_Local_Fuel.AI7()
        var_1 = divide(ai9_1, ai7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AJ17():
    # 'Charts_Data_M12_Local_Fuel'!AJ17
    value = "#DIV/0!"
    formula = "=AJ9/'Dashboard M12 Local Fuel'!AJ$7"
    @eval_fn
    def AJ17():
        aj9_1 = Charts_Data_M12_Local_Fuel.AJ9()
        aj7_1 = Dashboard_M12_Local_Fuel.AJ7()
        var_1 = divide(aj9_1, aj7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AK17():
    # 'Charts_Data_M12_Local_Fuel'!AK17
    value = "#DIV/0!"
    formula = "=AK9/'Dashboard M12 Local Fuel'!AK$7"
    @eval_fn
    def AK17():
        ak9_1 = Charts_Data_M12_Local_Fuel.AK9()
        ak7_1 = Dashboard_M12_Local_Fuel.AK7()
        var_1 = divide(ak9_1, ak7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AL17():
    # 'Charts_Data_M12_Local_Fuel'!AL17
    value = "#DIV/0!"
    formula = "=AL9/'Dashboard M12 Local Fuel'!AL$7"
    @eval_fn
    def AL17():
        al9_1 = Charts_Data_M12_Local_Fuel.AL9()
        al7_1 = Dashboard_M12_Local_Fuel.AL7()
        var_1 = divide(al9_1, al7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class D18():
    # 'Charts_Data_M12_Local_Fuel'!D18
    value = "Geothermal"

@register(Charts_Data_M12_Local_Fuel)
class F18():
    # 'Charts_Data_M12_Local_Fuel'!F18
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G18():
    # 'Charts_Data_M12_Local_Fuel'!G18
    value = 0
    formula = "=G10/'Dashboard M12 Local Fuel'!G$7"
    @eval_fn
    def G18():
        g10_1 = Charts_Data_M12_Local_Fuel.G10()
        g7_1 = Dashboard_M12_Local_Fuel.G7()
        var_1 = divide(g10_1, g7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class H18():
    # 'Charts_Data_M12_Local_Fuel'!H18
    value = 0
    formula = "=H10/'Dashboard M12 Local Fuel'!H$7"
    @eval_fn
    def H18():
        h10_1 = Charts_Data_M12_Local_Fuel.H10()
        h7_1 = Dashboard_M12_Local_Fuel.H7()
        var_1 = divide(h10_1, h7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class I18():
    # 'Charts_Data_M12_Local_Fuel'!I18
    value = 0
    formula = "=I10/'Dashboard M12 Local Fuel'!I$7"
    @eval_fn
    def I18():
        i10_1 = Charts_Data_M12_Local_Fuel.I10()
        i7_1 = Dashboard_M12_Local_Fuel.I7()
        var_1 = divide(i10_1, i7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class J18():
    # 'Charts_Data_M12_Local_Fuel'!J18
    value = 0
    formula = "=J10/'Dashboard M12 Local Fuel'!J$7"
    @eval_fn
    def J18():
        j10_1 = Charts_Data_M12_Local_Fuel.J10()
        j7_1 = Dashboard_M12_Local_Fuel.J7()
        var_1 = divide(j10_1, j7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class K18():
    # 'Charts_Data_M12_Local_Fuel'!K18
    value = 0
    formula = "=K10/'Dashboard M12 Local Fuel'!K$7"
    @eval_fn
    def K18():
        k10_1 = Charts_Data_M12_Local_Fuel.K10()
        k7_1 = Dashboard_M12_Local_Fuel.K7()
        var_1 = divide(k10_1, k7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class L18():
    # 'Charts_Data_M12_Local_Fuel'!L18
    value = 0
    formula = "=L10/'Dashboard M12 Local Fuel'!L$7"
    @eval_fn
    def L18():
        l10_1 = Charts_Data_M12_Local_Fuel.L10()
        l7_1 = Dashboard_M12_Local_Fuel.L7()
        var_1 = divide(l10_1, l7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class M18():
    # 'Charts_Data_M12_Local_Fuel'!M18
    value = 0.0209136620627
    formula = "=M10/'Dashboard M12 Local Fuel'!M$7"
    @eval_fn
    def M18():
        m10_1 = Charts_Data_M12_Local_Fuel.M10()
        m7_1 = Dashboard_M12_Local_Fuel.M7()
        var_1 = divide(m10_1, m7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class N18():
    # 'Charts_Data_M12_Local_Fuel'!N18
    value = 0.0200047917138
    formula = "=N10/'Dashboard M12 Local Fuel'!N$7"
    @eval_fn
    def N18():
        n10_1 = Charts_Data_M12_Local_Fuel.N10()
        n7_1 = Dashboard_M12_Local_Fuel.N7()
        var_1 = divide(n10_1, n7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class O18():
    # 'Charts_Data_M12_Local_Fuel'!O18
    value = 0.021668027356
    formula = "=O10/'Dashboard M12 Local Fuel'!O$7"
    @eval_fn
    def O18():
        o10_1 = Charts_Data_M12_Local_Fuel.O10()
        o7_1 = Dashboard_M12_Local_Fuel.O7()
        var_1 = divide(o10_1, o7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class P18():
    # 'Charts_Data_M12_Local_Fuel'!P18
    value = 0.0225036223366
    formula = "=P10/'Dashboard M12 Local Fuel'!P$7"
    @eval_fn
    def P18():
        p10_1 = Charts_Data_M12_Local_Fuel.P10()
        p7_1 = Dashboard_M12_Local_Fuel.P7()
        var_1 = divide(p10_1, p7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Q18():
    # 'Charts_Data_M12_Local_Fuel'!Q18
    value = 0.0165111455232
    formula = "=Q10/'Dashboard M12 Local Fuel'!Q$7"
    @eval_fn
    def Q18():
        q10_1 = Charts_Data_M12_Local_Fuel.Q10()
        q7_1 = Dashboard_M12_Local_Fuel.Q7()
        var_1 = divide(q10_1, q7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class R18():
    # 'Charts_Data_M12_Local_Fuel'!R18
    value = 0.0200866992266
    formula = "=R10/'Dashboard M12 Local Fuel'!R$7"
    @eval_fn
    def R18():
        r10_1 = Charts_Data_M12_Local_Fuel.R10()
        r7_1 = Dashboard_M12_Local_Fuel.R7()
        var_1 = divide(r10_1, r7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class S18():
    # 'Charts_Data_M12_Local_Fuel'!S18
    value = 0.0233188624613
    formula = "=S10/'Dashboard M12 Local Fuel'!S$7"
    @eval_fn
    def S18():
        s10_1 = Charts_Data_M12_Local_Fuel.S10()
        s7_1 = Dashboard_M12_Local_Fuel.S7()
        var_1 = divide(s10_1, s7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class T18():
    # 'Charts_Data_M12_Local_Fuel'!T18
    value = 0.0276200473112
    formula = "=T10/'Dashboard M12 Local Fuel'!T$7"
    @eval_fn
    def T18():
        t10_1 = Charts_Data_M12_Local_Fuel.T10()
        t7_1 = Dashboard_M12_Local_Fuel.T7()
        var_1 = divide(t10_1, t7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class U18():
    # 'Charts_Data_M12_Local_Fuel'!U18
    value = 0.0296197522974
    formula = "=U10/'Dashboard M12 Local Fuel'!U$7"
    @eval_fn
    def U18():
        u10_1 = Charts_Data_M12_Local_Fuel.U10()
        u7_1 = Dashboard_M12_Local_Fuel.U7()
        var_1 = divide(u10_1, u7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class V18():
    # 'Charts_Data_M12_Local_Fuel'!V18
    value = 0.0271127471065
    formula = "=V10/'Dashboard M12 Local Fuel'!V$7"
    @eval_fn
    def V18():
        v10_1 = Charts_Data_M12_Local_Fuel.V10()
        v7_1 = Dashboard_M12_Local_Fuel.V7()
        var_1 = divide(v10_1, v7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class W18():
    # 'Charts_Data_M12_Local_Fuel'!W18
    value = 0.0245505814726
    formula = "=W10/'Dashboard M12 Local Fuel'!W$7"
    @eval_fn
    def W18():
        w10_1 = Charts_Data_M12_Local_Fuel.W10()
        w7_1 = Dashboard_M12_Local_Fuel.W7()
        var_1 = divide(w10_1, w7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class X18():
    # 'Charts_Data_M12_Local_Fuel'!X18
    value = "#DIV/0!"
    formula = "=X10/'Dashboard M12 Local Fuel'!X$7"
    @eval_fn
    def X18():
        x10_1 = Charts_Data_M12_Local_Fuel.X10()
        x7_1 = Dashboard_M12_Local_Fuel.X7()
        var_1 = divide(x10_1, x7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Y18():
    # 'Charts_Data_M12_Local_Fuel'!Y18
    value = "#DIV/0!"
    formula = "=Y10/'Dashboard M12 Local Fuel'!Y$7"
    @eval_fn
    def Y18():
        y10_1 = Charts_Data_M12_Local_Fuel.Y10()
        y7_1 = Dashboard_M12_Local_Fuel.Y7()
        var_1 = divide(y10_1, y7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Z18():
    # 'Charts_Data_M12_Local_Fuel'!Z18
    value = "#DIV/0!"
    formula = "=Z10/'Dashboard M12 Local Fuel'!Z$7"
    @eval_fn
    def Z18():
        z10_1 = Charts_Data_M12_Local_Fuel.Z10()
        z7_1 = Dashboard_M12_Local_Fuel.Z7()
        var_1 = divide(z10_1, z7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AA18():
    # 'Charts_Data_M12_Local_Fuel'!AA18
    value = "#DIV/0!"
    formula = "=AA10/'Dashboard M12 Local Fuel'!AA$7"
    @eval_fn
    def AA18():
        aa10_1 = Charts_Data_M12_Local_Fuel.AA10()
        aa7_1 = Dashboard_M12_Local_Fuel.AA7()
        var_1 = divide(aa10_1, aa7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AB18():
    # 'Charts_Data_M12_Local_Fuel'!AB18
    value = "#DIV/0!"
    formula = "=AB10/'Dashboard M12 Local Fuel'!AB$7"
    @eval_fn
    def AB18():
        ab10_1 = Charts_Data_M12_Local_Fuel.AB10()
        ab7_1 = Dashboard_M12_Local_Fuel.AB7()
        var_1 = divide(ab10_1, ab7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AC18():
    # 'Charts_Data_M12_Local_Fuel'!AC18
    value = "#DIV/0!"
    formula = "=AC10/'Dashboard M12 Local Fuel'!AC$7"
    @eval_fn
    def AC18():
        ac10_1 = Charts_Data_M12_Local_Fuel.AC10()
        ac7_1 = Dashboard_M12_Local_Fuel.AC7()
        var_1 = divide(ac10_1, ac7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AD18():
    # 'Charts_Data_M12_Local_Fuel'!AD18
    value = "#DIV/0!"
    formula = "=AD10/'Dashboard M12 Local Fuel'!AD$7"
    @eval_fn
    def AD18():
        ad10_1 = Charts_Data_M12_Local_Fuel.AD10()
        ad7_1 = Dashboard_M12_Local_Fuel.AD7()
        var_1 = divide(ad10_1, ad7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AE18():
    # 'Charts_Data_M12_Local_Fuel'!AE18
    value = "#DIV/0!"
    formula = "=AE10/'Dashboard M12 Local Fuel'!AE$7"
    @eval_fn
    def AE18():
        ae10_1 = Charts_Data_M12_Local_Fuel.AE10()
        ae7_1 = Dashboard_M12_Local_Fuel.AE7()
        var_1 = divide(ae10_1, ae7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AF18():
    # 'Charts_Data_M12_Local_Fuel'!AF18
    value = "#DIV/0!"
    formula = "=AF10/'Dashboard M12 Local Fuel'!AF$7"
    @eval_fn
    def AF18():
        af10_1 = Charts_Data_M12_Local_Fuel.AF10()
        af7_1 = Dashboard_M12_Local_Fuel.AF7()
        var_1 = divide(af10_1, af7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AG18():
    # 'Charts_Data_M12_Local_Fuel'!AG18
    value = "#DIV/0!"
    formula = "=AG10/'Dashboard M12 Local Fuel'!AG$7"
    @eval_fn
    def AG18():
        ag10_1 = Charts_Data_M12_Local_Fuel.AG10()
        ag7_1 = Dashboard_M12_Local_Fuel.AG7()
        var_1 = divide(ag10_1, ag7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AH18():
    # 'Charts_Data_M12_Local_Fuel'!AH18
    value = "#DIV/0!"
    formula = "=AH10/'Dashboard M12 Local Fuel'!AH$7"
    @eval_fn
    def AH18():
        ah10_1 = Charts_Data_M12_Local_Fuel.AH10()
        ah7_1 = Dashboard_M12_Local_Fuel.AH7()
        var_1 = divide(ah10_1, ah7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AI18():
    # 'Charts_Data_M12_Local_Fuel'!AI18
    value = "#DIV/0!"
    formula = "=AI10/'Dashboard M12 Local Fuel'!AI$7"
    @eval_fn
    def AI18():
        ai10_1 = Charts_Data_M12_Local_Fuel.AI10()
        ai7_1 = Dashboard_M12_Local_Fuel.AI7()
        var_1 = divide(ai10_1, ai7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AJ18():
    # 'Charts_Data_M12_Local_Fuel'!AJ18
    value = "#DIV/0!"
    formula = "=AJ10/'Dashboard M12 Local Fuel'!AJ$7"
    @eval_fn
    def AJ18():
        aj10_1 = Charts_Data_M12_Local_Fuel.AJ10()
        aj7_1 = Dashboard_M12_Local_Fuel.AJ7()
        var_1 = divide(aj10_1, aj7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AK18():
    # 'Charts_Data_M12_Local_Fuel'!AK18
    value = "#DIV/0!"
    formula = "=AK10/'Dashboard M12 Local Fuel'!AK$7"
    @eval_fn
    def AK18():
        ak10_1 = Charts_Data_M12_Local_Fuel.AK10()
        ak7_1 = Dashboard_M12_Local_Fuel.AK7()
        var_1 = divide(ak10_1, ak7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AL18():
    # 'Charts_Data_M12_Local_Fuel'!AL18
    value = "#DIV/0!"
    formula = "=AL10/'Dashboard M12 Local Fuel'!AL$7"
    @eval_fn
    def AL18():
        al10_1 = Charts_Data_M12_Local_Fuel.AL10()
        al7_1 = Dashboard_M12_Local_Fuel.AL7()
        var_1 = divide(al10_1, al7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class D19():
    # 'Charts_Data_M12_Local_Fuel'!D19
    value = "Wind "

@register(Charts_Data_M12_Local_Fuel)
class F19():
    # 'Charts_Data_M12_Local_Fuel'!F19
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G19():
    # 'Charts_Data_M12_Local_Fuel'!G19
    value = 0
    formula = "=G11/'Dashboard M12 Local Fuel'!G$7"
    @eval_fn
    def G19():
        g11_1 = Charts_Data_M12_Local_Fuel.G11()
        g7_1 = Dashboard_M12_Local_Fuel.G7()
        var_1 = divide(g11_1, g7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class H19():
    # 'Charts_Data_M12_Local_Fuel'!H19
    value = 0
    formula = "=H11/'Dashboard M12 Local Fuel'!H$7"
    @eval_fn
    def H19():
        h11_1 = Charts_Data_M12_Local_Fuel.H11()
        h7_1 = Dashboard_M12_Local_Fuel.H7()
        var_1 = divide(h11_1, h7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class I19():
    # 'Charts_Data_M12_Local_Fuel'!I19
    value = 0
    formula = "=I11/'Dashboard M12 Local Fuel'!I$7"
    @eval_fn
    def I19():
        i11_1 = Charts_Data_M12_Local_Fuel.I11()
        i7_1 = Dashboard_M12_Local_Fuel.I7()
        var_1 = divide(i11_1, i7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class J19():
    # 'Charts_Data_M12_Local_Fuel'!J19
    value = 0
    formula = "=J11/'Dashboard M12 Local Fuel'!J$7"
    @eval_fn
    def J19():
        j11_1 = Charts_Data_M12_Local_Fuel.J11()
        j7_1 = Dashboard_M12_Local_Fuel.J7()
        var_1 = divide(j11_1, j7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class K19():
    # 'Charts_Data_M12_Local_Fuel'!K19
    value = 0
    formula = "=K11/'Dashboard M12 Local Fuel'!K$7"
    @eval_fn
    def K19():
        k11_1 = Charts_Data_M12_Local_Fuel.K11()
        k7_1 = Dashboard_M12_Local_Fuel.K7()
        var_1 = divide(k11_1, k7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class L19():
    # 'Charts_Data_M12_Local_Fuel'!L19
    value = 0
    formula = "=L11/'Dashboard M12 Local Fuel'!L$7"
    @eval_fn
    def L19():
        l11_1 = Charts_Data_M12_Local_Fuel.L11()
        l7_1 = Dashboard_M12_Local_Fuel.L7()
        var_1 = divide(l11_1, l7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class M19():
    # 'Charts_Data_M12_Local_Fuel'!M19
    value = 0.000662423685243
    formula = "=M11/'Dashboard M12 Local Fuel'!M$7"
    @eval_fn
    def M19():
        m11_1 = Charts_Data_M12_Local_Fuel.M11()
        m7_1 = Dashboard_M12_Local_Fuel.M7()
        var_1 = divide(m11_1, m7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class N19():
    # 'Charts_Data_M12_Local_Fuel'!N19
    value = 0.00773770245533
    formula = "=N11/'Dashboard M12 Local Fuel'!N$7"
    @eval_fn
    def N19():
        n11_1 = Charts_Data_M12_Local_Fuel.N11()
        n7_1 = Dashboard_M12_Local_Fuel.N7()
        var_1 = divide(n11_1, n7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class O19():
    # 'Charts_Data_M12_Local_Fuel'!O19
    value = 0.0228362166569
    formula = "=O11/'Dashboard M12 Local Fuel'!O$7"
    @eval_fn
    def O19():
        o11_1 = Charts_Data_M12_Local_Fuel.O11()
        o7_1 = Dashboard_M12_Local_Fuel.O7()
        var_1 = divide(o11_1, o7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class P19():
    # 'Charts_Data_M12_Local_Fuel'!P19
    value = 0.0227877817778
    formula = "=P11/'Dashboard M12 Local Fuel'!P$7"
    @eval_fn
    def P19():
        p11_1 = Charts_Data_M12_Local_Fuel.P11()
        p7_1 = Dashboard_M12_Local_Fuel.P7()
        var_1 = divide(p11_1, p7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Q19():
    # 'Charts_Data_M12_Local_Fuel'!Q19
    value = 0.0246650944112
    formula = "=Q11/'Dashboard M12 Local Fuel'!Q$7"
    @eval_fn
    def Q19():
        q11_1 = Charts_Data_M12_Local_Fuel.Q11()
        q7_1 = Dashboard_M12_Local_Fuel.Q7()
        var_1 = divide(q11_1, q7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class R19():
    # 'Charts_Data_M12_Local_Fuel'!R19
    value = 0.0260273051248
    formula = "=R11/'Dashboard M12 Local Fuel'!R$7"
    @eval_fn
    def R19():
        r11_1 = Charts_Data_M12_Local_Fuel.R11()
        r7_1 = Dashboard_M12_Local_Fuel.R7()
        var_1 = divide(r11_1, r7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class S19():
    # 'Charts_Data_M12_Local_Fuel'!S19
    value = 0.0344793890195
    formula = "=S11/'Dashboard M12 Local Fuel'!S$7"
    @eval_fn
    def S19():
        s11_1 = Charts_Data_M12_Local_Fuel.S11()
        s7_1 = Dashboard_M12_Local_Fuel.S7()
        var_1 = divide(s11_1, s7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class T19():
    # 'Charts_Data_M12_Local_Fuel'!T19
    value = 0.0402790368204
    formula = "=T11/'Dashboard M12 Local Fuel'!T$7"
    @eval_fn
    def T19():
        t11_1 = Charts_Data_M12_Local_Fuel.T11()
        t7_1 = Dashboard_M12_Local_Fuel.T7()
        var_1 = divide(t11_1, t7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class U19():
    # 'Charts_Data_M12_Local_Fuel'!U19
    value = 0.0529995239444
    formula = "=U11/'Dashboard M12 Local Fuel'!U$7"
    @eval_fn
    def U19():
        u11_1 = Charts_Data_M12_Local_Fuel.U11()
        u7_1 = Dashboard_M12_Local_Fuel.U7()
        var_1 = divide(u11_1, u7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class V19():
    # 'Charts_Data_M12_Local_Fuel'!V19
    value = 0.0614349140766
    formula = "=V11/'Dashboard M12 Local Fuel'!V$7"
    @eval_fn
    def V19():
        v11_1 = Charts_Data_M12_Local_Fuel.V11()
        v7_1 = Dashboard_M12_Local_Fuel.V7()
        var_1 = divide(v11_1, v7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class W19():
    # 'Charts_Data_M12_Local_Fuel'!W19
    value = 0.065268790496
    formula = "=W11/'Dashboard M12 Local Fuel'!W$7"
    @eval_fn
    def W19():
        w11_1 = Charts_Data_M12_Local_Fuel.W11()
        w7_1 = Dashboard_M12_Local_Fuel.W7()
        var_1 = divide(w11_1, w7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class X19():
    # 'Charts_Data_M12_Local_Fuel'!X19
    value = "#DIV/0!"
    formula = "=X11/'Dashboard M12 Local Fuel'!X$7"
    @eval_fn
    def X19():
        x11_1 = Charts_Data_M12_Local_Fuel.X11()
        x7_1 = Dashboard_M12_Local_Fuel.X7()
        var_1 = divide(x11_1, x7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Y19():
    # 'Charts_Data_M12_Local_Fuel'!Y19
    value = "#DIV/0!"
    formula = "=Y11/'Dashboard M12 Local Fuel'!Y$7"
    @eval_fn
    def Y19():
        y11_1 = Charts_Data_M12_Local_Fuel.Y11()
        y7_1 = Dashboard_M12_Local_Fuel.Y7()
        var_1 = divide(y11_1, y7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Z19():
    # 'Charts_Data_M12_Local_Fuel'!Z19
    value = "#DIV/0!"
    formula = "=Z11/'Dashboard M12 Local Fuel'!Z$7"
    @eval_fn
    def Z19():
        z11_1 = Charts_Data_M12_Local_Fuel.Z11()
        z7_1 = Dashboard_M12_Local_Fuel.Z7()
        var_1 = divide(z11_1, z7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AA19():
    # 'Charts_Data_M12_Local_Fuel'!AA19
    value = "#DIV/0!"
    formula = "=AA11/'Dashboard M12 Local Fuel'!AA$7"
    @eval_fn
    def AA19():
        aa11_1 = Charts_Data_M12_Local_Fuel.AA11()
        aa7_1 = Dashboard_M12_Local_Fuel.AA7()
        var_1 = divide(aa11_1, aa7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AB19():
    # 'Charts_Data_M12_Local_Fuel'!AB19
    value = "#DIV/0!"
    formula = "=AB11/'Dashboard M12 Local Fuel'!AB$7"
    @eval_fn
    def AB19():
        ab11_1 = Charts_Data_M12_Local_Fuel.AB11()
        ab7_1 = Dashboard_M12_Local_Fuel.AB7()
        var_1 = divide(ab11_1, ab7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AC19():
    # 'Charts_Data_M12_Local_Fuel'!AC19
    value = "#DIV/0!"
    formula = "=AC11/'Dashboard M12 Local Fuel'!AC$7"
    @eval_fn
    def AC19():
        ac11_1 = Charts_Data_M12_Local_Fuel.AC11()
        ac7_1 = Dashboard_M12_Local_Fuel.AC7()
        var_1 = divide(ac11_1, ac7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AD19():
    # 'Charts_Data_M12_Local_Fuel'!AD19
    value = "#DIV/0!"
    formula = "=AD11/'Dashboard M12 Local Fuel'!AD$7"
    @eval_fn
    def AD19():
        ad11_1 = Charts_Data_M12_Local_Fuel.AD11()
        ad7_1 = Dashboard_M12_Local_Fuel.AD7()
        var_1 = divide(ad11_1, ad7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AE19():
    # 'Charts_Data_M12_Local_Fuel'!AE19
    value = "#DIV/0!"
    formula = "=AE11/'Dashboard M12 Local Fuel'!AE$7"
    @eval_fn
    def AE19():
        ae11_1 = Charts_Data_M12_Local_Fuel.AE11()
        ae7_1 = Dashboard_M12_Local_Fuel.AE7()
        var_1 = divide(ae11_1, ae7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AF19():
    # 'Charts_Data_M12_Local_Fuel'!AF19
    value = "#DIV/0!"
    formula = "=AF11/'Dashboard M12 Local Fuel'!AF$7"
    @eval_fn
    def AF19():
        af11_1 = Charts_Data_M12_Local_Fuel.AF11()
        af7_1 = Dashboard_M12_Local_Fuel.AF7()
        var_1 = divide(af11_1, af7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AG19():
    # 'Charts_Data_M12_Local_Fuel'!AG19
    value = "#DIV/0!"
    formula = "=AG11/'Dashboard M12 Local Fuel'!AG$7"
    @eval_fn
    def AG19():
        ag11_1 = Charts_Data_M12_Local_Fuel.AG11()
        ag7_1 = Dashboard_M12_Local_Fuel.AG7()
        var_1 = divide(ag11_1, ag7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AH19():
    # 'Charts_Data_M12_Local_Fuel'!AH19
    value = "#DIV/0!"
    formula = "=AH11/'Dashboard M12 Local Fuel'!AH$7"
    @eval_fn
    def AH19():
        ah11_1 = Charts_Data_M12_Local_Fuel.AH11()
        ah7_1 = Dashboard_M12_Local_Fuel.AH7()
        var_1 = divide(ah11_1, ah7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AI19():
    # 'Charts_Data_M12_Local_Fuel'!AI19
    value = "#DIV/0!"
    formula = "=AI11/'Dashboard M12 Local Fuel'!AI$7"
    @eval_fn
    def AI19():
        ai11_1 = Charts_Data_M12_Local_Fuel.AI11()
        ai7_1 = Dashboard_M12_Local_Fuel.AI7()
        var_1 = divide(ai11_1, ai7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AJ19():
    # 'Charts_Data_M12_Local_Fuel'!AJ19
    value = "#DIV/0!"
    formula = "=AJ11/'Dashboard M12 Local Fuel'!AJ$7"
    @eval_fn
    def AJ19():
        aj11_1 = Charts_Data_M12_Local_Fuel.AJ11()
        aj7_1 = Dashboard_M12_Local_Fuel.AJ7()
        var_1 = divide(aj11_1, aj7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AK19():
    # 'Charts_Data_M12_Local_Fuel'!AK19
    value = "#DIV/0!"
    formula = "=AK11/'Dashboard M12 Local Fuel'!AK$7"
    @eval_fn
    def AK19():
        ak11_1 = Charts_Data_M12_Local_Fuel.AK11()
        ak7_1 = Dashboard_M12_Local_Fuel.AK7()
        var_1 = divide(ak11_1, ak7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AL19():
    # 'Charts_Data_M12_Local_Fuel'!AL19
    value = "#DIV/0!"
    formula = "=AL11/'Dashboard M12 Local Fuel'!AL$7"
    @eval_fn
    def AL19():
        al11_1 = Charts_Data_M12_Local_Fuel.AL11()
        al7_1 = Dashboard_M12_Local_Fuel.AL7()
        var_1 = divide(al11_1, al7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class D20():
    # 'Charts_Data_M12_Local_Fuel'!D20
    value = "Biomass "

@register(Charts_Data_M12_Local_Fuel)
class F20():
    # 'Charts_Data_M12_Local_Fuel'!F20
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G20():
    # 'Charts_Data_M12_Local_Fuel'!G20
    value = 0
    formula = "=G12/'Dashboard M12 Local Fuel'!G$7"
    @eval_fn
    def G20():
        g12_1 = Charts_Data_M12_Local_Fuel.G12()
        g7_1 = Dashboard_M12_Local_Fuel.G7()
        var_1 = divide(g12_1, g7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class H20():
    # 'Charts_Data_M12_Local_Fuel'!H20
    value = 0
    formula = "=H12/'Dashboard M12 Local Fuel'!H$7"
    @eval_fn
    def H20():
        h12_1 = Charts_Data_M12_Local_Fuel.H12()
        h7_1 = Dashboard_M12_Local_Fuel.H7()
        var_1 = divide(h12_1, h7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class I20():
    # 'Charts_Data_M12_Local_Fuel'!I20
    value = 0
    formula = "=I12/'Dashboard M12 Local Fuel'!I$7"
    @eval_fn
    def I20():
        i12_1 = Charts_Data_M12_Local_Fuel.I12()
        i7_1 = Dashboard_M12_Local_Fuel.I7()
        var_1 = divide(i12_1, i7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class J20():
    # 'Charts_Data_M12_Local_Fuel'!J20
    value = 0
    formula = "=J12/'Dashboard M12 Local Fuel'!J$7"
    @eval_fn
    def J20():
        j12_1 = Charts_Data_M12_Local_Fuel.J12()
        j7_1 = Dashboard_M12_Local_Fuel.J7()
        var_1 = divide(j12_1, j7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class K20():
    # 'Charts_Data_M12_Local_Fuel'!K20
    value = 0
    formula = "=K12/'Dashboard M12 Local Fuel'!K$7"
    @eval_fn
    def K20():
        k12_1 = Charts_Data_M12_Local_Fuel.K12()
        k7_1 = Dashboard_M12_Local_Fuel.K7()
        var_1 = divide(k12_1, k7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class L20():
    # 'Charts_Data_M12_Local_Fuel'!L20
    value = 0
    formula = "=L12/'Dashboard M12 Local Fuel'!L$7"
    @eval_fn
    def L20():
        l12_1 = Charts_Data_M12_Local_Fuel.L12()
        l7_1 = Dashboard_M12_Local_Fuel.L7()
        var_1 = divide(l12_1, l7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class M20():
    # 'Charts_Data_M12_Local_Fuel'!M20
    value = 0.0315124410265
    formula = "=M12/'Dashboard M12 Local Fuel'!M$7"
    @eval_fn
    def M20():
        m12_1 = Charts_Data_M12_Local_Fuel.M12()
        m7_1 = Dashboard_M12_Local_Fuel.M7()
        var_1 = divide(m12_1, m7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class N20():
    # 'Charts_Data_M12_Local_Fuel'!N20
    value = 0.0372730789007
    formula = "=N12/'Dashboard M12 Local Fuel'!N$7"
    @eval_fn
    def N20():
        n12_1 = Charts_Data_M12_Local_Fuel.N12()
        n7_1 = Dashboard_M12_Local_Fuel.N7()
        var_1 = divide(n12_1, n7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class O20():
    # 'Charts_Data_M12_Local_Fuel'!O20
    value = 0.0307120735567
    formula = "=O12/'Dashboard M12 Local Fuel'!O$7"
    @eval_fn
    def O20():
        o12_1 = Charts_Data_M12_Local_Fuel.O12()
        o7_1 = Dashboard_M12_Local_Fuel.O7()
        var_1 = divide(o12_1, o7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class P20():
    # 'Charts_Data_M12_Local_Fuel'!P20
    value = 0.0396227161609
    formula = "=P12/'Dashboard M12 Local Fuel'!P$7"
    @eval_fn
    def P20():
        p12_1 = Charts_Data_M12_Local_Fuel.P12()
        p7_1 = Dashboard_M12_Local_Fuel.P7()
        var_1 = divide(p12_1, p7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Q20():
    # 'Charts_Data_M12_Local_Fuel'!Q20
    value = 0.0392855334303
    formula = "=Q12/'Dashboard M12 Local Fuel'!Q$7"
    @eval_fn
    def Q20():
        q12_1 = Charts_Data_M12_Local_Fuel.Q12()
        q7_1 = Dashboard_M12_Local_Fuel.Q7()
        var_1 = divide(q12_1, q7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class R20():
    # 'Charts_Data_M12_Local_Fuel'!R20
    value = 0.0357570289298
    formula = "=R12/'Dashboard M12 Local Fuel'!R$7"
    @eval_fn
    def R20():
        r12_1 = Charts_Data_M12_Local_Fuel.R12()
        r7_1 = Dashboard_M12_Local_Fuel.R7()
        var_1 = divide(r12_1, r7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class S20():
    # 'Charts_Data_M12_Local_Fuel'!S20
    value = 0.0365709239598
    formula = "=S12/'Dashboard M12 Local Fuel'!S$7"
    @eval_fn
    def S20():
        s12_1 = Charts_Data_M12_Local_Fuel.S12()
        s7_1 = Dashboard_M12_Local_Fuel.S7()
        var_1 = divide(s12_1, s7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class T20():
    # 'Charts_Data_M12_Local_Fuel'!T20
    value = 0.0354584912915
    formula = "=T12/'Dashboard M12 Local Fuel'!T$7"
    @eval_fn
    def T20():
        t12_1 = Charts_Data_M12_Local_Fuel.T12()
        t7_1 = Dashboard_M12_Local_Fuel.T7()
        var_1 = divide(t12_1, t7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class U20():
    # 'Charts_Data_M12_Local_Fuel'!U20
    value = 0.043752383304
    formula = "=U12/'Dashboard M12 Local Fuel'!U$7"
    @eval_fn
    def U20():
        u12_1 = Charts_Data_M12_Local_Fuel.U12()
        u7_1 = Dashboard_M12_Local_Fuel.U7()
        var_1 = divide(u12_1, u7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class V20():
    # 'Charts_Data_M12_Local_Fuel'!V20
    value = 0.0460510690541
    formula = "=V12/'Dashboard M12 Local Fuel'!V$7"
    @eval_fn
    def V20():
        v12_1 = Charts_Data_M12_Local_Fuel.V12()
        v7_1 = Dashboard_M12_Local_Fuel.V7()
        var_1 = divide(v12_1, v7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class W20():
    # 'Charts_Data_M12_Local_Fuel'!W20
    value = 0.0443854318269
    formula = "=W12/'Dashboard M12 Local Fuel'!W$7"
    @eval_fn
    def W20():
        w12_1 = Charts_Data_M12_Local_Fuel.W12()
        w7_1 = Dashboard_M12_Local_Fuel.W7()
        var_1 = divide(w12_1, w7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class X20():
    # 'Charts_Data_M12_Local_Fuel'!X20
    value = "#DIV/0!"
    formula = "=X12/'Dashboard M12 Local Fuel'!X$7"
    @eval_fn
    def X20():
        x12_1 = Charts_Data_M12_Local_Fuel.X12()
        x7_1 = Dashboard_M12_Local_Fuel.X7()
        var_1 = divide(x12_1, x7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Y20():
    # 'Charts_Data_M12_Local_Fuel'!Y20
    value = "#DIV/0!"
    formula = "=Y12/'Dashboard M12 Local Fuel'!Y$7"
    @eval_fn
    def Y20():
        y12_1 = Charts_Data_M12_Local_Fuel.Y12()
        y7_1 = Dashboard_M12_Local_Fuel.Y7()
        var_1 = divide(y12_1, y7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Z20():
    # 'Charts_Data_M12_Local_Fuel'!Z20
    value = "#DIV/0!"
    formula = "=Z12/'Dashboard M12 Local Fuel'!Z$7"
    @eval_fn
    def Z20():
        z12_1 = Charts_Data_M12_Local_Fuel.Z12()
        z7_1 = Dashboard_M12_Local_Fuel.Z7()
        var_1 = divide(z12_1, z7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AA20():
    # 'Charts_Data_M12_Local_Fuel'!AA20
    value = "#DIV/0!"
    formula = "=AA12/'Dashboard M12 Local Fuel'!AA$7"
    @eval_fn
    def AA20():
        aa12_1 = Charts_Data_M12_Local_Fuel.AA12()
        aa7_1 = Dashboard_M12_Local_Fuel.AA7()
        var_1 = divide(aa12_1, aa7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AB20():
    # 'Charts_Data_M12_Local_Fuel'!AB20
    value = "#DIV/0!"
    formula = "=AB12/'Dashboard M12 Local Fuel'!AB$7"
    @eval_fn
    def AB20():
        ab12_1 = Charts_Data_M12_Local_Fuel.AB12()
        ab7_1 = Dashboard_M12_Local_Fuel.AB7()
        var_1 = divide(ab12_1, ab7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AC20():
    # 'Charts_Data_M12_Local_Fuel'!AC20
    value = "#DIV/0!"
    formula = "=AC12/'Dashboard M12 Local Fuel'!AC$7"
    @eval_fn
    def AC20():
        ac12_1 = Charts_Data_M12_Local_Fuel.AC12()
        ac7_1 = Dashboard_M12_Local_Fuel.AC7()
        var_1 = divide(ac12_1, ac7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AD20():
    # 'Charts_Data_M12_Local_Fuel'!AD20
    value = "#DIV/0!"
    formula = "=AD12/'Dashboard M12 Local Fuel'!AD$7"
    @eval_fn
    def AD20():
        ad12_1 = Charts_Data_M12_Local_Fuel.AD12()
        ad7_1 = Dashboard_M12_Local_Fuel.AD7()
        var_1 = divide(ad12_1, ad7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AE20():
    # 'Charts_Data_M12_Local_Fuel'!AE20
    value = "#DIV/0!"
    formula = "=AE12/'Dashboard M12 Local Fuel'!AE$7"
    @eval_fn
    def AE20():
        ae12_1 = Charts_Data_M12_Local_Fuel.AE12()
        ae7_1 = Dashboard_M12_Local_Fuel.AE7()
        var_1 = divide(ae12_1, ae7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AF20():
    # 'Charts_Data_M12_Local_Fuel'!AF20
    value = "#DIV/0!"
    formula = "=AF12/'Dashboard M12 Local Fuel'!AF$7"
    @eval_fn
    def AF20():
        af12_1 = Charts_Data_M12_Local_Fuel.AF12()
        af7_1 = Dashboard_M12_Local_Fuel.AF7()
        var_1 = divide(af12_1, af7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AG20():
    # 'Charts_Data_M12_Local_Fuel'!AG20
    value = "#DIV/0!"
    formula = "=AG12/'Dashboard M12 Local Fuel'!AG$7"
    @eval_fn
    def AG20():
        ag12_1 = Charts_Data_M12_Local_Fuel.AG12()
        ag7_1 = Dashboard_M12_Local_Fuel.AG7()
        var_1 = divide(ag12_1, ag7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AH20():
    # 'Charts_Data_M12_Local_Fuel'!AH20
    value = "#DIV/0!"
    formula = "=AH12/'Dashboard M12 Local Fuel'!AH$7"
    @eval_fn
    def AH20():
        ah12_1 = Charts_Data_M12_Local_Fuel.AH12()
        ah7_1 = Dashboard_M12_Local_Fuel.AH7()
        var_1 = divide(ah12_1, ah7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AI20():
    # 'Charts_Data_M12_Local_Fuel'!AI20
    value = "#DIV/0!"
    formula = "=AI12/'Dashboard M12 Local Fuel'!AI$7"
    @eval_fn
    def AI20():
        ai12_1 = Charts_Data_M12_Local_Fuel.AI12()
        ai7_1 = Dashboard_M12_Local_Fuel.AI7()
        var_1 = divide(ai12_1, ai7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AJ20():
    # 'Charts_Data_M12_Local_Fuel'!AJ20
    value = "#DIV/0!"
    formula = "=AJ12/'Dashboard M12 Local Fuel'!AJ$7"
    @eval_fn
    def AJ20():
        aj12_1 = Charts_Data_M12_Local_Fuel.AJ12()
        aj7_1 = Dashboard_M12_Local_Fuel.AJ7()
        var_1 = divide(aj12_1, aj7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AK20():
    # 'Charts_Data_M12_Local_Fuel'!AK20
    value = "#DIV/0!"
    formula = "=AK12/'Dashboard M12 Local Fuel'!AK$7"
    @eval_fn
    def AK20():
        ak12_1 = Charts_Data_M12_Local_Fuel.AK12()
        ak7_1 = Dashboard_M12_Local_Fuel.AK7()
        var_1 = divide(ak12_1, ak7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AL20():
    # 'Charts_Data_M12_Local_Fuel'!AL20
    value = "#DIV/0!"
    formula = "=AL12/'Dashboard M12 Local Fuel'!AL$7"
    @eval_fn
    def AL20():
        al12_1 = Charts_Data_M12_Local_Fuel.AL12()
        al7_1 = Dashboard_M12_Local_Fuel.AL7()
        var_1 = divide(al12_1, al7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class D21():
    # 'Charts_Data_M12_Local_Fuel'!D21
    value = "Solar "

@register(Charts_Data_M12_Local_Fuel)
class F21():
    # 'Charts_Data_M12_Local_Fuel'!F21
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G21():
    # 'Charts_Data_M12_Local_Fuel'!G21
    value = 0
    formula = "=G13/'Dashboard M12 Local Fuel'!G$7"
    @eval_fn
    def G21():
        g13_1 = Charts_Data_M12_Local_Fuel.G13()
        g7_1 = Dashboard_M12_Local_Fuel.G7()
        var_1 = divide(g13_1, g7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class H21():
    # 'Charts_Data_M12_Local_Fuel'!H21
    value = 0
    formula = "=H13/'Dashboard M12 Local Fuel'!H$7"
    @eval_fn
    def H21():
        h13_1 = Charts_Data_M12_Local_Fuel.H13()
        h7_1 = Dashboard_M12_Local_Fuel.H7()
        var_1 = divide(h13_1, h7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class I21():
    # 'Charts_Data_M12_Local_Fuel'!I21
    value = 0
    formula = "=I13/'Dashboard M12 Local Fuel'!I$7"
    @eval_fn
    def I21():
        i13_1 = Charts_Data_M12_Local_Fuel.I13()
        i7_1 = Dashboard_M12_Local_Fuel.I7()
        var_1 = divide(i13_1, i7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class J21():
    # 'Charts_Data_M12_Local_Fuel'!J21
    value = 0
    formula = "=J13/'Dashboard M12 Local Fuel'!J$7"
    @eval_fn
    def J21():
        j13_1 = Charts_Data_M12_Local_Fuel.J13()
        j7_1 = Dashboard_M12_Local_Fuel.J7()
        var_1 = divide(j13_1, j7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class K21():
    # 'Charts_Data_M12_Local_Fuel'!K21
    value = 6.46186598325e-06
    formula = "=K13/'Dashboard M12 Local Fuel'!K$7"
    @eval_fn
    def K21():
        k13_1 = Charts_Data_M12_Local_Fuel.K13()
        k7_1 = Dashboard_M12_Local_Fuel.K7()
        var_1 = divide(k13_1, k7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class L21():
    # 'Charts_Data_M12_Local_Fuel'!L21
    value = 8.54164831794e-06
    formula = "=L13/'Dashboard M12 Local Fuel'!L$7"
    @eval_fn
    def L21():
        l13_1 = Charts_Data_M12_Local_Fuel.L13()
        l7_1 = Dashboard_M12_Local_Fuel.L7()
        var_1 = divide(l13_1, l7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class M21():
    # 'Charts_Data_M12_Local_Fuel'!M21
    value = 0
    formula = "=M13/'Dashboard M12 Local Fuel'!M$7"
    @eval_fn
    def M21():
        m13_1 = Charts_Data_M12_Local_Fuel.M13()
        m7_1 = Dashboard_M12_Local_Fuel.M7()
        var_1 = divide(m13_1, m7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class N21():
    # 'Charts_Data_M12_Local_Fuel'!N21
    value = 0
    formula = "=N13/'Dashboard M12 Local Fuel'!N$7"
    @eval_fn
    def N21():
        n13_1 = Charts_Data_M12_Local_Fuel.N13()
        n7_1 = Dashboard_M12_Local_Fuel.N7()
        var_1 = divide(n13_1, n7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class O21():
    # 'Charts_Data_M12_Local_Fuel'!O21
    value = 0.000745529310943
    formula = "=O13/'Dashboard M12 Local Fuel'!O$7"
    @eval_fn
    def O21():
        o13_1 = Charts_Data_M12_Local_Fuel.O13()
        o7_1 = Dashboard_M12_Local_Fuel.O7()
        var_1 = divide(o13_1, o7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class P21():
    # 'Charts_Data_M12_Local_Fuel'!P21
    value = 0.0013697864089
    formula = "=P13/'Dashboard M12 Local Fuel'!P$7"
    @eval_fn
    def P21():
        p13_1 = Charts_Data_M12_Local_Fuel.P13()
        p7_1 = Dashboard_M12_Local_Fuel.P7()
        var_1 = divide(p13_1, p7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Q21():
    # 'Charts_Data_M12_Local_Fuel'!Q21
    value = 0.00358725515444
    formula = "=Q13/'Dashboard M12 Local Fuel'!Q$7"
    @eval_fn
    def Q21():
        q13_1 = Charts_Data_M12_Local_Fuel.Q13()
        q7_1 = Dashboard_M12_Local_Fuel.Q7()
        var_1 = divide(q13_1, q7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class R21():
    # 'Charts_Data_M12_Local_Fuel'!R21
    value = 0.00563159086255
    formula = "=R13/'Dashboard M12 Local Fuel'!R$7"
    @eval_fn
    def R21():
        r13_1 = Charts_Data_M12_Local_Fuel.R13()
        r7_1 = Dashboard_M12_Local_Fuel.R7()
        var_1 = divide(r13_1, r7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class S21():
    # 'Charts_Data_M12_Local_Fuel'!S21
    value = 0.00971448495577
    formula = "=S13/'Dashboard M12 Local Fuel'!S$7"
    @eval_fn
    def S21():
        s13_1 = Charts_Data_M12_Local_Fuel.S13()
        s7_1 = Dashboard_M12_Local_Fuel.S7()
        var_1 = divide(s13_1, s7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class T21():
    # 'Charts_Data_M12_Local_Fuel'!T21
    value = 0.0215174152141
    formula = "=T13/'Dashboard M12 Local Fuel'!T$7"
    @eval_fn
    def T21():
        t13_1 = Charts_Data_M12_Local_Fuel.T13()
        t7_1 = Dashboard_M12_Local_Fuel.T7()
        var_1 = divide(t13_1, t7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class U21():
    # 'Charts_Data_M12_Local_Fuel'!U21
    value = 0.0423238510859
    formula = "=U13/'Dashboard M12 Local Fuel'!U$7"
    @eval_fn
    def U21():
        u13_1 = Charts_Data_M12_Local_Fuel.U13()
        u7_1 = Dashboard_M12_Local_Fuel.U7()
        var_1 = divide(u13_1, u7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class V21():
    # 'Charts_Data_M12_Local_Fuel'!V21
    value = 0.0630679857906
    formula = "=V13/'Dashboard M12 Local Fuel'!V$7"
    @eval_fn
    def V21():
        v13_1 = Charts_Data_M12_Local_Fuel.V13()
        v7_1 = Dashboard_M12_Local_Fuel.V7()
        var_1 = divide(v13_1, v7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class W21():
    # 'Charts_Data_M12_Local_Fuel'!W21
    value = 0.0741387192264
    formula = "=W13/'Dashboard M12 Local Fuel'!W$7"
    @eval_fn
    def W21():
        w13_1 = Charts_Data_M12_Local_Fuel.W13()
        w7_1 = Dashboard_M12_Local_Fuel.W7()
        var_1 = divide(w13_1, w7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class X21():
    # 'Charts_Data_M12_Local_Fuel'!X21
    value = "#DIV/0!"
    formula = "=X13/'Dashboard M12 Local Fuel'!X$7"
    @eval_fn
    def X21():
        x13_1 = Charts_Data_M12_Local_Fuel.X13()
        x7_1 = Dashboard_M12_Local_Fuel.X7()
        var_1 = divide(x13_1, x7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Y21():
    # 'Charts_Data_M12_Local_Fuel'!Y21
    value = "#DIV/0!"
    formula = "=Y13/'Dashboard M12 Local Fuel'!Y$7"
    @eval_fn
    def Y21():
        y13_1 = Charts_Data_M12_Local_Fuel.Y13()
        y7_1 = Dashboard_M12_Local_Fuel.Y7()
        var_1 = divide(y13_1, y7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Z21():
    # 'Charts_Data_M12_Local_Fuel'!Z21
    value = "#DIV/0!"
    formula = "=Z13/'Dashboard M12 Local Fuel'!Z$7"
    @eval_fn
    def Z21():
        z13_1 = Charts_Data_M12_Local_Fuel.Z13()
        z7_1 = Dashboard_M12_Local_Fuel.Z7()
        var_1 = divide(z13_1, z7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AA21():
    # 'Charts_Data_M12_Local_Fuel'!AA21
    value = "#DIV/0!"
    formula = "=AA13/'Dashboard M12 Local Fuel'!AA$7"
    @eval_fn
    def AA21():
        aa13_1 = Charts_Data_M12_Local_Fuel.AA13()
        aa7_1 = Dashboard_M12_Local_Fuel.AA7()
        var_1 = divide(aa13_1, aa7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AB21():
    # 'Charts_Data_M12_Local_Fuel'!AB21
    value = "#DIV/0!"
    formula = "=AB13/'Dashboard M12 Local Fuel'!AB$7"
    @eval_fn
    def AB21():
        ab13_1 = Charts_Data_M12_Local_Fuel.AB13()
        ab7_1 = Dashboard_M12_Local_Fuel.AB7()
        var_1 = divide(ab13_1, ab7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AC21():
    # 'Charts_Data_M12_Local_Fuel'!AC21
    value = "#DIV/0!"
    formula = "=AC13/'Dashboard M12 Local Fuel'!AC$7"
    @eval_fn
    def AC21():
        ac13_1 = Charts_Data_M12_Local_Fuel.AC13()
        ac7_1 = Dashboard_M12_Local_Fuel.AC7()
        var_1 = divide(ac13_1, ac7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AD21():
    # 'Charts_Data_M12_Local_Fuel'!AD21
    value = "#DIV/0!"
    formula = "=AD13/'Dashboard M12 Local Fuel'!AD$7"
    @eval_fn
    def AD21():
        ad13_1 = Charts_Data_M12_Local_Fuel.AD13()
        ad7_1 = Dashboard_M12_Local_Fuel.AD7()
        var_1 = divide(ad13_1, ad7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AE21():
    # 'Charts_Data_M12_Local_Fuel'!AE21
    value = "#DIV/0!"
    formula = "=AE13/'Dashboard M12 Local Fuel'!AE$7"
    @eval_fn
    def AE21():
        ae13_1 = Charts_Data_M12_Local_Fuel.AE13()
        ae7_1 = Dashboard_M12_Local_Fuel.AE7()
        var_1 = divide(ae13_1, ae7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AF21():
    # 'Charts_Data_M12_Local_Fuel'!AF21
    value = "#DIV/0!"
    formula = "=AF13/'Dashboard M12 Local Fuel'!AF$7"
    @eval_fn
    def AF21():
        af13_1 = Charts_Data_M12_Local_Fuel.AF13()
        af7_1 = Dashboard_M12_Local_Fuel.AF7()
        var_1 = divide(af13_1, af7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AG21():
    # 'Charts_Data_M12_Local_Fuel'!AG21
    value = "#DIV/0!"
    formula = "=AG13/'Dashboard M12 Local Fuel'!AG$7"
    @eval_fn
    def AG21():
        ag13_1 = Charts_Data_M12_Local_Fuel.AG13()
        ag7_1 = Dashboard_M12_Local_Fuel.AG7()
        var_1 = divide(ag13_1, ag7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AH21():
    # 'Charts_Data_M12_Local_Fuel'!AH21
    value = "#DIV/0!"
    formula = "=AH13/'Dashboard M12 Local Fuel'!AH$7"
    @eval_fn
    def AH21():
        ah13_1 = Charts_Data_M12_Local_Fuel.AH13()
        ah7_1 = Dashboard_M12_Local_Fuel.AH7()
        var_1 = divide(ah13_1, ah7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AI21():
    # 'Charts_Data_M12_Local_Fuel'!AI21
    value = "#DIV/0!"
    formula = "=AI13/'Dashboard M12 Local Fuel'!AI$7"
    @eval_fn
    def AI21():
        ai13_1 = Charts_Data_M12_Local_Fuel.AI13()
        ai7_1 = Dashboard_M12_Local_Fuel.AI7()
        var_1 = divide(ai13_1, ai7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AJ21():
    # 'Charts_Data_M12_Local_Fuel'!AJ21
    value = "#DIV/0!"
    formula = "=AJ13/'Dashboard M12 Local Fuel'!AJ$7"
    @eval_fn
    def AJ21():
        aj13_1 = Charts_Data_M12_Local_Fuel.AJ13()
        aj7_1 = Dashboard_M12_Local_Fuel.AJ7()
        var_1 = divide(aj13_1, aj7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AK21():
    # 'Charts_Data_M12_Local_Fuel'!AK21
    value = "#DIV/0!"
    formula = "=AK13/'Dashboard M12 Local Fuel'!AK$7"
    @eval_fn
    def AK21():
        ak13_1 = Charts_Data_M12_Local_Fuel.AK13()
        ak7_1 = Dashboard_M12_Local_Fuel.AK7()
        var_1 = divide(ak13_1, ak7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AL21():
    # 'Charts_Data_M12_Local_Fuel'!AL21
    value = "#DIV/0!"
    formula = "=AL13/'Dashboard M12 Local Fuel'!AL$7"
    @eval_fn
    def AL21():
        al13_1 = Charts_Data_M12_Local_Fuel.AL13()
        al7_1 = Dashboard_M12_Local_Fuel.AL7()
        var_1 = divide(al13_1, al7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class D22():
    # 'Charts_Data_M12_Local_Fuel'!D22
    value = "Biofuels "

@register(Charts_Data_M12_Local_Fuel)
class F22():
    # 'Charts_Data_M12_Local_Fuel'!F22
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G22():
    # 'Charts_Data_M12_Local_Fuel'!G22
    value = "#REF!"
    formula = "=G14/'Dashboard M12 Local Fuel'!G$7"
    @eval_fn
    def G22():
        g14_1 = Charts_Data_M12_Local_Fuel.G14()
        g7_1 = Dashboard_M12_Local_Fuel.G7()
        var_1 = divide(g14_1, g7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class H22():
    # 'Charts_Data_M12_Local_Fuel'!H22
    value = "#REF!"
    formula = "=H14/'Dashboard M12 Local Fuel'!H$7"
    @eval_fn
    def H22():
        h14_1 = Charts_Data_M12_Local_Fuel.H14()
        h7_1 = Dashboard_M12_Local_Fuel.H7()
        var_1 = divide(h14_1, h7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class I22():
    # 'Charts_Data_M12_Local_Fuel'!I22
    value = "#REF!"
    formula = "=I14/'Dashboard M12 Local Fuel'!I$7"
    @eval_fn
    def I22():
        i14_1 = Charts_Data_M12_Local_Fuel.I14()
        i7_1 = Dashboard_M12_Local_Fuel.I7()
        var_1 = divide(i14_1, i7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class J22():
    # 'Charts_Data_M12_Local_Fuel'!J22
    value = "#REF!"
    formula = "=J14/'Dashboard M12 Local Fuel'!J$7"
    @eval_fn
    def J22():
        j14_1 = Charts_Data_M12_Local_Fuel.J14()
        j7_1 = Dashboard_M12_Local_Fuel.J7()
        var_1 = divide(j14_1, j7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class K22():
    # 'Charts_Data_M12_Local_Fuel'!K22
    value = "#REF!"
    formula = "=K14/'Dashboard M12 Local Fuel'!K$7"
    @eval_fn
    def K22():
        k14_1 = Charts_Data_M12_Local_Fuel.K14()
        k7_1 = Dashboard_M12_Local_Fuel.K7()
        var_1 = divide(k14_1, k7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class L22():
    # 'Charts_Data_M12_Local_Fuel'!L22
    value = 2.43911513079e-05
    formula = "=L14/'Dashboard M12 Local Fuel'!L$7"
    @eval_fn
    def L22():
        l14_1 = Charts_Data_M12_Local_Fuel.L14()
        l7_1 = Dashboard_M12_Local_Fuel.L7()
        var_1 = divide(l14_1, l7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class M22():
    # 'Charts_Data_M12_Local_Fuel'!M22
    value = 4.81676651127e-05
    formula = "=M14/'Dashboard M12 Local Fuel'!M$7"
    @eval_fn
    def M22():
        m14_1 = Charts_Data_M12_Local_Fuel.M14()
        m7_1 = Dashboard_M12_Local_Fuel.M7()
        var_1 = divide(m14_1, m7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class N22():
    # 'Charts_Data_M12_Local_Fuel'!N22
    value = 4.9351443709e-05
    formula = "=N14/'Dashboard M12 Local Fuel'!N$7"
    @eval_fn
    def N22():
        n14_1 = Charts_Data_M12_Local_Fuel.N14()
        n7_1 = Dashboard_M12_Local_Fuel.N7()
        var_1 = divide(n14_1, n7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class O22():
    # 'Charts_Data_M12_Local_Fuel'!O22
    value = 0.000172684757146
    formula = "=O14/'Dashboard M12 Local Fuel'!O$7"
    @eval_fn
    def O22():
        o14_1 = Charts_Data_M12_Local_Fuel.O14()
        o7_1 = Dashboard_M12_Local_Fuel.O7()
        var_1 = divide(o14_1, o7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class P22():
    # 'Charts_Data_M12_Local_Fuel'!P22
    value = "#REF!"
    formula = "=P14/'Dashboard M12 Local Fuel'!P$7"
    @eval_fn
    def P22():
        p14_1 = Charts_Data_M12_Local_Fuel.P14()
        p7_1 = Dashboard_M12_Local_Fuel.P7()
        var_1 = divide(p14_1, p7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Q22():
    # 'Charts_Data_M12_Local_Fuel'!Q22
    value = "#REF!"
    formula = "=Q14/'Dashboard M12 Local Fuel'!Q$7"
    @eval_fn
    def Q22():
        q14_1 = Charts_Data_M12_Local_Fuel.Q14()
        q7_1 = Dashboard_M12_Local_Fuel.Q7()
        var_1 = divide(q14_1, q7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class R22():
    # 'Charts_Data_M12_Local_Fuel'!R22
    value = "#REF!"
    formula = "=R14/'Dashboard M12 Local Fuel'!R$7"
    @eval_fn
    def R22():
        r14_1 = Charts_Data_M12_Local_Fuel.R14()
        r7_1 = Dashboard_M12_Local_Fuel.R7()
        var_1 = divide(r14_1, r7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class S22():
    # 'Charts_Data_M12_Local_Fuel'!S22
    value = "#REF!"
    formula = "=S14/'Dashboard M12 Local Fuel'!S$7"
    @eval_fn
    def S22():
        s14_1 = Charts_Data_M12_Local_Fuel.S14()
        s7_1 = Dashboard_M12_Local_Fuel.S7()
        var_1 = divide(s14_1, s7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class T22():
    # 'Charts_Data_M12_Local_Fuel'!T22
    value = "#REF!"
    formula = "=T14/'Dashboard M12 Local Fuel'!T$7"
    @eval_fn
    def T22():
        t14_1 = Charts_Data_M12_Local_Fuel.T14()
        t7_1 = Dashboard_M12_Local_Fuel.T7()
        var_1 = divide(t14_1, t7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class U22():
    # 'Charts_Data_M12_Local_Fuel'!U22
    value = "#REF!"
    formula = "=U14/'Dashboard M12 Local Fuel'!U$7"
    @eval_fn
    def U22():
        u14_1 = Charts_Data_M12_Local_Fuel.U14()
        u7_1 = Dashboard_M12_Local_Fuel.U7()
        var_1 = divide(u14_1, u7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class V22():
    # 'Charts_Data_M12_Local_Fuel'!V22
    value = "#REF!"
    formula = "=V14/'Dashboard M12 Local Fuel'!V$7"
    @eval_fn
    def V22():
        v14_1 = Charts_Data_M12_Local_Fuel.V14()
        v7_1 = Dashboard_M12_Local_Fuel.V7()
        var_1 = divide(v14_1, v7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class W22():
    # 'Charts_Data_M12_Local_Fuel'!W22
    value = "#REF!"
    formula = "=W14/'Dashboard M12 Local Fuel'!W$7"
    @eval_fn
    def W22():
        w14_1 = Charts_Data_M12_Local_Fuel.W14()
        w7_1 = Dashboard_M12_Local_Fuel.W7()
        var_1 = divide(w14_1, w7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class X22():
    # 'Charts_Data_M12_Local_Fuel'!X22
    value = "#REF!"
    formula = "=X14/'Dashboard M12 Local Fuel'!X$7"
    @eval_fn
    def X22():
        x14_1 = Charts_Data_M12_Local_Fuel.X14()
        x7_1 = Dashboard_M12_Local_Fuel.X7()
        var_1 = divide(x14_1, x7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Y22():
    # 'Charts_Data_M12_Local_Fuel'!Y22
    value = "#REF!"
    formula = "=Y14/'Dashboard M12 Local Fuel'!Y$7"
    @eval_fn
    def Y22():
        y14_1 = Charts_Data_M12_Local_Fuel.Y14()
        y7_1 = Dashboard_M12_Local_Fuel.Y7()
        var_1 = divide(y14_1, y7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Z22():
    # 'Charts_Data_M12_Local_Fuel'!Z22
    value = "#REF!"
    formula = "=Z14/'Dashboard M12 Local Fuel'!Z$7"
    @eval_fn
    def Z22():
        z14_1 = Charts_Data_M12_Local_Fuel.Z14()
        z7_1 = Dashboard_M12_Local_Fuel.Z7()
        var_1 = divide(z14_1, z7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AA22():
    # 'Charts_Data_M12_Local_Fuel'!AA22
    value = "#REF!"
    formula = "=AA14/'Dashboard M12 Local Fuel'!AA$7"
    @eval_fn
    def AA22():
        aa14_1 = Charts_Data_M12_Local_Fuel.AA14()
        aa7_1 = Dashboard_M12_Local_Fuel.AA7()
        var_1 = divide(aa14_1, aa7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AB22():
    # 'Charts_Data_M12_Local_Fuel'!AB22
    value = "#REF!"
    formula = "=AB14/'Dashboard M12 Local Fuel'!AB$7"
    @eval_fn
    def AB22():
        ab14_1 = Charts_Data_M12_Local_Fuel.AB14()
        ab7_1 = Dashboard_M12_Local_Fuel.AB7()
        var_1 = divide(ab14_1, ab7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AC22():
    # 'Charts_Data_M12_Local_Fuel'!AC22
    value = "#REF!"
    formula = "=AC14/'Dashboard M12 Local Fuel'!AC$7"
    @eval_fn
    def AC22():
        ac14_1 = Charts_Data_M12_Local_Fuel.AC14()
        ac7_1 = Dashboard_M12_Local_Fuel.AC7()
        var_1 = divide(ac14_1, ac7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AD22():
    # 'Charts_Data_M12_Local_Fuel'!AD22
    value = "#REF!"
    formula = "=AD14/'Dashboard M12 Local Fuel'!AD$7"
    @eval_fn
    def AD22():
        ad14_1 = Charts_Data_M12_Local_Fuel.AD14()
        ad7_1 = Dashboard_M12_Local_Fuel.AD7()
        var_1 = divide(ad14_1, ad7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AE22():
    # 'Charts_Data_M12_Local_Fuel'!AE22
    value = "#REF!"
    formula = "=AE14/'Dashboard M12 Local Fuel'!AE$7"
    @eval_fn
    def AE22():
        ae14_1 = Charts_Data_M12_Local_Fuel.AE14()
        ae7_1 = Dashboard_M12_Local_Fuel.AE7()
        var_1 = divide(ae14_1, ae7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AF22():
    # 'Charts_Data_M12_Local_Fuel'!AF22
    value = "#REF!"
    formula = "=AF14/'Dashboard M12 Local Fuel'!AF$7"
    @eval_fn
    def AF22():
        af14_1 = Charts_Data_M12_Local_Fuel.AF14()
        af7_1 = Dashboard_M12_Local_Fuel.AF7()
        var_1 = divide(af14_1, af7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AG22():
    # 'Charts_Data_M12_Local_Fuel'!AG22
    value = "#REF!"
    formula = "=AG14/'Dashboard M12 Local Fuel'!AG$7"
    @eval_fn
    def AG22():
        ag14_1 = Charts_Data_M12_Local_Fuel.AG14()
        ag7_1 = Dashboard_M12_Local_Fuel.AG7()
        var_1 = divide(ag14_1, ag7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AH22():
    # 'Charts_Data_M12_Local_Fuel'!AH22
    value = "#REF!"
    formula = "=AH14/'Dashboard M12 Local Fuel'!AH$7"
    @eval_fn
    def AH22():
        ah14_1 = Charts_Data_M12_Local_Fuel.AH14()
        ah7_1 = Dashboard_M12_Local_Fuel.AH7()
        var_1 = divide(ah14_1, ah7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AI22():
    # 'Charts_Data_M12_Local_Fuel'!AI22
    value = "#REF!"
    formula = "=AI14/'Dashboard M12 Local Fuel'!AI$7"
    @eval_fn
    def AI22():
        ai14_1 = Charts_Data_M12_Local_Fuel.AI14()
        ai7_1 = Dashboard_M12_Local_Fuel.AI7()
        var_1 = divide(ai14_1, ai7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AJ22():
    # 'Charts_Data_M12_Local_Fuel'!AJ22
    value = "#REF!"
    formula = "=AJ14/'Dashboard M12 Local Fuel'!AJ$7"
    @eval_fn
    def AJ22():
        aj14_1 = Charts_Data_M12_Local_Fuel.AJ14()
        aj7_1 = Dashboard_M12_Local_Fuel.AJ7()
        var_1 = divide(aj14_1, aj7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AK22():
    # 'Charts_Data_M12_Local_Fuel'!AK22
    value = "#REF!"
    formula = "=AK14/'Dashboard M12 Local Fuel'!AK$7"
    @eval_fn
    def AK22():
        ak14_1 = Charts_Data_M12_Local_Fuel.AK14()
        ak7_1 = Dashboard_M12_Local_Fuel.AK7()
        var_1 = divide(ak14_1, ak7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AL22():
    # 'Charts_Data_M12_Local_Fuel'!AL22
    value = "#REF!"
    formula = "=AL14/'Dashboard M12 Local Fuel'!AL$7"
    @eval_fn
    def AL22():
        al14_1 = Charts_Data_M12_Local_Fuel.AL14()
        al7_1 = Dashboard_M12_Local_Fuel.AL7()
        var_1 = divide(al14_1, al7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class D23():
    # 'Charts_Data_M12_Local_Fuel'!D23
    value = "Missing"

@register(Charts_Data_M12_Local_Fuel)
class F23():
    # 'Charts_Data_M12_Local_Fuel'!F23
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G23():
    # 'Charts_Data_M12_Local_Fuel'!G23
    value = "#REF!"
    formula = "=G15/'Dashboard M12 Local Fuel'!G$7"
    @eval_fn
    def G23():
        g15_1 = Charts_Data_M12_Local_Fuel.G15()
        g7_1 = Dashboard_M12_Local_Fuel.G7()
        var_1 = divide(g15_1, g7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class H23():
    # 'Charts_Data_M12_Local_Fuel'!H23
    value = "#REF!"
    formula = "=H15/'Dashboard M12 Local Fuel'!H$7"
    @eval_fn
    def H23():
        h15_1 = Charts_Data_M12_Local_Fuel.H15()
        h7_1 = Dashboard_M12_Local_Fuel.H7()
        var_1 = divide(h15_1, h7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class I23():
    # 'Charts_Data_M12_Local_Fuel'!I23
    value = "#REF!"
    formula = "=I15/'Dashboard M12 Local Fuel'!I$7"
    @eval_fn
    def I23():
        i15_1 = Charts_Data_M12_Local_Fuel.I15()
        i7_1 = Dashboard_M12_Local_Fuel.I7()
        var_1 = divide(i15_1, i7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class J23():
    # 'Charts_Data_M12_Local_Fuel'!J23
    value = "#REF!"
    formula = "=J15/'Dashboard M12 Local Fuel'!J$7"
    @eval_fn
    def J23():
        j15_1 = Charts_Data_M12_Local_Fuel.J15()
        j7_1 = Dashboard_M12_Local_Fuel.J7()
        var_1 = divide(j15_1, j7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class K23():
    # 'Charts_Data_M12_Local_Fuel'!K23
    value = "#REF!"
    formula = "=K15/'Dashboard M12 Local Fuel'!K$7"
    @eval_fn
    def K23():
        k15_1 = Charts_Data_M12_Local_Fuel.K15()
        k7_1 = Dashboard_M12_Local_Fuel.K7()
        var_1 = divide(k15_1, k7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class L23():
    # 'Charts_Data_M12_Local_Fuel'!L23
    value = 0.0664445331932
    formula = "=L15/'Dashboard M12 Local Fuel'!L$7"
    @eval_fn
    def L23():
        l15_1 = Charts_Data_M12_Local_Fuel.L15()
        l7_1 = Dashboard_M12_Local_Fuel.L7()
        var_1 = divide(l15_1, l7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class M23():
    # 'Charts_Data_M12_Local_Fuel'!M23
    value = 0.000239596666377
    formula = "=M15/'Dashboard M12 Local Fuel'!M$7"
    @eval_fn
    def M23():
        m15_1 = Charts_Data_M12_Local_Fuel.M15()
        m7_1 = Dashboard_M12_Local_Fuel.M7()
        var_1 = divide(m15_1, m7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class N23():
    # 'Charts_Data_M12_Local_Fuel'!N23
    value = 0.000348498801871
    formula = "=N15/'Dashboard M12 Local Fuel'!N$7"
    @eval_fn
    def N23():
        n15_1 = Charts_Data_M12_Local_Fuel.N15()
        n7_1 = Dashboard_M12_Local_Fuel.N7()
        var_1 = divide(n15_1, n7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class O23():
    # 'Charts_Data_M12_Local_Fuel'!O23
    value = 0
    formula = "=O15/'Dashboard M12 Local Fuel'!O$7"
    @eval_fn
    def O23():
        o15_1 = Charts_Data_M12_Local_Fuel.O15()
        o7_1 = Dashboard_M12_Local_Fuel.O7()
        var_1 = divide(o15_1, o7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class P23():
    # 'Charts_Data_M12_Local_Fuel'!P23
    value = "#REF!"
    formula = "=P15/'Dashboard M12 Local Fuel'!P$7"
    @eval_fn
    def P23():
        p15_1 = Charts_Data_M12_Local_Fuel.P15()
        p7_1 = Dashboard_M12_Local_Fuel.P7()
        var_1 = divide(p15_1, p7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Q23():
    # 'Charts_Data_M12_Local_Fuel'!Q23
    value = "#REF!"
    formula = "=Q15/'Dashboard M12 Local Fuel'!Q$7"
    @eval_fn
    def Q23():
        q15_1 = Charts_Data_M12_Local_Fuel.Q15()
        q7_1 = Dashboard_M12_Local_Fuel.Q7()
        var_1 = divide(q15_1, q7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class R23():
    # 'Charts_Data_M12_Local_Fuel'!R23
    value = "#REF!"
    formula = "=R15/'Dashboard M12 Local Fuel'!R$7"
    @eval_fn
    def R23():
        r15_1 = Charts_Data_M12_Local_Fuel.R15()
        r7_1 = Dashboard_M12_Local_Fuel.R7()
        var_1 = divide(r15_1, r7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class S23():
    # 'Charts_Data_M12_Local_Fuel'!S23
    value = "#REF!"
    formula = "=S15/'Dashboard M12 Local Fuel'!S$7"
    @eval_fn
    def S23():
        s15_1 = Charts_Data_M12_Local_Fuel.S15()
        s7_1 = Dashboard_M12_Local_Fuel.S7()
        var_1 = divide(s15_1, s7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class T23():
    # 'Charts_Data_M12_Local_Fuel'!T23
    value = "#REF!"
    formula = "=T15/'Dashboard M12 Local Fuel'!T$7"
    @eval_fn
    def T23():
        t15_1 = Charts_Data_M12_Local_Fuel.T15()
        t7_1 = Dashboard_M12_Local_Fuel.T7()
        var_1 = divide(t15_1, t7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class U23():
    # 'Charts_Data_M12_Local_Fuel'!U23
    value = "#REF!"
    formula = "=U15/'Dashboard M12 Local Fuel'!U$7"
    @eval_fn
    def U23():
        u15_1 = Charts_Data_M12_Local_Fuel.U15()
        u7_1 = Dashboard_M12_Local_Fuel.U7()
        var_1 = divide(u15_1, u7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class V23():
    # 'Charts_Data_M12_Local_Fuel'!V23
    value = "#REF!"
    formula = "=V15/'Dashboard M12 Local Fuel'!V$7"
    @eval_fn
    def V23():
        v15_1 = Charts_Data_M12_Local_Fuel.V15()
        v7_1 = Dashboard_M12_Local_Fuel.V7()
        var_1 = divide(v15_1, v7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class W23():
    # 'Charts_Data_M12_Local_Fuel'!W23
    value = "#REF!"
    formula = "=W15/'Dashboard M12 Local Fuel'!W$7"
    @eval_fn
    def W23():
        w15_1 = Charts_Data_M12_Local_Fuel.W15()
        w7_1 = Dashboard_M12_Local_Fuel.W7()
        var_1 = divide(w15_1, w7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class X23():
    # 'Charts_Data_M12_Local_Fuel'!X23
    value = "#REF!"
    formula = "=X15/'Dashboard M12 Local Fuel'!X$7"
    @eval_fn
    def X23():
        x15_1 = Charts_Data_M12_Local_Fuel.X15()
        x7_1 = Dashboard_M12_Local_Fuel.X7()
        var_1 = divide(x15_1, x7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Y23():
    # 'Charts_Data_M12_Local_Fuel'!Y23
    value = "#REF!"
    formula = "=Y15/'Dashboard M12 Local Fuel'!Y$7"
    @eval_fn
    def Y23():
        y15_1 = Charts_Data_M12_Local_Fuel.Y15()
        y7_1 = Dashboard_M12_Local_Fuel.Y7()
        var_1 = divide(y15_1, y7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Z23():
    # 'Charts_Data_M12_Local_Fuel'!Z23
    value = "#REF!"
    formula = "=Z15/'Dashboard M12 Local Fuel'!Z$7"
    @eval_fn
    def Z23():
        z15_1 = Charts_Data_M12_Local_Fuel.Z15()
        z7_1 = Dashboard_M12_Local_Fuel.Z7()
        var_1 = divide(z15_1, z7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AA23():
    # 'Charts_Data_M12_Local_Fuel'!AA23
    value = "#REF!"
    formula = "=AA15/'Dashboard M12 Local Fuel'!AA$7"
    @eval_fn
    def AA23():
        aa15_1 = Charts_Data_M12_Local_Fuel.AA15()
        aa7_1 = Dashboard_M12_Local_Fuel.AA7()
        var_1 = divide(aa15_1, aa7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AB23():
    # 'Charts_Data_M12_Local_Fuel'!AB23
    value = "#REF!"
    formula = "=AB15/'Dashboard M12 Local Fuel'!AB$7"
    @eval_fn
    def AB23():
        ab15_1 = Charts_Data_M12_Local_Fuel.AB15()
        ab7_1 = Dashboard_M12_Local_Fuel.AB7()
        var_1 = divide(ab15_1, ab7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AC23():
    # 'Charts_Data_M12_Local_Fuel'!AC23
    value = "#REF!"
    formula = "=AC15/'Dashboard M12 Local Fuel'!AC$7"
    @eval_fn
    def AC23():
        ac15_1 = Charts_Data_M12_Local_Fuel.AC15()
        ac7_1 = Dashboard_M12_Local_Fuel.AC7()
        var_1 = divide(ac15_1, ac7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AD23():
    # 'Charts_Data_M12_Local_Fuel'!AD23
    value = "#REF!"
    formula = "=AD15/'Dashboard M12 Local Fuel'!AD$7"
    @eval_fn
    def AD23():
        ad15_1 = Charts_Data_M12_Local_Fuel.AD15()
        ad7_1 = Dashboard_M12_Local_Fuel.AD7()
        var_1 = divide(ad15_1, ad7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AE23():
    # 'Charts_Data_M12_Local_Fuel'!AE23
    value = "#REF!"
    formula = "=AE15/'Dashboard M12 Local Fuel'!AE$7"
    @eval_fn
    def AE23():
        ae15_1 = Charts_Data_M12_Local_Fuel.AE15()
        ae7_1 = Dashboard_M12_Local_Fuel.AE7()
        var_1 = divide(ae15_1, ae7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AF23():
    # 'Charts_Data_M12_Local_Fuel'!AF23
    value = "#REF!"
    formula = "=AF15/'Dashboard M12 Local Fuel'!AF$7"
    @eval_fn
    def AF23():
        af15_1 = Charts_Data_M12_Local_Fuel.AF15()
        af7_1 = Dashboard_M12_Local_Fuel.AF7()
        var_1 = divide(af15_1, af7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AG23():
    # 'Charts_Data_M12_Local_Fuel'!AG23
    value = "#REF!"
    formula = "=AG15/'Dashboard M12 Local Fuel'!AG$7"
    @eval_fn
    def AG23():
        ag15_1 = Charts_Data_M12_Local_Fuel.AG15()
        ag7_1 = Dashboard_M12_Local_Fuel.AG7()
        var_1 = divide(ag15_1, ag7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AH23():
    # 'Charts_Data_M12_Local_Fuel'!AH23
    value = "#REF!"
    formula = "=AH15/'Dashboard M12 Local Fuel'!AH$7"
    @eval_fn
    def AH23():
        ah15_1 = Charts_Data_M12_Local_Fuel.AH15()
        ah7_1 = Dashboard_M12_Local_Fuel.AH7()
        var_1 = divide(ah15_1, ah7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AI23():
    # 'Charts_Data_M12_Local_Fuel'!AI23
    value = "#REF!"
    formula = "=AI15/'Dashboard M12 Local Fuel'!AI$7"
    @eval_fn
    def AI23():
        ai15_1 = Charts_Data_M12_Local_Fuel.AI15()
        ai7_1 = Dashboard_M12_Local_Fuel.AI7()
        var_1 = divide(ai15_1, ai7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AJ23():
    # 'Charts_Data_M12_Local_Fuel'!AJ23
    value = "#REF!"
    formula = "=AJ15/'Dashboard M12 Local Fuel'!AJ$7"
    @eval_fn
    def AJ23():
        aj15_1 = Charts_Data_M12_Local_Fuel.AJ15()
        aj7_1 = Dashboard_M12_Local_Fuel.AJ7()
        var_1 = divide(aj15_1, aj7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AK23():
    # 'Charts_Data_M12_Local_Fuel'!AK23
    value = "#REF!"
    formula = "=AK15/'Dashboard M12 Local Fuel'!AK$7"
    @eval_fn
    def AK23():
        ak15_1 = Charts_Data_M12_Local_Fuel.AK15()
        ak7_1 = Dashboard_M12_Local_Fuel.AK7()
        var_1 = divide(ak15_1, ak7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AL23():
    # 'Charts_Data_M12_Local_Fuel'!AL23
    value = "#REF!"
    formula = "=AL15/'Dashboard M12 Local Fuel'!AL$7"
    @eval_fn
    def AL23():
        al15_1 = Charts_Data_M12_Local_Fuel.AL15()
        al7_1 = Dashboard_M12_Local_Fuel.AL7()
        var_1 = divide(al15_1, al7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class D24():
    # 'Charts_Data_M12_Local_Fuel'!D24
    value = "Total"

@register(Charts_Data_M12_Local_Fuel)
class F24():
    # 'Charts_Data_M12_Local_Fuel'!F24
    value = "Notes"

@register(Charts_Data_M12_Local_Fuel)
class G24():
    # 'Charts_Data_M12_Local_Fuel'!G24
    value = 0.056274378442
    formula = "=G16/'Dashboard M12 Local Fuel'!G$7"
    @eval_fn
    def G24():
        g16_1 = Charts_Data_M12_Local_Fuel.G16()
        g7_1 = Dashboard_M12_Local_Fuel.G7()
        var_1 = divide(g16_1, g7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class H24():
    # 'Charts_Data_M12_Local_Fuel'!H24
    value = 0.0700278743846
    formula = "=H16/'Dashboard M12 Local Fuel'!H$7"
    @eval_fn
    def H24():
        h16_1 = Charts_Data_M12_Local_Fuel.H16()
        h7_1 = Dashboard_M12_Local_Fuel.H7()
        var_1 = divide(h16_1, h7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class I24():
    # 'Charts_Data_M12_Local_Fuel'!I24
    value = 0.0626668696462
    formula = "=I16/'Dashboard M12 Local Fuel'!I$7"
    @eval_fn
    def I24():
        i16_1 = Charts_Data_M12_Local_Fuel.I16()
        i7_1 = Dashboard_M12_Local_Fuel.I7()
        var_1 = divide(i16_1, i7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class J24():
    # 'Charts_Data_M12_Local_Fuel'!J24
    value = 0.0519174910027
    formula = "=J16/'Dashboard M12 Local Fuel'!J$7"
    @eval_fn
    def J24():
        j16_1 = Charts_Data_M12_Local_Fuel.J16()
        j7_1 = Dashboard_M12_Local_Fuel.J7()
        var_1 = divide(j16_1, j7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class K24():
    # 'Charts_Data_M12_Local_Fuel'!K24
    value = 0.0662004462995
    formula = "=K16/'Dashboard M12 Local Fuel'!K$7"
    @eval_fn
    def K24():
        k16_1 = Charts_Data_M12_Local_Fuel.K16()
        k7_1 = Dashboard_M12_Local_Fuel.K7()
        var_1 = divide(k16_1, k7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class L24():
    # 'Charts_Data_M12_Local_Fuel'!L24
    value = 0.0700356319605
    formula = "=L16/'Dashboard M12 Local Fuel'!L$7"
    @eval_fn
    def L24():
        l16_1 = Charts_Data_M12_Local_Fuel.L16()
        l7_1 = Dashboard_M12_Local_Fuel.L7()
        var_1 = divide(l16_1, l7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class M24():
    # 'Charts_Data_M12_Local_Fuel'!M24
    value = 0.0678068125611
    formula = "=M16/'Dashboard M12 Local Fuel'!M$7"
    @eval_fn
    def M24():
        m16_1 = Charts_Data_M12_Local_Fuel.M16()
        m7_1 = Dashboard_M12_Local_Fuel.M7()
        var_1 = divide(m16_1, m7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class N24():
    # 'Charts_Data_M12_Local_Fuel'!N24
    value = 0.0816549551314
    formula = "=N16/'Dashboard M12 Local Fuel'!N$7"
    @eval_fn
    def N24():
        n16_1 = Charts_Data_M12_Local_Fuel.N16()
        n7_1 = Dashboard_M12_Local_Fuel.N7()
        var_1 = divide(n16_1, n7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class O24():
    # 'Charts_Data_M12_Local_Fuel'!O24
    value = 0.0891129263534
    formula = "=O16/'Dashboard M12 Local Fuel'!O$7"
    @eval_fn
    def O24():
        o16_1 = Charts_Data_M12_Local_Fuel.O16()
        o7_1 = Dashboard_M12_Local_Fuel.O7()
        var_1 = divide(o16_1, o7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class P24():
    # 'Charts_Data_M12_Local_Fuel'!P24
    value = 0.0938810183414
    formula = "=P16/'Dashboard M12 Local Fuel'!P$7"
    @eval_fn
    def P24():
        p16_1 = Charts_Data_M12_Local_Fuel.P16()
        p7_1 = Dashboard_M12_Local_Fuel.P7()
        var_1 = divide(p16_1, p7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Q24():
    # 'Charts_Data_M12_Local_Fuel'!Q24
    value = 0.0950542585772
    formula = "=Q16/'Dashboard M12 Local Fuel'!Q$7"
    @eval_fn
    def Q24():
        q16_1 = Charts_Data_M12_Local_Fuel.Q16()
        q7_1 = Dashboard_M12_Local_Fuel.Q7()
        var_1 = divide(q16_1, q7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class R24():
    # 'Charts_Data_M12_Local_Fuel'!R24
    value = 0.0948019596755
    formula = "=R16/'Dashboard M12 Local Fuel'!R$7"
    @eval_fn
    def R24():
        r16_1 = Charts_Data_M12_Local_Fuel.R16()
        r7_1 = Dashboard_M12_Local_Fuel.R7()
        var_1 = divide(r16_1, r7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class S24():
    # 'Charts_Data_M12_Local_Fuel'!S24
    value = 0.11907162581
    formula = "=S16/'Dashboard M12 Local Fuel'!S$7"
    @eval_fn
    def S24():
        s16_1 = Charts_Data_M12_Local_Fuel.S16()
        s7_1 = Dashboard_M12_Local_Fuel.S7()
        var_1 = divide(s16_1, s7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class T24():
    # 'Charts_Data_M12_Local_Fuel'!T24
    value = 0.138009747843
    formula = "=T16/'Dashboard M12 Local Fuel'!T$7"
    @eval_fn
    def T24():
        t16_1 = Charts_Data_M12_Local_Fuel.T16()
        t7_1 = Dashboard_M12_Local_Fuel.T7()
        var_1 = divide(t16_1, t7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class U24():
    # 'Charts_Data_M12_Local_Fuel'!U24
    value = 0.180882870877
    formula = "=U16/'Dashboard M12 Local Fuel'!U$7"
    @eval_fn
    def U24():
        u16_1 = Charts_Data_M12_Local_Fuel.U16()
        u7_1 = Dashboard_M12_Local_Fuel.U7()
        var_1 = divide(u16_1, u7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class V24():
    # 'Charts_Data_M12_Local_Fuel'!V24
    value = 0.213069484807
    formula = "=V16/'Dashboard M12 Local Fuel'!V$7"
    @eval_fn
    def V24():
        v16_1 = Charts_Data_M12_Local_Fuel.V16()
        v7_1 = Dashboard_M12_Local_Fuel.V7()
        var_1 = divide(v16_1, v7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class W24():
    # 'Charts_Data_M12_Local_Fuel'!W24
    value = 0.234198029605
    formula = "=W16/'Dashboard M12 Local Fuel'!W$7"
    @eval_fn
    def W24():
        w16_1 = Charts_Data_M12_Local_Fuel.W16()
        w7_1 = Dashboard_M12_Local_Fuel.W7()
        var_1 = divide(w16_1, w7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class X24():
    # 'Charts_Data_M12_Local_Fuel'!X24
    value = "#DIV/0!"
    formula = "=X16/'Dashboard M12 Local Fuel'!X$7"
    @eval_fn
    def X24():
        x16_1 = Charts_Data_M12_Local_Fuel.X16()
        x7_1 = Dashboard_M12_Local_Fuel.X7()
        var_1 = divide(x16_1, x7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Y24():
    # 'Charts_Data_M12_Local_Fuel'!Y24
    value = "#DIV/0!"
    formula = "=Y16/'Dashboard M12 Local Fuel'!Y$7"
    @eval_fn
    def Y24():
        y16_1 = Charts_Data_M12_Local_Fuel.Y16()
        y7_1 = Dashboard_M12_Local_Fuel.Y7()
        var_1 = divide(y16_1, y7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class Z24():
    # 'Charts_Data_M12_Local_Fuel'!Z24
    value = "#DIV/0!"
    formula = "=Z16/'Dashboard M12 Local Fuel'!Z$7"
    @eval_fn
    def Z24():
        z16_1 = Charts_Data_M12_Local_Fuel.Z16()
        z7_1 = Dashboard_M12_Local_Fuel.Z7()
        var_1 = divide(z16_1, z7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AA24():
    # 'Charts_Data_M12_Local_Fuel'!AA24
    value = "#DIV/0!"
    formula = "=AA16/'Dashboard M12 Local Fuel'!AA$7"
    @eval_fn
    def AA24():
        aa16_1 = Charts_Data_M12_Local_Fuel.AA16()
        aa7_1 = Dashboard_M12_Local_Fuel.AA7()
        var_1 = divide(aa16_1, aa7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AB24():
    # 'Charts_Data_M12_Local_Fuel'!AB24
    value = "#DIV/0!"
    formula = "=AB16/'Dashboard M12 Local Fuel'!AB$7"
    @eval_fn
    def AB24():
        ab16_1 = Charts_Data_M12_Local_Fuel.AB16()
        ab7_1 = Dashboard_M12_Local_Fuel.AB7()
        var_1 = divide(ab16_1, ab7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AC24():
    # 'Charts_Data_M12_Local_Fuel'!AC24
    value = "#DIV/0!"
    formula = "=AC16/'Dashboard M12 Local Fuel'!AC$7"
    @eval_fn
    def AC24():
        ac16_1 = Charts_Data_M12_Local_Fuel.AC16()
        ac7_1 = Dashboard_M12_Local_Fuel.AC7()
        var_1 = divide(ac16_1, ac7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AD24():
    # 'Charts_Data_M12_Local_Fuel'!AD24
    value = "#DIV/0!"
    formula = "=AD16/'Dashboard M12 Local Fuel'!AD$7"
    @eval_fn
    def AD24():
        ad16_1 = Charts_Data_M12_Local_Fuel.AD16()
        ad7_1 = Dashboard_M12_Local_Fuel.AD7()
        var_1 = divide(ad16_1, ad7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AE24():
    # 'Charts_Data_M12_Local_Fuel'!AE24
    value = "#DIV/0!"
    formula = "=AE16/'Dashboard M12 Local Fuel'!AE$7"
    @eval_fn
    def AE24():
        ae16_1 = Charts_Data_M12_Local_Fuel.AE16()
        ae7_1 = Dashboard_M12_Local_Fuel.AE7()
        var_1 = divide(ae16_1, ae7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AF24():
    # 'Charts_Data_M12_Local_Fuel'!AF24
    value = "#DIV/0!"
    formula = "=AF16/'Dashboard M12 Local Fuel'!AF$7"
    @eval_fn
    def AF24():
        af16_1 = Charts_Data_M12_Local_Fuel.AF16()
        af7_1 = Dashboard_M12_Local_Fuel.AF7()
        var_1 = divide(af16_1, af7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AG24():
    # 'Charts_Data_M12_Local_Fuel'!AG24
    value = "#DIV/0!"
    formula = "=AG16/'Dashboard M12 Local Fuel'!AG$7"
    @eval_fn
    def AG24():
        ag16_1 = Charts_Data_M12_Local_Fuel.AG16()
        ag7_1 = Dashboard_M12_Local_Fuel.AG7()
        var_1 = divide(ag16_1, ag7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AH24():
    # 'Charts_Data_M12_Local_Fuel'!AH24
    value = "#DIV/0!"
    formula = "=AH16/'Dashboard M12 Local Fuel'!AH$7"
    @eval_fn
    def AH24():
        ah16_1 = Charts_Data_M12_Local_Fuel.AH16()
        ah7_1 = Dashboard_M12_Local_Fuel.AH7()
        var_1 = divide(ah16_1, ah7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AI24():
    # 'Charts_Data_M12_Local_Fuel'!AI24
    value = "#DIV/0!"
    formula = "=AI16/'Dashboard M12 Local Fuel'!AI$7"
    @eval_fn
    def AI24():
        ai16_1 = Charts_Data_M12_Local_Fuel.AI16()
        ai7_1 = Dashboard_M12_Local_Fuel.AI7()
        var_1 = divide(ai16_1, ai7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AJ24():
    # 'Charts_Data_M12_Local_Fuel'!AJ24
    value = "#DIV/0!"
    formula = "=AJ16/'Dashboard M12 Local Fuel'!AJ$7"
    @eval_fn
    def AJ24():
        aj16_1 = Charts_Data_M12_Local_Fuel.AJ16()
        aj7_1 = Dashboard_M12_Local_Fuel.AJ7()
        var_1 = divide(aj16_1, aj7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AK24():
    # 'Charts_Data_M12_Local_Fuel'!AK24
    value = "#DIV/0!"
    formula = "=AK16/'Dashboard M12 Local Fuel'!AK$7"
    @eval_fn
    def AK24():
        ak16_1 = Charts_Data_M12_Local_Fuel.AK16()
        ak7_1 = Dashboard_M12_Local_Fuel.AK7()
        var_1 = divide(ak16_1, ak7_1)
        return var_1

@register(Charts_Data_M12_Local_Fuel)
class AL24():
    # 'Charts_Data_M12_Local_Fuel'!AL24
    value = "#DIV/0!"
    formula = "=AL16/'Dashboard M12 Local Fuel'!AL$7"
    @eval_fn
    def AL24():
        al16_1 = Charts_Data_M12_Local_Fuel.AL16()
        al7_1 = Dashboard_M12_Local_Fuel.AL7()
        var_1 = divide(al16_1, al7_1)
        return var_1